import satisfactory_calc as sf_calc
from satisfactory_calc import RECIPE, Ingredients, Liquid, Purity

# ネジの生産ライン
root_node_screw = sf_calc.RecipeNode(RECIPE[Ingredients.screw].with_clock_speed(2))
node_iron_rod = sf_calc.RecipeNode(RECIPE[Ingredients.iron_rod], parent=root_node_screw)
node_iron_ingot = sf_calc.RecipeNode(RECIPE[Ingredients.iron_ingot], parent=node_iron_rod)
node_iron_ore = sf_calc.RecipeNode(RECIPE[Ingredients.iron_ore].with_purity(Purity.pure).with_clock_speed(2.5), parent=node_iron_ingot)

print(root_node_screw)
print(root_node_screw.detailed_recipe_tree_dumps())
print("-" * 30)
#
#
#
# ケーブルを生成するトップノード
root_node_cable = sf_calc.RecipeNode(RECIPE[Ingredients.cable])
# ケーブル以下のノードを基本レシピで生成する
root_node_cable.automatic_node_generation()
print(root_node_cable.detailed_recipe_tree_dumps())

# 銅の原石のノードを取得する
copper_ore_node = root_node_cable.get_input_nodes(Ingredients.wire)[0].get_input_nodes(Ingredients.copper_ingot)[0].get_input_nodes(Ingredients.copper_ore)[0]
# 銅の原石のノードに設定されているレシピを上書きする
copper_ore_node.recipe = copper_ore_node.recipe.with_purity(Purity.pure).with_clock_speed(2.5)
print(root_node_cable.detailed_recipe_tree_dumps())

# さらに銅の原石のノードを追加する
sf_calc.RecipeNode(RECIPE[Ingredients.copper_ore].with_purity(Purity.impure),
                   parent=root_node_cable.get_input_nodes(Ingredients.wire)[0].get_input_nodes(Ingredients.copper_ingot)[0])
print(root_node_cable.detailed_recipe_tree_dumps())
print("-" * 30)
