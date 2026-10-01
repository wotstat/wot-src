import CGF, logging
from portal_constants import PORTAL_GUI_MARKERS_2D, PORTAL_GUI_MARKERS_MINIMAP
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
_logger = logging.getLogger(__name__)

@registerComponent
class PortalAreaMarker(object):
    category = b'Portal'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'Portal Area Marker'
    stateID = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'state ID', value=-1)
    cullDistance = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Distance in which marker will be visible', value=500)
    hasProgressBar = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'Has progress bar', value=False)
    hasTimerBoard = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'Has timer board', value=False)
    marker2DEntryID = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'marker2DEntryID', value=b'No marker', annotations={b'comboBox': {b'Portal HP marker': (PORTAL_GUI_MARKERS_2D.BOSS_HP_MARKER), 
                     b'Portal marker': (PORTAL_GUI_MARKERS_2D.PORTAL_MARKER), 
                     b'Trap marker': (PORTAL_GUI_MARKERS_2D.TRAP_MARKER), 
                     b'No marker': (PORTAL_GUI_MARKERS_2D.NO_MARKER)}})
    markerMinimapEntryID = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'markerMinimapEntryID', value=b'No marker', annotations={b'comboBox': {b'Portal marker': (PORTAL_GUI_MARKERS_MINIMAP.PORTAL_MINIMAP_ENTRY), 
                     b'Trap marker': (PORTAL_GUI_MARKERS_MINIMAP.TRAP_MINIMAP_ENTRY), 
                     b'Minefield marker': (PORTAL_GUI_MARKERS_MINIMAP.MINEFIELD_MINIMAP_ENTRY), 
                     b'Frontier Observer Active': (PORTAL_GUI_MARKERS_MINIMAP.FRONTIER_OBSERVER_ACTIVE), 
                     b'Frontier Observer Inactive': (PORTAL_GUI_MARKERS_MINIMAP.FRONTIER_OBSERVER_INACTIVE), 
                     b'No marker': (PORTAL_GUI_MARKERS_MINIMAP.NO_MARKER)}})

    def __init__(self):
        self.id = None
        return
