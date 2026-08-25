from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class MinimapClientModel(BaseClientModel):
    __slots__ = (b'showGrid', b'minimumAnimationDuration', b'maximumAnimationDuration', b'animationDurationPerMeter', b'minimumAnimationDistance', b'canToggleFullMap')

    def __init__(self, showGrid, canToggleFullMap, minimumAnimationDuration, maximumAnimationDuration, animationDurationPerMeter, minimumAnimationDistance):
        super(MinimapClientModel, self).__init__()
        self.showGrid = showGrid
        self.canToggleFullMap = canToggleFullMap
        self.minimumAnimationDuration = minimumAnimationDuration
        self.maximumAnimationDuration = maximumAnimationDuration
        self.animationDurationPerMeter = animationDurationPerMeter
        self.minimumAnimationDistance = minimumAnimationDistance
        return

    def __repr__(self):
        return (b'<MinimapClientModel>: showGrid=%s, minimumAnimationDuration=%s, maximumAnimationDuration=%s, ' + b'animationDurationPerMeter=%s, minimumAnimationDistance=%s, canToggleFullMap=%s') % (
         self.showGrid,
         self.minimumAnimationDuration,
         self.maximumAnimationDuration,
         self.animationDurationPerMeter,
         self.minimumAnimationDistance,
         self.canToggleFullMap)
