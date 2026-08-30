from debug_utils import LOG_WARNING

class BATTLE_RESULTS(object):
    CYBERSPORT_BTNTOTEAMPROFILE = b'#battle_results:cyberSport/btnToTeamProfile'
    CYBERSPORT_POINTS = b'#battle_results:cyberSport/points'
    CYBERSPORT_STATUS_WIN = b'#battle_results:cyberSport/status/win'
    CYBERSPORT_STATUS_LOSE = b'#battle_results:cyberSport/status/lose'
    CYBERSPORT_STATUS_TIE = b'#battle_results:cyberSport/status/tie'
    NODATA = b'#battle_results:noData'
    COMMON_ARENA_FULLNAME = b'#battle_results:common/arena/fullName'
    FINISH_PLAYERTANK_SEPARATOR = b'#battle_results:finish/playerTank/separator'
    FINISH_REASON_0 = b'#battle_results:finish/reason/0'
    FINISH_CLANBATTLE_REASON_ATTACK_1WIN = b'#battle_results:finish/clanBattle_reason_attack/1win'
    FINISH_CLANBATTLE_REASON_ATTACK_1LOSE = b'#battle_results:finish/clanBattle_reason_attack/1lose'
    FINISH_CLANBATTLE_REASON_ATTACK_1TIE = b'#battle_results:finish/clanBattle_reason_attack/1tie'
    FINISH_CLANBATTLE_REASON_DEF_1WIN = b'#battle_results:finish/clanBattle_reason_def/1win'
    FINISH_CLANBATTLE_REASON_DEF_1LOSE = b'#battle_results:finish/clanBattle_reason_def/1lose'
    FINISH_CLANBATTLE_REASON_DEF_1TIE = b'#battle_results:finish/clanBattle_reason_def/1tie'
    FINISH_REASON_1WIN = b'#battle_results:finish/reason/1win'
    FINISH_REASON_1LOSE = b'#battle_results:finish/reason/1lose'
    FINISH_REASON_1TIE = b'#battle_results:finish/reason/1tie'
    FINISH_REASON_2 = b'#battle_results:finish/reason/2'
    FINISH_REASON_3 = b'#battle_results:finish/reason/3'
    FINISH_REASON_4 = b'#battle_results:finish/reason/4'
    FINISH_REASON_5 = b'#battle_results:finish/reason/5'
    FINISH_REASON_8 = b'#battle_results:finish/reason/8'
    FINISH_REASON_9 = b'#battle_results:finish/reason/9'
    FINISH_REASON_10WIN = b'#battle_results:finish/reason/10win'
    FINISH_REASON_10LOSE = b'#battle_results:finish/reason/10lose'
    FINISH_CLARIFICATION_FINISHALLPLAYERSLEFT = b'#battle_results:finish/clarification/finishAllPlayersLeft'
    FINISH_OVERTIME_WIN = b'#battle_results:finish/overtime/win'
    FINISH_OVERTIME_LOSE = b'#battle_results:finish/overtime/lose'
    COMMON_MAINFINISHREASONTITLE = b'#battle_results:common/mainFinishReasonTitle'
    COMMON_OVERTIMEFINISHREASONTITLE = b'#battle_results:common/overtimeFinishReasonTitle'
    COMMON_XPMULTIPLIERSIGN = b'#battle_results:common/xpMultiplierSign'
    COMMON_BATTLEEFFICIENCY_TITLE = b'#battle_results:common/battleEfficiency/title'
    COMMON_BATTLEEFFICIENCYWITHOUTOREDERS_TITLE = b'#battle_results:common/battleEfficiencyWithoutOreders/title'
    COMMON_BATTLEEFFICIENCYWITHSKILLS_TITLE = b'#battle_results:common/battleEfficiencyWithSkills/title'
    COMMON_BATTLEEFFICIENCY_ALLIES = b'#battle_results:common/battleEfficiency/allies'
    COMMON_BATTLEEFFICIENCY_NONE = b'#battle_results:common/battleEfficiency/none'
    COMMON_BATTLEEFFICIENCY_TECHNIQUE = b'#battle_results:common/battleEfficiency/technique'
    COMMON_BATTLEEFFICIENCY_BASES = b'#battle_results:common/battleEfficiency/bases'
    COMMON_BATTLEEFFICIENCY_ALLYBASE = b'#battle_results:common/battleEfficiency/allyBase'
    COMMON_BATTLEEFFICIENCY_ENEMYBASE = b'#battle_results:common/battleEfficiency/enemyBase'
    COMMON_BATTLEEFFICIENCY_NEUTRALBASE = b'#battle_results:common/battleEfficiency/neutralBase'
    COMMON_QUESTS_NOPROGRESS = b'#battle_results:common/quests/noprogress'
    COMMON_TOOLTIP_XPTITLESQUAD = b'#battle_results:common/tooltip/xpTitleSquad'
    COMMON_TOOLTIP_ASSIST_HEADER = b'#battle_results:common/tooltip/assist/header'
    COMMON_TOOLTIP_ASSIST_DESCRIPTION = b'#battle_results:common/tooltip/assist/description'
    COMMON_TOOLTIP_PARAMS_VAL = b'#battle_results:common/tooltip/params/val'
    COMMON_TOOLTIP_PARAMS_VAL_SECONDS = b'#battle_results:common/tooltip/params/val/seconds'
    COMMON_TOOLTIP_ASSIST_PART1 = b'#battle_results:common/tooltip/assist/part1'
    COMMON_TOOLTIP_ASSIST_PART2 = b'#battle_results:common/tooltip/assist/part2'
    COMMON_TOOLTIP_ASSIST_TOTAL = b'#battle_results:common/tooltip/assist/total'
    COMMON_PROGRESSTITLE = b'#battle_results:common/progressTitle'
    COMMON_VEHICLE_RESEARCH = b'#battle_results:common/vehicle/research'
    COMMON_VEHICLE_PURCHASE = b'#battle_results:common/vehicle/purchase'
    COMMON_VEHICLE_DETAILS = b'#battle_results:common/vehicle/details'
    COMMON_FITTING_RESEARCH = b'#battle_results:common/fitting/research'
    COMMON_FITTING_PURCHASE = b'#battle_results:common/fitting/purchase'
    COMMON_RESEARCHPREDICTION = b'#battle_results:common/researchPrediction'
    COMMON_NEWSKILLPREDICTION = b'#battle_results:common/newSkillPrediction'
    COMMON_CREWMEMBER_NEWFREESKILL = b'#battle_results:common/crewMember/newFreeSkill'
    COMMON_CREWMEMBER_NEWSKILL = b'#battle_results:common/crewMember/newSkill'
    COMMON_CREWMEMBER_DESCRIPTION = b'#battle_results:common/crewMember/description'
    COMMON_NOPROGRESS = b'#battle_results:common/noProgress'
    COMMON_TOOLTIP_DAMAGE_HEADER = b'#battle_results:common/tooltip/damage/header'
    COMMON_TOOLTIP_DAMAGE_DESCRIPTION = b'#battle_results:common/tooltip/damage/description'
    COMMON_TOOLTIP_DAMAGE_PART1 = b'#battle_results:common/tooltip/damage/part1'
    COMMON_TOOLTIP_DAMAGE_PART2 = b'#battle_results:common/tooltip/damage/part2'
    COMMON_TOOLTIP_SPOTTED_HEADER = b'#battle_results:common/tooltip/spotted/header'
    COMMON_TOOLTIP_SPOTTED_DESCRIPTION = b'#battle_results:common/tooltip/spotted/description'
    COMMON_TOOLTIP_ARMOR_HEADER = b'#battle_results:common/tooltip/armor/header'
    COMMON_TOOLTIP_ARMOR_DESCRIPTION = b'#battle_results:common/tooltip/armor/description'
    COMMON_TOOLTIP_ARMOR_PART1 = b'#battle_results:common/tooltip/armor/part1'
    COMMON_TOOLTIP_ARMOR_PART2 = b'#battle_results:common/tooltip/armor/part2'
    COMMON_TOOLTIP_ARMOR_PART3 = b'#battle_results:common/tooltip/armor/part3'
    COMMON_TOOLTIP_STUN_HEADER = b'#battle_results:common/tooltip/stun/header'
    COMMON_TOOLTIP_STUN_DESCRIPTION = b'#battle_results:common/tooltip/stun/description'
    COMMON_TOOLTIP_STUN_PART1 = b'#battle_results:common/tooltip/stun/part1'
    COMMON_TOOLTIP_STUN_PART2 = b'#battle_results:common/tooltip/stun/part2'
    COMMON_TOOLTIP_STUN_PART3 = b'#battle_results:common/tooltip/stun/part3'
    COMMON_TOOLTIP_DEFENCE_HEADER = b'#battle_results:common/tooltip/defence/header'
    COMMON_TOOLTIP_DEFENCE_DESCRIPTION = b'#battle_results:common/tooltip/defence/description'
    COMMON_TOOLTIP_DEFENCE_TOTALPOINTS = b'#battle_results:common/tooltip/defence/totalPoints'
    COMMON_TOOLTIP_CAPTURE_HEADER = b'#battle_results:common/tooltip/capture/header'
    COMMON_TOOLTIP_CAPTURE_DESCRIPTION = b'#battle_results:common/tooltip/capture/description'
    COMMON_TOOLTIP_CAPTURE_TOTALPOINTS = b'#battle_results:common/tooltip/capture/totalPoints'
    COMMON_TOOLTIP_KILL_HEADER = b'#battle_results:common/tooltip/kill/header'
    COMMON_TOOLTIP_KILL_1_DESCRIPTION = b'#battle_results:common/tooltip/kill-1/description'
    COMMON_TOOLTIP_KILL0_DESCRIPTION = b'#battle_results:common/tooltip/kill0/description'
    COMMON_TOOLTIP_KILL1_DESCRIPTION = b'#battle_results:common/tooltip/kill1/description'
    COMMON_TOOLTIP_KILL2_DESCRIPTION = b'#battle_results:common/tooltip/kill2/description'
    COMMON_TOOLTIP_KILL3_DESCRIPTION = b'#battle_results:common/tooltip/kill3/description'
    COMMON_TOOLTIP_KILL4_DESCRIPTION = b'#battle_results:common/tooltip/kill4/description'
    COMMON_TOOLTIP_KILL5_DESCRIPTION = b'#battle_results:common/tooltip/kill5/description'
    COMMON_TOOLTIP_KILL6_DESCRIPTION = b'#battle_results:common/tooltip/kill6/description'
    COMMON_TOOLTIP_KILL7_DESCRIPTION = b'#battle_results:common/tooltip/kill7/description'
    COMMON_TOOLTIP_TEAMKILL_HEADER = b'#battle_results:common/tooltip/teamKill/header'
    COMMON_TOOLTIP_TEAMKILL_1_DESCRIPTION = b'#battle_results:common/tooltip/teamKill-1/description'
    COMMON_TOOLTIP_TEAMKILL0_DESCRIPTION = b'#battle_results:common/tooltip/teamKill0/description'
    COMMON_TOOLTIP_TEAMKILL1_DESCRIPTION = b'#battle_results:common/tooltip/teamKill1/description'
    COMMON_TOOLTIP_TEAMKILL2_DESCRIPTION = b'#battle_results:common/tooltip/teamKill2/description'
    COMMON_TOOLTIP_TEAMKILL3_DESCRIPTION = b'#battle_results:common/tooltip/teamKill3/description'
    COMMON_TOOLTIP_TEAMKILL4_DESCRIPTION = b'#battle_results:common/tooltip/teamKill4/description'
    COMMON_TOOLTIP_TEAMKILL5_DESCRIPTION = b'#battle_results:common/tooltip/teamKill5/description'
    COMMON_TOOLTIP_CRITS_HEADER = b'#battle_results:common/tooltip/crits/header'
    COMMON_TOOLTIP_CRITS_DESCRIPTION = b'#battle_results:common/tooltip/crits/description'
    COMMON_TOOLTIP_CRITS_CRITDAMAGE = b'#battle_results:common/tooltip/crits/critDamage'
    COMMON_TOOLTIP_CRITS_CRITDESTRUCTION = b'#battle_results:common/tooltip/crits/critDestruction'
    COMMON_TOOLTIP_CRITS_CRITWOUND = b'#battle_results:common/tooltip/crits/critWound'
    COMMON_TOOLTIP_CRITS_TOTAL = b'#battle_results:common/tooltip/crits/total'
    COMMON_TOOLTIP_COUNTER = b'#battle_results:common/tooltip/counter'
    COMMON_TOOLTIP_COUNTER_FORENEMY = b'#battle_results:common/tooltip/counter/forEnemy'
    COMMON_TOOLTIP_COUNTER_NOITEMS = b'#battle_results:common/tooltip/counter/noItems'
    COMMON_CLANABBREV = b'#battle_results:common/clanAbbrev'
    COMMON_BATTLETYPE_SORTIE = b'#battle_results:common/battleType/sortie'
    COMMON_VEHICLESTATE_ALIVE = b'#battle_results:common/vehicleState/alive'
    COMMON_VEHICLESTATE_DEAD0 = b'#battle_results:common/vehicleState/dead0'
    COMMON_VEHICLESTATE_DEAD1 = b'#battle_results:common/vehicleState/dead1'
    COMMON_VEHICLESTATE_DEAD2 = b'#battle_results:common/vehicleState/dead2'
    COMMON_VEHICLESTATE_DEAD3 = b'#battle_results:common/vehicleState/dead3'
    COMMON_VEHICLESTATE_DEAD4 = b'#battle_results:common/vehicleState/dead4'
    COMMON_VEHICLESTATE_DEAD5 = b'#battle_results:common/vehicleState/dead5'
    COMMON_VEHICLESTATE_DEAD6 = b'#battle_results:common/vehicleState/dead6'
    COMMON_VEHICLESTATE_DEAD7 = b'#battle_results:common/vehicleState/dead7'
    COMMON_VEHICLESTATE_DEAD12 = b'#battle_results:common/vehicleState/dead12'
    COMMON_VEHICLESTATE_DEAD13 = b'#battle_results:common/vehicleState/dead13'
    COMMON_VEHICLESTATE_DEAD15 = b'#battle_results:common/vehicleState/dead15'
    COMMON_VEHICLESTATE_DEAD27 = b'#battle_results:common/vehicleState/dead27'
    COMMON_VEHICLESTATE_DEAD29 = b'#battle_results:common/vehicleState/dead29'
    COMMON_VEHICLESTATE_PREMATURELEAVE = b'#battle_results:common/vehicleState/prematureLeave'
    COMMON_DETAILS_NOPREMTITLE = b'#battle_results:common/details/noPremTitle'
    COMMON_DETAILS_PREMTITLE = b'#battle_results:common/details/premTitle'
    COMMON_DETAILS_CREDITSTITLE = b'#battle_results:common/details/creditsTitle'
    COMMON_DETAILS_XPTITLE = b'#battle_results:common/details/xpTitle'
    COMMON_DETAILS_XPTITLESQUAD = b'#battle_results:common/details/xpTitleSquad'
    COMMON_DETAILS_CRYSTAL = b'#battle_results:common/details/crystal'
    COMMON_DETAILS_GETPREMBTN = b'#battle_results:common/details/getPremBtn'
    COMMON_PREMIUMBONUS = b'#battle_results:common/premiumBonus'
    COMMON_DETAILS_PREMIUMPLUS_CREDITS = b'#battle_results:common/details/premiumPlus/credits'
    COMMON_DETAILS_PREMIUMPLUS_PREMIUM = b'#battle_results:common/details/premiumPlus/premium'
    COMMON_DETAILS_PREMIUMPLUS_SQUAD = b'#battle_results:common/details/premiumPlus/squad'
    COMMON_DETAILS_PREMIUMPLUS_BONUS = b'#battle_results:common/details/premiumPlus/bonus'
    COMMON_DETAILS_PREMIUMPLUS_QUESTS = b'#battle_results:common/details/premiumPlus/quests'
    COMMON_RESULTSSHAREBTN = b'#battle_results:common/resultsShareBtn'
    COMMON_DETAILS_BUYPREMIUMBTN = b'#battle_results:common/details/buyPremiumBtn'
    COMMON_NOINCOME_ALERT_TITLE = b'#battle_results:common/noIncome/alert/title'
    COMMON_NOINCOME_ALERT_TEXT = b'#battle_results:common/noIncome/alert/text'
    COMMON_VEHICLESTATE_VICTORY = b'#battle_results:common/vehicleState/victory'
    COMMON_PREMIUMBONUS_DESCRIPTION = b'#battle_results:common/premiumBonus/description'
    COMMON_PREMIUMBONUS_RULE = b'#battle_results:common/premiumBonus/rule'
    COMMON_PREMIUMBONUS_EXPIREDBATTLERESULT = b'#battle_results:common/premiumBonus/expiredBattleResult'
    COMMON_PREMIUMBONUS_TANKSTATECHANGED = b'#battle_results:common/premiumBonus/tankStateChanged'
    COMMON_PREMIUMBONUS_TANKMENSTATECHANGED = b'#battle_results:common/premiumBonus/tankmenStateChanged'
    COMMON_PREMIUMBONUS_ISXPTOTMENCHANGED = b'#battle_results:common/premiumBonus/isXPToTmenChanged'
    COMMON_PREMIUMBONUS_BONUSLEFT = b'#battle_results:common/premiumBonus/bonusLeft'
    COMMON_PREMIUMBONUS_APPLIEDBONUS = b'#battle_results:common/premiumBonus/appliedBonus'
    COMMON_PREMIUMBONUS_APPLYBONUSBTN = b'#battle_results:common/premiumBonus/applyBonusBtn'
    TEAM_STATS_OWNTEAM = b'#battle_results:team/stats/ownTeam'
    TEAM_STATS_ENEMYTEAM = b'#battle_results:team/stats/enemyTeam'
    TEAM_PLAYERNUMBER_HEADER = b'#battle_results:team/playerNumber/header'
    TEAM_PLAYERNUMBER_BODY = b'#battle_results:team/playerNumber/body'
    TEAM_SQUADHEADER_HEADER = b'#battle_results:team/squadHeader/header'
    TEAM_SQUADHEADER_BODY = b'#battle_results:team/squadHeader/body'
    TEAM_PLAYERHEADER_HEADER = b'#battle_results:team/playerHeader/header'
    TEAM_PLAYERHEADER_BODY = b'#battle_results:team/playerHeader/body'
    TEAM_TANKHEADER_HEADER = b'#battle_results:team/tankHeader/header'
    TEAM_TANKHEADER_BODY = b'#battle_results:team/tankHeader/body'
    TEAM_HEALTHHEADER_HEADER = b'#battle_results:team/healthHeader/header'
    TEAM_HEALTHHEADER_BODY = b'#battle_results:team/healthHeader/body'
    TEAM_DAMAGEHEADER_HEADER = b'#battle_results:team/damageHeader/header'
    TEAM_DAMAGEHEADER_BODY = b'#battle_results:team/damageHeader/body'
    TEAM_FRAGHEADER_HEADER = b'#battle_results:team/fragHeader/header'
    TEAM_FRAGHEADER_BODY = b'#battle_results:team/fragHeader/body'
    TEAM_XPHEADER_HEADER = b'#battle_results:team/xpHeader/header'
    TEAM_XPHEADER_BODY = b'#battle_results:team/xpHeader/body'
    TEAM_MEDALHEADER_HEADER = b'#battle_results:team/medalHeader/header'
    TEAM_MEDALHEADER_BODY = b'#battle_results:team/medalHeader/body'
    TEAM_RESOURCEHEADER_HEADER = b'#battle_results:team/resourceHeader/header'
    TEAM_RESOURCEHEADER_BODY = b'#battle_results:team/resourceHeader/body'
    TEAM_DAMAGEANDCONSUMABLESHEADER_HEADER = b'#battle_results:team/damageAndConsumablesHeader/header'
    TEAM_DAMAGEANDCONSUMABLESHEADER_BODY = b'#battle_results:team/damageAndConsumablesHeader/body'
    TEAM_EPICRANKHEADER_HEADER = b'#battle_results:team/epicRankHeader/header'
    TEAM_EPICRANKHEADER_BODY = b'#battle_results:team/epicRankHeader/body'
    TEAM_EPICRESPAWNHEADER_HEADER = b'#battle_results:team/epicRespawnHeader/header'
    TEAM_EPICRESPAWNHEADER_BODY = b'#battle_results:team/epicRespawnHeader/body'
    TEAM_FALLOUTFRAGHEADER_HEADER = b'#battle_results:team/falloutFragHeader/header'
    TEAM_FALLOUTFRAGHEADER_BODY = b'#battle_results:team/falloutFragHeader/body'
    TEAM_VICTORYSCORE_HEADER = b'#battle_results:team/victoryScore/header'
    TEAM_VICTORYSCORE_BODY = b'#battle_results:team/victoryScore/body'
    TEAM_FLAGS_HEADER = b'#battle_results:team/flags/header'
    TEAM_FLAGS_BODY = b'#battle_results:team/flags/body'
    TEAM_FALLOUTRESOURCEPOINTS_HEADER = b'#battle_results:team/falloutResourcePoints/header'
    TEAM_FALLOUTRESOURCEPOINTS_BODY = b'#battle_results:team/falloutResourcePoints/body'
    TEAM_DEATHS_HEADER = b'#battle_results:team/deaths/header'
    TEAM_DEATHS_BODY = b'#battle_results:team/deaths/body'
    TEAM_TEAMSCORE_HEADER = b'#battle_results:team/teamScore/header'
    TEAM_TEAMSCORE_BODY = b'#battle_results:team/teamScore/body'
    TEAM_DAMAGEHEADERNOSORT_HEADER = b'#battle_results:team/damageHeaderNoSort/header'
    TEAM_FRAGHEADERNOSORT_HEADER = b'#battle_results:team/fragHeaderNoSort/header'
    TEAM_XPHEADERNOSORT_HEADER = b'#battle_results:team/xpHeaderNoSort/header'
    TEAM_VICTORYSCORENOSORT_HEADER = b'#battle_results:team/victoryScoreNoSort/header'
    TEAM_FLAGSNOSORT_HEADER = b'#battle_results:team/flagsNoSort/header'
    TEAM_DEATHSNOSORT_HEADER = b'#battle_results:team/deathsNoSort/header'
    TEAM_SQUADHEADERNOSORT_HEADER = b'#battle_results:team/squadHeaderNoSort/header'
    TEAM_PLAYERHEADERNOSORT_HEADER = b'#battle_results:team/playerHeaderNoSort/header'
    TEAM_TEAMRESOURCETOTAL = b'#battle_results:team/teamResourceTotal'
    TEAM_TEAMINFLUENCETOTAL = b'#battle_results:team/teamInfluenceTotal'
    TEAM_STATS_LABELS_XP = b'#battle_results:team/stats/labels_xp'
    TEAM_STATS_LABELS_XPFORATTACK = b'#battle_results:team/stats/labels_xpForAttack'
    TEAM_STATS_INFOTIP_XPFORATTACK_HEADER = b'#battle_results:team/stats/infotip_xpForAttack/header'
    TEAM_STATS_INFOTIP_XPFORATTACK_BODY = b'#battle_results:team/stats/infotip_xpForAttack/body'
    TEAM_STATS_LABELS_XPFORASSIST = b'#battle_results:team/stats/labels_xpForAssist'
    TEAM_STATS_INFOTIP_XPFORASSIST_HEADER = b'#battle_results:team/stats/infotip_xpForAssist/header'
    TEAM_STATS_INFOTIP_XPFORASSIST_BODY = b'#battle_results:team/stats/infotip_xpForAssist/body'
    TEAM_STATS_LABELS_XPOTHER = b'#battle_results:team/stats/labels_xpOther'
    TEAM_STATS_INFOTIP_XPOTHER_HEADER = b'#battle_results:team/stats/infotip_xpOther/header'
    TEAM_STATS_INFOTIP_XPOTHER_BODY = b'#battle_results:team/stats/infotip_xpOther/body'
    TEAM_STATS_LABELS_SHOTS = b'#battle_results:team/stats/labels_shots'
    TEAM_STATS_LABELS_HITS = b'#battle_results:team/stats/labels_hits'
    TEAM_STATS_LABELS_EXPLOSIONHITS = b'#battle_results:team/stats/labels_explosionHits'
    TEAM_STATS_LABELS_FLAMEEXPLOSIONHITS = b'#battle_results:team/stats/labels_flameExplosionHits'
    TEAM_STATS_LABELS_DAMAGEDEALT = b'#battle_results:team/stats/labels_damageDealt'
    TEAM_STATS_LABELS_SNIPERDAMAGEDEALT = b'#battle_results:team/stats/labels_sniperDamageDealt'
    TEAM_STATS_LABELS_DESTRUCTIBLESDAMAGEDEALT = b'#battle_results:team/stats/labels_destructiblesDamageDealt'
    TEAM_STATS_LABELS_EQUIPMENTDAMAGEDEALT = b'#battle_results:team/stats/labels_equipmentDamageDealt'
    TEAM_STATS_LABELS_ARTILLERYFORTEQUIPDAMAGEDEALT = b'#battle_results:team/stats/labels_artilleryFortEquipDamageDealt'
    TEAM_STATS_LABELS_DAMAGEDEALTRATIO = b'#battle_results:team/stats/labels_damageDealtRatio'
    TEAM_STATS_LABELS_DIRECTHITSRECEIVED = b'#battle_results:team/stats/labels_directHitsReceived'
    TEAM_STATS_LABELS_PIERCINGSRECEIVED = b'#battle_results:team/stats/labels_piercingsReceived'
    TEAM_STATS_LABELS_NODAMAGEDIRECTHITSRECEIVED = b'#battle_results:team/stats/labels_noDamageDirectHitsReceived'
    TEAM_STATS_LABELS_EXPLOSIONHITSRECEIVED = b'#battle_results:team/stats/labels_explosionHitsReceived'
    TEAM_STATS_LABELS_DAMAGEBLOCKEDBYARMOR = b'#battle_results:team/stats/labels_damageBlockedByArmor'
    TEAM_STATS_LABELS_TEAMHITSDAMAGE = b'#battle_results:team/stats/labels_teamHitsDamage'
    TEAM_STATS_LABELS_SPOTTED = b'#battle_results:team/stats/labels_spotted'
    TEAM_STATS_LABELS_DAMAGEDKILLED = b'#battle_results:team/stats/labels_damagedKilled'
    TEAM_STATS_LABELS_KILLED = b'#battle_results:team/stats/labels_killed'
    TEAM_STATS_LABELS_DAMAGEASSISTED = b'#battle_results:team/stats/labels_damageAssisted'
    TEAM_STATS_LABELS_DAMAGEASSISTEDSTUN = b'#battle_results:team/stats/labels_damageAssistedStun'
    TEAM_STATS_LABELS_STUNNUM = b'#battle_results:team/stats/labels_stunNum'
    TEAM_STATS_LABELS_STUNDURATION = b'#battle_results:team/stats/labels_stunDuration'
    TEAM_STATS_LABELS_DAMAGEDEALTBYORDER = b'#battle_results:team/stats/labels_damageDealtByOrder'
    TEAM_STATS_LABELS_KILLSBYORDER = b'#battle_results:team/stats/labels_killsByOrder'
    TEAM_STATS_LABELS_DAMAGEASSISTEDSELF = b'#battle_results:team/stats/labels_damageAssistedSelf'
    TEAM_STATS_LABELS_EQUIPMENTDAMAGEASSISTED = b'#battle_results:team/stats/labels_equipmentDamageAssisted'
    TEAM_STATS_LABELS_DAMAGEASSISTEDSTUNSELF = b'#battle_results:team/stats/labels_damageAssistedStunSelf'
    TEAM_STATS_LABELS_CAPTUREPOINTSVAL = b'#battle_results:team/stats/labels_capturePointsVal'
    TEAM_STATS_LABELS_MILEAGE = b'#battle_results:team/stats/labels_mileage'
    TEAM_STATS_LABELS_TIMESDESTROYED = b'#battle_results:team/stats/labels_timesDestroyed'
    TEAM_STATS_LABELS_DAMAGETOSUPPLIES = b'#battle_results:team/stats/labels_damageToSupplies'
    TEAM_STATS_LABELS_DAMAGEFROMSUPPLIES = b'#battle_results:team/stats/labels_damageFromSupplies'
    TEAM_STATS_LABELS_SUPPLIESDESTROYED = b'#battle_results:team/stats/labels_suppliesDestroyed'
    TEAM_STATS_LABELS_DISTRIBUTEDSUPPLYDAMAGE = b'#battle_results:team/stats/labels_distributedSupplyDamage'
    TEAM_STATS_LABELS_DISTRIBUTEDSUPPLYBASEPOINTS = b'#battle_results:team/stats/labels_distributedSupplyBasePoints'
    TEAM_STATS_LABELS_FLAGS = b'#battle_results:team/stats/labels_flags'
    TEAM_STATS_LABELS_DEATHS = b'#battle_results:team/stats/labels_deaths'
    TEAM_STATS_MILEAGE = b'#battle_results:team/stats/mileage'
    TEAM_STATS_LABELS_DAMAGEDEALTBYSKILLS = b'#battle_results:team/stats/labels_damageDealtBySkills'
    TEAM_STATS_LABELS_HEALED = b'#battle_results:team/stats/labels_healed'
    TEAM_STATS_LABELS_HEALEDALLY = b'#battle_results:team/stats/labels_healedAlly'
    TEAM_STATS_LABELS_CAPTUREDPOINTSOFINTEREST = b'#battle_results:team/stats/labels_capturedPointsOfInterest'
    TEAM_STATS_LABELS_ROLESKILLUSED = b'#battle_results:team/stats/labels_roleSkillUsed'
    TEAM_STATS_CLOSE = b'#battle_results:team/stats/close'
    TEAM_RANKHEADER_HEADER = b'#battle_results:team/rankHeader/header'
    TEAM_RANKHEADER_BODY = b'#battle_results:team/rankHeader/body'
    TEAM_STATS_LABELS_DESTROYRECOVERYRATIO = b'#battle_results:team/stats/labels_destroyRecoveryRatio'
    TEAM_STATS_LABELS_ATKOBJECTIVES = b'#battle_results:team/stats/labels_atkObjectives'
    TEAM_STATS_LABELS_DEFOBJECTIVES = b'#battle_results:team/stats/labels_defObjectives'
    DETAILS_TIME_LBL_OBJECTIVESREACHED = b'#battle_results:details/time/lbl_objectivesReached'
    DETAILS_TIME_LBL_OBJECTIVESDESTROYED = b'#battle_results:details/time/lbl_objectivesDestroyed'
    DETAILS_TIME_LBL_BASESCAPTURED = b'#battle_results:details/time/lbl_basesCaptured'
    DETAILS_TIME_VAL_YES = b'#battle_results:details/time/val_yes'
    DETAILS_TIME_VAL_NO = b'#battle_results:details/time/val_no'
    DETAILS_TIME_EPIC = b'#battle_results:details/time_epic'
    DETAILS_STATS = b'#battle_results:details/stats'
    DETAILS_CREDITS = b'#battle_results:details/credits'
    DETAILS_PREM = b'#battle_results:details/prem'
    DETAILS_PREMPLUS = b'#battle_results:details/premPlus'
    DETAILS_NOPREM = b'#battle_results:details/noPrem'
    DETAILS_TIME = b'#battle_results:details/time'
    DETAILS_XP = b'#battle_results:details/xp'
    DETAILS_RESOURCE = b'#battle_results:details/resource'
    DETAILS_CRYSTAL = b'#battle_results:details/crystal'
    DETAILS_TIME_LBL_ARENACREATETIMEONLYSTR = b'#battle_results:details/time/lbl_arenaCreateTimeOnlyStr'
    DETAILS_TIME_LBL_DURATION = b'#battle_results:details/time/lbl_duration'
    DETAILS_TIME_LBL_PLAYERKILLED = b'#battle_results:details/time/lbl_playerKilled'
    DETAILS_TIME_VALUE = b'#battle_results:details/time/value'
    DETAILS_CALCULATIONS_BOOSTERS = b'#battle_results:details/calculations/boosters'
    DETAILS_CALCULATIONS_BATTLEPAYMENTS = b'#battle_results:details/calculations/battlePayments'
    DETAILS_CALCULATIONS_TACTICALTRAINING = b'#battle_results:details/calculations/tacticalTraining'
    DETAILS_CALCULATIONS_MILITARYMANEUVERS = b'#battle_results:details/calculations/militaryManeuvers'
    DETAILS_CALCULATIONS_HEAVYTRUCKS = b'#battle_results:details/calculations/heavyTrucks'
    DETAILS_CALCULATIONS_INTERMEDIATETOTAL = b'#battle_results:details/calculations/intermediateTotal'
    DETAILS_CALCULATIONS_BASE = b'#battle_results:details/calculations/base'
    DETAILS_CALCULATIONS_XPRECORD = b'#battle_results:details/calculations/xpRecord'
    DETAILS_CALCULATIONS_SQUADBONUS = b'#battle_results:details/calculations/squadBonus'
    DETAILS_CALCULATIONS_NOPENALTY = b'#battle_results:details/calculations/noPenalty'
    DETAILS_CALCULATIONS_EVENT = b'#battle_results:details/calculations/event'
    DETAILS_CALCULATIONS_SUBSTEAMBONUS = b'#battle_results:details/calculations/subsTeamBonus'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_DESERTER = b'#battle_results:details/calculations/fairPlayViolation/deserter'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_EPIC_DESERTER = b'#battle_results:details/calculations/fairPlayViolation/epic_deserter'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_COMP7_DESERTER = b'#battle_results:details/calculations/fairPlayViolation/comp7_deserter'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_AFK = b'#battle_results:details/calculations/fairPlayViolation/afk'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_SUICIDE = b'#battle_results:details/calculations/fairPlayViolation/suicide'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_EVENT_DESERTER = b'#battle_results:details/calculations/fairPlayViolation/event_deserter'
    DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_EVENT_AFK = b'#battle_results:details/calculations/fairPlayViolation/event_afk'
    DETAILS_CALCULATIONS_FRIENDLYFIREPENALTY = b'#battle_results:details/calculations/friendlyFirePenalty'
    DETAILS_CALCULATIONS_FRIENDLYFIRERANKEDXPPENALTY = b'#battle_results:details/calculations/friendlyFireRankedXpPenalty'
    DETAILS_CALCULATIONS_FRIENDLYFIRECOMPENSATION = b'#battle_results:details/calculations/friendlyFireCompensation'
    DETAILS_CALCULATIONS_PLAYERRANKXP = b'#battle_results:details/calculations/playerRankXP'
    DETAILS_CALCULATIONS_FRONTLINEXP = b'#battle_results:details/calculations/frontlineXP'
    DETAILS_CALCULATIONS_DISTRIBUTEDXP = b'#battle_results:details/calculations/distributedXP'
    DETAILS_CALCULATIONS_AUTOREPAIR = b'#battle_results:details/calculations/autoRepair'
    DETAILS_CALCULATIONS_AUTOLOAD = b'#battle_results:details/calculations/autoLoad'
    DETAILS_CALCULATIONS_AUTOEQUIP = b'#battle_results:details/calculations/autoEquip'
    DETAILS_CALCULATIONS_AUTOBOOSTERS = b'#battle_results:details/calculations/autoBoosters'
    DETAILS_CALCULATIONS_AOGASFACTOR = b'#battle_results:details/calculations/aogasFactor'
    DETAILS_CALCULATIONS_PREMIUMVEHICLEXP = b'#battle_results:details/calculations/premiumVehicleXP'
    DETAILS_CALCULATIONS_SQUADXP = b'#battle_results:details/calculations/squadXP'
    DETAILS_CALCULATIONS_SQUADXPPENALTY = b'#battle_results:details/calculations/squadXPPenalty'
    DETAILS_CALCULATIONS_ADDITIONALBONUS = b'#battle_results:details/calculations/additionalBonus'
    DETAILS_CALCULATIONS_TOTAL = b'#battle_results:details/calculations/total'
    DETAILS_CALCULATIONS_PIGGYBANKINFO = b'#battle_results:details/calculations/piggyBankInfo'
    DETAILS_CALCULATIONS_PIGGYBANKINFO_TOOLTIP = b'#battle_results:details/calculations/piggyBankInfo/tooltip'
    DETAILS_CALCULATIONS_FIRSTWIN = b'#battle_results:details/calculations/firstWin'
    DETAILS_CALCULATIONS_IGRBONUS = b'#battle_results:details/calculations/igrBonus'
    DETAILS_CALCULATIONS_FORTORDER = b'#battle_results:details/calculations/fortOrder'
    DETAILS_CALCULATIONS_REFERRALBONUS = b'#battle_results:details/calculations/referralBonus'
    DETAILS_CALCULATIONS_MULTIPLIERINFO_HEADER = b'#battle_results:details/calculations/multiplierInfo/header'
    DETAILS_CALCULATIONS_MULTIPLIERINFO_BODY = b'#battle_results:details/calculations/multiplierInfo/body'
    DETAILS_CALCULATIONS_MULTIPLIERINFO_VEHICLESEPARATOR = b'#battle_results:details/calculations/multiplierInfo/vehicleSeparator'
    DETAILS_CALCULATIONS_SQUAD_RESTRICTIONS_TITLE = b'#battle_results:details/calculations/squad/restrictions/title'
    DETAILS_CALCULATIONS_CRYSTAL_TOTAL = b'#battle_results:details/calculations/crystal/total'
    DETAILS_CALCULATIONS_CRYSTAL_EVENTS = b'#battle_results:details/calculations/crystal/events'
    DETAILS_CALCULATIONS_BIRTHDAYECONOMICSBONUS = b'#battle_results:details/calculations/birthdayEconomicsBonus'
    DETAILS_CALCULATIONS_DIRECTIVES = b'#battle_results:details/calculations/directives'
    TANKSELECTOR_NEXT = b'#battle_results:tankSelector/next'
    VICTORYSCORE = b'#battle_results:victoryScore'
    EXTERMINATIONVICTORY_ALLIES = b'#battle_results:exterminationVictory/allies'
    EXTERMINATIONVICTORY_ENEMIES = b'#battle_results:exterminationVictory/enemies'
    SELECTVEHICLE = b'#battle_results:selectVehicle'
    ALLVEHICLES = b'#battle_results:allVehicles'
    FALLOUT_CLASSIC_WIN_POINTS = b'#battle_results:fallout/classic/win/points'
    FALLOUT_CLASSIC_WIN_CAP = b'#battle_results:fallout/classic/win/cap'
    FALLOUT_CLASSIC_WIN_EXTERMINATION = b'#battle_results:fallout/classic/win/extermination'
    FALLOUT_CLASSIC_LOSE_POINTS = b'#battle_results:fallout/classic/lose/points'
    FALLOUT_CLASSIC_LOSE_CAP = b'#battle_results:fallout/classic/lose/cap'
    FALLOUT_CLASSIC_LOSE_EXTERMINATION = b'#battle_results:fallout/classic/lose/extermination'
    FALLOUT_CLASSIC_TIE = b'#battle_results:fallout/classic/tie'
    FALLOUT_MULTITEAM_WIN_POINTS = b'#battle_results:fallout/multiteam/win/points'
    FALLOUT_MULTITEAM_WIN_CAP = b'#battle_results:fallout/multiteam/win/cap'
    FALLOUT_MULTITEAM_WIN_EXTERMINATION = b'#battle_results:fallout/multiteam/win/extermination'
    FALLOUT_MULTITEAM_ENDED = b'#battle_results:fallout/multiteam/ended'
    GARAGE_UNIQUEDAMAGE = b'#battle_results:garage/uniqueDamage'
    FALLOUT_MULTITEAM_NOPLAYERSELECTED = b'#battle_results:fallout/multiteam/noPlayerSelected'
    PLAYERS_TEAMMATE_UNKNOWN = b'#battle_results:players/teammate/unknown'
    PLAYERS_ENEMY_UNKNOWN = b'#battle_results:players/enemy/unknown'
    GETPREMIUMPOPOVER_HEADERTEXT = b'#battle_results:getPremiumPopover/headerText'
    GETPREMIUMPOPOVER_DESCRIPTIONTEXT = b'#battle_results:getPremiumPopover/descriptionText'
    GETPREMIUMPOPOVER_ACTIONBTN_LABEL = b'#battle_results:getPremiumPopover/actionBtn/label'
    GETPREMIUMPOPOVER_PREM = b'#battle_results:getPremiumPopover/prem'
    GETPREMIUMPOPOVER_AWARD = b'#battle_results:getPremiumPopover/award'
    PERSONALQUEST_BONUS_MULTIPLIER = b'#battle_results:personalQuest/bonus/multiplier'
    PERSONALQUEST_BONUS_DESCR = b'#battle_results:personalQuest/bonus/descr'
    PERSONALQUEST_FAILED_ATTENTION = b'#battle_results:personalQuest/failed/attention'
    PERSONALQUEST_FAILED_DESCR = b'#battle_results:personalQuest/failed/descr'
    PROGRESSIVEREWARD_DESCR = b'#battle_results:progressiveReward/descr'
    CUSTOMIZATIONPROGRESS_DESCR = b'#battle_results:customizationProgress/descr'
    CUSTOMIZATIONPROGRESS_AWARD_RECEIVED = b'#battle_results:customizationProgress/award/received'
    CUSTOMIZATIONPROGRESS_AWARD_NEWLEVEL = b'#battle_results:customizationProgress/award/newLevel'
    GIFTSYSTEM_BANNER_TITLE = b'#battle_results:giftSystem/banner/title'
    GIFTSYSTEM_BANNER_TITLE_EMPHASIZED = b'#battle_results:giftSystem/banner/title/emphasized'
    GIFTSYSTEM_BANNER_STAMPS_LABEL_AVAILABLE = b'#battle_results:giftSystem/banner/stamps/label/available'
    GIFTSYSTEM_BANNER_STAMPS_LABEL_NOTAVAILABLE = b'#battle_results:giftSystem/banner/stamps/label/notAvailable'
    GIFTSYSTEM_BANNER_STAMPS_BUTTON_NOTAVAILABLE = b'#battle_results:giftSystem/banner/stamps/button/notAvailable'
    DETAILS_TIME_LBL_ENUM = (
     DETAILS_TIME_LBL_OBJECTIVESREACHED,
     DETAILS_TIME_LBL_OBJECTIVESDESTROYED,
     DETAILS_TIME_LBL_BASESCAPTURED,
     DETAILS_TIME_LBL_ARENACREATETIMEONLYSTR,
     DETAILS_TIME_LBL_DURATION,
     DETAILS_TIME_LBL_PLAYERKILLED)
    DETAILS_CALCULATIONS_ENUM = (
     DETAILS_CALCULATIONS_BOOSTERS,
     DETAILS_CALCULATIONS_BATTLEPAYMENTS,
     DETAILS_CALCULATIONS_TACTICALTRAINING,
     DETAILS_CALCULATIONS_MILITARYMANEUVERS,
     DETAILS_CALCULATIONS_HEAVYTRUCKS,
     DETAILS_CALCULATIONS_INTERMEDIATETOTAL,
     DETAILS_CALCULATIONS_BASE,
     DETAILS_CALCULATIONS_XPRECORD,
     DETAILS_CALCULATIONS_SQUADBONUS,
     DETAILS_CALCULATIONS_NOPENALTY,
     DETAILS_CALCULATIONS_EVENT,
     DETAILS_CALCULATIONS_SUBSTEAMBONUS,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_DESERTER,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_EPIC_DESERTER,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_COMP7_DESERTER,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_AFK,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_SUICIDE,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_EVENT_DESERTER,
     DETAILS_CALCULATIONS_FAIRPLAYVIOLATION_EVENT_AFK,
     DETAILS_CALCULATIONS_FRIENDLYFIREPENALTY,
     DETAILS_CALCULATIONS_FRIENDLYFIRERANKEDXPPENALTY,
     DETAILS_CALCULATIONS_FRIENDLYFIRECOMPENSATION,
     DETAILS_CALCULATIONS_PLAYERRANKXP,
     DETAILS_CALCULATIONS_FRONTLINEXP,
     DETAILS_CALCULATIONS_DISTRIBUTEDXP,
     DETAILS_CALCULATIONS_AUTOREPAIR,
     DETAILS_CALCULATIONS_AUTOLOAD,
     DETAILS_CALCULATIONS_AUTOEQUIP,
     DETAILS_CALCULATIONS_AUTOBOOSTERS,
     DETAILS_CALCULATIONS_AOGASFACTOR,
     DETAILS_CALCULATIONS_PREMIUMVEHICLEXP,
     DETAILS_CALCULATIONS_SQUADXP,
     DETAILS_CALCULATIONS_SQUADXPPENALTY,
     DETAILS_CALCULATIONS_ADDITIONALBONUS,
     DETAILS_CALCULATIONS_TOTAL,
     DETAILS_CALCULATIONS_PIGGYBANKINFO,
     DETAILS_CALCULATIONS_PIGGYBANKINFO_TOOLTIP,
     DETAILS_CALCULATIONS_FIRSTWIN,
     DETAILS_CALCULATIONS_IGRBONUS,
     DETAILS_CALCULATIONS_FORTORDER,
     DETAILS_CALCULATIONS_REFERRALBONUS,
     DETAILS_CALCULATIONS_MULTIPLIERINFO_HEADER,
     DETAILS_CALCULATIONS_MULTIPLIERINFO_BODY,
     DETAILS_CALCULATIONS_MULTIPLIERINFO_VEHICLESEPARATOR,
     DETAILS_CALCULATIONS_SQUAD_RESTRICTIONS_TITLE,
     DETAILS_CALCULATIONS_CRYSTAL_TOTAL,
     DETAILS_CALCULATIONS_CRYSTAL_EVENTS,
     DETAILS_CALCULATIONS_BIRTHDAYECONOMICSBONUS,
     DETAILS_CALCULATIONS_DIRECTIVES)
    TEAM_STATS_LABELS_ENUM = (
     TEAM_STATS_LABELS_XP,
     TEAM_STATS_LABELS_XPFORATTACK,
     TEAM_STATS_LABELS_XPFORASSIST,
     TEAM_STATS_LABELS_XPOTHER,
     TEAM_STATS_LABELS_SHOTS,
     TEAM_STATS_LABELS_HITS,
     TEAM_STATS_LABELS_EXPLOSIONHITS,
     TEAM_STATS_LABELS_FLAMEEXPLOSIONHITS,
     TEAM_STATS_LABELS_DAMAGEDEALT,
     TEAM_STATS_LABELS_SNIPERDAMAGEDEALT,
     TEAM_STATS_LABELS_DESTRUCTIBLESDAMAGEDEALT,
     TEAM_STATS_LABELS_EQUIPMENTDAMAGEDEALT,
     TEAM_STATS_LABELS_ARTILLERYFORTEQUIPDAMAGEDEALT,
     TEAM_STATS_LABELS_DAMAGEDEALTRATIO,
     TEAM_STATS_LABELS_DIRECTHITSRECEIVED,
     TEAM_STATS_LABELS_PIERCINGSRECEIVED,
     TEAM_STATS_LABELS_NODAMAGEDIRECTHITSRECEIVED,
     TEAM_STATS_LABELS_EXPLOSIONHITSRECEIVED,
     TEAM_STATS_LABELS_DAMAGEBLOCKEDBYARMOR,
     TEAM_STATS_LABELS_TEAMHITSDAMAGE,
     TEAM_STATS_LABELS_SPOTTED,
     TEAM_STATS_LABELS_DAMAGEDKILLED,
     TEAM_STATS_LABELS_KILLED,
     TEAM_STATS_LABELS_DAMAGEASSISTED,
     TEAM_STATS_LABELS_DAMAGEASSISTEDSTUN,
     TEAM_STATS_LABELS_STUNNUM,
     TEAM_STATS_LABELS_STUNDURATION,
     TEAM_STATS_LABELS_DAMAGEDEALTBYORDER,
     TEAM_STATS_LABELS_KILLSBYORDER,
     TEAM_STATS_LABELS_DAMAGEASSISTEDSELF,
     TEAM_STATS_LABELS_EQUIPMENTDAMAGEASSISTED,
     TEAM_STATS_LABELS_DAMAGEASSISTEDSTUNSELF,
     TEAM_STATS_LABELS_CAPTUREPOINTSVAL,
     TEAM_STATS_LABELS_MILEAGE,
     TEAM_STATS_LABELS_TIMESDESTROYED,
     TEAM_STATS_LABELS_DAMAGETOSUPPLIES,
     TEAM_STATS_LABELS_DAMAGEFROMSUPPLIES,
     TEAM_STATS_LABELS_SUPPLIESDESTROYED,
     TEAM_STATS_LABELS_DISTRIBUTEDSUPPLYDAMAGE,
     TEAM_STATS_LABELS_DISTRIBUTEDSUPPLYBASEPOINTS,
     TEAM_STATS_LABELS_FLAGS,
     TEAM_STATS_LABELS_DEATHS,
     TEAM_STATS_LABELS_DAMAGEDEALTBYSKILLS,
     TEAM_STATS_LABELS_HEALED,
     TEAM_STATS_LABELS_HEALEDALLY,
     TEAM_STATS_LABELS_CAPTUREDPOINTSOFINTEREST,
     TEAM_STATS_LABELS_ROLESKILLUSED,
     TEAM_STATS_LABELS_DESTROYRECOVERYRATIO,
     TEAM_STATS_LABELS_ATKOBJECTIVES,
     TEAM_STATS_LABELS_DEFOBJECTIVES)
    TEAM_STATS_INFOTIP_ALL_HEADER_ENUM = (
     TEAM_STATS_INFOTIP_XPFORATTACK_HEADER,
     TEAM_STATS_INFOTIP_XPFORASSIST_HEADER,
     TEAM_STATS_INFOTIP_XPOTHER_HEADER)
    TEAM_STATS_INFOTIP_ALL_BODY_ENUM = (
     TEAM_STATS_INFOTIP_XPFORATTACK_BODY,
     TEAM_STATS_INFOTIP_XPFORASSIST_BODY,
     TEAM_STATS_INFOTIP_XPOTHER_BODY)
    COMMON_VEHICLESTATE_DEAD_ENUM = (
     COMMON_VEHICLESTATE_DEAD0,
     COMMON_VEHICLESTATE_DEAD1,
     COMMON_VEHICLESTATE_DEAD2,
     COMMON_VEHICLESTATE_DEAD3,
     COMMON_VEHICLESTATE_DEAD4,
     COMMON_VEHICLESTATE_DEAD5,
     COMMON_VEHICLESTATE_DEAD6,
     COMMON_VEHICLESTATE_DEAD7,
     COMMON_VEHICLESTATE_DEAD12,
     COMMON_VEHICLESTATE_DEAD13,
     COMMON_VEHICLESTATE_DEAD15,
     COMMON_VEHICLESTATE_DEAD27,
     COMMON_VEHICLESTATE_DEAD29)

    @classmethod
    def getDetailsTimeLbl(cls, statName):
        outcome = (b'#battle_results:details/time/lbl_{}').format(statName)
        if outcome not in cls.DETAILS_TIME_LBL_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getDetailsCalculation(cls, statName):
        outcome = (b'#battle_results:details/calculations/{}').format(statName)
        if outcome not in cls.DETAILS_CALCULATIONS_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getTeamStatsLabel(cls, statName):
        outcome = (b'#battle_results:team/stats/labels_{}').format(statName)
        if outcome not in cls.TEAM_STATS_LABELS_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getTeamStatsInfotipHeader(cls, statName):
        outcome = (b'#battle_results:team/stats/infotip_{}/header').format(statName)
        if outcome not in cls.TEAM_STATS_INFOTIP_ALL_HEADER_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getTeamStatsInfotipBody(cls, statName):
        outcome = (b'#battle_results:team/stats/infotip_{}/body').format(statName)
        if outcome not in cls.TEAM_STATS_INFOTIP_ALL_BODY_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getVehicleDeadState(cls, intType):
        outcome = (b'#battle_results:common/vehicleState/dead{}').format(intType)
        if outcome not in cls.COMMON_VEHICLESTATE_DEAD_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
