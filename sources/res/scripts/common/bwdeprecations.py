from __future__ import absolute_import
import functools, warnings, BigWorld

def deprecatedAlias(method, oldname):

    def warnAndCallWrapper(*args, **kwargs):
        warnings.warn(b'%s.%s is deprecated, use %s.%s instead' % (
         method.__module__, oldname, method.__module__, method.__name__), DeprecationWarning, 2)
        return method(*args, **kwargs)

    return functools.wraps(method)(warnAndCallWrapper)


def addDeprecatedAliasOf(module, newname, oldname):
    if not hasattr(module, newname):
        return
    if hasattr(module, oldname):
        return
    method = getattr(module, newname)
    setattr(module, oldname, deprecatedAlias(method, oldname))
    return


if BigWorld.component == b'client':
    addDeprecatedAliasOf(BigWorld, b'serverTime', b'stime')
addDeprecatedAliasOf(BigWorld, b'ThirdPersonTargetingMatrix', b'ThirdPersonTargettingMatrix')
addDeprecatedAliasOf(BigWorld, b'MouseTargetingMatrix', b'MouseTargettingMatrix')
if BigWorld.component == b'client':
    if not hasattr(BigWorld, b'cachedEntities'):
        BigWorld.cachedEntities = {}
    if not hasattr(BigWorld, b'allEntities'):
        BigWorld.allEntities = BigWorld.entities
if BigWorld.component == b'cell':
    import OldSpaceData
