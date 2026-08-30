import time, calendar, datetime, XmlConfigReader
from debug_utils import LOG_WARNING
from goodie_constants import GOODIE_VARIETY
from . import goodie_helpers
from items.vehicles import makeVehicleTypeCompDescrByName
from soft_exception import SoftException
_CONFIG_FILE = b'scripts/server_xml/goodies.xml'
g_cache = None

def readConfig(verbose):
    reader = XmlConfigReader.makeReader(_CONFIG_FILE, b'goodies', verbose)
    return _readGoodies(reader, b'goodies')


def _readGoodieResource(section):
    for n, t in goodie_helpers.GOODIE_TEXT_TO_RESOURCE.iteritems():
        v = section.readString(n, b'')
        if v:
            value, isPercentage = XmlConfigReader.parsePercentage(v)
            return (
             t, value, isPercentage)

    raise SoftException(b'Goodie without any resources')
    return


def _readGoodieTarget(reader, subsectionName):
    for n, t in goodie_helpers.GOODIE_TEXT_TO_TARGET.iteritems():
        section = reader.getSubsection((b'/').join((subsectionName, n)))
        if section:
            name = section.readString(b'name', b'')
            if name == b'':
                name = None
            if name and t == goodie_helpers.GOODIE_TARGET_TYPE.ON_BUY_VEHICLE:
                name = makeVehicleTypeCompDescrByName(name)
            limit = section.readInt(b'limit', 0)
            if limit == 0:
                limit = None
            resource = _readGoodieResource(section)
            return (
             (
              t, name, limit), resource)

    return


def _readGoodieCondition(section):
    if section is None:
        return
    else:
        for n, t in goodie_helpers.GOODIE_TEXT_TO_CONDITION.iteritems():
            value = section.readString(n, b'')
            if value:
                return (t, int(value))

        return


def _readPrice(reader, subsectionName):
    priceSectionName = subsectionName + b'/price'
    if reader.getSubsection(priceSectionName) is None:
        return
    else:
        if reader.getSubsection(priceSectionName + b'/gold') is not None:
            isGold = True
        else:
            isGold = False
        value = reader.getSubsection(subsectionName).readInt(b'price', 0)
        if isGold:
            return (0, value)
        return (value, 0)
        return


def _validator(uid, variety, resource, price):
    t, value, isPercentage = resource
    if value < 0:
        raise SoftException(b'Bad goodie %d value (negative) %d' % uid % value)
    if variety in GOODIE_VARIETY.DISCOUNT_LIKE and isPercentage and value > 100:
        raise SoftException(b'Bad goodie %d value %d' % uid % value)
    if price is not None and price <= 0:
        raise SoftException(b'Bad goodie %d price (negative or zero) %d' % uid % price)
    return


def _readGoodies(reader, subsectionName):
    section = reader.getSubsection(subsectionName)
    if section is None:
        return {}
    else:
        goodies = {b'goodies': {}, b'prices': {}, b'notInShop': (set())}
        for packet_name, packet in section.items():
            v, uid = (None, -1)
            if b'_' in packet_name:
                v, uid = packet_name.split(b'_')
            variety = GOODIE_VARIETY.NAME_TO_ID.get(v, None)
            if variety is None:
                raise SoftException(b'No <%s> parameter' % b'variety')
            uid = int(uid)
            if uid < 0:
                raise SoftException(b'No <uid> parameter')
            enabled = bool(packet.readInt(b'enabled', 1))
            autostart = bool(packet.readInt(b'autostart', 0))
            notInShop = bool(packet.readInt(b'notInShop', 1))
            counter = packet.readInt(b'counter', 1)
            lifetime = XmlConfigReader.parseDuration(packet.readString(b'lifetime', b'0'))
            if lifetime == 0:
                lifetime = None
            useby = packet.readString(b'useby', b'')
            if useby == b'':
                useby = None
            else:
                useby = calendar.timegm(datetime.datetime.strptime(useby, b'%d.%m.%Y %H:%M:%S').timetuple())
            condition = _readGoodieCondition(reader.getSubsection((b'/').join((subsectionName, packet_name, b'condition'))))
            target, resource = _readGoodieTarget(reader, (b'/').join((subsectionName, packet_name)))
            price = _readPrice(reader, (b'/').join((subsectionName, packet_name)))
            _validator(uid, variety, resource, price)
            goodies[b'goodies'][uid] = (
             variety, target, enabled, lifetime, useby, counter, autostart, condition, resource)
            if price is not None:
                goodies[b'prices'][uid] = price
            if notInShop or price is None:
                goodies[b'notInShop'].add(uid)
            elif useby is not None and useby < time.time():
                LOG_WARNING(b'Expired goodie is removed from the shop %d' % uid)
                goodies[b'notInShop'].add(uid)

        return goodies


def init(gameParams=None):
    global g_cache
    if gameParams is not None:
        goodies = gameParams[b'goodies']
    else:
        goodies = readConfig(True)
    if g_cache is None:
        g_cache = {}
    else:
        g_cache.clear()
    g_cache.update(goodie_helpers.loadDefinitions(goodies))
    return
