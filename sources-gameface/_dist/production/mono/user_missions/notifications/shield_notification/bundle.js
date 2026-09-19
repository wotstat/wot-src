import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Dn as e,
  H as a,
  Jt as l,
  L as t,
  St as i,
  U as n,
  V as o,
  at as c,
  dt as p,
  it as r,
  un as m,
  ut as d,
  vt as _,
  yt as h,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ var [u, g] = i()(
    ({ observableModel: s }) => ({ root: s.object() }),
    ({ externalModel: s }) => ({ openChallenge: s.createCallbackNoArgs("onClick") }),
  ),
  b = "App_image_95a6abe1",
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
  L = s(l(), 1),
  M = R.strings.user_missions.hub.challenge_missions.notification.shield,
  z = _(function () {
    const { model: s, controls: l } = g(),
      { attempts: i, missionID: p, isPopUp: _ } = s.root.get();
    return (0, L.jsxs)(t, {
      className: e(j, _ && x),
      children: [
        (0, L.jsxs)("div", {
          className: A,
          children: [
            (0, L.jsx)("div", {
              className: b,
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.userMissions.hub.challenge.shield_challenge()})`,
              },
            }),
            (0, L.jsxs)("div", {
              className: N,
              children: [
                (0, L.jsxs)("div", {
                  className: k,
                  children: [i, (0, L.jsx)("span", { className: v })],
                }),
                (0, L.jsx)(d, { text: M.title(), className: f, upgradeLegacy: !0 }),
                (0, L.jsx)(d, {
                  params: { mission: p },
                  text: M.text(),
                  className: y,
                  upgradeLegacy: !0,
                }),
              ],
            }),
            (0, L.jsx)(o, {
              className: C,
              size: a.small,
              onClick: l.openChallenge,
              theme: n.secondary,
              children: M.button(),
            }),
          ],
        }),
        _ && (0, L.jsx)(r, { size: c.small, onClose: m, className: w }),
      ],
    });
  });
h((0, L.jsx)(u, { children: (0, L.jsx)(p, { children: (0, L.jsx)(z, {}) }) }));
