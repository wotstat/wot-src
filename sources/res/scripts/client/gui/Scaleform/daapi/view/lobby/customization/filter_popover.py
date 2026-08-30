from __future__ import absolute_import
import logging
from collections import OrderedDict
from future.utils import iteritems
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs
from gui.Scaleform.daapi.view.meta.CustomizationFiltersPopoverMeta import CustomizationFiltersPopoverMeta
from gui.customization.shared import PROJECTION_DECAL_TEXT_FORM_TAG
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from items.components.c11n_constants import ProjectionDecalFormTags, Rarity
from skeletons.gui.customization import ICustomizationService
from uilogging.customization_3d_objects.logger import CustomizationFilterLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationFilterButtons, CustomizationViewKeys
_logger = logging.getLogger(__name__)

class FiltersPopoverVO(object):
    __slots__ = (b'lblTitle', b'lblGroups', b'lblShowOnlyFilters', b'lblAdditional', b'additionalCheckBoxData', b'btnDefault', b'basicFilterType', b'groupType', b'btnDefaultTooltip', b'groupTypeSelectedIndex', b'filterBtns', b'additionalEnabled', b'formsBtns', b'formsBtnsLbl', b'raritiesBtns', b'raritiesBtnsLbl')

    def __init__(self, lblTitle, lblGroups, lblShowOnlyFilters, lblAdditional, additionalCheckBoxData, btnDefault, groupType, btnDefaultTooltip, groupTypeSelectedIndex, filterBtns, additionalEnabled, formsBtns=None, formsBtnsLbl=b'', raritiesBtns=None, raritiesBtnsLbl=b''):
        self.lblTitle = lblTitle
        self.lblGroups = lblGroups
        self.lblShowOnlyFilters = lblShowOnlyFilters
        self.lblAdditional = lblAdditional
        self.additionalCheckBoxData = additionalCheckBoxData
        self.btnDefault = btnDefault
        self.groupType = groupType
        self.btnDefaultTooltip = btnDefaultTooltip
        self.groupTypeSelectedIndex = groupTypeSelectedIndex
        self.filterBtns = filterBtns
        self.additionalEnabled = additionalEnabled
        self.formsBtns = formsBtns
        self.formsBtnsLbl = formsBtnsLbl
        self.raritiesBtns = raritiesBtns
        self.raritiesBtnsLbl = raritiesBtnsLbl
        return

    def asDict(self):
        return {b'lblTitle': (self.lblTitle), 
           b'lblGroups': (self.lblGroups), 
           b'lblShowOnlyFilters': (self.lblShowOnlyFilters), 
           b'lblAdditional': (self.lblAdditional), 
           b'additionalCheckBoxData': (self.additionalCheckBoxData), 
           b'btnDefault': (self.btnDefault), 
           b'groupType': (self.groupType), 
           b'btnDefaultTooltip': (self.btnDefaultTooltip), 
           b'groupTypeSelectedIndex': (self.groupTypeSelectedIndex), 
           b'filterBtns': (self.filterBtns), 
           b'additionalEnabled': (self.additionalEnabled), 
           b'formsBtns': (self.formsBtns), 
           b'formsBtnsLbl': (self.formsBtnsLbl), 
           b'raritiesBtns': (self.raritiesBtns), 
           b'raritiesBtnsLbl': (self.raritiesBtnsLbl)}


