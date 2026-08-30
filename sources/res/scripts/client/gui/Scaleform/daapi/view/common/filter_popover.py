from __future__ import absolute_import
import itertools, logging, typing
from future.utils import viewvalues
import constants
from account_helpers import AccountSettings
from account_helpers.AccountSettings import VEHICLE_CAROUSEL_COUNTERS_SEEN
from account_helpers.settings_core import settings_constants
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui import GUI_NATIONS
from gui.Scaleform import getNationsFilterAssetPath, getVehicleTypeAssetPath, getLevelsAssetPath, getButtonsAssetPath, getCustomizationTypeAssetPath
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION
from gui.Scaleform.daapi.view.common.shared import isVehicleFilterNew
from gui.Scaleform.daapi.view.common.filter_contexts import FilterSetupContext, getFilterPopoverSetupContexts
from gui.filters.carousel_filter import FILTER_KEYS
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass import BattlePassFilterConsts
from gui.Scaleform.daapi.view.meta.TankCarouselFilterPopoverMeta import TankCarouselFilterPopoverMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.settings import VEHICLE_LEVELS
from gui.shared.formatters import text_styles
from gui.shared.formatters.ranges import toRomanRangeString
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER, VEHICLE_ROLES_LABELS, VEHICLE_CLASS_NAME, VEHICLE_ROLES_LABELS_BY_CLASS
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IBattlePassController, IHangarGuiController
from skeletons.gui.shared import IItemsCache
from uilogging.customization_3d_objects.logger import CustomizationHangarVehicleFilterLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationButtons, CustomizationViewKeys
if typing.TYPE_CHECKING:
    from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import ICarouselEnvironment
_logger = logging.getLogger(__name__)
_VEHICLE_LEVEL_FILTERS = [(b'level_{}').format(level) for level in VEHICLE_LEVELS]

