from CurrentVehicle import g_currentPreviewVehicle
from customization_quests_common import serializeToken
from frameworks.wulf import ViewFlags, ViewSettings
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelStyleProgressionMeta import VehiclePreviewBottomPanelStyleProgressionMeta
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization.progression_styles.stage_switcher_model import SwitcherType
from gui.impl.gen.view_models.views.lobby.vehicle_preview.buying_panel.progression_styles_buying_panel_model import ProgressionStylesBuyingPanelModel
from gui.impl.pub import ViewImpl
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import BattlePassEvent
from helpers import dependency
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared.gui_items import IGuiItemsFactory
from skeletons.gui.shared.utils import IHangarSpace
from shared_utils import first
from gui.shared.gui_items.customization.c11n_helpers import getProgressionStyleCamouflage
import logging
_logger = logging.getLogger(__name__)

class VehiclePreviewBottomPanelStyleProgression(VehiclePreviewBottomPanelStyleProgressionMeta):

    def __init__(self, ctx=None):
        super(VehiclePreviewBottomPanelStyleProgression, self).__init__()
        self.__backAlias = None
        self.__backCallback = None
        self.__styleLevel = None
        self.__ctx = ctx
        return

    def setBackAlias(self, backAlias):
        self.__backAlias = backAlias
        return

    def setBackCallback(self, backCallback):
        self.__backCallback = backCallback
        return

    def setStyleLevel(self, styleLevel):
        self.__styleLevel = styleLevel
        self.__view.setStyleLevel(self.__styleLevel)
        return

    def setAvailableLevel(self, availableLevel):
        self.__view.setAvailableLevel(availableLevel)
        return

    def setCtx(self, ctx):
        self.__view.setCtx(ctx)
        return

    def _makeInjectView(self):
        style = self.__ctx.get(b'style')
        if style and style.isQuestsProgression:
            self.__view = QuestsProgressionStylesBuyingPanelView(flags=ViewFlags.VIEW)
        else:
            self.__view = ProgressionStylesBuyingPanelView(flags=ViewFlags.VIEW)
        return self.__view


class ProgressionStylesBuyingPanelView(ViewImpl):
    __slots__ = (b'__styleLevel', b'__availableLevel', b'__ctx')
    __customizationService = dependency.descriptor(ICustomizationService)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, flags=ViewFlags.VIEW):
        settings = ViewSettings(R.views.lobby.vehicle_preview.buying_panel.VPProgressionStylesBuyingPanel())
        settings.flags = flags
        settings.model = ProgressionStylesBuyingPanelModel()
        self.__styleLevel = None
        self.__availableLevel = None
        self.__ctx = None
        super(ProgressionStylesBuyingPanelView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(ProgressionStylesBuyingPanelView, self).getViewModel()

    def setStyleLevel(self, styleLevel):
        self.__styleLevel = styleLevel
        return

    def setAvailableLevel(self, availableLevel):
        self.__availableLevel = availableLevel
        return

    def setCtx(self, ctx):
        self.__ctx = ctx
        return

    def _initialize(self, *args, **kwargs):
        super(ProgressionStylesBuyingPanelView, self)._initialize(*args, **kwargs)
        self.viewModel.onChange += self.__onChange
        return

    def _onLoading(self, *args, **kwargs):
        super(ProgressionStylesBuyingPanelView, self)._onLoading(*args, **kwargs)
        g_currentPreviewVehicle.onChangeStarted += self.__onVehicleChangeStarted
        g_currentPreviewVehicle.onChanged += self.__onVehicleChanged
        with self.getViewModel().transaction() as model:
            model.setCurrentLevel(1)
            model.setSelectedLevel(1)
        return

    def _onLoaded(self, *args, **kwargs):
        currentLevel = self.__customizationService.getCurrentProgressionStyleLevel()
        with self.getViewModel().transaction() as model:
            model.setCurrentLevel(self.__availableLevel or 1)
            model.setSelectedLevel(currentLevel if self.__styleLevel is None else self.__styleLevel)
            model.setIsReady(True)
        if self.__styleLevel is not None:
            self.__customizationService.changeStyleProgressionLevelPreview(self.__styleLevel)
        style = self.__ctx.get(b'style') if self.__ctx else None
        if style and style.isProgressionRewindEnabled:
            model.setCurrentLevel(style.maxProgressionLevel)
            model.setSelectedLevel(style.maxProgressionLevel)
            model.setNumberOfBullets(style.maxProgressionLevel)
            model.setSwitcherType(SwitcherType.TEXT)
            model.setStyleID(style.id)
            self.__styleLevel = style.maxProgressionLevel
        model.setIsBulletsBeforeCurrentDisabled(False)
        return

    def _finalize(self):
        self.viewModel.onChange -= self.__onChange
        event = BattlePassEvent(BattlePassEvent.ON_PREVIEW_PROGRESSION_STYLE_CLOSE, ctx={b'level': (self.__styleLevel)})
        g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)
        g_currentPreviewVehicle.onChangeStarted -= self.__onVehicleChangeStarted
        g_currentPreviewVehicle.onChanged -= self.__onVehicleChanged
        self.__ctx = None
        super(ProgressionStylesBuyingPanelView, self)._finalize()
        return

    def __onChange(self, *args):
        if args:
            level = args[0].get(b'selectedLevel')
            if level is not None:
                level = int(level)
                with self.viewModel.transaction() as tx:
                    tx.setSelectedLevel(level)
                self.__customizationService.changeStyleProgressionLevelPreview(level)
                self.__styleLevel = level
        return

    def __onVehicleChangeStarted(self):
        entity = self.__hangarSpace.getVehicleEntity()
        if entity and entity.appearance:
            entity.appearance.loadState.unsubscribe(self.__onVehicleLoadFinished, self.__onVehicleLoadStarted)
        return

    def __onVehicleChanged(self):
        entity = self.__hangarSpace.getVehicleEntity()
        if entity and entity.appearance:
            entity.appearance.loadState.subscribe(self.__onVehicleLoadFinished, self.__onVehicleLoadStarted)
        return

    def __onVehicleLoadStarted(self):
        return

    def __onVehicleLoadFinished(self):
        if self.__styleLevel is not None:
            self.__customizationService.changeStyleProgressionLevelPreview(self.__styleLevel)
        return


