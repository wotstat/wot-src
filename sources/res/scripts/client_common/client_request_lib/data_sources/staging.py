from __future__ import absolute_import
import functools, json
from datetime import datetime, time as dt_time
from functools import wraps
from future.moves.urllib.parse import urlencode
from future.utils import viewitems
from itertools import groupby
from client_request_lib import exceptions
from client_request_lib.data_sources import base

def _doResponse(callback, result, status_code, response_code):
    callback(result, status_code, response_code)
    return


EXAMPLES = {}
SUCCESS_STATUSES = [
 200, 201, 304]

def convert_data(data_mapping, paginated=False):

    def wrapper(func):

        @functools.wraps(func)
        def wrapped(self, callback, *args, **kwargs):

            def new_callback(data, *args, **kwargs):
                for field, converter in data_mapping.items():
                    listed_data = data
                    if paginated:
                        listed_data = data.get(b'items', [])
                    if not isinstance(listed_data, list):
                        listed_data = [
                         listed_data]
                    for portion in listed_data:
                        if field in portion:
                            portion[field] = converter(portion[field])

                callback(data, *args, **kwargs)
                return

            func(self, new_callback, *args, **kwargs)
            return

        return wrapped

    return wrapper


def from_iso(iso_date):
    if iso_date:
        if b'.' in iso_date:
            format = b'%Y-%m-%dT%H:%M:%S.%f'
        else:
            format = b'%Y-%m-%dT%H:%M:%S'
        return datetime.strptime(iso_date, format)
    return iso_date


def timestamp_to_datetime(timestamp):
    return timestamp and datetime.fromtimestamp(timestamp)


def translate_field_names(response, field_mapping, requested_fields=None):
    if requested_fields:
        field_mapping = {k: v for k, v in viewitems(field_mapping) if k in requested_fields}
    if isinstance(response, list):
        return [translate_field_names(i, field_mapping) for i in response]
    backward_mapping = sorted((v, k) for k, v in viewitems(field_mapping))
    result = {}
    for key, field_iter in groupby(backward_mapping, key=(lambda x: x[0].split(b'.', 1)[0])):
        inner_mapping = {}
        sibling_mapping = {}
        our = b''
        for their, our in field_iter:
            if b'.' in their:
                if b'.' in our:
                    inner_mapping[our.split(b'.', 1)[1]] = their.split(b'.', 1)[1]
                else:
                    sibling_mapping[our] = their.split(b'.', 1)[1]
            elif their in response:
                result[our] = response[their]

        if key in response:
            if sibling_mapping:
                siblings = translate_field_names(response[key], sibling_mapping)
                result.update(siblings)
            if inner_mapping:
                result.update({(our.split(b'.')[0]): (translate_field_names(response[key], inner_mapping))})

    return result


def generate_docstring_mapping(field_mapping):
    result = [
     b'\n        .. list-table::\n            :widths: 50 50\n            :header-rows: 1\n\n            * - client_request_lib\n            - Backend\n    ']
    for our, their in viewitems(field_mapping):
        row = (b'\n            * - ``{our}``\n            - ``{their}``\n        ').format(our=our, their=their)
        result.append(row)

    return (b'').join(result)


def mapped_fields(field_mapping, paginated=False, accept_fields_argument=True):

    def wrapper(func):

        @wraps(func)
        def wrapped(self, callback, *args, **kwargs):
            old_fields = None
            if accept_fields_argument:
                if kwargs.get(b'fields'):
                    old_fields = kwargs[b'fields']
                    kwargs[b'fields'] = [field_mapping[f] for f in kwargs[b'fields']]
                else:
                    old_fields = field_mapping.keys()
                    kwargs[b'fields'] = field_mapping.values()
                if paginated and kwargs.get(b'get_total_count'):
                    kwargs[b'fields'].append(b'total')

            def wrapped_callback(response, status_code, response_code):
                if status_code in SUCCESS_STATUSES:
                    if paginated:
                        new_response = {b'items': [translate_field_names(i, field_mapping, requested_fields=old_fields) for i in response[b'items']]}
                        if kwargs.get(b'get_total_count'):
                            new_response[b'total'] = response[b'total']
                        response = new_response
                    elif isinstance(response, list):
                        response = [translate_field_names(i, field_mapping, requested_fields=old_fields) for i in response]
                    else:
                        response = translate_field_names(response, field_mapping, requested_fields=old_fields)
                callback(response, status_code, response_code)
                return

            func(self, wrapped_callback, *args, **kwargs)
            return

        if wrapped.__doc__ is not None:
            wrapped.__doc__ = (b'\n\n').join([
             wrapped.__doc__, generate_docstring_mapping(field_mapping)])
        return wrapped

    return wrapper


