from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_button_model import CustomizationButtonModel

class CustomizationToolbarModel(ViewModel):
    __slots__ = (b'onActionBtnClick',)

    def __init__(self, properties=3, commands=1):
        super(CustomizationToolbarModel, self).__init__(properties=properties, commands=commands)
        return

    def getButtonList(self):
        return self._getArray(0)

    def setButtonList(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getButtonListType():
        return CustomizationButtonModel

    def getIsToolbarPanelEnabled(self):
        return self._getBool(1)

    def setIsToolbarPanelEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsInscriptionPanelEnabled(self):
        return self._getBool(2)

    def setIsInscriptionPanelEnabled(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(CustomizationToolbarModel, self)._initialize()
        self._addArrayProperty(b'buttonList', Array())
        self._addBoolProperty(b'isToolbarPanelEnabled', False)
        self._addBoolProperty(b'isInscriptionPanelEnabled', False)
        self.onActionBtnClick = self._addCommand(b'onActionBtnClick')
        return
