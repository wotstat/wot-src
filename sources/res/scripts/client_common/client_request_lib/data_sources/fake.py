import random, string, time
from functools import wraps, partial
from datetime import datetime, timedelta, time as dt_time
from client_request_lib import exceptions
from client_request_lib.data_sources import base
from helpers import time_utils
EXAMPLES = {}

def _doResponse(callback, result, status_code, response_code):
    callback(result, status_code, response_code, None)
    return


def fake_method(example):

    def wrapper(func):

        @wraps(func)
        def wrapped(self, callback, *args, **kwargs):
            try:
                result = func(self, *args, **kwargs)
                response_code = exceptions.ResponseCodes.NO_ERRORS
                status_code = 200
            except exceptions.BaseRequestError as e:
                result = {b'description': (e.description)}
                status_code = e.status_code
                response_code = e.response_code
            except:
                raise

            _doResponse(callback, result, status_code, response_code)
            return

        name = func.__name__
        if b'get_' in name:
            name = name.split(b'get_', 1)[-1]
        EXAMPLES[name] = example
        return wrapped

    return wrapper


def paginated_method(func):

    @wraps(func)
    def wrapped(*args, **kwargs):
        offset = kwargs.pop(b'offset') or 0
        limit = kwargs.pop(b'limit') or 18
        diapasone = slice(offset, offset + limit)
        get_total_count = kwargs.pop(b'get_total_count', False)
        result = func(*args, **kwargs)
        total = len(result)
        result = {b'items': (result[diapasone])}
        if get_total_count:
            result[b'total'] = total
        return result

    return wrapped


def get_gift_system_state(req_event_ids):
    current_time = int(time.time())
    event_stub = {b'send_limit': 1, 
       b'execution_time': (current_time - time_utils.ONE_SECOND), 
       b'expiration_time': (current_time + time_utils.ONE_MINUTE), 
       b'expiration_delta': (5 * time_utils.ONE_MINUTE), 
       b'state': []}
    return {event_id: event_stub for event_id in req_event_ids}


def get_gift_system_wait_response(*_):
    wait_response = {b'players': [], b'last_player_updated_at': None, 
       b'first_player_updated_at': None}
    return wait_response


def post_gift_system_gift(*_):
    current_time = int(time.time())
    response_stub = {b'execution_time': (current_time - time_utils.ONE_SECOND)}
    return response_stub


def post_gift_system_gift_multiple(*_):
    current_time = int(time.time())
    response_stub = {b'execution_time': (current_time - time_utils.ONE_SECOND)}
    return response_stub


def get_uilogging_session(*_, **__):
    return {b'auth': {b'token': b'uilogging_token_stub', b'expiration': (time.time() + 86400)}, b'logging': {b'max_logs_count': 50, 
                    b'max_log_properties_count': 250, 
                    b'url': b'https://localhost:81/logging'}}


def get_statistic_lootbox(*_, **__):
    return {123: [
           1766220793, 12, {}]}


