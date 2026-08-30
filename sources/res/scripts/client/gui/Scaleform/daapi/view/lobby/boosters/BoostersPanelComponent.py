from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.SlotsPanelMeta import SlotsPanelMeta
from gui.Scaleform.genConsts.BOOSTER_CONSTANTS import BOOSTER_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.goodies.goodie_items import MAX_ACTIVE_BOOSTERS_COUNT
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IBoostersController
from skeletons.gui.goodies import IGoodiesCache
_GUI_SLOTS_PROPS = {b'slotsCount': MAX_ACTIVE_BOOSTERS_COUNT, 
   b'slotWidth': 50, 
   b'paddings': 64, 
   b'groupPadding': 18, 
   b'ySlotPosition': 5, 
   b'offsetSlot': 13, 
   b'useOnlyLeftBtn': True}
ADD_BOOSTER_ID = b'add'
_ADD_AVAILABLE_BOOSTER_ID = b'addAvailable'
_EMPTY_BOOSTER_ID = b'empty'

class BoostersPanelComponent(SlotsPanelMeta):
    boosters = dependency.descriptor(IBoostersController)
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self):
        super(BoostersPanelComponent, self).__init__()
        self._isPanelInactive = True
        self._wasPopulated = False
        self._slotsMap = {}
        self._slotProps = None
        return

    def setSettings(self, isPanelInactive=True):
        self._isPanelInactive = isPanelInactive
        if self._wasPopulated:
            self._buildList()
        return

    def setSlotProps(self, slotProps):
        self._slotProps = slotProps
        self.as_setPanelPropsS(self._slotProps or _GUI_SLOTS_PROPS)
        return

    def getBoosterSlotID(self, idx):
        return self._slotsMap.get(int(idx), None)

    def getSlotTooltipBody(self, slotIdx):
        boosterID = self._slotsMap.get(int(slotIdx), None)
        tooltip = b''
        if boosterID in (ADD_BOOSTER_ID, _ADD_AVAILABLE_BOOSTER_ID):
            if not self._isPanelInactive:
                body = TOOLTIPS.BOOSTERSPANEL_OPENBOOSTERSWINDOW_BODY
                tooltip = makeTooltip(None, body)
        else:
            tooltip = TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO
        return tooltip

    def _populate(self):
        super(BoostersPanelComponent, self)._populate()
        g_clientUpdateManager.addCallbacks({b'goodies': (self.__onUpdateGoodies)})
        self.boosters.onBoosterChangeNotify += self.__onUpdateGoodies
        self._buildList()
        self._wasPopulated = True
        return

    def _dispose(self):
        self._isPanelInactive = None
        self._wasPopulated = None
        self._slotsMap = None
        self.boosters.onBoosterChangeNotify -= self.__onUpdateGoodies
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(BoostersPanelComponent, self)._dispose()
        return

    def __getAvailableBoosters(self):
        criteria = REQ_CRITERIA.BOOSTER.IS_READY_TO_ACTIVATE
        return self.goodiesCache.getBoosters(criteria=criteria)

    def _buildList(self):
        result = []
        activeBoosters = self.goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.ACTIVE)
        activeBoostersList = sorted(activeBoosters.values(), key=(lambda b: b.getUsageLeftTime()), reverse=True)
        availableBoostersCount = len(self.__getAvailableBoosters())
        activeBoostersCount = min(len(activeBoostersList), MAX_ACTIVE_BOOSTERS_COUNT)
        freeSlotsCount = MAX_ACTIVE_BOOSTERS_COUNT - min(activeBoostersCount, MAX_ACTIVE_BOOSTERS_COUNT)
        addBoostersSlotsCount = min(freeSlotsCount, availableBoostersCount)
        self._slotsMap = {}
        for idx in range(0, activeBoostersCount):
            booster = activeBoostersList[idx]
            self._slotsMap[idx] = booster.boosterID
            result.append(self.__makeBoosterVO(idx, booster))

        icon = b''
        if not self._isPanelInactive:
            icon = RES_ICONS.MAPS_ICONS_ARTEFACT_EMPTYORDER
        addAndActiveBoostersCount = activeBoostersCount + addBoostersSlotsCount
        for idx in range(activeBoostersCount, MAX_ACTIVE_BOOSTERS_COUNT):
            self._slotsMap[idx], slotLinkage = self.getEmptySlotParams(idx, addAndActiveBoostersCount)
            result.append(self.__makeEmptyBoosterVO(idx, slotLinkage, icon))

        self.as_setPanelPropsS(self._slotProps or _GUI_SLOTS_PROPS)
        self.as_setSlotsS(result)
        return

    def getEmptySlotParams(self, idx, addAndActiveBoostersCount):
        if idx < addAndActiveBoostersCount and not self._isPanelInactive:
            slotLinkage = BOOSTER_CONSTANTS.SLOT_ADD_UI
            emptyBoosterID = _ADD_AVAILABLE_BOOSTER_ID
        else:
            slotLinkage = BOOSTER_CONSTANTS.SLOT_UI
            emptyBoosterID = ADD_BOOSTER_ID
        return (
         emptyBoosterID, slotLinkage)

    def __makeBoosterVO(self, idx, booster):
        return {b'boosterId': (booster.boosterID), 
           b'id': (str(idx)), 
           b'icon': (booster.icon), 
           b'inCooldown': (booster.inCooldown), 
           b'cooldownPercent': (booster.getCooldownAsPercent()), 
           b'leftTime': (booster.getUsageLeftTime()), 
           b'leftTimeText': (booster.getShortLeftTimeStr()), 
           b'showLeftTime': True, 
           b'isDischarging': True, 
           b'isInactive': (self._isPanelInactive), 
           b'isEmpty': False, 
           b'qualityIconSrc': (booster.getQualityIcon()), 
           b'slotLinkage': (BOOSTER_CONSTANTS.SLOT_UI)}

    def __makeEmptyBoosterVO(self, idx, slotLinkage, icon):
        return {b'id': (str(idx)), 
           b'isInactive': (self._isPanelInactive), 
           b'isEmpty': True, 
           b'icon': icon, 
           b'slotLinkage': slotLinkage, 
           b'showLeftTime': False}

    def __onUpdateGoodies(self, *args):
        self._buildList()
        return
