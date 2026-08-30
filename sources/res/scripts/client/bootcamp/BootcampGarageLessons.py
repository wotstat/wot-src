from ResMgr import openSection
from soft_exception import SoftException
XML_BATTLE_RESULTS_PATH = b'scripts/bootcamp_docs/garage_lessons/battle_results.xml'

class _FillStruct(object):

    def __init__(self, key, vtype, funcs=None, default=None):
        self._key = key
        self._vtype = vtype
        funcs = funcs or []
        if not isinstance(funcs, list):
            funcs = [
             funcs]
        self._funcs = funcs
        self._default = default
        return

    def __call__(self, section, container):
        if section.has_key(self._key):
            container[self._key] = self._vtype()
            for func in self._funcs:
                func(section[self._key], container[self._key])

        elif self._default is not None:
            container[self._key] = self._default
        return


class _FillValue(_FillStruct):

    def __call__(self, section, container):
        if section.has_key(self._key):
            container[self._key] = getattr(section[self._key], self._vtype)
            for func in self._funcs:
                func(section[self._key], container[self._key])

        elif self._default is not None:
            container[self._key] = self._default
        return


def _getSubSections(section, subsectionName):
    subsection = section[subsectionName]
    if subsection is None:
        return []
    else:
        return subsection.items()


def _readSequenceItem(section, fields):
    messageContent = {}
    if fields:
        subSection = section[b'data']
        for field in fields:
            _FillValue(field, b'asString', default=b'')(subSection, messageContent)

    return messageContent


def _readSubItemSectionSequence(section, key, fields):
    subSection = section[b'data']
    keySection = subSection[key]
    content = []
    if keySection:
        content = [_readSequenceItem(messageSec, fields) for _, messageSec in _getSubSections(keySection, b'sequence')]
    return content


def _readVideoSection(section):
    messagesFields = (b'video-path', b'event-start', b'event-stop', b'event-pause', b'event-resume', b'event-loop', b'icon', b'video-fit-to-screen')
    subtitlesFields = (b'subtitle', b'voiceover', b'keypoint')
    messageSec = section[b'message']
    content = {b'messages': (_readSequenceItem(messageSec, messagesFields)), b'voiceovers': (_readSubItemSectionSequence(messageSec, b'subtitles', subtitlesFields))}
    return content


class GarageLessons:

    def __init__(self):
        self.__battleResults = {}
        self.readBattleResultsFile(XML_BATTLE_RESULTS_PATH)
        return

    def getBattleResult(self, lessonId):
        if lessonId in self.__battleResults:
            return self.__battleResults[lessonId]
        raise SoftException((b'Battle results not found. Lesson - {0}.').format(lessonId))
        return

    def readBattleResultsData(self, datas, section):
        for _, dataSection in section.items():
            dataSectionDict = {}
            _FillValue(b'id', b'asString', default=b'')(dataSection, dataSectionDict)
            _FillValue(b'label', b'asString', default=b'')(dataSection, dataSectionDict)
            _FillValue(b'description', b'asString', default=b'')(dataSection, dataSectionDict)
            _FillValue(b'icon', b'asString')(dataSection, dataSectionDict)
            _FillValue(b'iconTooltip', b'asString')(dataSection, dataSectionDict)
            datas.append(dataSectionDict)

        return

    def readBattleResultsFile(self, path):
        resultsConfig = openSection(path)
        if resultsConfig is None:
            raise SoftException(b"Can't open config file (%s)" % path)
        for name, section in resultsConfig.items():
            if name == b'lesson':
                lesson_id = section[b'id'].asInt
                currentBattle = self.__battleResults[lesson_id] = {}
                medals = currentBattle[b'medals'] = []
                ribbons = currentBattle[b'ribbons'] = []
                unlocks = currentBattle[b'unlocks'] = []
                self.readBattleResultsData(medals, section[b'medals'])
                self.readBattleResultsData(ribbons, section[b'ribbons'])
                self.readBattleResultsData(unlocks, section[b'unlocks'])
                currentBattle[b'videos'] = []
                videosSection = section[b'videos']
                if videosSection is not None:
                    currentBattle[b'videos'] = tuple(_readVideoSection(videoSection) for videoSection in videosSection.values())

        return
