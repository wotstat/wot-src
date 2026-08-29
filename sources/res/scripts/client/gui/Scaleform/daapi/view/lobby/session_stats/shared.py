import nations
from account_helpers.settings_core.settings_constants import SESSION_STATS
from gui import makeHtmlString
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings_controller import SessionStatsSettingsController
from gui.Scaleform.genConsts.SESSION_STATS_CONSTANTS import SESSION_STATS_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
_INFOTIP_PRECISION = 4

def toNiceNumber(value, coef=1):
    if value is None:
        return b'-'
    else:
        return backport.getNiceNumberFormat(float(value * coef))


_EFFICIENT_DATA = {(SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_WTR): {b'title': (R.strings.session_stats.propertyInfo.prop.label.wtr()), 
                                                       b'label': (R.strings.session_stats.label.wtr()), 
                                                       b'descr': (R.strings.session_stats.propertyInfo.prop.descr.wtr()), 
                                                       b'icon': (R.images.gui.maps.icons.library.wtrIcon_24()), 
                                                       b'totalValue': toNiceNumber, 
                                                       b'currentValue': (lambda data: toNiceNumber(data.wtr.value)), 
                                                       b'delta': (lambda data: data.wtr.delta), 
                                                       b'settings': (SESSION_STATS.SHOW_WTR)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_RATIO_DAMAGE): {b'title': (R.strings.session_stats.propertyInfo.prop.label.ratioDamage()), 
                                                                b'label': (R.strings.session_stats.label.damaged()), 
                                                                b'descr': (R.strings.session_stats.propertyInfo.prop.descr.ratioDamage()), 
                                                                b'icon': (R.images.gui.maps.icons.eventBoards.ratio_damage()), 
                                                                b'totalValue': (lambda stats: toNiceNumber(stats.getDamageEfficiency())), 
                                                                b'currentValue': (lambda data: processRatioValue(data.ratioDamage.value)), 
                                                                b'delta': (lambda data: data.ratioDamage.delta), 
                                                                b'settings': (SESSION_STATS.SHOW_RATIO_DAMAGE)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_RATIO_KILL): {b'title': (R.strings.session_stats.propertyInfo.prop.label.ratioKill()), 
                                                              b'label': (R.strings.session_stats.label.destroyed()), 
                                                              b'descr': (R.strings.session_stats.propertyInfo.prop.descr.ratioKill()), 
                                                              b'icon': (R.images.gui.maps.icons.eventBoards.vehicle_destroyed()), 
                                                              b'totalValue': (lambda stats: toNiceNumber(stats.getFragsEfficiency())), 
                                                              b'currentValue': (lambda data: processRatioValue(data.ratioKill.value)), 
                                                              b'delta': (lambda data: data.ratioKill.delta), 
                                                              b'settings': (SESSION_STATS.SHOW_RATIO_KILL)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_WINS): {b'title': (R.strings.session_stats.propertyInfo.prop.label.wins()), 
                                                        b'label': (R.strings.session_stats.label.victory()), 
                                                        b'descr': (R.strings.session_stats.propertyInfo.prop.descr.wins()), 
                                                        b'icon': (R.images.gui.maps.icons.statistic.wins24()), 
                                                        b'totalValue': (lambda stats: toNiceNumber(stats.getWinsCount())), 
                                                        b'currentValue': (lambda data: toNiceNumber(data.wins.value)), 
                                                        b'delta': (lambda _: 0), 
                                                        b'settings': (SESSION_STATS.SHOW_WINS)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_AVERAGE_DAMAGE): {b'title': (R.strings.session_stats.propertyInfo.prop.label.averageDamage()), 
                                                                  b'label': (R.strings.session_stats.label.averageDamage()), 
                                                                  b'descr': (R.strings.session_stats.propertyInfo.prop.descr.averageDamage()), 
                                                                  b'icon': (R.images.gui.maps.icons.statistic.avgDamage24()), 
                                                                  b'totalValue': (lambda stats: toNiceNumber(stats.getAvgDamage())), 
                                                                  b'currentValue': (lambda data: toNiceNumber(data.averageDamage.value)), 
                                                                  b'delta': (lambda data: data.averageDamage.delta), 
                                                                  b'settings': (SESSION_STATS.SHOW_AVERAGE_DAMAGE)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_HELP_DAMAGE): {b'title': (R.strings.session_stats.propertyInfo.prop.label.helpDamage()), 
                                                               b'label': (R.strings.session_stats.label.assist()), 
                                                               b'descr': (R.strings.session_stats.propertyInfo.prop.descr.helpDamage()), 
                                                               b'icon': (R.images.gui.maps.icons.statistic.assist24()), 
                                                               b'totalValue': (lambda stats: toNiceNumber(stats.getDamageAssistedEfficiencyWithStan())), 
                                                               b'currentValue': (lambda data: toNiceNumber(data.helpDamage.value)), 
                                                               b'delta': (lambda data: data.helpDamage.delta), 
                                                               b'settings': (SESSION_STATS.SHOW_HELP_DAMAGE)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_BLOCKED_DAMAGE): {b'title': (R.strings.session_stats.propertyInfo.prop.label.blockedDamage()), 
                                                                  b'label': (R.strings.session_stats.label.blockedDamage()), 
                                                                  b'descr': (R.strings.session_stats.propertyInfo.prop.descr.blockedDamage()), 
                                                                  b'icon': (R.images.gui.maps.icons.eventBoards.blocked_damage_average()), 
                                                                  b'totalValue': (lambda stats: toNiceNumber(stats.getAvgDamageBlocked())), 
                                                                  b'currentValue': (lambda data: toNiceNumber(data.blockedDamage.value)), 
                                                                  b'delta': (lambda data: data.blockedDamage.delta), 
                                                                  b'settings': (SESSION_STATS.SHOW_BLOCKED_DAMAGE)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_AVERAGE_XP): {b'title': (R.strings.session_stats.propertyInfo.prop.label.averageXp()), 
                                                              b'label': (R.strings.session_stats.label.averageXP()), 
                                                              b'descr': (R.strings.session_stats.propertyInfo.prop.descr.averageXp()), 
                                                              b'icon': (R.images.gui.maps.icons.statistic.avgExp24()), 
                                                              b'totalValue': (lambda stats: toNiceNumber(stats.getAvgXP())), 
                                                              b'currentValue': (lambda data: toNiceNumber(data.averageXp.value)), 
                                                              b'delta': (lambda data: data.averageXp.delta), 
                                                              b'settings': (SESSION_STATS.SHOW_AVERAGE_XP)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_WIN_RATE): {b'title': (R.strings.session_stats.propertyInfo.prop.label.winRate()), 
                                                            b'label': (R.strings.session_stats.label.winRate()), 
                                                            b'descr': (R.strings.session_stats.propertyInfo.prop.descr.winRate()), 
                                                            b'icon': (R.images.gui.maps.icons.statistic.wins24()), 
                                                            b'totalValue': (lambda stats: toNiceNumber(stats.getWinsEfficiency(), 100)), 
                                                            b'currentValue': (lambda data: processRatioValue(data.winRate.value)), 
                                                            b'delta': (lambda data: data.winRate.delta), 
                                                            b'settings': (SESSION_STATS.SHOW_WIN_RATE)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_AVERAGE_VEHICLE_LEVEL): {b'title': (R.strings.session_stats.propertyInfo.prop.label.averageVehiclesLevel()), 
                                                                         b'label': (R.strings.session_stats.label.averageVehiclesLevel()), 
                                                                         b'descr': (R.strings.session_stats.propertyInfo.prop.descr.averageVehiclesLevel()), 
                                                                         b'icon': (R.images.gui.maps.icons.statistic.c_2_sr_ur_tech32()), 
                                                                         b'totalValue': (lambda _: None), 
                                                                         b'currentValue': (lambda data: toNiceNumber(data.averageVehicleLevel)), 
                                                                         b'delta': (lambda _: None), 
                                                                         b'settings': (SESSION_STATS.SHOW_AVERAGE_VEHICLE_LEVEL)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_AVERAGE_FRAGS): {b'title': (R.strings.session_stats.propertyInfo.prop.label.averageFrags()), 
                                                                 b'label': (R.strings.session_stats.label.averageFrags()), 
                                                                 b'descr': (R.strings.session_stats.propertyInfo.prop.descr.averageFrags()), 
                                                                 b'icon': (R.images.gui.maps.icons.statistic.c_3_sr_kill32()), 
                                                                 b'totalValue': (lambda stats: toNiceNumber(stats.getAvgFrags())), 
                                                                 b'currentValue': (lambda data: toNiceNumber(data.averageFrags)), 
                                                                 b'delta': (lambda _: 0), 
                                                                 b'settings': (SESSION_STATS.SHOW_AVERAGE_FRAGS)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_SURVIVED_RATIO): {b'title': (R.strings.session_stats.propertyInfo.prop.label.survivedRate()), 
                                                                  b'label': (R.strings.session_stats.label.survivedRate()), 
                                                                  b'descr': (R.strings.session_stats.propertyInfo.prop.descr.survivedRate()), 
                                                                  b'icon': (R.images.gui.maps.icons.statistic.c_4_alive32()), 
                                                                  b'totalValue': (lambda stats: toNiceNumber(stats.getSurvivalEfficiency(), 100)), 
                                                                  b'currentValue': (lambda data: processRatioValue(data.survivedRatio.value)), 
                                                                  b'delta': (lambda data: data.survivedRatio.delta), 
                                                                  b'settings': (SESSION_STATS.SHOW_SURVIVED_RATE)}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_SPOTTED): {b'title': (R.strings.session_stats.propertyInfo.prop.label.spotted()), 
                                                           b'label': (R.strings.session_stats.label.spotted()), 
                                                           b'descr': (R.strings.session_stats.propertyInfo.prop.descr.spotted()), 
                                                           b'icon': (R.images.gui.maps.icons.statistic.c_5_obnaruzh32()), 
                                                           b'totalValue': (lambda stats: toNiceNumber(stats.getAvgEnemiesSpotted())), 
                                                           b'currentValue': (lambda data: toNiceNumber(data.spotted.value)), 
                                                           b'delta': (lambda data: data.spotted.delta), 
                                                           b'settings': (SESSION_STATS.SHOW_SPOTTED)}}
