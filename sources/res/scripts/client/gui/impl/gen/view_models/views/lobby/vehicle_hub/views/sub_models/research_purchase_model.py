from frameworks.wulf import ViewModel

class ResearchPurchaseModel(ViewModel):
    __slots__ = (b'onAction', b'onBlueprint')
    ACTION_RESEARCH = b'action_research'
    ACTION_PURCHASE = b'action_purchase'
    ACTION_PURCHASE_CAN_VIEW_IN_GARAGE = b'action_purchase_can_view_in_garage'
    ACTION_PURCHASE_SHOP = b'action_purchase_shop'
    ACTION_RESTORE = b'action_restore'
    ACTION_IN_GARAGE = b'action_in_garage'
    ACTION_TO_LOOTBOX = b'action_in_lootbox'
    ACTION_PURCHASE_LOOTBOX = b'action_purchase_lootbox'
    ACTION_STATE_ENABLED = b'action_state_enabled'
    ACTION_STATE_DISABLED = b'action_state_disabled'
    ACTION_DESC_NOT_ENOUGH_CREDITS = b'notEnoughCredits'
    ACTION_DESC_NOT_ENOUGH_XP = b'notEnoughXp'
    ACTION_DESC_PARENT_MODULE_IS_LOCKED = b'parentModuleIsLocked'
    ACTION_DESC_WALLET_UNAVAILABLE = b'walletUnavailable'
    ACTION_DESC_RESTORE_REQUESTED = b'restoreRequested'
    ACTION_READY_FOR_TRADE_IN = b'readyForTradeIn'

    def __init__(self, properties=19, commands=2):
        super(ResearchPurchaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getAction(self):
        return self._getString(0)

    def setAction(self, value):
        self._setString(0, value)
        return

    def getActionState(self):
        return self._getString(1)

    def setActionState(self, value):
        self._setString(1, value)
        return

    def getActionStateReason(self):
        return self._getString(2)

    def setActionStateReason(self, value):
        self._setString(2, value)
        return

    def getPrice(self):
        return self._getNumber(3)

    def setPrice(self, value):
        self._setNumber(3, value)
        return

    def getOldPrice(self):
        return self._getNumber(4)

    def setOldPrice(self, value):
        self._setNumber(4, value)
        return

    def getPriceDiscount(self):
        return self._getNumber(5)

    def setPriceDiscount(self, value):
        self._setNumber(5, value)
        return

    def getCurrency(self):
        return self._getString(6)

    def setCurrency(self, value):
        self._setString(6, value)
        return

    def getBlueprintFragments(self):
        return self._getNumber(7)

    def setBlueprintFragments(self, value):
        self._setNumber(7, value)
        return

    def getBlueprintTotal(self):
        return self._getNumber(8)

    def setBlueprintTotal(self, value):
        self._setNumber(8, value)
        return

    def getCombatXp(self):
        return self._getNumber(9)

    def setCombatXp(self, value):
        self._setNumber(9, value)
        return

    def getFreeXp(self):
        return self._getNumber(10)

    def setFreeXp(self, value):
        self._setNumber(10, value)
        return

    def getTimeLeft(self):
        return self._getNumber(11)

    def setTimeLeft(self, value):
        self._setNumber(11, value)
        return

    def getCooldownTimeLeft(self):
        return self._getNumber(12)

    def setCooldownTimeLeft(self, value):
        self._setNumber(12, value)
        return

    def getNotInShopVehicle(self):
        return self._getBool(13)

    def setNotInShopVehicle(self, value):
        self._setBool(13, value)
        return

    def getPromoTitle(self):
        return self._getString(14)

    def setPromoTitle(self, value):
        self._setString(14, value)
        return

    def getPromoFinishTime(self):
        return self._getNumber(15)

    def setPromoFinishTime(self, value):
        self._setNumber(15, value)
        return

    def getCanTradeIn(self):
        return self._getBool(16)

    def setCanTradeIn(self, value):
        self._setBool(16, value)
        return

    def getPremium(self):
        return self._getBool(17)

    def setPremium(self, value):
        self._setBool(17, value)
        return

    def getElite(self):
        return self._getBool(18)

    def setElite(self, value):
        self._setBool(18, value)
        return

    def _initialize(self):
        super(ResearchPurchaseModel, self)._initialize()
        self._addStringProperty(b'action', b'')
        self._addStringProperty(b'actionState', b'')
        self._addStringProperty(b'actionStateReason', b'')
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'oldPrice', 0)
        self._addNumberProperty(b'priceDiscount', 0)
        self._addStringProperty(b'currency', b'')
        self._addNumberProperty(b'blueprintFragments', 0)
        self._addNumberProperty(b'blueprintTotal', 0)
        self._addNumberProperty(b'combatXp', 0)
        self._addNumberProperty(b'freeXp', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'cooldownTimeLeft', 0)
        self._addBoolProperty(b'notInShopVehicle', False)
        self._addStringProperty(b'promoTitle', b'')
        self._addNumberProperty(b'promoFinishTime', 0)
        self._addBoolProperty(b'canTradeIn', False)
        self._addBoolProperty(b'premium', False)
        self._addBoolProperty(b'elite', False)
        self.onAction = self._addCommand(b'onAction')
        self.onBlueprint = self._addCommand(b'onBlueprint')
        return
