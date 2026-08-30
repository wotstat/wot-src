from functools import partial
import BigWorld, helpers
from helpers.EffectsList import EffectsListPlayer

class StaticSceneBoundEffects(object):

    def __init__(self):
        super(StaticSceneBoundEffects, self).__init__()
        self._models = {}
        self.__incrementalEffectID = -1
        return

    def destroy(self):
        self._matProv = None
        for mID, elem in self._models.items():
            elem[b'effectsPlayer'].stop()
            model = elem[b'model']
            if model is not None:
                BigWorld.player().delModel(model)
            del self._models[mID]

        return

    def addNew(self, position, effectsList, keyPoints, callbackOnStop, **args):
        model = helpers.newFakeModel()
        model.position = position
        BigWorld.player().addModel(model)
        direction = args.get(b'dir')
        if direction is not None:
            model.rotate(direction.yaw, (0.0, 1.0, 0.0))
        self.__incrementalEffectID += 1
        effectID = self.__incrementalEffectID
        desc = dict()
        desc[b'model'] = model
        desc[b'effectsPlayer'] = EffectsListPlayer(effectsList, keyPoints, **args)
        desc[b'effectsPlayer'].play(model, None, partial(self.__callbackBeforeDestroy, effectID, callbackOnStop), args.get(b'waitForKeyOff', False))
        self._models[effectID] = desc
        return effectID

    def stop(self, effectID):
        if self._models.has_key(effectID):
            desc = self._models[effectID]
            desc[b'effectsPlayer'].stop()
            BigWorld.player().delModel(desc[b'model'])
            del self._models[effectID]
        return

    def __callbackBeforeDestroy(self, effectID, callbackOnStop):
        if callbackOnStop is not None:
            callbackOnStop()
        self.stop(effectID)
        return


class ModelBoundEffects(object):

    def __init__(self, model):
        self.__model = model
        self._effects = list()
        return

    def destroy(self):
        self.stop()
        self.__model = None
        return

    def stop(self, forceDelete=False):
        for elem in self._effects[:]:
            elem.stop(forceDelete=forceDelete)
            self._effects.remove(elem)

        return

    def addNew(self, matProv, effectsList, keyPoints, waitForKeyOff=False, **args):
        return self.addNewToNode(b'', matProv, effectsList, keyPoints, waitForKeyOff, **args)

    def addNewToNode(self, node, matProv, effectsList, keyPoints, waitForKeyOff=False, excludeTags=None, **args):
        if not node and matProv is None:
            position = None
        else:
            position = (
             node, matProv)
        desc = EffectsListPlayer(effectsList, keyPoints, position=position, excludeTags=excludeTags, **args)
        desc.play(self.__model, None, partial(self._effects.remove, desc), waitForKeyOff)
        self._effects.append(desc)
        return desc

    def reattachTo(self, model):
        self.__model = model
        for elem in self._effects:
            elem.reattachTo(model)

        return
