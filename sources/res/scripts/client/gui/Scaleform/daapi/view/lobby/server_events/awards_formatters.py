from __future__ import absolute_import
from future.utils import viewvalues
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import NewStyleBonusComposer
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.auxiliary.rewards_helper import NEW_STYLE_FORMATTED_BONUSES
from gui.server_events import formatters
from gui.server_events.awards_formatters import AWARDS_SIZES, AwardsPacker, QuestsBonusComposer, getPostBattleAwardsPacker
from gui.server_events.bonuses import BlueprintsBonusSubtypes, formatBlueprint
from gui.battle_pass.battle_pass_bonuses_helper import BonusesHelper
from gui.shared.gui_items.crew_skin import localizedFullName as localizeSkinName
from nations import NAMES
SIMPLE_BONUSES_MAX_ITEMS = 5
_DISPLAYED_AWARDS_COUNT = 2
_END_LINE_SEPARATOR = b','
_EMPTY_STRING = b''

class OldStyleBonusFormatter(object):

    def __init__(self):
        self._result = []
        return

    def accumulateBonuses(self, bonus):
        self._result.append(bonus)
        return

    def extractFormattedBonuses(self, addLineSeparator=False):
        result = self._result[:]
        self._result = []
        return result

    @classmethod
    def getOrder(cls):
        return 0


class DossierFormatter(OldStyleBonusFormatter):

    @classmethod
    def getOrder(cls):
        return 1

    def accumulateBonuses(self, bonus):
        for achieve in bonus.getAchievements():
            self._result.append(formatters.packAchieveElementByItem(achieve))

        for badge in bonus.getBadges():
            self._result.append(formatters.packBadgeElementByItem(badge))

        return


class CustomizationsFormatter(OldStyleBonusFormatter):

    @classmethod
    def getOrder(cls):
        return 2

    def accumulateBonuses(self, bonus):
        customizationsList = bonus.getList()
        if customizationsList:
            self._result.append(formatters.packCustomizations(customizationsList))
        return


class VehiclesFormatter(OldStyleBonusFormatter):

    def __init__(self, event):
        super(VehiclesFormatter, self).__init__()
        self.__eventID = str(event.getID())
        return

    @classmethod
    def getOrder(cls):
        return 3

    def accumulateBonuses(self, bonus, event=None):
        formattedList = bonus.formattedList()
        if formattedList:
            vehiclesLbl, _ = _joinUpToMax(formattedList)
            self._result.append(formatters.packVehiclesBonusBlock(vehiclesLbl, self.__eventID))
        return


class CrewBookFormatter(OldStyleBonusFormatter):

    @classmethod
    def getOrder(cls):
        return 4

    def accumulateBonuses(self, bonus):
        result = []
        for book, count in sorted(bonus.getItems()):
            if book is None or not count:
                continue
            result.append(self._formatBook(book, count))

        if result:
            self._result.append(formatters.packSimpleBonusesBlock(result))
        return

    @classmethod
    def _formatBook(cls, book, count):
        return backport.text(R.strings.quests.bonuses.items.name(), name=book.userName, count=count)


class CrewSkinFormatter(OldStyleBonusFormatter):

    @classmethod
    def getOrder(cls):
        return 5

    def accumulateBonuses(self, bonus):
        result = []
        for skin, count, _, _ in sorted(bonus.getItems()):
            if skin is None or not count:
                continue
            result.append(self._formatCrewSkin(skin, count))

        if result:
            self._result.append(formatters.packSimpleBonusesBlock(result))
        return

    @classmethod
    def _formatCrewSkin(cls, skin, count):
        return backport.text(R.strings.quests.bonuses.items.name(), name=localizeSkinName(skin), count=count)


class BlueprintsFormatter(OldStyleBonusFormatter):
    _ORDER = [
     BlueprintsBonusSubtypes.FINAL_FRAGMENT,
     BlueprintsBonusSubtypes.UNIVERSAL_FRAGMENT,
     BlueprintsBonusSubtypes.NATION_FRAGMENT,
     BlueprintsBonusSubtypes.VEHICLE_FRAGMENT,
     BlueprintsBonusSubtypes.RANDOM_FRAGMENT,
     BlueprintsBonusSubtypes.RANDOM_NATIONAL_FRAGMENT]

    def __init__(self):
        super(BlueprintsFormatter, self).__init__()
        self._groupedFragments = {}
        return

    @classmethod
    def getOrder(cls):
        return 5

    def accumulateBonuses(self, bonus):
        blueprintType = bonus.getBlueprintName()
        fragments = self._groupedFragments.get(blueprintType, [])
        fragments.append(bonus)
        self._groupedFragments[blueprintType] = fragments
        return

    def extractFormattedBonuses(self, addLineSeparator=False):
        result = []
        for fragmentType in self._ORDER:
            fragments = self._groupedFragments.get(fragmentType)
            if fragments:
                fragmentLabels = []
                for fragment in fragments:
                    fragmentLabels.append(formatBlueprint(fragment, fragment.getCount()))

                result.append(formatters.packLongBonusesBlock(fragmentLabels, linesLimit=len(NAMES)))

        self._groupedFragments = {}
        return result


class BattlePassPointsFormatter(OldStyleBonusFormatter):

    def accumulateBonuses(self, bonus):
        formattedList = bonus.formattedList()
        if formattedList:
            self._result.append(formatters.packSimpleBonusesBlock(formattedList))
        return


