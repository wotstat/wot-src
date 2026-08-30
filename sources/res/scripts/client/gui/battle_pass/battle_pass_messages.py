from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from messenger import g_settings
from battle_pass_common import isBattlePassPassToken

def getBattlePassBuyShopFormattedMsg(data):
    _template = b'battlePassBuyShopInvoiceReceived'
    tags = data.get(b'tags', ())
    if b'battlePassBuyChapter' in tags:
        chaptersNames = []
        dataEx = data.get(b'data', {})
        for tokenName in dataEx.get(b'tokens', {}).iterkeys():
            if isBattlePassPassToken(tokenName):
                chapterID = int(tokenName.split(b':')[-1])
                chaptersNames.append(text_styles.credits(backport.text(R.strings.battle_pass.chapter.fullName.quoted.num(chapterID)())))

        if chaptersNames:
            chapterInBundle = b'several' if len(chaptersNames) > 1 else b'single'
            return (
             _template,
             g_settings.msgTemplates.format(_template, ctx={b'header': (backport.text(R.strings.battle_pass.ingameShop.notification.title())), 
                b'description': (backport.text(R.strings.battle_pass.ingameShop.notification.dyn(chapterInBundle).description(), chapter=(b', ').join(chaptersNames)))}))
    return (None, None)
