from __future__ import absolute_import
from future.utils import viewitems
import nations
from gui import GUI_NATIONS_ORDER_INDEX_REVERSED
from gui.impl import backport
from gui.shared.gui_items.Vehicle import getSmallIconPath, Vehicle, VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED, getTypeSmallIconPath, getTypeBigIconPath
from helpers import int2roman, dependency
from helpers.i18n import makeString as _ms
from debug_utils import LOG_ERROR
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
from gui.server_events.awards_formatters import QuestsBonusComposer, getEventBoardsAwardPacker
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import formatErrorTextWithIcon, formatOkTextWithIcon, formatNotAvailableTextWithIcon, formatParameters, getFullName, getString, getClanTag, getStatusTitleStyle, formatAdditionalParameters, formatDate, formatTime
from gui.event_boards.event_boards_items import EVENT_TYPE, ExcelItem, PlayerEventsData, EventSettings, OBJECTIVE_PARAMETERS as _op, PLAYER_STATE_REASON as _psr, CALCULATION_METHODS as _cm
from gui.Scaleform import getNationsFilterAssetPath
from nations import AVAILABLE_NAMES
from skeletons.gui.shared import IItemsCache

class EVENT_BOARDS_GROUP_TYPES(object):
    GOLD = 1
    SILVER = 2
    BRONZE = 3
    IRON = 4
    WOOD = 5


_CATEGORY_NAMES = {(EVENT_BOARDS_GROUP_TYPES.GOLD): b'gold', 
   (EVENT_BOARDS_GROUP_TYPES.SILVER): b'silver', 
   (EVENT_BOARDS_GROUP_TYPES.BRONZE): b'bronze', 
   (EVENT_BOARDS_GROUP_TYPES.IRON): b'iron', 
   (EVENT_BOARDS_GROUP_TYPES.WOOD): b'wood'}
FORMATS = {(EVENT_TYPE.NATION): (b'#nations:{}', b'../maps/icons/filters/nationsMedium/{}.png', None), 
   (EVENT_TYPE.LEVEL): (b'#menu:levels/{}', b'../maps/icons/filters/levels/level_{}.png', None), 
   (EVENT_TYPE.CLASS): (b'#quests:classes/{}', b'../maps/icons/filters/tanks/{}.png', b'../maps/icons/vehicleTypes/big/{}.png')}

def _vehicleHeaderCreator(vehicleCDStr):
    itemsCache = dependency.instance(IItemsCache)
    vehicle = itemsCache.items.getItemByCD(int(vehicleCDStr))
    title = vehicle.shortUserName
    iconPath = getTypeBigIconPath(vehicle.type, vehicle.isPremium)
    txtLevel = int2roman(vehicle.level)
    return (title, iconPath, txtLevel)


def makeTableViewHeaderVO(eType, value, eventName, status=None, statusTooltip=None):
    if eType == EVENT_TYPE.VEHICLE:
        title, icon, level = _vehicleHeaderCreator(value)
        popoverAlias = EVENTBOARDS_ALIASES.RESULT_FILTER_POPOVER_VEHICLES_ALIAS
    else:
        _title, _, _icon = FORMATS[eType]
        title = _ms(_title.format(value))
        icon = _icon.format(value) if _icon else None
        level = None
        popoverAlias = EVENTBOARDS_ALIASES.RESULT_FILTER_POPOVER_ALIAS
    return {b'title': title, 
       b'icon': icon, 
       b'name': (text_styles.main(_ms(EVENT_BOARDS.EXCEL_SUBHEADER, eventName=eventName))), 
       b'level': level, 
       b'popoverAlias': popoverAlias, 
       b'status': status, 
       b'statusTooltip': statusTooltip}


_LEADERBOARD_BG_CREATORS = {(EVENT_TYPE.NATION): (RES_ICONS.getEventBoardBg), 
   (EVENT_TYPE.VEHICLE): (lambda _: RES_ICONS.getEventBoardBg(b'vehicle')), 
   (EVENT_TYPE.LEVEL): (lambda _: RES_ICONS.getEventBoardBg(b'level')), 
   (EVENT_TYPE.CLASS): (lambda _: RES_ICONS.getEventBoardBg(b'class'))}

def makeTableViewBackgroundVO(eType, value):
    return _LEADERBOARD_BG_CREATORS[eType](value)


_OBJECTIVE_STRINGS = {(_op.ORIGINALXP): b'exp', 
   (_op.XP): b'exp', 
   (_op.DAMAGEDEALT): b'damage', 
   (_op.DAMAGEASSISTED): b'damage'}
