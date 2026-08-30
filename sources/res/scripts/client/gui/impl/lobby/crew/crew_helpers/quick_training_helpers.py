import typing
if typing.TYPE_CHECKING:
    from typing import Dict

class UiData(object):
    __slots__ = (b'_freeXP', b'_booksData', b'_preSelectedBook', b'_preSelectedFreeXp')

    def __init__(self):
        self._freeXP = 0
        self._booksData = {}
        self._preSelectedBook = 0
        self._preSelectedFreeXp = 0
        return

    def addBook(self, bookCD):
        self._booksData[bookCD] = 0
        return

    def updateBooks(self, bookCD, count):
        self._booksData.update({bookCD: count})
        return

    def isBookSelected(self):
        return any(count for count in self._booksData.itervalues())

    def isSomeSelected(self):
        return self.isBookSelected() or self.freeXp

    def clearPreSelected(self):
        self._preSelectedBook = 0
        self._preSelectedFreeXp = 0
        return

    def clear(self):
        self._freeXP = 0
        for bookCD in self._booksData.iterkeys():
            self._booksData[bookCD] = 0

        self.clearPreSelected()
        return

    def getBooksData(self):
        return self._booksData

    @property
    def freeXp(self):
        return self._freeXP

    @freeXp.setter
    def freeXp(self, value):
        self._freeXP = value
        return

    @property
    def preSelectedBook(self):
        return self._preSelectedBook

    @preSelectedBook.setter
    def preSelectedBook(self, value):
        self._preSelectedFreeXp = 0
        self._preSelectedBook = value
        return

    @property
    def preSelectedFreeXp(self):
        return self._preSelectedFreeXp

    @preSelectedFreeXp.setter
    def preSelectedFreeXp(self, value):
        self._preSelectedBook = 0
        self._preSelectedFreeXp = value
        return

    def __repr__(self):
        return (b'freeXP: {}, books: {}').format(self._freeXP, self._booksData)
