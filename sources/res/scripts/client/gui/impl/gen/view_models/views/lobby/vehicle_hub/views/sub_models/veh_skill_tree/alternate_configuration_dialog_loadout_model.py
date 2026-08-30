from enum import Enum
from frameworks.wulf import ViewModel

class LoadoutType(Enum):
    SHELLSCONSUMABLESSWITCH = b'shellsConsumablesSwitch'
    OPTDEVBOOSTERSSWITCH = b'optDevBoostersSwitch'


class AlternateConfigurationDialogLoadoutModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AlternateConfigurationDialogLoadoutModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return LoadoutType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getIconName(self):
        return self._getString(1)

    def setIconName(self, value):
        self._setString(1, value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(AlternateConfigurationDialogLoadoutModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addStringProperty(b'iconName', b'')
        self._addBoolProperty(b'isSelected', False)
        return
