import { r as a } from "../chunks/rolldown-runtime.js";
import {
  Ct as e,
  Dt as s,
  Et as t,
  G as r,
  H as i,
  Hn as n,
  In as d,
  It as o,
  Jt as l,
  K as c,
  Ln as m,
  Nt as p,
  Ot as _,
  Pn as y,
  Pt as u,
  Rt as x,
  St as g,
  Tn as h,
  U as f,
  V as v,
  Vt as j,
  W as N,
  Wt as b,
  dt as w,
  ht as A,
  yn as T,
  zn as C,
} from "../chunks/lib.js";
import "../chunks/_wg-global-styles.js";
import { m as E } from "../chunks/vendor.js";
var H = a(C(), 1),
  [O, k] = t()(
    ({ observableModel: a }) => ({ mainRewards: a.array("mainRewards") }),
    ({ externalModel: a }) => ({
      animationEnded: a.createCallbackNoArgs("onAnimationEnded"),
      close: a.createCallback((a) => ({ reason: a }), "onClose"),
    }),
  ),
  M = "TextMask_gradient_4dbfb7a9",
  S = "TextMask_9987747a",
  W = "TextMask_gradient__top_f63df556",
  z = "TextMask_gradient__bottom_9724ea06",
  Q = l(),
  I = ({ text: a, className: e }) =>
    (0, Q.jsxs)("span", {
      className: m(S, e),
      children: [
        a,
        (0, Q.jsx)("span", { className: m(M, W), children: a }),
        (0, Q.jsx)("span", { className: m(M, z), children: a }),
      ],
    }),
  P = ({ text: a, openTag: e, closeTag: s, classNames: t }) => {
    const [r, i] = a.split(e);
    if (!i) return a;
    const [n, d] = i.split(s);
    return (0, Q.jsxs)("span", {
      className: t?.title,
      children: [r && y(r), n && (0, Q.jsx)(I, { className: t?.highlight, text: n }), d && y(d)],
    });
  },
  B = "Header_7d83acf6",
  D = "Header_subTitleWrapper_dd95ac49",
  L = "Header_subTitle_11b912d7",
  V = "Header_arrow_de9151",
  $ = "Header_arrowHead_4e2a2709",
  G = "Header_arrowBody_27276e71",
  J = "Header_arrow__left_65f475ba",
  K = "Header_arrow__right_65f475ba",
  U = "Header_title_c5f44fd0",
  q = "Header_underTitleWrapper_4dc05e5a",
  F = "Header_wing_c1b09cf4",
  X = "Header_wing__left_a6e40196",
  Y = "Header_wing__right_f408d2da",
  Z = "Header_underTitle_a88a751e",
  aa = E(function () {
    const a = s(),
      e = n.resolve("strings"),
      t = e.readOrEmpty("awards.collector20.title"),
      r = e.readOrEmpty("awards.collector20.subTitle"),
      i = e.readOrEmpty("awards.collector20.underTitle"),
      l = o(
        ((a) => ({
          from: { opacity: 0, y: "-20rem" },
          to: { opacity: 1, y: "0rem" },
          delay: 100,
          config: { duration: 400, easings: d.easeOutQuad },
          onStart: () => {
            a.play("animation", { target: "subtitle" });
          },
        }))(a),
      ),
      c = o(
        ((a) => ({
          from: { opacity: 0, y: "-20rem" },
          to: { opacity: 1, y: "0rem" },
          delay: 1e3,
          config: { duration: 500, easings: d.easeOutQuad },
          onStart: () => {
            a.play("animation", { target: "title" });
          },
        }))(a),
      );
    return (0, Q.jsxs)("div", {
      className: B,
      children: [
        (0, Q.jsxs)(u.div, {
          style: l,
          className: D,
          children: [
            (0, Q.jsxs)("div", {
              className: m(V, J),
              children: [(0, Q.jsx)("div", { className: G }), (0, Q.jsx)("div", { className: $ })],
            }),
            r && (0, Q.jsx)(I, { className: L, text: r }),
            (0, Q.jsxs)("div", {
              className: m(V, K),
              children: [(0, Q.jsx)("div", { className: $ }), (0, Q.jsx)("div", { className: G })],
            }),
          ],
        }),
        t &&
          (0, Q.jsx)(u.div, {
            style: c,
            className: U,
            children: (0, Q.jsx)(P, { text: t, openTag: "{gold_Open}", closeTag: "{gold_Close}" }),
          }),
        (0, Q.jsxs)("div", {
          className: q,
          children: [
            i && (0, Q.jsx)("div", { className: Z, children: i }),
            (0, Q.jsx)("div", { className: m(F, X) }),
            (0, Q.jsx)("div", { className: m(F, Y) }),
          ],
        }),
      ],
    });
  }),
  ea = "AnimatedReward_1789d927",
  sa = ({ children: a, animationConfig: e, className: s }) => {
    const t = o(e);
    return (0, Q.jsx)(u.div, { style: t, className: m(ea, s), children: a });
  },
  ta = "MainRewards_title_b9294abf",
  ra = "MainRewards_f647a436",
  ia = "MainRewards_reward_7b876cb8",
  na = "MainRewards_captions_4f8422d",
  da = (a, e, s, t) => ({
    from: { opacity: 0, y: "20rem", pointerEvents: "none" },
    to: { opacity: 1, y: "0rem", pointerEvents: "auto" },
    trail: 300,
    delay: e + 300 * s,
    config: { duration: a },
    onStart: () => {
      t.play("animation", { target: "reward" });
    },
  }),
  oa = ({ rewards: a, classNames: e, oneCountDelay: t, duration: r }) => {
    const n = b({ size: N.S296x222 }, { medium: { size: N.S400x300 } }),
      d = s();
    return (0, Q.jsx)("div", {
      className: m(ra, e?.base),
      children: T(a, (a, s) =>
        (0, Q.jsxs)(
          sa,
          {
            animationConfig: da(r, t, s, d),
            className: ia,
            children: [
              (0, Q.jsx)(v, {
                name: a.name,
                image: i(
                  { item: a.item, type: a.overlayType, icon: a.icon, name: a.name, value: a.value },
                  n.size,
                ),
                special: a.overlayType,
                size: n.size,
                tooltipArgs: f({ tooltipId: a.tooltipId }, Number(a.tooltipContentId)),
              }),
              (0, Q.jsx)("div", {
                className: m(na, e?.caption),
                children: (0, Q.jsx)("div", { className: ta, children: y(a.label) }),
              }),
            ],
          },
          s + a.name + a.value,
        ),
      ),
    });
  },
  la = "App_video_b460a12e",
  ca = "App_decorWrapper_bb0bfe54",
  ma = "App_5c487cff",
  pa = "App_closeButton_f5179698",
  _a = "App_content_6d450fd7",
  ya = "App_wrapperRewards_af08fa77",
  ua = "App_reward_da80d895",
  xa = "App_mainRewardCaption_5929e7e0",
  ga = "App_ribbonWrapper_2210ce95",
  ha = "App_godraysWrapper_bbc67cd8",
  fa = "App_ribbon_f6a1d903",
  va = "App_raysWrapper_e48e223c",
  ja = "App_godrays_3df409cd",
  Na = "App_rays_20aa2b69",
  ba = "App_wrapperButton_6d5ac65d",
  wa = "App_button_7b36300d",
  Aa = "App_buttonContent_cd42fca3",
  Ta = 300,
  Ra = 2400,
  Ca = Ra,
  Ea = (a) => ({
    from: { opacity: 0, y: "0rem" },
    to: { opacity: 1, y: "-20rem" },
    delay: a,
    config: { duration: 400, easings: d.easeOutQuad },
  }),
  Ha = (a) => ({
    from: { opacity: 0 },
    to: { opacity: 1 },
    delay: a,
    config: { duration: 600, easings: d.easeOutQuad },
  }),
  Oa = (a) => ({
    from: { opacity: 0 },
    to: { opacity: 1 },
    delay: a,
    config: { duration: Ta, easings: d.easeOutQuad },
  }),
  ka = (a) => ({
    from: { opacity: 0, y: "0rem" },
    to: { opacity: 1, y: "-10rem" },
    delay: a,
    config: { duration: Ta, easings: d.easeOutQuad },
  }),
  Ma = E(function () {
    const [a, e] = (0, H.useState)(!1),
      t = (() => {
        const a = j(),
          e = p(),
          s = 2560 / 1440,
          t = viewEnv.pxToRem(a.width) * e,
          r = viewEnv.pxToRem(a.height) * e,
          i = t / r;
        return (0, H.useMemo)(
          () =>
            s >= i
              ? { width: r * s + "rem", height: `${r}rem` }
              : { width: `${t}rem`, height: t / s + "rem" },
          [r, i, t, s],
        );
      })(),
      { model: i, controls: d } = k(),
      l = s(),
      _ = n.resolve("strings"),
      y = () => {
        a && d.close("cancel");
      };
    (x(h.ESCAPE, y), x(h.ENTER, y), x(h.SPACE, y));
    const g = _.readOrEmpty("awards.collector20.button.affirmative"),
      f = (0, H.useCallback)(() => Ra + i.mainRewards.get().items.length * Ta, [i.mainRewards]),
      [v, N] = o(() => Ea(2e3)),
      [b, T] = o(() => Ha(Ca)),
      [C, E] = o(() => Oa(f())),
      [O, M] = o(() => ka(f()));
    return (
      (0, H.useLayoutEffect)(() => {
        e(!1);
        const a = f();
        (N.start({ ...Ea(2e3) }),
          T.start({
            ...Ha(Ca),
            onStart: () => {
              l.play("animation", { target: "godrays" });
            },
          }),
          E.start({ ...Oa(a) }),
          M.start({
            ...ka(a),
            onStart: () => {
              l.play("animation", { target: "end" });
            },
            onRest: () => e(!0),
          }),
          N.set({ opacity: 0, y: "0rem" }),
          T.set({ opacity: 0 }),
          E.set({ opacity: 0 }),
          M.set({ opacity: 0, y: "0rem" }));
      }, [M, E, T, N, f, l]),
      (0, Q.jsxs)("div", {
        className: m(ma),
        children: [
          (0, Q.jsx)(c, {
            src: R.videos.achievements.bg_reward_screen(),
            autoplay: !0,
            loop: !0,
            className: la,
            style: t,
          }),
          (0, Q.jsxs)("div", {
            className: ca,
            children: [
              (0, Q.jsx)(u.div, {
                style: v,
                className: ga,
                children: (0, Q.jsx)("div", { className: fa }),
              }),
              (0, Q.jsx)(u.div, {
                style: b,
                className: ha,
                children: (0, Q.jsxs)("div", {
                  className: va,
                  children: [
                    (0, Q.jsx)("div", { className: ja }),
                    (0, Q.jsx)("div", { className: Na }),
                  ],
                }),
              }),
            ],
          }),
          (0, Q.jsx)(u.div, { style: C, className: pa, children: (0, Q.jsx)(r, { onClose: y }) }),
          (0, Q.jsx)(aa, {}),
          (0, Q.jsxs)("div", {
            className: _a,
            children: [
              (0, Q.jsx)("div", {
                className: ya,
                children: (0, Q.jsx)("div", {
                  className: ua,
                  children: (0, Q.jsx)(oa, {
                    oneCountDelay: Ra,
                    rewards: i.mainRewards.get().items,
                    duration: Ta,
                    classNames: { caption: xa },
                  }),
                }),
              }),
              (0, Q.jsx)(u.div, {
                style: O,
                className: ba,
                children: (0, Q.jsx)(w, {
                  theme: A.primary,
                  classNames: { base: wa, content: Aa },
                  onClick: () => {
                    a && d.close("confirm");
                  },
                  children: g,
                }),
              }),
            ],
          }),
        ],
      })
    );
  }),
  Sa = _({
    animation: {
      title: "ach_cup_hover",
      subtitle: "gui_random_reward_red_ribbon_appear",
      godrays: "ach_sub_glare",
      reward: "gui_random_reward_appear",
      end: "gui_random_reward_end",
    },
  });
e(
  (0, Q.jsx)(O, { children: (0, Q.jsx)(g, { soundsOverrides: Sa, children: (0, Q.jsx)(Ma, {}) }) }),
);
