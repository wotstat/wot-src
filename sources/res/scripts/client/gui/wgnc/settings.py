class WGNC_GUI_TYPE(object):
    UNDEFINED = 0
    POP_UP = 1
    BASIC_WINDOW = 2
    COMPLEX_WINDOW = 4
    BROWSER = 8


class WGNC_DATA_PROXY_TYPE(object):
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
    INTEGRATED_AUCTION_RATE_LOST = 257
    INTEGRATED_AUCTION_RATE_BELOW_COMPETITIVE = 258
    CLAN_SUPPLY_QUEST_UPDATE = 259


WGNC_POP_UP_PRIORITIES = (b'low', b'medium', b'high')
WGNC_POP_UP_BUTTON_WIDTH = 107
WGNC_GUI_INVALID_SEQS = (
 WGNC_GUI_TYPE.UNDEFINED,
 WGNC_GUI_TYPE.BASIC_WINDOW | WGNC_GUI_TYPE.COMPLEX_WINDOW,
 WGNC_GUI_TYPE.POP_UP | WGNC_GUI_TYPE.BASIC_WINDOW | WGNC_GUI_TYPE.COMPLEX_WINDOW)
WGNC_DEFAULT_ICON = b'InformationIcon'
_WGNC_ICON_TO_LOCAL = {b'information': WGNC_DEFAULT_ICON, 
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
   b'ClanQuestNotification': b'clanQuestNotification', 
   b'rankedYearLb': b'RankedYearLB'}

def convertToLocalIcon(icon):
    result = WGNC_DEFAULT_ICON
    if icon in _WGNC_ICON_TO_LOCAL:
        result = _WGNC_ICON_TO_LOCAL[icon]
    return result


_WGNC_BG_TO_LOCAL = {b'battle_defeat': (
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
               b'BgReferral', (288, 128)), 
   b'craftmachine': (
                   b'CraftmachineBG', (288, 80)), 
   b'ClanQuestNotification': (
                            b'BgclanQuestNotification', (288, 110)), 
   b'clansupply': (
                 b'ClanSupplyQuestBG', (288, 132))}

def convertToLocalBG(icon):
    result = (
     b'', (0, 0))
    if icon in _WGNC_BG_TO_LOCAL:
        result = _WGNC_BG_TO_LOCAL[icon]
    return result
