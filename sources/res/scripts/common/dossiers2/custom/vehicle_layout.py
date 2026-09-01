from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
from dossiers2.custom.battle_statistics_layouts import *
from dossiers2.custom.dependencies import ACHIEVEMENT15X15_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENT7X7_DEPENDENCIES
from dossiers2.custom.dependencies import FALLOUT_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import FORT_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import GLOBAL_MAP_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import RANKED_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import A30X30_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import EPIC_BATTLE_STATS_DEPENDENCIES
TOTAL_BLOCK_LAYOUT = [
 11, 12, 13, 14, 15]
_totalBlockBuilder = StaticSizeBlockBuilder(b'total', TOTAL_BLOCK_LAYOUT, {}, [])
_a15x15BlockBuilder = StaticSizeBlockBuilder(b'a15x15', A15X15_BLOCK_LAYOUT, A15X15_STATS_DEPENDENCIES, [])
_a15x15_2BlockBuilder = StaticSizeBlockBuilder(b'a15x15_2', A15X15_2_BLOCK_LAYOUT, {}, [])
_clanBlockBuilder = StaticSizeBlockBuilder(b'clan', CLAN_BLOCK_LAYOUT, CLAN_STATS_DEPENDENCIES, [])
_clan2BlockBuilder = StaticSizeBlockBuilder(b'clan2', CLAN2_BLOCK_LAYOUT, {}, [])
_companyBlockBuilder = StaticSizeBlockBuilder(b'company', COMPANY_BLOCK_LAYOUT, {}, [])
_company2BlockBuilder = StaticSizeBlockBuilder(b'company2', COMPANY2_BLOCK_LAYOUT, {}, [])
_a7x7BlockBuilder = StaticSizeBlockBuilder(b'a7x7', A7X7_BLOCK_LAYOUT, A7X7_STATS_DEPENDENCIES, [])
_rated7x7BlockBuilder = StaticSizeBlockBuilder(b'rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_historicalBlockBuilder = StaticSizeBlockBuilder(b'historical', HISTORICAL_BLOCK_LAYOUT, HISTORICAL_STATS_DEPENDENCIES, [])
_fortBattlesBlockBuilder = StaticSizeBlockBuilder(b'fortBattles', FORT_BLOCK_LAYOUT, FORT_BATTLES_STATS_DEPENDENCIES, [])
_fortSortiesBlockBuilder = StaticSizeBlockBuilder(b'fortSorties', FORT_BLOCK_LAYOUT, FORT_SORTIES_STATS_DEPENDENCIES, [])
_globalMapCommonBlockBuilder = StaticSizeBlockBuilder(b'globalMapCommon', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_falloutBlockBuilder = StaticSizeBlockBuilder(b'fallout', FALLOUT_VEHICLE_BLOCK_LAYOUT, FALLOUT_STATS_DEPENDENCIES, [])
_rankedBlockBuilder = StaticSizeBlockBuilder(b'ranked', RANKED_BLOCK_LAYOUT, RANKED_STATS_DEPENDENCIES, [])
_rankedBlockBuilder_10x10 = StaticSizeBlockBuilder(b'ranked_10x10', RANKED_BLOCK_LAYOUT, RANKED_STATS_DEPENDENCIES, [])
_a30x30BlockBuilder = StaticSizeBlockBuilder(b'a30x30', A30X30_BLOCK_LAYOUT, A30X30_STATS_DEPENDENCIES, [])
_epicBattleBlockBuilder = StaticSizeBlockBuilder(b'epicBattle', EPIC_BATTLE_VEHICLE_BLOCK_LAYOUT, {}, [])
_comp7Season1BlockBuilder = StaticSizeBlockBuilder(b'comp7Season1', COMP7_BLOCK_LAYOUT, {}, [])
_comp7Season2BlockBuilder = StaticSizeBlockBuilder(b'comp7Season2', COMP7_BLOCK_LAYOUT, {}, [])
_comp7Season3BlockBuilder = StaticSizeBlockBuilder(b'comp7Season3', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchiveGriffinBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchiveGriffin', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchivePegasusBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchivePegasus', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchiveManticoreBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchiveManticore', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchiveDragonBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchiveDragon', COMP7_BLOCK_LAYOUT, {}, [])
_maxPopUps = [
 b'maxXP', b'maxFrags', b'maxDamage']
_maxFalloutPopUps = _maxPopUps + [b'maxWinPoints', b'maxCoins']
_max15x15BlockBuilder = StaticSizeBlockBuilder(b'max15x15', MAX_15x15_BLOCK_LAYOUT, {}, _maxPopUps)
_max7x7BlockBuilder = StaticSizeBlockBuilder(b'max7x7', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxHistoricalBlockBuilder = StaticSizeBlockBuilder(b'maxHistorical', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxFortBattlesBlockBuilder = StaticSizeBlockBuilder(b'maxFortBattles', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxFortSortiesBlockBuilder = StaticSizeBlockBuilder(b'maxFortSorties', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder(b'maxRated7x7', MAX_BLOCK_LAYOUT, {}, [])
_maxGlobalMapCommonBlockBuilder = StaticSizeBlockBuilder(b'maxGlobalMapCommon', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxFalloutBlockBuilder = StaticSizeBlockBuilder(b'maxFallout', MAX_FALLOUT_BLOCK_LAYOUT, {}, _maxFalloutPopUps)
_maxRankedBlockBuilder = StaticSizeBlockBuilder(b'maxRanked', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_max30x30BlockBuilder = StaticSizeBlockBuilder(b'max30x30', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxEpicBattleBlockBuilder = StaticSizeBlockBuilder(b'maxEpicBattle', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxRankedBlockBuilder_10x10 = StaticSizeBlockBuilder(b'maxRanked_10x10', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxComp7Season1BlockBuilder = StaticSizeBlockBuilder(b'maxComp7Season1', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7Season2BlockBuilder = StaticSizeBlockBuilder(b'maxComp7Season2', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7Season3BlockBuilder = StaticSizeBlockBuilder(b'maxComp7Season3', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchiveGriffinBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchiveGriffin', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchivePegasusBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchivePegasus', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchiveManticoreBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchiveManticore', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchiveDragonBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchiveDragon', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_vehTypeFragsBlockBuilder = DictBlockBuilder(b'vehTypeFrags', b'I', b'H', VEH_TYPE_FRAGS_DEPENDENCIES)
_rankedSeasonsBlockBuilder = DictBlockBuilder(b'rankedSeasons', b'II', b'BB', {})
_maxRankedSeason1BlockBuilder = StaticSizeBlockBuilder(b'maxRankedSeason1', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxRankedSeason2BlockBuilder = StaticSizeBlockBuilder(b'maxRankedSeason2', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_maxRankedSeason3BlockBuilder = StaticSizeBlockBuilder(b'maxRankedSeason3', MAX_BLOCK_LAYOUT, {}, _maxPopUps)
_ACHIEVEMENTS15X15_BLOCK_LAYOUT = [
 74, 
 75, 
 76, 
 77, 
 78, 
 79, 
 80, 
 81, 
 82, 
 83, 
 84, 
 85, 
 86, 
 87, 
 88, 
 89, 
 90, 
 91, 
 92, 
 93, 
 94, 
 95, 
 96, 
 97, 
 98, 
 99, 
 100, 
 101, 
 102, 
 103, 
 104, 
 105, 
 106, 
 107, 
 108, 
 109, 
 110, 
 111, 
 112, 
 113, 
 114, 
 115, 
 116, 
 117, 
 118, 
 119, 
 120, 
 121, 
 122, 
 123, 
 124, 
 125, 
 126, 
 127, 
 128, 
 129, 
 130, 
 131, 
 132, 
 133, 
 134, 
 135, 
 136, 
 137, 
 138, 
 139, 
 140, 
 141, 
 142, 
 143, 
 144, 
 145, 
 146, 
 147, 
 148, 
 149, 
 150, 
 151, 
 152, 
 153, 
 154, 
 155, 
 156, 
 157, 
 158, 
 159, 
 160, 
 161, 
 162, 
 163]
_achievements15x15PopUps = [
 164, 
 165, 
 166, 
 167, 
 168, 
 169, 
 170, 
 171, 
 172, 
 173, 
 174, 
 175, 
 176, 
 177, 
 178, 
 179, 
 139, 
 142, 
 180, 
 153, 
 154, 
 155, 
 156, 
 157, 
 158, 
 159]
_achievements15x15BlockBuilder = StaticSizeBlockBuilder(b'achievements', _ACHIEVEMENTS15X15_BLOCK_LAYOUT, ACHIEVEMENT15X15_DEPENDENCIES, _achievements15x15PopUps)
ACHIEVEMENTS7X7_BLOCK_LAYOUT = [
 182, 183, 184, 
 185, 186, 187, 
 188, 
 189, 190, 191, 192, 
 193, 
 194, 195, 196, 
 197, 198, 199, 200, 
 201, 202, 203, 204, 205, 
 206, 
 207, 
 208, 209, 210, 211, 212, 
 213, 
 214, 215, 216, 217, 
 218, 
 219]
_achievements7x7BlockBuilder = StaticSizeBlockBuilder(b'achievements7x7', ACHIEVEMENTS7X7_BLOCK_LAYOUT, ACHIEVEMENT7X7_DEPENDENCIES, [])
UNIQUE_VEH_ACHIEVEMENT_VALUES = []
_uniqueVehAchievementPopUps = []
_uniqueVehAchievementBlockBuilder = BinarySetDossierBlockBuilder(b'uniqueAchievements', UNIQUE_VEH_ACHIEVEMENT_VALUES, {}, _uniqueVehAchievementPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = [
 222, 223, 224, 225, 
 226, 227, 228]
_singleAchievementsPopUps = [222, 223, 224, 225, 
 226, 227, 228]
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder(b'singleAchievements', _SINGLE_ACHIEVEMENTS_VALUES, {}, _singleAchievementsPopUps)
FORT_ACHIEVEMENTS_BLOCK_LAYOUT = [
 230, 231, 232, 233, 234, 235]
_fortPersonalAchievementsPopUps = [
 b'soldierOfFortune']
_fortPersonalAchievementsBlockBuilder = StaticSizeBlockBuilder(b'fortAchievements', FORT_ACHIEVEMENTS_BLOCK_LAYOUT, FORT_ACHIEVEMENTS_DEPENDENCIES, _fortPersonalAchievementsPopUps)
CLAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 b'medalRotmistrov']
_clanAchievementsBlockBuilder = StaticSizeBlockBuilder(b'clanAchievements', CLAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, [])
FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT = [
 239, 240, 241, 242, 
 243, 244, 245, 246, 247, 248, 
 249, 250]
_falloutAchievementsPopUps = [b'falloutDieHard']
_falloutAchievementsBlockBuilder = StaticSizeBlockBuilder(b'falloutAchievements', FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _falloutAchievementsPopUps)
EPIC_BATTLE_ACHIEVEMENTS_BLOCK_LAYOUT = [
 252, 253, 254, 255, 
 256]
_epicBattleAchievementsPopUps = [252, 253, 254, 255, 
 256]
_epicBattleAchievementsBlockBuilder = StaticSizeBlockBuilder(b'epicBattleAchievements', EPIC_BATTLE_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _epicBattleAchievementsPopUps)
_playerInscriptionsBlockBuilder = ListBlockBuilder(b'inscriptions', b'H', {})
_playerEmblemsBlockBuilder = ListBlockBuilder(b'emblems', b'H', {})
_camouflagesBlockBuilder = ListBlockBuilder(b'camouflages', b'H', {})
COMPENSATION_BLOCK_LAYOUT = [
 b'gold']
_compensationBlockBuilder = StaticSizeBlockBuilder(b'compensation', COMPENSATION_BLOCK_LAYOUT, {}, [])
vehicleDossierLayout = (
 _a15x15BlockBuilder, _a15x15_2BlockBuilder, _clanBlockBuilder,
 _clan2BlockBuilder, _companyBlockBuilder, _company2BlockBuilder, _a7x7BlockBuilder,
 _achievements15x15BlockBuilder, _vehTypeFragsBlockBuilder, _totalBlockBuilder,
 _max15x15BlockBuilder, _max7x7BlockBuilder,
 _playerInscriptionsBlockBuilder, _playerEmblemsBlockBuilder, _camouflagesBlockBuilder,
 _compensationBlockBuilder, _achievements7x7BlockBuilder, _historicalBlockBuilder,
 _maxHistoricalBlockBuilder, _uniqueVehAchievementBlockBuilder, _fortBattlesBlockBuilder,
 _maxFortBattlesBlockBuilder, _fortSortiesBlockBuilder,
 _maxFortSortiesBlockBuilder, _fortPersonalAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder, _clanAchievementsBlockBuilder,
 _rated7x7BlockBuilder, _maxRated7x7BlockBuilder,
 _globalMapCommonBlockBuilder, _maxGlobalMapCommonBlockBuilder,
 _falloutBlockBuilder, _maxFalloutBlockBuilder, _falloutAchievementsBlockBuilder,
 _rankedBlockBuilder, _maxRankedBlockBuilder, _rankedSeasonsBlockBuilder,
 _a30x30BlockBuilder, _max30x30BlockBuilder,
 _epicBattleBlockBuilder, _maxEpicBattleBlockBuilder, _epicBattleAchievementsBlockBuilder,
 _maxRankedSeason1BlockBuilder, _maxRankedSeason2BlockBuilder, _maxRankedSeason3BlockBuilder,
 _rankedBlockBuilder_10x10, _maxRankedBlockBuilder_10x10,
 _comp7Season1BlockBuilder, _maxComp7Season1BlockBuilder,
 _comp7Season2BlockBuilder, _maxComp7Season2BlockBuilder,
 _comp7Season3BlockBuilder, _maxComp7Season3BlockBuilder,
 _comp7ArchiveGriffinBlockBuilder, _maxComp7ArchiveGriffinBlockBuilder,
 _comp7ArchivePegasusBlockBuilder, _maxComp7ArchivePegasusBlockBuilder,
 _comp7ArchiveManticoreBlockBuilder, _maxComp7ArchiveManticoreBlockBuilder,
 _comp7ArchiveDragonBlockBuilder, _maxComp7ArchiveDragonBlockBuilder)
VEHICLE_DOSSIER_BLOCKS = {b.name: b for b in vehicleDossierLayout}
