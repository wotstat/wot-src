import typing
from constants import IS_CHINA
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum
from gui.shared.formatters.date_time import getRegionalDateTime
from gui.shared.gui_items.Vehicle import getUserName
from helpers import dependency
from items.vehicles import getVehicleType
from messenger import g_settings
from messenger.formatters.service_channel import GeneralFormatter
from messenger.formatters.service_channel import ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData
from renewable_subscription_common.settings_constants import WotPlusTier, PRO_THRESHOLD_DAYS
from skeletons.gui.game_control import IWotPlusController
if typing.TYPE_CHECKING:
    from messenger.proto.bw.wrappers import ServiceChannelMessage
    from typing import Dict, Tuple

def getVehicleNameFromVehicleCD(message, messageDataKey):
    vehTypeCD = message.data.get(messageDataKey)
    if not vehTypeCD:
        return b''
    return getUserName(getVehicleType(vehTypeCD))


class WotPlusUnlockedAwardFormatter(GeneralFormatter):

    def __init__(self):
        super(WotPlusUnlockedAwardFormatter, self).__init__(b'')
        return

    def format(self, message, *args):
        return []


class _WotPlusDateTimeFormatter(GeneralFormatter):
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)

    def _getConvertedDateTime(self, dTime):
        return getRegionalDateTime(dTime or 0, DateTimeFormatsEnum.SHORTDATETIME)


class _WotPlusPeriodicityTimeFormatter(_WotPlusDateTimeFormatter):

    def _getPeriodicityMessageText(self, message):
        if message.get(b'billingDays', 0) > PRO_THRESHOLD_DAYS:
            return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfRenewalProYearly()
        return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfRenewalPro()

    def getText(self, message, *args):
        expiryTime = message.get(b'expiryTime', 0)
        return backport.text(self._getPeriodicityMessageText(message), time=self._getConvertedDateTime(expiryTime))


class WotPlusUnlockedFormatter(_WotPlusPeriodicityTimeFormatter):

    def __init__(self):
        super(WotPlusUnlockedFormatter, self).__init__(b'WotPlusUnlockMessage')
        return

    def _getPeriodicityMessageText(self, _):
        return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfRenewal()


class WotPlusCoreUnlockedFormatter(_WotPlusPeriodicityTimeFormatter):

    def __init__(self):
        super(WotPlusCoreUnlockedFormatter, self).__init__(b'WotPlusCoreUnlockMessage')
        return

    def _getPeriodicityMessageText(self, _):
        return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfRenewal()


class WotPlusProUnlockedFormatter(_WotPlusPeriodicityTimeFormatter):

    def __init__(self):
        super(WotPlusProUnlockedFormatter, self).__init__(b'WotPlusProUnlockMessage')
        return

    def _getPeriodicityMessageText(self, message):
        if message.get(b'periodicity', WotPlusPeriodicityEnum.P6MONTHS) == WotPlusPeriodicityEnum.P12MONTHS:
            return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfUnlockProYearly()
        return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfUnlockPro()


class WotPlusRenewedFormatter(_WotPlusPeriodicityTimeFormatter):

    def __init__(self):
        super(WotPlusRenewedFormatter, self).__init__(b'WotPlusRenewMessage')
        return

    def getTitle(self, message, *args):
        return backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.renewMessage.title())

    def getText(self, message, *args):
        return super(WotPlusRenewedFormatter, self).getText(message.data)

    def _getPeriodicityMessageText(self, _):
        return R.strings.messenger.serviceChannelMessages.wotPlus.nextDateOfRenewalChange()


class WotPlusUpgradeFormatter(_WotPlusPeriodicityTimeFormatter):

    def __init__(self):
        super(WotPlusUpgradeFormatter, self).__init__(b'WotPlusUpgradeMessage')
        return

    def getTitle(self, message, *args):
        return backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.upgradeMessage.title())

    def getText(self, message, *args):
        return super(WotPlusUpgradeFormatter, self).getText(message.data)


