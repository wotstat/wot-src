from gui.Scaleform.framework.entities.View import View

class BarracksMeta(View):

    def invalidateTanksList(self):
        self._printOverrideError(b'invalidateTanksList')
        return

    def setFilter(self, nation, role, tankType, location, nationID):
        self._printOverrideError(b'setFilter')
        return

    def onShowRecruitWindowClick(self, rendererData, menuEnabled):
        self._printOverrideError(b'onShowRecruitWindowClick')
        return

    def actTankman(self, dataCompact):
        self._printOverrideError(b'actTankman')
        return

    def buyBerths(self):
        self._printOverrideError(b'buyBerths')
        return

    def closeBarracks(self):
        self._printOverrideError(b'closeBarracks')
        return

    def setTankmenFilter(self):
        self._printOverrideError(b'setTankmenFilter')
        return

    def openPersonalCase(self, value, tabID):
        self._printOverrideError(b'openPersonalCase')
        return

    def onCountersVisited(self, visitedIds):
        self._printOverrideError(b'onCountersVisited')
        return

    def as_setTankmenS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmen(data)
        return

    def as_updateTanksListS(self, provider):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTanksList(provider)
        return

    def as_setTankmenFilterS(self, nation, role, tankType, location, nationID):
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmenFilter(nation, role, tankType, location, nationID)
        return

    def as_switchFilterEnableS(self, nationEnable, roleEnable, typeEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_switchFilterEnable(nationEnable, roleEnable, typeEnable)
        return

    def as_setCountersDataS(self, countersData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCountersData(countersData)
        return

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
        return
