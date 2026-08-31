import typing, BigWorld
from frameworks.wulf import ViewSettings, ViewFlags
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_file_view_model import PersonalFileViewModel
from gui.impl.lobby.container_views.base.components import ContainerBase
from gui.impl.lobby.crew.container_vews.common.tankman_info_component import TankmanInfoComponent
from gui.impl.lobby.crew.container_vews.personal_file.components.post_progression_widget_component import PostProgressionWidgetComponent
from gui.impl.lobby.crew.container_vews.personal_file.components.skill_matrix_component import SkillMatrixComponent
from gui.impl.lobby.crew.container_vews.personal_file.context import PersonalFileViewContext
from gui.impl.lobby.crew.container_vews.personal_file.controller import PersonalFileInteractionController
from gui.impl.lobby.crew.personal_case import IPersonalTab
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.shared import IItemsCache
from PlayerEvents import g_playerEvents
if typing.TYPE_CHECKING:
    from typing import List, Type
    from gui.impl.lobby.container_views.base.controllers import InteractionController
    from gui.impl.lobby.container_views.base.components import ComponentBase

class PersonalFileView(ContainerBase, IPersonalTab, ViewImpl):
    __slots__ = (b'__isAnimationShowing', b'__hasPendingRefresh')
    TITLE = backport.text(R.strings.crew.tankmanContainer.tab.personalFile())
    itemsCache = dependency.descriptor(IItemsCache)
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, layoutID=R.views.lobby.crew.personal_case.PersonalFileView(), **kwargs):
        self.__isAnimationShowing = True
        self.__hasPendingRefresh = False
        settings = ViewSettings(layoutID, ViewFlags.LOBBY_TOP_SUB_VIEW, PersonalFileViewModel())
        super(PersonalFileView, self).__init__(settings, **kwargs)
        return

    @property
    def viewModel(self):
        return super(PersonalFileView, self).getViewModel()

    def onChangeTankman(self, tankmanID):
        if tankmanID != self.context.tankman.invID:
            self.__clearAnimationData(self.context.skillAnimationsSkipped)
        if hasattr(self, b'interactionCtrl'):
            self.interactionCtrl.onChangeTankman(tankmanID)
        return

    def _getEvents(self):
        return ((g_playerEvents.onDisconnected, self.__onDisconnected),)

    def onStopAnimations(self):
        BigWorld.player().crewAccountController.setTankmanVeteranAnimanionPlayed(self.context.tankman.invID)
        if hasattr(self, b'interactionCtrl'):
            self.interactionCtrl.onStopAnimations()
        return

    def setAnimationInProgress(self, isEnabled):
        self.getParentView().setAnimationInProgress(isEnabled)
        return

    def hideContent(self):
        self.getParentView().toggleContentVisibility(False)
        return

    def showContent(self):
        self.getParentView().toggleContentVisibility(True)
        return

    def refresh(self):
        if not self.__isAnimationShowing:
            self.__hasPendingRefresh = True
            return
        super(PersonalFileView, self).refresh()
        return

    def _getComponents(self):
        return [
         TankmanInfoComponent(key=b'tankman_info', parent=self),
         SkillMatrixComponent(key=b'skill_matrix', parent=self),
         PostProgressionWidgetComponent(key=b'post_progression', parent=self)]

    def _getContext(self, *args, **kwargs):
        return PersonalFileViewContext(kwargs.get(b'tankmanID'))

    def _getInteractionControllerCls(self):
        return PersonalFileInteractionController

    def _fillViewModel(self, vm):
        vm.setTankmanId(self.context.tankmanID)
        vm.setSkillsEfficiency(self.context.tankman.currentVehicleSkillsEfficiency)
        vm.setIsTankmanInVehicle(self.context.tankman.vehicleDescr is not None)
        hasPostProgression = self.context.tankman.descriptor.isMaxSkillXp()
        vm.setHasPostProgression(hasPostProgression)
        if hasPostProgression:
            vm.setIsPostProgressionAnimated(BigWorld.player().crewAccountController.getTankmanVeteranAnimanion(self.context.tankman.invID))
        return

    def _finalize(self):
        try:
            try:
                self.__clearAnimationData()
            except AttributeError:
                pass

        finally:
            super(PersonalFileView, self)._finalize()

        return

    def __clearAnimationData(self, skipped=False):
        if not skipped:
            BigWorld.player().crewAccountController.clearTankmanAnimanions(self.context.tankman.invID)
        return

    def __onDisconnected(self):
        self.destroyWindow()
        return
