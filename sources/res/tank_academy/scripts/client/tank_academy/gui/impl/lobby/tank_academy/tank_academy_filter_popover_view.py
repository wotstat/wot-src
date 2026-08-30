from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.gen import R
from gui.impl.pub.view_impl import PopOverViewImpl
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.popovers import filter_control_view_model as filter_control_vm, tank_academy_filter_popover_view_model as ta_filter_popover_vm

class TankAcademyFilterPopoverView(PopOverViewImpl):
    __slots__ = (b'__filters', b'__updateCallback')

    def __init__(self, filtersDict=None, updateCallback=None):
        settings = ViewSettings(R.views.tank_academy.lobby.tank_academy.popovers.TankAcademyFilterPopoverView())
        settings.flags = ViewFlags.VIEW
        settings.model = ta_filter_popover_vm.TankAcademyFilterPopoverViewModel()
        self.__filters = filtersDict or {}
        self.__updateCallback = updateCallback
        super(TankAcademyFilterPopoverView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(TankAcademyFilterPopoverView, self).getViewModel()

    def onToggleFilter(self, event):
        changesFromEvent = {b'Types': (event.get(ta_filter_popover_vm.TankAcademyFilterPopoverViewModel.ARG_CONTROL_TYPE, {})), 
           b'Nations': (event.get(ta_filter_popover_vm.TankAcademyFilterPopoverViewModel.ARG_CONTROL_NATION, {}))}
        changes = {k: {v: (not self.__filters[k][v])} for k, v in changesFromEvent.iteritems() if k and v}
        self._updateFilter(changes)
        return

    def updateFilterFromOutside(self, changes):
        self._updateFilter(changes)
        return

    def _onLoading(self, *args, **kwargs):
        super(TankAcademyFilterPopoverView, self)._onLoading(*args, **kwargs)
        self._update()
        return

    def _finalize(self):
        self.__updateCallback = None
        self.__filters = None
        super(TankAcademyFilterPopoverView, self)._finalize()
        return

    def _update(self):
        with self.viewModel.transaction() as tx:
            for key in self.__filters:
                filterArray = getattr(tx, b'get' + key)()
                filterArray.clear()
                filters = self.__filters[key]
                for filterName, filterValue in filters.iteritems():
                    currentControl = filter_control_vm.FilterControlViewModel()
                    currentControl.setName(filterName)
                    currentControl.setIsSelected(filterValue)
                    filterArray.addViewModel(currentControl)

                filterArray.invalidate()

        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onToggleFilter, self.onToggleFilter),)

    def _changeVMValue(self, vm, valuesDict, valueName):
        allVMs = getattr(vm, b'get' + valueName)()
        for singleVM in allVMs:
            name = singleVM.getName()
            if name in valuesDict:
                singleVM.setIsSelected(valuesDict[name])

        return

    def _updateFilter(self, changes):
        for filterName in self.__filters:
            self.__filters[filterName].update(changes.get(filterName, {}))

        with self.viewModel.transaction() as tx:
            for change in changes:
                self._changeVMValue(tx, changes[change], change)

        if self.__updateCallback:
            self.__updateCallback(self.__filters)
        return
