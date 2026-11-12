import logging
from gui import GUI_SETTINGS
from new_year.gui.constants import VIEW_ALIAS
from gui.shared.event_dispatcher import showBrowserOverlayView
from helpers import time_utils, dependency
from new_year.skeletons.new_year import INewYearController
_logger = logging.getLogger(__name__)

def getTimerGameDayLeft():
    return time_utils.getDayTimeLeft() + 1


def showInfoVideo():
    url = GUI_SETTINGS.newYearInfo.get(b'baseURL')
    if url is None:
        _logger.error(b'newYearInfo.baseURL is missed')
    showBrowserOverlayView(url, alias=VIEW_ALIAS.NY_BROWSER_VIEW)
    return


class HoverObject(object):
    __slots__ = (b'objectName', b'spaceHover', b'guiHover')

    def __init__(self, objectName):
        self.objectName = objectName
        self.spaceHover = False
        self.guiHover = False
        return

    @property
    def isHovered(self):
        return self.objectName is not None and self.spaceHover

    def setSpaceObjectHover(self, objectName, isHovered):
        self.objectName = objectName
        self.spaceHover = isHovered
        return

    def setGUIObjectHover(self, objectName, isHovered):
        self.objectName = objectName
        self.guiHover = isHovered
        return

    def clear(self):
        self.objectName = None
        self.spaceHover = False
        self.guiHover = False
        return


@dependency.replace_none_kwargs(newYearController=INewYearController)
def destroyGUIHoveredObject(hoverObject, newYearController=None):
    if hoverObject.guiHover and hoverObject.objectName is not None:
        newYearController.setGuiObjectHover(hoverObject.objectName, False)
    hoverObject.clear()
    return
