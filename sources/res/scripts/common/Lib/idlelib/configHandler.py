from __future__ import print_function
import os, sys
from ConfigParser import ConfigParser
from Tkinter import TkVersion
from tkFont import Font, nametofont

class InvalidConfigType(Exception):
    pass


class InvalidConfigSet(Exception):
    pass


class InvalidFgBg(Exception):
    pass


class InvalidTheme(Exception):
    pass


class IdleConfParser(ConfigParser):

    def __init__(self, cfgFile, cfgDefaults=None):
        self.file = cfgFile
        ConfigParser.__init__(self, defaults=cfgDefaults)
        return

    def Get(self, section, option, type=None, default=None, raw=False):
        if not self.has_option(section, option):
            return default
        else:
            if type == b'bool':
                return self.getboolean(section, option)
            if type == b'int':
                return self.getint(section, option)
            return self.get(section, option, raw=raw)

        return

    def GetOptionList(self, section):
        if self.has_section(section):
            return self.options(section)
        else:
            return []

        return

    def Load(self):
        self.read(self.file)
        return


class IdleUserConfParser(IdleConfParser):

    def AddSection(self, section):
        if not self.has_section(section):
            self.add_section(section)
        return

    def RemoveEmptySections(self):
        for section in self.sections():
            if not self.GetOptionList(section):
                self.remove_section(section)

        return

    def IsEmpty(self):
        self.RemoveEmptySections()
        return not self.sections()

    def RemoveOption(self, section, option):
        if self.has_section(section):
            return self.remove_option(section, option)
        return False

    def SetOption(self, section, option, value):
        if self.has_option(section, option):
            if self.get(section, option) == value:
                return False
            else:
                self.set(section, option, value)
                return True

        elif not self.has_section(section):
            self.add_section(section)
        self.set(section, option, value)
        return True
        return

    def RemoveFile(self):
        if os.path.exists(self.file):
            os.remove(self.file)
        return

    def Save(self):
        if not self.IsEmpty():
            fname = self.file
            try:
                cfgFile = open(fname, b'w')
            except IOError:
                os.unlink(fname)
                cfgFile = open(fname, b'w')

            with cfgFile:
                self.write(cfgFile)
        else:
            self.RemoveFile()
        return


