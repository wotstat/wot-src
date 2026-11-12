import CGF
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from new_year.skeletons.new_year import INewYearSurpriseMachine, INewYearCurrencyController
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyType
from new_year.ny_constants import NySurpriseMachineStates, ViewAliases
from cgf_components.hover_component import SelectionComponent, IsHoveredComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from skeletons.gui.impl import INewYearNavigation
from GenericComponents import AnimatorComponent
from Sound import Sound2DComponent
from helpers import dependency

@registerComponent
class NyInteractiveGroup(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'NY Interactive Group'
    category = b'New Year'
    kind = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Kind', value=NySurpriseMachineStates.MACHINE, annotations={b'comboBox': {(NySurpriseMachineStates.MACHINE): (NySurpriseMachineStates.MACHINE), 
                     (NySurpriseMachineStates.BUTTONS): (NySurpriseMachineStates.BUTTONS)}})


@registerComponent
class NyMachineActivationComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'NY Machine Activator'
    category = b'New Year'
    highlightSound = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Highlight Sound', value=Sound2DComponent)
    __nyMachineController = dependency.descriptor(INewYearSurpriseMachine)

    def clickAction(self):
        self.__nyMachineController.tryActivateMachine()
        return

    def playHighlight(self):
        self.highlightSound().play()
        return


class NewYearMachineActivatorManager(CGF.ComponentManager):
    __nyMachineController = dependency.descriptor(INewYearSurpriseMachine)
    __newYearNavigation = dependency.descriptor(INewYearNavigation)

    def activate(self):
        self.__nyMachineController.onUpdateApplyCoin += self.__syncInteractive
        self.__nyMachineController.onActivationChanged += self.__syncInteractive
        self.__nyMachineController.onMachineBusyStatusUpdated += self.__syncInteractive
        self.__newYearNavigation.onChangeView += self.__syncInteractive
        self.__syncInteractive()
        return

    def deactivate(self):
        self.__nyMachineController.onUpdateApplyCoin -= self.__syncInteractive
        self.__nyMachineController.onActivationChanged -= self.__syncInteractive
        self.__nyMachineController.onMachineBusyStatusUpdated -= self.__syncInteractive
        self.__newYearNavigation.onChangeView -= self.__syncInteractive
        return

    @onAddedQuery(NyMachineActivationComponent, SelectionComponent)
    def handleBtnClickAdded(self, machineActComp, selectComp):
        selectComp.onClickAction += machineActComp.clickAction
        return

    @onRemovedQuery(NyMachineActivationComponent, SelectionComponent)
    def handleBtnClickRemoved(self, machineActComp, selectComp):
        selectComp.onClickAction -= machineActComp.clickAction
        return

    @onAddedQuery(NyMachineActivationComponent, IsHoveredComponent)
    def onHoverEnter(self, machineActComp, *_):
        machineActComp.playHighlight()
        self.__nyMachineController.onMachineButtonHovered(True)
        return

    @onRemovedQuery(NyMachineActivationComponent, IsHoveredComponent)
    def onHoverLeave(self, *_):
        self.__nyMachineController.onMachineButtonHovered(False)
        return

    def __syncInteractive(self, *args):
        inView = self.__newYearNavigation.getCurrentViewName() == ViewAliases.SURPRISE_MACHINE_VIEW
        canApply = self.__nyMachineController.canApplyCoin
        busy = self.__nyMachineController.isMachineBusy
        activated = self.__nyMachineController.isMachineActivated
        enable = inView and not activated and canApply and not busy
        if not enable:
            self.__nyMachineController.onMachineButtonHovered(False)
        setGroups(self.spaceID, NySurpriseMachineStates.MACHINE, enable)
        return


