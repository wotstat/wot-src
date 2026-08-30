import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.bonuses import getServiceBonuses
from helpers import dependency
from helpers.time_utils import getTimestampFromISO
from skeletons.gui.game_control import IMapboxController
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array, ViewEvent
    from frameworks.wulf.windows_system.window import Window
    from gui.impl.pub import WindowImpl
    from gui.shared.missions.packers.bonus import BonusUIPacker

def getMapboxRewardTooltip(event, tooltipData, parentWindow):
    if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        tooltipData = tooltipData[int(tooltipId)]
        window = backport.BackportTooltipWindow(tooltipData, parentWindow)
        window.load()
        return window
    else:
        return


def packMapboxRewardModelAndTooltip(rewardsList, bonusList, packer, numBattles, tooltipsList=None):
    groupStartIdx = len(tooltipsList)
    groupIdx = 0
    mapboxCtrl = dependency.instance(IMapboxController)
    for bonusItem in bonusList:
        totalIdx = groupStartIdx + groupIdx
        tooltipsData = packer.getToolTip(bonusItem)
        for bonusIdx, bonusModel in enumerate(packer.pack(bonusItem)):
            bonusModel.setTooltipId(str(totalIdx))
            bonusModel.setIndex(groupIdx)
            storedReward = mapboxCtrl.getStoredReward(numBattles, totalIdx)
            if storedReward:
                bonusModel.setPreviousIcon(mapboxCtrl.getStoredReward(numBattles, totalIdx))
            if tooltipsList is not None:
                tooltipsList.append(tooltipsData[bonusIdx])
            groupIdx += 1
            rewardsList.addViewModel(bonusModel)
            if bonusItem.getName() == b'selectableCrewbook':
                mapboxCtrl.storeReward(numBattles, totalIdx, bonusModel.getIcon())

    return


def formatMapboxBonuses(reward):
    result = []
    for bonusItemData in formatMapboxRewards(reward):
        result += getServiceBonuses(bonusItemData[b'name'], bonusItemData[b'value'])

    return result


def formatMapboxRewards(reward):
    result = []
    for bonusItemData in reward:
        name = bonusItemData[b'name']
        value = bonusItemData[b'value']
        valueAdapter = _BONUS_FORMAT_ADAPTERS.get(name)
        if valueAdapter is not None:
            value = valueAdapter(bonusItemData[b'value'])
        result.append({b'name': name, b'value': value})

    return result


def convertTimeFromISO(timeStr):
    if timeStr:
        return getTimestampFromISO(timeStr)
    return 0


def _adaptMapboxDossierFormat(dossierValue):
    result = {}
    for bonus in dossierValue:
        result.setdefault(bonus[b'dossierType'], {})
        result[bonus[b'dossierType']].update({(bonus[b'achievementType'], bonus[b'achievementName']): {b'value': (bonus[b'value']), 
                                                                    b'unique': (bonus[b'unique']), b'type': (bonus[b'type'])}})

    return result


def _adaptCDKeys(itemValue):
    return {int(key): value for key, value in itemValue.iteritems()}


def _adaptUniversalCrewbook(crewbookItems):
    for crewbook in crewbookItems:
        options = crewbook[b'options']
        valueAdapter = _BONUS_FORMAT_ADAPTERS.get(options[b'name'])
        if valueAdapter is not None:
            crewbook[b'options'][b'value'] = valueAdapter(options[b'value'])

    return crewbookItems


_BONUS_FORMAT_ADAPTERS = {b'dossier': _adaptMapboxDossierFormat, 
   b'goodies': _adaptCDKeys, 
   b'items': _adaptCDKeys, 
   b'selectableCrewbook': _adaptUniversalCrewbook, 
   b'randomCrewbook': _adaptUniversalCrewbook}