_VIEW_ECONOMIC_DATA_WITH_SPENIDNG = (
 SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_NET_CREDITS,
 SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_NET_CRYSTAL)
_VIEW_ECONOMIC_DATA_WITHOUT_SPENIDNG = (
 SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_INCOME_CREDITS,
 SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_INCOME_CRYSTAL,
 SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_XP,
 SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_FREE_XP)
_ECONOMIC_DATA = {(SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_NET_CREDITS): {b'label': (R.strings.session_stats.label.totalCredits()), 
                                                               b'tooltip': (lambda _: b''), 
                                                               b'detail': (lambda data: data.creditsDetails), 
                                                               b'value': (lambda data: toIntegral(data.netCredits)), 
                                                               b'bigIcon': (R.images.gui.maps.icons.library.creditsIcon_23x22()), 
                                                               b'smallIcon': (R.images.gui.maps.icons.library.CreditsIcon_2())}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_NET_CRYSTAL): {b'label': (R.strings.session_stats.label.totalCrystal()), 
                                                               b'tooltip': (lambda _: b''), 
                                                               b'detail': (lambda data: data.crystalDetails), 
                                                               b'value': (lambda data: toIntegral(data.netCrystal)), 
                                                               b'bigIcon': (R.images.gui.maps.icons.library.crystal_23x22()), 
                                                               b'smallIcon': (R.images.gui.maps.icons.library.crystal_16x16())}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_INCOME_CREDITS): {b'label': (R.strings.tooltips.credits.header()), 
                                                                  b'tooltip': (lambda data: makeTooltipData(backport.text(R.strings.tooltips.credits.header()), R.strings.session_stats.tooltip.statValue.credits.body, toNiceNumber(data.incomeCredits))), 
                                                                  b'detail': (lambda _: None), 
                                                                  b'value': (lambda data: toIntegral(data.incomeCredits)), 
                                                                  b'bigIcon': (R.images.gui.maps.icons.library.creditsIcon_23x22()), 
                                                                  b'smallIcon': (R.images.gui.maps.icons.library.CreditsIcon_2())}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_INCOME_CRYSTAL): {b'label': (R.strings.menu.crystals.promoWindow.title()), 
                                                                  b'tooltip': (lambda data: makeTooltipData(backport.text(R.strings.menu.crystals.promoWindow.title()), R.strings.session_stats.tooltip.statValue.crystals.body, toNiceNumber(data.incomeCrystal))), 
                                                                  b'detail': (lambda _: None), 
                                                                  b'value': (lambda data: toIntegral(data.incomeCrystal)), 
                                                                  b'bigIcon': (R.images.gui.maps.icons.library.crystal_23x22()), 
                                                                  b'smallIcon': (R.images.gui.maps.icons.library.crystal_16x16())}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_XP): {b'label': (R.strings.session_stats.label.gamingXp()), 
                                                      b'tooltip': (lambda data: makeTooltipData(backport.text(R.strings.session_stats.label.gamingXp()), R.strings.session_stats.tooltip.statValue.xp.body, toNiceNumber(data.xp))), 
                                                      b'detail': (lambda data: data.crystalDetails), 
                                                      b'value': (lambda data: toIntegral(data.xp)), 
                                                      b'bigIcon': (R.images.gui.maps.icons.library.xpIcon_23x22()), 
                                                      b'smallIcon': (R.images.gui.maps.icons.library.XpIcon())}, 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_FREE_XP): {b'label': (R.strings.session_stats.label.freeXp()), 
                                                           b'tooltip': (lambda data: makeTooltipData(backport.text(R.strings.session_stats.label.freeXp()), R.strings.session_stats.tooltip.statValue.freeXp.body, toNiceNumber(data.freeXP))), 
                                                           b'detail': (lambda data: data.crystalDetails), 
                                                           b'value': (lambda data: toIntegral(data.freeXP)), 
                                                           b'bigIcon': (R.images.gui.maps.icons.library.freeXpIcon_23x22()), 
                                                           b'smallIcon': (R.images.gui.maps.icons.library.FreeXpIcon_2())}}
