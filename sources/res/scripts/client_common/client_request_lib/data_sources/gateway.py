from __future__ import absolute_import
import zlib, json
from datetime import datetime, timedelta, time as dt_time
from future.moves.urllib import parse
from future.utils import viewitems
from client_request_lib import exceptions
from client_request_lib.data_sources import base
from debug_utils import LOG_ERROR
from py2to3.compat import base64compat
EXAMPLES = {}
DEFAULT_SINCE_DELAY = timedelta(days=1)
SUCCESS_STATUSES = [
 200, 201, 304]
ERROR_MAP = {e.response_code: e for e in exceptions.BaseRequestError.__subclasses__()}

def get_error_from_response(response_code):
    return ERROR_MAP.get(response_code, exceptions.WgcgError)


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


class GatewayDataAccessor(base.BaseDataAccessor):

    def __init__(self, url_fetcher, gateway_host, client_lang=None, user_agent=None):
        super(GatewayDataAccessor, self).__init__()
        self.client_lang = client_lang
        self._session_id = None
        self.url_fetcher = url_fetcher
        self.gateway_host = gateway_host
        self.user_agent = user_agent
        return

    def _apply_converters(self, data, converters):
        if data:
            if not isinstance(data, (tuple, list)):
                data = [
                 data]
            for k, convert in converters.items():
                if b'.' in k:
                    prefix, body = k.split(b'.', 1)
                    for portion in data:
                        if prefix in portion:
                            self._apply_converters(portion[prefix], {body: convert})

                else:
                    for portion in data:
                        if k in portion:
                            portion[k] = convert(portion[k])

        return

    def _preprocess_callback(self, callback, converters=None):

        def wrapper(something):

            def wrapped(response, func=something):
                try:
                    data = response.body
                    headers = response.headers()
                    try:
                        data = zlib.decompress(data, 16 + zlib.MAX_WBITS)
                    except zlib.error:
                        pass

                    data = json.loads(data) if data else {}
                except Exception as error:
                    LOG_ERROR(b'Can not process request response. Exception occured: %s' % type(error).__name__, str(error))
                    data = None
                    headers = None

                if response.responseCode not in SUCCESS_STATUSES:
                    error_data = None
                    if data:
                        error_data = {b'description': (data.get(b'description', b'')), b'title': (data.get(b'title', b'')), 
                           b'notification_type': (data.get(b'notification_type', b'')), 
                           b'extra_data': (data.get(b'extra_data'))}
                    return callback(error_data, response.responseCode, response.responseCode, headers)
                else:
                    response_code = exceptions.ResponseCodes.NO_ERRORS
                    if func:
                        data = func(data)
                    if converters:
                        self._apply_converters(data, converters)
                    return callback(data, response.responseCode, response_code, headers)

            if not callable(something):
                return wrapped(something, func=None)
            else:
                return wrapped

        return wrapper

    def login(self, callback, account_id, spa_token, jwt):
        if jwt:
            auth_type = b'JWT'
            auth_data = spa_token
        else:
            auth_type = b'Basic'
            auth_data = base64compat.b64encode((b':').join([str(account_id), str(spa_token)]))
        extra_headers = {b'AUTHORIZATION': (b'%s %s' % (auth_type, auth_data))}

        def inner_callback(data, status_code, response_code, headers):
            if status_code in SUCCESS_STATUSES:
                self._session_id = data[b'session']
            callback(data, status_code, response_code, headers)
            return

        self._request_data(inner_callback, b'/login/', headers=extra_headers)
        return

    def logout(self, callback):
        self._request_data(callback, b'/logout/')
        self._session_id = None
        return

    def _request_data(self, callback, url, get_data=None, method=b'GET', post_data=None, headers=None, converters=None):
        get_data = get_data or {}
        get_data = {k: v for k, v in viewitems(get_data) if v is not None}
        url = (b'/').join([self.gateway_host.rstrip(b'/'), url.lstrip(b'/')])
        if get_data:
            values = []
            for k, val in viewitems(get_data):
                if not isinstance(val, (list, tuple)):
                    val = [
                     val]
                values.append((k, (b',').join(str(i) for i in val)))

            urlencoded_string = parse.urlencode(values)
            url = (b'{}?{}').format(url, urlencoded_string)
        default_headers = {b'Accept-Encoding': b'compress, gzip'}
        if self.client_lang:
            default_headers[b'Accept-Language'] = self.client_lang
        default_headers.update(headers or {})
        if self._session_id:
            default_headers[b'COOKIE'] = b'session=%s' % self._session_id
        if self.user_agent:
            default_headers[b'User-Agent'] = self.user_agent
        headers = tuple((b'{}: {}').format(k, v) for k, v in viewitems(default_headers) if v)
        args = [headers, 30.0, method]
        if post_data:
            args.append(json.dumps(post_data))
        self.url_fetcher(url, self._preprocess_callback(callback, converters=converters), *args)
        return

    def craftmachine_modules_info(self, callback):
        url = b'/craft/client_settings/'
        return self._request_data(callback, url)

    def get_clans_ratings(self, callback, clan_ids, fields=None):
        get_params = {b'clan_ids': clan_ids, b'fields': fields}
        url = b'/ratings/clans/'
        return self._request_data(callback, url, get_data=get_params)

    def get_clans_info(self, callback, clan_ids, fields=None):
        get_params = {b'clan_ids': clan_ids, b'fields': fields}
        url = b'/clans/info/'
        return self._request_data(callback, url, get_data=get_params, converters={b'created_at': from_iso})

    def get_accounts_names(self, callback, account_ids, fields=None):
        get_params = {b'id': account_ids, b'fields': fields}
        url = b'/accounts/names/'
        return self._request_data(callback, url, get_data=get_params, converters={b'id': int})

    def get_account_attribute_by_prefix(self, callback, attr_prefix, fields=None):
        get_params = {b'attr_prefix': attr_prefix, b'fields': fields}
        url = b'/accounts/attributes/get_by_prefix/'
        return self._request_data(callback, url, get_data=get_params)

    def agate_v4_fetch_product_list_state(self, callback, request_data, fields=None):
        url = b'/agate/api/v4/commerce/fetchProductListState/'
        return self._request_data(callback, url, method=b'POST', post_data=request_data)

    def agate_v6_get_user_subscriptions3(self, callback, request_data, fields=None):
        url = b'/agate/api/v6/commerce/getUserSubscriptions3/'
        return self._request_data(callback, url, method=b'POST', post_data=request_data)

    def get_clan_members(self, callback, clan_id, fields=None):
        get_params = {b'fields': fields}
        url = b'/clans/%s/members/' % clan_id
        return self._request_data(callback, url, get_data=get_params, converters={b'joined_at': from_iso})

    def get_clan_favorite_attributes(self, callback, clan_id, fields=None):
        get_params = {b'clan_id': clan_id}
        url = b'/cwh/gm/clans/favorite_attributes'
        return self._request_data(callback, url, get_data=get_params, converters={b'favorite_primetime': (lambda x: x and datetime.strptime(x, b'%H:%M').time()), 
           b'favorite_arena_6': int, 
           b'favorite_arena_8': int, b'favorite_arena_10': int})

    def get_accounts_clans(self, callback, account_ids, fields=None):
        get_params = {b'fields': fields, 
           b'account_ids': account_ids}
        url = b'/accounts/clans/'
        return self._request_data(callback, url, get_data=get_params, converters={b'in_clan_cooldown_till': from_iso, 
           b'joined_at': from_iso})

    def get_account_applications_count_since(self, callback, account_id, since=None):
        since = since or datetime.utcnow() - DEFAULT_SINCE_DELAY
        get_params = {b'created_after': (since.isoformat())}
        url = b'/accounts/%s/applications/count/' % account_id
        return self._request_data(callback, url, get_data=get_params)

    def get_clan_invites_count_since(self, callback, clan_id, since=None):
        since = since or datetime.utcnow() - DEFAULT_SINCE_DELAY
        get_params = {b'created_after': (since.isoformat())}
        url = b'/clans/%s/invites/count/' % clan_id
        return self._request_data(callback, url, get_data=get_params)

    def get_alive_status(self, callback):
        url = b'/ping/'
        return self._request_data(callback, url)

    def get_account_applications(self, callback, fields=None, statuses=None, get_total_count=False, limit=None, offset=None):
        get_params = {b'fields': fields, 
           b'statuses': statuses}
        if get_total_count:
            get_params[b'get_total_count'] = b'true'
        if limit is not None:
            get_params[b'limit'] = limit
        if offset is not None:
            get_params[b'offset'] = offset
        url = b'/my/applications/'
        return self._request_data(callback, url, get_data=get_params, converters={b'items.created_at': from_iso, 
           b'items.updated_at': from_iso})

    def get_clan_applications(self, callback, clan_id, fields=None, statuses=None, get_total_count=False, limit=None, offset=None):
        get_params = {b'fields': fields, 
           b'statuses': statuses}
        if get_total_count:
            get_params[b'get_total_count'] = b'true'
        if limit is not None:
            get_params[b'limit'] = limit
        if offset is not None:
            get_params[b'offset'] = offset
        url = b'/clans/%s/applications/' % clan_id
        return self._request_data(callback, url, get_data=get_params, converters={b'items.created_at': from_iso, 
           b'items.updated_at': from_iso})

    def create_applications(self, callback, clan_ids, comment, fields=None):
        url = b'/clans/applications/'
        data = {b'clan_ids': clan_ids, 
           b'comment': comment}
        return self._request_data(callback, url, method=b'POST', post_data=data)

    def accept_application(self, callback, application_id, fields=None):
        url = b'/clans/applications/%s/' % application_id
        data = {b'status': b'accepted'}
        return self._request_data(callback, url, method=b'PATCH', post_data=data)

    def decline_application(self, callback, application_id, fields=None):
        url = b'/clans/applications/%s/' % application_id
        data = {b'status': b'declined'}
        return self._request_data(callback, url, method=b'PATCH', post_data=data)

    def create_invites(self, callback, clan_id, account_ids, comment, fields=None):
        url = b'/clans/%s/invites/' % clan_id
        data = {b'account_ids': account_ids, 
           b'comment': comment}
        return self._request_data(callback, url, method=b'POST', post_data=data)

    def accept_invite(self, callback, invite_id, fields=None):
        url = b'/clans/invites/%s/' % invite_id
        data = {b'status': b'accepted'}
        return self._request_data(callback, url, method=b'PATCH', post_data=data)

    def decline_invite(self, callback, invite_id, fields=None):
        url = b'/clans/invites/%s/' % invite_id
        data = {b'status': b'declined'}
        return self._request_data(callback, url, method=b'PATCH', post_data=data)

    def bulk_decline_invites(self, callback, invite_ids, fields=None):
        url = b'/clans/decline_invites/'
        data = {b'invite_ids': invite_ids}
        return self._request_data(callback, url, method=b'PATCH', post_data=data)

    def search_clans(self, callback, search, get_total_count=False, fields=None, offset=None, limit=None):
        get_params = {b'search': (search.encode(b'utf-8')), b'fields': fields}
        if get_total_count:
            get_params[b'get_total_count'] = b'true'
        if limit is not None:
            get_params[b'limit'] = limit
        if offset is not None:
            get_params[b'offset'] = offset
        url = b'/clans/search/'
        return self._request_data(callback, url, get_data=get_params, converters={b'items.created_at': from_iso})

    def get_recommended_clans(self, callback, get_total_count=False, fields=None, offset=None, limit=None):
        get_params = {b'fields': fields}
        if get_total_count:
            get_params[b'get_total_count'] = b'true'
        if limit is not None:
            get_params[b'limit'] = limit
        if offset is not None:
            get_params[b'offset'] = offset
        url = b'/clans/recommended/'
        return self._request_data(callback, url, get_data=get_params, converters={b'items.created_at': from_iso})

    def get_clan_invites(self, callback, clan_id, fields=None, statuses=None, get_total_count=False, limit=None, offset=None):
        get_params = {b'fields': fields, 
           b'statuses': statuses}
        if get_total_count:
            get_params[b'get_total_count'] = b'true'
        if limit is not None:
            get_params[b'limit'] = limit
        if offset is not None:
            get_params[b'offset'] = offset
        url = b'clans/%s/invites/' % clan_id
        return self._request_data(callback, url, get_data=get_params, converters={b'items.created_at': from_iso, 
           b'items.updated_at': from_iso})

    def get_account_invites(self, callback, fields=None, statuses=None, get_total_count=False, limit=None, offset=None):
        statuses = statuses or [1, 2, 3, 4, 5, 6]
        get_params = {b'fields': fields, 
           b'statuses': statuses}
        if get_total_count:
            get_params[b'get_total_count'] = b'true'
        if limit is not None:
            get_params[b'limit'] = limit
        if offset is not None:
            get_params[b'offset'] = offset
        url = b'/my/invites/'
        return self._request_data(callback, url, get_data=get_params, converters={b'items.created_at': from_iso, 
           b'items.updated_at': from_iso})

    def get_accounts_info(self, callback, account_ids, fields=None):
        get_params = {b'account_ids': account_ids, 
           b'fields': fields}
        url = b'/accounts/info/'
        return self._request_data(callback, url, get_data=get_params, converters={b'account_id': int})

    def get_clan_provinces(self, callback, clan_id, fields=None):
        get_params = {b'clan_id': [
                      clan_id], 
           b'fields': fields}
        url = b'/global_map/wgapi/clan_provinces/'
        return self._request_data(callback, url, get_data=get_params, converters={b'prime_time': (lambda x: x and datetime.strptime(x, b'%H:%M').time()), 
           b'pillage_end_datetime': from_iso, 
           b'clan_id': int})

    def get_clan_globalmap_stats(self, callback, clan_id, fields=None):
        url = b'/global_map/wgapi/clan_stats/'
        get_params = {b'clan_id': clan_id}
        if fields:
            get_params[b'fields'] = fields
        return self._request_data(callback, url, get_data=get_params, converters={b'clan_id': int})

    def get_fronts_info(self, callback, front_names=None, fields=None):
        url = b'/global_map/wgapi/new_fronts/'
        get_params = {b'fields': fields, 
           b'front_names': front_names}
        return self._request_data(callback, url, get_data=get_params)

    def get_stronghold_info(self, callback, clan_id=None, fields=None):
        url = b'/strongholds/info/'
        get_params = {b'clan_id': clan_id}
        if fields:
            get_params[b'fields'] = fields
        return self._request_data(callback, url, get_data=get_params, converters={b'clan_id': int, 
           b'defence_hour': (lambda x: dt_time(x, 0) if x >= 0 else None)})

    def get_strongholds_statistics(self, callback, clan_id, fields=None):
        url = b'/strongholds/statistics/'
        get_params = {b'clan_id': clan_id}
        if fields:
            get_params[b'fields'] = fields
        return self._request_data(callback, url, get_data=get_params, converters={b'vacation_start': timestamp_to_datetime, 
           b'vacation_finish': timestamp_to_datetime})

    def get_strongholds_state(self, callback, clan_id, fields=None):
        url = b'/strongholds/state/'
        get_params = {b'clan_id': clan_id}
        return self._request_data(callback, url, get_data=get_params, converters={b'clan_id': int, 
           b'defence_hour': (lambda x: dt_time(x, 0) if x >= 0 else None)})

    def get_wgsh_unit_info(self, callback, periphery_id, unit_server_id, rev, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={b'rev': rev}, converters={b'periphery_id': int, 
           b'unit_server_id': int})

    def get_wgsh_common_unit_info(self, callback, periphery_id, unit_server_id, rev, fields=None):
        url = b'/wgsh/v2/periphery/units/info/'
        get_data = {b'rev': rev, 
           b'periphery_id': periphery_id, 
           b'unit_server_id': unit_server_id}
        return self._request_data(callback, url, get_data=get_data, converters={b'periphery_id': int, 
           b'unit_server_id': int})

    def get_wgsh_account_unit_info(self, callback, periphery_id, unit_server_id, rev, fields=None):
        url = b'/wgsh/v2/periphery/units/account_info/'
        get_data = {b'rev': rev, 
           b'periphery_id': periphery_id, 
           b'unit_server_id': unit_server_id}
        return self._request_data(callback, url, get_data=get_data, converters={b'periphery_id': int, 
           b'unit_server_id': int})

    def set_vehicle(self, callback, periphery_id, unit_server_id, vehicle_cd, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/vehicles/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'vehicle_cd': vehicle_cd}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'PATCH', post_data=post_data)

    def set_slot_vehicle_type_filter(self, callback, periphery_id, unit_server_id, slot_idx, vehicle_types, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/set_slot_vehicle_filters/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        _data = {b'slot_id': slot_idx, 
           b'vehicle_types': vehicle_types}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=_data)

    def set_slot_vehicles_filter(self, callback, periphery_id, unit_server_id, slot_idx, vehicles, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/set_slot_vehicle_filters/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        _data = {b'slot_id': slot_idx, 
           b'vehicle_cds': vehicles}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=_data)

    def get_slot_vehicle_filters(self, callback, periphery_id, unit_server_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/get_slot_vehicle_filters/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'GET')

    def stop_players_matching(self, callback, periphery_id, unit_server_id):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/stop_players_matching/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'DELETE')

    def set_readiness(self, callback, periphery_id, unit_server_id, is_ready, reset_vehicle, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/readiness/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        patch_data = {b'is_ready': is_ready, 
           b'reset_vehicle': reset_vehicle}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'PATCH', post_data=patch_data)

    def invite_players(self, callback, periphery_id, unit_server_id, accounts_to_invite, comment, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/invite/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'accounts_to_invite': accounts_to_invite, 
           b'comment': comment}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def assign_player(self, callback, periphery_id, unit_server_id, account_to_assign, slot_id_to_assign, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/assign/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'account_to_assign': account_to_assign, 
           b'slot_id_to_assign': slot_id_to_assign}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def unassign_player(self, callback, periphery_id, unit_server_id, account_to_unassign, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/unassign/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'account_to_unassign': account_to_unassign}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def give_leadership(self, callback, periphery_id, unit_server_id, target_account_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/give_leadership/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'target_account_id': target_account_id}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'PATCH', post_data=post_data)

    def set_equipment_commander(self, callback, periphery_id, unit_server_id, target_account_id, role, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/equipment_commander/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'equipment_commander_id': target_account_id, 
           b'role': role}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def leave_room(self, callback, periphery_id, unit_server_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/leave/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST')

    def leave_mode(self, callback, fields=None):
        url = b'/wgsh/leave_mode/'
        return self._request_data(callback, url, get_data={}, converters={}, method=b'DELETE')

    def take_away_leadership(self, callback, periphery_id, unit_server_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/take_away_leadership/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'PATCH')

    def kick_player(self, callback, periphery_id, unit_server_id, account_to_kick, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/kick/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'account_to_kick': account_to_kick}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def set_open(self, callback, periphery_id, unit_server_id, is_open, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/set_open/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'is_open': is_open}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'PATCH', post_data=post_data)

    def lock_reserve(self, callback, periphery_id, unit_server_id, reserve_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/lock_reserve/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'reserve_id': reserve_id}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def unlock_reserve(self, callback, periphery_id, unit_server_id, reserve_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/unlock_reserve/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        post_data = {b'reserve_id': reserve_id}
        return self._request_data(callback, url, get_data={}, converters={b'periphery_id': int, 
           b'unit_server_id': int}, method=b'POST', post_data=post_data)

    def wgsh_event_settings(self, callback, fields=None):
        url = b'/wgshevents/settings'
        return self._request_data(callback, url, get_data={}, method=b'GET')

    def wgsh_event_clan_info(self, callback, fields=None):
        url = b'/wgshevents/clan/info'
        return self._request_data(callback, url, method=b'GET')

    def wgsh_event_get_frozen_vehicles(self, callback):
        url = b'/wgshevents/frozen_vehicle'
        return self._request_data(callback, url, method=b'GET')

    def wgsh_event_unfreeze_vehicle(self, callback, playerSpaID, vehicleCD, price):
        url = b'/wgshevents/frozen_vehicle'
        return self._request_data(callback, url, method=b'PATCH', post_data={b'vehicle_cd': vehicleCD, 
           b'repair_price': price, 
           b'spa_id': playerSpaID})

    def clan_statistics(self, callback, clan_id, fields=None):
        url = (b'/wgsh/clans/{clan_id}/').format(clan_id=clan_id)
        return self._request_data(callback, url, get_data={}, converters={}, method=b'GET')

    def join_room(self, callback, periphery_id, unit_server_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/join/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={}, method=b'POST')

    def matchmaking_info(self, callback, periphery_id, unit_server_id, fields=None):
        url = (b'/wgsh/periphery/{periphery_id}/units/{unit_server_id}/matchmaking_info/').format(periphery_id=periphery_id, unit_server_id=unit_server_id)
        return self._request_data(callback, url, get_data={}, method=b'GET')

    def user_ranked_position(self, callback, fields=None):
        url = b'/ranked/user_position/'
        return self._request_data(callback, url, get_data={}, method=b'GET')

    def user_ranked_year_position(self, callback):
        url = b'/ranked/user_yearly_position/'
        return self._request_data(callback, url, get_data={}, method=b'GET')

    def account_statistics(self, callback, account_id, fields=None):
        url = (b'/wgsh/accounts/{account_id}/').format(account_id=account_id)
        return self._request_data(callback, url, get_data={}, converters={}, method=b'GET')

    def join_event(self, callback, event_id, fields=None):
        url = b'/wgelen/wot/v1/join_event'
        post_data = {b'event_id': event_id}
        return self._request_data(callback, url, method=b'POST', post_data=post_data)

    def leave_event(self, callback, event_id, fields=None):
        url = b'/wgelen/wot/v1/leave_event'
        post_data = {b'event_id': event_id}
        return self._request_data(callback, url, method=b'POST', post_data=post_data)

    def get_events_data(self, callback, fields=None):
        url = b'/wgelen/wot/v1/get_events_data'
        return self._request_data(callback, url, method=b'GET')

    def get_hangar_flag(self, callback, fields=None):
        url = b'/wgelen/wot/v1/get_hangar_flag'
        return self._request_data(callback, url, method=b'GET')

    def get_leaderboard(self, callback, event_id, page_number, leaderboard_id, fields=None):
        url = b'/wgelen/wot/v1/get_leaderboard'
        get_data = {b'event_id': event_id, 
           b'page_number': page_number, 
           b'leaderboard_id': leaderboard_id}
        return self._request_data(callback, url, get_data, b'GET')

    def get_my_event_top(self, callback, event_id, fields=None):
        url = b'/wgelen/wot/v1/get_my_event_top'
        get_data = {b'event_id': event_id}
        return self._request_data(callback, url, get_data, b'GET')

    def get_my_leaderboard_position(self, callback, event_id, leaderboard_id, fields=None):
        url = b'/wgelen/wot/v1/get_my_leaderboard_position'
        get_data = {b'event_id': event_id, 
           b'leaderboard_id': leaderboard_id}
        return self._request_data(callback, url, get_data, b'GET')

    def get_player_data(self, callback, fields=None):
        url = b'/wgelen/wot/v1/get_player_data'
        return self._request_data(callback, url, method=b'GET')

    def get_player_progression(self, callback, event_id, leaderboard_id, fields=None):
        url = b'/wgelen/wot/v1/get_player_progression'
        get_data = {b'event_id': event_id, 
           b'leaderboard_id': leaderboard_id}
        return self._request_data(callback, url, get_data, method=b'GET')

    def hof_user_info(self, callback):
        url = b'/hof/user/info/'
        return self._request_data(callback, url, method=b'GET')

    def hof_user_exclude(self, callback):
        url = b'/hof/user/exclude/'
        return self._request_data(callback, url, method=b'POST')

    def hof_user_restore(self, callback):
        url = b'/hof/user/restore/'
        return self._request_data(callback, url, method=b'POST')

    def get_teaser(self, callback, additionalData=None):
        url = b'/promobe/teaser/'
        get_params = {b'language': (self._get_formatted_language_code())}
        if additionalData:
            get_params.update(additionalData)
        return self._request_data(callback, url, get_data=get_params, method=b'GET')

    def send_teaser(self, callback, promo_id, additionalData=None):
        url = b'/promobe/teaser/view/'
        params = {b'promoscreen_id': promo_id, 
           b'language': (self._get_formatted_language_code())}
        if additionalData:
            params.update(additionalData)
        return self._request_data(callback, url, params, method=b'POST')

    def get_unread_count(self, callback, additionalData=None):
        url = b'/promobe/unread/'
        get_params = {b'language': (self._get_formatted_language_code())}
        if additionalData:
            get_params.update(additionalData)
        return self._request_data(callback, url, get_data=get_params, method=b'GET')

    def client_promo_log(self, callback, data):
        url = b'/client_promo_log/'
        return self._request_data(callback, url, data, method=b'GET')

    def get_mapbox_progression(self, callback):
        url = b'/mapbox/progress'
        return self._request_data(callback, url, method=b'GET')

    def select_mapbox_crewbook(self, callback, itemID):
        url = b'/mapbox'
        return self._request_data(callback, url, method=b'POST', post_data={b'itemID': itemID})

    def complete_survey(self, callback, surveyData):
        url = b'/mapbox/surveys/complete'
        return self._request_data(callback, url, method=b'POST', post_data=surveyData)

    def request_authorized_survey_url(self, callback, mapURL):
        return self._request_data(callback, mapURL, method=b'GET')

    def get_gift_system_state(self, callback, req_event_ids):
        url = b'/giftsystem/event/state'
        get_params = {b'event_id': req_event_ids}
        return self._request_data(callback, url, get_data=get_params, method=b'GET')

    def post_gift_system_gift(self, callback, entitlement_code, receiver_id, meta_info):
        url = b'/giftsystem/gift'
        post_data = {b'entitlement_code': entitlement_code, b'receiver_id': receiver_id}
        post_data.update(meta_info)
        return self._request_data(callback, url, method=b'POST', post_data=post_data)

    def get_friend_balance(self, callback, spa_id):
        url = b'/friend_service/api/v1/friend_balance/'
        params = {b'friend_spa_id': (int(spa_id))}
        return self._request_data(callback, url, params, method=b'GET')

    def get_friend_list(self, callback):
        url = b'/friend_service/api/v1/friends/list/'
        return self._request_data(callback, url, method=b'GET')

    def put_best_friend(self, callback, spa_id):
        url = b'/friend_service/api/v1/best_friends/set/'
        data = {b'friend_spa_id': (int(spa_id))}
        return self._request_data(callback, url, post_data=data, method=b'PUT')

    def delete_best_friend(self, callback, spa_id):
        url = b'/friend_service/api/v1/best_friends/delete/'
        data = {b'friend_spa_id': (int(spa_id))}
        return self._request_data(callback, url, post_data=data, method=b'DELETE')

    def post_gather_friend_ny_resources(self, callback, spa_id):
        url = b'/friend_service/api/v1/best_friends/gather/'
        data = {b'friend_spa_id': (int(spa_id))}
        return self._request_data(callback, url, post_data=data, method=b'POST')

    def get_uilogging_session(self, callback):
        return self._request_data(callback, b'/uilogging/session', method=b'GET')

    def get_inventory_entitlements(self, callback, entitlement_codes):
        url = b'/shop/inventory_entitlements/'
        if entitlement_codes:
            urlencoded_string = parse.urlencode([(b'entitlement_codes', code) for code in entitlement_codes])
            url = (b'{}?{}').format(url, urlencoded_string)
        return self._request_data(callback, url, method=b'GET')

    def get_inventory_entitlements_v5(self, callback, entitlementsFilter):
        url = b'/agate/api/v5/inventory/getInventoryEntitlements/'
        return self._request_data(callback, url, method=b'POST', post_data=entitlementsFilter)

    def get_storefront_products(self, callback, ctx):
        url = (b'/shop/api/external/v2/{storefront}/products_with_categories/').format(storefront=ctx.getStorefront())
        return self._request_data(callback, url, method=b'GET')

    def buy_storefront_product(self, callback, ctx):
        url = (b'/shop/api/external/v2/{storefront}/products/{product_code}/buy/').format(storefront=ctx.getStorefront(), product_code=ctx.getProductCode())
        price = ctx.getExpectedPrice()
        postData = {b'amount': 1, 
           b'prices': [
                     {b'amount': (price.value), 
                        b'code': (price.currency), 
                        b'item_type': b'currency'}]}
        return self._request_data(callback, url, method=b'POST', post_data=postData)

    def get_clan_supply_quests(self, callback):
        url = b'/clansupply/client/clansupply/quests'
        return self._request_data(callback, url, method=b'GET')

    def post_clan_supply_quests(self, callback):
        url = b'/clansupply/client/clansupply/quests'
        return self._request_data(callback, url, method=b'POST')

    def claim_quest_rewards(self, callback):
        url = b'/clansupply/client/clansupply/claim_rewards'
        return self._request_data(callback, url, method=b'POST')

    def get_progression_settings(self, callback):
        url = b'/clansupply/client/campaign_map/settings'
        return self._request_data(callback, url, method=b'GET')

    def get_progression_progress(self, callback):
        url = b'/clansupply/client/campaign_map/progress'
        return self._request_data(callback, url, method=b'GET')

    def purchase_progression_stage(self, callback, region_number, expected_price):
        url = b'/clansupply/client/campaign_map/purchase'
        return self._request_data(callback, url, method=b'POST', post_data={b'region_number': region_number, 
           b'expected_price': expected_price})

    def __prepare_jwt_header(self, jwt_token):
        if jwt_token:
            return {b'Authorization': ((b'Bearer {}').format(jwt_token))}
        else:
            return

    def get_best_replays(self, callback, jwt_token, **kwargs):
        url = b'/api/v1/replays'
        get_data = {b'limit': 50}
        get_data.update(kwargs)
        return self._request_data(callback, url, method=b'GET', get_data=get_data, headers=self.__prepare_jwt_header(jwt_token))

    def get_top_replays(self, callback, jwt_token):
        url = b'/api/v1/replays/best'
        return self._request_data(callback, url, method=b'GET', headers=self.__prepare_jwt_header(jwt_token))

    def get_replay_link(self, callback, jwt_token, replay_id):
        url = (b'/api/v1/replays/{}/link').format(replay_id)
        return self._request_data(callback, url, method=b'GET', headers=self.__prepare_jwt_header(jwt_token))

    def post_find_replay(self, callback, jwt_token, replay_name):
        url = b'/api/v1/replays/signed_link'
        return self._request_data(callback, url, get_data={b'replay_name': replay_name}, method=b'GET', headers=self.__prepare_jwt_header(jwt_token))

    def get_loadouts(self, callback, client_cache_updated_at, loadout_types):
        url = b'wotlda/api/get_loadouts'
        get_params = {b'client_cache_updated_at': client_cache_updated_at, b'loadout_types': loadout_types}
        return self._request_data(callback, url, get_data=get_params, method=b'GET')

    def get_ingame_tournaments(self, callback):
        url = b'tmsis-wot/api/v2/tournaments/ingame_tournament/'
        return self._request_data(callback, url, method=b'GET')

    def get_w2gt_tips(self, callback, headers, params):
        url = b'/w2gt/wgcg/battle_tips'
        return self._request_data(callback, url, method=b'GET', headers=headers, get_data=params)

    def _get_formatted_language_code(self):
        return self.client_lang.replace(b'_', b'-')
