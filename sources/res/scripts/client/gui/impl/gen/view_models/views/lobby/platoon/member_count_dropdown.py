from frameworks.wulf import Array
from gui.impl.gen.view_models.ui_kit.gf_drop_down_model import GfDropDownModel
from gui.impl.gen.view_models.views.lobby.platoon.dropdown_item import DropdownItem

class MemberCountDropdown(GfDropDownModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=1):
        super(MemberCountDropdown, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(3)

    def setItems(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getItemsType():
        return DropdownItem

    def getIsDisabled(self):
        return self._getBool(4)

    def setIsDisabled(self, value):
        self._setBool(4, value)
        return

    def getTooltipText(self):
        return self._getString(5)

    def setTooltipText(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(MemberCountDropdown, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addBoolProperty(b'isDisabled', False)
        self._addStringProperty(b'tooltipText', b'')
        return
