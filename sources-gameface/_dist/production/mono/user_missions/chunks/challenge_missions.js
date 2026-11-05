import { r as e } from "./rolldown-runtime.js";
import {
  $ as s,
  $t as a,
  C as t,
  Dn as n,
  Dt as i,
  En as r,
  Gt as l,
  H as c,
  I as o,
  It as d,
  J as m,
  Jt as _,
  K as u,
  Kt as h,
  M as g,
  Mt as b,
  N as p,
  Nn as f,
  Ot as x,
  P as v,
  Q as j,
  Qt as y,
  S as N,
  St as w,
  T as I,
  Tt as C,
  U as k,
  V as S,
  W as T,
  Wt as D,
  X as E,
  Xt as P,
  Y as M,
  Z as B,
  Zt as A,
  _t as $,
  a as O,
  an as L,
  c as z,
  cn as H,
  ct as V,
  en as W,
  et as K,
  f as q,
  fn as F,
  gn as X,
  i as Y,
  in as U,
  j as G,
  jt as J,
  kn as Q,
  n as Z,
  nn as ee,
  o as se,
  pn as ae,
  q as te,
  qt as ne,
  r as ie,
  s as re,
  st as le,
  t as ce,
  tn as oe,
  tt as de,
  w as me,
  x as _e,
} from "./lib.js";
import { i as ue, r as he, t as ge } from "./get_reward_image.js";
var be = e(n(), 1),
  pe = { tension: 800, friction: 40 },
  fe = {
    from: { opacity: 0, transform: "translateY(50px)" },
    to: { opacity: 1, transform: "translateY(0px)" },
    leave: { opacity: 0, transform: "translateY(0px)" },
  },
  xe = (e, s, a) => {
    const t = (0, be.useRef)(!1);
    return b({
      from: "left" === e ? { transform: "translateX(-100%)" } : { transform: "translateY(100%)" },
      to: { transform: "translate(0%, 0%)" },
      config: pe,
      immediate: t.current,
      onRest: () => {
        t.current || ((t.current = !0), s?.());
      },
      onStart: () => {
        a?.();
      },
    });
  },
  ve = "active",
  je = "new",
  ye = "normal",
  Ne = ["gold", "credits", "freeXP", "crystal", "equipCoin", "bptaler"],
  we = "style_2d",
  Ie = "crew_member",
  Ce = "vehicle",
  ke = "attachments_set",
  Re = "improved_equipment",
  Se = "currencies",
  Te = "gui_vehicle_menu_open",
  De = "minimize",
  Ee = "bp_unlock_big",
  Pe = "dt_locked_reset_button",
  Me = (function (e) {
    return (
      (e.INACTIVE = "inactive"),
      (e.ACTIVE = "active"),
      (e.FAILED = "failed"),
      (e.COMPLETED = "completed"),
      e
    );
  })({}),
  [Be, Ae] = w()(
    ({ observableModel: e }) => {
      const s = {
          ...e.primitives(["enabled", "selectedChallengeID"]),
          root: e.object(),
          challengesPacks: e.arrayClone("challengesPacks"),
          viewedChallenges: a.set([]),
          scrollTargetID: a.box(null),
          shouldScrollToActive: a.box(!1),
        },
        t = y(() => {
          const e = s.challengesPacks.get();
          return e
            ? L(e, (e) => ({
                complexity: e.complexity,
                challenges: L(e.challenges, (e) => {
                  const a = e.challengeID;
                  return s.viewedChallenges.has(a) ? { ...e, isNew: !1 } : e;
                }),
              }))
            : [];
        }),
        n = y(() => {
          const e = new Map();
          return (
            t.get().forEach((s) => {
              s.challenges.forEach((s) => {
                e.set(s.challengeID, s);
              });
            }),
            e
          );
        });
      W(
        () => s.root.get().activeChallengeID,
        A((e) => {
          s.shouldScrollToActive.get() &&
            e &&
            (s.scrollTargetID.set(e), s.shouldScrollToActive.set(!1));
        }),
      );
      const i = (e) => n.get().get(e),
        r = A((e) => {
          s.scrollTargetID.set(e);
        }),
        l = A(() => {
          s.shouldScrollToActive.set(!0);
        });
      return {
        ...s,
        setScrollTarget: r,
        enableScrollToActive: l,
        computes: {
          challenges: t,
          challengesById: n,
          getChallengesByComplexity: (e) =>
            y(() => t.get().find((s) => s.complexity === e)?.challenges || []),
          getChallengeByID: i,
          getCardStatus: (e) =>
            y(() => {
              const s = i(e);
              if (s) return s.state === Me.ACTIVE ? ve : s.isNew ? je : ye;
            }),
          getMissionState: (e, a) =>
            y(() => {
              const t = i(e),
                n = a === t?.completedMissions,
                r = n && s.root.get().activeChallengeID === s.selectedChallengeID.get();
              return a < t?.completedMissions
                ? "done"
                : n && t?.remainingAttempts < 1
                  ? "failed"
                  : r
                    ? "active"
                    : "locked";
            }),
        },
      };
    },
    ({ externalModel: e, model: s }) => {
      const a = e.createCallback(
          A((e) => (s.viewedChallenges.add(e), { selectedChallengeID: e })),
          "onSelectChallenge",
        ),
        t = e.createCallback((e, s = !1) => ({ action: e, isFree: s }), "onAction");
      return {
        selectChallenge: a,
        onAction: t,
        handleAction: (e, n = 0) => {
          if ("to_active_challenge" === e) {
            const { activeChallengeID: e } = s.root.get();
            return (s.setScrollTarget(e), a(e));
          }
          return "restart" === e || "activate" === e
            ? (s.enableScrollToActive(), t(e, n > 0))
            : t(e);
        },
        openPreview: e.createCallback((e) => e, "openPreview"),
      };
    },
  ),
  $e = (e, s = 0, a) =>
    b({ from: fe.from, to: e ? fe.to : fe.from, config: pe, delay: e ? s : 0, onRest: a }),
  Oe = (e, s, a, t) => {
    const n = s === e.completedMissions,
      i = n && a === t,
      r = s < e.completedMissions,
      l = n && e.remainingAttempts < 1;
    return r ? "done" : l ? "failed" : i ? "active" : "locked";
  },
  Le = { tension: 400, friction: 60, duration: 1e3 },
  ze = "ActiveLabel_e577414e",
  He = e(ne(), 1),
  Ve = f.resolve("strings"),
  We = ({ className: e }) =>
    (0, He.jsx)("div", {
      className: r(ze, e),
      children: Ve.readOrEmpty("user_missions.hub.challenge_missions.card.activeLabel"),
    }),
  Ke = "PreviewableReward_5e9e4c84",
  qe = "PreviewableReward_name_a3e59465",
  Fe = "PreviewableReward_label_62ca7a49",
  Xe = "PreviewableReward_iconPosition_9043e7b9",
  Ye = "PreviewableReward_icon_7cb83516",
  Ue = f.resolve("strings"),
  Ge = ({ kingReward: e, openPreview: s, labelKey: a, className: t, classNames: n }) => {
    const i = Ue.readOrEmpty(`user_missions.hub.challenge_missions.reward.${a}`);
    return (0, He.jsxs)("div", {
      className: r(Ke, t),
      children: [
        (0, He.jsx)(re, {
          type: "preview",
          size: "normal",
          onClick: () => {
            s({
              bonusType: e.bonusType,
              bonusId: e.id,
              styleID: e.styleID,
              attachmentsToken: e.value,
            });
          },
          className: Xe,
          classNames: { icon: Ye },
        }),
        e.label &&
          (0, He.jsx)(me, {
            classMix: r(qe, n?.name),
            text:
              "attachmentsTitle" !== a
                ? e.label
                : Ue.readOrEmpty(`quests.bonusName.attachments_set.${e.icon}`, "silent") ||
                  Ue.readOrEmpty("quests.bonusName.attachments_set.default"),
          }),
        (0, He.jsx)("div", { className: r(Fe, n?.label), children: i }),
      ],
    });
  },
  Je = "AttachmentSet_name_ed624d0c",
  Qe = {
    base: "CurrenciesDescription_5a5f9bec",
    count: "CurrenciesDescription_count_2d00f3a7",
    count__credits: "CurrenciesDescription_count__credits_15e8d585",
    count__gold: "CurrenciesDescription_count__gold_95cfe941",
    count__freeXP: "CurrenciesDescription_count__freeXP_6eb2bc2d",
    count__crystal: "CurrenciesDescription_count__crystal_3b6d7fb5",
    count__tankXP: "CurrenciesDescription_count__tankXP_532fa33a",
    name: "CurrenciesDescription_name_6d26e764",
  },
  Ze = f.resolve("strings"),
  es = "ImprovedEquipment_4bafe1ca",
  ss = "ImprovedEquipment_name_3ad02c56",
  as = "ImprovedEquipment_label_a7a4323c",
  ts = R.strings.user_missions.hub.challenge_missions.reward,
  ns = "TankmanDescription_fb7e0eff",
  is = "TankmanDescription_name_ff60c953",
  rs = "TankmanDescription_label_3f65b2da",
  ls = R.strings.user_missions.hub.challenge_missions.reward,
  cs = (e) => {
    switch (e) {
      case se.heavyTank:
        return se.heavyTank;
      case se.lightTank:
        return se.lightTank;
      case se.mediumTank:
        return se.mediumTank;
      case se.SPG:
        return se.SPG;
      default:
        return se["AT-SPG"];
    }
  },
  os = ({ kingReward: e, classNames: s, vehicleTypeIconSize: a = O.x48x48 }) => {
    const { isInHangar: t, vehicleShortName: n, type: i, level: r, isElite: l } = e;
    return (0, He.jsx)("div", {
      className: s?.base,
      children: (0, He.jsxs)(Y, {
        children: [
          (0, He.jsx)(Y.Level, { className: s?.level, value: r, numberType: z.numberTypes.roman }),
          (0, He.jsx)(Y.Type, { className: s?.typeIcon, type: cs(i), premium: l, size: a }),
          (0, He.jsx)(Y.Name, { className: s?.name, children: n }),
          t && (0, He.jsx)("div", { className: s?.vehicleInHangar }),
        ],
      }),
    });
  },
  ds = "VehicleDescription_229a36fc",
  ms = "VehicleDescription_namePosition_3eb3146b",
  _s = "VehicleDescription_name_79570ca1",
  us = "VehicleDescription_vehicleCaption_f2842983",
  hs = "VehicleDescription_vehicleInHangar_37261f1",
  gs = "VehicleDescription_iconPosition_460dc8ce",
  bs = "VehicleDescription_icon_7bb8a458",
  ps = R.strings.user_missions.hub.challenge_missions.reward,
  fs = {
    [Ie]: ({ kingReward: e }) => {
      const { label: s } = e;
      return (0, He.jsxs)("div", {
        className: ns,
        children: [
          (0, He.jsx)("div", { className: is, children: s }),
          (0, He.jsx)("div", { className: rs, children: ls.tankmanTitle() }),
        ],
      });
    },
    [Ce]: ({ kingReward: e, openPreview: s }) =>
      (0, He.jsxs)("div", {
        className: ds,
        children: [
          (0, He.jsx)(re, {
            type: "preview",
            size: "normal",
            onClick: () => {
              s({
                bonusType: e.bonusType,
                bonusId: e.id,
                styleID: e.styleID,
                attachmentsToken: e.value,
              });
            },
            className: gs,
            classNames: { icon: bs },
          }),
          (0, He.jsx)(os, {
            kingReward: e,
            classNames: { base: ms, name: _s, level: _s, vehicleInHangar: hs },
          }),
          (0, He.jsx)("div", { className: us, children: ps.vehicleTitle() }),
        ],
      }),
    [we]: ({ kingReward: e, openPreview: s }) =>
      (0, He.jsx)(Ge, { kingReward: e, openPreview: s, labelKey: "style2DTitle" }),
    [ke]: ({ kingReward: e, openPreview: s }) =>
      (0, He.jsx)(Ge, {
        kingReward: e,
        openPreview: s,
        labelKey: "attachmentsTitle",
        classNames: { name: Je },
      }),
    [Re]: ({ kingReward: e }) => {
      const { label: s } = e;
      return (0, He.jsxs)("div", {
        className: es,
        children: [
          (0, He.jsx)(V, { className: ss, text: s }),
          (0, He.jsx)("div", { className: as, children: ts.improvedEquipment() }),
        ],
      });
    },
    [Se]: ({ kingReward: e }) => {
      const s = e.bonusType ?? "",
        a = Number(e.value ?? 0);
      return (0, He.jsxs)("div", {
        className: Qe.base,
        children: [
          (0, He.jsx)(V, {
            className: r(Qe.count, Qe[`count__${s}`]),
            text: Q.formatNumber("integral", a),
          }),
          (0, He.jsx)("div", {
            className: Qe.name,
            children: Ze.readOrEmpty(`quests.bonusName.${s}`),
          }),
        ],
      });
    },
  },
  xs = ({ kingRewardType: e, kingReward: s, openPreview: a }) => {
    const t = fs[Ne.includes(e) ? Se : e];
    return t
      ? (0, He.jsx)(t, { kingReward: s, openPreview: a })
      : (console.warn("Unknown king reward type:", e), null);
  },
  vs = f.resolve("images"),
  js = f.resolve("aliases"),
  ys = "KingReward_ad0db18a",
  Ns = "KingReward_background_944ce27a",
  ws = "KingReward_content_e5feff31",
  Is = "KingReward_rewardImage_ad25ebc3",
  Cs = "KingReward_controls_d0dba1f9",
  ks = "KingReward_overlay_f33628c4",
  Rs = "KingReward_count_a785a0ee",
  Ss = R.strings.user_missions.hub.challenge_missions.reward,
  Ts = $(function ({ kingRewardType: e, kingReward: s, missionId: a, className: t }) {
    const { model: n, controls: i } = Ae(),
      { selectedChallengeID: l } = n.root.get(),
      { bg: c } = ((e) => {
        const s = `userMissions.challenges.kingReward.c_${e}`;
        return {
          bg:
            vs.readOrEmpty(s, "silent") ||
            vs.readOrEmpty("userMissions.challenges.kingReward.default"),
        };
      })(l),
      { rewardImage: o, overlayImage: d } = ((e) => ({
        rewardImage: ue(e, ge.S600x450),
        overlayImage: e.overlayType
          ? he({ size: ge.S400x300, name: e.name, special: e.overlayType })
          : null,
      }))(s),
      m = ((e, s) =>
        x({
          resId: js.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
          contentId: Number(e.tooltipContentId),
          args: { tooltipId: e.tooltipId, missionId: s },
        }))(s, a),
      { count: _ } = s;
    return (0, He.jsxs)("div", {
      className: r(ys, t),
      children: [
        (0, He.jsx)("div", { className: Ns, style: { backgroundImage: `url(${c})` } }),
        (0, He.jsxs)("div", {
          className: ws,
          children: [
            (0, He.jsx)("div", {
              className: Is,
              style: { backgroundImage: `url(${o})` },
              ...m,
              children:
                d && (0, He.jsx)("div", { className: ks, style: { backgroundImage: `url(${d})` } }),
            }),
            (0, He.jsx)("div", {
              className: Cs,
              children: (0, He.jsx)(xs, {
                kingRewardType: e,
                kingReward: s,
                openPreview: i.openPreview,
              }),
            }),
            _ > 1 && (0, He.jsx)(V, { text: Ss.multi(), className: Rs, params: { count: _ } }),
          ],
        }),
      ],
    });
  }),
  Ds = "ConditionItem_493eba0b",
  Es = "ConditionItem_conditionIcon_3db9911b",
  Ps = "ConditionItem_conditionBg_c885d96f",
  Ms = "ConditionItem_conditionText_2f989dc8",
  Bs = "ConditionItem_conditionTitle_a283e646",
  As = "ConditionItem_conditionDescription_500fc72a",
  $s = "ConditionItem_multiline_6e29776a",
  Os = f.resolve("images"),
  Ls = ({ condition: e }) => {
    const { iconKey: s, titleData: a, descrData: t } = e,
      { breakpoint: n } = h(),
      i = n.weight >= _.large.weight,
      r = `userMissions.challenges.missionIcons.${i ? "c_128" : "c_80"}.${s}`,
      l = `userMissions.challenges.missionIcons.${i ? "c_128" : "c_80"}.folder`,
      c = Os.readOrEmpty(r, "silent") || Os.readOrEmpty(l);
    return (0, He.jsxs)("div", {
      className: Ds,
      children: [
        (0, He.jsx)("div", {
          className: Es,
          children: (0, He.jsx)("div", { className: Ps, style: { backgroundImage: `url(${c})` } }),
        }),
        (0, He.jsxs)("div", {
          className: Ms,
          children: [
            (0, He.jsx)("div", { className: Bs, children: a }),
            (0, He.jsx)(o, { text: `${t}`, classNames: { base: $s, text: As }, upgradeLegacy: !0 }),
          ],
        }),
      ],
    });
  },
  zs = "OrSeparator_6a9b8792",
  Hs = "OrSeparator_separatorArrow_99267c4f",
  Vs = "OrSeparator_separatorArrow__rotate_d7353f8f",
  Ws = f.resolve("strings"),
  Ks = () =>
    (0, He.jsxs)("div", {
      className: zs,
      children: [
        (0, He.jsx)("div", { className: r(Hs, Vs) }),
        (0, He.jsx)("span", {
          children: Ws.readOrEmpty("user_missions.hub.challenge_missions.card.or"),
        }),
        (0, He.jsx)("div", { className: Hs }),
      ],
    }),
  qs = {
    base: "ConditionsList_77f64f73",
    base__locked: "ConditionsList_base__locked_2b33f65e",
    condition: "ConditionsList_condition_1282d07b",
  },
  Fs = ({ mission: e, state: s }) =>
    (0, He.jsx)("div", {
      className: r(qs.base, qs[`base__${s}`]),
      children: L(e.postBattleCondition.items, (e, s, a) =>
        (0, He.jsxs)(
          "div",
          {
            className: qs.condition,
            children: [(0, He.jsx)(Ls, { condition: e }), s < a.length - 1 && (0, He.jsx)(Ks, {})],
          },
          `${s}`,
        ),
      ),
    }),
  Xs = "Overlay_7ff640ef",
  Ys = f.resolve("images");
