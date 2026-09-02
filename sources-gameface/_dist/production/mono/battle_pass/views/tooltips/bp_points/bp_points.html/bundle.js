import { j as s, w as e, k as t } from "../../../../chunks/vendor.js";
import {
  m as i,
  G as a,
  i as l,
  R as n,
  h as o,
  j as r,
  cd as c,
  J as d,
  U as h,
  d as _,
} from "../../../../chunks/lib.js";
import { V as j, W as x } from "../../../../chunks/wot_plus_banner.js";
import { P as m, a as p } from "../../../../chunks/per_battle_points_table.js";
/* empty css                       */ const v = "VehicleList_82a6a4d",
  b = "VehicleList_info_41a84ef",
  u = "VehicleList_points_9c8e2f92",
  N = "VehicleList_top_af361d05",
  f = ({ vehiclesList: e }) => {
    const t = ({
      vehicleLevel: e,
      vehicleName: t,
      vehicleType: i,
      vehicleBonus: l,
      vehicleTop: n,
      isElite: o,
    }) => ({
      vehicle: s.jsx(
        j,
        { isElite: o, isSpecial: !0, vehicleLevel: e, vehicleName: t, vehicleType: i },
        "vehicle",
      ),
      bonus: s.jsx(
        "div",
        {
          className: u,
          children: s.jsx(a, {
            text: R.strings.battle_pass.howToEarnPoints.bonus(),
            binding: { bonus: l },
          }),
        },
        "bonus",
      ),
      top: s.jsx(
        "div",
        {
          className: N,
          children: s.jsx(a, {
            text: R.strings.battle_pass.points.topCount(),
            binding: { top: n },
          }),
        },
        "top",
      ),
    });
    return s.jsx("div", {
      className: v,
      children: i(e, (e, i) => s.jsx(a, { classMix: b, text: e.textResource, binding: t(e) }, i)),
    });
  },
  [g, w] = l()(
    ({ observableModel: s }) => ({
      ...{
        ...s.primitives(["isWotPlusShown"]),
        rewardPoints: s.array("rewardPoints"),
        vehiclesList: s.array("vehiclesList"),
      },
    }),
    n,
  ),
  P = "Header_a103bd21",
  C = "Header_icon_eed746ab",
  L = "Header_labels_f416515f",
  k = "Header_title_381c9f5b",
  V = "Header_subtitle_632b6de",
  W = R.strings.battle_pass.tooltips.points,
  S = () =>
    s.jsxs("div", {
      className: P,
      children: [
        s.jsx("div", { className: C }),
        s.jsxs("div", {
          className: L,
          children: [
            s.jsx("div", { className: k, children: W.title() }),
            s.jsx("div", { className: V, children: W.subtitle() }),
          ],
        }),
      ],
    }),
  H = "Points_2d36306a",
  y = "Points_separator_162767d5",
  T = "Points_105728d0",
  E = "Points_table_eac25b11",
  B = e(() => {
    const { model: e } = w(),
      t = e.rewardPoints.get(),
      i = e.isWotPlusShown.get(),
      { breakpoint: a } = o();
    return s.jsxs("div", {
      className: H,
      children: [
        s.jsx("div", { className: y }),
        s.jsx("div", {
          className: T,
          children: s.jsx(m, {
            showSeparator: !1,
            stretchBg: !0,
            separatorRows: t.items,
            mixClass: E,
            children: s.jsx(p, {
              tableColumnWidth: a.weight < r.small.weight ? 210 : 230,
              rewardPoints: t,
              hasAdditionalPoints: i,
            }),
          }),
        }),
      ],
    });
  }),
  M = "Content_d4d03eba",
  A = "Content_separator_774f59ff",
  D = "Content_subtitleRules_2104a67e",
  F = "Content_subtitleVehicles_ead57094",
  G = "Content_pointsWrapper_21e79339",
  J = "Content_footerSeparator_a66c0c84",
  U = "Content_footer_92eb1524",
  q = "Content_footer__offset_9202885e",
  z = R.strings.battle_pass.tooltips.points,
  I = e(() => {
    const { model: e } = w(),
      { items: i } = e.vehiclesList.get(),
      l = e.isWotPlusShown.get();
    return s.jsxs("div", {
      className: M,
      children: [
        s.jsx(S, {}),
        s.jsx("div", { className: D, children: z.rules() }),
        s.jsxs("div", {
          className: G,
          children: [s.jsx(B, {}), l && s.jsx(x, {}), s.jsx("div", { className: A })],
        }),
        i.length > 0 &&
          s.jsxs(s.Fragment, {
            children: [
              s.jsx("div", { className: F, children: z.specialVehicles() }),
              s.jsx(f, { vehiclesList: i }),
              s.jsx("div", { className: J, children: s.jsx("div", { className: A }) }),
            ],
          }),
        s.jsx("div", { className: t(U, !i.length && q), children: s.jsx(a, { text: z.footer() }) }),
      ],
    });
  }),
  K = () => s.jsx(c, { children: s.jsx(c.Decorator, { children: s.jsx(I, {}) }) });
_(new d().add(h).addWithProps(g, {}).render(s.jsx(K, {})));
