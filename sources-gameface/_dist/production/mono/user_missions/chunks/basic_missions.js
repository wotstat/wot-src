import { r as e } from "./rolldown-runtime.js";
import {
  $ as s,
  A as i,
  At as t,
  Bt as o,
  C as r,
  Ct as a,
  Dn as n,
  Dt as l,
  E as c,
  En as d,
  Et as m,
  Ft as u,
  Gt as _,
  Ht as p,
  It as g,
  Jt as f,
  Kt as x,
  Mn as h,
  Mt as b,
  Nt as C,
  On as v,
  Ot as N,
  Pn as y,
  Pt as I,
  Q as j,
  S as k,
  Sn as M,
  St as E,
  Ut as w,
  V as S,
  Vt as P,
  Wt as B,
  Xt as O,
  Y as T,
  _ as A,
  _t as L,
  an as D,
  c as W,
  cn as F,
  d as H,
  fn as G,
  g as V,
  gn as q,
  h as $,
  hn as z,
  in as U,
  j as Q,
  jt as Y,
  kt as X,
  l as J,
  ln as K,
  m as Z,
  on as ee,
  ot as se,
  p as ie,
  rn as te,
  st as oe,
  tt as re,
  u as ae,
  un as ne,
  w as le,
  wn as ce,
  wt as de,
  xn as me,
  xt as ue,
  y as _e,
  yn as pe,
  z as ge,
  zt as fe,
} from "./lib.js";
import { t as xe } from "../hub/bundle.js";
import { n as he, r as be } from "./helpers.js";
import { t as Ce } from "./reward_wrapper.js";
var [ve, Ne] = E()(
    ({ observableModel: e }) => e.object(),
    ({ externalModel: e }) => ({
      goToCampaigns: e.createCallbackNoArgs("goToCampaigns"),
      goToOperation: e.createCallbackNoArgs("goToOperation"),
    }),
  ),
  ye = (function (e) {
    return (
      (e.CAMPAIGN_NOT_ACTIVATED = "campaignNotActivated"),
      (e.IN_PROGRESS = "inProgress"),
      (e.IN_PROGRESS_FOR_HONORS = "inProgressForHonors"),
      (e.COMPLETED = "completed"),
      (e.COMPLETED_WITH_HONORS = "completedWithHonors"),
      e
    );
  })({}),
  Ie = "ActionButton_20d194fb",
  je = "ActionButton_text_eb11c2b7",
  ke = e(f(), 1);
function Me({ textPath: e, ...s }) {
  return (0, ke.jsx)(S, {
    ...s,
    className: n(Ie, s.className),
    children: (0, ke.jsx)(oe, { className: je, path: e }),
  });
}
var Re = "TextBlock_97d73ac3",
  Ee = "TextBlock_base__centered_d13b3a4b",
  we = "TextBlock_title_770e50f6",
  Se = "TextBlock_description_eacddfcf",
  Pe = y.resolve("strings");
y.resolve("aliases");
var Be = (e, s, i) => {
    const t = `${e}.${s}`;
    return s === ye.COMPLETED_WITH_HONORS ? `${t}.${i ? "allCompleted" : "default"}` : t;
  },
  Oe = L(function ({ centered: e = !1, className: s, classNames: t }) {
    const { model: o } = Ne(),
      {
        state: r,
        allOperationsCompleted: a,
        currentOperationName: l,
        nextOperationName: c,
        stageNumber: d,
        totalProgress: m,
      } = o.get();
    return (0, ke.jsxs)("div", {
      className: n(Re, e && Ee, s),
      children: [
        (0, ke.jsx)(oe, {
          path: Be("user_missions.hub.basic_missions.personal.title", r, a),
          params: { currentOperationName: l, nextOperationName: c, stageNumber: d },
          className: n(we, t?.title),
        }),
        (0, ke.jsx)(i, {
          classMix: n(Se, t?.description),
          justifyContent: e ? A.Center : A.FlexStart,
          text: Pe.readOrEmpty(Be("user_missions.hub.basic_missions.personal.description", r, a))
            .replace("{{currentOperationName}}", l)
            .replace("{{nextOperationName}}", c)
            .replace("{{totalProgress}}", m.toString()),
          isTruncationAvailable: !0,
        }),
      ],
    });
  }),
  Te = "CampaignNotActivated_9407dfc7",
  Ae = "CampaignNotActivated_textBlock_c662540",
  Le = "CampaignNotActivated_title_d30bb4f2",
  De = L(function () {
    const { controls: e } = Ne();
    return (0, ke.jsxs)("div", {
      className: Te,
      children: [
        (0, ke.jsx)(Oe, { className: Ae, classNames: { title: Le } }),
        (0, ke.jsx)(Me, {
          theme: "primary",
          onClick: e.goToCampaigns,
          textPath: "user_missions.hub.basic_missions.personal.button.to_campaign",
        }),
      ],
    });
  }),
  We = "Completed_47cefd15",
  Fe = "Completed_textBlock_15b3296b",
  He = L(function () {
    const { controls: e } = Ne();
    return (0, ke.jsxs)("div", {
      className: We,
      children: [
        (0, ke.jsx)(Oe, { className: Fe }),
        (0, ke.jsx)(Me, {
          theme: "primary",
          onClick: e.goToOperation,
          textPath: "user_missions.hub.basic_missions.personal.button.to_operation",
        }),
      ],
    });
  }),
  Ge = "CompletedWithHonors_bc0ee63d",
  Ve = "CompletedWithHonors_base__allCompleted_632ea0e2",
  qe = "CompletedWithHonors_completedIcon_de0cf0c3",
  $e = "CompletedWithHonors_textBlock_9e298c15",
  ze = "CompletedWithHonors_base__hasUncompleted_906ea6c6",
  Ue = "CompletedWithHonors_title_a75dacc1",
  Qe = "CompletedWithHonors_description_aead74a",
  Ye = L(function () {
    const { model: e, controls: s } = Ne(),
      { allOperationsCompleted: i } = e.get();
    return (0, ke.jsxs)("div", {
      className: n(Ge, i ? Ve : ze),
      children: [
        i && (0, ke.jsx)("div", { className: qe }),
        (0, ke.jsx)(Oe, { centered: i, className: $e, classNames: { title: Ue, description: Qe } }),
        (0, ke.jsx)(Me, {
          theme: i ? "primary" : "secondary",
          onClick: s.goToOperation,
          textPath:
            "user_missions.hub.basic_missions.personal.button." +
            (i ? "to_completed_operation" : "to_operation"),
        }),
      ],
    });
  }),
  Xe = e(v(), 1),
  Je = {
    base: "ProgressCount_1bbbcb2",
    slash: "ProgressCount_slash_ac34047e",
    slash__fullWidth: "ProgressCount_slash__fullWidth_c807c2b",
    current: "ProgressCount_current_6cb06e0d",
    current__slashCenter: "ProgressCount_current__slashCenter_6ce420af",
    total: "ProgressCount_total_faa00922",
    total__slashCenter: "ProgressCount_total__slashCenter_bb7952a3",
  },
  Ke = "fullWidth",
  Ze = y.resolve("intl"),
  es = (0, Xe.memo)(function ({
    current: e,
    total: s,
    children: i,
    displayType: t = Ke,
    className: o,
    classNames: r,
  }) {
    return (0, ke.jsxs)("div", {
      className: n(Je.base, o),
      children: [
        (0, ke.jsx)("div", {
          className: n(Je.current, Je[`current__${t}`], r?.current),
          children: i ?? Ze.formatNumber("integral", e),
        }),
        (0, ke.jsx)("div", { className: n(Je.slash, Je[`slash__${t}`], r?.slash), children: "/" }),
        (0, ke.jsx)("div", {
          className: n(Je.total, Je[`total__${t}`], r?.total),
          children: Ze.formatNumber("integral", s),
        }),
      ],
    });
  }),
  ss = "Index_f505a04a",
  is = (0, Xe.memo)(function (e) {
    return (0, ke.jsx)(V, { ...e, classNames: { background: ss } });
  }),
  ts = (function (e) {
    return (
      (e.PROGRESSION = "progression"),
      (e.PM3_POINTS = "pm3_points"),
      (e.CUSTOM_SIMPLE = "custom_simple"),
      e
    );
  })({}),
  os = y.resolve("strings");
function rs(e) {
  return (0, ke.jsx)(se, {
    ...l({
      header: os.readOrEmpty(`personal_missions_30.detail.name.${e.id}`),
      body: os
        .readOrEmpty("user_missions.hub.basic_missions.personal.detail.tooltip.body")
        .replace("{{vehicleName}}", e.vehicleName),
    }),
    path: `personal_missions_30.vehicle_detail.c_400x150.${e.id}`,
    width: 150,
    height: 75,
    className: e.className,
  });
}
var as = {
    base: "InProgress_a9a08feb",
    base__inProgress: "InProgress_base__inProgress_1f5a0708",
    textBlock: "InProgress_textBlock_9bd89594",
    base__inProgressForHonors: "InProgress_base__inProgressForHonors_68457abb",
    title: "InProgress_title_f07812d0",
    description: "InProgress_description_802491c1",
    progress: "InProgress_progress_523f308d",
    points: "InProgress_points_9ee62ee",
    container: "InProgress_container_fb690b6c",
    detail: "InProgress_detail_da841dde",
    progressBar: "InProgress_progressBar_fc1f13a5",
  },
  ns = y.resolve("views"),
  ls = L(function () {
    const { model: e, controls: s } = Ne(),
      {
        state: i,
        totalProgress: t,
        currentProgress: o,
        previousProgress: r,
        detailId: a,
        vehicleName: l,
      } = e.get(),
      c = m(
        ts.PM3_POINTS,
        (0, Xe.useMemo)(
          () => ({
            resId: ns.read((e) => e.mono.personal_missions_30.tooltips.param_tooltip("resId")),
          }),
          [],
        ),
      );
    return (0, ke.jsxs)("div", {
      className: n(as.base, as[`base__${i}`]),
      children: [
        (0, ke.jsx)(Oe, {
          className: as.textBlock,
          classNames: { title: as.title, description: as.description },
        }),
        i === ye.IN_PROGRESS
          ? (0, ke.jsxs)(ke.Fragment, {
              children: [
                (0, ke.jsxs)("div", {
                  className: as.progress,
                  children: [
                    (0, ke.jsx)(es, { current: o, total: t }),
                    (0, ke.jsx)("div", { ...c, className: as.points }),
                  ],
                }),
                (0, ke.jsxs)("div", {
                  className: as.container,
                  children: [
                    (0, ke.jsx)(rs, { id: a, vehicleName: l, className: as.detail }),
                    (0, ke.jsx)(is, {
                      value: o,
                      size: "full",
                      maxValue: t,
                      className: as.progressBar,
                      children: (0, ke.jsx)($, { initValue: r, initMaxValue: t }),
                    }),
                  ],
                }),
              ],
            })
          : (0, ke.jsx)(oe, {
              path: "user_missions.hub.basic_missions.personal.progress.inProgressForHonors",
              params: { progress: (0, ke.jsx)(es, { current: o, total: t }) },
              className: as.progress,
            }),
        (0, ke.jsx)(Me, {
          theme: "secondary",
          onClick: s.goToOperation,
          textPath: "user_missions.hub.basic_missions.personal.button.to_operation",
        }),
      ],
    });
  }),
  cs = "PersonalMissions_background_cee2473a",
  ds = "PersonalMissions_d479b157",
  ms = (e, s, i, t) => {
    const o = "userMissions.personal_missions.backgrounds";
    switch (e) {
      case ye.IN_PROGRESS:
      case ye.IN_PROGRESS_FOR_HONORS:
        return `${o}.op_${i}`;
      case ye.COMPLETED_WITH_HONORS:
        return `${o}.${s ? "completed" : `op_${t}`}`;
      case ye.COMPLETED:
        return `${o}.op_${t}`;
      default:
        return `${o}.campaign`;
    }
  },
  us = L(function (e) {
    const { model: s } = Ne(),
      { state: i, allOperationsCompleted: t, currentOperationId: o, nextOperationId: r } = s.get();
    return (0, ke.jsxs)(Z, {
      className: n(ds, e.className),
      disableMouse: !0,
      children: [
        (0, ke.jsx)(se, {
          path: ms(i, t, o, r),
          width: "auto",
          height: "auto",
          fit: "cover",
          className: cs,
        }),
        (() => {
          switch (i) {
            case ye.CAMPAIGN_NOT_ACTIVATED:
              return (0, ke.jsx)(De, {});
            case ye.IN_PROGRESS:
            case ye.IN_PROGRESS_FOR_HONORS:
              return (0, ke.jsx)(ls, {});
            case ye.COMPLETED:
              return (0, ke.jsx)(He, {});
            case ye.COMPLETED_WITH_HONORS:
              return (0, ke.jsx)(Ye, {});
            default:
              console.error(`Unknown personal missions state ${i}`);
          }
        })(),
      ],
    });
  }),
  [_s, ps] = E()(
    ({ observableModel: e }) => ({
      ...e.primitives(["updateWeekDay"]),
      missions: e.transform(
        (e) =>
          H(e).map((e) => ({
            ...e,
            specConditions: be(e.specialConditionIds),
            rerollAvailableTimestamp: pe(me(), M(e.timeToNextReroll)),
          })),
        "missionsList",
      ),
    }),
    ({ externalModel: e }) => ({ reroll: e.createCallback((e) => ({ questId: e }), "onReroll") }),
  ),
  gs = (0, Xe.createContext)(null),
  fs = () => {
    const e = (0, Xe.useContext)(gs);
    if (!e) throw new Error("useAnimation must be used within an AnimationProvider");
    return e;
  },
  xs = L(function ({ completed: e, rerollState: s, children: i }) {
    const [t, o] = (0, Xe.useState)(!1),
      r = a(),
      [n, l] = b(() => ({ from: { x: 0 } })),
      [c, m] = b(() => ({ from: { x: 0 } })),
      [_, p] = b(() => ({ from: { x: 0 } })),
      [g, f] = b(() => ({ from: { opacity: e ? 0.5 : 1 } })),
      [x, h] = b(() => ({ from: { opacity: "in" === s ? 1 : 0 } })),
      [C, v] = u(3, (e) => ({
        from:
          "in" === s
            ? { transform: "translateY(-30rem)", opacity: 0 }
            : { transform: "translateY(0rem)", opacity: 1 },
      })),
      [N, y] = b(() => ({ from: { opacity: e || "in" === s ? 0 : 1 } })),
      [I, j] = b(() => ({ from: { transform: "rotate(0deg)" } })),
      k = (e) => {
        (o(!0), Promise.all(e.flat()).then(() => o(!1)));
      },
      M = w(() => {
        k([
          l.start({ to: { x: 1 }, config: { duration: 1500, easing: d.easeInOutCubic } }),
          p.start({ to: { x: 1 }, config: { duration: 800 } }),
          m.start({ to: { x: 1 }, config: { duration: 1500, easing: d.easeInOutCubic } }),
          y.start({ to: { opacity: 0 }, config: { duration: 400, easing: d.easeInCubic } }),
          f.start({ to: { opacity: 0.5 }, config: { duration: 200, easing: d.easeInCubic } }),
        ]);
      }),
      R = w(() => {
        k([
          j.start({ to: { transform: "rotate(360deg)" }, config: { duration: 400 }, loop: !0 }),
          v.start((e) => ({
            to: { transform: "translateY(30rem)", opacity: 0 },
            delay: 50 * (3 - e),
            config: { duration: 250, easing: d.easeInQuint },
          })),
          h.start({
            to: { opacity: 1 },
            config: { duration: 300, easing: d.easeInQuint },
            delay: 100,
          }),
        ]);
      }),
      E = w(() => {
        k([
          v.start((e) => ({
            to: { transform: "translateY(0rem)", opacity: 1 },
            config: { duration: 300, easing: d.easeOutQuint },
            delay: 50 * e,
          })),
          h.start({
            to: { opacity: 0 },
            config: { duration: 300, easing: d.easeOutQuint },
            delay: 100,
          }),
          y.start({ to: { opacity: 1 }, config: { duration: 100 }, delay: 300 }),
        ]);
      });
    return (
      (0, Xe.useEffect)(() => {
        switch (s) {
          case "in":
            return E();
          case "out":
            return (r.play(xe.umg_hub_quest_reroll), R());
          case "waiting":
            return void j.start({
              to: { transform: "rotate(360deg)" },
              config: { duration: 400 },
              loop: !0,
            });
          default:
            j.set({ transform: "rotate(0deg)" });
        }
      }, [E, R, j, s, r]),
      (0, ke.jsx)(gs.Provider, {
        value: {
          completedGlowStyle: n,
          completedBlickContainerStyle: c,
          completedBlickStyle: _,
          completedFadingStyle: g,
          rerollingSprings: C,
          rerollIconStyle: I,
          rerollButtonStyle: N,
          rerollGlowStyle: x,
          playCompletion: M,
          inProgress: t,
        },
        children: i,
      })
    );
  }),
  hs = "CompletionEffects_c32f942",
  bs = "CompletionEffects_glow_3093d825",
  Cs = "CompletionEffects_glowIcon_1b3d9ffe",
  vs = "CompletionEffects_blick_eedba3f2",
  Ns = "CompletionEffects_blickLines_9288dfea",
  ys = "CompletionEffects_blickLine_12f1a3a3";
