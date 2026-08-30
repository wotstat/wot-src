from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.info_tip_model import InfoTipModel
from gui.impl.gen.view_models.views.lobby.crew.mentor_assigment_tankman_model import MentorAssigmentTankmanModel

class MentorAssigmentViewModel(BaseCrewViewModel):
    __slots__ = (b'onResetFilters', b'onLoadCards', b'onTankmanSelected', b'onCardMouseEnter', b'onCardMouseLeave', b'onTipClose', b'onTipsReadyToShow')

    def __init__(self, properties=10, commands=11):
        super(MentorAssigmentViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedTankmanID(self):
        return self._getNumber(2)

    def setSelectedTankmanID(self, value):
        self._setNumber(2, value)
        return

    def getLicensesAmount(self):
        return self._getNumber(3)

    def setLicensesAmount(self, value):
        self._setNumber(3, value)
        return

    def getNation(self):
        return self._getString(4)

    def setNation(self, value):
        self._setString(4, value)
        return

    def getHasFilters(self):
        return self._getBool(5)

    def setHasFilters(self, value):
        self._setBool(5, value)
        return

    def getItemsAmount(self):
        return self._getNumber(6)

    def setItemsAmount(self, value):
        self._setNumber(6, value)
        return

    def getItemsOffset(self):
        return self._getNumber(7)

    def setItemsOffset(self, value):
        self._setNumber(7, value)
        return

    def getTankmanList(self):
        return self._getArray(8)

    def setTankmanList(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getTankmanListType():
        return MentorAssigmentTankmanModel

    def getTips(self):
        return self._getArray(9)

    def setTips(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getTipsType():
        return InfoTipModel

    def _initialize(self):
        super(MentorAssigmentViewModel, self)._initialize()
        self._addNumberProperty(b'selectedTankmanID', 0)
        self._addNumberProperty(b'licensesAmount', 0)
        self._addStringProperty(b'nation', b'')
        self._addBoolProperty(b'hasFilters', False)
        self._addNumberProperty(b'itemsAmount', 0)
        self._addNumberProperty(b'itemsOffset', 0)
        self._addArrayProperty(b'tankmanList', Array())
        self._addArrayProperty(b'tips', Array())
        self.onResetFilters = self._addCommand(b'onResetFilters')
        self.onLoadCards = self._addCommand(b'onLoadCards')
        self.onTankmanSelected = self._addCommand(b'onTankmanSelected')
        self.onCardMouseEnter = self._addCommand(b'onCardMouseEnter')
        self.onCardMouseLeave = self._addCommand(b'onCardMouseLeave')
        self.onTipClose = self._addCommand(b'onTipClose')
        self.onTipsReadyToShow = self._addCommand(b'onTipsReadyToShow')
        return
