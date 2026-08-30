from debug_utils import LOG_WARNING

class READABLE_KEY_NAMES(object):
    KEY_NONE = b'#readable_key_names:KEY_NONE'
    KEY_NONE_ALT = b'#readable_key_names:KEY_NONE_ALT'
    KEY_ESCAPE = b'#readable_key_names:KEY_ESCAPE'
    KEY_1 = b'#readable_key_names:KEY_1'
    KEY_2 = b'#readable_key_names:KEY_2'
    KEY_3 = b'#readable_key_names:KEY_3'
    KEY_4 = b'#readable_key_names:KEY_4'
    KEY_5 = b'#readable_key_names:KEY_5'
    KEY_6 = b'#readable_key_names:KEY_6'
    KEY_7 = b'#readable_key_names:KEY_7'
    KEY_8 = b'#readable_key_names:KEY_8'
    KEY_9 = b'#readable_key_names:KEY_9'
    KEY_0 = b'#readable_key_names:KEY_0'
    KEY_MINUS = b'#readable_key_names:KEY_MINUS'
    KEY_EQUALS = b'#readable_key_names:KEY_EQUALS'
    KEY_BACKSPACE = b'#readable_key_names:KEY_BACKSPACE'
    KEY_TAB = b'#readable_key_names:KEY_TAB'
    KEY_Q = b'#readable_key_names:KEY_Q'
    KEY_W = b'#readable_key_names:KEY_W'
    KEY_E = b'#readable_key_names:KEY_E'
    KEY_R = b'#readable_key_names:KEY_R'
    KEY_T = b'#readable_key_names:KEY_T'
    KEY_Y = b'#readable_key_names:KEY_Y'
    KEY_U = b'#readable_key_names:KEY_U'
    KEY_I = b'#readable_key_names:KEY_I'
    KEY_O = b'#readable_key_names:KEY_O'
    KEY_P = b'#readable_key_names:KEY_P'
    KEY_LBRACKET = b'#readable_key_names:KEY_LBRACKET'
    KEY_RBRACKET = b'#readable_key_names:KEY_RBRACKET'
    KEY_RETURN = b'#readable_key_names:KEY_RETURN'
    KEY_LCONTROL = b'#readable_key_names:KEY_LCONTROL'
    KEY_A = b'#readable_key_names:KEY_A'
    KEY_S = b'#readable_key_names:KEY_S'
    KEY_D = b'#readable_key_names:KEY_D'
    KEY_F = b'#readable_key_names:KEY_F'
    KEY_G = b'#readable_key_names:KEY_G'
    KEY_H = b'#readable_key_names:KEY_H'
    KEY_J = b'#readable_key_names:KEY_J'
    KEY_K = b'#readable_key_names:KEY_K'
    KEY_L = b'#readable_key_names:KEY_L'
    KEY_SEMICOLON = b'#readable_key_names:KEY_SEMICOLON'
    KEY_APOSTROPHE = b'#readable_key_names:KEY_APOSTROPHE'
    KEY_GRAVE = b'#readable_key_names:KEY_GRAVE'
    KEY_LSHIFT = b'#readable_key_names:KEY_LSHIFT'
    KEY_BACKSLASH = b'#readable_key_names:KEY_BACKSLASH'
    KEY_Z = b'#readable_key_names:KEY_Z'
    KEY_X = b'#readable_key_names:KEY_X'
    KEY_C = b'#readable_key_names:KEY_C'
    KEY_V = b'#readable_key_names:KEY_V'
    KEY_B = b'#readable_key_names:KEY_B'
    KEY_N = b'#readable_key_names:KEY_N'
    KEY_M = b'#readable_key_names:KEY_M'
    KEY_COMMA = b'#readable_key_names:KEY_COMMA'
    KEY_PERIOD = b'#readable_key_names:KEY_PERIOD'
    KEY_SLASH = b'#readable_key_names:KEY_SLASH'
    KEY_RSHIFT = b'#readable_key_names:KEY_RSHIFT'
    KEY_NUMPADSTAR = b'#readable_key_names:KEY_NUMPADSTAR'
    KEY_LALT = b'#readable_key_names:KEY_LALT'
    KEY_SPACE = b'#readable_key_names:KEY_SPACE'
    KEY_CAPSLOCK = b'#readable_key_names:KEY_CAPSLOCK'
    KEY_F1 = b'#readable_key_names:KEY_F1'
    KEY_F2 = b'#readable_key_names:KEY_F2'
    KEY_F3 = b'#readable_key_names:KEY_F3'
    KEY_F4 = b'#readable_key_names:KEY_F4'
    KEY_F5 = b'#readable_key_names:KEY_F5'
    KEY_F6 = b'#readable_key_names:KEY_F6'
    KEY_F7 = b'#readable_key_names:KEY_F7'
    KEY_F8 = b'#readable_key_names:KEY_F8'
    KEY_F9 = b'#readable_key_names:KEY_F9'
    KEY_F10 = b'#readable_key_names:KEY_F10'
    KEY_NUMLOCK = b'#readable_key_names:KEY_NUMLOCK'
    KEY_SCROLL = b'#readable_key_names:KEY_SCROLL'
    KEY_NUMPAD7 = b'#readable_key_names:KEY_NUMPAD7'
    KEY_NUMPAD8 = b'#readable_key_names:KEY_NUMPAD8'
    KEY_NUMPAD9 = b'#readable_key_names:KEY_NUMPAD9'
    KEY_NUMPADMINUS = b'#readable_key_names:KEY_NUMPADMINUS'
    KEY_NUMPAD4 = b'#readable_key_names:KEY_NUMPAD4'
    KEY_NUMPAD5 = b'#readable_key_names:KEY_NUMPAD5'
    KEY_NUMPAD6 = b'#readable_key_names:KEY_NUMPAD6'
    KEY_ADD = b'#readable_key_names:KEY_ADD'
    KEY_NUMPAD1 = b'#readable_key_names:KEY_NUMPAD1'
    KEY_NUMPAD2 = b'#readable_key_names:KEY_NUMPAD2'
    KEY_NUMPAD3 = b'#readable_key_names:KEY_NUMPAD3'
    KEY_NUMPAD0 = b'#readable_key_names:KEY_NUMPAD0'
    KEY_NUMPADPERIOD = b'#readable_key_names:KEY_NUMPADPERIOD'
    KEY_OEM_102 = b'#readable_key_names:KEY_OEM_102'
    KEY_F11 = b'#readable_key_names:KEY_F11'
    KEY_F12 = b'#readable_key_names:KEY_F12'
    KEY_F13 = b'#readable_key_names:KEY_F13'
    KEY_F14 = b'#readable_key_names:KEY_F14'
    KEY_F15 = b'#readable_key_names:KEY_F15'
    KEY_KANA = b'#readable_key_names:KEY_KANA'
    KEY_ABNT_C1 = b'#readable_key_names:KEY_ABNT_C1'
    KEY_CONVERT = b'#readable_key_names:KEY_CONVERT'
    KEY_NOCONVERT = b'#readable_key_names:KEY_NOCONVERT'
    KEY_YEN = b'#readable_key_names:KEY_YEN'
    KEY_ABNT_C2 = b'#readable_key_names:KEY_ABNT_C2'
    KEY_NUMPADEQUALS = b'#readable_key_names:KEY_NUMPADEQUALS'
    KEY_PREVTRACK = b'#readable_key_names:KEY_PREVTRACK'
    KEY_AT = b'#readable_key_names:KEY_AT'
    KEY_COLON = b'#readable_key_names:KEY_COLON'
    KEY_UNDERLINE = b'#readable_key_names:KEY_UNDERLINE'
    KEY_KANJI = b'#readable_key_names:KEY_KANJI'
    KEY_STOP = b'#readable_key_names:KEY_STOP'
    KEY_AX = b'#readable_key_names:KEY_AX'
    KEY_UNLABELED = b'#readable_key_names:KEY_UNLABELED'
    KEY_NEXTTRACK = b'#readable_key_names:KEY_NEXTTRACK'
    KEY_ENTER = b'#readable_key_names:KEY_ENTER'
    KEY_NUMPADENTER = b'#readable_key_names:KEY_NUMPADENTER'
    KEY_RCONTROL = b'#readable_key_names:KEY_RCONTROL'
    KEY_MUTE = b'#readable_key_names:KEY_MUTE'
    KEY_CALCULATOR = b'#readable_key_names:KEY_CALCULATOR'
    KEY_PLAYPAUSE = b'#readable_key_names:KEY_PLAYPAUSE'
    KEY_MEDIASTOP = b'#readable_key_names:KEY_MEDIASTOP'
    KEY_VOLUMEDOWN = b'#readable_key_names:KEY_VOLUMEDOWN'
    KEY_VOLUMEUP = b'#readable_key_names:KEY_VOLUMEUP'
    KEY_WEBHOME = b'#readable_key_names:KEY_WEBHOME'
    KEY_NUMPADCOMMA = b'#readable_key_names:KEY_NUMPADCOMMA'
    KEY_NUMPADSLASH = b'#readable_key_names:KEY_NUMPADSLASH'
    KEY_SYSRQ = b'#readable_key_names:KEY_SYSRQ'
    KEY_RALT = b'#readable_key_names:KEY_RALT'
    KEY_PAUSE = b'#readable_key_names:KEY_PAUSE'
    KEY_HOME = b'#readable_key_names:KEY_HOME'
    KEY_UPARROW = b'#readable_key_names:KEY_UPARROW'
    KEY_PGUP = b'#readable_key_names:KEY_PGUP'
    KEY_LEFTARROW = b'#readable_key_names:KEY_LEFTARROW'
    KEY_RIGHTARROW = b'#readable_key_names:KEY_RIGHTARROW'
    KEY_END = b'#readable_key_names:KEY_END'
    KEY_DOWNARROW = b'#readable_key_names:KEY_DOWNARROW'
    KEY_PGDN = b'#readable_key_names:KEY_PGDN'
    KEY_INSERT = b'#readable_key_names:KEY_INSERT'
    KEY_DELETE = b'#readable_key_names:KEY_DELETE'
    KEY_LWIN = b'#readable_key_names:KEY_LWIN'
    KEY_RWIN = b'#readable_key_names:KEY_RWIN'
    KEY_APPS = b'#readable_key_names:KEY_APPS'
    KEY_POWER = b'#readable_key_names:KEY_POWER'
    KEY_SLEEP = b'#readable_key_names:KEY_SLEEP'
    KEY_WAKE = b'#readable_key_names:KEY_WAKE'
    KEY_WEBSEARCH = b'#readable_key_names:KEY_WEBSEARCH'
    KEY_WEBFAVORITES = b'#readable_key_names:KEY_WEBFAVORITES'
    KEY_WEBREFRESH = b'#readable_key_names:KEY_WEBREFRESH'
    KEY_WEBSTOP = b'#readable_key_names:KEY_WEBSTOP'
    KEY_WEBFORWARD = b'#readable_key_names:KEY_WEBFORWARD'
    KEY_WEBBACK = b'#readable_key_names:KEY_WEBBACK'
    KEY_MYCOMPUTER = b'#readable_key_names:KEY_MYCOMPUTER'
    KEY_MAIL = b'#readable_key_names:KEY_MAIL'
    KEY_MEDIASELECT = b'#readable_key_names:KEY_MEDIASELECT'
    KEY_MOUSE0 = b'#readable_key_names:KEY_MOUSE0'
    KEY_LEFTMOUSE = b'#readable_key_names:KEY_LEFTMOUSE'
    KEY_MOUSE1 = b'#readable_key_names:KEY_MOUSE1'
    KEY_RIGHTMOUSE = b'#readable_key_names:KEY_RIGHTMOUSE'
    KEY_MOUSE2 = b'#readable_key_names:KEY_MOUSE2'
    KEY_MIDDLEMOUSE = b'#readable_key_names:KEY_MIDDLEMOUSE'
    KEY_MOUSE3 = b'#readable_key_names:KEY_MOUSE3'
    KEY_MOUSE4 = b'#readable_key_names:KEY_MOUSE4'
    KEY_MOUSE5 = b'#readable_key_names:KEY_MOUSE5'
    KEY_MOUSE6 = b'#readable_key_names:KEY_MOUSE6'
    KEY_MOUSE7 = b'#readable_key_names:KEY_MOUSE7'
    KEY_JOYDUP = b'#readable_key_names:KEY_JOYDUP'
    KEY_JOYDDOWN = b'#readable_key_names:KEY_JOYDDOWN'
    KEY_JOYDLEFT = b'#readable_key_names:KEY_JOYDLEFT'
    KEY_JOYDRIGHT = b'#readable_key_names:KEY_JOYDRIGHT'
    KEY_JOYSTART = b'#readable_key_names:KEY_JOYSTART'
    KEY_JOYBACK = b'#readable_key_names:KEY_JOYBACK'
    KEY_JOYALPUSH = b'#readable_key_names:KEY_JOYALPUSH'
    KEY_JOYARPUSH = b'#readable_key_names:KEY_JOYARPUSH'
    KEY_JOYA = b'#readable_key_names:KEY_JOYA'
    KEY_JOYB = b'#readable_key_names:KEY_JOYB'
    KEY_JOYX = b'#readable_key_names:KEY_JOYX'
    KEY_JOYY = b'#readable_key_names:KEY_JOYY'
    KEY_JOYBLACK = b'#readable_key_names:KEY_JOYBLACK'
    KEY_JOYWHITE = b'#readable_key_names:KEY_JOYWHITE'
    KEY_JOYLTRIGGER = b'#readable_key_names:KEY_JOYLTRIGGER'
    KEY_JOYRTRIGGER = b'#readable_key_names:KEY_JOYRTRIGGER'
    KEY_JOYALUP = b'#readable_key_names:KEY_JOYALUP'
    KEY_JOYALDOWN = b'#readable_key_names:KEY_JOYALDOWN'
    KEY_JOYALLEFT = b'#readable_key_names:KEY_JOYALLEFT'
    KEY_JOYALRIGHT = b'#readable_key_names:KEY_JOYALRIGHT'
    KEY_DEBUG = b'#readable_key_names:KEY_DEBUG'
    KEY_LCDKB_LEFT = b'#readable_key_names:KEY_LCDKB_LEFT'
    KEY_LCDKB_RIGHT = b'#readable_key_names:KEY_LCDKB_RIGHT'
    KEY_LCDKB_OK = b'#readable_key_names:KEY_LCDKB_OK'
    KEY_LCDKB_CANCEL = b'#readable_key_names:KEY_LCDKB_CANCEL'
    KEY_LCDKB_UP = b'#readable_key_names:KEY_LCDKB_UP'
    KEY_LCDKB_DOWN = b'#readable_key_names:KEY_LCDKB_DOWN'
    KEY_LCDKB_MENU = b'#readable_key_names:KEY_LCDKB_MENU'
    KEY_IME_CHAR = b'#readable_key_names:KEY_IME_CHAR'
    KEY_ENUM = (
     KEY_NONE,
     KEY_NONE_ALT,
     KEY_ESCAPE,
     KEY_1,
     KEY_2,
     KEY_3,
     KEY_4,
     KEY_5,
     KEY_6,
     KEY_7,
     KEY_8,
     KEY_9,
     KEY_0,
     KEY_MINUS,
     KEY_EQUALS,
     KEY_BACKSPACE,
     KEY_TAB,
     KEY_Q,
     KEY_W,
     KEY_E,
     KEY_R,
     KEY_T,
     KEY_Y,
     KEY_U,
     KEY_I,
     KEY_O,
     KEY_P,
     KEY_LBRACKET,
     KEY_RBRACKET,
     KEY_RETURN,
     KEY_LCONTROL,
     KEY_A,
     KEY_S,
     KEY_D,
     KEY_F,
     KEY_G,
     KEY_H,
     KEY_J,
     KEY_K,
     KEY_L,
     KEY_SEMICOLON,
     KEY_APOSTROPHE,
     KEY_GRAVE,
     KEY_LSHIFT,
     KEY_BACKSLASH,
     KEY_Z,
     KEY_X,
     KEY_C,
     KEY_V,
     KEY_B,
     KEY_N,
     KEY_M,
     KEY_COMMA,
     KEY_PERIOD,
     KEY_SLASH,
     KEY_RSHIFT,
     KEY_NUMPADSTAR,
     KEY_LALT,
     KEY_SPACE,
     KEY_CAPSLOCK,
     KEY_F1,
     KEY_F2,
     KEY_F3,
     KEY_F4,
     KEY_F5,
     KEY_F6,
     KEY_F7,
     KEY_F8,
     KEY_F9,
     KEY_F10,
     KEY_NUMLOCK,
     KEY_SCROLL,
     KEY_NUMPAD7,
     KEY_NUMPAD8,
     KEY_NUMPAD9,
     KEY_NUMPADMINUS,
     KEY_NUMPAD4,
     KEY_NUMPAD5,
     KEY_NUMPAD6,
     KEY_ADD,
     KEY_NUMPAD1,
     KEY_NUMPAD2,
     KEY_NUMPAD3,
     KEY_NUMPAD0,
     KEY_NUMPADPERIOD,
     KEY_OEM_102,
     KEY_F11,
     KEY_F12,
     KEY_F13,
     KEY_F14,
     KEY_F15,
     KEY_KANA,
     KEY_ABNT_C1,
     KEY_CONVERT,
     KEY_NOCONVERT,
     KEY_YEN,
     KEY_ABNT_C2,
     KEY_NUMPADEQUALS,
     KEY_PREVTRACK,
     KEY_AT,
     KEY_COLON,
     KEY_UNDERLINE,
     KEY_KANJI,
     KEY_STOP,
     KEY_AX,
     KEY_UNLABELED,
     KEY_NEXTTRACK,
     KEY_ENTER,
     KEY_NUMPADENTER,
     KEY_RCONTROL,
     KEY_MUTE,
     KEY_CALCULATOR,
     KEY_PLAYPAUSE,
     KEY_MEDIASTOP,
     KEY_VOLUMEDOWN,
     KEY_VOLUMEUP,
     KEY_WEBHOME,
     KEY_NUMPADCOMMA,
     KEY_NUMPADSLASH,
     KEY_SYSRQ,
     KEY_RALT,
     KEY_PAUSE,
     KEY_HOME,
     KEY_UPARROW,
     KEY_PGUP,
     KEY_LEFTARROW,
     KEY_RIGHTARROW,
     KEY_END,
     KEY_DOWNARROW,
     KEY_PGDN,
     KEY_INSERT,
     KEY_DELETE,
     KEY_LWIN,
     KEY_RWIN,
     KEY_APPS,
     KEY_POWER,
     KEY_SLEEP,
     KEY_WAKE,
     KEY_WEBSEARCH,
     KEY_WEBFAVORITES,
     KEY_WEBREFRESH,
     KEY_WEBSTOP,
     KEY_WEBFORWARD,
     KEY_WEBBACK,
     KEY_MYCOMPUTER,
     KEY_MAIL,
     KEY_MEDIASELECT,
     KEY_MOUSE0,
     KEY_LEFTMOUSE,
     KEY_MOUSE1,
     KEY_RIGHTMOUSE,
     KEY_MOUSE2,
     KEY_MIDDLEMOUSE,
     KEY_MOUSE3,
     KEY_MOUSE4,
     KEY_MOUSE5,
     KEY_MOUSE6,
     KEY_MOUSE7,
     KEY_JOYDUP,
     KEY_JOYDDOWN,
     KEY_JOYDLEFT,
     KEY_JOYDRIGHT,
     KEY_JOYSTART,
     KEY_JOYBACK,
     KEY_JOYALPUSH,
     KEY_JOYARPUSH,
     KEY_JOYA,
     KEY_JOYB,
     KEY_JOYX,
     KEY_JOYY,
     KEY_JOYBLACK,
     KEY_JOYWHITE,
     KEY_JOYLTRIGGER,
     KEY_JOYRTRIGGER,
     KEY_JOYALUP,
     KEY_JOYALDOWN,
     KEY_JOYALLEFT,
     KEY_JOYALRIGHT,
     KEY_DEBUG,
     KEY_LCDKB_LEFT,
     KEY_LCDKB_RIGHT,
     KEY_LCDKB_OK,
     KEY_LCDKB_CANCEL,
     KEY_LCDKB_UP,
     KEY_LCDKB_DOWN,
     KEY_LCDKB_MENU,
     KEY_IME_CHAR)

    @classmethod
    def key(cls, bwKey):
        outcome = (b'#readable_key_names:KEY_{}').format(bwKey)
        if outcome not in cls.KEY_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
