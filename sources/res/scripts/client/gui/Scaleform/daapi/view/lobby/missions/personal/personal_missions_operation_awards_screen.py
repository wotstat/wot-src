from gui.Scaleform.daapi.view.meta.PersonalMissionsOperationAwardsScreenMeta import PersonalMissionsOperationAwardsScreenMeta
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import AWARDS_SIZES, LABEL_ALIGN
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.settings import ICONS_SIZES
from gui.server_events.pm_constants import SOUNDS, PERSONAL_MISSIONS_SOUND_SPACE
from gui.shared.utils.functions import makeTooltip
from gui.shared.gui_items.Vehicle import getTypeBigIconPath
from gui.server_events import finders
from helpers import dependency
from helpers.i18n import makeString as _ms
from shared_utils import first
from skeletons.gui.server_events import IEventsCache

class PersonalMissionsOperationAwardsScreen(PersonalMissionsOperationAwardsScreenMeta):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SOUND_SPACE
    _eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, ctx):
        ctx = ctx or {}
        super(PersonalMissionsOperationAwardsScreen, self).__init__(ctx)
        self.__branch = ctx[b'branch']
        self.__operationID = ctx[b'operationID']
        self.__questsIds = ctx[b'questIds']
        self.__vehicleAward = None
        return

    def onPlaySound(self, soundType):
        self.soundManager.playSound(SOUNDS.TANK_AWARD_WINDOW)
        return

    def onCloseWindow(self):
        self.destroy()
        self.soundManager.setRTPC(SOUNDS.RTCP_OVERLAY, SOUNDS.MIN_MISSIONS_ZOOM)
        return

    def _populate(self):
        super(PersonalMissionsOperationAwardsScreen, self)._populate()
        badges, camouflageAward = self.__getBonuses(self.__questsIds)
        self.as_setInitDataS({b'closeBtnLabel': (PERSONAL_MISSIONS.AWARDSSCREEN_CLOSEBTN_LABEL), 
           b'header': (self.__getHeader()), 
           b'headerExtra': (PERSONAL_MISSIONS.AWARDSSCREEN_HEADEREXTRA), 
           b'campaignId': (self.__branch), 
           b'vehicleData': (self.__getVehicleData())})
        awards = self.__packBadges(badges)
        if camouflageAward:
            awards.append(camouflageAward)
        renderSize = 80 if self.__vehicleAward else 110
        self.as_setAwardDataS({b'ribbonType': b'ribbon1', 
           b'rendererLinkage': b'RibbonAwardAnimUI', 
           b'gap': 20, 
           b'rendererWidth': renderSize, 
           b'rendererHeight': renderSize, 
           b'awards': awards})
        self.as_playAwardsAnimationS()
        self.soundManager.playSound(SOUNDS.TANK_AWARD_WINDOW)
        self.soundManager.setRTPC(SOUNDS.RTCP_OVERLAY, SOUNDS.MAX_MISSIONS_ZOOM)
        return

    def __getHeader(self):
        operation = self._eventsCache.getPersonalMissions().getOperationsForBranch(self.__branch)[self.__operationID]
        if operation.isFullCompleted():
            l18nKey = PERSONAL_MISSIONS.AWARDSSCREEN_HEADER_FULLYCOMPLETED
        else:
            l18nKey = PERSONAL_MISSIONS.AWARDSSCREEN_HEADER
        return _ms(l18nKey, missionName=operation.getShortUserName())

    def __getVehicleData(self):
        if self.__vehicleAward is None:
            return
        else:
            vehicle, _ = first(self.__vehicleAward.getVehicles())
            vehName = vehicle.name
            vehIcon = RES_ICONS.getPersonalMissionVehicleAwardImage(ICONS_SIZES.X550, vehName.split(b':')[-1])
            vehicleLevel = _ms(TOOLTIPS.level(vehicle.level))
            vehicleTypeIcon = getTypeBigIconPath(vehicle.type, vehicle.isElite)
            if vehIcon is not None:
                return {b'vehicleSrc': vehIcon, 
                   b'vehicleTypeIcon': vehicleTypeIcon, 
                   b'vehicleName': (vehicle.userName), 
                   b'vehicleLevel': vehicleLevel, 
                   b'tooltip': {b'isSpecial': True, 
                                b'specialAlias': (TOOLTIPS_CONSTANTS.AWARD_VEHICLE), 
                                b'specialArgs': [
                                               vehicle.intCD]}}
            return

    def __packBadges(self, badges):
        result = []
        for badge in badges:
            result.append({b'label': None, 
               b'imgSource': (badge.getBigIcon() if self.__vehicleAward else badge.getIconX110()), 
               b'tooltip': None, 
               b'isSpecial': True, 
               b'specialAlias': (TOOLTIPS_CONSTANTS.BADGE), 
               b'specialArgs': [
                              badge.badgeID], 
               b'align': (LABEL_ALIGN.RIGHT)})

        return result

    def __getBonuses(self, tokensQuestsIds):
        finderFunc = finders.multipleTokenFinder(tokensQuestsIds)
        resultQuests = self._eventsCache.getHiddenQuests(finderFunc)
        vehicles = []
        achievements = []
        hasTankCamo = False
        hasNationCamo = False
        for quest in resultQuests.itervalues():
            if quest.getBonuses(b'customizations', []):
                hasTankCamo = True
                continue
            vehicles.extend(quest.getBonuses(b'vehicles', []))
            for bonus in quest.getBonuses(b'dossier', []):
                achievements.extend(bonus.getBadges())

            for bonus in quest.getBonuses(b'tokens', []):
                for token in bonus.getTokens():
                    if token.endswith(b':camouflage'):
                        hasNationCamo = True

        self.__vehicleAward = first(vehicles)
        if hasTankCamo or hasNationCamo:
            if self.__vehicleAward:
                camouflageIcon = RES_ICONS.getBonusIcon(AWARDS_SIZES.BIG, b'camouflage')
            else:
                camouflageIcon = RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_AWARDS_110X110_CAMOUFLAGE
            if hasTankCamo and hasNationCamo:
                tooltipKeys = (TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGEALL_HEADER,
                 TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGEALL_BODY)
            elif hasTankCamo:
                tooltipKeys = (TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGEONLY_HEADER,
                 TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGEONLY_BODY)
            else:
                tooltipKeys = (TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGENATION_HEADER,
                 TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGENATION_BODY)
            camouflageAward = {b'imgSource': camouflageIcon, 
               b'itemName': b'camouflage', 
               b'tooltip': (makeTooltip(*tooltipKeys))}
        else:
            camouflageAward = None
        return (sorted(achievements, reverse=True), camouflageAward)
