import logging
from collections import defaultdict
from helpers import dependency
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.genConsts.TUTORIAL_TRIGGER_TYPES import TUTORIAL_TRIGGER_TYPES
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from skeletons.gui.impl import IGuiLoader
from skeletons.tutorial import ITutorialLoader
from tutorial.data.events import GuiEventType
from shared_utils import first
from tutorial.gui.Scaleform.pop_ups import TutorialWulfWindow
_logger = logging.getLogger(__name__)

class GUIEffectScope(object):
    COMPONENT = 0
    SCENE = 1


class GUIEffect(object):
    __slots__ = ()

    def clear(self):
        return

    def play(self, effectData):
        return False

    def stop(self, effectID=None, effectSubType=None):
        return

    def cancel(self, scopeType, scopeName):
        return

    def isStillRunning(self, effectID=None, effectSubType=None):
        return False


class ApplicationEffect(GUIEffect):
    __tutorialLoader = dependency.descriptor(ITutorialLoader)
    __slots__ = (b'_app',)

    def __init__(self):
        super(GUIEffect, self).__init__()
        self._app = None
        return

    def clear(self):
        self._app = None
        super(ApplicationEffect, self).clear()
        return

    def setApplication(self, app):
        self._app = app
        return

    def _getContainer(self, layer):
        if self._app is None:
            return
        else:
            manager = self._app.containerManager
            if manager is None:
                return
            return manager.getContainer(layer)

    def _getTutorialLayout(self):
        return self.__tutorialLoader.gui


class ComponentEffect(GUIEffect):
    __slots__ = (b'_component',)

    def __init__(self):
        super(ComponentEffect, self).__init__()
        self._component = None
        return

    def clear(self):
        self._component = None
        super(ComponentEffect, self).clear()
        return

    def setComponent(self, component):
        self._component = component
        return

    def play(self, effectData):
        if self._component is not None:
            return self._doPlay(effectData)
        else:
            _logger.error(b'Component still is not found to play effect %r', self)
            return False

    def _doPlay(self, effectData):
        raise NotImplementedError
        return


class ShowDialogEffect(ApplicationEffect):
    __slots__ = (b'_aliasMap', b'_gameFaceMap', b'_dialogID', b'_layoutID')
    uiLoader = dependency.descriptor(IGuiLoader)

    def __init__(self, aliasMap, gameFaceMap):
        super(ShowDialogEffect, self).__init__()
        self._aliasMap = aliasMap
        self._gameFaceMap = gameFaceMap
        self._dialogID = None
        self._layoutID = None
        return

    def clear(self):
        self._dialogID = None
        self._layoutID = None
        super(ShowDialogEffect, self).clear()
        return

    def play(self, effectData):
        effectData = effectData[0]
        result = False
        if b'type' in effectData and b'dialogID' in effectData:
            dialogType = effectData[b'type']
            dialogID = effectData[b'dialogID']
            if dialogID == self._dialogID:
                _logger.error(b'Dialog is displayed %r', effectData[b'dialogID'])
                return False
            if dialogType in self._aliasMap:
                alias = self._aliasMap[dialogType]
                self._dialogID = dialogID
                self._layoutID = None
                self._app.loadView(SFViewLoadParams(alias, dialogID), effectData)
                result = True
            elif dialogType in self._gameFaceMap:
                self._dialogID = dialogID
                viewClass = self._gameFaceMap[dialogType]
                window = TutorialWulfWindow(viewClass(), effectData)
                window.load()
                self._layoutID = window.getLayoutID()
                result = True
            else:
                _logger.error(b'Alias of dialog not found. effectData: %r, aliasMap: %r', effectData, self._aliasMap)
        else:
            _logger.error(b'Type or id of dialog not found %r', effectData)
        return result

    def stop(self, effectID=None, effectSubType=None):
        isForceStop = effectID is None
        if not isForceStop and effectID != self._dialogID:
            _logger.error(b'Dialog is not opened %r', effectID)
            return
        else:
            effectID = self._dialogID
            layoutID = self._layoutID
            self._dialogID = None
            self._layoutID = None
            if layoutID is not None:
                view = self.uiLoader.windowsManager.getViewByLayoutID(layoutID)
                if view is not None:
                    view.destroyWindow()
                return
            container = self._getContainer(WindowLayer.TOP_WINDOW)
            if container is not None:
                dialog = container.getView(criteria={(POP_UP_CRITERIA.UNIQUE_NAME): effectID})
                if dialog is not None:
                    dialog.destroy()
            return

    def isStillRunning(self, effectID=None, effectSubType=None):
        if effectID is not None:
            result = self._dialogID == effectID
        else:
            result = self._dialogID is not None
        return result


