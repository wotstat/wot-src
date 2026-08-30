import BigWorld, Keys
from functools import partial
from bwdebug import ERROR_MSG, INFO_MSG, TRACE_MSG
KEY_ALIAS_CONTROL = (
 Keys.KEY_LCONTROL, Keys.KEY_RCONTROL)
KEY_ALIAS_ALT = (Keys.KEY_LALT, Keys.KEY_RALT)
KEY_ALIAS_SHIFT = (Keys.KEY_LSHIFT, Keys.KEY_RSHIFT)
KEY_ALIAS_WINDOWS = (Keys.KEY_LWIN, Keys.KEY_RWIN)
keyAliases = {b'CONTROL': KEY_ALIAS_CONTROL, b'ALT': KEY_ALIAS_ALT, 
   b'SHIFT': KEY_ALIAS_SHIFT, 
   b'WINDOWS': KEY_ALIAS_WINDOWS}

def _stringToKey(key):
    if key in keyAliases:
        return keyAliases[key]
    else:
        return BigWorld.stringToKey(key)

    return


def _keyToString(key):
    try:
        return _reverseKeysLookup[key]
    except KeyError:
        return b''

    return


def _isKeyDown(key):
    if type(key) is tuple:
        for k in key:
            if BigWorld.isKeyDown(k):
                return True

    else:
        return BigWorld.isKeyDown(key)
    return


def _keyInKeyList(key, keyList):
    for k in keyList:
        if type(k) is tuple:
            return _keyInKeyList(key, k)
        if k == key:
            return True

    return False


def BWKeyBindingAction(actionName, *args, **kargs):

    def addActionName(actionName, actionFunction):
        if not hasattr(actionFunction, b'_BWKeyBindingActionNames'):
            actionFunction._BWKeyBindingActionNames = []
        actionFunction._BWKeyBindingActionNames += [(actionName, args, kargs)]
        return actionFunction

    return partial(addActionName, actionName)


class BWActionHandler(object):

    def __init__(self):
        self.setupActionList()
        return

    def setupActionList(self):
        entityClass = self.__class__
        self.actionFunctions = {}
        for name, function in entityClass.__dict__.items():
            if hasattr(function, b'_BWKeyBindingActionNames'):
                actionNames = function._BWKeyBindingActionNames
                function = getattr(self, name)
                for actionName, args, kargs in actionNames:
                    self.actionFunctions[actionName] = partial(getattr(self, name), *args, **kargs)

        return


class BWKeyBindings:

    def __init__(self):
        self.actionsByBinding = {}
        self.actionsByName = {}
        self.handlers = []
        return

    def readInDefaultKeyBindings(self, dataSection):
        self.actionsByName = {}
        for actionDataSection in dataSection.values():
            actionBinding = _ActionBinding()
            actionBinding.readFromDataSection(actionDataSection)
            actionName = actionBinding.actionName
            self.actionsByName[actionName] = actionBinding

        return

    def readInPreferenceKeyBindings(self, dataSection):
        for actionDataSection in dataSection.values():
            actionBinding = _ActionBinding()
            actionBinding.readFromDataSection(actionDataSection)
            actionName = actionBinding.actionName
            if self.actionsByName.has_key(actionName):
                self.actionsByName[actionName].addPreferenceKeyBindings(actionBinding)

        return

    def writePreferenceKeyBindings(self, dataSection):
        dataSection.deleteSection(b'keyBindings')
        dataSection.createSection(b'keyBindings')
        keyBindingsSection = dataSection._keyBindings
        for action in self.actionsByName.values():
            action.writePreferenceKeyBindings(keyBindingsSection)

        return

    def addHandler(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)
        return

    def removeHandler(self, handler):
        if handler in self.handlers:
            self.handlers.remove(handler)
        return

    def buildBindList(self):
        self.actionsByBinding = {}
        for action in self.actionsByName.values():
            for binding in action.getBindings():
                if not self.actionsByBinding.has_key(binding):
                    self.actionsByBinding[binding] = []
                self.actionsByBinding[binding] += [action.actionName]

        self.bindList = []
        for downKeys, actionNames in self.actionsByBinding.items():
            notDownLists = []
            for otherDownKeys, otherActionNames in self.actionsByBinding.items():
                if actionNames != otherActionNames:
                    containedEntirely = 1
                    for key in downKeys:
                        containedEntirely = containedEntirely and key in otherDownKeys

                    if containedEntirely:
                        notDownList = []
                        for otherKey in otherDownKeys:
                            if otherKey not in downKeys:
                                notDownList.append(otherKey)

                        notDownLists.append(notDownList)

            for actionName in actionNames:
                self.bindList.append((downKeys, notDownLists, actionName))

        for entity in self.handlers:
            if getattr(entity, b'onBindCallback', None):
                entity.onBindCallback(self)

        return

    def printBindList(self):
        bindListByName = {}
        for downKeys, notDownKeysList, actionName in self.bindList:
            if bindListByName.has_key(actionName):
                bindListByName[actionName] += [(downKeys, notDownKeysList)]
            else:
                bindListByName[actionName] = [
                 (
                  downKeys, notDownKeysList)]

        actionNames = sorted(bindListByName.keys())
        for actionName in actionNames:
            for downKeys, notDownKeysList in bindListByName[actionName]:
                print actionName, b':',
                for downKey in downKeys:
                    print _keyToString(downKey),

                if len(notDownKeysList) > 0:
                    if len(notDownKeysList) == 1:
                        print b'but not',
                        for notDownKey in notDownKeysList[0]:
                            print _keyToString(notDownKey),

                    else:
                        print b'but not any of {',
                        for notDownKeys in notDownKeysList:
                            print b'[',
                            for notDownKey in notDownKeys:
                                print _keyToString(notDownKey),

                            print b']',

                        print b'}',
                print

        return

    def getBindingsForAction(self, actionName):
        if self.actionsByName.has_key(actionName):
            return self.actionsByName[actionName].getBindings()
        else:
            return []

        return

    def addBindingForAction(self, actionName, binding):
        binding = tuple(sorted(binding))
        if actionName not in self.actionsByName:
            ERROR_MSG(b"Action '%s' is unknown" % (actionName,))
            return
        action = self.actionsByName[actionName]
        bindings = action.getBindings()
        if binding in bindings:
            ERROR_MSG(b"Action '%s' already has the binding %s" % (actionName, binding))
            return
        return action.addBinding(binding)

    def removeBindingForAction(self, actionName, binding):
        binding = tuple(sorted(binding))
        if actionName not in self.actionsByName:
            ERROR_MSG(b"Action '%s' is unknown" % (actionName,))
            return
        action = self.actionsByName[actionName]
        bindings = action.getBindings()
        if binding not in bindings:
            ERROR_MSG(b"Action '%s' does not have the binding %s" % (actionName, binding))
            return
        return self.actionsByName[actionName].removeBinding(binding)

    def callActionByName(self, actionName, *args, **kargs):
        for entity in reversed(self.handlers):
            if entity.actionFunctions.has_key(actionName):
                ret = entity.actionFunctions[actionName](True, *args, **kargs)
                if ret != False:
                    break

        return

    def callActionForKeyState(self, key):
        for downKeys, upKeySets, actionName in self.bindList:
            if _keyInKeyList(key, downKeys):
                okayToGo = 1
                for downKey in downKeys:
                    okayToGo = okayToGo and _isKeyDown(downKey)

                if okayToGo:
                    for upKeys in upKeySets:
                        allDown = True
                        for upKey in upKeys:
                            allDown = allDown and _isKeyDown(upKey)

                        okayToGo = okayToGo and not allDown

                for entity in reversed(self.handlers):
                    if entity.actionFunctions.has_key(actionName):
                        ret = entity.actionFunctions[actionName](okayToGo)
                        if ret != False:
                            break

        return

    def getActionForKeyState(self, key):
        for downKeys, upKeySets, actionName in self.bindList:
            if _keyInKeyList(key, downKeys):
                okayToGo = 1
                for downKey in downKeys:
                    okayToGo = okayToGo and _isKeyDown(downKey)

                if okayToGo:
                    for upKeys in upKeySets:
                        allDown = True
                        for upKey in upKeys:
                            allDown = allDown and _isKeyDown(upKey)

                        okayToGo = okayToGo and not allDown

                if okayToGo:
                    return actionName

        return


