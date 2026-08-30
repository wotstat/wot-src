from __future__ import absolute_import
from typing import NamedTuple, List, Optional
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution
IconSetData = NamedTuple(b'IconSetData', [
 (
  b'iconRes', int),
 (
  b'label', Optional[str]),
 (
  b'imageSubstitutions', Optional[List[ImageSubstitution]])])
