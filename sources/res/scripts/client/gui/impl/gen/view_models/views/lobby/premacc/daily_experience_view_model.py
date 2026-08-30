from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.daily_experience_base_model import DailyExperienceBaseModel

class DailyExperienceViewModel(DailyExperienceBaseModel):
    __slots__ = (b'onGoToContentPage', b'onBackBtnClicked')

    def __init__(self, properties=5, commands=2):
        super(DailyExperienceViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackBtnLabel(self):
        return self._getResource(4)

    def setBackBtnLabel(self, value):
        self._setResource(4, value)
        return

    def _initialize(self):
        super(DailyExperienceViewModel, self)._initialize()
        self._addResourceProperty(b'backBtnLabel', R.invalid())
        self.onGoToContentPage = self._addCommand(b'onGoToContentPage')
        self.onBackBtnClicked = self._addCommand(b'onBackBtnClicked')
        return
