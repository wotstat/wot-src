from helpers import aop
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.MENU import MENU
from gui.shared.formatters import text_styles, icons
from gui.prb_control.settings import PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import _DisabledSelectorItem

class _BattleTypeDisable(aop.Aspect):

    def __init__(self, battleTypeAttributes):
        self._battleTypeAttributes = battleTypeAttributes
        aop.Aspect.__init__(self)
        return

    def atCall(self, cd):
        cd.avoid()
        items = cd.args[0]
        items.append(_DisabledSelectorItem(*self._battleTypeAttributes))
        return


class RankedBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (
         MENU.HEADERBUTTONS_BATTLE_TYPES_RANKED,
         PREBATTLE_ACTION_NAME.RANKED,
         1))
        return


class CommandBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (
         MENU.HEADERBUTTONS_BATTLE_TYPES_UNIT,
         PREBATTLE_ACTION_NAME.E_SPORT,
         3,
         SELECTOR_BATTLE_TYPES.UNIT))
        return


class SortieBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (
         MENU.HEADERBUTTONS_BATTLE_TYPES_STRONGHOLDS,
         PREBATTLE_ACTION_NAME.STRONGHOLD,
         5,
         SELECTOR_BATTLE_TYPES.SORTIE))
        return


class TrainingBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (
         MENU.HEADERBUTTONS_BATTLE_TYPES_TRAINING,
         PREBATTLE_ACTION_NAME.TRAININGS_LIST,
         7))
        return


class SpecialBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (
         MENU.HEADERBUTTONS_BATTLE_TYPES_SPEC,
         PREBATTLE_ACTION_NAME.SPEC_BATTLES_LIST,
         6))
        return


class StrongholdBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (
         MENU.HEADERBUTTONS_BATTLE_TYPES_STRONGHOLDS,
         PREBATTLE_ACTION_NAME.STRONGHOLDS_BATTLES_LIST,
         4))
        return


class OnBattleTypeSelectorPopulate(aop.Aspect):

    def atReturn(self, cd):
        cd.self.as_showMiniClientInfoS((b'{0} {1}').format(icons.alert(-3), text_styles.main(_ms(b'#miniclient:battle_type_select_popover/message'))), _ms(b'#miniclient:personal_quests_welcome_view/continue_download'))
        return
