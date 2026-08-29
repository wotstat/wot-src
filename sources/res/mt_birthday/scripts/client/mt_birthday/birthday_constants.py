from constants import ARENA_BONUS_TYPE
from constants_utils import ConstInjector
from messenger import m_constants
from shared_utils import CONST_CONTAINER
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.birthday_main_view_model import TabId
BIRTHDAY_STAMP_CODE = b'giftsystem_5_stamp'
BIRTHDAY_GOLDEN_TICKET = b'birthday2026_golden_ticket'
BIRTHDAY_STAMP_CODE_SPECIAL = b'giftsystem_5_stampSpecial'
BIRTHDAY_BLOGGER_TOKEN = b'birthday_26_blogger_token'
BIRTHDAY_GOLDEN_TICKET_CURRENCY = b'goldenticket'
BIRTHDAY_REPLY_GIFT_TOKEN = b'birthday_26_rg_token'
LAST_BATTLES_PLAYERS_SAVE_COUNT = 5
POST_BATTLE_EXTRA_TAB_UI = b'PostbattleExtraTabUI'
POST_BATTLE_REDEFINED_TAB_UI = b'GiftSystemTeamStatsUI'
BIRTHDAY_BLOGGER_LOOTBOX_TAG = b'bloggerLootBox'

class BirthdayLootBoxes(CONST_CONTAINER):
    LARGE = b'tanks_birthday_2026_large'
    SMALL = b'tanks_birthday_2026_small'


class AnchorNames(CONST_CONTAINER):
    GOLD_WAGON = b'GoldWagon'
    POST_OFFICE = b'PostOffice'
    QUEST_GIVER = b'QuestGiver'


CUSTOM_NOTIFICATION_NAME = b'BirthdayBonusNotification'
CUSTOM_GIFT_NOTIFICATION_NAME = b'BirthdayGiftNotification'

class GFNotificationTemplates(m_constants.GFNotificationTemplates, ConstInjector):
    CUSTOM_BIRTHDAY_GIFT_NOTIFICATION = CUSTOM_GIFT_NOTIFICATION_NAME
    CUSTOM_BIRTHDAY_BONUS_NOTIFICATION = CUSTOM_NOTIFICATION_NAME


class BirthdayStorageKeys(CONST_CONTAINER):
    MT_BIRTHDAY = b'MT_BIRTHDAY'
    BIRTHDAY_WELCOME_NOTIFICATION = b'BirthdayWelcomeNotification'
    GIFT_RECEIVED = b'GIFT_RECEIVED'
    BONUS_RECEIVED = b'BONUS_RECEIVED'
    BIRTHDAY_GENERAL_TIPS_SEEN = b'BirthdayGeneralTipsSeen'
    BIRTHDAY_MAIL_TIPS_SEEN = b'BirthdayMailTipsSeen'
    BIRTHDAY_QUEST_GIVER_TIPS_SEEN = b'BirthdayQuestGiverTipsSeen'
    BIRTHDAY_GOLD_WAGON_TIPS_SEEN = b'BirthdayGoldWagonTipsSeen'
    BIRTHDAY_TICKET_EXCHANGE_TIPS_SEEN = b'BirthdayTicketExchangeTipsSeen'


ACCOUNT_DEFAULT_SETTINGS = {(BirthdayStorageKeys.MT_BIRTHDAY): {(BirthdayStorageKeys.BIRTHDAY_WELCOME_NOTIFICATION): False, 
                                       (BirthdayStorageKeys.GIFT_RECEIVED): False, 
                                       (BirthdayStorageKeys.BONUS_RECEIVED): False, 
                                       (BirthdayStorageKeys.BIRTHDAY_GENERAL_TIPS_SEEN): False, 
                                       (BirthdayStorageKeys.BIRTHDAY_MAIL_TIPS_SEEN): False, 
                                       (BirthdayStorageKeys.BIRTHDAY_QUEST_GIVER_TIPS_SEEN): False, 
                                       (BirthdayStorageKeys.BIRTHDAY_GOLD_WAGON_TIPS_SEEN): False, 
                                       (BirthdayStorageKeys.BIRTHDAY_TICKET_EXCHANGE_TIPS_SEEN): False}}
TAB_ID_TO_ACCOUNT_SETTING = {(TabId.MAIL): (BirthdayStorageKeys.BIRTHDAY_MAIL_TIPS_SEEN), 
   (TabId.QUESTS): (BirthdayStorageKeys.BIRTHDAY_QUEST_GIVER_TIPS_SEEN), 
   (TabId.GOLD_WAGON): (BirthdayStorageKeys.BIRTHDAY_GOLD_WAGON_TIPS_SEEN), 
   (TabId.TICKET_EXCHANGE): (BirthdayStorageKeys.BIRTHDAY_TICKET_EXCHANGE_TIPS_SEEN)}
MT_BIRTHDAY_EVENT_STATE = {b'Active': b'Active', 
   b'Paused': b'Paused', 
   b'Disabled': b'Disabled'}
SUPPORTED_POST_BATTLE_BONUS_TYPES = ARENA_BONUS_TYPE.RANDOM_RANGE + (
 ARENA_BONUS_TYPE.SORTIE_2, ARENA_BONUS_TYPE.FORT_BATTLE_2)

def isBirthdayQuestGiverQuest(questID):
    return questID.startswith(b'mt_birthday_quest_giver')
