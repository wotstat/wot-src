class IGeneratorMarker(object):

    def onGeneratorCapture(self, generatorIndex, progress, timeLeft, numInvaders):
        return

    def onGeneratorStopCapture(self, generatorIndex):
        return

    def onGeneratorLocked(self, generatorID, isLocked):
        return
