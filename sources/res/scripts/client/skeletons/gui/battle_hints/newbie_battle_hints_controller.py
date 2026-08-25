from __future__ import absolute_import
import typing

class INewbieBattleHintsController(object):

    def fini(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isUserSettingEnabled(self):
        raise NotImplementedError
        return

    def getDisplayCount(self, uniqueName):
        raise NotImplementedError
        return

    def resetHistory(self):
        raise NotImplementedError
        return
