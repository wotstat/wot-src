from __future__ import absolute_import
import operator, typing
from collections import defaultdict, namedtuple
from future.utils import listvalues, viewitems, viewvalues
from past.builtins import xrange
import ResMgr, nations
from constants import IS_DEVELOPMENT
from debug_utils import LOG_ERROR, LOG_DEBUG
from gui import GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.techtree.nodes import BaseNode
from gui.Scaleform.daapi.view.lobby.techtree.settings import NATION_TREE_REL_FILE_PATH
from gui.Scaleform.daapi.view.lobby.techtree.settings import NATION_TREE_REL_PREMIUM_FILE_PATH
from gui.Scaleform.daapi.view.lobby.techtree.settings import NODE_ORDER_PREFIX_COMMON, NODE_ORDER_PREFIX_PREMIUM
from gui.Scaleform.daapi.view.lobby.techtree.settings import TREE_SHARED_REL_FILE_PATH, UnlockStats
from gui.Scaleform.daapi.view.lobby.techtree.settings import UNKNOWN_VEHICLE_LEVEL
from gui.Scaleform.daapi.view.lobby.techtree.settings import UnlockProps, DEFAULT_UNLOCK_PROPS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.lobby.exchange.exchange_rates_helper import calculateMaxPossibleFreeXp
from gui.shared.gui_items import GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from items import _xml, vehicles, getTypeOfCompactDescr
from skeletons.gui.shared import IItemsCache
from skeletons.gui.techtree_events import ITechTreeEventsListener
from soft_exception import SoftException

class _ConfigError(SoftException):

    def __init__(self, ctx, msg):
        super(_ConfigError, self).__init__()
        self.msg = msg
        self.ctx = ctx
        return

    def __str__(self):
        return (b'Config error in {0:>s}. {1:>s}').format(self.ctx[1], self.msg)


def _makeLines():
    return {b'outLiteral': None, b'outPin': None, b'inPins': []}


DISPLAY_SETTINGS = {b'hasRoot': b'readBool', 
   b'isLevelDisplayed': b'readBool', 
   b'nodeRendererName': b'readString', 
   b'firstLevelToHighlight': b'readInt'}
_VEHICLE = GUI_ITEM_TYPE.VEHICLE
_VEHICLE_TYPE_NAME = GUI_ITEM_TYPE_NAMES[_VEHICLE]
_AnnouncementInfo = namedtuple(b'_AnnouncementInfo', (
 b'userString',
 b'tooltip',
 b'tags',
 b'level',
 b'icon',
 b'isElite'))

