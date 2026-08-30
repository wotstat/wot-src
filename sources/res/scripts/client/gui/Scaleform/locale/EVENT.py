from debug_utils import LOG_WARNING

class EVENT(object):
    PUNISHMENTWINDOW_REASON_EVENT_DESERTER = b'#event:punishmentWindow/reason/event_deserter'
    PUNISHMENTWINDOW_REASON_EVENT_AFK = b'#event:punishmentWindow/reason/event_afk'
    BATTLEHINTS_TESTMESSAGE = b'#event:battleHints/testMessage'
    BATTLEHINTS_TESTMESSAGEWITHPARAMS = b'#event:battleHints/testMessageWithParams'
    ALL_ENUM = (
     PUNISHMENTWINDOW_REASON_EVENT_DESERTER,
     PUNISHMENTWINDOW_REASON_EVENT_AFK,
     BATTLEHINTS_TESTMESSAGE,
     BATTLEHINTS_TESTMESSAGEWITHPARAMS)

    @classmethod
    def all(cls, key0):
        outcome = (b'#event:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
