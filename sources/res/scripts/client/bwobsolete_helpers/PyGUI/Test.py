import BigWorld, GUI
from Window import DraggableWindow
import random
from functools import partial

def clear():
    while len(GUI.roots()):
        GUI.delRoot(GUI.roots()[0])

    return


def _deleteComponent(t):
    if t.parent:
        t.parent.delChild(t)
    else:
        GUI.delRoot(t)
    return


class TestWindow(DraggableWindow):
    factoryString = b'PyGUI.Test.TestWindow'

    def __init__(self, component):
        DraggableWindow.__init__(self, component)
        return

    def buttonClicked(self):
        t = GUI.Text(b'Button Clicked!')
        t.colour = (255, 0, 0, 255)
        t.position.y = 0.85
        t.verticalAnchor = GUI.Simple.eVAnchor.TOP
        GUI.addRoot(t)
        BigWorld.callback(2.5, partial(_deleteComponent, t))
        return

    def buttonToggled(self, newState):
        self.component.statusLabel.text = b'Toggle state: %s' % (b'True' if newState else b'False')
        return

    def draggableBeginDrag(self):
        self.component.draggableStatus.text = b'Dragging'
        return

    def draggableEndDrag(self):
        self.component.draggableStatus.text = b''
        return

    def draggableDragging(self):
        self.component.draggableStatus.colour = (
         int(random.random() * 127),
         int(random.random() * 127),
         int(random.random() * 127),
         255)
        return

    def onBound(self):
        self.component.button1.script.onClick = self.buttonClicked
        self.component.button2.script.onActivate = lambda : self.buttonToggled(True)
        self.component.button2.script.onDeactivate = lambda : self.buttonToggled(False)
        self.component.draggable.script.onBeginDrag = self.draggableBeginDrag
        self.component.draggable.script.onEndDrag = self.draggableEndDrag
        self.component.draggable.script.onDragging = self.draggableDragging
        return


def testWindow():
    BigWorld.camera(BigWorld.CursorCamera())
    BigWorld.setCursor(GUI.mcursor())
    GUI.mcursor().visible = True
    clear()
    w = GUI.load(b'gui/tests/window.gui')
    GUI.addRoot(w)
    return w
