from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.user_missions_plugin_model import UserMissionsPluginModel
from gui.impl.gen.view_models.views.lobby.hangar.user_missions_slide_model import UserMissionsSlideModel

class UserMissionsWidgetModel(ViewModel):
    __slots__ = (b'onSlideChanged',)

    def __init__(self, properties=4, commands=1):
        super(UserMissionsWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlides(self):
        return self._getArray(0)

    def setSlides(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSlidesType():
        return UserMissionsSlideModel

    def getSelectedSlide(self):
        return self._getString(1)

    def setSelectedSlide(self, value):
        self._setString(1, value)
        return

    def getPlugins(self):
        return self._getMap(2)

    def setPlugins(self, value):
        self._setMap(2, value)
        return

    @staticmethod
    def getPluginsType():
        return (int, UserMissionsPluginModel)

    def getVisibleGroups(self):
        return self._getArray(3)

    def setVisibleGroups(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getVisibleGroupsType():
        return unicode

    def _initialize(self):
        super(UserMissionsWidgetModel, self)._initialize()
        self._addArrayProperty(b'slides', Array())
        self._addStringProperty(b'selectedSlide', b'')
        self._addMapProperty(b'plugins', Map(int, UserMissionsPluginModel))
        self._addArrayProperty(b'visibleGroups', Array())
        self.onSlideChanged = self._addCommand(b'onSlideChanged')
        return
