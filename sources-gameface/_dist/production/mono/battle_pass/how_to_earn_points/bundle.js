import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Br as a,
  Cr as t,
  Er as n,
  Et as l,
  Jt as s,
  Kt as i,
  Ln as o,
  Lr as c,
  Or as _,
  Ot as d,
  Qn as r,
  Rn as m,
  Rt as b,
  Sr as p,
  Tt as u,
  Xn as T,
  Yn as g,
  Yt as x,
  Zr as h,
  Zt as v,
  _n as f,
  ci as C,
  dr as j,
  en as E,
  fn as N,
  gn as I,
  gr as y,
  ir as A,
  pi as L,
  pn as w,
  qn as O,
  qt as P,
  tn as B,
  ui as S,
  wt as k,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as M } from "../chunks/vendor.js";
import { t as F } from "../chunks/tank_name.js";
var G = e(S(), 1),
  D = (function (e) {
    return (
      (e[(e.REGULAR = 1)] = "REGULAR"),
      (e[(e.RANKED = 22)] = "RANKED"),
      (e[(e.BATTLE_ROYALE_SOLO = 29)] = "BATTLE_ROYALE_SOLO"),
      (e[(e.EPIC_BATTLE = 27)] = "EPIC_BATTLE"),
      (e[(e.COMP7 = 43)] = "COMP7"),
      (e[(e.COMP7_LIGHT = 49)] = "COMP7_LIGHT"),
      e
    );
  })({}),
  $ = (function (e) {
    return ((e[(e.LIMIT = 0)] = "LIMIT"), (e[(e.DAILY = 1)] = "DAILY"), e);
  })({}),
  [W, z] = f()(
    ({ observableModel: e }) => {
      const n = {
          root: e.object(),
          gameModes: e.array("gameModes"),
          selectedGameMode: y.box(D.REGULAR),
        },
        l = I(() => n.gameModes.get(), { equals: a }),
        s = I(() => t(l(), (e) => e.arenaBonusType === n.selectedGameMode.get()) || 0, {
          equals: a,
        }),
        i = I(() => p(l(), (e) => e.arenaBonusType === n.selectedGameMode.get()), { equals: a }),
        o = I((e) => p(l(), (a) => e === a.arenaBonusType), { equals: a });
      return {
        ...n,
        computes: { getItems: l, getSlide: o, activeIndex: s, activeGameModeInfo: i },
      };
    },
    ({ externalModel: e, model: a }) => {
      const t = j((e) => {
        a.selectedGameMode.set(e);
      });
      return {
        openWotPlus: e.createCallbackNoArgs("onWotPlusClick"),
        onGoToMissions: e.createCallbackNoArgs("onGoToMissions"),
        setSelectedGameMode: t,
      };
    },
  ),
  Y = R.images.gui.maps.icons,
  U = Y.battleTypes.c_136x136,
  H = Y.battleTypes.c_136x136,
  q = {
    [D.REGULAR]: { small: U.random(), large: H.random() },
    [D.BATTLE_ROYALE_SOLO]: { small: U.battle_royale(), large: H.battle_royale() },
    [D.EPIC_BATTLE]: { small: U.epicbattle(), large: H.epicbattle() },
    [D.COMP7]: { small: U.comp7(), large: H.comp7() },
    [D.COMP7_LIGHT]: { small: U.comp7Light(), large: H.comp7Light() },
  },
  V = {
    [D.REGULAR]: { levelRange: [4, 11] },
    [D.RANKED]: { levelRange: [10] },
    [D.BATTLE_ROYALE_SOLO]: { levelRange: [1] },
    [D.EPIC_BATTLE]: { levelRange: [8] },
    [D.COMP7]: { levelRange: [10] },
    [D.COMP7_LIGHT]: { levelRange: [8] },
  },
  K = "Tab_c3955d2a",
  Z = "Tab_asset_5cd5cc49",
  J = "Tab_base__active_0",
  Q = "Tab_container_e3bc117d",
  X = "Tab_title_960e90b1",
  ee = "Tab_conditions_5d132c9",
  ae = T(),
  te = L.resolve("strings"),
  ne = "battle_pass.howToEarnPoints",
  le = function ({ gameMode: e, isActive: a }) {
    const t = e.arenaBonusType,
      { breakpoint: n } = g(),
      l = n.weight >= r.medium.weight,
      { large: s, small: i } = q[t],
      o = V[t]?.levelRange ?? [],
      c =
        2 === o.length
          ? { startLevel: A(o[0]), endLevel: A(o[1]) }
          : { level: void 0 !== o[0] ? A(o[0]) : void 0 };
    return (0, ae.jsxs)("div", {
      className: C(K, a && J),
      children: [
        (0, ae.jsx)("div", { className: Z, style: { backgroundImage: `url(${l ? s : i})` } }),
        (0, ae.jsxs)("div", {
          className: Q,
          children: [
            (0, ae.jsx)("div", {
              className: X,
              children: te.readOrEmpty(`${ne}.battleTypeTitle.c_${t}`),
            }),
            (0, ae.jsx)("div", {
              className: ee,
              children: (0, ae.jsx)(E, {
                text: te.readOrEmpty(`${ne}.text.c_${t}`),
                upgradeLegacy: !0,
                params: c,
              }),
            }),
          ],
        }),
      ],
    });
  },
  se = {
    base: "CellContent_177ddb0a",
    additionalPoints: "CellContent_additionalPoints_5f0288bd",
    additionalPointsGlow: "CellContent_additionalPointsGlow_ee785ca8",
    additionalPointsDivider: "CellContent_additionalPointsDivider_739e6319",
    additionalPointsText: "CellContent_additionalPointsText_c401a44d",
    icon: "CellContent_icon_e330d96c",
    nationFlag: "CellContent_nationFlag_1e599ea1",
    nationFlag__ussr: "CellContent_nationFlag__ussr_a53ec45c",
    nationFlag__usa: "CellContent_nationFlag__usa_6d4f07d3",
    nationFlag__uk: "CellContent_nationFlag__uk_c56c878a",
    nationFlag__sweden: "CellContent_nationFlag__sweden_8c359e80",
    nationFlag__poland: "CellContent_nationFlag__poland_670bd31d",
    nationFlag__japan: "CellContent_nationFlag__japan_b4aac1d6",
    nationFlag__italy: "CellContent_nationFlag__italy_f23616cf",
    nationFlag__germany: "CellContent_nationFlag__germany_335c46bc",
    nationFlag__france: "CellContent_nationFlag__france_4f9745b1",
    nationFlag__czech: "CellContent_nationFlag__czech_20d72479",
    nationFlag__china: "CellContent_nationFlag__china_ab42d81b",
    level: "CellContent_level_da760857",
    name: "CellContent_name_43694647",
    fadeInWithScale: "CellContent_fadeInWithScale_da760857",
    slideUp: "CellContent_slideUp_da760857",
    blink: "CellContent_blink_da760857",
    scale: "CellContent_scale_da760857",
    rotate: "CellContent_rotate_da760857",
    windowIn: "CellContent_windowIn_da760857",
    fadeOut: "CellContent_fadeOut_da760857",
    fadeIn: "CellContent_fadeIn_da760857",
  },
  ie = ({ points: e, externalPoints: a, text: t, tableType: n, vehicleInfo: l }) => {
    const s = e > 0,
      i = a > 0,
      o = Boolean(t),
      c = !s && !i,
      _ = O({ vehicleTypeIconSize: d.x48x48 }, { extraLarge: { vehicleTypeIconSize: d.x64x64 } });
    if (c)
      return n !== Me.VEHICLES || o
        ? t
        : (0, ae.jsxs)(ae.Fragment, {
            children: [
              (0, ae.jsx)("div", {
                className: C(se.nationFlag, se[`nationFlag__${l.vehicleNation}`]),
              }),
              (0, ae.jsx)(F, {
                ...l,
                vehicleTypeIconSize: _.vehicleTypeIconSize,
                classNames: { level: se.level, name: se.name },
                isShortName: !0,
              }),
            ],
          });
    const r =
      i &&
      (0, ae.jsx)("div", {
        className: se.additionalPoints,
        children: s
          ? (0, ae.jsxs)(ae.Fragment, {
              children: [
                (0, ae.jsx)("div", { className: se.additionalPointsGlow }),
                (0, ae.jsx)("div", { className: se.additionalPointsDivider, children: "/" }),
                (0, ae.jsx)("div", { className: se.additionalPointsText, children: e + a }),
              ],
            })
          : (0, ae.jsx)("div", { className: se.additionalPointsText, children: `+ ${a}` }),
      });
    return (0, ae.jsxs)("div", {
      className: C(se.base, se[`base__${n}`]),
      children: [
        s && (0, ae.jsx)("div", { className: se.points, children: e }),
        r,
        (i || !s) && (0, ae.jsx)("div", { className: se.icon }),
      ],
    });
  },
  oe = {
    base: "Table_9c955553",
    base__battle_royal: "Table_base__battle_royal_ef69bf65",
    column: "Table_column_6acd9a5",
    cell: "Table_cell_4af15b7a",
    cell__content: "Table_cell__content_e5e43a36",
    cell__text: "Table_cell__text_4b942dd9",
    cell__truncated: "Table_cell__truncated_4ce15390",
    cell__inFirstRow: "Table_cell__inFirstRow_234e5f51",
    cell__column_0: "Table_cell__column_0_7c85074c",
    rowDivider: "Table_rowDivider_93df077b",
    fadeInWithScale: "Table_fadeInWithScale_ef69bf65",
    slideUp: "Table_slideUp_ef69bf65",
    blink: "Table_blink_ef69bf65",
    scale: "Table_scale_ef69bf65",
    rotate: "Table_rotate_ef69bf65",
    windowIn: "Table_windowIn_ef69bf65",
    fadeOut: "Table_fadeOut_ef69bf65",
    fadeIn: "Table_fadeIn_ef69bf65",
  },
  ce = ({ tableRows: e, tableType: a, shouldEnableTruncate: t = !1 }) => {
    const l = O({ isSmallScreen: !0 }, { medium: { isSmallScreen: !1 } }),
      s = n(e, 0)?.cell;
    if (!s) return null;
    const o = _(s, (a, t) => _(e, (e) => e.cell?.[t])),
      c = R.strings.settings.LANGUAGE_CODE();
    return (0, ae.jsx)("div", {
      className: C(oe.base, oe[`base__${a}`]),
      children: _(o, (e, n) =>
        (0, ae.jsx)(
          "div",
          {
            className: oe.column,
            children: _(e, (s, o) => {
              if (!s) return null;
              const { text: _, points: d, externalPoints: r, vehicleInfo: m } = s.value,
                b = Boolean(_),
                p = b && 0 === d && 0 === r,
                u = t && l.isSmallScreen && p,
                T = 0 === o,
                g = o === e.length - 1,
                x = C(
                  oe.cell,
                  b && oe.cell__text,
                  T ? oe.cell__inFirstRow : oe.cell__content,
                  oe[`cell__column_${n}`],
                  u && oe.cell__truncated,
                );
              return (0, ae.jsxs)(
                G.Fragment,
                {
                  children: [
                    u
                      ? (0, ae.jsx)(i, {
                          text: _,
                          className: x,
                          tooltipParams: { body: _ },
                          lang: c,
                        })
                      : (0, ae.jsx)("div", {
                          className: x,
                          lang: c,
                          children: (0, ae.jsx)(ie, {
                            points: d,
                            externalPoints: r,
                            text: _,
                            tableType: a,
                            vehicleInfo: m,
                          }),
                        }),
                    !g && (0, ae.jsx)("div", { className: oe.rowDivider }),
                  ],
                },
                `cell_${o}_${a}`,
              );
            }),
          },
          `column_${n}_${a}`,
        ),
      ),
    });
  },
  _e = "WotPlusBanner_4f7164a3",
  de = "WotPlusBanner_text_35aa0162",
  re = "WotPlusBanner_link_2fb44a00",
  me = L.resolve("strings"),
  be = M(() => {
    const { controls: e } = z(),
      a = me.readOrEmpty("battle_pass.howToEarnPoints.plusBanner.link"),
      t = O({ imageSize: 52 }, { large: { imageSize: 64 } });
    return (0, ae.jsxs)("div", {
      className: _e,
      children: [
        (0, ae.jsx)(b, {
          path: "battlePass.how_to_earn_points.plus_logo",
          width: t.imageSize,
          height: t.imageSize,
        }),
        (0, ae.jsxs)("div", {
          className: de,
          children: [
            (0, ae.jsx)(E, {
              text: me.readOrEmpty("battle_pass.howToEarnPoints.plusBanner.line1"),
              params: {
                link: (0, ae.jsx)("a", { className: re, onClick: e.openWotPlus, children: a }),
              },
              upgradeLegacy: !0,
            }),
            me.readOrEmpty("battle_pass.howToEarnPoints.plusBanner.line2"),
          ],
        }),
      ],
    });
  }),
  pe = "TabContent_tables_6de11214",
  ue = "TabContent_e5b5facf",
  Te = "TabContent_base__battleRoyal_7bbb6e2f",
  ge = "TabContent_conditions_6de11214",
  xe = "TabContent_title_38082bc8",
  he = L.resolve("strings"),
  ve = M(function () {
    const { model: e } = z(),
      { isWotPlusShown: a } = e.root.get(),
      { battleRoyaleCondtions: t } = e.computes.activeGameModeInfo();
    return (0, ae.jsxs)("div", {
      className: C(ue, Te),
      children: [
        (0, ae.jsxs)("div", {
          className: pe,
          children: [
            (0, ae.jsxs)("div", {
              className: ge,
              children: [
                (0, ae.jsx)("div", {
                  className: xe,
                  children: he.readOrEmpty("battle_pass.howToEarnPoints.battleRoyal.solo"),
                }),
                (0, ae.jsx)(ce, { tableRows: t.solo, tableType: Me.BATTLE_ROYAL }),
              ],
            }),
            (0, ae.jsxs)("div", {
              className: ge,
              children: [
                (0, ae.jsx)("div", {
                  className: xe,
                  children: he.readOrEmpty("battle_pass.howToEarnPoints.battleRoyal.platoon"),
                }),
                (0, ae.jsx)(ce, { tableRows: t.squad, tableType: Me.BATTLE_ROYAL }),
              ],
            }),
          ],
        }),
        a && (0, ae.jsx)(be, {}),
      ],
    });
  }),
  fe = R.strings.battle_pass.howToEarnPoints.card,
  Ce = R.images.gui.maps.icons.battlePass,
  je = {
    [$.LIMIT]: {
      title: fe.limitPoints.title(),
      text: fe.limitPoints.text(),
      image: Ce.how_to_earn_points.limit(),
    },
    [$.DAILY]: {
      title: fe.daily.title(),
      text: fe.daily.text(),
      linkText: fe.daily.linkText(),
      image: Ce.how_to_earn_points.daily(),
    },
  },
  Ee = {
    base: "Card_8b9276",
    description: "Card_description_60408b2f",
    text: "Card_text_c006a64b",
    image: "Card_image_c20b5a1",
    cardTitle: "Card_cardTitle_426a6860",
    linkButton: "Card_linkButton_e48299f6",
    fadeInWithScale: "Card_fadeInWithScale_f4c22d1c",
    slideUp: "Card_slideUp_f4c22d1c",
    blink: "Card_blink_f4c22d1c",
    scale: "Card_scale_f4c22d1c",
    rotate: "Card_rotate_f4c22d1c",
    windowIn: "Card_windowIn_f4c22d1c",
    fadeOut: "Card_fadeOut_f4c22d1c",
    fadeIn: "Card_fadeIn_f4c22d1c",
  },
  Ne = ({ card: e }) => {
    const { controls: a } = z(),
      t = je[e],
      n = O(
        { buttonSize: u.extraSmall },
        { large: { buttonSize: u.small }, extraLarge: { buttonSize: u.medium } },
      );
    return (0, ae.jsxs)("div", {
      className: Ee.base,
      children: [
        t?.image &&
          (0, ae.jsx)("div", {
            className: C(Ee.image, Ee[`image__${e}`]),
            style: { backgroundImage: `url(${t?.image})` },
          }),
        (0, ae.jsxs)("div", {
          className: Ee.description,
          children: [
            (0, ae.jsx)("div", { className: Ee.cardTitle, children: je[e].title }),
            (0, ae.jsx)("div", { className: Ee.text, children: t?.text }),
            "linkText" in t &&
              t?.linkText &&
              (0, ae.jsx)(k, {
                onClick: a.onGoToMissions,
                size: n.buttonSize,
                theme: l.secondary,
                className: Ee.linkButton,
                children: t?.linkText,
              }),
          ],
        }),
      ],
    });
  },
  Ie = "DefaultTab_63c3b559",
  ye = "DefaultTab_conditions__hasVehiclesTable_af1a115f",
  Ae = "DefaultTab_conditions_e2f32c0d",
  Le = "DefaultTab_vehicles_c9db3cba",
  Re = "DefaultTab_wotPlusBanner_74c26ec6",
  we = "DefaultTab_wotPlusBanner__hasVehicles_a5409707",
  Oe = "DefaultTab_title_1d604cc7",
  Pe = "DefaultTab_cards_c1bfc92c",
  Be = L.resolve("strings"),
  Se = "battle_pass.howToEarnPoints",
  ke = M(function () {
    const { model: e } = z(),
      { isWotPlusShown: a } = e.root.get(),
      { cards: t, conditions: n, vehicles: l } = e.computes.activeGameModeInfo(),
      s = l.length > 0,
      i = t.length > 0;
    return (0, ae.jsxs)("div", {
      className: Ie,
      children: [
        (0, ae.jsxs)("div", {
          className: C(Ae, s && ye),
          children: [
            (0, ae.jsx)("div", { className: Oe, children: Be.readOrEmpty(`${Se}.conditions`) }),
            (0, ae.jsx)(ce, { tableRows: n, tableType: Me.CONDITIONS, shouldEnableTruncate: s }),
            a && (0, ae.jsx)("div", { className: C(Re, s && we), children: (0, ae.jsx)(be, {}) }),
          ],
        }),
        s &&
          (0, ae.jsxs)("div", {
            className: Le,
            children: [
              (0, ae.jsx)("div", { className: Oe, children: Be.readOrEmpty(`${Se}.vehicles`) }),
              (0, ae.jsx)(ce, { tableRows: l, tableType: Me.VEHICLES, shouldEnableTruncate: !0 }),
            ],
          }),
        i &&
          (0, ae.jsx)("div", {
            className: Pe,
            children: _(t, (e, a) => (0, ae.jsx)(Ne, { card: e }, `card-${a}`)),
          }),
      ],
    });
  }),
  Me = { CONDITIONS: "conditions", VEHICLES: "vehicles", BATTLE_ROYAL: "battle_royal" },
  Fe = M(function () {
    const { model: e } = z(),
      { arenaBonusType: a } = e.computes.activeGameModeInfo();
    return a !== D.BATTLE_ROYALE_SOLO ? (0, ae.jsx)(ke, {}) : (0, ae.jsx)(ve, {});
  }),
  Ge = "App_28aad4f9",
  De = "App_animationMain_355bda5d",
  $e = "App_animationBg_1dccac61",
  We = "App_mainBg_4662d711",
  ze = "App_dimBg_e8187a2a",
  Ye = "App_content_ffc5f1c8",
  Ue = "App_close_fbc86043",
  He = "App_titleContainer_ef2e4d7b",
  qe = "App_title_b6b0162",
  Ve = "App_description_79d7b229",
  Ke = "App_tabs_b46e68d",
  Ze = "App_tabBase_8445bc2d",
  Je = "App_tabBase__active_c7ebc4ed",
  Qe = "App_tabBorderImage_abbc895d",
  Xe = "App_tabBorderImage__active_f5aee4bf",
  ea = "App_tabBorderImage__hover_bd175ff0",
  aa = "App_tabBackground_3445b93d",
  ta = "App_tabBackground__active_8643ea94",
  na = "App_tabBackground__hover_498f3901",
  la = "App_tabContent_a32e480",
  sa = "App_contentTab_22347cf",
  ia = L.resolve("strings"),
  oa = "battle_pass.howToEarnPoints",
  ca = M(function () {
    const e = (0, G.useRef)(!1),
      [a, t] = (0, G.useState)(null),
      { model: l, controls: i } = z(),
      d = l.computes.getItems(),
      r = l.selectedGameMode.get(),
      b = l.computes.activeIndex();
    return (
      o(),
      (0, G.useEffect)(() => {
        const a = (a) => {
          (a.code !== c.ARROW_LEFT && a.code !== c.ARROW_RIGHT) || (e.current = !1);
        };
        return (window.addEventListener("keyup", a), () => window.removeEventListener("keyup", a));
      }, []),
      m(c.ARROW_LEFT, () => {
        e.current ||
          ((e.current = !0), 0 !== b && i.setSelectedGameMode(n(d, b - 1)?.arenaBonusType || 1));
      }),
      m(c.ARROW_RIGHT, () => {
        e.current ||
          ((e.current = !0),
          b !== d.length - 1 && i.setSelectedGameMode(n(d, b + 1)?.arenaBonusType || 1));
      }),
      (0, ae.jsxs)("div", {
        className: Ge,
        children: [
          (0, ae.jsx)("div", { className: $e }),
          (0, ae.jsxs)("div", {
            className: De,
            children: [
              (0, ae.jsx)("div", {
                className: We,
                children: (0, ae.jsx)("div", { className: ze }),
              }),
              (0, ae.jsx)(v, { className: Ue, onClose: h.close }),
              (0, ae.jsxs)("div", {
                className: Ye,
                children: [
                  (0, ae.jsxs)("div", {
                    className: He,
                    children: [
                      (0, ae.jsx)("div", {
                        className: qe,
                        children: ia.readOrEmpty(`${oa}.title`),
                      }),
                      (0, ae.jsx)("div", {
                        className: Ve,
                        children: (0, ae.jsx)(E, { text: ia.readOrEmpty(`${oa}.description`) }),
                      }),
                    ],
                  }),
                  (0, ae.jsxs)(P, {
                    size: s.large,
                    theme: x.custom,
                    active: r,
                    onActiveChange: i.setSelectedGameMode,
                    children: [
                      (0, ae.jsx)("div", {
                        className: Ke,
                        children: _(d, (e) => {
                          const n = r === e.arenaBonusType,
                            l = a === e.arenaBonusType && !n,
                            s = {
                              base: C(Ze, n && Je),
                              background: C(aa, n && ta, l && na),
                              borderImage: C(Qe, n && Xe, l && ea),
                              content: la,
                            };
                          return (0, ae.jsx)(
                            P.Tab,
                            {
                              tabId: e.arenaBonusType,
                              classNames: s,
                              onMouseEnter: () => t(e.arenaBonusType),
                              onMouseLeave: () => t(null),
                              children: (0, ae.jsx)(le, {
                                gameMode: e,
                                isActive: r === e.arenaBonusType,
                              }),
                            },
                            e.arenaBonusType,
                          );
                        }),
                      }),
                      (0, ae.jsx)(P.Content, {
                        children: () =>
                          (0, ae.jsx)("div", { className: sa, children: (0, ae.jsx)(Fe, {}) }),
                      }),
                    ],
                  }),
                ],
              }),
            ],
          }),
        ],
      })
    );
  });
N(
  new w()
    .add(B)
    .addWithProps(W, {})
    .render((0, ae.jsx)(ca, {})),
);
