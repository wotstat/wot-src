from gui.impl.gen.view_models.views.lobby.crew.idle_crew_bonus import IdleCrewBonus

class CrewHeaderModel(IdleCrewBonus):
    __slots__ = (b'onCrewOperationsClick', b'onIdleCrewBonusToggle')

    def __init__(self, properties=3, commands=2):
        super(CrewHeaderModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAccelerateCrewTrainingActive(self):
        return self._getBool(1)

    def setIsAccelerateCrewTrainingActive(self, value):
        self._setBool(1, value)
        return

    def getIsAccelerateCrewTrainingAvailable(self):
        return self._getBool(2)

    def setIsAccelerateCrewTrainingAvailable(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(CrewHeaderModel, self)._initialize()
        self._addBoolProperty(b'isAccelerateCrewTrainingActive', False)
        self._addBoolProperty(b'isAccelerateCrewTrainingAvailable', False)
        self.onCrewOperationsClick = self._addCommand(b'onCrewOperationsClick')
        self.onIdleCrewBonusToggle = self._addCommand(b'onIdleCrewBonusToggle')
        return
