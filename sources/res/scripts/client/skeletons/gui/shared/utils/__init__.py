from typing import TYPE_CHECKING, Optional
from skeletons.gui.shared.utils import requesters
if TYPE_CHECKING:
    from gui.shared.gui_items import ItemsCollection
    from gui.shared.gui_items.Tankman import Tankman
    from gui.shared.gui_items.Vehicle import Vehicle
    from gui.veh_post_progression.models.progression import PostProgressionItem
    from items.vehicles import VehicleType
    from gui.shared.gui_items.dossier import AccountDossier

class IItemsRequester(requesters.IRequester):

    @property
    def inventory(self):
        raise NotImplementedError
        return

    @property
    def stats(self):
        raise NotImplementedError
        return

    @property
    def dossiers(self):
        raise NotImplementedError
        return

    @property
    def goodies(self):
        raise NotImplementedError
        return

    @property
    def shop(self):
        raise NotImplementedError
        return

    @property
    def recycleBin(self):
        raise NotImplementedError
        return

    @property
    def vehicleRotation(self):
        raise NotImplementedError
        return

    @property
    def ranked(self):
        raise NotImplementedError
        return

    @property
    def battleRoyale(self):
        raise NotImplementedError
        return

    @property
    def badges(self):
        raise NotImplementedError
        return

    @property
    def epicMetaGame(self):
        raise NotImplementedError
        return

    @property
    def blueprints(self):
        raise NotImplementedError
        return

    @property
    def tokens(self):
        raise NotImplementedError
        return

    @property
    def sessionStats(self):
        raise NotImplementedError
        return

    @property
    def anonymizer(self):
        raise NotImplementedError
        return

    @property
    def battlePass(self):
        raise NotImplementedError
        return

    @property
    def giftSystem(self):
        raise NotImplementedError
        return

    @property
    def gameRestrictions(self):
        raise NotImplementedError
        return

    @property
    def resourceWell(self):
        raise NotImplementedError
        return

    @property
    def achievements20(self):
        raise NotImplementedError
        return

    @property
    def refProgram(self):
        raise NotImplementedError
        return

    @property
    def armoryYard(self):
        raise NotImplementedError
        return

    def requestUserDossier(self, databaseID, callback):
        raise NotImplementedError
        return

    def unloadUserDossier(self, databaseID):
        raise NotImplementedError
        return

    def requestUserVehicleDossier(self, databaseID, vehTypeCompDescr, callback):
        raise NotImplementedError
        return

    def invalidateCache(self, diff=None):
        raise NotImplementedError
        return

    def getVehicle(self, vehInvID):
        raise NotImplementedError
        return

    def getStockVehicle(self, typeCompDescr):
        raise NotImplementedError
        return

    def getVehicleCopy(self, vehicle):
        raise NotImplementedError
        return

    def getVehicleCopyByCD(self, typeCompDescr):
        raise NotImplementedError
        return

    def getLayoutsVehicleCopy(self, vehicle, ignoreDisabledProgression=False):
        raise NotImplementedError
        return

    def getTankman(self, tmanInvID):
        raise NotImplementedError
        return

    def getCrewSkin(self, skinID):
        raise NotImplementedError
        return

    def getTankmen(self, criteria=None):
        raise NotImplementedError
        return

    def getInventoryTankmen(self, criteria=None):
        raise NotImplementedError
        return

    def getDismissedTankmen(self, criteria=None):
        raise NotImplementedError
        return

    def removeUnsuitableTankmen(self, tankmen, criteria=None):
        raise NotImplementedError
        return

    def tankmenInBarracksCount(self):
        raise NotImplementedError
        return

    def freeTankmenBerthsCount(self):
        raise NotImplementedError
        return

    def getItems(self, itemTypeID=None, criteria=None, nationID=None, onlyWithPrices=True):
        raise NotImplementedError
        return

    def getItemsAsync(self, itemTypeID=None, criteria=None, nationID=None, onlyWithPrices=True, callback=None):
        raise NotImplementedError
        return

    def getVehicles(self, criteria=None):
        raise NotImplementedError
        return

    def getStyles(self, criteria=None):
        raise NotImplementedError
        return

    def getBadges(self, criteria=None):
        raise NotImplementedError
        return

    def getBadgeByID(self, badgeID):
        raise NotImplementedError
        return

    def getItemByCD(self, typeCompDescr):
        raise NotImplementedError
        return

    def getItem(self, itemTypeID, nationID, innationID):
        raise NotImplementedError
        return

    def getTankmanDossier(self, tmanInvID):
        raise NotImplementedError
        return

    def getVehicleDossier(self, vehTypeCompDescr, databaseID=None):
        raise NotImplementedError
        return

    def getVehicleDossiersIterator(self):
        raise NotImplementedError
        return

    def getAccountDossier(self, databaseID=None):
        raise NotImplementedError
        return

    def getClanInfo(self, databaseID=None):
        raise NotImplementedError
        return

    def getDogTag(self, databaseID=None):
        raise NotImplementedError
        return

    def getBattleRoyaleStats(self, arenaType, databaseID=None, vehicleIntCD=None):
        raise NotImplementedError
        return

    def getVehPostProgression(self, vehIntCD, vehType=None):
        raise NotImplementedError
        return

    def getPreviousItem(self, itemTypeID, invDataIdx):
        raise NotImplementedError
        return

    def doesVehicleExist(self, intCD):
        raise NotImplementedError
        return

    def onDisconnected(self):
        raise NotImplementedError
        return

    def getWTR(self, databaseID=None):
        raise NotImplementedError
        return

    def getLayout(self, databaseID=None):
        raise NotImplementedError
        return

    def getLayoutState(self, databaseID=None):
        raise NotImplementedError
        return

    def resetBattleAbilitiesUnlock(self):
        raise NotImplementedError
        return


