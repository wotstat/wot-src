import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $ as a,
  $n as t,
  $r as s,
  $t as r,
  A as n,
  An as i,
  Ar as o,
  At as l,
  B as c,
  Bn as d,
  Br as _,
  Cn as u,
  Ct as m,
  D as p,
  Dn as h,
  Dr as b,
  Dt as f,
  E as g,
  En as v,
  Er as x,
  Et as w,
  F as C,
  Fn as y,
  Fr as S,
  Ft as j,
  G as I,
  Gn as N,
  Gr as k,
  Gt as P,
  H as B,
  Hn as A,
  Hr as E,
  Ht as T,
  I as L,
  In as O,
  Ir as D,
  It as W,
  Jn as V,
  Jr as M,
  K as z,
  Kn as $,
  Kr as F,
  Kt as H,
  L as U,
  Lr as G,
  Lt as q,
  M as K,
  Mn as X,
  Mr as Z,
  Mt as J,
  N as Q,
  Nn as Y,
  Nr as ee,
  Nt as ae,
  O as te,
  On as se,
  Or as re,
  Ot as ne,
  P as ie,
  Pn as oe,
  Pr as le,
  Pt as ce,
  Q as de,
  Qn as _e,
  Qr as ue,
  R as me,
  Rn as pe,
  Rr as he,
  Rt as be,
  S as fe,
  Sn as ge,
  Sr as ve,
  St as xe,
  T as we,
  Tn as Ce,
  Tr as ye,
  Tt as Se,
  U as je,
  Un as Ie,
  Ur as Ne,
  Ut as ke,
  V as Pe,
  Vn as Re,
  Vt as Be,
  W as Ae,
  Wn as Ee,
  Wr as Te,
  Wt as Le,
  Xn as Oe,
  Xr as De,
  Xt as We,
  Y as Ve,
  Yn as Me,
  Z as ze,
  Zr as $e,
  _ as Fe,
  _n as He,
  _r as Ue,
  _t as Ge,
  a as qe,
  ai as Ke,
  an as Xe,
  ar as Ze,
  at as Je,
  b as Qe,
  bn as Ye,
  br as ea,
  bt as aa,
  c as ta,
  ci as sa,
  cn as ra,
  cr as na,
  ct as ia,
  d as oa,
  di as la,
  dr as ca,
  dt as da,
  en as _a,
  er as ua,
  et as ma,
  f as pa,
  fi as ha,
  fn as ba,
  fr as fa,
  ft as ga,
  g as va,
  gn as xa,
  gr as wa,
  gt as Ca,
  h as ya,
  hn as Sa,
  ht as ja,
  i as Ia,
  in as Na,
  it as ka,
  j as Pa,
  jn as Ra,
  jr as Ba,
  jt as Aa,
  k as Ea,
  kn as Ta,
  kr as La,
  kt as Oa,
  li as Da,
  ln as Wa,
  lr as Va,
  lt as Ma,
  m as za,
  mn as $a,
  mt as Fa,
  ni as Ha,
  nr as Ua,
  nt as Ga,
  o as qa,
  on as Ka,
  or as Xa,
  ot as Za,
  p as Ja,
  pi as Qa,
  pn as Ya,
  pt as et,
  qn as at,
  qr as tt,
  ri as st,
  rn as rt,
  rr as nt,
  rt as it,
  s as ot,
  si as lt,
  sr as ct,
  st as dt,
  tn as _t,
  tr as ut,
  tt as mt,
  u as pt,
  ui as ht,
  ut as bt,
  v as ft,
  vn as gt,
  vr as vt,
  vt as xt,
  wn as wt,
  wr as Ct,
  wt as yt,
  x as St,
  xn as jt,
  xr as It,
  y as Nt,
  yn as kt,
  yr as Pt,
  yt as Rt,
  z as Bt,
  zn as At,
  zr as Et,
} from "../chunks/lib.js";
import "../chunks/global.js";
import {
  a as Tt,
  c as Lt,
  d as Ot,
  f as Dt,
  h as Wt,
  i as Vt,
  l as Mt,
  m as zt,
  n as $t,
  o as Ft,
  p as Ht,
  r as Ut,
  s as Gt,
  t as qt,
  u as Kt,
} from "../chunks/vendor.js";
import {
  a as Xt,
  c as Zt,
  d as Jt,
  f as Qt,
  l as Yt,
  n as es,
  o as as,
  p as ts,
  r as ss,
  t as rs,
} from "../chunks/utils.js";
import { t as ns } from "../chunks/tank_name.js";
import { n as is, t as os } from "../chunks/filename.js";
import { n as ls, t as cs } from "../chunks/tankmen_screen.js";
import { n as ds, t as _s } from "../chunks/constants.js";
var us = e(ht(), 1),
  ms = Oe(),
  ps = (0, us.createContext)({
    currentValue: 0,
    prevValue: 0,
    setCurrentValue: (e) => {},
    setPrevValue: (e) => {},
    delta: 0,
    setDelta: (e) => {},
    levelsCount: 0,
    hasMoved: !1,
    setHasMoved: (e) => {},
    levelPrice: 0,
    levelsToBuy: 0,
    setLevelsToBuy: (e) => {},
    levelsPassed: 0,
    maxValueAchieved: !1,
    setMaxValueAchieved: (e) => {},
  });
function hs() {
  const e = (0, us.useContext)(ps);
  if (!e) throw new Error("use useBPProgressBar must be used within a ProgressBar");
  return e;
}
function bs({ children: e, levelsCount: a, levelPrice: t, levelsPassed: s }) {
  const [r, n] = (0, us.useState)(0),
    [i, o] = (0, us.useState)(0),
    [l, c] = (0, us.useState)(0),
    [d, _] = (0, us.useState)(0),
    [u, m] = (0, us.useState)(!1),
    [p, h] = (0, us.useState)(!1),
    b = (0, us.useMemo)(
      () => ({
        currentValue: r,
        prevValue: i,
        setCurrentValue: n,
        setPrevValue: o,
        delta: l,
        setDelta: c,
        levelsCount: a,
        hasMoved: u,
        setHasMoved: m,
        levelPrice: t,
        levelsToBuy: d,
        setLevelsToBuy: _,
        levelsPassed: s,
        maxValueAchieved: p,
        setMaxValueAchieved: h,
      }),
      [r, i, n, o, l, c, a, u, m, t, d, _, s, p, h],
    );
  return (0, ms.jsx)(ps.Provider, { value: b, children: e });
}
var fs = "BuyButtons_ce6c20b6",
  gs = "BuyButtons_button_8a617f11",
  vs = Qa.resolve("strings"),
  xs = ({
    isWalletAvailable: e,
    purchaseAbortedCount: a,
    onAccept: t,
    onCancel: s,
    className: r,
  }) => {
    const n = at({ buttonSize: Se.medium }, { large: { buttonSize: Se.large } }),
      { maxValueAchieved: i, setMaxValueAchieved: o, levelsToBuy: l } = hs(),
      c = h();
    (0, us.useEffect)(() => {
      o(!1);
    }, [a, o]);
    const d = Ee(() => {
      !e || i || c.isRunning || (o(!0), c.run(t, 20 * l));
    });
    return (
      ((e) => {
        const a = (0, us.useCallback)(
          (a) => {
            a.altKey || e();
          },
          [e],
        );
        pe(D.ENTER, a);
      })(d),
      (0, ms.jsxs)("div", {
        className: sa(fs, r),
        children: [
          (0, ms.jsx)(yt, {
            theme: w.primary,
            size: n.buttonSize,
            className: gs,
            onClick: d,
            disabled: !e,
            children: vs.readOrEmpty("battle_pass.battlePassBuyView.confirm.btnBuy"),
          }),
          (0, ms.jsx)(yt, {
            theme: w.secondary,
            size: n.buttonSize,
            className: gs,
            onClick: s,
            children: vs.readOrEmpty("battle_pass.battlePassBuyView.btnCancel"),
          }),
        ],
      })
    );
  },
  ws = {
    base: "Title_df1cd9e2",
    chapter: "Title_chapter_4c7a1992",
    base__transparentChapterName: "Title_base__transparentChapterName_2e63cf3",
    subTitle: "Title_subTitle_2bbdc239",
    fadeInWithScale: "Title_fadeInWithScale_2e63cf3",
    slideUp: "Title_slideUp_2e63cf3",
    blink: "Title_blink_2e63cf3",
    scale: "Title_scale_2e63cf3",
    rotate: "Title_rotate_2e63cf3",
    windowIn: "Title_windowIn_2e63cf3",
    fadeOut: "Title_fadeOut_2e63cf3",
    fadeIn: "Title_fadeIn_2e63cf3",
  },
  Cs = Qa.resolve("strings"),
  ys = ({ chapter: e, subTitle: a, className: t, type: s = "default" }) =>
    (0, ms.jsxs)("div", {
      className: sa(ws.base, ws[`base__${s}`], t),
      children: [
        (0, ms.jsx)("span", {
          className: ws.chapter,
          children: (0, ms.jsx)(aa, {
            text: Cs.readOrEmpty("battle_pass.battlePassBuyLevels.chapter"),
            binding: { name: Cs.readOrEmpty(`battle_pass.chapter.fullName.c_${e}`) },
          }),
        }),
        (0, ms.jsx)("span", { className: ws.subTitle, children: a }),
      ],
    }),
  [Ss, js] = He()(
    ({ observableModel: e }) => {
      const a = { root: e.object(), rewards: e.arrayClone("rewards.items") },
        t = xa(() => re(a.rewards.get(), E), { equals: _ });
      return { ...a, computes: { getRewards: t } };
    },
    ({ externalModel: e }) => ({
      changeSelectedLevels: e.createCallback((e) => ({ count: e }), "onChangeSelectedLevels"),
      buy: e.createCallbackNoArgs("onPurchase"),
    }),
  ),
  Is = (e, a) => Math.round((e / a) * 100);
var Ns = "Delta_7e5549",
  ks = "Delta_outside_b28c01e5",
  Ps = "Delta_outside__increase_91391b24",
  Rs = "Delta_inside_b1b3a5c5",
  Bs = "Delta_inside__increase_fcd871c4",
  As = (0, us.memo)(
    (0, us.forwardRef)(function (
      {
        from: e,
        step: t,
        growAnimationConfig: s,
        shrinkAnimationConfig: r,
        classNames: n,
        className: o,
        steps: l,
        onState: c,
        ...d
      },
      _,
    ) {
      const u = (0, us.useRef)(null),
        m = it(),
        [p, h] = Ra(() => ({ width: 0 })),
        [b, f] = Ra(() => ({ width: 0 })),
        [g, v] = Ra(() => ({ x: 0, width: 0 })),
        [x, ...w] = l,
        [C, y] = (0, us.useState)(w),
        [S, j] = (0, us.useState)(x ?? "done"),
        I = (m.value - e) / m.maxValue,
        N = a(I);
      ma("delta");
      const k = Ee(c ?? Ne);
      (0, us.useEffect)(() => k(S), [S, k]);
      const P = Ee(() => {
          const [e, ...a] = C;
          e ? (j(e), y(a)) : j("done");
        }),
        R = Ee(() => {
          const a = u.current?.parentElement;
          if (!a) return;
          const t = a.offsetWidth,
            s = Math.max(m.value, e),
            r = e / m.maxValue,
            n = (s - e) / m.maxValue,
            i = Math.round(t * r),
            o = Math.round(t * n);
          v.start({ x: i, width: o, immediate: !0 });
        });
      return (
        (0, us.useEffect)(() => {
          if ((R(), 0 === I))
            return (h.set({ width: 100 }), f.set({ width: 100 }), j("done"), void y([]));
        }, [I, R, h, f]),
        (0, us.useEffect)(() => {
          ("growing" === S &&
            (f.set({ width: 100 }),
            h.start({
              from: { width: 0 },
              to: { width: 100 },
              config: s ?? mt,
              onRest: P,
              onStart: () => N({ step: S }),
            })),
            "shrinking" === S &&
              (h.set({ width: 100 }),
              f.start({
                from: { width: 100 },
                to: { width: 0 },
                config: r ?? mt,
                onRest: P,
                onStart: () => N({ step: S }),
              })));
        }, [S, h, f, s, r, P, N]),
        (0, ms.jsxs)(i.div, {
          ...d,
          ref: $a([_, u]),
          className: sa(o, Ns),
          style: {
            transform: g.x.to((e) => `translateX(${e}px)`),
            width: g.width.to((e) => `${e}px`),
          },
          children: [
            (0, ms.jsxs)(i.div, {
              style: { width: b.width.to((e) => `${e}%`) },
              className: sa(n?.outside, ks, I > 0 && Ps),
              children: [
                (0, ms.jsx)(i.div, {
                  style: { width: p.width.to((e) => `${e}%`) },
                  className: sa(n?.inside, Rs, I > 0 && Bs),
                }),
                d.children,
              ],
            }),
            d.children,
          ],
        })
      );
    }),
  );
var Es = "Pointer_45abb891",
  Ts = "Pointer_9fe9949c",
  Ls = "Pointer_pointer__down_925b0a0d",
  Os = { top: "top", down: "down" },
  Ds = function ({
    position: e = Os.down,
    maxValueAchieved: a,
    silent: t = !1,
    setMaxValueAchieved: s,
    soundTarget: r,
    className: n,
    classNames: i,
  }) {
    const o = (0, us.useRef)(!1),
      l = (0, us.useRef)(null),
      [c, d] = (0, us.useState)(!1),
      _ = (0, us.useRef)(null),
      u = (0, us.useRef)(null),
      m = (0, us.useRef)(null),
      p = (0, us.useRef)(null),
      { percentage: h, maxValue: b, setValue: f, value: g, status: v } = it(),
      {
        setCurrentValue: x,
        setPrevValue: w,
        setHasMoved: C,
        levelsCount: y,
        levelsToBuy: S,
        setLevelsToBuy: j,
        levelsPassed: I,
      } = hs(),
      { controls: N } = js(),
      k = (function (e, a) {
        const t = ge(),
          s = a ?? "controlled-progress-bar:pointer";
        return Ee(({ event: a, diff: r = 0 }) => {
          if (!e)
            return "grab" === a
              ? t.play("pointerGrab", { target: s })
              : "drag" === a
                ? t.play("pointerDrag", { target: s })
                : "hover" === a
                  ? t.play("mouse-enter", { target: s })
                  : "delta" === a && r > 0
                    ? t.play("increaseDelta", { target: s })
                    : void 0;
        });
      })(t, r),
      P = (0, us.useRef)(I),
      R = Math.round((b / y) * 1e3) / 1e3,
      B = (I / y) * b,
      A = B + R,
      E = 100 * h,
      T = Ee(() => d(!1));
    (0, us.useEffect)(() => {
      const e = P.current,
        a = Math.max(0, I - e);
      let t;
      if (null === m.current) t = B + R;
      else {
        const e = m.current - a * R,
          s = Math.max(e, R);
        ((m.current = s), (t = B + s));
      }
      return (
        (t = Math.min(t, b)),
        f(B),
        x(B),
        l.current && cancelAnimationFrame(l.current),
        (l.current = requestAnimationFrame(() => {
          (f(t), x(t));
        })),
        w(B),
        (P.current = I),
        () => {
          l.current && cancelAnimationFrame(l.current);
        }
      );
    }, [I, y, b, f, B, x, w, R]);
    const L = Ee((e) => {
      if (!_.current) return;
      C(!0);
      const a = _.current.getBoundingClientRect(),
        t = e.clientX - a.left,
        s = Math.max(0, Math.min(1, t / a.width)) * b,
        r = Math.round(s / R) * R,
        n = Math.max(r, A);
      (p.current !== n && (n !== B && k({ event: "drag" }), (p.current = n)),
        f(n),
        x(n),
        (m.current = n - B));
    });
    function O() {
      (C(!1), s(!1), d(!0), (p.current = g));
    }
    ((0, us.useEffect)(() => {
      u.current && (u.current.style.left = `${E}%`);
    }, [E]),
      (0, us.useEffect)(() => {
        if (c)
          return new he().add(Et(window, "mousemove", (e) => L(e))).add(
            Et(window, "mouseup", (e) => {
              (L(e), T());
            }),
          ).dispose;
      }, [c, L, T]));
    const D = (e) => Math.min(Math.max(e, A), b);
    return (
      pe(G.ARROW_LEFT, () => {
        if (o.current || c || a) return;
        o.current = !0;
        const e = D(g - R);
        (f(e), x(e), (m.current = e - B), j(Math.round(((e - B) * y) / 100)));
      }),
      pe(G.ARROW_RIGHT, () => {
        if (o.current || c || a) return;
        o.current = !0;
        const e = D(g + R);
        (f(e), x(e), (m.current = e - B), j(Math.round(((e - B) * y) / 100)));
      }),
      (0, us.useEffect)(() => {
        const e = (e) => {
          (e.code !== G.ARROW_LEFT && e.code !== G.ARROW_RIGHT) || (o.current = !1);
        };
        return (window.addEventListener("keyup", e), () => window.removeEventListener("keyup", e));
      }, []),
      (0, us.useEffect)(() => {
        N.changeSelectedLevels(S);
      }, [S, N]),
      "disabled" === v
        ? null
        : (0, ms.jsxs)("div", {
            ref: _,
            className: sa(Es, n),
            onMouseDown: O,
            onClick: L,
            children: [
              (0, ms.jsx)("div", {
                ref: u,
                className: sa(Ts, e === Os.down && Ls, i?.pointer),
                onMouseDown: (e) => {
                  (e.stopPropagation(), k({ event: "grab" }), O());
                },
                onMouseEnter: function () {
                  c || k({ event: "hover" });
                },
              }),
              !a && (0, ms.jsx)(As, { from: B, steps: ["growing"], step: R }),
            ],
          })
    );
  };
Ds.positions = Os;
var Ws = "LevelSlider_dbac30ca",
  Vs = "LevelSlider_step_fb995ce2",
  Ms = "LevelSlider_completed_5226098c",
  zs = "LevelSlider_label_aecacc79",
  $s = "LevelSlider_labelDynamic_a0abcf78",
  Fs = "LevelSlider_hidden_2d711256",
  Hs = 100,
  Us = () => {
    const e = (0, us.useRef)([]),
      {
        prevValue: a,
        currentValue: t,
        levelsCount: s,
        hasMoved: r,
        maxValueAchieved: n,
        setMaxValueAchieved: i,
        levelsPassed: o,
      } = hs(),
      l = s + 1,
      c = Math.round((a * s) / Hs),
      d = Math.round((t * s) / Hs);
    return (0, ms.jsx)("div", {
      className: Ws,
      style: { width: 22 * s + "rem" },
      children: (0, ms.jsxs)(ze, {
        size: Ga.large,
        value: Is(o, s),
        maxValue: Hs,
        maxValueAchieved: n,
        children: [
          (0, ms.jsx)(ze.Fill, {}),
          (0, ms.jsx)(Ds, { maxValueAchieved: n, setMaxValueAchieved: i }),
          (0, ms.jsx)(ze.DynamicIndicator, {
            className: sa(t === Hs && Fs, $s),
            staticIndicatorsRefs: e,
            position: de.above,
            transformCurrentValue: (e) =>
              (function (e, a) {
                const t = Te(0, 100, e);
                return Math.floor((t / 100) * a);
              })(e, l),
          }),
          (0, ms.jsx)(ze.NumberIndicators, {
            position: de.above,
            count: l,
            classNames: { step: Vs, completed: Ms, stepClassNames: { label: zs } },
            children: (e) =>
              e % 5 == 0 || (e === c && !n) || (c === d && e === d + 1) ? e : void 0,
          }),
        ],
      }),
    });
  },
  Gs = "RewardsList_61e5d0fd",
  qs = "RewardsList_reward_110a9a1e",
  Ks = "RewardsList_rewardInfo_b223a75b",
  Xs = Wt(() => {
    const { model: e } = js(),
      a = e.computes.getRewards(),
      { levelsToBuy: t } = hs();
    return (
      (0, us.useEffect)(() => {
        ct(F, 0);
      }, [t]),
      (0, ms.jsx)("div", {
        className: Gs,
        children: re(a, (e, a) =>
          (0, ms.jsx)(
            "div",
            {
              className: qs,
              "data-id": `${e.id}_${e.bigIcon}_${a}`,
              children: (0, ms.jsx)(I, { ...Xt(e, Ve.S180x135), classNames: { info: Ks } }),
            },
            `${e.id}_${e.bigIcon}_${a}`,
          ),
        ),
      })
    );
  }),
  Zs = {
    base: "Content_c7f39005",
    buttonWrapper: "Content_buttonWrapper_3596c383",
    buttonWrapper__active: "Content_buttonWrapper__active_97efd5f3",
    rewards: "Content_rewards_6623df59",
    mask: "Content_mask_52164205",
    mask__top: "Content_mask__top_650e84e9",
    mask__bottom: "Content_mask__bottom_528835af",
    mask__both: "Content_mask__both_98f564af",
    scrollBar: "Content_scrollBar_c1dabd5f",
    fadeInWithScale: "Content_fadeInWithScale_da09528a",
    slideUp: "Content_slideUp_da09528a",
    blink: "Content_blink_da09528a",
    scale: "Content_scale_da09528a",
    rotate: "Content_rotate_da09528a",
    windowIn: "Content_windowIn_da09528a",
    fadeOut: "Content_fadeOut_da09528a",
    fadeIn: "Content_fadeIn_da09528a",
  },
  Js = Wt(() => {
    const { model: e } = js(),
      a = e.computes.getRewards().length,
      { api: t } = ga(),
      [s, r] = xt(t);
    return (
      (0, us.useEffect)(() => {
        t.recalculateContent();
      }, [a, t]),
      (0, ms.jsxs)("div", {
        className: Zs.base,
        children: [
          (0, ms.jsx)(Us, {}),
          (0, ms.jsxs)("div", {
            className: Zs.rewards,
            children: [
              (0, ms.jsx)("div", {
                className: sa(Zs.mask, Zs[`mask__${bt(s, r)}`]),
                children: (0, ms.jsx)(ia, { children: (0, ms.jsx)(Xs, {}) }),
              }),
              (0, ms.jsx)(da, { classNames: { base: Zs.scrollBar } }),
            ],
          }),
        ],
      })
    );
  }),
  Qs = "Footer_9d3d3a12",
  Ys = "Footer_currency_9b510c1c",
  er = "Footer_footerLabel_e28c9ab3",
  ar = "Footer_currencyIcon_cfcb6dcf",
  tr = Qa.resolve("strings"),
  sr = () => {
    const {
        currentValue: e,
        prevValue: a,
        levelPrice: t,
        levelsCount: s,
        setLevelsToBuy: r,
        levelsToBuy: n,
        levelsPassed: i,
      } = hs(),
      o = at({ currencySize: B.medium }, { large: { currencySize: B.large } });
    return (
      (0, us.useEffect)(() => {
        const t = Math.round((a * s) / 100),
          n = Math.round((e * s) / 100);
        r(n === t ? 1 : n - i);
      }, [a, e, s, r, i]),
      (0, ms.jsxs)("div", {
        className: Qs,
        children: [
          (0, ms.jsx)(_a, {
            text: tr.pluralOrEmpty("battle_pass.battlePassBuyLevels.levelsSelected", n),
            upgradeLegacy: !0,
            params: { count: n },
            className: er,
          }),
          (0, ms.jsx)(c, {
            classNames: { base: Ys, icon: ar },
            type: je.gold,
            size: o.currencySize,
            reverse: !0,
            children: n * t,
          }),
        ],
      })
    );
  },
  rr = "App_848b5de0",
  nr = "App_background_d5285348",
  ir = "App_shadow_b96f6299",
  or = "App_content_3a6c6ebb",
  lr = "App_contentContainer_dc3584c8",
  cr = "App_footer_7b1985",
  dr = "App_bottomLip_64987100",
  _r = "App_title_536f5f20",
  ur = Qa.resolve("strings"),
  mr = Wt(() => {
    const { model: e, controls: a } = js(),
      {
        isWalletAvailable: t,
        levelsPassed: s,
        levelsTotal: r,
        chapterID: n,
        levelPrice: i,
        purchaseAbortedCount: o,
      } = e.root.get(),
      l = m();
    (O(l.goBack), At(G.SPACE, l.goBack));
    const c = {
      backgroundImage: `url(${is(R.images.gui.maps.icons.battlePass.backgrounds.chapter_general, n)})`,
    };
    return (0, ms.jsx)(bs, {
      levelsCount: r,
      levelPrice: i,
      levelsPassed: s,
      children: (0, ms.jsxs)("div", {
        className: rr,
        children: [
          (0, ms.jsx)("div", { style: c, className: nr }),
          (0, ms.jsx)("div", { className: ir }),
          (0, ms.jsxs)("div", {
            className: or,
            children: [
              (0, ms.jsx)(ys, {
                chapter: n,
                subTitle: ur.readOrEmpty("battle_pass.battlePassBuyView.descr"),
                className: _r,
              }),
              (0, ms.jsx)("div", {
                className: lr,
                children: (0, ms.jsx)(dt, { children: (0, ms.jsx)(Js, {}) }),
              }),
              (0, ms.jsxs)("div", {
                className: cr,
                children: [
                  (0, ms.jsx)("div", { className: dr }),
                  (0, ms.jsx)(sr, {}),
                  (0, ms.jsx)(xs, {
                    onAccept: a.buy,
                    onCancel: l.goBack,
                    isWalletAvailable: t,
                    purchaseAbortedCount: o,
                  }),
                ],
              }),
            ],
          }),
        ],
      }),
    });
  }),
  pr = () =>
    (0, ms.jsx)(Ss, {
      options: { rootId: R.aliases.battle_pass.BuyLevels("resId") },
      children: (0, ms.jsx)(mr, {}),
    }),
  [hr, br] = He()(({ observableModel: e }) => {
    const a = {
        levels: e.object(),
        nowRewards: e.array("nowRewards.items"),
        futureRewards: e.array("futureRewards.items"),
      },
      t = xa(() => a.nowRewards.get(), { equals: _ }),
      s = xa(() => a.futureRewards.get(), { equals: _ });
    return { ...a, computes: { nowRewards: t, futureRewards: s } };
  }, Ne),
  fr = {
    base: "GroupTitle_eaeb27ea",
    iconContainer: "GroupTitle_iconContainer_53d16b22",
    icon: "GroupTitle_icon_fd08ab04",
    fadeInWithScale: "GroupTitle_fadeInWithScale_bdc8a0f5",
    slideUp: "GroupTitle_slideUp_bdc8a0f5",
    blink: "GroupTitle_blink_bdc8a0f5",
    scale: "GroupTitle_scale_bdc8a0f5",
    rotate: "GroupTitle_rotate_bdc8a0f5",
    windowIn: "GroupTitle_windowIn_bdc8a0f5",
    fadeOut: "GroupTitle_fadeOut_bdc8a0f5",
    fadeIn: "GroupTitle_fadeIn_bdc8a0f5",
  },
  gr = Qa.resolve("images"),
  vr = "checked",
  xr = "locked",
  wr = "x32",
  Cr = "x48",
  yr = "x96",
  Sr = ({ type: e, className: a = "", title: t = "" }) => {
    const s = V(at({ iconSize: wr }, { medium: { iconSize: Cr } }).iconSize, yr),
      r = gr.readOrEmpty(`battlePass.buy.rewards.${e}_${s}`);
    return (0, ms.jsxs)("div", {
      className: sa(fr.base, fr[`base__${e}`], a),
      children: [
        (0, ms.jsx)("div", {
          className: fr.iconContainer,
          children: (0, ms.jsx)("div", {
            className: fr.icon,
            style: { backgroundImage: `url(${r})` },
          }),
        }),
        (0, ms.jsx)("span", { children: t }),
      ],
    });
  },
  jr = "GroupRewards_46776305",
  Ir = "GroupRewards_item_17e76f62",
  Nr = "GroupRewards_title_a5115b64",
  kr = ({ rewards: e, className: a }) =>
    (0, ms.jsx)("div", {
      className: sa(jr, a),
      children: re(e, (e, a) =>
        (0, ms.jsx)(
          "div",
          {
            className: Ir,
            children: (0, ms.jsx)(L, { ...Xt(e, ra.Big, !0), classNames: { title: Nr } }),
          },
          `reward_${a}_${e.name}`,
        ),
      ),
    }),
  Pr = "RewardsBlock_479e00eb",
  Rr = "RewardsBlock_title_677ec3f0",
  Br = "RewardsBlock_rewards_e9af771e",
  Ar = ({ type: e, rewards: a, className: t = "", title: s = "" }) =>
    (0, ms.jsxs)("div", {
      className: sa(Pr, t),
      children: [
        (0, ms.jsx)(Sr, { type: e, className: Rr, title: s }),
        (0, ms.jsx)(kr, { rewards: a, className: Br }),
      ],
    }),
  Er = {
    base: "Content_690d4e59",
    base__hasScroll: "Content_base__hasScroll_d4326fda",
    mask: "Content_mask_3c273268",
    mask__top: "Content_mask__top_49c2b256",
    mask__bottom: "Content_mask__bottom_73ebbe0b",
    mask__both: "Content_mask__both_5a3cae0c",
    content: "Content_4089e099",
    rewardsBlock: "Content_rewardsBlock_da09528a",
    scrollBar: "Content_scrollBar_1436f72c",
    fadeInWithScale: "Content_fadeInWithScale_da09528a",
    slideUp: "Content_slideUp_da09528a",
    blink: "Content_blink_da09528a",
    scale: "Content_scale_da09528a",
    rotate: "Content_rotate_da09528a",
    windowIn: "Content_windowIn_da09528a",
    fadeOut: "Content_fadeOut_da09528a",
    fadeIn: "Content_fadeIn_da09528a",
  },
  Tr = Qa.resolve("strings"),
  Lr = Wt(({ className: e }) => {
    const { model: a } = br(),
      t = a.computes.nowRewards(),
      s = a.computes.futureRewards(),
      { api: r } = ga();
    C(r);
    const [n, i] = (0, us.useState)(!1),
      [o, l] = xt(r),
      c = (0, us.useCallback)(() => {
        const [e, a] = r.getBounds();
        i(e !== a);
      }, [r]);
    return (
      (0, us.useEffect)(
        () => (
          r.events.on("resizeHandled", c),
          () => {
            r.events.off("resizeHandled", c);
          }
        ),
        [r.events, c],
      ),
      (0, ms.jsxs)("div", {
        className: sa(Er.base, n && Er.base__hasScroll, e),
        children: [
          (0, ms.jsx)(ia, {
            classNames: { content: Er.content, wrapper: sa(Er.mask, Er[`mask__${bt(o, l)}`]) },
            children: (0, ms.jsxs)("div", {
              className: Er.rewardsBlock,
              children: [
                t.length > 0 &&
                  (0, ms.jsx)(Ar, {
                    type: vr,
                    rewards: t,
                    title: Tr.readOrEmpty("battle_pass.battlePassBuyView.reward.titleNowRewards"),
                  }),
                s.length > 0 &&
                  (0, ms.jsx)(Ar, {
                    type: xr,
                    rewards: s,
                    title: Tr.readOrEmpty(
                      "battle_pass.battlePassBuyView.reward.titleFutureRewards",
                    ),
                  }),
              ],
            }),
          }),
          (0, ms.jsx)(da, { classNames: { base: Er.scrollBar } }),
        ],
      })
    );
  }),
  Or = "MoreRewards_3800bba1",
  Dr = "MoreRewards_content_797d0c7d",
  Wr = "MoreRewards_background_485149b6",
  Vr = Wt(() => {
    const { model: e } = br(),
      { chapterID: a } = e.levels.get(),
      [t, s] = (0, us.useState)(!1);
    (O(m().goBack),
      (0, us.useEffect)(() => {
        (async () => {
          (await Yt(), s(!0));
        })();
      }, []));
    const r = is(R.images.gui.maps.icons.battlePass.backgrounds.chapter_general, a);
    return (0, ms.jsxs)("div", {
      className: Or,
      children: [
        (0, ms.jsx)("div", { className: Wr, style: { backgroundImage: `url(${r})` } }),
        t && (0, ms.jsx)(dt, { children: (0, ms.jsx)(Lr, { className: Dr }) }),
      ],
    });
  }),
  Mr = {
    base__x60x60: "Emblem_base__x60x60_d8756e36",
    base__x100x100: "Emblem_base__x100x100_547cf3ad",
    base__x160x160: "Emblem_base__x160x160_c9c06954",
    base__x200x200: "Emblem_base__x200x200_2ddeb5ee",
    base__x240x240: "Emblem_base__x240x240_308c1aa9",
    base__x360x360: "Emblem_base__x360x360_98f20cf9",
    shield: "Emblem_shield_451cf2c9",
    icon: "Emblem_icon_73d84087",
    shield__x74x74: "Emblem_shield__x74x74_a298d905",
    shield__x120x120: "Emblem_shield__x120x120_c8aa5234",
    shield__x200x200: "Emblem_shield__x200x200_f1ed9db0",
    shield__x260x260: "Emblem_shield__x260x260_ef1c262b",
    shield__x300x300: "Emblem_shield__x300x300_7c6d6f97",
    shield__x456x456: "Emblem_shield__x456x456_c818292e",
    icon__x28x28: "Emblem_icon__x28x28_6ea3e635",
    icon__x48x48: "Emblem_icon__x48x48_f2526f88",
    icon__x60x60: "Emblem_icon__x60x60_628dbf9a",
    icon__x80x80: "Emblem_icon__x80x80_34079478",
    icon__x100x100: "Emblem_icon__x100x100_e8181a63",
    icon__x120x120: "Emblem_icon__x120x120_c8aa5234",
    icon__x160x160: "Emblem_icon__x160x160_aec06e5c",
    fadeInWithScale: "Emblem_fadeInWithScale_9b4d607c",
    slideUp: "Emblem_slideUp_9b4d607c",
    blink: "Emblem_blink_9b4d607c",
    scale: "Emblem_scale_9b4d607c",
    rotate: "Emblem_rotate_9b4d607c",
    windowIn: "Emblem_windowIn_9b4d607c",
    fadeOut: "Emblem_fadeOut_9b4d607c",
    fadeIn: "Emblem_fadeIn_9b4d607c",
  },
  zr = "x100x100",
  $r = "x160x160",
  Fr = "x200x200",
  Hr = "x240x240",
  Ur = "x360x360",
  Gr = "x74x74",
  qr = "x120x120",
  Kr = "x200x200",
  Xr = "x260x260",
  Zr = "x300x300",
  Jr = "x456x456",
  Qr = "x600x600",
  Yr = "x912x912",
  en = "x28x28",
  an = "x48x48",
  tn = "x60x60",
  sn = "x80x80",
  rn = "x100x100",
  nn = "x120x120",
  on = "x160x160",
  ln = "x240x240",
  cn = "x320x320",
  dn = Qa.resolve("images"),
  _n = function ({
    iconSize: e,
    shieldSize: a,
    containerSize: t,
    chapterID: s,
    bpPurchased: r,
    className: n = "",
  }) {
    const i = r ? "purchased" : "basic",
      o = String(s).slice(-1),
      l = a === Gr ? qr : a === qr ? Xr : a === Kr ? Jr : a === Xr || a === Zr ? Qr : Yr,
      c =
        e === en
          ? tn
          : e === an
            ? rn
            : e === tn
              ? nn
              : e === sn
                ? on
                : e === rn || e === nn
                  ? ln
                  : cn,
      d =
        dn.readOrEmpty(`battlePass.emblem.shield.c_${s}.${i}.${V(a, l)}`, "silent") ||
        dn.readOrEmpty(`battlePass.emblem.shield.default.${i}.${a}`),
      _ =
        dn.readOrEmpty(`battlePass.emblem.icon.c_${s}.${i}.${V(e, c)}`, "silent") ||
        dn.readOrEmpty(`battlePass.emblem.icon.default_${o}.${i}.${e}`);
    return (0, ms.jsxs)("div", {
      className: sa(Mr.base, Mr[`base__${t}`], n),
      children: [
        (0, ms.jsx)("div", {
          className: sa(Mr.shield, Mr[`shield__${a}`]),
          style: { backgroundImage: `url(${d})` },
        }),
        (0, ms.jsx)("div", {
          className: sa(Mr.icon, Mr[`icon__${e}`]),
          style: {
            backgroundImage: `url(${s > 0 ? _ : dn.readOrEmpty(`battlePass.emblem.icon.not_chosen.${V(e, tn)}`)})`,
          },
        }),
      ],
    });
  },
  [un, mn] = He()(
    ({ observableModel: e }) => {
      const a = {
          root: e.object(),
          main: e.primitives([
            "state",
            "shopOfferDiscount",
            "isShopOfferAvailable",
            "isWalletAvailable",
          ]),
          rewards: e.array("rewards"),
          chapters: e.array("chapters"),
          package: e.array("package"),
        },
        t = xa(() => a.rewards.get().topPriorityRewards.items, { equals: _ }),
        s = xa(() => a.rewards.get().prevTopPriorityRewards.items, { equals: _ }),
        r = xa(() => a.rewards.get().nowRewards.items, { equals: _ }),
        n = xa(() => a.rewards.get().futureRewards.items, { equals: _ }),
        i = xa(() => a.package.get().starterPackRewards.items, { equals: _ }),
        o = xa(() => {
          const { chapterID: e } = a.package.get(),
            t = a.chapters.get();
          return {
            chapterIDs: [
              e,
              ...It(
                t,
                ({ chapterID: a }) => a !== e,
                ({ chapterID: e }) => e,
              ),
            ],
            amount: ea(t, ({ hasStarterPack: e }) => e).length,
          };
        }),
        l = xa(
          (e) =>
            ve(a.chapters.get(), ({ hasStarterPack: a, chapterID: t }) => a && t === e)
              ?.hasStarterPack,
        ),
        c = xa(() => ea(a.chapters.get(), ({ isExtra: e }) => !e));
      return {
        ...a,
        computes: {
          topPriorityRewards: t,
          prevTopPriorityRewards: s,
          nowRewards: r,
          futureRewards: n,
          starterPackInfo: o,
          starterPackRewards: i,
          hasStarterPackInChapter: l,
          regularChapters: c,
        },
      };
    },
    ({ model: e, externalModel: a }) => ({
      shopOffer: a.createCallbackNoArgs("onShopOfferClick"),
      buy: a.createCallbackNoArgs("onBuyClick"),
      togglePurchaseWithLevels: a.createCallbackNoArgs("onChangePurchaseWithLevels"),
      closeClick: a.createCallbackNoArgs("onShopOfferClick"),
      showRewardsClick: a.createCallbackNoArgs("onShowRewardsClick"),
    }),
  ),
  pn = "PurchaseBlock_fa4dd8be",
  hn = "PurchaseBlock_button_3b8b9877",
  bn = "PurchaseBlock_previousPrice_1e77a9b2",
  fn = "PurchaseBlock_currentPrice_c4a7499d",
  gn = "PurchaseBlock_currency_a51b98a4",
  vn = "PurchaseBlock_actionLip_63994768",
  xn = Qa.resolve("strings"),
  wn = Wt(function ({ isPriceUpdateAnimation: e }) {
    const { model: a, controls: t } = mn(),
      { isWalletAvailable: s } = a.root.get(),
      { price: r, prevPrice: n } = a.package.get(),
      i = at(
        { currencySize: B.medium, buttonSize: Se.small },
        { medium: { currencySize: B.extraLarge, buttonSize: Se.large } },
      );
    return (0, ms.jsxs)("div", {
      className: pn,
      children: [
        (0, ms.jsx)("div", { className: vn }),
        e
          ? (0, ms.jsx)("div", {
              className: bn,
              children: (0, ms.jsx)(c, {
                classNames: { base: gn },
                type: je.gold,
                size: i.currencySize,
                children: n,
              }),
            })
          : (0, ms.jsx)("div", {
              className: fn,
              children: (0, ms.jsx)(c, {
                classNames: { base: gn },
                type: je.gold,
                size: i.currencySize,
                children: r,
              }),
            }),
        (0, ms.jsx)(yt, {
          theme: w.primary,
          size: i.buttonSize,
          className: hn,
          onClick: t.buy,
          disabled: !s,
          "data-test-id": "buyButton",
          children: xn.readOrEmpty("battle_pass.battlePassBuyView.confirm.btnBuy"),
        }),
      ],
    });
  }),
  Cn = "DiscountIcon_932f671c",
  yn = "DiscountIcon_icon_655d7c11",
  Sn = "DiscountIcon_highlight_75d6adf";
function jn({ className: e = "" }) {
  return (0, ms.jsxs)("div", {
    className: sa(Cn, e),
    children: [(0, ms.jsx)("div", { className: yn }), (0, ms.jsx)("div", { className: Sn })],
  });
}
var In = "Logos_1ed97e35",
  Nn = "Logos_logoWrapper_826e9a4f",
  kn = "Logos_logo_ada5f291",
  Pn = "Logos_starterPack_f4dabb81",
  Rn = Qa.resolve("images"),
  Bn = (e) => {
    const a = String(e).slice(-1);
    return (
      Rn.readOrEmpty(`battlePass.emblem.icon.c_${e}.purchased.${on}`, "silent") ||
      Rn.readOrEmpty(`battlePass.emblem.icon.default_${a}.purchased.${on}`)
    );
  },
  An = R.strings.battle_pass.battlePassBuyView.confirm.shopOfferBlock;
var En = Wt(function ({ className: e = "" }) {
    const {
        model: { computes: a },
      } = mn(),
      { chapterIDs: t, amount: s } = a.starterPackInfo();
    return (0, ms.jsxs)("div", {
      className: sa(In, e),
      children: [
        t.map((e, a) =>
          (0, ms.jsx)(
            "div",
            {
              className: Nn,
              style: { zIndex: t.length - a },
              children: (0, ms.jsx)("div", {
                className: kn,
                style: { backgroundImage: `url(${Bn(e)})` },
              }),
            },
            e,
          ),
        ),
        Boolean(s) &&
          (0, ms.jsx)(aa, { classMix: Pn, text: An.packsAmount(), binding: { amount: s } }),
      ],
    });
  }),
  Tn = "ShopOfferBlock_5d538f0f",
  Ln = "ShopOfferBlock_logos_c4a5c492",
  On = "ShopOfferBlock_headline_333a5398",
  Dn = "ShopOfferBlock_text_83d7e7fc",
  Wn = "ShopOfferBlock_discount_c7eeef37",
  Vn = "ShopOfferBlock_title_7245add2",
  Mn = "ShopOfferBlock_description_ef059d17",
  zn = "ShopOfferBlock_button_4790b6d6",
  $n = R.strings.battle_pass.battlePassBuyView.confirm.shopOfferBlock;
var Fn = Wt(function ({ className: e = "" }) {
    const { model: a, controls: t } = mn(),
      s = a.computes.regularChapters(),
      r = Ee(() => {
        t.shopOffer();
      }),
      n = at({ buttonSize: Se.small }, { medium: { buttonSize: Se.large } });
    return (0, ms.jsxs)("div", {
      className: sa(Tn, e),
      children: [
        Boolean(s.length) && (0, ms.jsx)(En, { className: Ln }),
        (0, ms.jsxs)("div", {
          className: On,
          children: [
            (0, ms.jsx)(_a, {
              upgradeLegacy: !0,
              className: Dn,
              text: $n.headline(),
              params: { count: s.length },
            }),
            (0, ms.jsx)(jn, { className: Wn }),
          ],
        }),
        (0, ms.jsx)(_a, { upgradeLegacy: !0, className: Vn, text: $n.title() }),
        (0, ms.jsx)(_a, { upgradeLegacy: !0, className: Mn, text: $n.description() }),
        (0, ms.jsx)(yt, { size: n.buttonSize, onClick: r, className: zn, children: $n.buy() }),
      ],
    });
  }),
  Hn = "AnimatedReward_1789d927",
  Un = ({ children: e, animationConfig: a, className: t }) => {
    const s = Ra(a);
    return (0, ms.jsx)(i.div, { style: s, className: sa(Hn, t), children: e });
  },
  Gn = {
    base: "Rewards_e0c7ea28",
    descriptionText: "Rewards_descriptionText_70d3a019",
    priorityRewards: "Rewards_priorityRewards_8561c5b0",
    priorityRewards__rewardsButtonVisible: "Rewards_priorityRewards__rewardsButtonVisible_e006900",
    rewardsWrapper: "Rewards_rewardsWrapper_e727c56d",
    buttonWrapper: "Rewards_buttonWrapper_fd4269bd",
    rewardBtn: "Rewards_rewardBtn_c25bebb2",
    rewardBtn__currentRewardsAnimation: "Rewards_rewardBtn__currentRewardsAnimation_4dddd688",
    "fade-in": "Rewards_fade-in_405577a5",
    buttonContent: "Rewards_buttonContent_5599209b",
    fadeInWithScale: "Rewards_fadeInWithScale_405577a5",
    slideUp: "Rewards_slideUp_405577a5",
    blink: "Rewards_blink_405577a5",
    scale: "Rewards_scale_405577a5",
    rotate: "Rewards_rotate_405577a5",
    windowIn: "Rewards_windowIn_405577a5",
    fadeOut: "Rewards_fadeOut_405577a5",
    fadeIn: "Rewards_fadeIn_405577a5",
  },
  qn = (e, a, t) => ({
    from: { opacity: 0 },
    to: { opacity: 1 },
    delay: 100 * e,
    config: { duration: 100 },
    onStart: () => {
      a();
    },
    reset: t,
  }),
  Kn = Qa.resolve("strings"),
  Xn = Wt(({ isCheckboxAnimationActive: e, isPrevious: a = !1, className: t }) => {
    const { model: s } = mn(),
      { chapterID: r, isPurchaseWithLevels: n } = s.package.get(),
      o =
        s.computes.nowRewards().length +
        s.computes.futureRewards().length -
        s.computes.topPriorityRewards().length,
      l = s.computes.topPriorityRewards(),
      c = s.computes.prevTopPriorityRewards(),
      d = a ? c : l,
      _ = o > 0,
      u = () => {
        ue.sound(R.sounds.bp_reward());
      },
      { breakpoint: p } = Me(),
      h = p.weight < _e.medium.weight ? ra.Small : ra.Big,
      b = Ra(qn(6, u)),
      f = m();
    return (0, ms.jsxs)("div", {
      className: sa(Gn.base, t),
      children: [
        (0, ms.jsx)("div", {
          className: Gn.descriptionText,
          children:
            a !== n
              ? Kn.readOrEmpty("battle_pass.battlePassBuyView.confirm.descriptionCheckboxChecked")
              : Kn.readOrEmpty("battle_pass.battlePassBuyView.confirm.description"),
        }),
        (0, ms.jsxs)("div", {
          className: Gn.rewardsWrapper,
          children: [
            (0, ms.jsx)("div", {
              className: sa(Gn.priorityRewards, _ && Gn.priorityRewards__rewardsButtonVisible),
              children: re(d, (e, t) =>
                a
                  ? (0, us.createElement)(L, { ...Xt(e, h), key: `${e.name}_${t}` })
                  : (0, ms.jsx)(
                      Un,
                      { animationConfig: qn(t, u), children: (0, ms.jsx)(L, { ...Xt(e, h) }) },
                      `${e.name}_${t}`,
                    ),
              ),
            }),
            _ &&
              (0, ms.jsx)(i.div, {
                style: b,
                children: (0, ms.jsx)("div", {
                  className: Gn.buttonWrapper,
                  children: (0, ms.jsx)(yt, {
                    theme: w.secondary,
                    size: Se.large,
                    className: sa(Gn.rewardBtn, e && Gn.rewardBtn__currentRewardsAnimation),
                    classNames: { content: Gn.buttonContent },
                    onClick: () => f.push(ls.battlePass.buyPassRewards, { packageID: r }),
                    children: (0, ms.jsx)(aa, {
                      text: Kn.readOrEmpty("battle_pass.battlePassBuyView.btnRewards"),
                      binding: { count: o },
                      classMix: Gn.text,
                    }),
                  }),
                }),
              }),
          ],
        }),
      ],
    });
  }),
  Zn = {
    base: "StarterPack_231839be",
    presentLogo: "StarterPack_presentLogo_cb1c6f84",
    presentLogo__x36x36: "StarterPack_presentLogo__x36x36_15fc148b",
    presentLogo__x52x52: "StarterPack_presentLogo__x52x52_f480a652",
    equalLogo: "StarterPack_equalLogo_407c8a9c",
    rewardsWrapper: "StarterPack_rewardsWrapper_bf86c609",
    rewards: "StarterPack_rewards_231839be",
    fadeInWithScale: "StarterPack_fadeInWithScale_e09c33a3",
    slideUp: "StarterPack_slideUp_e09c33a3",
    blink: "StarterPack_blink_e09c33a3",
    scale: "StarterPack_scale_e09c33a3",
    rotate: "StarterPack_rotate_e09c33a3",
    windowIn: "StarterPack_windowIn_e09c33a3",
    fadeOut: "StarterPack_fadeOut_e09c33a3",
    fadeIn: "StarterPack_fadeIn_e09c33a3",
  },
  Jn = Qa.resolve("strings"),
  Qn = "x36x36",
  Yn = "x52x52",
  ei = Wt(function ({ starterPackRewards: e, presentSize: a, rewardSize: t, classNames: s }) {
    return (0, ms.jsxs)("div", {
      className: Zn.base,
      children: [
        (0, ms.jsx)("div", {
          className: sa(Zn.presentLogo, Zn[`presentLogo__${a}`], s?.presentLogo),
        }),
        (0, ms.jsx)("div", {
          className: sa(Zn.equalLogo, s?.equalLogo),
          children: Jn.readOrEmpty("battle_pass.progression.footer.starter_pack.equal"),
        }),
        (0, ms.jsx)("div", {
          className: Zn.rewardsWrapper,
          children: (0, ms.jsx)("div", {
            className: Zn.rewards,
            children: re(e, (e, a) =>
              (0, ms.jsx)(L, { ...Xt(e, t), className: s?.reward }, `reward_${e.name}_${a}`),
            ),
          }),
        }),
      ],
    });
  }),
  ai = "StarterPack_packDescription_e09c33a3",
  ti = "StarterPack_purchaseText_67051b2",
  si = "StarterPack_presentLogo_f1509f42",
  ri = "StarterPack_equalLogo_4d2bea9f",
  ni = Qa.resolve("strings"),
  ii = Wt(function () {
    const { model: e } = mn(),
      a = e.computes.starterPackRewards(),
      { breakpoint: t } = Me(),
      s = t.weight < _e.medium.weight ? ra.Small : ra.Big;
    return (0, ms.jsxs)(ms.Fragment, {
      children: [
        (0, ms.jsx)(_a, {
          text: ni.readOrEmpty("battle_pass.battlePassBuyView.confirm.starterPack.description"),
          upgradeLegacy: !0,
          params: {
            purchaseText: (0, ms.jsx)("span", {
              className: ti,
              children: ni.readOrEmpty(
                "battle_pass.battlePassBuyView.confirm.starterPack.purchaseText",
              ),
            }),
          },
          className: ai,
        }),
        (0, ms.jsx)(ei, {
          starterPackRewards: a,
          presentSize: Yn,
          rewardSize: s,
          classNames: { presentLogo: si, equalLogo: ri },
        }),
      ],
    });
  }),
  oi = {
    base: "PassContent_1cb8450b",
    contentWrapper: "PassContent_contentWrapper_6bd43d6a",
    contentWrapper__noShopOffer: "PassContent_contentWrapper__noShopOffer_3c8d5049",
    content: "PassContent_content_c067e9cf",
    emblem: "PassContent_emblem_bf66736c",
    chapterInfo: "PassContent_chapterInfo_3efcc8f4",
    chapterName: "PassContent_chapterName_b21f7a0e",
    check: "PassContent_check_a557a239",
    checkIcon: "PassContent_checkIcon_2ddd3576",
    checkboxLabel: "PassContent_checkboxLabel_968825b",
    previousRewards: "PassContent_previousRewards_3344ac4c",
    fadeOut: "PassContent_fadeOut_f51cf613",
    content__rewardsUpdateAnimation: "PassContent_content__rewardsUpdateAnimation_f51cf613",
    currentRewards: "PassContent_currentRewards_cc1995e8",
    fadeIn: "PassContent_fadeIn_f51cf613",
    checkbox: "PassContent_checkbox_a0d760a8",
    starterPack: "PassContent_starterPack_bcf3e072",
    offerBack: "PassContent_offerBack_a71885da",
    offerWrapper: "PassContent_offerWrapper_e8393a4",
    offer: "PassContent_offer_d09e2495",
    fadeInWithScale: "PassContent_fadeInWithScale_f51cf613",
    slideUp: "PassContent_slideUp_f51cf613",
    blink: "PassContent_blink_f51cf613",
    scale: "PassContent_scale_f51cf613",
    rotate: "PassContent_rotate_f51cf613",
    windowIn: "PassContent_windowIn_f51cf613",
  },
  li = Qa.resolve("strings"),
  ci = Qa.resolve("images"),
  di = Wt(() => {
    const [e, a] = (0, us.useState)(!1),
      t = (0, us.useRef)(!1),
      { model: s, controls: r } = mn(),
      { chapterID: n, remainingLevelsCount: i, isPurchaseWithLevels: o } = s.package.get(),
      l = s.computes.hasStarterPackInChapter(n),
      c = s.main.isShopOfferAvailable.get(),
      d = m();
    At(D.ESCAPE, () => d.goBack());
    const _ = (() => {
      const e = String(n).slice(-1),
        a = `battlePass.backgrounds.chapter_general.c_${n}`,
        t = `battlePass.backgrounds.chapter_general.default_${e}`;
      return ci.readOrEmpty(a, "silent") || ci.readOrEmpty(t);
    })();
    (0, us.useEffect)(() => {
      if (t.current)
        return (
          a(!0),
          ct(() => {
            a(!1);
          }, 300)
        );
      t.current = !0;
    }, [o, t]);
    const u = at(
      { iconSize: rn, shieldSize: Xr, containerSize: Fr },
      {
        medium: { iconSize: nn, shieldSize: Zr, containerSize: Hr },
        large: { iconSize: on, shieldSize: Jr, containerSize: Ur },
      },
    );
    return (0, ms.jsxs)("div", {
      className: oi.base,
      style: { backgroundImage: `url(${_})` },
      children: [
        (0, ms.jsx)("div", {
          className: sa(
            oi.contentWrapper,
            !c && oi.contentWrapper__noShopOffer,
            e && oi.contentWrapper__rewardsUpdateAnimation,
          ),
          children: (0, ms.jsxs)("div", {
            className: oi.content,
            children: [
              (0, ms.jsx)("div", {
                className: oi.emblem,
                children: (0, ms.jsx)(_n, {
                  iconSize: u.iconSize,
                  shieldSize: u.shieldSize,
                  containerSize: u.containerSize,
                  bpPurchased: !0,
                  chapterID: n,
                }),
              }),
              (0, ms.jsxs)("div", {
                className: oi.chapterInfo,
                children: [
                  (0, ms.jsx)("div", {
                    className: oi.chapterName,
                    children: li.readOrEmpty(`battle_pass.chapter.fullName.c_${n}`),
                  }),
                  i > 0 &&
                    (0, ms.jsx)("div", {
                      className: oi.checkbox,
                      children: (0, ms.jsx)(Q, {
                        checked: o,
                        onCheckedChange: r.togglePurchaseWithLevels,
                        classNames: { checkIcon: oi.checkIcon, check: oi.check },
                        "data-test-id": "buyLevelsCheckbox",
                        children: (0, ms.jsx)(_a, {
                          text: li.pluralOrEmpty(
                            "battle_pass.battlePassBuyView.confirm.checkbox.stage",
                            i,
                          ),
                          upgradeLegacy: !0,
                          params: { stagesNumber: i },
                          className: oi.checkboxLabel,
                        }),
                      }),
                    }),
                  e
                    ? (0, ms.jsx)(Xn, {
                        isCheckboxAnimationActive: e,
                        className: oi.previousRewards,
                        isPrevious: !0,
                      })
                    : (0, ms.jsx)(Xn, {
                        isCheckboxAnimationActive: e,
                        className: oi.currentRewards,
                      }),
                  (0, ms.jsx)("div", {
                    className: oi.starterPack,
                    children: l && (0, ms.jsx)(ii, {}),
                  }),
                  (0, ms.jsx)(wn, { isPriceUpdateAnimation: e }),
                ],
              }),
            ],
          }),
        }),
        c &&
          (0, ms.jsxs)(ms.Fragment, {
            children: [
              (0, ms.jsx)("div", { className: oi.offerBack }),
              (0, ms.jsx)("div", {
                className: oi.offerWrapper,
                children: (0, ms.jsx)("div", {
                  className: oi.offer,
                  children: (0, ms.jsx)(Fn, {}),
                }),
              }),
            ],
          }),
      ],
    });
  }),
  _i = { context: "model.rewards", rootId: R.aliases.battle_pass.BuyPass("resId") },
  ui = Wt(() => {
    const { model: e } = mn();
    switch (e.main.state.get()) {
      case "buyState":
      default:
        return (0, ms.jsx)(di, {});
      case "rewardsState":
        return (0, ms.jsx)(hr, { options: _i, children: (0, ms.jsx)(Vr, {}) });
    }
  }),
  mi = () =>
    (0, ms.jsx)(un, {
      options: { rootId: R.aliases.battle_pass.BuyPass("resId") },
      children: (0, ms.jsx)(ui, {}),
    }),
  pi = [
    { emblem: { delay: 0, diff: 60, duration: 350 } },
    { deadline: { delay: 30 } },
    { chapterName: { delay: 60 } },
    { finalReward: { delay: 90 } },
    { buttonsGroup: { delay: 120 } },
  ],
  hi = (e = 0, a = 30, t = 200) => ({
    from: { opacity: 0, transform: `translateY(${a}rem)` },
    to: { opacity: 1, transform: "translateY(0rem)" },
    config: { duration: t, easing: lt.easeInOutCubic },
    delay: e,
  }),
  bi = Qa.resolve("images"),
  fi = Qa.resolve("videos"),
  [gi, vi] = He()(
    ({ observableModel: e }) => {
      const a = e.array("chapters"),
        t = {
          root: e.object(),
          selectedChapterID: wa.box(0),
          prevChapterIndex: wa.box(0),
          chapters: a,
        },
        s = xa(() => Z(a.get(), ({ isExtra: e }) => e)),
        r = xa(() => Z(a.get(), ({ chapterState: e }) => e === Qt.Active)),
        n = xa(() => Pt(a.get(), ({ chapterState: e }) => e === Qt.Completed)),
        i = xa((e) => ve(a.get(), (a) => a.chapterID === e), { equals: _ }),
        l = xa((e) => {
          const t = ve(a.get(), (a) => a.chapterID === e);
          return { levelProgression: t?.levelProgression || 0, currentLevel: t?.currentLevel || 0 };
        }),
        c = xa(() => ea(t.chapters.get(), (e) => !e.isExtra), { equals: _ }),
        d = xa(() => ea(t.chapters.get(), (e) => !e.isExtra && !e.isPostProgression), {
          equals: _,
        }),
        u = xa(() => ea(c(), (e) => e.chapterState === Qt.Completed).length, { equals: _ }),
        m = xa(() => ea(t.chapters.get(), (e) => e.isExtra)),
        p = xa(() => ea(t.chapters.get(), (e) => e.isPostProgression)),
        h = [2],
        b = xa(
          () => {
            const e = ve(t.chapters.get(), ({ chapterID: e }) => e === t.selectedChapterID.get());
            return e || x(t.chapters.get(), t.prevChapterIndex.get());
          },
          { equals: _ },
        ),
        f = xa(
          () => {
            const { timeLeft: e, isExtra: a } = b();
            return a ? Ke(e).days < 3 : Ke(e).days < 20;
          },
          { equals: _ },
        ),
        g = xa(() => [...(s() ? m() : []), ...d(), ...p()]),
        v = xa(
          () => {
            const e = [];
            return (
              re(g(), (a) => {
                const t = String(a.chapterID).slice(-1),
                  s = `battlePass.backgrounds.chapter_choice.c_${a.chapterID}`,
                  r = `battlePass.backgrounds.chapter_choice.default_${t}`,
                  n = `battle_pass.chapter_choice.c_${a.chapterID}.idle`;
                e.push({
                  chapter: a.chapterID,
                  mainBg: bi.readOrEmpty(s, "silent") || bi.readOrEmpty(r),
                  idleBg: fi.readOrEmpty(n, "silent") || "",
                });
              }),
              e
            );
          },
          { equals: _ },
        );
      return {
        ...t,
        computes: {
          getChapterById: i,
          getProgressionInfoByChapterId: l,
          hasExtra: s,
          hasActive: r,
          detailedTimer: f,
          isCompleted: n,
          regularChapters: c,
          extraChapters: m,
          regularChaptersCompleteCount: u,
          chaptersLineInfo: () =>
            o(
              c(),
              (e, { chapterID: a, chapterState: t }, s) => (
                h.includes(s + 1) || e.push({ chapterID: a, chapterState: t }),
                e
              ),
              [],
            ),
          sortedChapters: g,
          selectedChapter: b,
          backgrounds: v,
        },
      };
    },
    ({ externalModel: e, model: a, cleanup: t }) => {
      const s = ca((e) => {
          a.selectedChapterID.set(e);
        }),
        r = ca((e) => {
          a.prevChapterIndex.set(e);
        }),
        n = Ue(
          () => a.root.get().selectedChapter,
          (e) => {
            (s(e), r(e));
          },
          { fireImmediately: !0 },
        );
      return (
        t(() => {
          n();
        }),
        {
          openPreview: e.createCallback((e) => ({ chapterID: e }), "onPreviewClick"),
          openAbout: e.createCallbackNoArgs("onAboutClick"),
          openPointsInfo: e.createCallbackNoArgs("onPointsInfoClick"),
          onViewLoaded: e.createCallbackNoArgs("onViewLoaded"),
          showTankmen: e.createCallback((e) => ({ chapterID: e }), "showTankmen"),
          onChapterSelect: e.createCallback((e) => ({ chapterID: e }), "onChapterSelect"),
          setSelectedChapterID: s,
          setPrevChapterIndex: r,
        }
      );
    },
  ),
  xi = "LoopVideo_cfc6c5cb";
function wi({ src: e, style: a }) {
  const t = (0, us.useRef)(null),
    [s, r] = oe(() => {
      const e = t.current;
      return !e || !e.getCachedKeyframes()?.length || (e.goToAndPlay(0), !1);
    });
  return (
    (0, us.useEffect)(() => (s(), r), []),
    (0, us.useEffect)(() => {
      const e = t.current;
      return () => {
        e && (e.domRef.src = "");
      };
    }, [t]),
    (0, ms.jsx)(K, { src: e, style: a, className: xi, ref: t, autoplay: !0, loop: !0 })
  );
}
var Ci = "Background_d1f724bf",
  yi = "Background_mainBg_b8b64d56",
  Si = "Background_idleBg_30e8ffa",
  ji = Wt(function ({ style: e, i: a, index: t, classNames: s = {} }) {
    const { model: r } = vi(),
      n = r.prevChapterIndex.get(),
      { mainBg: o, idleBg: l } = r.computes.backgrounds()[a],
      { width: c, height: d } = N(),
      _ = Jt(c, d, Ta(), l);
    return (0, ms.jsxs)("div", {
      className: Ci,
      children: [
        (0, ms.jsx)(i.div, {
          className: sa(yi, s?.main),
          style: {
            ...e,
            backgroundImage: `url(${o})`,
            zIndex: a === t ? 3 : a === n ? 2 : 1,
            transform: e.x.to((e) => `translateX(${e}rem)`),
          },
        }),
        a === t &&
          l &&
          (0, ms.jsx)("div", {
            className: sa(Si, s?.idle),
            children: (0, ms.jsx)(wi, { src: l, style: _ }),
          }),
      ],
    });
  }),
  Ii =
    (W.assault,
    W.universal,
    W.break,
    W.sniper,
    W.scout,
    W.support,
    P.lightTank,
    P.mediumTank,
    P.heavyTank,
    P["AT-SPG"],
    P.SPG,
    Ze(1, 12, E),
    "vehicle_types"),
  Ni = "nations",
  ki = "levels",
  Pi = { heavy_tank: ae, medium_tank: j, light_tank: ce, at_spg: Aa };
function Ri(e, a) {
  return (
    "isCommonProgression" === e &&
    a.status !== Oa.UNSUITABLE_TO_QUEUE &&
    a.bpProgress < a.maxBpScore
  );
}
function Bi(e, a, t, s) {
  switch (a) {
    case "elite":
      return e.includes("premium") || (s && s.elite && !t.premium);
    case "premium":
      return t.premium || (e.includes("elite") && s && s.elite);
    case "bonus":
      return s && s.bonusMultiplier >= 2;
    case "favorite":
      return t.favorite;
    case "crystals":
      return t.crystalEarning;
    case "rented":
      return !0;
    case "canInstallAttachments":
      return t.canInstallAttachments;
    case "own3DStyle":
      return s && s.own3DStyle;
    case "event":
    case "funRandom":
      return t.isSuitableVehicle;
    default:
      return !1;
  }
}
var Ai = {
  [ki]: (e, a) => !e.levels || e.levels.includes(`level_${a.level}`),
  [Ni]: (e, a) => !e.nations || e.nations.includes(Pa(a.nationId)),
  [Ii]: (e, a) => !e.vehicle_types || e.vehicle_types.includes(a.type),
};
function Ei(e, a, t) {
  let s = !1;
  const r = e.specials ?? [];
  for (const n of r)
    if ("rented" !== n) {
      if (!Bi(r, n, a, t)) return !1;
    } else s = !0;
  if (!s && T(a) && !t?.fromWotPlus) return !1;
  if (t && e.battle_pass && e.battle_pass.length > 0)
    for (const n of e.battle_pass) if (!Ri(n, t)) return !1;
  for (const n of Object.keys(e)) if (n in Ai && !Ai[n](e, a)) return !1;
  return ((e, a) => {
    const t = J(a.role);
    let s = !1;
    for (const r of Object.keys(Pi))
      if (r in e && ((s = !0), e[r].some((e) => e.includes(t)))) return !0;
    return !s;
  })(e, a);
}
function Ti(e, { shortName: a, fullName: t }) {
  const s = e.toLowerCase();
  return !(s.length > 0 && !a.toLowerCase().includes(s) && !t.toLowerCase().includes(s));
}
function Li(e, a, t) {
  const s = e[a] ?? [],
    r = { ...e };
  return (
    (r[a] = s.includes(t) ? s.filter((e) => e !== t) : [...s, t]),
    r[a].length > 0 || delete r[a],
    r
  );
}
function Oi(e, a) {
  return "regular" === a.type
    ? Li(e, a.field, a.value)
    : Object.keys(Pi).reduce((e, t) => {
        const s = Pi[t].find((e) => e.includes(a.role));
        return s
          ? Li(
              e,
              t,
              (function (e, a) {
                return "at_spg" === e ? `role_ATSPG_${a}` : `role_${e[0].toUpperCase()}T_${a}`;
              })(t, s),
            )
          : e;
      }, e);
}
function Di(e, a, t, s) {
  if (t.favorite !== s.favorite) return t.favorite ? -1 : 1;
  const r = e[Pa(t.nationId)] ?? 0,
    n = e[Pa(s.nationId)] ?? 0;
  if (r !== n) return r - n;
  const i = a[t.type] ?? 0,
    o = a[s.type] ?? 0;
  return i !== o
    ? i - o
    : t.level !== s.level
      ? t.level - s.level
      : t.premium !== s.premium
        ? t.premium
          ? 1
          : -1
        : t.shortName.localeCompare(s.shortName);
}
var [Wi, Vi] = He("FilterVehiclesProvider")(
    ({ observableModel: e, readByPath: a }) => {
      function s(e) {
        try {
          return JSON.parse(e);
        } catch (a) {
          return (console.error(a), {});
        }
      }
      const { text_search: r, ...n } = s(a("filters")),
        i = { ...e.primitives(["defaultFilters"]) },
        o = Sa.structural(() => s(i.defaultFilters.get())),
        l = {
          ...e.primitives(["carouselRowCount"]),
          filters: wa.box(n, { deep: !1 }),
          searchName: wa.box(r?.[0] ?? ""),
          nations: e.arrayClone("nationsOrder"),
        };
      return {
        ...l,
        computes: {
          hasFilters: Sa.primitive(
            () => !t.structural(o(), l.filters.get()) || l.searchName.get().length > 0,
          ),
          nations: () => l.nations.get(),
          nationToIndex: Sa.shallow(() => l.nations.get().reduce((e, a, t) => ((e[a] = t), e), {})),
          default: o,
        },
      };
    },
    ({ cleanup: e, model: a, externalModel: t }) => {
      const s = t.createCallback((e) => e, "onSaveFilter");
      return (
        e(
          fa(() => {
            var e, t;
            ((e = a.filters.get()),
              (t = a.searchName.get()),
              s({ filters: JSON.stringify({ ...e, text_search: t.length > 0 ? [t] : void 0 }) }));
          }),
        ),
        {
          reset: ca(() => {
            (a.filters.set(a.computes.default()), a.searchName.set(""));
          }),
          search: ca((e) => {
            a.searchName.set(e);
          }),
          change: ca((e) => {
            a.filters.set(Oi(a.filters.get(), e));
          }),
          carouselTypeChange: t.createCallback((e) => ({ rowCount: e }), "onCarouselTypeChange"),
        }
      );
    },
  ),
  Mi = [P.lightTank, P.mediumTank, P.heavyTank, P["AT-SPG"], P.SPG].reduce(
    (e, a, t) => ((e[a] = t), e),
    {},
  ),
  [zi, $i] = He("VehicleStatisticsProvider")(({ observableModel: e }) => {
    const a = e.dict("statistics"),
      t = Sa.structural((e) => a.get(e));
    return { ids: Sa.primitive(() => a.keys), get: t };
  }),
  [Fi, Hi] = He("VehiclesProvider")(
    ({ observableModel: e }) => {
      const a = { vehicles: e.dictRef("vehicles") };
      return {
        get: Sa.structural((e) => {
          if (-1 === e) return;
          const t = a.vehicles.get(e);
          if (!t) return void console.error(`Error getting vehicle with id: ${e}`);
          const s = (function (e) {
            try {
              const a = JSON.parse(e);
              return ((a.shortName = a.shortName.replace(/<img.+\/>/, "")), a);
            } catch (a) {
              throw (console.error(`Error parsing JSON for element ${e}:`, a), a);
            }
          })(t);
          return { ...s, imageKey: Be(s.name) };
        }),
        has: Sa.primitive((e) => Boolean(a.vehicles.get(e))),
        ids: Sa.shallow(() => [...a.vehicles.keys.values()]),
        amount: Sa.primitive(() => a.vehicles.length),
        list: Sa.shallow(() => {
          let e = [];
          for (const [s, r] of a.vehicles.entries())
            try {
              e.push(JSON.parse(r.get()));
            } catch (t) {
              console.error(`Error parsing JSON for element ${s}:`, t);
            }
          return e;
        }),
      };
    },
    Ne,
    { useRequires: () => ({ statistics: $i() }) },
  ),
  [Ui, Gi] = He("MyVehiclesProvider")(
    (e) => {
      const a = e.requires.statistic.model.ids,
        t = Sa.structural((t) => {
          if (a().has(t)) return e.requires.vehicles.model.get(t);
        }),
        s = Sa.shallow(() => {
          const t = [];
          for (const s of a().values()) {
            const a = e.requires.vehicles.model.get(s);
            a ? t.push(a) : console.warn(`No vehicle with id: ${s}`);
          }
          return t;
        });
      return { get: t, getAll: s, amount: Sa.primitive(() => s().length), ids: a };
    },
    Ne,
    { useRequires: () => ({ vehicles: Hi(), statistic: $i() }) },
  ),
  qi = Qa.resolve("strings"),
  Ki = nt(ut + Ua),
  Xi = () => `${Date.now().toString(16)}_${Ki(3)}`;
function Zi(e, a, t = 1) {
  const s = Ae(a, { count: t });
  return e.has(s) ? Zi(e, a, t + 1) : s;
}
function Ji(e = "", a = []) {
  return {
    title: "" !== e ? e : qi.readOrEmpty("playlists.defaultName"),
    createdAt: Date.now(),
    modifiedAt: Date.now(),
    list: a,
  };
}
var Qi = (e) => ({ type: "ok", value: e });
function Yi(e) {
  if ("ok" === e.type) return e.value;
}
var eo = "delete",
  ao = "import",
  to = Lt({
    title: Dt(),
    createdAt: Ot(Gt(), Ut(), Ft(0)),
    modifiedAt: Ot(Gt(), Ut(), Ft(0)),
    list: $t(Ot(Gt(), Ut())),
  }),
  so = Ot(
    Dt(),
    Ht((e) => (e.length > 0 ? e : void 0)),
  ),
  ro = "new",
  no = "existing",
  [io, oo, { Context: lo }] =
    (Lt({ id: Ot(Dt(), Tt(1)), playlistState: Mt(zt([Vt(no), Vt(ro)])) }),
    Lt({ title: Dt() }),
    Lt({
      titles: Ot(
        $t(Dt()),
        Ht((e) => new Set(e)),
      ),
    }),
    He("PlaylistsProvider")(
      ({ requires: e, observableModel: a }) => {
        const s = a.dict("storage"),
          r = a.primitives(["selectedID", "enabled", "dirtyEdit"]),
          n = e.filters.model.computes.default,
          i = {
            vehicles: e.vehicles.model,
            myVehicles: e.myVehicles.model,
            enabled: r.enabled,
            nationsOrder: e.filters.model.nations,
            filters: wa.box(n(), { deep: !1 }),
            searchName: wa.box("", { deep: !1 }),
            edit: { initial: wa.box(void 0, { deep: !1 }), dirty: r.dirtyEdit },
          },
          o = Sa.shallow(() => s.keys),
          l = Sa.primitive(() => Kt(so, r.selectedID.get())),
          c = Sa.structural((e) => {
            try {
              const a = s.get(e);
              if (!a) return Qi(void 0);
              const t = Kt(to, JSON.parse(a)),
                r = new Set();
              for (const e of t.list)
                if (Le[e]) {
                  const a = Le[e].find((e) => Boolean(i.myVehicles.get(e.toString())));
                  r.add(a ?? e);
                } else r.add(e);
              return Qi({ ...t, list: [...r.values()] });
            } catch (r) {
              return (
                console.error(`Error getting playlist with ${e} id`, r),
                (a = "PARSE_ERROR"),
                (t = String(r)),
                { type: "error", error: { tag: a, msg: t } }
              );
            }
            var a, t;
          }),
          d = Sa.shallow(() =>
            S(o().values())
              .map((e) => c(e))
              .filter((e) => "ok" === e.type && void 0 !== e.value)
              .map((e) => e.value.title)
              .reduce((e, a) => e.add(a), new Set()),
          ),
          _ = Sa.primitive((e) => {
            const a = c(e);
            if ("ok" !== a.type || void 0 === a.value)
              throw new Error(`Can't get playlist by id ${e}`);
            return a.value;
          }),
          u = Sa.structural((e) => {
            const a = c(e);
            if ("ok" === a.type && void 0 !== a.value) return { id: e, ...a.value };
          }),
          m = Sa.shallow(() =>
            S(o().values())
              .map((e) => u(e))
              .filter((e) => void 0 !== e)
              .toArray()
              .sort((e, a) => e.title.localeCompare(a.title))
              .map((e) => e.id),
          ),
          p = Sa.primitive(() => {
            const e = l();
            if (e) return u(e);
          }),
          h = Sa.shallow(() => {
            const a = e.filters.model.computes.nationToIndex();
            return ee(e.myVehicles.model.getAll(), (e, t) => Di(a, Mi, e, t));
          }),
          b = Sa.primitive((e) => {
            const a = u(e),
              t = g();
            if (void 0 === a || 0 === a.list.length) return;
            const s = new Set(a.list);
            for (let r = 0; r < t.length; r += 1) {
              const e = Number(t[r]?.id);
              if (ua(e) && s.has(e)) return r;
            }
          }),
          f = Sa.primitive(
            () => !1 === t.structural(n(), i.filters.get()) || i.searchName.get().length > 0,
          ),
          g = Sa.shallow(() => {
            const a = i.filters.get(),
              t = h(),
              s = i.searchName.get();
            return t.filter((t) => !!Ti(s, t) && Ei(a, t, e.statistic.model.get(t.id)));
          }),
          v = Sa.primitive((a) => Boolean(e.statistic.model.get(a)?.elite)),
          x = Sa.shallow((a) => e.vehicles.model.get(a)?.imageKey),
          w = Sa.primitive(() => g().length),
          C = Sa.shallow(() => p()?.list.map(i.vehicles.get));
        return {
          ...i,
          current: p,
          titles: d,
          currentId: l,
          byIdUnsafe: _,
          byId: c,
          byIdFull: u,
          filtered: g,
          filteredAmount: w,
          defaultFilters: n,
          hasFilters: f,
          vehicleImage: x,
          currentVehicles: C,
          ids: o,
          sortedIds: m,
          isElite: v,
          firstAddedVehicleIndexByPlaylistId: b,
        };
      },
      ({ model: e, externalModel: a }) => {
        const t = a.createCallback(
          (e) => ({ id: e.id, data: JSON.stringify(e.initial), skipRedirect: e.skipRedirect }),
          "onCreate",
        );
        return {
          filters: Va({
            update: (a) => {
              e.filters.set(Oi(e.filters.get(), a));
            },
            reset: () => {
              (e.filters.set(e.defaultFilters()), e.searchName.set(""));
            },
            search: (a) => e.searchName.set(a),
            change: (a) => {
              e.filters.set(Oi(e.filters.get(), a));
            },
          }),
          create: ca((a) => {
            const { id: s = Xi(), vehicleIds: r = [], skipRedirect: n = !1 } = a ?? {};
            t({ id: s, initial: Ji(Zi(e.titles(), "playlists.defaultName"), r), skipRedirect: n });
          }),
          edit: {
            sendModify: a.createCallback(
              (e, a) => ({ id: e, data: JSON.stringify(a) }),
              "onModify",
            ),
            setDirty: a.createCallback((e) => ({ value: e }), "onSetDirtyEdit"),
          },
          select: a.createCallback((e = "") => ({ id: e }), "onSelect"),
          save: a.createCallback((e) => ({ id: e }), "onSave"),
          exit: a.createCallback((e) => ({ id: e }), "onDiscard"),
          goToAboutVehicle: a.createCallback((e) => ({ intCD: e }), "onGoToAboutVehicle"),
          openImport: a.createCallback(
            ca(() => ({
              type: ao,
              params: JSON.stringify({ titles: Array.from(e.titles().values()) }),
            })),
            "openImportConfirm",
          ),
          openDeleteConfirm: a.createCallback(
            (e, a) => ({ id: e, type: eo, params: JSON.stringify({ title: a }) }),
            "openDeleteConfirm",
          ),
        };
      },
      { useRequires: () => ({ vehicles: Hi(), myVehicles: Gi(), filters: Vi(), statistic: $i() }) },
    )),
  co = "pending",
  _o = "readyToSelect",
  uo = "disabled",
  [mo, po] = He("VehiclesInventoryProvider")(
    (e) => {
      const a = e.observableModel.primitives([
          "freeSlotsCount",
          "defaultSlotPrice",
          "slotPrice",
          "slotPriceCurrency",
          "recoverableVehicleCount",
          "currentVehicleIntCD",
          "currentVehicleInventoryId",
          "hasDiscont",
          "bpEntityValid",
          "bpStatus",
          "telecomRentStatus",
        ]),
        t = wa.box([], { deep: !1 }),
        s = { intCD: a.currentVehicleIntCD, inventoryId: a.currentVehicleInventoryId },
        r = Sa.shallow(() => {
          const a = s.intCD.get();
          return e.requires.vehicles.model.get(a);
        }),
        n = Sa.shallow((a) => {
          if (void 0 === a) return;
          const t = s.intCD.get();
          return -1 === t ? e.requires.vehicles.model.get(a) : e.requires.vehicles.model.get(t);
        }),
        i = Sa.shallow(() => {
          const a = s.intCD.get();
          return e.requires.statistic.model.get(a);
        }),
        o = Sa.primitive(() => -1 !== s.intCD.get()),
        l = Sa.shallow((e) => La(e, (e) => c.get(String(e)))),
        c = e.requires.myVehicles.model,
        d = Sa.structural(() => e.requires.vehicles.model.list().filter((e) => e.rent.isRented)),
        _ = Sa.primitive(() =>
          e.requires.vehicles.model.list().some((a) => {
            const t = e.requires.statistic.model.get(a.vehicleId);
            if (t) return "inPrebattle" === t.status;
          }),
        ),
        u = Sa.primitive(() => {
          const a = [...c.getAll()],
            t = e.requires.filters.model.computes.nationToIndex();
          return (a.sort((e, a) => Di(t, Mi, e, a)), a);
        });
      return (
        e.cleanup(
          fa(() => {
            const a = e.requires.filters.model.filters.get(),
              s = e.requires.filters.model.searchName.get(),
              r = e.requires.playlists?.model.current(),
              n = c.ids(),
              i = (r ? l(r.list) : u()).filter(
                (t) =>
                  !1 !== n.has(t.id) &&
                  !!Ei(a, t, e.requires.statistic.model.get(t.id)) &&
                  Ti(s, t),
              );
            vt(() => t.set(i));
          }),
        ),
        {
          vehicles: e.requires.myVehicles.model,
          vehicle: n,
          selectedVehicle: r,
          isVehicleSelected: o,
          selectedVehicleStatistics: i,
          accumulateByIds: l,
          rentVehiclesList: d,
          prebattleModeActive: _,
          current: {
            intCD: a.currentVehicleIntCD,
            inventoryId: a.currentVehicleInventoryId,
            amount: Sa.primitive(() => t.get().length),
            list: () => t.get(),
            ids: Sa.shallow(() => t.get().map((e) => e.id)),
            playlist: e.requires.playlists ? e.requires.playlists.model.current : () => {},
          },
          slots: {
            free: a.freeSlotsCount,
            price: {
              defaultValue: a.defaultSlotPrice,
              value: a.slotPrice,
              currency: a.slotPriceCurrency,
            },
            recover: a.recoverableVehicleCount,
            discount: a.hasDiscont,
          },
          bpState: { active: a.bpEntityValid, status: a.bpStatus },
          telecomRentStatus: a.telecomRentStatus,
        }
      );
    },
    (e) => ({
      select: e.externalModel.createCallback((e) => ({ id: e }), "onSelect"),
      buySlot: e.externalModel.createCallbackNoArgs("onBuySlot"),
      goBuyVehicle: e.externalModel.createCallbackNoArgs("onGoBuyVehicle"),
      goRecoverVehicle: e.externalModel.createCallbackNoArgs("onGoRecoverVehicle"),
      selectTelecomRentalVehicle: e.externalModel.createCallbackNoArgs(
        "onSelectTelecomRentalVehicle",
      ),
    }),
    {
      useRequires: () => ({
        myVehicles: Gi(),
        vehicles: Hi(),
        statistic: $i(),
        filters: Vi(),
        playlists: (0, us.useContext)(lo),
      }),
    },
  ),
  [ho, bo, { Context: fo }] = He("ManageableVehiclePlaylistsModel")(
    (e) => {
      const a = {
          ...e.observableModel.primitives({ intCD: "vehicleId" }),
          displayedVehicleId: wa.box(-1),
          changesInPlaylistSelection: wa.set(new Set()),
        },
        t = Sa.shallow(() =>
          e.requires.playlists.model.sortedIds().reduce((a, t) => {
            const s = e.requires.playlists.model.byIdFull(t);
            return (s ? a.push(s) : console.warn(`Missing playlist data for id = ${t}`), a);
          }, []),
        ),
        s = Sa.structural(() =>
          t().map(({ id: e, title: t, list: s }) => {
            const r = s.includes(a.displayedVehicleId.get());
            return { id: e, title: t, selected: a.changesInPlaylistSelection.has(e) ? !r : r };
          }, []),
        ),
        r = Sa.primitive(() => 0 === s().length);
      return (
        e.cleanup(
          fa(() => {
            (a.displayedVehicleId.get(), t(), vt(() => a.changesInPlaylistSelection.clear()));
          }),
        ),
        {
          ...a,
          computeds: {
            playlistItems: s,
            isVehiclePlaylistsEmpty: r,
            vehicle: Sa.shallow(() => {
              const t = a.displayedVehicleId.get(),
                s = e.requires.vehicles.model.get(t),
                r = e.requires.vehicleStatistics.model.get(t);
              if (void 0 !== s && void 0 !== r) return { ...s, elite: r.elite };
            }),
            empty: Sa.primitive(() => -1 === a.vehicleId.get()),
            sortedPlaylists: t,
            hasChanges: Sa.primitive(() => a.changesInPlaylistSelection.size > 0),
            enabled: Sa.primitive(() => e.requires.playlists.model.enabled.get()),
          },
        }
      );
    },
    (e) => ({
      setDisplayedVehicleId: ca((a) => {
        e.model.displayedVehicleId.set(a);
      }),
      reset: e.externalModel.createCallbackNoArgs("onReset"),
      selectVehicle: e.externalModel.createCallback((e) => ({ id: e }), "onSelectVehicle"),
      goToCreatePlaylist: (a) => {
        e.requires.playlists.controls.create({ vehicleIds: a });
      },
      togglePlaylist: ca((a) => {
        e.model.changesInPlaylistSelection.has(a)
          ? e.model.changesInPlaylistSelection.delete(a)
          : e.model.changesInPlaylistSelection.add(a);
      }),
      save: ca(() => {
        const a = e.model.displayedVehicleId.get(),
          t = e.requires.playlists.model.currentId();
        for (const s of e.model.changesInPlaylistSelection) {
          const t = Yi(e.requires.playlists.model.byId(s));
          if (!t) return void console.warn(`Missing playlist data for id = ${s}`);
          (e.requires.playlists.controls.edit.sendModify(s, {
            ...t,
            modifiedAt: Date.now(),
            list: t.list.includes(a) ? t.list.filter((e) => e !== a) : [...t.list, a],
          }),
            e.requires.playlists.controls.save(s));
        }
        e.requires.playlists.controls.select(t);
      }),
      cancel: ca(() => {
        e.model.changesInPlaylistSelection.clear();
      }),
    }),
    { useRequires: () => ({ vehicles: Hi(), playlists: oo(), vehicleStatistics: $i() }) },
  ),
  go = () => (0, us.useContext)(fo),
  vo = (e) =>
    (0, ms.jsxs)("svg", {
      width: 24,
      height: 24,
      viewBox: "0 0 24 24",
      fill: "none",
      xmlns: "http://www.w3.org/2000/svg",
      xmlnsXlink: "http://www.w3.org/1999/xlink",
      ...e,
      children: [
        (0, ms.jsx)("path", {
          opacity: 0.8,
          d: "M19 16H22V18H19V21H17V18H14V16H17V13H19V16Z",
          fill: "#0D0E10",
        }),
        (0, ms.jsx)("path", {
          d: "M19 15H22V17H19V20H17V17H14V15H17V12H19V15Z",
          fill: "url(#paint0_radial_111851_505980)",
        }),
        (0, ms.jsx)("g", {
          opacity: 0.8,
          children: (0, ms.jsx)("path", {
            d: "M12 16H5V15H12V16ZM15 13H5V12H15V13ZM19 10H5V9H19V10ZM19 7H5V6H19V7Z",
            fill: "url(#paint1_radial_111851_505980)",
          }),
        }),
        (0, ms.jsx)("path", {
          opacity: 0.8,
          d: "M12 17H5V16H12V17ZM15 14H5V13H15V14ZM19 11H5V10H19V11ZM19 8H5V7H19V8Z",
          fill: "#0D0E10",
        }),
        (0, ms.jsxs)("defs", {
          children: [
            (0, ms.jsxs)("radialGradient", {
              id: "paint0_radial_111851_505980",
              cx: 0,
              cy: 0,
              r: 1,
              gradientUnits: "userSpaceOnUse",
              gradientTransform: "translate(15.7778 13.6) rotate(90) scale(5.6 4.97778)",
              children: [
                (0, ms.jsx)("stop", { offset: 6.20882e-10, stopColor: "#EDE6D9" }),
                (0, ms.jsx)("stop", { offset: 1, stopColor: "#C2C7CE" }),
              ],
            }),
            (0, ms.jsxs)("radialGradient", {
              id: "paint1_radial_111851_505980",
              cx: 0,
              cy: 0,
              r: 1,
              gradientUnits: "userSpaceOnUse",
              gradientTransform: "translate(12 14.0904) rotate(180) scale(8.90909 2.42616)",
              children: [
                (0, ms.jsx)("stop", { offset: 6.20882e-10, stopColor: "#EDE6D9" }),
                (0, ms.jsx)("stop", { offset: 1, stopColor: "#C2C7CE" }),
              ],
            }),
          ],
        }),
      ],
    }),
  xo = "Buttons_937965ba",
  wo = "Buttons_right_268130b5",
  Co = "Buttons_button_aeef4019",
  yo = "Buttons_button__create_61690fd8",
  So = "Buttons_icon_378ba619",
  jo = Qa.resolve("strings"),
  Io = Wt(function () {
    const { model: e, controls: a } = bo();
    return (0, ms.jsxs)("div", {
      className: sa(xo),
      children: [
        (0, ms.jsx)(U, {
          body: jo.readOrEmpty("playlists.managaeble_playlists.buttons.create.tooltipBody"),
          children: (0, ms.jsx)(yt, {
            className: sa(Co, yo),
            theme: yt.themes.secondary,
            size: yt.sizes.extraSmall,
            autoAlignContent: !1,
            onClick: () => {
              (a.goToCreatePlaylist([e.displayedVehicleId.get()]), a.reset());
            },
            children: (0, ms.jsx)(vo, { className: So }),
          }),
        }),
        (0, ms.jsxs)("div", {
          className: wo,
          children: [
            (0, ms.jsx)(yt, {
              className: Co,
              theme: yt.themes.secondary,
              size: yt.sizes.extraSmall,
              onClick: () => {
                (a.cancel(), a.reset());
              },
              children: (0, ms.jsx)(H, {
                text: jo.readOrEmpty("playlists.managaeble_playlists.buttons.cancel.title"),
              }),
            }),
            (0, ms.jsx)(yt, {
              className: Co,
              theme: yt.themes.primary,
              size: yt.sizes.extraSmall,
              disabled: !e.computeds.hasChanges(),
              onClick: () => {
                (a.save(), a.reset());
              },
              children: (0, ms.jsx)(H, {
                text: jo.readOrEmpty("playlists.managaeble_playlists.buttons.save.title"),
              }),
            }),
          ],
        }),
      ],
    });
  }),
  No = "Item_itemBackground_f5007fc6",
  ko = "Item_c5163bf",
  Po = "Item_checkbox_cfffba80",
  Ro = "Item_item__checked_5f6fcc69",
  Bo = "Item_check_a68580c8",
  Ao = "Item_checkboxLabel_885d0061",
  Eo = Wt(function ({ id: e, title: a, checked: t }) {
    const { controls: s } = bo();
    return (0, ms.jsxs)("div", {
      className: sa(ko, t && Ro),
      children: [
        (0, ms.jsx)("div", { className: No }),
        (0, ms.jsx)(Q, {
          checked: t,
          onCheckedChange: () => s.togglePlaylist(e),
          size: ie.small,
          className: Po,
          classNames: { label: Ao, check: Bo },
          children: (0, ms.jsx)(H, { text: a }),
        }),
      ],
    });
  }),
  To = "List_152fbdf4",
  Lo = "List_scrollWrapper_e69e8089",
  Oo = "List_scrollContent_30662217",
  Do = "List_scrollbar_611defd3",
  Wo = Wt(function () {
    const { model: e } = bo(),
      a = e.computeds.playlistItems();
    return (0, ms.jsxs)("div", {
      className: To,
      children: [
        (0, ms.jsx)(Ma, {
          classNames: { wrapper: Lo, content: Oo },
          children: re(a, ({ id: e, title: a, selected: t }) =>
            (0, ms.jsx)(Eo, { id: e, title: a, checked: t }, e),
          ),
        }),
        (0, ms.jsx)(da, { classNames: { base: Do } }),
      ],
    });
  }),
  Vo = "Vehicle_name_f5f779f6",
  Mo = "Vehicle_level_c03ad304",
  zo = "Vehicle_type_9905a21f",
  $o = Wt(function () {
    const { model: e } = bo(),
      a = e.computeds.vehicle();
    if (void 0 === a) return null;
    const t = J(a.role);
    return (0, ms.jsxs)(f, {
      children: [
        (0, ms.jsx)(f.Level, { value: a.level, className: Mo }),
        ke(a.type) &&
          (0, ms.jsx)(f.Type, {
            size: f.Type.sizes.x24x24,
            className: zo,
            type: a.type,
            premium: a.elite,
          }),
        (0, ms.jsx)(H, { text: a.fullName, className: Vo }),
        "without_role" !== t && (0, ms.jsx)(f.Role, { size: f.Role.sizes.x16x16, roleKey: t }),
      ],
    });
  }),
  Fo = "Styles_display_f2930fa3",
  Ho = "Styles_header_dcb2494f",
  Uo = "Styles_body_504cd01f",
  Go = "Styles_title_ece3f15e",
  qo = Qa.resolve("strings");
function Ko({ className: e }) {
  return (0, ms.jsxs)(Ea.Header, {
    className: sa(Ho, e),
    children: [
      (0, ms.jsx)(Ea.Title, {
        className: Go,
        children: (0, ms.jsx)(H, {
          text: qo.readOrEmpty("playlists.managaeble_playlists.header.title"),
        }),
      }),
      (0, ms.jsx)($o, {}),
    ],
  });
}
function Xo({ className: e }) {
  return (0, ms.jsxs)(Ea.Body, {
    className: sa(Uo, e),
    children: [
      (0, ms.jsx)(Ea.Divider, {}),
      (0, ms.jsx)(dt, { children: (0, ms.jsx)(Wo, {}) }),
      (0, ms.jsx)(Ea.Divider, {}),
      (0, ms.jsx)(Io, {}),
    ],
  });
}
var Zo = (0, us.memo)(function ({ vehicleId: e, tipSize: a, className: t, children: s, ...r }) {
    return (0, ms.jsxs)(Ea.Display, {
      ...r,
      className: sa(Fo, t),
      children: [(0, ms.jsx)(Ea.Tip, { size: a }), (0, ms.jsx)(Ea.Close, {}), s],
    });
  }),
  Jo = Wt(({ children: e }) => {
    const a = n(),
      t = d(),
      s = h(),
      r = se(),
      { model: i, controls: o } = bo(),
      l = i.vehicleId.get(),
      c = i.displayedVehicleId.get(),
      [_, u] = (0, us.useState)(!1),
      [m, p] = (0, us.useState)(!1),
      b = Ee(() => {
        (p(!0), a.open(), s.run(() => p(!1), 250));
      }),
      f = Ee(() => {
        (p(!0),
          a.close(),
          s.run(() => {
            (u(!0),
              o.setDisplayedVehicleId(-1),
              r.run(() => {
                (p(!1), u(!1));
              }));
          }, 250));
      }),
      g = Ee(() => {
        (u(!0), o.setDisplayedVehicleId(l), r.run(() => u(!1)));
      });
    (0, us.useEffect)(() => {
      t || i.computeds.empty() || a.opened || (o.reset(), f());
    }, [a.opened]);
    const v = Ee(() => {
      r.isRunning ||
        (a.opened || s.isRunning || l === c
          ? a.opened || -1 === l || -1 === c
            ? a.opened && -1 === l && -1 !== c && f()
            : s.isRunning || b()
          : g());
    });
    return (
      (0, us.useEffect)(v, [v, l, c, a.opened, m, _]),
      A(() => {
        i.computeds.empty() || o.reset();
      }),
      e
    );
  }),
  Qo = (e) => `manageable-vehicle-playlists-model-${e}`,
  Yo = Wt(function ({ children: e, position: a, freeSpaceRem: t, tipSize: s }) {
    const { model: r, controls: n } = bo(),
      i = r.displayedVehicleId.get(),
      o = gt("rem"),
      l = Ee((e, { callerBounding: a }) => {
        const t = e.trigger.bounding.get();
        if (t && !v(t, a)) return (e.close(), !1);
      }),
      c = r.vehicleId.get(),
      d = r.computeds.isVehiclePlaylistsEmpty(),
      _ = $(c);
    return (
      (0, us.useEffect)(() => {
        d && -1 === _ && -1 !== c && (n.goToCreatePlaylist([c]), n.reset());
      }, [_, c, d, n]),
      d
        ? null
        : (0, ms.jsx)(Ea, {
            id: Qo(i),
            children: (0, ms.jsxs)(Jo, {
              children: [
                (0, ms.jsx)(Ea.Portal, {
                  paddingsRem: o,
                  position: a,
                  freeSpaceRem: t,
                  onBeforePositionChange: l,
                  children:
                    -1 !== i &&
                    (0, ms.jsxs)(
                      Zo,
                      {
                        vehicleId: i,
                        tipSize: s,
                        children: [(0, ms.jsx)(Ko, {}), (0, ms.jsx)(Xo, {})],
                      },
                      i,
                    ),
                }),
                e,
              ],
            }),
          })
    );
  });
var el = e(Da(), 1),
  al = "emptySlot",
  tl = "left",
  sl = "right",
  rl = "both",
  nl = "none",
  il = 189,
  ol = 245,
  ll = {
    default: { single: il, double: il },
    breakpoints: {
      medium: { single: 224 },
      large: { single: ol, double: ol },
      extraLarge: { single: 302 },
    },
  },
  cl = (e, a) => (e || a ? (e ? (a ? nl : sl) : tl) : rl),
  dl = "Content_7ccb81a0",
  _l = "Content_disabledOverlay_a8908196",
  ul = "Content_base__disabled_da09528a",
  ml = "Content_base__selected_da09528a",
  pl = "Content_base__empty_da09528a";
function hl({ children: e, selected: a, disabled: t, empty: s }) {
  return (0, ms.jsxs)("div", {
    "data-name": "Content",
    className: sa(dl, s && pl, a && ml, t && ul),
    children: [e, t && (0, ms.jsx)("div", { className: _l })],
  });
}
var bl = "Slot_977dd8f1",
  fl = "Slot_base__wrapper_ae3081b5",
  gl = "Slot_base__disabled_334cc10f",
  vl = "Slot_base__empty_d386066c",
  xl = "Slot_content_1a27c8cf",
  wl = "Slot_base__active_71f19f5c",
  Cl = "Slot_base__selected_71f19f5c",
  yl = "Slot_selected_6e9f21df",
  Sl = "Slot_selected__border_e2a17304",
  jl = (0, us.memo)(function ({
    children: e,
    selected: a = !1,
    disabled: t = !1,
    active: s,
    className: r,
    ...n
  }) {
    const i = t || void 0 === n.onClick;
    return (0, ms.jsx)("div", {
      ...n,
      "data-name": "Slot",
      className: sa(bl, s && wl, a && Cl, t && gl, i && vl, fl, r),
      children: (0, ms.jsxs)("div", {
        className: xl,
        children: [
          (0, ms.jsx)(hl, { selected: a, disabled: t, empty: i, children: e }),
          a && (0, ms.jsx)("div", { className: sa(yl, Sl) }),
          (0, ms.jsx)("div", { className: yl }),
        ],
      }),
    });
  }),
  Il = { buySlot: "buySlot", buyTank: "buyTank", restoreTank: "restoreTank", rentTank: "rentTank" },
  Nl = {
    [Il.buySlot]: "buy_slot",
    [Il.buyTank]: "buy_vehicle_new",
    [Il.restoreTank]: "restore_vehicle",
    [Il.rentTank]: "wot_plus_slot",
  },
  kl = "ActionCards_wrapper_690d669a",
  Pl = "ActionCards_text_cdbc926",
  Rl = "ActionCards_wrapper__double_70640c01",
  Bl = "ActionCards_content_a46de8cf",
  Al = "ActionCards_content__buySlot_a70e9708",
  El = "ActionCards_icon_f8219d70",
  Tl = "ActionCards_contentIcon_166df330",
  Ll = "ActionCards_currency_ac7c654f",
  Ol = "ActionCards_discount_967a7825",
  Dl = {
    [co]: "menu.tankCarousel.wotPlusSelectionPending",
    [_o]: "menu.tankCarousel.wotPlusSelectionAvailable",
  },
  Wl = Wt(function ({ type: e }) {
    const a = po(),
      t = a.model.slots.price.currency.get(),
      s = a.model.slots.price.value.get(),
      n = a.model.slots.free.get(),
      i = a.model.slots.recover.get(),
      o = a.model.slots.discount.get(),
      l = a.model.telecomRentStatus.get();
    if (e === Il.buySlot)
      return (0, ms.jsx)("div", {
        className: Ll,
        children: (0, ms.jsx)(Bt, {
          type: Pe.currency,
          size: B.extraSmall,
          enabled: o,
          classNames: { icon: Ol },
          children: (0, ms.jsx)(c, {
            type: t,
            size: B.extraSmall,
            reverse: !0,
            classNames: { base: sa(Bl, Al), icon: Tl },
            children: s,
          }),
        }),
      });
    if (e === Il.rentTank) {
      const e = Dl[l];
      return e ? (0, ms.jsx)(r, { className: Pl, upgradeLegacy: !0, path: e }) : null;
    }
    return (0, ms.jsxs)("div", {
      className: Bl,
      children: [
        e === Il.buyTank &&
          (0, ms.jsx)(r, {
            upgradeLegacy: !0,
            path: "menu.tankCarousel.vehicleStates.buyTankEmptyCount",
            params: { count: n },
          }),
        e === Il.restoreTank &&
          (0, ms.jsx)(r, {
            upgradeLegacy: !0,
            path: "menu.tankCarousel.vehicleStates.restoreTankCount",
            params: { count: i },
          }),
      ],
    });
  });
function Vl({ type: e, width: a, height: t, doubleRow: s, className: n }) {
  const i = po(),
    o = ge(),
    l = i.model.slots.price.value.get(),
    c = i.model.slots.price.defaultValue.get(),
    d = i.model.slots.discount.get();
  i.model.telecomRentStatus.get();
  const _ = Qa.resolve("strings"),
    m = V(`hangar.carousel.actionCards.x48x48.${e}`, `hangar.carousel.actionCards.x96x96.${e}`),
    p = u({
      header: _.readOrEmpty(`tooltips.tanks_carousel.${Nl[e]}.header`),
      body: _.readOrEmpty(`tooltips.tanks_carousel.${Nl[e]}.body`),
    }),
    h = wt(
      "actionSlotPrice",
      (0, us.useMemo)(() => [[l], [c]], [l, c]),
      (0, us.useMemo)(() => ({ disabled: !d }), [d]),
    ),
    b = d && Nl[e] === Nl.buySlot ? h : p;
  return (0, ms.jsx)(jl, {
    ...b,
    className: n,
    style: { width: void 0 !== a ? `${a}px` : void 0, height: void 0 !== t ? `${t}px` : void 0 },
    "data-test-id": e,
    onClick: function (a) {
      (b.onClick(), o.play("click", { target: "vehicle:action-cards", original: a }));
      const t = {
        [Il.buySlot]: i.controls.buySlot,
        [Il.buyTank]: i.controls.goBuyVehicle,
        [Il.restoreTank]: i.controls.goRecoverVehicle,
        [Il.rentTank]: i.controls.selectTelecomRentalVehicle,
      }[e];
      if ("function" != typeof t)
        return console.error(`Unknown action type ${e} in ${Vl.name} handleClick`);
      t();
    },
    onMouseEnter: function (e) {
      (b.onMouseEnter(e), o.play("mouse-enter", { target: "vehicle:action-cards", original: e }));
    },
    children: (0, ms.jsxs)("div", {
      className: sa(kl, s && Rl),
      children: [
        (0, ms.jsx)(be, {
          className: El,
          path: `hangar.carousel.actionCards.x32x32.${e}`,
          adaptive: { medium: { path: m } },
        }),
        (0, ms.jsx)("div", {
          className: Pl,
          children: (0, ms.jsx)(r, { path: `menu.tankCarousel.vehicleStates.${e}` }),
        }),
        (0, ms.jsx)(Wl, { type: e }),
      ],
    }),
  });
}
var Ml = "54033",
  zl = "50705",
  $l = "56833",
  Fl = "51201",
  Hl = { [Ml]: "alpha", [zl]: "alpha", [Fl]: "super", [$l]: "super" },
  Ul = "ammoNotFull",
  Gl = "crewNotFull",
  ql = "exploded",
  Kl = "destroyed",
  Xl = "damaged",
  Zl = "rentable",
  Jl = "rentableAgain",
  Ql = "rentalIsOver",
  Yl = "tooHeavy",
  ec = "unsuitableToQueue",
  ac = "unsuitableToUnit",
  tc = "inPrebattle",
  sc = "battle",
  rc = "wot_plus_exclusive_vehicle_disabled",
  nc = {
    [Ul]: "ammo",
    [Gl]: "crew",
    [ql]: "repair",
    [Kl]: "repair",
    [Xl]: "repair",
    [Zl]: "rental",
    [Jl]: "rental",
    [Ql]: "rental",
    [Yl]: "notSuitable",
    [ec]: "notSuitable",
    [ac]: "notSuitable",
    [tc]: "inPlatoon",
    [sc]: "inBattle",
    [rc]: "notSuitable",
  };
function ic(e, a, t) {
  return !(!e || "disabled" === a || !t) && t.status !== ec && t.maxBpScore > 0;
}
function oc(e) {
  return e > 2;
}
var [lc, cc, dc] = He()(({ observableModel: e }) => ({
    ...e.primitives(["isCrystalEarnEnabled", "isDailyMultipliedXpEnabled", "isInfiniteAmmo"]),
  })),
  _c = () => (0, us.useContext)(dc.Context),
  uc = {
    base: "ProBoost_7490b440",
    arrow: "ProBoost_arrow_346b5e61",
    glow: "ProBoost_glow_280ac9aa",
    base__double: "ProBoost_base__double_b53eea3f",
    base__active: "ProBoost_base__active_7b71aa2e",
    corner: "ProBoost_corner_9f13801e",
    base__activating: "ProBoost_base__activating_7b71aa2e",
    "arrow-brightness-activating": "ProBoost_arrow-brightness-activating_7b71aa2e",
    "arrow-translation-activating": "ProBoost_arrow-translation-activating_7b71aa2e",
    "glow-activating": "ProBoost_glow-activating_7b71aa2e",
    triangle: "ProBoost_triangle_ae0f2fba",
    "triangle-opacity-activating": "ProBoost_triangle-opacity-activating_7b71aa2e",
    "triangle-translation-activating": "ProBoost_triangle-translation-activating_7b71aa2e",
    triangle__1: "ProBoost_triangle__1_1cb04326",
    triangle__2: "ProBoost_triangle__2_39aff7fd",
    triangle__3: "ProBoost_triangle__3_e738f7f2",
    base__deactivating: "ProBoost_base__deactivating_7b71aa2e",
    "arrow-deactivating": "ProBoost_arrow-deactivating_7b71aa2e",
    fadeInWithScale: "ProBoost_fadeInWithScale_7b71aa2e",
    slideUp: "ProBoost_slideUp_7b71aa2e",
    blink: "ProBoost_blink_7b71aa2e",
    scale: "ProBoost_scale_7b71aa2e",
    rotate: "ProBoost_rotate_7b71aa2e",
    windowIn: "ProBoost_windowIn_7b71aa2e",
    fadeOut: "ProBoost_fadeOut_7b71aa2e",
    fadeIn: "ProBoost_fadeIn_7b71aa2e",
  },
  mc = {
    inactive: uc.base__inactive,
    activating: uc.base__activating,
    active: uc.base__active,
    deactivating: uc.base__deactivating,
  };
function pc({ className: e, doubleRow: a, state: t = "inactive", isCornerHidden: s = !1 }) {
  return "inactive" === t
    ? null
    : (0, ms.jsxs)("div", {
        className: sa(uc.base, t && mc[t], a && uc.base__double, e),
        children: [
          (0, ms.jsx)("div", { className: uc.glow }),
          !s && (0, ms.jsx)("div", { className: uc.corner }),
          (0, ms.jsx)("div", { className: uc.arrow }),
          [uc.triangle__1, uc.triangle__2, uc.triangle__3].map((e) =>
            (0, ms.jsx)("div", { className: sa(uc.triangle, e) }, e),
          ),
        ],
      });
}
var hc = "Background_1089bc1c",
  bc = "Background_wotPlus_3cf6035a",
  fc = "Background_crystal_6112fa42",
  gc = "Background_bpBonus_cf76872",
  vc = "Background_multiplier_284cda6c",
  xc = "Background_flag_beb58b8",
  wc = "Background_base__double_26effab7",
  Cc = "Background_flag__active_de322c1b",
  yc = "Background_vehicle_23ef6e2b",
  Sc = "Background_vehicle__dimmed_7f14a6c7",
  jc = "Background_crystal__limit_61072361",
  Ic = We("Favorite", "Background_favorite_d98f92cc", {
    variants: { active: { true: "Background_favorite__active_7f14a6c7" } },
  });
function Nc({ nationId: e, selected: a, active: t, className: s }) {
  return (0, ms.jsx)(be, {
    className: sa(xc, a || (t && Cc), s),
    path: `hangar.carousel.cards.flags.x400x300.${Pa(e)}`,
    position: "top left",
  });
}
var kc = Wt(function ({ vehicle: e, statistic: a, validBP: t, doubleRow: s, classNames: r }) {
  const n = _c()?.model,
    i = n?.isCrystalEarnEnabled.get() ?? !0,
    o = (x(a?.numberOfCrystalEarned ?? [], 1) ?? 0) <= (x(a?.numberOfCrystalEarned ?? [], 0) ?? 0),
    l = a?.proBoostActive,
    c = a?.fromWotPlus,
    d = i && e.crystalEarning && !c,
    _ = $(l),
    u = (n?.isDailyMultipliedXpEnabled.get() ?? !0) && oc(Number(a?.bonusMultiplier)),
    m = (0, us.useMemo)(
      () => (l ? (!1 === _ ? "activating" : "active") : _ ? "deactivating" : "inactive"),
      [l, _],
    );
  return (0, ms.jsxs)(ms.Fragment, {
    children: [
      c && (0, ms.jsx)("div", { className: sa(bc, r?.wotPlus) }),
      (0, ms.jsx)(pc, { state: m, className: r?.proBoostIcon, doubleRow: s, isCornerHidden: d }),
      d && (0, ms.jsx)("div", { className: sa(fc, o && jc, r?.crystal) }),
      a?.bpSpecial && t && (0, ms.jsx)("div", { className: sa(gc, r?.bpBonus) }),
      u && (0, ms.jsx)("div", { className: vc }),
    ],
  });
});
function Pc({
  vehicle: e,
  validBP: a,
  dimmed: t,
  active: s,
  statistic: r,
  selected: n,
  doubleRow: i,
  ...o
}) {
  return (0, ms.jsxs)("div", {
    ...o,
    className: sa(hc, i && wc, o.className),
    children: [
      (0, ms.jsx)(Nc, { nationId: e.nationId, active: s, selected: n }),
      (0, ms.jsx)(p, {
        className: sa(yc, ((r?.status && "undamaged" !== r.status) || t) && Sc),
        name: e.name,
      }),
      (0, ms.jsx)(kc, { vehicle: e, statistic: r, validBP: a, doubleRow: i }),
      (0, ms.jsx)(Ic, { active: e.favorite }),
    ],
  });
}
var Rc = "Bonuses_8169b4b3",
  Bc = "Bonuses_bonus_91f120c3",
  Ac = "Bonuses_bonus__active_2364401e",
  Ec = "Bonuses_bonusIcon_b65fb47f",
  Tc = "Bonuses_bonusValue_322db074",
  Lc = "Bonuses_bonusValue__highlighted_4bcc07c6",
  Oc = "Bonuses_rent_ea11a7e4",
  Dc = "Bonuses_base__double_ca1cd57b",
  Wc = "Bonuses_icon_3991db74",
  Vc = "Bonuses_text_a556857c",
  Mc = Qa.resolve("strings");
function zc({
  bonusMultiplier: e,
  vehicleId: a,
  restBonusEnabled: t,
  className: s,
  classNames: r,
}) {
  const n = oc(e),
    i = Ce({
      resId: R.aliases.hangar.shared.VehiclesStatistics("resId"),
      contentId: R.views.mono.rest_bonus.tooltips.rest_bonus_tooltip("resId"),
      args: { intCD: a },
      disabled: !t,
    });
  return (0, ms.jsxs)("div", {
    className: sa(Bc, -1 !== e && Ac, s),
    ...i,
    children: [
      (0, ms.jsx)("div", { className: sa(Ec, r?.icon) }),
      (0, ms.jsx)("div", {
        className: sa(Tc, r?.value, n && Lc),
        children: `${Mc.readOrEmpty("common.multiplierSmall")}${e}`,
      }),
    ],
  });
}
var $c = Wt(function ({ vehicle: e, statistic: a, doubleRow: t, ...s }) {
    const r = _c()?.model.isDailyMultipliedXpEnabled.get() ?? !0;
    return (0, ms.jsxs)("div", {
      ...s,
      className: sa(Rc, t && Dc, s.className),
      children: [
        r &&
          a &&
          (0, ms.jsx)(zc, {
            bonusMultiplier: a.bonusMultiplier,
            vehicleId: e.vehicleId,
            restBonusEnabled: a.restBonusEnabled,
          }),
        (0, ms.jsx)(g.ShortCounter, {
          time: e.rent.leftTime,
          wins: e.rent.leftWins,
          battles: e.rent.leftBattles,
          classNames: { base: Oc, icon: Wc, text: Vc },
        }),
      ],
    });
  }),
  Fc = {
    base: "Information_dd628d50",
    info: "Information_info_b2948982",
    details: "Information_details_e5340a0c",
    base__double: "Information_base__double_6e8d4f26",
    text: "Information_text_a2b2c19b",
    text__level: "Information_text__level_e5a9014e",
    text__premium: "Information_text__premium_741ebb2f",
    truncatedText: "Information_truncatedText_ede7ae03",
    battlePass: "Information_battlePass_63749625",
    battlePass__bonus: "Information_battlePass__bonus_6e8d4f26",
    battlePass__active: "Information_battlePass__active_960b5eed",
    bpPoints: "Information_bpPoints_21ee2e63",
    points: "Information_points_b67585b1",
    points__slash: "Information_points__slash_b8c7004e",
    bpShadow: "Information_bpShadow_4248ba9f",
    bpIcon: "Information_bpIcon_a622154",
    prestige: "Information_prestige_95cc4ef2",
    prestige__active: "Information_prestige__active_960b5eed",
    identifier: "Information_identifier_1bcd619a",
    identifier__changeNation: "Information_identifier__changeNation_665b13a2",
    identifier__alpha: "Information_identifier__alpha_6e8d4f26",
    identifier__super: "Information_identifier__super_46b1ed0d",
    identifier__rent: "Information_identifier__rent_1fba5dce",
    identifierIcon: "Information_identifierIcon_3636b34b",
    identifierIcon__alpha: "Information_identifierIcon__alpha_ddf4d235",
    identifierIcon__super: "Information_identifierIcon__super_34b8f5c2",
    identifierIcon__changeNation: "Information_identifierIcon__changeNation_dfee83c8",
    fadeInWithScale: "Information_fadeInWithScale_6e8d4f26",
    slideUp: "Information_slideUp_6e8d4f26",
    blink: "Information_blink_6e8d4f26",
    scale: "Information_scale_6e8d4f26",
    rotate: "Information_rotate_6e8d4f26",
    windowIn: "Information_windowIn_6e8d4f26",
    fadeOut: "Information_fadeOut_6e8d4f26",
    fadeIn: "Information_fadeIn_6e8d4f26",
  },
  Hc = We("VehicleName", {
    element: (e) => (0, ms.jsx)(f.Name, { ...e }),
    className: Fc.text,
    cva: { variants: { premium: { true: Fc.text__premium } } },
  });
function Uc({ statistic: e, vehicle: a, className: t, status: s }) {
  const r = Qa.resolve("views"),
    n = Qa.resolve("aliases"),
    i = Qa.resolve("strings"),
    o = Ce({
      resId: n.read((e) => e.hangar.shared.VehiclesStatistics("resId")),
      contentId: r.read((e) =>
        "paused" !== s
          ? e.mono.battle_pass.tooltips.vehicle_bp_points("resId")
          : e.mono.battle_pass.tooltips.on_pause("resId"),
      ),
      args: { intCD: a?.vehicleId },
    });
  return (0, ms.jsxs)("div", {
    className: sa(
      Fc.battlePass,
      e.maxBpScore > 0 && Fc.battlePass__active,
      e.bpSpecial && Fc.battlePass__bonus,
      t,
    ),
    onMouseEnter: function (e) {
      o?.onMouseEnter(e);
    },
    onMouseLeave: function (e) {
      o?.onMouseLeave();
    },
    children: [
      (0, ms.jsxs)("div", {
        className: Fc.bpPoints,
        children: [
          (0, ms.jsx)("div", {
            className: Fc.points,
            children: la.formatNumber("integral", e.bpProgress),
          }),
          (0, ms.jsx)("div", {
            className: sa(Fc.points, Fc.points__slash),
            children: i.readOrEmpty("common.common.slash"),
          }),
          (0, ms.jsx)("div", {
            className: Fc.points,
            children: la.formatNumber("integral", e.maxBpScore),
          }),
          (0, ms.jsx)("div", { className: Fc.bpShadow }),
        ],
      }),
      (0, ms.jsx)("div", { className: Fc.bpIcon }),
    ],
  });
}
function Gc({ statistic: e, elite: a, vehicle: t, selected: s, classNames: r, className: n }) {
  return (0, ms.jsxs)("div", {
    className: sa(Fc.details, n),
    children: [
      e &&
        (0, ms.jsx)(f.Prestige, {
          level: e.prestigeLevel,
          grade: e.prestigeGrade,
          type: e.prestigeType,
          direction: q.left,
          className: sa(Fc.prestige, s && Fc.prestige__active, r?.prestige),
        }),
      (0, ms.jsx)(f.Level, { className: sa(Fc.text, Fc.text__level, r?.level), value: t.level }),
      ke(t.type) &&
        (0, ms.jsx)(f.Type, {
          type: t.type,
          premium: a || e?.elite,
          size: f.Type.sizes.x24x24,
          className: r?.type,
        }),
    ],
  });
}
function qc({ vehicle: e, className: a, classNames: t }) {
  const s = Hl[e.id],
    r = e.nationChangeAvailable,
    n = e.rent.leftTime > 0 || e.rent.leftWins > 0 || e.rent.leftBattles > 0;
  return (0, ms.jsxs)("div", {
    className: sa(
      Fc.identifier,
      Fc[`identifier__${s}`],
      r && Fc.identifier__changeNation,
      n && Fc.identifier__rent,
      a,
    ),
    children: [
      (0, ms.jsx)(Hc, {
        className: t?.name,
        premium: e.premium,
        children: (0, ms.jsx)(H, { className: Fc.truncatedText, text: e.shortName }),
      }),
      (s || r) &&
        (0, ms.jsx)("div", {
          className: sa(
            Fc.identifierIcon,
            Fc[`identifierIcon__${s}`],
            r && Fc.identifierIcon__changeNation,
            t?.icon,
          ),
        }),
    ],
  });
}
var Kc = Wt(function ({ vehicle: e, statistic: a, selected: t, doubleRow: s, ...r }) {
    const n = po(),
      i = n.model.bpState.active.get(),
      o = n.model.bpState.status.get();
    return (0, ms.jsxs)("div", {
      ...r,
      className: sa(Fc.base, s && Fc.base__double, r.className),
      children: [
        a && ic(i, o, a) && (0, ms.jsx)(Uc, { vehicle: e, statistic: a, status: o }),
        (0, ms.jsxs)(f, {
          className: Fc.info,
          children: [
            (0, ms.jsx)(Gc, { vehicle: e, statistic: a, selected: t }),
            (0, ms.jsx)(qc, { vehicle: e }),
          ],
        }),
      ],
    });
  }),
  Xc = {
    base: "Overlay_ef16c91",
    alert: "Overlay_alert_db4a0e15",
    alertIcon: "Overlay_alertIcon_3d7c077a",
    base__double: "Overlay_base__double_3c7155a",
    alertText: "Overlay_alertText_ca764641",
    alertText__light: "Overlay_alertText__light_bece984e",
    fadeInWithScale: "Overlay_fadeInWithScale_3c7155a",
    slideUp: "Overlay_slideUp_3c7155a",
    blink: "Overlay_blink_3c7155a",
    scale: "Overlay_scale_3c7155a",
    rotate: "Overlay_rotate_3c7155a",
    windowIn: "Overlay_windowIn_3c7155a",
    fadeOut: "Overlay_fadeOut_3c7155a",
    fadeIn: "Overlay_fadeIn_3c7155a",
  };
We("Disable", Xc.disable);
function Zc({ status: e, classNames: a, className: t }) {
  const s = Qa.resolve("images"),
    n = V(`hangar.carousel.cards.alerts.${nc[e]}`, `hangar.carousel.cards.alerts.${nc[e]}_upscale`),
    i = V(
      "hangar.carousel.cards.alerts.notSuitable",
      "hangar.carousel.cards.alerts.notSuitable_upscale",
    ),
    o = e === sc || e === tc;
  return (0, ms.jsxs)("div", {
    className: sa(Xc.alert, t),
    children: [
      (0, ms.jsx)(be, { className: sa(Xc.alertIcon, a?.icon), path: s.has(n) ? n : i }),
      (0, ms.jsx)(r, {
        upgradeLegacy: !0,
        className: sa(Xc.alertText, o && Xc.alertText__light, a?.text),
        path: `menu.tankCarousel.vehicleStates.${e}`,
        params: { icon: (0, ms.jsx)(be, { path: "library.premium_small", width: 34, height: 16 }) },
      }),
    ],
  });
}
function Jc({ statistic: e, doubleRow: a, ...t }) {
  return "undamaged" === e.status
    ? null
    : (0, ms.jsx)("div", {
        ...t,
        className: sa(Xc.base, a && Xc.base__double, t.className),
        children: (0, ms.jsx)(Zc, { status: e.status }),
      });
}
var Qc = "Card_e79008fd",
  Yc = "Card_base__double_f8b7f334",
  ed = "Card_content_a6141b08",
  ad = "Card_border_e9cb9a85",
  td = Qa.resolve("views"),
  sd = Qa.resolve("aliases"),
  rd = Wt(function ({
    vehicleId: e,
    selected: a = !1,
    doubleRow: t,
    children: s,
    concurrent: r,
    ...n
  }) {
    const i = po(),
      o = Hi().model.get(e),
      l = $i().model.get(e),
      c = ge(),
      d = i.model.current.inventoryId.get(),
      _ = i.model.prebattleModeActive(),
      u = i.model.bpState.active.get(),
      m = i.model.bpState.status.get();
    if (!o || !l) return (0, ms.jsx)(jl, { ...n });
    const p = r ? nd : Pc;
    return (0, ms.jsxs)(jl, {
      ...n,
      className: sa("vehicle-card", n.className),
      selected: a,
      "data-test-id": `vehicleCard-${e}`,
      onMouseEnter: function (e) {
        (c.play("mouse-enter", { target: "vehicle-card", original: e }), n.onMouseEnter?.(e));
      },
      onMouseLeave: function (e) {
        n.onMouseLeave?.(e);
      },
      onClick: function (e) {
        _ ||
          (o && o.inventoryId === d) ||
          (c.play("click", { target: "vehicle-card", original: e }),
          i.controls.select(o.inventoryId),
          n.onClick?.(e));
      },
      children: [
        (0, ms.jsx)(p, {
          vehicle: o,
          validBP: ic(u, m, l),
          dimmed: _,
          statistic: l,
          selected: a,
          doubleRow: t,
        }),
        (0, ms.jsx)(id, {
          concurrent: r,
          statistic: l,
          vehicle: o,
          selected: a,
          disableContextMenu: _,
          doubleRow: t,
        }),
      ],
    });
  });
function nd(e) {
  const [a, t] = (0, us.useState)(!0),
    [, s] = (0, us.useTransition)();
  return (
    (0, us.useEffect)(() => {
      a && s(() => t(!1));
    }, [a]),
    a ? null : (0, ms.jsx)(Pc, { ...e })
  );
}
function id({
  vehicle: e,
  statistic: a,
  selected: t,
  doubleRow: s,
  concurrent: r,
  disableContextMenu: n,
}) {
  const [i, o] = (0, us.useState)(r),
    [, l] = (0, us.useTransition)(),
    c = Ye(
      "vehicle",
      (0, us.useMemo)(() => ({ inventoryId: e?.inventoryId }), [e?.inventoryId]),
    ),
    d = Ce({
      resId: sd.read((e) => e.hangar.shared.VehiclesInventory("resId")),
      contentId: td.read((e) => e.mono.hangar.vehicle_tooltip("resId")),
      args: us.useMemo(() => ({ inventoryId: e?.inventoryId }), [e?.inventoryId]),
    });
  return (
    (0, us.useEffect)(() => {
      i && l(() => o(!1));
    }, [i]),
    i
      ? null
      : (0, ms.jsxs)("div", {
          ...d,
          ...(!n && c),
          className: sa(Qc, s && Yc),
          children: [
            (0, ms.jsxs)("div", {
              className: ed,
              children: [
                (0, ms.jsx)(Kc, { vehicle: e, selected: t, statistic: a, doubleRow: s }),
                (0, ms.jsx)($c, { vehicle: e, statistic: a, doubleRow: s }),
              ],
            }),
            (0, ms.jsx)(Jc, { statistic: a, doubleRow: s }),
          ],
        })
  );
}
var od = {
  empty: "ActiveSlots_empty_9aab1ce1",
  doubleSlots: "ActiveSlots_doubleSlots_2ce42013",
  slot__double: "ActiveSlots_slot__double_e321ab18",
  fadeInWithScale: "ActiveSlots_fadeInWithScale_54b124fa",
  slideUp: "ActiveSlots_slideUp_54b124fa",
  blink: "ActiveSlots_blink_54b124fa",
  scale: "ActiveSlots_scale_54b124fa",
  rotate: "ActiveSlots_rotate_54b124fa",
  windowIn: "ActiveSlots_windowIn_54b124fa",
  fadeOut: "ActiveSlots_fadeOut_54b124fa",
  fadeIn: "ActiveSlots_fadeIn_54b124fa",
};
function ld({ width: e, className: a }) {
  return (0, ms.jsx)("div", {
    className: od.empty,
    children: (0, ms.jsx)(jl, {
      className: a,
      style: { width: `${e}px` },
      children: (0, ms.jsx)("div", { className: od.vehicleSlot }),
    }),
  });
}
function cd({ slotId: e, width: a, currentVehicleId: t, double: s, className: r }) {
  const n = (function (e) {
    const a = go(),
      t = Boolean(a && a.model.computeds.enabled()),
      s = !a || a.model.computeds.isVehiclePlaylistsEmpty(),
      r = Ee(() => {
        t && !s && a.model.vehicleId.get() === e && a.controls.reset();
      });
    return (0, us.useMemo)(() => {
      if (t && !s) return { "data-popover-trigger-id": Qo(e), onMouseDown: r };
    }, [s, t, r, e]);
  })(Number(e));
  return void 0 === e
    ? null
    : e in Il
      ? (0, ms.jsx)(Vl, { className: sa(ad, r), type: e, width: a, doubleRow: s })
      : "emptySlot" === e
        ? (0, ms.jsx)(ld, { className: sa(ad, r), width: a })
        : (0, ms.jsx)(rd, {
            ...n,
            vehicleId: e,
            selected: e === t,
            doubleRow: s,
            className: sa(ad, r),
            style: { width: a },
          });
}
function dd({ chunkedSlots: e, classNames: a, ...t }) {
  return void 0 === e
    ? null
    : (0, ms.jsx)("div", {
        className: od.doubleSlots,
        children: e.map((e, s) =>
          (0, ms.jsx)(cd, { ...t, slotId: e, className: sa(od.slot__double, a?.slot) }, s),
        ),
      });
}
var _d = {
  button: "ArrowButton_button_7654af94",
  icon: "ArrowButton_icon_35e5294f",
  button__left: "ArrowButton_button__left_5327085d",
  background: "ArrowButton_background_5327085d",
  border: "ArrowButton_border_5327085d",
  overlay: "ArrowButton_overlay_c36cbc33",
  content: "ArrowButton_content_4666fd05",
  button__right: "ArrowButton_button__right_5327085d",
  fadeInWithScale: "ArrowButton_fadeInWithScale_5327085d",
  slideUp: "ArrowButton_slideUp_5327085d",
  blink: "ArrowButton_blink_5327085d",
  scale: "ArrowButton_scale_5327085d",
  rotate: "ArrowButton_rotate_5327085d",
  windowIn: "ArrowButton_windowIn_5327085d",
  fadeOut: "ArrowButton_fadeOut_5327085d",
  fadeIn: "ArrowButton_fadeIn_5327085d",
};
function ud({ direction: e, className: a, ...t }) {
  return (0, ms.jsx)(yt, {
    ...t,
    classNames: {
      base: sa(_d.button, _d[`button__${e}`], a),
      background: _d.background,
      border: _d.border,
      overlay: _d.overlay,
      content: _d.content,
    },
    theme: yt.themes.secondary,
    size: yt.sizes.small,
    autoAlignContent: !1,
    soundTarget: "carousel:arrow_button",
    children: (0, ms.jsx)(be, { path: "hangar.carousel.buttonArrow", className: _d.icon }),
  });
}
ud.direction = { right: "right", left: "left" };
var md = {
  navButtonWrapper: "CarouselNavButtons_navButtonWrapper_a13c2a68",
  navButton: "CarouselNavButtons_navButton_adcc2e9b",
  navButton__left: "CarouselNavButtons_navButton__left_5f6dc3a0",
  navButton__right: "CarouselNavButtons_navButton__right_66b4f03f",
  navButton__hidden: "CarouselNavButtons_navButton__hidden_69011a0b",
  mask: "CarouselNavButtons_mask_17bb1a0e",
  mask__both: "CarouselNavButtons_mask__both_7294632e",
  mask__left: "CarouselNavButtons_mask__left_e8bc4c90",
  mask__right: "CarouselNavButtons_mask__right_6be519f7",
  fadeInWithScale: "CarouselNavButtons_fadeInWithScale_3f67251c",
  slideUp: "CarouselNavButtons_slideUp_3f67251c",
  blink: "CarouselNavButtons_blink_3f67251c",
  scale: "CarouselNavButtons_scale_3f67251c",
  rotate: "CarouselNavButtons_rotate_3f67251c",
  windowIn: "CarouselNavButtons_windowIn_3f67251c",
  fadeOut: "CarouselNavButtons_fadeOut_3f67251c",
  fadeIn: "CarouselNavButtons_fadeIn_3f67251c",
};
function pd(e) {
  return ({ button: a }) => {
    0 === a && e();
  };
}
function hd({ itemWidth: e, api: a, children: t }) {
  const s = (0, us.useRef)(null),
    [r, n] = (0, us.useState)(!1),
    { applyScroll: i, animationScroll: o, disabled: l } = a,
    [c, d] = xt(a),
    _ = c || l,
    u = d || l;
  function m(a) {
    function t() {
      i(o.scrollPosition.get() + a * e);
    }
    r || (t(), (s.current = window.setInterval(t, 100)), n(!0));
  }
  function p() {
    (null !== s.current && (clearInterval(s.current), (s.current = null)), n(!1));
  }
  return (0, ms.jsxs)("div", {
    className: md.navButtonWrapper,
    children: [
      (0, ms.jsx)(ud, {
        direction: ud.direction.left,
        onMouseDown: pd(() => m(-1)),
        onMouseUp: p,
        onMouseLeave: p,
        className: sa(md.navButton, md.navButton__left, _ && md.navButton__hidden),
      }),
      (0, ms.jsx)("div", { className: sa(md.mask, md[`mask__${cl(c, d)}`]), children: t }),
      (0, ms.jsx)(ud, {
        direction: ud.direction.right,
        onMouseDown: pd(() => m(1)),
        onMouseUp: p,
        onMouseLeave: p,
        className: sa(md.navButton, md.navButton__right, u && md.navButton__hidden),
      }),
    ],
  });
}
var bd = {
    base: "CarouselScroll_3690a837",
    areaContent: "CarouselScroll_areaContent_f5dd7772",
    fadeInWithScale: "CarouselScroll_fadeInWithScale_57c79593",
    slideUp: "CarouselScroll_slideUp_57c79593",
    blink: "CarouselScroll_blink_57c79593",
    scale: "CarouselScroll_scale_57c79593",
    rotate: "CarouselScroll_rotate_57c79593",
    windowIn: "CarouselScroll_windowIn_57c79593",
    fadeOut: "CarouselScroll_fadeOut_57c79593",
    fadeIn: "CarouselScroll_fadeIn_57c79593",
  },
  fd = "dragging",
  gd = "idle";
function vd({
  api: e,
  children: a,
  className: t,
  areaClassNames: s,
  staticContent: r,
  disabled: n,
  onDraggingState: i,
}) {
  const { animationScroll: o, applyScroll: l, setDisabled: c } = e,
    d = ja(e, Fa.horizontal, void 0, { gapBeforeStart: 5 });
  return (
    (0, us.useEffect)(() => {
      i?.(d.type === fd);
    }, [d.type, i]),
    (0, us.useEffect)(() => {
      c(n);
    }, [n, c]),
    (0, us.useEffect)(
      () =>
        na(() => {
          d.type === gd && o.scrollPosition.idle && l(o.scrollPosition.get());
        }),
      [o.scrollPosition, d, l],
    ),
    (0, ms.jsx)("div", {
      className: sa(bd.base, t),
      children: (0, ms.jsxs)(Ca, {
        className: s?.base,
        classNames: {
          wrapper: sa(bd.areaWrapper, s?.wrapper),
          content: sa(bd.areaContent, s?.content),
        },
        children: [a, r],
      }),
    })
  );
}
var xd = "CarouselSkeleton_1ac002e3",
  wd = "CarouselSkeleton_content_b18f8dd7",
  Cd = "CarouselSkeleton_scroll_badf82c7";
function yd(e) {
  return (0, ms.jsx)("div", { ...e, className: sa(wd, e.className) });
}
function Sd({
  api: e,
  widthElement: a,
  totalElements: t,
  disabled: s,
  onDraggingState: r,
  renderElement: n,
  classNames: i,
}) {
  return (0, ms.jsx)("div", {
    className: sa(xd, i?.base),
    children: (0, ms.jsx)(hd, {
      api: e,
      itemWidth: a,
      children: (0, ms.jsx)(we, {
        api: e,
        elementWidth: a - De(1),
        direction: "horizontal",
        totalElements: t,
        wrappers: { Content: yd },
        className: sa(Cd, i?.scroll),
        renderScroll: (a) =>
          (0, ms.jsx)(vd, { ...a, api: e, disabled: s, onDraggingState: r, children: a.children }),
        renderElement: (e) => (n ? n(e) : (0, ms.jsx)(ld, { className: i?.element, width: a })),
      }),
    }),
  });
}
function jd(e, a, t, s) {
  return (0, us.useMemo)(() => {
    if (!a) return { activeSlotsAmount: 0, activeSlotsIds: [] };
    const r = ((e, a) => ({
        left: [...(a != uo ? [Il.rentTank] : [])],
        right: [Il.buyTank, ...(e > 0 ? [Il.restoreTank] : []), Il.buySlot],
      }))(t, s),
      n = e.length + r.right.length + r.left.length,
      i = Math.max(0, a - n);
    return {
      activeSlotsAmount: n,
      activeSlotsIds: [...r.left, ...e, ...r.right, ...Array(i).fill(al)],
    };
  }, [t, e, a, s]);
}
function Id({ api: e, carouselRows: a }) {
  const t = (function (e) {
      const a = at(ll.default, ll.breakpoints);
      return De(2 === e ? a.double : a.single);
    })(a),
    [s, r] = (0, us.useState)({ carouselRows: 0, cardWidth: 0, visibleSlots: 0 });
  return (
    (0, us.useLayoutEffect)(() => {
      function s() {
        const s = e.getWrapperSize();
        s &&
          r(
            2 !== a
              ? { visibleSlots: Math.ceil(s / t), cardWidth: t, carouselRows: a }
              : { visibleSlots: Math.ceil((s / t) * a), cardWidth: t, carouselRows: a },
          );
      }
      return (
        s(),
        new he().add(e.events.on("resizeHandled", s)).add(e.events.on("recalculateContent", s))
          .dispose
      );
    }, [e, t, a]),
    s
  );
}
var Nd = "Carousel_draggingOverlay_2ac699b0",
  kd = "Carousel_9b3e04da",
  Pd = "Carousel_base__visible_24d53d12",
  Rd = "Carousel_card_5449ec9a",
  Bd = "Carousel_card__inactive_c59331d9",
  Ad =
    (Wt(function () {
      const e = go(),
        [a, t] = (0, us.useState)(!1),
        { api: s } = Rt(),
        r = po(),
        n = Vi().model.carouselRowCount.get(),
        i = r.model.prebattleModeActive(),
        o = r.model.telecomRentStatus.get(),
        l = r.model.current.ids(),
        c = r.model.current.list(),
        d = r.model.selectedVehicle()?.id,
        { currentIndex: _ } = (function (e, a) {
          return (0, us.useMemo)(() => {
            if (!a) return { currentIndex: -1, currentPosition: -1 };
            const t = e.indexOf(a);
            return { currentIndex: t, currentPosition: t >= 0 ? t + 1 : -1 };
          }, [e, a]);
        })(l, d),
        u = $(d),
        m = r.model.slots.recover.get(),
        { carouselRows: p, cardWidth: h, visibleSlots: b } = Id({ api: s, carouselRows: n }),
        { activeSlotsAmount: f, activeSlotsIds: g } = jd(l, b, m, o),
        v =
          ((x = g),
          (0, us.useMemo)(() => {
            const e = [];
            for (let a = 0; a < x.length; a += 2) e.push(x.slice(a, a + 2));
            return (1 === e.at(-1)?.length && e.at(-1)?.push(al), e);
          }, [x]));
      var x;
      ((0, us.useEffect)(() => {
        const e = Ie(500, !0, () =>
          $e.contextMenu.hide(
            0,
            Qa.resolve("aliases").read((e) => e.common.contextMenu.Backport("resId")),
          ),
        );
        return (
          s.events.on("change", e),
          () => {
            (e.cancel(), s.events.off("change", e));
          }
        );
      }, [s]),
        (function (e, a, t, s, r, n) {
          const i = (0, us.useRef)(null);
          (0, us.useLayoutEffect)(() => {
            function o() {
              const o = e.getWrapperSize(),
                l = e.animationScroll.scrollPosition.get();
              if (!o) return;
              n && e.applyScroll(0, { immediate: !0 });
              const c = t - De(1),
                d = l,
                _ = l + o,
                u = c * Math.floor(a / s),
                m = u + c,
                p = u - (Math.floor(o / c) / 2) * c;
              if (u > d && m < _)
                return (
                  i.current && r && i.current - r !== 0 && e.applyScroll(p, { immediate: !0 }),
                  void (i.current = r)
                );
              ((i.current = r), e.applyScroll(p, { immediate: !0 }));
            }
            return (
              o(),
              new he()
                .add(e.events.on("resizeHandled", o))
                .add(e.events.on("recalculateContent", o)).dispose
            );
          }, [a, e, t, s, n, r]);
        })(s, _, h, p, l.length, b > f),
        (function (e, a, t, s, r) {
          const n = 2 === s;
          function i(s) {
            t(-1 !== e ? a[e + s].inventoryId : a[0].inventoryId);
          }
          const o = [
            {
              key: D.ARROW_DOWN,
              blockKey: !n || e % s === s - 1 || e === a.length - 1,
              action: () => i(1),
            },
            { key: D.ARROW_UP, blockKey: !n || e % s === 0, action: () => i(-1) },
            { key: D.ARROW_LEFT, blockKey: n ? e < s : 0 === e, action: () => i(-s) },
            {
              key: D.ARROW_RIGHT,
              blockKey: n ? e > a.length - (s + 1) : e === a.length - 1,
              action: () => i(s),
            },
            { key: D.HOME, blockKey: 0 === a.length, action: () => t(a[0].inventoryId) },
            { key: D.END, blockKey: 0 === a.length, action: () => t(a[a.length - 1].inventoryId) },
          ];
          for (const { key: l, blockKey: c, action: d } of o) {
            const e = r || c ? D.NONE : l;
            At(e, d);
          }
        })(_, c, r.controls.select, p, 0 === l.length || i));
      const w = (function (e, a) {
        const [t, s] = (0, us.useState)(0 === a),
          r = se();
        return (
          (0, us.useEffect)(() => {
            if (t || 0 === a) return s(!0);
            function n() {
              (s(!0), i.dispose(), r.clear());
            }
            r.run(n);
            const i = new he()
              .add(r.clear)
              .add(e.events.on("resizeHandled", () => r.run(n)))
              .add(e.events.on("recalculateContent", () => r.run(n)));
            return i.dispose;
          }, [e, a, t, r]),
          t
        );
      })(s, l.length);
      return (
        (0, us.useEffect)(() => {
          e && e.model.computeds.enabled() && d !== u && e.controls.reset();
        }, [d, u, e]),
        (0, ms.jsxs)(ms.Fragment, {
          children: [
            (0, ms.jsx)(Sd, {
              api: s,
              widthElement: h,
              totalElements: 2 === p ? v.length : g.length,
              disabled: b > f,
              onDraggingState: t,
              classNames: { base: sa(kd, w && Pd), element: sa(Rd, a && Bd) },
              renderElement: (e) => {
                const t = sa(Rd, a && Bd);
                return 2 === p
                  ? (0, ms.jsx)(te, {
                      failure: () => (0, ms.jsx)(ld, { className: t, width: h }),
                      children: (0, ms.jsx)(
                        dd,
                        {
                          chunkedSlots: v[e],
                          currentVehicleId: d,
                          width: h,
                          classNames: { slot: t },
                          double: !0,
                        },
                        e,
                      ),
                    })
                  : (0, ms.jsx)(te, {
                      failure: () => (0, ms.jsx)(ld, { className: t, width: h }),
                      children: (0, ms.jsx)(
                        cd,
                        { slotId: g[e], currentVehicleId: d, width: h, className: t, double: !1 },
                        g[e] ?? e,
                      ),
                    });
              },
            }),
            e &&
              e.model.computeds.enabled() &&
              (0, ms.jsx)(Yo, { freeSpaceRem: 0, tipSize: "32rem" }),
            el.createPortal(a && (0, ms.jsx)("div", { className: Nd }), document.body),
          ],
        })
      );
    }),
    "ActiveCardHeader_235d362d"),
  Ed = "ActiveCardHeader_activeText_530ba0e9",
  Td = "ActiveCardHeader_idleVideo_b2e26623",
  Ld = function ({ text: e, videoSrc: a, className: t = "", classNames: s }) {
    return (0, ms.jsxs)("div", {
      className: sa(Ad, t),
      children: [
        (0, ms.jsx)("div", { className: sa(Ed, s?.activeText), children: e }),
        (0, ms.jsx)(K, { className: sa(Td, s?.idleVideo), src: a, autoplay: !0, loop: !0 }),
      ],
    });
  },
  Od = "Content_8ce13fac",
  Dd = "Content_base__disabled_da09528a",
  Wd = "Content_base__selected_da09528a";
function Vd({ children: e, selected: a, disabled: t }) {
  return (0, ms.jsx)("div", { className: sa(Od, a && Wd, t && Dd), children: e });
}
var Md = "Slot_750e4447",
  zd = "Slot_base__disabled_440d6866",
  $d = "Slot_content_27d2b58",
  Fd = "Slot_base__active_71f19f5c",
  Hd = "Slot_base__selected_71f19f5c",
  Ud = "Slot_selected_302eadc9",
  Gd = "Slot_selected__border_e2a17304";
function qd({
  children: e,
  selected: a = !1,
  disabled: t = !1,
  active: s = !1,
  className: r,
  ...n
}) {
  return (0, ms.jsx)("div", {
    ...n,
    className: sa(Md, s && Fd, a && Hd, t && zd, r),
    children: (0, ms.jsxs)("div", {
      className: $d,
      children: [
        (0, ms.jsx)(Vd, { selected: a, disabled: t, children: e }),
        a && (0, ms.jsx)("div", { className: sa(Ud, Gd) }),
        (0, ms.jsx)("div", { className: Ud }),
      ],
    }),
  });
}
var Kd = "regular",
  Xd = "postprogression",
  Zd = "extra",
  Jd = (e, a) => (e ? Zd : a ? Xd : Kd),
  Qd = {
    regular: {
      extraSmall: {
        cardWidth: "262rem",
        cardHeight: "166rem",
        rewardWidth: "288rem",
        rewardHeight: "192rem",
      },
      small: {
        cardWidth: "262rem",
        cardHeight: "166rem",
        rewardWidth: "288rem",
        rewardHeight: "192rem",
      },
      medium: {
        cardWidth: "326rem",
        cardHeight: "206rem",
        rewardWidth: "360rem",
        rewardHeight: "240rem",
      },
      large: {
        cardWidth: "406rem",
        cardHeight: "256rem",
        rewardWidth: "450rem",
        rewardHeight: "300rem",
      },
      extraLarge: {
        cardWidth: "486rem",
        cardHeight: "306rem",
        rewardWidth: "540rem",
        rewardHeight: "360rem",
      },
    },
    postprogression: {
      extraSmall: {
        cardWidth: "198rem",
        cardHeight: "166rem",
        rewardWidth: "192rem",
        rewardHeight: "192rem",
      },
      small: {
        cardWidth: "198rem",
        cardHeight: "166rem",
        rewardWidth: "192rem",
        rewardHeight: "192rem",
      },
      medium: {
        cardWidth: "246rem",
        cardHeight: "206rem",
        rewardWidth: "240rem",
        rewardHeight: "240rem",
      },
      large: {
        cardWidth: "306rem",
        cardHeight: "256rem",
        rewardWidth: "300rem",
        rewardHeight: "300rem",
      },
      extraLarge: {
        cardWidth: "366rem",
        cardHeight: "306rem",
        rewardWidth: "360rem",
        rewardHeight: "360rem",
      },
    },
    extra: {
      extraSmall: {
        cardWidth: "262rem",
        cardHeight: "230rem",
        rewardWidth: "288rem",
        rewardHeight: "256rem",
      },
      small: {
        cardWidth: "262rem",
        cardHeight: "230rem",
        rewardWidth: "288rem",
        rewardHeight: "256rem",
      },
      medium: {
        cardWidth: "326rem",
        cardHeight: "286rem",
        rewardWidth: "360rem",
        rewardHeight: "320rem",
      },
      large: {
        cardWidth: "406rem",
        cardHeight: "356rem",
        rewardWidth: "450rem",
        rewardHeight: "400rem",
      },
      extraLarge: {
        cardWidth: "486rem",
        cardHeight: "426rem",
        rewardWidth: "540rem",
        rewardHeight: "480rem",
      },
    },
  },
  Yd = {
    base: "Status_d06498e2",
    icon: "Status_icon_1af01ceb",
    base__done: "Status_base__done_35b9a31c",
    base__locked: "Status_base__locked_35b9a31c",
    line: "Status_line_324edf86",
    shadow: "Status_shadow_75136b3b",
    glowInner: "Status_glowInner_3e65d7dc",
    blur: "Status_blur_fe6f30fc",
    glowBig: "Status_glowBig_156fcd01",
    fadeInWithScale: "Status_fadeInWithScale_35b9a31c",
    slideUp: "Status_slideUp_35b9a31c",
    blink: "Status_blink_35b9a31c",
    scale: "Status_scale_35b9a31c",
    rotate: "Status_rotate_35b9a31c",
    windowIn: "Status_windowIn_35b9a31c",
    fadeOut: "Status_fadeOut_35b9a31c",
    fadeIn: "Status_fadeIn_35b9a31c",
  },
  e_ = ({ type: e, className: a }) =>
    (0, ms.jsxs)("div", {
      className: sa(Yd.base, Yd[`base__${e}`], a),
      children: [
        (0, ms.jsx)("div", { className: Yd.glowBig }),
        (0, ms.jsx)("div", { className: Yd.line }),
        (0, ms.jsx)("div", { className: Yd.shadow }),
        (0, ms.jsx)("div", { className: Yd.glowInner }),
        (0, ms.jsx)("svg", {
          width: "42",
          height: "42",
          viewBox: "0 0 42 42",
          className: Yd.blur,
          children: (0, ms.jsx)("g", {
            children: (0, ms.jsx)("circle", { cx: "21", cy: "21", r: "3" }),
          }),
        }),
        (0, ms.jsx)("div", { className: sa(Yd.icon) }),
      ],
    }),
  a_ = "UnlockedState_d8033d83",
  t_ = "UnlockedState_stages_ef0d6acd",
  s_ = "UnlockedState_mainStage_286ea378",
  r_ = "UnlockedState_additionalStage_83045438",
  n_ = "UnlockedState_cycleText_5b49e844",
  i_ = R.strings.battle_pass.chapterChoice,
  o_ = function ({ currentLevel: e, cyclesCompletedCount: a, maxLevel: t }) {
    const s = (e - 1) % t;
    return (0, ms.jsxs)("div", {
      className: a_,
      children: [
        (0, ms.jsx)(aa, {
          classMix: n_,
          text: i_.postprogression.unlocked.cycle(),
          binding: { cycle: a + 1 },
        }),
        (0, ms.jsxs)("div", {
          className: t_,
          children: [
            (0, ms.jsx)("span", { className: s_, children: `${s}` }),
            (0, ms.jsx)(aa, { classMix: r_, text: i_.stages.additional(), binding: { level: t } }),
          ],
        }),
      ],
    });
  },
  l_ = "PostprogressionInfo_f8fcfc44",
  c_ = "PostprogressionInfo_lockedText_c823728d",
  d_ = R.strings.battle_pass.chapterChoice,
  __ = Wt(function ({ chapterID: e }) {
    const { model: a } = vi(),
      t = a.computes.getChapterById(e);
    if (!t) return;
    const { currentLevel: s, cyclesCompletedCount: r, maxLevel: n } = t,
      i = a.computes.regularChapters().length - 1 !== a.computes.regularChaptersCompleteCount();
    return (0, ms.jsx)("div", {
      className: l_,
      children: i
        ? (0, ms.jsx)(_a, {
            className: c_,
            text: d_.postprogression.locked(),
            params: { count: a.computes.regularChapters().length - 1 },
          })
        : (0, ms.jsx)(o_, { currentLevel: s, cyclesCompletedCount: r, maxLevel: n }),
    });
  }),
  u_ = "CompletedState_completeText_f209b72f",
  m_ = "CompletedState_completeText__bought_4533734f",
  p_ = R.strings.battle_pass.chapterChoice,
  h_ = function ({ isBought: e, chapterRewardsCount: a }) {
    return (0, ms.jsx)(ms.Fragment, {
      children: e
        ? (0, ms.jsx)("div", { className: sa(u_, m_), children: p_.stages.complete.improved() })
        : (0, ms.jsx)(aa, {
            classMix: u_,
            text: p_.stages.complete.unimproved(),
            binding: { count: a },
          }),
    });
  },
  b_ = "UncompletedState_9e8c0393",
  f_ = "UncompletedState_mainStage_5808557f",
  g_ = "UncompletedState_additionalStage_ef80ee9c",
  v_ = R.strings.battle_pass.chapterChoice,
  x_ = function ({ currentLevel: e, maxStages: a }) {
    return (0, ms.jsxs)("div", {
      className: b_,
      children: [
        (0, ms.jsx)("span", { className: f_, children: "" + (e - 1) }),
        (0, ms.jsx)(aa, { classMix: g_, text: v_.stages.additional(), binding: { level: a } }),
      ],
    });
  },
  w_ = "RegularInfo_46f7818d",
  C_ = "RegularInfo_uncomplete_854e3542",
  y_ =
    (R.strings.battle_pass.chapterChoice,
    Wt(function ({ chapterID: e }) {
      const { model: a } = vi(),
        t = a.computes.getChapterById(e);
      if (!t) return;
      const {
        currentLevel: s,
        chapterState: r,
        isBought: n,
        chapterRewardsCount: i,
        maxLevel: o,
      } = t;
      return (0, ms.jsx)("div", {
        className: w_,
        children:
          r === Qt.Completed
            ? (0, ms.jsx)(h_, { isBought: n, chapterRewardsCount: i })
            : (0, ms.jsx)("div", {
                className: C_,
                children: (0, ms.jsx)(x_, { currentLevel: s, maxStages: o }),
              }),
      });
    })),
  S_ = {
    base: "CardInfo_7298ebd2",
    base__postprogression: "CardInfo_base__postprogression_f10eeba",
    infoIcon: "CardInfo_infoIcon_fe2dde8d",
    infoIcon__x60x60: "CardInfo_infoIcon__x60x60_69dd0923",
    infoIcon__x80x80: "CardInfo_infoIcon__x80x80_39f83cbc",
    infoIcon__x120x120: "CardInfo_infoIcon__x120x120_a47141e5",
    infoDescription: "CardInfo_infoDescription_af2ed432",
    chapterName: "CardInfo_chapterName_91c4f3ea",
    chapterName__bought: "CardInfo_chapterName__bought_a3ef657b",
    fadeInWithScale: "CardInfo_fadeInWithScale_8e8a9c2",
    slideUp: "CardInfo_slideUp_8e8a9c2",
    blink: "CardInfo_blink_8e8a9c2",
    scale: "CardInfo_scale_8e8a9c2",
    rotate: "CardInfo_rotate_8e8a9c2",
    windowIn: "CardInfo_windowIn_8e8a9c2",
    fadeOut: "CardInfo_fadeOut_8e8a9c2",
    fadeIn: "CardInfo_fadeIn_8e8a9c2",
  },
  j_ = Qa.resolve("images"),
  I_ = Qa.resolve("strings"),
  N_ = R.strings.battle_pass.chapterChoice,
  k_ = Wt(function ({ chapterID: e, className: a = "" }) {
    const { model: t } = vi(),
      { breakpoint: s } = Me(),
      r = t.computes.getChapterById(e),
      n = at({ iconSize: tn }, { large: { iconSize: sn }, extraLarge: { iconSize: nn } }),
      i = V(n.iconSize, on);
    if (!r) return;
    const { isBought: o, isPostProgression: l, isExtra: c } = r,
      d = Jd(c, l),
      _ = (() => {
        const a = String(e).slice(-1);
        return (
          j_.readOrEmpty(
            `battlePass.emblem.icon.c_${e}.${o ? "purchased" : "basic"}.${i}`,
            "silent",
          ) ||
          j_.readOrEmpty(`battlePass.emblem.icon.default_${a}.${o ? "purchased" : "basic"}.${i}`)
        );
      })();
    return (0, ms.jsxs)("div", {
      className: sa(S_.base, l && S_.base__postprogression),
      children: [
        (0, ms.jsx)("div", {
          className: sa(S_.infoIcon, S_[`infoIcon__${n.iconSize}`]),
          style: { backgroundImage: `url(${_})` },
        }),
        (0, ms.jsxs)("div", {
          className: S_.infoDescription,
          style: { "--card-width": Qd[d][s.name].cardWidth },
          children: [
            (0, ms.jsx)("div", {
              className: sa(S_.chapterName, o && S_.chapterName__bought),
              children: l
                ? N_.postprogression.name()
                : I_.readOrEmpty(`battle_pass.chapter.fullName.c_${e}`),
            }),
            l ? (0, ms.jsx)(__, { chapterID: e }) : (0, ms.jsx)(y_, { chapterID: e }),
          ],
        }),
      ],
    });
  }),
  P_ = {
    base: "CardTemplate_664f5f0d",
    bg: "CardTemplate_bg_e653648c",
    reward: "CardTemplate_reward_4b474b06",
    base__paused: "CardTemplate_base__paused_5ee959db",
    base__notStarted: "CardTemplate_base__notStarted_5ee959db",
    base__completed: "CardTemplate_base__completed_5ee959db",
    base__selected: "CardTemplate_base__selected_5ee959db",
    progressBar: "CardTemplate_progressBar_9b805b48",
    progressBar__active: "CardTemplate_progressBar__active_5ddba882",
    progressBarBg: "CardTemplate_progressBarBg_5ee959db",
    info: "CardTemplate_info_b6b5a8af",
    status: "CardTemplate_status_4dbaa00d",
    fadeInWithScale: "CardTemplate_fadeInWithScale_5ee959db",
    slideUp: "CardTemplate_slideUp_5ee959db",
    blink: "CardTemplate_blink_5ee959db",
    scale: "CardTemplate_scale_5ee959db",
    rotate: "CardTemplate_rotate_5ee959db",
    windowIn: "CardTemplate_windowIn_5ee959db",
    fadeOut: "CardTemplate_fadeOut_5ee959db",
    fadeIn: "CardTemplate_fadeIn_5ee959db",
  },
  R_ = Qa.resolve("images"),
  B_ = (e, a = !1) => (e === Qt.Completed ? fe.done : a ? fe.locked : void 0),
  A_ = Wt(function ({ chapterID: e, classNames: a = {} }) {
    const { model: t } = vi(),
      { breakpoint: s } = Me(),
      r = t.computes.getChapterById(e);
    if (!r) return;
    const { chapterState: n, isExtra: i, isPostProgression: o, currentLevel: l, maxLevel: c } = r,
      d = Jd(i, o),
      _ = e === t.selectedChapterID.get(),
      u =
        t.computes.regularChapters().length - 1 !== t.computes.regularChaptersCompleteCount() && o,
      m = String(e).slice(-1),
      p =
        R_.readOrEmpty(`battlePass.chapter_choice.card_bg.c_${e}`, "silent") ||
        R_.readOrEmpty(`battlePass.chapter_choice.card_bg.default_${m}`),
      h =
        R_.readOrEmpty(`battlePass.chapter_choice.tanks.c_${e}`, "silent") ||
        R_.readOrEmpty(`battlePass.chapter_choice.tanks.default_${m}`);
    return (0, ms.jsxs)("div", {
      className: sa(P_.base, P_[`base__${n}`], _ && P_.base__selected),
      children: [
        (0, ms.jsx)("div", { className: P_.bg, style: { backgroundImage: `url(${p})` } }),
        (0, ms.jsx)("div", {
          className: sa(P_.reward, a.reward),
          style: {
            backgroundImage: `url(${h})`,
            width: Qd[d][s.name].rewardWidth,
            height: Qd[d][s.name].rewardHeight,
          },
        }),
        n !== Qt.Completed &&
          !o &&
          (0, ms.jsx)(St, {
            value: l,
            maxValue: c,
            size: "small",
            className: sa(P_.progressBar, n === Qt.Active && P_.progressBar__active),
            classNames: { background: P_.progressBarBg },
          }),
        (0, ms.jsx)("div", { className: P_.info, children: (0, ms.jsx)(k_, { chapterID: e }) }),
        B_(n, u) &&
          (0, ms.jsx)("div", {
            className: P_.status,
            children: (0, ms.jsx)(e_, { type: B_(n, u) }),
          }),
      ],
    });
  }),
  E_ = {
    base: "Card_3be28e6f",
    base__extra: "Card_base__extra_5e0e439b",
    slot: "Card_slot_356826af",
    active: "Card_active_741bc02a",
    info: "Card_info_9eddf15f",
    idleVideo__regular: "Card_idleVideo__regular_f4c22d1c",
    idleVideo__extra: "Card_idleVideo__extra_4cdfaaf7",
    idleVideo__postprogression: "Card_idleVideo__postprogression_b28e5b27",
    fadeInWithScale: "Card_fadeInWithScale_f4c22d1c",
    slideUp: "Card_slideUp_f4c22d1c",
    blink: "Card_blink_f4c22d1c",
    scale: "Card_scale_f4c22d1c",
    rotate: "Card_rotate_f4c22d1c",
    windowIn: "Card_windowIn_f4c22d1c",
    fadeOut: "Card_fadeOut_f4c22d1c",
    fadeIn: "Card_fadeIn_f4c22d1c",
  },
  T_ = R.strings.battle_pass.chapterChoice,
  L_ = Wt(function ({ chapterID: e }) {
    const { model: a, controls: t } = vi(),
      { breakpoint: s } = Me(),
      r = a.computes.getChapterById(e);
    if (!r) return;
    const { chapterState: n, isPostProgression: i, isExtra: o } = r,
      l = a.selectedChapterID.get(),
      c = a.computes.selectedChapter(),
      d = a.computes.sortedChapters().indexOf(c),
      _ = Jd(o, i);
    return (0, ms.jsxs)("div", {
      className: sa(E_.base, o && E_.base__extra),
      children: [
        n === Qt.Active &&
          (0, ms.jsx)(Ld, {
            text: i ? T_.activeChapter.postprogression.text() : T_.activeChapter.text(),
            videoSrc: R.videos.battle_pass.chapter_choice.activeAnimation(),
            className: E_.active,
            classNames: { idleVideo: E_[`idleVideo__${i ? Xd : Kd}`] },
          }),
        (0, ms.jsx)(qd, {
          selected: l === e,
          active: n === Qt.Active,
          onClick: () => {
            e !== l &&
              (t.setPrevChapterIndex(d),
              t.setSelectedChapterID(e),
              t.onChapterSelect(e),
              ue.sound(R.sounds.bp_select_chapter()));
          },
          onMouseEnter: () => {
            ue.sound(R.sounds.bp_highlight_02());
          },
          className: E_.slot,
          style: { width: Qd[_][s.name].cardWidth, height: Qd[_][s.name].cardHeight },
          "data-test-id": `chapterID-${e}`,
          children: (0, ms.jsx)(A_, { chapterID: e }),
        }),
      ],
    });
  }),
  O_ = {
    base: "CardsContent_f347026f",
    mask: "CardsContent_mask_b9df56c2",
    mask__both: "CardsContent_mask__both_a3217d34",
    mask__left: "CardsContent_mask__left_96e6e67c",
    mask__right: "CardsContent_mask__right_50882304",
    cardsWrapper: "CardsContent_cardsWrapper_7a6da9dd",
    cardsWrapper__inactive: "CardsContent_cardsWrapper__inactive_92450b8d",
    scrollWrapper: "CardsContent_scrollWrapper_e65fe5a6",
    scrollBar: "CardsContent_scrollBar_9c08690c",
    fadeInWithScale: "CardsContent_fadeInWithScale_ef18ba3c",
    slideUp: "CardsContent_slideUp_ef18ba3c",
    blink: "CardsContent_blink_ef18ba3c",
    scale: "CardsContent_scale_ef18ba3c",
    rotate: "CardsContent_rotate_ef18ba3c",
    windowIn: "CardsContent_windowIn_ef18ba3c",
    fadeOut: "CardsContent_fadeOut_ef18ba3c",
    fadeIn: "CardsContent_fadeIn_ef18ba3c",
  },
  D_ = Wt(function () {
    const { model: e, controls: a } = vi(),
      [t, s] = (0, us.useState)(!1),
      { api: r } = Rt(),
      { animationScroll: n, applyScroll: i, getBounds: o } = r,
      l = e.computes.selectedChapter(),
      c = e.computes.sortedChapters(),
      d = c.indexOf(l),
      _ = ja(r, Fa.horizontal, void 0, { gapBeforeStart: 5 }),
      [u, m] = xt(r);
    ((0, us.useEffect)(() => {
      l && a.setSelectedChapterID(l.chapterID);
    }, [a, l]),
      (0, us.useEffect)(
        () =>
          na(() => {
            "idle" === _.type && n.scrollPosition.idle && i(n.scrollPosition.get());
          }),
        [n.scrollPosition, i, _.type],
      ),
      (0, us.useEffect)(() => {
        const e = c.indexOf(l),
          [a, t] = o();
        i(e >= Math.floor(c.length / 2) ? t : a);
      }, [i, o, l, c]),
      (0, us.useEffect)(() => {
        s("dragging" === _.type);
      }, [_.type]),
      (0, us.useEffect)(() => {
        const e = (e, a, t) => {
          !1 === (Za(a.get(), t) && Za(a.goal, t)) && e.stopPropagation();
        };
        return (
          r.events.on("mouseWheel", e),
          () => {
            r.events.off("mouseWheel", e);
          }
        );
      }, [r]));
    const p = (e, t) => {
      (Xa(void 0 !== c[e]),
        a.setSelectedChapterID(c[e].chapterID),
        a.onChapterSelect(c[e].chapterID),
        e !== t && a.setPrevChapterIndex(t));
    };
    return (
      At(D.ARROW_RIGHT, () => {
        p(d < c.length - 1 ? d + 1 : d, d);
      }),
      At(D.ARROW_LEFT, () => {
        p(d > 0 ? d - 1 : d, d);
      }),
      (0, ms.jsxs)("div", {
        className: O_.base,
        children: [
          (0, ms.jsx)("div", {
            className: sa(O_.mask, O_[`mask__${cl(u, m)}`]),
            children: (0, ms.jsx)(Ca, {
              classNames: { wrapper: O_.scrollWrapper },
              children: (0, ms.jsx)("div", {
                className: sa(O_.cardsWrapper, t && O_.cardsWrapper__inactive),
                children: re(c, (e, a) =>
                  (0, ms.jsx)(L_, { chapterID: e.chapterID }, `${e.chapterID}_${a}`),
                ),
              }),
            }),
          }),
          (0, ms.jsx)(Ge, { classNames: { base: O_.scrollBar } }),
        ],
      })
    );
  }),
  W_ = "ButtonsGroup_6fd5782",
  V_ = "ButtonsGroup_button_17bae557",
  M_ = Qa.resolve("strings"),
  z_ = Wt(function () {
    const e = m(),
      { model: a, controls: t } = vi(),
      s = a.computes.selectedChapter(),
      { breakpoint: r } = Me(),
      n = r.weight >= _e.large.weight ? Se.large : Se.medium;
    return (
      At(D.SPACE, () => {
        s?.isPostProgression
          ? e.push(ls.battlePass.postProgression, {})
          : e.push(ls.battlePass.progression, { chapterID: s?.chapterID });
      }),
      (0, ms.jsxs)("div", {
        className: W_,
        children: [
          s?.isPostProgression
            ? (0, ms.jsx)(yt, {
                onClick: () => e.push(ls.battlePass.postProgression, {}),
                className: V_,
                size: n,
                "data-test-id": "toPostProgression",
                children: M_.readOrEmpty(
                  "battle_pass.chapterChoice.chapterInfo.buttons.toPostProgression",
                ),
              })
            : (0, ms.jsx)(yt, {
                onClick: () => e.push(ls.battlePass.progression, { chapterID: s?.chapterID }),
                className: V_,
                size: n,
                "data-test-id": "toChapter",
                children: M_.readOrEmpty("battle_pass.chapterChoice.chapterInfo.buttons.toChapter"),
              }),
          0 !== s?.tankmenScreenID &&
            (0, ms.jsx)(yt, {
              onClick: () => {
                void 0 !== s?.chapterID && t.showTankmen(s?.chapterID);
              },
              className: V_,
              theme: w.secondary,
              size: n,
              "data-test-id": "toCrewMembers",
              children: M_.readOrEmpty(
                "battle_pass.chapterChoice.chapterInfo.buttons.toCrewMembers",
              ),
            }),
        ],
      })
    );
  }),
  $_ = "Deadline_d8216f12",
  F_ = "Deadline_timerIcon_cda81cf2",
  H_ = "Deadline_timerLabel_218217e0",
  U_ = Qa.resolve("strings"),
  G_ = s,
  q_ = Wt(function () {
    const { model: e } = vi(),
      { expireTime: a, timeLeft: t } = e.computes.selectedChapter(),
      s = e.computes.detailedTimer();
    return (0, ms.jsx)("div", {
      className: $_,
      children: s
        ? (0, ms.jsx)(aa, {
            text: U_.readOrEmpty("battle_pass.chapterChoice.chapterInfo.deadline.time"),
            binding: {
              endTime: (0, ms.jsx)(
                Nt,
                { start: t, size: Qe.x48x48, classNames: { icon: F_, label: H_ } },
                t,
              ),
            },
          })
        : (0, ms.jsx)(aa, {
            text: U_.readOrEmpty("battle_pass.chapterChoice.chapterInfo.deadline.date"),
            binding: { endDate: G_(a, ha.DayMonthFull) },
          }),
    });
  }),
  K_ = {
    base: "PreviewButton_8d85fd92",
    base__x100x100: "PreviewButton_base__x100x100_40f65925",
    base__x120x120: "PreviewButton_base__x120x120_eabae7e5",
    base__x140x140: "PreviewButton_base__x140x140_592ecabc",
    base__hovered: "PreviewButton_base__hovered_6f70d99a",
    fadeInWithScale: "PreviewButton_fadeInWithScale_22577403",
    slideUp: "PreviewButton_slideUp_22577403",
    blink: "PreviewButton_blink_22577403",
    scale: "PreviewButton_scale_22577403",
    rotate: "PreviewButton_rotate_22577403",
    windowIn: "PreviewButton_windowIn_22577403",
    fadeOut: "PreviewButton_fadeOut_22577403",
    fadeIn: "PreviewButton_fadeIn_22577403",
  },
  X_ = "x100x100",
  Z_ = "x120x120",
  J_ = "x140x140",
  Q_ = Qa.resolve("images"),
  Y_ = function ({
    iconSize: e,
    onClick: a,
    onMouseEnter: t,
    onMouseLeave: s,
    soundHover: r = "",
    soundClick: n = "",
    className: i = "",
  }) {
    const [o, l] = (0, us.useState)(!1),
      c = Q_.readOrEmpty(`battlePass.icons.previewButton.${V(e, J_)}`);
    return (0, ms.jsx)("div", {
      className: sa(K_.base, o && K_.base__hovered, K_[`base__${e}`], i),
      onClick: (e) => {
        (a?.(e), n && ue.sound(n));
      },
      onMouseEnter: () => {
        (l(!0), t?.(), r && ue.sound(r));
      },
      onMouseLeave: () => {
        (l(!1), s?.());
      },
      style: { backgroundImage: `url(${c})` },
    });
  },
  eu = {
    base: "InGarage_66bdf5dd",
    base__x24x24: "InGarage_base__x24x24_79818dbf",
    base__x32x32: "InGarage_base__x32x32_839c6a2c",
    base__x48x48: "InGarage_base__x48x48_19be1254",
    base__x80x80: "InGarage_base__x80x80_c3a1d174",
    fadeInWithScale: "InGarage_fadeInWithScale_2e055df1",
    slideUp: "InGarage_slideUp_2e055df1",
    blink: "InGarage_blink_2e055df1",
    scale: "InGarage_scale_2e055df1",
    rotate: "InGarage_rotate_2e055df1",
    windowIn: "InGarage_windowIn_2e055df1",
    fadeOut: "InGarage_fadeOut_2e055df1",
    fadeIn: "InGarage_fadeIn_2e055df1",
  },
  au = "x24x24",
  tu = "x32x32",
  su = "x48x48",
  ru = "x80x80",
  nu = Qa.resolve("images"),
  iu = function ({ iconSize: e, className: a = "" }) {
    const t = nu.readOrEmpty(`battlePass.icons.inGarage.${e}`);
    return (0, ms.jsx)("div", {
      className: sa(eu.base, eu[`base__${e}`], a),
      style: { backgroundImage: `url(${t})` },
    });
  },
  ou = {
    vehicleWrapper: "SubTitle_vehicleWrapper_c315a83c",
    styleWrapper: "SubTitle_styleWrapper_59988398",
    style: "SubTitle_style_c315a83c",
    vehicleStyle: "SubTitle_vehicleStyle_1b9867d2",
    postProgression: "SubTitle_postProgression_c315a83c",
    crew: "SubTitle_crew_f25c78a4",
    styleLevel: "SubTitle_styleLevel_c315a83c",
    styleName: "SubTitle_styleName_cab7080b",
    attachmentsSet: "SubTitle_attachmentsSet_c3439b6f",
    vehicle: "SubTitle_vehicle_947ca1b3",
    vehicleLevel: "SubTitle_vehicleLevel_c315a83c",
    vehicleName: "SubTitle_vehicleName_c315a83c",
    inGarage__style: "SubTitle_inGarage__style_b8f6084a",
    inGarage__vehicle: "SubTitle_inGarage__vehicle_1cb9fdfb",
    fadeInWithScale: "SubTitle_fadeInWithScale_c315a83c",
    slideUp: "SubTitle_slideUp_c315a83c",
    blink: "SubTitle_blink_c315a83c",
    scale: "SubTitle_scale_c315a83c",
    rotate: "SubTitle_rotate_c315a83c",
    windowIn: "SubTitle_windowIn_c315a83c",
    fadeOut: "SubTitle_fadeOut_c315a83c",
    fadeIn: "SubTitle_fadeIn_c315a83c",
  },
  lu = Qa.resolve("strings"),
  cu = "vehicle",
  du = "style",
  _u = Wt(function () {
    const { model: e } = vi(),
      a = e.computes.selectedChapter(),
      {
        breakpoint: { weight: t },
      } = Me(),
      s = (e) =>
        e === cu
          ? t < _e.large.weight
            ? ne.x64x64
            : ne.x96x96
          : e === du
            ? t < _e.large.weight
              ? ne.x24x24
              : ne.x48x48
            : void 0,
      r = (e) =>
        e === cu
          ? t >= _e.large.weight
            ? ru
            : t >= _e.medium.weight
              ? su
              : tu
          : e === du
            ? t >= _e.large.weight
              ? tu
              : au
            : tu,
      n = { level: ou.vehicleLevel, name: ou.vehicleName },
      i = { level: ou.styleLevel, name: ou.styleName };
    if (!a) return;
    const {
      styleName: o,
      vehicleInfo: l,
      finalRewardType: c,
      isVehicleInHangar: d,
      attachmentsSetName: _,
    } = a;
    return (() => {
      switch (c) {
        case ts.Vehicle:
          return (0, ms.jsxs)("div", {
            className: ou.vehicleWrapper,
            children: [
              (0, ms.jsx)(aa, {
                classMix: ou.vehicle,
                text: lu.readOrEmpty("battle_pass.chapterChoice.vehicle.reward.subTitle"),
                binding: {
                  vehicleName: (0, ms.jsx)(ns, { ...l, vehicleTypeIconSize: s(cu), classNames: n }),
                },
              }),
              d &&
                (0, ms.jsx)(iu, {
                  iconSize: r(cu),
                  className: sa(ou.inGarage, ou.inGarage__vehicle),
                }),
            ],
          });
        case ts.VehicleStyle:
          return (0, ms.jsx)(aa, {
            classMix: ou.vehicleStyle,
            text: lu.readOrEmpty("battle_pass.chapterChoice.vehicleStyle.reward.subTitle"),
            binding: { styleName: o },
          });
        case ts.Style:
          return (0, ms.jsxs)("div", {
            className: ou.styleWrapper,
            children: [
              (0, ms.jsx)(aa, {
                classMix: ou.style,
                text: lu.readOrEmpty("battle_pass.chapterChoice.stylePreview.reward.subTitle"),
                binding: {
                  vehicleName: (0, ms.jsx)(ns, { ...l, vehicleTypeIconSize: s(du), classNames: i }),
                },
              }),
              d &&
                (0, ms.jsx)(iu, {
                  iconSize: r(du),
                  className: sa(ou.inGarage, ou.inGarage__style),
                }),
            ],
          });
        case ts.Tankman:
          return (0, ms.jsx)(aa, {
            classMix: ou.crew,
            text: lu.readOrEmpty("battle_pass.chapterChoice.crewMember.reward.subTitle"),
          });
        case ts.AttachmentsSet:
          return (0, ms.jsx)("span", {
            className: ou.attachmentsSet,
            children: lu.readOrEmpty(`quests.bonusName.attachments_set.${_}`),
          });
        case ts.PostProgression:
          return (0, ms.jsx)(aa, {
            classMix: ou.postProgression,
            text: lu.readOrEmpty("battle_pass.chapterChoice.eliteCircuit.reward.subTitle"),
          });
        default:
          return "";
      }
    })();
  }),
  uu = "Title_vehicleStyleWrapper_5727057f",
  mu = "Title_postProgression_2e63cf3",
  pu = "Title_crew_ace25966",
  hu = "Title_vehicle_c974ddd5",
  bu = "Title_vehicleStyle_e7d39a46",
  fu = "Title_attachmentsSet_7b3dafcc",
  gu = "Title_style_2e63cf3",
  vu = "Title_level_2e63cf3",
  xu = "Title_name_93838a06",
  wu = "Title_inGarage_1c4370bb",
  Cu = Qa.resolve("strings"),
  yu = Wt(function () {
    const { model: e } = vi(),
      a = e.computes.selectedChapter(),
      {
        breakpoint: { weight: t },
      } = Me(),
      s = t < _e.large.weight ? ne.x64x64 : ne.x96x96,
      r = t >= _e.large.weight ? ru : t >= _e.medium.weight ? su : tu,
      n = { level: vu, name: xu };
    if (!a) return;
    const {
      styleName: i,
      vehicleInfo: o,
      finalRewardType: l,
      isVehicleInHangar: c,
      tankmanNames: d,
    } = a;
    return (function () {
      switch (l) {
        case ts.Vehicle:
          return (0, ms.jsx)(aa, {
            classMix: hu,
            text: Cu.readOrEmpty("battle_pass.chapterChoice.vehicle.reward.title"),
          });
        case ts.VehicleStyle:
          return (0, ms.jsxs)("div", {
            className: uu,
            children: [
              (0, ms.jsx)(aa, {
                classMix: bu,
                text: Cu.readOrEmpty("battle_pass.chapterChoice.vehicleStyle.reward.title"),
                binding: {
                  vehicleName: (0, ms.jsx)(ns, { ...o, vehicleTypeIconSize: s, classNames: n }),
                },
              }),
              c && (0, ms.jsx)(iu, { iconSize: r, className: wu }),
            ],
          });
        case ts.Style:
          return (0, ms.jsx)(aa, {
            classMix: gu,
            text: Cu.readOrEmpty("battle_pass.chapterChoice.stylePreview.reward.title"),
            binding: { styleName: i },
          });
        case ts.Tankman:
          return (0, ms.jsx)(aa, {
            classMix: pu,
            text: b(d, Cu.readOrEmpty("battle_pass.common.comma")),
          });
        case ts.AttachmentsSet:
          return (0, ms.jsx)("span", {
            className: fu,
            children: Cu.readOrEmpty("battle_pass.finalReward.attachmentsSet.title"),
          });
        case ts.PostProgression:
          return (0, ms.jsx)(aa, {
            classMix: mu,
            text: Cu.readOrEmpty("battle_pass.chapterChoice.eliteCircuit.reward.title"),
          });
        default:
          return "";
      }
    })();
  }),
  Su = "FinalReward_96b2b9a7",
  ju = "FinalReward_rewardInfo_e61fb0c8",
  Iu = "FinalReward_preview_68854b55",
  Nu = Wt(function () {
    const { model: e, controls: a } = vi(),
      t = at(
        { previewButton: X_ },
        { medium: { previewButton: Z_ }, large: { previewButton: J_ } },
      ),
      s = e.computes.selectedChapter();
    Xa(void 0 !== s);
    const { chapterID: r, finalRewardType: n } = s,
      i = (0, us.useCallback)(
        (e) => {
          (a.openPreview(r), e.stopPropagation());
        },
        [a, r],
      ),
      o = [ts.Style, ts.Vehicle, ts.VehicleStyle, ts.AttachmentsSet].includes(n);
    return (0, ms.jsxs)("div", {
      className: Su,
      children: [
        o &&
          (0, ms.jsx)("div", {
            className: Iu,
            children: (0, ms.jsx)(Y_, {
              iconSize: t.previewButton,
              onClick: i,
              soundHover: R.sounds.bp_highlight_02(),
              soundClick: R.sounds.play(),
            }),
          }),
        (0, ms.jsxs)("div", {
          className: ju,
          children: [(0, ms.jsx)(yu, {}), (0, ms.jsx)(_u, {})],
        }),
      ],
    });
  }),
  ku = {
    base: "ChapterInfo_583787",
    deadline: "ChapterInfo_deadline_df593065",
    info: "ChapterInfo_info_50f38f5c",
    chapterName: "ChapterInfo_chapterName_2e84101e",
    chapterName__bougth: "ChapterInfo_chapterName__bougth_4015ed41",
    finalReward__vehicleStyle: "ChapterInfo_finalReward__vehicleStyle_9092be9e",
    finalReward__vehicle: "ChapterInfo_finalReward__vehicle_8f1be3b9",
    finalReward__style: "ChapterInfo_finalReward__style_939c7d1e",
    finalReward__attachmentsSet: "ChapterInfo_finalReward__attachmentsSet_71da8196",
    finalReward__tankman: "ChapterInfo_finalReward__tankman_939c7d1e",
    finalReward__postProgression: "ChapterInfo_finalReward__postProgression_42299b8a",
    buttonsGroup__vehicleStyle: "ChapterInfo_buttonsGroup__vehicleStyle_32e73b60",
    buttonsGroup__vehicle: "ChapterInfo_buttonsGroup__vehicle_19a07e37",
    buttonsGroup__style: "ChapterInfo_buttonsGroup__style_939c7d1e",
    buttonsGroup__attachmentsSet: "ChapterInfo_buttonsGroup__attachmentsSet_99acb72a",
    buttonsGroup__tankman: "ChapterInfo_buttonsGroup__tankman_939c7d1e",
    buttonsGroup__postProgression: "ChapterInfo_buttonsGroup__postProgression_d83fdc7a",
    emblem: "ChapterInfo_emblem_b1fd21e1",
    fadeInWithScale: "ChapterInfo_fadeInWithScale_939c7d1e",
    slideUp: "ChapterInfo_slideUp_939c7d1e",
    blink: "ChapterInfo_blink_939c7d1e",
    scale: "ChapterInfo_scale_939c7d1e",
    rotate: "ChapterInfo_rotate_939c7d1e",
    windowIn: "ChapterInfo_windowIn_939c7d1e",
    fadeOut: "ChapterInfo_fadeOut_939c7d1e",
    fadeIn: "ChapterInfo_fadeIn_939c7d1e",
  },
  Pu = Qa.resolve("strings"),
  Ru = Wt(function () {
    const { model: e } = vi(),
      a = e.computes.selectedChapter(),
      t = at(
        { iconSize: sn, shieldSize: Kr, containerSize: $r },
        {
          medium: { iconSize: rn, shieldSize: Xr, containerSize: Fr },
          large: { iconSize: nn, shieldSize: Zr, containerSize: Hr },
          extraLarge: { iconSize: on, shieldSize: Jr, containerSize: Ur },
        },
      ),
      s = X(
        pi.length,
        pi.map((e) => {
          const { delay: a, diff: t, duration: s } = Object.values(e)[0];
          return hi(a, t, s);
        }),
      ),
      r = pi.reduce((e, a, t) => {
        const r = Object.keys(a)[0];
        return s[t] ? ((e[r] = s[t]), e) : e;
      }, {});
    if (!a) return;
    const { chapterID: n, isBought: o, finalRewardType: l } = a;
    return (0, ms.jsxs)("div", {
      className: ku.base,
      children: [
        (0, ms.jsx)(i.div, {
          style: r.emblem,
          children: (0, ms.jsx)(_n, {
            iconSize: t.iconSize,
            shieldSize: t.shieldSize,
            containerSize: t.containerSize,
            bpPurchased: o,
            chapterID: n,
            className: ku.emblem,
          }),
        }),
        (0, ms.jsxs)("div", {
          className: ku.info,
          children: [
            (0, ms.jsx)(i.div, {
              style: r.deadline,
              children: (0, ms.jsx)("div", {
                className: ku.deadline,
                children: (0, ms.jsx)(q_, {}),
              }),
            }),
            (0, ms.jsx)(i.div, {
              style: r.chapterName,
              children: (0, ms.jsx)(H, {
                className: sa(ku.chapterName, o && ku.chapterName__bougth),
                text: Pu.readOrEmpty(`battle_pass.chapter.fullName.c_${n}`),
              }),
            }),
            (0, ms.jsx)(i.div, {
              style: r.finalReward,
              children: (0, ms.jsx)("div", {
                className: sa(ku.finalReward, ku[`finalReward__${l}`]),
                children: (0, ms.jsx)(Nu, {}),
              }),
            }),
            (0, ms.jsx)(i.div, {
              style: r.buttonsGroup,
              children: (0, ms.jsx)("div", {
                className: sa(ku.buttonsGroup, ku[`buttonsGroup__${l}`]),
                children: (0, ms.jsx)(z_, {}),
              }),
            }),
          ],
        }),
      ],
    });
  }),
  Bu = "FreeBpPoints_13635b90",
  Au = "FreeBpPoints_pointsBlock_de8d94dc",
  Eu = "FreeBpPoints_points_cd1a8292",
  Tu = "FreeBpPoints_icon_e6968e4a",
  Lu = "FreeBpPoints_text_74f25e3",
  Ou = Qa.resolve("strings"),
  Du = Wt(function () {
    const { model: e } = vi(),
      { freePoints: a } = e.root.get(),
      t = u({
        header: Ou.readOrEmpty("battle_pass.chapterChoice.freePoints.tooltip.header"),
        body: Ou.readOrEmpty("battle_pass.chapterChoice.freePoints.tooltip.body"),
      }),
      s = at({ iconSize: "" }, { medium: { iconSize: "_medium" }, large: { iconSize: "_large" } });
    return (0, ms.jsxs)("div", {
      className: Bu,
      ...t,
      children: [
        (0, ms.jsxs)("div", {
          className: Au,
          children: [
            (0, ms.jsx)("div", { className: Eu, children: (0, ms.jsx)(Ka, { value: a }) }),
            (0, ms.jsx)(be, {
              className: Tu,
              path: `battlePass.chapter_choice.freePoints${s.iconSize}`,
            }),
          ],
        }),
        (0, ms.jsx)("div", {
          className: Lu,
          children: Ou.readOrEmpty("battle_pass.chapterChoice.freePoints.text"),
        }),
      ],
    });
  }),
  Wu = "App_772aceb",
  Vu = "App_background_f46709aa",
  Mu = "App_main_879c8615",
  zu = "App_idle_e06fed7f",
  $u = "App_shadow_d2a46054",
  Fu = "App_freeBpPoints_c3ec6dd0",
  Hu = "App_chapterInfo_ae823c83",
  Uu = "App_cards_a8851e46",
  Gu = Wt(function () {
    const { model: e, controls: a } = vi(),
      { onViewLoaded: t } = a,
      s = e.computes.selectedChapter(),
      r = e.prevChapterIndex.get(),
      n = e.computes.sortedChapters().indexOf(s),
      [o, l] = (0, us.useState)(n),
      [c, d] = (0, us.useState)(!1),
      _ = m();
    (At(D.ESCAPE, () => {
      _.goBack();
    }),
      (0, us.useEffect)(
        () =>
          na(() => {
            c || (t(), d(!0));
          }),
        [c, t],
      ));
    const [u, p] = X(e.computes.backgrounds().length, (e) => ({
        x: 0,
        opacity: e === n ? 1 : 0,
        config: { duration: 400, easing: lt.easeOutQuint },
      })),
      h = 0.1 * viewEnv.getViewSizeRem().width,
      b = (0, us.useCallback)(
        (e, a) => {
          (p.start((t) =>
            t === e
              ? {
                  from: { x: a * h, opacity: 0, zIndex: 3 },
                  to: { x: 0, opacity: 1, zIndex: 3 },
                  reset: !0,
                }
              : {},
          ),
            l(e));
        },
        [p, h],
      );
    (0, us.useEffect)(() => {
      b(n, r < n ? 1 : -1);
    }, [r, n, b]);
    const [f] = Ra(() => hi(200, 60)),
      [g] = Ra(() => hi(300, 60)),
      [v] = Ra(() =>
        ((e = 0) => ({
          from: { opacity: 0, transform: "scale(1.1)" },
          to: { opacity: 1, transform: "scale(1)" },
          config: { duration: 500, easing: lt.easeInOutCubic },
          delay: e,
        }))(),
      );
    return (0, ms.jsx)(ms.Fragment, {
      children:
        c &&
        (0, ms.jsxs)("div", {
          className: Wu,
          children: [
            (0, ms.jsx)(i.div, {
              className: Vu,
              style: v,
              children: (0, ms.jsxs)(ms.Fragment, {
                children: [
                  u.map((e, a) =>
                    (0, ms.jsx)(
                      ji,
                      { style: e, i: a, index: o, classNames: { idle: zu, main: Mu } },
                      a,
                    ),
                  ),
                  (0, ms.jsx)("div", { className: $u }),
                ],
              }),
            }),
            e.root.get().freePoints > 0 &&
              (0, ms.jsx)(i.div, { className: Fu, style: g, children: (0, ms.jsx)(Du, {}) }),
            (0, ms.jsx)("div", { className: Hu, children: (0, ms.jsx)(Ru, {}) }, s?.chapterID),
            (0, ms.jsx)(i.div, {
              className: Uu,
              style: f,
              children: (0, ms.jsx)(et, { children: (0, ms.jsx)(D_, {}) }),
            }),
          ],
        }),
    });
  }),
  qu = () =>
    (0, ms.jsx)(gi, {
      options: { rootId: R.aliases.battle_pass.ChapterChoice("resId") },
      children: (0, ms.jsx)(Gu, {}),
    }),
  Ku = (e, a, t, s, r) => {
    const n = R.images.gui.maps.icons.battlePass.awards_widget;
    return r
      ? `url(${n.$dyn(`${e.toLowerCase()}_${a}${t}_${s}_${r}`)})`
      : `url(${n.$dyn(`${e.toLowerCase()}_${a}${t}_${s}`)})`;
  },
  Xu = (function (e) {
    return (
      (e.Award = "Award"),
      (e.Ticket = "Ticket"),
      (e.Coin = "Coin"),
      (e.Taler = "Taler"),
      (e.Collection = "Collection"),
      (e.Commander = "Commander"),
      e
    );
  })({}),
  Zu = (function (e) {
    return ((e.Small = "small"), (e.Big = "big"), e);
  })({}),
  Ju = (function (e) {
    return ((e.None = ""), (e.Small = "s"), (e.Medium = "m"), e);
  })({}),
  Qu = (function (e) {
    return ((e.Border = "border"), (e.Background = "bg"), (e.Icon = "icon"), (e.None = ""), e);
  })({}),
  Yu = (function (e) {
    return (
      (e.Hover = "Hover"),
      (e.Disabled = "Disabled"),
      (e.Triggered = "Triggered"),
      (e.None = ""),
      e
    );
  })({}),
  em = {
    base: "Background_8e48022f",
    bg: "Background_bg_fcef4881",
    bgDisabled: "Background_bgDisabled_26effab7",
    bgHover: "Background_bgHover_32967f75",
    base__big: "Background_base__big_26effab7",
    base__hovered: "Background_base__hovered_26effab7",
    fadeInWithScale: "Background_fadeInWithScale_26effab7",
    slideUp: "Background_slideUp_26effab7",
    blink: "Background_blink_26effab7",
    scale: "Background_scale_26effab7",
    rotate: "Background_rotate_26effab7",
    windowIn: "Background_windowIn_26effab7",
    fadeOut: "Background_fadeOut_26effab7",
    fadeIn: "Background_fadeIn_26effab7",
  },
  am = ({ size: e, isHover: a, disabled: t = !1, type: s = Xu.Coin }) => {
    const { breakpoint: r } = Me(),
      n = r.weight >= _e.medium.weight ? Ju.Medium : Ju.Small;
    return (0, ms.jsx)("div", {
      className: sa(em.base, em[`base__${e}`], em[`base__${e}${s}`], a && em.base__hovered),
      children: t
        ? (0, ms.jsx)("div", {
            className: em.bgDisabled,
            style: { backgroundImage: Ku(s, Qu.Background, Yu.Disabled, e, n) },
          })
        : (0, ms.jsxs)(ms.Fragment, {
            children: [
              (0, ms.jsx)("div", {
                className: em.bg,
                style: { backgroundImage: Ku(s, Qu.Background, Yu.None, e, n) },
              }),
              (0, ms.jsx)("div", {
                className: em.bgHover,
                style: { backgroundImage: Ku(s, Qu.Background, Yu.Hover, e, n) },
              }),
            ],
          }),
    });
  },
  tm = {
    base: "Border_3359fba1",
    border: "Border_b559a98b",
    borderHover: "Border_borderHover_6143f6b7",
    base__hovered: "Border_base__hovered_b559a98b",
    borderDisabled: "Border_borderDisabled_6282d18a",
    borderDisabled__big: "Border_borderDisabled__big_80fa355b",
    fadeInWithScale: "Border_fadeInWithScale_b559a98b",
    slideUp: "Border_slideUp_b559a98b",
    blink: "Border_blink_b559a98b",
    scale: "Border_scale_b559a98b",
    rotate: "Border_rotate_b559a98b",
    windowIn: "Border_windowIn_b559a98b",
    fadeOut: "Border_fadeOut_b559a98b",
    fadeIn: "Border_fadeIn_b559a98b",
  },
  sm = ({ size: e, isHover: a, highlighted: t = !1, disabled: s = !1, type: r = Xu.Coin }) => {
    const { breakpoint: n } = Me(),
      i = n.weight >= _e.medium.weight ? Ju.Medium : Ju.Small;
    return (0, ms.jsx)("div", {
      className: sa(tm.base, tm[`base__${e}`], a && tm.base__hovered),
      children: s
        ? (0, ms.jsx)("div", {
            className: sa(tm.borderDisabled, tm[`borderDisabled__${e}`]),
            style: { backgroundImage: Ku(r, Qu.Border, Yu.Disabled, e, i) },
          })
        : (0, ms.jsxs)(ms.Fragment, {
            children: [
              (0, ms.jsx)("div", {
                className: tm.border,
                style: { backgroundImage: Ku(t ? Xu.Collection : r, Qu.Border, Yu.None, e, i) },
              }),
              (0, ms.jsx)("div", {
                className: tm.borderHover,
                style: { backgroundImage: Ku(r, Qu.Border, Yu.Hover, e, i) },
              }),
            ],
          }),
    });
  },
  rm = {
    base: "CountValue_897d3748",
    base__big: "CountValue_base__big_94594a84",
    fadeInWithScale: "CountValue_fadeInWithScale_108ab14",
    slideUp: "CountValue_slideUp_108ab14",
    blink: "CountValue_blink_108ab14",
    scale: "CountValue_scale_108ab14",
    rotate: "CountValue_rotate_108ab14",
    windowIn: "CountValue_windowIn_108ab14",
    fadeOut: "CountValue_fadeOut_108ab14",
    fadeIn: "CountValue_fadeIn_108ab14",
  },
  nm = ({ state: e, count: a, size: t, maxCount: s = 0 }) => {
    switch (e) {
      case om.InProgress:
        return (0, ms.jsx)(aa, { text: `${a || 0} / ${s}` });
      case om.Completed:
        return (0, ms.jsx)("div", { className: sa(rm.base, rm[`base__${t}`]) });
      default:
        return (0, ms.jsx)(Ka, { format: "integral", value: a });
    }
  },
  im = {
    base: "Count_1153e9f8",
    base__big: "Count_base__big_4b990a50",
    base__locked: "Count_base__locked_c07f63fe",
    base__disabled: "Count_base__disabled_67818843",
    fadeInWithScale: "Count_fadeInWithScale_d63373f8",
    slideUp: "Count_slideUp_d63373f8",
    blink: "Count_blink_d63373f8",
    scale: "Count_scale_d63373f8",
    rotate: "Count_rotate_d63373f8",
    windowIn: "Count_windowIn_d63373f8",
    fadeOut: "Count_fadeOut_d63373f8",
    fadeIn: "Count_fadeIn_d63373f8",
  },
  om = (function (e) {
    return ((e.Default = ""), (e.InProgress = "InProgress"), (e.Completed = "Completed"), e);
  })({}),
  lm = ({ size: e, count: a, maxCount: t, state: s = "", isLocked: r = !1, disabled: n = !1 }) =>
    (0, ms.jsx)("div", {
      className: sa(im.base, im[`base__${e}`], r && im.base__locked, n && im.base__disabled),
      children: (0, ms.jsx)(nm, { state: s, size: e, count: a, maxCount: t }),
    }),
  cm = {
    base: "Icon_891882bd",
    base__big: "Icon_base__big_e04b5410",
    base__darkened: "Icon_base__darkened_211e4f9f",
    base__hover: "Icon_base__hover_ab1977b2",
    base__disabled: "Icon_base__disabled_92482313",
    fadeInWithScale: "Icon_fadeInWithScale_55a8ab20",
    slideUp: "Icon_slideUp_55a8ab20",
    blink: "Icon_blink_55a8ab20",
    scale: "Icon_scale_55a8ab20",
    rotate: "Icon_rotate_55a8ab20",
    windowIn: "Icon_windowIn_55a8ab20",
    fadeOut: "Icon_fadeOut_55a8ab20",
    fadeIn: "Icon_fadeIn_55a8ab20",
  },
  dm = (e, a, t) => {
    switch (!0) {
      case t:
        return "disabled";
      case e:
        return "hover";
      case a:
        return "darkened";
      default:
        return "";
    }
  },
  _m = ({ size: e, isHover: a, isDark: t = !0, disabled: s = !1, type: r }) => {
    const { breakpoint: n } = Me(),
      i = n.weight >= _e.medium.weight ? Ju.Medium : Ju.Small;
    return (0, ms.jsx)("div", {
      className: sa(cm.base, cm[`base__${e}`], cm[`base__${dm(a, t, s)}`]),
      style: { backgroundImage: Ku(r, Qu.Icon, Yu.None, e, r === Xu.Collection ? Ju.None : i) },
    });
  },
  um = {
    base: "Label_e1274655",
    base__big: "Label_base__big_a8cc16a4",
    base__gold: "Label_base__gold_6ef0fe9",
    base__hover: "Label_base__hover_b5605ac8",
    base__disabled: "Label_base__disabled_4a0c758c",
    fadeInWithScale: "Label_fadeInWithScale_e3f8b3ce",
    slideUp: "Label_slideUp_e3f8b3ce",
    blink: "Label_blink_e3f8b3ce",
    scale: "Label_scale_e3f8b3ce",
    rotate: "Label_rotate_e3f8b3ce",
    windowIn: "Label_windowIn_e3f8b3ce",
    fadeOut: "Label_fadeOut_e3f8b3ce",
    fadeIn: "Label_fadeIn_e3f8b3ce",
  },
  mm = (e, a) => {
    switch (!0) {
      case e:
        return "disabled";
      case a:
        return "hover";
      default:
        return "";
    }
  },
  pm = ({ size: e, title: a, isHover: t, disabled: s = !1, isGold: r = !1 }) =>
    (0, ms.jsx)("div", {
      className: sa(um.base, um[`base__${e}`], um[`base__${mm(s, t)}`], r && um.base__gold),
      children: a,
    }),
  hm = {
    base: "ChoiceAward_edd74108",
    base__big: "ChoiceAward_base__big_ca77c409",
    base__disabled: "ChoiceAward_base__disabled_991de9d",
    base__hasAppearAnimation: "ChoiceAward_base__hasAppearAnimation_aeaea71d",
    baseAppear: "ChoiceAward_baseAppear_3f034cd8",
    shine: "ChoiceAward_shine_2a2a93bd",
    shine_small_s: "ChoiceAward_shine_small_s_3f034cd8",
    shine_small_m: "ChoiceAward_shine_small_m_3f034cd8",
    shine_big_s: "ChoiceAward_shine_big_s_3f034cd8",
    shine_big_m: "ChoiceAward_shine_big_m_3f034cd8",
    shine__left: "ChoiceAward_shine__left_9adf4b0f",
    shine__right: "ChoiceAward_shine__right_872a6406",
    arrow: "ChoiceAward_arrow_e556b329",
    blinkShape: "ChoiceAward_blinkShape_4cbfbe8c",
    blink: "ChoiceAward_blink_d3e21e1f",
    blinker: "ChoiceAward_blinker_3f034cd8",
    fadeInWithScale: "ChoiceAward_fadeInWithScale_3f034cd8",
    slideUp: "ChoiceAward_slideUp_3f034cd8",
    scale: "ChoiceAward_scale_3f034cd8",
    rotate: "ChoiceAward_rotate_3f034cd8",
    windowIn: "ChoiceAward_windowIn_3f034cd8",
    fadeOut: "ChoiceAward_fadeOut_3f034cd8",
    fadeIn: "ChoiceAward_fadeIn_3f034cd8",
  },
  bm = R.strings.battle_pass.awardsWidget,
  fm = ({ count: e, disabled: a = !1, onClick: t, size: s }) => {
    const [r, n] = (0, us.useState)(!1),
      i = 1 === e ? bm.title.awardSingle() : bm.title.awardMultiple(),
      o = a ? bm.description.awardDisabled() : bm.description.award(),
      l = (0, us.useCallback)(() => {
        a || (ue.click(), t());
      }, [a, t]);
    return (0, ms.jsx)(U, {
      body: o,
      isEnabled: Boolean(o),
      children: (0, ms.jsxs)("div", {
        className: sa(
          hm.base,
          hm[`base__${s}`],
          a ? hm.base__disabled : hm.base__hasAppearAnimation,
        ),
        onMouseEnter: () => {
          (ue.sound(R.sounds.bp_highlight_02()), n(!0));
        },
        onMouseLeave: () => {
          n(!1);
        },
        onClick: l,
        children: [
          (0, ms.jsx)(sm, { size: s, isHover: r, type: Xu.Award, disabled: a }),
          (0, ms.jsx)(am, { size: s, isHover: r, type: Xu.Award, disabled: a }),
          (0, ms.jsx)(_m, { size: s, isHover: r, type: Xu.Award, disabled: a, isDark: !1 }),
          (0, ms.jsx)(lm, { size: s, count: e, disabled: a }),
          (0, ms.jsx)(pm, { size: s, isHover: r, title: i, disabled: a, isGold: !0 }),
          !a &&
            (0, ms.jsxs)(ms.Fragment, {
              children: [
                (0, ms.jsx)("div", { className: sa(hm.shine, hm.shine__left) }),
                (0, ms.jsx)("div", { className: sa(hm.shine, hm.shine__right) }),
                (0, ms.jsx)("div", { className: hm.arrow }),
                (0, ms.jsx)("div", {
                  className: hm.blinkShape,
                  children: (0, ms.jsx)("div", { className: hm.blink }),
                }),
              ],
            }),
        ],
      }),
    });
  },
  gm = {
    base: "CoinAward_f5a8f424",
    base__big: "CoinAward_base__big_df55371",
    fadeInWithScale: "CoinAward_fadeInWithScale_a9001336",
    slideUp: "CoinAward_slideUp_a9001336",
    blink: "CoinAward_blink_a9001336",
    scale: "CoinAward_scale_a9001336",
    rotate: "CoinAward_rotate_a9001336",
    windowIn: "CoinAward_windowIn_a9001336",
    fadeOut: "CoinAward_fadeOut_a9001336",
    fadeIn: "CoinAward_fadeIn_a9001336",
  },
  vm = R.strings.battle_pass.awardsWidget,
  xm = ({ count: e, onClick: a, size: t }) => {
    const [s, r] = (0, us.useState)(!1);
    return (0, ms.jsx)(U, {
      body: vm.description.coin(),
      isEnabled: Boolean(vm.description.coin()),
      children: (0, ms.jsxs)("div", {
        className: sa(gm.base, gm[`base__${t}`]),
        onMouseEnter: () => {
          (ue.sound(R.sounds.bp_highlight_02()), r(!0));
        },
        onMouseLeave: () => {
          r(!1);
        },
        onClick: () => {
          (ue.click(), a());
        },
        children: [
          (0, ms.jsx)(sm, { size: t, isHover: s }),
          (0, ms.jsx)(am, { size: t, isHover: s }),
          (0, ms.jsx)(_m, { size: t, isHover: s, type: Xu.Coin }),
          (0, ms.jsx)(lm, { size: t, count: e }),
          (0, ms.jsx)(pm, { size: t, isHover: s, title: vm.title.coin() }),
        ],
      }),
    });
  },
  wm = {
    base: "CollectionAward_7e81ced4",
    base__big: "CollectionAward_base__big_e54e4774",
    bubble: "CollectionAward_bubble_6b106ffd",
    fadeInWithScale: "CollectionAward_fadeInWithScale_4cd724f9",
    slideUp: "CollectionAward_slideUp_4cd724f9",
    blink: "CollectionAward_blink_4cd724f9",
    scale: "CollectionAward_scale_4cd724f9",
    rotate: "CollectionAward_rotate_4cd724f9",
    windowIn: "CollectionAward_windowIn_4cd724f9",
    fadeOut: "CollectionAward_fadeOut_4cd724f9",
    fadeIn: "CollectionAward_fadeIn_4cd724f9",
  },
  Cm = R.strings.battle_pass.awardsWidget,
  ym = ({ count: e, maxCount: a, newItemsCount: t, hasTrigger: s, size: r, onClick: n }) => {
    const [i, o] = (0, us.useState)(!1),
      l = a === e,
      c = r === Zu.Small && s,
      d = l ? Cm.description.collectionCompleted() : Cm.description.collection(),
      _ = Ee(() => {
        (ue.click(), n());
      });
    return (0, ms.jsx)(U, {
      body: d,
      isEnabled: Boolean(d),
      children: (0, ms.jsxs)("div", {
        className: sa(wm.base, wm[`base__${r}`]),
        onMouseEnter: () => {
          (ue.sound(R.sounds.bp_highlight_02()), o(!0));
        },
        onMouseLeave: () => {
          o(!1);
        },
        onClick: _,
        children: [
          (0, ms.jsx)(sm, { size: r, isHover: i, type: Xu.Coin, highlighted: c }),
          (0, ms.jsx)(am, { size: r, isHover: i }),
          (0, ms.jsx)(_m, { size: r, isHover: i, type: Xu.Collection }),
          (0, ms.jsx)(lm, {
            size: r,
            count: e,
            maxCount: a,
            state: l ? om.Completed : om.InProgress,
          }),
          (0, ms.jsx)(pm, { size: r, isHover: i, title: Cm.title.collection() }),
          t > 0 &&
            (0, ms.jsx)("div", {
              className: wm.bubble,
              children: (0, ms.jsx)(ft, { size: "small" }),
            }),
        ],
      }),
    });
  },
  Sm = {
    base: "CommanderAward_d7dc7d83",
    icon: "CommanderAward_icon_f54191ae",
    base__hover: "CommanderAward_base__hover_9c46950e",
    fadeInWithScale: "CommanderAward_fadeInWithScale_9c46950e",
    slideUp: "CommanderAward_slideUp_9c46950e",
    blink: "CommanderAward_blink_9c46950e",
    scale: "CommanderAward_scale_9c46950e",
    rotate: "CommanderAward_rotate_9c46950e",
    windowIn: "CommanderAward_windowIn_9c46950e",
    fadeOut: "CommanderAward_fadeOut_9c46950e",
    fadeIn: "CommanderAward_fadeIn_9c46950e",
  },
  jm = R.strings.battle_pass.awardsWidget,
  Im = ({ onClick: e, size: a, tankmenScreenID: t }) => {
    const [s, r] = (0, us.useState)(!1),
      n = jm.description.commander(),
      i =
        R.images.gui.maps.icons.battlePass.awards_widget.$dyn(`commander_icon_small_${t}`) ||
        R.images.gui.maps.icons.battlePass.awards_widget.commander_icon_small();
    return (0, ms.jsx)(U, {
      body: n,
      isEnabled: Boolean(n),
      children: (0, ms.jsxs)("div", {
        className: sa(Sm.base, Sm[`base__${a}`], s && Sm.base__hover),
        onMouseEnter: () => {
          (ue.sound(R.sounds.bp_highlight_02()), r(!0));
        },
        onMouseLeave: () => r(!1),
        onClick: () => {
          (ue.click(), e());
        },
        children: [
          (0, ms.jsx)(sm, { size: a, isHover: s }),
          (0, ms.jsx)(am, { size: a, isHover: s }),
          (0, ms.jsx)(pm, { size: a, isHover: s, title: jm.title.commander() }),
          (0, ms.jsx)("div", { className: Sm.icon, style: { backgroundImage: `url(${i})` } }),
        ],
      }),
    });
  },
  Nm = {
    base: "TalerAward_c1966527",
    base__big: "TalerAward_base__big_75f7f954",
    fadeInWithScale: "TalerAward_fadeInWithScale_7a3c6bdb",
    slideUp: "TalerAward_slideUp_7a3c6bdb",
    blink: "TalerAward_blink_7a3c6bdb",
    scale: "TalerAward_scale_7a3c6bdb",
    rotate: "TalerAward_rotate_7a3c6bdb",
    windowIn: "TalerAward_windowIn_7a3c6bdb",
    fadeOut: "TalerAward_fadeOut_7a3c6bdb",
    fadeIn: "TalerAward_fadeIn_7a3c6bdb",
  },
  km = R.strings.battle_pass.awardsWidget,
  Pm = ({ count: e, onClick: a, size: t }) => {
    const [s, r] = (0, us.useState)(!1);
    return (0, ms.jsx)(U, {
      body: km.description.taler(),
      children: (0, ms.jsxs)("div", {
        className: sa(Nm.base, Nm[`base__${t}`], s && Nm.base__hover),
        onMouseEnter: () => {
          (ue.sound(R.sounds.bp_highlight_02()), r(!0));
        },
        onMouseLeave: () => {
          r(!1);
        },
        onClick: () => {
          (ue.click(), a());
        },
        children: [
          (0, ms.jsx)(sm, { size: t, isHover: s }),
          (0, ms.jsx)(am, { size: t, isHover: s }),
          (0, ms.jsx)(_m, { size: t, isHover: s, type: Xu.Taler }),
          (0, ms.jsx)(lm, { size: t, count: e }),
          (0, ms.jsx)(pm, { size: t, isHover: s, title: km.title.taler() }),
        ],
      }),
    });
  },
  Rm = {
    base: "TicketAward_af869a5b",
    base__big: "TicketAward_base__big_6ea086b3",
    base__hasAppearAnimation: "TicketAward_base__hasAppearAnimation_94749694",
    baseAppear: "TicketAward_baseAppear_5b80ab82",
    shine: "TicketAward_shine_7589460e",
    shine_small_s: "TicketAward_shine_small_s_5b80ab82",
    shine_small_m: "TicketAward_shine_small_m_5b80ab82",
    shine_big_s: "TicketAward_shine_big_s_5b80ab82",
    shine_big_m: "TicketAward_shine_big_m_5b80ab82",
    shine__left: "TicketAward_shine__left_176547fa",
    shine__right: "TicketAward_shine__right_d221ffc5",
    arrow: "TicketAward_arrow_ae4102b5",
    blinkShape: "TicketAward_blinkShape_b3a9e256",
    blink: "TicketAward_blink_fde51f1e",
    blinker: "TicketAward_blinker_5b80ab82",
    fadeInWithScale: "TicketAward_fadeInWithScale_5b80ab82",
    slideUp: "TicketAward_slideUp_5b80ab82",
    scale: "TicketAward_scale_5b80ab82",
    rotate: "TicketAward_rotate_5b80ab82",
    windowIn: "TicketAward_windowIn_5b80ab82",
    fadeOut: "TicketAward_fadeOut_5b80ab82",
    fadeIn: "TicketAward_fadeIn_5b80ab82",
  },
  Bm = R.strings.battle_pass.awardsWidget,
  Am = ({ count: e, onClick: a, size: t }) => {
    const [s, r] = (0, us.useState)(!1),
      n = Boolean(e),
      i = n ? Xu.Ticket : void 0;
    return (0, ms.jsx)(U, {
      body: Bm.description.ticket(),
      isEnabled: Boolean(Bm.description.ticket()),
      children: (0, ms.jsxs)("div", {
        className: sa(Rm.base, Rm[`base__${t}`], n && Rm.base__hasAppearAnimation),
        onMouseEnter: () => {
          (ue.sound(R.sounds.bp_highlight_02()), r(!0));
        },
        onMouseLeave: () => {
          r(!1);
        },
        onClick: () => {
          (ue.click(), a());
        },
        children: [
          (0, ms.jsx)(sm, { size: t, isHover: s, type: i }),
          (0, ms.jsx)(am, { size: t, isHover: s, type: i }),
          (0, ms.jsx)(_m, { size: t, isHover: s, type: Xu.Ticket, isDark: !n }),
          (0, ms.jsx)(lm, { size: t, count: e }),
          (0, ms.jsx)(pm, { size: t, isHover: s, title: Bm.title.ticket(), isGold: n }),
          n &&
            (0, ms.jsxs)(ms.Fragment, {
              children: [
                (0, ms.jsx)("div", { className: sa(Rm.shine, Rm.shine__left) }),
                (0, ms.jsx)("div", { className: sa(Rm.shine, Rm.shine__right) }),
                (0, ms.jsx)("div", { className: Rm.arrow }),
                (0, ms.jsx)("div", {
                  className: Rm.blinkShape,
                  children: (0, ms.jsx)("div", { className: Rm.blink }),
                }),
              ],
            }),
        ],
      }),
    });
  },
  [Em, Tm] = He()(
    ({ observableModel: e, externalModel: a }) => {
      const t = { root: e.object(), collectionEntryPoint: e.object("collectionEntryPoint") },
        s = xa((e) => {
          const {
              talerCount: s,
              notChosenRewardCount: r,
              bpcoinCount: n,
              ticketsCount: i,
              isChooseRewardsEnabled: o,
              tankmenScreenID: l,
              isTalerEnabled: c,
              isBpCoinEnabled: d,
              isTicketsEnabled: _,
            } = t.root.get(),
            {
              collectionItemCount: u,
              newCollectionItemCount: m,
              maxCollectionItemCount: p,
              isFirstEnter: h,
              isCollectionsEnabled: b,
            } = t.collectionEntryPoint.get();
          return [
            {
              type: Xu.Award,
              props: {
                size: e,
                count: r,
                disabled: !o,
                onClick: a.createCallbackNoArgs("onTakeRewardsClick"),
              },
              condition: r > 0,
            },
            {
              type: Xu.Ticket,
              props: { size: e, count: i, onClick: a.createCallbackNoArgs("showTickets") },
              condition: _,
            },
            {
              type: Xu.Coin,
              props: { size: e, count: n, onClick: a.createCallbackNoArgs("onBpcoinClick") },
              condition: d,
            },
            {
              type: Xu.Taler,
              props: { size: e, count: s, onClick: a.createCallbackNoArgs("showTalers") },
              condition: c,
            },
            {
              type: Xu.Collection,
              props: {
                size: e,
                count: u,
                maxCount: p,
                newItemsCount: m,
                hasTrigger: h,
                onClick: a.createCallbackNoArgs("collectionEntryPoint.openCollection"),
              },
              condition: b,
            },
            {
              type: Xu.Commander,
              props: {
                size: e,
                count: 0,
                tankmenScreenID: l,
                onClick: a.createCallbackNoArgs("showTankmen"),
              },
              condition: 0 !== l,
            },
          ];
        });
      return { ...t, computes: { awardsList: s } };
    },
    ({ externalModel: e }) => ({
      takeRewards: e.createCallbackNoArgs("onTakeRewardsClick"),
      openGoodsForBpCoins: e.createCallbackNoArgs("onBpcoinClick"),
      openGoodsForBpTalers: e.createCallbackNoArgs("showTalers"),
      openCollection: e.createCallbackNoArgs("collectionEntryPoint.openCollection"),
    }),
  ),
  Lm = {
    base: "AwardsWrapper_f2595641",
    award: "AwardsWrapper_award_cc628048",
    base__big: "AwardsWrapper_base__big_b50d5668",
    fadeInWithScale: "AwardsWrapper_fadeInWithScale_b50d5668",
    slideUp: "AwardsWrapper_slideUp_b50d5668",
    blink: "AwardsWrapper_blink_b50d5668",
    scale: "AwardsWrapper_scale_b50d5668",
    rotate: "AwardsWrapper_rotate_b50d5668",
    windowIn: "AwardsWrapper_windowIn_b50d5668",
    fadeOut: "AwardsWrapper_fadeOut_b50d5668",
    fadeIn: "AwardsWrapper_fadeIn_b50d5668",
  },
  Om = (e, a) => {
    switch (e) {
      case Xu.Award:
        return (0, ms.jsx)(fm, { ...a });
      case Xu.Ticket:
        return (0, ms.jsx)(Am, { ...a });
      case Xu.Coin:
        return (0, ms.jsx)(xm, { ...a });
      case Xu.Taler:
        return (0, ms.jsx)(Pm, { ...a });
      case Xu.Collection:
        return (0, ms.jsx)(ym, { ...a });
      case Xu.Commander:
        return (0, ms.jsx)(Im, { ...a });
      default:
        return (console.warn("Unknown award type: ", e), null);
    }
  },
  Dm = Wt(({ size: e, classNames: a }) => {
    const { model: t } = Tm();
    return (0, ms.jsx)("div", {
      className: sa(Lm.base, Lm[`base__${e}`], a?.base),
      children: re(
        t.computes.awardsList(e),
        (e) =>
          e.condition &&
          (0, ms.jsx)(
            "div",
            { className: sa(Lm.award, a?.award), children: Om(e.type, e.props) },
            e.type,
          ),
      ),
    });
  }),
  Wm = ({ rootId: e, size: a = Zu.Small, context: t = "model", classNames: s }) =>
    (0, ms.jsx)(Em, {
      options: { context: t, rootId: e },
      children: (0, ms.jsx)(Dm, { size: a, classNames: s }),
    }),
  [Vm, Mm] = He()(
    ({ observableModel: e }) => {
      const a = { root: e.object(), nowRewards: e.array("rewards.nowRewards.items") },
        t = xa(() => a.nowRewards.get(), { equals: _ });
      return { ...a, computes: { rewardList: t } };
    },
    ({ externalModel: e }) => ({
      close: e.createCallbackNoArgs("onClose"),
      takeRewards: e.createCallbackNoArgs("onTakeRewardsClick"),
      showPreviewVehicle: e.createCallbackNoArgs("onPreviewVehicle"),
      showTankmen: e.createCallbackNoArgs("showTankmen"),
      showHangar: e.createCallbackNoArgs("showHangar"),
    }),
  ),
  zm = "selectableRewardsState",
  $m = "finalState",
  Fm = "FinalStateLabel_icon_2cf5ceb5",
  Hm = "FinalStateLabel_greenLight_7967eb2f",
  Um = "FinalStateLabel_text_f6f99450",
  Gm = () =>
    (0, ms.jsxs)(ms.Fragment, {
      children: [
        (0, ms.jsx)("div", { className: Fm }),
        (0, ms.jsx)("div", { className: Hm }),
        (0, ms.jsx)("div", {
          className: Um,
          children: R.strings.battle_pass.holidayFinalScreen.finalState.label(),
        }),
      ],
    }),
  qm = {
    base: "Final_fe33f216",
    controls: "Final_controls_ff63bbde",
    label: "Final_label_d1e455c6",
    base__finalState: "Final_base__finalState_a3c6efa6",
    text: "Final_text_78e61012",
    icon: "Final_icon_2e669607",
    greenLight: "Final_greenLight_e3a16077",
    finalStateText: "Final_finalStateText_d9b1929a",
    buttonWrapper: "Final_buttonWrapper_a582995e",
    button: "Final_button_dee53b83",
    fadeInWithScale: "Final_fadeInWithScale_a3c6efa6",
    slideUp: "Final_slideUp_a3c6efa6",
    blink: "Final_blink_a3c6efa6",
    scale: "Final_scale_a3c6efa6",
    rotate: "Final_rotate_a3c6efa6",
    windowIn: "Final_windowIn_a3c6efa6",
    fadeOut: "Final_fadeOut_a3c6efa6",
    fadeIn: "Final_fadeIn_a3c6efa6",
  },
  Km = R.strings.battle_pass.holidayFinalScreen,
  Xm = Wt(() => {
    const { model: e, controls: a } = Mm(),
      { takeRewards: t, showHangar: s } = a,
      { state: r, finalRewardType: n } = e.root.get(),
      i = r === zm;
    return (0, ms.jsx)("div", {
      className: sa(qm.base, qm[`base__${r}`]),
      children: (0, ms.jsxs)("div", {
        className: qm.controls,
        children: [
          (0, ms.jsx)("div", {
            className: qm.label,
            children: i
              ? (0, ms.jsx)("div", {
                  className: qm.text,
                  children: Km.selectableRewardsState.label(),
                })
              : (0, ms.jsx)(Gm, {}),
          }),
          (0, ms.jsx)("div", {
            className: qm.buttonWrapper,
            children: (0, ms.jsx)(ya, {
              size: va.medium,
              mixClass: qm.button,
              onClick: () => {
                i ? t() : s();
              },
              children: (() => {
                switch (r) {
                  case zm:
                    return Km.selectableRewardsState.button();
                  case $m:
                    return n === ts.Vehicle
                      ? Km.finalState.button.showVehicle()
                      : Km.finalState.button.showHangar();
                  default:
                    return "";
                }
              })(),
            }),
          }),
        ],
      }),
    });
  }),
  Zm = "Divider_3683d6e2",
  Jm = "Divider_divider__right_24d5147b",
  Qm = ({ isRight: e = !1 }) => (0, ms.jsx)("div", { className: sa(Zm, e && Jm) }),
  Ym = "Title_ec301c01",
  ep = "Title_text_65e6762b",
  ap = ({ text: e }) =>
    (0, ms.jsxs)("div", {
      className: Ym,
      children: [
        (0, ms.jsx)(Qm, {}),
        (0, ms.jsx)("div", { className: ep, children: e }),
        (0, ms.jsx)(Qm, { isRight: !0 }),
      ],
    }),
  tp = {
    base: "Purchase_78d7de59",
    content: "Purchase_content_1a1b801",
    preview: "Purchase_preview_a16bc569",
    shadow: "Purchase_shadow_87ba71b",
    visibleRewards: "Purchase_visibleRewards_8b26a786",
    title: "Purchase_title_8d5affdf",
    description: "Purchase_description_34691989",
    button: "Purchase_button_9d44c3bd",
    button__active: "Purchase_button__active_83b91b24",
    button__disappearing: "Purchase_button__disappearing_4a8ba62c",
    rewardButton: "Purchase_rewardButton_bc4b54c4",
    fadeInWithScale: "Purchase_fadeInWithScale_6cb4414a",
    slideUp: "Purchase_slideUp_6cb4414a",
    blink: "Purchase_blink_6cb4414a",
    scale: "Purchase_scale_6cb4414a",
    rotate: "Purchase_rotate_6cb4414a",
    windowIn: "Purchase_windowIn_6cb4414a",
    fadeOut: "Purchase_fadeOut_6cb4414a",
    fadeIn: "Purchase_fadeIn_6cb4414a",
  },
  sp = R.strings.battle_pass.holidayFinalScreen.buyState,
  rp = (e) => ({
    from: { opacity: 0 },
    to: { opacity: 1 },
    delay: 400 + 100 * e,
    config: { duration: 400 },
    onStart: () => {
      ue.sound(R.sounds.bp_reward());
    },
  }),
  np = Wt(() => {
    const { model: e, controls: a } = Mm(),
      { chapterID: t, finalRewardType: s } = e.root.get(),
      { showPreviewVehicle: r } = a,
      n = m(),
      o = e.computes.rewardList(),
      l = s === ts.Vehicle,
      {
        breakpoint: { weight: c },
      } = Me(),
      d = c <= _e.small.weight ? ra.Small : ra.Big,
      _ = o.length > 9 ? [...Ba(o, 0, 9)] : o,
      u = Ra(rp(_.length)),
      p = o.length - _.length;
    return (0, ms.jsxs)("div", {
      className: tp.base,
      children: [
        l &&
          (0, ms.jsx)("div", {
            className: tp.preview,
            children: (0, ms.jsx)(za, { type: "preview", onClick: r }),
          }),
        (0, ms.jsxs)("div", {
          className: tp.content,
          children: [
            (0, ms.jsx)("div", { className: tp.shadow }),
            (0, ms.jsx)("div", {
              className: tp.title,
              children: (0, ms.jsx)(ap, { text: sp.title() }),
            }),
            (0, ms.jsx)("div", { className: tp.description, children: sp.description() }),
            (0, ms.jsx)("div", {
              className: tp.visibleRewards,
              children: re(_, (e, a) =>
                (0, ms.jsx)(
                  Un,
                  {
                    animationConfig: rp(a),
                    children: (0, ms.jsx)(L, { ...Xt(e, d), className: tp.reward }),
                  },
                  `${e.item}_${a}`,
                ),
              ),
            }),
            p > 0 &&
              (0, ms.jsx)(i.div, {
                style: u,
                children: (0, ms.jsx)(ya, {
                  type: Fe.ghost,
                  size: va.medium,
                  mixClass: tp.rewardButton,
                  onClick: () => {
                    n.push(ls.battlePass.buyPassRewards, { chapterID: t });
                  },
                  children: (0, ms.jsx)(aa, { text: sp.moreRewards(), binding: { count: p } }),
                }),
              }),
          ],
        }),
      ],
    });
  }),
  ip = "Rewards_full_eea97d7",
  op = { context: "model.rewards" },
  lp = Wt(() =>
    (0, ms.jsx)(hr, {
      options: op,
      children: (0, ms.jsx)("div", { className: ip, children: (0, ms.jsx)(Vr, {}) }),
    }),
  ),
  cp = "Tankmen_9641cad5",
  dp = "Tankmen_image_208678b",
  _p = "Tankmen_title_ebf30d50",
  up = "Tankmen_description_e7d7080c",
  mp = "Tankmen_tankmenBtn_96878805",
  pp = "Tankmen_button_e7e9840c",
  hp = "Tankmen_blink_22bb5961",
  bp = R.strings.battle_pass.holidayFinalScreen.tankmenState,
  fp = Wt(() => {
    const { controls: e } = Mm(),
      { showTankmen: a } = e;
    return (0, ms.jsxs)("div", {
      className: cp,
      children: [
        (0, ms.jsx)("div", { className: dp }),
        (0, ms.jsx)("div", { className: _p, children: (0, ms.jsx)(ap, { text: bp.title() }) }),
        (0, ms.jsx)("div", { className: up, children: bp.description() }),
        (0, ms.jsx)("div", {
          className: mp,
          children: (0, ms.jsxs)(ya, {
            type: Fe.main,
            size: va.medium,
            mixClass: pp,
            onClick: a,
            children: [(0, ms.jsx)("div", { className: hp }), bp.tankmenButton()],
          }),
        }),
      ],
    });
  }),
  gp = Wt(() => {
    const { model: e } = Mm(),
      { state: a } = e.root.get();
    switch (a) {
      case "buyState":
        return (0, ms.jsx)(np, {});
      case "rewardsState":
        return (0, ms.jsx)(lp, {});
      case "tankmenState":
        return (0, ms.jsx)(fp, {});
      case zm:
      case $m:
        return (0, ms.jsx)(Xm, {});
      default:
        return (console.warn("Unknown state ", a), null);
    }
  }),
  vp = "Footer_5f98e398",
  xp = "Footer_light_2fc739c7",
  wp = "Footer_buttonWrapper_fbd12995",
  Cp = "Footer_button_9e4f9bc",
  yp = "Footer_blink_106ec98e",
  Sp = R.strings.battle_pass.holidayFinalScreen.buyState,
  jp = Wt(() => {
    const { model: e } = Mm(),
      { isSeasonEndingSoon: a, chapterID: t } = e.root.get(),
      s = m();
    return (0, ms.jsxs)("div", {
      className: vp,
      children: [
        (0, ms.jsx)("div", { className: xp }),
        (0, ms.jsx)("div", {
          className: wp,
          children: (0, ms.jsxs)(ya, {
            type: Fe.main,
            size: va.medium,
            mixClass: Cp,
            onClick: () => {
              s.push(ls.battlePass.buyPass, { chapterID: t });
            },
            children: [a && (0, ms.jsx)("div", { className: yp }), Sp.buyButton()],
          }),
        }),
      ],
    });
  }),
  Ip = "Header_add5cf9d",
  Np = "Header_title_1435c6ee",
  kp = "Header_description_e959461d",
  Pp = ({ title: e, description: a }) =>
    (0, ms.jsxs)("div", {
      className: Ip,
      children: [
        (0, ms.jsx)("div", { className: Np, children: e }),
        (0, ms.jsx)("div", { className: kp, children: a }),
      ],
    }),
  Rp = {
    base: "App_ef84fef",
    base__rewardsState: "App_base__rewardsState_a9a568ab",
    background: "App_background_a2d1b7ea",
    base__tankmenState: "App_base__tankmenState_0",
    additionalAnimation: "App_additionalAnimation_eb290d79",
    fadeIn: "App_fadeIn_0",
    header: "App_header_4716088",
    awards: "App_awards_2541e2b5",
    footer: "App_footer_e521ba53",
    base__buyState: "App_base__buyState_0",
    fadeInWithScale: "App_fadeInWithScale_0",
    slideUp: "App_slideUp_0",
    blink: "App_blink_0",
    scale: "App_scale_0",
    rotate: "App_rotate_0",
    windowIn: "App_windowIn_0",
    fadeOut: "App_fadeOut_0",
  },
  Bp = R.strings.battle_pass,
  Ap = Wt(() => {
    const [e, a] = (0, us.useState)(!1),
      { model: t } = Mm(),
      { state: s, chapterID: r } = t.root.get(),
      n = m();
    return (
      (0, us.useEffect)(() => {
        (async () => {
          (await Yt(), a(!0));
        })();
      }, []),
      At(D.ESCAPE, () => n.goBack()),
      (0, ms.jsxs)("div", {
        className: sa(Rp.base, Rp[`base__${s}`]),
        children: [
          (0, ms.jsx)("div", { className: Rp.background }),
          e &&
            (0, ms.jsxs)("div", {
              className: Rp.additionalAnimation,
              children: [
                (0, ms.jsxs)("div", {
                  className: Rp.header,
                  children: [
                    (0, ms.jsx)(Pp, {
                      title: (0, ms.jsx)(aa, {
                        text: Bp.holidayFinalScreen.chapter(),
                        binding: { chapterName: Bp.chapter.fullNameUppercased.$num(r) },
                      }),
                      description: Bp.holidayFinalScreen.completed(),
                    }),
                    (0, ms.jsx)("div", {
                      className: Rp.awards,
                      children: (0, ms.jsx)(Wm, {
                        rootId: R.aliases.battle_pass.HolidayFinal("resId"),
                        context: "model.awardsWidget",
                      }),
                    }),
                  ],
                }),
                (0, ms.jsx)(gp, {}),
                (0, ms.jsx)("div", { className: Rp.footer, children: (0, ms.jsx)(jp, {}) }),
              ],
            }),
        ],
      })
    );
  }),
  Ep = () =>
    (0, ms.jsx)(Vm, {
      options: { rootId: R.aliases.battle_pass.HolidayFinal("resId") },
      children: (0, ms.jsx)(Ap, {}),
    }),
  Tp = 1e3,
  Lp = {
    ...pt,
    withStack: !0,
    type: Ja.Simple,
    delta: { duration: 500, delay: 300 },
    line: { duration: 500, delay: 300 },
  },
  Op = {
    ...pa,
    line: { ...pa.line, bgColorFinished: "#000000" },
    pattern: { ...pa.pattern, bgImageFinished: pa.bgImageBase },
  },
  Dp = (function (e) {
    return (
      (e.FillProgressMax = "fillProgressMax"),
      (e.RunCycle = "runCycle"),
      (e.ResetProgress = "resetProgress"),
      (e.RefillProgress = "refillProgress"),
      (e.Idle = "idle"),
      e
    );
  })({}),
  Wp = {
    fillProgressMax: { nextStep: "runCycle", delay: Tp },
    runCycle: { nextStep: "resetProgress", delay: 2200 },
    resetProgress: { nextStep: "refillProgress", delay: Tp },
    refillProgress: { nextStep: "idle", delay: Tp },
  },
  Vp = (function (e) {
    return (
      (e.COMPLETED = "completed"),
      (e.IN_PROGRESS = "inProgress"),
      (e.NOT_STARTED = "notStarted"),
      e
    );
  })({}),
  Mp = (function (e) {
    return (
      (e.NotAvailable = "notAvailable"),
      (e.PurchasingIP = "purchasingIP"),
      (e.ExtraChapter = "extraChapter"),
      e
    );
  })({}),
  zp = (function (e) {
    return ((e.left = "left"), (e.right = "right"), e);
  })({}),
  $p = (function (e) {
    return (
      (e[(e.Active = 0)] = "Active"),
      (e[(e.Paused = 1)] = "Paused"),
      (e[(e.Completed = 2)] = "Completed"),
      (e[(e.NotStarted = 3)] = "NotStarted"),
      e
    );
  })({}),
  Fp = (function (e) {
    return (
      (e[(e.Locked = 0)] = "Locked"),
      (e[(e.Unlocked = 1)] = "Unlocked"),
      (e[(e.Paused = 2)] = "Paused"),
      e
    );
  })({}),
  Hp = {
    "--small-card-width": "140rem",
    "--small-current-card-width": "224rem",
    "--medium-card-width": "220rem",
    "--medium-current-card-width": "340rem",
    "--extra-large-card-width": "276rem",
  },
  Up = (e, a = !1) =>
    a
      ? e < _e.medium.weight
        ? 224
        : 340
      : e < _e.medium.weight
        ? 140
        : e < _e.extraLarge.weight
          ? 220
          : 276,
  [Gp, qp] = He()(
    ({ observableModel: e }) => {
      const a = {
          root: e.object(),
          levels: e.array("levels"),
          chapters: e.array("chapters"),
          animationStep: wa.box(Dp.Idle),
        },
        t = xa((e) => {
          const t = a.levels.get(),
            s = le(t, e - 1);
          s || console.warn(`level info not found for number: ${e}`);
          const r = t.length;
          return { ...s, maxLevel: r, isFirstLevel: 1 === e, isLastLevel: e === r };
        }),
        s = xa((e) => {
          const a = t(e);
          return re(a.rewards, (e) => ({ ...e }));
        }),
        r = xa((e) => {
          const {
              currentLevel: s,
              currentLevelPoints: r,
              previousLevel: n,
              postProgressionStatus: i,
            } = a.root.get(),
            o = a.animationStep.get();
          if ([Dp.FillProgressMax, Dp.RunCycle].includes(o))
            return e === n ? Vp.IN_PROGRESS : Vp.COMPLETED;
          const { levelPoints: l, maxLevel: c } = t(e);
          return e < s || (s === c && r === l * c)
            ? Vp.COMPLETED
            : e === s && (i !== Fp.Locked || r > 0)
              ? Vp.IN_PROGRESS
              : Vp.NOT_STARTED;
        }),
        n = xa((e) => {
          const { postProgressionStatus: t } = a.root.get(),
            s = r(e);
          return { cardStatus: s, isDisabled: t !== Fp.Unlocked && s === Vp.NOT_STARTED };
        }),
        i = xa(
          () =>
            d()
              ? m().length && p() && h()
                ? Mp.ExtraChapter
                : u()
                  ? Mp.PurchasingIP
                  : void 0
              : Mp.NotAvailable,
          { equals: _ },
        ),
        l = xa(() => ea(a.chapters.get(), (e) => e.isRegular), { equals: _ }),
        c = xa(
          () => ea(a.chapters.get(), (e) => e.isRegular && e.chapterStatus === $p.Completed).length,
          { equals: _ },
        ),
        d = xa(() => c() === l().length),
        u = xa(() => Z(a.chapters.get(), (e) => !e.isBattlePassPurchased)),
        m = xa(() => ea(a.chapters.get(), (e) => !e.isRegular)),
        p = xa(() => Z(m(), (e) => e.chapterStatus !== $p.Active)),
        h = xa(() => Z(m(), (e) => e.chapterStatus !== $p.Completed)),
        b = xa(() => {
          const { currentLevel: e, currentLevelPoints: t } = a.root.get(),
            s = e - 1;
          return o(
            a.levels.get(),
            (e, { levelPoints: a }, r) => (r < s ? e + a : r === s ? e + t : e),
            0,
          );
        }),
        f = xa(() => o(a.levels.get(), (e, { levelPoints: a }) => e + a, 0)),
        g = xa(() => {
          const {
            currentLevel: e,
            currentLevelPoints: t,
            previousLevel: s,
            previousLevelPoints: r,
          } = a.root.get();
          return e !== s || t !== r;
        }),
        v = xa(() => {
          const { cyclesCompletedCount: e, previousCyclesCompletedCount: t } = a.root.get();
          return e > t;
        }),
        x = xa((e) => {
          const {
              currentLevel: s,
              currentLevelPoints: r,
              previousLevel: n,
              previousLevelPoints: i,
              postProgressionStatus: o,
            } = a.root.get(),
            l = a.animationStep.get(),
            { levelPoints: c, maxLevel: d } = t(s),
            { levelPoints: _ } = t(n),
            u = v(),
            [m = 0, p = 0] = ((e, a) => {
              const t = Up(e),
                s = Up(e, a);
              return [t, a ? s : t];
            })(e, o !== Fp.Locked),
            h = m * (d - 1) + p,
            b = (
              (e, a) =>
              (t, s, r, n = !1) =>
                e * (t - 1) + ((n ? e : a) / r) * s
            )(m, p),
            f = !u && n < s;
          return {
            progressValue: [Dp.FillProgressMax, Dp.RunCycle].includes(l) ? h : b(s, r, c),
            previousProgressValue: l === Dp.ResetProgress ? 0 : b(n, i, _, f),
            maxProgressValue: h,
          };
        }),
        w = xa(() => {
          const e = ea(
            m(),
            (e) =>
              (e.chapterStatus === $p.Active || e.chapterStatus === $p.Completed) &&
              !e.isBattlePassPurchased,
          );
          return e.length > 0 ? e : ea(a.chapters.get(), (e) => !e.isBattlePassPurchased);
        });
      return {
        ...a,
        computes: {
          footerState: i,
          regularChapters: l,
          completedRegularChaptersCount: c,
          extraChapters: m,
          cardStates: n,
          levelInfo: t,
          levelRewards: s,
          currentPointsInChapter: b,
          totalPointsInChapter: f,
          progressChanged: g,
          cycleChanged: v,
          getProgressValues: x,
          chaptersForPurchase: w,
        },
      };
    },
    ({ model: e, externalModel: a }) => ({
      openPointsInfo: a.createCallbackNoArgs("onOpenPointsInfo"),
      openInfoPage: a.createCallbackNoArgs("onOpenInfoPage"),
      setAnimationStep: ca((a) => e.animationStep.set(a)),
      handleProgressAchieved: a.createCallbackNoArgs("onProgressAchieved"),
      handleCycleCompleted: a.createCallbackNoArgs("onCycleCompleted"),
    }),
  ),
  Kp = "Highlight_ec6e9d0b",
  Xp = "Highlight_inner_fc05a4f9",
  Zp = "Highlight_side_ffdc7ad0",
  Jp = "Highlight_side__left_48f019cc",
  Qp = "Highlight_side__right_7a86ef2a",
  Yp = (0, us.memo)(() =>
    (0, ms.jsxs)("div", {
      className: Kp,
      children: [
        (0, ms.jsx)("div", { className: sa(Zp, Jp) }),
        (0, ms.jsx)("div", { className: Xp }),
        (0, ms.jsx)("div", { className: sa(Zp, Qp) }),
      ],
    }),
  ),
  eh = "Background_3985f66b",
  ah = "Background_default_7c7472e5",
  th = "Background_base__first_26effab7",
  sh = "Background_base__last_26effab7",
  rh = "Background_disabled_aebb7525",
  nh = Wt(({ level: e }) => {
    const { model: a } = qp(),
      { isFirstLevel: t, isLastLevel: s } = a.computes.levelInfo(e),
      { cardStatus: r, isDisabled: n } = a.computes.cardStates(e);
    return (0, ms.jsxs)("div", {
      className: sa(eh, t && th, s && sh),
      children: [
        (0, ms.jsx)("div", { className: ah }),
        n && (0, ms.jsx)("div", { className: rh }),
        r === Vp.IN_PROGRESS && (0, ms.jsx)(Yp, {}),
      ],
    });
  }),
  ih = {
    base: "CardRewards_178a6e14",
    base__completed: "CardRewards_base__completed_434ea7b1",
    rewards: "CardRewards_rewards_db8e5858",
    rewards__2: "CardRewards_rewards__2_32a806d4",
    base__inProgress: "CardRewards_base__inProgress_35611a2f",
    rewards__3: "CardRewards_rewards__3_6ac4c499",
    reward: "CardRewards_reward_8562c98f",
    rewards__1: "CardRewards_rewards__1_35611a2f",
    fadeInWithScale: "CardRewards_fadeInWithScale_35611a2f",
    slideUp: "CardRewards_slideUp_35611a2f",
    blink: "CardRewards_blink_35611a2f",
    scale: "CardRewards_scale_35611a2f",
    rotate: "CardRewards_rotate_35611a2f",
    windowIn: "CardRewards_windowIn_35611a2f",
    fadeOut: "CardRewards_fadeOut_35611a2f",
    fadeIn: "CardRewards_fadeIn_35611a2f",
  },
  oh = xa((e) => {
    const { item: a, name: t, value: s, overlayType: r, tooltipId: n, tooltipContentId: i } = e;
    return {
      name: a || t,
      smallImage: rt(e, ra.Big),
      bigImage: rt(e, ra.S180x135),
      special: r,
      value: s,
      valueType: Xe(t),
      tooltipArgs: Na({ tooltipId: n }, Number(i), { ignoreShowDelay: !0 }),
    };
  }),
  lh = Wt(({ level: e, className: a }) => {
    const { model: t } = qp(),
      s = t.computes.levelRewards(e),
      { cardStatus: r } = t.computes.cardStates(e),
      {
        breakpoint: { weight: n },
      } = Me(),
      i = n < _e.medium.weight,
      o = 1 === s.length,
      l = ((e, a) => (a ? (e ? ra.Big : ra.S180x135) : e ? ra.Small : ra.Big))(i, o),
      c = (e) => (i || !o ? e.smallImage : e.bigImage);
    return (0, ms.jsx)("div", {
      className: sa(ih.base, ih[`base__${r}`], a),
      children: (0, ms.jsx)("div", {
        className: sa(ih.rewards, ih[`rewards__${s.length}`]),
        children: re(s, (e, a) => {
          const t = oh(e);
          return (0, ms.jsx)(
            "div",
            { className: sa(ih.reward), children: (0, ms.jsx)(L, { size: l, image: c(t), ...t }) },
            `reward__${t.name}${a}`,
          );
        }),
      }),
    });
  }),
  ch = {
    base: "Divider_e7aefb14",
    base__left: "Divider_base__left_c4dc4b02",
    base__right: "Divider_base__right_5c287de9",
    inner: "Divider_inner_5e9c8eab",
    fadeInWithScale: "Divider_fadeInWithScale_76b1f722",
    slideUp: "Divider_slideUp_76b1f722",
    blink: "Divider_blink_76b1f722",
    scale: "Divider_scale_76b1f722",
    rotate: "Divider_rotate_76b1f722",
    windowIn: "Divider_windowIn_76b1f722",
    fadeOut: "Divider_fadeOut_76b1f722",
    fadeIn: "Divider_fadeIn_76b1f722",
  },
  dh = ({ position: e }) =>
    (0, ms.jsx)("div", {
      className: sa(ch.base, ch[`base__${e}`]),
      children: (0, ms.jsx)("div", { className: ch.inner }),
    }),
  _h = {
    base: "Stage_2019a8bb",
    number: "Stage_number_1d4a1a4c",
    animatedNumber: "Stage_animatedNumber_3b1e34e9",
    numberInProgress: "Stage_numberInProgress_9fdc0826",
    title: "Stage_title_29b5b4ba",
    glow: "Stage_glow_cc25be2a",
    base__inProgress: "Stage_base__inProgress_68142ff2",
    animatedGlow: "Stage_animatedGlow_a126942e",
    fadeInWithScale: "Stage_fadeInWithScale_68142ff2",
    slideUp: "Stage_slideUp_68142ff2",
    blink: "Stage_blink_68142ff2",
    scale: "Stage_scale_68142ff2",
    rotate: "Stage_rotate_68142ff2",
    windowIn: "Stage_windowIn_68142ff2",
    fadeOut: "Stage_fadeOut_68142ff2",
    fadeIn: "Stage_fadeIn_68142ff2",
  },
  uh = Wt(({ level: e, className: a }) => {
    const { model: t } = qp(),
      { postProgressionStatus: s } = t.root.get(),
      { cardStatus: r } = t.computes.cardStates(e),
      [n, o] = (0, us.useState)(!1),
      l = r === Vp.IN_PROGRESS,
      c = s === Fp.Unlocked,
      { stageOpacity: d } = Ra({
        from: { stageOpacity: n ? 1 : 0 },
        to: { stageOpacity: 0 },
        delay: 0,
        onStart: () => ue.sound(R.sounds.bp_current_phase()),
        config: { duration: 750, easing: ss },
      }),
      { sparkOpacity: _ } = Ra({
        from: { sparkOpacity: n ? 0.7 : 0 },
        to: { sparkOpacity: 0 },
        delay: 1100,
        onRest: () => o(!1),
        config: { duration: 300, easing: ss },
      });
    return (
      (0, us.useEffect)(() => {
        if (l)
          return ct(() => {
            o(!0);
          }, 100);
      }, [l]),
      (0, ms.jsx)("div", {
        className: sa(_h.base, _h[`base__${r}`], a),
        children: l
          ? (0, ms.jsxs)(ms.Fragment, {
              children: [
                c &&
                  (0, ms.jsxs)(ms.Fragment, {
                    children: [
                      (0, ms.jsx)("div", { className: _h.glow }),
                      (0, ms.jsx)(i.div, { style: { opacity: _ }, className: _h.animatedGlow }),
                    ],
                  }),
                (0, ms.jsxs)("div", {
                  className: _h.numberInProgress,
                  children: [
                    e,
                    (0, ms.jsx)(i.div, {
                      style: {
                        opacity: d,
                        transform: d
                          .to([0, 1], [2.5, 1])
                          .to((e) => `translate(-50%, -50%) scale(${e})`),
                      },
                      className: _h.animatedNumber,
                      children: e,
                    }),
                  ],
                }),
                (0, ms.jsx)("div", {
                  className: _h.title,
                  children: R.strings.battle_pass.postProgressionView.progression.currentStep(),
                }),
              ],
            })
          : (0, ms.jsx)("div", { className: _h.number, children: e }),
      })
    );
  }),
  mh = {
    base__showAnimation: "CompletedStatus_base__showAnimation_8334d234",
    slideUp: "CompletedStatus_slideUp_bdf18196",
    fadeIn: "CompletedStatus_fadeIn_bdf18196",
    base__hideAnimation: "CompletedStatus_base__hideAnimation_5e0caacf",
    slideDown: "CompletedStatus_slideDown_bdf18196",
    fadeOut: "CompletedStatus_fadeOut_bdf18196",
    icon: "CompletedStatus_icon_6277c5c1",
    iconGlow: "CompletedStatus_iconGlow_2dfae495",
    fadeInWithScale: "CompletedStatus_fadeInWithScale_bdf18196",
    blink: "CompletedStatus_blink_bdf18196",
    scale: "CompletedStatus_scale_bdf18196",
    rotate: "CompletedStatus_rotate_bdf18196",
    windowIn: "CompletedStatus_windowIn_bdf18196",
  },
  ph = ({ shouldAppear: e }) =>
    (0, ms.jsxs)("div", {
      className: sa(mh.base, e ? mh.base__showAnimation : mh.base__hideAnimation),
      children: [
        (0, ms.jsx)("div", { className: mh.iconGlow }),
        (0, ms.jsx)(U, {
          body: R.strings.battle_pass.tooltips.completed.got(),
          children: (0, ms.jsx)("div", { className: mh.icon }),
        }),
      ],
    }),
  hh = {
    base: "CurrentPoints_4c27ce16",
    base__appear: "CurrentPoints_base__appear_2cb3686f",
    fadeIn: "CurrentPoints_fadeIn_3970c66e",
    base__disappear: "CurrentPoints_base__disappear_e11174fb",
    fadeOut: "CurrentPoints_fadeOut_3970c66e",
    value__current: "CurrentPoints_value__current_9c51dee4",
    value__total: "CurrentPoints_value__total_99fac246",
    divider: "CurrentPoints_divider_83c77e4c",
    icon: "CurrentPoints_icon_6b371e14",
    fadeInWithScale: "CurrentPoints_fadeInWithScale_3970c66e",
    slideUp: "CurrentPoints_slideUp_3970c66e",
    blink: "CurrentPoints_blink_3970c66e",
    scale: "CurrentPoints_scale_3970c66e",
    rotate: "CurrentPoints_rotate_3970c66e",
    windowIn: "CurrentPoints_windowIn_3970c66e",
  },
  bh = Wt(({ totalLevelPoints: e, shouldAppear: a, shouldDisappear: t, className: s }) => {
    const { model: r } = qp(),
      { currentLevelPoints: n, previousLevelPoints: i } = r.root.get();
    return (0, ms.jsx)(me, {
      ignoreShowDelay: !0,
      contentId: R.views.mono.battle_pass.tooltips.bp_points("resId"),
      children: (0, ms.jsxs)("div", {
        className: sa(hh.base, a && hh.base__appear, t && hh.base__disappear, s),
        children: [
          (0, ms.jsx)("div", { className: sa(hh.value, hh.value__current), children: t ? i : n }),
          (0, ms.jsx)("div", { className: hh.divider, children: "/" }),
          (0, ms.jsx)("div", { className: sa(hh.value, hh.value__total), children: e }),
          (0, ms.jsx)("div", { className: hh.icon }),
        ],
      }),
    });
  }),
  fh = "Status_41b476d1",
  gh = "Status_pointsWrapper_6042cf48",
  vh = Wt(({ level: e, className: a }) => {
    const { model: t } = qp(),
      { cardStatus: s, isDisabled: r } = t.computes.cardStates(e),
      { levelPoints: n } = t.computes.levelInfo(e),
      i = t.animationStep.get(),
      o = [Dp.FillProgressMax, Dp.RunCycle].includes(i),
      l = i === Dp.ResetProgress,
      c = s === Vp.COMPLETED && !r,
      d = s === Vp.IN_PROGRESS,
      [_, u] = (0, us.useState)(c);
    return (
      (0, us.useEffect)(() => {
        if (i === Dp.RunCycle) return void u(!1);
        const a = i === Dp.FillProgressMax,
          t = i === Dp.ResetProgress;
        return _
          ? void 0
          : ct(
              () => {
                u(!!a || c);
              },
              (t ? 500 : 0) + 100 * e,
            );
      }, [i, _, c, e]),
      (0, ms.jsxs)("div", {
        className: sa(fh, a),
        children: [
          c && _ && (0, ms.jsx)(ph, { shouldAppear: _ }),
          d &&
            (0, ms.jsx)(bh, {
              className: gh,
              totalLevelPoints: n,
              shouldAppear: l,
              shouldDisappear: o,
            }),
        ],
      })
    );
  }),
  xh = {
    base: "Card_1d966e2a",
    base__inProgress: "Card_base__inProgress_b07d56b3",
    stage: "Card_stage_1d11f254",
    rewards: "Card_rewards_aba92251",
    status: "Card_status_f3176857",
    points: "Card_points_a0ccfd85",
    points__initial: "Card_points__initial_86462962",
    progressShadow: "Card_progressShadow_e0bd1d",
    fadeInWithScale: "Card_fadeInWithScale_f4c22d1c",
    slideUp: "Card_slideUp_f4c22d1c",
    blink: "Card_blink_f4c22d1c",
    scale: "Card_scale_f4c22d1c",
    rotate: "Card_rotate_f4c22d1c",
    windowIn: "Card_windowIn_f4c22d1c",
    fadeOut: "Card_fadeOut_f4c22d1c",
    fadeIn: "Card_fadeIn_f4c22d1c",
  },
  wh = Wt(({ level: e }) => {
    const { model: a } = qp(),
      { levelPoints: t, isFirstLevel: s, isLastLevel: r } = a.computes.levelInfo(e),
      { cardStatus: n } = a.computes.cardStates(e),
      i = !s && n === Vp.IN_PROGRESS,
      o = !r && a.computes.cardStates(e + 1).cardStatus !== Vp.IN_PROGRESS;
    return (0, ms.jsxs)("div", {
      className: sa(xh.base, xh[`base__${n}`]),
      style: Hp,
      children: [
        (0, ms.jsx)(nh, { level: e }),
        (0, ms.jsx)(uh, { className: xh.stage, level: e }),
        (0, ms.jsx)(lh, { className: xh.rewards, level: e }),
        (0, ms.jsx)(vh, { className: xh.status, level: e }),
        (0, ms.jsx)("div", { className: xh.points, children: e * t }),
        s && (0, ms.jsx)("div", { className: sa(xh.points, xh.points__initial), children: 0 }),
        i && (0, ms.jsx)(dh, { position: zp.left }),
        o && (0, ms.jsx)(dh, { position: zp.right }),
      ],
    });
  }),
  Ch = "Cards_afe60a85",
  yh = Wt(() => {
    const { model: e } = qp(),
      a = e.levels.get(),
      { chapterID: t } = e.root.get();
    return (0, ms.jsx)("div", {
      className: Ch,
      children: re(a, ({ level: e }, a) => (0, ms.jsx)(wh, { level: e }, `${t}_${a}`)),
    });
  }),
  Sh = "ExtraChapter_51af81b2",
  jh = "ExtraChapter_wrapper_1111764a",
  Ih = "ExtraChapter_border_1fc38ae",
  Nh = "ExtraChapter_base__hover_d6a2f84c",
  kh = "ExtraChapter_bg_6bfbbfc5",
  Ph = "ExtraChapter_widget_ba8b2337",
  Rh = "ExtraChapter_title_4965d60",
  Bh = "ExtraChapter_description_1a9020c",
  Ah = "ExtraChapter_content_7e770f3c",
  Eh = R.strings.battle_pass.postProgressionView.footer.extraChapter,
  Th = Wt(() => {
    const { model: e } = qp(),
      a = e.computes.extraChapters()[0]?.chapterID,
      [t, s] = (0, us.useState)(!1),
      r = m();
    return a
      ? (0, ms.jsxs)("div", {
          className: sa(Sh, t && Nh),
          onMouseOver: (e) => {
            (e.stopPropagation(), s(!0), ue.sound(R.sounds.highlight()));
          },
          onMouseOut: () => {
            s(!1);
          },
          onClick: () => {
            (r.push(ls.battlePass.progression, { chapterID: a }), ue.sound(R.sounds.play()));
          },
          children: [
            (0, ms.jsxs)("div", {
              className: jh,
              children: [
                (0, ms.jsx)("div", { className: kh }),
                (0, ms.jsxs)("div", {
                  className: Ah,
                  children: [
                    (0, ms.jsx)("div", { className: Rh, children: Eh.title.text() }),
                    (0, ms.jsx)("div", { className: Bh, children: Eh.description.text() }),
                  ],
                }),
              ],
            }),
            (0, ms.jsx)("div", { className: Ph }),
            (0, ms.jsx)("div", { className: Ih }),
          ],
        })
      : null;
  }),
  Lh = "NotAvailable_e1e3731d",
  Oh = "NotAvailable_background_a3edbc06",
  Dh = "NotAvailable_content_94110074",
  Wh = "NotAvailable_button_149fb125",
  Vh = "NotAvailable_description_6cafdd55",
  Mh = "NotAvailable_completedCount_8450f150",
  zh = R.strings.battle_pass.postProgressionView.footer,
  $h = Wt(() => {
    const { model: e } = qp(),
      a = m(),
      t = e.computes.completedRegularChaptersCount(),
      s = e.computes.regularChapters().length;
    return (0, ms.jsxs)("div", {
      className: Lh,
      children: [
        (0, ms.jsx)("div", { className: Oh }),
        (0, ms.jsxs)("div", {
          className: Dh,
          children: [
            (0, ms.jsx)(aa, {
              classMix: Vh,
              text: zh.description.text(),
              binding: {
                completedChapters: (0, ms.jsx)("span", { className: Mh, children: t }),
                chaptersAmount: s,
              },
            }),
            (0, ms.jsx)(ya, {
              type: Fe.ghost,
              size: va.medium,
              mixClass: Wh,
              onClick: () => a.push(ls.battlePass.chapterChoice),
              children: zh.button.text(),
            }),
          ],
        }),
      ],
    });
  }),
  Fh = "PurchasingIp_349aa5c4",
  Hh = "PurchasingIp_wrapper_2ff2079e",
  Uh = "PurchasingIp_border_78bb5b9b",
  Gh = "PurchasingIp_base__hover_e6cc332b",
  qh = "PurchasingIp_bg_345ee932",
  Kh = "PurchasingIp_blink_990fb4a0",
  Xh = "PurchasingIp_text_4355bb8a",
  Zh = "PurchasingIp_button_b213818",
  Jh = "PurchasingIp_content_b09e9d85",
  Qh = R.strings.battle_pass.postProgressionView.footer.purchaseIP,
  Yh = Wt(() => {
    const { model: e } = qp(),
      a = m(),
      [t, s] = (0, us.useState)(!1);
    return (0, ms.jsxs)("div", {
      className: sa(Fh, t && Gh),
      onMouseOver: (e) => {
        (e.stopPropagation(), s(!0), ue.sound(R.sounds.highlight()));
      },
      onMouseOut: () => {
        s(!1);
      },
      onClick: () => {
        const t = e.computes.chaptersForPurchase();
        (ue.sound(R.sounds.play()), a.push(ls.battlePass.buyPass, { chapterID: t[0]?.chapterID }));
      },
      children: [
        (0, ms.jsxs)("div", {
          className: Hh,
          children: [
            (0, ms.jsx)("div", { className: qh }),
            (0, ms.jsx)("div", { className: Kh }),
            (0, ms.jsxs)("div", {
              className: Jh,
              children: [
                (0, ms.jsx)("div", {
                  className: Xh,
                  children:
                    R.strings.battle_pass.postProgressionView.footer.purchaseIP.banner.text(),
                }),
                (0, ms.jsx)(ya, {
                  type: Fe.main,
                  size: va.medium,
                  mixClass: Zh,
                  children: Qh.button.text(),
                }),
              ],
            }),
          ],
        }),
        (0, ms.jsx)("div", { className: Uh }),
      ],
    });
  }),
  eb = "Footer_447447a9",
  ab = Wt(({ className: e = "" }) => {
    const { model: a } = qp(),
      t = a.computes.footerState();
    return (0, ms.jsx)("div", {
      className: sa(eb, e),
      children: (() => {
        switch (t) {
          case Mp.NotAvailable:
            return (0, ms.jsx)($h, {});
          case Mp.PurchasingIP:
            return (0, ms.jsx)(Yh, {});
          case Mp.ExtraChapter:
            return (0, ms.jsx)(Th, {});
          default:
            return null;
        }
      })(),
    });
  }),
  tb = "Header_8161ac6c",
  sb = "Header_background_ca26eac9",
  rb = "Header_headlineContainer_83fb95ed",
  nb = "Header_headline_49f93202",
  ib = "Header_divider_d589871a",
  ob = "Header_title_87287815",
  lb = "Header_descriptionContainer_5475d6de",
  cb = "Header_descriptionPaused_65f475ba",
  db = "Header_description_1d21a2e3",
  _b = "Header_icon_c2a24f90",
  ub = "Header_label_f1c2cd27",
  mb = R.strings.battle_pass.postProgressionView.header,
  pb = Wt(({ className: e }) => {
    const { postProgressionStatus: a, endDate: t } = qp().model.root.get(),
      r = a === Fp.Locked,
      n = a === Fp.Paused,
      i = s(t, ha.DayMonthFull);
    return (0, ms.jsxs)("div", {
      className: sa(tb, e),
      children: [
        (0, ms.jsx)("div", { className: sb }),
        (0, ms.jsxs)("div", {
          className: rb,
          children: [
            !r &&
              (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsx)("span", { className: nb, children: mb.headline.unlocked() }),
                  (0, ms.jsx)("div", { className: ib }),
                ],
              }),
            (0, ms.jsx)(aa, {
              classMix: nb,
              text: mb.headline.deadline(),
              binding: { endDate: i },
            }),
          ],
        }),
        (0, ms.jsx)("span", { className: ob, children: mb.title() }),
        (0, ms.jsx)("div", {
          className: lb,
          children: n
            ? (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsx)("div", { className: _b }),
                  (0, ms.jsx)("span", {
                    className: ub,
                    children: mb.description.onPause.highlight(),
                  }),
                  (0, ms.jsx)("span", {
                    className: cb,
                    children: mb.description.onPause.regular(),
                  }),
                ],
              })
            : (0, ms.jsx)("span", { className: db, children: mb.description.active() }),
        }),
      ],
    });
  }),
  hb = "Counter_530269bb",
  bb = "Counter_infinityIconContainer_1ffbc2e2",
  fb = "Counter_infinityIcon_d060ec47",
  gb = "Counter_label_3f062fe0",
  vb = "Counter_cyclesCompleted_98e1bb2c",
  xb = "Counter_cyclesNumber_623ae487",
  wb = "Counter_cyclesNumber__animated_78a25366",
  Cb = "Counter_cyclesNumber__hidden_4c746c1c",
  yb = R.strings.battle_pass.postProgressionView.progression,
  Sb = Wt(({ className: e, labelRef: a, shouldRun: t }) => {
    const { model: s } = qp(),
      { cyclesCompletedCount: r, previousCyclesCompletedCount: n } = s.root.get(),
      i = s.animationStep.get(),
      o = r !== n && [Dp.Idle, Dp.FillProgressMax].includes(i);
    return (0, ms.jsxs)("div", {
      className: sa(hb, e),
      ref: a,
      children: [
        (0, ms.jsx)("div", { className: bb, children: (0, ms.jsx)("div", { className: fb }) }),
        (0, ms.jsx)("div", {
          className: gb,
          children: r
            ? (0, ms.jsxs)("div", {
                className: vb,
                children: [
                  (0, ms.jsx)("span", { children: yb.cyclesCompleted() }),
                  (0, ms.jsx)(
                    "span",
                    { className: sa(xb, t && wb, o && Cb), children: r },
                    `cyclesCompletedCount-${t}`,
                  ),
                ],
              })
            : yb.cyclicalProgression(),
        }),
      ],
    });
  }),
  jb = {
    base: "Cycle_74f0e867",
    labelContainer: "Cycle_labelContainer_3604ca19",
    contour: "Cycle_contour_24ba23fd",
    border: "Cycle_border_c131c31f",
    border__horizontal: "Cycle_border__horizontal_c4a77614",
    contour__2x: "Cycle_contour__2x_8af1a177",
    border__vertical: "Cycle_border__vertical_218efe03",
    arrow: "Cycle_arrow_9ac4ac6",
    bar: "Cycle_bar_ed90b853",
    bar__state1: "Cycle_bar__state1_cdb101bd",
    state1: "Cycle_state1_8af1a177",
    bar__state2: "Cycle_bar__state2_19af5de",
    state2: "Cycle_state2_8af1a177",
    bar__state3: "Cycle_bar__state3_297a53d6",
    state3: "Cycle_state3_8af1a177",
    bar__state4: "Cycle_bar__state4_a23fc208",
    state4: "Cycle_state4_8af1a177",
    bar__state5: "Cycle_bar__state5_e607ac47",
    state5: "Cycle_state5_8af1a177",
    fadeInWithScale: "Cycle_fadeInWithScale_8af1a177",
    slideUp: "Cycle_slideUp_8af1a177",
    blink: "Cycle_blink_8af1a177",
    scale: "Cycle_scale_8af1a177",
    rotate: "Cycle_rotate_8af1a177",
    windowIn: "Cycle_windowIn_8af1a177",
    fadeOut: "Cycle_fadeOut_8af1a177",
    fadeIn: "Cycle_fadeIn_8af1a177",
  },
  Ib = "--label-offset",
  Nb = { left: 0, width: 0 },
  kb = Wt(({ className: e, shouldRun: a }) => {
    const { model: t } = qp(),
      { cyclesCompletedCount: s } = t.root.get(),
      r = (0, us.useRef)(null),
      n = (0, us.useRef)(null),
      {
        breakpoint: { weight: i },
      } = Me(),
      o = Ta(),
      [l, c] = (0, us.useState)({ [Ib]: "0%" });
    return (
      y(() => {
        const e = r.current?.getBoundingClientRect() ?? Nb,
          a = n.current?.getBoundingClientRect().left ?? 0,
          t = 15 * o,
          s = (100 * (a - e.left - t)) / e.width;
        c({ [Ib]: `${s}%` });
      }, [r.current, n.current, i, o, s]),
      (0, ms.jsxs)("div", {
        className: sa(jb.base, e),
        style: l,
        children: [
          (0, ms.jsx)("div", { className: jb.arrow }),
          (0, ms.jsxs)("div", {
            className: sa(jb.contour, jb[`contour__${o}x`]),
            ref: r,
            children: [
              (0, ms.jsx)("div", { className: sa(jb.border, jb.border__vertical) }),
              (0, ms.jsx)("div", { className: sa(jb.border, jb.border__horizontal) }),
              a &&
                Array(5)
                  .fill(void 0)
                  .map((e, a) =>
                    (0, ms.jsx)(
                      "div",
                      { className: sa(jb.bar, jb[`bar__state${a + 1}`]) },
                      `bar-${a}`,
                    ),
                  ),
            ],
          }),
          (0, ms.jsx)(Sb, { className: jb.labelContainer, labelRef: n, shouldRun: a }),
        ],
      })
    );
  }),
  Pb = "ProgressBar_7a10c6f0",
  Rb = "ProgressBar_progressBackground_ce66ede4",
  Bb = "ProgressBar_progressBar_61381794",
  Ab = "ProgressBar_progressBar__disabled_f37621b4",
  Eb = "ProgressBar_optimizedProgressBar_87a4af2b",
  Tb = "ProgressBar_cycle_7886c8",
  Lb = Wt(() => {
    const { model: e, controls: a } = qp(),
      { postProgressionStatus: t } = e.root.get(),
      s = e.animationStep.get(),
      r = s === Dp.RunCycle,
      n = t === Fp.Locked,
      i = t === Fp.Paused,
      o = n || i,
      {
        breakpoint: { weight: l },
      } = Me(),
      {
        progressValue: c,
        previousProgressValue: d,
        maxProgressValue: _,
      } = e.computes.getProgressValues(l),
      u = e.computes.progressChanged();
    ((0, us.useEffect)(() => {
      switch (s) {
        case Dp.FillProgressMax:
        case Dp.RefillProgress:
          return void a.handleProgressAchieved();
        case Dp.RunCycle:
          return void a.handleCycleCompleted();
      }
    }, [s, a]),
      (0, us.useEffect)(() => {
        if (u && s === Dp.Idle)
          return ct(() => {
            a.handleProgressAchieved();
          }, Tp);
      }, [s, a, u]));
    const m = (0, us.useRef)(ta());
    return (0, ms.jsxs)("div", {
      className: Pb,
      style: { "--progress-line-width": `${_}rem` },
      children: [
        (0, ms.jsx)("div", { className: Rb }),
        (0, ms.jsx)(me, {
          contentId: R.views.mono.battle_pass.tooltips.bp_points("resId"),
          children: (0, ms.jsx)("div", {
            className: sa(Bb, o && Ab),
            children: (0, ms.jsx)(ot, {
              api: m,
              value: c,
              deltaFrom: d,
              maxValue: _,
              disabled: o,
              animationSettings: Lp,
              theme: Op,
              className: Eb,
            }),
          }),
        }),
        (0, ms.jsx)(kb, { className: Tb, shouldRun: r }),
      ],
    });
  }),
  Ob = "Toolbar_infoButtons_dd878d8c",
  Db = R.strings.battle_pass.postProgressionView.toolbar,
  Wb = Wt(({ className: e }) => {
    const { openInfoPage: a, openPointsInfo: t } = qp().controls;
    return (0, ms.jsx)("div", {
      className: e,
      children: (0, ms.jsxs)("div", {
        className: Ob,
        children: [
          (0, ms.jsx)(qa, { caption: Db.aboutBattlePass(), type: "info", onClick: a }),
          (0, ms.jsx)(qa, { caption: Db.howToEarnPoints(), type: "info", onClick: t }),
        ],
      }),
    });
  }),
  Vb = "App_ad9a5024",
  Mb = "App_toolbar_d16ffb0a",
  zb = "App_awardsWidget_1186a317",
  $b = "App_award_70e8698f",
  Fb = "App_content_b9a70459",
  Hb = "App_header_77cc1fba",
  Ub = "App_progression_992167b9",
  Gb = "App_footer_e6643cae",
  qb = R.images.gui.maps.icons.battlePass.backgrounds.progression,
  Kb = Wt(() => {
    const { model: e, controls: a } = qp(),
      { chapterID: t } = e.root.get(),
      s = e.animationStep.get(),
      r = e.computes.cycleChanged(),
      n = m();
    ((0, us.useEffect)(() => {
      if (s !== Dp.Idle) {
        const { nextStep: e, delay: t } = Wp[s];
        return ct(() => {
          a.setAnimationStep(e);
        }, t);
      }
      r && a.setAnimationStep(Dp.FillProgressMax);
    }, [s, a, r]),
      At(D.ESCAPE, () => n.goBack()));
    const i = `url(${is(qb, t)})`;
    return (0, ms.jsxs)("div", {
      className: Vb,
      style: { backgroundImage: i },
      children: [
        (0, ms.jsx)(Wb, { className: Mb }),
        (0, ms.jsx)(Wm, {
          rootId: R.aliases.battle_pass.PostProgression("resId"),
          context: "model.awardsWidget",
          classNames: { base: zb, award: $b },
        }),
        (0, ms.jsxs)("div", {
          className: Fb,
          children: [
            (0, ms.jsx)(pb, { className: Hb }),
            (0, ms.jsxs)("div", {
              className: Ub,
              children: [(0, ms.jsx)(yh, {}), (0, ms.jsx)(Lb, {})],
            }),
          ],
        }),
        (0, ms.jsx)(ab, { className: Gb }),
      ],
    });
  }),
  Xb = () =>
    (0, ms.jsx)(Gp, {
      options: { rootId: R.aliases.battle_pass.PostProgression("resId") },
      children: (0, ms.jsx)(Kb, {}),
    }),
  Zb = (function (e) {
    return (
      (e.Active = "active"),
      (e.Paused = "paused"),
      (e.Completed = "completed"),
      (e.NotStarted = "notStarted"),
      e
    );
  })({}),
  Jb = (function (e) {
    return (
      (e.NoAction = "noAction"),
      (e.Buy = "buy"),
      (e.BuyLevel = "buyLevel"),
      (e.ActivateChapter = "activateChapter"),
      e
    );
  })({}),
  Qb = (function (e) {
    return ((e.COMMON = "common"), (e.EXTRA = "extra"), (e.HOLIDAY = "holiday"), e);
  })({}),
  Yb = (function (e) {
    return ((e.left = "left"), (e.right = "right"), e);
  })({}),
  ef = (function (e) {
    return (
      (e.COMPLETED = "completed"),
      (e.IN_PROGRESS = "inProgress"),
      (e.NOT_STARTED = "notStarted"),
      e
    );
  })({}),
  af = (function (e) {
    return (
      (e.UNLOCK_BIG = "bp_unlock_big"),
      (e.UNLOCK_SMALL = "bp_unlock_small"),
      (e.IMPROVED_REWARD = "bp_improved_reward"),
      e
    );
  })({}),
  tf = (function (e) {
    return ((e.back = "back"), (e.forward = "forward"), e);
  })({}),
  sf = (function (e) {
    return ((e.Default = "default"), (e.Gray = "gray"), e);
  })({}),
  rf = [Zb.Active, Zb.Completed],
  [nf, of] = He()(
    ({ observableModel: e }) => {
      const a = {
          root: e.object(),
          levels: e.array("levels.items"),
          widget3dStyle: e.object("widget3dStyle"),
          widget3dStyleVehicleInfo: e.object("widget3dStyle.vehicleInfo"),
          widgetFinalRewards: e.object("widgetFinalRewards"),
          vehicleInfo: e.object("widgetFinalRewards.vehicleInfo"),
          freeTankmanInfo: e.array("widgetFinalRewards.tankmanInfo.free"),
          paidTankmanInfo: e.array("widgetFinalRewards.tankmanInfo.paid"),
          styleInfo: e.object("widgetFinalRewards.styleInfo"),
          vehicleInfoFromStyle: e.object("widgetFinalRewards.styleInfo.vehicleInfo"),
          attachmentsSetInfo: e.object("widgetFinalRewards.attachmentsSetInfo"),
          freeFinalRewards: e.array("freeFinalRewards"),
          paidFinalRewards: e.array("paidFinalRewards"),
          starterPackRewards: e.array("starterPackRewards.items"),
        },
        t = xa(() => re(a.freeFinalRewards.get(), E), { equals: _ }),
        s = xa(() => re(a.paidFinalRewards.get(), E), { equals: _ }),
        r = xa(() => re(a.starterPackRewards.get(), E), { equals: _ }),
        n = xa(() => a.root.get().chapterType === Qb.HOLIDAY),
        i = xa(() => ({
          freeFinalRewards: Zt(t()),
          ...(s().length && { paidFinalRewards: Zt(s()) }),
        })),
        o = xa(() => {
          const { freeFinalRewards: e, paidFinalRewards: a } = i();
          return !(!a && e.mainReward === rs.progressiveStyle);
        }),
        l = xa(() => a.root.get().chapterType === Qb.EXTRA),
        c = xa(() => !(n() || l()), { equals: _ }),
        d = xa((e) => (e ? a.paidTankmanInfo.get() : a.freeTankmanInfo.get())),
        u = xa((e) => {
          const t = a.levels.get(),
            s = le(t, e - 1);
          return (
            s || console.warn(`level info not found for number: ${e}`),
            { ...s, maxLevel: t.length }
          );
        }),
        m = xa((e, a) => {
          const t = u(e);
          return re(a ? t.freeRewardItems.items : t.paidRewardItems.items, (e) => ({ ...e }));
        }),
        p = xa(() => {
          const {
            freePointsInLevel: e,
            currentPointsInLevel: t,
            chapterState: s,
            hasExtra: r,
          } = a.root.get();
          return { current: rf.includes(s) || r ? t : e, total: u(1)?.levelPoints };
        }),
        h = xa((e, t) => {
          const {
              chapterState: s,
              currentLevel: r,
              potentialLevel: n,
              currentPointsInChapter: i,
              freePointsInChapter: o,
            } = a.root.get(),
            { levelPoints: l, maxLevel: c } = u(e),
            d = t ? o : i,
            _ = t ? n : r;
          return e < _ || (_ === c && d === l * c)
            ? ef.COMPLETED
            : e === _ && (s !== Zb.NotStarted || d > 0)
              ? ef.IN_PROGRESS
              : ef.NOT_STARTED;
        }),
        b = xa((e, t, s, r) => {
          const { currentLevel: n, currentPointsInLevel: i } = a.root.get();
          return ((n - 1) * e + (i / r) * t) / s;
        }),
        f = xa(() => ye(a.levels.get(), (e) => "number" == typeof e.levelPoints)?.levelPoints),
        g = xa((e, a) => {
          const { needTakeFree: t, needTakePaid: s } = u(e);
          return a ? s : t;
        }),
        v = xa((e, t) => {
          const { isBattlePassPurchased: s, chapterState: r } = a.root.get(),
            n = u(e),
            i = h(e, !1);
          return {
            cardStatus: { current: i, potential: h(e, !0) },
            isRare: n.isRare && i !== ef.IN_PROGRESS,
            isDisabled: (t && !s) || (r !== Zb.Active && i === ef.NOT_STARTED),
          };
        });
      return {
        ...a,
        computes: {
          getFreeFinalRewards: t,
          getPaidFinalRewards: s,
          regularBattlePass: c,
          getFinalRewardTankmanInfo: d,
          currentLevelPoints: p,
          levelInfo: u,
          levelRewardItems: m,
          getCurrentWidth: b,
          getTotalLevelPoints: f,
          isRewardNeedTake: g,
          cardStates: v,
          isLayoutWithExtraWidget: o,
          getFinalRewardsDescription: i,
          getStarterPackRewards: r,
        },
      };
    },
    ({ externalModel: e }) => ({
      chapterActivate: e.createCallbackNoArgs("onChapterActivate"),
      openAbout: e.createCallbackNoArgs("onAboutClick"),
      openPreview: e.createCallbackNoArgs("widgetFinalRewards.onRewardPreviewClick"),
      open3dStylePreview: e.createCallback((e) => ({ level: e }), "widget3dStyle.onPreviewClick"),
      onStyleBonusPreview: e.createCallback((e) => ({ bonusId: e }), "onStyleBonusPreview"),
      showTankmen: e.createCallbackNoArgs("widgetFinalRewards.showTankmen"),
      openInfo: e.createCallbackNoArgs("onPointsInfoClick"),
      viewLoad: e.createCallbackNoArgs("onViewLoaded"),
      finishLevelsAnimation: e.createCallbackNoArgs("onLevelsAnimationFinished"),
      takeReward: e.createCallback(({ level: e }) => ({ level: e }), "onTakeClick"),
      finishAnimation: e.createCallbackNoArgs("onFinishedAnimation"),
    }),
  ),
  lf = "AttachmentsSetDescription_title_be2f4c09",
  cf = "AttachmentsSetDescription_name_30b7f496",
  df = Qa.resolve("strings"),
  _f = Wt(() => {
    const { model: e, controls: a } = of(),
      { attachmentsSetName: t } = e.attachmentsSetInfo.get();
    return (0, ms.jsxs)(ms.Fragment, {
      children: [
        (0, ms.jsx)(za, { type: "preview", size: "normal", onClick: a.openPreview }),
        (0, ms.jsx)("span", {
          className: lf,
          children: df.readOrEmpty("battle_pass.finalReward.attachmentsSet.title"),
        }),
        (0, ms.jsx)("span", {
          className: cf,
          children: df.readOrEmpty(`quests.bonusName.attachments_set.${t}`),
        }),
      ],
    });
  }),
  uf = "AdditionalRewardInfo_rewardText_31efb669",
  mf = "AdditionalRewardInfo_subTitle_251693c1",
  pf = "AdditionalRewardInfo_subTitleTextWrapper_19819b2b",
  hf = "AdditionalRewardInfo_subTitleText_b6b02718",
  bf = "AdditionalRewardInfo_subTitleText__truncated_539e6fd4",
  ff = "AdditionalRewardInfo_infoIcon_a4fa826d",
  gf = R.strings.battle_pass.progression.extraChapterWidget,
  vf = Wt(({ additionalReward: e }) => {
    const {
        model: { widgetFinalRewards: a, styleInfo: t, vehicleInfo: s },
      } = of(),
      { vehicleName: r } = s.get(),
      { battleQuest: n } = a.get(),
      [i, o] = (0, us.useState)(!1),
      l = (0, us.useRef)(null),
      c = (0, us.useCallback)(async () => {
        await Yt();
        const e = l.current;
        e && o(e.scrollWidth > e.offsetWidth);
      }, []);
    return (
      Re(
        () => (
          c(),
          engine.on("clientResized", c),
          () => {
            engine.off("clientResized", c);
          }
        ),
      ),
      (0, ms.jsxs)(ms.Fragment, {
        children: [
          e === rs.style &&
            (0, ms.jsx)(aa, {
              classMix: uf,
              text: gf.vehicleSubTitle(),
              binding: { styleName: t.get().styleName },
            }),
          e === rs.battleQuest &&
            (0, ms.jsx)(me, {
              contentId: R.views.mono.battle_pass.tooltips.random_quest("resId"),
              args: { tokenID: n },
              children: (0, ms.jsxs)("div", {
                className: mf,
                children: [
                  (0, ms.jsx)("div", {
                    className: pf,
                    children: (0, ms.jsx)("div", {
                      className: sa(hf, i && bf),
                      ref: l,
                      children: (0, ms.jsx)(aa, {
                        text: gf.styleSubTitle(),
                        binding: { vehicleName: r },
                      }),
                    }),
                  }),
                  (0, ms.jsx)("div", { className: ff }),
                ],
              }),
            }),
        ],
      })
    );
  }),
  xf = "StyleDescription_rewardTitle_a38f5a35",
  wf = "StyleDescription_rewardTitle__singleReward_844cd016",
  Cf = "StyleDescription_title_10aa0199",
  yf = "StyleDescription_title__singleReward_4f032bf8",
  Sf = "StyleDescription_vehicleTitle_d97e976a",
  jf = "StyleDescription_vehicleLabel_d39e5139",
  If = "StyleDescription_vehicleInHangar_f82728b9",
  Nf = "StyleDescription_remark_bf754841",
  kf = "StyleDescription_lockIcon_6a873423",
  Pf = "StyleDescription_baseClass_cf456a8f",
  Rf = "StyleDescription_name_9ce7517f",
  Bf = "StyleDescription_level_7a97d385",
  Af = "StyleDescription_type_8cffe3f7",
  Ef = R.strings.battle_pass.progression.extraChapterWidget,
  Tf = Wt(({ additionalReward: e, isPaidReward: a }) => {
    const {
        model: { styleInfo: t, vehicleInfoFromStyle: s, root: r, computes: n },
        controls: i,
      } = of(),
      { isBattlePassPurchased: o } = r.get(),
      { styleName: l, isVehicleInHangar: c } = t.get(),
      d = n.getPaidFinalRewards().length,
      _ = { base: Pf, level: Bf, name: Rf, typeIcon: Af };
    return (0, ms.jsxs)(ms.Fragment, {
      children: [
        (0, ms.jsx)(za, { type: "preview", size: "normal", onClick: i.openPreview }),
        (0, ms.jsx)("div", {
          className: sa(xf, !d && wf),
          children: d ? Ef.style3DTitle() : Ef.styleTitle(),
        }),
        (0, ms.jsx)(aa, {
          classMix: sa(Cf, !d && yf),
          text: Ef.styleName(),
          binding: { styleName: l },
        }),
        !d &&
          (0, ms.jsxs)("div", {
            className: Sf,
            children: [
              (0, ms.jsx)(aa, {
                classMix: jf,
                text: Ef.forLabel(),
                binding: {
                  vehicleName: (0, ms.jsx)(ns, {
                    ...s.get(),
                    classNames: _,
                    vehicleTypeIconSize: ne.x24x24,
                  }),
                },
              }),
              c &&
                (0, ms.jsx)(U, {
                  body: Ef.inHangarTooltip(),
                  children: (0, ms.jsx)("div", { className: If }),
                }),
            ],
          }),
        e && (0, ms.jsx)(vf, { additionalReward: e }),
        a &&
          !o &&
          (0, ms.jsx)(me, {
            contentId: R.views.mono.battle_pass.tooltips.lock_icon("resId"),
            children: (0, ms.jsxs)("div", {
              className: Nf,
              children: [
                (0, ms.jsx)("div", { className: kf }),
                (0, ms.jsx)("div", { children: Ef.styleRemark() }),
              ],
            }),
          }),
      ],
    });
  }),
  Lf = "Skills_12e25c21",
  Of = "Skills_skill_d5e5036d",
  Df = "Skills_zeroSkill_8baec091",
  Wf = "Skills_glow_b87093c6",
  Vf = "Skills_zeroSkillIcon_f9fb247",
  Mf = "Skills_skillIcon_2a4ffd3a",
  zf = "Skills_skillIcon__specificPerk_9fedba",
  $f = "Skills_divider_5189f326",
  Ff = "Skills_light_dc85d289",
  Hf = ({ skills: e, className: a = "" }) => {
    const t = Ct(e, (e) => e.isZero);
    return (0, ms.jsxs)("div", {
      className: sa(Lf, a),
      children: [
        re(e, (e, a) =>
          (0, ms.jsxs)(
            "div",
            {
              className: Of,
              children: [
                (0, ms.jsx)(me, {
                  contentId: R.views.mono.battle_pass.tooltips.crew_member_skill("resId"),
                  args: { name: e.name, isZero: e.isZero, hasZeroPerk: void 0 !== t },
                  children: (0, ms.jsxs)("div", {
                    children: [
                      e.isZero &&
                        "new_skill" === e.name &&
                        (0, ms.jsxs)("div", {
                          className: Df,
                          children: [
                            (0, ms.jsx)("div", { className: Wf }),
                            (0, ms.jsx)("div", { className: Vf }),
                          ],
                        }),
                      (0, ms.jsx)("div", {
                        className: sa(Mf, "new_skill" !== e.name && zf),
                        style: {
                          backgroundImage: `url('R.images.gui.maps.icons.battlePass.tankman.perks.icon_perk_${e.name}')`,
                        },
                      }),
                    ],
                  }),
                }),
                t === a && (0, ms.jsx)("div", { className: $f }),
              ],
            },
            `${e.name}_${a}`,
          ),
        ),
        (0, ms.jsx)("div", { className: Ff }),
      ],
    });
  },
  Uf = {
    base: "Voice_c37942b8",
    icon: "Voice_icon_341b24d6",
    icon__speaker: "Voice_icon__speaker_172c2c35",
    icon__wave0: "Voice_icon__wave0_77617b3a",
    base__animate: "Voice_base__animate_d1a20ef1",
    wave0: "Voice_wave0_d1a20ef1",
    icon__wave1: "Voice_icon__wave1_1096fc2",
    wave1: "Voice_wave1_d1a20ef1",
    fadeInWithScale: "Voice_fadeInWithScale_d1a20ef1",
    slideUp: "Voice_slideUp_d1a20ef1",
    blink: "Voice_blink_d1a20ef1",
    scale: "Voice_scale_d1a20ef1",
    rotate: "Voice_rotate_d1a20ef1",
    windowIn: "Voice_windowIn_d1a20ef1",
    fadeOut: "Voice_fadeOut_d1a20ef1",
    fadeIn: "Voice_fadeIn_d1a20ef1",
    wave2: "Voice_wave2_d1a20ef1",
  },
  Gf = R.strings.battle_pass.progression.extraChapterWidget,
  qf = (() => {
    const e = Math.ceil(ds / 800);
    return { duration: 800, iterationCount: e, totalDuration: 800 * e };
  })(),
  Kf = ({ groupName: e }) => {
    const [a, t] = (0, us.useState)(!1),
      s = (0, us.useCallback)(() => {
        a || (ue.sound(R.sounds.play()), ue.sound(e), t(!0));
      }, [a, e]);
    return (
      (0, us.useEffect)(() => {
        a &&
          ct(() => {
            t(!1);
          }, qf.totalDuration);
      }, [a]),
      (0, ms.jsx)(U, {
        body: Gf.voiceoverTooltip(),
        children: (0, ms.jsxs)("div", {
          className: sa(Uf.base, a && Uf.base__animate),
          onClick: s,
          onMouseEnter: () => {
            ue.sound(R.sounds.bp_highlight());
          },
          style: {
            "--animation-duration": `${qf.duration}ms`,
            "--animation-iteration-count": qf.iterationCount,
          },
          children: [
            (0, ms.jsx)("div", { className: sa(Uf.icon, Uf.icon__speaker) }),
            (0, ms.jsx)("div", { className: sa(Uf.icon, Uf.icon__wave0) }),
            (0, ms.jsx)("div", { className: sa(Uf.icon, Uf.icon__wave1) }),
            (0, ms.jsx)("div", { className: sa(Uf.icon, Uf.icon__wave2) }),
          ],
        }),
      })
    );
  },
  Xf = "TankmanDescription_title_6b604eaf",
  Zf = "TankmanDescription_title__noVoice_132efc49",
  Jf = "TankmanDescription_name_9f802b92",
  Qf = "TankmanDescription_skills_8507fe1b",
  Yf = "TankmanDescription_skill_2e650973",
  eg = "TankmanDescription_skill__paidReward_f372df77",
  ag = "TankmanDescription_description_4c6b2a1b",
  tg = "TankmanDescription_lockIcon_7b9909c0",
  sg = "TankmanDescription_lockText_e8d2d84c",
  rg = "TankmanDescription_showCommander_392de842",
  ng = "TankmanDescription_close_b105aa08",
  ig = R.strings.battle_pass.progression.extraChapterWidget,
  og = R.strings.battle_pass.awardsWidget.description.commander(),
  lg = Wt(({ isPaidReward: e }) => {
    const { model: a, controls: t } = of(),
      { tankmenScreenID: s, isBattlePassPurchased: r } = a.root.get(),
      {
        tankman: n,
        hasVoice: i,
        skills: o,
        groupName: l,
      } = a.computes.getFinalRewardTankmanInfo(e),
      { freeFinalRewards: c, paidFinalRewards: d } = a.computes.getFinalRewardsDescription(),
      _ = c.mainReward === rs.tankman && d?.mainReward === rs.tankman;
    return (0, ms.jsxs)(ms.Fragment, {
      children: [
        i && (0, ms.jsx)(Kf, { groupName: l }),
        (0, ms.jsx)("div", { className: sa(Xf, !i && Zf), children: ig.tankman() }),
        (0, ms.jsx)("div", { className: Jf, children: n }),
        o.length > 0 &&
          (0, ms.jsx)("div", {
            className: Qf,
            children: (0, ms.jsx)(Hf, { skills: o, className: sa(Yf, e && eg) }),
          }),
        e &&
          !r &&
          (0, ms.jsx)(me, {
            contentId: R.views.mono.battle_pass.tooltips.lock_icon("resId"),
            children: (0, ms.jsxs)("div", {
              className: ag,
              children: [
                (0, ms.jsx)("div", { className: tg }),
                (0, ms.jsx)("div", { className: sg, children: ig.labelWithBP() }),
              ],
            }),
          }),
        Boolean(s) &&
          !_ &&
          (0, ms.jsx)(U, {
            body: og,
            isEnabled: Boolean(og),
            children: (0, ms.jsx)("div", {
              className: rg,
              children: (0, ms.jsx)(ya, {
                type: Fe.ghost,
                size: va.small,
                mixClass: ng,
                onClick: t.showTankmen,
                children: ig.commanderVoices(),
              }),
            }),
          }),
      ],
    });
  }),
  cg = "Timer_992312dc",
  dg = "Timer_light_b54b0e12",
  _g = "Timer_icon_daefbc5f",
  ug = "Timer_value_ef2605c8",
  mg = ({ expireTime: e = 0 }) => {
    const a = ((e) => {
      const a = (e) => e.toString().padStart(2, "0");
      return `${e.days ? Ha(R.strings.common.duration.days(), { days: e.days }) : ""} ${a(e.hours)} : ${a(e.minutes)} : ${a(e.seconds)}`;
    })(Ke(kt(e, 1)));
    return (0, ms.jsx)(U, {
      body: R.strings.battle_pass.progression.extraChapterWidget.timer(),
      children: (0, ms.jsxs)("div", {
        className: cg,
        children: [
          (0, ms.jsx)("div", { className: _g }),
          (0, ms.jsx)("div", { className: ug, children: a }),
          (0, ms.jsx)("div", { className: dg }),
          (0, ms.jsx)("div", { className: dg }),
        ],
      }),
    });
  },
  pg = "VehicleInfo_f8a1a53e",
  hg = "VehicleInfo_type_f9fe252e",
  bg = ({ vehicleLvl: e, vehicleName: a, vehicleType: t, isElite: s, classNames: r }) =>
    (0, ms.jsxs)("div", {
      className: sa(pg, r?.base),
      children: [
        es(e),
        (0, ms.jsx)("div", {
          className: sa(hg, r?.type),
          style: {
            backgroundImage: `url(${R.images.gui.maps.icons.vehicleTypes.big.$dyn(`${st(t)}${s ? "_elite" : ""}`)})`,
          },
        }),
        a,
      ],
    }),
  fg = {
    vehicleBg: "VehicleDescription_vehicleBg_a5f58731",
    vehicleBg__description: "VehicleDescription_vehicleBg__description_449188e7",
    vehicleCaption: "VehicleDescription_vehicleCaption_ff05b2b9",
    description: "VehicleDescription_description_ac70d89a",
    rewardLabel: "VehicleDescription_rewardLabel_e69780e1",
    rewardDescription: "VehicleDescription_rewardDescription_ac995cfe",
    rewardLockIcon: "VehicleDescription_rewardLockIcon_bf4a508e",
    rewardLockText: "VehicleDescription_rewardLockText_1ae0fc44",
    fadeInWithScale: "VehicleDescription_fadeInWithScale_ae4f1424",
    slideUp: "VehicleDescription_slideUp_ae4f1424",
    blink: "VehicleDescription_blink_ae4f1424",
    scale: "VehicleDescription_scale_ae4f1424",
    rotate: "VehicleDescription_rotate_ae4f1424",
    windowIn: "VehicleDescription_windowIn_ae4f1424",
    fadeOut: "VehicleDescription_fadeOut_ae4f1424",
    fadeIn: "VehicleDescription_fadeIn_ae4f1424",
  },
  gg = R.strings.battle_pass.progression.extraChapterWidget,
  vg = Wt(({ additionalReward: e, isPaidReward: a }) => {
    const {
        model: { vehicleInfo: t, root: s, computes: r },
        controls: n,
      } = of(),
      {
        vehicleType: i,
        isElite: o,
        vehicleName: l,
        vehicleShortName: c,
        vehicleLvl: d,
        vehicleNation: _,
      } = t.get(),
      {
        breakpoint: { weight: u },
      } = Me(),
      { isBattlePassPurchased: m, seasonNum: p } = s.get(),
      h = r.getPaidFinalRewards().length,
      b = { backgroundImage: `url(R.images.gui.maps.icons.flags.c_600x450.${_})` },
      f = u > _e.medium.weight ? 14 : 12,
      g = l.length > f ? c : l,
      v = gg.tank.description.$num(p);
    return (0, ms.jsxs)(ms.Fragment, {
      children: [
        (0, ms.jsx)("div", {
          className: sa(fg.vehicleBg, !h && fg.vehicleBg__description),
          style: b,
        }),
        (0, ms.jsx)(za, { type: "preview", size: "normal", onClick: n.openPreview }),
        (0, ms.jsx)("div", { className: fg.vehicleCaption, children: gg.vehicleCaption() }),
        (0, ms.jsx)(bg, {
          classNames: { base: fg.vehicleInfo },
          vehicleLvl: d,
          vehicleName: g,
          vehicleType: i,
          isElite: o,
        }),
        !h &&
          v &&
          (0, ms.jsx)("div", { className: fg.description, children: (0, ms.jsx)(aa, { text: v }) }),
        e &&
          (0, ms.jsx)("div", {
            className: fg.rewardLabel,
            children: (0, ms.jsx)(vf, { additionalReward: e }),
          }),
        a &&
          !m &&
          (0, ms.jsx)(me, {
            contentId: R.views.mono.battle_pass.tooltips.lock_icon("resId"),
            children: (0, ms.jsxs)("div", {
              className: fg.rewardDescription,
              children: [
                (0, ms.jsx)("div", { className: fg.rewardLockIcon }),
                (0, ms.jsx)("div", { className: fg.rewardLockText, children: gg.labelWithBP() }),
              ],
            }),
          }),
      ],
    });
  }),
  xg = "Separator_da94a3ab",
  wg = "Separator_separatorBg_79e9a0f1",
  Cg = ({ classNames: e }) =>
    (0, ms.jsx)("div", {
      className: sa(xg, e?.base),
      children: (0, ms.jsx)("div", { className: sa(wg, e?.separatorBg) }),
    }),
  yg = "ExtraChapterWidget_3f5dd2c5",
  Sg = "ExtraChapterWidget_widgetWrapper_df1761bd",
  jg = "ExtraChapterWidget_base__freeSingleReward_3f5dd2c5",
  Ig = "ExtraChapterWidget_glow_ea30fd08",
  Ng = "ExtraChapterWidget_content_7571cec7",
  kg = "ExtraChapterWidget_content__left_2a162beb",
  Pg = "ExtraChapterWidget_content__singleReward_d0c77a05",
  Rg = "ExtraChapterWidget_separatorBg_58fe9583",
  Bg = "ExtraChapterWidget_timer_92648812",
  Ag = [rs.style, rs.attachmentsSet],
  Eg = { [rs.tankman]: lg, [rs.vehicle]: vg, [rs.style]: Tf, [rs.attachmentsSet]: _f },
  Tg = ({ mainReward: e, additionalReward: a }, t) => {
    if (!e) return null;
    const s = Eg[e];
    return s
      ? (0, ms.jsx)(s, { additionalReward: a, ...t })
      : (console.warn("Unknown final reward type:", e), null);
  },
  Lg = Wt(() => {
    const {
        model: { root: e, computes: a },
      } = of(),
      { timeLeft: t } = e.get(),
      { freeFinalRewards: s, paidFinalRewards: r } = a.getFinalRewardsDescription(),
      n = a.regularBattlePass(),
      i = !r && Ag.includes(s.mainReward ?? "");
    return (0, ms.jsxs)("div", {
      className: sa(yg, i && jg),
      children: [
        (0, ms.jsxs)("div", {
          className: Sg,
          children: [
            (0, ms.jsx)("div", { className: Ig }),
            (0, ms.jsx)("div", {
              className: sa(Ng, !r && Pg),
              children: Tg(s, { isPaidReward: !1 }),
            }),
            r &&
              (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsx)(Cg, { classNames: { separatorBg: Rg } }),
                  (0, ms.jsx)("div", {
                    className: sa(Ng, kg),
                    children: Tg(r, { isPaidReward: !0 }),
                  }),
                ],
              }),
          ],
        }),
        !n && (0, ms.jsx)("div", { className: Bg, children: (0, ms.jsx)(mg, { expireTime: t }) }),
      ],
    });
  }),
  Og = {
    base: "Footer_ab6b29ea",
    light: "Footer_light_3b6e1ce3",
    light__red: "Footer_light__red_944d6c45",
    light__green: "Footer_light__green_9e6310c0",
    buttonWrapper: "Footer_buttonWrapper_bdb4b046",
    starterAndButton: "Footer_starterAndButton_2f4854e4",
    button: "Footer_button_9e575f35",
    labelContainer: "Footer_labelContainer_ae5572d4",
    label: "Footer_label_e76dc882",
    label__buy: "Footer_label__buy_8b13ea86",
    days: "Footer_days_9ed2f711",
    points: "Footer_points_58964618",
    status: "Footer_status_9143122e",
    info: "Footer_info_5836cdb1",
    infoHover: "Footer_infoHover_63796a67",
    blink: "Footer_blink_106ec98e",
    move: "Footer_move_4308958a",
    fadeInWithScale: "Footer_fadeInWithScale_4308958a",
    slideUp: "Footer_slideUp_4308958a",
    scale: "Footer_scale_4308958a",
    rotate: "Footer_rotate_4308958a",
    windowIn: "Footer_windowIn_4308958a",
    fadeOut: "Footer_fadeOut_4308958a",
    fadeIn: "Footer_fadeIn_4308958a",
  },
  Dg = Qa.resolve("strings"),
  Wg = (e, a) =>
    e
      ? a
        ? Dg.readOrEmpty("battle_pass.progression.activatePausedExtraChapterDescr")
        : Dg.readOrEmpty("battle_pass.progression.activateExtraChapterDescr")
      : Dg.readOrEmpty("battle_pass.progression.activateChapterDescr"),
  Vg = Wt(() => {
    const { model: e, controls: a } = of(),
      t = m(),
      {
        actionType: s,
        chapterType: r,
        hasExtra: n,
        isSeasonEndingSoon: i,
        freePointsInChapter: o,
        currentPointsInChapter: l,
        chapterState: c,
        timeLeft: d,
        chapterID: _,
        isStarterPack: u,
      } = e.root.get(),
      p = r === Qb.EXTRA,
      h = r === Qb.HOLIDAY,
      b = c === Zb.Paused,
      f = o - l,
      g = s === Jb.ActivateChapter && f > 0,
      v = s !== Jb.ActivateChapter && i,
      x = u
        ? Dg.readOrEmpty("battle_pass.progression.battlePassBuyDescrStarterPack")
        : h
          ? Dg.readOrEmpty("battle_pass.progression.battlePassBuyHolidayDescr")
          : Dg.readOrEmpty("battle_pass.progression.battlePassBuyDescr"),
      {
        buyBtnLabel: w,
        tooltip: C,
        label: y,
        warning: S,
        buttonType: j,
        lightColor: I,
        route: N,
        params: k,
      } = ((e) => {
        switch (e) {
          case Jb.Buy:
            return {
              buyBtnLabel: Dg.readOrEmpty("battle_pass.progression.battlePassBuyBtn"),
              tooltip: Dg.readOrEmpty("battle_pass.tooltips.footerBuyBtn.battlePass.descr"),
              label: x,
              warning: Dg.readOrEmpty("battle_pass.progression.seasonEndingDescr"),
              buttonType: Fe.main,
              lightColor: "red",
              route: ls.battlePass.buyPass,
              params: { chapterID: _ },
            };
          case Jb.BuyLevel:
            return {
              buyBtnLabel: Dg.readOrEmpty("battle_pass.progression.episodeBuyBtn"),
              tooltip: h
                ? Dg.readOrEmpty("battle_pass.tooltips.footerBuyBtn.episode.holidayDescr")
                : Dg.readOrEmpty("battle_pass.tooltips.footerBuyBtn.episode.descr"),
              label: Dg.readOrEmpty("battle_pass.progression.episodeBuyDescr"),
              warning: Dg.readOrEmpty("battle_pass.progression.seasonEndingDescr"),
              buttonType: Fe.main,
              lightColor: "",
              route: ls.battlePass.buyLevels,
              params: { chapterID: _ },
            };
          case Jb.ActivateChapter:
            return {
              buyBtnLabel: Dg.readOrEmpty("battle_pass.progression.activateChapter"),
              tooltip: Dg.readOrEmpty("battle_pass.tooltips.footerBuyBtn.activateChapter.descr"),
              label: Wg(p, b),
              warning: Dg.readOrEmpty("battle_pass.progression.freePointsDescr"),
              buttonType: Fe.primary,
              lightColor: "green",
              route: "",
              params: {},
            };
          default:
            return {
              buyBtnLabel: "",
              tooltip: "",
              label: "",
              warning: "",
              buttonType: Fe.ghost,
              lightColor: "green",
              route: "",
              params: {},
            };
        }
      })(s),
      P = g || v ? S : y,
      R = ((e) => {
        const a = Ke(e);
        switch (!0) {
          case a.days >= 1:
            return (0, ms.jsx)(aa, {
              text: Dg.readOrEmpty("battle_pass.status.timeLeft.days"),
              binding: { day: a.days },
            });
          case a.hours >= 1:
            return (0, ms.jsx)(aa, {
              text: Dg.readOrEmpty("battle_pass.status.timeLeft.hours"),
              binding: { hour: a.hours },
            });
          case a.minutes >= 1:
            return (0, ms.jsx)(aa, {
              text: Dg.readOrEmpty("battle_pass.status.timeLeft.min"),
              binding: { min: a.minutes },
            });
          default:
            return Dg.readOrEmpty("battle_pass.status.timeLeft.lessMin");
        }
      })(d),
      B = e.computes.getStarterPackRewards(),
      A = () => {
        s === Jb.ActivateChapter
          ? a.chapterActivate()
          : N && t.push(N, { chapterID: k.chapterID || void 0, reset: k.reset });
      };
    return (0, ms.jsxs)("div", {
      className: Og.base,
      children: [
        !u &&
          (0, ms.jsxs)(ms.Fragment, {
            children: [
              (0, ms.jsx)("div", { className: sa(Og.light, Og[`light__${I}`]) }),
              (0, ms.jsxs)("div", {
                className: Og.labelContainer,
                children: [
                  b &&
                    (0, ms.jsx)("div", {
                      className: Og.status,
                      children: Dg.readOrEmpty("battle_pass.progression.footer.status.paused"),
                    }),
                  (0, ms.jsx)("div", { className: Og.label, children: P }),
                  v && (0, ms.jsx)("div", { className: Og.days, children: R }),
                  g &&
                    (0, ms.jsxs)(ms.Fragment, {
                      children: [
                        (0, ms.jsx)("div", { className: Og.points, children: f }),
                        (0, ms.jsx)("div", {
                          className: Og.info,
                          children: (0, ms.jsx)(U, {
                            header: Dg.readOrEmpty(
                              "battle_pass.tooltips.progression.freePoints.header",
                            ),
                            body: n
                              ? Dg.readOrEmpty(
                                  "battle_pass.tooltips.progression.freePoints.bodyExceptExtra",
                                )
                              : Dg.readOrEmpty("battle_pass.tooltips.progression.freePoints.body"),
                            children: (0, ms.jsx)("div", { className: Og.infoHover }),
                          }),
                        }),
                      ],
                    }),
                ],
              }),
            ],
          }),
        (0, ms.jsx)("div", {
          className: Og.buttonWrapper,
          children: u
            ? (0, ms.jsxs)("div", {
                className: Og.starterAndButton,
                "data-test-id": `${s}ButtonWithSeasonData`,
                children: [
                  (0, ms.jsxs)(ms.Fragment, {
                    children: [
                      (0, ms.jsx)("div", {
                        className: sa(Og.label, Og.label__buy),
                        children: (0, ms.jsx)(aa, { text: P }),
                      }),
                      v && (0, ms.jsx)("div", { className: Og.days, children: R }),
                    ],
                  }),
                  (0, ms.jsx)(U, {
                    body: C,
                    children: (0, ms.jsxs)(ya, {
                      type: j,
                      size: va.medium,
                      mixClass: Og.button,
                      onClick: A,
                      children: [v && (0, ms.jsx)("div", { className: Og.blink }), w],
                    }),
                  }),
                  (0, ms.jsx)(ei, { starterPackRewards: B, presentSize: Qn, rewardSize: ra.Small }),
                ],
              })
            : (0, ms.jsx)(U, {
                body: C,
                children: (0, ms.jsxs)(ya, {
                  type: j,
                  size: va.medium,
                  mixClass: Og.button,
                  onClick: A,
                  children: [v && (0, ms.jsx)("div", { className: Og.blink }), w],
                }),
              }),
        }),
      ],
    });
  }),
  Mg = "Header_d6c7a62a",
  zg = "Header_labels_73a63da7",
  $g = "Header_title_46bb5059",
  Fg = "Header_chapterWrapper_ec40e5cf",
  Hg = "Header_chapterText_b2d85aee",
  Ug = "Header_titleText_593dd9b2",
  Gg = "Header_chapterStatus_9c15353a",
  qg = "Header_date_dc70e297",
  Kg = "Header_titleButtons_7521b3e5",
  Xg = "Header_titleButton_d86731f6",
  Zg = "Header_logo_46c0cb85",
  Jg = "Header_awards_f810fc3a",
  Qg = "Header_emblem_c890a2dc",
  Yg = "Header_emblem__isChapterNotChosen_8aa33950",
  ev = R.strings.battle_pass,
  av = Wt(() => {
    const { controls: e, model: a } = of(),
      {
        chapterID: t,
        chapterState: r,
        seasonNum: n,
        expireTime: i,
        isBattlePassPurchased: o,
        timeLeft: l,
        chapterType: c,
      } = a.root.get(),
      d = [Zb.NotStarted, Zb.Paused],
      _ =
        (u = r) === Zb.Paused
          ? ev.progression.header.paused()
          : u === Zb.NotStarted
            ? ev.progression.header.inactive()
            : void 0;
    var u;
    const m = c === Qb.EXTRA,
      p = c === Qb.HOLIDAY,
      h = Math.trunc(l / 86400),
      b = String(ev.chapter.fullName.$num(t)),
      f = z(ev.progression.seasonEndingTooltip(), { day: h }),
      g = z(ev.progression.header.chapter.status(), { chapterName: b }),
      v = at(
        { iconSize: an, shieldSize: qr, containerSize: zr },
        { medium: { iconSize: sn, shieldSize: Kr, containerSize: $r } },
      ),
      x = H;
    return (0, ms.jsxs)("div", {
      className: Mg,
      children: [
        (0, ms.jsx)("div", {
          className: Zg,
          children: (0, ms.jsx)("div", {
            className: sa(Qg, d.includes(r) && Yg),
            children: (0, ms.jsx)(_n, {
              iconSize: v.iconSize,
              shieldSize: v.shieldSize,
              containerSize: v.containerSize,
              bpPurchased: o,
              chapterID: t,
              className: Qg,
            }),
          }),
        }),
        (0, ms.jsx)("div", {
          className: zg,
          children: (0, ms.jsxs)("div", {
            className: $g,
            children: [
              (0, ms.jsx)(U, {
                body: f,
                isEnabled: Boolean(l),
                children: (0, ms.jsx)("div", {
                  className: qg,
                  children: m
                    ? (0, ms.jsx)(aa, {
                        text: ev.progression.season.end.special(),
                        binding: { endTime: s(i, ha.DayMonthFull) },
                      })
                    : p
                      ? (0, ms.jsx)(aa, {
                          text: ev.progression.season.end.special(),
                          binding: { endTime: s(i, ha.DayMonthFullTime) },
                        })
                      : (0, ms.jsx)(aa, {
                          text: ev.progression.season.end.normal(),
                          binding: {
                            seasonNum: es(n),
                            seasonName: String(ev.season.fullName.$num(n)),
                            endDate: s(i, ha.DayMonthFull),
                          },
                        }),
                }),
              }),
              (0, ms.jsxs)("div", {
                className: Fg,
                children: [
                  (0, ms.jsx)("div", {
                    className: Ug,
                    children: (0, ms.jsx)(x, {
                      className: Hg,
                      text: b,
                      tooltipParams: { body: g },
                    }),
                  }),
                  _ && (0, ms.jsx)("div", { className: Gg, children: _ }),
                ],
              }),
              (0, ms.jsxs)("div", {
                className: Kg,
                children: [
                  (0, ms.jsx)("div", {
                    className: Xg,
                    children: (0, ms.jsx)(qa, {
                      caption: m || p ? ev.progression.aboutExtra() : ev.progression.about(),
                      type: "info",
                      onClick: e.openAbout,
                    }),
                  }),
                  (0, ms.jsx)("div", {
                    className: Xg,
                    children: (0, ms.jsx)(qa, {
                      caption: ev.progression.howToEarnPoints.title(),
                      type: "info",
                      onClick: e.openInfo,
                    }),
                  }),
                ],
              }),
            ],
          }),
        }),
        (0, ms.jsx)("div", {
          className: Jg,
          children: (0, ms.jsx)(Wm, {
            rootId: R.aliases.battle_pass.Progression("resId"),
            context: "model.awardsWidget",
          }),
        }),
      ],
    });
  }),
  tv = (function (e) {
    return ((e.Dragging = "dragging"), (e.End = "scrollingToEnd"), (e.Idle = "idle"), e);
  })({}),
  sv = { type: "idle" },
  rv = (function (e) {
    return (
      (e[(e.MainButton = 0)] = "MainButton"),
      (e[(e.AuxiliaryButton = 1)] = "AuxiliaryButton"),
      (e[(e.SecondaryButton = 2)] = "SecondaryButton"),
      (e[(e.FourthButton = 3)] = "FourthButton"),
      (e[(e.FifthButton = 4)] = "FifthButton"),
      e
    );
  })({});
var nv = {
    base: "ArrowButton_bae005da",
    base__gray: "ArrowButton_base__gray_2872d83c",
    icon: "ArrowButton_icon_78679b8c",
    icon__4k: "ArrowButton_icon__4k_2f0ad49a",
    icon__back: "ArrowButton_icon__back_20344757",
    icon__forward: "ArrowButton_icon__forward_3467f80",
    fadeInWithScale: "ArrowButton_fadeInWithScale_5327085d",
    slideUp: "ArrowButton_slideUp_5327085d",
    blink: "ArrowButton_blink_5327085d",
    scale: "ArrowButton_scale_5327085d",
    rotate: "ArrowButton_rotate_5327085d",
    windowIn: "ArrowButton_windowIn_5327085d",
    fadeOut: "ArrowButton_fadeOut_5327085d",
    fadeIn: "ArrowButton_fadeIn_5327085d",
  },
  iv = ({ onClick: e, direction: a, type: t = sf.Default, className: s, tooltipBody: r }) => {
    const n = (0, us.useCallback)(() => {
        ue.sound(R.sounds.highlight());
      }, []),
      i = (0, us.useCallback)(() => {
        (ue.sound(R.sounds.bp_slide()), e());
      }, [e]);
    return (0, ms.jsx)(U, {
      body: r,
      children: (0, ms.jsx)("div", {
        className: sa(nv.base, nv[`base__${t}`], s),
        onClick: i,
        onMouseEnter: n,
        children: (0, ms.jsx)("div", {
          className: sa(nv.icon, nv[`icon__${a}`], 2 === tt() && nv.icon__4k),
        }),
      }),
    });
  },
  ov = "Bookmark_1a260409",
  lv = "Bookmark_container_5cba29f3",
  cv = "Bookmark_container__start_f008a523",
  dv = "Bookmark_container__wide_16a4de6e",
  _v = "Bookmark_textWrapper_985290f6",
  uv = "Bookmark_withTooltip_ef0470d4",
  mv = "Bookmark_text_7877afbc",
  pv = "Bookmark_text__basic_9271b9b6",
  hv = "Bookmark_text__premium_49218d9e",
  bv = "Bookmark_text__single_8125f23e",
  fv = "Bookmark_text__wide_3f764b56",
  gv = "Bookmark_text__disappeared_68a02d91",
  vv = "Bookmark_textInner_8a053178",
  xv = "Bookmark_leftTextLine_efb7ffd5",
  wv = "Bookmark_rightTextLine_c747efe3",
  Cv = ({ isWide: e, isDecorated: a }) =>
    (0, ms.jsxs)("div", {
      className: sa(mv, bv, e && fv),
      children: [
        a && (0, ms.jsx)("div", { className: xv }),
        (0, ms.jsx)("div", {
          className: vv,
          children: R.strings.battle_pass.progression.postProgressionDescr(),
        }),
        a && (0, ms.jsx)("div", { className: wv }),
      ],
    }),
  yv = (0, us.forwardRef)(
    (
      {
        isWide: e = !1,
        isDisappeared: a = !1,
        tooltipBody: t,
        tooltipTitle: s,
        chapterStep: r,
        mixClass: n,
      },
      i,
    ) => {
      const o = (0, us.useRef)(null);
      (0, us.useImperativeHandle)(i, () => ({
        width: () => {
          const e = o.current;
          if (e) {
            const a = window.getComputedStyle(e, null).getPropertyValue("width");
            return Number(a.split("rem")[0]);
          }
          return 0;
        },
      }));
      const l = (0, ms.jsx)(aa, {
        text: R.strings.battle_pass.tooltips.postProgress.body(),
        binding: { chapterStep: r },
      });
      return (0, ms.jsx)("div", {
        className: sa(ov, n),
        ref: o,
        children: (0, ms.jsx)("div", {
          className: sa(lv, e && dv, !e && cv),
          children: e
            ? (0, ms.jsx)(U, {
                body: t,
                header: s,
                isEnabled: "string" == typeof t,
                children: (0, ms.jsx)("div", {
                  className: uv,
                  children: (0, ms.jsx)(Cv, { isWide: e, isDecorated: !0 }),
                }),
              })
            : (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsx)("div", {
                    className: _v,
                    children: (0, ms.jsx)(U, {
                      header: R.strings.battle_pass.tooltips.postProgress.header(),
                      body: l,
                      children: (0, ms.jsx)(Cv, { isWide: e }),
                    }),
                  }),
                  (0, ms.jsx)(me, {
                    contentId: R.views.mono.battle_pass.tooltips.lock_icon("resId"),
                    children: (0, ms.jsx)("div", {
                      className: sa(mv, hv),
                      children: R.strings.battle_pass.progression.premiumProgressionDescr(),
                    }),
                  }),
                  (0, ms.jsx)("div", {
                    className: sa(mv, pv, a && gv),
                    children: R.strings.battle_pass.progression.baseProgressionDescr(),
                  }),
                ],
              }),
        }),
      });
    },
  ),
  Sv = "LoupeButton_d966f396",
  jv = "LoupeButton_icon_bfb9d784",
  Iv = "LoupeButton_iconHover_22ab079c",
  Nv = "LoupeButton_hoverArea_fa5a9428",
  kv = ({ onClick: e, hoverAreaClasses: a }) => {
    const t = (0, us.useCallback)(() => ue.sound(R.sounds.highlight()), []),
      s = (0, us.useCallback)(() => {
        (ue.sound(R.sounds.play()), e());
      }, [e]),
      r = sa(Nv, a);
    return (0, ms.jsxs)("div", {
      className: Sv,
      onClick: s,
      onMouseEnter: t,
      children: [
        (0, ms.jsx)("div", { className: jv }),
        (0, ms.jsx)("div", { className: Iv }),
        a && (0, ms.jsx)("div", { className: r }),
      ],
    });
  },
  Pv = "VehicleInfo_c9c556fb",
  Rv = "VehicleInfo_prefix_da97ceb4",
  Bv = "VehicleInfo_type_514b50be",
  Av = R.strings.battle_pass.progression.widget3dStyle,
  Ev = (0, us.memo)(({ vehicleLvl: e, vehicleName: a, vehicleType: t, isElite: s }) => {
    const r = (0, us.useMemo)(() => {
      const e = st(t);
      return {
        backgroundImage: `url(${R.images.gui.maps.icons.vehicleTypes.big.$dyn(`${e}${s ? "_elite" : ""}`)})`,
      };
    }, [t, s]);
    return (0, ms.jsxs)("div", {
      className: Pv,
      children: [
        (0, ms.jsx)("div", { className: Rv, children: Av.forVehicle() }),
        es(e),
        (0, ms.jsx)("div", { className: Bv, style: r }),
        a,
      ],
    });
  }),
  Tv = "Widget3dStyle_a34c3929",
  Lv = "Widget3dStyle_title_d5bd52fc",
  Ov = "Widget3dStyle_base__closedChapter_9577883c",
  Dv = "Widget3dStyle_box_7d47e858",
  Wv = "Widget3dStyle_light_afd0e007",
  Vv = "Widget3dStyle_image_37b4439c",
  Mv = "Widget3dStyle_previewButton_42e4e473",
  zv = "Widget3dStyle_box__hovered_9577883c",
  $v = "Widget3dStyle_footer_ff3bf09e",
  Fv = "Widget3dStyle_caption_cc553073",
  Hv = R.strings.battle_pass.progression.widget3dStyle,
  Uv = Wt(({ widget3dStyleRef: e, level: a, isShowTitle: t }) => {
    const [s, r] = (0, us.useState)(!1),
      { controls: n, model: i } = of(),
      { chapterState: o, isStyleTaken: l } = i.root.get(),
      { styleName: c, styleId: d } = i.widget3dStyle.get(),
      {
        breakpoint: { weight: _ },
      } = Me(),
      u = as(
        a,
        d,
        ((e, a) => (2 !== a ? (e <= _e.small.weight ? "_small" : "_medium") : ""))(
          _,
          viewEnv.getScale(),
        ),
      ),
      m = (0, ms.jsx)(aa, { text: Hv.currentStyle(), binding: { name: c } }),
      p = (0, us.useCallback)(() => {
        n.open3dStylePreview(a);
      }, [n, a]);
    return (0, ms.jsxs)("div", {
      className: sa(Tv, o === Zb.Completed && Ov),
      ref: e,
      children: [
        !l && t && (0, ms.jsx)("div", { className: Lv, children: Hv.titleNoChapterSelected() }),
        (0, ms.jsxs)("div", {
          className: sa(Dv, s && zv),
          onMouseEnter: () => r(!0),
          onMouseLeave: () => r(!1),
          children: [
            !l && 1 === a && (0, ms.jsx)("div", { className: Wv }),
            (0, ms.jsx)("div", { className: Vv, style: u }),
            (0, ms.jsx)("div", { className: Mv, children: (0, ms.jsx)(kv, { onClick: p }) }),
          ],
        }),
        (0, ms.jsxs)("div", {
          className: $v,
          children: [
            (0, ms.jsx)("div", { className: Fv, children: m }),
            (0, ms.jsx)(Ev, { ...i.widget3dStyleVehicleInfo.get() }),
          ],
        }),
      ],
    });
  }),
  Gv = ({
    level: e,
    levelWidth: a,
    currentLevelWidth: t,
    pointsInLevel: s,
    totalPointsInLevel: r,
    currentLevel: n,
  }) => (e > n ? t + a * (e - 2) + a * (s / r) : (e - 1) * a + t * (s / r)),
  qv = (e) => e + 1,
  Kv = Wt(
    ({
      api: e,
      progressChange: a,
      levelWidth: t,
      currentLevelWidth: s,
      level: r,
      previousLevel: n,
      currentPointsInLevel: i,
      previousPointsInLevel: o,
      currentPointsInChapter: l,
      previousPointsInChapter: c,
      theme: d,
    }) => {
      const { model: _ } = of(),
        { isPaused: u, showLevelsAnimations: m, currentLevel: p } = _.root.get(),
        h = _.levels.get(),
        [b, f] = (0, us.useState)(0),
        g = (0, us.useRef)(-1),
        [{ previousBaseEarnedPoints: v, maxBasePoints: w, baseProgressionSize: C }, y] = (0,
        us.useState)({ previousBaseEarnedPoints: 0, maxBasePoints: 0, baseProgressionSize: 0 });
      (0, us.useEffect)(() => {
        if (u) return;
        const e = g.current !== c,
          a = e ? n : r,
          d = s + (h.length - 1) * t,
          _ = x(h, a - 1),
          m = r <= h.length ? r - 1 : h.length - 1,
          b = x(h, m)?.levelPoints;
        if (!b) return;
        const f = Gv({
            level: r,
            levelWidth: t,
            currentLevelWidth: s,
            pointsInLevel: i,
            totalPointsInLevel: b,
            currentLevel: p,
          }),
          v = _ ? _.levelPoints : 0,
          w = Gv({
            level: a > r ? r : a,
            levelWidth: t,
            currentLevelWidth: a < p ? t : s,
            pointsInLevel: o,
            totalPointsInLevel: v,
            currentLevel: p,
          }),
          C = e && a <= r ? w : f;
        (c !== l && t && (g.current = c),
          y({ maxBasePoints: d, previousBaseEarnedPoints: C, baseProgressionSize: f }));
      }, [u, t, s, r, n, l, o, i, c, p, h]);
      const S = (0, us.useMemo)(
        () => ({
          ...pt,
          withStack: !0,
          type: Ja.Simple,
          delta: { duration: 400, delay: 300 },
          line: { duration: 400, delay: 300 },
        }),
        [],
      );
      return (
        (0, us.useEffect)(() => {
          const e = p !== n || i !== o;
          if (!m && (e || l === c))
            return e && -1 === g.current
              ? ct(() => {
                  f(qv);
                }, 700)
              : void 0;
          f(qv);
        }, [l, c, m]),
        (0, us.useEffect)(() => {
          if (m)
            return na(() => {
              a && a();
            });
        }, [a, m]),
        (0, ms.jsx)(
          ot,
          { animationSettings: S, deltaFrom: v, value: C, maxValue: w || void 0, api: e, theme: d },
          b,
        )
      );
    },
  ),
  Xv = {
    base: "Progression_1b76c395",
    base__isLayoutWithExtraWidget: "Progression_base__isLayoutWithExtraWidget_61efd8f5",
    scrollWrapper: "Progression_scrollWrapper_5d6c50f7",
    wrapper: "Progression_wrapper_2d700f2",
    section__last: "Progression_section__last_36865a6",
    divider: "Progression_divider_875ac4ce",
    dividerContent: "Progression_dividerContent_32563f87",
    dividerText: "Progression_dividerText_9f28ff3a",
    progressContainer: "Progression_progressContainer_bf13204b",
    progress: "Progression_progress_f2c8d04a",
    progress__inactive: "Progression_progress__inactive_884002f1",
    progressBackground: "Progression_progressBackground_58b1a303",
    progressBackground__disabled: "Progression_progressBackground__disabled_bbabdc5",
    progressBackground__finished: "Progression_progressBackground__finished_335b0244",
    decor: "Progression_decor_158cf9e5",
    decorBackground: "Progression_decorBackground_da5971de",
    decor__left: "Progression_decor__left_61efd8f5",
    row: "Progression_row_2b2744bc",
    row__basic: "Progression_row__basic_db90f79e",
    bookmark: "Progression_bookmark_adda18c9",
    bookmark__start: "Progression_bookmark__start_e45cdc98",
    bookmarkLeftFixed: "Progression_bookmarkLeftFixed_87985cd2",
    bookmarkLeftFixed__active: "Progression_bookmarkLeftFixed__active_3d829e66",
    bookmarkLeftResponsive: "Progression_bookmarkLeftResponsive_f380dd1b",
    bookmarkBackground: "Progression_bookmarkBackground_3695986",
    scrollToButton: "Progression_scrollToButton_b51d1a4f",
    scrollToButton__visible: "Progression_scrollToButton__visible_750807fe",
    scrollToButton__forward: "Progression_scrollToButton__forward_f3d60cf3",
    scrollToButton__backward: "Progression_scrollToButton__backward_d30703b1",
    arrowButton: "Progression_arrowButton_fe2d3e38",
    progressionToButton: "Progression_progressionToButton_277ce88b",
    progressionToButton__hidden: "Progression_progressionToButton__hidden_43581710",
    progressionToButton__back: "Progression_progressionToButton__back_defa3226",
    progressionToButton__forward: "Progression_progressionToButton__forward_d0ad294b",
    shadow: "Progression_shadow_aeeafbe",
    shadow__left: "Progression_shadow__left_7a5e7f90",
    shadow__right: "Progression_shadow__right_b09b06b4",
    additionalShadow: "Progression_additionalShadow_19983a68",
    additionalShadow__active: "Progression_additionalShadow__active_3d829e66",
    scrollBarPosition: "Progression_scrollBarPosition_31bb147f",
    fadeInWithScale: "Progression_fadeInWithScale_61efd8f5",
    slideUp: "Progression_slideUp_61efd8f5",
    blink: "Progression_blink_61efd8f5",
    scale: "Progression_scale_61efd8f5",
    rotate: "Progression_rotate_61efd8f5",
    windowIn: "Progression_windowIn_61efd8f5",
    fadeOut: "Progression_fadeOut_61efd8f5",
    fadeIn: "Progression_fadeIn_61efd8f5",
  },
  Zv = R.strings.battle_pass.tooltips.progression.freePoints,
  Jv = Wt(
    ({
      progressApi: e,
      freePointsApi: a,
      levelWidth: t,
      currentLevelWidth: s,
      progressChange: r,
    }) => {
      const { model: n } = of(),
        {
          chapterState: i,
          currentLevel: o,
          previousLevel: l,
          currentPointsInLevel: c,
          previousPointsInLevel: d,
          currentPointsInChapter: _,
          previousPointsInChapter: u,
          freePointsInLevel: m,
          freePointsInChapter: p,
          previousFreePointsInChapter: h,
          previousFreePointsInLevel: b,
          potentialLevel: f,
          previousPotentialLevel: g,
        } = n.root.get(),
        v = n.levels.get(),
        x = Ta(),
        w = (i === Zb.NotStarted || i === Zb.Paused) && p - _ > 0,
        C = n.computes.getTotalLevelPoints();
      if (!C) return;
      const y = n.computes.getCurrentWidth(t, s, x, C),
        S = _ >= v.length * C,
        j = {
          "--progress-line-base": pa.line.bgColorBase,
          "--progress-line-disabled": pa.line.bgColorDisabled,
          "--progress-line-finished": pa.line.bgColorFinished,
        };
      return (0, ms.jsxs)("div", {
        className: Xv.progressContainer,
        children: [
          w &&
            (0, ms.jsx)(U, {
              header: Zv.header(),
              body: Zv.body(),
              children: (0, ms.jsx)("div", {
                className: Xv.progress,
                children: (0, ms.jsx)(Kv, {
                  api: a,
                  progressChange: r,
                  levelWidth: t,
                  currentLevelWidth: s,
                  level: f,
                  previousLevel: g,
                  currentPointsInLevel: m,
                  previousPointsInLevel: b,
                  currentPointsInChapter: p,
                  previousPointsInChapter: h,
                  theme: oa,
                }),
              }),
            }),
          (0, ms.jsx)("div", {
            className: sa(Xv.progressBackground, S && Xv.progressBackground__finished),
            style: { width: `${y}rem`, ...j },
          }),
          (0, ms.jsx)(me, {
            contentId: R.views.mono.battle_pass.tooltips.bp_points("resId"),
            children: (0, ms.jsx)("div", {
              className: sa(Xv.progress, w && Xv.progress__inactive),
              children: (0, ms.jsx)(Kv, {
                api: e,
                levelWidth: t,
                currentLevelWidth: s,
                level: o,
                previousLevel: l,
                currentPointsInLevel: c,
                previousPointsInLevel: d,
                currentPointsInChapter: _,
                previousPointsInChapter: u,
                progressChange: r,
              }),
            }),
          }),
        ],
      });
    },
  ),
  Qv = "Background_3985f66b",
  Yv = "Background_default_6d3ad0aa",
  ex = "Background_base__premium_26effab7",
  ax = "Background_rare_927afb2",
  tx = "Background_rareBg_af0bac1",
  sx = "Background_pattern_f3c44da",
  rx = "Background_pattern__left_910cb7b6",
  nx = "Background_pattern__right_9077c0df",
  ix = "Background_pattern__leftIndent_508a3857",
  ox = "Background_pattern__rightIndent_db46b63f",
  lx = "Background_pattern__completed_51752ce4",
  cx = "Background_disabled_12f45c1c",
  dx = "Background_inProgress_f241145e",
  _x = "Background_inProgressInner_eca44a42",
  ux = "Background_inProgressPart_886e2046",
  mx = "Background_inProgressPart__left_6b695373",
  px = "Background_inProgressPart__right_cb03c83d",
  hx = (e) => `url(R.images.gui.maps.icons.battlePass.progression.pattern_rare_${e})`,
  bx = Wt(({ level: e, isPremium: a = !1 }) => {
    const { model: t } = of(),
      { cardStatus: s, isRare: r, isDisabled: n } = t.computes.cardStates(e, a),
      i =
        s.current !== ef.IN_PROGRESS &&
        ((e, a) => {
          switch (e) {
            case ef.NOT_STARTED:
              return a;
            case ef.COMPLETED:
              return !a;
            default:
              return (console.warn(`Unsupported status for isIndent: ${e}`), !1);
          }
        })(s.current, a);
    return (0, ms.jsxs)("div", {
      className: sa(Qv, a && ex),
      children: [
        (0, ms.jsx)("div", { className: Yv }),
        n && (0, ms.jsx)("div", { className: cx }),
        s.current === ef.IN_PROGRESS &&
          (0, ms.jsxs)("div", {
            className: dx,
            children: [
              (0, ms.jsx)("div", { className: sa(ux, mx) }),
              !a && (0, ms.jsx)("div", { className: _x }),
              (0, ms.jsx)("div", { className: sa(ux, px) }),
            ],
          }),
        r &&
          (0, ms.jsxs)("div", {
            className: ax,
            children: [
              (0, ms.jsx)("div", {
                className: sa(sx, rx, i && ix, s.current === ef.COMPLETED && lx),
                style: { backgroundImage: hx("left") },
              }),
              (0, ms.jsx)("div", {
                className: sa(sx, nx, !i && ox, s.current === ef.COMPLETED && lx),
                style: { backgroundImage: hx("right") },
              }),
              s.current === ef.NOT_STARTED && (0, ms.jsx)("div", { className: tx }),
            ],
          }),
      ],
    });
  }),
  fx = {
    base: "Stage_7c79af8a",
    base__rewardTaken: "Stage_base__rewardTaken_a669b795",
    number: "Stage_number_1d4a1a4c",
    animatedNumber: "Stage_animatedNumber_3b1e34e9",
    numberInProgress: "Stage_numberInProgress_d91be11d",
    title: "Stage_title_a5ffe511",
    glow: "Stage_glow_cc400fdf",
    base__inProgress: "Stage_base__inProgress_68142ff2",
    animatedGlow: "Stage_animatedGlow_4243426d",
    iconFinal: "Stage_iconFinal_b5e7d2e",
    fadeInWithScale: "Stage_fadeInWithScale_68142ff2",
    slideUp: "Stage_slideUp_68142ff2",
    blink: "Stage_blink_68142ff2",
    scale: "Stage_scale_68142ff2",
    rotate: "Stage_rotate_68142ff2",
    windowIn: "Stage_windowIn_68142ff2",
    fadeOut: "Stage_fadeOut_68142ff2",
    fadeIn: "Stage_fadeIn_68142ff2",
  },
  gx = R.strings.battle_pass.progression,
  vx = Wt(({ stepNumber: e, stageAnimationDelay: a, isRewardAnimationActive: t }) => {
    const { model: s, controls: r } = of(),
      { chapterState: n, showLevelsAnimations: o } = s.root.get(),
      [l, c] = (0, us.useState)(!1),
      { cardStatus: d } = s.computes.cardStates(e, !1),
      _ = s.computes.isRewardNeedTake(e, !1) || s.computes.isRewardNeedTake(e, !0),
      u = s.computes.levelInfo(e).maxLevel === e,
      m = d.current === ef.IN_PROGRESS,
      p = n === Zb.NotStarted || n === Zb.Paused,
      h = d.current === ef.COMPLETED && !_ && !t,
      { stageOpacity: b } = Ra({
        from: { stageOpacity: l ? 1 : 0 },
        to: { stageOpacity: 0 },
        delay: 0,
        onStart: () => ue.sound(R.sounds.bp_current_phase()),
        config: { duration: 750, easing: ss },
      }),
      { sparkOpacity: f } = Ra({
        from: { sparkOpacity: l ? 1 : 0 },
        to: { sparkOpacity: 0 },
        delay: 1100,
        onRest: () => c(!1),
        config: { duration: 1500, easing: ss },
      });
    return (
      (0, us.useEffect)(() => {
        if (o && m)
          return ct(() => {
            (c(!0), r.finishLevelsAnimation());
          }, a + 100);
      }, [o, m, a]),
      (0, ms.jsxs)("div", {
        className: sa(fx.base, fx[`base__${d.current}`], h && fx.base__rewardTaken),
        children: [
          m &&
            !p &&
            (0, ms.jsxs)(ms.Fragment, {
              children: [
                (0, ms.jsx)("div", { className: fx.glow }),
                (0, ms.jsx)(i.div, { style: { opacity: f }, className: fx.animatedGlow }),
              ],
            }),
          u && (0, ms.jsx)("div", { className: fx.iconFinal }),
          m
            ? (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsxs)("div", {
                    className: fx.numberInProgress,
                    children: [
                      e,
                      (0, ms.jsx)(i.div, {
                        style: {
                          opacity: b,
                          transform: b
                            .to([0, 1], [2.5, 1])
                            .to((e) => `translate(-50%, -50%) scale(${e})`),
                        },
                        className: fx.animatedNumber,
                        children: e,
                      }),
                    ],
                  }),
                  (0, ms.jsx)("div", {
                    className: fx.title,
                    children: p ? gx.pausedStep() : gx.currentStep(),
                  }),
                ],
              })
            : (0, ms.jsx)("div", { className: fx.number, children: e }),
        ],
      })
    );
  }),
  xx = "ClosedStatus_659358dc",
  wx = "ClosedStatus_icon_26722519",
  Cx = "ClosedStatus_icon__current_d82fe3b3",
  yx = "ClosedStatus_icon__exit_70d0e6c0",
  Sx = "ClosedStatus_icon__exitActive_6e4d1395",
  jx = "ClosedStatus_icon__exitCurrentActive_add31c82",
  Ix = "ClosedStatus_icon__exitDone_694aab32",
  Nx = "ClosedStatus_title_9c1acbb0",
  kx = "ClosedStatus_title__exit_29b67eb8",
  Px = "ClosedStatus_title__exitActive_3d936f93",
  Rx = "ClosedStatus_title__exitDone_694aab32",
  Bx = Wt(
    ({
      level: e,
      playUnlockAnimation: a = !1,
      handleUnlockAnimationExited: t,
      baseUnlockProps: s,
    }) => {
      const r = (0, us.useRef)(null),
        n = (0, us.useRef)(null),
        { model: i } = of(),
        { isBattlePassPurchased: o } = i.root.get(),
        { cardStatus: l } = i.computes.cardStates(e, !0),
        c = l.current === ef.IN_PROGRESS,
        d = { exit: yx, exitActive: c ? jx : Sx, exitDone: Ix },
        _ = { exit: kx, exitActive: Px, exitDone: Rx },
        u = !o || a,
        m = c && u;
      return (0, ms.jsxs)("div", {
        className: xx,
        children: [
          u &&
            (0, ms.jsx)(qt, {
              ...s,
              nodeRef: r,
              classNames: d,
              onExited: t,
              children: (0, ms.jsx)("div", { ref: r, className: sa(wx, c && Cx) }),
            }),
          m &&
            (0, ms.jsx)(qt, {
              ...s,
              nodeRef: n,
              classNames: u ? _ : {},
              children: (0, ms.jsx)("div", {
                ref: n,
                className: Nx,
                children: R.strings.battle_pass.progression.currentStepLocked(),
              }),
            }),
        ],
      });
    },
  ),
  Ax = "CompletedStatus_cd7b3965",
  Ex = "CompletedStatus_base__showAnimation_b386bcdc",
  Tx = "CompletedStatus_iconGlow__completedEnter_8876529f",
  Lx = "CompletedStatus_iconGlow__completedEnterActive_81bf80a4",
  Ox = "CompletedStatus_iconGlow__completedEnterDone_36f61f63",
  Dx = "CompletedStatus_icon_a8f57fb0",
  Wx = ({ completedIn: e, handleCompleteGlowAnimationExited: a, children: t }) => {
    const s = (0, us.useRef)(null),
      r = { exit: Tx, exitActive: Lx, exitDone: Ox };
    return (0, ms.jsxs)("div", {
      className: sa(Ax, e && Ex),
      children: [
        (0, ms.jsx)(qt, {
          in: !e,
          nodeRef: s,
          timeout: aw,
          classNames: r,
          onExited: a,
          children: (0, ms.jsx)("div", { ref: s, children: t }),
        }),
        (0, ms.jsx)(U, {
          body: tw.tooltips.completed.got(),
          children: (0, ms.jsx)("div", { className: Dx }),
        }),
      ],
    });
  },
  Vx = {
    base: "CurrentPoints_4c27ce16",
    value__current: "CurrentPoints_value__current_9c51dee4",
    value__total: "CurrentPoints_value__total_99fac246",
    divider: "CurrentPoints_divider_83c77e4c",
    icon: "CurrentPoints_icon_6b371e14",
    fadeInWithScale: "CurrentPoints_fadeInWithScale_3970c66e",
    slideUp: "CurrentPoints_slideUp_3970c66e",
    blink: "CurrentPoints_blink_3970c66e",
    scale: "CurrentPoints_scale_3970c66e",
    rotate: "CurrentPoints_rotate_3970c66e",
    windowIn: "CurrentPoints_windowIn_3970c66e",
    fadeOut: "CurrentPoints_fadeOut_3970c66e",
    fadeIn: "CurrentPoints_fadeIn_3970c66e",
  },
  Mx = Wt(() => {
    const {
        model: { computes: e },
      } = of(),
      { current: a, total: t } = e.currentLevelPoints();
    return (0, ms.jsx)(me, {
      ignoreShowDelay: !0,
      contentId: R.views.mono.battle_pass.tooltips.bp_points("resId"),
      children: (0, ms.jsxs)("div", {
        className: Vx.base,
        children: [
          (0, ms.jsx)("div", { className: sa(Vx.value, Vx.value__current), children: a }),
          (0, ms.jsx)("div", { className: Vx.divider, children: "/" }),
          (0, ms.jsx)("div", { className: sa(Vx.value, Vx.value__total), children: t }),
          (0, ms.jsx)("div", { className: Vx.icon }),
        ],
      }),
    });
  }),
  zx = "Effects_glowWrapper_efa5ae0d",
  $x = "Effects_glow_75ba9df8",
  Fx = "Effects_glow__active_b9e151",
  Hx = "Effects_dust_f4cf542",
  Ux = "Effects_dust__active_ece15182",
  Gx = ({ baseUnlockProps: e }) => {
    const a = (0, us.useRef)(null),
      t = (0, us.useRef)(null),
      s = { exit: $x, exitActive: Fx, exitDone: $x },
      r = { exit: Hx, exitActive: Ux, exitDone: Hx };
    return (0, ms.jsxs)("div", {
      children: [
        (0, ms.jsx)(qt, {
          ...e,
          nodeRef: a,
          classNames: s,
          children: (0, ms.jsx)("div", {
            ref: a,
            className: zx,
            children: (0, ms.jsx)("div", { className: $x }),
          }),
        }),
        (0, ms.jsx)(qt, {
          ...e,
          nodeRef: t,
          classNames: r,
          children: (0, ms.jsx)("div", {
            ref: t,
            className: zx,
            children: (0, ms.jsx)("div", { className: Hx }),
          }),
        }),
      ],
    });
  },
  qx = "Status_5c99d05d",
  Kx = "Status_base__inProgress_21b2f358",
  Xx = "Status_iconContainer_7da53d2b",
  Zx = "Status_iconInner_9a38fa07",
  Jx = "Status_iconGlow_e61b8bfb",
  Qx = "Status_iconGlow__completed_1ceaf83f",
  Yx = "Status_iconGlow__hidden_5ce2d06a",
  ew = "Status_pointsWrapper_6042cf48",
  aw = 1500,
  tw = R.strings.battle_pass,
  sw = R.views.mono.battle_pass,
  rw = Wt(
    ({
      isPremium: e,
      playCompleteAnimation: a,
      playUnlockAnimation: t,
      completeAnimationDelay: s = 0,
      unlockAnimationDelay: r = 0,
      baseTimeout: n = 0,
      playUnlockAnimationSound: i = !0,
      playCompleteAnimationSound: o = !0,
      onAnimationDone: l,
      initialAnimationDelay: c,
      completedDuration: d,
      level: _,
    }) => {
      const { model: u } = of(),
        { cardStatus: m, isDisabled: p } = u.computes.cardStates(_, e),
        h = u.computes.isRewardNeedTake(_, e),
        [b, f] = (0, us.useState)(!1),
        [g, v] = (0, us.useState)(!1),
        [x, w] = (0, us.useState)(!0),
        [C, y] = (0, us.useState)(!1),
        S = m.current === ef.COMPLETED && !h && !p,
        j = (p && e) || S || t,
        I = !e && m.current === ef.IN_PROGRESS && m.potential !== ef.COMPLETED,
        N = () => {
          (o && ue.sound(af.IMPROVED_REWARD), f(!0));
        };
      ((0, us.useEffect)(
        () =>
          t
            ? ct(() => {
                (w(!1),
                  i &&
                    !C &&
                    (m.current === ef.IN_PROGRESS
                      ? ue.sound(af.UNLOCK_BIG)
                      : ue.sound(af.UNLOCK_SMALL)));
              }, c + r)
            : a
              ? (v(!0),
                ct(() => {
                  (v(!1), N());
                }, c + s))
              : void (g && v(!1)),
        [t, a, g],
      ),
        (0, us.useEffect)(() => {
          if (a && C)
            return ct(() => {
              N();
            }, s);
        }, [a, C]));
      const k = () => {
          (!a && l && l(), y(!0));
        },
        P = { in: x, timeout: aw + n };
      return (0, ms.jsxs)("div", {
        className: sa(qx, m.current === ef.IN_PROGRESS && Kx),
        style: { "--animation-duration": `${d}ms` },
        children: [
          j &&
            (0, ms.jsxs)("div", {
              className: Xx,
              children: [
                ((!a && S) || (b && !h)) &&
                  (0, ms.jsx)(Wx, {
                    completedIn: b,
                    handleCompleteGlowAnimationExited: () => {
                      g && v(!1);
                    },
                    children: (0, ms.jsx)("div", { className: sa(Jx, Qx, g && Yx) }),
                  }),
                !a &&
                  !t &&
                  p &&
                  e &&
                  (0, ms.jsx)(me, {
                    isEnabled: e,
                    contentId: sw.tooltips.lock_icon("resId"),
                    children: (0, ms.jsx)("div", {
                      children: (0, ms.jsx)(Bx, {
                        level: _,
                        baseUnlockProps: P,
                        playUnlockAnimation: t,
                        handleUnlockAnimationExited: k,
                      }),
                    }),
                  }),
                t &&
                  !C &&
                  (0, ms.jsx)(me, {
                    contentId: sw.tooltips.lock_icon("resId"),
                    children: (0, ms.jsxs)("div", {
                      className: Zx,
                      children: [
                        (0, ms.jsx)(Bx, {
                          level: _,
                          baseUnlockProps: P,
                          playUnlockAnimation: t,
                          handleUnlockAnimationExited: k,
                        }),
                        m.current === ef.IN_PROGRESS && (0, ms.jsx)(Gx, { baseUnlockProps: P }),
                      ],
                    }),
                  }),
              ],
            }),
          I && (0, ms.jsx)("div", { className: ew, children: (0, ms.jsx)(Mx, {}) }),
        ],
      });
    },
  ),
  nw = {
    base: "Rewards_70f08a68",
    base__column: "Rewards_base__column_a9c4b33d",
    base__inProgress: "Rewards_base__inProgress_d0a3b9e5",
    reward: "Rewards_reward_3ab9772c",
    base__tripleDefault: "Rewards_base__tripleDefault_405577a5",
    reward__0: "Rewards_reward__0_405577a5",
    reward__2: "Rewards_reward__2_ab1f8587",
    base__reverse: "Rewards_base__reverse_405577a5",
    base__tripleInProgress: "Rewards_base__tripleInProgress_405577a5",
    reward__1: "Rewards_reward__1_804d2a62",
    base__single: "Rewards_base__single_405577a5",
    shine: "Rewards_shine_353df8a9",
    base__animated: "Rewards_base__animated_405577a5",
    fadeIn: "Rewards_fadeIn_405577a5",
    rewardInner: "Rewards_rewardInner_cdaabcb1",
    changeReward: "Rewards_changeReward_405577a5",
    staticShine: "Rewards_staticShine_6885b0f2",
    explosion: "Rewards_explosion_20cd9d55",
    preview: "Rewards_preview_4455ca2",
    iconButton: "Rewards_iconButton_1f79ae3",
    fadeInWithScale: "Rewards_fadeInWithScale_405577a5",
    slideUp: "Rewards_slideUp_405577a5",
    blink: "Rewards_blink_405577a5",
    scale: "Rewards_scale_405577a5",
    rotate: "Rewards_rotate_405577a5",
    windowIn: "Rewards_windowIn_405577a5",
    fadeOut: "Rewards_fadeOut_405577a5",
  },
  iw = xa((e) => {
    const {
      item: a,
      name: t,
      value: s,
      overlayType: r,
      tooltipId: n,
      tooltipContentId: i,
      id: o,
      icon: l,
    } = e;
    return {
      id: o,
      icon: l,
      name: a || t,
      smallImage: rt(e, ra.Big),
      bigImage: rt(e, ra.S180x135),
      special: r,
      value: s,
      valueType: Xe(t),
      tooltipArgs: Na({ tooltipId: n }, Number(i), { ignoreShowDelay: !0 }),
    };
  }),
  ow = Wt(({ isPremium: e, levelNum: a, hasAnimation: t }) => {
    const {
        breakpoint: { weight: s },
      } = Me(),
      { model: r, controls: n } = of(),
      { cardStatus: i } = r.computes.cardStates(a, e),
      o = r.computes.isRewardNeedTake(a, e),
      l = r.computes.levelRewardItems(a, !0),
      c = r.computes.levelRewardItems(a, !1),
      d = e ? c : l,
      [_, u] = (0, us.useState)(d),
      m = i.current === ef.IN_PROGRESS,
      p = (0, us.useRef)(!1);
    (0, us.useEffect)(() => {
      if (p.current) return ct(() => u(d), 1e3);
      p.current = !0;
    }, [d, p]);
    return (0, ms.jsx)("div", {
      className: sa(
        nw.base,
        m && nw.base__inProgress,
        e && nw.base__reverse,
        t && nw.base__animated,
        1 === d.length && nw.base__single,
        2 === d.length && nw.base__column,
        3 === d.length && (m ? nw.base__tripleInProgress : nw.base__tripleDefault),
      ),
      children: re(_, (e, a) => {
        const r = iw(e),
          i = r.name.includes(Wa.StyleProgressToken) || r.name.includes(Wa.BattlePassSelectToken),
          l = (o && i) || t,
          { size: c, image: _ } = ((e) => {
            const a = s < _e.medium.weight;
            return d.length > 1
              ? a
                ? { size: ra.Small, image: e.smallImage }
                : { size: ra.Big, image: e.smallImage }
              : a
                ? { size: ra.Big, image: e.smallImage }
                : { size: ra.S180x135, image: e.bigImage };
          })(r);
        return (0, ms.jsxs)(
          "div",
          {
            className: sa(nw.reward, nw[`reward__${a}`]),
            children: [
              l && (0, ms.jsx)("div", { className: nw.shine }),
              t &&
                (0, ms.jsxs)(ms.Fragment, {
                  children: [
                    (0, ms.jsx)("div", { className: nw.staticShine }),
                    (0, ms.jsx)("div", { className: nw.explosion }),
                  ],
                }),
              (0, ms.jsx)(L, { size: c, image: _, className: nw.rewardInner, ...r }),
              r.icon === rs.style &&
                (0, ms.jsx)("div", {
                  className: nw.preview,
                  children: (0, ms.jsx)(za, {
                    type: "preview",
                    size: "normal",
                    className: nw.iconButton,
                    onClick: () => n.onStyleBonusPreview(r.id),
                  }),
                }),
            ],
          },
          `reward__${r.name}${a}`,
        );
      }),
    });
  }),
  lw = "CardRewards_50fb1177",
  cw = "CardRewards_base__completed_434ea7b1",
  dw = Wt(({ levelNum: e, isRewardAnimationActive: a, isPremium: t = !1 }) => {
    const { model: s } = of(),
      { cardStatus: r, isDisabled: n } = s.computes.cardStates(e, t),
      i = s.computes.isRewardNeedTake(e, t),
      o = r.current === ef.COMPLETED && !i && !n && !a;
    return (0, ms.jsx)("div", {
      className: sa(lw, o && cw),
      children: (0, ms.jsx)(ow, { levelNum: e, isPremium: t, hasAnimation: a }),
    });
  }),
  _w = "CardContent_f26d7969",
  uw = "CardContent_status_b4751d54",
  mw = "CardContent_buttonHolder_5af6834d",
  pw = "CardContent_buttonLight_c4e99653",
  hw = "CardContent_buttonInner_331e7784",
  bw = "CardContent_buttonInner__disabled_df771be2",
  fw = "CardContent_button_3b7b5ae4",
  gw = "CardContent_button__disabled_d7ebe82e",
  vw = "CardContent_buttonBlink_4f39579b",
  xw = "CardContent_buttonText_25c40fc",
  ww = 100,
  Cw = R.strings.battle_pass.progression,
  yw = Wt(
    ({
      isPremium: e,
      stepNumber: a,
      onFinalAnimationDone: t,
      maxVisibleCards: s,
      showLevelsAnimations: r,
      showBuyAnimations: n,
    }) => {
      const {
          model: i,
          controls: { finishAnimation: o, takeReward: l },
        } = of(),
        { isBattlePassPurchased: c, currentLevel: d, previousLevel: _ } = i.root.get(),
        {
          needTakePaid: u,
          needTakeFree: m,
          isFreeRewardChoiceEnabled: p,
          isPaidRewardChoiceEnabled: h,
        } = i.computes.levelInfo(a),
        { cardStatus: b } = i.computes.cardStates(a, e),
        f = i.computes.isRewardNeedTake(a, e),
        g = b.current === ef.IN_PROGRESS,
        v = b.current === ef.COMPLETED,
        [x, w] = (0, us.useState)(!1),
        [C, y] = (0, us.useState)(!1),
        {
          breakpoint: { weight: S },
        } = Me(),
        j = S <= _e.small.weight ? va.extraSmall : va.small,
        I = (0, us.useRef)(f),
        N = I.current;
      ((0, us.useEffect)(() => {
        I.current = f;
      }),
        (0, us.useEffect)(() => {
          if (N && !f) {
            const e = ct(() => {
                (w(!1), o());
              }, 1800),
              a = ct(() => {
                y(!1);
              }, 2300);
            return (
              w(!0),
              y(!0),
              () => {
                (e(), a());
              }
            );
          }
        }, [f]));
      const k = (() => {
          let i,
            o = 0,
            l = 0,
            u = 0,
            m = 0,
            p = !1,
            h = !1,
            b = !1,
            f = 300 * Math.ceil(d / 25);
          if (s && n && c) {
            const e = Math.floor(0.5 * s);
            let t = d - e,
              r = d + e,
              n = 0;
            t <= 0 && ((n = 1 - t), (r += n), (t = 1));
            const i = a < d && a >= t,
              c = a > d && a <= r,
              _ = a === t;
            (i ? (o = (a - t + 1) * ww) : c && (o = (a - t) * ww),
              (p = Boolean(g || i || c || _)),
              (h = Boolean(g || _)),
              (b = Boolean(v && p)),
              (l = (s - n - 1) * ww),
              g && (m = (a - t + 1) * ww * 2.5));
          }
          if (s && r) {
            const n = Math.min(d - _, Math.floor(0.5 * s));
            let o = d - n;
            o <= 0 && (o = 1);
            const c = a < d && a >= o;
            (c && ((l = (a - o + 1) * ww), e && (l += ww)),
              (b = Boolean(v && c)),
              (u = n * ww + ww * Math.trunc(n / 2) + f),
              r && (i = t));
          }
          return (
            C && ((f = 0), (l = 1800), (b = Boolean(v))),
            a === d - 1 && (i = t),
            {
              baseTimeout: m,
              playCompleteAnimation: b,
              playCompleteAnimationSound: b,
              playUnlockAnimation: p,
              playUnlockAnimationSound: h,
              unlockAnimationDelay: o,
              onAnimationDone: i,
              completeAnimationDelay: l,
              stageAnimationDelay: u,
              initialAnimationDelay: f,
            }
          );
        })(),
        P = Ee(() => {
          l({ level: a });
        }),
        R = m || u,
        B = R && !(p || h);
      return (0, ms.jsxs)("div", {
        className: _w,
        children: [
          !e &&
            (0, ms.jsxs)(ms.Fragment, {
              children: [
                (0, ms.jsx)(vx, {
                  stepNumber: a,
                  stageAnimationDelay: k.stageAnimationDelay,
                  isRewardAnimationActive: x,
                }),
                R &&
                  (0, ms.jsx)(U, {
                    isEnabled: B,
                    body: Cw.btnRewardsUnavailable(),
                    children: (0, ms.jsxs)("div", {
                      className: mw,
                      children: [
                        !B && (0, ms.jsx)("div", { className: pw }),
                        (0, ms.jsx)("div", {
                          className: sa(hw, B && bw),
                          children: (0, ms.jsxs)(ya, {
                            type: Fe.ghost,
                            size: j,
                            disabled: B,
                            onClick: P,
                            mixClass: sa(fw, B && gw),
                            children: [
                              !B && (0, ms.jsx)("div", { className: vw }),
                              (0, ms.jsx)("div", { className: xw, children: Cw.takeReward() }),
                            ],
                          }),
                        }),
                      ],
                    }),
                  }),
              ],
            }),
          (0, ms.jsx)(dw, { levelNum: a, isPremium: e, isRewardAnimationActive: x }),
          (0, ms.jsx)("div", {
            className: uw,
            children: (0, ms.jsx)(rw, {
              isPremium: Boolean(e),
              completedDuration: 500,
              level: a,
              ...k,
            }),
          }),
        ],
      });
    },
  ),
  Sw = {
    base: "Divider_e7aefb14",
    base__left: "Divider_base__left_c4dc4b02",
    base__right: "Divider_base__right_5c287de9",
    base__rare: "Divider_base__rare_e403ffc2",
    base__completed: "Divider_base__completed_e15d1358",
    base__premium: "Divider_base__premium_edc64468",
    inner: "Divider_inner_5e9c8eab",
    fadeInWithScale: "Divider_fadeInWithScale_76b1f722",
    slideUp: "Divider_slideUp_76b1f722",
    blink: "Divider_blink_76b1f722",
    scale: "Divider_scale_76b1f722",
    rotate: "Divider_rotate_76b1f722",
    windowIn: "Divider_windowIn_76b1f722",
    fadeOut: "Divider_fadeOut_76b1f722",
    fadeIn: "Divider_fadeIn_76b1f722",
  },
  jw = ({ position: e, isPremium: a = !1, isRare: t = !1, status: s }) =>
    (0, ms.jsx)("div", {
      className: sa(
        Sw.base,
        Sw[`base__${s}`],
        Sw[`base__${e}`],
        t && Sw.base__rare,
        a && Sw.base__premium,
      ),
      children: (0, ms.jsx)("div", { className: Sw.inner }),
    }),
  Iw = {
    base: "Card_83a2cdb2",
    base__inProgress: "Card_base__inProgress_cc79557f",
    base__nonPremium: "Card_base__nonPremium_43e4be2f",
    totalPoints: "Card_totalPoints_c960ba66",
    totalPoints__default: "Card_totalPoints__default_86462962",
    totalPoints__final: "Card_totalPoints__final_b0d756a8",
    progressShadow: "Card_progressShadow_e0bd1d",
    fadeInWithScale: "Card_fadeInWithScale_f4c22d1c",
    slideUp: "Card_slideUp_f4c22d1c",
    blink: "Card_blink_f4c22d1c",
    scale: "Card_scale_f4c22d1c",
    rotate: "Card_rotate_f4c22d1c",
    windowIn: "Card_windowIn_f4c22d1c",
    fadeOut: "Card_fadeOut_f4c22d1c",
    fadeIn: "Card_fadeIn_f4c22d1c",
  },
  Nw = (e, a, t, s) =>
    e === ef.COMPLETED
      ? 100
      : e !== ef.IN_PROGRESS || (a !== Zb.NotStarted && a !== Zb.Paused)
        ? 0
        : (100 * t) / s,
  kw = Wt(
    ({
      isPremium: e,
      stepNumber: a,
      maxLevels: t,
      maxVisibleCards: s,
      showBuyAnimations: r,
      showLevelsAnimations: n,
      onAnimationDone: i,
      levelRef: o,
    }) => {
      const { model: l } = of(),
        { currentPointsInLevel: c, chapterState: d } = l.root.get(),
        { cardStatus: _, isRare: u } = l.computes.cardStates(a, e),
        { levelPoints: m } = l.computes.levelInfo(a),
        p = !e && (_.current === ef.COMPLETED || _.current === ef.IN_PROGRESS),
        h = 1 === a,
        b = a === t,
        f = h ? void 0 : l.computes.cardStates(a - 1, e),
        g = b ? void 0 : l.computes.cardStates(a + 1, e),
        v = (0, us.useRef)(null),
        x = e ? (a - 1) * m : m;
      (0, us.useImperativeHandle)(o, () => ({
        width: () => {
          const e = v.current;
          return e ? e.offsetWidth : 0;
        },
        offsetLeft: () => {
          const e = v.current;
          return e ? e.offsetLeft : 0;
        },
        getOffsetLeftInArea: () => {
          const e = v.current;
          if (!e) return 0;
          const a = e.parentNode,
            t = a ? a.offsetLeft : 0;
          return e.offsetLeft + t;
        },
        getHTMLElement: () => v.current,
      }));
      const w =
          !h &&
          ((_.current === ef.NOT_STARTED && !u) ||
            (f?.isRare && _.current !== ef.IN_PROGRESS) ||
            f?.cardStatus.current === ef.IN_PROGRESS),
        C =
          !b &&
          ((_.current === ef.COMPLETED && !u) ||
            (g?.isRare && _.current !== ef.IN_PROGRESS) ||
            g?.cardStatus.current === ef.IN_PROGRESS),
        y = { width: `${Nw(_.current, d, c, x)}%` },
        S = {
          "--small-card-width": "140rem",
          "--small-current-card-width": "224rem",
          "--big-card-width": "220rem",
          "--big-current-card-width": "340rem",
        };
      return (0, ms.jsxs)("div", {
        className: sa(Iw.base, Iw[`base__${_.current}`], !e && Iw.base__nonPremium),
        ref: v,
        style: S,
        children: [
          (0, ms.jsx)(bx, { level: a, isPremium: e }),
          (0, ms.jsx)(yw, {
            isPremium: e,
            stepNumber: a,
            maxVisibleCards: s,
            showLevelsAnimations: n,
            showBuyAnimations: r,
            onFinalAnimationDone: i,
          }),
          e &&
            (0, ms.jsxs)(ms.Fragment, {
              children: [
                (0, ms.jsx)("div", {
                  className: sa(Iw.totalPoints, Iw.totalPoints__default),
                  children: x,
                }),
                b &&
                  (0, ms.jsx)("div", {
                    className: sa(Iw.totalPoints, Iw.totalPoints__final),
                    children: t * m,
                  }),
              ],
            }),
          p && (0, ms.jsx)("div", { className: Iw.progressShadow, style: y }),
          !w && (0, ms.jsx)(jw, { position: Yb.left, isPremium: e, isRare: u, status: _.current }),
          !C && (0, ms.jsx)(jw, { position: Yb.right, isPremium: e, isRare: u, status: _.current }),
        ],
      });
    },
  ),
  Pw = Wt(
    ({
      currentCardRef: e,
      freeProgressionCutCardRef: a,
      potentialLevelCardRef: t,
      isPremium: s,
      sectionKey: r,
      maxVisibleCards: n,
    }) => {
      const { model: i } = of(),
        {
          chapterID: o,
          currentLevel: l,
          potentialLevel: c,
          showBuyAnimations: d,
          showLevelsAnimations: _,
        } = i.root.get(),
        u = i.levels.get(),
        [m, p] = (0, us.useState)(!1),
        h = () => {
          p(!0);
        },
        b = Boolean(n && s && d),
        f = Boolean(n && _),
        g = (s, r, n) => (s === r ? e : s === n ? t : a);
      return (0, ms.jsx)("div", {
        className: sa(Xv.row, !s && Xv.row__basic),
        children: re(u, (e, a) =>
          (0, ms.jsx)(
            kw,
            {
              showBuyAnimations: b && !m,
              showLevelsAnimations: f,
              levelRef: g(e.level, l, c),
              stepNumber: e.level,
              isPremium: s,
              maxLevels: u.length,
              maxVisibleCards: n,
              onAnimationDone: h,
            },
            `${o}_${r}_${a}`,
          ),
        ),
      });
    },
  ),
  Rw = Wt(
    ({
      currentCardRef: e,
      freeProgressionCutCardRef: a,
      potentialLevelCardRef: t,
      onProgressChanged: s,
      widget3dStyleLeftRef: r,
      shadowLipRef: n,
      api: i,
    }) => {
      const { model: o } = of(),
        { currentLevel: l, currentPointsInLevel: c, showLevelsAnimations: d } = o.root.get(),
        _ = o.computes.isLayoutWithExtraWidget(),
        u = o.levels.get(),
        m = (0, us.useRef)(ta()),
        p = (0, us.useRef)(ta());
      i.current.moveProgressBars = (e) => {
        (m.current.update(e), p.current.update(e));
      };
      const [h, b] = (0, us.useState)({ levelWidth: 0, currentLevelWidth: 0, maxCardsShown: 0 }),
        f = (0, us.useCallback)(() => {
          if (e.current) {
            const t = e.current,
              s = a.current,
              r = t ? t.width() : 0,
              n = s ? s.width() : 0;
            return !n && r
              ? { currentLevelWidth: r, levelWidth: 224 === r ? 140 : 220 }
              : { currentLevelWidth: r, levelWidth: n };
          }
        }, [e, a]),
        {
          breakpoint: { weight: g },
        } = Me();
      return (
        (0, us.useEffect)(() => {
          Yt().then(() => {
            const e = f();
            if (e) {
              const a =
                Math.floor(
                  (viewEnv.getClientSizeRem().width - e.currentLevelWidth) / e.levelWidth,
                ) + 1;
              b({
                levelWidth: e.levelWidth,
                currentLevelWidth: e.currentLevelWidth,
                maxCardsShown: a,
              });
            }
          });
        }, [g, f, u.length, l, c]),
        (0, us.useEffect)(() => {
          d && ue.sound(R.sounds.bp_progress_bar_start());
        }, [d]),
        (0, us.useEffect)(() => {
          s && s();
        }, [l, c, s]),
        (0, ms.jsxs)("div", {
          className: Xv.wrapper,
          children: [
            !_ &&
              (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsx)(Uv, { widget3dStyleRef: r, level: 1, isShowTitle: !0 }),
                  (0, ms.jsx)("div", {
                    className: sa(Xv.decor, Xv.decor__left),
                    children: (0, ms.jsx)("div", { className: Xv.decorBackground }),
                  }),
                  (0, ms.jsx)("div", {
                    className: Xv.bookmarkBackground,
                    ref: n,
                    children: (0, ms.jsx)(yv, {
                      isDisappeared: !0,
                      mixClass: Xv.bookmarkLeftResponsive,
                    }),
                  }),
                ],
              }),
            (0, ms.jsxs)("div", {
              className: Xv.section,
              children: [
                (0, ms.jsx)(Pw, {
                  sectionKey: "baseCard",
                  currentCardRef: e,
                  freeProgressionCutCardRef: a,
                  potentialLevelCardRef: t,
                  maxVisibleCards: d ? h.maxCardsShown : 0,
                  currentLevel: l,
                }),
                (0, ms.jsx)(Jv, { progressApi: m, freePointsApi: p, progressChange: s, ...h }),
                (0, ms.jsx)(Pw, {
                  sectionKey: "basePremiumCard",
                  isPremium: !0,
                  currentCardRef: e,
                  freeProgressionCutCardRef: a,
                  potentialLevelCardRef: t,
                  maxVisibleCards: h.maxCardsShown,
                  currentLevel: l,
                }),
              ],
            }),
            !_ &&
              (0, ms.jsxs)(ms.Fragment, {
                children: [
                  (0, ms.jsx)("div", {
                    className: Xv.decor,
                    children: (0, ms.jsx)("div", { className: Xv.decorBackground }),
                  }),
                  (0, ms.jsx)(Uv, { level: 4 }),
                ],
              }),
          ],
        })
      );
    },
  ),
  Bw = { allowedButtons: [rv.MainButton] },
  Aw = R.strings.battle_pass.progression,
  Ew = ["dragStart", "dragEnd", "dragging"],
  Tw = Wt(({ onHorizontalScroll: e }) => {
    const { model: a } = of(),
      t = a.levels.get(),
      { currentLevel: s, isBattlePassPurchased: r, showBuyAnimations: n } = a.root.get(),
      i = (0, us.useRef)({ moveProgressBars: () => {} }),
      o = (0, us.useRef)(null),
      l = (0, us.useRef)(null),
      c = (0, us.useRef)(null),
      d = (0, us.useRef)(null),
      _ = (0, us.useRef)(null),
      u = (0, us.useRef)(null),
      m = (0, us.useRef)(null),
      p = (0, us.useRef)(0),
      h = a.computes.isLayoutWithExtraWidget(),
      [b, f] = (0, us.useState)("hidden"),
      [g, v] = (0, us.useState)("hidden"),
      [x, w] = (0, us.useState)(!1),
      [C, y] = (0, us.useState)(void 0),
      S = qe(),
      {
        animationScroll: { scrollPosition: j },
        applyScroll: I,
        events: N,
        handleMouseWheel: k,
        getContainerSize: P,
        getWrapperSize: R,
      } = S,
      [B, A] = (function (e, a, t) {
        const {
            contentRef: s,
            wrapperRef: r,
            scrollPosition: n,
            clampPosition: i,
            animationScroll: o,
            events: l,
          } = e,
          [c, d] = (0, us.useState)(sv);
        return (
          (0, us.useEffect)(() => {
            const e = s.current;
            e && (e.style.cursor = "dragging" === c.type ? "move" : "grab");
          }, [s, c.type]),
          (0, us.useEffect)(() => {
            if ("dragging" !== c.type) return;
            const e = (e) => {
              const t = s.current,
                l = r.current;
              if (!t || !l) return;
              const d = c.positionFrom - e.screenX,
                _ = c.previousScrollPosition + d;
              n.start({
                scrollPosition: i(t, _),
                from: { scrollPosition: o.scrollPosition.get() },
                ...(a && { config: a }),
              });
            };
            function t() {
              (window.removeEventListener("mousemove", e),
                document.body.removeEventListener("mouseleave", t),
                d({ type: "scrollingToEnd" }));
            }
            return (
              window.addEventListener("mousemove", e),
              window.addEventListener("mouseup", t),
              document.body.addEventListener("mouseleave", t),
              () => {
                (window.removeEventListener("mousemove", e),
                  window.removeEventListener("mouseup", t),
                  document.body.removeEventListener("mouseleave", t));
              }
            );
          }, [o.scrollPosition, i, s, c, n, r, a, t]),
          (0, us.useEffect)(() => {
            if ("scrollingToEnd" !== c.type) return;
            const e = () => {
              d(sv);
            };
            return (o.scrollPosition.idle && e(), l.on("rest", e), () => l.off("rest", e));
          }, [o.scrollPosition, c.type, l]),
          (0, us.useEffect)(() => {
            const e = s.current;
            if (!e) return;
            const a = (e) => {
              (t && t.allowedButtons && -1 === t.allowedButtons.findIndex((a) => e.button === a)) ||
                d({
                  type: "dragging",
                  positionFrom: e.screenX,
                  previousScrollPosition: o.scrollPosition.get(),
                });
            };
            return (
              e.addEventListener("mousedown", a),
              () => e.removeEventListener("mousedown", a)
            );
          }, [o.scrollPosition, s, t]),
          [c, d]
        );
      })(S, void 0, Bw),
      E = (e) => {
        (B.type === tv.Dragging && A({ type: tv.End }), k(e));
      },
      T = (0, us.useMemo)(() => ({ ...S, handleMouseWheel: E }), []),
      L = (0, us.useCallback)(
        (e) => {
          const a = d.current ? d.current.offsetWidth : 0,
            t = _.current ? _.current.offsetWidth : 0;
          if (o.current) {
            const s = R();
            (i.current.moveProgressBars({
              viewPort: o.current,
              horizontalScrollPosition: s ? e - s : e,
              leftOffset: a + t,
            }),
              w(h || e > a + 0.5 * t));
          }
        },
        [R, h],
      ),
      O = (0, us.useCallback)((e = !1) => {
        const a = l.current;
        let t = 0,
          s = 0;
        const r = d.current ? d.current.offsetWidth : 0,
          n = _.current ? _.current.offsetWidth : 0;
        a && ((t = a.width()), (s = a.offsetLeft() + r + n));
        const i = o.current;
        let c = 0;
        if (t && i) {
          const a = 0.5 * i.offsetWidth;
          e && p.current
            ? (c = s + t - 0.5 * p.current - a)
            : ((c = s + 0.5 * t - a), (p.current = t));
        }
        return ((c = Math.round(c < 0 ? 0 : c)), c);
      }, []),
      D = () => {
        const e = o.current,
          a = l && l.current,
          t = c.current,
          s = d.current ? d.current.offsetWidth : 0,
          r = _.current ? _.current.offsetWidth : 0;
        if (a && t) {
          const n = a.offsetLeft() + s + r,
            i = t.offsetLeft() + s + r,
            o =
              j.goal < n - e.offsetWidth
                ? "navToCurrentLevel"
                : t && j.goal < i - e.offsetWidth
                  ? "navToPotentialLevel"
                  : "hidden",
            l = (() => {
              switch (!0) {
                case t && j.goal > i + t.width():
                  return "navToPotentialLevel";
                case j.goal > n + a.width():
                  return "navToCurrentLevel";
                default:
                  return "hidden";
              }
            })();
          (f(o), v(l));
        }
      },
      W = (e) => {
        const a = ((e) => {
          let a = 0;
          if (e && e.current && o && o.current) {
            const t = e.current,
              s = d.current ? d.current.offsetWidth : 0,
              r = _.current ? _.current.offsetWidth : 0;
            let n = 0,
              i = 0;
            t && ((n = t.width()), (i = t.offsetLeft() + s + r));
            const l = o.current;
            (n && l && (a = i + 0.5 * n - 0.5 * l.offsetWidth), (a = Math.round(a < 0 ? 0 : a)));
          }
          return a;
        })(e);
        (L(j.goal), I(a), D());
      },
      V = (e) => {
        switch (e) {
          case "navToCurrentLevel":
            return W(l);
          case "navToPotentialLevel":
            return W(c);
        }
      },
      M = (e) => {
        switch (e) {
          case "navToCurrentLevel":
            return { type: sf.Default, tooltipBody: Aw.backToCurrentStageArrow.descr() };
          case "navToPotentialLevel":
            return { type: sf.Gray, tooltipBody: Aw.backToPotentialStageArrow.descr() };
        }
      },
      z = (e) => {
        (L(j.goal), D(), y(e?.type));
      };
    return (
      (0, us.useEffect)(
        () =>
          na(() => {
            r && n && I(O());
          }),
        [I, O, r, n],
      ),
      (0, us.useEffect)(() => {
        const e = async () => {
          const e = P(),
            a = j.goal;
          await Yt();
          const t = P(),
            s = o.current,
            [, r] = S.getBounds(),
            n = 0.25 * s.offsetWidth,
            i = t && e && t !== e ? (a * t) / e : a;
          (L(i), I(i > r - n ? r : i));
        };
        return (
          engine.on("clientResized", e),
          () => {
            engine.off("clientResized", e);
          }
        );
      }, []),
      (0, us.useEffect)(() => ct(() => W(l), 700), [s]),
      (0, us.useEffect)(() => {
        if (((e = "") => Ew.includes(e))(C)) return void e("dragStart" === C);
        const a = () => {
            C || L(j.goal);
          },
          t = () => {
            (e(!1), L(j.goal));
          },
          s = () => {
            (e(!0), L(j.goal));
          };
        return (
          N.on("change", a),
          N.on("rest", t),
          N.on("start", s),
          () => {
            (N.off("change", a), N.off("rest", t), N.off("start", s));
          }
        );
      }, [N, L, e, j.goal, C]),
      (0, ms.jsxs)(ms.Fragment, {
        children: [
          (0, ms.jsx)("div", {
            className: sa(Xv.bookmark, Xv.bookmark__start),
            children: (0, ms.jsx)(yv, {
              chapterStep: t.length,
              mixClass: sa(Xv.bookmarkLeftFixed, x && Xv.bookmarkLeftFixed__active),
            }),
          }),
          (0, ms.jsx)("div", {
            className: Xv.scrollWrapper,
            ref: o,
            onClick: z,
            onMouseLeave: D,
            onWheel: z,
            children: (0, ms.jsx)(Ia.Horizontal.Area.Default, {
              api: T,
              barClassNames: { base: Xv.scrollBarPosition },
              onDrag: z,
              children: (0, ms.jsx)(Rw, {
                api: i,
                currentCardRef: l,
                freeProgressionCutCardRef: u,
                potentialLevelCardRef: c,
                separatorRef: m,
                widget3dStyleLeftRef: d,
                shadowLipRef: _,
                onProgressChanged: z,
              }),
            }),
          }),
          (0, ms.jsx)("div", {
            className: sa(
              Xv.scrollToButton,
              Xv.scrollToButton__backward,
              "hidden" !== g && Xv.scrollToButton__visible,
            ),
            children: (0, ms.jsx)(iv, {
              onClick: () => V(g),
              direction: tf.back,
              className: Xv.arrowButton,
              ...M(g),
            }),
          }),
          (0, ms.jsx)("div", {
            className: sa(
              Xv.scrollToButton,
              Xv.scrollToButton__forward,
              "hidden" !== b && Xv.scrollToButton__visible,
            ),
            children: (0, ms.jsx)(iv, {
              onClick: () => V(b),
              direction: tf.forward,
              className: Xv.arrowButton,
              ...M(b),
            }),
          }),
        ],
      })
    );
  }),
  Lw = Wt(() => {
    const { model: e } = of(),
      a = e.computes.isLayoutWithExtraWidget(),
      [t, s] = (0, us.useState)(!1),
      r = sa(Xv.additionalShadow, t && Xv.additionalShadow__active);
    return (0, ms.jsxs)("div", {
      className: sa(Xv.base, a && Xv.base__isLayoutWithExtraWidget),
      children: [
        (0, ms.jsx)("div", {
          className: sa(Xv.shadow, Xv.shadow__left),
          children: (0, ms.jsx)("div", { className: r }),
        }),
        (0, ms.jsx)("div", {
          className: sa(Xv.shadow, Xv.shadow__right),
          children: (0, ms.jsx)("div", { className: r }),
        }),
        (0, ms.jsx)(Tw, {
          onHorizontalScroll: (e) => {
            s(e);
          },
        }),
      ],
    });
  }),
  Ow = "ProgressionContent_23d7382d",
  Dw = "ProgressionContent_base__extra_108a8890",
  Ww = "ProgressionContent_base__extraChapter_efc5bb01",
  Vw = "ProgressionContent_header_3c9de2e1",
  Mw = "ProgressionContent_progression_ee26929",
  zw = "ProgressionContent_progression__extraChapter_ed356b04",
  $w = "ProgressionContent_extraChapterWidget_6d130b1f",
  Fw = "ProgressionContent_footer_b7b80223",
  Hw = Wt(() => {
    const {
        model: { root: e, computes: a },
      } = of(),
      { chapterType: t, chapterID: s, actionType: r, isPaused: n } = e.get(),
      i = a.isLayoutWithExtraWidget(),
      o = t === Qb.EXTRA,
      l = r !== Jb.NoAction,
      c = sa(Mw, i && zw);
    return (0, ms.jsxs)("div", {
      className: sa(Ow, i && Dw, o && Ww),
      style: os(s),
      children: [
        !n && (0, ms.jsx)("div", { className: c, children: (0, ms.jsx)(Lw, {}) }),
        (0, ms.jsx)("div", { className: Vw, children: (0, ms.jsx)(av, {}) }),
        (0, ms.jsx)("div", { className: Fw, children: l && (0, ms.jsx)(Vg, {}) }),
        i && (0, ms.jsx)("div", { className: $w, children: (0, ms.jsx)(Lg, {}) }),
      ],
    });
  }),
  Uw = "App_7cf6cd46",
  Gw = Wt(() => {
    const { model: e, controls: a } = of(),
      { showReplaceRewardsAnimations: t } = e.root.get(),
      s = m();
    return (
      At(D.ESCAPE, () => s.goBack()),
      (0, us.useEffect)(() => {
        const e = () => {
          document.body.style.height = window.innerHeight - (innerHeight % 2) + "px";
        };
        return (
          window.addEventListener("resize", e),
          e(),
          () => {
            (window.removeEventListener("resize", e), (document.body.style.height = "auto"));
          }
        );
      }, []),
      (0, us.useEffect)(
        () =>
          na(() => {
            a.viewLoad();
          }),
        [],
      ),
      (0, us.useEffect)(() => {
        t && ue.sound(R.sounds.bp_pick_up_award());
      }, [t]),
      (0, ms.jsx)("div", { className: Uw, children: (0, ms.jsx)(Hw, {}) })
    );
  }),
  qw = () =>
    (0, ms.jsx)(nf, {
      options: { rootId: R.aliases.battle_pass.Progression("resId") },
      children: (0, ms.jsx)(Gw, {}),
    }),
  Kw = "App_811b056b",
  Xw = "App_mainView_54c70e4",
  Zw = Wt(() => {
    const { location: e } = m(),
      a = Y(e, {
        from: { opacity: 0 },
        enter: { opacity: 1, config: { duration: 150, easing: lt.easeInQuad }, delay: 150 },
      });
    return (0, ms.jsx)(us.Suspense, {
      fallback: (0, ms.jsx)("div", {}),
      children: (0, ms.jsx)("div", {
        className: Kw,
        children: a((e, a) =>
          (0, ms.jsx)(i.div, {
            className: Xw,
            style: e,
            children: (0, ms.jsxs)(Je, {
              children: [
                (0, ms.jsx)(ka, { path: ls.battlePass.progression, component: qw }),
                (0, ms.jsx)(ka, { path: ls.battlePass.chapterChoice, component: qu }),
                (0, ms.jsx)(ka, { path: ls.battlePass.postProgression, component: Xb }),
                (0, ms.jsx)(ka, { path: ls.battlePass.buyPass, component: mi }),
                (0, ms.jsx)(ka, { path: ls.battlePass.buyPassRewards, component: mi }),
                (0, ms.jsx)(ka, { path: ls.battlePass.buyLevels, component: pr }),
                (0, ms.jsx)(ka, { path: ls.battlePass.buyLevelsRewards, component: pr }),
                (0, ms.jsx)(ka, { path: ls.battlePass.holidayFinal, component: Ep }),
                (0, ms.jsx)(ka, { path: ls.battlePass.tankmenScreen, component: cs }),
              ],
            }),
          }),
        ),
      }),
    });
  });
ba(
  new Ya()
    .add(_t)
    .add(jt)
    .addWithProps(xe, { context: "model.router" })
    .render((0, ms.jsx)(Zw, {})),
)
  .then(() => M(document.getElementById("root")))
  .then(() => k());
