from __future__ import absolute_import
import typing
from constants import ARENA_BONUS_TYPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController
if typing.TYPE_CHECKING:
    from typing import Dict

class USER(object):
    INFO = b'userInfo'
    CLAN_INFO = b'clanInfo'
    SEND_CLAN_INVITE = b'sendClanInvite'
    CREATE_PRIVATE_CHANNEL = b'createPrivateChannel'
    ADD_TO_FRIENDS = b'addToFriends'
    REQUEST_FRIENDSHIP = b'requestFriendship'
    REMOVE_FROM_FRIENDS = b'removeFromFriends'
    ADD_TO_IGNORED = b'addToIgnored'
    REMOVE_FROM_IGNORED = b'removeFromIgnored'
    COPY_TO_CLIPBOARD = b'copyToClipBoard'
    SET_MUTED = b'setMuted'
    UNSET_MUTED = b'unsetMuted'
    CREATE_SQUAD = b'createSquad'
    CREATE_EVENT_SQUAD = b'createEventSquad'
    CREATE_BATTLE_ROYALE_SQUAD = b'createBattleRoyaleSquad'
    INVITE = b'invite'
    VEHICLE_INFO = b'vehicleInfoEx'
    END_REFERRAL_COMPANY = b'endReferralCompany'
    CREATE_MAPBOX_SQUAD = b'createMapboxSquad'


SETTINGS_WINDOWS_MAP = {}
DEFAULT_SETTINGS_ALIAS = VIEW_ALIAS.SETTINGS_WINDOW

def registerSettingsWindow(arenaBonusType, viewAlias):
    SETTINGS_WINDOWS_MAP[arenaBonusType] = viewAlias
    return


def getSettingsWindowAlias():
    platoonController = dependency.instance(IPlatoonController)
    arenaBonusCaps = platoonController.getPrbEntityType()
    return SETTINGS_WINDOWS_MAP.get(arenaBonusCaps, DEFAULT_SETTINGS_ALIAS)
