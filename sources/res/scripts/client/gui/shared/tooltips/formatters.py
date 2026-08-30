from __future__ import absolute_import
from gui import makeHtmlString
from gui.Scaleform.genConsts.ACTION_PRICE_CONSTANTS import ACTION_PRICE_CONSTANTS
from gui.Scaleform.genConsts.BATTLE_RESULT_TYPES import BATTLE_RESULT_TYPES
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.ranked_battles.ranked_builders.shared_vos import buildRankTooltipVO
from gui.shared.formatters import text_styles
from gui.shared.money import MONEY_UNDEFINED
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE, ACTION_TOOLTIPS_STATE
from gui.shared.utils.functions import makeTooltip, stripColorTagDescrTags
from helpers import i18n, time_utils
from gui.impl.gen import R
from gui.impl import backport
TXT_GAP_FOR_BIG_TITLE = 2
TXT_GAP_FOR_SMALL_TITLE = 3
RENDERERS_ALIGN_LEFT = b'renderers_left'
RENDERERS_ALIGN_RIGHT = b'renderers_right'
RENDERERS_ALIGN_CENTER = b'renderers_center'

def packPadding(top=0, left=0, bottom=0, right=0):
    data = {}
    if top != 0:
        data[b'top'] = top
    if left != 0:
        data[b'left'] = left
    if bottom != 0:
        data[b'bottom'] = bottom
    if right != 0:
        data[b'right'] = right
    return data


def packBlockDataItem(linkage, data, padding=None, blockWidth=0):
    data = {b'linkage': linkage, 
       b'data': data, 
       b'blockWidth': blockWidth}
    if padding is not None:
        data[b'padding'] = padding
    return data


def packTextBlockData(text, useHtml=True, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_BLOCK_LINKAGE, padding=None, blockWidth=0):
    return packBlockDataItem(linkage, {b'text': text, b'useHtml': useHtml}, padding, blockWidth)


def packTextWithBgBlockData(text, useHtml=True, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_WITH_BG_BLOCK_LINKAGE, padding=None, bgColor=-1, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT):
    return packBlockDataItem(linkage, {b'text': text, b'useHtml': useHtml, b'bgColor': bgColor, b'align': align}, padding)


def packAlignedTextBlockData(text, align, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_BLOCK_LINKAGE, padding=None, blockWidth=0):
    return packBlockDataItem(linkage, {b'text': (makeHtmlString(b'html_templates:lobby/textStyle', b'alignText', {b'align': align, b'message': text})), 
       b'useHtml': True}, padding, blockWidth)


def packTextParameterBlockData(name, value, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_PARAMETER_BLOCK_LINKAGE, valueWidth=-1, gap=5, padding=None, highlight=False, blockWidth=0):
    data = {b'name': name, 
       b'value': value}
    if valueWidth != -1:
        data[b'valueWidth'] = valueWidth
    if gap != -1:
        data[b'gap'] = gap
    if highlight:
        data[b'highlight'] = True
    return packBlockDataItem(linkage, data, padding, blockWidth)


def packTextParameterTwoColBlockData(name, value, value2, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_PARAMETER_BLOCK_TWO_COL_LINKAGE, valueWidth=-1, value2Gap=-1, gap=5, padding=None, highlight=False, blockWidth=0):
    data = {b'name': name, 
       b'value': value, 
       b'value2': value2}
    if valueWidth != -1:
        data[b'valueWidth'] = valueWidth
    if value2Gap != -1:
        data[b'value2Gap'] = value2Gap
    if gap != -1:
        data[b'gap'] = gap
    if highlight:
        data[b'highlight'] = True
    return packBlockDataItem(linkage, data, padding, blockWidth)


def packTextParameterTwoColWithIconBlockData(leftText, rightText, icon, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_PARAMETER_BLOCK_TWO_COL_WITH_ICON_LINKAGE, valueWidth=-1, value2Gap=-1, padding=None, iconPadding=None, highlight=False, blockWidth=0):
    data = {b'name': rightText, 
       b'value': leftText, 
       b'icon': icon}
    if valueWidth != -1:
        data[b'valueWidth'] = valueWidth
    if value2Gap != -1:
        data[b'value2Gap'] = value2Gap
    if iconPadding is not None:
        data[b'iconPadding'] = iconPadding
    if highlight:
        data[b'highlight'] = True
    return packBlockDataItem(linkage, data, padding, blockWidth)


