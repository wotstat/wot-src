import json, BigWorld, Settings, constants
from predefined_hosts import AUTO_LOGIN_QUERY_URL
from debug_utils import LOG_DEBUG, LOG_WARNING
from gui import GUI_SETTINGS
if GUI_SETTINGS.cryptLoginInfo:

    def _crypt(data):
        return BigWorld.cpdata(data)


    def _decrypt(data):
        return BigWorld.ucpdata(data)


else:

    def _crypt(data):
        return data


    def _decrypt(data):
        return data


def _LOG_PERSONAL_DATA(msg, *kargs, **kwargs):
    if constants.IS_DEVELOPMENT:
        LOG_DEBUG(msg, *kargs, **kwargs)
    return


class Preferences(dict):

    def __init__(self):
        dict.__init__(self)
        self.__oldFormat = False
        preferences = Settings.g_instance.userPrefs
        if not preferences.has_key(Settings.KEY_LOGIN_INFO):
            preferences.write(Settings.KEY_LOGIN_INFO, b'')
        elif preferences[Settings.KEY_LOGIN_INFO].readString(b'login', b''):
            self.__oldFormat = True
            self.__readOldPreferencesFormat(preferences[Settings.KEY_LOGIN_INFO])
            _LOG_PERSONAL_DATA((b'Read old format preferences: {0}').format(self))
        else:
            try:
                loginInfo = json.loads(_decrypt(preferences[Settings.KEY_LOGIN_INFO].readString(b'data', b'')), encoding=b'utf-8')
                self.update(loginInfo)
                _LOG_PERSONAL_DATA((b'Read login info from preferences.xml: {0}').format(self))
            except ValueError:
                LOG_WARNING(b'Ignoring login info from preferences.xml')

        self.__invalidateSettingsSanity()
        return

    def writeLoginInfo(self):
        _LOG_PERSONAL_DATA((b'Wrote login info into preferences.xml: {0}').format(self))
        if self.__oldFormat:
            Settings.g_instance.userPrefs.deleteSection(Settings.KEY_LOGIN_INFO)
            Settings.g_instance.userPrefs.write(Settings.KEY_LOGIN_INFO, b'')
            self.__oldFormat = False
        Settings.g_instance.userPrefs[Settings.KEY_LOGIN_INFO].writeString(b'data', _crypt(json.dumps(dict(self), encoding=b'utf-8')))
        return

    def __invalidateSettingsSanity(self):
        if not GUI_SETTINGS.rememberPassVisible:
            self[b'remember_user'] = False
            self[b'token2'] = b''
            self[b'password_length'] = 0
        return

    def __readOldPreferencesFormat(self, loginInfo):
        self[b'login'] = BigWorld.ucpdata(loginInfo.readString(b'login', b''))
        self[b'remember_user'] = loginInfo.readBool(b'rememberPwd', False)
        if self[b'remember_user']:
            pwdLengthToken2 = BigWorld.ucpdata(loginInfo.readString(b'token2'))
            if pwdLengthToken2:
                self[b'password_length'] = int(pwdLengthToken2.split(b':')[0])
                self[b'token2'] = pwdLengthToken2.split(b':', 1)[1]
        lastLoginType = loginInfo.readString(b'lastLoginType', b'basic')
        if lastLoginType == b'basic':
            lastLoginType = b'credentials'
        self[b'login_type'] = lastLoginType
        self[b'session'] = BigWorld.cpsalt(loginInfo.readString(b'salt', b''))
        self[b'name'] = loginInfo.readString(b'user', b'')
        return

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            if key == b'remember_user':
                return False
            if key == b'server_name':
                return AUTO_LOGIN_QUERY_URL
            if key == b'login_type':
                return b'credentials'
            if key == b'password_length':
                return 0
            if key == b'server_select_was_set':
                return False
            return b''

        return

    def __repr__(self):
        noNeedToKnow = (b'login', b'password_length')
        magic = lambda k, v: (k, v if k not in noNeedToKnow else b'*' * len(str(v)))
        filtered = dict(magic(k, v) for k, v in self.iteritems())
        return (b'<{} {}>').format(type(self).__name__, dict.__repr__(filtered))
