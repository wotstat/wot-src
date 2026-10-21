import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
factorComponentClasses = {}

class FactorRegisterMeta(type):

    def __init__(cls, name, bases, attrs):
        super(FactorRegisterMeta, cls).__init__(name, bases, attrs)
        if attrs.get(b'_skipFactorComponentRegistry'):
            return
        factorComponentClasses[cls.__name__] = cls
        return


class BuffComponent(object):
    __metaclass__ = FactorRegisterMeta
    _skipFactorComponentRegistry = True
    factorName = None


@registerComponent
class PeriodicHealthChangeComponent(BuffComponent):
    domain = CGF.DomainOption.DomainAll
    category = b'Events Core'
    editorTitle = b'Periodic Health Change'
    factorName = b'buffs/periodicHealthChange'
    healthChange = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Health Change', value=1.0)

    def __init__(self):
        super(PeriodicHealthChangeComponent, self).__init__()
        self.attackerVehicleID = None
        self.attackerInfo = None
        return


@registerComponent
class MovementBlockedComponent(BuffComponent):
    domain = CGF.DomainOption.DomainAll
    category = b'Events Core'
    editorTitle = b'Movement Blocked'
    factorName = b'buffs/movementBlocked'


class BaseFactorComponent(BuffComponent):
    domain = CGF.DomainOption.DomainAll
    category = b'Vehicle Factors'
    editorTitle = b'Base Factor Component'
    factorName = b'baseFactor'
    factorValue = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Factor Value', value=1.0)


def createFactorComponentClass(className, factorName, factorType=CGFMetaTypes.FLOAT, factorValue=1.0):
    classAttrs = {b'editorTitle': className, 
       b'factorName': factorName, 
       b'factorValue': (ComponentProperty(type=factorType, editorName=b'Factor Value', value=factorValue))}
    return FactorRegisterMeta(className, (BaseFactorComponent,), classAttrs)


factorsComponents = {b'engine/power': b'EnginePowerFactorComponent', 
   b'gun/piercing': b'GunPiercingComponent', 
   b'gun/reloadTime': b'GunReloadTimeComponent', 
   b'gun/rotationSpeed': b'GunRotationSpeedComponent', 
   b'gun/aimingTime': b'GunAimingTimeComponent', 
   b'turret/rotationSpeed': b'TurretRotationSpeedComponent', 
   b'vehicle/maxSpeed': b'VehicleMaxSpeedComponent'}
for factorName, className in factorsComponents.iteritems():
    componentClass = createFactorComponentClass(className, factorName)
    registerComponent(componentClass)

vehicleBuffsComponents = dict(factorsComponents)
vehicleBuffsComponents.update({(PeriodicHealthChangeComponent.factorName): (PeriodicHealthChangeComponent.__name__), 
   (MovementBlockedComponent.factorName): (MovementBlockedComponent.__name__)})
