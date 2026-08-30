import ArenaType, BigWorld, Math
from AvatarInputHandler.cameras import getViewProjectionMatrix
from ClientSelectableCameraObject import ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle
from Event import Event
from frameworks.state_machine import StateIdsObserver
from gui import GUI_SETTINGS
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_group_model import MapsTrainingGroupModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_map_model import MapsTrainingMapModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_scenario_model import MapsTrainingScenarioModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_view_model import MapsTrainingViewModel
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_minimap_point import MapsTrainingMinimapPoint
from gui.impl.lobby.maps_training.maps_training_tactical_maps_config import TacticalMapsConfigReader, Scenario, Team, Point
from gui.impl.lobby.maps_training.scenario_tooltip import ScenarioTooltip
from gui.prb_control.entities.listener import IGlobalListener
from gui.impl.lobby.hangar.presenters.utils import fillMenuSharedItems, navigateTo
from gui.server_events.bonuses import getNonQuestBonuses
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.missions.packers.bonus import getDefaultBonusPacker
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency
from items import vehicles
from skeletons.gui.game_control import IMapsTrainingController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from maps_training_common.maps_training_constants import VEHICLE_TYPE, VEHICLE_CLASSES_ORDER, SCENARIO_INDEXES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from skeletons.gui.shared.utils import IHangarSpace
from gui.impl.lobby.maps_training.maps_training_base_view import MapsTrainingBaseView
from vehicle_systems.tankStructure import TankNodeNames
from gui.impl.lobby.maps_training.sound_constants import MAPS_TRAINING_SOUND_SPACE

class _MapsTrainingStatesObserver(StateIdsObserver):
    __mapsTrainingCtrl = dependency.descriptor(IMapsTrainingController)

    def __init__(self):
        from gui.impl.lobby.maps_training.states import EntryState
        from gui.impl.lobby.maps_training.states import SelectedState
        super(_MapsTrainingStatesObserver, self).__init__([
         EntryState.STATE_ID,
         SelectedState.STATE_ID])
        self.onNavigationChanged = Event()
        return

    def onEnterState(self, state, event):
        from gui.impl.lobby.maps_training.states import SelectedState
        selectedMap = None
        if state.getStateID() == SelectedState.STATE_ID:
            params = event.params if event is not None else self.__mapsTrainingCtrl.getPageCtx()
            selectedMap = params.get(b'map', b'')
        self.onNavigationChanged(selectedMap)
        return


