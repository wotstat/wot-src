from __future__ import absolute_import
import ResMgr, nations, os
from past.builtins import intern
from items import _xml
from items import vehicles
from items.components import crew_books_constants
from items.components import tankmen_components
import items.components.crew_books_components as cb

def _readPriceForItem(pricesDest, xmlCtx, section, compactDescr):
    if pricesDest is not None:
        pricesDest[b'itemPrices'][compactDescr] = _xml.readPrice(xmlCtx, section, b'price')
        if section.readBool(b'notInShop', False):
            pricesDest[b'notInShopItems'].add(compactDescr)
    return


def _copyPriceForItem(pricesDest, sourceCompactDescr, destCompactDescr, itemNotInShop):
    if pricesDest is not None:
        pricesDest[b'itemPrices'][destCompactDescr] = pricesDest[b'itemPrices'].getPrices(sourceCompactDescr)
        if itemNotInShop or sourceCompactDescr in pricesDest[b'notInShopItems']:
            pricesDest[b'notInShopItems'].add(destCompactDescr)
    return


def _readPriceGroups(pricesCache, cache, xmlCtx, section, sectionName):
    for tag, iSection in section.items():
        if tag != sectionName:
            continue
        priceGroup = cb.PriceGroup()
        priceGroup.id = _xml.readInt(xmlCtx, iSection, b'id', 1)
        iCtx = (xmlCtx, b'id %s' % priceGroup.id)
        if priceGroup.id in cache.priceGroups:
            _xml.raiseWrongXml(iCtx, b'id', b'duplicate price group id')
        priceGroup.name = intern(_xml.readString(iCtx, iSection, b'name'))
        if priceGroup.name in cache.priceGroupNames:
            _xml.raiseWrongXml(iCtx, b'id', b'duplicate price group name "%s"' % priceGroup.name)
        priceGroup.notInShop = iSection.readBool(b'notInShop', False)
        _readPriceForItem(pricesCache, iCtx, iSection, priceGroup.compactDescr)
        if iSection.has_key(b'tags'):
            tags = iSection.readString(b'tags').split()
            priceGroup.tags = frozenset(intern(tag) for tag in tags)
            for priceTag in priceGroup.tags:
                cache.priceGroupTags.setdefault(priceTag, []).append(priceGroup)

        cache.priceGroupNames[priceGroup.name] = priceGroup.id
        cache.priceGroups[priceGroup.id] = priceGroup

    return


def _readGroupTags(xmlCtx, section, subsectionName):
    source = _xml.readStringOrNone(xmlCtx, section, subsectionName)
    if source is not None:
        tags = source.split()
        restrictions = []
        for tag in tags:
            if not (tag in tankmen_components.GROUP_TAG.RANGE or vehicles.g_list.isVehicleExisting(tag)):
                _xml.raiseWrongXml(xmlCtx, subsectionName, (b'unknown tag "{}"').format(tag))
            if tag in tankmen_components.GROUP_TAG.RESTRICTIONS:
                restrictions.append(tag)

        if restrictions and tankmen_components.GROUP_TAG.PASSPORT_REPLACEMENT_FORBIDDEN not in restrictions:
            _xml.raiseWrongXml(xmlCtx, subsectionName, (b'Group contains tags of restrictions {}, so tag "{}" is mandatory').format(restrictions, tankmen_components.GROUP_TAG.PASSPORT_REPLACEMENT_FORBIDDEN))
    else:
        tags = []
    return frozenset(tags)


