from gui.Scaleform.daapi.view.meta.PersonalMissionsAbstractInfoViewMeta import PersonalMissionsAbstractInfoViewMeta

class PersonalMissionFirstEntryAwardViewMeta(PersonalMissionsAbstractInfoViewMeta):

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return
