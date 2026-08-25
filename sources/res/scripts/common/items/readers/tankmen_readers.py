from __future__ import absolute_import
from past.builtins import intern
import ResMgr
from constants import IS_CLIENT, IS_WEB, IS_BOT
from items import _xml
from items.components import component_constants, skills_constants
from items.components import shared_components
from items.components import tankmen_components

def _parseName(xmlCtx, section):
    return shared_components.I18nString(_xml.readNonEmptyString(xmlCtx, section, component_constants.EMPTY_STRING)).value


def _parseIcon(xmlCtx, section):
    return _xml.readNonEmptyString(xmlCtx, section, component_constants.EMPTY_STRING)


def _readIDs(xmlCtx, subsections, accumulator, parser=None):
    res = set()
    for sname, subsection in subsections:
        try:
            contentID = int(sname[1:])
        except ValueError:
            contentID = -1

        if sname[0] != b'_' or not 0 <= contentID <= 65535:
            _xml.raiseWrongSection(xmlCtx, sname)
        if contentID in accumulator:
            _xml.raiseWrongXml(xmlCtx, sname, b'ID is not unique')
        if parser is not None:
            accumulator[contentID] = parser((xmlCtx, sname), subsection)
        else:
            accumulator[contentID] = component_constants.EMPTY_STRING
        res.add(contentID)

    if not res:
        _xml.raiseWrongXml(xmlCtx, b'', b'is empty')
    return res


def _readRanks(xmlCtx, subsections):
    ranks = tankmen_components.RanksSet()
    for sname, subsection in subsections:
        if ranks.getRankByName(sname) is not None:
            _xml.raiseWrongXml(xmlCtx, sname, b'is not unique')
        sname = intern(sname)
        ctx = (xmlCtx, sname)
        if IS_CLIENT or IS_WEB:
            i18n = shared_components.I18nString(_xml.readNonEmptyString(ctx, subsection, b'userString'))
            icon = _parseIcon((ctx, b'icon'), _xml.getSubsection(ctx, subsection, b'icon'))
            rank = tankmen_components.Rank(sname, i18n=i18n, icon=icon)
        else:
            rank = tankmen_components.Rank(sname)
        ranks.add(rank)

    return ranks


def _readRoleRanks(xmlCtx, section, ranks):
    roleRanks = tankmen_components.RoleRanks()
    for roleName in skills_constants.ROLES:
        rankIDs = []
        for rankName in _xml.readNonEmptyString(xmlCtx, section, roleName).split():
            rankIDs.append(ranks.getIDByName(rankName))

        roleRanks.setRanksIDs(roleName, tuple(rankIDs))

    return roleRanks


def _readGroupTags(xmlCtx, section, subsectionName):
    source = _xml.readStringOrNone(xmlCtx, section, subsectionName)
    if source is not None:
        from items import vehicles
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


def _readGroupRoles(xmlCtx, section, subsectionName):
    source = _xml.readStringOrNone(xmlCtx, section, subsectionName)
    if source is not None:
        tags = source.split()
        roles = []
        for tag in tags:
            if tag not in skills_constants.ROLES:
                _xml.raiseWrongXml(xmlCtx, subsectionName, (b'unknown tag "{}"').format(tag))
            roles.append(intern(tag))

    else:
        tags = skills_constants.ROLES
    return frozenset(tags)


def _readTankmenGroup(xmlCtx, groupName, subsection, firstNames, lastNames, icons):
    if IS_CLIENT or IS_WEB or IS_BOT:
        parseName = _parseName
        parseIcon = _parseIcon
    else:
        parseName = parseIcon = None
    return tankmen_components.NationGroup(_xml.readNonNegativeInt(xmlCtx, subsection, b'groupID'), groupName, _xml.readNonEmptyString(xmlCtx, subsection, b'sex') == b'female', subsection.readBool(b'notInShop', False), _readIDs((
     xmlCtx, b'firstNames'), _xml.getChildren(xmlCtx, subsection, b'firstNames'), firstNames, parseName), _readIDs((
     xmlCtx, b'lastNames'), _xml.getChildren(xmlCtx, subsection, b'lastNames'), lastNames, parseName), _readIDs((
     xmlCtx, b'icons'), _xml.getChildren(xmlCtx, subsection, b'icons'), icons, parseIcon), _xml.readNonNegativeFloat(xmlCtx, subsection, b'weight'), _readGroupTags((xmlCtx, b'tags'), subsection, b'tags'), _readGroupRoles((xmlCtx, b'roles'), subsection, b'roles'))


def _readNationConfigSection(xmlCtx, section):
    config = {}
    firstNames = {}
    lastNames = {}
    icons = {}
    for kindName in component_constants.TANKMEN_GROUPS:
        groups = []
        totalWeight = 0.0
        groupIDs = set()
        for sname, subsection in _xml.getChildren(xmlCtx, section, kindName):
            ctx = (xmlCtx, kindName + b'/' + sname)
            group = _readTankmenGroup(ctx, sname, subsection, firstNames, lastNames, icons)
            groupID = group.groupID
            if groupID in groupIDs:
                _xml.raiseWrongXml(xmlCtx, sname, b'duplicate groupID %d' % groupID)
            groupIDs.add(groupID)
            totalWeight += group.weight
            groups.append(group)

        totalWeight = max(0.001, totalWeight)
        for group in groups:
            group.weight /= totalWeight

        config[kindName] = {group.groupID: group for group in groups}

    ranks = _readRanks((xmlCtx, b'ranks'), _xml.getChildren(xmlCtx, section, b'ranks'))
    config[b'roleRanks'] = _readRoleRanks((
     xmlCtx, b'roleRanks'), _xml.getSubsection(xmlCtx, section, b'roleRanks'), ranks)
    if IS_CLIENT or IS_WEB or IS_BOT:
        config[b'firstNames'] = firstNames
        config[b'lastNames'] = lastNames
        config[b'icons'] = icons
        config[b'ranks'] = ranks
    else:
        config[b'firstNames'] = frozenset(firstNames)
        config[b'lastNames'] = frozenset(lastNames)
        config[b'icons'] = frozenset(icons)
    return tankmen_components.NationConfig(xmlCtx[1], **config)


def readNationConfig(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    config = _readNationConfigSection((None, xmlPath), section)
    ResMgr.purge(xmlPath, True)
    return config


def readLoreConfig(xmlPath):
    xmlCtx = (
     None, xmlPath)
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    config = tankmen_components.LoreComponent()
    for partName, part in _xml.getChildren(xmlCtx, section, tankmen_components.LoreComponent.SECTION):
        config.addDescrForGroup(partName, part.asString)
        if part.has_key(tankmen_components.LoreComponent.NATION_SECTION):
            for itemName, item in _xml.getChildren(xmlCtx, part, tankmen_components.LoreComponent.NATION_SECTION):
                config.addNationDescrForGroup(partName, itemName, item.asString)

    return config
