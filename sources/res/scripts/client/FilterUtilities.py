from __future__ import absolute_import
import BigWorld

def enableVisualiseAvatarFilter(entity):
    if hasattr(entity.filter, b'debugMatrixes') and callable(entity.filter.debugMatrixes):
        disableVisualiseAvatarFilter(entity)
        entity._filterCubeModels = []
        for matrixProvider in entity.filter.debugMatrixes():
            cubeModel = BigWorld.Model(b'helpers/models/unit_cube.model')
            servo = BigWorld.Servo(matrixProvider)
            cubeModel.addMotor(servo)
            entity.addModel(cubeModel)
            entity._filterCubeModels.append(cubeModel)

    return


def disableVisualiseAvatarFilter(entity):
    if hasattr(entity, b'_filterCubeModels'):
        for cube in entity._filterCubeModels:
            entity.delModel(cube)

        del entity._filterCubeModels
    return


def enableVisualiseAllAvatarFilters():
    for entity in BigWorld.entities.values():
        enableVisualiseAvatarFilter(entity)

    return


def disableVisualiseAllAvatarFilters():
    for entity in BigWorld.entities.values():
        disableVisualiseAvatarFilter(entity)

    return
