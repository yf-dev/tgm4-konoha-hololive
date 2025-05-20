from dataclasses import dataclass
from typing import Literal

CHARACTER_ID = Literal[
    "ao",
    "gigi",
    "kanade",
    "niko",
    "fauna",
    "towa",
    "aqua",
    "nerissa",
    "okayu",
    "bijou",
    "kanata",
    "kiara",
    "raden",
    "flare",
    "liz",
    "mococo",
    "fuwawa",
    "su",
    "mumei",
    "vivi",
    "azki",
    "marine",
    "fubuki",
    "shion",
    "noel",
    "watame",
    "ame",
    "gura",
    "mio",
    "korone",
    "calli",
    "subaru",
    "miko",
    "bae",
    "raora",
    "sana",
    "ceci",
    "kronii",
    "suisei",
    "pekora",
    "roboco",
    "luna",
    "ina",
    "riona",
    "shiori",
    "irys",
    "ririka",
    "hajime",
    "chihaya",
    "sora",
]


@dataclass
class Character:
    id: CHARACTER_ID
    name1: str
    name2: str


CHARACTERS: list[Character] = [
    Character(
        "ame",
        "ワトソン・アメリア（わとそん あめりあ）",
        "Watson Amelia",
    ),
    Character(
        "ao",
        "火威青（ひおどし あお）",
        "Hiodoshi Ao",
    ),
    Character(
        "aqua",
        "湊あくあ（みなと あくあ）",
        "Minato Aqua",
    ),
    Character(
        "azki",
        "あずき（あずき）",
        "AZKi",
    ),
    Character(
        "bae",
        "ハコス・ベールズ（はこす べーるず）",
        "Hakos Baelz",
    ),
    Character(
        "bijou",
        "古石ビジュー（こせき びじゅー）",
        "Koseki Bijou",
    ),
    Character(
        "calli",
        "森カリオペ（もり かりおぺ）",
        "Mori Calliope",
    ),
    Character(
        "ceci",
        "セシリア・イマーグリーン（せしりあ いまーぐりーん）",
        "Cecilia Immergreen",
    ),
    Character(
        "chihaya",
        "輪堂千速（りんどう ちはや）",
        "Rindo Chihaya",
    ),
    Character(
        "fauna",
        "セレス・ファウナ（せれす ふぁうな）",
        "Ceres Fauna",
    ),
    Character(
        "flare",
        "不知火フレア（しらぬい ふれあ）",
        "Shiranui Flare",
    ),
    Character(
        "fubuki",
        "白上フブキ（しらかみ ふぶき）",
        "Shirakami Fubuki",
    ),
    Character(
        "fuwawa", "フワワ・アビスガード（ふわわ あびすがーど）", "Fuwawa Abyssgard"
    ),
    Character(
        "gigi",
        "ジジ・ムリン（じじ むりん）",
        "Gigi Murin",
    ),
    Character(
        "gura",
        "がうる・ぐら（がうる ぐら）",
        "Gawr Gura",
    ),
    Character(
        "hajime",
        "轟はじめ（とどろき はじめ）",
        "Todoroki Hajime",
    ),
    Character(
        "ina",
        "一伊那尓栖（にのまえ いなにす）",
        "Ninomae Ina'nis",
    ),
    Character(
        "irys",
        "アイリス（あいりす）",
        "IRyS",
    ),
    Character(
        "kanade",
        "音乃瀬奏（おとのせ かなで）",
        "Otonose Kanade",
    ),
    Character(
        "kanata",
        "天音かなた（あまね かなた）",
        "Amane Kanata",
    ),
    Character(
        "kiara",
        "小鳥遊キアラ（たかなし きあら）",
        "Takanashi Kiara",
    ),
    Character(
        "korone",
        "戌神ころね（いぬがみ ころね）",
        "Inugami Korone",
    ),
    Character(
        "kronii",
        "オーロ・クロニー（おーろ くろにー）",
        "Ouro Kronii",
    ),
    Character(
        "liz",
        "エリザベス・ローズ・ブラッドフレイム（えりざべす ろーず ぶらっどふれいむ）",
        "Elizabeth Rose Bloodflame",
    ),
    Character(
        "luna",
        "姫森ルーナ（ひめもり るーな）",
        "Himemori Luna",
    ),
    Character(
        "marine",
        "宝鐘マリン（ほうしょう まりん）",
        "Houshou Marine",
    ),
    Character(
        "miko",
        "さくらみこ（さくら みこ）",
        "Sakura Miko",
    ),
    Character(
        "mio",
        "大神ミオ（おおかみ みお）",
        "Ookami Mio",
    ),
    Character(
        "mococo", "モココ・アビスガード（もここ あびすがーど）", "Mococo Abyssgard"
    ),
    Character(
        "mumei",
        "七詩ムメイ（ななし むめい）",
        "Nanashi Mumei",
    ),
    Character(
        "nerissa",
        "ネリッサ・レイヴンクロフト （ねりっさ れいゔんくろふと）",
        "Nerissa Ravencroft",
    ),
    Character(
        "niko",
        "虎金妃笑虎（こがねい にこ）",
        "Koganei Niko",
    ),
    Character(
        "noel",
        "白銀ノエル（しろがね のえる）",
        "Shirogane Noel",
    ),
    Character(
        "okayu",
        "猫又おかゆ（ねこまた おかゆ）",
        "Nekomata Okayu",
    ),
    Character(
        "pekora",
        "兎田ぺこら（うさだ ぺこら）",
        "Usada Pekora",
    ),
    Character(
        "raden",
        "儒烏風亭らでん（じゅうふうてい らでん）",
        "Juufuutei Raden",
    ),
    Character(
        "raora",
        "ラオーラ・パンテーラ（らおーら ぱんてーら）",
        "Raora Panthera",
    ),
    Character(
        "riona",
        "響咲リオナ（いさき りおな）",
        "Isaki Riona",
    ),
    Character(
        "ririka",
        "一条莉々華（いちじょう りりか）",
        "Ichijou Ririka",
    ),
    Character(
        "roboco",
        "ロボ子さん（ろぼこさん）",
        "Robocosan",
    ),
    Character(
        "sana",
        "九十九佐命（つくも さな）",
        "Tsukumo Sana",
    ),
    Character(
        "shion",
        "紫咲シオン（むらさき しおん）",
        "Murasaki Shion",
    ),
    Character(
        "shiori",
        "シオリ・ノヴェラ（しおり のゔぇら）",
        "Shiori Novella",
    ),
    Character(
        "sora",
        "ときのそら（ときのそら）",
        "Tokino Sora",
    ),
    Character(
        "su",
        "水宮枢（みずみや すう）",
        "Mizumiya Su",
    ),
    Character(
        "subaru",
        "大空スバル（おおぞら すばる）",
        "Oozora Subaru",
    ),
    Character(
        "suisei",
        "星街すいせい（ほしまち すいせい）",
        "Hoshimachi Suisei",
    ),
    Character(
        "towa",
        "常闇トワ（とこやみ とわ）",
        "Tokoyami Towa",
    ),
    Character(
        "vivi",
        "綺々羅々ヴィヴィ（ききらら ゔぃゔぃ）",
        "Kikirara Vivi",
    ),
    Character(
        "watame",
        "角巻わため（つのまき わため）",
        "Tsunomaki Watame",
    ),
]

CHARACTER_MAP: dict[CHARACTER_ID, Character] = {c.id: c for c in CHARACTERS}