function Is() {
  const e = fs();
  return (0, ke.jsxs)("div", {
    className: hs,
    children: [
      (0, ke.jsx)(Y.div, {
        style: { opacity: e.completedGlowStyle.x.to([0, 0.05, 1], [0, 1, 0]).to((e) => e) },
        className: bs,
        children: (0, ke.jsx)("div", { className: Cs }),
      }),
      (0, ke.jsx)(Y.div, {
        style: {
          opacity: e.completedBlickContainerStyle.x.to([0, 0.3, 1], [0, 1, 0]).to((e) => e),
        },
        className: vs,
        children: (0, ke.jsxs)(Y.div, {
          style: {
            transform: e.completedBlickStyle.x
              .to([0, 1], [-100, 100])
              .to((e) => `translateX(${e}%)`),
            opacity: e.completedBlickStyle.x.to([0, 0.1, 0.6, 1], [1, 1, 0, 0]).to((e) => e),
          },
          className: Ns,
          children: [
            (0, ke.jsx)("div", { className: ys }),
            (0, ke.jsx)("div", { className: ys }),
            (0, ke.jsx)("div", { className: ys }),
          ],
        }),
      }),
    ],
  });
}
var js = "SpecConditionsIcons_ab3f13c7",
  ks = "SpecConditionsIcons_icon_d767e7b4";
function Ms({ specConditions: e, className: s, ...i }) {
  return (0, ke.jsx)("div", {
    ...i,
    className: n(js, s),
    children: ee(e, (e) =>
      (0, ke.jsx)(se, { width: 24, height: 24, path: e.iconPath, className: ks }, e.id),
    ),
  });
}
var Rs = (function (e) {
    return ((e.REROLL = "reroll"), (e.SPEC_CONDITIONS = "spec_conditions"), e);
  })({}),
  Es = "Conditions_specConditions_faac5c77",
  ws = "Conditions_commonCondition_72d62c0e";
y.resolve("aliases");
var Ss = y.resolve("views");
function Ps({ commonConditionId: e, specConditions: s }) {
  const t = fs(),
    o = m(
      Rs.SPEC_CONDITIONS,
      (0, Xe.useMemo)(
        () => ({
          specConditions: s,
          resId: Ss.read((e) => e.mono.user_missions.tooltips.param_tooltip("resId")),
        }),
        [s],
      ),
    );
  return (0, ke.jsxs)(Y.div, {
    style: t.rerollingSprings[0],
    children: [
      s.length > 0 && (0, ke.jsx)(Ms, { ...o, specConditions: s, className: Es }),
      (0, ke.jsx)(i, { text: he(e, s), classMix: ws, isTruncationAvailable: !0 }),
    ],
  });
}
var Bs = "Icon_animatedIcon_96d2a89c",
  Os = "Icon_f61225ad";
function Ts({ completed: e, commonConditionId: s, className: i }) {
  const t = fs(),
    o = x(
      {
        completedIcon: "userMissions.hub.basic.done_icon_s",
        missionIcon: `userMissions.weekly.commonCond.x32x32.c_${s}`,
      },
      {
        medium: {
          completedIcon: "userMissions.hub.basic.done_icon_m",
          missionIcon: `userMissions.weekly.commonCond.x80x80.c_${s}`,
        },
      },
    ),
    r = g(e, {
      initial: { opacity: e ? 1 : 0.2, scale: 1 },
      from: { opacity: 0, scale: 0.2 },
      enter: { opacity: e ? 1 : 0.2, scale: 1, config: { duration: 200, easing: d.easeOutCubic } },
      leave: { opacity: 0, scale: 0.2, config: { duration: 200, easing: d.easeInCubic } },
      exitBeforeEnter: !0,
    });
  return (0, ke.jsx)("div", {
    className: n(Os, i),
    children: (0, ke.jsx)(Y.div, {
      style: t.rerollingSprings[0],
      children: r((e, s) =>
        (0, ke.jsx)(Y.div, {
          style: e,
          className: Bs,
          children: (0, ke.jsx)(se, {
            path: s ? o.completedIcon : o.missionIcon,
            width: 32,
            height: 32,
            adaptive: { medium: { width: 80, height: 80 } },
          }),
        }),
      ),
    }),
  });
}
var As = Xe.memo(function (e) {
    return (0, ke.jsx)(is, {
      size: "small",
      value: e.currentProgress,
      maxValue: e.totalProgress,
      children: (0, ke.jsx)($, {
        initValue: e.previousProgress,
        initMaxValue: e.totalProgress,
        animationProps: e.animationProps,
      }),
    });
  }),
  Ls = "Reroll_9aa89152",
  Ds = "Reroll_button_bf3e46bd",
  Ws = "Reroll_text_f15ae95",
  Fs = "Reroll_icon_9cea8d59",
  Hs = "Reroll_timer_9c3c15fe",
  Gs = "Reroll button",
  Vs = y.resolve("strings"),
  qs = y.resolve("views");
function $s({
  rerollCooldown: e,
  rerollAvailableTimestamp: s,
  timeToNextReroll: i,
  onClick: t,
  className: o,
}) {
  const r = a(),
    l = X((0, Xe.useMemo)(() => ({ until: s, tick: M(1) }), [s])),
    { rerollButtonStyle: d, rerollIconStyle: u } = fs(),
    _ = m(
      Rs.REROLL,
      (0, Xe.useMemo)(
        () => ({
          rerollCooldown: e,
          rerollAvailableTimestamp: ce(s),
          resId: qs.read((e) => e.mono.user_missions.tooltips.param_tooltip("resId")),
        }),
        [e, s],
      ),
    );
  return (0, ke.jsx)(Y.div, {
    ..._,
    style: d,
    className: n(Ls, o),
    children: l.done
      ? (0, ke.jsxs)("div", {
          onClick: () => {
            (r.play("click", { target: Gs }), t());
          },
          onMouseEnter: () => {
            r.play("mouse-enter", { target: Gs });
          },
          className: Ds,
          children: [
            (0, ke.jsx)("div", {
              className: Ws,
              children: Vs.readOrEmpty("user_missions.hub.basic_missions.daily.reroll_button"),
            }),
            (0, ke.jsx)(Y.div, { style: u, className: Fs }),
          ],
        })
      : (0, ke.jsx)(c, {
          start: i,
          format: c.format.superCompact,
          size: c.size.x24x24,
          className: Hs,
        }),
  });
}
var zs = "Rewards_rewardItem_5e36a95a",
  Us = "Rewards_boxRewardClassName_f0825900",
  Qs = y.resolve("aliases");
function Ys(e) {
  const s = x(
    { rewardSize: ge.S24x24, rewardMaxCount: 4 },
    { large: { rewardSize: ge.Small, rewardMaxCount: 5 } },
  );
  return (0, ke.jsx)(Ce, {
    bonuses: e.bonuses,
    questId: e.id,
    size: s.rewardSize,
    resId: Qs.read((e) => e.user_missions.hub.basicMissions.WeeklyMissions("resId")),
    count: e.bonuses.length <= s.rewardMaxCount ? s.rewardMaxCount : s.rewardMaxCount - 1,
    rewardItemClassMix: zs,
    boxRewardClassName: Us,
  });
}
var Xs = "Mission_557cf0dd",
  Js = "Mission_base__animating_f1a3e9cd",
  Ks = "Mission_rerollGlow_a0c30a93",
  Zs = "Mission_wrapper_9f0c513c",
  ei = "Mission_icon_3808d908",
  si = "Mission_content_238fdcb6",
  ii = "Mission_conditions_c4d5bc79",
  ti = "Mission_rightContent_e710873a",
  oi = "Mission_reroll_15a6d836",
  ri = "Mission_reroll__noEvents_f1a3e9cd",
  ai = "Mission_progressBarWrapper_5877296e",
  ni = L(function ({
    bonuses: e,
    commonConditionId: s,
    currentProgress: i,
    id: t,
    previousProgress: o,
    specConditions: r,
    isRerollInProgress: l,
    timeToNextReroll: c,
    rerollAvailableTimestamp: d,
    rerollCooldown: m,
    totalProgress: u,
    className: _,
  }) {
    const { controls: p } = ps(),
      g = a(),
      f = fs(),
      [x, h] = (0, Xe.useState)(o === u),
      { playCompletion: b } = f,
      C = (0, Xe.useMemo)(
        () => ({
          onStart: () => {
            g.play(xe.umg_hub_quest_progress);
          },
          onRest: () => {
            i === u && (g.play(xe.umg_hub_quest_complete), b(), h(!0));
          },
        }),
        [i, u, g, b],
      );
    return (0, ke.jsxs)("div", {
      className: n(Xs, f.inProgress && Js, _),
      children: [
        (0, ke.jsx)(Is, {}),
        (0, ke.jsx)(Y.div, { style: f.rerollGlowStyle, className: Ks }),
        (0, ke.jsxs)("div", {
          className: Zs,
          children: [
            (0, ke.jsxs)("div", {
              className: si,
              children: [
                (0, ke.jsxs)("div", {
                  className: ii,
                  children: [
                    (0, ke.jsx)(Ts, { completed: x, commonConditionId: s, className: ei }),
                    (0, ke.jsxs)(Y.div, {
                      style: f.completedFadingStyle,
                      children: [
                        (0, ke.jsx)(Ps, { commonConditionId: s, specConditions: r }),
                        (0, ke.jsx)(Y.div, {
                          style: f.rerollingSprings[1],
                          children: (0, ke.jsx)(es, { current: i, total: u }),
                        }),
                      ],
                    }),
                  ],
                }),
                (0, ke.jsxs)(Y.div, {
                  style: f.completedFadingStyle,
                  className: ti,
                  children: [
                    (0, ke.jsx)($s, {
                      rerollCooldown: m,
                      rerollAvailableTimestamp: d,
                      timeToNextReroll: c,
                      onClick: () => p.reroll(t),
                      className: n(oi, (i === u || l) && ri),
                    }),
                    (0, ke.jsx)(Y.div, {
                      style: f.rerollingSprings[2],
                      children: (0, ke.jsx)(Ys, { bonuses: e, id: t }),
                    }),
                  ],
                }),
              ],
            }),
            (0, ke.jsx)(Y.div, {
              style: f.completedFadingStyle,
              children: (0, ke.jsx)(Y.div, {
                style: f.rerollingSprings[2],
                children: (0, ke.jsx)("div", {
                  className: ai,
                  children: (0, ke.jsx)(As, {
                    previousProgress: o,
                    currentProgress: i,
                    totalProgress: u,
                    animationProps: C,
                  }),
                }),
              }),
            }),
          ],
        }),
      ],
    });
  }),
  li = "WeeklyMissions_b5c4ab0c",
  ci = "WeeklyMissions_base__fullHeight_1393a178",
  di = "WeeklyMissions_list_ef7648a3",
  mi = "WeeklyMissions_title_eeb41405",
  ui = "WeeklyMissions_title__right_82a872e3",
  _i = L(function (e) {
    const { model: s } = ps(),
      i = s.missions.get(),
      t = (0, Xe.useRef)(i);
    (0, Xe.useEffect)(() => {
      t.current = i;
    }, [i]);
    const o = (0, Xe.useMemo)(() => {
        const e = new Set(),
          s = new Set();
        return (
          U(t.current, (t, o) => {
            const r = D(i, o);
            r && r.id !== t.id && (e.add(t.id), s.add(r.id));
          }),
          { rerolledIds: e, newIds: s }
        );
      }, [i]),
      r = g(i, {
        key: (e) => e.id,
        initial: { x: 1 },
        from: { x: 0 },
        enter: { x: 1 },
        leave: { x: 0, config: { duration: 600 } },
        exitBeforeEnter: !0,
      });
    return (0, ke.jsxs)(Z, {
      className: n(li, e.fullHeight && ci, e.className),
      disableMouse: !0,
      children: [
        (0, ke.jsx)(oe, { className: mi, path: "user_missions.hub.basic_missions.weekly.title" }),
        (0, ke.jsx)(oe, {
          className: n(mi, ui),
          path: "user_missions.hub.basic_missions.weekly.update_info",
          params: {
            weekDay: y
              .resolve("strings")
              .readOrEmpty(`menu.dateTime.weekDays.full.c_${s.updateWeekDay.get()}`),
          },
        }),
        (0, ke.jsx)("div", {
          className: di,
          children: r((e, s) =>
            (0, ke.jsx)(xs, {
              completed: s.previousProgress === s.totalProgress,
              rerollState: (() => {
                switch (!0) {
                  case o.rerolledIds.has(s.id):
                    return "out";
                  case o.newIds.has(s.id):
                    return "in";
                  case s.isRerollInProgress:
                    return "waiting";
                  default:
                    return "idle";
                }
              })(),
              children: (0, ke.jsx)(ni, { ...s }),
            }),
          ),
        }),
      ],
    });
  }),
  pi = "DisabledState_4abbc2ea",
  gi = "DisabledState_background_2be33fab",
  fi = "DisabledState_content_29454c97",
  xi = "DisabledState_icon_58468d38",
  hi = "DisabledState_message_90090227";
