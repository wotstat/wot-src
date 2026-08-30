import logging
from itertools import chain
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from gui.shared.event_dispatcher import showBattlePass, showBattlePassTankmenVoiceover, showShop
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from web.common import formatBattlePassInfo
from web.web_client_api import Field, W2CSchema, WebCommandException, w2c, w2capi
_logger = logging.getLogger(__name__)
_R_VIEWS = R.aliases.battle_pass
_VIEWS_IDS = {b'chapter_choice': (_R_VIEWS.ChapterChoice()), 
   b'progression': (_R_VIEWS.Progression())}
_VIEWS_COMMANDS = {b'voiceover': showBattlePassTankmenVoiceover}

def _isValidViewID(_, data):
    viewID = data.get(b'id')
    if viewID in chain(_VIEWS_IDS, _VIEWS_COMMANDS):
        return True
    raise WebCommandException((b'id: "{}" is not supported').format(viewID))
    return


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def _isValidChapterID(_, data, battlePass):
    chapterID = data.get(b'chapter_id')
    if chapterID in battlePass.getChapterIDs():
        return True
    raise WebCommandException((b'chapter_id: "{}" is not valid').format(chapterID))
    return


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def _isValidTankman(_, data, battlePass):
    tankmanToken = data.get(b'tankman')
    if tankmanToken in battlePass.getSpecialTankmen():
        return True
    raise WebCommandException((b'Tankman token: "{}" is not valid').format(tankmanToken))
    return


class _ShowViewSchema(W2CSchema):
    id = Field(required=False, type=basestring, validator=_isValidViewID)
    chapter_id = Field(required=False, type=int, validator=_isValidChapterID)
    tankman = Field(required=False, type=basestring, validator=_isValidTankman)


@w2capi(name=b'battle_pass', key=b'action')
class BattlePassWebApi(W2CSchema):
    __battlePass = dependency.descriptor(IBattlePassController)

    @w2c(_ShowViewSchema, name=b'show_view')
    def handleShowView(self, cmd):
        if cmd.id in _VIEWS_COMMANDS and hasattr(cmd, b'tankman'):
            showView = _VIEWS_COMMANDS[cmd.id]
            showView(self.__getTankmenScreenID(cmd.tankman))
        else:
            showBattlePass(_VIEWS_IDS.get(cmd.id), cmd.chapter_id)
        return

    @w2c(W2CSchema, name=b'get_info')
    def handleGetInfo(self, _):
        return formatBattlePassInfo()

    @w2c(W2CSchema, name=b'finish_bp_purchase')
    def finishBattlePassPurchase(self, _):
        g_eventBus.handleEvent(events.BattlePassEvent(events.BattlePassEvent.ON_FINISH_BATTLE_PASS_PURCHASE), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __getTankmenScreenID(self, groupName):
        for screenID, screenData in self.__battlePass.getTankmenScreens().iteritems():
            if groupName in screenData[b'tankmen']:
                return screenID

        return


class BattlePassWebApiMixin(object):

    @w2c(W2CSchema, b'battle_pass_common')
    def openBattlePassMainProgression(self, _):
        showBattlePass()
        return

    @w2c(W2CSchema, b'battle_pass_buy:')
    def openBattlePassMainWithBuy(self, _):
        battlePass = dependency.instance(IBattlePassController)
        view = (battlePass.isHoliday() or R.aliases.battle_pass.ChapterChoice)() if 1 else R.aliases.battle_pass.BuyPass()
        showBattlePass(view)
        return

    @w2c(W2CSchema, b'battle_pass_levels_buy:')
    def openBattlePassMainWithBuyLevels(self, _):
        battlePass = dependency.instance(IBattlePassController)
        currentChapterID = battlePass.getCurrentChapterID()
        if battlePass.hasActiveChapter() and battlePass.isBought(chapterID=currentChapterID):
            showBattlePass(R.aliases.battle_pass.BuyLevels(), currentChapterID)
        return
