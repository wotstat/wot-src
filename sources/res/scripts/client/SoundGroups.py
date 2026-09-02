import BigWorld, WWISE, Event, Settings, ResMgr, PlayerEvents, MusicControllerWWISE, Windowing, typing
from ReplayEvents import g_replayEvents
from debug_utils import LOG_ERROR, LOG_WARNING, LOG_DEBUG
from helpers import i18n, dependency
from skeletons.gui.app_loader import IAppLoader, GuiGlobalSpaceID
from soft_exception import SoftException
from vehicle_systems.tankStructure import TankPartNames
if typing.TYPE_CHECKING:
    from typing import Optional
ENABLE_LS = True
ENABLE_ENGINE_N_TRACKS = True
DEBUG_TRACE_SOUND = False
DEBUG_TRACE_STACK = False
DEBUG_TRACE_EFFECTLIST = False
g_instance = None
DSP_LOWPASS_LOW = 7000
DSP_LOWPASS_HI = 20000
DSP_SEEKSPEED = 200000
SOUND_ENABLE_STATUS_DEFAULT = 0
SOUND_ENABLE_STATUS_VALUES = range(3)
MASTER_VOLUME_DEFAULT = 0.5
OFF_POSTFIX = b'_off'
DEFAULT_SIX_SENSE = b'lightbulb'
CUSTOM_MP3_EVENTS = (b'sixthSense', b'soundExploring', b'sixthSense' + OFF_POSTFIX)
USER_SETTINGS_CATEGORY_NAMES = (
 b'gui', b'vehicles', b'voice', b'effects', b'ambient', b'music', b'music_hangar')
VIDEO_RTPC_EVENT = b'RTPC_ext_video_volume'

class CREW_GENDER_SWITCHES(object):
    GROUP = b'SWITCH_ext_vo_gender'
    MALE = b'SWITCH_ext_vo_gender_male'
    FEMALE = b'SWITCH_ext_vo_gender_female'
    DEFAULT = MALE
    GENDER_ALL = (
     MALE, FEMALE)


