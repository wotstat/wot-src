from soft_exception import SoftException

class ResponseCodes(object):
    NO_ERRORS = 0
    UNKNOWN_ERROR = 1
    AUTHENTIFICATION_ERROR = 2
    PERMISSION_DENIED = 3
    BAD_REQUEST = 4
    EXPORTER_ERROR = 5
    GLOBAL_MAP_ERROR = 7
    WGRS_ERROR = 8
    WGCCFE_ERROR = 9
    CLAN_IS_DISBANDED = 10
    STRONGHOLD_NOT_FOUND = 11
    WGCCBE_ERROR = 12
    ACCOUNT_BANNED = 13
    SPA_ERROR = 14
    UNKNOWN_ACCOUNT = 15
    CLAN_DOES_NOT_EXIST = 16
    CLAN_ALREADY_DISBANDED = 17
    CLAN_IS_FULL = 18
    ACCOUNT_ALREADY_IN_CLAN = 19
    RECRUITING_POLICY_MISMATCH = 21
    ACCOUNT_DOES_NOT_MEET_REQUIREMENTS = 22
    TOO_MANY_INVITES = 23
    INVITE_DOES_NOT_EXIST = 24
    INVITE_IS_NOT_ACTIVE = 25
    TOO_MANY_APPLICATIONS = 26
    APPLICATION_DOES_NOT_EXIST = 27
    APPLICATION_IS_NOT_ACTIVE = 28
    ACCOUNT_NOT_IN_CLAN = 29
    CLAN_IS_NOT_ACTIVE = 30
    RATINGS_NOT_FOUND = 31
    CLIENTGW_ERROR = 32
    EXPORTER_DISABLED = 33
    GLOBAL_MAP_DISABLED = 34
    WGRS_DISABLED = 35
    WGCCFE_DISABLED = 36
    SPA_DISABLED = 37
    WGCCBE_DISABLED = 38
    ACCOUNT_IN_TRANSACTION = 39
    CLAN_IN_TRANSACTION = 40
    ACCOUNT_ALREADY_INVITED = 41
    ACCOUNT_ALREADY_APPLIED = 42
    ACCOUNT_IN_COOLDOWN = 43


class BaseRequestError(SoftException):

    def __init__(self, *args, **kwargs):
        if b'extra_data' in kwargs:
            self.extra_data = kwargs[b'extra_data']
        return


class AuthentificationError(BaseRequestError):
    status_code = 401
    response_code = ResponseCodes.AUTHENTIFICATION_ERROR
    description = b'User is not authentificated'


class PermissionDenied(BaseRequestError):
    status_code = 403
    response_code = ResponseCodes.PERMISSION_DENIED
    description = b'Forbidden'


class BadRequest(BaseRequestError):
    status_code = 400
    description = b'Bad request'
    response_code = ResponseCodes.BAD_REQUEST


class ExporterError(BaseRequestError):
    status_code = 500
    description = b'Exporter error was occurred'
    response_code = ResponseCodes.EXPORTER_ERROR


class SpaError(BaseRequestError):
    status_code = 500
    description = b'SPA error was occurred'
    response_code = ResponseCodes.SPA_ERROR


class GlobalMapError(BaseRequestError):
    status_code = 500
    description = b'Global map error was occurred'
    response_code = ResponseCodes.GLOBAL_MAP_ERROR


class WgrsError(BaseRequestError):
    status_code = 500
    description = b'Grs error was occurred'
    response_code = ResponseCodes.WGRS_ERROR


class WgccfeError(BaseRequestError):
    description = b'WGCCFE error was occurred'
    status_code = 500
    response_code = ResponseCodes.WGCCFE_ERROR


class ClanDisbandedError(BaseRequestError):
    description = b'Clan is disbanded'
    status_code = 409
    response_code = ResponseCodes.CLAN_IS_DISBANDED


class StrongholdNotFoundError(BaseRequestError):
    description = b'Stronghold is not found'
    status_code = 409
    response_code = ResponseCodes.STRONGHOLD_NOT_FOUND


class WgccbeError(BaseRequestError):
    description = b'WGCCBE error was occurred'
    status_code = 500
    response_code = ResponseCodes.WGCCBE_ERROR


class AccountBannedError(BaseRequestError):
    description = b'Account is banned'
    status_code = 403
    response_code = ResponseCodes.ACCOUNT_BANNED


class UnknownAccountError(BaseRequestError):
    description = b'Account in unknown'
    status_code = 404
    response_code = ResponseCodes.UNKNOWN_ACCOUNT


