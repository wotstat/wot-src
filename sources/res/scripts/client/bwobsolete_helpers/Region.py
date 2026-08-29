import BigWorld, FantasyDemo

class Region:

    def __init__(self):
        self.currentSpace = b''
        self.currentRegion = None
        self.currentDesc = b''
        self.listeners = []
        FantasyDemo.addChangeEnvironmentsListener(self.onChangeEnvironments)
        return

    def fini(self):
        FantasyDemo.delChangeEnvironmentsListener(self.onChangeEnvironments)
        return

    def addListener(self, l):
        self.listeners.append(l)
        l.onEnterRegion(self.describeCurrent())
        return

    def delListener(self, l):
        try:
            self.listeners.remove(l)
        except ValueError:
            pass

        return

    def describeCurrent(self):
        if self.currentRegion != None:
            return self.currentRegion
        else:
            return self.currentSpace
            return

    def onChangeEnvironments(self, inside):
        player = BigWorld.player()
        if player != None:
            spaceID = player.spaceID
            try:
                self.currentSpace = self.fancify(FantasyDemo.rds.spaceNameMap[spaceID])
            except KeyError:
                self.currentSpace = b''

            self.checkForChanges()
        return

    def fancify(self, name):
        name = name.split(b'spaces/')[-1]
        name = name.replace(b'_', b' ')
        name = name.title()
        return name

    def onEnterRegion(self, description):
        if self.currentRegion != description:
            self.currentRegion = description
            self.checkForChanges()
        return

    def onLeaveRegion(self, description):
        if self.currentRegion == description:
            self.currentRegion = None
            self.checkForChanges()
        return

    def checkForChanges(self):
        desc = self.describeCurrent()
        if self.currentDesc != desc:
            self.currentDesc = desc
            for l in self.listeners:
                l.onEnterRegion(desc)

        return
