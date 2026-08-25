from __future__ import absolute_import
from gui.impl.gen.view_models.views.lobby.page.footer.notifications_center_model import NotificationsCenterModel
from gui.impl.pub.view_component import ViewComponent
from gui.shared.notifications import NotificationPriorityLevel
from notification import NotificationMVC

class NotificationsCenterPresenter(ViewComponent[NotificationsCenterModel]):

    def __init__(self):
        super(NotificationsCenterPresenter, self).__init__(model=NotificationsCenterModel)
        return

    @property
    def viewModel(self):
        return super(NotificationsCenterPresenter, self).getViewModel()

    def _initialize(self):
        super(NotificationsCenterPresenter, self)._initialize()
        NotificationMVC.g_instance.getModel().onNotifiedMessagesCountChanged += self.__onNotifiedMessagesCountChange
        NotificationMVC.g_instance.getModel().onNotificationReceived += self.__onNotificationReceived
        self.__updateNotifiedMessagesCount()
        return

    def _finalize(self):
        model = NotificationMVC.g_instance.getModel()
        if model:
            model.onNotifiedMessagesCountChanged -= self.__onNotifiedMessagesCountChange
            model.onNotificationReceived -= self.__onNotificationReceived
        return

    def __updateNotifiedMessagesCount(self):
        self.viewModel.setNewNotificationsCount(NotificationMVC.g_instance.getModel().getNotifiedMessagesCount())
        return

    def __onNotifiedMessagesCountChange(self, _):
        self.__updateNotifiedMessagesCount()
        return

    def __onNotificationReceived(self, notification):
        priorityLevel = notification.getPriorityLevel()
        self.viewModel.setHasImportantNotification(priorityLevel == NotificationPriorityLevel.HIGH)
        return
