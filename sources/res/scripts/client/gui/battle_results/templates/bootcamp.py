from gui.battle_results.components import base, bootcamp
_BOOTCAMP_VO_META = base.DictMeta({b'background': b'', 
   b'rewards': {b'medals': [], b'ribbons': [], b'unlocks': []}, b'hasUnlocks': False, 
   b'stats': [], b'resultTypeStr': b'', 
   b'finishReasonStr': b'', 
   b'showRewards': False, 
   b'credits': {b'value': 0, b'str': b'0'}, b'xp': {b'value': 0, b'str': b'0'}, b'finishReason': b'', 
   b'playerResult': b'', 
   b'videoButtons': [], b'alternativeLayout': False})
_BOOTCAMP_REWARDS_VO_META = base.DictMeta({b'medals': [], b'ribbons': [], b'unlocks': []})
_BOOTCAMP_STATVALUE_VO_META = base.DictMeta({b'value': 0, 
   b'str': b'0'})
BOOTCAMP_RESULTS_BLOCK = base.StatsBlock(_BOOTCAMP_VO_META, b'')
BOOTCAMP_RESULTS_BLOCK.addComponent(0, bootcamp.BackgroundItem(b'background'))
BOOTCAMP_RESULTS_BLOCK.addComponent(1, bootcamp.RewardsBlock(_BOOTCAMP_REWARDS_VO_META, b'rewards'))
BOOTCAMP_RESULTS_BLOCK.addComponent(2, bootcamp.HasUnlocksFlag(b'hasUnlocks'))
BOOTCAMP_RESULTS_BLOCK.addComponent(3, bootcamp.StatsBlock(base.ListMeta(), b'stats'))
BOOTCAMP_RESULTS_BLOCK.addComponent(4, bootcamp.ResultTypeStrItem(b'resultTypeStr'))
BOOTCAMP_RESULTS_BLOCK.addComponent(5, bootcamp.FinishReasonStrItem(b'finishReasonStr'))
BOOTCAMP_RESULTS_BLOCK.addComponent(6, bootcamp.ShowRewardsFlag(b'showRewards'))
BOOTCAMP_RESULTS_BLOCK.addComponent(7, bootcamp.CreditsBlock(_BOOTCAMP_STATVALUE_VO_META, b'credits'))
BOOTCAMP_RESULTS_BLOCK.addComponent(8, bootcamp.XPBlock(_BOOTCAMP_STATVALUE_VO_META, b'xp'))
BOOTCAMP_RESULTS_BLOCK.addComponent(9, bootcamp.FinishReasonItem(b'finishReason'))
BOOTCAMP_RESULTS_BLOCK.addComponent(10, bootcamp.PlayerResultItem(b'playerResult'))
BOOTCAMP_RESULTS_BLOCK.addComponent(11, bootcamp.VideoButtonsItem(b'videoButtons'))
BOOTCAMP_RESULTS_BLOCK.addComponent(12, bootcamp.AlternativeLayoutFlag(b'alternativeLayout'))
