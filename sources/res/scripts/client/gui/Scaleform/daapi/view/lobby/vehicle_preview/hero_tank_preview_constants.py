from collections import namedtuple
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IHeroTankController
_VehicleData = namedtuple(b'_SpecialParamsVehicle', (b'name', b'styleID'))
_OFFSPRING_VEHICLE = _VehicleData(name=b'usa:A127_TL_1_LPC', styleID=83)
_PreviewParams = namedtuple(b'_PreviewParams', (b'buyButtonLabel', b'enterEvent', b'exitEvent'))
_SPECIAL_PREVIEW_PARAMS = {_OFFSPRING_VEHICLE: (_PreviewParams(buyButtonLabel=R.strings.vehicle_preview.buyingPanel.buyBtn.label.offspring(), enterEvent=b'ev_fest_off_hero_tank_in', exitEvent=b'ev_fest_off_hero_tank_out'))}

@dependency.replace_none_kwargs(heroTanksControl=IHeroTankController)
def getHeroTankPreviewParams(heroTanksControl=None):
    vName = heroTanksControl.getCurrentVehicleName()
    vStyleId = heroTanksControl.getCurrentTankStyleId()
    vData = _VehicleData(vName, vStyleId)
    return _SPECIAL_PREVIEW_PARAMS.get(vData)
