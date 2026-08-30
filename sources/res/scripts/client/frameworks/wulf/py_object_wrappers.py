from constants import IS_EDITOR, IS_WEB
if not (IS_EDITOR or IS_WEB):
    import _wulf as _py_objects
else:
    import wulf_wrapper as _py_objects
PyObjectArray = _py_objects.PyObjectArray
PyObjectCommand = _py_objects.PyObjectCommand
PyGuiApplication = _py_objects.PyGuiApplication
ResourceDescriptor = _py_objects.PyResourceDescriptor
PyObjectViewSettings = _py_objects.PyObjectViewSettings
PyObjectView = _py_objects.PyObjectView
PyObjectViewModel = _py_objects.PyObjectViewModel
PyObjectWindowSettings = _py_objects.PyObjectWindowSettings
PyObjectWindow = _py_objects.PyObjectWindow
PyObjectWindowsArea = _py_objects.PyObjectWindowsArea
isTranslatedKeyValid = _py_objects.isTranslatedKeyValid
isTranslatedTextExisted = _py_objects.isTranslatedTextExisted
getTranslatedText = _py_objects.getTranslatedText
getTranslatedPluralText = _py_objects.getTranslatedPluralText
getImagePath = _py_objects.getImagePath
getSoundEffectId = _py_objects.getSoundEffectId
getLayoutPath = _py_objects.getLayoutPath
getTranslatedTextByResId = _py_objects.getTranslatedTextByResId
getTranslatedPluralTextByResId = _py_objects.getTranslatedPluralTextByResId
getTranslatedKey = _py_objects.getTranslatedKey
getNumberFormat = _py_objects.getNumberFormat
getRealFormat = _py_objects.getRealFormat
getTimeFormat = _py_objects.getTimeFormat
getDateFormat = _py_objects.getDateFormat
caseMap = _py_objects.caseMap
ResourceType = _py_objects.PyResourceType
__all__ = (b'PyObjectArray', b'PyObjectCommand', b'PyGuiApplication', b'ResourceDescriptor', b'PyObjectViewSettings', b'PyObjectView', b'PyObjectViewModel', b'PyObjectWindowSettings', b'PyObjectWindow', b'PyObjectWindowsArea', b'isTranslatedKeyValid', b'isTranslatedTextExisted', b'getTranslatedText', b'getTranslatedPluralText', b'getImagePath', b'getSoundEffectId', b'getLayoutPath', b'getTranslatedTextByResId', b'getTranslatedPluralTextByResId', b'getTranslatedKey', b'getNumberFormat', b'getRealFormat', b'getTimeFormat', b'getDateFormat', b'caseMap', b'ResourceType')
