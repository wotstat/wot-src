from gui.Scaleform.framework.entities.DAAPIDataProvider import DAAPIDataProvider
from messenger import g_settings
from messenger.m_constants import USER_GUI_TYPE
from messenger.storage import storage_getter

class MembersDataProvider(DAAPIDataProvider):

    def __init__(self):
        super(MembersDataProvider, self).__init__()
        self.__list = []
        return

    @property
    def collection(self):
        return self.__list

    @storage_getter(b'users')
    def usersStorage(self):
        return

    def buildList(self, members):
        self.__list = []
        members = sorted(members, key=(lambda member: member.getName().lower()))
        getUser = self.usersStorage.getUser
        getColors = g_settings.getColorScheme(b'rosters').getColors
        for member in members:
            dbID = member.getDatabaseID()
            isOnline = member.isOnline()
            user = getUser(dbID)
            if user:
                tags = list(user.getTags())
                colors = getColors(user.getGuiType())
            else:
                tags = []
                colors = getColors(USER_GUI_TYPE.OTHER)
            self.__list.append({b'dbID': dbID, 
               b'userName': (member.getFullName()), 
               b'isOnline': isOnline, 
               b'color': (colors[0 if isOnline else 1]), 
               b'tags': tags, 
               b'isPlayerSpeaking': False})

        return

    def emptyItem(self):
        return {b'dbID': 0, 
           b'userName': b'', 
           b'isOnline': False, 
           b'color': 0, 
           b'tags': [], b'isPlayerSpeaking': False}