var Us = "RewardImage_5b6b980",
  Gs = "RewardImage_count_21fdceb9";
var Js = "RewardName_text_debdee3b";
var Qs = "Reward_cd75c111",
  Zs = f.resolve("aliases"),
  ea = (0, be.forwardRef)(function (
    { reward: e, missionId: s, className: a = "", disabledRewardTooltip: t = !1, ...n },
    i,
  ) {
    const { tooltipContentId: l, tooltipId: c } = e,
      o = x({
        resId: Zs.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
        contentId: Number(l),
        args: { tooltipId: c, missionId: s },
      });
    return (
      (0, be.useEffect)(() => {
        t &&
          F.tooltip.hide(
            Zs.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
            Number(l),
          );
      }, [t, l]),
      (0, He.jsx)("div", { ref: i, ...o, className: r(Qs, a), children: n.children })
    );
  });
((ea.Image = function ({ showCounter: e, count: s, image: a, className: t = "" }) {
  return (0, He.jsx)("div", {
    className: r(Us, t),
    style: { backgroundImage: `url(${a})` },
    children:
      e &&
      (0, He.jsx)(V, {
        text: R.strings.user_missions.hub.challenge_missions.reward.multi(),
        className: Gs,
        params: { count: s },
      }),
  });
}),
  (ea.Name = function ({ reward: e, className: s = "" }) {
    const { label: a } = e;
    return (0, He.jsx)(V, { className: r(Js, s), text: Q.formatNumber("integral", Number(a)) });
  }),
  (ea.Overlay = function ({ size: e, special: s, className: a }) {
    return (0, He.jsx)("div", {
      className: r(Xs, a),
      style: { backgroundImage: `url(${Ys.readOrEmpty(`quests.bonuses.${e}.${I(s)}_overlay`)})` },
    });
  }));
