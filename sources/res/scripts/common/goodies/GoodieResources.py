from typing import TYPE_CHECKING, TypeVar
from GoodieValue import GoodieValue
if TYPE_CHECKING:
    from typing import Generator

class GoodieResource(object):
    __slots__ = (b'_value',)

    def __init__(self, value):
        self._value = value
        return

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._value == other._value

    def __hash__(self):
        return hash(self._value)

    def __repr__(self):
        return (b'<{} value={}>').format(self.__class__.__name__, self._value)

    @property
    def value(self):
        return self._value

    @classmethod
    def provideCompatibleValueDescr(cls, actualVal, isPercent):
        if isPercent:
            return GoodieValue.percent(actualVal)
        return GoodieValue.absolute(actualVal)

    def iterate(self):
        yield self
        return


class Gold(GoodieResource):

    def __init__(self, value):
        super(Gold, self).__init__(value)
        return


class Credits(GoodieResource):

    def __init__(self, value):
        super(Credits, self).__init__(value)
        return


class Experience(GoodieResource):

    def __init__(self, value):
        super(Experience, self).__init__(value)
        return


class CrewExperience(GoodieResource):

    def __init__(self, value):
        super(CrewExperience, self).__init__(value)
        return


class FreeExperience(GoodieResource):

    def __init__(self, value):
        super(FreeExperience, self).__init__(value)
        return


class FrontlineExperience(GoodieResource):

    def __init__(self, value):
        super(FrontlineExperience, self).__init__(value)
        return


GoodieResourceType = TypeVar(b'GoodieResourceType', bound=GoodieResource)
