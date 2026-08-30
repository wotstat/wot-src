from __future__ import absolute_import
import BigWorld
from debug_utils import LOG_ERROR, LOG_DEBUG
_IS_ENABLED = True
if _IS_ENABLED:

    def add(path, forced=False):
        result = True
        try:
            result = BigWorld.wg_precacheScaleformResource(path, forced)
            if result:
                LOG_DEBUG(b'Resource is added to precache', path)
        except AttributeError:
            LOG_ERROR(b'BigWorld package does not include function wg_precacheScaleformResource')

        return result


    def clear(path=b''):
        try:
            BigWorld.wg_eraseScaleformResFromCache(path)
            LOG_DEBUG(b'Resource(s) is(are) cleared from precache', path)
        except AttributeError:
            LOG_ERROR(b'BigWorld package does not include function wg_eraseScaleformResFromCache')

        return


else:

    def add(path, forced=False):
        return True


    def clear(path=b''):
        return
