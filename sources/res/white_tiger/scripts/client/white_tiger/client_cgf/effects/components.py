import CGF, GenericComponents
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class WTAnimatorLinkComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'
    linkToAnimator = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Link to Animator', value=GenericComponents.AnimatorComponent)


@registerComponent
class WTAnomalyDisappearComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'
    prefab = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'prefab', value=b'', annotations={b'path': b'*.prefab'})


@registerComponent
class WTAnomalyBinocularComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'
    binocularsEffects = ComponentProperty(type=CGFMetaTypes.STRING_LIST, editorName=b'binoculars effects')
