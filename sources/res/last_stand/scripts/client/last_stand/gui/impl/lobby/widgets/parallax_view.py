from __future__ import absolute_import
import json, logging, typing, ResMgr
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from gui.shared.utils.graphics import isLowPreset
from helpers import dependency
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_view_model import ParallaxViewModel
from last_stand.skeletons.ls_controller import ILSController
from last_stand.skeletons.ls_story_point_controller import ILSStoryPointController
if typing.TYPE_CHECKING:
    from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_model import ParallaxModel
_logger = logging.getLogger(__name__)
PATH_TO_CONFIGS = b'last_stand/gui/parallax/configs.json'
PARALLAX_DEFAULT_SCALE = 1

class ParallaxView(ViewComponent[ParallaxViewModel]):
    lsCtrl = dependency.descriptor(ILSController)
    lsStoryPointCtrl = dependency.descriptor(ILSStoryPointController)

    def __init__(self):
        super(ParallaxView, self).__init__(R.aliases.last_stand.shared.Parallax(), ParallaxViewModel)
        self._parallaxConfig = _toJson(_readSection(PATH_TO_CONFIGS))
        self._currentSlideID = self.lsStoryPointCtrl.FIRST_STORY_POINT_INDEX
        return

    @property
    def viewModel(self):
        return super(ParallaxView, self).getViewModel()

    def _subscribe(self):
        super(ParallaxView, self)._subscribe()
        self.viewModel.onSlide += self.__onSlide
        return

    def _unsubscribe(self):
        self.viewModel.onSlide -= self.__onSlide
        super(ParallaxView, self)._unsubscribe()
        return

    def __onSlide(self, args):
        self._currentSlideID = int(args.get(b'slideIndex', self.lsStoryPointCtrl.FIRST_STORY_POINT_INDEX))
        self.__readParallaxConfig(self._currentSlideID)
        return

    def __readParallaxConfig(self, currentSlideID):
        with self.viewModel.transaction() as tx:
            if not self.lsCtrl.isParallaxEnabled():
                tx.setIsParallaxEnabled(False)
                _logger.info(b'last_stand_config.xml parallaxEnabled is False')
                return
            if isLowPreset():
                tx.setIsParallaxEnabled(False)
                _logger.info(b'Low graphics settings')
                return
            slideParallaxConfig = self._parallaxConfig.get(str(currentSlideID))
            if slideParallaxConfig is None:
                tx.setIsParallaxEnabled(False)
                _logger.info(b'cannot find config for %s', currentSlideID)
                return
            parallaxStructure = _readSection(slideParallaxConfig.get(b'structurePath', b''))
            if parallaxStructure == b'':
                tx.setIsParallaxEnabled(False)
                _logger.info(b'cannot find parallax structure:%s', slideParallaxConfig.get(b'structurePath'))
                return
            tx.setIsParallaxEnabled(True)
            chunks = _getChunks(slideParallaxConfig.get(b'chunksCount', 0), slideParallaxConfig.get(b'chunkName', b''), slideParallaxConfig.get(b'chunksDataDirPath', b''))
            modelParallax = tx.parallax
            modelParallax.setSlideId(currentSlideID)
            modelParallax.setPerspective(slideParallaxConfig.get(b'perspective', 0))
            modelParallax.setPerspectiveOriginX(slideParallaxConfig.get(b'perspectiveOriginX', 0))
            modelParallax.setPerspectiveOriginY(slideParallaxConfig.get(b'perspectiveOriginY', 0))
            modelParallax.setWrapperWidth(slideParallaxConfig.get(b'wrapperWidth', 0))
            modelParallax.setWrapperHeight(slideParallaxConfig.get(b'wrapperHeight', 0))
            modelParallax.setOverallScale(slideParallaxConfig.get(b'overallScale', PARALLAX_DEFAULT_SCALE))
            modelParallax.setXTilt(slideParallaxConfig.get(b'xTilt', 0.0))
            modelParallax.setXTiltRange(slideParallaxConfig.get(b'xTiltRange', 0.0))
            modelParallax.setYTilt(slideParallaxConfig.get(b'yTilt', 0.0))
            modelParallax.setYTiltRange(slideParallaxConfig.get(b'yTiltRange', 0.0))
            modelParallax.setXSlide(slideParallaxConfig.get(b'xSlide', 0.0))
            modelParallax.setYSlide(slideParallaxConfig.get(b'ySlide', 0.0))
            modelParallax.setParallaxStructure(parallaxStructure)
            modelParallax.setAtlas(chunks)
            modelParallax.setChunkFileExt(slideParallaxConfig.get(b'chunkFileExt', b''))
            modelParallax.setChunksAssetsPath(slideParallaxConfig.get(b'chunksAssetsPath', b''))
        return


def _readSection(path):
    if path == b'':
        return b''
    else:
        section = ResMgr.openSection(path)
        ResMgr.purge(path)
        if section is not None:
            return section.asString
        return b''


def _toJson(inputData):
    try:
        jsonData = json.loads(inputData)
    except Exception as e:
        _logger.error(b'%s', e)
        return

    if not jsonData:
        _logger.error(b'Empty jsonData received')
        return
    else:
        return jsonData


def _getChunks(count, name, path):
    allChunks = {}
    for i in range(count):
        chunkPath = (b'{0}{1}{2}.json').format(path, name, str(i))
        chunk = _toJson(_readSection(chunkPath))
        if chunk is not None:
            allChunks.update(chunk)
        else:
            _logger.error(b'Chunk of parallax atlas is None')

    return json.dumps(allChunks)
