import ArenaType, BigWorld
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.Scaleform.Waiting import Waiting
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_result_model import DoneValueEnum, MapsTrainingResultModel
from gui.impl.pub import ViewImpl, WindowImpl
from gui.shared.missions.packers.bonus import getDefaultBonusPacker
from gui.sounds.filters import switchHangarOverlaySoundFilter
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.game_control import IMapsTrainingController
from PlayerEvents import g_playerEvents
from maps_training_common.maps_training_constants import SCENARIO_INDEXES
from skeletons.gui.shared.utils import IHangarSpace
_SECONDS_IN_MINUTE = 60

class MapsTrainingResult(ViewImpl):
    __slots__ = (b'__arenaUniqueID', b'__isFromNotifications', b'__tooltipData')
    battleResults = dependency.descriptor(IBattleResultsService)
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.maps_training.MapsTrainingResult())
        settings.model = MapsTrainingResultModel()
        settings.args = args
        settings.kwargs = kwargs
        super(MapsTrainingResult, self).__init__(settings)
        self.__arenaUniqueID = kwargs.get(b'arenaUniqueID', None)
        self.__isFromNotifications = kwargs.get(b'isFromNotifications', False)
        self.__tooltipData = {}
        return

    @property
    def viewModel(self):
        return super(MapsTrainingResult, self).getViewModel()

    def createToolTip(self, event):
        tooltipId = event.getArgument(b'tooltipId', b'')
        if not tooltipId:
            return super(MapsTrainingResult, self).createToolTip(event)
        window = backport.BackportTooltipWindow(self.__tooltipData.get(tooltipId), self.getParentWindow())
        window.load()
        return window

    def _onLoading(self, *args, **kwargs):

        def _setResults():
            if self.battleResults.areResultsPosted(self.__arenaUniqueID):
                self.__setBattleResults()
            else:
                Waiting.show(b'stats')
                self.battleResults.onResultPosted += self.__handleBattleResultsPosted
            return

        super(MapsTrainingResult, self)._onLoading(*args, **kwargs)
        switchHangarOverlaySoundFilter(on=True)
        self.mapsTrainingController.requestInitialDataFromServer(_setResults)
        return

    def _initialize(self, *args, **kwargs):
        super(MapsTrainingResult, self)._initialize(*args, **kwargs)
        self.viewModel.setHangarReady(self.hangarSpace.spaceInited)
        self.__addListeners()
        return

    def _finalize(self):
        self.__removeListeners()
        switchHangarOverlaySoundFilter(on=False)
        super(MapsTrainingResult, self)._finalize()
        return

    def __handleBattleResultsPosted(self, reusableInfo, _, __):
        if self.__arenaUniqueID == reusableInfo.arenaUniqueID:
            Waiting.hide(b'stats')
            self.__setBattleResults()
        return

    def __addListeners(self):
        self.viewModel.onClose += self.__onClose
        g_playerEvents.onDisconnected += self.__onDisconnected
        self.hangarSpace.onSpaceCreate += self.__onHangarSpaceCreated
        return

    def __removeListeners(self):
        self.viewModel.onClose -= self.__onClose
        self.battleResults.onResultPosted -= self.__handleBattleResultsPosted
        g_playerEvents.onDisconnected -= self.__onDisconnected
        self.hangarSpace.onSpaceCreate -= self.__onHangarSpaceCreated
        return

    def __onClose(self):
        if not self.__isFromNotifications and self.battleResults.areResultsPosted(self.__arenaUniqueID):
            self.__showMapsTrainingPage()
        self.destroyWindow()
        return

    def __onDisconnected(self):
        self.destroyWindow()
        return

    def __onHangarSpaceCreated(self):
        self.__setHangarReady()
        return

    def __setHangarReady(self):
        if Waiting.isVisible():
            BigWorld.callback(0.1, self.__setHangarReady)
        else:
            self.viewModel.setHangarReady(True)
        return

    def __showMapsTrainingPage(self):
        vo = self.battleResults.getResultsVO(self.__arenaUniqueID)
        mapID = vo[b'geometryId']
        vehicle = vo[b'vehicle']
        team = vo[b'team']
        geometryType = ArenaType.g_geometryCache[mapID]
        self.mapsTrainingController.showMapsTrainingPage(ctx={b'map': (geometryType.geometryName), 
           b'vehicleType': (vehicle[b'type']), 
           b'side': team, 
           b'showAnimation': (vo[b'accountProgress'][b'hasImproved'])})
        return

    def __setBattleResults(self):
        vo = self.battleResults.getResultsVO(self.__arenaUniqueID)
        stats = {i[b'id']: i[b'value'] for i in vo[b'stats']}
        totalTargets, _, _ = vo[b'scenarioProgress'][-1]
        with self.viewModel.transaction() as model:
            self.__addRewards(model, vo)
            geometryID = vo[b'geometryId']
            geometryType = ArenaType.g_geometryCache[geometryID]
            mapName = geometryType.geometryName
            model.setMapID(mapName)
            model.setMapName(R.strings.arenas.dyn((b'c_{}').format(mapName)).name())
            scenarioIndex = SCENARIO_INDEXES[vo[b'team'], vo[b'vehicle'][b'type']]
            model.setSelectedScenario(backport.text(R.strings.maps_training.result.scenario(), scenario=scenarioIndex))
            model.setSelectedVehicleType(R.strings.maps_training.vehicleType.dyn(vo[b'vehicle'][b'type'])())
            model.setTime(self.__getDuration(vo))
            model.setKills(stats[b'questKills'])
            model.setDoneValue(self.__getDoneValue(vo))
            model.setWasDone(vo[b'wasDone'])
            model.setAllTargets(totalTargets)
            vehicleName = vo[b'vehicle'][b'name'].split(b':')[-1].replace(b'-', b'_')
            vehicleImage = R.images.gui.maps.shop.vehicles.c_600x450.dyn(vehicleName)
            if vehicleImage.isValid():
                model.setVehicleImage(vehicleImage())
        return

    def __addRewards(self, model, vo):
        packer = getDefaultBonusPacker()
        tooltipIdx = 0
        rewardsModel = model.getRewards()
        rewardsModel.clear()
        for bonus in vo[b'rewards']:
            bonusList = packer.pack(bonus)
            bonusTooltipList = packer.getToolTip(bonus)
            for bonusIdx, item in enumerate(bonusList):
                item.setIndex(bonusIdx)
                tooltipId = str(tooltipIdx)
                item.setTooltipId(tooltipId)
                rewardsModel.addViewModel(item)
                self.__tooltipData[tooltipId] = bonusTooltipList[bonusIdx]
                tooltipIdx += 1

        return

    @staticmethod
    def __getDoneValue(vo):
        doneValue = vo[b'doneValue']
        if doneValue > 0:
            return DoneValueEnum.DONE
        if doneValue < 0:
            return DoneValueEnum.UNDONE
        return DoneValueEnum.PARTIALDONE

    @staticmethod
    def __getDuration(vo):
        duration = vo[b'duration']
        return (b'{}:{:02d}').format(duration / _SECONDS_IN_MINUTE, duration % _SECONDS_IN_MINUTE)


class MapsTrainingResultWindow(WindowImpl):

    def __init__(self, arenaUniqueID, isFromNotifications):
        super(MapsTrainingResultWindow, self).__init__(wndFlags=WindowFlags.WINDOW_FULLSCREEN | WindowFlags.WINDOW, content=MapsTrainingResult(arenaUniqueID=arenaUniqueID, isFromNotifications=isFromNotifications), layer=WindowLayer.TOP_WINDOW)
        return
