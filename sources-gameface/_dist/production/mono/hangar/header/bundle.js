import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $n as t,
  Ar as a,
  Br as s,
  Dn as r,
  Dr as n,
  Fn as i,
  Fr as o,
  Gi as l,
  Gr as c,
  Hr as d,
  Ia as u,
  In as _,
  Ja as m,
  Or as b,
  Pi as p,
  Qa as v,
  Qn as f,
  Ti as g,
  Tr as h,
  aa as y,
  ai as x,
  an as N,
  ao as B,
  ar as j,
  ci as I,
  cr as E,
  dn as A,
  dr as C,
  ea as k,
  en as T,
  eo as P,
  fi as S,
  fn as M,
  ga as O,
  hi as W,
  hn as w,
  hr as D,
  in as H,
  jn as L,
  jr as V,
  kr as z,
  li as $,
  lr as F,
  mi as U,
  mn as G,
  oa as Q,
  on as q,
  pn as Y,
  pr as J,
  qr as K,
  ro as X,
  rr as Z,
  sn as ee,
  to as te,
  ui as ae,
  un as se,
  uo as re,
  ur as ne,
  xr as ie,
  zi as oe,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { n as le, t as ce } from "../chunks/divider.js";
import { a as de, i as ue, n as _e, r as me } from "../chunks/user_account_model.js";
var be = (function (e) {
    return ((e.Hangar = "hangar"), (e.Default = "default"), e);
  })({}),
  [pe, ve] = D("HeaderStateModel")((e) => ({ features: e.observableModel.dict("features") })),
  [fe, ge] = D()(
    ({ observableModel: e }) => ({
      ...e.primitives(["pageTitle", "backNavigationDescription", "backNavigationAllowed"]),
      infoButtons: e.arrayClone("infoButtons"),
    }),
    ({ externalModel: e }) => ({
      navigateTo: e.createCallback((e) => ({ name: e }), "onNavigate"),
      doInfoAction: e.createCallback((e) => ({ index: e }), "onInfoAction"),
    }),
  ),
  [he, ye] = D("CurrentVehicleInfoProvider")(({ observableModel: e }) => {
    const t = { vehicles: e.dictRef("vehicles") };
    return {
      vehicle: J.shallow(() => {
        try {
          const e = t.vehicles.entries()[0];
          if (e) {
            const [, t] = e;
            return JSON.parse(t.get());
          }
        } catch (e) {
          console.error("Error parsing JSON for current vehicle:", e);
        }
      }),
    };
  }, O),
  [xe, Ne] = D("HeaderProvider")(({ observableModel: e }) => e.primitives(["oldStyle"]), O),
  Be = "playerReady",
  je = "searchingBattle",
  Ie = "battleReady",
  [Ee, Ae] = D("PrebattleProvider")(
    ({ observableModel: e }) => {
      const t = {
          ...e.primitives([
            "currentMode",
            "currentModeId",
            "battleStatus",
            "queueType",
            "battleButtonAlwaysOn",
          ]),
          states: e.dict("states"),
          battleVehicle: e.transform((e) => {
            if (r(e.type)) return { ...e, type: e.type };
          }, "battleVehicle"),
        },
        a = J.primitive(() => t.battleStatus.get() === je),
        s = J.primitive(() => t.battleStatus.get() === Ie);
      return { ...t, computes: { isSearchingBattle: a, isBattleReady: s } };
    },
    ({ externalModel: e }) => ({
      actionPrebattle: e.createCallback((e) => ({ action: e }), "onAction"),
    }),
  ),
  [Ce, ke] = D("PremiumShopProvider")(
    ({ observableModel: e }) => ({ ...e.primitives({ isPremiumShop: "premiumShopEnabled" }) }),
    ({ externalModel: e }) => ({
      openPremiumShop: e.createCallbackNoArgs("onOpenExternalPremiumShop"),
    }),
  ),
  [Te, Pe] = D("TutorialProvider")(
    ({ observableModel: e }) => {
      const t = { triggers: e.arrayClone("triggers.items") },
        a = J.primitive(() => t.triggers.get().length);
      return { ...t, computes: { triggersCount: a } };
    },
    ({ externalModel: e }) => ({
      onTriggerActivated: e.createCallback(
        (e, t, a) => ({ componentId: e, triggerType: t, state: a }),
        "onTriggerActivated",
      ),
    }),
  ),
  Se = e(X(), 1),
  [Me, Oe] = D("BattleStartProvider")(
    ({ observableModel: e }) => ({ ...e.primitives(["tooltip"]) }),
    O,
  );
var We = "active",
  we = "ready",
  Re = "notReady",
  De = "disabled";
var He = {
    backgroundEffect: "BackgroundEffects_backgroundEffect_7bb0c1b5",
    base: "BackgroundEffects_47bdcaf9",
    backgroundEffect__rays: "BackgroundEffects_backgroundEffect__rays_4ebbd8d0",
  },
  Le = e(W(), 1),
  Ve = "rays";
var ze = (0, Se.memo)(function ({ buttonState: e, className: t }) {
    const a = e === We ? [Ve] : [];
    const r = re.resolve("videos"),
      n = c(a, {
        from: { opacity: 0 },
        enter: { opacity: 1 },
        leave: { opacity: 0 },
        config: { duration: 100 },
        trail: 500,
      });
    return (0, Le.jsx)("div", {
      className: te(He.base, t),
      children: n((e, t) =>
        (0, Le.jsx)(s.div, {
          style: e,
          children: (0, Le.jsx)(
            M,
            {
              loop: !0,
              autoplay: !0,
              src: r.readOrEmpty(`header_footer.battle_button.${t}`),
              className: te(He.backgroundEffect, He[`backgroundEffect__${t}`]),
            },
            t,
          ),
        }),
      ),
    });
  }),
  $e = "ButtonEffects_merged_86ab891d",
  Fe = "ButtonEffects_bdb5411e",
  Ue = (0, Se.memo)(function ({ className: e, onAnimationStarted: t }) {
    const a = re.resolve("videos"),
      s = $({ value: "small" }, { large: { value: "large" } });
    return (0, Le.jsx)("div", {
      className: te(Fe, e),
      children: (0, Le.jsx)(
        M,
        {
          autoplay: !0,
          loop: !0,
          onPlay: t,
          src: a.readOrEmpty(`header_footer.battle_button.foreground_${s.value}`),
          className: $e,
        },
        `glitterEffect-${s.value}`,
      ),
    });
  }),
  Ge = {
    textGlow: "ButtonText_textGlow_89301672",
    base: "ButtonText_841a3b01",
    base__ready: "ButtonText_base__ready_5e741ba3",
    breath: "ButtonText_breath_5e741ba3",
    textWrapper: "ButtonText_textWrapper_535d5dc6",
    base__disabled: "ButtonText_base__disabled_5e741ba3",
    text: "ButtonText_text_b56e6fa7",
    base__active: "ButtonText_base__active_5e741ba3",
    base__notReady: "ButtonText_base__notReady_5e741ba3",
    textOverlay: "ButtonText_textOverlay_1bcba7de",
  };