def packOptDeviceSlotBlockData(imagePath, slotState, showSlotHighlight=False, showUpArrow=False, slotAlpha=1, slotSpecs=None, deviceSpecs=None, specsGap=-26, slotSpecsOffset=-10, deviceSpecsOffset=-40, padding=None, overlayPath=None, overlayPadding=None, highlightPath=None, highlightPadding=None):
    data = {b'imagePath': imagePath, 
       b'slotState': slotState, 
       b'showSlotHighlight': (bool(showSlotHighlight)), 
       b'showUpArrow': showUpArrow, 
       b'slotAlpha': slotAlpha, 
       b'specsGap': specsGap, 
       b'slotSpecsOffset': slotSpecsOffset, 
       b'deviceSpecsOffset': deviceSpecsOffset}
    if slotSpecs:
        data[b'slotSpecs'] = slotSpecs
    if deviceSpecs:
        data[b'deviceSpecs'] = deviceSpecs
    if overlayPath is not None:
        data[b'overlayPath'] = overlayPath
        if overlayPadding is not None:
            data[b'overlayPadding'] = overlayPadding
    if highlightPath is not None:
        data[b'highlightPath'] = highlightPath
        if highlightPadding is not None:
            data[b'highlightPadding'] = highlightPadding
    return packBlockDataItem(BLOCKS_TOOLTIP_TYPES.TOOLTIP_OPT_DEVICE_SLOT_BLOCK, data, padding)


def packAbilityBattleRankedItemBlockData(title, items, padding=None, blockWidth=0):
    data = {b'abilityName': title, 
       b'items': items}
    return packBlockDataItem(BLOCKS_TOOLTIP_TYPES.TOOLTIP_ABILITY_BATTLE_RANK_ITEM_BLOCK, data, padding, blockWidth)


def packAbilityBattleRanksBlockData(padding=None, blockWidth=0):
    return packBlockDataItem(BLOCKS_TOOLTIP_TYPES.TOOLTIP_ABILITY_BATTLE_RANK_BLOCK, {b'highlight': False}, padding, blockWidth)


def packTextParameterWithIconBlockData(name, value, icon, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_PARAMETER_WITH_ICON_BLOCK_LINKAGE, valueWidth=-1, gap=5, nameOffset=-1, padding=None, iconYOffset=None):
    data = {b'name': name, 
       b'value': value, 
       b'icon': icon}
    if valueWidth != -1:
        data[b'valueWidth'] = valueWidth
    if gap != -1:
        data[b'gap'] = gap
    if nameOffset != -1:
        data[b'nameOffset'] = nameOffset
    if iconYOffset is not None:
        data[b'iconYOffset'] = iconYOffset
    return packBlockDataItem(linkage, data, padding)


def packTitleDescParameterWithIconBlockData(title, value=b'', icon=None, desc=None, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TITLE_DESC_PARAMETER_WITH_ICON_BLOCK_LINKAGE, valueAtRight=False, valueWidth=-1, titleWidth=-1, gap=5, titlePadding=None, valuePadding=None, iconPadding=None, padding=None, iconAlpha=1):
    data = {b'name': title, 
       b'value': value, 
       b'valueAtRight': valueAtRight, 
       b'iconAlpha': iconAlpha, 
       b'gap': gap}
    if icon is not None:
        data[b'icon'] = icon
    if valueWidth != -1:
        data[b'valueWidth'] = valueWidth
    if titleWidth != -1:
        data[b'titleWidth'] = titleWidth
    if titlePadding is not None:
        data[b'titlePadding'] = titlePadding
    if valuePadding is not None:
        data[b'valuePadding'] = valuePadding
    if iconPadding is not None:
        data[b'iconPadding'] = iconPadding
    if gap != -1:
        data[b'gap'] = gap
    if desc is not None:
        blocks = [packBlockDataItem(linkage, data), packTextBlockData(desc)]
        return packBuildUpBlockData(blocks, gap, BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_LINKAGE, padding)
    else:
        return packBlockDataItem(linkage, data, padding)


def packDashLineItemPriceBlockData(title, value, icon, desc=None, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_DASHLINE_ITEM_PRICE_BLOCK_LINKAGE, padding=None):
    data = {b'name': title, 
       b'value': value, 
       b'icon': icon, 
       b'gap': (-1), 
       b'valueWidth': (-1)}
    return packBlockDataItem(linkage, data, padding)


