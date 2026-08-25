from __future__ import absolute_import
import logging, CGF
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.registration import ComponentProperty, registerComponent
_logger = logging.getLogger(__name__)

@registerComponent
class ClientTestComponent(object):
    group = DEMO_CATEGORY
    editorTitle = b'Client Test'
    domain = CGF.Domain.ClientEditor
    stringList = ComponentProperty(type=CGF.PropertyType.StringList, editorName=b'String List', value=(b'Test1', b'Test2'))
    intList = ComponentProperty(type=CGF.PropertyType.IntList, editorName=b'Int List', value=(1, 2, 3))
    floatList = ComponentProperty(type=CGF.PropertyType.FloatList, editorName=b'Float List', value=(4.0, 5.0, 6.0, 7.0))
    double = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Double', value=55.0)
    integer = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Integer', value=777)
    string = ComponentProperty(type=CGF.PropertyType.String, editorName=b'String', value=b'Tiger')
    transformLink = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Link to Transform', value=CGF.TransformComponent)


class ClientTestSystem(CGF.System):
    ClientTestCreated = CGF.CreateReaction(CGF.ReactRw(ClientTestComponent))
    TransformAccess = CGF.AccessReaction(CGF.Ro(CGF.TransformComponent))
    Reactions = CGF.Reactions(ClientTestCreated, TransformAccess)

    def update(self):
        transformAccess = self.reaction(self.TransformAccess)
        for clientTest in self.reaction(self.ClientTestCreated):
            _logger.debug(b'ClientTestComponent stringList = %s', clientTest.stringList)
            _logger.debug(b'ClientTestComponent double = %f', clientTest.double)
            _logger.debug(b'ClientTestComponent integer = %d', clientTest.integer)
            _logger.debug(b'ClientTestComponent string = %s', clientTest.string)
            if clientTest.transformLink:
                transform = transformAccess.find(clientTest.transformLink)
                _logger.debug(b'ClientTestComponent transform from link =\n%s', transform.worldTransform)

        return
