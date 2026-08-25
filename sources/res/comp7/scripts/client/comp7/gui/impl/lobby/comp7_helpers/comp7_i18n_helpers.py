from gui.impl import backport
from gui.impl.gen import R
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank, Division
RANK_MAP = {(Rank.FIRST): b'first', 
   (Rank.SECOND): b'second', 
   (Rank.THIRD): b'third', 
   (Rank.FOURTH): b'fourth', 
   (Rank.FIFTH): b'fifth', 
   (Rank.SIXTH): b'sixth'}
DIVISION_MAP = {(Division.A): b'A', 
   (Division.B): b'B', 
   (Division.C): b'C', 
   (Division.D): b'D', 
   (Division.E): b'E'}

def getRankLocale(rank):
    rankString = RANK_MAP[Rank(rank)]
    return backport.text(R.strings.comp7_ext.rank.dyn(rankString)())


def getDivisionLocale(division):
    divisionString = DIVISION_MAP[Division(division)]
    return backport.text(R.strings.comp7_ext.division.dyn(divisionString)())
