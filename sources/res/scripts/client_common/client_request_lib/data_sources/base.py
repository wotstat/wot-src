from __future__ import absolute_import
from abc import ABCMeta, abstractmethod
from py2to3.patched_future import with_metaclass
__all__ = (b'BaseDataAccessor',)

class BaseDataAccessor(with_metaclass(ABCMeta, object)):

    def __init__(self):
        return

    @abstractmethod
    def login(self, callback, account_id, spa_token, jwt):
        return

    @abstractmethod
    def logout(self, callback):
        return

    @abstractmethod
    def get_clans_ratings(self, callback, clan_ids, fields=None):
        return

    @abstractmethod
    def get_accounts_names(self, callback, account_ids):
        return

    @abstractmethod
    def get_clan_invites(self, callback, clan_id, fields=None, statuses=None, offset=0, limit=18):
        return

    @abstractmethod
    def get_account_invites(self, callback, fields=None, statuses=None, offset=0, limit=18):
        return

    @abstractmethod
    def get_account_applications_count_since(self, callback, account_id, since=None):
        return

    @abstractmethod
    def get_clan_invites_count_since(self, callback, clan_id, since=None):
        return

    @abstractmethod
    def get_clan_applications(self, callback, clan_id, fields=None, statuses=None, offset=0, limit=18):
        return

    @abstractmethod
    def search_clans(self, callback, search, get_total_count=False, fields=None, offset=0, limit=18):
        return

    @abstractmethod
    def get_clans_info(self, callback, clan_ids, fields=None):
        return

    @abstractmethod
    def get_clan_members(self, callback, clan_id, fields=None):
        return

    @abstractmethod
    def get_clan_favorite_attributes(self, callback, clan_id, fields=None):
        return

    @abstractmethod
    def get_accounts_clans(self, callback, account_ids, fields=None):
        return

    @abstractmethod
    def get_accounts_info(self, callback, account_ids, fields=None):
        return

    @abstractmethod
    def get_clan_provinces(self, callback, clan_id, fields=None):
        return

    @abstractmethod
    def get_clan_globalmap_stats(self, callback, clan_id, fields=None):
        return

    @abstractmethod
    def get_fronts_info(self, callback, front_names=None, fields=None):
        return

    @abstractmethod
    def get_stronghold_info(self, callback, clan_id=None, fields=None):
        return

    @abstractmethod
    def get_strongholds_statistics(self, callback, clan_id, fields=None):
        return

    @abstractmethod
    def get_strongholds_state(self, callback, clan_id, fields=None):
        return
