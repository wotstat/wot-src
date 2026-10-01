(() => {
  var __webpack_modules__ = {
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => l });
        var n = t(5238),
          r = t(6179),
          a = t.n(r);
        const s = ["children", "body", "header", "note", "alert", "args"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const i = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let u = e.children,
              t = e.body,
              l = e.header,
              c = e.note,
              E = e.alert,
              d = e.args,
              m = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, s);
            const _ = (0, r.useMemo)(() => {
              const e = Object.assign({}, d, { body: t, header: l, note: c, alert: E });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [E, t, l, c, d]);
            return a().createElement(
              n.u,
              o(
                {
                  contentId:
                    ((A = null == d ? void 0 : d.hasHtmlContent),
                    A ? i.SimpleTooltipHtmlContent("resId") : i.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: _,
                },
                m,
              ),
              u,
            );
            var A;
          };
      },
      5238: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => i });
        var n = t(4179),
          r = t(6179);
        const a = [
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
        function s(e) {
          return Object.entries(e || {}).map(([e, u]) => {
            const t = { __Type: "GFValueProxy", name: e };
            switch (typeof u) {
              case "number":
                t.number = u;
                break;
              case "boolean":
                t.bool = u;
                break;
              case "undefined":
                break;
              default:
                t.string = u.toString();
            }
            return t;
          });
        }
        const o = (e, u, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: n.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: r,
                },
                t,
              ),
            );
          },
          i = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              E = e.onClick,
              d = e.ignoreShowDelay,
              m = void 0 !== d && d,
              _ = e.ignoreMouseClick,
              A = void 0 !== _ && _,
              F = e.decoratorId,
              D = void 0 === F ? 0 : F,
              B = e.isEnabled,
              g = void 0 === B || B,
              C = e.targetId,
              p = void 0 === C ? 0 : C,
              h = e.onShow,
              f = e.onHide,
              b = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, a);
            const v = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, r.useMemo)(
                () =>
                  p ||
                  ((e = 1) => {
                    const u = new Error().stack;
                    let t,
                      n = R.invalid("resId");
                    return (
                      u &&
                        ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (n = window.subViews[t].id)),
                      { caller: t, stack: u, resId: n }
                    );
                  })().resId,
                [p],
              ),
              w = (0, r.useCallback)(() => {
                (v.current.isVisible && v.current.timeoutId) ||
                  (o(t, D, { isMouseEvent: !0, on: !0, arguments: s(n) }, S),
                  h && h(),
                  (v.current.isVisible = !0));
              }, [t, D, n, S, h]),
              x = (0, r.useCallback)(() => {
                if (v.current.isVisible || v.current.timeoutId) {
                  const e = v.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (v.current.timeoutId = 0)),
                    o(t, D, { on: !1 }, S),
                    v.current.isVisible && f && f(),
                    (v.current.isVisible = !1));
                }
              }, [t, D, S, f]),
              y = (0, r.useCallback)((e) => {
                v.current.isVisible &&
                  ((v.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (v.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(v.current.prevTarget) && x();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = v.current.hideTimerId;
              return (
                document.addEventListener("wheel", y, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", y, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === g && x();
              }, [g, x]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", x),
                  () => {
                    (window.removeEventListener("mouseleave", x), x());
                  }
                ),
                [x],
              ));
            return g
              ? (0, r.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((M = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((v.current.timeoutId = window.setTimeout(w, m ? 100 : 400)),
                            i && i(e),
                            M && M(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (x(), null == l || l(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === A && x(), null == E || E(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === A && x(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    b,
                  ),
                )
              : u;
            var M;
          };
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
      3532: (e) => {
        e.exports = {
          BLACK_REAL: "#000000",
          WHITE_REAL: "#FFFFFF",
          WHITE: "#F2F2F7",
          WHITE_ORANGE: "#FEFEEC",
          WHITE_SPANISH: "#E9E2BF",
          PAR: "#8C8C7E",
          PAR_SECONDARY: "#595950",
          PAR_TERTIARY: "#37362E",
          INFO_RED: "#FF0000",
          RED: "#FF2717",
          RED_DARK: "#B70000",
          YELLOW: "#FEAB34",
          ORANGE: "#EE7000",
          CREAM: "#FFDD99",
          BROWN: "#CBAC77",
          GREEN_BRIGHT: "#80D43A",
          GREEN: "#7AB300",
          GREEN_DARK: "#497212",
          BLUE_BOOSTER: "#CCFFFF",
          BLUE_TEAMKILLER: "#09E2FF",
          CRED: "#CED9D9",
          GOLD: "#FFC363",
          BOND: "#C9C9B6",
          PROM: "#A29B70",
        };
      },
      9887: (e) => {
        e.exports = {
          XS: "4rem",
          SM: "8rem",
          SMp: "10rem",
          MD: "16rem",
          MDp: "20rem",
          LG: "32rem",
          XL: "64rem",
        };
      },
      5067: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => Y });
        var n = {};
        (t.r(n), t.d(n, { mouse: () => E, onResize: () => l }));
        var r = {};
        (t.r(r),
          t.d(r, {
            events: () => n,
            getMouseGlobalPosition: () => m,
            getSize: () => d,
            graphicsQuality: () => _,
          }));
        var a = {};
        (t.r(a), t.d(a, { getBgUrl: () => F, getTextureUrl: () => A }));
        var s = {};
        function o(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        function i(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        (t.r(s),
          t.d(s, {
            addModelObserver: () => R,
            addPreloadTexture: () => S,
            children: () => a,
            displayStatus: () => D,
            displayStatusIs: () => X,
            events: () => B,
            extraSize: () => z,
            forceTriggerMouseMove: () => $,
            freezeTextureBeforeResize: () => P,
            getBrowserTexturePath: () => x,
            getDisplayStatus: () => V,
            getScale: () => N,
            getSize: () => M,
            getViewGlobalPosition: () => L,
            isClientAccessible: () => U,
            isEventHandled: () => G,
            isFocused: () => H,
            pxToRem: () => O,
            remToPx: () => k,
            resize: () => T,
            sendEvent: () => v,
            setAnimateWindow: () => I,
            setEventHandled: () => W,
            setInputPaddingsRem: () => w,
            setSidePaddingsRem: () => y,
            whenTutorialReady: () => j,
          }));
        const l = o("clientResized"),
          c = { down: o("mousedown"), up: o("mouseup"), move: o("mousemove") };
        const E = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && i(!1);
          }
          function t() {
            e.enabled && i(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : i(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const a = `mouse${u}`,
                    s = c[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, o),
                    n(),
                    () => {
                      r &&
                        (s(), window.removeEventListener(a, o), (e.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
            },
            enableOutside() {
              e.enabled && i(!0);
            },
            disableOutside() {
              e.enabled && i(!1);
            },
          });
        })();
        function d(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function m(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const _ = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function A(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function F(e, u, t) {
          return `url(${A(e, u, t)})`;
        }
        const D = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          B = {
            onTextureFrozen: o("self.onTextureFrozen"),
            onTextureReady: o("self.onTextureReady"),
            onDomBuilt: o("self.onDomBuilt"),
            onLoaded: o("self.onLoaded"),
            onDisplayChanged: o("self.onShowingStatusChanged"),
            onFocusUpdated: o("self.onFocusChanged"),
            children: {
              onAdded: o("children.onAdded"),
              onLoaded: o("children.onLoaded"),
              onRemoved: o("children.onRemoved"),
              onAttached: o("children.onAttached"),
              onTextureReady: o("children.onTextureReady"),
              onRequestPosition: o("children.requestPosition"),
            },
          },
          g = ["args"];
        const C = 2,
          p = 16,
          h = 32,
          f = 64,
          b = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, g);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, u]) => {
                          const t = "GFValueProxy";
                          switch (typeof u) {
                            case "number":
                              return { __Type: t, name: e, number: u };
                            case "boolean":
                              return { __Type: t, name: e, bool: u };
                            default:
                              return { __Type: t, name: e, string: u.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, a));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          v = {
            close(e) {
              b("popover" === e ? C : h);
            },
            minimize() {
              b(f);
            },
            move(e) {
              b(p, { isMouseEvent: !0, on: e });
            },
          };
        function S(e) {
          viewEnv.addPreloadTexture(e);
        }
        function w(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function x(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function R(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function y(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function M(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function T(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function L(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: k(u.x), y: k(u.y) };
        }
        function P() {
          viewEnv.freezeTextureBeforeResize();
        }
        function N() {
          return viewEnv.getScale();
        }
        function O(e) {
          return viewEnv.pxToRem(e);
        }
        function k(e) {
          return viewEnv.remToPx(e);
        }
        function I(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function H() {
          return viewEnv.isFocused();
        }
        function U() {
          return viewEnv.isClientAccessible();
        }
        function W() {
          return viewEnv.setEventHandled();
        }
        function G() {
          return viewEnv.isEventHandled();
        }
        function $() {
          viewEnv.forceTriggerMouseMove();
        }
        function V() {
          return viewEnv.getShowingStatus();
        }
        const X = Object.keys(D).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === D[u]), e),
            {},
          ),
          z = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          j = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : B.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          Y = { view: s, client: r };
      },
      5521: (e, u, t) => {
        "use strict";
        let n, r;
        (t.d(u, { n: () => n }),
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
          })(n || (n = {})),
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
      1358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var n = t(5067);
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
          addCallback(e, u, t = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = n.O.view.addModelObserver(e, t, r);
            return (
              a > 0
                ? ((this._callbacks[a] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(a) : (this._views[t] = [a])))
                : console.error("Can't add callback for model:", e),
              a
            );
          }
          removeCallback(e, u = 0) {
            let t = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((t = viewEnv.removeDataChangedCallback(e, u)), delete this._callbacks[e]),
              t || console.error("Can't remove callback by id:", e),
              t
            );
          }
          _emmitDataChanged(e, u, t) {
            t.forEach((t) => {
              const n = this._callbacks[t];
              void 0 !== n && n(e, u);
            });
          }
        }
        r.__instance = void 0;
        const a = r;
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
      4179: (e, u, t) => {
        "use strict";
        t.d(u, { B3: () => l, Z5: () => s, B0: () => i, ry: () => B });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let n = e.target;
                  do {
                    if (n === u) return;
                    n = n.parentNode;
                  } while (n);
                  t();
                });
              }));
          }
          static get instance() {
            return (n.__instance || (n.__instance = new n()), n.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              n = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== n,
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
        const r = n;
        var a = t(1358);
        const s = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
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
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(5521),
          _ = t(5067);
        const A = ["args"];
        function F(e, u, t, n, r, a, s) {
          try {
            var o = e[a](s),
              i = o.value;
          } catch (e) {
            return void t(e);
          }
          o.done ? u(i) : Promise.resolve(i).then(n, r);
        }
        const D = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          B = (function () {
            var e,
              u =
                ((e = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((e) => {
                      engine.on("Ready", e);
                    })
                  );
                }),
                function () {
                  var u = this,
                    t = arguments;
                  return new Promise(function (n, r) {
                    var a = e.apply(u, t);
                    function s(e) {
                      F(a, n, r, s, o, "next", e);
                    }
                    function o(e) {
                      F(a, n, r, s, o, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          g = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, u]) => {
                          const t = { __Type: "GFValueProxy", name: e };
                          switch (typeof u) {
                            case "number":
                              t.number = u;
                              break;
                            case "boolean":
                              t.bool = u;
                              break;
                            default:
                              t.string = u.toString();
                          }
                          return t;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, a));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          C = () => g(i.CLOSE),
          p = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var h = t(7572);
        const f = r.instance,
          b = {
            DataTracker: a.Z,
            ViewModel: h.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: d,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => g(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => g(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              g(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, r = R.invalid("resId"), a) => {
              const s = _.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                E = o.width,
                d = o.height,
                m = {
                  x: _.O.view.pxToRem(l) + s.x,
                  y: _.O.view.pxToRem(c) + s.y,
                  width: _.O.view.pxToRem(E),
                  height: _.O.view.pxToRem(d),
                };
              g(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: D(m),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => p(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              p(e, C);
            },
            handleViewEvent: g,
            onBindingsReady: B,
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
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const n in u)
                if (Object.prototype.hasOwnProperty.call(u, n)) {
                  const r = Object.prototype.toString.call(u[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = u[n];
                    t[n] = [];
                    for (let u = 0; u < r.length; u++) t[n].push({ value: e(r[u].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = e(u[n]))
                      : (t[n] = u[n]);
                }
              return t;
            },
            ClickOutsideManager: f,
            SystemLocale: s,
            UserLocale: o,
          };
        window.ViewEnvHelper = b;
      },
      307: (e, u, t) => {
        "use strict";
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => Yt,
            Bar: () => Xt,
            DefaultScroll: () => jt,
            Direction: () => Rt,
            defaultSettings: () => yt,
            useHorizontalScrollApi: () => Tt,
          }));
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => mn,
            Bar: () => cn,
            Default: () => dn,
            useVerticalScrollApi: () => qt,
          }));
        var a = t(6179),
          s = t.n(a);
        const o = (e, u, t) =>
          u.extraLargeHeight ||
          u.largeHeight ||
          u.mediumHeight ||
          u.smallHeight ||
          u.extraSmallHeight
            ? (u.extraLargeHeight && t.extraLarge) ||
              (u.largeHeight && t.large) ||
              (u.mediumHeight && t.medium) ||
              (u.smallHeight && t.small) ||
              (u.extraSmallHeight && t.extraSmall)
              ? e
              : null
            : e;
        var i = t(5067);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function E(e, u, t) {
          const n = (function (e, u) {
              switch (!0) {
                case e >= u.extraLarge.width:
                  return u.extraLarge.weight;
                case e >= u.large.width && e < u.extraLarge.width:
                  return u.large.weight;
                case e >= u.medium.width && e < u.large.width:
                  return u.medium.weight;
                case e >= u.small.width && e < u.medium.width:
                  return u.small.weight;
                default:
                  return u.extraSmall.weight;
              }
            })(e, t),
            r = (function (e, u) {
              switch (!0) {
                case e >= u.extraLarge.height:
                  return u.extraLarge.weight;
                case e >= u.large.height && e < u.extraLarge.height:
                  return u.large.weight;
                case e >= u.medium.height && e < u.large.height:
                  return u.medium.weight;
                case e >= u.small.height && e < u.medium.height:
                  return u.small.weight;
                default:
                  return u.extraSmall.weight;
              }
            })(u, t),
            a = Math.min(n, r);
          return {
            extraLarge: a === t.extraLarge.weight,
            large: a === t.large.weight,
            medium: a === t.medium.weight,
            small: a === t.small.weight,
            extraSmall: a === t.extraSmall.weight,
            extraLargeWidth: n === t.extraLarge.weight,
            largeWidth: n === t.large.weight,
            mediumWidth: n === t.medium.weight,
            smallWidth: n === t.small.weight,
            extraSmallWidth: n === t.extraSmall.weight,
            extraLargeHeight: r === t.extraLarge.weight,
            largeHeight: r === t.large.weight,
            mediumHeight: r === t.medium.weight,
            smallHeight: r === t.small.weight,
            extraSmallHeight: r === t.extraSmall.weight,
          };
        }
        !(function (e) {
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
        })(c || (c = {}));
        const d = i.O.client.getSize("rem"),
          m = d.width,
          _ = d.height,
          A = Object.assign({ width: m, height: _ }, E(m, _, l)),
          F = (0, a.createContext)(A),
          D = ["children"];
        const B = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, D);
          const n = (0, a.useContext)(F),
            r = n.extraLarge,
            s = n.large,
            i = n.medium,
            l = n.small,
            c = n.extraSmall,
            E = n.extraLargeWidth,
            d = n.largeWidth,
            m = n.mediumWidth,
            _ = n.smallWidth,
            A = n.extraSmallWidth,
            B = n.extraLargeHeight,
            g = n.largeHeight,
            C = n.mediumHeight,
            p = n.smallHeight,
            h = n.extraSmallHeight,
            f = { extraLarge: B, large: g, medium: C, small: p, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && r) return u;
            if (t.large && s) return u;
            if (t.medium && i) return u;
            if (t.small && l) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && E) return o(u, t, f);
            if (t.largeWidth && d) return o(u, t, f);
            if (t.mediumWidth && m) return o(u, t, f);
            if (t.smallWidth && _) return o(u, t, f);
            if (t.extraSmallWidth && A) return o(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return u;
              if (t.largeHeight && g) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && p) return u;
              if (t.extraSmallHeight && h) return u;
            }
          }
          return null;
        };
        B.defaultProps = {
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
        (0, a.memo)(B);
        const g = (e) => {
            const u = (0, a.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          C = (0, a.memo)(({ children: e }) => {
            const u = (0, a.useContext)(F),
              t = (0, a.useState)(u),
              n = t[0],
              r = t[1],
              o = (0, a.useCallback)((e, u) => {
                const t = i.O.view.pxToRem(e),
                  n = i.O.view.pxToRem(u);
                r(Object.assign({ width: t, height: n }, E(t, n, l)));
              }, []);
            (g(() => {
              engine.on("clientResized", o);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", o), [o]));
            const c = (0, a.useMemo)(() => Object.assign({}, n), [n]);
            return s().createElement(F.Provider, { value: c }, e);
          });
        var p = t(6483),
          h = t.n(p),
          f = t(926),
          b = t.n(f);
        let v, S, w;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(v || (v = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = l.small.width)] = "Small"),
              (e[(e.Medium = l.medium.width)] = "Medium"),
              (e[(e.Large = l.large.width)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
          })(S || (S = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.small.height)] = "Small"),
              (e[(e.Medium = l.medium.height)] = "Medium"),
              (e[(e.Large = l.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(w || (w = {})));
        const x = () => {
            const e = (0, a.useContext)(F),
              u = e.width,
              t = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return v.ExtraLarge;
                  case e.large:
                    return v.Large;
                  case e.medium:
                    return v.Medium;
                  case e.small:
                    return v.Small;
                  case e.extraSmall:
                    return v.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), v.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return S.ExtraLarge;
                  case e.largeWidth:
                    return S.Large;
                  case e.mediumWidth:
                    return S.Medium;
                  case e.smallWidth:
                    return S.Small;
                  case e.extraSmallWidth:
                    return S.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), S.ExtraSmall);
                }
              })(e),
              s = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return w.ExtraLarge;
                  case e.largeHeight:
                    return w.Large;
                  case e.mediumHeight:
                    return w.Medium;
                  case e.smallHeight:
                    return w.Small;
                  case e.extraSmallHeight:
                    return w.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), w.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: n,
              mediaWidth: r,
              mediaHeight: s,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          y = ["children", "className"];
        function M() {
          return (
            (M =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            M.apply(this, arguments)
          );
        }
        const T = {
            [S.ExtraSmall]: "",
            [S.Small]: b().SMALL_WIDTH,
            [S.Medium]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH}`,
            [S.Large]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH}`,
            [S.ExtraLarge]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH} ${b().EXTRA_LARGE_WIDTH}`,
          },
          L = {
            [w.ExtraSmall]: "",
            [w.Small]: b().SMALL_HEIGHT,
            [w.Medium]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT}`,
            [w.Large]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT}`,
            [w.ExtraLarge]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT} ${b().EXTRA_LARGE_HEIGHT}`,
          },
          P = {
            [v.ExtraSmall]: "",
            [v.Small]: b().SMALL,
            [v.Medium]: `${b().SMALL} ${b().MEDIUM}`,
            [v.Large]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE}`,
            [v.ExtraLarge]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE} ${b().EXTRA_LARGE}`,
          },
          N = (e) => {
            let u = e.children,
              t = e.className,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, y);
            const r = x(),
              a = r.mediaWidth,
              o = r.mediaHeight,
              i = r.mediaSize;
            return s().createElement("div", M({ className: h()(t, T[a], L[o], P[i]) }, n), u);
          },
          O = ["children"];
        const k = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, O);
          return s().createElement(C, null, s().createElement(N, t, u));
        };
        var I = t(493),
          H = t.n(I),
          U = t(9459);
        function W(e) {
          engine.call("PlaySound", e);
        }
        const G = {
            base: "TextButton_base_b6",
            base__right: "TextButton_base__right_39",
            icon: "TextButton_icon_17",
            icon__back: "TextButton_icon__back_43",
            icon__forward: "TextButton_icon__forward_59",
            icon__close: "TextButton_icon__close_53",
            icon__info: "TextButton_icon__info_33",
            glow: "TextButton_glow_a4",
            caption: "TextButton_caption_82",
            caption__back: "TextButton_caption__back_b9",
            caption__forward: "TextButton_caption__forward_4e",
            caption__close: "TextButton_caption__close_36",
            caption__info: "TextButton_caption__info_23",
            goto: "TextButton_goto_e7",
            base__left: "TextButton_base__left_ff",
            shine: "TextButton_shine_e2",
          },
          $ = [
            "caption",
            "onClick",
            "goto",
            "side",
            "type",
            "classNames",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onMouseUp",
            "soundClick",
            "soundHover",
          ];
        function V() {
          return (
            (V =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            V.apply(this, arguments)
          );
        }
        class X extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && W(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && W(this.props.soundClick));
              }),
              (this._onMouseUp = (e) => (u) => {
                (e && e(u), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const e = this.props,
              u = e.caption,
              t = e.onClick,
              n = e.goto,
              r = e.side,
              a = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              E = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(e, $)),
              m = h()(G.base, G[`base__${a}`], G[`base__${r}`], null == o ? void 0 : o.base),
              _ = h()(G.icon, G[`icon__${a}`], G[`icon__${r}`], null == o ? void 0 : o.icon),
              A = h()(G.glow, null == o ? void 0 : o.glow),
              F = h()(G.caption, G[`caption__${a}`], null == o ? void 0 : o.caption),
              D = h()(G.goto, null == o ? void 0 : o.goto);
            return s().createElement(
              "div",
              V(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(E),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                d,
              ),
              "info" !== a && s().createElement("div", { className: G.shine }),
              s().createElement(
                "div",
                { className: _ },
                s().createElement("div", { className: A }),
              ),
              s().createElement("div", { className: F }, u),
              n && s().createElement("div", { className: D }, n),
            );
          }
        }
        X.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const z = (e, u) => {
          let t;
          const n = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(n));
          };
        };
        var j = t(5521),
          Y = t(4179);
        const q = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function K(e = j.n.NONE, u = q, t = !1) {
          (0, a.useEffect)(() => {
            if (e !== j.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), u(n), t && n.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        let Q;
        !(function (e) {
          ((e[(e.Space = 32)] = "Space"),
            (e[(e.Enter = 13)] = "Enter"),
            (e[(e.A = 65)] = "A"),
            (e[(e.B = 66)] = "B"),
            (e[(e.C = 67)] = "C"),
            (e[(e.D = 68)] = "D"),
            (e[(e.E = 69)] = "E"),
            (e[(e.F = 70)] = "F"),
            (e[(e.G = 71)] = "G"),
            (e[(e.H = 72)] = "H"),
            (e[(e.I = 73)] = "I"),
            (e[(e.J = 74)] = "J"),
            (e[(e.K = 75)] = "K"),
            (e[(e.L = 76)] = "L"),
            (e[(e.M = 77)] = "M"),
            (e[(e.N = 78)] = "N"),
            (e[(e.O = 79)] = "O"),
            (e[(e.P = 80)] = "P"),
            (e[(e.Q = 81)] = "Q"),
            (e[(e.R = 82)] = "R"),
            (e[(e.S = 83)] = "S"),
            (e[(e.T = 84)] = "T"),
            (e[(e.U = 85)] = "U"),
            (e[(e.V = 86)] = "V"),
            (e[(e.W = 87)] = "W"),
            (e[(e.X = 88)] = "X"),
            (e[(e.Y = 89)] = "Y"),
            (e[(e.Z = 90)] = "Z"));
        })(Q || (Q = {}));
        const Z = (e = {}) => {
          (0, a.useEffect)(() => {
            const u = (u) => {
              if (!u.altKey && !u.ctrlKey && !u.shiftKey) {
                const t = e[u.keyCode];
                "function" == typeof t && t(u);
              }
            };
            return (
              window.addEventListener("keyup", u),
              () => {
                window.removeEventListener("keyup", u);
              }
            );
          }, [e]);
        };
        var J = t(3403);
        let ee;
        !(function (e) {
          ((e[(e.NonSet = 0)] = "NonSet"),
            (e[(e.Debug = 10)] = "Debug"),
            (e[(e.Info = 20)] = "Info"),
            (e[(e.Warning = 30)] = "Warning"));
        })(ee || (ee = {}));
        let ue;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(ue || (ue = {}));
        const te = "metrics",
          ne = ({ partnerID: e, item: u, parentScreen: t, itemState: n, info: r }) => ({
            item: u,
            partnerID: e || null,
            parent_screen: t || null,
            item_state: n || null,
            additional_info: r || null,
          }),
          re = (e, u) => {
            const t = (0, a.useCallback)(
              (t, n = ee.Info, r) => {
                (r || (r = {}),
                  Object.keys(r).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: u,
                      action: t,
                      logLevel: n,
                      params: JSON.stringify(r),
                    }));
              },
              [e, u],
            );
            return (e, u, n) => t(e, u, n);
          };
        let ae, se;
        function oe() {}
        (!(function (e) {
          e.RewardsScreen = "sa_rewards_screen";
        })(ae || (ae = {})),
          (function (e) {
            ((e.GoToShopButton = "goto_shop_button"),
              (e.ConfirmButton = "confirm_button"),
              (e.CloseButton = "close_button"));
          })(se || (se = {})));
        function ie() {
          return !1;
        }
        console.log;
        var le = t(9174);
        function ce(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return Ee(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Ee(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Ee(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const de = (e) => (0 === e ? window : window.subViews.get(e));
        function me(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, n) => u(null == e ? void 0 : e.value, t, n));
        }
        const _e = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? me(e, (e) => ("object" == typeof e ? _e(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? _e(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? _e(u) : u]),
                    )
              : e,
          Ae = (e) => _e(e);
        var Fe = t(3946);
        const De = ["AT", "BT"],
          Be = ((e, u) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: n = "real", options: r, children: o, mocks: l }) {
                const c = (0, a.useRef)([]),
                  E = (t, n, r) => {
                    var a;
                    const s = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = de,
                        context: n = "model",
                      } = {}) {
                        const r = new Map();
                        function a(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = r.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const s = (e) => {
                          const r = t(u),
                            a = n.split(".").reduce((e, u) => e[u], r);
                          return "string" != typeof e || 0 === e.length
                            ? a
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, a);
                        };
                        return {
                          subscribe: (t, a) => {
                            const o = "string" == typeof a ? `${n}.${a}` : n,
                              l = i.O.view.addModelObserver(o, u, !0);
                            return (r.set(l, t), e && t(s(a)), l);
                          },
                          readByPath: s,
                          createCallback: (e, u) => {
                            const t = s(u);
                            return (...u) => {
                              t(e(...u));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const u = s(e);
                            return () => {
                              u();
                            };
                          },
                          dispose: function () {
                            for (var e, t = ce(r.keys()); !(e = t()).done;) a(e.value, u);
                          },
                          unsubscribe: a,
                        };
                      })(n),
                      o =
                        "real" === t
                          ? s
                          : Object.assign({}, s, {
                              readByPath:
                                null != (a = null == r ? void 0 : r.getter) ? a : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == r ? void 0 : r.getter(e)) : o.readByPath(e),
                      E = (e) => c.current.push(e),
                      d = e({
                        mode: t,
                        readByPath: l,
                        externalModel: o,
                        observableModel: {
                          array: (e, u) => {
                            const n = null != u ? u : l(e),
                              r = le.LO.box(n, { equals: ie });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, le.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, u) => {
                            const n = null != u ? u : l(e),
                              r = le.LO.box(n, { equals: ie });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, le.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, u) => {
                            const n = l(u);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, u) => ((e[u] = le.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, le.aD)((u) => {
                                      e.forEach((e) => {
                                        r[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                r
                              );
                            }
                            {
                              const r = e,
                                a = Object.entries(r),
                                s = a.reduce((e, [u, t]) => ((e[t] = le.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, le.aD)((e) => {
                                      a.forEach(([u, t]) => {
                                        s[t].set(e[u]);
                                      });
                                    }),
                                    u,
                                  ),
                                s
                              );
                            }
                          },
                        },
                        cleanup: E,
                      }),
                      m = { mode: t, model: d, externalModel: o, cleanup: E };
                    return {
                      model: d,
                      controls: "mocks" === t && r ? r.controls(m) : u(m),
                      externalModel: o,
                      mode: t,
                    };
                  },
                  d = (0, a.useRef)(!1),
                  m = (0, a.useState)(n),
                  _ = m[0],
                  A = m[1],
                  F = (0, a.useState)(() => E(n, r, l)),
                  D = F[0],
                  B = F[1];
                return (
                  (0, a.useEffect)(() => {
                    d.current ? B(E(_, r, l)) : (d.current = !0);
                  }, [l, _, r]),
                  (0, a.useEffect)(() => {
                    A(n);
                  }, [n]),
                  (0, a.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [D],
                  ),
                  s().createElement(t.Provider, { value: D }, o)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  vehicles: e.array("vehicles", []),
                  bonuses: e.array("bonuses", []),
                  mainBonuses: e.array("mainBonuses", []),
                },
                t = (0, Fe.Om)(() => Ae(u.bonuses.get())),
                n = (0, Fe.Om)(() => u.root.get().specialCurrencyCount > 0),
                r = (0, Fe.Om)(() => u.mainBonuses.get().length),
                a = (0, Fe.Om)(() => {
                  const e = [],
                    t = Ae(u.mainBonuses.get());
                  if ((r() && t.forEach((u) => e.push(u)), n())) {
                    const u = { name: "awardCoin" };
                    if ((e.push(u), e.length >= 3)) {
                      var a = [e[2], e[1]];
                      ((e[1] = a[0]), (e[2] = a[1]));
                    }
                  }
                  return e;
                }),
                s = (0, Fe.Om)(() => me(u.vehicles.get(), (e) => Object.assign({}, e))),
                o = (0, Fe.Om)(() => {
                  const e = u.root
                    .get()
                    .category.replace(/^\D+/g, "")
                    .replace(/[^0-9]/g, "");
                  return parseInt(e, 10);
                }),
                i = (0, Fe.Om)(() => {
                  const e = u.root.get().category;
                  return De.includes(e);
                }),
                l = (0, Fe.Om)(() => Boolean(a().length), { equals: ie });
              return Object.assign({}, u, {
                computes: {
                  getBonuses: t,
                  getMainBonuses: a,
                  getHasVehicles: (0, Fe.Om)(() => u.vehicles.get().length > 0),
                  getVehicles: s,
                  getBonusesLength: (0, Fe.Om)(() => u.bonuses.get().length),
                  getMainBonusesLength: r,
                  getIsShopAvailable: (0, Fe.Om)(() => !u.root.get().isShopOnOpenLocked),
                  getCoinsCount: (0, Fe.Om)(() => u.root.get().specialCurrencyCount),
                  getPlayingYearsFromCategory: o,
                  hasTestersCategory: i,
                  getHasCoins: n,
                  hasMainRewards: l,
                },
              });
            },
            ({ externalModel: e }) => ({
              onOpenBtnClick: e.createCallbackNoArgs("onOpenBtnClick"),
            }),
          ),
          ge = Be[0],
          Ce = Be[1];
        var pe = t(9762),
          he = t(4734);
        let fe, be;
        (!(function (e) {
          ((e.Vehicles = "vehicles"), (e.Ribbon = "ribbon"));
        })(fe || (fe = {})),
          (function (e) {
            ((e.ShowMoreRewards = "showMoreRewards"), (e.ToVehicles = "toVehicles"));
          })(be || (be = {})));
        let ve, Se, we, xe, Re, ye, Me, Te, Le;
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
            (e.PortalEventDiscount25 = "portalEventDiscountToken"),
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
            (e.RewardsSlots = "rewardsSlots"),
            (e.RazlomCoin = "razlom_coin"));
        })(ve || (ve = {})),
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
          })(Se || (Se = {})),
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
          })(we || (we = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(xe || (xe = {})),
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
          })(Re || (Re = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(ye || (ye = {})),
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
          })(Me || (Me = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(Te || (Te = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Le || (Le = {})));
        class Pe extends s().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = Y.B3.GOLD;
            else e = Y.B3.INTEGRAL;
            const u = Y.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        Pe.defaultProps = { format: "integral" };
        const Ne = [
            ve.Items,
            ve.Equipment,
            ve.Xp,
            ve.XpFactor,
            ve.Blueprints,
            ve.BlueprintsAny,
            ve.Goodies,
            ve.Berths,
            ve.Slots,
            ve.Tokens,
            ve.CrewSkins,
            ve.CrewBooks,
            ve.Customizations,
            ve.CreditsFactor,
            ve.TankmenXp,
            ve.TankmenXpFactor,
            ve.FreeXpFactor,
            ve.BattleToken,
            ve.PremiumUniversal,
            ve.NaturalCover,
            ve.BpCoin,
            ve.BattlePassSelectToken,
            ve.BattlaPassFinalAchievement,
            ve.BattleBadge,
            ve.BonusX5,
            ve.CrewBonusX3,
            ve.NewYearFillers,
            ve.NewYearInvoice,
            ve.EpicSelectToken,
            ve.Comp7TokenWeeklyReward,
            ve.Comp7TokenCouponReward,
            ve.BattleBoosterGift,
            ve.CosmicLootboxCommon,
            ve.CosmicLootboxSilver,
            ve.SelectableBonus,
            ve.PostStamp,
            ve.PremiumPlusUniversal,
            ve.GoldenTicket,
            ve.RewardsSlots,
          ],
          Oe = [ve.Gold, ve.Credits, ve.Crystal, ve.FreeXp],
          ke = [ve.BattlePassPoints],
          Ie = [ve.PremiumPlus, ve.Premium];
        let He;
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
        })(He || (He = {}));
        const Ue = (e) =>
            Ne.includes(e)
              ? xe.MULTI
              : Oe.includes(e)
                ? xe.CURRENCY
                : ke.includes(e)
                  ? xe.NUMBER
                  : Ie.includes(e)
                    ? xe.PREMIUM_PLUS
                    : xe.STRING,
          We = ["engravings", "backgrounds"],
          Ge = ["engraving", "background"],
          $e = (e, u = we.Small) => {
            const t = e.name,
              n = e.type,
              r = e.value,
              a = e.icon,
              s = e.item,
              o = e.dogTagType,
              i = ((e) => {
                switch (e) {
                  case we.S600x450:
                    return "c_600x450";
                  case we.S400x300:
                    return "c_400x300";
                  case we.S296x222:
                    return "c_296x222";
                  case we.S232x174:
                    return "c_232x174";
                  case we.Big:
                    return "c_80x80";
                  case we.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_${r}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${r}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${r}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${s}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${a}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case we.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case we.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${a}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const n = We[e];
                  if (n) {
                    const r = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(n),
                      a = r.$dyn(t);
                    return a ? `${a}` : `${r.$dyn(Ge[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, u, a);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${i}.${a}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case we.S600x450:
                      return "c_600x450";
                    case we.S400x300:
                      return "c_400x300";
                    case we.S296x222:
                      return "c_296x222";
                    case we.S232x174:
                      return "c_232x174";
                    case we.S180x135:
                      return "big";
                    case we.Big:
                    case we.S80x80:
                      return "c_80x80";
                    case we.Small:
                    case we.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${a}`;
              case "xp":
              case "xpFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.exp`;
              case "creditsFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.credits`;
              case "tankmenXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.tankmenXP`;
              case "dailyXPFactor":
              case "freeXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.freeXP`;
              case "tmanToken":
              case "battlePassSelectToken":
              case "selectableBonus":
              case "groups":
              case "lootBoxToken":
              case "customizations":
              case "crewSkins":
              case "goodies":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${i}.${a}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case we.Mini:
                      return He.s32;
                    case we.Small:
                    case we.S48x48:
                      return He.s48;
                    case we.S80x80:
                    case we.Big:
                      return He.s80;
                    case we.S128x100:
                      return He.s116;
                    case we.S180x135:
                    case we.S232x174:
                    case we.S296x222:
                      return He.s296;
                    case we.S400x300:
                      return He.s400;
                    case we.S600x450:
                      return He.s600;
                  }
                })(u)}`;
              case ve.StyleProgress:
              case ve.LbStyleProgress:
                return je(a, u, Le.ProgressionStyle);
              case "portal":
                return `R.images.gui.maps.icons.rewards.${u}.${s}`;
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          Ve = (e, u, t) => {
            const n = u && { contentId: u };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || u),
                ignoreMouseClick: !0,
                ignoreShowDelay: !u,
              },
              n,
              t,
            );
          },
          Xe = (e) => {
            if (void 0 === e) return null;
            switch (e) {
              case Re.BATTLE_BOOSTER:
                return Me.BATTLE_BOOSTER;
              case Re.BATTLE_BOOSTER_REPLACE:
                return Me.BATTLE_BOOSTER_REPLACE;
              case Re.BUILT_IN_EQUIPMENT:
                return Me.BUILT_IN_EQUIPMENT;
              case Re.EQUIPMENT_PLUS:
                return Me.EQUIPMENT_PLUS;
              case Re.EQUIPMENT_TROPHY_BASIC:
                return Me.EQUIPMENT_TROPHY_BASIC;
              case Re.EQUIPMENT_TROPHY_UPGRADED:
                return Me.EQUIPMENT_TROPHY_UPGRADED;
              case Re.EQUIPMENT_MODERNIZED_UPGRADED_1:
                return Me.EQUIPMENT_MODERNIZED_UPGRADED_1;
              case Re.EQUIPMENT_MODERNIZED_UPGRADED_2:
                return Me.EQUIPMENT_MODERNIZED_UPGRADED_2;
              case Re.EQUIPMENT_MODERNIZED_UPGRADED_3:
                return Me.EQUIPMENT_MODERNIZED_UPGRADED_3;
              case Re.PROGRESSION_STYLE_UPGRADED_1:
                return Me.PROGRESSION_STYLE_UPGRADED_1;
              case Re.PROGRESSION_STYLE_UPGRADED_2:
                return Me.PROGRESSION_STYLE_UPGRADED_2;
              case Re.PROGRESSION_STYLE_UPGRADED_3:
                return Me.PROGRESSION_STYLE_UPGRADED_3;
              case Re.PROGRESSION_STYLE_UPGRADED_4:
                return Me.PROGRESSION_STYLE_UPGRADED_4;
            }
          },
          ze = (e, u) => {
            if (void 0 === e) return null;
            switch (u) {
              case xe.MULTI: {
                const u = Number(e);
                return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
              }
              case xe.CURRENCY:
              case xe.NUMBER:
                return s().createElement(Pe, { format: "integral", value: Number(e) });
              case xe.PREMIUM_PLUS: {
                const u = Number(e);
                return isNaN(u) ? e : null;
              }
              default:
                return e;
            }
          },
          je = (e, u, t) => {
            const n = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              r = n.$dyn(e);
            return String(null != r ? r : n.$dyn(t));
          };
        var Ye = t(9887),
          qe = t.n(Ye);
        const Ke = ["xl", "lg", "md", "sm", "xs"],
          Qe = (e) => e.includes("_") && ((e) => Ke.includes(e))(e.split("_").at(-1)),
          Ze = [v.ExtraLarge, v.Large, v.Medium, v.Small, v.ExtraSmall],
          Je = (e, u) =>
            Object.keys(e).reduce((t, n) => {
              if (n in t) return t;
              if (Qe(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const a = Ze.indexOf(u),
                  s = (-1 !== a ? Ke.slice(a) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  o = s ? e[s] : void 0;
                return ((t[r] = void 0 !== o ? o : e[r]), t);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, u) => Ke.some((t) => void 0 !== u[`${e}_${t}`]))(n, e) ||
                  (t[n] = r),
                t
              );
            }, {}),
          eu = (e, u = Je) => {
            const t = (
              (e, u = Je) =>
              (t) => {
                const n = x().mediaSize,
                  r = (0, a.useMemo)(() => u(t, n), [t, n]);
                return s().createElement(e, r);
              }
            )(e, u);
            return s().memo((u) =>
              Object.keys(u).some((e) => Qe(e) && void 0 !== u[e])
                ? s().createElement(t, u)
                : s().createElement(e, u),
            );
          },
          uu = {
            mt__XS: "Box_mt__XS_0c",
            mt__SM: "Box_mt__SM_eb",
            mt__SMp: "Box_mt__SMp_cf",
            mt__MD: "Box_mt__MD_25",
            mt__MDp: "Box_mt__MDp_49",
            mt__LG: "Box_mt__LG_e8",
            mt__XL: "Box_mt__XL_83",
            mr__XS: "Box_mr__XS_7c",
            mr__SM: "Box_mr__SM_08",
            mr__SMp: "Box_mr__SMp_06",
            mr__MD: "Box_mr__MD_4a",
            mr__MDp: "Box_mr__MDp_b6",
            mr__LG: "Box_mr__LG_d0",
            mr__XL: "Box_mr__XL_db",
            mb__XS: "Box_mb__XS_bb",
            mb__SM: "Box_mb__SM_83",
            mb__SMp: "Box_mb__SMp_04",
            mb__MD: "Box_mb__MD_ed",
            mb__MDp: "Box_mb__MDp_65",
            mb__LG: "Box_mb__LG_c8",
            mb__XL: "Box_mb__XL_f8",
            ml__XS: "Box_ml__XS_8a",
            ml__SM: "Box_ml__SM_e6",
            ml__SMp: "Box_ml__SMp_fb",
            ml__MD: "Box_ml__MD_2b",
            ml__MDp: "Box_ml__MDp_c7",
            ml__LG: "Box_ml__LG_39",
            ml__XL: "Box_ml__XL_4a",
          },
          tu = [
            "className",
            "width",
            "height",
            "m",
            "mt",
            "mr",
            "mb",
            "ml",
            "column",
            "row",
            "flexDirection",
            "flexStart",
            "center",
            "flexEnd",
            "spaceBetween",
            "spaceAround",
            "justifyContent",
            "alignItems",
            "alignSelf",
            "wrap",
            "flexWrap",
            "grow",
            "shrink",
            "flex",
            "style",
            "children",
          ];
        function nu() {
          return (
            (nu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            nu.apply(this, arguments)
          );
        }
        Object.keys(qe());
        const ru = {
            XL: { mt: uu.mt__XL, mr: uu.mr__XL, mb: uu.mb__XL, ml: uu.ml__XL },
            LG: { mt: uu.mt__LG, mr: uu.mr__LG, mb: uu.mb__LG, ml: uu.ml__LG },
            MDp: { mt: uu.mt__MDp, mr: uu.mr__MDp, mb: uu.mb__MDp, ml: uu.ml__MDp },
            MD: { mt: uu.mt__MD, mr: uu.mr__MD, mb: uu.mb__MD, ml: uu.ml__MD },
            SMp: { mt: uu.mt__SMp, mr: uu.mr__SMp, mb: uu.mb__SMp, ml: uu.ml__SMp },
            SM: { mt: uu.mt__SM, mr: uu.mr__SM, mb: uu.mb__SM, ml: uu.ml__SM },
            XS: { mt: uu.mt__XS, mr: uu.mr__XS, mb: uu.mb__XS, ml: uu.ml__XS },
          },
          au = (Object.keys(ru), ["mt", "mr", "mb", "ml"]),
          su = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          ou = eu((e) => {
            let u = e.className,
              t = e.width,
              n = e.height,
              r = e.m,
              o = e.mt,
              i = void 0 === o ? r : o,
              l = e.mr,
              c = void 0 === l ? r : l,
              E = e.mb,
              d = void 0 === E ? r : E,
              m = e.ml,
              _ = void 0 === m ? r : m,
              A = e.column,
              F = e.row,
              D = e.flexDirection,
              B = void 0 === D ? (A ? "column" : F && "row") || void 0 : D,
              g = e.flexStart,
              C = e.center,
              p = e.flexEnd,
              f = e.spaceBetween,
              b = e.spaceAround,
              v = e.justifyContent,
              S =
                void 0 === v
                  ? (g ? "flex-start" : C && "center") ||
                    (p && "flex-end") ||
                    (f && "space-between") ||
                    (b && "space-around") ||
                    void 0
                  : v,
              w = e.alignItems,
              x =
                void 0 === w
                  ? (g ? "flex-start" : C && "center") || (p && "flex-end") || void 0
                  : w,
              R = e.alignSelf,
              y = e.wrap,
              M = e.flexWrap,
              T = void 0 === M ? (y ? "wrap" : void 0) : M,
              L = e.grow,
              P = e.shrink,
              N = e.flex,
              O = void 0 === N ? (L || P ? `${L ? 1 : 0} ${P ? 1 : 0} auto` : void 0) : N,
              k = e.style,
              I = e.children,
              H = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, tu);
            const U = (0, a.useMemo)(() => {
                const e = { mt: i, mr: c, mb: d, ml: _ },
                  u = ((e) =>
                    au.reduce((u, t) => {
                      const n = e[t];
                      return n && "number" != typeof n ? u.concat(ru[!0 === n ? "MD" : n][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    au.reduce((u, t) => {
                      const n = e[t];
                      return ("number" == typeof n && (u[su[t]] = n + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, k, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: O,
                    alignSelf: R,
                    display: B || x ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: T,
                    justifyContent: S,
                    alignItems: x,
                  }),
                  computedClassNames: u,
                };
              }, [t, n, i, c, d, _, k, O, R, B, T, S, x]),
              W = U.computedStyle,
              G = U.computedClassNames;
            return s().createElement(
              "div",
              nu({ className: h()(uu.base, ...G, u), style: W }, H),
              I,
            );
          });
        let iu;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(iu || (iu = {}));
        const lu = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          cu = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          Eu = (e, u, t = iu.left) => e.split(u).reduce(t === iu.left ? lu : cu, []),
          du = (() => {
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
            return (u) =>
              u
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          mu = ["zh_cn", "zh_sg", "zh_tw"],
          _u = (e, u = iu.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return mu.includes(t)
              ? du(e)
              : ((e, u = iu.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (Eu(r, /( )/, u).forEach((e) => (t = t.concat(Eu(e, n, iu.left)))), t);
                })(e, u);
          },
          Au = "FormatText_base_d0",
          Fu = ({ binding: e, text: u = "", classMix: t, alignment: n = iu.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : s().createElement(
                  a.Fragment,
                  null,
                  u.split("\n").map((u, r) =>
                    s().createElement(
                      "div",
                      { className: h()(Au, t), key: `${u}-${r}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : _u(e, u))))(u, n, e).map((e, u) =>
                        s().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var Du = t(3532),
          Bu = t.n(Du);
        const gu = {
            "paragraph-P10": "Text_paragraph-P10_2c",
            "paragraph-P12": "Text_paragraph-P12_22",
            "paragraph-P14": "Text_paragraph-P14_a7",
            "paragraph-P16": "Text_paragraph-P16_90",
            "paragraph-P18": "Text_paragraph-P18_50",
            "paragraph-P24": "Text_paragraph-P24_33",
            "heading-H14": "Text_heading-H14_8b",
            "heading-H15": "Text_heading-H15_9e",
            "heading-H18": "Text_heading-H18_b7",
            "heading-H20R": "Text_heading-H20R_f6",
            "heading-H22": "Text_heading-H22_27",
            "heading-H24R": "Text_heading-H24R_be",
            "heading-H24": "Text_heading-H24_0c",
            "heading-H28": "Text_heading-H28_78",
            "heading-H36": "Text_heading-H36_32",
            "heading-H56": "Text_heading-H56_c3",
            "heading-H73": "Text_heading-H73_8f",
            "heading-H144": "Text_heading-H144_a9",
            BLACK_REAL: "Text_BLACK_REAL_30",
            WHITE_REAL: "Text_WHITE_REAL_bc",
            WHITE: "Text_WHITE_62",
            WHITE_ORANGE: "Text_WHITE_ORANGE_54",
            WHITE_SPANISH: "Text_WHITE_SPANISH_df",
            PAR: "Text_PAR_15",
            PAR_SECONDARY: "Text_PAR_SECONDARY_5d",
            PAR_TERTIARY: "Text_PAR_TERTIARY_c9",
            INFO_RED: "Text_INFO_RED_30",
            RED: "Text_RED_66",
            RED_DARK: "Text_RED_DARK_d8",
            YELLOW: "Text_YELLOW_ed",
            ORANGE: "Text_ORANGE_be",
            CREAM: "Text_CREAM_57",
            BROWN: "Text_BROWN_18",
            GREEN_BRIGHT: "Text_GREEN_BRIGHT_3f",
            GREEN: "Text_GREEN_e3",
            GREEN_DARK: "Text_GREEN_DARK_f1",
            BLUE_BOOSTER: "Text_BLUE_BOOSTER_21",
            BLUE_TEAMKILLER: "Text_BLUE_TEAMKILLER_ab",
            CRED: "Text_CRED_f7",
            GOLD: "Text_GOLD_28",
            BOND: "Text_BOND_be",
            PROM: "Text_PROM_65",
          },
          Cu = [
            "text",
            "variant",
            "className",
            "color",
            "m",
            "mt",
            "mr",
            "mb",
            "ml",
            "style",
            "format",
          ];
        function pu() {
          return (
            (pu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            pu.apply(this, arguments)
          );
        }
        Object.keys(qe());
        const hu = Object.keys(Bu()),
          fu = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          bu = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          vu = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Su = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          wu =
            (Object.keys(Su),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": fu,
              "heading-H36": fu,
              "heading-H28": bu,
              "heading-H24": bu,
              "heading-H24R": bu,
              "heading-H22": bu,
              "heading-H20R": bu,
              "heading-H18": bu,
              "heading-H15": vu,
              "heading-H14": vu,
              "paragraph-P24": bu,
              "paragraph-P18": bu,
              "paragraph-P16": bu,
              "paragraph-P14": vu,
              "paragraph-P12": vu,
              "paragraph-P10": vu,
            }),
          xu =
            (Object.keys(wu),
            (e) =>
              e
                ? ((e) => hu.includes(e))(e)
                  ? { colorClassName: gu[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Ru = eu((e) => {
            let u = e.text,
              t = e.variant,
              n = e.className,
              r = e.color,
              o = e.m,
              i = e.mt,
              l = void 0 === i ? o : i,
              c = e.mr,
              E = void 0 === c ? o : c,
              d = e.mb,
              m = void 0 === d ? o : d,
              _ = e.ml,
              A = void 0 === _ ? o : _,
              F = e.style,
              D = e.format,
              B = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Cu);
            const g = (0, a.useMemo)(() => {
                const e = xu(r),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, n), colorClassName: u };
              }, [F, r]),
              C = g.computedStyle,
              p = g.colorClassName;
            return s().createElement(
              ou,
              pu(
                {
                  className: h()(gu.base, t && gu[t], p, n),
                  style: C,
                  mt: !0 === l ? wu[t || "paragraph-P16"].mt : l,
                  mr: !0 === E ? wu[t || "paragraph-P16"].mr : E,
                  mb: !0 === m ? wu[t || "paragraph-P16"].mb : m,
                  ml: !0 === A ? wu[t || "paragraph-P16"].ml : A,
                },
                B,
              ),
              void 0 !== D ? s().createElement(Fu, pu({}, D, { text: u })) : u,
            );
          });
        var yu = t(5238);
        const Mu = ["children"];
        function Tu() {
          return (
            (Tu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Tu.apply(this, arguments)
          );
        }
        const Lu = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, Mu);
          return s().createElement(
            yu.u,
            Tu(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              t,
            ),
            u,
          );
        };
        var Pu = t(6373);
        function Nu() {
          return (
            (Nu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Nu.apply(this, arguments)
          );
        }
        const Ou = ({ children: e, tooltipArgs: u, className: t }) => {
            if (!u) return e;
            const n = s().createElement("div", { className: t }, e);
            if (u.header || u.body) return s().createElement(Pu.i, u, n);
            const r = u.contentId,
              a = u.args,
              o = null == a ? void 0 : a.contentId;
            return r || o
              ? s().createElement(yu.u, Nu({}, u, { contentId: r || o }), n)
              : s().createElement(Lu, u, n);
          },
          ku = {
            base: "MainReward_base_94",
            base__withCoins: "MainReward_base__withCoins_ca",
            icon: "MainReward_icon_c8",
            value: "MainReward_value_41",
            base__credits: "MainReward_base__credits_5a",
            base__gold: "MainReward_base__gold_5b",
            base__crystal: "MainReward_base__crystal_32",
            overlay: "MainReward_overlay_c7",
            label: "MainReward_label_5f",
            label__large: "MainReward_label__large_ef",
          },
          Iu = (0, a.memo)(
            ({
              icon: e,
              value: u,
              name: t,
              tooltipId: n,
              tooltipContentId: r,
              hasCoins: a,
              size: o,
              label: i,
              overlayType: l,
            }) => {
              const c = Xe(
                ((e) => ("equipmentModernized" === e ? Re.EQUIPMENT_MODERNIZED_UPGRADED_1 : e))(l),
              );
              return s().createElement(
                Ou,
                { tooltipArgs: Ve({ tooltipId: n, contentId: Number(r) }) },
                s().createElement(
                  "div",
                  { className: h()(ku.base, a && ku.base__withCoins, ku[`base__${t}`]) },
                  c &&
                    a &&
                    s().createElement("div", {
                      className: h()(ku.overlay),
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${o}.${c}_overlay)`,
                      },
                    }),
                  s().createElement("div", {
                    className: ku.icon,
                    style: { backgroundImage: `url('${e}')` },
                  }),
                  u && s().createElement("div", { className: ku.value }, ze(u, Ue(t))),
                  s().createElement(Ru, {
                    className: h()(ku.label, o === we.S600x450 && ku.label__large),
                    text: i,
                  }),
                ),
              );
            },
          );
        var Hu = t(7030);
        const Uu = (e) => Math.sqrt(1 - Math.pow(e - 1, 2)),
          Wu = (0, a.memo)(
            ({ index: e, delay: u = 0, onAnimationEnd: t, className: n, children: r }) => {
              const a = (0, Hu.useSpring)({
                from: { scale: 1.2, opacity: 0, transform: "translateY(20rem)" },
                to: { scale: 1, opacity: 1, transform: "translateY(0)" },
                delay: u + 900 + 200 * e,
                config: { duration: 400, easing: Uu },
                onStart: () => {
                  W(R.sounds.gui_random_reward_appear());
                },
                onRest: () => {
                  null == t || t();
                },
              });
              return s().createElement(Hu.animated.div, { style: a, className: n }, r);
            },
          );
        var Gu = t(5668);
        const $u = {
            base: "AwardCoin_base_a3",
            coin: "AwardCoin_coin_30",
            fadeInWithScale: "AwardCoin_fadeInWithScale_e6",
            count: "AwardCoin_count_2f",
            fadeIn: "AwardCoin_fadeIn_73",
            value: "AwardCoin_value_f6",
            label: "AwardCoin_label_c1",
            fadeOut: "AwardCoin_fadeOut_45",
            raysAppearance: "AwardCoin_raysAppearance_f0",
            rotate: "AwardCoin_rotate_28",
            slideUp: "AwardCoin_slideUp_5d",
            scale: "AwardCoin_scale_5e",
          },
          Vu = R.strings.seniority_awards.rewardsView.sacoin,
          Xu = (0, a.memo)(({ count: e, size: u, onAnimationEnd: t }) => {
            const n = (0, a.useState)(!1),
              r = n[0],
              o = n[1],
              i = u === we.S600x450;
            return (
              (0, a.useEffect)(() => W(R.sounds.gui_hangar_reward_main_icon()), []),
              s().createElement(
                "div",
                { className: $u.base },
                s().createElement(
                  "div",
                  { className: $u.coin, onAnimationEnd: () => o(!0) },
                  s().createElement(Gu.F, null),
                ),
                r &&
                  s().createElement(
                    "div",
                    { className: $u.count, onAnimationEnd: t },
                    s().createElement(Ru, {
                      text: Vu.counter(),
                      className: $u.value,
                      format: { binding: { count: e } },
                    }),
                  ),
                s().createElement(Ru, {
                  className: h()($u.label, i && $u.label__large),
                  text: Vu.label(),
                }),
              )
            );
          }),
          zu = {
            1: {
              [v.ExtraSmall]: [we.S296x222],
              [v.Small]: [we.S400x300],
              [v.Medium]: [we.S400x300],
              [v.Large]: [we.S600x450],
              [v.ExtraLarge]: [we.S600x450],
            },
            2: {
              [v.ExtraSmall]: [we.S296x222, we.S296x222],
              [v.Small]: [we.S296x222, we.S296x222],
              [v.Medium]: [we.S296x222, we.S296x222],
              [v.Large]: [we.S400x300, we.S400x300],
              [v.ExtraLarge]: [we.S400x300, we.S400x300],
            },
            3: {
              [v.ExtraSmall]: [we.S296x222, we.S296x222, we.S296x222],
              [v.Small]: [we.S296x222, we.S400x300, we.S296x222],
              [v.Medium]: [we.S296x222, we.S400x300, we.S296x222],
              [v.Large]: [we.S400x300, we.S600x450, we.S400x300],
              [v.ExtraLarge]: [we.S400x300, we.S600x450, we.S400x300],
            },
          },
          ju = (e, u, t) => {
            var n;
            const r = null != (n = e.icon) && n.match(/^\d/) ? `c_${e.icon}` : e.icon;
            if (e.name === ve.TmanToken)
              switch (t) {
                case we.Mini:
                case we.Small:
                case we.S48x48:
                case we.Big:
                case we.S80x80:
                  return `R.images.gui.maps.icons.tankmen.icons.s80x80.${e.icon}`;
                case we.S128x100:
                case we.S180x135:
                case we.S232x174:
                  return `R.images.gui.maps.icons.tankmen.icons.s232x174.${e.icon}`;
                case we.S296x222:
                  return `R.images.gui.maps.icons.tankmen.icons.s296x222.${e.icon}`;
                case we.S400x300:
                  return `R.images.gui.maps.icons.tankmen.icons.s400x300.${e.icon}`;
                case we.S600x450:
                  return `R.images.gui.maps.icons.tankmen.icons.s600x450.${e.icon}`;
                default:
                  return (
                    console.error("Unknown image size", t),
                    "R.images.gui.maps.icons.tankmen.icons.s600x450.tankman"
                  );
              }
            return $e(Object.assign({}, e, { icon: r }), t);
          },
          Yu = (e) => --e * e * e + 1,
          qu = {
            base: "SeniorityReward_base_e4",
            base__withCoins: "SeniorityReward_base__withCoins_ea",
            icon: "SeniorityReward_icon_2a",
            label: "SeniorityReward_label_da",
            base__credits: "SeniorityReward_base__credits_5b",
            base__gold: "SeniorityReward_base__gold_56",
            base__crystal: "SeniorityReward_base__crystal_ce",
            overlay: "SeniorityReward_overlay_f1",
          },
          Ku = ({
            icon: e,
            value: u,
            name: t,
            tooltipId: n,
            tooltipContentId: r,
            hasCoins: a,
            overlayType: o,
          }) => {
            const i = Xe(
              ((e) => ("equipmentModernized" === e ? Re.EQUIPMENT_MODERNIZED_UPGRADED_1 : e))(o),
            );
            return s().createElement(
              Ou,
              { tooltipArgs: Ve({ tooltipId: n, contentId: Number(r) }) },
              s().createElement(
                "div",
                { className: h()(qu.base, a && qu.base__withCoins, qu[`base__${t}`]) },
                i &&
                  a &&
                  s().createElement("div", {
                    className: h()(qu.overlay),
                    style: {
                      backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.s180x135.${i}_overlay)`,
                    },
                  }),
                s().createElement("div", {
                  className: qu.icon,
                  style: { backgroundImage: `url('${e}')` },
                }),
                u && s().createElement("div", { className: qu.label }, ze(u, Ue(t))),
              ),
            );
          },
          Qu = "AnimatedReward_base_64",
          Zu = "AnimatedReward_base__withCoins_53",
          Ju = (0, a.memo)(
            ({
              delay: e,
              duration: u,
              icon: t,
              value: n,
              name: r,
              tooltipId: a,
              tooltipContentId: o,
              hasCoins: i,
              onRest: l,
              overlayType: c,
            }) => {
              const E = (0, Hu.useSpring)({
                from: { opacity: 0, transform: i ? "translateY(30rem)" : "scale(0.5)" },
                to: { opacity: 1, transform: i ? "translateY(0)" : "scale(1)" },
                delay: e,
                config: { duration: u, easing: Yu },
                onStart: () => W(R.sounds.gui_random_reward_icon()),
                onRest: l,
              });
              return s().createElement(
                Hu.animated.div,
                { style: E, className: h()(Qu, i && Zu) },
                s().createElement(Ku, {
                  overlayType: c,
                  icon: t,
                  value: n,
                  name: r,
                  tooltipId: a,
                  tooltipContentId: o,
                  hasCoins: i,
                }),
              );
            },
          ),
          et = (0, a.createContext)({ rewards: [] }),
          ut = "RewardsAnimatedText_base_c4",
          tt = ({ animatedText: e, duration: u }) => {
            const t = (0, Hu.useSpring)({
              from: { opacity: 0, transform: "translateY(30rem)" },
              to: { opacity: 1, transform: "translateY(0)" },
              config: { duration: u, easing: Yu },
            });
            return s().createElement(Hu.animated.div, { style: t, className: ut }, e);
          },
          nt = "Rewards_base_e7",
          rt = "Rewards_base__withCoins_62",
          at = "Rewards_rewards_c5",
          st = (e, u) => {
            var t;
            const n = null != (t = e.icon) && t.match(/^\d/) ? `c_${e.icon}` : e.icon,
              r = u ? we.Big : we.S400x300;
            return $e(Object.assign({}, e, { icon: n }), r);
          },
          ot = (e) => (null == e ? void 0 : e.overlayType),
          it = (0, J.Pi)(({ onAnimationEnd: e }) => {
            const u = Ce().model.computes.getHasCoins(),
              t = (0, a.useContext)(et).rewards,
              n = R.strings.seniority_awards.rewardsView.subTitle.otherRewards();
            return s().createElement(
              "div",
              { className: h()(nt, u && rt) },
              u && s().createElement(tt, { duration: 150, animatedText: n }),
              s().createElement(
                "div",
                { className: at },
                t &&
                  t.map((n, r) =>
                    s().createElement(Ju, {
                      key: n.index,
                      delay: 150 * (r + 1),
                      duration: 150,
                      name: n.name,
                      icon: st(n, u),
                      value: n.value,
                      tooltipId: n.tooltipId,
                      tooltipContentId: n.tooltipContentId,
                      onRest: r === t.length - 1 ? e : void 0,
                      overlayType: ot(n),
                      hasCoins: u,
                    }),
                  ),
              ),
            );
          }),
          lt = "MainRewards_base_53",
          ct = "MainRewards_awardCoin_5c",
          Et = "MainRewards_glow_31",
          dt = "MainRewards_mainReward_e5",
          mt = (0, J.Pi)(({ onAnimationEnd: e }) => {
            const u = Ce().model,
              t = x().mediaSize,
              n = u.computes.getCoinsCount(),
              r = u.computes.getHasCoins(),
              a = u.computes.getMainBonuses(),
              o = u.computes.getMainBonusesLength(),
              i = (o || r) && a.length <= 3;
            return s().createElement(
              "div",
              { className: lt },
              i &&
                (null == a
                  ? void 0
                  : a.map((u, i) =>
                      "awardCoin" === u.name && r
                        ? s().createElement(
                            "div",
                            { key: u.name, className: h()(ct, dt) },
                            s().createElement("div", { className: Et }),
                            s().createElement(Xu, {
                              count: n,
                              size: zu[null == a ? void 0 : a.length][t][i],
                              onAnimationEnd: o ? void 0 : e,
                            }),
                          )
                        : s().createElement(
                            Wu,
                            {
                              key: u.name,
                              index: i,
                              onAnimationEnd: i === a.length - 1 ? e : void 0,
                              className: dt,
                            },
                            s().createElement(Iu, {
                              overlayType: ot(u),
                              icon: ju(u, 0, zu[null == a ? void 0 : a.length][t][i]),
                              value: u.value,
                              name: u.name,
                              tooltipId: u.tooltipId,
                              tooltipContentId: u.tooltipContentId,
                              size: zu[null == a ? void 0 : a.length][t][i],
                              label: u.label,
                              hasCoins: !1,
                            }),
                          ),
                    )),
            );
          }),
          _t = "Ribbon_base_0f",
          At = "Ribbon_ribbon_33",
          Ft = "Ribbon_base__withMainRewards_c1",
          Dt = "Ribbon_rewards_4b",
          Bt = "Ribbon_radialLines_e5",
          gt = "Ribbon_linesWrapper_ca",
          Ct = (0, a.memo)(({ hasMainRewards: e, onAnimationEnd: u }) => {
            const t = (0, a.useState)(!1),
              n = t[0],
              r = t[1],
              o = (0, a.useState)(!1),
              i = o[0],
              l = o[1],
              c = (0, a.useCallback)(() => {
                l(!0);
              }, []);
            return s().createElement(
              "div",
              {
                className: h()(_t, e && Ft),
                onAnimationEnd: () => {
                  e ? r(!0) : l(!0);
                },
              },
              s().createElement(
                "div",
                { className: At },
                s().createElement(
                  "div",
                  { className: gt },
                  s().createElement("div", { className: Bt }),
                ),
                n && e && s().createElement(mt, { onAnimationEnd: c }),
                s().createElement(
                  "div",
                  { className: Dt },
                  i && s().createElement(it, { onAnimationEnd: u }),
                ),
              ),
            );
          }),
          pt = (e) => {
            let u,
              t = null;
            return (
              (t = requestAnimationFrame(() => {
                t = requestAnimationFrame(() => {
                  ((t = null), (u = e()));
                });
              })),
              () => {
                ("function" == typeof u && u(), null !== t && cancelAnimationFrame(t));
              }
            );
          },
          ht = (e, u, t) => (t < e ? e : t > u ? u : t),
          ft = [];
        function bt(e) {
          const u = (0, a.useRef)(e);
          return (
            (0, a.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, a.useCallback)((...e) => (0, u.current)(...e), ft)
          );
        }
        function vt(e, u, t = []) {
          const n = (0, a.useRef)(0),
            r = (0, a.useCallback)(() => window.clearInterval(n.current), t || []);
          (0, a.useEffect)(() => r, [r]);
          const s = (null != t ? t : []).concat([u]);
          return [
            (0, a.useCallback)((t) => {
              ((n.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, s),
            r,
          ];
        }
        function St(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return wt(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return wt(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function wt(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        function xt(e, u, t) {
          const n = (0, a.useMemo)(
            () =>
              (function (e, u, t, n) {
                let r,
                  a = !1,
                  s = 0;
                function o() {
                  r && clearTimeout(r);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - s;
                  function E() {
                    ((s = Date.now()), t.apply(l, i));
                  }
                  a ||
                    (n && !r && E(),
                    o(),
                    void 0 === n && c > e
                      ? E()
                      : !0 !== u &&
                        (r = setTimeout(
                          n
                            ? function () {
                                r = void 0;
                              }
                            : E,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
                  (i.cancel = function () {
                    (o(), (a = !0));
                  }),
                  i
                );
              })(t, e),
            u,
          );
          return ((0, a.useEffect)(() => n.cancel, [n]), n);
        }
        let Rt;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Rt || (Rt = {}));
        const yt = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          Mt = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: s = !1,
          }) => {
            const o = (e, t) => {
              const n = u(e),
                r = n[0],
                a = n[1];
              return ht(r, a, t);
            };
            return (l = {}) => {
              const c = l.settings,
                E = void 0 === c ? yt : c,
                d = (0, a.useRef)(null),
                m = (0, a.useRef)(null),
                _ = (() => {
                  const e = (0, a.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    n = (e, t) => {
                      u(e).delete(t);
                    },
                    r = (e, ...t) => {
                      for (var n, r = St(u(e).values()); !(n = r()).done;) (0, n.value)(...t);
                    };
                  return (0, a.useMemo)(() => ({ on: t, off: n, trigger: r }), []);
                })(),
                A = xt(
                  () => {
                    i.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                F = (0, Hu.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = d.current;
                    u && (t(u, e), _.trigger("change", e), s && A());
                  },
                  onRest: (e) => _.trigger("rest", e),
                  onStart: (e) => _.trigger("start", e),
                  onPause: (e) => _.trigger("pause", e),
                })),
                D = F[0],
                B = F[1],
                g = (0, a.useCallback)(
                  (e, u, t) => {
                    var n;
                    const r = D.scrollPosition.get(),
                      a = (null != (n = D.scrollPosition.goal) ? n : 0) - r;
                    return o(e, u * t + a + r);
                  },
                  [D.scrollPosition],
                ),
                C = (0, a.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = d.current;
                    n &&
                      B.start({
                        scrollPosition: o(n, e),
                        immediate: u,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: o(n, D.scrollPosition.get()) },
                      });
                  },
                  [B, E.animationConfig, D.scrollPosition],
                ),
                p = (0, a.useCallback)(
                  (e) => {
                    const u = d.current,
                      t = m.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return r(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, E.step),
                      a = g(u, e, n);
                    C(a);
                  },
                  [C, g, E.step],
                ),
                h = (0, a.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && p(n(e)),
                      d.current && _.trigger("mouseWheel", e, D.scrollPosition, u(d.current)));
                  },
                  [D.scrollPosition, p, _],
                ),
                f = ((e, u = []) => {
                  const t = (0, a.useRef)(),
                    n = (0, a.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, a.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    pt(() => {
                      const e = d.current;
                      e &&
                        (C(o(e, D.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [C, D.scrollPosition.goal],
                ),
                b = bt(() => {
                  const e = d.current;
                  if (!e) return;
                  const u = o(e, D.scrollPosition.goal);
                  (u !== D.scrollPosition.goal && C(u, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, a.useEffect)(
                () => (
                  window.addEventListener("resize", f),
                  () => {
                    window.removeEventListener("resize", f);
                  }
                ),
                [f],
              );
              const v = (0, a.useCallback)((e) => _.trigger("isThumbDraggingChanged", e), [_]);
              return (0, a.useMemo)(
                () => ({
                  getWrapperSize: () => (m.current ? r(m.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? u(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: o,
                  handleMouseWheel: h,
                  applyScroll: C,
                  applyStepTo: p,
                  contentRef: d,
                  wrapperRef: m,
                  scrollPosition: B,
                  animationScroll: D,
                  recalculateContent: b,
                  handleIsThumbDragging: v,
                  events: { on: _.on, off: _.off },
                }),
                [D.scrollPosition, C, p, v, _.off, _.on, b, h, B, E.step.clampedArrowStepTimeout],
              );
            };
          },
          Tt = Mt({
            getBounds: (e) => {
              var u, t;
              return [
                0,
                e.offsetWidth -
                  (null != (u = null == (t = e.parentElement) ? void 0 : t.offsetWidth) ? u : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, u) => {
              e.style.transform = `translateX(-${u.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? Rt.Next : Rt.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          Lt = "HorizontalBar_base_49",
          Pt = "HorizontalBar_base__nonActive_82",
          Nt = "HorizontalBar_leftButton_5f",
          Ot = "HorizontalBar_rightButton_03",
          kt = "HorizontalBar_track_0d",
          It = "HorizontalBar_thumb_fd",
          Ht = "HorizontalBar_rail_32",
          Ut = "disable",
          Wt = { pending: !1, offset: 0 },
          Gt = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          $t = () => {},
          Vt = (e, u) => Math.max(20, e.offsetWidth * u),
          Xt = (0, a.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Gt, onDrag: n = $t }) => {
              const r = (0, a.useRef)(null),
                o = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = e.stepTimeout || 100,
                d = (0, a.useState)(Wt),
                m = d[0],
                _ = d[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                F = () => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const a = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    E = ht(0, 1, a / (r - n)),
                    d = (u.offsetWidth - Vt(u, s)) * E;
                  ((t.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(Ut), void i.current.classList.remove(Ut));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (o.current.classList.remove(Ut), void i.current.classList.add(Ut));
                        var u, t;
                        (o.current.classList.remove(Ut), i.current.classList.remove(Ut));
                      }
                    })(d));
                },
                D = bt(() => {
                  ((() => {
                    const u = c.current,
                      t = l.current,
                      n = e.getWrapperSize(),
                      a = e.getContainerSize();
                    if (!(a && u && n && t)) return;
                    const s = Math.min(1, n / a);
                    ((u.style.width = `${Vt(t, s)}px`),
                      (u.style.display = "flex"),
                      r.current &&
                        (1 === s ? r.current.classList.add(Pt) : r.current.classList.remove(Pt)));
                  })(),
                    F());
                });
              ((0, a.useEffect)(() => pt(D)),
                (0, a.useEffect)(
                  () =>
                    pt(() => {
                      const u = () => {
                        F();
                      };
                      let t = $t;
                      const n = () => {
                        (t(), (t = pt(D)));
                      };
                      return (
                        e.events.on("recalculateContent", D),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", n),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", D),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, a.useEffect)(() => {
                  if (!m.pending) return;
                  const u = (u) => {
                      var t;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const a = l.current,
                        s = c.current;
                      if (!r || !a || !s) return;
                      const o = u.screenX - m.offset - a.getBoundingClientRect().x,
                        i = (o / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), A(Wt));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, m.offset, m.pending, n, A]));
              const B = vt((u) => e.applyStepTo(u), E, [e]),
                g = B[0],
                C = B[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", C, !0),
                  () => document.removeEventListener("mouseup", C, !0)
                ),
                [C],
              );
              const p = (e) => {
                e.target.classList.contains(Ut) || W("highlight");
              };
              return s().createElement(
                "div",
                { className: h()(Lt, u.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: h()(Nt, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ut) || 0 !== e.button || (W("play"), g(Rt.Next));
                  },
                  onMouseUp: C,
                  ref: o,
                  onMouseEnter: p,
                }),
                s().createElement(
                  "div",
                  {
                    className: h()(kt, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((W("play"), u.target === n))
                          A({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = c.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const a = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * u);
                          })(u.screenX > n.getBoundingClientRect().x ? Rt.Prev : Rt.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: p,
                  },
                  s().createElement("div", { ref: c, className: h()(It, u.thumb) }),
                  s().createElement("div", { className: h()(Ht, u.rail) }),
                ),
                s().createElement("div", {
                  className: h()(Ot, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ut) || 0 !== e.button || (W("play"), g(Rt.Prev));
                  },
                  onMouseUp: C,
                  ref: i,
                  onMouseEnter: p,
                }),
              );
            },
          ),
          zt = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          jt = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            classNames: o,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: h()(zt.base, e.base) });
              }, [n]),
              d = (0, a.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: h()(zt.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: h()(zt.defaultScrollArea, r) },
                s().createElement(Yt, { className: i, api: d, classNames: o }, e),
              ),
              s().createElement(Xt, { getStepByRailClick: l, api: u, onDrag: c, classNames: E }),
            );
          },
          Yt = ({ api: e, className: u, classNames: t, children: n, style: r }) => (
            (0, a.useEffect)(() => pt(e.recalculateContent)),
            s().createElement(
              "div",
              { className: h()(zt.base, u), style: r },
              s().createElement(
                "div",
                {
                  className: h()(zt.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: h()(zt.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((Yt.Bar = Xt),
          (Yt.Default = jt),
          (Yt.SeniorityAwards = ({ api: e, className: u, classNames: t, children: n }) => (
            (0, a.useEffect)(() => pt(e.recalculateContent)),
            s().createElement(
              "div",
              { className: h()(zt.base, u) },
              s().createElement(
                "div",
                { className: h()(zt.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: h()(zt.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const qt = Mt({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Rt.Next : Rt.Prev),
          }),
          Kt = "VerticalBar_base_f3",
          Qt = "VerticalBar_base__nonActive_42",
          Zt = "VerticalBar_topButton_d7",
          Jt = "VerticalBar_bottomButton_06",
          en = "VerticalBar_track_df",
          un = "VerticalBar_thumb_32",
          tn = "VerticalBar_rail_43",
          nn = "disable",
          rn = () => {},
          an = { pending: !1, offset: 0 },
          sn = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          on = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          ln = (e, u) => Math.max(20, e.offsetHeight * u),
          cn = (0, a.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = sn, onDrag: n = rn }) => {
              const r = (0, a.useRef)(null),
                o = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = e.stepTimeout || 100,
                d = (0, a.useState)(an),
                m = d[0],
                _ = d[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                F = bt(() => {
                  const u = c.current,
                    t = l.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && a && u && t)) return;
                  const s = Math.min(1, n / a);
                  return (
                    (u.style.height = `${ln(t, s)}px`),
                    u.classList.add(un),
                    r.current &&
                      (1 === s ? r.current.classList.add(Qt) : r.current.classList.remove(Qt)),
                    s
                  );
                }),
                D = bt(() => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const a = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    E = ht(0, 1, a / (r - n)),
                    d = (u.offsetHeight - ln(u, s)) * E;
                  ((t.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(nn), void i.current.classList.remove(nn));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (o.current.classList.remove(nn), void i.current.classList.add(nn));
                        var u, t;
                        (o.current.classList.remove(nn), i.current.classList.remove(nn));
                      }
                    })(d));
                }),
                B = bt(() => {
                  on(e, () => {
                    (F(), D());
                  });
                });
              ((0, a.useEffect)(() => pt(B)),
                (0, a.useEffect)(() => {
                  const u = () => {
                    on(e, () => {
                      D();
                    });
                  };
                  let t = rn;
                  const n = () => {
                    (t(), (t = pt(B)));
                  };
                  return (
                    e.events.on("recalculateContent", B),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", n),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", B),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, a.useEffect)(() => {
                  if (!m.pending) return;
                  const u = (u) => {
                      on(e, (t) => {
                        const r = l.current,
                          a = c.current,
                          s = e.getContainerSize();
                        if (!r || !a || !s) return;
                        const o = u.screenY - m.offset - r.getBoundingClientRect().y,
                          i = (o / r.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: a, thumbOffset: o, contentOffset: i }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        A(an));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, m.offset, m.pending, n, A]));
              const g = vt((u) => e.applyStepTo(u), E, [e]),
                C = g[0],
                p = g[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", p, !0),
                  () => document.removeEventListener("mouseup", p, !0)
                ),
                [p],
              );
              const f = (e) => {
                e.target.classList.contains(nn) || W("highlight");
              };
              return s().createElement(
                "div",
                { className: h()(Kt, u.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: h()(Zt, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(nn) || 0 !== e.button || (W("play"), C(Rt.Next));
                  },
                  ref: o,
                  onMouseEnter: f,
                }),
                s().createElement(
                  "div",
                  {
                    className: h()(en, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((W("play"), u.target === n))
                          (e.handleIsThumbDragging(!0),
                            A({ pending: !0, offset: u.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            c.current &&
                              on(e, (n) => {
                                if (!n) return;
                                const r = t(e),
                                  a = e.clampPosition(n, n.scrollTop + r * u);
                                e.applyScroll(a);
                              });
                          })(u.screenY > n.getBoundingClientRect().y ? Rt.Prev : Rt.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: f,
                  },
                  s().createElement("div", { ref: c, className: u.thumb }),
                  s().createElement("div", { className: h()(tn, u.rail) }),
                ),
                s().createElement("div", {
                  className: h()(Jt, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(nn) || 0 !== e.button || (W("play"), C(Rt.Prev));
                  },
                  onMouseUp: p,
                  ref: i,
                  onMouseEnter: f,
                }),
              );
            },
          ),
          En = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          dn = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: o,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: h()(En.base, e.base) });
              }, [n]),
              d = (0, a.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: h()(En.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: h()(En.area, r) },
                s().createElement(mn, { className: o, classNames: i, api: d }, e),
              ),
              s().createElement(cn, { getStepByRailClick: l, api: u, onDrag: c, classNames: E }),
            );
          },
          mn = ({ className: e, classNames: u, children: t, api: n }) => (
            (0, a.useEffect)(() => pt(n.recalculateContent)),
            s().createElement(
              "div",
              { className: h()(En.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              s().createElement(
                "div",
                { className: h()(En.content, null == u ? void 0 : u.content), ref: n.contentRef },
                t,
              ),
            )
          );
        mn.Default = dn;
        const _n = { Vertical: r, Horizontal: n },
          An = { areaWidth: 0, contentWidth: 0, setAreaWidth: () => oe, setContentWidth: () => oe },
          Fn = (0, a.createContext)(An),
          Dn = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          Bn = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        function gn(e) {
          let u = "";
          for (let t = Bn.length - 1; t >= 0; t--) for (; e >= Bn[t];) ((u += Dn[t]), (e -= Bn[t]));
          return u;
        }
        ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE());
        const Cn = "Vehicle_base_62",
          pn = "Vehicle_hoverArea_25",
          hn = "Vehicle_base__big_8c",
          fn = "Vehicle_image_80",
          bn = "Vehicle_vehicleName_a1",
          vn = "Vehicle_nation_88",
          Sn = "Vehicle_type_14",
          wn = ({
            index: e,
            name: u,
            techName: t,
            type: n,
            tier: r,
            isPremium: a,
            nation: o,
            vehicleCD: i,
            onRestAnimation: l,
            isBig: c = !1,
            isEnabledSound: E = !0,
          }) => {
            const d = {
                backgroundImage: `url(R.images.gui.maps.icons.seniorityAwards.rewards.vehicles.${t})`,
              },
              m = { backgroundImage: `url(R.images.gui.maps.icons.flags.c_60x40..${o})` },
              _ = {
                backgroundImage: `url(R.images.gui.maps.icons.vehicleTypes.c_60x54..${n.replace(/-/g, "_")}${a ? "_elite" : ""})`,
              },
              A = { tooltipId: "TOOLTIP_VEHICLE_REWARD", vehicleCD: i },
              F = (0, Hu.useSpring)({
                from: { opacity: 0, transform: "translateX(30rem)" },
                to: { opacity: 1, transform: "translateX(0%)" },
                delay: 1e3 * e,
                config: { duration: 1e3, easing: Yu },
                onStart: () => E && W(R.sounds.wdr_award_tank()),
                onRest: () => {
                  l(e);
                },
              }),
              D = (0, Hu.useSpring)({
                from: { opacity: 0 },
                to: { opacity: 1 },
                delay: 1e3 * e + 500,
                config: { duration: 500, easing: Yu },
              });
            return s().createElement(
              Lu,
              { args: A },
              s().createElement(
                "div",
                { className: h()(Cn, c && hn) },
                s().createElement("div", { className: pn }),
                s().createElement(
                  Hu.animated.div,
                  { style: F },
                  s().createElement("div", { className: fn, style: d }),
                ),
                s().createElement(
                  Hu.animated.div,
                  { style: D, className: bn },
                  s().createElement("div", { className: vn, style: m }),
                  gn(r),
                  s().createElement("div", { className: Sn, style: _ }),
                  u,
                ),
              ),
            );
          },
          xn = "Vehicles_base_1d",
          Rn = "Vehicles_container_d2",
          yn = "Vehicles_scrollWrapper_b0",
          Mn = "Vehicles_scrollContent_a4",
          Tn = "Vehicles_scrollList_ed",
          Ln = "Vehicles_scrollList__disabled_7b",
          Pn = "Vehicles_scrollLeftButton_28",
          Nn = "Vehicles_scrollRightButton_4d",
          On = "Vehicles_scrollTrack_bd",
          kn = "Vehicles_item_16",
          In = "Vehicles_item__offset_ab",
          Hn = "Vehicles_item__big_85",
          Un = "Vehicles_bar_5d",
          Wn = "Vehicles_bar__visible_8b";
        function Gn() {
          return (
            (Gn =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Gn.apply(this, arguments)
          );
        }
        let $n;
        !(function (e) {
          ((e.Active = "active"),
            (e.Pause = "pause"),
            (e.ActiveWithoutScroll = "activeWithoutScroll"),
            (e.End = "end"));
        })($n || ($n = {}));
        const Vn = (0, J.Pi)(
            ({
              isVisible: e,
              isStoppedScrolling: u,
              onScrollChange: t,
              onAnimationEnd: n,
              setMaxScrollPosition: r,
            }) => {
              var o, i;
              const l = Ce().model,
                c = (0, a.useContext)(Fn),
                E = c.setAreaWidth,
                d = c.areaWidth,
                m = c.contentWidth,
                _ = c.setContentWidth,
                A = l.computes.getVehicles(),
                F = 1 === A.length,
                D = Tt(),
                B = (0, a.useRef)([]),
                g = (0, a.useRef)(null),
                C = (null == (o = g.current) ? void 0 : o.offsetWidth) || 0;
              E(C);
              const p = (null == (i = D.contentRef.current) ? void 0 : i.offsetWidth) || 0;
              r(p);
              const f = (0, a.useState)($n.Active),
                b = f[0],
                v = f[1],
                S = b === $n.Active;
              (0, a.useEffect)(() => {
                u && v($n.ActiveWithoutScroll);
              }, [u]);
              const w = e && b === $n.End,
                x = (0, a.useCallback)(() => {
                  const e = D.animationScroll.scrollPosition.get();
                  t(e);
                }, [t, D.animationScroll.scrollPosition]),
                R = (0, a.useCallback)(
                  (e) => {
                    w && D.handleMouseWheel(e);
                  },
                  [D, w],
                ),
                y = (0, a.useCallback)(() => {
                  (p !== m && _(p), C !== d && E(C));
                }, [d, p, m, C, E, _]);
              (0, a.useEffect)(
                () => (
                  D.events.on("change", x),
                  D.events.on("resizeHandled", y),
                  window.addEventListener("resize", x),
                  window.addEventListener("wheel", R),
                  () => {
                    (D.events.off("change", x),
                      D.events.off("resizeHandled", y),
                      window.removeEventListener("resize", x),
                      window.removeEventListener("wheel", R));
                  }
                ),
                [D.events, x, R, y],
              );
              const M = (0, a.useCallback)(
                  (e, u) => {
                    const t = g.current;
                    (t ? Math.round(t.getBoundingClientRect().right) : 0) < e &&
                      (v($n.Pause),
                      D.applyScroll(D.animationScroll.scrollPosition.goal + u),
                      v($n.Active));
                  },
                  [D],
                ),
                T = (0, a.useCallback)(
                  (e) => {
                    if (e + 1 === A.length) v($n.End);
                    else if (S) {
                      const u = B.current[e],
                        t = B.current[e + 1];
                      M(Math.round(t.getBoundingClientRect().right), u.offsetWidth);
                    }
                  },
                  [S, M, A.length],
                );
              return (
                (0, a.useEffect)(() => {
                  w && (null == n || n());
                }, [n, w]),
                s().createElement(
                  "div",
                  { className: xn },
                  s().createElement(
                    "div",
                    { className: Rn, ref: g },
                    s().createElement(
                      "div",
                      { className: h()(Tn, b !== $n.End && Ln) },
                      s().createElement(
                        _n.Horizontal.Area.SeniorityAwards,
                        { classNames: { content: Mn, wrapper: yn }, api: D },
                        s().createElement(
                          Hu.SpringContext,
                          { pause: b === $n.Pause },
                          A.map((e, u) =>
                            s().createElement(
                              "div",
                              {
                                key: e.vehicleCD,
                                ref: (e) => (B.current[u] = e),
                                className: h()(kn, In, F && Hn),
                              },
                              s().createElement(
                                wn,
                                Gn({}, e, {
                                  index: u,
                                  onRestAnimation: T,
                                  isBig: F,
                                  isEnabledSound: S,
                                }),
                              ),
                            ),
                          ),
                        ),
                      ),
                      s().createElement(
                        "div",
                        { className: h()(Un, b === $n.End && Wn) },
                        s().createElement(_n.Horizontal.Bar, {
                          api: D,
                          classNames: { leftButton: Pn, rightButton: Nn, track: On },
                        }),
                      ),
                    ),
                  ),
                )
              );
            },
          ),
          Xn = "Content_base_0b",
          zn = "Content_vehicles_a7",
          jn = "Content_vehicles__single_81",
          Yn = "Content_vehicles__hidden_f1",
          qn = "Content_ribbon_90",
          Kn = "Content_ribbon__hidden_90",
          Qn = (0, a.memo)(
            ({
              machineState: e,
              isFirstEnter: u,
              isStoppedScrolling: t,
              onScrollChange: n,
              onAnimationEnd: r,
              setMaxScrollPosition: o,
              hasVehicles: i,
              hasMainRewards: l,
              isSingleVehicle: c,
            }) => {
              const E = e === fe.Vehicles && !u,
                d = e === fe.Ribbon && !u,
                m = h()(zn, c && jn, e !== fe.Vehicles && Yn),
                _ = h()(qn, E && Kn);
              return (
                (0, a.useEffect)(() => {
                  d && r();
                }, [d, r]),
                s().createElement(
                  "div",
                  { className: Xn },
                  i &&
                    s().createElement(
                      "div",
                      { className: m },
                      s().createElement(Vn, {
                        isVisible: e === fe.Vehicles,
                        isStoppedScrolling: t,
                        onScrollChange: n,
                        onAnimationEnd: r,
                        setMaxScrollPosition: o,
                      }),
                    ),
                  (e === fe.Ribbon || !u) &&
                    s().createElement(
                      "div",
                      { className: _ },
                      s().createElement(Ct, { hasMainRewards: l, onAnimationEnd: r }),
                    ),
                )
              );
            },
          ),
          Zn = {
            base: "CButton_base_40",
            base__main: "CButton_base__main_42",
            base__primary: "CButton_base__primary_7f",
            base__primaryGreen: "CButton_base__primaryGreen_6f",
            base__primaryRed: "CButton_base__primaryRed_ec",
            base__secondary: "CButton_base__secondary_50",
            base__ghost: "CButton_base__ghost_ed",
            base__extraSmall: "CButton_base__extraSmall_27",
            base__small: "CButton_base__small_df",
            base__medium: "CButton_base__medium_74",
            base__disabled: "CButton_base__disabled_d9",
            back: "CButton_back_e5",
            texture: "CButton_texture_fe",
            state: "CButton_state_11",
            base__focus: "CButton_base__focus_83",
            stateHighlightHover: "CButton_stateHighlightHover_ff",
            stateHighlightActive: "CButton_stateHighlightActive_35",
            stateDisabled: "CButton_stateDisabled_54",
            base__firstHover: "CButton_base__firstHover_d5",
            base__highlightActive: "CButton_base__highlightActive_b2",
            content: "CButton_content_cc",
          };
        let Jn, er;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(Jn || (Jn = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(er || (er = {})));
        const ur = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: r,
          mixClass: o,
          soundHover: i,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: E,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: _,
          onClick: A,
        }) => {
          const F = (0, a.useRef)(null),
            D = (0, a.useState)(t),
            B = D[0],
            g = D[1],
            C = (0, a.useState)(!1),
            p = C[0],
            f = C[1],
            b = (0, a.useState)(!1),
            v = b[0],
            S = b[1],
            w = (0, a.useCallback)(() => {
              r || (F.current && (F.current.focus(), g(!0)));
            }, [r]),
            x = (0, a.useCallback)(
              (e) => {
                B && null !== F.current && !F.current.contains(e.target) && g(!1);
              },
              [B],
            ),
            y = (0, a.useCallback)(
              (e) => {
                r || (A && A(e));
              },
              [r, A],
            ),
            M = (0, a.useCallback)(
              (e) => {
                r || (null !== i && W(i), c && c(e), S(!0));
              },
              [r, i, c],
            ),
            T = (0, a.useCallback)(
              (e) => {
                E && E(e);
              },
              [E],
            ),
            L = (0, a.useCallback)(
              (e) => {
                r || (m && m(e), f(!1));
              },
              [r, m],
            ),
            P = (0, a.useCallback)(
              (e) => {
                r || (null !== l && W(l), d && d(e), t && w(), f(!0));
              },
              [r, l, d, w, t],
            ),
            N = (0, a.useCallback)(
              (e) => {
                r || (_ && _(e), f(!1));
              },
              [r, _],
            ),
            O = h()(
              Zn.base,
              Zn[`base__${n}`],
              {
                [Zn.base__disabled]: r,
                [Zn[`base__${u}`]]: u,
                [Zn.base__focus]: B,
                [Zn.base__highlightActive]: p,
                [Zn.base__firstHover]: v,
              },
              o,
            ),
            k = h()(Zn.state, Zn.state__default);
          return (
            (0, a.useEffect)(
              () => (
                document.addEventListener("mousedown", x),
                () => {
                  document.removeEventListener("mousedown", x);
                }
              ),
              [x],
            ),
            (0, a.useEffect)(() => {
              g(t);
            }, [t]),
            s().createElement(
              "div",
              {
                ref: F,
                className: O,
                onMouseEnter: M,
                onMouseMove: T,
                onMouseUp: L,
                onMouseDown: P,
                onMouseLeave: N,
                onClick: y,
              },
              n !== Jn.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: Zn.back }),
                  s().createElement("span", { className: Zn.texture }),
                ),
              s().createElement(
                "span",
                { className: k },
                s().createElement("span", { className: Zn.stateDisabled }),
                s().createElement("span", { className: Zn.stateHighlightHover }),
                s().createElement("span", { className: Zn.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: Zn.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        ur.defaultProps = {
          type: Jn.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const tr = (0, a.memo)(ur),
          nr = "Footer_base_0b",
          rr = "Footer_description_ac",
          ar = "Footer_buttonHolder_0e",
          sr = "Footer_button_d2",
          or = "Footer_buttonText_0b",
          ir = R.strings.seniority_awards.rewardsView,
          lr = "yes1",
          cr = (0, J.Pi)(({ hasMoreRewards: e, onShowMoreClick: u, onAcceptClick: t }) => {
            const n = Ce().model.computes.getIsShopAvailable(),
              r = n ? ir.gotoRewardsBtn() : ir.applyBtn();
            return s().createElement(
              "div",
              { className: nr },
              e
                ? s().createElement(
                    "div",
                    { className: ar },
                    s().createElement(
                      tr,
                      { size: er.medium, onClick: u, soundClick: lr, mixClass: sr },
                      s().createElement("div", { className: or }, ir.moreRewardsBtn()),
                    ),
                  )
                : s().createElement(
                    s().Fragment,
                    null,
                    n && s().createElement("div", { className: rr }, ir.exchangeCoins()),
                    s().createElement(
                      "div",
                      { className: ar },
                      s().createElement(
                        tr,
                        {
                          size: er.medium,
                          type: n ? Jn.primaryGreen : Jn.primary,
                          onClick: t,
                          soundClick: lr,
                          mixClass: sr,
                          isFocused: !0,
                        },
                        s().createElement("div", { className: or }, r),
                      ),
                    ),
                  ),
            );
          }),
          Er = "FormatGradientText_gradientBox_86",
          dr = "FormatGradientText_gradientText_a6",
          mr = "FormatGradientText_gradientText__copied_52",
          _r = (e, u) =>
            e.replace(/%\((.*?)\)s/g, (e, t) => {
              if (u && t in u) {
                return String(u[t]);
              }
              return "";
            }),
          Ar = (0, a.memo)(({ text: e, binding: u, className: t, classNames: n }) => {
            const r = ((e, u, t) => {
                const n =
                    /(?:%\(|{)\w*(?:_[Gg]radient|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Gg]radient|End)(?:\)s|})?/g,
                  r = /(?<=(?:_[Gg]radient|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
                  a = u ? Object.assign({}, u) : {};
                let o = e,
                  i = n.exec(e);
                for (; i;) {
                  const l = i[0],
                    c = r.exec(l),
                    E = i[1],
                    d = _r(E, u);
                  if (c) {
                    const e = c[0].replaceAll(")", "");
                    ((o = o.replace(l, `%(${e})`)),
                      (a[e] = s().createElement(
                        "div",
                        { className: Er },
                        s().createElement(
                          "div",
                          { className: h()(dr, null == t ? void 0 : t.text) },
                          d,
                        ),
                        s().createElement(
                          "div",
                          { className: h()(dr, mr, null == t ? void 0 : t.copiedText) },
                          d,
                        ),
                      )));
                  }
                  i = n.exec(e);
                }
                return [o, a];
              })(e, u, n),
              a = r[0],
              o = r[1];
            return s().createElement(Ru, { text: a, className: t, format: { binding: o } });
          }),
          Fr = "Header_base_eb",
          Dr = "Header_titleBox_72",
          Br = "Header_light_f6",
          gr = "Header_line_25",
          Cr = "Header_line__inverted_ab",
          pr = "Header_title_4c",
          hr = "Header_gradientText_37",
          fr = "Header_gradientText__copied_d8",
          br = "Header_subTitleBox_01",
          vr = "Header_subTitle_e7",
          Sr = R.strings.seniority_awards.rewardsView,
          wr = (0, J.Pi)(() => {
            const e = Ce().model,
              u = e.root.get().category,
              t = e.computes.getPlayingYearsFromCategory(),
              n = e.computes.hasTestersCategory() ? Sr.subTitle.$dyn(u) : Sr.$plural("subTitle", t);
            return s().createElement(
              "div",
              { className: Fr },
              s().createElement(
                "div",
                { className: Dr },
                s().createElement("div", { className: Br }),
                s().createElement("div", { className: gr }),
                s().createElement(
                  "div",
                  { className: pr },
                  s().createElement(Ru, { text: Sr.title(), className: hr }),
                  s().createElement(Ru, { text: Sr.title(), className: h()(hr, fr) }),
                ),
                s().createElement("div", { className: h()(gr, Cr) }),
              ),
              s().createElement(
                "div",
                { className: br },
                s().createElement(Ar, { className: vr, text: n, binding: { years: t } }),
              ),
            );
          }),
          xr = {
            base: "App_base_0f",
            bgWrapper: "App_bgWrapper_99",
            bgWrapper__side: "App_bgWrapper__side_c0",
            bgWrapper__sideRibbon: "App_bgWrapper__sideRibbon_44",
            background: "App_background_1f",
            foreground: "App_foreground_dd",
            bg_smoke: "App_bg_smoke_19",
            bg_side: "App_bg_side_4b",
            bg_side__left: "App_bg_side__left_5e",
            bg_side__right: "App_bg_side__right_e5",
            vignette: "App_vignette_db",
            shadow: "App_shadow_03",
            base__ribbon: "App_base__ribbon_86",
            blackout: "App_blackout_57",
            gradient: "App_gradient_00",
            textButton: "App_textButton_51",
            fadeIn: "App_fadeIn_c0",
            textButton__back: "App_textButton__back_92",
            textButton__close: "App_textButton__close_26",
            goto: "App_goto_32",
            header: "App_header_de",
            slideUp: "App_slideUp_a5",
            footer: "App_footer_72",
            fadeOut: "App_fadeOut_a4",
            raysAppearance: "App_raysAppearance_fe",
            rotate: "App_rotate_66",
            fadeInWithScale: "App_fadeInWithScale_c6",
            scale: "App_scale_47",
          },
          Rr = R.strings.seniority_awards.rewardsView;
        let yr;
        !(function (e) {
          ((e.ShowHeader = "showHeader"),
            (e.ShowContent = "showContent"),
            (e.ShowFooter = "showFooter"),
            (e.Finished = "finished"));
        })(yr || (yr = {}));
        const Mr = (0, J.Pi)(() => {
          const e = Ce(),
            u = e.model,
            t = e.controls,
            n = u.computes,
            r = x().mediaSize,
            o = ((e) => {
              const u = re(e, te),
                t = (0, a.useCallback)(
                  (e) => {
                    u(e.action, e.logLevel, ne(e));
                  },
                  [u],
                );
              return (e) => t(e);
            })("seniority_awards_22"),
            l = (0, a.useState)(0),
            c = l[0],
            E = l[1],
            d = (0, a.useState)(yr.ShowHeader),
            m = d[0],
            _ = d[1],
            A = (0, a.useState)(!1),
            F = A[0],
            D = A[1],
            B = (0, a.useState)(!1),
            g = B[0],
            C = B[1],
            p = (0, a.useState)(0),
            f = p[0],
            b = p[1],
            S = (0, a.useState)(0),
            w = S[0],
            y = S[1],
            M = (0, a.useState)(0),
            T = M[0],
            L = M[1],
            P = n.getHasVehicles(),
            N = 1 === u.computes.getVehicles().length,
            O = u.computes.hasMainRewards(),
            k = n.getBonuses(),
            I = O,
            H = (0, a.useMemo)(
              () =>
                ((e, u, t) => {
                  const n = t ? 10 : 5;
                  return (0, pe.C)({
                    id: "seniority-awards",
                    initial: e,
                    context: {
                      visibleRewards: u.slice(0, n),
                      rewardWatchedCount: n,
                      isFirstEnter: !0,
                    },
                    states: {
                      [fe.Vehicles]: { on: { [be.ShowMoreRewards]: { target: fe.Ribbon } } },
                      [fe.Ribbon]: {
                        exit: (0, he.f0)((e) => ({
                          visibleRewards: e.visibleRewards,
                          rewardWatchedCount: e.rewardWatchedCount,
                          isFirstEnter: !1,
                        })),
                        on: {
                          [be.ToVehicles]: {
                            target: fe.Vehicles,
                            actions: (0, he.f0)((e) => ({
                              visibleRewards: u.slice(0, n),
                              rewardWatchedCount: n,
                              isRibbonVisited: e.isFirstEnter,
                            })),
                          },
                          [be.ShowMoreRewards]: {
                            target: fe.Ribbon,
                            internal: !0,
                            actions: (0, he.f0)((e) => {
                              const t = e.rewardWatchedCount + n;
                              return {
                                visibleRewards: u.slice(e.rewardWatchedCount, t),
                                rewardWatchedCount: t,
                                isRibbonVisited: e.isFirstEnter,
                              };
                            }),
                            cond: (e) => e.rewardWatchedCount < u.length,
                          },
                        },
                      },
                    },
                  });
                })(P ? fe.Vehicles : fe.Ribbon, k, I),
              [k, P, I],
            ),
            G = (0, U.eO)(H),
            $ = G[0],
            V = G[1],
            Y = n.getBonusesLength(),
            q = r === v.ExtraLarge ? 5 : 4,
            Q = n.getVehicles().length > q,
            J = $.value === fe.Vehicles || $.context.rewardWatchedCount < Y,
            ee = (0, a.useMemo)(
              () => ({ rewards: $.context.visibleRewards }),
              [$.context.visibleRewards],
            ),
            oe = (0, a.useCallback)(
              (e = !1) => {
                (o({
                  action: e ? ue.KeyDown : ue.Click,
                  item: se.CloseButton,
                  parentScreen: ae.RewardsScreen,
                }),
                  i.O.view.sendEvent.close(),
                  W(R.sounds.wdr_award_2025_stop()));
              },
              [o],
            ),
            ie = (0, a.useCallback)(() => {
              (_(yr.ShowContent), V(be.ShowMoreRewards));
            }, [V]),
            le = (0, a.useCallback)(() => {
              (m !== yr.Finished && (C(!0), $.value === fe.Ribbon)) || ie();
            }, [m, ie, $.value]),
            ce = (0, a.useCallback)(
              (e = !1) => {
                (o({
                  action: e ? ue.KeyDown : ue.Click,
                  item: n.getIsShopAvailable() ? se.GoToShopButton : se.ConfirmButton,
                  parentScreen: ae.RewardsScreen,
                }),
                  W(R.sounds.wdr_award_2025_stop()),
                  t.onOpenBtnClick());
              },
              [t, n, o],
            );
          !(function ({
            key: e = j.n.ESCAPE,
            callback: u = () => i.O.view.sendEvent.close(),
            preventPropagation: t = !0,
          } = {}) {
            K(e, u, t);
          })({
            callback: (0, a.useCallback)(() => {
              J ? le() : oe(true);
            }, [J, le, oe]),
          });
          const Ee = (0, a.useCallback)(() => {
            J ? le() : ce(true);
          }, [J, le, ce]);
          Z({ [j.n.ENTER]: Ee, [j.n.SPACE]: Ee });
          return (
            (0, a.useEffect)(() => {
              W(R.sounds.wdr_award_2025_start());
            }, []),
            (0, a.useEffect)(() => {
              switch (m) {
                case yr.ShowHeader:
                  return z(() => _(yr.ShowContent), 1e3);
                case yr.ShowFooter:
                  return z(() => _(yr.Finished), 800);
                default:
                  return;
              }
            }, [m]),
            s().createElement(
              "div",
              { className: h()(xr.base, xr[`base__${$.value}`]) },
              s().createElement(
                "div",
                { className: xr.bgWrapper },
                s().createElement("div", {
                  className: xr.background,
                  style: { transform: `translateX(-${i.O.view.pxToRem(c / 1.5)}rem)` },
                }),
                s().createElement("div", {
                  className: xr.foreground,
                  style: { transform: `translateX(-${i.O.view.pxToRem(c)}rem)` },
                }),
                s().createElement("div", {
                  className: xr.bg_smoke,
                  style: { transform: `translateX(-${i.O.view.pxToRem(c / 1.1)}rem)` },
                }),
              ),
              s().createElement(
                "div",
                {
                  className: h()(xr.bgWrapper, xr.bgWrapper__side, {
                    [xr.bgWrapper__sideRibbon]: $.value === fe.Ribbon,
                  }),
                },
                s().createElement("div", {
                  className: h()(xr.bg_side, xr.bg_side__left),
                  style: { transform: `translateX(-${i.O.view.pxToRem(c)}rem)` },
                }),
                Q &&
                  0 !== T &&
                  s().createElement("div", {
                    className: h()(xr.bg_side, xr.bg_side__right),
                    style: { transform: `translateX(${i.O.view.pxToRem(T - f - c)}rem)` },
                  }),
                !Q && s().createElement("div", { className: h()(xr.bg_side, xr.bg_side__right) }),
                s().createElement("div", { className: xr.vignette }),
              ),
              s().createElement("div", { className: xr.shadow }),
              s().createElement("div", { className: xr.blackout }),
              s().createElement("div", { className: xr.gradient }),
              F &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement(
                    "div",
                    { className: h()(xr.textButton, xr.textButton__close) },
                    s().createElement(X, {
                      caption: Rr.textButton.close(),
                      type: "close",
                      side: "right",
                      onClick: () => oe(),
                    }),
                  ),
                  P &&
                    s().createElement(
                      "div",
                      { className: h()(xr.textButton, xr.textButton__back) },
                      s().createElement(X, {
                        caption: Rr.textButton.back(),
                        goto: Rr.textButton.goto(),
                        type: "back",
                        side: "left",
                        onClick: () => V(be.ToVehicles),
                        classNames: { goto: xr.goto },
                      }),
                    ),
                ),
              s().createElement("div", { className: xr.header }, s().createElement(wr, null)),
              m !== yr.ShowHeader &&
                s().createElement(
                  et.Provider,
                  { value: ee },
                  s().createElement(
                    Fn.Provider,
                    {
                      value: { areaWidth: f, setAreaWidth: b, contentWidth: w, setContentWidth: y },
                    },
                    s().createElement(Qn, {
                      machineState: $.value,
                      isFirstEnter: $.context.isFirstEnter,
                      isStoppedScrolling: g,
                      onScrollChange: (e) => E(e),
                      onAnimationEnd: () => {
                        (_(yr.Finished), D($.value === fe.Ribbon));
                      },
                      setMaxScrollPosition: (e) => L(e),
                      hasVehicles: P,
                      hasMainRewards: O,
                      isSingleVehicle: N,
                    }),
                  ),
                ),
              (m === yr.ShowFooter || m === yr.Finished) &&
                s().createElement(
                  "div",
                  { className: xr.footer },
                  s().createElement(cr, {
                    hasMoreRewards: J,
                    onShowMoreClick: ie,
                    onAcceptClick: ce,
                  }),
                ),
            )
          );
        });
        engine.whenReady.then(() => {
          H().render(
            s().createElement(k, null, s().createElement(ge, null, s().createElement(Mr, null))),
            document.getElementById("root"),
          );
        });
      },
      5668: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => i });
        var n = t(6373),
          r = t(6179),
          a = t.n(r);
        const s = "SeniorityAwardCoin_base_f6",
          o = R.strings.tooltips.awardItem.sacoin,
          i = (0, r.memo)(({ isTooltipEnabled: e = !0 }) =>
            a().createElement(
              n.i,
              { header: o.header(), body: o.body(), isEnabled: e },
              a().createElement("div", { className: s }),
            ),
          );
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(e) {
    var u = __webpack_module_cache__[e];
    if (void 0 !== u) return u.exports;
    var t = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](t, t.exports, __webpack_require__), t.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, u, t, n) => {
      if (!u) {
        var r = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [u, t, n] = deferred[i], a = !0, s = 0; s < u.length; s++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(i--, 1);
            var o = t();
            void 0 !== o && (e = o);
          }
        }
        return e;
      }
      n = n || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > n; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [u, t, n];
    }),
    (__webpack_require__.n = (e) => {
      var u = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(u, { a: u }), u);
    }),
    (__webpack_require__.d = (e, u) => {
      for (var t in u)
        __webpack_require__.o(u, t) &&
          !__webpack_require__.o(e, t) &&
          Object.defineProperty(e, t, { enumerable: !0, get: u[t] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (e, u) => Object.prototype.hasOwnProperty.call(e, u)),
    (__webpack_require__.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 300),
    (() => {
      var e = { 300: 0, 589: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            r,
            [a, s, o] = t,
            i = 0;
          if (a.some((u) => 0 !== e[u])) {
            for (n in s) __webpack_require__.o(s, n) && (__webpack_require__.m[n] = s[n]);
            if (o) var l = o(__webpack_require__);
          }
          for (u && u(t); i < a.length; i++)
            ((r = a[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [851], () => __webpack_require__(307));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
