import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $t as t,
  Ar as a,
  Br as s,
  C as r,
  Cn as n,
  Cr as o,
  Dn as c,
  Er as d,
  Gt as l,
  Hn as i,
  In as _,
  Jt as b,
  K as u,
  Kt as m,
  Lr as p,
  Or as f,
  Pr as g,
  Qn as C,
  Qr as w,
  Rn as h,
  Sr as v,
  Tn as y,
  Wt as x,
  Xn as k,
  Y as j,
  Yn as N,
  Yt as I,
  Zt as T,
  _n as B,
  ci as S,
  cr as E,
  ct as O,
  dr as G,
  dt as A,
  en as $,
  fn as W,
  ft as z,
  gn as M,
  gr as L,
  pi as D,
  pn as U,
  sr as P,
  st as q,
  ti as F,
  tn as H,
  ui as Y,
  ut as K,
  vt as Q,
  w as J,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as X } from "../chunks/vendor.js";
import { n as Z, t as V } from "../chunks/filename.js";
var ee = e(Y()),
  te = "state_limited",
  ae = "state_received",
  se = D.resolve("strings"),
  re = D.resolve("images");
function ne(e) {
  const t = e.match(/(?:_(?:t|tier))?(\d+)\b/);
  if (t && void 0 !== t[1]) return t && t[1] ? parseInt(t[1], 10) : null;
}
var oe = (function (e) {
  return (
    (e.None = "none"),
    (e.Trophy = "trophy"),
    (e.Deluxe = "deluxe"),
    (e.Modernized = "modernized_device"),
    (e.BattleBooster = "battleBooster"),
    e
  );
})({});
function ce(e) {
  return e.includes("delux")
    ? "deluxe"
    : e.includes("modernized")
      ? "modernized_device"
      : e.includes("trophy")
        ? "trophy"
        : e.toLowerCase().endsWith("battleBooster".toLowerCase())
          ? "battleBooster"
          : "none";
}
function de(e, t) {
  return t && "none" !== t ? t : e;
}
var le = (e, t = j.Small, a) => {
    if ("modernized_device" === a) {
      const a = ne(e);
      if (a) return re.readOrEmpty(`quests.bonuses.${t}.modernized_devices_t${a}_gift`, "silent");
    }
    return re.readOrEmpty(`quests.bonuses.${t}.${de(e, a)}_gift`, "silent");
  },
  ie = (e, t) => {
    const a = e.match(/^offer:([^:]+):/);
    return a
      ? void 0 === a[1]
        ? ""
        : se.readOrEmpty(`selectable_reward.tabs.items.${a[1]}`, "silent")
      : se.readOrEmpty(`selectable_reward.tabs.items.${de(e, t)}`, "silent");
  },
  _e = (e) => {
    const t = e.split("_")[1],
      a = t && se.readOrEmpty(`blueprints.nations.${t}`, "silent"),
      s = se.readOrEmpty(`artefacts.${e}.name`, "silent");
    return (
      a ||
      (s && "string" == typeof s ? F(s) : (console.error("title for reward is not provided"), null))
    );
  };
function be(e, t) {
  if ("modernized_device" === t) {
    const t = ne(e);
    if (t)
      return re.readOrEmpty(
        `selectableReward.reward.optDeviceType.modernized_devices_t${t}`,
        "silent",
      );
  }
  return re.readOrEmpty(`selectableReward.reward.optDeviceType.${t}`, "silent");
}
var ue = (e, t = "s180x135", a = "R.images.gui.maps.icons.selectableReward.reward") =>
  `${a}.${t}.${e}`;
