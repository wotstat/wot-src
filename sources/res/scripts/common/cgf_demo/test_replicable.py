import CGF, Math
from Event import Event
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerReplicableComponent

@registerReplicableComponent
class TestReplicableComponent(object):
    category = DEMO_CATEGORY
    editorTitle = b'Test Replication Types'
    replicableInt = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'IntValue', value=777)
    replicableFloat = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Float Value', value=10.0)
    replicableString = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'States', value=b'Test String')
    replicableVector3 = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName=b'States', value=Math.Vector3(1.0, 2.0, 3.0))
    replicableStringList = ComponentProperty(type=CGFMetaTypes.STRING_LIST, editorName=b'States', value=(b'one', b'two', b'three'))
    assetIndex = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Default asset', value=0)
    assets = ComponentProperty(type=CGFMetaTypes.STRING_LIST, editorName=b'Models')

    def __init__(self):
        self.onReplicated = Event()
        return

    def set_replicableInt(self, old):
        self.onReplicated(old, self.replicableInt)
        return

    def set_replicableFloat(self, old):
        self.onReplicated(old, self.replicableFloat)
        return

    def set_replicableString(self, old):
        self.onReplicated(old, self.replicableFloat)
        return

    def set_replicableVector3(self, old):
        self.onReplicated(old, self.replicableFloat)
        return

    def set_replicableStringList(self, old):
        self.onReplicated(old, self.replicableFloat)
        return
