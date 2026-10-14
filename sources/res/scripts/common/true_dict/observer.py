from __future__ import absolute_import
from typing import Any, List, Tuple

class _TrueDictObserverBase(object):

    def onTrueDictAdded(self, propertyName, keyName):
        return

    def onTrueDictUpdated(self, propertyName, keyName, oldValue):
        return

    def onTrueDictRemoved(self, propertyName, keyName, oldValue):
        return

    def _observeNested(self, propertyName, changePath, oldValue):
        prop, index = changePath[0], changePath[1]
        keys, values = self._window(propertyName, index, index + 1)
        if not keys:
            return
        if prop == b'values':
            self.onTrueDictUpdated(propertyName, keys[0], oldValue)
        elif prop == b'keys':
            oldKey, newKey = oldValue, keys[0]
            if oldKey != newKey:
                self.onTrueDictRemoved(propertyName, oldKey, values[0])
                self.onTrueDictAdded(propertyName, newKey)
        return

    def _observeSlice(self, propertyName, changePath, oldValue):
        prop = changePath[0]
        if prop == b'values' and len(changePath) > 2 and isinstance(changePath[-1], (tuple, list)):
            index = changePath[1]
            keys, _ = self._window(propertyName, index, index + 1)
            if keys:
                self.onTrueDictUpdated(propertyName, keys[0], oldValue)
            return
        start, end = self._sliceBounds(changePath)
        oldSlice = list(oldValue)
        newKeys, newValues = self._window(propertyName, start, end)
        if prop == b'values' and start < end and oldSlice:
            for offset, newVal in enumerate(newValues):
                if offset < len(oldSlice) and oldSlice[offset] != newVal:
                    self.onTrueDictUpdated(propertyName, newKeys[offset], oldSlice[offset])

            return
        slot = self._pending().setdefault(propertyName, {})
        if prop == b'keys':
            slot[b'addedItems'] = [key for key in newKeys if key not in oldSlice]
            slot[b'removedItems'] = [key for key in oldSlice if key not in newKeys]
        else:
            slot[b'prevValues'] = oldSlice
        if b'addedItems' in slot and b'prevValues' in slot:
            del self._pending()[propertyName]
            for key in slot[b'addedItems']:
                self.onTrueDictAdded(propertyName, key)

            for key, oldVal in zip(slot[b'removedItems'], slot[b'prevValues']):
                self.onTrueDictRemoved(propertyName, key, oldVal)

        return

    def _window(self, propertyName, start, end):
        trueDict = getattr(self, propertyName, None)
        if trueDict is None:
            return ([], [])
        else:
            return trueDict.positionalSlice(start, end)

    def _pending(self):
        return self.__dict__.setdefault(b'_truedict_pending', {})

    @staticmethod
    def _sliceBounds(changePath):
        spec = changePath[1]
        if isinstance(spec, (tuple, list)):
            return (spec[0], spec[1])
        return (
         changePath[-2], changePath[-1])


def TrueDictObserverMixin(propertyName):

    def _setNested(self, changePath, oldValue):
        self._observeNested(propertyName, changePath, oldValue)
        return

    def _setSlice(self, changePath, oldValue):
        self._observeSlice(propertyName, changePath, oldValue)
        return

    attrs = {(b'setNested_%s' % propertyName): _setNested, 
       (b'setSlice_%s' % propertyName): _setSlice}
    return type(b'TrueDictObserverMixin_%s' % propertyName, (
     _TrueDictObserverBase,), attrs)