class ShowWindowEffect(ApplicationEffect):
    __slots__ = (b'_aliasMap', b'_windowIDs')

    def __init__(self, aliasMap):
        super(ShowWindowEffect, self).__init__()
        self._aliasMap = aliasMap
        self._windowIDs = set()
        return

    def clear(self):
        self._windowIDs.clear()
        super(ShowWindowEffect, self).clear()
        return

    def play(self, effectData):
        windowID, windowType, content = effectData
        result = False
        if windowType in self._aliasMap:
            alias = self._aliasMap[windowType]
            self._windowIDs.add(windowID)
            self._app.loadView(SFViewLoadParams(alias, windowID), content)
            result = True
        else:
            _logger.error(b'Alias of window not found %r %r', windowType, self._aliasMap)
        return result

    def stop(self, effectID=None, effectSubType=None):
        isForceStop = effectID is None
        if not isForceStop:
            if effectID not in self._windowIDs:
                _logger.error(b'Window is not opened %r', effectID)
                return
            effectIDs = {
             effectID}
        else:
            effectIDs = self._windowIDs.copy()
        container = self._getContainer(WindowLayer.WINDOW)
        if container is None:
            container = self._getContainer(WindowLayer.OVERLAY)
        if container is not None:
            getView = container.getView
            for eID in effectIDs:
                window = getView(criteria={(POP_UP_CRITERIA.UNIQUE_NAME): eID})
                if window is not None:
                    window.destroy()
                    self._windowIDs.remove(eID)
                elif not isForceStop:
                    _logger.error(b'Window is not opened %r', eID)

        return

    def isStillRunning(self, effectID=None, effectSubType=None):
        if effectID is not None:
            result = effectID in self._windowIDs
        else:
            result = len(self._windowIDs)
        return result


_GUI_EVENT_TO_TRIGGER_TYPE = {(GuiEventType.CLICK): (TUTORIAL_TRIGGER_TYPES.CLICK_TYPE), 
   (GuiEventType.CLICK_OUTSIDE): (TUTORIAL_TRIGGER_TYPES.CLICK_OUTSIDE_TYPE), 
   (GuiEventType.ESC): (TUTORIAL_TRIGGER_TYPES.ESCAPE), 
   (GuiEventType.ENABLE): (TUTORIAL_TRIGGER_TYPES.ENABLED), 
   (GuiEventType.DISABLE): (TUTORIAL_TRIGGER_TYPES.DISABLED), 
   (GuiEventType.ENABLED_CHANGE): (TUTORIAL_TRIGGER_TYPES.ENABLED_CHANGE), 
   (GuiEventType.VISIBLE_CHANGE): (TUTORIAL_TRIGGER_TYPES.VISIBLE_CHANGE)}

class ShowChainHint(ApplicationEffect):
    __slots__ = (b'_hintsDict',)

    def __init__(self):
        super(ShowChainHint, self).__init__()
        self._hintsDict = {}
        return

    def isStillRunning(self, effectID=None, effectSubType=None):
        if effectID is not None:
            result = effectID in self._hintsDict
        else:
            result = bool(self._hintsDict)
        return result

    def play(self, effectData):
        hintProps, triggers, silent = effectData
        if hintProps.hintID in self._hintsDict:
            _logger.debug(b'Hint %r is already added', hintProps.hintID)
            return True
        else:
            layout = self._getTutorialLayout()
            if layout is not None:
                content = {b'uniqueID': (hintProps.uniqueID), b'hintText': (hintProps.text), 
                   b'hasBox': (hintProps.hasBox), 
                   b'hasArrow': False, 
                   b'arrowDir': b'', 
                   b'arrowLoop': False, 
                   b'updateRuntime': (hintProps.updateRuntime), 
                   b'hideImmediately': (hintProps.hideImmediately), 
                   b'checkViewArea': (hintProps.checkViewArea)}
                arrow = hintProps.arrow
                if arrow is not None:
                    content[b'hasArrow'] = True
                    content[b'arrowDir'] = arrow.direction
                    content[b'arrowLoop'] = arrow.loop
                    content[b'positionValue'] = arrow.positionValue
                    content[b'textPadding'] = arrow.textPadding
                padding = hintProps.padding
                if padding is not None:
                    content[b'padding'] = padding._asdict()
                triggers = [_GUI_EVENT_TO_TRIGGER_TYPE[item] for item in triggers]
                _logger.debug(b'layout %r showInteractiveHint with id %r, content %r, triggers %r', layout, hintProps.itemID, content, triggers)
                result = layout.showInteractiveHint(hintProps.itemID, content, triggers, silent)
                if result:
                    self._hintsDict.update({(hintProps.hintID): (hintProps.itemID)})
                return result
            return False

    def stop(self, effectID=None, effectSubType=None):
        if effectID and effectID not in self._hintsDict:
            _logger.debug(b'Hint is not added. effectID: %r', effectID)
            return
        layout = self._getTutorialLayout()
        if layout and effectID:
            layout.closeInteractiveHint(self._hintsDict.pop(effectID))
        elif layout:
            for itemId in self._hintsDict.itervalues():
                layout.closeInteractiveHint(itemId)

        return

    def cancel(self, scopeType, scopeName):
        _logger.debug(b'Hint cancel. scopeType: %r, scopeName: %r., _hintsDict: %r', scopeType, scopeName, self._hintsDict)
        if scopeType == GUIEffectScope.COMPONENT and scopeName in self._hintsDict:
            self.stop(scopeName)
        elif scopeType == GUIEffectScope.SCENE:
            self.stop()
        return


