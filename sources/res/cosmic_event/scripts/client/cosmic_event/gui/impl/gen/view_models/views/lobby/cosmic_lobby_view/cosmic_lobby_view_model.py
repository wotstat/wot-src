from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.cosmic_lobby_view.medal_model import MedalModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.cosmic_lobby_view.progression_model import ProgressionModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.cosmic_lobby_view.rovers_model import RoversModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.cosmic_lobby_view.scoring_model import ScoringModel
from gui.impl.gen.view_models.views.lobby.daily.widget_quest_model import WidgetQuestModel

class LobbyRouteEnum(Enum):
    MAIN = b'main'
    ARTEFACT = b'artefact'
    PICKUPS = b'pickups'


class RoverEnum(IntEnum):
    OLD = 1
    NEW = 2


class CosmicLobbyViewModel(ViewModel):
    __slots__ = (b'onLobbyRouteChange', b'onClose', b'onAboutEvent', b'onShopClicked', b'onVehicleChange')

    def __init__(self, properties=20, commands=5):
        super(CosmicLobbyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getFadeOut(self):
        return self._getBool(0)

    def setFadeOut(self, value):
        self._setBool(0, value)
        return

    def getCurrentProgressSectionIndex(self):
        return self._getNumber(1)

    def setCurrentProgressSectionIndex(self, value):
        self._setNumber(1, value)
        return

    def getMarsPoints(self):
        return self._getNumber(2)

    def setMarsPoints(self, value):
        self._setNumber(2, value)
        return

    def getMarsPointsLimit(self):
        return self._getNumber(3)

    def setMarsPointsLimit(self, value):
        self._setNumber(3, value)
        return

    def getArtefactProgressDeltaFrom(self):
        return self._getNumber(4)

    def setArtefactProgressDeltaFrom(self, value):
        self._setNumber(4, value)
        return

    def getMarsPointsEarnedToday(self):
        return self._getNumber(5)

    def setMarsPointsEarnedToday(self, value):
        self._setNumber(5, value)
        return

    def getMarsPointsTodaysLimit(self):
        return self._getNumber(6)

    def setMarsPointsTodaysLimit(self, value):
        self._setNumber(6, value)
        return

    def getLobbyRoute(self):
        return LobbyRouteEnum(self._getString(7))

    def setLobbyRoute(self, value):
        self._setString(7, value.value)
        return

    def getIsVehicleInBattle(self):
        return self._getBool(8)

    def setIsVehicleInBattle(self, value):
        self._setBool(8, value)
        return

    def getSelectedVehicle(self):
        return RoverEnum(self._getNumber(9))

    def setSelectedVehicle(self, value):
        self._setNumber(9, value.value)
        return

    def getSelectedVehicleResource(self):
        return self._getString(10)

    def setSelectedVehicleResource(self, value):
        self._setString(10, value)
        return

    def getIsSomethingHappeningWithArtefact(self):
        return self._getBool(11)

    def setIsSomethingHappeningWithArtefact(self, value):
        self._setBool(11, value)
        return

    def getLastVisitedProgressionLevel(self):
        return self._getNumber(12)

    def setLastVisitedProgressionLevel(self, value):
        self._setNumber(12, value)
        return

    def getIsProgressionFinished(self):
        return self._getBool(13)

    def setIsProgressionFinished(self, value):
        self._setBool(13, value)
        return

    def getMedals(self):
        return self._getArray(14)

    def setMedals(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getMedalsType():
        return MedalModel

    def getScoring(self):
        return self._getArray(15)

    def setScoring(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getScoringType():
        return ScoringModel

    def getMissions(self):
        return self._getArray(16)

    def setMissions(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getMissionsType():
        return WidgetQuestModel

    def getProgression(self):
        return self._getArray(17)

    def setProgression(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getProgressionType():
        return ProgressionModel

    def getRovers(self):
        return self._getArray(18)

    def setRovers(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getRoversType():
        return RoversModel

    def getQuestTimer(self):
        return self._getNumber(19)

    def setQuestTimer(self, value):
        self._setNumber(19, value)
        return

    def _initialize(self):
        super(CosmicLobbyViewModel, self)._initialize()
        self._addBoolProperty(b'fadeOut', False)
        self._addNumberProperty(b'currentProgressSectionIndex', 0)
        self._addNumberProperty(b'marsPoints', 0)
        self._addNumberProperty(b'marsPointsLimit', 0)
        self._addNumberProperty(b'artefactProgressDeltaFrom', 0)
        self._addNumberProperty(b'marsPointsEarnedToday', 0)
        self._addNumberProperty(b'marsPointsTodaysLimit', 0)
        self._addStringProperty(b'lobbyRoute', LobbyRouteEnum.MAIN.value)
        self._addBoolProperty(b'isVehicleInBattle', False)
        self._addNumberProperty(b'selectedVehicle', RoverEnum.OLD.value)
        self._addStringProperty(b'selectedVehicleResource', b'')
        self._addBoolProperty(b'isSomethingHappeningWithArtefact', False)
        self._addNumberProperty(b'lastVisitedProgressionLevel', 0)
        self._addBoolProperty(b'isProgressionFinished', False)
        self._addArrayProperty(b'medals', Array())
        self._addArrayProperty(b'scoring', Array())
        self._addArrayProperty(b'missions', Array())
        self._addArrayProperty(b'progression', Array())
        self._addArrayProperty(b'rovers', Array())
        self._addNumberProperty(b'questTimer', 0)
        self.onLobbyRouteChange = self._addCommand(b'onLobbyRouteChange')
        self.onClose = self._addCommand(b'onClose')
        self.onAboutEvent = self._addCommand(b'onAboutEvent')
        self.onShopClicked = self._addCommand(b'onShopClicked')
        self.onVehicleChange = self._addCommand(b'onVehicleChange')
        return
