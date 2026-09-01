from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
from dossiers2.custom.dependencies import ACHIEVEMENT15X15_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENT7X7_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENTRATED7X7_DEPENDENCIES
from dossiers2.custom.dependencies import HISTORICAL_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import FALLOUT_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import FORT_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import SINGLE_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import GLOBAL_MAP_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import RANKED_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import A30X30_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import EPIC_BATTLE_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import STEAM_ACHIEVEMENT_DEPENDENCIES
from dossiers2.custom.dependencies import VEHICLE_ACHIEVEMENTS_DEPENDENCIES, VEHICLE_ACHIEVEMENTS_POP_UPS
from dossiers2.custom.dependencies import CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES, CUSTOMIZATION_ACHIEVEMENTS_POP_UPS
from dossiers2.custom.dependencies import PLAYER_BADGES_DEPENDENCIES
from dossiers2.custom.battle_statistics_layouts import *
TOTAL_BLOCK_LAYOUT = [
 18, 19, 20, 21, 22]
_totalBlockBuilder = StaticSizeBlockBuilder(b'total', TOTAL_BLOCK_LAYOUT, TOTAL_STATS_DEPENDENCIES, [])
_a15x15BlockBuilder = StaticSizeBlockBuilder(b'a15x15', A15X15_BLOCK_LAYOUT, A15X15_STATS_DEPENDENCIES, [])
_a15x15_2BlockBuilder = StaticSizeBlockBuilder(b'a15x15_2', A15X15_2_BLOCK_LAYOUT, {}, [])
_clanBlockBuilder = StaticSizeBlockBuilder(b'clan', CLAN_BLOCK_LAYOUT, CLAN_STATS_DEPENDENCIES, [])
_clan2BlockBuilder = StaticSizeBlockBuilder(b'clan2', CLAN2_BLOCK_LAYOUT, {}, [])
_companyBlockBuilder = StaticSizeBlockBuilder(b'company', COMPANY_BLOCK_LAYOUT, {}, [])
_company2BlockBuilder = StaticSizeBlockBuilder(b'company2', COMPANY2_BLOCK_LAYOUT, {}, [])
_a7x7BlockBuilder = StaticSizeBlockBuilder(b'a7x7', A7X7_BLOCK_LAYOUT, A7X7_STATS_DEPENDENCIES, [])
_rated7x7BlockBuilder = StaticSizeBlockBuilder(b'rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_historicalBlockBuilder = StaticSizeBlockBuilder(b'historical', HISTORICAL_BLOCK_LAYOUT, HISTORICAL_STATS_DEPENDENCIES, [])
_fortBattlesInClanBlockBuilder = StaticSizeBlockBuilder(b'fortBattlesInClan', FORT_BLOCK_LAYOUT, {}, [])
_fortSortiesInClanBlockBuilder = StaticSizeBlockBuilder(b'fortSortiesInClan', FORT_BLOCK_LAYOUT, {}, [])
_fortBattlesBlockBuilder = StaticSizeBlockBuilder(b'fortBattles', FORT_BLOCK_LAYOUT, FORT_BATTLES_STATS_DEPENDENCIES, [])
_fortSortiesBlockBuilder = StaticSizeBlockBuilder(b'fortSorties', FORT_BLOCK_LAYOUT, FORT_SORTIES_STATS_DEPENDENCIES, [])
_globalMapMiddleBlockBuilder = StaticSizeBlockBuilder(b'globalMapMiddle', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_globalMapChampionBlockBuilder = StaticSizeBlockBuilder(b'globalMapChampion', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_globalMapAbsoluteBlockBuilder = StaticSizeBlockBuilder(b'globalMapAbsolute', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_falloutBlockBuilder = StaticSizeBlockBuilder(b'fallout', FALLOUT_BLOCK_LAYOUT, FALLOUT_STATS_DEPENDENCIES, [])
_rankedBlockBuilder = StaticSizeBlockBuilder(b'ranked', RANKED_BLOCK_LAYOUT, RANKED_STATS_DEPENDENCIES, [])
_a30x30BlockBuilder = StaticSizeBlockBuilder(b'a30x30', A30X30_BLOCK_LAYOUT, A30X30_STATS_DEPENDENCIES, [])
_epicBattleBlockBuilder = StaticSizeBlockBuilder(b'epicBattle', EPIC_BATTLE_BLOCK_LAYOUT, EPIC_BATTLE_STATS_DEPENDENCIES, [])
_rankedSeason1BlockBuilder = StaticSizeBlockBuilder(b'rankedSeason1', RANKED_BLOCK_LAYOUT, {}, [])
_rankedSeason2BlockBuilder = StaticSizeBlockBuilder(b'rankedSeason2', RANKED_BLOCK_LAYOUT, {}, [])
_rankedSeason3BlockBuilder = StaticSizeBlockBuilder(b'rankedSeason3', RANKED_BLOCK_LAYOUT, {}, [])
_rankedArchiveBlockBuilder = StaticSizeBlockBuilder(b'rankedArchive', RANKED_BLOCK_LAYOUT, {}, [])
_ranked_10x10BlockBuilder = StaticSizeBlockBuilder(b'ranked_10x10', RANKED_BLOCK_LAYOUT, RANKED_STATS_DEPENDENCIES, [])
_comp7Season1BlockBuilder = StaticSizeBlockBuilder(b'comp7Season1', COMP7_BLOCK_LAYOUT, {}, [])
_comp7Season2BlockBuilder = StaticSizeBlockBuilder(b'comp7Season2', COMP7_BLOCK_LAYOUT, {}, [])
_comp7Season3BlockBuilder = StaticSizeBlockBuilder(b'comp7Season3', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchiveGriffinBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchiveGriffin', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchivePegasusBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchivePegasus', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchiveManticoreBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchiveManticore', COMP7_BLOCK_LAYOUT, {}, [])
_comp7ArchiveDragonBlockBuilder = StaticSizeBlockBuilder(b'comp7ArchiveDragon', COMP7_BLOCK_LAYOUT, {}, [])
_max15x15BlockBuilder = StaticSizeBlockBuilder(b'max15x15', MAX_15x15_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_max7x7BlockBuilder = StaticSizeBlockBuilder(b'max7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder(b'maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxHistoricalBlockBuilder = StaticSizeBlockBuilder(b'maxHistorical', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortBattlesBlockBuilder = StaticSizeBlockBuilder(b'maxFortBattles', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortSortiesBlockBuilder = StaticSizeBlockBuilder(b'maxFortSorties', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortBattlesInClanBlockBuilder = StaticSizeBlockBuilder(b'maxFortBattlesInClan', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortSortiesInClanBlockBuilder = StaticSizeBlockBuilder(b'maxFortSortiesInClan', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapMiddleBlockBuilder = StaticSizeBlockBuilder(b'maxGlobalMapMiddle', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapChampionBlockBuilder = StaticSizeBlockBuilder(b'maxGlobalMapChampion', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapAbsoluteBlockBuilder = StaticSizeBlockBuilder(b'maxGlobalMapAbsolute', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFalloutBlockBuilder = StaticSizeBlockBuilder(b'maxFallout', MAX_FALLOUT_BLOCK_LAYOUT_WITH_AVATAR, {}, [])
_maxRankedBlockBuilder = StaticSizeBlockBuilder(b'maxRanked', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_max30x30BlockBuilder = StaticSizeBlockBuilder(b'max30x30', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxEpicBattleBlockBuilder = StaticSizeBlockBuilder(b'maxEpicBattle', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedSeason1BlockBuilder = StaticSizeBlockBuilder(b'maxRankedSeason1', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedSeason2BlockBuilder = StaticSizeBlockBuilder(b'maxRankedSeason2', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedSeason3BlockBuilder = StaticSizeBlockBuilder(b'maxRankedSeason3', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedArchiveBlockBuilder = StaticSizeBlockBuilder(b'maxRankedArchive', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRanked_10x10BlockBuilder = StaticSizeBlockBuilder(b'maxRanked_10x10', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxComp7Season1BlockBuilder = StaticSizeBlockBuilder(b'maxComp7Season1', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7Season2BlockBuilder = StaticSizeBlockBuilder(b'maxComp7Season2', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7Season3BlockBuilder = StaticSizeBlockBuilder(b'maxComp7Season3', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchiveGriffinBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchiveGriffin', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchivePegasusBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchivePegasus', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchiveManticoreBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchiveManticore', MAX_COMP7_BLOCK_LAYOUT, {}, [])
_maxComp7ArchiveDragonBlockBuilder = StaticSizeBlockBuilder(b'maxComp7ArchiveDragon', MAX_COMP7_BLOCK_LAYOUT, {}, [])

class VEHICLE_STATS:
    FRAGS = b'vehTypeFrags'
    A15x15_CUT = b'a15x15Cut'
    A30x30_CUT = b'a30x30Cut'
    A7x7_CUT = b'a7x7Cut'
    HISTORICAL_CUT = b'historicalCut'
    FORT_SORTIES_CUT = b'fortSortiesCut'
    FORT_BATTLES_CUT = b'fortBattlesCut'
    RANKED_CUT = b'rankedCut'
    RANKED_CUT_SEASON_1 = b'rankedCutSeason1'
    RANKED_CUT_SEASON_2 = b'rankedCutSeason2'
    RANKED_CUT_SEASON_3 = b'rankedCutSeason3'
    RANKED_CUT_ARCHIVE = b'rankedCutArchive'
    RANKED_CUT_10X10 = b'rankedCut_10x10'
    RATED_7x7_CUT = b'rated7x7Cut'
    GLOBAL_MAP_COMMON_CUT = b'globalMapCommonCut'
    FALLOUT_CUT = b'falloutCut'
    MARK_OF_MASTERY_CUT = b'markOfMasteryCut'
    EPIC_BATTLE_CUT = b'epicBattleCut'
    COMP7_CUT_SEASON_1 = b'comp7CutSeason1'
    COMP7_CUT_SEASON_2 = b'comp7CutSeason2'
    COMP7_CUT_SEASON_3 = b'comp7CutSeason3'
    COMP7_CUT_ARCHIVE_GRIFFIN = b'comp7CutArchiveGriffin'
    COMP7_CUT_ARCHIVE_PEGASUS = b'comp7CutArchivePegasus'
    COMP7_CUT_ARCHIVE_MANTICORE = b'comp7CutArchiveManticore'
    COMP7_CUT_ARCHIVE_DRAGON = b'comp7CutArchiveDragon'
    PRESTIGE_SYSTEM = b'prestigeSystem'
    VEHICLE_ACHIEVEMENTS = b'vehicleAchievements'
    CUSTOMIZATION_ACHIEVEMENTS = b'customizationAchievements'
    STAT_TRACKERS_VEH_STATS_CUT = b'statTrackersVehStatsCut'
    ALL = (
     FRAGS, A15x15_CUT, A30x30_CUT, A7x7_CUT, HISTORICAL_CUT, FORT_SORTIES_CUT, FORT_BATTLES_CUT, RANKED_CUT,
     RANKED_CUT_SEASON_1, RANKED_CUT_SEASON_2, RANKED_CUT_SEASON_3, RANKED_CUT_ARCHIVE, RANKED_CUT_10X10,
     RATED_7x7_CUT, GLOBAL_MAP_COMMON_CUT, FALLOUT_CUT, MARK_OF_MASTERY_CUT, EPIC_BATTLE_CUT,
     COMP7_CUT_SEASON_1, COMP7_CUT_SEASON_2, COMP7_CUT_SEASON_3, COMP7_CUT_ARCHIVE_GRIFFIN, PRESTIGE_SYSTEM,
     VEHICLE_ACHIEVEMENTS, CUSTOMIZATION_ACHIEVEMENTS, COMP7_CUT_ARCHIVE_PEGASUS,
     STAT_TRACKERS_VEH_STATS_CUT, COMP7_CUT_ARCHIVE_MANTICORE, COMP7_CUT_ARCHIVE_DRAGON)


_vehTypeFragsBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FRAGS, b'I', b'H', VEH_TYPE_FRAGS_DEPENDENCIES)
_a15x15CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.A15x15_CUT, b'I', b'III', {})
_a7x7CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.A7x7_CUT, b'I', b'IIIIIII', {})
_rated7x7CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.RATED_7x7_CUT, b'I', b'IIIIIII', {})
_historicalCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.HISTORICAL_CUT, b'I', b'III', {})
_fortBattlesCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FORT_BATTLES_CUT, b'I', b'III', {})
_fortSortiesCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FORT_SORTIES_CUT, b'I', b'III', {})
_globalMapCommonCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.GLOBAL_MAP_COMMON_CUT, b'I', b'III', {})
_falloutCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FALLOUT_CUT, b'I', b'IIII', {})
_rankedCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT, b'I', b'III', {})
_rankedCutSeason1BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_SEASON_1, b'I', b'III', {})
_rankedCutSeason2BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_SEASON_2, b'I', b'III', {})
_rankedCutSeason3BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_SEASON_3, b'I', b'III', {})
_rankedCutArchiveBlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_ARCHIVE, b'I', b'III', {})
_rankedCut10x10BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_10X10, b'I', b'III', {})
_a30x30CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.A30x30_CUT, b'I', b'III', {})
_markOfMasteryCut = DictBlockBuilder(VEHICLE_STATS.MARK_OF_MASTERY_CUT, b'I', b'B', {})
_epicBattleCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.EPIC_BATTLE_CUT, b'I', b'III', {})
_comp7CutSeason1BlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_SEASON_1, b'I', b'IIII', {})
_comp7CutSeason2BlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_SEASON_2, b'I', b'IIII', {})
_comp7CutSeason3BlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_SEASON_3, b'I', b'IIII', {})
_comp7CutArchiveGriffinBlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_ARCHIVE_GRIFFIN, b'I', b'IIII', {})
_comp7CutArchivePegasusBlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_ARCHIVE_PEGASUS, b'I', b'IIII', {})
_comp7CutArchiveManticoreBlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_ARCHIVE_MANTICORE, b'I', b'IIII', {})
_comp7CutArchiveDragonBlockBuilder = DictBlockBuilder(VEHICLE_STATS.COMP7_CUT_ARCHIVE_DRAGON, b'I', b'IIII', {})
_statTrackersVehStatsCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.STAT_TRACKERS_VEH_STATS_CUT, b'I', b'I', {})
_ACHIEVEMENTS15X15_BLOCK_LAYOUT = [
 91, 92, 93, 94, 
 95, 96, 97, 98, 
 99, 
 100, 101, 102, 103, 
 104, 
 105, 
 106, 107, 108, 109, 110, 111, 112, 
 113, 
 114, 115, 116, 
 117, 118, 
 119, 
 120, 121, 122, 123, 124, 
 125, 
 126, 127, 
 128, 129, 
 130, 
 131, 132, 133, 134, 
 135, 
 136, 137, 138, 
 139, 140, 
 141, 142, 143, 
 144, 145, 146, 
 147, 
 148, 149, 
 150, 151, 152, 153, 
 154, 
 155, 156, 157, 158, 
 159, 160, 161, 
 162, 163, 
 164, 165, 
 166, 167, 168, 169, 
 170, 171, 172, 173, 
 174, 175, 
 176, 177, 
 178, 179, 180, 
 181, 182, 183, 184, 
 185, 
 186, 187, 
 188, 189, 190, 
 191, 192, 193, 194, 
 195, 196, 197, 
 198, 
 199, 200, 
 201, 202, 203, 
 204, 205, 206, 207, 
 208, 
 209, 210, 
 211, 212, 213, 
 214, 215, 216, 
 217, 218, 219, 220, 
 221, 
 222, 223, 
 224, 225, 
 226, 227, 228, 
 229, 230, 231, 
 232, 
 233, 234, 
 235, 236, 237, 
 238, 239, 240, 241, 
 242, 243, 244, 
 245, 
 246, 
 247]
_achievements15x15PopUps = [
 104, 105, 106, 107, 108, 109, 
 110, 112, 113, 114, 115, 116, 
 117, 
 118, 
 119, 120, 121, 122, 
 123, 
 124, 125, 126, 127, 138, 139, 
 248, 
 141, 
 142, 143, 111, 128, 135, 
 129, 130, 131, 132, 133, 
 134, 
 136, 154, 137, 249, 
 250, 
 251, 252, 253, 254, 255, 256, 
 257, 
 258, 259, 260, 261, 
 262, 
 263, 264, 265, 266, 
 267, 
 268, 
 269, 270, 271, 
 272, 273, 274, 275, 
 276, 277, 278, 279, 
 144, 
 145, 146, 147, 
 148, 149, 150, 151, 152, 153, 157, 
 158, 
 159, 
 160, 161, 162, 
 163, 
 166, 168, 
 170, 171, 172, 173, 174, 175, 
 176, 
 177, 
 180, 181, 182, 183, 
 184, 185, 187, 190, 
 191, 
 192, 193, 
 195, 196, 197, 198, 
 199, 200, 
 201, 202, 203, 
 204, 
 205, 206, 207, 208, 
 209, 210, 280, 281, 
 282, 283, 284, 285, 
 286, 
 287, 288, 
 289, 290, 291, 292, 
 293, 294, 295, 
 216, 217, 218, 
 219, 
 221, 222, 223, 225, 
 226, 227, 228, 229, 
 230, 231, 
 232, 
 233, 234, 
 235, 236, 237, 
 238, 239, 240, 241, 
 242, 243, 244, 
 245, 
 246, 247]
_achievements15x15BlockBuilder = StaticSizeBlockBuilder(b'achievements', _ACHIEVEMENTS15X15_BLOCK_LAYOUT, ACHIEVEMENT15X15_DEPENDENCIES, _achievements15x15PopUps)
_STEAM_BLOCK_LAYOUT = [
 297, 298, 299, 300, 
 301, 302, 303, 304, 
 305, 306, 307, 308, 
 309, 
 310, 311, 
 312, 
 313, 314, 315, 
 316, 317, 318, 
 319, 320, 
 321, 322, 
 323, 324, 325, 326, 
 327, 328, 329, 330, 331, 
 332, 
 333, 334, 
 335, 
 336, 337, 338, 339, 
 340, 341, 342, 
 343, 
 344, 345, 346, 
 347, 348, 349, 
 350, 351, 352, 
 353, 354, 355, 
 356, 
 357, 358, 
 359, 360, 361, 362, 
 363, 364, 365, 366, 
 367, 368, 
 369, 370, 371, 
 372, 373]
_steamAchievementsPopUps = []
_steamAchievementsLogRecords = [298, 299, 300, 
 302, 303, 304, 
 306, 307, 308, 
 309, 310, 311, 
 313, 
 314, 315, 
 316, 317, 318, 
 319, 320, 321, 
 322, 324, 326, 
 328, 
 330, 331, 332, 
 333, 335, 337, 
 339, 340, 341, 
 343, 345, 346, 
 347, 
 353, 354, 
 355, 356, 357, 
 358, 359, 360, 
 361, 362, 363, 
 364, 
 365, 366, 
 367, 369, 373]
_steamAchievementsBlockBuilder = StaticSizeBlockBuilder(b'steamAchievements', _STEAM_BLOCK_LAYOUT, STEAM_ACHIEVEMENT_DEPENDENCIES, _steamAchievementsPopUps, _steamAchievementsLogRecords)
ACHIEVEMENTS7X7_BLOCK_LAYOUT = [
 375, 376, 377, 
 378, 379, 380, 
 381, 
 382, 383, 384, 385, 
 386, 
 387, 388, 389, 
 390, 391, 392, 393, 
 394, 395, 396, 397, 398, 
 399, 
 400, 
 401, 402, 403, 404, 405, 
 406, 
 407, 408, 409, 410, 
 411, 
 412]
_achievement7x7PopUps = [376, 378, 379, 382, 
 383, 389, 388, 
 386, 385, 391, 393, 
 395, 397, 
 399, 400, 
 402, 404, 406, 408, 
 410, 412]
_achievements7x7BlockBuilder = StaticSizeBlockBuilder(b'achievements7x7', ACHIEVEMENTS7X7_BLOCK_LAYOUT, ACHIEVEMENT7X7_DEPENDENCIES, _achievement7x7PopUps)
ACHIEVEMENTSRATED7X7_BLOCK_LAYOUT = [
 414, 415, 416, 
 417, 418, 419]
_achievementRated7x7PopUps = [b'tacticalAdvantage', b'tacticalSkill', b'secretOperations']
_achievementsRated7x7BlockBuilder = StaticSizeBlockBuilder(b'achievementsRated7x7', ACHIEVEMENTSRATED7X7_BLOCK_LAYOUT, ACHIEVEMENTRATED7X7_DEPENDENCIES, _achievementRated7x7PopUps)
HISTORICAL_ACHIEVEMENTS_BLOCK_LAYOUT = [
 b'guardsman', b'makerOfHistory', b'bothSidesWins',
 b'weakVehiclesWins']
_historicalAchievementsPopUps = [b'guardsman', b'makerOfHistory']
_historicalAchievementsBlockBuilder = StaticSizeBlockBuilder(b'historicalAchievements', HISTORICAL_ACHIEVEMENTS_BLOCK_LAYOUT, HISTORICAL_ACHIEVEMENTS_DEPENDENCIES, _historicalAchievementsPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = [
 426, 427, 428, 429, 
 430, 431, 432, 433, 434, 
 435, 436, 437, 438, 
 439, 40, 
 440, 441, 442, 443, 
 444, 445, 446, 447, 448, 
 449, 
 450, 451, 
 452, 453, 454, 455, 456, 457, 458, 
 459, 460, 
 461, 
 462, 463, 464, 
 465, 466, 467, 468, 
 469, 470, 471, 472, 
 473, 
 474, 475, 
 476, 477, 478, 479, 480, 
 481, 482, 483, 484, 
 485, 
 486, 487, 488, 
 489, 490, 491, 492, 493, 494, 
 495, 496, 497, 
 498, 
 499, 500, 501, 502, 
 503, 504, 505, 506, 507, 
 508, 509, 
 510, 511, 512, 513, 514, 
 515, 516, 517, 518, 
 519, 520, 521, 
 522, 
 523, 524, 525, 526, 
 527, 528, 529, 530, 531, 
 532, 533, 
 534, 
 535, 536, 537, 538, 
 539, 540, 541, 542, 
 543, 544, 545, 
 546, 547, 
 548, 549, 550, 
 551, 552, 553, 554, 
 555, 556, 557, 
 558, 
 559, 560, 561, 562, 
 563, 564, 565, 
 566, 567, 568, 
 569, 
 570, 571, 572, 573, 574, 
 575, 576, 577, 578, 579, 
 580, 581, 
 582, 583, 584, 
 585, 586, 587, 588, 
 589, 590, 591, 592, 
 593, 
 594, 595, 596, 
 597, 598, 599, 600, 
 601, 602, 603, 
 604, 605, 
 606, 
 607, 608, 609, 
 610, 611, 612, 
 49, 613, 614, 615, 
 616, 
 617, 618, 
 619, 620, 621, 622, 
 623, 624, 625, 
 626, 627, 628, 
 629, 
 630, 631, 
 632, 633, 634, 
 635, 636, 637, 638, 
 639, 640, 641, 
 642, 
 643, 644, 645, 646, 
 647, 648, 649, 650, 
 651, 652, 653, 
 654, 
 655, 656, 
 657, 658, 659, 
 660, 661, 662, 
 663, 664, 665, 
 666, 
 667, 668, 
 669, 670, 671, 
 672, 673, 674, 
 675, 676, 677, 
 678, 
 679, 680, 
 681, 682, 
 683, 684, 685, 
 686, 687, 688, 689, 
 690, 
 691, 692, 693, 
 694, 695, 696, 
 697, 698, 699, 
 700, 701, 702, 
 703, 
 704, 705, 706, 
 707, 708, 709, 710, 
 711, 712, 713, 
 714, 
 715, 716, 
 717, 718, 719, 
 720, 721, 722, 
 723, 724, 725, 
 726, 
 727]
_singleAchievementsPopUps = [
 426, 427, 428, 429, 
 430, 431, 432, 433, 434, 
 435, 436, 437, 438, 
 439, 40, 
 440, 441, 442, 443, 
 444, 445, 446, 447, 448, 
 449, 
 450, 451, 452, 
 453, 454, 455, 456, 457, 458, 
 459, 460, 
 461, 
 462, 463, 464, 
 465, 466, 467, 468, 
 469, 470, 471, 472, 
 473, 
 474, 475, 
 476, 477, 478, 479, 480, 
 481, 482, 483, 484, 
 485, 
 486, 487, 488, 
 489, 490, 491, 492, 493, 494, 
 495, 496, 497, 
 498, 
 499, 500, 501, 502, 
 503, 504, 505, 506, 
 507, 508, 509, 
 510, 511, 512, 
 513, 514, 515, 516, 517, 
 518, 519, 520, 521, 
 522, 
 523, 524, 525, 
 526, 527, 528, 529, 
 530, 531, 532, 533, 
 534, 
 539, 540, 541, 
 542, 543, 544, 545, 546, 
 547, 548, 549, 550, 
 551, 
 552, 553, 
 554, 555, 556, 
 557, 558, 559, 560, 
 561, 562, 563, 
 564, 
 565, 566, 
 567, 568, 569, 570, 
 571, 572, 573, 574, 575, 576, 
 577, 
 578, 579, 580, 581, 
 582, 583, 584, 585, 586, 
 587, 588, 589, 
 590, 
 591, 592, 593, 594, 
 595, 596, 597, 598, 
 599, 600, 601, 
 602, 
 603, 604, 605, 
 606, 607, 608, 
 609, 610, 611, 
 612, 
 49, 613, 614, 
 615, 616, 617, 
 618, 619, 620, 
 621, 622, 623, 
 624, 
 625, 626, 
 627, 628, 629, 
 630, 631, 632, 
 633, 634, 635, 
 636, 
 637, 638, 639, 
 640, 641, 
 642, 643, 644, 
 645, 646, 
 647, 
 648, 649, 650, 
 651, 652, 653, 
 654, 655, 656, 
 657, 658, 659, 
 660, 
 661, 662, 
 663, 664, 665, 
 666, 667, 668, 669, 
 670, 671, 672, 
 673, 
 674, 675, 
 676, 677, 678, 
 679, 680, 681, 
 682, 683, 684, 
 685, 
 686, 687, 
 688, 689, 
 690, 691, 692, 693, 
 694, 695, 696, 
 697, 
 698, 699, 
 700, 701, 702, 703, 
 704, 705, 706, 
 707, 708, 709, 
 710, 
 711, 712, 713, 
 714, 715, 716, 
 717, 718, 719, 
 720, 
 721, 722, 
 723, 724, 725, 
 726, 727]
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder(b'singleAchievements', _SINGLE_ACHIEVEMENTS_VALUES, SINGLE_ACHIEVEMENTS_DEPENDENCIES, _singleAchievementsPopUps)
FORT_ACHIEVEMENTS_BLOCK_LAYOUT = [
 729, 730, 731, 732, 733, 734]
_fortPersonalAchievementsPopUps = [
 b'soldierOfFortune']
_fortPersonalAchievementsBlockBuilder = StaticSizeBlockBuilder(b'fortAchievements', FORT_ACHIEVEMENTS_BLOCK_LAYOUT, FORT_ACHIEVEMENTS_DEPENDENCIES, _fortPersonalAchievementsPopUps)
CLAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 b'medalRotmistrov']
_clanAchievementsPopUps = [b'medalRotmistrov']
_clanAchievementsBlockBuilder = StaticSizeBlockBuilder(b'clanAchievements', CLAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _clanAchievementsPopUps)
RANKED_BADGES_BLOCK_LAYOUT = [
 738, 739, 740, 741, 742, 743, 744, 745, 746]
_playerBadgesBlockBuilder = DictBlockBuilder(b'playerBadges', b'I', b'I', PLAYER_BADGES_DEPENDENCIES)
_rankedSeasonsBlockBuilder = DictBlockBuilder(b'rankedSeasons', b'II', b'BHHHH', {})
_rareAchievementsBlockBuilder = ListBlockBuilder(b'rareAchievements', b'I', {})
UNIQUE_ACHIEVEMENT_VALUES = [
 752, 753, 
 754, 755, 
 756, 757, 
 758, 759, 
 760, 761, 
 762, 
 763]
_uniqueAchievementPopUps = [
 752, 753, 
 754, 755, 
 756, 757, 
 758, 759, 
 760, 761, 
 762, 
 763]
_uniqueAchievementBlockBuilder = BinarySetDossierBlockBuilder(b'uniqueAchievements', UNIQUE_ACHIEVEMENT_VALUES, {}, _uniqueAchievementPopUps)
FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT = [
 765, 766, 767, 768, 
 769, 770, 771, 772, 773, 774, 
 775, 776]
_falloutAchievementsPopUps = [765, 766, 767, 768, 769, 
 770, 771, 772, 773, 774, 775]
_falloutAchievementsBlockBuilder = StaticSizeBlockBuilder(b'falloutAchievements', FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _falloutAchievementsPopUps)
EPIC_BATTLE_ACHIEVEMENTS_BLOCK_LAYOUT = [
 778, 779, 780, 781, 
 782, 783]
_epicBattleAchievementsPopUps = [b'frontlineMedal']
_epicBattleAchievementsBlockBuilder = StaticSizeBlockBuilder(b'epicBattleAchievements', EPIC_BATTLE_ACHIEVEMENTS_BLOCK_LAYOUT, EPIC_BATTLE_STATS_DEPENDENCIES, _epicBattleAchievementsPopUps)
_epicBattleSeasonsBlockBuilder = DictBlockBuilder(b'epicSeasons', b'II', b'HHBHH', {})
_battleRoyaleSeasonsBlockBuilder = DictBlockBuilder(b'battleRoyaleSeasons', b'II', b'HHH', {})
_prestigeSystemBlockBuilder = DictBlockBuilder(VEHICLE_STATS.PRESTIGE_SYSTEM, b'I', b'II', {})
_vehicleAchievementsBlockBuilder = DictBlockBuilder(VEHICLE_STATS.VEHICLE_ACHIEVEMENTS, b'H', b'HHI', VEHICLE_ACHIEVEMENTS_DEPENDENCIES, VEHICLE_ACHIEVEMENTS_POP_UPS, set())
_customizationAchievementsBlockBuilder = DictBlockBuilder(VEHICLE_STATS.CUSTOMIZATION_ACHIEVEMENTS, b'H', b'HHI', CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES, CUSTOMIZATION_ACHIEVEMENTS_POP_UPS, set())
_commendationsBlockBuilder = DictBlockBuilder(b'commendations', b'I', b'II', {})
accountDossierLayout = (
 _a15x15BlockBuilder, _a15x15_2BlockBuilder, _clanBlockBuilder,
 _clan2BlockBuilder, _companyBlockBuilder, _company2BlockBuilder, _a7x7BlockBuilder,
 _achievements15x15BlockBuilder, _vehTypeFragsBlockBuilder, _a15x15CutBlockBuilder,
 _rareAchievementsBlockBuilder, _totalBlockBuilder, _a7x7CutBlockBuilder,
 _max15x15BlockBuilder, _max7x7BlockBuilder,
 _achievements7x7BlockBuilder, _historicalBlockBuilder, _maxHistoricalBlockBuilder,
 _historicalAchievementsBlockBuilder, _historicalCutBlockBuilder,
 _uniqueAchievementBlockBuilder,
 _fortBattlesBlockBuilder, _maxFortBattlesBlockBuilder, _fortBattlesCutBlockBuilder,
 _fortSortiesBlockBuilder, _maxFortSortiesBlockBuilder, _fortSortiesCutBlockBuilder,
 _fortBattlesInClanBlockBuilder, _maxFortBattlesInClanBlockBuilder,
 _fortSortiesInClanBlockBuilder,
 _maxFortSortiesInClanBlockBuilder, _fortPersonalAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder, _clanAchievementsBlockBuilder,
 _rated7x7BlockBuilder, _maxRated7x7BlockBuilder, _achievementsRated7x7BlockBuilder,
 _rated7x7CutBlockBuilder,
 _globalMapMiddleBlockBuilder, _globalMapChampionBlockBuilder, _globalMapAbsoluteBlockBuilder,
 _maxGlobalMapMiddleBlockBuilder, _maxGlobalMapChampionBlockBuilder,
 _maxGlobalMapAbsoluteBlockBuilder,
 _globalMapCommonCutBlockBuilder,
 _falloutBlockBuilder, _falloutCutBlockBuilder, _maxFalloutBlockBuilder,
 _falloutAchievementsBlockBuilder,
 _rankedBlockBuilder, _maxRankedBlockBuilder, _rankedCutBlockBuilder,
 _rankedSeasonsBlockBuilder,
 _a30x30BlockBuilder, _a30x30CutBlockBuilder, _max30x30BlockBuilder, _markOfMasteryCut,
 _playerBadgesBlockBuilder,
 _epicBattleBlockBuilder, _epicBattleCutBlockBuilder, _maxEpicBattleBlockBuilder,
 _epicBattleAchievementsBlockBuilder, _rankedSeason1BlockBuilder, _rankedSeason2BlockBuilder,
 _rankedSeason3BlockBuilder, _maxRankedSeason1BlockBuilder, _maxRankedSeason2BlockBuilder,
 _maxRankedSeason3BlockBuilder, _rankedCutSeason1BlockBuilder, _rankedCutSeason2BlockBuilder,
 _rankedCutSeason3BlockBuilder, _rankedArchiveBlockBuilder, _maxRankedArchiveBlockBuilder,
 _rankedCutArchiveBlockBuilder, _epicBattleSeasonsBlockBuilder,
 _battleRoyaleSeasonsBlockBuilder, _ranked_10x10BlockBuilder, _maxRanked_10x10BlockBuilder,
 _rankedCut10x10BlockBuilder, _steamAchievementsBlockBuilder,
 _comp7Season1BlockBuilder, _maxComp7Season1BlockBuilder, _comp7CutSeason1BlockBuilder,
 _comp7Season2BlockBuilder, _maxComp7Season2BlockBuilder, _comp7CutSeason2BlockBuilder,
 _comp7Season3BlockBuilder, _maxComp7Season3BlockBuilder, _comp7CutSeason3BlockBuilder,
 _comp7ArchiveGriffinBlockBuilder, _maxComp7ArchiveGriffinBlockBuilder,
 _comp7CutArchiveGriffinBlockBuilder,
 _prestigeSystemBlockBuilder, _vehicleAchievementsBlockBuilder,
 _customizationAchievementsBlockBuilder,
 _comp7ArchivePegasusBlockBuilder, _maxComp7ArchivePegasusBlockBuilder,
 _comp7CutArchivePegasusBlockBuilder,
 _commendationsBlockBuilder,
 _statTrackersVehStatsCutBlockBuilder,
 _comp7ArchiveManticoreBlockBuilder, _maxComp7ArchiveManticoreBlockBuilder,
 _comp7CutArchiveManticoreBlockBuilder, _comp7ArchiveDragonBlockBuilder,
 _maxComp7ArchiveDragonBlockBuilder, _comp7CutArchiveDragonBlockBuilder)
ACCOUNT_DOSSIER_BLOCKS = {b.name: b for b in accountDossierLayout}
ACCOUNT_DOSSIER_STATIC_BLOCKS = frozenset(b.name for b in accountDossierLayout if isinstance(b, StaticSizeBlockBuilder))
ACCOUNT_DOSSIER_BINARY_SET_BLOCKS = [b.name for b in accountDossierLayout if isinstance(b, BinarySetDossierBlockBuilder)]
ACCOUNT_DOSSIER_DICT_BLOCKS = [b.name for b in accountDossierLayout if isinstance(b, DictBlockBuilder)]
ACCOUNT_DOSSIER_LIST_BLOCKS = [b.name for b in accountDossierLayout if isinstance(b, ListBlockBuilder)]
