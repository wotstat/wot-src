from __future__ import absolute_import
from future.utils import viewvalues
import nations
from gui import GUI_NATIONS_ORDER_INDEX_REVERSED
from gui.Scaleform.daapi.view.meta.VehicleSelectPopoverMeta import VehicleSelectPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES_REVERSED
from gui.shared.utils import sortByFields

class VehicleSelectPopoverBase(VehicleSelectPopoverMeta):

    def __init__(self, ctx=None):
        super(VehicleSelectPopoverBase, self).__init__(ctx)
        self._vehDP = None
        self._isMultiSelect = True
        if ctx is not None:
            data = ctx.get(b'data', None)
            self._isMultiSelect = data.isMultiSelect if data is not None else True
        return

    def setVehicleSelected(self, dbID, autoClose):
        self._vehDP.toggleSelectionByID(dbID)
        if autoClose:
            self.addButtonClicked()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _initDP(self):
        self._vehDP = VehiclesDataProvider(self._isMultiSelect)
        self._vehDP.setFlashObject(self.as_getTableDPS())
        return

    def _dispose(self):
        super(VehicleSelectPopoverBase, self)._dispose()
        self._vehDP.fini()
        self._vehDP = None
        return

    def _updateSortField(self):
        sort = self._vehDP.getLastSortMethod()
        order = b'ascending' if sort[0][1] else b'descending'
        self.as_updateTableSortFieldS(sortField=sort[0][0], sortDirection=order)
        return


class VehiclesDataProvider(SortableDAAPIDataProvider):

    def __init__(self, isMultiSelect=True):
        super(VehiclesDataProvider, self).__init__()
        self.__isMultiSelect = isMultiSelect
        self.__selectedDbID = 0
        self.__list = None
        self.__listMapping = {}
        self._sort = (
         (
          b'level', False),)
        self.__sortMapping = {b'check': (lambda v: v[b'selected']), 
           b'nations': (lambda v: GUI_NATIONS_ORDER_INDEX_REVERSED[nations.NAMES[v[b'nationID']]]), 
           b'type': (lambda v: VEHICLE_TYPES_ORDER_INDICES_REVERSED[v[b'type']]), 
           b'level': (lambda v: v[b'level'] << 16 | GUI_NATIONS_ORDER_INDEX_REVERSED[nations.NAMES[v[b'nationID']]] << 8 | VEHICLE_TYPES_ORDER_INDICES_REVERSED[v[b'type']]), 
           b'name': (lambda v: v[b'shortUserName']), 
           b'hangar': (lambda v: v[b'inHangar'])}
        return

    @property
    def sortedCollection(self):
        return sortByFields(self._sort, self.__list, self.__sortingMethod)

    @property
    def collection(self):
        return self.__list

    def emptyItem(self):
        return

    def pySortOn(self, fields, order):
        super(VehiclesDataProvider, self).pySortOn(fields, order)
        if self.__list:
            self.__list = sortByFields(self._sort, self.__list, self.__sortingMethod)
            self.buildList(self.__list)
        return

    def buildList(self, vehicleVOs):
        self.__list = vehicleVOs
        for item in self.__list:
            storedItem = self.__listMapping.get(item[b'dbID'])
            if storedItem:
                item[b'selected'] = storedItem[b'selected']
            self.__listMapping[item[b'dbID']] = item
            if not self.__isMultiSelect and item[b'selected']:
                self.__selectedDbID = item[b'dbID']

        self.refresh()
        return

    def toggleSelectionByID(self, dbID):
        if not self.__isMultiSelect:
            if self.__selectedDbID:
                self.__listMapping[self.__selectedDbID][b'selected'] = False
            self.__selectedDbID = dbID
        self.__listMapping[dbID][b'selected'] = not self.__listMapping[dbID][b'selected']
        self.refresh()
        return

    def getSelected(self):
        return tuple(v[b'dbID'] for v in viewvalues(self.__listMapping) if v[b'selected'])

    def getLastSortMethod(self):
        return self._sort

    def clear(self):
        self.__list = []
        self.__listMapping = {}
        return

    def fini(self):
        self.clear()
        self.destroy()
        return

    def __sortingMethod(self, item, field):
        valueGetter = self.__sortMapping[field]
        return valueGetter(item)
