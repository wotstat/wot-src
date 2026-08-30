from __future__ import absolute_import
import os
from collections import OrderedDict
import typing
from future.utils import lmap
import ResMgr
from items import _xml
from items.components import perks_constants
from items.components.perks_components import Perk, PerkArgument
from items.components.perks_constants import PerkTags

def _readPerkArguments(xmlCtx, section):
    argsDict = OrderedDict()
    argsSection = _xml.getSubsection(xmlCtx, section, b'defaultBlockSettings', throwIfMissing=False)
    if argsSection:
        for _, argSection in argsSection.items():
            argId = _xml.readString(xmlCtx, argSection, b'argId')
            value = argSection.readFloat(b'value', 0.0)
            postValues = lmap(float, _xml.readStringOrEmpty(xmlCtx, argSection, b'postValues').split())
            argsDict[argId] = PerkArgument(value, postValues)

    return argsDict


def _readPerkItem(xmlCtx, section, storage):
    perkID = _xml.readInt(xmlCtx, section, b'id', 1)
    flags = PerkTags.pack(_xml.readStringOrEmpty(xmlCtx, section, b'tags').split())
    args = _readPerkArguments(xmlCtx, section)
    storage[perkID] = Perk(perkID, flags, args)
    return


def _readPerksCacheFromXMLSection(xmlCtx, section, sectionName, storage):
    if sectionName not in PERKS_READERS:
        _xml.raiseWrongXml(xmlCtx, sectionName, b'unknown section')
    reader = PERKS_READERS[sectionName]
    for gname, gsection in section.items():
        if gname != sectionName:
            continue
        reader(xmlCtx, gsection, storage)

    return


PERKS_READERS = {b'perk': _readPerkItem}

def readPerksCacheFromXML(cache, folder):
    xmlCtx = (
     None, perks_constants.PERKS_XML_FILE)
    pgFile = os.path.join(folder, perks_constants.PERKS_XML_FILE)
    _readPerksCacheFromXMLSection(xmlCtx, ResMgr.openSection(pgFile), b'perk', cache)
    ResMgr.purge(pgFile)
    return
