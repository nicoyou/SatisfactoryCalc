import enum
from .define import Ingredients, Liquid, Gas

from . import define
import nlib3


class Language(enum.Enum):
    english = enum.auto()
    japanese = enum.auto()


def translation(item: define.Item, language: Language) -> str:
    """アイテム名を指定された言語に変換する"""
    lp = LANGUAGE_PACK.get(language)
    if lp is None:
        nlib3.print_error_log("指定された言語パックは存在しません")
        return item
    return lp.get(item, str(item))  # 翻訳後のアイテム名を返す ( 存在しなければ元の名前を返す )


LANGUAGE_PACK = {
    Language.english: {},
    Language.japanese: {
                                                                # Ore 鉱石
        Ingredients.iron_ore: "鉄鉱石",
        Ingredients.copper_ore: "銅鉱石",
        Ingredients.limestone: "石灰岩",
        Ingredients.coal: "石炭",
        Ingredients.caterium_ore: "カテリウム鉱石",
        Ingredients.raw_quartz: "未加工石英",
        Ingredients.sulfur: "硫黄",
        Ingredients.bauxite: "ボーキサイト",
        Ingredients.uranium: "ウラン",
        Ingredients.sam_ore: "SAM鉱石",

                                                                # Plants/Animals 植物・動物類
        Ingredients.leaves: "葉",
        Ingredients.wood: "木",
        Ingredients.flower_petals: "花弁",
        Ingredients.mycelia: "菌糸",
        Ingredients.blue_power_slug: "青のパワー・スラッグ",
        Ingredients.yellow_power_slug: "黄のパワー・スラッグ",
        Ingredients.purple_power_slug: "紫のパワー・スラッグ",

                                                                # Alien Remains エイリアンの遺骸
        Ingredients.hog_remains: "ホッグの遺骸",
        Ingredients.hatcher_remains: "ハッチャーの遺骸",
        Ingredients.stinger_remains: "スティンガーの遺骸",
        Ingredients.plasma_spitter_remains: "プラズマ・スピッターの遺骸",
        Ingredients.alien_protein: "エイリアンのタンパク質",
        Ingredients.organic_data_capsule: "オーガニック・データカプセル",

                                                                # Recovery Item 回復アイテム
        Ingredients.beryl_nut: "ベリル・ナッツ",
        Ingredients.paleberry: "パレベリー",
        Ingredients.bacon_agaric: "ベーコンタケ",

                                                                # Others その他
        Ingredients.hard_drive: "ハードドライブ",
        Ingredients.hub_parts: "HUB部品",
        Ingredients.ficsit_coupon: "FICSITクーポン",
        Ingredients.mercer_sphere: "マーサー・スフィア",
        Ingredients.somersloop: "ソマースループ",
        Ingredients.power_shard: "パワー・シャード",
        Ingredients.beacon: "ビーコン",

                                                                # Biomass バイオマス
        Ingredients.biomass: "バイオマス",
        Ingredients.fabric: "布地",
        Ingredients.solid_biofuel: "固体バイオ燃料",
        Ingredients.color_cartridge: "カラー弾薬",

                                                                # Mineral 鉱物
        Ingredients.concrete: "コンクリート",
        Ingredients.quartz_crystal: "石英結晶",
        Ingredients.silica: "シリカ",
        Ingredients.compacted_coal: "圧縮石炭",
        Ingredients.copper_powder: "銅粉",

                                                                # The Expendables 消耗品
        Ingredients.gas_filter: "ガスフィルター",
        Ingredients.iodine_infused_filter: "ヨウ素注入フィルター",

                                                                # Ammunition 弾薬
        Ingredients.black_powder: "黒色火薬",
        Ingredients.smokeless_powder: "無煙火薬",
        Ingredients.iron_rebar: "鉄筋",
        Ingredients.stun_rebar: "スタン鉄筋",
        Ingredients.shatter_rebar: "破砕鉄筋",
        Ingredients.explosive_rebar: "爆砕鉄筋",
        Ingredients.nobelisk: "ノーベリスク",
        Ingredients.gas_nobelisk: "ガス・ノーベリスク",
        Ingredients.cluster_nobelisk: "クラスター・ノーベリスク",
        Ingredients.pulse_nobelisk: "パルス・ノーベリスク",
        Ingredients.nuke_nobelisk: "ニューク・ノーベリスク",
        Ingredients.rifle_ammo: "ライフル弾",
        Ingredients.homing_rifle_ammo: "ホーミングライフル弾",
        Ingredients.turbo_rifle_ammo: "ターボライフル弾",

                                                                # Ingot インゴット
        Ingredients.iron_ingot: "鉄のインゴット",
        Ingredients.copper_ingot: "銅のインゴット",
        Ingredients.steel_ingot: "鋼鉄のインゴット",
        Ingredients.caterium_ingot: "カテリウムのインゴット",
        Ingredients.aluminum_ingot: "アルミのインゴット",

                                                                # Basic Parts 基本部品
        Ingredients.iron_plate: "鉄板",
        Ingredients.iron_rod: "鉄のロッド",
        Ingredients.screw: "ネジ",
        Ingredients.reinforced_iron_plate: "強化鉄板",
        Ingredients.modular_frame: "モジュラー・フレーム",
        Ingredients.copper_sheet: "銅のシート",
        Ingredients.steel_beam: "鋼梁",
        Ingredients.steel_pipe: "鋼鉄のパイプ",
        Ingredients.encased_industrial_beam: "コンクリート被覆型鋼梁",
        Ingredients.heavy_modular_frame: "ヘビー・モジュラー・フレーム",
        Ingredients.alclad_aluminum_sheet: "アルクラッド・アルミシート",
        Ingredients.aluminum_casing: "アルミ筐体",

                                                                # Electronics 電子機器
        Ingredients.wire: "ワイヤー",
        Ingredients.cable: "ケーブル",
        Ingredients.quickwire: "クイックワイヤー",
        Ingredients.circuit_board: "回路基板",
        Ingredients.ai_limiter: "AI リミッター",
        Ingredients.high_speed_connector: "高速コネクター",

                                                                # Industrial Parts 産業用部品
        Ingredients.rotor: "ローター",
        Ingredients.stator: "固定子",
        Ingredients.motor: "モーター",
        Ingredients.heat_sink: "ヒートシンク",
        Ingredients.turbo_motor: "ターボモーター",
        Ingredients.battery: "バッテリー",
        Ingredients.fused_modular_frame: "溶融モジュラー・フレーム",
        Ingredients.cooling_system: "冷却システム",

                                                                # Communication 通信
        Ingredients.crystal_oscillator: "水晶発振器",
        Ingredients.computer: "コンピューター",
        Ingredients.supercomputer: "スーパーコンピューター",
        Ingredients.radio_control_unit: "無線制御ユニット",

                                                                # Petroleum Products 石油製品
        Ingredients.plastic: "プラスチック",
        Ingredients.rubber: "ゴム",
        Ingredients.petroleum_coke: "石油コークス",
        Ingredients.polymer_resin: "合成樹脂",

                                                                # Advanced Refining 先進的な精製
        Ingredients.aluminum_scrap: "アルミのスクラップ",

                                                                # Container 容器入り
        Ingredients.packaged_fuel: "容器入り燃料",
        Ingredients.packaged_turbofuel: "容器入りターボ燃料",
        Ingredients.packaged_liquid_biofuel: "容器入り液体バイオ燃料",
        Ingredients.packaged_heavy_oil_residue: "容器入り廃重油",
        Ingredients.packaged_oil: "容器入り原油",
        Ingredients.packaged_water: "容器入り水",
        Ingredients.packaged_sulfuric_acid: "容器入り硫酸",
        Ingredients.packaged_nitrogen_gas: "容器入り窒素ガス",
        Ingredients.packaged_nitric_acid: "容器入り硝酸",
        Ingredients.packaged_alumina_solution: "容器入りアルミナ溶液",

                                                                # Storage 貯蔵庫
        Ingredients.empty_canister: "空の容器",
        Ingredients.empty_fluid_tank: "空の液体タンク",
        Ingredients.pressure_conversion_cube: "圧力変換キューブ",

                                                                # Nuclear Power 原子力
        Ingredients.electromagnetic_control_rod: "電磁制御棒",
        Ingredients.encased_uranium_cell: "被覆型ウラン･セル",
        Ingredients.uranium_fuel_rod: "ウラン燃料棒",
        Ingredients.uranium_waste: "ウラン廃棄物",
        Ingredients.non_fissile_uranium: "非分裂性ウラン",
        Ingredients.plutonium_pellet: "プルトニウム・ペレット",
        Ingredients.encased_plutonium_cell: "被覆型プルトニウム・セル",
        Ingredients.plutonium_fuel_rod: "プルトニウム燃料棒",
        Ingredients.plutonium_waste: "プルトニウム廃棄物",

                                                                # Orbital Elevator 軌道エレベーター
        Ingredients.smart_plating: "スマート・プレート",
        Ingredients.versatile_framework: "多目的フレームワーク",
        Ingredients.automated_wiring: "自動ワイヤー",
        Ingredients.modular_engine: "モジュラーエンジン",
        Ingredients.adaptive_control_unit: "自律制御ユニット",
        Ingredients.assembly_director_system: "組立指揮システム",
        Ingredients.magnetic_field_generator: "磁界発生装置",
        Ingredients.thermal_propulsion_rocket: "熱推進型ロケット",
        Ingredients.nuclear_pasta: "原子核パスタ",

                                                                # Liquid 液体
        Liquid.water: "水",
        Liquid.crude_oil: "原油",
        Liquid.heavy_oil_residue: "廃重油",
        Liquid.fuel: "燃料",
        Liquid.Turbofuel: "ターボ燃料",
        Liquid.liquid_biofuel: "液体バイオ燃料",
        Liquid.alumina_solution: "アルミナ溶液",
        Liquid.sulfuric_acid: "硫酸",
        Liquid.nitric_acid: "硝酸",

                                                                # Gas 気体
        Gas.nitrogen_gas: "窒素ガス",
    },
}
