from __future__ import absolute_import
import typing, weakref
from events_containers.common.containers import ClientEventsContainer

class IViewUpdater(object):

    def initialize(self):
        return

    def finalize(self):
        return

    def destroy(self):
        return


class ViewUpdatersCollection(object):

    def __init__(self):
        self.__updaters = []
        return

    def initialize(self, updaters):
        self.__updaters = updaters
        for updater in self.__updaters:
            updater.initialize()

        return

    def finalize(self):
        for updater in self.__updaters:
            updater.finalize()

        return

    def destroy(self):
        updaters, self.__updaters = self.__updaters, []
        for updater in updaters:
            updater.destroy()

        return


class ViewUpdater(ClientEventsContainer, IViewUpdater):

    def __init__(self, view):
        super(ViewUpdater, self).__init__()
        self.__view = weakref.proxy(view)
        return

    @property
    def view(self):
        return self.__view

    def destroy(self):
        self.__view = None
        super(ViewUpdater, self).destroy()
        return
