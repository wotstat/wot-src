from collections import namedtuple
from messenger.doc_loaders import _xml_helpers
from messenger.m_constants import BATTLE_CHANNEL

def _readSet(xmlCtx, section, _, readers):
    result = []
    items = section[b'items']
    if items is None:
        raise _xml_helpers.XMLError(xmlCtx, b'Items not found')
    for tagName, subSec in items.items():
        if tagName != b'item':
            raise _xml_helpers.XMLError(xmlCtx, (b'Tag "{0:>s}" is invalid').format(tagName))
        ctx = xmlCtx.next(subSec)
        name = _xml_helpers.readNoEmptyStr(xmlCtx, subSec, b'name', b'Item name is not defined')
        if name not in readers:
            raise _xml_helpers.XMLError(xmlCtx, (b'Item "{0:>s}" is not valid').format(name))
        result.append(readers[name](ctx, subSec, settings=None))

    return result


def _readSettings(xmlCtx, section, settings, setReaders, itemReaders):
    for tagName, subSec in section.items():
        if tagName == b'name':
            continue
        if tagName == b'set':
            readers = setReaders
        elif tagName == b'item':
            readers = itemReaders
        else:
            raise _xml_helpers.XMLError(xmlCtx, (b'Tag "{0:>s}" is invalid').format(tagName))
        ctx = xmlCtx.next(subSec)
        name = _xml_helpers.readNoEmptyStr(ctx, subSec, b'name', b'Tag "name" is not defined')
        if name not in readers:
            raise _xml_helpers.XMLError(ctx, (b'Set/item "{0:>s}" is not valid').format(name))
        readers[name](ctx, subSec, settings)

    return


def _readServiceChannel(xmlCtx, section, settings):
    result = dict(_readSet(xmlCtx, section, settings, {b'highPriorityMsgLifeTime': (_xml_helpers.readFloatItem), 
       b'highPriorityMsgAlphaSpeed': (_xml_helpers.readFloatItem), 
       b'mediumPriorityMsgLifeTime': (_xml_helpers.readFloatItem), 
       b'mediumPriorityMsgAlphaSpeed': (_xml_helpers.readFloatItem), 
       b'stackLength': (_xml_helpers.readIntItem), 
       b'padding': (_xml_helpers.readIntItem)}))
    settings.serviceChannel = settings.serviceChannel._replace(**result)
    return


def _readLobbyColors(xmlCtx, section, settings):
    result = dict(_readSet(xmlCtx, section, settings, {b'breaker': (_xml_helpers.readRGBItem), 
       b'messageBody': (_xml_helpers.readRGBItem), 
       b'badWord': (_xml_helpers.readRGBItem)}))
    settings.colors = settings.colors._replace(**result)
    return


_LOBBY_SET_READERS = {b'serviceChannel': _readServiceChannel}
_LOBBY_ITEM_READERS = {b'messageRawFormat': (_xml_helpers.readUnicodeItem), 
   b'badWordFormat': (_xml_helpers.readUnicodeItem)}

def _readBattleMessageLifeCycle(xmlCtx, section, settings):
    result = dict(_readSet(xmlCtx, section, settings, {b'lifeTime': (_xml_helpers.readFloatItem), 
       b'alphaSpeed': (_xml_helpers.readFloatItem)}))
    settings.messageLifeCycle = settings.messageLifeCycle._replace(**result)
    return


_ReceiverInBattle = namedtuple(b'_ReceiverInBattle', (b'name', b'label', b'modifiers', b'bwModifiers', b'order'))

def _readReceiverValue(xmlCtx, section, settings=None):
    name = _xml_helpers.readNoEmptyStr(xmlCtx, section, b'name', b'Receiver name is not defined')
    valueSec = section[b'value']
    if not valueSec:
        raise _xml_helpers.XMLError(xmlCtx, b'Item value is not defined')
    modifiers = []
    modifiersSec = valueSec[b'modifiers']
    if modifiersSec:
        modifiers = [s.asInt for s in modifiersSec.values()]
    bwModifiers = []
    modifiersSec = valueSec[b'bw-modifiers']
    if modifiersSec:
        bwModifiers = [s.asInt for s in modifiersSec.values()]
    label = _xml_helpers.readNoEmptyI18nStr(xmlCtx.next(valueSec), valueSec, b'label', b'Label is not defined')
    return (
     name,
     _ReceiverInBattle(name, label, modifiers, bwModifiers, valueSec.readInt(b'order')))


def _readReceivers(xmlCtx, section, settings):
    readers = {}
    receivers = {}
    for _, name, label in BATTLE_CHANNEL.ALL:
        readers[name] = _readReceiverValue
        receivers[name] = _ReceiverInBattle(name, label, [], [], 0)

    result = dict(_readSet(xmlCtx, section, settings, readers))
    receivers.update(result)
    settings.receivers = receivers
    return


_BATTLE_SET_READERS = {b'messageLifeCycle': _readBattleMessageLifeCycle, 
   b'receivers': _readReceivers}
_BATTLE_ITEM_READERS = {b'messageFormat': (_xml_helpers.readUnicodeItem), 
   b'targetFormat': (_xml_helpers.readStringItem), 
   b'inactiveStateAlpha': (_xml_helpers.readIntItem), 
   b'hintText': (_xml_helpers.readI18nStringItem), 
   b'toolTipText': (_xml_helpers.readI18nStringItem), 
   b'toolTipTextWithMuteInfo': (_xml_helpers.readI18nStringItem), 
   b'numberOfMessagesInHistory': (_xml_helpers.readIntItem), 
   b'alphaForLastMessages': (_xml_helpers.readIntItem), 
   b'chatIsLockedToolTipText': (_xml_helpers.readI18nStringItem), 
   b'recoveredLatestMessages': (_xml_helpers.readIntItem), 
   b'lifeTimeRecoveredMessages': (_xml_helpers.readIntItem), 
   b'battleRoyaleTooltip': (_xml_helpers.readI18nStringItem)}
_SETTINGS_LOADERS = {b'lobby': (
            _readSettings, _LOBBY_SET_READERS, _LOBBY_ITEM_READERS), 
   b'battle': (
             _readSettings, _BATTLE_SET_READERS, _BATTLE_ITEM_READERS)}

def load(xmlCtx, section, messengerSettings):
    for tagName, subSec in section.items():
        if tagName != b'settings':
            raise _xml_helpers.XMLError(xmlCtx, (b'Tag "{0:>s}" is invalid').format(tagName))
        name = _xml_helpers.readNoEmptyStr(xmlCtx, subSec, b'name', b'Setting name is not defined')
        if name not in _SETTINGS_LOADERS:
            raise _xml_helpers.XMLError(xmlCtx, (b'Setting "{0:>s}" is not valid').format(name))
        loader, setReaders, itemReaders = _SETTINGS_LOADERS[name]
        if hasattr(messengerSettings, name):
            loader(xmlCtx.next(subSec), subSec, getattr(messengerSettings, name), setReaders, itemReaders)
        else:
            raise _xml_helpers.XMLError(xmlCtx, (b'Settings has not attribute {0:>s}').format(name))

    return
