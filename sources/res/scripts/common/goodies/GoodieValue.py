from soft_exception import SoftException
from math import floor

class GoodieValue(object):
    __slots__ = [
     b'value', b'isAbsolute']

    def __init__(self, value, isAbsolute=True):
        self.isAbsolute = isAbsolute
        if isAbsolute:
            self.value = int(value)
        elif value < 0:
            raise SoftException(b'Bad goodie value <%s>' % value)
        self.value = float(value) / 100
        return

    def __lt__(self, other):
        if self.isAbsolute == other.isAbsolute:
            return self.value < other.value
        raise SoftException(b'Comparison of absolute and percent values')
        return

    def __gt__(self, other):
        if self.isAbsolute == other.isAbsolute:
            return self.value > other.value
        raise SoftException(b'Comparison of absolute and percent values')
        return

    def __eq__(self, other):
        if self.isAbsolute == other.isAbsolute:
            return self.value == other.value
        raise SoftException(b'Comparison of absolute and percent values')
        return

    @staticmethod
    def percent(value):
        return GoodieValue(value, False)

    @staticmethod
    def absolute(value):
        return GoodieValue(value, True)

    def increase(self, x):
        if self.isAbsolute:
            return int(x) + self.value
        else:
            return int(floor(x + float(x) * self.value))

        return

    def reduce(self, x):
        if self.isAbsolute:
            result = int(x) - self.value
            if result < 0:
                raise SoftException(b'Goodie is negative %d > %d' % (self.value, x))
            return result
        return int(floor(x - float(x) * self.value))
        return

    def delta(self, x):
        if self.isAbsolute:
            return self.value
        else:
            return int(round(float(x) * self.value))

        return