_PROP_ID_TO_POSITIVE_VALUE_STYLE_MAP = {(SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_NET_CREDITS): (text_styles.credits), 
   (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_NET_CRYSTAL): (text_styles.crystal)}

def packTotalPropData(sessionStats, propId):
    value = _ECONOMIC_DATA[propId][b'value'](sessionStats)
    detailsData = _ECONOMIC_DATA[propId][b'detail'](sessionStats)
    params = []
    for paramName in detailsData._fields:
        param = getattr(detailsData, paramName)
        if param:
            params.append({b'label': (text_styles.standard(backport.text(getattr(R.strings.session_stats.propertyInfo.total.label, paramName)()))), 
               b'value': (_PROP_ID_TO_POSITIVE_VALUE_STYLE_MAP[propId](toIntegral(param)) if param > 0 else text_styles.error(toIntegral(param)))})

    return {b'title': (text_styles.promoSubTitle(backport.text(getattr(R.strings.session_stats.propertyInfo.total.label, propId)()))), 
       b'description': (text_styles.main(backport.text(R.strings.session_stats.propertyInfo.total.descr()))), 
       b'params': params, 
       b'icon': (getSessionStatsPropImage(propId)), 
       b'total': {b'label': (text_styles.mainBig(backport.text(R.strings.session_stats.propertyInfo.total.total()))), 
                  b'value': (text_styles.highlightText(value))}}


