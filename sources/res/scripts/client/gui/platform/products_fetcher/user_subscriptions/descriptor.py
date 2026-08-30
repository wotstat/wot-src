import time, calendar

class UserSubscriptionDescriptor(object):

    def __init__(self, data):
        self._params = data
        return

    @property
    def productCode(self):
        return self._params.get(b'product_code')

    @property
    def status(self):
        return self._params.get(b'status')

    @property
    def nextBilling(self):
        if self._params.get(b'next_billing_time') is None:
            return 0
        else:
            return int(calendar.timegm(time.strptime(self._params.get(b'next_billing_time'), b'%Y-%m-%dT%H:%M:%SZ')))
