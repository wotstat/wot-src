from serialization import parseCompDescr
from serialization.serializable_component import SerializableComponentChildType
from .attachment import AttachmentComponent
from .camouflage import CamouflageComponent
from .customization_outfit import CustomizationOutfit, getAllItemsFromOutfit
from .decal import DecalComponent
from .insignia import InsigniaComponent
from .paint import PaintComponent
from .personal_number import PersonalNumberComponent
from .projection_decal import ProjectionDecalComponent
from .sequence import SequenceComponent
__all__ = (b'AttachmentComponent', b'CamouflageComponent', b'CustomizationOutfit', b'getAllItemsFromOutfit', b'DecalComponent', b'InsigniaComponent', b'PaintComponent', b'PersonalNumberComponent', b'ProjectionDecalComponent', b'SequenceComponent', b'CUSTOMIZATION_CLASSES', b'parseC11sComponentDescr')
CUSTOMIZATION_CLASS_LIST = [
 AttachmentComponent, 
 CamouflageComponent, 
 CustomizationOutfit, 
 DecalComponent, 
 InsigniaComponent, 
 PaintComponent, 
 PersonalNumberComponent, 
 ProjectionDecalComponent, 
 SequenceComponent]
CUSTOMIZATION_CLASSES = {subClass.customType: subClass for subClass in CUSTOMIZATION_CLASS_LIST}

def parseC11sComponentDescr(customizationElementCompDescr):
    return parseCompDescr(CUSTOMIZATION_CLASSES, customizationElementCompDescr)
