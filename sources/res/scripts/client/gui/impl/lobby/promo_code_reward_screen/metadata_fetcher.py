import logging, BigWorld, ResMgr
from BWUtil import AsyncReturn
from gui.impl.lobby.promo_code_reward_screen import RewardScreenDescr
from helpers import getClientLanguage, dependency
from shared_utils import findFirst
from skeletons.gui.lobby_context import ILobbyContext
from th_async import th_async, await_callback, th_await
_logger = logging.getLogger(__name__)

class MetadataFetcher(object):

    @staticmethod
    def get(codeId):
        codeDescr = yield th_await(MetadataFetcher.fetch(codeId))
        raise AsyncReturn(codeDescr)
        return

    @staticmethod
    @th_async()
    def fetch(codeId):
        lobbyContext = dependency.instance(ILobbyContext)
        filecache = BigWorld.player().customFilesCache
        fileserver = lobbyContext.getServerSettings().fileServer
        descriptorUrl = fileserver.getRewardScreensDescrsUrl(getClientLanguage())
        if not descriptorUrl:
            _logger.error(b'Error getting descriptor URL for promo code %s', codeId)
            raise AsyncReturn(None)
        _, content = yield await_callback(filecache.get)(descriptorUrl, headers={})
        if not content:
            _logger.error(b'Error fetching description for promo code %s', codeId)
            raise AsyncReturn(None)
        descrData = MetadataFetcher.__handleCodeDescrData(codeId, content)
        if descrData is None:
            _logger.error(b'There is not description for promo code %s', codeId)
            raise AsyncReturn(None)
        descr, title, subtitle, background, quests, questsDescr, tags = descrData
        defaultDescr = RewardScreenDescr(codeId, descr, title, subtitle, None, quests, questsDescr, tags)
        if not background:
            raise AsyncReturn(defaultDescr)
        backgroundUrl = fileserver.getRewardScreenBackgroundUrl(background)
        if not backgroundUrl:
            _logger.warning(b'Error getting decoration URL for reward screen %s', codeId)
            raise AsyncReturn(defaultDescr)
        raise AsyncReturn(RewardScreenDescr(codeId, descr, title, subtitle, backgroundUrl, quests, questsDescr, tags))
        return

    @staticmethod
    def __handleCodeDescrData(codeId, content):
        section = ResMgr.DataSection()
        section.createSectionFromString(content)
        if not section.has_key(b'root/reward_screens'):
            return
        else:
            codesSection = section[b'root/reward_screens']
            _, codeItem = findFirst((lambda (itemName, sub): itemName == b'item' and sub[b'id'].asString == codeId), codesSection.items(), default=(None, None))
            if codeItem is not None:
                codeId = codeItem[b'id'].asString
                description = codeItem.readString(b'description') if codeItem.has_key(b'description') else b''
                title = codeItem[b'title'].asString
                subtitle = codeItem.readString(b'subtitle') if codeItem.has_key(b'subtitle') else b''
                background = codeItem.readString(b'background') if codeItem.has_key(b'background') else b''
                questsStr = codeItem.readString(b'quests') if codeItem.has_key(b'quests') else b''
                quests = None
                if questsStr:
                    quests = questsStr.split(b' ')
                questsDescr = codeItem.readString(b'questsDescription') if codeItem.has_key(b'questsDescription') else b''
                tagsStr = codeItem.readString(b'tags') if codeItem.has_key(b'tags') else b''
                tags = None
                if tagsStr:
                    tags = tagsStr.split(b' ')
                return (description, title, subtitle, background, quests, questsDescr, tags)
            return
