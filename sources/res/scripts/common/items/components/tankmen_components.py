from __future__ import absolute_import
import typing
from debug_utils import LOG_ERROR
from items.components import component_constants
from items.components import legacy_stuff
from items.components import skills_constants
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from past.builtins import unicode
    from items.components import shared_components

class SPECIAL_VOICE_TAG(object):
    BUFFON = b'buffonSpecialVoice'
    SABATON = b'sabatonSpecialVoice'
    OFFSPRING = b'offspringSpecialVoice'
    RACER = b'racerSpecialVoice'
    RACER_EN = b'racerSpecialVoiceEn'
    CELEBRITY_2021 = b'celebrity21SpecialVoice'
    CELEBRITY_2022 = b'celebrity22SpecialVoice'
    CELEBRITY_2023 = b'celebrity23SpecialVoice'
    CELEBRITY_2024 = b'celebrity24SpecialVoice'
    CELEBRITY_2025 = b'celebrity25SpecialVoice'
    CELEBRITY_2026 = b'celebrity26SpecialVoice'
    DAY_OF_COSMONAUTICS_21 = b'gagarin21_specialVoice'
    MIHO = b'mihoSpecialVoice'
    YHA = b'yhaSpecialVoice'
    QUICKY_BABY = b'quickyBabySpecialVoice'
    WITCHES_CREW = b'witchesSpecialVoice'
    HAND_OF_BLOOD = b'handOfBloodSpecialVoice'
    NAMELESS = b'japan:J29_Nameless'
    EDELWEISS = b'japan:J30_Edelweiss'
    TALKTOME_GOOSE = b'talktomeGooseSpecialVoice'
    SKILL_4_LTU = b'skill4ltuSpecialVoice'
    ALICE = b'aliceSpecialVoice'
    DARJEELING = b'darjeelingSpecialVoice'
    KEI = b'keiSpecialVoice'
    HW25_QUICKYBABY = b'hw25_Quickybaby_SpecialVoice'
    HW25_MAILAND = b'hw25_Mailand_SpecialVoice'
    HW25_MOUZ_AKROBAT = b'hw25_MouzAkrobat_SpecialVoice'
    HW25_SKILL4LTU = b'hw25_Skill4ltu_SpecialVoice'
    HW25_LU_JUN_CN = b'hw25_LuJun_CN_SpecialVoice'
    HW25_TITI_CN = b'hw25_Titi_CN_SpecialVoice'
    HW25_DA_KUN_CN = b'hw25_DaKun_CN_SpecialVoice'
    HW25_PANCHEZHANG_CN = b'hw25_Panchezhang_CN_SpecialVoice'
    ERWIN = b'erwinSpecialVoice'
    JAGER_MAILAND = b'jager_mailand_SpecialVoice'
    JAGER_MOUZAKROBAT = b'jager_mouzAkrobat_SpecialVoice'
    BATTLE_OF_BLOGGERS = (b'ru1_LebwaSpecialVoice', b'ru2_YushaSpecialVoice', b'ru3_Amway921SpecialVoice', b'ru4_KorbenDallasSpecialVoice', b'eu1_MailandSpecialVoice', b'eu2_Skill4ltuSpecialVoice', b'eu3_DezgamezSpecialVoice', b'eu4_AwesomeEpicGuysSpecialVoice')
    BATTLE_OF_BLOGGERS_2021 = (b'bb21_ru1_Yusha_specialVoice', b'bb21_ru1_Vspishka_specialVoice', b'bb21_ru2_Amway921_specialVoice', b'bb21_ru2_Korbendailas_specialVoice', b'bb21_ru3_Lebwa_specialVoice', b'bb21_ru3_Inspirer_specialVoice', b'bb21_ru4_Evilgranny_specialVoice', b'bb21_ru4_Nearyou_specialVoice', b'bb21_eu1_Circon_specialVoice', b'bb21_eu2_Dakillzor_specialVoice', b'bb21_eu3_Newmulti2k_specialVoice', b'bb21_eu4_Orzanel_specialVoice', b'bb21_na1_Cabbagemechanic_specialVoice', b'bb21_na2_Tragicloss_specialVoice', b'bb21_na3_Cmdraf_specialVoice', b'bb21_asia1_Mastertortoise_specialVoice', b'bb21_asia2_Summertiger_specialVoice', b'bb21_asia3_Maharlika_specialVoice')
    G_I_JOE_TWITCH_2021 = (b'duke_specialVoice', b'cobra_specialVoice')
    WHITE_TIGER_EVENT_2021 = (b'letov_SpecialVoice', b'armand_SpecialVoice', b'elisa_SpecialVoice', b'krieger_SpecialVoice')
    WHITE_TIGER_EVENT_2022 = (b'villanelle_SpecialVoice', b'ermelinda_SpecialVoice')
    WHITE_TIGER_EVENT_2023 = (b'hannelore_SpecialVoice', b'jana_SpecialVoice')
    WHITE_TIGER_EVENT_2024 = (b'ermelinda24_SpecialVoice', b'krieger24_SpecialVoice', b'mouzAkrobat24_SpecialVoice', b'quickyBaby24_SpecialVoice', b'dakillzor24_SpecialVoice', b'skill4ltu24_SpecialVoice', b'bMeng24_SpecialVoice', b'saoNian24_SpecialVoice', b'yiTuanTuan24_SpecialVoice', b'zhongPengFei24_SpecialVoice')
    SABATON_2021 = b'sabaton21_specialVoice'
    G_I_JOE_2022 = (b'baroness22SpecialVoice', b'coverGirl22SpecialVoice')
    BPH_2022 = (b'commander_bph_2022_1', b'commander_bph_2022_2', b'commander_bph_2022_3', b'commander_bph_2022_4')
    BP_12_M = (b'tankman_bp_12_m_5', b'tankman_bp_12_m_8', b'tankman_bp_12_m_9', b'tankman_bp_12_m_10')
    BP_H2 = (b'tankmen_bp1002_1', b'tankmen_bp1002_3')
    BP_13 = (b'tankmen_bp13_1', b'tankmen_bp13_2', b'tankmen_bp13_3', b'tankmen_bp13_4', b'tankmen_bp13_5', b'tankmen_bp13_6', b'tankmen_bp13_7', b'tankmen_bp13_8', b'tankmen_bp13_9')
    CYGAN = b'cygan_SpecialVoice'
    MARTY_VOLE = b'martyVole_SpecialVoice'
    CTM_24 = (b'kirk_SpecialVoice', b'spock_SpecialVoice', b'uhura_SpecialVoice')
    ERIKA = b'erikaSpecialVoice'
    MIKA = b'mikaSpecialVoice'
    BP_14_M = (b'tankmen_bp14_5', b'tankmen_bp14_6')
    MT_LB_1 = b'tankmen_mtlb1_1'
    BP_15_M = (b'tankmen_bp15_5', b'tankmen_bp15_6', b'tankmen_bp15_7', b'tankmen_bp15_8', b'tankmen_bp15_9')
    BP_H4 = (b'tankmen_bp1004_1', b'tankmen_bp1004_2', b'tankmen_bp1004_3', b'tankmen_bp1004_4', b'tankmen_bp1004_5')
    BP_16_M = (b'tankmen_bp16_5', b'tankmen_bp16_6', b'tankmen_bp16_7', b'tankmen_bp16_8', b'tankmen_bp16_9')
    BP_17_DC_M = (b'tankmen_bp17_5', b'tankmen_bp17_8')
    BP_18_M = (b'tankmen_bp18_5', b'tankmen_bp18_6', b'tankmen_bp18_7', b'tankmen_bp18_8', b'tankmen_bp18_9')
    BP_18_NM = (b'tankmen_bp18_10', b'tankmen_bp18_11', b'tankmen_bp18_12', b'tankmen_bp18_13', b'tankmen_bp18_14')
    BP_H5 = (b'tankmen_bp1005_1', b'tankmen_bp1005_2')
    BP_H6 = (b'tankmen_bp1006_1', b'tankmen_bp1006_2', b'tankmen_bp1006_3', b'tankmen_bp1006_4', b'tankmen_bp1006_5', b'tankmen_bp1006_6')
    BP_19_M = (b'tankmen_bp19_5', b'tankmen_bp19_6', b'tankmen_bp19_7', b'tankmen_bp19_8', b'tankmen_bp19_9')
    BP_20_M = (b'tankmen_bp20_5', b'tankmen_bp20_6', b'tankmen_bp20_7', b'tankmen_bp20_8', b'tankmen_bp20_9')
    MT_LB_4 = b'tankmen_mtlb4_1'
    ALL = (
     BUFFON, SABATON, OFFSPRING, RACER, RACER_EN, CELEBRITY_2021, MIHO, YHA, ALICE, DARJEELING, CELEBRITY_2022, DAY_OF_COSMONAUTICS_21, SABATON_2021, QUICKY_BABY, WITCHES_CREW, CELEBRITY_2023, HAND_OF_BLOOD, NAMELESS, EDELWEISS, SKILL_4_LTU, TALKTOME_GOOSE, CELEBRITY_2024, CYGAN, ERIKA, MIKA, MARTY_VOLE, MT_LB_1, MT_LB_4, CELEBRITY_2025, KEI, HW25_QUICKYBABY, HW25_MAILAND, HW25_MOUZ_AKROBAT, HW25_SKILL4LTU, HW25_LU_JUN_CN, HW25_TITI_CN, HW25_DA_KUN_CN, HW25_PANCHEZHANG_CN, CELEBRITY_2026, ERWIN, JAGER_MAILAND, JAGER_MOUZAKROBAT) + BATTLE_OF_BLOGGERS + BATTLE_OF_BLOGGERS_2021 + G_I_JOE_TWITCH_2021 + WHITE_TIGER_EVENT_2021 + G_I_JOE_2022 + WHITE_TIGER_EVENT_2022 + BPH_2022 + WHITE_TIGER_EVENT_2023 + BP_12_M + BP_H2 + BP_13 + CTM_24 + BP_14_M + WHITE_TIGER_EVENT_2024 + BP_15_M + BP_H4 + BP_16_M + BP_17_DC_M + BP_18_M + BP_18_NM + BP_H5 + BP_H6 + BP_19_M + BP_20_M


