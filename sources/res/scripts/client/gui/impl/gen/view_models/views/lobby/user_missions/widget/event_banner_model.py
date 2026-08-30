from frameworks.wulf import ViewModel

class EventBannerModel(ViewModel):
    __slots__ = ()
    APPEAR_PENDING = b'pending'
    APPEAR_READY_TO_PLAY = b'readyToPlay'
    APPEAR_NONE = b'none'
    BG_SIZE_BIG = b'big'
    BG_SIZE_MEDIUM = b'medium'
    BG_SIZE_SMALL = b'small'

    def __init__(self, properties=16, commands=0):
        super(EventBannerModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getBorderColor(self):
        return self._getString(1)

    def setBorderColor(self, value):
        self._setString(1, value)
        return

    def getTitle(self):
        return self._getString(2)

    def setTitle(self, value):
        self._setString(2, value)
        return

    def getIntroDescription(self):
        return self._getString(3)

    def setIntroDescription(self, value):
        self._setString(3, value)
        return

    def getInProgressDescription(self):
        return self._getString(4)

    def setInProgressDescription(self, value):
        self._setString(4, value)
        return

    def getTimerText(self):
        return self._getString(5)

    def setTimerText(self, value):
        self._setString(5, value)
        return

    def getIsMode(self):
        return self._getBool(6)

    def setIsMode(self, value):
        self._setBool(6, value)
        return

    def getHasRewards(self):
        return self._getBool(7)

    def setHasRewards(self, value):
        self._setBool(7, value)
        return

    def getBannerState(self):
        return self._getString(8)

    def setBannerState(self, value):
        self._setString(8, value)
        return

    def getIconsPath(self):
        return self._getString(9)

    def setIconsPath(self, value):
        self._setString(9, value)
        return

    def getVideosPath(self):
        return self._getString(10)

    def setVideosPath(self, value):
        self._setString(10, value)
        return

    def getTimerValue(self):
        return self._getNumber(11)

    def setTimerValue(self, value):
        self._setNumber(11, value)
        return

    def getEventStartDate(self):
        return self._getNumber(12)

    def setEventStartDate(self, value):
        self._setNumber(12, value)
        return

    def getEventEndDate(self):
        return self._getNumber(13)

    def setEventEndDate(self, value):
        self._setNumber(13, value)
        return

    def getAppearAnimationState(self):
        return self._getString(14)

    def setAppearAnimationState(self, value):
        self._setString(14, value)
        return

    def getShowTimerBeforeEventEnd(self):
        return self._getNumber(15)

    def setShowTimerBeforeEventEnd(self, value):
        self._setNumber(15, value)
        return

    def _initialize(self):
        super(EventBannerModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'borderColor', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'introDescription', b'')
        self._addStringProperty(b'inProgressDescription', b'')
        self._addStringProperty(b'timerText', b'')
        self._addBoolProperty(b'isMode', False)
        self._addBoolProperty(b'hasRewards', False)
        self._addStringProperty(b'bannerState', b'')
        self._addStringProperty(b'iconsPath', b'')
        self._addStringProperty(b'videosPath', b'')
        self._addNumberProperty(b'timerValue', 0)
        self._addNumberProperty(b'eventStartDate', 0)
        self._addNumberProperty(b'eventEndDate', 0)
        self._addStringProperty(b'appearAnimationState', b'')
        self._addNumberProperty(b'showTimerBeforeEventEnd', 0)
        return