function Qe({ buttonState: e, buttonText: t, animationActive: a, onAnimationEnded: r }) {
  const n = d({
    opacity: a ? 0.9 : 0,
    config: { duration: a ? 3600 : 1e3, easing: a ? P.easeInCirc : P.easeOutCirc },
    onRest: () => {
      a && r();
    },
  });
  return e === We
    ? (0, Le.jsx)(s.div, { className: Ge.textGlow, style: n, children: t })
    : e === we
      ? (0, Le.jsx)("div", { className: Ge.textGlow, children: t })
      : null;
}
var qe = E(function ({
    actionType: e,
    buttonState: t,
    animationActive: a,
    onAnimationEnded: s,
    className: r,
  }) {
    const n = Ae(),
      i = re.resolve("strings"),
      o = B.toUpperCase(
        i.readOrEmpty(
          (function (e, t) {
            return "battleStartAction" === e
              ? "menu.headerButtons.battle.button.battle"
              : t
                ? "menu.headerButtons.notReady"
                : "menu.headerButtons.ready";
          })(e, n.model.states.get(Be)),
        ),
      );
    return (0, Le.jsxs)("div", {
      className: te(Ge.base, Ge[`base__${t}`], r),
      children: [
        (0, Le.jsx)(A, {
          classNames: { base: Ge.textWrapper, text: Ge.text, textOverlay: Ge.textOverlay },
          children: o,
        }),
        (0, Le.jsx)(Qe, { buttonState: t, buttonText: o, animationActive: a, onAnimationEnded: s }),
      ],
    });
  }),
  Ye = {
    background: "ButtonWrapper_background_5f66b44f",
    border: "ButtonWrapper_border_4e5ba0c2",
    button: "ButtonWrapper_button_ac00a3ae",
    button__disabled: "ButtonWrapper_button__disabled_5b8e9d9",
    background__disabled: "ButtonWrapper_background__disabled_4ab5c051",
    background__notReady: "ButtonWrapper_background__notReady_d27296f9",
    background__ready: "ButtonWrapper_background__ready_2853577d",
    background__appear: "ButtonWrapper_background__appear_22cf4f98",
    fadeIn: "ButtonWrapper_fadeIn_d27296f9",
    background__dissapear: "ButtonWrapper_background__dissapear_6a20b5f2",
    flicker: "ButtonWrapper_flicker_d27296f9",
    content: "ButtonWrapper_content_a523ce6e",
    button__ready: "ButtonWrapper_button__ready_d27296f9",
    button__notReady: "ButtonWrapper_button__notReady_d27296f9",
    overlay: "ButtonWrapper_overlay_ccea80e8",
  },
  Je = [we, Re],
  Ke = E(function ({
    buttonState: e,
    transitionActive: t,
    transitionFromState: a,
    actionType: s,
    children: r,
    className: n,
  }) {
    const i = Oe(),
      o = Ae(),
      l = i.model.tooltip.get(),
      c = (function (e) {
        const t = e.match(/{HEADER}(.*?){\/HEADER}/)?.[1],
          a = e.match(/{BODY}(.*?){\/BODY}/)?.[1],
          s = e.match(/{NOTE}(.*?){\/NOTE}/)?.[1],
          r = e.match(/{ATTENTION}(.*?){\/ATTENTION}/)?.[1];
        return b({
          header: t,
          body: a,
          alert: r,
          note: s,
          hasHtmlContent: !0,
          disabled: 0 === e.length,
        });
      })(l),
      d = e === De;
    const u = a && Je.includes(a) && Je.includes(e);
    return (0, Le.jsx)("div", {
      ...(d && l && c),
      className: n,
      children: (0, Le.jsxs)(_, {
        theme: _.themes.custom,
        disabled: d,
        autoAlignContent: !1,
        onClick: function () {
          d || o.controls.actionPrebattle(s);
        },
        className: te(Ye.button, Ye[`button__${e}`]),
        classNames: {
          background: te(Ye.background, Ye[`background__${e}`], t && !u && Ye.background__appear),
          content: Ye.content,
          border: Ye.border,
          overlay: Ye.overlay,
        },
        "data-test-id": "battleButton",
        soundTarget: "battleButton",
        children: [
          t &&
            !u &&
            (0, Le.jsx)("div", {
              className: te(Ye.background, Ye.background__dissapear, Ye[`background__${a}`]),
            }),
          r,
        ],
      }),
    });
  }),
  Xe = {
    hoverOverlay: "BattleButton_hoverOverlay_5196983d",
    buttonEffects: "BattleButton_buttonEffects_53b5d8e2",
    reflector: "BattleButton_reflector_47e1d14b",
    backgroundEffects: "BattleButton_backgroundEffects_815ae971",
    base: "BattleButton_40c20cf8",
    fadeIn: "BattleButton_fadeIn_ea4cde73",
    reflector__ready: "BattleButton_reflector__ready_ea4cde73",
    reflector__notReady: "BattleButton_reflector__notReady_a8ef3bf5",
    desaturation: "BattleButton_desaturation_fb74a8a1",
    desaturation__hidden: "BattleButton_desaturation__hidden_6167cc9c",
    buttonText: "BattleButton_buttonText_8108fe79",
  },
  Ze = "FightButton",
  et = "enabled_change",
  tt = Z("BattleButton", Xe.base),
  at = E(function ({ classNames: e }) {
    const t = Ae(),
      [a, s] = (0, Se.useState)(!1),
      [r, n] = (0, Se.useState)(!1),
      [i, l] = (0, Se.useState)(),
      { model: c, controls: d } = Pe(),
      u = c.computes.triggersCount(),
      _ = o(),
      m = "BATTLE_ROYALE_TOURNAMENT" === t.model.queueType.get(),
      b = "TRAINING" === t.model.currentMode.get(),
      p =
        (!t.model.states.get("playerCreator") && !b && t.model.states.get("readinessAvailable")) ||
        m
          ? "readyAction"
          : "battleStartAction",
      v = (function (e, t, a) {
        return t ? De : "battleStartAction" === e ? We : a ? Re : we;
      })(p, !t.model.states.get("actionEnabled"), t.model.states.get(Be)),
      f = I(v),
      g = v === De;
    return (
      (0, Se.useEffect)(
        () =>
          oe(() => {
            const e = y(c.triggers.get(), (e) => e.componentId === Ze);
            ((u > 0 && e) || (f && v !== f)) && d.onTriggerActivated(Ze, et, !0);
          }),
        [v, d, c.triggers, f, u],
      ),
      (0, Se.useEffect)(() => {
        f &&
          v !== f &&
          (n(!0),
          l(f),
          _.run(() => {
            n(!1);
          }, 600));
      }, [_, v, f]),
      (0, Se.useLayoutEffect)(
        () => () => {
          d.onTriggerActivated(Ze, et, !1);
        },
        [],
      ),
      (0, Le.jsxs)(tt, {
        className: e?.base,
        id: "fight-button",
        children: [
          (0, Le.jsx)(ze, { buttonState: v, className: te(Xe.backgroundEffects, e?.effect) }),
          (0, Le.jsxs)(Ke, {
            actionType: p,
            buttonState: v,
            transitionActive: r,
            transitionFromState: i,
            className: e?.content,
            children: [
              !g && (0, Le.jsx)("div", { className: te(Xe.reflector, Xe[`reflector__${v}`]) }),
              v === We &&
                (0, Le.jsx)(Ue, { className: Xe.buttonEffects, onAnimationStarted: () => s(!0) }),
              (0, Le.jsx)("div", { className: Xe.hoverOverlay }),
              (0, Le.jsx)("div", { className: te(Xe.desaturation, !g && Xe.desaturation__hidden) }),
              (0, Le.jsx)(qe, {
                actionType: p,
                buttonState: v,
                animationActive: a,
                onAnimationEnded: () => s(!1),
                className: Xe.buttonText,
              }),
            ],
          }),
        ],
      })
    );
  }),
  st = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Le.jsx)(Me, { options: e, children: (0, Le.jsx)(at, { ...t }) }),
  );
