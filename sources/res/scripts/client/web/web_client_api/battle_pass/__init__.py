import logging
from gui.impl.gen import R
from gui.server_events.events_dispatcher import showMissionsBattlePass
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from web.common import formatBattlePassInfo
from web.web_client_api import Field, W2CSchema, WebCommandException, w2c, w2capi
_logger = logging.getLogger(__name__)
_R_VIEWS = R.views.lobby.battle_pass
_VIEWS_IDS = {b'intro': (_R_VIEWS.BattlePassIntroView()), 
   b'chapter_choice': (_R_VIEWS.ChapterChoiceView()), 
   b'progression': (_R_VIEWS.BattlePassProgressionsView())}

def _isValidViewID(_, data):
    viewID = data.get(b'id')
    if viewID in _VIEWS_IDS:
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


class _ShowViewSchema(W2CSchema):
    id = Field(required=False, type=basestring, validator=_isValidViewID)
    chapter_id = Field(required=False, type=int, validator=_isValidChapterID)


@w2capi(name=b'battle_pass', key=b'action')
class BattlePassWebApi(W2CSchema):
    __battlePass = dependency.descriptor(IBattlePassController)

    @w2c(_ShowViewSchema, name=b'show_view')
    def handleShowView(self, cmd):
        showMissionsBattlePass(_VIEWS_IDS.get(cmd.id), cmd.chapter_id)
        return

    @w2c(W2CSchema, name=b'get_info')
    def handleGetInfo(self, _):
        return formatBattlePassInfo()