def packEfficiencyPropData(randomStats, sessionStats, accountWtr, propId):
    data = _EFFICIENT_DATA[propId]
    isWtr = propId == SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_WTR
    isInteger = propId in (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_WTR,)
    isWithoutTotalValue = propId in (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_AVERAGE_VEHICLE_LEVEL,)
    isWithoutDelta = propId in (SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_WINS,
     SESSION_STATS_CONSTANTS.SESSION_STATS_PROPS_AVERAGE_FRAGS)
    if isWtr:
        totalValue = data[b'totalValue'](accountWtr)
    else:
        totalValue = data[b'totalValue'](randomStats)
    currentValue = data[b'currentValue'](sessionStats)
    dynamicValue = data[b'delta'](sessionStats)
    if not dynamicValue:
        dynamicValue = text_styles.highlightText(b'-')
        diffIconSource = None
    elif dynamicValue > 0.0:
        precisionValue = precisionFormat(dynamicValue, showIntegerOnly=isInteger)
        dynamicValue = precisionValue and text_styles.success(precisionValue)
        diffIconSource = backport.image(R.images.gui.maps.icons.vehParams.icon_increase())
    else:
        precisionValue = precisionFormat(dynamicValue, showIntegerOnly=isInteger)
        dynamicValue = precisionValue and text_styles.error(precisionValue)
        diffIconSource = backport.image(R.images.gui.maps.icons.vehParams.icon_decrease())
    params = []
    if not isWithoutTotalValue:
        params.append({b'label': (text_styles.standard(backport.text(R.strings.session_stats.propertyInfo.total()))), 
           b'value': (text_styles.main(totalValue))})
    params.append({b'label': (text_styles.standard(backport.text(R.strings.session_stats.propertyInfo.current()))), 
       b'value': (text_styles.main(currentValue))})
    if not isWithoutTotalValue and not isWithoutDelta:
        params.append({b'label': (text_styles.standard(backport.text(R.strings.session_stats.propertyInfo.dynamic()))), 
           b'value': dynamicValue, 
           b'delta': {b'icon': diffIconSource}})
    return {b'title': (text_styles.promoSubTitle(backport.text(data[b'title']))), 
       b'description': (text_styles.main(backport.text(data[b'descr']))), 
       b'params': params, 
       b'icon': (getSessionStatsPropImage(propId))}


