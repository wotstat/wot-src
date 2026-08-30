from skeletons.gui.game_control import IPlatoonController
from visual_script.block import Meta, Block
from visual_script.dependency import dependencyImporter
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE
dependency, shared, events = dependencyImporter(b'helpers.dependency', b'gui.shared', b'gui.shared.events')

class PlatoonMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16758861

    @classmethod
    def blockCategory(cls):
        return b'Platoon'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/platoon'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class OnPlatoonStateChanged(Block, PlatoonMeta):
    _PLAYER_INDEX = -1
    _platoonController = dependency.descriptor(IPlatoonController)

    def __init__(self, *args, **kwargs):
        super(OnPlatoonStateChanged, self).__init__(*args, **kwargs)
        self._subscribe = self._makeEventInputSlot(b'subscribe', self.__subscribe)
        self._unsubscribe = self._makeEventInputSlot(b'unsubscribe', self.__unsubscribe)
        self._subscribeOut = self._makeEventOutputSlot(b'subscribeOut')
        self._unsubscribeOut = self._makeEventOutputSlot(b'unsubscribeOut')
        self._onPlatoonEnter = self._makeEventOutputSlot(b'onPlatoonEnter')
        self._onPlatoonExit = self._makeEventOutputSlot(b'onPlatoonExit')
        self._onPlayerEnter = self._makeEventOutputSlot(b'onPlayerEnter')
        self._onPlayerExit = self._makeEventOutputSlot(b'onPlayerExit')
        self._index = self._makeDataOutputSlot(b'index', SLOT_TYPE.INT, None)
        return

    def __subscribe(self):
        shared.g_eventBus.addListener(events.HangarVehicleEvent.ON_PLATOON_TANK_LOADED, self.__onPlatoonTankEnter, scope=shared.EVENT_BUS_SCOPE.LOBBY)
        shared.g_eventBus.addListener(events.HangarVehicleEvent.ON_PLATOON_TANK_DESTROY, self.__onPlatoonTankLeave, scope=shared.EVENT_BUS_SCOPE.LOBBY)
        self._platoonController.onPlatoonTankVisualizationChanged += self.__enablePlatoonLighting
        self._subscribeOut.call()
        return

    def __unsubscribe(self):
        shared.g_eventBus.removeListener(events.HangarVehicleEvent.ON_PLATOON_TANK_LOADED, self.__onPlatoonTankEnter, scope=shared.EVENT_BUS_SCOPE.LOBBY)
        shared.g_eventBus.removeListener(events.HangarVehicleEvent.ON_PLATOON_TANK_DESTROY, self.__onPlatoonTankLeave, scope=shared.EVENT_BUS_SCOPE.LOBBY)
        self._platoonController.onPlatoonTankVisualizationChanged -= self.__enablePlatoonLighting
        self._unsubscribeOut.call()
        return

    def __onPlatoonTankEnter(self, event):
        entity = event.ctx[b'entity']
        self._index.setValue(entity.slotIndex)
        self._onPlatoonEnter.call()
        return

    def __onPlatoonTankLeave(self, event):
        entity = event.ctx[b'entity']
        self._index.setValue(entity.slotIndex)
        self._onPlatoonExit.call()
        return

    def __enablePlatoonLighting(self, isEnabled):
        self._index.setValue(self._PLAYER_INDEX)
        if isEnabled:
            self._onPlayerEnter.call()
        else:
            self._onPlayerExit.call()
        return
