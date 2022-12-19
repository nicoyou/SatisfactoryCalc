import enum

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
    Language.japanese: {},
}