class MapsTrainingView(MapsTrainingBaseView, IGlobalListener):
    __slots__ = (b'__selectedMap', b'__selectedScenario', b'__ctxVehicleType', b'__ctxSide', b'__ctxShowAnimation', b'__tooltipData', b'__account', b'__mapsConfig', b'__isDataLoaded', b'__blur', b'__blurRectId', b'__packer', b'__tickCallback', b'__preferences', b'__markerPosOffset', b'__finalizationInProgress')
    _TACTICAL_MAPS_CONFIG_PATH = b'scripts/maps_training_tactical_maps.xml'
    _SCENARIO_COUNT = len(VEHICLE_TYPE.ALL_TYPES) * len(VEHICLE_TYPE.ALL_TEAMS)
    _UPDATE_TICK_RATE = 0.1
    _MEDIUM_TANK_OFFSET = 1.26959
    _MAX_MAP_DIFFICULTY = 3
    _DEFAULT_MAP_DIFFICULTY = 3
    _DISABLED_MAP_GROUP_ID = 2
    _COMMON_SOUND_SPACE = MAPS_TRAINING_SOUND_SPACE
    lobbyContext = dependency.descriptor(ILobbyContext)
    itemsCache = dependency.descriptor(IItemsCache)
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, *args, **kwargs):
        super(MapsTrainingView, self).__init__(viewResource=R.views.mono.maps_training.maps_training_page(), viewModel=MapsTrainingViewModel())
        self.__selectedMap = None
        self.__selectedScenario = 0
        self.__ctxVehicleType = b''
        self.__ctxSide = 0
        self.__ctxShowAnimation = False
        self.__tooltipData = {}
        self.__account = BigWorld.player()
        self.__mapsConfig = TacticalMapsConfigReader.readXml(self._TACTICAL_MAPS_CONFIG_PATH)
        self.__isDataLoaded = False
        self.__blur = CachedBlur(blurAnimRepeatCount=1, blurRadius=0.1)
        self.__blurRectId = None
        self.__packer = getDefaultBonusPacker()
        self.__tickCallback = None
        self.__preferences = self.mapsTrainingController.preferences
        self.__markerPosOffset = 0.0
        self.__finalizationInProgress = False
        self.__initFromCtx(kwargs.get(b'ctx', {}))
        self.__lsmObserver = _MapsTrainingStatesObserver()
        return

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.maps_training.scenario_tooltip():
            geometryID = ArenaType.g_geometryNamesToIDs[self.__selectedMap]
            data = self.__account.mapsTraining.getGeometryData(geometryID)
            mapConfig = self.__mapsConfig.getMapConfig(self.__selectedMap)
            scenario = mapConfig.scenarios[int(event.getArgument(b'scenario'))]
            _, vehicleName = self.__getVehicleForScenario(scenario)
            return ScenarioTooltip(scenario.vehicleType, scenario.team, self.__selectedMap, list(self.__getTargets(scenario)), vehicleName, data[scenario.vehicleType][scenario.team][b'completed'], self.__getRewards(geometryID, b'scenarioComplete'))
        return super(MapsTrainingView, self).createToolTipContent(event=event, contentID=contentID)

    def createToolTip(self, event):
        tooltipId = event.getArgument(b'tooltipId', b'')
        if not tooltipId:
            return super(MapsTrainingView, self).createToolTip(event)
        window = backport.BackportTooltipWindow(self.__tooltipData.get(tooltipId), self.getParentWindow())
        window.load()
        return window

    def _getEvents(self):
        return super(MapsTrainingView, self)._getEvents() + (
         (
          self.__lsmObserver.onNavigationChanged, self.__onNavigationChanged),
         (
          self.viewModel.onNavigate, navigateTo),
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onBack, self.__onBack),
         (
          self.viewModel.onSelect, self.__onSelect),
         (
          self.viewModel.onScenarioSelect, self.__onScenarioSelect),
         (
          self.viewModel.onBlurRectUpdated, self.__onBlurRectUpdated),
         (
          self.viewModel.onFilteringChange, self.__filterChangeHandler),
         (
          self.viewModel.onInfoClicked, self.__clickInfoHandler),
         (
          g_currentPreviewVehicle.onChangeStarted, self.__onPreviewVehicleChangeStarted),
         (
          g_currentPreviewVehicle.onChanged, self.__onPreviewVehicleChanged))

    def _onLoading(self, *args, **kwargs):
        super(MapsTrainingView, self)._onLoading(*args, **kwargs)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__lsmObserver)
        Waiting.show(b'loadPage')
        self.__finalizationInProgress = False
        self.mapsTrainingController.requestInitialDataFromServer(self.__fillData)
        return

    def _onLoaded(self, *args, **kwargs):
        super(MapsTrainingView, self)._onLoaded(*args, **kwargs)
        self.__checkCamera()
        self.__updateMenuItems()
        return

    def _finalize(self):
        super(MapsTrainingView, self)._finalize()
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__lsmObserver)
        self.__lsmObserver = None
        self.__finalizationInProgress = True
        self.__blur.fini()
        if self.__tickCallback is not None:
            BigWorld.cancelCallback(self.__tickCallback)
        return

    def __initFromCtx(self, ctx):
        selectedMap = ctx.get(b'map', b'')
        self.__ctxVehicleType = ctx.get(b'vehicleType', b'')
        self.__ctxSide = ctx.get(b'side', 0)
        self.__ctxShowAnimation = ctx.get(b'showAnimation', False)
        self.__selectedMap = selectedMap
        return

    def _removeListeners(self):
        super(MapsTrainingView, self)._removeListeners()
        self.stopGlobalListening()
        return

    def __onNavigationChanged(self, selectedMap):
        self.__blur.disable()
        self.__selectedMap = selectedMap
        self.__selectedScenario = 0
        with self.viewModel.transaction() as model:
            self.__updateAllSelections(model)
        if not selectedMap:
            self.mapsTrainingController.reset()
        g_eventBus.handleEvent(events.FightButtonEvent(events.FightButtonEvent.FIGHT_BUTTON_UPDATE), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __onClose(self):
        self.mapsTrainingController.selectRandomMode()
        return

    def __onBack(self):
        state = getLobbyStateMachine().getStateFromView(self)
        if state:
            state.goBack()
        return

    def __onSelect(self, args):
        from gui.impl.lobby.maps_training.states import SelectedState
        SelectedState.goTo(map=str(args.get(b'id')))
        return

    def __onScenarioSelect(self, args):
        self.__selectedScenario = int(args.get(b'id'))
        with self.viewModel.transaction() as model:
            self.__updateSelectedScenario(model)
        return

    def __updateSelectedMap(self, model):
        isMapSelected = bool(self.__selectedMap)
        model.setIsMapSelected(isMapSelected)
        if isMapSelected:
            mapConfig = self.__mapsConfig.getMapConfig(self.__selectedMap)
            geometryID = ArenaType.g_geometryNamesToIDs[self.__selectedMap]
            data = self.__account.mapsTraining.getGeometryData(geometryID)
            serverConfig = self.mapsTrainingController.getConfig()
            trainingMaps = serverConfig[b'maps']
            mapModel = model.selectedMapModel
            mapModel.setId(self.__selectedMap)
            mapModel.setImage(R.images.gui.maps.icons.map.dyn((b'c_{}').format(self.__selectedMap))())
            mapModel.setGroupId(trainingMaps[geometryID] - 1)
            scenarioModels = mapModel.getScenarios()
            scenarioModels.clear()
            for scenario in mapConfig.scenarios:
                scenarioModel = MapsTrainingScenarioModel()
                scenarioModel.setTeam(scenario.team)
                scenarioModel.setScenarioNum(SCENARIO_INDEXES[scenario.team, scenario.vehicleType])
                scenarioModel.setVehicleType(scenario.vehicleType)
                scenarioModel.setIsComplete(data[scenario.vehicleType][scenario.team][b'completed'])
                scenarioBonuses = self.__getRewards(geometryID, b'scenarioComplete')
                bonusArray = scenarioModel.getRewards()
                self.__fillBonusArray(bonusArray, scenarioBonuses)
                scenarioModels.addViewModel(scenarioModel)

            isNotComplete = any(not data[scenario.vehicleType][scenario.team][b'completed'] for scenario in mapConfig.scenarios)
            mapBonuses = self.__getRewards(geometryID, b'mapComplete')
            finalBonusArray = mapModel.getRewards()
            finalBonusArray.clear()
            if isNotComplete:
                self.__fillBonusArray(finalBonusArray, mapBonuses)
        self.mapsTrainingController.setSelectedMap(self.__selectedMap)
        return

    def __getRewards(self, geometryID, stage):
        config = self.mapsTrainingController.getConfig()
        finalBonuses = []
        mapRewardsConfig = config[b'rewards'][geometryID][stage]
        for rewardName, rewardData in mapRewardsConfig.iteritems():
            finalBonuses.extend(getNonQuestBonuses(rewardName, rewardData))

        return finalBonuses

    def __fillBonusArray(self, bonusArray, bonusesData):
        for bonus in bonusesData:
            bonusList = self.__packer.pack(bonus)
            bonusTooltipList = self.__packer.getToolTip(bonus)
            for bonusIndex, item in enumerate(bonusList):
                item.setIndex(bonusIndex)
                tooltipId = str(len(self.__tooltipData))
                item.setTooltipId(tooltipId)
                bonusArray.addViewModel(item)
                self.__tooltipData[tooltipId] = bonusTooltipList[bonusIndex]

        return

    def __updateSelectedScenario(self, model):
        if not self.__selectedMap:
            return
        mapConfig = self.__mapsConfig.getMapConfig(self.__selectedMap)
        scenario = mapConfig.scenarios[self.__selectedScenario]
        if scenario.team != self.mapsTrainingController.getSelectedTeam():
            self.mapsTrainingController.setSelectedTeam(scenario.team)
        self.__markerPosOffset = self._MEDIUM_TANK_OFFSET if scenario.vehicleType == VEHICLE_TYPE.MEDIUM else 0.0
        vehicle, vehicleName = self.__getVehicleForScenario(scenario)
        if vehicle != self.mapsTrainingController.getSelectedVehicle():
            self.mapsTrainingController.setSelectedVehicle(vehicle)
        elif g_currentPreviewVehicle.intCD != vehicle:
            self.mapsTrainingController.updateSelectedVehicle()
        selectedMapModel = model.selectedMapModel
        selectedMapModel.setSelectedScenario(self.__selectedScenario)
        selectedMapModel.setVehicleName(vehicleName)
        imageResource = R.images.gui.maps.icons.mapsTraining.minimap.scenarios.dyn((b'c_{}_team{}_{}').format(self.__selectedMap, scenario.team, scenario.vehicleType))
        selectedMapModel.setScenarioImage(imageResource() if imageResource.isValid() else R.invalid())
        points = selectedMapModel.getPoints()
        points.clear()
        teamData = mapConfig.teams[scenario.team]
        for teamId, teamForBaseData in mapConfig.teams.iteritems():
            teamPointModel = self.__createPointModel((b'team{}').format(teamId), [], teamForBaseData.isLeft, teamForBaseData.tooltipImage, teamForBaseData.position, MapsTrainingMinimapPoint.POINT_TYPE_BASE if teamId == scenario.team else MapsTrainingMinimapPoint.POINT_TYPE_ENEMY_BASE)
            points.addViewModel(teamPointModel)

        pointsData = teamData.scenarioPoints[scenario.vehicleType]
        for pointData in pointsData:
            pointModel = self.__createPointModel(pointData.id, pointData.textKeys, pointData.isLeft, pointData.tooltipImage, pointData.position, MapsTrainingMinimapPoint.POINT_TYPE_DEFAULT)
            points.addViewModel(pointModel)

        selectedMapModel.setIsShowCompleteAnimation(self.__ctxShowAnimation)
        self.__ctxShowAnimation = False
        return

    @staticmethod
    def __createPointModel(pointId, textKeys, isLeft, tooltipImage, position, pointType):
        pointModel = MapsTrainingMinimapPoint()
        pointModel.setId(pointId)
        textKeysModel = pointModel.getTextKeys()
        for textKey in textKeys:
            textKeysModel.addString(textKey)

        pointModel.setIsLeft(isLeft)
        if tooltipImage:
            pointModel.setIsShowTooltip(True)
            pointModel.setTooltipImage(R.images.gui.maps.icons.mapsTraining.minimap.tooltips.dyn(tooltipImage)())
        pointModel.setPositionX(position.x)
        pointModel.setPositionY(position.y)
        pointModel.setType(pointType)
        return pointModel

    def __getVehicleForScenario(self, scenario):
        configuration = self.mapsTrainingController.getConfig()
        mapId = ArenaType.g_geometryNamesToIDs[self.__selectedMap]
        for vehCompDescr in configuration[b'vehicles'][mapId]:
            vehDescr = vehicles.VehicleDescr(typeID=vehicles.parseIntCompactDescr(vehCompDescr)[1:])
            vehicleData = self.itemsCache.items.getStockVehicle(vehCompDescr)
            if scenario.vehicleType == vehicleData.type:
                return (vehDescr.name, vehicleData.userName)

        return

    def __getTargets(self, scenario):
        goals = self.__getScenarioConfig(scenario.vehicleType, scenario.team)[b'goals']
        for vehCls in VEHICLE_CLASSES_ORDER:
            for _ in xrange(goals[vehCls]):
                yield vehCls

        return

    def __getScenarioConfig(self, vehType, team):
        mapId = ArenaType.g_geometryNamesToIDs[self.__selectedMap]
        config = self.mapsTrainingController.getConfig()
        return config.get(b'scenarios', {}).get(mapId, {}).get(team, {}).get(vehType, {})

    def __filterChangeHandler(self, kwargs):
        incompleteFilter = kwargs.get(b'incomplete', False)
        if incompleteFilter != self.__preferences.incompleteFilter:
            self.__preferences.incompleteFilter = incompleteFilter
            self.__preferences.save()
        titleFilter = kwargs.get(b'title', b'')
        if titleFilter != self.__preferences.titleFilter:
            self.__preferences.titleFilter = titleFilter
        return

    def __clickInfoHandler(self):
        from gui.shared.event_dispatcher import showBrowserOverlayView
        url = GUI_SETTINGS.infoPageMapsTraining
        showBrowserOverlayView(url, VIEW_ALIAS.BROWSER_OVERLAY)
        return

    def __fillData(self):
        configuration = self.mapsTrainingController.getConfig()
        trainingMaps = configuration[b'maps']
        availableMaps = []
        mapIDs = self.lobbyContext.getServerSettings().getPreferredMapsConfig()[b'mapIDs']
        for geometryID in mapIDs:
            if geometryID not in ArenaType.g_geometryCache:
                continue
            geometryType = ArenaType.g_geometryCache[geometryID]
            availableMaps.append(geometryType)

        with self.viewModel.transaction() as model:
            model.setIncompleteFilter(self.__preferences.incompleteFilter)
            model.setTitleFilter(self.__preferences.titleFilter)
            groupArray = model.getGroups()
            groupArray.clear()
            for groupId in range(self._MAX_MAP_DIFFICULTY):
                groupVM = MapsTrainingGroupModel()
                groupArray.addViewModel(groupVM)
                groupVM.setGroupId(groupId)
                groupVM.setGroupTitle(backport.text(R.strings.maps_training.mapSelection.groupTitle.num(groupId)()))
                groupVM.setIsGroupDisabled(groupId == self._DISABLED_MAP_GROUP_ID)

            mapsModel = model.getMaps()
            mapsModel.clear()
            for geometryType in availableMaps:
                slotModel = MapsTrainingMapModel()
                mapName = geometryType.geometryName
                mapId = geometryType.geometryID
                slotModel.setId(mapName)
                slotModel.setIsEnabled(mapId in trainingMaps)
                data = self.__account.mapsTraining.getGeometryData(mapId)
                slotModel.setIsCompleted(data[b'total'] >= self._SCENARIO_COUNT)
                slotModel.setGroupId(trainingMaps.get(mapId, self._DEFAULT_MAP_DIFFICULTY) - 1)
                slotModel.setTitle(R.strings.arenas.dyn((b'c_{}').format(mapName)).name())
                slotModel.setImage(R.images.gui.maps.icons.map.dyn((b'c_{}').format(mapName))())
                mapsModel.addViewModel(slotModel)

            if self.__selectedMap:
                if g_currentPreviewVehicle.isPresent() and self.__tickCallback is None:
                    self.__onPreviewVehicleChanged()
                self.__updateAllSelections(model)
            model.setIsDataLoaded(True)
        self.__isDataLoaded = True
        Waiting.hide(b'loadPage')
        return

    def __updateAllSelections(self, model):
        self.__selectScenario()
        self.__updateSelectedMap(model)
        self.__updateSelectedScenario(model)
        return

    def __selectScenario(self):
        if not self.__selectedMap:
            return
        scenarios = self.__mapsConfig.getMapConfig(self.__selectedMap).scenarios
        if self.__ctxVehicleType and self.__ctxSide:
            self.__selectedScenario = next((index for index, scenario in enumerate(scenarios) if scenario.team == self.__ctxSide and self.__ctxVehicleType == scenario.vehicleType), 0)
            self.__ctxVehicleType = b''
            self.__ctxSide = 0
        else:
            geometryID = ArenaType.g_geometryNamesToIDs[self.__selectedMap]
            data = self.__account.mapsTraining.getGeometryData(geometryID)
            self.__selectedScenario = next((index for index, scenario in enumerate(scenarios) if not data[scenario.vehicleType][scenario.team][b'completed']), 0)
        return

    def __onBlurRectUpdated(self, args):
        viewX, viewY = self.getParentWindow().globalPosition
        blurRect = Math.Vector4(int(args.get(b'left')) + viewX, int(args.get(b'top')) + viewY, int(args.get(b'right')) + viewX, int(args.get(b'bottom')) + viewY)
        if not self.__blur.enabled:
            self.__blur.enable()
        if self.__blurRectId:
            self.__blur.changeRect(self.__blurRectId, blurRect)
        else:
            self.__blurRectId = self.__blur.addRect(blurRect)
        return

    def __onPreviewVehicleChangeStarted(self):
        if self.__tickCallback is not None and not self.__finalizationInProgress:
            BigWorld.cancelCallback(self.__tickCallback)
            self.__tickCallback = None
        return

    def __onPreviewVehicleChanged(self):
        if self.__tickCallback is None and not self.__finalizationInProgress:
            self.__tickCallback = BigWorld.callback(self._UPDATE_TICK_RATE, self.__tick)
        return

    def __updateMarkerPosition(self):
        if self.__selectedMap and self.hangarSpace.spaceInited:
            vehEntity = self.hangarSpace.space.getVehicleEntity()
            if not vehEntity or not vehEntity.model:
                return
            guiNode = vehEntity.model.node(TankNodeNames.GUI)
            mat = Math.Matrix(guiNode)
            markerWorldPos = mat.applyToOrigin()
            markerWorldPos.y += self.__markerPosOffset
            pos = self.worldToScreenPos(markerWorldPos)
            if pos:
                self.viewModel.vehicleMarker.setTop(pos.y)
        return

    def worldToScreenPos(self, worldPos):
        screenWidth, screenHeight = BigWorld.windowSize()
        viewProjMatrix = getViewProjectionMatrix()
        clipPos = viewProjMatrix.applyV4Point(Math.Vector4(worldPos.x, worldPos.y, worldPos.z, 1.0))
        if clipPos.w <= 0.0:
            return None
        else:
            ndcPos = Math.Vector2()
            ndcPos.x = clipPos.x / clipPos.w
            ndcPos.y = clipPos.y / clipPos.w
            if abs(ndcPos.x) > 1.0 or abs(ndcPos.y) > 1.0:
                return None
            halfScreenWidth = screenWidth / 2.0
            halfScreenHeight = screenHeight / 2.0
            screenPosX = halfScreenWidth * (ndcPos.x + 1.0)
            screenPosY = halfScreenHeight * (1.0 - ndcPos.y)
            screenPosY -= min(screenHeight - self.getParentWindow().size[1], screenPosY)
            return Math.Vector2(screenPosX, screenPosY)

    def __tick(self):
        self.__updateMarkerPosition()
        self.__tickCallback = BigWorld.callback(self._UPDATE_TICK_RATE, self.__tick)
        return

    def __checkCamera(self):
        if self.hangarSpace.spaceInited:
            hangarVehicleEntity = self.hangarSpace.space.getVehicleEntity()
            if hangarVehicleEntity and hangarVehicleEntity.state == CameraMovementStates.FROM_OBJECT:
                BigWorld.callback(0, self.__switchCamera)
        return

    def __switchCamera(self):
        ClientSelectableCameraObject.switchCamera()
        if self.__selectedMap:
            g_currentPreviewVehicle.resetAppearance()
            g_currentPreviewVehicle.selectNoVehicle()
            self.mapsTrainingController.updateSelectedVehicle()
        return

    def __updateMenuItems(self):
        with self.viewModel.transaction() as model:
            fillMenuSharedItems(model)
        return
