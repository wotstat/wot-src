import time, typing
from collections import namedtuple
from gui.impl import backport
from gui.impl.gen import R
from gui.marathon.marathon_constants import MarathonState, R_TITLE_TOOLTIP, R_BUYING_PANEL, BUYING_BUTTON_ICON_ALIGN, MarathonFlagTooltip
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
from helpers.time_utils import ONE_DAY, getTimeStructInLocal, ONE_HOUR
MarathonEventTooltipData = namedtuple(b'MarathonEventTooltipData', (b'header', b'body', b'bodyExtraVehicle', b'bodyExtraStyle', b'bodyExtraSmart', b'errorBattleType', b'errorVehType', b'extraStateSteps', b'extraStateDiscount', b'extraStateCompleted', b'stateStart', b'stateEnd', b'stateProgress', b'stateComplete', b'daysShort', b'hoursShort', b'minutesShort', b'previewAnnounce', b'previewInProgress'))
MarathonEventIconsData = namedtuple(b'MarathonEventIconsData', (b'tooltipHeader', b'okIcon', b'timeIcon', b'timeIconGlow', b'alertIcon', b'iconFlag', b'saleIcon', b'mapFlagHeaderIcon'))

class MarathonResourceManager(object):

    def __init__(self, dataContainer):
        self._data = dataContainer
        self._initialize()
        return

    def getBuyBtnEnabledData(self, hasIgbLink):
        return {b'enabled': True, 
           b'label': (backport.text(R_BUYING_PANEL.buyBtn.label.buy())), 
           b'btnIcon': (None if hasIgbLink else backport.image(R.images.gui.maps.icons.library.buyInWeb())), 
           b'btnIconAlign': BUYING_BUTTON_ICON_ALIGN, 
           b'btnTooltip': (makeTooltip(body=backport.text(R_BUYING_PANEL.buyBtn.tooltip.active.body()))), 
           b'customOffer': None}

    def getBuyBtnDiscountData(self, discount, hasIgbLink):
        discountText = text_styles.discountText(backport.text(R_BUYING_PANEL.customOffer.discount()))
        discountValue = text_styles.promoTitle(backport.text(R.strings.quests.action.discount.percent(), value=backport.getIntegralFormat(discount)))
        return {b'enabled': True, 
           b'label': (backport.text(R_BUYING_PANEL.buyBtn.label.buy())), 
           b'btnIcon': (None if hasIgbLink else backport.image(R.images.gui.maps.icons.library.buyInWeb())), 
           b'btnIconAlign': BUYING_BUTTON_ICON_ALIGN, 
           b'btnTooltip': (makeTooltip(body=backport.text(R_BUYING_PANEL.buyBtn.tooltip.active.body()))), 
           b'customOffer': ((b' ').join((discountText, discountValue)))}

    def getBuyBtnDisabledData(self, hasIgbLink):
        questStartTime, _ = self._data.getQuestStartFinishTime()
        addInfo = backport.text(self._data.tooltips.previewAnnounce, marathonStartDate=text_styles.neutral(self._getDateTimeText(questStartTime)))
        tooltip = makeTooltip(header=backport.text(R_BUYING_PANEL.buyBtn.tooltip.inactive.header()), body=backport.text(R_BUYING_PANEL.buyBtn.tooltip.inactive.body(), addInfo=addInfo, event_name=backport.text(self._data.label)))
        return {b'enabled': False, 
           b'label': (backport.text(R_BUYING_PANEL.buyBtn.label.buy())), 
           b'btnIcon': (None if hasIgbLink else backport.image(R.images.gui.maps.icons.library.buyInWeb())), 
           b'btnIconAlign': BUYING_BUTTON_ICON_ALIGN, 
           b'btnTooltip': tooltip, 
           b'customOffer': None}

    def getEmptyTooltip(self):
        return makeTooltip()

    def getExtraTimeToBuy(self):
        _, groupFinishTimeLeft = self._data.getGroupTimeInterval()
        gmtime = time.gmtime(groupFinishTimeLeft)
        if groupFinishTimeLeft >= ONE_DAY:
            text = backport.text(self._data.tooltips.daysShort, value=str(gmtime.tm_yday))
        elif groupFinishTimeLeft >= ONE_HOUR:
            text = backport.text(self._data.tooltips.hoursShort, value=str(gmtime.tm_hour + 1))
        else:
            text = backport.text(self._data.tooltips.minutesShort, value=str(gmtime.tm_min + 1))
        return text_styles.neutral(text)

    def getHangarFlagTooltip(self):
        return MarathonFlagTooltip.COUNTDOWN(self._data).create()

    def getTitleNotStartedTooltip(self):
        questStartTime, _ = self._data.getQuestStartFinishTime()
        tooltipBody = self._data.infoBody.announce()
        addInfo = backport.text(self._data.bodyAddInfo.announce(), addInfo=backport.text(self._data.tooltips.previewAnnounce, marathonStartDate=text_styles.neutral(self._getDateTimeText(questStartTime))))
        return self._getTitleMakeTooltip(tooltipBody, addInfo)

    def getTitleTooltip(self, finishSaleTime, discount):
        if discount:
            tooltipBody = self._data.infoBody.progress.withDiscount()
        else:
            tooltipBody = self._data.infoBody.progress()
        addInfo = backport.text(self._data.bodyAddInfo.progress(), endVehicleSellDate=text_styles.neutral(self._getDateTimeText(finishSaleTime)), addInfo=backport.text(self._data.tooltips.previewInProgress))
        return self._getTitleMakeTooltip(tooltipBody, addInfo)

    def _initialize(self):
        marathonBody = R_TITLE_TOOLTIP.info.dyn(self._data.prefix)
        self._data.infoBody = marathonBody.body if marathonBody.isValid() else R_TITLE_TOOLTIP.info.body
        self._data.label = self._getLabelObject(R.strings.quests.missions.tab.label)()
        self._data.backBtnLabel = self._getLabelObject(R.strings.vehicle_preview.header.backBtn.descrLabel)()
        self._data.tooltips = self._getTooltips()
        self._data.icons = self._getIcons()
        return

    def getHangarFlag(self):
        return backport.image(R.images.gui.maps.icons.library.hangarFlag.dyn(self._data.hangarFlagName)())

    def _getDateTimeText(self, timestamp):
        localDateTime = getTimeStructInLocal(timestamp)
        monthName = backport.text(R.strings.menu.dateTime.months.dyn((b'c_{}').format(localDateTime.tm_mon))())
        dateTimeText = backport.text(R.strings.marathon.vehiclePreview.tooltip.dateTime(), day=localDateTime.tm_mday, monthName=monthName, year=localDateTime.tm_year, hour=localDateTime.tm_hour, min=(b'{min:02d}').format(min=localDateTime.tm_min))
        return dateTimeText.replace(b' ', b'&nbsp;')

    def _getTitleMakeTooltip(self, tooltipBody, addInfo):
        label = backport.text(self._data.label)
        return makeTooltip(header=backport.text(R.strings.marathon.vehiclePreview.title.tooltip.rewards(), event_name=label), body=backport.text(tooltipBody, event_name=label, addInfo=addInfo))

    def _getTooltips(self):
        body = self._getTooltipString(b'body')
        error = self._getTooltipString(b'error')
        state = self._getTooltipString(b'state')
        extraState = self._getTooltipString(b'extra_state')
        return MarathonEventTooltipData(header=self._getTooltipString(b'header')(), body=body(), bodyExtraVehicle=body.extra_vehicle(), bodyExtraStyle=body.extra_style(), bodyExtraSmart=body.extra_smart(), errorBattleType=error.battle_type(), errorVehType=error.veh_type(), extraStateSteps=extraState.steps(), extraStateDiscount=extraState.discount(), extraStateCompleted=extraState.completed(), stateStart=state.start(), stateEnd=state.end(), stateProgress=extraState(), stateComplete=state.complete(), daysShort=R.strings.tooltips.template.days.short(), hoursShort=R.strings.tooltips.template.hours.short(), minutesShort=R.strings.tooltips.template.minutes.short(), previewAnnounce=self._getVehiclePreviewBodyString(b'announce')(), previewInProgress=self._getVehiclePreviewBodyString(b'inprogress')())

    def _getIcons(self):
        return MarathonEventIconsData(tooltipHeader=backport.image(R.images.gui.maps.icons.quests.dyn(self._data.marathonTooltipHeader)()), okIcon=backport.image(self._getIconsResource(b'ok_icon')()), timeIcon=backport.image(self._getIconsResource(b'time_icon')()), timeIconGlow=backport.image(self._getIconsResource(b'time_icon_glow')()), alertIcon=backport.image(self._getIconsResource(b'alert_icon')()), iconFlag=backport.image(self._getIconsResource(b'icon_flag')()), saleIcon=backport.image(self._getIconsResource(b'sale_icon')()), mapFlagHeaderIcon={(MarathonState.ENABLED_STATE): (backport.image(self._getIconsResource(b'cup_icon')())), 
           (MarathonState.DISABLED_STATE): (backport.image(self._getIconsResource(b'cup_disable_icon')()))})

    def _getLabelObject(self, obj):
        resourceObj = obj.dyn(self._data.prefix)
        if resourceObj.isValid():
            return resourceObj
        return obj.marathon

    def _getResouce(self, obj, attr):
        resourceObj = obj.dyn(self._data.prefix)
        if resourceObj.isValid():
            string = resourceObj.dyn(attr)
            if string.isValid():
                return string
        return obj.marathon.dyn(attr)

    def _getTooltipString(self, attr):
        return self._getResouce(R.strings.tooltips, attr)

    def _getVehiclePreviewBodyString(self, attr):
        return self._getResouce(R.strings.marathon.vehiclePreview.title.tooltip.body, attr)

    def _getIconsResource(self, attr):
        return self._getResouce(R.images.gui.maps.icons.library, attr)
