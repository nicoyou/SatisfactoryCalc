from typing import Final

from .define import Building, Item
from .sf_calc import Recipe, RecipeIO


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
                                                                                                                                                                 # Raw Quartz
    Item.raw_quartz: Recipe(RecipeIO(), RecipeIO(Item.raw_quartz, 780), Building.miner_mk3),
    Item.quartz_crystal: Recipe(RecipeIO(Item.raw_quartz, 37.5), RecipeIO(Item.quartz_crystal, 22.5), Building.constructor),
    Item.silica: Recipe(RecipeIO(Item.raw_quartz, 22.5), RecipeIO(Item.silica, 37.5), Building.constructor),
                                                                                                                                                                 # Caterium
    Item.caterium_ore: Recipe(RecipeIO(), RecipeIO(Item.caterium_ore, 780), Building.miner_mk3),
    Item.caterium_ingot: Recipe(RecipeIO(Item.caterium_ore, 45), RecipeIO(Item.caterium_ingot, 15), Building.smelter),
    alternate(Item.caterium_ingot): Recipe(RecipeIO(Item.caterium_ore, 24).add_item(Item.water, 24), RecipeIO(Item.caterium_ingot, 12), Building.smelter),
    Item.quickwire: Recipe(RecipeIO(Item.caterium_ingot, 12), RecipeIO(Item.quickwire, 60), Building.constructor),
    alternate(Item.quickwire): Recipe(RecipeIO(Item.caterium_ingot, 7.5).add_item(Item.copper_ingot, 37.5), RecipeIO(Item.quickwire, 90), Building.constructor),
                                                                                                                                                                 # Sulfur
    Item.sulfur: Recipe(RecipeIO(), RecipeIO(Item.sulfur, 780), Building.miner_mk3),
    Item.black_powder: Recipe(RecipeIO(Item.coal, 15).add_item(Item.sulfur, 15), RecipeIO(Item.black_powder, 30), Building.assembler),
    Item.compacted_coal: Recipe(RecipeIO(Item.coal, 25).add_item(Item.sulfur, 25), RecipeIO(Item.compacted_coal, 25), Building.assembler),
                                                                                                                                                                 # Liquid
    Item.water: Recipe(RecipeIO(), RecipeIO(Item.water, 120), Building.water_extractor),
    Item.crude_oil: Recipe(RecipeIO(), RecipeIO(Item.crude_oil, 120), Building.oil_extractor),
    Item.sulfuric_acid: Recipe(RecipeIO(Item.sulfur, 50).add_item(Item.water, 50), RecipeIO(Item.sulfuric_acid, 50), Building.refinery),
                                                                                                                                                                 # Nuclear power
}
