import Event, constants
from PlayerEvents import g_playerEvents
from skeletons.gui.game_control import IIGRController

class IGRController(IIGRController):

    def __init__(self):
        super(IGRController, self).__init__()
        self.__xpFactor = 1.0
        self.__roomType = constants.IGR_TYPE.NONE
        self.onIgrTypeChanged = Event.Event()
        return

    def init(self):
        g_playerEvents.onIGRTypeChanged += self.__onIGRTypeChanged
        return

    def fini(self):
        g_playerEvents.onIGRTypeChanged -= self.__onIGRTypeChanged
        self.onIgrTypeChanged.clear()
        super(IGRController, self).fini()
        return

    def onLobbyStarted(self, ctx=None):
        data = (ctx or {}).get(b'igrData', {})
        self.__roomType = data.get(b'roomType', constants.IGR_TYPE.NONE)
        self.__xpFactor = data.get(b'igrXPFactor', 1.0)
        self.onIgrTypeChanged(self.__roomType, self.__xpFactor)
        return

    def onDisconnected(self):
        self.__xpFactor = 1.0
        self.__roomType = constants.IGR_TYPE.NONE
        return

    def getXPFactor(self):
        return self.__xpFactor

    def getRoomType(self):
        return self.__roomType

    def __onIGRTypeChanged(self, roomType, xpFactor):
        if roomType is not None:
            self.__roomType = roomType
        if xpFactor is not None:
            self.__xpFactor = xpFactor
        self.onIgrTypeChanged(self.__roomType, self.__xpFactor)
        return
