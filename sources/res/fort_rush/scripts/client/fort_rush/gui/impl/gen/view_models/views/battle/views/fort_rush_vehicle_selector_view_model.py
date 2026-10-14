from enum import Enum
from frameworks.wulf import Array, ViewModel
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_playlist_item_model import FortRushPlaylistItemModel

class AnnouncementTypeEnum(Enum):
    NONE = b'none'
    TEXT = b'text'
    RESPAWN = b'respawn'


class FortRushVehicleSelectorViewModel(ViewModel):
    __slots__ = (b'onTankSelected', b'onBattleButtonClicked')

    def __init__(self, properties=10, commands=2):
        super(FortRushVehicleSelectorViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedTankId(self):
        return self._getNumber(0)

    def setSelectedTankId(self, value):
        self._setNumber(0, value)
        return

    def getIsAnnouncementVisible(self):
        return self._getBool(1)

    def setIsAnnouncementVisible(self, value):
        self._setBool(1, value)
        return

    def getAnnouncementCountdownTargetTime(self):
        return self._getReal(2)

    def setAnnouncementCountdownTargetTime(self, value):
        self._setReal(2, value)
        return

    def getAnnouncementHeading(self):
        return self._getString(3)

    def setAnnouncementHeading(self, value):
        self._setString(3, value)
        return

    def getAnnouncementDescription(self):
        return self._getString(4)

    def setAnnouncementDescription(self, value):
        self._setString(4, value)
        return

    def getAnnouncementType(self):
        return AnnouncementTypeEnum(self._getString(5))

    def setAnnouncementType(self, value):
        self._setString(5, value.value)
        return

    def getSelectedPlaylistId(self):
        return self._getString(6)

    def setSelectedPlaylistId(self, value):
        self._setString(6, value)
        return

    def getPlaylists(self):
        return self._getArray(7)

    def setPlaylists(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getPlaylistsType():
        return FortRushPlaylistItemModel

    def getEligibleVehicleTiers(self):
        return self._getArray(8)

    def setEligibleVehicleTiers(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getEligibleVehicleTiersType():
        return int

    def getForbiddenVehClasses(self):
        return self._getArray(9)

    def setForbiddenVehClasses(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getForbiddenVehClassesType():
        return unicode

    def _initialize(self):
        super(FortRushVehicleSelectorViewModel, self)._initialize()
        self._addNumberProperty(b'selectedTankId', 0)
        self._addBoolProperty(b'isAnnouncementVisible', False)
        self._addRealProperty(b'announcementCountdownTargetTime', -1)
        self._addStringProperty(b'announcementHeading', b'')
        self._addStringProperty(b'announcementDescription', b'')
        self._addStringProperty(b'announcementType', AnnouncementTypeEnum.NONE.value)
        self._addStringProperty(b'selectedPlaylistId', b'')
        self._addArrayProperty(b'playlists', Array())
        self._addArrayProperty(b'eligibleVehicleTiers', Array())
        self._addArrayProperty(b'forbiddenVehClasses', Array())
        self.onTankSelected = self._addCommand(b'onTankSelected')
        self.onBattleButtonClicked = self._addCommand(b'onBattleButtonClicked')
        return
