from enum import Enum

class SubMode(Enum):
    DEFAULT = b'default'
    STPATRICK = b'stPatrick'


class CoinType(Enum):
    BRCOIN = b'brcoin'
    STPCOIN = b'stpcoin'