function rt() {
  const e = G().paramsStruct.routeType;
  return "string" == typeof e ? e : be.Default;
}
var nt = {
    border: "InfoButton_border_f3a2eae1",
    base: "InfoButton_74c97479",
    base__smallSize: "InfoButton_base__smallSize_c40e1b5c",
    base__mediumSize: "InfoButton_base__mediumSize_f347ecd3",
    content: "InfoButton_content_1cc251f9",
    content__label: "InfoButton_content__label_a89c101d",
    label: "InfoButton_label_5a5ddc63",
    icon: "InfoButton_icon_c58f1a93",
  },
  it = { small: "small", medium: "medium" },
  ot = { [it.small]: 16, [it.medium]: 24 },
  lt = (0, Se.forwardRef)(function (
    { size: e, infoType: t, label: a, tooltipHeader: s, tooltipBody: r, classNames: n = {}, ...i },
    o,
  ) {
    const l = s || r,
      c = b({ header: s, body: r }),
      d = S(e, ae);
    return (0, Le.jsxs)(_, {
      ...i,
      onClick: function (e) {
        (l && c.onClick(), i.onClick?.(e));
      },
      onMouseEnter: function (e) {
        (l && c.onMouseEnter(e), i.onMouseEnter?.(e));
      },
      onMouseLeave: function (e) {
        (c.onMouseLeave(), i.onMouseLeave?.(e));
      },
      ref: o,
      size: _.sizes.small,
      theme: _.themes.secondary,
      autoAlignContent: !1,
      className: te(nt.base, nt[`base__${e}Size`], i.className),
      classNames: { ...n, content: te(nt.content, a && nt.content__label, n?.content) },
      children: [
        (0, Le.jsx)("div", { className: nt.border }),
        (0, Le.jsx)(j, {
          className: nt.icon,
          path: `header_footer.info_icon_${t}_${d}`,
          height: ot[e],
          width: ot[e],
        }),
        a && (0, Le.jsx)("div", { className: nt.label, children: a }),
      ],
    });
  });
lt.sizes = it;
var ct = "NavigationBar_425ae997",
  dt = "NavigationBar_button_c5ece62",
  ut = "NavigationBar_button__backNavigation_7dc54008",
  _t = "NavigationBar_label_4840a20f",
  mt = "NavigationBar_icon_95c9bdbb",
  bt = "NavigationBar_iconImage_e695cd8e",
  pt = "NavigationBar_iconImage__default_dfd5b7a7",
  vt = "NavigationBar_iconImage__hover_c132ba6f",
  ft = "NavigationBar_iconImage__active_fbf5db52",
  gt = "NavigationBar_button__garageNavigation_69a10af0",
  ht = "NavigationBar_divider_7592acb0",
  yt = "NavigationBar_pageTitle_5847696c",
  xt = "NavigationBar_hiddenLabel_1fa48c6e",
  Nt = "NavigationBar_base__ready_69a10af0",
  Bt = "NavigationBar_base__animating_69a10af0",
  jt = "NavigationBar_hiddenLabelInner_8490d7c",
  It = "NavigationBar_infoButton_8aaee3f9",
  Et = "NavigationBar_infoButton__last_efa963fb";
function At({ classNames: e = {} }) {
  return (0, Le.jsxs)("div", {
    className: te(mt, e.icon),
    children: [
      (0, Le.jsx)("div", { className: te(bt, pt, e.iconImage, e.iconImage__default) }),
      (0, Le.jsx)("div", { className: te(bt, vt, e.iconImage, e.iconImage__hover) }),
      (0, Le.jsx)("div", { className: te(bt, ft, e.iconImage, e.iconImage__active) }),
    ],
  });
}
var Ct = E(function ({
    classNames: e = {},
    className: t,
    garageNavigationAllowed: a,
    battleButtonVisible: s,
  }) {
    const { model: r, controls: n } = ge(),
      i = ie(),
      o = re.resolve("strings"),
      l = r.pageTitle.get(),
      c = r.backNavigationAllowed.get(),
      d = r.backNavigationDescription.get(),
      u = r.infoButtons.get();
    function _(e) {
      i.play("mouse-enter", { target: "NavigationButton", original: e });
    }
    function m(e) {
      return function () {
        n.doInfoAction(e);
      };
    }
    const b = U(),
      v = re.resolve("intl"),
      f = (0, Se.useRef)(null),
      [g, h] = (0, Se.useState)(0),
      [y, x] = (0, Se.useState)(!1),
      [N, B] = (0, Se.useState)(!1);
    K(() => {
      (x(!0), h(f.current?.offsetWidth ? f.current?.offsetWidth + 1 : 0));
      const e = p(() => B(!0));
      return () => {
        (x(!1), h(0), B(!1), e());
      };
    }, [b.screenWidthRem, b.breakpoint.name, a, s, c, d, l]);
    const j = $({ value: lt.sizes.small }, { extraLarge: { value: lt.sizes.medium } });
    return (0, Le.jsxs)("div", {
      className: te(ct, y && Nt, N && Bt, t, e.base),
      children: [
        (0, Le.jsxs)(le, {
          className: te(ht, e.divider),
          children: [
            a &&
              (0, Le.jsxs)("div", {
                className: te(dt, gt, e.button, e.button__garageNavigation),
                "data-test-id": "garageButton",
                onClick: function (e) {
                  (i.play("click", { target: "NavigationButton", original: e }),
                    n.navigateTo("garage"));
                },
                onMouseEnter: _,
                children: [
                  (0, Le.jsx)(At, { classNames: e }),
                  (0, Le.jsx)("div", {
                    className: te(_t, e.label),
                    children: v.toUpperCase(o.readOrEmpty("menu.headerButtons.hangar")),
                  }),
                ],
              }),
            c &&
              (0, Le.jsx)(Le.Fragment, {
                children: (0, Le.jsxs)("div", {
                  className: te(dt, ut, e.button, e.button__backNavigation),
                  onClick: function (e) {
                    (i.play("click", { target: "NavigationButton", original: e }),
                      n.navigateTo("back"));
                  },
                  onMouseEnter: _,
                  children: [
                    (0, Le.jsx)(At, { classNames: e }),
                    (0, Le.jsx)("div", {
                      className: te(_t, e.label),
                      children: v.toUpperCase(o.readOrEmpty("menu.headerButtons.navigation.back")),
                    }),
                    d &&
                      (0, Le.jsx)("div", {
                        ref: f,
                        className: te(xt, e.hiddenLabel),
                        style: { "--width": `${g}px` },
                        children: (0, Le.jsx)(ee, { className: jt, text: v.toUpperCase(d) }),
                      }),
                  ],
                }),
              }),
            l &&
              (0, Le.jsx)(Le.Fragment, {
                children: (0, Le.jsx)("div", {
                  className: te(yt, e.title),
                  children: (0, Le.jsx)(ee, { text: v.toUpperCase(l) }),
                }),
              }),
          ],
        }),
        u.length > 0 &&
          k(u, (t, a) =>
            (0, Le.jsx)(
              "div",
              {
                className: te(It, a === u.length - 1 && Et, e?.infoButton),
                children: (0, Le.jsx)(lt, {
                  size: j.value,
                  onClick: m(a),
                  infoType: t.type,
                  label: t.label,
                  tooltipHeader: t.tooltipHeader,
                  tooltipBody: t.tooltipBody,
                }),
              },
              a,
            ),
          ),
      ],
    });
  }),
  kt = (function (e) {
    return (
      (e[(e.UNDEFINED = 0)] = "UNDEFINED"),
      (e[(e.ADD_NEEDED = 1)] = "ADD_NEEDED"),
      (e[(e.ADDED = 2)] = "ADDED"),
      (e[(e.CONFIRMATION_SENT = 3)] = "CONFIRMATION_SENT"),
      (e[(e.CONFIRMED = 4)] = "CONFIRMED"),
      (e[(e.PROCESSING = 5)] = "PROCESSING"),
      e
    );
  })({}),
  Tt = "PlayersProfile_b15b3eb3",
  Pt = "PlayersProfile_playerInfo_89f70778",
  St = "PlayersProfile_playerInfoWrapper_2ed6c121",
  Mt = "PlayersProfile_badgeWrapper_910cac78",
  Ot = "PlayersProfile_suffixBadgeWrapper_a4096e4e",
  Wt = "PlayersProfile_badge_4050c3e9",
  wt = "PlayersProfile_text_99417432",
  Rt = "PlayersProfile_text__name_2ed6c121",
  Dt = "PlayersProfile_text__teamKiller_8bf5e412",
  Ht = "PlayersProfile_base__alertVisible_9b40d452",
  Lt = "PlayersProfile_anonymizerIcon_8632eb46",
  Vt = "PlayersProfile_alertIcon_b8de5d15",
  zt = re.resolve("strings"),
  $t = Z("PlayersProfile", Tt, { variants: { alertVisible: { true: Ht } } }),
  Ft = new Set([kt.ADD_NEEDED, kt.ADDED]),
  Ut = { width: "48rem", height: "48rem", marginLeft: "-35rem" },
  Gt = E(function () {
    const e = ie(),
      a = b({
        header: zt.readOrEmpty("tooltips.header.account.header"),
        body: zt.readOrEmpty("tooltips.header.account.body"),
      }),
      { model: s, controls: r } = me(),
      {
        userName: n,
        badgeID: i,
        isInClan: o,
        clanAbbrev: l,
        suffixBadgeID: c,
        teamKiller: d,
        hasSteamAccount: u,
        steamEmailStatus: _,
        anonymized: m,
        email: p,
      } = s.userInfo.get(),
      v = V(
        "AccountCompletion",
        (0, Se.useMemo)(() => [p], [p]),
      ),
      f = u && Ft.has(_);
    const g = S(q.Badge.sizes.x48x48, q.Badge.sizes.x80x80),
      h = S(q.Stripe.sizes.medium, q.Stripe.sizes.big);
    return (0, Le.jsxs)($t, {
      alertVisible: f,
      children: [
        (0, Le.jsxs)(q, {
          ...a,
          className: Pt,
          onClick: function (t) {
            (e.play("click", { target: "player-info", original: t }),
              a.onClick(),
              r.openAccountDashboard());
          },
          onMouseEnter: function (t) {
            (e.play("mouse-enter", { target: "player-info", original: t }), a.onMouseEnter(t));
          },
          children: [
            i > 0 &&
              (0, Le.jsx)("div", {
                className: Mt,
                children: (0, Le.jsx)(q.Badge, {
                  badgeId: String(i),
                  width: 48,
                  height: 48,
                  size: g,
                  className: Wt,
                }),
              }),
            (0, Le.jsxs)(q.Wrapper, {
              className: St,
              children: [
                (0, Le.jsx)(q.Name, {
                  className: te(wt, Rt, d && Dt),
                  children: (0, Le.jsx)(ee, { text: n }),
                }),
                o &&
                  (0, Le.jsx)(q.ClanTag, {
                    className: wt,
                    children: (0, Le.jsx)(t, {
                      upgradeLegacy: !0,
                      path: "common.clanTag",
                      params: { abbrev: l },
                    }),
                  }),
              ],
            }),
            c > 0 &&
              (0, Le.jsx)("div", {
                className: Ot,
                children: (0, Le.jsx)(q.Stripe, {
                  badgeId: String(c),
                  size: h,
                  stripeIcon: q.Stripe.icons.stripe.medium,
                  stipeBadgeIcon: q.Stripe.icons.badge.medium,
                  style: Ut,
                }),
              }),
            m && (0, Le.jsx)("div", { className: Lt }),
          ],
        }),
        f && (0, Le.jsx)("div", { ...v, className: Vt }),
      ],
    });
  }),
  Qt = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Le.jsx)(_e, { options: e, children: (0, Le.jsx)(Gt, { ...t }) }),
  ),
  qt = "Premiums_e458a55f",
  Yt = "Premiums_subscription_5299180c",
  Jt = "Premiums_subscription__unavailable_86efdd6c",
  Kt = "Premiums_text_82711911",
  Xt = "Premiums_text__premShop_a067f33c",
  Zt = "Premiums_divider_268fb4cd",
  ea = "Premiums_wotPlusImg_195105fb",
  ta = "Premiums_wotPlusImg__disabled_8e8e6ceb",
  aa = "Premiums_wotPlusImg__pro_798bc63",
  sa = "Premiums_alertIcon_da4f2f9b",
  ra = "Premiums_premiumImg_d5d73467",
  na = "Premiums_premiumImg__disabled_12a94c05",
  ia = "Premiums_premiumShopImg_99a91f62",
  oa = Z("PremiumShop", te(qt, "Premiums_base__clickable_dd8e69b8")),
  la = re.resolve("strings");