var sa = {
  base: "RewardBlock_38712af9",
  rewardImage: "RewardBlock_rewardImage_d907cdef",
  overlay: "RewardBlock_overlay_1d46d904",
  overlay__small: "RewardBlock_overlay__small_f679120f",
  overlay__big: "RewardBlock_overlay__big_35869797",
  label: "RewardBlock_label_788aa697",
  label__credits: "RewardBlock_label__credits_4efa2e49",
  label__gold: "RewardBlock_label__gold_f705d51a",
  label__freeXP: "RewardBlock_label__freeXP_6615ab1e",
  label__crystal: "RewardBlock_label__crystal_6dd6cc02",
  label__tankXP: "RewardBlock_label__tankXP_8b84c167",
};
function aa({ reward: e, missionId: s, className: a = "", disabledRewardTooltip: t = !1 }) {
  const n = e.count ?? 0,
    i = Ne.includes(e.name ?? ""),
    c = n > 1 && !i,
    o = e.overlayType,
    d = l({ size: ge.Small }, { large: { size: ge.Big } });
  return (0, He.jsx)("div", {
    className: r(sa.base, a),
    children: (0, He.jsxs)(ea, {
      reward: e,
      missionId: s,
      disabledRewardTooltip: t,
      children: [
        (0, He.jsxs)("div", {
          className: sa.rewardImage,
          children: [
            (0, He.jsx)(ea.Image, { showCounter: c, count: n, image: ue(e, ge.Big) }),
            o &&
              (0, He.jsx)(ea.Overlay, {
                special: o,
                size: d.size,
                className: r(sa.overlay, sa[`overlay__${d.size}`]),
              }),
          ],
        }),
        i && (0, He.jsx)(ea.Name, { reward: e, className: r(sa.label, sa[`label__${e.name}`]) }),
      ],
    }),
  });
}
var ta = "RewardsList_bd99d393",
  na = "RewardsList_divider_1204c896",
  ia = "RewardsList_rewards_d4b0aa21",
  ra = ({ sortedRewards: e, missionId: s, disabledRewardTooltip: a = !1 }) =>
    (0, He.jsxs)("div", {
      className: ta,
      children: [
        e.length > 0 && (0, He.jsx)("div", { className: na }),
        (0, He.jsx)("div", {
          className: ia,
          children: L(e, (e, t) =>
            (0, He.jsx)(aa, { reward: e, missionId: s, disabledRewardTooltip: a }, `${t}_${e.id}`),
          ),
        }),
      ],
    }),
  la = {
    base: "CardContent_e7b3309a",
    base__done: "CardContent_base__done_d9024844",
    overlay: "CardContent_overlay_cd50a956",
    activeLabel: "CardContent_activeLabel_adf2deb8",
    card: "CardContent_card_1c10a3c3",
    kingReward: "CardContent_kingReward_36e46b8",
  };
function ca({
  mission: e,
  state: s,
  isLastCard: a,
  mainRewardType: t,
  disabledRewardTooltip: n = !1,
}) {
  const i = e.bonuses,
    l = e.id,
    c = ee(i, (e) => "" !== t && e.bonusType === t),
    o = H(a && c ? oe(i, (e) => e.bonusType !== t) : i);
  return (0, He.jsxs)("div", {
    className: r(la.base, la[`base__${s}`]),
    children: [
      "active" === s && (0, He.jsx)(We, { className: la.activeLabel }),
      (0, He.jsxs)("div", {
        className: la.overlay,
        children: [
          (0, He.jsxs)("div", {
            className: la.card,
            children: [
              (0, He.jsx)(Fs, { mission: e, state: s }),
              (0, He.jsx)(ra, { sortedRewards: o, missionId: l, disabledRewardTooltip: n }),
            ],
          }),
          c &&
            a &&
            (0, He.jsx)("div", {
              className: la.kingReward,
              children: (0, He.jsx)(Ts, { kingRewardType: t, kingReward: c, missionId: l }),
            }),
        ],
      }),
    ],
  });
}
var oa = "MissionNumber_2f758a67",
  da = "MissionNumber_missionNumber_560428d8",
  ma = "MissionNumber_missionNumber__active_10840043",
  _a = ({ number: e, active: s, className: a = "" }) =>
    (0, He.jsx)("div", {
      className: r(oa, a),
      children: (0, He.jsx)("div", { className: r(da, s && ma), children: e }),
    }),
  ua = "Content_fa80e432",
  ha = "Content_base__selected_da09528a";