class SPECIAL_CREW_TAG(object):
    SABATON = b'sabatonCrew'
    OFFSPRING = b'offspringCrew'
    MIHO = b'mihoCrew'
    YHA = b'yhaCrew'
    WITCHES_CREW = b'witchesCrew'
    MIKA_CREW = b'mikaCrew'
    DARJEELING_CREW = b'darjeelingCrew'
    HW25_CREW = b'hw25_Crew'
    HW25_CREW_CN = b'hw25_Crew_CN'
    HIPPO_CREW = b'hippoCrew'
    ALL = (
     SABATON, OFFSPRING, MIHO, YHA, WITCHES_CREW, MIKA_CREW, DARJEELING_CREW, HW25_CREW, HW25_CREW_CN,
     HIPPO_CREW)


class GROUP_TAG(object):
    PASSPORT_REPLACEMENT_FORBIDDEN = b'passportReplacementForbidden'
    RESTRICTIONS = (
     PASSPORT_REPLACEMENT_FORBIDDEN,)
    RANGE = RESTRICTIONS + tuple(skills_constants.ROLES) + SPECIAL_VOICE_TAG.ALL + SPECIAL_CREW_TAG.ALL


class Rank(legacy_stuff.LegacyStuff):
    __slots__ = (b'__name', b'__i18n', b'__icon')

    def __init__(self, name, i18n=None, icon=None):
        super(Rank, self).__init__()
        self.__name = name
        self.__i18n = i18n
        self.__icon = icon or component_constants.EMPTY_STRING
        return

    def __repr__(self):
        return (b'Rank({})').format(self.__name)

    @property
    def name(self):
        return self.__name

    @property
    def userString(self):
        if self.__i18n is not None:
            return self.__i18n.value
        else:
            return component_constants.EMPTY_STRING
            return

    @property
    def icon(self):
        return self.__icon