def get_clan_error(data):
    error_map = {b'DATA_ERROR': (exceptions.BadRequest), 
       b'SPA_ERROR': (exceptions.SpaError), 
       b'PERMISSION_DENIED': (exceptions.PermissionDenied), 
       b'ACCOUNT_ALREADY_IN_CLAN': (exceptions.AccountInClanError), 
       b'ACCOUNT_NOT_IN_CLAN': (exceptions.AccountNotInClanError), 
       b'STRONGHOLD_NOT_FOUND': (exceptions.StrongholdNotFoundError), 
       b'TOO_MANY_INVITES': (exceptions.TooManyInvitesError), 
       b'WGCCFE_ERROR': (exceptions.WgccfeError), 
       b'ACCOUNT_DOES_NOT_MEET_REQUIREMENTS': (exceptions.AccountRequirementsError), 
       b'APPLICATION_DOES_NOT_EXIST': (exceptions.ApplicationDoesNotExistError), 
       b'CLAN_ALREADY_DISBANDED': (exceptions.ClanDisbandedError), 
       b'INVITE_IS_NOT_ACTIVE': (exceptions.InviteIsNotActiveError), 
       b'CLAN_IS_FULL': (exceptions.ClanIsFullError), 
       b'INVITE_DOES_NOT_EXIST': (exceptions.InviteDoesNotExistError), 
       b'RECRUITING_POLICY_MISMATCH': (exceptions.RecruitingPolicyError), 
       b'ACCOUNT_BANNED': (exceptions.AccountBannedError), 
       b'TOO_MANY_APPLICATIONS': (exceptions.TooManyApplicationsError), 
       b'APPLICATION_IS_NOT_ACTIVE': (exceptions.ApplicationIsNotActiveError), 
       b'WGCCBE_ERROR': (exceptions.WgccbeError), 
       b'CLAN_DOES_NOT_EXIST': (exceptions.ClanDoesNotExistError), 
       b'UNKNOWN_ACCOUNT': (exceptions.UnknownAccountError), 
       b'CLAN_IS_NOT_ACTIVE': (exceptions.ClanIsNotActiveError)}
    error_key = data and data[b'title']
    return error_map.get(error_key, exceptions.WgccbeError)


def get_stronghold_error(data):
    error_map = {b'VALIDATION_ERROR': (exceptions.BadRequest), 
       b'SPA_ACCOUNT_DOES_NOT_EXIST': (exceptions.UnknownAccountError), 
       b'SPA_ERROR': (exceptions.SpaError), 
       b'CLAN_DOES_NOT_EXIST': (exceptions.ClanDoesNotExistError), 
       b'BE_ERROR': (exceptions.WgccbeError), 
       b'CLAN_IS_DISBANDED': (exceptions.ClanDisbandedError), 
       b'STRONGHOLD_NOT_FOUND': (exceptions.StrongholdNotFoundError)}
    error_key = data and data[b'error']
    return error_map.get(error_key, exceptions.WgccfeError)


def get_spa_error(data):
    return exceptions.SpaError


def get_global_map_error(data):
    return exceptions.GlobalMapError


def get_exporter_error(data):
    error = b'Ensure each value is less than or equal to 9223372036854775807.'
    if data and error in data.get(b'account_ids', []):
        return exceptions.BadRequest
    return exceptions.ExporterError


def get_ratings_error(data):
    return exceptions.WgrsError


def get_wgsh_error(data):
    return exceptions.WgshError


ERROR_MAP = {b'ratings': get_ratings_error, 
   b'exporter': get_exporter_error, 
   b'global_map': get_global_map_error, 
   b'clans': get_clan_error, 
   b'spa': get_spa_error, 
   b'strongholds': get_stronghold_error, 
   b'wgsh': get_wgsh_error}

def preprocess_callback(callback, service):

    def wrapper(something):

        def wrapped(response, func=something):
            if response.responseCode not in SUCCESS_STATUSES:
                try:
                    data = json.loads(response.body)
                except:
                    data = None

                error = ERROR_MAP[service](data)
                return callback({b'description': (error.description)}, error.status_code, error.response_code)
            else:
                data = json.loads(response.body)
                response_code = exceptions.ResponseCodes.NO_ERRORS
                if func:
                    data = func(data)
                callback(data, response.responseCode, response_code)
                return

        if not callable(something):
            return wrapped(something, func=None)
        else:
            functools.wraps(something)(wrapped)
            return wrapped

    return wrapper


