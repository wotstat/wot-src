from tutorial.control import context

class SalesStartReqs(context.StartReqs):

    def isEnabled(self):
        return True

    def prepare(self, ctx):
        return

    def process(self, descriptor, ctx):
        return True
