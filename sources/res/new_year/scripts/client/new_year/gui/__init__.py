def replaceNewYearNavigation():
    from helpers import dependency
    from skeletons.gui.impl import INewYearNavigation
    from new_year.gui.impl.new_year.navigation import NewYearNavigation
    dependency.replaceInstance(INewYearNavigation, NewYearNavigation)
    return


_NY_VIGNETTE_INTENSITY = 0.6

def addNewYearVignetteSettings(personality):
    from constants_utils import addVignetteSettings
    addVignetteSettings(b'hangar', _NY_VIGNETTE_INTENSITY, personality)
    addVignetteSettings(b'heroVehiclePreviewPage', _NY_VIGNETTE_INTENSITY, personality)
    addVignetteSettings(b'vehiclePreviewPage', _NY_VIGNETTE_INTENSITY, personality)
    addVignetteSettings(b'ny_navigation', _NY_VIGNETTE_INTENSITY, personality)
    return
