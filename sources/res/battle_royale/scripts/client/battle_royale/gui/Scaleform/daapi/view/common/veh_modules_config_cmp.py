from __future__ import absolute_import
import logging, typing
from future.utils import lrange
from gui.Scaleform.daapi.view.meta.VehModulesConfiguratorCmpMeta import VehModulesConfiguratorCmpMeta
from gui.doc_loaders.battle_royale_settings_loader import getTreeModuleIcon
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items import GUI_ITEM_TYPE, isItemVehicleHull
from helpers import int2roman
_logger = logging.getLogger(__name__)
_GAP_BETWEEN_COLUMNS = 100
_GAP_BETWEEN_MODULES = 60
_ITEM_TYPE_TO_HEADER_ICON = {(GUI_ITEM_TYPE.TURRET): (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.tower())), 
   (GUI_ITEM_TYPE.GUN): (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.gun())), 
   (GUI_ITEM_TYPE.ENGINE): (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.engine())), 
   (GUI_ITEM_TYPE.RADIO): (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.radio())), 
   (GUI_ITEM_TYPE.CHASSIS): (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.chassis())), 
   b'hull': (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.hull())), 
   b'vehicle': (backport.image(R.images.gui.maps.icons.battleRoyale.tree.header.vehicle()))}

def _makeItemVO(intCD, icon, selected):
    return {b'intCD': intCD, 
       b'icon': icon, 
       b'potentialLinks': [], b'activeLink': (-1), 
       b'selected': selected, 
       b'available': False, 
       b'gap': _GAP_BETWEEN_MODULES}


def _makeModuleVO(item, selected):
    itemIntCD = item.intCD
    return _makeItemVO(itemIntCD, getTreeModuleIcon(item), selected)


def _makeColumnVO(index, modules, headerIcon, selected=False):
    return {b'index': index, 
       b'headerIcon': headerIcon, 
       b'headerText': (int2roman(index + 1)), 
       b'selected': selected, 
       b'highlighted': False, 
       b'availableForSelection': False, 
       b'modules': modules, 
       b'gap': _GAP_BETWEEN_COLUMNS}


def _makeFirstColumnVO(vehicle):
    return _makeColumnVO(0, [
     _makeItemVO(vehicle.intCD, b'vehicle', selected=True)], _ITEM_TYPE_TO_HEADER_ICON[b'vehicle'], selected=True)


def _getHeaderIcon(item, vehicle):
    if item.itemTypeID == GUI_ITEM_TYPE.CHASSIS and isItemVehicleHull(item.intCD, vehicle):
        return _ITEM_TYPE_TO_HEADER_ICON[b'hull']
    return _ITEM_TYPE_TO_HEADER_ICON[item.itemTypeID]


