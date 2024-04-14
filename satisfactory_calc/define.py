import enum

import nlib3

CONVEYOR_BELT_MAX = 780
PIPE_MAX = 600


class Item(nlib3.StrEnum):
    """アイテム"""


class Ingredients(Item):
    """材料"""
    # Ore 鉱石
    iron_ore = "Iron Ore"           # 鉄鉱石
    copper_ore = "Copper Ore"       # 銅鉱石
    limestone = "Limestone"         # 石灰岩
    coal = "Coal"                   # 石炭
    caterium_ore = "Caterium Ore"   # カテリウム鉱石
    raw_quartz = "Raw Quartz"       # 未加工石英
    sulfur = "Sulfur"               # 硫黄
    bauxite = "Bauxite"             # ボーキサイト
    uranium = "Uranium"             # ウラン
    sam_ore = "SAM Ore"             # SAM鉱石

    # Plants/Animals 植物・動物類
    leaves = "Leaves"                           # 葉
    wood = "Wood"                               # 木
    flower_petals = "Flower Petals"             # 花弁
    mycelia = "Mycelia"                         # 菌糸
    blue_power_slug = "Blue Power Slug"         # 青のパワー・スラッグ
    yellow_power_slug = "Yellow Power Slug"     # 黄のパワー・スラッグ
    purple_power_slug = "Purple Power Slug"     # 紫のパワー・スラッグ

    # Alien Remains エイリアンの遺骸
    hog_remains = "Hog Remains"                         # ホッグの遺骸
    hatcher_remains = "Hatcher Remains"                 # ハッチャーの遺骸
    stinger_remains = "Stinger Remains"                 # スティンガーの遺骸
    plasma_spitter_remains = "Plasma Spitter Remains"   # プラズマ・スピッターの遺骸
    alien_protein = "Alien Protein"                     # エイリアンのタンパク質
    organic_data_capsule = "Organic Data Capsule"       # オーガニック・データカプセル

    # Recovery Item 回復アイテム
    beryl_nut = "Beryl Nut"         # ベリル・ナッツ
    paleberry = "Paleberry"         # パレベリー
    bacon_agaric = "Bacon Agaric"   # ベーコンタケ

    # Others その他
    hard_drive = "Hard Drive"           # ハードドライブ
    hub_parts = "HUB Parts"             # HUB 部品
    ficsit_coupon = "FICSIT Coupon"     # FICSIT クーポン
    mercer_sphere = "Mercer Sphere"     # マーサー・スフィア
    somersloop = "Somersloop"           # ソマースループ
    power_shard = "Power Shard"         # パワー・シャード
    beacon = "Beacon"                   # ビーコン

    # Biomass バイオマス
    biomass = "Biomass"                     # バイオマス
    fabric = "Fabric"                       # 布地
    solid_biofuel = "Solid Biofuel"         # 固体バイオ燃料
    color_cartridge = "Color Cartridge"     # カラー弾薬

    # Mineral 鉱物
    concrete = "Concrete"               # コンクリート
    quartz_crystal = "Quartz Crystal"   # 石英結晶
    silica = "Silica"                   # シリカ
    compacted_coal = "Compacted Coal"   # 圧縮石炭
    copper_powder = "Copper Powder"     # 銅粉

    # The Expendables 消耗品
    gas_filter = "Gas Filter"                           # ガスフィルター
    iodine_infused_filter = "Iodine Infused Filter"     # ヨウ素注入フィルター

    # Ammunition 弾薬
    black_powder = "Black Powder"               # 黒色火薬
    smokeless_powder = "Smokeless Powder"       # 無煙火薬
    iron_rebar = "Iron Rebar"                   # 鉄筋
    stun_rebar = "Stun Rebar"                   # スタン鉄筋
    shatter_rebar = "Shatter Rebar"             # 破砕鉄筋
    explosive_rebar = "Explosive Rebar"         # 爆砕鉄筋
    nobelisk = "Nobelisk"                       # ノーベリスク
    gas_nobelisk = "Gas Nobelisk"               # ガス・ノーベリスク
    cluster_nobelisk = "Cluster Nobelisk"       # クラスター・ノーベリスク
    pulse_nobelisk = "Pulse Nobelisk"           # パルス・ノーベリスク
    nuke_nobelisk = "Nuke Nobelisk"             # ニューク・ノーベリスク
    rifle_ammo = "Rifle Ammo"                   # ライフル弾
    homing_rifle_ammo = "Homing Rifle Ammo"     # ホーミングライフル弾
    turbo_rifle_ammo = "Turbo Rifle Ammo"       # ターボライフル弾

    # Ingot インゴット
    iron_ingot = "Iron Ingot"           # 鉄のインゴット
    copper_ingot = "Copper Ingot"       # 銅のインゴット
    steel_ingot = "Steel Ingot"         # 鋼鉄のインゴット
    caterium_ingot = "Caterium Ingot"   # カテリウムのインゴット
    aluminum_ingot = "Aluminum Ingot"   # アルミのインゴット

    # Basic Parts 基本部品
    iron_plate = "Iron Plate"                               # 鉄板
    iron_rod = "Iron Rod"                                   # 鉄のロッド
    screw = "Screw"                                         # ネジ
    reinforced_iron_plate = "Reinforced Iron Plate"         # 強化鉄板
    modular_frame = "Modular Frame"                         # モジュラー・フレーム
    copper_sheet = "Copper Sheet"                           # 銅のシート
    steel_beam = "Steel Beam"                               # 鋼梁
    steel_pipe = "Steel Pipe"                               # 鋼鉄のパイプ
    encased_industrial_beam = "Encased Industrial Beam"     # コンクリート被覆型鋼梁
    heavy_modular_frame = "Heavy Modular Frame"             # ヘビー・モジュラー・フレーム
    alclad_aluminum_sheet = "Alclad Aluminum Sheet"         # アルクラッド・アルミシート
    aluminum_casing = "Aluminum Casing"                     # アルミ筐体

    # Electronics 電子機器
    wire = "Wire"                                   # ワイヤー
    cable = "Cable"                                 # ケーブル
    quickwire = "Quickwire"                         # クイックワイヤー
    circuit_board = "Circuit Board"                 # 回路基板
    ai_limiter = "AI Limiter"                       # AI リミッター
    high_speed_connector = "High-Speed Connector"   # 高速コネクター

    # Industrial Parts 産業用部品
    rotor = "Rotor"                                 # ローター
    stator = "Stator"                               # 固定子
    motor = "Motor"                                 # モーター
    heat_sink = "Heat Sink"                         # ヒートシンク
    turbo_motor = "Turbo Motor"                     # ターボモーター
    battery = "Battery"                             # バッテリー
    fused_modular_frame = "Fused Modular Frame"     # 溶融モジュラー・フレーム
    cooling_system = "Cooling System"               # 冷却システム

    # Communication 通信
    crystal_oscillator = "Crystal Oscillator"   # 水晶発振器
    computer = "Computer"                       # コンピューター
    supercomputer = "Supercomputer"             # スーパーコンピューター
    radio_control_unit = "Radio Control Unit"   # 無線制御ユニット

    # Petroleum Products 石油製品
    plastic = "Plastic"                 # プラスチック
    rubber = "Rubber"                   # ゴム
    petroleum_coke = "Petroleum Coke"   # 石油コークス
    polymer_resin = "Polymer Resin"     # 合成樹脂

    # Advanced Refining 先進的な精製
    aluminum_scrap = "Aluminum Scrap"   # アルミのスクラップ

    # Container 容器入り
    packaged_fuel = "Packaged Fuel"                             # 容器入り燃料
    packaged_turbo_fuel = "Packaged Turbofuel"                  # 容器入りターボ燃料
    packaged_liquid_biofuel = "Packaged Liquid Biofuel"         # 容器入り液体バイオ燃料
    packaged_heavy_oil_residue = "Packaged Heavy Oil Residue"   # 容器入り廃重油
    packaged_oil = "Packaged Oil"                               # 容器入り原油
    packaged_water = "Packaged Water"                           # 容器入り水
    packaged_sulfuric_acid = "Packaged Sulfuric Acid"           # 容器入り硫酸
    packaged_nitrogen_gas = "Packaged Nitrogen Gas"             # 容器入り窒素ガス
    packaged_nitric_acid = "Packaged Nitric Acid"               # 容器入り硝酸
    packaged_alumina_solution = "Packaged Alumina Solution"     # 容器入りアルミナ溶液

    # Storage 貯蔵庫
    empty_canister = "Empty Canister"                       # 空の容器
    empty_fluid_tank = "Empty Fluid Tank"                   # 空の液体タンク
    pressure_conversion_cube = "Pressure Conversion Cube"   # 圧力変換キューブ

    # Nuclear Power 原子力
    electromagnetic_control_rod = "Electromagnetic Control Rod"     # 電磁制御棒
    encased_uranium_cell = "Encased Uranium Cell"                   # 被覆型ウラン･セル
    uranium_fuel_rod = "Uranium Fuel Rod"                           # ウラン燃料棒
    uranium_waste = "Uranium Waste"                                 # ウラン廃棄物
    non_fissile_uranium = "Non-fissile Uranium"                     # 非分裂性ウラン
    plutonium_pellet = "Plutonium Pellet"                           # プルトニウム・ペレット
    encased_plutonium_cell = "Encased Plutonium Cell"               # 被覆型プルトニウム・セル
    plutonium_fuel_rod = "Plutonium Fuel Rod"                       # プルトニウム燃料棒
    plutonium_waste = "Plutonium Waste"                             # プルトニウム廃棄物

    # Orbital Elevator 軌道エレベーター
    smart_plating = "Smart Plating"                             # スマート・プレート
    versatile_framework = "Versatile Framework"                 # 多目的フレームワーク
    automated_wiring = "Automated Wiring"                       # 自動ワイヤー
    modular_engine = "Modular Engine"                           # モジュラーエンジン
    adaptive_control_unit = "Adaptive Control Unit"             # 自律制御ユニット
    assembly_director_system = "Assembly Director System"       # 組立指揮システム
    magnetic_field_generator = "Magnetic Field Generator"       # 磁界発生装置
    thermal_propulsion_rocket = "Thermal Propulsion Rocket"     # 熱推進型ロケット
    nuclear_pasta = "Nuclear Pasta"                             # 原子核パスタ


