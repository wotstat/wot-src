from __future__ import absolute_import
from visual_script.block import Meta

class PVEBattleHUDMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16742912

    @classmethod
    def blockCategory(cls):
        return b'Event HUD'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/hint'
