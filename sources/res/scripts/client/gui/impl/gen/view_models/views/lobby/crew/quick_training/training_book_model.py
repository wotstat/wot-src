from frameworks.wulf import ViewModel

class TrainingBookModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(TrainingBookModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getTitle(self):
        return self._getString(3)

    def setTitle(self, value):
        self._setString(3, value)
        return

    def getMainText(self):
        return self._getString(4)

    def setMainText(self, value):
        self._setString(4, value)
        return

    def getAdditionalText(self):
        return self._getString(5)

    def setAdditionalText(self, value):
        self._setString(5, value)
        return

    def getBookAddedXp(self):
        return self._getNumber(6)

    def setBookAddedXp(self, value):
        self._setNumber(6, value)
        return

    def getAvailableCount(self):
        return self._getNumber(7)

    def setAvailableCount(self, value):
        self._setNumber(7, value)
        return

    def getSelectedCount(self):
        return self._getNumber(8)

    def setSelectedCount(self, value):
        self._setNumber(8, value)
        return

    def getPostProgressionClaimCount(self):
        return self._getNumber(9)

    def setPostProgressionClaimCount(self, value):
        self._setNumber(9, value)
        return

    def getHasError(self):
        return self._getBool(10)

    def setHasError(self, value):
        self._setBool(10, value)
        return

    def getHasPotentialLoss(self):
        return self._getBool(11)

    def setHasPotentialLoss(self, value):
        self._setBool(11, value)
        return

    def getCanBuyBook(self):
        return self._getBool(12)

    def setCanBuyBook(self, value):
        self._setBool(12, value)
        return

    def getIsDisabled(self):
        return self._getBool(13)

    def setIsDisabled(self, value):
        self._setBool(13, value)
        return

    def getIsPersonal(self):
        return self._getBool(14)

    def setIsPersonal(self, value):
        self._setBool(14, value)
        return

    def getIsPostProgressionShown(self):
        return self._getBool(15)

    def setIsPostProgressionShown(self, value):
        self._setBool(15, value)
        return

    def getCanAddMoreBooks(self):
        return self._getBool(16)

    def setCanAddMoreBooks(self, value):
        self._setBool(16, value)
        return

    def _initialize(self):
        super(TrainingBookModel, self)._initialize()
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'mainText', b'')
        self._addStringProperty(b'additionalText', b'')
        self._addNumberProperty(b'bookAddedXp', 0)
        self._addNumberProperty(b'availableCount', 0)
        self._addNumberProperty(b'selectedCount', 0)
        self._addNumberProperty(b'postProgressionClaimCount', 0)
        self._addBoolProperty(b'hasError', False)
        self._addBoolProperty(b'hasPotentialLoss', False)
        self._addBoolProperty(b'canBuyBook', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isPersonal', False)
        self._addBoolProperty(b'isPostProgressionShown', False)
        self._addBoolProperty(b'canAddMoreBooks', False)
        return