def packBuildUpBlockData(blocks, gap=0, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_LINKAGE, padding=None, stretchBg=True, layout=BLOCKS_TOOLTIP_TYPES.LAYOUT_VERTICAL, blockWidth=0, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, stretchLast=False):
    data = {b'blocksData': blocks, 
       b'stretchBg': stretchBg, 
       b'layout': layout, 
       b'align': align, 
       b'stretchLast': stretchLast}
    if gap != 0:
        data[b'gap'] = gap
    return packBlockDataItem(linkage, data, padding, blockWidth)


def packTitleDescBlock(title, desc=None, gap=TXT_GAP_FOR_BIG_TITLE, useHtml=True, textBlockLinkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_BLOCK_LINKAGE, blocksLinkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_LINKAGE, padding=None, descPadding=None):
    blocks = [
     packTextBlockData(title, useHtml, textBlockLinkage)]
    if desc is not None:
        blocks.append(packTextBlockData(stripColorTagDescrTags(desc), useHtml, textBlockLinkage, descPadding))
    return packBuildUpBlockData(blocks, gap, blocksLinkage, padding)


def packTitleDescBlockSmallTitle(title, desc=None, useHtml=True, textBlockLinkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_BLOCK_LINKAGE, blocksLinkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_LINKAGE, padding=None):
    return packTitleDescBlock(title, desc, TXT_GAP_FOR_SMALL_TITLE, useHtml, textBlockLinkage, blocksLinkage, padding)


def packResultBlockData(title, text):
    return packBuildUpBlockData([
     packTextBlockData(title, True, BATTLE_RESULT_TYPES.TOOLTIP_RESULT_TTILE_LEFT_LINKAGE),
     packTextBlockData(text, True, BATTLE_RESULT_TYPES.TOOLTIP_ICON_TEXT_PARAMETER_LINKAGE)])


def packImageTextBlockData(title=None, desc=None, img=None, imgPadding=None, imgAtLeft=True, txtPadding=None, txtGap=0, txtOffset=-1, txtAlign=b'left', ignoreImageSize=False, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_IMAGETEXT_BLOCK_LINKAGE, padding=None, descPadding=None, descLeading=0, flipHorizontal=False, titleAtMiddle=False, blockWidth=0, snapImage=False):
    data = {b'spriteAtLeft': imgAtLeft, 
       b'snapImage': snapImage, 
       b'textsAlign': txtAlign, 
       b'ignoreImageSize': ignoreImageSize, 
       b'titleAtMiddle': titleAtMiddle}
    if title is not None:
        data[b'title'] = title
    if desc is not None:
        data[b'description'] = desc
    if img is not None:
        data[b'imagePath'] = img
    if imgPadding is not None:
        data[b'spritePadding'] = imgPadding
    if txtPadding is not None:
        data[b'textsPadding'] = txtPadding
    if txtGap != 0:
        data[b'textsGap'] = txtGap
    if txtOffset != 0:
        data[b'textsOffset'] = txtOffset
    if descPadding is not None:
        data[b'descPadding'] = descPadding
    if descLeading != 0:
        data[b'descLeading'] = descLeading
    if flipHorizontal:
        data[b'flipHorizontal'] = flipHorizontal
    return packBlockDataItem(linkage, data, padding, blockWidth)


def packItemTitleDescBlockData(title=None, desc=None, img=None, imgPadding=None, imgAtLeft=True, txtPadding=None, txtGap=0, txtOffset=-1, txtAlign=b'left', linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_ITEM_TITLE_DESC_BLOCK_LANKAGE, padding=None, overlayPath=None, overlayPadding=None, highlightPath=None, highlightPadding=None, descPadding=None):
    data = {b'spriteAtLeft': imgAtLeft, 
       b'textsAlign': txtAlign}
    if title is not None:
        data[b'title'] = title
    if desc is not None:
        data[b'description'] = desc
    if img is not None:
        data[b'imagePath'] = img
    if imgPadding is not None:
        data[b'spritePadding'] = imgPadding
    if txtPadding is not None:
        data[b'textsPadding'] = txtPadding
    if txtGap != 0:
        data[b'textsGap'] = txtGap
    if txtOffset != 0:
        data[b'textsOffset'] = txtOffset
    if descPadding is not None:
        data[b'descPadding'] = descPadding
    if overlayPath is not None:
        data[b'overlayPath'] = overlayPath
        if overlayPadding is not None:
            data[b'overlayPadding'] = overlayPadding
    if highlightPath is not None:
        data[b'highlightPath'] = highlightPath
        if highlightPadding is not None:
            data[b'highlightPadding'] = highlightPadding
    return packBlockDataItem(linkage, data, padding)


