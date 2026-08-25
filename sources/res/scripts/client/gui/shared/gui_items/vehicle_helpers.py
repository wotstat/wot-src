from __future__ import absolute_import
from constants import ROLE_TYPE, ROLE_TYPE_TO_LABEL
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleIcon
from gui.shared.gui_items.Vehicle import Vehicle

def getRoleMessage(role):
    if role == ROLE_TYPE.NOT_DEFINED:
        return b''
    roleLabel = ROLE_TYPE_TO_LABEL.get(role)
    msg = text_styles.concatStylesToSingleLine(getRoleIcon(roleLabel), b' ', backport.text(R.strings.menu.roleExp.roleName.dyn(roleLabel)(), groupName=backport.text(R.strings.menu.roleExp.roleGroupName.dyn(roleLabel)())))
    return makeHtmlString(b'html_templates:vehicleStatus', Vehicle.VEHICLE_STATE_LEVEL.ROLE, {b'message': msg})
