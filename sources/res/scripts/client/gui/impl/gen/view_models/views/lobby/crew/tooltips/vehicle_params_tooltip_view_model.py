from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_category import VehicleParamsCategory
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_item import VehicleParamsItem
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_note import VehicleParamsNote

class VehicleParamsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(VehicleParamsTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getUnitOfMeasurement(self):
        return self._getString(1)

    def setUnitOfMeasurement(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getHeaderNotes(self):
        return self._getArray(3)

    def setHeaderNotes(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getHeaderNotesType():
        return VehicleParamsNote

    def getIcon(self):
        return self._getResource(4)

    def setIcon(self, value):
        self._setResource(4, value)
        return

    def getCategories(self):
        return self._getArray(5)

    def setCategories(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getCategoriesType():
        return VehicleParamsCategory

    def getPenalties(self):
        return self._getArray(6)

    def setPenalties(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getPenaltiesType():
        return VehicleParamsItem

    def getIsNotFullCrew(self):
        return self._getBool(7)

    def setIsNotFullCrew(self, value):
        self._setBool(7, value)
        return

    def getFooterNotes(self):
        return self._getArray(8)

    def setFooterNotes(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getFooterNotesType():
        return VehicleParamsNote

    def getIsAdvanced(self):
        return self._getBool(9)

    def setIsAdvanced(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(VehicleParamsTooltipViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'unitOfMeasurement', b'')
        self._addStringProperty(b'description', b'')
        self._addArrayProperty(b'headerNotes', Array())
        self._addResourceProperty(b'icon', R.invalid())
        self._addArrayProperty(b'categories', Array())
        self._addArrayProperty(b'penalties', Array())
        self._addBoolProperty(b'isNotFullCrew', False)
        self._addArrayProperty(b'footerNotes', Array())
        self._addBoolProperty(b'isAdvanced', False)
        return
