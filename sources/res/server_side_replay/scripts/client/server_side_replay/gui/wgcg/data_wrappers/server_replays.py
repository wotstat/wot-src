from __future__ import absolute_import
from typing import NamedTuple, List, Optional
from shared_utils import CONST_CONTAINER

class DataNames(CONST_CONTAINER):
    TOP_REPLAYS = b'TOP_REPLAYS'
    BEST_REPLAYS = b'BEST_REPLAYS'
    MY_REPLAYS = b'MY_REPLAYS'
    REPLAY_LINK = b'REPLAY_LINK'
    FIND_REPLAY = b'FIND_REPLAY'
    ONE_REPLAY = b'ONE_REPLAY'


class StatParams(CONST_CONTAINER):
    DAMAGE_DEALT = b'damage_dealt'
    DAMAGE_ASSISTED = b'damage_assisted'
    DAMAGE_BLOCKED = b'damage_blocked'
    KILLS = b'kills_made'
    EXP = b'exp'
    MARK_OF_MASTERY = b'mastery_mark'
    LIKE_COUNT = b'likes_received'


ShortReplay = NamedTuple(b'ShortReplay', [
 (
  b'rank', int),
 (
  b'replay_id', int),
 (
  b'arena_id', int),
 (
  b'vehicle_entity_id', int),
 (
  b'map', str),
 (
  b'battle_type', int),
 (
  b'battle_start', int),
 (
  b'vehicle_cd', int),
 (
  b'spa_id', int),
 (
  b'nickname', str),
 (
  b'clan_tag', str),
 (
  b'clan_color', Optional[int]),
 (
  b'exp', int),
 (
  b'damage_dealt', int),
 (
  b'damage_assisted', int),
 (
  b'damage_blocked', int),
 (
  b'kills_made', int),
 (
  b'mastery_mark', int),
 (
  b'achievements_received', int),
 (
  b'achievements', List[str])])
PageReplays = NamedTuple(b'PageReplays', [
 (
  b'rankings', List[ShortReplay]),
 (
  b'total_entries', int),
 (
  b'limit', int),
 (
  b'offset', int)])
TopReplays = NamedTuple(b'TopReplays', [
 (
  b'exp', ShortReplay),
 (
  b'damage_dealt', ShortReplay),
 (
  b'damage_assisted', ShortReplay),
 (
  b'damage_blocked', ShortReplay),
 (
  b'kills_made', ShortReplay),
 (
  b'likes_received', ShortReplay)])
ReplayLink = NamedTuple(b'ReplayLink', [
 (
  b'replay_link', str),
 (
  b'expire_time', int)])
