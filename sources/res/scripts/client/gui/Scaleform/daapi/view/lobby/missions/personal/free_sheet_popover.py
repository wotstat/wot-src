import operator
from gui.Scaleform.daapi.view.meta.FreeSheetPopoverMeta import FreeSheetPopoverMeta
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.server_events import events_dispatcher
from gui.server_events.events_helpers import AwardSheetPresenter
from gui.shared.formatters import text_styles
from helpers import dependency
from helpers.i18n import makeString as _ms
from personal_missions import PM_BRANCH
from skeletons.gui.server_events import IEventsCache

class FreeSheetPopover(FreeSheetPopoverMeta):
    __eventsCache = dependency.descriptor(IEventsCache)
    __ANIMATION_DELAY = 200

    def __init__(self, ctx=None):
        super(FreeSheetPopover, self).__init__(ctx)
        self.__playAnimation = False
        self.__branch = PM_BRANCH.REGULAR
        if ctx is not None:
            ctxData = ctx.get(b'data')
            if ctxData is not None:
                self.__playAnimation = ctxData.showAnimation
                if ctxData.passedData and ctxData.passedData.children:
                    self.__branch = ctxData.passedData.children.get(b'branch', PM_BRANCH.REGULAR)
        return

    def onTaskClick(self, questID):
        events_dispatcher.showPersonalMission(int(questID))
        self.destroy()
        return

    def _populate(self):
        super(FreeSheetPopover, self)._populate()
        self.__eventsCache.onSyncCompleted += self.__update
        self.__update()
        return

    def _dispose(self):
        self.__eventsCache.onSyncCompleted -= self.__update
        super(FreeSheetPopover, self)._dispose()
        return

    def __update(self):
        freeSheetsQuests = []
        pawnedSheets = 0
        for _, o in sorted(self.__eventsCache.getPersonalMissions().getOperationsForBranch(self.__branch).iteritems(), key=operator.itemgetter(0)):
            if o.isUnlocked():
                operationName = _ms(PERSONAL_MISSIONS.OPERATIONTITLE_TITLE, title=o.getShortUserName())
                idx = 1
                for classifier in o.getIterationChain():
                    _, quests = o.getChainByClassifierAttr(classifier)
                    for quest in sorted(quests.itervalues(), key=(lambda q: q.getID())):
                        if quest.areTokensPawned():
                            freeSheetsQuests.append({b'taskId': (str(quest.getID())), 
                               b'taskText': (text_styles.standard(operationName)), 
                               b'descrText': (text_styles.main(quest.getUserName())), 
                               b'animDelay': (self.__ANIMATION_DELAY * idx if self.__playAnimation else -1)})
                            idx += 1
                            pawnedSheets += quest.getPawnCost()

        freeSheets = self.__eventsCache.getPersonalMissions().getFreeTokensCount(self.__branch)
        if pawnedSheets == 0:
            pawnedSheetsDescrText = PERSONAL_MISSIONS.FREESHEETPOPOVER_PAWNEDSHEETSINFO_DESCR_NOONE
        else:
            pawnedSheetsDescrText = PERSONAL_MISSIONS.FREESHEETPOPOVER_PAWNEDSHEETSINFO_DESCR
        self.as_setDataS({b'titleText': (text_styles.highTitle(PERSONAL_MISSIONS.FREESHEETPOPOVER_TITLE)), 
           b'freeSheetsInfo': {b'imgSource': (AwardSheetPresenter.getIcon(AwardSheetPresenter.Size.SMALL)), 
                               b'titleText': (text_styles.middleTitle(_ms(PERSONAL_MISSIONS.FREESHEETPOPOVER_FREESHEETSINFO_TITLE, count=freeSheets))), 
                               b'descrText': (text_styles.standard(PERSONAL_MISSIONS.FREESHEETPOPOVER_FREESHEETSINFO_DESCR))}, 
           b'pawnedSheetsInfo': {b'imgSource': (AwardSheetPresenter.getPawnedIcon()), 
                                 b'titleText': (text_styles.middleTitle(_ms(PERSONAL_MISSIONS.FREESHEETPOPOVER_PAWNEDSHEETSINFO_TITLE, count=pawnedSheets))), 
                                 b'descrText': (text_styles.standard(pawnedSheetsDescrText))}, 
           b'hasPawnedSheets': (pawnedSheets > 0)})
        if pawnedSheets > 0:
            self.as_setListDataProviderS(freeSheetsQuests)
        return
