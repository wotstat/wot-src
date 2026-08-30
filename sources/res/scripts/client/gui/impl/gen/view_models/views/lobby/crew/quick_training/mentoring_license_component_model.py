from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class MentoringLicenseComponentModel(ComponentBaseModel):
    __slots__ = (b'openMentoring',)

    def __init__(self, properties=4, commands=1):
        super(MentoringLicenseComponentModel, self).__init__(properties=properties, commands=commands)
        return

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)
        return

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(MentoringLicenseComponentModel, self)._initialize()
        self._addNumberProperty(b'amount', 0)
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isVisible', False)
        self.openMentoring = self._addCommand(b'openMentoring')
        return
