from frameworks.wulf import Array
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_email_model import FieldEmailModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_password_model import FieldPasswordModel

class AddCredentialsModel(BaseWgnpOverlayViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=4):
        super(AddCredentialsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def email(self):
        return self._getViewModel(9)

    @staticmethod
    def getEmailType():
        return FieldEmailModel

    @property
    def password(self):
        return self._getViewModel(10)

    @staticmethod
    def getPasswordType():
        return FieldPasswordModel

    def getQuestID(self):
        return self._getString(11)

    def setQuestID(self, value):
        self._setString(11, value)
        return

    def getBonuses(self):
        return self._getArray(12)

    def setBonuses(self, value):
        self._setArray(12, value)
        return

    def getRewardsTitle(self):
        return self._getResource(13)

    def setRewardsTitle(self, value):
        self._setResource(13, value)
        return

    def getIsPasswordInputVisible(self):
        return self._getBool(14)

    def setIsPasswordInputVisible(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(AddCredentialsModel, self)._initialize()
        self._addViewModelProperty(b'email', FieldEmailModel())
        self._addViewModelProperty(b'password', FieldPasswordModel())
        self._addStringProperty(b'questID', b'')
        self._addArrayProperty(b'bonuses', Array())
        self._addResourceProperty(b'rewardsTitle', R.invalid())
        self._addBoolProperty(b'isPasswordInputVisible', True)
        return