function ga({ children: e, selected: s }) {
  return (0, He.jsx)("div", { className: r(ua, s && ha), children: e });
}
var ba = {
  disabled: "Slot_disabled_287eb554",
  base: "Slot_d5a6e7cd",
  base__done: "Slot_base__done_be1191df",
  content: "Slot_content_c4a2aafd",
  base__active: "Slot_base__active_71f19f5c",
  selected: "Slot_selected_c65825e6",
  selected__border: "Slot_selected__border_1228134",
};
function pa({ children: e, state: s, className: a, ...t }) {
  const n = "active" === s;
  return (0, He.jsx)("div", {
    ...t,
    className: r(ba.base, ba[`base__${s}`], a),
    children: (0, He.jsxs)("div", {
      className: ba.content,
      children: [
        ("locked" === s || "failed" === s) && (0, He.jsx)("div", { className: ba.disabled }),
        n && (0, He.jsx)("div", { className: r(ba.selected, ba.selected__border) }),
        (0, He.jsx)("div", { className: ba.selected }),
        (0, He.jsx)(ga, { selected: n, children: e }),
      ],
    }),
  });
}
var fa = {
    base: "Status_684476cf",
    icon: "Status_icon_6c4af360",
    base__done: "Status_base__done_35b9a31c",
    base__locked: "Status_base__locked_35b9a31c",
    icon__disabled: "Status_icon__disabled_8a3e5587",
    line: "Status_line_324edf86",
    shadow: "Status_shadow_75136b3b",
    glowInner: "Status_glowInner_c9a2a44d",
    blur: "Status_blur_fe6f30fc",
    glowBig: "Status_glowBig_eec956d5",
  },
  xa = "done",
  va = "locked",
  ja = ({ type: e, tooltipBodyText: s, disabled: a, className: t }) => {
    const n = i({ body: s });
    return (0, He.jsxs)("div", {
      className: r(fa.base, fa[`base__${e}`], t),
      children: [
        (0, He.jsx)("div", { className: fa.glowBig }),
        (0, He.jsx)("div", { className: fa.line }),
        (0, He.jsx)("div", { className: fa.shadow }),
        (0, He.jsx)("div", { className: fa.glowInner }),
        (0, He.jsx)("svg", {
          width: "42",
          height: "42",
          viewBox: "0 0 42 42",
          className: fa.blur,
          children: (0, He.jsx)("g", {
            children: (0, He.jsx)("circle", { cx: "21", cy: "21", r: "3" }),
          }),
        }),
        (0, He.jsx)("div", { className: r(fa.icon, a && fa.icon__disabled), ...n }),
      ],
    });
  },
  ya = {
    base: "Card_52e1a4f9",
    missionNumber: "Card_missionNumber_e5ee23b0",
    base__locked: "Card_base__locked_f4c22d1c",
    base__failed: "Card_base__failed_f4c22d1c",
    base__done: "Card_base__done_f4c22d1c",
    base__active: "Card_base__active_f4c22d1c",
    slot: "Card_slot_6fc1552c",
    slot__wideCard: "Card_slot__wideCard_b14825c3",
    status: "Card_status_ee4f9e1d",
    shimmerContainer: "Card_shimmerContainer_6c3e43d7",
    shimmer: "Card_shimmer_5d9bc25a",
  },
  Na = f.resolve("strings"),
  wa = "user_missions.tooltip.hub.card";
function Ia({
  mission: e,
  missionNumber: s,
  state: a,
  mainRewardType: t,
  isLastCard: n,
  className: i,
  disabledRewardTooltip: l = !1,
}) {
  const c = e.bonuses,
    o = ((e) => {
      const [s, a] = b(() => ({
        from: { transform: "skewY(-20deg) translateY(-100%)" },
        to: { transform: "skewY(-20deg) translateY(-100%)" },
        config: Le,
      }));
      return (
        (0, be.useEffect)(() => {
          "active" === e &&
            a.start({
              from: { transform: "skewY(-20deg) translateY(-100%)" },
              to: { transform: "skewY(-20deg) translateY(100%)" },
              delay: 1e3,
            });
        }, [e, a]),
        s
      );
    })(a),
    d = (0, be.useRef)(a),
    m = ((e) =>
      "done" === e
        ? Na.readOrEmpty(`${wa}.completed`)
        : "locked" === e
          ? Na.readOrEmpty(`${wa}.disabled`)
          : "")(a),
    _ = ((e) => ("done" === e ? xa : "active" !== e ? va : void 0))(a),
    u = ((e) => "active" === e || "failed" === e)(a),
    h = ((e) => "done" === e || "locked" === e)(a);
  (0, be.useEffect)(() => {
    const e = d.current;
    ("active" === a && "active" !== e && ae.sound(Ee),
      "failed" === a && "failed" !== e && ae.sound(Pe),
      (d.current = a));
  }, [a]);
  const g = ee(c, (e) => "" !== t && e.bonusType === t);
  return (0, He.jsx)("div", {
    className: r(ya.base, ya[`base__${a}`], i),
    children: (0, He.jsxs)(pa, {
      state: a,
      className: r(ya.slot, g && n && ya.slot__wideCard),
      children: [
        "active" === a &&
          (0, He.jsx)("div", {
            className: ya.shimmerContainer,
            children: (0, He.jsx)(J.div, { style: o, className: ya.shimmer }),
          }),
        (0, He.jsx)(_a, { number: s, active: u, className: ya.missionNumber }),
        (0, He.jsx)(ca, {
          mission: e,
          state: a,
          isLastCard: n,
          mainRewardType: t,
          disabledRewardTooltip: l,
        }),
        _ &&
          (0, He.jsx)("div", {
            className: ya.status,
            children: (0, He.jsx)(ja, { type: _, disabled: !h || l, tooltipBodyText: m }),
          }),
      ],
    }),
  });
}
var Ca = "ReplayBlock_4b4cbc0b",
  ka = "ReplayBlock_infoBlock_f3445bd4",
  Ra = "ReplayBlock_text_dbfcc0fa",
  Sa = "ReplayBlock_currentNumber_d6ce45cb",
  Ta = "ReplayBlock_currentNumber__complete_d0a4bd99",
  Da = "ReplayBlock_completedText_b0e0a907",
  Ea = "ReplayBlock_infoIcon_d1694385",
  Pa = f.resolve("strings"),
  Ma = "user_missions.hub.challenge_missions";
