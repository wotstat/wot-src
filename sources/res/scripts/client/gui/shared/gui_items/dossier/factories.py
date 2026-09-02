import nations
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE, getType as getAchieveType, ACHIEVEMENT_BLOCK as _AB, RARE_STORAGE_RECORD, HONORED_RANK_RECORD
from gui.shared.gui_items.dossier import achievements as _as
from gui.shared.gui_items.dossier.achievements import abstract as _abstract_achievements
from gui.shared.gui_items.dossier.achievements.loyal_service import LoyalServiceAchievement

class _AchieveFactory(object):

    def __init__(self, achieveClass, name, block, dossier):
        self._achieveClass = achieveClass
        self._name = name
        self._block = block
        self._dossier = dossier
        return

    def getName(self):
        return self._name

    def getBlock(self):
        return self._block

    def getDossier(self):
        return self._dossier

    def getAchieveClass(self):
        return self._achieveClass

    def isInDossier(self):
        return self._achieveClass.checkIsInDossier(self._block, self._name, self._dossier)

    def isValid(self):
        return self._achieveClass.checkIsValid(self._block, self._name, self._dossier)

    def create(self, value=None):
        return self._achieveClass(self._name, self._block, self._dossier, value)

    @classmethod
    def get(cls, achieveClass):
        return (lambda name, block, dossier: cls(achieveClass, name, block, dossier))


class _CustomAchieveFactory(_AchieveFactory):

    def create(self, value=None):
        return self._achieveClass(self._dossier, value)

    @classmethod
    def get(cls, achieveClass):
        return (lambda name, block, dossier: cls(achieveClass, name, block, dossier))


class _BlockAchieveFactory(_AchieveFactory):

    def create(self, value=None):
        return self._achieveClass(self._name, self._dossier, value)

    @classmethod
    def get(cls, achieveClass):
        return (lambda name, block, dossier: cls(achieveClass, name, block, dossier))


class _SequenceAchieveFactory(_AchieveFactory):

    def create(self, value=None):
        counts = {}
        achieves = self._dossier.getBlock(self._block) if self._dossier is not None else ()
        for achieveID in set(achieves):
            counts[achieveID] = achieves.count(achieveID)

        result = {}
        for achieveID, count in counts.iteritems():
            factory = getAchievementFactory((self._block, achieveID), self._dossier)
            if factory is not None:
                achieve = factory.create(value=count)
                if achieve is not None:
                    result[achieveID] = achieve

        return result

    @classmethod
    def get(cls, defaultClass):
        return (lambda name, block, dossier: cls(defaultClass, name, block, dossier))

    def isInDossier(self):
        return True


class _RareAchievesFactory(_SequenceAchieveFactory):

    def isValid(self):
        return not self._dossier.isInRoaming()

    @classmethod
    def get(cls):
        return (lambda rareID, block, dossier: cls(_abstract_achievements.RareAchievement, rareID, block, dossier))


class _NationAchieveFactory(_AchieveFactory):

    def __init__(self, achieveClass, name, nationID, block, dossier):
        super(_NationAchieveFactory, self).__init__(achieveClass, name, block, dossier)
        self._nationID = nationID
        return

    def getNationID(self):
        return self._nationID

    def create(self, value=None):
        return self._achieveClass(self._nationID, self._block, self._dossier, value)

    @classmethod
    def get(cls, achieveClass, nationID=-1):
        return (lambda name, block, dossier: cls(achieveClass, name, nationID, block, dossier))


_ACHIEVEMENTS_BY_BLOCK = {(_AB.RARE): (_BlockAchieveFactory.get(_abstract_achievements.RareAchievement))}
_ACHIEVEMENTS_BY_TYPE = {(ACHIEVEMENT_TYPE.CLASS): (_AchieveFactory.get(_abstract_achievements.ClassProgressAchievement)), 
   (ACHIEVEMENT_TYPE.SERIES): (_AchieveFactory.get(_abstract_achievements.SeriesAchievement))}
