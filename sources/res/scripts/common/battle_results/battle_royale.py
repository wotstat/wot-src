from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from DictPackers import ValueReplayPacker, MergeDictPacker
BATTLE_RESULTS = [
 (
  b'maxAchievedBRTitle', tuple, (0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'brPosInBattle', int, 255, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'battleXPTotal', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'modulesDescriptors', list, [], None, b'extend', ENTRY_TYPE.SERVER),
 (
  b'achivedLevel', int, 1, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'brAwardTokens', dict, {}, None, b'joinDicts', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'currencies', dict, {},
  MergeDictPacker((
   b'brcoin', dict, {},
   MergeDictPacker((
    b'count', int, 0, None, b'sum'), (
    b'original', int, 0, None, b'sum'), (
    b'replay', str, b'', ValueReplayPacker(), b'skip'), (
    b'premiumFactor100', int, 0, None, b'any'), (
    b'premiumPlusFactor100', int, 0, None, b'any'), (
    b'premiumVipFactor100', int, 0, None, b'any'), (
    b'appliedPremiumFactor100', int, 0, None, b'any'), (
    b'coinsForPlace', int, 0, None, b'any'), (
    b'dailyBonusFactor', int, 0, None, b'any'), (
    b'leaveCoins', int, 0, None, b'any'), (
    b'subtotal', int, 0, None, b'sum')),
   b'joinByEachPacker'), (
   b'stpcoin', dict, {},
   MergeDictPacker((
    b'count', int, 0, None, b'sum'), (
    b'original', int, 0, None, b'sum'), (
    b'replay', str, b'', ValueReplayPacker(), b'skip'), (
    b'premiumFactor100', int, 0, None, b'any'), (
    b'premiumPlusFactor100', int, 0, None, b'any'), (
    b'premiumVipFactor100', int, 0, None, b'any'), (
    b'appliedPremiumFactor100', int, 0, None, b'any'), (
    b'coinsForPlace', int, 0, None, b'any'), (
    b'dailyBonusFactor', int, 0, None, b'any'), (
    b'leaveCoins', int, 0, None, b'any'), (
    b'subtotal', int, 0, None, b'sum')),
   b'joinByEachPacker')),
  b'joinByEachPacker', ENTRY_TYPE.VEHICLE_SELF)]
