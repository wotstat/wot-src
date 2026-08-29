class VehicleComponentDispatcher(object):

    def __init__(self):
        self._registry = {}
        return

    def register(self, name, onAbsent=None, onPresent=None):
        entry = {b'absent': onAbsent, b'present': onPresent}
        self._registry[name] = entry
        return

    def unregister(self):
        self._registry.clear()
        return

    def dispatch(self, vehicle, componentName, *args, **kwargs):
        handlers = self._registry.get(componentName)
        if handlers is None:
            return
        else:
            component = vehicle.dynamicComponents.get(componentName)
            if component is None:
                handlers[b'absent'](vehicle, *args, **kwargs)
            else:
                handlers[b'present'](vehicle, component, *args, **kwargs)
            return
