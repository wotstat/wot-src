from collections import namedtuple, defaultdict
HintProps = namedtuple(b'HintProps', (b'uniqueID', b'hintID', b'itemID', b'text', b'hasBox', b'arrow', b'padding', b'updateRuntime', b'hideImmediately', b'checkViewArea'))

class HintsData(object):

    def __init__(self):
        super(HintsData, self).__init__()
        self.__guiFilePath = None
        self.__hints = defaultdict(list)
        return

    def getHints(self):
        return self.__hints

    def getHintsCount(self):
        return sum(len(hintsList) for hintsList in self.__hints.itervalues())

    def setGuiFilePath(self, filePath):
        self.__guiFilePath = filePath
        return

    def getGuiFilePath(self):
        return self.__guiFilePath

    def addHint(self, hint):
        self.__hints[hint[b'itemID']].append(hint)
        return

    def hintsForItem(self, itemID):
        if itemID in self.__hints:
            return self.__hints[itemID]
        return ()

    def markAsShown(self, itemID, hintID):
        if itemID in self.__hints:
            hintsList = self.__hints[itemID]
            self._delHints(hintsList, (hintID,))
        return

    def markHintsAsShown(self, hintIDs):
        for hintsList in self.__hints.itervalues():
            self._delHints(hintsList, hintIDs)

        return

    @staticmethod
    def _delHints(hintsList, ids):
        for idx, hint in reversed(list(enumerate(hintsList))):
            if hint[b'hintID'] in ids:
                del hintsList[idx]

        return
