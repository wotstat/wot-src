from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IVehicleComparisonBasket

def packHeaderColumnData(columnID, btnWidth, btnHeight, label=b'', icon=b'', tooltip=b'', direction=b'descending', showSeparator=True, textAlign=b'center', enabled=False, verticalTextAlign=b'bottom'):
    return {b'id': columnID, 
       b'label': (_ms(label)), 
       b'iconSource': icon, 
       b'buttonWidth': btnWidth, 
       b'toolTip': tooltip, 
       b'defaultSortDirection': direction, 
       b'buttonHeight': btnHeight, 
       b'showSeparator': showSeparator, 
       b'enabled': enabled, 
       b'textAlign': textAlign, 
       b'verticalTextAlign': verticalTextAlign}


def getTreeNodeCompareData(vehicle):
    comparisonBasket = dependency.instance(IVehicleComparisonBasket)
    return {b'modeAvailable': (comparisonBasket.isEnabled()), 
       b'cmpBasketFull': (not comparisonBasket.isReadyToAdd(vehicle))}


def resolveStateTooltip(comparisonBasket, vehicle, enabledTooltip, fullTooltip, invalidTooltip=VEH_COMPARE.VEHPREVIEW_COMPAREVEHICLEBTN_TOOLTIPS_CANNOTADDTOCOMPARE, miniclientTooltip=VEH_COMPARE.COMPAREVEHICLEBTN_TOOLTIPS_MINICLIENT):
    if not comparisonBasket.isAvailable():
        state, tooltip = False, miniclientTooltip
    elif comparisonBasket.isFull():
        state, tooltip = False, fullTooltip
    elif not isValidVehicleForComparing(vehicle):
        state, tooltip = False, invalidTooltip
    else:
        state, tooltip = True, enabledTooltip
    return (state, tooltip)
