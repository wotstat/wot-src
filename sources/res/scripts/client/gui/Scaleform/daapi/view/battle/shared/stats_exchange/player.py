from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS
from gui.battle_control.arena_info.settings import PLAYER_STATUS
from soft_exception import SoftException

class PlayerStatusComponent(broker.StatusComponent):

    def __init__(self):
        super(PlayerStatusComponent, self).__init__(status=PLAYER_STATUS.DEFAULT)
        return


class InvitationStatusComponent(broker.StatusComponent):

    def __init__(self):
        super(InvitationStatusComponent, self).__init__(status=INVITATION_DELIVERY_STATUS.NONE)
        return


class InvitationsExchangeBlock(broker.ExchangeBlock):

    def __init__(self):
        super(InvitationsExchangeBlock, self).__init__(InvitationStatusComponent())
        return

    def addSortIDs(self, arenaDP, *flags):
        raise SoftException(b'This method should not be reached in this context')
        return

    def addTotalStats(self, stats):
        raise SoftException(b'This method should not be reached in this context')
        return


class UserTagsItemData(broker.VehicleComponent):
    __slots__ = (b'_ctx', b'_avatarSessionID', b'_igrType', b'_tags')

    def __init__(self, ctx):
        super(UserTagsItemData, self).__init__()
        self._ctx = ctx
        self._avatarSessionID = b''
        self._igrType = 0
        self._tags = None
        return

    def clear(self):
        self._avatarSessionID = b''
        self._igrType = 0
        self._tags = None
        super(UserTagsItemData, self).clear()
        return

    def destroy(self):
        self._ctx = None
        super(UserTagsItemData, self).destroy()
        return

    def get(self, forced=False):
        if self._tags is None:
            tags = self._ctx.getUserTags(self._avatarSessionID, self._igrType)
        else:
            tags = self._ctx.addTagByIGRType(self._tags, self._igrType)
        if forced or tags:
            return {b'isEnemy': (self._isEnemy), 
               b'vehicleID': (self._vehicleID), 
               b'userTags': tags}
        else:
            return {}

    def addVehicleInfo(self, vInfoVO):
        playerVO = vInfoVO.player
        self._avatarSessionID = playerVO.avatarSessionID
        self._igrType = playerVO.igrType
        self._vehicleID = vInfoVO.vehicleID
        return

    def addUserTags(self, tags):
        self._tags = tags
        return


class UsersTagsListExchangeData(broker.ExchangeBlock):

    def __init__(self, ctx):
        super(UsersTagsListExchangeData, self).__init__(UserTagsItemData(ctx))
        return

    def addSortIDs(self, arenaDP, *flags):
        raise SoftException(b'This method should not be reached in this context')
        return

    def addTotalStats(self, stats):
        raise SoftException(b'This method should not be reached in this context')
        return
