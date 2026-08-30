import enumerations
BTMS_COMMANDS = enumerations.Enumeration(b'Battle messenger commands', [
 (
  b'ChannelsInit', (lambda : b'Messenger.Battle.ChannelsInit')),
 (
  b'CheckCooldownPeriod', (lambda : b'Messenger.Battle.CheckCooldownPeriod')),
 (
  b'SendMessage', (lambda : b'Messenger.Battle.SendMessage')),
 (
  b'ReceiveMessage', (lambda : b'Messenger.Battle.RecieveMessage')),
 (
  b'ClearMessages', (lambda : b'Messenger.Battle.ClearMessages')),
 (
  b'PopulateUI', (lambda : b'Messenger.Battle.PopulateUI')),
 (
  b'RefreshUI', (lambda : b'Messenger.Battle.RefreshUI')),
 (
  b'ChangeFocus', (lambda : b'Messenger.Battle.ChangeFocus')),
 (
  b'JoinToChannel', (lambda : b'Messenger.Battle.JoinToChannel')),
 (
  b'ShowActionFailureMessage', (lambda : b'Messenger.Battle.ShowActionFailureMesssage')),
 (
  b'UpdateReceivers', (lambda : b'Messenger.Battle.UpdateReceivers')),
 (
  b'UserPreferencesUpdated', (lambda : b'Messenger.Battle.UserPreferencesUpdated')),
 (
  b'ReceiverChanged', (lambda : b'Messenger.Battle.ReceiverChanged')),
 (
  b'AddToFriends', (lambda : b'Battle.UsersRoster.AddToFriends')),
 (
  b'RemoveFromFriends', (lambda : b'Battle.UsersRoster.RemoveFromFriends')),
 (
  b'AddToIgnored', (lambda : b'Battle.UsersRoster.AddToIgnored')),
 (
  b'RemoveFromIgnored', (lambda : b'Battle.UsersRoster.RemoveFromIgnored')),
 (
  b'AddMuted', (lambda : b'Battle.UsersRoster.AddMuted')),
 (
  b'RemoveMuted', (lambda : b'Battle.UsersRoster.RemoveMuted')),
 (
  b'isHistoryEnabled', (lambda : b'Messenger.Battle.isHistoryEnabled')),
 (
  b'upHistory', (lambda : b'Messenger.Battle.upHistory')),
 (
  b'downHistory', (lambda : b'Messenger.Battle.downHistory')),
 (
  b'EnabledHistoryControls', (lambda : b'Messenger.Battle.EnabledHistoryControls')),
 (
  b'GetLatestHistory', (lambda : b'Messenger.Battle.GetLatestHistory')),
 (
  b'ShowHistoryMessages', (lambda : b'Messenger.Battle.ShowHistoryMessages')),
 (
  b'GetLastMessages', (lambda : b'Messenger.Battle.GetLastMessages')),
 (
  b'ShowLatestMessages', (lambda : b'Messenger.Battle.ShowLatestMessages'))], instance=enumerations.CallabbleEnumItem)

class FILL_COLORS(object):
    BLACK = b'black'
    BROWN = b'brown'
    GREEN = b'green'
    RED = b'red'
