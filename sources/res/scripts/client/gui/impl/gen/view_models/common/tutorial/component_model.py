from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.tutorial.rect_model import RectModel

class ComponentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ComponentModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rect(self):
        return self._getViewModel(0)

    @staticmethod
    def getRectType():
        return RectModel

    def getViewId(self):
        return self._getString(1)

    def setViewId(self, value):
        self._setString(1, value)
        return

    def getComponentId(self):
        return self._getString(2)

    def setComponentId(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ComponentModel, self)._initialize()
        self._addViewModelProperty(b'rect', RectModel())
        self._addStringProperty(b'viewId', b'')
        self._addStringProperty(b'componentId', b'')
        return