def packLastBattleData(data):
    settings = SessionStatsSettingsController().getSettings()
    isViewWithSpending = settings[SESSION_STATS.ECONOMIC_BLOCK_VIEW] == SESSION_STATS.ECONOMIC_BLOCK_VIEW_WITH_SPENDING
    result = []
    if isViewWithSpending:
        for idWithoutSpending in _VIEW_ECONOMIC_DATA_WITHOUT_SPENIDNG:
            economicData = _ECONOMIC_DATA[idWithoutSpending]
            result.append({b'label': (text_styles.main(backport.text(economicData[b'label']))), 
               b'icon': (backport.image(economicData[b'bigIcon'])), 
               b'value': (economicData[b'value'](data)), 
               b'tooltip': (economicData[b'tooltip'](data))})

    else:
        for idWithSpending in _VIEW_ECONOMIC_DATA_WITH_SPENIDNG:
            economicData = _ECONOMIC_DATA[idWithSpending]
            result.append({b'label': (backport.text(economicData[b'label'])), 
               b'icon': (backport.image(economicData[b'bigIcon'])), 
               b'value': (economicData[b'value'](data)), 
               b'id': idWithSpending})

    return result


def packTotalData(data):
    settings = SessionStatsSettingsController().getSettings()
    isViewWithSpending = settings[SESSION_STATS.ECONOMIC_BLOCK_VIEW] == SESSION_STATS.ECONOMIC_BLOCK_VIEW_WITH_SPENDING
    result = []
    if isViewWithSpending:
        for idWithSpending in _VIEW_ECONOMIC_DATA_WITH_SPENIDNG:
            economicData = _ECONOMIC_DATA[idWithSpending]
            result.append({b'label': (backport.text(economicData[b'label'])), 
               b'icon': (backport.image(economicData[b'smallIcon'])), 
               b'value': (economicData[b'value'](data)), 
               b'id': idWithSpending})

    else:
        for idWithoutSpending in _VIEW_ECONOMIC_DATA_WITHOUT_SPENIDNG:
            economicData = _ECONOMIC_DATA[idWithoutSpending]
            result.append({b'label': (text_styles.main(backport.text(economicData[b'label']))), 
               b'icon': (backport.image(economicData[b'smallIcon'])), 
               b'value': (economicData[b'value'](data)), 
               b'tooltip': (economicData[b'tooltip'](data))})

    return result


def packBattleEfficiencyData(data, parameters):
    settings = SessionStatsSettingsController().getSettings()
    view = []
    for parameter in parameters:
        for idEfficientData, efficient in _EFFICIENT_DATA.iteritems():
            if efficient[b'settings'] == parameter and settings[efficient[b'settings']]:
                view.append({b'icon': (backport.image(efficient[b'icon'])), 
                   b'label': (text_styles.main(backport.text(efficient[b'label']))), 
                   b'value': (text_styles.stats(efficient[b'currentValue'](data))), 
                   b'delta': (getDeltaAsData(efficient[b'delta'](data))), 
                   b'id': idEfficientData})

    return view


def makeTooltipData(header, resId, total):
    body = backport.text(resId(), total=total, lastBattle=total)
    return makeTooltip(header, body)


def toIntegral(value):
    if value is None:
        return b'-'
    else:
        return backport.getIntegralFormat(value)


def precisionFormat(value, showIntegerOnly=False):
    if showIntegerOnly:
        if abs(value) >= 1:
            return backport.getIntegralFormat(value)
        return b''
    if abs(value) >= 10:
        return backport.getFractionalFormat(value)
    if abs(value) >= 10 ** (-_INFOTIP_PRECISION):
        return b'%.*f' % (_INFOTIP_PRECISION, value)
    return b''


def getDeltaAsData(deltaVal):
    data = {}
    if deltaVal:
        if deltaVal < 0:
            data[b'icon'] = backport.image(R.images.gui.maps.icons.vehParams.icon_decrease())
        else:
            data[b'icon'] = backport.image(R.images.gui.maps.icons.vehParams.icon_increase())
    return data


def getNationIcon(nationID, width, height):
    return (b'../maps/icons/nations/{0}x{1}/{2}.png').format(width, height, nations.NAMES[nationID])


def getSessionStatsPropImage(propId, width=54, height=54):
    return (b'../maps/icons/statistic/{0}x{1}/{2}.png').format(width, height, propId)


def processRatioValue(value):
    if value.ratio is not None:
        return backport.getNiceNumberFormat(float(value.ratio))
    else:
        if value.dealt is not None and value.received is not None:
            ctx = {b'numerator': (backport.getIntegralFormat(value.dealt)), b'denominator': (backport.getIntegralFormat(value.received))}
            sourceKey = b'inverse' if value.dealt == 0 else b'normal'
            return makeHtmlString(b'html_templates:lobby/session_stats/', b'ratio', ctx, sourceKey=sourceKey)
        return b'-'