function ca() {
  const { model: e, controls: t } = ke(),
    a = ie(),
    s = b({
      header: la.readOrEmpty("tooltips.header.premShop.header"),
      body: la.readOrEmpty("tooltips.header.premShop.body"),
    });
  if (e.premiumShopEnabled.get())
    return (0, Le.jsxs)(oa, {
      ...s,
      onClick: function (e) {
        (s.onClick(),
          a.play("click", { target: "premium-shop", original: e }),
          t.openPremiumShop());
      },
      onMouseEnter: function (e) {
        (s.onMouseEnter(e), a.play("mouse-enter", { target: "premium-shop", original: e }));
      },
      children: [
        (0, Le.jsx)("div", { className: ia }),
        (0, Le.jsx)("div", {
          className: te(Kt, Xt),
          children: la.readOrEmpty("menu.headerButtons.btnLabel.premShop"),
        }),
      ],
    });
}
var da = (function (e) {
    return ((e.Inactive = "Inactive"), (e.Active = "Active"), (e.Cancelled = "Cancelled"), e);
  })({}),
  ua = Z("Premiums", qt),
  _a = re.resolve("strings"),
  ma = re.resolve("aliases"),
  ba = re.resolve("views");
var pa = E(function ({ className: e }) {
    const s = ie(),
      r = a({
        resId: ma.read((e) => e.lobby_header.default.UserAccount("resId")),
        contentId: ma.read((e) => e.common.tooltip.Backport("resId")),
        decoratorId: R.invalid("resId"),
        args: { tooltipId: "ammunitionEmptySlot", tooltipArgs: '["#tooltips:header/premium_buy"]' },
      }),
      { model: i, controls: o } = me(),
      l = i.wotPlus.get(),
      c = i.benefits.get(),
      d = i.proBenefits.get(),
      u = i.subscriptionPrimitives.isCnRealm.get(),
      _ = i.getTooltipVariant(),
      m = (function (e) {
        if (void 0 === e) return null;
        const { unit: t, value: a } = e;
        return "days" === t
          ? { unit: "day", value: a }
          : "hours" === t
            ? { unit: "hour", value: a }
            : { unit: "hour", value: 1 };
      })(i.premiums.basic.get()),
      { type: p, state: v, isWotPlusEnabled: f } = l,
      { state: g } = i.premiumAccount.get(),
      h = (0, Se.useRef)(!1),
      y = n(
        "wot_plus_header_widget",
        (0, Se.useMemo)(
          () => ({
            ...l,
            bonuses: c,
            proBonuses: d,
            isCnRegion: u,
            tooltipVariant: _,
            resId: ba.read((e) => e.mono.hangar.tooltips("resId")),
          }),
          [l, c, d, u, _],
        ),
        { showDelay: 50 },
      ),
      x = b({ body: _a.readOrEmpty("subscription.headerButton.tooltip.unavailable") });
    const N = v && v === ue.Active;
    return (0, Le.jsxs)(ua, {
      className: e,
      children: [
        (0, Le.jsxs)("div", {
          ...(f ? y : x),
          className: te(Yt, !f && Jt),
          "data-test-id": "wotPlus",
          onClick: f
            ? function (e) {
                ((h.current = !0),
                  y.onClick(),
                  s.play("click", { target: "premiums:wot-plus", original: e }),
                  requestAnimationFrame(() => {
                    o.openWotPlusSubscriptionPage();
                  }));
              }
            : void 0,
          onMouseEnter: function (e) {
            h.current ||
              (f ? y?.onMouseEnter(e) : x?.onMouseEnter(e),
              s.play("mouse-enter", { target: "premiums:wot-plus", original: e }));
          },
          children: [
            (0, Le.jsx)("div", { className: te(ea, !N && ta, p === de.Pro && N && aa) }),
            (0, Le.jsx)("div", {
              className: Kt,
              children: _a.readOrEmpty(
                v === ue.Active || v === ue.Cancelled
                  ? "subscription.headerButton.state.active"
                  : "subscription.headerButton.state.available",
              ),
            }),
            v === ue.Cancelled &&
              (0, Le.jsx)(j, { path: "subscription.alert_icon", className: sa }),
          ],
        }),
        (0, Le.jsx)(ce, { className: Zt }),
        (0, Le.jsxs)("div", {
          ...r,
          className: Yt,
          "data-test-id": "premium",
          onClick: function (e) {
            (r.onClick(),
              s.play("click", { target: "premiums:premium", original: e }),
              o.openPremiumSubscriptionPage());
          },
          onMouseEnter: function (e) {
            (r.onMouseEnter(e), s.play("mouse-enter", { target: "premiums:premium", original: e }));
          },
          children: [
            (0, Le.jsx)("div", { className: te(ra, g === da.Inactive && na) }),
            (0, Le.jsx)("div", {
              className: Kt,
              children:
                g === da.Active && m
                  ? (0, Le.jsx)("span", {
                      children: (0, Le.jsx)(t, {
                        path: `menu.timeLeft.short.${m.unit}`,
                        params: { [m.unit]: Math.ceil(m.value) },
                        upgradeLegacy: !0,
                      }),
                    })
                  : (0, Le.jsx)("span", { children: _a.readOrEmpty("menu.common.premiumBuy") }),
            }),
          ],
        }),
      ],
    });
  }),
  va = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Le.jsx)(_e, { options: e, children: (0, Le.jsx)(pa, { ...t }) }),
  ),
  fa = "UserProfile_2146e52",
  ga = "UserProfile_divider_4a395a41",
  ha = re.resolve("aliases"),
  ya = ha.read((e) => e.lobby_header.default.UserAccount("resId")),
  xa = ha.read((e) => e.lobby_header.default.PremShop("resId"));
