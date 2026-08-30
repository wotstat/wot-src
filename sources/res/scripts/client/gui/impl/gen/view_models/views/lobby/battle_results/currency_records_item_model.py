from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_details_model import CurrencyRecordsItemDetailsModel

class CurrencyRecordsItemModel(ViewModel):
    __slots__ = ()
    CRYSTAL = b'crystal'
    XP_COST = b'xp'
    FREE_XP = b'freeXP'
    CREDITS = b'credits'
    GOLD = b'gold'
    COMMON_CURRENCY = b'commonCurrency'
    ORIGINAL_CRYSTALS = b'originalCrystals'
    EVENT_CRYSTALS = b'eventCrystals'
    AUTO_EQUIP_CRYSTALS = b'autoEquipCrystals'
    TOTAL_CRYSTALS = b'totalCrystals'
    ORIGINAL_XP = b'originalXP'
    ACHIEVEMENT_XP = b'achievementXP'
    FRIENDLY_FIRE_PENALTY_XP = b'originalXPPenalty'
    IGR_BONUS_XP = b'igrBonusXP'
    FIRST_WIN_XP = b'firstWinXP'
    ADDITIONAL_BONUS_XP = b'additionalBonusXP'
    BOOSTERS_XP = b'boostersXP'
    TACTICAL_TRAINING_XP = b'tacticalTrainingXP'
    EVENT_XP = b'eventXP'
    REFERRAL_BONUS_XP = b'referralBonusXP'
    PREMIUM_VEHICLE_XP = b'premiumVehicleXP'
    SQUAD_BONUS_XP = b'squadBonusXP'
    SQUAD_PENALTY_XP = b'squadPenaltyXP'
    WOT_PLUS_BONUS_XP = b'wotPlusBonusXP'
    WOT_PLUS_PRO_BOOST_XP = b'wotPlusProBoostXP'
    TOTAL_XP = b'totalXP'
    ORIGINAL_FREE_XP = b'originalFreeXP'
    ACHIEVEMENT_FREE_XP = b'achievementFreeXP'
    IGR_BONUS_FREE_XP = b'igrBonusFreeXP'
    FIRST_WIN_FREE_XP = b'firstWinFreeXP'
    ADDITIONAL_BONUS_FREE_XP = b'additionalBonusFreeXP'
    BOOSTERS_FREE_XP = b'boostersFreeXP'
    MILITARY_MANEUVERS_FREE_XP = b'militaryManeuversFreeXP'
    EVENT_FREE_XP = b'eventFreeXP'
    PREMIUM_VEHICLE_FREE_XP = b'premiumVehicleFreeXP'
    WOT_PLUS_BONUS_FREE_XP = b'wotPlusBonusFreeXP'
    WOT_PLUS_PRO_BOOST_FREE_XP = b'wotPlusProBoostFreeXP'
    TOTAL_FREE_XP = b'totalFreeXP'
    BASE_EARNED_CREDITS = b'baseEarnedCredits'
    SQUAD_BONUS_CREDITS = b'squadBonusCredits'
    ACHIEVEMENT_CREDITS = b'achievementCredits'
    BOOSTERS_CREDITS = b'boostersCredits'
    PET_SYSTEM_BONUS_CREDITS = b'petSystemBonusCredits'
    BATTLE_PAYMENTS_CREDITS = b'battlePaymentsCredits'
    EVENT_PAYMENTS_CREDITS = b'eventPaymentsCredits'
    REFERRAL_BONUS_CREDITS = b'referralBonusCredits'
    WOT_PLUS_BONUS_CREDITS = b'wotPlusBonusCredits'
    WOT_PLUS_PRO_BOOST_CREDITS = b'wotPlusProBoostCredits'
    FRIENDLY_FIRE_PENALTY_CREDITS = b'friendlyFirePenaltyCredits'
    FRIENDLY_FIRE_COMPENSATION_CREDITS = b'friendlyFireCompensationCredits'
    PIGGY_BANK_CREDITS = b'piggyBankCredits'
    AUTO_REPAIR_CREDITS = b'autoRepairCredits'
    AUTO_LOAD_CREDITS = b'autoLoadCredits'
    AUTO_EQUIP_CREDITS = b'autoEquipCredits'
    INTERMEDIATE_TOTAL_CREDITS = b'intermediateTotalCredits'
    TOTAL_CREDITS = b'totalCredits'
    GOLD_EVENT_PAYMENTS = b'goldEventPayments'
    GOLD_PIGGY_BANK = b'goldPiggyBank'
    INTERMEDIATE_TOTAL_GOLD = b'intermediateTotalGold'
    TOTAL_GOLD = b'totalGold'
    AOGAS_FACTOR = b'aogasFactor'
    DESERTER_VIOLATION = b'deserterViolation'
    AFK_VIOLATION = b'afkViolation'
    SUICIDE_VIOLATION = b'suicideViolation'

    def __init__(self, properties=5, commands=0):
        super(CurrencyRecordsItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamName(self):
        return self._getString(0)

    def setParamName(self, value):
        self._setString(0, value)
        return

    def getCurrencyType(self):
        return self._getString(1)

    def setCurrencyType(self, value):
        self._setString(1, value)
        return

    def getBaseValue(self):
        return self._getReal(2)

    def setBaseValue(self, value):
        self._setReal(2, value)
        return

    def getPremiumValue(self):
        return self._getReal(3)

    def setPremiumValue(self, value):
        self._setReal(3, value)
        return

    def getDetailedItemRecords(self):
        return self._getArray(4)

    def setDetailedItemRecords(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getDetailedItemRecordsType():
        return CurrencyRecordsItemDetailsModel

    def _initialize(self):
        super(CurrencyRecordsItemModel, self)._initialize()
        self._addStringProperty(b'paramName', b'')
        self._addStringProperty(b'currencyType', b'')
        self._addRealProperty(b'baseValue', 0.0)
        self._addRealProperty(b'premiumValue', 0.0)
        self._addArrayProperty(b'detailedItemRecords', Array())
        return
