VIEW_OVERLAPPED = b'viewOverlapped'

class TooltipPositionerMixin(object):

    def __onWindowPositionChanged(self, uniqueID, *_):
        window = self.gui.windowsManager.getWindow(uniqueID)
        if window:
            window.onPositionChanged -= self.__onWindowPositionChanged
            if self.__positionX and self.__positionY:
                width, __ = window.size
                window.move(int(self.__positionX) - int(width), int(self.__positionY))
        return

    def createToolTip(self, event):
        if self.hasDeferModelUpdate:
            return VIEW_OVERLAPPED
        window = super(TooltipPositionerMixin, self).createToolTip(event)
        if window:
            self.__positionX = event.getArgument(b'positionX')
            self.__positionY = event.getArgument(b'positionY')
            window.onPositionChanged += self.__onWindowPositionChanged
        return window
