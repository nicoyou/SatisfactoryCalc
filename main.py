import sf_calc
import recipe
from define import Item

root_node_screw = sf_calc.RecipeNode(recipe.RECIPE[Item.screw])
node_iron_rod = sf_calc.RecipeNode(recipe.RECIPE[Item.iron_rod], parent=root_node_screw)
node_iron_ingot = sf_calc.RecipeNode(recipe.RECIPE[Item.iron_ingot], parent=node_iron_rod)
node_iron_ore = sf_calc.RecipeNode(recipe.RECIPE[Item.iron_ore], parent=node_iron_ingot)

print(root_node_screw)
print(root_node_screw.get_recipe_tree_str())
