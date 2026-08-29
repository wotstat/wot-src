from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.collection.pages_blurred_background_model import PagesBlurredBackgroundModel

class ItemType(Enum):
    PHOTO = b'photo'
    NOTE = b'note'
    TANKMAN = b'tankman'
    MEDAL = b'medal'
    STYLE2D = b'style2d'
    STYLE3D = b'style3d'
    OTHERCUSTOMIZATION = b'otherCustomization'


class CollectionItemPreviewModel(ViewModel):
    __slots__ = (b'onClosePreview', b'onOpenPreview')

    def __init__(self, properties=10, commands=2):
        super(CollectionItemPreviewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return ItemType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getSmallImage(self):
        return self._getString(4)

    def setSmallImage(self, value):
        self._setString(4, value)
        return

    def getMediumImage(self):
        return self._getString(5)

    def setMediumImage(self, value):
        self._setString(5, value)
        return

    def getLargeImage(self):
        return self._getString(6)

    def setLargeImage(self, value):
        self._setString(6, value)
        return

    def getCurrentCollection(self):
        return self._getString(7)

    def setCurrentCollection(self, value):
        self._setString(7, value)
        return

    def getPage(self):
        return self._getNumber(8)

    def setPage(self, value):
        self._setNumber(8, value)
        return

    def getPagesBlurredBackgrounds(self):
        return self._getArray(9)

    def setPagesBlurredBackgrounds(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getPagesBlurredBackgroundsType():
        return PagesBlurredBackgroundModel

    def _initialize(self):
        super(CollectionItemPreviewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'type')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'smallImage', b'')
        self._addStringProperty(b'mediumImage', b'')
        self._addStringProperty(b'largeImage', b'')
        self._addStringProperty(b'currentCollection', b'defaultConfig')
        self._addNumberProperty(b'page', 0)
        self._addArrayProperty(b'pagesBlurredBackgrounds', Array())
        self.onClosePreview = self._addCommand(b'onClosePreview')
        self.onOpenPreview = self._addCommand(b'onOpenPreview')
        return
