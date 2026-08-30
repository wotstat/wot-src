from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
_tmanTotalBlockLayout = [
 b'battlesCount']
_tmanTotalBlockBuilder = StaticSizeBlockBuilder(b'total', _tmanTotalBlockLayout, {}, [])
TMAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32, 
 33, 
 34]
_tankmanAchievementsBlockBuilder = StaticSizeBlockBuilder(b'achievements', TMAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, [])
tmanDossierLayout = (
 _tmanTotalBlockBuilder,
 _tankmanAchievementsBlockBuilder)
