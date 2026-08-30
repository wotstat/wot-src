from __future__ import absolute_import
import logging
from collections import namedtuple
from future.utils import viewitems
from shared_utils import makeTupleByDict
_logger = logging.getLogger(__name__)

class BundlesConfig(object):
    __slots__ = (b'__bundles',)

    def __init__(self, config):
        if config is not None:
            self.__bundles = {bundleID: BundleConfig(**bundle) for bundleID, bundle in viewitems(config)}
        else:
            self.__bundles = {}
        return

    def getBundleIDs(self):
        return list(self.__bundles.keys())

    def getBundles(self):
        return list(self.__bundles.values())

    def getBundle(self, bundleID):
        if bundleID in self.__bundles:
            return self.__bundles[bundleID]
        _logger.error(b'Trying to get non-existing bundle by ID: %s', bundleID)
        return BundleConfig.defaults()


class BundleConfig(namedtuple(b'_BundleConfig', (b'enabled', b'id', b'type', b'start', b'finish', b'steps', b'cells', b'bonus'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, id=0, type=b'', start=0, finish=0, steps={}, cells={}, bonus={})
        defaults.update(kwargs)
        cls.__packStepConfigs(defaults)
        cls.__packCellConfigs(defaults)
        return super(BundleConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(**dict(enabled=False, id=0, type=b'', start=0, finish=0, steps={}, cells={}, bonus={}))

    @classmethod
    def __packStepConfigs(cls, data):
        data[b'steps'] = {stepNumber: makeTupleByDict(StepConfig, step) for stepNumber, step in viewitems(data[b'steps'])}
        return

    @classmethod
    def __packCellConfigs(cls, data):
        data[b'cells'] = {cellName: makeTupleByDict(CellConfig, cell) for cellName, cell in viewitems(data[b'cells'])}
        return


class StepConfig(namedtuple(b'_StepConfig', (b'number', b'price', b'fixedBonus'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(number=False, price={}, fixedBonus={})
        defaults.update(kwargs)
        return super(StepConfig, cls).__new__(cls, **defaults)


class CellConfig(namedtuple(b'_CellConfig', (b'name', b'template', b'coordinates', b'tags'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(name=b'', template=b'', coordinates={}, tags=[])
        defaults.update(kwargs)
        cls.__packCoordinatesConfig(defaults)
        return super(CellConfig, cls).__new__(cls, **defaults)

    @classmethod
    def __packCoordinatesConfig(cls, data):
        data[b'coordinates'] = makeTupleByDict(CoordinatesConfig, data[b'coordinates'])
        return


class CoordinatesConfig(namedtuple(b'_CoordinatesConfig', (b'start', b'end'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(start=(0, 0), end=(0, 0))
        defaults.update(kwargs)
        return super(CoordinatesConfig, cls).__new__(cls, **defaults)