_METHOD_ICON_NAMES = {(_cm.MAX): (b'battle_%s_max', b'calendar', b'battle_quantity'), 
   (_cm.SUMN): (b'battle_%s_total', b'battle_%s', b'battle_quantity'), 
   (_cm.SUMSEQN): (b'battle_%s_total', b'battle_%s', b'battle_quantity'), 
   (_cm.SUMMSEQN): (b'battle_%s_total', b'battle_%s', b'battle_quantity'), 
   (_cm.SUMALL): (b'battle_%s_total', b'battle_exp_average', b'battle_quantity')}

def makeTableHeaderVO(method, objective, eventType):
    if objective == _op.WINS:
        icons = (
         RES_ICONS.getEventBoardIcon(b'win_quantity'),
         RES_ICONS.getEventBoardIcon(b'battle_exp_average'),
         RES_ICONS.getEventBoardIcon(b'battle_quantity'))
    else:
        try:
            icons = [RES_ICONS.getEventBoardIcon(icon) if b'%s' not in icon else RES_ICONS.getEventBoardIcon(icon % _OBJECTIVE_STRINGS[objective]) for icon in _METHOD_ICON_NAMES[method]]
        except KeyError:
            LOG_ERROR(b'WGELEN: Wrong method/objective: %s/%s!' % (method, objective))
            return

    return {b'columns': [
                  {b'tooltip': (makeTooltip(TOOLTIPS.elen_excel_objparam_all_all_header(method, objective), TOOLTIPS.elen_excel_objparam_all_all_body(method, objective))), 
                     b'icon': (icons[0])},
                  {b'tooltip': (makeTooltip(TOOLTIPS.elen_excel_addparam_all_all_header(method, objective), TOOLTIPS.elen_excel_addparam_all_all_body(method, objective))), 
                     b'icon': (icons[1])},
                  {b'tooltip': (makeTooltip(TOOLTIPS.ELEN_EXCEL_INFOPARAM_WINS_HEADER, TOOLTIPS.elen_excel_infoparam_wins_all_body(eventType))), 
                     b'icon': (icons[2])}], 
       b'positionTooltip': (makeTooltip(TOOLTIPS.ELEN_EXCEL_POSITION_HEADER, TOOLTIPS.ELEN_EXCEL_POSITION_BODY)), 
       b'playerTooltip': (makeTooltip(TOOLTIPS.ELEN_EXCEL_PLAYER_HEADER, TOOLTIPS.ELEN_EXCEL_PLAYER_BODY))}


def makeEventBoardsTableDataVO(rewardCategories, method):
    rewardsFormatter = QuestsBonusComposer(getEventBoardsAwardPacker())
    data = []
    stripes = []
    for categoryNumber, category in viewitems(rewardCategories):
        players = category.get(b'players')
        if not players:
            continue
        rewards = category[b'rewards']
        isIndividual = len(rewards) > 1 and categoryNumber == EVENT_BOARDS_GROUP_TYPES.GOLD
        stripeVO = {b'rendererLinkage': (EVENTBOARDS_ALIASES.AWARD_STRIPE_RENDERER), 
           b'id': categoryNumber, 
           b'groupIcon': (RES_ICONS.getEventBoardGroup(categoryNumber)), 
           b'tooltip': (_ms(TOOLTIPS.ELEN_ANCOR_ALLGROUPS_HEADER, group=int2roman(categoryNumber), min=category.get(b'rank_min'), max=category.get(b'rank_max')))}
        if not isIndividual and rewards:
            stripeVO[b'icons'] = rewardsFormatter.getFormattedBonuses(rewards[0])
        data.append(stripeVO)
        stripes.append(stripeVO)
        for currentPlayerData in players:
            name = currentPlayerData.getName()
            clanAbbrev = currentPlayerData.getClanTag()
            clanColor = currentPlayerData.getClanColor()
            rank = currentPlayerData.getRank()
            params = (
             currentPlayerData.getP1(),
             currentPlayerData.getP2(),
             currentPlayerData.getP3())
            formattedParameters = formatParameters(method, params)
            player = {b'position': rank, 
               b'value1': (formattedParameters[0]), 
               b'value2': (formattedParameters[1]), 
               b'value3': (formattedParameters[2]), 
               b'userVO': {b'dbID': (currentPlayerData.getSpaId()), 
                           b'fullName': (getFullName(name, clanAbbrev, clanColor)), 
                           b'userName': name, 
                           b'clanAbbrev': (getClanTag(clanAbbrev, clanColor))}}
            additionalParameters = formatAdditionalParameters(method, params)
            player.update(additionalParameters)
            if isIndividual:
                player[b'icons'] = rewardsFormatter.getFormattedBonuses(rewards[min(rank, len(rewards)) - 1])
                player[b'rendererLinkage'] = EVENTBOARDS_ALIASES.TOP_PLAYER_AWARD_RENDERER
            else:
                player[b'rendererLinkage'] = EVENTBOARDS_ALIASES.BASE_PLAYER_AWARD_RENDERER
            data.append(player)

    return ({b'tableDP': data}, {b'tableDP': stripes})


