import ResMgr, nations, os
from constants import REGIONAL_REALMS
from items import _xml
from items import vehicles
from items.components import skills_constants, crew_skins_constants
from items.components import tankmen_components
import items.components.crew_skins_components as cc

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
        priceGroup = cc.PriceGroup()
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
            priceGroup.tags = frozenset(map(intern, tags))
            for tag in priceGroup.tags:
                cache.priceGroupTags.setdefault(tag, []).append(priceGroup)

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


def _readSkinItem(pricesCache, cache, xmlCtx, section, storage):
    skinID = _xml.readInt(xmlCtx, section, b'id', 1)
    if skinID in storage:
        _xml.raiseWrongXml(xmlCtx, b'id', b"duplicate id '%s'" % skinID)
    priceGroup = section.readString(b'priceGroup')
    tags = _readGroupTags((xmlCtx, b'tags'), section, b'tags')
    firstNameID = _xml.readStringOrEmpty(xmlCtx, section, b'firstName')
    lastNameID = _xml.readNonEmptyString(xmlCtx, section, b'lastName')
    description = _xml.readNonEmptyString(xmlCtx, section, b'description')
    iconID = _xml.readNonEmptyString(xmlCtx, section, b'icon')
    rarity = _xml.readInt(xmlCtx, section, b'rarity', 1)
    soundSetID = section.readString(b'soundSet', crew_skins_constants.NO_CREW_SKIN_SOUND_SET)
    historical = _xml.readInt(xmlCtx, section, b'historical') == 0
    realmsStr = section.readString(b'realms', b'')
    realms = realmsStr.split()
    unexpectedRealms = set(realms) - REGIONAL_REALMS
    if unexpectedRealms:
        _xml.raiseWrongXml(xmlCtx, b'realms', b"unknown realms '%s'" % unexpectedRealms)
    crewSkinItem = cc.CrewSkin(skinID, priceGroup, firstNameID, lastNameID, iconID, description, rarity, tags, historical, soundSetID, realms)
    if section.has_key(b'filters'):
        filterSection = _xml.getSubsection(xmlCtx, section, b'filters')
        if filterSection.has_key(b'nation'):
            nation = filterSection.readString(b'nation', b'')
            if nation and nation not in nations.NAMES:
                _xml.raiseWrongXml(xmlCtx, b'nation', b"unknown nation '%s'" % nation)
            crewSkinItem.nation = nation if nation else None
        if filterSection.has_key(b'sex'):
            sex = filterSection.readString(b'sex', b'')
            if sex not in crew_skins_constants.TANKMAN_SEX.AVAILABLE:
                _xml.raiseWrongXml(xmlCtx, b'sex', b"unknown tankman sex '%s'" % sex)
            crewSkinItem.sex = sex
    storage[skinID] = crewSkinItem
    groupsDict = cache.priceGroups
    itemToGroup = cache.itemToPriceGroup
    if crewSkinItem.priceGroup:
        if crewSkinItem.priceGroup not in cache.priceGroupNames:
            _xml.raiseWrongXml(xmlCtx, b'priceGroup', b'unknown price group %s for item %s' % (
             crewSkinItem.priceGroup, crewSkinItem.id))
        priceGroupId = cache.priceGroupNames[crewSkinItem.priceGroup]
        crewSkinItem.priceGroupTags = groupsDict[priceGroupId].tags
        itemToGroup[crewSkinItem.compactDescr] = groupsDict[priceGroupId].compactDescr
        itemNotInShop = section.readBool(b'notInShop', False)
        _copyPriceForItem(pricesCache, groupsDict[priceGroupId].compactDescr, crewSkinItem.compactDescr, itemNotInShop)
    else:
        _xml.raiseWrongXml(xmlCtx, b'priceGroup', b'no price for item %s' % crewSkinItem.id)
    return


def _readCrewSkinsCacheFromXMLSection(pricesCache, cache, xmlCtx, section, sectionName, storage):
    for i, (gname, gsection) in enumerate(section.items()):
        if gname != sectionName:
            continue
        _readSkinItem(pricesCache, cache, xmlCtx, gsection, storage)

    return


def readCrewSkinsCacheFromXML(pricesCache, cache, folder):
    pgFile = os.path.join(folder, crew_skins_constants.CREW_SKINS_PRICE_GROUPS_XML_FILE)
    _readPriceGroups(pricesCache, cache, (None, crew_skins_constants.CREW_SKINS_PRICE_GROUPS_XML_FILE), ResMgr.openSection(pgFile), b'priceGroup')
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, crew_skins_constants.CREW_SKINS_XML_FILE)
    _readCrewSkinsCacheFromXMLSection(pricesCache, cache, (None, crew_skins_constants.CREW_SKINS_XML_FILE), ResMgr.openSection(pgFile), b'crewSkin', cache.skins)
    ResMgr.purge(pgFile)
    return
