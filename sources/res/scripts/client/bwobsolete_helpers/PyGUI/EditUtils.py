import BigWorld, GUI, Math, ResMgr

def setup():
    BigWorld.camera(BigWorld.CursorCamera())
    BigWorld.setCursor(GUI.mcursor())
    GUI.mcursor().visible = True
    return


def clearAll():
    while len(GUI.roots()):
        GUI.delRoot(GUI.roots()[0])

    return


def clone(component):
    ResMgr.purge(b'gui/temp_clone.gui', True)
    component.save(b'gui/temp_clone.gui')
    return GUI.load(b'gui/temp_clone.gui')


weatherWindow = None

def weather():
    global weatherWindow
    setup()
    weatherWindow = GUI.load(b'gui/weather_window.gui')
    GUI.addRoot(weatherWindow)
    return weatherWindow


def saveWeather():
    if weatherWindow:
        weatherWindow.save(b'gui/weather_window.gui')
    return
