from gui.shared.events import HasCtxEvent

class DynamicFactorsEvent(HasCtxEvent):
    UPDATE_LEVEL = b'dynamicFactors/updateLevel'


class WTCrosshairVisibilityEvents(HasCtxEvent):
    SHOW_CROSSHAIR = b'WTCrosshairVisibility/showCrossHair'
