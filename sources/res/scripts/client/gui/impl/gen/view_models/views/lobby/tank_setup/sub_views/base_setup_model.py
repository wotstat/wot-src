from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.filters_model import FiltersModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.setup_tabs_model import SetupTabsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel

class BaseSetupModel(ViewModel):
    __slots__ = (b'onSlotAction', b'onDealConfirmed', b'onDealCancelled', b'onAutoRenewalChanged', b'onTabChanged', b'onFilterChanged', b'onFilterReset')
    SELECT_SLOT_ACTION = b'select'
    REVERT_SLOT_ACTION = b'undo'
    RETURN_TO_STORAGE_ACTION = b'cancel'
    SWAP_SLOTS_ACTION = b'swap'
    DEMOUNT_SLOT_ACTION = b'demount'
    DEMOUNT_SLOT_FROM_SETUP_ACTION = b'demount_from_setup'
    DEMOUNT_SLOT_FROM_SETUPS_ACTION = b'demount_from_setups'
    DESTROY_SLOT_ACTION = b'destroy'
    SHOW_INFO_SLOT_ACTION = b'show_info'
    UPGRADE_SLOT_ACTION = b'upgrade'
    ADD_ONE_SLOT_ACTION = b'add_one'
    DRAG_AND_DROP_SLOT_ACTION = b'drag_drop'
    DECONSTRUCT_SLOT_ACTION = b'deconstruct'

    def __init__(self, properties=5, commands=7):
        super(BaseSetupModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def filter(self):
        return self._getViewModel(0)

    @staticmethod
    def getFilterType():
        return FiltersModel

    @property
    def dealPanel(self):
        return self._getViewModel(1)

    @staticmethod
    def getDealPanelType():
        return DealPanelModel

    @property
    def tabs(self):
        return self._getViewModel(2)

    @staticmethod
    def getTabsType():
        return SetupTabsModel

    def getSlots(self):
        return self._getArray(3)

    def setSlots(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSlotsType():
        return BaseSlotModel

    def getSyncInitiator(self):
        return self._getNumber(4)

    def setSyncInitiator(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(BaseSetupModel, self)._initialize()
        self._addViewModelProperty(b'filter', FiltersModel())
        self._addViewModelProperty(b'dealPanel', DealPanelModel())
        self._addViewModelProperty(b'tabs', SetupTabsModel())
        self._addArrayProperty(b'slots', Array())
        self._addNumberProperty(b'syncInitiator', 0)
        self.onSlotAction = self._addCommand(b'onSlotAction')
        self.onDealConfirmed = self._addCommand(b'onDealConfirmed')
        self.onDealCancelled = self._addCommand(b'onDealCancelled')
        self.onAutoRenewalChanged = self._addCommand(b'onAutoRenewalChanged')
        self.onTabChanged = self._addCommand(b'onTabChanged')
        self.onFilterChanged = self._addCommand(b'onFilterChanged')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        return
