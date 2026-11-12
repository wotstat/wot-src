class RaidConfig(object):
    __slots__ = (b'_config',)

    def __init__(self, config=None):
        self._config = config or {}
        return

    def isEnabled(self):
        return self._config.get(b'isEnabled', False)

    def getTamagotchiUrl(self):
        return self._config.get(b'tamagotchiUrl')

    def getRaidBoost(self):
        return self._config.get(b'raidBoost')
