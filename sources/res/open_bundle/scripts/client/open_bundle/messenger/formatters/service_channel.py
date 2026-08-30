from __future__ import absolute_import
from future.utils import viewitems
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.recruit_helper import getRecruitInfo
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from messenger import g_settings
from messenger.formatters.service_channel import QuestAchievesFormatter

class OpenBundleAchievesFormatter(QuestAchievesFormatter):
    _BULLET = u'\u2022'

    @classmethod
    def formatData(cls, data):
        if not data:
            return b''
        result = []
        fixedRewards = g_settings.htmlTemplates.format(b'openBundleFixedReward', {b'text': (cls.formatQuestAchieves(data.get(b'fixedBonus') or {}))})
        randomBonus = cls.formatQuestAchieves(data.get(b'randomBonus') or {})
        cellRewards = g_settings.htmlTemplates.format(b'openBundleCellRewards', {b'text': randomBonus}) if randomBonus else b''
        for rewardsType in (fixedRewards, cellRewards):
            if rewardsType:
                result.append(rewardsType)

        result.append(b'')
        return cls._SEPARATOR.join(result)

    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter=False, processCustomizations=True, processTokens=True):
        result = cls.getFormattedAchieves(data, asBattleFormatter, processCustomizations, processTokens)
        if result:
            result = [(b'{} {}').format(cls._BULLET, s[len(cls._SEPARATOR):] if s.startswith(cls._SEPARATOR) else s) for s in result]
            return cls._SEPARATOR.join(result)
        else:
            return

    @classmethod
    def _processTokens(cls, tokens):
        result = []
        for token, tokenData in viewitems(tokens.get(b'tokens', {})):
            tankmanTokenResult = cls._processTankmanToken(token, tokenData)
            if tankmanTokenResult:
                result.append(tankmanTokenResult)

        return (b'{}{} ').format(cls._SEPARATOR, cls._BULLET).join(result)

    @classmethod
    def _processTankmanToken(cls, tokenName, tokenData):
        if tokenName.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
            tankmanInfo = getRecruitInfo(tokenName)
            if tankmanInfo is not None:
                groupName = tankmanInfo.getGroupName()
                if groupName == b'men1':
                    text = backport.text(R.strings.open_bundle.formatter.crew.male(), count=str(tokenData.get(b'count')))
                elif groupName == b'women1':
                    text = backport.text(R.strings.open_bundle.formatter.crew.female(), count=str(tokenData.get(b'count')))
                else:
                    text = backport.text(R.strings.open_bundle.formatter.uniqueTankman(), fullName=tankmanInfo.getFullUserName())
                return g_settings.htmlTemplates.format(b'openBundleTankman', {b'text': text})
        return
