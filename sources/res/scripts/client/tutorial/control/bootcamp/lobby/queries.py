from math import ceil
from constants import PREMIUM_ENTITLEMENTS, BootcampVersion
from gui.impl.gen import R
from gui.impl import backport
from gui.Scaleform.genConsts.BOOTCAMP_MESSAGE_ALIASES import BOOTCAMP_MESSAGE_ALIASES
from helpers import i18n, dependency, time_utils
from nations import NAMES as NATION_NAMES
from tutorial.control import ContentQuery
from tutorial.logger import LOG_ERROR
from skeletons.gui.game_control import IBootcampController
_PRESET_RENDERERS = {b'FINISH': (BOOTCAMP_MESSAGE_ALIASES.RENDERER_FIN_UI), 
   b'ORANGE': (BOOTCAMP_MESSAGE_ALIASES.RENDERER_ORANGE_UI), 
   b'BLUE': (BOOTCAMP_MESSAGE_ALIASES.RENDERER_BLUE), 
   b'GOLD': (BOOTCAMP_MESSAGE_ALIASES.RENDERER_GOLD), 
   b'INTRO': (BOOTCAMP_MESSAGE_ALIASES.RENDERER_INTRO)}
_BOTTOM_RENDERERS = {b'rewards': (BOOTCAMP_MESSAGE_ALIASES.BOTTOM_REWARDS_VIEW_UI), 
   b'buttons': (BOOTCAMP_MESSAGE_ALIASES.BOTTOM_BUTTONS_VIEW_UI)}
_BOTTOM_DATA_FIELDS = (b'label', b'icon', b'description', b'iconTooltip', b'labelTooltip', b'animationTarget', b'animationType')

