class ICarouselEventEntry(object):

    @staticmethod
    def getIsActive(state):
        raise NotImplementedError
        return


class IBattleModifiersEntry(object):

    @classmethod
    def getIsActive(cls):
        raise NotImplementedError
        return