function bi({ message: e }) {
  return (0, ke.jsxs)("div", {
    className: pi,
    children: [
      (0, ke.jsx)("div", { className: gi }),
      (0, ke.jsxs)("div", {
        className: fi,
        children: [
          (0, ke.jsx)("div", { className: xi }),
          (0, ke.jsx)("div", { className: hi, children: e }),
        ],
      }),
    ],
  });
}
var Ci = "Block_content_7290bea6";
function vi({ content: e, isEnabled: s, disabilityReason: i, className: t }) {
  return (0, ke.jsx)(Z, {
    className: t,
    disableMouse: !0,
    children: s
      ? (0, ke.jsx)("div", { className: Ci, children: e })
      : (0, ke.jsx)(bi, { message: i }),
  });
}
var Ni = (0, Xe.createContext)(null);
function yi() {
  const e = (0, Xe.useContext)(Ni);
  return (O(null !== e, "AnimationsContext is null"), e);
}
function Ii() {
  return (0, Xe.useContext)(Ni);
}
function ji(e, s, i = e) {
  return e + "+" + s + "+" + i;
}
function ki(e, s, ...i) {
  let t = e.current;
  if (0 == i.length) return !1;
  for (let o = 0; o < i.length - 1; o++) {
    const e = i[o];
    ((t[e] = t[e] ?? {}), (t = t[e]));
  }
  return ((t[i[i.length - 1]] = s), !0);
}
function Mi(e, ...s) {
  const i = (e, t) => {
    if (t === s.length) return ae(e);
    const o = s[t];
    return o in e && ((t === s.length - 1 || i(e[o], t + 1)) && delete e[o], ae(e));
  };
  return i(e.current, 0);
}
function Ri(e, ...s) {
  let i = e.current;
  return s.reduce((e, s) => e?.[s], i);
}
function Ei(e, ...s) {
  let i = e.current;
  return void 0 !== s.reduce((e, s) => e?.[s], i);
}
function wi(e, s, i, t) {
  Object.entries(s).forEach(([s, o]) => {
    ae(o)
      ? Ei(i, e, s, e) && t(s, e)
      : Object.entries(o).forEach(([o, r]) => {
          const a = o || e;
          Ei(i, e, s, a) && t(s, a, r);
        });
  });
}
function Si({ storage: e, id: s, emitter: i, providerCfg: t }) {
  Ei(e, s) || Pi({ id: s, emitter: i, providerCfg: t });
}
function Pi({ id: e, emitter: s, providerCfg: i }) {
  const t = i?.triggerId || e;
  (s.trigger(t, { id: e, ...i?.triggerParams }),
    i?.triggerCallback?.({ id: e, ...i?.triggerParams }));
}
function Bi({ sound: e, soundCfg: s }) {
  e && s && ("string" == typeof s ? e.play(s) : e.play(s.eventName, s?.event));
}
function Oi({ children: e }) {
  const s = P(),
    i = (0, Xe.useRef)({}),
    t = (0, Xe.useRef)({}),
    o = (0, Xe.useRef)({}),
    r = de(),
    a = w(({ id: e, animName: s, elementId: t = e }) => Ei(i, e, s, t)),
    n = w((e, s, t = e) => {
      Mi(i, e, s, t);
    }),
    l = w(
      ({ id: e, animName: s, config: t, elementId: o = e }) => (
        ki(i, t, e, s, o),
        () => n(e, s, o)
      ),
    ),
    c = w(
      ({
        id: e,
        animName: s,
        elementId: t = e,
        animCallParams: o,
        providerCfg: a,
        soundCfg: n,
      }) => {
        const l = Ri(i, e, s, t);
        (l &&
          (a?.skip
            ? l.skip({ ...o, ...a?.animCallParams })
            : l.start({ ...o, ...a?.animCallParams })),
          Bi({ sound: r, soundCfg: n }));
      },
    ),
    d = w(({ id: e, animName: i, elementId: o = e, providerCfg: r = {} }) => {
      const a = s.on(ji(e, i, o), () => {
        (Mi(t, e, i, o), Si({ storage: t, id: e, emitter: s, providerCfg: r }), a());
      });
      ki(t, !0, e, i, o);
    }),
    m = w(({ complexId: e, id: i, animName: t, elementId: r = i, providerCfg: a }) => {
      const n = s.on(ji(i, t, r), function () {
          (!(function ({
            storage: e,
            complexId: s,
            groupId: i,
            animName: t,
            elementId: o,
            emitter: r,
            providerCfg: a,
          }) {
            let n = Ri(e, s, i, t);
            n &&
              (n.delete(o),
              n.size || Mi(e, s, i, t),
              Si({ storage: e, id: s, emitter: r, providerCfg: a }));
          })({
            storage: o,
            complexId: e,
            groupId: i,
            animName: t,
            elementId: r,
            emitter: s,
            providerCfg: a,
          }),
            n());
        }),
        l = Ri(o, e, i, t);
      l ? l.add(r) : ki(o, new Set().add(r), e, i, t);
    }),
    u = w(({ groupId: e, groupCfg: o, providerCfg: a, soundCfg: n }) => {
      (Mi(t, e),
        a?.skip ||
          a?.skipTrigger ||
          wi(e, o, i, (s, i) => {
            d({ id: e, animName: s, elementId: i, providerCfg: a });
          }),
        wi(e, o, i, (s, i, t) => {
          c({ id: e, animName: s, elementId: i, animCallParams: t, providerCfg: a });
        }),
        Bi({ sound: r, soundCfg: n }),
        a?.skip && !a?.skipTrigger && Pi({ id: e, emitter: s, providerCfg: a }));
    }),
    _ = w(({ complexId: e, complexCfg: t, providerCfg: a, soundCfg: n }) => {
      if ((Mi(o, e), !a?.skip && !a?.skipTrigger))
        for (let [s, o] of Object.entries(t))
          wi(s, o, i, (i, t) => {
            m({ complexId: e, id: s, animName: i, elementId: t, providerCfg: a });
          });
      for (let [s, o] of Object.entries(t))
        wi(s, o, i, (e, i, t) => {
          c({ id: s, animName: e, elementId: i, animCallParams: t, providerCfg: a });
        });
      (Bi({ sound: r, soundCfg: n }),
        a?.skip && !a?.skipTrigger && Pi({ id: e, emitter: s, providerCfg: a }));
    }),
    p = (0, Xe.useMemo)(
      () => ({
        registerAnimation: l,
        unRegistrateAnimation: n,
        startAnimation: c,
        startGroupAnimation: u,
        startComplexAnimation: _,
        checkRegisteredInStorage: a,
        emitter: s,
      }),
      [a, s, l, c, _, u, n],
    );
  return (0, ke.jsx)(Ni.Provider, { value: p, children: e });
}
var [Ti, Ai] = E()(
  ({ observableModel: e }) => {
    const s = {
        ...e.primitives(["timeToNextRerol", "areAllMissionsCompleted", "timeToMissionsUpdate"]),
        missionsList: e.arrayClone("missionsList"),
        bonusMission: e.object("bonusMission"),
        bonusMissionBonuses: e.arrayClone("bonusMission.bonuses"),
      },
      i = ue.model((e) => {
        const i = s.bonusMission.get();
        if (e == i.id) return i;
        const t = s.missionsList.get();
        return te(t, (s) => s.id == e);
      }),
      t = ue.model(() => s.missionsList.get().some(({ animateCompletion: e }) => e));
    return { ...s, computes: { missionById: i, isAnyCompleteAnimation: t } };
  },
  ({ externalModel: e }) => ({ onReroll: e.createCallback((e) => ({ questId: e }), "onReroll") }),
);
function Li({ registerAnimation: e, id: s, animName: i, elementId: t = s, config: o }) {
  (0, Xe.useLayoutEffect)(
    () => e?.({ id: s, animName: i, elementId: t, config: o }),
    [s, i, o, t, e],
  );
}
var Di = {
    from: { opacity: 0 },
    to: async (e) => {
      (await e({ opacity: 1, config: { duration: 175 } }),
        await e({ opacity: 0, config: { duration: 800 } }));
    },
  },
  Wi = {
    from: { opacity: 0 },
    to: async (e) => {
      (await e({ opacity: 0.5 }), await e({ opacity: 0 }));
    },
    config: { duration: 400 },
  };
function Fi(e = Gi.GREY_LENSE, s) {
  const i = C(),
    t = ((e) => {
      switch (e) {
        case Gi.GREEN:
          return Di;
        case Gi.GREEN_LENSE:
        case Gi.GREY_LENSE:
          return Wi;
        default:
          return Di;
      }
    })(e),
    o = w(() => s?.()),
    r = w(() => {
      i.start({ onRest: o, ...t, reset: !0 });
    }),
    a = w(() => {
      i.start({ to: { opacity: 0 }, reset: !0, immediate: !0 });
    }),
    n = b({ ref: i, onRest: o, ...t });
  return (0, Xe.useMemo)(() => ({ glowStyle: n, config: { start: r, skip: a } }), [n, a, r]);
}
var Hi = {
    base: "Glow_95d62d77",
    icon: "Glow_icon_d88e8512",
    icon__greyLense: "Glow_icon__greyLense_4150ede3",
  },
  Gi = { GREEN: "green", GREEN_LENSE: "greenLense", GREY_LENSE: "greyLense" },
  Vi = { path: "", width: 250, height: 250 },
  qi = {
    [Gi.GREEN]: {
      path: "userMissions.hub.animations.glow_green_1200x800",
      width: 1200,
      height: 800,
    },
    [Gi.GREEN_LENSE]: {
      path: "userMissions.hub.animations.glow_lens_green_250x250",
      width: 250,
      height: 250,
    },
    [Gi.GREY_LENSE]: {
      path: "userMissions.hub.animations.glow_lens_grey_250x250",
      width: 250,
      height: 250,
    },
  },
  $i = (e) => (qi[e] ? qi[e] : Vi),
  zi = "glow";
var Ui = (0, Xe.memo)(function ({ id: e, elementId: s, className: i, glowType: t = Gi.GREEN }) {
  const o = Ii(),
    { glowStyle: r, config: a } = Fi(
      t,
      w(() => o?.emitter.trigger(ji(e, zi, s), e, s)),
    );
  return (
    Li({ id: e, elementId: s, registerAnimation: o?.registerAnimation, animName: zi, config: a }),
    (0, ke.jsx)(Y.div, {
      style: r,
      className: n(Hi.base, i),
      children: (0, ke.jsx)(se, { ...$i(t), className: n(Hi.icon, Hi[`icon__${t}`]) }),
    })
  );
});
function Qi(e, s) {
  const i = I(e, { onRest: w(() => s?.()) }),
    t = w((e) => {
      e?.to != i.get() ? i.start({ ...e }) : s?.();
    }),
    o = w((e) => {
      i.start({ ...e, delay: 0, immediate: !0, config: { duration: 0 } });
    });
  return (0, Xe.useMemo)(() => ({ opacity: i, config: { start: t, skip: o } }), [i, o, t]);
}
var Yi = "opacity";
var Xi = (0, Xe.memo)(function ({ id: e, from: s, className: i, elementId: t, children: o, ...r }) {
    const a = Ii(),
      { opacity: n, config: l } = Qi(
        s,
        w(() => a?.emitter.trigger(ji(e, Yi, t), e, t)),
      );
    return (
      Li({ id: e, elementId: t, registerAnimation: a?.registerAnimation, animName: Yi, config: l }),
      o ? (0, ke.jsx)(Y.div, { style: { opacity: n }, className: i, ...r, children: o }) : null
    );
  }),
  Ji = {
    from: { opacity: 0 },
    to: async (e) => {
      (await e({ opacity: 0.5, config: { duration: 180 } }),
        await e({ opacity: 0, config: { duration: 420 } }));
    },
  },
  Ki = {
    from: { transform: "translateX(-100%)" },
    to: { transform: "translateX(100%)" },
    config: { duration: 600 },
  };
var Zi = "Reflection_7a45ed9c",
  et = "Reflection_bg_5a5ee806",
  st = "Reflection_lines_container_58665661",
  it = "Reflection_line_1_fc841d05",
  tt = "Reflection_line_2_10b982d",
  ot = "Reflection_line_3_43ed32ee",
  rt = "reflection";