def packAtlasIconTextBlockData(title=None, desc=None, atlas=None, icon=None, iconPadding=None, iconAtLeft=True, txtPadding=None, txtGap=0, txtOffset=-1, txtAlign=b'left', ignoreIconSize=False, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_ATLASICON_TEXT_BLOCK_LINKAGE, padding=None, descPadding=None, descLeading=0, titleAtMiddle=False, blockWidth=0, snapIcon=False):
    data = {b'spriteAtLeft': iconAtLeft, 
       b'snapImage': snapIcon, 
       b'textsAlign': txtAlign, 
       b'ignoreIconSize': ignoreIconSize, 
       b'titleAtMiddle': titleAtMiddle}
    if title is not None:
        data[b'title'] = title
    if desc is not None:
        data[b'description'] = desc
    if atlas is not None:
        data[b'atlasName'] = atlas
    if icon is not None:
        data[b'iconName'] = icon
    if iconPadding is not None:
        data[b'spritePadding'] = iconPadding
    if txtPadding is not None:
        data[b'textsPadding'] = txtPadding
    if txtGap != 0:
        data[b'textsGap'] = txtGap
    if txtOffset != 0:
        data[b'textsOffset'] = txtOffset
    if descPadding is not None:
        data[b'descPadding'] = descPadding
    if descLeading != 0:
        data[b'descLeading'] = descLeading
    return packBlockDataItem(linkage, data, padding, blockWidth)


def packRendererTextBlockData(rendererType, dataType, rendererData, title=None, desc=None, rendererPadding=None, imgAtLeft=True, titleAtMiddle=False, txtPadding=None, txtGap=0, txtOffset=-1, txtAlign=b'left', linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_RENDERER_TEXT_BLOCK_LINKAGE, padding=None):
    data = {b'rendererData': {b'rendererType': rendererType, 
                         b'data': rendererData, 
                         b'dataType': dataType}, 
       b'spriteAtLeft': imgAtLeft, 
       b'titleAtMiddle': titleAtMiddle, 
       b'textsAlign': txtAlign}
    if title is not None:
        data[b'title'] = title
    if desc is not None:
        data[b'description'] = desc
    if rendererPadding is not None:
        data[b'spritePadding'] = rendererPadding
    if txtPadding is not None:
        data[b'textsPadding'] = txtPadding
    if txtGap != 0:
        data[b'textsGap'] = txtGap
    if txtOffset != 0:
        data[b'textsOffset'] = txtOffset
    return packBlockDataItem(linkage, data, padding)


def packImageBlockData(img=None, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_IMAGE_BLOCK_LINKAGE, width=-1, height=-1, padding=None, alpha=1.0):
    data = {b'align': align, 
       b'alpha': alpha}
    if img is not None:
        data[b'imagePath'] = img
    if width != -1:
        data[b'width'] = width
    if height != -1:
        data[b'height'] = height
    return packBlockDataItem(linkage, data, padding)


def packQuestRewardItemBlockData(img=None, overlayPath=None, overlayPadding=None, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_QUEST_REWARD_ITEM_BLOCK_LINKAGE, padding=None):
    data = {b'align': align, 
       b'alpha': 1.0}
    if img is not None:
        data[b'imagePath'] = img
    if overlayPath is not None:
        data[b'overlayPath'] = overlayPath
        if overlayPadding is not None:
            data[b'overlayPadding'] = overlayPadding
    return packBlockDataItem(linkage, data, padding)


def packQuestProgressBlockData(progress=0, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_QUEST_PROGRESS_BLOCK_LINKAGE, padding=None):
    data = {b'progress': progress}
    return packBlockDataItem(linkage, data, padding)


def packQuestOrConditionBlockData(linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_QUEST_OR_CONDITION_BLOCK_LINKAGE, padding=None):
    return packBlockDataItem(linkage, {}, padding)


