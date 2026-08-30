from __future__ import absolute_import
import typing
from Event import Event
if typing.TYPE_CHECKING:
    from typing import Optional
    from items.components.c11n_components import StyleItem
    from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs
    from gui.Scaleform.daapi.view.lobby.customization.context.context import CustomizationContext
    from gui.customization.constants import CustomizationModes
    from items.components.c11n_constants import SeasonType

class ICustomizationService(object):
    onRegionHighlighted = None
    onOutfitChanged = None
    onCustomizationHelperRecreated = None
    onVisibilityChanged = None

    @property
    def isOver3dScene(self):
        raise NotImplementedError
        return

    @property
    def lastAppliedSeason(self):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def showCustomization(self, vehInvID=None, callback=None, season=None, modeId=None, tabId=None, itemCD=None):
        raise NotImplementedError
        return

    def closeCustomization(self):
        raise NotImplementedError
        return

    def getCtx(self):
        raise NotImplementedError
        return

    def createCtx(self, season=None, modeId=None, tabId=None, source=None, itemCD=None):
        raise NotImplementedError
        return

    def saveLastWrittenDataFromCtx(self):
        raise NotImplementedError
        return

    def destroyCtx(self):
        raise NotImplementedError
        return

    def startHighlighter(self, mode):
        raise NotImplementedError
        return

    def stopHighlighter(self):
        raise NotImplementedError
        return

    def suspendHighlighter(self):
        raise NotImplementedError
        return

    def resumeHighlighter(self):
        raise NotImplementedError
        return

    def getSelectionMode(self):
        raise NotImplementedError
        return

    def getPointForRegionLeaderLine(self, areaId):
        raise NotImplementedError
        return

    def getAnchorParams(self, areaId, slotId, regionId):
        raise NotImplementedError
        return

    def getHightlighter(self):
        raise NotImplementedError
        return

    def getItems(self, itemTypeID, vehicle=None, criteria=None):
        raise NotImplementedError
        return

    def getPaints(self, vehicle=None, criteria=None):
        raise NotImplementedError
        return

    def getCamouflages(self, vehicle=None, criteria=None):
        raise NotImplementedError
        return

    def getStyles(self, vehicle=None, criteria=None):
        raise NotImplementedError
        return

    def getItemByID(self, itemTypeID, itemID):
        raise NotImplementedError
        return

    def getTypedItemsByCDs(self, itemTypeID, itemCDs):
        raise NotImplementedError
        return

    def getItemByCD(self, itemCD):
        raise NotImplementedError
        return

    def getEmptyOutfit(self, vehicleCD=b''):
        raise NotImplementedError
        return

    def getEmptyOutfitWithNationalEmblems(self, vehicleCD):
        raise NotImplementedError
        return

    def tryOnOutfit(self, outfit):
        raise NotImplementedError
        return

    def getCurrentOutfit(self, season):
        raise NotImplementedError
        return

    def getCurrentStyle(self):
        raise NotImplementedError
        return

    def getCustomOutfit(self, season):
        raise NotImplementedError
        return

    def isStyleInstalled(self):
        raise NotImplementedError
        return

    def isRegionSelected(self):
        raise NotImplementedError
        return

    def buyItems(self, item, count, vehicle=None):
        raise NotImplementedError
        return

    def sellItem(self, item, count, vehicle=None):
        raise NotImplementedError
        return

    def setSelectHighlighting(self, value):
        raise NotImplementedError
        return

    def resetHighlighting(self):
        raise NotImplementedError
        return

    def highlightRegions(self, regionsMask):
        raise NotImplementedError
        return

    def selectRegions(self, regionsMask):
        raise NotImplementedError
        return

    def setSelectingRegionEnabled(self, enable):
        raise NotImplementedError
        return

    def setDOFenabled(self, enable):
        raise NotImplementedError
        return

    def setDOFparams(self, params):
        raise NotImplementedError
        return

    def changeStyleProgressionLevelPreview(self, level):
        raise NotImplementedError
        return

    def getCurrentProgressionStyleLevel(self):
        raise NotImplementedError
        return

    @staticmethod
    def removeAdditionalProgressionData(outfit, style, vehCD, season):
        raise NotImplementedError
        return

    def getQuestsForProgressionItem(self, itemCD):
        raise NotImplementedError
        return

    def getItemCDByQuestID(self, eventID):
        raise NotImplementedError
        return

    def isProgressionQuests(self, eventID):
        raise NotImplementedError
        return

    def getStyleItemByQuestID(self, eventID):
        raise NotImplementedError
        return
