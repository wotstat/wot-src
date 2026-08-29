from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.progression import Progression
from gui.impl.gen.view_models.views.lobby.hangar.header_widget_view_model import HeaderWidgetViewModel

class BirthdayEntryPointViewModel(HeaderWidgetViewModel):
    __slots__ = (b'onClick', b'onAnimationEnded', b'onComponentDestroyed')

    def __init__(self, properties=3, commands=4):
        super(BirthdayEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progression(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionType():
        return Progression

    def getIsPaused(self):
        return self._getBool(1)

    def setIsPaused(self, value):
        self._setBool(1, value)
        return

    def getEconomicBonus(self):
        return self._getNumber(2)

    def setEconomicBonus(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BirthdayEntryPointViewModel, self)._initialize()
        self._addViewModelProperty(b'progression', Progression())
        self._addBoolProperty(b'isPaused', False)
        self._addNumberProperty(b'economicBonus', 0)
        self.onClick = self._addCommand(b'onClick')
        self.onAnimationEnded = self._addCommand(b'onAnimationEnded')
        self.onComponentDestroyed = self._addCommand(b'onComponentDestroyed')
        return
