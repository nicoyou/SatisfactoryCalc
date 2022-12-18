from pathlib import Path

import nlib3

from . import define
from .define import Building, Item, Ingredients, Liquid, Gas, Purity


class RecipeIO():
    def __init__(self, item: Item | None = None, speed_pm: float | None = None) -> None:
        self.items = []
        if item is not None and speed_pm is not None:
            self.add_item(item, speed_pm)
        return

    def add_item(self, item: Item, speed_pm: float):
        self.items.append((item, speed_pm))
        return self

    def get_items(self) -> tuple:
        return tuple(self.items)

    def get_item_names(self) -> tuple:
        return tuple([row[0] for row in self.items])

    @staticmethod
    def from_items(item_list):
        cls = RecipeIO()
        for row in item_list:
            cls.add_item(row[0], row[1])
        return cls

    def __len__(self):
        return len(self.items)


class Recipe():
    def __init__(self, in_items: RecipeIO, out_items: RecipeIO, building: Building, clock_speed: float = 1, purity: Purity = Purity.normal) -> None:
        self.in_items = in_items
        self.out_items = out_items
        self.building = building
        self.clock_speed = clock_speed
        self.purity = purity
        if self.purity != Purity.normal and len(self.in_items) != 0:
            nlib3.print_error_log("入力アイテムの設定されているレシピに資源ノードの純度を設定することはできません")
        return

    def with_clock_speed(self, clock_speed: float):
        return self.__class__(self.in_items, self.out_items, self.building, clock_speed, self.purity)

    def with_purity(self, purity: Purity):
        return self.__class__(self.in_items, self.out_items, self.building, self.clock_speed, purity)

    def get_in_items(self) -> tuple:
        return tuple([(item_name, speed_pm * self.clock_speed) for item_name, speed_pm in self.in_items.get_items()])

    def get_in_item_names(self) -> tuple:
        return self.in_items.get_item_names()

    def get_out_items(self) -> tuple:
        result = []
        for item_name, speed_pm in self.out_items.get_items():
            out_num = speed_pm * self.purity.value * self.clock_speed
            if type(item_name) is Ingredients and out_num > define.CONVEYOR_BELT_MAX:
                out_num = define.CONVEYOR_BELT_MAX
            elif (type(item_name) is Liquid or type(item_name) is Gas) and out_num > define.PIPE_MAX:
                out_num = define.PIPE_MAX
            result.append((item_name, out_num))
        return tuple(result)

    def get_out_item_names(self) -> tuple:
        return self.out_items.get_item_names()

    def get_out_item_speed_pm(self, item: Item):
        for item_name, speed_pm in self.get_out_items():
            if item == item_name:
                return speed_pm

    def to_dict(self) -> dict:
        result = {
            "in_item": self.in_items.get_items(),
            "out_item": self.out_items.get_items(),
            "building": self.building,
        }
        return result

    @staticmethod
    def from_dict(recipe_dict):
        return Recipe(RecipeIO.from_items(recipe_dict["in_item"]), RecipeIO.from_items(recipe_dict["out_item"]), recipe_dict["building"])


def save_recipe_list(file_path: str | Path, recipe_list: list[Recipe] | tuple[Recipe, ...]) -> None:
    recipe_dict_list = [row.to_dict() for row in recipe_list]
    nlib3.save_json(file_path, recipe_dict_list)
    return


def load_recipe_list(file_path: str | Path):
    recipe_dict_list = nlib3.load_json(file_path)
    return [Recipe.from_dict(row) for row in recipe_dict_list]