class SoundModes(object):
    __MODES_FOLDER = b'gui/soundModes/'
    __MODES_FILENAME = b'main_sound_modes.xml'
    DEFAULT_MODE_NAME = b'default'
    DEFAULT_NATION = b'default'
    MEDIA_PATH = None

    class SoundModeDesc(object):

        def __init__(self, dataSection):
            self.name = dataSection.readString(b'name', b'default')
            self.voiceLanguage = dataSection.readString(b'wwise_language', b'')
            descriptionLink = dataSection.readString(b'description', b'')
            self.description = i18n.makeString(descriptionLink)
            self.invisible = dataSection.readBool(b'invisible', False)
            self.wwbanksToBeLoaded = []
            self.__isValid = None
            wwbanksSec = dataSection[b'wwbanks']
            if wwbanksSec is not None:
                for bank in wwbanksSec.values():
                    bankName = bank.asString
                    manualPath = bank.readString(b'filePath', b'')
                    self.wwbanksToBeLoaded.append((bankName, manualPath))

            return

        def getIsValid(self, soundModes):
            if self.__isValid is None:
                self.__isValid = True
                for soundBankName, soundPath in self.wwbanksToBeLoaded:
                    pathToCheck = soundPath if soundPath != b'' else b'%s/%s' % (SoundModes.MEDIA_PATH, soundBankName)
                    if not ResMgr.isFile(pathToCheck):
                        self.__isValid = False

            return self.__isValid

        def __repr__(self):
            return b'SoundModeDesc<name=%s; lang=%s; visible=%s>' % (
             self.name, self.voiceLanguage, not self.invisible)

        def __cmp__(self, other):
            if not isinstance(other, SoundModes.SoundModeDesc):
                return -1
            if self.name == b'default':
                return -1
            if other.name == b'default':
                return 1
            return 1

    class NationalPresetDesc(object):

        def __init__(self, dataSection):
            self.name = dataSection.readString(b'name', b'default')
            descriptionLink = dataSection.readString(b'description', b'')
            self.description = i18n.makeString(descriptionLink)
            self.mapping = {}
            for nationSec in (dataSection[b'nations'] or {}).values():
                nationName = nationSec.readString(b'name', b'default')
                soundMode = nationSec.readString(b'soundMode', b'default')
                self.mapping[nationName] = soundMode

            return

        def __repr__(self):
            return b'NationalPresetDesc<name=%s>' % self.name

    modes = property((lambda self: self.__modes))
    nationalPresets = property((lambda self: self.__nationalPresets))
    currentMode = property((lambda self: self.__currentMode))
    currentNationalPreset = property((lambda self: self.__currentNationalPreset))
    nationToSoundModeMapping = property((lambda self: self.__nationToSoundModeMapping))

    def __init__(self, initialModeName):
        if SoundModes.MEDIA_PATH is None:
            engineConfig = ResMgr.openSection(b'engine_config.xml')
            if engineConfig is not None:
                SoundModes.MEDIA_PATH = engineConfig.readString(b'soundMgr/mediaPath', b'audioww')
            else:
                SoundModes.MEDIA_PATH = b'audioww'
        self.__modes = {}
        self.__currentMode = SoundModes.DEFAULT_MODE_NAME
        self.__nationalPresets = {}
        self.__nationToSoundModeMapping = {b'default': (SoundModes.DEFAULT_MODE_NAME)}
        self.__currentNationalPreset = (
         SoundModes.DEFAULT_MODE_NAME, False)
        modesSettingsSection = ResMgr.openSection(SoundModes.__MODES_FOLDER + SoundModes.__MODES_FILENAME)
        if modesSettingsSection is None:
            LOG_ERROR(b'%s is not found' % SoundModes.__MODES_FILENAME)
            return
        else:
            soundModes, nationalPresets = self.__readSoundModesConfig(modesSettingsSection, self.__nationalPresets)
            self.__modes = dict((soundMode.name, soundMode) for soundMode in soundModes)
            self.__nationalPresets = dict((preset.name, preset) for preset in nationalPresets)
            if SoundModes.DEFAULT_MODE_NAME not in self.__modes:
                LOG_ERROR(b'Default sound mode is not found!')
            folderSection = ResMgr.openSection(SoundModes.__MODES_FOLDER)
            if folderSection is None:
                LOG_ERROR(b"Folder for SoundModes: '%s' is not found!" % SoundModes.__MODES_FOLDER)
            else:
                defaultNationalPresets = dict(self.__nationalPresets)
                for modesConfigSection in folderSection.values():
                    if ResMgr.getFilename(modesConfigSection.name) != SoundModes.__MODES_FILENAME:
                        soundModes, nationalPresets = self.__readSoundModesConfig(modesConfigSection, defaultNationalPresets)
                        for mode in soundModes:
                            if self.__modes.has_key(mode.name):
                                LOG_WARNING(b"%s config tries to redefine soundMode '%s', ignored" % (
                                 modesConfigSection.name, mode.name))
                            else:
                                self.__modes[mode.name] = mode

                        for preset in nationalPresets:
                            if self.__nationalPresets.has_key(preset.name):
                                LOG_WARNING(b"%s config tries to redefine nationalPreset '%s', ignored" % (
                                 preset.name, preset.name))
                            else:
                                self.__nationalPresets[preset.name] = preset

            self.setMode(initialModeName)
            return

    def __readSoundModesConfig(self, rootSection, mainNationalPresets):
        soundModes = []
        modesSection = rootSection[b'modes']
        if modesSection is not None:
            for modeSec in modesSection.values():
                if modeSec.name == b'mode':
                    soundModes.append(SoundModes.SoundModeDesc(modeSec))

        nationalPresetsSection = rootSection[b'nationalPresets']
        nationalPresets = self.__readNationalPresets(nationalPresetsSection or {})
        overridesSection = rootSection[b'nationalPresetsOverrides']
        overrides = self.__readNationalPresets(overridesSection or {})
        for overridePreset in overrides:
            nationalPresetToOverride = mainNationalPresets.get(overridePreset.name)
            if nationalPresetToOverride is not None:
                for nationName, soundMode in overridePreset.mapping.iteritems():
                    nationalPresetToOverride.mapping[nationName] = soundMode

            else:
                LOG_WARNING(b"Failed to override nationalPreset '%s'" % overridePreset.name)

        return (
         soundModes, nationalPresets)

    def __readNationalPresets(self, rootSection):
        for nationalPresetSec in rootSection.values():
            if nationalPresetSec.name == b'preset':
                yield SoundModes.NationalPresetDesc(nationalPresetSec)

        return

    def setMode(self, modeName):
        languageSet = self.__setMode(modeName)
        if not languageSet:
            defaultVoiceLanguage = b''
            if SoundModes.DEFAULT_MODE_NAME in self.__modes:
                defaultVoiceLanguage = self.__modes[SoundModes.DEFAULT_MODE_NAME].voiceLanguage
            WWISE.setLanguage(defaultVoiceLanguage)
            self.__currentMode = SoundModes.DEFAULT_MODE_NAME
        return languageSet

    def __setMode(self, modeName):
        if modeName not in self.__modes:
            LOG_DEBUG(b'Sound mode %s does not exist' % modeName)
            return False
        if self.__currentMode == modeName:
            return True
        self.__currentMode = modeName
        modeDesc = self.__modes[modeName]
        WWISE.setLanguage(modeDesc.voiceLanguage)
        return True

    def setCurrentNation(self, nation, genderSwitch=CREW_GENDER_SWITCHES.DEFAULT):
        if g_instance is not None:
            g_instance.setSwitch(CREW_GENDER_SWITCHES.GROUP, genderSwitch)
        nationToQueue = nation
        if nation not in self.__nationToSoundModeMapping:
            nationToQueue = SoundModes.DEFAULT_NATION
        soundMode = self.__nationToSoundModeMapping.get(nationToQueue)
        success = soundMode is not None and self.setMode(soundMode)
        if not success:
            self.setNationalMappingByMode(SoundModes.DEFAULT_MODE_NAME)
        return success

    def setNationalMapping(self, nationToSoundModeMapping):
        for soundModeName in nationToSoundModeMapping.itervalues():
            soundModeDesc = self.__modes.get(soundModeName)
            if soundModeDesc is None:
                LOG_WARNING(b"SoundMode '%s' is not found" % soundModeName)
                return False
            if not soundModeDesc.getIsValid(self):
                LOG_WARNING(b"SoundMode '%s' has invalid banks" % soundModeName)
                return False

        self.__nationToSoundModeMapping = nationToSoundModeMapping
        self.__currentNationalPreset = None
        return True

    def setNationalMappingByMode(self, soundMode):
        if soundMode not in self.__modes:
            return False
        success = self.setNationalMapping({b'default': soundMode})
        if not success:
            return False
        self.__currentNationalPreset = (soundMode, False)
        return True

    def setNationalMappingByPreset(self, presetName):
        preset = self.__nationalPresets.get(presetName)
        if preset is None:
            return False
        else:
            success = self.setNationalMapping(preset.mapping)
            if not success:
                return False
            self.__currentNationalPreset = (presetName, True)
            return True


