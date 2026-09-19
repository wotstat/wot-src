import { r as e } from "./rolldown-runtime.js";
import {
  Br as a,
  Ct as s,
  Et as n,
  Hr as t,
  In as i,
  Or as l,
  Qr as _,
  Qt as o,
  R as c,
  Tt as r,
  Xn as d,
  _n as b,
  _t as m,
  bt as k,
  ci as u,
  gn as v,
  gt as p,
  pi as h,
  pt as f,
  qn as S,
  ui as w,
  wr as g,
  wt as I,
  yt as N,
} from "./lib.js";
import "./global.js";
import { h as x } from "./vendor.js";
import { n as j, t as P } from "./constants.js";
var T = e(w(), 1),
  V = e(o(), 1),
  y = {
    root: "/hangar",
    battlePass: {
      chapterChoice: "/battlePass/chapterChoice",
      progression: "/battlePass/progression",
      postProgression: "/battlePass/postProgression",
      intro: "/battlePass/intro",
      buyPass: "/battlePass/buyPass",
      buyPassRewards: "/battlePass/buyPassRewards",
      buyLevels: "/battlePass/buyLevels",
      buyLevelsRewards: "/battlePass/buyLevelsRewards",
      holidayFinal: "/battlePass/holidayFinal",
      tankmenScreen: "/battlePass/tankmenScreen",
    },
  },
  [O, C] = b()(
    ({ observableModel: e }) => {
      const s = { tankmenList: e.array("tankmen") };
      return { computes: { getTankmenList: v(() => l(s.tankmenList.get(), t), { equals: a }) } };
    },
    ({ externalModel: e }) => ({
      showShop: e.createCallback((e) => ({ tankmanGroupName: e }), "showShop"),
    }),
  ),
  L = (function (e) {
    return (
      (e.RECEIVED = "received"),
      (e.PROGRESSION = "progression"),
      (e.IN_SHOP = "inShop"),
      (e.NOT_FULL = "notFull"),
      (e.UNAVAILABLE = "unavailable"),
      e
    );
  })({}),
  D = {
    base: "Details_f71cbec7",
    base__received: "Details_base__received_cc86090a",
    button: "Details_button_7162adb1",
    label: "Details_label_53b1bce8",
    label__received: "Details_label__received_672e99c5",
    fadeInWithScale: "Details_fadeInWithScale_43c92208",
    slideUp: "Details_slideUp_43c92208",
    blink: "Details_blink_43c92208",
    scale: "Details_scale_43c92208",
    rotate: "Details_rotate_43c92208",
    windowIn: "Details_windowIn_43c92208",
    fadeOut: "Details_fadeOut_43c92208",
    fadeIn: "Details_fadeIn_43c92208",
  },
  E = d(),
  $ = h.resolve("strings"),
  U = x(({ tankman: e, className: a }) => {
    const { controls: t } = C(),
      {
        state: i,
        progressionLevel: l,
        count: _,
        availableCount: o,
        groupName: c,
        chapterID: d,
      } = e,
      b = s(),
      m = S({ buttonSize: r.extraSmall }, { large: { buttonSize: r.small } }),
      v = $.readOrEmpty(`battle_pass.tankmenVoiceover.${i}`),
      p = u(D.label, D[`label__${i}`]),
      h = (() => {
        switch (i) {
          case L.PROGRESSION:
            return (0, E.jsx)(k, { classMix: p, text: v, binding: { progressionLevel: l } });
          case L.NOT_FULL:
            return (0, E.jsx)(k, {
              classMix: p,
              text: v,
              binding: { availableCount: o, count: _ },
            });
          default:
            return (0, E.jsx)("span", { className: p, children: v });
        }
      })(),
      f = (() => {
        switch (i) {
          case L.PROGRESSION:
            return {
              label: $.readOrEmpty("battle_pass.tankmenVoiceover.chapterButton"),
              handler: () => b.push(y.battlePass.progression, { chapterID: d }),
            };
          case L.IN_SHOP:
          case L.NOT_FULL:
            return {
              label: $.readOrEmpty("battle_pass.tankmenVoiceover.shopButton"),
              handler: () => t.showShop(c),
            };
          default:
            return null;
        }
      })();
    return (0, E.jsxs)("div", {
      className: u(D.base, D[`base__${i}`], a),
      children: [
        h,
        f &&
          (0, E.jsx)(I, {
            onClick: f.handler,
            className: D.button,
            theme: n.secondary,
            size: m.buttonSize,
            children: f.label,
          }),
      ],
    });
  }),
  W = {
    base: "Skills_12e25c21",
    skill: "Skills_skill_8dd2237b",
    skill__specificPerk: "Skills_skill__specificPerk_9fedba",
    tooltip: "Skills_tooltip_313e3831",
    zeroIcon: "Skills_zeroIcon_907fac9b",
    icon: "Skills_icon_f9b466d4",
    icon__new_skill: "Skills_icon__new_skill_dfb9653d",
    divider: "Skills_divider_693bc0a8",
    fadeInWithScale: "Skills_fadeInWithScale_2c9d324a",
    slideUp: "Skills_slideUp_2c9d324a",
    blink: "Skills_blink_2c9d324a",
    scale: "Skills_scale_2c9d324a",
    rotate: "Skills_rotate_2c9d324a",
    windowIn: "Skills_windowIn_2c9d324a",
    fadeOut: "Skills_fadeOut_2c9d324a",
    fadeIn: "Skills_fadeIn_2c9d324a",
  },
  z = h.resolve("images"),
  A = ({ skills: e, className: a }) => {
    const s = g(e, (e) => e.isZero);
    return (0, E.jsx)("div", {
      className: u(W.base, a),
      children: l(e, (e, a) => {
        const { name: n, isZero: t } = e,
          i = n !== P,
          l = a === s && !i;
        return (0, E.jsxs)(
          T.Fragment,
          {
            children: [
              (0, E.jsx)(c, {
                contentId: R.views.mono.battle_pass.tooltips.crew_member_skill("resId"),
                args: { name: n, isZero: t, hasZeroPerk: void 0 !== s },
                children: (0, E.jsxs)("div", {
                  className: u(W.skill, i && W.skill__specificPerk),
                  children: [
                    t && !i && (0, E.jsx)("div", { className: W.zeroIcon }),
                    (0, E.jsx)("div", {
                      className: u(W.icon, W[`icon__${n}`]),
                      style: {
                        backgroundImage: `url(${z.readOrEmpty(`battlePass.tankman.new_perks.icon_perk_${n}`)})`,
                      },
                    }),
                  ],
                }),
              }),
              l && (0, E.jsx)("div", { className: W.divider }),
            ],
          },
          `${e.name}_${a}`,
        );
      }),
    });
  },
  B = {
    base: "Voice_cd68eca5",
    icon: "Voice_icon_a4c0c739",
    icon__speaker: "Voice_icon__speaker_96c5b33",
    icon__wave0: "Voice_icon__wave0_86731afb",
    base__animate: "Voice_base__animate_d1a20ef1",
    wave0: "Voice_wave0_d1a20ef1",
    icon__wave1: "Voice_icon__wave1_a21172b8",
    wave1: "Voice_wave1_d1a20ef1",
    icon__wave2: "Voice_icon__wave2_8dd59152",
    wave2: "Voice_wave2_d1a20ef1",
    label: "Voice_label_5b3d7cf5",
    base__hover: "Voice_base__hover_d1a20ef1",
    fadeInWithScale: "Voice_fadeInWithScale_d1a20ef1",
    slideUp: "Voice_slideUp_d1a20ef1",
    blink: "Voice_blink_d1a20ef1",
    scale: "Voice_scale_d1a20ef1",
    rotate: "Voice_rotate_d1a20ef1",
    windowIn: "Voice_windowIn_d1a20ef1",
    fadeOut: "Voice_fadeOut_d1a20ef1",
    fadeIn: "Voice_fadeIn_d1a20ef1",
  },
  F = h.resolve("strings"),
  H = (() => {
    const e = Math.ceil(j / 800);
    return { duration: 800, iterationCount: e, totalDuration: 800 * e };
  })(),
  M = ({ isHovered: e, isPlayingSound: a, className: s }) =>
    (0, E.jsxs)("div", {
      className: u(B.base, e && B.base__hover, a && B.base__animate, s),
      style: {
        "--animation-duration": `${H.duration}ms`,
        "--animation-iteration-count": H.iterationCount,
      },
      children: [
        (0, E.jsx)("div", { className: u(B.icon, B.icon__speaker) }),
        Array.from({ length: 3 }, (e, a) =>
          (0, E.jsx)("div", { className: u(B.icon, B[`icon__wave${a}`]) }, `wave${a}`),
        ),
        (0, E.jsx)("div", {
          className: B.label,
          children: F.readOrEmpty("battle_pass.tankmenVoiceover.listen"),
        }),
      ],
    }),
  G = {
    base: "Tankman_90661404",
    base__hover: "Tankman_base__hover_ca952550",
    base__active: "Tankman_base__active_9fe4dd8e",
    base__disabled: "Tankman_base__disabled_9be07c52",
    interactiveContainer: "Tankman_interactiveContainer_8be6d5d0",
    base__muted: "Tankman_base__muted_ca952550",
    image: "Tankman_image_2e7bae1e",
    content: "Tankman_content_a12559ff",
    voice: "Tankman_voice_a253f649",
    skills: "Tankman_skills_771bfa6a",
    name: "Tankman_name_eb347b56",
    fadeInWithScale: "Tankman_fadeInWithScale_ca952550",
    slideUp: "Tankman_slideUp_ca952550",
    blink: "Tankman_blink_ca952550",
    scale: "Tankman_scale_ca952550",
    rotate: "Tankman_rotate_ca952550",
    windowIn: "Tankman_windowIn_ca952550",
    fadeOut: "Tankman_fadeOut_ca952550",
    fadeIn: "Tankman_fadeIn_ca952550",
  },
  Z = h.resolve("images"),
  q = ({ tankman: e, activeTankman: a, setActiveTankman: s }) => {
    const { groupName: n, fullName: t, hasVoiceover: i, skills: l } = e,
      o = Boolean(a) && a !== n,
      [c, r] = (0, T.useState)(!1),
      [d, b] = (0, T.useState)(!1),
      [m, k] = (0, T.useState)(!1);
    return (
      (0, T.useEffect)(() => {
        d && !o && i && (r(!0), _.sound(R.sounds.bp_highlight()));
      }, [o, d, i]),
      (0, E.jsxs)("div", {
        className: u(
          G.base,
          o && G.base__disabled,
          m && G.base__active,
          c && G.base__hover,
          !i && G.base__muted,
        ),
        children: [
          (0, E.jsx)("div", {
            className: G.interactiveContainer,
            onClick: () => {
              m ||
                o ||
                !i ||
                (s(n),
                k(!0),
                _.sound(R.sounds.play()),
                _.sound(n),
                setTimeout(() => {
                  (k(!1), s(""));
                }, j));
            },
            onMouseEnter: () => {
              !o && i ? (r(!0), _.sound(R.sounds.bp_highlight())) : b(!0);
            },
            onMouseLeave: () => {
              (r(!1), b(!1));
            },
            children: i && (0, E.jsx)(M, { className: G.voice, isHovered: c, isPlayingSound: m }),
          }),
          (0, E.jsx)("div", {
            className: G.image,
            style: {
              backgroundImage: `url(${Z.readOrEmpty(`battlePass.tankman.persons.commander_${n}`)})`,
            },
          }),
          (0, E.jsxs)("div", {
            className: G.content,
            children: [
              l.length > 0 && (0, E.jsx)(A, { className: G.skills, skills: l }),
              (0, E.jsx)("span", { className: G.name, children: t }),
              (0, E.jsx)(U, { className: G.details, tankman: e }),
            ],
          }),
        ],
      })
    );
  },
  Q = "Content_bd627888",
  X = "Content_scrollWrapper_722ae7d9",
  J = "Content_scrollWrapper__hasScroll_24bcd139",
  K = "Content_scrollContent_bc619017",
  Y = "Content_scrollBar_66a66791",
  ee = x(({ className: e }) => {
    const {
        model: { computes: a },
      } = C(),
      s = a.getTankmenList(),
      [n, t] = (0, T.useState)(""),
      { api: i } = N(),
      [l, _] = (0, T.useState)(!1),
      o = (0, T.useCallback)(() => {
        const [e, a] = i.getBounds();
        _(e !== a);
      }, [i]);
    return (
      (0, T.useEffect)(
        () => (
          i.events.on("resizeHandled", o),
          () => {
            i.events.off("resizeHandled", o);
          }
        ),
        [i.events, o],
      ),
      (0, E.jsxs)("div", {
        className: (0, V.default)(Q, e),
        children: [
          (0, E.jsx)(p, {
            classNames: { wrapper: (0, V.default)(X, l && J), content: K },
            children: s.map((e, a) =>
              (0, E.jsx)(q, { tankman: e, activeTankman: n, setActiveTankman: t }, `tankman-${a}`),
            ),
          }),
          (0, E.jsx)(m, { classNames: { base: Y } }),
        ],
      })
    );
  }),
  ae = "App_7603ab20",
  se = "App_content_927ebd71",
  ne = () => (
    i(s().goBack),
    (0, E.jsx)("div", {
      className: ae,
      children: (0, E.jsx)(f, { children: (0, E.jsx)(ee, { className: se }) }),
    })
  ),
  te = () =>
    (0, E.jsx)(O, {
      options: { rootId: R.aliases.battle_pass.TankmenScreen("resId") },
      children: (0, E.jsx)(ne, {}),
    });
export { y as n, te as t };
