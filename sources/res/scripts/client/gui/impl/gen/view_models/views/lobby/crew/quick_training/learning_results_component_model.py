from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class LearningResultsComponentModel(ComponentBaseModel):
    __slots__ = (b'learn', b'cancel')

    def __init__(self, properties=3, commands=2):
        super(LearningResultsComponentModel, self).__init__(properties=properties, commands=commands)
        return

    def getCrewXpAmount(self):
        return self._getNumber(1)

    def setCrewXpAmount(self, value):
        self._setNumber(1, value)
        return

    def getPersonalXpAmount(self):
        return self._getNumber(2)

    def setPersonalXpAmount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(LearningResultsComponentModel, self)._initialize()
        self._addNumberProperty(b'crewXpAmount', 0)
        self._addNumberProperty(b'personalXpAmount', 0)
        self.learn = self._addCommand(b'learn')
        self.cancel = self._addCommand(b'cancel')
        return