class RecipeNode():
    def __init__(self, recipe: Recipe, parent=None, main_item=False) -> None:
        self.recipe = recipe
        self.input_recipe_node_list = []
        self.main_item = main_item
        if parent is not None:
            parent.add_input_recipe(self)
        return

    def add_input_recipe(self, recipe_node) -> bool:
        for out_item in recipe_node.recipe.out_items.get_item_names():
            if out_item in self.recipe.in_items.get_item_names():
                self.input_recipe_node_list.append(recipe_node)
                return True
        nlib3.print_error_log("指定されたレシピが正しくありません")
        return False

    def get_out_machines_num_from_main(self) -> float | None:
        if self.main_item:                                                                                                    # 入力アイテムがなければ
            return 1
        else:
            for in_item, in_speed_pm in self.recipe.get_in_items():                                                           # 全ての入力アイテム
                input_node_speed_pm_list = []                                                                                 # 現在接続されている前ノードの出力アイテムと現在のノードの入力ノードが一致する出力速度
                for input_recipe_node in self.input_recipe_node_list:                                                         # 全ての前ノード
                    if in_item in input_recipe_node.recipe.get_out_item_names():
                        result = input_recipe_node.get_out_machines_num_from_main()                                           # 前ノードのレシピの出力から今回必要な素材を取得する
                        if result:                                                                                            # 前ノード以前にメインノードが存在すれば
                            input_node_speed_pm_list.append(result * input_recipe_node.recipe.get_out_item_speed_pm(in_item)) # このレシピに渡される in_item の数
                if input_node_speed_pm_list:                                                                                  # 一つでも入力される素材があれば
                    return ((sum(input_node_speed_pm_list)) / in_speed_pm)
        return None

    def get_info(self, item: Item) -> tuple[float | None, float | None]:
        """毎分生成されるアイテムの数を取得する

        Args:
            item: 複数個の出力が存在する可能性があるため、取得したいアイテムの種類を指定する

        Returns:
            アイテム数
        """
        result_out_speed_pm = None
        machines = None
        for out_item, out_speed_pm in self.recipe.get_out_items():
            if out_item == item:                                                # 要求されたアイテムと同じなら
                if not self.recipe.get_in_items():                              # 入力アイテムがなければ
                    result_out_speed_pm = out_speed_pm
                    machines = 1
                else:
                    for in_item, in_speed_pm in self.recipe.get_in_items():     # 全ての入力アイテム
                        input_node_speed_pm_list = []                           # 現在接続されている前ノードの出力アイテムと現在のノードの入力ノードが一致する出力速度
                        for input_recipe_node in self.input_recipe_node_list:   # 全ての前ノード
                            result = input_recipe_node.get_info(in_item)[0]     # このレシピに渡される in_item の数

                            if result:
                                input_node_speed_pm_list.append(result)                                         # このレシピに渡される in_item の数
                        if input_node_speed_pm_list:                                                            # 一つでも入力される素材があれば
                            machines_temp = sum(input_node_speed_pm_list) / in_speed_pm
                            result_out_speed_pm_temp = machines_temp * out_speed_pm
                            if result_out_speed_pm is None or result_out_speed_pm < result_out_speed_pm_temp:   # 1つ目の input アイテムか、それ移行で今までのインプットアイテム量より効率が良ければ
                                machines = machines_temp
                                result_out_speed_pm = result_out_speed_pm_temp
        return (result_out_speed_pm, machines)

    def detailed_recipe_tree_dumps(self) -> str:
        """詳細な情報を付加したレシピツリーを出力する

        Returns:
            レシピツリーの文字列
        """
        result = "("
        for item_name, speed_pm in self.recipe.get_out_items():
            info_result = self.get_info(item_name)
            result += f"{{item: {item_name}, out: {info_result[0]}, machines: {info_result[1]}}}, "
        result = result[:-2]
        result += ")"
        if self.input_recipe_node_list:
            result += "  ←  "
            for i, row in enumerate(self.input_recipe_node_list):
                if len(row.input_recipe_node_list) >= 1:    # 入力素材の入力素材が一つ以上あれば
                    if i == len(self.input_recipe_node_list) - 1:
                        result += "[" + row.detailed_recipe_tree_dumps() + "]"
                    else:
                        result += "[" + row.detailed_recipe_tree_dumps() + "], "
                else:
                    result += row.detailed_recipe_tree_dumps()
        return result

    def __str__(self) -> str:
        result = "("
        for row in self.recipe.get_out_item_names():
            result += f"{row}, "
        result = result[:-2]
        result += ")"
        if self.input_recipe_node_list:
            result += "  ←  "
            for i, row in enumerate(self.input_recipe_node_list):
                if len(row.input_recipe_node_list) >= 1:    # 入力素材の入力素材が一つ以上あれば
                    if i == len(self.input_recipe_node_list) - 1:
                        result += "[" + str(row) + "]"
                    else:
                        result += "[" + str(row) + "], "
                else:
                    result += str(row)
        return result
