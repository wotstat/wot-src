import logging, WWISE
from helpers import time_utils
_logger = logging.getLogger(__name__)

class BattleResultsBonusConstants(object):
    MAX_MULTIPLIER = 5
    MIN_MULTIPLIER = 1
    LOST_BATTLE_BACKGROUND_MULTIPLIER = 1


class PiggyBankConstants(object):
    MAX_AMOUNT = 750000
    MAX_AMOUNT_GOLD = 500
    SMASH_MAX_DELAY = 300
    OPEN_SOON_THRESHOLD_DEFAULT = 86400
    PIGGY_BANK_CREDITS = b'piggyBank.credits'
    PIGGY_BANK_GOLD = b'piggyBank.gold'
    PIGGY_BANK = b'piggyBank'
    PIGGY_BANK_SMASH_TIMESTAMP_CREDITS = b'piggyBank.lastSmashTimestamp'
    PIGGY_BANK_SMASH_TIMESTAMP_GOLD = b'piggyBank.lastSmashTimestampGold'


def validateAdditionalBonusMultiplier(multiplier):
    if multiplier < BattleResultsBonusConstants.MIN_MULTIPLIER or multiplier > BattleResultsBonusConstants.MAX_MULTIPLIER:
        return BattleResultsBonusConstants.MIN_MULTIPLIER
    return int(multiplier)


def getOpenTimeHelper(config, data):
    if not config or not data:
        _logger.error(b'Incorrect config or data given')
        return 0
    lastSmashTimestamp = data.get(b'lastSmashTimestamp', 0)
    cycleLength = config.get(b'cycleLength', 0)
    cycleStartTime = config.get(b'cycleStartTime', 0)
    if cycleLength <= 0:
        return 0
    if lastSmashTimestamp <= cycleStartTime:
        openTime = cycleStartTime
    else:
        openTime = cycleStartTime + ((lastSmashTimestamp - cycleStartTime) / cycleLength + 1) * cycleLength
    openTime += PiggyBankConstants.SMASH_MAX_DELAY
    return time_utils.makeLocalServerTime(openTime)


def getDeltaTimeHelper(config, data):
    return time_utils.getTimeDeltaFromNow(getOpenTimeHelper(config, data))


class SoundViewMixin(object):
    PREM_VIEW_STATE_TEMPL = b'STATE_hangar_filtered'
    PREM_VIEW_STATE_ENTER = (b'{}_on').format(PREM_VIEW_STATE_TEMPL)
    PREM_VIEW_STATE_EXIT = (b'{}_off').format(PREM_VIEW_STATE_TEMPL)
    __globSoundEntryCount = 0

    @classmethod
    def _addSoundEvent(cls):
        WWISE.WW_setState(cls.PREM_VIEW_STATE_TEMPL, cls.PREM_VIEW_STATE_ENTER)
        SoundViewMixin.__globSoundEntryCount += 1
        return

    @classmethod
    def _removeSoundEvent(cls):
        if SoundViewMixin.__globSoundEntryCount > 0:
            SoundViewMixin.__globSoundEntryCount -= 1
        if SoundViewMixin.__globSoundEntryCount == 0:
            WWISE.WW_setState(cls.PREM_VIEW_STATE_TEMPL, cls.PREM_VIEW_STATE_EXIT)
        return