var at = (0, Xe.memo)(function ({ id: e, elementId: s, className: i }) {
    const { registerAnimation: t, emitter: o } = yi(),
      {
        bgStyle: r,
        linesStyle: a,
        config: l,
      } = (function (e) {
        const s = C(),
          i = C(),
          t = (0, Xe.useRef)(0),
          o = w(() => {
            ((t.current += 1), 2 == t.current && ((t.current = 0), e?.()));
          }),
          r = w(() => {
            (s.start({ ...Ji, onRest: o, reset: !0 }), i.start({ ...Ki, onRest: o, reset: !0 }));
          }),
          a = w(() => {
            (s.start({ to: { opacity: 0 }, immediate: !0 }), i.start({ ...Ki, immediate: !0 }));
          }),
          n = b({ ref: s, onRest: o, ...Ji }),
          l = b({ ref: i, onRest: o, ...Ki });
        return (0, Xe.useMemo)(
          () => ({ bgStyle: n, linesStyle: l, config: { start: r, skip: a } }),
          [n, l, a, r],
        );
      })(w(() => o.trigger(ji(e, rt, s), e, s)));
    return (
      Li({ id: e, elementId: s, registerAnimation: t, animName: rt, config: l }),
      (0, ke.jsx)("div", {
        className: n(Zi, i),
        children: (0, ke.jsx)(Y.div, {
          style: r,
          className: et,
          children: (0, ke.jsxs)(Y.div, {
            style: a,
            className: st,
            children: [
              (0, ke.jsx)("div", { className: it }),
              (0, ke.jsx)("div", { className: tt }),
              (0, ke.jsx)("div", { className: ot }),
            ],
          }),
        }),
      })
    );
  }),
  nt = {
    from: { opacity: 0, transform: "scale(0.2)" },
    enter: { opacity: 1, transform: "scale(1)" },
    leave: { opacity: 0, transform: "scale(0.2)" },
    initial: { opacity: 1, transform: "scale(1)" },
  };
var lt = "swap";
var ct = (0, Xe.memo)(function ({ init: e = !1, id: s, elementId: i, className: t, children: o }) {
    const r = Ii(),
      { transitions: a, config: n } = (function (e, s) {
        const [i, t] = (0, Xe.useState)(e),
          o = (0, Xe.useRef)(!1),
          r = (0, Xe.useRef)(0),
          a = w((e) => {
            ((o.current = !1), i != Boolean(e?.state) ? t(Boolean(e?.state)) : s?.());
          }),
          n = w((e) => {
            ((o.current = !0), i != Boolean(e?.state) ? t(Boolean(e?.state)) : s?.());
          }),
          l = w(() => {
            ((r.current += 1), 2 == r.current && (s?.(), (r.current = 0)));
          }),
          c = g(i, { ...nt, onRest: l, immediate: o.current });
        return (0, Xe.useMemo)(
          () => ({ transitions: c, config: { start: a, skip: n } }),
          [c, a, n],
        );
      })(
        e,
        w(() => r?.emitter.trigger(ji(s, lt, i), s, i)),
      );
    return (
      Li({ id: s, elementId: i, registerAnimation: r?.registerAnimation, animName: lt, config: n }),
      o ? a((e, s) => (0, ke.jsx)(Y.div, { style: e, className: t, children: o[Number(s)] })) : null
    );
  }),
  [dt, mt] = E()(
    ({ observableModel: e }) => ({
      ...e.primitives(["targetQuestId"]),
      dailyMissionsBlockStatus: e.object("dailyMissionsBlockStatus"),
      premiumDailyMissionsBlockStatus: e.object("premiumDailyMissionsBlockStatus"),
      rewardProgressBlockStatus: e.object("rewardProgressBlockStatus"),
    }),
    ne,
  ),
  ut = "delta",
  _t = "condition",
  pt = "progress",
  gt = "missionIcon",
  ft = "reward",
  xt = "reRollHook",
  ht = "reRollComponent",
  bt = "reRollComponentIcon",
  Ct = "reRollComponentTimer",
  vt = "reRollComponentButton",
  Nt = { duration: 100, easing: (e) => -(Math.cos(Math.PI * e) - 1) / 2 },
  yt = { from: { opacity: 0, y: -G(10) }, to: { opacity: 1, y: 0 }, config: Nt },
  It = { from: { opacity: 1, y: 0 }, to: { opacity: 0, y: G(10) }, config: Nt };
function jt(e) {
  const s = C(),
    i = (0, Xe.useCallback)(() => e?.(), [e]),
    t = b({ ref: s, opacity: 1, y: 0, config: Nt, onRest: i }),
    o = w((e) => {
      e?.leave
        ? s.start({ ...It, ...e, onRest: i, reset: !0 })
        : s.start({ ...yt, ...e, onRest: i, reset: !0 });
    }),
    r = w((e) => {
      e?.leave
        ? s.start({ ...It, ...e, onRest: i, delay: 0, reset: !0, immediate: !0 })
        : s.start({ ...yt, ...e, onRest: i, delay: 0, reset: !0, immediate: !0 });
    });
  return (0, Xe.useMemo)(() => ({ styles: t, config: { start: o, skip: r } }), [t, o, r]);
}
var kt = "slideInOut";
var Mt = (0, Xe.memo)(function ({ id: e, elementId: s, className: i, children: t }) {
    const [o, r] = (0, Xe.useReducer)((e) => e + 1, 0),
      a = (0, Xe.useRef)(t),
      n = ji(e, kt, s),
      l = (0, Xe.useRef)(n),
      c = l.current == n,
      { registerAnimation: d, emitter: m } = yi(),
      { styles: u, config: _ } = jt(
        w(() => {
          ((l.current = n), m.trigger(ji(e, kt, s), e, s));
        }),
      );
    return (
      (0, Xe.useEffect)(() => {
        c && (a.current = t);
      }, [c, t]),
      Li({
        id: e,
        elementId: s,
        registerAnimation: d,
        animName: kt,
        config: {
          start: w((e) => {
            (r(), _.start(e));
          }),
          skip: w((e) => {
            (r(), _.skip(e));
          }),
        },
      }),
      c
        ? (0, ke.jsx)(Y.div, { style: u, className: i, children: t })
        : (0, Xe.isValidElement)(a.current) && a.current.props?.id && a.current.props?.id != e
          ? (0, ke.jsx)(Y.div, {
              style: u,
              className: i,
              children: (0, Xe.cloneElement)(a.current, { id: e }),
            })
          : (0, ke.jsx)(Y.div, { style: u, className: i, children: a.current })
    );
  }),
  Rt = "LOCKED_BLOCK",
  Et = "lockIcon",
  wt = "lockText",
  St = "glowLock",
  Pt = "baseCard",
  Bt = "lockBonusHook",
  Ot = "unlockBonusHook",
  Tt = {
    slideOut: {
      [kt]: {
        [gt]: { leave: !0, delay: 100 },
        [_t]: { leave: !0, delay: 80 },
        [pt]: { leave: !0, delay: 40 },
        [ft]: { leave: !0, delay: 20 },
      },
    },
    slideIn: {
      [kt]: {
        [gt]: { delay: 40 },
        [_t]: { delay: 60 },
        [pt]: { delay: 100 },
        [ft]: { delay: 120 },
      },
    },
  };
function At(e, s) {
  (0, Xe.useEffect)(() => {
    e || s();
  });
}
function Lt(e, s, i) {
  const { totalProgress: t, isCompleted: o, id: r } = s;
  o && !i.isCompleted && 0 == t && (e[r] = _o.missionComplete);
}
function Dt(e, s, i) {
  const { totalProgress: t, animateCompletion: o, isCompleted: r, id: a } = i;
  o ? 0 == t && (e[a] = _o.missionComplete) : r && (s[a] = _o.missionComplete);
}
var Wt = {
    [Yi]: {
      [Pt]: { to: 0, reset: !0, immediate: !0 },
      [Rt]: { to: 1, reset: !0, config: { duration: 300 } },
      [Et]: { to: 1, reset: !0, config: { duration: 300 } },
      [wt]: { to: 1, reset: !0, config: { duration: 300 } },
    },
  },
  Ft = "lockBonusAnim",
  Ht = "bonusSlideOut",
  Gt = "showLockComplete";
var Vt = {
  from: 0,
  to: 360,
  loop: !1,
  pause: !1,
  reset: !0,
  immediate: !1,
  config: { duration: 400 },
};
var qt = "rotate";
var $t = (0, Xe.memo)(function ({ id: e, className: s, elementId: i, props: t, children: o }) {
    const r = Ii(),
      a = w(() => r?.emitter.trigger(ji(e, qt, i), e, i)),
      { rotate: n, config: l } = (function (e) {
        const s = (0, Xe.useRef)(!1),
          i = w((e, i) => {
            s.current && i.stop().set(0);
          }),
          t = I(0, { ...Vt, pause: !0, ...e, onStart: i }),
          o = w((e) => {
            ((s.current = !1), t.start({ ...Vt, ...e, onStart: i }).then(ne));
          }),
          r = w((e) => {
            ((s.current = !0), t.stop().set(0));
          });
        return (0, Xe.useMemo)(() => ({ rotate: t, config: { start: o, skip: r } }), [t, r, o]);
      })(t),
      c = w((e) => {
        (l.start(e), e?.loop && a());
      }),
      d = w((e) => {
        (l.skip(e), a());
      });
    return (
      Li({
        id: e,
        animName: qt,
        elementId: i,
        registerAnimation: r?.registerAnimation,
        config: { start: c, skip: d },
      }),
      o ? (0, ke.jsx)(Y.div, { style: { rotate: n }, className: s, children: o }) : null
    );
  }),
  zt = {
    reRollSlideOut: { [qt]: { [bt]: { loop: !0 } }, ...Tt.slideOut },
    reRollSlideIn: { [Yi]: { [ht]: { to: 0, config: { duration: 100 } } }, ...Tt.slideIn },
    missionUnComplete: {
      [lt]: { "": { state: !1 } },
      [Yi]: { [_t]: { to: 1 }, [pt]: { to: 1 }, [ht]: { to: 1 }, [ft]: { to: 1 } },
    },
  },
  Ut = "useMissionChangedHook";
function Qt(e) {
  const { startGroupAnimation: s, registerAnimation: i, emitter: t } = yi(),
    o = xt,
    r = ji(`${e}_slideInComplete`, Ut, o),
    a = ji(`${e}_slideOutComplete`, Ut, o);
  (p(t, r, () => {
    t.trigger(ji(e, Ut, o), e, o);
  }),
    p(t, a, () => {
      (s({
        groupId: e,
        groupCfg: zt.missionUnComplete,
        providerCfg: { skip: !0, skipTrigger: !0 },
      }),
        setTimeout(() => {
          s({ groupId: e, groupCfg: zt.reRollSlideIn, providerCfg: { triggerId: r } });
        }, 400));
    }),
    Li({
      id: e,
      elementId: o,
      registerAnimation: i,
      animName: Ut,
      config: {
        start: w(() => {
          s({
            groupId: e,
            groupCfg: zt.reRollSlideOut,
            providerCfg: { triggerId: a },
            soundCfg: xe.umg_hub_quest_reroll,
          });
        }),
        skip: ne,
      },
    }));
}
var Yt = {
  missionChange: { [Ut]: { [xt]: {} } },
  hideReRollComponent: { [Yi]: { [ht]: { to: 0, config: { duration: 150 } } } },
  lockBonus: { [Ft]: { [Bt]: {} } },
};
function Xt(e, s, i) {
  const { id: t, currentProgress: o } = s;
  return !!(t != i.id || (0 == o && i.currentProgress)) && ((e[t] = Yt.missionChange), !0);
}
function Jt({ missions: e, bonusMission: s, timeToNextReRoll: i, isFirstRender: t }) {
  const { startComplexAnimation: o, startGroupAnimation: r } = yi(),
    a = _(e),
    n = _({ ...s });
  At(t, () => {
    const t = {},
      l = {};
    var c, d, m;
    (e.forEach((e, s) => {
      const i = a[s];
      Xt(t, e, i) || e.isLocked || (l[e.id] = Yt.hideReRollComponent);
    }),
      s.isAvailable && ((c = t), (d = s), "BONUS_CARD" != (m = n).id && Xt(c, d, m)),
      !s.isAvailable && n.isAvailable && r({ groupId: s.id, groupCfg: Yt.lockBonus }),
      ae(t) ||
        (i > 0 && o({ complexId: uo.HIDE_REROLL_COMPONENT, complexCfg: l }),
        o({ complexId: uo.RE_ROLL, complexCfg: t })));
  });
}
var Kt = {
  showReRollTimer: {
    [Yi]: {
      [Ct]: { to: 1, immediate: !0 },
      [vt]: { to: 0, immediate: !0 },
      [ht]: { to: 1, delay: 400, config: { duration: 200 } },
    },
    [qt]: { [bt]: { immediate: !0, pause: !0, loop: !1 } },
  },
  stopRotation: { [qt]: { [bt]: {} } },
  showReRollButton: {
    [Yi]: {
      [Ct]: { to: 0, immediate: !0 },
      [vt]: { to: 1, immediate: !0 },
      [ht]: { to: 1, delay: 400, config: { duration: 200 } },
    },
  },
};
function Zt(e, s) {
  return e.reduce((e, { id: i, isCompleted: t, isLocked: o }) => (t || o || (e[i] = s), e), {});
}
function eo(e, s) {
  return e.reduce((e, { id: i, isCompleted: t, isLocked: o }) => (!t && o && (e[i] = s), e), {});
}
var so = "UnlockVideo_2a17fce0",
  io = "UnlockVideo_video_c11372d2",
  to = y.resolve("videos"),
  oo = "unlockVideo";
var ro = (0, Xe.memo)(function ({ id: e, elementId: s, className: i }) {
    const t = (0, Xe.useRef)(null),
      o = Ii(),
      { opacity: r, config: a } = Qi(0),
      l = w(() => {
        t.current && (t.current.play(), a.start({ to: 1 }));
      }),
      c = w(ne),
      d = (0, Xe.useCallback)(() => {
        o?.emitter.trigger(ji(e, oo, s), e, s);
      }, [o?.emitter, s, e]);
    Li({
      id: e,
      elementId: s,
      registerAnimation: o?.registerAnimation,
      animName: oo,
      config: { start: l, skip: c },
    });
    const m = to.readOrEmpty("user_missions.unlock_72x72");
    return (0, ke.jsx)(Y.div, {
      style: { opacity: r },
      className: n(so, i),
      children: (0, ke.jsx)(J, { src: m, ref: t, onEnded: d, className: io }),
    });
  }),
  ao = {
    hideLockState: {
      [Yi]: {
        [Et]: { to: 0, reset: !0, config: { duration: 300 } },
        [wt]: { to: 0, reset: !0, config: { duration: 300 } },
      },
      [rt]: {},
      [zi]: { [St]: {} },
      [oo]: {},
    },
  },
  no = { [Yi]: { [Pt]: { to: 1, reset: !0, immediate: !0 } }, ...Tt.slideIn },
  lo = "unlockBonusAnim",
  co = "hideLockEvent",
  mo = "showBonusQuestComplete";
