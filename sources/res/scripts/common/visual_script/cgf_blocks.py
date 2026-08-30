from visual_script.block import Meta
from visual_script.misc import ASPECT

class CGFMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16540163

    @classmethod
    def blockCategory(cls):
        return b'CGF'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/cgf'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR, ASPECT.SERVER]
