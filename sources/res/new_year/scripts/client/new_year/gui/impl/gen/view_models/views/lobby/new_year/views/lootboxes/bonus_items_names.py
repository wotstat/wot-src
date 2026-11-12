from frameworks.wulf import ViewModel

class BonusItemsNames(ViewModel):
    __slots__ = ()
    TOYS = b'nyToys'
    BOX_WITH_TOYS = b'boxWithToys'
    PREMIUM_PLUS = b'premium_plus'
    EXTRA_SLOT = b'extraSlot'
    VARIADIC_DISCOUNT = b'variadicDiscount'
    VEHICLE = b'vehicles'
    OTHER = b'other'

    def __init__(self, properties=0, commands=0):
        super(BonusItemsNames, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(BonusItemsNames, self)._initialize()
        return
