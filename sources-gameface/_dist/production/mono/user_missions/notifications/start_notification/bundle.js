import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Dn as e,
  H as a,
  Jt as l,
  L as t,
  St as n,
  U as i,
  V as o,
  at as c,
  dt as r,
  it as p,
  un as m,
  ut as b,
  vt as _,
  yt as d,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ var [h, u] = n()(
    ({ observableModel: s }) => ({ root: s.object() }),
    ({ externalModel: s }) => ({ openChallenge: s.createCallbackNoArgs("onClick") }),
  ),
  g = "App_image_95a6abe1",
  x = "App_9e9b93b",
  j = "App_base__popup_a2438b5f",
  f = "App_wrapper_ffdbb6e9",
  A = "App_description_bb08788d",
  N = "App_title_cd1a36ec",
  k = "App_text_b138bc7f",
  C = "App_button_cec9cac4",
  v = "App_close_654073f5",
  w = s(l(), 1),
  y = R.strings.user_missions.hub.challenge_missions.notification.start,
  M = _(function () {
    const { model: s, controls: l } = u(),
      { first: n, isPopUp: r } = s.root.get(),
      _ = n,
      d = _ ? y.title() : y.newChallengesTitle(),
      h = _ ? y.text() : y.newChallengesText();
    return (0, w.jsxs)(t, {
      className: e(x, r && j),
      children: [
        (0, w.jsxs)("div", {
          className: f,
          children: [
            (0, w.jsx)("div", {
              className: g,
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.userMissions.hub.challenge.started_challenge()})`,
              },
            }),
            (0, w.jsxs)("div", {
              className: A,
              children: [
                (0, w.jsx)(b, { text: d, className: N }),
                (0, w.jsx)(b, { text: h, className: k }),
              ],
            }),
            (0, w.jsx)(o, {
              className: C,
              size: a.small,
              onClick: l.openChallenge,
              theme: i.primary,
              children: y.button(),
            }),
          ],
        }),
        r && (0, w.jsx)(p, { size: c.small, onClose: m, className: v }),
      ],
    });
  });
d((0, w.jsx)(h, { children: (0, w.jsx)(r, { children: (0, w.jsx)(M, {}) }) }));
