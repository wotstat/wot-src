from shared_utils import CONST_CONTAINER
from gui.impl.gen import R

class ParagonsSystemMessages(CONST_CONTAINER):
    PROJECT_IS_AVAILABLE = b'projectIsAvailable'
    BRANCH_RESET_IS_AVAILABLE = b'branchResetIsAvailable'
    PROJECT_IS_CONTINUING = b'projectIsContinuing'
    NEW_CHAPTER_IS_AVAILABLE = b'newStageIsAvailable'
    PROJECT_IS_UNAVAILABLE = b'projectIsUnavailable'
    BRANCH_RESET_ERROR = b'paragonsBranchResetError'
    BATTLE_REWARD = b'paragonsBattleReward'
    LEVEL_REWARDS = b'paragonsLevelReward'
    LEVEL_SELECTABLE_REWARDS = b'paragonsLevelSelectableReward'
    BRANCH_RESETED = b'paragonsBranchReseted'
    BRANCH_IS_UNAVAILABLE = b'paragonsBranchIsUnavailable'
    BRANCH_IS_AVAILABLE = b'paragonsBranchIsAvailable'
    FIRST_MAIN_REWARD_ACHIEVED = b'paragonsFirstMainRewardBadgeAchieved'
    CHAPTER_COMPLETED = b'paragonsChapterCompleted'
    CHAPTER_1_COMPLETED = b'paragons_S1_completed'
    CHAPTER_2_COMPLETED = b'paragons_S2_completed'
    CHAPTER_COMPLETE_MESSAGES = {1: CHAPTER_1_COMPLETED, 
       2: CHAPTER_2_COMPLETED}

    @classmethod
    def getChapterCompleteMessage(cls, chapterID):
        return cls.CHAPTER_COMPLETE_MESSAGES.get(chapterID)


MESSAGE_ICONS = {(ParagonsSystemMessages.FIRST_MAIN_REWARD_ACHIEVED): (R.images.gui.maps.icons.paragons.messenger.notification_icon_first11), 
   (ParagonsSystemMessages.CHAPTER_1_COMPLETED): (R.images.gui.maps.icons.paragons.messenger.notification_icon_first_chapter), 
   (ParagonsSystemMessages.CHAPTER_2_COMPLETED): (R.images.gui.maps.icons.paragons.messenger.notification_icon_chapter_S2)}
PARAGONS_POST_BATTLE_FAKE_QUEST_ID = b'paragonsFakeQuestID'