class VehiclesFilterPopover(TankCarouselFilterPopoverMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx):
        super(VehiclesFilterPopover, self).__init__()
        self._carousel = None
        self._isFrontline = False
        self._isRanked = False
        self._isComp7 = False
        self._withRoles = False
        if ctx and b'data' in ctx:
            data = ctx[b'data']
            self._isFrontline = getattr(data, b'isFrontline', False)
            self._isRanked = getattr(data, b'isRanked', False)
            self._isComp7 = getattr(data, b'isComp7', False)
        self._mapping = {}
        self.__usedFilters = ()
        return

    def setTankCarousel(self, carousel):
        customParams = carousel.getCustomParams()
        customParams[b'isRanked'] = self._isRanked
        customParams[b'isComp7'] = self._isComp7
        self._mapping = self._generateMapping((carousel.hasRentedVehicles() or not carousel.filter.isDefault((FILTER_KEYS.RENTED,))), (carousel.hasEventVehicles() or not carousel.filter.isDefault((FILTER_KEYS.EVENT,))), carousel.hasRoles(), carousel.hasCustomization(), **customParams)
        self.__usedFilters = list(itertools.chain.from_iterable(viewvalues(self._mapping)))
        self._carousel = carousel
        self._carousel.setPopoverCallback(self.__onCarouselSwitched)
        self._update(isInitial=True)
        return

    def changeFilter(self, sectionId, itemId):
        if self._carousel is not None and self._carousel.filter is not None:
            if sectionId in (FILTER_POPOVER_SECTION.ROLES, FILTER_POPOVER_SECTION.ROLES_WITH_EXTRA):
                filters = self._carousel.filter.getFilters(self.__usedFilters)
                target = self._mapping[FILTER_POPOVER_SECTION.ROLES][self.__getSelectedVehType(filters)][itemId]
            else:
                target = self._mapping[sectionId][itemId]
            self.__markAsSeen(target)
            self._carousel.filter.switch(target, save=False)
            self._update()
        return

    def changeSearchNameVehicle(self, inputText):
        self._carousel.filter.update({b'searchNameVehicle': inputText}, save=False)
        self._update()
        return

    def _getUpdateVO(self, filters):
        mapping = self._mapping
        vehType = self.__getSelectedVehType(filters)
        return {b'nations': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.NATIONS]], b'vehicleTypes': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.VEHICLE_TYPES]], b'levels': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.LEVELS]], b'customization': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.CUSTOMIZATION]], b'specials': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.SPECIALS]], b'hidden': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.HIDDEN]], b'progressions': [filters[key] for key in mapping[FILTER_POPOVER_SECTION.PROGRESSIONS]], b'roles': {vType: [filters[role] for role in mapping[FILTER_POPOVER_SECTION.ROLES].get(vType, [])] for vType in mapping[FILTER_POPOVER_SECTION.VEHICLE_TYPES] if vType != VEHICLE_CLASS_NAME.SPG}, 
           b'rolesLabel': (self.__getRolesLabel(vehType)), 
           b'rolesSectionVisible': (self._withRoles and vehType is not None and vehType is not VEHICLE_CLASS_NAME.SPG), 
           b'asSeen': (self.__getSeenEnties())}

    def _getInitialVO(self, filters, xpRateMultiplier):
        mapping = self._mapping
        vehType = self.__getSelectedVehType(filters)
        dataVO = {b'nationsSectionId': (FILTER_POPOVER_SECTION.NATIONS), 
           b'vehicleTypesSectionId': (FILTER_POPOVER_SECTION.VEHICLE_TYPES), 
           b'levelsSectionId': (FILTER_POPOVER_SECTION.LEVELS), 
           b'specialSectionId': (FILTER_POPOVER_SECTION.SPECIALS), 
           b'hiddenSectionId': (FILTER_POPOVER_SECTION.HIDDEN), 
           b'progressionsSectionId': (FILTER_POPOVER_SECTION.PROGRESSIONS), 
           b'rolesSectionId': (FILTER_POPOVER_SECTION.ROLES_WITH_EXTRA), 
           b'customizationId': (FILTER_POPOVER_SECTION.CUSTOMIZATION), 
           b'titleLabel': (text_styles.highTitle(b'#tank_carousel_filter:popover/title')), 
           b'nationsLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/nations')), 
           b'vehicleTypesLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/vehicleTypes')), 
           b'levelsLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/levels')), 
           b'specialsLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/specials')), 
           b'hiddenLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/hidden')), 
           b'progressionsLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/progressions')), 
           b'customizationLabel': (text_styles.standard(b'#tank_carousel_filter:popover/label/customization')), 
           b'rolesLabel': (self.__getRolesLabel(vehType)), 
           b'searchInputLabel': (backport.text(R.strings.tank_carousel_filter.popover.label.searchNameVehicle())), 
           b'searchInputName': (filters.get(b'searchNameVehicle') or b''), 
           b'searchInputTooltip': (makeTooltip(b'#tank_carousel_filter:tooltip/searchInput/header', backport.text(R.strings.tank_carousel_filter.tooltip.searchInput.body(), count=50))), 
           b'searchInputMaxChars': 50, 
           b'nations': [], b'vehicleTypes': [], b'levels': [], b'customization': [], b'specials': [], b'hidden': [], b'progressions': [], b'roles': {}, b'hiddenSectionVisible': True, 
           b'specialSectionVisible': True, 
           b'tankTierSectionVisible': True, 
           b'searchSectionVisible': True, 
           b'customizationVisible': False, 
           b'progressionsSectionVisible': False, 
           b'rolesSectionVisible': False, 
           b'changeableArrowDirection': False}

        def isSelected(entry):
            return filters.get(entry, False)

        for entry in mapping[FILTER_POPOVER_SECTION.NATIONS]:
            dataVO[b'nations'].append({b'id': entry, 
               b'value': (getNationsFilterAssetPath(entry)), 
               b'tooltip': (makeTooltip((b'#nations:{}').format(entry), b'#tank_carousel_filter:tooltip/nations/body')), 
               b'selected': (isSelected(entry))})

        for entry in mapping[FILTER_POPOVER_SECTION.LEVELS]:
            dataVO[b'levels'].append({b'id': entry, 
               b'value': (getLevelsAssetPath(entry)), 
               b'selected': (isSelected(entry))})

        for entry in mapping[FILTER_POPOVER_SECTION.CUSTOMIZATION]:
            dataVO[b'customization'].append({b'id': entry, 
               b'value': (getCustomizationTypeAssetPath(entry)), 
               b'tooltip': (makeTooltip((b'#menu:carousel_tank_filter/{}').format(entry), (b'#tank_carousel_filter:tooltip/customization/{}/body').format(entry))), 
               b'selected': (isSelected(entry)), 
               b'isNew': (isVehicleFilterNew(entry))})

        for entry in mapping[FILTER_POPOVER_SECTION.VEHICLE_TYPES]:
            dataVO[b'vehicleTypes'].append({b'id': entry, 
               b'value': (getVehicleTypeAssetPath(entry)), 
               b'tooltip': (makeTooltip((b'#menu:carousel_tank_filter/{}').format(entry), b'#tank_carousel_filter:tooltip/vehicleTypes/body')), 
               b'selected': (isSelected(entry))})

        for entry in mapping[FILTER_POPOVER_SECTION.HIDDEN]:
            dataVO[b'hidden'].append({b'label': (text_styles.standard((b'#tank_carousel_filter:popover/checkbox/{}').format(entry))), 
               b'tooltip': (makeTooltip((b'#tank_carousel_filter:tooltip/{}/header').format(entry), (b'#tank_carousel_filter:tooltip/{}/body').format(entry))), 
               b'selected': (isSelected(entry))})

        for entry in mapping[FILTER_POPOVER_SECTION.SPECIALS]:
            contexts = getFilterPopoverSetupContexts(xpRateMultiplier)
            filterCtx = contexts.get(entry, FilterSetupContext())
            tooltipRes = R.strings.tank_carousel_filter.tooltip.dyn(entry)
            enabled = not (entry == FILTER_KEYS.BONUS and self._isFrontline)
            dataVO[b'specials'].append(self._packSpecial(entry, filterCtx, isSelected(entry), tooltipRes, enabled))

        for entry in mapping[FILTER_POPOVER_SECTION.PROGRESSIONS]:
            contexts = getFilterPopoverSetupContexts(xpRateMultiplier)
            filterCtx = contexts.get(entry, FilterSetupContext())
            tooltipRes = R.strings.tank_carousel_filter.tooltip.dyn(entry)
            dataVO[b'progressions'].append({b'id': entry, 
               b'value': (getButtonsAssetPath(filterCtx.asset or entry)), 
               b'tooltip': (makeTooltip(backport.text(tooltipRes.header()) if tooltipRes else b'', backport.text(tooltipRes.body(), **filterCtx.ctx)) if tooltipRes else b''), 
               b'selected': (isSelected(entry))})

        for vType in mapping[FILTER_POPOVER_SECTION.VEHICLE_TYPES]:
            if vType != VEHICLE_CLASS_NAME.SPG:
                dataVO[b'roles'][vType] = [self.__getRoleVO(entry, filters) for entry in mapping[FILTER_POPOVER_SECTION.ROLES].get(vType, []) if entry is not None]

        if not dataVO[b'hidden']:
            dataVO[b'hiddenSectionVisible'] = False
        if not dataVO[b'specials']:
            dataVO[b'specialSectionVisible'] = False
        if self._withRoles and vehType is not None and vehType is not VEHICLE_CLASS_NAME.SPG:
            dataVO[b'rolesSectionVisible'] = True
        return dataVO

    def _packSpecial(self, entry, filterCtx, isSelected, tooltipRes, enabled):
        return {b'id': entry, 
           b'value': (getButtonsAssetPath(filterCtx.asset or entry)), 
           b'tooltip': (makeTooltip(backport.text(tooltipRes.header()) if tooltipRes else b'', backport.text(tooltipRes.body(), **filterCtx.ctx)) if tooltipRes else b''), 
           b'selected': isSelected, 
           b'enabled': enabled}

    def _dispose(self):
        if self._carousel is not None and self._carousel.filter is not None:
            self._carousel.filter.save()
            self._carousel.blinkCounter()
        if self._carousel is not None:
            self._carousel.setPopoverCallback(None)
            self._carousel = None
        self._mapping = {}
        self.__usedFilters = ()
        super(VehiclesFilterPopover, self)._dispose()
        return

    def _update(self, isInitial=False):
        filters = self._carousel.filter.getFilters(self.__usedFilters)
        xpRateMultiplier = self.itemsCache.items.shop.dailyXPFactor
        self._withRoles = self._carousel.hasRoles()
        if isInitial:
            self.as_setInitDataS(self._getInitialVO(filters, xpRateMultiplier))
        else:
            self.as_setStateS(self._getUpdateVO(filters))
        self._carousel.applyFilter()
        self.as_showCounterS(text_styles.main(backport.text(R.strings.tank_carousel_filter.popover.counter(), count=self._carousel.formatCountVehicles())))
        return

    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = {(FILTER_POPOVER_SECTION.NATIONS): GUI_NATIONS, 
           (FILTER_POPOVER_SECTION.VEHICLE_TYPES): VEHICLE_TYPES_ORDER, 
           (FILTER_POPOVER_SECTION.LEVELS): _VEHICLE_LEVEL_FILTERS, 
           (FILTER_POPOVER_SECTION.CUSTOMIZATION): [], (FILTER_POPOVER_SECTION.SPECIALS): [], (FILTER_POPOVER_SECTION.HIDDEN): [], (FILTER_POPOVER_SECTION.PROGRESSIONS): [], (FILTER_POPOVER_SECTION.ROLES): (VEHICLE_ROLES_LABELS_BY_CLASS if hasRoles else {}), 
           (FILTER_POPOVER_SECTION.ROLES_WITH_EXTRA): (VEHICLE_ROLES_LABELS + [constants.ROLES_COLLAPSE] if hasRoles else []), 
           (FILTER_POPOVER_SECTION.TEXT_SEARCH): [
                                                FILTER_KEYS.SEARCH_NAME_VEHICLE]}
        isBattleRoyaleEnabled = kwargs.get(b'hasBattleRoyleVehicles', False)
        if isBattleRoyaleEnabled:
            mapping[FILTER_POPOVER_SECTION.HIDDEN].append(FILTER_KEYS.BATTLE_ROYALE)
        elif hasEvent:
            mapping[FILTER_POPOVER_SECTION.HIDDEN].append(FILTER_KEYS.EVENT)
        if isBattleRoyaleEnabled and hasEvent:
            _logger.warning(b'It is not correct to show event and battleRoyale filters once')
        return mapping

    def __getSelectedVehType(self, filters):
        vehType = None
        if self._withRoles:
            for entry in self._mapping[FILTER_POPOVER_SECTION.VEHICLE_TYPES]:
                if filters.get(entry, False):
                    if vehType is None:
                        vehType = entry
                    else:
                        vehType = None
                        break

        return vehType

    def __onCarouselSwitched(self):
        self.destroy()
        return

    @staticmethod
    def __getRolesLabel(vehType):
        levels = toRomanRangeString(constants.ROLE_LEVELS)
        if vehType is not None and vehType != VEHICLE_CLASS_NAME.SPG:
            return text_styles.standard(_ms(TANK_CAROUSEL_FILTER.getRolesLabel(vehType), levels=levels))
        else:
            return b''

    @staticmethod
    def __getRoleVO(role, filters):
        return {b'id': role, 
           b'value': (backport.image(R.images.gui.maps.icons.roleExp.roles.c_16x16.dyn(role)())), 
           b'tooltip': (makeTooltip(backport.text(R.strings.menu.roleExp.roleName.dyn(role)(), groupName=backport.text(R.strings.menu.roleExp.roleGroupName.dyn(role)())), backport.text(R.strings.tank_carousel_filter.tooltip.role.body()))), 
           b'selected': (filters[role])}

    def __markAsSeen(self, entry):
        if isVehicleFilterNew(entry):
            counters = AccountSettings.getCounters(VEHICLE_CAROUSEL_COUNTERS_SEEN)
            counters.update({entry: True})
            AccountSettings.setCounters(VEHICLE_CAROUSEL_COUNTERS_SEEN, counters)
        return

    def __getSeenEnties(self):
        return [entry for entry, isSeen in AccountSettings.getCounters(VEHICLE_CAROUSEL_COUNTERS_SEEN).items() if isSeen]


