import logging, GenericComponents, CGF
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
_logger = logging.getLogger(__name__)

@registerComponent
class ClientTestComponent(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    stringList = ComponentProperty(type=CGFMetaTypes.STRING_LIST, editorName=b'String List', value=(b'Test1', b'Test2'))
    intList = ComponentProperty(type=CGFMetaTypes.INT_LIST, editorName=b'Int List', value=(1, 2, 3))
    floatList = ComponentProperty(type=CGFMetaTypes.FLOAT_LIST, editorName=b'Float List', value=(4.0, 5.0, 6.0, 7.0))
    double = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Double', value=55.0)
    integer = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Integer', value=777)
    string = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'String', value=b'Tiger')
    transformLink = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Link to Transform', value=GenericComponents.TransformComponent)

    def __init__(self):
        super(ClientTestComponent, self).__init__()
        _logger.debug(b'ClientTestComponent stringList = %s', self.stringList)
        _logger.debug(b'ClientTestComponent double = %f', self.double)
        _logger.debug(b'ClientTestComponent integer = %d', self.integer)
        _logger.debug(b'ClientTestComponent string = %s', self.string)
        if self.transformLink is not None:
            _logger.debug(b'ClientTestComponent transform from link =\n%s', self.transformLink().worldTransform)
        return