def packBlueprintBlockData(blueprintImg, schemeImg, numCols, numRows, layout, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BLUEPRINT_BLOCK_LINKAGE, width=-1, height=-1, padding=None, alpha=1.0):
    data = {b'blueprintPath': blueprintImg, 
       b'blueprintLayout': layout, 
       b'imagePath': schemeImg, 
       b'numCols': numCols, 
       b'numRows': numRows, 
       b'align': align, 
       b'alpha': alpha}
    if width != -1:
        data[b'width'] = width
    if height != -1:
        data[b'height'] = height
    return packBlockDataItem(linkage, data, padding)


def packTextBetweenLineBlockData(text, useHtml=True, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TEXT_BETWEEN_LINE_BLOCK_LINKAGE, customGap=5, lineAlpha=0.25, lineThickness=1, padding=None):
    data = {b'text': text, 
       b'useHtml': useHtml, 
       b'customGap': customGap, 
       b'lineAlpha': lineAlpha, 
       b'lineThickness': lineThickness}
    return packBlockDataItem(linkage, data, padding)


def packSaleTextParameterBlockData(name, saleData, actionStyle=ACTION_PRICE_CONSTANTS.STATE_CAMOUFLAGE, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_SALE_TEXT_PARAMETER_BLOCK_LINKAGE, padding=None, currency=None):
    data = {b'name': name, 
       b'saleData': saleData, 
       b'actionStyle': actionStyle, 
       b'currency': currency}
    return packBlockDataItem(linkage, data, padding)


def packActionTextParameterBlockData(name, value, icon, actionStyle=ACTION_PRICE_CONSTANTS.STATE_ALIGN_TOP, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_ACTION_TEXT_PARAMETER_BLOCK_LINKAGE, padding=None, currency=None, valueWidth=-1):
    data = {b'name': name, 
       b'value': value, 
       b'icon': icon, 
       b'actionStyle': actionStyle, 
       b'currency': currency, 
       b'valueWidth': valueWidth}
    return packBlockDataItem(linkage, data, padding)


def packStatusDeltaBlockData(title, valueStr, statusBarData, buffIconSrc=b'', linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_STATUS_DELTA_PARAMETER_BLOCK_LINKAGE, padding=None, deltaBlockGap=5):
    data = {b'title': title, 
       b'valueStr': valueStr, 
       b'statusBarData': statusBarData, 
       b'buffIconSrc': buffIconSrc, 
       b'deltaBlockGap': deltaBlockGap}
    return packBlockDataItem(linkage, data, padding)


def packCrewSkillsBlockData(crewStr, skillsStr, crewfIconSrc=b'', linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_CREW_SKILLS_BLOCK_LINKAGE, padding=None):
    data = {b'crewStr': crewStr, 
       b'skillsStr': skillsStr, 
       b'crewfIconSrc': crewfIconSrc}
    return packBlockDataItem(linkage, data, padding)


def packGroupBlockData(listData, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_GROUP_BLOCK_LINKAGE, padding=None, align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER, rendererWidth=48):
    data = {b'rendererType': (RANKEDBATTLES_ALIASES.RANKED_AWARD_RENDERER_ALIAS), 
       b'listIconSrc': listData, 
       b'align': align, 
       b'rendererWidth': rendererWidth}
    return packBlockDataItem(linkage, data, padding)


def packRankBlockData(rank, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_RANK_BLOCK_LINKAGE, padding=None):
    data = buildRankTooltipVO(rank=rank, imageSize=RANKEDBATTLES_ALIASES.WIDGET_BIG)
    return packBlockDataItem(linkage, data, padding)


def packItemActionTooltipData(item, isBuying=True):
    if isBuying:
        itemPrice = item.buyPrices.itemPrice
        itemAltPrice = item.buyPrices.itemAltPrice
    else:
        itemPrice = item.sellPrices.itemPrice
        itemAltPrice = item.sellPrices.itemAltPrice
    return packActionTooltipData(ACTION_TOOLTIPS_TYPE.ITEM, str(item.intCD), isBuying, itemPrice.price, itemPrice.defPrice, itemAltPrice.price, itemAltPrice.defPrice)


