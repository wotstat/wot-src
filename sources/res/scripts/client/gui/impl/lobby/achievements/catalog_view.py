from functools import partial
import typing
from PlayerEvents import g_playerEvents
from advanced_achievements_client.constants import TROPHIES_ACHIEVEMENT_ID
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleCDForStyle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl.gen import R
from gui.impl.gui_decorators import args2params
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.catalog_view_model import CatalogViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.breadcrumb_model import BreadcrumbModel
from gui.impl.lobby.achievements.profile_utils import fillDetailsModel, fillBreadcrumbModel, fillAchievementCardModel, getTrophiesData, createBackportTooltipDecorator, createTooltipContentDecorator
from gui.shared.event_dispatcher import showAdvancedAchievementsCatalogView, showAdvancedAchievementsView, showStylePreview, showAnimatedDogTags, showVehicleHubModules
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from skeletons.gui.game_control import IAchievementsController
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.app_loader import IAppLoader
from uilogging.advanced_achievement.logger import AdvancedAchievementLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementViewKey, AdvancedAchievementButtons
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_SOUND_SPACE
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.details_model import DetailsModel

class CatalogView(ViewImpl):
    __slots__ = (b'__tooltipData', b'__closeCallback', b'__breadcrumbAchievementIDs', b'__achievementCategory', b'__uiLogging', b'__uiParentScreen', b'__mainViewCallback')
    __achievementsController = dependency.descriptor(IAchievementsController)
    __customizationService = dependency.descriptor(ICustomizationService)
    __appLoader = dependency.descriptor(IAppLoader)
    _COMMON_SOUND_SPACE = ACHIEVEMENTS_SOUND_SPACE

    def __init__(self, initAchievementIDs, achievementCategory, closeCallback, uiParentScreen, mainViewCallback=None, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.achievements.CatalogView())
        settings.flags = ViewFlags.VIEW
        settings.model = CatalogViewModel()
        settings.args = args
        settings.kwargs = kwargs
        self.__tooltipData = {}
        self.__achievementCategory = achievementCategory
        self.__closeCallback = closeCallback
        self.__breadcrumbAchievementIDs = initAchievementIDs
        self.__uiParentScreen = uiParentScreen
        self.__uiLogging = AdvancedAchievementLogger(AdvancedAchievementViewKey.CATALOG)
        self.__mainViewCallback = mainViewCallback
        super(CatalogView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(CatalogView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onBreadcrumbClick, self.__onBreadcrumbClick),
         (
          self.viewModel.onCatalogClick, self.__onCatalogClick),
         (
          self.viewModel.onStylePreview, self.__onStylePreview),
         (
          self.viewModel.onPurchaseVehicleClick, self.__onPurchaseVehicleClick),
         (
          self.viewModel.onCardClick, self.__onCardClick),
         (
          self.viewModel.onHintClose, self.__onHintClose),
         (
          self.viewModel.onCardHover, self.__onCardHover),
         (
          self.viewModel.onDogTagPreview, self.__onDogTagPreview),
         (
          g_playerEvents.onDisconnected, self.destroyWindow))

    @createTooltipContentDecorator(AdvancedAchievementViewKey.CATALOG)
    def createToolTipContent(self, event, contentID):
        return

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(CatalogView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def _onLoading(self, *args, **kwargs):
        self.__updatePage()
        self.viewModel.setIsNeededShowHint(self.__achievementsController.getShowHint())
        super(CatalogView, self)._onLoading(*args, **kwargs)
        return

    def _onLoaded(self, *args, **kwargs):
        Waiting.hide(b'loadPage')
        self.__uiLogging.onViewOpen(AdvancedAchievementViewKey.CATALOG, parentScreen=self.__uiParentScreen)
        super(CatalogView, self)._onLoaded(*args, **kwargs)
        return

    def _finalize(self):
        Waiting.hide(b'loadPage')
        self.__breadcrumbAchievementIDs = None
        super(CatalogView, self)._finalize()
        return

    def __updatePage(self):
        self.__tooltipData.clear()
        with self.viewModel.transaction() as model:
            self.__updateAchievementScore(model)
            self.__updateBreadcrumbs(model)
            self.__updateAchievements(model)
        return

    def __updateAchievementScore(self, model):
        model.setAchievementScore(self.__achievementsController.getCurrentScore())
        model.setMaxAchievementsScore(self.__achievementsController.getTotalScore())
        return

    def __updateBreadcrumbs(self, model):
        breadcrumbs = model.getBreadcrumbs()
        breadcrumbs.clear()
        for achievementID in self.__breadcrumbAchievementIDs:
            if achievementID == TROPHIES_ACHIEVEMENT_ID:
                trophiesData = getTrophiesData()
                breadcrumbModel = BreadcrumbModel()
                breadcrumbModel.setAchievementId(TROPHIES_ACHIEVEMENT_ID)
                breadcrumbModel.setKey(trophiesData[b'key'])
                breadcrumbs.addViewModel(breadcrumbModel)
            else:
                breadcrumbs.addViewModel(fillBreadcrumbModel(self.__achievementsController.getAchievementByID(achievementID, self.__achievementCategory)))

        breadcrumbs.invalidate()
        return

    def __updateAchievements(self, model):
        descriptionAchievementID = self.__breadcrumbAchievementIDs[-1]
        if descriptionAchievementID == TROPHIES_ACHIEVEMENT_ID:
            self.__updateTrophiesDescription(model)
            self.__updateAchievementsList(model, self.__achievementsController.getTrophiesAchievements())
        else:
            descriptionAchievement = self.__achievementsController.getAchievementByID(descriptionAchievementID, self.__achievementCategory)
            self.__updateDescription(model, descriptionAchievement)
            self.__updateAchievementsList(model, descriptionAchievement.getChildsIterator())
        return

    def __updateDescription(self, model, descriptionAchievement):
        fillDetailsModel(descriptionAchievement, self.__tooltipData, model.details)
        return

    def __updateTrophiesDescription(self, model):
        detailsModel = model.details
        trophiesData = getTrophiesData()
        detailsModel.setType(trophiesData[b'type'])
        detailsModel.setBackground(trophiesData[b'background'])
        detailsModel.setKey(trophiesData[b'key'])
        detailsModel.setIconPosition(trophiesData[b'iconPosition'])
        detailsModel.setIsTrophy(trophiesData[b'isTrophy'])
        return

    def __updateAchievementsList(self, model, achievements):
        with model.getAchievementsList().transaction() as achievementsList:
            achievementsList.clear()
            for achievement in achievements:
                bubbleCount = self.__getAchievementBubbles(achievement)
                achievementsList.addViewModel(fillAchievementCardModel(achievement, self.__tooltipData, bubbleCount))

        return

    def __getAchievementBubbles(self, achievement):
        descriptionAchievementID = self.__breadcrumbAchievementIDs[-1]
        if descriptionAchievementID == TROPHIES_ACHIEVEMENT_ID:
            if achievement.getID() not in self.__achievementsController.getSeenTrophiesAdvancedAchievements(achievement.getCategory()):
                return 1
            return 0
        return self.__achievementsController.getUnseenAdvancedAchievementsCount(achievement.getCategory(), achievement.getID())

    def __navigateToBreadcrumb(self, achievementID):
        while self.__breadcrumbAchievementIDs[-1] != achievementID:
            self.__breadcrumbAchievementIDs.pop()

        return

    def __addBreadcrumb(self, achievementID):
        self.__breadcrumbAchievementIDs.append(achievementID)
        return

    def __onClose(self):
        self.__closeCallback()
        self.destroyWindow()
        return

    def __onBreadcrumbClick(self, args):
        self.__navigateToBreadcrumb(int(args[b'achievementId']))
        self.__updatePage()
        return

    def __onCatalogClick(self):
        self.__uiLogging.logClick(AdvancedAchievementButtons.CATALOG)
        showAdvancedAchievementsView(closeCallback=self.__mainViewCallback)
        self.destroyWindow()
        return

    def __onStylePreview(self, args):
        style = self.__customizationService.getItemByID(GUI_ITEM_TYPE.STYLE, int(args[b'id']))
        styledVehicleCD = getVehicleCDForStyle(style)
        showStylePreview(styledVehicleCD, style, backCallback=_getPreviewCallback(self.__appLoader, self.__breadcrumbAchievementIDs, self.__achievementCategory, self.__closeCallback, AdvancedAchievementViewKey.CATALOG))
        self.destroyWindow()
        return

    @args2params(int)
    def __onPurchaseVehicleClick(self, intCD):
        showVehicleHubModules(intCD)
        self.destroyWindow()
        return

    def __onCardClick(self, args):
        self.__uiLogging.logCardClick(int(args[b'achievementId']), args[b'category'])
        self.__addBreadcrumb(int(args[b'achievementId']))
        self.__updatePage()
        return

    def __onHintClose(self):
        self.__achievementsController.setShowHint(False)
        self.viewModel.setIsNeededShowHint(False)
        return

    def __onCardHover(self, args):
        achievementId = int(args[b'achievementId'])
        category = args[b'achievementCategory']
        if self.__breadcrumbAchievementIDs[-1] == TROPHIES_ACHIEVEMENT_ID:
            if achievementId not in self.__achievementsController.getSeenTrophiesAdvancedAchievements(category):
                self.__achievementsController.seeUnseenTrophiesAdvancedAchievement(category, achievementId)
                with self.viewModel.transaction() as model:
                    self.__updateAchievements(model)
        elif achievementId in self.__achievementsController.getUnseenAdvancedAchievements(category):
            self.__achievementsController.seeUnseenAdvancedAchievement(category, achievementId)
            with self.viewModel.transaction() as model:
                self.__updateAchievements(model)
        return

    def __onDogTagPreview(self, args):
        self.__uiLogging.logClick(AdvancedAchievementButtons.DOG_TAG_PREVIEW)
        showAnimatedDogTags(args[b'backgroundId'], args[b'engravingId'])
        self.destroyWindow()
        return


class CatalogViewWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, initAchievementIDs, achievementCategory, closeCallback, uiParentScreen, parent=None, *args, **kwargs):
        super(CatalogViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW_FULLSCREEN, content=CatalogView(initAchievementIDs=initAchievementIDs, achievementCategory=achievementCategory, closeCallback=closeCallback, uiParentScreen=uiParentScreen, *args, **kwargs), parent=parent, layer=WindowLayer.FULLSCREEN_WINDOW)
        return


def _getPreviewCallback(appLoader, initAchievementIDs, achievementCategory, closeCallback, parentScreen):

    def backToCatalog(appLoader, initAchievementIDs, achievementCategory, closeCallback, parentScreen):
        containerManager = appLoader.getApp().containerManager
        stylePreview = containerManager.getViewByKey(ViewKey(VIEW_ALIAS.STYLE_PREVIEW))
        if stylePreview is not None:
            stylePreview.destroy()
        showAdvancedAchievementsCatalogView(initAchievementIDs, achievementCategory, closeCallback, parentScreen)
        return

    return partial(backToCatalog, appLoader, initAchievementIDs, achievementCategory, closeCallback, parentScreen)
