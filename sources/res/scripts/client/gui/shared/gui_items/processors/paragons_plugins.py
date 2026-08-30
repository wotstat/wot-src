import typing
from gui.shared.gui_items.processors.plugins import SyncValidator, makeSuccess, makeError
from helpers import dependency
from paragons_common import getAllParagonsEntitlements, PARAGONS_SELECTED_REWARD_TOKEN_PREFIX
from skeletons.gui.game_control import IParagonsController
from skeletons.gui.shared import IItemsCache

class ParagonsResetBranchValidator(SyncValidator):
    __slots__ = (b'__branchID',)
    __paragonsController = dependency.descriptor(IParagonsController)

    def __init__(self, branchID, isEnabled=True):
        super(ParagonsResetBranchValidator, self).__init__(isEnabled)
        self.__branchID = branchID
        return

    def _validate(self):
        if self.__branchID in self.__paragonsController.branches.availableToResetBranchIds:
            return makeSuccess()
        return makeError(b'branch_is_not_available_for_reset')


class ParagonsChapterValidator(SyncValidator):
    __slots__ = (b'__chapterID',)
    __paragonsController = dependency.descriptor(IParagonsController)

    def __init__(self, chapterID, isEnabled=True):
        super(ParagonsChapterValidator, self).__init__(isEnabled)
        self.__chapterID = chapterID
        return

    def _validate(self):
        if self.__chapterID in self.__paragonsController.allChapterIDs:
            return makeSuccess()
        return makeError((b'nonexistent chapter with chapterID={}').format(self.__chapterID))


class ParagonsChapterLevelValidator(SyncValidator):
    __slots__ = (b'__chapterID', b'__levelID')
    __paragonsController = dependency.descriptor(IParagonsController)

    def __init__(self, chapterID, levelID, isEnabled=True):
        super(ParagonsChapterLevelValidator, self).__init__(isEnabled)
        self.__chapterID = chapterID
        self.__levelID = levelID
        return

    def _validate(self):
        if self.__levelID in self.__paragonsController.config.getChapterLevelIDs(self.__chapterID):
            return makeSuccess()
        return makeError((b'nonexistent level id {} in chapterID={}').format(self.__levelID, self.__chapterID))


class ParagonsValidateSelectedRewardEntCode(SyncValidator):
    __slots__ = (b'__entCode',)

    def __init__(self, entCode, isEnabled=True):
        super(ParagonsValidateSelectedRewardEntCode, self).__init__(isEnabled)
        self.__entCode = entCode
        return

    def _validate(self):
        if self.__entCode in getAllParagonsEntitlements():
            return makeSuccess()
        return makeError((b'wrong entitlement for mark {}').format(self.__entCode))


class ParagonsValidateSelectedRewardToken(SyncValidator):
    __slots__ = (b'__tokenID',)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, tokenID, isEnabled=True):
        super(ParagonsValidateSelectedRewardToken, self).__init__(isEnabled)
        self.__tokenID = tokenID
        return

    def _validate(self):
        if self.__tokenID.startswith(PARAGONS_SELECTED_REWARD_TOKEN_PREFIX) and self.__itemsCache.items.tokens.isTokenAvailable(self.__tokenID):
            return makeSuccess()
        return makeError((b'wrong token for mark {}').format(self.__tokenID))


class ParagonsValidateSelectedRewardInOrder(SyncValidator):
    __slots__ = (b'__entCode', b'__chapterID', b'__levelID', b'__bonusCD')
    __paragonsController = dependency.descriptor(IParagonsController)

    def __init__(self, chapterID, levelID, entCode, tokenID, isEnabled=True):
        super(ParagonsValidateSelectedRewardInOrder, self).__init__(isEnabled)
        self.__entCode = entCode
        self.__chapterID = chapterID
        self.__levelID = levelID
        self.__bonusCD = tokenID.split(b':')[-1]
        return

    def _validate(self):
        if (self.__chapterID, self.__levelID, self.__entCode) not in self.__paragonsController.paragons.storage.selectedRewards:
            return makeSuccess()
        return makeError((b'reward already added to order {} {} {}').format(self.__chapterID, self.__levelID, self.__entCode, self.__bonusCD))


class ParagonsChangeChapterValidator(SyncValidator):
    __slots__ = (b'__chapterID',)
    __paragonsController = dependency.descriptor(IParagonsController)

    def __init__(self, chapterID, isEnabled=True):
        super(ParagonsChangeChapterValidator, self).__init__(isEnabled)
        self.__chapterID = chapterID
        return

    def _validate(self):
        if self.__chapterID == self.__paragonsController.chapterID:
            return makeError((b'chapter with ID={} is active').format(self.__chapterID))
        if self.__paragonsController.isChapterComplete(self.__chapterID):
            return makeError((b'chapter with ID={} is completed').format(self.__chapterID))
        if self.__chapterID in self.__paragonsController.config.getAnnouncementChapterIDs():
            return makeError((b'chapter with ID={} is announcement').format(self.__chapterID))
        return makeSuccess()
