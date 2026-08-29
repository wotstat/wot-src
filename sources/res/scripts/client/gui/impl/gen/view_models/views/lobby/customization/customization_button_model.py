from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_sub_button_model import CustomizationSubButtonModel

class ButtonActionType(Enum):
    CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_PARTS = b'apply_all_parts'
    CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS = b'apply_all_seasons'
    CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS_ALERT = b'apply_all_seasons_alert'
    CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_SEASONS = b'remove_all_seasons'
    CUSTOMIZATION_SHEET_ACTION_REMOVE_ONE = b'remove_one'
    CUSTOMIZATION_SHEET_ACTION_COLOR_CHANGE = b'color_change'
    CUSTOMIZATION_SHEET_ACTION_SCALE_CHANGE = b'scale_change'
    CUSTOMIZATION_SHEET_RENT_PROLONG = b'rent_prolong'
    CUSTOMIZATION_SHEET_RENT_NOT_PROLONG = b'rent_not_prolong'
    CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_PARTS = b'remove_from_all_parts'
    CUSTOMIZATION_SHEET_ACTION_CLOSE = b'action_close'
    CUSTOMIZATION_SHEET_ACTION_HORIZONZONTAL_MIRROR_RIGHT = b'horizontal_mirror_right'
    CUSTOMIZATION_SHEET_ACTION_HORIZONZONTAL_MIRROR_LEFT = b'horizontal_mirror_left'
    CUSTOMIZATION_SHEET_ACTION_VERTICAL_MIRROR_UP = b'vertical_mirror_up'
    CUSTOMIZATION_SHEET_ACTION_VERTICAL_MIRROR_DOWN = b'vertical_mirror_down'
    CUSTOMIZATION_SHEET_ACTION_MIRROR_LEFT_UP = b'mirror_left_up'
    CUSTOMIZATION_SHEET_ACTION_MIRROR_RIGHT_UP = b'mirror_right_up'
    CUSTOMIZATION_SHEET_ACTION_MIRROR_LEFT_DOWN = b'mirror_left_down'
    CUSTOMIZATION_SHEET_ACTION_MIRROR_RIGHT_DOWN = b'mirror_right_down'
    CUSTOMIZATION_SHEET_ACTION_MOVE = b'move'
    CUSTOMIZATION_SHEET_ACTION_EDIT = b'edit'
    CUSTOMIZATION_SHEET_ACTION_INFO = b'info'
    CUSTOMIZATION_SHEET_ACTION_GET_BACK = b'get_back'
    CUSTOMIZATION_SHEET_ACTION_SWITCH_PROGRESSION_LVL = b'switch_progression_lvl'
    CUSTOMIZATION_SHEET_ACTION_EDIT_STYLE = b'edit_style'


class CustomizationButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomizationButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getActionBtnLabel(self):
        return self._getString(0)

    def setActionBtnLabel(self, value):
        self._setString(0, value)
        return

    def getDisableTooltip(self):
        return self._getString(1)

    def setDisableTooltip(self, value):
        self._setString(1, value)
        return

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getActionType(self):
        return ButtonActionType(self._getString(3))

    def setActionType(self, value):
        self._setString(3, value.value)
        return

    def getProgressionLevel(self):
        return self._getNumber(4)

    def setProgressionLevel(self, value):
        self._setNumber(4, value)
        return

    def getSubButtons(self):
        return self._getArray(5)

    def setSubButtons(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getSubButtonsType():
        return CustomizationSubButtonModel

    def _initialize(self):
        super(CustomizationButtonModel, self)._initialize()
        self._addStringProperty(b'actionBtnLabel', b'')
        self._addStringProperty(b'disableTooltip', b'')
        self._addBoolProperty(b'isEnabled', False)
        self._addStringProperty(b'actionType')
        self._addNumberProperty(b'progressionLevel', 1)
        self._addArrayProperty(b'subButtons', Array())
        return
