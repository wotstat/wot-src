from __future__ import absolute_import
from enumerations import Enumeration
INVITE_TYPES = Enumeration(b'InviteTypes', [
 4, 
 5, 
 6, 
 7, 
 8])
_g_invitesConfig = {(INVITE_TYPES.BARTER.index()): {b'TTL': 900, b'keepInArchive': 3600, b'checkIgnore': True}, 
   (INVITE_TYPES.TEAM.index()): {b'TTL': (-1), b'keepInArchive': (-1), b'checkIgnore': True}, (INVITE_TYPES.CLAN.index()): {b'TTL': (-1), b'keepInArchive': (-1), b'checkIgnore': True}, (INVITE_TYPES.TRAINING_ROOM.index()): {b'TTL': 900, b'keepInArchive': 3600, b'checkIgnore': True}, 
   (INVITE_TYPES.PREBATTLE.index()): {b'TTL': 900, b'keepInArchive': 3600, b'checkIgnore': True}}
_g_defaultInviteConfig = {b'TTL': (-1), b'keepInArchive': (-1), b'checkIgnore': True}

def getInviteConfig(inviteTypeIdx):
    return _g_invitesConfig.get(inviteTypeIdx, _g_defaultInviteConfig)


INVITE_STATUS = Enumeration(b'Invite statuses', [
 b'accepted',
 b'rejected',
 b'invalid',
 b'invalidTTL'])
