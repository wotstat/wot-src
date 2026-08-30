from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import RoleCriteriesGroup
from gui.shared.utils.requesters.ItemsRequester import RequestCriteria, PredicateCondition
FL_RENT = RequestCriteria(PredicateCondition((lambda item: item.name.endswith(b'_FL'))))

class FLRentedCriteriesGroup(RoleCriteriesGroup):

    def update(self, filters):
        super(FLRentedCriteriesGroup, self).update(filters)
        if not filters[b'rented']:
            self._criteria |= ~FL_RENT
        return

    @staticmethod
    def isApplicableFor(vehicle):
        return True