class ShowOnceOnlyHint(ShowChainHint):
    __slots__ = ()

    def stop(self, effectID=None, effectSubType=None):
        if effectID is not None:
            super(ShowOnceOnlyHint, self).stop(effectID)
        return


class UpdateContentEffect(ApplicationEffect):
    __slots__ = ()

    def play(self, effectData):
        effectData = effectData[0]
        result = False
        effectID = None
        layer = None
        if b'dialogID' in effectData:
            effectID = effectData[b'dialogID']
            layer = WindowLayer.TOP_WINDOW
        if effectID is not None:
            container = self._getContainer(layer)
            if container is not None:
                view = container.getView(criteria={(POP_UP_CRITERIA.UNIQUE_NAME): effectID})
                if view is not None:
                    if hasattr(view, b'as_updateContentS'):
                        view.as_updateContentS(effectData)
                        result = True
                    else:
                        _logger.error(b'View %r is invalid', view)
                else:
                    _logger.debug(b'View is not on scene. effectID: %r', effectID)
                    result = True
        return result


class SetCriteriaEffect(ApplicationEffect):
    __slots__ = ()

    def play(self, effectData):
        itemID, value = effectData
        layout = self._getTutorialLayout()
        if layout is not None:
            layout.setCriteria(itemID, value)
            return True
        else:
            return False


class SetViewCriteriaEffect(ApplicationEffect):
    __slots__ = ()

    def play(self, effectData):
        itemIDs, value = effectData
        layout = self._getTutorialLayout()
        if layout is not None:
            for itemID in itemIDs:
                layout.setViewCriteria(itemID, value)

            return True
        return False


_ACTION_TO_TRIGGER_TYPE = {(GuiEventType.CLICK): (TUTORIAL_TRIGGER_TYPES.CLICK_TYPE), 
   (GuiEventType.CLICK_OUTSIDE): (TUTORIAL_TRIGGER_TYPES.CLICK_OUTSIDE_TYPE), 
   (GuiEventType.ESC): (TUTORIAL_TRIGGER_TYPES.ESCAPE), 
   (GuiEventType.ENABLE): (TUTORIAL_TRIGGER_TYPES.ENABLED), 
   (GuiEventType.DISABLE): (TUTORIAL_TRIGGER_TYPES.DISABLED), 
   (GuiEventType.ENABLED_CHANGE): (TUTORIAL_TRIGGER_TYPES.ENABLED_CHANGE), 
   (GuiEventType.VISIBLE_CHANGE): (TUTORIAL_TRIGGER_TYPES.VISIBLE_CHANGE)}