class StorageBlueprintsFilterPopover(VehiclesFilterPopover):

    def _getInitialVO(self, filters, xpRateMultiplier):
        vo = super(StorageBlueprintsFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        vo[b'searchSectionVisible'] = False
        vo[b'hiddenSectionVisible'] = True
        vo[b'changeableArrowDirection'] = True
        vo[b'progressionsSectionVisible'] = False
        for entry in vo[b'hidden']:
            entry[b'tooltip'] = None

        return vo

    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = super(StorageBlueprintsFilterPopover, self)._generateMapping(hasRented, hasEvent, hasRoles, hasCustomization, **kwargs)
        mapping[FILTER_POPOVER_SECTION.HIDDEN].append(b'unlock_available')
        return mapping


class TankCarouselFilterPopover(VehiclesFilterPopover):
    _BASE_SPECIALS_LIST = [
     FILTER_KEYS.BONUS, FILTER_KEYS.FAVORITE, FILTER_KEYS.PREMIUM, FILTER_KEYS.ELITE, FILTER_KEYS.CRYSTALS]
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, ctx):
        super(TankCarouselFilterPopover, self).__init__(ctx)
        self._carouselRowCount = 0
        self._readRowCount(ctx)
        return

    def switchCarouselType(self, selected):
        setting = self.__settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
        self._carouselRowCount = setting.CAROUSEL_TYPES.index(setting.OPTIONS.DOUBLE if selected else setting.OPTIONS.SINGLE)
        self._carousel.setRowCount(self._carouselRowCount + 1)
        return

    @classmethod
    def _hasClanWarsVehicles(cls):
        return bool(cls.itemsCache.items.getItems(GUI_ITEM_TYPE.VEHICLE, REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.CLAN_WARS))

    @classmethod
    def _getBaseSpecialsList(cls):
        return cls._BASE_SPECIALS_LIST

    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = super(TankCarouselFilterPopover, cls)._generateMapping(hasRented, hasEvent, hasRoles, hasCustomization, **kwargs)
        mapping[FILTER_POPOVER_SECTION.SPECIALS].extend(cls._getBaseSpecialsList())
        if hasRented:
            mapping[FILTER_POPOVER_SECTION.SPECIALS].append(FILTER_KEYS.RENTED)
        if hasEvent:
            mapping[FILTER_POPOVER_SECTION.SPECIALS].append(FILTER_KEYS.EVENT)
        if constants.IS_KOREA:
            mapping[FILTER_POPOVER_SECTION.SPECIALS].append(FILTER_KEYS.IGR)
        if cls._hasClanWarsVehicles():
            mapping[FILTER_POPOVER_SECTION.SPECIALS].append(FILTER_KEYS.CLAN_RENTED)
        if hasCustomization:
            mapping[FILTER_POPOVER_SECTION.CUSTOMIZATION].append(FILTER_KEYS.OWN_3D_STYLE)
            mapping[FILTER_POPOVER_SECTION.CUSTOMIZATION].append(FILTER_KEYS.CAN_INSTALL_ATTACHMENTS)
        if kwargs.get(b'isRanked', False):
            mapping[FILTER_POPOVER_SECTION.SPECIALS].append(FILTER_KEYS.RANKED)
        if kwargs.get(b'isComp7', False):
            mapping[FILTER_POPOVER_SECTION.SPECIALS].append(b'comp7')
        return mapping

    def _dispose(self):
        self._saveRowCount()
        super(TankCarouselFilterPopover, self)._dispose()
        return

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(TankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO.update({b'toggleSwitchCarouselTooltip': (makeTooltip(b'#tank_carousel_filter:tooltip/toggleSwitchCarousel/header', b'#tank_carousel_filter:tooltip/toggleSwitchCarousel/body')), 
           b'toggleSwitchCarouselIcon': (RES_ICONS.MAPS_ICONS_FILTERS_DOUBLE_CAROUSEL), 
           b'toggleSwitchCarouselSelected': (bool(self._carouselRowCount))})
        return dataVO

    def _readRowCount(self, _):
        setting = self.__settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
        self._carouselRowCount = setting.get()
        return

    def _saveRowCount(self):
        self.__settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.GAME_EXTENDED, {(settings_constants.GAME.CAROUSEL_TYPE): (self._carouselRowCount)})
        return

    def _update(self, isInitial=False):
        super(TankCarouselFilterPopover, self)._update(isInitial)
        self._carousel.updateHotFilters()
        return