class RanksSet(object):
    __slots__ = (b'__ranks', b'__rankIDsByNames')

    def __init__(self):
        super(RanksSet, self).__init__()
        self.__ranks = []
        self.__rankIDsByNames = {}
        return

    def __repr__(self):
        return (b'RanksSet({})').format(list(self.__rankIDsByNames))

    def add(self, rank):
        self.__rankIDsByNames[rank.name] = len(self.__ranks)
        self.__ranks.append(rank)
        return

    def getRankByID(self, rankID):
        if 0 <= rankID < len(self.__ranks):
            return self.__ranks[rankID]
        else:
            return
            return

    def getRankByName(self, name):
        if name in self.__rankIDsByNames:
            return self.__ranks[self.__rankIDsByNames[name]]
        else:
            return
            return

    def getIDByName(self, name):
        if name in self.__rankIDsByNames:
            return self.__rankIDsByNames[name]
        raise SoftException((b'Name of rank "{}" is not found').format(name))
        return

    def generator(self):
        for rank in self.__ranks:
            yield (
             self.__rankIDsByNames[rank.name], rank)

        return


class RoleRanks(legacy_stuff.LegacyStuff):
    __slots__ = (b'__ranks',)

    def __init__(self):
        super(RoleRanks, self).__init__()
        self.__ranks = {}
        for skill in skills_constants.ROLES:
            self.__ranks[skill] = component_constants.EMPTY_TUPLE

        return

    def __repr__(self):
        return (b'RoleRanks(ranks={}, radioman={}, driver={}, gunner={}, loader={})').format(self.commander, self.radioman, self.driver, self.gunner, self.loader)

    @property
    def commander(self):
        return self.__ranks[b'commander']

    @property
    def radioman(self):
        return self.__ranks[b'radioman']

    @property
    def driver(self):
        return self.__ranks[b'driver']

    @property
    def gunner(self):
        return self.__ranks[b'gunner']

    @property
    def loader(self):
        return self.__ranks[b'loader']

    def getRanksIDs(self, roleName):
        if roleName in self.__ranks:
            return self.__ranks[roleName]
        else:
            return component_constants.EMPTY_TUPLE

        return

    def getRankID(self, roleName, rankIdx):
        ranks = self.getRanksIDs(roleName)
        if 0 <= rankIdx < len(ranks):
            return ranks[rankIdx]
        else:
            return
            return

    def setRanksIDs(self, roleName, roleIDs):
        if roleName not in skills_constants.ROLES:
            raise SoftException((b'Role {} is not found').format(roleName))
        self.__ranks[roleName] = roleIDs
        return


