from extension_utils import ResMgr
from ExtensionsManager import makeExtensionPath
from constants import IS_CLIENT
from debug_utils import LOG_CURRENT_EXCEPTION
from wotdecorators import singleton
from new_year_common.items.readers.collectibles_readers import _readCollections
from new_year_common.items.components.ny_constants import ToySettings, YEARS, YEARS_INFO
from new_year_common.items.components.ny_constants import PREMIUM_TOY
_CONFIG_FILE = makeExtensionPath(b'new_year', b'scripts/item_defs/collectibles/collectibles.xml')

@singleton
class g_cache(object):

    def __init__(self):
        self.__cfg = {}
        return

    def __getattr__(self, collectionName):
        try:
            return self.__cfg[collectionName]
        except KeyError:
            raise AttributeError

        return

    def __getitem__(self, collectionName):
        try:
            return self.__cfg[collectionName]
        except KeyError:
            raise KeyError

        return

    def init(self, nofail=True):
        try:
            try:
                section = ResMgr.openSection(_CONFIG_FILE)
                self.__cfg = cfg = {k: CollectionDescriptor(**v) for k, v in _readCollections(section[b'collections']).iteritems()}
            except Exception:
                self.ffini()
                if nofail:
                    raise
                LOG_CURRENT_EXCEPTION()

        finally:
            ResMgr.purge(_CONFIG_FILE)

        return

    def ffini(self):
        self.__cfg.clear()
        return

    @property
    def currentNyCollection(self):
        return self[YEARS.getYearStrFromYearNum(YEARS_INFO.CURRENT_YEAR)]

    def __iter__(self):
        return (citem for coll in self.__cfg.itervalues() for citem in coll.itervalues())

    def __nonzero__(self):
        return bool(self.__cfg)


class CollectionDescriptor(object):
    __slots__ = (b'__cfg',)

    def __init__(self, **kwargs):
        cfg = self.__cfg = dict(kwargs)
        cfg[b'toys'] = {tid: ToyDescriptor(**d) for tid, d in kwargs.get(b'toys', {}).iteritems()}
        return

    def __int__(self):
        return -1

    def __getattr__(self, name):
        try:
            return self.__cfg[name]
        except KeyError:
            raise AttributeError

        return

    def __getitem__(self, item):
        try:
            return self.__cfg[item]
        except KeyError:
            raise KeyError

        return

    def __iter__(self):
        return self.toys.itervalues()


@singleton
class EmptyCollection(CollectionDescriptor):
    __slots__ = ()

    def __init__(self):
        CollectionDescriptor.__init__(self, **{b'toys': {}})
        return


class ToyDescriptor(object):
    __slots__ = (b'__cfg',)

    def __init__(self, **kwargs):
        self.__cfg = {k: v for k, v in kwargs.iteritems() if k in (b'id', b'rank', b'type', b'setting', b'collection', b'icon', b'price') or IS_CLIENT}
        return

    def __getattr__(self, name):
        cfg = self.__cfg
        if name in cfg:
            return cfg[name]
        raise AttributeError((b"'{}' object has no attribute '{}'").format(self.__class__, name))
        return

    def __getitem__(self, item):
        cfg = self.__cfg
        if item in cfg:
            return cfg[item]
        raise KeyError((b"'{}' object has no attribute '{}'").format(self.__class__, item))
        return

    def __int__(self):
        return -1

    @property
    def price(self):
        if self.hasPrice():
            return self.__cfg[b'price']
        else:
            return

    def isMegaToy(self):
        return self.__cfg[b'setting'] in ToySettings.MEGA

    def isPremiumToy(self):
        return self.__cfg[b'rank'] in PREMIUM_TOY

    def hasName(self):
        return b'name' in self.__cfg

    def hasPrefab(self):
        return b'prefab' in self.__cfg

    def hasPrice(self):
        return b'price' in self.__cfg


def init(verbose=False, nofail=True):
    if not g_cache:
        g_cache.init(nofail)
    return
