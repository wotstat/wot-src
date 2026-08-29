from shared_utils import CONST_CONTAINER

class BROWSER(CONST_CONTAINER):
    SIZE = (990, 550)
    VIDEO_SIZE = (864, 486)


class PROMO(CONST_CONTAINER):

    class TEMPLATE(CONST_CONTAINER):
        PATCH = b'promo_patchnote'
        ACTION = b'promo_action'
