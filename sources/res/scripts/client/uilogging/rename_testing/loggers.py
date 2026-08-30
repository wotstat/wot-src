from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
from uilogging.base.logger import MetricsLogger
from uilogging.rename_testing.constants import FEATURE, RENAME_TESTING_ACTION_CLICK, RenameTestingItems

@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def _renameTestingPartnerID(connectionMgr=None):
    return str(connectionMgr.lastSessionID or b'')


class RenameTestingUILogger(MetricsLogger):
    __slots__ = (b'__partnerID',)

    def __init__(self):
        super(RenameTestingUILogger, self).__init__(FEATURE)
        self.__partnerID = _renameTestingPartnerID()
        return

    def __logClick(self, item):
        self.log(action=RENAME_TESTING_ACTION_CLICK, item=item, partnerID=self.__partnerID)
        return

    def logHangarEnter(self):
        self.__logClick(RenameTestingItems.HANGAR_ENTER)
        return

    def logModeSelectorOpen(self):
        self.__logClick(RenameTestingItems.MODE_SELECTOR_OPEN)
        return

    def logTrainingModSelectorItem(self):
        self.__logClick(RenameTestingItems.TRAINING_MODE_SELECTOR_CARD)
        return

    def logTrainingOpenCreateRoomDialog(self):
        self.__logClick(RenameTestingItems.TRAINING_OPEN_CREATE_ROOM_DIALOG)
        return

    def logTrainingJoinRoom(self):
        self.__logClick(RenameTestingItems.TRAINING_JOIN_ROOM)
        return

    def logPlatoonMenuSection(self):
        self.__logClick(RenameTestingItems.PLATOON_MENU_SECTION)
        return

    def logCreateNewPlatoon(self):
        self.__logClick(RenameTestingItems.CREATE_NEW_PLATOON)
        return

    def logPlatoonFindPlayers(self):
        self.__logClick(RenameTestingItems.PLATOON_FIND_PLAYERS)
        return

    def logPlatoonReadyButton(self):
        self.__logClick(RenameTestingItems.PLATOON_READY_BUTTON)
        return

    def logPlatoonFightButton(self):
        self.__logClick(RenameTestingItems.PLATOON_FIGHT_BUTTON)
        return

    def logTrainingStartBattle(self):
        self.__logClick(RenameTestingItems.TRAINING_START_BATTLE)
        return

    def logTrainingCreateRoom(self):
        self.__logClick(RenameTestingItems.TRAINING_CREATE_ROOM)
        return
