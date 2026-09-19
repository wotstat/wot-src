import { r as e } from "../chunks/rolldown-runtime.js";
import {
  An as a,
  Br as s,
  Hr as t,
  I as i,
  In as n,
  Ir as r,
  Jn as o,
  Nn as l,
  Or as d,
  Qn as c,
  Qr as _,
  R as m,
  Xn as p,
  Yn as u,
  Yr as w,
  _ as b,
  _n as h,
  an as g,
  bt as T,
  ci as f,
  cn as A,
  cr as x,
  dn as v,
  dr as P,
  fn as y,
  g as S,
  gn as N,
  gr as B,
  h as L,
  in as j,
  ir as E,
  jn as k,
  ln as I,
  o as U,
  on as C,
  pi as V,
  pn as W,
  r as Y,
  rn as $,
  ti as F,
  tn as O,
  ui as M,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as z } from "../chunks/vendor.js";
import { i as D, r as G, s as H } from "../chunks/utils.js";
import { n as q } from "../chunks/filename.js";
import { n as Q, t as X } from "../chunks/useKeyup.js";
var J = e(M(), 1),
  K = (function (e) {
    return (
      (e.BUY_BATTLE_PASS = "buyBattlePassReason"),
      (e.BUY_BATTLE_PASS_LEVELS = "buyBattlePassLevelsReason"),
      (e.BUY_MULTIPLE_BATTLE_PASS = "buyMultipleBattlePassReason"),
      (e.BUY_BATTLE_PASS_WITH_LEVELS = "buyBattlePassWithLevelsReason"),
      (e.STYLE_UPGRADE = "styleUpgradeReason"),
      (e.DEFAULT = "defaultReason"),
      e
    );
  })({}),
  [Z, ee] = h()(
    ({ observableModel: e }) => {
      const a = {
          root: e.object(),
          mainRewards: e.array("mainRewards.items"),
          additionalRewards: e.array("additionalRewards.items"),
          packageRewards: e.array("packageRewards.items"),
          starterPackRewards: e.array("starterPackRewards.items"),
          canToOpenAdditionView: B.box(!1),
        },
        i = N(() => {
          const { reason: e } = a.root.get();
          return e === K.BUY_BATTLE_PASS;
        }),
        n = N(() => {
          const { reason: e } = a.root.get();
          return e === K.BUY_BATTLE_PASS_WITH_LEVELS;
        }),
        r = N(() => {
          const { reason: e } = a.root.get();
          return e === K.BUY_MULTIPLE_BATTLE_PASS;
        }),
        o = N(() => i() || r() || n()),
        l = N(() => {
          const { reason: e } = a.root.get();
          return e === K.STYLE_UPGRADE;
        }),
        c = N(
          () =>
            o() && !a.canToOpenAdditionView.get()
              ? [...d(a.starterPackRewards.get(), t), ...d(a.packageRewards.get(), t)]
              : d(a.additionalRewards.get(), t),
          { equals: s },
        ),
        _ = N(() => c().length),
        m = N(() => _() > 0),
        p = N(() => d(a.mainRewards.get(), t), { equals: s }),
        u = N(() => {
          const e = p();
          if (1 === e.length) return e;
          const a = [...e],
            s = a[0];
          return a[1] && s ? ((a[0] = a[1]), (a[1] = s), a) : a;
        }),
        w = N(() => (a.root.get().isFinalReward ? u() : p())),
        b = N(() => w().length),
        h = N(() => {
          const { isFinalReward: e } = a.root.get();
          return 1 === b() || e;
        }),
        g = N(() => {
          const { isFinalReward: e } = a.root.get();
          return (2 !== w().length && e) || o() || l();
        }),
        T = [K.BUY_BATTLE_PASS_LEVELS, K.BUY_BATTLE_PASS_WITH_LEVELS, K.DEFAULT].includes(
          a.root.get().reason,
        ),
        f = N(() => {
          const { isPostProgressionUnlocked: e, isExtra: s, isFinalReward: t } = a.root.get();
          return e && !s && t && T;
        });
      return {
        ...a,
        computes: {
          isReasonBuy: i,
          isReasonBuyWithLevels: n,
          isMultiplePurchase: r,
          isReasonBuyCurrently: o,
          isReasonStyleUpgrade: l,
          getAdditionalRewards: c,
          getAdditionalRewardsLength: _,
          hasAdditionalRewards: m,
          getRewards: w,
          getRewardsLength: b,
          hasBigSizeReward: h,
          getFinalRewards: u,
          hasGlowAnimation: g,
          hasPostProgressionBanner: f,
        },
      };
    },
    ({ model: e, externalModel: a }) => ({
      enableToOpenAdditionView: P(() => {
        e.canToOpenAdditionView.set(!0);
      }),
      buy: a.createCallbackNoArgs("onBuyClick"),
      close: a.createCallbackNoArgs("onClose"),
      onShowPostProgression: a.createCallbackNoArgs("onShowPostProgression"),
    }),
  ),
  ae = "AdditionalRewards_c7f66cac",
  se = "AdditionalRewards_title_3afa6e1a",
  te = "AdditionalRewards_title__updateAnimation_3afa6e1a",
  ie = "AdditionalRewards_reward_79ca4edb",
  ne = "AdditionalRewards_rewardsList_532db93b",
  re = p(),
  oe = R.strings.battle_pass.battlePassAwardsView,
  le = z(({ rewards: e, pageNumber: s, className: t }) => {
    const { model: n } = ee(),
      r = n.canToOpenAdditionView.get(),
      { breakpoint: o } = u(),
      d = o.weight >= c.large.weight ? A.Big : A.Small,
      m = l(e, {
        from: { opacity: 0, y: "20rem" },
        enter: { opacity: 1, y: "0rem" },
        trail: 100,
        config: { duration: 300, easing: G },
        onStart: () => _.sound(R.sounds.bp_reward()),
        delay: 1 === s ? 1600 - (r ? 800 : 0) : 100,
      });
    return (0, re.jsxs)("div", {
      className: f(ae, t),
      children: [
        (0, re.jsx)("div", { className: f(se, r && te), children: oe.additionalRewards.subText() }),
        (0, re.jsx)("div", {
          className: ne,
          children: m((e, s) => {
            const t = s.item || s.name,
              n = $(s, d),
              r = (() => {
                const e = s.value.split("_");
                return "universal" === e[0]
                  ? { value: e[e.length - 1], valueType: v.MULTI }
                  : { value: s.value, valueType: g(s.name) };
              })(),
              o = j({ tooltipId: s.tooltipId }, Number(s.tooltipContentId), {
                ignoreShowDelay: !0,
              });
            return (0, re.jsx)(a.div, {
              className: ie,
              style: e,
              children: (0, re.jsx)(i, {
                name: t,
                image: n,
                special: s.overlayType,
                value: r.value,
                valueType: r.valueType,
                size: d,
                tooltipArgs: o,
              }),
            });
          }),
        }),
      ],
    });
  }),
  de = "Banner_d226745a",
  ce = "Banner_content_b0220cfe",
  _e = "Banner_icon_5d6fa4df",
  me = "Banner_description_ac932ff",
  pe = "Banner_title_f8c86772",
  ue = "Banner_text_6a6f5026",
  we = "Banner_buttonContainer_9bae7c89",
  be = "Banner_buttonWrapper_4e9f1fa3",
  he = "Banner_buttonGlow_d6f79d6a",
  ge = R.strings.battle_pass.battlePassAwardsView.footer,
  Te = z(({ className: e, parentRef: a }) => {
    const { model: s, controls: t } = ee(),
      { seasonStopped: i, currentLevel: n } = s.root.get();
    X({ [r.ENTER]: t.buy, [r.SPACE]: t.buy });
    const { breakpoint: o } = u(),
      l = o.weight >= c.medium.weight;
    return (0, re.jsxs)("div", {
      ref: a,
      className: f(de, e),
      children: [
        (0, re.jsxs)("div", {
          className: ce,
          children: [
            (0, re.jsx)("div", { className: _e }),
            (0, re.jsxs)("div", {
              className: me,
              children: [
                (0, re.jsx)("div", { className: pe, children: ge.bpTitle() }),
                (0, re.jsx)("div", {
                  className: ue,
                  children: n >= 45 ? ge.bpLastStagesTitle() : ge.bpInProgressTitle(),
                }),
              ],
            }),
          ],
        }),
        (0, re.jsxs)("div", {
          className: we,
          children: [
            (0, re.jsx)("div", { className: he }),
            (0, re.jsx)("div", {
              className: be,
              children: (0, re.jsx)(L, {
                disabled: i,
                type: b.main,
                size: l ? S.medium : S.small,
                onClick: t.buy,
                children: ge.bpButtonTitle(),
              }),
            }),
          ],
        }),
      ],
    });
  }),
  fe = "Footer_f09fca09",
  Ae = "Footer_base__withPostProgressionPath_67ee05f9",
  Re = "Footer_postProgressionInfo_90b6969f",
  xe = "Footer_lockImage_39ae8112",
  ve = "Footer_title_d3857cd",
  Pe = "Footer_title__highlight_97414ca4",
  ye = "Footer_buttonContainer_873ac017",
  Se = "Footer_postProgressionButton_45a39895",
  Ne = R.strings.battle_pass.battlePassAwardsView,
  Be = z(({ button: e, className: a }) => {
    const { model: s, controls: t } = ee(),
      { breakpoint: i } = u(),
      { reason: n, chapterID: r, isBaseStyleLevel: o, isPostProgressionUnlocked: l } = s.root.get(),
      d = s.computes.hasPostProgressionBanner(),
      _ = s.computes.isReasonBuyCurrently(),
      m = ((e, a, s) => {
        switch (e) {
          case K.BUY_BATTLE_PASS:
            return (0, re.jsx)(T, {
              text: Ne.mainReward.bpBuyAwardsCaption(),
              binding: { chapter: R.strings.battle_pass.chapter.fullName.$num(a) },
            });
          case K.BUY_BATTLE_PASS_WITH_LEVELS:
            return (0, re.jsx)(T, {
              text: Ne.mainReward.bpBuyWithLevels(),
              binding: { chapter: R.strings.battle_pass.chapter.fullName.$num(a) },
            });
          case K.BUY_MULTIPLE_BATTLE_PASS:
            return Ne.footer.allChaptersText();
          case K.STYLE_UPGRADE:
            return s ? Ne.footer.bpDescriptionGotStyle() : "";
          default:
            return "";
        }
      })(n, r, o),
      p = i.weight >= c.medium.weight;
    return (0, re.jsxs)("div", {
      className: f(fe, a, l && Ae),
      children: [
        d
          ? (0, re.jsxs)("div", {
              className: Re,
              children: [
                (0, re.jsx)("div", { className: xe }),
                (0, re.jsx)("div", { children: Ne.footer.postProgressionText() }),
              ],
            })
          : Boolean(m) && (0, re.jsx)("div", { className: f(ve, _ && Pe), children: m }),
        (0, re.jsxs)("div", {
          className: ye,
          "data-test-id": "buttonContainer",
          children: [
            (0, re.jsx)(L, {
              type: b.primary,
              size: p ? S.medium : S.small,
              onClick: e.onClick,
              children: e.text,
            }),
            d &&
              e.hasPostProgressionButton &&
              (0, re.jsx)(L, {
                type: b.secondary,
                size: p ? S.medium : S.small,
                onClick: t.onShowPostProgression,
                mixClass: Se,
                children: Ne.footer.postProgressionButton(),
              }),
          ],
        }),
      ],
    });
  }),
  Le = (e, a) => {
    const s = a.postfix ? `_${a.postfix}` : "";
    return ((e) => {
      const a = e.path.$dyn(`${e.name}_${e.id}`),
        s = e.path.$dyn("default");
      return a || s;
    })(e).$dyn(`${a.name}${s}`);
  },
  je = (function (e) {
    return ((e.Season = "season"), (e.Chapter = "chapter"), e);
  })({}),
  Ee = "ChapterLogo_aa1334cf",
  ke = z(() => {
    const { model: e } = ee(),
      { chapterID: a } = e.root.get(),
      s = e.computes.isMultiplePurchase()
        ? { backgroundImage: "url(R.images.gui.maps.icons.battlePass.rewards.bp_icon_triple)" }
        : {
            backgroundImage: `url(${Le({ path: R.images.gui.maps.icons.battlePass.rewards.chapterLogo, name: je.Chapter, id: a }, { name: "bp_icon" })})`,
          };
    return (0, re.jsx)("div", { className: Ee, style: s });
  }),
  Ie = "Glow_ae7a850f",
  Ue = "Glow_91b75819",
  Ce = ({ className: e }) =>
    (0, re.jsx)("div", {
      className: f(Ie, e),
      children: (0, re.jsx)("img", {
        className: Ue,
        src: "swf://gui/flash/animations/battlePass/rays.swf",
        alt: "",
      }),
    }),
  Ve = "AttachmentOverlay_cb258ef",
  We = ({ overlayType: e, rewardSize: a, className: s }) =>
    (0, re.jsx)("div", {
      className: f(Ve, s),
      style: {
        backgroundImage: `url(R.images.gui.maps.icons.customization.rarity.glowWithSign.${a}.${e})`,
      },
    }),
  Ye = "Compensation_50897e74",
  $e = V.resolve("images"),
  Fe = ({ className: e }) => {
    const a = o(
      $e.readOrEmpty("battlePass.icons.compensation"),
      $e.readOrEmpty("battlePass.icons.compensation_large"),
    );
    return (0, re.jsx)("div", { className: f(Ye, e), style: { backgroundImage: `url(${a})` } });
  },
  Oe = {
    base: "TankName_6f5fa973",
    base__wide: "TankName_base__wide_bdc02313",
    type: "TankName_type_be575ae0",
    fadeInWithScale: "TankName_fadeInWithScale_a6870619",
    slideUp: "TankName_slideUp_a6870619",
    blink: "TankName_blink_a6870619",
    scale: "TankName_scale_a6870619",
    rotate: "TankName_rotate_a6870619",
    windowIn: "TankName_windowIn_a6870619",
    fadeOut: "TankName_fadeOut_a6870619",
    fadeIn: "TankName_fadeIn_a6870619",
  },
  Me = (e, a) => ({
    backgroundImage: `url(R.images.gui.maps.icons.vehicleTypes.big.${e.replace("-", "_")}${a ? "_elite" : ""})`,
  }),
  ze = ({ isElite: e, vehicleName: a, vehicleType: s, vehicleLvl: t, isWide: i }) =>
    (0, re.jsxs)("div", {
      className: f(Oe.base, i && Oe.base__wide),
      children: [
        (0, re.jsx)("div", { className: Oe.level, children: E(t) }),
        (0, re.jsx)("div", { className: Oe.type, style: Me(s, e) }),
        (0, re.jsx)("div", { className: Oe.name, children: a }),
      ],
    }),
  De = "Text_textCenter_a832bab6",
  Ge = R.strings.battle_pass,
  He = ({ type: e, value: a }) => {
    switch (e) {
      case I.BattlaPassFinalAchievement:
        return (0, re.jsx)(T, {
          text: Ge.battlePassAwardsView.mainReward.reward(),
          binding: { name: a },
        });
      case I.TmanToken:
        return (0, re.jsx)(T, {
          classMix: De,
          text: Ge.battlePassAwardsView.mainReward.commander(),
          binding: { name: a },
        });
      case I.Gold:
      case I.Credits:
      case I.Crystal:
      case I.EquipCoin:
        return (0, re.jsx)(C, { format: "integral", value: Number(a) });
      default:
        return (0, re.jsx)(re.Fragment, { children: F(a) });
    }
  },
  qe = {
    base: "Title_ddf5c9be",
    title: "Title_37b34825",
    base__wide: "Title_base__wide_2e63cf3",
    base__credits: "Title_base__credits_2e63cf3",
    base__gold: "Title_base__gold_2e63cf3",
    base__bptaler: "Title_base__bptaler_2e63cf3",
    base__crystal: "Title_base__crystal_2e63cf3",
    subtitle: "Title_subtitle_918f7dda",
    fadeInWithScale: "Title_fadeInWithScale_2e63cf3",
    slideUp: "Title_slideUp_2e63cf3",
    blink: "Title_blink_2e63cf3",
    scale: "Title_scale_2e63cf3",
    rotate: "Title_rotate_2e63cf3",
    windowIn: "Title_windowIn_2e63cf3",
    fadeOut: "Title_fadeOut_2e63cf3",
    fadeIn: "Title_fadeIn_2e63cf3",
  },
  Qe = R.strings.battle_pass,
  Xe = ({ reward: e, size: a, className: s }) => {
    const {
        name: t,
        userName: i,
        vehicleLvl: n,
        vehicleName: r,
        vehicleType: o,
        isElite: l,
        isCollectionEntity: d,
      } = e,
      c = t === I.Vehicles;
    return (0, re.jsxs)("div", {
      className: f(qe.base, qe[`base__${a}`], qe[`base__${t}`], s),
      children: [
        (0, re.jsx)("div", {
          className: qe.title,
          children:
            c && n && r && o
              ? (0, re.jsx)(ze, {
                  vehicleLvl: n,
                  vehicleName: r,
                  vehicleType: o,
                  isElite: l || !1,
                  isWide: a === Ze.Wide,
                })
              : (0, re.jsx)(He, { type: t, value: i }),
        }),
        d && (0, re.jsx)("div", { className: qe.subtitle, children: Qe.common.collectionText() }),
      ],
    });
  },
  Je = {
    base: "Reward_c14bb065",
    imageWrapper: "Reward_imageWrapper_ee9e0933",
    image: "Reward_image_39bfebdb",
    fadeInWithScale: "Reward_fadeInWithScale_21f091ec",
    base__updateAnimation: "Reward_base__updateAnimation_21f091ec",
    base__wide: "Reward_base__wide_21f091ec",
    base__small: "Reward_base__small_21f091ec",
    compensation: "Reward_compensation_298a4419",
    compensation__wide: "Reward_compensation__wide_725e7d79",
    compensation__small: "Reward_compensation__small_a906de0f",
    attachment: "Reward_attachment_48a1a96b",
    title: "Reward_title_eac8d89d",
    fadeIn: "Reward_fadeIn_21f091ec",
    count: "Reward_count_b77b0d34",
    slideUp: "Reward_slideUp_21f091ec",
    blink: "Reward_blink_21f091ec",
    scale: "Reward_scale_21f091ec",
    rotate: "Reward_rotate_21f091ec",
    windowIn: "Reward_windowIn_21f091ec",
    fadeOut: "Reward_fadeOut_21f091ec",
  },
  Ke = R.strings.battle_pass,
  Ze = (function (e) {
    return ((e.Normal = "normal"), (e.Wide = "wide"), (e.Small = "small"), e);
  })({}),
  ea = [I.BattlaPassFinalAchievement, I.TmanToken, I.Vehicles],
  aa = [
    Y.credits,
    Y.gold,
    Y.crystal,
    Y.xp,
    Y.freeXP,
    Y.equipCoin,
    I.BattlaPassFinalAchievement,
    I.TmanToken,
    I.Vehicles,
    I.PremiumPlus,
    I.BattlePassTaler,
  ],
  sa = z(({ reward: e, rewardListIndex: a }) => {
    const { model: s } = ee(),
      t = s.canToOpenAdditionView.get(),
      i = s.computes.hasBigSizeReward(),
      n = s.computes.getRewardsLength(),
      {
        overlayType: r,
        tooltipContentId: o,
        tooltipId: l,
        name: d,
        userName: c,
        value: _,
        isCompensation: p,
      } = e,
      u = (() => {
        const e = _.split("_");
        return "universal" === e[0] ? e[e.length - 1] : _;
      })(),
      w = ((b = d), !aa.includes(b) && Number(u) > 1);
    var b;
    const h = ((e) => ea.includes(e))(d) || (c && c.length > 0),
      g = i ? (1 === n || 1 === a ? "wide" : "small") : "normal";
    return (0, re.jsxs)("div", {
      className: f(Je.base, Je[`base__${g}`], t && Je.base__updateAnimation),
      children: [
        (0, re.jsx)(m, {
          ignoreShowDelay: !0,
          contentId: Number(o),
          args: { tooltipId: l },
          children: (0, re.jsxs)("div", {
            className: Je.imageWrapper,
            children: [
              (0, re.jsx)("div", {
                className: Je.image,
                style: D(e),
                children:
                  p && (0, re.jsx)(Fe, { className: f(Je.compensation, Je[`compensation__${g}`]) }),
              }),
              H(d) &&
                (0, re.jsx)(We, {
                  overlayType: r,
                  rewardSize: A.S600x450,
                  className: Je.attachment,
                }),
              w &&
                (0, re.jsx)("div", {
                  className: Je.count,
                  children: (0, re.jsx)(T, {
                    text: Ke.common.multiplier(),
                    binding: { multiplier: u },
                  }),
                }),
            ],
          }),
        }),
        h && (0, re.jsx)(Xe, { reward: e, size: g, className: Je.title }),
      ],
    });
  }),
  ta = "Rewards_1a8854f",
  ia = "Rewards_base__updateSize_222a87fa",
  na = z(() => {
    const { model: e } = ee(),
      a = e.canToOpenAdditionView.get(),
      s = e.computes.getRewards();
    return (0, re.jsx)("div", {
      className: f(ta, a && ia),
      children: s.map((e, a) => (0, re.jsx)(sa, { reward: e, rewardListIndex: a }, `reward-${a}`)),
    });
  }),
  ra = "Ribbon_2234841",
  oa = "Ribbon_base__indentWide_72bb1f1",
  la = z(() => {
    const { model: e } = ee(),
      { isBattlePassPurchased: a, chapterID: s } = e.root.get(),
      t = e.computes.hasBigSizeReward(),
      i = e.computes.isReasonBuyCurrently(),
      n = t || i,
      { breakpoint: r } = u(),
      o = ((e) => {
        switch (e) {
          case c.small.name:
            return "small";
          case c.medium.name:
            return "medium";
          default:
            return "large";
        }
      })(r.name),
      l = {
        backgroundImage: `url(${Le({ path: R.images.gui.maps.icons.battlePass.logo.ribbon, name: je.Chapter, id: s }, { name: "ribbon", postfix: `${o}${a ? "_with_bp" : ""}` })})`,
      };
    return (0, re.jsx)("div", { className: f(ra, n && oa), style: l });
  }),
  da = "MainRewards_c825d49e",
  ca = "MainRewards_glow_31c8c598",
  _a = "MainRewards_rays_11ac61d3",
  ma = z(({ className: e }) => {
    const { model: s } = ee(),
      t = s.canToOpenAdditionView.get(),
      i = s.computes.isReasonBuyCurrently(),
      n = s.computes.hasGlowAnimation(),
      [r, o] = (0, J.useState)(!1),
      { contentOpacity: l } = k({
        from: { contentOpacity: 1 },
        contentOpacity: t ? 1 : 0,
        config: { duration: 400 },
        onResolve: () => {
          t && o(!0);
        },
      });
    return (0, re.jsxs)("div", {
      className: f(da, e),
      children: [
        n && !t && (0, re.jsx)(Ce, { className: ca }),
        (0, re.jsx)("div", { className: _a }),
        (0, re.jsx)(la, {}),
        i && !r
          ? (0, re.jsx)(a.div, {
              style: { opacity: l.to({ output: [1, 0] }) },
              children: (0, re.jsx)(ke, {}),
            })
          : (0, re.jsx)(na, {}),
      ],
    });
  }),
  pa = "App_1b1884ba",
  ua = "App_overlay_ce1d3259",
  wa = "App_overlay__common_f6f1f131",
  ba = "App_main_20c49be8",
  ha = "App_close_110976dc",
  ga = "App_content_d2251eca",
  Ta = "App_header_c3dc2c23",
  fa = "App_rewards_927ebd71",
  Aa = "App_rewards__additionalCentring_6f33396d",
  Ra = "App_additionalRewards_2598f029",
  xa = "App_additionalRewards__slideTop_bc21615e",
  va = "App_additionalRewards__animateSlide_9db8979b",
  Pa = "App_base__buyWithLevels_0",
  ya = "App_mainRewards_de1e5f92",
  Sa = "App_mainRewards__slideTop_bc21615e",
  Na = "App_mainRewards__animateSlide_7838291c",
  Ba = "App_footer_e0204304",
  La = "App_footer__hide_642d4e09",
  ja = "App_footer__diffTop_8dc6cdec",
  Ea = "App_banner_e0204304",
  ka = "App_banner__showPreparation_ca795627",
  Ia = R.strings.battle_pass,
  Ua = (e) =>
    e
      ? (0, re.jsx)(T, {
          text: Ia.battlePassAwardsView.header.bpTitle(),
          binding: { chapter: Ia.chapter.fullNameUppercased.$num(e) },
        })
      : Ia.battlePassAwardsView.header.bpTitleWithoutChapter(),
  Ca = (e, a) => {
    switch (e) {
      case K.BUY_BATTLE_PASS:
      case K.BUY_MULTIPLE_BATTLE_PASS:
      case K.BUY_BATTLE_PASS_WITH_LEVELS:
        return Ia.battlePassAwardsView.header.bpTitleWithoutChapter();
      case K.BUY_BATTLE_PASS_LEVELS:
      case K.STYLE_UPGRADE:
      case K.DEFAULT:
        return Ua(a);
    }
    return (console.warn("Unknown title reason: ", e), Ua(a));
  },
  Va = (e, a, s) => {
    switch (e) {
      case K.BUY_BATTLE_PASS:
      case K.BUY_MULTIPLE_BATTLE_PASS:
      case K.BUY_BATTLE_PASS_WITH_LEVELS:
        return Ia.battlePassAwardsView.header.bpBoughtText();
      case K.BUY_BATTLE_PASS_LEVELS:
        return a
          ? Ia.battlePassAwardsView.header.bpFinalLevelText()
          : Ia.battlePassAwardsView.header.bpLevelsText();
      case K.STYLE_UPGRADE:
        return s
          ? Ia.battlePassAwardsView.header.styleReceivedText()
          : Ia.battlePassAwardsView.header.styleUpgradedText();
      case K.DEFAULT:
        return a
          ? Ia.battlePassAwardsView.header.bpFinalLevelText()
          : Ia.battlePassAwardsView.header.bpLevelsText();
    }
    return (console.warn("Unknown status reason: ", e), "");
  },
  Wa = (e, a, s) =>
    s
      ? Ia.battlePassAwardsView.additionalRewards.seeMoreButtonText()
      : e
        ? (0, re.jsx)(T, {
            text: Ia.battlePassAwardsView.additionalRewards.bpRemainLevelsAwardsText(),
            binding: { remainingAwardsCount: a },
          })
        : Ia.battlePassAwardsView.additionalRewards.button(),
  Ya = z(() => {
    const { model: e, controls: a } = ee(),
      {
        reason: s,
        chapterID: t,
        isFinalReward: i,
        isBaseStyleLevel: r,
        isNeedToShowOffer: o,
      } = e.root.get(),
      l = e.canToOpenAdditionView.get(),
      d = e.computes.getAdditionalRewards(),
      c = e.computes.getAdditionalRewardsLength(),
      _ = e.computes.hasAdditionalRewards(),
      m = e.computes.isReasonBuyCurrently(),
      p = e.computes.isReasonBuyWithLevels(),
      u = e.computes.isReasonStyleUpgrade(),
      b = e.computes.hasPostProgressionBanner(),
      h = e.computes.hasBigSizeReward(),
      g = e.computes.getRewards().length > 0,
      [T, A] = (0, J.useState)(1),
      [v, P] = (0, J.useState)(0),
      [y, S] = (0, J.useState)(!1),
      N = m && g && !l,
      B = `${w(v)}rem`;
    n(a.close);
    const L = { title: Ca(s, t), subtitle: Va(s, i, r) },
      j = d.slice(10 * (T - 1), 10 * T),
      E = j.length,
      k = Math.ceil(c / 10),
      I = T < k,
      C = k > 1,
      V = o && !u && !I && !b,
      W = V && C,
      Y = !V || W,
      $ = (0, J.useRef)(null),
      F = () => {
        x(() => {
          $ && $.current && P($.current.offsetHeight);
        });
      };
    ((0, J.useEffect)(() => {
      (F(), S(!1));
    }, [V, W]),
      (0, J.useEffect)(() => {
        const e = () => {
          (F(), S(!0));
        };
        return (
          window.addEventListener("resize", e),
          () => {
            window.removeEventListener("resize", e);
          }
        );
      }, []));
    const O = ((e, a, s, t, i, n) => ({
        onClick: n,
        text: Wa(i, a > t * (s + 1) ? 10 : a - t * s, e),
        hasPostProgressionButton: !e && !i,
      }))(N, c, T, E, I, () => {
        N ? a.enableToOpenAdditionView() : I ? A(T + 1) : a.close();
      }),
      M = h && _,
      z = {
        backgroundImage: t
          ? `url(${q(R.images.gui.maps.icons.battlePass.backgrounds.chapter_general, t)})`
          : "url(R.images.gui.maps.icons.battlePass.backgrounds.common)",
        "--banner-height": B,
      };
    return (0, re.jsxs)("div", {
      className: f(pa, p && l && Pa),
      style: z,
      children: [
        (0, re.jsx)("div", { className: f(ua, !t && wa) }),
        (0, re.jsxs)("div", {
          className: ba,
          children: [
            (0, re.jsx)("div", {
              className: ha,
              children: (0, re.jsx)(U, {
                caption: R.strings.menu.viewHeader.closeBtn.label(),
                type: "close",
                side: "right",
                onClick: a.close,
              }),
            }),
            (0, re.jsxs)("div", {
              className: ga,
              children: [
                (0, re.jsx)("div", {
                  className: Ta,
                  children: (0, re.jsx)(Q, { title: L.title, status: L.subtitle }),
                }),
                (0, re.jsxs)("div", {
                  className: f(fa, M && Aa),
                  children: [
                    (0, re.jsx)(ma, { className: f(ya, W && Sa, W && !y && Na) }),
                    _ &&
                      (0, re.jsx)(le, {
                        rewards: j,
                        pageNumber: T,
                        className: f(Ra, W && xa, W && !y && va),
                      }),
                  ],
                }),
              ],
            }),
            Y && (0, re.jsx)(Be, { button: O, className: f(Ba, W && La, !V && ja) }),
            V && (0, re.jsx)(Te, { className: f(Ea, C && ka), parentRef: $ }),
          ],
        }),
      ],
    });
  });
y(
  new W()
    .add(O)
    .addWithProps(Z, {})
    .render((0, re.jsx)(Ya, {})),
);
