from gui.battle_results.reusable.common import CommonInfo

class Comp7CommonInfo(CommonInfo):
    __slots__ = (b'__bannedVehicles',)

    def __init__(self, *args, **kwargs):
        super(Comp7CommonInfo, self).__init__(*args, **kwargs)
        self.__bannedVehicles = kwargs.get(b'comp7BannedVehicles', {})
        return

    @property
    def bannedVehicles(self):
        return self.__bannedVehicles
