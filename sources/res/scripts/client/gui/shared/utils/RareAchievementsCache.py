import re
from functools import partial
import ResMgr, Event
from debug_utils import LOG_WARNING, LOG_CURRENT_EXCEPTION, LOG_DEBUG
from helpers import i18n, getClientLanguage
from account_helpers.rare_achievements import getRareAchievementImage, getRareAchievementImageUrl, getRareAchievementImageBig, getRareAchievementText
from skeletons.gui.shared.utils import IRaresCache

class IMAGE_TYPE(object):
    IT_67X71 = 1
    IT_180X180 = 2


class IMAGE_PATH(object):
    IT_67X71 = b'gui/maps/icons/achievement/'
    IT_180X180 = b'gui/maps/icons/achievement/big/'


URL_NAMES = {(IMAGE_TYPE.IT_67X71): b'rare_achievements_images', 
   (IMAGE_TYPE.IT_180X180): b'rare_achievements_images_big'}

class RaresCache(IRaresCache):
    RARE_ACHIEVEMENT_PREFIX = b'rare'
    RARE_ACHIEVEMENT_PATTERN = b'^%s([0-9]+)' % RARE_ACHIEVEMENT_PREFIX
    RARE_ACHIEVEMENT_ICON_PATTERN = b'^%s[0-9]+\\.png$' % RARE_ACHIEVEMENT_PREFIX

    def __init__(self):
        self.__cache = dict()
        self.__local = set()
        self.onTextReceived = Event.Event()
        self.onImageReceived = Event.Event()
        achieveIDPattern = re.compile(self.RARE_ACHIEVEMENT_PATTERN)
        iconPattern = re.compile(self.RARE_ACHIEVEMENT_ICON_PATTERN)
        rareIcons67x71 = ResMgr.openSection(IMAGE_PATH.IT_67X71)
        rareIcons180x180 = ResMgr.openSection(IMAGE_PATH.IT_180X180)
        listOfIcons = set()
        if rareIcons67x71 is not None:
            listOfIcons.update(filter(iconPattern.match, rareIcons67x71.keys()))
        if rareIcons180x180 is not None:
            listOfIcons.update(filter(iconPattern.match, rareIcons180x180.keys()))
        for icon in listOfIcons:
            rareName = achieveIDPattern.search(icon).group()
            rareID = self.__getRareAchievementID(rareName)
            self.__local.add(rareID)
            achieveData = self.__cache[rareID] = {b'image': {}}
            try:
                achieveData[b'image'][IMAGE_TYPE.IT_67X71] = rareIcons67x71[icon].asBinary
            except Exception:
                LOG_WARNING(b'Cannot load rare achievement local file', icon)
                LOG_CURRENT_EXCEPTION()

            try:
                achieveData[b'image'][IMAGE_TYPE.IT_180X180] = rareIcons180x180[icon].asBinary
            except Exception:
                LOG_WARNING(b'Cannot load rare achievement local file', icon)

            achieveData[b'title'] = i18n.makeString(b'#achievements:%s' % rareName)
            achieveData[b'descr'] = i18n.makeString(b'#achievements:%s_descr' % rareName)
            heroInfoKey = b'%s_heroInfo' % rareName
            heroInfoMsg = i18n.makeString(b'#achievements:%s' % heroInfoKey)
            if heroInfoMsg != heroInfoKey:
                achieveData[b'historyInfo'] = heroInfoMsg
            condKey = b'%s_condition' % rareName
            condMsg = i18n.makeString(b'#achievements:%s' % condKey)
            if condMsg != condKey:
                achieveData[b'conditions'] = condMsg

        ResMgr.purge(IMAGE_PATH.IT_67X71, True)
        ResMgr.purge(IMAGE_PATH.IT_180X180, True)
        return

    def request(self, listOfIds):
        LOG_DEBUG(b'Request action achievements data', listOfIds)
        if not listOfIds:
            return
        landId = getClientLanguage()
        for achieveId in listOfIds:
            if self.isLocallyLoaded(achieveId):
                LOG_DEBUG(b'Action achievements data loaded locally', achieveId)
                continue
            getRareAchievementText(landId, achieveId, self.__onTextReceived)
            getRareAchievementImage(achieveId, partial(self.__onImageReceived, IMAGE_TYPE.IT_67X71))
            getRareAchievementImageBig(achieveId, partial(self.__onImageReceived, IMAGE_TYPE.IT_180X180))

        return

    def __onTextReceived(self, rareID, text):
        achieveData = self.__cache.setdefault(rareID, dict())
        title = text.get(b'title')
        descr = text.get(b'description')
        info = text.get(b'historyInfo')
        cond = text.get(b'conditions')

        def valueChanged(key, value):
            return value is not None and (key not in achieveData or achieveData[key] != value)

        descrChanged = valueChanged(b'descr', descr)
        titleChanged = valueChanged(b'title', title)
        infoChanged = valueChanged(b'historyInfo', info)
        condChanged = valueChanged(b'conditions', cond)
        isGenerateEvent = descrChanged or titleChanged or infoChanged or condChanged
        if descr is not None:
            achieveData[b'descr'] = descr
        if title is not None:
            achieveData[b'title'] = title
        if info is not None:
            achieveData[b'historyInfo'] = info
        if cond is not None:
            achieveData[b'conditions'] = cond
        if isGenerateEvent:
            LOG_DEBUG(b'Text received for achievement', text)
            self.onTextReceived(rareID, achieveData)
        return

    def __onImageReceived(self, imgType, imgID, imageData):
        achieveData = self.__cache.setdefault(imgID, dict())
        achieveImgData = achieveData.setdefault(b'image', {})
        if imageData is None:
            return
        else:
            isGenerateEvent = imgType not in achieveImgData or achieveImgData[imgType] != imageData
            achieveImgData[imgType] = imageData
            if isGenerateEvent:
                LOG_DEBUG(b'Image received for achievement', imgType, imgID, type(imageData))
                self.onImageReceived(imgType, imgID, imageData)
            return

    def isLocallyLoaded(self, achieveID):
        return achieveID in self.__local

    def getTitle(self, achieveID):
        return self.__cache.get(achieveID, dict()).get(b'title') or i18n.makeString(b'#tooltips:achievement/action/unavailable/title')

    def getDescription(self, achieveID):
        return self.__cache.get(achieveID, dict()).get(b'descr') or i18n.makeString(b'#tooltips:achievement/action/unavailable/descr')

    def getImageData(self, imgType, achieveID):
        return self.__cache.get(achieveID, dict()).get(b'image', {}).get(imgType)

    def getHeroInfo(self, achieveID):
        return self.__cache.get(achieveID, dict()).get(b'historyInfo')

    def getConditions(self, achieveID):
        return self.__cache.get(achieveID, dict()).get(b'conditions')

    def getAchievementImageUrl(self, imgType, achieveID):
        return getRareAchievementImageUrl(URL_NAMES[imgType], achieveID)

    @classmethod
    def __getRareAchievementID(cls, rareName):
        return int(rareName.replace(cls.RARE_ACHIEVEMENT_PREFIX, b''))
