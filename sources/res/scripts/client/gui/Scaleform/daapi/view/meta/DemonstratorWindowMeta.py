from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class DemonstratorWindowMeta(AbstractWindowView):

    def onGameplaySelected(self, index):
        self._printOverrideError(b'onGameplaySelected')
        return

    def onLvlSelected(self, index):
        self._printOverrideError(b'onLvlSelected')
        return

    def onSpawnSelected(self, index):
        self._printOverrideError(b'onSpawnSelected')
        return

    def onMapSelected(self, index):
        self._printOverrideError(b'onMapSelected')
        return

    def onBattleStart(self):
        self._printOverrideError(b'onBattleStart')
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_setGameplayTabsS(self, tabList, selectedTab):
        if self._isDAAPIInited():
            return self.flashObject.as_setGameplayTabs(tabList, selectedTab)
        return

    def as_setSpawnsS(self, spawnList, selectedSpawn):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpawns(spawnList, selectedSpawn)
        return

    def as_setLevelsS(self, lvlList, selectedLvl):
        if self._isDAAPIInited():
            return self.flashObject.as_setLevels(lvlList, selectedLvl)
        return

    def as_enablePlatoonWarningS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enablePlatoonWarning(value)
        return

    def as_enableExtendedSettingsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableExtendedSettings(value)
        return

    def as_enableBattleButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableBattleButton(value)
        return
