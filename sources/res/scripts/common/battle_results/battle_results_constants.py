from __future__ import absolute_import
import typing
from chat_shared import SYS_MESSAGE_TYPE
from constants import ARENA_BONUS_TYPE
if typing.TYPE_CHECKING:
    from typing import Dict
PATH_TO_CONFIG = {(ARENA_BONUS_TYPE.REGULAR): [
                              b'.random'], 
   (ARENA_BONUS_TYPE.EPIC_RANDOM): [
                                  b'.random'], 
   (ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING): [
                                           b'.random'], 
   (ARENA_BONUS_TYPE.WINBACK): [
                              b'.random'], 
   (ARENA_BONUS_TYPE.RANKED): [
                             b'.ranked'], 
   (ARENA_BONUS_TYPE.EPIC_BATTLE): [
                                  b'.frontline'], 
   (ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING): [
                                           b'.frontline'], 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO): [
                                         b'.battle_royale'], 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD): [
                                          b'.battle_royale'], 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SOLO): [
                                             b'.battle_royale'], 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SQUAD): [
                                              b'.battle_royale'], 
   (ARENA_BONUS_TYPE.MAPBOX): [
                             b'.random'], 
   (ARENA_BONUS_TYPE.MAPS_TRAINING): [
                                    b'.maps_training'], 
   (ARENA_BONUS_TYPE.RANDOM_NP2): [
                                 b'.random']}
POSSIBLE_TYPES = (
 int, float, str, bool, list, tuple, dict, set, None)

class BATTLE_RESULT_ENTRY_TYPE:
    COMMON = 1
    ACCOUNT_SELF = 2
    ACCOUNT_ALL = 3
    VEHICLE_SELF = 4
    VEHICLE_ALL = 5
    PLAYER_INFO = 6
    SERVER = 7
    ALL = (
     COMMON, ACCOUNT_SELF, ACCOUNT_ALL, VEHICLE_SELF, VEHICLE_ALL, PLAYER_INFO, SERVER)


ARENA_BONUS_TYPE_TO_SM_TYPE_BATTLE_RESULT = {(ARENA_BONUS_TYPE.REGULAR): (SYS_MESSAGE_TYPE.battleResults.index())}
ARENA_BONUS_TYPE_TO_SM_TYPE_AUTO_MAINTENANCE = {(ARENA_BONUS_TYPE.REGULAR): (SYS_MESSAGE_TYPE.autoMaintenance.index())}
