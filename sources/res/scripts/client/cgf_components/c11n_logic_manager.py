import BigWorld, CGF
from cgf_script.component_meta_class import registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController, IHeroTankController

@registerComponent
class OnC11nAppearComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = b'On Customization appear'
    category = b'C11n'


@registerComponent
class OnC11nHideComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = b'On Customization hide'
    category = b'C11n'


class C11nLogicManager(CGF.ComponentManager):
    __heroTankCtrl = dependency.descriptor(IHeroTankController)
    __platoonController = dependency.descriptor(IPlatoonController)

    def __init__(self):
        super(C11nLogicManager, self).__init__()
        self.__c11nAppearRoots = []
        self.__c11nHideRoots = []
        return

    def destroy(self):
        self.clear()
        return

    def deactivate(self):
        self.clear()
        return

    def clear(self):
        self.__c11nAppearRoots = []
        self.__c11nHideRoots = []
        return

    @onAddedQuery(CGF.GameObject, OnC11nAppearComponent)
    def onAddedAppearDetail(self, gameObject, _):
        self.__c11nAppearRoots.append(gameObject)
        return

    @onRemovedQuery(CGF.GameObject, OnC11nAppearComponent)
    def onRemovedAppearDetail(self, gameObject, _):
        if gameObject in self.__c11nAppearRoots:
            self.__c11nAppearRoots.remove(gameObject)
        return

    @onAddedQuery(CGF.GameObject, OnC11nHideComponent)
    def onAddedDisappearDetail(self, gameObject, _):
        self.__c11nHideRoots.append(gameObject)
        return

    @onRemovedQuery(CGF.GameObject, OnC11nHideComponent)
    def onRemovedHideDetail(self, gameObject, _):
        if gameObject in self.__c11nHideRoots:
            self.__c11nHideRoots.remove(gameObject)
        return

    def __hideOtherTanks(self):
        self.__platoonController.onPlatoonTankVisualizationBlocked(True)
        self.__heroTankCtrl.setHidden(True)
        return

    def __showOtherTanks(self):
        self.__platoonController.onPlatoonTankVisualizationBlocked(False)
        self.__heroTankCtrl.setHidden(False)
        return

    def onC11nEnter(self):
        hManager = CGF.HierarchyManager(self.spaceID)
        for appearRoot in self.__c11nAppearRoots:
            children = hManager.getChildrenIncludingInactive(appearRoot)
            if not children:
                continue
            for child in children:
                child.activate()

        for hideRoot in self.__c11nHideRoots:
            children = hManager.getChildrenIncludingInactive(hideRoot)
            if not children:
                continue
            for child in children:
                child.deactivate()

        BigWorld.callback(0.0, self.__hideOtherTanks)
        return

    def onC11nExit(self):
        hManager = CGF.HierarchyManager(self.spaceID)
        for appearRoot in self.__c11nAppearRoots:
            children = hManager.getChildrenIncludingInactive(appearRoot)
            if not children:
                continue
            for child in children:
                child.deactivate()

        for hideRoot in self.__c11nHideRoots:
            children = hManager.getChildrenIncludingInactive(hideRoot)
            if not children:
                continue
            for child in children:
                child.activate()

        self.__showOtherTanks()
        return
