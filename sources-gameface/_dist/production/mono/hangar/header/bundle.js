import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $n as t,
  Ar as a,
  Dn as s,
  Dr as r,
  Fn as n,
  Ft as i,
  Gi as o,
  Ia as l,
  In as c,
  It as d,
  Ja as u,
  Kt as _,
  Mt as m,
  Or as b,
  Pi as p,
  Pr as v,
  Qa as f,
  Qn as g,
  R as h,
  St as x,
  Ti as y,
  Tr as N,
  Vr as B,
  Wr as j,
  _t as I,
  aa as E,
  ai as A,
  ao as C,
  ar as k,
  ci as T,
  cr as P,
  d as S,
  dr as M,
  ea as O,
  eo as W,
  f as w,
  fi as D,
  ga as H,
  hi as V,
  hn as L,
  hr as z,
  jn as $,
  jr as F,
  kr as U,
  li as G,
  lr as Q,
  mi as q,
  oa as Y,
  pr as J,
  qr as K,
  ro as X,
  rr as Z,
  to as ee,
  ui as te,
  uo as ae,
  ur as se,
  xr as re,
  xt as ne,
  zi as ie,
  zr as oe,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { n as le, t as ce } from "../chunks/divider.js";
import { a as de, i as ue, n as _e, r as me } from "../chunks/user_account_model.js";
var be = (function (e) {
    return ((e.Hangar = "hangar"), (e.Default = "default"), e);
  })({}),
  [pe, ve] = z("HeaderStateModel")((e) => ({ features: e.observableModel.dict("features") })),
  [fe, ge] = z()(
    ({ observableModel: e }) => ({
      ...e.primitives(["pageTitle", "backNavigationDescription", "backNavigationAllowed"]),
      infoButtons: e.arrayClone("infoButtons"),
    }),
    ({ externalModel: e }) => ({
      navigateTo: e.createCallback((e) => ({ name: e }), "onNavigate"),
      doInfoAction: e.createCallback((e) => ({ index: e }), "onInfoAction"),
    }),
  ),
  [he, xe] = z("CurrentVehicleInfoProvider")(({ observableModel: e }) => {
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
  }, H),
  [ye, Ne] = z("HeaderProvider")(({ observableModel: e }) => e.primitives(["oldStyle"]), H),
  Be = "playerReady",
  je = "searchingBattle",
  Ie = "battleReady",
  [Ee, Ae] = z("PrebattleProvider")(
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
            if (s(e.type)) return { ...e, type: e.type };
          }, "battleVehicle"),
        },
        a = J.primitive(() => t.battleStatus.get() === je),
        r = J.primitive(() => t.battleStatus.get() === Ie);
      return { ...t, computes: { isSearchingBattle: a, isBattleReady: r } };
    },
    ({ externalModel: e }) => ({
      actionPrebattle: e.createCallback((e) => ({ action: e }), "onAction"),
    }),
  ),
  [Ce, ke] = z("PremiumShopProvider")(
    ({ observableModel: e }) => ({ ...e.primitives({ isPremiumShop: "premiumShopEnabled" }) }),
    ({ externalModel: e }) => ({
      openPremiumShop: e.createCallbackNoArgs("onOpenExternalPremiumShop"),
    }),
  ),
  [Te, Pe] = z("TutorialProvider")(
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
  [Me, Oe] = z("BattleStartProvider")(
    ({ observableModel: e }) => ({ ...e.primitives(["tooltip"]) }),
    H,
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
  Ve = e(V(), 1),
  Le = "rays";
var ze = (0, Se.memo)(function ({ buttonState: e, className: t }) {
    const a = e === We ? [Le] : [];
    const s = ae.resolve("videos"),
      r = j(a, {
        from: { opacity: 0 },
        enter: { opacity: 1 },
        leave: { opacity: 0 },
        config: { duration: 100 },
        trail: 500,
      });
    return (0, Ve.jsx)("div", {
      className: ee(He.base, t),
      children: r((e, t) =>
        (0, Ve.jsx)(oe.div, {
          style: e,
          children: (0, Ve.jsx)(
            h,
            {
              loop: !0,
              autoplay: !0,
              src: s.readOrEmpty(`header_footer.battle_button.${t}`),
              className: ee(He.backgroundEffect, He[`backgroundEffect__${t}`]),
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
    const a = ae.resolve("videos"),
      s = G({ value: "small" }, { large: { value: "large" } });
    return (0, Ve.jsx)("div", {
      className: ee(Fe, e),
      children: (0, Ve.jsx)(
        h,
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
function Qe({ buttonState: e, buttonText: t, animationActive: a, onAnimationEnded: s }) {
  const r = B({
    opacity: a ? 0.9 : 0,
    config: { duration: a ? 3600 : 1e3, easing: a ? W.easeInCirc : W.easeOutCirc },
    onRest: () => {
      a && s();
    },
  });
  return e === We
    ? (0, Ve.jsx)(oe.div, { className: Ge.textGlow, style: r, children: t })
    : e === we
      ? (0, Ve.jsx)("div", { className: Ge.textGlow, children: t })
      : null;
}
var qe = P(function ({
    actionType: e,
    buttonState: t,
    animationActive: a,
    onAnimationEnded: s,
    className: r,
  }) {
    const n = Ae(),
      i = ae.resolve("strings"),
      o = C.toUpperCase(
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
    return (0, Ve.jsxs)("div", {
      className: ee(Ge.base, Ge[`base__${t}`], r),
      children: [
        (0, Ve.jsx)(w, {
          classNames: { base: Ge.textWrapper, text: Ge.text, textOverlay: Ge.textOverlay },
          children: o,
        }),
        (0, Ve.jsx)(Qe, { buttonState: t, buttonText: o, animationActive: a, onAnimationEnded: s }),
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
  Ke = P(function ({
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
      d = (function (e) {
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
      u = e === De;
    const _ = a && Je.includes(a) && Je.includes(e);
    return (0, Ve.jsx)("div", {
      ...(u && l && d),
      className: n,
      children: (0, Ve.jsxs)(c, {
        theme: c.themes.custom,
        disabled: u,
        autoAlignContent: !1,
        onClick: function () {
          u || o.controls.actionPrebattle(s);
        },
        className: ee(Ye.button, Ye[`button__${e}`]),
        classNames: {
          background: ee(Ye.background, Ye[`background__${e}`], t && !_ && Ye.background__appear),
          content: Ye.content,
          border: Ye.border,
          overlay: Ye.overlay,
        },
        "data-test-id": "battleButton",
        soundTarget: "battleButton",
        children: [
          t &&
            !_ &&
            (0, Ve.jsx)("div", {
              className: ee(Ye.background, Ye.background__dissapear, Ye[`background__${a}`]),
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
  at = P(function ({ classNames: e }) {
    const t = Ae(),
      [a, s] = (0, Se.useState)(!1),
      [r, n] = (0, Se.useState)(!1),
      [i, o] = (0, Se.useState)(),
      { model: l, controls: c } = Pe(),
      d = l.computes.triggersCount(),
      u = v(),
      _ = "BATTLE_ROYALE_TOURNAMENT" === t.model.queueType.get(),
      m = "TRAINING" === t.model.currentMode.get(),
      b =
        (!t.model.states.get("playerCreator") && !m && t.model.states.get("readinessAvailable")) ||
        _
          ? "readyAction"
          : "battleStartAction",
      p = (function (e, t, a) {
        return t ? De : "battleStartAction" === e ? We : a ? Re : we;
      })(b, !t.model.states.get("actionEnabled"), t.model.states.get(Be)),
      f = T(p),
      g = p === De;
    return (
      (0, Se.useEffect)(
        () =>
          ie(() => {
            const e = E(l.triggers.get(), (e) => e.componentId === Ze);
            ((d > 0 && e) || (f && p !== f)) && c.onTriggerActivated(Ze, et, !0);
          }),
        [p, c, l.triggers, f, d],
      ),
      (0, Se.useEffect)(() => {
        f &&
          p !== f &&
          (n(!0),
          o(f),
          u.run(() => {
            n(!1);
          }, 600));
      }, [u, p, f]),
      (0, Se.useLayoutEffect)(
        () => () => {
          c.onTriggerActivated(Ze, et, !1);
        },
        [],
      ),
      (0, Ve.jsxs)(tt, {
        className: e?.base,
        id: "fight-button",
        children: [
          (0, Ve.jsx)(ze, { buttonState: p, className: ee(Xe.backgroundEffects, e?.effect) }),
          (0, Ve.jsxs)(Ke, {
            actionType: b,
            buttonState: p,
            transitionActive: r,
            transitionFromState: i,
            className: e?.content,
            children: [
              !g && (0, Ve.jsx)("div", { className: ee(Xe.reflector, Xe[`reflector__${p}`]) }),
              p === We &&
                (0, Ve.jsx)(Ue, { className: Xe.buttonEffects, onAnimationStarted: () => s(!0) }),
              (0, Ve.jsx)("div", { className: Xe.hoverOverlay }),
              (0, Ve.jsx)("div", { className: ee(Xe.desaturation, !g && Xe.desaturation__hidden) }),
              (0, Ve.jsx)(qe, {
                actionType: b,
                buttonState: p,
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
    (0, Ve.jsx)(Me, { options: e, children: (0, Ve.jsx)(at, { ...t }) }),
  );
function rt() {
  const e = d().paramsStruct.routeType;
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
      d = b({ header: s, body: r }),
      u = D(e, te);
    return (0, Ve.jsxs)(c, {
      ...i,
      onClick: function (e) {
        (l && d.onClick(), i.onClick?.(e));
      },
      onMouseEnter: function (e) {
        (l && d.onMouseEnter(e), i.onMouseEnter?.(e));
      },
      onMouseLeave: function (e) {
        (d.onMouseLeave(), i.onMouseLeave?.(e));
      },
      ref: o,
      size: c.sizes.small,
      theme: c.themes.secondary,
      autoAlignContent: !1,
      className: ee(nt.base, nt[`base__${e}Size`], i.className),
      classNames: { ...n, content: ee(nt.content, a && nt.content__label, n?.content) },
      children: [
        (0, Ve.jsx)("div", { className: nt.border }),
        (0, Ve.jsx)(k, {
          className: nt.icon,
          path: `header_footer.info_icon_${t}_${u}`,
          height: ot[e],
          width: ot[e],
        }),
        a && (0, Ve.jsx)("div", { className: nt.label, children: a }),
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
  xt = "NavigationBar_pageTitle_5847696c",
  yt = "NavigationBar_hiddenLabel_1fa48c6e",
  Nt = "NavigationBar_base__ready_69a10af0",
  Bt = "NavigationBar_base__animating_69a10af0",
  jt = "NavigationBar_hiddenLabelInner_8490d7c",
  It = "NavigationBar_infoButton_8aaee3f9",
  Et = "NavigationBar_infoButton__last_efa963fb";
function At({ classNames: e = {} }) {
  return (0, Ve.jsxs)("div", {
    className: ee(mt, e.icon),
    children: [
      (0, Ve.jsx)("div", { className: ee(bt, pt, e.iconImage, e.iconImage__default) }),
      (0, Ve.jsx)("div", { className: ee(bt, vt, e.iconImage, e.iconImage__hover) }),
      (0, Ve.jsx)("div", { className: ee(bt, ft, e.iconImage, e.iconImage__active) }),
    ],
  });
}
var Ct = P(function ({
    classNames: e = {},
    className: t,
    garageNavigationAllowed: a,
    battleButtonVisible: s,
  }) {
    const { model: r, controls: n } = ge(),
      i = re(),
      o = ae.resolve("strings"),
      l = r.pageTitle.get(),
      c = r.backNavigationAllowed.get(),
      d = r.backNavigationDescription.get(),
      u = r.infoButtons.get();
    function m(e) {
      i.play("mouse-enter", { target: "NavigationButton", original: e });
    }
    function b(e) {
      return function () {
        n.doInfoAction(e);
      };
    }
    const v = q(),
      f = ae.resolve("intl"),
      g = (0, Se.useRef)(null),
      [h, x] = (0, Se.useState)(0),
      [y, N] = (0, Se.useState)(!1),
      [B, j] = (0, Se.useState)(!1);
    K(() => {
      (N(!0), x(g.current?.offsetWidth ? g.current?.offsetWidth + 1 : 0));
      const e = p(() => j(!0));
      return () => {
        (N(!1), x(0), j(!1), e());
      };
    }, [v.screenWidthRem, v.breakpoint.name, a, s, c, d, l]);
    const I = G({ value: lt.sizes.small }, { extraLarge: { value: lt.sizes.medium } });
    return (0, Ve.jsxs)("div", {
      className: ee(ct, y && Nt, B && Bt, t, e.base),
      children: [
        (0, Ve.jsxs)(le, {
          className: ee(ht, e.divider),
          children: [
            a &&
              (0, Ve.jsxs)("div", {
                className: ee(dt, gt, e.button, e.button__garageNavigation),
                "data-test-id": "garageButton",
                onClick: function (e) {
                  (i.play("click", { target: "NavigationButton", original: e }),
                    n.navigateTo("garage"));
                },
                onMouseEnter: m,
                children: [
                  (0, Ve.jsx)(At, { classNames: e }),
                  (0, Ve.jsx)("div", {
                    className: ee(_t, e.label),
                    children: f.toUpperCase(o.readOrEmpty("menu.headerButtons.hangar")),
                  }),
                ],
              }),
            c &&
              (0, Ve.jsx)(Ve.Fragment, {
                children: (0, Ve.jsxs)("div", {
                  className: ee(dt, ut, e.button, e.button__backNavigation),
                  onClick: function (e) {
                    (i.play("click", { target: "NavigationButton", original: e }),
                      n.navigateTo("back"));
                  },
                  onMouseEnter: m,
                  children: [
                    (0, Ve.jsx)(At, { classNames: e }),
                    (0, Ve.jsx)("div", {
                      className: ee(_t, e.label),
                      children: f.toUpperCase(o.readOrEmpty("menu.headerButtons.navigation.back")),
                    }),
                    d &&
                      (0, Ve.jsx)("div", {
                        ref: g,
                        className: ee(yt, e.hiddenLabel),
                        style: { "--width": `${h}px` },
                        children: (0, Ve.jsx)(_, { className: jt, text: f.toUpperCase(d) }),
                      }),
                  ],
                }),
              }),
            l &&
              (0, Ve.jsx)(Ve.Fragment, {
                children: (0, Ve.jsx)("div", {
                  className: ee(xt, e.title),
                  children: (0, Ve.jsx)(_, { text: f.toUpperCase(l) }),
                }),
              }),
          ],
        }),
        u.length > 0 &&
          O(u, (t, a) =>
            (0, Ve.jsx)(
              "div",
              {
                className: ee(It, a === u.length - 1 && Et, e?.infoButton),
                children: (0, Ve.jsx)(lt, {
                  size: I.value,
                  onClick: b(a),
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
  Vt = "PlayersProfile_anonymizerIcon_8632eb46",
  Lt = "PlayersProfile_alertIcon_b8de5d15",
  zt = ae.resolve("strings"),
  $t = Z("PlayersProfile", Tt, { variants: { alertVisible: { true: Ht } } }),
  Ft = new Set([kt.ADD_NEEDED, kt.ADDED]),
  Ut = { width: "48rem", height: "48rem", marginLeft: "-35rem" },
  Gt = P(function () {
    const e = re(),
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
        steamEmailStatus: m,
        anonymized: p,
        email: v,
      } = s.userInfo.get(),
      f = F(
        "AccountCompletion",
        (0, Se.useMemo)(() => [v], [v]),
      ),
      g = u && Ft.has(m);
    const h = D(S.Badge.sizes.x48x48, S.Badge.sizes.x80x80),
      x = D(S.Stripe.sizes.medium, S.Stripe.sizes.big);
    return (0, Ve.jsxs)($t, {
      alertVisible: g,
      children: [
        (0, Ve.jsxs)(S, {
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
              (0, Ve.jsx)("div", {
                className: Mt,
                children: (0, Ve.jsx)(S.Badge, {
                  badgeId: String(i),
                  width: 48,
                  height: 48,
                  size: h,
                  className: Wt,
                }),
              }),
            (0, Ve.jsxs)(S.Wrapper, {
              className: St,
              children: [
                (0, Ve.jsx)(S.Name, {
                  className: ee(wt, Rt, d && Dt),
                  children: (0, Ve.jsx)(_, { text: n }),
                }),
                o &&
                  (0, Ve.jsx)(S.ClanTag, {
                    className: wt,
                    children: (0, Ve.jsx)(t, {
                      upgradeLegacy: !0,
                      path: "common.clanTag",
                      params: { abbrev: l },
                    }),
                  }),
              ],
            }),
            c > 0 &&
              (0, Ve.jsx)("div", {
                className: Ot,
                children: (0, Ve.jsx)(S.Stripe, {
                  badgeId: String(c),
                  size: x,
                  stripeIcon: S.Stripe.icons.stripe.medium,
                  stipeBadgeIcon: S.Stripe.icons.badge.medium,
                  style: Ut,
                }),
              }),
            p && (0, Ve.jsx)("div", { className: Vt }),
          ],
        }),
        g && (0, Ve.jsx)("div", { ...f, className: Lt }),
      ],
    });
  }),
  Qt = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Ve.jsx)(_e, { options: e, children: (0, Ve.jsx)(Gt, { ...t }) }),
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
  oa = Z("PremiumShop", ee(qt, "Premiums_base__clickable_dd8e69b8")),
  la = ae.resolve("strings");
function ca() {
  const { model: e, controls: t } = ke(),
    a = re(),
    s = b({
      header: la.readOrEmpty("tooltips.header.premShop.header"),
      body: la.readOrEmpty("tooltips.header.premShop.body"),
    });
  if (e.premiumShopEnabled.get())
    return (0, Ve.jsxs)(oa, {
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
        (0, Ve.jsx)("div", { className: ia }),
        (0, Ve.jsx)("div", {
          className: ee(Kt, Xt),
          children: la.readOrEmpty("menu.headerButtons.btnLabel.premShop"),
        }),
      ],
    });
}
var da = (function (e) {
    return ((e.Inactive = "Inactive"), (e.Active = "Active"), (e.Cancelled = "Cancelled"), e);
  })({}),
  ua = Z("Premiums", qt),
  _a = ae.resolve("strings"),
  ma = ae.resolve("aliases"),
  ba = ae.resolve("views");
var pa = P(function ({ className: e }) {
    const s = re(),
      n = a({
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
      x = r(
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
      y = b({ body: _a.readOrEmpty("subscription.headerButton.tooltip.unavailable") });
    const N = v && v === ue.Active;
    return (0, Ve.jsxs)(ua, {
      className: e,
      children: [
        (0, Ve.jsxs)("div", {
          ...(f ? x : y),
          className: ee(Yt, !f && Jt),
          "data-test-id": "wotPlus",
          onClick: f
            ? function (e) {
                ((h.current = !0),
                  x.onClick(),
                  s.play("click", { target: "premiums:wot-plus", original: e }),
                  requestAnimationFrame(() => {
                    o.openWotPlusSubscriptionPage();
                  }));
              }
            : void 0,
          onMouseEnter: function (e) {
            h.current ||
              (f ? x?.onMouseEnter(e) : y?.onMouseEnter(e),
              s.play("mouse-enter", { target: "premiums:wot-plus", original: e }));
          },
          children: [
            (0, Ve.jsx)("div", { className: ee(ea, !N && ta, p === de.Pro && N && aa) }),
            (0, Ve.jsx)("div", {
              className: Kt,
              children: _a.readOrEmpty(
                v === ue.Active || v === ue.Cancelled
                  ? "subscription.headerButton.state.active"
                  : "subscription.headerButton.state.available",
              ),
            }),
            v === ue.Cancelled &&
              (0, Ve.jsx)(k, { path: "subscription.alert_icon", className: sa }),
          ],
        }),
        (0, Ve.jsx)(ce, { className: Zt }),
        (0, Ve.jsxs)("div", {
          ...n,
          className: Yt,
          "data-test-id": "premium",
          onClick: function (e) {
            (n.onClick(),
              s.play("click", { target: "premiums:premium", original: e }),
              o.openPremiumSubscriptionPage());
          },
          onMouseEnter: function (e) {
            (n.onMouseEnter(e), s.play("mouse-enter", { target: "premiums:premium", original: e }));
          },
          children: [
            (0, Ve.jsx)("div", { className: ee(ra, g === da.Inactive && na) }),
            (0, Ve.jsx)("div", {
              className: Kt,
              children:
                g === da.Active && m
                  ? (0, Ve.jsx)("span", {
                      children: (0, Ve.jsx)(t, {
                        path: `menu.timeLeft.short.${m.unit}`,
                        params: { [m.unit]: Math.ceil(m.value) },
                        upgradeLegacy: !0,
                      }),
                    })
                  : (0, Ve.jsx)("span", { children: _a.readOrEmpty("menu.common.premiumBuy") }),
            }),
          ],
        }),
      ],
    });
  }),
  va = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Ve.jsx)(_e, { options: e, children: (0, Ve.jsx)(pa, { ...t }) }),
  ),
  fa = "UserProfile_2146e52",
  ga = "UserProfile_divider_4a395a41",
  ha = ae.resolve("aliases"),
  xa = ha.read((e) => e.lobby_header.default.UserAccount("resId")),
  ya = ha.read((e) => e.lobby_header.default.PremShop("resId"));
function Na({ className: e }) {
  const t = n(xa);
  return (0, Ve.jsx)("div", {
    className: ee(fa, e),
    children: (0, Ve.jsxs)(le, {
      className: ga,
      children: [
        t && (0, Ve.jsx)(Qt, { options: { rootId: xa } }),
        t && (0, Ve.jsx)(va, { options: { rootId: xa } }),
        ya && (0, Ve.jsx)(ca, {}),
      ],
    }),
  });
}
var Ba = P(function ({ garageNavigationAllowed: e, battleButtonVisible: t, classNames: a }) {
    return rt() === be.Hangar
      ? (0, Ve.jsx)(Na, { className: a?.userProfile })
      : (0, Ve.jsx)(Ct, {
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
  return Math.max(0, Math.floor(e - Date.now() / l));
}
var [Ma, Oa] = z()(
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
        a = J.primitive(() => E(t.reserves.get(), (e) => e.inactivationTime > 0)),
        s = J.shallow(() => {
          const e = t.reserves.get();
          return Y(e, (e, t) => Pa(e.reserveType) - Pa(t.reserveType));
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
  Va = "Activate_icon__glow_6978c825",
  La = "Activate_amount_262c55ed",
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
  Za = P(function () {
    const { model: e } = Oa(),
      t = ae.resolve("strings"),
      a = ae.resolve("intl"),
      s = e.computes.visible(),
      r = e.allReserves.get(),
      n = e.limitedReserves.get(),
      i = e.reserveExpire.get(),
      o = e.computes.disabled();
    return s
      ? null
      : (0, Ve.jsxs)("div", {
          className: ee(Wa, o && wa),
          children: [
            (0, Ve.jsxs)("div", {
              className: Ra,
              children: [
                (0, Ve.jsx)("div", { className: ee(Ka, i && Xa) }),
                (0, Ve.jsx)("div", { className: ee(qa, n && Ya, i && Ja) }),
                (0, Ve.jsx)("div", {
                  className: Da,
                  children: (0, Ve.jsx)("div", { className: ee(Ha, n && Va) }),
                }),
                (0, Ve.jsx)(w, {
                  classNames: { base: La, text: ee(za, n && $a), textOverlay: ee(Fa, n && Ua) },
                  children: a.formatNumber("integral", r),
                }),
              ],
            }),
            !o &&
              (0, Ve.jsx)("div", {
                className: ee(Ga, n && Qa),
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
  ts = P(function ({ type: e, timeLeft: a, timeTotal: s, icon: r, className: n }) {
    const { model: i } = Oa(),
      { minutesLeft: o, percentLeft: c } = (function (e, t) {
        const [a, s] = (0, Se.useState)(Sa(e));
        ((0, Se.useEffect)(() => {
          s(Sa(e));
        }, [e]),
          (0, Se.useEffect)(() => {
            if (0 === a) return;
            const t = setTimeout(() => {
              s(Sa(e));
            }, l);
            return () => clearTimeout(t);
          }, [a, e]));
        const r = u(a),
          n = Math.ceil(f(r));
        return { minutesLeft: n, percentLeft: Math.max(0, Math.min(100, (n / (t / 60)) * 100)) };
      })(a, s),
      d = i.computes.disabled(),
      _ = o <= 9,
      m = o <= 2,
      b = G({ size: Aa }, { large: { size: Ca } }),
      p = D(b.size, ka),
      v = r.includes("premium");
    return a <= 0
      ? null
      : (0, Ve.jsxs)("div", {
          className: ee(es.base, d && es.base__disabled, n),
          style: { "--fill_percentage": `${c}%` },
          children: [
            (0, Ve.jsx)("div", { className: ee(es.background, es[`background__${_ ? Ea : e}`]) }),
            (0, Ve.jsx)(k, {
              className: es.icon,
              path: `personal_reserves.common.cards.${p}.${r}`,
            }),
            (0, Ve.jsx)(k, {
              className: ee(es.premium, v && es.premium__visible),
              path: `personal_reserves.common.cards.${b.size}.premium_booster_glow`,
            }),
            (0, Ve.jsxs)("div", {
              className: ee(es.timer, _ && es.timer__visible),
              children: [
                (0, Ve.jsx)("div", { className: es.timerGlow }),
                (0, Ve.jsx)(t, {
                  upgradeLegacy: !0,
                  path: "personal_reserves.hangarEntry.minute",
                  params: { minutesLeft: o },
                }),
              ],
            }),
            (0, Ve.jsx)("div", { className: ee(es.alert, m && es.alert__visible) }),
            (0, Ve.jsxs)("div", {
              className: es.fill,
              children: [
                (0, Ve.jsx)("div", {
                  className: ee(es.fillPattern, es[`fillPattern__${_ ? Ea : e}`]),
                }),
                (0, Ve.jsx)("div", {
                  className: ee(es.fillBorderTop, m && es.fillBorderTop__alert),
                }),
                (0, Ve.jsx)("div", {
                  className: ee(es.fillBorderBottom, _ && es.fillBorderBottom__visible),
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
  cs = P(function () {
    const { model: e } = Oa(),
      t = e.computes.sortedBoosters(),
      a = e.computes.visible(),
      s = e.computes.disabled();
    return a
      ? (0, Ve.jsxs)("div", {
          className: ee(ns, s && is),
          children: [
            (0, Ve.jsx)("div", { className: as }),
            (0, Ve.jsx)("div", { className: ss }),
            (0, Ve.jsx)("div", { className: rs }),
            (0, Ve.jsx)("div", {
              className: os,
              children: o(
                t,
                (e) => e.state === Ia.Active,
                (e) =>
                  (0, Ve.jsx)(
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
  _s = P(function () {
    const { model: e, controls: t } = Oa(),
      s = (function () {
        const e = ae.resolve("views");
        return a({
          resId: ae
            .resolve("aliases")
            .read((e) => e.lobby_header.default.ReservesEntryPoint("resId")),
          contentId: e.read((e) => e.lobby.personal_reserves.PersonalReservesTooltip("resId")),
        });
      })(),
      r = re(),
      n = e.computes.disabled();
    return (0, Ve.jsxs)("div", {
      ...s,
      className: ee(ds, n && us),
      onClick: function (e) {
        (s.onClick(), n || (r.play("click", { target: "reserves", original: e }), t.openBooster()));
      },
      onMouseEnter: function (e) {
        (s.onMouseEnter(e), n || r.play("mouse-enter", { target: "reserves", original: e }));
      },
      "data-test-id": "reservesButton",
      children: [(0, Ve.jsx)(cs, {}), (0, Ve.jsx)(Za, {})],
    });
  }),
  ms = (0, Se.memo)(({ options: e, ...t }) =>
    (0, Ve.jsx)(Ma, { options: e, children: (0, Ve.jsx)(_s, { ...t }) }),
  ),
  [bs, ps] = z("WalletModel")(
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
  xs = "Hint_discountWithHintText_381cf018",
  ys = "Hint_onlyHintText_751386e1",
  Ns = "Hint_discountValue_b1f389fc",
  Bs = "Hint_discountHintTitle_9db2d839",
  js = "Hint_hintText_6f3fa83f",
  Is = "Hint_hintTitle_135a3ed",
  Es = "Hint_discountValue__withHint_e7bbe38f";
function As({ classNames: e }) {
  const t = ae.resolve("strings");
  return (0, Ve.jsxs)("div", {
    className: ee(hs, e?.onlyDiscount),
    children: [
      (0, Ve.jsx)("div", { className: ee(fs, e?.discountBackground) }),
      (0, Ve.jsx)(g.Root, {
        children: (0, Ve.jsx)(g.Value, {
          value: t.readOrEmpty("common.common.percent"),
          classNames: { valueContainer: ee(gs, e?.discount), value: ee(Ns, e?.discountValue) },
        }),
      }),
    ],
  });
}
function Cs({ type: e, classNames: t }) {
  const a = ae.resolve("intl"),
    s = ae.resolve("strings");
  return (0, Ve.jsx)("div", {
    className: ee(js, ys, t?.hintText, t?.onlyHintText),
    children: (0, Ve.jsx)(w, {
      classNames: t?.textGradient,
      children: (0, Ve.jsx)("div", {
        className: ee(Is, t?.hintTitle),
        children: a.toUpperCase(s.readOrEmpty(`menu.headerButtons.btnLabel.${e}`)),
      }),
    }),
  });
}
function ks({ classNames: e, type: t }) {
  const a = ae.resolve("intl"),
    s = ae.resolve("strings");
  return (0, Ve.jsxs)("div", {
    className: ee(xs, e?.discountWithHintText),
    children: [
      (0, Ve.jsx)("div", { className: ee(fs, e?.discountBackground) }),
      (0, Ve.jsx)("div", {
        className: ee(Bs, e?.discountHintTitle),
        children: a.toUpperCase(s.readOrEmpty(`menu.headerButtons.btnLabel.${t}`)),
      }),
      (0, Ve.jsx)(g.Root, {
        children: (0, Ve.jsx)(g.Value, {
          value: s.readOrEmpty("common.common.percent"),
          classNames: { valueContainer: ee(gs, e?.discount), value: ee(Ns, Es, e?.discountValue) },
        }),
      }),
    ],
  });
}
function Ts({ classNames: e, type: t }) {
  return (0, Ve.jsxs)("div", {
    className: ee(vs, e?.base),
    children: [
      (0, Ve.jsx)(As, {
        classNames: {
          onlyDiscount: e?.onlyDiscount,
          discountBackground: e?.discountBackground,
          discount: e?.discount,
          discountValue: e?.discountValue,
        },
      }),
      (0, Ve.jsx)(Cs, {
        type: t,
        classNames: {
          hintText: e?.hintText,
          textGradient: e?.textGradient,
          onlyHintText: e?.onlyHintText,
        },
      }),
      (0, Ve.jsx)(ks, { classNames: e, type: t }),
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
    i = ae.resolve("intl"),
    o = ae.resolve("strings"),
    l = G(
      {
        displayValue: () =>
          a >= Ss
            ? { abbreviated: !0, value: y(a, Ms, "floor") / Ss }
            : { abbreviated: !1, value: a },
      },
      {
        medium: {
          displayValue: () =>
            a >= 1e7
              ? { abbreviated: !0, value: y(a, Ms, "floor") / Ss }
              : { abbreviated: !1, value: a },
        },
        large: {
          displayValue: () =>
            a >= 1e8
              ? { abbreviated: !0, value: y(a, Ms, "floor") / Ss }
              : { value: a, abbreviated: !1 },
        },
      },
    );
  if (!1 === e)
    return (0, Ve.jsxs)("div", {
      className: ee(Ps.value, Ps.value__unavailable, r?.value),
      children: [
        (0, Ve.jsx)("div", {
          className: Ps.dash,
          children: o.readOrEmpty("common.common.semi_dash"),
        }),
        (0, Ve.jsx)("div", {
          className: Ps.dash,
          children: o.readOrEmpty("common.common.semi_dash"),
        }),
      ],
    });
  const c = l.displayValue();
  return (0, Ve.jsx)("div", {
    ref: n,
    className: ee(Ps.value, r?.base),
    children: c.abbreviated
      ? (0, Ve.jsx)(t, {
          path: "menu.hangar_header.million",
          params: { value: c.value },
          brackets: { start: "%(", end: ")s" },
          className: ee(Ps.formattedValue, r?.formattedValue),
        })
      : i.formatNumber(s === x.gold ? "gold" : "integral", c.value),
  });
}
var Ws = P(function ({ currency: e, type: t, className: a, classNames: s }) {
    const { controls: r } = ps(),
      n = re(),
      i = "AVAILABLE" === e.status,
      o = (function (e, t, a, s) {
        const r = ae.resolve("strings"),
          n = b({
            header: r.readOrEmpty(`tooltips.header.buttons.${e}.header`),
            body: r.readOrEmpty(`tooltips.header.buttons.${e}.body`),
          }),
          i = (0, Se.useMemo)(() => ({ disabled: "string" != typeof a || "" === a }), [a]),
          o = U(
            a,
            (0, Se.useMemo)(() => [s], [s]),
            i,
          );
        return !1 === t ? n : o;
      })(t, i, e.tooltipType, e.value),
      l = D(
        G({ size: ne.extraSmall }, { large: { size: ne.small }, extraLarge: { size: ne.medium } })
          .size,
        ne.small,
      );
    return (0, Ve.jsxs)("div", {
      ...o,
      className: ee(
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
        (0, Ve.jsx)("div", {
          className: ee(Ps.currencyWrapper, s?.currencyWrapper),
          children: (0, Ve.jsx)(I, {
            reverse: !0,
            classNames: { ...s?.currency, icon: ee(Ps.currencyIcon, s?.currency?.icon) },
            type: t,
            size: l,
            "data-test-id": t,
            children: (0, Ve.jsx)(Os, {
              wgMoneyAvailable: i,
              value: e.value,
              type: t,
              classNames: s?.currencyValue,
            }),
          }),
        }),
        i &&
          (0, Ve.jsx)("div", {
            className: ee(Ps.hintWrapper, s?.hintWrapper),
            children: (0, Ve.jsx)(Ts, {
              type: t,
              classNames: {
                ...s?.hint,
                discountWithHintText: ee(Ps.discountWithHintText, s?.hint?.discountWithHintText),
                onlyDiscount: ee(Ps.onlyDiscount, s?.hint?.onlyDiscount),
                onlyHintText: ee(Ps.onlyHintText, s?.hint?.onlyHintText),
                base: ee(Ps.hint, s?.hint?.base),
                textGradient: { text: Ps.text, textOverlay: ee(Ps.text, Ps.text__overlay) },
              },
            }),
          }),
      ],
    });
  }),
  ws = P(function (e) {
    const t = ps().model.currencies.get(e.type);
    return t
      ? (0, Ve.jsx)(Ws, { ...e, currency: t })
      : (console.error(`Currency with type ${e.type} is not defined`), null);
  }),
  Rs = "Wallet_fc600169",
  Ds = [x.crystal, x.gold, x.credits],
  Hs = P(function ({ className: e, classNames: t, currenciesOrder: a = Ds }) {
    const { model: s } = ps(),
      r = s.list(a);
    return (0, Ve.jsx)("div", {
      "data-name": "Wallet",
      className: ee(Rs, e),
      children: r.map((e) => (0, Ve.jsx)(ws, { type: e, classNames: t }, e)),
    });
  }),
  Vs = (0, Se.memo)(({ className: e, classNames: t, currenciesOrder: a, ...s }) =>
    (0, Ve.jsx)(bs, {
      ...s,
      children: (0, Ve.jsx)(Hs, { className: e, classNames: t, currenciesOrder: a }),
    }),
  ),
  Ls = "RightSide_7ef6e2a9",
  zs = "RightSide_separator_fea82003",
  $s = ae.resolve("aliases"),
  Fs = $s.read((e) => e.lobby_header.default.ReservesEntryPoint("resId")),
  Us = $s.read((e) => e.lobby_header.default.Wallet("resId")),
  Gs = function () {
    const e = n(Fs),
      t = n(Us);
    return (0, Ve.jsx)("div", {
      className: Ls,
      children: (0, Ve.jsxs)(le, {
        className: zs,
        children: [
          e && (0, Ve.jsx)(ms, { options: { rootId: Fs } }),
          t && (0, Ve.jsx)(Vs, { options: { rootId: Us } }),
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
  Ks = P(function ({ className: e }) {
    const a = Ae(),
      s = a.model.currentMode.get(),
      r = xe(),
      n = a.model.currentModeId.get(),
      i = ((o = n), "BATTLE_ROYALE_TOURNAMENT" !== a.model.queueType.get() && qs.has(o));
    var o;
    const l = r.model.vehicle();
    if (void 0 !== l)
      return i
        ? (0, Ve.jsx)(t, {
            className: ee(Js.base, Js[`base__${n}`], e),
            path: "menu.headerButtons.battle.vehicleInfo",
            params: {
              mode: s,
              level: Ys(n) ? (0, Ve.jsx)($, { value: l.level, className: Js.details }) : "",
              type: (0, Ve.jsx)(L, {
                className: Js.vehicleType,
                type: l.type,
                size: L.sizes.x24x24,
              }),
              name: (0, Ve.jsx)("div", { className: Js.details, children: l.shortName }),
            },
          })
        : (0, Ve.jsx)(t, {
            className: ee(Js.base, e),
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
  er = ae.resolve("aliases").read((e) => e.lobby_header.default.FightStart("resId")),
  tr = new Set([je, Ie]),
  ar = new Set(["mapsTraining"]);
var sr = P(function () {
    const e = A(0, 250),
      t = d(),
      a = Ne(),
      s = Ae(),
      [r, i] = (0, Se.useState)(!1),
      o = s.model.battleStatus.get(),
      l = s.model.battleButtonAlwaysOn.get(),
      c = !s.model.computes.isSearchingBattle() && !s.model.computes.isBattleReady(),
      u = rt(),
      _ = Boolean(
        m(t.location, { paths: ["/:hangar/allVehicles", "/:eventName/:hangar/allVehicles"] }),
      ),
      b = t.location.includes("/postBattleResults"),
      p = n(er),
      v = s.model.currentModeId.get();
    return (
      (0, Se.useEffect)(() => {
        p
          ? b && ar.has(v)
            ? i(!1)
            : l
              ? i(!0)
              : tr.has(o)
                ? i(!1)
                : i(u === be.Hangar || _ || b)
          : i(!1);
      }, [l, o, u, _, b, p, v]),
      (0, Ve.jsxs)(Zs, {
        ref: e,
        oldStyle: a.model.oldStyle.get(),
        battleButtonVisible: r,
        children: [
          (0, Ve.jsx)("div", {
            className: Xs.leftSide,
            children: (0, Ve.jsx)(Ba, {
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
            (0, Ve.jsxs)(Ve.Fragment, {
              children: [
                (0, Ve.jsx)(st, {
                  options: { rootId: er },
                  classNames: {
                    base: ee(
                      Xs.battleButton,
                      u === be.Hangar || _
                        ? Xs.battleButton__withoutFadein
                        : Xs.battleButton__fadein,
                    ),
                    effect: Xs.battleButtonEffects,
                  },
                }),
                b &&
                  (0, Ve.jsx)("div", {
                    className: Xs.vehicleInfoWrapper,
                    children: (0, Ve.jsx)(Ks, {}),
                  }),
              ],
            }),
          (0, Ve.jsx)("div", {
            className: ee(Xs.rightSide, r && Xs.rightSide__battleButtonVisible),
            children:
              !s.model.computes.isSearchingBattle() &&
              !s.model.computes.isBattleReady() &&
              (0, Ve.jsx)(Gs, {}),
          }),
        ],
      })
    );
  }),
  rr = ae.resolve("aliases"),
  nr = N({ click: { battleButton: "gui_battle" } });
se(
  new M()
    .addWithProps(Q, { soundsOverrides: nr })
    .add(ye)
    .addWithProps(i, {
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
    .render((0, Ve.jsx)(sr, {})),
);
