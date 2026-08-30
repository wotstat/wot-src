import ResMgr
from items import _xml
from debug_utils_bootcamp import LOG_ERROR_BOOTCAMP
from BootcampContext import AreaMarker

def _parseID(xmlCtx, section, msg):
    entityID = section.asString
    if not entityID:
        _xml.raiseWrongXml(xmlCtx, section.name, msg)
    return entityID


def _readModelMarkerSection(xmlCtx, section, name=b'model'):
    result = {}
    if name in section.keys():
        subSec = _xml.getSubsection(xmlCtx, section, name)
        result = {b'path': (_xml.readString(xmlCtx, subSec, b'path')), 
           b'action': (_xml.readString(xmlCtx, subSec, b'action')), 
           b'offset': (_xml.readVector3(xmlCtx, subSec, b'offset'))}
    return result


def _readWorldMarkerSection(xmlCtx, section):
    subSec = _xml.getSubsection(xmlCtx, section, b'world')
    return {b'shape': (_xml.readString(xmlCtx, subSec, b'shape')), 
       b'min-distance': (_xml.readFloat(xmlCtx, subSec, b'min-distance')), 
       b'max-distance': (_xml.readFloat(xmlCtx, subSec, b'max-distance')), 
       b'offset': (_xml.readVector3(xmlCtx, subSec, b'offset'))}


def _readAreaMarkerSection(xmlCtx, section, markerID):
    return AreaMarker(markerID, _readModelMarkerSection(xmlCtx, section), _readModelMarkerSection(xmlCtx, section, name=b'ground'), _readWorldMarkerSection(xmlCtx, section), createInd=section.readBool(b'create-indicator', True))


_MARKER_TYPES = {b'Area': _readAreaMarkerSection}

def _readMarkerSection(xmlCtx, section, _):
    markerID = _parseID(xmlCtx, section, b'Specify a marker ID')
    type = _xml.readString(xmlCtx, section, b'type')
    marker = None
    if type in _MARKER_TYPES:
        parser = _MARKER_TYPES[type]
        marker = parser(xmlCtx, section, markerID)
    else:
        LOG_ERROR_BOOTCAMP(b'Marker is not supported:', type)
    return marker


_BASE_ENTITY_PARSERS = {b'marker': _readMarkerSection}
_ENTITY_PARSERS = _BASE_ENTITY_PARSERS.copy()

def _parseEntity(xmlCtx, name, section, flags):
    parser = _ENTITY_PARSERS.get(name)
    item = None
    if parser is not None:
        item = parser(xmlCtx, section, flags)
    else:
        LOG_ERROR_BOOTCAMP(b'Entity is not supported:', name)
    return item


class BootcampParser(object):

    @staticmethod
    def parse(chapter):
        filePath = chapter.getFilePath()
        section = ResMgr.openSection(filePath)
        if section is None:
            _xml.raiseWrongXml(None, filePath, b'can not open or read')
        xmlCtx = (
         None, filePath)
        flags = []
        BootcampParser._parseEntities(xmlCtx, section, flags, chapter)
        _xml.clearCaches()
        return

    @staticmethod
    def _parseEntities(xmlCtx, section, flags, chapter):
        for name, subSec in _xml.getChildren(xmlCtx, section, b'has-id'):
            entity = _parseEntity(xmlCtx, name, subSec, flags)
            if entity is not None:
                chapter.addEntity(entity)

        return
