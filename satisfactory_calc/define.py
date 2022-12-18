import enum

import nlib3


class Item(nlib3.StrEnum):
    # Coal
    coal = "Coal"
    # Iron
    iron_ore = "Iron Ore"
    iron_ingot = "Iron Ingot"
    iron_plate = "Iron Plate"
    iron_rod = "Iron Rod"
    screw = "screw"
    # Copper
    copper_ore = "Copper Ore"
    copper_ingot = "Copper Ingot"
    # Raw Quartz
    raw_quartz = "Raw Quartz"
    quartz_crystal = "Quartz Crystal"
    silica = "Silica"
    # Caterium
    caterium_ore = "Caterium Ore"
    caterium_ingot = "Caterium Ingot"
    quickwire = "Quickwire"
    # Sulfur
    sulfur = "Sulfur"
    black_powder = "Black Powder"
    compacted_coal = "Compacted Coal"
    # Liquid
    water = "Water"
    crude_oil = "Crude Oil"
    sulfuric_acid = "Sulfuric Acid"
    # Nuclear power
    uranium = "Uranium"
    encased_uranium_cell = "Encased Uranium Cell"


class Building(nlib3.StrEnum):
    miner_mk1 = "Miner Mk.1"
    miner_mk2 = "Miner Mk.2"
    miner_mk3 = "Miner Mk.3"
    smelter = "Smelter"                     # 製錬炉
    constructor = "Constructor"             # 製作機
    assembler = "Assembler"                 # 組立機
    Manufacturer = "Manufacturer"           # 製造機
    water_extractor = "Water Extractor"     # 揚水ポンプ
    oil_extractor = "Oil Extractor"         # 原油抽出機
    refinery = "Refinery"                   # 精製施設
    othre = "othre"




class Purity(float, enum.Enum):
    """純度"""
    impure = 0.5
    normal = 1
    pure = 2
