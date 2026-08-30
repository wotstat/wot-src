from __future__ import absolute_import
from adisp import adisp_process
from gui import GUI_SETTINGS, DialogsInterface, makeHtmlString
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.ReportBugPanelMeta import ReportBugPanelMeta
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IExternalLinksController

class ReportBugPanel(ReportBugPanelMeta):

    def reportBug(self):
        self.reportBugOpenConfirm()
        return

    def _populate(self):
        super(ReportBugPanel, self)._populate()
        if GUI_SETTINGS.reportBugLink:
            text = backport.text(R.strings.menu.ingame_menu.links.report_bug())
            reportBugLink = self.makeHyperLink(b'ingameMenu', text)
            self.as_setHyperLinkS(reportBugLink)
        return

    @staticmethod
    def makeHyperLink(linkType, text):
        ctx = {b'linkType': linkType, 
           b'text': text}
        linkHtml = makeHtmlString(b'html_templates:lobby/system_messages', b'link', ctx)
        return linkHtml

    @staticmethod
    @adisp_process
    def reportBugOpenConfirm():
        isOk = yield DialogsInterface.showI18nConfirmDialog(b'reportBug', focusedID=DIALOG_BUTTON_ID.SUBMIT)
        if isOk:
            links = dependency.instance(IExternalLinksController)
            links.open(GUI_SETTINGS.reportBugLink)
        return
