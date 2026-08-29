from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_booster_slot_model import BattleBoosterSlotModel

class InstructionType(Enum):
    ECONOMIC = b'economic'
    CREW = b'crew'
    OPTDEVICE = b'optDevice'


class BattleBoostersSetupModel(BaseSetupModel):
    __slots__ = (b'showInfoPage', b'onIntroPassed')

    def __init__(self, properties=9, commands=9):
        super(BattleBoostersSetupModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlots(self):
        return self._getArray(5)

    def setSlots(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getSlotsType():
        return BattleBoosterSlotModel

    def getWithIntroduction(self):
        return self._getBool(6)

    def setWithIntroduction(self, value):
        self._setBool(6, value)
        return

    def getIntroductionType(self):
        return self._getString(7)

    def setIntroductionType(self, value):
        self._setString(7, value)
        return

    def getInstructionType(self):
        return InstructionType(self._getString(8))

    def setInstructionType(self, value):
        self._setString(8, value.value)
        return

    def _initialize(self):
        super(BattleBoostersSetupModel, self)._initialize()
        self._addArrayProperty(b'slots', Array())
        self._addBoolProperty(b'withIntroduction', False)
        self._addStringProperty(b'introductionType', b'')
        self._addStringProperty(b'instructionType')
        self.showInfoPage = self._addCommand(b'showInfoPage')
        self.onIntroPassed = self._addCommand(b'onIntroPassed')
        return
