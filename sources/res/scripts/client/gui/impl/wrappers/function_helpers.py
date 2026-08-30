import functools

def replaceNoneKwargsModel(func):

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if b'model' not in kwargs:
            actual = None
        else:
            actual = kwargs[b'model']
        if actual is None:
            with self.getViewModel().transaction() as model:
                kwargs[b'model'] = model
                return func(self, *args, **kwargs)
        else:
            return func(self, *args, **kwargs)
        return

    return wrapper