var me = (function (e) {
    return ((e.None = "none"), (e.Accepting = "accepting"), e);
  })({}),
  [pe, fe] = B()(
    ({ observableModel: e }) => {
      const t = {
          root: e.object(),
          tabs: e.array("tabs"),
          rewards: e.array("rewards"),
          animationState: L.box("none"),
        },
        r = M(
          (e) => {
            const a = g(t.tabs.get(), e);
            return { ...a, optDeviceType: ce(a.type) };
          },
          { equals: s },
        ),
        n = M(
          (e) => {
            const a = g(t.rewards.get(), e);
            return { ...a, optDeviceType: ce(a.type) };
          },
          { equals: s },
        ),
        o = M(() => a(t.tabs.get(), (e, t) => e + t.limit, 0));
      return { ...t, computes: { tabByIndex: r, rewardByIndex: n, rewardsToClaimTotal: o } };
    },
    ({ externalModel: e, model: t }) => {
      const a = G((e) => t.animationState.set(e));
      return {
        close: e.createCallbackNoArgs("onCloseClick"),
        submit: e.createCallbackNoArgs("onOkClick"),
        reduceReward: e.createCallback((e) => ({ type: e }), "onRewardReduce"),
        addReward: e.createCallback((e) => ({ type: e }), "onRewardAdd"),
        openTab: e.createCallback((e) => ({ type: e }), "onTabClick"),
        setAnimationState: a,
      };
    },
  ),
  ge = {
    base: "Category_a031eac",
    title: "Category_title_372b86f3",
    base__completed: "Category_base__completed_b894c2f0",
    imageContainer: "Category_imageContainer_4669b2b4",
    image: "Category_image_16708176",
    base__accepting: "Category_base__accepting_b894c2f0",
    blink: "Category_blink_b894c2f0",
    check: "Category_check_d9fca567",
    counter: "Category_counter_53ffc003",
    fadeInWithScale: "Category_fadeInWithScale_b894c2f0",
    slideUp: "Category_slideUp_b894c2f0",
    scale: "Category_scale_b894c2f0",
    rotate: "Category_rotate_b894c2f0",
    windowIn: "Category_windowIn_b894c2f0",
    fadeOut: "Category_fadeOut_b894c2f0",
    fadeIn: "Category_fadeIn_b894c2f0",
  },
  Ce = k(),
  we = D.resolve("strings"),
  he = D.resolve("views").read((e) =>
    e.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
  ),
  ve = X(({ index: e, className: t, classNames: a }) => {
    const {
        breakpoint: { weight: s },
      } = N(),
      { model: r, controls: n } = fe(),
      o = r.animationState.get(),
      { optDeviceType: c, count: d, limit: l, type: i } = r.computes.tabByIndex(e),
      _ = d === l,
      m = r.root.get().selectedTab === i,
      p = we.readOrEmpty(`selectable_reward.tabs.items.${c}`, "silent"),
      f = s >= C.medium.weight ? j.Big : j.Small,
      g = y((0, ee.useMemo)(() => ({ contentId: he, args: { type: i } }), [i]));
    return (0, Ce.jsxs)("div", {
      className: S(ge.base, _ && ge.base__completed, !m && d && ge[`base__${o}`], t),
      onClick: () => {
        (w.sound("bp_click"), n.openTab(i));
      },
      onMouseEnter: () => w.sound("bp_highlight"),
      children: [
        (0, Ce.jsxs)("div", {
          ...g,
          className: ge.imageContainer,
          children: [
            (0, Ce.jsx)("div", {
              className: ge.image,
              style: { backgroundImage: `url(${le(i, f, c)})` },
            }),
            (0, Ce.jsx)("div", { className: ge.check }),
          ],
        }),
        (0, Ce.jsx)("div", {
          className: ge.counter,
          children: u(we.readOrEmpty("selectable_reward.tabs.counter"), { count: d, limit: l }),
        }),
        (0, Ce.jsx)("div", {
          className: S(ge.title, a?.title),
          children: (0, Ce.jsx)(b, { text: ie(i, c), params: { equipmentType: p } }),
        }),
      ],
    });
  });
