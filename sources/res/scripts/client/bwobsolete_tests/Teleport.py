import BigWorld, Math, math, random
from functools import partial

def teleportNext(timer, destinationList):
    dest = destinationList[0]
    BigWorld.player().tryToTeleport(dest[0], dest[1])
    if len(destinationList) > 1:
        BigWorld.callback(timer, partial(teleportNext, timer, destinationList[1:]))
    else:
        print b'teleport test finished'
    return


def testTeleport():
    d = []
    d.append([b'spaces/highlands', b'demo2'])
    d.append([b'spaces/highlands', b'demo3'])
    d.append([b'spaces/highlands', b'demo4'])
    d.append([b'spaces/arctic', b'demo1'])
    d.append([b'spaces/arctic', b'demo2'])
    d.append([b'spaces/arctic', b'demo3'])
    d.append([b'spaces/arctic', b'demo4'])
    d.append([b'spaces/highlands', b'demo1'])
    BigWorld.callback(0.1, partial(teleportNext, 20, d))
    return
