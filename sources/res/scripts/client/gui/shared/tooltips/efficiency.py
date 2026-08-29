from gui import makeHtmlString
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.tooltips import formatters
from helpers.i18n import makeString as ms
from gui.shared.formatters import text_styles

def makeHtmlText(pattern, text):
    return makeHtmlString(b'html_templates:lobby/battle_results', pattern, {b'text': text})


class HeaderItemPacker(object):

    def __init__(self, headerTitle, icon):
        super(HeaderItemPacker, self).__init__()
        self.__headerTitle = headerTitle
        self.__icon = icon
        return

    def pack(self, data):
        titleStr = text_styles.highTitle(self.__headerTitle)
        return [
         formatters.packImageTextBlockData(titleStr, img=self.__icon, txtPadding={b'left': 18, b'top': 9, b'bottom': 1}, padding={b'left': 2, b'top': 7})]


class TermsItemPacker(HeaderItemPacker):

    def __init__(self, headerTitle, icon, termsAlias):
        super(TermsItemPacker, self).__init__(headerTitle, icon)
        self._termsAlias = termsAlias
        return

    def pack(self, data):
        items = super(TermsItemPacker, self).pack(data)
        items.append(formatters.packBuildUpBlockData(self._packTerms(data)))
        return items

    def _packTerms(self, data):
        text = makeHtmlText(b'tooltip_terms_label', ms(self._termsAlias))
        return [formatters.packTextBlockData(text)]


class KillItemPacker(TermsItemPacker):

    def __init__(self):
        super(KillItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_KILL_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_DESTRUCTION, BATTLE_RESULTS.COMMON_TOOLTIP_KILL_1_DESCRIPTION)
        return

    def pack(self, data):
        items = super(KillItemPacker, self).pack(data)
        reason = data.get(b'killReason', None)
        if reason is not None and reason >= 0:
            rKill = R.strings.battle_results.common.tooltip.dyn((b'kill{}').format(reason))
            if rKill:
                text = makeHtmlText(b'tooltip_add_info_label', backport.text(rKill.description()))
                items.append(formatters.packTextBlockData(text))
        return items

    def _packTerms(self, data):
        text = makeHtmlText(b'tooltip_terms_label', ms(self._termsAlias))
        return [formatters.packTextBlockData(text)]


class DetectionItemPacker(TermsItemPacker):

    def __init__(self):
        super(DetectionItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_SPOTTED_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_DETECTION, BATTLE_RESULTS.COMMON_TOOLTIP_SPOTTED_DESCRIPTION)
        return


class LinerItemPacker(TermsItemPacker):

    def pack(self, data):
        items = super(LinerItemPacker, self).pack(data)
        values = data.get(b'values', None)
        discript = data.get(b'discript', None)
        if values is not None and discript is not None:
            packer = formatters.packTextParameterBlockData
            blocks = [packer(value=values[i], name=discript[i]) for i in range(0, len(values))]
            blockToInsert = formatters.packBuildUpBlockData(blocks)
            items.append(blockToInsert)
        return items


class DamageItemPacker(LinerItemPacker):

    def __init__(self):
        super(DamageItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_DAMAGE_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_DAMAGE, BATTLE_RESULTS.COMMON_TOOLTIP_DAMAGE_DESCRIPTION)
        return


class ArmorItemPacker(LinerItemPacker):

    def __init__(self):
        super(ArmorItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_ARMOR_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_ARMOR, BATTLE_RESULTS.COMMON_TOOLTIP_ARMOR_DESCRIPTION)
        return


class StunItemPacker(LinerItemPacker):

    def __init__(self):
        super(StunItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_STUN_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_STUN, BATTLE_RESULTS.COMMON_TOOLTIP_STUN_DESCRIPTION)
        return


class AssistItemPacker(LinerItemPacker):

    def __init__(self):
        super(AssistItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_ASSIST_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_HELP, BATTLE_RESULTS.COMMON_TOOLTIP_ASSIST_DESCRIPTION)
        return


class CaptureItemPacker(LinerItemPacker):

    def __init__(self):
        super(CaptureItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_CAPTURE_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_CAPTURE, BATTLE_RESULTS.COMMON_TOOLTIP_CAPTURE_DESCRIPTION)
        return


class DefenceItemPacker(LinerItemPacker):

    def __init__(self):
        super(DefenceItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_DEFENCE_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_DEFENCE, BATTLE_RESULTS.COMMON_TOOLTIP_DEFENCE_DESCRIPTION)
        return


class CritsItemPacker(TermsItemPacker):

    def __init__(self):
        super(CritsItemPacker, self).__init__(BATTLE_RESULTS.COMMON_TOOLTIP_CRITS_HEADER, RES_ICONS.MAPS_ICONS_LIBRARY_EFFICIENCY_48X48_MODULE, BATTLE_RESULTS.COMMON_TOOLTIP_CRITS_DESCRIPTION)
        return

    def pack(self, data):
        items = super(CritsItemPacker, self).pack(data)
        critDamage = data.get(b'critDamage', None)
        critWound = data.get(b'critWound', None)
        critDestruction = data.get(b'critDestruction', None)
        if critDamage:
            self.__addResultBlock(items, BATTLE_RESULTS.COMMON_TOOLTIP_CRITS_CRITDAMAGE, critDamage)
        if critDestruction:
            self.__addResultBlock(items, BATTLE_RESULTS.COMMON_TOOLTIP_CRITS_CRITDESTRUCTION, critDestruction)
        if critWound:
            self.__addResultBlock(items, BATTLE_RESULTS.COMMON_TOOLTIP_CRITS_CRITWOUND, critWound)
        if data[b'isGarage']:
            text = makeHtmlText(b'tooltip_add_info_label', ms(BATTLE_RESULTS.GARAGE_UNIQUEDAMAGE))
            items.append(formatters.packTextBlockData(text))
        return items

    def __addResultBlock(self, items, title, text):
        htmlTitle = makeHtmlText(b'tooltip_block_title_label', ms(title))
        items.append(formatters.packResultBlockData(htmlTitle, text))
        return
