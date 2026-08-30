from collections import namedtuple
from gui.clans.data_wrapper.utils import FieldsCheckerMixin, fmtUnavailableValue
from shared_utils import makeTupleByDict
_StrongholdEventClanInfoData = namedtuple(b'_StrongholdEventClanInfoData', [
 b'primetime_start', b'primetime_end'])
_StrongholdEventClanInfoData.__new__.__defaults__ = (0, 0)

class StrongholdEventClanInfoData(_StrongholdEventClanInfoData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'primetime_start',))
    def getPrimeTimeStart(self):
        return self.primetime_start

    @fmtUnavailableValue(fields=(b'primetime_end',))
    def getPrimeTimeEnd(self):
        return self.primetime_end


_StrongholdEventConfig = namedtuple(b'_StrongholdEventConfig', [
 11, 12, 13, 14, 15, 
 16, 17, 18, 
 19, 20, 21, 22, 23])
_StrongholdEventConfig.__new__.__defaults__ = (
 b'', [], [], b'', b'', 0, 0, 0, 0, 0, 0, False, [])

class StrongholdEventConfig(_StrongholdEventConfig, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'visible_start_date',))
    def getVisibleStartDate(self):
        return self.visible_start_date

    @fmtUnavailableValue(fields=(b'visible_end_date',))
    def getVisibleEndDate(self):
        return self.visible_end_date

    @fmtUnavailableValue(fields=(b'event_start_date',))
    def getStartDate(self):
        return self.event_start_date

    @fmtUnavailableValue(fields=(b'event_end_date',))
    def getEndDate(self):
        return self.event_end_date

    @fmtUnavailableValue(fields=(b'unfreeze_vehicle_roles',))
    def getUnfreezeVehicleRoles(self):
        return self.unfreeze_vehicle_roles


_StrongholdEventSettingsData = namedtuple(b'_StrongholdEventClanInfoData', [
 b'event_config'])
_StrongholdEventSettingsData.__new__.__defaults__ = (None,)

class StrongholdEventSettingsData(_StrongholdEventSettingsData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'event_config',))
    def getEventConfig(self):
        return makeTupleByDict(StrongholdEventConfig, self.event_config)

    def getStartDate(self):
        return self.getEventConfig().getStartDate()

    def getEndDate(self):
        return self.getEventConfig().getEndDate()
