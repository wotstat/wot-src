import BigWorld, GUI
from Button import Button
from CheckBox import CheckBox

class RadioButton(CheckBox):
    factoryString = b'PyGUI.RadioButton'

    def __init__(self, component):
        CheckBox.__init__(self, component)
        self.buttonStyle = Button.RADIOBUTTON_STYLE
        return

    @staticmethod
    def create(texture, text=b'', groupName=b'', **kwargs):
        b = RadioButton(CheckBox.createInternal(texture, text, **kwargs), **kwargs)
        b.groupName = groupName
        return b.component
