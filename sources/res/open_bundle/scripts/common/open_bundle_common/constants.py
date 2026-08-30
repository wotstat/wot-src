from __future__ import absolute_import
from datetime import timedelta
OPEN_BUNDLE_GAME_PARAMS_KEY = b'open_bundle_config'
OPEN_BUNDLE_PDATA_KEY = b'openBundle'
MIN_X_COORDINATE = 0
MIN_Y_COORDINATE = 0
MAX_X_COORDINATE = 12
MAX_Y_COORDINATE = 5
OPEN_BUNDLE_MAX_CELLS = (MAX_X_COORDINATE - MIN_X_COORDINATE) * (MAX_Y_COORDINATE - MIN_Y_COORDINATE)
OPEN_BUNDLE_CELL_TAGS = (b'rare', b'uniqueNotification')
OPEN_BUNDLE_TEMPLATES = (b'S1', b'S2', b'S3', b'S4', b'M1', b'M2', b'L1')
OPEN_BUNDLE_DATA_LIFETIME = timedelta(days=60).total_seconds()
OPEN_BUNDLE_FIXED_REWARD_LOGGING_OFFSET = 1000
