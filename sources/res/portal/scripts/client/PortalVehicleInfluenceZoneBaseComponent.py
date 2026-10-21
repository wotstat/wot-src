import BigWorld
from abc import ABCMeta, abstractmethod

class PortalVehicleInfluenceZoneBaseComponent(BigWorld.DynamicScriptComponent):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(PortalVehicleInfluenceZoneBaseComponent, self).__init__()
        if self.__isAppearanceReady():
            self.__onAppearanceReady()
        else:
            self.entity.onAppearanceReady += self.__onAppearanceReady
        return

    def onDestroy(self):
        self.entity.onAppearanceReady -= self.__onAppearanceReady
        return

    def __isAppearanceReady(self):
        appearance = self.entity.appearance
        return appearance is not None and appearance.isConstructed

    def __onAppearanceReady(self):
        self.onAppearanceReady()
        return

    @abstractmethod
    def onAppearanceReady(self):
        raise NotImplementedError
        return