function Ba({ selectedChallenge: e, className: s = "" }) {
  const a = e.allowedCompletions,
    t = e.completions,
    n = i({
      header: Pa.readOrEmpty("user_missions.tooltip.hub.replay.header"),
      body: Pa.readOrEmpty("user_missions.tooltip.hub.replay.body"),
    });
  return (0, He.jsx)("div", {
    className: r(Ca, s),
    children: (0, He.jsxs)("div", {
      className: ka,
      ...n,
      children: [
        (0, He.jsx)("div", {
          className: Ra,
          children: (0, He.jsx)(me, {
            text: Pa.readOrEmpty(`${Ma}.header.numberTemplate`),
            binding: {
              currentNumber: (0, He.jsx)("span", { className: r(Sa, a === t && Ta), children: t }),
              commonNumber: (0, He.jsx)("span", { children: a }),
            },
          }),
        }),
        (0, He.jsx)("div", { className: Da, children: Pa.readOrEmpty(`${Ma}.replay.completed`) }),
        (0, He.jsx)("div", { className: Ea }),
      ],
    }),
  });
}
var Aa = "CardsList_cardsWrapper_6c2823cb",
  $a = "CardsList_cardsWrapper__inactive_87faefde",
  Oa = "CardsList_questCard_4309168",
  La = "CardsList_questCard__last_a714fc36",
  za = "CardsList_additionalMargin_ffdbf123",
  Ha = ({
    dragging: e,
    selectedChallenge: s,
    missions: a,
    activeChallengeID: t,
    selectedChallengeID: n,
    mainRewardType: i,
    cardsRef: l,
    replayRef: c,
  }) => {
    const [o, d] = (0, be.useState)(!1);
    return (0, He.jsxs)("div", {
      className: r(Aa, e && $a),
      ref: l,
      onMouseDown: () => d(!0),
      onMouseUp: () => d(!1),
      onMouseLeave: () => d(!1),
      children: [
        L(a, (l, c, d) =>
          (0, He.jsx)(
            Ia,
            {
              disabledRewardTooltip: e || o,
              missionNumber: c + 1,
              mission: l,
              className: r(Oa, c === a.length - 1 && La),
              state: Oe(s, c, t, n),
              mainRewardType: i,
              isLastCard: c === d.length - 1,
            },
            `${l.id}_${c}`,
          ),
        ),
        (0, He.jsx)("div", {
          ref: c,
          children:
            s.allowedCompletions > 1
              ? (0, He.jsx)(Ba, { selectedChallenge: s })
              : (0, He.jsx)("div", { className: za }),
        }),
      ],
    });
  },
  Va = {
    kingReward: "StickyKingReward_kingReward_784e7ea7",
    kingReward__active: "StickyKingReward_kingReward__active_e3d84edb",
    kingReward__failed: "StickyKingReward_kingReward__failed_9232f04b",
    lip: "StickyKingReward_lip_fa4cc4ea",
  },
  Wa = ({ state: e, kingRewardRef: s, kingReward: a, mainRewardType: t, missionId: n }) =>
    (0, He.jsxs)("div", {
      className: r(Va.kingReward, Va[`kingReward__${e}`]),
      ref: s,
      children: [
        (0, He.jsx)("div", { className: Va.lip }),
        (0, He.jsx)(Ts, { kingRewardType: t, kingReward: a, missionId: n }),
      ],
    }),
  Ka = "left",
  qa = "right",
  Fa = "both",
  Xa = "none",
  Ya = {
    base: "CardsContent_5a377872",
    mask: "CardsContent_mask_af240217",
    mask__both: "CardsContent_mask__both_e9f58edc",
    mask__left: "CardsContent_mask__left_cc482a2a",
    mask__right: "CardsContent_mask__right_933e7016",
    maskReward: "CardsContent_maskReward_78f7ce87",
    scrollWrapper: "CardsContent_scrollWrapper_e65fe5a6",
    scrollBar: "CardsContent_scrollBar_ddc6ce4b",
    kingReward: "CardsContent_kingReward_3201ccb6",
    kingReward__done: "CardsContent_kingReward__done_a3c56347",
  },
  Ua = $(function ({ selectedChallenge: e, enableAnimation: a = !1 }) {
    const { model: t } = Ae(),
      n = (0, be.useRef)(null),
      i = (0, be.useRef)(null),
      l = (0, be.useRef)(null),
      c = (0, be.useRef)(null),
      [o, d] = (0, be.useState)(!1),
      [m, _] = (0, be.useState)(!1),
      { api: u } = de(),
      { animationScroll: h, applyScroll: g } = u,
      { activeChallengeID: p } = t.root.get(),
      f = e?.challengeID,
      x = e?.missions,
      v = e?.mainRewardType ?? "",
      y = x ? U(x, x.length - 1) : void 0,
      N = y?.bonuses ? ee(y.bonuses, (e) => "" !== v && e.bonusType === v) : void 0,
      [w, I] = b(() => ({ maskStop: 100, isSticky: 0, config: { precision: 0.1 } })),
      C = B(u, E.horizontal, void 0, { gapBeforeStart: 5 }),
      [k, R] = K(u),
      S = (0, be.useCallback)(() => {
        if (!l.current || !e) return 0;
        const s = e.completedMissions,
          a = l.current.children[s] || n.current;
        return a ? a.offsetLeft - 40 : 0;
      }, [e]),
      T = $e(a, 100, () => g(S())),
      D = (0, be.useCallback)(() => {
        const e = i.current,
          s = c.current;
        if (!e) return;
        if (!s) return void I.start({ maskStop: e.offsetWidth, isSticky: 1, immediate: !0 });
        const a = h.scrollPosition.get(),
          t = n.current,
          r = e.offsetWidth,
          l = s.offsetWidth,
          o = t?.offsetWidth || 0,
          [d, m] = u.getBounds();
        if (a < m - o) {
          const e = r - l;
          I.start({ maskStop: e, isSticky: 1, immediate: !0 });
        } else I.start({ maskStop: r, isSticky: 0, immediate: !0 });
      }, [h.scrollPosition, I, u]),
      M = (0, be.useCallback)(() => {
        (_(!0), D());
      }, [D]),
      A = (0, be.useCallback)(() => {
        (D(), m && h.scrollPosition.idle && _(!1));
      }, [h.scrollPosition, D, m]);
    if (
      ((0, be.useEffect)(
        () => (
          P(() => {
            D();
          }),
          u.events.on("mouseWheel", M),
          u.events.on("change", A),
          u.events.on("resizeHandled", D),
          () => {
            (u.events.off("mouseWheel", M),
              u.events.off("change", A),
              u.events.off("resizeHandled", D));
          }
        ),
        [u, M, A, I, D],
      ),
      (0, be.useEffect)(() => {
        P(() => {
          "idle" === C.type && h.scrollPosition.idle && (_(!1), g(h.scrollPosition.get()));
        });
      }, [h.scrollPosition, g, C.type]),
      (0, be.useEffect)(() => d("dragging" === C.type), [C.type]),
      (0, be.useEffect)(
        () => (
          p === f && g(S()),
          u.events.on("resizeHandled", () => g(S())),
          () => {
            u.events.off("resizeHandled", () => g(S()));
          }
        ),
        [u, p, g, S, f],
      ),
      !e)
    )
      return null;
    const $ = o || m;
    return (0, He.jsxs)(J.div, {
      style: T,
      className: Ya.base,
      children: [
        (0, He.jsx)("div", {
          className: r(
            Ya.mask,
            Ya[`mask__${((O = k), (L = R), O || L ? (O ? (L ? Xa : qa) : Ka) : Fa)}`],
          ),
          ref: i,
          children: (0, He.jsx)(J.div, {
            className: Ya.maskReward,
            style: {
              maskImage: w.maskStop.to(
                (e) => `linear-gradient(to right, #000 ${e}px, transparent ${e}px)`,
              ),
            },
            children: (0, He.jsx)(j, {
              classNames: { wrapper: Ya.scrollWrapper },
              children:
                x &&
                f &&
                (0, He.jsx)(Ha, {
                  dragging: $,
                  selectedChallenge: e,
                  missions: x,
                  activeChallengeID: p,
                  selectedChallengeID: f,
                  mainRewardType: v,
                  cardsRef: l,
                  replayRef: n,
                }),
            }),
          }),
        }),
        N &&
          e &&
          y &&
          f &&
          x &&
          (0, He.jsx)(J.div, {
            className: r(
              Ya.kingReward,
              "done" === Oe(e, x.length - 1, p, f) && Ya.kingReward__done,
            ),
            style: { visibility: w.isSticky.to((e) => (1 === e ? "visible" : "hidden")) },
            children: (0, He.jsx)(Wa, {
              state: Oe(e, x.length - 1, p, f),
              kingRewardRef: c,
              kingReward: N,
              mainRewardType: v,
              missionId: y.id,
            }),
          }),
        (0, He.jsx)(s, { classNames: { base: Ya.scrollBar } }),
      ],
    });
    var O, L;
  }),
  Ga = "Badges_active_2b01effc",
  Ja = "Badges_active__shown_962cc4d1",
  Qa = "Badges_bubble_44df09e",
  Za = (0, be.memo)(function ({ status: e }) {
    const s = D(e) === ve;
    return (0, He.jsxs)(He.Fragment, {
      children: [
        e === ve &&
          (0, He.jsx)("div", {
            className: r(Ga, s && Ja),
            children: (0, He.jsx)(le, {
              path: "user_missions.hub.challenge_missions.missionsActive",
            }),
          }),
        e === je &&
          (0, He.jsx)(Z.Root, {
            className: Qa,
            children: (0, He.jsx)(Z.Value, {
              size: "medium",
              value: R.strings.user_missions.hub.challenge_missions.new(),
            }),
          }),
      ],
    });
  }),
  et = "Info_challengeName_7ddcece6",
  st = "Info_settings_386b6846",
  at = "Info_divider_5cd32879",
  tt = "Info_attempts_4f65ac9e",
  nt = "Info_attempts__disabled_e68e1244",
  it = "Info_attemptsIcon_cc763bd9",
  rt = "Info_completed_5702881a",
  lt = "Info_completedIcon_a3825991",
  ct = (0, be.memo)(function ({
    challengeName: e,
    completed: s,
    formattedCount: a,
    remainingAttempts: t,
  }) {
    const n = t > 0;
    return (0, He.jsxs)(He.Fragment, {
      children: [
        (0, He.jsx)("div", { className: et, children: (0, He.jsx)(ce, { text: e }) }),
        (0, He.jsx)("div", {
          className: st,
          children: s
            ? (0, He.jsxs)("div", {
                className: rt,
                children: [
                  (0, He.jsx)("span", { className: lt }),
                  (0, He.jsx)(le, {
                    path: "user_missions.hub.challenge_missions.missionsCompleted",
                  }),
                ],
              })
            : (0, He.jsxs)(He.Fragment, {
                children: [
                  (0, He.jsx)("div", { children: a }),
                  (0, He.jsx)("div", { className: at }),
                  (0, He.jsxs)("div", {
                    className: r(tt, !n && nt),
                    children: [t, (0, He.jsx)("span", { className: it })],
                  }),
                ],
              }),
        }),
      ],
    });
  }),
  ot = {
    base: "Content_fce2a30",
    background: "Content_background_b9b41a3",
    background__selected: "Content_background__selected_f0f8210c",
    pattern: "Content_pattern_80b99e79",
    pattern__easy: "Content_pattern__easy_15858571",
    pattern__medium: "Content_pattern__medium_8fccc978",
    pattern__hard: "Content_pattern__hard_fc4c8922",
    content: "Content_b6bbe7a6",
    timer: "Content_timer_6e8a2c03",
    accent: "Content_accent_9c27dd12",
  },
  dt = R.images.gui.maps.icons.userMissions.hub.challenge.background,
  mt = $(function ({ challengeID: e, complexity: s, selected: a }) {
    const { model: t } = Ae(),
      { breakpoint: n } = h(),
      i = t.computes.getChallengeByID(e),
      l = t.computes.getCardStatus(e).get(),
      c = i?.completedMissions ?? 0,
      o = i?.totalMissions ?? 0,
      d = i?.type ?? "",
      m = i?.expireTime ?? 0,
      u = i?.challengeName ?? "",
      b = i?.state,
      f = i?.remainingAttempts ?? 0,
      x = (0, He.jsx)(le, {
        path: "user_missions.hub.challenge_missions.missionsCount",
        params: {
          currentMissions: (0, He.jsx)("span", { className: ot.accent, children: c }),
          totalMissions: o,
        },
      }),
      j = "special" === d ? dt.additional.$dyn(`c_${e}`) : dt.basic();
    return (0, He.jsxs)("div", {
      className: ot.base,
      children: [
        l && (0, He.jsx)(Za, { status: l }),
        (0, He.jsx)("div", {
          className: r(ot.background, a && ot.background__selected),
          style: { backgroundImage: `url(${j})` },
        }),
        (0, He.jsx)("div", { className: r(ot.pattern, d && ot[`pattern__${s}`]) }),
        i &&
          (0, He.jsxs)("div", {
            className: ot.content,
            children: [
              b !== Me.COMPLETED &&
                (0, He.jsx)(
                  G,
                  {
                    type: v.accent,
                    format: m > 86400 ? g.compact : g.default,
                    size: n.weight < _.extraLarge.weight ? p.x24x24 : p.x32x32,
                    className: ot.timer,
                    start: m,
                  },
                  m,
                ),
              (0, He.jsx)(ct, {
                challengeName: u,
                completed: b === Me.COMPLETED,
                formattedCount: x,
                remainingAttempts: f,
              }),
            ],
          }),
      ],
    });
  }),
  _t = "Card_wrapper_96ab126",
  ut = "Card_f75461f4";
