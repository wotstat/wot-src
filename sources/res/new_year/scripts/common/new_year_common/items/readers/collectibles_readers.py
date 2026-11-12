import BigWorld
from new_year_common.items.components.ny_constants import MIN_TOY_RANK, YEARS_INFO
from new_year_common.ny_exception import NYSoftException
TOY_PRICE_CURRENCY = (b'gold',)

def _readCollections(section):
    cfg = {}
    for name, subsection in section.items():
        cfg[name] = _readCollection(subsection)

    return cfg


def _readCollection(section):
    cfg = {(intern(b'isEnabled')): False, (intern(b'toys')): {}}
    domains = section.readString(b'domains', b'')
    if not domains:
        return cfg
    domainList = domains.split()
    if BigWorld.component not in domainList:
        return cfg
    isEnabled = cfg[b'isEnabled'] = section.readBool(b'isEnabled', False)
    if not isEnabled:
        return cfg
    cfg[b'toys'] = _readToys(section[b'toys'], section.name)
    return cfg


def _readToys(section, collectionName=None):
    cfg = {}
    for subsection in section.values():
        toy = _readToy(subsection, collectionName)
        cfg[toy[b'id']] = toy

    return cfg


def _readToy(section, collectionName=None):
    cfg = {(intern(b'collection')): collectionName} if collectionName else {}
    toyData = {intern(name): section.readInt(name) if name in (b'id', b'rank') else intern(section.readString(name)) for name, subsection in section.items()}
    if section.has_key(b'price'):
        price = _readToyPrice(section[b'price'])
        toyData.update(price)
    if collectionName and collectionName != b'defaultToys':
        if not MIN_TOY_RANK <= toyData[b'rank'] <= YEARS_INFO.getMaxToyRankByYear(collectionName):
            raise NYSoftException((b'Invalid toy rank, toy collection:{}, toy id: {}').format(collectionName, toyData[b'id']))
        if toyData[b'setting'] not in YEARS_INFO.getCollectionTypesByYear(collectionName):
            raise NYSoftException((b'Invalid setting, toy collection:{}, toy id: {}').format(collectionName, toyData[b'id']))
    cfg.update(toyData)
    return cfg


def _readToyPrice(section):
    result = {}
    for name in section.keys():
        if name not in TOY_PRICE_CURRENCY:
            raise NYSoftException((b'Invalid toy currency: {}').format(name))
        if name in result:
            raise NYSoftException((b'Duplicated currency: {}').format(name))
        value = section.readInt(name)
        if value <= 0:
            raise NYSoftException((b'Invalid price value: {}').format(value))
        result[intern(name)] = value

    return {(intern(b'price')): result}
