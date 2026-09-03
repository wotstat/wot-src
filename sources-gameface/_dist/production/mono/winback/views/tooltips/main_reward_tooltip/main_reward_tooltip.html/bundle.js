import { x as e, j as a } from "../../../../chunks/vendor.js";
import {
  m as s,
  K as l,
  L as i,
  M as r,
  i as c,
  n as d,
  r as n,
  a5 as v,
  t as m,
  W as p,
  F as o,
  a6 as t,
  b as h,
  U as _,
} from "../../../../chunks/lib.js";
import { R as j } from "../../../../chunks/winback_reward_view_model.js";
/* empty css                       */ const [x, b] = c("MainRewardTooltipModel")(
    ({ observableModel: e }) => ({ rewards: e.array("rewards") }),
    d,
  ),
  L = "App_d6b0e451",
  w = "App_title_7858e66b",
  A = "App_separator_5986716c",
  E = "App_description_d87084dc",
  N = "App_rewards_ff6b94c3",
  u = "App_reward_fefa0cc6",
  f = "App_label_382ed0ee",
  T = "App_vehicle_4ade442a",
  k = "App_vehicleLevel_1a558fca",
  C = "App_discount_8b0e8a4b",
  R = n.resolve("strings"),
  S = e(function () {
    const { model: e } = b(),
      c = ((e) =>
        s(e, (e) => ({
          name: e.name,
          image: i(e, r.Small),
          value: e.value,
          valueType: l(e.name),
          vehicleLvl: "vehicleLvl" in e ? e.vehicleLvl : void 0,
          label: e.label,
        })))(e.rewards.get());
    return a.jsx(v, {
      children: a.jsxs("div", {
        className: L,
        children: [
          a.jsx("div", {
            className: w,
            children: R.readOrEmpty("winback.mainRewardTooltip.title"),
          }),
          a.jsx("div", {
            className: E,
            children: R.readOrEmpty("winback.mainRewardTooltip.description"),
          }),
          a.jsxs("div", {
            className: N,
            children: [
              a.jsx("div", { className: A }),
              s(c, (e, s) =>
                a.jsxs(
                  "div",
                  {
                    className: u,
                    children: [
                      e.name === j.SELECTABLE_VEHICLE_DISCOUNT && e.vehicleLvl
                        ? a.jsxs("div", {
                            className: T,
                            children: [
                              a.jsx("div", { className: k, children: m(e.vehicleLvl) }),
                              a.jsx("div", { className: C }),
                            ],
                          })
                        : a.jsx(p, { ...e, size: r.S48x48 }),
                      a.jsx("div", {
                        className: f,
                        children:
                          e.name === j.SELECTABLE_VEHICLE_DISCOUNT && e.vehicleLvl
                            ? a.jsx(o, {
                                path: "winback.mainRewardTooltip.vehicleRewardLabel",
                                params: { level: m(e.vehicleLvl) },
                              })
                            : a.jsx(a.Fragment, { children: a.jsx(t, { text: e.label }) }),
                      }),
                    ],
                  },
                  s,
                ),
              ),
            ],
          }),
        ],
      }),
    });
  });
h(a.jsx(x, { children: a.jsx(_, { children: a.jsx(S, {}) }) }), { immediateLayout: !1 });
