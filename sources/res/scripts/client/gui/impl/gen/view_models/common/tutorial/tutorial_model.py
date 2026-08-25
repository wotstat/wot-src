from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.tutorial.component_model import ComponentModel
from gui.impl.gen.view_models.common.tutorial.criterion_model import CriterionModel
from gui.impl.gen.view_models.common.tutorial.descriptions_model import DescriptionsModel
from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel
from gui.impl.gen.view_models.common.tutorial.triggers_model import TriggersModel
from gui.impl.gen.view_models.common.tutorial.view_criterion_model import ViewCriterionModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class TutorialModel(ViewModel):
    __slots__ = (b'onComponentFound', b'onComponentDisposed', b'onEffectCompleted', b'onComponentUpdate', b'onTriggerActivated')

    def __init__(self, properties=7, commands=5):
        super(TutorialModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def effects(self):
        return self._getViewModel(0)

    @staticmethod
    def getEffectsType():
        return EffectModel

    @property
    def triggers(self):
        return self._getViewModel(1)

    @staticmethod
    def getTriggersType():
        return TriggersModel

    @property
    def foundComponents(self):
        return self._getViewModel(2)

    @staticmethod
    def getFoundComponentsType():
        return ComponentModel

    @property
    def descriptions(self):
        return self._getViewModel(3)

    @staticmethod
    def getDescriptionsType():
        return DescriptionsModel

    @property
    def criteria(self):
        return self._getViewModel(4)

    @staticmethod
    def getCriteriaType():
        return CriterionModel

    @property
    def viewCriteria(self):
        return self._getViewModel(5)

    @staticmethod
    def getViewCriteriaType():
        return ViewCriterionModel

    def getEnabled(self):
        return self._getBool(6)

    def setEnabled(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(TutorialModel, self)._initialize()
        self._addViewModelProperty(b'effects', ListModel())
        self._addViewModelProperty(b'triggers', ListModel())
        self._addViewModelProperty(b'foundComponents', ListModel())
        self._addViewModelProperty(b'descriptions', DescriptionsModel())
        self._addViewModelProperty(b'criteria', ListModel())
        self._addViewModelProperty(b'viewCriteria', ListModel())
        self._addBoolProperty(b'enabled', False)
        self.onComponentFound = self._addCommand(b'onComponentFound')
        self.onComponentDisposed = self._addCommand(b'onComponentDisposed')
        self.onEffectCompleted = self._addCommand(b'onEffectCompleted')
        self.onComponentUpdate = self._addCommand(b'onComponentUpdate')
        self.onTriggerActivated = self._addCommand(b'onTriggerActivated')
        return
