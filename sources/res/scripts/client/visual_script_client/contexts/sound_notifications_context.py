import weakref, BigWorld
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.context import VScriptContext, vse_event_out, vse_func_call

class SoundNotificationsContext(VScriptContext):

    def __init__(self):
        VScriptContext.__init__(self, ASPECT.CLIENT)
        avatar = BigWorld.player()
        if avatar:
            self.__soundNotifications = avatar.soundNotifications
            if self.__soundNotifications:
                self.__soundNotifications.onPlayEvent += self.onPlayQueueEvent
                self.__soundNotifications.onAddEvent += self.onAddQueueEvent
        return

    def destroy(self):
        super(SoundNotificationsContext, self).destroy()
        if self.__soundNotifications:
            self.__soundNotifications.onPlayEvent -= self.onPlayQueueEvent
            self.__soundNotifications.onAddEvent -= self.onAddQueueEvent
            self.__soundNotifications = None
        return

    @vse_event_out(SLOT_TYPE.STR, display_name=b'OnPlayQueueEvent', description=b'Reacts on gameplay event triggered from queue', aspects=[
     ASPECT.CLIENT])
    def onPlayQueueEvent(self, eventName):
        return

    @vse_event_out(SLOT_TYPE.STR, display_name=b'OnAddQueueEvent', description=b'Reacts on gameplay event added to queue', aspects=[
     ASPECT.CLIENT])
    def onAddQueueEvent(self, eventName):
        return

    @vse_func_call(None, (SLOT_TYPE.INT,), display_name=b'PlayNextQueueEvent', description=b'Triggers next queue Event by queue number', aspects=[
     ASPECT.CLIENT])
    def playNextQueueEvent(self, queueNum):
        if self.__soundNotifications:
            self.__soundNotifications.playNextQueueEvent(queueNum)
        return

    @vse_func_call(None, (SLOT_TYPE.INT, SLOT_TYPE.INT), display_name=b'ReplayLastQueueEvent', description=b'Triggers next soundEvent of current eventChain', aspects=[
     ASPECT.CLIENT])
    def replayLastQueueEvent(self, queueNum):
        if self.__soundNotifications:
            self.__soundNotifications.replayLastQueueEvent(queueNum)
        return

    @vse_func_call(SLOT_TYPE.STR, (SLOT_TYPE.INT,), display_name=b'GetFirstQueueEvent', description=b'Returns name of first Event in queue if exists', aspects=[
     ASPECT.CLIENT])
    def getFirstQueueEvent(self, queueNum):
        eventName = b''
        if self.__soundNotifications:
            eventName = self.__soundNotifications.getFirstQueueEvent(queueNum)
        return eventName

    @vse_func_call(None, (SLOT_TYPE.INT,), display_name=b'ClearQueue', description=b'Clears queue by queue Number', aspects=[
     ASPECT.CLIENT])
    def clearQueue(self, queueNum):
        if self.__soundNotifications:
            self.__soundNotifications.clearQueue(queueNum)
        return

    @vse_func_call(SLOT_TYPE.BOOL, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetEventInfoBool', description=b'Returns Event info from sound_notifications.xml by eventName', aspects=[
     ASPECT.CLIENT])
    def getEventInfoBool(self, eventName, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getEventInfo(eventName, parameter)
        return value.lower() in (b'1', b'true')

    @vse_func_call(SLOT_TYPE.INT, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetEventInfoInt', description=b'Returns Event info from sound_notifications.xml by eventName', aspects=[
     ASPECT.CLIENT])
    def getEventInfoInt(self, eventName, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getEventInfo(eventName, parameter)
        if value:
            return int(value)
        return 0

    @vse_func_call(SLOT_TYPE.FLOAT, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetEventInfoFloat', description=b'Returns Event info from sound_notifications.xml by eventName', aspects=[
     ASPECT.CLIENT])
    def getEventInfoFloat(self, eventName, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getEventInfo(eventName, parameter)
        if value:
            return float(value)
        return 0.0

    @vse_func_call(SLOT_TYPE.STR, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetEventInfoString', description=b'Returns Event info from sound_notifications.xml by eventName', aspects=[
     ASPECT.CLIENT])
    def getEventInfoString(self, eventName, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getEventInfo(eventName, parameter)
        return value

    @vse_func_call(arrayOf(SLOT_TYPE.STR), (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetEventInfoStringArray', description=b'Returns Event info from sound_notifications.xml by eventName', aspects=[
     ASPECT.CLIENT])
    def getEventInfoStringArray(self, eventName, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getEventInfo(eventName, parameter)
        return value.split()

    @vse_func_call(SLOT_TYPE.BOOL, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetCircumstanceInfoBool', description=b'Returns Circumstance info from sound_circumstances.xml by Circumstance index', aspects=[
     ASPECT.CLIENT])
    def getCircumstanceInfoBool(self, circIndex, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getCircumstanceInfo(circIndex, parameter)
        return value.lower() in (b'1', b'true')

    @vse_func_call(SLOT_TYPE.INT, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetCircumstanceInfoInt', description=b'Returns Circumstance info from sound_circumstances.xml by Circumstance index', aspects=[
     ASPECT.CLIENT])
    def getCircumstanceInfoInt(self, circIndex, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getCircumstanceInfo(circIndex, parameter)
        if value:
            return int(value)
        return 0

    @vse_func_call(SLOT_TYPE.STR, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetCircumstanceInfoString', description=b'Returns Circumstance info from sound_circumstances.xml by Circumstance index', aspects=[
     ASPECT.CLIENT])
    def getCircumstanceInfoString(self, circIndex, parameter):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getCircumstanceInfo(circIndex, parameter)
        return value

    @vse_func_call(SLOT_TYPE.STR, (SLOT_TYPE.INT,), display_name=b'GetPlayingEventName', description=b'Returns Name of playing Event', aspects=[
     ASPECT.CLIENT])
    def getPlayingEventName(self, queueNum):
        value = None
        if self.__soundNotifications:
            value = self.__soundNotifications.getPlayingEventData(queueNum, b'eventName')
        return value

    @vse_func_call(SLOT_TYPE.VEHICLE, (SLOT_TYPE.INT,), display_name=b'GetPlayingEventVehicle', description=b'Returns Vehicle of playing Event', aspects=[
     ASPECT.CLIENT])
    def getPlayingEventVehicle(self, queueNum):
        value = None
        if self.__soundNotifications:
            value = self.__soundNotifications.getPlayingEventData(queueNum, b'vehicle')
        if value:
            return weakref.proxy(value)
        else:
            return

    @vse_func_call(SLOT_TYPE.VEHICLE, (SLOT_TYPE.INT,), display_name=b'GetPlayingEventBoundVehicle', description=b'Returns BoundVehicle of playing Event', aspects=[
     ASPECT.CLIENT])
    def getPlayingEventBoundVehicle(self, queueNum):
        value = None
        if self.__soundNotifications:
            value = self.__soundNotifications.getPlayingEventData(queueNum, b'boundVehicle')
        if value:
            return weakref.proxy(value)
        else:
            return

    @vse_func_call(SLOT_TYPE.VECTOR3, (SLOT_TYPE.INT,), display_name=b'GetPlayingEventPosition', description=b'Returns Position of playing Event', aspects=[
     ASPECT.CLIENT])
    def getPlayingEventPosition(self, queueNum):
        value = None
        if self.__soundNotifications:
            value = self.__soundNotifications.getPlayingEventData(queueNum, b'position')
        return value

    @vse_func_call(SLOT_TYPE.BOOL, (SLOT_TYPE.INT,), display_name=b'GetPlayingEventIs2D', description=b'Returns is playing Event 2D', aspects=[
     ASPECT.CLIENT])
    def getPlayingEventIs2D(self, queueNum):
        value = None
        if self.__soundNotifications:
            value = self.__soundNotifications.getPlayingEventData(queueNum, b'is2D')
        return value

    @vse_func_call(SLOT_TYPE.STR, (SLOT_TYPE.STR, SLOT_TYPE.STR), display_name=b'GetCircumstanceIndex', description=b'Returns Circumstance Index from sound_circumstances.xml by Circumstance group and name', aspects=[
     ASPECT.CLIENT])
    def getCircumstanceIndex(self, circGroup, circName):
        value = b''
        if self.__soundNotifications:
            value = self.__soundNotifications.getCircumstanceIndex(circGroup, circName)
        return value

    @vse_func_call(None, (SLOT_TYPE.STR, SLOT_TYPE.FLOAT), display_name=b'SetEventCooldown', description=b'Sets Cooldown time for Event by eventName', aspects=[
     ASPECT.CLIENT])
    def setEventCooldown(self, eventName, cooldown):
        if self.__soundNotifications:
            self.__soundNotifications.setEventCooldown(eventName, cooldown)
        return

    @vse_func_call(None, (SLOT_TYPE.STR, SLOT_TYPE.INT, SLOT_TYPE.FLOAT), display_name=b'SetEventPriority', description=b'Sets temporary Priority for Event by eventName', aspects=[
     ASPECT.CLIENT])
    def setEventPriority(self, eventName, priority, hold):
        if self.__soundNotifications:
            self.__soundNotifications.setEventPriority(eventName, priority, hold)
        return

    @vse_func_call(None, (SLOT_TYPE.STR, SLOT_TYPE.INT, SLOT_TYPE.FLOAT), display_name=b'SetCircumstanceWeight', description=b'Sets temporary Weight for circumstance', aspects=[
     ASPECT.CLIENT])
    def setCircumstanceWeight(self, circIndex, weight, hold):
        if self.__soundNotifications:
            self.__soundNotifications.setCircumstanceWeight(circIndex, weight, hold)
        return

    @vse_func_call(None, (SLOT_TYPE.STR, SLOT_TYPE.INT, SLOT_TYPE.FLOAT), display_name=b'SetCircumstanceGroupWeight', description=b'Sets temporary Weight for group of circumstances', aspects=[
     ASPECT.CLIENT])
    def setCircumstanceGroupWeight(self, groupName, weight, hold):
        if self.__soundNotifications:
            self.__soundNotifications.setCircumstanceGroupWeight(groupName, weight, hold)
        return