def packActionTooltipData(actionType, key, isBuying, price, oldPrice, altPrice=MONEY_UNDEFINED, oldAltPrice=MONEY_UNDEFINED):
    states = []
    if altPrice.isDefined():
        price = price + altPrice
    if oldAltPrice.isDefined():
        oldPrice = oldPrice + oldAltPrice
    for currency, oldValue in oldPrice.iterallitems():
        priceValue = price.getSignValue(currency)
        if priceValue < oldValue:
            state = ACTION_TOOLTIPS_STATE.DISCOUNT if isBuying else ACTION_TOOLTIPS_STATE.PENALTY
        elif priceValue > oldValue:
            state = ACTION_TOOLTIPS_STATE.PENALTY if isBuying else ACTION_TOOLTIPS_STATE.DISCOUNT
        else:
            state = None
        states.append(state)

    return {b'type': actionType, 
       b'key': key, 
       b'isBuying': isBuying, 
       b'state': states, 
       b'newPrice': (price.toMoneyTuple()), 
       b'oldPrice': (oldPrice.toMoneyTuple()), 
       b'ico': (price.getCurrency())}


def packItemRentActionTooltipData(item, rentPackage):
    defaultPrice = rentPackage[b'defaultRentPrice'].toMoneyTuple()
    price = rentPackage[b'rentPrice'].toMoneyTuple()
    states = len(price) * (ACTION_TOOLTIPS_STATE.DISCOUNT,)
    return {b'type': (ACTION_TOOLTIPS_TYPE.RENT), 
       b'key': (str(item.intCD)), 
       b'state': states, 
       b'newPrice': price, 
       b'oldPrice': defaultPrice, 
       b'rentPackage': (rentPackage[b'rentID'])}


def packImageListParameterBlockData(listIconSrc, columnWidth, rowHeight, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TILE_LIST_BLOCK_LINKAGE, padding=None, verticalGap=0, horizontalGap=0):
    return packBlockDataItem(linkage, {b'dataType': b'net.wg.gui.data.ImageRendererVO', 
       b'rendererType': b'ImageRendererUI', 
       b'listIconSrc': listIconSrc, 
       b'columnWidth': columnWidth, 
       b'rowHeight': rowHeight, 
       b'verticalGap': verticalGap, 
       b'horizontalGap': horizontalGap}, padding)


def packMapBoxBlockData(listIconSrc, columnWidth, rowHeight, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TILE_LIST_BLOCK_LINKAGE, padding=None, verticalGap=0, horizontalGap=0, blockWidth=0, renderersAlign=RENDERERS_ALIGN_LEFT):
    return packBlockDataItem(linkage, {b'dataType': b'net.wg.gui.lobby.hangar.mapBox.data.MapBoxItemVO', 
       b'rendererType': b'MapBoxItemRendererUI', 
       b'listIconSrc': listIconSrc, 
       b'columnWidth': columnWidth, 
       b'rowHeight': rowHeight, 
       b'verticalGap': verticalGap, 
       b'horizontalGap': horizontalGap, 
       b'renderersAlign': renderersAlign}, padding, blockWidth=blockWidth)


def packQuestAwardsBlockData(listData, columnWidth, rowHeight, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TILE_LIST_BLOCK_LINKAGE, padding=None):
    return packBlockDataItem(linkage, {b'dataType': b'net.wg.gui.data.AwardItemVO', 
       b'rendererType': b'AwardItemRendererUI', 
       b'listIconSrc': listData, 
       b'columnWidth': columnWidth, 
       b'rowHeight': rowHeight}, padding)


def packMissionVehiclesBlockData(listData, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TILE_LIST_BLOCK_LINKAGE, padding=None):
    return packBlockDataItem(linkage, {b'dataType': b'net.wg.gui.lobby.missions.data.MissionVehicleItemRendererVO', 
       b'rendererType': b'MissionVehicleItemRendererUI', 
       b'listIconSrc': listData, 
       b'columnWidth': 290, 
       b'rowHeight': 32}, padding)


def packMissionVehiclesTypeBlockData(listData, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TILE_LIST_BLOCK_LINKAGE, padding=None):
    return packBlockDataItem(linkage, {b'dataType': b'net.wg.gui.lobby.missions.data.MissionVehicleTypeRendererVO', 
       b'rendererType': b'MissionVehicleTypeRendererUI', 
       b'listIconSrc': listData, 
       b'columnWidth': 470, 
       b'rowHeight': 70}, padding)


