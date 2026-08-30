import typing
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.shared.gui_items.crew_book import CrewBook
COUNT_KEY = b'count'
IS_PERSONAL_KEY = b'isPersonal'

class QuickTrainingSelectionData(object):
    __slots__ = (b'_freeXP', b'_selectedBooks', b'_preSelectedFreeXp', b'_aquiringCommonXp', b'_aquiringPersonalXp', b'_preSelectedCommonXp', b'_preSelectedPersonalXp', b'_preSelectedBookId')

    def __init__(self):
        self._freeXP = 0
        self._selectedBooks = {}
        self._preSelectedFreeXp = 0
        self._aquiringCommonXp = 0
        self._aquiringPersonalXp = 0
        self._preSelectedCommonXp = 0
        self._preSelectedPersonalXp = 0
        self._preSelectedBookId = None
        return

    @property
    def books(self):
        return self._selectedBooks

    @property
    def freeXp(self):
        return self._freeXP

    @freeXp.setter
    def freeXp(self, value):
        self._freeXP = value
        self._preSelectedFreeXp = 0
        return

    @property
    def preSelectedFreeXp(self):
        return self._preSelectedFreeXp

    @property
    def hasAnyBook(self):
        return len(self._selectedBooks) > 0

    @property
    def hasPersonalBook(self):
        for selectionData in self._selectedBooks.values():
            if selectionData[IS_PERSONAL_KEY]:
                return True

        return False

    @property
    def hasCommonBook(self):
        for selectionData in self._selectedBooks.values():
            if not selectionData[IS_PERSONAL_KEY]:
                return True

        return False

    def isBookPreSelecteed(self, bookId):
        return self._preSelectedBookId is not None and self._preSelectedBookId == bookId

    def getAcquiringBooksXpValues(self):
        return (
         self._aquiringPersonalXp, self._aquiringCommonXp)

    def getAllAquiringBooksXpValue(self):
        return (
         self._preSelectedPersonalXp + self._aquiringPersonalXp,
         self._preSelectedCommonXp + self._aquiringCommonXp)

    def getPersonalBookId(self):
        for bookId, selectionData in self._selectedBooks.items():
            if selectionData[IS_PERSONAL_KEY]:
                return bookId

        return

    def setBook(self, book, count):
        previousCount = self._selectedBooks.get(book.intCD, {}).get(COUNT_KEY, 0)
        if book.intCD not in self._selectedBooks and count > 0:
            self.clearPreSelected()
            self._selectedBooks[book.intCD] = {COUNT_KEY: count, IS_PERSONAL_KEY: (book.isPersonal())}
        elif count == 0:
            self._selectedBooks.pop(book.intCD)
        else:
            self._selectedBooks[book.intCD][COUNT_KEY] = count
        if book.isPersonal():
            self._aquiringPersonalXp += (count - previousCount) * book.getXP()
        else:
            self._aquiringCommonXp += (count - previousCount) * book.getXP()
        return

    def setFreeXpFromPreSelected(self):
        self._freeXP = self._preSelectedFreeXp
        self._preSelectedFreeXp = 0
        return

    def setPreSelectedFreeXp(self, freeXp):
        self._preSelectedFreeXp = freeXp
        self._preSelectedCommonXp = 0
        self._preSelectedPersonalXp = 0
        self._preSelectedBookId = None
        return

    def setPreSelectedBook(self, book):
        self._preSelectedFreeXp = 0
        self._preSelectedBookId = book.intCD
        if book.isPersonal():
            self._preSelectedPersonalXp = book.getXP()
            self._preSelectedCommonXp = 0
        else:
            self._preSelectedCommonXp = book.getXP()
            self._preSelectedPersonalXp = 0
        return

    def getBookCountById(self, bookId):
        if bookId not in self._selectedBooks:
            return 0
        return self._selectedBooks[bookId][COUNT_KEY]

    def clear(self):
        self._freeXP = 0
        self._selectedBooks = {}
        self._aquiringCommonXp = 0
        self._aquiringPersonalXp = 0
        self.clearPreSelected()
        return

    def clearPreSelected(self):
        self._preSelectedFreeXp = 0
        self._preSelectedCommonXp = 0
        self._preSelectedPersonalXp = 0
        self._preSelectedBookId = None
        return
