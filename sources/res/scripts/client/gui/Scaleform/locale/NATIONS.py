from debug_utils import LOG_WARNING

class NATIONS(object):
    USSR = b'#nations:ussr'
    GERMANY = b'#nations:germany'
    USA = b'#nations:usa'
    FRANCE = b'#nations:france'
    UK = b'#nations:uk'
    JAPAN = b'#nations:japan'
    CZECH = b'#nations:czech'
    CHINA = b'#nations:china'
    POLAND = b'#nations:poland'
    SWEDEN = b'#nations:sweden'
    ITALY = b'#nations:italy'
    INTUNION = b'#nations:intunion'
    USSR_GENETIVECASE = b'#nations:ussr/genetiveCase'
    GERMANY_GENETIVECASE = b'#nations:germany/genetiveCase'
    USA_GENETIVECASE = b'#nations:usa/genetiveCase'
    CHINA_GENETIVECASE = b'#nations:china/genetiveCase'
    FRANCE_GENETIVECASE = b'#nations:france/genetiveCase'
    UK_GENETIVECASE = b'#nations:uk/genetiveCase'
    JAPAN_GENETIVECASE = b'#nations:japan/genetiveCase'
    CZECH_GENETIVECASE = b'#nations:czech/genetiveCase'
    SWEDEN_GENETIVECASE = b'#nations:sweden/genetiveCase'
    POLAND_GENETIVECASE = b'#nations:poland/genetiveCase'
    ITALY_GENETIVECASE = b'#nations:italy/genetiveCase'
    INTUNION_GENETIVECASE = b'#nations:intunion/genetiveCase'
    ALL_GENETIVECASE_ENUM = (
     USSR_GENETIVECASE,
     GERMANY_GENETIVECASE,
     USA_GENETIVECASE,
     CHINA_GENETIVECASE,
     FRANCE_GENETIVECASE,
     UK_GENETIVECASE,
     JAPAN_GENETIVECASE,
     CZECH_GENETIVECASE,
     SWEDEN_GENETIVECASE,
     POLAND_GENETIVECASE,
     ITALY_GENETIVECASE,
     INTUNION_GENETIVECASE)
    ALL_ENUM = (
     USSR,
     GERMANY,
     USA,
     FRANCE,
     UK,
     JAPAN,
     CZECH,
     CHINA,
     POLAND,
     SWEDEN,
     ITALY,
     INTUNION,
     USSR_GENETIVECASE,
     GERMANY_GENETIVECASE,
     USA_GENETIVECASE,
     CHINA_GENETIVECASE,
     FRANCE_GENETIVECASE,
     UK_GENETIVECASE,
     JAPAN_GENETIVECASE,
     CZECH_GENETIVECASE,
     SWEDEN_GENETIVECASE,
     POLAND_GENETIVECASE,
     ITALY_GENETIVECASE,
     INTUNION_GENETIVECASE)

    @classmethod
    def genetiveCase(cls, key0):
        outcome = (b'#nations:{}/genetiveCase').format(key0)
        if outcome not in cls.ALL_GENETIVECASE_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def all(cls, key0):
        outcome = (b'#nations:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
