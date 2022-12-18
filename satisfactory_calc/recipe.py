from typing import Final

from .define import Building, Item, Ingredients, Liquid
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
    Ingredients.iron_ore:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.iron_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.iron_ingot:
    Recipe(
        RecipeIO(Ingredients.iron_ore, 30),
        RecipeIO(Ingredients.iron_ingot, 30),
        Building.smelter,
    ),
    Ingredients.iron_plate:
    Recipe(
        RecipeIO(Ingredients.iron_ingot, 30),
        RecipeIO(Ingredients.iron_plate, 20),
        Building.constructor,
    ),
    Ingredients.iron_rod:
    Recipe(
        RecipeIO(Ingredients.iron_ingot, 15),
        RecipeIO(Ingredients.iron_rod, 15),
        Building.constructor,
    ),
    Ingredients.screw:
    Recipe(
        RecipeIO(Ingredients.iron_rod, 10),
        RecipeIO(Ingredients.screw, 40),
        Building.constructor,
    ),
                                                                                                # Copper
    Ingredients.copper_ore:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.copper_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.copper_ingot:
    Recipe(
        RecipeIO(Ingredients.copper_ore, 30),
        RecipeIO(Ingredients.copper_ingot, 30),
        Building.constructor,
    ),
                                                                                                # Raw Quartz
    Ingredients.raw_quartz:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.raw_quartz, 240),
        Building.miner_mk3,
    ),
    Ingredients.quartz_crystal:
    Recipe(
        RecipeIO(Ingredients.raw_quartz, 37.5),
        RecipeIO(Ingredients.quartz_crystal, 22.5),
        Building.constructor,
    ),
    Ingredients.silica:
    Recipe(
        RecipeIO(Ingredients.raw_quartz, 22.5),
        RecipeIO(Ingredients.silica, 37.5),
        Building.constructor,
    ),
                                                                                                # Caterium
    Ingredients.caterium_ore:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.caterium_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.caterium_ingot:
    Recipe(
        RecipeIO(Ingredients.caterium_ore, 45),
        RecipeIO(Ingredients.caterium_ingot, 15),
        Building.smelter,
    ),
    alternate(Ingredients.caterium_ingot):
    Recipe(
        RecipeIO(Ingredients.caterium_ore, 24).add_item(Liquid.water, 24),
        RecipeIO(Ingredients.caterium_ingot, 12),
        Building.smelter,
    ),
    Ingredients.quickwire:
    Recipe(
        RecipeIO(Ingredients.caterium_ingot, 12),
        RecipeIO(Ingredients.quickwire, 60),
        Building.constructor,
    ),
    alternate(Ingredients.quickwire):
    Recipe(
        RecipeIO(Ingredients.caterium_ingot, 7.5).add_item(Ingredients.copper_ingot, 37.5),
        RecipeIO(Ingredients.quickwire, 90),
        Building.constructor,
    ),
                                                                                                # Sulfur
    Ingredients.sulfur:
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.sulfur, 240),
        Building.miner_mk3,
    ),
    Ingredients.black_powder:
    Recipe(
        RecipeIO(Ingredients.coal, 15).add_item(Ingredients.sulfur, 15),
        RecipeIO(Ingredients.black_powder, 30),
        Building.assembler,
    ),
    Ingredients.compacted_coal:
    Recipe(
        RecipeIO(Ingredients.coal, 25).add_item(Ingredients.sulfur, 25),
        RecipeIO(Ingredients.compacted_coal, 25),
        Building.assembler,
    ),
                                                                                                # Liquid
    Liquid.water:
    Recipe(
        RecipeIO(),
        RecipeIO(Liquid.water, 120),
        Building.water_extractor,
    ),
    Liquid.crude_oil:
    Recipe(
        RecipeIO(),
        RecipeIO(Liquid.crude_oil, 120),
        Building.oil_extractor,
    ),
    Liquid.sulfuric_acid:
    Recipe(
        RecipeIO(Ingredients.sulfur, 50).add_item(Liquid.water, 50),
        RecipeIO(Liquid.sulfuric_acid, 50),
        Building.refinery,
    ),
                                                                                                # Nuclear power
}