class FilterPopover(CustomizationFiltersPopoverMeta):
    PROJECTION_DECAL_IMAGE_FORM_TAG = {(ProjectionDecalFormTags.SQUARE): (backport.image(R.images.gui.maps.icons.customization.icon_form_1_c())), 
       (ProjectionDecalFormTags.RECT1X2): (backport.image(R.images.gui.maps.icons.customization.icon_form_2_c())), 
       (ProjectionDecalFormTags.RECT1X3): (backport.image(R.images.gui.maps.icons.customization.icon_form_3_c())), 
       (ProjectionDecalFormTags.RECT1X4): (backport.image(R.images.gui.maps.icons.customization.icon_form_4_c())), 
       (ProjectionDecalFormTags.RECT1X6): (backport.image(R.images.gui.maps.icons.customization.icon_form_6()))}
    service = dependency.descriptor(ICustomizationService)

    def __init__(self, ctx=None):
        super(FilterPopover, self).__init__()
        self.__ctx = None
        self.__filterChangeHandlers = None
        data = ctx[b'data']
        self._purchasedToggleEnabled = data.purchasedEnabled
        self._historicToggleEnabled = data.historicEnabled
        self._nonHistoricToggleEnabled = data.nonHistoricEnabled
        self._fantasticalToggleEnabled = data.fantasticalEnabled
        self._appliedToggleEnabled = data.appliedEnabled
        self._groups = data.groups
        self._selectedGroup = data.selectedGroup
        self._groupCount = data.groupCount
        self._hideOnAnotherVehEnabled = data.hideOnAnotherVehEnabled
        self._showOnlyProgressionDecalsEnabled = data.showOnlyProgressionDecalsEnabled
        self._showOnlyEditableStylesEnabled = data.showOnlyEditableStylesEnabled
        self._showOnlyNonEditableStylesEnabled = data.showOnlyNonEditableStylesEnabled
        self._formfactorTypes = OrderedDict()
        for i, val in enumerate(data.formfactorGroups):
            if i <= len(ProjectionDecalFormTags.ALL):
                self._formfactorTypes[ProjectionDecalFormTags.ALL[i]] = val

        self._raritiesGroup = OrderedDict()
        for index, val in enumerate(data.raritiesGroup):
            self._raritiesGroup[Rarity.FILTERABLE[index]] = val

        if hasattr(data, b'isInit'):
            self._isInit = data.isInit
        else:
            self._isInit = False
        self.__uiLogger = CustomizationFilterLogger(CustomizationViewKeys.CUSTOMIZATION_FILTER_POPOVER)
        return

    def onFilterChange(self, index, value):
        self.__filterChangeHandlers[index](value)
        return

    def onFormChange(self, index, value):
        if not self._formfactorTypes:
            return
        if index >= len(ProjectionDecalFormTags.ALL):
            _logger.warning(b'"index" = %(index)s is not valid', {b'index': index})
            return
        formFactor = ProjectionDecalFormTags.ALL[index]
        if formFactor not in self._formfactorTypes:
            _logger.warning(b'"index" = %(index)s is not valid  (self._formfactorTypes = %(formfactorTypes)s)', {b'index': index, b'formfactorTypes': (self._formfactorTypes)})
            return
        self._formfactorTypes[formFactor] = value
        self.__ctx.events.onCarouselFiltered(formfactorGroups=self._formfactorTypes)
        self.updateDefaultButton()
        return

    def onRarityChange(self, index, value):
        if not self._raritiesGroup:
            return
        if index >= len(Rarity.FILTERABLE):
            _logger.warning(b'"index" = %(index)s is not valid', {b'index': index})
            return
        rarity = Rarity.FILTERABLE[index]
        if rarity not in self._raritiesGroup:
            _logger.warning(b'"index" = %(index)s is not valid  (self._raritiesGroup = %(raritiesGroup)s)', {b'index': index, b'raritiesGroup': (self._raritiesGroup)})
            return
        self.__uiLogger.onRarityFilterClick(rarity)
        self._raritiesGroup[rarity] = value
        self.__ctx.events.onCarouselFiltered(raritiesGroup=self._raritiesGroup)
        self.updateDefaultButton()
        return

    def setShowOnlyHistoric(self, value):
        self.__uiLogger.onPrimaryFilterClick(CustomizationFilterButtons.HISTORIC)
        self._historicToggleEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(historic=value)
        return

    def setShowOnlyNonHistoric(self, value):
        self.__uiLogger.onPrimaryFilterClick(CustomizationFilterButtons.NON_HISTORIC)
        self._nonHistoricToggleEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(nonHistoric=value)
        return

    def setShowOnlyFantastical(self, value):
        self.__uiLogger.onPrimaryFilterClick(CustomizationFilterButtons.FANTASTICAL)
        self._fantasticalToggleEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(fantastical=value)
        return

    def setShowOnlyAcquired(self, value):
        self.__uiLogger.onPrimaryFilterClick(CustomizationFilterButtons.IN_DEPOT)
        self._purchasedToggleEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(inventory=value)
        return

    def setHideOnAnotherVeh(self, value):
        self._hideOnAnotherVehEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(onAnotherVeh=value)
        return

    def setShowOnlyProgressionDecals(self, value):
        self._showOnlyProgressionDecalsEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(onlyProgressionDecals=value)
        return

    def setShowOnlyEditableStyles(self, value):
        self._showOnlyEditableStylesEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(onlyEditableStyles=value)
        return

    def setShowOnlyNonEditableStyles(self, value):
        self._showOnlyNonEditableStylesEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(onlyNonEditableStyles=value)
        return

    def setShowOnlyApplied(self, value):
        self.__uiLogger.onPrimaryFilterClick(CustomizationFilterButtons.APPLIED)
        self._appliedToggleEnabled = value
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(applied=value)
        return

    def changeGroup(self, itemId):
        if not self._isInit:
            self.__ctx.events.onCarouselFiltered(group=itemId)
            self._selectedGroup = itemId
            self.updateDefaultButton()
        else:
            self._isInit = False
        return

    def updateDefaultButton(self):
        if self._groupCount > 0:
            defaultGroup = self._selectedGroup == self._groupCount - 1
        else:
            defaultGroup = True
        defaultFormfactorGroups = any(self._formfactorTypes.values())
        notDefault = not defaultGroup or defaultFormfactorGroups or self._historicToggleEnabled or self._nonHistoricToggleEnabled or self._fantasticalToggleEnabled or self._purchasedToggleEnabled or self._hideOnAnotherVehEnabled or self._showOnlyProgressionDecalsEnabled or self._showOnlyEditableStylesEnabled or self._showOnlyNonEditableStylesEnabled or self._appliedToggleEnabled or any(self._raritiesGroup.values())
        self.as_enableDefBtnS(notDefault)
        return

    def setDefaultFilter(self):
        self.__uiLogger.onFilterClick(CustomizationFilterButtons.RESET_FILTER)
        self._historicToggleEnabled = False
        self._nonHistoricToggleEnabled = False
        self._fantasticalToggleEnabled = False
        self._purchasedToggleEnabled = False
        self._appliedToggleEnabled = False
        self._hideOnAnotherVehEnabled = False
        self._showOnlyProgressionDecalsEnabled = False
        self._showOnlyEditableStylesEnabled = False
        self._showOnlyNonEditableStylesEnabled = False
        oldGroup = self._selectedGroup
        self._selectedGroup = self._groupCount - 1
        if self._selectedGroup != oldGroup:
            self._isInit = True
        self._formfactorTypes = OrderedDict.fromkeys(self._formfactorTypes, False)
        self._raritiesGroup = OrderedDict.fromkeys(self._raritiesGroup, False)
        self.__updateVO = self.__createUpdateVO()
        self.as_setDataS(self.__updateVO.asDict())
        self.updateDefaultButton()
        self.__ctx.events.onCarouselFiltered(historic=self._historicToggleEnabled, nonHistoric=self._nonHistoricToggleEnabled, fantastical=self._fantasticalToggleEnabled, inventory=self._purchasedToggleEnabled, applied=self._appliedToggleEnabled, group=self._selectedGroup, formfactorGroups=self._formfactorTypes, onAnotherVeh=self._hideOnAnotherVehEnabled, onlyProgressionDecals=self._showOnlyProgressionDecalsEnabled, onlyEditableStyles=self._showOnlyEditableStylesEnabled, onlyNonEditableStyles=self._showOnlyNonEditableStylesEnabled, raritiesGroup=self._raritiesGroup, isReset=True)
        return

    def _populate(self):
        super(FilterPopover, self)._populate()
        self.__ctx = self.service.getCtx()
        self.updateDefaultButton()
        self.__updateVO = self.__createUpdateVO()
        self.as_setDataS(self.__updateVO.asDict())
        self.__uiLogger.onViewOpen(CustomizationViewKeys.CUSTOMIZATION_FILTER_POPOVER, CustomizationViewKeys.CUSTOMIZATION_BOTTOM_PANEL)
        return

    def _dispose(self):
        self.__uiLogger.onViewClose(CustomizationViewKeys.CUSTOMIZATION_FILTER_POPOVER, CustomizationViewKeys.CUSTOMIZATION_BOTTOM_PANEL)
        if self.__ctx.events is not None:
            self.__ctx.events.onFilterPopoverClosed()
        self.__ctx = None
        self.__filterChangeHandlers = None
        self.__uiLogger = None
        super(FilterPopover, self)._dispose()
        return

    def __createUpdateVO(self):
        _filterBtns = [
         {b'value': (backport.image(R.images.gui.maps.icons.buttons.fantastical())), 
            b'tooltip': (makeTooltip(backport.text(R.strings.vehicle_customization.carousel.filter.fantasticalBtn.header()), backport.text(R.strings.vehicle_customization.carousel.filter.fantasticalBtn.body()))), 
            b'selected': (self._fantasticalToggleEnabled)},
         {b'value': (backport.image(R.images.gui.maps.icons.buttons.non_historical())), 
            b'tooltip': (makeTooltip(backport.text(R.strings.vehicle_customization.carousel.filter.nonHistoricalBtn.header()), backport.text(R.strings.vehicle_customization.carousel.filter.nonHistoricalBtn.body()))), 
            b'selected': (self._nonHistoricToggleEnabled)},
         {b'value': (backport.image(R.images.gui.maps.icons.buttons.hist_small())), 
            b'tooltip': (makeTooltip(backport.text(R.strings.vehicle_customization.carousel.filter.historicalBtn.header()), backport.text(R.strings.vehicle_customization.carousel.filter.historicalBtn.body()))), 
            b'selected': (self._historicToggleEnabled)},
         {b'value': (backport.image(R.images.gui.maps.icons.customization.storage_icon())), 
            b'tooltip': (makeTooltip(backport.text(R.strings.vehicle_customization.carousel.filter.storageBtn.header()), backport.text(R.strings.vehicle_customization.carousel.filter.storageBtn.body()))), 
            b'selected': (self._purchasedToggleEnabled)},
         {b'value': (backport.image(R.images.gui.maps.icons.buttons.equipped_icon())), 
            b'tooltip': (makeTooltip(backport.text(R.strings.vehicle_customization.carousel.filter.equippedBtn.header()), backport.text(R.strings.vehicle_customization.carousel.filter.equippedBtn.body()))), 
            b'selected': (self._appliedToggleEnabled)}]
        self.__filterChangeHandlers = [
         self.setShowOnlyFantastical, self.setShowOnlyNonHistoric,
         self.setShowOnlyHistoric, self.setShowOnlyAcquired, self.setShowOnlyApplied]
        if self.__ctx.isProgressiveItemsExist:
            progressionDecalsBtnTooltip = makeTooltip(backport.text(R.strings.vehicle_customization.customization.filterPopover.progressionDecalsBtn.header()), backport.text(R.strings.vehicle_customization.customization.filterPopover.progressionDecalsBtn.body()))
            _filterBtns.append({b'value': (backport.image(R.images.gui.maps.icons.buttons.progression())), 
               b'tooltip': progressionDecalsBtnTooltip, 
               b'selected': (self._showOnlyProgressionDecalsEnabled)})
            self.__filterChangeHandlers.append(self.setShowOnlyProgressionDecals)
        if self.__ctx.mode.tabId in (CustomizationTabs.STYLES_3D, CustomizationTabs.STYLES_2D):
            editableStylesBtnTooltip = makeTooltip(backport.text(R.strings.vehicle_customization.customization.filterPopover.editableStylesBtn.header()), backport.text(R.strings.vehicle_customization.customization.filterPopover.editableStylesBtn.body()))
            _filterBtns.append({b'value': (backport.image(R.images.gui.maps.icons.buttons.editable_small())), 
               b'tooltip': editableStylesBtnTooltip, 
               b'selected': (self._showOnlyEditableStylesEnabled)})
            self.__filterChangeHandlers.append(self.setShowOnlyEditableStyles)
            nonEditableStylesBtnTooltip = makeTooltip(backport.text(R.strings.vehicle_customization.customization.filterPopover.nonEditableStylesBtn.header()), backport.text(R.strings.vehicle_customization.customization.filterPopover.nonEditableStylesBtn.body()))
            _filterBtns.append({b'value': (backport.image(R.images.gui.maps.icons.buttons.non_editable())), 
               b'tooltip': nonEditableStylesBtnTooltip, 
               b'selected': (self._showOnlyNonEditableStylesEnabled)})
            self.__filterChangeHandlers.append(self.setShowOnlyNonEditableStyles)
        _formsBtns = [{b'value': (self.PROJECTION_DECAL_IMAGE_FORM_TAG[formType]), b'selected': value, b'tooltip': (makeTooltip((b'{} {}').format(backport.text(R.strings.vehicle_customization.popover.tooltip.form()), backport.text(PROJECTION_DECAL_TEXT_FORM_TAG[formType])), backport.text(R.strings.vehicle_customization.popover.tooltip.form.body(), value=backport.text(R.strings.vehicle_customization.form.dyn(formType)()))))} for formType, value in iteritems(self._formfactorTypes)]
        formsBtnsLbl = b''
        if self._formfactorTypes:
            formsBtnsLbl = text_styles.standard(backport.text(R.strings.vehicle_customization.filter.popover.formfilters.title()))
        _raritiesBtns = [{b'value': (backport.image(R.images.gui.maps.icons.customization.rarity.sign.s20x20.dyn(rarity)())), b'selected': selected, b'tooltip': (makeTooltip(backport.text(R.strings.vehicle_customization.customization.filterPopover.rarity.header(), rarity=backport.text(R.strings.vehicle_customization.customization.rarity.dyn(rarity)())), backport.text(R.strings.vehicle_customization.customization.filterPopover.rarity.body(), rarity=backport.text(R.strings.vehicle_customization.customization.rarity.dyn(rarity)()).lower())))} for rarity, selected in iteritems(self._raritiesGroup)]
        raritiesBtnsLbl = b''
        if self._raritiesGroup:
            raritiesBtnsLbl = text_styles.standard(backport.text(R.strings.vehicle_customization.filter.popover.rarity.title()))
        additionalCheckBoxLabel = backport.text(R.strings.vehicle_customization.filter.popover.showonlyfilters.onAnotherVeh())
        additionalCheckBoxTooltip = makeTooltip(backport.text(R.strings.vehicle_customization.customization.filterPopover.additionalCheckBox.header()), backport.text(R.strings.vehicle_customization.customization.filterPopover.additionalCheckBox.body()))
        return FiltersPopoverVO(lblTitle=text_styles.highTitle(backport.text(R.strings.vehicle_customization.filter.popover.title())), lblGroups=text_styles.standard(backport.text(R.strings.vehicle_customization.filter.popover.groups.title())), lblShowOnlyFilters=text_styles.standard(backport.text(R.strings.vehicle_customization.filter.popover.showonlyfilters.title())), lblAdditional=text_styles.standard(backport.text(R.strings.vehicle_customization.filter.popover.showonlyfilters.additional())), additionalCheckBoxData={b'label': additionalCheckBoxLabel, 
           b'tooltip': additionalCheckBoxTooltip, 
           b'selected': (self._hideOnAnotherVehEnabled)}, btnDefault=backport.text(R.strings.vehicle_customization.filter.popover.getDefaultSettings()), groupType=self._groups if self._groupCount > 1 else None, btnDefaultTooltip=makeTooltip(backport.text(R.strings.vehicle_customization.customization.filterPopover.refresh.header()), backport.text(R.strings.vehicle_customization.customization.filterPopover.refresh.body())), groupTypeSelectedIndex=self._selectedGroup, filterBtns=_filterBtns, additionalEnabled=self.__ctx.isItemsOnAnotherVeh, formsBtnsLbl=formsBtnsLbl, formsBtns=_formsBtns, raritiesBtnsLbl=raritiesBtnsLbl, raritiesBtns=_raritiesBtns)
