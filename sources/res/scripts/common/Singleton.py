from __future__ import absolute_import, print_function

class Singleton(object):

    def __new__(cls, *args, **kwargs):
        singleton_instance = cls.__dict__.get(b'__instance__')
        if singleton_instance is not None:
            return singleton_instance
        else:
            cls.__instance__ = singleton_instance = object.__new__(cls)
            singleton_instance._singleton_init(*args, **kwargs)
            return singleton_instance

    def _singleton_init(self, *args, **kwargs):
        return


if __name__ == b'__main__':

    class MySingleton(Singleton):

        def _singleton_init(self, instanceName):
            self.instanceName = instanceName
            return


    ins1 = MySingleton(b'instance1')
    print(id(ins1), ins1.instanceName)
    ins2 = MySingleton(b'instance2')
    print(id(ins2), ins2.instanceName)