class FakeDataAccessor(base.BaseDataAccessor):
    requests_before_logout = -1

    def __init__(self, url_fetcher=None, config=None, client_lang=None, user_agent=None):
        super(FakeDataAccessor, self).__init__()
        self.client_lang = client_lang
        self._account = None
        self._storage = {}
        self.account = None
        self.user_agent = user_agent
        return

    def login(self, callback, account_id, spa_token, jwt):
        self.account = account_id
        self._account = self.requests_before_logout
        access_token = (b'').join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        result, status_code = {b'access_token': access_token, b'expires_in': 36000}, 200
        response_code = exceptions.ResponseCodes.NO_ERRORS
        _doResponse(callback, result, status_code, response_code)
        return

    def get_alive_status(self, callback):
        result, status_code = {b'status': b'I am alive!'}, 200
        response_code = exceptions.ResponseCodes.NO_ERRORS
        _doResponse(callback, result, status_code, response_code)
        return

    def logout(self, callback):
        self.account = None
        self._account = None
        result, status_code = (b'ok', 200)
        response_code = exceptions.ResponseCodes.NO_ERRORS
        _doResponse(callback, result, status_code, response_code)
        return

    def _filter_data(self, data, fields):
        if isinstance(data, list):
            return [self._filter_data(i, fields) for i in data]
        return {k: v for k, v in data.iteritems() if k in fields}

    def _request_data(self, section, entity_id, fields=None):
        if not self._account:
            raise exceptions.AuthentificationError()
        self._account -= 1
        try:
            result = self._storage[section][entity_id]
        except KeyError:
            result = EXAMPLES[section]
            if callable(result):
                result = result(entity_id)
                self._storage.setdefault(section, {})[entity_id] = result

        if isinstance(result, exceptions.BaseRequestError):
            raise result
        if fields:
            result = self._filter_data(result, fields)
        return result

    def _compare_keys(self, example, data):
        if isinstance(example, list):
            for i in data:
                self._compare_keys(example[0], i)

        if isinstance(example, dict):
            if set(example) ^ set(data):
                missed = set(example) - set(data)
                extra = set(data) - set(example)
                message = []
                if missed:
                    message.append(b'(%s) keys are missed' % (b', ').join(missed))
                if extra:
                    message.append(b'(%s) keys are not needed' % (b', ').join(extra))
                raise ValueError((b' and ').join(message))
        return

    def set_data(self, section, entity_id, data):
        example = EXAMPLES[section]
        if not isinstance(data, exceptions.BaseRequestError):
            self._compare_keys(example, data)
        self._storage.setdefault(section, {})[entity_id] = data
        return

    @fake_method(example=(lambda clan_id: {b'clan_id': clan_id, 
       b'xp_avg': (random.randrange(1, 1000) / 10.0), 
       b'efficiency': (random.randrange(1, 10000)), 
       b'battles_count_avg': (random.randrange(1, 10000)), 
       b'wins_ratio_avg': (random.randrange(1, 100)), 
       b'gm_elo_rating_6': (random.randrange(1, 1000)), 
       b'gm_elo_rating_8': (random.randrange(1, 1000)), 
       b'gm_elo_rating_10': (random.randrange(1, 1000)), 
       b'gm_elo_rating_6_rank': (random.randrange(1, 1000)), 
       b'gm_elo_rating_8_rank': (random.randrange(1, 1000)), 
       b'gm_elo_rating_10_rank': (random.randrange(1, 1000)), 
       b'fb_elo_rating_8': (random.randrange(1, 1000)), 
       b'fb_elo_rating_10': (random.randrange(1, 1000)), 
       b'fb_battles_count_10_28d': (random.randrange(1, 100)), 
       b'fs_battles_count_10_28d': (random.randrange(1, 100)), 
       b'gm_battles_count_28d': (random.randrange(1, 100)), 
       b'fs_battles_count_28d': (random.randrange(1, 100)), 
       b'fb_battles_count_28d': (random.randrange(1, 100))}))
    def get_clans_ratings(self, clan_ids, fields=None):
        return [self._request_data(b'clans_ratings', i, fields=fields) for i in clan_ids]

    @fake_method(example=(lambda clan_id: {b'name': b'xxx', 
       b'tag': b'ff', b'motto': b'yyyy', b'leader_id': 666, b'members_count': 13, 
       b'clan_id': clan_id, b'created_at': (datetime.now()), 
       b'accepts_join_requests': True, 
       b'treasury': 2423}))
    def get_clans_info(self, clan_ids, fields=None):
        return [self._request_data(b'clans_info', clan_id, fields=fields) for clan_id in clan_ids]

    @fake_method(example=(lambda acc_id: {b'id': acc_id, b'name': b'name'}))
    def get_accounts_names(self, account_ids, fields=None):
        return [self._request_data(b'accounts_names', account_id, fields=fields) for account_id in account_ids]

    @fake_method(example=(lambda attr_prefix: {b'user_stated_country': b'RU'}))
    def get_account_attribute_by_prefix(self, attr_prefix, fields=None):
        return self._request_data(b'account_attributes', attr_prefix, fields=fields)

    @fake_method(example=(lambda clan_id: [{b'account_id': (2324 + i), b'role_name': b'officer', b'role_bw_flag': (1 << i), b'clan_id': clan_id, b'joined_at': (datetime.now())} for i in range(11)]))
    def get_clan_members(self, clan_id, fields=None):
        return self._request_data(b'clan_members', clan_id, fields=fields)

    @fake_method(example={b'clan_id': 2790, 
       b'favorite_arena_6': 1, 
       b'favorite_arena_8': 3, 
       b'favorite_arena_10': 65549, 
       b'favorite_primetime': (dt_time(19, 0))})
    def get_clan_favorite_attributes(self, clan_id, fields=None):
        return self._request_data(b'clan_favorite_attributes', clan_id, fields=fields)

    @fake_method(example={b'total': 17})
    def get_account_applications_count_since(self, account_id, since=None):
        return self._request_data(b'account_applications_count_since', account_id)

    @fake_method(example={b'total': 14})
    def get_clan_invites_count_since(self, clan_id, since=None):
        return self._request_data(b'clan_invites_count_since', clan_id)

    @fake_method(example={b'account_id': 234, 
       b'joined_at': (datetime.now()), b'clan_id': 343, b'role_bw_flag': 13, 
       b'role_name': b'commander', b'in_clan_cooldown_till': (datetime.now()), 
       b'clan_tag': b'fake', 
       b'clan_color': 123})
    def get_accounts_clans(self, account_ids, fields):
        return [self._request_data(b'accounts_clans', i, fields=fields) for i in account_ids]

    @fake_method(example=(lambda (account_id, statuses): [{b'status': (random.choice(statuses or (b'active', b'declined', b'cancelled', b'accepted', b'expired', b'error', b'deleted'))), b'created_at': (datetime.now()), b'updated_at': (datetime.now()), b'sender_id': (random.randrange(1, 10000)), b'id': (random.randrange(1, 1000000)), b'account_id': account_id, b'clan_id': (random.randrange(1, 10000)), b'status_changer_id': (random.randrange(1, 10000)), b'comment': ((b'Welcome {}!').format(random.randrange(1, 10000)) if random.choice((1, 0)) else b'')} for i in range(random.randrange(0, 1000))]))
    @paginated_method
    def get_account_applications(self, fields=None, statuses=None):
        return self._request_data(b'account_applications', (
         self.account, tuple(statuses or [])), fields=fields)

    @fake_method(example=(lambda (clan_id, statuses): [{b'status': (random.choice(statuses or (b'active', b'declined', b'cancelled', b'accepted', b'expired', b'error', b'deleted'))), b'created_at': (datetime.now()), b'updated_at': (datetime.now()), b'sender_id': (random.randrange(1, 10000)), b'id': (random.randrange(1, 1000000)), b'account_id': (random.randrange(1, 10000)), b'clan_id': clan_id, b'status_changer_id': (random.randrange(1, 10000)), b'comment': ((b'Welcome {}!').format(random.randrange(1, 10000)) if random.choice((1, 0)) else b'')} for i in range(random.randrange(0, 1000))]))
    @paginated_method
    def get_clan_applications(self, clan_id, fields=None, statuses=None):
        return self._request_data(b'clan_applications', (
         clan_id, tuple(statuses or [])), fields=fields)

    @fake_method(example=(lambda search: [] if len(search) % 2 else [{b'name': (b'Clan Name %d' % random.randrange(1, 1000)), b'tag': b'TCLAN', b'motto': b'Clan Motto', b'leader_id': (random.randrange(1, 10000)), b'clan_id': (random.randrange(1, 100)), b'members_count': (random.randrange(1, 50)), b'created_at': (datetime.now()), b'accepts_join_requests': (random.choice((True, False)))} for i in range(random.randrange(1, 36))]))
    @paginated_method
    def search_clans(self, search, fields=None):
        return self._request_data(b'search_clans', search)

    @fake_method(example=(lambda account: [{b'name': (b'Clan Name %d' % random.randrange(1, 1000)), b'tag': b'TCLAN', b'motto': b'Clan Motto', b'leader_id': (random.randrange(1, 10000)), b'clan_id': (random.randrange(1, 100)), b'members_count': (random.randrange(1, 50)), b'created_at': (datetime.now()), b'accepts_join_requests': (random.choice((True, False)))} for i in range(random.randrange(1, 36))]))
    @paginated_method
    def get_recommended_clans(self, fields=None):
        return self._request_data(b'recommended_clans', self.account)

    @fake_method(example=(lambda (clan_id, statuses): [{b'status': (random.choice(statuses or (b'active', b'declined', b'cancelled', b'accepted', b'expired', b'error', b'deleted'))), b'created_at': (datetime.now()), b'updated_at': (datetime.now()), b'sender_id': (random.randrange(1, 10000)), b'id': (random.randrange(1, 1000000)), b'account_id': (random.randrange(1, 10000)), b'clan_id': clan_id, b'comment': ((b'Welcome {}!').format(random.randrange(1, 10000)) if random.choice((1, 0)) else b''), b'status_changer_id': 2132} for i in range(random.randrange(0, 1000))]))
    @paginated_method
    def get_clan_invites(self, clan_id, fields=None, statuses=None):
        return self._request_data(b'clan_invites', (
         clan_id, tuple(statuses or [])), fields=fields)

    @fake_method(example=(lambda (account_id, statuses): [{b'status': (random.choice(statuses or (b'active', b'declined', b'cancelled', b'accepted', b'expired', b'error', b'deleted'))), b'created_at': (datetime.now()), b'updated_at': (datetime.now()), b'sender_id': (random.randrange(1, 10000)), b'id': (random.randrange(1, 1000000)), b'account_id': account_id, b'clan_id': (random.randrange(1, 10000)), b'status_changer_id': 2132, b'comment': ((b'Welcome {}!').format(random.randrange(1, 10000)) if random.choice((1, 0)) else b'')} for i in range(random.randrange(0, 1000))]))
    @paginated_method
    def get_account_invites(self, fields=None, statuses=None):
        return self._request_data(b'account_invites', (
         self.account, tuple(statuses or [])), fields=fields)

    @fake_method(example=(lambda account_id: {b'global_rating': (random.randrange(100, 10000)), 
       b'battle_avg_xp': (random.randrange(100, 10000)), 
       b'battles_count': (random.randrange(1, 1000)), 
       b'battle_avg_performance': (random.uniform(0, 1)), 
       b'xp_amount': (random.randrange(100, 1000)), 
       b'account_id': account_id}))
    def get_accounts_info(self, account_ids, fields=None):
        return [self._request_data(b'accounts_info', acc_id, fields=fields) for acc_id in account_ids]

    @fake_method(example=[
     {b'front_name': b'some_front', 
        b'province_id': b'some_province', 
        b'front_name_localized': b'some_front_localized', 
        b'province_id_localized': b'some_province_localized', 
        b'revenue': 324, 
        b'hq_connected': True, 
        b'prime_time': (dt_time(18, 0, 0)), 
        b'periphery': 333, 
        b'game_map': b'some_map', 
        b'pillage_cooldown': 1, 
        b'pillage_end_datetime': (datetime.now() + timedelta(hours=3)), 
        b'turns_owned': 12},
     {b'front_name': b'some_front2', 
        b'province_id': b'some_province2', 
        b'front_name_localized': b'some_front_localized2', 
        b'province_id_localized': b'some_province_localized2', 
        b'revenue': 333, 
        b'hq_connected': True, 
        b'prime_time': (dt_time(19, 0, 0)), 
        b'periphery': 444, 
        b'game_map': b'some_map2', 
        b'pillage_cooldown': None, 
        b'pillage_end_datetime': None, 
        b'turns_owned': 12, 
        b'arena_id': 5}])
    def get_clan_provinces(self, clan_id, fields=None):
        return self._request_data(b'clan_provinces', clan_id, fields=fields)

    @fake_method(example={b'battles_lost': 12, 
       b'influence_points': 121, 
       b'provinces_captured': 23, 
       b'provinces_count': 234, 
       b'battles_played': 332, 
       b'battles_won': 232, 
       b'battles_played_on_6_level': 21, 
       b'battles_won_on_6_level': 12, 
       b'battles_played_on_8_level': 32, 
       b'battles_won_on_8_level': 21, 
       b'battles_played_on_10_level': 43, 
       b'battles_won_on_10_level': 23})
    def get_clan_globalmap_stats(self, clan_id, fields=None):
        return self._request_data(b'clan_globalmap_stats', clan_id, fields=fields)

    @fake_method(example=[
     {b'front_name': b'front_name', 
        b'front_name_localized': b'front_name_localized', 
        b'min_vehicle_level': 2, 
        b'max_vehicle_level': 4}])
    def get_fronts_info(self, front_names=None, fields=None):
        return self._request_data(b'fronts_info', front_names, fields=fields)

    @fake_method(example={b'defence_mode_is_activated': True, 
       b'defence_hour': (dt_time(10, 0)), 
       b'sortie_battles_count': 23, 
       b'sortie_wins': 12, 
       b'sortie_losses': 19, 
       b'sortie_fort_resource_in_absolute': 100, 
       b'sortie_fort_resource_in_champion': 71, 
       b'sortie_fort_resource_in_middle': 60, 
       b'defence_battles_count': 234, 
       b'defence_combat_wins': 21, 
       b'sortie_middle_battles_count': 12, 
       b'sortie_champion_battles_count': 32, 
       b'sortie_absolute_battles_count': 23, 
       b'defence_enemy_base_capture_count': 43, 
       b'defence_capture_enemy_building_total_count': 55, 
       b'defence_loss_own_building_total_count': 65, 
       b'defence_attack_efficiency': 23.2, 
       b'defence_success_attack_count': 122, 
       b'defence_attack_count': 13, 
       b'defence_defence_efficiency': 32.2, 
       b'defence_defence_count': 24, 
       b'defence_success_defence_count': 5, 
       b'total_resource_amount': 321, 
       b'defence_resource_loss_count': 112, 
       b'defence_resource_capture_count': 322, 
       b'fb_battles_count_8': 23, 
       b'fb_battles_count_10': 12, 
       b'level': 2, 
       b'buildings': [
                    {b'type': 1, 
                       b'direction': 0, 
                       b'level': 2, 
                       b'position': 2},
                    {b'type': 2, 
                       b'direction': 1, 
                       b'level': 3, 
                       b'position': 2}]})
    def get_stronghold_info(self, clan_id, fields=None):
        return self._request_data(b'stronghold_info', clan_id, fields=fields)

    @fake_method(example={b'buildings_count': 4, 
       b'directions_count': 3, 
       b'buildings': [
                    {b'type': 1, 
                       b'hp': 32, 
                       b'storage': 123, 
                       b'level': 4, 
                       b'position': 7, 
                       b'direction': 1}], 
       b'directions': [
                     1, 2], 
       b'off_day': 3, 
       b'vacation_start': (datetime.utcnow() + timedelta(days=1)), 
       b'vacation_finish': (datetime.utcnow() + timedelta(days=4)), 
       b'periphery_id': 333, 
       b'clan_tag': b'tag', 
       b'clan_name': b'some_name', 
       b'clan_id': 21, 
       b'level': 2, 
       b'sortie_wins_period': 7, 
       b'sortie_battles_wins_percentage_period': 20.0, 
       b'sortie_battles_count_period': 122, 
       b'defence_battles_count_period': 21})
    def get_strongholds_statistics(self, clan_id, fields=None):
        return self._request_data(b'strongholds_statistics', clan_id, fields=fields)

    @fake_method(example={b'clan_id': 234, b'defence_hour': (dt_time(10, 0))})
    def get_strongholds_state(self, clan_id, fields=None):
        return self._request_data(b'strongholds_state', clan_id, fields=fields)

    @fake_method(example=[{b'clan_id': 234, b'account_id': 3, b'id': 23}])
    def create_invites(self, clan_id, account_ids, comment, fields=None):
        return self._request_data(b'create_invites', (clan_id, account_ids), fields=fields)

    @fake_method(example=[{b'clan_id': 224, b'account_id': 3, b'id': 123}])
    def create_applications(self, clan_ids, comment, fields=None):
        return self._request_data(b'create_applications', clan_ids, fields=fields)

    @fake_method(example=(lambda obj_id: {b'transaction_id': 213, 
       b'id': obj_id, b'account_id': 343, b'clan_id': 17}))
    def accept_application(self, application_id, fields=None):
        return self._request_data(b'accept_application', application_id, fields=fields)

    @fake_method(example=(lambda obj_id: {b'id': obj_id, b'account_id': 343, b'clan_id': 17}))
    def decline_application(self, application_id, fields=None):
        return self._request_data(b'decline_application', application_id, fields=fields)

    @fake_method(example=(lambda obj_id: {b'transaction_id': 213, b'id': obj_id, b'account_id': 343, b'clan_id': 17}))
    def accept_invite(self, invite_id, fields=None):
        return self._request_data(b'accept_invite', invite_id, fields=fields)

    @fake_method(example=(lambda obj_id: {b'id': obj_id, b'account_id': 343, b'clan_id': 17}))
    def decline_invite(self, invite_id, fields=None):
        return self._request_data(b'decline_invite', invite_id, fields=fields)

    @fake_method(example=[{b'id': 991, b'account_id': 1001, b'clan_id': 19}, {b'id': 992, b'account_id': 1001, b'clan_id': 19}, {b'id': 993, b'account_id': 1001, b'clan_id': 19}])
    def bulk_decline_invites(self, invite_ids):
        return self._request_data(b'bulk_decline_invites', invite_ids)

    @fake_method(example={b'permissions': {b'manage_reserves': [
                                           b'commander',
                                           b'combat_officer',
                                           b'executive_officer',
                                           b'personnel_officer']}, 
       b'time_to_ready': 900, 
       b'max_level': 10, 
       b'battle_series_duration': 3600, 
       b'enemy_clan': None, 
       b'industrial_resource_multiplier': 1, 
       b'max_players_count': 15, 
       b'type': b'FORT_BATTLE', 
       b'max_legionaries_count': 0, 
       b'available_reserves': {b'ARTILLERY_STRIKE': [], b'HIGH_CAPACITY_TRANSPORT': [], b'REQUISITION': [], b'AIRSTRIKE': []}, b'direction': b'A', 
       b'min_players_count': 1, 
       b'matchmaker_next_tick': 1475578800, 
       b'battle_series_status': [
                               {b'battle_reward': 0, 
                                  b'gameplay_id': 0, 
                                  b'geometry_id': 6, 
                                  b'first_resp_clan_id': None, 
                                  b'second_resp_clan_id': None, 
                                  b'attacker': None, 
                                  b'clan_owner_id': 14000012972L, 
                                  b'current_battle': False, 
                                  b'map_id': 6},
                               {b'battle_reward': 0, 
                                  b'gameplay_id': 0, 
                                  b'geometry_id': 14, 
                                  b'first_resp_clan_id': None, 
                                  b'second_resp_clan_id': None, 
                                  b'attacker': None, 
                                  b'clan_owner_id': 14000012972L, 
                                  b'current_battle': False, 
                                  b'map_id': 14},
                               {b'battle_reward': 0, 
                                  b'gameplay_id': 0, 
                                  b'geometry_id': 20, 
                                  b'first_resp_clan_id': None, 
                                  b'second_resp_clan_id': None, 
                                  b'attacker': None, 
                                  b'clan_owner_id': 14000012972L, 
                                  b'current_battle': False, 
                                  b'map_id': 20}], 
       b'battle_duration': 600, 
       b'requisition_bonus_percent': None, 
       b'public': False, 
       b'selected_reserves': [
                            None,
                            None,
                            None], 
       b'min_level': 1})
    def get_wgsh_unit_info(self, periphery_id, unit_id, rev, fields=None):
        return self._request_data(b'wgsh_unit_info', unit_id)

    @fake_method(example={})
    def set_vehicle(self, periphery_id, unit_id, vehicle_cd, fields=None):
        return self._request_data(b'set_vehicle', unit_id)

    @fake_method(example={})
    def set_readiness(self, periphery_id, unit_id, is_ready, reset_vehicle, fields=None):
        return self._request_data(b'set_readiness', unit_id)

    @fake_method(example={})
    def invite_players(self, periphery_id, unit_id, accounts_to_invite, comment, fields=None):
        return self._request_data(b'invite_players', unit_id)

    @fake_method(example={})
    def assign_player(self, periphery_id, unit_id, account_to_assign, fields=None):
        return self._request_data(b'assign_player', unit_id)

    @fake_method(example={})
    def unassign_player(self, periphery_id, unit_id, account_to_assign, fields=None):
        return self._request_data(b'unassign_player', unit_id)

    @fake_method(example={})
    def give_leadership(self, periphery_id, unit_id, account_to_assign, fields=None):
        return self._request_data(b'give_leadership', unit_id)

    @fake_method(example={})
    def give_equipment_commander(self, periphery_id, unit_id, target_account_id, fields=None):
        return self._request_data(b'give_equipment_commander', unit_id)

    @fake_method(example={})
    def leave_room(self, periphery_id, unit_id, fields=None):
        return self._request_data(b'leave_room', unit_id)

    @fake_method(example={})
    def take_away_leadership(self, periphery_id, unit_id, fields=None):
        return self._request_data(b'take_away_leadership', unit_id)

    @fake_method(example={})
    def kick_player(self, periphery_id, unit_id, account_to_assign, fields=None):
        return self._request_data(b'kick_player', unit_id)

    @fake_method(example={})
    def set_open(self, periphery_id, unit_id, is_open, fields=None):
        return self._request_data(b'set_open', unit_id)

    @fake_method(example={})
    def lock_reserve(self, periphery_id, unit_id, reserve_id, fields=None):
        return self._request_data(b'lock_reserve', unit_id)

    @fake_method(example={})
    def unlock_reserve(self, periphery_id, unit_id, reserve_id, fields=None):
        return self._request_data(b'unlock_reserve', unit_id)

    @fake_method(example=(lambda clan_id: {b'skirmishes_statistics': {b'last_28_days_battles_count': 1, 
                                  b'last_28_days_wins_count': 1, 
                                  b'wins_count': 1, 
                                  b'loses_count': 1, 
                                  b'draws_count': 1}, 
       b'battles_statistics': {b'last_28_days_battles_count': 1, 
                               b'last_28_days_wins_count': 1, 
                               b'wins_count': 1, 
                               b'loses_count': 1, 
                               b'draws_count': 1}, 
       b'skirmishes_count_last_28_days': 1, 
       b'battles_count_last_28_days': 1, 
       b'clear_wins_count': 1, 
       b'level_6_statistics': {b'wins_count': 1, 
                               b'battles_count': 1}, 
       b'level_8_statistics': {b'wins_count': 1, 
                               b'battles_count': 1}, 
       b'level_10_statistics': {b'wins_count': 1, 
                                b'battles_count': 1}}))
    def clan_statistics(self, clan_id, fields=None):
        return self._request_data(b'clan_statistics', clan_id)

    @fake_method(example=(lambda account_id: {b'skirmishes_statistics': {b'wins_count': 1, 
                                  b'loses_count': 1, 
                                  b'draws_count': 1}, 
       b'battles_statistics': {b'wins_count': 1, 
                               b'loses_count': 1, 
                               b'draws_count': 1}, 
       b'industrial_resource_total': {b'random_battles': 1, 
                                      b'skirmishes': 1, 
                                      b'battles': 1}, 
       b'industrial_resource_last_28_days': {b'random_battles': 1, 
                                             b'skirmishes': 1, 
                                             b'battles': 1}}))
    def account_statistics(self, account_id, fields=None):
        return self._request_data(b'account_statistics', account_id)

    @fake_method(example={})
    def join_room(self, periphery_id, unit_id, fields=None):
        return self._request_data(b'join_room', unit_id)

    @fake_method(example={b'results': {b'season': {b'avg_exp': 6113244, 
                                b'total_battles': 2, 
                                b'battles_with_steps': 1, 
                                b'points': 91, 
                                b'avg_assist_damage': 2, 
                                b'avg_damage': 348}}, 
       b'meta': {b'spa': {b'id': 519}}})
    def user_season_statistics(self, fields=None):
        return self._request_data(b'user_season_statistics', None)

    @fake_method(example={b'data': {b'promo_name': b'Bang bang bang', 
                 b'type': b'news', 
                 b'image': b'//webbrg.tanki.su/dcont/fb/image/9.12.jpg', 
                 b'video': b'https://www.youtube.com/watch?v=_jGPljdFBqA', 
                 b'important': False, 
                 b'promoscreen_url': b'/promoscreens/<slug>/'}, 
       b'unread': 3, 
       b'sent_at': 1423813849})
    def get_teaser(self, fields=None, **kwargs):
        return self._request_data(b'teaser', None)

    @fake_method(example=None)
    def send_teaser(self, promo_id):
        return self._request_data(b'send_teaser', None)

    @fake_method(example={b'unread': 3})
    def get_unread_count(self, fields=None):
        return self._request_data(b'unread', None)

    @fake_method(example=None)
    def get_events_data(self, fields=None):
        return self._request_data(b'events_data', None, fields)

    @fake_method(example=None)
    def get_hangar_flag(self, fields=None):
        return self._request_data(b'hangar_flag', None, fields)

    @fake_method(example=None)
    def get_mapbox_progression(self):
        return self._request_data(b'mapbox_progression', None)

    @fake_method(example=get_gift_system_state)
    def get_gift_system_state(self, req_event_ids):
        self._storage.get(b'gift_system_state', {}).clear()
        return self._request_data(b'gift_system_state', frozenset(req_event_ids))

    @fake_method(example=get_gift_system_wait_response)
    def get_gift_system_wait_response(self, *_):
        self._storage.get(b'get_gift_system_wait_response', {}).clear()
        return self._request_data(b'get_gift_system_wait_response', None)

    @fake_method(example=post_gift_system_gift)
    def post_gift_system_gift(self, *_):
        self._storage.get(b'post_gift_system_gift', {}).clear()
        return self._request_data(b'post_gift_system_gift', None)

    @fake_method(example=post_gift_system_gift_multiple)
    def post_gift_system_gift_multiple(self, *_):
        self._storage.get(b'post_gift_system_gift_multiple', {}).clear()
        return self._request_data(b'post_gift_system_gift_multiple', None)

    @fake_method(example=get_uilogging_session)
    def get_uilogging_session(self):
        self._storage.get(b'uilogging_session', {}).clear()
        return self._request_data(b'uilogging_session', None)

    @fake_method(example={b'data': {b'balance': [
                            {b'code': b'fake_code', 
                               b'amount': 0, 
                               b'expires_at': b'1970-01-01T00:00:00Z'}], 
                 b'balance_version': 0, 
                 b'on_hold': {b'granted': [], b'consumed': []}}})
    def get_inventory_entitlements(self, entitlement_codes):
        return self._request_data(b'inventory_entitlements', None)

    @fake_method(example={b'data': {b'balance': [
                            {b'code': b'fake_code', 
                               b'amount': 0, 
                               b'expires_at': b'1970-01-01T00:00:00Z', 
                               b'tags': []}], 
                 b'balance_version': 0, 
                 b'on_hold': {b'granted': [], b'consumed': []}}})
    def get_inventory_entitlements_v5(self, entitlementsFilter):
        return self._request_data(b'get_inventory_entitlements_v5', None)

    @fake_method(example=get_statistic_lootbox)
    def get_statistic_lootbox(self, *_):
        self._storage.get(b'get_statistic_lootbox', {}).clear()
        return self._request_data(b'get_statistic_lootbox', None)
