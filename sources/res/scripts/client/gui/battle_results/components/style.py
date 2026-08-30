from collections import namedtuple
from constants import IGR_TYPE
from gui import makeHtmlString
from gui.Scaleform import settings
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS
from gui.battle_results.components import base
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
from helpers import i18n
WIDE_STAT_ROW = b'wideLine'
NORMAL_STAT_ROW = b'normalLine'
SMALL_STAT_LINE = b'smallLineUI'
LINE_BRAKE_STR = b'<br/>'
_STATS_INFOTIP_HEADER_FORMAT = b'#battle_results:team/stats/infotip_{0}/header'
_VEHICLE_STATE_PREFIX = b'{0} ('
_VEHICLE_STATE_SUFFIX = b')'
_DIFF_FORMAT = b'+ {}'
_LINE_FEED = b'\n'

def getUnknownPlayerName(isEnemy=False):
    if isEnemy:
        return i18n.makeString(BATTLE_RESULTS.PLAYERS_ENEMY_UNKNOWN)
    return i18n.makeString(BATTLE_RESULTS.PLAYERS_TEAMMATE_UNKNOWN)


I18nDeathReason = namedtuple(b'I18nDeathReason', b'i18nString prefix suffix')

def makeI18nDeathReason(deathReason):
    state = backport.text(R.strings.battle_results.common.vehicleState.dyn((b'dead{}').format(deathReason), R.invalid)())
    return I18nDeathReason(state, _VEHICLE_STATE_PREFIX.format(state), _VEHICLE_STATE_SUFFIX)


def markValueAsError(value):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'negative_value', {b'value': value})


def markValueAsEmpty(value):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'empty_stat_value', {b'value': value})


def makeMarksOfMasteryText(marksOfMastery, totalVehicles):
    return makeHtmlString(b'html_templates:lobby/profileStatistics', b'marksOfMasteryText', {b'marksOfMastery': marksOfMastery, b'totalVehicles': totalVehicles})


def getIntegralFormatIfNoEmpty(value):
    if value:
        return backport.getIntegralFormat(value)
    return markValueAsEmpty(value)


def getFractionalFormatIfNoEmpty(value):
    if value:
        return backport.getFractionalFormat(value)
    return markValueAsEmpty(value)


_SPLASH_CHAR_NO_EMPTY_STAT = b'/'
_SPLASH_CHAR_EMPTY_STAT = markValueAsEmpty(_SPLASH_CHAR_NO_EMPTY_STAT)

def getTooltipParamsStyle(paramKey=None):
    if paramKey is None:
        paramKey = BATTLE_RESULTS.COMMON_TOOLTIP_PARAMS_VAL
    return makeHtmlString(b'html_templates:lobby/battle_results', b'tooltip_params_style', {b'text': (i18n.makeString(paramKey))})


def _makeModuleTooltipLabel(module, suffix):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'tooltip_crit_label', {b'image': ((b'{0}{1}').format(module, suffix)), 
       b'value': (backport.text(R.strings.item_types.dyn(module).name()))})


def makeCriticalModuleTooltipLabel(module):
    return _makeModuleTooltipLabel(module, b'Critical')


def makeDestroyedModuleTooltipLabel(module):
    return _makeModuleTooltipLabel(module, b'Destroyed')


def makeTankmenTooltipLabel(role):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'tooltip_crit_label', {b'image': ((b'{0}Destroyed').format(role)), 
       b'value': (backport.text(R.strings.item_types.tankman.roles.dyn(role)()))})


class StatRow(base.StatsItem):
    __slots__ = (b'text', b'label', b'lineType', b'column1', b'column2', b'column3', b'column4')

    def __init__(self, text, label, lineType, column1=_LINE_FEED, column2=_LINE_FEED, column3=_LINE_FEED, column4=_LINE_FEED):
        super(StatRow, self).__init__(b'')
        self.text = text
        self.label = label
        self.lineType = lineType
        self.column1 = column1
        self.column2 = column2
        self.column3 = column3
        self.column4 = column4
        return

    def setRecord(self, record, reusable):
        return

    def getVO(self):
        return {b'label': (self.label), 
           b'labelStripped': (self.text), 
           b'col1': (self.column1), 
           b'col2': (self.column2), 
           b'col3': (self.column3), 
           b'col4': (self.column4), 
           b'lineType': (self.lineType)}


class EmptyStatRow(StatRow):
    __slots__ = ()

    def __init__(self):
        super(EmptyStatRow, self).__init__(_LINE_FEED, _LINE_FEED, None)
        return


