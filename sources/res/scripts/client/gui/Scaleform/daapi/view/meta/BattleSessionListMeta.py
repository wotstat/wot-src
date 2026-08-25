from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BattleSessionListMeta(AbstractWindowView):

    def requestToJoinTeam(self, prbID, prbType):
        self._printOverrideError(b'requestToJoinTeam')
        return

    def getClientID(self):
        self._printOverrideError(b'getClientID')
        return

    def as_refreshListS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_refreshList(data)
        return
