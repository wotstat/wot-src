from constants import PREBATTLE_TYPE
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.legacy.ctx import TeamSettingsCtx, JoinLegacyCtx
from gui.shared.utils.decorators import ReprInjector
_REQUEST_TYPE = prb_settings.REQUEST_TYPE
_FUNCTIONAL_FLAG = prb_settings.FUNCTIONAL_FLAG

@ReprInjector.withParent((b'__arenaTypeID', b'arenaTypeID'), (b'__roundLen', b'roundLen'))
class EpicTrainingSettingsCtx(TeamSettingsCtx):
    __slots__ = (b'__arenaTypeID', b'__roundLen')

    def __init__(self, waitingID=b'', isOpened=True, comment=b'', isRequestToCreate=True, arenaTypeID=0, roundLen=900, flags=_FUNCTIONAL_FLAG.UNDEFINED):
        super(EpicTrainingSettingsCtx, self).__init__(PREBATTLE_TYPE.EPIC_TRAINING, waitingID=waitingID, isOpened=isOpened, comment=comment, isRequestToCreate=isRequestToCreate, flags=flags)
        self.__arenaTypeID = arenaTypeID
        self.__roundLen = int(roundLen)
        return

    @classmethod
    def fetch(cls, settings):
        return EpicTrainingSettingsCtx(isOpened=settings[b'isOpened'], comment=settings[b'comment'], isRequestToCreate=False, arenaTypeID=settings[b'arenaTypeID'], roundLen=settings[b'roundLength'])

    def getArenaTypeID(self):
        return self.__arenaTypeID

    def setArenaTypeID(self, arenaTypeID):
        self.__arenaTypeID = arenaTypeID
        return

    def getRoundLen(self):
        return self.__roundLen

    def setRoundLen(self, roundLen):
        self.__roundLen = int(roundLen)
        return

    def isArenaTypeIDChanged(self, settings):
        return self.__arenaTypeID != settings[prb_settings.PREBATTLE_SETTING_NAME.ARENA_TYPE_ID]

    def isRoundLenChanged(self, settings):
        return self.__roundLen != settings[prb_settings.PREBATTLE_SETTING_NAME.ROUND_LENGTH]

    def areSettingsChanged(self, settings):
        return super(EpicTrainingSettingsCtx, self).areSettingsChanged(settings) or self.isArenaTypeIDChanged(settings) or self.isRoundLenChanged(settings)


class JoinEpicBattleTrainingCtx(JoinLegacyCtx):
    __slots__ = ()

    def __init__(self, prbID, prbClusterID, waitingID=b'', flags=_FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinEpicBattleTrainingCtx, self).__init__(prbID, PREBATTLE_TYPE.EPIC_TRAINING, prbClusterID, waitingID=waitingID, flags=flags)
        return
