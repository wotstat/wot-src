import itertools, logging, sys, typing
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.server_events.awards_formatters import AWARDS_SIZES
from gui.server_events.bonuses import HIDDEN_BONUSES
from gui.Scaleform.daapi.view.lobby.missions.cards_formatters import CardBattleConditionsFormatters
from gui.server_events.cond_formatters import CONDITION_SIZE
from helpers import dependency, i18n
from skeletons.gui.game_control import IMarathonEventsController
from skeletons.gui.server_events import IEventsCache
from web.web_client_api import w2c, w2capi, Field, W2CSchema
from gui.server_events.event_items import Quest
from web.web_client_api.common import sanitizeResPath
_logger = logging.getLogger(__name__)

class _QuestsSchema(W2CSchema):
    ids = Field(type=list)


class _RequestQuestBonusSchema(W2CSchema):
    quest_id_base = Field(type=basestring, default=b'')


class _RawQuestConditionsFormatters(CardBattleConditionsFormatters):
    MAX_CONDITIONS_IN_CARD = sys.maxint
    ICON_SIZE = CONDITION_SIZE.NORMAL

    def _getFormattedField(self, field):
        return i18n.makeString(*field.args)


def _formatQuestConditions(quest):
    formatter = _RawQuestConditionsFormatters()
    conditions = formatter.format(quest)
    return [{b'description': (cond[b'description']), b'title': (cond[b'title']), b'type': (cond[b'state']), b'icon': (sanitizeResPath(cond[b'icon'])), b'progress': (cond[b'progress'])} for cond in itertools.chain.from_iterable(component[b'data'] for component in conditions)]


def _formatQuestBonuses(quest):
    entries = []
    for bonus in quest.getBonuses():
        if any(isinstance(bonus, hb) for hb in HIDDEN_BONUSES):
            continue
        for item in bonus.getWrappedEpicBonusList():
            icon = {size: sanitizeResPath(path) for size, path in item.get(b'icon').iteritems()}
            entries.append({b'id': (item.get(b'id', 0)), 
               b'type': (item[b'type']), 
               b'icon': icon, 
               b'value': (item.get(b'value', 0))})

    return entries


def _questAsDict(quest):
    return {b'id': (quest.getID()), 
       b'description': (quest.getDescription()), 
       b'name': (quest.getUserName()), 
       b'conditions': (_formatQuestConditions(quest)), 
       b'bonuses': (_formatQuestBonuses(quest)), 
       b'is_completed': (quest.isCompleted()), 
       b'priority': (quest.getPriority())}


@w2capi(name=b'user_data', key=b'action')
class QuestsWebApi(W2CSchema):
    _eventsCache = dependency.descriptor(IEventsCache)
    _marathonsCtrl = dependency.descriptor(IMarathonEventsController)

    @w2c(_QuestsSchema, b'get_tokens')
    def handleGetTokens(self, command):
        tokens = self._eventsCache.questsProgress.getTokensData()
        if hasattr(command, b'ids') and command.ids:
            tokens = {k: v for k, v in tokens.iteritems() if k in command.ids}
        return {b'token_list': tokens, b'action': b'get_tokens'}

    @w2c(_QuestsSchema, b'get_quests')
    def handleGetQuests(self, command):
        if command.ids is not None:

            def filterFunc(quest):
                return quest.getID() in command.ids

        else:
            filterFunc = None
        data = {qID: _questAsDict(quest) for qID, quest in self._eventsCache.getActiveQuests(filterFunc=filterFunc).iteritems()}
        return data

    @w2c(_QuestsSchema, b'get_quests_old')
    def handleGetQuestsOld(self, command):

        def _processQuest(progressData, questData):
            data = {}
            if questData is not None:
                data.update({b'startTime': (questData.getStartTime()), 
                   b'startTimeLeft': (questData.getStartTimeLeft()), 
                   b'finishTime': (questData.getFinishTime()), 
                   b'finishTimeLeft': (questData.getFinishTimeLeft())})
            data.update(progressData)
            return data

        quests = self._eventsCache.questsProgress.getQuestsData()
        if hasattr(command, b'ids') and command.ids:
            quests = {k: v for k, v in quests.iteritems() if k in command.ids}
        quests = {k: _processQuest(v, self._eventsCache.getHiddenQuests().get(k)) for k, v in quests.items()}
        return {b'quest_list': quests, 
           b'action': b'get_quests'}

    @w2c(_QuestsSchema, b'get_step')
    def handleGetStep(self, command):
        if hasattr(command, b'custom_parameters') and b'prefix' in command.custom_parameters:
            marathon = self._marathonsCtrl.getMarathon(command.custom_parameters[b'prefix'])
            if marathon is not None:
                currentStep, allSteps = marathon.getMarathonProgress()
                return {b'current_step': currentStep, 
                   b'all_steps': allSteps}
        return

    @w2c(_RequestQuestBonusSchema, b'get_quest_descr')
    def requestQuestDescr(self, cmd):
        questInfo = {}
        questIdBase = cmd.quest_id_base
        allQuests = self._eventsCache.getAllQuests(filterFunc=(lambda q: q.getID().startswith(questIdBase)))
        for questData in allQuests.itervalues():
            questInfo[b'title'] = questData.getUserName()
            questInfo[b'description'] = questData.getDescription()
            iconKey = questData.getID().replace(questIdBase, b'').lstrip(b'_')
            if iconKey:
                questInfo[b'icon'] = {(AWARDS_SIZES.BIG): (RES_ICONS.get128ConditionIcon(iconKey)), (AWARDS_SIZES.SMALL): (RES_ICONS.get90ConditionIcon(iconKey))}
                break
        else:
            _logger.warning(b'Missing icon for quest: %s', questIdBase)

        return questInfo