class Liquid(Item):
    """液体の材料"""
    water = "Water"                             # 水
    crude_oil = "Crude Oil"                     # 原油
    heavy_oil_residue = "Heavy Oil Residue"     # 廃重油
    fuel = "Fuel"                               # 燃料
    turbo_fuel = "Turbofuel"                    # ターボ燃料
    liquid_biofuel = "Liquid Biofuel"           # 液体バイオ燃料
    alumina_solution = "Alumina Solution"       # アルミナ溶液
    sulfuric_acid = "Sulfuric Acid"             # 硫酸
    nitric_acid = "Nitric Acid"                 # 硝酸


class Gas(Item):
    """気体の材料"""
    nitrogen_gas = "Nitrogen Gas"   # 窒素ガス


class Building(nlib3.StrEnum):
    """建物"""
    # Manufacturers 製造
    constructor = "Constructor"                     # 製作機
    assembler = "Assembler"                         # 組立機
    manufacturer = "Manufacturer"                   # 製造機
    refinery = "Refinery"                           # 精製施設
    blender = "Blender"                             # 混合機
    packager = "Packager"                           # 充填機
    particle_accelerator = "Particle Accelerator"   # 粒子加速器

    # Smelters 精錬所
    smelter = "Smelter"     # 製錬炉
    foundry = "Foundry"     # 鋳造炉

    # Miners 採鉱
    miner_mk1 = "Miner Mk.1"    # 採鉱機Mk.1
    miner_mk2 = "Miner Mk.2"    # 採鉱機Mk.2
    miner_mk3 = "Miner Mk.3"    # 採鉱機Mk.3

    # Fluid Extractors 液体抽出機
    water_extractor = "Water Extractor"                         # 揚水ポンプ
    oil_extractor = "Oil Extractor"                             # 原油抽出機
    resource_well_pressurizer = "Resource Well Pressurizer"     # 資源井加圧機
    resource_well_extractor = "Resource Well Extractor"         # 資源井抽出器
    craft_bench = "Craft Bench"                                 # 工作台
    equipment_workshop = "Equipment Workshop"                   # 整備品作業場

    # Generators 発電機
    biomass_burner = "Biomass Burner"               # バイオマス・バーナー
    coal_generator = "Coal Generator"               # 石炭発電機
    fuel_generator = "Fuel Generator"               # 燃料式発電機
    geothermal_generator = "Geothermal Generator"   # 地熱発電機
    nuclear_power_plant = "Nuclear Power Plant"     # 原子力発電所

    other = "other"


class Purity(float, enum.Enum):
    """純度"""
    impure = 0.5    # 低純度
    normal = 1      # 中純度
    pure = 2        # 高純度
