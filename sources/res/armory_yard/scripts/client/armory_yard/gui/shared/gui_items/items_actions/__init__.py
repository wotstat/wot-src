from gui.shared.gui_items.items_actions.factory import registerAction
from armory_yard.gui.shared.gui_items.items_actions.actions import CollectRewardsAction, BuyStepTokensAction, RerollQuestAction, AcceptRerollAction
COLLECT_REWARDS = b'collectRewards'
BUY_STEP_TOKENS = b'buyStepTokens'
BUY_PURCHASE_STAGE_TOKENS = b'buyStepTokens'
REROLL_QUEST = b'rerollQuest'
ACCEPT_REROLL = b'acceptReroll'

def registerActions():
    registerAction(COLLECT_REWARDS, CollectRewardsAction)
    registerAction(BUY_STEP_TOKENS, BuyStepTokensAction)
    registerAction(REROLL_QUEST, RerollQuestAction)
    registerAction(ACCEPT_REROLL, AcceptRerollAction)
    return