class HangarTankCarouselFilterPopover(TankCarouselFilterPopover):
    __hangarGuiCtrl = dependency.descriptor(IHangarGuiController)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, ctx):
        super(HangarTankCarouselFilterPopover, self).__init__(ctx)
        self.__uiCustomizationLogger = CustomizationHangarVehicleFilterLogger(CustomizationViewKeys.VEHICLE_FILTER)
        isCustomizationTutorial = self.__settingsCore.serverSettings.updateIsHintTutorial(settings_constants.OnceOnlyHints.VEHICLE_C11N_FILTER_HINT)
        self.__uiCustomizationLogger.onHintButtonClick(CustomizationButtons.VEHICLE_FILTER, isCustomizationTutorial, CustomizationViewKeys.VEHICLE_CAROUSEL)
        return

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(HangarTankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO[b'customizationVisible'] = True
        return dataVO

    @classmethod
    def _getBaseSpecialsList(cls):
        specialsList = cls._BASE_SPECIALS_LIST[:]
        dynamicEconomics = cls.__hangarGuiCtrl.dynamicEconomics
        hasDailyXP = FILTER_KEYS.BONUS in specialsList
        if hasDailyXP and not dynamicEconomics.checkCurrentBonusCaps(_CAPS.DAILY_MULTIPLIED_XP, default=hasDailyXP):
            specialsList.remove(FILTER_KEYS.BONUS)
        hasCrystalRewards = FILTER_KEYS.CRYSTALS in specialsList
        if hasCrystalRewards and not dynamicEconomics.checkCurrentCrystalRewards(default=hasCrystalRewards):
            specialsList.remove(FILTER_KEYS.CRYSTALS)
        return specialsList

    def changeFilter(self, sectionId, itemId):
        self.__uiCustomizationLogger.onFilterButtonClick(self._carousel, self._mapping, sectionId, itemId)
        super(HangarTankCarouselFilterPopover, self).changeFilter(sectionId, itemId)
        return


class BattlePassCarouselFilterPopover(HangarTankCarouselFilterPopover):
    __battlePassController = dependency.descriptor(IBattlePassController)

    @classmethod
    def _generateMapping(cls, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = super(BattlePassCarouselFilterPopover, cls)._generateMapping(hasRented, hasEvent, hasRoles, hasCustomization, **kwargs)
        if cls.__battlePassController.isVisible() and kwargs.get(b'isBattlePass', True):
            mapping[FILTER_POPOVER_SECTION.PROGRESSIONS].extend([BattlePassFilterConsts.FILTER_KEY_COMMON])
        return mapping

    def _getInitialVO(self, filters, xpRateMultiplier):
        isBattlePass = self._carousel.getCustomParams().get(b'isBattlePass', True)
        dataVO = super(BattlePassCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO[b'progressionsSectionVisible'] = self.__battlePassController.isVisible() and isBattlePass
        return dataVO
