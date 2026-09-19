import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Ur as e,
  Xn as t,
  _n as a,
  ci as n,
  fn as o,
  gn as c,
  n as i,
  pn as l,
  tn as r,
  ui as d,
} from "../../chunks/lib.js";
import "../../chunks/global.js";
import { h as m } from "../../chunks/vendor.js";
import { t as _ } from "../../chunks/icon_text_block.js";
d();
var x = (function (s) {
    return ((s.COMMON = "common"), (s.EXTRA = "extra"), (s.HOLIDAY = "holiday"), s);
  })({}),
  [p, u] = a()(({ observableModel: s }) => {
    const e = { root: s.object() },
      t = c(() => e.root.get().chapterType === x.HOLIDAY);
    return { ...e, computes: { isHoliday: t } };
  }, e),
  j = "Message_3327d7a0",
  h = "Message_separator_8e93a926",
  b = "Message_content_6bca034f",
  g = "Message_text_7eae674d",
  C = t(),
  v = ({ text: s }) =>
    (0, C.jsxs)("div", {
      className: j,
      children: [
        (0, C.jsx)("div", { className: h }),
        (0, C.jsx)("div", {
          className: b,
          children: (0, C.jsx)("div", { className: g, children: s }),
        }),
        (0, C.jsx)("div", { className: h }),
      ],
    }),
  N = "CustomContent_background_64384741",
  k = "CustomContent_tank_61704151",
  f = "CustomContent_footer_2bfe8c75",
  P = "CustomContent_messageWrapper_8c5889c7",
  w = "CustomContent_textWrapper_69b29c66",
  M = "CustomContent_check_67de302c",
  T = "CustomContent_text_edf6432",
  y = R.strings.battle_pass.tooltips,
  O = m(() => {
    const { model: s } = u(),
      { isBattlePassPurchased: e } = s.root.get();
    return (0, C.jsxs)(C.Fragment, {
      children: [
        (0, C.jsx)("div", { className: N }),
        (0, C.jsx)("div", { className: k }),
        (0, C.jsx)("div", {
          className: f,
          children: (0, C.jsx)("div", {
            className: P,
            children: (0, C.jsx)(v, {
              text: (0, C.jsxs)("div", {
                className: w,
                children: [
                  (0, C.jsx)("div", {
                    className: M,
                    style: {
                      backgroundImage: `url(${e ? R.images.gui.maps.icons.battlePass.tooltips.double_check() : R.images.gui.maps.icons.battlePass.tooltips.check()})`,
                    },
                  }),
                  (0, C.jsx)("div", {
                    className: T,
                    children: e ? y.completed.claimRewards() : y.completed.rewardsObtained(),
                  }),
                ],
              }),
            }),
          }),
        }),
      ],
    });
  }),
  A = "Content_d9cfcd3f",
  D = "Content_base__noDescription_b474774a",
  H = "Content_title_22d0441e",
  W = "Content_subTitle_7bb4259d",
  B = "Content_tank_dcd7ba89",
  I = "Content_footer_e0404414",
  F = "Content_flare_273bab95",
  L = "Content_messageWrapper_21d573e9",
  X = "Content_info_a37d477a",
  Y = "Content_unlock_8083471",
  E = R.strings.battle_pass.tooltips,
  S = m(() => {
    const { model: s } = u(),
      { isBattlePassPurchased: e, notChosenRewardCount: t, isAvailableTankmen: a } = s.root.get(),
      o = t > 0,
      c = s.computes.isHoliday();
    return (0, C.jsxs)("div", {
      className: n(A, e && !o && !a && D),
      children: [
        (0, C.jsx)("div", { className: H, children: E.completed.title() }),
        (0, C.jsx)("div", {
          className: W,
          children: c ? E.completed.oneChapterSubTitle() : E.completed.subTitle(),
        }),
        c
          ? (0, C.jsx)(O, {})
          : (0, C.jsxs)(C.Fragment, {
              children: [
                (0, C.jsx)("div", { className: B }),
                (0, C.jsxs)("div", {
                  className: I,
                  children: [
                    (0, C.jsx)("div", { className: F }),
                    (0, C.jsx)("div", {
                      className: L,
                      children: (0, C.jsx)(v, { text: E.completed.message() }),
                    }),
                  ],
                }),
              ],
            }),
        (0, C.jsxs)("div", {
          className: X,
          children: [
            o &&
              (0, C.jsx)(_, {
                icon: R.images.gui.maps.icons.battlePass.tooltips.bow_small(),
                text: t > 1 ? E.claimRewards.multiple() : E.claimRewards.c_1(),
                className: Y,
              }),
            !e &&
              (0, C.jsx)(_, {
                icon: R.images.gui.maps.icons.battlePass.progression.icon_lock_current_small(),
                text: E.unlockBattlePass(),
                className: Y,
              }),
            a &&
              (0, C.jsx)(_, {
                icon: R.images.gui.maps.icons.battlePass.icons.tankmen_small(),
                text: E.completed.tankmenNotRecieved(),
                className: n(Y),
              }),
          ],
        }),
      ],
    });
  }),
  U = () => (0, C.jsx)(i, { children: (0, C.jsx)(i.Decorator, { children: (0, C.jsx)(S, {}) }) });
o(
  new l()
    .add(r)
    .addWithProps(p, {})
    .render((0, C.jsx)(U, {})),
);
