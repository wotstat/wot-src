from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class ClanSupplyRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.CLAN_SUPPLY_GET_QUESTS): (self.__getQuests), 
           (WebRequestDataType.CLAN_SUPPLY_POST_QUESTS): (self.__postQuests), 
           (WebRequestDataType.CLAN_SUPPLY_CLAIM_QUESTS_REWARDS): (self.__claimQuestRewards), 
           (WebRequestDataType.CLAN_SUPPLY_GET_PROGRESSION_SETTINGS): (self.__getProgressionSettings), 
           (WebRequestDataType.CLAN_SUPPLY_GET_PROGRESSION_PROGRESS): (self.__getProgressionProgress), 
           (WebRequestDataType.CLAN_SUPPLY_PURCHASE_PROGRESSION_STAGE): (self.__purchaseProgressionStage)}
        return handlers

    def __getQuests(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clan_supply', b'get_clan_supply_quests'))

    def __postQuests(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clan_supply', b'post_clan_supply_quests'))

    def __claimQuestRewards(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clan_supply', b'claim_quest_rewards'))

    def __getProgressionSettings(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clan_supply', b'get_progression_settings'))

    def __getProgressionProgress(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clan_supply', b'get_progression_progress'))

    def __purchaseProgressionStage(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clan_supply', b'purchase_progression_stage'), *ctx.getRequestArgs())
