import ArenaType
from account_helpers import gameplay_ctx
from constants import PREBATTLE_TYPE, Configs
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.lobby.trainings import formatters
from gui.Scaleform.daapi.view.meta.TrainingWindowMeta import TrainingWindowMeta
from gui.prb_control import prbEntityProperty
from gui.prb_control.prb_getters import getTrainingBattleRoundLimits
from gui.shared import events, EVENT_BUS_SCOPE
from helpers import dependency
from helpers import i18n
from gui.impl import backport
from gui.impl.gen import R
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from uilogging.rename_testing.loggers import RenameTestingUILogger

class ArenasCache(object):

    def __init__(self, ctx):
        self.__cache = []
        self.__isEpic = ctx.get(b'isEpic', False)
        for arenaTypeID, arenaType in ArenaType.g_cache.iteritems():
            if arenaType.explicitRequestOnly or not gameplay_ctx.isCreationEnabled(arenaType.gameplayName, self.__isEpic):
                continue
            try:
                nameSuffix = b''
                if arenaType.gameplayName != b'ctf':
                    arenaGameplayName = b'#arenas:type/%s/%s/name' % (arenaType.gameplayName, arenaType.geometryName)
                    if i18n.doesTextExist(arenaGameplayName):
                        nameSuffix = i18n.makeString(arenaGameplayName)
                    else:
                        nameSuffix = i18n.makeString(b'#arenas:type/%s/name' % arenaType.gameplayName)
                self.__cache.append({b'label': (b'%s - %s' % (arenaType.name, nameSuffix) if nameSuffix else arenaType.name), 
                   b'name': (arenaType.name), 
                   b'arenaType': nameSuffix, 
                   b'key': arenaTypeID, 
                   b'size': (arenaType.maxPlayersInTeam), 
                   b'time': (arenaType.roundLength / 60), 
                   b'description': b'', 
                   b'icon': (formatters.getMapIconPath(arenaType))})
            except Exception:
                LOG_ERROR(b'There is error while reading arenas cache', arenaTypeID, arenaType)
                LOG_CURRENT_EXCEPTION()
                continue

        self.__cache = sorted(self.__cache, key=(lambda x: (
         x[b'label'].lower(), x[b'name'].lower())))
        return

    @property
    def cache(self):
        return self.__cache


class TrainingSettingsWindow(TrainingWindowMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, ctx=None):
        super(TrainingSettingsWindow, self).__init__()
        self.__isCreateRequest = ctx.get(b'isCreateRequest', False)
        self.__settings = ctx.get(b'settings', None)
        self.__isEpic = self.__settings.getEntityType() == PREBATTLE_TYPE.EPIC_TRAINING
        self.__arenasCache = ArenasCache({b'isEpic': (self.__isEpic)})
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
        super(TrainingSettingsWindow, self)._dispose()
        return

    def getMapsData(self):
        return self.__arenasCache.cache

    def getInfo(self):
        if not self.__isCreateRequest:
            self.__settings = self.__settings.fetch(self.prbEntity.getSettings())
        _, maxBound = getTrainingBattleRoundLimits()
        if self.__isEpic:
            rTitle = R.strings.menu.epic_training.create.title() if self.__isCreateRequest else R.strings.menu.epic_training.info.settings.title()
        else:
            rTitle = R.strings.menu.training.create.title() if self.__isCreateRequest else R.strings.menu.training.info.settings.title()
        canChangeComment = isShowComment = self.__isDescriptionEnabled()
        info = {b'description': (self.__settings.getComment()), 
           b'timeout': (self.__settings.getRoundLen() / 60), 
           b'arena': (self.__settings.getArenaTypeID()), 
           b'privacy': (not self.__settings.isOpened()), 
           b'create': (self.__isCreateRequest), 
           b'wndTitle': (backport.text(rTitle)), 
           b'canMakeOpenedClosed': True, 
           b'canChangeComment': canChangeComment, 
           b'isShowComment': isShowComment, 
           b'canChangeArenaTime': (not self.__isEpic), 
           b'canChangeArena': True, 
           b'maxBattleTime': (maxBound / 60)}
        if not self.__isCreateRequest:
            permissions = self.prbEntity.getPermissions()
            info[b'canMakeOpenedClosed'] = permissions.canMakeOpenedClosed()
            info[b'canChangeComment'] = permissions.canChangeComment() and canChangeComment
            info[b'canChangeArena'] = permissions.canChangeArena()
        return info

    def updateTrainingRoom(self, arena, roundLength, isPrivate, comment):
        if self.__isCreateRequest and not self.__isEpic:
            RenameTestingUILogger().logTrainingCreateRoom()
        self.__settings.setArenaTypeID(arena)
        self.__settings.setRoundLen(roundLength * 60)
        self.__settings.setOpened(not isPrivate)
        self.__settings.setComment(comment)
        if self.__isEpic:
            eventType = events.TrainingSettingsEvent.UPDATE_EPIC_TRAINING_SETTINGS
        else:
            eventType = events.TrainingSettingsEvent.UPDATE_TRAINING_SETTINGS
        self.fireEvent(events.TrainingSettingsEvent(eventType, ctx={b'settings': (self.__settings)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __updateVO(self):
        self.as_setDataS(self.getInfo(), self.getMapsData())
        return

    def __onServerSettingsChange(self, diff):
        if Configs.PRE_MODERATION_CONFIG.value in diff:
            self.__updateVO()
        return

    def __isDescriptionEnabled(self):
        return self.__lobbyContext.getServerSettings().preModerationConfig.prebattleDescriptionEnabled
