from enum import Enum
from gui.impl.gen.view_models.views.lobby.post_progression.base_step_model import BaseStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.restrictions_model import RestrictionsModel

class ActionState(Enum):
    PERSISTENT = b'persistent'
    SELECTABLE = b'selectable'
    CHANGEABLE = b'changeable'


class StepState(Enum):
    RESTRICTED = b'restricted'
    UNAVAILABLELOCKED = b'unavailableLocked'
    AVAILABLEPURCHASE = b'availablePurchase'
    RECEIVED = b'received'


class StepModel(BaseStepModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(StepModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def restrictions(self):
        return self._getViewModel(2)

    @staticmethod
    def getRestrictionsType():
        return RestrictionsModel

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)
        return

    def getActionState(self):
        return ActionState(self._getString(4))

    def setActionState(self, value):
        self._setString(4, value.value)
        return

    def getStepState(self):
        return StepState(self._getString(5))

    def setStepState(self, value):
        self._setString(5, value.value)
        return

    def _initialize(self):
        super(StepModel, self)._initialize()
        self._addViewModelProperty(b'restrictions', RestrictionsModel())
        self._addBoolProperty(b'isDisabled', False)
        self._addStringProperty(b'actionState')
        self._addStringProperty(b'stepState')
        return
