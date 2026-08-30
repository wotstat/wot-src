from __future__ import absolute_import
import Event
from account_helpers.settings_core.settings_constants import SESSION_STATS
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings_controller import SessionStatsSettingsController, MAX_STATS
from gui.Scaleform.daapi.view.lobby.session_stats.shared import toIntegral
from gui.Scaleform.daapi.view.meta.SessionStatsSettingsMeta import SessionStatsSettingsMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
_EFFICIENCY_BLOCK = {(SESSION_STATS.SHOW_WTR): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.wtr())), 
                              b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.wtr())))}, 
   (SESSION_STATS.SHOW_RATIO_DAMAGE): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.ratioDamage())), 
                                       b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.ratioDamage())))}, 
   (SESSION_STATS.SHOW_RATIO_KILL): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.ratioKill())), 
                                     b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.ratioKill())))}, 
   (SESSION_STATS.SHOW_WINS): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.wins())), 
                               b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.wins())))}, 
   (SESSION_STATS.SHOW_AVERAGE_DAMAGE): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.averageDamage())), 
                                         b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.averageDamage())))}, 
   (SESSION_STATS.SHOW_HELP_DAMAGE): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.helpDamage())), 
                                      b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.helpDamage())))}, 
   (SESSION_STATS.SHOW_BLOCKED_DAMAGE): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.blockedDamage())), 
                                         b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.blockedDamage())))}, 
   (SESSION_STATS.SHOW_AVERAGE_XP): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.averageXp())), 
                                     b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.averageXp())))}, 
   (SESSION_STATS.SHOW_WIN_RATE): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.winRate())), 
                                   b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.winRate())))}, 
   (SESSION_STATS.SHOW_AVERAGE_VEHICLE_LEVEL): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.averageVehiclesLevel())), 
                                                b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.averageVehiclesLevel())))}, 
   (SESSION_STATS.SHOW_AVERAGE_FRAGS): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.averageFrags())), 
                                        b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.averageFrags())))}, 
   (SESSION_STATS.SHOW_SURVIVED_RATE): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.survivedRate())), 
                                        b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.survivedRate())))}, 
   (SESSION_STATS.SHOW_SPOTTED): {b'label': (backport.text(R.strings.session_stats.propertyInfo.prop.label.spotted())), 
                                  b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.propertyInfo.prop.descr.spotted())))}}
_COMMON_BLOCK = {(SESSION_STATS.IS_NOT_NEEDED_RESET_STATS_EVERY_DAY): {b'label': (backport.text(R.strings.session_stats.settings.commonSettings.isNotNeededResetStatsEveryDay())), 
                                                         b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.tooltip.settings.commonSettings.isNotNeededResetStatsEveryDay.body())))}, 
   (SESSION_STATS.IS_NEEDED_SAVE_CURRENT_TAB): {b'label': (backport.text(R.strings.session_stats.settings.commonSettings.saveCurrentTab())), 
                                                b'tooltip': (makeTooltip(body=backport.text(R.strings.session_stats.tooltip.settings.commonSettings.saveCurrentTab.body())))}}
_ECONOMIC_BLOCK_VIEW = {(SESSION_STATS.ECONOMIC_BLOCK_VIEW_WITHOUT_SPENDING): {b'label': (backport.text(R.strings.session_stats.settings.economicBlock.withoutSpending()))}, 
   (SESSION_STATS.ECONOMIC_BLOCK_VIEW_WITH_SPENDING): {b'label': (backport.text(R.strings.session_stats.settings.economicBlock.withSpending()))}}

