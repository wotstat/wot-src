from enum import Enum
from typing import TYPE_CHECKING
from helpers import dependency
from shared_utils import getFullClassName
if TYPE_CHECKING:
    from typing import Any, Optional

class SettingsTarget(Enum):
    CLIENT = b'client'


class ISettingsProvider(object):
    TARGET = None

    def get(self, name, key, default=None):
        raise NotImplementedError
        return

    def set(self, name, key, value):
        raise NotImplementedError
        return

    def load(self, name):
        raise NotImplementedError
        return

    def dump(self, name, version):
        raise NotImplementedError
        return

    def drop(self, name):
        raise NotImplementedError
        return

    def dropUnused(self):
        raise NotImplementedError
        return


class ISettingsRepository(object):

    def get(self, name, key, default=None):
        raise NotImplementedError
        return

    def set(self, name, key, value):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def load(self, settingsSerializable):
        raise NotImplementedError
        return

    def dump(self, settingsSerializable):
        raise NotImplementedError
        return

    def drop(self, settingsSerializable):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return


class SettingsSerializable(object):
    TARGET = SettingsTarget.CLIENT
    VERSION = 0
    __settingsRepository = dependency.descriptor(ISettingsRepository)

    @classmethod
    def getSettingsID(cls):
        return getFullClassName(cls)

    def getSetting(self, key, default=None):
        return self.__settingsRepository.get(self, key, default)

    def setSetting(self, key, value):
        self.__settingsRepository.set(self, key, value)
        return

    def _loadSettings(self):
        self.__settingsRepository.load(self)
        return

    def _dumpSettings(self):
        self.__settingsRepository.dump(self)
        return
