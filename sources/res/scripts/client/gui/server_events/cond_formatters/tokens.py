from collections import namedtuple
from gui.server_events.cond_formatters.formatters import ConditionFormatter, ConditionsFormatter
from gui.server_events.formatters import TOKEN_SIZES
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from soft_exception import SoftException
_PreFormattedTokenCondition = namedtuple(b'_PreFormattedTokenCondition', b'tokenID, styleID, eventID, needCount')

class PreFormattedTokenCondition(_PreFormattedTokenCondition):
    eventsCache = dependency.descriptor(IEventsCache)

    @property
    def gotCount(self):
        return self.eventsCache.questsProgress.getTokenCount(self.tokenID)

    @property
    def title(self):
        title = self.eventsCache.prefetcher.getTokenInfo(self.styleID)
        return title

    def getCounterText(self):
        if self.gotCount == self.needCount:
            tokensGot = text_styles.bonusAppliedText(self.gotCount)
        else:
            tokensGot = text_styles.stats(self.gotCount)
        tokensNeed = text_styles.standard(self.needCount)
        return text_styles.disabled((b'{} / {}').format(tokensGot, tokensNeed))

    def getImage(self, size):
        return self.eventsCache.prefetcher.getTokenImage(self.styleID, size)


class TokenConditionFormatter(ConditionFormatter):

    def format(self, condition, event):
        needCount = condition.getNeededCount()
        styleID = condition.getStyleID()
        tokenId = condition.getID()
        return [PreFormattedTokenCondition(tokenId, styleID, event.getID(), needCount)]


class TokensConditionFormatter(ConditionsFormatter):

    def __init__(self):
        super(TokensConditionFormatter, self).__init__({b'token': (TokenConditionFormatter())})
        return

    def format(self, conditions, event):
        result = []
        tokenConditions = conditions.getTokens()
        for condition in tokenConditions:
            if condition.isDisplayable():
                fmt = self.getConditionFormatter(condition.getName())
                result.extend(fmt.format(condition, event))

        return result

    def _packCondition(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _getFormattedField(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _packConditions(self, *args, **kwargs):
        raise SoftException(b'This method should not be reached in this context')
        return


class TokensMarathonFormatter(object):
    BIG_ICONS_COUNT = 2

    def __init__(self):
        self.__tokensConditionsFormatter = TokensConditionFormatter()
        return

    def format(self, event):
        result = []
        preFormattedTokenConditions = self.__tokensConditionsFormatter.format(event.accountReqs, event)
        isNormalSize = len(preFormattedTokenConditions) > self.BIG_ICONS_COUNT
        size = TOKEN_SIZES.MEDIUM if isNormalSize else TOKEN_SIZES.BIG
        for preFormattedCondition in preFormattedTokenConditions:
            result.append({b'tokenId': (preFormattedCondition.tokenID), 
               b'questId': (preFormattedCondition.eventID), 
               b'isNormalSize': isNormalSize, 
               b'imgSrc': (preFormattedCondition.getImage(size)), 
               b'countText': (preFormattedCondition.getCounterText())})

        return result
