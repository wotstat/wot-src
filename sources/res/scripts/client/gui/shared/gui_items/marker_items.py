from __future__ import absolute_import
import Math, copy, ResMgr
from extension_utils import importClass
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask as FLAG, COMPONENT_MARKER_TYPE_NAMES
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers import MarkerBase
from soft_exception import SoftException
DEFAULT_MARKER = b'DEFAULT'
_COMPONENT_MARKERS_CONFIG = b'gui/component_marker_items.xml'

class MarkerParamsFactory(object):
    MARKER_DATA = {}

    @classmethod
    def readConfigs(cls, path=_COMPONENT_MARKERS_CONFIG):
        _xml = ResMgr.openSection(path)
        if not _xml:
            return
        for markerItemName, section in _xml.items():
            markerItemName = markerItemName.upper()
            if markerItemName in cls.MARKER_DATA:
                raise SoftException(b'Duplicated marker type: (%s) in xml config' % markerItemName)
            cls.MARKER_DATA[markerItemName] = cls._readParams(section)

        ResMgr.purge(path)
        return

    @classmethod
    def getMarkerParams(cls, matrix, markerStyle=DEFAULT_MARKER, bitMask=FLAG.NONE):
        params = copy.deepcopy(cls.MARKER_DATA.get(markerStyle, {}))
        if bitMask == FLAG.NONE:
            bitMask = MarkerParamsFactory.buildBitMask(params)
        offset = params.get(b'offset', (0, 0, 0))
        mp = Math.MatrixProduct()
        mp.a = matrix
        mp.b = Math.Matrix()
        mp.b.translation = offset
        params.update({b'matrixProduct': mp, b'bitMask': bitMask})
        return params

    @classmethod
    def buildBitMask(cls, params):
        bitMask = FLAG.NONE
        for key in params:
            if key in FLAG.LIST:
                bitMask |= key

        return bitMask

    @classmethod
    def _readParams(cls, section):
        config = {b'visible': (section.readBool(b'visible', True)), 
           b'areaRadius': (section.readFloat(b'areaRadius', 0.0)), 
           b'disappearingRadius': (section.readFloat(b'disappearingRadius', 0.0)), 
           b'reverseDisappearing': (section.readBool(b'reverseDisappearing', False)), 
           b'offset': (section.readVector3(b'offset', (0, 0, 0)))}
        config = cls._readComponents(config, section[b'components'])
        return config

    @classmethod
    def _readComponents(cls, config, section):
        for componentTypeName, componentSection in section.items():
            componentType = COMPONENT_MARKER_TYPE_NAMES.get(componentTypeName)
            if componentTypeName is None:
                raise SoftException(b'Unknown marker component type: (%s)' % componentTypeName)
            config[componentType] = cls._readComponent(componentSection, componentType)

        return config

    @classmethod
    def _readComponent(cls, section, componentType):
        items = []
        for item in section.values():
            classPath = item.readString(b'class')
            if classPath:
                clazz = importClass(classPath, b'')
            else:
                clazz = MarkerBase.COMPONENT_CLASS[componentType]
            if clazz is None:
                raise SoftException(b'Class is None')
            config = clazz.configReader(item[b'config']) if item.has_key(b'config') else {}
            config.update({b'clazz': clazz})
            items.append(config)

        return items


def init():
    MarkerParamsFactory.readConfigs()
    return