function ht({ challengeID: e, isSelected: s, onSelect: a, complexity: t, className: n, ...i }) {
  return (0, He.jsx)("div", {
    ...i,
    children: (0, He.jsx)(q, {
      classNames: { wrapper: _t, card: ut },
      className: n,
      selected: s,
      active: s,
      onClick: () => a(e),
      children: (0, He.jsx)(mt, { challengeID: e, complexity: t, selected: s }),
    }),
  });
}
var gt = {
    base: "Header_7811c695",
    content: "Header_content_ae11a84e",
    complexityIcon: "Header_complexityIcon_e1dd4f6",
    complexityIcon__hard: "Header_complexityIcon__hard_4a94b878",
    complexityIcon__medium: "Header_complexityIcon__medium_c8f36b2a",
    complexityIcon__easy: "Header_complexityIcon__easy_1d4962ab",
  },
  bt = f.resolve("strings");
function pt({ complexity: e, className: s }) {
  const a = i({
    body: bt.readOrEmpty("user_missions.hub.challenge_missions.complexity.tooltip.body"),
  });
  return (0, He.jsx)("div", {
    className: r(gt.base, s),
    children: (0, He.jsxs)("div", {
      className: gt.content,
      ...a,
      children: [
        (0, He.jsx)("div", { className: r(gt.complexityIcon, gt[`complexityIcon__${e}`]) }),
        (0, He.jsx)(le, { path: `user_missions.hub.challenge_missions.complexity.${e}` }),
      ],
    }),
  });
}
var ft = "Complexity_card__selected_cd2a2f69",
  xt = $(function ({ complexity: e }) {
    const { model: s, controls: a } = Ae(),
      { api: t } = m(),
      n = s.selectedChallengeID.get(),
      i = s.computes.getChallengesByComplexity(e).get(),
      l = (0, be.useCallback)(
        (e) => {
          a.selectChallenge(e);
          const s = document.querySelector(`[data-challenge-id="${e}"]`);
          if (!s) return;
          const [n, i] = t.getBounds(),
            r = t.animationScroll.scrollPosition.get(),
            l = t.getWrapperSize() ?? 0,
            c = ((e, s, a, t, n, i) => {
              const r = 0.03 * t,
                l = e + s,
                c = a + r;
              return e >= c && l <= a + t - r
                ? null
                : e < c
                  ? Math.max(n, e - r)
                  : Math.min(i, l - t + r);
            })(s.offsetTop, s.offsetHeight, r, l, n, i);
          null !== c && t.animationScroll.scrollPosition.start(c);
        },
        [t, a],
      );
    return (0, He.jsxs)(He.Fragment, {
      children: [
        (0, He.jsx)(pt, { complexity: e }),
        L(i, (s) => {
          const a = s.challengeID,
            t = n === a;
          return (0, He.jsx)(
            ht,
            {
              className: r(t && ft),
              challengeID: a,
              isSelected: t,
              onSelect: l,
              complexity: e,
              "data-challenge-id": a,
            },
            a,
          );
        }),
      ],
    });
  }),
  vt = "ChallengeList_eefb9f3f",
  jt = "ChallengeList_verticalBar_9881b2c2",
  yt = $(function () {
    const { model: e } = Ae(),
      s = e.computes.challenges.get(),
      { api: a } = m();
    ie(a);
    const t = e.scrollTargetID.get();
    return (
      (0, be.useEffect)(() => {
        if (!t) return;
        const s = document.querySelector(`[data-challenge-id="${t}"]`);
        if (s) {
          const [e, t] = a.getBounds(),
            n = a.animationScroll.scrollPosition.get(),
            i = a.getWrapperSize() ?? 0,
            r = ((e, s, a, t, n, i) => {
              if (e >= a && e + s <= a + t) return null;
              const r = e - t / 2 + s / 2;
              return Math.max(n, Math.min(i, r));
            })(s.offsetTop, s.offsetHeight, n, i, e, t);
          null !== r && a.animationScroll.scrollPosition.start(r, { immediate: !0 });
        }
        e.setScrollTarget(null);
      }, [t, e, a]),
      (0, He.jsxs)(He.Fragment, {
        children: [
          (0, He.jsx)(u, {
            children: L(s, (e) =>
              e.challenges?.length
                ? (0, He.jsx)(xt, { complexity: e.complexity }, `challenge__${e.complexity}`)
                : null,
            ),
          }),
          (0, He.jsx)(te, { classNames: { base: jt } }),
        ],
      })
    );
  });
function Nt({ isAnimating: e = !1 }) {
  return (0, He.jsx)("div", {
    className: vt,
    style: { pointerEvents: e ? "none" : "auto", cursor: e ? "default" : "auto" },
    children: (0, He.jsx)(T, { children: (0, He.jsx)(yt, {}) }),
  });
}
var wt = {
    base: "ProgressInfo_8424c779",
    shields: "ProgressInfo_shields_16781924",
    shields__dimmed: "ProgressInfo_shields__dimmed_acbcf101",
    shield: "ProgressInfo_shield_16781924",
    shieldIcon: "ProgressInfo_shieldIcon_55d5061d",
    shieldIcon__fault: "ProgressInfo_shieldIcon__fault_f4da6e67",
    dashIcon: "ProgressInfo_dashIcon_fe02568c",
    attemptsText: "ProgressInfo_attemptsText_7e98713a",
    currentNumber: "ProgressInfo_currentNumber_54bf163d",
    restartBlock: "ProgressInfo_restartBlock_f649403c",
    remaining: "ProgressInfo_remaining_3c852f20",
  },
  It = f.resolve("aliases"),
  Ct = f.resolve("views"),
  kt = It.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
  Rt = Ct.read((e) => e.mono.user_missions.tooltips.challenges_shields_tooltip("resId"));