class IHangarSpace(object):
    onStatsReceived = None
    onSpaceCreating = None
    onSpaceCreate = None
    onSpaceDestroy = None
    onMouseEnter = None
    onMouseExit = None
    onMouseDown = None
    onMouseUp = None
    onVehicleChangeStarted = None
    onVehicleChanged = None
    onSpaceRefresh = None
    onSpaceRefreshCompleted = None
    onHeroTankReady = None
    onSpaceChanged = None
    onNotifyCursorOver3dScene = None
    onSpaceChangedByAction = None

    @property
    def space(self):
        raise NotImplementedError
        return

    @property
    def spaceID(self):
        raise NotImplementedError
        return

    @property
    def inited(self):
        raise NotImplementedError
        return

    @property
    def spaceInited(self):
        raise NotImplementedError
        return

    @property
    def isPremium(self):
        raise NotImplementedError
        return

    @property
    def isModelLoaded(self):
        raise NotImplementedError
        return

    @property
    def isCursorOver3DScene(self):
        raise NotImplementedError
        return

    @property
    def spacePath(self):
        raise NotImplementedError
        return

    @property
    def visibilityMask(self):
        raise NotImplementedError
        return

    @property
    def environment(self):
        raise NotImplementedError
        return

    def spaceLoading(self):
        raise NotImplementedError
        return

    def init(self, isPremium):
        raise NotImplementedError
        return

    def refreshSpace(self, isPremium, forceRefresh=False):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return

    def updateVehicle(self, vehicle):
        raise NotImplementedError
        return

    def startToUpdateVehicle(self, vehicle, outfit=None):
        raise NotImplementedError
        return

    def updateVehicleDescriptor(self, descr):
        raise NotImplementedError
        return

    def updatePreviewVehicle(self, vehicle, outfit=None):
        raise NotImplementedError
        return

    def removeVehicle(self):
        raise NotImplementedError
        return

    def onPremiumChanged(self, isPremium, attrs, premiumExpiryTime):
        raise NotImplementedError
        return

    def setVehicleSelectable(self, flag):
        raise NotImplementedError
        return

    def updateVehicleOutfit(self, outfit):
        raise NotImplementedError
        return

    def getVehicleEntity(self):
        raise NotImplementedError
        return

    def getVehicleEntityAppearance(self):
        raise NotImplementedError
        return

    def getCentralPointForArea(self, areaID):
        raise NotImplementedError
        return

    def getAnchorParams(self, slotId, areaId, regionId):
        raise NotImplementedError
        return

    def updateAnchorsParams(self, *args):
        raise NotImplementedError
        return


class IHangarSpaceReloader(object):

    def init(self):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return

    def changeHangarSpace(self, spaceName, visibilityMask, environment, waitingMessage=None, backgroundImage=None):
        raise NotImplementedError
        return

    @property
    def hangarSpacePath(self):
        raise NotImplementedError
        return


class IRaresCache(object):
    onTextReceived = None
    onImageReceived = None

    def request(self, listOfIds):
        raise NotImplementedError
        return

    def isLocallyLoaded(self, achieveID):
        raise NotImplementedError
        return

    def getTitle(self, achieveID):
        raise NotImplementedError
        return

    def getDescription(self, achieveID):
        raise NotImplementedError
        return

    def getImageData(self, imgType, achieveID):
        raise NotImplementedError
        return

    def getHeroInfo(self, achieveID):
        raise NotImplementedError
        return

    def getConditions(self, achieveID):
        raise NotImplementedError
        return

    def getAchievementImageUrl(self, imgType, achieveID):
        raise NotImplementedError
        return
