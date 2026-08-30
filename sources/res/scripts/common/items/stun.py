from __future__ import absolute_import
import ResMgr
from soft_exception import SoftException
from items import _xml
_CONFIG_FILE = b'scripts/item_defs/vehicles/common/stun.xml'
g_cfg = {}

def readConfig():
    section = ResMgr.openSection(_CONFIG_FILE)
    if section is None:
        _xml.raiseWrongXml(None, _CONFIG_FILE, b'can not open or read')
    xmlCtx = (
     None, _CONFIG_FILE)
    c = {}
    c[b'baseStunDuration'] = _xml.readNonNegativeFloat(xmlCtx, section, b'baseStunDuration')
    c[b'guaranteedStunDuration'] = _xml.readFraction(xmlCtx, section, b'guaranteedStunDuration')
    c[b'damageDurationCoeff'] = _xml.readFraction(xmlCtx, section, b'damageDurationCoeff')
    c[b'guaranteedStunEffect'] = _xml.readFraction(xmlCtx, section, b'guaranteedStunEffect')
    c[b'damageEffectCoeff'] = _xml.readFraction(xmlCtx, section, b'damageEffectCoeff')
    c[b'minStunDuration'] = _xml.readNonNegativeFloat(xmlCtx, section, b'minStunDuration')
    c[b'shellEffectFactor'] = _xml.readFraction(xmlCtx, section, b'shellEffectFactor')
    c[b'stunFactorEnginePower'] = _xml.readFraction(xmlCtx, section, b'stunFactorEnginePower')
    c[b'stunFactorVehicleRotationSpeed'] = _xml.readFraction(xmlCtx, section, b'stunFactorVehicleRotationSpeed')
    c[b'stunFactorTurretTraverse'] = _xml.readFraction(xmlCtx, section, b'stunFactorTurretTraverse')
    c[b'stunFactorViewDistance'] = _xml.readFraction(xmlCtx, section, b'stunFactorViewDistance')
    c[b'stunFactorMaxSpeed'] = _xml.readFraction(xmlCtx, section, b'stunFactorMaxSpeed')
    c[b'stunFactorReloadTime'] = _xml.readPositiveFloat(xmlCtx, section, b'stunFactorReloadTime', 1.0)
    _validateValue1inf(b'stunFactorReloadTime', c[b'stunFactorReloadTime'])
    c[b'stunFactorAimingTime'] = _xml.readPositiveFloat(xmlCtx, section, b'stunFactorAimingTime', 1.0)
    _validateValue1inf(b'stunFactorAimingTime', c[b'stunFactorAimingTime'])
    c[b'stunFactorVehicleMovementShotDispersion'] = _xml.readPositiveFloat(xmlCtx, section, b'stunFactorVehicleMovementShotDispersion', 1.0)
    _validateValue1inf(b'stunFactorVehicleMovementShotDispersion', c[b'stunFactorVehicleMovementShotDispersion'])
    c[b'stunFactorVehicleRotationShotDispersion'] = _xml.readPositiveFloat(xmlCtx, section, b'stunFactorVehicleRotationShotDispersion', 1.0)
    _validateValue1inf(b'stunFactorVehicleRotationShotDispersion', c[b'stunFactorVehicleRotationShotDispersion'])
    c[b'stunFactorTurretRotationShotDispersion'] = _xml.readPositiveFloat(xmlCtx, section, b'stunFactorTurretRotationShotDispersion', 1.0)
    _validateValue1inf(b'stunFactorTurretRotationShotDispersion', c[b'stunFactorTurretRotationShotDispersion'])
    c[b'stunFactorMinShotDispersion'] = _xml.readPositiveFloat(xmlCtx, section, b'stunFactorMinShotDispersion', 1.0)
    _validateValue1inf(b'stunFactorMinShotDispersion', c[b'stunFactorMinShotDispersion'])
    return c


def init():
    global g_cfg
    g_cfg.update(readConfig())
    return


def _validateValue1inf(keyName, value):
    if value < 1:
        raise SoftException(b'invalid value for "%s": %s (it should be in range [1, +inf])' % (keyName, value))
    return