def _readBookItem(pricesCache, cache, xmlCtx, section, storage):
    bookID = _xml.readInt(xmlCtx, section, b'id', 1)
    priceGroup = section.readString(b'priceGroup')
    tags = _readGroupTags((xmlCtx, b'tags'), section, b'tags')
    nameID = _xml.readStringOrEmpty(xmlCtx, section, b'name')
    descriptionID = _xml.readStringOrEmpty(xmlCtx, section, b'description')
    iconID = _xml.readNonEmptyString(xmlCtx, section, b'icon')
    type = _xml.readNonEmptyString(xmlCtx, section, b'type')
    if type not in crew_books_constants.CREW_BOOK_RARITY.ALL_TYPES:
        _xml.raiseWrongXml(xmlCtx, b'type', b"unknown crew book rarity type '%s'" % type)
    crewBookItem = cb.CrewBook(bookID, priceGroup, nameID, descriptionID, iconID, type, tags)
    if section.has_key(b'filters'):
        filterSection = _xml.getSubsection(xmlCtx, section, b'filters')
        if filterSection.has_key(b'nation'):
            nation = filterSection.readString(b'nation', b'')
            if nation and nation not in nations.NAMES:
                _xml.raiseWrongXml(xmlCtx, b'nation', b"unknown nation '%s'" % nation)
            crewBookItem.nation = nation if nation else None
    if not crewBookItem.nation and type not in crew_books_constants.CREW_BOOK_RARITY.NO_NATION_TYPES:
        _xml.raiseWrongXml(xmlCtx, b'nation', b"crew book with rarity type '%s' should have nation" % type)
    storage[bookID] = crewBookItem
    groupsDict = cache.priceGroups
    itemToGroup = cache.itemToPriceGroup
    if crewBookItem.priceGroup:
        if crewBookItem.priceGroup not in cache.priceGroupNames:
            _xml.raiseWrongXml(xmlCtx, b'priceGroup', b'unknown price group %s for item %s' % (
             crewBookItem.priceGroup, crewBookItem.id))
        priceGroupId = cache.priceGroupNames[crewBookItem.priceGroup]
        crewBookItem.priceGroupTags = groupsDict[priceGroupId].tags
        itemToGroup[crewBookItem.compactDescr] = groupsDict[priceGroupId].compactDescr
        itemNotInShop = section.readBool(b'notInShop', False)
        _copyPriceForItem(pricesCache, groupsDict[priceGroupId].compactDescr, crewBookItem.compactDescr, itemNotInShop)
    else:
        _xml.raiseWrongXml(xmlCtx, b'priceGroup', b'no price for item %s' % crewBookItem.id)
    return


def _readBookTypeItem(pricesCache, cache, xmlCtx, section, storage):
    type = _xml.readStringOrEmpty(xmlCtx, section, b'type')
    if type not in crew_books_constants.CREW_BOOK_RARITY.ALL_TYPES:
        _xml.raiseWrongXml(xmlCtx, b'type', b"unknown crew book rarity type '%s'" % type)
    exp = _xml.readInt(xmlCtx, section, b'exp', 0)
    storage[type] = exp
    return


def _readCrewBooksCacheFromXMLSection(pricesCache, cache, xmlCtx, section, sectionName, storage):
    for gname, gsection in section.items():
        if gname != sectionName:
            continue
        reader = __xmlReaders[sectionName]
        reader(pricesCache, cache, xmlCtx, gsection, storage)

    return


def readCrewBooksCacheFromXML(pricesCache, cache, folder):
    pgFile = os.path.join(folder, crew_books_constants.CREW_BOOKS_PRICE_GROUPS_XML_FILE)
    _readPriceGroups(pricesCache, cache, (None, crew_books_constants.CREW_BOOKS_PRICE_GROUPS_XML_FILE), ResMgr.openSection(pgFile), b'priceGroup')
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, crew_books_constants.CREW_BOOKS_XML_FILE)
    _readCrewBooksCacheFromXMLSection(pricesCache, cache, (None, crew_books_constants.CREW_BOOKS_XML_FILE), ResMgr.openSection(pgFile), b'crewBook', cache.books)
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, crew_books_constants.CREW_BOOK_TYPES_XML_FILE)
    _readCrewBooksCacheFromXMLSection(pricesCache, cache, (None, crew_books_constants.CREW_BOOK_TYPES_XML_FILE), ResMgr.openSection(pgFile), b'crewBookType', cache.rarityGroups)
    ResMgr.purge(pgFile)
    return


__xmlReaders = {b'crewBook': _readBookItem, 
   b'crewBookType': _readBookTypeItem}
