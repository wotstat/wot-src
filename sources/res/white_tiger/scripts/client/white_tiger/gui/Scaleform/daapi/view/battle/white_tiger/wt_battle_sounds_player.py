import SoundGroups
from gui.battle_control.controllers.battle_hints_ctrl import IBattleHintView

class BattleHintSoundPlayer(IBattleHintView):

    def showHint(self, hint, data):
        super(BattleHintSoundPlayer, self).showHint(hint, data)
        hintName = hint.name
        if hintName == b'wtGeneratorSpawned_hunters' or hintName == b'wtGeneratorSpawned_boss':
            SoundGroups.g_instance.playSound2D(b'ev_white_tiger_widget_icon_generator_03')
        return

    def getAlias(self):
        return b''
