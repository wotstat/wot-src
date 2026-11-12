import CGF
from helpers import dependency
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery
from new_year.skeletons.new_year import INewYearEnvironmentSwitchController
from new_year.ny_constants import EnvironmentState

@registerComponent
class NyEnvironmentDependentComponent(object):
    editorTitle = b'NY Environment Dependent'
    category = b'New Year'
    dayActive = ComponentProperty(CGFMetaTypes.BOOL, editorName=b'Day', value=True)
    nightActive = ComponentProperty(CGFMetaTypes.BOOL, editorName=b'Night', value=True)
    raccoonActive = ComponentProperty(CGFMetaTypes.BOOL, editorName=b'Raccoon', value=True)

    def __init__(self):
        self.activeEnvironments = []
        self.__initEnvironments()
        return

    def __initEnvironments(self):
        if self.dayActive:
            self.activeEnvironments.append(EnvironmentState.DAY)
        if self.nightActive:
            self.activeEnvironments.append(EnvironmentState.NIGHT)
        if self.raccoonActive:
            self.activeEnvironments.append(EnvironmentState.RACCOON)
        return


class NyEnvironmentDependentManager(CGF.ComponentManager):
    __nyEnvSwitcherController = dependency.descriptor(INewYearEnvironmentSwitchController)

    def activate(self):
        self.__nyEnvSwitcherController.onEnvironmentSwitched += self.__onEnvironmentSwitched
        return

    def deactivate(self):
        self.__nyEnvSwitcherController.onEnvironmentSwitched -= self.__onEnvironmentSwitched
        return

    @onAddedQuery(CGF.GameObject, NyEnvironmentDependentComponent)
    def onAddedEnvDependent(self, root, envComponent):
        if self.__nyEnvSwitcherController.resolvedUserEnvState in envComponent.activeEnvironments:
            self.__activateChildren(root)
        else:
            self.__deactivateChildren(root)
        return

    def __activateChildren(self, root):
        hManager = CGF.HierarchyManager(self.spaceID)
        children = hManager.getChildrenIncludingInactive(root)
        if not children:
            return
        for child in children:
            if not child.isActive():
                child.activate()

        return

    def __deactivateChildren(self, root):
        hManager = CGF.HierarchyManager(self.spaceID)
        children = hManager.getChildrenIncludingInactive(root)
        if not children:
            return
        for child in children:
            if child.isActive():
                child.deactivate()

        return

    def __onEnvironmentSwitched(self):
        newEnv = self.__nyEnvSwitcherController.resolvedUserEnvState
        for root, envComponent in CGF.Query(self.spaceID, (CGF.GameObject, NyEnvironmentDependentComponent)):
            if newEnv in envComponent.activeEnvironments:
                self.__activateChildren(root)
            else:
                self.__deactivateChildren(root)

        return
