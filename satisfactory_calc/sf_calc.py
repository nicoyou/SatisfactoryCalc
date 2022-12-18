from pathlib import Path

import nlib3

from .define import Building, Item


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
    def __init__(self, in_items: RecipeIO, out_items: RecipeIO, building: Building) -> None:
        self.in_items = in_items
        self.out_items = out_items
        self.building = building
        return

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
        self.input_recipe_node = {}
        self.main_item = main_item
        if parent is not None:
            parent.add_input_recipe(self)
        return

    def add_input_recipe(self, recipe_node) -> bool:
        for out_item in recipe_node.recipe.out_items.get_item_names():
            if out_item in self.recipe.in_items.get_item_names():
                self.input_recipe_node[out_item] = recipe_node
                return True
        nlib3.print_error_log("指定されたレシピが正しくありません")
        return False

    def get_out_speed_pm_from_main(self, item: Item) -> float | None:
        for out_item, out_speed_pm in self.recipe.out_items.get_items():
            if out_item == item:                                                                            # 要求されたアイテムと同じなら
                if self.main_item:                                                                          # 入力アイテムがなければ
                    return out_speed_pm
                else:
                    for in_item, in_speed_pm in self.recipe.in_items.get_items():                           # 全ての入力アイテム
                        if in_item in self.input_recipe_node:                                               # 必要な入力アイテムの前ノードが存在すれば
                            result = self.input_recipe_node[in_item].get_out_speed_pm_from_main(in_item)    # このレシピに渡される in_item の数
                            if result:
                                return (result / in_speed_pm) * out_speed_pm
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
        for out_item, out_speed_pm in self.recipe.out_items.get_items():
            if out_item == item:                                                                                    # 要求されたアイテムと同じなら
                if not self.recipe.in_items:                                                                        # 入力アイテムがなければ
                    result_out_speed_pm = out_speed_pm
                    machines = 1
                else:
                    for in_item, in_speed_pm in self.recipe.in_items.get_items():                                   # 全ての入力アイテム
                        if in_item in self.input_recipe_node:                                                       # 必要な入力アイテムの前ノードが存在すれば
                            result = self.input_recipe_node[in_item].get_info(in_item)[0]                           # このレシピに渡される in_item の数
                            if result:
                                machines_temp = result / in_speed_pm
                                result_out_speed_pm_temp = machines_temp * out_speed_pm
                                if result_out_speed_pm is None or result_out_speed_pm < result_out_speed_pm_temp:   # 1つ目の input アイテムか、それ移行で今までのインプットアイテム量より効率が良ければ
                                    machines = machines_temp
                                    result_out_speed_pm = result_out_speed_pm_temp
        return (result_out_speed_pm, machines)

    def get_recipe_tree_str(self) -> str:
        result = "("
        for item_name, speed_pm in self.recipe.out_items.get_items():
            info_result = self.get_info(item_name)
            result += f"{{item: {item_name}, out: {info_result[0]}, machines: {info_result[1]}}}, "
        result = result[:-2]
        result += ")"
        if self.input_recipe_node:
            result += "  ←  "
            for row in self.input_recipe_node.values():
                result += row.get_recipe_tree_str()
        return result

    def __str__(self) -> str:
        result = "("
        for row in self.recipe.out_items.get_item_names():
            result += f"{row}, "
        result = result[:-2]
        result += ")"
        if self.input_recipe_node:
            result += "  ←  "
            for i, row in enumerate(self.input_recipe_node.values()):
                if len(row.input_recipe_node) >= 1:     # 入力素材の入力素材が一つ以上あれば
                    if i == len(self.input_recipe_node) - 1:
                        result += "[" + str(row) + "]"
                    else:
                        result += "[" + str(row) + "], "
                else:
                    result += str(row)
        return result