class RatingsNotFoundError(BaseRequestError):
    description = b'Ratings not found error'
    status_code = 404
    response_code = ResponseCodes.RATINGS_NOT_FOUND


class ClanDoesNotExistError(BaseRequestError):
    description = b'Clan does not exist'
    status_code = 404
    response_code = ResponseCodes.CLAN_DOES_NOT_EXIST


class ClanIsFullError(BaseRequestError):
    description = b'Clan has not free space'
    status_code = 409
    response_code = ResponseCodes.CLAN_IS_FULL


class AccountInClanError(BaseRequestError):
    description = b'Account is in clan already'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_ALREADY_IN_CLAN


class AccountNotInClanError(BaseRequestError):
    description = b'Account is not in clan'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_NOT_IN_CLAN


class RecruitingPolicyError(BaseRequestError):
    description = b'Recruiting policy mismatch'
    status_code = 409
    response_code = ResponseCodes.RECRUITING_POLICY_MISMATCH


class AccountRequirementsError(BaseRequestError):
    description = b'Account does not meet requirements'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_DOES_NOT_MEET_REQUIREMENTS


class TooManyInvitesError(BaseRequestError):
    description = b'Too many invites'
    status_code = 409
    response_code = ResponseCodes.TOO_MANY_INVITES


class InviteDoesNotExistError(BaseRequestError):
    description = b'Invite does not exist'
    status_code = 404
    response_code = ResponseCodes.INVITE_DOES_NOT_EXIST


class InviteIsNotActiveError(BaseRequestError):
    description = b'Invite is not active'
    status_code = 409
    response_code = ResponseCodes.INVITE_IS_NOT_ACTIVE


class TooManyApplicationsError(BaseRequestError):
    description = b'Too Many Applications'
    status_code = 409
    response_code = ResponseCodes.TOO_MANY_APPLICATIONS


class ApplicationDoesNotExistError(BaseRequestError):
    description = b'Application does not exist'
    status_code = 404
    response_code = ResponseCodes.APPLICATION_DOES_NOT_EXIST


class ApplicationIsNotActiveError(BaseRequestError):
    description = b'Application is not active'
    status_code = 409
    response_code = ResponseCodes.APPLICATION_IS_NOT_ACTIVE


class ClanIsNotActiveError(BaseRequestError):
    description = b'Clan is not active'
    status_code = 409
    response_code = ResponseCodes.CLAN_IS_NOT_ACTIVE


class ClientgwError(BaseRequestError):
    description = b'CLIENTGW error is occurred'
    status_code = 500
    response_code = ResponseCodes.CLIENTGW_ERROR


class ExporterDisabled(BaseRequestError):
    description = b'Exporter proxying is disabled'
    status_code = 503
    response_code = ResponseCodes.EXPORTER_DISABLED


class GlobalMapDisabled(BaseRequestError):
    description = b'Global map proxying is disabled'
    status_code = 503
    response_code = ResponseCodes.GLOBAL_MAP_DISABLED


class WgrsDisabled(BaseRequestError):
    description = b'WGRS proxying is disabled'
    status_code = 503
    response_code = ResponseCodes.WGRS_DISABLED


class WgccfeDisabled(BaseRequestError):
    description = b'WGCCFE proxying is disabled'
    status_code = 503
    response_code = ResponseCodes.WGCCFE_DISABLED


class SpaDisabled(BaseRequestError):
    description = b'SPA proxying is disabled'
    status_code = 503
    response_code = ResponseCodes.SPA_DISABLED


class WgccbeDisabled(BaseRequestError):
    description = b'WGCCBE proxying is disabled'
    status_code = 503
    response_code = ResponseCodes.WGCCBE_DISABLED


class AccountInTransaction(BaseRequestError):
    description = b'Account in transaction'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_IN_TRANSACTION


class ClanInTransaction(BaseRequestError):
    description = b'Clan in transaction'
    status_code = 409
    response_code = ResponseCodes.CLAN_IN_TRANSACTION


class AccountAlreadyInvited(BaseRequestError):
    description = b'Account already invited'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_ALREADY_INVITED


class AccountAlreadyApplied(BaseRequestError):
    description = b'Account already applied'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_ALREADY_APPLIED


class AccountInCooldown(BaseRequestError):
    description = b'Account in cooldown'
    status_code = 409
    response_code = ResponseCodes.ACCOUNT_IN_COOLDOWN
