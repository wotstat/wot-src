from frameworks.wulf import Array
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel

class DocumentChangeDialogModel(DialogTemplateViewModel):
    __slots__ = (b'onChangeFirstName', b'onChangeLastName')

    def __init__(self, properties=10, commands=4):
        super(DocumentChangeDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getFirstNameIndex(self):
        return self._getNumber(6)

    def setFirstNameIndex(self, value):
        self._setNumber(6, value)
        return

    def getLastNameIndex(self):
        return self._getNumber(7)

    def setLastNameIndex(self, value):
        self._setNumber(7, value)
        return

    def getFirstNameList(self):
        return self._getArray(8)

    def setFirstNameList(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getFirstNameListType():
        return unicode

    def getLastNameList(self):
        return self._getArray(9)

    def setLastNameList(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getLastNameListType():
        return unicode

    def _initialize(self):
        super(DocumentChangeDialogModel, self)._initialize()
        self._addNumberProperty(b'firstNameIndex', 0)
        self._addNumberProperty(b'lastNameIndex', 0)
        self._addArrayProperty(b'firstNameList', Array())
        self._addArrayProperty(b'lastNameList', Array())
        self.onChangeFirstName = self._addCommand(b'onChangeFirstName')
        self.onChangeLastName = self._addCommand(b'onChangeLastName')
        return