def makeParameterTooltipVO(method, amount, parameter):
    parametersWithTooltip = [
     _op.ORIGINALXP, _op.XP]
    maxOrSum = b'max' if method == _cm.MAX else b'sum'
    if parameter in parametersWithTooltip and amount is not None:
        return makeTooltip(header=_ms(EVENT_BOARDS.TOOLTIP_TOP_NOREWARDGROUP), body=_ms(EVENT_BOARDS.tooltip_top_description_all(maxOrSum, parameter), number=int(amount)))
    else:
        return


def makeEventBoardsTableViewStatusVO(title, tooltip, info, value1, value2, value3, showPoints, buttonLabel, buttonTooltip, buttonVisible, buttonEnabled, titleTooltip, method):
    buttonTop = not title
    result = {b'title': title, 
       b'titleTooltip': tooltip, 
       b'buttonLabel': buttonLabel, 
       b'buttonTooltip': buttonTooltip, 
       b'buttonVisible': buttonVisible, 
       b'buttonEnabled': buttonEnabled, 
       b'buttonTop': buttonTop, 
       b'informationTooltip': titleTooltip}
    if showPoints:
        result.update({b'info': (text_styles.playerOnline(info)), 
           b'value1': (text_styles.vehicleStatusSimpleText(getString(value1))), 
           b'value2': (text_styles.main(getString(value2) if method != _cm.MAX else formatDate(value2))), 
           b'value3': (text_styles.main(getString(value3, b'0'))), 
           b'valueTime': (None if method != _cm.MAX else formatTime(value2))})
    return result


def makeAwardGroupDataTooltipVO(rewardCategories, enabledAncors):
    result = []
    for idx, enable in enumerate(enabledAncors):
        v = idx + 1
        if v in rewardCategories:
            body = TOOLTIPS.ELEN_ANCOR_ALLGROUPS_BODY if enable else TOOLTIPS.ELEN_ANCOR_NOTOCCUPIED_BODY
            header = _ms(TOOLTIPS.ELEN_ANCOR_ALLGROUPS_HEADER, group=int2roman(v), min=rewardCategories[v].get(b'rank_min'), max=rewardCategories[v].get(b'rank_max'))
            tooltip = makeTooltip(header, body)
            result.append(tooltip)

    return result


def makeFiltersVO(eventType, filters, selected=None, category=None):
    tooltip, value, _ = FORMATS[eventType]
    data = [{b'id': (str(lid)), b'value': (value.format(f)), b'tooltip': (makeTooltip(tooltip.format(f), (b'#event_boards:{0}/tooltip/{1}').format(category, eventType)) if category else _ms(tooltip.format(f))), b'selected': (lid == selected)} for lid, f in filters]
    return data


def _makeCantJoinReasonTooltip(stateReasons, playerData, limits):

    def _addItem(name, error):
        formatter = formatNotAvailableTextWithIcon if error else formatOkTextWithIcon
        return (error, formatter(name))

    header = TOOLTIPS.ELEN_STATUS_REQUIREMENTS_HEADER
    body = b''
    date = backport.getShortDateFormat(limits.getRegistrationDateMaxTs())
    winRateMin = limits.getWinRateMin()
    winRateMax = limits.getWinRateMax()
    battlesCount = limits.getBattlesCountMin()
    winRate = playerData.getWinRate()
    items = []
    items.append(_addItem(_ms(TOOLTIPS.ELEN_STATUS_CANTJOIN_REASON_BYAGE, date=date), _psr.BYAGE in stateReasons))
    items.append(_addItem(_ms(TOOLTIPS.ELEN_STATUS_CANTJOIN_REASON_BYVEHICLE), _psr.VEHICLESMISSING in stateReasons))
    if battlesCount:
        items.append(_addItem(_ms(TOOLTIPS.ELEN_STATUS_CANTJOIN_REASON_BYBATTLESCOUNT, number=battlesCount), _psr.BYBATTLESCOUNT in stateReasons))
    if winRateMin:
        items.append(_addItem(_ms(TOOLTIPS.ELEN_STATUS_CANTJOIN_REASON_BYWINRATELOW, number=winRateMin), _psr.BYWINRATE in stateReasons and winRate < winRateMin))
    if winRateMax:
        items.append(_addItem(_ms(TOOLTIPS.ELEN_STATUS_CANTJOIN_REASON_BYWINRATEHIGH, number=winRateMax), _psr.BYWINRATE in stateReasons and winRate > winRateMax))
    items.sort(key=(lambda item: item[0]), reverse=True)
    body = (b'\n').join([item[1] for item in items])
    return makeTooltip(header, body)