function Na({ className: e }) {
  const t = i(ya);
  return (0, Le.jsx)("div", {
    className: te(fa, e),
    children: (0, Le.jsxs)(le, {
      className: ga,
      children: [
        t && (0, Le.jsx)(Qt, { options: { rootId: ya } }),
        t && (0, Le.jsx)(va, { options: { rootId: ya } }),
        xa && (0, Le.jsx)(ca, {}),
      ],
    }),
  });
}
var Ba = E(function ({ garageNavigationAllowed: e, battleButtonVisible: t, classNames: a }) {
    return rt() === be.Hangar
      ? (0, Le.jsx)(Na, { className: a?.userProfile })
      : (0, Le.jsx)(Ct, {
          classNames: a?.navigationBar,
          garageNavigationAllowed: e,
          battleButtonVisible: t,
        });
  }),
  ja = (function (e) {
    return ((e.Personal = "personal"), (e.Clan = "clan"), (e.Event = "event"), e);
  })({}),
  Ia = (function (e) {
    return (
      (e[(e.Inactive = 0)] = "Inactive"),
      (e[(e.Active = 1)] = "Active"),
      (e[(e.Used = 2)] = "Used"),
      e
    );
  })({}),
  Ea = "alert",
  Aa = "x24x24",
  Ca = "x32x32",
  ka = "x96x96",
  Ta = { [ja.Personal]: 0, [ja.Clan]: 1, [ja.Event]: 2 };
