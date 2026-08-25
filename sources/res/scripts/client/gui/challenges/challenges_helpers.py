from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import ChallengesMissions
from gui import GUI_SETTINGS
from helpers import time_utils
TIME_BEFORE_END_OF_EXPIRATION = time_utils.ONE_DAY + time_utils.ONE_MINUTE

def getSettings(settingName, defaultValue=None):
    settings = AccountSettings.getSettings(ChallengesMissions.SETTINGS)
    return settings.get(settingName, defaultValue)


def setSettings(settingName, value):
    settings = AccountSettings.getSettings(ChallengesMissions.SETTINGS)
    settings[settingName] = value
    AccountSettings.setSettings(ChallengesMissions.SETTINGS, settings)
    return


def setVisitedChallenge(challengeID):
    settings = AccountSettings.getSettings(ChallengesMissions.SETTINGS)
    settings[ChallengesMissions.VISITED_CHALLENGES].add(challengeID)
    AccountSettings.setSettings(ChallengesMissions.SETTINGS, settings)
    return


def getChallengesInfoUrl():
    return (b'').join((GUI_SETTINGS.baseUrls[b'webBridgeRootURL'], GUI_SETTINGS.challenges[b'info']))
