from gui.shared.badges import buildBadge
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker
from gui.Scaleform.settings import ICONS_SIZES
from gui.battle_control.arena_info import vos_collections
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class ISortedIDsComposer(object):
    __slots__ = ()

    def addSortIDs(self, isEnemy, arenaDP):
        raise NotImplementedError
        return


class VehiclesSortedIDsComposer(broker.SingleSideComposer, ISortedIDsComposer):
    __slots__ = (b'_items', b'_collectionClass')

    def __init__(self, voField=b'vehiclesIDs', sortKey=vos_collections.VehicleInfoSortKey):
        super(VehiclesSortedIDsComposer, self).__init__(voField=voField, sortKey=sortKey)
        self._collectionClass = vos_collections.VehiclesInfoCollection
        return

    def addSortIDs(self, isEnemy, arenaDP):
        self._items = self._collectionClass(sortKey=self._sortKey).ids(arenaDP)
        self.filterIDs(arenaDP)
        return

    def removeObserverIDs(self, arenaDP):
        self._items = [vID for vID in self._items if not arenaDP.getVehicleInfo(vID).vehicleType.isObserver]
        return

    def filterIDs(self, arenaDP):
        self.removeObserverIDs(arenaDP)
        return


class AllySortedIDsComposer(VehiclesSortedIDsComposer):
    __slots__ = ()

    def __init__(self, voField=b'vehiclesIDs', sortKey=vos_collections.VehicleInfoSortKey):
        super(AllySortedIDsComposer, self).__init__(voField, sortKey)
        self._collectionClass = vos_collections.AllyItemsCollection
        return

    def addSortIDs(self, isEnemy, arenaDP):
        super(AllySortedIDsComposer, self).addSortIDs(isEnemy, arenaDP)
        return


class EnemySortedIDsComposer(VehiclesSortedIDsComposer):
    __slots__ = ()

    def __init__(self, voField=b'vehiclesIDs', sortKey=vos_collections.VehicleInfoSortKey):
        super(EnemySortedIDsComposer, self).__init__(voField, sortKey)
        self._collectionClass = vos_collections.EnemyItemsCollection
        return

    def addSortIDs(self, isEnemy, arenaDP):
        super(EnemySortedIDsComposer, self).addSortIDs(isEnemy, arenaDP)
        return


class BiSortedIDsComposer(broker.BiDirectionComposer, ISortedIDsComposer):
    __slots__ = ()

    def addSortIDs(self, isEnemy, arenaDP):
        if isEnemy:
            self._right.addSortIDs(isEnemy, arenaDP)
        else:
            self._left.addSortIDs(isEnemy, arenaDP)
        return


class TeamsSortedIDsComposer(BiSortedIDsComposer):
    __slots__ = ()

    def __init__(self, sortKey=vos_collections.VehicleInfoSortKey):
        super(TeamsSortedIDsComposer, self).__init__(left=AllySortedIDsComposer(voField=b'leftItemsIDs', sortKey=sortKey), right=EnemySortedIDsComposer(voField=b'rightItemsIDs', sortKey=sortKey))
        return


class TeamsCorrelationIDsComposer(BiSortedIDsComposer):
    __slots__ = ()

    def __init__(self):
        sortKey = vos_collections.FragCorrelationSortKey
        super(TeamsCorrelationIDsComposer, self).__init__(left=AllySortedIDsComposer(voField=b'leftCorrelationIDs', sortKey=sortKey), right=EnemySortedIDsComposer(voField=b'rightCorrelationIDs', sortKey=sortKey))
        return


class TotalStatsComposer(broker.IExchangeComposer):
    __slots__ = (b'_stats',)

    def __init__(self):
        super(TotalStatsComposer, self).__init__()
        self._stats = {}
        return

    def clear(self):
        self._stats = None
        return

    def compose(self, data):
        if self._stats:
            data[b'totalStats'] = self._stats
        return data

    def addTotalStats(self, stats):
        self._stats = stats
        return


