(() => {
  "use strict";
  var e,
    t = {
      3495: (e, t, a) => {
        a.d(t, { Y: () => d });
        var l = a(3138),
          i = a(6179),
          r = a(1043),
          n = a(5262);
        const s = l.O.client.getSize("rem"),
          o = s.width,
          m = s.height,
          _ = Object.assign({ width: o, height: m }, (0, n.T)(o, m, r.j)),
          d = (0, i.createContext)(_);
      },
      1039: (e, t, a) => {
        var l = a(6179),
          i = a.n(l),
          r = a(6536),
          n = a(3495),
          s = a(1043),
          o = a(5262),
          m = a(3138);
        (0, l.memo)(({ children: e }) => {
          const t = (0, l.useContext)(n.Y),
            a = (0, l.useState)(t),
            _ = a[0],
            d = a[1],
            c = (0, l.useCallback)((e, t) => {
              const a = m.O.view.pxToRem(e),
                l = m.O.view.pxToRem(t);
              d(Object.assign({ width: a, height: l }, (0, o.T)(a, l, s.j)));
            }, []);
          ((0, r.Z)(() => {
            engine.on("clientResized", c);
          }),
            (0, l.useEffect)(() => () => engine.off("clientResized", c), [c]));
          const g = (0, l.useMemo)(() => Object.assign({}, _), [_]);
          return i().createElement(n.Y.Provider, { value: g }, e);
        });
      },
      6010: (e, t, a) => {
        var l = a(6179),
          i = a(7382),
          r = a(3495);
        const n = ["children"];
        const s = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                l,
                i = {},
                r = Object.keys(e);
              for (l = 0; l < r.length; l++) ((a = r[l]), t.indexOf(a) >= 0 || (i[a] = e[a]));
              return i;
            })(e, n);
          const s = (0, l.useContext)(r.Y),
            o = s.extraLarge,
            m = s.large,
            _ = s.medium,
            d = s.small,
            c = s.extraSmall,
            g = s.extraLargeWidth,
            h = s.largeWidth,
            u = s.mediumWidth,
            b = s.smallWidth,
            w = s.extraSmallWidth,
            p = s.extraLargeHeight,
            v = s.largeHeight,
            f = s.mediumHeight,
            E = s.smallHeight,
            x = s.extraSmallHeight,
            L = { extraLarge: p, large: v, medium: f, small: E, extraSmall: x };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && o) return t;
            if (a.large && m) return t;
            if (a.medium && _) return t;
            if (a.small && d) return t;
            if (a.extraSmall && c) return t;
          } else {
            if (a.extraLargeWidth && g) return (0, i.H)(t, a, L);
            if (a.largeWidth && h) return (0, i.H)(t, a, L);
            if (a.mediumWidth && u) return (0, i.H)(t, a, L);
            if (a.smallWidth && b) return (0, i.H)(t, a, L);
            if (a.extraSmallWidth && w) return (0, i.H)(t, a, L);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && p) return t;
              if (a.largeHeight && v) return t;
              if (a.mediumHeight && f) return t;
              if (a.smallHeight && E) return t;
              if (a.extraSmallHeight && x) return t;
            }
          }
          return null;
        };
        s.defaultProps = {
          extraLarge: !1,
          large: !1,
          medium: !1,
          small: !1,
          extraSmall: !1,
          extraLargeWidth: !1,
          largeWidth: !1,
          mediumWidth: !1,
          smallWidth: !1,
          extraSmallWidth: !1,
          extraLargeHeight: !1,
          largeHeight: !1,
          mediumHeight: !1,
          smallHeight: !1,
          extraSmallHeight: !1,
        };
        (0, l.memo)(s);
      },
      7382: (e, t, a) => {
        a.d(t, { H: () => l });
        const l = (e, t, a) =>
          t.extraLargeHeight ||
          t.largeHeight ||
          t.mediumHeight ||
          t.smallHeight ||
          t.extraSmallHeight
            ? (t.extraLargeHeight && a.extraLarge) ||
              (t.largeHeight && a.large) ||
              (t.mediumHeight && a.medium) ||
              (t.smallHeight && a.small) ||
              (t.extraSmallHeight && a.extraSmall)
              ? e
              : null
            : e;
      },
      7739: (e, t, a) => {
        (a(6010), a(1039), a(3495));
      },
      1043: (e, t, a) => {
        a.d(t, { j: () => l });
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, a) => {
        var l;
        function i(e, t, a) {
          const l = (function (e, t) {
              switch (!0) {
                case e >= t.extraLarge.width:
                  return t.extraLarge.weight;
                case e >= t.large.width && e < t.extraLarge.width:
                  return t.large.weight;
                case e >= t.medium.width && e < t.large.width:
                  return t.medium.weight;
                case e >= t.small.width && e < t.medium.width:
                  return t.small.weight;
                default:
                  return t.extraSmall.weight;
              }
            })(e, a),
            i = (function (e, t) {
              switch (!0) {
                case e >= t.extraLarge.height:
                  return t.extraLarge.weight;
                case e >= t.large.height && e < t.extraLarge.height:
                  return t.large.weight;
                case e >= t.medium.height && e < t.large.height:
                  return t.medium.weight;
                case e >= t.small.height && e < t.medium.height:
                  return t.small.weight;
                default:
                  return t.extraSmall.weight;
              }
            })(t, a),
            r = Math.min(l, i);
          return {
            extraLarge: r === a.extraLarge.weight,
            large: r === a.large.weight,
            medium: r === a.medium.weight,
            small: r === a.small.weight,
            extraSmall: r === a.extraSmall.weight,
            extraLargeWidth: l === a.extraLarge.weight,
            largeWidth: l === a.large.weight,
            mediumWidth: l === a.medium.weight,
            smallWidth: l === a.small.weight,
            extraSmallWidth: l === a.extraSmall.weight,
            extraLargeHeight: i === a.extraLarge.weight,
            largeHeight: i === a.large.weight,
            mediumHeight: i === a.medium.weight,
            smallHeight: i === a.small.weight,
            extraSmallHeight: i === a.extraSmall.weight,
          };
        }
        (a.d(t, { T: () => i }),
          (function (e) {
            ((e.extraLarge = "extraLarge"),
              (e.large = "large"),
              (e.medium = "medium"),
              (e.small = "small"),
              (e.extraSmall = "extraSmall"),
              (e.extraLargeWidth = "extraLargeWidth"),
              (e.largeWidth = "largeWidth"),
              (e.mediumWidth = "mediumWidth"),
              (e.smallWidth = "smallWidth"),
              (e.extraSmallWidth = "extraSmallWidth"),
              (e.extraLargeHeight = "extraLargeHeight"),
              (e.largeHeight = "largeHeight"),
              (e.mediumHeight = "mediumHeight"),
              (e.smallHeight = "smallHeight"),
              (e.extraSmallHeight = "extraSmallHeight"));
          })(l || (l = {})));
      },
      122: (e, t, a) => {
        a.d(t, { F: () => l });
        const l = (e, t) => {
          let a;
          const l = setTimeout(() => {
            a = e();
          }, t);
          return () => {
            ("function" == typeof a && a(), clearTimeout(l));
          };
        };
      },
      527: (e, t, a) => {
        (a.r(t), a.d(t, { mouse: () => s, onResize: () => r }));
        var l = a(2472),
          i = a(1176);
        const r = (0, l.E)("clientResized"),
          n = { down: (0, l.E)("mousedown"), up: (0, l.E)("mouseup"), move: (0, l.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, i.R)(!1);
          }
          function a() {
            e.enabled && (0, i.R)(!0);
          }
          function l() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", a))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", a))
              : (0, i.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, a) => (
              (t[a] = (function (t) {
                return (a) => {
                  e.listeners += 1;
                  let i = !0;
                  const r = `mouse${t}`,
                    s = n[t]((e) => a([e, "outside"]));
                  function o(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, o),
                    l(),
                    () => {
                      i &&
                        (s(), window.removeEventListener(r, o), (e.listeners -= 1), l(), (i = !1));
                    }
                  );
                };
              })(a)),
              t
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), l());
            },
            enable() {
              ((e.enabled = !0), l());
            },
            enableOutside() {
              e.enabled && (0, i.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, i.R)(!1);
            },
          });
        })();
      },
      5959: (e, t, a) => {
        (a.r(t),
          a.d(t, {
            events: () => l,
            getMouseGlobalPosition: () => r,
            getSize: () => i,
            graphicsQuality: () => n,
          }));
        var l = a(527);
        function i(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const n = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, a) => {
        function l(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        a.d(t, { R: () => l });
      },
      2472: (e, t, a) => {
        function l(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        a.d(t, { E: () => l });
      },
      3138: (e, t, a) => {
        a.d(t, { O: () => i });
        var l = a(5959);
        const i = { view: a(7641), client: l };
      },
      3722: (e, t, a) => {
        function l(e, t, a = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, a);
        }
        function i(e, t, a) {
          return `url(${l(e, t, a)})`;
        }
        (a.r(t), a.d(t, { getBgUrl: () => i, getTextureUrl: () => l }));
      },
      6112: (e, t, a) => {
        a.d(t, { W: () => l });
        const l = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, a) => {
        a.d(t, { U: () => i });
        var l = a(2472);
        const i = {
          onTextureFrozen: (0, l.E)("self.onTextureFrozen"),
          onTextureReady: (0, l.E)("self.onTextureReady"),
          onDomBuilt: (0, l.E)("self.onDomBuilt"),
          onLoaded: (0, l.E)("self.onLoaded"),
          onDisplayChanged: (0, l.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, l.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, l.E)("children.onAdded"),
            onLoaded: (0, l.E)("children.onLoaded"),
            onRemoved: (0, l.E)("children.onRemoved"),
            onAttached: (0, l.E)("children.onAttached"),
            onTextureReady: (0, l.E)("children.onTextureReady"),
            onRequestPosition: (0, l.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, a) => {
        (a.r(t),
          a.d(t, {
            addModelObserver: () => _,
            addPreloadTexture: () => s,
            children: () => l,
            displayStatus: () => i.W,
            displayStatusIs: () => y,
            events: () => r.U,
            extraSize: () => $,
            forceTriggerMouseMove: () => S,
            freezeTextureBeforeResize: () => u,
            getBrowserTexturePath: () => m,
            getDisplayStatus: () => P,
            getScale: () => b,
            getSize: () => c,
            getViewGlobalPosition: () => h,
            isClientAccessible: () => E,
            isEventHandled: () => L,
            isFocused: () => f,
            pxToRem: () => w,
            remToPx: () => p,
            resize: () => g,
            sendEvent: () => n.qP,
            setAnimateWindow: () => v,
            setEventHandled: () => x,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => M,
          }));
        var l = a(3722),
          i = a(6112),
          r = a(6538),
          n = a(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function m(e, t, a, l = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, a, l);
        }
        function _(e, t, a) {
          return viewEnv.addDataChangedCallback(e, t, a);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function c(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function g(e, t, a = "px") {
          return "rem" === a ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function h(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: p(t.x), y: p(t.y) };
        }
        function u() {
          viewEnv.freezeTextureBeforeResize();
        }
        function b() {
          return viewEnv.getScale();
        }
        function w(e) {
          return viewEnv.pxToRem(e);
        }
        function p(e) {
          return viewEnv.remToPx(e);
        }
        function v(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function f() {
          return viewEnv.isFocused();
        }
        function E() {
          return viewEnv.isClientAccessible();
        }
        function x() {
          return viewEnv.setEventHandled();
        }
        function L() {
          return viewEnv.isEventHandled();
        }
        function S() {
          viewEnv.forceTriggerMouseMove();
        }
        function P() {
          return viewEnv.getShowingStatus();
        }
        const y = Object.keys(i.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === i.W[t]), e),
            {},
          ),
          $ = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          M = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        a.d(t, { qP: () => m });
        const l = ["args"];
        const i = 2,
          r = 16,
          n = 32,
          s = 64,
          o = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                n = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    l,
                    i = {},
                    r = Object.keys(e);
                  for (l = 0; l < r.length; l++) ((a = r[l]), t.indexOf(a) >= 0 || (i[a] = e[a]));
                  return i;
                })(t, l);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, n, {
                      arguments:
                        ((i = r),
                        Object.entries(i).map(([e, t]) => {
                          const a = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: a, name: e, number: t };
                            case "boolean":
                              return { __Type: a, name: e, bool: t };
                            default:
                              return { __Type: a, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, n));
            }
            return viewEnv.handleViewEvent({ __Type: a, type: e });
            var i;
          },
          m = {
            close(e) {
              o("popover" === e ? i : n);
            },
            minimize() {
              o(s);
            },
            move(e) {
              o(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      6536: (e, t, a) => {
        a.d(t, { Z: () => i });
        var l = a(6179);
        const i = (e) => {
          const t = (0, l.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      5415: (e, t, a) => {
        (a(6179), a(7739));
        var l = a(1043);
        let i, r, n;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.j.small.width)] = "Small"),
            (e[(e.Medium = l.j.medium.width)] = "Medium"),
            (e[(e.Large = l.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.j.extraLarge.width)] = "ExtraLarge"));
        })(i || (i = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = l.j.small.width)] = "Small"),
              (e[(e.Medium = l.j.medium.width)] = "Medium"),
              (e[(e.Large = l.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = l.j.extraLarge.width)] = "ExtraLarge"));
          })(r || (r = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.j.small.height)] = "Small"),
              (e[(e.Medium = l.j.medium.height)] = "Medium"),
              (e[(e.Large = l.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.j.extraLarge.height)] = "ExtraLarge"));
          })(n || (n = {})));
      },
      903: (e, t, a) => {
        a.d(t, { FL: () => i, wD: () => l });
        (a(5415), a(8546));
        const l = (e, t, a = "") => {
            const l = a.length > 0 ? `_${a}` : a,
              i = e.$dyn(`c_${t}${l}`),
              r = e.$dyn(`common${l}`);
            return i || r;
          },
          i = (e, t, a, i) => {
            const r = R.images.gui.maps.icons.battlePass.logo,
              n = l(r, e, `emblem${i ? "_BP" : ""}${a ? "_open" : ""}${t}`);
            return n ? { backgroundImage: `url(${n})` } : void 0;
          };
      },
      9830: (e, t, a) => {
        var l = a(6483),
          i = a.n(l),
          r = a(6179),
          n = a.n(r),
          s = a(903);
        const o = {
            base: "Emblem_base_be",
            progress: "Emblem_progress_37",
            progress__small: "Emblem_progress__small_42",
            progress__completed: "Emblem_progress__completed_69",
            hideProgress: "Emblem_hideProgress_b4",
            progress__hidden: "Emblem_progress__hidden_6d",
            image: "Emblem_image_dc",
            image__micro: "Emblem_image__micro_aa",
            image__small: "Emblem_image__small_ce",
            image__open: "Emblem_image__open_43",
            image__openSmall: "Emblem_image__openSmall_5d",
            image__openMicro: "Emblem_image__openMicro_a9",
            image__battlePass: "Emblem_image__battlePass_ba",
            image__battlePassSmall: "Emblem_image__battlePassSmall_d5",
            image__battlePassMicro: "Emblem_image__battlePassMicro_6e",
            image__battlePassOpen: "Emblem_image__battlePassOpen_36",
            image__battlePassSmallOpen: "Emblem_image__battlePassSmallOpen_2f",
            image__battlePassMicroOpen: "Emblem_image__battlePassMicroOpen_e5",
            image__seasonWaiting: "Emblem_image__seasonWaiting_96",
            image__seasonWaitingSmall: "Emblem_image__seasonWaitingSmall_c0",
            image__seasonWaitingMicro: "Emblem_image__seasonWaitingMicro_86",
            image__completedFree: "Emblem_image__completedFree_56",
            image__completedFreeSmall: "Emblem_image__completedFreeSmall_a1",
            image__completedFreeMicro: "Emblem_image__completedFreeMicro_45",
            image__completedFreeOpen: "Emblem_image__completedFreeOpen_08",
            image__completedFreeSmallOpen: "Emblem_image__completedFreeSmallOpen_91",
            image__completedFreeMicroOpen: "Emblem_image__completedFreeMicroOpen_d3",
            image__completedGolden: "Emblem_image__completedGolden_77",
            image__completedGoldenSmall: "Emblem_image__completedGoldenSmall_be",
            image__completedGoldenMicro: "Emblem_image__completedGoldenMicro_2d",
            marathon: "Emblem_marathon_c6",
            resource: "Emblem_resource_97",
            marathon__micro: "Emblem_marathon__micro_61",
            resource__micro: "Emblem_resource__micro_67",
            marathon__small: "Emblem_marathon__small_0b",
            resource__small: "Emblem_resource__small_41",
            hideLevel: "Emblem_hideLevel_f2",
            showLevel: "Emblem_showLevel_c5",
            hideLevelSmall: "Emblem_hideLevelSmall_cc",
            showLevelSmall: "Emblem_showLevelSmall_31",
            hideLevelMicro: "Emblem_hideLevelMicro_15",
            showLevelMicro: "Emblem_showLevelMicro_bc",
            showIcon: "Emblem_showIcon_c2",
            showIconSmall: "Emblem_showIconSmall_1d",
            showIconMicro: "Emblem_showIconMicro_f8",
          },
          m = {
            base: "Label_base_85",
            textWithBlend: "Label_textWithBlend_07",
            textWithBlend__show: "Label_textWithBlend__show_fa",
            show: "Label_show_69",
            textWithBlend__new: "Label_textWithBlend__new_4a",
            textWithBlend__hide: "Label_textWithBlend__hide_f1",
            hide: "Label_hide_33",
            textMask: "Label_textMask_7f",
            textMask__animated: "Label_textMask__animated_38",
            maskAppearance: "Label_maskAppearance_26",
            textMask__micro: "Label_textMask__micro_37",
            textMask__small: "Label_textMask__small_54",
            textMask__medium: "Label_textMask__medium_eb",
            textMask__large: "Label_textMask__large_0a",
            textMask__extraLarge: "Label_textMask__extraLarge_4c",
            text: "Label_text_67",
            text__micro: "Label_text__micro_a4",
            text__small: "Label_text__small_e0",
            text__large: "Label_text__large_65",
            text__extraLarge: "Label_text__extraLarge_22",
            text__blended: "Label_text__blended_67",
            text__filtered: "Label_text__filtered_86",
            text__rewardScreen: "Label_text__rewardScreen_68",
            textAppearance: "Label_textAppearance_31",
            text__show: "Label_text__show_95",
            text__hide: "Label_text__hide_37",
            text__hideWithDelay: "Label_text__hideWithDelay_53",
            text__new: "Label_text__new_a0",
            hideLevel: "Label_hideLevel_61",
            showLevel: "Label_showLevel_55",
            hideLevelSmall: "Label_hideLevelSmall_9d",
            showLevelSmall: "Label_showLevelSmall_96",
            hideLevelMicro: "Label_hideLevelMicro_9e",
            showLevelMicro: "Label_showLevelMicro_50",
            showIcon: "Label_showIcon_0f",
            showIconSmall: "Label_showIconSmall_96",
            hideProgress: "Label_hideProgress_0c",
            showIconMicro: "Label_showIconMicro_1e",
          },
          _ = "R.images.gui.maps.icons.battlePass.logo",
          d = R.images.gui.maps.icons.battlePass.logo,
          c = (e, t, a) => {
            if (e && t) {
              const e = `c_${a}_font_texture_gold_contrast`;
              return d.$dyn(e) ? `url(${_}.${e})` : `url(${_}.font_texture_gold_contrast)`;
            }
            if (e) {
              const e = `c_${a}_font_texture_gold`;
              return d.$dyn(e) ? `url(${_}.${e})` : `url(${_}.font_texture_gold)`;
            }
            const l = `c_${a}_font_texture`;
            return d.$dyn(l) ? `url(${_}.${l})` : `url(${_}.font_texture)`;
          },
          g = (0, r.memo)(
            ({
              level: e,
              size: t,
              isGold: a,
              isForRewardScreen: l = !1,
              curState: r,
              isFirstLevel: s,
              showProgressionCompleted: o,
              chapterID: _ = 0,
            }) => {
              const d = i()(m.base, m[`base__${t}`]),
                g = i()(
                  m.text,
                  m.text__filtered,
                  m[`text__${t}`],
                  m[`text__${r}`],
                  o && m.text__hideWithDelay,
                  s && m.text__new,
                  l && m.text__rewardScreen,
                ),
                h = i()(
                  m.textWithBlend,
                  s && m.text__new,
                  o && m.text__hideWithDelay,
                  m[`textWithBlend__${r}`],
                ),
                u = i()(m.text, m.text__blended, m[`text__${t}`], l && m.text__rewardScreen),
                b = i()(m.textMask, l && m.textMask__animated, m[`textMask__${t}`]);
              return n().createElement(
                "div",
                { className: d },
                n().createElement("div", { className: g }, e),
                n().createElement(
                  "div",
                  { className: h },
                  n().createElement("div", { className: u }, e),
                  n().createElement("div", {
                    className: b,
                    style: { backgroundImage: c(a, l, _) },
                  }),
                ),
              );
            },
          );
        var h = a(8546);
        const u = {
            label: "EmblemLabels_label_14",
            label__small: "EmblemLabels_label__small_a3",
            label__micro: "EmblemLabels_label__micro_4b",
            label__hasProgress: "EmblemLabels_label__hasProgress_26",
            label__hasProgressProgression: "EmblemLabels_label__hasProgressProgression_77",
            label__hasProgressSmall: "EmblemLabels_label__hasProgressSmall_c1",
            label__show: "EmblemLabels_label__show_3d",
            showLevel: "EmblemLabels_showLevel_04",
            label__showSmall: "EmblemLabels_label__showSmall_7e",
            showLevelSmall: "EmblemLabels_showLevelSmall_2f",
            label__hide: "EmblemLabels_label__hide_28",
            hideLevel: "EmblemLabels_hideLevel_be",
            label_hideSmall: "EmblemLabels_label_hideSmall_65",
            hideLevelSmall: "EmblemLabels_hideLevelSmall_c1",
            label__hideWithDelay: "EmblemLabels_label__hideWithDelay_68",
            label__hideWithDelaySmall: "EmblemLabels_label__hideWithDelaySmall_36",
            label__new: "EmblemLabels_label__new_d7",
            label__newSmall: "EmblemLabels_label__newSmall_c1",
            label__disabled: "EmblemLabels_label__disabled_b6",
            icon: "EmblemLabels_icon_40",
            icon__small: "EmblemLabels_icon__small_f3",
            icon__micro: "EmblemLabels_icon__micro_cf",
            icon__animated: "EmblemLabels_icon__animated_09",
            showIcon: "EmblemLabels_showIcon_d3",
            icon__animatedSmall: "EmblemLabels_icon__animatedSmall_e4",
            icon__animatedMicro: "EmblemLabels_icon__animatedMicro_10",
            showIconSmall: "EmblemLabels_showIconSmall_cb",
            hideLevelMicro: "EmblemLabels_hideLevelMicro_65",
            showLevelMicro: "EmblemLabels_showLevelMicro_ab",
            hideProgress: "EmblemLabels_hideProgress_7f",
            showIconMicro: "EmblemLabels_showIconMicro_5c",
          },
          b = (e, t) => {
            const a = e ? "BP" : "";
            return `${((e) => {
              switch (e) {
                case h.$u.Small:
                  return "l";
                case h.$u.Micro:
                  return "s";
                default:
                  return "xl";
              }
            })(t)}${a}`;
          },
          w = (0, r.memo)(
            ({
              newLevel: e,
              level: t,
              size: a,
              battlePassState: l,
              hasProgression: r,
              isGolden: o,
              labelAnimation: m,
              newLabelAnimation: _,
              isChapterChosen: d = !1,
              chapterID: c = 0,
              isProgressionCompleted: w = !1,
              hasBeenActive: p = !1,
              isChapterSelection: v = !1,
              isProgression: f = !1,
            }) => {
              let E = "",
                x = "";
              a === h.$u.Small
                ? ((E = "Small"), (x = "__small"))
                : a === h.$u.Micro && ((E = "Micro"), (x = "__micro"));
              const L = l === h.Bq.SwitchedChapterRightNow,
                S = l === h.Bq.CompletedRightNow,
                P = ((e, t, a, l, i) => (e || i ? t || !a : t || !l))(v, w, p, d, f),
                y = !f && !v;
              return n().createElement(
                n().Fragment,
                null,
                P
                  ? n().createElement("div", {
                      className: i()(u.icon, x && u[`icon${x}`], S && u[`icon__animated${E}`]),
                      style: {
                        backgroundImage: `url(${(() => {
                          const e = R.images.gui.maps.icons.battlePass.logo,
                            t = b(o, a);
                          if (y) {
                            if (w) {
                              const a = e.tank.$dyn(`tank_${t}`),
                                l = e.tank.$dyn(`c_${c}_tank_${t}`);
                              return null != l ? l : a;
                            }
                            if (!d) return e.$dyn("not_chosen");
                          }
                          return (0, s.wD)(e.chapterIcons, c, t);
                        })()})`,
                      },
                    })
                  : n().createElement(
                      "div",
                      {
                        className: i()(
                          u.label,
                          u[`label${x}`],
                          L && u.label__new,
                          L && u[`label__new${E}`],
                          !S && w && u.label__disabled,
                          u[`label__${m}${E}`],
                          r && u[`label__hasProgress${E}`],
                          r && u[`label__hasProgress${E}${f ? "Progression" : ""}`],
                        ),
                        lang: R.strings.settings.LANGUAGE_CODE(),
                      },
                      n().createElement(g, {
                        level: t,
                        size: a,
                        isGold: o,
                        isFirstLevel: L,
                        curState: m,
                        showProgressionCompleted: S,
                        key: "label",
                        chapterID: c,
                      }),
                    ),
                e &&
                  n().createElement(
                    "div",
                    {
                      className: i()(
                        u.label,
                        u[`label${x}`],
                        L && u.label__new,
                        L && u[`label__new${E}`],
                        u[`label__${_}${E}`],
                        r && u[`label__hasProgress${E}`],
                      ),
                    },
                    n().createElement(g, {
                      level: e,
                      size: a,
                      isGold: o,
                      isFirstLevel: L,
                      curState: _,
                      key: "newLabel",
                      chapterID: c,
                    }),
                  ),
              );
            },
          ),
          p = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let v, f;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(v || (v = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(f || (f = {})));
        const E = ({ size: e = v.Default, classMix: t }) =>
            n().createElement("div", { className: i()(p.background, p[`background__${e}`], t) }),
          x = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          L = ({ size: e }) => {
            const t = i()(x.base, x[`base__${e}`]);
            return n().createElement("div", { className: t });
          },
          S = {
            base: "ProgressLineImpose_base_80",
            base__disabled: "ProgressLineImpose_base__disabled_cc",
            base__finished: "ProgressLineImpose_base__finished_d4",
            base__withoutBounce: "ProgressLineImpose_base__withoutBounce_56",
            pattern: "ProgressLineImpose_pattern_1c",
            base__small: "ProgressLineImpose_base__small_55",
            gradient: "ProgressLineImpose_gradient_35",
            glow: "ProgressLineImpose_glow_a5",
            glow__left: "ProgressLineImpose_glow__left_d8",
          },
          P = (0, r.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: a,
              baseStyles: l,
              isComplete: r,
              withoutBounce: s,
            }) => {
              const o = i()(
                  S.base,
                  S[`base__${e}`],
                  a && S.base__disabled,
                  r && S.base__finished,
                  s && S.base__withoutBounce,
                ),
                m = !a && !r;
              return n().createElement(
                "div",
                { className: o, style: l, ref: t },
                n().createElement("div", { className: S.pattern }),
                n().createElement("div", { className: S.gradient }),
                m && n().createElement(L, { size: e }),
              );
            },
          ),
          y = ({ size: e, value: t, lineRef: a, disabled: l, onComplete: i }) => {
            const s = (0, r.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              o = 100 === t;
            return (
              (0, r.useEffect)(() => {
                o && i && i();
              }, [o, i]),
              n().createElement(P, {
                size: e,
                disabled: l,
                baseStyles: s,
                isComplete: o,
                lineRef: a,
              })
            );
          };
        var $ = a(122);
        let M, C;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(M || (M = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(C || (C = {})));
        const B = "ProgressBarDeltaSimple_base_6c",
          k = "ProgressBarDeltaSimple_delta_99",
          O = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: l,
              size: i,
              to: s,
              onEndAnimation: o,
              onChangeAnimationState: m,
            }) => {
              const _ = s < l,
                d = (0, r.useState)(C.Idle),
                c = d[0],
                g = d[1],
                h = c === C.In,
                u = c === C.End,
                b = c === C.Idle,
                w = (0, r.useCallback)(
                  (e) => {
                    (g(e), m && m(e));
                  },
                  [m],
                );
              ((0, r.useEffect)(() => {
                if (b && !a) {
                  const e = t;
                  return (0, $.F)(() => {
                    w(C.In);
                  }, e);
                }
              }, [w, a, b, t]),
                (0, r.useEffect)(() => {
                  if (h) {
                    const a = e + t;
                    return (0, $.F)(() => {
                      (o && o(), w(C.End));
                    }, a);
                  }
                }, [w, h, o, t, e]));
              const p = (0, r.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, t, e],
                ),
                v = (0, r.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, t, e],
                ),
                f = (0, r.useMemo)(
                  () => ({ width: `${Math.abs(l - s)}%`, left: `${_ ? s : l}%` }),
                  [l, _, s],
                );
              return u
                ? null
                : n().createElement(
                    "div",
                    { className: B, style: f },
                    n().createElement(
                      "div",
                      { style: b ? p : v, className: k },
                      n().createElement(L, { size: i }),
                    ),
                  );
            },
          ),
          W = (0, r.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: l,
              disabled: i,
              isComplete: s,
              animationSettings: o,
              onChangeAnimationState: m,
              onEndAnimation: _,
            }) => {
              const d = (0, r.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return n().createElement(
                n().Fragment,
                null,
                n().createElement(P, {
                  size: t,
                  lineRef: l,
                  disabled: i,
                  isComplete: s,
                  baseStyles: d,
                }),
                a >= 0 &&
                  n().createElement(O, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: a,
                    size: t,
                    to: e,
                    onChangeAnimationState: m,
                    onEndAnimation: _,
                  }),
              );
            },
          ),
          z = "ProgressBarDeltaGrow_base_7e",
          I = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          H = "ProgressBarDeltaGrow_glow_68",
          D = (e) => (e ? { left: 0 } : { right: 0 }),
          A = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          j = (e) => ({ transitionDuration: `${e}ms` }),
          F = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: l,
              size: s,
              to: o,
              onEndAnimation: m,
              onChangeAnimationState: _,
              className: d,
            }) => {
              const c = o < l,
                g = (0, r.useState)(M.Idle),
                h = g[0],
                u = g[1],
                b = h === M.End,
                w = h === M.Idle,
                p = h === M.Grow,
                v = h === M.Shrink,
                f = (0, r.useCallback)(
                  (e) => {
                    (u(e), _ && _(e));
                  },
                  [_],
                ),
                E = (0, r.useCallback)(
                  (e, t) =>
                    (0, $.F)(() => {
                      f(e);
                    }, t),
                  [f],
                );
              (0, r.useEffect)(() => {
                if (!a)
                  return w
                    ? E(M.Grow, t)
                    : p
                      ? E(M.Shrink, e)
                      : v
                        ? E(M.End, e)
                        : void (b && m && m());
              }, [E, a, b, p, w, v, m, t, e]);
              const x = (0, r.useMemo)(() => Object.assign({ width: "100%" }, j(e), D(c)), [c, e]),
                S = (0, r.useMemo)(() => Object.assign({ width: "0%" }, j(e), D(c)), [c, e]),
                P = (0, r.useMemo)(() => Object.assign({ width: "0%" }, A(c, l), j(e)), [l, c, e]),
                y = (0, r.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - l)}%` }, A(c, l), j(e)),
                  [l, c, o, e],
                );
              if (b) return null;
              const C = i()(z, d, c && 0 === o && I);
              return n().createElement(
                "div",
                { style: w ? P : y, className: C },
                n().createElement(
                  "div",
                  { style: v ? S : x, className: H },
                  n().createElement(L, { size: s }),
                ),
              );
            },
          ),
          T = (0, r.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: l,
              disabled: i,
              isComplete: s,
              animationSettings: o,
              onEndAnimation: m,
              onChangeAnimationState: _,
            }) => {
              const d = e < a,
                c = (0, r.useState)(!1),
                g = c[0],
                h = c[1],
                u = (0, r.useCallback)(
                  (e) => {
                    (e === M.Shrink && h(!0), _ && _(e));
                  },
                  [_],
                ),
                b = (0, r.useMemo)(() => ({ width: `${a}%`, transitionProperty: "none" }), [a]),
                w = (0, r.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return n().createElement(
                n().Fragment,
                null,
                n().createElement(P, {
                  size: t,
                  lineRef: l,
                  disabled: i,
                  isComplete: s,
                  withoutBounce: d && 0 === e,
                  baseStyles: g ? w : b,
                }),
                a >= 0 &&
                  n().createElement(F, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    onChangeAnimationState: u,
                    freezed: o.freezed,
                    onEndAnimation: m,
                    from: a,
                    size: t,
                    to: e,
                    className: o.delta.className,
                  }),
              );
            },
          ),
          N = ["onComplete", "onEndAnimation"];
        function G() {
          return (
            (G =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var l in a) Object.prototype.hasOwnProperty.call(a, l) && (e[l] = a[l]);
                }
                return e;
              }),
            G.apply(this, arguments)
          );
        }
        const V = (0, r.memo)((e) => {
            let t = e.onComplete,
              a = e.onEndAnimation,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  l,
                  i = {},
                  r = Object.keys(e);
                for (l = 0; l < r.length; l++) ((a = r[l]), t.indexOf(a) >= 0 || (i[a] = e[a]));
                return i;
              })(e, N);
            const i = (0, r.useState)(!1),
              s = i[0],
              o = i[1],
              m = (0, r.useCallback)(() => {
                const e = 100 === l.to;
                (e !== s && o(e), e && t && t(), a && a());
              }, [s, t, a, l.to]);
            switch (l.animationSettings.type) {
              case f.Simple:
                return n().createElement(W, G({}, l, { onEndAnimation: m, isComplete: s }));
              case f.Growing:
                return n().createElement(T, G({}, l, { onEndAnimation: m, isComplete: s }));
              default:
                return null;
            }
          }),
          q = ["onEndAnimation"];
        function U() {
          return (
            (U =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var l in a) Object.prototype.hasOwnProperty.call(a, l) && (e[l] = a[l]);
                }
                return e;
              }),
            U.apply(this, arguments)
          );
        }
        const Q = (0, r.memo)((e) => {
          let t = e.onEndAnimation,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                l,
                i = {},
                r = Object.keys(e);
              for (l = 0; l < r.length; l++) ((a = r[l]), t.indexOf(a) >= 0 || (i[a] = e[a]));
              return i;
            })(e, q);
          const l = (0, r.useRef)({}),
            i = (0, r.useCallback)(() => {
              ((l.current.from = void 0), t && t());
            }, [t]),
            s = "number" == typeof l.current.from ? l.current.from : a.from;
          return (
            (l.current.from = s),
            n().createElement(V, U({}, a, { onEndAnimation: i, key: `${s}-${a.to}`, from: s }))
          );
        });
        function Y() {
          return (
            (Y =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var l in a) Object.prototype.hasOwnProperty.call(a, l) && (e[l] = a[l]);
                }
                return e;
              }),
            Y.apply(this, arguments)
          );
        }
        const Z = (0, r.memo)(
            ({
              size: e,
              value: t,
              lineRef: a,
              disabled: l,
              deltaFrom: i,
              animationSettings: r,
              onEndAnimation: s,
              onChangeAnimationState: o,
              onComplete: m,
            }) => {
              if (i === t)
                return n().createElement(y, {
                  key: `${i}-${t}`,
                  size: e,
                  value: t,
                  lineRef: a,
                  disabled: l,
                  onComplete: m,
                });
              const _ = {
                from: i,
                to: t,
                size: e,
                lineRef: a,
                disabled: l,
                animationSettings: r,
                onComplete: m,
                onEndAnimation: s,
                onChangeAnimationState: o,
              };
              return r.withStack
                ? n().createElement(Q, _)
                : n().createElement(V, Y({ key: `${i}-${t}` }, _));
            },
          ),
          J = (e) => ({
            "--progress-base": `url(${e.bgImageBase})`,
            "--progress-line-base": e.line.bgColorBase,
            "--progress-line-disabled": e.line.bgColorDisabled,
            "--progress-line-finished": e.line.bgColorFinished,
            "--progress-pattern-base": `url(${e.pattern.bgImageBase})`,
            "--progress-pattern-disabled": `url(${e.pattern.bgImageDisabled})`,
            "--progress-pattern-finished": `url(${e.pattern.bgImageFinished})`,
            "--progress-glow": `url('${e.glow}')`,
            "--progress-glow-small": `url('${e.glowSmall}')`,
            "--progress-delta-color": e.delta.color,
            "--progress-delta-shadow": e.delta.shadow,
          }),
          K = (e, t, a) => (a < e ? e : a > t ? t : a),
          X = (e, t, a) => {
            if ("number" == typeof a) {
              return (K(0, t, a) / t) * 100;
            }
            return e;
          },
          ee = {
            bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_grey",
            line: {
              bgColorBase: "#f50",
              bgColorDisabled: "transparent",
              bgColorFinished: "#59a011",
            },
            pattern: {
              bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_orange",
              bgImageDisabled: "R.images.gui.maps.icons.components.progress_bar.pattern_disabled",
              bgImageFinished: "R.images.gui.maps.icons.components.progress_bar.pattern_green",
            },
            glow: "R.images.gui.maps.icons.components.progress_bar.glow",
            glowSmall: "R.images.gui.maps.icons.components.progress_bar.glow_small",
            delta: {
              color: "#ffc",
              shadow:
                "0 0 4px 1px #ffaa0066, 0 0 9px 1px #ffaa0066, 0 0 12px 2px #ff550066, 0 0 12px 4px #ff000066",
            },
          },
          te = {
            freezed: !1,
            withStack: !1,
            type: f.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          ae = (0, r.memo)(
            ({
              maxValue: e = 100,
              theme: t = ee,
              size: a = v.Default,
              animationSettings: l = te,
              disabled: s = !1,
              withoutBackground: o = !1,
              progressBarBackgroundClassMix: m,
              value: _,
              deltaFrom: d,
              lineRef: c,
              onChangeAnimationState: g,
              onEndAnimation: h,
              onComplete: u,
            }) => {
              const b = ((e, t, a) =>
                (0, r.useMemo)(() => {
                  const l = (K(0, t, e) / t) * 100;
                  return { value: l, deltaFrom: X(l, t, a) };
                }, [a, t, e]))(_, e, d);
              return n().createElement(
                "div",
                { className: i()(p.base, p[`base__${a}`]), style: J(t) },
                !o && n().createElement(E, { size: a, classMix: m }),
                n().createElement(Z, {
                  size: a,
                  lineRef: c,
                  disabled: s,
                  value: b.value,
                  deltaFrom: b.deltaFrom,
                  animationSettings: l,
                  onEndAnimation: h,
                  onChangeAnimationState: g,
                  onComplete: u,
                }),
              );
            },
          ),
          le = {
            base: "EmblemProgressBar_base_5c",
            base__small: "EmblemProgressBar_base__small_6c",
            base__completed: "EmblemProgressBar_base__completed_6d",
            hideProgress: "EmblemProgressBar_hideProgress_18",
            base__completePostProgression: "EmblemProgressBar_base__completePostProgression_20",
            base__hidden: "EmblemProgressBar_base__hidden_8b",
            hideLevel: "EmblemProgressBar_hideLevel_1e",
            showLevel: "EmblemProgressBar_showLevel_5d",
            hideLevelSmall: "EmblemProgressBar_hideLevelSmall_ae",
            showLevelSmall: "EmblemProgressBar_showLevelSmall_df",
            hideLevelMicro: "EmblemProgressBar_hideLevelMicro_13",
            showLevelMicro: "EmblemProgressBar_showLevelMicro_ae",
            showIcon: "EmblemProgressBar_showIcon_55",
            showIconSmall: "EmblemProgressBar_showIconSmall_26",
            showIconMicro: "EmblemProgressBar_showIconMicro_78",
          },
          ie = (0, r.memo)(
            ({
              progression: e,
              isNoVehicles: t = !1,
              showProgressionCompleted: a,
              isProgressionCompleted: l,
              size: r,
            }) => {
              const s = i()(
                le.base,
                le[`base__${r}`],
                a && le.base__completed,
                !a && l && le.base__hidden,
              );
              return n().createElement(
                "div",
                { className: s },
                n().createElement(ae, {
                  key: e.to,
                  size: v.Small,
                  value: e.to || 0,
                  deltaFrom: e.from || 0,
                  disabled: t,
                }),
              );
            },
          );
        function re() {
          return (
            (re =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var l in a) Object.prototype.hasOwnProperty.call(a, l) && (e[l] = a[l]);
                }
                return e;
              }),
            re.apply(this, arguments)
          );
        }
        (0, r.memo)((e) => {
          const t = e.progression,
            a = e.size,
            l = e.battlePassState,
            r = e.hasBattlePass,
            m = e.isChapterChosen,
            _ = e.hasBeenActive,
            d = void 0 !== _ && _,
            c = e.isChapterSelection,
            g = void 0 !== c && c,
            u = e.isOpen,
            b = void 0 !== u && u,
            p = e.isProgression,
            v = void 0 !== p && p,
            f = e.showProgressBar,
            E = void 0 === f || f,
            x = e.chapterType,
            L = e.chapterID;
          let S = "",
            P = "",
            y = "";
          a === h.$u.Small
            ? ((S = "Small"), (P = "__small"), (y = "_small"))
            : a === h.$u.Micro && ((S = "Micro"), (P = "__micro"), (y = "_micro"));
          const $ = b ? "Open" : "",
            M = l === h.Bq.CompletedRightNow,
            C = r || l === h.Bq.Bought,
            B = (l === h.Bq.Completed || M) && C,
            k = (l === h.Bq.Completed || M) && !C,
            O = B || k,
            W = i()(
              o.image,
              o[`image${P}`],
              b && o[`image__open${S}`],
              C && o[`image__battlePass${S}${$}`],
              l === h.Bq.AwaitSeason && o[`image__seasonWaiting${S}`],
              k && o[`image__completedFree${S}${$}`],
            ),
            R = i()(o[`${x}`], o[`${x}${P}`]),
            z = void 0 !== t.from,
            I = E && ((z && m) || d);
          return n().createElement(
            "div",
            { className: o.base },
            n().createElement("div", { className: R }),
            n().createElement(
              "div",
              { className: W, style: (0, s.FL)(L, y, b, C) },
              l !== h.Bq.AwaitSeason &&
                n().createElement(
                  n().Fragment,
                  null,
                  n().createElement(
                    w,
                    re(
                      {
                        hasProgression: z,
                        isGolden: C,
                        isProgressionCompleted: O,
                        isChapterChosen: m,
                        hasBeenActive: d,
                        isChapterSelection: g,
                        isProgression: v,
                      },
                      e,
                      t,
                    ),
                  ),
                  I &&
                    n().createElement(ie, {
                      key: t.to,
                      progression: t,
                      showProgressionCompleted: M,
                      isProgressionCompleted: O,
                      size: a,
                    }),
                ),
            ),
          );
        });
      },
      8546: (e, t, a) => {
        let l, i, r, n;
        (a.d(t, { $u: () => l, Bq: () => r }),
          (function (e) {
            ((e.Micro = "micro"), (e.Small = "small"), (e.Medium = "medium"));
          })(l || (l = {})),
          (function (e) {
            ((e.ACTIVE = "active"), (e.COMPLETED = "completed"), (e.NOT_CHOSEN = "notChosen"));
          })(i || (i = {})),
          (function (e) {
            ((e.AwaitSeason = "awaitSeason"),
              (e.Bought = "bought"),
              (e.Free = "free"),
              (e.Completed = "completed"),
              (e.CompletedRightNow = "completedRightNow"),
              (e.SwitchedChapterRightNow = "switchedChapterRightNow"),
              (e.NoVehiclesBase = "noVehiclesBase"),
              (e.ChapterNotChosen = "chapterNotChosen"));
          })(r || (r = {})),
          (function (e) {
            ((e.None = ""),
              (e.ShowLevel = "show"),
              (e.HideLevel = "hide"),
              (e.HideLevelWithDelay = "hideWithDelay"));
          })(n || (n = {})));
      },
    },
    a = {};
  function l(e) {
    var i = a[e];
    if (void 0 !== i) return i.exports;
    var r = (a[e] = { exports: {} });
    return (t[e](r, r.exports, l), r.exports);
  }
  ((l.m = t),
    (e = []),
    (l.O = (t, a, i, r) => {
      if (!a) {
        var n = 1 / 0;
        for (_ = 0; _ < e.length; _++) {
          for (var [a, i, r] = e[_], s = !0, o = 0; o < a.length; o++)
            (!1 & r || n >= r) && Object.keys(l.O).every((e) => l.O[e](a[o]))
              ? a.splice(o--, 1)
              : ((s = !1), r < n && (n = r));
          if (s) {
            e.splice(_--, 1);
            var m = i();
            void 0 !== m && (t = m);
          }
        }
        return t;
      }
      r = r || 0;
      for (var _ = e.length; _ > 0 && e[_ - 1][2] > r; _--) e[_] = e[_ - 1];
      e[_] = [a, i, r];
    }),
    (l.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (l.d(t, { a: t }), t);
    }),
    (l.d = (e, t) => {
      for (var a in t)
        l.o(t, a) && !l.o(e, a) && Object.defineProperty(e, a, { enumerable: !0, get: t[a] });
    }),
    (l.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (l.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t)),
    (l.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (l.j = 1730),
    (() => {
      var e = { 1730: 0 };
      l.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var i,
            r,
            [n, s, o] = a,
            m = 0;
          if (n.some((t) => 0 !== e[t])) {
            for (i in s) l.o(s, i) && (l.m[i] = s[i]);
            if (o) var _ = o(l);
          }
          for (t && t(a); m < n.length; m++)
            ((r = n[m]), l.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return l.O(_);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var i = l.O(void 0, [1519], () => l(9830));
  i = l.O(i);
})();
