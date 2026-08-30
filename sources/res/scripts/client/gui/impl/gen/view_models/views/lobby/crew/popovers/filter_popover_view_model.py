from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_group_model import FilterToggleGroupModel

class FilterPopoverViewModel(ViewModel):
    __slots__ = (b'onUpdateFilter', b'onResetFilter')

    def __init__(self, properties=4, commands=2):
        super(FilterPopoverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getFilterGroups(self):
        return self._getArray(1)

    def setFilterGroups(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getFilterGroupsType():
        return FilterToggleGroupModel

    def getCanResetFilter(self):
        return self._getBool(2)

    def setCanResetFilter(self, value):
        self._setBool(2, value)
        return

    def getShowResetBtn(self):
        return self._getBool(3)

    def setShowResetBtn(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(FilterPopoverViewModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addArrayProperty(b'filterGroups', Array())
        self._addBoolProperty(b'canResetFilter', False)
        self._addBoolProperty(b'showResetBtn', False)
        self.onUpdateFilter = self._addCommand(b'onUpdateFilter')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        return
