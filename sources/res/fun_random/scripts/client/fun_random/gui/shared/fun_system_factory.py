from __future__ import absolute_import
from gui.shared.system_factory import CollectEventsManager

class FunFactoryConstants(object):
    SUB_MODE = 0
    BATTLE_RESULTS_SUB_FORMATTER = 1
    BATTLE_RESULTS_SUB_PRESENTER = 2
    BATTLE_RESULTS_SOUND_ENV = 3
    MODE_ASSETS_PACK_CONFIG_PATH = 4


__collectFunRandomEM = CollectEventsManager()

def registerFunRandomSubMode(subModeImpl, subMode):

    def onCollect(ctx):
        ctx[subModeImpl] = subMode
        return

    __collectFunRandomEM.addListener((FunFactoryConstants.SUB_MODE, subModeImpl), onCollect)
    return


def collectFunRandomSubMode(subModeImpl):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.SUB_MODE, subModeImpl), {}).get(subModeImpl)


def registerBattleResultsMessageSubFormatter(arenaGuiType, battleResultsFormatterCls):

    def onCollect(ctx):
        ctx[b'battleResultsSubFormatter'] = battleResultsFormatterCls
        return

    __collectFunRandomEM.addListener((FunFactoryConstants.BATTLE_RESULTS_SUB_FORMATTER, arenaGuiType), onCollect)
    return


def collectBattleResultsMessageSubFormatter(arenaGuiType):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.BATTLE_RESULTS_SUB_FORMATTER, arenaGuiType), ctx={}).get(b'battleResultsSubFormatter')


def registerBattleResultsSubPresenter(subModeImpl, subPresenterCls, viewCls):

    def onCollect(ctx):
        ctx[b'battleResultsSubPresenters'][subModeImpl] = (
         subPresenterCls, viewCls)
        return

    __collectFunRandomEM.addListener(FunFactoryConstants.BATTLE_RESULTS_SUB_PRESENTER, onCollect)
    return


def collectBattleResultsSubPresenters():
    return __collectFunRandomEM.handleEvent(FunFactoryConstants.BATTLE_RESULTS_SUB_PRESENTER, {b'battleResultsSubPresenters': {}})[b'battleResultsSubPresenters']


def registerBattleResultsSoundEnv(arenaGuiType, battleResultsSoundEnvCls):

    def onCollect(ctx):
        ctx[b'battleResultsSoundEnv'] = battleResultsSoundEnvCls
        return

    __collectFunRandomEM.addListener((FunFactoryConstants.BATTLE_RESULTS_SOUND_ENV, arenaGuiType), onCollect)
    return


def collectBattleResultsSoundEnv(arenaGuiType):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.BATTLE_RESULTS_SOUND_ENV, arenaGuiType), ctx={}).get(b'battleResultsSoundEnv')


def registerModeAssetsPackConfigPath(assetsPointer, path):

    def onCollect(ctx):
        ctx[b'modeAssetsPackConfigPath'] = path
        return

    __collectFunRandomEM.addListener((FunFactoryConstants.MODE_ASSETS_PACK_CONFIG_PATH, assetsPointer), onCollect)
    return


def collectModeAssetsPackConfigPath(assetsPointer):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.MODE_ASSETS_PACK_CONFIG_PATH, assetsPointer), ctx={}).get(b'modeAssetsPackConfigPath', b'')
