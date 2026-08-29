import BigWorld
__all__ = (b'regionDecorator', b'enterToRegion', b'exitFromRegion')

def _isRegionSupported():
    if not hasattr(BigWorld, b'uniprofRegionEnter'):
        return False
    if not hasattr(BigWorld, b'uniprofRegionExit'):
        return False
    return True


_IS_REGION_SUPPORTED = _isRegionSupported()
if _IS_REGION_SUPPORTED:
    from .regions import regionDecorator
    from .regions import enterToRegion, exitFromRegion
else:

    class _DummyDecorator(object):
        __slots__ = ()

        def __call__(self, func):
            return func


    def enterToRegion(*_):
        return


    def exitFromRegion(*_):
        return


    def regionDecorator(*_, **__):
        return _DummyDecorator()
