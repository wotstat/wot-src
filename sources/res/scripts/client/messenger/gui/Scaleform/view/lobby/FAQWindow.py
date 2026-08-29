from gui.Scaleform.daapi.view.meta.FAQWindowMeta import FAQWindowMeta
from gui.shared.events import OpenLinkEvent
from messenger.gui.Scaleform.data.faq_data import FAQList
from messenger import g_settings
FAQ_BATCH_SIZE = 5

class FAQWindow(FAQWindowMeta):

    def __init__(self, ctx=None):
        super(FAQWindow, self).__init__()
        self.__list = None
        return

    def onWindowClose(self):
        self.destroy()
        return

    def onLinkClicked(self, eventType):
        self.fireEvent(OpenLinkEvent(eventType))
        return

    def updateData(self):
        formatHtml = g_settings.htmlTemplates.format
        batch = []
        item = self.__list.getItem(0)
        if item.question and item.answer:
            batch = [
             formatHtml(b'firstFAQItem', ctx=item._asdict())]
        for item in self.__list.getIterator(offset=1):
            if FAQ_BATCH_SIZE > len(batch):
                self.as_appendTextS((b'').join(batch))
                batch = []
            batch.append(formatHtml(b'nextFAQItem', ctx=item._asdict()))

        if batch:
            self.as_appendTextS((b'').join(batch))
        return

    def _populate(self):
        super(FAQWindow, self)._populate()
        self.__list = FAQList()
        self.updateData()
        return

    def _dispose(self):
        if self.__list:
            self.__list.clear()
            self.__list = None
        super(FAQWindow, self)._dispose()
        return
