import BigWorld, armory_yard_constants

class AccountArmoryYardRerollComponent(BigWorld.StaticScriptComponent):

    def rerollArmoryQuestPaid(self, questID, rerollCost, rerollCurrency, callback=None):
        self.entity._doCmdIntStrArr(armory_yard_constants.CMD_REROLL_ARMORY_QUEST, rerollCost, (rerollCurrency,
         questID), callback)
        return

    def rerollArmoryQuestFree(self, questID, callback=None):
        self.entity._doCmdIntStrArr(armory_yard_constants.CMD_REROLL_ARMORY_QUEST, 0, (b'', questID), callback)
        return

    def acceptReroll(self, conditionID, questID, callback=None):
        self.entity._doCmdIntStr(armory_yard_constants.CMD_ACCEPT_REROLL_ARMORY_QUEST, conditionID, questID, callback)
        return