function St({ attempts: e, remainingAttempts: s, isFailed: a, isCompleted: t, className: n = "" }) {
  const i = x({ resId: kt, contentId: Rt });
  return (0, He.jsxs)("div", {
    className: r(wt.base, n),
    children: [
      (0, He.jsx)("div", {
        className: r(wt.shields, t && wt.shields__dimmed),
        children: Array.from({ length: e }).map((t, n) =>
          (0, He.jsxs)(
            "div",
            {
              className: wt.shield,
              children: [
                (0, He.jsx)("div", {
                  ...i,
                  className: r(wt.shieldIcon, (a || n > s - 1) && wt.shieldIcon__fault),
                }),
                n !== e - 1 && (0, He.jsx)("div", { className: wt.dashIcon }),
              ],
            },
            n,
          ),
        ),
      }),
      !t &&
        (0, He.jsxs)("div", {
          className: wt.attemptsText,
          ...i,
          children: [
            (0, He.jsx)(me, {
              text: Nn.readOrEmpty("user_missions.hub.challenge_missions.header.numberTemplate"),
              binding: {
                currentNumber: (0, He.jsx)("span", { className: wt.currentNumber, children: s }),
                commonNumber: (0, He.jsx)("span", { className: wt.commonNumber, children: e }),
              },
            }),
            (0, He.jsx)(me, {
              text: Nn.readOrEmpty("user_missions.hub.challenge_missions.header.remaining"),
              classMix: wt.remaining,
            }),
          ],
        }),
    ],
  });
}
var Tt = "RestartPrice_33839785",
  Dt = "RestartPrice_multiplier_a8d3f008",
  Et = "RestartPrice_multiplier__opacity_2c4332c7",
  Pt = "RestartPrice_restartIcon_5bfca1dc",
  Mt = "RestartPrice_restartIcon__opacity_83950c61",
  Bt = "RestartPrice_currency_4cba0a13",
  At = "RestartPrice_currencyIcon_8a20d0ca",
  $t = f.resolve("aliases"),
  Ot = f.resolve("views"),
  Lt = $t.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
  zt = Ot.read((e) => e.mono.user_missions.tooltips.challenges_restart_tooltip("resId"));
function Ht({ challengeData: e, hasOpacity: s = !1 }) {
  const a = e.restartCost,
    t = e.currencyType,
    n = e.isEnoughMoney,
    i = e.remainingFreeRestarts,
    l = i > 0,
    c = x({ resId: Lt, contentId: zt }),
    { breakpoint: o } = h(),
    d = o.weight >= _.large.weight ? N.medium : N.small;
  return (0, He.jsxs)("div", {
    className: Tt,
    ...c,
    children: [
      (0, He.jsx)("div", { className: r(Pt, s && Mt) }),
      l
        ? (0, He.jsx)(me, {
            text: Nn.readOrEmpty(`${wn}.multiplier`),
            binding: { count: i },
            classMix: r(Dt, s && Et),
          })
        : (0, He.jsx)(_e, {
            size: d,
            type: t,
            enough: !l && n,
            reverse: !0,
            classNames: { base: Bt, icon: At },
            children: a,
          }),
    ],
  });
}
var Vt = "RestartAction_6898d409",
  Wt = "RestartAction_button_3a224126",
  Kt = "RestartAction_info_6898d409",
  qt = "RestartAction_text_2929e8aa",
  Ft = "RestartAction_infoIcon_6c17b18",
  Xt = f.resolve("aliases"),
  Yt = f.resolve("views"),
  Ut = Xt.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
  Gt = Yt.read((e) => e.mono.user_missions.tooltips.challenges_restart_tooltip("resId"));
function Jt({ challengeData: e, onAction: s, hasButton: a }) {
  const n = e.remainingFreeRestarts,
    i = e.isEnoughMoney,
    r = e.currencyType === t.crystal,
    { breakpoint: l } = h(),
    o = x({ resId: Ut, contentId: Gt }),
    d = l.weight >= _.large.weight ? c.large : c.small,
    m = n > 0;
  return (0, He.jsxs)("div", {
    className: Vt,
    children: [
      (0, He.jsx)(Ht, { challengeData: e, hasOpacity: !a }),
      a
        ? (0, He.jsx)(S, {
            disabled: r && !i,
            onClick: () => s("restart"),
            className: Wt,
            size: d,
            children: m
              ? Nn.readOrEmpty(`${wn}.buttons.freeRestart`)
              : Nn.readOrEmpty(`${wn}.buttons.restart`),
          })
        : (0, He.jsxs)("div", {
            className: Kt,
            ...o,
            children: [
              m &&
                (0, He.jsx)(me, {
                  text: Nn.readOrEmpty("user_missions.hub.challenge_missions.header.restart.text"),
                  binding: { count: n },
                  classMix: qt,
                }),
              (0, He.jsx)("div", { className: Ft }),
            ],
          }),
    ],
  });
}
var Qt = "RestartInfo_cf799b5c",
  Zt = "RestartInfo_text_48b53e90",
  en = "RestartInfo_infoIcon_12406d73",
  sn = f.resolve("aliases"),
  an = f.resolve("views"),
  tn = sn.read((e) => e.user_missions.hub.challengeMissions.MainView("resId")),
  nn = an.read((e) => e.mono.user_missions.tooltips.challenges_restart_tooltip("resId"));
function rn({ challengeData: e }) {
  const s = e.remainingFreeRestarts,
    a = s > 0,
    t = x({ resId: tn, contentId: nn });
  return (0, He.jsxs)("div", {
    className: Qt,
    ...t,
    children: [
      (0, He.jsx)(Ht, { challengeData: e, hasOpacity: !0 }),
      a &&
        (0, He.jsx)(me, {
          text: Nn.readOrEmpty("user_missions.hub.challenge_missions.header.restart.text"),
          binding: { count: s },
          classMix: Zt,
        }),
      (0, He.jsx)("div", { className: en }),
    ],
  });
}
var ln = "RestartBlock_7a915f27";
function cn(e) {
  const { challengeData: s, className: a = "" } = e,
    t = s.remainingAttempts;
  return (0, He.jsx)("div", {
    className: r(ln, a),
    children: 0 === t ? (0, He.jsx)(Jt, { ...e }) : (0, He.jsx)(rn, { challengeData: s }),
  });
}
var on = "StatusInfo_162c825c",
  dn = "StatusInfo_timer_11d7de6d",
  mn = "StatusInfo_timerIcon_805f04b1",
  _n = "StatusInfo_timerLabel_cea31b20",
  un = "StatusInfo_timerWarningBlock_fcebd6",
  hn = "StatusInfo_divider_31e9fdd7",
  gn = "StatusInfo_timerUnavailableText_baa0a877",
  bn = "StatusInfo_timerUnavailableText__anotherActive_c29a992",
  pn = "StatusInfo_lockIcon_d41e4eed",
  fn = "StatusInfo_lockIcon__anotherActive_83adce2b",
  xn = "StatusInfo_timerWarningText_449e513",
  vn = "StatusInfo_button_db9e092d";