_ACHIEVEMENTS_BY_NAME = {(_AB.TOTAL, b'warrior'): (_CustomAchieveFactory.get(_as.regular_ext.WarriorAchievement)), 
   (_AB.TOTAL, b'heroesOfRassenay'): (_CustomAchieveFactory.get(_as.regular_ext.HeroesOfRassenayAchievement)), 
   (_AB.TOTAL, b'medalLafayettePool'): (_CustomAchieveFactory.get(_as.regular_ext.MedalLafayettePoolAchievement)), 
   (_AB.TOTAL, b'medalRadleyWalters'): (_CustomAchieveFactory.get(_as.regular_ext.MedalRadleyWaltersAchievement)), 
   (_AB.TOTAL, b'tankExpert'): (_NationAchieveFactory.get(_as.nation_specific.TankExpertAchievement)), 
   (_AB.TOTAL, b'mechanicEngineer'): (_NationAchieveFactory.get(_as.nation_specific.MechEngineerAchievement)), 
   (_AB.TOTAL, b'mousebane'): (_CustomAchieveFactory.get(_as.simple_progress.MousebaneAchievement)), 
   (_AB.TOTAL, b'beasthunter'): (_CustomAchieveFactory.get(_as.simple_progress.BeasthunterAchievement)), 
   (_AB.TOTAL, b'pattonValley'): (_CustomAchieveFactory.get(_as.simple_progress.PattonValleyAchievement)), 
   (_AB.TOTAL, b'sinai'): (_CustomAchieveFactory.get(_as.simple_progress.SinaiAchievement)), 
   (_AB.TOTAL, b'markOfMastery'): (_CustomAchieveFactory.get(_as.MarkOfMasteryAchievement)), 
   (_AB.TOTAL, b'medalGudz'): (_CustomAchieveFactory.get(_as.class_progress.MedalGudzAchievement)), 
   (_AB.TOTAL, b'medalSamokhin'): (_CustomAchieveFactory.get(_as.class_progress.MedalSamokhinAchievement)), 
   (_AB.TOTAL, b'medalAbrams'): (_CustomAchieveFactory.get(_as.class_progress.MedalAbramsAchievement)), 
   (_AB.TOTAL, b'medalPoppel'): (_CustomAchieveFactory.get(_as.class_progress.MedalPoppelAchievement)), 
   (_AB.TOTAL, b'medalKay'): (_CustomAchieveFactory.get(_as.class_progress.MedalKayAchievement)), 
   (_AB.TOTAL, b'medalEkins'): (_CustomAchieveFactory.get(_as.class_progress.MedalEkinsAchievement)), 
   (_AB.TOTAL, b'medalLeClerc'): (_CustomAchieveFactory.get(_as.class_progress.MedalLeClercAchievement)), 
   (_AB.TOTAL, b'medalLavrinenko'): (_CustomAchieveFactory.get(_as.class_progress.MedalLavrinenkoAchievement)), 
   (_AB.TOTAL, b'marksOnGun'): (_CustomAchieveFactory.get(_as.mark_on_gun.MarkOnGunAchievement)), 
   (_AB.TOTAL, b'sniper'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'medalUshakov'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'reliableComrade'): (_CustomAchieveFactory.get(_as.simple_progress.ReliableComradeAchievement)), 
   (_AB.TOTAL, b'readyForBattleLT'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleLTAchievement)), 
   (_AB.TOTAL, b'readyForBattleMT'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleMTAchievement)), 
   (_AB.TOTAL, b'readyForBattleHT'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleHTAchievement)), 
   (_AB.TOTAL, b'readyForBattleSPG'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleSPGAchievement)), 
   (_AB.TOTAL, b'readyForBattleATSPG'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleATSPGAchievement)), 
   (_AB.TOTAL, b'readyForBattleAllianceUSSR'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleAllianceUSSRAchievement)), 
   (_AB.TOTAL, b'readyForBattleAllianceGermany'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleAllianceGermanyAchievement)), 
   (_AB.TOTAL, b'readyForBattleAllianceUSA'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleAllianceUSAAchievement)), 
   (_AB.TOTAL, b'readyForBattleAllianceFrance'): (_CustomAchieveFactory.get(_as.ready_for_battle.ReadyForBattleAllianceFranceAchievement)), 
   (_AB.TOTAL, b'testartilleryman'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.TOTAL, b'EFC2016Goleador'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.TOTAL, b'markIBomberman'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.TOTAL, b'markIRepairer'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.TOTAL, b'markI100Years'): (_CustomAchieveFactory.get(_as.class_progress.MarkI100Years)), 
   (_AB.TOTAL, b'FE18ClosedStage'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.TOTAL, b'FE18SoloStriker'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.TOTAL, b'FE18SoloMidfielder'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.TOTAL, b'FE18SoloDefender'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.TOTAL, b'superTesterVeteran'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.TOTAL, b'superTesterVeteranCross'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.CLAN, b'medalRotmistrov'): (_CustomAchieveFactory.get(_as.class_progress.MedalRotmistrovAchievement)), 
   (_AB.RATED_7X7, b'strategicOperations'): (_CustomAchieveFactory.get(_as.class_progress.StrategicOperationsAchievement)), 
   (_AB.RATED_7X7, b'tacticalAdvantage'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.RATED_7X7, b'tacticalSkill'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.RATED_7X7, b'secretOperations'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FORT, b'fireAndSword'): (_AchieveFactory.get(_abstract_achievements.DeprecatedClassAchievement)), 
   (_AB.FORT, b'soldierOfFortune'): (_CustomAchieveFactory.get(_as.class_progress.SoldierOfFortuneAchievement)), 
   (_AB.FORT, b'kampfer'): (_AchieveFactory.get(_abstract_achievements.DeprecatedClassAchievement)), 
   (_AB.FORT, b'conqueror'): (_AchieveFactory.get(_abstract_achievements.DeprecatedClassAchievement)), 
   (_AB.FORT, b'counterblow'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FORT, b'crusher'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.HISTORICAL, b'makerOfHistory'): (_CustomAchieveFactory.get(_as.class_progress.MakerOfHistoryAchievement)), 
   (_AB.HISTORICAL, b'guardsman'): (_CustomAchieveFactory.get(_as.class_progress.GuardsmanAchievement)), 
   (_AB.SINGLE, b'diehard'): (_CustomAchieveFactory.get(_as.series.DiehardAchievement)), 
   (_AB.SINGLE, b'invincible'): (_CustomAchieveFactory.get(_as.series.InvincibleAchievement)), 
   (_AB.SINGLE, b'tacticalBreakthrough'): (_CustomAchieveFactory.get(_as.series.TacticalBreakthroughAchievement)), 
   (_AB.SINGLE, b'handOfDeath'): (_CustomAchieveFactory.get(_as.series.HandOfDeathAchievement)), 
   (_AB.SINGLE, b'armorPiercer'): (_CustomAchieveFactory.get(_as.series.ArmorPiercerAchievement)), 
   (_AB.SINGLE, b'titleSniper'): (_CustomAchieveFactory.get(_as.series.TitleSniperAchievement)), 
   (_AB.SINGLE, b'victoryMarch'): (_CustomAchieveFactory.get(_as.series.VictoryMarchAchievement)), 
   (_AB.SINGLE_7X7, b'victoryMarch'): (_CustomAchieveFactory.get(_as.series.VictoryMarchClubAchievement)), 
   (_AB.SINGLE, b'battleCitizen'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'WFC2014'): (_CustomAchieveFactory.get(_as.series.WFC2014Achievement)), 
   (_AB.SINGLE, b'deathTrack'): (_CustomAchieveFactory.get(_as.series.DeathTrackAchievement)), 
   (_AB.SINGLE, b'moonSphere'): (_CustomAchieveFactory.get(_as.regular.MoonSphereAchievement)), 
   (_AB.SINGLE, b'aimer'): (_CustomAchieveFactory.get(_as.series.AimerAchievement)), 
   (_AB.SINGLE, b'tankwomen'): (_CustomAchieveFactory.get(_as.simple_progress.TankwomenAchievement)), 
   (_AB.SINGLE, b'operationWinter'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'fallout'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'fallout2'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'falloutSingleWolf'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'falloutPackOfWolfs'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'falloutSteelHunter'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'falloutAlwaysInLine'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'EFC2016'): (_CustomAchieveFactory.get(_as.series.EFC2016Achievement)), 
   (_AB.SINGLE, b'markIProtector'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'markIBaseProtector'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'xmasTreeBronze'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'xmasTreeSilver'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'xmasTreeGold'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'rankedBattlesPioneer'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'rankedBattlesHero'): (_CustomAchieveFactory.get(_as.series.RankedBattlesHeroAchievement)), 
   (_AB.SINGLE, b'rankedBattlesSeasonOne'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'HE17A1'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'HE17A2'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'HE17A3'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'NY18A1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY18A2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY18A3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'FE18Universal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'FE18Collection1'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'FE18Collection2'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'FE18Collection3'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'FE18OpenRegistration'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'FE18OpenPlayOff'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'FE18OpenFinalStage'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'FE18OpenFirstPlace'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'medalKursk'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'streamersEventUsha'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'streamersEventJove'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'streamersEventAmway921'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'streamersEventLeBwA'): (_AchieveFactory.get(_as.regular.Achieved)), 
   (_AB.SINGLE, b'DdaymarathonMedal'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'twitchPrime'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'twitchPrime2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'twitchPrime3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'twitchPrime4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'alphaTester'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'betaTester'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'15YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'14YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'13YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'12YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'11YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'10YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'09YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'08YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'07YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'06YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'05YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'04YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'03YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'02YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'01YearsOfService'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'betaTester_cn'): (_AchieveFactory.get(LoyalServiceAchievement)), 
   (_AB.SINGLE, b'NY19A1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY19A2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY19A3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'se12019Medal'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'Fest19Collection1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Fest19Collection2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Fest19Collection3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Fest19Racer'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Fest19Offspring'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'RP2018firstmed'): (_AchieveFactory.get(_as.regular.ReferralProgramSingleAchievement)), 
   (_AB.TOTAL, b'RP2018secondmed'): (_AchieveFactory.get(_as.regular.ReferralProgramSingleAchievement)), 
   (_AB.TOTAL, b'RP2018thirdmed'): (_AchieveFactory.get(_as.regular.ReferralProgramSingleAchievement)), 
   (_AB.TOTAL, b'RP2018sergeant'): (_CustomAchieveFactory.get(_as.class_progress.ReferralProgramClassAchievement)), 
   (_AB.TOTAL, b'rankedDivisionFighter'): (_CustomAchieveFactory.get(_as.class_progress.RankedDivisionFighterAchievement)), 
   (_AB.TOTAL, b'rankedStayingPower'): (_CustomAchieveFactory.get(_as.class_progress.RankedStayingPowerAchievement)), 
   (_AB.TEAM_7X7, b'geniusForWarMedal'): (_CustomAchieveFactory.get(_as.simple_progress.GeniusForWarAchievement)), 
   (_AB.TEAM_7X7, b'wolfAmongSheepMedal'): (_CustomAchieveFactory.get(_as.simple_progress.WolfAmongSheepAchievement)), 
   (_AB.TEAM_7X7, b'fightingReconnaissanceMedal'): (_CustomAchieveFactory.get(_as.simple_progress.FightingReconnaissanceAchievement)), 
   (_AB.TEAM_7X7, b'crucialShotMedal'): (_CustomAchieveFactory.get(_as.simple_progress.CrucialShotAchievement)), 
   (_AB.TEAM_7X7, b'forTacticalOperations'): (_CustomAchieveFactory.get(_as.class_progress.ForTacticalOperationsAchievement)), 
   (_AB.TEAM_7X7, b'battleTested'): (_CustomAchieveFactory.get(_as.class_progress.BattleTestedAchievement)), 
   (_AB.TEAM_7X7, b'guerrillaMedal'): (_CustomAchieveFactory.get(_as.simple_progress.GuerrillaAchievement)), 
   (_AB.TEAM_7X7, b'infiltratorMedal'): (_CustomAchieveFactory.get(_as.simple_progress.InfiltratorAchievement)), 
   (_AB.TEAM_7X7, b'sentinelMedal'): (_CustomAchieveFactory.get(_as.simple_progress.SentinelAchievement)), 
   (_AB.TEAM_7X7, b'prematureDetonationMedal'): (_CustomAchieveFactory.get(_as.simple_progress.PrematureDetonationAchievement)), 
   (_AB.TEAM_7X7, b'bruteForceMedal'): (_CustomAchieveFactory.get(_as.simple_progress.BruteForceAchievement)), 
   (_AB.TEAM_7X7, b'promisingFighterMedal'): (_CustomAchieveFactory.get(_as.simple_progress.PromisingFighterAchievement)), 
   (_AB.TEAM_7X7, b'heavyFireMedal'): (_CustomAchieveFactory.get(_as.simple_progress.HeavyFireAchievement)), 
   (_AB.TEAM_7X7, b'rangerMedal'): (_CustomAchieveFactory.get(_as.simple_progress.RangerAchievement)), 
   (_AB.TEAM_7X7, b'fireAndSteelMedal'): (_CustomAchieveFactory.get(_as.simple_progress.FireAndSteelAchievement)), 
   (_AB.TEAM_7X7, b'pyromaniacMedal'): (_CustomAchieveFactory.get(_as.simple_progress.PyromaniacAchievement)), 
   (_AB.UNIQUE, b'histBattle1_battlefield'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle2_battlefield'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle3_battlefield'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle4_battlefield'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle5_battlefield'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle6_battlefield'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle1_historyLessons'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle2_historyLessons'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle3_historyLessons'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle4_historyLessons'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle5_historyLessons'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.UNIQUE, b'histBattle6_historyLessons'): (_AchieveFactory.get(_abstract_achievements.HistoricalAchievement)), 
   (_AB.FALLOUT, b'stormLord'): (_CustomAchieveFactory.get(_as.class_progress.StormLordAchievement)), 
   (_AB.FALLOUT, b'winnerLaurels'): (_CustomAchieveFactory.get(_as.class_progress.WinnerLaurelsAchievement)), 
   (_AB.FALLOUT, b'shoulderToShoulder'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'aloneInTheField'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'fallenFlags'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'effectiveSupport'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'falloutDieHard'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'predator'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'unreachable'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.FALLOUT, b'bannerman'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.EPIC_BATTLE, b'epicBattle1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.EPIC_BATTLE, b'epicBattle2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.EPIC_BATTLE, b'epicBattle3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.EPIC_BATTLE, b'epicBattle4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'BR2019Top1Solo'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.TOTAL, b'BR2019Top1Squad'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'BR2019Title25'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'BR2019Title15'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'BR2019Title5'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'october19'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'november19'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'december19'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'january20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'february20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'march20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'june20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'september20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'october20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'january21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'february21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'march21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'april21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'may21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'june21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'july21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'august21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'september21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'october21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'november21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'december21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'june22'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'july22'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'august22'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY20A1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY20A2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY20A3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobLebwa'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobYusha'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobAmway921'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobKorbenDallas'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobMailand'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobSkill4ltu'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobDezgamez'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobAwesomeEpicGuys'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobTigers'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'medalBobDragons'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bootcampMedal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_5'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_6'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_7'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_8'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_8ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_8quest'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_9'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_NY23'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_10'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_11'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_12'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_13'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_14'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_14_Marathon'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_15'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_16'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_16_Marathon'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_17'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_18'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_18_5_Marathon'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_19'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_20'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BattlePassCommonPr_21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'collectorVehicle'): (_NationAchieveFactory.get(_as.nation_specific.VehicleCollectorAchievement)), 
   (_AB.SINGLE, b'dedicationMedal1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'dedicationMedal2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'dedicationMedal3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'dedicationMedal4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'personalMissionsThird'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'ParagonsFirstSeason'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Paragons_S2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'ParagonsFirstElevenVehicle'): (_AchieveFactory.get(_abstract_achievements.RegularAchievement)), 
   (_AB.SINGLE, b'mt_comp_3_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2023Medal01'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2023Medal02'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'TenYearsCountdownParticipation'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'TenYearsCountdownStageMedal'): (_AchieveFactory.get(_abstract_achievements.StageAchievement)), 
   (_AB.SINGLE, b'TenYearsCountdownSPGEventMedal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'TenYearsCountdownBrawlMedal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BigAnniversaryMedal_CN'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   HONORED_RANK_RECORD: (_CustomAchieveFactory.get(_as.regular.HonoredRankAchievement)), 
   (_AB.SINGLE, b'se2020Medal'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'hw2019Medal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2019Medal1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2019Medal2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2019Medal3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   RARE_STORAGE_RECORD: (_RareAchievesFactory.get()), 
   (_AB.TOTAL, b'wtHunterWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wtBossWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wtSpecBossDefeat'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY21_AtmsphrLevel'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY21_CelebChallenge'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Lebwa_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Yusha_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Amway921_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021KorbenDallas_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021NearYou_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021EvilGranny_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Vspishka_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Inspirer_ru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Circon_eu'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Dakillzor_eu'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021NewMulti2k_eu'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Orzanel_eu'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Cabbagemechanic_na'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021TragicLoss_na'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021CmdrAF_na'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021MasterTortoise_apac'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021SummerTiger_apac'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2021Maharlika_apac'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'gagarin21'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wtxHunterWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wtxBossWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wtxSpecBossDefeat'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'whiteTiger2012'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2021Medal1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2021Medal2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY22_AtmsphrLevel'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY22_CelebChallenge'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'oowTankmanWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'oowStrategistWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'oowCompetetiveWin'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'oowCBTParticipant'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wclTournamentParticipant'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wclParticipant'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wt2022HunterWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wt2022BossWins'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wt2022SpecBossDefeat'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7Season1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2022Medal01'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hw2022Medal02'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY23_AtmsphrLevel'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY23_CelebChallenge'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_2023_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Cosmic_MartianStalker'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'Cosmic_SpaceTrace'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.MT, b'rpBronzeMedal'): (_AchieveFactory.get(_as.regular.ReferralProgramSingleAchievement)), 
   (_AB.MT, b'rpSilverMedal'): (_AchieveFactory.get(_as.regular.ReferralProgramSingleAchievement)), 
   (_AB.MT, b'rpGoldMedal'): (_AchieveFactory.get(_as.regular.ReferralProgramSingleAchievement)), 
   (_AB.SINGLE, b'onboardingMedal'): (_AchieveFactory.get(_abstract_achievements.RegularAchievement)), 
   (_AB.SINGLE, b'comp7_3_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY24_AtmsphrLevel'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_3_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_3_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hb24Medal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_4_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_3_4_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'races24FirstPlace'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'races24Progression'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BirthdayPr_2025'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'BirthdayPr_2026'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'wt2024HunterWins'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.TOTAL, b'wt2024BossWins'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.TOTAL, b'wt2024MaxPlasma'): (_AchieveFactory.get(_abstract_achievements.QuestAchievement)), 
   (_AB.SINGLE, b'comp7_4_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_1_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_1_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_2_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_2_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY25_AtmsphrLevel'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_3_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_3_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'cosm2025_medal_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'cosm2025_medal_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hb25MedalOffence'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hb25MedalDefence'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2025Lebwa'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2025Yusha'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2025NearYou'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'bob2025Jove'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'support_2025'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_4_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_4_4_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'wt2025'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TEAM_7X7, b'willToWinSpirit'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TEAM_7X7, b'armoredFist'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TEAM_7X7, b'noMansLand'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TEAM_7X7, b'kingOfTheHill'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TEAM_7X7, b'godOfWar'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'luckyDevil'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.EPIC_BATTLE, b'frontlineMedal'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_1_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_1_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'portal2025Medal_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'portal2025Medal_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_2_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_2_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'clan_season_25_first'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'clan_season_25_last'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY26_AtmsphrLevel'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'NY26_CelebTaskCompleted'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.EPIC_BATTLE, b'saboteur'): (_CustomAchieveFactory.get(_as.simple_progress.SaboteurAchievement)), 
   (_AB.TOTAL, b'huntsman'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'medalBurda'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.TOTAL, b'medalDumitru'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'cosm2026_medal_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'cosm2026_medal_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_3'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_3_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_3_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hb26MedalTanker'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'hb26MedalSPG'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_4'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_4_champion'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_5_4_legend'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'wt2026'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'clan_season_26_first'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'clan_season_26_last'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1_champion_0'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1_champion_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1_champion_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1_legend_0'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1_legend_1'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement)), 
   (_AB.SINGLE, b'comp7_6_1_legend_2'): (_AchieveFactory.get(_abstract_achievements.DeprecatedAchievement))}
for _nID, _ in enumerate(nations.NAMES):
    _ACHIEVEMENTS_BY_NAME[(_AB.TOTAL, b'tankExpert%d' % _nID)] = _NationAchieveFactory.get(_as.nation_specific.TankExpertAchievement, _nID)
    _ACHIEVEMENTS_BY_NAME[(_AB.TOTAL, b'mechanicEngineer%d' % _nID)] = _NationAchieveFactory.get(_as.nation_specific.MechEngineerAchievement, _nID)
    _ACHIEVEMENTS_BY_NAME[(_AB.TOTAL, b'collectorVehicle%d' % _nID)] = _NationAchieveFactory.get(_as.nation_specific.VehicleCollectorAchievement, _nID)

def getAchievementFactory(record, dossier=None):
    achieveType = getAchieveType(record)
    if record in _ACHIEVEMENTS_BY_NAME:
        factoryMaker = _ACHIEVEMENTS_BY_NAME[record]
    elif achieveType is not None and achieveType in _ACHIEVEMENTS_BY_TYPE:
        factoryMaker = _ACHIEVEMENTS_BY_TYPE[achieveType]
    elif record[0] in _ACHIEVEMENTS_BY_BLOCK:
        factoryMaker = _ACHIEVEMENTS_BY_BLOCK[record[0]]
    else:
        factoryMaker = _AchieveFactory.get(_abstract_achievements.RegularAchievement)
    return factoryMaker(record[1], record[0], dossier)
