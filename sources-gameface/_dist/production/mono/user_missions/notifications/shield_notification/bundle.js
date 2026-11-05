import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  En as e,
  H as a,
  L as l,
  St as t,
  U as i,
  V as n,
  _t as o,
  ct as c,
  ln as p,
  nt as r,
  qt as m,
  rt as d,
  vt as _,
  yt as h,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ var [g, b] = t()(
    ({ observableModel: s }) => ({ root: s.object() }),
    ({ externalModel: s }) => ({ openChallenge: s.createCallbackNoArgs("onClick") }),
  ),
  u = "App_image_95a6abe1",
  j = "App_32d4293d",
  x = "App_base__popup_a2438b5f",
  A = "App_wrapper_ffdbb6e9",
  N = "App_description_879346b9",
  f = "App_title_3185c7d",
  k = "App_attempts_271a108",
  v = "App_icon_dff333e0",
  y = "App_text_533ed64b",
  C = "App_button_55edc998",
  w = "App_close_654073f5",
  L = s(m(), 1),
  M = R.strings.user_missions.hub.challenge_missions.notification.shield,
  z = o(function () {
    const { model: s, controls: t } = b(),
      { attempts: o, missionID: m, isPopUp: _ } = s.root.get();
    return (0, L.jsxs)(l, {
      className: e(j, _ && x),
      children: [
        (0, L.jsxs)("div", {
          className: A,
          children: [
            (0, L.jsx)("div", {
              className: u,
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.userMissions.hub.challenge.shield_challenge()})`,
              },
            }),
            (0, L.jsxs)("div", {
              className: N,
              children: [
                (0, L.jsxs)("div", {
                  className: k,
                  children: [o, (0, L.jsx)("span", { className: v })],
                }),
                (0, L.jsx)(c, { text: M.title(), className: f, upgradeLegacy: !0 }),
                (0, L.jsx)(c, {
                  params: { mission: m },
                  text: M.text(),
                  className: y,
                  upgradeLegacy: !0,
                }),
              ],
            }),
            (0, L.jsx)(n, {
              className: C,
              size: a.small,
              onClick: t.openChallenge,
              theme: i.secondary,
              children: M.button(),
            }),
          ],
        }),
        _ && (0, L.jsx)(r, { size: d.small, onClose: p, className: w }),
      ],
    });
  });
h((0, L.jsx)(g, { children: (0, L.jsx)(_, { children: (0, L.jsx)(z, {}) }) }));
