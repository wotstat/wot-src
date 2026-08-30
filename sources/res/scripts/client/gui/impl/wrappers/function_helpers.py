from __future__ import absolute_import
from functools import wraps

def replaceNoneKwargsModel(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        actual = kwargs.get(b'model')
        if actual is None:
            with self.getViewModel().transaction() as model:
                kwargs[b'model'] = model
                return func(self, *args, **kwargs)
        else:
            return func(self, *args, **kwargs)
        return

    return wrapper
