from helpers import dependency
from helpers.events_handler import EventsHandler
from skeletons.gui.game_control import IComp7Controller
from web.client_web_api.api import C2WHandler, c2w

class Comp7BattleResultEventHandler(C2WHandler, EventsHandler):
    __comp7Ctrl = dependency.descriptor(IComp7Controller)

    def init(self):
        super(Comp7BattleResultEventHandler, self).init()
        self._subscribe()
        return

    def fini(self):
        self._unsubscribe()
        super(Comp7BattleResultEventHandler, self).fini()
        return

    def _getEvents(self):
        return (
         (
          self.__comp7Ctrl.onComp7BattleFinished, self.__sendInfo),
         (
          self.__comp7Ctrl.onStatusUpdated, self.__sendStatusInfo),
         (
          self.__comp7Ctrl.onComp7ConfigChanged, self.__sendStatusInfo),
         (
          self.__comp7Ctrl.onComp7RanksConfigChanged, self.__sendStatusInfo))

    @c2w(name=b'comp7_battle_result')
    def __sendInfo(self, *args, **kwargs):
        return b'Comp7BattleFinished'

    @c2w(name=b'comp7_status_updated')
    def __sendStatusInfo(self, *args, **kwargs):
        return b'Comp7StatusUpdated'
