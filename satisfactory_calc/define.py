import enum

import nlib3

CONVEYOR_BELT_MAX = 780
PIPE_MAX = 600


class Item(nlib3.StrEnum):
    """アイテム"""


class Ingredients(Item):
    """材料"""
    # Limestone
    limestone = "Limestone"
    concrete = "Concrete"
    # Coal
    coal = "Coal"
    # Iron
    iron_ore = "Iron Ore"
    iron_ingot = "Iron Ingot"
    iron_plate = "Iron Plate"
    iron_rod = "Iron Rod"
    screw = "screw"
    # Steel Ingot
    steel_ingot = "Steel Ingot"
    steel_beam = "Steel Beam"
    steel_pipe = "Steel Pipe"
    encased_industrial_beam = "Encased Industrial Beam"
    # Copper
    copper_ore = "Copper Ore"
    copper_ingot = "Copper Ingot"
    copper_powder = "Copper Powder"
    copper_sheet = "Copper Sheet"
    wire = "Wire"
    cable = "Cable"
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
    # Nuclear power
    uranium = "Uranium"
    encased_uranium_cell = "Encased Uranium Cell"


class Liquid(Item):
    """液体の材料"""
    water = "Water"
    crude_oil = "Crude Oil"
    sulfuric_acid = "Sulfuric Acid"


class Gas(Item):
    """気体の材料"""


class Building(nlib3.StrEnum):
    """建物"""
    miner_mk1 = "Miner Mk.1"
    miner_mk2 = "Miner Mk.2"
    miner_mk3 = "Miner Mk.3"
    smelter = "Smelter"                     # 製錬炉
    foundry = "Foundry"                     # 鋳造所
    constructor = "Constructor"             # 製作機
    assembler = "Assembler"                 # 組立機
    manufacturer = "Manufacturer"           # 製造機
    water_extractor = "Water Extractor"     # 揚水ポンプ
    oil_extractor = "Oil Extractor"         # 原油抽出機
    refinery = "Refinery"                   # 精製施設
    blender = "Blender"                     # 混合機
    othre = "othre"


class Purity(float, enum.Enum):
    """純度"""
    impure = 0.5    # 低純度
    normal = 1      # 中純度
    pure = 2        # 高純度
