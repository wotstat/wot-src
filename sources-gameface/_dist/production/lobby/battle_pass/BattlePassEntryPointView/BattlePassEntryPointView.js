(() => {
  var __webpack_modules__ = {
      3495: (e, t, u) => {
        "use strict";
        u.d(t, { Y: () => m });
        var a = u(3138),
          r = u(6179),
          n = u(1043),
          o = u(5262);
        const l = a.O.client.getSize("rem"),
          i = l.width,
          s = l.height,
          _ = Object.assign({ width: i, height: s }, (0, o.T)(i, s, n.j)),
          m = (0, r.createContext)(_);
      },
      1039: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => _ });
        var a = u(6179),
          r = u.n(a),
          n = u(6536),
          o = u(3495),
          l = u(1043),
          i = u(5262),
          s = u(3138);
        const _ = (0, a.memo)(({ children: e }) => {
          const t = (0, a.useContext)(o.Y),
            u = (0, a.useState)(t),
            _ = u[0],
            m = u[1],
            c = (0, a.useCallback)((e, t) => {
              const u = s.O.view.pxToRem(e),
                a = s.O.view.pxToRem(t);
              m(Object.assign({ width: u, height: a }, (0, i.T)(u, a, l.j)));
            }, []);
          ((0, n.Z)(() => {
            engine.on("clientResized", c);
          }),
            (0, a.useEffect)(() => () => engine.off("clientResized", c), [c]));
          const E = (0, a.useMemo)(() => Object.assign({}, _), [_]);
          return r().createElement(o.Y.Provider, { value: E }, e);
        });
      },
      6010: (e, t, u) => {
        "use strict";
        var a = u(6179),
          r = u(7382),
          n = u(3495);
        const o = ["children"];
        const l = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, o);
          const l = (0, a.useContext)(n.Y),
            i = l.extraLarge,
            s = l.large,
            _ = l.medium,
            m = l.small,
            c = l.extraSmall,
            E = l.extraLargeWidth,
            d = l.largeWidth,
            A = l.mediumWidth,
            g = l.smallWidth,
            h = l.extraSmallWidth,
            p = l.extraLargeHeight,
            F = l.largeHeight,
            C = l.mediumHeight,
            B = l.smallHeight,
            b = l.extraSmallHeight,
            S = { extraLarge: p, large: F, medium: C, small: B, extraSmall: b };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && i) return t;
            if (u.large && s) return t;
            if (u.medium && _) return t;
            if (u.small && m) return t;
            if (u.extraSmall && c) return t;
          } else {
            if (u.extraLargeWidth && E) return (0, r.H)(t, u, S);
            if (u.largeWidth && d) return (0, r.H)(t, u, S);
            if (u.mediumWidth && A) return (0, r.H)(t, u, S);
            if (u.smallWidth && g) return (0, r.H)(t, u, S);
            if (u.extraSmallWidth && h) return (0, r.H)(t, u, S);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && p) return t;
              if (u.largeHeight && F) return t;
              if (u.mediumHeight && C) return t;
              if (u.smallHeight && B) return t;
              if (u.extraSmallHeight && b) return t;
            }
          }
          return null;
        };
        l.defaultProps = {
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
        (0, a.memo)(l);
      },
      7382: (e, t, u) => {
        "use strict";
        u.d(t, { H: () => a });
        const a = (e, t, u) =>
          t.extraLargeHeight ||
          t.largeHeight ||
          t.mediumHeight ||
          t.smallHeight ||
          t.extraSmallHeight
            ? (t.extraLargeHeight && u.extraLarge) ||
              (t.largeHeight && u.large) ||
              (t.mediumHeight && u.medium) ||
              (t.smallHeight && u.small) ||
              (t.extraSmallHeight && u.extraSmall)
              ? e
              : null
            : e;
      },
      7739: (e, t, u) => {
        "use strict";
        u.d(t, { YN: () => r.Y, ZN: () => a.Z });
        u(6010);
        var a = u(1039),
          r = u(3495);
      },
      1043: (e, t, u) => {
        "use strict";
        u.d(t, { j: () => a });
        const a = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, u) => {
        "use strict";
        var a;
        function r(e, t, u) {
          const a = (function (e, t) {
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
            })(e, u),
            r = (function (e, t) {
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
            })(t, u),
            n = Math.min(a, r);
          return {
            extraLarge: n === u.extraLarge.weight,
            large: n === u.large.weight,
            medium: n === u.medium.weight,
            small: n === u.small.weight,
            extraSmall: n === u.extraSmall.weight,
            extraLargeWidth: a === u.extraLarge.weight,
            largeWidth: a === u.large.weight,
            mediumWidth: a === u.medium.weight,
            smallWidth: a === u.small.weight,
            extraSmallWidth: a === u.extraSmall.weight,
            extraLargeHeight: r === u.extraLarge.weight,
            largeHeight: r === u.large.weight,
            mediumHeight: r === u.medium.weight,
            smallHeight: r === u.small.weight,
            extraSmallHeight: r === u.extraSmall.weight,
          };
        }
        (u.d(t, { T: () => r }),
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
          })(a || (a = {})));
      },
      926: (e) => {
        e.exports = {
          SMALL_WIDTH: "mediaSmallWidth",
          MEDIUM_WIDTH: "mediaMediumWidth",
          LARGE_WIDTH: "mediaLargeWidth",
          EXTRA_LARGE_WIDTH: "mediaExtraLargeWidth",
          SMALL_HEIGHT: "mediaSmallHeight",
          MEDIUM_HEIGHT: "mediaMediumHeight",
          LARGE_HEIGHT: "mediaLargeHeight",
          EXTRA_LARGE_HEIGHT: "mediaExtraLargeHeight",
          SMALL: "mediaSmall",
          MEDIUM: "mediaMedium",
          LARGE: "mediaLarge",
          EXTRA_LARGE: "mediaExtraLarge",
        };
      },
      122: (e, t, u) => {
        "use strict";
        u.d(t, { F: () => a });
        const a = (e, t) => {
          let u;
          const a = setTimeout(() => {
            u = e();
          }, t);
          return () => {
            ("function" == typeof u && u(), clearTimeout(a));
          };
        };
      },
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => l, onResize: () => n }));
        var a = u(2472),
          r = u(1176);
        const n = (0, a.E)("clientResized"),
          o = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const l = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, r.R)(!1);
          }
          function u() {
            e.enabled && (0, r.R)(!0);
          }
          function a() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", u))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", u))
              : (0, r.R)(!1);
          }
          const n = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let r = !0;
                  const n = `mouse${t}`,
                    l = o[t]((e) => u([e, "outside"]));
                  function i(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(n, i),
                    a(),
                    () => {
                      r &&
                        (l(), window.removeEventListener(n, i), (e.listeners -= 1), a(), (r = !1));
                    }
                  );
                };
              })(u)),
              t
            ),
            {},
          );
          return Object.assign({}, n, {
            disable() {
              ((e.enabled = !1), a());
            },
            enable() {
              ((e.enabled = !0), a());
            },
            enableOutside() {
              e.enabled && (0, r.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, r.R)(!1);
            },
          });
        })();
      },
      5959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => a,
            getMouseGlobalPosition: () => n,
            getSize: () => r,
            graphicsQuality: () => o,
          }));
        var a = u(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function n(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const o = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, u) => {
        "use strict";
        function a(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => a });
      },
      2472: (e, t, u) => {
        "use strict";
        function a(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        u.d(t, { E: () => a });
      },
      3138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => r });
        var a = u(5959);
        const r = { view: u(7641), client: a };
      },
      3722: (e, t, u) => {
        "use strict";
        function a(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function r(e, t, u) {
          return `url(${a(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => r, getTextureUrl: () => a }));
      },
      6112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => r });
        var a = u(2472);
        const r = {
          onTextureFrozen: (0, a.E)("self.onTextureFrozen"),
          onTextureReady: (0, a.E)("self.onTextureReady"),
          onDomBuilt: (0, a.E)("self.onDomBuilt"),
          onLoaded: (0, a.E)("self.onLoaded"),
          onDisplayChanged: (0, a.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, a.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, a.E)("children.onAdded"),
            onLoaded: (0, a.E)("children.onLoaded"),
            onRemoved: (0, a.E)("children.onRemoved"),
            onAttached: (0, a.E)("children.onAttached"),
            onTextureReady: (0, a.E)("children.onTextureReady"),
            onRequestPosition: (0, a.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => _,
            addPreloadTexture: () => l,
            children: () => a,
            displayStatus: () => r.W,
            displayStatusIs: () => v,
            events: () => n.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => D,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => f,
            getScale: () => g,
            getSize: () => c,
            getViewGlobalPosition: () => d,
            isClientAccessible: () => B,
            isEventHandled: () => S,
            isFocused: () => C,
            pxToRem: () => h,
            remToPx: () => p,
            resize: () => E,
            sendEvent: () => o.qP,
            setAnimateWindow: () => F,
            setEventHandled: () => b,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => L,
          }));
        var a = u(3722),
          r = u(6112),
          n = u(6538),
          o = u(8566);
        function l(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function s(e, t, u, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, a);
        }
        function _(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function c(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function E(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function d(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: p(t.x), y: p(t.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function g() {
          return viewEnv.getScale();
        }
        function h(e) {
          return viewEnv.pxToRem(e);
        }
        function p(e) {
          return viewEnv.remToPx(e);
        }
        function F(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function B() {
          return viewEnv.isClientAccessible();
        }
        function b() {
          return viewEnv.setEventHandled();
        }
        function S() {
          return viewEnv.isEventHandled();
        }
        function D() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const v = Object.keys(r.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === r.W[t]), e),
            {},
          ),
          w = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          L = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : n.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => s });
        const a = ["args"];
        const r = 2,
          n = 16,
          o = 32,
          l = 64,
          i = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const n = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, a);
              return void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, o, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, t]) => {
                          const u = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: u, name: e, number: t };
                            case "boolean":
                              return { __Type: u, name: e, bool: t };
                            default:
                              return { __Type: u, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: u, type: e });
            var r;
          },
          s = {
            close(e) {
              i("popover" === e ? r : o);
            },
            minimize() {
              i(l);
            },
            move(e) {
              i(n, { isMouseEvent: !0, on: e });
            },
          };
      },
      6536: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => r });
        var a = u(6179);
        const r = (e) => {
          const t = (0, a.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      5415: (e, t, u) => {
        "use strict";
        u.d(t, { Aq: () => i, GS: () => s, cJ: () => o, fd: () => l });
        var a = u(6179),
          r = u(7739),
          n = u(1043);
        let o, l, i;
        (!(function (e) {
          ((e[(e.ExtraSmall = n.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = n.j.small.width)] = "Small"),
            (e[(e.Medium = n.j.medium.width)] = "Medium"),
            (e[(e.Large = n.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = n.j.extraLarge.width)] = "ExtraLarge"));
        })(o || (o = {})),
          (function (e) {
            ((e[(e.ExtraSmall = n.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = n.j.small.width)] = "Small"),
              (e[(e.Medium = n.j.medium.width)] = "Medium"),
              (e[(e.Large = n.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = n.j.extraLarge.width)] = "ExtraLarge"));
          })(l || (l = {})),
          (function (e) {
            ((e[(e.ExtraSmall = n.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = n.j.small.height)] = "Small"),
              (e[(e.Medium = n.j.medium.height)] = "Medium"),
              (e[(e.Large = n.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = n.j.extraLarge.height)] = "ExtraLarge"));
          })(i || (i = {})));
        const s = () => {
          const e = (0, a.useContext)(r.YN),
            t = e.width,
            u = e.height,
            n = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return o.ExtraLarge;
                case e.large:
                  return o.Large;
                case e.medium:
                  return o.Medium;
                case e.small:
                  return o.Small;
                case e.extraSmall:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(e),
            s = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return l.ExtraLarge;
                case e.largeWidth:
                  return l.Large;
                case e.mediumWidth:
                  return l.Medium;
                case e.smallWidth:
                  return l.Small;
                case e.extraSmallWidth:
                  return l.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), l.ExtraSmall);
              }
            })(e),
            _ = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return i.ExtraLarge;
                case e.largeHeight:
                  return i.Large;
                case e.mediumHeight:
                  return i.Medium;
                case e.smallHeight:
                  return i.Small;
                case e.extraSmallHeight:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: n,
            mediaWidth: s,
            mediaHeight: _,
            remScreenWidth: t,
            remScreenHeight: u,
          };
        };
      },
      5521: (e, t, u) => {
        "use strict";
        let a, r;
        (u.d(t, { n: () => a }),
          (function (e) {
            ((e[(e.NONE = -1)] = "NONE"),
              (e[(e.ALT = 165)] = "ALT"),
              (e[(e.ENTER = 13)] = "ENTER"),
              (e[(e.ESCAPE = 27)] = "ESCAPE"),
              (e[(e.SPACE = 32)] = "SPACE"),
              (e[(e.END = 35)] = "END"),
              (e[(e.HOME = 36)] = "HOME"),
              (e[(e.ARROW_LEFT = 37)] = "ARROW_LEFT"),
              (e[(e.ARROW_UP = 38)] = "ARROW_UP"),
              (e[(e.ARROW_RIGHT = 39)] = "ARROW_RIGHT"),
              (e[(e.ARROW_DOWN = 40)] = "ARROW_DOWN"),
              (e[(e.NUM_PLUS = 107)] = "NUM_PLUS"),
              (e[(e.NUM_MINUS = 109)] = "NUM_MINUS"),
              (e[(e.PLUS = 187)] = "PLUS"),
              (e[(e.MINUS = 189)] = "MINUS"),
              (e[(e.PAGE_UP = 33)] = "PAGE_UP"),
              (e[(e.PAGE_DOWN = 34)] = "PAGE_DOWN"),
              (e[(e.BACKSPACE = 8)] = "BACKSPACE"),
              (e[(e.DELETE = 46)] = "DELETE"),
              (e[(e.TAB = 9)] = "TAB"),
              (e[(e.KEY_N = 78)] = "KEY_N"),
              (e[(e.KEY_0 = 48)] = "KEY_0"),
              (e[(e.KEY_1 = 49)] = "KEY_1"),
              (e[(e.KEY_2 = 50)] = "KEY_2"),
              (e[(e.KEY_3 = 51)] = "KEY_3"),
              (e[(e.KEY_4 = 52)] = "KEY_4"),
              (e[(e.KEY_5 = 53)] = "KEY_5"),
              (e[(e.KEY_6 = 54)] = "KEY_6"),
              (e[(e.KEY_7 = 55)] = "KEY_7"),
              (e[(e.KEY_8 = 56)] = "KEY_8"),
              (e[(e.KEY_9 = 57)] = "KEY_9"),
              (e[(e.CAPS_LOCK = 20)] = "CAPS_LOCK"),
              (e[(e.INSERT = 45)] = "INSERT"),
              (e[(e.F1 = 112)] = "F1"),
              (e[(e.F2 = 113)] = "F2"),
              (e[(e.F3 = 114)] = "F3"),
              (e[(e.F4 = 115)] = "F4"),
              (e[(e.F5 = 116)] = "F5"),
              (e[(e.F6 = 117)] = "F6"),
              (e[(e.F7 = 118)] = "F7"),
              (e[(e.F8 = 119)] = "F8"),
              (e[(e.F9 = 120)] = "F9"),
              (e[(e.F10 = 121)] = "F10"),
              (e[(e.F11 = 122)] = "F11"),
              (e[(e.F12 = 123)] = "F12"),
              (e[(e.SELECT = 93)] = "SELECT"),
              (e[(e.NUMPAD_0 = 96)] = "NUMPAD_0"),
              (e[(e.NUMPAD_1 = 97)] = "NUMPAD_1"),
              (e[(e.NUMPAD_2 = 98)] = "NUMPAD_2"),
              (e[(e.NUMPAD_3 = 99)] = "NUMPAD_3"),
              (e[(e.NUMPAD_4 = 100)] = "NUMPAD_4"),
              (e[(e.NUMPAD_5 = 101)] = "NUMPAD_5"),
              (e[(e.NUMPAD_6 = 102)] = "NUMPAD_6"),
              (e[(e.NUMPAD_7 = 103)] = "NUMPAD_7"),
              (e[(e.NUMPAD_8 = 104)] = "NUMPAD_8"),
              (e[(e.NUMPAD_9 = 105)] = "NUMPAD_9"),
              (e[(e.NUM_DECIMAL = 110)] = "NUM_DECIMAL"),
              (e[(e.STAR = 106)] = "STAR"),
              (e[(e.NUM_SLASH = 111)] = "NUM_SLASH"),
              (e[(e.FORWARD_SLASH = 191)] = "FORWARD_SLASH"),
              (e[(e.COMMA = 188)] = "COMMA"),
              (e[(e.DASH = 189)] = "DASH"),
              (e[(e.PERIOD = 190)] = "PERIOD"));
          })(a || (a = {})),
          (function (e) {
            ((e.ALT = "Alt"),
              (e.ALT_GRAPH = "AltGraph"),
              (e.CAPS_LOCK = "CapsLock"),
              (e.CONTROL = "Control"),
              (e.FN = "Fn"),
              (e.FN_LOCK = "FnLock"),
              (e.META = "Meta"),
              (e.NUM_LOCK = "NumLock"),
              (e.SCROLL_LOCK = "ScrollLock"),
              (e.SHIFT = "Shift"),
              (e.SYMBOL = "Symbol"),
              (e.SYMBOL_LOCK = "SymbolLock"));
          })(r || (r = {})));
      },
      1358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
        var a = u(3138);
        class r {
          constructor() {
            ((this._callbacks = void 0),
              (this._updateHandler = void 0),
              (this._views = void 0),
              (this.clearViewCallbacks = (e) => {
                this._views[e] &&
                  (this._views[e].forEach((e) => {
                    delete this._callbacks[e];
                  }),
                  delete this._views[e]);
              }),
              (this._callbacks = {}),
              (this._views = {}),
              (this._updateHandler = void 0));
          }
          static get instance() {
            return (window.__dataTracker || (window.__dataTracker = new r()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, t, u = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const n = a.O.view.addModelObserver(e, u, r);
            return (
              n > 0
                ? ((this._callbacks[n] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(n) : (this._views[u] = [n])))
                : console.error("Can't add callback for model:", e),
              n
            );
          }
          removeCallback(e, t = 0) {
            let u = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((u = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              u || console.error("Can't remove callback by id:", e),
              u
            );
          }
          _emmitDataChanged(e, t, u) {
            u.forEach((u) => {
              const a = this._callbacks[u];
              void 0 !== a && a(e, t);
            });
          }
        }
        r.__instance = void 0;
        const n = r;
      },
      7572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(1358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(4179);
        class ViewModel {
          constructor(path, watchingFields = []) {
            ((this.dataTracker = void 0),
              (this.modelPath = void 0),
              (this.callbacks = void 0),
              (this.data = void 0),
              (this._notifyObservers = () => {
                ((this.data = eval(this.modelPath)),
                  this.callbacks.forEach((e) => {
                    e(this.data);
                  }));
              }),
              (this.dataTracker = new _DataTracker__WEBPACK_IMPORTED_MODULE_0__.Z()),
              (this.modelPath = path),
              (this.callbacks = new Set()),
              (0, _index__WEBPACK_IMPORTED_MODULE_1__.ry)().then(() => {
                (this._addCallback(path),
                  watchingFields.forEach((e) => {
                    this._addCallback(path + "." + e);
                  }),
                  this._notifyObservers());
              }));
          }
          subscribe(e) {
            (this.callbacks.add(e), null !== this.data && void 0 !== this.data && e(this.data));
          }
          unsubscribe(e) {
            this.callbacks.delete(e);
          }
          destroy() {
            (this.dataTracker.clear(), this.callbacks.clear());
          }
          _addCallback(e) {
            this.dataTracker.addCallback(e, this._notifyObservers);
          }
        }
        const __WEBPACK_DEFAULT_EXPORT__ = ViewModel;
      },
      4179: (e, t, u) => {
        "use strict";
        u.d(t, { Sw: () => n.Z, B3: () => s, Z5: () => o, B0: () => i, ry: () => p });
        class a {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: u }) => {
                  let a = e.target;
                  do {
                    if (a === t) return;
                    a = a.parentNode;
                  } while (a);
                  u();
                });
              }));
          }
          static get instance() {
            return (a.__instance || (a.__instance = new a()), a.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const u = e,
              a = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== u || t !== a,
            )),
              this.removeMouseListener());
          }
          addMouseListener() {
            this._listenMouse ||
              (document.addEventListener("mousedown", this.onMouseDown), (this._listenMouse = !0));
          }
          removeMouseListener() {
            this._listenMouse &&
              0 === this.entries.length &&
              (document.removeEventListener("mousedown", this.onMouseDown),
              (this._listenMouse = !1));
          }
        }
        a.__instance = void 0;
        const r = a;
        var n = u(1358);
        const o = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          l = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, u) => userLocale.getTimeFormat(e, t, void 0 === u || u),
            getTimeString: (e, t, u) => userLocale.getTimeString(e, t, void 0 === u || u),
          };
        let i;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(i || (i = {}));
        const s = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          _ = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          c = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = u(5521),
          d = u(3138);
        const A = ["args"];
        function g(e, t, u, a, r, n, o) {
          try {
            var l = e[n](o),
              i = l.value;
          } catch (e) {
            return void u(e);
          }
          l.done ? t(i) : Promise.resolve(i).then(a, r);
        }
        const h = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          p = (function () {
            var e,
              t =
                ((e = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((e) => {
                      engine.on("Ready", e);
                    })
                  );
                }),
                function () {
                  var t = this,
                    u = arguments;
                  return new Promise(function (a, r) {
                    var n = e.apply(t, u);
                    function o(e) {
                      g(n, a, r, o, l, "next", e);
                    }
                    function l(e) {
                      g(n, a, r, o, l, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          F = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                n = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, n, {
                      arguments:
                        ((a = r),
                        Object.entries(a).map(([e, t]) => {
                          const u = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              u.number = t;
                              break;
                            case "boolean":
                              u.bool = t;
                              break;
                            default:
                              u.string = t.toString();
                          }
                          return u;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, n));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var a;
          },
          C = () => F(i.CLOSE),
          B = (e, t) => {
            e.keyCode === E.n.ESCAPE && t();
          };
        var b = u(7572);
        const S = r.instance,
          D = {
            DataTracker: n.Z,
            ViewModel: b.Z,
            ViewEventType: i,
            NumberFormatType: s,
            RealFormatType: _,
            TimeFormatType: m,
            DateFormatType: c,
            makeGlobalBoundingBox: h,
            sendMoveEvent: (e) => F(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => F(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, u = 0) => {
              F(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, u, a, r = R.invalid("resId"), n) => {
              const o = d.O.view.getViewGlobalPosition(),
                l = u.getBoundingClientRect(),
                s = l.x,
                _ = l.y,
                m = l.width,
                c = l.height,
                E = {
                  x: d.O.view.pxToRem(s) + o.x,
                  y: d.O.view.pxToRem(_) + o.y,
                  width: d.O.view.pxToRem(m),
                  height: d.O.view.pxToRem(c),
                };
              F(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: r,
                direction: t,
                bbox: h(E),
                on: !0,
                args: n,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => B(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              B(e, C);
            },
            handleViewEvent: F,
            onBindingsReady: p,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const a in t)
                if (Object.prototype.hasOwnProperty.call(t, a)) {
                  const r = Object.prototype.toString.call(t[a]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = t[a];
                    u[a] = [];
                    for (let t = 0; t < r.length; t++) u[a].push({ value: e(r[t].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[a] = e(t[a]))
                      : (u[a] = t[a]);
                }
              return u;
            },
            ClickOutsideManager: S,
            SystemLocale: o,
            UserLocale: l,
          };
        window.ViewEnvHelper = D;
      },
      7265: (e, t, u) => {
        "use strict";
        var a = u(6179),
          r = u.n(a),
          n = u(493),
          o = u.n(n),
          l = u(7739),
          i = u(6483),
          s = u.n(i),
          _ = u(926),
          m = u.n(_),
          c = u(5415);
        const E = ["children", "className"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        const A = {
            [c.fd.ExtraSmall]: "",
            [c.fd.Small]: m().SMALL_WIDTH,
            [c.fd.Medium]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH}`,
            [c.fd.Large]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH}`,
            [c.fd.ExtraLarge]:
              `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH} ${m().EXTRA_LARGE_WIDTH}`,
          },
          g = {
            [c.Aq.ExtraSmall]: "",
            [c.Aq.Small]: m().SMALL_HEIGHT,
            [c.Aq.Medium]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT}`,
            [c.Aq.Large]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT}`,
            [c.Aq.ExtraLarge]:
              `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT} ${m().EXTRA_LARGE_HEIGHT}`,
          },
          h = {
            [c.cJ.ExtraSmall]: "",
            [c.cJ.Small]: m().SMALL,
            [c.cJ.Medium]: `${m().SMALL} ${m().MEDIUM}`,
            [c.cJ.Large]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE}`,
            [c.cJ.ExtraLarge]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE} ${m().EXTRA_LARGE}`,
          },
          p = (e) => {
            let t = e.children,
              u = e.className,
              a = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, E);
            const n = (0, c.GS)(),
              o = n.mediaWidth,
              l = n.mediaHeight,
              i = n.mediaSize;
            return r().createElement("div", d({ className: s()(u, A[o], g[l], h[i]) }, a), t);
          },
          F = ["children"];
        const C = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, F);
            return r().createElement(l.ZN, null, r().createElement(p, u, t));
          },
          B = 33,
          b = 0,
          S = !0,
          D = "play";
        function f(e) {
          const t = e.chunk,
            u = t.rows * t.columns;
          return (a) => {
            const r = a % u,
              n = (r % t.columns) * e.width,
              o = Math.trunc(r / t.columns) * e.height;
            return { path: e.getChunkPath(Math.trunc(a / u)), x: n, y: o };
          };
        }
        const v = [
          "width",
          "height",
          "getImageSource",
          "frameCount",
          "onAnimate",
          "frameTime",
          "initialFrameIndex",
          "lastFrameIndex",
          "loop",
          "state",
          "onAnimationDone",
          "onAnimationComplete",
          "poster",
        ];
        function w() {
          return (
            (w =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            w.apply(this, arguments)
          );
        }
        const L = (0, a.memo)(function (e) {
            let t = e.width,
              u = e.height,
              n = e.getImageSource,
              o = e.frameCount,
              l = e.onAnimate,
              i = e.frameTime,
              s = void 0 === i ? B : i,
              _ = e.initialFrameIndex,
              m = void 0 === _ ? b : _,
              c = e.lastFrameIndex,
              E = void 0 === c ? o - 1 : c,
              d = e.loop,
              A = void 0 === d ? S : d,
              g = e.state,
              h = void 0 === g ? D : g,
              p = e.onAnimationDone,
              F = e.onAnimationComplete,
              C = e.poster,
              f = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, v);
            const L = (0, a.useRef)(null);
            return (
              (0, a.useEffect)(() => {
                const e = L.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  u = (u) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(u.img, -u.x, -u.y));
                  };
                switch (h) {
                  case "play":
                    return (function () {
                      const e = y(m, E, n),
                        t = P(m, E),
                        a = window.setInterval(() => {
                          const r = t(),
                            n = e.get(r);
                          n
                            ? (null == l || l(r, n),
                              u(n),
                              r === E &&
                                (null == F || F(),
                                A || (null == p || p(), window.clearInterval(a))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, s);
                      return () => window.clearInterval(a);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === m && C ? { path: C, x: 0, y: 0 } : n(m),
                        t = new Image();
                      t.src = e.path;
                      const a = () => u(O(e, t));
                      return (
                        t.addEventListener("load", a),
                        () => t.removeEventListener("load", a)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [s, n, m, E, A, l, F, p, C, h]),
              r().createElement("canvas", w({}, f, { width: t, height: u, ref: L }))
            );
          }),
          P = (e, t) => {
            let u = e;
            return () => {
              const a = u;
              return ((u += 1), u > t && (u = e), a);
            };
          },
          O = (e, t) => Object.assign({}, e, { img: t }),
          y = (e, t, u) => {
            const a = new Map(),
              r = {};
            for (let n = e; n <= t; n++) {
              const e = u(n),
                t = r[e.path];
              if (t) a.set(n, O(e, t));
              else {
                const t = new Image();
                ((r[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${n})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  a.set(n, O(e, t)));
              }
            }
            return a;
          };
        let T, I, M;
        (!(function (e) {
          ((e.NORMAL = "normal"),
            (e.NEW_LEVEL = "newLevel"),
            (e.BUY_BATTLE_PASS = "buyBattlePass"),
            (e.NOT_TAKEN_REWARDS = "notTakenRewards"),
            (e.PROGRESSION_COMPLETED = "progressionCompleted"),
            (e.NEW_CHAPTER = "newChapter"),
            (e.CHANGE_PROGRESS = "changeProgress"),
            (e.CHAPTER_NOT_CHOSEN = "chapterNotChosen"));
        })(T || (T = {})),
          (function (e) {
            ((e.DISABLED = "disabled"),
              (e.SEASON_WAITING = "seasonWaiting"),
              (e.NORMAL = "normal"),
              (e.ATTENTION = "attention"));
          })(I || (I = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(M || (M = {})));
        const x = (e) => {
          let t,
            u = null;
          return (
            (u = requestAnimationFrame(() => {
              u = requestAnimationFrame(() => {
                ((u = null), (t = e()));
              });
            })),
            () => {
              ("function" == typeof t && t(), null !== u && cancelAnimationFrame(u));
            }
          );
        };
        var N = u(3138);
        const k = () => {
            const e = (0, a.useState)(N.O.view.getScale()),
              t = e[0],
              u = e[1];
            return (
              (0, a.useEffect)(() => {
                const e = () => {
                  u(N.O.view.getScale());
                };
                return (
                  window.addEventListener("resize", e),
                  () => {
                    window.removeEventListener("resize", e);
                  }
                );
              }, []),
              t
            );
          },
          H = (e = 1) => {
            const t = new Error().stack;
            let u,
              a = R.invalid("resId");
            return (
              t &&
                ((u = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                window.__feature &&
                  window.__feature !== u &&
                  window.subViews[u] &&
                  (a = window.subViews[u].id)),
              { caller: u, stack: t, resId: a }
            );
          },
          U = (e, t) => e.split(".").reduce((e, t) => e && e[t], t);
        var W = u(6536),
          $ = u(4179);
        const G = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          j = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          z = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, u) => {
                const a = U(`${e}.${u}`, window);
                return G(a) ? t(e, u, a) : `${e}.${u}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          V = (e) => {
            const t = ((e) => {
                const t = H(),
                  u = t.caller,
                  a = t.resId,
                  r = window.__feature && window.__feature !== u && u ? `subViews.${u}` : "";
                return { modelPrefix: r, modelPath: j(r, e || ""), resId: a };
              })(),
              u = t.modelPrefix,
              a = e.split(".");
            if (a.length > 0) {
              const e = [a[0]];
              return (
                a.reduce((t, a) => {
                  const r = U(j(u, `${t}.${a}`), window);
                  return G(r) ? (e.push(r.id), `${t}.${a}.value`) : (e.push(a), `${t}.${a}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          q = $.Sw.instance;
        let X;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(X || (X = {}));
        const Y = (e = "model", t = X.Deep) => {
            const u = (0, a.useState)(0),
              r = (u[0], u[1]),
              n = (0, a.useMemo)(() => H(), []),
              o = n.caller,
              l = n.resId,
              i = (0, a.useMemo)(
                () => (window.__feature && window.__feature !== o ? `subViews.${o}.${e}` : e),
                [o, e],
              ),
              s = (0, a.useState)(() =>
                ((e) => {
                  const t = U(e, window);
                  for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                  return G(t) ? t.value : t;
                })(z(i)),
              ),
              _ = s[0],
              m = s[1],
              c = (0, a.useRef)(-1);
            return (
              (0, W.Z)(() => {
                if (
                  ("boolean" == typeof t &&
                    ((t = t ? X.Deep : X.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  t !== X.None)
                ) {
                  const u = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      t === X.Deep
                        ? (e === _ && r((e) => e + 1), m(e))
                        : m(Object.assign([], e));
                    },
                    a = V(e);
                  c.current = q.addCallback(a, u, l, t === X.Deep);
                }
              }),
              (0, a.useEffect)(() => {
                if (t !== X.None)
                  return () => {
                    q.removeCallback(c.current, l);
                  };
              }, [l, t]),
              _
            );
          },
          K = "display",
          Z = "enabled",
          Q = "enabled_change";
        var J = u(3403);
        function ee() {
          return !1;
        }
        console.log;
        var te = u(9174);
        function ue(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return ae(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return ae(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function ae(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, a = new Array(t); u < t; u++) a[u] = e[u];
          return a;
        }
        const re = (e) => (0 === e ? window : window.subViews.get(e));
        function ne(e, t) {
          var u;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (u = e[t]) ? void 0 : u.value;
        }
        const oe = ne;
        var le = u(3946);
        let ie, se;
        (!(function (e) {
          ((e.style = "style"),
            (e.tankman = "tankman"),
            (e.vehicle = "vehicle"),
            (e.mixed = "mixed"));
        })(ie || (ie = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(se || (se = {})));
        (ie.style, ie.tankman);
        const _e = ((e, t) => {
            const u = (0, a.createContext)({});
            return [
              function ({ mode: n = "real", options: o, children: l, mocks: i }) {
                const s = (0, a.useRef)([]),
                  _ = (u, a, r) => {
                    var n;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: u = re,
                        context: a = "model",
                      } = {}) {
                        const r = new Map();
                        function n(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, u) => {
                            u.forEach((t) => {
                              const u = r.get(t);
                              void 0 !== u && u(e);
                            });
                          });
                        });
                        const o = (e) => {
                          const r = u(t),
                            n = a.split(".").reduce((e, t) => e[t], r);
                          return "string" != typeof e || 0 === e.length
                            ? n
                            : e.split(".").reduce((e, t) => {
                                const u = e[t];
                                return "function" == typeof u ? u.bind(e) : u;
                              }, n);
                        };
                        return {
                          subscribe: (u, n) => {
                            const l = "string" == typeof n ? `${a}.${n}` : a,
                              i = N.O.view.addModelObserver(l, t, !0);
                            return (r.set(i, u), e && u(o(n)), i);
                          },
                          readByPath: o,
                          createCallback: (e, t) => {
                            const u = o(t);
                            return (...t) => {
                              u(e(...t));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const t = o(e);
                            return () => {
                              t();
                            };
                          },
                          dispose: function () {
                            for (var e, u = ue(r.keys()); !(e = u()).done;) n(e.value, t);
                          },
                          unsubscribe: n,
                        };
                      })(a),
                      l =
                        "real" === u
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (n = null == r ? void 0 : r.getter) ? n : () => {},
                            }),
                      i = (e) =>
                        "mocks" === u ? (null == r ? void 0 : r.getter(e)) : l.readByPath(e),
                      _ = (e) => s.current.push(e),
                      m = e({
                        mode: u,
                        readByPath: i,
                        externalModel: l,
                        observableModel: {
                          array: (e, t) => {
                            const a = null != t ? t : i(e),
                              r = te.LO.box(a, { equals: ee });
                            return (
                              "real" === u &&
                                l.subscribe(
                                  (0, te.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, t) => {
                            const a = null != t ? t : i(e),
                              r = te.LO.box(a, { equals: ee });
                            return (
                              "real" === u &&
                                l.subscribe(
                                  (0, te.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, t) => {
                            const a = i(t);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, t) => ((e[t] = te.LO.box(a[t], {})), e), {});
                              return (
                                "real" === u &&
                                  l.subscribe(
                                    (0, te.aD)((t) => {
                                      e.forEach((e) => {
                                        r[e].set(t[e]);
                                      });
                                    }),
                                    t,
                                  ),
                                r
                              );
                            }
                            {
                              const r = e,
                                n = Object.entries(r),
                                o = n.reduce((e, [t, u]) => ((e[u] = te.LO.box(a[t], {})), e), {});
                              return (
                                "real" === u &&
                                  l.subscribe(
                                    (0, te.aD)((e) => {
                                      n.forEach(([t, u]) => {
                                        o[u].set(e[t]);
                                      });
                                    }),
                                    t,
                                  ),
                                o
                              );
                            }
                          },
                        },
                        cleanup: _,
                      }),
                      c = { mode: u, model: m, externalModel: l, cleanup: _ };
                    return {
                      model: m,
                      controls: "mocks" === u && r ? r.controls(c) : t(c),
                      externalModel: l,
                      mode: u,
                    };
                  },
                  m = (0, a.useRef)(!1),
                  c = (0, a.useState)(n),
                  E = c[0],
                  d = c[1],
                  A = (0, a.useState)(() => _(n, o, i)),
                  g = A[0],
                  h = A[1];
                return (
                  (0, a.useEffect)(() => {
                    m.current ? h(_(E, o, i)) : (m.current = !0);
                  }, [i, E, o]),
                  (0, a.useEffect)(() => {
                    d(n);
                  }, [n]),
                  (0, a.useEffect)(
                    () => () => {
                      (g.externalModel.dispose(), s.current.forEach((e) => e()));
                    },
                    [g],
                  ),
                  r().createElement(u.Provider, { value: g }, l)
                );
              },
              () => (0, a.useContext)(u),
            ];
          })(
            ({ observableModel: e }) => {
              const t = { root: e.object(), chapterTypes: e.array("availableChapterTypes") },
                u = (0, le.Om)(
                  () => {
                    return (
                      (e = t.chapterTypes.get()),
                      (u = (e) => e),
                      Array.isArray(e)
                        ? e.map(u)
                        : e.map((e, t, a) => u(null == e ? void 0 : e.value, t, a))
                    );
                    var e, u;
                  },
                  { equals: ee },
                ),
                a = (0, le.Om)(
                  () =>
                    (function (e, t) {
                      if (Array.isArray(e)) return e.some(t);
                      for (let u = 0; u < e.length; u++) if (t(oe(e, u), u, e)) return !0;
                      return !1;
                    })(t.chapterTypes.get(), (e) => e === se.Marathon),
                  { equals: ee },
                );
              return Object.assign({}, t, {
                computes: { getAvailableChapterTypes: u, hasMarathon: a },
              });
            },
            ({ externalModel: e }) => ({ openBattlePass: e.createCallbackNoArgs("onClick") }),
          ),
          me = _e[0],
          ce = _e[1],
          Ee = [
            "children",
            "contentId",
            "args",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onClick",
            "ignoreShowDelay",
            "ignoreMouseClick",
            "decoratorId",
            "isEnabled",
            "targetId",
            "onShow",
            "onHide",
          ];
        function de(e) {
          return Object.entries(e || {}).map(([e, t]) => {
            const u = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                u.number = t;
                break;
              case "boolean":
                u.bool = t;
                break;
              case "undefined":
                break;
              default:
                u.string = t.toString();
            }
            return u;
          });
        }
        const Ae = (e, t, u = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: $.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: a,
                },
                u,
              ),
            );
          },
          ge = (e) => {
            let t = e.children,
              u = e.contentId,
              r = e.args,
              n = e.onMouseEnter,
              o = e.onMouseLeave,
              l = e.onMouseDown,
              i = e.onClick,
              s = e.ignoreShowDelay,
              _ = void 0 !== s && s,
              m = e.ignoreMouseClick,
              c = void 0 !== m && m,
              E = e.decoratorId,
              d = void 0 === E ? 0 : E,
              A = e.isEnabled,
              g = void 0 === A || A,
              h = e.targetId,
              p = void 0 === h ? 0 : h,
              F = e.onShow,
              C = e.onHide,
              B = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Ee);
            const b = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, a.useMemo)(() => p || H().resId, [p]),
              D = (0, a.useCallback)(() => {
                (b.current.isVisible && b.current.timeoutId) ||
                  (Ae(u, d, { isMouseEvent: !0, on: !0, arguments: de(r) }, S),
                  F && F(),
                  (b.current.isVisible = !0));
              }, [u, d, r, S, F]),
              f = (0, a.useCallback)(() => {
                if (b.current.isVisible || b.current.timeoutId) {
                  const e = b.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (b.current.timeoutId = 0)),
                    Ae(u, d, { on: !1 }, S),
                    b.current.isVisible && C && C(),
                    (b.current.isVisible = !1));
                }
              }, [u, d, S, C]),
              v = (0, a.useCallback)((e) => {
                b.current.isVisible &&
                  ((b.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (b.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(b.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = b.current.hideTimerId;
              return (
                document.addEventListener("wheel", v, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", v, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === g && f();
              }, [g, f]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", f),
                  () => {
                    (window.removeEventListener("mouseleave", f), f());
                  }
                ),
                [f],
              ));
            return g
              ? (0, a.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((w = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((b.current.timeoutId = window.setTimeout(D, _ ? 100 : 400)),
                            n && n(e),
                            w && w(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (f(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === c && f(), null == i || i(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === c && f(), null == l || l(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    B,
                  ),
                )
              : t;
            var w;
          },
          he = (e) => {
            const t = (0, a.useRef)();
            return (
              (0, a.useEffect)(() => {
                t.current = e;
              }, [e]),
              t.current
            );
          };
        let pe;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(pe || (pe = {}));
        (() => {
          const e = new RegExp(
            /[\(\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?[ %\+\x2D-9A-Za-\{\}\xA0\xC0-\u0237\u2013\u2014\u2026]+[\)\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3002\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\uFF01\uFF0C\uFF1A\uFF1B\uFF1F\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?/gmu
              .source +
              "|" +
              /[\(\xAB\u201C\u275D][\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}][\0-\u2E7F\u2E9A\u2EF4-\u2EFF\u2FD6-\u3004\u3006\u3008-\u3020\u302A-\u3037\u303C-\u33FF\u4DC0-\u4DFF\uA000-\uF8FF\uFA6E\uFA6F\uFADA-\u{16FE1}\u{16FE4}-\u{16FEF}\u{16FF2}-\u{1FFFF}\u{2A6E0}-\u{2A6FF}\u{2B739}-\u{2B73F}\u{2B81E}\u{2B81F}\u{2CEA2}-\u{2CEAF}\u{2EBE1}-\u{2F7FF}\u{2FA1E}-\u{2FFFF}\u{3134B}-\u{10FFFF}]?|[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}][\0-\u2E7F\u2E9A\u2EF4-\u2EFF\u2FD6-\u3004\u3006\u3008-\u3020\u302A-\u3037\u303C-\u33FF\u4DC0-\u4DFF\uA000-\uF8FF\uFA6E\uFA6F\uFADA-\u{16FE1}\u{16FE4}-\u{16FEF}\u{16FF2}-\u{1FFFF}\u{2A6E0}-\u{2A6FF}\u{2B739}-\u{2B73F}\u{2B81E}\u{2B81F}\u{2CEA2}-\u{2CEAF}\u{2EBE1}-\u{2F7FF}\u{2FA1E}-\u{2FFFF}\u{3134B}-\u{10FFFF}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?[\)\xBB\u201D\u275E][\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?/gmu
                .source +
              "|" +
              /[A-Za-z\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0560-\u0588\u05D0-\u05EA\u05EF-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u0860-\u086A\u0870-\u0887\u0889-\u088E\u08A0-\u08C9\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u09FC\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0AF9\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58-\u0C5A\u0C5D\u0C60\u0C61\u0C80\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D04-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D54-\u0D56\u0D5F-\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F5\u13F8-\u13FD\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16F1-\u16F8\u1700-\u1711\u171F-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1878\u1880-\u1884\u1887-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4C\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1C80-\u1C88\u1C90-\u1CBA\u1CBD-\u1CBF\u1CE9-\u1CEC\u1CEE-\u1CF3\u1CF5\u1CF6\u1CFA\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312F\u3131-\u318E\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DBF\u4E00-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA8FD\uA8FE\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB69\uAB70-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC\u{10000}-\u{1000B}\u{1000D}-\u{10026}\u{10028}-\u{1003A}\u{1003C}\u{1003D}\u{1003F}-\u{1004D}\u{10050}-\u{1005D}\u{10080}-\u{100FA}\u{10280}-\u{1029C}\u{102A0}-\u{102D0}\u{10300}-\u{1031F}\u{1032D}-\u{10340}\u{10342}-\u{10349}\u{10350}-\u{10375}\u{10380}-\u{1039D}\u{103A0}-\u{103C3}\u{103C8}-\u{103CF}\u{10400}-\u{1049D}\u{104B0}-\u{104D3}\u{104D8}-\u{104FB}\u{10500}-\u{10527}\u{10530}-\u{10563}\u{10570}-\u{1057A}\u{1057C}-\u{1058A}\u{1058C}-\u{10592}\u{10594}\u{10595}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10600}-\u{10736}\u{10740}-\u{10755}\u{10760}-\u{10767}\u{10780}-\u{10785}\u{10787}-\u{107B0}\u{107B2}-\u{107BA}\u{10800}-\u{10805}\u{10808}\u{1080A}-\u{10835}\u{10837}\u{10838}\u{1083C}\u{1083F}-\u{10855}\u{10860}-\u{10876}\u{10880}-\u{1089E}\u{108E0}-\u{108F2}\u{108F4}\u{108F5}\u{10900}-\u{10915}\u{10920}-\u{10939}\u{10980}-\u{109B7}\u{109BE}\u{109BF}\u{10A00}\u{10A10}-\u{10A13}\u{10A15}-\u{10A17}\u{10A19}-\u{10A35}\u{10A60}-\u{10A7C}\u{10A80}-\u{10A9C}\u{10AC0}-\u{10AC7}\u{10AC9}-\u{10AE4}\u{10B00}-\u{10B35}\u{10B40}-\u{10B55}\u{10B60}-\u{10B72}\u{10B80}-\u{10B91}\u{10C00}-\u{10C48}\u{10C80}-\u{10CB2}\u{10CC0}-\u{10CF2}\u{10D00}-\u{10D23}\u{10E80}-\u{10EA9}\u{10EB0}\u{10EB1}\u{10F00}-\u{10F1C}\u{10F27}\u{10F30}-\u{10F45}\u{10F70}-\u{10F81}\u{10FB0}-\u{10FC4}\u{10FE0}-\u{10FF6}\u{11003}-\u{11037}\u{11071}\u{11072}\u{11075}\u{11083}-\u{110AF}\u{110D0}-\u{110E8}\u{11103}-\u{11126}\u{11144}\u{11147}\u{11150}-\u{11172}\u{11176}\u{11183}-\u{111B2}\u{111C1}-\u{111C4}\u{111DA}\u{111DC}\u{11200}-\u{11211}\u{11213}-\u{1122B}\u{11280}-\u{11286}\u{11288}\u{1128A}-\u{1128D}\u{1128F}-\u{1129D}\u{1129F}-\u{112A8}\u{112B0}-\u{112DE}\u{11305}-\u{1130C}\u{1130F}\u{11310}\u{11313}-\u{11328}\u{1132A}-\u{11330}\u{11332}\u{11333}\u{11335}-\u{11339}\u{1133D}\u{11350}\u{1135D}-\u{11361}\u{11400}-\u{11434}\u{11447}-\u{1144A}\u{1145F}-\u{11461}\u{11480}-\u{114AF}\u{114C4}\u{114C5}\u{114C7}\u{11580}-\u{115AE}\u{115D8}-\u{115DB}\u{11600}-\u{1162F}\u{11644}\u{11680}-\u{116AA}\u{116B8}\u{11700}-\u{1171A}\u{11740}-\u{11746}\u{11800}-\u{1182B}\u{118A0}-\u{118DF}\u{118FF}-\u{11906}\u{11909}\u{1190C}-\u{11913}\u{11915}\u{11916}\u{11918}-\u{1192F}\u{1193F}\u{11941}\u{119A0}-\u{119A7}\u{119AA}-\u{119D0}\u{119E1}\u{119E3}\u{11A00}\u{11A0B}-\u{11A32}\u{11A3A}\u{11A50}\u{11A5C}-\u{11A89}\u{11A9D}\u{11AB0}-\u{11AF8}\u{11C00}-\u{11C08}\u{11C0A}-\u{11C2E}\u{11C40}\u{11C72}-\u{11C8F}\u{11D00}-\u{11D06}\u{11D08}\u{11D09}\u{11D0B}-\u{11D30}\u{11D46}\u{11D60}-\u{11D65}\u{11D67}\u{11D68}\u{11D6A}-\u{11D89}\u{11D98}\u{11EE0}-\u{11EF2}\u{11FB0}\u{12000}-\u{12399}\u{12480}-\u{12543}\u{12F90}-\u{12FF0}\u{13000}-\u{1342E}\u{14400}-\u{14646}\u{16800}-\u{16A38}\u{16A40}-\u{16A5E}\u{16A70}-\u{16ABE}\u{16AD0}-\u{16AED}\u{16B00}-\u{16B2F}\u{16B40}-\u{16B43}\u{16B63}-\u{16B77}\u{16B7D}-\u{16B8F}\u{16E40}-\u{16E7F}\u{16F00}-\u{16F4A}\u{16F50}\u{16F93}-\u{16F9F}\u{16FE0}\u{16FE1}\u{16FE3}\u{17000}-\u{187F7}\u{18800}-\u{18CD5}\u{18D00}-\u{18D08}\u{1AFF0}-\u{1AFF3}\u{1AFF5}-\u{1AFFB}\u{1AFFD}\u{1AFFE}\u{1B000}-\u{1B122}\u{1B150}-\u{1B152}\u{1B164}-\u{1B167}\u{1B170}-\u{1B2FB}\u{1BC00}-\u{1BC6A}\u{1BC70}-\u{1BC7C}\u{1BC80}-\u{1BC88}\u{1BC90}-\u{1BC99}\u{1D400}-\u{1D454}\u{1D456}-\u{1D49C}\u{1D49E}\u{1D49F}\u{1D4A2}\u{1D4A5}\u{1D4A6}\u{1D4A9}-\u{1D4AC}\u{1D4AE}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D505}\u{1D507}-\u{1D50A}\u{1D50D}-\u{1D514}\u{1D516}-\u{1D51C}\u{1D51E}-\u{1D539}\u{1D53B}-\u{1D53E}\u{1D540}-\u{1D544}\u{1D546}\u{1D54A}-\u{1D550}\u{1D552}-\u{1D6A5}\u{1D6A8}-\u{1D6C0}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6FA}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D734}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D76E}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D7A8}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7CB}\u{1DF00}-\u{1DF1E}\u{1E100}-\u{1E12C}\u{1E137}-\u{1E13D}\u{1E14E}\u{1E290}-\u{1E2AD}\u{1E2C0}-\u{1E2EB}\u{1E7E0}-\u{1E7E6}\u{1E7E8}-\u{1E7EB}\u{1E7ED}\u{1E7EE}\u{1E7F0}-\u{1E7FE}\u{1E800}-\u{1E8C4}\u{1E900}-\u{1E943}\u{1E94B}\u{1EE00}-\u{1EE03}\u{1EE05}-\u{1EE1F}\u{1EE21}\u{1EE22}\u{1EE24}\u{1EE27}\u{1EE29}-\u{1EE32}\u{1EE34}-\u{1EE37}\u{1EE39}\u{1EE3B}\u{1EE42}\u{1EE47}\u{1EE49}\u{1EE4B}\u{1EE4D}-\u{1EE4F}\u{1EE51}\u{1EE52}\u{1EE54}\u{1EE57}\u{1EE59}\u{1EE5B}\u{1EE5D}\u{1EE5F}\u{1EE61}\u{1EE62}\u{1EE64}\u{1EE67}-\u{1EE6A}\u{1EE6C}-\u{1EE72}\u{1EE74}-\u{1EE77}\u{1EE79}-\u{1EE7C}\u{1EE7E}\u{1EE80}-\u{1EE89}\u{1EE8B}-\u{1EE9B}\u{1EEA1}-\u{1EEA3}\u{1EEA5}-\u{1EEA9}\u{1EEAB}-\u{1EEBB}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[ \):;\u2022\u3001\u3002\u300A-\u300D\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]|[\(,1A-Za-\{\}\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0560-\u0588\u05D0-\u05EA\u05EF-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u0860-\u086A\u0870-\u0887\u0889-\u088E\u08A0-\u08C9\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u09FC\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0AF9\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58-\u0C5A\u0C5D\u0C60\u0C61\u0C80\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D04-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D54-\u0D56\u0D5F-\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F5\u13F8-\u13FD\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16F1-\u16F8\u1700-\u1711\u171F-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1878\u1880-\u1884\u1887-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4C\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1C80-\u1C88\u1C90-\u1CBA\u1CBD-\u1CBF\u1CE9-\u1CEC\u1CEE-\u1CF3\u1CF5\u1CF6\u1CFA\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312F\u3131-\u318E\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DBF\u4E00-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA8FD\uA8FE\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB69\uAB70-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC\u{10000}-\u{1000B}\u{1000D}-\u{10026}\u{10028}-\u{1003A}\u{1003C}\u{1003D}\u{1003F}-\u{1004D}\u{10050}-\u{1005D}\u{10080}-\u{100FA}\u{10280}-\u{1029C}\u{102A0}-\u{102D0}\u{10300}-\u{1031F}\u{1032D}-\u{10340}\u{10342}-\u{10349}\u{10350}-\u{10375}\u{10380}-\u{1039D}\u{103A0}-\u{103C3}\u{103C8}-\u{103CF}\u{10400}-\u{1049D}\u{104B0}-\u{104D3}\u{104D8}-\u{104FB}\u{10500}-\u{10527}\u{10530}-\u{10563}\u{10570}-\u{1057A}\u{1057C}-\u{1058A}\u{1058C}-\u{10592}\u{10594}\u{10595}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10600}-\u{10736}\u{10740}-\u{10755}\u{10760}-\u{10767}\u{10780}-\u{10785}\u{10787}-\u{107B0}\u{107B2}-\u{107BA}\u{10800}-\u{10805}\u{10808}\u{1080A}-\u{10835}\u{10837}\u{10838}\u{1083C}\u{1083F}-\u{10855}\u{10860}-\u{10876}\u{10880}-\u{1089E}\u{108E0}-\u{108F2}\u{108F4}\u{108F5}\u{10900}-\u{10915}\u{10920}-\u{10939}\u{10980}-\u{109B7}\u{109BE}\u{109BF}\u{10A00}\u{10A10}-\u{10A13}\u{10A15}-\u{10A17}\u{10A19}-\u{10A35}\u{10A60}-\u{10A7C}\u{10A80}-\u{10A9C}\u{10AC0}-\u{10AC7}\u{10AC9}-\u{10AE4}\u{10B00}-\u{10B35}\u{10B40}-\u{10B55}\u{10B60}-\u{10B72}\u{10B80}-\u{10B91}\u{10C00}-\u{10C48}\u{10C80}-\u{10CB2}\u{10CC0}-\u{10CF2}\u{10D00}-\u{10D23}\u{10E80}-\u{10EA9}\u{10EB0}\u{10EB1}\u{10F00}-\u{10F1C}\u{10F27}\u{10F30}-\u{10F45}\u{10F70}-\u{10F81}\u{10FB0}-\u{10FC4}\u{10FE0}-\u{10FF6}\u{11003}-\u{11037}\u{11071}\u{11072}\u{11075}\u{11083}-\u{110AF}\u{110D0}-\u{110E8}\u{11103}-\u{11126}\u{11144}\u{11147}\u{11150}-\u{11172}\u{11176}\u{11183}-\u{111B2}\u{111C1}-\u{111C4}\u{111DA}\u{111DC}\u{11200}-\u{11211}\u{11213}-\u{1122B}\u{11280}-\u{11286}\u{11288}\u{1128A}-\u{1128D}\u{1128F}-\u{1129D}\u{1129F}-\u{112A8}\u{112B0}-\u{112DE}\u{11305}-\u{1130C}\u{1130F}\u{11310}\u{11313}-\u{11328}\u{1132A}-\u{11330}\u{11332}\u{11333}\u{11335}-\u{11339}\u{1133D}\u{11350}\u{1135D}-\u{11361}\u{11400}-\u{11434}\u{11447}-\u{1144A}\u{1145F}-\u{11461}\u{11480}-\u{114AF}\u{114C4}\u{114C5}\u{114C7}\u{11580}-\u{115AE}\u{115D8}-\u{115DB}\u{11600}-\u{1162F}\u{11644}\u{11680}-\u{116AA}\u{116B8}\u{11700}-\u{1171A}\u{11740}-\u{11746}\u{11800}-\u{1182B}\u{118A0}-\u{118DF}\u{118FF}-\u{11906}\u{11909}\u{1190C}-\u{11913}\u{11915}\u{11916}\u{11918}-\u{1192F}\u{1193F}\u{11941}\u{119A0}-\u{119A7}\u{119AA}-\u{119D0}\u{119E1}\u{119E3}\u{11A00}\u{11A0B}-\u{11A32}\u{11A3A}\u{11A50}\u{11A5C}-\u{11A89}\u{11A9D}\u{11AB0}-\u{11AF8}\u{11C00}-\u{11C08}\u{11C0A}-\u{11C2E}\u{11C40}\u{11C72}-\u{11C8F}\u{11D00}-\u{11D06}\u{11D08}\u{11D09}\u{11D0B}-\u{11D30}\u{11D46}\u{11D60}-\u{11D65}\u{11D67}\u{11D68}\u{11D6A}-\u{11D89}\u{11D98}\u{11EE0}-\u{11EF2}\u{11FB0}\u{12000}-\u{12399}\u{12480}-\u{12543}\u{12F90}-\u{12FF0}\u{13000}-\u{1342E}\u{14400}-\u{14646}\u{16800}-\u{16A38}\u{16A40}-\u{16A5E}\u{16A70}-\u{16ABE}\u{16AD0}-\u{16AED}\u{16B00}-\u{16B2F}\u{16B40}-\u{16B43}\u{16B63}-\u{16B77}\u{16B7D}-\u{16B8F}\u{16E40}-\u{16E7F}\u{16F00}-\u{16F4A}\u{16F50}\u{16F93}-\u{16F9F}\u{16FE0}\u{16FE1}\u{16FE3}\u{17000}-\u{187F7}\u{18800}-\u{18CD5}\u{18D00}-\u{18D08}\u{1AFF0}-\u{1AFF3}\u{1AFF5}-\u{1AFFB}\u{1AFFD}\u{1AFFE}\u{1B000}-\u{1B122}\u{1B150}-\u{1B152}\u{1B164}-\u{1B167}\u{1B170}-\u{1B2FB}\u{1BC00}-\u{1BC6A}\u{1BC70}-\u{1BC7C}\u{1BC80}-\u{1BC88}\u{1BC90}-\u{1BC99}\u{1D400}-\u{1D454}\u{1D456}-\u{1D49C}\u{1D49E}\u{1D49F}\u{1D4A2}\u{1D4A5}\u{1D4A6}\u{1D4A9}-\u{1D4AC}\u{1D4AE}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D505}\u{1D507}-\u{1D50A}\u{1D50D}-\u{1D514}\u{1D516}-\u{1D51C}\u{1D51E}-\u{1D539}\u{1D53B}-\u{1D53E}\u{1D540}-\u{1D544}\u{1D546}\u{1D54A}-\u{1D550}\u{1D552}-\u{1D6A5}\u{1D6A8}-\u{1D6C0}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6FA}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D734}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D76E}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D7A8}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7CB}\u{1DF00}-\u{1DF1E}\u{1E100}-\u{1E12C}\u{1E137}-\u{1E13D}\u{1E14E}\u{1E290}-\u{1E2AD}\u{1E2C0}-\u{1E2EB}\u{1E7E0}-\u{1E7E6}\u{1E7E8}-\u{1E7EB}\u{1E7ED}\u{1E7EE}\u{1E7F0}-\u{1E7FE}\u{1E800}-\u{1E8C4}\u{1E900}-\u{1E943}\u{1E94B}\u{1EE00}-\u{1EE03}\u{1EE05}-\u{1EE1F}\u{1EE21}\u{1EE22}\u{1EE24}\u{1EE27}\u{1EE29}-\u{1EE32}\u{1EE34}-\u{1EE37}\u{1EE39}\u{1EE3B}\u{1EE42}\u{1EE47}\u{1EE49}\u{1EE4B}\u{1EE4D}-\u{1EE4F}\u{1EE51}\u{1EE52}\u{1EE54}\u{1EE57}\u{1EE59}\u{1EE5B}\u{1EE5D}\u{1EE5F}\u{1EE61}\u{1EE62}\u{1EE64}\u{1EE67}-\u{1EE6A}\u{1EE6C}-\u{1EE72}\u{1EE74}-\u{1EE77}\u{1EE79}-\u{1EE7C}\u{1EE7E}\u{1EE80}-\u{1EE89}\u{1EE8B}-\u{1EE9B}\u{1EEA1}-\u{1EEA3}\u{1EEA5}-\u{1EEA9}\u{1EEAB}-\u{1EEBB}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]/gmu
                .source +
              "|" +
              /[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]/gmu
                .source,
            "gum",
          );
        })();
        let Fe;
        !(function (e) {
          ((e.SHORT_DATE = "short-date"),
            (e.SHORT_TIME = "short-time"),
            (e.SHORT_DATE_TIME = "short-date-time"),
            (e.FULL_DATE = "full-date"),
            (e.FULL_DATE_TIME = "full-date-time"),
            (e.MONTH = "month"),
            (e.MONTH_DATE = "month-date"),
            (e.DATE_MONTH = "date-month"),
            (e.MONTH_YEAR = "month-year"),
            (e.WEEK_DAY = "week-day"),
            (e.WEEK_DAY_TIME = "week-day-time"),
            (e.YEAR = "year"),
            (e.DATE_YEAR = "date-year"));
        })(Fe || (Fe = {}));
        Date.now();
        $.Sw.instance;
        const Ce = he,
          Be = [];
        function be(e) {
          const t = (0, a.useRef)(e);
          return (
            (0, a.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, a.useCallback)((...e) => (0, t.current)(...e), Be)
          );
        }
        function Se(e) {
          engine.call("PlaySound", e);
        }
        let De, fe, ve, we;
        (!(function (e) {
          ((e.HangarView = "hangar"),
            (e.BattlePassProgression = "battle_pass_progression"),
            (e.CollectionProgression = "collection_progression"));
        })(De || (De = {})),
          (function (e) {
            ((e.CollectionEntryPointView = "collection_entry_point_view"),
              (e.BattlePassCollectionEntryPoint = "battle_pass_collection_entry_point"),
              (e.CollectionProgressTooltip = "collection_progress_tooltip"));
          })(fe || (fe = {})),
          (function (e) {
            e.Click = "click";
          })(ve || (ve = {})),
          (function (e) {
            ((e[(e.NonSet = 0)] = "NonSet"),
              (e[(e.Debug = 10)] = "Debug"),
              (e[(e.Info = 20)] = "Info"),
              (e[(e.Warning = 30)] = "Warning"));
          })(we || (we = {})));
        let Le;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(Le || (Le = {}));
        const Pe = "metrics",
          Oe = ({ partnerID: e, item: t, parentScreen: u, itemState: a, info: r }) => ({
            item: t,
            partnerID: e || null,
            parent_screen: u || null,
            item_state: a || null,
            additional_info: r || null,
          }),
          ye = (e, t) => {
            const u = (0, a.useCallback)(
              (u, a = we.Info, r) => {
                (r || (r = {}),
                  Object.keys(r).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: t,
                      action: u,
                      logLevel: a,
                      params: JSON.stringify(r),
                    }));
              },
              [e, t],
            );
            return (e, t, a) => u(e, t, a);
          },
          Te = "Blink_base_88",
          Ie = "Blink_shadowWrapper_49",
          Me = "Blink_blinkWrapper_33",
          xe = "Blink_blinkInner_82",
          Ne = "Blink_blink_68",
          Re = (0, J.Pi)(({ isInfinite: e = !1, children: t }) => {
            const u = ce().model.root.get().isSmall,
              a = e ? "infinite" : 1;
            return r().createElement(
              "div",
              { className: Te },
              r().createElement("div", {
                className: Ie,
                style: {
                  maskImage: `url('R.images.gui.maps.icons.battlePass.logo.full_widget_mask${u ? "_small" : ""}')`,
                  animationIterationCount: a,
                },
              }),
              r().createElement(
                "div",
                {
                  className: Me,
                  style: {
                    maskImage: `url('R.images.gui.maps.icons.battlePass.logo.widget_mask${u ? "_small" : ""}')`,
                  },
                },
                r().createElement(
                  "div",
                  { className: xe, style: { animationIterationCount: a } },
                  r().createElement("div", { className: Ne }),
                ),
              ),
              t,
            );
          });
        var ke = u(122),
          He = u(903);
        let Ue, We, $e, Ge, je, ze, Ve, qe, Xe;
        (!(function (e) {
          ((e.Items = "items"),
            (e.Equipment = "equipment"),
            (e.Xp = "xp"),
            (e.XpFactor = "xpFactor"),
            (e.Blueprints = "blueprints"),
            (e.BlueprintsAny = "blueprintsAny"),
            (e.Goodies = "goodies"),
            (e.Berths = "berths"),
            (e.Slots = "slots"),
            (e.Tokens = "tokens"),
            (e.CrewSkins = "crewSkins"),
            (e.CrewBooks = "crewBooks"),
            (e.Customizations = "customizations"),
            (e.CreditsFactor = "creditsFactor"),
            (e.Currency = "currency"),
            (e.TankmenXp = "tankmenXP"),
            (e.TankmenXpFactor = "tankmenXPFactor"),
            (e.FreeXpFactor = "freeXPFactor"),
            (e.BattleToken = "battleToken"),
            (e.PremiumUniversal = "premium_universal"),
            (e.Gold = "gold"),
            (e.Credits = "credits"),
            (e.Crystal = "crystal"),
            (e.FreeXp = "freeXP"),
            (e.Premium = "premium"),
            (e.PremiumPlus = "premium_plus"),
            (e.BattlePassPoints = "battlePassPoints"),
            (e.BattlePassSelectToken = "battlePassSelectToken"),
            (e.SelectableBonus = "selectableBonus"),
            (e.StyleProgressToken = "styleProgressToken"),
            (e.TmanToken = "tmanToken"),
            (e.NaturalCover = "naturalCover"),
            (e.BpCoin = "bpcoin"),
            (e.BattlaPassFinalAchievement = "dossier_achievement"),
            (e.BattleBadge = "dossier_badge"),
            (e.NewYearAlbumsAccess = "newYearAlbumsAccess"),
            (e.NewYearFillers = "ny22Fillers"),
            (e.NewYearInvoice = "newYearInvoice"),
            (e.NewYearToyFragments = "ny22ToyFragments"),
            (e.NewYearSlot = "newYearSlot"),
            (e.BonusX5 = "battle_bonus_x5"),
            (e.CrewBonusX3 = "crew_bonus_x3"),
            (e.Vehicles = "vehicles"),
            (e.EpicSelectToken = "epicSelectToken"),
            (e.CollectionItem = "collectionItem"),
            (e.Comp7TokenWeeklyReward = "comp7TokenWeeklyReward"),
            (e.Comp7TokenCouponReward = "comp7TokenCouponReward"),
            (e.BattleBoosterGift = "battleBooster_gift"),
            (e.CosmicLootboxSilver = "lootBoxToken"),
            (e.CosmicLootboxCommon = "cosmic_2024_2"),
            (e.Branch = "branch"),
            (e.VehicleSelect = "vehicleSelect"),
            (e.StyleProgress = "styleProgress"),
            (e.ParagonsUnlocks = "paragonsUnlocks"),
            (e.LootBoxToken = "lootBoxToken"),
            (e.PostStamp = "giftsystem_5_stamp"),
            (e.Quests = "quests"),
            (e.ArmoryCoin = "armory_coin"),
            (e.PremiumPlusUniversal = "premium_plus_universal"),
            (e.DogTagType = "dogTagComponents"),
            (e.GoldenTicket = "goldenticket"),
            (e.LbStyleProgress = "lbStyleProgress"),
            (e.RewardsSlots = "rewardsSlots"));
        })(Ue || (Ue = {})),
          (function (e) {
            ((e.Gold = "gold"),
              (e.Credits = "credits"),
              (e.Crystal = "crystal"),
              (e.Premium = "premium"),
              (e.PremiumPlus = "premium_plus"),
              (e.Vehicles = "vehicles"),
              (e.Customizations = "customizations"),
              (e.Blueprints = "blueprints"),
              (e.BlueprintsAny = "blueprintsAny"),
              (e.BlueprintsFinal = "finalBlueprints"),
              (e.Goodies = "goodies"),
              (e.CrewSkins = "crewSkins"),
              (e.Xp = "xp"),
              (e.XpFactor = "xpFactor"),
              (e.FreeXp = "freeXP"),
              (e.FreeXPFactor = "freeXPFactor"),
              (e.TankmenXP = "tankmenXP"),
              (e.TankmenXPFactor = "tankmenXPFactor"),
              (e.DailyXPFactor = "dailyXPFactor"),
              (e.CreditsFactor = "creditsFactor"),
              (e.Items = "items"),
              (e.StrBonus = "strBonus"),
              (e.Groups = "groups"),
              (e.Berths = "berths"),
              (e.Slots = "slots"),
              (e.Meta = "meta"),
              (e.Tokens = "tokens"),
              (e.Dossier = "dossier"),
              (e.OneOf = "oneof"),
              (e.PremiumUniversal = "premium_universal"),
              (e.BadgesGroup = "badgesGroup"),
              (e.Entitlements = "entitlements"),
              (e.RankedDailyBattles = "rankedDailyBattles"),
              (e.RankedBonusBattles = "rankedBonusBattles"),
              (e.BattlePassPoints = "battlePassPoints"),
              (e.BattleBadge = "dossier_badge"),
              (e.BattleAchievement = "dossier_achievement"));
          })(We || (We = {})),
          (function (e) {
            ((e.Big = "big"),
              (e.Small = "small"),
              (e.Mini = "mini"),
              (e.S600x450 = "s600x450"),
              (e.S400x300 = "s400x300"),
              (e.S296x222 = "s296x222"),
              (e.S232x174 = "s232x174"),
              (e.S180x135 = "s180x135"),
              (e.S128x100 = "s128x100"),
              (e.S80x80 = "s80x80"),
              (e.S48x48 = "s48x48"));
          })($e || ($e = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(Ge || (Ge = {})),
          (function (e) {
            ((e.BATTLE_BOOSTER = "battleBooster"),
              (e.BATTLE_BOOSTER_REPLACE = "battleBoosterReplace"),
              (e.BUILT_IN_EQUIPMENT = "builtInEquipment"),
              (e.EQUIPMENT_PLUS = "equipmentPlus"),
              (e.EQUIPMENT_TROPHY_BASIC = "equipmentTrophyBasic"),
              (e.EQUIPMENT_TROPHY_UPGRADED = "equipmentTrophyUpgraded"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_1 = "equipmentModernized_1"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_2 = "equipmentModernized_2"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_3 = "equipmentModernized_3"),
              (e.PROGRESSION_STYLE_UPGRADED_1 = "progressionStyleUpgraded_1"),
              (e.PROGRESSION_STYLE_UPGRADED_2 = "progressionStyleUpgraded_2"),
              (e.PROGRESSION_STYLE_UPGRADED_3 = "progressionStyleUpgraded_3"),
              (e.PROGRESSION_STYLE_UPGRADED_4 = "progressionStyleUpgraded_4"));
          })(je || (je = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(ze || (ze = {})),
          (function (e) {
            ((e.BATTLE_BOOSTER = "battleBooster"),
              (e.BATTLE_BOOSTER_REPLACE = "battleBoosterReplace"),
              (e.BUILT_IN_EQUIPMENT = "builtInEquipment"),
              (e.EQUIPMENT_PLUS = "equipmentPlus"),
              (e.EQUIPMENT_TROPHY_BASIC = "equipmentTrophyBasic"),
              (e.EQUIPMENT_TROPHY_UPGRADED = "equipmentTrophyUpgraded"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_1 = "equipmentModernized_1"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_2 = "equipmentModernized_2"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_3 = "equipmentModernized_3"),
              (e.PROGRESSION_STYLE_UPGRADED_1 = "progressionStyleUpgraded_1"),
              (e.PROGRESSION_STYLE_UPGRADED_2 = "progressionStyleUpgraded_2"),
              (e.PROGRESSION_STYLE_UPGRADED_3 = "progressionStyleUpgraded_3"),
              (e.PROGRESSION_STYLE_UPGRADED_4 = "progressionStyleUpgraded_4"));
          })(Ve || (Ve = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(qe || (qe = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Xe || (Xe = {})));
        class Ye extends r().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = $.B3.GOLD;
            else e = $.B3.INTEGRAL;
            const t = $.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        Ye.defaultProps = { format: "integral" };
        (Ue.Items,
          Ue.Equipment,
          Ue.Xp,
          Ue.XpFactor,
          Ue.Blueprints,
          Ue.BlueprintsAny,
          Ue.Goodies,
          Ue.Berths,
          Ue.Slots,
          Ue.Tokens,
          Ue.CrewSkins,
          Ue.CrewBooks,
          Ue.Customizations,
          Ue.CreditsFactor,
          Ue.TankmenXp,
          Ue.TankmenXpFactor,
          Ue.FreeXpFactor,
          Ue.BattleToken,
          Ue.PremiumUniversal,
          Ue.NaturalCover,
          Ue.BpCoin,
          Ue.BattlePassSelectToken,
          Ue.BattlaPassFinalAchievement,
          Ue.BattleBadge,
          Ue.BonusX5,
          Ue.CrewBonusX3,
          Ue.NewYearFillers,
          Ue.NewYearInvoice,
          Ue.EpicSelectToken,
          Ue.Comp7TokenWeeklyReward,
          Ue.Comp7TokenCouponReward,
          Ue.BattleBoosterGift,
          Ue.CosmicLootboxCommon,
          Ue.CosmicLootboxSilver,
          Ue.SelectableBonus,
          Ue.PostStamp,
          Ue.PremiumPlusUniversal,
          Ue.GoldenTicket,
          Ue.RewardsSlots,
          Ue.Gold,
          Ue.Credits,
          Ue.Crystal,
          Ue.FreeXp,
          Ue.BattlePassPoints,
          Ue.PremiumPlus,
          Ue.Premium);
        let Ke;
        !(function (e) {
          ((e.s16 = "16"),
            (e.s32 = "32"),
            (e.s48 = "48"),
            (e.s66 = "66"),
            (e.s80 = "80"),
            (e.s116 = "116"),
            (e.s296 = "296"),
            (e.s360 = "360"),
            (e.s400 = "400"),
            (e.s600 = "600"));
        })(Ke || (Ke = {}));
        let Ze, Qe;
        (!(function (e) {
          ((e.Active = "active"),
            (e.Paused = "paused"),
            (e.Completed = "completed"),
            (e.NotStarted = "notStarted"),
            (e.Disabled = "disabled"));
        })(Ze || (Ze = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(Qe || (Qe = {})));
        var Je = u(8546);
        var et = u(9830);
        const tt = "StateNormal_base_0d",
          ut = "StateNormal_flag_f8",
          at = "StateNormal_base__medium_e3",
          rt = "StateNormal_emblem_0f",
          nt = "StateNormal_counter_cd",
          ot = "StateNormal_chapterLogoIcon_26",
          lt = "StateNormal_base__smallX2_07",
          it = "StateNormal_freePoints_37",
          st = (e, t) => {
            const u = R.images.gui.maps.icons.battlePass.logo.flag,
              a = t ? "m" : "l";
            return { backgroundImage: `url(${(0, He.wD)(u, e, a)})` };
          },
          _t = ({
            chapterID: e,
            isSmall: t,
            scale: u,
            progressionState: n,
            hasBattlePass: o,
            stateClasses: l,
            onFinish: i,
            duration: _,
            progressInfo: m,
            emblem: E,
            notChosenRewardCount: d,
            isSeasonWaiting: A,
            isChapterChosen: g,
            freePoints: h,
            chapterType: p,
            children: F,
          }) => {
            const C = (0, c.GS)().mediaSize;
            (0, a.useEffect)(() => {
              if (void 0 !== _ && void 0 !== i)
                return (0, ke.F)(() => {
                  i();
                }, _);
            }, [_, i]);
            const B = (0, a.useMemo)(
                () =>
                  A
                    ? Je.Bq.AwaitSeason
                    : g || n === Je.Tj.ACTIVE || n === Je.Bq.Completed
                      ? n === Je.Tj.ACTIVE
                        ? o
                          ? Je.Bq.Bought
                          : Je.Bq.Free
                        : Je.Bq.Completed
                      : Je.Bq.ChapterNotChosen,
                [o, n, A, g],
              ),
              b = B === Je.Bq.Completed,
              S = Boolean(g) && B !== Je.Bq.ChapterNotChosen,
              D = Boolean(g) && !b,
              f = b && Boolean(h),
              v = S || f,
              w = t ? Je.$u.Small : Je.$u.Medium;
            return r().createElement(
              "div",
              { className: s()(tt, !t && at, C <= c.cJ.Small && 2 === u && lt) },
              D &&
                r().createElement("div", {
                  className: s()(ut, null == l ? void 0 : l.flag),
                  style: st(e, t),
                }),
              r().createElement(
                "div",
                { className: s()(rt, null == l ? void 0 : l.emblem) },
                r().createElement(et.G, {
                  chapterID: e,
                  progression: m,
                  size: t ? Je.$u.Small : Je.$u.Medium,
                  battlePassState: E || B,
                  hasBattlePass: o,
                  isChapterChosen: g,
                  isOpen: v,
                  chapterType: p,
                }),
                n === Je.Tj.NOT_CHOSEN && r().createElement(Re, { isInfinite: !0 }),
                0 !== d &&
                  r().createElement(
                    "div",
                    {
                      className: s()(nt, l && l.counter),
                      lang: R.strings.settings.LANGUAGE_CODE(),
                    },
                    d,
                  ),
                F,
              ),
              S &&
                r().createElement("div", {
                  className: s()(ot, l && l.chapterLogoIcon),
                  style: (0, He.cs)(e, o, w),
                }),
              f &&
                r().createElement(
                  "div",
                  { className: s()(it, l && l.freePoints) },
                  ((e = 0) => e.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "))(h),
                ),
            );
          },
          mt = "StateAttention_base_2e",
          ct = "StateAttention_emblem_1b",
          Et = "StateAttention_emblemCopy_17";
        function dt() {
          return (
            (dt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            dt.apply(this, arguments)
          );
        }
        const At = (e) => {
            const t = (0, a.useMemo)(() => ({ emblem: ct }), []);
            return (
              (0, a.useEffect)(() => {
                Se("bp_attention_widget");
              }, []),
              r().createElement(
                "div",
                { className: mt },
                r().createElement("div", { className: Et }),
                r().createElement(
                  _t,
                  dt({ stateClasses: t, duration: 2600 }, e),
                  r().createElement(Re, null),
                ),
              )
            );
          },
          gt = {
            base: "StateBuyBP_base_7e",
            flag: "StateBuyBP_flag_30",
            flagBuyBPIn: "StateBuyBP_flagBuyBPIn_cc",
            emblem: "StateBuyBP_emblem_26",
            emblemBuyBP: "StateBuyBP_emblemBuyBP_13",
            fadeInWithScale: "StateBuyBP_fadeInWithScale_b4",
            slideUp: "StateBuyBP_slideUp_19",
            wrapperHover: "StateBuyBP_wrapperHover_f7",
            wrapperOut: "StateBuyBP_wrapperOut_56",
            flagHover: "StateBuyBP_flagHover_70",
            emblemHover: "StateBuyBP_emblemHover_0a",
            logoIconHover: "StateBuyBP_logoIconHover_6b",
            logoIconHoverSmall: "StateBuyBP_logoIconHoverSmall_91",
            logoSmallX2IconHover: "StateBuyBP_logoSmallX2IconHover_6c",
            freePointsHover: "StateBuyBP_freePointsHover_12",
            flagOut: "StateBuyBP_flagOut_e1",
            emblemOut: "StateBuyBP_emblemOut_e6",
            freePointsOut: "StateBuyBP_freePointsOut_f0",
            logoIconOut: "StateBuyBP_logoIconOut_b2",
            logoIconOutSmall: "StateBuyBP_logoIconOutSmall_02",
            logoSmallX2IconOut: "StateBuyBP_logoSmallX2IconOut_91",
            emblemLevelUp: "StateBuyBP_emblemLevelUp_86",
            emblemAttention: "StateBuyBP_emblemAttention_ef",
            emblemCopyAttention: "StateBuyBP_emblemCopyAttention_2f",
            flagLevelUp: "StateBuyBP_flagLevelUp_ec",
            flagLevelUpPosOut: "StateBuyBP_flagLevelUpPosOut_ec",
            flagLevelUpLightOut: "StateBuyBP_flagLevelUpLightOut_96",
            flareLevelUp: "StateBuyBP_flareLevelUp_15",
            flagSwitchChapter: "StateBuyBP_flagSwitchChapter_c4",
            lightBuyBP: "StateBuyBP_lightBuyBP_18",
            lightAttention: "StateBuyBP_lightAttention_6f",
            lightAttentionSmall: "StateBuyBP_lightAttentionSmall_e3",
            lightChapterNotChosen: "StateBuyBP_lightChapterNotChosen_a6",
            lightChapterNotChosenSmall: "StateBuyBP_lightChapterNotChosenSmall_13",
          },
          ht = (e) => {
            const t = e.isSmall,
              u = e.scale,
              a = (0, c.GS)().mediaSize;
            return r().createElement(
              "div",
              {
                className: s()(
                  gt.base,
                  !t && gt.base__medium,
                  a <= c.cJ.Small && 2 === u && gt.base__smallX2,
                ),
              },
              r().createElement(_t, e, r().createElement(Re, null)),
            );
          },
          pt = "StateChapterNotChosen_base_ff",
          Ft = "StateChapterNotChosen_flag_e3",
          Ct = "StateChapterNotChosen_emblem_38";
        function Bt() {
          return (
            (Bt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Bt.apply(this, arguments)
          );
        }
        const bt = (e) =>
            r().createElement(
              "div",
              { className: pt },
              r().createElement(
                _t,
                Bt({}, e, { stateClasses: { emblem: e.isFirstShow ? Ct : "", flag: Ft } }),
              ),
            ),
          St = {
            base: "StateComplete_base_c7",
            flag: "StateComplete_flag_4a",
            flagLevelUp: "StateComplete_flagLevelUp_f2",
            emblem: "StateComplete_emblem_0e",
            emblemLevelUp: "StateComplete_emblemLevelUp_86",
            fadeInWithScale: "StateComplete_fadeInWithScale_31",
            slideUp: "StateComplete_slideUp_e6",
            wrapperHover: "StateComplete_wrapperHover_67",
            wrapperOut: "StateComplete_wrapperOut_4b",
            flagHover: "StateComplete_flagHover_c2",
            emblemHover: "StateComplete_emblemHover_c8",
            logoIconHover: "StateComplete_logoIconHover_63",
            logoIconHoverSmall: "StateComplete_logoIconHoverSmall_a6",
            logoSmallX2IconHover: "StateComplete_logoSmallX2IconHover_0d",
            freePointsHover: "StateComplete_freePointsHover_b7",
            flagOut: "StateComplete_flagOut_f0",
            emblemOut: "StateComplete_emblemOut_7f",
            freePointsOut: "StateComplete_freePointsOut_b5",
            logoIconOut: "StateComplete_logoIconOut_f1",
            logoIconOutSmall: "StateComplete_logoIconOutSmall_5d",
            logoSmallX2IconOut: "StateComplete_logoSmallX2IconOut_e0",
            emblemAttention: "StateComplete_emblemAttention_31",
            emblemCopyAttention: "StateComplete_emblemCopyAttention_7e",
            flagLevelUpPosOut: "StateComplete_flagLevelUpPosOut_5b",
            flagLevelUpLightOut: "StateComplete_flagLevelUpLightOut_04",
            flareLevelUp: "StateComplete_flareLevelUp_e2",
            flagBuyBPIn: "StateComplete_flagBuyBPIn_2e",
            flagSwitchChapter: "StateComplete_flagSwitchChapter_c3",
            emblemBuyBP: "StateComplete_emblemBuyBP_50",
            lightBuyBP: "StateComplete_lightBuyBP_86",
            lightAttention: "StateComplete_lightAttention_8e",
            lightAttentionSmall: "StateComplete_lightAttentionSmall_03",
            lightChapterNotChosen: "StateComplete_lightChapterNotChosen_49",
            lightChapterNotChosenSmall: "StateComplete_lightChapterNotChosenSmall_d6",
          };
        function Dt() {
          return (
            (Dt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Dt.apply(this, arguments)
          );
        }
        const ft = (e) => {
            const t = e.isSmall,
              u = e.scale,
              a = (0, c.GS)().mediaSize,
              n = { emblem: St.emblem, flag: St.flag };
            return r().createElement(
              "div",
              {
                className: s()(
                  St.base,
                  !t && St.base__medium,
                  a <= c.cJ.Small && 2 === u && St.base__smallX2,
                ),
              },
              r().createElement(_t, Dt({}, e, { stateClasses: n }), r().createElement(Re, null)),
            );
          },
          vt = {
            base: "StateLevelUp_base_c1",
            flag: "StateLevelUp_flag_8f",
            flagLevelUp: "StateLevelUp_flagLevelUp_fa",
            emblem: "StateLevelUp_emblem_fe",
            emblemLevelUp: "StateLevelUp_emblemLevelUp_f4",
            fadeInWithScale: "StateLevelUp_fadeInWithScale_0b",
            slideUp: "StateLevelUp_slideUp_aa",
            wrapperHover: "StateLevelUp_wrapperHover_ca",
            wrapperOut: "StateLevelUp_wrapperOut_03",
            flagHover: "StateLevelUp_flagHover_bf",
            emblemHover: "StateLevelUp_emblemHover_b4",
            logoIconHover: "StateLevelUp_logoIconHover_07",
            logoIconHoverSmall: "StateLevelUp_logoIconHoverSmall_21",
            logoSmallX2IconHover: "StateLevelUp_logoSmallX2IconHover_55",
            freePointsHover: "StateLevelUp_freePointsHover_c9",
            flagOut: "StateLevelUp_flagOut_5e",
            emblemOut: "StateLevelUp_emblemOut_a4",
            freePointsOut: "StateLevelUp_freePointsOut_70",
            logoIconOut: "StateLevelUp_logoIconOut_44",
            logoIconOutSmall: "StateLevelUp_logoIconOutSmall_db",
            logoSmallX2IconOut: "StateLevelUp_logoSmallX2IconOut_c9",
            emblemAttention: "StateLevelUp_emblemAttention_1a",
            emblemCopyAttention: "StateLevelUp_emblemCopyAttention_0e",
            flagLevelUpPosOut: "StateLevelUp_flagLevelUpPosOut_c8",
            flagLevelUpLightOut: "StateLevelUp_flagLevelUpLightOut_25",
            flareLevelUp: "StateLevelUp_flareLevelUp_87",
            flagBuyBPIn: "StateLevelUp_flagBuyBPIn_3b",
            flagSwitchChapter: "StateLevelUp_flagSwitchChapter_61",
            emblemBuyBP: "StateLevelUp_emblemBuyBP_b4",
            lightBuyBP: "StateLevelUp_lightBuyBP_86",
            lightAttention: "StateLevelUp_lightAttention_64",
            lightAttentionSmall: "StateLevelUp_lightAttentionSmall_d2",
            lightChapterNotChosen: "StateLevelUp_lightChapterNotChosen_b5",
            lightChapterNotChosenSmall: "StateLevelUp_lightChapterNotChosenSmall_08",
          };
        function wt() {
          return (
            (wt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            wt.apply(this, arguments)
          );
        }
        const Lt = (e) => {
            const t = e.prevLevel,
              u = e.progressInfo,
              n = e.scale,
              o = e.isSmall,
              l = (0, a.useState)(0),
              i = l[0],
              _ = l[1],
              m = (0, a.useState)(0),
              E = m[0],
              d = m[1],
              A = (0, a.useState)(u),
              g = A[0],
              h = A[1],
              p = (0, a.useState)(!1),
              F = p[0],
              C = p[1],
              B = (0, a.useState)(!1),
              b = B[0],
              S = B[1],
              D = (0, c.GS)().mediaSize,
              f = (0, a.useMemo)(() => (F ? { emblem: vt.emblem, flag: vt.flag } : void 0), [F]),
              v = (0, a.useCallback)(() => {
                h({
                  from: t > u.level ? 99 : 0,
                  to: u.to,
                  level: u.level,
                  labelAnimation: Je.ru.None,
                  newLabelAnimation: Je.ru.None,
                });
              }, [u, t]),
              w = (0, a.useCallback)(() => {
                (Se("bp_levelup_widget"),
                  C(!0),
                  h({
                    from: t > u.level ? 99 : 0,
                    to: u.to,
                    level: t,
                    newLevel: u.level,
                    labelAnimation: Je.ru.HideLevel,
                    newLabelAnimation: Je.ru.ShowLevel,
                  }),
                  d(window.setTimeout(v, 1200)));
              }, [u, t, v]);
            return (
              (0, a.useLayoutEffect)(() => {
                b ||
                  (_(window.setTimeout(w, 1200)),
                  h({ from: u.from, to: t > u.level ? 0 : 99, level: t }),
                  S(!0));
              }, [w, u, t, b]),
              (0, a.useEffect)(
                () => () => {
                  (window.clearTimeout(i), window.clearTimeout(E));
                },
                [i, E],
              ),
              r().createElement(
                "div",
                {
                  className: s()(
                    vt.base,
                    !o && vt.base__medium,
                    D <= c.cJ.Small && 2 === n && vt.base__smallX2,
                  ),
                },
                r().createElement(
                  _t,
                  wt({}, e, { progressInfo: g, stateClasses: f, duration: 3e3 }),
                  F && r().createElement(Re, null),
                ),
              )
            );
          },
          Pt = "StateMouseOut_base_63",
          Ot = "StateMouseOut_flag_b0",
          yt = "StateMouseOut_emblem_cf",
          Tt = "StateMouseOut_chapterLogoIcon_55",
          It = "StateMouseOut_base__medium_89",
          Mt = "StateMouseOut_base__smallX2_e5",
          xt = "StateMouseOut_freePoints_fb";
        function Nt() {
          return (
            (Nt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Nt.apply(this, arguments)
          );
        }
        const Rt = (e) => {
            const t = e.scale,
              u = (0, c.GS)().mediaSize,
              a = { emblem: yt, flag: Ot, chapterLogoIcon: Tt, freePoints: xt };
            return r().createElement(
              "div",
              { className: s()(Pt, u <= c.cJ.Medium && Number(t) > 1 && Mt, u > c.cJ.Small && It) },
              r().createElement(_t, Nt({}, e, { stateClasses: a, duration: 200 })),
            );
          },
          kt = "StateMouseOver_base_95",
          Ht = "StateMouseOver_flag_34",
          Ut = "StateMouseOver_emblem_aa",
          Wt = "StateMouseOver_chapterLogoIcon_a8",
          $t = "StateMouseOver_base__medium_d1",
          Gt = "StateMouseOver_base__smallX2_b2",
          jt = "StateMouseOver_freePoints_ff";
        function zt() {
          return (
            (zt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            zt.apply(this, arguments)
          );
        }
        const Vt = (e) => {
            const t = e.scale,
              u = (0, c.GS)().mediaSize,
              n = { emblem: Ut, flag: Ht, chapterLogoIcon: Wt, freePoints: jt };
            return (
              (0, a.useEffect)(() => {
                Se("highlight");
              }, []),
              r().createElement(
                "div",
                {
                  className: s()(kt, u <= c.cJ.Medium && Number(t) > 1 && Gt, u > c.cJ.Small && $t),
                },
                r().createElement(_t, zt({}, e, { stateClasses: n })),
              )
            );
          },
          qt = "StateNotTakenRewards_base_21",
          Xt = "StateNotTakenRewards_counter_dd";
        function Yt() {
          return (
            (Yt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Yt.apply(this, arguments)
          );
        }
        const Kt = (e) => {
            const t = (0, a.useMemo)(() => ({ counter: Xt }), []);
            return r().createElement(
              "div",
              { className: qt },
              r().createElement(_t, Yt({ stateClasses: t, duration: 2600 }, e)),
            );
          },
          Zt = "StateProgressChange_base_b5";
        function Qt() {
          return (
            (Qt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Qt.apply(this, arguments)
          );
        }
        const Jt = (e) =>
            r().createElement(
              "div",
              { className: Zt },
              r().createElement(_t, Qt({}, e, { duration: 1200 })),
            ),
          eu = "StateShow_base_ef",
          tu = "StateShow_flag_31",
          uu = "StateShow_emblem_44",
          au = "StateShow_chapterLogoIcon_66",
          ru = "StateShow_freePoints_36";
        function nu() {
          return (
            (nu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            nu.apply(this, arguments)
          );
        }
        const ou = (e) => {
            const t = e.isFirstShow,
              u = e.progressionState,
              n = (0, a.useMemo)(
                () => ({ emblem: uu, flag: tu, chapterLogoIcon: au, freePoints: ru }),
                [],
              );
            (0, a.useEffect)(() => {
              Se(t || u === Je.Tj.NOT_CHOSEN ? "bp_show_widget" : "bp_show_widget_02");
            }, [t, u]);
            const o = u === Je.Tj.COMPLETED;
            return r().createElement(
              "div",
              { className: eu },
              r().createElement(
                _t,
                nu({}, e, { stateClasses: n, duration: t ? 1650 : 600 }),
                t && !o && r().createElement(Re, null),
              ),
            );
          },
          lu = {
            base: "StateSwitchChapter_base_05",
            flag: "StateSwitchChapter_flag_79",
            flagSwitchChapter: "StateSwitchChapter_flagSwitchChapter_8a",
            emblem: "StateSwitchChapter_emblem_d5",
            slideUp: "StateSwitchChapter_slideUp_0d",
            fadeInWithScale: "StateSwitchChapter_fadeInWithScale_2b",
            wrapperHover: "StateSwitchChapter_wrapperHover_2c",
            wrapperOut: "StateSwitchChapter_wrapperOut_e6",
            flagHover: "StateSwitchChapter_flagHover_69",
            emblemHover: "StateSwitchChapter_emblemHover_55",
            logoIconHover: "StateSwitchChapter_logoIconHover_25",
            logoIconHoverSmall: "StateSwitchChapter_logoIconHoverSmall_44",
            logoSmallX2IconHover: "StateSwitchChapter_logoSmallX2IconHover_b9",
            freePointsHover: "StateSwitchChapter_freePointsHover_6e",
            flagOut: "StateSwitchChapter_flagOut_13",
            emblemOut: "StateSwitchChapter_emblemOut_e8",
            freePointsOut: "StateSwitchChapter_freePointsOut_dc",
            logoIconOut: "StateSwitchChapter_logoIconOut_dc",
            logoIconOutSmall: "StateSwitchChapter_logoIconOutSmall_c3",
            logoSmallX2IconOut: "StateSwitchChapter_logoSmallX2IconOut_1b",
            emblemLevelUp: "StateSwitchChapter_emblemLevelUp_c5",
            emblemAttention: "StateSwitchChapter_emblemAttention_9e",
            emblemCopyAttention: "StateSwitchChapter_emblemCopyAttention_4a",
            flagLevelUp: "StateSwitchChapter_flagLevelUp_72",
            flagLevelUpPosOut: "StateSwitchChapter_flagLevelUpPosOut_45",
            flagLevelUpLightOut: "StateSwitchChapter_flagLevelUpLightOut_b6",
            flareLevelUp: "StateSwitchChapter_flareLevelUp_50",
            flagBuyBPIn: "StateSwitchChapter_flagBuyBPIn_75",
            emblemBuyBP: "StateSwitchChapter_emblemBuyBP_ba",
            lightBuyBP: "StateSwitchChapter_lightBuyBP_19",
            lightAttention: "StateSwitchChapter_lightAttention_2a",
            lightAttentionSmall: "StateSwitchChapter_lightAttentionSmall_24",
            lightChapterNotChosen: "StateSwitchChapter_lightChapterNotChosen_da",
            lightChapterNotChosenSmall: "StateSwitchChapter_lightChapterNotChosenSmall_c5",
          };
        function iu() {
          return (
            (iu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            iu.apply(this, arguments)
          );
        }
        const su = (e) => {
          const t = e.progressInfo,
            u = e.isSmall,
            n = e.scale,
            o = e.hasBattlePass,
            l = (0, a.useState)(!1),
            i = l[0],
            _ = l[1],
            m = (0, c.GS)().mediaSize,
            E = { emblem: lu.emblem, flag: lu.flag },
            d = (0, a.useCallback)(() => {
              _(!0);
            }, []),
            A = (0, a.useCallback)(() => {
              const e = window.setTimeout(d, 500);
              return () => {
                window.clearTimeout(e);
              };
            }, [d]);
          return (
            (0, a.useLayoutEffect)(() => {
              const e = window.setTimeout(A, 450);
              return () => {
                window.clearTimeout(e);
              };
            }, [A]),
            r().createElement(
              "div",
              {
                className: s()(
                  lu.base,
                  !u && lu.base__medium,
                  m <= c.cJ.Small && 2 === n && lu.base__smallX2,
                ),
              },
              r().createElement(
                _t,
                iu({}, e, {
                  progressInfo: t,
                  emblem: o ? Je.Bq.Bought : Je.Bq.Free,
                  stateClasses: E,
                  duration: 3500,
                }),
                i && r().createElement(Re, null),
              ),
            )
          );
        };
        let _u;
        !(function (e) {
          ((e.NORMAL = "NORMAL"),
            (e.SHOW = "SHOW"),
            (e.PROGRESS_CHANGE = "PROGRESS_CHANGE"),
            (e.MOUSE_OVER = "MOUSE_OVER"),
            (e.MOUSE_OUT = "MOUSE_OUT"),
            (e.LEVEL_DOWN = "LEVEL_DOWN"),
            (e.LEVEL_UP = "LEVEL_UP"),
            (e.BUY_BP = "BUY_BP"),
            (e.SWITCH_CHAPTER = "SWITCH_CHAPTER"),
            (e.SHOW_NOT_TAKEN_REWARDS = "SHOW_NOT_TAKEN_REWARDS"),
            (e.COMPLETE = "COMPLETE"),
            (e.ATTENTION = "ATTENTION"),
            (e.CHAPTER_NOT_CHOSEN = "CHAPTER_NOT_CHOSEN"),
            (e.MARATHON_CHAPTER = "MARATHON_CHAPTER"));
        })(_u || (_u = {}));
        const mu = {
          base: "Content_base_81",
          base__smallX2: "Content_base__smallX2_95",
          base__disabled: "Content_base__disabled_76",
          base__seasonWaiting: "Content_base__seasonWaiting_7c",
          effects: "Content_effects_0d",
          effects__normal: "Content_effects__normal_cd",
          effects__disabled: "Content_effects__disabled_44",
          effects__seasonWaiting: "Content_effects__seasonWaiting_4d",
          componentWrapper: "Content_componentWrapper_15",
          componentWrapper__hidden: "Content_componentWrapper__hidden_7a",
          fadeInWithScale: "Content_fadeInWithScale_fc",
          slideUp: "Content_slideUp_39",
          wrapperHover: "Content_wrapperHover_39",
          wrapperOut: "Content_wrapperOut_d1",
          flagHover: "Content_flagHover_73",
          emblemHover: "Content_emblemHover_1a",
          logoIconHover: "Content_logoIconHover_26",
          logoIconHoverSmall: "Content_logoIconHoverSmall_4e",
          logoSmallX2IconHover: "Content_logoSmallX2IconHover_ef",
          freePointsHover: "Content_freePointsHover_8d",
          flagOut: "Content_flagOut_c3",
          emblemOut: "Content_emblemOut_01",
          freePointsOut: "Content_freePointsOut_31",
          logoIconOut: "Content_logoIconOut_f1",
          logoIconOutSmall: "Content_logoIconOutSmall_1d",
          logoSmallX2IconOut: "Content_logoSmallX2IconOut_49",
          emblemLevelUp: "Content_emblemLevelUp_38",
          emblemAttention: "Content_emblemAttention_40",
          emblemCopyAttention: "Content_emblemCopyAttention_53",
          flagLevelUp: "Content_flagLevelUp_85",
          flagLevelUpPosOut: "Content_flagLevelUpPosOut_66",
          flagLevelUpLightOut: "Content_flagLevelUpLightOut_fe",
          flareLevelUp: "Content_flareLevelUp_b6",
          flagBuyBPIn: "Content_flagBuyBPIn_49",
          flagSwitchChapter: "Content_flagSwitchChapter_7d",
          emblemBuyBP: "Content_emblemBuyBP_e7",
          lightBuyBP: "Content_lightBuyBP_d1",
          lightAttention: "Content_lightAttention_aa",
          lightAttentionSmall: "Content_lightAttentionSmall_80",
          lightChapterNotChosen: "Content_lightChapterNotChosen_56",
          lightChapterNotChosenSmall: "Content_lightChapterNotChosenSmall_12",
        };
        function cu() {
          return (
            (cu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            cu.apply(this, arguments)
          );
        }
        const Eu = R.strings.battle_pass.tooltips.entryPoint.disabled,
          du = R.views.common.tooltip_window,
          Au = (e, t, u, a) => {
            if (e) return _u.SHOW;
            switch (t) {
              case T.BUY_BATTLE_PASS:
                return _u.BUY_BP;
              case T.PROGRESSION_COMPLETED:
                return _u.COMPLETE;
              case T.NEW_LEVEL:
                return u === a ? _u.NORMAL : u < a ? _u.LEVEL_DOWN : _u.LEVEL_UP;
              case T.CHANGE_PROGRESS:
                return u !== a ? _u.LEVEL_UP : _u.PROGRESS_CHANGE;
              case T.NEW_CHAPTER:
                return u === a ? _u.NORMAL : _u.SWITCH_CHAPTER;
              case T.NOT_TAKEN_REWARDS:
                return _u.SHOW_NOT_TAKEN_REWARDS;
              case T.NORMAL:
                return _u.NORMAL;
              case T.CHAPTER_NOT_CHOSEN:
                return _u.CHAPTER_NOT_CHOSEN;
            }
          },
          gu = (0, J.Pi)(() => {
            const e = ce(),
              t = e.model,
              u = e.controls,
              n = t.root.get(),
              o = n.level,
              l = n.prevLevel,
              i = n.battlePassState,
              _ = n.isSmall,
              m = n.tooltipID,
              E = n.progression,
              d = n.prevProgression,
              A = n.animState,
              g = n.animStateKey,
              h = n.hasBattlePass,
              p = n.chapterID,
              F = n.isProgressionCompleted,
              C = n.notChosenRewardCount,
              B = n.battleType,
              b = n.isChapterChosen,
              S = n.freePoints,
              D = n.isResourceAvailable,
              f = n.isFirstShow,
              v = n.chapterType,
              w = (0, a.useState)(!0),
              L = w[0],
              P = w[1],
              O = (0, a.useState)(Au(L, A, o, l)),
              y = O[0],
              M = O[1],
              x = (0, a.useState)(h),
              N = x[0],
              R = x[1],
              H = (0, a.useState)(A),
              U = H[0],
              W = H[1],
              $ = (0, a.useState)(!1),
              G = $[0],
              j = $[1],
              z = (0, a.useState)(!1),
              V = z[0],
              q = z[1],
              X = (0, a.useState)([L ? _u.SHOW : _u.NORMAL])[1],
              Y = t.computes.hasMarathon(),
              K = ((e) => {
                const t = ye(e, Pe),
                  u = (0, a.useCallback)(
                    (e) => {
                      t(e.action, e.logLevel, Oe(e));
                    },
                    [t],
                  );
                return (e) => u(e);
              })("collection"),
              Z = i !== I.DISABLED,
              Q = Ce(Y),
              J = k(),
              ee = (0, c.GS)().mediaSize,
              te = s()(
                mu.base,
                mu[`${mu.base}__${i}`],
                i === I.DISABLED && mu.base__disabled,
                i === I.SEASON_WAITING && mu.base__seasonWaiting,
                ee <= c.cJ.Medium && J > 1 && mu.base__smallX2,
              ),
              ue = i === I.DISABLED,
              ae = (0, a.useMemo)(
                () => (ue ? du.simple_tooltip_content.SimpleTooltipContent("resId") : m),
                [ue, m],
              ),
              re = (0, a.useMemo)(
                () => (ue ? du.tooltip_window.TooltipWindow("resId") : void 0),
                [ue],
              ),
              ne = (0, a.useMemo)(
                () => (ue ? { header: Eu.header(), body: Eu.$dyn(B) || Eu.body() } : void 0),
                [B, ue],
              ),
              oe = (0, a.useCallback)(
                (e) => {
                  X((t) => {
                    const u = t[0],
                      a = t[t.length - 1];
                    if (0 === t.length) M(e);
                    else {
                      if (1 === t.length && u === _u.NORMAL) return (M(e), [e]);
                      if (a === _u.NORMAL) return t.splice(t.length - 1, 1).concat(e);
                    }
                    return t.concat(e);
                  });
                },
                [X],
              ),
              le = (0, a.useCallback)(() => {
                Z && j(!0);
              }, [Z]),
              ie = (0, a.useCallback)(() => {
                Z && j(!1);
              }, [Z]),
              _e = (0, a.useCallback)(() => {
                Z &&
                  (u.openBattlePass(),
                  M(_u.MOUSE_OUT),
                  X([]),
                  j(!1),
                  Se("play"),
                  K({
                    item: fe.BattlePassCollectionEntryPoint,
                    action: ve.Click,
                    parentScreen: De.BattlePassProgression,
                  }));
              }, [u, Z, K, X]),
              me = (0, a.useCallback)(
                () => (F ? Je.Tj.COMPLETED : b ? Je.Tj.ACTIVE : Je.Tj.NOT_CHOSEN),
                [F, b],
              );
            var Ee;
            ((Ee = () => {
              P(!1);
            }),
              (0, a.useEffect)(Ee, []),
              (0, a.useEffect)(() => {
                W(A);
              }, [A, g, E]),
              (0, a.useEffect)(() => {
                h !== N && R(h);
              }, [N, h, y]));
            const de = be(() => {
                (M(_u.MOUSE_OVER), X([]));
              }),
              Ae = be(() => {
                (M(_u.MOUSE_OUT), X([]));
              }),
              he = ((e, t, u, r) => {
                const n = (0, a.useState)(!1),
                  o = n[0],
                  l = n[1],
                  i = (0, a.useRef)(!1);
                return (
                  (0, a.useEffect)(() => {
                    if (o)
                      return (0, ke.F)(() => {
                        l(!1);
                      }, t);
                  }, [t, o]),
                  (0, a.useEffect)(() => {
                    o
                      ? (i.current = !0)
                      : !i.current || e
                        ? ((i.current = !1), e ? u && u() : r && r())
                        : (i.current = !1);
                  }, [o, e, r, u]),
                  { setIsAnimationPending: l }
                );
              })(G, 3200, de, Ae),
              pe = he.setIsAnimationPending;
            ((0, a.useEffect)(() => {
              if (
                (y !== Au(L, U, o, l) || y === _u.SHOW) &&
                y !== _u.MOUSE_OVER &&
                y !== _u.MOUSE_OUT
              )
                switch (U) {
                  case T.BUY_BATTLE_PASS:
                    oe(_u.BUY_BP);
                    break;
                  case T.PROGRESSION_COMPLETED:
                    oe(_u.COMPLETE);
                    break;
                  case T.NEW_LEVEL:
                    (pe(!0), oe(o < l ? _u.LEVEL_DOWN : _u.LEVEL_UP));
                    break;
                  case T.CHANGE_PROGRESS:
                    oe(o !== l ? _u.LEVEL_UP : _u.PROGRESS_CHANGE);
                    break;
                  case T.NEW_CHAPTER:
                    (X([]), oe(_u.SWITCH_CHAPTER));
                    break;
                  case T.NOT_TAKEN_REWARDS:
                    oe(_u.SHOW_NOT_TAKEN_REWARDS);
                    break;
                  case T.NORMAL:
                    oe(_u.NORMAL);
                    break;
                  case T.CHAPTER_NOT_CHOSEN:
                    oe(_u.CHAPTER_NOT_CHOSEN);
                }
            }, [U, oe, o, l, L, y, X, pe]),
              (0, a.useEffect)(() => {
                "boolean" == typeof Q &&
                  Q !== Y &&
                  (q(!0),
                  setTimeout(() => {
                    q(!1);
                  }, 800));
              }, [Q, Y]));
            const Fe = (0, a.useCallback)(() => {
                (y === Au(L, U, o, l) &&
                  y !== _u.LEVEL_UP &&
                  y !== _u.LEVEL_DOWN &&
                  y !== _u.PROGRESS_CHANGE &&
                  y !== _u.SHOW) ||
                  X((e) => (e.length > 1 ? (M(e[1]), e.slice(1)) : (W(T.NORMAL), [])));
              }, [X, L, U, o, l, y]),
              Be = (0, a.useMemo)(() => {
                const e = me(),
                  t = {
                    chapterID: p,
                    isSmall: _,
                    isMouseOver: G,
                    progressInfo: { level: o, to: E, from: E },
                    hasBattlePass: N,
                    onFinish: Fe,
                    progressionState: e,
                    notChosenRewardCount: C,
                    isSeasonWaiting: i === I.SEASON_WAITING,
                    isDisabled: i === I.DISABLED,
                    isChapterChosen: b,
                    freePoints: i !== I.DISABLED ? S : 0,
                    duration: 0,
                    scale: J,
                    chapterType: !Y && D ? se.Resource : v,
                  };
                switch (y) {
                  case _u.ATTENTION:
                    return G ? r().createElement(Vt, t) : r().createElement(At, t);
                  case _u.SHOW:
                    return (
                      t.progressInfo.level !== l && -1 !== l && (t.progressInfo.level = l),
                      r().createElement(ou, cu({}, t, { isFirstShow: f }))
                    );
                  case _u.NORMAL:
                    return r().createElement(_t, t);
                  case _u.PROGRESS_CHANGE:
                    return ((t.progressInfo.from = d > E ? 0 : d), r().createElement(Jt, t));
                  case _u.MOUSE_OVER:
                    return r().createElement(Vt, t);
                  case _u.MOUSE_OUT:
                    return r().createElement(Rt, t);
                  case _u.LEVEL_DOWN:
                  case _u.LEVEL_UP:
                    return (
                      (t.progressInfo.from = d),
                      r().createElement(Lt, cu({}, t, { prevLevel: l }))
                    );
                  case _u.BUY_BP:
                    return r().createElement(ht, t);
                  case _u.SWITCH_CHAPTER:
                    return r().createElement(su, cu({ prevLevel: l }, t));
                  case _u.SHOW_NOT_TAKEN_REWARDS:
                    return r().createElement(Kt, t);
                  case _u.COMPLETE:
                    return e === Je.Tj.NOT_CHOSEN
                      ? r().createElement(bt, t)
                      : e === Je.Tj.COMPLETED
                        ? r().createElement(ft, t)
                        : r().createElement(_t, t);
                  case _u.CHAPTER_NOT_CHOSEN:
                    return r().createElement(bt, cu({}, t, { isFirstShow: L }));
                }
              }, [me, p, _, G, o, E, N, Fe, C, i, b, S, J, Y, D, v, y, l, f, d, L]);
            return r().createElement(
              ge,
              { contentId: ae, decoratorId: re, args: ne },
              r().createElement(
                "div",
                {
                  className: te,
                  style: { cursor: Z ? "pointer" : "default" },
                  onMouseEnter: le,
                  onMouseLeave: ie,
                  onClick: _e,
                },
                r().createElement(
                  "div",
                  { className: s()(mu.effects, mu[`${mu.effects}__${i}`]) },
                  r().createElement(
                    "div",
                    { className: s()(mu.componentWrapper, V && mu.componentWrapper__hidden) },
                    Be,
                  ),
                ),
              ),
            );
          }),
          hu = "App_base_f0",
          pu = "App_light_08",
          Fu = "App_light__chapterNotChosen_ff",
          Cu = "App_hintBody_61",
          Bu = "App_hintBodyX2_8a",
          bu = "App_hintBody__large_ba",
          Su = "App_hintBodyX2__large_e3",
          Du = {
            width: 250,
            height: 250,
            frameCount: 75,
            chunk: { count: 2, columns: 7, rows: 6 },
            getChunkPath:
              ((fu = "R.images.gui.maps.icons.sequence.sun_shine_sprite.sprite_"),
              (e) => `${fu}${e}`),
          };
        var fu;
        const vu = (0, J.Pi)(() => {
          const e = ce().model.root.get(),
            t = e.isChapterChosen,
            u = e.battlePassState,
            n = e.isProgressionCompleted,
            o = e.isResourceAvailable,
            l = [I.DISABLED, I.SEASON_WAITING].includes(u),
            i = (0, a.useRef)(null),
            _ = (0, c.GS)().mediaSize,
            m = 1 === k() ? s()(Cu, o && bu) : s()(Bu, o && Su),
            E = ((e, t) => {
              const u = Y("tutorialModel.effects.items").filter((u) => {
                if (!u) return !1;
                const a = u.value,
                  r = window.__featureId.toString();
                return a.componentId === e && a.type === t && a.viewId === r;
              });
              if (0 === u.length) return null;
              const a = Object.assign({}, u[0].value);
              return {
                effect: a,
                completeEffect: () => {
                  (tutorialModel.onEffectCompleted({
                    componentId: e,
                    viewId: window.__featureId.toFixed(0),
                    effectType: t,
                    effectBuilder: a.builder,
                  }),
                    t === K && window.tutorialApi && window.tutorialApi.updateComponents());
                },
              };
            })("EntryPointTrigger", Z);
          (0, a.useEffect)(
            () =>
              x(() => {
                null !== E && E.completeEffect();
              }),
            [E],
          );
          const d = ((e, t) => {
            const u = Y("tutorialModel.triggers.items").filter((u) => {
              if (!u) return !1;
              const a = u.value,
                r = a.triggers.filter((e) => e.value === t);
              return a.componentId === e && r.length > 0;
            });
            return 0 === u.length
              ? null
              : window.tutorialModel.foundComponents.items.some((t) => t.value.componentId === e)
                ? {
                    trigger: u[0].value,
                    runTrigger: (u) => {
                      window.tutorialModel.onTriggerActivated({
                        componentId: e,
                        triggerType: t,
                        state: u,
                      });
                    },
                  }
                : null;
          })("EntryPointTrigger", Q);
          return (
            (0, a.useEffect)(() => {
              d && d.runTrigger(!0);
            }, [d]),
            (0, a.useEffect)(
              () =>
                x(() => {
                  if (i.current) {
                    const e = i.current.getBoundingClientRect();
                    viewEnv.setInputArea(
                      viewEnv.pxToRem(e.x),
                      viewEnv.pxToRem(e.y),
                      viewEnv.pxToRem(e.width),
                      viewEnv.pxToRem(e.height),
                    );
                  }
                }),
              [_],
            ),
            r().createElement(
              "div",
              { className: hu, ref: i },
              !t &&
                !l &&
                r().createElement(
                  "div",
                  { className: s()(pu, n && Fu) },
                  r().createElement(L, {
                    width: Du.width,
                    height: Du.height,
                    frameCount: Du.frameCount,
                    getImageSource: f(Du),
                  }),
                ),
              r().createElement("div", { className: m, id: "entry-point-trigger" }),
              r().createElement(gu, null),
            )
          );
        });
        engine.whenReady.then(() => {
          o().render(
            r().createElement(me, null, r().createElement(C, null, r().createElement(vu, null))),
            document.getElementById("root"),
          );
        });
      },
      903: (e, t, u) => {
        "use strict";
        u.d(t, { FL: () => l, cs: () => o, wD: () => n });
        u(5415);
        var a = u(8546);
        const r = (e) => {
            switch (e) {
              case a.$u.Micro:
                return "s";
              case a.$u.Small:
                return "m";
              default:
                return "l";
            }
          },
          n = (e, t, u = "") => {
            const a = u.length > 0 ? `_${u}` : u,
              r = e.$dyn(`c_${t}${a}`),
              n = e.$dyn(`common${a}`);
            return r || n;
          },
          o = (e, t, u) => {
            const a = R.images.gui.maps.icons.battlePass.logo.chapterIcons,
              o = t ? "BP" : "",
              l = `${r(u)}${o}`;
            return { backgroundImage: `url(${n(a, e, l)})` };
          },
          l = (e, t, u, a) => {
            const r = R.images.gui.maps.icons.battlePass.logo,
              o = n(r, e, `emblem${a ? "_BP" : ""}${u ? "_open" : ""}${t}`);
            return o ? { backgroundImage: `url(${o})` } : void 0;
          };
      },
      9830: (e, t, u) => {
        "use strict";
        u.d(t, { G: () => oe });
        var a = u(6483),
          r = u.n(a),
          n = u(6179),
          o = u.n(n),
          l = u(903);
        const i = {
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
          s = {
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
          m = R.images.gui.maps.icons.battlePass.logo,
          c = (e, t, u) => {
            if (e && t) {
              const e = `c_${u}_font_texture_gold_contrast`;
              return m.$dyn(e) ? `url(${_}.${e})` : `url(${_}.font_texture_gold_contrast)`;
            }
            if (e) {
              const e = `c_${u}_font_texture_gold`;
              return m.$dyn(e) ? `url(${_}.${e})` : `url(${_}.font_texture_gold)`;
            }
            const a = `c_${u}_font_texture`;
            return m.$dyn(a) ? `url(${_}.${a})` : `url(${_}.font_texture)`;
          },
          E = (0, n.memo)(
            ({
              level: e,
              size: t,
              isGold: u,
              isForRewardScreen: a = !1,
              curState: n,
              isFirstLevel: l,
              showProgressionCompleted: i,
              chapterID: _ = 0,
            }) => {
              const m = r()(s.base, s[`base__${t}`]),
                E = r()(
                  s.text,
                  s.text__filtered,
                  s[`text__${t}`],
                  s[`text__${n}`],
                  i && s.text__hideWithDelay,
                  l && s.text__new,
                  a && s.text__rewardScreen,
                ),
                d = r()(
                  s.textWithBlend,
                  l && s.text__new,
                  i && s.text__hideWithDelay,
                  s[`textWithBlend__${n}`],
                ),
                A = r()(s.text, s.text__blended, s[`text__${t}`], a && s.text__rewardScreen),
                g = r()(s.textMask, a && s.textMask__animated, s[`textMask__${t}`]);
              return o().createElement(
                "div",
                { className: m },
                o().createElement("div", { className: E }, e),
                o().createElement(
                  "div",
                  { className: d },
                  o().createElement("div", { className: A }, e),
                  o().createElement("div", {
                    className: g,
                    style: { backgroundImage: c(u, a, _) },
                  }),
                ),
              );
            },
          );
        var d = u(8546);
        const A = {
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
          g = (e, t) => {
            const u = e ? "BP" : "";
            return `${((e) => {
              switch (e) {
                case d.$u.Small:
                  return "l";
                case d.$u.Micro:
                  return "s";
                default:
                  return "xl";
              }
            })(t)}${u}`;
          },
          h = (0, n.memo)(
            ({
              newLevel: e,
              level: t,
              size: u,
              battlePassState: a,
              hasProgression: n,
              isGolden: i,
              labelAnimation: s,
              newLabelAnimation: _,
              isChapterChosen: m = !1,
              chapterID: c = 0,
              isProgressionCompleted: h = !1,
              hasBeenActive: p = !1,
              isChapterSelection: F = !1,
              isProgression: C = !1,
            }) => {
              let B = "",
                b = "";
              u === d.$u.Small
                ? ((B = "Small"), (b = "__small"))
                : u === d.$u.Micro && ((B = "Micro"), (b = "__micro"));
              const S = a === d.Bq.SwitchedChapterRightNow,
                D = a === d.Bq.CompletedRightNow,
                f = ((e, t, u, a, r) => (e || r ? t || !u : t || !a))(F, h, p, m, C),
                v = !C && !F;
              return o().createElement(
                o().Fragment,
                null,
                f
                  ? o().createElement("div", {
                      className: r()(A.icon, b && A[`icon${b}`], D && A[`icon__animated${B}`]),
                      style: {
                        backgroundImage: `url(${(() => {
                          const e = R.images.gui.maps.icons.battlePass.logo,
                            t = g(i, u);
                          if (v) {
                            if (h) {
                              const u = e.tank.$dyn(`tank_${t}`),
                                a = e.tank.$dyn(`c_${c}_tank_${t}`);
                              return null != a ? a : u;
                            }
                            if (!m) return e.$dyn("not_chosen");
                          }
                          return (0, l.wD)(e.chapterIcons, c, t);
                        })()})`,
                      },
                    })
                  : o().createElement(
                      "div",
                      {
                        className: r()(
                          A.label,
                          A[`label${b}`],
                          S && A.label__new,
                          S && A[`label__new${B}`],
                          !D && h && A.label__disabled,
                          A[`label__${s}${B}`],
                          n && A[`label__hasProgress${B}`],
                          n && A[`label__hasProgress${B}${C ? "Progression" : ""}`],
                        ),
                        lang: R.strings.settings.LANGUAGE_CODE(),
                      },
                      o().createElement(E, {
                        level: t,
                        size: u,
                        isGold: i,
                        isFirstLevel: S,
                        curState: s,
                        showProgressionCompleted: D,
                        key: "label",
                        chapterID: c,
                      }),
                    ),
                e &&
                  o().createElement(
                    "div",
                    {
                      className: r()(
                        A.label,
                        A[`label${b}`],
                        S && A.label__new,
                        S && A[`label__new${B}`],
                        A[`label__${_}${B}`],
                        n && A[`label__hasProgress${B}`],
                      ),
                    },
                    o().createElement(E, {
                      level: e,
                      size: u,
                      isGold: i,
                      isFirstLevel: S,
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
        let F, C;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(F || (F = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(C || (C = {})));
        const B = ({ size: e = F.Default, classMix: t }) =>
            o().createElement("div", { className: r()(p.background, p[`background__${e}`], t) }),
          b = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          S = ({ size: e }) => {
            const t = r()(b.base, b[`base__${e}`]);
            return o().createElement("div", { className: t });
          },
          D = {
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
          f = (0, n.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: u,
              baseStyles: a,
              isComplete: n,
              withoutBounce: l,
            }) => {
              const i = r()(
                  D.base,
                  D[`base__${e}`],
                  u && D.base__disabled,
                  n && D.base__finished,
                  l && D.base__withoutBounce,
                ),
                s = !u && !n;
              return o().createElement(
                "div",
                { className: i, style: a, ref: t },
                o().createElement("div", { className: D.pattern }),
                o().createElement("div", { className: D.gradient }),
                s && o().createElement(S, { size: e }),
              );
            },
          ),
          v = ({ size: e, value: t, lineRef: u, disabled: a, onComplete: r }) => {
            const l = (0, n.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              i = 100 === t;
            return (
              (0, n.useEffect)(() => {
                i && r && r();
              }, [i, r]),
              o().createElement(f, {
                size: e,
                disabled: a,
                baseStyles: l,
                isComplete: i,
                lineRef: u,
              })
            );
          };
        var w = u(122);
        let L, P;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(L || (L = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(P || (P = {})));
        const O = "ProgressBarDeltaSimple_base_6c",
          y = "ProgressBarDeltaSimple_delta_99",
          T = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: a,
              size: r,
              to: l,
              onEndAnimation: i,
              onChangeAnimationState: s,
            }) => {
              const _ = l < a,
                m = (0, n.useState)(P.Idle),
                c = m[0],
                E = m[1],
                d = c === P.In,
                A = c === P.End,
                g = c === P.Idle,
                h = (0, n.useCallback)(
                  (e) => {
                    (E(e), s && s(e));
                  },
                  [s],
                );
              ((0, n.useEffect)(() => {
                if (g && !u) {
                  const e = t;
                  return (0, w.F)(() => {
                    h(P.In);
                  }, e);
                }
              }, [h, u, g, t]),
                (0, n.useEffect)(() => {
                  if (d) {
                    const u = e + t;
                    return (0, w.F)(() => {
                      (i && i(), h(P.End));
                    }, u);
                  }
                }, [h, d, i, t, e]));
              const p = (0, n.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, t, e],
                ),
                F = (0, n.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, t, e],
                ),
                C = (0, n.useMemo)(
                  () => ({ width: `${Math.abs(a - l)}%`, left: `${_ ? l : a}%` }),
                  [a, _, l],
                );
              return A
                ? null
                : o().createElement(
                    "div",
                    { className: O, style: C },
                    o().createElement(
                      "div",
                      { style: g ? p : F, className: y },
                      o().createElement(S, { size: r }),
                    ),
                  );
            },
          ),
          I = (0, n.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: a,
              disabled: r,
              isComplete: l,
              animationSettings: i,
              onChangeAnimationState: s,
              onEndAnimation: _,
            }) => {
              const m = (0, n.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${i.line.duration}ms`,
                  transitionDelay: `${i.line.delay}ms`,
                }),
                [i.line.delay, i.line.duration, e],
              );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(f, {
                  size: t,
                  lineRef: a,
                  disabled: r,
                  isComplete: l,
                  baseStyles: m,
                }),
                u >= 0 &&
                  o().createElement(T, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    freezed: i.freezed,
                    from: u,
                    size: t,
                    to: e,
                    onChangeAnimationState: s,
                    onEndAnimation: _,
                  }),
              );
            },
          ),
          M = "ProgressBarDeltaGrow_base_7e",
          x = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          N = "ProgressBarDeltaGrow_glow_68",
          k = (e) => (e ? { left: 0 } : { right: 0 }),
          H = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          U = (e) => ({ transitionDuration: `${e}ms` }),
          W = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: a,
              size: l,
              to: i,
              onEndAnimation: s,
              onChangeAnimationState: _,
              className: m,
            }) => {
              const c = i < a,
                E = (0, n.useState)(L.Idle),
                d = E[0],
                A = E[1],
                g = d === L.End,
                h = d === L.Idle,
                p = d === L.Grow,
                F = d === L.Shrink,
                C = (0, n.useCallback)(
                  (e) => {
                    (A(e), _ && _(e));
                  },
                  [_],
                ),
                B = (0, n.useCallback)(
                  (e, t) =>
                    (0, w.F)(() => {
                      C(e);
                    }, t),
                  [C],
                );
              (0, n.useEffect)(() => {
                if (!u)
                  return h
                    ? B(L.Grow, t)
                    : p
                      ? B(L.Shrink, e)
                      : F
                        ? B(L.End, e)
                        : void (g && s && s());
              }, [B, u, g, p, h, F, s, t, e]);
              const b = (0, n.useMemo)(() => Object.assign({ width: "100%" }, U(e), k(c)), [c, e]),
                D = (0, n.useMemo)(() => Object.assign({ width: "0%" }, U(e), k(c)), [c, e]),
                f = (0, n.useMemo)(() => Object.assign({ width: "0%" }, H(c, a), U(e)), [a, c, e]),
                v = (0, n.useMemo)(
                  () => Object.assign({ width: `${Math.abs(i - a)}%` }, H(c, a), U(e)),
                  [a, c, i, e],
                );
              if (g) return null;
              const P = r()(M, m, c && 0 === i && x);
              return o().createElement(
                "div",
                { style: h ? f : v, className: P },
                o().createElement(
                  "div",
                  { style: F ? D : b, className: N },
                  o().createElement(S, { size: l }),
                ),
              );
            },
          ),
          $ = (0, n.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: a,
              disabled: r,
              isComplete: l,
              animationSettings: i,
              onEndAnimation: s,
              onChangeAnimationState: _,
            }) => {
              const m = e < u,
                c = (0, n.useState)(!1),
                E = c[0],
                d = c[1],
                A = (0, n.useCallback)(
                  (e) => {
                    (e === L.Shrink && d(!0), _ && _(e));
                  },
                  [_],
                ),
                g = (0, n.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
                h = (0, n.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${i.line.duration}ms` }),
                  [i.line.duration, e],
                );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(f, {
                  size: t,
                  lineRef: a,
                  disabled: r,
                  isComplete: l,
                  withoutBounce: m && 0 === e,
                  baseStyles: E ? h : g,
                }),
                u >= 0 &&
                  o().createElement(W, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    onChangeAnimationState: A,
                    freezed: i.freezed,
                    onEndAnimation: s,
                    from: u,
                    size: t,
                    to: e,
                    className: i.delta.className,
                  }),
              );
            },
          ),
          G = ["onComplete", "onEndAnimation"];
        function j() {
          return (
            (j =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            j.apply(this, arguments)
          );
        }
        const z = (0, n.memo)((e) => {
            let t = e.onComplete,
              u = e.onEndAnimation,
              a = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, G);
            const r = (0, n.useState)(!1),
              l = r[0],
              i = r[1],
              s = (0, n.useCallback)(() => {
                const e = 100 === a.to;
                (e !== l && i(e), e && t && t(), u && u());
              }, [l, t, u, a.to]);
            switch (a.animationSettings.type) {
              case C.Simple:
                return o().createElement(I, j({}, a, { onEndAnimation: s, isComplete: l }));
              case C.Growing:
                return o().createElement($, j({}, a, { onEndAnimation: s, isComplete: l }));
              default:
                return null;
            }
          }),
          V = ["onEndAnimation"];
        function q() {
          return (
            (q =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            q.apply(this, arguments)
          );
        }
        const X = (0, n.memo)((e) => {
          let t = e.onEndAnimation,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((u = n[a]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, V);
          const a = (0, n.useRef)({}),
            r = (0, n.useCallback)(() => {
              ((a.current.from = void 0), t && t());
            }, [t]),
            l = "number" == typeof a.current.from ? a.current.from : u.from;
          return (
            (a.current.from = l),
            o().createElement(z, q({}, u, { onEndAnimation: r, key: `${l}-${u.to}`, from: l }))
          );
        });
        function Y() {
          return (
            (Y =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Y.apply(this, arguments)
          );
        }
        const K = (0, n.memo)(
            ({
              size: e,
              value: t,
              lineRef: u,
              disabled: a,
              deltaFrom: r,
              animationSettings: n,
              onEndAnimation: l,
              onChangeAnimationState: i,
              onComplete: s,
            }) => {
              if (r === t)
                return o().createElement(v, {
                  key: `${r}-${t}`,
                  size: e,
                  value: t,
                  lineRef: u,
                  disabled: a,
                  onComplete: s,
                });
              const _ = {
                from: r,
                to: t,
                size: e,
                lineRef: u,
                disabled: a,
                animationSettings: n,
                onComplete: s,
                onEndAnimation: l,
                onChangeAnimationState: i,
              };
              return n.withStack
                ? o().createElement(X, _)
                : o().createElement(z, Y({ key: `${r}-${t}` }, _));
            },
          ),
          Z = (e) => ({
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
          Q = (e, t, u) => (u < e ? e : u > t ? t : u),
          J = (e, t, u) => {
            if ("number" == typeof u) {
              return (Q(0, t, u) / t) * 100;
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
            type: C.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          ue = (0, n.memo)(
            ({
              maxValue: e = 100,
              theme: t = ee,
              size: u = F.Default,
              animationSettings: a = te,
              disabled: l = !1,
              withoutBackground: i = !1,
              progressBarBackgroundClassMix: s,
              value: _,
              deltaFrom: m,
              lineRef: c,
              onChangeAnimationState: E,
              onEndAnimation: d,
              onComplete: A,
            }) => {
              const g = ((e, t, u) =>
                (0, n.useMemo)(() => {
                  const a = (Q(0, t, e) / t) * 100;
                  return { value: a, deltaFrom: J(a, t, u) };
                }, [u, t, e]))(_, e, m);
              return o().createElement(
                "div",
                { className: r()(p.base, p[`base__${u}`]), style: Z(t) },
                !i && o().createElement(B, { size: u, classMix: s }),
                o().createElement(K, {
                  size: u,
                  lineRef: c,
                  disabled: l,
                  value: g.value,
                  deltaFrom: g.deltaFrom,
                  animationSettings: a,
                  onEndAnimation: d,
                  onChangeAnimationState: E,
                  onComplete: A,
                }),
              );
            },
          ),
          ae = {
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
          re = (0, n.memo)(
            ({
              progression: e,
              isNoVehicles: t = !1,
              showProgressionCompleted: u,
              isProgressionCompleted: a,
              size: n,
            }) => {
              const l = r()(
                ae.base,
                ae[`base__${n}`],
                u && ae.base__completed,
                !u && a && ae.base__hidden,
              );
              return o().createElement(
                "div",
                { className: l },
                o().createElement(ue, {
                  key: e.to,
                  size: F.Small,
                  value: e.to || 0,
                  deltaFrom: e.from || 0,
                  disabled: t,
                }),
              );
            },
          );
        function ne() {
          return (
            (ne =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            ne.apply(this, arguments)
          );
        }
        const oe = (0, n.memo)((e) => {
          const t = e.progression,
            u = e.size,
            a = e.battlePassState,
            n = e.hasBattlePass,
            s = e.isChapterChosen,
            _ = e.hasBeenActive,
            m = void 0 !== _ && _,
            c = e.isChapterSelection,
            E = void 0 !== c && c,
            A = e.isOpen,
            g = void 0 !== A && A,
            p = e.isProgression,
            F = void 0 !== p && p,
            C = e.showProgressBar,
            B = void 0 === C || C,
            b = e.chapterType,
            S = e.chapterID;
          let D = "",
            f = "",
            v = "";
          u === d.$u.Small
            ? ((D = "Small"), (f = "__small"), (v = "_small"))
            : u === d.$u.Micro && ((D = "Micro"), (f = "__micro"), (v = "_micro"));
          const w = g ? "Open" : "",
            L = a === d.Bq.CompletedRightNow,
            P = n || a === d.Bq.Bought,
            O = (a === d.Bq.Completed || L) && P,
            y = (a === d.Bq.Completed || L) && !P,
            T = O || y,
            I = r()(
              i.image,
              i[`image${f}`],
              g && i[`image__open${D}`],
              P && i[`image__battlePass${D}${w}`],
              a === d.Bq.AwaitSeason && i[`image__seasonWaiting${D}`],
              y && i[`image__completedFree${D}${w}`],
            ),
            M = r()(i[`${b}`], i[`${b}${f}`]),
            x = void 0 !== t.from,
            N = B && ((x && s) || m);
          return o().createElement(
            "div",
            { className: i.base },
            o().createElement("div", { className: M }),
            o().createElement(
              "div",
              { className: I, style: (0, l.FL)(S, v, g, P) },
              a !== d.Bq.AwaitSeason &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement(
                    h,
                    ne(
                      {
                        hasProgression: x,
                        isGolden: P,
                        isProgressionCompleted: T,
                        isChapterChosen: s,
                        hasBeenActive: m,
                        isChapterSelection: E,
                        isProgression: F,
                      },
                      e,
                      t,
                    ),
                  ),
                  N &&
                    o().createElement(re, {
                      key: t.to,
                      progression: t,
                      showProgressionCompleted: L,
                      isProgressionCompleted: T,
                      size: u,
                    }),
                ),
            ),
          );
        });
      },
      8546: (e, t, u) => {
        "use strict";
        let a, r, n, o;
        (u.d(t, { $u: () => a, Bq: () => n, Tj: () => r, ru: () => o }),
          (function (e) {
            ((e.Micro = "micro"), (e.Small = "small"), (e.Medium = "medium"));
          })(a || (a = {})),
          (function (e) {
            ((e.ACTIVE = "active"), (e.COMPLETED = "completed"), (e.NOT_CHOSEN = "notChosen"));
          })(r || (r = {})),
          (function (e) {
            ((e.AwaitSeason = "awaitSeason"),
              (e.Bought = "bought"),
              (e.Free = "free"),
              (e.Completed = "completed"),
              (e.CompletedRightNow = "completedRightNow"),
              (e.SwitchedChapterRightNow = "switchedChapterRightNow"),
              (e.NoVehiclesBase = "noVehiclesBase"),
              (e.ChapterNotChosen = "chapterNotChosen"));
          })(n || (n = {})),
          (function (e) {
            ((e.None = ""),
              (e.ShowLevel = "show"),
              (e.HideLevel = "hide"),
              (e.HideLevelWithDelay = "hideWithDelay"));
          })(o || (o = {})));
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(e) {
    var t = __webpack_module_cache__[e];
    if (void 0 !== t) return t.exports;
    var u = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](u, u.exports, __webpack_require__), u.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, u, a) => {
      if (!t) {
        var r = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, u, a] = deferred[i], n = !0, o = 0; o < t.length; o++)
            (!1 & a || r >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((n = !1), a < r && (r = a));
          if (n) {
            deferred.splice(i--, 1);
            var l = u();
            void 0 !== l && (e = l);
          }
        }
        return e;
      }
      a = a || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > a; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, u, a];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var u in t)
        __webpack_require__.o(t, u) &&
          !__webpack_require__.o(e, u) &&
          Object.defineProperty(e, u, { enumerable: !0, get: t[u] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t)),
    (__webpack_require__.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 6229),
    (() => {
      var e = { 6229: 0, 1730: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var a,
            r,
            [n, o, l] = u,
            i = 0;
          if (n.some((t) => 0 !== e[t])) {
            for (a in o) __webpack_require__.o(o, a) && (__webpack_require__.m[a] = o[a]);
            if (l) var s = l(__webpack_require__);
          }
          for (t && t(u); i < n.length; i++)
            ((r = n[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(s);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [1519], () => __webpack_require__(7265));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
