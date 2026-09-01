(() => {
  "use strict";
  var __webpack_modules__ = {
      3495: (u, e, t) => {
        t.d(e, { Y: () => A });
        var n = t(3138),
          a = t(6179),
          i = t(1043),
          r = t(5262);
        const o = n.O.client.getSize("rem"),
          s = o.width,
          E = o.height,
          l = Object.assign({ width: s, height: E }, (0, r.T)(s, E, i.j)),
          A = (0, a.createContext)(l);
      },
      1039: (u, e, t) => {
        var n = t(6179),
          a = t.n(n),
          i = t(6536),
          r = t(3495),
          o = t(1043),
          s = t(5262),
          E = t(3138);
        (0, n.memo)(({ children: u }) => {
          const e = (0, n.useContext)(r.Y),
            t = (0, n.useState)(e),
            l = t[0],
            A = t[1],
            F = (0, n.useCallback)((u, e) => {
              const t = E.O.view.pxToRem(u),
                n = E.O.view.pxToRem(e);
              A(Object.assign({ width: t, height: n }, (0, s.T)(t, n, o.j)));
            }, []);
          ((0, i.Z)(() => {
            engine.on("clientResized", F);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", F), [F]));
          const d = (0, n.useMemo)(() => Object.assign({}, l), [l]);
          return a().createElement(r.Y.Provider, { value: d }, u);
        });
      },
      6010: (u, e, t) => {
        var n = t(6179),
          a = t(7382),
          i = t(3495);
        const r = ["children"];
        const o = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                i = Object.keys(u);
              for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, r);
          const o = (0, n.useContext)(i.Y),
            s = o.extraLarge,
            E = o.large,
            l = o.medium,
            A = o.small,
            F = o.extraSmall,
            d = o.extraLargeWidth,
            c = o.largeWidth,
            _ = o.mediumWidth,
            m = o.smallWidth,
            D = o.extraSmallWidth,
            B = o.extraLargeHeight,
            C = o.largeHeight,
            g = o.mediumHeight,
            h = o.smallHeight,
            v = o.extraSmallHeight,
            w = { extraLarge: B, large: C, medium: g, small: h, extraSmall: v };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return e;
            if (t.large && E) return e;
            if (t.medium && l) return e;
            if (t.small && A) return e;
            if (t.extraSmall && F) return e;
          } else {
            if (t.extraLargeWidth && d) return (0, a.H)(e, t, w);
            if (t.largeWidth && c) return (0, a.H)(e, t, w);
            if (t.mediumWidth && _) return (0, a.H)(e, t, w);
            if (t.smallWidth && m) return (0, a.H)(e, t, w);
            if (t.extraSmallWidth && D) return (0, a.H)(e, t, w);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return e;
              if (t.largeHeight && C) return e;
              if (t.mediumHeight && g) return e;
              if (t.smallHeight && h) return e;
              if (t.extraSmallHeight && v) return e;
            }
          }
          return null;
        };
        o.defaultProps = {
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
        (0, n.memo)(o);
      },
      7382: (u, e, t) => {
        t.d(e, { H: () => n });
        const n = (u, e, t) =>
          e.extraLargeHeight ||
          e.largeHeight ||
          e.mediumHeight ||
          e.smallHeight ||
          e.extraSmallHeight
            ? (e.extraLargeHeight && t.extraLarge) ||
              (e.largeHeight && t.large) ||
              (e.mediumHeight && t.medium) ||
              (e.smallHeight && t.small) ||
              (e.extraSmallHeight && t.extraSmall)
              ? u
              : null
            : u;
      },
      7739: (u, e, t) => {
        (t(6010), t(1039), t(3495));
      },
      1043: (u, e, t) => {
        t.d(e, { j: () => n });
        const n = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (u, e, t) => {
        var n;
        function a(u, e, t) {
          const n = (function (u, e) {
              switch (!0) {
                case u >= e.extraLarge.width:
                  return e.extraLarge.weight;
                case u >= e.large.width && u < e.extraLarge.width:
                  return e.large.weight;
                case u >= e.medium.width && u < e.large.width:
                  return e.medium.weight;
                case u >= e.small.width && u < e.medium.width:
                  return e.small.weight;
                default:
                  return e.extraSmall.weight;
              }
            })(u, t),
            a = (function (u, e) {
              switch (!0) {
                case u >= e.extraLarge.height:
                  return e.extraLarge.weight;
                case u >= e.large.height && u < e.extraLarge.height:
                  return e.large.weight;
                case u >= e.medium.height && u < e.large.height:
                  return e.medium.weight;
                case u >= e.small.height && u < e.medium.height:
                  return e.small.weight;
                default:
                  return e.extraSmall.weight;
              }
            })(e, t),
            i = Math.min(n, a);
          return {
            extraLarge: i === t.extraLarge.weight,
            large: i === t.large.weight,
            medium: i === t.medium.weight,
            small: i === t.small.weight,
            extraSmall: i === t.extraSmall.weight,
            extraLargeWidth: n === t.extraLarge.weight,
            largeWidth: n === t.large.weight,
            mediumWidth: n === t.medium.weight,
            smallWidth: n === t.small.weight,
            extraSmallWidth: n === t.extraSmall.weight,
            extraLargeHeight: a === t.extraLarge.weight,
            largeHeight: a === t.large.weight,
            mediumHeight: a === t.medium.weight,
            smallHeight: a === t.small.weight,
            extraSmallHeight: a === t.extraSmall.weight,
          };
        }
        (t.d(e, { T: () => a }),
          (function (u) {
            ((u.extraLarge = "extraLarge"),
              (u.large = "large"),
              (u.medium = "medium"),
              (u.small = "small"),
              (u.extraSmall = "extraSmall"),
              (u.extraLargeWidth = "extraLargeWidth"),
              (u.largeWidth = "largeWidth"),
              (u.mediumWidth = "mediumWidth"),
              (u.smallWidth = "smallWidth"),
              (u.extraSmallWidth = "extraSmallWidth"),
              (u.extraLargeHeight = "extraLargeHeight"),
              (u.largeHeight = "largeHeight"),
              (u.mediumHeight = "mediumHeight"),
              (u.smallHeight = "smallHeight"),
              (u.extraSmallHeight = "extraSmallHeight"));
          })(n || (n = {})));
      },
      7078: (u, e, t) => {
        t.d(e, { t: () => s });
        var n = t(6179),
          a = t.n(n),
          i = t(2056);
        const r = ["children"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            o.apply(this, arguments)
          );
        }
        const s = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                i = Object.keys(u);
              for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, r);
          return a().createElement(
            i.u,
            o(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              t,
            ),
            e,
          );
        };
      },
      6373: (u, e, t) => {
        t.d(e, { i: () => E });
        var n = t(2056),
          a = t(6179),
          i = t.n(a);
        const r = ["children", "body", "header", "note", "alert", "args"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            o.apply(this, arguments)
          );
        }
        const s = R.views.common.tooltip_window.simple_tooltip_content,
          E = (u) => {
            let e = u.children,
              t = u.body,
              E = u.header,
              l = u.note,
              A = u.alert,
              F = u.args,
              d = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  i = Object.keys(u);
                for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, r);
            const c = (0, a.useMemo)(() => {
              const u = Object.assign({}, F, { body: t, header: E, note: l, alert: A });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [A, t, E, l, F]);
            return i().createElement(
              n.u,
              o(
                {
                  contentId:
                    ((_ = null == F ? void 0 : F.hasHtmlContent),
                    _ ? s.SimpleTooltipHtmlContent("resId") : s.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                d,
              ),
              e,
            );
            var _;
          };
      },
      2056: (u, e, t) => {
        t.d(e, { u: () => E });
        var n = t(7902),
          a = t(4179),
          i = t(6179);
        const r = [
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
        function o(u) {
          return Object.entries(u || {}).map(([u, e]) => {
            const t = { __Type: "GFValueProxy", name: u };
            switch (typeof e) {
              case "number":
                t.number = e;
                break;
              case "boolean":
                t.bool = e;
                break;
              case "undefined":
                break;
              default:
                t.string = e.toString();
            }
            return t;
          });
        }
        const s = (u, e, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: a.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: n,
                },
                t,
              ),
            );
          },
          E = (u) => {
            let e = u.children,
              t = u.contentId,
              a = u.args,
              E = u.onMouseEnter,
              l = u.onMouseLeave,
              A = u.onMouseDown,
              F = u.onClick,
              d = u.ignoreShowDelay,
              c = void 0 !== d && d,
              _ = u.ignoreMouseClick,
              m = void 0 !== _ && _,
              D = u.decoratorId,
              B = void 0 === D ? 0 : D,
              C = u.isEnabled,
              g = void 0 === C || C,
              h = u.targetId,
              v = void 0 === h ? 0 : h,
              w = u.onShow,
              f = u.onHide,
              b = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  i = Object.keys(u);
                for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, r);
            const p = (0, i.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              k = (0, i.useMemo)(() => v || (0, n.F)().resId, [v]),
              S = (0, i.useCallback)(() => {
                (p.current.isVisible && p.current.timeoutId) ||
                  (s(t, B, { isMouseEvent: !0, on: !0, arguments: o(a) }, k),
                  w && w(),
                  (p.current.isVisible = !0));
              }, [t, B, a, k, w]),
              x = (0, i.useCallback)(() => {
                if (p.current.isVisible || p.current.timeoutId) {
                  const u = p.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (p.current.timeoutId = 0)),
                    s(t, B, { on: !1 }, k),
                    p.current.isVisible && f && f(),
                    (p.current.isVisible = !1));
                }
              }, [t, B, k, f]),
              O = (0, i.useCallback)((u) => {
                p.current.isVisible &&
                  ((p.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (p.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(p.current.prevTarget) && x();
                  }, 200)));
              }, []);
            ((0, i.useEffect)(() => {
              const u = p.current.hideTimerId;
              return (
                document.addEventListener("wheel", O, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", O, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, i.useEffect)(() => {
                !1 === g && x();
              }, [g, x]),
              (0, i.useEffect)(
                () => (
                  window.addEventListener("mouseleave", x),
                  () => {
                    (window.removeEventListener("mouseleave", x), x());
                  }
                ),
                [x],
              ));
            return g
              ? (0, i.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((y = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((p.current.timeoutId = window.setTimeout(S, c ? 100 : 400)),
                            E && E(u),
                            y && y(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (x(), null == l || l(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === m && x(), null == F || F(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === m && x(), null == A || A(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    b,
                  ),
                )
              : e;
            var y;
          };
      },
      527: (u, e, t) => {
        (t.r(e), t.d(e, { mouse: () => o, onResize: () => i }));
        var n = t(2472),
          a = t(1176);
        const i = (0, n.E)("clientResized"),
          r = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const o = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && (0, a.R)(!1);
          }
          function t() {
            u.enabled && (0, a.R)(!0);
          }
          function n() {
            u.enabled
              ? u.listeners < 1
                ? ((u.initialized = !1),
                  document.body.removeEventListener("mouseenter", e),
                  document.body.removeEventListener("mouseleave", t))
                : u.initialized ||
                  ((u.initialized = !0),
                  document.body.addEventListener("mouseenter", e),
                  document.body.addEventListener("mouseleave", t))
              : (0, a.R)(!1);
          }
          const i = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let a = !0;
                  const i = `mouse${e}`,
                    o = r[e]((u) => t([u, "outside"]));
                  function s(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(i, s),
                    n(),
                    () => {
                      a &&
                        (o(), window.removeEventListener(i, s), (u.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(t)),
              e
            ),
            {},
          );
          return Object.assign({}, i, {
            disable() {
              ((u.enabled = !1), n());
            },
            enable() {
              ((u.enabled = !0), n());
            },
            enableOutside() {
              u.enabled && (0, a.R)(!0);
            },
            disableOutside() {
              u.enabled && (0, a.R)(!1);
            },
          });
        })();
      },
      5959: (u, e, t) => {
        (t.r(e),
          t.d(e, {
            events: () => n,
            getMouseGlobalPosition: () => i,
            getSize: () => a,
            graphicsQuality: () => r,
          }));
        var n = t(527);
        function a(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function i(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const r = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (u, e, t) => {
        function n(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        t.d(e, { R: () => n });
      },
      2472: (u, e, t) => {
        function n(u) {
          return (e) => (
            engine.on(u, e),
            () => {
              engine.off(u, e);
            }
          );
        }
        t.d(e, { E: () => n });
      },
      3138: (u, e, t) => {
        t.d(e, { O: () => a });
        var n = t(5959);
        const a = { view: t(7641), client: n };
      },
      3722: (u, e, t) => {
        function n(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function a(u, e, t) {
          return `url(${n(u, e, t)})`;
        }
        (t.r(e), t.d(e, { getBgUrl: () => a, getTextureUrl: () => n }));
      },
      6112: (u, e, t) => {
        t.d(e, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (u, e, t) => {
        t.d(e, { U: () => a });
        var n = t(2472);
        const a = {
          onTextureFrozen: (0, n.E)("self.onTextureFrozen"),
          onTextureReady: (0, n.E)("self.onTextureReady"),
          onDomBuilt: (0, n.E)("self.onDomBuilt"),
          onLoaded: (0, n.E)("self.onLoaded"),
          onDisplayChanged: (0, n.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, n.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, n.E)("children.onAdded"),
            onLoaded: (0, n.E)("children.onLoaded"),
            onRemoved: (0, n.E)("children.onRemoved"),
            onAttached: (0, n.E)("children.onAttached"),
            onTextureReady: (0, n.E)("children.onTextureReady"),
            onRequestPosition: (0, n.E)("children.requestPosition"),
          },
        };
      },
      7641: (u, e, t) => {
        (t.r(e),
          t.d(e, {
            addModelObserver: () => l,
            addPreloadTexture: () => o,
            children: () => n,
            displayStatus: () => a.W,
            displayStatusIs: () => p,
            events: () => i.U,
            extraSize: () => k,
            forceTriggerMouseMove: () => f,
            freezeTextureBeforeResize: () => _,
            getBrowserTexturePath: () => E,
            getDisplayStatus: () => b,
            getScale: () => m,
            getSize: () => F,
            getViewGlobalPosition: () => c,
            isClientAccessible: () => h,
            isEventHandled: () => w,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => d,
            sendEvent: () => r.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => v,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => A,
            whenTutorialReady: () => S,
          }));
        var n = t(3722),
          a = t(6112),
          i = t(6538),
          r = t(8566);
        function o(u) {
          viewEnv.addPreloadTexture(u);
        }
        function s(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function E(u, e, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, n);
        }
        function l(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function A(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function F(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function d(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function c(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: B(e.x), y: B(e.y) };
        }
        function _() {
          viewEnv.freezeTextureBeforeResize();
        }
        function m() {
          return viewEnv.getScale();
        }
        function D(u) {
          return viewEnv.pxToRem(u);
        }
        function B(u) {
          return viewEnv.remToPx(u);
        }
        function C(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function g() {
          return viewEnv.isFocused();
        }
        function h() {
          return viewEnv.isClientAccessible();
        }
        function v() {
          return viewEnv.setEventHandled();
        }
        function w() {
          return viewEnv.isEventHandled();
        }
        function f() {
          viewEnv.forceTriggerMouseMove();
        }
        function b() {
          return viewEnv.getShowingStatus();
        }
        const p = Object.keys(a.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === a.W[e]), u),
            {},
          ),
          k = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          S = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : i.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        t.d(e, { qP: () => E });
        const n = ["args"];
        const a = 2,
          i = 16,
          r = 32,
          o = 64,
          s = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const i = e.args,
                r = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    a = {},
                    i = Object.keys(u);
                  for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                  return a;
                })(e, n);
              return void 0 !== i
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, r, {
                      arguments:
                        ((a = i),
                        Object.entries(a).map(([u, e]) => {
                          const t = "GFValueProxy";
                          switch (typeof e) {
                            case "number":
                              return { __Type: t, name: u, number: e };
                            case "boolean":
                              return { __Type: t, name: u, bool: e };
                            default:
                              return { __Type: t, name: u, string: e.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, r));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var a;
          },
          E = {
            close(u) {
              s("popover" === u ? a : r);
            },
            minimize() {
              s(o);
            },
            move(u) {
              s(i, { isMouseEvent: !0, on: u });
            },
          };
      },
      4598: (u, e, t) => {
        function n() {}
        t.d(e, { ZT: () => n });
        console.log;
      },
      7902: (u, e, t) => {
        t.d(e, { F: () => n });
        const n = (u = 1) => {
          const e = new Error().stack;
          let t,
            n = R.invalid("resId");
          return (
            e &&
              ((t = e.split("\n")[u].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== t &&
                window.subViews[t] &&
                (n = window.subViews[t].id)),
            { caller: t, stack: e, resId: n }
          );
        };
      },
      6536: (u, e, t) => {
        t.d(e, { Z: () => a });
        var n = t(6179);
        const a = (u) => {
          const e = (0, n.useRef)(!1);
          e.current || (u(), (e.current = !0));
        };
      },
      9924: (u, e, t) => {
        (t(6483), t(7739), t(5262), t(6179), t(3649));
      },
      5521: (u, e, t) => {
        let n, a;
        (t.d(e, { n: () => n }),
          (function (u) {
            ((u[(u.NONE = -1)] = "NONE"),
              (u[(u.ALT = 165)] = "ALT"),
              (u[(u.ENTER = 13)] = "ENTER"),
              (u[(u.ESCAPE = 27)] = "ESCAPE"),
              (u[(u.SPACE = 32)] = "SPACE"),
              (u[(u.END = 35)] = "END"),
              (u[(u.HOME = 36)] = "HOME"),
              (u[(u.ARROW_LEFT = 37)] = "ARROW_LEFT"),
              (u[(u.ARROW_UP = 38)] = "ARROW_UP"),
              (u[(u.ARROW_RIGHT = 39)] = "ARROW_RIGHT"),
              (u[(u.ARROW_DOWN = 40)] = "ARROW_DOWN"),
              (u[(u.NUM_PLUS = 107)] = "NUM_PLUS"),
              (u[(u.NUM_MINUS = 109)] = "NUM_MINUS"),
              (u[(u.PLUS = 187)] = "PLUS"),
              (u[(u.MINUS = 189)] = "MINUS"),
              (u[(u.PAGE_UP = 33)] = "PAGE_UP"),
              (u[(u.PAGE_DOWN = 34)] = "PAGE_DOWN"),
              (u[(u.BACKSPACE = 8)] = "BACKSPACE"),
              (u[(u.DELETE = 46)] = "DELETE"),
              (u[(u.TAB = 9)] = "TAB"),
              (u[(u.KEY_N = 78)] = "KEY_N"),
              (u[(u.KEY_0 = 48)] = "KEY_0"),
              (u[(u.KEY_1 = 49)] = "KEY_1"),
              (u[(u.KEY_2 = 50)] = "KEY_2"),
              (u[(u.KEY_3 = 51)] = "KEY_3"),
              (u[(u.KEY_4 = 52)] = "KEY_4"),
              (u[(u.KEY_5 = 53)] = "KEY_5"),
              (u[(u.KEY_6 = 54)] = "KEY_6"),
              (u[(u.KEY_7 = 55)] = "KEY_7"),
              (u[(u.KEY_8 = 56)] = "KEY_8"),
              (u[(u.KEY_9 = 57)] = "KEY_9"),
              (u[(u.CAPS_LOCK = 20)] = "CAPS_LOCK"),
              (u[(u.INSERT = 45)] = "INSERT"),
              (u[(u.F1 = 112)] = "F1"),
              (u[(u.F2 = 113)] = "F2"),
              (u[(u.F3 = 114)] = "F3"),
              (u[(u.F4 = 115)] = "F4"),
              (u[(u.F5 = 116)] = "F5"),
              (u[(u.F6 = 117)] = "F6"),
              (u[(u.F7 = 118)] = "F7"),
              (u[(u.F8 = 119)] = "F8"),
              (u[(u.F9 = 120)] = "F9"),
              (u[(u.F10 = 121)] = "F10"),
              (u[(u.F11 = 122)] = "F11"),
              (u[(u.F12 = 123)] = "F12"),
              (u[(u.SELECT = 93)] = "SELECT"),
              (u[(u.NUMPAD_0 = 96)] = "NUMPAD_0"),
              (u[(u.NUMPAD_1 = 97)] = "NUMPAD_1"),
              (u[(u.NUMPAD_2 = 98)] = "NUMPAD_2"),
              (u[(u.NUMPAD_3 = 99)] = "NUMPAD_3"),
              (u[(u.NUMPAD_4 = 100)] = "NUMPAD_4"),
              (u[(u.NUMPAD_5 = 101)] = "NUMPAD_5"),
              (u[(u.NUMPAD_6 = 102)] = "NUMPAD_6"),
              (u[(u.NUMPAD_7 = 103)] = "NUMPAD_7"),
              (u[(u.NUMPAD_8 = 104)] = "NUMPAD_8"),
              (u[(u.NUMPAD_9 = 105)] = "NUMPAD_9"),
              (u[(u.NUM_DECIMAL = 110)] = "NUM_DECIMAL"),
              (u[(u.STAR = 106)] = "STAR"),
              (u[(u.NUM_SLASH = 111)] = "NUM_SLASH"),
              (u[(u.FORWARD_SLASH = 191)] = "FORWARD_SLASH"),
              (u[(u.COMMA = 188)] = "COMMA"),
              (u[(u.DASH = 189)] = "DASH"),
              (u[(u.PERIOD = 190)] = "PERIOD"));
          })(n || (n = {})),
          (function (u) {
            ((u.ALT = "Alt"),
              (u.ALT_GRAPH = "AltGraph"),
              (u.CAPS_LOCK = "CapsLock"),
              (u.CONTROL = "Control"),
              (u.FN = "Fn"),
              (u.FN_LOCK = "FnLock"),
              (u.META = "Meta"),
              (u.NUM_LOCK = "NumLock"),
              (u.SCROLL_LOCK = "ScrollLock"),
              (u.SHIFT = "Shift"),
              (u.SYMBOL = "Symbol"),
              (u.SYMBOL_LOCK = "SymbolLock"));
          })(a || (a = {})));
      },
      3649: (u, e, t) => {
        let n;
        !(function (u) {
          ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
        })(n || (n = {}));
        (() => {
          const u = new RegExp(
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
      },
      1358: (u, e, t) => {
        t.d(e, { Z: () => i });
        var n = t(3138);
        class a {
          constructor() {
            ((this._callbacks = void 0),
              (this._updateHandler = void 0),
              (this._views = void 0),
              (this.clearViewCallbacks = (u) => {
                this._views[u] &&
                  (this._views[u].forEach((u) => {
                    delete this._callbacks[u];
                  }),
                  delete this._views[u]);
              }),
              (this._callbacks = {}),
              (this._views = {}),
              (this._updateHandler = void 0));
          }
          static get instance() {
            return (window.__dataTracker || (window.__dataTracker = new a()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(u, e, t = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const i = n.O.view.addModelObserver(u, t, a);
            return (
              i > 0
                ? ((this._callbacks[i] = e),
                  t > 0 && (this._views[t] ? this._views[t].push(i) : (this._views[t] = [i])))
                : console.error("Can't add callback for model:", u),
              i
            );
          }
          removeCallback(u, e = 0) {
            let t = !1;
            return (
              void 0 !== u &&
                void 0 !== this._callbacks[u] &&
                ((t = viewEnv.removeDataChangedCallback(u, e)), delete this._callbacks[u]),
              t || console.error("Can't remove callback by id:", u),
              t
            );
          }
          _emmitDataChanged(u, e, t) {
            t.forEach((t) => {
              const n = this._callbacks[t];
              void 0 !== n && n(u, e);
            });
          }
        }
        a.__instance = void 0;
        const i = a;
      },
      7572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
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
                  this.callbacks.forEach((u) => {
                    u(this.data);
                  }));
              }),
              (this.dataTracker = new _DataTracker__WEBPACK_IMPORTED_MODULE_0__.Z()),
              (this.modelPath = path),
              (this.callbacks = new Set()),
              (0, _index__WEBPACK_IMPORTED_MODULE_1__.ry)().then(() => {
                (this._addCallback(path),
                  watchingFields.forEach((u) => {
                    this._addCallback(path + "." + u);
                  }),
                  this._notifyObservers());
              }));
          }
          subscribe(u) {
            (this.callbacks.add(u), null !== this.data && void 0 !== this.data && u(this.data));
          }
          unsubscribe(u) {
            this.callbacks.delete(u);
          }
          destroy() {
            (this.dataTracker.clear(), this.callbacks.clear());
          }
          _addCallback(u) {
            this.dataTracker.addCallback(u, this._notifyObservers);
          }
        }
        const __WEBPACK_DEFAULT_EXPORT__ = ViewModel;
      },
      4179: (u, e, t) => {
        t.d(e, { B3: () => E, Gr: () => l, Z5: () => r, B0: () => s, ry: () => B });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (u) => {
                this.entries.forEach(({ container: e, callback: t }) => {
                  let n = u.target;
                  do {
                    if (n === e) return;
                    n = n.parentNode;
                  } while (n);
                  t();
                });
              }));
          }
          static get instance() {
            return (n.__instance || (n.__instance = new n()), n.__instance);
          }
          register(u, e) {
            (this.addMouseListener(), this.entries.push({ container: u, callback: e }));
          }
          unregister(u, e) {
            const t = u,
              n = e;
            ((this.entries = this.entries.filter(
              ({ container: u, callback: e }) => u !== t || e !== n,
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
        n.__instance = void 0;
        const a = n;
        var i = t(1358);
        const r = {
            getNumberFormat: (u, e) => systemLocale.getNumberFormat(u, e),
            getRealFormat: (u, e) => systemLocale.getRealFormat(u, e),
            getTimeFormat: (u, e) => systemLocale.getTimeFormat(u, e),
            getDateFormat: (u, e) => systemLocale.getDateFormat(u, e),
            toUpperCase: (u) => systemLocale.toUpperCase(u),
            toLowerCase: (u) => systemLocale.toUpperCase(u),
          },
          o = {
            getNumberFormat: (u) => userLocale.getNumberFormat(u),
            getTimeFormat: (u, e, t) => userLocale.getTimeFormat(u, e, void 0 === t || t),
            getTimeString: (u, e, t) => userLocale.getTimeString(u, e, void 0 === t || t),
          };
        let s;
        !(function (u) {
          ((u[(u.UNDEFINED = 0)] = "UNDEFINED"),
            (u[(u.TOOLTIP = 1)] = "TOOLTIP"),
            (u[(u.POP_OVER = 2)] = "POP_OVER"),
            (u[(u.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (u[(u.DROP_DOWN = 8)] = "DROP_DOWN"),
            (u[(u.MOVE = 16)] = "MOVE"),
            (u[(u.CLOSE = 32)] = "CLOSE"),
            (u[(u.MINIMIZE = 64)] = "MINIMIZE"));
        })(s || (s = {}));
        const E = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          l = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          A = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          F = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var d = t(5521),
          c = t(3138);
        const _ = ["args"];
        function m(u, e, t, n, a, i, r) {
          try {
            var o = u[i](r),
              s = o.value;
          } catch (u) {
            return void t(u);
          }
          o.done ? e(s) : Promise.resolve(s).then(n, a);
        }
        const D = (u) => ({
            __Type: "GFBoundingBox",
            x: u.x,
            y: u.y,
            width: u.width,
            height: u.height,
          }),
          B = (function () {
            var u,
              e =
                ((u = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((u) => {
                      engine.on("Ready", u);
                    })
                  );
                }),
                function () {
                  var e = this,
                    t = arguments;
                  return new Promise(function (n, a) {
                    var i = u.apply(e, t);
                    function r(u) {
                      m(i, n, a, r, o, "next", u);
                    }
                    function o(u) {
                      m(i, n, a, r, o, "throw", u);
                    }
                    r(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          C = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                i = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    a = {},
                    i = Object.keys(u);
                  for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                  return a;
                })(e, _);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, i, {
                      arguments:
                        ((n = a),
                        Object.entries(n).map(([u, e]) => {
                          const t = { __Type: "GFValueProxy", name: u };
                          switch (typeof e) {
                            case "number":
                              t.number = e;
                              break;
                            case "boolean":
                              t.bool = e;
                              break;
                            default:
                              t.string = e.toString();
                          }
                          return t;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, i));
            } else viewEnv.handleViewEvent({ __Type: t, type: u });
            var n;
          },
          g = () => C(s.CLOSE),
          h = (u, e) => {
            u.keyCode === d.n.ESCAPE && e();
          };
        var v = t(7572);
        const w = a.instance,
          f = {
            DataTracker: i.Z,
            ViewModel: v.Z,
            ViewEventType: s,
            NumberFormatType: E,
            RealFormatType: l,
            TimeFormatType: A,
            DateFormatType: F,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => C(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: g,
            sendClosePopOverEvent: () => C(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              C(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, n, a = R.invalid("resId"), i) => {
              const r = c.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                E = o.x,
                l = o.y,
                A = o.width,
                F = o.height,
                d = {
                  x: c.O.view.pxToRem(E) + r.x,
                  y: c.O.view.pxToRem(l) + r.y,
                  width: c.O.view.pxToRem(A),
                  height: c.O.view.pxToRem(F),
                };
              C(s.POP_OVER, {
                isMouseEvent: !0,
                contentID: u,
                decoratorID: n || R.invalid("resId"),
                targetID: a,
                direction: e,
                bbox: D(d),
                on: !0,
                args: i,
              });
            },
            addEscapeListener: (u) => {
              const e = (e) => h(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              h(u, g);
            },
            handleViewEvent: C,
            onBindingsReady: B,
            onLayoutReady: () =>
              new Promise((u) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    u();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
            dumpViewModel: function u(e) {
              const t = {};
              if ("object" != typeof e) return e;
              for (const n in e)
                if (Object.prototype.hasOwnProperty.call(e, n)) {
                  const a = Object.prototype.toString.call(e[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = e[n];
                    t[n] = [];
                    for (let e = 0; e < a.length; e++) t[n].push({ value: u(a[e].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = u(e[n]))
                      : (t[n] = e[n]);
                }
              return t;
            },
            ClickOutsideManager: w,
            SystemLocale: r,
            UserLocale: o,
          };
        window.ViewEnvHelper = f;
      },
      3486: (u, e, t) => {
        t.d(e, { Id: () => n });
        let n, a;
        (!(function (u) {
          ((u.B0 = "b0"),
            (u.B1 = "b1"),
            (u.B2 = "b2"),
            (u.B3 = "b3"),
            (u.B4 = "b4"),
            (u.B5 = "b5"),
            (u.B6 = "b6"));
        })(n || (n = {})),
          (function (u) {
            ((u.Small = "small"), (u.Medium = "medium"), (u.Big = "big"));
          })(a || (a = {})));
      },
      2100: (u, e, t) => {
        var n = t(6483),
          a = t.n(n),
          i = (t(7739), t(9924), t(6179)),
          r = t.n(i),
          o = t(3486),
          s = t(7078),
          E = t(2646),
          l = t(4179);
        const A = "BonusBattles_base_1b",
          F = "BonusBattles_light_51",
          d = "BonusBattles_divider_52",
          c = "BonusBattles_divider__right_08",
          _ = "BonusBattles_icon_2c",
          m = "BonusBattles_amount_a2",
          D = { tooltipId: E.T3 };
        (0, i.memo)((u) => {
          const e = u.amount,
            t = l.Z5.getNumberFormat(e, l.B3.INTEGRAL),
            n = a()(d, c);
          return r().createElement(
            s.t,
            { args: D },
            r().createElement(
              "div",
              { className: A },
              r().createElement("div", { className: F }),
              r().createElement("div", { className: d }),
              r().createElement("div", { className: _ }),
              r().createElement("div", { className: m }, t),
              r().createElement("div", { className: n }),
            ),
          );
        });
        let B, C;
        (!(function (u) {
          ((u.ExtraLarge = "extraLarge"),
            (u.Large = "large"),
            (u.Medium = "medium"),
            (u.SMedium = "smedium"),
            (u.Small = "small"),
            (u.ExtraSmall = "extraSmall"),
            (u.Tiny = "tiny"));
        })(B || (B = {})),
          (function (u) {
            ((u.Large = "large"),
              (u.Medium = "medium"),
              (u.SMedium = "smedium"),
              (u.Small = "small"),
              (u.ExtraSmall = "extraSmall"));
          })(C || (C = {})));
        const g = {
            base: "Blink_base_67",
            blink: "Blink_blink_75",
            blinker: "Blink_blinker_ef",
            widget: "Blink_widget_98",
            widgetBlinker: "Blink_widgetBlinker_14",
            widget__small: "Blink_widget__small_ea",
            widgetBlinkerSmall: "Blink_widgetBlinkerSmall_f2",
          },
          h = (0, i.memo)(({ isWidget: u = !1, size: e = C.Medium }) => {
            const t = a()(g.base, { [g.widget]: u, [g[`widget__${e}`]]: u });
            return r().createElement(
              "div",
              { className: t },
              r().createElement("div", { className: g.blink }),
            );
          }),
          v = {
            base: "Rank_base_80",
            icon: "Rank_icon_64",
            icon__extraSmall: "Rank_icon__extraSmall_ed",
            icon__medium: "Rank_icon__medium_c3",
            icon__large: "Rank_icon__large_65",
            icon__next: "Rank_icon__next_89",
            frame: "Rank_frame_88",
            frame__extraSmall: "Rank_frame__extraSmall_6a",
            frame__small: "Rank_frame__small_33",
            unburnable: "Rank_unburnable_65",
            unburnable__small: "Rank_unburnable__small_76",
            lock: "Rank_lock_01",
            lock__medium: "Rank_lock__medium_89",
            lock__extraSmall: "Rank_lock__extraSmall_c1",
            lock__small: "Rank_lock__small_6f",
          },
          w = {
            [C.Large]: "80x110",
            [C.Medium]: "58x80",
            [C.SMedium]: "58x80",
            [C.Small]: "42x56",
            [C.ExtraSmall]: "42x56",
          };
        (0, i.memo)((u) => {
          const e = u.isInactive,
            t = void 0 !== e && e,
            n = u.divisionID,
            o = u.rankName,
            l = u.rankID,
            A = u.isUnburnable,
            F = u.size,
            d = void 0 === F ? C.Medium : F,
            c = u.isLocked,
            _ = void 0 !== c && c,
            m = (0, i.useMemo)(() => {
              const u = R.images.gui.maps.icons.rankedBattles,
                e = w[d],
                t = u.ranks.$dyn(`c_${e}`),
                a = t && t.$dyn(`rank${n}_${o}`);
              return a ? { backgroundImage: `url(${a})` } : void 0;
            }, [n, o, d]),
            D = (u) => [v[u], v[`${u}__${d}`]],
            B = a()(v.icon, t && v.icon__next, ...D("icon")),
            g = a()(...D("frame"), ...D("unburnable")),
            f = a()(...D("lock")),
            b = d !== C.ExtraSmall;
          return r().createElement(
            s.t,
            { args: { rankID: l, tooltipId: E.MS } },
            r().createElement(
              "div",
              { className: v.base },
              r().createElement("div", { className: B, style: m }),
              A && r().createElement("div", { className: g }),
              !t && b && r().createElement(h, { isWidget: !0, size: d }),
              _ && r().createElement("div", { className: f, "data-emblem": "lock" }),
            ),
          );
        });
        E.u6;
        const f = {
          base: "RankedStat_base_29",
          icon: "RankedStat_icon_83",
          icon__efficiency: "RankedStat_icon__efficiency_9e",
          icon__efficiency__medium: "RankedStat_icon__efficiency__medium_e6",
          icon__position: "RankedStat_icon__position_6f",
          icon__position__medium: "RankedStat_icon__position__medium_10",
          value: "RankedStat_value_cb",
          value__medium: "RankedStat_value__medium_dc",
          delta: "RankedStat_delta_ff",
          delta__medium: "RankedStat_delta__medium_89",
          delta__smedium: "RankedStat_delta__smedium_74",
          delta__minus: "RankedStat_delta__minus_71",
          arrow: "RankedStat_arrow_97",
          arrow__medium: "RankedStat_arrow__medium_f8",
          arrow__smedium: "RankedStat_arrow__smedium_52",
          arrow__minus: "RankedStat_arrow__minus_e1",
        };
        let b, p;
        (!(function (u) {
          ((u.Efficiency = "efficiency"), (u.Position = "position"));
        })(b || (b = {})),
          (function (u) {
            ((u.Medium = "medium"), (u.SMedium = "smedium"));
          })(p || (p = {})));
        const k = {
            [b.Efficiency]: "rankedBattlesEfficiency",
            [b.Position]: "RANKED_BATTLES_POSITION_TOOLTIP",
          },
          S = (0, i.memo)(
            ({
              type: u,
              value: e,
              valueDiff: t = 0,
              isUnavailable: n = !1,
              isPercent: i = !1,
              size: o = p.Medium,
            }) => {
              const E = (u) =>
                  n
                    ? "---"
                    : i
                      ? l.Z5.getRealFormat(100 * u, l.Gr.WO_ZERO_DIGITS) + "%"
                      : l.Z5.getRealFormat(u, l.Gr.WO_ZERO_DIGITS),
                A = E(e),
                F = E(t);
              return r().createElement(
                s.t,
                { args: { tooltipId: k[u] } },
                r().createElement(
                  "div",
                  { className: a()(f.base, f[`base__${o}`]) },
                  r().createElement("div", {
                    className: a()(f.icon, f[`icon__${u}`], f[`icon__${u}__${o}`]),
                  }),
                  r().createElement("div", { className: a()(f.value, f[`value__${o}`]) }, A),
                  0 !== t &&
                    !n &&
                    r().createElement(
                      "div",
                      { className: a()(f.delta, f[`delta__${o}`], t < 0 && f.delta__minus) },
                      r().createElement("div", {
                        className: a()(f.arrow, f[`arrow__${o}`], t < 0 && f.arrow__minus),
                      }),
                      F,
                    ),
                ),
              );
            },
          ),
          x = 33,
          O = 0,
          y = !0,
          M = "play";
        const T = [
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
        function L() {
          return (
            (L =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            L.apply(this, arguments)
          );
        }
        const P = (0, i.memo)(function (u) {
            let e = u.width,
              t = u.height,
              n = u.getImageSource,
              a = u.frameCount,
              o = u.onAnimate,
              s = u.frameTime,
              E = void 0 === s ? x : s,
              l = u.initialFrameIndex,
              A = void 0 === l ? O : l,
              F = u.lastFrameIndex,
              d = void 0 === F ? a - 1 : F,
              c = u.loop,
              _ = void 0 === c ? y : c,
              m = u.state,
              D = void 0 === m ? M : m,
              B = u.onAnimationDone,
              C = u.onAnimationComplete,
              g = u.poster,
              h = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  i = Object.keys(u);
                for (n = 0; n < i.length; n++) ((t = i[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, T);
            const v = (0, i.useRef)(null);
            return (
              (0, i.useEffect)(() => {
                const u = v.current;
                if (!u) return;
                const e = u.getContext("2d"),
                  t = (t) => {
                    (e.clearRect(0, 0, u.width, u.height), e.drawImage(t.img, -t.x, -t.y));
                  };
                switch (D) {
                  case "play":
                    return (function () {
                      const u = H(A, d, n),
                        e = N(A, d),
                        a = window.setInterval(() => {
                          const n = e(),
                            i = u.get(n);
                          i
                            ? (null == o || o(n, i),
                              t(i),
                              n === d &&
                                (null == C || C(),
                                _ || (null == B || B(), window.clearInterval(a))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, E);
                      return () => window.clearInterval(a);
                    })();
                  case "stop":
                    return (function () {
                      const u = 0 === A && g ? { path: g, x: 0, y: 0 } : n(A),
                        e = new Image();
                      e.src = u.path;
                      const a = () => t(I(u, e));
                      return (
                        e.addEventListener("load", a),
                        () => e.removeEventListener("load", a)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [E, n, A, d, _, o, C, B, g, D]),
              r().createElement("canvas", L({}, h, { width: e, height: t, ref: v }))
            );
          }),
          N = (u, e) => {
            let t = u;
            return () => {
              const n = t;
              return ((t += 1), t > e && (t = u), n);
            };
          },
          I = (u, e) => Object.assign({}, u, { img: e }),
          H = (u, e, t) => {
            const n = new Map(),
              a = {};
            for (let i = u; i <= e; i++) {
              const u = t(i),
                e = a[u.path];
              if (e) n.set(i, I(u, e));
              else {
                const e = new Image();
                ((a[u.path] = e),
                  (e.src = u.path),
                  (e.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${i})`,
                      u.path,
                      `(${u.x},${u.y})`,
                    );
                  }),
                  n.set(i, I(u, e)));
              }
            }
            return n;
          };
        var W = t(3138),
          U = t(4598);
        const j = {
            base: "AnimatedBackground_base_12",
            widget: "AnimatedBackground_widget_3d",
            rays: "AnimatedBackground_rays_85",
            sunShineCanvas: "AnimatedBackground_sunShineCanvas_27",
            staticHighlight: "AnimatedBackground_staticHighlight_a8",
            widget__smedium: "AnimatedBackground_widget__smedium_a0",
            animation: "AnimatedBackground_animation_06",
            fadeIn: "AnimatedBackground_fadeIn_78",
            none: "AnimatedBackground_none_f0",
            raysAppearance: "AnimatedBackground_raysAppearance_7c",
            rotate: "AnimatedBackground_rotate_fa",
            "reverse-rotate": "AnimatedBackground_reverse-rotate_cc",
            slideUp: "AnimatedBackground_slideUp_64",
            fadeInWithScale: "AnimatedBackground_fadeInWithScale_ae",
            lockStartAnimation: "AnimatedBackground_lockStartAnimation_d6",
            lockEndAnimation: "AnimatedBackground_lockEndAnimation_17",
            fadeOut: "AnimatedBackground_fadeOut_50",
          },
          V = {
            width: 400,
            height: 400,
            frameCount: 50,
            chunk: { count: 2, rows: 5, columns: 5 },
            getChunkPath:
              ((z = "R.images.gui.maps.icons.sequence.sun_shine_big_sprite.sprite_"),
              (u) => `${z}${u}`),
          };
        var z;
        const G = (function (u) {
          const e = u.chunk,
            t = e.rows * e.columns;
          return (n) => {
            const a = n % t,
              i = (a % e.columns) * u.width,
              r = Math.trunc(a / e.columns) * u.height;
            return { path: u.getChunkPath(Math.trunc(n / t)), x: i, y: r };
          };
        })(V);
        let K;
        !(function (u) {
          ((u.Medium = "medium"), (u.SMedium = "smedium"), (u.ExtraSmall = "extraSmall"));
        })(K || (K = {}));
        const q = ({ className: u, isAnimated: e, isWidget: t, size: n }) => {
          const i = a()(u, j.base, { [j.animation]: e, [j.widget]: t, [j[`widget__${n}`]]: t });
          return r().createElement(
            "div",
            { className: i },
            W.O.client.graphicsQuality.isHigh()
              ? r().createElement(
                  r().Fragment,
                  null,
                  r().createElement(P, {
                    onAnimationDone: U.ZT,
                    width: V.width,
                    height: V.height,
                    frameCount: V.frameCount,
                    getImageSource: G,
                    frameTime: 50,
                    className: j.sunShineCanvas,
                  }),
                  r().createElement("div", { className: j.rays }),
                )
              : r().createElement("div", { className: j.staticHighlight }),
          );
        };
        var Y = t(6373);
        const $ = {
          base: "RankedStatBattles_base_f2",
          icon: "RankedStatBattles_icon_c5",
          icon__medium: "RankedStatBattles_icon__medium_f7",
          value: "RankedStatBattles_value_1d",
          value__medium: "RankedStatBattles_value__medium_34",
        };
        let Z;
        !(function (u) {
          ((u.Medium = "medium"), (u.SMedium = "smedium"));
        })(Z || (Z = {}));
        const X = (0, i.memo)(({ value: u, isUnavailable: e = !1, size: t = Z.Medium }) => {
            const n = ((u) => (e ? "---" : l.Z5.getRealFormat(u, l.Gr.WO_ZERO_DIGITS)))(u),
              i = R.strings.tooltips.rankedBattleView.stats.totalBattles;
            return r().createElement(
              Y.i,
              { header: i.$dyn("header"), body: i.$dyn("body") },
              r().createElement(
                "div",
                { className: a()($.base, $[`base__${t}`]) },
                r().createElement("div", { className: a()($.icon, $[`icon__${t}`]) }),
                r().createElement("div", { className: a()($.value, $[`value__${t}`]) }, n),
              ),
            );
          }),
          Q = {
            base: "League_base_18",
            base__extraSmall: "League_base__extraSmall_c7",
            base__smedium: "League_base__smedium_5e",
            base__medium: "League_base__medium_15",
            base__b2: "League_base__b2_c9",
            wrapper: "League_wrapper_91",
            icon: "League_icon_dd",
            base__small: "League_base__small_30",
          },
          J = { [C.Medium]: "100x100", [C.SMedium]: "70x70", [C.ExtraSmall]: "70x70" },
          uu = { tooltipId: E._Y };
        (0, i.memo)((u) => {
          const e = u.leagueID,
            t = u.efficiency,
            n = u.efficiencyDiff,
            E = u.isEfficiencyUnavailable,
            l = void 0 !== E && E,
            A = u.isBattlesUnavailable,
            F = void 0 !== A && A,
            d = u.size,
            c = u.battlesTotal,
            _ = u.cardSize,
            m = ![B.Small, B.ExtraSmall].includes(d),
            D = ![B.Small, B.ExtraSmall].includes(d),
            g = (0, i.useMemo)(
              () =>
                [B.Small, B.ExtraSmall].includes(d)
                  ? C.ExtraSmall
                  : B.SMedium === d
                    ? C.SMedium
                    : C.Medium,
              [d],
            ),
            h = (0, i.useMemo)(() => (d === B.SMedium ? p.SMedium : p.Medium), [d]),
            v = (0, i.useMemo)(
              () =>
                [B.Small, B.ExtraSmall].includes(d)
                  ? K.ExtraSmall
                  : d === B.SMedium
                    ? K.SMedium
                    : K.Medium,
              [d],
            ),
            w = (0, i.useMemo)(() => {
              const u = R.images.gui.maps.icons.rankedBattles.league,
                t = J[g],
                n = u.$dyn(`c_${t}`);
              if (n) {
                return { backgroundImage: `url(${n.$num(e)})` };
              }
            }, [e, g]);
          return r().createElement(
            "div",
            {
              className: a()(Q.base, Q[`base__${B.SMedium === d && _ === o.Id.B2 ? o.Id.B2 : d}`]),
            },
            m &&
              r().createElement(S, {
                type: b.Efficiency,
                value: t,
                valueDiff: n,
                isUnavailable: l,
                isPercent: !0,
                size: h,
              }),
            r().createElement(
              s.t,
              { args: uu },
              r().createElement(
                "div",
                { className: Q.wrapper },
                r().createElement("div", { className: Q.icon, style: w }),
                D && r().createElement(q, { isAnimated: !0, isWidget: !0, size: v }),
              ),
            ),
            m && r().createElement(X, { value: c, isUnavailable: F, size: h }),
          );
        });
      },
      2646: (u, e, t) => {
        t.d(e, { MS: () => a, T3: () => i, _Y: () => r, u6: () => n });
        const n = "rankedStep",
          a = "rankedBattlesRank",
          i = "rankedBattlesBonus",
          r = "rankedBattlesLeague";
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(u) {
    var e = __webpack_module_cache__[u];
    if (void 0 !== e) return e.exports;
    var t = (__webpack_module_cache__[u] = { exports: {} });
    return (__webpack_modules__[u](t, t.exports, __webpack_require__), t.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (u, e, t, n) => {
      if (!e) {
        var a = 1 / 0;
        for (s = 0; s < deferred.length; s++) {
          for (var [e, t, n] = deferred[s], i = !0, r = 0; r < e.length; r++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[r]))
              ? e.splice(r--, 1)
              : ((i = !1), n < a && (a = n));
          if (i) {
            deferred.splice(s--, 1);
            var o = t();
            void 0 !== o && (u = o);
          }
        }
        return u;
      }
      n = n || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > n; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [e, t, n];
    }),
    (__webpack_require__.n = (u) => {
      var e = u && u.__esModule ? () => u.default : () => u;
      return (__webpack_require__.d(e, { a: e }), e);
    }),
    (__webpack_require__.d = (u, e) => {
      for (var t in e)
        __webpack_require__.o(e, t) &&
          !__webpack_require__.o(u, t) &&
          Object.defineProperty(u, t, { enumerable: !0, get: e[t] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (u) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (u, e) => Object.prototype.hasOwnProperty.call(u, e)),
    (__webpack_require__.r = (u) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(u, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(u, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 153),
    (() => {
      var u = { 153: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var n,
            a,
            [i, r, o] = t,
            s = 0;
          if (i.some((e) => 0 !== u[e])) {
            for (n in r) __webpack_require__.o(r, n) && (__webpack_require__.m[n] = r[n]);
            if (o) var E = o(__webpack_require__);
          }
          for (e && e(t); s < i.length; s++)
            ((a = i[s]), __webpack_require__.o(u, a) && u[a] && u[a][0](), (u[a] = 0));
          return __webpack_require__.O(E);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [705], () => __webpack_require__(2100));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
