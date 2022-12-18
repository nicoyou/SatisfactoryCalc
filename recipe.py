from typing import Final

from define import Building, Item
from sf_calc import Recipe, RecipeIO


def alternate(product: Item, num: int = 1) -> str:
    """代替レシピのキーを生成する

    Args:
        product: 元のアイテム名
        num: 代替レシピの番号 ( n番目 )

    Returns:
        キー
    """
    return f"alternate{num}_{product}"


RECIPE: Final[dict[str | Item, Recipe]] = {
                                                                                                                                                                 # Iron
    Item.iron_ore: Recipe(RecipeIO(), RecipeIO(Item.iron_ore, 780), Building.miner_mk3),
    Item.iron_ingot: Recipe(RecipeIO(Item.iron_ore, 30), RecipeIO(Item.iron_ingot, 30), Building.smelter),
    Item.iron_plate: Recipe(RecipeIO(Item.iron_ingot, 30), RecipeIO(Item.iron_plate, 20), Building.constructor),
    Item.iron_rod: Recipe(RecipeIO(Item.iron_ingot, 15), RecipeIO(Item.iron_rod, 15), Building.constructor),
    Item.screw: Recipe(RecipeIO(Item.iron_rod, 10), RecipeIO(Item.screw, 40), Building.constructor),
                                                                                                                                                                 # Copper
    Item.copper_ore: Recipe(RecipeIO(), RecipeIO(Item.copper_ore, 780), Building.miner_mk3),
    Item.copper_ingot: Recipe(RecipeIO(Item.copper_ore, 30), RecipeIO(Item.copper_ingot, 30), Building.constructor),
                                                                                                                                                                 # Caterium
    Item.caterium_ore: Recipe(RecipeIO(), RecipeIO(Item.caterium_ore, 780), Building.miner_mk3),
    Item.caterium_ingot: Recipe(RecipeIO(Item.caterium_ore, 45), RecipeIO(Item.caterium_ingot, 15), Building.smelter),
    alternate(Item.caterium_ingot): Recipe(RecipeIO(Item.caterium_ore, 24).add_item(Item.water, 24), RecipeIO(Item.caterium_ingot, 12), Building.smelter),
    Item.quickwire: Recipe(RecipeIO(Item.caterium_ingot, 12), RecipeIO(Item.quickwire, 60), Building.constructor),
    alternate(Item.quickwire): Recipe(RecipeIO(Item.caterium_ingot, 7.5).add_item(Item.copper_ingot, 37.5), RecipeIO(Item.quickwire, 90), Building.constructor),
                                                                                                                                                                 # Liquid
    Item.water: Recipe(RecipeIO(), RecipeIO(Item.water, 240), Building.pump),
}
