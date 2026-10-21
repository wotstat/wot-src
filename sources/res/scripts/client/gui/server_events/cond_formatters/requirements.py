import types, typing, nations
from constants import EVENT_TYPE, IGR_TYPE, IS_CHINA
from gui import makeHtmlString
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.cond_formatters import packText, packTokenProgress, getSeparatorBlock
from gui.server_events.cond_formatters.formatters import ConditionsFormatter, ConditionFormatter
from gui.server_events.conditions import GROUP_TYPE, AndGroup
from gui.server_events.formatters import TOKEN_SIZES
from gui.shared.formatters import text_styles, icons
from helpers import int2roman, dependency
from helpers.i18n import makeString as ms
from helpers.dependency import replace_none_kwargs
from shared_utils import first
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Tuple

def packTokens(tokens):
    return {b'tokens': tokens, b'isNeedShowIcon': False}


def relate(relation, value, label):
    if not isinstance(value, types.StringTypes):
        value = backport.getNiceNumberFormat(value)
    else:
        value = value
    relation = backport.text(R.strings.quests.details.requirementsRelation.dyn(relation)())
    rlabel = backport.text(R.strings.quests.details.requirements.relation(), relation=relation, value=value)
    return (u'{}{}').format(label, rlabel)


def prepareAccountConditionsGroup(conditions, event):
    group = AndGroup()
    group.add(conditions.getConditions())
    group.add(_getAdapter(event.vehicleReqs.getConditions(), event.vehicleReqs.getSuitableVehicles()))
    return group


@replace_none_kwargs(itemsCache=IItemsCache)
def _isVehicleConditionAvailable(condition, suitableVehicleIntCDs, itemsCache=None):
    for vehicleIntCD in suitableVehicleIntCDs:
        vehicle = itemsCache.items.getItemByCD(vehicleIntCD)
        if condition.isAvailable(vehicle):
            return True

    return False


def _getAdapter(condition, suitableVehicles):
    if condition.getName() == GROUP_TYPE.AND:
        return VehicleGroupAndAdapter(condition, suitableVehicles)
    if condition.getName() == GROUP_TYPE.OR:
        return VehicleGroupOrAdapter(condition, suitableVehicles)
    return VehicleConditionAdapter(condition, suitableVehicles)


