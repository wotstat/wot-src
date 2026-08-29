from gui import GUI_SETTINGS
from messenger import g_settings
from messenger.ext.filters import chain, collection
from messenger.storage import storage_getter
__all__ = (b'MessageFiltersChain',)

class MessageFiltersChain(chain.FiltersChain):

    def __init__(self):
        inFilters = [
         {b'name': b'htmlEscape', 
            b'filter': (collection.HtmlEscapeFilter()), 
            b'order': 0, 
            b'lock': True}]
        outFilters = [
         {b'name': b'normalizeLobbyMessage', 
            b'filter': (collection.NormalizeMessageFilter()), 
            b'order': 0, 
            b'lock': False}]
        super(MessageFiltersChain, self).__init__(inFilters, outFilters)
        return

    @storage_getter(b'playerCtx')
    def playerCtx(self):
        return

    def init(self):
        g_settings.onUserPreferencesUpdated += self.__ms_onUserPreferencesUpdated
        self.playerCtx.onAccountAttrsChanged += self.__pc_onAccountAttrsChanged
        self.__ms_onUserPreferencesUpdated()
        return

    def fini(self):
        g_settings.onUserPreferencesUpdated -= self.__ms_onUserPreferencesUpdated
        self.playerCtx.onAccountAttrsChanged -= self.__pc_onAccountAttrsChanged
        return

    def __ms_onUserPreferencesUpdated(self):
        if GUI_SETTINGS.postBattleExchange.enabled:
            self.addFilter(b'postBattleFilter', collection.PostBattleLinksFilter())
        if g_settings.userPrefs.enableOlFilter:
            if not self.hasFilter(b'enableOlFilter'):
                self.addFilter(b'olFilter', collection.getObsceneLanguageFilter(), removed=[
                 b'coloringOlFilter'])
        else:
            ctx = self.playerCtx
            isAdmin = ctx.isChatAdmin() or ctx.isGameAdmin()
            if isAdmin and not self.hasFilter(b'coloringOlFilter'):
                self.addFilter(b'coloringOlFilter', collection.ColoringObsceneLanguageFilter(), removed=[
                 b'olFilter'])
            else:
                self.removeFilter(b'olFilter')
        if g_settings.userPrefs.enableSpamFilter:
            self.addFilter(b'domainFilter', collection.DomainNameFilter())
            self.addFilter(b'spamFilter', collection.SpamFilter())
            self.addFilter(b'floodFilter', collection.FloodFilter())
        else:
            self.removeFilter(b'domainFilter')
            self.removeFilter(b'spamFilter')
            self.removeFilter(b'floodFilter')
        return

    def __pc_onAccountAttrsChanged(self):
        ctx = self.playerCtx
        if ctx.isChatAdmin() or ctx.isGameAdmin():
            if not g_settings.userPrefs.enableOlFilter and not self.hasFilter(b'coloringOlFilter'):
                self.addFilter(b'coloringOlFilter', collection.ColoringObsceneLanguageFilter(), removed=[
                 b'olFilter'])
        else:
            self.removeFilter(b'coloringOlFilter')
        return
