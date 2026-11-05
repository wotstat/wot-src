import { r as o } from "./rolldown-runtime.js";
import { B as e, D as t, E as a, O as s, an as r, qt as n, y as i } from "./lib.js";
var l = o(n(), 1);
function p({ bonuses: o, questId: n, size: p, resId: d, ...v }) {
  const u = r(o, (o) => {
      return {
        size: p,
        name: o.name,
        image: a(o, p),
        value: o.value,
        valueType: s(o.name),
        special:
          "overlayType" in o &&
          o.overlayType &&
          ((r = o.overlayType),
          ("string" == typeof r && Object.values(e).includes(r)) ||
            (console.warn(`Invalid overlayType value: ${r}`), 0))
            ? o.overlayType
            : void 0,
        tooltipArgs: {
          ...t(
            { tooltipId: `${n}:${o.tooltipId}` },
            Number(o.tooltipContentId) ||
              R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                "resId",
              ),
          ),
          resId: d,
        },
      };
      var r;
    }),
    y = {
      contentId: R.views.lobby.tooltips.AdditionalRewardsTooltip("resId"),
      args: { showFromIndex: v.count, questId: n },
      resId: d,
    };
  return (0, l.jsx)(i, { ...v, data: u, boxRewardTooltip: y, size: p });
}
export { p as t };
