from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class KillerUserNameModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(KillerUserNameModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserNameModel

    def getIsPersonal(self):
        return self._getBool(1)

    def setIsPersonal(self, value):
        self._setBool(1, value)
        return

    def getIsSameSquad(self):
        return self._getBool(2)

    def setIsSameSquad(self, value):
        self._setBool(2, value)
        return

    def getIsBot(self):
        return self._getBool(3)

    def setIsBot(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(KillerUserNameModel, self)._initialize()
        self._addViewModelProperty(b'user', UserNameModel())
        self._addBoolProperty(b'isPersonal', False)
        self._addBoolProperty(b'isSameSquad', False)
        self._addBoolProperty(b'isBot', False)
        return
