from frameworks.wulf import ViewModel

class CustomizationTypesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(CustomizationTypesModel, self).__init__(properties=properties, commands=commands)
        return

    def getPaint(self):
        return self._getNumber(0)

    def setPaint(self, value):
        self._setNumber(0, value)
        return

    def getCamouflage(self):
        return self._getNumber(1)

    def setCamouflage(self, value):
        self._setNumber(1, value)
        return

    def getModification(self):
        return self._getNumber(2)

    def setModification(self, value):
        self._setNumber(2, value)
        return

    def getOutfit(self):
        return self._getNumber(3)

    def setOutfit(self, value):
        self._setNumber(3, value)
        return

    def getStyle(self):
        return self._getNumber(4)

    def setStyle(self, value):
        self._setNumber(4, value)
        return

    def getDecal(self):
        return self._getNumber(5)

    def setDecal(self, value):
        self._setNumber(5, value)
        return

    def getEmblem(self):
        return self._getNumber(6)

    def setEmblem(self, value):
        self._setNumber(6, value)
        return

    def getInscription(self):
        return self._getNumber(7)

    def setInscription(self, value):
        self._setNumber(7, value)
        return

    def getProjectionDecal(self):
        return self._getNumber(8)

    def setProjectionDecal(self, value):
        self._setNumber(8, value)
        return

    def getInsignia(self):
        return self._getNumber(9)

    def setInsignia(self, value):
        self._setNumber(9, value)
        return

    def getPersonalNumber(self):
        return self._getNumber(10)

    def setPersonalNumber(self, value):
        self._setNumber(10, value)
        return

    def getSequence(self):
        return self._getNumber(11)

    def setSequence(self, value):
        self._setNumber(11, value)
        return

    def getAttachment(self):
        return self._getNumber(12)

    def setAttachment(self, value):
        self._setNumber(12, value)
        return

    def _initialize(self):
        super(CustomizationTypesModel, self)._initialize()
        self._addNumberProperty(b'Paint', 0)
        self._addNumberProperty(b'Camouflage', 0)
        self._addNumberProperty(b'Modification', 0)
        self._addNumberProperty(b'Outfit', 0)
        self._addNumberProperty(b'Style', 0)
        self._addNumberProperty(b'Decal', 0)
        self._addNumberProperty(b'Emblem', 0)
        self._addNumberProperty(b'Inscription', 0)
        self._addNumberProperty(b'ProjectionDecal', 0)
        self._addNumberProperty(b'Insignia', 0)
        self._addNumberProperty(b'PersonalNumber', 0)
        self._addNumberProperty(b'Sequence', 0)
        self._addNumberProperty(b'Attachment', 0)
        return
