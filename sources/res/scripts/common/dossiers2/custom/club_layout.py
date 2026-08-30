from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
from dossiers2.custom.battle_statistics_layouts import *
from dossiers2.custom.dependencies import CLUB_BATTLES_STAT_DEPENDENCIES
from dossiers2.custom.dependencies import CLUB_ACHIEVEMENTS_DEPENDENCIES
_rated7x7BlockBuilder = StaticSizeBlockBuilder(b'rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder(b'maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
rated7x7DossierLayout = (
 _rated7x7BlockBuilder, _maxRated7x7BlockBuilder)
_clubTotalBlockLayout = [
 b'creationTime', b'lastBattleTime']
_clubTotalBlockBuilder = StaticSizeBlockBuilder(b'total', _clubTotalBlockLayout, {}, [])
_clubBattlesBlockLayout = [
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21]
_clubBattlesBlockBuilder = StaticSizeBlockBuilder(b'clubBattles', _clubBattlesBlockLayout, CLUB_BATTLES_STAT_DEPENDENCIES, [])
_clubBestVehiclesBlockBuilder = DictBlockBuilder(b'vehicles', b'I', b'II', {})
_clubBestMapsBlockBuilder = DictBlockBuilder(b'maps', b'I', b'II', {})
CLUB_ACHIEVEMENTS_BLOCK_LAYOUT = [
 27, 28, 29, 
 30, 31, 32]
_clubAchievementsPopUps = [
 b'strategicOperations']
_clubAchievementsBlockBuilder = StaticSizeBlockBuilder(b'achievementsRated7x7', CLUB_ACHIEVEMENTS_BLOCK_LAYOUT, CLUB_ACHIEVEMENTS_DEPENDENCIES, _clubAchievementsPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = [
 b'victoryMarch']
_singleAchievementsPopUps = [b'victoryMarch']
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder(b'singleAchievementsRated7x7', _SINGLE_ACHIEVEMENTS_VALUES, {}, _singleAchievementsPopUps)
clubDossierLayout = (
 _clubTotalBlockBuilder, _clubBattlesBlockBuilder, _clubBestVehiclesBlockBuilder,
 _clubBestMapsBlockBuilder, _clubAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder)
