from frameworks.wulf import ViewModel

class AttachmentsSetInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AttachmentsSetInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getAttachmentsSetName(self):
        return self._getString(0)

    def setAttachmentsSetName(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(AttachmentsSetInfoModel, self)._initialize()
        self._addStringProperty(b'attachmentsSetName', b'')
        return
