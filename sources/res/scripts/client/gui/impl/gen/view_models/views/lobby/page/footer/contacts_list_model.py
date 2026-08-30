from frameworks.wulf import ViewModel

class ContactsListModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ContactsListModel, self).__init__(properties=properties, commands=commands)
        return

    def getContactsCount(self):
        return self._getNumber(0)

    def setContactsCount(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(ContactsListModel, self)._initialize()
        self._addNumberProperty(b'contactsCount', 0)
        return
