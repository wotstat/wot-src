from __future__ import absolute_import
from visual_script.block import Block, Meta
from visual_script.dependency import dependencyImporter
from visual_script import ASPECT
from visual_script.slot_types import SLOT_TYPE
event_dispatcher, dependency, game_controller, CurrentVehicle = dependencyImporter(b'advent_calendar.gui.shared.event_dispatcher', b'helpers.dependency', b'advent_calendar.skeletons.game_controller', b'CurrentVehicle')

class AdventCalendarMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 10512127

    @classmethod
    def blockCategory(cls):
        return b'Advent'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class OpenAdventCalendar(Block, AdventCalendarMeta):

    def __init__(self, *args, **kwargs):
        super(OpenAdventCalendar, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self, *_):
        event_dispatcher.showAdventCalendarMainWindow()
        self._out.call()
        return


class OnAdventCalendarConfigChanged(Block, AdventCalendarMeta):
    __adventController = dependency.descriptor(game_controller.IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        super(OnAdventCalendarConfigChanged, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def onStartScript(self):
        self.__adventController.onConfigChanged += self.__onConfigChanged
        return

    def onFinishScript(self):
        self.__adventController.onConfigChanged -= self.__onConfigChanged
        return

    def __onConfigChanged(self):
        self._out.call()
        return


class IsAdventCalendarAvailable(Block, AdventCalendarMeta):
    __adventController = dependency.descriptor(game_controller.IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        super(IsAdventCalendarAvailable, self).__init__(*args, **kwargs)
        self._isAvailable = self._makeDataOutputSlot(b'isAvailable', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        self._isAvailable.setValue(self.__adventController.isAvailable())
        return


class ADOnPreviewVehicleOrStyleSelected(Block, AdventCalendarMeta):

    def __init__(self, *args, **kwargs):
        super(ADOnPreviewVehicleOrStyleSelected, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def onStartScript(self):
        CurrentVehicle.g_currentPreviewVehicle.onChanged += self.__onPreviewVehicleSelected
        return

    def onFinishScript(self):
        CurrentVehicle.g_currentPreviewVehicle.onChanged -= self.__onPreviewVehicleSelected
        return

    def __onPreviewVehicleSelected(self):
        self._out.call()
        return


class ADIsPreviewVehicleOrStyleSelected(Block, AdventCalendarMeta):

    def __init__(self, *args, **kwargs):
        super(ADIsPreviewVehicleOrStyleSelected, self).__init__(*args, **kwargs)
        self._isSelected = self._makeDataOutputSlot(b'isSelected', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        self._isSelected.setValue(CurrentVehicle.g_currentPreviewVehicle.item is not None)
        return
