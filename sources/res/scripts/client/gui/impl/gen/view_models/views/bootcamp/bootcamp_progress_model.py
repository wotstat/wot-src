from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.bootcamp.bootcamp_lesson_model import BootcampLessonModel

class BootcampProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BootcampProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentLesson(self):
        return self._getNumber(0)

    def setCurrentLesson(self, value):
        self._setNumber(0, value)
        return

    def getTotalLessons(self):
        return self._getNumber(1)

    def setTotalLessons(self, value):
        self._setNumber(1, value)
        return

    def getIsNeedAwarding(self):
        return self._getBool(2)

    def setIsNeedAwarding(self, value):
        self._setBool(2, value)
        return

    def getLevels(self):
        return self._getArray(3)

    def setLevels(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getLevelsType():
        return BootcampLessonModel

    def _initialize(self):
        super(BootcampProgressModel, self)._initialize()
        self._addNumberProperty(b'currentLesson', 0)
        self._addNumberProperty(b'totalLessons', 0)
        self._addBoolProperty(b'isNeedAwarding', False)
        self._addArrayProperty(b'levels', Array())
        return