class RecursiveFormatter(ConditionsFormatter):

    def __init__(self, formatters=None, gatheringFormatters=None):
        super(RecursiveFormatter, self).__init__(formatters)
        self.__gatheringFormatters = gatheringFormatters or {}
        return

    def createGatheringFormatters(self):
        result = {}
        for key, cls in self.__gatheringFormatters.iteritems():
            result[key] = cls()

        return result

    def _packCondition(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _getFormattedField(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _packConditions(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return


class VehicleConditionAdapter(object):

    def __init__(self, condition, suitableVehicles):
        self._condition = condition
        self._suitableVehicles = suitableVehicles
        return

    def isAvailable(self):
        return _isVehicleConditionAvailable(self._condition, self._suitableVehicles)

    def getName(self):
        return self._condition.getName()

    def getValue(self):
        return self._condition.getValue()


class VehicleGroupAdapter(VehicleConditionAdapter):

    def isEmpty(self):
        return not self._condition.items

    def getSortedItems(self):
        return [_getAdapter(condition, self._suitableVehicles) for condition in self._condition.getSortedItems()]


class VehicleGroupOrAdapter(VehicleGroupAdapter):

    def isAvailable(self, *args, **kwargs):
        for cond in self._condition.items:
            if _isVehicleConditionAvailable(cond, self._suitableVehicles):
                return True

        return False


class VehicleGroupAndAdapter(VehicleGroupAdapter):

    def isAvailable(self, *args, **kwargs):
        res = True
        for cond in self._condition.items:
            res = _isVehicleConditionAvailable(cond, self._suitableVehicles)
            if not res:
                return res

        return res


class AccountRequirementsFormatter(ConditionsFormatter):

    def __init__(self, formatters=None):
        super(AccountRequirementsFormatter, self).__init__(formatters or {b'and': (RecursiveGroupFormatter()), 
           b'or': (RecursiveGroupFormatter()), 
           b'single': (SingleGroupFormatter())})
        return

    def format(self, conditions, event):
        if event.isGuiDisabled():
            return {}
        group = prepareAccountConditionsGroup(conditions, event)
        formatter = self._getGroupFormatter(group)
        requirements, passed, total = formatter.format(group, event)
        conclusion = formatter.conclusion(group, event, requirements, passed, total)
        if not requirements and not conclusion:
            return {}
        return {b'header': conclusion, 
           b'requirements': (self._processRequirements(requirements))}

    @staticmethod
    def _processRequirements(requirements):
        for item in requirements:
            for key in (b'isAvailable', b'isSeparator'):
                if key in item:
                    del item[key]

        return requirements

    def _getGroupFormatter(self, group):
        if len(group.items) == 1 and first(group.items).getName() not in (b'token', b'and', b'or'):
            return self.getConditionFormatter(b'single')
        return self.getConditionFormatter(group.getName())

    def _packCondition(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _getFormattedField(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _packConditions(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return


class TQAccountRequirementsFormatter(AccountRequirementsFormatter):

    def __init__(self):
        super(TQAccountRequirementsFormatter, self).__init__({b'and': (TQRecursiveGroupFormatter()), 
           b'or': (TQRecursiveGroupFormatter()), 
           b'single': (SingleGroupFormatter())})
        return

    def _getGroupFormatter(self, group):
        return self.getConditionFormatter(group.getName())


class SingleGroupFormatter(ConditionsFormatter):

    def __init__(self):
        super(SingleGroupFormatter, self).__init__({b'premiumAccount': (PremiumAccountFormatter()), 
           b'premiumPlusAccount': (PremiumPlusAccountFormatter()), 
           b'wotPlus': (WotPlusFormatter()), 
           b'inClan': (InClanRequirementFormatter()), 
           b'igrType': (IgrTypeRequirementFormatter()), 
           b'GR': (GlobalRatingRequirementFormatter()), 
           b'accountDossier': (AccountDossierRequirementFormatter()), 
           b'vehiclesUnlocked': (VehiclesRequirementFormatter()), 
           b'vehiclesOwned': (VehiclesRequirementFormatter()), 
           b'hasReceivedMultipliedXP': (HasReceivedMultipliedXPFormatter())})
        return

    def conclusion(self, group, event, requirements, passed, total):
        if group.isAvailable():
            icon = b''
            style = text_styles.standard
            header = b'#quests:missionDetails/requirements/header/available'
        else:
            icon = (
             icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_MARKER_BLOCKED, width=14, height=14, vSpace=-1, hSpace=-2),)
            style = text_styles.error
            header = b'#quests:missionDetails/requirements/header/unavailable'
        result = []
        for condition in group.getSortedItems():
            fmt = self.getConditionFormatter(condition.getName())
            if fmt:
                branch = fmt.format(condition, event, self._styler)
                result.extend(branch)

        result = (branch.get(b'text') for branch in result)
        reason = text_styles.concatStylesToMultiLine(*result)
        return text_styles.concatStylesWithSpace(icon, style(header), reason)

    def format(self, group, event):
        passed = 0
        for condition in group.getSortedItems():
            if condition.isAvailable():
                passed += 1

        return ([], passed, len(group.items))

    @staticmethod
    def _styler(isRequirementMet):
        if isRequirementMet:
            return text_styles.standard
        return text_styles.main

    def _packCondition(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _getFormattedField(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _packConditions(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return


class RecursiveGroupFormatter(RecursiveFormatter):

    def __init__(self, formatters=None):
        super(RecursiveGroupFormatter, self).__init__(formatters=formatters or {b'premiumAccount': (PremiumAccountFormatter()), 
           b'premiumPlusAccount': (PremiumPlusAccountFormatter()), 
           b'wotPlus': (WotPlusFormatter()), 
           b'inClan': (InClanRequirementFormatter()), 
           b'igrType': (IgrTypeRequirementFormatter()), 
           b'GR': (GlobalRatingRequirementFormatter()), 
           b'accountDossier': (AccountDossierRequirementFormatter()), 
           b'vehiclesUnlocked': (VehiclesRequirementFormatter()), 
           b'vehiclesOwned': (VehiclesRequirementFormatter()), 
           b'hasReceivedMultipliedXP': (HasReceivedMultipliedXPFormatter())}, gatheringFormatters={b'token': TokenGatheringRequirementFormatter})
        return

    def conclusion(self, group, event, requirements, passed, total):
        if not total:
            return b''
        if group.isAvailable():
            icon = b''
            headerStyle = text_styles.standard
            reasonStyle = text_styles.standard
            header = b'#quests:missionDetails/requirements/header/available'
            reason = b'#quests:missionDetails/requirements/conclusion/available'
            count = total
        else:
            icon = (
             icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_MARKER_BLOCKED, width=14, height=14, vSpace=-1, hSpace=-2),)
            headerStyle = text_styles.error
            reasonStyle = text_styles.main
            header = b'#quests:missionDetails/requirements/header/unavailable'
            if len(requirements) == 1:
                reason = requirements[0][b'text']
            else:
                reason = b'#quests:missionDetails/requirements/conclusion/unavailable'
            count = total - passed
        return text_styles.concatStylesWithSpace(icon, headerStyle(header), reasonStyle(ms(reason, count=count)))

    def format(self, group, event, isNested=False, topHasOrGroup=False):
        result = []
        total, passed = (0, 0)
        separator = getSeparatorBlock(group.getName())
        gatheringFmts = self.createGatheringFormatters()
        for condition in group.getSortedItems():
            conditionName = condition.getName()
            if conditionName in GROUP_TYPE.ALL():
                isInOrGroup = topHasOrGroup or conditionName == GROUP_TYPE.OR
                branch, bpassed, btotal = self.format(condition, event, isNested=True, topHasOrGroup=isInOrGroup)
                total += btotal
                passed += bpassed
                if branch and isInOrGroup and not isNested:
                    branch[0].update(icon=self._getIcon(condition.isAvailable()))
                result.extend(branch)
                if separator:
                    result.append(separator)
            else:
                if conditionName in gatheringFmts:
                    fmt = gatheringFmts.get(conditionName)
                    fmt.gather(condition, event)
                    branch = []
                elif self.hasFormatter(conditionName):
                    fmt = self.getConditionFormatter(conditionName)
                    branch = fmt.format(condition, event, self._styler)
                else:
                    branch = []
                if branch:
                    total += 1
                    if condition.isAvailable():
                        passed += 1
                if branch:
                    isAvailable = condition.isAvailable()
                    result.extend(self._processNonGroupConidtions(branch, isNested, isAvailable, separator, topHasOrGroup))

        for fmt in gatheringFmts.itervalues():
            branch = fmt.format(self._styler)
            if branch:
                total += 1
                isAvailable = fmt.isAvailable()
                result.extend(self._processNonGroupConidtions(branch, isNested, isAvailable, separator, topHasOrGroup))

        if result and result[-1].get(b'isSeparator'):
            result.pop()
        return (result, passed, total)

    @classmethod
    def _processNonGroupConidtions(cls, branch, isNested, isAvailable, separator, isInOrGroup):
        formattedBranch = []
        for item in branch:
            if not isNested or not isInOrGroup:
                item.update(icon=cls._getIcon(isAvailable))
            formattedBranch.append(item)

        if separator:
            formattedBranch.append(separator)
        return formattedBranch

    @staticmethod
    def _getIcon(isAvailable):
        if isAvailable:
            return RES_ICONS.MAPS_ICONS_LIBRARY_OKICON
        return RES_ICONS.MAPS_ICONS_LIBRARY_CYBERSPORT_NOTAVAILABLEICON

    @staticmethod
    def _styler(isRequirementMet):
        if isRequirementMet:
            return text_styles.success
        return text_styles.main

    @staticmethod
    def _iconize(isAvailable, isNested, branch):
        if isAvailable:
            icon = RES_ICONS.MAPS_ICONS_LIBRARY_OKICON
        else:
            icon = RES_ICONS.MAPS_ICONS_LIBRARY_CYBERSPORT_NOTAVAILABLEICON
        if not isNested and branch:
            branch[0].update(icon=icon)
        return


class TQRecursiveGroupFormatter(RecursiveGroupFormatter):

    def __init__(self):
        super(TQRecursiveGroupFormatter, self).__init__(formatters={b'premiumAccount': (PremiumAccountFormatter()), 
           b'premiumPlusAccount': (PremiumPlusAccountFormatter()), 
           b'wotPlus': (WotPlusFormatter()), 
           b'inClan': (InClanRequirementFormatter()), 
           b'igrType': (IgrTypeRequirementFormatter()), 
           b'GR': (GlobalRatingRequirementFormatter()), 
           b'accountDossier': (AccountDossierRequirementFormatter()), 
           b'vehiclesUnlocked': (VehiclesRequirementFormatter()), 
           b'vehiclesOwned': (VehiclesRequirementFormatter()), 
           b'hasReceivedMultipliedXP': (HasReceivedMultipliedXPFormatter())})
        return


class PremiumAccountFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        if condition.isPremiumNeeded():
            labelKey = b'premiumAccount'
        else:
            labelKey = b'notPremiumAccount'
        label = backport.text(R.strings.quests.details.requirements.dyn(labelKey)())
        style = styler(condition.isAvailable())
        return [
         packText(style(label))]


class PremiumPlusAccountFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        if condition.isPremiumNeeded():
            labelKey = b'premiumPlusAccount'
        else:
            labelKey = b'notPremiumAccount'
        label = backport.text(R.strings.quests.details.requirements.dyn(labelKey)())
        style = styler(condition.isAvailable())
        return [
         packText(style(label))]


class WotPlusFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        labelKey = b'wotPlus' if condition.isWotPlusNeeded() else b'withoutWotPlus'
        label = backport.text(R.strings.quests.details.requirements.dyn(labelKey)())
        return [
         packText(style(label))]


class InClanRequirementFormatter(ConditionFormatter):
    itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def format(cls, condition, event, styler):
        labelKey = None
        if condition.getClanIds() is None:
            if condition.isNegative():
                labelKey = b'notInAnyClan'
            else:
                labelKey = b'inAnyClan'
        else:
            clanDBID = cls.itemsCache.items.stats.clanDBID
            if not condition.isNegative():
                if clanDBID:
                    if clanDBID in condition.getClanIds():
                        labelKey = b'forCurrentClan'
                    else:
                        labelKey = b'notForCurrentClan'
                else:
                    labelKey = b'inClan'
            elif clanDBID and clanDBID in condition.getClanIds():
                labelKey = b'notForCurrentClan'
        if labelKey is not None:
            label = backport.text(R.strings.quests.details.requirements.dyn(labelKey)())
            style = styler(condition.isAvailable())
            return [
             packText(style(label))]
        else:
            return []


class IgrTypeRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        igrTypes = condition.getIgrTypes()
        if IS_CHINA:
            key = b'igr'
        elif igrTypes.issubset({IGR_TYPE.BASE}):
            key = b'igrBasic'
        elif igrTypes.issubset({IGR_TYPE.PREMIUM}):
            key = b'igrPremium'
        else:
            key = b'igr'
        label = backport.text(R.strings.quests.details.requirements.dyn(key)())
        style = styler(condition.isAvailable())
        return [
         packText(makeHtmlString(b'html_templates:lobby/quests', b'playInIgr', {b'label': (style(label))}))]


class GlobalRatingRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        relation, value = condition.relation, condition.relationValue
        label = backport.text(R.strings.quests.details.requirements.globalRating())
        label = relate(relation, value, label)
        style = styler(condition.isAvailable())
        return [
         packText(style(label))]


class VehiclesRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        labelKey = (b'#quests:details/requirements/{}').format(condition.getName())
        result = []
        if condition.isAnyVehicleAcceptable():
            label = ms((b'{}/all').format(labelKey))
            result.append(packText(style(label)))
        elif b'types' not in condition.data:
            _, fnations, flevels, fclasses, _ = condition.parseFilters()
            keys, kwargs = [], {}
            if fnations:
                keys.append(b'nation')
                names = [nations.NAMES[nationId] for nationId in fnations]
                names = [ms((b'#menu:nations/{}').format(name)) for name in names]
                kwargs[b'nation'] = (b', ').join(names)
            if fclasses:
                keys.append(b'type')
                names = [ms((b'#menu:classes/{}').format(name)) for name in fclasses]
                kwargs[b'type'] = (b', ').join(names)
            if flevels:
                keys.append(b'level')
                names = [int2roman(lvl) for lvl in flevels]
                kwargs[b'level'] = (b', ').join(names)
            labelKey = (b'{}/{}').format(labelKey, (b'_').join(keys))
            if condition.relationValue is None and condition.isNegative():
                labelKey = (b'{}/not').format(labelKey)
            label = ms(labelKey, **kwargs)
            label = relate(condition.relation, condition.relationValue, label)
            result.append(packText(style(label)))
        elif condition.isNegative():
            labelKey = (b'{}/not').format(labelKey)
        label = ms(labelKey)
        names = [vehicle.userName for vehicle in condition.getVehiclesList()]
        result.append(packText(style((b'{}: {}').format(label, (b', ').join(names)))))
        return result


class HasReceivedMultipliedXPFormatter(ConditionFormatter):
    itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        xpKey = b'receivedMultXp' if condition.getValue() else b'notReceivedMultXp'
        key = R.strings.quests.details.requirements.vehicle.dyn(xpKey)()
        label = backport.text(key, mult=cls.itemsCache.items.shop.dailyXPFactor)
        return [
         packText(style(label))]


class AccountDossierRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        if condition.average:
            titleKey = R.strings.quests.details.requirements.dossierAvgValue()
        else:
            titleKey = R.strings.quests.details.requirements.dossierValue()
        block, record = condition.recordName
        battleMode = cls._dossierBlock2BattleMode(block)
        labelKey = R.strings.quests.details.dossier.dyn(battleMode).dyn(record)()
        label = backport.text(titleKey, label=backport.text(labelKey))
        label = relate(condition.relation, condition.relationValue, label)
        return [
         packText(style(label))]

    @classmethod
    def _dossierBlock2BattleMode(cls, block):
        if block in (b'a15x15', b'a15x15_2'):
            return b'random'
        if block in (b'company', b'company2'):
            return b'company'
        if block in (b'clan', b'clan2'):
            return b'clan'
        if block == b'a7x7':
            return b'team'
        if block == b'rated7x7':
            return b'ladder'
        if block == b'historical':
            return b'historical'
        if block == b'achievements':
            return b'achievements'
        return b'random'


class TokenGatheringRequirementFormatter(ConditionFormatter):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        self._tokens = []
        self._isAvailable = True
        return

    def format(self, styler):
        style = styler(self._isAvailable)
        result = []
        if self._tokens:
            result = [packText(style(b'#quests:details/requirements/token')),
             packTokens(self._tokens)]
        return result

    def gather(self, condition, event):
        if not condition.isDisplayable():
            return
        if event.getType() not in EVENT_TYPE.LIKE_BATTLE_QUESTS + EVENT_TYPE.LIKE_TOKEN_QUESTS:
            return
        needCount = condition.getNeededCount()
        gotCount = condition.getReceivedCount()
        image = condition.getImage(TOKEN_SIZES.BIG)
        self._tokens.append(packTokenProgress(condition.getID(), event.getID(), b'', image, gotCount, needCount, isBigSize=True))
        self._isAvailable = self._isAvailable and condition.isAvailable()
        return

    def isAvailable(self):
        return self._isAvailable
