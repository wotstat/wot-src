import Math, copy
from constants import MarkerItem
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask as FLAG
from gui.Scaleform.daapi.view.battle.shared.minimap.settings import CONTAINER_NAME, ENTRY_SYMBOL_NAME
from gui.Scaleform.daapi.view.battle.shared.component_marker import markers_components
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.battle.shared.indicators import _DIRECT_INDICATOR_SWF, _DIRECT_INDICATOR_MC_NAME
from gui.Scaleform.daapi.view.battle.shared.markers2d import settings

class MarkerParamsFactory(object):
    ZONE_MARKER_DEFAULT_COLOR_SETTINGS = {b'default': {b'fillColor': 16729670, 
                    b'fillAlpha': 0.25, 
                    b'fillBlendMode': (markers_components.PolygonalZoneMinimapMarkerComponent.Blending.NORMAL), 
                    b'outlineColor': 16740967, 
                    b'outlineAlpha': 0.45, 
                    b'outlineBlendMode': (markers_components.PolygonalZoneMinimapMarkerComponent.Blending.NORMAL), 
                    b'lineThickness': 3.0}, 
       b'colorBlind': {b'fillColor': 6840319, 
                       b'fillAlpha': 0.4, 
                       b'fillBlendMode': (markers_components.PolygonalZoneMinimapMarkerComponent.Blending.NORMAL), 
                       b'outlineColor': 11644159, 
                       b'outlineAlpha': 0.6, 
                       b'outlineBlendMode': (markers_components.PolygonalZoneMinimapMarkerComponent.Blending.NORMAL), 
                       b'lineThickness': 3.0}}
    MARKER_DATA = {(MarkerItem.DEFAULT): {b'visible': True, 
                              b'areaRadius': 5.0, 
                              b'disappearingRadius': 0.0, 
                              b'reverseDisappearing': False, 
                              b'offset': (0, 10, 0), 
                              (FLAG.MARKER_2D): [
                                               {b'shape': b'arrow', 
                                                  b'min-distance': 0.0, 
                                                  b'max-distance': 0.0, 
                                                  b'distance': 0.0, 
                                                  b'distanceFieldColor': b'white', 
                                                  b'symbol': (settings.MARKER_SYMBOL_NAME.STATIC_OBJECT_MARKER)}], 
                              (FLAG.DIRECTION_INDICATOR): [
                                                         {b'dIndicatorShapes': (b'green', b'green'), 
                                                            b'swf': _DIRECT_INDICATOR_SWF, 
                                                            b'mcName': _DIRECT_INDICATOR_MC_NAME}], 
                              (FLAG.MINIMAP_MARKER): [
                                                    {b'symbol': (ENTRY_SYMBOL_NAME.ARTY_MARKER), 
                                                       b'container': (CONTAINER_NAME.PERSONAL), 
                                                       b'onlyTranslation': False},
                                                    {b'symbol': (ENTRY_SYMBOL_NAME.BOMBER_ENTRY), 
                                                       b'container': (CONTAINER_NAME.EQUIPMENTS), 
                                                       b'onlyTranslation': True}], 
                              (FLAG.ANIM_SEQUENCE_MARKER): [
                                                          {b'path': b'content/Interface/Arrow/animations/bootcamp_arrow.seq'}], 
                              (FLAG.TERRAIN_MARKER): [
                                                    {b'path': b'content/Interface/TargetPoint/TargetPoint_red.visual', 
                                                       b'size': (50.0, 20.0), 
                                                       b'direction': (1.0, 0.0, 0.0), 
                                                       b'objDirection': True, 
                                                       b'color': 4294967295L}]}, 
       (MarkerItem.STATIC_DEATH_ZONE_PROXIMITY): {b'visible': True, 
                                                  b'areaRadius': 0.0, 
                                                  b'disappearingRadius': 50.0, 
                                                  b'reverseDisappearing': True, 
                                                  b'offset': (0, 10, 0), 
                                                  (FLAG.MARKER_2D): [
                                                                   {b'shape': b'deathZone', 
                                                                      b'min-distance': 0.0, 
                                                                      b'max-distance': 0.0, 
                                                                      b'distance': 0.0, 
                                                                      b'distanceFieldColor': b'orange', 
                                                                      b'metersString': (b' ' + backport.text(R.strings.ingame_gui.marker.meters()))}]}, 
       (MarkerItem.COMP7_RECON): {(FLAG.MINIMAP_MARKER): [
                                                        {b'symbol': (ENTRY_SYMBOL_NAME.COMP7_RECON), 
                                                           b'container': (CONTAINER_NAME.EQUIPMENTS)}]}, 
       (MarkerItem.POLYGONAL_ZONE): {b'visible': True, 
                                     (FLAG.MINIMAP_MARKER): [
                                                           {b'symbol': b'CustomDeathZoneMinimapEntryUI', 
                                                              b'container': (CONTAINER_NAME.FLAGS), 
                                                              b'clazz': (markers_components.PolygonalZoneMinimapMarkerComponent), 
                                                              b'color': ZONE_MARKER_DEFAULT_COLOR_SETTINGS}]}, 
       (MarkerItem.STATIC_DEATH_ZONE): {b'visible': True, 
                                        (FLAG.MINIMAP_MARKER): [
                                                              {b'symbol': b'CustomDeathZoneMinimapEntryUI', 
                                                                 b'container': (CONTAINER_NAME.FLAGS), 
                                                                 b'clazz': (markers_components.StaticDeathZoneMinimapMarkerComponent), 
                                                                 b'color': ZONE_MARKER_DEFAULT_COLOR_SETTINGS}]}}

    @classmethod
    def getMarkerParams(cls, matrix, markerStyle=MarkerItem.DEFAULT, bitMask=FLAG.NONE):
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
        for key in params.iterkeys():
            if key in FLAG.LIST:
                bitMask |= key

        return bitMask
