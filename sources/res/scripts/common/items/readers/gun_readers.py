from __future__ import absolute_import
from typing import TYPE_CHECKING, Tuple, Optional
import ResMgr
from items import _xml
from items.components import component_constants
from items.components import gun_components
from items.components.component_constants import ZERO_FLOAT
from items.components.shell_components import Stun
from items.stun import g_cfg as stunConfig
from items.readers import shared_readers
from items.readers.shared_readers import readFloatPair
from constants import IS_EDITOR, IS_UE_EDITOR, IS_CLIENT, IS_WEB
from math_common import ceilTo
if TYPE_CHECKING:
    from items.vehicles import Cache

def readRecoilEffect(xmlCtx, section, cache):
    if not section.has_key(b'recoil'):
        return
    else:
        effName = _xml.readStringOrNone(xmlCtx, section, b'recoil/recoilEffect')
        if effName is not None:
            recoilEff = cache.getGunRecoilEffects(effName)
            if recoilEff is not None:
                backoffTime = recoilEff[0]
                returnTime = recoilEff[1]
            else:
                backoffTime = component_constants.ZERO_FLOAT
                returnTime = component_constants.ZERO_FLOAT
        else:
            backoffTime = _xml.readNonNegativeFloat(xmlCtx, section, b'recoil/backoffTime')
            returnTime = _xml.readNonNegativeFloat(xmlCtx, section, b'recoil/returnTime')
        recoil = gun_components.RecoilEffect(lodDist=shared_readers.readLodDist(xmlCtx, section, b'recoil/lodDist', cache), amplitude=_xml.readNonNegativeFloat(xmlCtx, section, b'recoil/amplitude'), backoffTime=backoffTime, returnTime=returnTime)
        if IS_EDITOR:
            recoil.effectName = effName
        return recoil


def readShot(xmlCtx, section, nationID, projectileSpeedFactor, cache):
    shellName = section.name
    shellID = cache.shellIDs(nationID).get(shellName)
    if shellID is None:
        _xml.raiseWrongXml(xmlCtx, b'', b'unknown shell type name')
    shellDescr = cache.shells(nationID)[shellID]
    defaultPortion = ZERO_FLOAT
    if section.has_key(b'defaultPortion'):
        defaultPortion = _xml.readFraction(xmlCtx, section, b'defaultPortion')
    if IS_CLIENT or IS_WEB:
        defaultPortion = ceilTo(defaultPortion, decimals=-3, epsilon=1e-06)
    shot = gun_components.GunShot(shellDescr, defaultPortion, readFloatPair(xmlCtx, section, b'piercingPower'), _xml.readPositiveFloat(xmlCtx, section, b'speed') * projectileSpeedFactor, _xml.readNonNegativeFloat(xmlCtx, section, b'gravity') * projectileSpeedFactor ** 2, _xml.readPositiveFloat(xmlCtx, section, b'maxDistance'), _xml.readFloat(xmlCtx, section, b'maxHeight', 1000000.0))
    if not IS_UE_EDITOR:
        from helpers_common import computeShotMaxDistance
        shot.maxDistance = computeShotMaxDistance(shot)
    return shot


def readStunParams(section, xmlCtx=None, useDefaults=False):
    if not section.readBool(b'hasStun', False):
        return {}
    stunParams = {}
    if section.has_key(b'stunRadius'):
        stunParams[b'stunRadius'] = _xml.readPositiveFloat(xmlCtx, section, b'stunRadius')
    if section.has_key(b'stunDuration'):
        stunParams[b'stunDuration'] = _xml.readPositiveFloat(xmlCtx, section, b'stunDuration')
    elif useDefaults:
        stunParams[b'stunDuration'] = stunConfig.get(b'baseStunDuration', 30)
    if section.has_key(b'stunFactor'):
        stunFactor = _xml.readPositiveFloat(xmlCtx, section, b'stunFactor')
        if stunFactor > 1:
            _xml.raiseWrongXml(xmlCtx, b'stunFactor', b'stun factor cannot exceed 1')
        stunParams[b'stunFactor'] = stunFactor
    elif useDefaults:
        stunParams[b'stunFactor'] = 1.0
    if section.has_key(b'guaranteedStunDuration'):
        stunParams[b'guaranteedStunDuration'] = _xml.readFraction(xmlCtx, section, b'guaranteedStunDuration')
    elif useDefaults:
        stunParams[b'guaranteedStunDuration'] = stunConfig[b'guaranteedStunDuration']
    if section.has_key(b'damageDurationCoeff'):
        stunParams[b'damageDurationCoeff'] = _xml.readFraction(xmlCtx, section, b'damageDurationCoeff')
    elif useDefaults:
        stunParams[b'damageDurationCoeff'] = stunConfig[b'damageDurationCoeff']
    if section.has_key(b'guaranteedStunEffect'):
        stunParams[b'guaranteedStunEffect'] = _xml.readFraction(xmlCtx, section, b'guaranteedStunEffect')
    elif useDefaults:
        stunParams[b'guaranteedStunEffect'] = stunConfig[b'guaranteedStunEffect']
    if section.has_key(b'damageEffectCoeff'):
        stunParams[b'damageEffectCoeff'] = _xml.readFraction(xmlCtx, section, b'damageEffectCoeff')
    elif useDefaults:
        stunParams[b'damageEffectCoeff'] = stunConfig[b'damageEffectCoeff']
    for key in stunParams:
        pass

    return stunParams
