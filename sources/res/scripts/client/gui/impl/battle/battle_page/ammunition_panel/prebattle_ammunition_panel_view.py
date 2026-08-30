from __future__ import absolute_import
from typing import TYPE_CHECKING
import CommandMapping
from Event import Event, EventManager
from account_helpers.settings_core.settings_constants import CONTROLS
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.battle.battle_page.ammunition_panel.ammunition_panel import PrebattleAmmunitionPanel
from gui.impl.battle.battle_page.ammunition_panel.groups_controller import COMMAND_MAPPING
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GROUPS_MAP
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_panel_view_model import PrebattleAmmunitionPanelViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.pub import ViewImpl
from gui.impl.pub.tooltip_window import SimpleTooltipContent
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from gui.shared.tooltips.consumables_panel import makeShellTooltip, buildEquipmentSlotTooltipTextBySlotInfo
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
if TYPE_CHECKING:
    from typing import Optional
    from frameworks.wulf import ViewEvent, View
_R_SIMPLE_TOOLTIPS = (
 R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent(),
 R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipHtmlContent())

class PrebattleAmmunitionPanelView(ViewImpl):
    __slots__ = (b'onSwitchLayout', b'onViewLoaded', b'__ammunitionPanel', b'__vehicle', b'__eventManager')
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, vehicle, *args):
        settings = ViewSettings(layoutID=R.views.battle.battle_page.PrebattleAmmunitionPanelView(), flags=ViewFlags.VIEW, model=PrebattleAmmunitionPanelViewModel(), args=args)
        super(PrebattleAmmunitionPanelView, self).__init__(settings)
        self.__ammunitionPanel = None
        self.__vehicle = vehicle
        self.__eventManager = EventManager()
        self.onSwitchLayout = Event(self.__eventManager)
        self.onViewLoaded = Event(self.__eventManager)
        return

    @property
    def viewModel(self):
        return super(PrebattleAmmunitionPanelView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        slotType = event.getArgument(b'slotType')
        header, body = (b'', b'')
        if slotType == TankSetupConstants.SHELLS:
            intCD = int(event.getArgument(b'intCD'))
            header, body, _ = makeShellTooltip(intCD)
        elif slotType in (TankSetupConstants.BATTLE_BOOSTERS, TankSetupConstants.CONSUMABLES):
            slotId = int(event.getArgument(b'slotId'))
            header, body = buildEquipmentSlotTooltipTextBySlotInfo(slotType=slotType, slotId=slotId)
        if header or body:
            return SimpleTooltipContent(R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipHtmlContent(), header, body)
        else:
            return

    def createContextMenu(self, event):
        return

    def setNextShellCD(self, shellCD):
        if shellCD is None:
            return
        else:
            self.__ammunitionPanel.onNextShellChanged(shellCD)
            return

    def setCurrentShellCD(self, shellCD):
        if shellCD is None:
            return
        else:
            self.__ammunitionPanel.onCurrentShellChanged(shellCD)
            return

    def updateViewActive(self, isActive):
        self.viewModel.setIsDisabled(not isActive)
        return

    def updateViewVehicle(self, vehicle, fullUpdate=True):
        self.__vehicle = vehicle
        self.__ammunitionPanel.update(self.__vehicle, fullUpdate=fullUpdate)
        self.__ammunitionPanel.viewModel.setAmmoNotFull(not self.__vehicle.isAmmoFull)
        return

    def updateState(self, state):
        self.viewModel.setState(state)
        return

    def setTimer(self, timeLeft):
        self.viewModel.setTimeTillBattleStart(timeLeft)
        return

    def _initialize(self, *args, **kwargs):
        super(PrebattleAmmunitionPanelView, self)._initialize()
        self.__addListeners()
        self.__ammunitionPanel.initialize()
        return

    def _finalize(self):
        self.__removeListeners()
        self.__ammunitionPanel.finalize()
        super(PrebattleAmmunitionPanelView, self)._finalize()
        return

    def _onLoading(self, currShellCD, nextShellCD, state, *args, **kwargs):
        super(PrebattleAmmunitionPanelView, self)._onLoading(*args, **kwargs)
        self.__ammunitionPanel = PrebattleAmmunitionPanel(self.viewModel.ammunitionPanel, self.__vehicle, ctx={b'state': state})
        self.__ammunitionPanel.onLoading()
        self.updateViewVehicle(self.__vehicle, fullUpdate=False)
        self.viewModel.setState(state)
        self.setCurrentShellCD(currShellCD)
        self.setNextShellCD(nextShellCD)
        return

    def _onLoaded(self, *args, **kwargs):
        super(PrebattleAmmunitionPanelView, self)._onLoaded(*args, **kwargs)
        self.viewModel.setIsReady(True)
        self.onViewLoaded()
        return

    def __addListeners(self):
        g_eventBus.addListener(GameEvent.CHANGE_AMMUNITION_SETUP, self.__onChangeSetupByKey, scope=EVENT_BUS_SCOPE.BATTLE)
        self.viewModel.ammunitionPanel.onChangeSetupIndex += self.__onChangeSetupByButton
        self.__settingsCore.onSettingsApplied += self.__onSettingsApplied
        return

    def __removeListeners(self):
        g_eventBus.removeListener(GameEvent.CHANGE_AMMUNITION_SETUP, self.__onChangeSetupByKey, scope=EVENT_BUS_SCOPE.BATTLE)
        self.viewModel.ammunitionPanel.onChangeSetupIndex -= self.__onChangeSetupByButton
        self.__settingsCore.onSettingsApplied -= self.__onSettingsApplied
        self.__eventManager.clear()
        return

    def __onChangeSetupByButton(self, args):
        hudGroupID, newLayoutIdx = args.get(b'groupId', None), args.get(b'currentIndex', None)
        if self.viewModel.getIsDisabled() or hudGroupID is None or newLayoutIdx is None:
            return
        self.__changeSetup(int(hudGroupID), int(newLayoutIdx))
        return

    def __onChangeSetupByKey(self, event):
        key = event.ctx[b'key']
        cmdMap = CommandMapping.g_instance
        hudGroupID = None
        if cmdMap.isFired(CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_1, key):
            hudGroupID = COMMAND_MAPPING[CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_1]
        elif cmdMap.isFired(CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_2, key):
            hudGroupID = COMMAND_MAPPING[CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_2]
        if self.viewModel.getIsDisabled() or hudGroupID is None:
            return
        self.__changeSetup(hudGroupID)
        return

    def __changeSetup(self, hudGroupID, newLayoutIdx=None):
        groupID = GROUPS_MAP[hudGroupID]
        newLayoutIdx = newLayoutIdx or self.__vehicle.setupLayouts.getNextLayoutIndex(groupID)
        if self.__ammunitionPanel.isNewSetupLayoutIndexValid(hudGroupID, newLayoutIdx):
            self.onSwitchLayout(groupID, newLayoutIdx)
        return

    def __onSettingsApplied(self, diff):
        if CONTROLS.KEYBOARD in diff:
            self.__ammunitionPanel.updateSectionsWithKeySettings()
        return
