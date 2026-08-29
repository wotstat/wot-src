from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class InscriptionStateEnum(IntEnum):
    EMPTY = 0
    SUBMITENTER = 1
    FIRSTENTER = 2
    EDITENTER = 3
    NOTAVAILABLEENTER = 4


class CustomizationMarkerEditModeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CustomizationMarkerEditModeModel, self).__init__(properties=properties, commands=commands)
        return

    def getEditDigitsCount(self):
        return self._getNumber(0)

    def setEditDigitsCount(self, value):
        self._setNumber(0, value)
        return

    def getInscriptionState(self):
        return InscriptionStateEnum(self._getNumber(1))

    def setInscriptionState(self, value):
        self._setNumber(1, value.value)
        return

    def getInvalidInscriptionNumber(self):
        return self._getString(2)

    def setInvalidInscriptionNumber(self, value):
        self._setString(2, value)
        return

    def getInscriptionFirstEnterRange(self):
        return self._getArray(3)

    def setInscriptionFirstEnterRange(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getInscriptionFirstEnterRangeType():
        return unicode

    def getInscriptionDelay(self):
        return self._getNumber(4)

    def setInscriptionDelay(self, value):
        self._setNumber(4, value)
        return

    def getInscriptionDuration(self):
        return self._getNumber(5)

    def setInscriptionDuration(self, value):
        self._setNumber(5, value)
        return

    def getStartTimestamp(self):
        return self._getReal(6)

    def setStartTimestamp(self, value):
        self._setReal(6, value)
        return

    def _initialize(self):
        super(CustomizationMarkerEditModeModel, self)._initialize()
        self._addNumberProperty(b'editDigitsCount', 0)
        self._addNumberProperty(b'inscriptionState')
        self._addStringProperty(b'invalidInscriptionNumber', b'')
        self._addArrayProperty(b'inscriptionFirstEnterRange', Array())
        self._addNumberProperty(b'inscriptionDelay', 0)
        self._addNumberProperty(b'inscriptionDuration', 0)
        self._addRealProperty(b'startTimestamp', 0.0)
        return
