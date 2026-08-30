from shared_utils import CONST_CONTAINER

class IVideoSoundManager(object):

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def pause(self):
        raise NotImplementedError
        return

    def unpause(self):
        raise NotImplementedError
        return


class DummySoundManager(object):

    def start(self):
        return

    def stop(self):
        return

    def pause(self):
        return

    def unpause(self):
        return


class SoundManagerStates(CONST_CONTAINER):
    PLAYING = b'playing'
    PAUSE = b'pause'
    STOPPED = b'stopped'
