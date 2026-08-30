from extension_utils import importClass
from items import _xml
from constants import IS_CLIENT, IS_EDITOR, IS_BOT
import collections

def readExtras(xmlCtx, section, subsectionName, defaultModName, **kwargs):
    NoneExtra = importClass(b'NoneExtra', defaultModName)
    noneExtra = NoneExtra(b'_NoneExtra', 0, b'', None)
    extras = [
     noneExtra]
    extrasDict = {(noneExtra.name): noneExtra}
    for extraName, extraSection in _xml.getChildren(xmlCtx, section, subsectionName):
        ctx = (xmlCtx, subsectionName + b'/' + extraName)
        if extrasDict.has_key(extraName):
            _xml.raiseWrongXml(ctx, b'', b'name is not unique')
        clientName, _, serverName = extraSection.asString.partition(b':')
        classPath = (clientName if IS_CLIENT or IS_EDITOR or IS_BOT else serverName).strip()
        classObj = importClass(classPath, defaultModName)
        if classObj is not None:
            classExtras = classObj(extraName, len(extras), xmlCtx[1], extraSection, **kwargs)
            if isinstance(classExtras, collections.Iterable):
                for extra in classExtras:
                    extrasDict[extra.name] = extra

                extras.extend(classExtras)
            else:
                extras.append(classExtras)
                extrasDict[extraName] = classExtras
        else:
            _xml.raiseWrongXml(ctx, b'', b"Can't import %s" % classPath)

    if len(extras) > 200:
        _xml.raiseWrongXml(xmlCtx, subsectionName, b'too many extras')
    return (tuple(extras), extrasDict)
