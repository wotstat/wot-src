from __future__ import absolute_import
from future.utils import viewvalues
import BigWorld
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
from helpers import time_utils
FLAG_ICON_TEMPLATE = b'../maps/icons/battle/respawn/optimize_flags_160x100/%s.png'
VEHICLE_TYPE_TEMPLATE = b'../maps/icons/vehicleTypes/%s.png'
VEHICLE_FORMAT = makeHtmlString(b'html_templates:igr/premium-vehicle', b'name', {})
VEHICLE_ELITE_TYPE_TEMPLATE = b'../maps/icons/vehicleTypes/elite/%s.png'

def getVehicleName(vehicle):
    tags = vehicle.type.tags
    isIGR = bool(VEHICLE_TAGS.PREMIUM_IGR in tags)
    vehicleName = vehicle.type.shortUserString if isIGR else vehicle.type.userString
    if isIGR:
        vehicleName = VEHICLE_FORMAT % {b'vehicle': vehicleName}
    return vehicleName


def getSlotsStatesData(vehs, cooldowns, disabled, limits=None):
    if limits is None:
        limits = {}
    result = []
    for v in viewvalues(vehs):
        compactDescr = v.intCD
        cooldownTime = cooldowns.get(compactDescr, 0)
        cooldownStr = b''
        cooldown = cooldownTime - BigWorld.serverTime()
        enabled = cooldown <= 0 and not disabled and compactDescr not in limits
        if not enabled:
            if cooldown > 0:
                if disabled:
                    cooldownStr = backport.text(R.strings.ingame_gui.respawnView.disabledLbl())
                else:
                    cooldownStr = backport.text(R.strings.ingame_gui.respawnView.cooldownLbl(), time=time_utils.getTimeLeftFormat(cooldown))
            else:
                cooldownStr = backport.text(R.strings.ingame_gui.respawnView.classNotAvailable())
        result.append({b'vehicleID': compactDescr, 
           b'enabled': enabled, 
           b'cooldown': cooldownStr, 
           b'settings': (v.settings)})

    return result