class _ActionBinding:

    def __init__(self):
        self.actionName = b''
        self.bindings = ()
        self.defaultBindings = ()
        return

    def readFromDataSection(self, dataSection):
        self.actionName = dataSection._name.asString
        for key, value in dataSection.items():
            if key == b'keys':
                keys = value.asString.split()
                keys = [_stringToKey(key) for key in keys]
                if 0 in keys:
                    ERROR_MSG(b"Action '%s' is bound to one more more invalid keys" % (self.actionName,))
                if len(keys) > 0:
                    self.bindings += (tuple(sorted(keys)),)

        self.defaultBindings = self.bindings
        return

    def addPreferenceKeyBindings(self, preferenceBindings):
        newBindings = sorted(preferenceBindings.getBindings())
        if newBindings != sorted(self.defaultBindings):
            self.bindings = tuple(newBindings)
        return

    def writePreferenceKeyBindings(self, dataSection):
        if sorted(self.bindings) != sorted(self.defaultBindings):
            newDataSection = dataSection.createSection(b'action')
            newDataSection.writeString(b'name', self.actionName)
            for binding in self.bindings:
                bindingString = b''
                for key in binding:
                    bindingString += _reverseKeysLookup[key] + b' '

                newDataSection.writeStrings(b'keys', (bindingString.strip(),))

        return

    def addBinding(self, binding):
        self.bindings += (tuple(binding),)
        return

    def removeBinding(self, binding):
        newBindings = list(self.bindings)
        newBindings.remove(binding)
        self.bindings = tuple(newBindings)
        return

    def getBindings(self):
        return self.bindings


_reverseKeysLookup = {}

def _buildReverseKeysLookup():
    preferredSynonyms = (b'NONE', b'LEFTMOUSE', b'RIGHTMOUSE', b'MIDDLEMOUSE')
    for name in preferredSynonyms:
        value = BigWorld.stringToKey(name)
        if value != 0 or name == b'NONE':
            _reverseKeysLookup[value] = name
        else:
            TRACE_MSG(b'Synonym "%s" is missing from BigWorlds key list' % (name,))

    for name in Keys.__dict__.keys():
        value = BigWorld.stringToKey(name[4:])
        if value == 0:
            continue
        if _reverseKeysLookup.has_key(value):
            if _reverseKeysLookup[value] not in preferredSynonyms:
                TRACE_MSG(b'Unexpected synonym for "%s": "%s"' % (
                 _reverseKeysLookup[value], BigWorld.keyToString(value)))
        else:
            _reverseKeysLookup[value] = BigWorld.keyToString(value)

    for aliasName, aliasKeys in keyAliases.iteritems():
        _reverseKeysLookup[aliasKeys] = aliasName

    return


_buildReverseKeysLookup()