var uo = {
    MISSION_COMPLETE: "missionComplete",
    RE_ROLL: "reRoll",
    HIDE_REROLL_COMPONENT: "hideReRollComponent",
    SHOW_REROLL_COMPONENT: "showReRollComponent",
  },
  _o = {
    missionComplete: {
      [lt]: { "": { state: !0 } },
      [zi]: {},
      [rt]: {},
      [Yi]: {
        [_t]: { to: 0.5 },
        [pt]: { to: 0.5 },
        [ht]: { to: 0, config: { duration: 300 } },
        [ft]: { to: 0.5, delay: 200 },
      },
    },
  };
function po() {
  const {
      startAnimation: e,
      startComplexAnimation: s,
      checkRegisteredInStorage: i,
      emitter: t,
    } = yi(),
    { model: r } = mt(),
    { model: a } = Ai(),
    n = a.missionsList.get(),
    l = H(a.bonusMission.get()),
    c = a.timeToNextRerol.get(),
    d = fe();
  (!(function ({ missions: e, bonusMission: s }) {
    const { startComplexAnimation: i } = yi();
    o(() => {
      const t = {},
        o = {};
      (e.forEach((e) => {
        Dt(t, o, e);
      }),
        Dt(t, o, s),
        ae(o) ||
          i({
            complexId: uo.MISSION_COMPLETE,
            complexCfg: o,
            providerCfg: { skip: !0, skipTrigger: !0 },
          }),
        ae(t) ||
          i({
            complexId: uo.MISSION_COMPLETE,
            complexCfg: t,
            soundCfg: xe.umg_hub_quest_complete,
          }));
    });
  })({ missions: n, bonusMission: l }),
    (function ({ missions: e, bonusMission: s, isFirstRender: i }) {
      const { startComplexAnimation: t } = yi(),
        o = _(e),
        r = _(s);
      At(i, () => {
        const i = {};
        (e.forEach((e, s) => {
          const t = o[s];
          Lt(i, e, t);
        }),
          Lt(i, s, r),
          ae(i) ||
            t({
              complexId: uo.MISSION_COMPLETE,
              complexCfg: i,
              soundCfg: xe.umg_hub_quest_complete,
            }));
      });
    })({ missions: n, bonusMission: l, isFirstRender: d }),
    Jt({ missions: n, bonusMission: l, timeToNextReRoll: c, isFirstRender: d }),
    (function ({ missions: e, timeToNextReRoll: s, isFirstRender: i }) {
      const { startComplexAnimation: t, emitter: o } = yi(),
        r = _(s);
      (At(i, () => {
        if (0 == s && r > 0) {
          const s = Zt(e, Kt.showReRollButton);
          t({
            complexId: uo.SHOW_REROLL_COMPONENT,
            complexCfg: s,
            providerCfg: { skip: !0, skipTrigger: !0 },
          });
        }
      }),
        p(o, uo.RE_ROLL, () => {
          const s = eo(e, Kt.stopRotation),
            i = eo(e, Kt.showReRollButton);
          (t({
            complexId: uo.SHOW_REROLL_COMPONENT,
            complexCfg: s,
            providerCfg: { skip: !0, skipTrigger: !0 },
          }),
            t({ complexId: uo.SHOW_REROLL_COMPONENT, complexCfg: i }));
        }),
        p(o, uo.RE_ROLL, () => {
          if (0 == s) {
            const s = Zt(e, Kt.stopRotation),
              i = Zt(e, Kt.showReRollButton);
            return (
              t({
                complexId: uo.SHOW_REROLL_COMPONENT,
                complexCfg: s,
                providerCfg: { skip: !0, skipTrigger: !0 },
              }),
              void t({ complexId: uo.SHOW_REROLL_COMPONENT, complexCfg: i })
            );
          }
          const i = Zt(e, Kt.showReRollTimer);
          t({ complexId: uo.SHOW_REROLL_COMPONENT, complexCfg: i });
        }));
    })({ missions: n, timeToNextReRoll: c, isFirstRender: d }));
  const m = (0, Xe.useRef)(!1),
    u = (0, Xe.useCallback)(() => {
      l.isCompleted ||
        (n.every(({ isCompleted: e }) => e) &&
          !m.current &&
          ((m.current = !0), e({ id: l.id, animName: lo, elementId: Ot })));
    }, [l.isCompleted, l.id, n, e]);
  (p(t, ut, (e) => {
    const i = a.computes.missionById(e);
    i?.isCompleted &&
      i?.currentProgress == i?.totalProgress &&
      s({
        complexId: uo.MISSION_COMPLETE,
        complexCfg: { [e]: _o.missionComplete },
        soundCfg: xe.umg_hub_quest_complete,
      });
  }),
    p(t, uo.MISSION_COMPLETE, () => {
      u();
    }));
  const g = r.targetQuestId.get(),
    f = _(g);
  (0, Xe.useEffect)(() => {
    g &&
      f != g &&
      i({ id: g, animName: "reflection" }) &&
      e({ id: g, animName: rt, soundCfg: xe.umg_hub_highlight });
  }, [i, f, e, g]);
}
var go = (0, Xe.memo)(function ({ id: e, currentProgress: s, totalProgress: i, earned: t }) {
    const o = Ii(),
      { play: r } = a(),
      n = w(() => o?.emitter.trigger(ut, e)),
      l = w(() => r(xe.umg_hub_quest_progress)),
      c = (0, Xe.useMemo)(() => ({ onResolve: n, onStart: l }), [n, l]);
    return (0, ke.jsxs)(ke.Fragment, {
      children: [
        (0, ke.jsx)(es, { current: s, total: i }),
        (0, ke.jsx)(is, {
          size: "small",
          value: s,
          maxValue: i,
          children: (0, ke.jsx)($, { id: e, initValue: s - t, initMaxValue: i, animationProps: c }),
        }),
      ],
    });
  }),
  fo = "premiumMissionUnlockComplete";
var xo = (0, Xe.memo)(function ({
    id: e,
    currentProgress: s,
    totalProgress: i,
    earned: t,
    isPaused: o,
  }) {
    const r = yi(),
      [a, n] = (0, Xe.useState)(!o);
    return (
      p(r.emitter, fo, (s) => {
        e === s?.id && n(!0);
      }),
      (0, ke.jsx)(go, { id: e, currentProgress: a ? s : s - t, totalProgress: i, earned: t })
    );
  }),
  ho = "BaseMissionCard_34808815",
  bo = "BaseMissionCard_topContent_8e038c7d",
  Co = "BaseMissionCard_bottomContent_5f2b047c",
  vo = "BaseMissionCard_iconPosition_86b10539",
  No = "BaseMissionCard_icon_aafa664",
  yo = "BaseMissionCard_icon__quest_cdb5ef24",
  Io = "BaseMissionCard_sizeBoxTemp_b314ba10",
  jo = "BaseMissionCard_condition_acf099dc",
  ko = "BaseMissionCard_formatText_5d15d383",
  Mo = "BaseMissionCard_progress_22036f7a",
  Ro = "BaseMissionCard_rewardsContainer_4bc401ed",
  Eo = "BaseMissionCard_rewardItem_8174e9b5";
function wo({
  data: e,
  className: s,
  classNames: i,
  isPremium: t = !1,
  resId: o = 0,
  isProgressAnimationPaused: r = !1,
  iconSeverityLog: a = "warn",
}) {
  const l = e.icon + (t ? "_gold" : "_silver"),
    c = x(
      { iconPath: `userMissions.missionIcons.c_32.${l}`, rewardSize: ge.S24x24, rewardMaxCount: 4 },
      {
        medium: { iconPath: `userMissions.missionIcons.c_80.${l}` },
        large: { rewardSize: ge.Small, rewardMaxCount: 5 },
      },
    ),
    { id: d, isCompleted: m, animateCompletion: u } = e,
    _ = e.totalProgress > 0;
  return (
    (0, Xe.useEffect)(() => {
      e.icon || "silent" == a || h(`Icon for quest ID: ${d} is not set`, a);
    }, [e.icon, a, d]),
    (0, ke.jsxs)("div", {
      className: n(ho, s),
      children: [
        (0, ke.jsx)(Ui, { id: d }),
        (0, ke.jsxs)("div", {
          className: bo,
          children: [
            (0, ke.jsx)(Mt, {
              id: d,
              elementId: gt,
              className: vo,
              children: (0, ke.jsxs)(ct, {
                id: d,
                init: m && !u,
                children: [
                  e.icon &&
                    (0, ke.jsx)(
                      se,
                      {
                        path: c.iconPath,
                        width: 32,
                        height: 32,
                        adaptive: { medium: { width: 80, height: 80 } },
                        className: n(No, yo, i?.icon),
                      },
                      c.iconPath,
                    ),
                  (0, ke.jsx)(se, {
                    path: "userMissions.hub.basic.done_icon_s",
                    width: 32,
                    height: 32,
                    adaptive: {
                      medium: { width: 80, height: 80, path: "userMissions.hub.basic.done_icon_m" },
                    },
                    className: No,
                  }),
                ],
              }),
            }),
            (0, ke.jsx)("div", { className: Io }),
            (0, ke.jsx)(Xi, {
              id: d,
              elementId: _t,
              from: 0.9,
              children: (0, ke.jsx)(Mt, {
                id: d,
                elementId: _t,
                children: (0, ke.jsx)(Q, {
                  text: z(e.description),
                  classNames: { base: n(jo, i?.condition), text: ko },
                  upgradeLegacy: !0,
                }),
              }),
            }),
          ],
        }),
        (0, ke.jsxs)("div", {
          className: Co,
          children: [
            (0, ke.jsx)(Xi, {
              id: d,
              elementId: pt,
              from: 1,
              children: (0, ke.jsx)(Mt, {
                id: d,
                elementId: pt,
                className: Mo,
                children:
                  _ &&
                  (t
                    ? (0, ke.jsx)(xo, {
                        id: d,
                        currentProgress: e.currentProgress,
                        totalProgress: e.totalProgress,
                        earned: e.earned,
                        isPaused: r,
                      })
                    : (0, ke.jsx)(go, {
                        id: d,
                        currentProgress: e.currentProgress,
                        totalProgress: e.totalProgress,
                        earned: e.earned,
                      })),
              }),
            }),
            (0, ke.jsx)(Xi, {
              id: d,
              elementId: ft,
              from: 1,
              className: n(Ro, i?.rewards),
              children: (0, ke.jsx)(Mt, {
                id: d,
                elementId: ft,
                children: (0, ke.jsx)(
                  Ce,
                  {
                    bonuses: e.bonuses,
                    questId: e.id,
                    size: c.rewardSize,
                    resId: o,
                    count:
                      e.bonuses.length <= c.rewardMaxCount
                        ? c.rewardMaxCount
                        : c.rewardMaxCount - 1,
                    rewardItemClassMix: Eo,
                  },
                  d,
                ),
              }),
            }),
          ],
        }),
      ],
    })
  );
}
var So = "DailyBonusMissionCard_cardBlock_cc29aa9d",
  Po = "DailyBonusMissionCard_7d966ce1",
  Bo = "DailyBonusMissionCard_cardBlock__disabled_6a0da54e",
  Oo = "DailyBonusMissionCard_lockBlock_ac1dd103",
  To = "DailyBonusMissionCard_lockContent_19bd64b6",
  Ao = "DailyBonusMissionCard_lockIconBlock_cb535d36",
  Lo = "DailyBonusMissionCard_lockIcon_da4d31e0",
  Do = "DailyBonusMissionCard_unlockVideo_86889f8c",
  Wo = "DailyBonusMissionCard_lockMessage_662cb362",
  Fo = "DailyBonusMissionCard_timer_f1d1a15a",
  Ho = y.resolve("aliases"),
  Go = y.resolve("strings"),
  Vo = new Map([
    [!0, 1],
    [!1, 0],
  ]);
