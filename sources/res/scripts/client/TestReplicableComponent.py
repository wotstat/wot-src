import BigWorld, CGF, GenericComponents, GameplayDebug, cgf_demo.test_replicable
from cgf_script.managers_registrator import onAddedQuery, onProcessQuery

class TestReplicableComponent(BigWorld.DynamicScriptComponent, cgf_demo.test_replicable.TestReplicableComponent):
    pass


class DisplayReplicableValuesManager(CGF.ComponentManager):

    def __init__(self):
        super(DisplayReplicableValuesManager, self).__init__()
        self.totalReplicationCount = 0
        return

    @onAddedQuery(TestReplicableComponent, CGF.GameObject)
    def onAddedType(self, r, go):
        r.onReplicated += self.__onReplicationDone
        go.removeComponentByType(GenericComponents.DynamicModelComponent)
        if r.assetIndex < len(r.assets):
            go.createComponent(GenericComponents.DynamicModelComponent, r.assets[r.assetIndex])
        return

    @onProcessQuery(TestReplicableComponent, GameplayDebug.DebugTextComponent)
    def displayValues(self, r, text):
        text.addFrameText((b'Total Replication Count: {0}').format(self.totalReplicationCount))
        text.addFrameText((b'int: {0}').format(r.replicableInt))
        text.addFrameText((b'float: {0}').format(r.replicableFloat))
        text.addFrameText((b'Vector3: {0}').format(r.replicableVector3))
        text.addFrameText(r.replicableString)
        text.addFrameText((b'List: {0}').format(r.replicableStringList))
        return

    def __onReplicationDone(self, prev, new):
        self.totalReplicationCount += 1
        return
