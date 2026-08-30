import BigWorld, GUI, Keys
from PyGUIBase import PyGUIBase
from DraggableComponent import DraggableComponent

class Window(PyGUIBase):
    factoryString = b'PyGUI.Window'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        component.script = self
        return

    def onSave(self, dataSection):
        PyGUIBase.onSave(self, dataSection)
        return

    def onLoad(self, dataSection):
        PyGUIBase.onLoad(self, dataSection)
        return

    @staticmethod
    def create(texture):
        c = GUI.Window(texture)
        return Window(c).component


class EscapableWindow(Window):
    factoryString = b'PyGUI.EscapableWindow'

    def __init__(self, component=None):
        Window.__init__(self, component)
        component.script = self
        self.onEscape = None
        return

    def handleKeyEvent(self, event):
        if event.isKeyDown():
            if event.key == Keys.KEY_ESCAPE:
                if self.onEscape is not None:
                    self.onEscape()
                    return True
        return False


class DraggableWindow(Window, DraggableComponent):
    factoryString = b'PyGUI.DraggableWindow'

    def __init__(self, component, horzDrag=True, vertDrag=True, restrictToParent=True):
        Window.__init__(self, component)
        DraggableComponent.__init__(self, horzDrag, vertDrag, restrictToParent)
        component.script = self
        self.onBeginDrag = self._onBeginDrag
        return

    def handleMouseButtonEvent(self, comp, event):
        return DraggableComponent.handleMouseButtonEvent(self, comp, event)

    def onSave(self, dataSection):
        DraggableComponent.onSave(self, dataSection)
        Window.onSave(self, dataSection)
        return

    def onLoad(self, dataSection):
        DraggableComponent.onLoad(self, dataSection)
        Window.onLoad(self, dataSection)
        return

    def _onBeginDrag(self):
        self.listeners.onBeginDrag()
        return

    @staticmethod
    def create(texture):
        c = GUI.Window(texture)
        return DraggableWindow(c).component
