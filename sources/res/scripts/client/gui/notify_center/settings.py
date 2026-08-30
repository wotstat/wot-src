class NOTIFY_CENTER_GUI_TYPE(object):
    UNDEFINED = 0
    POP_UP = 1
    BASIC_WINDOW = 2
    COMPLEX_WINDOW = 4
    BROWSER = 8


class NOTIFY_CENTER_DATA_PROXY_TYPE(object):
    UNDEFINED = 0
    CLAN_APP = 1
    CLAN_INVITE = 2
    CLAN_APP_DECLINED = 4
    CLAN_APP_ACCEPTED = 8
    SHOW_IN_BROWSER = 11
    CLAN_INVITE_ACCEPTED = 16
    CLAN_INVITE_DECLINED = 18
    CLAN_INVITES_CREATED = 20
    CLAN_APP_DECLINED_FOR_MEMBERS = 24
    CLAN_APP_ACCEPTED_FOR_MEMBERS = 32
    SHOW_PROMO_TEASER = 64
    UPDATE_REFERRAL_BUBBLE = 80
    BECOME_RECRUITER = 81
    SHOW_REFERRAL_WINDOW = 82
    UPDATE_CLAN_NOTIFICATION = 96
    PAYMENT_METHOD_CHANGE_NOTIFICATION = 128
    MAPBOX_SURVEY_AVAILABLE_NOTIFICATION = 144
    MAPBOX_EVENT_STARTED_NOTIFICATION = 145
    MAPBOX_EVENT_ENDED_NOTIFICATION = 146
    MAPBOX_REWARD_RECEIVED_NOTIFICATION = 148
    INTEGRATED_AUCTION_RATE_ERROR = 256
    INTEGRATED_AUCTION_RESULT = 257
    INTEGRATED_AUCTION_RATE_BELOW_COMPETITIVE = 258


NOTIFY_CENTER_POP_UP_PRIORITIES = (b'low', b'medium', b'high')
NOTIFY_CENTER_POP_UP_BUTTON_WIDTH = 107
NOTIFY_CENTER_GUI_INVALID_SEQS = (
 NOTIFY_CENTER_GUI_TYPE.UNDEFINED,
 NOTIFY_CENTER_GUI_TYPE.BASIC_WINDOW | NOTIFY_CENTER_GUI_TYPE.COMPLEX_WINDOW,
 NOTIFY_CENTER_GUI_TYPE.POP_UP | NOTIFY_CENTER_GUI_TYPE.BASIC_WINDOW | NOTIFY_CENTER_GUI_TYPE.COMPLEX_WINDOW)
NOTIFY_CENTER_DEFAULT_ICON = b'InformationIcon'
_NOTIFY_CENTER_ICON_TO_LOCAL = {b'information': NOTIFY_CENTER_DEFAULT_ICON, 
   b'gold': b'GoldIcon', 
   b'text_message': b'MessageIcon', 
   b'offerIcon': b'OfferIcon', 
   b'gratzIcon': b'PersonalAchievementsIcon', 
   b'eventIcon': b'EventIcon', 
   b'shBattleResult': b'FortBattleResult', 
   b'sally_result': b'SallyResult', 
   b'sh_resource': b'FortResource', 
   b'hands': b'hands', 
   b'handsOff': b'handsOff', 
   b'handsPlus': b'handsPlus', 
   b'box': b'referralCoin', 
   b'craftmachine_resource': b'craftmachineResource', 
   b'ClanQuestNotification': b'ClanQuestNotification', 
   b'rankedYearLb': b'RankedYearLB', 
   b'error': b'ErrorIcon', 
   b'sprintEvent': b'SprintEventIcon', 
   b'warningIcon': b'WarningIcon'}

def convertToLocalIcon(icon):
    result = NOTIFY_CENTER_DEFAULT_ICON
    if icon in _NOTIFY_CENTER_ICON_TO_LOCAL:
        result = _NOTIFY_CENTER_ICON_TO_LOCAL[icon]
    return result


_NOTIFY_CENTER_BG_TO_LOCAL = {b'battle_defeat': (
                    b'BgBattleResultIconDefeat', (288, 167)), 
   b'battle_draw': (
                  b'BgBattleResultIconDraw', (288, 167)), 
   b'battle_victory': (
                     b'BgBattleResultIconVictory', (288, 167)), 
   b'sh_battle_defeat': (
                       b'FortBattleDefeatBg', (312, 170)), 
   b'sh_battle_draw': (
                     b'FortBattleDrawBg', (312, 170)), 
   b'sh_battle_victory': (
                        b'FortBattleVictoryBg', (312, 170)), 
   b'sh_sally_result': (
                      b'SallyResultBg', (312, 170)), 
   b'poll': (
           b'BgPoll', (288, 110)), 
   b'offer': (
            b'OfferIconBg', (288, 110)), 
   b'event': (
            b'EventIconBg', (288, 110)), 
   b'referral': (
               b'BgReferral', (288, 167)), 
   b'craftmachine': (
                   b'CraftmachineBG', (288, 80)), 
   b'ClanQuestNotification': (
                            b'BgClanQuestNotification', (288, 110))}

def convertToLocalBG(icon):
    result = (
     b'', (0, 0))
    if icon in _NOTIFY_CENTER_BG_TO_LOCAL:
        result = _NOTIFY_CENTER_BG_TO_LOCAL[icon]
    return result
