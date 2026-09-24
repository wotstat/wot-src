import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Or as e,
  Qn as t,
  Ur as i,
  Xn as a,
  Xt as n,
  Yn as l,
  _n as o,
  bt as r,
  fn as c,
  n as d,
  pn as h,
  tn as _,
  ui as m,
} from "../../chunks/lib.js";
import "../../chunks/global.js";
import { h as x } from "../../chunks/vendor.js";
import { n as j, t as p } from "../../chunks/wot_plus_banner.js";
import { n as v, t as b } from "../../chunks/per_battle_points_table.js";
m();
var u = s(n(), 1),
  f = "VehicleList_82a6a4d",
  N = "VehicleList_info_41a84ef",
  g = "VehicleList_points_9c8e2f92",
  w = "VehicleList_top_af361d05",
  P = a(),
  C = ({ vehiclesList: s }) => {
    const t = ({
      vehicleLevel: s,
      vehicleName: e,
      vehicleType: t,
      vehicleBonus: i,
      vehicleTop: a,
      isElite: n,
    }) => ({
      vehicle: (0, P.jsx)(
        j,
        { isElite: n, isSpecial: !0, vehicleLevel: s, vehicleName: e, vehicleType: t },
        "vehicle",
      ),
      bonus: (0, P.jsx)(
        "div",
        {
          className: g,
          children: (0, P.jsx)(r, {
            text: R.strings.battle_pass.howToEarnPoints.bonus(),
            binding: { bonus: i },
          }),
        },
        "bonus",
      ),
      top: (0, P.jsx)(
        "div",
        {
          className: w,
          children: (0, P.jsx)(r, {
            text: R.strings.battle_pass.points.topCount(),
            binding: { top: a },
          }),
        },
        "top",
      ),
    });
    return (0, P.jsx)("div", {
      className: f,
      children: e(s, (s, e) =>
        (0, P.jsx)(r, { classMix: N, text: s.textResource, binding: t(s) }, e),
      ),
    });
  },
  [L, k] = o()(
    ({ observableModel: s }) => ({
      ...s.primitives(["isWotPlusShown"]),
      rewardPoints: s.array("rewardPoints"),
      vehiclesList: s.array("vehiclesList"),
    }),
    i,
  ),
  S = "Header_a103bd21",
  V = "Header_icon_eed746ab",
  W = "Header_labels_f416515f",
  H = "Header_title_381c9f5b",
  y = "Header_subtitle_632b6de",
  T = R.strings.battle_pass.tooltips.points,
  E = () =>
    (0, P.jsxs)("div", {
      className: S,
      children: [
        (0, P.jsx)("div", { className: V }),
        (0, P.jsxs)("div", {
          className: W,
          children: [
            (0, P.jsx)("div", { className: H, children: T.title() }),
            (0, P.jsx)("div", { className: y, children: T.subtitle() }),
          ],
        }),
      ],
    }),
  B = "Points_2d36306a",
  M = "Points_separator_162767d5",
  X = "Points_105728d0",
  A = "Points_table_eac25b11",
  D = x(() => {
    const { model: s } = k(),
      e = s.rewardPoints.get(),
      i = s.isWotPlusShown.get(),
      { breakpoint: a } = l();
    return (0, P.jsxs)("div", {
      className: B,
      children: [
        (0, P.jsx)("div", { className: M }),
        (0, P.jsx)("div", {
          className: X,
          children: (0, P.jsx)(b, {
            showSeparator: !1,
            stretchBg: !0,
            separatorRows: e.items,
            mixClass: A,
            children: (0, P.jsx)(v, {
              tableColumnWidth: a.weight < t.small.weight ? 210 : 230,
              rewardPoints: e,
              hasAdditionalPoints: i,
            }),
          }),
        }),
      ],
    });
  }),
  F = "Content_d4d03eba",
  O = "Content_separator_774f59ff",
  Q = "Content_subtitleRules_2104a67e",
  U = "Content_subtitleVehicles_ead57094",
  Y = "Content_pointsWrapper_21e79339",
  q = "Content_footerSeparator_a66c0c84",
  z = "Content_footer_92eb1524",
  G = "Content_footer__offset_9202885e",
  I = R.strings.battle_pass.tooltips.points,
  J = x(() => {
    const { model: s } = k(),
      { items: e } = s.vehiclesList.get(),
      t = s.isWotPlusShown.get();
    return (0, P.jsxs)("div", {
      className: F,
      children: [
        (0, P.jsx)(E, {}),
        (0, P.jsx)("div", { className: Q, children: I.rules() }),
        (0, P.jsxs)("div", {
          className: Y,
          children: [
            (0, P.jsx)(D, {}),
            t && (0, P.jsx)(p, {}),
            (0, P.jsx)("div", { className: O }),
          ],
        }),
        e.length > 0 &&
          (0, P.jsxs)(P.Fragment, {
            children: [
              (0, P.jsx)("div", { className: U, children: I.specialVehicles() }),
              (0, P.jsx)(C, { vehiclesList: e }),
              (0, P.jsx)("div", { className: q, children: (0, P.jsx)("div", { className: O }) }),
            ],
          }),
        (0, P.jsx)("div", {
          className: (0, u.default)(z, !e.length && G),
          children: (0, P.jsx)(r, { text: I.footer() }),
        }),
      ],
    });
  }),
  K = () => (0, P.jsx)(d, { children: (0, P.jsx)(d.Decorator, { children: (0, P.jsx)(J, {}) }) });
c(
  new h()
    .add(_)
    .addWithProps(L, {})
    .render((0, P.jsx)(K, {})),
);