class QuestsProgressionStylesBuyingPanelView(ViewImpl):
    __slots__ = (b'__currentLevel', b'__availableLevel', b'__maxLevel', b'__ctx')
    __itemsFactory = dependency.descriptor(IGuiItemsFactory)
    __customizationService = dependency.descriptor(ICustomizationService)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    _DEFAULT_MAX_LEVEL = 4

    def __init__(self, flags=ViewFlags.VIEW):
        settings = ViewSettings(R.views.lobby.vehicle_preview.buying_panel.VPProgressionStylesBuyingPanel())
        settings.flags = flags
        settings.model = ProgressionStylesBuyingPanelModel()
        self.__currentLevel = None
        self.__availableLevel = None
        self.__maxLevel = None
        self.__ctx = None
        super(QuestsProgressionStylesBuyingPanelView, self).__init__(settings)
        return

    def setAvailableLevel(self, availableLevel):
        self.__availableLevel = availableLevel
        return

    def setStyleLevel(self, styleLevel):
        self.__currentLevel = styleLevel
        return

    def setCtx(self, ctx):
        self.__ctx = ctx
        return

    @property
    def viewModel(self):
        return super(QuestsProgressionStylesBuyingPanelView, self).getViewModel()

    def getCtxProperty(self, name):
        if self.__ctx:
            return self.__ctx.get(name)
        else:
            return

    def _getEvents(self):
        return (
         (
          g_currentPreviewVehicle.onChangeStarted, self.__onVehicleChangeStarted),
         (
          g_currentPreviewVehicle.onChanged, self.__onVehicleChanged),
         (
          self.viewModel.onChange, self.__onChange))

    def _finalize(self):
        self.__ctx = None
        super(QuestsProgressionStylesBuyingPanelView, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        super(QuestsProgressionStylesBuyingPanelView, self)._onLoading(*args, **kwargs)
        if not self.__ctx:
            _logger.warning(b'[ProgressStyle]: no style context provided to QuestsProgressionStylesBuyingPanelView')
        return

    def _onLoaded(self, *args, **kwargs):
        super(QuestsProgressionStylesBuyingPanelView, self)._onLoaded(*args, **kwargs)
        with self.getViewModel().transaction() as model:
            self.__setCustomizationLevel(self.__currentLevel or 1)
            model.setIsReady(True)
            model.setCurrentLevel(self.__availableLevel or 1)
            model.setSelectedLevel(self.__currentLevel or 1)
            style = self.getCtxProperty(b'style')
            if style:
                self.__maxLevel = self.__getMaxLevel()
                model.setStyleID(style.id)
                model.setNumberOfBullets(self.__maxLevel)
                model.setIsBulletsBeforeCurrentDisabled(False)
                model.setCurrentLevel(self.__availableLevel or 1)
            notificationText = self.getCtxProperty(b'notificationText')
            if notificationText is not None:
                model.setNotificationText(notificationText)
        return

    def __getMaxLevel(self):
        style = self.getCtxProperty(b'style')
        group = self.getCtxProperty(b'progressStyleGroupID')
        if style and group:
            tokenID = serializeToken(style.id, group)
            return len(style.descriptor.questsProgression.getItemsForGroup(tokenID)) - 1
        return self._DEFAULT_MAX_LEVEL

    def __setCustomizationLevel(self, level):
        style = self.getCtxProperty(b'style')
        group = self.getCtxProperty(b'progressStyleGroupID')
        if style and group:
            outfit = self.__getPreviewOutfit(style, group, level)
            self.__customizationService.tryOnOutfit(outfit)
        return

    def __getPreviewOutfit(self, style, group, level):
        camo = getProgressionStyleCamouflage(style.id, group, level)
        if camo is None:
            return camo
        else:
            season = first(style.seasons)
            outfit = style.getOutfit(season)
            outfitComponent = outfit.pack()
            for camoComponent in outfitComponent.camouflages:
                camoComponent.id = camo.id

            outfitComponent = style.descriptor.addPartsToOutfit(season, outfitComponent, outfit.vehicleCD)
            return self.__itemsFactory.createOutfit(component=outfitComponent, vehicleCD=outfit.vehicleCD)

    def __onChange(self, *args):
        if args:
            level = args[0].get(b'selectedLevel')
            if level is not None:
                self.__setCustomizationLevel(int(level))
                self.viewModel.setSelectedLevel(int(level))
                self.__currentLevel = level
        return

    def __onVehicleChangeStarted(self):
        entity = self.__hangarSpace.getVehicleEntity()
        if entity and entity.appearance:
            entity.appearance.loadState.unsubscribe(self.__onVehicleLoadFinished, self.__onVehicleLoadStarted)
        return

    def __onVehicleChanged(self):
        entity = self.__hangarSpace.getVehicleEntity()
        if entity and entity.appearance:
            entity.appearance.loadState.subscribe(self.__onVehicleLoadFinished, self.__onVehicleLoadStarted)
        return

    def __onVehicleLoadStarted(self):
        return

    def __onVehicleLoadFinished(self):
        self.__setCustomizationLevel(self.__currentLevel or 1)
        return
