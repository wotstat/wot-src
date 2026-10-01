import typing
from PlayerEvents import g_playerEvents
from frameworks.wulf import ViewFlags, ViewSettings
from gui.Scaleform.Waiting import Waiting
from gui.impl.gen import R
from gui.shared.event_dispatcher import showHangar
from portal.gui.impl.gen.view_models.views.lobby.portal_upgrade_ability_item_model import PortalUpgradeAbilityItemModel
from portal.gui.impl.gen.view_models.views.lobby.portal_upgrade_view_model import PortalUpgradeViewModel
from gui.impl.pub import ViewImpl
from portal.gui.shared.event_dispatcher import showAboutImprovementsView, showPortalUpgradeResetView
from portal.gui.impl.lobby.tooltips.modules_tooltip import ModulesTooltip
from portal.gui.impl.lobby.tooltips.abilities_tooltip import AbilitiesTooltip
from portal.gui.impl.lobby.tooltips.upgrade_info_tooltip import UpgradeInfoTooltip
from portal.gui.impl.lobby.tooltips.params_tooltip import ParamsTooltip
from portal.gui.impl.lobby.tooltips.progress_token_tooltip import ProgressTokenTooltip
from portal.gui.impl.gen.view_models.views.lobby.portal_research_tree import PortalResearchTree
from portal.gui.impl.gen.view_models.views.lobby.portal_ttx_item_model import PortalTtxItemModel
from portal.gui.impl.gen.view_models.views.lobby.params_ttx_model import ParamsTtxModel
from portal.gui.impl.gen.view_models.views.lobby.node_stage_model import NodeStageModel, NodeStatus, NodeType, ItemType, ItemModifier
from portal.skeletons.portal_event_controller import IPortalEventController
import logging
from helpers import dependency
from gui.impl import backport
from frameworks.wulf import Array
from portal.sounds.sound_constants import PORTAL_UPGRADE_SOUND_SPACE
from skeletons.gui.game_control import IHangarFeatureStateController
from skeletons.gui.shared import IItemsCache
from items import vehicles, ITEM_TYPE_NAMES
from portal_account_settings import isVehicleUpgradesViewed, setVehicleUpgradesViewed, setMaxViewedVehicleUpgradesStage, getMaxViewedVehicleUpgradesStages, isAboutImprovementsViewed, setMaxViewedUnlockedUpgradeLevel
from gui.shared.gui_items.Vehicle import Vehicle
from portal.vehicle_helpers.portal_params_helper import PortalParamsHelper
from portal_common.portal_account_helpers.vehicle_upgrade_tree import VehicleUpgradesHelper, MAX_NODES_PER_LEVEL
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import LobbySimpleEvent
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
if typing.TYPE_CHECKING:
    from portal.vehicle_helpers.portal_params_helper import PortalParam
    from typing import List
_logger = logging.getLogger(__name__)
UPGRADE_TYPE_TO_NODE_TYPE = {b'abilities': (NodeType.ABILITY), 
   b'vehicleModifiers': (NodeType.VEHICLEMODIFIER), 
   b'modules': (NodeType.MODULE)}

