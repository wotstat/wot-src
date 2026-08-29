from gui.Scaleform.daapi.view.meta.PerksPanelMeta import PerksPanelMeta
import WWISE, BigWorld
from items import tankmen
from shared_utils import CONST_CONTAINER
from helpers import dependency
from items.components.perks_constants import PerkState
from skeletons.gui.battle_session import IBattleSessionProvider

class PerksSounds(CONST_CONTAINER):
    PERK = b'detachment_perk'


class PerksPanel(PerksPanelMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def setPerks(self, perks):
        self.clearHUD()
        perksData = []
        for perkData in sorted(perks, key=(lambda k: k[b'perkID'])):
            perkID = perkData[b'perkID']
            skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
            perk = {b'perkName': skillName, 
               b'state': (perkData[b'state']), 
               b'duration': (perkData[b'coolDown']), 
               b'lifeTime': (self._getLifeTime(perkData))}
            perksData.append(perk)

        self.as_setPerksS(perksData)
        return

    def updatePerks(self, changedPerks, prevPerks):
        for perkID, perkData in changedPerks.iteritems():
            lifeTime = self._getLifeTime(perkData)
            state = perkData[b'state']
            skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
            self.as_updatePerkS(skillName, state, perkData[b'coolDown'], lifeTime)
            if state == PerkState.ACTIVE:
                if perkID not in prevPerks or prevPerks[perkID][b'state'] != PerkState.ACTIVE:
                    WWISE.WW_eventGlobal(PerksSounds.PERK)

        return

    def clearHUD(self):
        self.as_clearPanelS()
        return

    def _getLifeTime(self, perkData):
        lifeTimeServer = perkData[b'lifeTime']
        if BigWorld.serverTime() < lifeTimeServer:
            return lifeTimeServer - BigWorld.serverTime()
        return -1
