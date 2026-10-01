from gui.prb_control.entities.base.unit.requester import UnitRequestProcessor
from portal_common.portal_constants import CLIENT_UNIT_CMD

class PortalUnitRequestProcessor(UnitRequestProcessor):

    def doRequest(self, ctx, methodName, *args, **kwargs):
        if methodName == b'setVehicle':
            self.__setPortalVehicle(ctx, *args, **kwargs)
            return
        super(PortalUnitRequestProcessor, self).doRequest(ctx, methodName, *args, **kwargs)
        return

    def __setPortalVehicle(self, ctx, *args, **kwargs):
        vehInvID = kwargs.pop(b'vehInvID', -1)
        setReady = int(kwargs.pop(b'setReady', False))
        self.doRequest(ctx, b'doUnitCmd', CLIENT_UNIT_CMD.SET_PORTAL_VEHICLE, vehInvID, setReady, b'', **kwargs)
        return
