from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from story_mode.cgf_components.bunkers import BunkersSystem
from BunkerLogicComponent import BunkerLogicComponent

@registerModule
class ClientStoryModeModule(object):
    name = b'Client Story Mode Module'
    desc = b'Client Story Mode Functionalities'
    group = b'Store Mode'
    systems = [
     CGF.RegisterSystem(BunkersSystem, domain=CGF.Domain.Client, updateAfter=(
      CGF.TransformUpdateSystem,))]
    components = [
     BunkerLogicComponent]
