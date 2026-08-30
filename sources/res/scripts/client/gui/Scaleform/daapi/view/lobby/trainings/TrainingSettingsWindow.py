from __future__ import absolute_import
from future.utils import viewitems
import ArenaType
from account_helpers import gameplay_ctx
from constants import PREBATTLE_TYPE, Configs
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.meta.TrainingWindowMeta import TrainingWindowMeta
from gui.prb_control import prbEntityProperty
from gui.prb_control.prb_getters import getTrainingBattleRoundLimits
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.utils.functions import getArenaImage
from helpers import dependency
from gui.impl import backport
from gui.impl.gen import R
from gui.training_room_external_handlers import getAllTrainingRoomHandlers, getTrainingRoomHandler
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
CONFIG_KEYS_FOR_UPDATE = {
 Configs.PRE_MODERATION_CONFIG.value}

class ArenasCache(object):
    __lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self, ctx, settings):
        self.__cache = []
        self.__isEpic = ctx.get(b'isEpic', False)
        self.__settings = settings
        self.build()
        return

    def fini(self):
        self.__cache = []
        return

    @property
    def cache(self):
        return self.__cache

    def build(self):
        cache = []
        for arenaTypeID, arenaType in viewitems(ArenaType.g_cache):
            if not self.__isArenaSuitableForTraining(arenaType):
                continue
            try:
                arenaTypeName = self.__getArenaTypeName(arenaType)
                dataItem = {b'label': (b'%s - %s' % (arenaType.name, arenaTypeName) if arenaTypeName else arenaType.name), 
                   b'name': (arenaType.name), 
                   b'arenaType': arenaTypeName, 
                   b'key': arenaTypeID, 
                   b'size': (arenaType.maxPlayersInTeam), 
                   b'time': (arenaType.roundLength // 60), 
                   b'description': b'', 
                   b'icon': (getArenaImage(arenaType.geometryName)), 
                   b'canChangeArenaTime': (not self.__isEpic), 
                   b'alertText': b''}
                arenaData = self.__getHandlerForArenaTypeName(arenaType.gameplayName).getArenaData()
                if arenaData is not None:
                    dataItem.update(arenaData)
                cache.append(dataItem)
            except Exception:
                LOG_ERROR(b'There is error while reading arenas cache', arenaTypeID, arenaType)
                LOG_CURRENT_EXCEPTION()
                continue

        self.__cache = sorted(cache, key=(lambda x: (x[b'label'].lower(), x[b'name'].lower())))
        return

    def __getArenaTypeName(self, arena):
        if arena.gameplayName == b'ctf':
            return b''
        arenaGameplayName = R.strings.arenas.type.dyn(arena.gameplayName).dyn(arena.geometryName)
        if arenaGameplayName.exists():
            return backport.text(arenaGameplayName)
        return backport.text(R.strings.arenas.type.dyn(arena.gameplayName).name())

    def __isArenaSuitableForTraining(self, arena):
        if arena.explicitRequestOnly:
            return False
        else:
            arenaTypeFilter = self.__getHandlerForArenaTypeName(arena.gameplayName).getArenaFilter()
            if arenaTypeFilter is not None and not self.__isEpic:
                return arenaTypeFilter(arena, self.__settings)
            return gameplay_ctx.isCreationEnabled(arena.gameplayName, self.__isEpic)

    def __getHandlerForArenaTypeName(self, arenaTypeName):
        handlers = getAllTrainingRoomHandlers()
        for handler in handlers:
            if handler.isEnabledForGuiTypeName(arenaTypeName):
                return handler

        return getTrainingRoomHandler()


class TrainingSettingsWindow(TrainingWindowMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, ctx=None):
        super(TrainingSettingsWindow, self).__init__()
        self.__isCreateRequest = ctx.get(b'isCreateRequest', False)
        self.__settings = ctx.get(b'settings', None)
        self.__isEpic = self.__settings.getEntityType() == PREBATTLE_TYPE.EPIC_TRAINING
        self.__arenasCache = ArenasCache({b'isEpic': (self.__isEpic)}, self.__settings)
        return

    @prbEntityProperty
    def prbEntity(self):
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _populate(self):
        super(TrainingSettingsWindow, self)._populate()
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self.__updateVO()
        return

    def _dispose(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self.__arenasCache.fini()
        super(TrainingSettingsWindow, self)._dispose()
        return

    def getInfo(self):
        if not self.__isCreateRequest:
            self.__settings = self.__settings.fetch(self.prbEntity.getSettings())
        if self.itemsCache.isSynced():
            accountAttrs = self.itemsCache.items.stats.attributes
        else:
            accountAttrs = 0
        minBound, maxBound = getTrainingBattleRoundLimits(accountAttrs)
        if self.__isEpic:
            rTitle = R.strings.menu.epic_training.create.title() if self.__isCreateRequest else R.strings.menu.epic_training.info.settings.title()
        else:
            rTitle = R.strings.menu.training.create.title() if self.__isCreateRequest else R.strings.menu.training.info.settings.title()
        canChangeComment = isShowComment = self.__isDescriptionEnabled()
        info = {b'description': (self.__settings.getComment()), 
           b'timeout': (self.__settings.getRoundLen() // 60), 
           b'arena': (self.__settings.getArenaTypeID()), 
           b'privacy': (not self.__settings.isOpened()), 
           b'create': (self.__isCreateRequest), 
           b'wndTitle': (backport.text(rTitle)), 
           b'canMakeOpenedClosed': True, 
           b'canChangeComment': canChangeComment, 
           b'isShowComment': isShowComment, 
           b'canChangeArena': True, 
           b'minBattleTime': (minBound // 60), 
           b'maxBattleTime': (maxBound // 60)}
        if not self.__isCreateRequest:
            permissions = self.prbEntity.getPermissions()
            info[b'canMakeOpenedClosed'] = permissions.canMakeOpenedClosed()
            info[b'canChangeComment'] = permissions.canChangeComment() and canChangeComment
            info[b'canChangeArena'] = permissions.canChangeArena()
        return info

    def updateTrainingRoom(self, key, time, isPrivate, description):
        self.__settings.setArenaTypeID(key)
        self.__settings.setRoundLen(time * 60)
        self.__settings.setOpened(not isPrivate)
        self.__settings.setComment(description)
        if self.__isEpic:
            eventType = events.TrainingSettingsEvent.UPDATE_EPIC_TRAINING_SETTINGS
        else:
            eventType = events.TrainingSettingsEvent.UPDATE_TRAINING_SETTINGS
        self.fireEvent(events.TrainingSettingsEvent(eventType, ctx={b'settings': (self.__settings)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __updateVO(self):
        self.as_setDataS(self.getInfo(), self.__arenasCache.cache)
        return

    def __onServerSettingsChange(self, diff):
        if CONFIG_KEYS_FOR_UPDATE.intersection(diff.keys()):
            self.__arenasCache.build()
            self.__updateVO()
        return

    def __isDescriptionEnabled(self):
        return self.__lobbyContext.getServerSettings().preModerationConfig.prebattleDescriptionEnabled