function Pa(e) {
  return Ta[e] ?? 0;
}
function Sa(e) {
  return Math.max(0, Math.floor(e - Date.now() / u));
}
var [Ma, Oa] = D()(
    ({ observableModel: e }) => {
      const t = {
          reserves: e.arrayClone("reserves"),
          disabledCategories: e.arrayClone("disabledCategories"),
          ...e.primitives({
            totalReserves: "allReserves",
            totalLimitedReserves: "limitedReserves",
            expiringReserveWillExpireSoon: "reserveExpire",
          }),
        },
        a = J.primitive(() => y(t.reserves.get(), (e) => e.inactivationTime > 0)),
        s = J.shallow(() => {
          const e = t.reserves.get();
          return Q(e, (e, t) => Pa(e.reserveType) - Pa(t.reserveType));
        }),
        r = J.shallow(() => t.disabledCategories.get().every((e) => e.isDisabled));
      return { ...t, computes: { visible: a, sortedBoosters: s, disabled: r } };
    },
    ({ externalModel: e }) => ({ openBooster: e.createCallbackNoArgs("openBoosterNavigation") }),
  ),
  Wa = "Activate_d05a6105",
  wa = "Activate_base__disabled_77f76d6c",
  Ra = "Activate_wrapper_ea72f87a",
  Da = "Activate_iconWrapper_b884eeb8",
  Ha = "Activate_icon_bfced9a9",
  La = "Activate_icon__glow_6978c825",
  Va = "Activate_amount_262c55ed",
  za = "Activate_text_6ca62bb4",
  $a = "Activate_text__limited_cd94941e",
  Fa = "Activate_textOverlay_a5c8a675",
  Ua = "Activate_textOverlay__limited_6c5cb381",
  Ga = "Activate_hint_68b56ff6",
  Qa = "Activate_hint__glow_24eef452",
  qa = "Activate_glow_d01917a6",
  Ya = "Activate_glow__limited_5e88d41",
  Ja = "Activate_glow__alert_8001ed30",
  Ka = "Activate_sparks_718002e7",
  Xa = "Activate_sparks__visible_842edf80",
  Za = E(function () {
    const { model: e } = Oa(),
      t = re.resolve("strings"),
      a = re.resolve("intl"),
      s = e.computes.visible(),
      r = e.allReserves.get(),
      n = e.limitedReserves.get(),
      i = e.reserveExpire.get(),
      o = e.computes.disabled();
    return s
      ? null
      : (0, Le.jsxs)("div", {
          className: te(Wa, o && wa),
          children: [
            (0, Le.jsxs)("div", {
              className: Ra,
              children: [
                (0, Le.jsx)("div", { className: te(Ka, i && Xa) }),
                (0, Le.jsx)("div", { className: te(qa, n && Ya, i && Ja) }),
                (0, Le.jsx)("div", {
                  className: Da,
                  children: (0, Le.jsx)("div", { className: te(Ha, n && La) }),
                }),
                (0, Le.jsx)(A, {
                  classNames: { base: Va, text: te(za, n && $a), textOverlay: te(Fa, n && Ua) },
                  children: a.formatNumber("integral", r),
                }),
              ],
            }),
            !o &&
              (0, Le.jsx)("div", {
                className: te(Ga, n && Qa),
                children: a.toUpperCase(
                  t.readOrEmpty("menu.boostersWindow.boostersTableRenderer.activateBtnLabel"),
                ),
              }),
          ],
        });
  }),
  es = {
    background: "Card_background_d014d7d",
    fill: "Card_fill_68e6b048",
    fillPattern: "Card_fillPattern_496f8980",
    base: "Card_71731d1d",
    base__disabled: "Card_base__disabled_530f6e06",
    background__personal: "Card_background__personal_57d23cf4",
    background__clan: "Card_background__clan_46c6fc44",
    background__alert: "Card_background__alert_9b1dc5e1",
    alert: "Card_alert_402bb5af",
    alert__visible: "Card_alert__visible_bf4a84a5",
    icon: "Card_icon_1eb606a6",
    premium: "Card_premium_44855832",
    premium__visible: "Card_premium__visible_bd677cbc",
    timer: "Card_timer_27a2857b",
    timer__visible: "Card_timer__visible_bd677cbc",
    timerGlow: "Card_timerGlow_e2954b70",
    fillPattern__personal: "Card_fillPattern__personal_487b5eeb",
    fillPattern__clan: "Card_fillPattern__clan_d7903601",
    fillPattern__alert: "Card_fillPattern__alert_fba99a76",
    fillBorderTop: "Card_fillBorderTop_4308f9d9",
    fillBorderTop__alert: "Card_fillBorderTop__alert_b2944931",
    fillBorderBottom: "Card_fillBorderBottom_96ba37d9",
    fillBorderBottom__visible: "Card_fillBorderBottom__visible_594e8c6a",
  },
  ts = E(function ({ type: e, timeLeft: a, timeTotal: s, icon: r, className: n }) {
    const { model: i } = Oa(),
      { minutesLeft: o, percentLeft: l } = (function (e, t) {
        const [a, s] = (0, Se.useState)(Sa(e));
        ((0, Se.useEffect)(() => {
          s(Sa(e));
        }, [e]),
          (0, Se.useEffect)(() => {
            if (0 === a) return;
            const t = setTimeout(() => {
              s(Sa(e));
            }, u);
            return () => clearTimeout(t);
          }, [a, e]));
        const r = m(a),
          n = Math.ceil(v(r));
        return { minutesLeft: n, percentLeft: Math.max(0, Math.min(100, (n / (t / 60)) * 100)) };
      })(a, s),
      c = i.computes.disabled(),
      d = o <= 9,
      _ = o <= 2,
      b = $({ size: Aa }, { large: { size: Ca } }),
      p = S(b.size, ka),
      f = r.includes("premium");
    return a <= 0
      ? null
      : (0, Le.jsxs)("div", {
          className: te(es.base, c && es.base__disabled, n),
          style: { "--fill_percentage": `${l}%` },
          children: [
            (0, Le.jsx)("div", { className: te(es.background, es[`background__${d ? Ea : e}`]) }),
            (0, Le.jsx)(j, {
              className: es.icon,
              path: `personal_reserves.common.cards.${p}.${r}`,
            }),
            (0, Le.jsx)(j, {
              className: te(es.premium, f && es.premium__visible),
              path: `personal_reserves.common.cards.${b.size}.premium_booster_glow`,
            }),
            (0, Le.jsxs)("div", {
              className: te(es.timer, d && es.timer__visible),
              children: [
                (0, Le.jsx)("div", { className: es.timerGlow }),
                (0, Le.jsx)(t, {
                  upgradeLegacy: !0,
                  path: "personal_reserves.hangarEntry.minute",
                  params: { minutesLeft: o },
                }),
              ],
            }),
            (0, Le.jsx)("div", { className: te(es.alert, _ && es.alert__visible) }),
            (0, Le.jsxs)("div", {
              className: es.fill,
              children: [
                (0, Le.jsx)("div", {
                  className: te(es.fillPattern, es[`fillPattern__${d ? Ea : e}`]),
                }),
                (0, Le.jsx)("div", {
                  className: te(es.fillBorderTop, _ && es.fillBorderTop__alert),
                }),
                (0, Le.jsx)("div", {
                  className: te(es.fillBorderBottom, d && es.fillBorderBottom__visible),
                }),
              ],
            }),
          ],
        });
  }),
  as = "List_background_dc475fe4",
  ss = "List_border_59b5e8fe",
  rs = "List_borderShadow_776a55b9",
  ns = "List_e706f6ab",
  is = "List_base__disabled_8303c2c1",
  os = "List_cards_efba95c2",
  ls = "List_card_d0063856",
  cs = E(function () {
    const { model: e } = Oa(),
      t = e.computes.sortedBoosters(),
      a = e.computes.visible(),
      s = e.computes.disabled();
    return a
      ? (0, Le.jsxs)("div", {
          className: te(ns, s && is),
          children: [
            (0, Le.jsx)("div", { className: as }),
            (0, Le.jsx)("div", { className: ss }),
            (0, Le.jsx)("div", { className: rs }),
            (0, Le.jsx)("div", {
              className: os,
              children: l(
                t,
                (e) => e.state === Ia.Active,
                (e) =>
                  (0, Le.jsx)(
                    ts,
                    {
                      type: e.reserveType,
                      timeLeft: e.inactivationTime,
                      timeTotal: e.totalDuration,
                      icon: e.iconId,
                      className: ls,
                    },
                    e.boosterID,
                  ),
              ),
            }),
          ],
        })
      : null;
  }),
  ds = "Reserves_43f2a7a7",
  us = "Reserves_base__disabled_58e2c36d",
  _s = E(function () {
    const { model: e, controls: t } = Oa(),
      s = (function () {
        const e = re.resolve("views");
        return a({
          resId: re
            .resolve("aliases")
            .read((e) => e.lobby_header.default.ReservesEntryPoint("resId")),
          contentId: e.read((e) => e.lobby.personal_reserves.PersonalReservesTooltip("resId")),
        });
      })(),
      r = ie(),
      n = e.computes.disabled();
    return (0, Le.jsxs)("div", {
      ...s,
      className: te(ds, n && us),
      onClick: function (e) {
        (s.onClick(), n || (r.play("click", { target: "reserves", original: e }), t.openBooster()));
      },
      onMouseEnter: function (e) {
        (s.onMouseEnter(e), n || r.play("mouse-enter", { target: "reserves", original: e }));
      },
      "data-test-id": "reservesButton",
      children: [(0, Le.jsx)(cs, {}), (0, Le.jsx)(Za, {})],
    });
  }),
  ms = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Le.jsx)(Ma, { options: e, children: (0, Le.jsx)(_s, { ...t }) }),
  ),
  [bs, ps] = D("WalletModel")(
    ({ observableModel: e }) => {
      const t = { currencies: e.dict("currencies") };
      return {
        ...t,
        list: J.shallow((e) =>
          Array.from(t.currencies.keys.values()).sort((t, a) => {
            const s = e.indexOf(t),
              r = e.indexOf(a),
              n = e.length;
            return (-1 === s ? n : s) - (-1 === r ? n : r);
          }),
        ),
      };
    },
    ({ externalModel: e }) => ({
      currencyAction: e.createCallback((e) => ({ type: e }), "onCurrencyAction"),
    }),
  ),
  vs = "Hint_e53dd99e",
  fs = "Hint_discountBackground_d56ce0a3",
  gs = "Hint_discount_94b7b9ff",
  hs = "Hint_onlyDiscount_8b648a0a",
  ys = "Hint_discountWithHintText_381cf018",
  xs = "Hint_onlyHintText_751386e1",
  Ns = "Hint_discountValue_b1f389fc",
  Bs = "Hint_discountHintTitle_9db2d839",
  js = "Hint_hintText_6f3fa83f",
  Is = "Hint_hintTitle_135a3ed",
  Es = "Hint_discountValue__withHint_e7bbe38f";