def makeCantJoinReasonTextVO(event, playerData):
    playerState = playerData.getPlayerStateByEventId(event.getEventID())
    stateReasons = playerState.getPlayerStateReasons() if playerState else []
    stateReason = stateReasons[0] if stateReasons else None
    tooltip = None
    buttonVisible = False
    if event.isRegistrationFinished():
        result = formatErrorTextWithIcon(EVENT_BOARDS.STATUS_CANTJOIN_REASON_ENDREGISTRATION)
    elif _psr.SPECIALACCOUNT in stateReasons:
        result = getStatusTitleStyle(_ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_SPECIAL))
    elif stateReason is _psr.WASUNREGISTERED:
        result = getStatusTitleStyle(_ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_LEFTEVENT))
        tooltip = makeTooltip(EVENT_BOARDS.STATUS_CANTJOIN_REASON_LEFTEVENT, EVENT_BOARDS.STATUS_CANTJOIN_REASON_LEFTEVENT_TOOLTIP)
    else:
        limits = event.getLimits()
        if len(stateReasons) > 1:
            reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_MANY, number=len(stateReasons))
            tooltip = _makeCantJoinReasonTooltip(stateReasons, playerData, limits)
        elif stateReason is _psr.BYWINRATE:
            winRate = playerData.getWinRate()
            winRateMin = limits.getWinRateMin()
            winRateMax = limits.getWinRateMax()
            if winRate < winRateMin:
                reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_BYWINRATELOW, number=str(winRateMin))
            else:
                reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_BYWINRATEHIGH, number=str(winRateMax))
        elif stateReason is _psr.BYAGE:
            date = backport.getShortDateFormat(limits.getRegistrationDateMaxTs())
            reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_BYAGE, date=date)
        elif stateReason is _psr.BYBATTLESCOUNT:
            battlesCount = playerData.getBattlesCount()
            reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_BYBATTLESCOUNT, number=battlesCount)
        elif stateReason is _psr.BYBAN:
            reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_BANNED)
        elif stateReason is _psr.VEHICLESMISSING:
            reasonText = _ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_VEHICLESMISSING)
        else:
            reasonText = b''
        notAvailableText = formatErrorTextWithIcon(EVENT_BOARDS.STATUS_CANTJOIN_NOTAVAILABLE)
        reasonText = text_styles.main(reasonText)
        result = (b'{} {}').format(notAvailableText, reasonText)
        buttonVisible = True
    return (result, tooltip, buttonVisible)


def makeVehicleVO(vehicle):
    return {b'id': (vehicle.intCD), 
       b'vehicleName': (text_styles.main(vehicle.shortUserName)), 
       b'smallVehicleIconPath': (vehicle.iconSmall), 
       b'nationIconPath': (getNationsFilterAssetPath(AVAILABLE_NAMES[vehicle.nationID])), 
       b'typeIconPath': (getTypeSmallIconPath(vehicle.type, vehicle.isPremium)), 
       b'level': (vehicle.level), 
       b'isInHangar': (vehicle.isInInventory)}


def makeVehiclePopoverVO(vehicle):
    return {b'dbID': (vehicle.intCD), 
       b'level': (vehicle.level), 
       b'shortUserName': (vehicle.shortUserName), 
       b'smallIconPath': (getSmallIconPath(vehicle.name)), 
       b'nationID': (vehicle.nationID), 
       b'type': (vehicle.type), 
       b'typeIcon': (getTypeSmallIconPath(vehicle.type, vehicle.isPremium)), 
       b'inHangar': (vehicle.isInInventory), 
       b'selected': False}


def vehicleValueGetter(vehicle, field):
    if isinstance(vehicle, Vehicle):
        vehicle = makeVehiclePopoverVO(vehicle)
    sortMapping = {b'nations': (GUI_NATIONS_ORDER_INDEX_REVERSED[nations.NAMES[vehicle[b'nationID']]]), 
       b'type': (VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED[vehicle[b'type']]), 
       b'level': (vehicle[b'level']), 
       b'name': (vehicle[b'shortUserName']), 
       b'hangar': (vehicle[b'inHangar'])}
    return sortMapping[field]


def makePrimeTimesTooltipVO(primeTimes, currentPeripheryID, getNameFunc):
    ptList = []
    primeTimes = sorted(primeTimes, key=(lambda p: int(p.getServer())))
    for pt in primeTimes:
        peripheryID = int(pt.getServer())
        name = str(getNameFunc(peripheryID, False))
        timePeriod = (b'{} - {}').format(pt.getStartLocalTime(), pt.getEndLocalTime())
        ptList.append((b'{} {}').format(text_styles.main(name + b':'), text_styles.standard(timePeriod)))

    body = (b'\n').join(ptList)
    return makeTooltip(_ms(TOOLTIPS.ELEN_CONDITION_PRIMETIME), body)