class NationGroup(legacy_stuff.LegacyStuff):
    __slots__ = (b'__name', b'__isFemales', b'__notInShop', b'__firstNamesIDs', b'__lastNamesIDs', b'__iconsIDs', b'__weight', b'__tags', b'__roles', b'__groupID')

    def __init__(self, groupID, name, isFemales, notInShop, firstNamesIDs, lastNamesIDs, iconsIDs, weight, tags, roles):
        super(NationGroup, self).__init__()
        self.__groupID = groupID
        self.__name = name
        self.__isFemales = isFemales
        self.__notInShop = notInShop
        self.__firstNamesIDs = firstNamesIDs
        self.__lastNamesIDs = lastNamesIDs
        self.__iconsIDs = iconsIDs
        self.__weight = weight
        self.__tags = tags
        self.__roles = roles
        return

    def __repr__(self):
        return (b'NationGroup(groupID={}, name={}, isFemales={}, notInShop={}, weight={}, tags={}, roles={})').format(self.__groupID, self.__name, self.__isFemales, self.__notInShop, self.__weight, self.__tags, self.__roles)

    @property
    def groupID(self):
        return self.__groupID

    @property
    def name(self):
        return self.__name

    @property
    def isFemales(self):
        return self.__isFemales

    @property
    def notInShop(self):
        return self.__notInShop

    @property
    def firstNames(self):
        return self.__firstNamesIDs

    @property
    def firstNamesList(self):
        return list(self.__firstNamesIDs)

    @property
    def lastNames(self):
        return self.__lastNamesIDs

    @property
    def lastNamesList(self):
        return list(self.__lastNamesIDs)

    @property
    def icons(self):
        return self.__iconsIDs

    @property
    def iconsList(self):
        return list(self.__iconsIDs)

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value
        return

    @property
    def tags(self):
        return self.__tags

    @property
    def roles(self):
        return self.__roles

    @property
    def rolesList(self):
        return list(self.__roles)

    @property
    def isUnique(self):
        return len(self.__firstNamesIDs) * len(self.__lastNamesIDs) * len(self.__iconsIDs) == 1


