from gui.impl.gen.view_models.views.lobby.premacc.maps_blacklist_slot_model import MapsBlacklistSlotModel

class MapsBlacklistWidgetSlotModel(MapsBlacklistSlotModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MapsBlacklistWidgetSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsShowMode(self):
        return self._getBool(7)

    def setIsShowMode(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(MapsBlacklistWidgetSlotModel, self)._initialize()
        self._addBoolProperty(b'isShowMode', False)
        return