class VehicleInfoComponent(broker.ExchangeComponent):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __slots__ = (b'_data',)

    def __init__(self):
        super(VehicleInfoComponent, self).__init__()
        self._data = {}
        return

    def clear(self):
        self._data = {}
        super(VehicleInfoComponent, self).clear()
        return

    def get(self, forced=False):
        return self._data

    def addVehicleInfo(self, vInfoVO, overrides):
        vehicleID = vInfoVO.vehicleID
        vTypeVO = vInfoVO.vehicleType
        playerVO = vInfoVO.player
        accountDBID = playerVO.accountDBID
        sessionID = playerVO.avatarSessionID
        battleCtx = self.__sessionProvider.getCtx()
        isTeamKiller = playerVO.isTeamKiller or battleCtx.isTeamKiller(vehicleID, sessionID) or overrides.isTeamKiller(vInfoVO)
        parts = self._ctx.getPlayerFullName(vInfoVO)
        hasPrefixBadge = bool(vInfoVO.selectedBadge or vInfoVO.overriddenBadge)
        data = {b'accountDBID': accountDBID, 
           b'sessionID': sessionID, 
           b'playerName': (parts.playerName), 
           b'playerFakeName': (parts.playerFakeName), 
           b'playerFullName': (parts.playerFullName), 
           b'playerStatus': (overrides.getPlayerStatus(vInfoVO, isTeamKiller)), 
           b'clanAbbrev': (playerVO.clanAbbrev), 
           b'region': (parts.regionCode), 
           b'userTags': (self._ctx.getUserTags(sessionID, playerVO.igrType)), 
           b'squadIndex': (vInfoVO.squadIndex), 
           b'invitationStatus': (overrides.getInvitationDeliveryStatus(vInfoVO)), 
           b'vehicleID': vehicleID, 
           b'vehicleName': (vTypeVO.shortName), 
           b'vehicleType': (vTypeVO.getClassName()), 
           b'vehicleLevel': (vTypeVO.level), 
           b'vehicleIcon': (vTypeVO.iconPath), 
           b'vehicleIconName': (vTypeVO.iconName), 
           b'vehicleStatus': (vInfoVO.vehicleStatus), 
           b'isObserver': (vInfoVO.isObserver()), 
           b'vehicleAction': (overrides.getAction(vInfoVO)), 
           b'isVehiclePremiumIgr': (vTypeVO.isPremiumIGR), 
           b'teamColor': (overrides.getColorScheme()), 
           b'hasSelectedBadge': hasPrefixBadge}
        if vInfoVO.overriddenBadge:
            data[b'badge'] = {b'icon': ((b'override_badge_{}').format(vInfoVO.overriddenBadge)), b'content': None, 
               b'sizeContent': (ICONS_SIZES.X24), 
               b'isDynamic': False, 
               b'isAtlasSource': True}
        elif vInfoVO.selectedBadge:
            badgeID = vInfoVO.selectedBadge
            badge = buildBadge(badgeID, vInfoVO.getBadgeExtraInfo())
            if badge is not None:
                data[b'badge'] = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': True}, shortIconName=True)
        if vInfoVO.selectedSuffixBadge:
            data[b'suffixBadgeType'] = (b'badge_{}').format(vInfoVO.selectedSuffixBadge)
            data[b'suffixBadgeStripType'] = (b'strip_{}').format(vInfoVO.selectedSuffixBadge)
        return self._data.update(data)


class VehicleStatusComponent(broker.ExchangeComponent):
    __slots__ = (b'_vehicleID', b'_status', b'_idsComposers', b'_statsComposers', b'_dogTag')

    def __init__(self, idsComposers=None, statsComposers=None):
        super(VehicleStatusComponent, self).__init__()
        self._vehicleID = 0
        self._status = 0
        self._idsComposers = idsComposers or ()
        self._statsComposers = statsComposers or ()
        self._dogTag = None
        return

    def clear(self):
        self._vehicleID = 0
        self._status = 0
        for composer in self._idsComposers:
            composer.clear()

        for composer in self._statsComposers:
            composer.clear()

        super(VehicleStatusComponent, self).clear()
        return

    def get(self, forced=False):
        data = {b'isEnemy': (self._isEnemy), 
           b'vehicleID': (self._vehicleID), 
           b'status': (self._status)}
        if self._dogTag:
            data[b'dogTag'] = self._dogTag
        for composer in self._idsComposers:
            composer.compose(data)

        for composer in self._statsComposers:
            composer.compose(data)

        return data

    def addVehicleInfo(self, vInfoVO):
        self._vehicleID = vInfoVO.vehicleID
        self._status = vInfoVO.vehicleStatus
        self._dogTag = vInfoVO.dogTag
        return

    def addTotalStats(self, stats):
        for composer in self._statsComposers:
            composer.addTotalStats(stats)

        return

    def addSortIDs(self, arenaDP):
        for composer in self._idsComposers:
            composer.addSortIDs(self._isEnemy, arenaDP)

        return


class VehicleStatsComponent(broker.VehicleComponent):
    __slots__ = ()

    def addStats(self, vStatsVO):
        raise NotImplementedError
        return


class VehiclesExchangeBlock(broker.ExchangeBlock):
    __slots__ = (b'_idsComposers', b'_statsComposers')

    def __init__(self, itemComponent, positionComposer=None, idsComposers=None, statsComposers=None):
        super(VehiclesExchangeBlock, self).__init__(itemComponent, composer=positionComposer)
        self._idsComposers = idsComposers or ()
        self._statsComposers = statsComposers or ()
        return

    def clear(self):
        for composer in self._idsComposers:
            composer.clear()

        for composer in self._statsComposers:
            composer.clear()

        super(VehiclesExchangeBlock, self).clear()
        return

    def get(self, forced=False):
        data = super(VehiclesExchangeBlock, self).get(forced=forced)
        if data or forced:
            for composer in self._idsComposers:
                composer.compose(data)

            for composer in self._statsComposers:
                composer.compose(data)

        return data

    def addSortIDs(self, arenaDP, *flags):
        for composer in self._idsComposers:
            for flag in flags:
                composer.addSortIDs(flag, arenaDP)

        return

    def addTotalStats(self, stats):
        for composer in self._statsComposers:
            composer.addTotalStats(stats)

        return
