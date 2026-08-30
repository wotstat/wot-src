import typing, ResMgr, section2dict
from dict2model import models, schemas, fields
from helpers import VERSION_FILE_PATH, LOC_VERSION_FILE_PATH
_clientVersion = None
_locVersion = None

class ClientVersionMetaModel(models.Model):
    __slots__ = (b'client', b'overrides', b'realm', b'branch', b'buildScriptsRevision')

    def __init__(self, client=b'', overrides=b'', realm=b'', branch=b'', buildScriptsRevision=b''):
        super(ClientVersionMetaModel, self).__init__()
        self.client = client
        self.overrides = overrides
        self.realm = realm
        self.branch = branch
        self.buildScriptsRevision = buildScriptsRevision
        return

    def _reprArgs(self):
        return (b'client={}, overrides={}, realm={}, branch={}, buildScriptsRevision={}').format(self.client, self.overrides, self.realm, self.branch, self.buildScriptsRevision)


class ClientVersionModel(models.Model):
    __slots__ = (b'appname', b'version', b'showLicense', b'ingameHelpVersion', b'meta')

    def __init__(self, appname=b'', version=b'', showLicense=b'', ingameHelpVersion=b'', meta=None):
        super(ClientVersionModel, self).__init__()
        self.appname = appname
        self.version = version
        self.showLicense = showLicense
        self.ingameHelpVersion = ingameHelpVersion
        self.meta = meta or ClientVersionMetaModel()
        return

    def _reprArgs(self):
        return (b'appname={}, version={}, showLicense={}, ingameHelpVersion={}, meta={}').format(self.appname, self.version, self.showLicense, self.ingameHelpVersion, self.meta)


class LocalizationVersionModel(models.Model):
    __slots__ = (b'version', b'revision', b'language')

    def __init__(self, version=b'', revision=b'', language=b''):
        super(LocalizationVersionModel, self).__init__()
        self.version = version
        self.revision = revision
        self.language = language
        return

    def _reprArgs(self):
        return (b'version={}, revision={}, language={}').format(self.version, self.revision, self.language)


_clientVersionMetaSchema = schemas.Schema[ClientVersionMetaModel](fields={b'client': (fields.String(required=False, default=b'')), 
   b'overrides': (fields.String(required=False, default=b'')), 
   b'realm': (fields.String(required=False, default=b'')), 
   b'branch': (fields.String(required=False, default=b'')), 
   b'buildScriptsRevision': (fields.String(required=False, default=b''))}, checkUnknown=False, modelClass=ClientVersionMetaModel)
_clientVersionSchema = schemas.Schema[ClientVersionModel](fields={b'appname': (fields.String(required=False, default=b'')), 
   b'version': (fields.String(required=False, default=b'')), 
   b'showLicense': (fields.String(required=False, default=b'')), 
   b'ingameHelpVersion': (fields.String(required=False, default=b'')), 
   b'meta': (fields.Nested(schema=_clientVersionMetaSchema, required=False, default=ClientVersionMetaModel))}, checkUnknown=False, modelClass=ClientVersionModel)
_localizationVersionSchema = schemas.Schema[LocalizationVersionModel](fields={b'version': (fields.String(required=False, default=b'')), 
   b'revision': (fields.String(required=False, default=b'')), 
   b'language': (fields.String(required=False, default=b''))}, checkUnknown=False, modelClass=LocalizationVersionModel)

def getClientVersion(force=False):
    global _clientVersion
    if _clientVersion is None or force:
        section = ResMgr.openSection(VERSION_FILE_PATH)
        _clientVersion = _clientVersionSchema.deserialize(section2dict.parse(section, normalizeValues=False) if section else {})
    return _clientVersion


def getLocalizationVersion(force=False):
    global _locVersion
    if _locVersion is None or force:
        section = ResMgr.openSection(LOC_VERSION_FILE_PATH)
        _locVersion = _localizationVersionSchema.deserialize(section2dict.parse(section, normalizeValues=False) if section else {})
    return _locVersion
