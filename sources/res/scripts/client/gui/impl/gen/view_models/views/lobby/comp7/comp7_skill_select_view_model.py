from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.comp7.skill_model import SkillModel

class Comp7SkillSelectViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSelect', b'onEquip')

    def __init__(self, properties=2, commands=3):
        super(Comp7SkillSelectViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def skills(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillsType():
        return SkillModel

    @property
    def tankInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getTankInfoType():
        return VehicleModel

    def _initialize(self):
        super(Comp7SkillSelectViewModel, self)._initialize()
        self._addViewModelProperty(b'skills', UserListModel())
        self._addViewModelProperty(b'tankInfo', VehicleModel())
        self.onClose = self._addCommand(b'onClose')
        self.onSelect = self._addCommand(b'onSelect')
        self.onEquip = self._addCommand(b'onEquip')
        return
