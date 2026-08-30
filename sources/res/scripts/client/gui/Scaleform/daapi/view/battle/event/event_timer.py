from gui import makeHtmlString
from gui.Scaleform.daapi.view.meta.EventTimerMeta import EventTimerMeta

class EventTimer(EventTimerMeta):
    _COLOR = b'#ffffff'
    _MESSAGE = b'timerEventMessage'
    _HTML_TEMPLATE_PATH = b'html_templates:battleTimer'
    _WAIT_TIME = 300
    _ALARM_TIME = 60
    _ALART_STATE_ENABLED = 1
    _ALART_STATE_DISABLED = 0
    _MAX_PROGRESS = 100
    _TITLE_TMPL = b'<font color="{color}">{text}</font>'
    _TIMER_TMPL = b'<font color="{color}">{min:02d}:{sec:02d}</font>'

    def __init__(self):
        super(EventTimer, self).__init__()
        self._waitTime = self._WAIT_TIME
        self._alarmTime = self._ALARM_TIME
        self._visible = True
        self._progress = 0
        return

    def _populate(self):
        super(EventTimer, self)._populate()
        self._onUpdateScenarioTimer(self._waitTime, self._alarmTime, self._visible)
        return

    def _dispose(self):
        self._waitTime = 0
        self._alarmTime = 0
        self._visible = False
        super(EventTimer, self)._dispose()
        return

    def _onUpdateScenarioTimer(self, waitTime, alarmTime, visible):
        self._waitTime = waitTime
        self._alarmTime = alarmTime
        self._visible = visible
        self._updateTimer()
        return

    def _updateTimer(self):
        if self._waitTime >= 0 and self._visible:
            m, s = divmod(int(self._waitTime), self._ALARM_TIME)
            timeLeft = self._TIMER_TMPL.format(color=self._COLOR, min=m, sec=s)
            message = makeHtmlString(self._HTML_TEMPLATE_PATH, self._MESSAGE)
            titlText = self._TITLE_TMPL.format(color=self._COLOR, text=message)
            timerStateAlarm = self._ALART_STATE_DISABLED
            if self._waitTime <= self._alarmTime:
                timerStateAlarm = self._ALART_STATE_ENABLED
                if self._waitTime == self._ALARM_TIME:
                    self.as_playFxS()
            self.as_setTimerStateS(timerStateAlarm)
            self.as_updateTimeS(timeLeft)
            if self._progress < self._MAX_PROGRESS:
                self.as_updateTitleS(titlText)
                self.as_updateProgressBarS(self._progress, True)
        else:
            self._hideTimer()
        return

    def _playFxS(self):
        self.as_playFxS()
        return

    def _hideTimer(self):
        self.as_updateTimeS(b'')
        self.as_updateTitleS(b'')
        self.as_updateProgressBarS(0, False)
        return

    def setProgress(self, progress):
        self._progress = progress
        return
