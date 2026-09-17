import { D as s, j as e } from "../../../../chunks/vendor.js";
import {
  i as o,
  m as i,
  L as a,
  Y as r,
  Z as t,
  n,
  $ as l,
  g as d,
  F as m,
  a0 as c,
  r as p,
} from "../../../../chunks/lib.js";
import { D as u } from "../../../../chunks/divider.js";
import { E as y } from "../../../../chunks/extended_tooltip_decorator.js";
import { S as v } from "../../../../chunks/spec_conditions.js";
import { t as _ } from "../../../../chunks/helpers.js";
const [j, k] = o()(
    ({ observableModel: s }) => ({
      ...s.primitives(["commonConditionId"]),
      specConditions: s.transform((s) => _(s), "specialConditionIds"),
      rewards: s.transform(
        (s) =>
          i(s, (s) => {
            return {
              size: a.Small,
              name: s.name,
              image: t(s, a.Small),
              value: s.value,
              valueType: r(s.name),
              special:
                "overlayType" in s &&
                ((e = s.overlayType),
                ("string" == typeof e && Object.values(l).includes(e)) ||
                  (console.warn(`Invalid overlayType value: ${e}`), 0))
                  ? s.overlayType
                  : void 0,
            };
            var e;
          }),
        "bonuses",
      ),
    }),
    n,
  ),
  f = "WeeklyQuestTooltip_specConditions_dc19d553",
  h = "WeeklyQuestTooltip_divider_18712a6c",
  T = "WeeklyQuestTooltip_blockTitle_31eb440a",
  x = "WeeklyQuestTooltip_rewards_b03f0c37",
  b = "WeeklyQuestTooltip_rewardItem_e6e09bf9",
  w = d.resolve("strings"),
  C = s(function () {
    const { model: s } = k(),
      o = s.specConditions.get();
    return e.jsxs(y, {
      header: w.readOrEmpty("user_missions.tooltip.weekly_mission"),
      description: w.readOrEmpty(`weekly_quests.condition.common.c_${s.commonConditionId.get()}`),
      invertedColors: !0,
      children: [
        o.length > 0 && e.jsx(v, { specConditions: o, className: f }),
        e.jsx(u, { className: h }),
        e.jsx(m, { path: "user_missions.tooltip.daily_quests.rewards", className: T }),
        e.jsx(c, { data: s.rewards.get(), size: a.Small, classMix: x, rewardItemClassMix: b }),
      ],
    });
  });
p(e.jsx(j, { children: e.jsx(C, {}) }));