class NationConfig(legacy_stuff.LegacyStuff):
    __slots__ = (b'__name', b'__normalGroups', b'__premiumGroups', b'__roleRanks', b'__firstNames', b'__lastNames', b'__icons', b'__ranks')

    def __init__(self, name, normalGroups=None, premiumGroups=None, roleRanks=None, firstNames=None, lastNames=None, icons=None, ranks=None):
        super(NationConfig, self).__init__()
        self.__name = name
        self.__normalGroups = normalGroups or component_constants.EMPTY_TUPLE
        self.__premiumGroups = premiumGroups or component_constants.EMPTY_TUPLE
        self.__roleRanks = roleRanks
        self.__firstNames = firstNames or {}
        self.__lastNames = lastNames or {}
        self.__icons = icons or {}
        self.__ranks = ranks
        return

    def __repr__(self):
        return (b'NationConfig({})').format(self.__name)

    @property
    def normalGroups(self):
        return self.__normalGroups

    @property
    def premiumGroups(self):
        return self.__premiumGroups

    @property
    def roleRanks(self):
        return self.__roleRanks

    @property
    def firstNames(self):
        return self.__firstNames

    @property
    def lastNames(self):
        return self.__lastNames

    @property
    def icons(self):
        return self.__icons

    @property
    def ranks(self):
        return self.__ranks

    def hasFirstName(self, nameID):
        return nameID in self.__firstNames

    def hasLastName(self, nameID):
        return nameID in self.__lastNames

    def hasIcon(self, iconID):
        return iconID in self.__icons

    def getGroups(self, isPremium):
        if isPremium:
            return self.__premiumGroups
        else:
            return self.__normalGroups

        return

    def getRoleRanks(self, roleName):
        if self.__roleRanks is not None:
            return self.__roleRanks.getRanksIDs(roleName)
        else:
            return component_constants.EMPTY_TUPLE
            return

    def getFirstName(self, nameID):
        return self.__firstNames.get(nameID, component_constants.EMPTY_STRING)

    def getLastName(self, nameID):
        return self.__lastNames.get(nameID, component_constants.EMPTY_STRING)

    def getIcon(self, iconID):
        return self.__icons.get(iconID, component_constants.EMPTY_STRING)

    def getExtensionLessIcon(self, iconID):
        if iconID in self.__icons:
            return self.__icons[iconID].split(b'.png')[0]
        else:
            return component_constants.EMPTY_STRING

        return

    def getRank(self, rankID):
        if self.__ranks is not None:
            return self.__ranks.getRankByID(rankID)
        else:
            return
            return


class LoreGroupComponent(object):
    __slots__ = (b'descr_by_nation',)
    DEFAULT = b'default'

    def __init__(self, descr):
        self.descr_by_nation = {}
        self.addDescrForNation(LoreGroupComponent.DEFAULT, descr)
        return

    def addDescrForNation(self, nation, descr):
        if nation in self.descr_by_nation:
            LOG_ERROR((b'Lore description: {0} for nation: {1}, already exist ').format(descr, nation))
        self.descr_by_nation[nation] = descr
        return

    def getDescrForNation(self, nation):
        if nation in self.descr_by_nation:
            return self.descr_by_nation[nation]
        return self.descr_by_nation[LoreGroupComponent.DEFAULT]


class LoreComponent(object):
    __slots__ = (b'descr_by_group',)
    SECTION = b'descr_by_group'
    NATION_SECTION = b'nations'
    __DEFAULT = b'default'

    def __init__(self):
        self.descr_by_group = {}
        return

    def addDescrForGroup(self, group, descr):
        if group in self.descr_by_group:
            LOG_ERROR((b'Description: {0} for group: {1}, already exist ').format(group, descr))
        self.descr_by_group[group] = LoreGroupComponent(descr)
        return

    def addNationDescrForGroup(self, group, naiton, descr):
        self.descr_by_group[group].addDescrForNation(naiton, descr)
        return

    def getLoreDescrForGroup(self, group, nation=LoreGroupComponent.DEFAULT, isDefault=False):
        result = b''
        if group in self.descr_by_group:
            result = self.descr_by_group[group].getDescrForNation(nation)
        elif isDefault:
            result = self.descr_by_group[LoreComponent.__DEFAULT].getDescrForNation(LoreGroupComponent.DEFAULT)
        return result

    def __repr__(self):
        return (b'{}()').format(self.__class__.__name__)
