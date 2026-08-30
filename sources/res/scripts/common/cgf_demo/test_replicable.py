from __future__ import absolute_import
import Math, CGF
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.registration import ComponentProperty

class TestReplicableComponentDescriptor(object):
    category = DEMO_CATEGORY
    editorTitle = b'Test Replication Types'
    replicableInt = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'IntValue', value=777)
    replicableFloat = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Float Value', value=10.0)
    replicableString = ComponentProperty(type=CGF.PropertyType.String, editorName=b'States', value=b'Test String')
    replicableVector3 = ComponentProperty(type=CGF.PropertyType.Vector3, editorName=b'States', value=Math.Vector3(1.0, 2.0, 3.0))
    replicableStringList = ComponentProperty(type=CGF.PropertyType.StringList, editorName=b'States', value=(b'one', b'two', b'three'))
    assetIndex = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Default asset', value=0)
    assets = ComponentProperty(type=CGF.PropertyType.StringList, editorName=b'Models')
