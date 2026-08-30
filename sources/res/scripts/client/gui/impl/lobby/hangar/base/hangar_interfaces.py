from __future__ import absolute_import
import typing
from gui.shared.utils.requesters import RequestCriteria
if typing.TYPE_CHECKING:
    from Event import Event
    from gui.shared.gui_items import Vehicle

class IVehicleFilter(object):
    onDiff = None

    @property
    def criteria(self):
        raise NotImplementedError
        return

    @property
    def vehicles(self):
        raise NotImplementedError
        return

    def initialize(self):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return


class IAccountStyles(object):
    onChanged = None

    @property
    def criteria(self):
        raise NotImplementedError
        return

    def initialize(self):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return
