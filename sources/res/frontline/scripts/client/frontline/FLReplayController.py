import BattleReplay

class FLReplayController:

    def __init__(self):
        return

    @staticmethod
    def setDataCallback(eventName, callback):
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.setDataCallback(eventName, callback)
        return

    @staticmethod
    def delDataCallback(eventName, callback):
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.delDataCallback(eventName, callback)
        return

    @staticmethod
    def serializeCallbackData(eventName, data):
        BattleReplay.g_replayCtrl.serializeCallbackData(eventName, data)
        return
