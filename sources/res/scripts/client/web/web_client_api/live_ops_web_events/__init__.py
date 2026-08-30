from web.web_client_api import w2capi
from web.web_client_api.ui import ShopWebApiMixin

@w2capi(name=b'live_ops_web_events', key=b'action')
class LiveOpsWebEventsWebApi(ShopWebApiMixin):
    pass
