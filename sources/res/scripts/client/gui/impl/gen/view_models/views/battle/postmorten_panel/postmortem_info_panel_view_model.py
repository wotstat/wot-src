from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.battle.postmorten_panel.rating_button_model import RatingButtonModel

class PostmortemInfoPanelViewModel(ViewModel):
    __slots__ = (b'onRateButtonClick',)

    def __init__(self, properties=7, commands=1):
        super(PostmortemInfoPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFrontline(self):
        return self._getBool(0)

    def setIsFrontline(self, value):
        self._setBool(0, value)
        return

    def getIsFreecamAvailable(self):
        return self._getBool(1)

    def setIsFreecamAvailable(self, value):
        self._setBool(1, value)
        return

    def getIsBlinking(self):
        return self._getBool(2)

    def setIsBlinking(self, value):
        self._setBool(2, value)
        return

    def getHasLivesAvailable(self):
        return self._getBool(3)

    def setHasLivesAvailable(self, value):
        self._setBool(3, value)
        return

    def getIsRatingWidgetEnabled(self):
        return self._getBool(4)

    def setIsRatingWidgetEnabled(self, value):
        self._setBool(4, value)
        return

    def getIsRatingWidgetVisible(self):
        return self._getBool(5)

    def setIsRatingWidgetVisible(self, value):
        self._setBool(5, value)
        return

    def getRatingButtons(self):
        return self._getArray(6)

    def setRatingButtons(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRatingButtonsType():
        return RatingButtonModel

    def _initialize(self):
        super(PostmortemInfoPanelViewModel, self)._initialize()
        self._addBoolProperty(b'isFrontline', False)
        self._addBoolProperty(b'isFreecamAvailable', False)
        self._addBoolProperty(b'isBlinking', False)
        self._addBoolProperty(b'hasLivesAvailable', True)
        self._addBoolProperty(b'isRatingWidgetEnabled', False)
        self._addBoolProperty(b'isRatingWidgetVisible', True)
        self._addArrayProperty(b'ratingButtons', Array())
        self.onRateButtonClick = self._addCommand(b'onRateButtonClick')
        return
