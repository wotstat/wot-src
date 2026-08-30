from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class SpecialMissionCompletedViewModel(NotificationBaseModel):
    __slots__ = (b'onClose', b'onGoToBadge')

    def __init__(self, properties=1, commands=2):
        super(SpecialMissionCompletedViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(SpecialMissionCompletedViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onGoToBadge = self._addCommand(b'onGoToBadge')
        return
