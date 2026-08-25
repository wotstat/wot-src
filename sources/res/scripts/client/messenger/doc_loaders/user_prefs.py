import types
from helpers import dependency
from messenger.doc_loaders import _xml_helpers
from skeletons.account_helpers.settings_core import ISettingsCore
_userProps = {b'datetimeIdx': (
                  b'readInt', b'writeInt', (lambda value: value in xrange(0, 4)), False), 
   b'enableOlFilter': (
                     b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                     False), 
   b'enableSpamFilter': (
                       b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                       False), 
   b'invitesFromFriendsOnly': (
                             b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                             False), 
   b'storeReceiverInBattle': (
                            b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                            False), 
   b'disableBattleChat': (
                        b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                        False), 
   b'chatContactsListOnly': (
                           b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                           True), 
   b'receiveFriendshipRequest': (
                               b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                               False), 
   b'receiveInvitesInBattle': (
                             b'readBool', b'writeBool', (lambda value: isinstance(value, types.BooleanType)),
                             True)}

def loadDefault(xmlCtx, section, messengerSettings):
    data = {}
    for tagName, subSec in section.items():
        if tagName != b'preference':
            raise _xml_helpers.XMLError(xmlCtx, (b'Tag {0:>s} is invalid').format(tagName))
        ctx = xmlCtx.next(subSec)
        name = _xml_helpers.readNoEmptyStr(ctx, subSec, b'name', b'Preference name is not defined')
        if name not in _userProps:
            raise _xml_helpers.XMLError(ctx, (b'Preference {0:>s} is invalid').format(name))
        reader, _, validator, _ = _userProps[name]
        value = getattr(subSec, reader)(b'value')
        if validator(value):
            data[name] = value
        else:
            raise _xml_helpers.XMLError(ctx, (b'Invalid value of preference {0:>s}').format(name))

    if data:
        messengerSettings.userPrefs = messengerSettings.userPrefs._replace(**data)
    return


def loadFromServer(messengerSettings):
    from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
    data = messengerSettings.userPrefs._asdict()
    settingsCore = dependency.instance(ISettingsCore)
    core = settingsCore.serverSettings
    for key, (_, _, _, isExtended) in _userProps.iteritems():
        section = SETTINGS_SECTIONS.GAME_EXTENDED if isExtended else SETTINGS_SECTIONS.GAME
        settingValue = core.getSectionSettings(section, key, None)
        if settingValue is not None:
            data[key] = settingValue

    version = settingsCore.serverSettings.getVersion()
    if version is not None:
        data[b'version'] = version
    messengerSettings.saveUserPreferences(data)
    return


def flush(messengerSettings, data):
    oldData = messengerSettings.userPrefs._asdict()
    newData = {}
    for key, value in data.iteritems():
        if key in oldData and oldData[key] == value:
            continue
        if key in _userProps:
            newData[key] = value

    if newData:
        messengerSettings.userPrefs = messengerSettings.userPrefs._replace(**data)
    return len(newData) > 0
