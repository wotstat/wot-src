from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachment_bonus_model import AttachmentBonusModel

class AttachmentsPreviewFeature(Enum):
    CHALLENGES = b'challenges'
    OPEN_BUNDLE = b'open_bundle'
    BATTLE_PASS = b'battle_pass'


class AttachmentsPreviewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AttachmentsPreviewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAttachmentSetID(self):
        return self._getString(0)

    def setAttachmentSetID(self, value):
        self._setString(0, value)
        return

    def getFeature(self):
        return self._getString(1)

    def setFeature(self, value):
        self._setString(1, value)
        return

    def getAttachments(self):
        return self._getArray(2)

    def setAttachments(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getAttachmentsType():
        return AttachmentBonusModel

    def _initialize(self):
        super(AttachmentsPreviewModel, self)._initialize()
        self._addStringProperty(b'attachmentSetID', b'')
        self._addStringProperty(b'feature', b'')
        self._addArrayProperty(b'attachments', Array())
        return
