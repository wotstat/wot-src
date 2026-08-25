from __future__ import absolute_import
from gui import GUI_SETTINGS
from helpers import dependency
from skeletons.gui.shared import IItemsCache
RECRUITER_SPA_ID_ATTR = b'/wot/game/ref/recruiterSpaId'

def _getUrl(urlName=None):
    if urlName is None:
        return getReferralProgramURL()
    else:
        return getReferralProgramURL() + GUI_SETTINGS.referralProgram.get(urlName)


def getReferralProgramURL():
    return GUI_SETTINGS.referralProgram.get(b'baseUrl')


def getObtainVehicleURL():
    return _getUrl(b'getVehicle')


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isCurrentUserRecruit(itemsCache=None):
    return bool(itemsCache.items.stats.SPA.get(RECRUITER_SPA_ID_ATTR, False))
