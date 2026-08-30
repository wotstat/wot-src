from frameworks.wulf import ViewModel

class ParallaxModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(ParallaxModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlideId(self):
        return self._getNumber(0)

    def setSlideId(self, value):
        self._setNumber(0, value)
        return

    def getParallaxStructure(self):
        return self._getString(1)

    def setParallaxStructure(self, value):
        self._setString(1, value)
        return

    def getAtlas(self):
        return self._getString(2)

    def setAtlas(self, value):
        self._setString(2, value)
        return

    def getPerspective(self):
        return self._getNumber(3)

    def setPerspective(self, value):
        self._setNumber(3, value)
        return

    def getPerspectiveOriginX(self):
        return self._getNumber(4)

    def setPerspectiveOriginX(self, value):
        self._setNumber(4, value)
        return

    def getPerspectiveOriginY(self):
        return self._getNumber(5)

    def setPerspectiveOriginY(self, value):
        self._setNumber(5, value)
        return

    def getWrapperWidth(self):
        return self._getNumber(6)

    def setWrapperWidth(self, value):
        self._setNumber(6, value)
        return

    def getWrapperHeight(self):
        return self._getNumber(7)

    def setWrapperHeight(self, value):
        self._setNumber(7, value)
        return

    def getOverallScale(self):
        return self._getReal(8)

    def setOverallScale(self, value):
        self._setReal(8, value)
        return

    def getXTilt(self):
        return self._getReal(9)

    def setXTilt(self, value):
        self._setReal(9, value)
        return

    def getXTiltRange(self):
        return self._getReal(10)

    def setXTiltRange(self, value):
        self._setReal(10, value)
        return

    def getYTilt(self):
        return self._getReal(11)

    def setYTilt(self, value):
        self._setReal(11, value)
        return

    def getYTiltRange(self):
        return self._getReal(12)

    def setYTiltRange(self, value):
        self._setReal(12, value)
        return

    def getXSlide(self):
        return self._getReal(13)

    def setXSlide(self, value):
        self._setReal(13, value)
        return

    def getYSlide(self):
        return self._getReal(14)

    def setYSlide(self, value):
        self._setReal(14, value)
        return

    def getChunkFileExt(self):
        return self._getString(15)

    def setChunkFileExt(self, value):
        self._setString(15, value)
        return

    def getChunksAssetsPath(self):
        return self._getString(16)

    def setChunksAssetsPath(self, value):
        self._setString(16, value)
        return

    def _initialize(self):
        super(ParallaxModel, self)._initialize()
        self._addNumberProperty(b'slideId', 0)
        self._addStringProperty(b'parallaxStructure', b'')
        self._addStringProperty(b'atlas', b'')
        self._addNumberProperty(b'perspective', 0)
        self._addNumberProperty(b'perspectiveOriginX', 0)
        self._addNumberProperty(b'perspectiveOriginY', 0)
        self._addNumberProperty(b'wrapperWidth', 0)
        self._addNumberProperty(b'wrapperHeight', 0)
        self._addRealProperty(b'overallScale', 0.0)
        self._addRealProperty(b'xTilt', 0.0)
        self._addRealProperty(b'xTiltRange', 0.0)
        self._addRealProperty(b'yTilt', 0.0)
        self._addRealProperty(b'yTiltRange', 0.0)
        self._addRealProperty(b'xSlide', 0.0)
        self._addRealProperty(b'ySlide', 0.0)
        self._addStringProperty(b'chunkFileExt', b'')
        self._addStringProperty(b'chunksAssetsPath', b'')
        return
