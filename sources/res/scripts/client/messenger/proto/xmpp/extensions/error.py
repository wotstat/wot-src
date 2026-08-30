from shared_utils import findFirst
from messenger.proto.xmpp.extensions import PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.gloox_constants import ERROR_TYPE
from messenger.proto.xmpp.xmpp_constants import MUC_CREATION_ERROR
STANZA_ERRORS = {b'bad-request': (ERROR_TYPE.MODIFY), 
   b'conflict': (ERROR_TYPE.CANCEL), 
   b'feature-not-implemented': (ERROR_TYPE.CANCEL), 
   b'forbidden': (ERROR_TYPE.AUTH), 
   b'gone': (ERROR_TYPE.MODIFY), 
   b'internal-server-error': (ERROR_TYPE.WAIT), 
   b'item-not-found': (ERROR_TYPE.CANCEL), 
   b'jid-malformed': (ERROR_TYPE.MODIFY), 
   b'not-acceptable': (ERROR_TYPE.MODIFY), 
   b'not-allowed': (ERROR_TYPE.CANCEL), 
   b'not-authorized': (ERROR_TYPE.AUTH), 
   b'policy-violation': (ERROR_TYPE.CANCEL), 
   b'recipient-unavailable': (ERROR_TYPE.WAIT), 
   b'redirect': (ERROR_TYPE.WAIT), 
   b'registration-required': (ERROR_TYPE.AUTH), 
   b'remote-server-not-found': (ERROR_TYPE.CANCEL), 
   b'remote-server-timeout': (ERROR_TYPE.WAIT), 
   b'resource-constraint': (ERROR_TYPE.WAIT), 
   b'service-unavailable': (ERROR_TYPE.CANCEL), 
   b'subscription-required': (ERROR_TYPE.AUTH), 
   b'undefined-condition': (ERROR_TYPE.CANCEL), 
   b'unexpected-request': (ERROR_TYPE.WAIT)}
DEF_STANZA_ERROR_CONDITION = b'undefined-condition'

class StanzaErrorExtension(PyExtension):

    def __init__(self, errorCondition=None, errorType=None):
        super(StanzaErrorExtension, self).__init__(_TAG.ERROR)
        if errorCondition:
            codeExt = PyExtension(errorCondition)
            codeExt.setXmlNs(_NS.STANZA_ERROR)
            self.setChild(codeExt)
            if not errorType:
                errorType = STANZA_ERRORS[errorCondition]
        if errorType:
            self.setAttribute(b'type', errorType)
        return

    def parseTag(self, pyGlooxTag):
        errorType = pyGlooxTag.findAttribute(b'type')
        result = pyGlooxTag.filterXPath(self.getXPath(suffix=b'.'))
        if result:
            errorCondition = result[0].getTagName()
        else:
            errorCondition = DEF_STANZA_ERROR_CONDITION
        return (errorType, errorCondition)

    @classmethod
    def getDefaultData(cls):
        return (ERROR_TYPE.CANCEL, DEF_STANZA_ERROR_CONDITION)


class WgErrorExtension(PyExtension):

    def __init__(self):
        super(WgErrorExtension, self).__init__(_TAG.ERROR)
        self.setXmlNs(_NS.WG_EXTENSION)
        return

    @classmethod
    def getDefaultData(cls):
        return MUC_CREATION_ERROR.UNDEFINED

    def parseTag(self, pyGlooxTag):
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'status')))
        code = self.getDefaultData()
        if tag is not None:
            found = tag.findAttribute(b'code')
            if found and found.isdigit():
                code = int(found)
        return code