function As({ classNames: e }) {
  const t = re.resolve("strings");
  return (0, Le.jsxs)("div", {
    className: te(hs, e?.onlyDiscount),
    children: [
      (0, Le.jsx)("div", { className: te(fs, e?.discountBackground) }),
      (0, Le.jsx)(f.Root, {
        children: (0, Le.jsx)(f.Value, {
          value: t.readOrEmpty("common.common.percent"),
          classNames: { valueContainer: te(gs, e?.discount), value: te(Ns, e?.discountValue) },
        }),
      }),
    ],
  });
}
function Cs({ type: e, classNames: t }) {
  const a = re.resolve("intl"),
    s = re.resolve("strings");
  return (0, Le.jsx)("div", {
    className: te(js, xs, t?.hintText, t?.onlyHintText),
    children: (0, Le.jsx)(A, {
      classNames: t?.textGradient,
      children: (0, Le.jsx)("div", {
        className: te(Is, t?.hintTitle),
        children: a.toUpperCase(s.readOrEmpty(`menu.headerButtons.btnLabel.${e}`)),
      }),
    }),
  });
}
function ks({ classNames: e, type: t }) {
  const a = re.resolve("intl"),
    s = re.resolve("strings");
  return (0, Le.jsxs)("div", {
    className: te(ys, e?.discountWithHintText),
    children: [
      (0, Le.jsx)("div", { className: te(fs, e?.discountBackground) }),
      (0, Le.jsx)("div", {
        className: te(Bs, e?.discountHintTitle),
        children: a.toUpperCase(s.readOrEmpty(`menu.headerButtons.btnLabel.${t}`)),
      }),
      (0, Le.jsx)(f.Root, {
        children: (0, Le.jsx)(f.Value, {
          value: s.readOrEmpty("common.common.percent"),
          classNames: { valueContainer: te(gs, e?.discount), value: te(Ns, Es, e?.discountValue) },
        }),
      }),
    ],
  });
}
function Ts({ classNames: e, type: t }) {
  return (0, Le.jsxs)("div", {
    className: te(vs, e?.base),
    children: [
      (0, Le.jsx)(As, {
        classNames: {
          onlyDiscount: e?.onlyDiscount,
          discountBackground: e?.discountBackground,
          discount: e?.discount,
          discountValue: e?.discountValue,
        },
      }),
      (0, Le.jsx)(Cs, {
        type: t,
        classNames: {
          hintText: e?.hintText,
          textGradient: e?.textGradient,
          onlyHintText: e?.onlyHintText,
        },
      }),
      (0, Le.jsx)(ks, { classNames: e, type: t }),
    ],
  });
}
var Ps = {
    base: "Currency_92022680",
    hintWrapper: "Currency_hintWrapper_530465b9",
    base__interactive: "Currency_base__interactive_52396ddd",
    currencyWrapper: "Currency_currencyWrapper_b13579ba",
    currencyIcon: "Currency_currencyIcon_346f8c78",
    value: "Currency_value_b1cf6531",
    value__unavailable: "Currency_value__unavailable_3a328d4",
    dash: "Currency_dash_2806b61e",
    formattedValue: "Currency_formattedValue_b7cad7e0",
    hint: "Currency_hint_f9d16bb2",
    base__hidden: "Currency_base__hidden_271064ec",
    text: "Currency_text_f4484816",
    text__overlay: "Currency_text__overlay_64b93131",
    discountWithHintText: "Currency_discountWithHintText_95e3324b",
    base__discount: "Currency_base__discount_271064ec",
    onlyHintText: "Currency_onlyHintText_61ecd7b0",
    onlyDiscount: "Currency_onlyDiscount_61ecd7b0",
  },
  Ss = 1e6,
  Ms = 1e5;
function Os({ wgMoneyAvailable: e, value: a, type: s, classNames: r }) {
  const n = (0, Se.useRef)(null),
    i = re.resolve("intl"),
    o = re.resolve("strings"),
    l = $(
      {
        displayValue: () =>
          a >= Ss
            ? { abbreviated: !0, value: g(a, Ms, "floor") / Ss }
            : { abbreviated: !1, value: a },
      },
      {
        medium: {
          displayValue: () =>
            a >= 1e7
              ? { abbreviated: !0, value: g(a, Ms, "floor") / Ss }
              : { abbreviated: !1, value: a },
        },
        large: {
          displayValue: () =>
            a >= 1e8
              ? { abbreviated: !0, value: g(a, Ms, "floor") / Ss }
              : { value: a, abbreviated: !1 },
        },
      },
    );
  if (!1 === e)
    return (0, Le.jsxs)("div", {
      className: te(Ps.value, Ps.value__unavailable, r?.value),
      children: [
        (0, Le.jsx)("div", {
          className: Ps.dash,
          children: o.readOrEmpty("common.common.semi_dash"),
        }),
        (0, Le.jsx)("div", {
          className: Ps.dash,
          children: o.readOrEmpty("common.common.semi_dash"),
        }),
      ],
    });
  const c = l.displayValue();
  return (0, Le.jsx)("div", {
    ref: n,
    className: te(Ps.value, r?.base),
    children: c.abbreviated
      ? (0, Le.jsx)(t, {
          path: "menu.hangar_header.million",
          params: { value: c.value },
          brackets: { start: "%(", end: ")s" },
          className: te(Ps.formattedValue, r?.formattedValue),
        })
      : i.formatNumber(s === N.gold ? "gold" : "integral", c.value),
  });
}
var Ws = E(function ({ currency: e, type: t, className: a, classNames: s }) {
    const { controls: r } = ps(),
      n = ie(),
      i = "AVAILABLE" === e.status,
      o = (function (e, t, a, s) {
        const r = re.resolve("strings"),
          n = b({
            header: r.readOrEmpty(`tooltips.header.buttons.${e}.header`),
            body: r.readOrEmpty(`tooltips.header.buttons.${e}.body`),
          }),
          i = (0, Se.useMemo)(() => ({ disabled: "string" != typeof a || "" === a }), [a]),
          o = z(
            a,
            (0, Se.useMemo)(() => [s], [s]),
            i,
          );
        return !1 === t ? n : o;
      })(t, i, e.tooltipType, e.value),
      l = S(
        $({ size: H.extraSmall }, { large: { size: H.small }, extraLarge: { size: H.medium } })
          .size,
        H.small,
      );
    return (0, Le.jsxs)("div", {
      ...o,
      className: te(
        Ps.base,
        i ? Ps.base__interactive : Ps.base__nonInteractive,
        e.discount > 0 && Ps.base__discount,
        a,
      ),
      onMouseEnter: function (e) {
        (n.play("mouse-enter", { target: "WalletCurrency", original: e }), o.onMouseEnter(e));
      },
      onClick: function (e) {
        (o?.onClick(),
          i && (n.play("click", { target: "WalletCurrency", original: e }), r.currencyAction(t)));
      },
      children: [
        (0, Le.jsx)("div", {
          className: te(Ps.currencyWrapper, s?.currencyWrapper),
          children: (0, Le.jsx)(T, {
            reverse: !0,
            classNames: { ...s?.currency, icon: te(Ps.currencyIcon, s?.currency?.icon) },
            type: t,
            size: l,
            "data-test-id": t,
            children: (0, Le.jsx)(Os, {
              wgMoneyAvailable: i,
              value: e.value,
              type: t,
              classNames: s?.currencyValue,
            }),
          }),
        }),
        i &&
          (0, Le.jsx)("div", {
            className: te(Ps.hintWrapper, s?.hintWrapper),
            children: (0, Le.jsx)(Ts, {
              type: t,
              classNames: {
                ...s?.hint,
                discountWithHintText: te(Ps.discountWithHintText, s?.hint?.discountWithHintText),
                onlyDiscount: te(Ps.onlyDiscount, s?.hint?.onlyDiscount),
                onlyHintText: te(Ps.onlyHintText, s?.hint?.onlyHintText),
                base: te(Ps.hint, s?.hint?.base),
                textGradient: { text: Ps.text, textOverlay: te(Ps.text, Ps.text__overlay) },
              },
            }),
          }),
      ],
    });
  }),
  ws = E(function (e) {
    const t = ps().model.currencies.get(e.type);
    return t
      ? (0, Le.jsx)(Ws, { ...e, currency: t })
      : (console.error(`Currency with type ${e.type} is not defined`), null);
  }),
  Rs = "Wallet_fc600169",
  Ds = [N.crystal, N.gold, N.credits],
  Hs = E(function ({ className: e, classNames: t, currenciesOrder: a = Ds }) {
    const { model: s } = ps(),
      r = s.list(a);
    return (0, Le.jsx)("div", {
      "data-name": "Wallet",
      className: te(Rs, e),
      children: r.map((e) => (0, Le.jsx)(ws, { type: e, classNames: t }, e)),
    });
  }),
  Ls = (0, Se.memo)(({ className: e, classNames: t, currenciesOrder: a, ...s }) =>
    (0, Le.jsx)(bs, {
      ...s,
      children: (0, Le.jsx)(Hs, { className: e, classNames: t, currenciesOrder: a }),
    }),
  ),
  Vs = "RightSide_7ef6e2a9",
  zs = "RightSide_separator_fea82003",
  $s = re.resolve("aliases"),
  Fs = $s.read((e) => e.lobby_header.default.ReservesEntryPoint("resId")),
  Us = $s.read((e) => e.lobby_header.default.Wallet("resId")),
  Gs = function () {
    const e = i(Fs),
      t = i(Us);
    return (0, Le.jsx)("div", {
      className: Vs,
      children: (0, Le.jsxs)(le, {
        className: zs,
        children: [
          e && (0, Le.jsx)(ms, { options: { rootId: Fs } }),
          t && (0, Le.jsx)(Ls, { options: { rootId: Us } }),
        ],
      }),
    });
  },
  Qs = "battleRoyaleQueue",
  qs = new Set([
    "random",
    "trainingsList",
    "tournament",
    "epicQueue",
    "comp7",
    "comp7Light",
    "winback",
    "strongholdsBattlesList",
    "specBattlesList",
    Qs,
  ]);