class SetTriggerEffect(ApplicationEffect):
    __slots__ = (b'_triggersByItem',)

    def __init__(self):
        super(SetTriggerEffect, self).__init__()
        self._triggersByItem = defaultdict(list)
        return

    def play(self, effectData):
        itemID, actionType = effectData
        if actionType not in _ACTION_TO_TRIGGER_TYPE:
            _logger.error(b'Cannot find trigger type. itemID: %r, actionType: %r', itemID, actionType)
            return False
        else:
            triggerType = _ACTION_TO_TRIGGER_TYPE[actionType]
            layout = self._getTutorialLayout()
            if layout is None:
                return False
            itemTriggers = self._triggersByItem[itemID]
            if itemID in itemTriggers:
                _logger.error(b'Trigger is already set for item. itemID: %r, triggerType: %r', itemID, triggerType)
                return False
            itemTriggers.append(triggerType)
            layout.setTriggers(itemID, itemTriggers)
            return True

    def stop(self, effectID=None, effectSubType=None):
        layout = self._getTutorialLayout()
        itemID, actionType = effectID, effectSubType
        if itemID is None:
            if layout is not None:
                for _itemID in self._triggersByItem.iterkeys():
                    layout.clearTriggers(_itemID)

            self._triggersByItem.clear()
        elif actionType is None:
            if itemID in self._triggersByItem:
                if layout is not None:
                    layout.clearTriggers(itemID)
                del self._triggersByItem[itemID]
        elif itemID in self._triggersByItem:
            itemTriggers = self._triggersByItem[itemID]
            if actionType in _ACTION_TO_TRIGGER_TYPE:
                triggerType = _ACTION_TO_TRIGGER_TYPE[actionType]
                if triggerType in itemTriggers:
                    itemTriggers.remove(triggerType)
                    if layout is not None:
                        if itemTriggers:
                            layout.setTriggers(itemID, itemTriggers)
                        else:
                            layout.clearTriggers(itemID)
                    if not itemTriggers:
                        del self._triggersByItem[itemID]
            else:
                _logger.error(b'Cannot find trigger type. itemID: %r, actionType: %r', itemID, actionType)
        return


class SetItemPropsEffect(ApplicationEffect):
    __slots__ = ()

    def play(self, effectData):
        itemID, props = effectData
        layout = self._getTutorialLayout()
        if layout is None:
            return False
        else:
            return layout.setComponentProps(itemID, props)


class PlayAnimationEffect(ApplicationEffect):
    __slots__ = (b'_activeEffects',)

    def __init__(self):
        super(PlayAnimationEffect, self).__init__()
        self._activeEffects = {}
        return

    def isStillRunning(self, effectID=None, effectSubType=None):
        return first(self._iterEffects(effectID, effectSubType)) is not None

    def play(self, effectData):
        itemID, animID = effectData
        if itemID in self._activeEffects:
            _logger.error(b'Another animation is already playing on item %r. ' + b'Multiple animations on one item are not supported.', itemID)
            return False
        else:
            layout = self._getTutorialLayout()
            if layout is None:
                return False
            if layout.playComponentAnimation(itemID, animID):
                self._activeEffects[itemID] = animID
                return True
            return False

    def stop(self, effectID=None, effectSubType=None):
        layout = self._getTutorialLayout()
        if layout is None:
            return
        else:
            for itemID, animID in self._iterEffects(effectID, effectSubType):
                layout.stopComponentAnimation(itemID, animID)
                del self._activeEffects[itemID]

            return

    def cancel(self, scopeType, scopeName):
        if scopeType == GUIEffectScope.COMPONENT:
            self.stop(scopeName)
        return

    def _iterEffects(self, effectID, effectSubType):
        itemID, animID = effectID, effectSubType
        if itemID is None:
            items = self._activeEffects.items()
        elif itemID in self._activeEffects:
            items = (
             (
              itemID, self._activeEffects[itemID]),)
        else:
            items = ()
        for _itemID, _animID in items:
            if animID in (_animID, None):
                yield (
                 _itemID, _animID)

        return


class EffectsPlayer(object):
    __slots__ = (b'_effects',)

    def __init__(self, effects):
        super(EffectsPlayer, self).__init__()
        self._effects = effects
        return

    def iterEffects(self):
        for name, effect in self._effects.iteritems():
            yield (
             name, effect)

        return

    def filterByName(self, *names):
        for name, effect in self._effects.iteritems():
            if name in names:
                yield effect

        return

    def clear(self):
        while self._effects:
            _, effect = self._effects.popitem()
            effect.clear()

        return

    def play(self, effectName, effectData):
        result = False
        if effectName in self._effects:
            result = self._effects[effectName].play(effectData)
        else:
            _logger.error(b'GUI effect %r not found', effectName)
        return result

    def stop(self, effectName, effectID, effectSubType=None):
        if effectName in self._effects:
            self._effects[effectName].stop(effectID=effectID, effectSubType=effectSubType)
        else:
            _logger.error(b'GUI effect %r not found', effectName)
        return

    def cancel(self, scopeType, scopeName):
        for effect in self._effects.itervalues():
            effect.cancel(scopeType, scopeName)

        return

    def stopAll(self):
        for effect in self._effects.itervalues():
            effect.stop()

        return

    def isStillRunning(self, effectName, effectID=None, effectSubType=None):
        result = False
        if effectName in self._effects:
            result = self._effects[effectName].isStillRunning(effectID=effectID, effectSubType=effectSubType)
        else:
            _logger.error(b'GUI effect %r not found', effectName)
        return result
