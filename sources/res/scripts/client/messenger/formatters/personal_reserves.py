from gui.impl import backport
from gui.impl.gen import R
from helpers import html
from messenger import g_settings
from messenger.formatters.service_channel import GeneralFormatter

class IPersonalReservesFormatter(GeneralFormatter):

    def __init__(self):
        super(IPersonalReservesFormatter, self).__init__(b'PersonalReservesMessage')
        return


class IPersonalReservesExpirableFormatter(GeneralFormatter):

    def __init__(self):
        super(IPersonalReservesExpirableFormatter, self).__init__(b'PersonalReservesExpirableMessage')
        return


class ReleaseFormatter(IPersonalReservesFormatter):

    def getTitle(self, message, *args):
        return backport.text(R.strings.messenger.serviceChannelMessages.personalReservesRelease.title())

    def getText(self, message, *args):
        return g_settings.htmlTemplates.format(b'personalReservesRelease', ctx={b'boosterCount': (html.escape(message.get(b'values', b'')))})


class PersonalReservesSoonExpirationFormatter(IPersonalReservesExpirableFormatter):

    def getTitle(self, message, *args):
        return backport.text(R.strings.messenger.serviceChannelMessages.personalReservesSoonExpire.title())

    def getText(self, message, *args):
        return g_settings.htmlTemplates.format(b'personalReservesSoonExpire', ctx={b'boosterCount': (html.escape(message.get(b'values', b'')))})