class IdleConf():

    def __init__(self):
        self.config_types = (b'main', b'extensions', b'highlight', b'keys')
        self.defaultCfg = {}
        self.userCfg = {}
        self.cfg = {}
        self.CreateConfigHandlers()
        self.LoadCfgFiles()
        return

    def CreateConfigHandlers(self):
        if __name__ != b'__main__':
            idleDir = os.path.dirname(__file__)
        else:
            idleDir = os.path.abspath(sys.path[0])
        userDir = self.GetUserCfgDir()
        defCfgFiles = {}
        usrCfgFiles = {}
        for cfgType in self.config_types:
            defCfgFiles[cfgType] = os.path.join(idleDir, b'config-' + cfgType + b'.def')
            usrCfgFiles[cfgType] = os.path.join(userDir, b'config-' + cfgType + b'.cfg')

        for cfgType in self.config_types:
            self.defaultCfg[cfgType] = IdleConfParser(defCfgFiles[cfgType])
            self.userCfg[cfgType] = IdleUserConfParser(usrCfgFiles[cfgType])

        return

    def GetUserCfgDir(self):
        cfgDir = b'.idlerc'
        userDir = os.path.expanduser(b'~')
        if userDir != b'~':
            if not os.path.exists(userDir):
                warn = b'\n Warning: os.path.expanduser("~") points to\n ' + userDir + b',\n but the path does not exist.'
                try:
                    print(warn, file=sys.stderr)
                except IOError:
                    pass

                userDir = b'~'
        if userDir == b'~':
            userDir = os.getcwd()
        userDir = os.path.join(userDir, cfgDir)
        if not os.path.exists(userDir):
            try:
                os.mkdir(userDir)
            except (OSError, IOError):
                warn = b'\n Warning: unable to create user config directory\n' + userDir + b'\n Check path and permissions.\n Exiting!\n'
                print(warn, file=sys.stderr)
                raise SystemExit

        return userDir

    def GetOption(self, configType, section, option, default=None, type=None, warn_on_default=True, raw=False):
        try:
            if self.userCfg[configType].has_option(section, option):
                return self.userCfg[configType].Get(section, option, type=type, raw=raw)
        except ValueError:
            warning = b'\n Warning: configHandler.py - IdleConf.GetOption -\n invalid %r value for configuration option %r\n from section %r: %r' % (
             type, option, section,
             self.userCfg[configType].Get(section, option, raw=raw))
            try:
                print(warning, file=sys.stderr)
            except IOError:
                pass

        try:
            if self.defaultCfg[configType].has_option(section, option):
                return self.defaultCfg[configType].Get(section, option, type=type, raw=raw)
        except ValueError:
            pass

        if warn_on_default:
            warning = b'\n Warning: configHandler.py - IdleConf.GetOption -\n problem retrieving configuration option %r\n from section %r.\n returning default value: %r' % (
             option, section, default)
            try:
                print(warning, file=sys.stderr)
            except IOError:
                pass

        return default

    def SetOption(self, configType, section, option, value):
        self.userCfg[configType].SetOption(section, option, value)
        return

    def GetSectionList(self, configSet, configType):
        if configType not in self.config_types:
            raise InvalidConfigType(b'Invalid configType specified')
        if configSet == b'user':
            cfgParser = self.userCfg[configType]
        elif configSet == b'default':
            cfgParser = self.defaultCfg[configType]
        else:
            raise InvalidConfigSet(b'Invalid configSet specified')
        return cfgParser.sections()

    def GetHighlight(self, theme, element, fgBg=None):
        if self.defaultCfg[b'highlight'].has_section(theme):
            themeDict = self.GetThemeDict(b'default', theme)
        else:
            themeDict = self.GetThemeDict(b'user', theme)
        fore = themeDict[element + b'-foreground']
        if element == b'cursor':
            back = themeDict[b'normal-background']
        else:
            back = themeDict[element + b'-background']
        highlight = {b'foreground': fore, b'background': back}
        if not fgBg:
            return highlight
        if fgBg == b'fg':
            return highlight[b'foreground']
        if fgBg == b'bg':
            return highlight[b'background']
        raise InvalidFgBg(b'Invalid fgBg specified')
        return

    def GetThemeDict(self, type, themeName):
        if type == b'user':
            cfgParser = self.userCfg[b'highlight']
        elif type == b'default':
            cfgParser = self.defaultCfg[b'highlight']
        else:
            raise InvalidTheme(b'Invalid theme type specified')
        theme = {b'normal-foreground': b'#000000', b'normal-background': b'#ffffff', 
           b'keyword-foreground': b'#000000', 
           b'keyword-background': b'#ffffff', 
           b'builtin-foreground': b'#000000', 
           b'builtin-background': b'#ffffff', 
           b'comment-foreground': b'#000000', 
           b'comment-background': b'#ffffff', 
           b'string-foreground': b'#000000', 
           b'string-background': b'#ffffff', 
           b'definition-foreground': b'#000000', 
           b'definition-background': b'#ffffff', 
           b'hilite-foreground': b'#000000', 
           b'hilite-background': b'gray', 
           b'break-foreground': b'#ffffff', 
           b'break-background': b'#000000', 
           b'hit-foreground': b'#ffffff', 
           b'hit-background': b'#000000', 
           b'error-foreground': b'#ffffff', 
           b'error-background': b'#000000', 
           b'cursor-foreground': b'#000000', 
           b'stdout-foreground': b'#000000', 
           b'stdout-background': b'#ffffff', 
           b'stderr-foreground': b'#000000', 
           b'stderr-background': b'#ffffff', 
           b'console-foreground': b'#000000', 
           b'console-background': b'#ffffff'}
        for element in theme:
            if not cfgParser.has_option(themeName, element):
                warning = b'\n Warning: configHandler.IdleConf.GetThemeDict -\n problem retrieving theme element %r\n from theme %r.\n returning default color: %r' % (
                 element, themeName, theme[element])
                try:
                    print(warning, file=sys.stderr)
                except IOError:
                    pass

            theme[element] = cfgParser.Get(themeName, element, default=theme[element])

        return theme

    def CurrentTheme(self):
        default = self.GetOption(b'main', b'Theme', b'default', type=b'bool', default=True)
        if default:
            theme = self.GetOption(b'main', b'Theme', b'name2', default=b'')
        if default and not theme or not default:
            theme = self.GetOption(b'main', b'Theme', b'name', default=b'')
        source = self.defaultCfg if default else self.userCfg
        if source[b'highlight'].has_section(theme):
            return theme
        else:
            return b'IDLE Classic'

        return

    def CurrentKeys(self):
        return self.GetOption(b'main', b'Keys', b'name', default=b'')

    def GetExtensions(self, active_only=True, editor_only=False, shell_only=False):
        extns = self.RemoveKeyBindNames(self.GetSectionList(b'default', b'extensions'))
        userExtns = self.RemoveKeyBindNames(self.GetSectionList(b'user', b'extensions'))
        for extn in userExtns:
            if extn not in extns:
                extns.append(extn)

        if active_only:
            activeExtns = []
            for extn in extns:
                if self.GetOption(b'extensions', extn, b'enable', default=True, type=b'bool'):
                    if editor_only or shell_only:
                        if editor_only:
                            option = b'enable_editor'
                        else:
                            option = b'enable_shell'
                        if self.GetOption(b'extensions', extn, option, default=True, type=b'bool', warn_on_default=False):
                            activeExtns.append(extn)
                    else:
                        activeExtns.append(extn)

            return activeExtns
        return extns
        return

    def RemoveKeyBindNames(self, extnNameList):
        names = extnNameList
        kbNameIndicies = []
        for name in names:
            if name.endswith((b'_bindings', b'_cfgBindings')):
                kbNameIndicies.append(names.index(name))

        kbNameIndicies.sort(reverse=True)
        for index in kbNameIndicies:
            del names[index]

        return names

    def GetExtnNameForEvent(self, virtualEvent):
        extName = None
        vEvent = b'<<' + virtualEvent + b'>>'
        for extn in self.GetExtensions(active_only=0):
            for event in self.GetExtensionKeys(extn):
                if event == vEvent:
                    extName = extn

        return extName

    def GetExtensionKeys(self, extensionName):
        keysName = extensionName + b'_cfgBindings'
        activeKeys = self.GetCurrentKeySet()
        extKeys = {}
        if self.defaultCfg[b'extensions'].has_section(keysName):
            eventNames = self.defaultCfg[b'extensions'].GetOptionList(keysName)
            for eventName in eventNames:
                event = b'<<' + eventName + b'>>'
                binding = activeKeys[event]
                extKeys[event] = binding

        return extKeys

    def __GetRawExtensionKeys(self, extensionName):
        keysName = extensionName + b'_cfgBindings'
        extKeys = {}
        if self.defaultCfg[b'extensions'].has_section(keysName):
            eventNames = self.defaultCfg[b'extensions'].GetOptionList(keysName)
            for eventName in eventNames:
                binding = self.GetOption(b'extensions', keysName, eventName, default=b'').split()
                event = b'<<' + eventName + b'>>'
                extKeys[event] = binding

        return extKeys

    def GetExtensionBindings(self, extensionName):
        bindsName = extensionName + b'_bindings'
        extBinds = self.GetExtensionKeys(extensionName)
        if self.defaultCfg[b'extensions'].has_section(bindsName):
            eventNames = self.defaultCfg[b'extensions'].GetOptionList(bindsName)
            for eventName in eventNames:
                binding = self.GetOption(b'extensions', bindsName, eventName, default=b'').split()
                event = b'<<' + eventName + b'>>'
                extBinds[event] = binding

        return extBinds

    def GetKeyBinding(self, keySetName, eventStr):
        eventName = eventStr[2:-2]
        binding = self.GetOption(b'keys', keySetName, eventName, default=b'').split()
        return binding

    def GetCurrentKeySet(self):
        result = self.GetKeySet(self.CurrentKeys())
        if sys.platform == b'darwin':
            for k, v in result.items():
                v2 = [x.replace(b'<Alt-', b'<Option-') for x in v]
                if v != v2:
                    result[k] = v2

        return result

    def GetKeySet(self, keySetName):
        keySet = self.GetCoreKeys(keySetName)
        activeExtns = self.GetExtensions(active_only=1)
        for extn in activeExtns:
            extKeys = self.__GetRawExtensionKeys(extn)
            if extKeys:
                for event in extKeys:
                    if extKeys[event] in keySet.values():
                        extKeys[event] = b''
                    keySet[event] = extKeys[event]

        return keySet

    def IsCoreBinding(self, virtualEvent):
        return b'<<' + virtualEvent + b'>>' in self.GetCoreKeys()

    def GetCoreKeys(self, keySetName=None):
        keyBindings = {b'<<copy>>': [
                       b'<Control-c>', b'<Control-C>'], 
           b'<<cut>>': [
                      b'<Control-x>', b'<Control-X>'], 
           b'<<paste>>': [
                        b'<Control-v>', b'<Control-V>'], 
           b'<<beginning-of-line>>': [
                                    b'<Control-a>', b'<Home>'], 
           b'<<center-insert>>': [
                                b'<Control-l>'], 
           b'<<close-all-windows>>': [
                                    b'<Control-q>'], 
           b'<<close-window>>': [
                               b'<Alt-F4>'], 
           b'<<do-nothing>>': [
                             b'<Control-x>'], 
           b'<<end-of-file>>': [
                              b'<Control-d>'], 
           b'<<python-docs>>': [
                              b'<F1>'], 
           b'<<python-context-help>>': [
                                      b'<Shift-F1>'], 
           b'<<history-next>>': [
                               b'<Alt-n>'], 
           b'<<history-previous>>': [
                                   b'<Alt-p>'], 
           b'<<interrupt-execution>>': [
                                      b'<Control-c>'], 
           b'<<view-restart>>': [
                               b'<F6>'], 
           b'<<restart-shell>>': [
                                b'<Control-F6>'], 
           b'<<open-class-browser>>': [
                                     b'<Alt-c>'], 
           b'<<open-module>>': [
                              b'<Alt-m>'], 
           b'<<open-new-window>>': [
                                  b'<Control-n>'], 
           b'<<open-window-from-file>>': [
                                        b'<Control-o>'], 
           b'<<plain-newline-and-indent>>': [
                                           b'<Control-j>'], 
           b'<<print-window>>': [
                               b'<Control-p>'], 
           b'<<redo>>': [
                       b'<Control-y>'], 
           b'<<remove-selection>>': [
                                   b'<Escape>'], 
           b'<<save-copy-of-window-as-file>>': [
                                              b'<Alt-Shift-S>'], 
           b'<<save-window-as-file>>': [
                                      b'<Alt-s>'], 
           b'<<save-window>>': [
                              b'<Control-s>'], 
           b'<<select-all>>': [
                             b'<Alt-a>'], 
           b'<<toggle-auto-coloring>>': [
                                       b'<Control-slash>'], 
           b'<<undo>>': [
                       b'<Control-z>'], 
           b'<<find-again>>': [
                             b'<Control-g>', b'<F3>'], 
           b'<<find-in-files>>': [
                                b'<Alt-F3>'], 
           b'<<find-selection>>': [
                                 b'<Control-F3>'], 
           b'<<find>>': [
                       b'<Control-f>'], 
           b'<<replace>>': [
                          b'<Control-h>'], 
           b'<<goto-line>>': [
                            b'<Alt-g>'], 
           b'<<smart-backspace>>': [
                                  b'<Key-BackSpace>'], 
           b'<<newline-and-indent>>': [
                                     b'<Key-Return>', b'<Key-KP_Enter>'], 
           b'<<smart-indent>>': [
                               b'<Key-Tab>'], 
           b'<<indent-region>>': [
                                b'<Control-Key-bracketright>'], 
           b'<<dedent-region>>': [
                                b'<Control-Key-bracketleft>'], 
           b'<<comment-region>>': [
                                 b'<Alt-Key-3>'], 
           b'<<uncomment-region>>': [
                                   b'<Alt-Key-4>'], 
           b'<<tabify-region>>': [
                                b'<Alt-Key-5>'], 
           b'<<untabify-region>>': [
                                  b'<Alt-Key-6>'], 
           b'<<toggle-tabs>>': [
                              b'<Alt-Key-t>'], 
           b'<<change-indentwidth>>': [
                                     b'<Alt-Key-u>'], 
           b'<<del-word-left>>': [
                                b'<Control-Key-BackSpace>'], 
           b'<<del-word-right>>': [
                                 b'<Control-Key-Delete>']}
        if keySetName:
            for event in keyBindings:
                binding = self.GetKeyBinding(keySetName, event)
                if binding:
                    keyBindings[event] = binding
                else:
                    warning = b'\n Warning: configHandler.py - IdleConf.GetCoreKeys -\n problem retrieving key binding for event %r\n from key set %r.\n returning default value: %r' % (
                     event, keySetName, keyBindings[event])
                    try:
                        print(warning, file=sys.stderr)
                    except IOError:
                        pass

        return keyBindings

    def GetExtraHelpSourceList(self, configSet):
        helpSources = []
        if configSet == b'user':
            cfgParser = self.userCfg[b'main']
        elif configSet == b'default':
            cfgParser = self.defaultCfg[b'main']
        else:
            raise InvalidConfigSet(b'Invalid configSet specified')
        options = cfgParser.GetOptionList(b'HelpFiles')
        for option in options:
            value = cfgParser.Get(b'HelpFiles', option, default=b';')
            if value.find(b';') == -1:
                menuItem = b''
                helpPath = b''
            else:
                value = value.split(b';')
                menuItem = value[0].strip()
                helpPath = value[1].strip()
            if menuItem and helpPath:
                helpSources.append((menuItem, helpPath, option))

        helpSources.sort(key=(lambda x: int(x[2])))
        return helpSources

    def GetAllExtraHelpSourcesList(self):
        allHelpSources = self.GetExtraHelpSourceList(b'default') + self.GetExtraHelpSourceList(b'user')
        return allHelpSources

    def GetFont(self, root, configType, section):
        family = self.GetOption(configType, section, b'font', default=b'courier')
        size = self.GetOption(configType, section, b'font-size', type=b'int', default=b'10')
        bold = self.GetOption(configType, section, b'font-bold', default=0, type=b'bool')
        if family == b'TkFixedFont':
            if TkVersion < 8.5:
                family = b'Courier'
            else:
                f = Font(name=b'TkFixedFont', exists=True, root=root)
                actualFont = Font.actual(f)
                family = actualFont[b'family']
                size = actualFont[b'size']
                if size <= 0:
                    size = 10
                bold = actualFont[b'weight'] == b'bold'
        return (
         family, size, b'bold' if bold else b'normal')

    def LoadCfgFiles(self):
        for key in self.defaultCfg:
            self.defaultCfg[key].Load()
            self.userCfg[key].Load()

        return

    def SaveUserCfgFiles(self):
        for key in self.userCfg:
            self.userCfg[key].Save()

        return


idleConf = IdleConf()
if __name__ == b'__main__':
    from zlib import crc32
    line, crc = (
     0, 0)

    def sprint(obj):
        global crc
        global line
        txt = str(obj)
        line += 1
        crc = crc32(txt.encode(encoding=b'utf-8'), crc)
        print(txt)
        return


    def dumpCfg(cfg):
        print(b'\n', cfg, b'\n')
        for key in sorted(cfg.keys()):
            sections = cfg[key].sections()
            sprint(key)
            sprint(sections)
            for section in sections:
                options = cfg[key].options(section)
                sprint(section)
                sprint(options)
                for option in options:
                    sprint(option + b' = ' + cfg[key].Get(section, option))

        return


    dumpCfg(idleConf.defaultCfg)
    dumpCfg(idleConf.userCfg)
    print(b'\nlines = ', line, b', crc = ', crc, sep=b'')
