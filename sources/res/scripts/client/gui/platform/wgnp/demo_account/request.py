from constants import CURRENT_GAME_ID
from gui.platform.base.request import Params, ContentType
from gui.platform.wgnp.demo_account.response import WGNPDemoAccCredentialsAddResponse, WGNPDemoAccCredentialsConfirmResponse, WGNPDemoAccChangeNicknameResponse, WGNPDemoAccValidateNicknameResponse

class CredentialsStatusParams(Params):
    url = b'./personal/api/v2/account/credentials/basic/create/'
    method = b'GET'


class AddCredentialsParams(Params):
    response = WGNPDemoAccCredentialsAddResponse
    url = b'./personal/api/v2/account/credentials/basic/create/'
    headers = {b'Content-Type': (ContentType.FORM_URLENCODED.value)}
    proofOfWorkURL = b'./personal/api/v2/account/credentials/basic/create/challenge/?type=pow'
    method = b'POST'
    queryParams = {b'type': b'pow'}
    postData = {b'game': CURRENT_GAME_ID}

    def __init__(self, urlHost, login, password):
        super(AddCredentialsParams, self).__init__(urlHost)
        self.postData[b'login'] = login
        self.postData[b'password'] = password
        return


class ConfirmCredentialsParams(Params):
    response = WGNPDemoAccCredentialsConfirmResponse
    url = b'./personal/api/v2/account/credentials/basic/activate/'
    headers = {b'Content-Type': (ContentType.FORM_URLENCODED.value)}
    method = b'POST'
    postData = {b'game': CURRENT_GAME_ID}

    def __init__(self, urlHost, code):
        super(ConfirmCredentialsParams, self).__init__(urlHost)
        self.postData[b'code'] = code
        return


class NicknameStatusParams(Params):
    url = b'./personal/api/v2/account/name/update/state/'
    method = b'POST'


class ValidateNicknameParams(Params):
    response = WGNPDemoAccValidateNicknameResponse
    headers = {b'Content-Type': (ContentType.FORM_URLENCODED.value)}
    url = b'./personal/account/nicknames/{nickname}/'
    postData = {b'suggestions': 1, b'use_pattern': 1}
    method = b'POST'
    auth = False
    addUserAgentHeader = False

    def __init__(self, urlHost, nickname):
        super(ValidateNicknameParams, self).__init__(urlHost)
        self.url = self.url.format(nickname=nickname)
        return


class ChangeNicknameParams(Params):
    response = WGNPDemoAccChangeNicknameResponse
    url = b'./personal/api/v2/account/name/update/'
    headers = {b'Content-Type': (ContentType.FORM_URLENCODED.value)}
    method = b'POST'
    postData = {b'game': CURRENT_GAME_ID, b'via': CURRENT_GAME_ID}

    def __init__(self, urlHost, nickname, cost):
        super(ChangeNicknameParams, self).__init__(urlHost)
        self.postData[b'name'] = nickname
        self.postData[b'cost'] = cost
        return
