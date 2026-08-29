from extension_utils import ResMgr
from collections import namedtuple
_CONFIG_PATH = b'cosmic_event/gui/video_subs_config.xml'
CosmicSubtitlePhrase = namedtuple(b'CosmicSubtitlePhrase', [
 b'text', b'startTime', b'endTime'])

class CosmicVideoSubsConfigReader(object):

    @staticmethod
    def getIntroVideoPhrases():
        phrasesSection = ResMgr.openSection(_CONFIG_PATH + b'/introVideo/phrases')
        data = []
        if phrasesSection:
            for _, section in phrasesSection.items():
                text = section.readString(b'text')
                startTime = section.readFloat(b'startTime')
                endTime = section.readFloat(b'endTime')
                data.append(CosmicSubtitlePhrase(text, startTime, endTime))

        return data
