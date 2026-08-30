from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.impl.battle.battle_page.carousel.prebattle_carousel_view import PrebattleCarouselView
from gui.Scaleform.daapi.view.meta.PrebattleCarouselViewMeta import PrebattleCarouselViewMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import hasAliveInject
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared.utils.MethodsRules import MethodsRules
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class PrebattleCarouselInject(MethodsRules, PrebattleCarouselViewMeta, IAbstractPeriodView):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __slots__ = (b'__isViewLoaded', b'__isViewActive', b'__closeOnFullStatsClose', b'__isFullStatsShown')

    def __init__(self):
        super(PrebattleCarouselInject, self).__init__()
        self.__isViewLoaded = False
        self.__isViewActive = False
        self.__closeOnFullStatsClose = False
        self.__isFullStatsShown = False
        return

    @property
    def isActive(self):
        return self.__isViewActive and self.__isViewLoaded

    def onViewIsHidden(self):
        self.__isViewActive = False
        self._destroyInjected()
        return

    @MethodsRules.delayable()
    def showView(self, *_, **__):
        if self.__isViewActive:
            return
        self.as_showS()
        self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.PREBATTLE_CAROUSEL_VIEW, enableAiming=False)
        self._createInjectView()
        self.__isViewActive = True
        return

    @hasAliveInject(deadUnexpected=True)
    def hideView(self):
        self._hideView()
        return

    def setCountdown(self, state, timeLeft):
        return

    def hideCountdown(self, state, _):
        return

    def _populate(self):
        super(PrebattleCarouselInject, self)._populate()
        self.addListener(events.GameEvent.FULL_STATS, self._handleToggleFullStats, scope=EVENT_BUS_SCOPE.BATTLE)
        prbController = self.__sessionProvider.dynamic.comp7PrebattleSetup
        if prbController:
            prbController.onSelectionConfirmed += self.__onSelectionConfirmed
            prbController.onBattleStarted += self.__onBattleStarted
            prbController.onVehicleChanged += self.__onVehicleUpdated
        return

    def _onPopulate(self):
        return

    def _dispose(self):
        self.removeListener(events.GameEvent.FULL_STATS, self._handleToggleFullStats, scope=EVENT_BUS_SCOPE.BATTLE)
        prbController = self.__sessionProvider.dynamic.comp7PrebattleSetup
        if prbController:
            prbController.onSelectionConfirmed -= self.__onSelectionConfirmed
            prbController.onBattleStarted -= self.__onBattleStarted
            prbController.onVehicleChanged -= self.__onVehicleUpdated
        self._destroyInjected()
        self.clear()
        self.__isViewActive = False
        super(PrebattleCarouselInject, self)._dispose()
        return

    def _handleToggleFullStats(self, event):
        isFullStatsShown = event.ctx[b'isDown']
        self.__isFullStatsShown = isFullStatsShown
        if not isFullStatsShown and self.__closeOnFullStatsClose:
            self._hideView(useAnim=False)
            self.__closeOnFullStatsClose = False
        return

    def _hideView(self, useAnim=True):
        self.__isViewActive = False
        self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.PREBATTLE_CAROUSEL_VIEW)
        self.as_hideS(useAnim)
        return

    def _makeInjectView(self, *args):
        return PrebattleCarouselView(*args)

    def _addInjectContentListeners(self):
        self._injectView.onViewLoaded += self.__onViewLoaded
        return

    def _removeInjectContentListeners(self):
        self._injectView.onViewLoaded -= self.__onViewLoaded
        return

    def __onSelectionConfirmed(self):
        self._hideView()
        return

    def __onBattleStarted(self):
        if self.__isFullStatsShown:
            self.__closeOnFullStatsClose = True
        else:
            self._hideView()
        return

    def __onVehicleUpdated(self, vehicle):
        if self.__isPrebattleSwitchPossible() and not self.__isViewLoaded:
            self.showView(vehicle, True)
        return

    def __isPrebattleSwitchPossible(self):
        return not self.__sessionProvider.dynamic.comp7PrebattleSetup.isSelectionConfirmed()

    def __onViewLoaded(self):
        self.__isViewLoaded = True
        return
