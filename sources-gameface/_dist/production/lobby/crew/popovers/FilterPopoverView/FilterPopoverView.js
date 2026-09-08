(() => {
  var __webpack_modules__ = {
      926: (u) => {
        u.exports = {
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
      3532: (u) => {
        u.exports = {
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
      9887: (u) => {
        u.exports = {
          XS: "4rem",
          SM: "8rem",
          SMp: "10rem",
          MD: "16rem",
          MDp: "20rem",
          LG: "32rem",
          XL: "64rem",
        };
      },
      527: (u, e, t) => {
        "use strict";
        (t.r(e), t.d(e, { mouse: () => i, onResize: () => a }));
        var n = t(2472),
          r = t(1176);
        const a = (0, n.E)("clientResized"),
          o = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const i = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && (0, r.R)(!1);
          }
          function t() {
            u.enabled && (0, r.R)(!0);
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
              : (0, r.R)(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let r = !0;
                  const a = `mouse${e}`,
                    i = o[e]((u) => t([u, "outside"]));
                  function s(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(a, s),
                    n(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(a, s), (u.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(t)),
              e
            ),
            {},
          );
          return Object.assign({}, a, {
            disable() {
              ((u.enabled = !1), n());
            },
            enable() {
              ((u.enabled = !0), n());
            },
            enableOutside() {
              u.enabled && (0, r.R)(!0);
            },
            disableOutside() {
              u.enabled && (0, r.R)(!1);
            },
          });
        })();
      },
      5959: (u, e, t) => {
        "use strict";
        (t.r(e),
          t.d(e, {
            events: () => n,
            getMouseGlobalPosition: () => a,
            getSize: () => r,
            graphicsQuality: () => o,
          }));
        var n = t(527);
        function r(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function a(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const o = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (u, e, t) => {
        "use strict";
        function n(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        t.d(e, { R: () => n });
      },
      2472: (u, e, t) => {
        "use strict";
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
        "use strict";
        t.d(e, { O: () => r });
        var n = t(5959);
        const r = { view: t(7641), client: n };
      },
      3722: (u, e, t) => {
        "use strict";
        function n(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function r(u, e, t) {
          return `url(${n(u, e, t)})`;
        }
        (t.r(e), t.d(e, { getBgUrl: () => r, getTextureUrl: () => n }));
      },
      6112: (u, e, t) => {
        "use strict";
        t.d(e, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => r });
        var n = t(2472);
        const r = {
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
        "use strict";
        (t.r(e),
          t.d(e, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => a.U,
            extraSize: () => x,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => m,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => b,
            getScale: () => F,
            getSize: () => A,
            getViewGlobalPosition: () => _,
            isClientAccessible: () => h,
            isEventHandled: () => p,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => d,
            sendEvent: () => o.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => f,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => S,
          }));
        var n = t(3722),
          r = t(6112),
          a = t(6538),
          o = t(8566);
        function i(u) {
          viewEnv.addPreloadTexture(u);
        }
        function s(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function l(u, e, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, n);
        }
        function c(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function E(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function A(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function d(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function _(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: B(e.x), y: B(e.y) };
        }
        function m() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
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
        function f() {
          return viewEnv.setEventHandled();
        }
        function p() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function b() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(r.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === r.W[e]), u),
            {},
          ),
          x = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          S = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : a.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => l });
        const n = ["args"];
        const r = 2,
          a = 16,
          o = 32,
          i = 64,
          s = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                o = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(u);
                  for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                  return r;
                })(e, n);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, o, {
                      arguments:
                        ((r = a),
                        Object.entries(r).map(([u, e]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, o));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var r;
          },
          l = {
            close(u) {
              s("popover" === u ? r : o);
            },
            minimize() {
              s(i);
            },
            move(u) {
              s(a, { isMouseEvent: !0, on: u });
            },
          };
      },
      5521: (u, e, t) => {
        "use strict";
        let n, r;
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
          })(r || (r = {})));
      },
      1358: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => a });
        var n = t(3138);
        class r {
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
            return (window.__dataTracker || (window.__dataTracker = new r()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(u, e, t = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = n.O.view.addModelObserver(u, t, r);
            return (
              a > 0
                ? ((this._callbacks[a] = e),
                  t > 0 && (this._views[t] ? this._views[t].push(a) : (this._views[t] = [a])))
                : console.error("Can't add callback for model:", u),
              a
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
        "use strict";
        t.d(e, { B0: () => s, ry: () => B, Eu: () => C, SW: () => f });
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
        const r = n;
        var a = t(1358);
        const o = {
            getNumberFormat: (u, e) => systemLocale.getNumberFormat(u, e),
            getRealFormat: (u, e) => systemLocale.getRealFormat(u, e),
            getTimeFormat: (u, e) => systemLocale.getTimeFormat(u, e),
            getDateFormat: (u, e) => systemLocale.getDateFormat(u, e),
            toUpperCase: (u) => systemLocale.toUpperCase(u),
            toLowerCase: (u) => systemLocale.toUpperCase(u),
          },
          i = {
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
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          A = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var d = t(5521),
          _ = t(3138);
        const m = ["args"];
        function F(u, e, t, n, r, a, o) {
          try {
            var i = u[a](o),
              s = i.value;
          } catch (u) {
            return void t(u);
          }
          i.done ? e(s) : Promise.resolve(s).then(n, r);
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
                  return new Promise(function (n, r) {
                    var a = u.apply(e, t);
                    function o(u) {
                      F(a, n, r, o, i, "next", u);
                    }
                    function i(u) {
                      F(a, n, r, o, i, "throw", u);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          C = () =>
            new Promise((u) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  u();
                });
              });
            }),
          g = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const r = e.args,
                a = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(u);
                  for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                  return r;
                })(e, m);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, a, {
                      arguments:
                        ((n = r),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, a));
            } else viewEnv.handleViewEvent({ __Type: t, type: u });
            var n;
          },
          h = () => g(s.CLOSE),
          f = () => g(s.POP_OVER, { on: !1 }),
          p = (u, e) => {
            u.keyCode === d.n.ESCAPE && e();
          };
        var v = t(7572);
        const b = r.instance,
          w = {
            DataTracker: a.Z,
            ViewModel: v.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: A,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => g(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: h,
            sendClosePopOverEvent: f,
            sendShowContextMenuEvent: (u, e, t = 0) => {
              g(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, n, r = R.invalid("resId"), a) => {
              const o = _.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                E = i.width,
                A = i.height,
                d = {
                  x: _.O.view.pxToRem(l) + o.x,
                  y: _.O.view.pxToRem(c) + o.y,
                  width: _.O.view.pxToRem(E),
                  height: _.O.view.pxToRem(A),
                };
              g(s.POP_OVER, {
                isMouseEvent: !0,
                contentID: u,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: e,
                bbox: D(d),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (u) => {
              const e = (e) => p(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              p(u, h);
            },
            handleViewEvent: g,
            onBindingsReady: B,
            onLayoutReady: C,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
            dumpViewModel: function u(e) {
              const t = {};
              if ("object" != typeof e) return e;
              for (const n in e)
                if (Object.prototype.hasOwnProperty.call(e, n)) {
                  const r = Object.prototype.toString.call(e[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = e[n];
                    t[n] = [];
                    for (let e = 0; e < r.length; e++) t[n].push({ value: u(r[e].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = u(e[n]))
                      : (t[n] = e[n]);
                }
              return t;
            },
            ClickOutsideManager: b,
            SystemLocale: o,
            UserLocale: i,
          };
        window.ViewEnvHelper = w;
      },
      3939: (u, e, t) => {
        "use strict";
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => yt,
            Bar: () => wt,
            DefaultScroll: () => St,
            Direction: () => ct,
            defaultSettings: () => Et,
            useHorizontalScrollApi: () => dt,
          }));
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => Xt,
            Bar: () => zt,
            Default: () => $t,
            useVerticalScrollApi: () => Mt,
          }));
        var a = t(6179),
          o = t.n(a);
        const i = (u, e, t) =>
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
        var s = t(3138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function E(u, e, t) {
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
            r = (function (u, e) {
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
        !(function (u) {
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
        })(c || (c = {}));
        const A = s.O.client.getSize("rem"),
          d = A.width,
          _ = A.height,
          m = Object.assign({ width: d, height: _ }, E(d, _, l)),
          F = (0, a.createContext)(m),
          D = ["children"];
        const B = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                r = {},
                a = Object.keys(u);
              for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
              return r;
            })(u, D);
          const n = (0, a.useContext)(F),
            r = n.extraLarge,
            o = n.large,
            s = n.medium,
            l = n.small,
            c = n.extraSmall,
            E = n.extraLargeWidth,
            A = n.largeWidth,
            d = n.mediumWidth,
            _ = n.smallWidth,
            m = n.extraSmallWidth,
            B = n.extraLargeHeight,
            C = n.largeHeight,
            g = n.mediumHeight,
            h = n.smallHeight,
            f = n.extraSmallHeight,
            p = { extraLarge: B, large: C, medium: g, small: h, extraSmall: f };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && r) return e;
            if (t.large && o) return e;
            if (t.medium && s) return e;
            if (t.small && l) return e;
            if (t.extraSmall && c) return e;
          } else {
            if (t.extraLargeWidth && E) return i(e, t, p);
            if (t.largeWidth && A) return i(e, t, p);
            if (t.mediumWidth && d) return i(e, t, p);
            if (t.smallWidth && _) return i(e, t, p);
            if (t.extraSmallWidth && m) return i(e, t, p);
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
              if (t.extraSmallHeight && f) return e;
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
        const C = (u) => {
            const e = (0, a.useRef)(!1);
            e.current || (u(), (e.current = !0));
          },
          g = (0, a.memo)(({ children: u }) => {
            const e = (0, a.useContext)(F),
              t = (0, a.useState)(e),
              n = t[0],
              r = t[1],
              i = (0, a.useCallback)((u, e) => {
                const t = s.O.view.pxToRem(u),
                  n = s.O.view.pxToRem(e);
                r(Object.assign({ width: t, height: n }, E(t, n, l)));
              }, []);
            (C(() => {
              engine.on("clientResized", i);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, a.useMemo)(() => Object.assign({}, n), [n]);
            return o().createElement(F.Provider, { value: c }, u);
          });
        var h = t(6483),
          f = t.n(h),
          p = t(926),
          v = t.n(p);
        let b, w, x;
        (!(function (u) {
          ((u[(u.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = l.small.width)] = "Small"),
            (u[(u.Medium = l.medium.width)] = "Medium"),
            (u[(u.Large = l.large.width)] = "Large"),
            (u[(u.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
          (function (u) {
            ((u[(u.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = l.small.width)] = "Small"),
              (u[(u.Medium = l.medium.width)] = "Medium"),
              (u[(u.Large = l.large.width)] = "Large"),
              (u[(u.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
          })(w || (w = {})),
          (function (u) {
            ((u[(u.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = l.small.height)] = "Small"),
              (u[(u.Medium = l.medium.height)] = "Medium"),
              (u[(u.Large = l.large.height)] = "Large"),
              (u[(u.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(x || (x = {})));
        const S = () => {
            const u = (0, a.useContext)(F),
              e = u.width,
              t = u.height,
              n = ((u) => {
                switch (!0) {
                  case u.extraLarge:
                    return b.ExtraLarge;
                  case u.large:
                    return b.Large;
                  case u.medium:
                    return b.Medium;
                  case u.small:
                    return b.Small;
                  case u.extraSmall:
                    return b.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), b.ExtraSmall);
                }
              })(u),
              r = ((u) => {
                switch (!0) {
                  case u.extraLargeWidth:
                    return w.ExtraLarge;
                  case u.largeWidth:
                    return w.Large;
                  case u.mediumWidth:
                    return w.Medium;
                  case u.smallWidth:
                    return w.Small;
                  case u.extraSmallWidth:
                    return w.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), w.ExtraSmall);
                }
              })(u),
              o = ((u) => {
                switch (!0) {
                  case u.extraLargeHeight:
                    return x.ExtraLarge;
                  case u.largeHeight:
                    return x.Large;
                  case u.mediumHeight:
                    return x.Medium;
                  case u.smallHeight:
                    return x.Small;
                  case u.extraSmallHeight:
                    return x.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), x.ExtraSmall);
                }
              })(u);
            return {
              mediaSize: n,
              mediaWidth: r,
              mediaHeight: o,
              remScreenWidth: e,
              remScreenHeight: t,
            };
          },
          y = ["children", "className"];
        function M() {
          return (
            (M =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            M.apply(this, arguments)
          );
        }
        const L = {
            [w.ExtraSmall]: "",
            [w.Small]: v().SMALL_WIDTH,
            [w.Medium]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH}`,
            [w.Large]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH} ${v().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH} ${v().LARGE_WIDTH} ${v().EXTRA_LARGE_WIDTH}`,
          },
          T = {
            [x.ExtraSmall]: "",
            [x.Small]: v().SMALL_HEIGHT,
            [x.Medium]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT}`,
            [x.Large]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT} ${v().LARGE_HEIGHT}`,
            [x.ExtraLarge]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT} ${v().LARGE_HEIGHT} ${v().EXTRA_LARGE_HEIGHT}`,
          },
          O = {
            [b.ExtraSmall]: "",
            [b.Small]: v().SMALL,
            [b.Medium]: `${v().SMALL} ${v().MEDIUM}`,
            [b.Large]: `${v().SMALL} ${v().MEDIUM} ${v().LARGE}`,
            [b.ExtraLarge]: `${v().SMALL} ${v().MEDIUM} ${v().LARGE} ${v().EXTRA_LARGE}`,
          },
          N = (u) => {
            let e = u.children,
              t = u.className,
              n = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(u);
                for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                return r;
              })(u, y);
            const r = S(),
              a = r.mediaWidth,
              i = r.mediaHeight,
              s = r.mediaSize;
            return o().createElement("div", M({ className: f()(t, L[a], T[i], O[s]) }, n), e);
          },
          P = ["children"];
        const H = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                r = {},
                a = Object.keys(u);
              for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
              return r;
            })(u, P);
          return o().createElement(g, null, o().createElement(N, t, e));
        };
        var I = t(493),
          k = t.n(I);
        var W = t(4179);
        const G = [
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
        function U(u) {
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
        const j = (u, e, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: W.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: n,
                },
                t,
              ),
            );
          },
          z = (u) => {
            let e = u.children,
              t = u.contentId,
              n = u.args,
              r = u.onMouseEnter,
              o = u.onMouseLeave,
              i = u.onMouseDown,
              s = u.onClick,
              l = u.ignoreShowDelay,
              c = void 0 !== l && l,
              E = u.ignoreMouseClick,
              A = void 0 !== E && E,
              d = u.decoratorId,
              _ = void 0 === d ? 0 : d,
              m = u.isEnabled,
              F = void 0 === m || m,
              D = u.targetId,
              B = void 0 === D ? 0 : D,
              C = u.onShow,
              g = u.onHide,
              h = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(u);
                for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                return r;
              })(u, G);
            const f = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              p = (0, a.useMemo)(
                () =>
                  B ||
                  ((u = 1) => {
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
                  })().resId,
                [B],
              ),
              v = (0, a.useCallback)(() => {
                (f.current.isVisible && f.current.timeoutId) ||
                  (j(t, _, { isMouseEvent: !0, on: !0, arguments: U(n) }, p),
                  C && C(),
                  (f.current.isVisible = !0));
              }, [t, _, n, p, C]),
              b = (0, a.useCallback)(() => {
                if (f.current.isVisible || f.current.timeoutId) {
                  const u = f.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (f.current.timeoutId = 0)),
                    j(t, _, { on: !1 }, p),
                    f.current.isVisible && g && g(),
                    (f.current.isVisible = !1));
                }
              }, [t, _, p, g]),
              w = (0, a.useCallback)((u) => {
                f.current.isVisible &&
                  ((f.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (f.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(f.current.prevTarget) && b();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const u = f.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === F && b();
              }, [F, b]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", b),
                  () => {
                    (window.removeEventListener("mouseleave", b), b());
                  }
                ),
                [b],
              ));
            return F
              ? (0, a.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((f.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            r && r(u),
                            x && x(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (b(), null == o || o(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === A && b(), null == s || s(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === A && b(), null == i || i(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    h,
                  ),
                )
              : e;
            var x;
          },
          V = ["children", "body", "header", "note", "alert", "args"];
        function $() {
          return (
            ($ =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            $.apply(this, arguments)
          );
        }
        const X = R.views.common.tooltip_window.simple_tooltip_content,
          K = (u) => {
            let e = u.children,
              t = u.body,
              n = u.header,
              r = u.note,
              i = u.alert,
              s = u.args,
              l = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(u);
                for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                return r;
              })(u, V);
            const c = (0, a.useMemo)(() => {
              const u = Object.assign({}, s, { body: t, header: n, note: r, alert: i });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [i, t, n, r, s]);
            return o().createElement(
              z,
              $(
                {
                  contentId:
                    ((E = null == s ? void 0 : s.hasHtmlContent),
                    E ? X.SimpleTooltipHtmlContent("resId") : X.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              e,
            );
            var E;
          },
          Y = (u) => {
            let e,
              t = null;
            return (
              (t = requestAnimationFrame(() => {
                t = requestAnimationFrame(() => {
                  ((t = null), (e = u()));
                });
              })),
              () => {
                ("function" == typeof e && e(), null !== t && cancelAnimationFrame(t));
              }
            );
          },
          q = (u) => {
            (0, a.useEffect)(u, []);
          };
        function Z(u) {
          engine.call("PlaySound", u);
        }
        const Q = {
            playHighlight() {
              Z("highlight");
            },
            playClick() {
              Z("play");
            },
            playYes() {
              Z("yes1");
            },
          },
          J = {
            base: "PopoverDecorator_base_ed",
            decorator: "PopoverDecorator_decorator_d3",
            arrow: "PopoverDecorator_arrow_8a",
            arrow__bottom: "PopoverDecorator_arrow__bottom_c3",
            arrow__top: "PopoverDecorator_arrow__top_6e",
            arrow__left: "PopoverDecorator_arrow__left_7a",
            arrow__right: "PopoverDecorator_arrow__right_b6",
            closeBtn: "PopoverDecorator_closeBtn_32",
            content: "PopoverDecorator_content_f0",
          };
        var uu;
        !(function (u) {
          ((u[(u.Left = 0)] = "Left"),
            (u[(u.Right = 1)] = "Right"),
            (u[(u.Top = 2)] = "Top"),
            (u[(u.Bottom = 3)] = "Bottom"));
        })(uu || (uu = {}));
        const eu = ["__left", "__right", "__top", "__bottom"],
          tu = (0, a.forwardRef)(
            (
              { children: u, disableAutoSizeUpdate: e, onOutsideClick: t, customStyles: n = {} },
              r,
            ) => {
              const i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = (0, a.useState)(window.decorator && window.decorator.directionType),
                A = E[0],
                d = E[1],
                _ = (0, a.useCallback)(() => {
                  (Q.playClick(), s.O.view.sendEvent.close());
                }, []),
                m = (0, a.useCallback)(() => {
                  Q.playHighlight();
                }, []),
                F = f()(J.arrow, J[`arrow${eu[A]}`]);
              q(
                () => (
                  s.O.client.events.mouse.enableOutside(),
                  s.O.client.events.mouse.down(([, u]) => {
                    "outside" === u && (t ? t() : s.O.view.sendEvent.close("popover"));
                  })
                ),
              );
              const D = (0, a.useCallback)(
                  (u) => {
                    let e = u.target;
                    do {
                      if (e === i.current || e === c.current) return;
                      e = e.parentNode;
                    } while (e);
                    const n = window.decorator;
                    if (void 0 !== window.decorator) {
                      const u = s.O.client.getMouseGlobalPosition(),
                        e = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                        t =
                          u.x < n.boundX ||
                          u.x > n.boundX + n.boundWidth ||
                          u.y > n.boundY + n.boundHeight ||
                          u.y < n.boundY;
                      if (e && !t) return;
                    }
                    t ? t() : s.O.view.sendEvent.close("popover");
                  },
                  [i, c, t],
                ),
                B = (0, a.useCallback)(
                  () => (
                    s.O.view.freezeTextureBeforeResize(),
                    Y(() => {
                      if (l.current) {
                        const u = l.current.scrollWidth,
                          e = l.current.scrollHeight;
                        (s.O.view.resize(u, e), d(window.decorator.directionType));
                      }
                    })
                  ),
                  [],
                );
              return (
                (0, a.useImperativeHandle)(r, () => ({ updateSize: B })),
                q(() => {
                  s.O.view.setInputPaddingsRem(58);
                }),
                (0, a.useEffect)(() => {
                  document.addEventListener("mousedown", D, { capture: !0 });
                  const u = ((u) => {
                    let e = !1;
                    return {
                      promise: new Promise((t, n) => {
                        u.then((u) => !e && t(u)).catch((u) => !e && n(u));
                      }),
                      cancel() {
                        e = !0;
                      },
                    };
                  })((0, W.Eu)());
                  return (
                    !e && u.promise.then(() => B()),
                    () => {
                      (u.cancel(), document.removeEventListener("mousedown", D));
                    }
                  );
                }, [B, D, e]),
                o().createElement(
                  "div",
                  { className: J.base, ref: l },
                  o().createElement(
                    "div",
                    { className: J.decorator },
                    o().createElement(
                      "div",
                      { className: J.content, ref: i },
                      u,
                      window.decorator &&
                        window.decorator.isCloseBtnVisible &&
                        o().createElement(
                          K,
                          { body: R.strings.dialogs.common.error.cancel() },
                          o().createElement("div", {
                            className: J.closeBtn,
                            onClick: _,
                            onMouseEnter: m,
                            ref: c,
                          }),
                        ),
                    ),
                    o().createElement("div", { className: F, style: n.arrow }),
                  ),
                )
              );
            },
          );
        var nu = t(5521);
        const ru = (u) => {
          console.error(u.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function au(u = nu.n.NONE, e = ru, t = !1) {
          (0, a.useEffect)(() => {
            if (u !== nu.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === u) {
                if (s.O.view.isEventHandled()) return;
                (s.O.view.setEventHandled(), e(n), t && n.stopPropagation());
              }
            }
          }, [e, u, t]);
        }
        function ou(u, e) {
          var t;
          if (!(e >= u.length))
            return Array.isArray(u) ? u[e] : null == (t = u[e]) ? void 0 : t.value;
        }
        function iu(u, e) {
          return Array.isArray(u)
            ? u.map(e)
            : u.map((u, t, n) => e(null == u ? void 0 : u.value, t, n));
        }
        var su = t(3403);
        const lu = ["children"];
        function cu() {
          return (
            (cu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            cu.apply(this, arguments)
          );
        }
        const Eu = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                r = {},
                a = Object.keys(u);
              for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
              return r;
            })(u, lu);
          return o().createElement(
            z,
            cu(
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
        function Au() {
          return (
            (Au =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Au.apply(this, arguments)
          );
        }
        const du = ({ children: u, tooltipArgs: e, className: t }) => {
            if (!e) return u;
            const n = o().createElement("div", { className: t }, u);
            if (e.header || e.body) return o().createElement(K, e, n);
            const r = e.contentId,
              a = e.args,
              i = null == a ? void 0 : a.contentId;
            return r || i
              ? o().createElement(z, Au({}, e, { contentId: r || i }), n)
              : o().createElement(Eu, e, n);
          },
          _u = {
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
        let mu, Fu;
        (!(function (u) {
          ((u.main = "main"),
            (u.primary = "primary"),
            (u.primaryGreen = "primaryGreen"),
            (u.primaryRed = "primaryRed"),
            (u.secondary = "secondary"),
            (u.ghost = "ghost"));
        })(mu || (mu = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(Fu || (Fu = {})));
        const Du = ({
          children: u,
          size: e,
          isFocused: t,
          type: n,
          disabled: r,
          mixClass: i,
          soundHover: s,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: E,
          onMouseDown: A,
          onMouseUp: d,
          onMouseLeave: _,
          onClick: m,
        }) => {
          const F = (0, a.useRef)(null),
            D = (0, a.useState)(t),
            B = D[0],
            C = D[1],
            g = (0, a.useState)(!1),
            h = g[0],
            p = g[1],
            v = (0, a.useState)(!1),
            b = v[0],
            w = v[1],
            x = (0, a.useCallback)(() => {
              r || (F.current && (F.current.focus(), C(!0)));
            }, [r]),
            S = (0, a.useCallback)(
              (u) => {
                B && null !== F.current && !F.current.contains(u.target) && C(!1);
              },
              [B],
            ),
            y = (0, a.useCallback)(
              (u) => {
                r || (m && m(u));
              },
              [r, m],
            ),
            M = (0, a.useCallback)(
              (u) => {
                r || (null !== s && Z(s), c && c(u), w(!0));
              },
              [r, s, c],
            ),
            L = (0, a.useCallback)(
              (u) => {
                E && E(u);
              },
              [E],
            ),
            T = (0, a.useCallback)(
              (u) => {
                r || (d && d(u), p(!1));
              },
              [r, d],
            ),
            O = (0, a.useCallback)(
              (u) => {
                r || (null !== l && Z(l), A && A(u), t && x(), p(!0));
              },
              [r, l, A, x, t],
            ),
            N = (0, a.useCallback)(
              (u) => {
                r || (_ && _(u), p(!1));
              },
              [r, _],
            ),
            P = f()(
              _u.base,
              _u[`base__${n}`],
              {
                [_u.base__disabled]: r,
                [_u[`base__${e}`]]: e,
                [_u.base__focus]: B,
                [_u.base__highlightActive]: h,
                [_u.base__firstHover]: b,
              },
              i,
            ),
            H = f()(_u.state, _u.state__default);
          return (
            (0, a.useEffect)(
              () => (
                document.addEventListener("mousedown", S),
                () => {
                  document.removeEventListener("mousedown", S);
                }
              ),
              [S],
            ),
            (0, a.useEffect)(() => {
              C(t);
            }, [t]),
            o().createElement(
              "div",
              {
                ref: F,
                className: P,
                onMouseEnter: M,
                onMouseMove: L,
                onMouseUp: T,
                onMouseDown: O,
                onMouseLeave: N,
                onClick: y,
              },
              n !== mu.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: _u.back }),
                  o().createElement("span", { className: _u.texture }),
                ),
              o().createElement(
                "span",
                { className: H },
                o().createElement("span", { className: _u.stateDisabled }),
                o().createElement("span", { className: _u.stateHighlightHover }),
                o().createElement("span", { className: _u.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: _u.content, lang: R.strings.settings.LANGUAGE_CODE() },
                u,
              ),
            )
          );
        };
        Du.defaultProps = {
          type: mu.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Bu = (0, a.memo)(Du),
          Cu = {
            base: "Counter_base_9e",
            show: "Counter_show_be",
            base__big: "Counter_base__big_19",
            base__small: "Counter_base__small_3b",
            base__empty: "Counter_base__empty_98",
            base__animated: "Counter_base__animated_40",
            base__hidden: "Counter_base__hidden_56",
            hide: "Counter_hide_b6",
            bg: "Counter_bg_74",
            value: "Counter_value_3e",
            value__text: "Counter_value__text_d6",
            base__pattern: "Counter_base__pattern_71",
            plus: "Counter_plus_15",
            pattern: "Counter_pattern_83",
          },
          gu = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function hu() {
          return (
            (hu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            hu.apply(this, arguments)
          );
        }
        const fu = (u) => {
          let e = u.size,
            t = u.value,
            n = u.isEmpty,
            r = u.fadeInAnimation,
            a = u.hide,
            i = u.maximumNumber,
            s = u.className,
            l = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                r = {},
                a = Object.keys(u);
              for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
              return r;
            })(u, gu);
          const c = n ? null : t,
            E = "string" == typeof c;
          if ((c && !E && c < 0) || 0 === c) return null;
          const A = c && !E && c > i,
            d = f()(
              Cu.base,
              Cu[`base__${e}`],
              r && Cu.base__animated,
              a && Cu.base__hidden,
              !c && Cu.base__pattern,
              n && Cu.base__empty,
              s,
            );
          return o().createElement(
            "div",
            hu({ className: d }, l),
            o().createElement("div", { className: Cu.bg }),
            o().createElement("div", { className: Cu.pattern }),
            o().createElement(
              "div",
              { className: f()(Cu.value, E && Cu.value__text) },
              A ? i : c,
              A && o().createElement("span", { className: Cu.plus }, "+"),
            ),
          );
        };
        fu.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const pu = "ToggleButton_base_09",
          vu = "ToggleButton_overlay_76",
          bu = "ToggleButton_base__active_05",
          wu = "ToggleButton_button_14",
          xu = "ToggleButton_indicator_c2",
          Su = "ToggleButton_counter_86",
          yu = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function Mu() {
          return (
            (Mu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Mu.apply(this, arguments)
          );
        }
        const Lu = o().memo(function (u) {
            let e = u.isActive,
              t = u.counter,
              n = u.className,
              r = u.children,
              a = u.type,
              i = void 0 === a ? mu.secondary : a,
              s = u.size,
              l = void 0 === s ? Fu.small : s,
              c = u.hasIndicator,
              E = void 0 === c || c,
              A = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(u);
                for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                return r;
              })(u, yu);
            return o().createElement(
              "div",
              { className: f()(pu, n, e && bu) },
              o().createElement(Bu, Mu({ type: i, size: l, mixClass: wu }, A), r),
              o().createElement("div", { className: vu }),
              E && o().createElement("div", { className: xu }),
              Boolean(t) &&
                o().createElement(
                  "div",
                  { className: Su },
                  o().createElement(fu, { value: t, size: "small" }),
                ),
            );
          }),
          Tu = "FilterTitle_base_a7",
          Ru = "FilterTitle_label_05",
          Ou = "FilterTitle_discount_42",
          Nu = "FilterTitle_discountIcon_30",
          Pu = ({ label: u, hasDiscount: e, className: t }) =>
            o().createElement(
              "div",
              { className: f()(Tu, t) },
              o().createElement("div", { className: Ru }, u),
              e &&
                o().createElement(
                  "div",
                  { className: Ou },
                  o().createElement("div", { className: Nu }),
                ),
            );
        let Hu, Iu;
        function ku(u) {
          return u.replace(/-/g, "_");
        }
        (!(function (u) {
          ((u.Default = "default"),
            (u.Nation = "nation"),
            (u.Location = "location"),
            (u.TankmanRole = "tankmanRole"),
            (u.TankmanKind = "tankmanKind"),
            (u.VehicleGrade = "vehicleGrade"),
            (u.VehicleTier = "vehicleTier"),
            (u.VehicleType = "vehicleType"),
            (u.PersonalDataType = "personalDataType"),
            (u.VehicleCD = "vehicle"));
        })(Hu || (Hu = {})),
          (function (u) {
            ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
          })(Iu || (Iu = {})));
        const Wu = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          Gu = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          Uu = (u, e, t = Iu.left) => u.split(e).reduce(t === Iu.left ? Wu : Gu, []),
          ju = (() => {
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
            return (e) =>
              e
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(u);
          })(),
          zu = ["zh_cn", "zh_sg", "zh_tw"],
          Vu = (u, e = Iu.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return zu.includes(t)
              ? ju(u)
              : ((u, e = Iu.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = u.replace(/&nbsp;/g, " ");
                  return (Uu(r, /( )/, e).forEach((u) => (t = t.concat(Uu(u, n, Iu.left)))), t);
                })(u, e);
          },
          $u = "ToggleIcon_base_59",
          Xu = "ToggleIcon_base__small_3e",
          Ku = "ToggleIcon_icon_e7",
          Yu = o().memo(function ({ icon: u, isSmall: e = !1, classNames: t }) {
            return o().createElement(
              "div",
              { className: f()($u, e && Xu) },
              o().createElement("div", {
                className: f()(Ku, null == t ? void 0 : t.icon),
                style: { backgroundImage: `url(${u})` },
              }),
            );
          }),
          qu = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          Zu = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Qu = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          Ju = (u) =>
            Qu
              ? `${u}`
              : (function (u) {
                  let e = "";
                  for (let t = Zu.length - 1; t >= 0; t--)
                    for (; u >= Zu[t];) ((e += qu[t]), (u -= Zu[t]));
                  return e;
                })(u),
          ue = "VehicleTier_base_9c",
          ee = "VehicleTier_base__small_fc",
          te = ({ level: u, isSmall: e = !1 }) =>
            o().createElement("div", { className: f()(ue, e && ee) }, Ju(u)),
          ne = {
            icon__vehicleType: "ToggleButtonIcon_icon__vehicleType_83",
            icon__nation: "ToggleButtonIcon_icon__nation_c1",
            icon__vehicleGradePrimary: "ToggleButtonIcon_icon__vehicleGradePrimary_d6",
            icon__tankmanRole: "ToggleButtonIcon_icon__tankmanRole_4b",
            icon__selected: "ToggleButtonIcon_icon__selected_ca",
            icon__tankmanKind: "ToggleButtonIcon_icon__tankmanKind_5e",
            icon__vehicleGradeElite: "ToggleButtonIcon_icon__vehicleGradeElite_26",
            icon__locationRecruit: "ToggleButtonIcon_icon__locationRecruit_3b",
            icon__locationTankman: "ToggleButtonIcon_icon__locationTankman_f6",
            icon__locationUnique: "ToggleButtonIcon_icon__locationUnique_cb",
            icon__personalDataType: "ToggleButtonIcon_icon__personalDataType_a8",
            icon__tankmanKindDismissed: "ToggleButtonIcon_icon__tankmanKindDismissed_86",
            icon__vehicleGradePremium: "ToggleButtonIcon_icon__vehicleGradePremium_11",
          },
          re = ({ id: u, icon: e, type: t, isSmall: n = !0, isSelected: r = !1 }) => {
            return t === Hu.VehicleTier
              ? o().createElement(te, { isSmall: n, level: Number(u) })
              : o().createElement(Yu, {
                  icon: e,
                  isSmall: n,
                  classNames: {
                    icon: f()(
                      ne[`icon__${t}`],
                      ne[`icon__${t}${((a = u), a[0].toUpperCase() + a.slice(1))}`],
                      r && ne.icon__selected,
                    ),
                  },
                });
            var a;
          },
          ae = {
            base: "FilterToggleGroup_base_69",
            title: "FilterToggleGroup_title_65",
            content: "FilterToggleGroup_content_80",
            toggle: "FilterToggleGroup_toggle_d4",
            base__inPopup: "FilterToggleGroup_base__inPopup_11",
          };
        function oe() {
          return (
            (oe =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            oe.apply(this, arguments)
          );
        }
        let ie;
        !(function (u) {
          ((u.Default = "default"), (u.InPopup = "inPopup"));
        })(ie || (ie = {}));
        const se = ({ header: u, body: e, contentId: t, targetId: n }) =>
            t
              ? { contentId: t, targetId: n }
              : e || u
                ? { header: null != u ? u : void 0, body: null != e ? e : void 0 }
                : void 0,
          le = ({
            id: u,
            type: e,
            label: t,
            hasDiscount: n,
            filters: r,
            onClick: a,
            className: i,
            toggleProps: s,
            theme: l = ie.Default,
          }) => {
            const c = l === ie.InPopup;
            return o().createElement(
              "div",
              { className: f()(ae.base, ae[`base__${l}`], i) },
              c && o().createElement(Pu, { className: ae.title, label: t, hasDiscount: n }),
              o().createElement(
                "div",
                { className: ae.content },
                iu(r, ({ id: t, isSelected: n, tooltip: r, icon: i, counter: l }) =>
                  o().createElement(
                    du,
                    { key: t, tooltipArgs: se(r), className: ae.toggle },
                    o().createElement(
                      Lu,
                      oe({}, s, {
                        className: f()(ae.toggle, null == s ? void 0 : s.className),
                        isActive: n,
                        onClick: () => (null == a ? void 0 : a(u, t)),
                        counter: l,
                      }),
                      o().createElement(re, { id: t, icon: i, type: e, isSmall: c, isSelected: n }),
                    ),
                  ),
                ),
              ),
            );
          };
        function ce() {
          return !1;
        }
        console.log;
        var Ee = t(9174);
        function Ae(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return de(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return de(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var n = 0;
            return function () {
              return n >= u.length ? { done: !0 } : { done: !1, value: u[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function de(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, n = new Array(e); t < e; t++) n[t] = u[t];
          return n;
        }
        const _e = (u) => (0 === u ? window : window.subViews.get(u));
        const me = ((u, e) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: n = "real", options: r, children: i, mocks: l }) {
                const c = (0, a.useRef)([]),
                  E = (t, n, r) => {
                    var a;
                    const o = (function ({
                        initializer: u = !0,
                        rootId: e = 0,
                        getRoot: t = _e,
                        context: n = "model",
                      } = {}) {
                        const r = new Map();
                        function a(u, e = 0) {
                          viewEnv.removeDataChangedCallback(u, e)
                            ? r.delete(u)
                            : console.error("Can't remove callback by id:", u);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (u, e, t) => {
                            t.forEach((e) => {
                              const t = r.get(e);
                              void 0 !== t && t(u);
                            });
                          });
                        });
                        const o = (u) => {
                          const r = t(e),
                            a = n.split(".").reduce((u, e) => u[e], r);
                          return "string" != typeof u || 0 === u.length
                            ? a
                            : u.split(".").reduce((u, e) => {
                                const t = u[e];
                                return "function" == typeof t ? t.bind(u) : t;
                              }, a);
                        };
                        return {
                          subscribe: (t, a) => {
                            const i = "string" == typeof a ? `${n}.${a}` : n,
                              l = s.O.view.addModelObserver(i, e, !0);
                            return (r.set(l, t), u && t(o(a)), l);
                          },
                          readByPath: o,
                          createCallback: (u, e) => {
                            const t = o(e);
                            return (...e) => {
                              t(u(...e));
                            };
                          },
                          createCallbackNoArgs: (u) => {
                            const e = o(u);
                            return () => {
                              e();
                            };
                          },
                          dispose: function () {
                            for (var u, t = Ae(r.keys()); !(u = t()).done;) a(u.value, e);
                          },
                          unsubscribe: a,
                        };
                      })(n),
                      i =
                        "real" === t
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (a = null == r ? void 0 : r.getter) ? a : () => {},
                            }),
                      l = (u) =>
                        "mocks" === t ? (null == r ? void 0 : r.getter(u)) : i.readByPath(u),
                      E = (u) => c.current.push(u),
                      A = u({
                        mode: t,
                        readByPath: l,
                        externalModel: i,
                        observableModel: {
                          array: (u, e) => {
                            const n = null != e ? e : l(u),
                              r = Ee.LO.box(n, { equals: ce });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, Ee.aD)((u) => r.set(u)),
                                  u,
                                ),
                              r
                            );
                          },
                          object: (u, e) => {
                            const n = null != e ? e : l(u),
                              r = Ee.LO.box(n, { equals: ce });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, Ee.aD)((u) => r.set(u)),
                                  u,
                                ),
                              r
                            );
                          },
                          primitives: (u, e) => {
                            const n = l(e);
                            if (Array.isArray(u)) {
                              const r = u.reduce((u, e) => ((u[e] = Ee.LO.box(n[e], {})), u), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, Ee.aD)((e) => {
                                      u.forEach((u) => {
                                        r[u].set(e[u]);
                                      });
                                    }),
                                    e,
                                  ),
                                r
                              );
                            }
                            {
                              const r = u,
                                a = Object.entries(r),
                                o = a.reduce((u, [e, t]) => ((u[t] = Ee.LO.box(n[e], {})), u), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, Ee.aD)((u) => {
                                      a.forEach(([e, t]) => {
                                        o[t].set(u[e]);
                                      });
                                    }),
                                    e,
                                  ),
                                o
                              );
                            }
                          },
                        },
                        cleanup: E,
                      }),
                      d = { mode: t, model: A, externalModel: i, cleanup: E };
                    return {
                      model: A,
                      controls: "mocks" === t && r ? r.controls(d) : e(d),
                      externalModel: i,
                      mode: t,
                    };
                  },
                  A = (0, a.useRef)(!1),
                  d = (0, a.useState)(n),
                  _ = d[0],
                  m = d[1],
                  F = (0, a.useState)(() => E(n, r, l)),
                  D = F[0],
                  B = F[1];
                return (
                  (0, a.useEffect)(() => {
                    A.current ? B(E(_, r, l)) : (A.current = !0);
                  }, [l, _, r]),
                  (0, a.useEffect)(() => {
                    m(n);
                  }, [n]),
                  (0, a.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), c.current.forEach((u) => u()));
                    },
                    [D],
                  ),
                  o().createElement(t.Provider, { value: D }, i)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: u }) =>
              Object.assign(
                {},
                u.primitives([
                  "title",
                  "hasVehicleFilter",
                  "vehicleSortColumn",
                  "isVehicleSortAscending",
                  "canResetFilter",
                ]),
                { filterGroups: u.array("filterGroups"), vehicles: u.array("vehicles") },
              ),
            ({ externalModel: u }) => ({
              sortVehiclesByColumn: u.createCallback(
                (u) => ({ column: u }),
                "onSortVehiclesByColumn",
              ),
              updateFilter: u.createCallback(
                (u, e) => ({ groupID: u, toggleID: e }),
                "onUpdateFilter",
              ),
              selectVehicle: u.createCallback((u) => ({ vehicleCD: u }), "onSelectVehicle"),
              resetFilter: u.createCallbackNoArgs("onResetFilter"),
            }),
          ),
          Fe = me[0],
          De = me[1];
        var Be = t(9887),
          Ce = t.n(Be);
        const ge = ["xl", "lg", "md", "sm", "xs"],
          he = (u) => u.includes("_") && ((u) => ge.includes(u))(u.split("_").at(-1)),
          fe = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          pe = (u, e) =>
            Object.keys(u).reduce((t, n) => {
              if (n in t) return t;
              if (he(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const a = fe.indexOf(e),
                  o = (-1 !== a ? ge.slice(a) : [])
                    .map((u) => r + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  i = o ? u[o] : void 0;
                return ((t[r] = void 0 !== i ? i : u[r]), t);
              }
              const r = u[n];
              return (
                void 0 === r ||
                  ((u, e) => ge.some((t) => void 0 !== e[`${u}_${t}`]))(n, u) ||
                  (t[n] = r),
                t
              );
            }, {}),
          ve = (u, e = pe) => {
            const t = (
              (u, e = pe) =>
              (t) => {
                const n = S().mediaSize,
                  r = (0, a.useMemo)(() => e(t, n), [t, n]);
                return o().createElement(u, r);
              }
            )(u, e);
            return o().memo((e) =>
              Object.keys(e).some((u) => he(u) && void 0 !== e[u])
                ? o().createElement(t, e)
                : o().createElement(u, e),
            );
          },
          be = {
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
          we = [
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
        function xe() {
          return (
            (xe =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            xe.apply(this, arguments)
          );
        }
        Object.keys(Ce());
        const Se = {
            XL: { mt: be.mt__XL, mr: be.mr__XL, mb: be.mb__XL, ml: be.ml__XL },
            LG: { mt: be.mt__LG, mr: be.mr__LG, mb: be.mb__LG, ml: be.ml__LG },
            MDp: { mt: be.mt__MDp, mr: be.mr__MDp, mb: be.mb__MDp, ml: be.ml__MDp },
            MD: { mt: be.mt__MD, mr: be.mr__MD, mb: be.mb__MD, ml: be.ml__MD },
            SMp: { mt: be.mt__SMp, mr: be.mr__SMp, mb: be.mb__SMp, ml: be.ml__SMp },
            SM: { mt: be.mt__SM, mr: be.mr__SM, mb: be.mb__SM, ml: be.ml__SM },
            XS: { mt: be.mt__XS, mr: be.mr__XS, mb: be.mb__XS, ml: be.ml__XS },
          },
          ye = (Object.keys(Se), ["mt", "mr", "mb", "ml"]),
          Me = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Le = ve((u) => {
            let e = u.className,
              t = u.width,
              n = u.height,
              r = u.m,
              i = u.mt,
              s = void 0 === i ? r : i,
              l = u.mr,
              c = void 0 === l ? r : l,
              E = u.mb,
              A = void 0 === E ? r : E,
              d = u.ml,
              _ = void 0 === d ? r : d,
              m = u.column,
              F = u.row,
              D = u.flexDirection,
              B = void 0 === D ? (m ? "column" : F && "row") || void 0 : D,
              C = u.flexStart,
              g = u.center,
              h = u.flexEnd,
              p = u.spaceBetween,
              v = u.spaceAround,
              b = u.justifyContent,
              w =
                void 0 === b
                  ? (C ? "flex-start" : g && "center") ||
                    (h && "flex-end") ||
                    (p && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : b,
              x = u.alignItems,
              S =
                void 0 === x
                  ? (C ? "flex-start" : g && "center") || (h && "flex-end") || void 0
                  : x,
              y = u.alignSelf,
              M = u.wrap,
              L = u.flexWrap,
              T = void 0 === L ? (M ? "wrap" : void 0) : L,
              R = u.grow,
              O = u.shrink,
              N = u.flex,
              P = void 0 === N ? (R || O ? `${R ? 1 : 0} ${O ? 1 : 0} auto` : void 0) : N,
              H = u.style,
              I = u.children,
              k = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(u);
                for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                return r;
              })(u, we);
            const W = (0, a.useMemo)(() => {
                const u = { mt: s, mr: c, mb: A, ml: _ },
                  e = ((u) =>
                    ye.reduce((e, t) => {
                      const n = u[t];
                      return n && "number" != typeof n ? e.concat(Se[!0 === n ? "MD" : n][t]) : e;
                    }, []))(u),
                  r = ((u) =>
                    ye.reduce((e, t) => {
                      const n = u[t];
                      return ("number" == typeof n && (e[Me[t]] = n + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, H, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: P,
                    alignSelf: y,
                    display: B || S ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: T,
                    justifyContent: w,
                    alignItems: S,
                  }),
                  computedClassNames: e,
                };
              }, [t, n, s, c, A, _, H, P, y, B, T, w, S]),
              G = W.computedStyle,
              U = W.computedClassNames;
            return o().createElement(
              "div",
              xe({ className: f()(be.base, ...U, e), style: G }, k),
              I,
            );
          }),
          Te = "FormatText_base_d0",
          Re = ({ binding: u, text: e = "", classMix: t, alignment: n = Iu.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  a.Fragment,
                  null,
                  e.split("\n").map((e, r) =>
                    o().createElement(
                      "div",
                      { className: f()(Te, t), key: `${e}-${r}` },
                      ((u, e, t) =>
                        u
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((u) => (t && u in t ? t[u] : Vu(u, e))))(e, n, u).map((u, e) =>
                        o().createElement(a.Fragment, { key: `${e}-${u}` }, u),
                      ),
                    ),
                  ),
                );
        var Oe = t(3532),
          Ne = t.n(Oe);
        const Pe = {
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
          He = [
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
        function Ie() {
          return (
            (Ie =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Ie.apply(this, arguments)
          );
        }
        Object.keys(Ce());
        const ke = Object.keys(Ne()),
          We = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Ge = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Ue = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          je = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          ze =
            (Object.keys(je),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": We,
              "heading-H36": We,
              "heading-H28": Ge,
              "heading-H24": Ge,
              "heading-H24R": Ge,
              "heading-H22": Ge,
              "heading-H20R": Ge,
              "heading-H18": Ge,
              "heading-H15": Ue,
              "heading-H14": Ue,
              "paragraph-P24": Ge,
              "paragraph-P18": Ge,
              "paragraph-P16": Ge,
              "paragraph-P14": Ue,
              "paragraph-P12": Ue,
              "paragraph-P10": Ue,
            }),
          Ve =
            (Object.keys(ze),
            (u) =>
              u
                ? ((u) => ke.includes(u))(u)
                  ? { colorClassName: Pe[u] }
                  : { colorStyle: { color: u } }
                : {}),
          $e = ve((u) => {
            let e = u.text,
              t = u.variant,
              n = u.className,
              r = u.color,
              i = u.m,
              s = u.mt,
              l = void 0 === s ? i : s,
              c = u.mr,
              E = void 0 === c ? i : c,
              A = u.mb,
              d = void 0 === A ? i : A,
              _ = u.ml,
              m = void 0 === _ ? i : _,
              F = u.style,
              D = u.format,
              B = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(u);
                for (n = 0; n < a.length; n++) ((t = a[n]), e.indexOf(t) >= 0 || (r[t] = u[t]));
                return r;
              })(u, He);
            const C = (0, a.useMemo)(() => {
                const u = Ve(r),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, n), colorClassName: e };
              }, [F, r]),
              g = C.computedStyle,
              h = C.colorClassName;
            return o().createElement(
              Le,
              Ie(
                {
                  className: f()(Pe.base, t && Pe[t], h, n),
                  style: g,
                  mt: !0 === l ? ze[t || "paragraph-P16"].mt : l,
                  mr: !0 === E ? ze[t || "paragraph-P16"].mr : E,
                  mb: !0 === d ? ze[t || "paragraph-P16"].mb : d,
                  ml: !0 === m ? ze[t || "paragraph-P16"].ml : m,
                },
                B,
              ),
              void 0 !== D ? o().createElement(Re, Ie({}, D, { text: e })) : e,
            );
          });
        R.strings.common.percentValue();
        let Xe;
        !(function (u) {
          ((u.Objective = "objective"), (u.Possessive = "possessive"));
        })(Xe || (Xe = {}));
        const Ke = {
          header: R.strings.crew.filterPanel.counter.reset.header(),
          body: R.strings.crew.filterPanel.counter.reset.body(),
        };
        (R.strings.crew.filterPanel.counterMultySelect.reset.header(),
          R.strings.crew.filterPanel.counterMultySelect.reset.body());
        let Ye;
        !(function (u) {
          ((u.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (u.SHOP_INFO = "shop_info"),
            (u.RUDY = "rudy"));
        })(Ye || (Ye = {}));
        const qe = "ResetButton_base_28",
          Ze = R.strings.crew.filter,
          Qe = (0, su.Pi)(() => {
            const u = De(),
              e = u.model,
              t = u.controls;
            return o().createElement(
              K,
              Ke,
              o().createElement(
                Bu,
                {
                  onClick: t.resetFilter,
                  type: mu.secondary,
                  size: Fu.small,
                  disabled: !e.canResetFilter.get(),
                  mixClass: qe,
                },
                o().createElement($e, { text: Ze.reset() }),
              ),
            );
          }),
          Je = "Footer_base_ce",
          ut = () => o().createElement("div", { className: Je }, o().createElement(Qe, null)),
          et = (u, e, t) => (t < u ? u : t > e ? e : t),
          tt = [];
        function nt(u) {
          const e = (0, a.useRef)(u);
          return (
            (0, a.useLayoutEffect)(() => {
              e.current = u;
            }),
            (0, a.useCallback)((...u) => (0, e.current)(...u), tt)
          );
        }
        function rt(u, e, t = []) {
          const n = (0, a.useRef)(0),
            r = (0, a.useCallback)(() => window.clearInterval(n.current), t || []);
          (0, a.useEffect)(() => r, [r]);
          const o = (null != t ? t : []).concat([e]);
          return [
            (0, a.useCallback)((t) => {
              ((n.current = window.setInterval(() => u(t, !0), e)), u(t, !1));
            }, o),
            r,
          ];
        }
        function at(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return ot(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return ot(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var n = 0;
            return function () {
              return n >= u.length ? { done: !0 } : { done: !1, value: u[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function ot(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, n = new Array(e); t < e; t++) n[t] = u[t];
          return n;
        }
        const it = () => {
          const u = (0, a.useMemo)(() => ({}), []),
            e = (e) => (u[e] || (u[e] = new Map()), u[e]),
            t = (u, t) => {
              e(u).set(t, t);
            },
            n = (u, t) => {
              e(u).delete(t);
            },
            r = (u, ...t) => {
              for (var n, r = at(e(u).values()); !(n = r()).done;) {
                (0, n.value)(...t);
              }
            };
          return (0, a.useMemo)(() => ({ on: t, off: n, trigger: r }), []);
        };
        function st(u, e, t) {
          const n = (0, a.useMemo)(
            () =>
              (function (u, e, t, n) {
                let r,
                  a = !1,
                  o = 0;
                function i() {
                  r && clearTimeout(r);
                }
                function s(...s) {
                  const l = this,
                    c = Date.now() - o;
                  function E() {
                    ((o = Date.now()), t.apply(l, s));
                  }
                  a ||
                    (n && !r && E(),
                    i(),
                    void 0 === n && c > u
                      ? E()
                      : !0 !== e &&
                        (r = setTimeout(
                          n
                            ? function () {
                                r = void 0;
                              }
                            : E,
                          void 0 === n ? u - c : u,
                        )));
                }
                return (
                  "boolean" != typeof e && ((n = t), (t = e), (e = void 0)),
                  (s.cancel = function () {
                    (i(), (a = !0));
                  }),
                  s
                );
              })(t, u),
            e,
          );
          return ((0, a.useEffect)(() => n.cancel, [n]), n);
        }
        var lt = t(7030);
        let ct;
        !(function (u) {
          ((u[(u.Next = -1)] = "Next"), (u[(u.Prev = 1)] = "Prev"));
        })(ct || (ct = {}));
        const Et = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          At = ({
            getContainerSize: u,
            getBounds: e,
            setScrollPosition: t,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const i = (u, t) => {
              const n = e(u),
                r = n[0],
                a = n[1];
              return et(r, a, t);
            };
            return (l = {}) => {
              const c = l.settings,
                E = void 0 === c ? Et : c,
                A = (0, a.useRef)(null),
                d = (0, a.useRef)(null),
                _ = it(),
                m = st(
                  () => {
                    s.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                F = (0, lt.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (u) => {
                    const e = A.current;
                    e && (t(e, u), _.trigger("change", u), o && m());
                  },
                  onRest: (u) => _.trigger("rest", u),
                  onStart: (u) => _.trigger("start", u),
                  onPause: (u) => _.trigger("pause", u),
                })),
                D = F[0],
                B = F[1],
                C = (0, a.useCallback)(
                  (u, e, t) => {
                    var n;
                    const r = D.scrollPosition.get(),
                      a = (null != (n = D.scrollPosition.goal) ? n : 0) - r;
                    return i(u, e * t + a + r);
                  },
                  [D.scrollPosition],
                ),
                g = (0, a.useCallback)(
                  (u, { immediate: e = !1, reset: t = !0 } = {}) => {
                    const n = A.current;
                    n &&
                      B.start({
                        scrollPosition: i(n, u),
                        immediate: e,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: i(n, D.scrollPosition.get()) },
                      });
                  },
                  [B, E.animationConfig, D.scrollPosition],
                ),
                h = (0, a.useCallback)(
                  (u) => {
                    const e = A.current,
                      t = d.current;
                    if (!e || !t) return;
                    const n = ((u, e) => {
                        switch (e.type) {
                          case "proportional":
                            return r(u) / e.factor;
                          case "fixed":
                            return e.value;
                        }
                      })(t, E.step),
                      a = C(e, u, n);
                    g(a);
                  },
                  [g, C, E.step],
                ),
                f = (0, a.useCallback)(
                  (u) => {
                    (0 !== u.deltaY && h(n(u)),
                      A.current && _.trigger("mouseWheel", u, D.scrollPosition, e(A.current)));
                  },
                  [D.scrollPosition, h, _],
                ),
                p = ((u, e = []) => {
                  const t = (0, a.useRef)(),
                    n = (0, a.useCallback)((...e) => {
                      (t.current && t.current(), (t.current = u(...e)));
                    }, e);
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
                    Y(() => {
                      const u = A.current;
                      u &&
                        (g(i(u, D.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [g, D.scrollPosition.goal],
                ),
                v = nt(() => {
                  const u = A.current;
                  if (!u) return;
                  const e = i(u, D.scrollPosition.goal);
                  (e !== D.scrollPosition.goal && g(e, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, a.useEffect)(
                () => (
                  window.addEventListener("resize", p),
                  () => {
                    window.removeEventListener("resize", p);
                  }
                ),
                [p],
              );
              const b = (0, a.useCallback)((u) => _.trigger("isThumbDraggingChanged", u), [_]);
              return (0, a.useMemo)(
                () => ({
                  getWrapperSize: () => (d.current ? r(d.current) : void 0),
                  getContainerSize: () => (A.current ? u(A.current) : void 0),
                  getBounds: () =>
                    A.current
                      ? e(A.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: f,
                  applyScroll: g,
                  applyStepTo: h,
                  contentRef: A,
                  wrapperRef: d,
                  scrollPosition: B,
                  animationScroll: D,
                  recalculateContent: v,
                  handleIsThumbDragging: b,
                  events: { on: _.on, off: _.off },
                }),
                [D.scrollPosition, g, h, b, _.off, _.on, v, f, B, E.step.clampedArrowStepTimeout],
              );
            };
          },
          dt = At({
            getBounds: (u) => {
              var e, t;
              return [
                0,
                u.offsetWidth -
                  (null != (e = null == (t = u.parentElement) ? void 0 : t.offsetWidth) ? e : 0),
              ];
            },
            getContainerSize: (u) => u.offsetWidth,
            getWrapperSize: (u) => u.offsetWidth,
            setScrollPosition: (u, e) => {
              u.style.transform = `translateX(-${e.value.scrollPosition}px)`;
            },
            getDirection: (u) => (u.deltaY > 1 ? ct.Next : ct.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          _t = "HorizontalBar_base_49",
          mt = "HorizontalBar_base__nonActive_82",
          Ft = "HorizontalBar_leftButton_5f",
          Dt = "HorizontalBar_rightButton_03",
          Bt = "HorizontalBar_track_0d",
          Ct = "HorizontalBar_thumb_fd",
          gt = "HorizontalBar_rail_32",
          ht = "disable",
          ft = { pending: !1, offset: 0 },
          pt = (u) => {
            var e;
            return 0.9 * (null != (e = u.getWrapperSize()) ? e : 0);
          },
          vt = () => {},
          bt = (u, e) => Math.max(20, u.offsetWidth * e),
          wt = (0, a.memo)(
            ({ api: u, classNames: e = {}, getStepByRailClick: t = pt, onDrag: n = vt }) => {
              const r = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                s = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = u.stepTimeout || 100,
                A = (0, a.useState)(ft),
                d = A[0],
                _ = A[1],
                m = (0, a.useCallback)(
                  (u) => {
                    (_(u),
                      c.current &&
                        n({ type: u.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                F = () => {
                  const e = l.current,
                    t = c.current,
                    n = u.getWrapperSize(),
                    r = u.getContainerSize();
                  if (!(n && e && t && r)) return;
                  const a = u.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / r),
                    E = et(0, 1, a / (r - n)),
                    A = (e.offsetWidth - bt(e, o)) * E;
                  ((t.style.transform = `translateX(${0 | A}px)`),
                    ((u) => {
                      if (i.current && s.current && l.current && c.current) {
                        if (0 === u)
                          return (i.current.classList.add(ht), void s.current.classList.remove(ht));
                        if (
                          ((e = l.current),
                          (t = c.current),
                          u - (e.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(ht), void s.current.classList.add(ht));
                        var e, t;
                        (i.current.classList.remove(ht), s.current.classList.remove(ht));
                      }
                    })(A));
                },
                D = nt(() => {
                  ((() => {
                    const e = c.current,
                      t = l.current,
                      n = u.getWrapperSize(),
                      a = u.getContainerSize();
                    if (!(a && e && n && t)) return;
                    const o = Math.min(1, n / a);
                    ((e.style.width = `${bt(t, o)}px`),
                      (e.style.display = "flex"),
                      r.current &&
                        (1 === o ? r.current.classList.add(mt) : r.current.classList.remove(mt)));
                  })(),
                    F());
                });
              ((0, a.useEffect)(() => Y(D)),
                (0, a.useEffect)(
                  () =>
                    Y(() => {
                      const e = () => {
                        F();
                      };
                      let t = vt;
                      const n = () => {
                        (t(), (t = Y(D)));
                      };
                      return (
                        u.events.on("recalculateContent", D),
                        u.events.on("rest", e),
                        u.events.on("change", e),
                        u.events.on("resizeHandled", n),
                        () => {
                          (t(),
                            u.events.off("recalculateContent", D),
                            u.events.off("rest", e),
                            u.events.off("change", e),
                            u.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [u],
                ),
                (0, a.useEffect)(() => {
                  if (!d.pending) return;
                  const e = (e) => {
                      var t;
                      const r = u.contentRef.current;
                      if (!r) return;
                      const a = l.current,
                        o = c.current;
                      if (!r || !a || !o) return;
                      const i = e.screenX - d.offset - a.getBoundingClientRect().x,
                        s = (i / a.offsetWidth) * (null != (t = u.getContainerSize()) ? t : 0);
                      (u.scrollPosition.start({
                        scrollPosition: u.clampPosition(r, s),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: u.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: o, thumbOffset: i, contentOffset: s }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", e), m(ft));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [u, d.offset, d.pending, n, m]));
              const B = rt((e) => u.applyStepTo(e), E, [u]),
                C = B[0],
                g = B[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", g, !0),
                  () => document.removeEventListener("mouseup", g, !0)
                ),
                [g],
              );
              const h = (u) => {
                u.target.classList.contains(ht) || Z("highlight");
              };
              return o().createElement(
                "div",
                { className: f()(_t, e.base), ref: r, onWheel: u.handleMouseWheel },
                o().createElement("div", {
                  className: f()(Ft, e.leftButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(ht) || 0 !== u.button || (Z("play"), C(ct.Next));
                  },
                  onMouseUp: g,
                  ref: i,
                  onMouseEnter: h,
                }),
                o().createElement(
                  "div",
                  {
                    className: f()(Bt, e.track),
                    onMouseDown: (e) => {
                      const n = c.current;
                      if (n && 0 === e.button)
                        if ((Z("play"), e.target === n))
                          m({ pending: !0, offset: e.screenX - n.getBoundingClientRect().x });
                        else {
                          ((e) => {
                            const n = c.current,
                              r = u.contentRef.current;
                            if (!n || !r) return;
                            const a = t(u);
                            u.applyScroll(u.animationScroll.scrollPosition.get() + a * e);
                          })(e.screenX > n.getBoundingClientRect().x ? ct.Prev : ct.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: h,
                  },
                  o().createElement("div", { ref: c, className: f()(Ct, e.thumb) }),
                  o().createElement("div", { className: f()(gt, e.rail) }),
                ),
                o().createElement("div", {
                  className: f()(Dt, e.rightButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(ht) || 0 !== u.button || (Z("play"), C(ct.Prev));
                  },
                  onMouseUp: g,
                  ref: s,
                  onMouseEnter: h,
                }),
              );
            },
          ),
          xt = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          St = ({
            children: u,
            api: e,
            className: t,
            barClassNames: n,
            areaClassName: r,
            classNames: i,
            scrollClassName: s,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const u = n || {};
                return Object.assign({}, u, { base: f()(xt.base, u.base) });
              }, [n]),
              A = (0, a.useMemo)(() => Object.assign({}, e, { handleMouseWheel: () => {} }), [e]);
            return o().createElement(
              "div",
              { className: f()(xt.defaultScroll, t), onWheel: e.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(xt.defaultScrollArea, r) },
                o().createElement(yt, { className: s, api: A, classNames: i }, u),
              ),
              o().createElement(wt, { getStepByRailClick: l, api: e, onDrag: c, classNames: E }),
            );
          },
          yt = ({ api: u, className: e, classNames: t, children: n, style: r }) => (
            (0, a.useEffect)(() => Y(u.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(xt.base, e), style: r },
              o().createElement(
                "div",
                {
                  className: f()(xt.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: u.handleMouseWheel,
                  ref: u.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: f()(xt.content, null == t ? void 0 : t.content), ref: u.contentRef },
                  n,
                ),
              ),
            )
          );
        ((yt.Bar = wt),
          (yt.Default = St),
          (yt.SeniorityAwards = ({ api: u, className: e, classNames: t, children: n }) => (
            (0, a.useEffect)(() => Y(u.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(xt.base, e) },
              o().createElement(
                "div",
                { className: f()(xt.wrapper, null == t ? void 0 : t.wrapper), ref: u.wrapperRef },
                o().createElement(
                  "div",
                  { className: f()(xt.content, null == t ? void 0 : t.content), ref: u.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Mt = At({
            getBounds: (u) => [0, u.scrollHeight - u.offsetHeight],
            getContainerSize: (u) => u.scrollHeight,
            getWrapperSize: (u) => u.offsetHeight,
            setScrollPosition: (u, e) => {
              u.scrollTop = e.value.scrollPosition;
            },
            getDirection: (u) => (u.deltaY > 1 ? ct.Next : ct.Prev),
          }),
          Lt = "VerticalBar_base_f3",
          Tt = "VerticalBar_base__nonActive_42",
          Rt = "VerticalBar_topButton_d7",
          Ot = "VerticalBar_bottomButton_06",
          Nt = "VerticalBar_track_df",
          Pt = "VerticalBar_thumb_32",
          Ht = "VerticalBar_rail_43",
          It = "disable",
          kt = () => {},
          Wt = { pending: !1, offset: 0 },
          Gt = (u) => {
            var e;
            return 0.9 * (null != (e = u.getWrapperSize()) ? e : 0);
          },
          Ut = (u, e) => {
            u.contentRef.current && e(u.contentRef.current);
          },
          jt = (u, e) => Math.max(20, u.offsetHeight * e),
          zt = (0, a.memo)(
            ({ api: u, classNames: e = {}, getStepByRailClick: t = Gt, onDrag: n = kt }) => {
              const r = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                s = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = u.stepTimeout || 100,
                A = (0, a.useState)(Wt),
                d = A[0],
                _ = A[1],
                m = (0, a.useCallback)(
                  (u) => {
                    (_(u),
                      c.current &&
                        n({ type: u.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                F = nt(() => {
                  const e = c.current,
                    t = l.current,
                    n = u.getWrapperSize(),
                    a = u.getContainerSize();
                  if (!(n && a && e && t)) return;
                  const o = Math.min(1, n / a);
                  return (
                    (e.style.height = `${jt(t, o)}px`),
                    e.classList.add(Pt),
                    r.current &&
                      (1 === o ? r.current.classList.add(Tt) : r.current.classList.remove(Tt)),
                    o
                  );
                }),
                D = nt(() => {
                  const e = l.current,
                    t = c.current,
                    n = u.getWrapperSize(),
                    r = u.getContainerSize();
                  if (!(n && e && t && r)) return;
                  const a = u.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / r),
                    E = et(0, 1, a / (r - n)),
                    A = (e.offsetHeight - jt(e, o)) * E;
                  ((t.style.transform = `translateY(${0 | A}px)`),
                    ((u) => {
                      if (i.current && s.current && l.current && c.current) {
                        if (0 === u)
                          return (i.current.classList.add(It), void s.current.classList.remove(It));
                        if (
                          ((e = l.current),
                          (t = c.current),
                          u - (e.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(It), void s.current.classList.add(It));
                        var e, t;
                        (i.current.classList.remove(It), s.current.classList.remove(It));
                      }
                    })(A));
                }),
                B = nt(() => {
                  Ut(u, () => {
                    (F(), D());
                  });
                });
              ((0, a.useEffect)(() => Y(B)),
                (0, a.useEffect)(() => {
                  const e = () => {
                    Ut(u, () => {
                      D();
                    });
                  };
                  let t = kt;
                  const n = () => {
                    (t(), (t = Y(B)));
                  };
                  return (
                    u.events.on("recalculateContent", B),
                    u.events.on("rest", e),
                    u.events.on("change", e),
                    u.events.on("resizeHandled", n),
                    () => {
                      (t(),
                        u.events.off("recalculateContent", B),
                        u.events.off("rest", e),
                        u.events.off("change", e),
                        u.events.off("resizeHandled", n));
                    }
                  );
                }, [u]),
                (0, a.useEffect)(() => {
                  if (!d.pending) return;
                  const e = (e) => {
                      Ut(u, (t) => {
                        const r = l.current,
                          a = c.current,
                          o = u.getContainerSize();
                        if (!r || !a || !o) return;
                        const i = e.screenY - d.offset - r.getBoundingClientRect().y,
                          s = (i / r.offsetHeight) * o;
                        (u.scrollPosition.start({
                          scrollPosition: u.clampPosition(t, s),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: a, thumbOffset: i, contentOffset: s }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", e),
                        u.handleIsThumbDragging(!1),
                        m(Wt));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [u, d.offset, d.pending, n, m]));
              const C = rt((e) => u.applyStepTo(e), E, [u]),
                g = C[0],
                h = C[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const p = (u) => {
                u.target.classList.contains(It) || Z("highlight");
              };
              return o().createElement(
                "div",
                { className: f()(Lt, e.base), ref: r, onWheel: u.handleMouseWheel },
                o().createElement("div", {
                  className: f()(Rt, e.topButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(It) || 0 !== u.button || (Z("play"), g(ct.Next));
                  },
                  ref: i,
                  onMouseEnter: p,
                }),
                o().createElement(
                  "div",
                  {
                    className: f()(Nt, e.track),
                    onMouseDown: (e) => {
                      const n = c.current;
                      if (n && 0 === e.button)
                        if ((Z("play"), e.target === n))
                          (u.handleIsThumbDragging(!0),
                            m({ pending: !0, offset: e.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((e) => {
                            c.current &&
                              Ut(u, (n) => {
                                if (!n) return;
                                const r = t(u),
                                  a = u.clampPosition(n, n.scrollTop + r * e);
                                u.applyScroll(a);
                              });
                          })(e.screenY > n.getBoundingClientRect().y ? ct.Prev : ct.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: p,
                  },
                  o().createElement("div", { ref: c, className: e.thumb }),
                  o().createElement("div", { className: f()(Ht, e.rail) }),
                ),
                o().createElement("div", {
                  className: f()(Ot, e.bottomButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(It) || 0 !== u.button || (Z("play"), g(ct.Prev));
                  },
                  onMouseUp: h,
                  ref: s,
                  onMouseEnter: p,
                }),
              );
            },
          ),
          Vt = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          $t = ({
            children: u,
            api: e,
            className: t,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: i,
            scrollClassNames: s,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const u = n || {};
                return Object.assign({}, u, { base: f()(Vt.base, u.base) });
              }, [n]),
              A = (0, a.useMemo)(() => Object.assign({}, e, { handleMouseWheel: () => {} }), [e]);
            return o().createElement(
              "div",
              { className: f()(Vt.defaultScroll, t), onWheel: e.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(Vt.area, r) },
                o().createElement(Xt, { className: i, classNames: s, api: A }, u),
              ),
              o().createElement(zt, { getStepByRailClick: l, api: e, onDrag: c, classNames: E }),
            );
          },
          Xt = ({ className: u, classNames: e, children: t, api: n }) => (
            (0, a.useEffect)(() => Y(n.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(Vt.base, u), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(Vt.content, null == e ? void 0 : e.content), ref: n.contentRef },
                t,
              ),
            )
          );
        Xt.Default = $t;
        const Kt = { Vertical: r, Horizontal: n },
          Yt = ({
            startRowIndex: u,
            cellHeight: e,
            paddingTop: t,
            paddingBottom: n,
            amount: r,
            itemsAmountPerRow: a,
            visibleRowsAmount: o,
            numOdfHeadingsBefore: i,
            numOfEmptySlotsInside: s,
          }) => {
            const l = Math.ceil(r / a) * e,
              c = o * e + 40 * s,
              E = u * e + 40 * i;
            return { paddingTop: `${E + t}rem`, paddingBottom: `${Math.max(l - E - c, 0) + n}rem` };
          },
          qt = (0, a.memo)((u) => {
            const e = u.className,
              t = u.children,
              n = u.itemsAmountPerRow,
              r = u.visibleRowsAmount,
              a = u.realFirstInRowIndex,
              i = u.amount,
              s = u.numOdfHeadingsBefore,
              l = u.numOfEmptySlotsInside,
              c = Math.min(r * n + l, i - a);
            return o().createElement(
              "div",
              { className: e, style: Yt(Object.assign({}, u, { numOdfHeadingsBefore: s })) },
              ((u, e) => {
                const t = [];
                for (let n = 0; n < u; n++) t.push(e(n));
                return t;
              })(c, (u) => t(a + u)),
            );
          }),
          Zt = "VirtualGrid_base_52",
          Qt = ({
            amount: u,
            headingsIndexes: e,
            cellWidth: t,
            cellHeight: n,
            children: r,
            api: i,
            classNames: l,
            preloadedRows: c = 1,
            paddingTop: E = 0,
            paddingBottom: A = 0,
          }) => {
            const d = i.scrollApi,
              _ = (0, a.useRef)(0),
              m = (0, a.useState)(0),
              F = m[0],
              D = m[1],
              B = (0, a.useState)(null),
              C = B[0],
              g = B[1],
              h = (0, a.useState)(null),
              p = h[0],
              v = h[1];
            ((0, a.useEffect)(() => {
              const e = (e) => {
                if (!C) return;
                const t = Math.floor((s.O.view.pxToRem(e.value.scrollPosition) - E) / n),
                  r = Math.ceil(u / C),
                  a = Math.max(0, Math.min(t - c, r));
                (D(a), i.startRowIndexChanged(a));
              };
              return (d.events.on("change", e), () => d.events.off("change", e));
            }, [i, d, n, E, C, u, c]),
              (0, a.useEffect)(() => {
                const u = () => {
                    if (d.contentRef.current) {
                      const u = getComputedStyle(d.contentRef.current),
                        e = d.contentRef.current.getBoundingClientRect(),
                        r =
                          s.O.view.pxToRem(e.width) -
                          (parseFloat(u.paddingLeft) + parseFloat(u.paddingRight)),
                        a = Math.floor(r / t),
                        o = Math.ceil(s.O.view.pxToRem(e.height) / n) + 2 * c;
                      ((_.current = a), C !== a && g(a), v(o), i.layoutCalculated(a, o));
                    }
                  },
                  e = () => {
                    const e = _.current;
                    (u(), i.scrollToIndex(F * e));
                  };
                return (
                  d.events.on("recalculateContent", u),
                  d.events.on("resizeHandled", e),
                  () => {
                    (d.events.off("recalculateContent", u), d.events.off("resizeHandled", e));
                  }
                );
              }, [i, d, n, t, C, c, F]),
              (0, a.useEffect)(() => {
                const u = (u, e = !0) => {
                  C && d.applyScroll(Math.floor((u + 1) / C) * n + E, { immediate: e });
                };
                return (i.events.on("scrollToIndex", u), () => i.events.off("scrollToIndex", u));
              }, [i, n, C, E, d]));
            const b = (({ api: u, startRowIndex: e, itemsAmountPerRow: t, headingsIndexes: n }) => {
                const r = e * t;
                if (!n) return r;
                const a = n.reduce((u, e, n, a) => {
                  if (e < r) {
                    if (0 === n) return u + 1;
                    const r = (e - 1 - a[n - 1]) % t;
                    u += 1 - (r ? t - r : 0);
                  }
                  return u;
                }, r);
                return (u.firstCardIndexChanged(a), a);
              })({ api: i, headingsIndexes: e, startRowIndex: F, itemsAmountPerRow: C || 4 }),
              w = (({ offset: u, headingsIndexes: e }) => (e ? e.filter((e) => e < u).length : 0))({
                offset: b,
                headingsIndexes: e,
              }),
              x = (({ amount: u, offset: e, headingsIndexes: t }) =>
                t ? t.filter((t) => t >= e && t <= e + u).length : 0)({
                offset: b,
                amount: (p || 1) * (C || 4),
                headingsIndexes: e,
              }),
              S = (({ offset: u, amount: e, itemsAmountPerRow: t, headingsIndexes: n }) =>
                n
                  ? n.reduce((n, r, a, o) => {
                      if (r >= u && r <= u + e) {
                        if (0 === a) return n + 1;
                        const u = (r - 1 - o[a - 1]) % t;
                        n += 1 + (u ? t - u : 0);
                      }
                      return n;
                    }, 0)
                  : 0)({
                headingsIndexes: e,
                offset: b,
                amount: (p || 1) * (C || 4),
                itemsAmountPerRow: C || 4,
              });
            return o().createElement(
              Kt.Vertical.Default,
              {
                api: d,
                className: null == l ? void 0 : l.scroll,
                areaClassName: null == l ? void 0 : l.areaClassName,
                scrollClassName: null == l ? void 0 : l.scrollClassName,
                scrollClassNames: {
                  content: null == l ? void 0 : l.content,
                  wrapper: null == l ? void 0 : l.wrapper,
                },
              },
              null !== C &&
                null !== p &&
                o().createElement(
                  qt,
                  {
                    className: f()(Zt, null == l ? void 0 : l.inner),
                    paddingBottom: A,
                    realFirstInRowIndex: b,
                    numOdfHeadingsBefore: w,
                    numOdfHeadingsInside: x,
                    paddingTop: E,
                    amount: u,
                    itemsAmountPerRow: C,
                    visibleRowsAmount: p,
                    numOfEmptySlotsInside: S,
                    startRowIndex: F,
                    cellHeight: n,
                  },
                  r,
                ),
            );
          },
          Jt = "EmptyState_base_36",
          un = () =>
            o().createElement(
              "div",
              { className: Jt },
              R.strings.crew.filter.vehicles.noVehicles(),
            );
        let en;
        !(function (u) {
          ((u.Name = "name"), (u.Tier = "tier"), (u.Type = "type"));
        })(en || (en = {}));
        const tn = {
          base: "SortButton_base_74",
          base__disabled: "SortButton_base__disabled_f2",
          sortDirection: "SortButton_sortDirection_3b",
          base__current: "SortButton_base__current_19",
          base__isAscending: "SortButton_base__isAscending_c9",
        };
        let nn;
        !(function (u) {
          ((u.Default = "default"), (u.Disabled = "disabled"), (u.Current = "current"));
        })(nn || (nn = {}));
        const rn = (0, su.Pi)(
            ({
              column: u,
              className: e,
              children: t,
              state: n = nn.Default,
              isAscending: r = !0,
            }) => {
              const a = De().controls,
                i = R.strings.crew.filter.vehicles.tooltip.$dyn(u);
              return o().createElement(
                K,
                {
                  header: null == i ? void 0 : i.$dyn("header"),
                  body: null == i ? void 0 : i.$dyn("body"),
                },
                o().createElement(
                  "div",
                  {
                    onClick: () => n !== nn.Disabled && a.sortVehiclesByColumn(u),
                    className: f()(tn.base, r && tn.base__isAscending, tn[`base__${n}`], e),
                  },
                  t,
                  o().createElement("div", { className: tn.sortDirection }),
                ),
              );
            },
          ),
          an = {
            icon: "SortButtonContent_icon_0a",
            icon__type: "SortButtonContent_icon__type_b4",
            icon__tier: "SortButtonContent_icon__tier_65",
            name: "SortButtonContent_name_b4",
          },
          on = o().memo(function ({ column: u }) {
            return u === en.Name
              ? o().createElement(
                  "div",
                  { className: an.name },
                  R.strings.crew.filter.vehicles.vehicleName(),
                )
              : o().createElement("div", { className: f()(an.icon, an[`icon__${u}`]) });
          }),
          sn = {
            base: "Header_base_65",
            divider: "Header_divider_81",
            button: "Header_button_a5",
            button__tier: "Header_button__tier_95",
            button__type: "Header_button__type_e1",
            button__name: "Header_button__name_f4",
          },
          ln = [en.Tier, en.Type, en.Name],
          cn = (u, e) => (e ? nn.Disabled : u ? nn.Current : nn.Default),
          En = (0, su.Pi)(() => {
            const u = De().model,
              e = 0 === u.vehicles.get().length,
              t = u.isVehicleSortAscending.get(),
              n = u.vehicleSortColumn.get();
            return o().createElement(
              "div",
              { className: sn.base },
              ln.map((u) =>
                o().createElement(
                  rn,
                  {
                    key: u,
                    column: u,
                    className: f()(sn.button, sn[`button__${u}`]),
                    isAscending: t,
                    state: cn(u === n, e),
                  },
                  o().createElement(on, { column: u }),
                ),
              ),
              o().createElement("div", { className: sn.divider }),
            );
          }),
          An = {
            base: "VehicleTypeIcon_base_80",
            base__big: "VehicleTypeIcon_base__big_01",
            base__c_44x44: "VehicleTypeIcon_base__c_44x44_80",
            base__c_60x54: "VehicleTypeIcon_base__c_60x54_08",
          };
        let dn;
        !(function (u) {
          ((u.c83x74 = "big"), (u.c60x54 = "c_60x54"), (u.c44x44 = "c_44x44"));
        })(dn || (dn = {}));
        const _n = o().memo(function ({
            vehicleType: u,
            isElite: e,
            className: t,
            iconSize: n = dn.c44x44,
          }) {
            const r = `${ku(u)}${e ? "_elite" : ""}`,
              a = R.images.gui.maps.icons.vehicleTypes.$dyn(n);
            return o().createElement("div", {
              className: f()(An.base, An[`base__${n}`], t),
              style: { backgroundImage: `url(${null == a ? void 0 : a.$dyn(r)})` },
            });
          }),
          mn = "Content_base_c3",
          Fn = "Content_base__selected_dd",
          Dn = "Content_selectedFrame_ff",
          Bn = "Content_tier_99",
          Cn = "Content_type_2a",
          gn = "Content_typeIcon_92",
          hn = "Content_name_ee",
          fn = o().memo(function ({
            isSelected: u,
            name: e,
            onClick: t,
            tier: n,
            techName: r,
            nation: a,
            isPremium: i,
            type: s,
          }) {
            return o().createElement(
              "div",
              { onClick: t, className: f()(mn, u && Fn) },
              o().createElement("div", { className: Bn }, Ju(n)),
              o().createElement(
                "div",
                { className: Cn },
                o().createElement(_n, { className: gn, isElite: i, vehicleType: s }),
              ),
              o().createElement(
                "div",
                {
                  className: hn,
                  style: {
                    backgroundImage: `url(${R.images.gui.maps.icons.vehicle.small.$dyn(ku(`${a}-${r}`))})`,
                  },
                },
                e,
              ),
              u && o().createElement("div", { className: Dn }),
            );
          });
        function pn() {
          return (
            (pn =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            pn.apply(this, arguments)
          );
        }
        const vn = (0, su.Pi)(({ index: u }) => {
            const e = De(),
              t = e.model,
              n = e.controls,
              r = ou(t.vehicles.get(), u);
            if (!r) throw Error(`${u} is out ov vehicles range`);
            return o().createElement(
              fn,
              pn({}, r, { onClick: () => n.selectVehicle(r.vehicleCD) }),
            );
          }),
          bn = "VehicleList_base_ad",
          wn = "VehicleList_gridWrapper_bc",
          xn = [],
          Sn = (0, su.Pi)(({ className: u }) => {
            const e = De().model.vehicles.get().length,
              t = (() => {
                const u = Kt.Vertical.useVerticalScrollApi(),
                  e = it(),
                  t = (0, a.useCallback)((u, t = !0) => e.trigger("scrollToIndex", u, t), [e]),
                  n = (0, a.useCallback)((u, t) => e.trigger("layoutCalculated", u, t), [e]),
                  r = (0, a.useCallback)((u) => e.trigger("startRowIndexChanged", u), [e]),
                  o = (0, a.useCallback)((u) => e.trigger("firstCardIndexChanged", u), [e]);
                return (0, a.useMemo)(
                  () => ({
                    scrollToIndex: t,
                    layoutCalculated: n,
                    startRowIndexChanged: r,
                    firstCardIndexChanged: o,
                    scrollApi: u,
                    events: { off: e.off, on: e.on },
                  }),
                  [t, n, r, o, u, e.off, e.on],
                );
              })();
            return (
              (0, a.useEffect)(() => {
                t.scrollApi.applyScroll(0, { immediate: !0 });
              }, [e, t.scrollApi]),
              o().createElement(
                "div",
                { className: f()(bn, u) },
                o().createElement(En, null),
                o().createElement(
                  "div",
                  { className: wn },
                  e > 0
                    ? o().createElement(
                        Qt,
                        { amount: e, cellWidth: 230, cellHeight: 34, api: t, headingsIndexes: xn },
                        (u) => o().createElement(vn, { key: u, index: u }),
                      )
                    : o().createElement(un, null),
                ),
              )
            );
          }),
          yn = "FilterPopoverApp_base_a9",
          Mn = "FilterPopoverApp_base__withVehicleFilter_2b",
          Ln = "FilterPopoverApp_title_39",
          Tn = "FilterPopoverApp_divider_d0",
          Rn = "FilterPopoverApp_content_23",
          On = "FilterPopoverApp_filterGroup_ac",
          Nn = "FilterPopoverApp_vehicles_97";
        function Pn() {
          return (
            (Pn =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Pn.apply(this, arguments)
          );
        }
        const Hn = (u, e, t, n) => (100 * (e + t / 2 - (n + 58))) / s.O.view.pxToRem(u),
          In = (0, su.Pi)(() => {
            const u = (0, a.useState)(void 0),
              e = u[0],
              t = u[1],
              n = De(),
              r = n.model,
              i = n.controls,
              l = r.hasVehicleFilter.get(),
              c = (0, a.useRef)(null);
            var E;
            return (
              (E = W.SW),
              au(nu.n.ESCAPE, E),
              (0, a.useEffect)(
                () =>
                  Y(() =>
                    Y(() => {
                      c.current &&
                        t(
                          ((u) => {
                            const e = window.decorator,
                              t = e.directionType,
                              n = e.boundY,
                              r = e.boundHeight,
                              a = e.boundX,
                              o = e.boundWidth,
                              i = u.getBoundingClientRect(),
                              l = i.width,
                              c = i.height,
                              E = s.O.view.getViewGlobalPosition(),
                              A = E.x,
                              d = E.y;
                            switch (t) {
                              case uu.Left:
                              case uu.Right:
                                return { top: `${Hn(c, n, r, d)}%` };
                              case uu.Bottom:
                              case uu.Top:
                                return { left: `${Hn(l, a, o, A)}%` };
                            }
                          })(c.current),
                        );
                    }),
                  ),
                [],
              ),
              o().createElement(
                tu,
                { customStyles: { arrow: e } },
                o().createElement(
                  "div",
                  { ref: c, className: f()(yn, l && Mn) },
                  o().createElement(
                    "div",
                    { className: Ln },
                    r.title.get(),
                    o().createElement("div", { className: Tn }),
                  ),
                  o().createElement(
                    "div",
                    { className: Rn },
                    iu(r.filterGroups.get(), (u) =>
                      o().createElement(
                        le,
                        Pn({ key: u.id }, u, {
                          theme: ie.InPopup,
                          onClick: i.updateFilter,
                          className: On,
                        }),
                      ),
                    ),
                    l && o().createElement(Sn, { className: Nn }),
                    o().createElement(ut, null),
                  ),
                ),
              )
            );
          });
        engine.whenReady.then(() => {
          k().render(
            o().createElement(Fe, null, o().createElement(H, null, o().createElement(In, null))),
            document.getElementById("root"),
          );
        });
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
        var r = 1 / 0;
        for (s = 0; s < deferred.length; s++) {
          for (var [e, t, n] = deferred[s], a = !0, o = 0; o < e.length; o++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[o]))
              ? e.splice(o--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(s--, 1);
            var i = t();
            void 0 !== i && (u = i);
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
    (__webpack_require__.j = 35),
    (() => {
      var u = { 35: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var n,
            r,
            [a, o, i] = t,
            s = 0;
          if (a.some((e) => 0 !== u[e])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (i) var l = i(__webpack_require__);
          }
          for (e && e(t); s < a.length; s++)
            ((r = a[s]), __webpack_require__.o(u, r) && u[r] && u[r][0](), (u[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(3939));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
