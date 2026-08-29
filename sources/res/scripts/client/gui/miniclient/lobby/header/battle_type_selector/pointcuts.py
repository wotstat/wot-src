from helpers import aop
import aspects

class _BattleItemSelector(aop.Pointcut):

    def __init__(self, battleTypeBuilderMethod, aspects_):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.header', b'battle_selector_items', battleTypeBuilderMethod, aspects=aspects_)
        return


class RankedBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, b'_addRankedBattleType', (
         aspects.RankedBattle,))
        return


class CommandBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, b'_addCommandBattleType', (
         aspects.CommandBattle,))
        return


class TrainingBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, b'_addTrainingBattleType', (
         aspects.TrainingBattle,))
        return


class SpecialBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, b'_addSpecialBattleType', (
         aspects.SpecialBattle,))
        return


class StrongholdBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, b'_addStrongholdsBattleType', (
         aspects.StrongholdBattle,))
        return


class OnBattleTypeSelectorPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover', b'BattleTypeSelectPopover', b'_populate', aspects=(
         aspects.OnBattleTypeSelectorPopulate,))
        return
