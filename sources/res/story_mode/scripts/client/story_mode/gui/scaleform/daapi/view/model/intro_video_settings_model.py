import ResMgr, section2dict
from dict2model import models, schemas, fields
INTRO_VIDEO_SETTINGS_PATH = b'story_mode/gui/intro_video.xml'

class SoundEventsModel(models.Model):
    __slots__ = (b'start', b'pause', b'resume', b'stop')

    def __init__(self, start, pause, resume, stop):
        super(SoundEventsModel, self).__init__()
        self.start = start
        self.pause = pause
        self.resume = resume
        self.stop = stop
        return


class IntroVideoSettingsModel(models.Model):
    __slots__ = (b'videoPath', b'music', b'vo')

    def __init__(self, videoPath, music, vo):
        super(IntroVideoSettingsModel, self).__init__()
        self.videoPath = videoPath
        self.music = music
        self.vo = vo
        return


soundEventSchema = schemas.Schema(fields={b'start': (fields.String(required=True)), 
   b'pause': (fields.String(required=False, default=b'')), 
   b'resume': (fields.String(required=False, default=b'')), 
   b'stop': (fields.String(required=False, default=b''))}, modelClass=SoundEventsModel, checkUnknown=True)
introVideoSchema = schemas.Schema(fields={b'videoPath': (fields.String(required=True)), 
   b'music': (fields.Nested(soundEventSchema, required=True)), 
   b'vo': (fields.String(required=True))}, modelClass=IntroVideoSettingsModel, checkUnknown=True)
__introVideoSchema = None

def getSettings():
    global __introVideoSchema
    if __introVideoSchema:
        return __introVideoSchema
    root = ResMgr.openSection(INTRO_VIDEO_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    __introVideoSchema = introVideoSchema.deserialize(rawData)
    return __introVideoSchema
