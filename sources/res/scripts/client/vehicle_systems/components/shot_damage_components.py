from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery
import CGF, Math, BigWorld, GenericComponents
from items import vehicles
from vehicle_systems.tankStructure import TankPartNames

class ShotDamageComponent(object):

    def __init__(self, partName, compound, collisionComponent):
        self.partName = partName
        self.compound = compound
        self.collisionComponent = collisionComponent
        return


@registerComponent
class DamageStickerComponent(object):
    category = b'Render'
    domain = CGF.DomainOption.DomainClient
    damageSticker = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Damage sticker', value=b'')
    lodDistance = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Lod Distance', value=100)
    fadeoutTime = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Fadeout time', value=0)
    offset = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Offset', value=1.0)

    def __init__(self):
        super(DamageStickerComponent, self).__init__()
        self.stickerModel = None
        return


@autoregister(presentInAllWorlds=True)
class DamageStickerManager(CGF.ComponentManager):

    @onAddedQuery(ShotDamageComponent, DamageStickerComponent, GenericComponents.TransformComponent)
    def onAddedSticker(self, shotDamage, damageSticker, transform):
        if shotDamage.partName == TankPartNames.CHASSIS:
            return
        damageSticker.stickerModel = BigWorld.StickerModel(self.spaceID)
        idx = TankPartNames.getIdx(shotDamage.partName)
        geometryLink = shotDamage.compound.getPartGeometryLink(idx)
        m = Math.Matrix()
        m.setIdentity()
        stickerModel = damageSticker.stickerModel
        stickerModel.setupSuperModel(geometryLink, m)
        node = shotDamage.compound.node(shotDamage.partName)
        node.attach(damageSticker.stickerModel)
        stickerModel.setLODDistance(damageSticker.lodDistance)
        stickerId = vehicles.g_cache.damageStickers[b'ids'][damageSticker.damageSticker]
        segStart = transform.transform.applyPoint(Math.Vector3(0, 0, -damageSticker.offset))
        segEnd = transform.transform.applyPoint(Math.Vector3(0, 0, damageSticker.offset))
        stickerModel.addDamageSticker(stickerId, segStart, segEnd, idx, shotDamage.collisionComponent, True)
        stickerModel.setupFadeout(damageSticker.fadeoutTime)
        return

    @onRemovedQuery(ShotDamageComponent, DamageStickerComponent)
    def onRemovedSticker(self, shotDamage, damageSticker):
        if damageSticker.stickerModel is None:
            return
        else:
            node = shotDamage.compound.node(shotDamage.partName)
            node.detach(damageSticker.stickerModel)
            return
