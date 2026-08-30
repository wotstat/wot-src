from __future__ import absolute_import
from collections import defaultdict
from future.utils import viewvalues
from past.builtins import xrange
import BigWorld, GUI
from Math import Vector3, Matrix
import math_utils
from helpers.CallbackDelayer import CallbackDelayer

class DebugDrawEntity(BigWorld.Entity):
    BOX_MODEL = b'helpers/models/unit_cube.model'
    SPHERE_MODEL = b'helpers/models/unit_sphere.model'

    def __init__(self):
        super(DebugDrawEntity, self).__init__()
        self.objectStates = defaultdict((lambda : {b'version': 0, b'models': [], b'3Dtexts': []}))
        self.reuseModels = defaultdict(list)
        self.reuse3DTexts = []
        self.timer = CallbackDelayer()
        return

    def set_drawObjects(self, prev):
        self.__update()
        return

    def onEnterWorld(self, prereqs):
        self.__update()
        return

    def onLeaveWorld(self):
        for state in viewvalues(self.objectStates):
            for _, model, _ in state[b'models']:
                BigWorld.delModel(model)

            for model, _, _ in state[b'3Dtexts']:
                BigWorld.delModel(model)

        for listOfModels in viewvalues(self.reuseModels):
            for model, _ in listOfModels:
                BigWorld.delModel(model)

        for model, _, _ in self.reuse3DTexts:
            BigWorld.delModel(model)

        self.timer.destroy()
        self.timer = None
        return

    def __update(self):
        objectsToUpdate = []
        objectsPresent = []
        for drawObject in self.drawObjects:
            name = drawObject[b'name']
            objectsPresent.append(name)
            state = self.objectStates[name]
            if state[b'version'] != drawObject[b'version']:
                for modelName, model, motor in state[b'models']:
                    self.reuseModels[modelName].append((model, motor))

                for textObj in state[b'3Dtexts']:
                    self.reuse3DTexts.append(textObj)

                state[b'models'][:] = []
                state[b'3Dtexts'][:] = []
                state[b'version'] = drawObject[b'version']
                objectsToUpdate.append((state, drawObject))

        for key in self.objectStates.keys():
            if key not in objectsPresent:
                state = self.objectStates.pop(key)
                for modelName, model, motor in state[b'models']:
                    self.reuseModels[modelName].append((model, motor))

                for textObj in state[b'3Dtexts']:
                    self.reuse3DTexts.append(textObj)

        for state, draw in objectsToUpdate:
            for line in draw[b'lines']:
                points = line[b'points']
                width = line[b'width']
                for segment in [(points[i - 1], points[i]) for i in xrange(1, len(points))]:
                    obj = self.__createDirectedLine(segment[0], segment[1], width)
                    state[b'models'].append(obj)

                for point in points[1:-1]:
                    obj = self.__createSphere(point, (width * 1.25,) * 3)
                    state[b'models'].append(obj)

            for box in draw[b'boxes']:
                obj = self.__createBox(box[b'position'], box[b'rotation'], box[b'size'])
                state[b'models'].append(obj)

            for sphere in draw[b'spheres']:
                obj = self.__createSphere(sphere[b'position'], sphere[b'radius'])
                state[b'models'].append(obj)

            for text in draw[b'texts']:
                obj = self.__create3DText(text[b'position'], text[b'text'], text[b'color'], text[b'textSize'])
                state[b'3Dtexts'].append(obj)

        for listOfModels in viewvalues(self.reuseModels):
            for model, _ in listOfModels:
                BigWorld.delModel(model)

        for model, _, _ in self.reuse3DTexts:
            BigWorld.delModel(model)

        self.reuseModels.clear()
        self.reuse3DTexts[:] = []
        return

    def __createDirectedLine(self, pointA, pointB, width):
        modelName = self.BOX_MODEL
        model, motor = self.__getModel(modelName)
        direction = pointB - pointA
        scale = (width, width, direction.length)
        rotation = (direction.yaw, direction.pitch, 0)
        translation = pointA + direction * 0.5
        m = math_utils.createSRTMatrix(scale, rotation, translation)
        m.preMultiply(math_utils.createTranslationMatrix(Vector3(0.0, -0.5, 0.0)))
        motor.signal = m
        return (modelName, model, motor)

    def __createBox(self, position, rotation, size):
        modelName = self.BOX_MODEL
        model, motor = self.__getModel(modelName)
        m = math_utils.createSRTMatrix(size, rotation, position)
        m.preMultiply(math_utils.createTranslationMatrix(Vector3(0.0, -0.5, 0.0)))
        motor.signal = m
        return (modelName, model, motor)

    def __createSphere(self, position, radius):
        modelName = self.SPHERE_MODEL
        model, motor = self.__getModel(modelName)
        motor.signal = math_utils.createSRTMatrix(radius, (0, 0, 0), position)
        return (modelName, model, motor)

    def __getModel(self, modelName):
        if self.reuseModels[modelName]:
            model, motor = self.reuseModels[modelName].pop()
        else:
            model = BigWorld.Model(modelName)
            motor = BigWorld.Servo(Matrix())
            model.addMotor(motor)
            BigWorld.addModel(model, self.spaceID)
        return (
         model, motor)

    def __create3DText(self, position, text, color, textSize):
        if self.reuse3DTexts:
            model, motor, component = self.reuse3DTexts.pop()
        else:
            attachment = GUI.Attachment()
            component = GUI.Text(text)
            attachment.component = component
            attachment.faceCamera = True
            motor = BigWorld.Servo(math_utils.createTranslationMatrix(position))
            model = BigWorld.Model(b'')
            model.addMotor(motor)
            BigWorld.addModel(model, self.spaceID)
            model.root.attach(attachment)
            component.visible = True
            component.multiline = True
            component.explicitSize = True
            component.filterType = GUI.Simple.eFilterType.LINEAR
            component.verticalAnchor = GUI.Simple.eVAnchor.BOTTOM
        component.text = text
        component.size = (0, textSize)
        component.colour = color
        motor.signal = math_utils.createTranslationMatrix(position)
        return (
         model, motor, component)
