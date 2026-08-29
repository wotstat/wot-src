import CGF
from GenericComponents import TransformComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, autoregister
from CameraComponents import CameraComponent

@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class ArenaCameraManager(CGF.ComponentManager):

    def __init__(self, *args):
        super(ArenaCameraManager, self).__init__(*args)
        self.__cameras = dict()
        return

    def getCameraTransform(self, name):
        return self.__cameras.get(name)

    @onAddedQuery(CameraComponent, TransformComponent, tickGroup=b'preInitGroup')
    def onCameraAdded(self, cameraComponent, transformComponent):
        self.__cameras[cameraComponent.name] = transformComponent.worldTransform
        return

    @onRemovedQuery(CameraComponent, tickGroup=b'preInitGroup')
    def onCameraRemoved(self, cameraComponent):
        self.__cameras.pop(cameraComponent.name)
        return
