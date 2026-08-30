from __future__ import absolute_import
from collections import namedtuple
import CGF
from constants import UNKNOWN_RESPAWN_ID
VehicleAppearanceCacheInfo = namedtuple(b'VehicleAppearanceCacheInfo', (b'typeDescr', b'health', b'isCrewActive', b'isTurretDetached', b'outfitCD', b'forceDynAttachmentLoading', b'entityGameObject', b'respawnID'))
VehicleAppearanceCacheInfo.__new__.__defaults__ = (
 None, 0, False, False, b'', False, CGF.GameObject.INVALID_GAME_OBJECT, UNKNOWN_RESPAWN_ID)
