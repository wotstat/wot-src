from __future__ import absolute_import
from visual_script.misc import ASPECT

class PerkContextImplBase(object):

    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID):
        self._perksController = perksControllerWeakRef
        self._perkLevel = perkLevel
        self.perkID = perkID
        self.scopeID = scopeID
        self.vehicleID = perksControllerWeakRef.vehicleID
        return

    @property
    def vehicle(self):
        raise NotImplementedError
        return

    @property
    def perkLevel(self):
        raise NotImplementedError
        return

    @perkLevel.setter
    def perkLevel(self, value):
        raise NotImplementedError
        return

    def addFactorModifier(self, factor, value):
        raise NotImplementedError
        return

    def removeFactorModifiers(self, factor, numMods):
        raise NotImplementedError
        return

    def dropAllPerkModifiers(self):
        raise NotImplementedError
        return

    def notifyOnClient(self, *_):
        raise NotImplementedError
        return

    def notifyOnClientRibbon(self, *_):
        raise NotImplementedError
        return


class CrewContextImplBase(PerkContextImplBase):
    ASPECT = ASPECT.ALL

    def __init__(self, perksControllerWeakRef, perkID, perkLevel, scopeID, tmanIdxs):
        super(CrewContextImplBase).__init__(perksControllerWeakRef, perkID, perkLevel, scopeID)
        self._levelOverride = False
        self._tmanIdxs = tmanIdxs
        return
