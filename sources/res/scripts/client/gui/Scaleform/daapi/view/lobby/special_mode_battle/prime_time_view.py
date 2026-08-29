import time
from collections import namedtuple
from gui.Scaleform import MENU
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import PrimeTimeViewBase
from gui.Scaleform.daapi.view.lobby.prime_time_servers_data_provider import PrimeTimesServersDataProvider
from gui.shared.formatters import icons, text_styles
from helpers import time_utils
from helpers.i18n import makeString as _ms
LocaleData = namedtuple(b'LocaleData', (b'enableTitle', b'enableWelcomeTitle', b'enableBtnTitle', b'disableTitle', b'disableStatusTitle', b'disableStatusDescr', b'disableBtnTitle'))
ImgsData = namedtuple(b'ImgsData', (b'enableBackground', b'disableBackground'))

class SpecialModePrimeTimeView(PrimeTimeViewBase):

    def _getLocaleData(self):
        raise NotImplementedError
        return

    def _getImgsData(self):
        raise NotImplementedError
        return

    def _getAllServersDP(self):
        primeTimesForDay = self._getController().getPrimeTimesForDay(time.time(), groupIdentical=False)
        return PrimeTimesServersDataProvider(primeTimesForDay=primeTimesForDay)

    def _prepareData(self, serverList, serverName, serverTimeLeft):
        enableTitle, enableWelcomeTitle, enableBtnTitle, disableTitle, disableStatusTitle, disableStatusDescr, disableBtnTitle = self._getLocaleData()
        enableBackground, disableBackground = self._getImgsData()
        if self._isEnabled:
            timeLeftStr = time_utils.getTillTimeString(serverTimeLeft, MENU.HEADERBUTTONS_BATTLE_TYPES_RANKED_AVAILABILITY)
            status = text_styles.main(_ms(enableTitle, server=serverName, time=text_styles.warning(timeLeftStr)))
            mainBackground = enableBackground
            title = text_styles.epicTitle(enableWelcomeTitle)
            applyButtonLabel = _ms(enableBtnTitle)
        else:
            status = (b'{} {}\n{}').format(icons.alert(-3), text_styles.alert(disableStatusTitle), text_styles.main(disableStatusDescr))
            mainBackground = disableBackground
            title = text_styles.epicTitle(disableTitle)
            applyButtonLabel = _ms(disableBtnTitle)
        return {b'title': title, b'apply': applyButtonLabel, 
           b'mainBackground': mainBackground, 
           b'status': status, 
           b'serversDDEnabled': (len(serverList) > 1), 
           b'serverDDVisible': True}

    def _getPrbActionName(self, isEnabled):
        return self._getPrbForcedActionName()

    def _getEndSeasonTime(self):
        raise NotImplementedError
        return

    def _getTimeLeft(self, pID):
        primeTime = self._getController().getPrimeTimes().get(pID)
        if not primeTime:
            return 0
        _, timeLeft = primeTime.getAvailability(time_utils.getCurrentLocalServerTimestamp(), self._getEndSeasonTime())
        return timeLeft
