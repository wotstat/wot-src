from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.city.slot_model import SlotModel

class GroupSlotsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(GroupSlotsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def slots(self):
        return self._getViewModel(0)

    @staticmethod
    def getSlotsType():
        return SlotModel

    def getHasToysHint(self):
        return self._getBool(1)

    def setHasToysHint(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(GroupSlotsModel, self)._initialize()
        self._addViewModelProperty(b'slots', UserListModel())
        self._addBoolProperty(b'hasToysHint', False)
        return
