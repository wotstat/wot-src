from events_core_common.score_system.rules.base_score_rule import BaseScoreRule
from soft_exception import SoftException

class CumulativeScoreRule(BaseScoreRule):
    RULE_ID = b'cumulative'

    def __init__(self, config):
        self.count = 0
        super(CumulativeScoreRule, self).__init__(config)
        return

    def _initFromConfig(self, config):
        super(CumulativeScoreRule, self)._initFromConfig(config)
        count = config.get(b'count')
        if count is None:
            raise SoftException(b'[cumulative_score_rule] section <count> is missing')
        self.count = count
        return
