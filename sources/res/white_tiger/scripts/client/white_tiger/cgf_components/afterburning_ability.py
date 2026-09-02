from __future__ import absolute_import
import CGF, GenericComponents
from cgf_script.registration import ComponentProperty, registerComponent, registerModule
from CustomEffectManager import CustomEffectManager

@registerComponent
class CustomEffectsModifier(object):
    value = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Value', value=0)
    key = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Key', value=b'')


class CustomEffectsModifierSystem(CGF.System):
    ModifierActivated = CGF.ActivateReaction(CGF.ReactRo(CustomEffectsModifier), CGF.ReactRo(GenericComponents.RedirectorComponent))
    ModifierDeactivated = CGF.DeactivateReaction(CGF.ReactRo(CustomEffectsModifier), CGF.Ro(GenericComponents.RedirectorComponent))
    EffectManagerAccess = CGF.AccessReaction(CGF.Rw(CustomEffectManager))
    Reactions = CGF.Reactions(ModifierDeactivated, ModifierActivated, EffectManagerAccess)

    def update(self):
        effectManagerAccess = self.reaction(self.EffectManagerAccess)
        for modifier, redirector in self.reaction(self.ModifierDeactivated):
            self.onRemoved(modifier, redirector, effectManagerAccess)

        for modifier, redirector in self.reaction(self.ModifierActivated):
            self.onAdded(modifier, redirector, effectManagerAccess)

        return

    def onAdded(self, modifier, redirector, effectManagerAccess):
        effectMgr = effectManagerAccess.find(redirector.redirectionTarget)
        if effectMgr is not None:
            effectMgr.variables[modifier.key] = modifier.value
        return

    def onRemoved(self, modifier, redirector, effectManagerAccess):
        effectMgr = effectManagerAccess.find(redirector.redirectionTarget)
        if effectMgr is not None:
            effectMgr.variables[modifier.key] = 0
        return


@registerModule
class AfterburningModule(object):
    group = b'GameLogic'
    systems = [
     CGF.RegisterSystem(CustomEffectsModifierSystem, domain=CGF.Domain.ClientEditor)]
    components = [
     CustomEffectsModifier]
