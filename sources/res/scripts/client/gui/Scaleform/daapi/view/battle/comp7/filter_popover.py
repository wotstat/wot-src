from account_helpers import AccountSettings
from account_helpers.AccountSettings import COMP7_PREBATTLE_CAROUSEL_ROW_VALUE
from gui.Scaleform.daapi.view.battle.comp7.common import getSavedRowCountValue, rowValueToRowCount, rowCountToRowValue
from gui.Scaleform.daapi.view.common.filter_popover import TankCarouselFilterPopover, FILTER_SECTION
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles

class Comp7TankCarouselFilterPopover(TankCarouselFilterPopover):

    def switchCarouselType(self, selected):
        self._carouselRowCount = 1 if selected else 0
        self.__saveRowCountValue()
        self._carousel.setRowCount(rowValueToRowCount(self._carouselRowCount))
        return

    def _populate(self):
        super(Comp7TankCarouselFilterPopover, self)._populate()
        self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER, enableAiming=False)
        return

    def _dispose(self):
        self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER)
        super(Comp7TankCarouselFilterPopover, self)._dispose()
        return

    def _readRowCount(self, ctx):
        savedRowValue, isSavedByPlayer = getSavedRowCountValue()
        if isSavedByPlayer:
            self._carouselRowCount = savedRowValue
        elif ctx and b'data' in ctx:
            data = ctx[b'data']
            self._carouselRowCount = rowCountToRowValue(getattr(data, b'rowCount', 1))
        return

    def _saveRowCount(self):
        savedRowValue, isSavedByPlayer = getSavedRowCountValue()
        if isSavedByPlayer and savedRowValue != self._carouselRowCount:
            self.__saveRowCountValue()
        return

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(Comp7TankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO[b'specialSectionVisible'] = True
        dataVO[b'searchSectionVisible'] = True
        dataVO[b'progressionsSectionVisible'] = False
        dataVO[b'additionalInfo'] = text_styles.stats(backport.text(R.strings.comp7.battleCarousel.filterPopover.desc()))
        vehicleLevels = self._carousel.getCustomParams().get(b'vehicleLevelsFilter', list())
        if self._carousel is not None and not len(vehicleLevels) > 1:
            dataVO[b'tankTierSectionVisible'] = False
        return dataVO

    def _generateMapping(self, hasRented, hasEvent, hasRoles, **kwargs):
        mapping = super(Comp7TankCarouselFilterPopover, self)._generateMapping(hasRented, hasEvent, hasRoles, **kwargs)
        mapping[FILTER_SECTION.SPECIALS] = [
         b'rented', b'favorite']
        vehicleLevels = kwargs.get(b'vehicleLevelsFilter', list())
        if len(vehicleLevels) > 1:
            mapping[FILTER_SECTION.LEVELS] = [(b'level_{}').format(lvl) for lvl in vehicleLevels]
        else:
            mapping[FILTER_SECTION.LEVELS] = []
        return mapping

    def __saveRowCountValue(self):
        AccountSettings.setSettings(COMP7_PREBATTLE_CAROUSEL_ROW_VALUE, self._carouselRowCount)
        return
