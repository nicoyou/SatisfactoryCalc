from typing import Final

from .define import Building, Item, Ingredients, Liquid, Gas
from .sf_calc import Recipe, RecipeIO


def alternate(product: Item, num: int = 1) -> str:
    """代替レシピのキーを生成する

    Args:
        product: 生成されるアイテム名
        num: 代替レシピの番号 ( n番目 )

    Returns:
        キー
    """
    return f"alternate{num}_{product}"


def byproduct(product: Item, num: int = 1) -> str:
    """副産物からレシピを探すためのサブキーを生成する

    Args:
        product: 生成される副産物のアイテム
        num: 副産物レシピの番号 ( n番目 )

    Returns:
        キー
    """
    return f"byproduct{num}_{product}"


RECIPE: Final[dict[str | Item, Recipe]] = {
    # Ore 鉱石
    Ingredients.iron_ore: # 鉄鉱石
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.iron_ore, 240),
        Building.miner_mk3,
    ),
        Ingredients.copper_ore: # 銅鉱石
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.copper_ore, 240),
        Building.miner_mk3,
    ),
    Ingredients.limestone: # 石灰岩
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.limestone, 240),
        Building.miner_mk3,
    ),
    Ingredients.coal: # 石炭
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.coal, 240),
        Building.miner_mk3,
    ),
        Ingredients.caterium_ore: # カテリウム鉱石
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.caterium_ore, 240),
        Building.miner_mk3,
    ),
        Ingredients.raw_quartz: # 未加工石英
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.raw_quartz, 240),
        Building.miner_mk3,
    ),
        Ingredients.sulfur: # 硫黄
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.sulfur, 240),
        Building.miner_mk3,
    ),
        Ingredients.bauxite: # ボーキサイト
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.bauxite, 240),
        Building.miner_mk3,
    ),
        Ingredients.uranium: # ウラン鉱石
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.uranium, 240),
        Building.miner_mk3,
    ),
            Ingredients.sam_ore: # SAM鉱石
    Recipe(
        RecipeIO(),
        RecipeIO(Ingredients.sam_ore, 240),
        Building.miner_mk3,
    ),

    # Mineral 鉱物
    Ingredients.concrete: # コンクリート
    Recipe(
        RecipeIO(Ingredients.limestone, 45),
        RecipeIO(Ingredients.concrete, 15),
        Building.constructor,
    ),
    alternate(Ingredients.concrete):
    Recipe(
        RecipeIO(Ingredients.limestone,50).add_item(Ingredients.rubber,10),
        RecipeIO(Ingredients.concrete,45),
        Building.assembler,
    ),
    alternate(Ingredients.concrete,2):
    Recipe(
        RecipeIO(Ingredients.limestone,120).add_item(Liquid.water,100),
        RecipeIO(Ingredients.concrete,80),
        Building.refinery,
    ),
    alternate(Ingredients.concrete,3):
    Recipe(
        RecipeIO(Ingredients.silica,7.5).add_item(Ingredients.limestone,30),
        RecipeIO(Ingredients.concrete,25),
        Building.assembler,
    ),
    alternate(Ingredients.concrete,4):
    Recipe(
        RecipeIO(Ingredients.raw_quartz,11.25).add_item(Ingredients.limestone,18.75),
        RecipeIO(Ingredients.concrete,26.25),
        Building.assembler,
    ),
    Ingredients.quartz_crystal: # 石英結晶
    Recipe(
        RecipeIO(Ingredients.raw_quartz,37.5),
        RecipeIO(Ingredients.quartz_crystal,22.5),
        Building.constructor,
    ),
    alternate(Ingredients.quartz_crystal):
    Recipe(
        RecipeIO(Ingredients.raw_quartz,67.5).add_item(Liquid.water,37.5),
        RecipeIO(Ingredients.quartz_crystal,52.5),
        Building.refinery,
    ),
    Ingredients.silica:
    Recipe(
        RecipeIO(Ingredients.raw_quartz,22.5),
        RecipeIO(Ingredients.silica,37.5),
        Building.constructor,
    ),
    alternate(Ingredients.silica):
    Recipe(
        RecipeIO(Ingredients.raw_quartz,11.25).add_item(Ingredients.limestone,18.75),
        RecipeIO(Ingredients.silica,26.25),
        Building.assembler,
    ),
    Ingredients.compacted_coal: # 圧縮石炭
    Recipe(
        RecipeIO(Ingredients.coal,25).add_item(Ingredients.sulfur,25),
        RecipeIO(Ingredients.compacted_coal,25),
        Building.assembler,
    ),
    Ingredients.copper_powder: # 銅粉
    Recipe(
        RecipeIO(Ingredients.copper_ingot,300),
        RecipeIO(Ingredients.copper_powder,50),
        Building.constructor,
    ),

    # The Expendables 消耗品
    Ingredients.gas_filter: # ガスフィルター
    Recipe(
        RecipeIO(Ingredients.coal,37.5).add_item(Ingredients.rubber,15).add_item(Ingredients.fabric,15),
        RecipeIO(Ingredients.gas_filter,7.5),
        Building.manufacturer,
    ),
    Ingredients.iodine_infused_filter: # ヨウ素注入フィルター
    Recipe(
        RecipeIO(Ingredients.gas_filter,3.75).add_item(Ingredients.quickwire,30).add_item(Ingredients.aluminum_casing,3.75),
        RecipeIO(Ingredients.iodine_infused_filter,3.75),
        Building.manufacturer,
    ),

    # Ammunition 弾薬
    Ingredients.black_powder: # 黒色火薬
    Recipe(
        RecipeIO(Ingredients.coal,15).add_item(Ingredients.sulfur,15),
        RecipeIO(Ingredients.black_powder,30),
        Building.assembler,
    ),
    alternate(Ingredients.black_powder):
    Recipe(
        RecipeIO(Ingredients.sulfur,7.5).add_item(Ingredients.compacted_coal,3.75),
        RecipeIO(Ingredients.black_powder,15),
        Building.assembler,
    ),
    Ingredients.smokeless_powder: # 無煙火薬
    Recipe(
        RecipeIO(Ingredients.black_powder,20).add_item(Liquid.heavy_oil_residue,10),
        RecipeIO(Ingredients.smokeless_powder,20),
        Building.refinery,
    ),
    Ingredients.iron_rebar: # 鉄筋
    Recipe(
        RecipeIO(Ingredients.iron_rod,15),
        RecipeIO(Ingredients.iron_rebar,15),
        Building.constructor,
    ),
    Ingredients.stun_rebar: # スタン鉄筋
    Recipe(
        RecipeIO(Ingredients.iron_rebar,10).add_item(Ingredients.quickwire,50),
        RecipeIO(Ingredients.stun_rebar,10),
        Building.assembler,
    ),
    Ingredients.shatter_rebar: # 破砕鉄筋
    Recipe(
        RecipeIO(Ingredients.iron_rebar,10).add_item(Ingredients.quartz_crystal,15),
        RecipeIO(Ingredients.shatter_rebar,5),
        Building.assembler,
    ),
    Ingredients.explosive_rebar: # 爆砕鉄筋
    Recipe(
        RecipeIO(Ingredients.iron_rebar,10).add_item(Ingredients.smokeless_powder,10).add_item(Ingredients.steel_pipe,10),
        RecipeIO(Ingredients.explosive_rebar,5),
        Building.manufacturer,
    ),
    Ingredients.nobelisk: # ノーベリスク
    Recipe(
        RecipeIO(Ingredients.steel_pipe,20).add_item(Ingredients.black_powder,20),
        RecipeIO(Ingredients.nobelisk,10),
        Building.assembler,
    ),
    Ingredients.gas_nobelisk: # ガス・ノーベリスク
    Recipe(
        RecipeIO(Ingredients.nobelisk,5).add_item(Ingredients.biomass,50),
        RecipeIO(Ingredients.gas_nobelisk,5),
        Building.assembler,
    ),
    Ingredients.cluster_nobelisk: # クラスター・ノーベリスク
    Recipe(
        RecipeIO(Ingredients.nobelisk,7.5).add_item(Ingredients.smokeless_powder,10),
        RecipeIO(Ingredients.cluster_nobelisk,2.5),
        Building.assembler,
    ),
    Ingredients.pulse_nobelisk: # パルス・ノーベリスク
    Recipe(
        RecipeIO(Ingredients.nobelisk,5).add_item(Ingredients.crystal_oscillator,1),
        RecipeIO(Ingredients.pulse_nobelisk,5),
        Building.assembler,
    ),
    Ingredients.nuke_nobelisk: # ニューク・ノーベリスク
    Recipe(
        RecipeIO(Ingredients.nobelisk,2.5).add_item(Ingredients.encased_uranium_cell,10).add_item(Ingredients.smokeless_powder,5).add_item(Ingredients.ai_limiter,3),
        RecipeIO(Ingredients.nuke_nobelisk,0.5),
        Building.manufacturer,
    ),
    Ingredients.rifle_ammo: # ライフル弾
    Recipe(
        RecipeIO(Ingredients.copper_sheet,15).add_item(Ingredients.smokeless_powder,10),
        RecipeIO(Ingredients.rifle_ammo,75),
        Building.assembler,
    ),
    Ingredients.homing_rifle_ammo: # ホーミングライフル弾
    Recipe(
        RecipeIO(Ingredients.rifle_ammo,50).add_item(Ingredients.high_speed_connector,2.5),
        RecipeIO(Ingredients.homing_rifle_ammo,25),
        Building.assembler,
    ),
    Ingredients.turbo_rifle_ammo: # ターボライフル弾
    Recipe(
        RecipeIO(Ingredients.rifle_ammo,125).add_item(Ingredients.aluminum_casing,15).add_item(Liquid.Turbofuel,15),
        RecipeIO(Ingredients.turbo_rifle_ammo,250),
        Building.blender,
    ),
    alternate(Ingredients.turbo_rifle_ammo):
    Recipe(
        RecipeIO(Ingredients.rifle_ammo,125).add_item(Ingredients.aluminum_casing,15).add_item(Ingredients.packaged_turbofuel,15),
        RecipeIO(Ingredients.turbo_rifle_ammo,250),
        Building.manufacturer,
    ),

    # Ingot インゴット
    Ingredients.iron_ingot: # 鉄のインゴット
    Recipe(
        RecipeIO(Ingredients.iron_ore,30),
        RecipeIO(Ingredients.iron_ingot,30),
        Building.smelter,
    ),
    alternate(Ingredients.iron_ingot):
    Recipe(
        RecipeIO(Ingredients.iron_ore,35).add_item(Liquid.water,20),
        RecipeIO(Ingredients.iron_ingot,65),
        Building.refinery,
    ),
    alternate(Ingredients.iron_ingot,2):
    Recipe(
        RecipeIO(Ingredients.iron_ore,20).add_item(Ingredients.copper_ore,20),
        RecipeIO(Ingredients.iron_ingot,50),
        Building.foundry,
    ),
    Ingredients.copper_ingot: # 銅のインゴット
    Recipe(
        RecipeIO(Ingredients.copper_ore,30),
        RecipeIO(Ingredients.copper_ingot,30),
        Building.smelter,
    ),
    alternate(Ingredients.copper_ingot):
    Recipe(
        RecipeIO(Ingredients.copper_ore,50).add_item(Ingredients.iron_ore,25),
        RecipeIO(Ingredients.copper_ingot,100),
        Building.foundry,
    ),
        alternate(Ingredients.copper_ingot,2):
    Recipe(
        RecipeIO(Ingredients.copper_ore,15).add_item(Liquid.water,10),
        RecipeIO(Ingredients.copper_ingot,37.5),
        Building.refinery,
    ),
    Ingredients.steel_ingot: # 鋼鉄のインゴット
    Recipe(
        RecipeIO(Ingredients.iron_ore,45).add_item(Ingredients.coal,45),
        RecipeIO(Ingredients.steel_ingot,45),
        Building.foundry,
    ),
    alternate(Ingredients.steel_ingot):
    Recipe(
        RecipeIO(Ingredients.iron_ore,75).add_item(Ingredients.petroleum_coke,75),
        RecipeIO(Ingredients.steel_ingot,100),
        Building.foundry,
    ),
    alternate(Ingredients.steel_ingot,2):
    Recipe(
        RecipeIO(Ingredients.iron_ore,22.5).add_item(Ingredients.compacted_coal,11.25),
        RecipeIO(Ingredients.steel_ingot,37.5),
        Building.foundry,
    ),
    alternate(Ingredients.steel_ingot,3):
    Recipe(
        RecipeIO(Ingredients.iron_ingot,40).add_item(Ingredients.coal,40),
        RecipeIO(Ingredients.steel_ingot,60),
        Building.foundry,
    ),
    Ingredients.caterium_ingot: # カテリウムのインゴット
    Recipe(
        RecipeIO(Ingredients.caterium_ore,45),
        RecipeIO(Ingredients.caterium_ingot,15),
        Building.smelter,
    ),
    alternate(Ingredients.caterium_ingot):
    Recipe(
        RecipeIO(Ingredients.caterium_ore,24).add_item(Liquid.water,24),
        RecipeIO(Ingredients.caterium_ingot,12),
        Building.refinery,
    ),
    Ingredients.aluminum_ingot:  # アルミのインゴット
    Recipe(
        RecipeIO(Ingredients.aluminum_scrap,90).add_item(Ingredients.silica,75),
        RecipeIO(Ingredients.aluminum_ingot,60),
        Building.foundry,
    ),
    alternate(Ingredients.aluminum_ingot):
    Recipe(
        RecipeIO(Ingredients.aluminum_scrap,60),
        RecipeIO(Ingredients.aluminum_ingot,30),
        Building.smelter,
    ),

    # Basic Parts 基本部品
    Ingredients.iron_plate: # 鉄板
    Recipe(
        RecipeIO(Ingredients.iron_ingot,30),
        RecipeIO(Ingredients.iron_plate,20),
        Building.constructor,
    ),
    alternate(Ingredients.iron_plate):
    Recipe(
        RecipeIO(Ingredients.iron_ingot,50).add_item(Ingredients.plastic,10),
        RecipeIO(Ingredients.iron_plate,75),
        Building.assembler,
    ),
    alternate(Ingredients.iron_plate,2):
    Recipe(
        RecipeIO(Ingredients.steel_ingot,7.5).add_item(Ingredients.plastic,5),
        RecipeIO(Ingredients.iron_plate,45),
        Building.assembler,
    ),
    Ingredients.iron_rod: # 鉄のロッド
    Recipe(
        RecipeIO(Ingredients.iron_ingot,15),
        RecipeIO(Ingredients.iron_rod,15),
        Building.constructor,
    ),
    alternate(Ingredients.iron_rod):
    Recipe(
        RecipeIO(Ingredients.steel_ingot,12),
        RecipeIO(Ingredients.iron_rod,48),
        Building.constructor,
    ),
    Ingredients.screw: # ネジ
    Recipe(
        RecipeIO(Ingredients.iron_rod,10),
        RecipeIO(Ingredients.screw,40),
        Building.constructor,
    ),
    alternate(Ingredients.screw):
    Recipe(
        RecipeIO(Ingredients.iron_ingot,12.5),
        RecipeIO(Ingredients.screw,50),
        Building.constructor,
    ),
    alternate(Ingredients.screw,2):
    Recipe(
        RecipeIO(Ingredients.steel_ingot,5),
        RecipeIO(Ingredients.screw,260),
        Building.constructor,
    ),
    Ingredients.reinforced_iron_plate: # 強化鉄板
    Recipe(
        RecipeIO(Ingredients.iron_plate,30).add_item(Ingredients.screw,60),
        RecipeIO(Ingredients.reinforced_iron_plate,5),
        Building.assembler,
    ),
    alternate(Ingredients.reinforced_iron_plate):
    Recipe(
        RecipeIO(Ingredients.iron_plate,11.25).add_item(Ingredients.rubber,3.75),
        RecipeIO(Ingredients.reinforced_iron_plate,3.75),
        Building.assembler,
    ),
    alternate(Ingredients.reinforced_iron_plate,2):
    Recipe(
        RecipeIO(Ingredients.iron_plate,90).add_item(Ingredients.screw,250),
        RecipeIO(Ingredients.reinforced_iron_plate,15),
        Building.assembler,
    ),
    alternate(Ingredients.reinforced_iron_plate,3):
    Recipe(
        RecipeIO(Ingredients.iron_plate,18.75).add_item(Ingredients.wire,37.5),
        RecipeIO(Ingredients.reinforced_iron_plate,5.625),
        Building.assembler,
    ),
    Ingredients.modular_frame: #　モジュラー・フレーム 
    Recipe(
        RecipeIO(Ingredients.reinforced_iron_plate,3).add_item(Ingredients.iron_rod,12),
        RecipeIO(Ingredients.modular_frame,2),
        Building.assembler,
    ),
    alternate(Ingredients.modular_frame):
    Recipe(
        RecipeIO(Ingredients.reinforced_iron_plate,7.5).add_item(Ingredients.screw,140),
        RecipeIO(Ingredients.modular_frame,5),
        Building.assembler,
    ),
    alternate(Ingredients.modular_frame,2):
    Recipe(
        RecipeIO(Ingredients.reinforced_iron_plate,2).add_item(Ingredients.steel_pipe,10),
        RecipeIO(Ingredients.modular_frame,3),
        Building.assembler,
    ),
    Ingredients.copper_sheet: # 銅のシート
    Recipe(
        RecipeIO(Ingredients.copper_ingot,20),
        RecipeIO(Ingredients.copper_sheet,10),
        Building.constructor,
    ),
    alternate(Ingredients.copper_sheet):
    Recipe(
        RecipeIO(Ingredients.copper_ingot,22.5).add_item(Liquid.water,22.5),
        RecipeIO(Ingredients.copper_sheet,22.5),
        Building.refinery,
    ),
    Ingredients.steel_beam: # 鋼梁
    Recipe(
        RecipeIO(Ingredients.steel_ingot,60),
        RecipeIO(Ingredients.steel_beam,15),
        Building.constructor,
    ),
    Ingredients.steel_pipe: # 鋼鉄のパイプ
    Recipe(
        RecipeIO(Ingredients.steel_ingot,30),
        RecipeIO(Ingredients.steel_pipe,20),
        Building.constructor,
    ),
    Ingredients.encased_industrial_beam:
    Recipe(
        RecipeIO(Ingredients.steel_beam,24).add_item(Ingredients.concrete,30),
        RecipeIO(Ingredients.encased_industrial_beam,6),
        Building.assembler,
    ),
    alternate(Ingredients.encased_industrial_beam):
    Recipe(
        RecipeIO(Ingredients.steel_pipe,28).add_item(Ingredients.concrete,20),
        RecipeIO(Ingredients.encased_industrial_beam,4),
        Building.assembler,
    ),
    Ingredients.heavy_modular_frame: # ヘビー・モジュラー・フレーム
    Recipe(
        RecipeIO(Ingredients.modular_frame,10).add_item(Ingredients.steel_pipe,30).add_item(Ingredients.encased_industrial_beam,10).add_item(Ingredients.screw,200),
        RecipeIO(Ingredients.heavy_modular_frame,2),
        Building.manufacturer,
    ),
    alternate(Ingredients.heavy_modular_frame):
    Recipe(
        RecipeIO(Ingredients.modular_frame,18.75).add_item(Ingredients.encased_industrial_beam,11.25).add_item(Ingredients.rubber,75).add_item(Ingredients.screw,390),
        RecipeIO(Ingredients.heavy_modular_frame,3.75),
        Building.manufacturer,
    ),
    alternate(Ingredients.heavy_modular_frame,2):
    Recipe(
        RecipeIO(Ingredients.modular_frame,7.5).add_item(Ingredients.encased_industrial_beam,9.375).add_item(Ingredients.steel_pipe,33.75).add_item(Ingredients.concrete,20.625),
        RecipeIO(Ingredients.heavy_modular_frame,2.8125),
        Building.manufacturer,
    ),
    Ingredients.alclad_aluminum_sheet: # アルクラッド・アルミシート
    Recipe(
        RecipeIO(Ingredients.aluminum_ingot,30).add_item(Ingredients.copper_ingot,10),
        RecipeIO(Ingredients.alclad_aluminum_sheet,30),
        Building.assembler,
    ),
    Ingredients.aluminum_casing: # アルミ筐体
    Recipe(
        RecipeIO(Ingredients.aluminum_ingot,90),
        RecipeIO(Ingredients.aluminum_casing,60),
        Building.constructor,
    ),
    alternate(Ingredients.aluminum_casing):
    Recipe(
        RecipeIO(Ingredients.aluminum_ingot,150).add_item(Ingredients.copper_ingot,75),
        RecipeIO(Ingredients.aluminum_casing,112.5),
        Building.assembler,
    ),

    # Electronics 電子機器
    Ingredients.wire: # ワイヤー
    Recipe(
        RecipeIO(Ingredients.copper_ingot,15),
        RecipeIO(Ingredients.wire,30),
        Building.constructor,
    ),
    alternate(Ingredients.wire):
    Recipe(
        RecipeIO(Ingredients.copper_ingot,12).add_item(Ingredients.caterium_ingot,3),
        RecipeIO(Ingredients.wire,90),
        Building.assembler,
    ),
    alternate(Ingredients.wire,2):
    Recipe(
        RecipeIO(Ingredients.iron_ingot,12.5),
        RecipeIO(Ingredients.wire,22.5),
        Building.constructor,
    ),
    alternate(Ingredients.wire,3):
    Recipe(
        RecipeIO(Ingredients.caterium_ingot,15),
        RecipeIO(Ingredients.wire,120),
        Building.constructor,
    ),
    Ingredients.cable: # ケーブル
    Recipe(
        RecipeIO(Ingredients.wire,60),
        RecipeIO(Ingredients.cable,30),
        Building.constructor,
    ),
    alternate(Ingredients.cable):
    Recipe(
        RecipeIO(Ingredients.wire,37.5).add_item(Liquid.heavy_oil_residue,15),
        RecipeIO(Ingredients.cable,67.5),
        Building.refinery,
    ),
    alternate(Ingredients.cable,2):
    Recipe(
        RecipeIO(Ingredients.wire,45).add_item(Ingredients.rubber,30),
        RecipeIO(Ingredients.cable,100),
        Building.assembler,
    ),
    alternate(Ingredients.cable,3):
    Recipe(
        RecipeIO(Ingredients.quickwire,7.5).add_item(Ingredients.rubber,5),
        RecipeIO(Ingredients.cable,27.5),
        Building.assembler,
    ),
    Ingredients.quickwire: # クイックワイヤー
    Recipe(
        RecipeIO(Ingredients.caterium_ingot,12),
        RecipeIO(Ingredients.quickwire,60),
        Building.constructor,
    ),
    alternate(Ingredients.quickwire):
    Recipe(
        RecipeIO(Ingredients.caterium_ingot,7.5).add_item(Ingredients.copper_ingot,37.5),
        RecipeIO(Ingredients.quickwire,90),
        Building.assembler,
    ),
    Ingredients.circuit_board: # 回路基盤
    Recipe(
        RecipeIO(Ingredients.copper_sheet,15).add_item(Ingredients.plastic,30),
        RecipeIO(Ingredients.circuit_board,7.5),
        Building.assembler,
    ),
    alternate(Ingredients.circuit_board):
    Recipe(
        RecipeIO(Ingredients.rubber,30).add_item(Ingredients.petroleum_coke,45),
        RecipeIO(Ingredients.circuit_board,5),
        Building.assembler,
    ),
    alternate(Ingredients.circuit_board,2):
    Recipe(
        RecipeIO(Ingredients.copper_sheet,27.5).add_item(Ingredients.silica,27.5),
        RecipeIO(Ingredients.circuit_board,12.5),
        Building.assembler,
    ),
    alternate(Ingredients.circuit_board,3):
    Recipe(
        RecipeIO(Ingredients.plastic,12.5).add_item(Ingredients.quickwire,37.5),
        RecipeIO(Ingredients.circuit_board,8.75),
        Building.assembler,
    ),
    Ingredients.ai_limiter: # AIリミッター
    Recipe(
        RecipeIO(Ingredients.copper_sheet,25).add_item(Ingredients.quickwire,100),
        RecipeIO(Ingredients.ai_limiter,5),
        Building.assembler,
    ),
    Ingredients.high_speed_connector: # 高速コネクター
    Recipe(
        RecipeIO(Ingredients.quickwire,210).add_item(Ingredients.cable,37.5).add_item(Ingredients.circuit_board,3.75),
        RecipeIO(Ingredients.high_speed_connector,3.75),
        Building.manufacturer,
    ),
    alternate(Ingredients.high_speed_connector):
    Recipe(
        RecipeIO(Ingredients.quickwire,90).add_item(Ingredients.silica,37.5).add_item(Ingredients.circuit_board,3),
        RecipeIO(Ingredients.high_speed_connector,3),
        Building.manufacturer,
    ),

    # Industrial Parts 産業用部品
    Ingredients.rotor: # ローター
    Recipe(
        RecipeIO(Ingredients.iron_rod,20).add_item(Ingredients.screw,100),
        RecipeIO(Ingredients.rotor,4),
        Building.assembler,
    ),
    alternate(Ingredients.rotor):
    Recipe(
        RecipeIO(Ingredients.copper_sheet,22.5).add_item(Ingredients.screw,195),
        RecipeIO(Ingredients.rotor,11.25),
        Building.assembler,
    ),
    alternate(Ingredients.rotor,2):
    Recipe(
        RecipeIO(Ingredients.steel_pipe,10).add_item(Ingredients.wire,30),
        RecipeIO(Ingredients.rotor,5),
        Building.assembler,
    ),
    Ingredients.stator: # 固定子
    Recipe(
        RecipeIO(Ingredients.steel_pipe,15).add_item(Ingredients.wire,40),
        RecipeIO(Ingredients.stator,5),
        Building.assembler,
    ),
    alternate(Ingredients.stator):
    Recipe(
        RecipeIO(Ingredients.steel_pipe,16).add_item(Ingredients.quickwire,60),
        RecipeIO(Ingredients.stator,8),
        Building.assembler,
    ),
    Ingredients.motor: # モーター
    Recipe(
        RecipeIO(Ingredients.rotor,10).add_item(Ingredients.stator,10),
        RecipeIO(Ingredients.motor,5),
        Building.assembler,
    ),
    alternate(Ingredients.motor):
    Recipe(
        RecipeIO(Ingredients.rotor,3.75).add_item(Ingredients.stator,3.75).add_item(Ingredients.crystal_oscillator,1.25),
        RecipeIO(Ingredients.motor,7.5),
        Building.manufacturer,
    ),
    alternate(Ingredients.motor,2):
    Recipe(
        RecipeIO(Ingredients.electromagnetic_control_rod,3.75).add_item(Ingredients.rotor,7.5),
        RecipeIO(Ingredients.motor,7.5),
        Building.assembler,
    ),
    Ingredients.heat_sink: # ヒートシンク
    Recipe(
        RecipeIO(Ingredients.alclad_aluminum_sheet,37.5).add_item(Ingredients.copper_sheet,22.5),
        RecipeIO(Ingredients.heat_sink,7.5),
        Building.assembler,
    ),
    alternate(Ingredients.heat_sink):
    Recipe(
        RecipeIO(Ingredients.aluminum_casing,30).add_item(Ingredients.rubber,30),
        RecipeIO(Ingredients.heat_sink,10),
        Building.assembler,
    ),
    Ingredients.turbo_motor: # ターボモーター
    Recipe(
        RecipeIO(Ingredients.cooling_system,7.5).add_item(Ingredients.radio_control_unit,3.75).add_item(Ingredients.motor,7.5).add_item(Ingredients.rubber,45),
        RecipeIO(Ingredients.turbo_motor,1.875),
        Building.manufacturer,
    ),
    alternate(Ingredients.turbo_motor):
    Recipe(
        RecipeIO(Ingredients.motor,6.5625).add_item(Ingredients.radio_control_unit,8.4375).add_item(Ingredients.electromagnetic_control_rod,4.6875).add_item(Ingredients.rotor,6.5625),
        RecipeIO(Ingredients.turbo_motor,2.8125),
        Building.manufacturer,
    ),
    alternate(Ingredients.turbo_motor,2):
    Recipe(
        RecipeIO(Ingredients.motor,7.5).add_item(Ingredients.pressure_conversion_cube,1.875).add_item(Ingredients.packaged_nitrogen_gas,45).add_item(Ingredients.stator,15),
        RecipeIO(Ingredients.turbo_motor,3.75),
        Building.manufacturer,
    ),
    Ingredients.battery: # バッテリー
    Recipe(
        RecipeIO(Liquid.sulfuric_acid,50).add_item(Liquid.alumina_solution,40).add_item(Ingredients.aluminum_casing,20),
        RecipeIO(Ingredients.battery,20).add_item(Liquid.water,30),
        Building.blender,
    ),
    alternate(Ingredients.battery):
    Recipe(
        RecipeIO(Ingredients.sulfur,45).add_item(Ingredients.alclad_aluminum_sheet,52.5).add_item(Ingredients.plastic,60).add_item(Ingredients.wire,90),
        RecipeIO(Ingredients.battery,30),
        Building.manufacturer,
    ),
    Ingredients.fused_modular_frame: # 溶融モジュラー・フレーム
    Recipe(
        RecipeIO(Ingredients.heavy_modular_frame,1.5).add_item(Ingredients.aluminum_casing,75).add_item(Gas.nitrogen_gas,37.5),
        RecipeIO(Ingredients.fused_modular_frame,1.5),
        Building.blender,
    ),
    alternate(Ingredients.fused_modular_frame):
    Recipe(
        RecipeIO(Ingredients.heavy_modular_frame,3).add_item(Ingredients.aluminum_ingot,150).add_item(Liquid.nitric_acid,24).add_item(Liquid.fuel,30),
        RecipeIO(Ingredients.fused_modular_frame,3),
        Building.blender,
    ),
    Ingredients.cooling_system: # 冷却システム
    Recipe(
        RecipeIO(Ingredients.heat_sink,12).add_item(Ingredients.rubber,12).add_item(Liquid.water,30).add_item(Gas.nitrogen_gas,150),
        RecipeIO(Ingredients.cooling_system,6),
        Building.blender,
    ),
    alternate(Ingredients.cooling_system):
    Recipe(
        RecipeIO(Ingredients.heat_sink,9.375).add_item(Ingredients.motor,1.875).add_item(Gas.nitrogen_gas,45),
        RecipeIO(Ingredients.cooling_system,3.75),
        Building.blender,
    ),

    # Communication 通信
    Ingredients.crystal_oscillator: # 水晶発振器
    Recipe(
        RecipeIO(Ingredients.quartz_crystal,18).add_item(Ingredients.cable,14).add_item(Ingredients.reinforced_iron_plate,2.5),
        RecipeIO(Ingredients.crystal_oscillator,1),
        Building.manufacturer,
    ),
    alternate(Ingredients.crystal_oscillator):
    Recipe(
        RecipeIO(Ingredients.quartz_crystal,18.75).add_item(Ingredients.rubber,13.125).add_item(Ingredients.ai_limiter,1.875),
        RecipeIO(Ingredients.crystal_oscillator,1.875),
        Building.manufacturer,
    ),
    Ingredients.computer: # コンピューター
    Recipe(
        RecipeIO(Ingredients.circuit_board,25).add_item(Ingredients.cable,22.5).add_item(Ingredients.plastic,45).add_item(Ingredients.screw,130),
        RecipeIO(Ingredients.computer,2.5),
        Building.manufacturer,
    ),
    alternate(Ingredients.computer):
    Recipe(
        RecipeIO(Ingredients.circuit_board,7.5).add_item(Ingredients.crystal_oscillator,2.8125),
        RecipeIO(Ingredients.computer,2.8125),
        Building.assembler,
    ),
    alternate(Ingredients.computer,2):
    Recipe(
        RecipeIO(Ingredients.circuit_board,26.25).add_item(Ingredients.quickwire,105).add_item(Ingredients.rubber,45),
        RecipeIO(Ingredients.computer,3.75),
        Building.manufacturer,
    ),
    Ingredients.supercomputer: # スーパーコンピューター
    Recipe(
        RecipeIO(Ingredients.computer,3.75).add_item(Ingredients.ai_limiter,3.75).add_item(Ingredients.high_speed_connector,5.625).add_item(Ingredients.plastic,52.5),
        RecipeIO(Ingredients.supercomputer,1.875),
        Building.manufacturer,
    ),
    alternate(Ingredients.supercomputer):
    Recipe(
        RecipeIO(Ingredients.radio_control_unit,9).add_item(Ingredients.cooling_system,9),
        RecipeIO(Ingredients.supercomputer,3),
        Building.assembler,
    ),
    alternate(Ingredients.supercomputer,2):
    Recipe(
        RecipeIO(Ingredients.computer,3.6).add_item(Ingredients.electromagnetic_control_rod,2.4).add_item(Ingredients.battery,24).add_item(Ingredients.wire,54),
        RecipeIO(Ingredients.supercomputer,2.4),
        Building.manufacturer,
    ),
    Ingredients.radio_control_unit: # 無線制御ユニット
    Recipe(
        RecipeIO(Ingredients.aluminum_casing,40).add_item(Ingredients.crystal_oscillator,1.25).add_item(Ingredients.computer,1.25),
        RecipeIO(Ingredients.radio_control_unit,2.5),
        Building.manufacturer,
    ),
    alternate(Ingredients.radio_control_unit):
    Recipe(
        RecipeIO(Ingredients.crystal_oscillator,1.5).add_item(Ingredients.circuit_board,15).add_item(Ingredients.aluminum_casing,90).add_item(Ingredients.rubber,45),
        RecipeIO(Ingredients.radio_control_unit,4.5),
        Building.manufacturer,
    ),
    alternate(Ingredients.radio_control_unit,2):
    Recipe(
        RecipeIO(Ingredients.heat_sink,15).add_item(Ingredients.high_speed_connector,7.5).add_item(Ingredients.quartz_crystal,45),
        RecipeIO(Ingredients.radio_control_unit,3.75),
        Building.manufacturer,
    ),

    # Petroleum Products 石油製品
    Ingredients.plastic: # プラスチック
    Recipe(
        RecipeIO(Liquid.crude_oil,30),
        RecipeIO(Ingredients.plastic,20).add_item(Liquid.heavy_oil_residue,10),
        Building.refinery,
    ),
    alternate(Ingredients.plastic):
    Recipe(
        RecipeIO(Ingredients.polymer_resin,60).add_item(Liquid.water,20),
        RecipeIO(Ingredients.plastic,20),
        Building.refinery,
    ),
    alternate(Ingredients.plastic,2):
    Recipe(
        RecipeIO(Ingredients.rubber,30).add_item(Liquid.fuel,30),
        RecipeIO(Ingredients.plastic,60),
        Building.refinery,
    ),
    Ingredients.rubber: # ゴム
    Recipe(
        RecipeIO(Liquid.crude_oil,30),
        RecipeIO(Ingredients.rubber,20).add_item(Liquid.heavy_oil_residue,20),
        Building.refinery,
    ),
    alternate(Ingredients.rubber):
    Recipe(
        RecipeIO(Ingredients.polymer_resin,40).add_item(Liquid.water,40),
        RecipeIO(Ingredients.rubber,20),
        Building.refinery,
    ),
    alternate(Ingredients.rubber,2):
    Recipe(
        RecipeIO(Ingredients.plastic,30).add_item(Liquid.fuel,30),
        RecipeIO(Ingredients.rubber,60),
        Building.refinery,
    ),
    Ingredients.petroleum_coke: # 石油コークス
    Recipe(
        RecipeIO(Liquid.heavy_oil_residue,40),
        RecipeIO(Ingredients.petroleum_coke,120),
        Building.refinery,
    ),
    Ingredients.polymer_resin: # 合成樹脂
    Recipe(
        RecipeIO(Liquid.crude_oil,60),
        RecipeIO(Ingredients.polymer_resin,130).add_item(Liquid.heavy_oil_residue,20),
        Building.refinery,
    ),

    # Advanced Refining 先進的な精製
    Ingredients.aluminum_scrap: # アルミのスクラップ
    Recipe(
        RecipeIO(Liquid.alumina_solution,240).add_item(Ingredients.coal,120),
        RecipeIO(Ingredients.aluminum_scrap,360).add_item(Liquid.water,120),
        Building.refinery,
    ),
    alternate(Ingredients.aluminum_scrap):
    Recipe(
        RecipeIO(Liquid.alumina_solution,180).add_item(Ingredients.petroleum_coke,60),
        RecipeIO(Ingredients.aluminum_scrap,300).add_item(Liquid.water,105),
        Building.refinery,
    ),
    alternate(Ingredients.aluminum_scrap,2):
    Recipe(
        RecipeIO(Ingredients.bauxite,150).add_item(Ingredients.coal,100).add_item(Liquid.sulfuric_acid,50).add_item(Liquid.water,60),
        RecipeIO(Ingredients.aluminum_scrap,300).add_item(Liquid.water,50),
        Building.blender,
    ),

    # Container 容器入り
    Ingredients.packaged_fuel: # 容器入り燃料
    Recipe(
        RecipeIO(Liquid.fuel,40).add_item(Ingredients.empty_canister,40),
        RecipeIO(Liquid.fuel,40),
        Building.packager,
    ),
    alternate(Ingredients.packaged_fuel):
    Recipe(
        RecipeIO(Liquid.heavy_oil_residue,30).add_item(Ingredients.packaged_water,60),
        RecipeIO(Liquid.fuel,60),
        Building.refinery,
    ),
    Ingredients.packaged_turbofuel: # 容器入りターボ燃料
    Recipe(
        RecipeIO(Liquid.Turbofuel,20).add_item(Ingredients.empty_canister,20),
        RecipeIO(Ingredients.packaged_turbofuel,20),
        Building.packager,
    ),
    Ingredients.packaged_liquid_biofuel: # 容器入り液体バイオ燃料
    Recipe(
        RecipeIO(Liquid.liquid_biofuel,40).add_item(Ingredients.empty_canister,40),
        RecipeIO(Ingredients.packaged_liquid_biofuel,40),
        Building.packager,
    ),
    Ingredients.packaged_heavy_oil_residue: # 容器入り廃重油
    Recipe(
        RecipeIO(Liquid.heavy_oil_residue,30).add_item(Ingredients.empty_canister,30),
        RecipeIO(Ingredients.packaged_heavy_oil_residue,30),
        Building.packager,
    ),
    Ingredients.packaged_oil: # 容器入り原油
    Recipe(
        RecipeIO(Liquid.crude_oil,30).add_item(Ingredients.empty_canister,30),
        RecipeIO(Ingredients.packaged_oil,30),
        Building.packager,
    ),
    Ingredients.packaged_water: # 容器入り水
    Recipe(
        RecipeIO(Liquid.water,60).add_item(Ingredients.empty_canister,60),
        RecipeIO(Ingredients.packaged_water,60),
        Building.packager,
    ),
    Ingredients.packaged_sulfuric_acid: # 容器入り硫酸
    Recipe(
        RecipeIO(Liquid.sulfuric_acid,40).add_item(Ingredients.empty_canister,40),
        RecipeIO(Ingredients.packaged_sulfuric_acid,40),
        Building.packager,
    ),
    Ingredients.packaged_nitrogen_gas: # 容器入り窒素ガス
    Recipe(
        RecipeIO(Gas.nitrogen_gas,240).add_item(Ingredients.empty_fluid_tank,60),
        RecipeIO(Ingredients.packaged_nitrogen_gas,60),
        Building.packager,
    ),
    Ingredients.packaged_nitric_acid: # 容器入り硝酸
    Recipe(
        RecipeIO(Liquid.nitric_acid,30).add_item(Ingredients.empty_fluid_tank,30),
        RecipeIO(Ingredients.packaged_nitric_acid,30),
        Building.packager,
    ),
    Ingredients.packaged_alumina_solution: # 容器入りアルミナ溶液
    Recipe(
        RecipeIO(Liquid.alumina_solution,120).add_item(Ingredients.empty_canister,120),
        RecipeIO(Ingredients.packaged_alumina_solution,120),
        Building.packager,
    ),

    # Storage 貯蔵庫
    Ingredients.empty_canister: # 空の容器
    Recipe(
        RecipeIO(Ingredients.plastic,30),
        RecipeIO(Ingredients.empty_canister,60),
        Building.constructor,
    ),
    alternate(Ingredients.empty_canister):
    Recipe(
        RecipeIO(Ingredients.steel_ingot,60),
        RecipeIO(Ingredients.empty_canister,40),
        Building.constructor,
    ),
    alternate(Ingredients.empty_canister,2):
    Recipe(
        RecipeIO(Ingredients.iron_plate,30).add_item(Ingredients.copper_sheet,15),
        RecipeIO(Ingredients.empty_canister,60),
        Building.assembler,
    ),
    Ingredients.empty_fluid_tank: # 空の液体タンク
    Recipe(
        RecipeIO(Ingredients.aluminum_ingot,60),
        RecipeIO(Ingredients.empty_fluid_tank,60),
        Building.constructor,
    ),
    Ingredients.pressure_conversion_cube: # 圧力変換キューブ
    Recipe(
        RecipeIO(Ingredients.fused_modular_frame,1).add_item(Ingredients.radio_control_unit,2),
        RecipeIO(Ingredients.pressure_conversion_cube,1),
        Building.assembler,
    ),

    # Nuclear Power 原子力
    Ingredients.electromagnetic_control_rod: # 電磁制御棒
    Recipe(
        RecipeIO(Ingredients.stator,6).add_item(Ingredients.ai_limiter,4),
        RecipeIO(Ingredients.electromagnetic_control_rod,4),
        Building.assembler,
    ),
    alternate(Ingredients.electromagnetic_control_rod):
    Recipe(
        RecipeIO(Ingredients.stator,8).add_item(Ingredients.high_speed_connector,4),
        RecipeIO(Ingredients.electromagnetic_control_rod,8),
        Building.assembler,
    ),
    Ingredients.encased_uranium_cell: # 被覆型ウラン・セル
    Recipe(
        RecipeIO(Ingredients.uranium,50).add_item(Ingredients.concrete,15).add_item(Liquid.sulfuric_acid,40),
        RecipeIO(Ingredients.encased_uranium_cell,25).add_item(Liquid.sulfuric_acid,10),
        Building.blender,
    ),
    alternate(Ingredients.encased_uranium_cell):
    Recipe(
        RecipeIO(Ingredients.uranium,25).add_item(Ingredients.silica,15).add_item(Ingredients.sulfur,25).add_item(Ingredients.quickwire,75),
        RecipeIO(Ingredients.encased_uranium_cell,20),
        Building.manufacturer,
    ),
    Ingredients.uranium_fuel_rod: # ウラン燃料棒
    Recipe(
        RecipeIO(Ingredients.encased_uranium_cell,20).add_item(Ingredients.encased_industrial_beam,1.2).add_item(Ingredients.electromagnetic_control_rod,2),
        RecipeIO(Ingredients.uranium_fuel_rod,0.4),
        Building.manufacturer,
    ),
    alternate(Ingredients.uranium_fuel_rod):
    Recipe(
        RecipeIO(Ingredients.encased_uranium_cell,20).add_item(Ingredients.electromagnetic_control_rod,2).add_item(Ingredients.crystal_oscillator,0.6).add_item(Ingredients.beacon,1.2),
        RecipeIO(Ingredients.uranium_fuel_rod,0.6),
        Building.manufacturer,
    ),
    Ingredients.uranium_waste: # ウラン廃棄物
    Recipe(
        RecipeIO(Ingredients.uranium_fuel_rod,0.2).add_item(Liquid.water,240),
        RecipeIO(Ingredients.uranium_waste,10),
        Building.nuclear_power_plant,
    ),
    Ingredients.non_fissile_uranium: # 非分裂性ウラン
    Recipe(
        RecipeIO(Ingredients.uranium_waste,37.5).add_item(Ingredients.silica,25).add_item(Liquid.nitric_acid,15).add_item(Liquid.sulfuric_acid,15),
        RecipeIO(Ingredients.non_fissile_uranium,50).add_item(Liquid.water,15),
        Building.blender,
    ),
    alternate(Ingredients.non_fissile_uranium):
    Recipe(
        RecipeIO(Ingredients.uranium,25).add_item(Ingredients.uranium_waste,25).add_item(Liquid.nitric_acid,15).add_item(Liquid.sulfuric_acid,25),
        RecipeIO(Ingredients.non_fissile_uranium,100).add_item(Liquid.water,40),
        Building.blender,
    ),
    Ingredients.plutonium_pellet: # プルトニウム・ペレット
    Recipe(
        RecipeIO(Ingredients.non_fissile_uranium,100).add_item(Ingredients.uranium_waste,25),
        RecipeIO(Ingredients.plutonium_pellet,30),
        Building.particle_accelerator,
    ),
    Ingredients.encased_plutonium_cell: # 被覆型プルトニウム・セル
    Recipe(
        RecipeIO(Ingredients.plutonium_pellet,10).add_item(Ingredients.concrete,20),
        RecipeIO(Ingredients.encased_plutonium_cell,5),
        Building.assembler,
    ),
    alternate(Ingredients.encased_plutonium_cell):
    Recipe(
        RecipeIO(Ingredients.non_fissile_uranium,75).add_item(Ingredients.aluminum_casing,10),
        RecipeIO(Ingredients.encased_plutonium_cell,10),
        Building.particle_accelerator,
    ),
    Ingredients.plutonium_fuel_rod: # プルトニウム燃料棒
    Recipe(
        RecipeIO(Ingredients.encased_plutonium_cell,7.5).add_item(Ingredients.steel_beam,4.5).add_item(Ingredients.electromagnetic_control_rod,1.5).add_item(Ingredients.heat_sink,2.5),
        RecipeIO(Ingredients.plutonium_fuel_rod,0.25),
        Building.manufacturer,
    ),
    alternate(Ingredients.plutonium_fuel_rod):
    Recipe(
        RecipeIO(Ingredients.encased_plutonium_cell,10).add_item(Ingredients.pressure_conversion_cube,0.5),
        RecipeIO(Ingredients.plutonium_fuel_rod,0.5),
        Building.assembler,
    ),
    Ingredients.plutonium_waste: # プルトニウム廃棄物
    Recipe(
        RecipeIO(Ingredients.plutonium_fuel_rod,0.1).add_item(Liquid.water,240),
        RecipeIO(Ingredients.plutonium_waste,1),
        Building.nuclear_power_plant,
    ),

    # Orbital Elevator 軌道エレベーター
    Ingredients.smart_plating: # スマート・プレート
    Recipe(
        RecipeIO(Ingredients.reinforced_iron_plate,2).add_item(Ingredients.rotor,2),
        RecipeIO(Ingredients.smart_plating,2),
        Building.assembler,
    ),
    alternate(Ingredients.smart_plating):
    Recipe(
        RecipeIO(Ingredients.reinforced_iron_plate,2.5).add_item(Ingredients.rotor,2.5).add_item(Ingredients.plastic,7.5),
        RecipeIO(Ingredients.smart_plating,5),
        Building.manufacturer,
    ),
    Ingredients.versatile_framework: # 多目的ワイヤフレーム
    Recipe(
        RecipeIO(Ingredients.modular_frame,2.5).add_item(Ingredients.steel_beam,30),
        RecipeIO(Ingredients.versatile_framework,5),
        Building.assembler,
    ),
    alternate(Ingredients.versatile_framework):
    Recipe(
        RecipeIO(Ingredients.modular_frame,3.75).add_item(Ingredients.steel_beam,22.5).add_item(Ingredients.rubber,30),
        RecipeIO(Ingredients.versatile_framework,7.5),
        Building.manufacturer,
    ),
    Ingredients.automated_wiring: # 自動ワイヤー
    Recipe(
        RecipeIO(Ingredients.stator,2.5).add_item(Ingredients.cable,50),
        RecipeIO(Ingredients.automated_wiring,2.5),
        Building.assembler,
    ),
    alternate(Ingredients.automated_wiring):
    Recipe(
        RecipeIO(Ingredients.stator,3.75).add_item(Ingredients.wire,75).add_item(Ingredients.high_speed_connector,1.875),
        RecipeIO(Ingredients.automated_wiring,7.5),
        Building.manufacturer,
    ),
    Ingredients.modular_engine: # モジュラーエンジン
    Recipe(
        RecipeIO(Ingredients.motor,2).add_item(Ingredients.rubber,15).add_item(Ingredients.smart_plating,2),
        RecipeIO(Ingredients.modular_engine,1),
        Building.manufacturer,
    ),
    Ingredients.adaptive_control_unit: # 自律制御ユニット
    Recipe(
        RecipeIO(Ingredients.automated_wiring,7.5).add_item(Ingredients.circuit_board,5).add_item(Ingredients.heavy_modular_frame,1).add_item(Ingredients.computer,1),
        RecipeIO(Ingredients.adaptive_control_unit,1),
        Building.manufacturer,
    ),
    Ingredients.assembly_director_system: # 組立指揮システム
    Recipe(
        RecipeIO(Ingredients.adaptive_control_unit,1.5).add_item(Ingredients.supercomputer,0.75),
        RecipeIO(Ingredients.assembly_director_system,0.75),
        Building.assembler,
    ),
    Ingredients.magnetic_field_generator: # 磁界発生装置
    Recipe(
        RecipeIO(Ingredients.versatile_framework,2.5).add_item(Ingredients.electromagnetic_control_rod,1).add_item(Ingredients.battery,5),
        RecipeIO(Ingredients.magnetic_field_generator,1),
        Building.manufacturer,
    ),
    Ingredients.thermal_propulsion_rocket: # 熱推進型ロケット
    Recipe(
        RecipeIO(Ingredients.modular_engine,2.5).add_item(Ingredients.turbo_motor,1).add_item(Ingredients.cooling_system,3).add_item(Ingredients.fused_modular_frame,1),
        RecipeIO(Ingredients.thermal_propulsion_rocket,1),
        Building.manufacturer,
    ),
    Ingredients.nuclear_pasta: # 原子核パスタ
    Recipe(
        RecipeIO(Ingredients.copper_powder,100).add_item(Ingredients.pressure_conversion_cube,0.5),
        RecipeIO(Ingredients.nuclear_pasta,0.5),
        Building.particle_accelerator,
    ),

    # Liquid 液体
    Liquid.water: # 水
    Recipe(
        RecipeIO(),
        RecipeIO(Liquid.water, 120),
        Building.water_extractor,
    ),
    Liquid.crude_oil: # 原油 
    Recipe(
        RecipeIO(),
        RecipeIO(Liquid.crude_oil, 120),
        Building.oil_extractor,
    ),
    Liquid.heavy_oil_residue: # 廃重油
    Recipe(
        RecipeIO(Ingredients.packaged_heavy_oil_residue,20),
        RecipeIO(Liquid.heavy_oil_residue,20).add_item(Ingredients.empty_canister,20),
        Building.packager,
    ),
    alternate(Liquid.heavy_oil_residue):
    Recipe(
        RecipeIO(Liquid.crude_oil,30),
        RecipeIO(Liquid.heavy_oil_residue,40).add_item(Ingredients.polymer_resin,20),
        Building.refinery,
    ),
    Liquid.fuel: # 燃料
    Recipe(
        RecipeIO(Liquid.crude_oil,60),
        RecipeIO(Liquid.fuel,40).add_item(Ingredients.polymer_resin,30),
        Building.refinery,
    ),
    alternate(Liquid.fuel):
    Recipe(
        RecipeIO(Liquid.heavy_oil_residue,60),
        RecipeIO(Liquid.fuel,40),
        Building.refinery,
    ),
    alternate(Liquid.fuel,2):
    Recipe(
        RecipeIO(Ingredients.packaged_fuel,60),
        RecipeIO(Liquid.fuel,60).add_item(Ingredients.empty_canister,60),
        Building.refinery,
    ),
    alternate(Liquid.fuel,3):
    Recipe(
        RecipeIO(Liquid.heavy_oil_residue,50).add_item(Liquid.water,100),
        RecipeIO(Liquid.fuel,100),
        Building.blender,
    ),
    Liquid.Turbofuel: # ターボ燃料
    Recipe(
        RecipeIO(Liquid.fuel,22.5).add_item(Ingredients.compacted_coal,15),
        RecipeIO(Liquid.Turbofuel,18.75),
        Building.refinery,
    ),
    alternate(Liquid.Turbofuel):
    Recipe(
        RecipeIO(Ingredients.packaged_turbofuel,20),
        RecipeIO(Liquid.Turbofuel,20).add_item(Ingredients.empty_canister,20),
        Building.packager,
    ),
    alternate(Liquid.Turbofuel,2):
    Recipe(
        RecipeIO(Liquid.heavy_oil_residue,37.5).add_item(Ingredients.compacted_coal,30),
        RecipeIO(Liquid.heavy_oil_residue,30),
        Building.refinery,
    ),
    alternate(Liquid.Turbofuel,3):
    Recipe(
        RecipeIO(Liquid.fuel,15).add_item(Liquid.heavy_oil_residue,30).add_item(Ingredients.sulfur,22.5).add_item(Ingredients.petroleum_coke,22.5),
        RecipeIO(Liquid.Turbofuel,45),
        Building.blender,
    ),
    Liquid.liquid_biofuel: # 液体バイオ燃料
    Recipe(
        RecipeIO(Ingredients.solid_biofuel,90).add_item(Liquid.water,45),
        RecipeIO(Liquid.liquid_biofuel,60),
        Building.refinery,
    ),
    alternate(Liquid.liquid_biofuel):
    Recipe(
        RecipeIO(Ingredients.packaged_liquid_biofuel,60),
        RecipeIO(Liquid.liquid_biofuel,60).add_item(Ingredients.empty_canister,60),
        Building.packager,
    ),
    Liquid.alumina_solution: # アルミナ溶液
    Recipe(
        RecipeIO(Ingredients.bauxite,120).add_item(Liquid.water,180),
        RecipeIO(Liquid.alumina_solution,120).add_item(Ingredients.silica,50),
        Building.refinery,
    ),
    alternate(Liquid.alumina_solution):
    Recipe(
        RecipeIO(Ingredients.packaged_alumina_solution,120),
        RecipeIO(Liquid.alumina_solution,120).add_item(Ingredients.empty_canister,120),
        Building.packager,
    ),
    alternate(Liquid.alumina_solution,2):
    Recipe(
        RecipeIO(Ingredients.bauxite,200).add_item(Liquid.water,200),
        RecipeIO(Liquid.alumina_solution,240),
        Building.refinery,
    ),
    Liquid.sulfuric_acid: # 硫酸
    Recipe(
        RecipeIO(Ingredients.sulfur,50).add_item(Liquid.water,50),
        RecipeIO(Liquid.sulfuric_acid,50),
        Building.refinery,
    ),
    alternate(Liquid.sulfuric_acid):
    Recipe(
        RecipeIO(Ingredients.packaged_sulfuric_acid,60),
        RecipeIO(Liquid.sulfuric_acid,60).add_item(Ingredients.empty_canister,60),
        Building.packager,
    ),
    Liquid.nitric_acid: # 硝酸
    Recipe(
        RecipeIO(Gas.nitrogen_gas,120).add_item(Liquid.water,30).add_item(Ingredients.iron_plate,10),
        RecipeIO(Liquid.nitric_acid,30),
        Building.blender,
    ),
    alternate(Liquid.nitric_acid):
    Recipe(
        RecipeIO(Ingredients.packaged_nitric_acid,20),
        RecipeIO(Liquid.nitric_acid,20).add_item(Ingredients.empty_fluid_tank,20),
        Building.packager,
    ),

    # Gas 気体
    Gas.nitrogen_gas: # 窒素ガス
    Recipe(
        RecipeIO(),
        RecipeIO(Gas.nitrogen_gas,60),
        Building.resource_well_pressurizer,
    ),
    alternate(Gas.nitrogen_gas):
    Recipe(
        RecipeIO(Ingredients.packaged_nitrogen_gas,60),
        RecipeIO(Gas.nitrogen_gas,240).add_item(Ingredients.empty_fluid_tank,60),
        Building.packager,
    ),

    # Others その他
    Ingredients.beacon: # ビーコン
    Recipe(
        RecipeIO(Ingredients.iron_plate,22.5).add_item(Ingredients.iron_rod,7.5).add_item(Ingredients.wire,112.5).add_item(Ingredients.cable,15),
        RecipeIO(Ingredients.beacon,7.5),
        Building.manufacturer,
    ),
    alternate(Ingredients.beacon):
    Recipe(
        RecipeIO(Ingredients.steel_beam,2).add_item(Ingredients.steel_pipe,8).add_item(Ingredients.crystal_oscillator,0.5),
        RecipeIO(Ingredients.beacon,10),
        Building.manufacturer,
    ),
}