function qo({ data: e, isAnyCompleteAnimation: s, timeToMissionsUpdate: i }) {
  const { id: t, isAvailable: o } = e,
    r = !o || s;
  (!(function (e, s) {
    const { startGroupAnimation: i, registerAnimation: t, emitter: o } = yi();
    (p(o, Gt, () => {
      o.trigger(ji(e, Ft, s), e, s);
    }),
      p(o, Ht, () => {
        i({ groupId: e, groupCfg: Wt, providerCfg: { triggerId: Gt } });
      }),
      Li({
        id: e,
        elementId: s,
        registerAnimation: t,
        animName: Ft,
        config: {
          start: w(() => {
            i({ groupId: e, groupCfg: Tt.slideOut, providerCfg: { triggerId: Ht } });
          }),
          skip: w(() => {
            i({ groupId: e, groupCfg: Tt.slideOut, providerCfg: { skip: !0, triggerId: Ht } });
          }),
        },
      }));
  })(t, Bt),
    (function (e, s) {
      const { startGroupAnimation: i, registerAnimation: t, emitter: o } = yi();
      (p(o, mo, () => {
        o.trigger(ji(e, lo, s), e, s);
      }),
        p(o, co, () => {
          i({ groupId: e, groupCfg: no, providerCfg: { triggerId: mo } });
        }),
        Li({
          id: e,
          elementId: s,
          registerAnimation: t,
          animName: lo,
          config: {
            start: w(() => {
              (i({ groupId: e, groupCfg: Tt.slideOut, providerCfg: { skip: !0, skipTrigger: !0 } }),
                i({
                  groupId: e,
                  groupCfg: ao.hideLockState,
                  providerCfg: { triggerId: co },
                  soundCfg: xe.umg_hub_unlock_bonus,
                }));
            }),
            skip: w(() => {
              i({
                groupId: e,
                groupCfg: { ...Tt.slideOut, ...ao.hideLockState },
                providerCfg: { skip: !0, skipTrigger: !0 },
              });
            }),
          },
        }));
    })(t, Ot),
    Qt(t));
  const a = l({
    body: Go.readOrEmpty(
      "user_missions.hub.basic_missions.daily.bonus_daily_missions_timer.tooltip",
    ),
  });
  return (0, ke.jsxs)("div", {
    className: Po,
    children: [
      (0, ke.jsxs)(Xi, {
        id: t,
        elementId: Pt,
        className: n(So, !o && Bo),
        from: Vo.get(!r),
        children: [
          (0, ke.jsx)(wo, {
            data: { ...e, id: t },
            resId: Ho.read((e) =>
              e.user_missions.hub.basicMissions.DailyMissionsSection.DailyBlock("resId"),
            ),
            iconSeverityLog: o ? "warn" : "silent",
          }),
          !e.isCompleted &&
            i > 0 &&
            (0, ke.jsx)("div", {
              className: Fo,
              ...a,
              children: (0, ke.jsx)(c, { start: i, size: c.size.x24x24 }),
            }),
        ],
      }),
      (0, ke.jsxs)(Xi, {
        id: t,
        elementId: Rt,
        className: Oo,
        from: Vo.get(r),
        children: [
          (0, ke.jsx)(Ui, { id: t, elementId: St, glowType: Gi.GREY_LENSE }),
          (0, ke.jsxs)("div", {
            className: To,
            children: [
              (0, ke.jsxs)("div", {
                className: Ao,
                children: [
                  (0, ke.jsx)(Xi, {
                    id: t,
                    elementId: Et,
                    from: 1,
                    children: (0, ke.jsx)("div", { className: Lo }),
                  }),
                  (0, ke.jsx)(ro, { id: t, className: Do }),
                ],
              }),
              (0, ke.jsx)(Xi, {
                id: t,
                elementId: wt,
                from: 1,
                children: (0, ke.jsx)(oe, {
                  path: "user_missions.hub.basic_missions.daily.bonus_daily_missions_lock_info",
                  className: Wo,
                }),
              }),
            ],
          }),
        ],
      }),
      (0, ke.jsx)(at, { id: t }),
    ],
  });
}
var $o = "RerollButton_5f432227",
  zo = "RerollButton_base__active_c1f50ac9",
  Uo = "RerollButton_buttonAnim_cb83531a",
  Qo = "RerollButton_buttonAnim__hided_bb070845",
  Yo = "RerollButton_title_2b7fc3a",
  Xo = "RerollButton_iconAnimation_8a6d0ff3",
  Jo = "RerollButton_icon_990a0f17",
  Ko = "RerollButton_base__locked_6d55354d",
  Zo = "RerollButton_timerAnim_36fcf1f3",
  er = "RerollButton_timer_611c1639",
  sr = y.resolve("aliases"),
  ir = y.resolve("views"),
  tr = y.resolve("strings"),
  or = sr.read((e) => e.user_missions.hub.basicMissions.DailyMissionsSection.DailyBlock("resId")),
  rr = ir.read((e) => e.mono.user_missions.tooltips.daily_reroll_tooltip("resId"));
function ar({ id: e, isCompleted: s, isLocked: i, onClick: t, className: o, timeToNextReroll: r }) {
  const l = a(),
    d = N(
      ((e, s) =>
        s
          ? {
              contentId: ir.read((e) =>
                e.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent("resId"),
              ),
              decoratorId: ir.read((e) =>
                e.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
              ),
              args: {
                header: tr.readOrEmpty("quests.lockedForRerollTooltip.header"),
                body: tr.readOrEmpty("quests.lockedForRerollTooltip.body"),
              },
              disabled: e,
            }
          : { resId: or, contentId: rr, disabled: e })(s, i),
    ),
    m = !s && 0 === r && !i,
    u = r > 0 && !i;
  return (0, ke.jsxs)(Xi, {
    id: e,
    elementId: ht,
    from: s ? 0 : 1,
    ...d,
    className: n($o, m && zo, i && Ko, o),
    onClick: m ? t : void 0,
    children: [
      (0, ke.jsx)(Xi, {
        from: u ? 1 : 0,
        id: e,
        elementId: Ct,
        className: Zo,
        children: (0, ke.jsx)(c, {
          start: r,
          format: c.format.superCompact,
          size: c.size.x24x24,
          className: er,
        }),
      }),
      (0, ke.jsxs)(Xi, {
        from: u ? 0 : 1,
        id: e,
        onMouseEnter: () => {
          l.play("mouse-enter", { target: "Reroll button" });
        },
        elementId: vt,
        className: n(Uo, u && Qo),
        children: [
          !i &&
            (0, ke.jsx)("div", {
              className: Yo,
              children: tr.readOrEmpty("user_missions.hub.basic_missions.daily.reroll_button"),
            }),
          (0, ke.jsx)($t, {
            id: e,
            elementId: bt,
            className: Xo,
            children: (0, ke.jsx)("div", { className: Jo }),
          }),
        ],
      }),
    ],
  });
}
var nr = "DailyMissionCard_dbc24668",
  lr = "DailyMissionCard_reroll_fd5c6ea8",
  cr = y.resolve("aliases");
function dr({ data: e, timeToNextReroll: s, onReroll: i }) {
  const { id: t, isCompleted: o, isLocked: r } = e;
  return (
    Qt(t),
    (0, ke.jsxs)("div", {
      className: nr,
      children: [
        (0, ke.jsx)(wo, {
          data: e,
          resId: cr.read((e) =>
            e.user_missions.hub.basicMissions.DailyMissionsSection.DailyBlock("resId"),
          ),
        }),
        (0, ke.jsx)(at, { id: e.id }),
        e.isRerollEnabled &&
          (0, ke.jsx)(ar, {
            id: t,
            isCompleted: o,
            isLocked: r,
            onClick: () => i(e.id),
            timeToNextReroll: s,
            className: lr,
          }),
      ],
    })
  );
}
var mr = "DailyMissionsBlock_d8a9293c",
  ur = "DailyMissionsBlock_allMissionsCompletedBlock_d019306a",
  _r = "DailyMissionsBlock_allMissionsCompletedMessage_20d9eaa9",
  pr = "DailyMissionsBlock_timer_c9dd266c",
  gr = "DailyMissionsBlock_separator_3d64a18",
  fr = y.resolve("strings"),
  xr = L(function () {
    const { model: e, controls: s } = Ai(),
      i = e.timeToMissionsUpdate.get();
    po();
    const t = l({
      body: fr.readOrEmpty(
        "user_missions.hub.basic_missions.daily.new_daily_missions_timer.tooltip",
      ),
    });
    return (0, ke.jsxs)("div", {
      className: mr,
      children: [
        e.areAllMissionsCompleted.get() &&
          (0, ke.jsxs)("div", {
            className: ur,
            ...t,
            children: [
              (0, ke.jsx)("div", {
                className: _r,
                children: fr.readOrEmpty(
                  "user_missions.hub.basic_missions.daily.new_daily_missions_timer.message",
                ),
              }),
              (0, ke.jsx)(c, { start: i, size: c.size.x16x16, className: pr }),
            ],
          }),
        ee(e.missionsList.get(), (i, t) =>
          (0, ke.jsxs)(
            Xe.Fragment,
            {
              children: [
                (0, ke.jsx)(dr, {
                  data: i,
                  onReroll: s.onReroll,
                  timeToNextReroll: e.timeToNextRerol.get(),
                }),
                (0, ke.jsx)("div", { className: gr }),
              ],
            },
            `dm_card_${t}`,
          ),
        ),
        (0, ke.jsx)(qo, {
          data: { ...e.bonusMission.get(), bonuses: e.bonusMissionBonuses.get() },
          isAnyCompleteAnimation: e.computes.isAnyCompleteAnimation(),
          timeToMissionsUpdate: i,
        }),
      ],
    });
  }),
  hr = {
    rootId: y
      .resolve("aliases")
      .read((e) => e.user_missions.hub.basicMissions.DailyMissionsSection.DailyBlock("resId")),
  };
function br() {
  return (0, ke.jsx)(Ti, {
    options: hr,
    children: (0, ke.jsx)(Oi, { children: (0, ke.jsx)(xr, {}) }),
  });
}
var [Cr, vr] = E()(
    ({ observableModel: e }) => {
      const s = { ...e.primitives(["isAvailable"]), missionsList: e.arrayClone("missionsList") },
        i = ue.model((e) => te(s.missionsList.get(), (s) => s.id == e));
      return { ...s, computes: { missionById: i } };
    },
    ({ externalModel: e }) => ({ onPurchasePremium: e.createCallbackNoArgs("onPurchasePremium") }),
  ),
  Nr = {
    from: { opacity: 0, transform: "translateX(-10%)" },
    to: async (e) => {
      (await e({ opacity: 0.2, transform: "translateX(0%)", config: { duration: 300 } }),
        await e({ opacity: 0, transform: "translateX(10%)", config: { duration: 300 } }));
    },
  },
  yr = {
    from: { opacity: 0 },
    to: async (e) => {
      (await e({ opacity: 0.25, config: { duration: 200 } }),
        await e({ opacity: 0, config: { duration: 400 } }));
    },
  },
  Ir = {
    from: { opacity: 0.25 },
    to: async (e) => {
      (await e({ opacity: 0.9, config: { duration: 200 } }),
        await e({ opacity: 0.25, config: { duration: 400 } }));
    },
  };
var jr = "Arrow_391ca11f",
  kr = "Arrow_iconBig_9a073166",
  Mr = "Arrow_icon_bbabc0ab",
  Rr = "Arrow_icon__left_cc9a053b",
  Er = "Arrow_icon__right_2cb4415d",
  wr = "arrow";
function Sr({ id: e }) {
  const { registerAnimation: s, emitter: i } = yi(),
    {
      bigArrowStyle: t,
      leftArrowStyle: o,
      mainArrowStyle: r,
      rightArrowStyle: a,
      config: l,
    } = (function (e) {
      const s = C(),
        i = C(),
        t = C(),
        o = C(),
        r = (0, Xe.useRef)(0),
        a = w(() => {
          ((r.current += 1), 4 == r.current && ((r.current = 0), e?.()));
        }),
        n = w((e) => {
          const r = 0 | e?.delay;
          (s.start({ ...Nr, onRest: a, reset: !0, delay: r }),
            i.start({ ...yr, onRest: a, reset: !0, delay: r + 150 }),
            t.start({ ...Ir, onRest: a, reset: !0, delay: r + 250 }),
            o.start({ ...yr, onRest: a, reset: !0, delay: r + 350 }));
        }),
        l = b({ ref: s, onRest: a, ...Nr }),
        c = b({ ref: i, onRest: a, ...yr }),
        d = b({ ref: t, onRest: a, ...Ir }),
        m = b({ ref: o, onRest: a, ...yr });
      return (0, Xe.useMemo)(
        () => ({
          bigArrowStyle: l,
          leftArrowStyle: c,
          mainArrowStyle: d,
          rightArrowStyle: m,
          config: { start: n, skip: ne },
        }),
        [l, c, d, m, n],
      );
    })(w(() => i.trigger(ji(e, wr), e)));
  return (
    Li({ id: e, registerAnimation: s, animName: wr, config: l }),
    (0, ke.jsxs)("div", {
      className: jr,
      children: [
        (0, ke.jsx)(Y.div, { style: t, className: kr }),
        (0, ke.jsx)(Y.div, { style: o, className: n(Mr, Rr) }),
        (0, ke.jsx)(Y.div, { style: a, className: n(Mr, Er) }),
        (0, ke.jsx)(Y.div, { style: r, className: Mr }),
      ],
    })
  );
}
var Pr = "card",
  Br = "lockIcon",
  Or = "glowLock",
  Tr = "unlockGlowShow",
  Ar = "unlockGlowHide",
  Lr = "PremiumDailyMissionsCard_606cad53",
  Dr = "PremiumDailyMissionsCard_lockContainer_df076624",
  Wr = "PremiumDailyMissionsCard_card_b95d2566",
  Fr = "PremiumDailyMissionsCard_icon_77ecd434",
  Hr = "PremiumDailyMissionsCard_condition_5fa7ebd",
  Gr = "PremiumDailyMissionsCard_unlockVideo_416f470a",
  Vr = "PremiumDailyMissionsCard_lockIcon_9bac6cb",
  qr = "PremiumDailyMissionsCard_unlockGlowContainer_c6213bf6",
  $r = "PremiumDailyMissionsCard_unlockGlow_6356a26d",
  zr = y.resolve("aliases"),
  Ur = y.resolve("strings");
function Qr({ data: e, isJustUnlocked: s }) {
  const i = l({
      body: Ur.readOrEmpty("user_missions.hub.basic_missions.daily.premium.locked_mission.tooltip"),
    }),
    t = e.isLocked || s;
  return (0, ke.jsxs)("div", {
    className: Lr,
    children: [
      (0, ke.jsxs)(Xi, {
        id: e.id,
        elementId: Pr,
        from: t ? 0.25 : 1,
        className: Wr,
        children: [
          (0, ke.jsx)(wo, {
            data: e,
            isPremium: !0,
            classNames: { icon: Fr, condition: Hr },
            resId: zr.read((e) =>
              e.user_missions.hub.basicMissions.DailyMissionsSection.PremiumBlock("resId"),
            ),
            isProgressAnimationPaused: t,
          }),
          (0, ke.jsx)(at, { id: e.id }),
        ],
      }),
      t &&
        (0, ke.jsxs)(ke.Fragment, {
          children: [
            (0, ke.jsxs)("div", {
              className: Dr,
              ...(e.isLocked && i),
              children: [
                (0, ke.jsx)(Ui, { id: e.id, elementId: Or, glowType: Gi.GREY_LENSE }),
                (0, ke.jsx)(Xi, {
                  id: e.id,
                  elementId: Br,
                  from: 1,
                  children: (0, ke.jsx)("div", { className: Vr }),
                }),
                (0, ke.jsx)(ro, { id: e.id, className: Gr }),
              ],
            }),
            (0, ke.jsx)(Xi, {
              id: e.id,
              elementId: Ar,
              from: 1,
              className: qr,
              children: (0, ke.jsx)(Xi, {
                id: e.id,
                elementId: Tr,
                from: 0,
                className: qr,
                children: (0, ke.jsx)("div", { className: $r }),
              }),
            }),
          ],
        }),
    ],
  });
}
function Yr(e, s) {
  (0, Xe.useEffect)(() => {
    e && s();
  });
}
var Xr = {
  missionComplete: {
    [lt]: { "": { state: !0 } },
    [zi]: {},
    [Yi]: { [_t]: { to: 0.25 }, [pt]: { to: 0.5 }, [ft]: { to: 0.5, delay: 200 } },
    [wr]: { "": { delay: 600 } },
  },
  missionUnlock: {
    [rt]: {},
    [zi]: { [Or]: {} },
    [oo]: {},
    [Yi]: {
      [Pr]: { to: 1, delay: 1250 },
      [Br]: { to: 0 },
      [Tr]: { to: 1 },
      [Ar]: { to: 0, delay: 400 },
    },
  },
};
function Jr({ completeIdx: e, missions: s, startGroupAnimation: i }) {
  const t = s[e];
  if (
    (i({ groupId: t.id, groupCfg: Xr.missionComplete, soundCfg: xe.umg_hub_quest_complete }),
    e < s.length - 1)
  ) {
    const t = e + 1,
      o = s[t];
    setTimeout(() => {
      i({
        groupId: o.id,
        groupCfg: Xr.missionUnlock,
        providerCfg: { triggerId: fo, triggerParams: { unlockedIdx: t } },
        soundCfg: xe.umg_hub_unlock_premium,
      });
    }, 1e3);
  }
}
var Kr = "premiumMissionComplete",
  Zr = "premiumMissionLocked",
  ea = "premiumMissionUnComplete",
  sa = {
    missionUnComplete: {
      [lt]: { "": { state: !1 } },
      [Yi]: {
        [_t]: { to: 0.9 },
        [pt]: { to: 1 },
        [ft]: { to: 1 },
        [Pr]: { to: 1 },
        [Br]: { to: 0 },
      },
    },
    missionLock: {
      [lt]: { "": { state: !1 } },
      [Yi]: {
        [_t]: { to: 0.9 },
        [pt]: { to: 1 },
        [ft]: { to: 1 },
        [Pr]: { to: 0.25 },
        [Br]: { to: 1 },
      },
    },
  };
