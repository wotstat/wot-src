import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from gui.pet_system.constants import StorageStateKey

@registerComponent
class StorageStateComponent(object):
    group = b'Pet system'
    editorTitle = b'Pet Storage State Component'
    domain = CGF.Domain.Client
    names = {name: name for name in StorageStateKey.ALL}
    storageObjectKey = ComponentProperty(type=CGF.PropertyType.String, editorName=b'storage object key', value=b'active', annotations={b'comboBox': names})
