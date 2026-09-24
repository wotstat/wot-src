import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $t as a,
  Br as t,
  Cr as n,
  Er as l,
  Ft as s,
  Gt as i,
  Jt as o,
  Kt as c,
  Ln as _,
  Lr as d,
  Or as r,
  Qn as m,
  Rn as b,
  Sr as p,
  Tt as u,
  Ut as T,
  Wt as g,
  Xn as x,
  Yn as h,
  Yt as v,
  Zr as f,
  Zt as C,
  _n as j,
  ci as E,
  dr as N,
  en as I,
  fn as y,
  gn as A,
  gr as L,
  ir as w,
  pi as O,
  pn as P,
  qn as B,
  tn as S,
  ui as k,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as M } from "../chunks/vendor.js";
import { t as F } from "../chunks/tank_name.js";
var G = e(k(), 1),
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
  [W, z] = j()(
    ({ observableModel: e }) => {
      const a = {
          root: e.object(),
          gameModes: e.array("gameModes"),
          selectedGameMode: L.box(D.REGULAR),
        },
        l = A(() => a.gameModes.get(), { equals: t }),
        s = A(() => n(l(), (e) => e.arenaBonusType === a.selectedGameMode.get()) || 0, {
          equals: t,
        }),
        i = A(() => p(l(), (e) => e.arenaBonusType === a.selectedGameMode.get()), { equals: t }),
        o = A((e) => p(l(), (a) => e === a.arenaBonusType), { equals: t });
      return {
        ...a,
        computes: { getItems: l, getSlide: o, activeIndex: s, activeGameModeInfo: i },
      };
    },
    ({ externalModel: e, model: a }) => {
      const t = N((e) => {
        a.selectedGameMode.set(e);
      });
      return {
        openWotPlus: e.createCallbackNoArgs("onWotPlusClick"),
        onGoToMissions: e.createCallbackNoArgs("onGoToMissions"),
        setSelectedGameMode: t,
      };
    },
  ),
  U = R.images.gui.maps.icons,
  Y = U.battleTypes.c_136x136,
  H = U.battleTypes.c_136x136,
  q = {
    [D.REGULAR]: { small: Y.random(), large: H.random() },
    [D.BATTLE_ROYALE_SOLO]: { small: Y.battle_royale(), large: H.battle_royale() },
    [D.EPIC_BATTLE]: { small: Y.epicbattle(), large: H.epicbattle() },
    [D.COMP7]: { small: Y.comp7(), large: H.comp7() },
    [D.COMP7_LIGHT]: { small: Y.comp7Light(), large: H.comp7Light() },
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
  ae = x(),
  te = O.resolve("strings"),
  ne = "battle_pass.howToEarnPoints",
  le = function ({ gameMode: e, isActive: a }) {
    const t = e.arenaBonusType,
      { breakpoint: n } = h(),
      l = n.weight >= m.medium.weight,
      { large: s, small: i } = q[t],
      c = V[t]?.levelRange ?? [],
      _ =
        2 === c.length
          ? { startLevel: w(c[0]), endLevel: w(c[1]) }
          : { level: void 0 !== c[0] ? w(c[0]) : void 0 };
    return (0, ae.jsxs)("div", {
      className: E(K, a && J),
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
              children: (0, ae.jsx)(o, {
                text: te.readOrEmpty(`${ne}.text.c_${t}`),
                upgradeLegacy: !0,
                params: _,
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
      _ = B({ vehicleTypeIconSize: u.x48x48 }, { extraLarge: { vehicleTypeIconSize: u.x64x64 } });
    if (c)
      return n !== Me.VEHICLES || o
        ? t
        : (0, ae.jsxs)(ae.Fragment, {
            children: [
              (0, ae.jsx)("div", {
                className: E(se.nationFlag, se[`nationFlag__${l.vehicleNation}`]),
              }),
              (0, ae.jsx)(F, {
                ...l,
                vehicleTypeIconSize: _.vehicleTypeIconSize,
                classNames: { level: se.level, name: se.name },
                isShortName: !0,
              }),
            ],
          });
    const d =
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
      className: E(se.base, se[`base__${n}`]),
      children: [
        s && (0, ae.jsx)("div", { className: se.points, children: e }),
        d,
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
    const n = B({ isSmallScreen: !0 }, { medium: { isSmallScreen: !1 } }),
      s = l(e, 0)?.cell;
    if (!s) return null;
    const i = r(s, (a, t) => r(e, (e) => e.cell?.[t])),
      o = R.strings.settings.LANGUAGE_CODE();
    return (0, ae.jsx)("div", {
      className: E(oe.base, oe[`base__${a}`]),
      children: r(i, (e, l) =>
        (0, ae.jsx)(
          "div",
          {
            className: oe.column,
            children: r(e, (s, i) => {
              if (!s) return null;
              const { text: c, points: _, externalPoints: d, vehicleInfo: r } = s.value,
                m = Boolean(c),
                b = m && 0 === _ && 0 === d,
                p = t && n.isSmallScreen && b,
                u = 0 === i,
                g = i === e.length - 1,
                x = E(
                  oe.cell,
                  m && oe.cell__text,
                  u ? oe.cell__inFirstRow : oe.cell__content,
                  oe[`cell__column_${l}`],
                  p && oe.cell__truncated,
                );
              return (0, ae.jsxs)(
                G.Fragment,
                {
                  children: [
                    p
                      ? (0, ae.jsx)(T, {
                          text: c,
                          className: x,
                          tooltipParams: { body: c },
                          lang: o,
                        })
                      : (0, ae.jsx)("div", {
                          className: x,
                          lang: o,
                          children: (0, ae.jsx)(ie, {
                            points: _,
                            externalPoints: d,
                            text: c,
                            tableType: a,
                            vehicleInfo: r,
                          }),
                        }),
                    !g && (0, ae.jsx)("div", { className: oe.rowDivider }),
                  ],
                },
                `cell_${i}_${a}`,
              );
            }),
          },
          `column_${l}_${a}`,
        ),
      ),
    });
  },
  _e = "WotPlusBanner_4f7164a3",
  de = "WotPlusBanner_text_35aa0162",
  re = "WotPlusBanner_link_2fb44a00",
  me = O.resolve("strings"),
  be = M(() => {
    const { controls: e } = z(),
      a = me.readOrEmpty("battle_pass.howToEarnPoints.plusBanner.link"),
      t = B({ imageSize: 52 }, { large: { imageSize: 64 } });
    return (0, ae.jsxs)("div", {
      className: _e,
      children: [
        (0, ae.jsx)(s, {
          path: "battlePass.how_to_earn_points.plus_logo",
          width: t.imageSize,
          height: t.imageSize,
        }),
        (0, ae.jsxs)("div", {
          className: de,
          children: [
            (0, ae.jsx)(o, {
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
  he = O.resolve("strings"),
  ve = M(function () {
    const { model: e } = z(),
      { isWotPlusShown: a } = e.root.get(),
      { battleRoyaleCondtions: t } = e.computes.activeGameModeInfo();
    return (0, ae.jsxs)("div", {
      className: E(ue, Te),
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
    const { controls: t } = z(),
      n = je[e],
      l = B(
        { buttonSize: a.extraSmall },
        { large: { buttonSize: a.small }, extraLarge: { buttonSize: a.medium } },
      );
    return (0, ae.jsxs)("div", {
      className: Ee.base,
      children: [
        n?.image &&
          (0, ae.jsx)("div", {
            className: E(Ee.image, Ee[`image__${e}`]),
            style: { backgroundImage: `url(${n?.image})` },
          }),
        (0, ae.jsxs)("div", {
          className: Ee.description,
          children: [
            (0, ae.jsx)("div", { className: Ee.cardTitle, children: je[e].title }),
            (0, ae.jsx)("div", { className: Ee.text, children: n?.text }),
            "linkText" in n &&
              n?.linkText &&
              (0, ae.jsx)(C, {
                onClick: t.onGoToMissions,
                size: l.buttonSize,
                theme: I.secondary,
                className: Ee.linkButton,
                children: n?.linkText,
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
  Be = O.resolve("strings"),
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
          className: E(Ae, s && ye),
          children: [
            (0, ae.jsx)("div", { className: Oe, children: Be.readOrEmpty(`${Se}.conditions`) }),
            (0, ae.jsx)(ce, { tableRows: n, tableType: Me.CONDITIONS, shouldEnableTruncate: s }),
            a && (0, ae.jsx)("div", { className: E(Re, s && we), children: (0, ae.jsx)(be, {}) }),
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
            children: r(t, (e, a) => (0, ae.jsx)(Ne, { card: e }, `card-${a}`)),
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
  Ue = "App_content_ffc5f1c8",
  Ye = "App_close_fbc86043",
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
  ia = O.resolve("strings"),
  oa = "battle_pass.howToEarnPoints",
  ca = M(function () {
    const e = (0, G.useRef)(!1),
      [a, t] = (0, G.useState)(null),
      { model: n, controls: s } = z(),
      m = n.computes.getItems(),
      p = n.selectedGameMode.get(),
      u = n.computes.activeIndex();
    return (
      _(),
      (0, G.useEffect)(() => {
        const a = (a) => {
          (a.code !== d.ARROW_LEFT && a.code !== d.ARROW_RIGHT) || (e.current = !1);
        };
        return (window.addEventListener("keyup", a), () => window.removeEventListener("keyup", a));
      }, []),
      b(d.ARROW_LEFT, () => {
        e.current ||
          ((e.current = !0), 0 !== u && s.setSelectedGameMode(l(m, u - 1)?.arenaBonusType || 1));
      }),
      b(d.ARROW_RIGHT, () => {
        e.current ||
          ((e.current = !0),
          u !== m.length - 1 && s.setSelectedGameMode(l(m, u + 1)?.arenaBonusType || 1));
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
              (0, ae.jsx)(v, { className: Ye, onClose: f.close }),
              (0, ae.jsxs)("div", {
                className: Ue,
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
                        children: (0, ae.jsx)(o, { text: ia.readOrEmpty(`${oa}.description`) }),
                      }),
                    ],
                  }),
                  (0, ae.jsxs)(g, {
                    size: i.large,
                    theme: c.custom,
                    active: p,
                    onActiveChange: s.setSelectedGameMode,
                    children: [
                      (0, ae.jsx)("div", {
                        className: Ke,
                        children: r(m, (e) => {
                          const n = p === e.arenaBonusType,
                            l = a === e.arenaBonusType && !n,
                            s = {
                              base: E(Ze, n && Je),
                              background: E(aa, n && ta, l && na),
                              borderImage: E(Qe, n && Xe, l && ea),
                              content: la,
                            };
                          return (0, ae.jsx)(
                            g.Tab,
                            {
                              tabId: e.arenaBonusType,
                              classNames: s,
                              onMouseEnter: () => t(e.arenaBonusType),
                              onMouseLeave: () => t(null),
                              children: (0, ae.jsx)(le, {
                                gameMode: e,
                                isActive: p === e.arenaBonusType,
                              }),
                            },
                            e.arenaBonusType,
                          );
                        }),
                      }),
                      (0, ae.jsx)(g.Content, {
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
y(
  new P()
    .add(S)
    .addWithProps(W, {})
    .render((0, ae.jsx)(ca, {})),
);
