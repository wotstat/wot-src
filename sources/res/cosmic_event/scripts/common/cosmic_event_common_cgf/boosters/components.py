import CGF, Math, Triggers
from collections import deque
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent, registerReplicableComponent

@registerComponent
class BoosterActivationComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Cosmic'
    editorTitle = b'Booster activation component'
    turnOnTime = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Turn on periods', value=b'')
    turnOffTime = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Turn off periods', value=b'')

    def __init__(self):
        self.turnOnPeriodsLeft = deque()
        self.turnOffPeriodsLeft = deque()
        return

    def destroy(self):
        self.turnOnPeriodsLeft = None
        self.turnOffPeriodsLeft = None
        return


@registerComponent
class ImpulseComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Cosmic'
    editorTitle = b'Impulse'
    impulseDirection = ComponentProperty(type=CGFMetaTypes.VECTOR3, value=Math.Vector3(1, 0, 0), editorName=b'Impulse direction')
    massCoef = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Mass coefficient', value=1)
    velocityLimit = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Velocity limit', value=200.0)
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'AreaTrigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionID = None
        self.exitReactionID = None
        return


@registerComponent
class BoosterTypeComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Cosmic'
    editorTitle = b'Booster type'
    type = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Type', value=b'', annotations={b'comboBox': {b'board': b'board', 
                     b'geyser': b'geyser'}})


@registerReplicableComponent
class BoosterComponent(object):
    category = b'Cosmic'
    editorTitle = b'Booster replicable component'
