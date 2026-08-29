import weakref
_languageChangeListeners = []
_deviceListeners = []

def registerInputLangChangeListener(listener):
    global _languageChangeListeners
    _languageChangeListeners.append(weakref.ref(listener))
    return


def registerDeviceListener(listener):
    _deviceListeners.append(weakref.ref(listener))
    return


def handleInputLangChangeEvent():
    import GUI
    for listener in [x() for x in _languageChangeListeners if x() is not None]:
        if hasattr(listener, b'handleInputLangChangeEvent'):
            listener.handleInputLangChangeEvent()

    return True


def onRecreateDevice():
    for listener in [x() for x in _deviceListeners if x() is not None]:
        if hasattr(listener, b'onRecreateDevice'):
            listener.onRecreateDevice()

    return
