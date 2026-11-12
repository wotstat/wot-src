import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

class BuffComponent(object):
    pass


@registerComponent
class PeriodicHealthChangeComponent(BuffComponent):
    domain = CGF.DomainOption.DomainAll
    category = b'Events Core'
    editorTitle = b'Periodic Health Change'
    healthChange = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Health Change', value=1.0)


@registerComponent
class MovementBlockedComponent(BuffComponent):
    domain = CGF.DomainOption.DomainAll
    category = b'Events Core'
    editorTitle = b'Movement Blocked'


factorComponentClasses = {}

class FactorRegisterMeta(type):

    def __init__(cls, name, bases, attrs):
        super(FactorRegisterMeta, cls).__init__(name, bases, attrs)
        factorComponentClasses[cls.__name__] = cls
        return


class BaseFactorComponent(BuffComponent):
    __metaclass__ = FactorRegisterMeta
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


components = [
 (b'EnginePowerFactorComponent', b'engine/power')]
for componentArgs in components:
    componentClass = createFactorComponentClass(*componentArgs)
    registerComponent(componentClass)
