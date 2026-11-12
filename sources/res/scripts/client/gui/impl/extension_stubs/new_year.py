import logging
from skeletons.gui.impl import INewYearNavigation
_logger = logging.getLogger(__name__)

class NewYearNavigationStub(INewYearNavigation):

    @classmethod
    def showMainView(cls, objectName, instantly=False, viewAlias=None, *args, **kwargs):
        return

    @classmethod
    def showInfoView(cls, previousViewAlias=None, *args, **kwargs):
        return

    @classmethod
    def switchToIntro(cls):
        return

    @classmethod
    def switchByAnchorName(cls, anchorName):
        return

    @classmethod
    def switchFromStyle(cls, objectName, viewAlias=None, tabName=None, *args, **kwargs):
        return

    @classmethod
    def getCurrentViewName(cls):
        return

    @classmethod
    def getPreviousObject(cls):
        return

    @classmethod
    def switchToView(cls, aliasName, tabName=None, instantly=False, *args, **kwargs):
        return

    @classmethod
    def clear(cls):
        return

    @classmethod
    def getCurrentObject(cls):
        return

    @classmethod
    def switchTo(cls, objectName, instantly=False, viewAlias=None, withFade=False, *args, **kwargs):
        _logger.warning(b'NewYearNavigationStub:switchByAnchorName objectName=%s', objectName)
        return

    @classmethod
    def closeMainView(cls, switchCamera=False):
        return
