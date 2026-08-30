from constants import WG_GAMES
from gui.platform.base.request import Params
from gui.platform.wgnp.steam_account.response import WGNPSteamAccEmailAddResponse, WGNPSteamAccEmailConfirmResponse

class EmailStatusParams(Params):
    url = b'./personal/api/v2/account/email/state/'
    headers = {b'Content-Type': b'application/json'}
    method = b'POST'


class AddEmailParams(Params):
    response = WGNPSteamAccEmailAddResponse
    url = b'./personal/api/v2/account/email/create/'
    headers = {b'Content-Type': b'application/json'}
    proofOfWorkURL = b'./personal/api/v2/account/email/create/challenge/?type=pow'
    method = b'POST'
    queryParams = {b'type': b'pow'}
    postData = {b'game': (WG_GAMES.TANKS)}

    def __init__(self, urlHost, email):
        super(AddEmailParams, self).__init__(urlHost)
        self.postData[b'email'] = email
        return


class ConfirmEmailParams(Params):
    response = WGNPSteamAccEmailConfirmResponse
    url = b'./personal/api/v2/account/email/activate/'
    headers = {b'Content-Type': b'application/json'}
    method = b'POST'

    def __init__(self, urlHost, code):
        super(ConfirmEmailParams, self).__init__(urlHost)
        self.postData[b'code'] = code
        return
