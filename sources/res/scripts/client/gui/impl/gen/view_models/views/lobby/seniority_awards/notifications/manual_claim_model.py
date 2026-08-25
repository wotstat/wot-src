from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class ManualClaimModel(NotificationBaseModel):
    __slots__ = (b'onClick', b'onClose')

    def __init__(self, properties=1, commands=2):
        super(ManualClaimModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ManualClaimModel, self)._initialize()
        self.onClick = self._addCommand(b'onClick')
        self.onClose = self._addCommand(b'onClose')
        return
