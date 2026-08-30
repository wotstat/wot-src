from gui.Scaleform.daapi.view.lobby.missions.regular.missions_page import MissionView

class MissionsGroupedViewMeta(MissionView):

    def expand(self, id, value):
        self._printOverrideError(b'expand')
        return

    def clickActionBtn(self, actionID):
        self._printOverrideError(b'clickActionBtn')
        return

    def onClickButtonDetails(self):
        self._printOverrideError(b'onClickButtonDetails')
        return

    def onClickInfoBtn(self, eventType):
        self._printOverrideError(b'onClickInfoBtn')
        return

    def onClickOpenShopBtn(self, eventType):
        self._printOverrideError(b'onClickOpenShopBtn')
        return

    def onClickOpenEventBtn(self, eventType):
        self._printOverrideError(b'onClickOpenEventBtn')
        return