# byproduct 副産物

RECIPE[byproduct(Ingredients.silica)] = RECIPE[Liquid.alumina_solution]

RECIPE[byproduct(Liquid.water)] = RECIPE[Ingredients.battery]
RECIPE[byproduct(Liquid.water, 2)] = RECIPE[Ingredients.aluminum_scrap]
RECIPE[byproduct(Liquid.water, 3)] = RECIPE[alternate(Ingredients.aluminum_scrap)]
RECIPE[byproduct(Liquid.water, 4)] = RECIPE[alternate(Ingredients.aluminum_scrap, 2)]
RECIPE[byproduct(Liquid.water, 5)] = RECIPE[Ingredients.non_fissile_uranium]
RECIPE[byproduct(Liquid.water, 6)] = RECIPE[alternate(Ingredients.non_fissile_uranium)]

RECIPE[byproduct(Ingredients.polymer_resin)] = RECIPE[alternate(Liquid.heavy_oil_residue)]
RECIPE[byproduct(Ingredients.polymer_resin, 2)] = RECIPE[Liquid.fuel]

RECIPE[byproduct(Liquid.heavy_oil_residue)] = RECIPE[Ingredients.plastic]
RECIPE[byproduct(Liquid.heavy_oil_residue, 2)] = RECIPE[Ingredients.rubber]
RECIPE[byproduct(Liquid.heavy_oil_residue, 3)] = RECIPE[Ingredients.polymer_resin]

RECIPE[byproduct(Ingredients.empty_canister)] = RECIPE[Liquid.heavy_oil_residue]
RECIPE[byproduct(Ingredients.empty_canister, 2)] = RECIPE[alternate(Liquid.fuel, 2)]
RECIPE[byproduct(Ingredients.empty_canister, 3)] = RECIPE[alternate(Liquid.Turbofuel)]
RECIPE[byproduct(Ingredients.empty_canister, 4)] = RECIPE[alternate(Liquid.liquid_biofuel)]
RECIPE[byproduct(Ingredients.empty_canister, 5)] = RECIPE[alternate(Liquid.alumina_solution)]
RECIPE[byproduct(Ingredients.empty_canister, 6)] = RECIPE[alternate(Liquid.sulfuric_acid)]

RECIPE[byproduct(Ingredients.empty_fluid_tank)] = RECIPE[alternate(Liquid.nitric_acid)]
RECIPE[byproduct(Ingredients.empty_fluid_tank, 2)] = RECIPE[Gas.nitrogen_gas]

RECIPE[byproduct(Liquid.sulfuric_acid)] = RECIPE[Ingredients.encased_uranium_cell]