class SoundGroups(object):
    soundModes = property((lambda self: self.__soundModes))
    onVolumeChanged = Event.Event()
    onMusicVolumeChanged = Event.Event()

    def __init__(self):
        self.__enableStatus = SOUND_ENABLE_STATUS_DEFAULT
        self.__volumeByCategory = {}
        self.__masterVolume = 1.0
        self.__handleInside = None
        self.__handleOutside = None
        self.__activeStinger = None
        self.__activeTrack = None
        self.__activeStingerPriority = None
        self.__muffled = False
        self.__muffledByReplay = False
        self.__spaceID = GuiGlobalSpaceID.UNDEFINED
        PlayerEvents.g_playerEvents.onAvatarReady += self.onAvatarReady
        self.__categories = {b'vehicles': (b'outside/vehicles', b'vehicles'), 
           b'effects': (b'hits', b'outside/hits', b'inside/weapons', b'outside/weapons', b'outside/environment', b'battle_gui'), 
           b'gui': (b'gui', b'ingame_voice'), 
           b'music': (b'music',), 
           b'ambient': (b'outside/ambient', b'hangar_v2', b'ambientUR'), 
           b'masterVivox': (), 
           b'micVivox': (), 
           b'micWebrtc': (), 
           b'masterWebrtc': (), 
           b'masterFadeVivox': ()}
        defCategoryVolumes = {b'music': 0.5, 
           b'masterVivox': 0.7, 
           b'micVivox': 0.4, 
           b'micWebrtc': 0.8, 
           b'masterWebrtc': 1.0}
        userPrefs = Settings.g_instance.userPrefs
        soundModeName = SoundModes.DEFAULT_MODE_NAME
        nationalMapping = None
        self.__soundModes = None
        self.__viewPlayModeParam = WWISE.WW_getRTPCValue(b'RTPC_ext_viewPlayMode')
        if not userPrefs.has_key(Settings.KEY_SOUND_PREFERENCES):
            userPrefs.write(Settings.KEY_SOUND_PREFERENCES, b'')
            self.__masterVolume = MASTER_VOLUME_DEFAULT
            for categoryName in self.__categories.iterkeys():
                self.__volumeByCategory[categoryName] = defCategoryVolumes.get(categoryName, 1.0)

            self.savePreferences()
        else:
            ds = userPrefs[Settings.KEY_SOUND_PREFERENCES]
            self.__enableStatus = ds.readInt(b'enable', SOUND_ENABLE_STATUS_DEFAULT)
            self.__masterVolume = ds.readFloat(b'masterVolume', MASTER_VOLUME_DEFAULT)
            self.__volumeByCategory[b'music_hangar'] = ds.readFloat(b'volume_music_hangar', 1.0)
            self.__volumeByCategory[b'voice'] = ds.readFloat(b'volume_voice', 1.0)
            self.__volumeByCategory[b'ev_ambient'] = ds.readFloat(b'volume_ev_ambient', 0.8)
            self.__volumeByCategory[b'ev_effects'] = ds.readFloat(b'volume_ev_effects', 0.8)
            self.__volumeByCategory[b'ev_gui'] = ds.readFloat(b'volume_ev_gui', 0.8)
            self.__volumeByCategory[b'ev_music'] = ds.readFloat(b'volume_ev_music', 0.8)
            self.__volumeByCategory[b'ev_vehicles'] = ds.readFloat(b'volume_ev_vehicles', 0.8)
            self.__volumeByCategory[b'ev_voice'] = ds.readFloat(b'volume_ev_voice', 0.8)
            for categoryName in self.__categories.iterkeys():
                volume = ds.readFloat(b'volume_' + categoryName, defCategoryVolumes.get(categoryName, 1.0))
                self.__volumeByCategory[categoryName] = volume

            soundModeSec = ds[b'soundMode']
            if soundModeSec is not None:
                soundModeName = soundModeSec.asString
                if soundModeName == b'':
                    soundModeName = SoundModes.DEFAULT_MODE_NAME
                    if ds[b'soundMode'].has_key(b'nationalPreset'):
                        nationalMapping = ds.readString(b'soundMode/nationalPreset', b'')
                    else:
                        nationsSec = soundModeSec[b'nations']
                        if nationsSec is not None:
                            nationalMapping = {}
                            for nation, sec in nationsSec.items():
                                nationalMapping[nation] = sec.asString

        self.__soundModes = SoundModes(SoundModes.DEFAULT_MODE_NAME)
        if isinstance(nationalMapping, str):
            self.__soundModes.setNationalMappingByPreset(nationalMapping)
        elif isinstance(nationalMapping, dict):
            self.__soundModes.setNationalMapping(nationalMapping)
        else:
            self.__soundModes.setNationalMappingByMode(soundModeName)
        if not self.applyPreferences():
            Windowing.addWindowAccessibilitynHandler(self.__onWindowAccessibilityChanged)
        g_replayEvents.onMuteSound += self.__onReplayMute
        return

    def destroy(self):
        self.onVolumeChanged.clear()
        self.onMusicVolumeChanged.clear()
        PlayerEvents.g_playerEvents.onAvatarReady -= self.onAvatarReady
        g_replayEvents.onMuteSound -= self.__onReplayMute
        player = BigWorld.player()
        if player is not None and player.inputHandler is not None:
            player.inputHandler.onCameraChanged -= self.__onCameraChanged
        self.onVolumeChanged.clear()
        Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        LOG_DEBUG(b'Destroyed: %s' % self)
        return

    def startListeningGUISpaceChanges(self):
        appLoader = dependency.instance(IAppLoader)
        self.__spaceID = appLoader.getSpaceID()
        appLoader.onGUISpaceEntered += self.__onGUISpaceEntered
        return

    def stopListeningGUISpaceChanges(self):
        appLoader = dependency.instance(IAppLoader)
        appLoader.onGUISpaceEntered -= self.__onGUISpaceEntered
        return

    def enableLobbySounds(self, enable):
        for categoryName in (b'ambient', b'gui'):
            volume = 0.0 if not enable else self.__volumeByCategory[categoryName]
            self.setVolume(categoryName, volume, False)

        return

    def enableArenaSounds(self, enable):
        for categoryName in (b'vehicles', b'effects', b'ambient'):
            enable = enable and not self.__muffledByReplay
            volume = 0.0 if not enable else self.__volumeByCategory[categoryName]
            self.setVolume(categoryName, volume, False)

        return

    def enableAmbientAndMusic(self, enable):
        for categoryName in (b'ambient', b'music'):
            enable = enable and not self.__muffledByReplay
            volume = 0.0 if not enable else self.__volumeByCategory[categoryName]
            self.setVolume(categoryName, volume, False)

        return

    def enableEverythingExceptGui(self, enable):
        for categoryName in (b'ambient', b'music', b'music_hangar', b'vehicles', b'effects', b'voice'):
            enable = enable and not self.__muffledByReplay
            volume = 0.0 if not enable else self.__volumeByCategory[categoryName]
            self.setVolume(categoryName, volume, False)

        return

    def enableVoiceSounds(self, enable):
        for categoryName in (b'gui',):
            volume = 0.0 if not enable else self.__volumeByCategory[categoryName]
            self.setVolume(categoryName, volume, False)

        return

    def __onReplayMute(self, mute):
        if self.__muffledByReplay is mute:
            return
        self.__muffledByReplay = mute
        for categoryName in (b'vehicles', b'effects', b'ambient', b'gui', b'voice'):
            volume = 0.0 if mute else self.__volumeByCategory[categoryName]
            self.setVolume(categoryName, volume, False)

        return

    def __onGUISpaceEntered(self, spaceID):
        if WWISE.enabled:
            if spaceID == GuiGlobalSpaceID.LOGIN:
                WWISE.loadLogin()
                self.enableLobbySounds(True)
        self.__spaceID = spaceID
        return

    def setMasterVolume(self, volume):
        self.__masterVolume = volume
        self.__muffledVolume = self.__masterVolume * self.getVolume(b'masterFadeVivox')
        masterVolume = self.__muffledVolume if self.__muffled else self.__masterVolume
        self.savePreferences()
        WWISE.WW_setMasterVolume(masterVolume)
        self.onMusicVolumeChanged(b'music', self.__masterVolume, self.getVolume(b'music'))
        self.onMusicVolumeChanged(b'ambient', self.__masterVolume, self.getVolume(b'ambient'))
        return

    def getMasterVolume(self):
        if BigWorld.isWindowVisible():
            return self.__masterVolume
        return 0.0

    def getEnableStatus(self):
        return self.__enableStatus

    def setEnableStatus(self, status):
        if status not in SOUND_ENABLE_STATUS_VALUES:
            raise SoftException((b'Status {} is out of range(3)').format(status))
        self.__enableStatus = status
        self.savePreferences()
        return

    def setVolume(self, categoryName, volume, updatePrefs=True):
        WWISE.WW_setRTPCBus((b'RTPC_ext_menu_volume_{}').format(categoryName), volume * 100.0)
        if updatePrefs:
            self.__volumeByCategory[categoryName] = volume
            self.savePreferences()
        if categoryName == b'music' or categoryName == b'ambient':
            self.onMusicVolumeChanged(categoryName, self.__masterVolume, self.getVolume(categoryName))
        self.onVolumeChanged(categoryName, volume)
        return

    def setRTPC(self, name, level):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: setRTPC', name, level)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_setRTPCBus(name, level * 100.0)

    def getVolume(self, categoryName):
        return self.__volumeByCategory[categoryName]

    def getMaxVolumeFromCategories(self, categoryNames):
        return max(self.__volumeByCategory.get(key, 0.0) for key in categoryNames)

    def updateVideoVolume(self):
        volumeLevel = self.getMaxVolumeFromCategories(USER_SETTINGS_CATEGORY_NAMES)
        self.setRTPC(VIDEO_RTPC_EVENT, volumeLevel)
        return

    def savePreferences(self):
        ds = Settings.g_instance.userPrefs[Settings.KEY_SOUND_PREFERENCES]
        ds.writeFloat(b'masterVolume', self.__masterVolume)
        for categoryName in self.__volumeByCategory.iterkeys():
            ds.writeFloat(b'volume_' + categoryName, self.__volumeByCategory[categoryName])

        ds.writeInt(b'enable', self.__enableStatus)
        soundModeName = SoundModes.DEFAULT_MODE_NAME if self.__soundModes is None else self.__soundModes.currentMode
        ds.deleteSection(b'soundMode')
        if self.__soundModes is None:
            ds.writeString(b'soundMode', soundModeName)
        else:
            curPresetIsNationalPreset = self.__soundModes.currentNationalPreset
            soundModeSection = ds.createSection(b'soundMode')
            if curPresetIsNationalPreset is None:
                nationsSection = soundModeSection.createSection(b'nations')
                mapping = self.__soundModes.nationToSoundModeMapping
                for nation, mode in mapping.iteritems():
                    nationsSection.writeString(nation, mode)

            elif curPresetIsNationalPreset[1]:
                soundModeSection.writeString(b'nationalPreset', curPresetIsNationalPreset[0])
            else:
                ds.writeString(b'soundMode', curPresetIsNationalPreset[0])
        return

    def applyPreferences(self):
        if not BigWorld.isWindowVisible():
            return False
        self.setMasterVolume(self.__masterVolume)
        for categoryName in self.__volumeByCategory.iterkeys():
            newVolume = self.__volumeByCategory[categoryName]
            if self.__muffledByReplay and categoryName in (b'vehicles', b'effects', b'ambient'):
                newVolume = 0.0
            self.setVolume(categoryName, newVolume, updatePrefs=False)

        self.updateVideoVolume()
        return True

    def muffleWWISEVolume(self):
        if not self.__muffled:
            self.__muffled = True
            self.applyPreferences()
        return

    def restoreWWISEVolume(self):
        self.__muffled = False
        self.applyPreferences()
        return

    def onAvatarReady(self):
        BigWorld.player().inputHandler.onCameraChanged += self.__onCameraChanged
        PlayerEvents.g_playerEvents.onAvatarReady -= self.onAvatarReady
        self.changePlayMode(0)
        return

    def __onCameraChanged(self, cameraName, currentVehicleId=None):
        if cameraName != b'postmortem':
            return
        else:
            playerVehicle = BigWorld.entity(BigWorld.player().playerVehicleID)
            if playerVehicle is not None and playerVehicle.isAlive():
                return
            if currentVehicleId is None:
                return
            self.changePlayMode(0)
            return

    def __onWindowAccessibilityChanged(self, isAccessible):
        if isAccessible:
            self.applyPreferences()
            Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        return

    def unloadAll(self):
        MusicControllerWWISE.destroy()
        return

    def preloadSoundGroups(self, arenaName):
        MusicControllerWWISE.init(arenaName)
        return

    def getSound3D(self, node, event):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: getSound3D', event, node)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return self.WWgetSound(event, event + b' : ' + str(node), node)

    def prepareMP3(self, event=None):
        if event is None:
            LOG_ERROR(b'SOUND: event is None')
        elif event not in CUSTOM_MP3_EVENTS:
            LOG_ERROR(b'SOUND: event %s is not custom' % event)
        elif not ResMgr.isFile(b'audioww/%s.mp3' % event):
            LOG_ERROR(b"SOUND: mp3 file doesn't exist", b'audioww/%s.mp3' % event)
        else:
            WWISE.WW_prepareMP3(b'%s.mp3' % event)
            return True
        return False

    def getSound2D(self, event):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: getSound2D', event)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return self.WWgetSound(event, None, None)

    def playSound2D(self, event):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: playSound2D', event)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_eventGlobal(event)

    def playSoundPos(self, event, pos):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: playSoundPos', event, pos)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_eventGlobalPos(event, pos)

    def playCameraOriented(self, event, pos):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: playCameraOriented', event)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        WWISE.WW_playCameraOriented(event, pos)
        return

    def getCameraOriented(self, event, pos):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: playCameraOriented', event)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_getCameraOriented(event, pos)

    def WWgetSoundObject(self, objectName, matrix, local=(0.0, 0.0, 0.0), auxSend=False):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: WWgetSoundObject', objectName, matrix, local)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_getSoundObject(objectName, matrix, local, auxSend)

    def WWgetSound(self, eventName, objectName, matrix, local=(0.0, 0.0, 0.0)):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: WWgetSound', eventName, objectName, matrix, local)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_getSound(eventName, objectName, matrix, local)

    def WWgetSoundCallback(self, eventName, objectName, matrix, callback):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: WWgetSoundCallback', eventName, objectName, matrix, callback)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_getSoundCallback(eventName, objectName, matrix, callback)

    def WWgetSoundPos(self, eventName, objectName, position):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: WWgetSoundPos', eventName, objectName, position)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        return WWISE.WW_getSoundPos(eventName, objectName, position)

    def changePlayMode(self, mode):
        __ceilLess = None
        if BigWorld.player().getVehicleAttached() is not None:
            vehicleTypeDescriptor = BigWorld.player().getVehicleAttached().typeDescriptor
        else:
            vehicleTypeDescriptor = BigWorld.player().vehicleTypeDescriptor
        if vehicleTypeDescriptor is not None:
            __ceilLess = vehicleTypeDescriptor.turret.ceilless
        if mode == 0:
            self.__viewPlayModeParam.set(1)
            if __ceilLess is True:
                WWISE.WW_setState(b'STATE_viewPlayMode', b'STATE_viewplaymode_arcade_ceilless')
            else:
                WWISE.WW_setState(b'STATE_viewPlayMode', b'STATE_viewPlayMode_arcade')
            WWISE.WWsetCameraShift(None)
        elif mode == 1:
            self.__viewPlayModeParam.set(0)
            if __ceilLess is True:
                WWISE.WW_setState(b'STATE_viewPlayMode', b'STATE_viewplaymode_sniper_ceilless')
            else:
                WWISE.WW_setState(b'STATE_viewPlayMode', b'STATE_viewPlayMode_sniper')
            if BigWorld.player().getVehicleAttached() is not None:
                compoundModel = BigWorld.player().getVehicleAttached().appearance.compoundModel
                WWISE.WWsetCameraShift(compoundModel.node(TankPartNames.TURRET))
        elif mode == 2:
            self.__viewPlayModeParam.set(2)
            WWISE.WW_setState(b'STATE_viewPlayMode', b'STATE_viewPlayMode_strategic')
            WWISE.WWsetCameraShift(None)
        return

    def playStinger(self, event, priority):
        if self.__activeStinger is None or self.__activeStinger.isPlaying is False or priority > self.__activeStingerPriority:
            if self.__activeStinger is not None:
                self.__activeStinger.stop()
            self.__activeStinger = self.playSound2D(event)
            self.__activeStingerPriority = priority
        return

    def playTrack(self, event):
        if self.__activeTrack is None or self.__activeTrack.isPlaying is False:
            if self.__activeTrack is not None:
                self.__activeTrack.stop()
            self.__activeTrack = self.playSound2D(event)
        return

    def setSwitch(self, group, switch):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: setSwitch', group, switch)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        WWISE.WW_setSwitch(group, switch)
        return

    def setState(self, stateName, stateValue):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: setState', stateName, stateValue)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        WWISE.WW_setState(stateName, stateValue)
        return

    def setRTCPGlobal(self, group, value):
        if DEBUG_TRACE_SOUND is True:
            LOG_DEBUG(b'SOUND: setRTCPGlobal', group, value)
        if DEBUG_TRACE_STACK is True:
            import traceback
            traceback.print_stack()
        WWISE.WW_setRTCPGlobal(group, value)
        return