class StagingDataAccessor(base.BaseDataAccessor):
    requests_before_logout = -1

    def __init__(self, url_fetcher, staging_hosts=None, client_lang=None, user_agent=None):
        super(StagingDataAccessor, self).__init__()
        self.client_lang = client_lang
        self._account = None
        self.url_fetcher = url_fetcher
        self.staging_hosts = staging_hosts or {}
        self.user_agent = user_agent
        return

    def login(self, callback, account_id, spa_token):
        self._account = account_id
        result, status_code = (b'ok', 200)
        response_code = exceptions.ResponseCodes.NO_ERRORS
        callback(result, status_code, response_code)
        return

    def logout(self, callback):
        self._account = None
        result, status_code = (b'ok', 200)
        response_code = exceptions.ResponseCodes.NO_ERRORS
        callback(result, status_code, response_code)
        return

    def get_alive_status(self, callback):
        result, status_code = {b'status': b'I am alive!'}, 200
        response_code = exceptions.ResponseCodes.NO_ERRORS
        callback(result, status_code, response_code)
        return

    def _request_data(self, callback, service, url, method=b'GET', postData=None):
        service_host = self.staging_hosts[service].strip(b'/')
        url = (b'/').join([service_host] + url.strip(b'/').split(b'/'))
        if b'?' not in url:
            url = url + b'/'
        args = [
         None, 30.0, method]
        if postData:
            args.append(json.dumps(postData))
        self.url_fetcher(url, callback, *args)
        return

    @mapped_fields({b'efficiency': b'efficiency', 
       b'clan_id': b'clan_id', b'battles_count_avg': b'battles_count_avg', 
       b'wins_ratio_avg': b'wins_ratio_avg', 
       b'xp_avg': b'xp_avg', b'gm_elo_rating_6': b'gm_elo_rating_6', 
       b'gm_elo_rating_8': b'gm_elo_rating_8', 
       b'gm_elo_rating_10': b'gm_elo_rating_10', 
       b'gm_elo_rating_6_rank': b'gm_elo_rating_6_rank', 
       b'gm_elo_rating_8_rank': b'gm_elo_rating_8_rank', 
       b'gm_elo_rating_10_rank': b'gm_elo_rating_10_rank', 
       b'fb_elo_rating_8': b'fb_elo_rating_8', 
       b'fb_elo_rating_10': b'fb_elo_rating_10', 
       b'fb_battles_count_10_28d': b'fb_battles_count_10_28d', 
       b'fs_battles_count_10_28d': b'fs_battles_count_10_28d', 
       b'gm_battles_count_28d': b'gm_battles_count_28d', 
       b'fs_battles_count_28d': b'fs_battles_count_28d', 
       b'fb_battles_count_28d': b'fb_battles_count_28d'})
    def get_clans_ratings(self, callback, clan_ids, fields=None):
        get_params = {b'project': b'api', 
           b'fields': ((b',').join(fields)), 
           b'ids': ((b',').join(map(str, clan_ids)))}
        url = b'api/wot/clans/bulks/?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'ratings')
        def inner_callback(data):
            return data[b'data']

        return self._request_data(inner_callback, b'ratings', url)

    @convert_data({b'created_at': from_iso})
    @mapped_fields({b'name': b'name', 
       b'tag': b'tag', b'motto': b'motto', b'leader_id': b'leader_id', 
       b'members_count': b'members_count', b'created_at': b'created_at', 
       b'clan_id': b'id', b'treasury': b'treasury', b'accepts_join_requests': b'accepts_join_requests'})
    def get_clans_info(self, callback, clan_ids, fields=None):
        get_params = {b'ids': ((b',').join(map(str, clan_ids))), 
           b'fields': ((b',').join(fields))}
        url = b'/clans/?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            return data[b'items']

        return self._request_data(inner_callback, b'clans', url)

    @mapped_fields({b'id': b'id', b'name': b'name'})
    def get_accounts_names(self, callback, account_ids, fields=None):
        get_params = {b'id': account_ids}
        url = b'/spa/accounts/names/?%s' % urlencode(get_params, doseq=True)

        @preprocess_callback(callback, b'spa')
        def inner_callback(data):
            return [{b'id': k, b'name': v} for k, v in viewitems(data)]

        return self._request_data(inner_callback, b'spa', url)

    @convert_data({b'joined_at': from_iso})
    @mapped_fields({b'account_id': b'id', 
       b'joined_at': b'joined_at', 
       b'clan_id': b'clan_id', 
       b'role_bw_flag': b'role.bw_flag', 
       b'role_name': b'role.name'})
    def get_clan_members(self, callback, clan_id, fields=None):
        get_params = {b'fields': ((b',').join(fields))}
        url = b'/clans/%s/members?%s' % (clan_id, urlencode(get_params))
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'favorite_primetime': (lambda x: x and datetime.strptime(x, b'%H:%M').time())})
    @mapped_fields({b'favorite_arena_6': b'favorite_arena_6', 
       b'favorite_arena_8': b'favorite_arena_8', 
       b'favorite_arena_10': b'favorite_arena_10', 
       b'clan_id': b'clan_id', 
       b'favorite_primetime': b'favorite_primetime'})
    def get_clan_favorite_attributes(self, callback, clan_id, fields=None):
        get_params = {b'clan_id': clan_id}
        url = b'/gm/clans/favorite_attributes/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'joined_at': from_iso, b'in_clan_cooldown_till': from_iso})
    @mapped_fields({b'account_id': b'id', 
       b'joined_at': b'joined_at', 
       b'clan_id': b'clan_id', 
       b'role_bw_flag': b'role.bw_flag', 
       b'role_name': b'role.name', 
       b'in_clan_cooldown_till': b'in_clan_cooldown_till'})
    def get_accounts_clans(self, callback, account_ids, fields=None):
        get_params = {b'fields': ((b',').join(fields)), 
           b'ids': ((b',').join(map(str, account_ids)))}
        url = b'/accounts/?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            return data[b'items']

        return self._request_data(inner_callback, b'clans', url)

    @mapped_fields({b'total': b'total'}, accept_fields_argument=False)
    def get_account_applications_count_since(self, callback, account_id, since=None):
        get_params = {b'fields': b'id', 
           b'account_id': account_id, 
           b'created_after': (since.isoformat())}
        url = b'/applications/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @mapped_fields({b'total': b'total'}, accept_fields_argument=False)
    def get_clan_invites_count_since(self, callback, clan_id, since=None):
        get_params = {b'fields': b'id', 
           b'clan_id': clan_id, 
           b'created_after': (since.isoformat())}
        url = b'/invites/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'created_at': from_iso, b'updated_at': from_iso}, paginated=True)
    @mapped_fields({b'status': b'status', 
       b'created_at': b'created_at', 
       b'updated_at': b'updated_at', 
       b'sender_id': b'sender_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id', 
       b'comment': b'data.comment', 
       b'status_changer_id': b'data.status_changer_id'}, paginated=True)
    def get_account_applications(self, callback, fields=None, statuses=None, get_total_count=False, limit=18, offset=0):
        statuses = statuses or [1, 2, 3, 4, 5, 6]
        get_params = {b'fields': ((b',').join(fields)), 
           b'account_id': (self._account), 
           b'statuses': ((b',').join(statuses)), 
           b'limit': limit, 
           b'offset': offset}
        url = b'/applications/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'created_at': from_iso, b'updated_at': from_iso}, paginated=True)
    @mapped_fields({b'status': b'status', 
       b'created_at': b'created_at', 
       b'updated_at': b'updated_at', 
       b'sender_id': b'sender_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id', 
       b'comment': b'data.comment', 
       b'status_changer_id': b'data.status_changer_id'}, paginated=True)
    def get_clan_applications(self, callback, clan_id, fields=None, statuses=None, get_total_count=False, limit=18, offset=0):
        statuses = statuses or [1, 2, 3, 4, 5, 6]
        get_params = {b'fields': ((b',').join(fields)), 
           b'clan_id': clan_id, 
           b'statuses': ((b',').join(statuses)), 
           b'limit': limit, 
           b'offset': offset}
        url = b'/applications/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @mapped_fields({b'clan_id': b'clan_id', b'id': b'id', b'account_id': b'account_id'})
    def create_applications(self, callback, clan_ids, comment, fields=None):
        url = b'/applications/'
        data = {b'account_id': (self._account), 
           b'clan_ids': clan_ids, 
           b'comment': comment}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            return data.values()

        return self._request_data(inner_callback, b'clans', url, method=b'POST', postData=data)

    @mapped_fields({b'transaction_id': b'transaction_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id'})
    def accept_application(self, callback, application_id, fields=None):
        url = b'/applications/%s/' % application_id
        data = {b'initiator_id': (self._account), b'status': b'accepted'}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            data = data or {}
            data[b'account_id'] = data.pop(b'account_ids')[0]
            data[b'id'] = application_id
            return data

        return self._request_data(inner_callback, b'clans', url, method=b'PATCH', postData=data)

    @mapped_fields({b'transaction_id': b'transaction_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id'})
    def decline_application(self, callback, application_id, fields=None):
        url = b'/applications/%s/' % application_id
        data = {b'initiator_id': (self._account), b'status': b'declined'}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            data = data or {}
            data[b'id'] = application_id
            return data

        return self._request_data(inner_callback, b'clans', url, method=b'PATCH', postData=data)

    @mapped_fields({b'clan_id': b'clan_id', b'id': b'id', b'account_id': b'account_id'})
    def create_invites(self, callback, clan_id, account_ids, comment, fields=None):
        url = b'/invites/'
        data = {b'initiator_id': (self._account), 
           b'clan_id': clan_id, 
           b'account_ids': account_ids, 
           b'comment': comment}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            return data.values()

        return self._request_data(inner_callback, b'clans', url, method=b'POST', postData=data)

    @mapped_fields({b'transaction_id': b'transaction_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id'})
    def accept_invite(self, callback, invite_id, fields=None):
        url = b'/invites/%s/' % invite_id
        data = {b'initiator_id': (self._account), b'status': b'accepted'}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            data = data or {}
            data[b'account_id'] = data.pop(b'account_ids')[0]
            data[b'id'] = invite_id
            return data

        return self._request_data(inner_callback, b'clans', url, method=b'PATCH', postData=data)

    @mapped_fields({b'transaction_id': b'transaction_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id'})
    def decline_invite(self, callback, invite_id, fields=None):
        url = b'/invites/%s/' % invite_id
        data = {b'initiator_id': (self._account), b'status': b'declined'}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            data = data or {}
            data[b'id'] = invite_id
            return data

        return self._request_data(inner_callback, b'clans', url, method=b'PATCH', postData=data)

    @mapped_fields({b'id': b'id', b'clan_id': b'clan_id', b'account_id': b'account_id'})
    def bulk_decline_invites(self, callback, invite_ids, fields=None):
        url = b'/invites/'
        data = {b'initiator_id': (self._account), b'status': b'declined', b'ids': invite_ids}

        @preprocess_callback(callback, b'clans')
        def inner_callback(data):
            data = data and data[b'items'] or {}
            return data

        return self._request_data(inner_callback, b'clans', url, method=b'PATCH', postData=data)

    @convert_data({b'created_at': from_iso}, paginated=True)
    @mapped_fields({b'name': b'name', 
       b'tag': b'tag', b'motto': b'motto', b'leader_id': b'leader_id', 
       b'members_count': b'members_count', b'created_at': b'created_at', 
       b'clan_id': b'id', b'treasury': b'treasury', b'accepts_join_requests': b'accepts_join_requests'}, paginated=True)
    def search_clans(self, callback, search, get_total_count=False, fields=None, offset=0, limit=18):
        get_params = {b'search': search, 
           b'game': b'wot', 
           b'fields': ((b',').join(fields)), 
           b'limit': limit, 
           b'offset': offset}
        url = b'/clans/search/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'created_at': from_iso}, paginated=True)
    @mapped_fields({b'name': b'name', 
       b'tag': b'tag', b'motto': b'motto', b'leader_id': b'leader_id', 
       b'members_count': b'members_count', b'created_at': b'created_at', 
       b'clan_id': b'id', b'treasury': b'treasury', b'accepts_join_requests': b'accepts_join_requests'}, paginated=True)
    def get_recommended_clans(self, callback, get_total_count=False, fields=None, offset=0, limit=18):
        get_params = {b'game': b'wot', 
           b'fields': ((b',').join(fields)), 
           b'limit': limit, 
           b'offset': offset}
        url = b'/clans/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'created_at': from_iso, b'updated_at': from_iso}, paginated=True)
    @mapped_fields({b'status': b'status', 
       b'created_at': b'created_at', 
       b'updated_at': b'updated_at', 
       b'sender_id': b'sender_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id', 
       b'comment': b'data.comment', 
       b'status_changer_id': b'data.status_changer_id'}, paginated=True)
    def get_clan_invites(self, callback, clan_id, fields=None, statuses=None, get_total_count=False, limit=18, offset=0):
        statuses = statuses or [1, 2, 3, 4, 5, 6]
        get_params = {b'fields': ((b',').join(fields)), 
           b'clan_id': clan_id, 
           b'statuses': ((b',').join(statuses)), 
           b'limit': limit, 
           b'offset': offset}
        url = b'/invites/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @convert_data({b'created_at': from_iso, b'updated_at': from_iso}, paginated=True)
    @mapped_fields({b'status': b'status', 
       b'created_at': b'created_at', 
       b'updated_at': b'updated_at', 
       b'sender_id': b'sender_id', 
       b'id': b'id', 
       b'account_id': b'account_id', 
       b'clan_id': b'clan_id', 
       b'comment': b'data.comment', 
       b'status_changer_id': b'data.status_changer_id'}, paginated=True)
    def get_account_invites(self, callback, fields=None, statuses=None, get_total_count=False, limit=18, offset=0):
        statuses = statuses or [1, 2, 3, 4, 5, 6]
        get_params = {b'fields': ((b',').join(fields)), 
           b'account_id': (self._account), 
           b'statuses': ((b',').join(statuses)), 
           b'limit': limit, 
           b'offset': offset}
        url = b'/invites/?%s' % urlencode(get_params)
        return self._request_data(preprocess_callback(callback, b'clans'), b'clans', url)

    @mapped_fields({b'global_rating': b'summary.global_rating', 
       b'battle_avg_xp': b'summary.battle_avg_xp', 
       b'battles_count': b'summary.battles_count', 
       b'battle_avg_performance': b'summary.battle_avg_performance', 
       b'xp_amount': b'summary.xp_amount', 
       b'account_id': b'account_id'})
    def get_accounts_info(self, callback, account_ids, fields=None):
        fields = [i.split(b'.', 1) for i in fields if i != b'account_id']
        grouped = groupby(sorted(fields), key=(lambda x: x[0]))
        sections = [b'%s[%s]' % (k, (b',').join([j[1] for j in v])) for k, v in grouped]
        get_params = {b'account_ids': ((b',').join(map(str, account_ids))), 
           b'sections': ((b',').join(sections))}
        url = b'/wot/accounts/?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'exporter')
        def inner_callback(data):
            new_data = []
            for account_id, values in data.items():
                values[b'account_id'] = account_id
                new_data.append(values)

            return new_data

        return self._request_data(inner_callback, b'exporter', url)

    @convert_data({b'pillage_end_datetime': from_iso, 
       b'prime_time': (lambda x: x and datetime.strptime(x, b'%H:%M').time())})
    @mapped_fields({b'front_name': b'frontname', 
       b'province_id': b'province_id', 
       b'front_name_localized': b'frontname_localized', 
       b'province_id_localized': b'province_id_localized', 
       b'revenue': b'daily_revenue', 
       b'hq_connected': b'hq_connected', 
       b'prime_time': b'primetime', 
       b'game_map': b'game_map', 
       b'periphery': b'periphery_id', 
       b'turns_owned': b'turns_owned', 
       b'pillage_cooldown': b'pillage_cooldown', 
       b'pillage_end_datetime': b'pillage_end_datetime', 
       b'arena_id': b'arena_id'})
    def get_clan_provinces(self, callback, clan_id, fields=None):
        get_params = {b'clans': ((b',').join(map(str, [clan_id])))}
        url = b'/clans/provinces/?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'global_map')
        def inner_callback(data):
            res = data[b'clans'] and data[b'clans'][0][b'provinces']
            for i in res:
                i[b'frontname_localized'] = i[b'frontname']
                i[b'province_id_localized'] = i[b'province_id']

            return res

        return self._request_data(inner_callback, b'global_map', url)

    @mapped_fields({b'battles_lost': b'battles_lost', 
       b'battles_played': b'battles_played', 
       b'battles_played_on_10_level': b'battles_played_on_10_level', 
       b'battles_played_on_6_level': b'battles_played_on_6_level', 
       b'battles_played_on_8_level': b'battles_played_on_8_level', 
       b'battles_won': b'battles_won', 
       b'battles_won_on_10_level': b'battles_won_on_10_level', 
       b'battles_won_on_6_level': b'battles_won_on_6_level', 
       b'battles_won_on_8_level': b'battles_won_on_8_level', 
       b'influence_points': b'influence_points', 
       b'provinces_captured': b'provinces_captured', 
       b'provinces_count': b'provinces_count'})
    def get_clan_globalmap_stats(self, callback, clan_id, fields=None):
        get_params = {b'clans': ((b',').join(map(str, [clan_id])))}
        url = b'/clans/stats?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'global_map')
        def inner_callback(data):
            return data[b'clans'][0][b'stats']

        return self._request_data(inner_callback, b'global_map', url)

    @mapped_fields({b'front_name': b'id', 
       b'front_name_localized': b'id_localized', 
       b'min_vehicle_level': b'min_vehicle_level', 
       b'max_vehicle_level': b'max_vehicle_level'})
    def get_fronts_info(self, callback, front_names=None, fields=None):
        url = b'/fronts/'

        @preprocess_callback(callback, b'global_map')
        def inner_callback(data):
            res = data[b'fronts']
            for i in res:
                i[b'id_localized'] = i[b'id']

            return res

        return self._request_data(inner_callback, b'global_map', url)

    @convert_data({b'defence_hour': (lambda x: dt_time(x, 0) if x >= 0 else None)})
    @mapped_fields({b'buildings.direction': b'buildings.direction', 
       b'buildings.type': b'buildings.type', 
       b'buildings.level': b'buildings.level', 
       b'buildings.position': b'buildings.position', 
       b'defence_attack_efficiency': b'defence_attack_efficiency', 
       b'defence_battles_count': b'defence_battles_count', 
       b'defence_capture_enemy_building_total_count': b'defence_capture_enemy_building_total_count', 
       b'defence_combat_wins': b'defence_combat_wins', 
       b'defence_defence_efficiency': b'defence_defence_efficiency', 
       b'defence_enemy_base_capture_count': b'defence_enemy_base_capture_count', 
       b'defence_loss_own_building_total_count': b'defence_loss_own_building_total_count', 
       b'defence_resource_capture_count': b'defence_resource_capture_count', 
       b'defence_resource_loss_count': b'defence_resource_loss_count', 
       b'sortie_absolute_battles_count': b'sortie_absolute_battles_count', 
       b'sortie_battles_count': b'sortie_battles_count', 
       b'sortie_champion_battles_count': b'sortie_champion_battles_count', 
       b'sortie_middle_battles_count': b'sortie_middle_battles_count', 
       b'defence_attack_count': b'defence_attack_count', 
       b'defence_defence_count': b'defence_defence_count', 
       b'defence_success_attack_count': b'defence_success_attack_count', 
       b'defence_success_defence_count': b'defence_success_defence_count', 
       b'sortie_fort_resource_in_absolute': b'sortie_fort_resource_in_absolute', 
       b'sortie_fort_resource_in_champion': b'sortie_fort_resource_in_champion', 
       b'sortie_fort_resource_in_middle': b'sortie_fort_resource_in_middle', 
       b'sortie_losses': b'sortie_losses', 
       b'sortie_wins': b'sortie_wins', 
       b'level': b'level', 
       b'defence_hour': b'defence_hour', 
       b'defence_mode_is_activated': b'defence_mode_is_activated', 
       b'fb_battles_count_10': b'fb_battles_count_10', 
       b'fb_battles_count_8': b'fb_battles_count_8', 
       b'total_resource_amount': b'total_resource_amount'})
    def get_stronghold_info(self, callback, clan_id=None, fields=None):
        get_params = urlencode({b'performer_id': (self._account)})
        try:
            clan_id = int(clan_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = b'api/strongholds/%s/' % clan_id
        if self._account:
            url = (b'?').join([url, get_params])

        @preprocess_callback(callback, b'strongholds')
        def inner_callback(data):
            return data[b'stronghold']

        return self._request_data(inner_callback, b'strongholds', url)

    @convert_data({b'vacation_finish': timestamp_to_datetime, b'vacation_start': timestamp_to_datetime})
    @mapped_fields({b'buildings.type': b'buildings.type', 
       b'buildings.hp': b'buildings.hp', 
       b'buildings.direction': b'buildings.direction', 
       b'buildings.position': b'buildings.position', 
       b'buildings.storage': b'buildings.resource_amount', 
       b'buildings.level': b'buildings.level', 
       b'buildings_count': b'buildings_count', 
       b'clan_id': b'clan_id', 
       b'level': b'level', 
       b'clan_name': b'clan_name', 
       b'clan_tag': b'clan_tag', 
       b'directions': b'directions', 
       b'directions_count': b'directions_count', 
       b'off_day': b'off_day', 
       b'periphery_id': b'periphery_id', 
       b'vacation_finish': b'vacation_finish', 
       b'vacation_start': b'vacation_start', 
       b'sortie_wins_period': b'sortie_wins_period', 
       b'sortie_battles_wins_percentage_period': b'sortie_battles_wins_percentage_period', 
       b'sortie_battles_count_period': b'sortie_battles_count_period', 
       b'defence_battles_count_period': b'defence_battles_count_period'})
    def get_strongholds_statistics(self, callback, clan_id, fields=None):
        get_params = urlencode({b'performer_id': (self._account)})
        try:
            clan_id = int(clan_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = b'/api/strongholds/statistics/%s/' % clan_id
        if self._account:
            url = (b'?').join([url, get_params])

        @preprocess_callback(callback, b'strongholds')
        def inner_callback(data):
            return data[0]

        return self._request_data(inner_callback, b'strongholds', url)

    def get_wgsh_unit_info(self, callback, periphery_id, unit_server_id, rev, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/?rev={rev}').format(periphery_id=periphery_id, unit_server_id=unit_server_id, rev=rev)

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url)

    def get_wgsh_common_unit_info(self, callback, periphery_id, unit_server_id, rev, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        get_params = {b'periphery_id': periphery_id, 
           b'unit_server_id': unit_server_id, 
           b'rev': rev}
        url = (b'/unit_api/periphery/units/info/?{get_params}').format(get_params=urlencode(get_params))

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url)

    def get_wgsh_account_unit_info(self, callback, periphery_id, unit_server_id, rev, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        get_params = {b'periphery_id': periphery_id, 
           b'unit_server_id': unit_server_id, 
           b'rev': rev}
        url = (b'/unit_api/periphery/units/account_info/?{get_params}').format(get_params=urlencode(get_params))

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url)

    def set_vehicle(self, callback, periphery_id, unit_server_id, vehicle_cd, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/vehicles').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        patch_data = {b'vehicle_cd': vehicle_cd}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'PATCH', postData=patch_data)

    def set_readiness(self, callback, periphery_id, unit_server_id, is_ready, reset_vehicle, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/readiness').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        patch_data = {b'is_ready': is_ready, 
           b'reset_vehicle': reset_vehicle}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'PATCH', postData=patch_data)

    def invite_players(self, callback, periphery_id, unit_server_id, accounts_to_invite, comment, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/participants/{account_id}/invite').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'accounts_to_invite': accounts_to_invite, 
           b'comment': comment}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST', postData=post_data)

    def assign_player(self, callback, periphery_id, unit_server_id, account_to_assign, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/participants/{account_id}/assign').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'account_to_assign': account_to_assign}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST', postData=post_data)

    def unassign_player(self, callback, periphery_id, unit_server_id, account_to_unassign, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/participants/{account_id}/unassign').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'account_to_unassign': account_to_unassign}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST', postData=post_data)

    def give_leadership(self, callback, periphery_id, unit_server_id, target_account_id, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/give_leadership').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'target_account_id': target_account_id}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'PATCH', postData=post_data)

    def set_equipment_commander(self, callback, periphery_id, unit_server_id, target_account_id, role, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/equipment_commander').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'equipment_commander_id': target_account_id, 
           b'role': role}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'PATCH', postData=post_data)

    def leave_room(self, callback, periphery_id, unit_server_id, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/participants/{account_id}/leave').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST')

    def take_away_leadership(self, callback, periphery_id, unit_server_id, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery}/units/{unit}/participants/{account}/take_away_leadership').format(periphery=periphery_id, unit=unit_server_id, account=self._account)

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'PATCH')

    def kick_player(self, callback, periphery_id, unit_server_id, account_to_kick, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/kick').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'account_to_kick': account_to_kick}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST', postData=post_data)

    def set_open(self, callback, periphery_id, unit_server_id, is_open, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/participants/{account_id}/set_open').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'is_open': is_open}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'PATCH', postData=post_data)

    def lock_reserve(self, callback, periphery_id, unit_server_id, reserve_id, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/lock_reserve').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'reserve_id': reserve_id}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST', postData=post_data)

    def unlock_reserve(self, callback, periphery_id, unit_server_id, reserve_id, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/unlock_reserve').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)
        post_data = {b'reserve_id': reserve_id}

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST', postData=post_data)

    def clan_statistics(self, callback, clan_id, fields=None):
        try:
            clan_id = int(clan_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/external_api/v1/clan_card/{clan_id}').format(clan_id=clan_id)

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'GET')

    def wgsh_event_settings(self, callback, fields=None):
        url = b'/settings'

        @preprocess_callback(callback, b'wgshevents')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgshevents', url, method=b'GET')

    def wgsh_event_clan_info(self, callback, fields=None):

        @preprocess_callback(callback, b'wgshevents')
        def inner_callback(data):
            return data or {}

        url = b'/clan/info?%s' % urlencode({b'spa_id': (self._account)})
        return self._request_data(inner_callback, b'wgshevents', url, method=b'GET')

    def wgsh_event_get_frozen_vehicles(self, callback, fields=None):

        @preprocess_callback(callback, b'wgshevents')
        def inner_callback(data):
            return data or {}

        url = b'/frozen_vehicle?%s' % urlencode({b'spa_id': (self._account)})
        return self._request_data(inner_callback, b'wgshevents', url, method=b'GET')

    def account_statistics(self, callback, account_id, fields=None):
        try:
            account_id = int(account_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/external_api/accounts/{account_id}').format(account_id=account_id)

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'GET')

    def join_room(self, callback, periphery_id, unit_server_id, fields=None):
        try:
            periphery_id = int(periphery_id)
            unit_server_id = int(unit_server_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        url = (b'/unit_api/periphery/{periphery_id}/units/{unit_server_id}/members/{account_id}/join').format(periphery_id=periphery_id, unit_server_id=unit_server_id, account_id=self._account)

        @preprocess_callback(callback, b'wgsh')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'wgsh', url, method=b'POST')

    def user_ranked_position(self, callback, fields=None):
        url = (b'/user-position/{account_id}/').format(account_id=self._account)

        @preprocess_callback(callback, b'rblb')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'rblb', url, method=b'GET')

    def user_ranked_year_position(self, callback):
        url = (b'/user-yearly-position/{account_id}/').format(account_id=self._account)

        @preprocess_callback(callback, b'rblb')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'rblb', url, method=b'GET')

    @convert_data({b'defence_hour': (lambda x: dt_time(x, 0) if x >= 0 else None)})
    @mapped_fields({b'clan_id': b'clan_id', b'defence_hour': b'defence_hour'})
    def get_strongholds_state(self, callback, clan_id, fields=None):
        get_params = {b'clan_id': clan_id}
        try:
            clan_id = int(clan_id)
        except (TypeError, ValueError):
            error = exceptions.BadRequest()
            return callback({b'description': (error.description)}, error.status_code, error.response_code)

        if self._account:
            get_params[b'performer_id'] = self._account
        url = b'/api/strongholds/state/?%s' % urlencode(get_params)

        @preprocess_callback(callback, b'strongholds')
        def inner_callback(data):
            return data and data[0] or {}

        return self._request_data(inner_callback, b'strongholds', url)

    def get_teaser(self, callback, fields=None):
        url = b'/teaser/?%s' % urlencode(self._pack_promo_params(fields))

        @preprocess_callback(callback, b'promo')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'promo', url, method=b'GET')

    def send_teaser(self, callback, promo_id, fields=None):

        @preprocess_callback(callback, b'promo')
        def inner_callback(data):
            return data or {}

        params = {b'promoscreen_id': promo_id}
        if fields:
            params.update(fields)
        url = b'/teaser/view/'
        return self._request_data(inner_callback, b'promo', url, method=b'POST', postData=self._pack_promo_params(params))

    def get_unread_count(self, callback, fields=None):
        url = b'/unread/?%s' % urlencode(self._pack_promo_params(fields))

        @preprocess_callback(callback, b'promo')
        def inner_callback(data):
            return data or {}

        return self._request_data(inner_callback, b'promo', url, method=b'GET')

    def client_promo_log(self, callback, data, fields=None):

        @preprocess_callback(callback, b'promo')
        def inner_callback(data):
            return data or {}

        url = b'/client_promo_log/?%s' % urlencode(self._pack_promo_params(data))
        return self._request_data(inner_callback, b'promo', url, method=b'GET')

    def _pack_promo_params(self, params=None):
        if params is None:
            params = {}
        default_params = {b'spa_id': (self._account)}
        default_params.update(params)
        return default_params
