import CGF
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from skeletons.gui.game_control import IPlatoonController
from PlayerEvents import g_playerEvents
from Sound import Sound3DComponent
from helpers import dependency

@registerComponent
class NyEventsListenerComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'NY Actions Listener'
    category = b'New Year'
    fightSound = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Fight 3D Sound Component', value=Sound3DComponent)
    fightStopSound = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Fight Stop 3D Sound Component', value=Sound3DComponent)

    def playFightSound(self):
        self.__playLinkedSound(self.fightSound)
        return

    def playFightStopSound(self):
        self.__playLinkedSound(self.fightStopSound)
        return

    @staticmethod
    def __playLinkedSound(soundLink):
        sound = soundLink()
        if sound is not None:
            sound.play()
        return


class NewYearEventsListenerManager(CGF.ComponentManager):
    __platoonController = dependency.descriptor(IPlatoonController)

    def __init__(self, *args):
        super(NewYearEventsListenerManager, self).__init__(*args)
        self.__wasFightActive = False
        self.__fightSoundStarted = False
        return

    def activate(self):
        self.__wasFightActive = self.__isPlatoonFightActive()
        self.__fightSoundStarted = False
        g_playerEvents.onEnqueued += self.__onSingleFightClick
        g_playerEvents.onDequeued += self.__onSingleFightLeave
        g_playerEvents.onKickedFromQueue += self.__onSingleFightLeave
        self.__platoonController.onMembersUpdate += self.__onPlatoonMembersUpdate
        return

    def deactivate(self):
        g_playerEvents.onEnqueued -= self.__onSingleFightClick
        g_playerEvents.onDequeued -= self.__onSingleFightLeave
        g_playerEvents.onKickedFromQueue -= self.__onSingleFightLeave
        self.__platoonController.onMembersUpdate -= self.__onPlatoonMembersUpdate
        self.__fightSoundStarted = False
        return

    def __broadcastFightSound(self):
        if self.__fightSoundStarted:
            return
        for listener in CGF.Query(self.spaceID, NyEventsListenerComponent):
            listener.playFightSound()
            self.__fightSoundStarted = True

        return

    def __broadcastFightStopSound(self):
        if not self.__fightSoundStarted:
            return
        for listener in CGF.Query(self.spaceID, NyEventsListenerComponent):
            listener.playFightStopSound()

        self.__fightSoundStarted = False
        return

    def __onSingleFightClick(self, *_):
        self.__broadcastFightSound()
        return

    def __onSingleFightLeave(self, *_):
        self.__broadcastFightStopSound()
        return

    def __onPlatoonMembersUpdate(self, *_):
        isFightActive = self.__isPlatoonFightActive()
        if isFightActive == self.__wasFightActive:
            return
        if isFightActive:
            self.__broadcastFightSound()
        else:
            self.__broadcastFightStopSound()
        self.__wasFightActive = isFightActive
        return

    def __isPlatoonFightActive(self):
        return self.__platoonController.isInQueue() or self.__platoonController.isInSearch()