class SessionStatsSettings(SessionStatsSettingsMeta):

    def __init__(self):
        super(SessionStatsSettings, self).__init__()
        self.__sessionStatsSettings = SessionStatsSettingsController()
        self.__currentSettings = self.__sessionStatsSettings.getSettings()
        self.onShowStats = Event.Event()
        self.__lastChangedIdentifier = None
        return

    def _populate(self):
        super(SessionStatsSettings, self)._populate()
        self.__sessionStatsSettings.start()
        self.__setSettings()
        return

    def _dispose(self):
        self.__sessionStatsSettings.stop()
        self.__sessionStatsSettings = None
        super(SessionStatsSettings, self)._dispose()
        return

    def onClickResetBtn(self):
        self.__currentSettings = self.__sessionStatsSettings.getDefaultSettings()
        self.__setSettings()
        self.as_setControlsStateS(self.__getControlsData())
        return

    def onClickApplyBtn(self):
        if not self.__currentSettings[SESSION_STATS.IS_NEEDED_SAVE_CURRENT_TAB]:
            self.__currentSettings[SESSION_STATS.CURRENT_TAB] = SESSION_STATS.BATTLES_TAB
        self.__sessionStatsSettings.setSettings(self.__currentSettings)
        self.as_setControlsStateS(self.__getControlsData())
        self.onShowStats()
        return

    def onClickBackBtn(self):
        self.__currentSettings = self.__sessionStatsSettings.getSettings()
        self.__setSettings()
        self.onShowStats()
        return

    def onSettingsInputChanged(self, identifier, value):
        self.__lastChangedIdentifier = identifier
        self.__currentSettings[identifier] = value
        self.__setBattleSettingsStatus()
        self.__setSettings()
        return

    def __setSettings(self):
        data = {b'header': (self.__getHeader()), 
           b'common': (self.__getCommonBlocks()), 
           b'economics': (self.__getEconomicsBlock()), 
           b'battle': (self.__getBattlesBlock())}
        self.as_setDataS(data)
        self.as_setControlsStateS(self.__getControlsData())
        self.__setBattleSettingsStatus()
        return

    def __getHeader(self):
        enableResetBtn = self.__currentSettings != self.__sessionStatsSettings.getDefaultSettings()
        return {b'title': (text_styles.promoSubTitle(backport.text(R.strings.session_stats.settings.header()))), 
           b'resetBtnIcon': (RES_ICONS.MAPS_ICONS_STATISTIC_ICON_BUTTON_REFRESH_093), 
           b'resetBtnTooltip': (makeTooltip(header=backport.text(R.strings.session_stats.tooltip.settings.resetBtn.header()), body=backport.text(R.strings.session_stats.tooltip.settings.resetBtn.body()))), 
           b'resetBtnEnabled': enableResetBtn}

    def __getCommonBlocks(self):
        settings = self.__currentSettings
        inputs = []
        for key in SESSION_STATS.getCommonBlock():
            inputs.append({b'id': key, 
               b'label': (_COMMON_BLOCK[key][b'label']), 
               b'tooltip': (_COMMON_BLOCK[key][b'tooltip']), 
               b'selected': (bool(settings[key]))})

        return {b'title': (text_styles.highlightText(backport.text(R.strings.session_stats.settings.commonSettings.header()))), 
           b'inputs': inputs}

    def __getEconomicsBlock(self):
        settings = self.__currentSettings
        inputs = []
        for key in SESSION_STATS.getEconomicBlockView():
            inputs.append({b'id': (str(key)), 
               b'label': (_ECONOMIC_BLOCK_VIEW[key][b'label'])})

        return {b'title': (text_styles.highlightText(backport.text(R.strings.session_stats.settings.economicBlock.header()))), 
           b'selectedRadioIndex': (settings[SESSION_STATS.ECONOMIC_BLOCK_VIEW]), 
           b'id': (SESSION_STATS.ECONOMIC_BLOCK_VIEW), 
           b'inputs': inputs}

    def __getBattlesBlock(self):
        settings = self.__currentSettings
        inputs = []
        for key in SESSION_STATS.getEfficiencyBlock():
            if key in SESSION_STATS.getImmutableEfficiencyBlockParameters():
                continue
            inputs.append({b'id': key, 
               b'label': (_EFFICIENCY_BLOCK[key][b'label']), 
               b'tooltip': (_EFFICIENCY_BLOCK[key][b'tooltip']), 
               b'selected': (bool(settings[key]))})

        return {b'title': (text_styles.highlightText(backport.text(R.strings.session_stats.settings.efficiencyBlock.header()))), 
           b'inputs': inputs}

    def __getControlsData(self):
        enableApplyBtn = self.__sessionStatsSettings.validateSettings(self.__currentSettings)
        warning = {}
        if not enableApplyBtn:
            maxStats = MAX_STATS - len(SESSION_STATS.getImmutableEfficiencyBlockParameters())
            text = backport.text(R.strings.session_stats.settings.efficiencyBlock.error(), max=maxStats)
            warning[b'text'] = text_styles.alert(text)
            warning[b'icon'] = backport.image(R.images.gui.maps.icons.library.alertBigIcon())
        else:
            enableApplyBtn = self.__currentSettings != self.__sessionStatsSettings.getSettings()
        return {b'warning': warning, 
           b'states': [
                     {b'btnEnabled': enableApplyBtn, 
                        b'btnLabel': (backport.text(R.strings.session_stats.settings.controls.applyBtn()))},
                     {b'btnEnabled': True, 
                        b'btnLabel': (backport.text(R.strings.session_stats.settings.controls.backBtn()))}]}

    def __setBattleSettingsStatus(self):
        if self.__sessionStatsSettings.validateSettings(self.__currentSettings):
            textStyle = text_styles.neutral
            warningFlag = False
        else:
            textStyle = text_styles.error
            warningFlag = self.__lastChangedIdentifier in SESSION_STATS.getEfficiencyBlock()
        parameters = list(SESSION_STATS.getEfficiencyBlock())
        for parameter in SESSION_STATS.getImmutableEfficiencyBlockParameters():
            parameters.remove(parameter)

        maxSelectedItems = MAX_STATS - len(SESSION_STATS.getImmutableEfficiencyBlockParameters())
        numberSelectedItems = sum([self.__currentSettings[key] for key in parameters])
        self.as_setBattleSettingsStatusS(text_styles.main(backport.text(R.strings.session_stats.settings.efficiencyBlock.subheader(), selected=textStyle(toIntegral(numberSelectedItems)), max=text_styles.main(toIntegral(maxSelectedItems)))), warningFlag)
        return