function ia() {
  const { startAnimation: e, checkRegisteredInStorage: s } = yi(),
    { model: i } = mt(),
    { model: t } = vr(),
    r = H(t.missionsList.get()),
    a = _(r),
    n = fe(),
    l = i.targetQuestId.get(),
    c = _(l);
  ((0, Xe.useEffect)(() => {
    l &&
      c != l &&
      s({ id: l, animName: "reflection" }) &&
      e({ id: l, animName: rt, soundCfg: xe.umg_hub_highlight });
  }, [s, c, e, l]),
    (function ({ missions: e }) {
      const { startGroupAnimation: s } = yi();
      o(() => {
        const i = e.findIndex((e) => e.isCompleted && e.animateCompletion);
        -1 !== i && Jr({ completeIdx: i, missions: e, startGroupAnimation: s });
      });
    })({ missions: r }),
    (function ({ isFirstRender: e, missions: s, prevMissions: i }) {
      const { startComplexAnimation: t } = yi();
      (o(() => {
        const e = {};
        (s.forEach((s) => {
          s.isCompleted && !s.animateCompletion && (e[s.id] = Xr.missionComplete);
        }),
          ae(e) || t({ complexId: Kr, complexCfg: e, providerCfg: { skip: !0, skipTrigger: !0 } }));
      }),
        Yr(!e, () => {
          const e = {},
            o = {};
          (s.forEach((s, t) => {
            const r = i[t];
            s.isLocked && !r.isLocked
              ? (e[s.id] = sa.missionLock)
              : !s.isCompleted && r.isCompleted && (o[s.id] = sa.missionUnComplete);
          }),
            ae(e) ||
              t({ complexId: Zr, complexCfg: e, providerCfg: { skip: !0, skipTrigger: !0 } }),
            ae(o) ||
              t({ complexId: ea, complexCfg: o, providerCfg: { skip: !0, skipTrigger: !0 } }));
        }));
    })({ isFirstRender: n, missions: r, prevMissions: a }),
    (function ({ isFirstRender: e, missions: s, prevMissions: i }) {
      const { startGroupAnimation: t, emitter: o } = yi();
      (p(o, fo, ({ unlockedIdx: e }) => {
        s[e].isCompleted && Jr({ completeIdx: e, missions: s, startGroupAnimation: t });
      }),
        Yr(!e, () => {
          const e = s.findIndex((e, s) => {
            const t = i[s];
            return e.isCompleted && !t.isCompleted;
          });
          -1 !== e && Jr({ completeIdx: e, missions: s, startGroupAnimation: t });
        }));
    })({ isFirstRender: n, missions: r, prevMissions: a }));
}
var ta = "PremiumDailyMissionsList_a02f9e79",
  oa = L(function () {
    const { model: e } = vr(),
      s = e.missionsList.get();
    return (
      ia(),
      (0, ke.jsx)("div", {
        className: ta,
        children: ee(s, (e, i) => {
          const t = (i > 0 && D(s, i - 1)?.animateCompletion) || !1;
          return (0, ke.jsxs)(
            Xe.Fragment,
            {
              children: [
                (0, ke.jsx)(Qr, { data: e, isJustUnlocked: t }, `pdm_card_${e.id}`),
                i < s.length - 1 && (0, ke.jsx)(Sr, { id: e.id }),
              ],
            },
            `pdm_card_${e.id}`,
          );
        }),
      })
    );
  }),
  ra = "PurchasePremiumState_bg_9f5578d2",
  aa = "PurchasePremiumState_6e377b64",
  na = "PurchasePremiumState_icon_f474fb80",
  la = "PurchasePremiumState_container_c4d5c44e",
  ca = "PurchasePremiumState_title_d576f228",
  da = "PurchasePremiumState_message_a8e12b7c",
  ma = "PurchasePremiumState_button_4e9a2fc9",
  ua = "PurchasePremiumState_buttonTitle_2b5af5a0",
  _a = y.resolve("strings");
function pa() {
  const { controls: e } = vr();
  return (0, ke.jsxs)("div", {
    className: aa,
    children: [
      (0, ke.jsx)("div", { className: ra }),
      (0, ke.jsx)("div", { className: na }),
      (0, ke.jsxs)("div", {
        className: la,
        children: [
          (0, ke.jsx)("div", {
            className: ca,
            children: _a.readOrEmpty(
              "user_missions.hub.basic_missions.daily.purchase_premium.title",
            ),
          }),
          (0, ke.jsx)("div", {
            className: da,
            children: _a.readOrEmpty(
              "user_missions.hub.basic_missions.daily.purchase_premium.message",
            ),
          }),
          (0, ke.jsx)(S, {
            theme: S.themes.primary,
            size: S.sizes.small,
            onClick: e.onPurchasePremium,
            className: ma,
            children: (0, ke.jsx)("div", {
              className: ua,
              children: _a.readOrEmpty(
                "user_missions.hub.basic_missions.daily.purchase_premium.button",
              ),
            }),
          }),
        ],
      }),
    ],
  });
}
var ga = L(function () {
    const { model: e } = vr();
    return e.isAvailable.get() ? (0, ke.jsx)(oa, {}) : (0, ke.jsx)(pa, {});
  }),
  fa = {
    rootId: y
      .resolve("aliases")
      .read((e) => e.user_missions.hub.basicMissions.DailyMissionsSection.PremiumBlock("resId")),
  };
function xa() {
  return (0, ke.jsx)(Cr, {
    options: fa,
    children: (0, ke.jsx)(Oi, { children: (0, ke.jsx)(ga, {}) }),
  });
}
var [ha, ba] = E()(({ observableModel: e }) => e.primitives(["progressType"]), ne),
  Ca = (function (e) {
    return ((e.EpicQuest = "epicQuest"), (e.WinBack = "winBack"), (e.Disabled = "disabled"), e);
  })({}),
  [va, Na] = E()(
    ({ observableModel: e }) => ({
      ...e.primitives(["id", "current", "total", "earned", "winBackTimeLeft"]),
      bonuses: e.arrayClone("bonuses"),
    }),
    ({ externalModel: e }) => ({
      takeWinBackReward: e.createCallbackNoArgs("onTakeWinBackReward"),
    }),
  ),
  ya = "ClaimWinBack_f65a728",
  Ia = "ClaimWinBack_claimButton_f4d9ca67",
  ja = "ClaimWinBack_claimText_329621c1",
  ka = "ClaimWinBack_timer_89673125";
var Ma = L(function ({ className: e }) {
    const { model: s, controls: i } = Na(),
      t = y.resolve("strings"),
      o = s.winBackTimeLeft.get();
    return (0, ke.jsxs)("div", {
      className: n(ya, e),
      children: [
        (0, ke.jsx)(S, {
          theme: "primary",
          size: "small",
          autoAlignContent: !1,
          className: Ia,
          onClick: i.takeWinBackReward,
          children: (0, ke.jsx)("div", {
            className: ja,
            children: t.readOrEmpty(
              "user_missions.hub.reward_progress.epic_quest_progress.collect_win_back",
            ),
          }),
        }),
        (0, ke.jsxs)("div", {
          className: ka,
          children: [
            t.readOrEmpty("user_missions.hub.reward_progress.epic_quest_progress.time_left"),
            (0, ke.jsx)(c, { start: o }),
          ],
        }),
      ],
    });
  }),
  Ra = "EpicQuestProgress_bg_22314285",
  Ea = "EpicQuestProgress_70dbe9c2",
  wa = "EpicQuestProgress_header_b693c8b4",
  Sa = "EpicQuestProgress_info_e415f6af",
  Pa = "EpicQuestProgress_title_4037f217",
  Ba = "EpicQuestProgress_text_2f226d2",
  Oa = "EpicQuestProgress_rewardsMix_8b04a35e",
  Ta = "EpicQuestProgress_progress_9b81fedd",
  Aa = "EpicQuestProgress_progressBar_115e7a24",
  La = "EpicQuestProgress_claimWinBack_b707ef06",
  Da = y.resolve("aliases");
var Wa = L(function () {
    const { model: e } = Na(),
      s = e.total.get(),
      t = e.current.get(),
      o = e.earned.get(),
      r = e.id.get(),
      a = y.resolve("strings"),
      n = x({ rewardSize: ge.S24x24 }, { large: { rewardSize: ge.Small } });
    return (0, ke.jsxs)("div", {
      className: Ea,
      children: [
        (0, ke.jsx)("div", { className: Ra }),
        (0, ke.jsxs)("div", {
          className: wa,
          children: [
            (0, ke.jsxs)("div", {
              className: Sa,
              children: [
                (0, ke.jsx)(i, {
                  classMix: Pa,
                  isTruncationAvailable: !0,
                  text: a.readOrEmpty(
                    "user_missions.hub.reward_progress.epic_quest_progress.title",
                  ),
                }),
                (0, ke.jsx)(i, {
                  classMix: Ba,
                  isTruncationAvailable: !0,
                  text: a.readOrEmpty(
                    "user_missions.hub.reward_progress.epic_quest_progress.sub_title",
                  ),
                }),
              ],
            }),
            (0, ke.jsx)(Ce, {
              bonuses: e.bonuses.get(),
              questId: r,
              size: n.rewardSize,
              resId: Da.read((e) =>
                e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
              ),
              count: 5,
              classMix: Oa,
              isFixedBoxSize: !1,
            }),
          ],
        }),
        (0, ke.jsxs)("div", {
          className: Ta,
          children: [
            (0, ke.jsx)(es, { current: t, total: s }),
            (0, ke.jsxs)(is, {
              value: t,
              size: "full",
              maxValue: s,
              className: Aa,
              children: [
                (0, ke.jsx)($, { initValue: t - o, initMaxValue: s }),
                e.winBackTimeLeft.get() > 0 && (0, ke.jsx)(Ma, { className: La }),
              ],
            }),
          ],
        }),
      ],
    });
  }),
  Fa = {
    rootId: y
      .resolve("aliases")
      .read((e) =>
        e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
      ),
    context: "model.epicQuestProgress",
  };
function Ha() {
  return (0, ke.jsx)(va, { options: Fa, children: (0, ke.jsx)(Wa, {}) });
}
var [Ga, Va] = E()(
    ({ observableModel: e }) => {
      const s = {
          ...e.primitives([
            "id",
            "current",
            "total",
            "earned",
            "isBattlePassActive",
            "offersState",
            "timeLeftToClaim",
          ]),
          quests: e.arrayClone("quests"),
        },
        i = ue.model((e) => D(s.quests.get(), e)),
        t = ue.model((e) => {
          const s = i(e);
          return s ? K(s.rewards) : [];
        });
      return { ...s, computes: { rewardsByIndex: t } };
    },
    ({ externalModel: e }) => ({
      takeReward: e.createCallback((e) => ({ questNumber: e }), "onTakeReward"),
      takeAllRewards: e.createCallbackNoArgs("onTakeAllRewards"),
    }),
  ),
  qa = y
    .resolve("aliases")
    .read((e) =>
      e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
    ),
  $a = (function (e) {
    return ((e.AVAILABLE = "available"), (e.DISABLED = "disabled"), (e.NO_OFFERS = "no_offers"), e);
  })({}),
  za = "MainReward_c68d434f",
  Ua = "MainReward_base__withBattlePass_92334d39",
  Qa = "MainReward_hitBox_6b11fff9",
  Ya = "MainReward_claimButton_20c977ab",
  Xa = "MainReward_claimText_107d14cf",
  Ja = "MainReward_timer_234aa797",
  Ka = y.resolve("aliases"),
  Za = y.resolve("views");
var en = L(function () {
    const { model: e, controls: s } = Va(),
      i = e.timeLeftToClaim.get(),
      t = e.offersState.get(),
      o = y.resolve("strings"),
      r = N({
        resId: Ka.read((e) =>
          e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
        ),
        contentId: Za.read((e) => e.mono.winback.tooltips.main_reward_tooltip("resId")),
      });
    return (0, ke.jsxs)("div", {
      className: n(za, e.isBattlePassActive.get() && Ua),
      children: [
        (0, ke.jsx)("div", { ...r, className: Qa }),
        t != $a.NO_OFFERS &&
          (0, ke.jsxs)(ke.Fragment, {
            children: [
              (0, ke.jsx)(S, {
                theme: "primary",
                size: "medium",
                disabled: t == $a.DISABLED,
                className: Ya,
                onClick: s.takeAllRewards,
                children: (0, ke.jsx)("div", {
                  className: Xa,
                  children: o.readOrEmpty(
                    "user_missions.hub.reward_progress.win_back_quest_progress.claim_main",
                  ),
                }),
              }),
              i > 0 &&
                (0, ke.jsxs)("div", {
                  className: Ja,
                  children: [
                    o.readOrEmpty(
                      "user_missions.hub.reward_progress.win_back_quest_progress.time_left",
                    ),
                    (0, ke.jsx)(c, { start: i }),
                  ],
                }),
            ],
          }),
      ],
    });
  }),
  sn = (function (e) {
    return (
      (e.VEHICLE_FOR_GIFT = "vehicleForGift"),
      (e.VEHICLE_DISCOUNT = "vehicleDiscount"),
      (e.VEHICLE_FOR_RENT = "vehicleForRent"),
      (e.SELECTABLE_VEHICLE_FOR_GIFT = "selectableVehicleForGift"),
      (e.SELECTABLE_VEHICLE_DISCOUNT = "selectableVehicleDiscount"),
      e
    );
  })({}),
  tn = {
    base: "WinBackReward_debcb7d5",
    icon: "WinBackReward_icon_592ffdd7",
    base__vehicleForGift: "WinBackReward_base__vehicleForGift_5fa23c6c",
    base__vehicleDiscount: "WinBackReward_base__vehicleDiscount_5fa23c6c",
    level: "WinBackReward_level_d832cd76",
    base__vehicleForRent: "WinBackReward_base__vehicleForRent_5fa23c6c",
    discount: "WinBackReward_discount_86c0d506",
  },
  on = y.resolve("aliases"),
  rn = y.resolve("views");
