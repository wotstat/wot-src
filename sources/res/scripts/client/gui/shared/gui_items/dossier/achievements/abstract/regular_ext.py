from __future__ import absolute_import
from gui.shared.formatters import text_styles
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement
from helpers import i18n

class RegularExtAchievement(RegularAchievement):
    __slots__ = ()
    USER_DESCR_TEMPLATE = b'%(title)s\n<font size="3">&nbsp;</font>\n%(standard)s\n%(ext)s'
    USER_DESCR_WEB_TEMPLATE = b'%(title)s\n%(standard)s\n%(ext)s'

    def getUserDescription(self):
        return RegularExtAchievement.USER_DESCR_TEMPLATE % {b'title': (text_styles.main(self._getTranslatedText(b'#achievements:%s_descr'))), 
           b'standard': (text_styles.main(self._getStandardDescription())), 
           b'ext': (text_styles.main(self._getExtDescription()))}

    def getUserWebDescription(self):
        return RegularExtAchievement.USER_DESCR_WEB_TEMPLATE % {b'title': (i18n.makeString(b'#achievements:%s_descr' % self._getActualName())), 
           b'standard': (i18n.makeString(b'#achievements:%s_standard_descr' % self._getActualName(), condition=str(self._getStandardValues()) + self._getConditionText())), 
           b'ext': (i18n.makeString(b'#achievements:%s_ext_descr' % self._getActualName(), condition=str(self._getExtValues()) + self._getConditionText()))}

    def _getTranslatedText(self, translationRef):
        return text_styles.main(i18n.makeString(translationRef % self._getActualName()))

    def _getExtDescription(self):
        return self._getTranslatedText(b'#achievements:%s_ext_descr') % {b'condition': (text_styles.creditsSmall(str(self._getExtValues()) + self._getConditionText()))}

    def _getStandardDescription(self):
        return self._getTranslatedText(b'#achievements:%s_standard_descr') % {b'condition': (text_styles.creditsSmall(str(self._getStandardValues()) + self._getConditionText()))}

    def _getStandardValues(self):
        return

    def _getExtValues(self):
        return

    def _getConditionText(self):
        condTextKey = b'#achievements:%s_condition_text' % self._getActualName()
        if i18n.doesTextExist(condTextKey):
            return i18n.makeString(condTextKey)
        return b''