def packAwardsExBlockData(listData, columnWidth, rowHeight, horizontalGap=0, verticalGap=0, renderersAlign=RENDERERS_ALIGN_LEFT, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_TILE_LIST_BLOCK_LINKAGE, padding=None):
    return packBlockDataItem(linkage, {b'dataType': b'net.wg.gui.lobby.components.data.AwardItemRendererExVO', 
       b'rendererType': b'AwardItemRendererExUI', 
       b'listIconSrc': listData, 
       b'columnWidth': columnWidth, 
       b'rowHeight': rowHeight, 
       b'renderersAlign': renderersAlign, 
       b'horizontalGap': horizontalGap, 
       b'verticalGap': verticalGap}, padding)


def getActionPriceData(item):
    minRentPricePackage = item.getRentPackage()
    action = None
    if minRentPricePackage and minRentPricePackage[b'rentPrice'] != minRentPricePackage[b'defaultRentPrice']:
        action = packItemRentActionTooltipData(item, minRentPricePackage)
    elif not item.isRestoreAvailable():
        if item.buyPrices.getSum().isActionPrice():
            action = packItemActionTooltipData(item)
    return action


def getLimitExceededPremiumTooltip():
    return makeTooltip(i18n.makeString(TOOLTIPS.LOBBY_HEADER_BUYPREMIUMACCOUNT_DISABLED_HEADER), i18n.makeString(TOOLTIPS.LOBBY_HEADER_BUYPREMIUMACCOUNT_DISABLED_BODY, number=time_utils.ONE_YEAR // time_utils.ONE_DAY))


def packCounterTextBlockData(countLabel, desc, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_COUNTER_TEXT_BLOCK_LINKAGE, padding=None):
    data = {b'label': (str(countLabel)), 
       b'description': desc}
    return packBlockDataItem(linkage, data, padding)


def packBadgeInfoBlockData(badgeImgSource, vehImgSource, playerName, vehName, stripImgSource=b'', linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BADGE_INFO_BLOCK_LINKAGE, padding=None):
    data = {b'badgeImgSource': badgeImgSource, 
       b'vehImgSource': vehImgSource, 
       b'playerName': playerName, 
       b'vehName': vehName, 
       b'stripImgSource': stripImgSource}
    return packBlockDataItem(linkage, data, padding)


def packMoneyAndXpValueBlock(value, icon, iconYoffset, paddingBottom=15, valueWidth=84, gap=5):
    valueBlock = packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HEADER_BUTTONS_AVAILABLE), value=value, icon=icon, padding=packPadding(bottom=paddingBottom), valueWidth=valueWidth, iconYOffset=iconYoffset, gap=gap)
    return valueBlock


def packMoneyAndXpBlocks(tooltipBlocks, btnType, valueBlocks, alternativeData=None, hideActionBlock=False):
    alternativeData = alternativeData or {}
    titleBlocks = [
     packTitleDescBlock(text_styles.highTitle(TOOLTIPS.getHeaderBtnTitle(alternativeData.get(b'title') or btnType)), None, padding=packPadding(bottom=15))]
    tooltipBlocks.append(packBuildUpBlockData(titleBlocks))
    if valueBlocks is not None:
        tooltipBlocks.append(packBuildUpBlockData(valueBlocks, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE))
    decsBlocks = []
    descLinkage = BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_LINKAGE
    if btnType == CURRENCIES_CONSTANTS.CRYSTAL:
        descLinkage = BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILD_BLOCK_VIOLET_BIG_LINKAGE
        padding = packPadding(bottom=8)
        decsBlocks.append(packTextBlockData(text_styles.middleTitle(backport.text(R.strings.tooltips.header.buttons.crystal.descriptionTitle())), padding=padding))
        descVehicle = text_styles.vehicleStatusInfoText(backport.text(R.strings.tooltips.header.buttons.crystal.descriptionVehicle()))
        decsBlocks.append(packTextBlockData(text_styles.main(backport.text(R.strings.tooltips.header.buttons.crystal.description0(), vehicle=descVehicle)), padding=padding))
        decsBlocks.append(packTextBlockData(text_styles.main(backport.text(R.strings.tooltips.header.buttons.crystal.description1())), padding=packPadding(bottom=20)))
    elif btnType == CURRENCIES_CONSTANTS.EQUIP_COIN:
        descLinkage = BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILD_BLOCK_YELLOW_LIGHT_LINKAGE
        padding = packPadding(bottom=8)
        decsBlocks.append(packTextBlockData(text_styles.middleTitle(backport.text(R.strings.tooltips.header.buttons.equipCoin.descriptionTitle())), padding=padding))
        descEquipCoin = text_styles.vehicleStatusInfoText(backport.text(R.strings.tooltips.header.buttons.equipCoin.descriptionEquipCoin()))
        decsBlocks.append(packTextBlockData(text_styles.main(backport.text(R.strings.tooltips.header.buttons.equipCoin.description0(), equipCoin=descEquipCoin)), padding=padding))
        decsBlocks.append(packTextBlockData(text_styles.main(backport.text(R.strings.tooltips.header.buttons.equipCoin.description1()))))
    elif btnType == CURRENCIES_CONSTANTS.BRCOIN:
        decsBlocks.append(packTextBlockData(text_styles.main(TOOLTIPS.getHeaderBtnDesc(alternativeData.get(b'btnDesc') or btnType)), padding=packPadding(bottom=-8)))
    else:
        decsBlocks.append(packTextBlockData(text_styles.main(TOOLTIPS.getHeaderBtnDesc(alternativeData.get(b'btnDesc') or btnType)), padding=packPadding(bottom=15)))
    tooltipBlocks.append(packBuildUpBlockData(decsBlocks, linkage=descLinkage))
    if not hideActionBlock:
        if btnType != CURRENCIES_CONSTANTS.CRYSTAL:
            actionBlocks = [
             packAlignedTextBlockData(text=text_styles.standard(TOOLTIPS.getHeaderBtnClickDesc(alternativeData.get(b'btnClickDesc') or btnType)), align=alternativeData.get(b'btnClickDescAlign') or BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER)]
            tooltipBlocks.append(packBuildUpBlockData(actionBlocks))
    return tooltipBlocks