class _TechTreeDataProvider(object):
    __slots__ = (b'__loaded', b'__availableNations', b'__override', b'__displayInfo', b'__displaySettings', b'__gridSettings', b'__premiumGridSettings', b'__topLevels', b'__topItems', b'__nextLevels', b'__unlockPrices', b'__announcements', b'__announcementCDToName', b'__nextAnnouncements', b'__nodes', b'__nextTypeIDs')
    itemsCache = dependency.descriptor(IItemsCache)
    techTreeEventsListener = dependency.descriptor(ITechTreeEventsListener)

    def __init__(self):
        super(_TechTreeDataProvider, self).__init__()
        self.__loaded = False
        self.__availableNations = None
        self.__override = b''
        self._clear()
        return

    def load(self, isReload=False):
        if self.__loaded and not isReload:
            return False
        LOG_DEBUG(b'Tech tree data is being loaded')
        self._clear()
        try:
            try:
                shared = self.__readShared(clearCache=isReload)
                for nation in self.__availableNations:
                    info = self.__readNation(shared, nation, clearCache=isReload)
                    self.__displayInfo[nations.INDICES[nation]] = info

            except _ConfigError as error:
                LOG_ERROR(error)

        finally:
            self.__makeAbsoluteCoordinates()
            self.__loaded = True

        _xml.clearCaches()
        return True

    def setOverride(self, override=b''):
        if self.__override != override:
            self.__override = override
            self.__loaded = False
        return

    def getDisplaySettings(self, nationID):
        try:
            result = self.__displaySettings[nationID]
        except KeyError:
            result = {}

        return result

    def getGridSettings(self, nationID):
        result = self.__gridSettings[nationID]
        if result is not None:
            return result
        else:
            return {}

    def getPremiumGridSettings(self, nationID):
        result = self.__premiumGridSettings[nationID]
        if result is not None:
            return result
        else:
            return {}

    def getNationTreeIterator(self, nationID):
        if nationID >= len(self.__nodes):
            LOG_ERROR(b'Nation ID is out of range', nationID)
            return
        else:
            nodes = self.__nodes[nationID]
            if nodes is None:
                LOG_ERROR(b'Nodes is not found', nationID)
                return
            displayInfo = self.__displayInfo[nationID]
            if displayInfo is None:
                LOG_ERROR(b'Display info is not found', nationID)
                return
            for node in sorted(viewvalues(nodes), key=(lambda item: item.order)):
                yield (
                 node, displayInfo[node.nodeCD].copy())

            return

    def getTopLevel(self, vTypeCD):
        return self.__topLevels[vTypeCD]

    def getNextLevel(self, vTypeCD):
        return self.__nextLevels[vTypeCD].keys()

    def isNext2Unlock(self, vTypeCD, unlocked=None, xps=None, freeXP=0, level=UNKNOWN_VEHICLE_LEVEL):
        unlocked = unlocked or set()
        topLevel = self.getTopLevel(vTypeCD)
        available = False
        topIDs = set()
        compare = []
        result = DEFAULT_UNLOCK_PROPS
        for parentCD in topLevel:
            nextLevel = self.__nextLevels[parentCD]
            idx, xpCost, required = nextLevel[vTypeCD]
            discount, newCost = self.getBlueprintDiscountData(vTypeCD, level, xpCost)
            if required.issubset(unlocked) and parentCD in unlocked:
                topIDs.add(parentCD)
                compare.append(UnlockProps(parentCD, idx, newCost, topIDs, discount, xpCost))
                available = True
            elif not result.xpCost or result.xpCost > xpCost:
                result = UnlockProps(parentCD, idx, newCost, set(), discount, xpCost)

        if available:
            result = self._findNext2Unlock(compare, xps=xps, freeXP=freeXP)
        return (available, result)

    def getNext2UnlockByItems(self, itemCDs, unlocked=None, xps=None, freeXP=0):
        unlocked = unlocked or set()
        filtered = [item for item in itemCDs if item in self.__topItems]
        if not filtered or not unlocked:
            return {}
        available = defaultdict(list)
        parentCDs = {item for item in itemCDs if getTypeOfCompactDescr(item) == _VEHICLE}
        for item in filtered:
            if item in unlocked:
                parentCDs |= self.__topItems[item]

        for parentCD in parentCDs:
            if parentCD not in unlocked:
                continue
            nextLevel = self.__nextLevels[parentCD]
            topIDs = set()
            for childCD, (idx, xpCost, required) in viewitems(nextLevel):
                if required.issubset(unlocked):
                    topIDs.add(parentCD)
                    available[childCD].append(UnlockProps(parentCD, idx, xpCost, topIDs, 0, xpCost))

        result = {}
        for childCD, compare in viewitems(available):
            result[childCD] = self._findNext2Unlock(compare, xps=xps, freeXP=freeXP)

        return result

    def getAvailableNations(self):
        if self.__availableNations is None:
            section = ResMgr.openSection(TREE_SHARED_REL_FILE_PATH)
            if section is None:
                _xml.raiseWrongXml(None, TREE_SHARED_REL_FILE_PATH, b'can not open or read')
            xmlCtx = (
             None, TREE_SHARED_REL_FILE_PATH)
            self.__availableNations = self.__readAvailableNations(xmlCtx, section)
        return self.__availableNations[:]

    def getNationsMenuDataProvider(self):
        return [self._getNationsMenuItem(nation) for nation in self.getAvailableNations()]

    def _getNationsMenuItem(self, nation):
        nationID = nations.INDICES[nation]
        hasDiscount = nationID in self.techTreeEventsListener.getNations(unviewed=True)
        isTooltipSpecial = hasDiscount or nationID in self.techTreeEventsListener.getNations()
        return {b'tooltip': (TOOLTIPS_CONSTANTS.TECHTREE_NATION_DISCOUNT if isTooltipSpecial else nation), 
           b'isTooltipSpecial': isTooltipSpecial, 
           b'hasDiscount': hasDiscount, 
           b'label': nation}

    def getAvailableNationsIndices(self):
        return [nations.INDICES[nation] for nation in self.getAvailableNations()]

    def getUnlockPrices(self, compactDescr):
        return self.__unlockPrices[compactDescr]

    def getAllPossibleItems2Unlock(self, vehicle, unlocked):
        items = {}
        for unlockIdx, xpCost, nodeCD, required in vehicle.getUnlocksDescrs():
            if required.issubset(unlocked) and nodeCD not in unlocked:
                level = self.itemsCache.items.getItemByCD(nodeCD).level
                discount, newCost = self.getBlueprintDiscountData(nodeCD, level, xpCost)
                items[nodeCD] = UnlockProps(parentID=vehicle.intCD, unlockIdx=unlockIdx, xpCost=newCost, required=required, discount=discount, xpFullCost=xpCost)

        return items

    def getUnlockedVehicleItems(self, vehicle, unlocked):
        items = {}
        for unlockIdx, xpCost, nodeCD, required in vehicle.getUnlocksDescrs():
            if required.issubset(unlocked) and nodeCD in unlocked:
                discountData = self.getBlueprintDiscountData(vehicle.intCD, vehicle.level, xpCost)
                items[nodeCD] = UnlockProps(vehicle.intCD, unlockIdx, discountData[1], required, discountData[0], xpCost)

        return items

    def getAllVehiclePossibleXP(self, nodeCD, unlockStats):
        criteria = REQ_CRITERIA.VEHICLE.FULLY_ELITE | ~REQ_CRITERIA.IN_CD_LIST([nodeCD])
        eliteVehicles = self.itemsCache.items.getVehicles(criteria)
        dirtyResult = sum(map(operator.attrgetter(b'xp'), eliteVehicles.values()))
        result = calculateMaxPossibleFreeXp(xpFromVehicles=dirtyResult, itemsCache=self.itemsCache)
        result += unlockStats.getVehTotalXP(nodeCD)
        return result

    def isVehicleAvailableToUnlock(self, nodeCD, vehicleLevel=UNKNOWN_VEHICLE_LEVEL):
        unlocks = self.itemsCache.items.stats.unlocks
        xps = self.itemsCache.items.stats.vehiclesXPs
        freeXP = self.itemsCache.items.stats.actualFreeXP
        unlockProps = g_techTreeDP.getUnlockProps(nodeCD, vehicleLevel)
        parentID = unlockProps.parentID
        allPossibleXp = self.getAllVehiclePossibleXP(parentID, UnlockStats(unlocks, xps, freeXP))
        isNextToUnlock, props = self.isNext2Unlock(nodeCD, unlocked=set(unlocks), xps=xps, freeXP=freeXP, level=vehicleLevel)
        return (isNextToUnlock, allPossibleXp >= props.xpCost)

    def getUnlockProps(self, vehicleCD, vehicleLevel=UNKNOWN_VEHICLE_LEVEL):
        _, unlockProps = self.isNext2Unlock(vehicleCD, unlocked=self.itemsCache.items.stats.unlocks, xps=self.itemsCache.items.stats.vehiclesXPs, freeXP=self.itemsCache.items.stats.actualFreeXP, level=vehicleLevel)
        return unlockProps

    def getOldAndNewCost(self, vehicleCD, vehicleLevel):
        self.load()
        unlockProps = self.getUnlockProps(vehicleCD, vehicleLevel)
        if unlockProps is not None:
            return (unlockProps.xpCost, unlockProps.discount, unlockProps.xpFullCost)
        else:
            return (0, 0, 0)

    def getBlueprintDiscountData(self, vehicleCD, level, xpCost, blueprintCount=0):
        blueprints = self.itemsCache.items.blueprints
        discount = blueprints.getBlueprintDiscount(vehicleCD, level, blueprintCount)
        newCost = blueprints.calculateCost(xpCost, discount)
        return (discount, newCost)

    def getAnnouncementByName(self, name):
        if name in self.__announcements:
            return self.__announcements[name]
        else:
            return

    def getAnnouncementByCD(self, intCD):
        if intCD in self.__announcementCDToName:
            return self.getAnnouncementByName(self.__announcementCDToName[intCD])
        else:
            return

    def getNextAnnouncements(self, intCD):
        if intCD not in self.__nextAnnouncements:
            return
        for nodeCD in self.__nextAnnouncements[intCD]:
            yield nodeCD

        return

    def isActionEndNode(self, node):
        return self.__isBoundActionNode(node, self.getNextLevel(node.getNodeCD()))

    def isActionStartNode(self, node):
        return self.__isBoundActionNode(node, self.getTopLevel(node.getNodeCD()))

    def _clear(self):
        self.__displayInfo = [
         None] * len(nations.NAMES)
        self.__nextTypeIDs = [
         0] * len(nations.NAMES)
        self.__nodes = [
         None] * len(nations.NAMES)
        self.__displaySettings = {}
        self.__gridSettings = [
         None] * len(nations.NAMES)
        self.__premiumGridSettings = [None] * len(nations.NAMES)
        self.__topLevels = defaultdict(set)
        self.__topItems = defaultdict(set)
        self.__nextLevels = defaultdict(dict)
        self.__unlockPrices = defaultdict(dict)
        self.__announcements = {}
        self.__announcementCDToName = {}
        self.__nextAnnouncements = defaultdict(list)
        return

    def _findNext2Unlock(self, compare, xps=None, freeXP=0):
        xpGetter = xps.get

        def makeItem(item):
            xp = xpGetter(item.parentID, 0)
            return (item, xp, item.xpCost - xp)

        def getMinFreeXPSpent(props):
            _, _, minDelta = min(props, key=(lambda item: item[2]))
            filtered = (prop for prop in props if prop[2] == minDelta)
            recommended, _, _ = min(filtered, key=(lambda item: item[1]))
            return recommended

        mapping = [makeItem(unlockProps) for unlockProps in compare]
        filtered = []
        recommended = None
        if xps is not None:
            filtered = [item for item in mapping if item[0].xpCost <= item[1] + freeXP]
        if filtered:
            recommended = getMinFreeXPSpent(filtered)
        if recommended is None:
            if filtered:
                mapping = filtered
            recommended = getMinFreeXPSpent(mapping)
        return recommended

    def __readShared(self, clearCache=False):
        if clearCache:
            ResMgr.purge(TREE_SHARED_REL_FILE_PATH)
        shared = {b'settings': {}, b'grids': {}, b'default': {}, b'lines': {}}
        section = ResMgr.openSection(TREE_SHARED_REL_FILE_PATH)
        if section is None:
            _xml.raiseWrongXml(None, TREE_SHARED_REL_FILE_PATH, b'can not open or read')
        xmlCtx = (
         None, TREE_SHARED_REL_FILE_PATH)
        precessed = _xml.getChildren(xmlCtx, section, b'settings-set')
        for name, settingsSec in precessed:
            settingsName = settingsSec.asString
            xPath = (b'{0:>s}/{1:>s}/{2:>s}').format(TREE_SHARED_REL_FILE_PATH, name, settingsName)
            xmlCtx = (
             None, xPath)
            settings = {}
            for _, settingSec in settingsSec.items():
                name = _xml.readString(xmlCtx, settingSec, b'name')
                if name not in DISPLAY_SETTINGS:
                    LOG_ERROR(b'Setting is invalid', name)
                    continue
                reader = DISPLAY_SETTINGS[name]
                value = getattr(_xml, reader)(xmlCtx, settingSec, b'value')
                settings[name] = value

            for n in DISPLAY_SETTINGS:
                if n not in settings:
                    raise _ConfigError(xmlCtx, b'Setting not found')

            shared[b'settings'][settingsName] = settings

        if self.__availableNations is None:
            self.__availableNations = self.__readAvailableNations((
             None, TREE_SHARED_REL_FILE_PATH), section)
        self.__readAnnouncements((
         None, TREE_SHARED_REL_FILE_PATH), section)
        self.__readSharedMetrics(shared, xmlCtx, section)
        if self.__override:
            subSec = section[(b'overrides/{0:>s}').format(self.__override)]
            if subSec:
                xmlCtx = (
                 None,
                 (b'{0:>s}/overrides/{1:>s}').format(TREE_SHARED_REL_FILE_PATH, b'', self.__override))
                self.__readSharedMetrics(shared, xmlCtx, subSec)
        self.__readDefaultLine(shared, xmlCtx, section)
        return shared

    def __readSharedMetrics(self, shared, xmlCtx, section):
        precessed = _xml.getChildren(xmlCtx, section, b'grids')
        for name, gridSection in precessed:
            gridName = gridSection.asString
            xPath = (b'{0:>s}/{1:>s}/{2:>s}').format(TREE_SHARED_REL_FILE_PATH, name, gridName)
            gridCtx = (
             None, xPath)
            subSec = _xml.getSubsection(xmlCtx, gridSection, b'root')
            xmlCtx = (None, (b'{0:>s}/root').format(xPath))
            rootPos = {b'start': (_xml.readVector2(xmlCtx, subSec, b'start').tuple()), 
               b'step': (_xml.readInt(xmlCtx, subSec, b'step'))}
            subSec = _xml.getSubsection(gridCtx, gridSection, b'vertical')
            xmlCtx = (None, (b'{0:>s}/vertical').format(xPath))
            vertical = (
             _xml.readInt(xmlCtx, subSec, b'start'),
             _xml.readInt(xmlCtx, subSec, b'step'))
            subSec = _xml.getSubsection(gridCtx, gridSection, b'horizontal')
            xmlCtx = (None, (b'{0:>s}/horizontal').format(xPath))
            horizontal = (
             _xml.readInt(xmlCtx, subSec, b'start'),
             _xml.readInt(xmlCtx, subSec, b'step'))
            shared[b'grids'][gridName] = {b'root': rootPos, 
               b'vertical': vertical, 
               b'horizontal': horizontal}

        precessed = _xml.getChildren(xmlCtx, section, b'lines')
        lines = shared[b'lines']
        for name, sub in precessed:
            xPath = (b'{0:>s}/{1:>s}').format(TREE_SHARED_REL_FILE_PATH, name)
            xmlCtx = (None, xPath)
            pinsSec = _xml.getChildren(xmlCtx, sub, b'inPin')
            inPins = dict((pName, pSec.asVector2.tuple()) for pName, pSec in pinsSec)
            pinsSec = _xml.getChildren(xmlCtx, sub, b'outPin')
            outPins = dict((pName, pSec.asVector2.tuple()) for pName, pSec in pinsSec)
            pinsSec = _xml.getChildren(xmlCtx, sub, b'viaPin')
            viaPins = defaultdict(dict)
            for outPin, setSec in pinsSec:
                for inPin, pSec in setSec.items():
                    viaPins[outPin][inPin] = [section[1].asVector2.tuple() for section in pSec.items()]

            defSec = sub[b'default']
            default = {}
            if defSec is not None:
                xmlCtx = (
                 None, (b'{0:>s}/default').format(xPath))
                default = {b'outPin': (_xml.readString(xmlCtx, defSec, b'outPin')), 
                   b'inPin': (_xml.readString(xmlCtx, defSec, b'inPin'))}
            lines[name] = {b'inPins': inPins, 
               b'outPins': outPins, 
               b'viaPins': viaPins, 
               b'default': default}

        return

    def __readDefaultLine(self, shared, xmlCtx, section):
        defSec = _xml.getSubsection(xmlCtx, section, b'default-line')
        xPath = (b'{0:>s}/default-line').format(TREE_SHARED_REL_FILE_PATH)
        xmlCtx = (None, xPath)
        name = _xml.readString(xmlCtx, defSec, b'line')
        outPin = _xml.readString(xmlCtx, defSec, b'outPin')
        inPin = _xml.readString(xmlCtx, defSec, b'inPin')
        self.__getLineInfo(xmlCtx, name, 0, outPin, inPin, shared[b'lines'])
        shared[b'default'] = {b'line': name, 
           b'inPin': inPin, 
           b'outPin': outPin}
        return

    def __getLineInfo(self, xmlCtx, lineName, nodeCD, outPin, inPin, lineShared):
        if lineName not in lineShared:
            raise _ConfigError(xmlCtx, (b'Line {0:>s} not found').format(lineName))
        line = lineShared[lineName]
        if inPin not in line[b'inPins'].keys():
            raise _ConfigError(xmlCtx, (b'Not found in pin = {0:>s} for line {1:>s}').format(inPin, lineName))
        if outPin not in line[b'outPins'].keys():
            raise _ConfigError(xmlCtx, (b'Not found out pin = {0:>s} for line {1:>s} line').format(outPin, lineName))
        return (line[b'outPins'][outPin],
         {b'childID': nodeCD, 
            b'inPin': (line[b'inPins'][inPin]), 
            b'viaPins': (line[b'viaPins'].get(outPin, {}).get(inPin, []))})

    def __readAvailableNations(self, xmlCtx, root):
        names = []
        indices = nations.INDICES
        for _, section in _xml.getChildren(xmlCtx, root, b'available-nations'):
            name = section.asString
            if name not in indices:
                _xml.raiseWrongXml(xmlCtx, b'available-nations', (b'Nation {0:>s} not found').format(name))
            if name not in nations.AVAILABLE_NAMES:
                LOG_ERROR(b'Nation ignored, it not found in nations.AVAILABLE_NAMES', name)
                continue
            names.append(name)

        return sorted(names, key=GUI_NATIONS_ORDER_INDEX.get)

    def __readAnnouncements(self, xmlCtx, root):
        for name, section in _xml.getChildren(xmlCtx, root, b'announcements'):
            if name in self.__announcements:
                _xml.raiseWrongXml(xmlCtx, b'announcements', (b'Announcement vehicles {0:>s} is already added').format(name))
            tags = _xml.readNonEmptyString(xmlCtx, section, b'tags')
            if tags:
                tags = frozenset(tags.split(b' '))
            else:
                tags = frozenset()
            self.__announcements[name] = _AnnouncementInfo(_xml.readNonEmptyString(xmlCtx, section, b'user-string'), _xml.readNonEmptyString(xmlCtx, section, b'tooltip'), tags, _xml.readInt(xmlCtx, section, b'level'), _xml.readNonEmptyString(xmlCtx, section, b'icon'), _xml.readBool(xmlCtx, section, b'is-elite'))

        return

    def __getNextTypeID(self, nationID):
        nextTypeID = self.__nextTypeIDs[nationID]
        if not nextTypeID:
            nextTypeID = max(vehicles.g_list.getList(nationID).keys())
        nextTypeID += 1
        self.__nextTypeIDs[nationID] = nextTypeID
        return nextTypeID

    def __getNodeByName(self, nodeName, nationID, order=0):
        nodes = self.__nodes[nationID]
        if nodes is None:
            nodes = self.__nodes[nationID] = {}
        if nodeName in nodes:
            node = nodes[nodeName]
            if order:
                node.order = order
            return node
        isFound = True
        isAnnouncement = False
        if nodeName in self.__announcements:
            isAnnouncement = True
            vehicleTypeID = self.__getNextTypeID(nationID)
        else:
            _, vehicleTypeID = vehicles.g_list.getIDsByName((b'{0:>s}:{1:>s}').format(nations.NAMES[nationID], nodeName))
        try:
            nodeCD = vehicles.makeIntCompactDescrByID(_VEHICLE_TYPE_NAME, nationID, vehicleTypeID)
        except AssertionError:
            nodeCD = 0
            isFound = False

        if isAnnouncement:
            self.__announcementCDToName[nodeCD] = nodeName
        node = BaseNode(nodeName, nationID, vehicleTypeID, nodeCD, isFound=isFound, isAnnouncement=isAnnouncement, order=order)
        nodes[nodeName] = node
        return node

    def __isBoundActionNode(self, node, boundNodes):
        nodeCD = node.getNodeCD()
        nationID = node.getNationID()
        if nationID not in self.techTreeEventsListener.getNations(unviewed=True):
            return False
        hasAction = self.techTreeEventsListener.hasActiveAction
        if hasAction(nodeCD, nationID):
            return not any(hasAction(boundCD, nationID) for boundCD in boundNodes)
        return False

    def __readNodeLines(self, parentCD, nation, xmlCtx, section, shared):
        linesSec = section[b'lines']
        if linesSec is None:
            linesSec = {}
        result = defaultdict(_makeLines)
        nextLevel = self.__nextLevels[parentCD].keys()
        _, xPath = xmlCtx
        xPath = (b'{0:>s}/lines').format(xPath)
        nationID = nations.INDICES[nation]
        for name, sub in linesSec.items():
            xmlCtx = (None, (b'{0:>s}/lines/{1:>1}').format(xPath, name))
            node = self.__getNodeByName(name, nationID)
            if not node.isFound:
                raise _ConfigError(xmlCtx, (b'Unknown vehicle type name {0:>s}').format(name))
            if IS_DEVELOPMENT and not node.isAnnouncement:
                if node.nodeCD not in nextLevel:
                    _, nationID, vTypeID = vehicles.parseIntCompactDescr(parentCD)
                    pName = vehicles.g_list.getList(nationID)[vTypeID].name
                    LOG_ERROR((b'{0:>s} does not have relation with {1:>s}').format(pName, name))
                else:
                    nextLevel.remove(node.nodeCD)
            if node.isAnnouncement:
                self.__nextAnnouncements[parentCD].append(node.nodeCD)
            data = shared[b'default'].copy()
            tags = sub.keys()
            lineShared = shared[b'lines']
            line = data[b'line']
            if b'line' in tags:
                line = sub.readString(b'line')
                if line in lineShared:
                    data.update(lineShared[line][b'default'])
            outPin = data[b'outPin']
            if b'outPin' in tags:
                outPin = sub.readString(b'outPin')
            inPin = data[b'inPin']
            if b'inPin' in tags:
                inPin = sub.readString(b'inPin')
            outPos, lineInfo = self.__getLineInfo(xmlCtx, line, node.nodeCD, outPin, inPin, lineShared)
            result[outPin][b'outPin'] = outPos
            result[outPin][b'outLiteral'] = outPin
            result[outPin][b'inPins'].append(lineInfo)

        if IS_DEVELOPMENT and nextLevel:
            _, nationID, vTypeID = vehicles.parseIntCompactDescr(parentCD)
            pName = vehicles.g_list.getList(nationID)[vTypeID].name
            for itemCD in nextLevel:
                _, nationID, vTypeID = vehicles.parseIntCompactDescr(itemCD)
                uName = vehicles.g_list.getList(nationID)[vTypeID].name
                LOG_ERROR((b'Relation between {0:>s} and {1:>s} are not defined').format(pName, uName))

        return listvalues(result)

    def __readNation(self, shared, nation, clearCache=False):
        xmlPath = NATION_TREE_REL_FILE_PATH.format(nation)
        displayInfo, displaySettings, gridSettings = self.__readNodeList(shared, nation, xmlPath, clearCache, NODE_ORDER_PREFIX_COMMON)
        xmlPath = NATION_TREE_REL_PREMIUM_FILE_PATH.format(nation)
        premDisplayInfo, _, gridPremiumSettings = self.__readNodeList(shared, nation, xmlPath, clearCache, NODE_ORDER_PREFIX_PREMIUM)
        nationID = nations.INDICES[nation]
        self.__displaySettings[nationID] = displaySettings
        self.__gridSettings[nationID] = gridSettings
        self.__premiumGridSettings[nationID] = gridPremiumSettings
        displayInfo.update(premDisplayInfo)
        return displayInfo

    def __readNodeList(self, shared, nation, xmlPath, clearCache=False, orderPrefix=0):
        if clearCache:
            ResMgr.purge(xmlPath)
        section = ResMgr.openSection(xmlPath)
        if section is None:
            LOG_ERROR(b'can not open or read nation tree: ', nation, xmlPath)
            return ({}, {}, {})
        else:
            xmlCtx = (None, xmlPath)
            settingsName = _xml.readString(xmlCtx, section, b'settings')
            if settingsName not in shared[b'settings']:
                LOG_ERROR(b'not found settings (<settings> tag): ', settingsName, xmlPath)
                return ({}, {}, {})
            precessed = _xml.getSubsection(xmlCtx, section, b'grid')
            gridName = precessed.asString
            if gridName not in shared[b'grids']:
                LOG_ERROR(b'not found grid (<grid> tag): ', gridName, xmlPath)
                return ({}, {}, {})
            xPath = (b'{0:>s}/grid').format(xmlPath)
            xmlCtx = (None, xPath)
            grid = shared[b'grids'][gridName]
            settings = {}
            settings = shared[b'settings'][settingsName]
            rows = _xml.readInt(xmlCtx, precessed, b'rows')
            columns = _xml.readInt(xmlCtx, precessed, b'columns')
            nationID = nations.INDICES[nation]
            hasRoot = settings[b'hasRoot']
            if hasRoot:
                coords = self.__makeGridCoordsWithRoot(grid, rows, columns)
            else:
                coords = self.__makeGridCoordsWoRoot(grid, rows, columns)
            getVehicle = vehicles.g_cache.vehicle
            precessed = _xml.getChildren(xmlCtx, section, b'nodes')
            displayInfo = {}
            for name, nodeSection in precessed:
                xPath = (b'{0:>s}/nodes/{1:>s}').format(xmlPath, name)
                xmlCtx = (None, xPath)
                row = _xml.readInt(xmlCtx, nodeSection, b'row')
                column = _xml.readInt(xmlCtx, nodeSection, b'column')
                node = self.__getNodeByName(name, nationID, order=column * 1000 + orderPrefix * 100 + row)
                if not node.isFound:
                    raise _ConfigError(xmlCtx, (b'Unknown vehicle type name {0:>s}').format(node.nodeName))
                if not node.isAnnouncement:
                    vType = getVehicle(node.nationID, node.itemTypeID)
                    nextLevel = [(idx, descr) for idx, descr in enumerate(vType.unlocksDescrs) if getTypeOfCompactDescr(descr[1]) == _VEHICLE]
                    for unlockDescr in vType.unlocksDescrs:
                        self.__unlockPrices[unlockDescr[1]][vType.compactDescr] = unlockDescr[0]

                    for idx, data in nextLevel:
                        xpCost = data[0]
                        nextCD = data[1]
                        required = data[2:]
                        self.__nextLevels[node.nodeCD][nextCD] = (
                         idx, xpCost, set(required))
                        self.__topLevels[nextCD].add(node.nodeCD)
                        for itemCD in required:
                            self.__topItems[itemCD].add(node.nodeCD)

                if hasRoot and row > 1 and column == 1:
                    raise _ConfigError(xmlCtx, (b'In first column must be one node - root node, {0:>s} ').format(node.nodeName))
                if row > rows or column > columns:
                    raise _ConfigError(xmlCtx, (b'Invalid row or column index: {0:>s}, {1:d}, {2:d}').format(node.nodeName, row, column))
                lines = self.__readNodeLines(node.nodeCD, nation, xmlCtx, nodeSection, shared)
                displayInfo[node.nodeCD] = {b'row': row, 
                   b'column': column, 
                   b'position': (coords[column - 1][row - 1]), 
                   b'lines': lines}

            return (
             displayInfo, settings, self.__makeGridSettings(grid, rows, columns))

    def __makeAbsoluteCoordinates(self):
        for displayInfo in self.__displayInfo:
            if displayInfo is None:
                continue
            for info in viewvalues(displayInfo):
                lines = info[b'lines']
                nodePos = info[b'position']
                for lineInfo in lines:
                    pinPos = lineInfo[b'outPin']
                    lineInfo[b'outPin'] = (
                     pinPos[0] + nodePos[0], pinPos[1] + nodePos[1])
                    inPins = lineInfo[b'inPins']
                    for pin in inPins:
                        if pin[b'childID'] not in displayInfo:
                            continue
                        childInfo = displayInfo[pin[b'childID']]
                        childPos = childInfo[b'position']
                        pinPos = pin[b'inPin']
                        pin[b'inPin'] = (
                         pinPos[0] + childPos[0], pinPos[1] + childPos[1])
                        pin[b'viaPins'] = [(item[0] + nodePos[0], item[1] + nodePos[1]) for item in pin[b'viaPins']]

        return

    def __makeGridCoordsWithRoot(self, grid, rows, columns):
        start, step = grid[b'horizontal']
        hRange = xrange(start, start + step * columns, step)
        start, step = grid[b'vertical']
        vRange = xrange(start, start + step * rows, step)
        root = grid[b'root'][b'start']
        startRoot = root[1] + step * (rows >> 1)
        coordinates = [
         [
          [
           root[0], startRoot]]]
        for x in hRange:
            coordinates.append([(x, y) for y in vRange])

        return coordinates

    def __makeGridCoordsWoRoot(self, grid, rows, columns):
        coordinates = []
        start, step = grid[b'horizontal']
        hRange = xrange(start, start + step * (columns + 1), step)
        start, step = grid[b'vertical']
        vRange = xrange(start, start + step * (rows + 1), step)
        for x in hRange:
            coordinates.append([(x, y) for y in vRange])

        return coordinates

    def __makeGridSettings(self, grid, rows, columns):
        _, hStep = grid[b'horizontal']
        _, vStep = grid[b'vertical']
        gridSettings = {b'start': (list(grid[b'root'][b'start'])), 
           b'step': [
                   hStep, vStep], 
           b'size': [
                   rows, columns]}
        return gridSettings


g_techTreeDP = _TechTreeDataProvider()
