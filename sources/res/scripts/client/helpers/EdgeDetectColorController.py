import BigWorld, Math
from PlayerEvents import g_playerEvents
from Account import PlayerAccount
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
_DEFAULT_OVERLAY_COLOR = Math.Vector4(1, 1, 1, 1)
_OVERLAY_SOLID_KEYS = (b'overlay', b'destructible')
_OVERLAY_PATTERN_KEYS = (b'overlayForeground', b'overlay', b'destructibleForeground', b'destructible')
_OVERLAY_TARGET_INDEXES = {b'enemy': 1, b'friend': 2}
g_instance = None

class EdgeDetectColorController(object):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, dataSec):
        self.__colors = {b'common': (dict()), b'colorBlind': (dict())}
        self.__readColors(self.__colors, b'common', dataSec)
        self.__readColors(self.__colors, b'colorBlind', dataSec)
        return

    def updateColors(self):
        self.__changeColor({b'isColorBlind': (self.settingsCore.getSetting(b'isColorBlind'))})
        return

    def create(self):
        self.settingsCore.onSettingsChanged += self.__changeColor
        g_playerEvents.onAccountShowGUI += self.__onAccountShowGUI
        return

    def destroy(self):
        self.settingsCore.onSettingsChanged -= self.__changeColor
        g_playerEvents.onAccountShowGUI -= self.__onAccountShowGUI
        return

    def __readColors(self, colors, cType, section):
        cName = (b'{}/').format(cType)
        out, common = colors[cType], colors[b'common']
        out[b'self'] = section.readVector4(cName + b'self', common.get(b'self', Math.Vector4(0.2, 0.2, 0.2, 0.5)))
        out[b'enemy'] = section.readVector4(cName + b'enemy', common.get(b'enemy', Math.Vector4(1, 0, 0, 0.5)))
        out[b'friend'] = section.readVector4(cName + b'friend', common.get(b'friend', Math.Vector4(0, 1, 0, 0.5)))
        out[b'flag'] = section.readVector4(cName + b'flag', common.get(b'flag', Math.Vector4(1, 1, 1, 1)))
        out[b'hangar'] = section.readVector4(cName + b'hangar', common.get(b'hangar', Math.Vector4(1, 1, 0, 1)))
        self.__readOverlayColors(out, common, cType, b'overlaySolidColors', _OVERLAY_SOLID_KEYS, section)
        self.__readOverlayColors(out, common, cType, b'overlayPatternColors', _OVERLAY_PATTERN_KEYS, section)
        return

    def __readOverlayColors(self, out, common, cType, overlayType, keys, section):
        targets = [b'enemy', b'friend']
        common, out[overlayType] = common.get(overlayType) or {}, {}
        for target in targets:
            commonTarget, out[overlayType][target] = common.get(target) or {}, {}
            targetPath = (b'/').join([cType, overlayType, target]) + b'/'
            for key in keys:
                color = section.readVector4(targetPath + key, commonTarget.get(key, _DEFAULT_OVERLAY_COLOR))
                out[overlayType][target][key] = color

            out[overlayType][target][b'packed'] = [out[overlayType][target][key] for key in keys]

        return

    def __onAccountShowGUI(self, ctx):
        self.updateColors()
        return

    def __changeColor(self, diff):
        if b'isColorBlind' not in diff:
            return
        isHangar = isinstance(BigWorld.player(), PlayerAccount)
        cType = b'colorBlind' if diff[b'isColorBlind'] else b'common'
        colors = self.__colors[cType]
        colorsSet = (
         colors[b'hangar'] if isHangar else colors[b'self'],
         colors[b'enemy'], colors[b'friend'], colors[b'flag'])
        i = 0
        for c in colorsSet:
            BigWorld.setEdgeDetectEdgeColor(i, c)
            i += 1

        for target, idx in _OVERLAY_TARGET_INDEXES.iteritems():
            BigWorld.setEdgeDetectSolidColors(idx, *colors[b'overlaySolidColors'][target][b'packed'])
            BigWorld.setEdgeDetectPatternColors(idx, *colors[b'overlayPatternColors'][target][b'packed'])

        return
