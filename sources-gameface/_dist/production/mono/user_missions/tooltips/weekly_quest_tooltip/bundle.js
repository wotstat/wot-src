import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  B as e,
  Jt as o,
  Pn as t,
  S as i,
  St as a,
  _t as r,
  on as n,
  st as l,
  un as d,
  v as m,
  w as c,
  yt as p,
  z as u,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
import { t as y } from "../../chunks/divider.js";
import { t as _ } from "../../chunks/extended_tooltip_decorator.js";
import { r as v } from "../../chunks/helpers.js";
import { t as j } from "../../chunks/spec_conditions.js";
var [k, h] = a()(
    ({ observableModel: s }) => ({
      ...s.primitives(["commonConditionId"]),
      specConditions: s.transform((s) => v(s), "specialConditionIds"),
      rewards: s.transform(
        (s) =>
          n(s, (s) => {
            return {
              size: u.Small,
              name: s.name,
              image: i(s, u.Small),
              value: s.value,
              valueType: c(s.name),
              special:
                "overlayType" in s &&
                ((o = s.overlayType),
                ("string" == typeof o && Object.values(e).includes(o)) ||
                  (console.warn(`Invalid overlayType value: ${o}`), 0))
                  ? s.overlayType
                  : void 0,
            };
            var o;
          }),
        "bonuses",
      ),
    }),
    d,
  ),
  f = "WeeklyQuestTooltip_specConditions_dc19d553",
  w = "WeeklyQuestTooltip_divider_18712a6c",
  T = "WeeklyQuestTooltip_blockTitle_31eb440a",
  b = "WeeklyQuestTooltip_rewards_b03f0c37",
  x = "WeeklyQuestTooltip_rewardItem_e6e09bf9",
  g = s(o(), 1),
  C = t.resolve("strings"),
  I = r(function () {
    const { model: s } = h(),
      e = s.specConditions.get();
    return (0, g.jsxs)(_, {
      header: C.readOrEmpty("user_missions.tooltip.weekly_mission"),
      description: C.readOrEmpty(`weekly_quests.condition.common.c_${s.commonConditionId.get()}`),
      invertedColors: !0,
      children: [
        e.length > 0 && (0, g.jsx)(j, { specConditions: e, className: f }),
        (0, g.jsx)(y, { className: w }),
        (0, g.jsx)(l, { path: "user_missions.tooltip.daily_quests.rewards", className: T }),
        (0, g.jsx)(m, { data: s.rewards.get(), size: u.Small, classMix: b, rewardItemClassMix: x }),
      ],
    });
  });
p((0, g.jsx)(k, { children: (0, g.jsx)(I, {}) }));
