from enum import IntEnum
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.ny_currency_panel_model import NyCurrencyPanelModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.city.ny_city_marker_model import NyCityMarkerModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_back_button_model import NyBackButtonModel

class CameraState(IntEnum):
    NOT_EXIST = -1
    NOT_INSTALLED = 0
    INSTALLED = 1
    IN_TRANSITION = 2


class OnboardingState(IntEnum):
    DEFAULT = 0
    FIR = 1
    PANORAMA = 2


class OnboardingViewModel(ViewModel):
    __slots__ = (b'onClose', b'onLevelUp', b'onHoverMarker', b'onHoverOutMarker', b'onMouseOver3dScene', b'onMoveSpace', b'onMoveTo', b'onGoToFirObject', b'onHideBlur')

    def __init__(self, properties=7, commands=9):
        super(OnboardingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def backButton(self):
        return self._getViewModel(0)

    @staticmethod
    def getBackButtonType():
        return NyBackButtonModel

    @property
    def firMarker(self):
        return self._getViewModel(1)

    @staticmethod
    def getFirMarkerType():
        return NyCityMarkerModel

    @property
    def currencyPanel(self):
        return self._getViewModel(2)

    @staticmethod
    def getCurrencyPanelType():
        return NyCurrencyPanelModel

    def getAnimationCurrency(self):
        return self._getNumber(3)

    def setAnimationCurrency(self, value):
        self._setNumber(3, value)
        return

    def getCurrentState(self):
        return OnboardingState(self._getNumber(4))

    def setCurrentState(self, value):
        self._setNumber(4, value.value)
        return

    def getCameraState(self):
        return CameraState(self._getNumber(5))

    def setCameraState(self, value):
        self._setNumber(5, value.value)
        return

    def getIsFirstShow(self):
        return self._getBool(6)

    def setIsFirstShow(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(OnboardingViewModel, self)._initialize()
        self._addViewModelProperty(b'backButton', NyBackButtonModel())
        self._addViewModelProperty(b'firMarker', NyCityMarkerModel())
        self._addViewModelProperty(b'currencyPanel', NyCurrencyPanelModel())
        self._addNumberProperty(b'animationCurrency', 0)
        self._addNumberProperty(b'currentState')
        self._addNumberProperty(b'cameraState')
        self._addBoolProperty(b'isFirstShow', False)
        self.onClose = self._addCommand(b'onClose')
        self.onLevelUp = self._addCommand(b'onLevelUp')
        self.onHoverMarker = self._addCommand(b'onHoverMarker')
        self.onHoverOutMarker = self._addCommand(b'onHoverOutMarker')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onMoveTo = self._addCommand(b'onMoveTo')
        self.onGoToFirObject = self._addCommand(b'onGoToFirObject')
        self.onHideBlur = self._addCommand(b'onHideBlur')
        return