class MessageDialogContentQuery(ContentQuery):
    bootcampController = dependency.descriptor(IBootcampController)

    def invoke(self, content, varID):
        content[b'messages'], content[b'voiceovers'] = map(list, zip(*(self._makeMessageData(msgContent) for msgContent in content[b'sequence'])))
        return

    def _makeMessageData(self, msgContent):
        nationsDataDict = msgContent.get(b'nations_data', None)
        if nationsDataDict is not None:
            nation = self.bootcampController.nation
            data = nationsDataDict[NATION_NAMES[nation]]
        else:
            data = msgContent[b'data']
        showBottomData = not data[b'only_first_bootcamp_bottom'] or self.bootcampController.needAwarding()
        showReferralData = self.bootcampController.isReferralEnabled()
        if self.bootcampController.needAwarding() and data.get(b'label_first_bootcamp'):
            msgLabel = data[b'label_first_bootcamp']
        else:
            msgLabel = data[b'label']
        msgData = {b'messagePreset': (_PRESET_RENDERERS[data[b'preset']]), 
           b'label': (i18n.makeString(msgLabel)), 
           b'iconPath': (data[b'icon']), 
           b'message': (i18n.makeString(data[b'text']) if showBottomData else b''), 
           b'referralDescription': (i18n.makeString(data[b'description']) if showReferralData else b''), 
           b'background': (data[b'background'])}
        voiceover = {b'voiceover': (data[b'voiceover']), b'subtitle': (data[b'subtitle'])}
        if showBottomData:
            bottomRendererID = data[b'bottom_renderer']
            if bottomRendererID:
                bottomRenderer = _BOTTOM_RENDERERS.get(bottomRendererID)
                if bottomRenderer is not None:
                    msgData[b'bottomRenderer'] = bottomRenderer
                    msgData[b'bottomData'] = []
                    for bottom in data[b'bottom']:
                        processedBottom = dict(bottom)
                        self.__preprocessBottomData(processedBottom)
                        msgData[b'bottomData'].append(processedBottom)

                else:
                    LOG_ERROR(b'invalid bottom renderer ID', bottomRendererID)
        return (
         msgData, voiceover)

    def __preprocessBottomData(self, data):
        data[b'label'] = i18n.makeString(data[b'label'])
        data[b'description'] = i18n.makeString(data[b'description'])
        self.__formatLabel(data)
        keysToRemove = [key for key in data if key not in _BOTTOM_DATA_FIELDS]
        for key in keysToRemove:
            del data[key]

        return

    def __formatLabel(self, data):
        labelFormat = data.get(b'label_format')
        if labelFormat is None:
            return
        else:
            ctx = self.bootcampController.getContext()
            if b'bonuses' not in ctx:
                return
            lessonBonuses = ctx[b'bonuses'][b'battle'][self.bootcampController.getLessonNum() - 1]
            version = self.bootcampController.version
            lastBattleField = b'last_battle_short' if version == BootcampVersion.SHORT else b'last_battle'
            lessonBonuses.update(ctx[b'bonuses'][lastBattleField][b'bonus'])
            if labelFormat == b'getCredits':
                nationId = ctx[b'nation']
                nationsData = lessonBonuses.get(b'nations', None)
                if nationsData is not None:
                    formattedValue = backport.getIntegralFormat(nationsData[NATION_NAMES[nationId]][b'credits'][b'win'][0])
                    data[b'label'] = data[b'label'].format(formattedValue)
            elif labelFormat == b'getExperience':
                nationId = ctx[b'nation']
                nationsData = lessonBonuses.get(b'nations', None)
                if nationsData is not None:
                    formattedValue = backport.getIntegralFormat(nationsData[NATION_NAMES[nationId]][b'xp'][b'win'][0])
                    data[b'label'] = data[b'label'].format(formattedValue)
            elif labelFormat == b'getGold':
                data[b'label'] = data[b'label'].format(lessonBonuses[b'gold'])
            elif labelFormat == b'getPremiumHours':
                premiumType = PREMIUM_ENTITLEMENTS.PLUS if PREMIUM_ENTITLEMENTS.PLUS in lessonBonuses else PREMIUM_ENTITLEMENTS.BASIC
                days = lessonBonuses[premiumType]
                timeInSeconds = days * time_utils.ONE_DAY
                if timeInSeconds > time_utils.ONE_DAY:
                    time = ceil(timeInSeconds / time_utils.ONE_DAY)
                    timeMetric = backport.text(R.strings.menu.header.account.premium.days())
                else:
                    time = ceil(timeInSeconds / time_utils.ONE_HOUR)
                    timeMetric = backport.text(R.strings.menu.header.account.premium.hours())
                data[b'label'] = data[b'label'].format(str(int(time)) + b' ' + timeMetric)
            elif labelFormat == b'getRepairKits':
                data[b'label'] = data[b'label'].format(lessonBonuses[b'equipment'][b'largeRepairkit'][b'count'])
            elif labelFormat == b'getFirstAid':
                data[b'label'] = data[b'label'].format(lessonBonuses[b'equipment'][b'largeMedkit'][b'count'])
            elif labelFormat == b'getFireExtinguisher':
                data[b'label'] = data[b'label'].format(lessonBonuses[b'equipment'][b'handExtinguishers'][b'count'])
            elif labelFormat == b'getOptionalDeviceLabel':
                count = 0
                for value in lessonBonuses[b'optional'].itervalues():
                    count += value[b'count']

                data[b'label'] = data[b'label'].format(count)
            return


class SubtitleDialogContentQuery(MessageDialogContentQuery):

    def _makeMessageData(self, msgContent):
        data = msgContent[b'data']
        voiceover = {b'voiceover': (data[b'voiceover']), b'subtitle': (i18n.makeString(data[b'subtitle'])), b'keypoint': b''}
        return (
         data, voiceover)


class VideoDialogContentQuery(MessageDialogContentQuery):

    def _makeMessageData(self, msgContent):
        data = msgContent[b'data']
        voiceover = {b'voiceover': b'', b'subtitle': (data[b'subtitle'])}
        return (
         data, voiceover)
