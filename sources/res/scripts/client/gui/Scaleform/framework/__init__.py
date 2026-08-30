from __future__ import absolute_import
from collections import namedtuple
from frameworks.wulf import WindowLayer
import gui.Scaleform.framework.ScopeTemplates
from gui.Scaleform.framework.factories import EntitiesFactories, DAAPIModuleFactory, ViewFactory
from gui.Scaleform.framework.settings import UIFrameworkImpl

def getSwfExtensionUrl(extension, swf):
    return extension + b'|' + swf


class COMMON_VIEW_ALIAS(object):
    LOGIN = b'login'
    LOBBY = b'lobby'
    BATTLE = b'battle'
    CURSOR = b'cursor'
    WAITING = b'waiting'


class GroupedViewSettings(namedtuple(b'GroupedViewSettings', b'alias clazz url layer group event scope cacheable containers canDrag canClose isModal isCentered flags')):

    def getDAAPIObject(self):
        return {b'alias': (self.alias), 
           b'url': (self.url), 
           b'layer': (self.layer), 
           b'event': (self.event), 
           b'group': (self.group), 
           b'isGrouped': (self.group is not None), 
           b'canDrag': (self.canDrag), 
           b'canClose': (self.canClose), 
           b'isModal': (self.isModal), 
           b'isCentered': (self.isCentered), 
           b'flags': (self.flags)}

    def replaceSettings(self, settings):
        return self._replace(**settings)

    def toImmutableSettings(self):
        return self


GroupedViewSettings.__new__.__defaults__ = (
 None, None, None, 0, None, None, None, False, None, True, True, False, True, 0)

class ViewSettings(GroupedViewSettings):

    @staticmethod
    def __new__(cls, alias, clazz, url, layer, event, scope, cacheable, containers, canDrag, canClose, isModal, isCentered, flags):
        return GroupedViewSettings.__new__(cls, alias, clazz, url, layer, None, event, scope, cacheable, containers, canDrag, canClose, isModal, isCentered, flags)


ViewSettings.__new__.__defaults__ = (
 None, None, None, 0, None, None, False, None, True, True, False, True, 0)

class ComponentSettings(GroupedViewSettings):

    @staticmethod
    def __new__(cls, alias, clazz, scope):
        return GroupedViewSettings.__new__(cls, alias, clazz, None, WindowLayer.UNDEFINED, None, None, scope, False, None, True, False, True, 0)


ComponentSettings.__new__.__defaults__ = (None, None, None)

class ContainerSettings(namedtuple(b'ContainerSettings', b'type clazz')):
    pass


ContainerSettings.__new__.__defaults__ = (None, None)
g_entitiesFactories = EntitiesFactories((
 DAAPIModuleFactory((WindowLayer.UNDEFINED,)),
 ViewFactory((
  WindowLayer.HIDDEN_SERVICE_LAYOUT,
  WindowLayer.MARKER,
  WindowLayer.VIEW,
  WindowLayer.SUB_VIEW,
  WindowLayer.TOP_SUB_VIEW,
  WindowLayer.CURSOR,
  WindowLayer.WAITING,
  WindowLayer.WINDOW,
  WindowLayer.FULLSCREEN_WINDOW,
  WindowLayer.TOP_WINDOW,
  WindowLayer.OVERLAY,
  WindowLayer.SERVICE_LAYOUT))))
