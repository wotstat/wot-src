from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_vehicle_widget_view_model import BattlePassVehicleWidgetViewModel

class BattlePassWidget3DStyleViewModel(ViewModel):
    __slots__ = (b'onPreviewClick', b'onMarathonPreviewClick', b'onSoundClick')

    def __init__(self, properties=6, commands=3):
        super(BattlePassWidget3DStyleViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return BattlePassVehicleWidgetViewModel

    def getStyleName(self):
        return self._getString(1)

    def setStyleName(self, value):
        self._setString(1, value)
        return

    def getStyleId(self):
        return self._getNumber(2)

    def setStyleId(self, value):
        self._setNumber(2, value)
        return

    def getMarathonRewardId(self):
        return self._getString(3)

    def setMarathonRewardId(self, value):
        self._setString(3, value)
        return

    def getIntCD(self):
        return self._getNumber(4)

    def setIntCD(self, value):
        self._setNumber(4, value)
        return

    def getIsPaidReward(self):
        return self._getBool(5)

    def setIsPaidReward(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(BattlePassWidget3DStyleViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', BattlePassVehicleWidgetViewModel())
        self._addStringProperty(b'styleName', b'')
        self._addNumberProperty(b'styleId', 0)
        self._addStringProperty(b'marathonRewardId', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addBoolProperty(b'isPaidReward', False)
        self.onPreviewClick = self._addCommand(b'onPreviewClick')
        self.onMarathonPreviewClick = self._addCommand(b'onMarathonPreviewClick')
        self.onSoundClick = self._addCommand(b'onSoundClick')
        return
