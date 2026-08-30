import logging
from functools import partial
import BigWorld, Math, CGF
from typing import TYPE_CHECKING
import cosmic_prefabs
from cosmic_sound import CosmicBattleSounds
from script_component.DynamicScriptComponent import DynamicScriptComponent
if TYPE_CHECKING:
    from typing import Optional
    from Vehicle import Vehicle
    from cgf_obsolete_script.script_game_object import ScriptGameObject
_logger = logging.getLogger(__name__)

class _BaseEffectComponent(object):

    def __init__(self, entity, prefab):
        self.__entity = entity
        self.__prefab = prefab
        _logger.debug(b'%s: init entity[%s], prefab[%s]', self.__class__.__name__, entity.id, prefab)
        return

    def _createVisual(self, translation=None):
        parent = self.__entity.entityGameObject
        _logger.debug(b'BaseEffectComponent: creating new visual. entity[%s], translation[%s]', self.__entity.id, translation)
        CGF.loadGameObjectIntoHierarchy(self.__prefab, parent, translation or Math.Vector3(), self._prefabLoaded)
        return

    def _prefabLoaded(self, gameObject):
        return


class _CollisionEffectComponent(_BaseEffectComponent):

    def __init__(self, entity, prefab):
        super(_CollisionEffectComponent, self).__init__(entity, prefab)
        self._gameObjects = set()
        return

    def _prefabLoaded(self, gameObject):
        _logger.debug(b'CollisionEffectComponent: prefabLoaded')
        self._gameObjects.add(gameObject)
        gameObject.activate()
        BigWorld.callback(1.0, partial(self._remove, gameObject))
        return

    def _remove(self, gameObject):
        _logger.debug(b'CollisionEffectComponent: removing gameObject %s. All gameObjects %s', gameObject, self._gameObjects)
        if gameObject not in self._gameObjects:
            return
        self._gameObjects.remove(gameObject)
        CGF.removeGameObject(gameObject)
        return

    def add(self, point):
        _logger.debug(b'CollisionEffectComponent: add gameObject at point[%s].', point)
        self._createVisual(point)
        return

    def clear(self):
        _logger.debug(b'CollisionEffectComponent: clearing up gameObjects: %s', self._gameObjects)
        for gameObject in self._gameObjects:
            CGF.removeGameObject(gameObject)

        self._gameObjects.clear()
        return


class _ShieldEffectComponent(_BaseEffectComponent):

    def __init__(self, entity, prefab):
        super(_ShieldEffectComponent, self).__init__(entity, prefab)
        self._gameObject = None
        self._createVisual()
        return

    def _prefabLoaded(self, gameObject):
        _logger.debug(b'ShieldEffectComponent: prefabLoaded')
        self._gameObject = gameObject
        if self._gameObject:
            self._gameObject.deactivate()
        return

    def activate(self):
        _logger.debug(b'ShieldEffectComponent: activating shield effect.')
        if self._gameObject is not None:
            self._gameObject.deactivate()
            self._gameObject.activate()
        return

    def clear(self):
        _logger.debug(b'ShieldEffectComponent: clearing up gameObject: %s', self._gameObject)
        if self._gameObject is not None:
            CGF.removeGameObject(self._gameObject)
        self._gameObject = None
        return


class VehicleImpulseScheduler(DynamicScriptComponent):

    def __init__(self, *_, **__):
        super(VehicleImpulseScheduler, self).__init__(*_, **__)
        self.__rammingFieldComponent = _ShieldEffectComponent(self.entity, cosmic_prefabs.Vehicle.RAMMING_FIELD)
        self.__collisionComponent = _CollisionEffectComponent(self.entity, cosmic_prefabs.Vehicle.COLLISION_EFFECT)
        return

    def onDestroy(self):
        self.__rammingFieldComponent.clear()
        self.__collisionComponent.clear()
        super(VehicleImpulseScheduler, self).onDestroy()
        return

    def set_impactPoint(self, oldValue):
        _logger.debug(b'set_impactpoint: impactPoint=%s', self.impactPoint)
        impactPoint = self.impactPoint
        localPoint = self._getLocalImpactPoint(impactPoint)
        self.__collisionComponent.add(localPoint)
        CosmicBattleSounds.playRammingSound(self.entity.position)
        return

    def onCollision(self):
        _logger.debug(b'onCollision - showing shield collision effect for vehicle[%d].', self.entity.id)
        self.__rammingFieldComponent.activate()
        return

    def _getLocalImpactPoint(self, globalPoint):
        mi = Math.Matrix(self.entity.matrix)
        mi.invert()
        return mi.applyPoint(globalPoint)
