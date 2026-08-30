from frameworks.wulf import Map, ViewModel

class VehiclePlaylistsModel(ViewModel):
    __slots__ = (b'onSelect', b'onCreate', b'onModify', b'onSetDirtyEdit', b'onSave', b'onDiscard', b'onDelete', b'openImportConfirm', b'openDeleteConfirm', b'onGoToAboutVehicle')

    def __init__(self, properties=4, commands=10):
        super(VehiclePlaylistsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedID(self):
        return self._getString(0)

    def setSelectedID(self, value):
        self._setString(0, value)
        return

    def getEnabled(self):
        return self._getBool(1)

    def setEnabled(self, value):
        self._setBool(1, value)
        return

    def getDirtyEdit(self):
        return self._getBool(2)

    def setDirtyEdit(self, value):
        self._setBool(2, value)
        return

    def getStorage(self):
        return self._getMap(3)

    def setStorage(self, value):
        self._setMap(3, value)
        return

    @staticmethod
    def getStorageType():
        return (unicode, unicode)

    def _initialize(self):
        super(VehiclePlaylistsModel, self)._initialize()
        self._addStringProperty(b'selectedID', b'')
        self._addBoolProperty(b'enabled', False)
        self._addBoolProperty(b'dirtyEdit', False)
        self._addMapProperty(b'storage', Map(unicode, unicode))
        self.onSelect = self._addCommand(b'onSelect')
        self.onCreate = self._addCommand(b'onCreate')
        self.onModify = self._addCommand(b'onModify')
        self.onSetDirtyEdit = self._addCommand(b'onSetDirtyEdit')
        self.onSave = self._addCommand(b'onSave')
        self.onDiscard = self._addCommand(b'onDiscard')
        self.onDelete = self._addCommand(b'onDelete')
        self.openImportConfirm = self._addCommand(b'openImportConfirm')
        self.openDeleteConfirm = self._addCommand(b'openDeleteConfirm')
        self.onGoToAboutVehicle = self._addCommand(b'onGoToAboutVehicle')
        return