class WotPlusExpiredFormatter(_WotPlusDateTimeFormatter):

    def __init__(self):
        super(WotPlusExpiredFormatter, self).__init__(b'WotPlusExpireMessage')
        return

    def getTitle(self, message, *args):
        previousTier = message.data.get(b'previousTier', 0)
        timeOfExpiry = message.data.get(b'expiryTime', 0)
        if not IS_CHINA:
            if previousTier == WotPlusTier.PRO:
                messageTitle = R.strings.messenger.serviceChannelMessages.wotPlus.expireProMessage.title()
            else:
                messageTitle = R.strings.messenger.serviceChannelMessages.wotPlus.expireCoreMessage.title()
        else:
            messageTitle = R.strings.messenger.serviceChannelMessages.wotPlus.expireMessage.title()
        return backport.text(messageTitle, time=self._getConvertedDateTime(timeOfExpiry))


class PassiveXpActivatedFormatter(GeneralFormatter):

    def __init__(self):
        super(PassiveXpActivatedFormatter, self).__init__(b'PassiveXPStatusMessage')
        return

    def getText(self, message, *args):
        vehName = getVehicleNameFromVehicleCD(message, b'vehTypeCD')
        return backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.passiveXP.isActivated.text(), vehicleName=vehName)


class PassiveXpDeactivatedFormatter(GeneralFormatter):

    def __init__(self):
        super(PassiveXpDeactivatedFormatter, self).__init__(b'PassiveXPStatusMessage')
        return

    def getText(self, message, *args):
        vehName = getVehicleNameFromVehicleCD(message, b'vehTypeCD')
        return backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.passiveXP.isDeactivated.text(), vehicleName=vehName)


class PassiveXpSwitchedFormatter(GeneralFormatter):

    def __init__(self):
        super(PassiveXpSwitchedFormatter, self).__init__(b'PassiveXPSwitchedMessage')
        return

    def getValues(self, message, *args):
        oldVehTypeCD = message.data.get(b'oldVehTypeCD')
        newVehTypeCD = message.data.get(b'newVehTypeCD')
        oldVehName = getUserName(getVehicleType(oldVehTypeCD))
        newVehName = getUserName(getVehicleType(newVehTypeCD))
        return {b'oldVehName': oldVehName, b'newVehName': newVehName}


class PassiveXpIncompatibleCrewFormatter(GeneralFormatter):

    def __init__(self):
        super(PassiveXpIncompatibleCrewFormatter, self).__init__(b'PassiveXPIncompatibleCrewMessage')
        return

    def getValues(self, message, *args):
        vehName = getVehicleNameFromVehicleCD(message, b'vehTypeCD')
        return {b'vehicleName': vehName}


class PassiveXPDeactivateDueToPostProgressionFormatter(GeneralFormatter):

    def __init__(self):
        super(PassiveXPDeactivateDueToPostProgressionFormatter, self).__init__(b'PassiveXPDeactivateDueToPostProgression')
        return

    def getValues(self, message, *args):
        vehName = getVehicleNameFromVehicleCD(message, b'vehTypeCD')
        return {b'vehicleName': vehName}


class ProBoostActivatedFormatter(GeneralFormatter):

    def __init__(self):
        super(ProBoostActivatedFormatter, self).__init__(b'WotPlusProBoostActivatedMessage')
        return

    def getValues(self, message, *args):
        return {b'vehicleName': (getVehicleNameFromVehicleCD(message, b'vehTypeCD')), 
           b'cooldown': (message.data.get(b'cooldown', 0))}


class ProBoostDeactivatedFormatter(GeneralFormatter):

    def __init__(self):
        super(ProBoostDeactivatedFormatter, self).__init__(b'WotPlusProBoostDeactivatedMessage')
        return

    def getValues(self, message, *args):
        return {b'vehicleName': (getVehicleNameFromVehicleCD(message, b'vehTypeCD'))}


class ProBoostSwitchFormatter(GeneralFormatter):

    def __init__(self):
        super(ProBoostSwitchFormatter, self).__init__(b'WotPlusProBoostSwitchMessage')
        return

    def getValues(self, message, *args):
        return {b'vehicleNameTo': (getVehicleNameFromVehicleCD(message, b'vehTypeCDTo')), 
           b'vehicleNameFrom': (getVehicleNameFromVehicleCD(message, b'vehTypeCDFrom')), 
           b'cooldown': (message.data.get(b'cooldown', 0))}


class WotPlusSwitchFormatter(ServiceChannelFormatter):

    def format(self, template, *args):
        if template:
            formatted = g_settings.msgTemplates.format(template)
            return [
             MessageData(formatted, self._getGuiSettings(None, template))]
        else:
            return []