function jn({
  expireTime: e,
  isLocked: s,
  isAnotherActive: a,
  onAction: t,
  buttonSize: n,
  className: i = "",
}) {
  return (0, He.jsxs)("div", {
    className: r(on, i),
    children: [
      (0, He.jsx)(me, {
        text: Nn.readOrEmpty(`${wn}.timer.text`),
        binding: {
          timer: (0, He.jsx)(
            G,
            {
              size: p.x24x24,
              type: v.accent,
              format: e > 86400 ? g.compact : g.default,
              start: e,
              classNames: { icon: mn, label: _n },
            },
            e,
          ),
        },
        classMix: dn,
      }),
      s &&
        (0, He.jsxs)("div", {
          className: un,
          children: [
            (0, He.jsx)("div", { className: hn }),
            (0, He.jsx)(me, {
              text: Nn.readOrEmpty("user_missions.hub.challenge_missions.header.unavailable"),
              binding: {
                lockIcon: (0, He.jsx)("div", { className: r(pn, a && fn) }),
                text: (0, He.jsx)("span", {
                  className: xn,
                  children: a
                    ? Nn.readOrEmpty("user_missions.hub.challenge_missions.header.restriction")
                    : Nn.readOrEmpty(
                        "user_missions.hub.challenge_missions.header.vehicleRestriction",
                      ),
                }),
              },
              classMix: r(gn, a && bn),
            }),
            a &&
              (0, He.jsx)(S, {
                onClick: () => t("to_active_challenge"),
                className: vn,
                size: n,
                children: Nn.readOrEmpty(
                  "user_missions.hub.challenge_missions.header.buttons.toChallenge",
                ),
              }),
          ],
        }),
    ],
  });
}
var yn = {
    base: "Header_1d08ba03",
    labelBlock: "Header_labelBlock_9d52d682",
    completeText: "Header_completeText_a86a7997",
    completeIcon: "Header_completeIcon_c846c24",
    controls: "Header_controls_9dbb6d0f",
    name: "Header_name_4217eade",
    name__disabled: "Header_name__disabled_8b6614a6",
    attemptsSection: "Header_attemptsSection_b378f172",
    restartSection: "Header_restartSection_589df856",
    restartDivider: "Header_restartDivider_37e861e5",
    restartBlock: "Header_restartBlock_2b69d1e2",
    buttonWrapper: "Header_buttonWrapper_aeabf106",
    button: "Header_button_70aa1da5",
    shimmer: "Header_shimmer_825b28be",
  },
  Nn = f.resolve("strings"),
  wn = "user_missions.hub.challenge_missions.header",
  In = $(function ({ selectedChallenge: e, className: s = "", enableAnimation: a = !1 }) {
    const { model: t, controls: n } = Ae(),
      {
        activeChallengeID: i,
        isSuitableVehicles: o,
        selectedChallengeExpireTime: d,
      } = t.root.get(),
      m = e.state,
      u = e.challengeName,
      g = d,
      p = e.attempts,
      f = e.remainingAttempts,
      x = e.challengeID,
      v = e.remainingFreeRestarts,
      j = l(
        { buttonSize: c.small },
        { large: { buttonSize: c.medium }, extraLarge: { buttonSize: c.large } },
      ),
      { breakpoint: y } = h(),
      N = y.weight >= _.large.weight ? c.medium : c.extraSmall,
      w = m === Me.COMPLETED,
      I = m === Me.FAILED,
      C = m === Me.ACTIVE,
      R = m === Me.INACTIVE,
      T = Boolean(i && x !== i),
      D = T || !o,
      E = D || w,
      P = C ? "surrender" : "activate",
      M = $e(a, 0),
      B = b({
        from: { transform: "translateX(-100%)" },
        to: { transform: "translateX(100%)" },
        config: { duration: 700 },
        delay: 2800,
        loop: !0,
      }),
      A = (e) => {
        n.handleAction(e, v);
      };
    return (0, He.jsxs)(J.div, {
      style: M,
      className: r(yn.base, s, yn[`state_${m.toLowerCase()}`]),
      children: [
        !w &&
          (0, He.jsx)(jn, {
            expireTime: g,
            isLocked: D,
            isAnotherActive: T,
            onAction: A,
            buttonSize: N,
          }),
        w &&
          (0, He.jsx)("div", {
            className: yn.completeText,
            children: (0, He.jsx)(me, {
              text: Nn.readOrEmpty("user_missions.hub.challenge_missions.header.complete"),
              binding: { completeIcon: (0, He.jsx)("div", { className: yn.completeIcon }) },
            }),
          }),
        (0, He.jsxs)("div", {
          className: yn.controls,
          children: [
            (0, He.jsx)("div", { className: r(yn.name, E && yn.name__disabled), children: u }),
            (C || R) &&
              !D &&
              (0, He.jsxs)("div", {
                className: yn.buttonWrapper,
                children: [
                  (0, He.jsx)(S, {
                    onClick: () => A(P),
                    className: yn.button,
                    size: j.buttonSize,
                    theme: C ? k.secondary : k.primary,
                    disabled: D,
                    children: C
                      ? Nn.readOrEmpty(
                          "user_missions.hub.challenge_missions.header.buttons.surrender",
                        )
                      : Nn.readOrEmpty(
                          "user_missions.hub.challenge_missions.header.buttons.activate",
                        ),
                  }),
                  R && !D && (0, He.jsx)(J.div, { style: B, className: yn.shimmer }),
                ],
              }),
          ],
        }),
        (0, He.jsxs)("div", {
          className: r(yn.attemptsSection, E && yn.attemptsSection__disabled),
          children: [
            (0, He.jsx)(St, { attempts: p, remainingAttempts: f, isFailed: I, isCompleted: w }),
            !w &&
              (0, He.jsxs)("div", {
                className: r(yn.restartSection, E && yn.restartSection__disabled),
                children: [
                  (0, He.jsx)("div", { className: yn.restartDivider }),
                  (0, He.jsx)(cn, {
                    challengeData: e,
                    hasButton: !D,
                    isActive: C,
                    onAction: A,
                    className: yn.restartBlock,
                  }),
                ],
              }),
          ],
        }),
      ],
    });
  }),
  Cn = "ChallengeContent_3d909f5c",
  kn = "ChallengeContent_challengeInfo_cc1bc653",
  Rn = "ChallengeContent_transitionWrapper_2895b14e",
  Sn = "ChallengeContent_cards_ae124483",
  Tn = $(function () {
    const { model: e } = Ae(),
      { selectedChallengeID: s } = e.root.get(),
      a = e.computes.getChallengeByID(s),
      [t, n] = (0, be.useState)(!1),
      [i, r] = (0, be.useState)(!1),
      [l, c] = (0, be.useState)(!1),
      o = (0, be.useRef)(!1);
    ((0, be.useEffect)(() => {
      !o.current && s && (e.setScrollTarget(s), (o.current = !0));
    }, [s, e]),
      (0, be.useEffect)(() => {
        (r(!1), c(!0));
      }, [s]));
    const m = xe(
        "left",
        () => {
          n(!0);
        },
        C(Te),
      ),
      _ = xe("up"),
      u =
        ((h = a),
        (g = s),
        (b = () => {
          (r(!0), c(!1));
        }),
        (p = C(De)),
        d(h, {
          keys: g,
          from: fe.from,
          enter: () => async (e) => {
            (await e(fe.to), p?.(), b?.());
          },
          leave: fe.leave,
          config: pe,
        }));
    var h, g, b, p;
    return (0, He.jsxs)("div", {
      className: Cn,
      children: [
        (0, He.jsx)(J.div, { style: m, children: (0, He.jsx)(Nt, { isAnimating: l }) }),
        (0, He.jsx)(J.div, {
          className: kn,
          style: {
            transform: _.transform,
            pointerEvents: l ? "none" : "auto",
            cursor: l ? "default" : "auto",
          },
          children: u((e, s) => {
            if (!s) return null;
            const a = s,
              n = t && i;
            return (0, He.jsx)(J.div, {
              className: Rn,
              style: e,
              children:
                n &&
                (0, He.jsxs)(He.Fragment, {
                  children: [
                    (0, He.jsx)(In, { selectedChallenge: a, enableAnimation: !0 }),
                    (0, He.jsx)("div", {
                      className: Sn,
                      children: (0, He.jsx)(M, {
                        children: (0, He.jsx)(Ua, { selectedChallenge: a, enableAnimation: !0 }),
                      }),
                    }),
                  ],
                }),
            });
          }),
        }),
      ],
    });
  }),
  Dn = "ChallengesEmpty_2e7c4f64",
  En = "ChallengesEmpty_timerIcon_f155d3b5",
  Pn = "ChallengesEmpty_title_92c1e7c4",
  Mn = f.resolve("strings");
function Bn() {
  return (0, He.jsxs)("div", {
    className: Dn,
    children: [
      (0, He.jsx)("div", { className: En }),
      (0, He.jsx)("div", {
        className: Pn,
        children: Mn.readOrEmpty("user_missions.hub.challenge_missions.challenges_empty.title"),
      }),
    ],
  });
}
var An = "ChallengeMissions_f1737fb7",
  $n = "ChallengeMissions_empty_6a671d3b",
  On = $(function () {
    const { model: e } = Ae(),
      s = e.enabled.get();
    return (0, He.jsx)("div", {
      className: An,
      children: s
        ? (0, He.jsx)(Tn, {})
        : (0, He.jsx)("div", { className: $n, children: (0, He.jsx)(Bn, {}) }),
    });
  }),
  Ln = { rootId: R.aliases.user_missions.hub.challengeMissions.MainView("resId") };
function zn() {
  return (0, He.jsx)(Be, { options: Ln, children: (0, He.jsx)(On, {}) });
}
export { zn as default };