def packSeparatorBlockData(paddings=None, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT):
    if paddings is None:
        paddings = packPadding(top=-40)
    return packImageBlockData(img=RES_ICONS.MAPS_ICONS_LIBRARY_SEPARATOR, align=align, padding=paddings)


def packItemPriceBlockData(price, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_COMPOUND_PRICE_BLOCK_LINKAGE, padding=None):
    return packBlockDataItem(linkage, price, padding)


def packCustomizationImageBlockData(img=None, align=BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_IMAGE_BLOCK_NON_HISTORICAL_LINKAGE, width=-1, height=-1, padding=None, formfactor=None, isDim=False):
    data = {b'align': align}
    if img is not None:
        data[b'imagePath'] = img
    if width != -1:
        data[b'width'] = width
    if height != -1:
        data[b'height'] = height
    data[b'isDim'] = isDim
    if formfactor is not None:
        data[b'formfactor'] = formfactor
    return packBlockDataItem(linkage, data, padding)


def packCustomizationRarityHeaderBlockData(img, rarity, rarityBackground, rarityIcon, title, subTitle, imgOffset=65, videoSource=b'', linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_IMAGE_BLOCK_RARITY_HEADER_LINKAGE, width=-1, height=-1, padding=None):
    data = {b'rarity': rarity, 
       b'imgOffset': imgOffset, 
       b'imagePath': img, 
       b'rarityIcon': rarityIcon, 
       b'rarityBackground': rarityBackground, 
       b'title': title, 
       b'subTitle': subTitle, 
       b'videoSource': videoSource}
    if width != -1:
        data[b'width'] = width
    if height != -1:
        data[b'height'] = height
    return packBlockDataItem(linkage, data, padding)


def packCustomizationCharacteristicBlockData(icon, text, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_CUSTOMIZATION_ITEM_PROPERTY_BLOCK_LINKAGE, padding=None, isTextIcon=False, isWideOffset=False):
    data = {b'icon': icon, 
       b'name': text, 
       b'isTextIcon': isTextIcon, 
       b'isWideOffset': isWideOffset}
    return packBlockDataItem(linkage, data, padding)


def packImageListIconData(imgSrc, imgAlpha=1):
    return {b'imgSrc': imgSrc, 
       b'imgAlpha': imgAlpha}


def getImage(resource, width=16, height=16, vspace=0, hspace=0):
    return makeHtmlString(b'html_templates:common', b'image', {b'icon': resource, 
       b'width': width, 
       b'height': height, 
       b'vspace': vspace, 
       b'hspace': hspace})


def packMultipleText(separator=b' ', *args, **kwargs):
    return packTextBlockData(separator.join(args), **kwargs)
