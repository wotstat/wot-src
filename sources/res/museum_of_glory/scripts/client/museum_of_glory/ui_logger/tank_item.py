class TankItem(list):
    _ITEM_COUNT = 2

    def __init__(self):
        super(TankItem, self).__init__([0] * TankItem._ITEM_COUNT)
        return

    def updateVoiceoverTime(self, value):
        self[0] = max(value, self[0])
        return

    def increaseClickCount(self):
        self[1] += 1
        return