class PortalUpgradeView(ViewImpl):
    __slots__ = (b'__currentVehicle',)
    __itemsCache = dependency.descriptor(IItemsCache)
    __portalController = dependency.descriptor(IPortalEventController)
    __hangarFeatureStateController = dependency.descriptor(IHangarFeatureStateController)
    _COMMON_SOUND_SPACE = PORTAL_UPGRADE_SOUND_SPACE

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = PortalUpgradeViewModel()
        self.__currentVehicle = None
        super(PortalUpgradeView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(PortalUpgradeView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.portal.lobby.tooltips.ModulesTooltip():
            itemId = event.getArgument(b'itemId', b'default')
            return ModulesTooltip(itemId)
        if contentID == R.views.portal.lobby.tooltips.AbilitiesTooltip():
            name = event.getArgument(b'name', b'default')
            learned = event.getArgument(b'learned')
            nodes = self.__portalController.getVehicleUpgradeNodes(self.__currentVehicle)
            for _, (upgradeLevel, upgradeNodes) in enumerate(nodes.iteritems()):
                for _, (upgradeNode, _) in enumerate(zip(upgradeNodes[b'nodes'], upgradeNodes)):
                    _, _, _, itemName = self.__parseNodeItem(upgradeNode)
                    if itemName == name:
                        return AbilitiesTooltip(name, learned, level=upgradeLevel + 2)

            return AbilitiesTooltip(name, learned)
        if contentID == R.views.portal.lobby.tooltips.UpgradeInfoTooltip():
            return UpgradeInfoTooltip()
        if contentID == R.views.portal.lobby.tooltips.ParamsTooltip():
            name = event.getArgument(b'name')
            return ParamsTooltip(name)
        if contentID == R.views.portal.lobby.tooltips.ProgressTokenTooltip():
            currentPoints = self.__portalController.getVehicleExperience(self.__currentVehicle)
            nextLevelPoints = 0
            maxUpgradeLevel = len(self.__portalController.getVehicleUpgradeNodes(self.__currentVehicle))
            upgradeLevel = self.__portalController.getUpgradeLevel(self.__currentVehicle)
            isCompleted = upgradeLevel == maxUpgradeLevel
            nodes = self.__portalController.getVehicleUpgradeNodes(self.__currentVehicle)
            currentLevel = self.__portalController.getUpgradeLevel(self.__currentVehicle)
            for _, (upgradeLevel, upgradeNodes) in enumerate(nodes.iteritems()):
                if upgradeLevel == currentLevel:
                    researchedNodes = self.__portalController.getDeserializedUpgradeTreeLevel(self.__currentVehicle, upgradeLevel)
                    researchedNodes = [node for _, node in researchedNodes.iteritems()]
                    for _, (_, _) in enumerate(zip(upgradeNodes[b'nodes'], researchedNodes)):
                        requiredExp = upgradeNodes[b'requiredPoints']
                        nextLevelPoints = requiredExp

                    break

            return ProgressTokenTooltip(False, isCompleted, currentPoints, nextLevelPoints)
        return super(PortalUpgradeView, self).createToolTipContent(event, contentID)

    def _onLoaded(self, *args, **kwargs):
        self.__hangarFeatureStateController.enter(self.layoutID, doHideHeader=True)
        return

    def _onLoading(self, *args, **kwargs):
        super(PortalUpgradeView, self)._onLoading()
        self.__hangarFeatureStateController.cgfCameraManager.switchByCameraName(b'ShiftedTank', instantly=False)
        self._updateModel()
        return

    def _finalize(self):
        if self.__hangarFeatureStateController.cgfCameraManager:
            self.__hangarFeatureStateController.cgfCameraManager.switchByCameraName(b'Tank', instantly=False)
        self.__hangarFeatureStateController.exit(self.layoutID)
        super(PortalUpgradeView, self)._finalize()
        return

    def _updateModel(self):
        with self.viewModel.transaction() as model:
            self.__currentVehicle = self.__portalController.getCurrentSelectedVehicle()
            currentLevel = self.__portalController.getMaxUnlockedLevel(self.__currentVehicle)
            setMaxViewedUnlockedUpgradeLevel(self.__currentVehicle.intCD, currentLevel)
            if not isAboutImprovementsViewed():
                showAboutImprovementsView()
            isFirstEnter = not isVehicleUpgradesViewed(self.__currentVehicle.intCD) and self.__portalController.canUpgradeVehicle(self.__currentVehicle)
            if isFirstEnter:
                setVehicleUpgradesViewed(self.__currentVehicle.intCD, True)
            model.setIsFirstEnter(isFirstEnter)
            self.__fillUpgradesTree(model)
            self.__fillVehicleStats(model)
        self.__onPortalSquadStateChanged()
        return

    def __fillUpgradesTree(self, model):
        researchTreeStages = model.getResearchTree()
        researchTreeStages.clear()
        incompatibleModules = model.getIncompatibleModules()
        incompatibleModules.clear()
        incompatibleModules.invalidate()
        isUpgradeAvailable = self.__portalController.canUpgradeVehicle(self.__currentVehicle)
        model.setUpgradeAvailable(isUpgradeAvailable if isUpgradeAvailable else False)
        nodes = self.__portalController.getVehicleUpgradeNodes(self.__currentVehicle)
        vehicleExp = self.__portalController.getVehicleExperience(self.__currentVehicle)
        currentLevel = self.__portalController.getUpgradeLevel(self.__currentVehicle)
        for stageID, (upgradeLevel, upgradeNodes) in enumerate(nodes.iteritems()):
            stageView = PortalResearchTree()
            stageView.setStageNumber(upgradeLevel)
            stageNodes = Array()
            researchedNodes = self.__portalController.getDeserializedUpgradeTreeLevel(self.__currentVehicle, upgradeLevel)
            researchedNodes = [node for _, node in researchedNodes.iteritems()]
            stageView.setIsUnlocked(any(researchedNodes))
            stageView.setIsViewed(stageID <= getMaxViewedVehicleUpgradesStages(self.__currentVehicle.intCD))
            for nodeId, (upgradeNode, isResearched) in enumerate(zip(upgradeNodes[b'nodes'], researchedNodes)):
                requiredExp = upgradeNodes[b'requiredPoints']
                nodeView = NodeStageModel()
                if upgradeLevel > currentLevel:
                    nodeStatus = NodeStatus.LOCKED
                elif upgradeLevel < currentLevel:
                    nodeStatus = NodeStatus.LEARNED if isResearched else NodeStatus.SKIPPED
                elif requiredExp > vehicleExp:
                    nodeStatus = NodeStatus.NOT_ENOUGH_POINTS
                else:
                    nodeStatus = NodeStatus.AVAILABLE
                nodeView.setId(upgradeLevel * MAX_NODES_PER_LEVEL + nodeId)
                nodeView.setNodeStatus(nodeStatus)
                nodeType, itemType, itemModifier, itemName = self.__parseNodeItem(upgradeNode)
                nodeView.setNodeType(nodeType)
                if itemType:
                    nodeView.setItemType(itemType)
                if itemModifier:
                    nodeView.setItemModifier(itemModifier)
                nodeView.setPointsToOpen(requiredExp)
                nodeView.setName(itemName)
                stageNodes.addViewModel(nodeView)

            stageView.setStageNodes(stageNodes)
            researchTreeStages.addViewModel(stageView)

        researchTreeStages.invalidate()
        return

    def __parseNodeItem(self, upgradeNode):
        itemName = None
        itemType = upgradeNode[b'itemType']
        itemModifier = upgradeNode[b'itemModifier']
        upgradeTypes = [upgradeType for upgradeType in upgradeNode.keys() if upgradeNode[upgradeType] and isinstance(upgradeNode[upgradeType], list)]
        if len(upgradeTypes) > 1:
            _logger.warning(b'There must be exactly one item type per node')
        upgradeType = upgradeTypes[0]
        nodeItems = upgradeNode[upgradeType]
        if len(nodeItems) > 1:
            _logger.warning(b'There must be exactly one node item')
        item = nodeItems[0]
        if upgradeType == b'abilities':
            itemName = item
        elif upgradeType == b'vehicleModifiers':
            itemName = item[b'type']
        elif upgradeType == b'modules':
            itemName = vehicles.getItemByCompactDescr(item).name
            itemType = vehicles.getItemByCompactDescr(item).itemTypeName
        itemType = ItemType(itemType) if itemType else None
        nodeType = NodeType(UPGRADE_TYPE_TO_NODE_TYPE[upgradeType]) if upgradeType else None
        itemModifier = ItemModifier(itemModifier) if itemModifier else None
        return (
         nodeType, itemType, itemModifier, itemName)

    def __fillVehicleStats(self, model):
        ttx = model.getTtx()
        ttx.clear()
        vehicle = model.currentVehicle
        vehPoints = self.__portalController.getVehicleExperience(self.__currentVehicle)
        vehicle.setName(self.__currentVehicle.userName)
        vehicle.setVehicleType(self.__currentVehicle.type)
        vehicleLvl = self.__portalController.getCurrentVehicleLevel(self.__currentVehicle)
        vehicle.setLvl(vehicleLvl)
        maxUpgradeLevel = len(self.__portalController.getVehicleUpgradeNodes(self.__currentVehicle))
        upgradeLevel = self.__portalController.getUpgradeLevel(self.__currentVehicle)
        model.setIsMaxLevelAchieved(upgradeLevel == maxUpgradeLevel)
        vehicle.setPoints(vehPoints)
        allAbilities = self.__portalController.getVehicleAbilities(self.__currentVehicle, includeLocked=True)
        unlockedAbilities = self.__portalController.getVehicleAbilities(self.__currentVehicle, includeLocked=False)
        abilities = vehicle.getAbilities()
        abilities.clear()
        for ability in allAbilities:
            abilityItem = PortalUpgradeAbilityItemModel()
            abilityItem.setName(ability)
            abilityItem.setIsReceived(ability in unlockedAbilities)
            abilities.addViewModel(abilityItem)

        abilities.invalidate()
        params = PortalParamsHelper.getVehicleParams(vehicle=self.__currentVehicle)
        self.__fillTtxParams(model, params)
        return

    def __fillPreviewStats(self, model, previewNodeNumber):
        ttx = model.getTtx()
        ttx.clear()
        originalParams = PortalParamsHelper.getVehicleParams(self.__currentVehicle)
        comparedVehicle = Vehicle(strCompactDescr=self.__currentVehicle.strCD)
        comparedDescr = comparedVehicle.descriptor
        upgradeLevel = previewNodeNumber / MAX_NODES_PER_LEVEL
        nodes = self.__portalController.getVehicleUpgradeNodes(self.__currentVehicle)[upgradeLevel][b'nodes']
        node = nodes[previewNodeNumber % MAX_NODES_PER_LEVEL]
        if node[b'abilities']:
            _logger.warning(b'this code point should have never been reached. Abilities does not have preview')
        dependencyList = []
        if node[b'modules']:
            upgradeNodes = self.__portalController.getVehicleUpgradeNodes(comparedVehicle)
            for module in node[b'modules']:
                itemTypeID, _, moduleID = vehicles.parseIntCompactDescr(module)
                if ITEM_TYPE_NAMES[itemTypeID] == b'vehicleTurret':
                    turretDescr = vehicles.getItemByCompactDescr(module)
                    if not any(gun for gun in turretDescr.guns if gun.id[1] == comparedDescr.gun.id[1]):
                        dependencyList = VehicleUpgradesHelper.getTurretDependencyGuns(upgradeNodes, previewNodeNumber, turretDescr)
                        _logger.info(b"Can't install turret before gun.")
                        continue
                    comparedDescr.installTurret(module, 0)
                elif ITEM_TYPE_NAMES[itemTypeID] == b'vehicleGun':
                    turretDescr, _ = comparedDescr.turrets[0]
                    gunDescr = vehicles.getItemByCompactDescr(module)
                    if not any(gun for gun in turretDescr.guns if gun.id[1] == moduleID):
                        _logger.info(b"Can't install gun for incompatible turret.")
                        dependencyList = VehicleUpgradesHelper.getGunDependencyTurrets(upgradeNodes, previewNodeNumber, comparedDescr, gunDescr)
                        continue
                comparedDescr.installComponent(module)

        if node[b'vehicleModifiers']:
            modifiers = node[b'vehicleModifiers']
            comparedParams = PortalParamsHelper.applyModifiersAndGetParams(comparedVehicle, modifiers)
        else:
            comparedParams = PortalParamsHelper.getVehicleParams(comparedVehicle)
        compareResult = PortalParamsHelper.getComparedParams(originalParams, comparedParams)
        self.__fillTtxParams(model, params=compareResult)
        researchTreeStages = model.getResearchTree()
        incompatibleModules = model.getIncompatibleModules()
        incompatibleModules.clear()
        for dependNodeNumber, dependModule in dependencyList:
            dependModuleDescr = vehicles.getItemByCompactDescr(dependModule)
            stage = researchTreeStages.getValue(dependNodeNumber / MAX_NODES_PER_LEVEL)
            nodes = stage.getStageNodes()
            dependNode = nodes.getValue(dependNodeNumber % MAX_NODES_PER_LEVEL)
            dependNode.setNodeStatus(NodeStatus.NEED_TO_LEARN)
            incompatibleModules.addString(dependModuleDescr.userString)

        incompatibleModules.invalidate()
        return

    @staticmethod
    def __fillTtxParams(model, params):
        ttx = model.getTtx()
        ttx.clear()
        for param in params:
            ttxItemView = PortalTtxItemModel()
            ttxParams = Array()
            ttxItemView.setName(param.name)
            ttxItemView.setDescription(backport.text(R.strings.menu.tank_params.dyn(param.name)()))
            for valueId, paramValue in enumerate(param.values):
                ttxParam = ParamsTtxModel()
                ttxParam.setId(valueId)
                ttxParam.setStatus(paramValue.status)
                ttxParam.setValue(round(paramValue.value, 2))
                ttxParams.addViewModel(ttxParam)

            ttxItemView.setParams(ttxParams)
            ttx.addViewModel(ttxItemView)

        ttx.invalidate()
        return

    def __onCloseHandler(self):
        showHangar()
        Waiting.hide(b'loadPage')
        self.destroyWindow()
        return

    def __onAboutImprovements(self):
        showAboutImprovementsView()
        return

    def __onReset(self):
        showPortalUpgradeResetView()
        return

    def __onNodeSelect(self, selectedNodeNumber):
        nodeID = int(selectedNodeNumber[b'id'])
        with self.viewModel.transaction() as model:
            self._updateModel()
            self.__fillPreviewStats(model, nodeID)
        return

    def __onNodeReset(self):
        self._updateModel()
        return

    def __onNodeUpgrade(self, upgradeNodeNumber):
        nodeID = int(upgradeNodeNumber[b'id'])
        self.__portalController.upgradeCurrentVehicle(nodeID)
        return

    def __onSelectNextVehicle(self):
        self.__portalController.selectNextPortalVehicle()
        self._updateModel()
        return

    def __onSelectPrevVehicle(self):
        self.__portalController.selectPrevPortalVehicle()
        self._updateModel()
        return

    def __onStageHovered(self, stageNumber):
        stageID = int(stageNumber[b'id'])
        with self.viewModel.transaction() as model:
            stages = model.getResearchTree()
            viewedStage = stages.getValue(stageID)
            viewedStage.setIsViewed(True)
            setMaxViewedVehicleUpgradesStage(self.__currentVehicle.intCD, stageID)
        return

    def __onVehicleExpChanged(self, vehicleExperience):
        changedVehicles = [vehicle for vehicle, _ in vehicleExperience.items()]
        if self.__currentVehicle.intCD in changedVehicles:
            self._updateModel()
        return

    def __onVehicleUpgradesMasksChanged(self, vehicleUpgradesMasks):
        changedVehicles = [vehicle for vehicle, _ in vehicleUpgradesMasks.items()]
        if self.__currentVehicle.intCD in changedVehicles:
            self._updateModel()
        return

    def __onStartMoving(self):
        g_eventBus.handleEvent(LobbySimpleEvent(LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={b'isOver3dScene': True}), EVENT_BUS_SCOPE.GLOBAL)
        return

    def __onMoveSpace(self, args=None):
        if args is None:
            return
        else:
            g_eventBus.handleEvent(CameraRelatedEvents(CameraRelatedEvents.LOBBY_VIEW_MOUSE_MOVE, ctx={b'dx': (args.get(b'dx')), b'dy': (args.get(b'dy')), b'dz': (args.get(b'dz'))}), EVENT_BUS_SCOPE.GLOBAL)
            return

    def __onPortalSquadStateChanged(self, *_):
        item = self.__portalController.getCurrentSelectedVehicle()
        vehicleState, _ = item.getState()
        inPlatoon = vehicleState == Vehicle.VEHICLE_STATE.IN_PREBATTLE
        if inPlatoon:
            self.__onCloseHandler()
        return

    def __onClientUpdated(self, diff, _):
        self._updateModel()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onAboutImprovements, self.__onAboutImprovements),
         (
          self.viewModel.onReset, self.__onReset),
         (
          self.viewModel.onNodeUpgrade, self.__onNodeUpgrade),
         (
          self.viewModel.onNodeSelect, self.__onNodeSelect),
         (
          self.viewModel.onNodeReset, self.__onNodeReset),
         (
          self.viewModel.onNextVehicleClick, self.__onSelectNextVehicle),
         (
          self.viewModel.onPrevVehicleClick, self.__onSelectPrevVehicle),
         (
          self.viewModel.onStageHovered, self.__onStageHovered),
         (
          self.__portalController.onVehicleExperienceChanged, self.__onVehicleExpChanged),
         (
          self.__portalController.onVehicleUpgradesMasksChanged, self.__onVehicleUpgradesMasksChanged),
         (
          self.viewModel.onStartMoving, self.__onStartMoving),
         (
          self.viewModel.onMoveSpace, self.__onMoveSpace),
         (
          self.viewModel.onClose, self.__onCloseHandler),
         (
          g_playerEvents.onClientUpdated, self.__onClientUpdated))
