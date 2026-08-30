from __future__ import absolute_import
import BigWorld
from shared_utils import nextTick
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.AmmunitionPanelInjectMeta import AmmunitionPanelInjectMeta
from gui.impl.lobby.tank_setup.ammunition_panel.hangar_view import HangarAmmunitionPanelView
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.system_factory import collectAmmunitionPanelView
from helpers import dependency
from skeletons.gui.game_control import IHangarGuiController

class AmmunitionPanelInject(AmmunitionPanelInjectMeta, IGlobalListener):
    __hangarGuiCtrl = dependency.descriptor(IHangarGuiController)

    def onPrbEntitySwitching(self):
        self.getInjectView().setPrbSwitching(True)
        return

    def onPrbEntitySwitched(self):
        self.__invalidateInjectView()
        return

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        self.getInjectView().update()
        return

    def onHangarSwitchAnimComplete(self, isComplete):
        self.getInjectView().setHangarSwitchAnimState(isComplete)
        return

    def _populate(self):
        super(AmmunitionPanelInject, self)._populate()
        self.addListener(events.AmmunitionInjectEvent.INVALIDATE_INJECT_VIEW, self.__invalidateInjectView, EVENT_BUS_SCOPE.LOBBY)
        return

    def _onPopulate(self):
        self._createInjectView()
        return

    def _dispose(self):
        self.removeListener(events.AmmunitionInjectEvent.INVALIDATE_INJECT_VIEW, self.__invalidateInjectView, EVENT_BUS_SCOPE.LOBBY)
        super(AmmunitionPanelInject, self)._dispose()
        return

    def _makeInjectView(self):
        viewClass = self.__getInjectViewClass()
        return viewClass(flags=ViewFlags.VIEW)

    def _addInjectContentListeners(self):
        super(AmmunitionPanelInject, self)._addInjectContentListeners()
        self.startGlobalListening()
        self.getInjectView().onPanelSectionResized += self.__onPanelSectionResized
        self.getInjectView().onVehicleChanged += self.__onVehicleChanged
        return

    def _removeInjectContentListeners(self):
        super(AmmunitionPanelInject, self)._removeInjectContentListeners()
        self.stopGlobalListening()
        self.getInjectView().onVehicleChanged -= self.__onVehicleChanged
        return

    def __onPanelSectionResized(self, sectionType, offsetX, offsetY, width, height, **kwargs):
        self.as_setHelpLayoutS({b'sectionType': sectionType, 
           b'offsetX': offsetX, 
           b'offsetY': offsetY, 
           b'width': width, 
           b'height': height})
        return

    def __onVehicleChanged(self):
        self.as_clearHelpLayoutS()
        return

    def __getInjectViewClass(self):
        currentPresetGetter = self.__hangarGuiCtrl.sfController.currentPresetGetter
        ammunitionPanelViewCls = collectAmmunitionPanelView(currentPresetGetter.getAmmoInjectViewAlias())
        if ammunitionPanelViewCls is not None:
            return ammunitionPanelViewCls
        else:
            return HangarAmmunitionPanelView

    def __invalidateInjectView(self, *_):
        injectView = self.getInjectView()
        if type(injectView) is self.__getInjectViewClass():
            injectView.update()
        else:
            nextTick(self.__recreateInjectView)()
        return

    def __recreateInjectView(self):
        self._destroyInjected()
        player = BigWorld.player()
        if player is not None:
            self._createInjectView()
        return
