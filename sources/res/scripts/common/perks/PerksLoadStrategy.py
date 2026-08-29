from perks.vse_plan import VsePlan, PlanStatus
from th_async import th_async, th_await, distributeLoopOverTicks

class LoadType:
    DEFAULT = 0
    AUTO_START = 1
    DELAYED_LOAD_START = 2


class LoadState:
    DEFAULT = 0
    PRE_LOAD = 1
    LOAD = 2
    PRE_START = 3
    START = 4
    STATUS_LOADED = (
     LOAD, PRE_START, START)


class BaseLoadStrategy(object):

    def __init__(self, plans, scope, owner, onPlanReady):
        self._plans = plans
        self._scope = scope
        self._owner = owner
        self._state = None
        self._onPlansReady = onPlanReady
        self._setState(LoadState.DEFAULT)
        return

    def load(self):
        return

    def start(self):
        return

    def beforeBattleStart(self):
        return

    @property
    def state(self):
        return self._state

    def _setState(self, value):
        if self._state != value:
            self._state = value
            self._stateLogic()
        return

    def _stateLogic(self):
        if self._state == LoadState.START:
            self._onReady()
        return

    def _onStatusChanged(self):
        return

    def _checkIsAllPlansReady(self):
        return all(plan.isPlanStarted for plan in self._plans)

    def _checkIsAllPlansLoaded(self):
        return all(plan.status == PlanStatus.LOAD for plan in self._plans)

    def _clearPlansCallback(self):
        for plan in self._plans:
            plan._clearCallBack()

        return

    def _onReady(self):
        self._clearPlansCallback()
        self._plans = []
        self._scope = []
        self._setState(LoadState.DEFAULT)
        self._onPlansReady()
        return


class DefaultLoadStrategy(BaseLoadStrategy):

    def load(self):
        self._setState(LoadState.PRE_LOAD)
        return

    def start(self):
        if self._state == LoadState.PRE_LOAD:
            self._setState(LoadState.PRE_START)
        return

    @th_async
    def loadPlansAsync(self, isAutoStart=False):
        _MAX_LOAD_PLANS = 10
        tempCreator = []
        for scopeId, (scope, creator) in self._scope.iteritems():
            for perkId, (level, args) in scope:
                plan = VsePlan(self._owner, scopeId, level, perkId, self._onStatusChanged, args)
                self._plans.append(plan)
                tempCreator.append(creator)

        def asyncLoop():
            for idx, item in enumerate(self._plans):
                yield item.load(tempCreator[idx], isAutoStart)

            return

        yield th_await(distributeLoopOverTicks(asyncLoop(), maxPerTick=_MAX_LOAD_PLANS, logID=b'loadPlans'))
        return

    @th_async
    def _startAsync(self):

        def asyncLoop():
            for plan in self._plans:
                yield plan.start()

            return

        yield th_await(distributeLoopOverTicks(asyncLoop(), maxPerTick=1, logID=b'start'))
        return

    def _onStatusChanged(self):
        if self._state == LoadState.PRE_START:
            if self._checkIsAllPlansReady():
                self._setState(LoadState.START)
        return

    def _stateLogic(self):
        if self._state == LoadState.PRE_LOAD:
            self.loadPlansAsync()
            return
        if self._state == LoadState.PRE_START:
            self._onPlansReady()
            self._startAsync()
            return
        super(DefaultLoadStrategy, self)._stateLogic()
        return


class AutoStartStrategy(DefaultLoadStrategy):

    def start(self):
        return

    def load(self):
        self._setState(LoadState.PRE_LOAD)
        return

    def _stateLogic(self):
        if self._state == LoadState.PRE_LOAD:
            self.loadPlansAsync(True)
            return
        super(AutoStartStrategy, self)._stateLogic()
        return

    def _onStatusChanged(self):
        if self._state == LoadState.PRE_LOAD:
            if self._checkIsAllPlansReady():
                self._setState(LoadState.START)
        return


class DelayLoadStartStrategy(DefaultLoadStrategy):

    def __init__(self, plans, scope, owner, onPlanReady):
        self._isStarted = False
        super(DelayLoadStartStrategy, self).__init__(plans, scope, owner, onPlanReady)
        return

    def load(self):
        return

    def start(self):
        return

    def beforeBattleStart(self):
        if self._isStarted:
            return
        if self._state == LoadState.DEFAULT:
            self._setState(LoadState.PRE_LOAD)
        return

    def _onStatusChanged(self):
        if self._state == LoadState.PRE_LOAD:
            if self._checkIsAllPlansLoaded():
                self._setState(LoadState.PRE_START)
                return
        if self._state == LoadState.PRE_START:
            if self._checkIsAllPlansReady():
                self._setState(LoadState.START)
        return

    def _stateLogic(self):
        if self._state == LoadState.PRE_LOAD:
            self._isStarted = True
            self.loadPlansAsync()
            return
        super(DelayLoadStartStrategy, self)._stateLogic()
        return


BUILDER = {(LoadType.DEFAULT): DefaultLoadStrategy, 
   (LoadType.AUTO_START): AutoStartStrategy, 
   (LoadType.DELAYED_LOAD_START): DelayLoadStartStrategy}

def getLoadStarategy(value):
    return BUILDER.get(value)
