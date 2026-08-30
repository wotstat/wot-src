from __future__ import absolute_import
import BigWorld, ResMgr
from collections import namedtuple
_EXTENSIONS_RELATIVE_DIR = b'../wot_ext'
_EXTENSIONS_ABS_DIR = b'res/wot_ext'
_EXTENSION_PATH_TEMPLATE = b'{root}/{extension}/{path}'
_SETTINGS_FORMATTER = b'@({})'
_EXT_FORMATTER_ARGUMENT = b'EXTENSION'
_EXT_FORMATTER = _SETTINGS_FORMATTER.format(_EXT_FORMATTER_ARGUMENT)
_EXTENSION_IMPORT_PATHS = [
 9, 
 10, 
 11, 
 12, 
 13, 
 14]

def makeExtensionPath(extension, path):
    return _EXTENSION_PATH_TEMPLATE.format(root=_EXTENSIONS_RELATIVE_DIR, extension=extension, path=path)


Extension = namedtuple(b'Extension', (b'path', b'name', b'isEnabled', b'dirName', b'personality', b'commonPersonality', b'editorPersonality'))

class ExtensionsManager(object):
    __slots__ = (b'_extensions',)

    def __init__(self):
        super(ExtensionsManager, self).__init__()
        self._extensions = self._readExtensions()
        return

    @property
    def extensions(self):
        return [value for _, value in sorted(self._extensions.items())]

    @property
    def activeExtensions(self):
        return [extension for extension in self.extensions if extension.isEnabled]

    @property
    def activePaths(self):
        return [(b'/').join((_EXTENSIONS_ABS_DIR, extension.dirName, relativePath)) for extension in self.activeExtensions for relativePath in _EXTENSION_IMPORT_PATHS]

    def hasExtensions(self):
        return bool(self._extensions)

    def _readExtensions(self):
        extensions = {}
        for root in self._getExtensionsDirList():
            extension = self._readExtension(root)
            if extension:
                extensions[extension.name] = extension

        return extensions

    def getExtensionPath(self, path):
        if _EXT_FORMATTER not in path:
            return [path]
        pathList = []
        for ext in self.activeExtensions:
            extPath = path.replace(_EXT_FORMATTER, ext.dirName)
            if ResMgr.isDir(extPath) or ResMgr.isFile(extPath):
                pathList.append(extPath)

        return pathList

    @staticmethod
    def _readExtension(root):
        section = ResMgr.openSection(root + b'/extension.xml')
        if not section:
            return None
        else:
            return Extension(root + b'/', section.readString(b'FeatureName'), section.readBool(b'IsEnabled'), root.split(b'/')[-1], section.readString(b'Personality'), section.readString(b'CommonPersonality'), section.readString(b'EditorPersonality'))

    @staticmethod
    def _getExtensionsDirList():
        if getattr(BigWorld, b'getExtensionsDirList', None):
            return BigWorld.getExtensionsDirList()
        else:
            import os
            return [(b'{}/{}').format(_EXTENSIONS_RELATIVE_DIR, item) for item in os.listdir(ResMgr.resolveToAbsolutePath(_EXTENSIONS_RELATIVE_DIR)) if os.path.isdir(ResMgr.resolveToAbsolutePath(os.path.join(_EXTENSIONS_RELATIVE_DIR, item)))]


g_extensionsManager = ExtensionsManager()