def makeStatRow(label=b'', labelArgs=None, column1=None, column2=None, column3=None, column4=None, htmlKey=b''):
    if column2 is not None:
        lineType = WIDE_STAT_ROW
    elif not any((column2, column3, column4)):
        lineType = None
    else:
        lineType = NORMAL_STAT_ROW
    if label:
        if labelArgs:
            i18nText = i18n.makeString(BATTLE_RESULTS.getDetailsCalculation(statName=label), **labelArgs)
        else:
            i18nText = i18n.makeString(BATTLE_RESULTS.getDetailsCalculation(statName=label))
        if htmlKey:
            label = makeHtmlString(b'html_templates:lobby/battle_results', htmlKey, {b'value': i18nText})
        else:
            label = i18nText
    else:
        label = makeHtmlString(b'html_templates:lobby/battle_results', htmlKey)
        import re
        i18nText = re.sub(b'<[^<]+?>', b'', label)
    return {b'label': label, 
       b'labelStripped': i18nText, 
       b'col1': (column1 if column1 is not None else _LINE_FEED), 
       b'col2': (column2 if column2 is not None else _LINE_FEED), 
       b'col3': (column3 if column3 is not None else _LINE_FEED), 
       b'col4': (column4 if column4 is not None else _LINE_FEED), 
       b'lineType': lineType}


def makeCreditsLabel(value, canBeFaded=False, isDiff=False, useBigIcon=False, forceFade=False):
    formatted = backport.getGoldFormat(int(round(value)))
    if value < 0:
        formatted = markValueAsError(formatted)
    if isDiff:
        formatted = _DIFF_FORMAT.format(formatted)
    if useBigIcon:
        template = b'credits_label'
    elif canBeFaded and (not value or forceFade):
        template = b'credits_small_inactive_label'
    else:
        template = b'credits_small_label'
    return makeHtmlString(b'html_templates:lobby/battle_results', template, {b'value': formatted})


def makeGoldLabel(value, canBeFaded=False, isDiff=False, forceFade=False):
    formatted = backport.getGoldFormat(value)
    if isDiff:
        formatted = _DIFF_FORMAT.format(formatted)
    if canBeFaded and (not value or forceFade):
        template = b'gold_small_inactive_label'
    else:
        template = b'gold_small_label'
    return makeHtmlString(b'html_templates:lobby/battle_results', template, {b'value': formatted})


def makeXpLabel(value, canBeFaded=False, isDiff=False, useBigIcon=False, forceFade=False):
    formatted = backport.getIntegralFormat(int(value))
    if value < 0:
        formatted = markValueAsError(formatted)
    if isDiff:
        formatted = _DIFF_FORMAT.format(formatted)
    if useBigIcon:
        template = b'xp_label'
    elif canBeFaded and (not value or forceFade):
        template = b'xp_small_inactive_label'
    else:
        template = b'xp_small_label'
    return makeHtmlString(b'html_templates:lobby/battle_results', template, {b'value': formatted})


def makeFreeXpLabel(value, canBeFaded=False, forceFade=False):
    if canBeFaded and (not value or forceFade):
        template = b'free_xp_small_inactive_label'
    else:
        template = b'free_xp_small_label'
    return makeHtmlString(b'html_templates:lobby/battle_results', template, {b'value': (backport.getIntegralFormat(int(value)))})


def makeCrystalLabel(value):
    formatted = backport.getIntegralFormat(int(value))
    if value < 0:
        formatted = markValueAsError(formatted)
    return makeHtmlString(b'html_templates:lobby/battle_results', b'crystal_small_label', {b'value': formatted})


def makePercentLabel(value):
    formatted = backport.getGoldFormat(int(value))
    template = b'percent'
    if value < 0:
        formatted = markValueAsError(formatted)
        template = b'negative_percent'
    return makeHtmlString(b'html_templates:lobby/battle_results', template, {b'value': formatted})


def makeIGRIcon(igrType):
    if igrType == IGR_TYPE.PREMIUM:
        iconName = b'premium'
    else:
        iconName = b'basic'
    return makeHtmlString(b'html_templates:igr/iconSmall', iconName)


def makeIGRBonusLabel(igrIcon):
    return i18n.makeString(BATTLE_RESULTS.DETAILS_CALCULATIONS_IGRBONUS, igrIcon=igrIcon)


def makeIGRBonusValue(factor):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'igr_bonus', {b'value': (backport.getNiceNumberFormat(factor))})


def makeMultiXPFactorValue(value, useFreeXPStyle=False):
    if value > 0:
        if useFreeXPStyle:
            template = b'multy_xp_small_multiplier_free'
        else:
            template = b'multy_xp_small_multiplier'
    elif useFreeXPStyle:
        template = b'multy_xp_small_label_free'
    else:
        template = b'multy_xp_small_label'
    return makeHtmlString(b'html_templates:lobby/battle_results', template, {b'value': (int(value))})


def makeAOGASFactorValue(value):
    formatted = (b'').join((
     i18n.makeString(BATTLE_RESULTS.COMMON_XPMULTIPLIERSIGN),
     backport.getFractionalFormat(value)))
    formatted = markValueAsError(formatted)
    return formatted


def makeMultiLineHtmlString(seq):
    return LINE_BRAKE_STR.join(seq)


def makeStatValue(field, value):
    tooltip = b''
    tooltipHeader = _STATS_INFOTIP_HEADER_FORMAT.format(field)
    if i18n.doesTextExist(tooltipHeader):
        tooltip = makeTooltip(header=i18n.makeString(tooltipHeader), body=i18n.makeString(BATTLE_RESULTS.getTeamStatsInfotipBody(statName=field)))
    return {b'label': (i18n.makeString(BATTLE_RESULTS.getTeamStatsLabel(statName=field))), 
       b'value': value, 
       b'infoTooltip': tooltip}


