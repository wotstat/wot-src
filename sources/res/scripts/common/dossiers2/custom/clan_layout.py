from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
_rareAchievementsBlockBuilder = ListBlockBuilder(b'rareAchievements', b'I', {})
clanDossierLayout = (
 _rareAchievementsBlockBuilder,)
CLAN_DOSSIER_LIST_BLOCKS = [b.name for b in clanDossierLayout if isinstance(b, ListBlockBuilder)]