function an({ reward: e, className: s }) {
  const i = e.name,
    t = ((e) => {
      switch (e.name) {
        case sn.VEHICLE_FOR_GIFT:
        case sn.VEHICLE_DISCOUNT:
          return `vehicle.c_420x307.${q(e.vehicleName).toLowerCase()}`;
        case sn.SELECTABLE_VEHICLE_FOR_GIFT:
        case sn.SELECTABLE_VEHICLE_DISCOUNT:
          return `quests.bonuses.small.${e.name}`;
        case sn.VEHICLE_FOR_RENT:
          return "quests.bonuses.small.vehicles_rent";
      }
      return "";
    })(e);
  return (0, ke.jsxs)("div", {
    ...N({
      resId: on.read((e) =>
        e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
      ),
      contentId:
        Number(e.tooltipContentId) ||
        rn.read((e) =>
          e.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
        ),
      args: { tooltipId: e.tooltipId },
    }),
    className: n(tn.base, tn[`base__${i}`], s),
    children: [
      (0, ke.jsx)(se, { path: t, className: tn.icon }),
      e?.vehicleLvl && (0, ke.jsx)(W, { value: e.vehicleLvl, className: tn.level }),
      i == sn.VEHICLE_DISCOUNT &&
        (0, ke.jsx)(se, {
          path: "userMissions.hub.reward_progress.discount_colorize",
          className: tn.discount,
        }),
    ],
  });
}
var nn = "Quest_bd89fbc",
  ln = "Quest_info_2092d559",
  cn = new Set([
    sn.VEHICLE_FOR_GIFT,
    sn.VEHICLE_DISCOUNT,
    sn.VEHICLE_FOR_RENT,
    sn.SELECTABLE_VEHICLE_FOR_GIFT,
    sn.SELECTABLE_VEHICLE_DISCOUNT,
  ]);
var dn = L(function ({ style: e, className: s, index: i }) {
    const { model: t } = Va(),
      o = t.computes.rewardsByIndex(i),
      a = x({ rewardSize: ge.S24x24 }, { large: { rewardSize: ge.Small } });
    return (0, ke.jsx)("div", {
      className: n(nn, s),
      style: e,
      children: o.map((e, s) => {
        return cn.has(e.name)
          ? (0, ke.jsx)(an, { reward: e }, `${s}_${e.name}`)
          : (0, ke.jsx)(
              _e,
              {
                size: a.rewardSize,
                ...((i = e),
                (t = ge.Small),
                {
                  name: i.name,
                  image: k(i, t),
                  special: i.overlayType,
                  value: i.value,
                  valueType: le(i.name),
                  tooltipArgs: {
                    ...r(
                      { tooltipId: i.tooltipId },
                      Number(i.tooltipContentId) ||
                        R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                          "resId",
                        ),
                    ),
                    resId: qa,
                  },
                }),
                classNames: { info: ln },
              },
              `${s}_${e.name}`,
            );
        var i, t;
      }),
    });
  }),
  mn = "QuestStatus_questNumber_a4eb07b6",
  un = "QuestStatus_claim_f060156f",
  _n = "QuestStatus_claimText_bb723ab5",
  pn = [sn.SELECTABLE_VEHICLE_FOR_GIFT, sn.SELECTABLE_VEHICLE_DISCOUNT];
var gn = L(function ({ index: e, questNumber: s, className: i, style: t }) {
  const { model: o, controls: r } = Va(),
    a = o.current.get(),
    l = o.computes.rewardsByIndex(e),
    c = o.offersState.get(),
    d = y.resolve("strings");
  return a < s
    ? (0, ke.jsx)("div", { className: n(mn, i), style: t, children: s })
    : l.some(({ name: e }) => pn.includes(e))
      ? (0, ke.jsx)(S, {
          theme: "primary",
          size: "small",
          disabled: c === $a.DISABLED,
          className: n(un, i),
          autoAlignContent: !1,
          style: t,
          onClick: () => r.takeReward(s.toString()),
          children: (0, ke.jsx)("div", {
            className: _n,
            children: d.readOrEmpty(
              "user_missions.hub.reward_progress.win_back_quest_progress.claim",
            ),
          }),
        })
      : (0, ke.jsx)(se, {
          path: "userMissions.hub.reward_progress.completed",
          width: 11,
          height: 11,
          className: i,
          style: t,
        });
});
var fn = L(function ({ classNames: e }) {
    const { model: s } = Va(),
      i = s.total.get(),
      t = s.quests.get();
    return (0, ke.jsx)(ke.Fragment, {
      children: F(t, ({ questNumber: s }, t) => {
        const o = { left: (s / i) * 100 + "%" };
        return (0, ke.jsxs)(
          Xe.Fragment,
          {
            children: [
              (0, ke.jsx)(gn, { index: t, questNumber: s, className: e?.questStatus, style: o }),
              (0, ke.jsx)(dn, { index: t, className: e?.quest, style: o }),
            ],
          },
          `${t}_${s}`,
        );
      }),
    });
  }),
  xn = "WinBackProgress_bg_8a178cd6",
  hn = "WinBackProgress_7746c27",
  bn = "WinBackProgress_header_fddc8c5",
  Cn = "WinBackProgress_title_ae6c0cf1",
  vn = "WinBackProgress_text_9329bcf6",
  Nn = "WinBackProgress_content_cf4c626a",
  yn = "WinBackProgress_scroll_15d14186",
  In = "WinBackProgress_scrollWrapper_b8ebdca5",
  jn = "WinBackProgress_scrollWrapper__maskLeft_e282f4a5",
  kn = "WinBackProgress_progress_b2a3589c",
  Mn = "WinBackProgress_progressBar_7d519953",
  Rn = "WinBackProgress_questStatus_5f3d0943",
  En = "WinBackProgress_quest_f3ea405e",
  wn = "WinBackProgress_scrollBar_efbfbc78",
  Sn = "WinBackProgress_mainReward_1460436e";
y.resolve("aliases");
var Pn = y.resolve("intl");
var Bn = L(function () {
    const { model: e } = Va(),
      { api: o } = re(),
      r = t(),
      [a, l] = (0, Xe.useState)(!1),
      c = e.total.get(),
      d = e.current.get(),
      m = e.earned.get(),
      u = 160 * e.quests.get().length,
      _ = y.resolve("strings"),
      p = (0, Xe.useCallback)(() => {
        l(o.animationScroll.scrollPosition.get() > 0);
      }, [o]),
      g = B(() => r.run(() => o.applyScroll(u * (d / c) - 160)));
    return (
      (0, Xe.useEffect)(() => {
        const e = o.events.on("start", p),
          s = o.events.on("rest", p);
        return (
          g(),
          () => {
            (e(), s());
          }
        );
      }, [o.events, g, p]),
      (0, ke.jsxs)("div", {
        className: hn,
        children: [
          (0, ke.jsx)("div", { className: xn }),
          (0, ke.jsxs)("div", {
            className: bn,
            children: [
              (0, ke.jsx)(i, {
                classMix: Cn,
                isTruncationAvailable: !0,
                text: _.readOrEmpty(
                  "user_missions.hub.reward_progress.win_back_quest_progress.title",
                ).replace(
                  "{{progress}}",
                  _.readOrEmpty(
                    "user_missions.hub.reward_progress.win_back_quest_progress.progress",
                  )
                    .replace("{{current}}", Pn.formatNumber("integral", d))
                    .replace("{{total}}", Pn.formatNumber("integral", c)),
                ),
              }),
              (0, ke.jsx)(i, {
                classMix: vn,
                isTruncationAvailable: !0,
                text: _.readOrEmpty(
                  "user_missions.hub.reward_progress.win_back_quest_progress.sub_title",
                ),
              }),
            ],
          }),
          (0, ke.jsxs)("div", {
            className: Nn,
            children: [
              (0, ke.jsxs)("div", {
                className: yn,
                onWheel: o.handleMouseWheel,
                children: [
                  (0, ke.jsx)(j, {
                    classNames: { wrapper: n(In, a && jn) },
                    children: (0, ke.jsxs)("div", {
                      className: kn,
                      style: { width: `${u}rem` },
                      children: [
                        (0, ke.jsx)(is, {
                          value: d,
                          size: "full",
                          maxValue: c,
                          className: Mn,
                          children: (0, ke.jsx)($, { initValue: d - m, initMaxValue: c }),
                        }),
                        (0, ke.jsx)(fn, { classNames: { questStatus: Rn, quest: En } }),
                      ],
                    }),
                  }),
                  (0, ke.jsx)(s, { classNames: { base: wn } }),
                ],
              }),
              (0, ke.jsx)("div", { className: Sn, children: (0, ke.jsx)(en, {}) }),
            ],
          }),
        ],
      })
    );
  }),
  On = {
    rootId: y
      .resolve("aliases")
      .read((e) =>
        e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
      ),
    context: "model.winBackProgress",
  };
function Tn() {
  return (0, ke.jsx)(Ga, { options: On, children: (0, ke.jsx)(Bn, {}) });
}
var An = "RewardProgressBlock_bf1cc1f3";
var Ln = L(function () {
    const { model: e } = ba(),
      s = e.progressType.get();
    return (0, ke.jsx)("div", {
      className: An,
      children: (() => {
        switch (s) {
          case Ca.EpicQuest:
            return (0, ke.jsx)(Ha, {});
          case Ca.WinBack:
            return (0, ke.jsx)(Tn, {});
          default:
            return (console.error(`Unreachable branch in progress type: ${s}`), null);
        }
      })(),
    });
  }),
  Dn = {
    rootId: y
      .resolve("aliases")
      .read((e) =>
        e.user_missions.hub.basicMissions.DailyMissionsSection.RewardProgressBlock("resId"),
      ),
  };
function Wn() {
  return (0, ke.jsx)(ha, {
    options: Dn,
    children: (0, ke.jsx)(T, { children: (0, ke.jsx)(Ln, {}) }),
  });
}
var Fn = "DailyMissions_c4fedd54",
  Hn = "DailyMissions_title_6ad6e593",
  Gn = "DailyMissions_content_22c598b5",
  Vn = "DailyMissions_missionsBlock_778a9b79",
  qn = "DailyMissions_rewardProgress_73a64666",
  $n = y.resolve("strings"),
  zn = L(function () {
    const { model: e } = mt(),
      s = e.dailyMissionsBlockStatus.get();
    return (0, ke.jsxs)("div", {
      className: Fn,
      children: [
        s.isEnabled &&
          (0, ke.jsx)("div", {
            className: Hn,
            children: $n.readOrEmpty("user_missions.hub.basic_missions.daily.title"),
          }),
        (0, ke.jsxs)(ie, {
          className: Gn,
          border: "contour",
          children: [
            (0, ke.jsx)(vi, { content: (0, ke.jsx)(br, {}), className: Vn, ...s }),
            (0, ke.jsx)(vi, {
              content: (0, ke.jsx)(xa, {}),
              ...e.premiumDailyMissionsBlockStatus.get(),
              className: Vn,
            }),
            (0, ke.jsx)(vi, {
              content: (0, ke.jsx)(Wn, {}),
              ...e.rewardProgressBlockStatus.get(),
              className: qn,
            }),
          ],
        }),
      ],
    });
  }),
  Un = {
    rootId: y
      .resolve("aliases")
      .read((e) => e.user_missions.hub.basicMissions.DailyMissionsSection.MainView("resId")),
  };
function Qn() {
  return (0, ke.jsx)(dt, { options: Un, children: (0, ke.jsx)(zn, {}) });
}
var [Yn, Xn] = E()(
    ({ observableModel: e }) => ({
      ...e.primitives([
        "isDailySectionAvailable",
        "isWeeklySectionAvailable",
        "isPMSectionAvailable",
      ]),
    }),
    ne,
  ),
  Jn = "BasicMissions_1ecd0546",
  Kn = "BasicMissions_section_37456c06",
  Zn = "BasicMissions_rightCards_9fb1ec2c",
  el = y.resolve("aliases"),
  sl = { rootId: el.read((e) => e.user_missions.hub.basicMissions.WeeklyMissions("resId")) },
  il = { rootId: el.read((e) => e.user_missions.hub.basicMissions.PersonalMissions("resId")) },
  tl = L(function () {
    const { model: e } = Xn();
    return (0, ke.jsxs)("div", {
      className: Jn,
      children: [
        e.isDailySectionAvailable.get() &&
          (0, ke.jsx)("div", { className: Kn, children: (0, ke.jsx)(Qn, {}) }),
        e.isWeeklySectionAvailable.get() &&
          (0, ke.jsx)("div", {
            className: Kn,
            children: (0, ke.jsxs)(ie, {
              className: Zn,
              border: "contour",
              children: [
                (0, ke.jsx)(_s, {
                  options: sl,
                  children: (0, ke.jsx)(_i, { fullHeight: !e.isPMSectionAvailable.get() }),
                }),
                e.isPMSectionAvailable.get() &&
                  (0, ke.jsx)(ve, { options: il, children: (0, ke.jsx)(us, {}) }),
              ],
            }),
          }),
      ],
    });
  }),
  ol = { rootId: R.aliases.user_missions.hub.basicMissions.MainView("resId") };
function rl() {
  return (0, ke.jsx)(Yn, { options: ol, children: (0, ke.jsx)(tl, {}) });
}
export { rl as default };
