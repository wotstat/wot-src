from frameworks.wulf import ViewModel

class TooltipConstants(ViewModel):
    __slots__ = ()
    TANKMAN = b'tankman'
    HANGAR_MODULE = b'hangarModule'
    TECH_MAIN_SHELL = b'techMainShell'
    PRICE_DISCOUNT = b'priceDiscount'

    def __init__(self, properties=0, commands=0):
        super(TooltipConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TooltipConstants, self)._initialize()
        return
