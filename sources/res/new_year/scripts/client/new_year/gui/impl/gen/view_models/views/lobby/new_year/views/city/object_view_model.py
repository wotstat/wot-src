from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.city.group_slots_model import GroupSlotsModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.customization_zone.customization_zone_model import CustomizationZoneModel

class ObjectViewModel(ViewModel):
    __slots__ = (b'onGoToCustomizationObject', b'onClose', b'onEscape')

    def __init__(self, properties=5, commands=3):
        super(ObjectViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def groupSlots(self):
        return self._getViewModel(0)

    @staticmethod
    def getGroupSlotsType():
        return GroupSlotsModel

    @property
    def customizationZoneObject(self):
        return self._getViewModel(1)

    @staticmethod
    def getCustomizationZoneObjectType():
        return CustomizationZoneModel

    def getCurrentObject(self):
        return self._getString(2)

    def setCurrentObject(self, value):
        self._setString(2, value)
        return

    def getNextObject(self):
        return self._getString(3)

    def setNextObject(self, value):
        self._setString(3, value)
        return

    def getPrevObject(self):
        return self._getString(4)

    def setPrevObject(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(ObjectViewModel, self)._initialize()
        self._addViewModelProperty(b'groupSlots', UserListModel())
        self._addViewModelProperty(b'customizationZoneObject', CustomizationZoneModel())
        self._addStringProperty(b'currentObject', b'')
        self._addStringProperty(b'nextObject', b'')
        self._addStringProperty(b'prevObject', b'')
        self.onGoToCustomizationObject = self._addCommand(b'onGoToCustomizationObject')
        self.onClose = self._addCommand(b'onClose')
        self.onEscape = self._addCommand(b'onEscape')
        return