var ye = {
    base: "SelectButton_696eeaa5",
    base__plus: "SelectButton_base__plus_caa30688",
    base__disabled: "SelectButton_base__disabled_953b567",
    base__minus: "SelectButton_base__minus_2b97334c",
    fadeInWithScale: "SelectButton_fadeInWithScale_41cc3cb2",
    slideUp: "SelectButton_slideUp_41cc3cb2",
    blink: "SelectButton_blink_41cc3cb2",
    scale: "SelectButton_scale_41cc3cb2",
    rotate: "SelectButton_rotate_41cc3cb2",
    windowIn: "SelectButton_windowIn_41cc3cb2",
    fadeOut: "SelectButton_fadeOut_41cc3cb2",
    fadeIn: "SelectButton_fadeIn_41cc3cb2",
  },
  xe = (function (e) {
    return ((e.Plus = "plus"), (e.Minus = "minus"), e);
  })({}),
  ke = ({ type: e = "plus", isEnabled: t = !0, onClick: a }) =>
    (0, Ce.jsx)("div", {
      className: S(ye.base, ye[`base__${e}`], !t && ye.base__disabled),
      onClick: (e) => {
        (e.stopPropagation(), t && a(e));
      },
    }),
  je = {
    base: "Reward_aafd9d9f",
    reward: "Reward_d159ded4",
    image: "Reward_image_cdd2db9f",
    base__stateReceived: "Reward_base__stateReceived_21f091ec",
    base__stateLimited: "Reward_base__stateLimited_21f091ec",
    base__selected: "Reward_base__selected_21f091ec",
    base__accepting: "Reward_base__accepting_21f091ec",
    blink: "Reward_blink_21f091ec",
    optDeviceType: "Reward_optDeviceType_c9161298",
    packSize: "Reward_packSize_89374a40",
    label: "Reward_label_d9eb8f07",
    storage: "Reward_storage_5970894c",
    storage__hidden: "Reward_storage__hidden_4483c3c4",
    storageIcon: "Reward_storageIcon_3aa10d5a",
    selectControls: "Reward_selectControls_91575dd3",
    countText: "Reward_countText_a516c1a0",
    select: "Reward_select_98cf6062",
    state: "Reward_state_f012fad1",
    stateText: "Reward_stateText_3f71ade9",
    fadeInWithScale: "Reward_fadeInWithScale_21f091ec",
    slideUp: "Reward_slideUp_21f091ec",
    scale: "Reward_scale_21f091ec",
    rotate: "Reward_rotate_21f091ec",
    windowIn: "Reward_windowIn_21f091ec",
    fadeOut: "Reward_fadeOut_21f091ec",
    fadeIn: "Reward_fadeIn_21f091ec",
  },
  Ne = D.resolve("strings"),
  Ie = D.resolve("views").read((e) =>
    e.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
  ),
  Re = X(({ index: e, className: t }) => {
    const { model: a, controls: s } = fe(),
      r = a.animationState.get(),
      {
        type: o,
        count: c,
        state: d,
        storageCount: l,
        packSize: i,
        optDeviceType: _,
      } = a.computes.rewardByIndex(e),
      { addReward: b, reduceReward: m } = s,
      p = "state_normal" === d,
      f = d === te,
      g = d === ae,
      C = c > 0 && !g,
      h = C || p,
      v = r === me.Accepting && C,
      x = n(
        (0, ee.useMemo)(
          () =>
            f && 0 === c
              ? {
                  header: Ne.readOrEmpty("selectable_reward.reward.tooltip.state_limited.header"),
                  body: Ne.readOrEmpty("selectable_reward.reward.tooltip.state_limited.body"),
                }
              : { isEnabled: !1 },
          [f, c],
        ),
      ),
      k = y((0, ee.useMemo)(() => ({ contentId: Ie, args: { type: o } }), [o]));
    return (0, Ce.jsxs)("div", {
      className: S(
        je.base,
        t,
        C && je.base__selected,
        v && je.base__accepting,
        je[`base__${((j = d), j.replace(/_\w/g, (e) => e[1]?.toUpperCase() ?? e))}`],
      ),
      onClick: () => {
        p ? (w.sound("bp_click"), b(o)) : (f || g) && w.sound("bp_click_limit");
      },
      onMouseEnter: () => w.sound("bp_highlight"),
      children: [
        (0, Ce.jsxs)("div", {
          className: S(je.storage, l <= 0 && je.storage__hidden),
          children: [(0, Ce.jsx)("div", { className: je.storageIcon }), l],
        }),
        (0, Ce.jsxs)("div", {
          ...k,
          className: je.reward,
          children: [
            (0, Ce.jsx)("div", {
              className: je.image,
              style: { backgroundImage: `url(${ue(o)})` },
            }),
            _ !== oe.None &&
              (0, Ce.jsx)("div", {
                className: je.optDeviceType,
                style: { backgroundImage: `url(${be(o, _)})` },
              }),
            i > 1 &&
              (0, Ce.jsx)("div", {
                className: je.packSize,
                children: u(Ne.readOrEmpty("selectable_reward.reward.packSizeCount"), {
                  packSize: i,
                }),
              }),
          ],
        }),
        (0, Ce.jsx)("div", { className: je.label, children: _e(o) }),
        h
          ? (0, Ce.jsxs)("div", {
              className: je.selectControls,
              children: [
                (0, Ce.jsx)("span", { className: je.countText, children: c }),
                (0, Ce.jsxs)("div", {
                  className: je.select,
                  children: [
                    (0, Ce.jsx)(ke, {
                      type: xe.Minus,
                      isEnabled: C,
                      onClick: () => {
                        (w.sound("bp_click_minus"), m(o));
                      },
                    }),
                    (0, Ce.jsx)(ke, {
                      type: xe.Plus,
                      isEnabled: p,
                      onClick: () => {
                        p && (w.sound("bp_click_plus"), b(o));
                      },
                    }),
                  ],
                }),
              ],
            })
          : (f || g) &&
            (0, Ce.jsx)("div", {
              ...(f ? x : {}),
              className: je.state,
              children: (0, Ce.jsx)("div", {
                className: je.stateText,
                children: Ne.readOrEmpty(`selectable_reward.reward.${d}`),
              }),
            }),
      ],
    });
    var j;
  }),
  Te = {
    base: "ContentGrid_37546c98",
    scrollAreaContent: "ContentGrid_scrollAreaContent_d60bdc1",
    scrollAreaContent__centered: "ContentGrid_scrollAreaContent__centered_56ff9561",
    scrollArea: "ContentGrid_scrollArea_4b1babd8",
    cardsGrid: "ContentGrid_cardsGrid_3142d80",
    mask: "ContentGrid_mask_569ab401",
    mask__top: "ContentGrid_mask__top_a118e885",
    mask__bottom: "ContentGrid_mask__bottom_1cf7186f",
    mask__both: "ContentGrid_mask__both_b371be52",
    scrollBar: "ContentGrid_scrollBar_cc7e0d82",
    rewardCard: "ContentGrid_rewardCard_d9ece749",
    cardContent: "ContentGrid_cardContent_99c00bf7",
    statusWrapper: "ContentGrid_statusWrapper_7a9a6db7",
    statusWrapper__done: "ContentGrid_statusWrapper__done_bb2f9462",
    statusWrapper__alert: "ContentGrid_statusWrapper__alert_bb2f9462",
    icon: "ContentGrid_icon_ec9e371",
    fadeInWithScale: "ContentGrid_fadeInWithScale_e365c19f",
    slideUp: "ContentGrid_slideUp_e365c19f",
    blink: "ContentGrid_blink_e365c19f",
    scale: "ContentGrid_scale_e365c19f",
    rotate: "ContentGrid_rotate_e365c19f",
    windowIn: "ContentGrid_windowIn_e365c19f",
    fadeOut: "ContentGrid_fadeOut_e365c19f",
    fadeIn: "ContentGrid_fadeIn_e365c19f",
  },
  Be = X(({ className: e, onScrollableChange: t }) => {
    const { model: a } = fe(),
      { selectedTab: s } = a.root.get(),
      n = a.rewards.get(),
      o = a.tabs.get(),
      c = v(o, (e) => e.type === s),
      d = c.count >= c.limit,
      { api: l } = z(),
      [i, _] = Q(l),
      [b, u] = (0, ee.useState)(!1),
      m = (0, ee.useRef)(t);
    return (
      (m.current = t),
      (0, ee.useEffect)(() => {
        const e = () => {
          const [, e] = l.getBounds(),
            t = e > 0;
          u((e) => (e !== t ? t : e));
        };
        return (l.recalculateContent(), e(), l.events.on("recalculateContent", e));
      }, [n.length, l, s]),
      (0, ee.useEffect)(() => {
        m.current?.(b);
      }, [b]),
      (0, Ce.jsxs)("div", {
        className: S(Te.base, e),
        children: [
          (0, Ce.jsx)("div", {
            className: S(Te.mask, Te[`mask__${K(i, _)}`]),
            children: (0, Ce.jsx)(O, {
              classNames: {
                content: S(Te.scrollAreaContent, !b && Te.scrollAreaContent__centered),
              },
              children: (0, Ce.jsx)("div", {
                className: Te.scrollArea,
                children: (0, Ce.jsx)(r, {
                  border: "contour",
                  enabled: !0,
                  className: Te.cardsGrid,
                  children: f(n, (e, t) => {
                    const { count: a, state: s, type: r } = e,
                      { disabled: n, statusType: o } = (function (e, t, a) {
                        const s = e === te,
                          r = e === ae,
                          n = 0 === t;
                        return {
                          disabled: n && (s || r || a),
                          statusType: r ? "done" : s && n ? "alert" : void 0,
                        };
                      })(s, a, d);
                    return (0, Ce.jsx)(
                      J,
                      {
                        selected: a > 0,
                        disabled: n,
                        status: o,
                        className: Te.rewardCard,
                        classNames: {
                          mainContainerContent: Te.cardContent,
                          status: {
                            wrapper: S(Te.statusWrapper, Te[`statusWrapper__${o}`]),
                            icon: Te.icon,
                          },
                        },
                        soundTarget: "reward-selection:card",
                        children: (0, Ce.jsx)(Re, { index: t }),
                      },
                      r,
                    );
                  }),
                }),
              }),
            }),
          }),
          (0, Ce.jsx)(A, { classNames: { base: Te.scrollBar } }),
        ],
      })
    );
  }),
  Se = "Footer_775b7239",
  Ee = "Footer_buttons_877c593c",
  Oe = D.resolve("strings"),
  Ge = X(({ buttonsSize: e, classNames: a }) => {
    const { model: s, controls: r } = fe(),
      { totalRewardCount: o } = s.root.get(),
      d = o > 0,
      {
        breakpoint: { weight: l },
      } = N(),
      i = e ?? ((e) => (e > C.small.weight ? t.medium : t.small))(l),
      _ = c(),
      b = n(
        (0, ee.useMemo)(
          () => ({ disabled: d, body: Oe.readOrEmpty("selectable_reward.tooltips.footer.body") }),
          [d],
        ),
      );
    return (0, Ce.jsx)("div", {
      className: Se,
      children: (0, Ce.jsx)("div", {
        ...b,
        className: Ee,
        children: (0, Ce.jsx)(T, {
          size: i,
          theme: $.primary,
          disabled: !d,
          className: a?.button,
          onClick: () => {
            (r.setAnimationState(me.Accepting), _.run(r.submit, 600));
          },
          children: Oe.readOrEmpty("selectable_reward.footer.okBtn.label"),
        }),
      }),
    });
  }),
  Ae = {
    base: "Content_563e7cb8",
    base__accepting: "Content_base__accepting_cb7209e5",
    wrapper: "Content_wrapper_8961ad17",
    fadeIn: "Content_fadeIn_da09528a",
    wrapper__shown: "Content_wrapper__shown_9936ffdd",
    heading: "Content_heading_d9a7d80b",
    slideUp: "Content_slideUp_da09528a",
    title: "Content_title_f7727432",
    subTitle: "Content_subTitle_9c09656d",
    tabs: "Content_tabs_2049c8a6",
    tabBase: "Content_tabBase_da4d47fc",
    tabBackground: "Content_tabBackground_d4f2412",
    tabBackground__active: "Content_tabBackground__active_2055b5b",
    tabBackground__hover: "Content_tabBackground__hover_b301ca04",
    tabBorderImage: "Content_tabBorderImage_c9d862a4",
    tabBorderImage__active: "Content_tabBorderImage__active_81864d24",
    tabBorderImage__hover: "Content_tabBorderImage__hover_a26dd782",
    tabContent: "Content_tabContent_c4bf3aa",
    contentTab: "Content_contentTab_d65f5b89",
    contentTab__shown: "Content_contentTab__shown_9936ffdd",
    footer: "Content_footer_eaf6c6e0",
    bottomLip: "Content_bottomLip_f6b13712",
    fadeInWithScale: "Content_fadeInWithScale_da09528a",
    blink: "Content_blink_da09528a",
    scale: "Content_scale_da09528a",
    rotate: "Content_rotate_da09528a",
    windowIn: "Content_windowIn_da09528a",
    fadeOut: "Content_fadeOut_da09528a",
  },
  $e = X(({ title: e, subTitle: t, classNames: a, buttonsSize: s }) => {
    const r = (0, ee.useRef)(!1),
      [n, c] = (0, ee.useState)(!1),
      [i, _] = (0, ee.useState)(null),
      [b, u] = (0, ee.useState)(!1),
      { model: g, controls: C } = fe(),
      w = g.tabs.get(),
      { selectedTab: v } = g.root.get(),
      y = g.animationState.get(),
      k = o(w, (e) => e.type === v) ?? -1;
    return (
      (0, ee.useEffect)(() => {
        if (!n)
          return P(() => {
            c(!0);
          }, 300);
      }, [n]),
      (0, ee.useEffect)(() => {
        const e = (e) => {
          (e.code !== p.ARROW_LEFT && e.code !== p.ARROW_RIGHT) || (r.current = !1);
        };
        return (window.addEventListener("keyup", e), () => window.removeEventListener("keyup", e));
      }, []),
      h(p.ARROW_LEFT, () => {
        if (r.current) return;
        if (((r.current = !0), k <= 0)) return;
        const e = d(w, k - 1);
        C.openTab(e.type);
      }),
      h(p.ARROW_RIGHT, () => {
        if (r.current) return;
        if (((r.current = !0), k < 0 || k === w.length - 1)) return;
        const e = d(w, k + 1);
        C.openTab(e.type);
      }),
      (0, Ce.jsxs)("div", {
        className: S(Ae.base, Ae[`base__${y}`]),
        children: [
          (0, Ce.jsxs)(x, {
            size: l.large,
            theme: m.custom,
            active: v,
            children: [
              (0, Ce.jsxs)("div", {
                className: S(Ae.wrapper, n && Ae.wrapper__shown),
                children: [
                  (0, Ce.jsxs)("div", {
                    className: S(Ae.heading, a?.heading),
                    children: [
                      (0, Ce.jsx)("div", { className: S(Ae.title, a?.title), children: e }),
                      (0, Ce.jsx)("div", { className: S(Ae.subTitle, a?.subTitle), children: t }),
                    ],
                  }),
                  (0, Ce.jsx)("div", {
                    className: Ae.tabs,
                    children: f(w, (e, t) => {
                      const s = v === e.type,
                        r = i === e.type && !s,
                        n = {
                          base: Ae.tabBase,
                          background: S(
                            Ae.tabBackground,
                            s && Ae.tabBackground__active,
                            r && Ae.tabBackground__hover,
                          ),
                          borderImage: S(
                            Ae.tabBorderImage,
                            s && Ae.tabBorderImage__active,
                            r && Ae.tabBorderImage__hover,
                          ),
                          content: Ae.tabContent,
                        };
                      return (0, Ce.jsx)(
                        x.Tab,
                        {
                          tabId: e.type,
                          classNames: n,
                          onMouseEnter: () => _(e.type),
                          onMouseLeave: () => _(null),
                          onClick: () => C.openTab(e.type),
                          children: (0, Ce.jsx)(ve, {
                            index: t,
                            className: a?.category,
                            classNames: { title: a?.categoryTitle },
                          }),
                        },
                        e.type,
                      );
                    }),
                  }),
                ],
              }),
              (0, Ce.jsx)(x.Content, {
                children: () =>
                  (0, Ce.jsx)("div", {
                    className: S(Ae.contentTab, n && Ae.contentTab__shown),
                    children: (0, Ce.jsx)(q, {
                      children: (0, Ce.jsx)(Be, { onScrollableChange: u }),
                    }),
                  }),
              }),
            ],
          }),
          (0, Ce.jsxs)("div", {
            className: S(Ae.footer, a?.footer),
            children: [
              b && (0, Ce.jsx)("div", { className: Ae.bottomLip }),
              (0, Ce.jsx)(Ge, { buttonsSize: s, classNames: a?.footerClassNames }),
            ],
          }),
        ],
      })
    );
  }),
  We = "Error_9f7ff239",
  ze = "Error_title_881f33d",
  Me = "Error_description_9cc31237",
  Le = "Error_footer_2ba80f61",
  De = "Error_button_1befe7e6",
  Ue = D.resolve("strings"),
  Pe = X(() => {
    const { controls: e } = fe();
    return (0, Ce.jsxs)("div", {
      className: We,
      children: [
        (0, Ce.jsx)("div", {
          className: ze,
          children: Ue.readOrEmpty("selectable_reward.error.title"),
        }),
        (0, Ce.jsx)("div", {
          className: Me,
          children: Ue.readOrEmpty("selectable_reward.error.description"),
        }),
        (0, Ce.jsx)("div", {
          className: Le,
          children: (0, Ce.jsx)(T, {
            className: De,
            theme: $.primary,
            size: t.medium,
            onClick: e.close,
            children: Ue.readOrEmpty("selectable_reward.error.button"),
          }),
        }),
      ],
    });
  }),
  qe = "RewardSelection_496b50e",
  Fe = X(({ title: e, subTitle: t, classNames: a, buttonsSize: s }) => {
    const { model: r } = fe(),
      n = r.tabs.get();
    return (0, Ce.jsx)("div", {
      className: qe,
      children:
        n.length > 0
          ? (0, Ce.jsx)($e, { title: e, subTitle: t, classNames: a, buttonsSize: s })
          : (0, Ce.jsx)(Pe, {}),
    });
  }),
  He = ({ title: e = "", subTitle: t = "", modelProviderContext: a }) =>
    (0, Ce.jsx)(pe, {
      options: { context: a },
      children: (0, Ce.jsx)(Fe, { title: e, subTitle: t }),
    }),
  [Ye, Ke] = B()(
    ({ observableModel: e }) => ({ root: e.object() }),
    ({ externalModel: e }) => ({
      close: e.createCallbackNoArgs("selectableRewardModel.onCloseClick"),
    }),
  ),
  Qe = "App_285de3af",
  Je = "App_background_189ce663",
  Xe = "App_backgroundBlur_b6c090aa",
  Ze = "App_shadow_b56b33f2",
  Ve = "App_content_54c70e4",
  et = "App_close_fbc86043",
  tt = R.strings.battle_pass.rewardChoice,
  at = X(() => {
    const { model: e, controls: t } = Ke(),
      { chapterID: a, level: s } = e.root.get(),
      r = Boolean(s),
      [n, o] = (0, ee.useState)(!1);
    (i(t.close),
      _(t.close),
      (0, ee.useEffect)(
        () =>
          E(() => {
            o(!0);
          }),
        [],
      ));
    const c = (0, ee.useMemo)(
      () =>
        ((e, t) =>
          t
            ? {
                backgroundImage: `url(${Z(R.images.gui.maps.icons.battlePass.backgrounds.chapter_general, e)})`,
              }
            : V())(a, r),
      [a, r],
    );
    return (0, Ce.jsxs)("div", {
      className: Qe,
      children: [
        (0, Ce.jsx)("div", {
          className: Je,
          style: c,
          children: (0, Ce.jsx)("div", { className: Xe }),
        }),
        (0, Ce.jsx)("div", { className: Ze }),
        n &&
          (0, Ce.jsxs)("div", {
            className: Ve,
            children: [
              (0, Ce.jsx)(I, { className: et, onClose: t.close }),
              (0, Ce.jsx)(He, {
                modelProviderContext: "model.selectableRewardModel",
                title: tt.title(),
              }),
            ],
          }),
      ],
    });
  });
W(
  new U()
    .add(H)
    .add(Ye)
    .render((0, Ce.jsx)(at, {})),
);
