import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Ir as s,
  Ln as a,
  Qn as c,
  Ur as i,
  Xn as l,
  Yn as n,
  Zr as r,
  _ as t,
  _n as d,
  ci as o,
  fn as m,
  g as h,
  h as _,
  o as p,
  pn as b,
  ri as j,
  tn as v,
  ui as u,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as x } from "../chunks/vendor.js";
import { n as g } from "../chunks/utils.js";
import { n as N, t as w } from "../chunks/filename.js";
import { n as A, t as f } from "../chunks/useKeyup.js";
u();
var [V, k] = d()(
    ({ observableModel: e }) => ({ root: e.object(), vehicleInfo: e.object("vehicleInfo") }),
    i,
  ),
  C = "VehicleAward_1da7a90e",
  y = "VehicleAward_content_899c9ed4",
  I = "VehicleAward_vehicle_e48a2601",
  P = "VehicleAward_imageContainer_2313e12f",
  E = "VehicleAward_crop_908504d8",
  T = "VehicleAward_border_9c501e8e",
  $ = "VehicleAward_image_e1085013",
  L = "VehicleAward_score_9fcd64fb",
  S = "VehicleAward_scoreIcon_79b6ff35",
  W = "VehicleAward_level_be403845",
  z = "VehicleAward_name_db659683",
  B = "VehicleAward_title_d2db4e25",
  D = "VehicleAward_levelIcon_c18df12e",
  H = "VehicleAward_light_8a441018",
  K = "VehicleAward_rays_79b688e2",
  M = l(),
  Q = x(() => {
    const { model: e } = k(),
      { techName: s, vehicleLevelPoints: a } = e.root.get(),
      { vehicleType: c, vehicleName: i, vehicleLvl: l, isElite: n } = e.vehicleInfo.get(),
      r = j(s),
      t = {
        backgroundImage: `url(R.images.gui.maps.icons.vehicleTypes.big.${j(c)}${n ? "_elite" : ""})`,
      };
    return (0, M.jsx)("div", {
      className: C,
      children: (0, M.jsxs)("div", {
        className: y,
        children: [
          (0, M.jsx)("div", { className: H }),
          (0, M.jsxs)("div", {
            className: I,
            children: [
              r &&
                (0, M.jsxs)("div", {
                  className: P,
                  children: [
                    (0, M.jsx)("div", { className: K }),
                    (0, M.jsx)("div", {
                      className: E,
                      children: (0, M.jsx)("div", {
                        className: $,
                        style: {
                          backgroundImage: `url(${R.images.gui.maps.shop.vehicles.c_600x450.$dyn(r)})`,
                        },
                      }),
                    }),
                    (0, M.jsx)("div", { className: T }),
                  ],
                }),
              (0, M.jsxs)("span", {
                className: L,
                children: [a, "/", a, (0, M.jsx)("div", { className: S })],
              }),
            ],
          }),
          (0, M.jsxs)("span", {
            className: B,
            children: [
              (0, M.jsx)("span", { className: W, children: g(l) }),
              (0, M.jsx)("div", { className: D, style: t }),
              (0, M.jsx)("span", { className: z, children: i }),
            ],
          }),
        ],
      }),
    });
  }),
  U = "Content_deaba007",
  X = "Content_subTitle_15c1ed7d",
  Y = "Content_bonusPoints_20fbc1ad",
  Z = "Content_bonusIcon_3cb2baa3",
  q = "Content_2d9b5dc0",
  F = "Content_bottom_6af58715",
  G = "Content_reward_32d9fa9",
  J = "Content_buttonWrapper_c4ef9224",
  O = R.strings.battle_pass.battlePassVehicleAwardView,
  ee = x(() => {
    const { model: e } = k(),
      { battlePassPointsAward: s } = e.root.get(),
      { breakpoint: a } = n(),
      i = a.weight >= c.medium.weight;
    return (0, M.jsxs)("div", {
      className: U,
      children: [
        (0, M.jsx)(A, { title: O.content.title(), status: O.content.description() }),
        (0, M.jsxs)("div", {
          className: q,
          children: [
            (0, M.jsx)(Q, {}),
            (0, M.jsxs)("div", {
              className: F,
              children: [
                (0, M.jsxs)("div", {
                  className: G,
                  children: [
                    (0, M.jsx)("div", { className: X, children: O.content.subTitle() }),
                    (0, M.jsxs)("span", {
                      className: Y,
                      children: [s, (0, M.jsx)("div", { className: Z })],
                    }),
                  ],
                }),
                (0, M.jsx)(_, {
                  type: t.primary,
                  size: i ? h.medium : h.small,
                  onClick: () => r.close(),
                  mixClass: J,
                  children: O.button(),
                }),
              ],
            }),
          ],
        }),
      ],
    });
  }),
  se = "App_a42bc668",
  ae = "App_background_ceadfe63",
  ce = "App_background__shaded_1aa0b778",
  ie = "App_close_6d09ac22",
  le = x(() => {
    const { model: e } = k(),
      { chapterID: c } = e.root.get(),
      i = !c;
    (a(),
      f({ [s.ENTER]: () => r.close(), [s.SPACE]: () => r.close(), [s.ESCAPE]: () => r.close() }));
    return (0, M.jsxs)("div", {
      className: se,
      children: [
        (0, M.jsx)("div", {
          className: o(ae, i && ce),
          style: ((e) =>
            e
              ? {
                  backgroundImage: `url(${N(R.images.gui.maps.icons.battlePass.backgrounds.chapter_general, e)})`,
                }
              : w())(c),
        }),
        (0, M.jsx)("div", {
          className: ie,
          children: (0, M.jsx)(p, {
            caption: R.strings.menu.viewHeader.closeBtn.label(),
            type: "close",
            side: "right",
            onClick: () => r.close(),
          }),
        }),
        (0, M.jsx)(ee, {}),
      ],
    });
  });
m(
  new b()
    .add(v)
    .addWithProps(V, {})
    .render((0, M.jsx)(le, {})),
);