class SimpleBonusFormatter(OldStyleBonusFormatter):

    def accumulateBonuses(self, bonus, event=None):
        formattedList = bonus.formattedList()
        if formattedList:
            self._result.extend(formattedList)
        return

    def extractFormattedBonuses(self, addLineSeparator=False):
        simpleBonusesList = super(SimpleBonusFormatter, self).extractFormattedBonuses()
        result = []
        if simpleBonusesList:
            result.append(formatters.packSimpleBonusesBlock(simpleBonusesList, endlineSymbol=_END_LINE_SEPARATOR if addLineSeparator else _EMPTY_STRING))
        return result


class TextBonusFormatter(OldStyleBonusFormatter):

    def accumulateBonuses(self, bonus, event=None):
        formattedList = BonusesHelper.getTextStrings(bonus)
        if formattedList:
            self._result.extend(formattedList)
        return

    def extractFormattedBonuses(self, addLineSeparator=False):
        simpleBonusesList = super(TextBonusFormatter, self).extractFormattedBonuses()
        result = []
        if simpleBonusesList:
            result.append(formatters.packSimpleBonusesBlock(simpleBonusesList, endlineSymbol=_END_LINE_SEPARATOR if addLineSeparator else _EMPTY_STRING))
        return result


class BattlePassStyleProgressFormatter(OldStyleBonusFormatter):

    def accumulateBonuses(self, bonus, event=None):
        formattedList = BonusesHelper.getTextStrings(bonus)
        if formattedList:
            self._result.append(formatters.packSimpleBonusesBlock(formattedList))
        return


class NewStyleBonusFormatter(OldStyleBonusFormatter):

    def __init__(self, awardsPacker=None):
        super(NewStyleBonusFormatter, self).__init__()
        self.__formatter = NewStyleBonusComposer(_DISPLAYED_AWARDS_COUNT, awardsPacker or getPostBattleAwardsPacker())
        return

    def accumulateBonuses(self, bonus, event=None):
        formattedBonuses = self.__formatter.getVisibleFormattedBonuses([], [bonus], b'big')
        if formattedBonuses:
            self._result.extend(formattedBonuses)
        return

    def extractFormattedBonuses(self, addLineSeparator=False):
        simpleBonusesList = super(NewStyleBonusFormatter, self).extractFormattedBonuses()
        result = []
        if simpleBonusesList:
            result.append(formatters.packNewStyleBonusesBlock(simpleBonusesList, endlineSymbol=_END_LINE_SEPARATOR if addLineSeparator else _EMPTY_STRING))
        return result


def getFormattersMap(event):
    return {b'dossier': (DossierFormatter()), 
       b'customizations': (CustomizationsFormatter()), 
       b'vehicles': (VehiclesFormatter(event)), 
       b'crewBooks': (CrewBookFormatter()), 
       b'blueprints': (BlueprintsFormatter()), 
       b'crewSkins': (CrewSkinFormatter()), 
       b'battlePassPoints': (BattlePassPointsFormatter())}


class OldStyleAwardsPacker(AwardsPacker):

    def __init__(self, event):
        super(OldStyleAwardsPacker, self).__init__(getFormattersMap(event))
        self.__defaultFormatter = SimpleBonusFormatter()
        self.__newStyleFormatter = NewStyleBonusFormatter()
        return

    def format(self, bonuses, event=None):
        formattedBonuses = []
        isCustomizationBonusExist = False
        for b in bonuses:
            if b.isShowInGUI():
                formatter = self._getBonusFormatter(b.getName())
                if formatter:
                    formatter.accumulateBonuses(b)
                if b.getName() == b'customizations':
                    isCustomizationBonusExist = True

        fmts = [
         self.__defaultFormatter, self.__newStyleFormatter]
        fmts.extend(sorted(viewvalues(self.getFormatters()), key=(lambda f: f.getOrder())))
        for formatter in fmts:
            formattedBonuses.extend(formatter.extractFormattedBonuses(isCustomizationBonusExist))

        return formattedBonuses

    def _getBonusFormatter(self, bonusName):
        if bonusName in NEW_STYLE_FORMATTED_BONUSES:
            return self.__newStyleFormatter
        return self.getFormatters().get(bonusName, self.__defaultFormatter)


def getTextFormattersMap():
    return {b'default': (TextBonusFormatter()), 
       b'customizations': (CustomizationsFormatter()), 
       b'styleProgressToken': (BattlePassStyleProgressFormatter())}


class BattlePassTextBonusesPacker(AwardsPacker):

    def __init__(self):
        super(BattlePassTextBonusesPacker, self).__init__(getTextFormattersMap())
        return

    def format(self, bonuses, event=None):
        formattedBonuses = []
        for b in bonuses:
            if b.isShowInGUI():
                formatter = self._getBonusFormatter(b.getName())
                if formatter:
                    formatter.accumulateBonuses(b)

        for formatter in sorted(viewvalues(self.getFormatters()), key=(lambda f: f.getOrder())):
            formattedBonuses.extend(formatter.extractFormattedBonuses())

        return formattedBonuses

    def _getBonusFormatter(self, bonusName):
        formattersMap = self.getFormatters()
        if bonusName in formattersMap:
            return formattersMap[bonusName]
        else:
            return formattersMap.get(b'default', None)


class OldStyleBonusesFormatter(QuestsBonusComposer):

    def __init__(self, event):
        super(OldStyleBonusesFormatter, self).__init__(OldStyleAwardsPacker(event))
        return

    def getFormattedBonuses(self, bonuses, size=AWARDS_SIZES.SMALL):
        return self.getPreformattedBonuses(bonuses)


def _joinUpToMax(array, separator=b', '):
    if len(array) > SIMPLE_BONUSES_MAX_ITEMS:
        label = separator.join(array[:SIMPLE_BONUSES_MAX_ITEMS]) + b'..'
        fullLabel = separator.join(array)
    else:
        label = separator.join(array)
        fullLabel = None
    return (
     label, fullLabel)
