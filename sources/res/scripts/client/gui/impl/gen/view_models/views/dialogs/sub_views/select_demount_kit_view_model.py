from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectDemountKitViewModel(SelectOptionBaseItemViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SelectDemountKitViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStorageCount(self):
        return self._getNumber(4)

    def setStorageCount(self, value):
        self._setNumber(4, value)
        return

    def getText(self):
        return self._getString(5)

    def setText(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(SelectDemountKitViewModel, self)._initialize()
        self._addNumberProperty(b'storageCount', 0)
        self._addStringProperty(b'text', b'')
        return
