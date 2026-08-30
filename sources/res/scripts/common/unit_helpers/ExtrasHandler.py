from __future__ import absolute_import
from future.moves import pickle

class EmptyExtrasHandler(object):

    def __init__(self, unit):
        return

    def new(self, initial=None):
        result = {}
        if initial:
            result.update(initial)
        return result

    def pack(self, extras):
        return b''

    def unpack(self, extrasStr):
        return {}

    def reset(self, extras):
        return self.new()

    def updateUnitExtras(self, extras, updateStr):
        return


class SimpleExtrasHandler(EmptyExtrasHandler):

    def pack(self, extras):
        return pickle.dumps(extras, -1)

    def unpack(self, extrasStr):
        return pickle.loads(extrasStr)

    def reset(self, extras):
        return extras

    def updateUnitExtras(self, extras, updateStr):
        update = pickle.loads(updateStr)
        extras.update(update)
        return


class ClanBattleExtrasHandler(SimpleExtrasHandler):

    def __init__(self, unit=None):
        super(ClanBattleExtrasHandler, self).__init__(unit)
        self._unit = unit
        from unit_helpers.MsgProcessor import ClanBattleMgrMsgProcessor
        self._processor = ClanBattleMgrMsgProcessor(unit)
        return

    def new(self, initial=None):
        result = {b'battleID': 0, 
           b'scheduleTime': 0, 
           b'roundStart': 0, 
           b'battleResultList': [], b'isEnemyReadyForBattle': 0, 
           b'clanEquipments': None, 
           b'lastEquipRev': 0, 
           b'localizedData': None}
        if initial:
            result.update(initial)
        return result

    def updateUnitExtras(self, extras, updateStr):
        self._processor.unpackOps(updateStr)
        return


class SquadExtrasHandler(SimpleExtrasHandler):
    pass


class ExternalExtrasHandler(SimpleExtrasHandler):

    def new(self, initial=None):
        result = {b'rev': 1}
        if initial:
            result.update(initial)
        return result
