from skeletons.gui.event_boards_controllers import IEventBoardController
__all__ = (b'getEventServicesConfig',)

def getEventServicesConfig(manager):
    from gui.event_boards.event_boards_controller import EventBoardsController
    ctrl = EventBoardsController()
    manager.addInstance(IEventBoardController, ctrl, finalizer=b'fini')
    return
