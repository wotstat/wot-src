import logging, BigWorld, BattleRoyaleConstants as brc
_logger = logging.getLogger(__name__)

class AccountBattleRoyaleComponent(BigWorld.StaticScriptComponent):

    def applyTestDrive(self, invID, callback=None):
        _logger.debug(b"apply test drive for: '%r'", invID)
        self.entity._doCmdIntStr(brc.CMD_BATTLE_ROYALE_TEST_DRIVE, invID, b'', callback)
        return

    def applyRent(self, invID, callback=None):
        _logger.debug(b"apply rent for: '%r'", invID)
        self.entity._doCmdIntStr(brc.CMD_BATTLE_ROYALE_RENT, invID, b'', callback)
        return

    def setBrCoin(self, amount, callback=None):
        _logger.debug(b"set battle royale coin amount: '%r'", amount)
        self.entity._doCmdIntStr(brc.CMD_BATTLE_ROYALE_OPERATE_BRCOIN, amount, b'', callback)
        return
