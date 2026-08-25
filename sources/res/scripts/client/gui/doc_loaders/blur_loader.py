from __future__ import absolute_import
import ResMgr
from items import _xml
XML_PATH = b'gui/blur_settings.xml'

def readBlurSettings(xmlConfigPath=XML_PATH):
    rootSection = ResMgr.openSection(xmlConfigPath)
    if rootSection is None:
        _xml.raiseWrongXml(None, xmlConfigPath, b'invalid blur XML config')
    settings = {viewName: {param: reader(viewSection[param]) for param, reader in _PARAMS.items() if param in viewSection.keys()} for viewName, viewSection in rootSection.items()}
    defaults = settings.pop(b'_defaults')
    defaultKeys = set(defaults)
    for viewSettings in settings.values():
        missingParams = defaultKeys - set(viewSettings)
        viewSettings.update({p: defaults[p] for p in missingParams})

    return settings


def _readAlphaParams(section):
    return {p: section.readFloat(p) for p in (b'center', b'start', b'end')}


def _readDirection(section):
    return {p: section.readBool(p) for p in (b'top', b'right', b'bottom', b'left')}


def _readParams(section):
    return {p: section.readInt(p) for p in (b'hstart', b'hend', b'vstart', b'vend')}


def _readHorizontalParams(section):
    return {p: section.readInt(p) for p in (b'leftStart', b'leftEnd', b'rightStart', b'rightEnd')}


def _readVerticalParams(section):
    return {p: section.readInt(p) for p in (b'topStart', b'topEnd', b'bottomStart', b'bottomEnd')}


def _readHorizontalAlphas(section):
    return {p: section.readFloat(p) for p in (b'leftStart', b'leftEnd', b'rightStart', b'rightEnd')}


def _readVerticalAlphas(section):
    return {p: section.readFloat(p) for p in (b'topStart', b'topEnd', b'bottomStart', b'bottomEnd')}


def _readType(section):
    return {b'regular': 0, 
       b'radial': 1, 
       b'spinning': 2}[section.asWideString]


_PARAMS = {b'type': _readType, 
   b'dispatches': (lambda section: section.asInt), 
   b'applienceType': (lambda section: section.asInt), 
   b'applienceRadius': (lambda section: section.asInt), 
   b'intensity': (lambda section: section.asInt), 
   b'center': (lambda section: section.asVector2), 
   b'mipsCount': (lambda section: section.asInt), 
   b'alphaParams': _readAlphaParams, 
   b'direction': _readDirection, 
   b'params': _readParams, 
   b'horizontalParams': _readHorizontalParams, 
   b'verticalParams': _readVerticalParams, 
   b'horizontalAlphas': _readHorizontalAlphas, 
   b'verticalAlphas': _readVerticalAlphas}
