import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Ct as s,
  Et as a,
  Fn as l,
  Hn as t,
  Jt as i,
  Rt as o,
  St as n,
  Tn as c,
  Wt as r,
  bt as d,
  dt as _,
  gt as m,
  ht as g,
  mt as v,
  q as p,
  ut as N,
  xt as x,
  yt as j,
  zn as h,
} from "../chunks/lib.js";
import "../chunks/_wg-global-styles.js";
import { m as b } from "../chunks/vendor.js";
h();
var u = e(x(), 1),
  f = (function (e) {
    return (
      (e.STANDARD = "standard"),
      (e.POST_PROGRESSION = "postProgression"),
      (e.VEH_SKILL_TREE = "vehSkillTree"),
      e
    );
  })({}),
  [P, k] = a()(
    ({ observableModel: e }) => ({
      ...e.primitives(["type", "isPrestigeAvailable"]),
      vehicleInfo: e.object("vehicleInfo"),
      prestigeEmblem: e.object("prestigeEmblem"),
    }),
    ({ externalModel: e }) => ({
      goToProgression: e.createCallbackNoArgs("onGoToProgression"),
      close: e.createCallbackNoArgs("onClose"),
    }),
  ),
  w = "Icon_glow_b6f80802",
  y = "Icon_glow__light_3f310309",
  C = "Icon_glow__strong_cd5dd8a1",
  S = "Icon_7f7c6297",
  T = "Icon_tankIcon_34bc69b9",
  A = i(),
  E = t.resolve("images"),
  I = b(({ vehicleType: e }) => {
    const { model: s } = k(),
      a = r({ value: "c_440x330" }, { small: { value: "c_600x450" } }),
      t = E.readOrEmpty(`elitewindow.tank_icons.${a.value}.${l(e)}`);
    return (0, A.jsxs)("div", {
      className: S,
      children: [
        (0, A.jsx)("div", { className: (0, u.default)(w, C) }),
        !s.isPrestigeAvailable.get() && (0, A.jsx)("div", { className: (0, u.default)(w, y) }),
        (0, A.jsx)("div", { className: T, style: { backgroundImage: `url(${t})` } }),
      ],
    });
  }),
  O = "ProgressionBlock_textBackground_52823f45",
  B = "ProgressionBlock_29163b1a",
  D = "ProgressionBlock_lockWrapper_721c0560",
  G = "ProgressionBlock_lock_4669aa21",
  H = "ProgressionBlock_lockCloud_c5cf7fca",
  z = "ProgressionBlock_content_8ce0e880",
  L = "ProgressionBlock_title_a1a7cf79",
  F = "ProgressionBlock_description_340e09db",
  $ = "ProgressionBlock_icon_230ee763",
  M = R.strings.elite_window.elite_window,
  W = b(({ className: e }) => {
    const { model: s } = k(),
      a = s.type.get(),
      l =
        a === f.POST_PROGRESSION ? M.post_progression.description() : M.vanity_progression.title(),
      t = a !== f.POST_PROGRESSION && M.vanity_progression.description();
    return (0, A.jsxs)("div", {
      className: (0, u.default)(B, e),
      children: [
        (0, A.jsxs)("div", {
          className: D,
          children: [(0, A.jsx)("div", { className: H }), (0, A.jsx)("div", { className: G })],
        }),
        (0, A.jsxs)("div", {
          className: z,
          children: [
            (0, A.jsx)("div", { className: O }),
            l &&
              (0, A.jsxs)("div", {
                className: L,
                children: [a === f.POST_PROGRESSION && (0, A.jsx)("div", { className: $ }), l],
              }),
            t && (0, A.jsx)(j, { text: t, split: !0, className: F }),
          ],
        }),
      ],
    });
  }),
  q = "Content_glow_7d6ef440",
  J = "Content_glow__strong_4a868d52",
  K = "Content_9af045a3",
  V = "Content_base__hasPostProgression_a9391767",
  Q = "Content_main_f562db1d",
  U = "Content_section_57c57489",
  X = "Content_section__image_7f1ebf74",
  Y = "Content_section__body_8837b3f5",
  Z = "Content_section__title_806db271",
  ee = "Content_section__description_e93395a4",
  se = "Content_prestigeBadge_a19642a7",
  ae = "Content_prestigeEmblem_5e4cfab0",
  le = "Content_postProgression_9f8673d",
  te = "Content_arrow_82982ba8",
  ie = R.strings.elite_window.elite_window,
  oe = b(({ className: e }) => {
    const { model: s, controls: a } = k(),
      l = s.vehicleInfo.get(),
      t = s.type.get(),
      i = s.isPrestigeAvailable.get(),
      o = s.prestigeEmblem.get();
    return (0, A.jsxs)("div", {
      className: (0, u.default)(K, t !== f.STANDARD && V),
      children: [
        (0, A.jsxs)("div", {
          className: Q,
          children: [
            (0, A.jsx)("div", { className: te }),
            (0, A.jsxs)("div", {
              className: U,
              children: [
                (0, A.jsx)("div", {
                  className: X,
                  children: (0, A.jsx)(I, { vehicleType: l.vehicleType }),
                }),
                (0, A.jsxs)("div", {
                  className: Y,
                  children: [
                    (0, A.jsx)("div", { className: Z, children: ie.elite.title() }),
                    (0, A.jsx)(j, { className: ee, text: ie.elite.description(), split: !0 }),
                  ],
                }),
              ],
            }),
            i &&
              (0, A.jsxs)("div", {
                className: U,
                children: [
                  (0, A.jsxs)("div", {
                    className: (0, u.default)(X, se),
                    children: [
                      (0, A.jsx)("div", { className: (0, u.default)(q, J) }),
                      (0, A.jsx)(m, {
                        level: o.level,
                        grade: o.grade ?? 1,
                        type: o.type,
                        size: m.sizes.xl,
                        classNames: { base: ae },
                      }),
                    ],
                  }),
                  (0, A.jsxs)("div", {
                    className: Y,
                    children: [
                      (0, A.jsx)("div", { className: Z, children: ie.prestige.title() }),
                      (0, A.jsx)(j, { className: ee, text: ie.prestige.description(), split: !0 }),
                    ],
                  }),
                ],
              }),
          ],
        }),
        t !== f.STANDARD && (0, A.jsx)(W, { className: le }),
      ],
    });
  }),
  ne = "Footer_e604d473",
  ce = "Footer_button_cc34b9a4",
  re = R.strings.elite_window.elite_window,
  de = b(({ className: e }) => {
    const { model: s, controls: a } = k(),
      l = s.type.get();
    return (0, A.jsxs)("div", {
      className: (0, u.default)(ne, e),
      children: [
        (0, A.jsx)(_, {
          onClick: a.close,
          size: v.medium,
          theme: g.primary,
          className: ce,
          children: re.buttons.ok(),
        }),
        l !== f.STANDARD &&
          (0, A.jsx)(_, {
            onClick: a.goToProgression,
            size: v.medium,
            theme: g.secondary,
            classNames: { base: ce },
            children:
              l === f.POST_PROGRESSION
                ? re.buttons.post_progression()
                : re.buttons.vanity_progression(),
          }),
      ],
    });
  }),
  _e = "Header_ee5a2d07",
  me = "Header_tankName_8c840ed3",
  ge = "Header_vehicleText_b549f08a",
  ve = "Header_title_b0ea43f0",
  pe = R.strings.elite_window.elite_window,
  Ne = b(({ className: e }) => {
    const { model: s } = k(),
      a = s.vehicleInfo.get();
    if (a.vehicleType in N)
      return (0, A.jsxs)("div", {
        className: (0, u.default)(_e, e),
        children: [
          (0, A.jsxs)(p, {
            className: me,
            children: [
              (0, A.jsx)(p.Level, { className: ge, value: a.vehicleLvl }),
              (0, A.jsx)(p.Type, { type: a.vehicleType, premium: a.isElite }),
              (0, A.jsx)(p.Name, { className: ge, children: a.vehicleName }),
            ],
          }),
          (0, A.jsx)("div", { className: ve, children: pe.title() }),
        ],
      });
  }),
  xe = "App_f208273f",
  je = "App_backgroundGlare_3ba092e8",
  he = "App_header_494088d4",
  be = "App_footer_ac8fd39",
  ue = "App_closeButton_c796cf51",
  fe = b(function () {
    const { controls: e } = k();
    return (
      o(c.ESCAPE, e.close),
      (0, A.jsxs)("div", {
        className: xe,
        children: [
          (0, A.jsx)("div", { className: je }),
          (0, A.jsx)("div", {
            className: ue,
            children: (0, A.jsx)(d, {
              caption: R.strings.menu.viewHeader.closeBtn.label(),
              type: "close",
              side: "right",
              onClick: e.close,
            }),
          }),
          (0, A.jsx)(Ne, { className: he }),
          (0, A.jsx)(oe, {}),
          (0, A.jsx)(de, { className: be }),
        ],
      })
    );
  });
s((0, A.jsx)(P, { children: (0, A.jsx)(n, { children: (0, A.jsx)(fe, {}) }) }));