def makeTimeStatsVO(field, value):
    return {b'label': (i18n.makeString(BATTLE_RESULTS.getDetailsTimeLbl(statName=field))), 
       b'value': value}


def makeBadgeIcon(badge):
    return settings.getBadgeIconPath(settings.BADGES_ICONS.X24, badge)


def makeRankedResultsTitle(title):
    return text_styles.promoTitle(title)


def makeRankedPointValue(pointsValue):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'xp_small_label', {b'value': (text_styles.playerOnline(pointsValue))})


def makeRankedPointHugeValue(pointsValue):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'xp_small_label', {b'value': (text_styles.hightlight(pointsValue))})


def markVehicleAsTeamKiller(vehicle):
    vehicle.vehicleStatePrefix = vehicle.vehicleStatePrefix[:-1] + makeTeamKillerText(vehicle.vehicleStatePrefix[-1])
    vehicle.vehicleStateSuffix = makeTeamKillerText(vehicle.vehicleStateSuffix)
    return


def makeTeamKillerText(text):
    return makeHtmlString(b'html_templates:lobby/battle_results', b'team_killer', {b'text': text})


def makeRankedNickNameValue(name):
    return text_styles.playerOnline(name)


def makeRankedNickNameHugeValue(name):
    return text_styles.hightlight(name)


class GroupMiddleLabelBlock(base.DirectStatsItem):

    def __init__(self, label):
        super(GroupMiddleLabelBlock, self).__init__(b'', {b'groupLabel': (text_styles.main(label))})
        return


class _SlashedValueItem(base.StatsItem):

    def _convert(self, value, reusable):
        if value:
            converted = str(value)
            isEmpty = False
        else:
            converted = markValueAsEmpty(value)
            isEmpty = True
        return (isEmpty, converted)


class _RedSlashedValueItem(base.StatsItem):

    def _convert(self, value, reusable):
        isEmpty = value <= 0
        converted = str(value)
        return (isEmpty, converted)


class _RedSlashedValuesMeta(base.ListMeta):

    def registerComponent(self, component):
        super(_RedSlashedValuesMeta, self).registerComponent(component)
        if not isinstance(component, _RedSlashedValueItem):
            raise base.StatsComponentError(b'Block can be added _RedSlashedValueItem only')
        return

    def generateVO(self, components):
        if not self._registered:
            return _SPLASH_CHAR_EMPTY_STAT
        result = []
        noStats = True
        for component in components:
            isEmpty, value = component.getVO()
            noStats = noStats and isEmpty
            result.append(value)

        markValue = markValueAsEmpty if noStats else markValueAsError
        return markValue(_SPLASH_CHAR_NO_EMPTY_STAT.join(result))


class _SlashedValuesMeta(base.ListMeta):

    def registerComponent(self, component):
        super(_SlashedValuesMeta, self).registerComponent(component)
        if not isinstance(component, _SlashedValueItem):
            raise base.StatsComponentError(b'Block can be added SlashedValuesItem only')
        return

    def generateVO(self, components):
        if not self._registered:
            return _SPLASH_CHAR_EMPTY_STAT
        result = []
        noStats = True
        for component in components:
            isEmpty, value = component.getVO()
            noStats = noStats and isEmpty
            result.append(value)

        if noStats:
            slash = _SPLASH_CHAR_EMPTY_STAT
        else:
            slash = _SPLASH_CHAR_NO_EMPTY_STAT
        return slash.join(result)


class TwoItemsWithSlashBlock(base.StatsBlock):

    def __init__(self, itemClass, meta=None, field=b''):
        super(TwoItemsWithSlashBlock, self).__init__(meta=meta, field=field)
        self._itemClass = itemClass
        self.addComponent(0, itemClass(b''))
        self.addComponent(1, itemClass(b''))
        return

    def setRecord(self, result, reusable):
        for index, value in enumerate(result):
            self.getComponent(index).setRecord(value, reusable)

        return

    def clone(self, *exclude):
        return TwoItemsWithSlashBlock(self._itemClass, meta=self._meta, field=self._field)


class SlashedValuesBlock(TwoItemsWithSlashBlock):

    def __init__(self, field=b''):
        super(SlashedValuesBlock, self).__init__(_SlashedValueItem, meta=_SlashedValuesMeta(), field=field)
        return


class RedSlashedValuesBlock(TwoItemsWithSlashBlock):

    def __init__(self, field=b''):
        super(RedSlashedValuesBlock, self).__init__(_RedSlashedValueItem, meta=_RedSlashedValuesMeta(), field=field)
        return


class MetersToKillometersItem(base.StatsItem):

    def _convert(self, value, reusable):
        converted = backport.getFractionalFormat(value / 1000.0)
        if not value:
            converted = markValueAsEmpty(converted)
        return converted


class XpStatsItem(base.StatsItem):

    def _convert(self, value, reusable):
        converted = makeXpLabel(value)
        if not value:
            converted = markValueAsEmpty(converted)
        return converted
