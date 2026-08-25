from __future__ import absolute_import
from future.utils import lmap, viewitems

class Config(object):

    def __init__(self, **kwargs):
        lmap((lambda item: setattr(self, *item)), viewitems(kwargs))
        return

    @classmethod
    def create(cls, *args, **kwargs):
        raise NotImplementedError
        return
