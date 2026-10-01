SESSION_PROGRESS_REWARDS_PDATA_KEY = b'sessionProgressRewards'
CURRENT_STEP_PDATA_KEY = b'currentStep'
LAST_REWARD_GAME_DAY_PDATA_KEY = b'lastRewardGameDay'
AB_TEST_FEATURE_NAME = b'rewards'
AB_TEST_DEFAULT_GROUP_NAME = b'default'

def sessionProgressRewardsInitialData():
    return {CURRENT_STEP_PDATA_KEY: 0, 
       LAST_REWARD_GAME_DAY_PDATA_KEY: 0}
