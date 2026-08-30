from gui.game_loading.resources.consts import Milestones
from gui.game_loading.resources.models import StatusTextModel
from gui.game_loading.state_machine.const import ContentState

class ImageViewSettingsModel(object):
    __slots__ = (b'showVfx', b'contentState', b'ageRatingPath', b'info', b'hasVignette')

    def __init__(self, showVfx=True, contentState=ContentState.INVISIBLE, ageRatingPath=b'', info=b'', hasVignette=True):
        self.showVfx = showVfx
        self.contentState = contentState
        self.ageRatingPath = ageRatingPath
        self.info = info
        self.hasVignette = hasVignette
        return

    def __repr__(self):
        return (b'<ImageViewSettingsModel(vfx={}, contentState={}, ageRatingPath={}, info={})>').format(self.showVfx, self.contentState, self.ageRatingPath, self.info)


class ProgressSettingsModel(object):
    __slots__ = (b'startPercent', b'limitPercent', b'ticksInProgress', b'minTickTimeSec')

    def __init__(self, startPercent, limitPercent, ticksInProgress, minTickTimeSec):
        self.startPercent = startPercent
        self.limitPercent = limitPercent
        self.ticksInProgress = ticksInProgress
        self.minTickTimeSec = minTickTimeSec
        return

    def __repr__(self):
        return (b'<ProgressBarSettingsModel(start={}, limit={}, ticks={}, minTickTimeSec={})>').format(self.startPercent, self.limitPercent, self.ticksInProgress, self.minTickTimeSec)


class LoadingMilestoneModel(object):
    __slots__ = (b'name', b'percent', b'forceApply', b'status')

    def __init__(self, name, percent, forceApply, status):
        self.name = name
        self.percent = percent
        self.forceApply = forceApply
        self.status = status
        return

    def __repr__(self):
        return (b'<LoadingMilestoneModel(name={}, percent={}, forceApply={}, status={}>').format(self.name, self.percent, self.forceApply, self.status)
