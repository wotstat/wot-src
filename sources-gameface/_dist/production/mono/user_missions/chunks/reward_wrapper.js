import { r as o } from "./rolldown-runtime.js";
import { B as e, C as t, Jt as s, S as a, on as r, v as n, w as i } from "./lib.js";
var l = o(s(), 1);
function p({ bonuses: o, questId: s, size: p, resId: d, ...v }) {
  const u = r(o, (o) => {
      return {
        size: p,
        name: o.name,
        image: a(o, p),
        value: o.value,
        valueType: i(o.name),
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
            { tooltipId: `${s}:${o.tooltipId}` },
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
    m = {
      contentId: R.views.lobby.tooltips.AdditionalRewardsTooltip("resId"),
      args: { showFromIndex: v.count, questId: s },
      resId: d,
    };
  return (0, l.jsx)(n, { ...v, data: u, boxRewardTooltip: m, size: p });
}
export { p as t };
