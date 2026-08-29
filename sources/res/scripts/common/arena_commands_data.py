from collections import namedtuple
HESH_MAP_SIZE = 1000
HESH_GRID_STEP = 6
MAX_POSE_SIZE = HESH_MAP_SIZE / HESH_GRID_STEP

def getHashCode(pose):
    return sum([int(coord + HESH_MAP_SIZE * 0.5 + 0.5) / HESH_GRID_STEP * MAX_POSE_SIZE ** i for i, coord in enumerate(pose)])


class ArenaCommandData(namedtuple(b'ArenaCommandData', [
 6, 
 7, 
 8, 
 9, 
 10])):

    @staticmethod
    def getCommandData(*args, **kwargs):
        if kwargs:
            data = ArenaCommandData(kwargs.get(b'commandName', b'PREBATTLE_WAYPOINT'), kwargs.get(b'position', (0.0, 0.0, 0.0)), kwargs.get(b'team', b'') or kwargs.get(b'teams', b'both'), kwargs.get(b'name', b'') or kwargs.get(b'locationName', b'ERROR'), kwargs.get(b'state', b'IDLE'))
            return (
             getHashCode(kwargs[b'position']), data)
        else:
            return


ArenaCommandData.__new__.__defaults__ = (None,) * len(ArenaCommandData._fields)
