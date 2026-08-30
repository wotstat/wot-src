import typing
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Dict

class BaseScoreRule(object):
    RULE_ID = None

    def __init__(self, config):
        self.score = 0
        self.weight = 0
        self._initFromConfig(config)
        return

    def _initFromConfig(self, config):
        score = config.get(b'score')
        weight = config.get(b'weight')
        if score is None or weight is None:
            raise SoftException(b'[base_score_rule] sections <score> and <weight> are missing')
        self.score = score
        self.weight = weight
        return
