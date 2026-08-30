from __future__ import absolute_import
import typing
from dict2model import fields, validate
from helpers import dependency
from hints_common.battle.schemas.base import HMCContextType, HMCPropsType
from hints.battle.newbie import getLogger
from hints.battle.schemas.base import ClientHintHistoryModel, ClientHintHistorySchema, ClientHintModel, ClientHintSchema, CHMTextType, CHMVisualType, CHMSoundType, CHMLifecycleType
from skeletons.gui.battle_hints.newbie_battle_hints_controller import INewbieBattleHintsController
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory
    from typing import Optional
_logger = getLogger(b'Model')
_DEFAULT_DISPLAY_COUNT = 5

class NewbieClientHintHistoryModel(ClientHintHistoryModel):
    __slots__ = (b'displayCount',)

    def __init__(self, modifyPriority, cooldown, totalDisplayCount, perBattleCount, displayCount):
        super(NewbieClientHintHistoryModel, self).__init__(modifyPriority, cooldown, totalDisplayCount, perBattleCount)
        self.displayCount = displayCount
        return

    def _reprArgs(self):
        return (b'{}, displayCount={}').format(super(NewbieClientHintHistoryModel, self)._reprArgs(), self.displayCount)


class NewbieClientHintHistorySchema(ClientHintHistorySchema[NewbieClientHintHistoryModel]):
    __slots__ = ()

    def __init__(self):
        super(NewbieClientHintHistorySchema, self).__init__(checkUnknown=True, modelClass=NewbieClientHintHistoryModel)
        self._fields[b'displayCount'] = fields.Integer(required=False, default=_DEFAULT_DISPLAY_COUNT, deserializedValidators=validate.Range(minValue=1))
        return


class NewbieClientHintModel(ClientHintModel[HMCPropsType, HMCContextType, CHMTextType, CHMVisualType, CHMSoundType, CHMLifecycleType, NewbieClientHintHistoryModel]):
    __slots__ = ()
    _newbieHintsCtrl = dependency.descriptor(INewbieBattleHintsController)

    def validate(self, *args, **kwargs):
        if not self._newbieHintsCtrl.isEnabled():
            _logger.debug(b'Hint <%s> action disabled by server.', self.uniqueName)
            return False
        return super(NewbieClientHintModel, self).validate(*args, **kwargs)

    def canBeShown(self, historyStorage=None):
        if not self._newbieHintsCtrl.isEnabled() or not self._newbieHintsCtrl.isUserSettingEnabled():
            _logger.debug(b'Can not show <%s>. Disabled by server or user.', self.uniqueName)
            return False
        else:
            if self.history is not None:
                displayCount = self._newbieHintsCtrl.getDisplayCount(self.uniqueName)
                if displayCount is None:
                    _logger.debug(b'Can not show <%s>. History completed or disabled.', self.uniqueName)
                    return False
                if displayCount >= self.history.displayCount:
                    _logger.debug(b'Can not show <%s>. Hint reached display limit.', self.uniqueName)
                    return False
            return super(NewbieClientHintModel, self).canBeShown(historyStorage)


hintSchema = ClientHintSchema[NewbieClientHintModel](historySchema=NewbieClientHintHistorySchema(), modelClass=NewbieClientHintModel)
