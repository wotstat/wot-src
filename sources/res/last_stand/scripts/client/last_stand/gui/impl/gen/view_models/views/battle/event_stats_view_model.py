from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.battle.event_stats_team_member_model import EventStatsTeamMemberModel
from last_stand.gui.impl.gen.view_models.views.common.stat_column_settings_model import StatColumnSettingsModel

class EventStatsViewModel(ViewModel):
    __slots__ = (b'onPlayerClick', b'onSendFriendRequest', b'onSendPlatoonInvitation', b'onRemoveFromBlacklist')

    def __init__(self, properties=4, commands=4):
        super(EventStatsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def columnSettings(self):
        return self._getViewModel(0)

    @staticmethod
    def getColumnSettingsType():
        return StatColumnSettingsModel

    def getTeam(self):
        return self._getArray(1)

    def setTeam(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTeamType():
        return EventStatsTeamMemberModel

    def getContextMenuPlayerId(self):
        return self._getNumber(2)

    def setContextMenuPlayerId(self, value):
        self._setNumber(2, value)
        return

    def getClientArenaIdx(self):
        return self._getNumber(3)

    def setClientArenaIdx(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(EventStatsViewModel, self)._initialize()
        self._addViewModelProperty(b'columnSettings', StatColumnSettingsModel())
        self._addArrayProperty(b'team', Array())
        self._addNumberProperty(b'contextMenuPlayerId', -1)
        self._addNumberProperty(b'clientArenaIdx', 0)
        self.onPlayerClick = self._addCommand(b'onPlayerClick')
        self.onSendFriendRequest = self._addCommand(b'onSendFriendRequest')
        self.onSendPlatoonInvitation = self._addCommand(b'onSendPlatoonInvitation')
        self.onRemoveFromBlacklist = self._addCommand(b'onRemoveFromBlacklist')
        return
