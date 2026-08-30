from __future__ import absolute_import, print_function
import BigWorld, ResMgr
graphicsPresetsResource = b'system/data/graphics_settings_presets.xml'

class GraphicsPresets:

    def __init__(self):
        sect = ResMgr.openSection(graphicsPresetsResource)
        self.entries = {}
        self.entryNames = []
        self.selectedOption = -1
        for group in sect.values():
            if group.asString != b'':
                entry = {}
                for setting in group.values():
                    if setting.name == b'entry':
                        entry[setting.readString(b'label')] = setting.readInt(b'activeOption')

                self.entries[group.asString] = entry
                self.entryNames.append(group.asString)

        self.setSelectedOption()
        return

    def setSelectedOption(self):
        self.selectedOption = -1
        currentOptionMap = {}
        for currentOption in BigWorld.graphicsSettings():
            currentOptionMap[currentOption[0]] = currentOption[1]

        for i, entryName in enumerate(self.entryNames):
            foundOption = True
            for setting in self.entries[entryName].items():
                if currentOptionMap.get(setting[0]) != setting[1]:
                    foundOption = False
                    break

            if foundOption:
                self.selectedOption = i
                break

        return

    def selectGraphicsOptions(self, option):
        currentOption = self.entries[self.entryNames[option]]
        for setting in currentOption.items():
            try:
                BigWorld.setGraphicsSetting(setting[0], setting[1])
            except:
                print(b'selectGraphicsOptions: unable to set option ', setting[0])

        self.selectedOption = option
        return
