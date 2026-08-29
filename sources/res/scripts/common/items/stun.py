from soft_exception import SoftException
from items import _xml
import ResMgr
_CONFIG_FILE = b'scripts/item_defs/vehicles/common/stun.xml'
g_cfg = {}

def readConfig():
    reader = ResMgr.openSection(_CONFIG_FILE)
    if reader is None:
        _xml.raiseWrongXml(None, _CONFIG_FILE, b'can not open or read')
    xmlCtx = (
     None, _CONFIG_FILE)
    c = {}
    section = reader[b'DEFAULT']
    if section is None:
        _xml.raiseWrongXml(xmlCtx, reader.name, b"'DEFAULT' subsection is missed")
    readStunType(c, xmlCtx, section)
    section = reader[b'stunTypes']
    if section is not None:
        xmlCtx = (
         xmlCtx, section.name)
        for stunType, stunData in section.items():
            readStunType(c, xmlCtx, stunData, c[b'DEFAULT'])

    return c


def readStunType(config, xmlCtx, section, default=None):
    if section.name in config:
        _xml.raiseWrongXml(xmlCtx, section.name, b'duplicate stun type name')
    xmlCtx = (xmlCtx, section.name)
    config[section.name] = stunType = {}
    stunType[b'baseStunDuration'] = _xml.readNonNegativeFloat(xmlCtx, section, b'baseStunDuration', 0 if default is None else default[b'baseStunDuration'])
    stunType[b'shellEffectFactor'] = _xml.readFraction(xmlCtx, section, b'shellEffectFactor', 0 if default is None else default[b'shellEffectFactor'])
    factors = (b'stunFactorEnginePower', b'stunFactorVehicleRotationSpeed', b'stunFactorTurretTraverse', b'stunFactorViewDistance', b'stunFactorMaxSpeed')
    for factor in factors:
        stunType[factor] = _xml.readFraction(xmlCtx, section, factor, 0.0 if default is None else default[factor])

    factors = (b'stunFactorReloadTime', b'stunFactorAimingTime', b'stunFactorVehicleMovementShotDispersion', b'stunFactorVehicleRotationShotDispersion', b'stunFactorTurretRotationShotDispersion', b'stunFactorMinShotDispersion')
    for factor in factors:
        stunType[factor] = _xml.readPositiveFloat(xmlCtx, section, factor, 1.0 if default is None else default[factor])
        _validateValue1inf(factor, stunType[factor])

    return


def init():
    global g_cfg
    g_cfg.update(readConfig())
    return


def _validateValue1inf(keyName, value):
    if value < 1:
        raise SoftException(b'invalid value for "%s": %s (it should be in range [1, +inf])' % (keyName, value))
    return
