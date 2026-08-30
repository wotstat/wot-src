from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.lobby.tank_setup.sub_views.base_setup import BaseSetupSubView

class CompareBaseSetupSubView(BaseSetupSubView):
    __slots__ = ()

    def revertItem(self, slotID):
        self._interactor.changeSlotItem(slotID, None)
        return

    def _addListeners(self):
        super(CompareBaseSetupSubView, self)._addListeners()
        self._addSlotAction(BaseSetupModel.SELECT_SLOT_ACTION, self._onSelectItem)
        self._addSlotAction(BaseSetupModel.REVERT_SLOT_ACTION, self._onRevertItem)
        self._addSlotAction(BaseSetupModel.RETURN_TO_STORAGE_ACTION, self._onRevertItem)
        self._addSlotAction(BaseSetupModel.SWAP_SLOTS_ACTION, self._onSwapSlots)
        return

    def _onSelectItem(self, args):
        itemCD = int(args.get(b'intCD'))
        currentSlotID = int(args.get(b'currentSlotId', self._curSlotID))
        self._selectItem(currentSlotID, itemCD)
        return

    def _selectItem(self, slotID, item):
        self._interactor.changeSlotItem(slotID, item)
        return

    def _onSwapSlots(self, args):
        slotID = int(args.get(b'installedSlotId'))
        currentSlotID = int(args.get(b'currentSlotId', self._curSlotID))
        self._swapSlots(currentSlotID, slotID)
        return

    def _swapSlots(self, currentSlotID, slotID):
        self._interactor.swapSlots(currentSlotID, slotID)
        return

    def _onRevertItem(self, args):
        slotID = int(args.get(b'installedSlotId'))
        self.revertItem(slotID)
        return
