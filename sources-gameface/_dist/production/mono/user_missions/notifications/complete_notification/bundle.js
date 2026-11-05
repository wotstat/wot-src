import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  En as e,
  H as a,
  L as l,
  St as c,
  U as n,
  V as o,
  _t as r,
  cn as i,
  ct as t,
  ln as p,
  nt as m,
  qt as d,
  rt as _,
  vt as b,
  yt as h,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as g } from "../../chunks/rewards.js";
var [u, j] = c()(
    ({ observableModel: s }) => ({ root: s.object(), bonuses: s.array("rewards") }),
    ({ externalModel: s }) => ({ openChallenge: s.createCallbackNoArgs("onClick") }),
  ),
  x = "App_image_95a6abe1",
  N = "App_9e9b93b",
  f = "App_base__popup_a2438b5f",
  A = "App_wrapper_ffdbb6e9",
  v = "App_acceptIconContainer_ce6da395",
  k = "App_acceptIcon_d6166213",
  y = "App_description_3d77568a",
  C = "App_title_b04670be",
  w = "App_rewards_573bd253",
  M = "App_button_cec9cac4",
  I = "App_close_654073f5",
  L = s(d(), 1),
  z = R.strings.user_missions.hub.challenge_missions.notification.challenge_complete,
  U = r(function () {
    const { model: s, controls: c } = j(),
      { challengeName: r, anyMissionsLeft: d, isPopUp: b } = s.root.get(),
      h = s.bonuses.get(),
      u = i(h);
    return (0, L.jsxs)(l, {
      className: e(N, b && f),
      children: [
        (0, L.jsxs)("div", {
          className: A,
          children: [
            (0, L.jsx)("div", {
              className: x,
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.userMissions.hub.challenge.challenge_complete()})`,
              },
            }),
            (0, L.jsxs)("div", {
              className: y,
              children: [
                (0, L.jsx)(t, {
                  params: { challengeName: r },
                  text: z.title(),
                  className: C,
                  upgradeLegacy: !0,
                }),
                (0, L.jsx)("div", { className: v, children: (0, L.jsx)("div", { className: k }) }),
              ],
            }),
            (0, L.jsx)("div", { className: w, children: (0, L.jsx)(g, { bonuses: u }) }),
            (0, L.jsx)(o, {
              className: M,
              size: a.small,
              onClick: c.openChallenge,
              theme: d ? n.primary : n.secondary,
              children: d ? z.button() : z.affirmative(),
            }),
          ],
        }),
        b && (0, L.jsx)(m, { size: _.small, onClose: p, className: I }),
      ],
    });
  });
h((0, L.jsx)(u, { children: (0, L.jsx)(b, { children: (0, L.jsx)(U, {}) }) }));
