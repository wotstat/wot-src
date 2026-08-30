from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class EventBannersListModel(ViewModel):
    __slots__ = (b'onEventClick', b'onAppearAnimationPlayed')

    def __init__(self, properties=1, commands=2):
        super(EventBannersListModel, self).__init__(properties=properties, commands=commands)
        return

    def getBanners(self):
        return self._getArray(0)

    def setBanners(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getBannersType():
        return EventBannerModel

    def _initialize(self):
        super(EventBannersListModel, self)._initialize()
        self._addArrayProperty(b'banners', Array())
        self.onEventClick = self._addCommand(b'onEventClick')
        self.onAppearAnimationPlayed = self._addCommand(b'onAppearAnimationPlayed')
        return
