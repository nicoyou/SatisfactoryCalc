import satisfactory_calc as sf_calc
from satisfactory_calc import RECIPE, Ingredients, Purity

root_node_screw = sf_calc.RecipeNode(RECIPE[Ingredients.screw])
node_iron_rod = sf_calc.RecipeNode(RECIPE[Ingredients.iron_rod], parent=root_node_screw)
node_iron_ingot = sf_calc.RecipeNode(RECIPE[Ingredients.iron_ingot], parent=node_iron_rod)
node_iron_ore = sf_calc.RecipeNode(RECIPE[Ingredients.iron_ore].with_purity(Purity.pure).with_clock_speed(2.5), parent=node_iron_ingot)

print(root_node_screw)
print(root_node_screw.get_recipe_tree_str())
