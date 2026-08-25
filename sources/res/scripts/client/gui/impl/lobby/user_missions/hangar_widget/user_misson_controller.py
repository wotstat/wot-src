import Event
from PlayerEvents import g_playerEvents
from config_schemas.umg import WeightsModel
from config_schemas.umg import umgMissionsConfigSchema
from config_schemas.umg_config import umgConfigSchema
from gui.impl.lobby.user_missions.hangar_widget.providers.quest_providers import DailyQuestProvider, PremiumQuestProvider, WeeklyQuestProvider, QuestProviderBase
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.game_control import IGameSessionController
import typing

class MissionLoader(object):
    __slots__ = (b'providers',)

    def __init__(self):
        self.providers = []
        return

    def addProviders(self, providers):
        self.providers.extend(providers)
        return

    def loadQuests(self):
        allQuests = []
        for provider in self.providers:
            allQuests.extend(provider.getQuests())

        return allQuests

    def updateConfig(self, config):
        for provider in self.providers:
            provider.updateConfig(config)

        return

    def destroy(self):
        for provider in self.providers:
            provider.destroy()

        self.providers = []
        return


class MissionInitializer(object):
    __slots__ = (b'eventsCache', b'loader', b'config')

    def __init__(self, loader, eventsCache):
        self.eventsCache = eventsCache
        self.loader = loader
        self.config = None
        return

    def initialize(self):
        config = umgMissionsConfigSchema.getModel()
        dailyProvider = DailyQuestProvider(self.eventsCache, config)
        premiumProvider = PremiumQuestProvider(self.eventsCache, config)
        weeklyProvider = WeeklyQuestProvider(self.eventsCache, config)
        self.loader.addProviders([dailyProvider, premiumProvider, weeklyProvider])
        return

    def destroy(self):
        self.eventsCache = None
        self.loader = None
        return


class MissionController(object):
    eventsCache = dependency.descriptor(IEventsCache)
    gameSession = dependency.descriptor(IGameSessionController)

    def __init__(self):
        self.quests = []
        self.initializer = None
        self.loader = None
        self.onChanged = Event.Event()
        self.initData()
        return

    def initData(self):
        self.loader = MissionLoader()
        self.initializer = MissionInitializer(self.loader, self.eventsCache)
        self.initializer.initialize()
        self.refresh()
        self.subscribe()
        return

    def subscribe(self):
        self.eventsCache.onSyncCompleted += self._onSyncCompleted
        self.gameSession.onPremiumTypeChanged += self._onPremiumTypeChanged
        g_playerEvents.onConfigModelUpdated += self.__onConfigModelUpdated
        return

    def unsubscribe(self):
        self.eventsCache.onSyncCompleted -= self._onSyncCompleted
        self.gameSession.onPremiumTypeChanged -= self._onPremiumTypeChanged
        g_playerEvents.onConfigModelUpdated -= self.__onConfigModelUpdated
        return

    def refresh(self):
        self.quests = self.loader.loadQuests()
        self.onChanged()
        return

    def getSortedQuests(self):
        return sorted(self.quests, key=(lambda q: (-q.weight, tuple(-x for x in q.secondaryKey))))

    def destroy(self):
        self.unsubscribe()
        self.loader.destroy()
        self.loader = None
        self.initializer.destroy()
        self.initializer = None
        return

    def _onSyncCompleted(self, *args, **kwargs):
        self.refresh()
        return

    def _onPremiumTypeChanged(self, *args, **kwargs):
        self.refresh()
        return

    def __onConfigModelUpdated(self, gpKey):
        if umgMissionsConfigSchema.gpKey == gpKey:
            self.loader.updateConfig(umgMissionsConfigSchema.getModel())
            self.refresh()
        elif umgConfigSchema.gpKey == gpKey:
            self.refresh()
        return