class VehicleModulesConfiguratorCmp(VehModulesConfiguratorCmpMeta):

    def __init__(self):
        super(VehicleModulesConfiguratorCmp, self).__init__()
        self.__inited = False
        self.__availableLevel = None
        self.__currentLevel = 0
        self._columnsVOs = None
        self.__moduleIntCdToPosition = None
        self._vehicle = None
        return

    def setVehicle(self, vehicle):
        self._vehicle = vehicle
        return

    def setAvailableLevel(self, level):
        if self.__availableLevel != level:
            self.__availableLevel = level
            if self.__inited:
                updatedIndexes = self._updateColumns()
                if updatedIndexes:
                    self._sendUpdate(updatedIndexes)
            else:
                self._refresh()
                self.__inited = True
        return

    def getAvailableLevel(self):
        return self.__availableLevel

    def onClick(self, intCD, columnIdx, moduleIdx):
        return False

    def _syncVehicle(self, intCD):
        colID, modID = self.__moduleIntCdToPosition[intCD]
        if not self._columnsVOs[colID][b'modules'][modID][b'selected']:
            self._recreate()
            _logger.info(b'Module has been changed outside current view.')
        return

    def _recreate(self):
        self._init()
        self.as_updateItemsS(self._columnsVOs)
        return

    def _refresh(self):
        self._init()
        self.as_setItemsS(self._columnsVOs)
        return

    def _getHighlightedModules(self):
        result = []
        for column in self._columnsVOs:
            if column[b'highlighted']:
                for module in column[b'modules']:
                    if module[b'available']:
                        result.append((module[b'intCD'], module[b'icon'], len(result)))

                break

        return result

    def _init(self):
        self.__moduleIntCdToPosition = {}
        vehicle = self._vehicle
        self._columnsVOs = [_makeFirstColumnVO(vehicle)]
        currentLevel = 1
        for _, _, intCD, unlocks in vehicle.getUnlocksDescrs():
            item = self._getItem(intCD)
            level = item.level
            for unlockIntCD in unlocks:
                itemWhichUnlocks = self._getItem(unlockIntCD)
                if itemWhichUnlocks.level == level:
                    break

            if self._canBeShown(intCD, level, unlocks):
                columnIndex = level - 1
                while len(self._columnsVOs) <= columnIndex:
                    self._columnsVOs.append(None)

                moduleSelected = False
                if not self._columnsVOs[columnIndex]:
                    moduleSelected = self._isModuleSelected(item, vehicle)
                    self._columnsVOs[columnIndex] = _makeColumnVO(columnIndex, [_makeModuleVO(item, moduleSelected)], _getHeaderIcon(item, vehicle))
                    self.__moduleIntCdToPosition[item.intCD] = (
                     columnIndex, 0)
                else:
                    modules = self._columnsVOs[columnIndex][b'modules']
                    for m in modules:
                        if m[b'intCD'] == intCD:
                            break
                    else:
                        self.__moduleIntCdToPosition[item.intCD] = (
                         columnIndex, len(modules))
                        moduleSelected = self._isModuleSelected(item, vehicle)
                        modules.append(_makeModuleVO(item, moduleSelected))

                if moduleSelected:
                    self._columnsVOs[columnIndex][b'selected'] = True
                    if level > currentLevel:
                        currentLevel = level

        self.__currentLevel = currentLevel
        self._updateLinks(vehicle)
        self._updateColumns()
        return

    def _canBeShown(self, intCD, level, unlocks):
        return True

    def _isModuleSelected(self, item, vehicle):
        return item.isInstalled(vehicle)

    def _mayInstallModuleOnCurrentVehicle(self, mItem):
        return False

    def _installModule(self, moduleItem):
        return False

    def _dispose(self):
        self._vehicle = None
        self._columnsVOs = None
        super(VehicleModulesConfiguratorCmp, self)._dispose()
        return

    def _setCurrentLevel(self, moduleLevel):
        if moduleLevel > self.__currentLevel:
            self.__currentLevel = moduleLevel
        return

    def _updateColumns(self):
        changedColumns = set()
        currentColumn = self.__currentLevel - 1
        i = currentColumn - 1
        while i >= 0:
            columnVO = self._columnsVOs[i]
            if columnVO is not None:
                for mVO in columnVO[b'modules']:
                    if mVO[b'available']:
                        mVO[b'available'] = False
                        changedColumns.add(i)

                if columnVO[b'availableForSelection']:
                    columnVO[b'availableForSelection'] = False
                    changedColumns.add(i)
            i = i - 1

        j = currentColumn
        totalColumns = len(self._columnsVOs)
        availableColumn = self.__availableLevel - 1
        alreadyHasHighlight = False
        while j <= availableColumn and j < totalColumns:
            columnVO = self._columnsVOs[j]
            availableForSelection = currentColumn < j <= availableColumn
            if columnVO[b'availableForSelection'] != availableForSelection:
                columnVO[b'availableForSelection'] = availableForSelection
                changedColumns.add(j)
            columnHighlighted = not alreadyHasHighlight and availableForSelection
            if columnVO[b'highlighted'] != columnHighlighted:
                columnVO[b'highlighted'] = columnHighlighted
                for mVO in columnVO[b'modules']:
                    if columnHighlighted:
                        moduleItem = self._getItem(mVO[b'intCD'])
                        success = self._mayInstallModuleOnCurrentVehicle(moduleItem)
                        mVO[b'available'] = success
                    else:
                        mVO[b'available'] = False

                changedColumns.add(j)
            if columnVO[b'highlighted']:
                alreadyHasHighlight = True
            j = j + 1

        return changedColumns

    def _updateLinks(self, vehicle):
        for i in reversed(lrange(1, len(self._columnsVOs))):
            currentColumn = self._columnsVOs[i]
            if not currentColumn:
                return
            for moduleVO in currentColumn[b'modules']:
                for itemsCDs in vehicle.descriptor.type.unlocksDescrs:
                    intCD = itemsCDs[1]
                    if intCD == moduleVO[b'intCD']:
                        hasDirectLinks = False
                        for j in range(1, len(itemsCDs)):
                            unlockIntCD = itemsCDs[j]
                            if unlockIntCD in self.__moduleIntCdToPosition:
                                unlockColumnIdx, unlockModuleIdx = self.__moduleIntCdToPosition[unlockIntCD]
                                if unlockColumnIdx == i - 1:
                                    if unlockIntCD not in moduleVO[b'potentialLinks']:
                                        moduleVO[b'potentialLinks'].append(unlockIntCD)
                                    hasDirectLinks = True
                                    unlockModuleVO = self._columnsVOs[unlockColumnIdx][b'modules'][unlockModuleIdx]
                                    if moduleVO[b'selected'] and unlockModuleVO[b'selected']:
                                        moduleVO[b'activeLink'] = unlockIntCD

                        if not hasDirectLinks:
                            columnVOO = self._columnsVOs[i - 1]
                            if not columnVOO:
                                pass
                            else:
                                for prevModuleVO in columnVOO[b'modules']:
                                    prevModuleIntCD = prevModuleVO[b'intCD']
                                    if prevModuleIntCD not in moduleVO[b'potentialLinks']:
                                        moduleVO[b'potentialLinks'].append(prevModuleIntCD)
                                    if moduleVO[b'selected'] and prevModuleVO[b'selected']:
                                        moduleVO[b'activeLink'] = prevModuleIntCD

        return

    def _getItem(self, intCD):
        raise NotImplementedError
        return

    def _sendUpdate(self, updatedIndexes):
        self.as_updateItemsS([self._columnsVOs[i] for i in updatedIndexes])
        return
