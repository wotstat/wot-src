from __future__ import absolute_import
from items.readers import chassis_readers
from items.readers import gun_readers
from items.readers import shared_readers
from items.readers import skills_readers
from items.readers import sound_readers
from items.readers import tankmen_readers
from constants import HAS_DEV_RESOURCES
if HAS_DEV_RESOURCES:
    from items.readers.json_reader import vehicle_reader
__all__ = (b'chassis_readers', b'gun_readers', b'shared_readers', b'skills_readers', b'sound_readers', b'tankmen_readers', b'json_vehicle_reader')
if HAS_DEV_RESOURCES:
    json_vehicle_reader = vehicle_reader
else:
    json_vehicle_reader = None
