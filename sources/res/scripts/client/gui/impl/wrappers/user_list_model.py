from __future__ import absolute_import
import typing, logging, Event
from WeakMethod import WeakMethodProxy
from gui.impl.gen.view_models.ui_kit.list_model import ListModel
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
_logger = logging.getLogger(__name__)
T = typing.TypeVar(b'T')

class UserListModel(ListModel[T]):
    __slots__ = (b'onUserSelectionChanged', b'onUserItemClicked')

    def __init__(self):
        super(UserListModel, self).__init__()
        self.onUserSelectionChanged = Event.Event()
        self.onUserItemClicked = Event.Event()
        return

    def addNumber(self, value, isSelected=False):
        self.getItems().addNumber(value)
        if isSelected:
            self.addSelectedIndex(self.getItemsLength() - 1)
        return

    def addReal(self, value, isSelected=False):
        self.getItems().addReal(value)
        if isSelected:
            self.addSelectedIndex(self.getItemsLength() - 1)
        return

    def addBool(self, value, isSelected=False):
        self.getItems().addBool(value)
        if isSelected:
            self.addSelectedIndex(self.getItemsLength() - 1)
        return

    def addString(self, value, isSelected=False):
        self.getItems().addString(value)
        if isSelected:
            self.addSelectedIndex(self.getItemsLength() - 1)
        return

    def addViewModel(self, value, isSelected=False):
        self.getItems().addViewModel(value)
        if isSelected:
            self.addSelectedIndex(self.getItemsLength() - 1)
        return

    def addArray(self, value, isSelected=False):
        self.getItems().addArray(value)
        if isSelected:
            self.addSelectedIndex(self.getItemsLength() - 1)
        return

    def getItem(self, index):
        try:
            return self.getItems()[index]
        except IndexError:
            _logger.error(b'Index %d is out of range', index)
            return

        return

    def findItems(self, predicate):
        return [item for item in self.getItems() if predicate(item)]

    def findIndexes(self, predicate):
        return [idx for idx, item in enumerate(self.getItems()) if predicate(item)]

    def clearItems(self):
        self.getItems().clear()
        return

    def getItemsLength(self):
        return len(self.getItems())

    def getSelectedItem(self):
        selectedItemsIndices = self.getSelectedIndices()
        if selectedItemsIndices:
            return self.getItem(selectedItemsIndices[0])
        else:
            return

    def getSelectedItems(self):
        result = []
        selectedItemsIndices = self.getSelectedIndices()
        for index in selectedItemsIndices:
            result.append(self.getItem(index))

        return result

    def addSelectedIndex(self, index):
        self.getSelectedIndices().addNumber(index)
        return

    def removeItemByIndex(self, index):
        self.getItems().remove(index)
        return

    def removeItemByIndexes(self, indexes):
        self.getItems().removeValues(indexes)
        return

    def removeSelectedIndexes(self):
        selectedItems = self.getSelectedIndices()
        if selectedItems:
            self.removeItemByIndexes(selectedItems)
        else:
            _logger.error(b'There are no selected items in list')
        return

    def invalidate(self):
        self.getItems().invalidate()
        return

    def reserve(self, capacity):
        self.getItems().reserve(capacity)
        return

    def _initialize(self):
        super(UserListModel, self)._initialize()
        self.onSelectionChanged += WeakMethodProxy(self.__onSelectionChanged)
        self.onItemClicked += WeakMethodProxy(self.__onItemClicked)
        return

    def __onSelectionChanged(self, args=None):
        if b'selectedIndex' not in args or b'unselectedIndex' not in args:
            _logger.error(b'%r: Arguments "selectedIndex" or "unselectedIndex" is not defined in %r', self, args)
        index = args[b'selectedIndex']
        if index is not None and index >= 0:
            item = self.getItem(index)
            if item is not None:
                self.onUserSelectionChanged(item)
        return

    def __onItemClicked(self, args=None):
        if b'index' not in args:
            _logger.error(b'%r: Argument "index" is not defined in %r', self, args)
            return
        else:
            item = self.getItem(args[b'index'])
            if item is not None:
                self.onUserItemClicked(item)
            return
