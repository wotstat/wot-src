from items.vehicles import EnhancementItem

class VehicleEnhancements(object):

    def __init__(self, enhancements):
        self.factors = []
        for items in enhancements.itervalues():
            for enhancement in items.itervalues():
                if b'factors' in enhancement:
                    self.factors.extend([EnhancementItem(factor[b'name'], factor[b'value'], factor[b'operation']) for factor in enhancement[b'factors']])

        return

    def onCollectFactors(self, factors):
        for factor in self.factors:
            factors[factor.name] = factor.applyFactor(factors[factor.name])

        return
