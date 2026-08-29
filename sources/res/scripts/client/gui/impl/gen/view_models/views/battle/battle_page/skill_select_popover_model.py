from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.comp7.skill_model import SkillModel

class SkillSelectPopoverModel(ViewModel):
    __slots__ = (b'onEquip', b'onClose')

    def __init__(self, properties=1, commands=2):
        super(SkillSelectPopoverModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def skills(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillsType():
        return SkillModel

    def _initialize(self):
        super(SkillSelectPopoverModel, self)._initialize()
        self._addViewModelProperty(b'skills', UserListModel())
        self.onEquip = self._addCommand(b'onEquip')
        self.onClose = self._addCommand(b'onClose')
        return
