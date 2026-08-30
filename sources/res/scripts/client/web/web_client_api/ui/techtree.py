from helpers import dependency
from gui.shared import event_dispatcher
from skeletons.gui.shared import IItemsCache
from web.web_client_api import W2CSchema, w2c, Field

class _OpenTechTreeSchema(W2CSchema):
    vehicle_id = Field(required=True, type=int)


class TechTreeTabWebApiMixin(object):
    itemsCache = dependency.descriptor(IItemsCache)

    @w2c(_OpenTechTreeSchema, b'tech_tree')
    def openTechTree(self, cmd):
        event_dispatcher.showTechTree(cmd.vehicle_id)
        return

    @w2c(_OpenTechTreeSchema, b'research')
    def openResearch(self, cmd):
        event_dispatcher.showResearchView(cmd.vehicle_id)
        return

    @w2c(_OpenTechTreeSchema, b'vehicleHubOverview')
    def openVehicleHubOverview(self, cmd):
        event_dispatcher.showVehicleHubOverview(cmd.vehicle_id)
        return