function Ys(e) {
  return e !== Qs;
}
var Js = {
    base: "VehicleInfo_4b77df3f",
    base__battleRoyaleQueue: "VehicleInfo_base__battleRoyaleQueue_b5a06cbf",
    details: "VehicleInfo_details_3cde71e7",
    vehicleType: "VehicleInfo_vehicleType_5f8aaab4",
  },
  Ks = E(function ({ className: e }) {
    const a = Ae(),
      s = a.model.currentMode.get(),
      r = ye(),
      n = a.model.currentModeId.get(),
      i = ((o = n), "BATTLE_ROYALE_TOURNAMENT" !== a.model.queueType.get() && qs.has(o));
    var o;
    const l = r.model.vehicle();
    if (void 0 !== l)
      return i
        ? (0, Le.jsx)(t, {
            className: te(Js.base, Js[`base__${n}`], e),
            path: "menu.headerButtons.battle.vehicleInfo",
            params: {
              mode: s,
              level: Ys(n) ? (0, Le.jsx)(L, { value: l.level, className: Js.details }) : "",
              type: (0, Le.jsx)(w, {
                className: Js.vehicleType,
                type: l.type,
                size: w.sizes.x24x24,
              }),
              name: (0, Le.jsx)("div", { className: Js.details, children: l.shortName }),
            },
          })
        : (0, Le.jsx)(t, {
            className: te(Js.base, e),
            path: "menu.headerButtons.battle.modeInfo",
            params: { mode: s },
          });
  }),
  Xs = {
    base: "App_fe4b7101",
    base__oldStyle: "App_base__oldStyle_ed955e9f",
    leftSide: "App_leftSide_3f8cd87c",
    userProfile: "App_userProfile_7aef8044",
    navigationBar: "App_navigationBar_a5705175",
    navigationBar_button: "App_navigationBar_button_0",
    navigationBar_title: "App_navigationBar_title_e132fcfa",
    navigationBar_infoButton: "App_navigationBar_infoButton_760d7047",
    navigationBar_button__garageNavigation: "App_navigationBar_button__garageNavigation_e132fcfa",
    navigationBar_button__backNavigation: "App_navigationBar_button__backNavigation_0",
    rightSide: "App_rightSide_4ff92e61",
    base__battleButtonVisible: "App_base__battleButtonVisible_0",
    battleButton: "App_battleButton_415d9053",
    battleButton__fadein: "App_battleButton__fadein_18e051ce",
    fadeIn: "App_fadeIn_0",
    battleButton__withoutFadein: "App_battleButton__withoutFadein_4337493d",
    battleButtonEffects: "App_battleButtonEffects_1da8cd9d",
    vehicleInfoWrapper: "App_vehicleInfoWrapper_9f2ec684",
  },
  Zs = Z("Header", Xs.base, {
    variants: {
      oldStyle: { true: Xs.base__oldStyle },
      battleButtonVisible: { true: Xs.base__battleButtonVisible },
    },
  }),
  er = re.resolve("aliases").read((e) => e.lobby_header.default.FightStart("resId")),
  tr = new Set([je, Ie]),
  ar = new Set(["mapsTraining"]);
var sr = E(function () {
    const e = x(0, 250),
      t = G(),
      a = Ne(),
      s = Ae(),
      [r, n] = (0, Se.useState)(!1),
      o = s.model.battleStatus.get(),
      l = s.model.battleButtonAlwaysOn.get(),
      c = !s.model.computes.isSearchingBattle() && !s.model.computes.isBattleReady(),
      d = rt(),
      u = Boolean(
        se(t.location, { paths: ["/:hangar/allVehicles", "/:eventName/:hangar/allVehicles"] }),
      ),
      _ = t.location.includes("/postBattleResults"),
      m = i(er),
      b = s.model.currentModeId.get();
    return (
      (0, Se.useEffect)(() => {
        m
          ? _ && ar.has(b)
            ? n(!1)
            : l
              ? n(!0)
              : tr.has(o)
                ? n(!1)
                : n(d === be.Hangar || u || _)
          : n(!1);
      }, [l, o, d, u, _, m, b]),
      (0, Le.jsxs)(Zs, {
        ref: e,
        oldStyle: a.model.oldStyle.get(),
        battleButtonVisible: r,
        children: [
          (0, Le.jsx)("div", {
            className: Xs.leftSide,
            children: (0, Le.jsx)(Ba, {
              garageNavigationAllowed: c,
              battleButtonVisible: r,
              classNames: {
                userProfile: Xs.userProfile,
                navigationBar: {
                  base: Xs.navigationBar,
                  button: Xs.navigationBar_button,
                  button__garageNavigation: Xs.navigationBar_button__garageNavigation,
                  title: Xs.navigationBar_title,
                  infoButton: Xs.navigationBar_infoButton,
                  button__backNavigation: Xs.navigationBar_button__backNavigation,
                },
              },
            }),
          }),
          r &&
            (0, Le.jsxs)(Le.Fragment, {
              children: [
                (0, Le.jsx)(st, {
                  options: { rootId: er },
                  classNames: {
                    base: te(
                      Xs.battleButton,
                      d === be.Hangar || u
                        ? Xs.battleButton__withoutFadein
                        : Xs.battleButton__fadein,
                    ),
                    effect: Xs.battleButtonEffects,
                  },
                }),
                _ &&
                  (0, Le.jsx)("div", {
                    className: Xs.vehicleInfoWrapper,
                    children: (0, Le.jsx)(Ks, {}),
                  }),
              ],
            }),
          (0, Le.jsx)("div", {
            className: te(Xs.rightSide, r && Xs.rightSide__battleButtonVisible),
            children:
              !s.model.computes.isSearchingBattle() &&
              !s.model.computes.isBattleReady() &&
              (0, Le.jsx)(Gs, {}),
          }),
        ],
      })
    );
  }),
  rr = re.resolve("aliases"),
  nr = h({ click: { battleButton: "gui_battle" } });
ne(
  new C()
    .addWithProps(F, { soundsOverrides: nr })
    .add(xe)
    .addWithProps(Y, {
      context: "model.router",
      rootId: rr.read((e) => e.lobby_header.default.HeaderState("resId")),
    })
    .addWithProps(Te, { options: { context: "tutorialModel" } })
    .addWithProps(Ce, {
      options: { rootId: rr.read((e) => e.lobby_header.default.PremShop("resId")) },
    })
    .addWithProps(Ee, {
      options: { rootId: rr.read((e) => e.lobby_header.default.Prebattle("resId")) },
    })
    .addWithProps(he, {
      options: { rootId: rr.read((e) => e.lobby_header.default.CurrentVehicle("resId")) },
    })
    .addWithProps(pe, {
      options: { rootId: rr.read((e) => e.lobby_header.default.HeaderState("resId")) },
    })
    .addWithProps(fe, {
      options: { rootId: rr.read((e) => e.lobby_header.default.NavigationBar("resId")) },
    })
    .render((0, Le.jsx)(sr, {})),
);
