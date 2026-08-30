import BigWorld, Event
from debug_utils import LOG_ERROR
from future.utils import itervalues
from gui.prb_control.events_dispatcher import TOOLTIP_PRB_DATA
DEFAULT_FIELDS = {b'clientID': 0, 
   b'label': b'', 
   b'canClose': False, 
   b'isNotified': False, 
   b'icon': None, 
   b'order': 0, 
   b'isInProgress': False, 
   b'isWindowOpened': False, 
   b'readyData': None, 
   b'isWindowFocused': False, 
   b'tooltipData': None}

class ChannelsDataProvider(object):

    def __init__(self):
        super(ChannelsDataProvider, self).__init__()
        self.__data = {}
        self.__list = []
        self.onDataUpdated = Event.Event()
        return

    def clear(self):
        self.__data.clear()
        self.__list = []
        self.onDataUpdated.clear()
        return

    def addItem(self, clientID, data):
        label = data[b'label']
        tooltipData = data.get(b'tooltipData', None)
        if tooltipData is None:
            tooltipData = TOOLTIP_PRB_DATA(tooltipId=None, label=label)._asdict()
        item = {b'clientID': clientID, 
           b'label': label, 
           b'canClose': (data.get(b'canClose', False)), 
           b'isNotified': (data.get(b'isNotified', False)), 
           b'icon': (data.get(b'icon')), 
           b'order': (data.get(b'order', (0, BigWorld.time()))), 
           b'isInProgress': (data.get(b'isInProgress', False)), 
           b'isWindowOpened': (data.get(b'isWindowOpened', False)), 
           b'readyData': (data.get(b'readyData', None)), 
           b'isWindowFocused': (data.get(b'isWindowFocused', False)), 
           b'tooltipData': tooltipData}
        if clientID in self.__data:
            self.__data[clientID].update(item)
        else:
            self.__data[clientID] = item
        self.refresh()
        return

    def removeItem(self, clientID):
        if clientID in self.__data:
            self.__data.pop(clientID).clear()
            self.refresh()
        return

    def setItemField(self, clientID, key, value):
        result = False
        if clientID in self.__data:
            item = self.__data[clientID]
            if key in item:
                item[key] = value
                self.refresh()
                result = True
            else:
                LOG_ERROR(b'Key is invalid', key)
        return result

    def clearItemField(self, clientID, key):
        result = False
        if clientID in self.__data and key in DEFAULT_FIELDS:
            item = self.__data[clientID]
            item[key] = DEFAULT_FIELDS[key]
            self.refresh()
            result = True
        return result

    def setItemFields(self, clientID, fields):
        result = False
        if clientID in self.__data:
            item = self.__data[clientID]
            item.update(fields)
            self.refresh()
            result = True
        return result

    @property
    def collection(self):
        return self.__list

    def buildList(self):
        self.__list = sorted(itervalues(self.__data), key=(lambda item: item[b'order']))
        return

    def refresh(self):
        self.buildList()
        self.onDataUpdated()
        return
