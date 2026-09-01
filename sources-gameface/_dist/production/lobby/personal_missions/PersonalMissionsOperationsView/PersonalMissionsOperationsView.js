(() => {
  var __webpack_modules__ = {
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
      532: (e) => {
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
      887: (e) => {
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
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => o, onResize: () => r }));
        var a = t(472),
          n = t(176);
        const r = (0, a.E)("clientResized"),
          i = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const o = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, n.R)(!1);
          }
          function t() {
            e.enabled && (0, n.R)(!0);
          }
          function a() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : (0, n.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let n = !0;
                  const r = `mouse${u}`,
                    o = i[u]((e) => t([e, "outside"]));
                  function s(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, s),
                    a(),
                    () => {
                      n &&
                        (o(), window.removeEventListener(r, s), (e.listeners -= 1), a(), (n = !1));
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
              ((e.enabled = !1), a());
            },
            enable() {
              ((e.enabled = !0), a());
            },
            enableOutside() {
              e.enabled && (0, n.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, n.R)(!1);
            },
          });
        })();
      },
      959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => a,
            getMouseGlobalPosition: () => r,
            getSize: () => n,
            graphicsQuality: () => i,
          }));
        var a = t(527);
        function n(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const i = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      176: (e, u, t) => {
        "use strict";
        function a(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => a });
      },
      472: (e, u, t) => {
        "use strict";
        function a(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        t.d(u, { E: () => a });
      },
      138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => n });
        var a = t(959);
        const n = { view: t(641), client: a };
      },
      722: (e, u, t) => {
        "use strict";
        function a(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function n(e, u, t) {
          return `url(${a(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => n, getTextureUrl: () => a }));
      },
      112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => n });
        var a = t(472);
        const n = {
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
      641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => E,
            addPreloadTexture: () => o,
            children: () => a,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => x,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => _,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => F,
            getSize: () => m,
            getViewGlobalPosition: () => d,
            isClientAccessible: () => g,
            isEventHandled: () => b,
            isFocused: () => C,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => A,
            sendEvent: () => i.qP,
            setAnimateWindow: () => p,
            setEventHandled: () => h,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => c,
            whenTutorialReady: () => S,
          }));
        var a = t(722),
          n = t(112),
          r = t(538),
          i = t(566);
        function o(e) {
          viewEnv.addPreloadTexture(e);
        }
        function s(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, a);
        }
        function E(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function c(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function A(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function d(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: B(u.x), y: B(u.y) };
        }
        function _() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function B(e) {
          return viewEnv.remToPx(e);
        }
        function p(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function g() {
          return viewEnv.isClientAccessible();
        }
        function h() {
          return viewEnv.setEventHandled();
        }
        function b() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === n.W[u]), e),
            {},
          ),
          x = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          S = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => l });
        const a = ["args"];
        const n = 2,
          r = 16,
          i = 32,
          o = 64,
          s = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                i = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, a);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, i, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, i));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          l = {
            close(e) {
              s("popover" === e ? n : i);
            },
            minimize() {
              s(o);
            },
            move(e) {
              s(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, u, t) => {
        "use strict";
        let a, n;
        (t.d(u, { n: () => a }),
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
          })(n || (n = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var a = t(138);
        class n {
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
            return (window.__dataTracker || (window.__dataTracker = new n()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = a.O.view.addModelObserver(e, t, n);
            return (
              r > 0
                ? ((this._callbacks[r] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(r) : (this._views[t] = [r])))
                : console.error("Can't add callback for model:", e),
              r
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
              const a = this._callbacks[t];
              void 0 !== a && a(e, u);
            });
          }
        }
        n.__instance = void 0;
        const r = n;
      },
      572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(364);
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
      364: (e, u, t) => {
        "use strict";
        t.d(u, { Sw: () => r.Z, B0: () => s, ry: () => B });
        class a {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let a = e.target;
                  do {
                    if (a === u) return;
                    a = a.parentNode;
                  } while (a);
                  t();
                });
              }));
          }
          static get instance() {
            return (a.__instance || (a.__instance = new a()), a.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              a = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== a,
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
        const n = a;
        var r = t(358);
        const i = {
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
        let s;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(s || (s = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          E = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          c = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var A = t(521),
          d = t(138);
        const _ = ["args"];
        function F(e, u, t, a, n, r, i) {
          try {
            var o = e[r](i),
              s = o.value;
          } catch (e) {
            return void t(e);
          }
          o.done ? u(s) : Promise.resolve(s).then(a, n);
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
                  return new Promise(function (a, n) {
                    var r = e.apply(u, t);
                    function i(e) {
                      F(r, a, n, i, o, "next", e);
                    }
                    function o(e) {
                      F(r, a, n, i, o, "throw", e);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          p = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, _);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((a = n),
                        Object.entries(a).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var a;
          },
          C = () => p(s.CLOSE),
          g = (e, u) => {
            e.keyCode === A.n.ESCAPE && u();
          };
        var h = t(572);
        const b = n.instance,
          v = {
            DataTracker: r.Z,
            ViewModel: h.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: E,
            TimeFormatType: c,
            DateFormatType: m,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => p(s.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => p(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              p(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, a, n = R.invalid("resId"), r) => {
              const i = d.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                l = o.x,
                E = o.y,
                c = o.width,
                m = o.height,
                A = {
                  x: d.O.view.pxToRem(l) + i.x,
                  y: d.O.view.pxToRem(E) + i.y,
                  width: d.O.view.pxToRem(c),
                  height: d.O.view.pxToRem(m),
                };
              p(s.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: n,
                direction: u,
                bbox: D(A),
                on: !0,
                args: r,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => g(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              g(e, C);
            },
            handleViewEvent: p,
            onBindingsReady: B,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const a in u)
                if (Object.prototype.hasOwnProperty.call(u, a)) {
                  const n = Object.prototype.toString.call(u[a]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = u[a];
                    t[a] = [];
                    for (let u = 0; u < n.length; u++) t[a].push({ value: e(n[u].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[a] = e(u[a]))
                      : (t[a] = u[a]);
                }
              return t;
            },
            ClickOutsideManager: b,
            SystemLocale: i,
            UserLocale: o,
          };
        window.ViewEnvHelper = v;
      },
      937: (e, u, t) => {
        "use strict";
        var a = t(179),
          n = t.n(a);
        const r = (e, u, t) =>
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
        var i = t(138);
        const o = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var s;
        function l(e, u, t) {
          const a = (function (e, u) {
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
            n = (function (e, u) {
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
            r = Math.min(a, n);
          return {
            extraLarge: r === t.extraLarge.weight,
            large: r === t.large.weight,
            medium: r === t.medium.weight,
            small: r === t.small.weight,
            extraSmall: r === t.extraSmall.weight,
            extraLargeWidth: a === t.extraLarge.weight,
            largeWidth: a === t.large.weight,
            mediumWidth: a === t.medium.weight,
            smallWidth: a === t.small.weight,
            extraSmallWidth: a === t.extraSmall.weight,
            extraLargeHeight: n === t.extraLarge.weight,
            largeHeight: n === t.large.weight,
            mediumHeight: n === t.medium.weight,
            smallHeight: n === t.small.weight,
            extraSmallHeight: n === t.extraSmall.weight,
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
        })(s || (s = {}));
        const E = i.O.client.getSize("rem"),
          c = E.width,
          m = E.height,
          A = Object.assign({ width: c, height: m }, l(c, m, o)),
          d = (0, a.createContext)(A),
          _ = ["children"];
        const F = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, _);
          const n = (0, a.useContext)(d),
            i = n.extraLarge,
            o = n.large,
            s = n.medium,
            l = n.small,
            E = n.extraSmall,
            c = n.extraLargeWidth,
            m = n.largeWidth,
            A = n.mediumWidth,
            F = n.smallWidth,
            D = n.extraSmallWidth,
            B = n.extraLargeHeight,
            p = n.largeHeight,
            C = n.mediumHeight,
            g = n.smallHeight,
            h = n.extraSmallHeight,
            b = { extraLarge: B, large: p, medium: C, small: g, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && i) return u;
            if (t.large && o) return u;
            if (t.medium && s) return u;
            if (t.small && l) return u;
            if (t.extraSmall && E) return u;
          } else {
            if (t.extraLargeWidth && c) return r(u, t, b);
            if (t.largeWidth && m) return r(u, t, b);
            if (t.mediumWidth && A) return r(u, t, b);
            if (t.smallWidth && F) return r(u, t, b);
            if (t.extraSmallWidth && D) return r(u, t, b);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return u;
              if (t.largeHeight && p) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && g) return u;
              if (t.extraSmallHeight && h) return u;
            }
          }
          return null;
        };
        F.defaultProps = {
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
        (0, a.memo)(F);
        const D = (e) => {
            const u = (0, a.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          B = (0, a.memo)(({ children: e }) => {
            const u = (0, a.useContext)(d),
              t = (0, a.useState)(u),
              r = t[0],
              s = t[1],
              E = (0, a.useCallback)((e, u) => {
                const t = i.O.view.pxToRem(e),
                  a = i.O.view.pxToRem(u);
                s(Object.assign({ width: t, height: a }, l(t, a, o)));
              }, []);
            (D(() => {
              engine.on("clientResized", E);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", E), [E]));
            const c = (0, a.useMemo)(() => Object.assign({}, r), [r]);
            return n().createElement(d.Provider, { value: c }, e);
          });
        var p = t(483),
          C = t.n(p),
          g = t(926),
          h = t.n(g);
        let b, v, f;
        (!(function (e) {
          ((e[(e.ExtraSmall = o.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = o.small.width)] = "Small"),
            (e[(e.Medium = o.medium.width)] = "Medium"),
            (e[(e.Large = o.large.width)] = "Large"),
            (e[(e.ExtraLarge = o.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
          (function (e) {
            ((e[(e.ExtraSmall = o.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = o.small.width)] = "Small"),
              (e[(e.Medium = o.medium.width)] = "Medium"),
              (e[(e.Large = o.large.width)] = "Large"),
              (e[(e.ExtraLarge = o.extraLarge.width)] = "ExtraLarge"));
          })(v || (v = {})),
          (function (e) {
            ((e[(e.ExtraSmall = o.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = o.small.height)] = "Small"),
              (e[(e.Medium = o.medium.height)] = "Medium"),
              (e[(e.Large = o.large.height)] = "Large"),
              (e[(e.ExtraLarge = o.extraLarge.height)] = "ExtraLarge"));
          })(f || (f = {})));
        const w = () => {
            const e = (0, a.useContext)(d),
              u = e.width,
              t = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return b.ExtraLarge;
                  case e.large:
                    return b.Large;
                  case e.medium:
                    return b.Medium;
                  case e.small:
                    return b.Small;
                  case e.extraSmall:
                    return b.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), b.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return v.ExtraLarge;
                  case e.largeWidth:
                    return v.Large;
                  case e.mediumWidth:
                    return v.Medium;
                  case e.smallWidth:
                    return v.Small;
                  case e.extraSmallWidth:
                    return v.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), v.ExtraSmall);
                }
              })(e),
              i = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return f.ExtraLarge;
                  case e.largeHeight:
                    return f.Large;
                  case e.mediumHeight:
                    return f.Medium;
                  case e.smallHeight:
                    return f.Small;
                  case e.extraSmallHeight:
                    return f.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), f.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: n,
              mediaWidth: r,
              mediaHeight: i,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          x = ["children", "className"];
        function S() {
          return (
            (S =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            S.apply(this, arguments)
          );
        }
        const O = {
            [v.ExtraSmall]: "",
            [v.Small]: h().SMALL_WIDTH,
            [v.Medium]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH}`,
            [v.Large]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH}`,
            [v.ExtraLarge]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH} ${h().EXTRA_LARGE_WIDTH}`,
          },
          y = {
            [f.ExtraSmall]: "",
            [f.Small]: h().SMALL_HEIGHT,
            [f.Medium]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT}`,
            [f.Large]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT}`,
            [f.ExtraLarge]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT} ${h().EXTRA_LARGE_HEIGHT}`,
          },
          L = {
            [b.ExtraSmall]: "",
            [b.Small]: h().SMALL,
            [b.Medium]: `${h().SMALL} ${h().MEDIUM}`,
            [b.Large]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE}`,
            [b.ExtraLarge]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE} ${h().EXTRA_LARGE}`,
          },
          M = (e) => {
            let u = e.children,
              t = e.className,
              a = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, x);
            const r = w(),
              i = r.mediaWidth,
              o = r.mediaHeight,
              s = r.mediaSize;
            return n().createElement("div", S({ className: C()(t, O[i], y[o], L[s]) }, a), u);
          },
          T = ["children"];
        const k = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, T);
          return n().createElement(B, null, n().createElement(M, t, u));
        };
        var I = t(493),
          P = t.n(I),
          N = t(887),
          H = t.n(N);
        const W = ["xl", "lg", "md", "sm", "xs"],
          G = (e) => e.includes("_") && ((e) => W.includes(e))(e.split("_").at(-1)),
          $ = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          j = (e, u) =>
            Object.keys(e).reduce((t, a) => {
              if (a in t) return t;
              if (G(a)) {
                const n = a.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const r = $.indexOf(u),
                  i = (-1 !== r ? W.slice(r) : [])
                    .map((e) => n + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  o = i ? e[i] : void 0;
                return ((t[n] = void 0 !== o ? o : e[n]), t);
              }
              const n = e[a];
              return (
                void 0 === n ||
                  ((e, u) => W.some((t) => void 0 !== u[`${e}_${t}`]))(a, e) ||
                  (t[a] = n),
                t
              );
            }, {}),
          z = (e, u = j) => {
            const t = (
              (e, u = j) =>
              (t) => {
                const r = w().mediaSize,
                  i = (0, a.useMemo)(() => u(t, r), [t, r]);
                return n().createElement(e, i);
              }
            )(e, u);
            return n().memo((u) =>
              Object.keys(u).some((e) => G(e) && void 0 !== u[e])
                ? n().createElement(t, u)
                : n().createElement(e, u),
            );
          },
          U = {
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
          V = [
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
        function X() {
          return (
            (X =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            X.apply(this, arguments)
          );
        }
        Object.keys(H());
        const K = {
            XL: { mt: U.mt__XL, mr: U.mr__XL, mb: U.mb__XL, ml: U.ml__XL },
            LG: { mt: U.mt__LG, mr: U.mr__LG, mb: U.mb__LG, ml: U.ml__LG },
            MDp: { mt: U.mt__MDp, mr: U.mr__MDp, mb: U.mb__MDp, ml: U.ml__MDp },
            MD: { mt: U.mt__MD, mr: U.mr__MD, mb: U.mb__MD, ml: U.ml__MD },
            SMp: { mt: U.mt__SMp, mr: U.mr__SMp, mb: U.mb__SMp, ml: U.ml__SMp },
            SM: { mt: U.mt__SM, mr: U.mr__SM, mb: U.mb__SM, ml: U.ml__SM },
            XS: { mt: U.mt__XS, mr: U.mr__XS, mb: U.mb__XS, ml: U.ml__XS },
          },
          Y = (Object.keys(K), ["mt", "mr", "mb", "ml"]),
          q = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Q = z((e) => {
            let u = e.className,
              t = e.width,
              r = e.height,
              i = e.m,
              o = e.mt,
              s = void 0 === o ? i : o,
              l = e.mr,
              E = void 0 === l ? i : l,
              c = e.mb,
              m = void 0 === c ? i : c,
              A = e.ml,
              d = void 0 === A ? i : A,
              _ = e.column,
              F = e.row,
              D = e.flexDirection,
              B = void 0 === D ? (_ ? "column" : F && "row") || void 0 : D,
              p = e.flexStart,
              g = e.center,
              h = e.flexEnd,
              b = e.spaceBetween,
              v = e.spaceAround,
              f = e.justifyContent,
              w =
                void 0 === f
                  ? (p ? "flex-start" : g && "center") ||
                    (h && "flex-end") ||
                    (b && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : f,
              x = e.alignItems,
              S =
                void 0 === x
                  ? (p ? "flex-start" : g && "center") || (h && "flex-end") || void 0
                  : x,
              O = e.alignSelf,
              y = e.wrap,
              L = e.flexWrap,
              M = void 0 === L ? (y ? "wrap" : void 0) : L,
              T = e.grow,
              R = e.shrink,
              k = e.flex,
              I = void 0 === k ? (T || R ? `${T ? 1 : 0} ${R ? 1 : 0} auto` : void 0) : k,
              P = e.style,
              N = e.children,
              H = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, V);
            const W = (0, a.useMemo)(() => {
                const e = { mt: s, mr: E, mb: m, ml: d },
                  u = ((e) =>
                    Y.reduce((u, t) => {
                      const a = e[t];
                      return a && "number" != typeof a ? u.concat(K[!0 === a ? "MD" : a][t]) : u;
                    }, []))(e),
                  a = ((e) =>
                    Y.reduce((u, t) => {
                      const a = e[t];
                      return ("number" == typeof a && (u[q[t]] = a + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, P, a, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: I,
                    alignSelf: O,
                    display: B || S ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: M,
                    justifyContent: w,
                    alignItems: S,
                  }),
                  computedClassNames: u,
                };
              }, [t, r, s, E, m, d, P, I, O, B, M, w, S]),
              G = W.computedStyle,
              $ = W.computedClassNames;
            return n().createElement("div", X({ className: C()(U.base, ...$, u), style: G }, H), N);
          });
        let Z;
        function J(e) {
          return e.replace(/-/g, "_");
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(Z || (Z = {}));
        const ee = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          ue = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          te = (e, u, t = Z.left) => e.split(u).reduce(t === Z.left ? ee : ue, []),
          ae = (() => {
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
          ne = ["zh_cn", "zh_sg", "zh_tw"],
          re = (e, u = Z.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return ne.includes(t)
              ? ae(e)
              : ((e, u = Z.left) => {
                  let t = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (te(n, /( )/, u).forEach((e) => (t = t.concat(te(e, a, Z.left)))), t);
                })(e, u);
          },
          ie = "FormatText_base_d0",
          oe = ({ binding: e, text: u = "", classMix: t, alignment: r = Z.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : n().createElement(
                  a.Fragment,
                  null,
                  u.split("\n").map((u, i) =>
                    n().createElement(
                      "div",
                      { className: C()(ie, t), key: `${u}-${i}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : re(e, u))))(u, r, e).map((e, u) =>
                        n().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var se = t(532),
          le = t.n(se);
        const Ee = {
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
          ce = [
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
        function me() {
          return (
            (me =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            me.apply(this, arguments)
          );
        }
        Object.keys(H());
        const Ae = Object.keys(le()),
          de = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          _e = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Fe = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          De = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Be =
            (Object.keys(De),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": de,
              "heading-H36": de,
              "heading-H28": _e,
              "heading-H24": _e,
              "heading-H24R": _e,
              "heading-H22": _e,
              "heading-H20R": _e,
              "heading-H18": _e,
              "heading-H15": Fe,
              "heading-H14": Fe,
              "paragraph-P24": _e,
              "paragraph-P18": _e,
              "paragraph-P16": _e,
              "paragraph-P14": Fe,
              "paragraph-P12": Fe,
              "paragraph-P10": Fe,
            }),
          pe =
            (Object.keys(Be),
            (e) =>
              e
                ? ((e) => Ae.includes(e))(e)
                  ? { colorClassName: Ee[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Ce = z((e) => {
            let u = e.text,
              t = e.variant,
              r = e.className,
              i = e.color,
              o = e.m,
              s = e.mt,
              l = void 0 === s ? o : s,
              E = e.mr,
              c = void 0 === E ? o : E,
              m = e.mb,
              A = void 0 === m ? o : m,
              d = e.ml,
              _ = void 0 === d ? o : d,
              F = e.style,
              D = e.format,
              B = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, ce);
            const p = (0, a.useMemo)(() => {
                const e = pe(i),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  a = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, a), colorClassName: u };
              }, [F, i]),
              g = p.computedStyle,
              h = p.colorClassName;
            return n().createElement(
              Q,
              me(
                {
                  className: C()(Ee.base, t && Ee[t], h, r),
                  style: g,
                  mt: !0 === l ? Be[t || "paragraph-P16"].mt : l,
                  mr: !0 === c ? Be[t || "paragraph-P16"].mr : c,
                  mb: !0 === A ? Be[t || "paragraph-P16"].mb : A,
                  ml: !0 === _ ? Be[t || "paragraph-P16"].ml : _,
                },
                B,
              ),
              void 0 !== D ? n().createElement(oe, me({}, D, { text: u })) : u,
            );
          }),
          ge = (e = 1) => {
            const u = new Error().stack;
            let t,
              a = R.invalid("resId");
            return (
              u &&
                ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                window.__feature &&
                  window.__feature !== t &&
                  window.subViews[t] &&
                  (a = window.subViews[t].id)),
              { caller: t, stack: u, resId: a }
            );
          };
        var he = t(364);
        const be = [
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
        function ve(e) {
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
        const fe = (e, u, t = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: he.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: a,
                },
                t,
              ),
            );
          },
          we = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              i = e.onMouseLeave,
              o = e.onMouseDown,
              s = e.onClick,
              l = e.ignoreShowDelay,
              E = void 0 !== l && l,
              c = e.ignoreMouseClick,
              m = void 0 !== c && c,
              A = e.decoratorId,
              d = void 0 === A ? 0 : A,
              _ = e.isEnabled,
              F = void 0 === _ || _,
              D = e.targetId,
              B = void 0 === D ? 0 : D,
              p = e.onShow,
              C = e.onHide,
              g = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, be);
            const h = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              b = (0, a.useMemo)(() => B || ge().resId, [B]),
              v = (0, a.useCallback)(() => {
                (h.current.isVisible && h.current.timeoutId) ||
                  (fe(t, d, { isMouseEvent: !0, on: !0, arguments: ve(n) }, b),
                  p && p(),
                  (h.current.isVisible = !0));
              }, [t, d, n, b, p]),
              f = (0, a.useCallback)(() => {
                if (h.current.isVisible || h.current.timeoutId) {
                  const e = h.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (h.current.timeoutId = 0)),
                    fe(t, d, { on: !1 }, b),
                    h.current.isVisible && C && C(),
                    (h.current.isVisible = !1));
                }
              }, [t, d, b, C]),
              w = (0, a.useCallback)((e) => {
                h.current.isVisible &&
                  ((h.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (h.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(h.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = h.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === F && f();
              }, [F, f]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", f),
                  () => {
                    (window.removeEventListener("mouseleave", f), f());
                  }
                ),
                [f],
              ));
            return F
              ? (0, a.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((h.current.timeoutId = window.setTimeout(v, E ? 100 : 400)),
                            r && r(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (f(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === m && f(), null == s || s(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === m && f(), null == o || o(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    g,
                  ),
                )
              : u;
            var x;
          },
          xe = ["children", "body", "header", "note", "alert", "args"];
        function Se() {
          return (
            (Se =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Se.apply(this, arguments)
          );
        }
        const Oe = R.views.common.tooltip_window.simple_tooltip_content,
          ye = (e) => {
            let u = e.children,
              t = e.body,
              r = e.header,
              i = e.note,
              o = e.alert,
              s = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, xe);
            const E = (0, a.useMemo)(() => {
              const e = Object.assign({}, s, { body: t, header: r, note: i, alert: o });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [o, t, r, i, s]);
            return n().createElement(
              we,
              Se(
                {
                  contentId:
                    ((c = null == s ? void 0 : s.hasHtmlContent),
                    c ? Oe.SimpleTooltipHtmlContent("resId") : Oe.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                l,
              ),
              u,
            );
            var c;
          };
        let Le;
        !(function (e) {
          ((e.Available = "available"), (e.Disable = "disable"), (e.Hidden = "hidden"));
        })(Le || (Le = {}));
        var Me = t(521);
        const Te = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function Re(e = Me.n.NONE, u = Te, t = !1) {
          (0, a.useEffect)(() => {
            if (e !== Me.n.NONE)
              return (
                window.addEventListener("keydown", a, t),
                () => {
                  window.removeEventListener("keydown", a, t);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), u(a), t && a.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        const ke = (e, u) => e.split(".").reduce((e, u) => e && e[u], u),
          Ie = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          Pe = (e, u) => (e.length > 0 ? `${e}.${u}` : u),
          Ne = (e) =>
            ((e, u) =>
              e.split(".").reduce((e, t) => {
                const a = ke(`${e}.${t}`, window);
                return Ie(a) ? u(e, t, a) : `${e}.${t}`;
              }))(e, (e, u) => `${e}.${u}.value`),
          He = (e) => {
            const u = ((e) => {
                const u = ge(),
                  t = u.caller,
                  a = u.resId,
                  n = window.__feature && window.__feature !== t && t ? `subViews.${t}` : "";
                return { modelPrefix: n, modelPath: Pe(n, e || ""), resId: a };
              })(),
              t = u.modelPrefix,
              a = e.split(".");
            if (a.length > 0) {
              const e = [a[0]];
              return (
                a.reduce((u, a) => {
                  const n = ke(Pe(t, `${u}.${a}`), window);
                  return Ie(n) ? (e.push(n.id), `${u}.${a}.value`) : (e.push(a), `${u}.${a}`);
                }),
                e.reduce((e, u) => e + "." + u)
              );
            }
            return "";
          },
          We = he.Sw.instance;
        let Ge;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Ge || (Ge = {}));
        const $e = (e = "model", u = Ge.Deep) => {
            const t = (0, a.useState)(0),
              n = (t[0], t[1]),
              r = (0, a.useMemo)(() => ge(), []),
              i = r.caller,
              o = r.resId,
              s = (0, a.useMemo)(
                () => (window.__feature && window.__feature !== i ? `subViews.${i}.${e}` : e),
                [i, e],
              ),
              l = (0, a.useState)(() =>
                ((e) => {
                  const u = ke(e, window);
                  for (const e in u) "function" == typeof u[e] && (u[e] = u[e].bind(u));
                  return Ie(u) ? u.value : u;
                })(Ne(s)),
              ),
              E = l[0],
              c = l[1],
              m = (0, a.useRef)(-1);
            return (
              D(() => {
                if (
                  ("boolean" == typeof u &&
                    ((u = u ? Ge.Deep : Ge.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  u !== Ge.None)
                ) {
                  const t = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      u === Ge.Deep
                        ? (e === E && n((e) => e + 1), c(e))
                        : c(Object.assign([], e));
                    },
                    a = He(e);
                  m.current = We.addCallback(a, t, o, u === Ge.Deep);
                }
              }),
              (0, a.useEffect)(() => {
                if (u !== Ge.None)
                  return () => {
                    We.removeCallback(m.current, o);
                  };
              }, [o, u]),
              E
            );
          },
          je = "display",
          ze = "enabled",
          Ue = "enabled_change";
        function Ve(e) {
          engine.call("PlaySound", e);
        }
        const Xe = {
          playHighlight() {
            Ve("highlight");
          },
          playClick() {
            Ve("play");
          },
          playYes() {
            Ve("yes1");
          },
        };
        var Ke = t(515);
        let Ye, qe;
        (!(function (e) {
          ((e.Available = "available"),
            (e.AvailablePaused = "availablePaused"),
            (e.Active = "active"),
            (e.ActivePaused = "activePaused"),
            (e.Disabled = "disabled"),
            (e.DisabledPaused = "disabledPaused"),
            (e.Completed = "completed"),
            (e.CompletedPerfectly = "completedPerfectly"),
            (e.CompletedPaused = "completedPaused"));
        })(Ye || (Ye = {})),
          (function (e) {
            ((e.Development = "development"),
              (e.Disabled = "disabled"),
              (e.Active = "active"),
              (e.Completed = "completed"));
          })(qe || (qe = {})));
        const Qe = [Ye.Active, Ye.Available, Ye.Completed, Ye.CompletedPerfectly],
          Ze = [Ye.Active, Ye.Completed, Ye.CompletedPerfectly],
          Je = [Ye.Active, Ye.ActivePaused, Ye.Available, Ye.AvailablePaused];
        function eu() {
          return !1;
        }
        console.log;
        var uu = t(174);
        function tu(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return au(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return au(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function au(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, a = new Array(u); t < u; t++) a[t] = e[t];
          return a;
        }
        const nu = (e) => (0 === e ? window : window.subViews.get(e));
        var ru = t(946);
        const iu = ((e, u) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: r = "real", options: o, children: s, mocks: l }) {
                const E = (0, a.useRef)([]),
                  c = (t, a, n) => {
                    var r;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = nu,
                        context: a = "model",
                      } = {}) {
                        const n = new Map();
                        function r(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? n.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = n.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const o = (e) => {
                          const n = t(u),
                            r = a.split(".").reduce((e, u) => e[u], n);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, r);
                        };
                        return {
                          subscribe: (t, r) => {
                            const s = "string" == typeof r ? `${a}.${r}` : a,
                              l = i.O.view.addModelObserver(s, u, !0);
                            return (n.set(l, t), e && t(o(r)), l);
                          },
                          readByPath: o,
                          createCallback: (e, u) => {
                            const t = o(u);
                            return (...u) => {
                              t(e(...u));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const u = o(e);
                            return () => {
                              u();
                            };
                          },
                          dispose: function () {
                            for (var e, t = tu(n.keys()); !(e = t()).done;) r(e.value, u);
                          },
                          unsubscribe: r,
                        };
                      })(a),
                      s =
                        "real" === t
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (r = null == n ? void 0 : n.getter) ? r : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == n ? void 0 : n.getter(e)) : s.readByPath(e),
                      c = (e) => E.current.push(e),
                      m = e({
                        mode: t,
                        readByPath: l,
                        externalModel: s,
                        observableModel: {
                          array: (e, u) => {
                            const a = null != u ? u : l(e),
                              n = uu.LO.box(a, { equals: eu });
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, uu.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          object: (e, u) => {
                            const a = null != u ? u : l(e),
                              n = uu.LO.box(a, { equals: eu });
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, uu.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          primitives: (e, u) => {
                            const a = l(u);
                            if (Array.isArray(e)) {
                              const n = e.reduce((e, u) => ((e[u] = uu.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  s.subscribe(
                                    (0, uu.aD)((u) => {
                                      e.forEach((e) => {
                                        n[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                n
                              );
                            }
                            {
                              const n = e,
                                r = Object.entries(n),
                                i = r.reduce((e, [u, t]) => ((e[t] = uu.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  s.subscribe(
                                    (0, uu.aD)((e) => {
                                      r.forEach(([u, t]) => {
                                        i[t].set(e[u]);
                                      });
                                    }),
                                    u,
                                  ),
                                i
                              );
                            }
                          },
                        },
                        cleanup: c,
                      }),
                      A = { mode: t, model: m, externalModel: s, cleanup: c };
                    return {
                      model: m,
                      controls: "mocks" === t && n ? n.controls(A) : u(A),
                      externalModel: s,
                      mode: t,
                    };
                  },
                  m = (0, a.useRef)(!1),
                  A = (0, a.useState)(r),
                  d = A[0],
                  _ = A[1],
                  F = (0, a.useState)(() => c(r, o, l)),
                  D = F[0],
                  B = F[1];
                return (
                  (0, a.useEffect)(() => {
                    m.current ? B(c(d, o, l)) : (m.current = !0);
                  }, [l, d, o]),
                  (0, a.useEffect)(() => {
                    _(r);
                  }, [r]),
                  (0, a.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), E.current.forEach((e) => e()));
                    },
                    [D],
                  ),
                  n().createElement(t.Provider, { value: D }, s)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  operations: e.array("operations"),
                  lastOperation: e.object("lastOperation"),
                },
                t = (0, ru.Om)(
                  () => {
                    return (
                      (e = u.operations.get()),
                      (t = (e) => Object.assign({}, e)),
                      Array.isArray(e)
                        ? e.map(t)
                        : e.map((e, u, a) => t(null == e ? void 0 : e.value, u, a))
                    );
                    var e, t;
                  },
                  { equals: eu },
                );
              return Object.assign({}, u, { computes: { getOperations: t } });
            },
            ({ externalModel: e }) => ({
              openOperation: e.createCallback((e) => ({ operationId: e }), "onOpenOperation"),
              takeRewards: e.createCallbackNoArgs("onTakeRewards"),
              info: e.createCallbackNoArgs("onInfo"),
              close: e.createCallbackNoArgs("onClose"),
            }),
          ),
          ou = iu[0],
          su = iu[1],
          lu = {
            base: "App_base_8c",
            base__visible: "App_base__visible_74",
            fadeIn: "App_fadeIn_31",
            content: "App_content_ac",
            button: "App_button_42",
            header: "App_header_e4",
            info: "App_info_90",
            headerText: "App_headerText_23",
            headerButton: "App_headerButton_e1",
            operations: "App_operations_64",
            operations__small: "App_operations__small_45",
            video: "App_video_96",
            bgLow: "App_bgLow_ac",
            bgRoom: "App_bgRoom_b0",
            bgBlink: "App_bgBlink_8c",
            bgTable: "App_bgTable_0c",
            bgTable__low: "App_bgTable__low_63",
            bgSmoke: "App_bgSmoke_bd",
            parallax: "App_parallax_c5",
            vignette: "App_vignette_88",
          },
          Eu = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let cu, mu;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(cu || (cu = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(mu || (mu = {})));
        const Au = ({ size: e = cu.Default, classMix: u }) =>
            n().createElement("div", { className: C()(Eu.background, Eu[`background__${e}`], u) }),
          du = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          _u = ({ size: e }) => {
            const u = C()(du.base, du[`base__${e}`]);
            return n().createElement("div", { className: u });
          },
          Fu = {
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
          Du = (0, a.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: a,
              isComplete: r,
              withoutBounce: i,
            }) => {
              const o = C()(
                  Fu.base,
                  Fu[`base__${e}`],
                  t && Fu.base__disabled,
                  r && Fu.base__finished,
                  i && Fu.base__withoutBounce,
                ),
                s = !t && !r;
              return n().createElement(
                "div",
                { className: o, style: a, ref: u },
                n().createElement("div", { className: Fu.pattern }),
                n().createElement("div", { className: Fu.gradient }),
                s && n().createElement(_u, { size: e }),
              );
            },
          ),
          Bu = ({ size: e, value: u, lineRef: t, disabled: r, onComplete: i }) => {
            const o = (0, a.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              s = 100 === u;
            return (
              (0, a.useEffect)(() => {
                s && i && i();
              }, [s, i]),
              n().createElement(Du, {
                size: e,
                disabled: r,
                baseStyles: o,
                isComplete: s,
                lineRef: t,
              })
            );
          },
          pu = (e, u) => {
            let t;
            const a = setTimeout(() => {
              t = e();
            }, u);
            return () => {
              ("function" == typeof t && t(), clearTimeout(a));
            };
          };
        let Cu, gu;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(Cu || (Cu = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(gu || (gu = {})));
        const hu = "ProgressBarDeltaSimple_base_6c",
          bu = "ProgressBarDeltaSimple_delta_99",
          vu = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: i,
              to: o,
              onEndAnimation: s,
              onChangeAnimationState: l,
            }) => {
              const E = o < r,
                c = (0, a.useState)(gu.Idle),
                m = c[0],
                A = c[1],
                d = m === gu.In,
                _ = m === gu.End,
                F = m === gu.Idle,
                D = (0, a.useCallback)(
                  (e) => {
                    (A(e), l && l(e));
                  },
                  [l],
                );
              ((0, a.useEffect)(() => {
                if (F && !t) {
                  return pu(() => {
                    D(gu.In);
                  }, u);
                }
              }, [D, t, F, u]),
                (0, a.useEffect)(() => {
                  if (d) {
                    return pu(() => {
                      (s && s(), D(gu.End));
                    }, e + u);
                  }
                }, [D, d, s, u, e]));
              const B = (0, a.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [E ? "left" : "right"]: "0",
                  }),
                  [E, u, e],
                ),
                p = (0, a.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [E ? "left" : "right"]: "0",
                  }),
                  [E, u, e],
                ),
                C = (0, a.useMemo)(
                  () => ({ width: `${Math.abs(r - o)}%`, left: `${E ? o : r}%` }),
                  [r, E, o],
                );
              return _
                ? null
                : n().createElement(
                    "div",
                    { className: hu, style: C },
                    n().createElement(
                      "div",
                      { style: F ? B : p, className: bu },
                      n().createElement(_u, { size: i }),
                    ),
                  );
            },
          ),
          fu = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: i,
              isComplete: o,
              animationSettings: s,
              onChangeAnimationState: l,
              onEndAnimation: E,
            }) => {
              const c = (0, a.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${s.line.duration}ms`,
                  transitionDelay: `${s.line.delay}ms`,
                }),
                [s.line.delay, s.line.duration, e],
              );
              return n().createElement(
                n().Fragment,
                null,
                n().createElement(Du, {
                  size: u,
                  lineRef: r,
                  disabled: i,
                  isComplete: o,
                  baseStyles: c,
                }),
                t >= 0 &&
                  n().createElement(vu, {
                    transitionDuration: s.delta.duration,
                    transitionDelay: s.delta.delay,
                    freezed: s.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: E,
                  }),
              );
            },
          ),
          wu = "ProgressBarDeltaGrow_base_7e",
          xu = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          Su = "ProgressBarDeltaGrow_glow_68",
          Ou = (e) => (e ? { left: 0 } : { right: 0 }),
          yu = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          Lu = (e) => ({ transitionDuration: `${e}ms` }),
          Mu = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: i,
              to: o,
              onEndAnimation: s,
              onChangeAnimationState: l,
              className: E,
            }) => {
              const c = o < r,
                m = (0, a.useState)(Cu.Idle),
                A = m[0],
                d = m[1],
                _ = A === Cu.End,
                F = A === Cu.Idle,
                D = A === Cu.Grow,
                B = A === Cu.Shrink,
                p = (0, a.useCallback)(
                  (e) => {
                    (d(e), l && l(e));
                  },
                  [l],
                ),
                g = (0, a.useCallback)(
                  (e, u) =>
                    pu(() => {
                      p(e);
                    }, u),
                  [p],
                );
              (0, a.useEffect)(() => {
                if (!t)
                  return F
                    ? g(Cu.Grow, u)
                    : D
                      ? g(Cu.Shrink, e)
                      : B
                        ? g(Cu.End, e)
                        : void (_ && s && s());
              }, [g, t, _, D, F, B, s, u, e]);
              const h = (0, a.useMemo)(
                  () => Object.assign({ width: "100%" }, Lu(e), Ou(c)),
                  [c, e],
                ),
                b = (0, a.useMemo)(() => Object.assign({ width: "0%" }, Lu(e), Ou(c)), [c, e]),
                v = (0, a.useMemo)(
                  () => Object.assign({ width: "0%" }, yu(c, r), Lu(e)),
                  [r, c, e],
                ),
                f = (0, a.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - r)}%` }, yu(c, r), Lu(e)),
                  [r, c, o, e],
                );
              if (_) return null;
              const w = C()(wu, E, c && 0 === o && xu);
              return n().createElement(
                "div",
                { style: F ? v : f, className: w },
                n().createElement(
                  "div",
                  { style: B ? b : h, className: Su },
                  n().createElement(_u, { size: i }),
                ),
              );
            },
          ),
          Tu = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: i,
              isComplete: o,
              animationSettings: s,
              onEndAnimation: l,
              onChangeAnimationState: E,
            }) => {
              const c = e < t,
                m = (0, a.useState)(!1),
                A = m[0],
                d = m[1],
                _ = (0, a.useCallback)(
                  (e) => {
                    (e === Cu.Shrink && d(!0), E && E(e));
                  },
                  [E],
                ),
                F = (0, a.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                D = (0, a.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${s.line.duration}ms` }),
                  [s.line.duration, e],
                );
              return n().createElement(
                n().Fragment,
                null,
                n().createElement(Du, {
                  size: u,
                  lineRef: r,
                  disabled: i,
                  isComplete: o,
                  withoutBounce: c && 0 === e,
                  baseStyles: A ? D : F,
                }),
                t >= 0 &&
                  n().createElement(Mu, {
                    transitionDuration: s.delta.duration,
                    transitionDelay: s.delta.delay,
                    onChangeAnimationState: _,
                    freezed: s.freezed,
                    onEndAnimation: l,
                    from: t,
                    size: u,
                    to: e,
                    className: s.delta.className,
                  }),
              );
            },
          ),
          Ru = ["onComplete", "onEndAnimation"];
        function ku() {
          return (
            (ku =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ku.apply(this, arguments)
          );
        }
        const Iu = (0, a.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Ru);
            const i = (0, a.useState)(!1),
              o = i[0],
              s = i[1],
              l = (0, a.useCallback)(() => {
                const e = 100 === r.to;
                (e !== o && s(e), e && u && u(), t && t());
              }, [o, u, t, r.to]);
            switch (r.animationSettings.type) {
              case mu.Simple:
                return n().createElement(fu, ku({}, r, { onEndAnimation: l, isComplete: o }));
              case mu.Growing:
                return n().createElement(Tu, ku({}, r, { onEndAnimation: l, isComplete: o }));
              default:
                return null;
            }
          }),
          Pu = ["onEndAnimation"];
        function Nu() {
          return (
            (Nu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Nu.apply(this, arguments)
          );
        }
        const Hu = (0, a.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, Pu);
          const r = (0, a.useRef)({}),
            i = (0, a.useCallback)(() => {
              ((r.current.from = void 0), u && u());
            }, [u]),
            o = "number" == typeof r.current.from ? r.current.from : t.from;
          return (
            (r.current.from = o),
            n().createElement(Iu, Nu({}, t, { onEndAnimation: i, key: `${o}-${t.to}`, from: o }))
          );
        });
        function Wu() {
          return (
            (Wu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Wu.apply(this, arguments)
          );
        }
        const Gu = (0, a.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: a,
              deltaFrom: r,
              animationSettings: i,
              onEndAnimation: o,
              onChangeAnimationState: s,
              onComplete: l,
            }) => {
              if (r === u)
                return n().createElement(Bu, {
                  key: `${r}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: a,
                  onComplete: l,
                });
              const E = {
                from: r,
                to: u,
                size: e,
                lineRef: t,
                disabled: a,
                animationSettings: i,
                onComplete: l,
                onEndAnimation: o,
                onChangeAnimationState: s,
              };
              return i.withStack
                ? n().createElement(Hu, E)
                : n().createElement(Iu, Wu({ key: `${r}-${u}` }, E));
            },
          ),
          $u = (e) => ({
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
          ju = (e, u, t) => (t < e ? e : t > u ? u : t),
          zu = (e, u, t) => {
            if ("number" == typeof t) {
              return (ju(0, u, t) / u) * 100;
            }
            return e;
          },
          Uu = {
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
          Vu = {
            freezed: !1,
            withStack: !1,
            type: mu.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          Xu = (0, a.memo)(
            ({
              maxValue: e = 100,
              theme: u = Uu,
              size: t = cu.Default,
              animationSettings: r = Vu,
              disabled: i = !1,
              withoutBackground: o = !1,
              progressBarBackgroundClassMix: s,
              value: l,
              deltaFrom: E,
              lineRef: c,
              onChangeAnimationState: m,
              onEndAnimation: A,
              onComplete: d,
            }) => {
              const _ = ((e, u, t) =>
                (0, a.useMemo)(() => {
                  const a = (ju(0, u, e) / u) * 100;
                  return { value: a, deltaFrom: zu(a, u, t) };
                }, [t, u, e]))(l, e, E);
              return n().createElement(
                "div",
                { className: C()(Eu.base, Eu[`base__${t}`]), style: $u(u) },
                !o && n().createElement(Au, { size: t, classMix: s }),
                n().createElement(Gu, {
                  size: t,
                  lineRef: c,
                  disabled: i,
                  value: _.value,
                  deltaFrom: _.deltaFrom,
                  animationSettings: r,
                  onEndAnimation: A,
                  onChangeAnimationState: m,
                  onComplete: d,
                }),
              );
            },
          ),
          Ku = {
            base: "LastOperation_base_58",
            base__active: "LastOperation_base__active_51",
            base__completed: "LastOperation_base__completed_4c",
            base__development: "LastOperation_base__development_bb",
            backlight: "LastOperation_backlight_56",
            base__hovered: "LastOperation_base__hovered_47",
            bg: "LastOperation_bg_d7",
            stroke: "LastOperation_stroke_09",
            strokeGradient: "LastOperation_strokeGradient_1a",
            content: "LastOperation_content_b7",
            icon: "LastOperation_icon_f2",
            leftSection: "LastOperation_leftSection_20",
            base__disabled: "LastOperation_base__disabled_dd",
            title: "LastOperation_title_f0",
            subtitle: "LastOperation_subtitle_92",
            subtitle__text: "LastOperation_subtitle__text_58",
            iconLock: "LastOperation_iconLock_f2",
            development: "LastOperation_development_43",
            typeIcon: "LastOperation_typeIcon_19",
            typeIcon__heavyTank_elite: "LastOperation_typeIcon__heavyTank_elite_35",
            taskCompleted: "LastOperation_taskCompleted_4f",
            completedText: "LastOperation_completedText_25",
            operationText: "LastOperation_operationText_5a",
            operationText__done: "LastOperation_operationText__done_10",
            operationText__divider: "LastOperation_operationText__divider_ef",
            progressBarWrapper: "LastOperation_progressBarWrapper_30",
            progressBar: "LastOperation_progressBar_02",
            completedWrapper: "LastOperation_completedWrapper_25",
            completedIcon: "LastOperation_completedIcon_42",
          },
          Yu = R.strings.personal_missions_3.OperationsView,
          qu = "_elite",
          Qu = (0, a.memo)(
            ({
              name: e,
              level: u,
              typeIcon: t,
              totalQuests: r,
              delta: i,
              completedQuests: o,
              status: s,
              vehicleName: l,
              isElite: E,
              operationId: c,
            }) => {
              const m = (0, a.useState)(!1),
                A = m[0],
                d = m[1],
                _ = w().mediaSize,
                F = s === qe.Development,
                D = s === qe.Active || s === qe.Completed,
                B = _ === b.ExtraSmall ? b.Small : _,
                p = J(t),
                g = F ? "hidden" : `veh_${c}`,
                h = {
                  contentId:
                    R.views.lobby.personal_missions.tooltips.PersonalMissionsLastOperationTooltip(
                      "resId",
                    ),
                  args: { operationId: c },
                  ignoreShowDelay: !0,
                };
              return n().createElement(
                we,
                h,
                n().createElement(
                  "div",
                  {
                    className: C()(
                      Ku.base,
                      Ku[`base__${s}`],
                      A && Ku.base__hovered,
                      A && Ku[`base__${s}Hovered`],
                    ),
                    onMouseEnter: () => {
                      F || d(!0);
                    },
                    onMouseLeave: () => {
                      d(!1);
                    },
                  },
                  n().createElement("div", { className: Ku.backlight }),
                  n().createElement("div", { className: Ku.bg }),
                  n().createElement("div", { className: Ku.stroke }),
                  D && n().createElement("div", { className: Ku.strokeGradient }),
                  n().createElement(
                    "div",
                    { className: Ku.content },
                    n().createElement(
                      "div",
                      { className: Ku.leftSection },
                      n().createElement(Ce, {
                        className: Ku.title,
                        text: Yu.step(),
                        format: { binding: { name: e } },
                      }),
                      n().createElement(
                        "div",
                        { className: Ku.subtitle },
                        F
                          ? n().createElement(
                              n().Fragment,
                              null,
                              n().createElement("div", { className: Ku.iconLock }),
                              n().createElement(Ce, {
                                className: Ku.development,
                                text: Yu.development(),
                              }),
                            )
                          : n().createElement(
                              n().Fragment,
                              null,
                              n().createElement(Ce, { className: Ku.subtitle__text, text: u }),
                              n().createElement("div", {
                                className: C()(Ku.typeIcon, Ku[`typeIcon__${p}${E ? qu : ""}`]),
                                style: {
                                  backgroundImage: `url(R.images.gui.maps.icons.vehicleTypes.c_44x44.${p}${E ? qu : ""})`,
                                },
                              }),
                              n().createElement(Ce, { className: Ku.subtitle__text, text: l }),
                            ),
                      ),
                      s === qe.Completed
                        ? n().createElement(
                            "div",
                            { className: Ku.completedWrapper },
                            n().createElement("div", { className: Ku.completedIcon }),
                          )
                        : n().createElement(
                            "div",
                            { className: Ku.taskCompleted },
                            n().createElement(Ce, {
                              className: Ku.completedText,
                              text: Yu.completedLast(),
                            }),
                            n().createElement(Ce, {
                              className: C()(Ku.operationText, Ku.operationText__done),
                              text: String(o),
                            }),
                            n().createElement(Ce, {
                              className: C()(Ku.operationText, Ku.operationText__divider),
                              text: Yu.divider(),
                            }),
                            n().createElement(Ce, { className: Ku.operationText, text: String(r) }),
                          ),
                      n().createElement(
                        "div",
                        { className: Ku.progressBarWrapper },
                        n().createElement(
                          "div",
                          { className: Ku.progressBar },
                          n().createElement(Xu, {
                            size: cu.Medium,
                            maxValue: r,
                            value: o,
                            deltaFrom: i,
                            disabled: !D,
                          }),
                        ),
                      ),
                    ),
                    n().createElement("div", {
                      className: Ku.icon,
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.personalMissions3.OperationsView.vehicles.${g}_${B})`,
                      },
                    }),
                  ),
                ),
              );
            },
          ),
          Zu = ["children"];
        function Ju() {
          return (
            (Ju =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Ju.apply(this, arguments)
          );
        }
        const et = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, Zu);
          return n().createElement(
            we,
            Ju(
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
        function ut() {
          return (
            (ut =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ut.apply(this, arguments)
          );
        }
        const tt = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const a = n().createElement("div", { className: t }, e);
          if (u.header || u.body) return n().createElement(ye, u, a);
          const r = u.contentId,
            i = u.args,
            o = null == i ? void 0 : i.contentId;
          return r || o
            ? n().createElement(we, ut({}, u, { contentId: r || o }), a)
            : n().createElement(et, u, a);
        };
        let at;
        !(function (e) {
          ((e.BIG = "l"), (e.SMALL = "s"));
        })(at || (at = {}));
        const nt = (e) => {
            if (!e) return !1;
            const u = e.videoHeight,
              t = e.videoWidth;
            return Boolean(u && t);
          },
          rt = {
            base: "Operation_base_e5",
            base__active: "Operation_base__active_f0",
            base__available: "Operation_base__available_29",
            base__availablePaused: "Operation_base__availablePaused_13",
            base__activePaused: "Operation_base__activePaused_39",
            base__hovered: "Operation_base__hovered_3f",
            backlight: "Operation_backlight_65",
            bg: "Operation_bg_95",
            bg__france: "Operation_bg__france_4d",
            base__disabled: "Operation_base__disabled_f1",
            base__disabledPaused: "Operation_base__disabledPaused_a7",
            base__completed: "Operation_base__completed_06",
            base__completedPerfectly: "Operation_base__completedPerfectly_d1",
            base__completedPaused: "Operation_base__completedPaused_58",
            stroke: "Operation_stroke_5a",
            strokeGradient: "Operation_strokeGradient_44",
            icon: "Operation_icon_41",
            disabled: "Operation_disabled_0c",
            content: "Operation_content_40",
            title: "Operation_title_c6",
            subtitle: "Operation_subtitle_5d",
            typeIcon: "Operation_typeIcon_0b",
            typeIcon__heavyTank: "Operation_typeIcon__heavyTank_f5",
            typeIcon__heavyTank_elite: "Operation_typeIcon__heavyTank_elite_c4",
            typeIcon__AT_SPG_elite: "Operation_typeIcon__AT_SPG_elite_3a",
            typeIcon__mediumTank_elite: "Operation_typeIcon__mediumTank_elite_1f",
            typeIcon__lightTank_elite: "Operation_typeIcon__lightTank_elite_86",
            taskCompleted: "Operation_taskCompleted_b8",
            warning: "Operation_warning_2f",
            warning__string: "Operation_warning__string_62",
            warning__text: "Operation_warning__text_37",
            warning__name: "Operation_warning__name_40",
            specialIcon: "Operation_specialIcon_d5",
            completedText: "Operation_completedText_bf",
            operationText: "Operation_operationText_06",
            operationText__done: "Operation_operationText__done_56",
            operationText__divider: "Operation_operationText__divider_bc",
            progressBarWrapper: "Operation_progressBarWrapper_8e",
            progressBar: "Operation_progressBar_f1",
          },
          it = R.strings.personal_missions_3.OperationsView,
          ot = R.strings.personal_missions_3.tooltips.OperationsView.operation,
          st = "_elite",
          lt = (0, a.memo)(
            ({
              name: e,
              level: u,
              typeIcon: t,
              totalQuests: r,
              completedQuests: i,
              delta: o,
              status: s,
              vehicleName: l,
              id: E,
              operationId: c,
              prevOperationName: m,
              isElite: A,
              isHasLevels: d,
            }) => {
              const _ = (0, a.useState)(!1),
                F = _[0],
                D = _[1],
                B = w().mediaSize,
                p = Qe.some((e) => s === e),
                g = Ze.some((e) => s === e),
                h = s !== Ye.Disabled && s !== Ye.DisabledPaused,
                v = s === Ye.Disabled,
                f = s === Ye.Active || s === Ye.Available,
                x = s === Ye.Completed || s === Ye.CompletedPerfectly,
                S = (({ icon: e, status: u, bigStatuses: t, mediaSize: a, path: n }) =>
                  `url(${n}.${e}_${t.some((e) => u === e) ? at.BIG : at.SMALL}_${a === b.ExtraSmall ? b.Small : a})`)(
                  {
                    icon: `veh_${c}`,
                    status: s,
                    bigStatuses: Je,
                    mediaSize: B,
                    path: "R.images.gui.maps.icons.personalMissions3.OperationsView.vehicles",
                  },
                ),
                O = !p && s !== Ye.Disabled,
                y = J(t),
                L = O && d,
                M = L
                  ? {
                      header:
                        ((T = ot.simple.disabled.header()),
                        (k = { name: e }),
                        T.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
                          const u = 0 === e.indexOf("%") ? 2 : 1;
                          return String(k[e.slice(u, -u)]);
                        })),
                      body: ot.simple.disabled.body(),
                      ignoreShowDelay: !0,
                    }
                  : {
                      contentId:
                        R.views.lobby.personal_missions.tooltips.PersonalMissionsOperationsTooltip(
                          "resId",
                        ),
                      args: { operationId: c },
                      ignoreShowDelay: !0,
                    };
              var T, k;
              return n().createElement(
                tt,
                { tooltipArgs: M },
                n().createElement(
                  "div",
                  {
                    className: C()(
                      rt.base,
                      rt[`base__${s}`],
                      F && rt.base__hovered,
                      F && rt[`base__${s}Hovered`],
                    ),
                    onMouseEnter: () => {
                      L || D(!0);
                    },
                    onMouseLeave: () => {
                      D(!1);
                    },
                    id: E,
                  },
                  n().createElement("div", { className: rt.backlight }),
                  n().createElement("div", { className: C()(rt.bg, 10 === c && rt.bg__france) }),
                  n().createElement("div", { className: rt.icon, style: { backgroundImage: S } }),
                  !p && n().createElement("div", { className: rt.disabled }),
                  n().createElement("div", { className: rt.stroke }),
                  g && n().createElement("div", { className: rt.strokeGradient }),
                  n().createElement(
                    "div",
                    { className: rt.content },
                    n().createElement(
                      "div",
                      { className: rt.title },
                      n().createElement(Ce, { text: it.operationName() }),
                      n().createElement(Ce, {
                        text: it.warningOperationName(),
                        format: { binding: { name: e } },
                      }),
                    ),
                    n().createElement(
                      "div",
                      { className: rt.subtitle },
                      n().createElement(Ce, { className: rt.level, text: u }),
                      n().createElement("div", {
                        className: C()(rt.typeIcon, rt[`typeIcon__${y}${A ? st : ""}`]),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.vehicleTypes.c_44x44.${y}${A ? st : ""})`,
                        },
                      }),
                      n().createElement(Ce, { className: rt.vehicleName, text: l }),
                    ),
                    f
                      ? n().createElement(
                          "div",
                          { className: rt.taskCompleted },
                          n().createElement(Ce, {
                            className: rt.completedText,
                            text: it.completedTasks(),
                          }),
                          n().createElement(Ce, {
                            className: C()(rt.operationText, rt.operationText__done),
                            text: String(i),
                          }),
                          n().createElement(Ce, {
                            className: C()(rt.operationText, rt.operationText__divider),
                            text: it.divider(),
                          }),
                          n().createElement(Ce, { className: rt.operationText, text: String(r) }),
                        )
                      : n().createElement(
                          "div",
                          { className: rt.warning },
                          n().createElement("div", { className: rt.specialIcon }),
                          n().createElement(
                            "div",
                            { className: rt.warning__string },
                            !x &&
                              n().createElement(Ce, {
                                text: v ? it.warningOperation() : it.unavailable(),
                                className: rt.warning__text,
                              }),
                            v &&
                              n().createElement(Ce, {
                                text: it.warningOperationName(),
                                format: { binding: { name: m } },
                                className: C()(rt.warning__text, rt.warning__name),
                              }),
                          ),
                        ),
                    h &&
                      n().createElement(
                        "div",
                        { className: rt.progressBarWrapper },
                        n().createElement(
                          "div",
                          { className: rt.progressBar },
                          n().createElement(Xu, {
                            size: cu.Medium,
                            maxValue: r,
                            value: i,
                            deltaFrom: o,
                            disabled: !p || s === Ye.Available,
                          }),
                        ),
                      ),
                  ),
                ),
              );
            },
          ),
          Et = {
            base: "Operations_base_6a",
            operations: "Operations_operations_bb",
            operation: "Operations_operation_75",
            operation__last: "Operations_operation__last_03",
          };
        function ct() {
          return (
            (ct =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ct.apply(this, arguments)
          );
        }
        const mt = (0, a.memo)(({ operations: e, lastOperation: u, onOpenOperation: t }) => {
            const a = u.status === qe.Development,
              r = (e, u) => {
                e && (Xe.playClick(), t(u));
              };
            return n().createElement(
              "div",
              { className: Et.base },
              n().createElement(
                "div",
                { className: Et.operations },
                e.map((u, t) => {
                  const a =
                    Qe.some((e) => u.status === e) || u.status === Ye.Disabled || !u.isHasLevels;
                  return n().createElement(
                    "div",
                    {
                      key: `${u.name}_${t}`,
                      className: C()(Et.operation, t + 1 === e.length && Et.operation__last),
                      onClick: () => r(a, u.operationId),
                      onMouseEnter: a ? Xe.playHighlight : void 0,
                    },
                    n().createElement(lt, ct({}, u, { id: 0 === t ? "operation-block" : "" })),
                  );
                }),
              ),
              n().createElement(
                "div",
                {
                  className: Et.lastOperation,
                  onClick: () => r(!a, u.operationId),
                  onMouseEnter: a ? void 0 : Xe.playHighlight,
                },
                n().createElement(Qu, u),
              ),
            );
          }),
          At = {
            frameCount: 51,
            chunk: { count: 1, columns: 7, rows: 8 },
            path: "R.images.gui.maps.icons.personalMissions3.OperationsView.sequences.bg_smoke",
            frameTime: 30,
          },
          dt = [
            { koeffX: 0.005, koeffY: 0, classNames: lu.bgRoom },
            {
              koeffX: 0.005,
              koeffY: 0,
              cfg: {
                frameCount: 51,
                chunk: { count: 1, columns: 7, rows: 8 },
                path: "R.images.gui.maps.icons.personalMissions3.OperationsView.sequences.bg_blink",
                frameTime: 60,
              },
              sizes: {
                smallWidth: 162,
                smallHeight: 162,
                mediumWidth: 204,
                mediumHeight: 204,
                largeWidth: 256,
                largeHeight: 256,
              },
              classNames: lu.bgBlink,
            },
            {
              koeffX: 0.0025,
              koeffY: 0,
              src:
                null == R.videos.personal_mission.video_operations_person
                  ? void 0
                  : R.videos.personal_mission.video_operations_person(),
              classNames: lu.video,
            },
            { koeffX: 0, koeffY: 0, classNames: lu.bgTable, lowClassNames: lu.bgTable },
            {
              koeffX: 0,
              koeffY: 0,
              cfg: At,
              sizes: {
                smallWidth: 147,
                smallHeight: 133,
                mediumWidth: 168,
                mediumHeight: 152,
                largeWidth: 210,
                largeHeight: 190,
              },
              classNames: lu.bgSmoke,
            },
          ],
          _t = () => {
            const e = (0, a.useState)(i.O.view.getScale()),
              u = e[0],
              t = e[1];
            return (
              (0, a.useEffect)(() => {
                const e = () => {
                  t(i.O.view.getScale());
                };
                return (
                  window.addEventListener("resize", e),
                  () => {
                    window.removeEventListener("resize", e);
                  }
                );
              }, []),
              u
            );
          };
        var Ft = t(30);
        const Dt = 33,
          Bt = 0,
          pt = !0,
          Ct = "play";
        const gt = [
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
        function ht() {
          return (
            (ht =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ht.apply(this, arguments)
          );
        }
        const bt = (0, a.memo)(function (e) {
            let u = e.width,
              t = e.height,
              r = e.getImageSource,
              i = e.frameCount,
              o = e.onAnimate,
              s = e.frameTime,
              l = void 0 === s ? Dt : s,
              E = e.initialFrameIndex,
              c = void 0 === E ? Bt : E,
              m = e.lastFrameIndex,
              A = void 0 === m ? i - 1 : m,
              d = e.loop,
              _ = void 0 === d ? pt : d,
              F = e.state,
              D = void 0 === F ? Ct : F,
              B = e.onAnimationDone,
              p = e.onAnimationComplete,
              C = e.poster,
              g = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, gt);
            const h = (0, a.useRef)(null);
            return (
              (0, a.useEffect)(() => {
                const e = h.current;
                if (!e) return;
                const u = e.getContext("2d"),
                  t = (t) => {
                    (u.clearRect(0, 0, e.width, e.height), u.drawImage(t.img, -t.x, -t.y));
                  };
                switch (D) {
                  case "play":
                    return (function () {
                      const e = wt(c, A, r),
                        u = vt(c, A),
                        a = window.setInterval(() => {
                          const n = u(),
                            r = e.get(n);
                          r
                            ? (null == o || o(n, r),
                              t(r),
                              n === A &&
                                (null == p || p(),
                                _ || (null == B || B(), window.clearInterval(a))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, l);
                      return () => window.clearInterval(a);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === c && C ? { path: C, x: 0, y: 0 } : r(c),
                        u = new Image();
                      u.src = e.path;
                      const a = () => t(ft(e, u));
                      return (
                        u.addEventListener("load", a),
                        () => u.removeEventListener("load", a)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [l, r, c, A, _, o, p, B, C, D]),
              n().createElement("canvas", ht({}, g, { width: u, height: t, ref: h }))
            );
          }),
          vt = (e, u) => {
            let t = e;
            return () => {
              const a = t;
              return ((t += 1), t > u && (t = e), a);
            };
          },
          ft = (e, u) => Object.assign({}, e, { img: u }),
          wt = (e, u, t) => {
            const a = new Map(),
              n = {};
            for (let r = e; r <= u; r++) {
              const e = t(r),
                u = n[e.path];
              if (u) a.set(r, ft(e, u));
              else {
                const u = new Image();
                ((n[e.path] = u),
                  (u.src = e.path),
                  (u.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${r})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  a.set(r, ft(e, u)));
              }
            }
            return a;
          };
        const xt = "SequencedBg_base_2b",
          St = "SequencedBg_base__scaled_85",
          Ot = n().memo(({ cfg: e, sizes: u }) => {
            const t = w().mediaSize,
              a = _t(),
              r = (({ mediaSize: e, cfg: u, sizes: t }) => {
                const a = e === b.ExtraSmall ? b.Small : e,
                  n = a === b.Large ? b.ExtraLarge : a,
                  r = `${u.path}_${n}`,
                  i = {
                    width: t.smallWidth,
                    height: t.smallHeight,
                    frameCount: u.frameCount,
                    chunk: u.chunk,
                    getChunkPath: () => r,
                  };
                return n === b.Medium
                  ? Object.assign({}, i, { width: t.mediumWidth, height: t.mediumHeight })
                  : n === b.ExtraLarge
                    ? Object.assign({}, i, { width: t.largeWidth, height: t.largeHeight })
                    : i;
              })({ mediaSize: t, cfg: e, sizes: u }),
              i = (function (e) {
                const u = e.chunk,
                  t = u.rows * u.columns;
                return (a) => {
                  const n = a % t,
                    r = (n % u.columns) * e.width,
                    i = Math.trunc(n / u.columns) * e.height;
                  return { path: e.getChunkPath(Math.trunc(a / t)), x: r, y: i };
                };
              })(r);
            return n().createElement(
              "div",
              { className: C()(xt, 2 === a && St) },
              n().createElement(bt, {
                frameTime: e.frameTime,
                state: "play",
                width: r.width,
                height: r.height,
                frameCount: r.frameCount,
                getImageSource: i,
              }),
            );
          }),
          yt = (e) => {
            const u = (0, a.useRef)();
            return (
              (0, a.useEffect)(() => {
                u.current = e;
              }, [e]),
              u.current
            );
          };
        let Lt;
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
        })(Lt || (Lt = {}));
        Date.now();
        he.Sw.instance;
        const Mt = yt,
          Tt = "Video_video_26",
          Rt = n().memo(function ({
            src: e,
            className: u,
            autoPlay: t,
            isPaused: r = !1,
            loop: i = !1,
            loopPartDuration: o = 0,
            onStarted: s,
            onUpdated: l,
            onError: E,
            onSetVideoReady: c,
            onSetVideoIsPresent: m,
          }) {
            const A = (0, a.useRef)(null),
              d = ((e) => {
                const u = (0, a.useState)(nt(e ? e.current : null)),
                  t = u[0],
                  n = u[1];
                return (
                  (0, a.useEffect)(() => {
                    let u = 0;
                    const t = () => {
                      u = requestAnimationFrame(() => {
                        nt(e ? e.current : null) ? n(!0) : t();
                      });
                    };
                    return (
                      t(),
                      () => {
                        cancelAnimationFrame(u);
                      }
                    );
                  }, [e]),
                  (0, a.useEffect)(() => () => n(!1), [e]),
                  t
                );
              })(A),
              _ = Mt(r),
              F = (0, a.useCallback)(() => {
                s && !_ && s();
              }, [s, _]),
              D = (0, a.useCallback)(() => {
                const e = A.current;
                e &&
                  (i
                    ? ((e.currentTime = e.duration - o), e.removeEventListener("play", F), e.play())
                    : e.pause());
              }, [F, i, o]);
            return (
              (0, a.useEffect)(() => {
                const e = A.current;
                return (
                  e && (e.addEventListener("play", F), e.addEventListener("ended", D)),
                  () => {
                    e && (e.removeEventListener("play", F), e.removeEventListener("ended", D));
                  }
                );
              }, [D, F]),
              (0, a.useEffect)(
                () =>
                  pu(() => {
                    d ? c(d) : m(!1);
                  }, 250),
                [d, m, c],
              ),
              (0, a.useEffect)(() => {
                const e = A.current;
                e && e.play();
              }, [l, r]),
              n().createElement(
                "div",
                { className: u },
                n().createElement("video", {
                  ref: A,
                  src: e,
                  className: C()(Tt),
                  loop: !1,
                  autoPlay: t,
                  onError: E,
                }),
              )
            );
          }),
          kt = "LayerItem_base_3d",
          It = "LayerItem_base__scaled_dd",
          Pt = (0, a.memo)(
            ({
              x: e,
              y: u,
              koeffX: t,
              koeffY: r,
              classNames: i,
              cfg: o,
              sizes: s,
              src: l,
              onSetVideoReady: E,
              onSetVideoIsPresent: c,
            }) => {
              const m = _t(),
                A = (0, Ft.useSpring)(() => ({
                  xy: [0, 0],
                  config: { mass: 0.2, tension: 500, friction: 150 },
                })),
                d = A[0],
                _ = A[1],
                F = (0, a.useCallback)((e, u) => `translate3d(${e * t}rem,${u * r}rem,0)`, [t, r]);
              _.start({ xy: ((e, u) => [e, u])(e, u) });
              const D = (0, a.useMemo)(() => ({ transform: d.xy.to(F) }), [d.xy, F]),
                B = o && s,
                p = !o && l;
              return n().createElement(
                Ft.animated.div,
                { className: C()(kt, 2 === m && !p && It, i), style: D },
                B && n().createElement(Ot, { cfg: o, sizes: s }),
                p &&
                  n().createElement(Rt, {
                    src: l,
                    className: i,
                    onSetVideoReady: E,
                    onSetVideoIsPresent: c,
                    autoPlay: !0,
                    loop: !0,
                  }),
              );
            },
          ),
          Nt = "PMParallax_base_14";
        function Ht() {
          return (
            (Ht =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Ht.apply(this, arguments)
          );
        }
        const Wt = (0, a.memo)(({ onSetVideoReady: e, onSetVideoIsPresent: u }) => {
            const t = (0, a.useState)({ x: 0, y: 0 }),
              r = t[0],
              o = t[1],
              s = (0, a.createRef)(),
              l = (0, a.useCallback)(
                (e) => {
                  if (!s.current) return;
                  const u = s.current.getBoundingClientRect(),
                    t = u.width,
                    a = u.height;
                  return !(
                    0 === e.clientX ||
                    0 === e.clientY ||
                    e.clientX >= t - 1 ||
                    e.clientY >= a - 1
                  );
                },
                [s],
              );
            return (
              (0, a.useEffect)(() => {
                const e = (e) => {
                  if (!l(e)) return;
                  const u = i.O.client.getSize("rem").width,
                    t = i.O.client.getSize("rem").height / 2;
                  o({ x: u / 2 - e.clientX, y: t - e.clientY });
                };
                return (
                  document.addEventListener("mousemove", e),
                  () => {
                    document.removeEventListener("mousemove", e);
                  }
                );
              }, [l]),
              n().createElement(
                "div",
                { ref: s, className: Nt },
                dt.map((t, a) =>
                  n().createElement(
                    Pt,
                    Ht({}, t, {
                      key: a,
                      x: r.x,
                      y: r.y,
                      onSetVideoReady: e,
                      onSetVideoIsPresent: u,
                    }),
                  ),
                ),
              )
            );
          }),
          Gt = "TakeRewards_base_79",
          $t = "TakeRewards_base__disabled_48",
          jt = "TakeRewards_button_be",
          zt = "TakeRewards_border_b0",
          Ut = "TakeRewards_glow_3c",
          Vt = "TakeRewards_content_f0",
          Xt = "TakeRewards_buttonIcon_68",
          Kt = "TakeRewards_title_ec",
          Yt = "TakeRewards_hightlightWrapper_a8",
          qt = "TakeRewards_hightlight_6e",
          Qt = R.strings.personal_missions_3.OperationsView.takeRewards,
          Zt = (0, a.memo)(({ onClick: e, isDisabled: u = !1 }) =>
            n().createElement(
              "div",
              { className: C()(Gt, u && $t) },
              n().createElement(
                ye,
                { body: u ? Qt.tooltipDisable() : Qt.tooltip() },
                n().createElement(
                  "div",
                  {
                    className: jt,
                    onClick: u
                      ? void 0
                      : () => {
                          (e(), Xe.playClick());
                        },
                    onMouseEnter: u ? void 0 : Xe.playHighlight,
                  },
                  !u &&
                    n().createElement(
                      n().Fragment,
                      null,
                      n().createElement("div", { className: zt }),
                      n().createElement("div", { className: Ut }),
                    ),
                  n().createElement(
                    "div",
                    { className: Vt },
                    n().createElement("div", { className: Xt }),
                    n().createElement(Ce, { text: Qt.title(), className: Kt }),
                  ),
                  !u &&
                    n().createElement(
                      "div",
                      { className: Yt },
                      n().createElement("div", { className: qt }),
                    ),
                ),
              ),
            ),
          ),
          Jt = R.strings.personal_missions_3.OperationsView,
          ea = "PersonalMissionsOperation";
        viewEnv.clearInternalCacheAfterFinalize();
        const ua = (0, Ke.Pi)(() => {
          const e = su(),
            u = e.controls,
            t = e.model,
            r = t.root.get(),
            i = r.rewardsStatus,
            o = r.lastOperation,
            s = (0, a.useState)(!1),
            l = s[0],
            E = s[1],
            c = (0, a.useState)(!0),
            m = c[0],
            A = c[1],
            d = t.computes.getOperations(),
            _ =
              1 === viewEnv.getGraphicsQuality() ||
              !R.videos.personal_mission.video_operations_person ||
              !m,
            F = ((e, u) => {
              const t = $e("tutorialModel.effects.items").filter((t) => {
                if (!t) return !1;
                const a = t.value,
                  n = window.__featureId.toString();
                return a.componentId === e && a.type === u && a.viewId === n;
              });
              if (0 === t.length) return null;
              const a = Object.assign({}, t[0].value);
              return {
                effect: a,
                completeEffect: () => {
                  (tutorialModel.onEffectCompleted({
                    componentId: e,
                    viewId: window.__featureId.toFixed(0),
                    effectType: u,
                    effectBuilder: a.builder,
                  }),
                    u === je && window.tutorialApi && window.tutorialApi.updateComponents());
                },
              };
            })(ea, ze);
          (0, a.useEffect)(
            () =>
              ((e) => {
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
              })(() => {
                null !== F && F.completeEffect();
              }),
            [F],
          );
          const D = ((e, u) => {
            const t = $e("tutorialModel.triggers.items").filter((t) => {
              if (!t) return !1;
              const a = t.value,
                n = a.triggers.filter((e) => e.value === u);
              return a.componentId === e && n.length > 0;
            });
            return 0 === t.length
              ? null
              : window.tutorialModel.foundComponents.items.some((u) => u.value.componentId === e)
                ? {
                    trigger: t[0].value,
                    runTrigger: (t) => {
                      window.tutorialModel.onTriggerActivated({
                        componentId: e,
                        triggerType: u,
                        state: t,
                      });
                    },
                  }
                : null;
          })(ea, Ue);
          (0, a.useEffect)(() => {
            D && D.runTrigger(!0);
          }, [D]);
          const B = Je.some((e) => d.some((u) => u.status === e));
          var p;
          ((p = u.close), Re(Me.n.ESCAPE, p));
          return n().createElement(
            "div",
            { className: C()(lu.base, (l || _) && lu.base__visible, _ && lu.base__low) },
            _
              ? n().createElement("div", { className: lu.bgLow })
              : n().createElement(
                  n().Fragment,
                  null,
                  n().createElement("div", { className: lu.vignette }),
                  n().createElement(
                    "div",
                    { className: lu.parallax },
                    n().createElement(Wt, { onSetVideoReady: E, onSetVideoIsPresent: A }),
                  ),
                ),
            n().createElement(
              "div",
              { className: lu.header },
              n().createElement(Ce, { text: Jt.title(), className: lu.headerText }),
              n().createElement(
                ye,
                { body: Jt.info.tooltip() },
                n().createElement("div", {
                  className: lu.info,
                  onClick: () => {
                    (Xe.playClick(), u.info());
                  },
                  onMouseEnter: Xe.playHighlight,
                }),
              ),
            ),
            n().createElement(
              "div",
              { className: lu.content },
              i !== Le.Hidden &&
                n().createElement(
                  "div",
                  { className: lu.button },
                  n().createElement(Zt, { onClick: u.takeRewards, isDisabled: i === Le.Disable }),
                ),
              n().createElement(
                "div",
                { className: C()(lu.operations, B && lu.operations__small) },
                n().createElement(mt, {
                  operations: d,
                  lastOperation: o,
                  onOpenOperation: u.openOperation,
                }),
              ),
            ),
          );
        });
        const ta = {
            rewardsStatus: Le.Available,
            lastOperation: {
              name: "Колхозавро",
              icon: "maus",
              level: "XI",
              typeIcon: "AT-SPG",
              totalQuests: 75,
              completedQuests: 55,
              delta: 55,
              status: qe.Development,
              vehicleName: "Reno Logan",
            },
            operations: [
              {
                name: "tail_8",
                icon: "waffen",
                level: "VI",
                typeIcon: "AT-SPG",
                totalQuests: 75,
                completedQuests: 0,
                delta: 0,
                status: Ye.ActivePaused,
                vehicleName: "Reno Logan",
                operationId: 8,
                prevOperationName: "",
                isElite: !0,
                isHasLevels: !1,
              },
              {
                name: "tail_9",
                icon: "bct",
                level: "VI",
                typeIcon: "AT-SPG",
                totalQuests: 75,
                completedQuests: 45,
                delta: 45,
                status: Ye.Completed,
                vehicleName: "Reno Logan",
                operationId: 9,
                prevOperationName: "tail_8",
                isElite: !0,
                isHasLevels: !0,
              },
              {
                name: "tail_10",
                icon: "bct",
                level: "VI",
                typeIcon: "AT-SPG",
                totalQuests: 75,
                completedQuests: 55,
                delta: 55,
                status: Ye.CompletedPerfectly,
                vehicleName: "Reno Logan",
                operationId: 10,
                prevOperationName: "tail_9",
                isElite: !0,
                isHasLevels: !0,
              },
            ],
          },
          aa = {
            getter: ((na = ta), (e) => (e ? e.split(".").reduce((e, u) => e[u], na) : na)),
            controls: () =>
              (function (e) {
                const u = {};
                for (const t in e)
                  if (Object.prototype.hasOwnProperty.call(e, t)) {
                    const a = e[t];
                    u[t] = (0, uu.aD)(a);
                  }
                return u;
              })({
                close: () => {
                  console.log("Call onClosee");
                },
                openOperation: (e) => {
                  console.log(`Call onOpenOperation ${e}`);
                },
                takeRewards: () => {
                  console.log("Call onTakeRewards");
                },
                info: () => {
                  console.log("Call onInfo");
                },
              }),
          };
        var na;
        engine.whenReady.then(() => {
          P().render(
            n().createElement(
              ou,
              { mode: "real", mocks: aa },
              n().createElement(k, null, n().createElement(ua, null)),
            ),
            document.getElementById("root"),
          );
        });
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
    (__webpack_require__.O = (e, u, t, a) => {
      if (!u) {
        var n = 1 / 0;
        for (s = 0; s < deferred.length; s++) {
          for (var [u, t, a] = deferred[s], r = !0, i = 0; i < u.length; i++)
            (!1 & a || n >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[i]))
              ? u.splice(i--, 1)
              : ((r = !1), a < n && (n = a));
          if (r) {
            deferred.splice(s--, 1);
            var o = t();
            void 0 !== o && (e = o);
          }
        }
        return e;
      }
      a = a || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > a; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [u, t, a];
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
    (__webpack_require__.j = 535),
    (() => {
      var e = { 535: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var a,
            n,
            [r, i, o] = t,
            s = 0;
          if (r.some((u) => 0 !== e[u])) {
            for (a in i) __webpack_require__.o(i, a) && (__webpack_require__.m[a] = i[a]);
            if (o) var l = o(__webpack_require__);
          }
          for (u && u(t); s < r.length; s++)
            ((n = r[s]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [650], () => __webpack_require__(937));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
