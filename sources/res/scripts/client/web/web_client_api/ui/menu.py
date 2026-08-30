from types import NoneType
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import CustomUserCMHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IBrowserController
from web.web_client_api import WebCommandException, w2c, W2CSchema, Field

class _UserMenuSchema(W2CSchema):
    spa_id = Field(required=True, type=(int, long, basestring))
    user_name = Field(required=True, type=basestring)
    clan_abbrev = Field(type=(basestring, NoneType))
    custom_items = Field(type=list, default=[])
    excluded_items = Field(type=list, default=[])
    custom_items_after_end = Field(type=list, default=[])


class UserMenuWebApiMixin(object):
    browserController = dependency.descriptor(IBrowserController)

    @w2c(_UserMenuSchema, b'user_menu')
    def userMenu(self, cmd, ctx):
        context = {b'dbID': (cmd.spa_id), 
           b'userName': (cmd.user_name), 
           b'clanAbbrev': (cmd.clan_abbrev), 
           b'customItems': (cmd.custom_items), 
           b'excludedItems': (cmd.excluded_items), 
           b'customItemsAfterEnd': (cmd.custom_items_after_end)}
        callback = ctx.get(b'callback')
        appLoader = dependency.instance(IAppLoader)
        app = appLoader.getApp()
        try:
            app.contextMenuManager.show(CONTEXT_MENU_HANDLER_TYPE.CUSTOM_USER, context)
            cmHandler = app.contextMenuManager.getCurrentHandler()
        except AttributeError as ex:
            raise WebCommandException(b'Failed to show context menu: %s' % ex)

        if cmHandler is not None and isinstance(cmHandler, CustomUserCMHandler):
            webBrowser = self.browserController.getBrowser(ctx.get(b'browser_id'))
            webBrowser.allowMouseWheel = False

            def onSelectedCallback(optionId):
                callback({b'menu_type': b'user_menu', 
                   b'selected_item': optionId, 
                   b'spa_id': (cmd.spa_id)})
                webBrowser.allowMouseWheel = True
                return

            cmHandler.onSelected += onSelectedCallback
        else:
            return {b'menu_type': b'user_menu', b'selected_item': None, 
               b'spa_id': (cmd.spa_id)}
        return