@registerComponent
class NyCustomButtonComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'NY Machine Push Button'
    category = b'New Year'
    highlightSound = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Highlight Sound', value=Sound2DComponent)
    animator = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Animator', value=AnimatorComponent)
    __nyMachineController = dependency.descriptor(INewYearSurpriseMachine)
    __nyCurrencyController = dependency.descriptor(INewYearCurrencyController)
    PRESS_ANIM = b'onButtonPress'
    CAN_APPLY_COIN_ANIM = b'canApplyCoin'

    def clickAction(self):
        if not self.__nyMachineController.canApplyCoin:
            return
        self.__nyMachineController.onMachineButtonPress()
        self.animator().startLayerByName(self.PRESS_ANIM)
        return

    def handleApplyCoinAnimation(self):
        currency = self.__nyCurrencyController.getGiftMachineTokenCount
        if currency > 0:
            if not self.animator().isPlaying():
                self.animator().startLayerByName(self.CAN_APPLY_COIN_ANIM)
        else:
            self.animator().stopLayerByName(self.CAN_APPLY_COIN_ANIM)
        return

    def playHighlight(self):
        self.highlightSound().play()
        return


class NewYearMachineButtonsManager(CGF.ComponentManager):
    __nyMachineController = dependency.descriptor(INewYearSurpriseMachine)
    __nyCurrencyController = dependency.descriptor(INewYearCurrencyController)
    __newYearNavigation = dependency.descriptor(INewYearNavigation)

    def activate(self):
        self.__nyMachineController.onUpdateApplyCoin += self.__syncInteractive
        self.__nyMachineController.onActivationChanged += self.__syncInteractive
        self.__nyMachineController.onMachineBusyStatusUpdated += self.__syncInteractive
        self.__nyCurrencyController.onCurrencyUpdated += self.__onCurrencyUpdated
        self.__newYearNavigation.onChangeView += self.__syncInteractive
        self.__updateCurrency()
        self.__syncInteractive()
        return

    def deactivate(self):
        self.__nyMachineController.onUpdateApplyCoin -= self.__syncInteractive
        self.__nyMachineController.onActivationChanged -= self.__syncInteractive
        self.__nyMachineController.onMachineBusyStatusUpdated -= self.__syncInteractive
        self.__nyCurrencyController.onCurrencyUpdated -= self.__onCurrencyUpdated
        self.__newYearNavigation.onChangeView -= self.__syncInteractive
        return

    @onAddedQuery(NyCustomButtonComponent, SelectionComponent)
    def handleBtnClickAdded(self, btnComp, selectComp):
        selectComp.onClickAction += btnComp.clickAction
        return

    @onRemovedQuery(NyCustomButtonComponent, SelectionComponent)
    def handleBtnClickRemoved(self, btnComp, selectComp):
        selectComp.onClickAction -= btnComp.clickAction
        return

    @onAddedQuery(NyCustomButtonComponent, IsHoveredComponent)
    def onHoverEnter(self, btnComp, *_):
        btnComp.playHighlight()
        self.__nyMachineController.onMachineButtonHovered(True)
        return

    @onRemovedQuery(NyCustomButtonComponent, IsHoveredComponent)
    def onHoverLeave(self, *_):
        self.__nyMachineController.onMachineButtonHovered(False)
        return

    def __syncInteractive(self, *args):
        inView = self.__newYearNavigation.getCurrentViewName() == ViewAliases.SURPRISE_MACHINE_VIEW
        canApply = self.__nyMachineController.canApplyCoin
        busy = self.__nyMachineController.isMachineBusy
        activated = self.__nyMachineController.isMachineActivated
        enable = inView and activated and canApply and not busy
        if not enable:
            self.__nyMachineController.onMachineButtonHovered(False)
        setGroups(self.spaceID, NySurpriseMachineStates.BUTTONS, enable)
        return

    def __onCurrencyUpdated(self, currency, _):
        if currency == NyCurrencyType.NYGIFTMACHINETOKEN:
            self.__updateCurrency()
        return

    def __updateCurrency(self):
        for btnComp in CGF.Query(self.spaceID, NyCustomButtonComponent):
            btnComp.handleApplyCoinAnimation()

        return


def setGroups(spaceID, kind, enable):
    hierarchyManager = CGF.HierarchyManager(spaceID)
    for go, grp in CGF.Query(spaceID, (CGF.GameObject, NyInteractiveGroup)):
        if grp.kind != kind:
            continue
        for child in hierarchyManager.getChildrenIncludingInactive(go):
            if enable:
                child.activate()
            else:
                child.deactivate()

    return
