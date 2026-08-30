from abc import ABCMeta, abstractmethod
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from tutorial.control import TutorialProxyHolder
from tutorial.logger import LOG_MEMORY, LOG_ERROR
import SoundGroups, Event
__all__ = (b'StartReqs', b'BonusesRequester', b'SoundPlayer', b'GlobalStorage', b'SOUND_EVENT')

class StartReqs(object):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __del__(self):
        LOG_MEMORY((b'StartReqs deleted: {0:>s}').format(self))
        return

    def isEnabled(self):
        return False

    def prepare(self, ctx):
        raise NotImplementedError
        return

    def process(self, descriptor, ctx):
        raise NotImplementedError
        return


class BonusesRequester(TutorialProxyHolder):
    __meta__ = ABCMeta

    def __init__(self, completed):
        super(BonusesRequester, self).__init__()
        self._completed = completed
        return

    def getCompleted(self):
        return self._completed

    def setCompleted(self, completed):
        self._completed = completed
        return

    def isStillRunning(self):
        return False

    def getChapter(self, chapterID=None):
        chapter = self._data
        if chapterID:
            chapter = self._descriptor.getChapter(chapterID)
        return chapter

    @abstractmethod
    def request(self, chapterID=None):
        return


class SOUND_EVENT(object):
    HINT_SHOWN = 4
    ANIMATION_STARTED = 5


class SoundPlayer(object):
    __meta__ = ABCMeta

    def __init__(self):
        super(SoundPlayer, self).__init__()
        self._muted = False
        self._enabled = False
        return

    def setMuted(self, value):
        self._muted = value
        return

    def isMuted(self):
        return self._muted

    def setEnabled(self, value):
        self._enabled = value
        return

    def isEnabled(self):
        return self._enabled

    @abstractmethod
    def play(self, event, sndID=None):
        return

    @abstractmethod
    def stop(self):
        return

    def isPlaying(self, event, sndID=None):
        return False

    def goToNextChapter(self):
        return


class NoSound(SoundPlayer):

    def play(self, event, sndID=None):
        return

    def stop(self):
        return


class SimpleSoundPlayer(SoundPlayer):

    def play(self, _, sndID=None):
        if sndID is not None:
            SoundGroups.g_instance.playSound2D(sndID)
        else:
            LOG_ERROR(b'No sound event specified for SimpleSoundPlayer')
        return

    def stop(self):
        return


class GLOBAL_FLAG(object):
    MAY_PAWN_PERSONAL_MISSION = b'_MayPawnPersonalMission'
    HAVE_NEW_BADGE = b'_HaveNewBadge'
    LOBBY_MENU_ITEM_MANUAL = b'_LobbyMenuItemManual'
    HAVE_NEW_SUFFIX_BADGE = b'_HaveNewSuffixBadge'
    BADGE_PAGE_HAS_NEW_SUFFIX_BADGE = b'_BadgePageHasNewSuffixBadge'
    COLLECTIBLE_VEHICLE_PREVIEW_ENABLED = b'_CollectibleVehiclePreviewEnabled'
    DOGTAGS_ENABLED = b'_DogTagsEnabled'
    HAVE_NEW_ANIMATED_DOGTAG = b'_HaveNewAnimatedDogTag'
    VEH_POST_PROGRESSION_ENABLED = b'_VehPostProgressionEnabled'
    HANGAR_VEH_POST_PROGRESSION_PURCHASABLE = b'_HangarVehPostProgressionPurchasable'
    RESEARCH_VEH_POST_PROGRESSION_PURCHASABLE = b'_ResearchVehPostProgressionPurchasable'
    VISITED_ACHIEVEMENTS_FROM_NOTIFICATION = b'_VisitedAchievementsFromNotification'
    UNLOCKED_3D_CUSTOMIZATION = b'_Unlocked3DCustomization'
    ALL = (
     MAY_PAWN_PERSONAL_MISSION,
     HAVE_NEW_BADGE, HAVE_NEW_SUFFIX_BADGE, BADGE_PAGE_HAS_NEW_SUFFIX_BADGE,
     COLLECTIBLE_VEHICLE_PREVIEW_ENABLED, DOGTAGS_ENABLED,
     HAVE_NEW_ANIMATED_DOGTAG, VISITED_ACHIEVEMENTS_FROM_NOTIFICATION,
     UNLOCKED_3D_CUSTOMIZATION)


class GlobalStorage(object):
    __slots__ = (b'attribute',)
    __storage = {}
    __default = {}
    onSetValue = Event.Event()

    def __init__(self, attribute, defaultValue):
        self.attribute = attribute
        if attribute not in self.__storage:
            self.__storage[attribute] = defaultValue
        return

    def __repr__(self):
        return (b'GlobalStorage {0:s}: {1!r:s}').format(self.attribute, self.__storage.get(self.attribute))

    def __set__(self, _, value):
        self.__storage[self.attribute] = value
        return

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        else:
            return self.__storage[self.attribute]

    def value(self):
        return self.__storage[self.attribute]

    @classmethod
    def setFlags(cls, flags):
        for flag, value in flags.iteritems():
            if flag not in GLOBAL_FLAG.ALL:
                LOG_ERROR(b'It is not global flag', flag)
                continue
            cls.__storage[flag] = value

        return

    @classmethod
    def clearFlags(cls):
        if not cls.__storage:
            return
        for flag in GLOBAL_FLAG.ALL:
            if flag in cls.__storage:
                cls.__storage[flag] = False

        return

    @classmethod
    def all(cls):
        return cls.__storage.copy()

    @classmethod
    def getValue(cls, attribute):
        result = None
        if attribute in cls.__storage:
            result = cls.__storage[attribute]
        return result

    @classmethod
    def setValue(cls, attribute, value, showImmediately=True):
        oldValue = cls.__storage.get(attribute)
        if oldValue != value:
            cls.__storage[attribute] = value
            if showImmediately:
                cls.onSetValue(attribute, value)
        return
