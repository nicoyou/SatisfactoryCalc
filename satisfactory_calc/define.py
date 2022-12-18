import nlib3


class Item(nlib3.StrEnum):
    # Iron
    iron_ore = "Iron Ore"
    iron_ingot = "Iron Ingot"
    iron_plate = "Iron Plate"
    iron_rod = "Iron Rod"
    screw = "screw"
    # Copper
    copper_ore = "Copper Ore"
    copper_ingot = "Copper Ingot"
    # Caterium
    caterium_ore = "Caterium Ore"
    caterium_ingot = "Caterium Ingot"
    quickwire = "Quickwire"
    # Nuclear power
    uranium = "Uranium"
    encased_uranium_cell = "Encased Uranium Cell"
    # Liquid
    water = "Water"


class Building(nlib3.StrEnum):
    miner_mk1 = "Miner Mk.1"
    miner_mk2 = "Miner Mk.2"
    miner_mk3 = "Miner Mk.3"
    smelter = "Smelter"             # 製錬炉
    constructor = "Constructor"     # 製作機
    assembler = "Assembler"         # 組立機
    Manufacturer = "Manufacturer"   # 製造機
    pump = "Pump"                   # 揚水ポンプ
    othre = "othre"
