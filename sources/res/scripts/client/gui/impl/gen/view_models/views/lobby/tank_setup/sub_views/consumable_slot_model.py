from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel

class ConsumableSlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(ConsumableSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getDescription(self):
        return self._getString(21)

    def setDescription(self, value):
        self._setString(21, value)
        return

    def getIsBuiltIn(self):
        return self._getBool(22)

    def setIsBuiltIn(self, value):
        self._setBool(22, value)
        return

    def getItemName(self):
        return self._getString(23)

    def setItemName(self, value):
        self._setString(23, value)
        return

    def getIsBuyMoreDisabled(self):
        return self._getBool(24)

    def setIsBuyMoreDisabled(self, value):
        self._setBool(24, value)
        return

    def _initialize(self):
        super(ConsumableSlotModel, self)._initialize()
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'isBuiltIn', False)
        self._addStringProperty(b'itemName', b'')
        self._addBoolProperty(b'isBuyMoreDisabled', False)
        return
