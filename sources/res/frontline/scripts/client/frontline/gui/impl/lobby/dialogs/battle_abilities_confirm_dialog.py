from frameworks.wulf import ViewSettings
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView
from gui.impl.gen import R
from frontline.gui.impl.gen.view_models.views.lobby.dialogs.battle_abilities_confirm_dialog_model import BattleAbilitiesConfirmDialogModel
from gui.impl.pub.dialog_window import DialogButtons
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from PlayerEvents import g_playerEvents

class BattleAbilitiesConfirmDialog(FullScreenDialogBaseView):
    __epicMetaGameCtrl = dependency.descriptor(IEpicBattleMetaGameController)
    __slots__ = (b'__skillsInteractor', b'__vehicleType', b'__isCloseButtonClicked')
    LAYOUT_ID = R.views.frontline.mono.lobby.dialogs.battle_abilities_confirm_dialog()

    def __init__(self, skillsInteractor, vehicleType=b''):
        settings = ViewSettings(layoutID=self.LAYOUT_ID, model=BattleAbilitiesConfirmDialogModel())
        super(BattleAbilitiesConfirmDialog, self).__init__(settings)
        self.__skillsInteractor = skillsInteractor
        self.__vehicleType = vehicleType
        self.__isCloseButtonClicked = False
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(BattleAbilitiesConfirmDialog, self)._onLoading(*args, **kwargs)
        self._fillViewModel()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onCheckBoxClick, self._onCheckBoxClick),
         (
          self.viewModel.onSubmitClick, self._onSubmitClick),
         (
          self.viewModel.onCloseClick, self._onCloseClick),
         (
          self.viewModel.onCancelClick, self._onCancelClick),
         (
          g_playerEvents.onAccountBecomeNonPlayer, self.destroyWindow))

    def _fillViewModel(self):
        price = 0
        epicSkills = self.__epicMetaGameCtrl.getEpicSkills()
        skills = [epicSkills[item.innationID] for item in self.__skillsInteractor.getChangedList()]
        isMultipleAbilities = len(skills) > 1
        with self.viewModel.transaction() as vm:
            icons = vm.getIcons()
            names = vm.getNames()
            icons.clear()
            names.clear()
            icons.invalidate()
            names.invalidate()
            for skill in skills:
                skillInfo = skill.getSkillInfo()
                icons.addString(skillInfo.icon)
                names.addString(skillInfo.name)
                if not isMultipleAbilities:
                    vm.setSelectedSkillName(skillInfo.name)
                if not skill.isActivated:
                    price += skill.price

            vm.setIsTypeSelected(self.__skillsInteractor.getCheckboxState())
            vm.setPrice(price)
            vm.setIsBuy(price > 0)
            vm.setIsEnoughMoney(self.__epicMetaGameCtrl.getSkillPoints() >= price)
            vm.setIsMultipleAbilities(isMultipleAbilities)
            vm.setVehicleType(self.__vehicleType)
            vm.setBonus(self.__epicMetaGameCtrl.getRandomReservesBonusProbability())
        return

    def _getAdditionalData(self):
        return {b'rollBack': (not self.__isCloseButtonClicked), b'applyForAllOfType': (self.__skillsInteractor.getCheckboxState())}

    def _onCheckBoxClick(self):
        state = not self.viewModel.getIsTypeSelected()
        self.__skillsInteractor.setCheckboxState(state)
        self._fillViewModel()
        return

    def _onSubmitClick(self):
        self._setResult(DialogButtons.SUBMIT)
        return

    def _onCancelClick(self):
        self._setResult(DialogButtons.CANCEL)
        return

    def _onCloseClick(self):
        self.__isCloseButtonClicked = True
        self._setResult(DialogButtons.CANCEL)
        return
