class IPrbListRequester(object):

    def start(self, callback):
        return

    def stop(self):
        return

    def request(self, ctx=None):
        return


class IUnitRequestProcessor(object):

    def init(self):
        return

    def fini(self):
        return

    def doRequest(self, ctx, methodName, *args, **kwargs):
        return

    def doRequestChain(self, ctx, chain):
        return

    def doRawRequest(self, methodName, *args, **kwargs):
        return
