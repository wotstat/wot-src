(() => {
  var __webpack_modules__ = {
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
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => s, onResize: () => r }));
        var n = u(2472),
          a = u(1176);
        const r = (0, n.E)("clientResized"),
          o = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, a.R)(!1);
          }
          function u() {
            e.enabled && (0, a.R)(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", u))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", u))
              : (0, a.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let a = !0;
                  const r = `mouse${t}`,
                    s = o[t]((e) => u([e, "outside"]));
                  function l(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, l),
                    n(),
                    () => {
                      a &&
                        (s(), window.removeEventListener(r, l), (e.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(u)),
              t
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
              e.enabled && (0, a.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, a.R)(!1);
            },
          });
        })();
      },
      5959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => r,
            getSize: () => a,
            graphicsQuality: () => o,
          }));
        var n = u(527);
        function a(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
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
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => n });
      },
      2472: (e, t, u) => {
        "use strict";
        function n(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        u.d(t, { E: () => n });
      },
      3138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => a });
        var n = u(5959);
        const a = { view: u(7641), client: n };
      },
      3722: (e, t, u) => {
        "use strict";
        function n(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function a(e, t, u) {
          return `url(${n(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => a, getTextureUrl: () => n }));
      },
      6112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => a });
        var n = u(2472);
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
      7641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => n,
            displayStatus: () => a.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => D,
            freezeTextureBeforeResize: () => p,
            getBrowserTexturePath: () => i,
            getDisplayStatus: () => B,
            getScale: () => b,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => h,
            isEventHandled: () => F,
            isFocused: () => f,
            pxToRem: () => g,
            remToPx: () => A,
            resize: () => m,
            sendEvent: () => o.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => v,
            setInputPaddingsRem: () => l,
            setSidePaddingsRem: () => _,
            whenTutorialReady: () => S,
          }));
        var n = u(3722),
          a = u(6112),
          r = u(6538),
          o = u(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function l(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function i(e, t, u, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, n);
        }
        function c(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function _(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: A(t.x), y: A(t.y) };
        }
        function p() {
          viewEnv.freezeTextureBeforeResize();
        }
        function b() {
          return viewEnv.getScale();
        }
        function g(e) {
          return viewEnv.pxToRem(e);
        }
        function A(e) {
          return viewEnv.remToPx(e);
        }
        function C(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function f() {
          return viewEnv.isFocused();
        }
        function h() {
          return viewEnv.isClientAccessible();
        }
        function v() {
          return viewEnv.setEventHandled();
        }
        function F() {
          return viewEnv.isEventHandled();
        }
        function D() {
          viewEnv.forceTriggerMouseMove();
        }
        function B() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(a.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === a.W[t]), e),
            {},
          ),
          y = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          S = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => i });
        const n = ["args"];
        const a = 2,
          r = 16,
          o = 32,
          s = 64,
          l = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(t, n);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, o, {
                      arguments:
                        ((a = r),
                        Object.entries(a).map(([e, t]) => {
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
            var a;
          },
          i = {
            close(e) {
              l("popover" === e ? a : o);
            },
            minimize() {
              l(s);
            },
            move(e) {
              l(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      5521: (e, t, u) => {
        "use strict";
        let n, a;
        (u.d(t, { n: () => n }),
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
          })(a || (a = {})));
      },
      1358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => r });
        var n = u(3138);
        class a {
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
            return (window.__dataTracker || (window.__dataTracker = new a()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, t, u = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = n.O.view.addModelObserver(e, u, a);
            return (
              r > 0
                ? ((this._callbacks[r] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(r) : (this._views[u] = [r])))
                : console.error("Can't add callback for model:", e),
              r
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
              const n = this._callbacks[u];
              void 0 !== n && n(e, t);
            });
          }
        }
        a.__instance = void 0;
        const r = a;
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
        u.d(t, {
          Sw: () => r.Z,
          B3: () => i,
          Z5: () => o,
          B0: () => l,
          c9: () => f,
          wU: () => D,
          ry: () => A,
          Eu: () => C,
          SW: () => v,
          P3: () => F,
        });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: u }) => {
                  let n = e.target;
                  do {
                    if (n === t) return;
                    n = n.parentNode;
                  } while (n);
                  u();
                });
              }));
          }
          static get instance() {
            return (n.__instance || (n.__instance = new n()), n.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const u = e,
              n = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== u || t !== n,
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
        var r = u(1358);
        const o = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          s = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, u) => userLocale.getTimeFormat(e, t, void 0 === u || u),
            getTimeString: (e, t, u) => userLocale.getTimeString(e, t, void 0 === u || u),
          };
        let l;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(l || (l = {}));
        const i = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = u(5521),
          E = u(3138);
        const p = ["args"];
        function b(e, t, u, n, a, r, o) {
          try {
            var s = e[r](o),
              l = s.value;
          } catch (e) {
            return void u(e);
          }
          s.done ? t(l) : Promise.resolve(l).then(n, a);
        }
        const g = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          A = (function () {
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
                  return new Promise(function (n, a) {
                    var r = e.apply(t, u);
                    function o(e) {
                      b(r, n, a, o, s, "next", e);
                    }
                    function s(e) {
                      b(r, n, a, o, s, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          C = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          f = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(t, p);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, r, {
                      arguments:
                        ((n = a),
                        Object.entries(n).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          h = () => f(l.CLOSE),
          v = () => f(l.POP_OVER, { on: !1 }),
          F = (e, t, u, n, a = R.invalid("resId"), r) => {
            const o = E.O.view.getViewGlobalPosition(),
              s = u.getBoundingClientRect(),
              i = s.x,
              c = s.y,
              _ = s.width,
              d = s.height,
              m = {
                x: E.O.view.pxToRem(i) + o.x,
                y: E.O.view.pxToRem(c) + o.y,
                width: E.O.view.pxToRem(_),
                height: E.O.view.pxToRem(d),
              };
            f(l.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: a,
              direction: t,
              bbox: g(m),
              on: !0,
              args: r,
            });
          },
          D = () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
          B = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var w = u(7572);
        const y = a.instance,
          S = {
            DataTracker: r.Z,
            ViewModel: w.Z,
            ViewEventType: l,
            NumberFormatType: i,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: g,
            sendMoveEvent: (e) => f(l.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: h,
            sendClosePopOverEvent: v,
            sendShowContextMenuEvent: (e, t, u = 0) => {
              f(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: F,
            addEscapeListener: (e) => {
              const t = (t) => B(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              B(e, h);
            },
            handleViewEvent: f,
            onBindingsReady: A,
            onLayoutReady: C,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: D,
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const a = Object.prototype.toString.call(t[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = t[n];
                    u[n] = [];
                    for (let t = 0; t < a.length; t++) u[n].push({ value: e(a[t].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[n] = e(t[n]))
                      : (u[n] = t[n]);
                }
              return u;
            },
            ClickOutsideManager: y,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = S;
      },
      2774: (e, t, u) => {
        "use strict";
        var n = {};
        (u.r(n),
          u.d(n, {
            Area: () => ni,
            Bar: () => ei,
            DefaultScroll: () => ui,
            Direction: () => rt,
            defaultSettings: () => ot,
            useHorizontalScrollApi: () => lt,
          }));
        var a = {};
        (u.r(a),
          u.d(a, {
            Area: () => hi,
            Bar: () => Ai,
            Default: () => fi,
            useVerticalScrollApi: () => ai,
          }));
        var r = u(6179),
          o = u.n(r),
          s = u(493),
          l = u.n(s),
          i = u(3403);
        function c() {
          return !1;
        }
        console.log;
        var _ = u(9174),
          d = u(3138);
        function m(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return E(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return E(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function E(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const p = (e) => (0 === e ? window : window.subViews.get(e));
        const b = () => (e, t) => {
            const u = (0, r.createContext)({});
            return [
              function ({ mode: n = "real", options: a, children: s, mocks: l }) {
                const i = (0, r.useRef)([]),
                  E = (u, n, a) => {
                    var r;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: u = p,
                        context: n = "model",
                      } = {}) {
                        const a = new Map();
                        function r(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? a.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, u) => {
                            u.forEach((t) => {
                              const u = a.get(t);
                              void 0 !== u && u(e);
                            });
                          });
                        });
                        const o = (e) => {
                          const a = u(t),
                            r = n.split(".").reduce((e, t) => e[t], a);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, t) => {
                                const u = e[t];
                                return "function" == typeof u ? u.bind(e) : u;
                              }, r);
                        };
                        return {
                          subscribe: (u, r) => {
                            const s = "string" == typeof r ? `${n}.${r}` : n,
                              l = d.O.view.addModelObserver(s, t, !0);
                            return (a.set(l, u), e && u(o(r)), l);
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
                            for (var e, u = m(a.keys()); !(e = u()).done;) r(e.value, t);
                          },
                          unsubscribe: r,
                        };
                      })(n),
                      s =
                        "real" === u
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (r = null == a ? void 0 : a.getter) ? r : () => {},
                            }),
                      l = (e) =>
                        "mocks" === u ? (null == a ? void 0 : a.getter(e)) : s.readByPath(e),
                      E = (e) => i.current.push(e),
                      b = e({
                        mode: u,
                        readByPath: l,
                        externalModel: s,
                        observableModel: {
                          array: (e, t) => {
                            const n = null != t ? t : l(e),
                              a = _.LO.box(n, { equals: c });
                            return (
                              "real" === u &&
                                s.subscribe(
                                  (0, _.aD)((e) => a.set(e)),
                                  e,
                                ),
                              a
                            );
                          },
                          object: (e, t) => {
                            const n = null != t ? t : l(e),
                              a = _.LO.box(n, { equals: c });
                            return (
                              "real" === u &&
                                s.subscribe(
                                  (0, _.aD)((e) => a.set(e)),
                                  e,
                                ),
                              a
                            );
                          },
                          primitives: (e, t) => {
                            const n = l(t);
                            if (Array.isArray(e)) {
                              const a = e.reduce((e, t) => ((e[t] = _.LO.box(n[t], {})), e), {});
                              return (
                                "real" === u &&
                                  s.subscribe(
                                    (0, _.aD)((t) => {
                                      e.forEach((e) => {
                                        a[e].set(t[e]);
                                      });
                                    }),
                                    t,
                                  ),
                                a
                              );
                            }
                            {
                              const a = e,
                                r = Object.entries(a),
                                o = r.reduce((e, [t, u]) => ((e[u] = _.LO.box(n[t], {})), e), {});
                              return (
                                "real" === u &&
                                  s.subscribe(
                                    (0, _.aD)((e) => {
                                      r.forEach(([t, u]) => {
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
                        cleanup: E,
                      }),
                      g = { mode: u, model: b, externalModel: s, cleanup: E };
                    return {
                      model: b,
                      controls: "mocks" === u && a ? a.controls(g) : t(g),
                      externalModel: s,
                      mode: u,
                    };
                  },
                  b = (0, r.useRef)(!1),
                  g = (0, r.useState)(n),
                  A = g[0],
                  C = g[1],
                  f = (0, r.useState)(() => E(n, a, l)),
                  h = f[0],
                  v = f[1];
                return (
                  (0, r.useEffect)(() => {
                    b.current ? v(E(A, a, l)) : (b.current = !0);
                  }, [l, A, a]),
                  (0, r.useEffect)(() => {
                    C(n);
                  }, [n]),
                  (0, r.useEffect)(
                    () => () => {
                      (h.externalModel.dispose(), i.current.forEach((e) => e()));
                    },
                    [h],
                  ),
                  o().createElement(u.Provider, { value: h }, s)
                );
              },
              () => (0, r.useContext)(u),
            ];
          },
          g = b()(
            ({ observableModel: e }) => {
              const t = { root: e.object() };
              return Object.assign({}, t, { computes: {} });
            },
            ({ externalModel: e }) => ({}),
          ),
          A = (g[0], g[1]);
        var C = u(6483),
          f = u.n(C);
        const h = (e, t, u) =>
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
              : e,
          v = {
            extraLarge: { weight: 4, width: 2560, height: 1440 },
            large: { weight: 3, width: 1920, height: 1080 },
            medium: { weight: 2, width: 1600, height: 900 },
            small: { weight: 1, width: 1366, height: 768 },
            extraSmall: { weight: 0, width: 1024, height: 768 },
          };
        var F;
        function D(e, t, u) {
          const n = (function (e, t) {
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
            a = (function (e, t) {
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
            r = Math.min(n, a);
          return {
            extraLarge: r === u.extraLarge.weight,
            large: r === u.large.weight,
            medium: r === u.medium.weight,
            small: r === u.small.weight,
            extraSmall: r === u.extraSmall.weight,
            extraLargeWidth: n === u.extraLarge.weight,
            largeWidth: n === u.large.weight,
            mediumWidth: n === u.medium.weight,
            smallWidth: n === u.small.weight,
            extraSmallWidth: n === u.extraSmall.weight,
            extraLargeHeight: a === u.extraLarge.weight,
            largeHeight: a === u.large.weight,
            mediumHeight: a === u.medium.weight,
            smallHeight: a === u.small.weight,
            extraSmallHeight: a === u.extraSmall.weight,
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
        })(F || (F = {}));
        const B = d.O.client.getSize("rem"),
          w = B.width,
          y = B.height,
          S = Object.assign({ width: w, height: y }, D(w, y, v)),
          k = (0, r.createContext)(S),
          T = ["children"];
        const N = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, T);
          const n = (0, r.useContext)(k),
            a = n.extraLarge,
            o = n.large,
            s = n.medium,
            l = n.small,
            i = n.extraSmall,
            c = n.extraLargeWidth,
            _ = n.largeWidth,
            d = n.mediumWidth,
            m = n.smallWidth,
            E = n.extraSmallWidth,
            p = n.extraLargeHeight,
            b = n.largeHeight,
            g = n.mediumHeight,
            A = n.smallHeight,
            C = n.extraSmallHeight,
            f = { extraLarge: p, large: b, medium: g, small: A, extraSmall: C };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && a) return t;
            if (u.large && o) return t;
            if (u.medium && s) return t;
            if (u.small && l) return t;
            if (u.extraSmall && i) return t;
          } else {
            if (u.extraLargeWidth && c) return h(t, u, f);
            if (u.largeWidth && _) return h(t, u, f);
            if (u.mediumWidth && d) return h(t, u, f);
            if (u.smallWidth && m) return h(t, u, f);
            if (u.extraSmallWidth && E) return h(t, u, f);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && p) return t;
              if (u.largeHeight && b) return t;
              if (u.mediumHeight && g) return t;
              if (u.smallHeight && A) return t;
              if (u.extraSmallHeight && C) return t;
            }
          }
          return null;
        };
        N.defaultProps = {
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
        (0, r.memo)(N);
        const I = (e) => {
            const t = (0, r.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          M = (0, r.memo)(({ children: e }) => {
            const t = (0, r.useContext)(k),
              u = (0, r.useState)(t),
              n = u[0],
              a = u[1],
              s = (0, r.useCallback)((e, t) => {
                const u = d.O.view.pxToRem(e),
                  n = d.O.view.pxToRem(t);
                a(Object.assign({ width: u, height: n }, D(u, n, v)));
              }, []);
            (I(() => {
              engine.on("clientResized", s);
            }),
              (0, r.useEffect)(() => () => engine.off("clientResized", s), [s]));
            const l = (0, r.useMemo)(() => Object.assign({}, n), [n]);
            return o().createElement(k.Provider, { value: l }, e);
          }),
          x = (e) => {
            const t = (0, r.useRef)();
            return (
              (0, r.useEffect)(() => {
                t.current = e;
              }, [e]),
              t.current
            );
          };
        let O;
        function L(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        function P(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(O || (O = {}));
        const H = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          z = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          W = (e, t, u = O.left) => e.split(t).reduce(u === O.left ? H : z, []),
          U = (() => {
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
            return (t) =>
              t
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          V = ["zh_cn", "zh_sg", "zh_tw"],
          j = (e, t = O.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return V.includes(u)
              ? U(e)
              : ((e, t = O.left) => {
                  let u = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = e.replace(/&nbsp;/g, " ");
                  return (W(a, /( )/, t).forEach((e) => (u = u.concat(W(e, n, O.left)))), u);
                })(e, t);
          };
        let $;
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
        })($ || ($ = {}));
        var G = u(4179);
        const q = 60,
          X = 3600,
          Y = 86400;
        Date.now();
        const K = () => {},
          Z = (e = 0, t, u = 0, n = K) => {
            const a = (0, r.useState)(e),
              o = a[0],
              s = a[1];
            return (
              (0, r.useEffect)(() => {
                if (e > 0) {
                  s(e);
                  const a = Date.now(),
                    r = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - a) / 1e3);
                        null !== u && t <= u ? (s(u), n && n(), clearInterval(r)) : s(t);
                      },
                      1e3 * (t || (e > 120 ? q : 1)),
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                s(0);
              }, [e, t, u, n]),
              o
            );
          },
          J = (e = 1) => {
            const t = new Error().stack;
            let u,
              n = R.invalid("resId");
            return (
              t &&
                ((u = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                window.__feature &&
                  window.__feature !== u &&
                  window.subViews[u] &&
                  (n = window.subViews[u].id)),
              { caller: u, stack: t, resId: n }
            );
          },
          Q = (e, t) => e.split(".").reduce((e, t) => e && e[t], t),
          ee = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          te = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          ue = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, u) => {
                const n = Q(`${e}.${u}`, window);
                return ee(n) ? t(e, u, n) : `${e}.${u}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          ne = (e) => {
            const t = ((e) => {
                const t = J(),
                  u = t.caller,
                  n = t.resId,
                  a = window.__feature && window.__feature !== u && u ? `subViews.${u}` : "";
                return { modelPrefix: a, modelPath: te(a, e || ""), resId: n };
              })(),
              u = t.modelPrefix,
              n = e.split(".");
            if (n.length > 0) {
              const e = [n[0]];
              return (
                n.reduce((t, n) => {
                  const a = Q(te(u, `${t}.${n}`), window);
                  return ee(a) ? (e.push(a.id), `${t}.${n}.value`) : (e.push(n), `${t}.${n}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          ae = G.Sw.instance;
        let re;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(re || (re = {}));
        const oe = (e = "model", t = re.Deep) => {
            const u = (0, r.useState)(0),
              n = (u[0], u[1]),
              a = (0, r.useMemo)(() => J(), []),
              o = a.caller,
              s = a.resId,
              l = (0, r.useMemo)(
                () => (window.__feature && window.__feature !== o ? `subViews.${o}.${e}` : e),
                [o, e],
              ),
              i = (0, r.useState)(() =>
                ((e) => {
                  const t = Q(e, window);
                  for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                  return ee(t) ? t.value : t;
                })(ue(l)),
              ),
              c = i[0],
              _ = i[1],
              d = (0, r.useRef)(-1);
            return (
              I(() => {
                if (
                  ("boolean" == typeof t &&
                    ((t = t ? re.Deep : re.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  t !== re.None)
                ) {
                  const u = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      t === re.Deep
                        ? (e === c && n((e) => e + 1), _(e))
                        : _(Object.assign([], e));
                    },
                    a = ne(e);
                  d.current = ae.addCallback(a, u, s, t === re.Deep);
                }
              }),
              (0, r.useEffect)(() => {
                if (t !== re.None)
                  return () => {
                    ae.removeCallback(d.current, s);
                  };
              }, [s, t]),
              c
            );
          },
          se = (G.Sw.instance, x),
          le = Z,
          ie = /<link.*?>/g,
          ce = /\.\.\//g,
          _e = /<script.*?>/g,
          de = "default.css",
          me = (e) => {
            const t = e.match(ce);
            return t && t.join("");
          },
          Ee = () => {
            for (
              var e = 0, t = Array.from(document.head.querySelectorAll('link[rel="stylesheet"]'));
              e < t.length;
              e++
            ) {
              const u = t[e];
              if (!u.href.includes(de)) return u.href;
            }
            return "";
          },
          pe = (e, t) => {
            const u = Ee(),
              n = me(u);
            let a,
              r = e;
            for (; null !== (a = _e.exec(e));) {
              const e = a[0].match(/<script (defer|defer="defer") src="(.*?)">/);
              if (e) {
                const u = n + e[2].replace(ce, "");
                ((r = r.replace(e[2], u)),
                  (r = r.replace('<div id="root"', `<div data-root-id=${t} id="root"`)));
              }
            }
            return r;
          },
          be = "SubView_base_df",
          ge = "subViews.onChanged",
          Ae = (() => {
            const e = [];
            let t = !1;
            const u = () => {
              if (!e.length) return void (t = !1);
              const n = e.shift();
              n && ((t = !0), n().then(() => u()));
            };
            return {
              add: (n) => {
                (e.push(n), t || u());
              },
            };
          })(),
          Ce = (0, r.memo)(({ id: e, fallback: t, onLoadCallback: u, mixClass: n }) => {
            const a = (0, r.useState)(""),
              s = a[0],
              l = a[1],
              i = (0, r.useMemo)(() => ({ __html: pe(s, e) }), [s, e]),
              c = (0, r.useMemo)(() => window.subViews.addChildChangedCallback(e), [e]),
              _ = (0, r.useState)(!1),
              d = _[0],
              m = _[1],
              E = (0, r.useCallback)(
                (e) => {
                  e.includes(c) &&
                    (m(!0), engine.off(ge, E), window.subViews.removeChildChangedCallback(c));
                },
                [c],
              ),
              p = (0, r.useCallback)((e) => {
                Ae.add(
                  () =>
                    new Promise((t) => {
                      l(e);
                      const u = new MutationObserver(() => {
                          (u.disconnect(), t());
                        }),
                        n = document.getElementById("root");
                      n && u.observe(n, { childList: !0 });
                    }),
                );
              }, []);
            ((0, r.useEffect)(() => {
              if (window.subViews.ids().includes(e)) {
                const t = window.subViews.get(e),
                  u = t.path;
                let n;
                if ((n = u.split("/").pop()))
                  return (
                    (n = n.split(".")[0]),
                    (window.subViews[n] = Object.assign({ id: e }, t)),
                    engine.on(`subView:inject->${n}`, p),
                    (({ path: e, name: t }) => {
                      const u = new XMLHttpRequest();
                      ((u.onreadystatechange = () => {
                        4 === u.readyState &&
                          (200 === u.status
                            ? (0, G.Eu)().then(() => {
                                (console.info(`Sub view ${t} loaded: ${e}`),
                                  engine.TriggerEvent(`subView:inject->${t}`, u.responseText));
                              })
                            : console.error(`subView: status: ${u.status} - can't get bundle`));
                      }),
                        u.open("GET", e),
                        u.send());
                    })({ name: n, path: u }),
                    () => {
                      (n && window.subViews[n] && delete window.subViews[n],
                        engine.trigger("subView:destroy", { viewName: n, viewId: e }),
                        window.__dataTracker &&
                          window.__dataTracker.clearViewCallbacks &&
                          window.__dataTracker.clearViewCallbacks(e),
                        engine.off(`subView:inject->${n}`, p),
                        console.info(`Sub view ${n} is destroyed: ${u}`));
                    }
                  );
                console.error("subView: can't get View component name");
              } else engine.on(ge, E);
            }, [E, p, e, d]),
              (0, r.useEffect)(
                () => () => {
                  s &&
                    ((e) => {
                      const t = me(Ee());
                      let u;
                      for (; null !== (u = ie.exec(e));) {
                        const e = u[0].match(/href="(.*?)"/);
                        if (e) {
                          const u = t + e[1].replace(ce, ""),
                            n = document.head.querySelector(`[href="${u}"]`);
                          n && document.head.removeChild(n);
                        }
                      }
                    })(s);
                },
                [s],
              ));
            const b = f()(be, n);
            if (s) {
              let t;
              return (
                (t = document.getElementById("root")) && t.setAttribute("id", "bugSubView"),
                ((e) => {
                  let t;
                  const u = Ee(),
                    n = me(u);
                  for (; null !== (t = ie.exec(e));) {
                    const e = t[0].match(/href="(.*?)"/);
                    if (e && !e[1].includes(de) && n) {
                      const t = n + e[1].replace(ce, ""),
                        u = document.createElement("link");
                      ((u.href = t), (u.rel = "stylesheet"), document.head.appendChild(u));
                    }
                  }
                })(s),
                u && u(e),
                o().createElement("div", { className: b, dangerouslySetInnerHTML: i })
              );
            }
            return t
              ? o().createElement("div", { className: b }, o().createElement(t, null))
              : null;
          });
        var fe = u(5521);
        const he = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function ve(e = fe.n.NONE, t = he, u = !1) {
          (0, r.useEffect)(() => {
            if (e !== fe.n.NONE)
              return (
                window.addEventListener("keydown", n, u),
                () => {
                  window.removeEventListener("keydown", n, u);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (d.O.view.isEventHandled()) return;
                (d.O.view.setEventHandled(), t(n), u && n.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        function Fe(e) {
          engine.call("PlaySound", e);
        }
        const De = {
            playHighlight() {
              Fe("highlight");
            },
            playClick() {
              Fe("play");
            },
            playYes() {
              Fe("yes1");
            },
          },
          Be = {
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
        let we, ye;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(we || (we = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(ye || (ye = {})));
        const Se = ({
          children: e,
          size: t,
          isFocused: u,
          type: n,
          disabled: a,
          mixClass: s,
          soundHover: l,
          soundClick: i,
          onMouseEnter: c,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: E,
          onClick: p,
        }) => {
          const b = (0, r.useRef)(null),
            g = (0, r.useState)(u),
            A = g[0],
            C = g[1],
            h = (0, r.useState)(!1),
            v = h[0],
            F = h[1],
            D = (0, r.useState)(!1),
            B = D[0],
            w = D[1],
            y = (0, r.useCallback)(() => {
              a || (b.current && (b.current.focus(), C(!0)));
            }, [a]),
            S = (0, r.useCallback)(
              (e) => {
                A && null !== b.current && !b.current.contains(e.target) && C(!1);
              },
              [A],
            ),
            k = (0, r.useCallback)(
              (e) => {
                a || (p && p(e));
              },
              [a, p],
            ),
            T = (0, r.useCallback)(
              (e) => {
                a || (null !== l && Fe(l), c && c(e), w(!0));
              },
              [a, l, c],
            ),
            N = (0, r.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            I = (0, r.useCallback)(
              (e) => {
                a || (m && m(e), F(!1));
              },
              [a, m],
            ),
            M = (0, r.useCallback)(
              (e) => {
                a || (null !== i && Fe(i), d && d(e), u && y(), F(!0));
              },
              [a, i, d, y, u],
            ),
            x = (0, r.useCallback)(
              (e) => {
                a || (E && E(e), F(!1));
              },
              [a, E],
            ),
            O = f()(
              Be.base,
              Be[`base__${n}`],
              {
                [Be.base__disabled]: a,
                [Be[`base__${t}`]]: t,
                [Be.base__focus]: A,
                [Be.base__highlightActive]: v,
                [Be.base__firstHover]: B,
              },
              s,
            ),
            L = f()(Be.state, Be.state__default);
          return (
            (0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", S),
                () => {
                  document.removeEventListener("mousedown", S);
                }
              ),
              [S],
            ),
            (0, r.useEffect)(() => {
              C(u);
            }, [u]),
            o().createElement(
              "div",
              {
                ref: b,
                className: O,
                onMouseEnter: T,
                onMouseMove: N,
                onMouseUp: I,
                onMouseDown: M,
                onMouseLeave: x,
                onClick: k,
              },
              n !== we.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: Be.back }),
                  o().createElement("span", { className: Be.texture }),
                ),
              o().createElement(
                "span",
                { className: L },
                o().createElement("span", { className: Be.stateDisabled }),
                o().createElement("span", { className: Be.stateHighlightHover }),
                o().createElement("span", { className: Be.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: Be.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Se.defaultProps = {
          type: we.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const ke = (0, r.memo)(Se),
          Te = [
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
        function Ne(e) {
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
        const Ie = (e, t, u = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: G.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                u,
              ),
            );
          },
          Me = (e) => {
            let t = e.children,
              u = e.contentId,
              n = e.args,
              a = e.onMouseEnter,
              o = e.onMouseLeave,
              s = e.onMouseDown,
              l = e.onClick,
              i = e.ignoreShowDelay,
              c = void 0 !== i && i,
              _ = e.ignoreMouseClick,
              d = void 0 !== _ && _,
              m = e.decoratorId,
              E = void 0 === m ? 0 : m,
              p = e.isEnabled,
              b = void 0 === p || p,
              g = e.targetId,
              A = void 0 === g ? 0 : g,
              C = e.onShow,
              f = e.onHide,
              h = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Te);
            const v = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              F = (0, r.useMemo)(() => A || J().resId, [A]),
              D = (0, r.useCallback)(() => {
                (v.current.isVisible && v.current.timeoutId) ||
                  (Ie(u, E, { isMouseEvent: !0, on: !0, arguments: Ne(n) }, F),
                  C && C(),
                  (v.current.isVisible = !0));
              }, [u, E, n, F, C]),
              B = (0, r.useCallback)(() => {
                if (v.current.isVisible || v.current.timeoutId) {
                  const e = v.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (v.current.timeoutId = 0)),
                    Ie(u, E, { on: !1 }, F),
                    v.current.isVisible && f && f(),
                    (v.current.isVisible = !1));
                }
              }, [u, E, F, f]),
              w = (0, r.useCallback)((e) => {
                v.current.isVisible &&
                  ((v.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (v.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(v.current.prevTarget) && B();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = v.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === b && B();
              }, [b, B]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", B),
                  () => {
                    (window.removeEventListener("mouseleave", B), B());
                  }
                ),
                [B],
              ));
            return b
              ? (0, r.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((y = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((v.current.timeoutId = window.setTimeout(D, c ? 100 : 400)),
                            a && a(e),
                            y && y(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (B(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === d && B(), null == l || l(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === d && B(), null == s || s(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    h,
                  ),
                )
              : t;
            var y;
          },
          xe = ["children", "body", "header", "note", "alert", "args"];
        function Oe() {
          return (
            (Oe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Oe.apply(this, arguments)
          );
        }
        const Re = R.views.common.tooltip_window.simple_tooltip_content,
          Le = (e) => {
            let t = e.children,
              u = e.body,
              n = e.header,
              a = e.note,
              s = e.alert,
              l = e.args,
              i = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, xe);
            const c = (0, r.useMemo)(() => {
              const e = Object.assign({}, l, { body: u, header: n, note: a, alert: s });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [s, u, n, a, l]);
            return o().createElement(
              Me,
              Oe(
                {
                  contentId:
                    ((_ = null == l ? void 0 : l.hasHtmlContent),
                    _ ? Re.SimpleTooltipHtmlContent("resId") : Re.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                i,
              ),
              t,
            );
            var _;
          },
          Pe = (e) => {
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
          },
          He = "TextOverflow_base_3b",
          ze = ({ content: e, classMix: t }) => {
            const u = (0, r.useRef)(null),
              n = (0, r.useState)(!0),
              a = n[0],
              s = n[1];
            return (
              (0, r.useEffect)(() =>
                Pe(() => {
                  const e = u.current;
                  e && e.offsetWidth >= e.scrollWidth && s(!1);
                }),
              ),
              o().createElement(
                Le,
                { isEnabled: a, body: e },
                o().createElement("div", { ref: u, className: f()(He, t) }, e),
              )
            );
          };
        let We;
        !(function (e) {
          ((e.backport = "backport"), (e.normal = "normal"), (e.absent = "absent"));
        })(We || (We = {}));
        const Ue = "DialogTemplateButton_base_5f",
          Ve = "DialogTemplateButton_label_ff",
          je = "DialogTemplateButton_label__noTooltip_d0",
          $e = (0, r.memo)(
            ({
              onClick: e,
              isFocused: t,
              buttonID: u,
              isDisabled: n,
              label: a,
              tooltip: s,
              type: l,
            }) => {
              const i = (0, r.useCallback)(() => {
                  e({ buttonID: u });
                }, [e, u]),
                c = (0, r.useCallback)(
                  (e) => {
                    e.altKey || !t || n || i();
                  },
                  [t, n, i],
                );
              ve(fe.n.ENTER, c);
              const _ = (0, r.useMemo)(() => {
                  return (
                    (e = s.type),
                    (t = { buttonID: u }),
                    {
                      isEnabled: e !== We.absent,
                      args: t,
                      contentId: R.views.dialogs.common.DialogTemplateGenericTooltip("resId"),
                      decoratorId:
                        e === We.normal
                          ? R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId")
                          : void 0,
                      ignoreShowDelay: e === We.backport,
                      ignoreMouseClick: !0,
                    }
                  );
                  var e, t;
                }, [s.type, u]),
                d = f()(Ve, s.type !== We.absent && je);
              return o().createElement(
                Me,
                _,
                o().createElement(
                  "div",
                  { className: Ue },
                  o().createElement(
                    ke,
                    { size: ye.medium, type: l, disabled: n, onClick: i, isFocused: t },
                    o().createElement(ze, { classMix: d, content: a || "" }),
                  ),
                ),
              );
            },
          ),
          Ge = "DialogTemplateButtonList_base_ef";
        function qe() {
          return (
            (qe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            qe.apply(this, arguments)
          );
        }
        const Xe = (0, r.memo)(() => {
            const e = oe("model").onButtonClicked,
              t = oe("model.focus"),
              u = t.focusedIndex,
              n = t.onTabPressed,
              a = oe("model.buttons"),
              s = (0, r.useCallback)(
                (e) => {
                  n({ shift: e.shiftKey });
                },
                [n],
              );
            return (
              ve(fe.n.TAB, s),
              o().createElement(
                "div",
                { className: Ge },
                a.map(({ value: t }, n) =>
                  o().createElement($e, qe({ key: t.buttonID, isFocused: n === u, onClick: e }, t)),
                ),
              )
            );
          }),
          Ye = "DialogTemplateWrapper_base_cf",
          Ke = "DialogTemplateWrapper_base__hidden_b9",
          Ze = "DialogTemplateWrapper_subView_77",
          Je = (e, t, u) => (u < e ? e : u > t ? t : u);
        function Qe(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return et(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return et(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function et(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const tt = [];
        function ut(e) {
          const t = (0, r.useRef)(e);
          return (
            (0, r.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, r.useCallback)((...e) => (0, t.current)(...e), tt)
          );
        }
        function nt(e, t, u) {
          const n = (0, r.useMemo)(
            () =>
              (function (e, t, u, n) {
                let a,
                  r = !1,
                  o = 0;
                function s() {
                  a && clearTimeout(a);
                }
                function l(...l) {
                  const i = this,
                    c = Date.now() - o;
                  function _() {
                    ((o = Date.now()), u.apply(i, l));
                  }
                  r ||
                    (n && !a && _(),
                    s(),
                    void 0 === n && c > e
                      ? _()
                      : !0 !== t &&
                        (a = setTimeout(
                          n
                            ? function () {
                                a = void 0;
                              }
                            : _,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((n = u), (u = t), (t = void 0)),
                  (l.cancel = function () {
                    (s(), (r = !0));
                  }),
                  l
                );
              })(u, e),
            t,
          );
          return ((0, r.useEffect)(() => n.cancel, [n]), n);
        }
        var at = u(7030);
        let rt;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(rt || (rt = {}));
        const ot = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          st = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: u,
            getDirection: n,
            getWrapperSize: a,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const s = (e, u) => {
              const n = t(e),
                a = n[0],
                r = n[1];
              return Je(a, r, u);
            };
            return (l = {}) => {
              const i = l.settings,
                c = void 0 === i ? ot : i,
                _ = (0, r.useRef)(null),
                m = (0, r.useRef)(null),
                E = (() => {
                  const e = (0, r.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    u = (e, u) => {
                      t(e).set(u, u);
                    },
                    n = (e, u) => {
                      t(e).delete(u);
                    },
                    a = (e, ...u) => {
                      for (var n, a = Qe(t(e).values()); !(n = a()).done;) (0, n.value)(...u);
                    };
                  return (0, r.useMemo)(() => ({ on: u, off: n, trigger: a }), []);
                })(),
                p = nt(
                  () => {
                    d.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                b = (0, at.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = _.current;
                    t && (u(t, e), E.trigger("change", e), o && p());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                g = b[0],
                A = b[1],
                C = (0, r.useCallback)(
                  (e, t, u) => {
                    var n;
                    const a = g.scrollPosition.get(),
                      r = (null != (n = g.scrollPosition.goal) ? n : 0) - a;
                    return s(e, t * u + r + a);
                  },
                  [g.scrollPosition],
                ),
                f = (0, r.useCallback)(
                  (e, { immediate: t = !1, reset: u = !0 } = {}) => {
                    const n = _.current;
                    n &&
                      A.start({
                        scrollPosition: s(n, e),
                        immediate: t,
                        reset: u,
                        config: c.animationConfig,
                        from: { scrollPosition: s(n, g.scrollPosition.get()) },
                      });
                  },
                  [A, c.animationConfig, g.scrollPosition],
                ),
                h = (0, r.useCallback)(
                  (e) => {
                    const t = _.current,
                      u = m.current;
                    if (!t || !u) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return a(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(u, c.step),
                      r = C(t, e, n);
                    f(r);
                  },
                  [f, C, c.step],
                ),
                v = (0, r.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && h(n(e)),
                      _.current && E.trigger("mouseWheel", e, g.scrollPosition, t(_.current)));
                  },
                  [g.scrollPosition, h, E],
                ),
                F = ((e, t = []) => {
                  const u = (0, r.useRef)(),
                    n = (0, r.useCallback)((...t) => {
                      (u.current && u.current(), (u.current = e(...t)));
                    }, t);
                  return (
                    (0, r.useEffect)(
                      () => () => {
                        u.current && u.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    Pe(() => {
                      const e = _.current;
                      e &&
                        (f(s(e, g.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [f, g.scrollPosition.goal],
                ),
                D = ut(() => {
                  const e = _.current;
                  if (!e) return;
                  const t = s(e, g.scrollPosition.goal);
                  (t !== g.scrollPosition.goal && f(t, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, r.useEffect)(
                () => (
                  window.addEventListener("resize", F),
                  () => {
                    window.removeEventListener("resize", F);
                  }
                ),
                [F],
              );
              const B = (0, r.useCallback)((e) => E.trigger("isThumbDraggingChanged", e), [E]);
              return (0, r.useMemo)(
                () => ({
                  getWrapperSize: () => (m.current ? a(m.current) : void 0),
                  getContainerSize: () => (_.current ? e(_.current) : void 0),
                  getBounds: () =>
                    _.current
                      ? t(_.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: c.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: v,
                  applyScroll: f,
                  applyStepTo: h,
                  contentRef: _,
                  wrapperRef: m,
                  scrollPosition: A,
                  animationScroll: g,
                  recalculateContent: D,
                  handleIsThumbDragging: B,
                  events: { on: E.on, off: E.off },
                }),
                [g.scrollPosition, f, h, B, E.off, E.on, D, v, A, c.step.clampedArrowStepTimeout],
              );
            };
          },
          lt = st({
            getBounds: (e) => {
              var t, u;
              return [
                0,
                e.offsetWidth -
                  (null != (t = null == (u = e.parentElement) ? void 0 : u.offsetWidth) ? t : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, t) => {
              e.style.transform = `translateX(-${t.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? rt.Next : rt.Prev),
            triggerMouseMoveOnUpdate: !0,
          });
        var it = u(9887),
          ct = u.n(it);
        let _t, dt, mt;
        (!(function (e) {
          ((e[(e.ExtraSmall = v.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = v.small.width)] = "Small"),
            (e[(e.Medium = v.medium.width)] = "Medium"),
            (e[(e.Large = v.large.width)] = "Large"),
            (e[(e.ExtraLarge = v.extraLarge.width)] = "ExtraLarge"));
        })(_t || (_t = {})),
          (function (e) {
            ((e[(e.ExtraSmall = v.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = v.small.width)] = "Small"),
              (e[(e.Medium = v.medium.width)] = "Medium"),
              (e[(e.Large = v.large.width)] = "Large"),
              (e[(e.ExtraLarge = v.extraLarge.width)] = "ExtraLarge"));
          })(dt || (dt = {})),
          (function (e) {
            ((e[(e.ExtraSmall = v.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = v.small.height)] = "Small"),
              (e[(e.Medium = v.medium.height)] = "Medium"),
              (e[(e.Large = v.large.height)] = "Large"),
              (e[(e.ExtraLarge = v.extraLarge.height)] = "ExtraLarge"));
          })(mt || (mt = {})));
        const Et = () => {
            const e = (0, r.useContext)(k),
              t = e.width,
              u = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return _t.ExtraLarge;
                  case e.large:
                    return _t.Large;
                  case e.medium:
                    return _t.Medium;
                  case e.small:
                    return _t.Small;
                  case e.extraSmall:
                    return _t.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), _t.ExtraSmall);
                }
              })(e),
              a = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return dt.ExtraLarge;
                  case e.largeWidth:
                    return dt.Large;
                  case e.mediumWidth:
                    return dt.Medium;
                  case e.smallWidth:
                    return dt.Small;
                  case e.extraSmallWidth:
                    return dt.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), dt.ExtraSmall);
                }
              })(e),
              o = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return mt.ExtraLarge;
                  case e.largeHeight:
                    return mt.Large;
                  case e.mediumHeight:
                    return mt.Medium;
                  case e.smallHeight:
                    return mt.Small;
                  case e.extraSmallHeight:
                    return mt.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), mt.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: n,
              mediaWidth: a,
              mediaHeight: o,
              remScreenWidth: t,
              remScreenHeight: u,
            };
          },
          pt = ["xl", "lg", "md", "sm", "xs"],
          bt = (e) => e.includes("_") && ((e) => pt.includes(e))(e.split("_").at(-1)),
          gt = [_t.ExtraLarge, _t.Large, _t.Medium, _t.Small, _t.ExtraSmall],
          At = (e, t) =>
            Object.keys(e).reduce((u, n) => {
              if (n in u) return u;
              if (bt(n)) {
                const a = n.split("_").slice(0, -1).join("_");
                if (a in u) return u;
                const r = gt.indexOf(t),
                  o = (-1 !== r ? pt.slice(r) : [])
                    .map((e) => a + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  s = o ? e[o] : void 0;
                return ((u[a] = void 0 !== s ? s : e[a]), u);
              }
              const a = e[n];
              return (
                void 0 === a ||
                  ((e, t) => pt.some((u) => void 0 !== t[`${e}_${u}`]))(n, e) ||
                  (u[n] = a),
                u
              );
            }, {}),
          Ct = (e, t = At) => {
            const u = (
              (e, t = At) =>
              (u) => {
                const n = Et().mediaSize,
                  a = (0, r.useMemo)(() => t(u, n), [u, n]);
                return o().createElement(e, a);
              }
            )(e, t);
            return o().memo((t) =>
              Object.keys(t).some((e) => bt(e) && void 0 !== t[e])
                ? o().createElement(u, t)
                : o().createElement(e, t),
            );
          },
          ft = {
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
          ht = [
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
        function vt() {
          return (
            (vt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            vt.apply(this, arguments)
          );
        }
        Object.keys(ct());
        const Ft = {
            XL: { mt: ft.mt__XL, mr: ft.mr__XL, mb: ft.mb__XL, ml: ft.ml__XL },
            LG: { mt: ft.mt__LG, mr: ft.mr__LG, mb: ft.mb__LG, ml: ft.ml__LG },
            MDp: { mt: ft.mt__MDp, mr: ft.mr__MDp, mb: ft.mb__MDp, ml: ft.ml__MDp },
            MD: { mt: ft.mt__MD, mr: ft.mr__MD, mb: ft.mb__MD, ml: ft.ml__MD },
            SMp: { mt: ft.mt__SMp, mr: ft.mr__SMp, mb: ft.mb__SMp, ml: ft.ml__SMp },
            SM: { mt: ft.mt__SM, mr: ft.mr__SM, mb: ft.mb__SM, ml: ft.ml__SM },
            XS: { mt: ft.mt__XS, mr: ft.mr__XS, mb: ft.mb__XS, ml: ft.ml__XS },
          },
          Dt = (Object.keys(Ft), ["mt", "mr", "mb", "ml"]),
          Bt = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          wt = Ct((e) => {
            let t = e.className,
              u = e.width,
              n = e.height,
              a = e.m,
              s = e.mt,
              l = void 0 === s ? a : s,
              i = e.mr,
              c = void 0 === i ? a : i,
              _ = e.mb,
              d = void 0 === _ ? a : _,
              m = e.ml,
              E = void 0 === m ? a : m,
              p = e.column,
              b = e.row,
              g = e.flexDirection,
              A = void 0 === g ? (p ? "column" : b && "row") || void 0 : g,
              C = e.flexStart,
              h = e.center,
              v = e.flexEnd,
              F = e.spaceBetween,
              D = e.spaceAround,
              B = e.justifyContent,
              w =
                void 0 === B
                  ? (C ? "flex-start" : h && "center") ||
                    (v && "flex-end") ||
                    (F && "space-between") ||
                    (D && "space-around") ||
                    void 0
                  : B,
              y = e.alignItems,
              S =
                void 0 === y
                  ? (C ? "flex-start" : h && "center") || (v && "flex-end") || void 0
                  : y,
              k = e.alignSelf,
              T = e.wrap,
              N = e.flexWrap,
              I = void 0 === N ? (T ? "wrap" : void 0) : N,
              M = e.grow,
              x = e.shrink,
              O = e.flex,
              R = void 0 === O ? (M || x ? `${M ? 1 : 0} ${x ? 1 : 0} auto` : void 0) : O,
              L = e.style,
              P = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, ht);
            const z = (0, r.useMemo)(() => {
                const e = { mt: l, mr: c, mb: d, ml: E },
                  t = ((e) =>
                    Dt.reduce((t, u) => {
                      const n = e[u];
                      return n && "number" != typeof n ? t.concat(Ft[!0 === n ? "MD" : n][u]) : t;
                    }, []))(e),
                  a = ((e) =>
                    Dt.reduce((t, u) => {
                      const n = e[u];
                      return ("number" == typeof n && (t[Bt[u]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, L, a, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: R,
                    alignSelf: k,
                    display: A || S ? "flex" : void 0,
                    flexDirection: A,
                    flexWrap: I,
                    justifyContent: w,
                    alignItems: S,
                  }),
                  computedClassNames: t,
                };
              }, [u, n, l, c, d, E, L, R, k, A, I, w, S]),
              W = z.computedStyle,
              U = z.computedClassNames;
            return o().createElement(
              "div",
              vt({ className: f()(ft.base, ...U, t), style: W }, H),
              P,
            );
          }),
          yt = "FormatText_base_d0",
          St = ({ binding: e, text: t = "", classMix: u, alignment: n = O.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  r.Fragment,
                  null,
                  t.split("\n").map((t, a) =>
                    o().createElement(
                      "div",
                      { className: f()(yt, u), key: `${t}-${a}` },
                      ((e, t, u) =>
                        e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (u && e in u ? u[e] : j(e, t))))(
                        t,
                        n,
                        e,
                      ).map((e, t) => o().createElement(r.Fragment, { key: `${t}-${e}` }, e)),
                    ),
                  ),
                );
        var kt = u(3532),
          Tt = u.n(kt);
        const Nt = {
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
          It = [
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
        function Mt() {
          return (
            (Mt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Mt.apply(this, arguments)
          );
        }
        Object.keys(ct());
        const xt = Object.keys(Tt()),
          Ot = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Rt = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Lt = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Pt = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Ht =
            (Object.keys(Pt),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ot,
              "heading-H36": Ot,
              "heading-H28": Rt,
              "heading-H24": Rt,
              "heading-H24R": Rt,
              "heading-H22": Rt,
              "heading-H20R": Rt,
              "heading-H18": Rt,
              "heading-H15": Lt,
              "heading-H14": Lt,
              "paragraph-P24": Rt,
              "paragraph-P18": Rt,
              "paragraph-P16": Rt,
              "paragraph-P14": Lt,
              "paragraph-P12": Lt,
              "paragraph-P10": Lt,
            }),
          zt =
            (Object.keys(Ht),
            (e) =>
              e
                ? ((e) => xt.includes(e))(e)
                  ? { colorClassName: Nt[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Wt = Ct((e) => {
            let t = e.text,
              u = e.variant,
              n = e.className,
              a = e.color,
              s = e.m,
              l = e.mt,
              i = void 0 === l ? s : l,
              c = e.mr,
              _ = void 0 === c ? s : c,
              d = e.mb,
              m = void 0 === d ? s : d,
              E = e.ml,
              p = void 0 === E ? s : E,
              b = e.style,
              g = e.format,
              A = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, It);
            const C = (0, r.useMemo)(() => {
                const e = zt(a),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  n = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, b, n), colorClassName: t };
              }, [b, a]),
              h = C.computedStyle,
              v = C.colorClassName;
            return o().createElement(
              wt,
              Mt(
                {
                  className: f()(Nt.base, u && Nt[u], v, n),
                  style: h,
                  mt: !0 === i ? Ht[u || "paragraph-P16"].mt : i,
                  mr: !0 === _ ? Ht[u || "paragraph-P16"].mr : _,
                  mb: !0 === m ? Ht[u || "paragraph-P16"].mb : m,
                  ml: !0 === p ? Ht[u || "paragraph-P16"].ml : p,
                },
                A,
              ),
              void 0 !== g ? o().createElement(St, Mt({}, g, { text: t })) : t,
            );
          }),
          Ut = {
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
          Vt = [
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
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            jt.apply(this, arguments)
          );
        }
        class $t extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && Fe(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && Fe(this.props.soundClick));
              }),
              (this._onMouseUp = (e) => (t) => {
                (e && e(t), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const e = this.props,
              t = e.caption,
              u = e.onClick,
              n = e.goto,
              a = e.side,
              r = e.type,
              s = e.classNames,
              l = e.onMouseEnter,
              i = e.onMouseLeave,
              c = e.onMouseDown,
              _ = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(e, Vt)),
              m = f()(Ut.base, Ut[`base__${r}`], Ut[`base__${a}`], null == s ? void 0 : s.base),
              E = f()(Ut.icon, Ut[`icon__${r}`], Ut[`icon__${a}`], null == s ? void 0 : s.icon),
              p = f()(Ut.glow, null == s ? void 0 : s.glow),
              b = f()(Ut.caption, Ut[`caption__${r}`], null == s ? void 0 : s.caption),
              g = f()(Ut.goto, null == s ? void 0 : s.goto);
            return o().createElement(
              "div",
              jt(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(l),
                  onMouseLeave: this._onMouseLeave(i),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                d,
              ),
              "info" !== r && o().createElement("div", { className: Ut.shine }),
              o().createElement(
                "div",
                { className: E },
                o().createElement("div", { className: p }),
              ),
              o().createElement("div", { className: b }, t),
              n && o().createElement("div", { className: g }, n),
            );
          }
        }
        let Gt, qt;
        (($t.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (e) {
            ((e.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_PARTS = "apply_all_parts"),
              (e.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS = "apply_all_seasons"),
              (e.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS_ALERT = "apply_all_seasons_alert"),
              (e.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_SEASONS = "remove_all_seasons"),
              (e.CUSTOMIZATION_SHEET_ACTION_REMOVE_ONE = "remove_one"),
              (e.CUSTOMIZATION_SHEET_ACTION_COLOR_CHANGE = "color_change"),
              (e.CUSTOMIZATION_SHEET_ACTION_SCALE_CHANGE = "scale_change"),
              (e.CUSTOMIZATION_SHEET_RENT_PROLONG = "rent_prolong"),
              (e.CUSTOMIZATION_SHEET_RENT_NOT_PROLONG = "rent_not_prolong"),
              (e.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_PARTS = "remove_from_all_parts"),
              (e.CUSTOMIZATION_SHEET_ACTION_CLOSE = "action_close"),
              (e.CUSTOMIZATION_SHEET_ACTION_HORIZONZONTAL_MIRROR_RIGHT = "horizontal_mirror_right"),
              (e.CUSTOMIZATION_SHEET_ACTION_HORIZONZONTAL_MIRROR_LEFT = "horizontal_mirror_left"),
              (e.CUSTOMIZATION_SHEET_ACTION_VERTICAL_MIRROR_UP = "vertical_mirror_up"),
              (e.CUSTOMIZATION_SHEET_ACTION_VERTICAL_MIRROR_DOWN = "vertical_mirror_down"),
              (e.CUSTOMIZATION_SHEET_ACTION_MIRROR_LEFT_UP = "mirror_left_up"),
              (e.CUSTOMIZATION_SHEET_ACTION_MIRROR_RIGHT_UP = "mirror_right_up"),
              (e.CUSTOMIZATION_SHEET_ACTION_MIRROR_LEFT_DOWN = "mirror_left_down"),
              (e.CUSTOMIZATION_SHEET_ACTION_MIRROR_RIGHT_DOWN = "mirror_right_down"),
              (e.CUSTOMIZATION_SHEET_ACTION_MOVE = "move"),
              (e.CUSTOMIZATION_SHEET_ACTION_EDIT = "edit"),
              (e.CUSTOMIZATION_SHEET_ACTION_INFO = "info"),
              (e.CUSTOMIZATION_SHEET_ACTION_GET_BACK = "get_back"),
              (e.CUSTOMIZATION_SHEET_ACTION_SWITCH_PROGRESSION_LVL = "switch_progression_lvl"),
              (e.CUSTOMIZATION_SHEET_ACTION_EDIT_STYLE = "edit_style"));
          })(Gt || (Gt = {})),
          (function (e) {
            ((e[(e.digital = 0)] = "digital"), (e[(e.text = 1)] = "text"));
          })(qt || (qt = {})));
        const Xt = (e) => {
          (0, r.useEffect)(e, []);
        };
        function Yt() {
          const e = (0, r.useRef)(0);
          var t;
          return (
            (t = () => {
              window.clearTimeout(e.current);
            }),
            (0, r.useEffect)(() => t, []),
            (0, r.useMemo)(
              () => ({
                run: (t, u) => {
                  (window.clearTimeout(e.current),
                    (e.current = window.setTimeout(() => {
                      (t(), (e.current = 0));
                    }, u)));
                },
                clear: () => {
                  (window.clearTimeout(e.current), (e.current = 0));
                },
                get isRunning() {
                  return 0 !== e.current;
                },
              }),
              [],
            )
          );
        }
        let Kt;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(Kt || (Kt = {}));
        const Zt = {
          base: "Checkbox_base_36",
          base__disabled: "Checkbox_base__disabled_08",
          base__center: "Checkbox_base__center_52",
          base__bottom: "Checkbox_base__bottom_28",
          input: "Checkbox_input_37",
          base__mouseDown: "Checkbox_base__mouseDown_45",
          base__small: "Checkbox_base__small_18",
          base__medium: "Checkbox_base__medium_12",
          base__large: "Checkbox_base__large_f7",
          base__extraLarge: "Checkbox_base__extraLarge_c9",
          alertOverlay: "Checkbox_alertOverlay_52",
          base__alert: "Checkbox_base__alert_b7",
          blink: "Checkbox_blink_5e",
          base__checked: "Checkbox_base__checked_a2",
          inputHoverOverlay: "Checkbox_inputHoverOverlay_36",
          highlight: "Checkbox_highlight_b8",
          base__main: "Checkbox_base__main_3a",
          base__primary: "Checkbox_base__primary_ab",
          checkmark: "Checkbox_checkmark_60",
          fadeIn: "Checkbox_fadeIn_1a",
          label: "Checkbox_label_bc",
          labelContent: "Checkbox_labelContent_64",
        };
        let Jt, Qt, eu;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(Jt || (Jt = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(Qt || (Qt = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(eu || (eu = {})));
        const tu = [
          "id",
          "isChecked",
          "isDisabled",
          "isAlert",
          "size",
          "type",
          "soundHover",
          "soundClick",
          "onMouseEnter",
          "onMouseLeave",
          "onMouseUp",
          "onMouseDown",
          "onClick",
          "onChange",
          "onFocus",
          "onBlur",
          "text",
          "contentStyles",
          "children",
          "alignment",
        ];
        function uu() {
          return (
            (uu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            uu.apply(this, arguments)
          );
        }
        const nu = (e) => {
          let t = e.id,
            u = e.isChecked,
            n = void 0 !== u && u,
            a = e.isDisabled,
            s = void 0 !== a && a,
            l = e.isAlert,
            i = void 0 !== l && l,
            c = e.size,
            _ = void 0 === c ? Jt.medium : c,
            d = e.type,
            m = void 0 === d ? Qt.primary : d,
            E = e.soundHover,
            p = void 0 === E ? "highlight" : E,
            b = e.soundClick,
            g = void 0 === b ? "play" : b,
            A = e.onMouseEnter,
            C = e.onMouseLeave,
            h = e.onMouseUp,
            v = e.onMouseDown,
            F = e.onClick,
            D = e.onChange,
            B = e.onFocus,
            w = e.onBlur,
            y = e.text,
            S = e.contentStyles,
            k = e.children,
            T = e.alignment,
            N = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, tu);
          const I = (0, r.useState)(!1),
            M = I[0],
            x = I[1],
            O = (0, r.useState)(!1),
            R = (O[0], O[1]),
            L = (0, r.useCallback)(
              (e) => {
                s || (D && D(), F && F(e));
              },
              [s, D, F],
            ),
            P = (0, r.useCallback)(
              (e) => {
                const t = e.button === Kt.LEFT;
                s || (t && x(!0), t && v && v(e), g && Fe(g));
              },
              [s, v, g],
            ),
            H = (0, r.useCallback)(
              (e) => {
                s || (x(!1), h && h(e));
              },
              [s, h],
            ),
            z = (0, r.useCallback)(
              (e) => {
                s || (A && A(e), p && Fe(p));
              },
              [s, A, p],
            ),
            W = (0, r.useCallback)(
              (e) => {
                s || (x(!1), C && C(e));
              },
              [s, C],
            ),
            U = (0, r.useCallback)(
              (e) => {
                s || (R(!0), B && B(e));
              },
              [s, B],
            ),
            V = (0, r.useCallback)(
              (e) => {
                s || (R(!1), w && w(e));
              },
              [s, w],
            ),
            j = o().createElement(
              "div",
              { className: Zt.label },
              o().createElement(
                "div",
                { className: f()(Zt.labelContent, "s-labelContent"), style: S },
                y || k,
              ),
            );
          return o().createElement(
            "div",
            uu(
              {
                id: t,
                className: f()(Zt.base, Zt[`base__${_}`], Zt[`base__${m}`], {
                  [Zt.base__checked]: n,
                  [Zt.base__disabled]: s,
                  [Zt.base__mouseDown]: M,
                  [Zt.base__alert]: i,
                  [Zt.base__center]: T === eu.Center,
                  [Zt.base__bottom]: T === eu.Bottom,
                }),
                onClick: L,
                onMouseEnter: z,
                onMouseLeave: W,
                onMouseDown: P,
                onMouseUp: H,
                onFocus: U,
                onBlur: V,
              },
              N,
            ),
            o().createElement(
              "div",
              { className: Zt.input },
              o().createElement("div", { className: Zt.alertOverlay }),
              o().createElement("div", { className: Zt.inputHoverOverlay }),
              o().createElement("div", { className: Zt.highlight }),
            ),
            o().createElement("div", { className: Zt.checkmark }),
            ((y || k) && j) || null,
          );
        };
        let au, ru, ou;
        (!(function (e) {
          ((e.small = "small"),
            (e.big = "big"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(au || (au = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(ru || (ru = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(ou || (ou = {})));
        class su extends o().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = G.B3.GOLD;
            else e = G.B3.INTEGRAL;
            const t = G.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        su.defaultProps = { format: "integral" };
        const lu = {
            base: "Currency_base_57",
            icon: "Currency_icon_c5",
            base__small: "Currency_base__small_af",
            base__big: "Currency_base__big_bc",
            base__large: "Currency_base__large_65",
            base__extraLarge: "Currency_base__extraLarge_4d",
            "icon__credits-small": "Currency_icon__credits-small_9b",
            "icon__credits-big": "Currency_icon__credits-big_96",
            "icon__credits-large": "Currency_icon__credits-large_ac",
            "icon__credits-extraLarge": "Currency_icon__credits-extraLarge_16",
            "icon__gold-small": "Currency_icon__gold-small_86",
            "icon__gold-big": "Currency_icon__gold-big_15",
            "icon__gold-large": "Currency_icon__gold-large_36",
            "icon__gold-extraLarge": "Currency_icon__gold-extraLarge_a0",
            "icon__crystal-small": "Currency_icon__crystal-small_27",
            "icon__crystal-big": "Currency_icon__crystal-big_cd",
            "icon__crystal-large": "Currency_icon__crystal-large_d3",
            "icon__crystal-extraLarge": "Currency_icon__crystal-extraLarge_09",
            "icon__xp-small": "Currency_icon__xp-small_a7",
            "icon__xp-big": "Currency_icon__xp-big_97",
            "icon__xp-large": "Currency_icon__xp-large_6b",
            "icon__xp-extraLarge": "Currency_icon__xp-extraLarge_67",
            "icon__freeXP-small": "Currency_icon__freeXP-small_ca",
            "icon__freeXP-big": "Currency_icon__freeXP-big_21",
            "icon__freeXP-large": "Currency_icon__freeXP-large_c8",
            "icon__freeXP-extraLarge": "Currency_icon__freeXP-extraLarge_58",
            "icon__equipCoin-small": "Currency_icon__equipCoin-small_32",
            "icon__equipCoin-big": "Currency_icon__equipCoin-big_79",
            "icon__equipCoin-large": "Currency_icon__equipCoin-large_2c",
            "icon__equipCoin-extraLarge": "Currency_icon__equipCoin-extraLarge_8a",
            value: "Currency_value_e1",
            value__freeXP: "Currency_value__freeXP_cb",
            value__credits: "Currency_value__credits_76",
            value__gold: "Currency_value__gold_dd",
            value__xp: "Currency_value__xp_b0",
            value__crystal: "Currency_value__crystal_19",
            value__equipCoin: "Currency_value__equipCoin_d0",
            value__notEnough: "Currency_value__notEnough_56",
            stock: "Currency_stock_87",
            stock__indent: "Currency_stock__indent_a1",
            stock__interactive: "Currency_stock__interactive_93",
            stockBackground: "Currency_stockBackground_82",
          },
          iu = ({
            isDiscount: e,
            isInteractiveDiscount: t,
            size: u,
            type: n,
            isEnough: a,
            value: r,
            discountValue: s,
            showPlus: l,
            stockBackgroundName: i = ou.Red,
          }) => {
            const c = f()(lu.value, lu[`value__${n}`], !a && lu.value__notEnough),
              _ = f()(lu.icon, lu[`icon__${n}-${u}`]),
              d = f()(lu.stock, s && lu.stock__indent, t && lu.stock__interactive),
              m = l && r > 0 && "+",
              E = f()(lu.base, lu[`base__${u}`]);
            return o().createElement(
              "span",
              { className: E },
              o().createElement(
                "span",
                { className: c },
                m,
                o().createElement(su, { value: r, format: n === ru.gold ? "gold" : "integral" }),
              ),
              o().createElement("span", { className: _ }),
              e &&
                o().createElement(
                  "span",
                  { className: d },
                  o().createElement("span", {
                    className: lu.stockBackground,
                    style: { backgroundImage: `url(R.images.gui.maps.icons.library.${i})` },
                  }),
                  Boolean(s) && s,
                ),
            );
          };
        iu.defaultProps = { isEnough: !0 };
        const cu = o().memo(iu),
          _u = "Tutorial_tutorial_ce",
          du = "Tutorial_tutorial_border_ab",
          mu = "Tutorial_tutorial__hidden_8a",
          Eu = "Tutorial_tutorial_hint_bc",
          pu = "Tutorial_tutorial_hintSubstrate_c7",
          bu = "Tutorial_tutorial_hintArrow_75",
          gu = "Tutorial_tutorial_hintText_b5";
        class Au extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.onClick = () => {
                !this.props.isHidden && this.props.onClick && this.props.onClick();
              }));
          }
          componentDidMount() {
            this.handlerID = document.addEventListener("click", () => {
              this.props.onCancel && this.props.onCancel();
            });
          }
          componentWillUnmount() {
            document.removeEventListener("click", this.handlerID);
          }
          render() {
            const e = f()(_u, { [mu]: this.props.isHidden });
            return o().createElement(
              "div",
              { className: e, onClick: this.onClick },
              o().createElement("div", { className: du }),
              o().createElement(
                "div",
                { className: Eu },
                o().createElement("div", { className: pu }),
                o().createElement("div", { className: bu }),
                o().createElement("div", { className: gu }, this.props.text),
              ),
            );
          }
        }
        const Cu = "HangarCounter_base_43",
          fu = "HangarCounter_currencyWrapper_cb",
          hu = "HangarCounter_hangarIcon_46",
          vu = (0, r.memo)(({ count: e }) => {
            const t = Et().mediaSize <= _t.Small ? au.small : au.big;
            return o().createElement(
              "div",
              { className: Cu },
              o().createElement(
                "div",
                { className: fu },
                o().createElement(cu, { value: e, size: t, type: "equipCoin" }),
              ),
              o().createElement("div", { className: hu }),
            );
          }),
          Fu = "CartPanel_base_e7",
          Du = "CartPanel_base__onlyRightSide_f7",
          Bu = "CartPanel_leftSide_d1",
          wu = "CartPanel_checkboxContainer_32",
          yu = "CartPanel_rightSide_12",
          Su = "CartPanel_setupButton_b9",
          ku = "CartPanel_deleteButton_b0",
          Tu = "CartPanel_deleteButtonIcon_77",
          Nu = "CartPanel_backButton_ee",
          Iu = "CartPanel_backButtonIcon_f2",
          Mu = "CartPanel_amountWrapper_f1",
          xu = "CartPanel_amountGold_c6",
          Ou = "CartPanel_amountRent_c7",
          Ru = "CartPanel_amountCredits_7b",
          Lu = "CartPanel_amountEquipment_5b",
          Pu = "CartPanel_rentCount_11",
          Hu = R.strings.customization,
          zu = R.strings.vehicle_customization.customization,
          Wu = R.strings.customization.tooltips.cart,
          Uu = (0, r.memo)(
            ({
              price: e,
              onResetHandler: t,
              onBackHandler: u,
              onApplyHandler: n,
              onAutoRentChange: a,
              onAutoRentHintClose: s,
              cartParams: l,
              buttonSize: i,
              className: c,
            }) => {
              const _ = (0, r.useState)(!1),
                d = _[0],
                m = _[1],
                E = Et().mediaSize <= _t.Small ? au.small : au.big,
                p = ((e) =>
                  Array.from(e.values()).reduce((e, t) => {
                    if ("object" == typeof t && null !== t) {
                      const u = t.name,
                        n = t.value;
                      e[u] = (e[u] || 0) + n;
                    }
                    return e;
                  }, {}))(e),
                b = [
                  l.isEnoughMoney ? "" : Wu.BuyButtonDisabledNotEnoughMoney(),
                  l.isVehicleCustomized || l.buyButtonEnabled ? "" : Wu.buyButtonDisabledDefault(),
                  l.isLockedItem ? zu.lockedItemsApply() : "",
                ].filter((e) => e.length > 0)[0],
                g = l.isRentable && a,
                A = (0, r.useCallback)(() => {
                  (l.showAutoRentHint && (m(!0), s && s()), a && a());
                }, [l.showAutoRentHint, a, s]);
              return o().createElement(
                "div",
                { className: f()(Fu, c, !g && Du) },
                g &&
                  o().createElement(
                    "div",
                    { className: Bu },
                    l.showAutoRentHint &&
                      o().createElement(Au, {
                        text: R.strings.tutorial.customization.autoprolongation(),
                        isHidden: d,
                      }),
                    o().createElement(
                      "div",
                      { className: wu },
                      o().createElement(nu, {
                        isChecked: l.isAutoRentSelected,
                        size: "medium",
                        text: R.strings.vehicle_customization.window.purchase.autoProlongationLabel(),
                        type: "primary",
                        soundHover: "highlight",
                        soundClick: "play",
                        onChange: A,
                      }),
                    ),
                  ),
                o().createElement(
                  "div",
                  { className: yu },
                  o().createElement(
                    "div",
                    { className: Mu },
                    l.inStorageCount > 0 &&
                      o().createElement(
                        "div",
                        { className: Lu },
                        o().createElement(vu, { count: l.inStorageCount }),
                      ),
                    l.isRentable &&
                      ((null == p ? void 0 : p.gold) || (null == p ? void 0 : p.credits)) &&
                      !l.inStorageCount &&
                      o().createElement(
                        "div",
                        { className: Ou },
                        o().createElement(
                          "div",
                          { className: Pu },
                          o().createElement(Wt, {
                            text: `${l.rentCount} ${Hu.cartPanel.rentAmountLabel()}`,
                          }),
                        ),
                      ),
                    l.isGoldPrice
                      ? (null == p ? void 0 : p.gold) &&
                          o().createElement(
                            "div",
                            { className: xu },
                            o().createElement(cu, {
                              value: null == p ? void 0 : p.gold,
                              size: E,
                              type: ru.gold,
                              isEnough: l.isEnoughMoney,
                            }),
                          )
                      : (null == p ? void 0 : p.credits) &&
                          o().createElement(
                            "div",
                            { className: Ru },
                            o().createElement(cu, {
                              value: null == p ? void 0 : p.credits,
                              size: E,
                              type: ru.credits,
                              isEnough: l.isEnoughMoney,
                            }),
                          ),
                  ),
                  (l.clearButtonEnabled || l.cancelButtonEnabled) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      o().createElement(
                        Le,
                        {
                          body: l.cancelButtonEnabled
                            ? Wu.cancelButtonEnabled()
                            : Wu.cancelButtonDisabled(),
                        },
                        o().createElement(
                          "div",
                          null,
                          o().createElement(
                            ke,
                            {
                              type: we.ghost,
                              size: i,
                              mixClass: Nu,
                              onClick: u,
                              disabled: !l.cancelButtonEnabled,
                            },
                            o().createElement("div", { className: Iu }),
                          ),
                        ),
                      ),
                      o().createElement(
                        Le,
                        {
                          body: l.clearButtonEnabled
                            ? Wu.clearButtonEnabled()
                            : Wu.clearButtonDisabled(),
                        },
                        o().createElement(
                          "div",
                          null,
                          o().createElement(
                            ke,
                            {
                              type: we.ghost,
                              size: i,
                              mixClass: ku,
                              onClick: t,
                              soundClick: "cust_select_remove",
                              disabled: !l.clearButtonEnabled,
                            },
                            o().createElement("div", { className: Tu }),
                          ),
                        ),
                      ),
                    ),
                  o().createElement(
                    Le,
                    {
                      body: b || "",
                      isEnabled: l.isEnoughMoney
                        ? !l.isApplyButton && (null == b ? void 0 : b.length) > 0
                        : !l.buyButtonEnabled && (null == b ? void 0 : b.length) > 0,
                    },
                    o().createElement(
                      "div",
                      null,
                      o().createElement(
                        ke,
                        {
                          type: we.main,
                          size: i,
                          mixClass: Su,
                          disabled: !l.buyButtonEnabled,
                          onClick: n,
                        },
                        o().createElement(Wt, {
                          text: l.isApplyButton
                            ? Hu.cartPanel.applyButton()
                            : Hu.cartPanel.setupButton(),
                        }),
                      ),
                    ),
                  ),
                ),
              );
            },
          ),
          Vu = {
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
          ju = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function $u() {
          return (
            ($u =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            $u.apply(this, arguments)
          );
        }
        const Gu = (e) => {
          let t = e.size,
            u = e.value,
            n = e.isEmpty,
            a = e.fadeInAnimation,
            r = e.hide,
            s = e.maximumNumber,
            l = e.className,
            i = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, ju);
          const c = n ? null : u,
            _ = "string" == typeof c;
          if ((c && !_ && c < 0) || 0 === c) return null;
          const d = c && !_ && c > s,
            m = f()(
              Vu.base,
              Vu[`base__${t}`],
              a && Vu.base__animated,
              r && Vu.base__hidden,
              !c && Vu.base__pattern,
              n && Vu.base__empty,
              l,
            );
          return o().createElement(
            "div",
            $u({ className: m }, i),
            o().createElement("div", { className: Vu.bg }),
            o().createElement("div", { className: Vu.pattern }),
            o().createElement(
              "div",
              { className: f()(Vu.value, _ && Vu.value__text) },
              d ? s : c,
              d && o().createElement("span", { className: Vu.plus }, "+"),
            ),
          );
        };
        Gu.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const qu = {
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
        var Xu;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(Xu || (Xu = {}));
        const Yu = ["__left", "__right", "__top", "__bottom"],
          Ku =
            ((0, r.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: t, onOutsideClick: u, customStyles: n = {} },
                a,
              ) => {
                const s = (0, r.useRef)(null),
                  l = (0, r.useRef)(null),
                  i = (0, r.useRef)(null),
                  c = (0, r.useState)(window.decorator && window.decorator.directionType),
                  _ = c[0],
                  m = c[1],
                  E = (0, r.useCallback)(() => {
                    (De.playClick(), d.O.view.sendEvent.close());
                  }, []),
                  p = (0, r.useCallback)(() => {
                    De.playHighlight();
                  }, []),
                  b = f()(qu.arrow, qu[`arrow${Yu[_]}`]);
                Xt(
                  () => (
                    d.O.client.events.mouse.enableOutside(),
                    d.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (u ? u() : d.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const g = (0, r.useCallback)(
                    (e) => {
                      let t = e.target;
                      do {
                        if (t === s.current || t === i.current) return;
                        t = t.parentNode;
                      } while (t);
                      const n = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = d.O.client.getMouseGlobalPosition(),
                          t = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                          u =
                            e.x < n.boundX ||
                            e.x > n.boundX + n.boundWidth ||
                            e.y > n.boundY + n.boundHeight ||
                            e.y < n.boundY;
                        if (t && !u) return;
                      }
                      u ? u() : d.O.view.sendEvent.close("popover");
                    },
                    [s, i, u],
                  ),
                  A = (0, r.useCallback)(
                    () => (
                      d.O.view.freezeTextureBeforeResize(),
                      Pe(() => {
                        if (l.current) {
                          const e = l.current.scrollWidth,
                            t = l.current.scrollHeight;
                          (d.O.view.resize(e, t), m(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, r.useImperativeHandle)(a, () => ({ updateSize: A })),
                  Xt(() => {
                    d.O.view.setInputPaddingsRem(58);
                  }),
                  (0, r.useEffect)(() => {
                    document.addEventListener("mousedown", g, { capture: !0 });
                    const e = ((e) => {
                      let t = !1;
                      return {
                        promise: new Promise((u, n) => {
                          e.then((e) => !t && u(e)).catch((e) => !t && n(e));
                        }),
                        cancel() {
                          t = !0;
                        },
                      };
                    })((0, G.Eu)());
                    return (
                      !t && e.promise.then(() => A()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", g));
                      }
                    );
                  }, [A, g, t]),
                  o().createElement(
                    "div",
                    { className: qu.base, ref: l },
                    o().createElement(
                      "div",
                      { className: qu.decorator },
                      o().createElement(
                        "div",
                        { className: qu.content, ref: s },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          o().createElement(
                            Le,
                            { body: R.strings.dialogs.common.error.cancel() },
                            o().createElement("div", {
                              className: qu.closeBtn,
                              onClick: E,
                              onMouseEnter: p,
                              ref: i,
                            }),
                          ),
                      ),
                      o().createElement("div", { className: b, style: n.arrow }),
                    ),
                  )
                );
              },
            ),
            [
              "contentId",
              "decoratorId",
              "direction",
              "targetId",
              "args",
              "onClick",
              "children",
              "isEnabled",
            ]);
        function Zu() {
          return (
            (Zu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Zu.apply(this, arguments)
          );
        }
        const Ju = (e) => {
          let t = e.contentId,
            u = e.decoratorId,
            n = e.direction,
            a = void 0 === n ? Xu.Top : n,
            s = e.targetId,
            l = e.args,
            i = e.onClick,
            c = e.children,
            _ = e.isEnabled,
            d = void 0 === _ || _,
            m = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, Ku);
          const E = (0, r.useRef)(null),
            p = (0, r.useCallback)(() => {
              if ((0, G.wU)()) return (0, G.SW)();
              E.current && (0, G.P3)(t, a, E.current, u, s, l);
            }, [t, a, l, u, s]);
          return o().createElement(
            "div",
            Zu(
              {
                ref: E,
                onClick:
                  ((b = c.props.onClick),
                  (e) => {
                    d && (p(), i && i(e), b && b(e));
                  }),
              },
              m,
            ),
            c,
          );
          var b;
        };
        let Qu, en;
        (!(function (e) {
          ((e.Default = "default"),
            (e.Nation = "nation"),
            (e.Location = "location"),
            (e.TankmanRole = "tankmanRole"),
            (e.TankmanKind = "tankmanKind"),
            (e.VehicleGrade = "vehicleGrade"),
            (e.VehicleTier = "vehicleTier"),
            (e.VehicleType = "vehicleType"),
            (e.PersonalDataType = "personalDataType"),
            (e.VehicleCD = "vehicle"));
        })(Qu || (Qu = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"));
          })(en || (en = {})));
        const tn = {
            base: "RadioButton_base_d9",
            base__disabled: "RadioButton_base__disabled_84",
            input: "RadioButton_input_24",
            base__small: "RadioButton_base__small_71",
            base__medium: "RadioButton_base__medium_d8",
            blank: "RadioButton_blank_b5",
            blankHover: "RadioButton_blankHover_5e",
            blankMousedown: "RadioButton_blankMousedown_0e",
            check: "RadioButton_check_f2",
            checkHover: "RadioButton_checkHover_c6",
            checkMousedown: "RadioButton_checkMousedown_a7",
            transition: "RadioButton_transition_b3",
            base__blank: "RadioButton_base__blank_46",
            base__blankHover: "RadioButton_base__blankHover_9a",
            base__blankMousedown: "RadioButton_base__blankMousedown_cd",
            base__check: "RadioButton_base__check_fe",
            base__checkHover: "RadioButton_base__checkHover_2f",
            base__checkMousedown: "RadioButton_base__checkMousedown_83",
            label: "RadioButton_label_7f",
          },
          un = [
            "children",
            "labelRenderer",
            "value",
            "currentValue",
            "autofocus",
            "disabled",
            "size",
            "label",
            "soundHover",
            "soundClick",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseUp",
            "onMouseDown",
            "onClick",
            "onChange",
            "onFocus",
            "onBlur",
          ];
        function nn() {
          return (
            (nn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            nn.apply(this, arguments)
          );
        }
        const an = (0, r.memo)((e) => {
            let t = e.children,
              u = e.labelRenderer,
              n = e.value,
              a = e.currentValue,
              s = e.autofocus,
              l = void 0 !== s && s,
              i = e.disabled,
              c = void 0 !== i && i,
              _ = e.size,
              d = void 0 === _ ? en.Medium : _,
              m = e.label,
              E = e.soundHover,
              p = void 0 === E ? "highlight" : E,
              b = e.soundClick,
              g = void 0 === b ? "play" : b,
              A = e.onMouseEnter,
              C = e.onMouseLeave,
              h = e.onMouseUp,
              v = e.onMouseDown,
              F = e.onClick,
              D = e.onChange,
              B = e.onFocus,
              w = e.onBlur,
              y = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, un);
            const S = n === a,
              k = (0, r.useState)(!1),
              T = k[0],
              N = k[1],
              I = (0, r.useState)(!1),
              M = I[0],
              x = I[1],
              O = (0, r.useState)(l),
              R = O[0],
              L = O[1],
              P = (0, r.useRef)(null),
              H = (0, r.useCallback)(() => {
                !c && P.current && (P.current.focus(), L(!0));
              }, [c]),
              z = (0, r.useCallback)(
                (e) => {
                  R && null !== P.current && !P.current.contains(e.target) && L(!1);
                },
                [R],
              );
            ((0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", z),
                () => {
                  document.removeEventListener("mousedown", z);
                }
              ),
              [z],
            ),
              (0, r.useEffect)(() => {
                L(l);
              }, [l]));
            const W = (0, r.useCallback)(
                (e) => {
                  c || (D && D(n), F && F(n, e));
                },
                [c, D, F, n],
              ),
              U = (0, r.useCallback)(
                (e) => {
                  if (!c) {
                    const t = e.button === Kt.LEFT;
                    (t && N(!0), t && v && v(n, e), g && Fe(g), l && H());
                  }
                },
                [l, c, v, H, g, n],
              ),
              V = (0, r.useCallback)(
                (e) => {
                  c || (N(!1), h && h(n, e));
                },
                [c, h, n],
              ),
              j = (0, r.useCallback)(
                (e) => {
                  c || (A && A(n, e), p && Fe(p), x(!0));
                },
                [c, A, p, n],
              ),
              $ = (0, r.useCallback)(
                (e) => {
                  c || (N(!1), x(!1), C && C(n, e));
                },
                [c, C, n],
              ),
              G = (0, r.useCallback)(
                (e) => {
                  c || (L(!0), B && B(n, e));
                },
                [c, B, n],
              ),
              q = (0, r.useCallback)(
                (e) => {
                  c || (L(!1), w && w(n, e));
                },
                [c, w, n],
              ),
              X = f()(tn.base, tn[`base__${d}`], {
                [tn.base__blank]: !S && !M,
                [tn.base__blankHover]: !S && M && !T,
                [tn.base__blankMousedown]: !S && M && T,
                [tn.base__check]: S && !M,
                [tn.base__checkHover]: S && M && !T,
                [tn.base__checkMousedown]: S && M && T,
                [tn.base__focused]: R,
                [tn.base__disabled]: c,
              }),
              Y = (0, r.useMemo)(
                () => ({ isHovered: M, isMouseDown: T, isFocused: R, isChecked: S }),
                [M, T, R, S],
              ),
              K = (0, r.useRef)(tn.blank),
              Z = (0, r.useRef)(tn.blankHover),
              J = (0, r.useRef)(tn.blankMousedown),
              Q = (0, r.useRef)(tn.check),
              ee = (0, r.useRef)(tn.checkHover),
              te = (0, r.useRef)(tn.checkMousedown);
            return (
              (0, r.useEffect)(
                Pe(() => {
                  ((K.current = f()(tn.blank, tn.transition)),
                    (Z.current = f()(tn.blankHover, tn.transition)),
                    (J.current = f()(tn.blankMousedown, tn.transition)),
                    (Q.current = f()(tn.check, tn.transition)),
                    (ee.current = f()(tn.checkHover, tn.transition)),
                    (te.current = f()(tn.checkMousedown, tn.transition)));
                }),
                [],
              ),
              o().createElement(
                "div",
                nn(
                  {
                    ref: P,
                    className: X,
                    onClick: W,
                    onMouseEnter: j,
                    onMouseLeave: $,
                    onMouseDown: U,
                    onMouseUp: V,
                    onFocus: G,
                    onBlur: q,
                  },
                  y,
                ),
                o().createElement(
                  "div",
                  { className: tn.input },
                  o().createElement("div", { className: K.current }),
                  o().createElement("div", { className: Z.current }),
                  o().createElement("div", { className: J.current }),
                  o().createElement("div", { className: Q.current }),
                  o().createElement("div", { className: ee.current }),
                  o().createElement("div", { className: te.current }),
                ),
                o().createElement("div", { className: tn.label }, m || t || (u && u(Y))),
              )
            );
          }),
          rn = "RadioGroup_base_6e",
          on = "RadioGroup_radio_3b",
          sn = "RadioGroup_label_86",
          ln = (0, r.memo)(({ data: e, selectedValue: t, onClickHandler: u }) => {
            const n = (0, r.useState)(t),
              a = n[0],
              s = n[1],
              l = (0, r.useCallback)(
                (t) => {
                  t && (s(t), void 0 !== u && u(e[0].name, t));
                },
                [e, u],
              );
            return (
              (0, r.useEffect)(() => {
                s(t);
              }, [t]),
              o().createElement(
                "div",
                { className: rn },
                null == e
                  ? void 0
                  : e.map((e) =>
                      o().createElement(
                        "div",
                        { className: on, key: e.id },
                        o().createElement(
                          Le,
                          { header: e.tooltipHeader, body: e.tooltipBody },
                          o().createElement(
                            an,
                            { value: e.value, currentValue: a, onClick: () => l(e.value) },
                            o().createElement(Wt, { className: sn, text: e.label }),
                          ),
                        ),
                      ),
                    ),
              )
            );
          }),
          cn = ["children"];
        function _n() {
          return (
            (_n =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            _n.apply(this, arguments)
          );
        }
        const dn = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, cn);
          return o().createElement(
            Me,
            _n(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              u,
            ),
            t,
          );
        };
        function mn() {
          return (
            (mn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            mn.apply(this, arguments)
          );
        }
        const En = ({ children: e, tooltipArgs: t, className: u }) => {
          if (!t) return e;
          const n = o().createElement("div", { className: u }, e);
          if (t.header || t.body) return o().createElement(Le, t, n);
          const a = t.contentId,
            r = t.args,
            s = null == r ? void 0 : r.contentId;
          return a || s
            ? o().createElement(Me, mn({}, t, { contentId: a || s }), n)
            : o().createElement(dn, t, n);
        };
        function pn(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function bn(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, u, n) => t(null == e ? void 0 : e.value, u, n));
        }
        function gn(e, t) {
          for (let u = 0; u < e.length; u++) {
            const n = pn(e[u]);
            if (t(n, u, e)) return n;
          }
        }
        const An = "ToggleButton_base_19",
          Cn = "ToggleButton_overlay_6b",
          fn = "ToggleButton_base__active_6c",
          hn = "ToggleButton_button_1c",
          vn = "ToggleButton_indicator_9b",
          Fn = "ToggleButton_counter_63",
          Dn = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function Bn() {
          return (
            (Bn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Bn.apply(this, arguments)
          );
        }
        const wn = o().memo(function (e) {
            let t = e.isActive,
              u = e.counter,
              n = e.className,
              a = e.children,
              r = e.type,
              s = void 0 === r ? we.secondary : r,
              l = e.size,
              i = void 0 === l ? ye.small : l,
              c = e.hasIndicator,
              _ = void 0 === c || c,
              d = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Dn);
            return o().createElement(
              "div",
              { className: f()(An, n, t && fn) },
              o().createElement(ke, Bn({ type: s, size: i, mixClass: hn }, d), a),
              o().createElement("div", { className: Cn }),
              _ && o().createElement("div", { className: vn }),
              Boolean(u) &&
                o().createElement(
                  "div",
                  { className: Fn },
                  o().createElement(Gu, { value: u, size: "small" }),
                ),
            );
          }),
          yn = "FilterTitle_base_53",
          Sn = "FilterTitle_label_14",
          kn = "FilterTitle_discount_49",
          Tn = "FilterTitle_discountIcon_d4",
          Nn = ({ label: e, hasDiscount: t, className: u }) =>
            o().createElement(
              "div",
              { className: f()(yn, u) },
              o().createElement("div", { className: Sn }, e),
              t &&
                o().createElement(
                  "div",
                  { className: kn },
                  o().createElement("div", { className: Tn }),
                ),
            ),
          In = "ToggleIcon_base_31",
          Mn = "ToggleIcon_base__small_0e",
          xn = "ToggleIcon_icon_9e",
          On = o().memo(function ({ icon: e, iconParams: t, isSmall: u = !1, classNames: n }) {
            return o().createElement(
              "div",
              { className: f()(In, null == n ? void 0 : n.base, u && Mn) },
              o().createElement("div", {
                className: f()(xn, null == n ? void 0 : n.icon),
                style: {
                  backgroundImage: `url(${e})`,
                  width: (null == t ? void 0 : t.iconWidth) || "inherit",
                  height: (null == t ? void 0 : t.iconHeight) || "inherit",
                },
              }),
            );
          }),
          Rn = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          Ln = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Pn = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          Hn = (e) =>
            Pn
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let u = Ln.length - 1; u >= 0; u--)
                    for (; e >= Ln[u];) ((t += Rn[u]), (e -= Ln[u]));
                  return t;
                })(e),
          zn = "VehicleTier_base_99",
          Wn = "VehicleTier_base__small_67",
          Un = ({ level: e, isSmall: t = !1 }) =>
            o().createElement("div", { className: f()(zn, t && Wn) }, Hn(e)),
          Vn = {
            icon__vehicleType: "ToggleButtonIcon_icon__vehicleType_6d",
            icon__nation: "ToggleButtonIcon_icon__nation_76",
            icon__vehicleGradePrimary: "ToggleButtonIcon_icon__vehicleGradePrimary_40",
            icon__tankmanRole: "ToggleButtonIcon_icon__tankmanRole_f4",
            icon__selected: "ToggleButtonIcon_icon__selected_29",
            icon__tankmanKind: "ToggleButtonIcon_icon__tankmanKind_44",
            icon__vehicleGradeElite: "ToggleButtonIcon_icon__vehicleGradeElite_de",
            icon__locationRecruit: "ToggleButtonIcon_icon__locationRecruit_85",
            icon__locationTankman: "ToggleButtonIcon_icon__locationTankman_02",
            icon__locationUnique: "ToggleButtonIcon_icon__locationUnique_aa",
            icon__personalDataType: "ToggleButtonIcon_icon__personalDataType_ed",
            icon__tankmanKindDismissed: "ToggleButtonIcon_icon__tankmanKindDismissed_d8",
            icon__vehicleGradePremium: "ToggleButtonIcon_icon__vehicleGradePremium_ec",
          },
          jn = ({
            id: e,
            icon: t,
            iconParams: u,
            type: n,
            isSmall: a = !0,
            isSelected: r = !1,
            baseClassName: s = "",
            iconClassName: l = "",
          }) =>
            n === Qu.VehicleTier
              ? o().createElement(Un, { isSmall: a, level: Number(e) })
              : o().createElement(On, {
                  icon: t,
                  isSmall: a,
                  iconParams: u,
                  classNames: {
                    icon: f()(Vn[`icon__${n}`], Vn[`icon__${n}${P(e)}`], r && Vn.icon__selected, l),
                    base: s,
                  },
                }),
          $n = {
            base: "FilterToggleGroup_base_bd",
            title: "FilterToggleGroup_title_5c",
            content: "FilterToggleGroup_content_1b",
            toggle: "FilterToggleGroup_toggle_c2",
            base__inPopup: "FilterToggleGroup_base__inPopup_51",
          },
          Gn = ["id", "isSelected", "tooltip", "icon", "counter"];
        function qn() {
          return (
            (qn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            qn.apply(this, arguments)
          );
        }
        let Xn;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(Xn || (Xn = {}));
        const Yn = ({ header: e, body: t, contentId: u, targetId: n }) =>
            u
              ? { contentId: u, targetId: n }
              : t || e
                ? { header: null != e ? e : void 0, body: null != t ? t : void 0 }
                : void 0,
          Kn = ({
            id: e,
            type: t,
            label: u,
            hasDiscount: n,
            filters: a,
            onClick: r,
            className: s,
            toggleProps: l,
            theme: i = Xn.Default,
          }) => {
            const c = i === Xn.InPopup;
            return o().createElement(
              "div",
              { className: f()($n.base, $n[`base__${i}`], s) },
              c && o().createElement(Nn, { className: $n.title, label: u, hasDiscount: n }),
              o().createElement(
                "div",
                { className: $n.content },
                bn(a, (u) => {
                  let n = u.id,
                    a = u.isSelected,
                    s = u.tooltip,
                    i = u.icon,
                    _ = u.counter;
                  const d = (function (e, t) {
                      if (null == e) return {};
                      var u,
                        n,
                        a = {},
                        r = Object.keys(e);
                      for (n = 0; n < r.length; n++)
                        ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                      return a;
                    })(u, Gn),
                    m = d.iconWidth,
                    E = d.iconHeight;
                  return o().createElement(
                    En,
                    { key: n, tooltipArgs: Yn(s), className: $n.toggle },
                    o().createElement(
                      wn,
                      qn({}, l, {
                        className: f()($n.toggle, null == l ? void 0 : l.className),
                        isActive: a,
                        onClick: () => (null == r ? void 0 : r(e, n)),
                        counter: _,
                      }),
                      o().createElement(jn, {
                        id: n,
                        icon: i,
                        iconParams: { iconWidth: m, iconHeight: E },
                        type: t,
                        isSmall: c,
                        isSelected: a,
                        baseClassName: null == l ? void 0 : l.baseClassName,
                        iconClassName: f()(
                          null == l ? void 0 : l.iconClassName,
                          (null == l ? void 0 : l.parentStyles) &&
                            (null == l ? void 0 : l.parentStyles[`icon_${n}`]),
                        ),
                      }),
                    ),
                  );
                }),
              ),
            );
          },
          Zn = () => {
            const e = (0, r.useState)(d.O.view.getScale()),
              t = e[0],
              u = e[1];
            return (
              (0, r.useEffect)(() => {
                const e = () => {
                  u(d.O.view.getScale());
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
          Jn = {
            base: "NumberRange_base_65",
            base__animation: "NumberRange_base__animation_70",
            blinkAnim: "NumberRange_blinkAnim_5f",
            from: "NumberRange_from_45",
            from__red: "NumberRange_from__red_53",
            separatorWrapper: "NumberRange_separatorWrapper_5a",
            separator: "NumberRange_separator_61",
            counterGlow: "NumberRange_counterGlow_f6",
          },
          Qn = R.strings.crew.barracks.berthsAmountDivider(),
          ea = R.strings.crew.filterPanel.counter.selectLimit,
          ta = (0, r.memo)(function ({
            isFilterRange: e,
            from: t,
            to: u,
            className: n,
            isSelectMode: a = !1,
            isSelectedLimitReached: r = !1,
            isHideTotalCounter: s = !1,
            counterGlowShift: l,
            classNames: i,
            isAnimationEnabled: c = !1,
          }) {
            const _ = l
              ? o().createElement(
                  "div",
                  { className: Jn.separatorWrapper },
                  o().createElement(Wt, { className: Jn.separator, text: Qn }),
                  o().createElement("div", {
                    style: l,
                    className: f()(
                      Jn.counterGlow,
                      r && Jn.blink,
                      null == i ? void 0 : i.counterGlow,
                    ),
                  }),
                )
              : o().createElement(Wt, { className: Jn.separator, text: Qn });
            return a
              ? o().createElement(
                  Le,
                  { header: ea.header(), body: ea.body(), ignoreShowDelay: !0 },
                  o().createElement(
                    "div",
                    { className: f()(Jn.base, n) },
                    o().createElement(Wt, { className: Jn.from, text: String(t) }),
                    (t !== u || r) &&
                      o().createElement(
                        o().Fragment,
                        null,
                        _,
                        o().createElement(Wt, { text: String(u) }),
                      ),
                  ),
                )
              : o().createElement(
                  "div",
                  {
                    className: f()(
                      Jn.base,
                      e ? 0 === t && Jn.base__animation : t > u && Jn.base__animation,
                      c && Jn.base__animation,
                      n,
                    ),
                  },
                  o().createElement(Wt, {
                    className: f()(
                      Jn.from,
                      e ? 0 === t && u > 0 && Jn.from__red : t > u && Jn.from__red,
                    ),
                    text: String(t),
                  }),
                  (!s || t !== u) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      _,
                      o().createElement(Wt, { text: String(u) }),
                    ),
                );
          }),
          ua = "NumberRangeWithLabel_base_fd",
          na = "NumberRangeWithLabel_counterGlow_fa",
          aa = "NumberRangeWithLabel_blink_15",
          ra = (0, r.memo)(
            ({
              title: e,
              label: t = "",
              isGlowVisible: u = !1,
              isSelectedLimitReached: n = !1,
              isFilterRange: a = !1,
              isSelectMode: r = !1,
              className: s,
              classNames: l,
              from: i,
              to: c,
              staticCounterGlowShift: _,
              isHideTotalCounter: d = !1,
              isAnimationEnabled: m = !1,
            }) => {
              const E = Zn(),
                p =
                  i !== c || n
                    ? 7 * String(i).length * E + 4 * E
                    : Math.round((7 * String(i).length * E) / 2),
                b = { left: _ || p };
              return o().createElement(
                "div",
                { className: f()(ua, s) },
                t,
                o().createElement(ta, {
                  isFilterRange: a,
                  isSelectedLimitReached: n,
                  isSelectMode: r,
                  from: i,
                  to: c,
                  isHideTotalCounter: d,
                  classNames: l,
                  isAnimationEnabled: m,
                }),
                u &&
                  a &&
                  o().createElement("div", {
                    style: b,
                    className: f()(na, n && aa, null == l ? void 0 : l.counterGlow),
                  }),
                e,
              );
            },
          ),
          oa = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? bn(e, (e) => ("object" == typeof e ? oa(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? oa(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? oa(t) : t]),
                    )
              : e,
          sa = (e) => oa(e);
        var la = u(3946);
        const ia = b()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  carouselModel: e.object("carouselModel"),
                  filterModel: e.object("filterModel"),
                  filterModelStructure: e.object("filterModel.structure"),
                  carouselItemsList: e.array("carouselModel.carouselItemsList"),
                  arrowsList: e.array("carouselModel.arrowsList"),
                  bookmarksList: e.array("carouselModel.bookmarksList"),
                  tabsItemsList: e.array("tabsModel.tabItemsList", []),
                  billModel: e.object("billModel"),
                  buyPrice: e.array("billModel.buyPrice.price"),
                  headerVehicleInfo: e.object("headerVehicleInfoModel"),
                  seasonsTabs: e.object("seasonsModel"),
                  seasonsTabsItems: e.array("seasonsModel.seasonsList"),
                  markersModel: e.object("markersModel"),
                  markers: e.array("markersModel.markersList"),
                  editModeData: e.array("markersModel.editModeData"),
                  availability: e.array("availability"),
                  toolbarModel: e.object("toolbarModel"),
                  toolbarButtonList: e.array("toolbarModel.buttonList"),
                  selectedItemsCounter: e.array("selectedItemsCounter"),
                  hiddenItemsCounter: e.array("hiddenItemsCounter"),
                  stageSwitcherWidgetModel: e.object("stageSwitcherWidgetModel"),
                  customizationTypes: e.object("markersModel.customizationTypes"),
                  magneticToolModel: e.object("magneticToolModel"),
                },
                u = (0, la.Om)(
                  () =>
                    sa(t.carouselItemsList.get()).slice(0, t.carouselModel.get().totalItemsCount),
                  { equals: c },
                ),
                n = (0, la.Om)(() => gn(u(), (e) => e.isSelected), { equals: c }),
                a = (0, la.Om)(
                  () => {
                    var e;
                    return null == (e = n()) ? void 0 : e.intCD;
                  },
                  { equals: c },
                ),
                r = (0, la.Om)(() => sa(t.arrowsList.get()), { equals: c }),
                o = (0, la.Om)(() => sa(t.bookmarksList.get()), { equals: c }),
                s = (0, la.Om)(() => sa(t.tabsItemsList.get()), { equals: c }),
                l = (0, la.Om)(() => gn(s(), (e) => e.isSelected), { equals: c }),
                i = (0, la.Om)(
                  () => {
                    var e;
                    return null == (e = l()) ? void 0 : e.itemType;
                  },
                  { equals: c },
                ),
                _ = (0, la.Om)(() => sa(t.seasonsTabsItems.get()), { equals: c }),
                d = (0, la.Om)(() => sa(t.markers.get()), { equals: c }),
                m = (0, la.Om)(() => sa(t.editModeData.get()), { equals: c }),
                E = (0, la.Om)(() => sa(t.toolbarModel.get()), { equals: c }),
                p = (0, la.Om)(() => sa(t.billModel.get()), { equals: c }),
                b = (0, la.Om)(() => sa(t.buyPrice.get()), { equals: c }),
                g = (0, la.Om)(() => sa(t.stageSwitcherWidgetModel.get()), { equals: c }),
                A = (0, la.Om)(() => sa(t.toolbarButtonList.get()), { equals: c }),
                C = (0, la.Om)(() => sa(t.filterModelStructure.get()), { equals: c });
              return Object.assign({}, t, {
                computes: {
                  getItems: u,
                  getSelectedItem: n,
                  getSelectedItemId: a,
                  getCategories: o,
                  getTabsItemsList: s,
                  getSelectedTab: l,
                  getSelectedTabItemType: i,
                  getSeasonsTabsItemsList: _,
                  getMarkersList: d,
                  getEditData: m,
                  getBillModel: p,
                  getBuyPrice: b,
                  getToolbarButtonsList: A,
                  getArrowsList: r,
                  getStageSwitcher: g,
                  getStructureList: C,
                  getToolbarData: E,
                },
              });
            },
            ({ externalModel: e }) => ({
              onClose: e.createCallbackNoArgs("onClose"),
              onExpandCarousel: e.createCallback((e) => ({ isExpanded: e }), "onExpandCarousel"),
              onSelectItem: e.createCallback((e) => ({ itemId: e }), "onSelectItem"),
              onUnselectItem: e.createCallbackNoArgs("onUnselectItem"),
              hoverItem: e.createCallback((e) => ({ itemId: e }), "onHoverItem"),
              onEditItem: e.createCallback((e) => ({ itemId: e }), "onEditItem"),
              clearFilter: e.createCallbackNoArgs("clearFilter"),
              clickDecalsBanner: e.createCallbackNoArgs("onClickDecalsBanner"),
              moveSpace: e.createCallback((e) => e, "onMoveSpace"),
              selectTab: e.createCallback((e) => ({ tabId: e }), "onSelectTab"),
              hoverTab: e.createCallback((e) => ({ tabId: e }), "onHoverTab"),
              closeEditItem: e.createCallbackNoArgs("onCloseEditItem"),
              onSceneOverChange: e.createCallback(
                (e) => ({ isOver: !(0, G.wU)() && e }),
                "onSceneOverChange",
              ),
              onSceneDraggingChange: e.createCallback(
                (e) => ({ isDragging: e }),
                "onSceneDraggingChange",
              ),
              onSceneClick: e.createCallbackNoArgs("onSceneClick"),
              selectSeason: e.createCallback((e) => ({ seasonName: e }), "onSelectSeason"),
              selectAnchor: e.createCallback(
                (e, t, u) => ({ areaId: e, slotType: t, regionIdx: u }),
                "markersModel.onSelectAnchor",
              ),
              hoverAnchor: e.createCallback(
                (e, t, u, n) => ({ areaId: e, slotType: t, regionIdx: u, hover: n }),
                "markersModel.onHoverAnchor",
              ),
              dragAnchor: e.createCallback(
                (e, t, u) => ({ areaId: e, slotType: t, regionIdx: u }),
                "markersModel.onDragAnchor",
              ),
              onRemoveChar: e.createCallbackNoArgs("markersModel.onRemoveChar"),
              onAddChar: e.createCallback((e) => ({ char: e }), "markersModel.onAddChar"),
              onDeleteAllChars: e.createCallbackNoArgs("markersModel.onDeleteAllChars"),
              onEnterInput: e.createCallbackNoArgs("markersModel.onEnterInput"),
              onApplyToAllSeasonsChange: e.createCallbackNoArgs("onApplyToAllSeasonsChange"),
              onCancelChanges: e.createCallbackNoArgs("billModel.onCancelChanges"),
              onAutoRentHintClose: e.createCallbackNoArgs("billModel.onAutoRentHintClose"),
              onAutoRentChange: e.createCallbackNoArgs("billModel.onAutoRentChange"),
              onClearBasket: e.createCallbackNoArgs("billModel.onClearBasket"),
              onShowBuyWindow: e.createCallbackNoArgs("billModel.onShowBuyWindow"),
              closeBinEsc: e.createCallbackNoArgs("onCloseBinEsc"),
              buyItems: e.createCallbackNoArgs("onBuyItems"),
              onCloseStyleInfoEsc: e.createCallbackNoArgs("onCloseStyleInfoEsc"),
              changeFilter: e.createCallback((e, t) => ({ key: e, value: t }), "changeFilter"),
              onToolbarItemClick: e.createCallback(
                (e, t) => ({ actionType: e, actionData: t }),
                "toolbarModel.onActionBtnClick",
              ),
              progressiveInfoButtonClick: e.createCallbackNoArgs("onProgressiveInfoButtonClick"),
              onStageChange: e.createCallback(
                (e) => ({ selectedLevel: e }),
                "stageSwitcherWidgetModel.onChange",
              ),
              onPressSelectNextItem: e.createCallback(
                (e) => ({ isLeft: e }),
                "onPressSelectNextItem",
              ),
              onRequestItems: e.createCallback(
                (e, t) => ({ startIndex: e, endIndex: t }),
                "onRequestItems",
              ),
              toCustomizationResourceEvent: e.createCallbackNoArgs("toCustomizationResourceEvent"),
            }),
          ),
          ca = (ia[0], ia[1]),
          _a = {
            base: "Filters_base_c3",
            reverse: "Filters_reverse_26",
            filtersPopover: "Filters_filtersPopover_22",
            filtersPopoverUpdate: "Filters_filtersPopoverUpdate_e7",
            filtersPopoverIcon: "Filters_filtersPopoverIcon_bc",
            buttonFavorites: "Filters_buttonFavorites_f4",
            counterWrapper: "Filters_counterWrapper_dd",
            filterNumbers: "Filters_filterNumbers_72",
            filtersClearButton: "Filters_filtersClearButton_eb",
            filtersClearIcon: "Filters_filtersClearIcon_79",
            hiddenItemCounter: "Filters_hiddenItemCounter_d1",
          },
          da = R.strings.customization.tooltips.filters,
          ma = R.strings.customization.filters,
          Ea = R.strings.customization,
          pa = "all",
          ba = "sale",
          ga = "inventory",
          Aa = [
            {
              label: ma.labelAll(),
              id: pa,
              value: pa,
              name: "availability",
              tooltipHeader: da.allRadioHeader(),
              tooltipBody: da.allRadioBody(),
            },
            {
              label: ma.labelStock(),
              id: ga,
              value: ga,
              tooltipHeader: da.stockRadioHeader(),
              tooltipBody: da.stockRadioBody(),
            },
            {
              label: ma.labelSale(),
              id: ba,
              value: ba,
              tooltipHeader: da.saleRadioHeader(),
              tooltipBody: da.saleRadioBody(),
            },
          ],
          Ca = (0, i.Pi)(({ isReverse: e = !1, buttonSize: t }) => {
            const u = ca(),
              n = u.controls,
              a = u.model,
              s = Et().mediaSize,
              l = a.filterModel.get(),
              i = l.availability,
              c = l.filteredItemsCounter,
              _ = l.allItemsCounter,
              d = l.newHiddenItemsCounter,
              m = l.isFilteringActive,
              E = l.favorite,
              p = a.computes.getStructureList,
              b = (0, r.useMemo)(
                () => [
                  {
                    id: "fav1",
                    icon: "R.images.gui.maps.icons.customization.icon_favorites",
                    isSelected: E,
                    counter: 0,
                    tooltip: {
                      header: da.favoritesToggleHeader(),
                      body: da.favoritesToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
                [E],
              ),
              g = (0, r.useCallback)(() => {
                n.changeFilter("favorite", !E);
              }, [n, E]),
              A = e ? Xu.Top : Xu.Bottom;
            return o().createElement(
              "div",
              { className: f()(_a.base, e && _a.reverse) },
              o().createElement(
                "div",
                { className: _a.counterWrapper },
                o().createElement(
                  Ju,
                  {
                    contentId:
                      R.views.lobby.customization.popovers.CustomizationFilterPopoverView("resId"),
                    direction: p().length > 5 && s <= _t.Small ? Xu.Left : A,
                  },
                  o().createElement(
                    "div",
                    null,
                    o().createElement(
                      Le,
                      { header: da.popoverButtonTitle(), body: da.popoverButtonBody() },
                      o().createElement(
                        ke,
                        {
                          type: we.ghost,
                          size: t,
                          mixClass: f()(_a.filtersPopover, e && _a.filtersPopoverUpdate),
                        },
                        o().createElement("div", { className: _a.filtersPopoverIcon }),
                      ),
                    ),
                    d > 0 &&
                      o().createElement(Gu, {
                        size: "normal",
                        value: d,
                        className: _a.hiddenItemCounter,
                      }),
                  ),
                ),
                m &&
                  !e &&
                  o().createElement(ra, {
                    title:
                      m &&
                      o().createElement(
                        Le,
                        { body: Ea.customization.resetFilter.tooltip.text() },
                        o().createElement(
                          ke,
                          {
                            type: we.ghost,
                            onClick: n.clearFilter,
                            mixClass: f()(_a.filtersClearButton),
                          },
                          o().createElement("div", { className: _a.filtersClearIcon }),
                        ),
                      ),
                    from: c,
                    to: _,
                    isFilterRange: !0,
                    isGlowVisible: !0,
                    isSelectMode: !1,
                    isSelectedLimitReached: d > 0,
                    className: _a.filterNumbers,
                    staticCounterGlowShift: -1,
                    isAnimationEnabled: d > 0,
                  }),
              ),
              o().createElement(Kn, {
                id: "favorites",
                label: "",
                type: Qu.Default,
                hasDiscount: !1,
                filters: b,
                toggleProps: { type: we.ghost },
                onClick: g,
                className: f()(_a.buttonFavorites, e && _a.buttonFavoritesBorder),
              }),
              o().createElement(ln, { onClickHandler: n.changeFilter, data: Aa, selectedValue: i }),
            );
          }),
          fa = (e, t) => {
            let u;
            const n = setTimeout(() => {
              u = e();
            }, t);
            return () => {
              ("function" == typeof u && u(), clearTimeout(n));
            };
          },
          ha = (e, t, u) => Math.min(Math.max(e, t), u),
          va = {
            base: "Switcher_base_9c",
            base__hasCurrentText: "Switcher_base__hasCurrentText_57",
            base__small: "Switcher_base__small_96",
            base__isVisible: "Switcher_base__isVisible_02",
          },
          Fa = (e) => ({ transitionDelay: e / 20 + "s" }),
          Da = "SwitcherBullet_base_94",
          Ba = "SwitcherBullet_container_28",
          wa = "SwitcherBullet_base__selected_6e",
          ya = "SwitcherBullet_container__text_ff",
          Sa = "SwitcherBullet_finishedHover_42",
          ka = "SwitcherBullet_base__finished_e2",
          Ta = "SwitcherBullet_base__hover_87",
          Na = "SwitcherBullet_iconSmall_d4",
          Ia = "SwitcherBullet_base__afterCurrent_f6",
          Ma = "SwitcherBullet_iconBig_65",
          xa = "SwitcherBullet_base__currentSelected_eb",
          Oa = "SwitcherBullet_iconText_ca",
          Ra = "SwitcherBullet_iconTextGlow_a0",
          La = "SwitcherBullet_clickArea_84",
          Pa = "SwitcherBullet_base__disabled_2a",
          Ha = "SwitcherBullet_disabled_56",
          za = "SwitcherBullet_number_08",
          Wa = "SwitcherBullet_currentText_b6",
          Ua = "SwitcherBullet_text_e9",
          Va = "SwitcherBullet_texture_b3";
        var ja, $a;
        (!(function (e) {
          ((e.BIG = "big"), (e.SMALL = "small"));
        })(ja || (ja = {})),
          (function (e) {
            ((e.LIGHT = "light"), (e.DARK = "dark"));
          })($a || ($a = {})));
        const Ga = R.images.gui.maps.icons.components.switcher.numbers,
          qa = (0, r.memo)(
            ({
              numberToDisplay: e,
              index: t,
              selectedIndex: u,
              previousSelectedIndex: n,
              onChange: a,
              currentIndex: s,
              currentText: l,
              isDisabled: i = !1,
              mouseEnterSound: c,
              clickSound: _,
            }) => {
              const d = t !== u,
                m = (0, r.useState)(!1),
                E = m[0],
                p = m[1],
                b = (0, r.useCallback)(() => {
                  (p(!0), d && Fe(c));
                }, [d, c]),
                g = (0, r.useCallback)(() => {
                  d && (Fe(_), a(e));
                }, [d, _, e, a]),
                A = (0, r.useCallback)(() => {
                  p(!1);
                }, []),
                C = s || 0,
                h = f()(
                  Da,
                  t === u && wa,
                  t === u && t === C && xa,
                  t > C && t !== u && Ia,
                  t <= C && ka,
                  E && Ta,
                  i && Pa,
                ),
                v = (0, r.useMemo)(
                  () =>
                    ((e, t, u) =>
                      e === t
                        ? Fa(0)
                        : e === u
                          ? Fa(Math.abs(e - t) - 2)
                          : (u > t && e > t && e < u) || (u < t && e < t && e > u)
                            ? Fa(Math.abs(e - t) - 1)
                            : void 0)(t, n, u),
                  [t, n, u],
                ),
                F = (0, r.useCallback)(
                  () => ((t === u && t === C) || t === u ? ja.BIG : ja.SMALL),
                  [t, u, C],
                ),
                D = (0, r.useMemo)(() => {
                  const e = t > C ? $a.LIGHT : $a.DARK;
                  return Object.assign({}, v, {
                    backgroundImage: `url(${Ga.$dyn(`number_${t}_${F()}_${e}`)})`,
                  });
                }, [t, C, v, F]);
              return o().createElement(
                "div",
                { className: h },
                o().createElement(
                  "div",
                  { className: Ba, style: v },
                  o().createElement("div", { className: Sa, style: v }),
                  o().createElement("div", { className: Na, style: v }),
                  o().createElement("div", { className: Ma, style: v }),
                  o().createElement("div", { className: Ha }),
                  o().createElement("div", { className: za, style: D }),
                  o().createElement("div", {
                    className: La,
                    style: v,
                    onClick: g,
                    onMouseEnter: b,
                    onMouseLeave: A,
                  }),
                ),
                l && t === s && o().createElement("div", { className: Wa }, l),
              );
            },
          ),
          Xa = ({
            numberToDisplay: e,
            index: t,
            selectedIndex: u,
            previousSelectedIndex: n,
            onChange: a,
            currentIndex: s = 0,
            isDisabled: l = !1,
            mouseEnterSound: i,
            clickSound: c,
            styleID: _,
          }) => {
            const d = t === u,
              m = (0, r.useState)(!1),
              E = m[0],
              p = m[1],
              b = (0, r.useCallback)(() => {
                (p(!0), d || Fe(i));
              }, [d, i]),
              g = (0, r.useCallback)(() => {
                d || (Fe(c), a(e));
              }, [d, c, e, a]),
              A = (0, r.useCallback)(() => {
                p(!1);
              }, []),
              C = R.strings.vehicle_customization.style_switcher
                .$dyn(`style_${_}`)
                .$dyn(`level${e}`),
              h = f()(
                Da,
                d && wa,
                d && t === s && xa,
                t > s && t !== u && Ia,
                t <= s && ka,
                E && Ta,
                l && Pa,
              ),
              v = (0, r.useMemo)(
                () =>
                  ((e, t, u) =>
                    e === t
                      ? Fa(0)
                      : e === u
                        ? Fa(Math.abs(e - t) - 2)
                        : (u > t && e > t && e < u) || (u < t && e < t && e > u)
                          ? Fa(Math.abs(e - t) - 1)
                          : void 0)(t, n, u),
                [t, n, u],
              ),
              F = f()(Ba, ya);
            return o().createElement(
              "div",
              { className: h },
              o().createElement(
                "div",
                { className: F, style: v },
                d && o().createElement("div", { className: Va }),
                !d && o().createElement("div", { className: Ra }),
                o().createElement("div", { className: Oa, style: v }),
                o().createElement("div", { className: Ua }, C),
                o().createElement("div", {
                  className: La,
                  style: v,
                  onClick: g,
                  onMouseEnter: b,
                  onMouseLeave: A,
                }),
              ),
            );
          },
          Ya = "SwitcherSeparator_base_06",
          Ka = "SwitcherSeparator_base__isBeforeSelectedBullet_a8",
          Za = "SwitcherSeparator_base__notAnimated_73",
          Ja = "SwitcherSeparator_base__scaled_76",
          Qa = "SwitcherSeparator_base__rightTransformOrigin_b8",
          er = "SwitcherSeparator_base__leftTransformOrigin_49",
          tr = "SwitcherSeparator_base__transitionTransformOrigin_9f",
          ur = (0, r.memo)(
            ({ index: e, selectedIndex: t, previousSelectedIndex: u, isAnimated: n = !0 }) => {
              const a = ((e, t, u) =>
                  e === t + 1 || e === t - 1
                    ? Fa(0)
                    : e === u + 1 || e === u - 1
                      ? Fa(Math.abs(u - t) - 2)
                      : (u > t && e > t && e < u + 1) || (u < t && e < t && e > u - 1)
                        ? Fa(Math.abs(e - t) - 1)
                        : void 0)(e, u, t),
                r = 1 === Math.abs(e - t),
                s = 1 === Math.abs(e - u),
                l = ((e, t, u, n) =>
                  e === u + 1 || (e === t + 1 && !n)
                    ? Qa
                    : e === u - 1 || (e === t - 1 && !n)
                      ? er
                      : void 0)(e, u, t, r),
                i = f()(
                  Ya,
                  n && e < t && Ka,
                  n && s && r && tr,
                  n && (e === t + 1 || e === t - 1) && Ja,
                  n && l,
                  !n && Za,
                );
              return o().createElement("div", { className: i, style: a });
            },
          ),
          nr = (e, t) => ("number" == typeof e ? 2 * (e - t) : void 0);
        let ar;
        !(function (e) {
          e.small = "small";
        })(ar || (ar = {}));
        const rr = ({
            numberOfBullets: e,
            selectedNumber: t,
            onChange: u,
            currentText: n,
            currentNumber: a,
            startNumber: s = 1,
            isBulletsBeforeCurrentDisabled: l = !1,
            size: i,
            mouseEnterSound: c = "highlight",
            clickSound: _ = "play",
            isArabic: d = !1,
            hasLightShadows: m = !1,
            styleID: E = 0,
            switcherType: p = qt.digital,
          }) => {
            const b = (0, r.useState)(!1),
              g = b[0],
              A = b[1];
            (0, r.useEffect)(() => fa(() => A(!0), 0), []);
            const C = s + e - 1,
              h = ha(t, l && a ? a : s, C),
              v = "number" == typeof a ? ha(a, s, C) : void 0,
              F = nr(h, s),
              D = nr(v, s),
              B = (0, r.useRef)(F);
            (0, r.useEffect)(() => {
              B.current = F;
            });
            const w = B.current,
              y = f()(
                va.base,
                n && void 0 !== D && va.base__hasCurrentText,
                i && va[`base__${i}`],
                g && va.base__isVisible,
              ),
              S = (0, r.useMemo)(
                () =>
                  ((e, t) => {
                    const u = [];
                    for (let n = e; n <= t; n++) u.push(n);
                    return u;
                  })(s, C),
                [C, s],
              ),
              k = p === qt.digital;
            return o().createElement(
              "div",
              { className: y },
              S.map((e, t) => {
                const a = 2 * t,
                  r = !(!l || !D) && a < D;
                return o().createElement(
                  o().Fragment,
                  { key: t },
                  t > 0 &&
                    o().createElement(ur, {
                      index: a - 1,
                      selectedIndex: F,
                      previousSelectedIndex: w,
                      isAnimated: k,
                    }),
                  k
                    ? o().createElement(qa, {
                        index: a,
                        selectedIndex: F,
                        previousSelectedIndex: w,
                        numberToDisplay: e,
                        currentIndex: D,
                        currentText: n,
                        onChange: u,
                        isDisabled: r,
                        mouseEnterSound: c,
                        clickSound: _,
                        isArabic: d,
                        hasLightShadows: m,
                      })
                    : o().createElement(Xa, {
                        index: a,
                        selectedIndex: F,
                        previousSelectedIndex: w,
                        numberToDisplay: e,
                        currentIndex: D,
                        onChange: u,
                        isDisabled: r,
                        mouseEnterSound: c,
                        clickSound: _,
                        hasLightShadows: m,
                        styleID: E,
                      }),
                );
              }),
            );
          },
          or = "EscBtn_base_d0",
          sr = "EscBtn_esc_97",
          lr = "EscBtn_close_90",
          ir = (0, r.memo)(({ mixClass: e, soundClick: t = "play", onCloseCallback: u }) => {
            const n = f()(or, e);
            return o().createElement(
              "div",
              { className: n },
              o().createElement($t, {
                caption: "",
                type: "close",
                soundClick: t,
                onClick: u,
                classNames: { base: lr },
              }),
              o().createElement("div", { className: sr }),
            );
          }),
          cr = "Tab_base_05",
          _r = "Tab_content_99",
          dr = "Tab_base__selected_4b",
          mr = "Tab_base__accent_b2",
          Er = "Tab_selectedDivider_25",
          pr = "Tab_selectedDivider__left_57",
          br = "Tab_selectedDivider__right_78",
          gr = "Tab_divider_0e",
          Ar = "Tab_divider__left_ac",
          Cr = "Tab_divider__right_44",
          fr = "Tab_icon_fb",
          hr = "Tab_base__hover_54",
          vr = "Tab_plus_2d",
          Fr = "Tab_iconWrapper_c5",
          Dr = "Tab_label_e8",
          Br = "Tab_highlight_1c",
          wr = "Tab_highlight__left_87",
          yr = "Tab_highlight__right_d6",
          Sr = "Tab_tick_a3",
          kr = "Tab_tabsDivider_17",
          Tr = "Tab_bubble_4f";
        let Nr;
        !(function (e) {
          ((e.Active = "active"), (e.Accent = "accent"), (e.Default = "default"));
        })(Nr || (Nr = {}));
        const Ir = R.images.gui.maps.icons.customization.tabs,
          Mr = R.strings.customization.itemTypes,
          xr = R.strings.customization.tooltips.tabs,
          Or = (0, r.memo)(
            ({
              id: e,
              itemType: t,
              isFirst: u,
              isPlus: n,
              isLast: a,
              isPrevAnotherGroup: s,
              isNextAnotherGroup: l,
              isNextSelected: i,
              isAccent: c,
              isSelected: _,
              noveltyCounter: d,
              onClick: m,
              onHoverTab: E,
            }) => {
              const p = (0, r.useState)(!1),
                b = p[0],
                g = p[1],
                A = (0, r.useCallback)(() => {
                  _ || (De.playHighlight(), g(!0), E && E(e));
                }, [e, _, E]),
                C = (0, r.useMemo)(() => {
                  let e;
                  return (
                    (e = _ ? Nr.Active : c ? Nr.Accent : Nr.Default),
                    { backgroundImage: `url(${Ir.$dyn(`${t}_${e}`)})` }
                  );
                }, [c, _, t]),
                h = f()(cr, b && hr, _ && dr, c && !_ && mr);
              return o().createElement(
                "div",
                {
                  onClick: () => {
                    m(e);
                  },
                  onMouseEnter: A,
                  onMouseLeave: () => {
                    g(!1);
                  },
                  className: h,
                },
                u && !_ && o().createElement("div", { className: f()(gr, Ar) }),
                o().createElement(
                  Le,
                  {
                    header: String(xr.$dyn(`${t}_title`)),
                    body: String(xr.$dyn(`${t}_description`)),
                  },
                  o().createElement(
                    "div",
                    { className: _r },
                    o().createElement(
                      "div",
                      { className: Fr },
                      o().createElement("div", { className: fr, style: C }),
                      n && o().createElement("div", { className: vr }),
                    ),
                    o().createElement("div", { className: Dr }, Mr.$dyn(`${t}`)),
                    _
                      ? o().createElement(
                          o().Fragment,
                          null,
                          o().createElement("div", { className: f()(Br, wr) }),
                          o().createElement("div", { className: f()(Br, yr) }),
                          o().createElement("div", { className: Sr }),
                          o().createElement("div", { className: f()(Er, pr) }),
                          o().createElement("div", { className: f()(Er, br) }),
                        )
                      : o().createElement(
                          o().Fragment,
                          null,
                          s && o().createElement("div", { className: f()(gr, Ar) }),
                          l && o().createElement("div", { className: f()(gr, Cr) }),
                        ),
                  ),
                ),
                !l && !_ && !i && o().createElement("div", { className: a ? f()(gr, Cr) : kr }),
                Boolean(d) && o().createElement(Wt, { className: Tr, text: d.toString() }),
              );
            },
          ),
          Rr = "Tabs_base_51",
          Lr = "Tabs_tabs_ab",
          Pr = "Tabs_groupDivider_b2";
        function Hr() {
          return (
            (Hr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Hr.apply(this, arguments)
          );
        }
        const zr = (0, r.memo)(
            ({
              isEditable: e,
              tabs: t,
              onClick: u,
              onHoverTab: n,
              onEditClose: a,
              mixClass: r,
            }) => {
              var s;
              const l = null == (s = t.find((e) => e.isSelected)) ? void 0 : s.groupId;
              return o().createElement(
                "div",
                { className: f()(Rr, r) },
                t &&
                  t.map((e, a) => {
                    const r = t[a + 1],
                      s = t[a - 1],
                      i = r && r.isSelected,
                      c = s && e.groupId !== s.groupId,
                      _ = r && e.groupId !== r.groupId,
                      d = e.groupId === l;
                    return o().createElement(
                      "div",
                      { key: `${a}-${e.id}`, className: Lr },
                      o().createElement(
                        Or,
                        Hr(
                          {
                            isFirst: 0 === a,
                            isLast: a === t.length - 1,
                            isNextSelected: i,
                            isPrevAnotherGroup: c,
                            isNextAnotherGroup: _,
                            isAccent: d,
                            onClick: u,
                            onHoverTab: n,
                          },
                          e,
                        ),
                      ),
                      _ && o().createElement("div", { className: Pr }),
                    );
                  }),
                e && o().createElement(ir, { onCloseCallback: a }),
              );
            },
          ),
          Wr = "ExtendedItem_base_8b",
          Ur = "ExtendedItem_hoverBg_5c",
          Vr = "ExtendedItem_hoverBg__visible_6a",
          jr = "ExtendedItem_toggleBorder_9c",
          $r = "ExtendedItem_toggleBorder__select_01",
          Gr = "ExtendedItem_toggle_24",
          qr = "ExtendedItem_size_1c",
          Xr = "ExtendedItem_paletteIcon_87",
          Yr = R.images.gui.maps.icons.customization.toolbar.extended,
          Kr = (0, r.memo)(({ item: e, onActionClick: t, actionType: u }) => {
            const n = e.actionData,
              a = e.isSelected,
              s = e.icon,
              l = e.paletteIcon,
              i = (0, r.useState)(!1),
              c = i[0],
              _ = i[1],
              d = a ? Yr.toggle_on() : Yr.toggle_default();
            return o().createElement(
              "div",
              {
                className: Wr,
                onClick: () => {
                  (t(u, n), De.playClick());
                },
                onMouseEnter: () => {
                  (_(!0), De.playHighlight());
                },
                onMouseLeave: () => {
                  _(!1);
                },
              },
              o().createElement("div", { className: f()(Ur, c && Vr) }),
              o().createElement("div", { className: f()(jr, a && $r) }),
              o().createElement("div", { className: Gr, style: { backgroundImage: `url(${d})` } }),
              Boolean(s.length) && o().createElement(Wt, { className: qr, text: s }),
              Boolean(l.length) &&
                o().createElement("div", {
                  className: Xr,
                  style: { backgroundImage: `url(${l})` },
                }),
            );
          }),
          Zr = "ExtendedSubButtons_base_b5",
          Jr = "ExtendedSubButtons_bg_4f",
          Qr = "ExtendedSubButtons_content_17",
          eo = (0, r.memo)(({ subButtons: e, onMouseLeave: t, onActionClick: u, actionType: n }) =>
            o().createElement(
              "div",
              { className: Zr, onMouseLeave: t },
              o().createElement(
                "div",
                { className: Qr },
                o().createElement("div", { className: Jr }),
                e.map((e) =>
                  o().createElement(Kr, {
                    key: e.actionData,
                    item: e,
                    onActionClick: u,
                    actionType: n,
                  }),
                ),
              ),
            ),
          ),
          to = "ToolbarItem_base_c1",
          uo = "ToolbarItem_base__disable_40",
          no = "ToolbarItem_hoverBg_89",
          ao = "ToolbarItem_hoverBg__visible_c9",
          ro = "ToolbarItem_icon_65",
          oo = "ToolbarItem_icon__disable_ef",
          so = "ToolbarItem_disable_43",
          lo = "ToolbarItem_hoveredIcon_a8",
          io = "ToolbarItem_base__hover_02",
          co = "ToolbarItem_actionName_38",
          _o = "ToolbarItem_arrow_f4",
          mo = "ToolbarItem_arrow__left_00",
          Eo = "ToolbarItem_arrow__leftHover_72",
          po = "ToolbarItem_arrow__right_a9",
          bo = "ToolbarItem_arrow__rightHover_a9",
          go = "ToolbarItem_arrow__leftDisable_8c",
          Ao = "ToolbarItem_arrow__rightDisable_bd";
        let Co, fo;
        (!(function (e) {
          ((e[(e.RIGHT = 0)] = "RIGHT"), (e[(e.LEFT = 1)] = "LEFT"));
        })(Co || (Co = {})),
          (function (e) {
            ((e.COLOR_CHANGE = "color_change"), (e.SCALE_CHANGE = "scale_change"));
          })(fo || (fo = {})));
        const ho = R.images.gui.maps.icons.customization.toolbar,
          vo = [fo.COLOR_CHANGE, fo.SCALE_CHANGE],
          Fo = [
            Gt.CUSTOMIZATION_SHEET_ACTION_REMOVE_ONE,
            Gt.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_SEASONS,
            Gt.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_PARTS,
          ],
          Do = (0, r.memo)(({ toolbarItem: e, onItemClick: t, onItemOver: u, isSelected: n }) => {
            const a = e.actionType,
              s = e.isEnabled,
              l = e.actionBtnLabel,
              i = e.subButtons,
              c = e.progressionLevel,
              _ = `${a}${c}`,
              d = c > 0,
              m = s ? ho.default.$dyn(d ? _ : a) : ho.disable.$dyn(a),
              E = ho.idle.$dyn(d ? _ : a),
              p = (0, r.useState)(!1),
              b = p[0],
              g = p[1],
              A = (0, r.useState)(!1),
              C = A[0],
              h = A[1],
              v = (0, r.useState)(!1),
              F = v[0],
              D = v[1],
              B = (0, r.useState)({ left: !1, right: !1 }),
              w = B[0],
              y = B[1],
              S = vo.includes(a);
            (0, r.useEffect)(() => {
              (n && s && g(!0), n && S && D(!0));
            }, [n, S, s]);
            const k = (0, r.useCallback)(() => {
                (h(!1), n && S && h(!0));
              }, [n, S]),
              T = (e, u) => {
                (e.stopPropagation(), t(a, u));
              },
              N = (e) => {
                s &&
                  (e === Co.LEFT
                    ? y((e) => Object.assign({}, e, { left: !0 }))
                    : y((e) => Object.assign({}, e, { right: !0 })));
              },
              I = (e) => {
                s &&
                  (e === Co.LEFT
                    ? y((e) => Object.assign({}, e, { left: !1 }))
                    : y((e) => Object.assign({}, e, { right: !1 })));
              },
              M = S && C && n,
              x = f()(to, b && io, !s && uo),
              O = f()(_o, mo, w.left && s && Eo, !s && go),
              L = f()(_o, po, w.right && s && bo, !s && Ao);
            return o().createElement(
              "div",
              {
                onMouseEnter: () => {
                  s && (g(!0), S && !C && h(!0), u(a), De.playHighlight());
                },
                onMouseLeave: () => {
                  (g(!1), C && h(!1), F && D(!1));
                },
                onClick: () => {
                  s &&
                    !S &&
                    (a === Gt.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS
                      ? Fe(R.sounds.cust_select_double())
                      : a === Gt.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_PARTS
                        ? Fe(R.sounds.cust_color_apply())
                        : Fo.includes(a)
                          ? Fe(R.sounds.cust_select_remove())
                          : Fe(R.sounds.cust_select()),
                    t(a, d ? Co.RIGHT : -1));
                },
                className: x,
              },
              (M || F) &&
                s &&
                o().createElement(eo, {
                  subButtons: i,
                  actionType: a,
                  onActionClick: t,
                  onMouseLeave: k,
                }),
              o().createElement("div", { className: f()(no, b && ao) }),
              !s && o().createElement("div", { className: so }),
              o().createElement(Wt, { text: l, className: co }),
              d &&
                o().createElement("div", {
                  className: O,
                  onMouseEnter: () => N(Co.LEFT),
                  onMouseLeave: () => I(Co.LEFT),
                  onClick: (e) => T(e, Co.LEFT),
                }),
              o().createElement("div", {
                className: f()(ro, !s && oo),
                style: { backgroundImage: `url(${m})` },
              }),
              o().createElement("div", { className: lo, style: { backgroundImage: `url(${E})` } }),
              d &&
                o().createElement("div", {
                  className: L,
                  onMouseEnter: () => N(Co.RIGHT),
                  onMouseLeave: () => I(Co.RIGHT),
                  onClick: (e) => T(e, Co.RIGHT),
                }),
            );
          }),
          Bo = "Toolbar_base_56",
          wo = "Toolbar_content_31",
          yo = { type: "", index: -1 },
          So = (0, r.memo)(({ toolbarItems: e, onItemClick: t }) => {
            const u = (0, r.useState)(yo),
              n = u[0],
              a = u[1];
            (0, r.useEffect)(() => () => a(yo), [e]);
            const s = (0, r.useCallback)((e) => {
                a((t) => Object.assign({}, t, { type: e }));
              }, []),
              l = (0, r.useCallback)(
                (e, u, n) => {
                  (t(e, u), a({ type: e, index: n }));
                },
                [t],
              );
            return o().createElement(
              "div",
              { className: Bo },
              o().createElement(
                "div",
                { className: wo },
                e.map((e, t) =>
                  o().createElement(
                    En,
                    {
                      key: e.actionType,
                      tooltipArgs: {
                        body: e.disableTooltip,
                        isEnabled: Boolean(e.disableTooltip.length),
                      },
                    },
                    o().createElement(Do, {
                      key: e.actionType,
                      toolbarItem: e,
                      onItemClick: (e, u) => l(e, u, t),
                      onItemOver: s,
                      isSelected: n.type === e.actionType || t === n.index,
                    }),
                  ),
                ),
              ),
            );
          }),
          ko = "AllSeasonsHint_base_d7",
          To = "AllSeasonsHint_text_7b",
          No = R.strings.customization.customization.allSeasonsHint,
          Io = R.strings.customization.itemTypes,
          Mo = (0, r.memo)(({ itemType: e, isSelected: t, onSelectApplyingAllSeasons: u }) => {
            const n = Et().mediaSize <= _t.Small,
              a = n ? Jt.medium : Jt.large;
            return o().createElement(
              Le,
              { header: No.tooltip.header(), body: No.tooltip.body() },
              o().createElement(
                "div",
                { className: ko },
                o().createElement(
                  nu,
                  {
                    isChecked: t,
                    size: a,
                    type: Qt.main,
                    soundHover: R.sounds.highlight(),
                    soundClick: R.sounds.play(),
                    onChange: () => {
                      u();
                    },
                  },
                  o().createElement(Wt, {
                    text: n ? No.shortText() : No.text(),
                    className: To,
                    format: {
                      binding: !n && e ? { item: String(Io.$dyn(`${e}`)).toLowerCase() } : void 0,
                    },
                  }),
                ),
              ),
            );
          }),
          xo = 33,
          Oo = 0,
          Ro = !0,
          Lo = "play";
        const Po = [
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
        function Ho() {
          return (
            (Ho =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ho.apply(this, arguments)
          );
        }
        const zo = (0, r.memo)(function (e) {
            let t = e.width,
              u = e.height,
              n = e.getImageSource,
              a = e.frameCount,
              s = e.onAnimate,
              l = e.frameTime,
              i = void 0 === l ? xo : l,
              c = e.initialFrameIndex,
              _ = void 0 === c ? Oo : c,
              d = e.lastFrameIndex,
              m = void 0 === d ? a - 1 : d,
              E = e.loop,
              p = void 0 === E ? Ro : E,
              b = e.state,
              g = void 0 === b ? Lo : b,
              A = e.onAnimationDone,
              C = e.onAnimationComplete,
              f = e.poster,
              h = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Po);
            const v = (0, r.useRef)(null);
            return (
              (0, r.useEffect)(() => {
                const e = v.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  u = (u) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(u.img, -u.x, -u.y));
                  };
                switch (g) {
                  case "play":
                    return (function () {
                      const e = Vo(_, m, n),
                        t = Wo(_, m),
                        a = window.setInterval(() => {
                          const n = t(),
                            r = e.get(n);
                          r
                            ? (null == s || s(n, r),
                              u(r),
                              n === m &&
                                (null == C || C(),
                                p || (null == A || A(), window.clearInterval(a))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, i);
                      return () => window.clearInterval(a);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === _ && f ? { path: f, x: 0, y: 0 } : n(_),
                        t = new Image();
                      t.src = e.path;
                      const a = () => u(Uo(e, t));
                      return (
                        t.addEventListener("load", a),
                        () => t.removeEventListener("load", a)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [i, n, _, m, p, s, C, A, f, g]),
              o().createElement("canvas", Ho({}, h, { width: t, height: u, ref: v }))
            );
          }),
          Wo = (e, t) => {
            let u = e;
            return () => {
              const n = u;
              return ((u += 1), u > t && (u = e), n);
            };
          },
          Uo = (e, t) => Object.assign({}, e, { img: t }),
          Vo = (e, t, u) => {
            const n = new Map(),
              a = {};
            for (let r = e; r <= t; r++) {
              const e = u(r),
                t = a[e.path];
              if (t) n.set(r, Uo(e, t));
              else {
                const t = new Image();
                ((a[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${r})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  n.set(r, Uo(e, t)));
              }
            }
            return n;
          };
        let jo;
        !(function (e) {
          ((e.Active = "active"), (e.Ending = "ending"), (e.Disabled = "disabled"));
        })(jo || (jo = {}));
        const $o = (e) => (e < 0.5 ? 4 * e * e * e : (e - 1) * (2 * e - 2) * (2 * e - 2) + 1),
          Go = (e) => {
            const t = ((e) => {
                const t = new Date(1e3 * e);
                return { day: t.getDate(), month: t.getMonth() };
              })(e),
              u = t.day,
              n = t.month;
            return { day: u, month: R.strings.menu.dateTime.months.$num(n + 1) };
          },
          qo = (0, r.memo)(
            ({
              children: e,
              isVisible: t = !0,
              delay: u = 0,
              duration: n = 800,
              opacityFrom: a = 0,
              opacityEnter: r = 1,
              opacityLeave: s = 0,
              classMix: l,
            }) =>
              (0, at.useTransition)(t, {
                key: t,
                from: { opacity: a },
                enter: { opacity: r },
                leave: { opacity: s },
                delay: u,
                config: { duration: n, easing: $o },
              })((t, u) => u && o().createElement(at.animated.div, { className: l, style: t }, e)),
          ),
          Xo = {
            base: "EntryPoint_base_0f",
            base__small: "EntryPoint_base__small_2c",
            base__medium: "EntryPoint_base__medium_0a",
            base__big: "EntryPoint_base__big_7e",
            base__large: "EntryPoint_base__large_ec",
            base__disabled: "EntryPoint_base__disabled_1b",
            bg: "EntryPoint_bg_61",
            base__hover: "EntryPoint_base__hover_86",
            highlight: "EntryPoint_highlight_49",
            shadow: "EntryPoint_shadow_c7",
            content: "EntryPoint_content_bc",
            title: "EntryPoint_title_75",
            subTitle: "EntryPoint_subTitle_ec",
            timeContent: "EntryPoint_timeContent_b8",
            timeActive: "EntryPoint_timeActive_54",
            timeEnding: "EntryPoint_timeEnding_4a",
            particles: "EntryPoint_particles_07",
            base__isAloneBanner: "EntryPoint_base__isAloneBanner_70",
          };
        function Yo() {
          return (
            (Yo =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Yo.apply(this, arguments)
          );
        }
        var Ko;
        !(function (e) {
          ((e.Large = "large"), (e.Big = "big"), (e.Medium = "medium"), (e.Small = "small"));
        })(Ko || (Ko = {}));
        const Zo = R.strings.event.customizationResource,
          Jo = {
            width: 280,
            height: 170,
            frameCount: 136,
            chunk: { count: 1, rows: 20, columns: 7 },
            getChunkPath: () =>
              "R.images.gui.maps.icons.event.customizationResource.entryPoint.particles_sequence",
          },
          Qo = (function (e) {
            const t = e.chunk,
              u = t.rows * t.columns;
            return (n) => {
              const a = n % u,
                r = (a % t.columns) * e.width,
                o = Math.trunc(a / t.columns) * e.height;
              return { path: e.getChunkPath(Math.trunc(n / u)), x: r, y: o };
            };
          })(Jo),
          es = (e) => {
            const t = (function (e = 0) {
                let t = e;
                const u = Math.trunc(t / Y);
                t -= u * Y;
                const n = Math.trunc(t / X);
                t -= n * X;
                const a = Math.trunc(t / q);
                return ((t -= a * q), { days: u, hours: n, minutes: a, seconds: t });
              })(e),
              u = t.days,
              n = t.hours,
              a = t.minutes,
              r = R.strings.common.duration;
            if (u) {
              let e = Zo.eventFinishFormat() + L(r.days(), { days: u });
              return (n && (e += " " + L(r.hours(), { hours: n })), e);
            }
            if (n) {
              let e = Zo.eventFinishFormat() + L(r.hours(), { hours: n });
              return (a && (e += " " + L(r.minutes(), { minutes: a })), e);
            }
            return a
              ? Zo.eventFinishFormat() + L(r.minutes(), { minutes: a })
              : Zo.lessThanMinute();
          },
          ts = (0, i.Pi)(({ mixClass: e }) => {
            const t = ca(),
              u = t.controls,
              n = t.model,
              a = Et().mediaSize,
              s = (function (e = {}, t = []) {
                var u, n, a, o;
                const s = (0, r.useState)(null != (u = e.state) ? u : Lo),
                  l = s[0],
                  i = s[1],
                  c = (0, r.useState)(null != (n = e.initialFrameIndex) ? n : Oo),
                  _ = c[0],
                  d = c[1],
                  m = (0, r.useState)(null != (a = e.frameTime) ? a : xo),
                  E = m[0],
                  p = m[1],
                  b = (0, r.useState)(null != (o = e.loop) ? o : Ro),
                  g = b[0],
                  A = b[1],
                  C = (0, r.useRef)(_),
                  f = (0, r.useCallback)((e) => {
                    (d(e), i("play"));
                  }, []),
                  h = (0, r.useCallback)((e) => {
                    (d(e), i("stop"));
                  }, []),
                  v = (0, r.useCallback)(() => {
                    (d(0), i("stop"));
                  }, []),
                  F = (0, r.useCallback)(() => i("play"), []),
                  D = (0, r.useCallback)(() => {
                    (d(C.current + 1), i("stop"));
                  }, []);
                return {
                  props: {
                    state: l,
                    initialFrameIndex: _,
                    frameTime: E,
                    loop: g,
                    onAnimate: (0, r.useCallback)((t, u) => {
                      ((C.current = t), null == e.onAnimate || e.onAnimate(t, u));
                    }, t),
                    onAnimationDone: (0, r.useCallback)(() => {
                      v();
                    }, t),
                  },
                  enableLoop: (0, r.useCallback)(() => A(!0), []),
                  disableLoop: (0, r.useCallback)(() => A(!1), []),
                  setState: i,
                  setInitialFrameIndex: d,
                  setFrameTime: p,
                  goAndPlay: f,
                  goAndStop: h,
                  stop: v,
                  play: F,
                  pause: D,
                };
              })(),
              l = n.root.get(),
              i = l.timer,
              c = l.status,
              _ = l.isLimitsUpdated,
              d = l.isAloneBanner,
              m = c === jo.Active,
              E = c === jo.Disabled,
              p = c === jo.Ending,
              b = le(i - Math.floor(Date.now() / 1e3), q);
            const g = (0, r.useMemo)(() => es(b), [b]),
              A = (0, r.useState)(!1),
              C = A[0],
              h = A[1],
              v = (0, r.useMemo)(() => Go(i), [i]),
              F = v.day,
              D = v.month,
              B = (0, r.useMemo)(
                () =>
                  a >= _t.Large ? Ko.Large : d ? Ko.Big : a === _t.Medium ? Ko.Medium : Ko.Small,
                [a, d],
              ),
              w = (0, at.useSpring)({
                from: { x: 0, opacity: 0 },
                to: { x: 0, opacity: 1 },
                delay: 0,
                config: { duration: 800, easing: $o },
              });
            return o().createElement(
              at.animated.div,
              {
                className: f()(
                  Xo.base,
                  E && Xo.base__disabled,
                  Xo[`base__${B}`],
                  C && Xo.base__hover,
                  d && Xo.base__isAloneBanner,
                  e,
                ),
                onMouseEnter: () => {
                  E || (De.playHighlight(), h(!0));
                },
                onMouseLeave: () => {
                  h(!1);
                },
                onClick: () => {
                  E || (De.playClick(), u.toCustomizationResourceEvent());
                },
                style: w,
              },
              o().createElement("div", { className: Xo.bg }),
              o().createElement("div", { className: Xo.shadow }),
              o().createElement(qo, { classMix: Xo.highlight, isVisible: C }),
              o().createElement(
                "div",
                { className: Xo.content },
                o().createElement(Wt, { className: Xo.title, text: Zo.title() }),
                _ &&
                  o().createElement(Wt, {
                    className: Xo.subTitle,
                    text: a >= _t.Large ? Zo.subTitle() : Zo.shortSubTitle(),
                  }),
              ),
              o().createElement(
                "div",
                { className: f()(Xo.timeContent, E && Xo.timeContent__disabled) },
                m &&
                  o().createElement(Wt, {
                    className: Xo.timeActive,
                    text: Zo.endDateText(),
                    format: { binding: { day: F, month: D } },
                  }),
                p && o().createElement(Wt, { className: Xo.timeEnding, text: g }),
                E &&
                  o().createElement(Wt, { className: Xo.timeEnding, text: Zo.unavailable.text() }),
              ),
              _ &&
                o().createElement(
                  zo,
                  Yo({}, s.props, {
                    width: Jo.width,
                    height: Jo.height,
                    frameCount: Jo.frameCount,
                    getImageSource: Qo,
                    frameTime: 50,
                    loop: !0,
                    className: Xo.particles,
                  }),
                ),
            );
          });
        let us;
        !(function (e) {
          ((e[(e.Empty = 0)] = "Empty"),
            (e[(e.SubmitEnter = 1)] = "SubmitEnter"),
            (e[(e.FirstEnter = 2)] = "FirstEnter"),
            (e[(e.EditEnter = 3)] = "EditEnter"),
            (e[(e.NotAvailableEnter = 4)] = "NotAvailableEnter"));
        })(us || (us = {}));
        const ns = "Inscription_base_27",
          as = "Inscription_base__invalidInput_3d",
          rs = "Inscription_base__show_19",
          os = "Inscription_base__hide_4c",
          ss = "Inscription_base__withIcons_ea",
          ls = "Inscription_invalidEnterIcon_5f",
          is = "Inscription_icons_1d",
          cs = "Inscription_icon_44",
          _s = "Inscription_icon__withDelete_9a",
          ds = "Inscription_text_7e",
          ms = "Inscription_invalidNumber_78",
          Es = R.strings.vehicle_customization.propertySheet.inscriptionController,
          ps = {
            [us.Empty]: "",
            [us.EditEnter]: Es.editEnter(),
            [us.FirstEnter]: Es.firstEnter(),
            [us.SubmitEnter]: Es.submitEnter(),
            [us.NotAvailableEnter]: Es.notAvailableEnter(),
          },
          bs = {
            [us.Empty]: [],
            [us.EditEnter]: [
              R.images.gui.maps.icons.customization.inscription_controller.bspace_btn(),
              R.images.gui.maps.icons.customization.inscription_controller.delete_btn(),
            ],
            [us.FirstEnter]: [],
            [us.SubmitEnter]: [
              R.images.gui.maps.icons.customization.inscription_controller.enter_btn(),
            ],
            [us.NotAvailableEnter]: [],
          },
          gs = (0, r.memo)(
            ({
              inscriptionState: e,
              inscriptionDuration: t,
              inscriptionDelay: u,
              invalidInscriptionNumber: n,
              inscriptionFirstEnterRange: a,
              startTimestamp: s,
            }) => {
              const l = (0, r.useState)(!1),
                i = l[0],
                c = l[1],
                _ = (0, r.useState)(e),
                d = _[0],
                m = _[1],
                E = Yt(),
                p = Yt();
              (0, r.useEffect)(
                () => (
                  c(!1),
                  p.run(() => {
                    (c(!0), m(e));
                  }, u),
                  E.run(() => {
                    c(!1);
                  }, t + u),
                  () => {
                    (p.clear(), E.clear());
                  }
                ),
                [s],
              );
              const b = d === us.NotAvailableEnter;
              return o().createElement(
                "div",
                { className: f()(ns, b && as, i && rs, !i && os, Boolean(bs[d].length) && ss) },
                b && o().createElement("div", { className: ls }),
                o().createElement(Wt, {
                  className: ds,
                  text: ps[d],
                  format: {
                    binding: {
                      value: o().createElement(Wt, { className: ms, text: n }),
                      start: Boolean(a.length) && a[0],
                      end: Boolean(a.length > 1) && a[1],
                    },
                  },
                }),
                !b &&
                  Boolean(bs[d].length) &&
                  o().createElement(
                    "div",
                    { className: is },
                    bs[d].map((e, t) =>
                      o().createElement("div", {
                        className: f()(cs, d === us.EditEnter && _s),
                        key: t,
                        style: { backgroundImage: `url(${e})` },
                      }),
                    ),
                  ),
              );
            },
          ),
          As = {
            base: "MagneticTool_base_cf",
            wrapper: "MagneticTool_wrapper_c1",
            base__wide: "MagneticTool_base__wide_a0",
            base__factor2: "MagneticTool_base__factor2_cb",
            base__factor3: "MagneticTool_base__factor3_c2",
            base__factor4: "MagneticTool_base__factor4_67",
            base__factor6: "MagneticTool_base__factor6_79",
            border: "MagneticTool_border_d9",
            icon: "MagneticTool_icon_56",
            shine: "MagneticTool_shine_03",
          },
          Cs = ({ isEnabled: e, icon: t, isWide: u, isDim: n, formFactor: a, selectedTab: s }) => {
            const l = (0, r.useRef)(null),
              i = se(e);
            ((0, r.useEffect)(() => {
              !e && i && s !== ed.INSCRIPTION && Fe(R.sounds.cancelcloseno());
            }, [e, i, s]),
              (0, r.useEffect)(() => {
                if (!e) return;
                const t = d.O.client.events.mouse.move(([{ clientX: e, clientY: t }, u]) => {
                  const n = l.current;
                  n &&
                    ("outside" !== u
                      ? (n.style.setProperty("--visibility", "visible"),
                        n.style.setProperty("--x", `${viewEnv.pxToRem(e + 7)}rem`),
                        n.style.setProperty("--y", `${viewEnv.pxToRem(t + -40)}rem`))
                      : n.style.setProperty("--visibility", "hidden"));
                });
                return () => {
                  t();
                };
              }, [e]));
            const c = a > 0,
              _ = f()(As.base, !c && u && As.base__wide, c && As[`base__factor${a}`]);
            return o().createElement(
              "div",
              { className: _ },
              e &&
                o().createElement(
                  "div",
                  { ref: l, className: As.wrapper },
                  n && o().createElement("div", { className: As.shine }),
                  o().createElement("div", {
                    className: As.icon,
                    style: { backgroundImage: `url(${t})` },
                  }),
                  o().createElement("div", { className: As.border }),
                ),
            );
          },
          fs = "SceneHitArea_base_ec",
          hs = "SceneHitArea_base__down_e8",
          vs = "SceneHitArea_base__cursorActive_6e";
        let Fs;
        !(function (e) {
          ((e.None = "none"), (e.Ready = "ready"), (e.Dragging = "dragging"));
        })(Fs || (Fs = {}));
        const Ds = ({
            moveSpace: e,
            onSceneOverChange: t,
            onSceneDraggingChange: u,
            onSceneClick: n,
            onHideElements: a,
            onResetMagneticTool: s,
            isHovered: l,
            isOnboardingViewOpened: i = !1,
          }) => {
            const c = (0, r.useState)(!1),
              _ = c[0],
              m = c[1],
              E = (0, r.useRef)({ x: 0, y: 0, state: Fs.None }),
              p = (0, r.useRef)(null),
              b = (0, r.useRef)(null);
            ((0, r.useEffect)(() => {
              const e = d.O.client.events.mouse.up(([e]) => {
                (m(!1),
                  E.current.state === Fs.Ready && n(),
                  b.current && (clearTimeout(b.current), (b.current = null)),
                  a(!1),
                  u(!1));
                const t = e;
                if (t && t.button === Kt.RIGHT) s();
                else {
                  const e = t && t.target;
                  e && e !== p.current && !e.closest("[data-magnetic-tool-support]") && s();
                }
                E.current.state = Fs.None;
              });
              return () => e();
            }, [E, a, n, u, s]),
              (0, r.useEffect)(
                () => () => {
                  b.current && clearTimeout(b.current);
                },
                [],
              ));
            const g = (e) => {
              if (!p.current) return;
              const t = p.current.getBoundingClientRect(),
                u = t.width,
                n = t.height;
              return !(
                0 === e.clientX ||
                0 === e.clientY ||
                e.clientX >= u - 1 ||
                e.clientY >= n - 1
              );
            };
            return o().createElement("div", {
              className: f()(fs, _ && hs, l && vs),
              ref: p,
              onMouseDown: (e) => {
                (e.preventDefault(),
                  e.button === Kt.LEFT &&
                    g(e) &&
                    (m(!0),
                    (E.current.x = e.clientX),
                    (E.current.y = e.clientY),
                    (E.current.state = Fs.Ready),
                    u(!0),
                    (b.current = setTimeout(() => {
                      ((b.current = null), a(!0));
                    }, 200))));
              },
              onMouseMove: (t) => {
                if ((t.preventDefault(), _)) {
                  if (!g(t)) return;
                  const u = E.current,
                    n = t.clientX !== u.x ? t.clientX - u.x : 0,
                    r = t.clientY !== u.y ? t.clientY - u.y : 0;
                  (0 !== n && 0 !== r && (u.state = Fs.Dragging),
                    (u.x = t.clientX),
                    (u.y = t.clientY),
                    e({ dx: n, dy: r, dz: 0 }),
                    b.current && (clearTimeout(b.current), (b.current = null), a(!0)));
                }
              },
              onWheel: (t) => {
                if ((t.preventDefault(), !g(t))) return;
                const u = t.deltaY < 0;
                e({ dx: 0, dy: 0, dz: u ? -600 : 600 });
              },
              onMouseEnter: () => {
                !i && t(!0);
              },
              onMouseLeave: () => {
                !i && t(!0);
              },
            });
          },
          Bs = "BannerDecals_base_b8",
          ws = "BannerDecals_base__hover_b3",
          ys = "BannerDecals_title_f7",
          Ss = R.strings.customization,
          ks = (0, r.memo)(({ onClick: e, onMouseLeave: t, onMouseEnter: u, mixClass: n }) => {
            const a = (0, r.useState)(!1),
              s = a[0],
              l = a[1],
              i = (0, r.useState)(!1),
              c = i[0],
              _ = i[1];
            return o().createElement(
              "div",
              {
                className: f()(Bs, s && ws, n),
                onMouseEnter: () => {
                  (u && u(), l(!0), De.playHighlight());
                },
                onMouseLeave: () => {
                  (!c && t && t(), l(!1));
                },
                onClick: () => {
                  (u && u(), _(!0), De.playClick(), e());
                },
              },
              o().createElement(Wt, { className: ys, text: Ss.customization.decalsBanner() }),
            );
          }),
          Ts = {
            base: "SeasonsTab_base_f1",
            tabNotActive: "SeasonsTab_tabNotActive_0d",
            base__fullContent: "SeasonsTab_base__fullContent_bc",
            base__active: "SeasonsTab_base__active_06",
            tabActive: "SeasonsTab_tabActive_61",
            background: "SeasonsTab_background_a5",
            base__hover: "SeasonsTab_base__hover_59",
            activeTab: "SeasonsTab_activeTab_80",
            shine: "SeasonsTab_shine_19",
            blink: "SeasonsTab_blink_b5",
            base__animatingAppear: "SeasonsTab_base__animatingAppear_87",
            blik: "SeasonsTab_blik_0a",
            flareWrapper: "SeasonsTab_flareWrapper_84",
            flare: "SeasonsTab_flare_1c",
            flareActive: "SeasonsTab_flareActive_e0",
            iconsWrapper: "SeasonsTab_iconsWrapper_38",
            seasonIconWrapper: "SeasonsTab_seasonIconWrapper_b4",
            seasonIcon: "SeasonsTab_seasonIcon_75",
            seasonIcon__hide: "SeasonsTab_seasonIcon__hide_cf",
            seasonIcon__show: "SeasonsTab_seasonIcon__show_41",
            plus: "SeasonsTab_plus_9e",
            fadeOut: "SeasonsTab_fadeOut_46",
            base__animatingDisappear: "SeasonsTab_base__animatingDisappear_07",
            base__full: "SeasonsTab_base__full_31",
            check: "SeasonsTab_check_82",
            fadeInScale: "SeasonsTab_fadeInScale_68",
            titleWrapper: "SeasonsTab_titleWrapper_fe",
            title: "SeasonsTab_title_ea",
            fadeOutScale: "SeasonsTab_fadeOutScale_9a",
            fadeIn: "SeasonsTab_fadeIn_f1",
          },
          Ns = R.strings.customization.customization.seasonsTabs,
          Is = R.images.gui.maps.icons.customization.seasons,
          Ms = (0, r.memo)(
            ({
              onClick: e,
              isSelected: t,
              season: u,
              isShowFullTabContent: n,
              isAllTabsFull: a,
              isFull: s,
              className: l,
            }) => {
              var i;
              const c = (0, r.useState)(!1),
                _ = c[0],
                d = c[1],
                m = (0, r.useState)(null),
                E = m[0],
                p = m[1],
                b = Yt(),
                g = null != (i = se(s)) ? i : s;
              ((0, r.useEffect)(() => {
                if (b.isRunning) return () => b.clear();
              }, [b]),
                (0, r.useEffect)(() => {
                  (!g && s && (p(!0), !a && Fe(R.sounds.cust_tick_on())),
                    g && !s && Fe(R.sounds.cust_tick_off()));
                }, [g, s, b, a]),
                (0, r.useEffect)(() => {
                  if (E)
                    return b.run(() => {
                      p(!1);
                    }, 1200);
                }, [b, E]));
              const A = (0, r.useCallback)(() => {
                  b.isRunning || e(u);
                }, [b, e, u]),
                C = f()(
                  Ts.base,
                  Ts[`base__${u}`],
                  s && !E && Ts.base__full,
                  E && Ts.base__animatingAppear,
                  !E && null !== E && Ts.base__animatingDisappear,
                  _ && Ts.base__hover,
                  t && Ts.base__active,
                  n && Ts.base__fullContent,
                  l,
                );
              return o().createElement(
                "div",
                {
                  onMouseEnter: () => {
                    t || (0, G.wU)() || (d(!0), De.playHighlight());
                  },
                  onMouseLeave: () => {
                    d(!1);
                  },
                  onClick: A,
                  className: C,
                },
                o().createElement("div", { className: Ts.background }),
                t &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", { className: Ts.blink }),
                    o().createElement(
                      "div",
                      {
                        className: Ts.activeTab,
                        style: { backgroundImage: `url(${Is.$dyn(`${u}_bg`)})` },
                      },
                      o().createElement("div", {
                        className: Ts.shine,
                        style: { backgroundImage: `url(${Is.$dyn(`${u}_shine`)})` },
                      }),
                    ),
                  ),
                o().createElement(
                  "div",
                  { className: Ts.iconsWrapper },
                  o().createElement(
                    "div",
                    { className: Ts.seasonIconWrapper },
                    o().createElement("div", {
                      className: f()(
                        Ts.seasonIcon,
                        _ || t ? Ts.seasonIcon__hide : Ts.seasonIcon__show,
                      ),
                      style: { backgroundImage: `url(${Is.$dyn(`${u}_default`)})` },
                    }),
                    o().createElement("div", {
                      className: f()(
                        Ts.seasonIcon,
                        _ || t ? Ts.seasonIcon__show : Ts.seasonIcon__hide,
                      ),
                      style: { backgroundImage: `url(${Is.$dyn(`${u}_active`)})` },
                    }),
                  ),
                  o().createElement("div", { className: Ts.plus }),
                  o().createElement("div", { className: Ts.check }),
                ),
                o().createElement(
                  "div",
                  { className: Ts.titleWrapper },
                  o().createElement(Wt, { text: Ns.$dyn(`${u}`), className: Ts.title }),
                  t && o().createElement(Wt, { text: Ns.map(), className: Ts.title }),
                ),
                o().createElement(
                  "div",
                  { className: Ts.flareWrapper },
                  o().createElement("div", { className: Ts.flare }),
                ),
                t && o().createElement("div", { className: Ts.blik }),
              );
            },
          ),
          xs = "SeasonsTabs_base_24",
          Os = "SeasonsTabs_base__show_61";
        function Rs() {
          return (
            (Rs =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Rs.apply(this, arguments)
          );
        }
        const Ls = ({ tabs: e, isMinimised: t, onClick: u, className: n }) => {
            const a = Et().mediaSize,
              s = !t && a >= _t.Medium,
              l = e.every((e) => e.isFull);
            return (
              (0, r.useEffect)(() => {
                l && Fe(R.sounds.cust_tick_on_all());
              }, [l]),
              o().createElement(
                "div",
                { className: f()(xs, s && Os, n) },
                Boolean(null == e ? void 0 : e.length) &&
                  e.map((e) =>
                    o().createElement(
                      Ms,
                      Rs(
                        { key: e.season, isShowFullTabContent: s, isAllTabsFull: l, onClick: u },
                        e,
                      ),
                    ),
                  ),
              )
            );
          },
          Ps = "VehicleName_base_4d",
          Hs = "VehicleName_vehicleTypeContainer_1e",
          zs = "VehicleName_base__prem_ec",
          Ws = "VehicleName_vehicleType_68",
          Us = "VehicleName_shortName_23",
          Vs = R.images.gui.maps.icons.vehicleTypes.big,
          js = (0, r.memo)(({ name: e, tier: t, type: u, isPremium: n = !1, classMix: a }) => {
            const r = `${((s = u), s.replace(/-/g, "_"))}${n ? "_elite" : ""}`;
            var s;
            return o().createElement(
              o().Fragment,
              null,
              o().createElement(
                "div",
                { className: f()(Ps, n && zs, a) },
                o().createElement(Wt, { text: Hn(t) }),
                o().createElement(
                  "div",
                  { className: Hs },
                  o().createElement("div", {
                    className: Ws,
                    style: { backgroundImage: `url(${Vs.$dyn(r)})` },
                  }),
                ),
                o().createElement(Wt, { text: e, className: Us }),
              ),
              o().createElement("div", null),
            );
          });
        const $s = "App_base_f6",
          Gs = "App_base__expanded_2a",
          qs = "App_wrapper_5c",
          Xs = "App_header_17",
          Ys = "App_header__hide_c5",
          Ks = "App_infoButton_db",
          Zs = "App_base__fadeIn_54",
          Js = "App_base__fadeOut_33",
          Qs = "App_closeButton_7c",
          el = "App_description_d6",
          tl = "App_description__bonus_a0",
          ul = "App_topPanelWrapper_50",
          nl = "App_topPanel_29",
          al = "App_carouselBlock_24",
          rl = "App_carouselBlockBack_d6",
          ol = "App_markers_2a",
          sl = "App_markers__fadeIn_94",
          ll = "App_markers__fadeOut_e3",
          il = "App_emptyState_2f",
          cl = "App_entryPoint_ac",
          _l = "App_decalsBanner_75",
          dl = "App_decalsBanner__hide_98",
          ml = "App_decalsBanner__fadeIn_92",
          El = "App_decalsBanner__fadeOut_38",
          pl = "App_openPanelButton_55",
          bl = "App_openPanelButtonText_6f",
          gl = "App_leftPanel_85",
          Al = "App_rightPanel_fb",
          Cl = "App_divider_8c",
          fl = "App_seasontTabs_50",
          hl = "App_seasontTabs__fadeIn_3a",
          vl = "App_seasontTabs__fadeOut_a6",
          Fl = "App_magneticTool_4d",
          Dl = "App_inscription_3e",
          Bl = "App_toolbarWrapper_55",
          wl = "App_progressionWrapper_19",
          yl = "App_withProgressionWrapper_cb",
          Sl = "App_seasonsHint_6d",
          kl = "App_sub_7b",
          Tl = "App_sub__open_1c",
          Nl = "App_footer_b1",
          Il = "App_footer__hide_ce",
          Ml = "App_binCartPannelWrapper_8c",
          xl = "App_binCartPannelWrapper__open_3f",
          Ol = "App_binCartPannel_b1",
          Rl = "App_cart_25",
          Ll = "App_subInfo_18",
          Pl = "App_subInfo__open_b7",
          Hl = "App_back_ff",
          zl = "App_buttonHolder_58";
        function Wl(e, t, u = []) {
          const n = (0, r.useRef)(0),
            a = (0, r.useCallback)(() => window.clearInterval(n.current), u || []);
          (0, r.useEffect)(() => a, [a]);
          const o = (null != u ? u : []).concat([t]);
          return [
            (0, r.useCallback)((u) => {
              ((n.current = window.setInterval(() => e(u, !0), t)), e(u, !1));
            }, o),
            a,
          ];
        }
        const Ul = "HorizontalBar_base_49",
          Vl = "HorizontalBar_base__nonActive_82",
          jl = "HorizontalBar_leftButton_5f",
          $l = "HorizontalBar_rightButton_03",
          Gl = "HorizontalBar_track_0d",
          ql = "HorizontalBar_thumb_fd",
          Xl = "HorizontalBar_rail_32",
          Yl = "disable",
          Kl = { pending: !1, offset: 0 },
          Zl = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Jl = () => {},
          Ql = (e, t) => Math.max(20, e.offsetWidth * t),
          ei = (0, r.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = Zl, onDrag: n = Jl }) => {
              const a = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, r.useState)(Kl),
                m = d[0],
                E = d[1],
                p = (0, r.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                b = () => {
                  const t = i.current,
                    u = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && t && u && a)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / a),
                    _ = Je(0, 1, r / (a - n)),
                    d = (t.offsetWidth - Ql(t, o)) * _;
                  ((u.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (s.current && l.current && i.current && c.current) {
                        if (0 === e)
                          return (s.current.classList.add(Yl), void l.current.classList.remove(Yl));
                        if (
                          ((t = i.current),
                          (u = c.current),
                          e - (t.offsetWidth - u.offsetWidth) >= -0.5)
                        )
                          return (s.current.classList.remove(Yl), void l.current.classList.add(Yl));
                        var t, u;
                        (s.current.classList.remove(Yl), l.current.classList.remove(Yl));
                      }
                    })(d));
                },
                g = ut(() => {
                  ((() => {
                    const t = c.current,
                      u = i.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && n && u)) return;
                    const o = Math.min(1, n / r);
                    ((t.style.width = `${Ql(u, o)}px`),
                      (t.style.display = "flex"),
                      a.current &&
                        (1 === o ? a.current.classList.add(Vl) : a.current.classList.remove(Vl)));
                  })(),
                    b());
                });
              ((0, r.useEffect)(() => Pe(g)),
                (0, r.useEffect)(
                  () =>
                    Pe(() => {
                      const t = () => {
                        b();
                      };
                      let u = Jl;
                      const n = () => {
                        (u(), (u = Pe(g)));
                      };
                      return (
                        e.events.on("recalculateContent", g),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (u(),
                            e.events.off("recalculateContent", g),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, r.useEffect)(() => {
                  if (!m.pending) return;
                  const t = (t) => {
                      var u;
                      const a = e.contentRef.current;
                      if (!a) return;
                      const r = i.current,
                        o = c.current;
                      if (!a || !r || !o) return;
                      const s = t.screenX - m.offset - r.getBoundingClientRect().x,
                        l = (s / r.offsetWidth) * (null != (u = e.getContainerSize()) ? u : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(a, l),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: o, thumbOffset: s, contentOffset: l }));
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), p(Kl));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, m.offset, m.pending, n, p]));
              const A = Wl((t) => e.applyStepTo(t), _, [e]),
                C = A[0],
                h = A[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const v = (e) => {
                e.target.classList.contains(Yl) || Fe("highlight");
              };
              return o().createElement(
                "div",
                { className: f()(Ul, t.base), ref: a, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: f()(jl, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Yl) || 0 !== e.button || (Fe("play"), C(rt.Next));
                  },
                  onMouseUp: h,
                  ref: s,
                  onMouseEnter: v,
                }),
                o().createElement(
                  "div",
                  {
                    className: f()(Gl, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if ((Fe("play"), t.target === n))
                          p({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = c.current,
                              a = e.contentRef.current;
                            if (!n || !a) return;
                            const r = u(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * t);
                          })(t.screenX > n.getBoundingClientRect().x ? rt.Prev : rt.Next);
                        }
                    },
                    ref: i,
                    onMouseEnter: v,
                  },
                  o().createElement("div", { ref: c, className: f()(ql, t.thumb) }),
                  o().createElement("div", { className: f()(Xl, t.rail) }),
                ),
                o().createElement("div", {
                  className: f()($l, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Yl) || 0 !== e.button || (Fe("play"), C(rt.Prev));
                  },
                  onMouseUp: h,
                  ref: l,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          ti = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          ui = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: a,
            classNames: s,
            scrollClassName: l,
            getStepByRailClick: i,
            onDrag: c,
          }) => {
            const _ = (0, r.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: f()(ti.base, e.base) });
              }, [n]),
              d = (0, r.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: f()(ti.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(ti.defaultScrollArea, a) },
                o().createElement(ni, { className: l, api: d, classNames: s }, e),
              ),
              o().createElement(ei, { getStepByRailClick: i, api: t, onDrag: c, classNames: _ }),
            );
          },
          ni = ({ api: e, className: t, classNames: u, children: n, style: a }) => (
            (0, r.useEffect)(() => Pe(e.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(ti.base, t), style: a },
              o().createElement(
                "div",
                {
                  className: f()(ti.wrapper, null == u ? void 0 : u.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: f()(ti.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((ni.Bar = ei),
          (ni.Default = ui),
          (ni.SeniorityAwards = ({ api: e, className: t, classNames: u, children: n }) => (
            (0, r.useEffect)(() => Pe(e.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(ti.base, t) },
              o().createElement(
                "div",
                { className: f()(ti.wrapper, null == u ? void 0 : u.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: f()(ti.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const ai = st({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? rt.Next : rt.Prev),
          }),
          ri = "VerticalBar_base_f3",
          oi = "VerticalBar_base__nonActive_42",
          si = "VerticalBar_topButton_d7",
          li = "VerticalBar_bottomButton_06",
          ii = "VerticalBar_track_df",
          ci = "VerticalBar_thumb_32",
          _i = "VerticalBar_rail_43",
          di = "disable",
          mi = () => {},
          Ei = { pending: !1, offset: 0 },
          pi = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          bi = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          gi = (e, t) => Math.max(20, e.offsetHeight * t),
          Ai = (0, r.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = pi, onDrag: n = mi }) => {
              const a = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, r.useState)(Ei),
                m = d[0],
                E = d[1],
                p = (0, r.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                b = ut(() => {
                  const t = c.current,
                    u = i.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && t && u)) return;
                  const o = Math.min(1, n / r);
                  return (
                    (t.style.height = `${gi(u, o)}px`),
                    t.classList.add(ci),
                    a.current &&
                      (1 === o ? a.current.classList.add(oi) : a.current.classList.remove(oi)),
                    o
                  );
                }),
                g = ut(() => {
                  const t = i.current,
                    u = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && t && u && a)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / a),
                    _ = Je(0, 1, r / (a - n)),
                    d = (t.offsetHeight - gi(t, o)) * _;
                  ((u.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (s.current && l.current && i.current && c.current) {
                        if (0 === e)
                          return (s.current.classList.add(di), void l.current.classList.remove(di));
                        if (
                          ((t = i.current),
                          (u = c.current),
                          e - (t.offsetHeight - u.offsetHeight) >= -0.5)
                        )
                          return (s.current.classList.remove(di), void l.current.classList.add(di));
                        var t, u;
                        (s.current.classList.remove(di), l.current.classList.remove(di));
                      }
                    })(d));
                }),
                A = ut(() => {
                  bi(e, () => {
                    (b(), g());
                  });
                });
              ((0, r.useEffect)(() => Pe(A)),
                (0, r.useEffect)(() => {
                  const t = () => {
                    bi(e, () => {
                      g();
                    });
                  };
                  let u = mi;
                  const n = () => {
                    (u(), (u = Pe(A)));
                  };
                  return (
                    e.events.on("recalculateContent", A),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (u(),
                        e.events.off("recalculateContent", A),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, r.useEffect)(() => {
                  if (!m.pending) return;
                  const t = (t) => {
                      bi(e, (u) => {
                        const a = i.current,
                          r = c.current,
                          o = e.getContainerSize();
                        if (!a || !r || !o) return;
                        const s = t.screenY - m.offset - a.getBoundingClientRect().y,
                          l = (s / a.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(u, l),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: u.scrollTop },
                        }),
                          n({ type: "dragging", thumb: r, thumbOffset: s, contentOffset: l }));
                      });
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        p(Ei));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, m.offset, m.pending, n, p]));
              const C = Wl((t) => e.applyStepTo(t), _, [e]),
                h = C[0],
                v = C[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const F = (e) => {
                e.target.classList.contains(di) || Fe("highlight");
              };
              return o().createElement(
                "div",
                { className: f()(ri, t.base), ref: a, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: f()(si, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(di) || 0 !== e.button || (Fe("play"), h(rt.Next));
                  },
                  ref: s,
                  onMouseEnter: F,
                }),
                o().createElement(
                  "div",
                  {
                    className: f()(ii, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if ((Fe("play"), t.target === n))
                          (e.handleIsThumbDragging(!0),
                            p({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              bi(e, (n) => {
                                if (!n) return;
                                const a = u(e),
                                  r = e.clampPosition(n, n.scrollTop + a * t);
                                e.applyScroll(r);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? rt.Prev : rt.Next);
                        }
                    },
                    ref: i,
                    onMouseEnter: F,
                  },
                  o().createElement("div", { ref: c, className: t.thumb }),
                  o().createElement("div", { className: f()(_i, t.rail) }),
                ),
                o().createElement("div", {
                  className: f()(li, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(di) || 0 !== e.button || (Fe("play"), h(rt.Prev));
                  },
                  onMouseUp: v,
                  ref: l,
                  onMouseEnter: F,
                }),
              );
            },
          ),
          Ci = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          fi = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: a,
            scrollClassName: s,
            scrollClassNames: l,
            getStepByRailClick: i,
            onDrag: c,
          }) => {
            const _ = (0, r.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: f()(Ci.base, e.base) });
              }, [n]),
              d = (0, r.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: f()(Ci.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(Ci.area, a) },
                o().createElement(hi, { className: s, classNames: l, api: d }, e),
              ),
              o().createElement(Ai, { getStepByRailClick: i, api: t, onDrag: c, classNames: _ }),
            );
          },
          hi = ({ className: e, classNames: t, children: u, api: n }) => (
            (0, r.useEffect)(() => Pe(n.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(Ci.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(Ci.content, null == t ? void 0 : t.content), ref: n.contentRef },
                u,
              ),
            )
          );
        hi.Default = fi;
        const vi = { Vertical: a, Horizontal: n },
          Fi = { type: "idle" };
        const Di = (e, t) => {
            (0, r.useEffect)(() => {
              let t = null;
              return (
                (t = requestAnimationFrame(() => {
                  t = requestAnimationFrame(() => {
                    ((t = null), e());
                  });
                })),
                () => {
                  null !== t && cancelAnimationFrame(t);
                }
              );
            }, t);
          },
          Bi = "ArrowsHint_base_3c",
          wi = "ArrowsHint_content_ac",
          yi = "ArrowsHint_notificationBg_ef",
          Si = "ArrowsHint_arrows_7c",
          ki = "ArrowsHint_bg_e0",
          Ti = "ArrowsHint_arrow_41",
          Ni = "ArrowsHint_arrow__left_9c",
          Ii = "ArrowsHint_arrow__right_50",
          Mi = "ArrowsHint_text_a2",
          xi = () =>
            o().createElement(
              "div",
              { className: Bi },
              o().createElement("div", { className: ki }),
              o().createElement(
                "div",
                { className: wi },
                o().createElement("div", { className: yi }),
                o().createElement(Wt, {
                  className: Mi,
                  text: R.strings.customization.arrowHint.text(),
                }),
                o().createElement(
                  "div",
                  { className: Si },
                  o().createElement("div", { className: f()(Ti, Ni) }),
                  o().createElement("div", { className: f()(Ti, Ii) }),
                ),
              ),
            ),
          Oi = ({
            children: e,
            contentID: t,
            decoratorID: u = 0,
            targetId: n = 0,
            args: a,
            isEnabled: o = !0,
            onMouseDown: s,
          }) => {
            const l = (0, r.useCallback)(() => {
                ((0, G.c9)(G.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: n,
                  isMouseEvent: !0,
                  on: !0,
                  args: a,
                }),
                  De.playYes());
              }, [a, t, u, n]),
              i = (0, r.useCallback)(() => {
                (0, G.c9)(G.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: n,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, u, n]),
              c = (0, r.useCallback)(
                (e) => {
                  (s && s(e), ((e) => e.button === Kt.RIGHT)(e) && l());
                },
                [s, l],
              );
            return (
              (0, r.useEffect)(() => {
                !1 === o && i();
              }, [o, i]),
              o ? (0, r.cloneElement)(e, { onMouseDown: c }) : e
            );
          },
          Ri = ["children"];
        function Li() {
          return (
            (Li =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Li.apply(this, arguments)
          );
        }
        const Pi = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Ri);
            return o().createElement(
              Oi,
              Li({}, u, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          Hi = "Image_base_5c",
          zi = "Image_shine_08",
          Wi = "Image_content_03",
          Ui = (0, r.memo)(({ isDim: e, icon: t }) => {
            const u = (0, r.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]);
            return t
              ? o().createElement(
                  "span",
                  { className: Hi },
                  e && o().createElement("span", { className: zi }),
                  o().createElement("span", { className: Wi, style: u }),
                )
              : o().createElement("span", { className: Wi });
          }),
          Vi = "Price_base_9e",
          ji = "Price_base__stock_cc",
          $i = "Price_storage_04",
          Gi = "Price_storage__empty_2d",
          qi = "Price_icon_df",
          Xi = "Price_iconRent_ec",
          Yi = "Price_iconRent__autoRent_df",
          Ki = "Price_rental_5a",
          Zi = "Price_iconLocked_07",
          Ji = R.strings.customization,
          Qi = (0, r.memo)(
            ({
              locked: e,
              hasDiscount: t,
              isRental: u,
              autoRentEnabled: n,
              rentalInfoText: a,
              isStub: r,
              price: s,
              quantity: l,
              isFromStorage: i = !0,
              classMix: c,
            }) => {
              var _, d;
              if (r) return null;
              const m = f()(Xi, n && Yi);
              if (e)
                return o().createElement(
                  "span",
                  { className: f()(Vi, c) },
                  o().createElement(
                    "span",
                    { className: qi },
                    o().createElement("span", { className: Zi }),
                  ),
                );
              if (u && l > 0)
                return o().createElement(
                  "span",
                  { className: f()(Vi, c) },
                  o().createElement(
                    "span",
                    { className: qi },
                    o().createElement("span", { className: m }),
                  ),
                  l,
                );
              if (i && (0 === s.length || l > 0))
                return o().createElement(
                  "span",
                  { className: f()(Vi, c) },
                  o().createElement("span", { className: f()($i, !l && Gi) }, l),
                );
              const E = f()(Vi, t && ji, c);
              return o().createElement(
                "div",
                { className: E },
                "" !== a && o().createElement(Wt, { className: Ki, text: a }),
                Boolean(l && l > 1) &&
                  o().createElement(Wt, {
                    text: Ji.cart.quantity(),
                    format: { binding: { quantity: l } },
                  }),
                o().createElement(cu, {
                  isDiscount: t,
                  size: au.small,
                  type: null == (_ = s[0]) ? void 0 : _.name,
                  value: Number(null == (d = s[0]) ? void 0 : d.value),
                }),
              );
            },
          ),
          ec = "ProgressionLevelIcon_base_8a",
          tc = "ProgressionLevelIcon_icon_49",
          uc = "ProgressionLevelIcon_icon__big_74",
          nc = "ProgressionLevelIcon_icon__small_46",
          ac = ({ typeId: e, progressionLevel: t, classMix: u }) => {
            const n = `level_${t}`,
              a =
                36 === e
                  ? R.images.gui.maps.icons.customization.progression_icons
                  : R.images.gui.maps.icons.customization.progression_styles.icons,
              s = a.$dyn(n),
              l = a.$dyn(n.concat("_small")),
              i = (0, r.useMemo)(() => ({ backgroundImage: `url(${l})` }), [l]),
              c = (0, r.useMemo)(() => ({ backgroundImage: `url(${s})` }), [s]);
            return s && l
              ? o().createElement(
                  "div",
                  { className: ec },
                  o().createElement("div", { className: f()(tc, nc, u), style: i }),
                  o().createElement("div", { className: f()(tc, uc, u), style: c }),
                )
              : null;
          },
          rc = "Slot_base_25",
          oc = "Slot_base__big_e2",
          sc = "Slot_base__isProgression_0b",
          lc = "Slot_base__locked_4d",
          ic = "Slot_base__isAlreadyUsed_dd",
          cc = "Slot_base__selected_03",
          _c = "Slot_equippedIcon_0d",
          dc = "Slot_pulse_3a",
          mc = "Slot_image_c9",
          Ec = "Slot_inProgressIcon_8a",
          pc = "Slot_progressionArrow_74",
          bc = "Slot_progressionArrow__enabled_25",
          gc = "Slot_shadowBottom_96",
          Ac = "Slot_base__hasExtraName_55",
          Cc = "Slot_shadowTop_11",
          fc = "Slot_base__topLeftCornerVisible_f9",
          hc = "Slot_border_74",
          vc = "Slot_base__equipped_be",
          Fc = "Slot_topLeftCorner_b3",
          Dc = "Slot_ribbon_f5",
          Bc = "Slot_isLocked_bb",
          wc = "Slot_isAlreadyUsed_1a",
          yc = "Slot_isAlreadyUsedText_50",
          Sc = "Slot_isAlreadyUsedIcon_6a",
          kc = "Slot_icon_fc",
          Tc = "Slot_icon__editable_69",
          Nc = "Slot_icon__rewindable_fd",
          Ic = "Slot_icon__special_50",
          Mc = "Slot_icon__alert_6d",
          xc = "Slot_icon__unHistorical_64",
          Oc = "Slot_icon__fantastical_3a",
          Rc = "Slot_icon__serialNumber_26",
          Lc = "Slot_hover_7b",
          Pc = "Slot_price_d1",
          Hc = "Slot_styleName_c6",
          zc = "Slot_button_a6",
          Wc = "Slot_buttonWrapper_ac",
          Uc = "Slot_bubble_cc",
          Vc = "Slot_bubble__placeButton_28",
          jc = R.strings.customization,
          $c = (0, r.memo)(
            ({
              intCD: e,
              typeId: t,
              locked: u,
              soundHover: n = R.sounds.highlight(),
              soundClick: a = R.sounds.cust_select(),
              isSelected: s,
              customizationDisplayType: l,
              tooltip: i,
              isSpecial: c,
              showAlert: _,
              isDim: d,
              icon: m,
              isWide: E,
              quantity: p,
              buyPrice: b,
              extraName: g,
              classMix: A,
              progressionLevel: C,
              isProgressionRewindEnabled: h,
              editableIcon: v,
              onSelectItem: F,
              isEquipped: D,
              editBtnEnabled: B,
              onEditItem: w,
              isRental: y,
              rentalInfoText: S,
              autoRentEnabled: k,
              isWithSerialNumber: T,
              isMainType: N,
              isAlreadyUsed: I,
              noveltyCounter: M,
              editNoveltyCounter: x,
              onHoverItem: O,
              isInProgress: L,
              arrowEnabled: P,
              isNew: H,
              isFilled: z,
            }) => {
              var W;
              const U = (0, r.useMemo)(() => -1 === e, [e]),
                V = (0, r.useMemo)(() => !u, [u]),
                j = Et().mediaSize,
                $ = v.includes("disable") ? null : v,
                G = 1 === l,
                q = 2 === l,
                X = _ || c || T || l || $,
                Y = (0, r.useCallback)(() => {
                  (e && O(e), V && n && !s && Fe(n));
                }, [O, e, V, n, s]),
                K = (0, r.useCallback)(() => {
                  (C <= 0 && (u || I)) || (F && (e && F(e), Fe(a)));
                }, [e, I, u, F, C, a]),
                Z = (0, r.useCallback)(
                  (t) => {
                    (t.stopPropagation(), w && !u && e && w(e));
                  },
                  [e, u, w],
                ),
                J = f()(
                  rc,
                  A,
                  E && oc,
                  s && cc,
                  D && vc,
                  C > 0 && sc,
                  X && fc,
                  g && Ac,
                  u && lc,
                  I && ic,
                ),
                Q = (0, r.useMemo)(
                  () => ({ intCD: e, tooltip: i, showInventoryBlock: !u, progressionLevel: C }),
                  [e, u, C, i],
                ),
                ee = (0, r.useMemo)(
                  () => ({
                    tooltip: G
                      ? "techCustomizationNonhistoricItem"
                      : "techCustomizationFantasticalItem",
                  }),
                  [G],
                ),
                te = Boolean(null == (W = b.discount[0]) ? void 0 : W.value);
              return z
                ? o().createElement(
                    Pi,
                    { key: e, isEnabled: !U, args: { type: "customizationItem", intCD: e } },
                    o().createElement(
                      dn,
                      { args: Q },
                      o().createElement(
                        "div",
                        { className: J, onMouseEnter: Y, onClick: K },
                        H && o().createElement("div", { className: dc }),
                        D && o().createElement("div", { className: _c }),
                        o().createElement(
                          "div",
                          { className: hc },
                          void 0 !== P && o().createElement("div", { className: f()(pc, P && bc) }),
                          L && o().createElement("div", { className: Ec }),
                          o().createElement(
                            "div",
                            { className: mc },
                            o().createElement(Ui, { isDim: d, icon: m }),
                          ),
                          o().createElement("div", { className: Cc }),
                          o().createElement("div", { className: gc }),
                          u && o().createElement("div", { className: Bc }),
                          I &&
                            o().createElement(
                              "div",
                              { className: wc },
                              o().createElement(
                                "div",
                                { className: yc },
                                o().createElement("div", { className: Sc }),
                                E &&
                                  o().createElement(Wt, {
                                    text: jc.customization.carousel.is_already_used(),
                                  }),
                              ),
                            ),
                          Boolean(M) &&
                            o().createElement(Wt, { className: Uc, text: M.toString() }),
                          N && o().createElement("div", { className: Dc }),
                          o().createElement(
                            "div",
                            { className: Fc },
                            _ && o().createElement("div", { className: f()(kc, Mc) }),
                            c && o().createElement("div", { className: f()(kc, Ic) }),
                            T && o().createElement("div", { className: f()(kc, Rc) }),
                            (G || q) &&
                              !U &&
                              o().createElement(
                                dn,
                                { args: ee },
                                o().createElement("div", { className: f()(kc, G ? xc : Oc) }),
                              ),
                            $ &&
                              o().createElement("div", {
                                className: f()(kc, Tc),
                                style: {
                                  backgroundImage: `url(${(() => {
                                    if ($) return j <= _t.Small ? $ : $.replace("small", "big");
                                  })()})`,
                                },
                              }),
                            h
                              ? o().createElement("div", { className: f()(kc, Nc) })
                              : o().createElement(ac, {
                                  typeId: t,
                                  progressionLevel: C,
                                  classMix: kc,
                                }),
                          ),
                          o().createElement(Wt, { className: Hc, text: g }),
                          o().createElement(Qi, {
                            classMix: Pc,
                            isStub: U,
                            price: b.price,
                            quantity: p,
                            isRental: y,
                            rentalInfoText: S,
                            autoRentEnabled: k,
                            locked: u,
                            hasDiscount: te,
                          }),
                          o().createElement("div", { className: Lc }),
                          Boolean(v) &&
                            D &&
                            o().createElement(
                              Le,
                              {
                                body: B
                                  ? jc.customization.changeButton.tooltip()
                                  : jc.customization.changeButtonDisabled.tooltip(),
                              },
                              o().createElement(
                                "div",
                                { id: `${e}-tooltip`, className: Wc },
                                o().createElement(
                                  ke,
                                  {
                                    size: ye.small,
                                    type: B ? we.primary : we.secondary,
                                    disabled: !B,
                                    mixClass: zc,
                                    onClick: Z,
                                  },
                                  Boolean(x) &&
                                    o().createElement(Wt, {
                                      className: f()(Uc, Vc),
                                      text: x.toString(),
                                    }),
                                  j >= _t.Small
                                    ? o().createElement(Wt, {
                                        text: jc.customization.carousel.change_button(),
                                      })
                                    : o().createElement("img", {
                                        src: R.images.gui.maps.icons.customization.edit_btn(),
                                      }),
                                ),
                              ),
                            ),
                        ),
                      ),
                    ),
                  )
                : o().createElement(
                    "div",
                    { className: f()(rc, E && oc), onMouseEnter: Y, onClick: K },
                    o().createElement("div", { className: hc }),
                  );
            },
          ),
          Gc = "Slots_base_ef",
          qc = "Slots_categories_6b",
          Xc = "Slots_categorieBox_d3",
          Yc = "Slots_categorieText_12",
          Kc = "Slots_categorieBoxPattern_8d",
          Zc = "Slots_slot_17";
        function Jc() {
          return (
            (Jc =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Jc.apply(this, arguments)
          );
        }
        const Qc = (0, r.memo)(
          ({
            items: e,
            arrowsList: t,
            categories: u,
            onClick: n,
            onHoverItem: a,
            onEditClick: r,
            isEditable: s,
            categoriesRef: l,
            itemsRef: i,
          }) =>
            o().createElement(
              "div",
              { className: Gc },
              u.map((c, _) => {
                var d;
                return o().createElement(
                  "div",
                  { className: qc, key: `${_}` },
                  "" !== c.bookmarkName &&
                    o().createElement(
                      "div",
                      {
                        className: Xc,
                        ref: (e) => {
                          e ? l.current.set(c.bookmarkIndex, e) : l.current.delete(c.bookmarkIndex);
                        },
                      },
                      o().createElement("div", { className: Kc }),
                      o().createElement("div", { className: Yc }, c.bookmarkName),
                    ),
                  e
                    .slice(c.bookmarkIndex, null == (d = u[_ + 1]) ? void 0 : d.bookmarkIndex)
                    .map((e, u) => {
                      const l = t.find((e) => e.arrowIndex === u);
                      return o().createElement(
                        "div",
                        {
                          key: `${_}_${u}`,
                          ref: (t) => {
                            t ? i.current.set(e.intCD, t) : i.current.delete(e.intCD);
                          },
                          "data-magnetic-tool-support": !0,
                        },
                        o().createElement(
                          $c,
                          Jc(
                            {
                              onSelectItem: n,
                              onHoverItem: a,
                              onEditItem: r,
                              classMix: Zc,
                              arrowEnabled: null == l ? void 0 : l.isEnabled,
                              isEditable: s,
                            },
                            e,
                          ),
                        ),
                      );
                    }),
                );
              }),
            ),
        );
        let e_;
        !(function (e) {
          ((e.auto = "auto"), (e.left = "left"), (e.right = "right"));
        })(e_ || (e_ = {}));
        const t_ = {
            base: "Carousel_base_8a",
            arrow: "Carousel_arrow_6b",
            arrow__hover: "Carousel_arrow__hover_19",
            arrow__left: "Carousel_arrow__left_dd",
            arrow__right: "Carousel_arrow__right_99",
            arrow__hidden: "Carousel_arrow__hidden_de",
            shadow: "Carousel_shadow_6b",
            shadow__left: "Carousel_shadow__left_18",
            shadow__right: "Carousel_shadow__right_76",
            shadow__hidden: "Carousel_shadow__hidden_01",
            horizontalContent: "Carousel_horizontalContent_82",
            horizontalWrapper__withoutScroll: "Carousel_horizontalWrapper__withoutScroll_a1",
            horizontalWrapper: "Carousel_horizontalWrapper_fb",
            horizontalBar: "Carousel_horizontalBar_8a",
            bookmarksWrapper: "Carousel_bookmarksWrapper_13",
            bookmark: "Carousel_bookmark_04",
            slots: "Carousel_slots_ea",
            slots__transition: "Carousel_slots__transition_21",
            thumb: "Carousel_thumb_39",
            arrowsHint: "Carousel_arrowsHint_6f",
          },
          u_ = "right",
          n_ = "left",
          a_ = (e) => e.offsetLeft - 0.5 * e.offsetWidth,
          r_ = (e, t) => e.offsetLeft - t + 1.5 * e.offsetWidth,
          o_ = R.strings.customization,
          s_ = { allowedButtons: [Kt.LEFT] },
          l_ = (0, r.memo)(
            (0, r.forwardRef)(
              (
                {
                  items: e,
                  arrowsList: t,
                  categories: u,
                  onClick: n,
                  onHoverItem: a,
                  onEditClick: s,
                  scrollApi: l,
                  onArrowClick: i,
                  isCarouselArrowsHintVisible: c,
                  scrollStartItemId: _,
                  selectedItemId: m,
                  firstExpandedItemId: E,
                  tabId: p,
                  lastScrollState: b,
                  isEditable: g,
                  onUpdateItems: A,
                },
                C,
              ) => {
                const h = Et().mediaSize,
                  v = (0, r.useRef)(new Map()),
                  F = (0, r.useRef)(new Map()),
                  D = (0, r.useMemo)(() => e.filter((e) => e.isEquipped), [e]),
                  B = (0, r.useState)(0),
                  w = B[0],
                  y = B[1],
                  S = (0, r.useState)(!1),
                  k = S[0],
                  T = S[1],
                  N = (0, r.useState)(!1),
                  I = N[0],
                  M = N[1],
                  x = (0, r.useState)(!1),
                  O = x[0],
                  R = x[1],
                  L = (0, r.useState)(!1),
                  P = L[0],
                  H = L[1],
                  z = (0, r.useState)([]),
                  W = z[0],
                  U = z[1],
                  V = (0, r.useState)(!1),
                  j = V[0],
                  $ = V[1],
                  G = (0, r.useState)([0, 0]),
                  q = G[0],
                  X = G[1];
                (0, r.useImperativeHandle)(C, () => ({
                  getFirstVisibleItemId: () => {
                    const t = e.find((e) => {
                      const t = v.current.get(e.intCD);
                      return t && t.getBoundingClientRect().left > 0;
                    });
                    return t ? t.intCD : -1;
                  },
                }));
                const Y = { left: q[0], right: q[1] },
                  K = Y.right <= 0 && Y.left <= 0,
                  Z = (function (e, t, u) {
                    const n = e.contentRef,
                      a = e.wrapperRef,
                      o = e.scrollPosition,
                      s = e.clampPosition,
                      l = e.animationScroll,
                      i = e.events,
                      c = (0, r.useState)(Fi),
                      _ = c[0],
                      m = c[1];
                    return (
                      (0, r.useEffect)(() => {
                        const e = n.current;
                        e && (e.style.cursor = "dragging" === _.type ? "move" : "grab");
                      }, [n, _.type]),
                      (0, r.useEffect)(() => {
                        if ("dragging" !== _.type) return;
                        const e = d.O.client.events.mouse.move(([e, u]) => {
                            const r = n.current,
                              i = a.current;
                            if (!r || !i) return;
                            if ("inside" === u && e.clientX < 0) return;
                            const c = "inside" === u ? e.clientX : e.clientX - i.offsetLeft,
                              d = _.positionFrom - c,
                              m = _.previousScrollPosition + d;
                            o.start(
                              Object.assign(
                                {
                                  scrollPosition: s(r, m),
                                  from: { scrollPosition: l.scrollPosition.get() },
                                },
                                t && { config: t },
                              ),
                            );
                          }),
                          u = d.O.client.events.mouse.up(function () {
                            m({ type: "scrollingToEnd" });
                          });
                        return () => {
                          (e(), u());
                        };
                      }, [l.scrollPosition, s, n, _, o, a, t]),
                      (0, r.useEffect)(() => {
                        if ("scrollingToEnd" !== _.type) return;
                        const e = () => {
                          m(Fi);
                        };
                        return (
                          l.scrollPosition.idle && e(),
                          i.on("rest", e),
                          () => i.off("rest", e)
                        );
                      }, [l.scrollPosition, _.type, i]),
                      (0, r.useEffect)(() => {
                        const e = n.current;
                        if (!e) return;
                        const t = (e) => {
                          (u &&
                            u.allowedButtons &&
                            -1 === u.allowedButtons.findIndex((t) => e.button === t)) ||
                            m({
                              type: "dragging",
                              positionFrom: e.screenX,
                              previousScrollPosition: l.scrollPosition.get(),
                            });
                        };
                        return (
                          e.addEventListener("mousedown", t),
                          () => e.removeEventListener("mousedown", t)
                        );
                      }, [l.scrollPosition, n, u]),
                      _
                    );
                  })(l, void 0, s_),
                  J = "dragging" === Z.type,
                  Q = (0, r.useCallback)(() => {
                    const e = l.getWrapperSize();
                    if (!e) return null;
                    let t = !1,
                      u = !1;
                    (D.forEach((n) => {
                      const a = v.current.get(n.intCD);
                      if (!a) return null;
                      const r = a.getBoundingClientRect();
                      (r.right <= 0 && (t = !0), r.left >= e && (u = !0));
                    }),
                      T(t),
                      M(u));
                  }, [D, l]),
                  ee = (e) => {
                    const t = l.getWrapperSize();
                    if (!t) return null;
                    let u = null,
                      n = 1 / 0;
                    if (
                      (D.forEach((a) => {
                        const r = v.current.get(a.intCD);
                        if (!r) return null;
                        const o = r.getBoundingClientRect(),
                          s = o.width / 2;
                        if (e === n_) {
                          if (o.right - s <= 0) {
                            const e = t - o.right;
                            e < n && ((n = e), (u = r));
                          }
                        } else if (o.left + s >= t) {
                          const e = o.left - t;
                          e < n && ((n = e), (u = r));
                        }
                      }),
                      u)
                    ) {
                      const n = u.getBoundingClientRect(),
                        a = e === n_ ? u.offsetLeft - 36 : u.offsetLeft - t + n.width + 29;
                      l.scrollPosition.start({ scrollPosition: Y.right < a ? Y.right : a });
                    }
                  },
                  te = (0, r.useCallback)(() => {
                    const e = l.getContainerSize();
                    if (!e) return;
                    const t = u.length > 1 && !K;
                    if ((t !== j && $(t), !t)) return void (W.length > 0 && U([]));
                    const n = [];
                    (u.forEach((t) => {
                      const u = F.current.get(t.bookmarkIndex);
                      if (u) {
                        let a = (u.offsetLeft + u.offsetWidth / 2) / e;
                        ((a = Math.max(0, Math.min(1, a))),
                          n.push({ name: t.bookmarkName, position: a, index: t.bookmarkIndex }));
                      }
                    }),
                      JSON.stringify(n) !== JSON.stringify(W) && U(n));
                  }, [W, u, K, l, j]),
                  ue = (0, r.useCallback)(
                    (e) => {
                      const t = e.which;
                      (t === fe.n.ARROW_LEFT && i(!0), t === fe.n.ARROW_RIGHT && i(!1));
                    },
                    [i],
                  );
                (0, r.useEffect)(
                  () => (
                    window.addEventListener("keydown", ue),
                    () => window.removeEventListener("keydown", ue)
                  ),
                  [ue],
                );
                const ne = (0, r.useCallback)(() => {
                    const e = l.animationScroll.scrollPosition.goal;
                    y(e);
                    const t = l.getBounds(),
                      u = t[0],
                      n = t[1];
                    (u === Y.left && n === Y.right) || X([u, n]);
                  }, [l, Y.left, Y.right]),
                  ae = (0, r.useCallback)(
                    (t) => {
                      const u = e[t],
                        n = v.current.get(u.intCD);
                      if (n) return { position: n.offsetLeft, isFilled: u.isFilled };
                    },
                    [e],
                  ),
                  re = (0, r.useCallback)(() => {
                    const t = l.getWrapperSize();
                    if (t) {
                      const u = l.animationScroll.scrollPosition.goal;
                      A(u, t, e.length, ae);
                    }
                  }, [l, e, A, ae]),
                  oe = (0, r.useCallback)(() => {
                    (ne(), te(), Q(), re());
                  }, [Q, ne, te, re]);
                (0, r.useEffect)(
                  () => (
                    l.events.on("change", oe),
                    l.events.on("recalculateContent", oe),
                    l.events.on("resizeHandled", oe),
                    () => {
                      (l.events.off("change", oe),
                        l.events.off("recalculateContent", oe),
                        l.events.off("resizeHandled", oe));
                    }
                  ),
                  [oe, l.events],
                );
                const se = (0, r.useCallback)(
                    (e, t = !0, u = e_.auto) => {
                      const n = l.getBounds(),
                        a = n[0],
                        r = n[1];
                      if (!((a <= 0 && r <= 0) || void 0 === e))
                        if (e > 0) {
                          const n = l.getWrapperSize(),
                            a = v.current.get(e);
                          if (a && n) {
                            const e = l.animationScroll.scrollPosition.goal;
                            let r = 0,
                              o = !0;
                            if (u === e_.left) r = a_(a);
                            else if (u === e_.right) r = r_(a, n);
                            else {
                              const t = a.offsetLeft - e < 0,
                                u = a.offsetLeft + a.offsetWidth - e > n;
                              t || u ? (t ? (r = a_(a)) : u && (r = r_(a, n))) : (o = !1);
                            }
                            o &&
                              l.scrollPosition.start({ scrollPosition: r, immediate: t, reset: t });
                          }
                        } else l.applyScroll(0, { immediate: !0, reset: !0 });
                    },
                    [l],
                  ),
                  le = l.getContainerSize(),
                  ie = l.getWrapperSize();
                Di(() => {
                  if (ie && le && b.current)
                    return b.current.firstExpandedItemId !== E
                      ? ((b.current.firstExpandedItemId = E), void (E && se(E, !0, e_.left)))
                      : b.current.selectedItemId !== m
                        ? ((b.current.selectedItemId = m), void (m && se(m, !1, e_.auto)))
                        : b.current.tabId !== p
                          ? ((b.current.tabId = p), void se(_, !0, e_.left))
                          : void 0;
                }, [se, m, E, _, p, le, ie, b]);
                const ce = f()(
                    t_.shadow,
                    t_.shadow__left,
                    (w === Y.left || K) && t_.shadow__hidden,
                  ),
                  _e = f()(t_.shadow, t_.shadow__right, (w === Y.right || K) && t_.shadow__hidden),
                  de = f()(
                    t_.arrow,
                    t_.arrow__left,
                    O && t_.arrow__hover,
                    (!k || K) && t_.arrow__hidden,
                  ),
                  me = f()(
                    t_.arrow,
                    t_.arrow__right,
                    P && t_.arrow__hover,
                    (!I || K) && t_.arrow__hidden,
                  ),
                  Ee = () => {
                    De.playHighlight();
                  };
                return o().createElement(
                  "div",
                  { className: f()(t_.base, J && t_.base__dragging) },
                  c &&
                    o().createElement(
                      "div",
                      { className: t_.arrowsHint },
                      o().createElement(xi, null),
                    ),
                  o().createElement(
                    vi.Horizontal.Area,
                    {
                      api: l,
                      classNames: {
                        wrapper: f()(
                          t_.horizontalWrapper,
                          K && t_.horizontalWrapper__withoutScroll,
                        ),
                        content: t_.horizontalContent,
                      },
                    },
                    o().createElement(
                      "div",
                      { className: t_.slots },
                      o().createElement(Qc, {
                        items: e,
                        categories: u,
                        arrowsList: t,
                        onClick: n,
                        onHoverItem: a,
                        onEditClick: s,
                        isEditable: g,
                        itemsRef: v,
                        categoriesRef: F,
                      }),
                    ),
                  ),
                  o().createElement(vi.Horizontal.Bar, {
                    classNames: { base: t_.horizontalBar, thumb: t_.thumb },
                    api: l,
                  }),
                  j &&
                    o().createElement(
                      "div",
                      { className: t_.bookmarksWrapper },
                      W.map(({ name: e, position: t, index: u }) =>
                        o().createElement(
                          Le,
                          { key: `${e}-${u}`, body: e },
                          o().createElement("div", {
                            onMouseEnter: Ee,
                            onClick: () =>
                              ((e) => {
                                const t = l.getWrapperSize(),
                                  u = l.getContainerSize();
                                if (!t || !u) return;
                                const n = F.current.get(e);
                                if (n) {
                                  De.playClick();
                                  const e = n.offsetLeft + 0.5 * n.offsetWidth,
                                    a = e / u,
                                    r = h >= _t.Medium ? 36 : 29,
                                    o = e - a * (t - 2 * r) - r;
                                  l.scrollPosition.start({ scrollPosition: o });
                                }
                              })(u),
                            className: t_.bookmark,
                            style: { left: 100 * t + "%" },
                          }),
                        ),
                      ),
                    ),
                  o().createElement("div", { className: ce }),
                  o().createElement("div", { className: _e }),
                  o().createElement(
                    Le,
                    { body: o_.tooltips.carousel.arrow() },
                    o().createElement("div", {
                      className: de,
                      onMouseEnter: () => {
                        (R(!0), De.playHighlight());
                      },
                      onMouseLeave: () => {
                        R(!1);
                      },
                      onClick: () => {
                        ee(n_);
                      },
                    }),
                  ),
                  o().createElement(
                    Le,
                    { body: o_.tooltips.carousel.arrow() },
                    o().createElement("div", {
                      className: me,
                      onMouseEnter: () => {
                        (H(!0), De.playHighlight());
                      },
                      onClick: () => {
                        ee(u_);
                      },
                      onMouseLeave: () => {
                        H(!1);
                      },
                    }),
                  ),
                );
              },
            ),
          ),
          i_ = { type: "idle" };
        const c_ = "WarningText_base_5d",
          __ = "WarningText_header_57",
          d_ = "WarningText_headerIcon_2f",
          m_ = "WarningText_description_78",
          E_ = o().memo(({ header: e, description: t }) =>
            o().createElement(
              "div",
              { className: c_ },
              o().createElement(
                "div",
                { className: __ },
                o().createElement("div", { className: d_ }),
                e,
              ),
              o().createElement("div", { className: m_ }, t),
            ),
          ),
          p_ = "ListEmptyState_base_5f",
          b_ = "ListEmptyState_content_22",
          g_ = "ListEmptyState_buttonWrapper_fa",
          A_ = "ListEmptyState_button_cd",
          C_ = R.strings.customization,
          f_ = (0, r.memo)(
            ({
              warningHeader: e,
              warningDescription: t,
              buttonType: u = we.secondary,
              tooltipArgs: n = { body: C_.customization.resetFilter.tooltip.text() },
              className: a,
              onClick: r,
              children: s,
            }) =>
              o().createElement(
                "div",
                { className: f()(p_, a) },
                o().createElement(
                  "div",
                  { className: b_ },
                  o().createElement(E_, { header: e, description: t }),
                  s &&
                    o().createElement(
                      "div",
                      { className: g_ },
                      o().createElement(
                        Le,
                        n,
                        o().createElement(
                          ke,
                          { size: ye.small, type: u, onClick: r, mixClass: A_ },
                          s,
                        ),
                      ),
                    ),
                ),
              ),
          ),
          h_ = {
            base: "CarouselExpandedView_base_31",
            baseBack: "CarouselExpandedView_baseBack_03",
            tabs: "CarouselExpandedView_tabs_e1",
            filterHeader: "CarouselExpandedView_filterHeader_14",
            filterCounter: "CarouselExpandedView_filterCounter_85",
            filterNumbers: "CarouselExpandedView_filterNumbers_5e",
            filterNumbersLabel: "CarouselExpandedView_filterNumbersLabel_93",
            counterGlow: "CarouselExpandedView_counterGlow_6f",
            filtersClearButton: "CarouselExpandedView_filtersClearButton_86",
            filtersClearIcon: "CarouselExpandedView_filtersClearIcon_5b",
            filter: "CarouselExpandedView_filter_c0",
            currency: "CarouselExpandedView_currency_3b",
            closeButton: "CarouselExpandedView_closeButton_bd",
            carouselWrapper: "CarouselExpandedView_carouselWrapper_60",
            scrollArea: "CarouselExpandedView_scrollArea_b4",
            scrollContent: "CarouselExpandedView_scrollContent_4c",
            scrollContent__withoutScroll: "CarouselExpandedView_scrollContent__withoutScroll_2a",
            scrollContent__transition: "CarouselExpandedView_scrollContent__transition_f3",
            categories: "CarouselExpandedView_categories_41",
            category: "CarouselExpandedView_category_b3",
            slots: "CarouselExpandedView_slots_6c",
            slot: "CarouselExpandedView_slot_b3",
            base__dragging: "CarouselExpandedView_base__dragging_36",
            emptyState: "CarouselExpandedView_emptyState_ea",
            scrollbarWrapper: "CarouselExpandedView_scrollbarWrapper_14",
            lip: "CarouselExpandedView_lip_64",
            lip__hidden: "CarouselExpandedView_lip__hidden_0b",
            priceWrapper: "CarouselExpandedView_priceWrapper_85",
            price: "CarouselExpandedView_price_fe",
            bookmarksWrapper: "CarouselExpandedView_bookmarksWrapper_ce",
            bookmark: "CarouselExpandedView_bookmark_7f",
            thumb: "CarouselExpandedView_thumb_9f",
          };
        function v_() {
          return (
            (v_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            v_.apply(this, arguments)
          );
        }
        const F_ = R.strings.customization,
          D_ = (0, i.Pi)(
            ({ onCarouselCollapse: e, startScrollItemId: t, tabId: u, onUpdateItems: n }) => {
              const a = ca(),
                s = a.controls,
                l = a.model,
                i = l.computes.getItems(),
                c = l.computes.getCategories(),
                _ = l.computes.getBillModel(),
                m = Et().mediaSize <= _t.Small ? ye.small : ye.medium,
                E = l.computes.getTabsItemsList(),
                p = l.root.get(),
                b = p.filterModel,
                g = p.carouselModel,
                A = vi.Vertical.useVerticalScrollApi(),
                C = A.getWrapperSize(),
                h = A.getContainerSize(),
                v = l.computes.getBuyPrice(),
                F = (0, r.useRef)(new Map()),
                D = (0, r.useRef)(new Map()),
                B = (0, r.useState)(0),
                w = B[0],
                y = B[1],
                S = (0, r.useState)([]),
                k = S[0],
                T = S[1],
                N = (0, r.useState)(!1),
                I = N[0],
                M = N[1],
                x = (0, r.useState)([0, 0]),
                O = x[0],
                L = x[1],
                P = b.filteredItemsCounter,
                H = b.allItemsCounter,
                z = b.isFilteringActive,
                W = b.newHiddenItemsCounter,
                U = { top: O[0], bottom: O[1] },
                V = U.top <= 0 && U.bottom <= 0,
                j = Object.fromEntries(Object.entries(_).filter(([e]) => "buyPrice" !== e)),
                $ = (0, r.useCallback)(
                  () =>
                    i.find((e) => {
                      const t = F.current.get(e.intCD);
                      return t && t.offsetTop - w > 0;
                    }),
                  [i, w],
                ),
                G = (0, r.useCallback)(() => {
                  var t;
                  e(null == (t = $()) ? void 0 : t.intCD);
                }, [$, e]);
              !(function ({
                key: e = fe.n.ESCAPE,
                callback: t = () => d.O.view.sendEvent.close(),
                preventPropagation: u = !0,
              } = {}) {
                ve(e, t, u);
              })({ callback: G });
              const q = () => {
                  De.playHighlight();
                },
                X = (0, r.useCallback)(
                  (t) => {
                    (t && s.onSelectItem(t), e());
                  },
                  [e, s],
                ),
                Y = (0, r.useCallback)(
                  (t) => {
                    (t && s.onEditItem(t), e());
                  },
                  [s, e],
                ),
                K = (0, r.useCallback)(() => {
                  (s.onShowBuyWindow(), e());
                }, [s, e]),
                Z = (function (e, t) {
                  const u = e.contentRef,
                    n = e.wrapperRef,
                    a = e.scrollPosition,
                    o = e.clampPosition,
                    s = e.animationScroll,
                    l = e.events,
                    i = (0, r.useState)(i_),
                    c = i[0],
                    _ = i[1];
                  return (
                    (0, r.useEffect)(() => {
                      const e = u.current;
                      e && (e.style.cursor = "dragging" === c.type ? "grabbing" : "grab");
                    }, [u, c.type]),
                    (0, r.useEffect)(() => {
                      if ("dragging" !== c.type) return;
                      const e = d.O.client.events.mouse.move(([e, r]) => {
                          const l = u.current,
                            i = n.current;
                          if (!l || !i) return;
                          if ("inside" === r && e.clientY < 0) return;
                          const _ = "inside" === r ? e.clientY : e.clientY - i.offsetTop,
                            d = c.positionFrom - _,
                            m = c.previousScrollPosition + d;
                          a.start(
                            Object.assign(
                              {
                                scrollPosition: o(l, m),
                                from: { scrollPosition: s.scrollPosition.get() },
                              },
                              t && { config: t },
                            ),
                          );
                        }),
                        r = d.O.client.events.mouse.up(function () {
                          _({ type: "scrollingToEnd" });
                        });
                      return () => {
                        (e(), r());
                      };
                    }, [s.scrollPosition, o, u, c, a, n, t]),
                    (0, r.useEffect)(() => {
                      if ("scrollingToEnd" !== c.type) return;
                      const e = () => {
                        _(i_);
                      };
                      return (
                        s.scrollPosition.idle && e(),
                        l.on("rest", e),
                        () => l.off("rest", e)
                      );
                    }, [s.scrollPosition, c.type, l]),
                    (0, r.useEffect)(() => {
                      const e = u.current;
                      if (!e) return;
                      const t = (e) => {
                        _({
                          type: "dragging",
                          positionFrom: e.screenY,
                          previousScrollPosition: s.scrollPosition.get(),
                        });
                      };
                      return (
                        e.addEventListener("mousedown", t),
                        () => e.removeEventListener("mousedown", t)
                      );
                    }, [s.scrollPosition, u]),
                    c
                  );
                })(A),
                J = "dragging" === Z.type,
                Q = (0, r.useCallback)(() => {
                  const e = A.getContainerSize();
                  if (!e) return;
                  const t = c.length > 1 && !V;
                  if ((t !== I && M(t), !t)) return void (k.length > 0 && T([]));
                  const u = [];
                  (c.forEach((t) => {
                    const n = D.current.get(t.bookmarkIndex);
                    if (n) {
                      let a = (n.offsetTop + n.offsetHeight / 2) / e;
                      ((a = Math.max(0, Math.min(1, a))),
                        u.push({ name: t.bookmarkName, position: a, index: t.bookmarkIndex }));
                    }
                  }),
                    JSON.stringify(u) !== JSON.stringify(k) && T(u));
                }, [k, c, V, A, I]),
                ee = (0, r.useCallback)(() => {
                  const e = A.animationScroll.scrollPosition.goal;
                  y(e);
                  const t = A.getBounds(),
                    u = t[0],
                    n = t[1];
                  (u === U.top && n === U.bottom) || L([u, n]);
                }, [A, U.top, U.bottom]),
                te = (0, r.useCallback)(
                  (e) => {
                    const t = i[e],
                      u = F.current.get(t.intCD);
                    if (u) return { position: u.offsetTop, isFilled: t.isFilled };
                  },
                  [i],
                ),
                ue = (0, r.useCallback)(() => {
                  const e = A.getWrapperSize();
                  if (e) {
                    const t = A.animationScroll.scrollPosition.goal;
                    n(t, e, i.length, te);
                  }
                }, [A, i, n, te]),
                ne = (0, r.useCallback)(() => {
                  (ee(), Q(), ue());
                }, [ee, Q, ue]);
              (0, r.useEffect)(
                () => (
                  A.events.on("change", ne),
                  A.events.on("recalculateContent", ne),
                  A.events.on("resizeHandled", ne),
                  () => {
                    (A.events.off("change", ne),
                      A.events.off("recalculateContent", ne),
                      A.events.off("resizeHandled", ne));
                  }
                ),
                [ne, ee, A.events],
              );
              const ae = (0, r.useState)(t),
                re = ae[0],
                oe = ae[1];
              (Di(() => {
                if (re > -1 && C && h && !V) {
                  const e = F.current.get(re);
                  if (e) {
                    const t = e.offsetTop - 0.5 * e.offsetHeight;
                    (A.applyScroll(t, { immediate: !0, reset: !0 }), oe(-1));
                  }
                }
              }, [t, C, h, V, A]),
                Di(() => {
                  A.applyScroll(0, { immediate: !0, reset: !0 });
                }, [u, A]));
              const se = f()(h_.lip, (w === U.bottom || V) && h_.lip__hidden);
              return o().createElement(
                "div",
                { className: f()(h_.base, J && h_.base__dragging) },
                o().createElement("div", { className: h_.baseBack }),
                o().createElement(zr, {
                  tabs: E,
                  onClick: (e) => {
                    (Fe(R.sounds.cust_tab_switch()), s.selectTab(e));
                  },
                  onHoverTab: s.hoverTab,
                  mixClass: h_.tabs,
                }),
                o().createElement(
                  "div",
                  { className: h_.filterHeader },
                  o().createElement(
                    "div",
                    { className: h_.filterCounter },
                    o().createElement(ra, {
                      title:
                        z &&
                        o().createElement(
                          Le,
                          { body: F_.customization.resetFilter.tooltip.text() },
                          o().createElement(
                            ke,
                            {
                              type: we.ghost,
                              onClick: s.clearFilter,
                              mixClass: f()(h_.filtersClearButton),
                            },
                            o().createElement("div", { className: h_.filtersClearIcon }),
                          ),
                        ),
                      label: o().createElement(Wt, {
                        text: F_.filters.selectedTitle(),
                        className: h_.filterNumbersLabel,
                      }),
                      from: P,
                      to: H,
                      isFilterRange: !0,
                      isGlowVisible: z,
                      isSelectMode: !1,
                      className: h_.filterNumbers,
                      classNames: { counterGlow: h_.counterGlow },
                      isHideTotalCounter: !z,
                      isSelectedLimitReached: W > 0,
                      isAnimationEnabled: W > 0,
                    }),
                  ),
                  o().createElement(
                    "div",
                    { className: h_.filter },
                    o().createElement(Ca, { isReverse: !0, buttonSize: m }),
                  ),
                ),
                o().createElement(
                  "div",
                  { className: h_.carouselWrapper },
                  i.length > 0
                    ? o().createElement(
                        o().Fragment,
                        null,
                        o().createElement(
                          vi.Vertical.Area,
                          {
                            api: A,
                            className: f()(h_.scrollArea, V && h_.scrollArea__withoutScroll),
                            classNames: {
                              content: f()(h_.scrollContent, V && h_.scrollContent__withoutScroll),
                            },
                          },
                          c.map((e, t) => {
                            var u;
                            const n = g.isProgressionDecalsBannerVisible && e.isProgressive;
                            return o().createElement(
                              "div",
                              { className: h_.categories, key: `${t}` },
                              "" !== e.bookmarkName &&
                                o().createElement(
                                  "div",
                                  {
                                    className: h_.category,
                                    ref: (t) => {
                                      t
                                        ? D.current.set(e.bookmarkIndex, t)
                                        : D.current.delete(e.bookmarkIndex);
                                    },
                                  },
                                  e.bookmarkName,
                                ),
                              o().createElement(
                                "div",
                                { className: h_.slots },
                                n &&
                                  o().createElement(ks, {
                                    mixClass: h_.slot,
                                    onClick: s.clickDecalsBanner,
                                  }),
                                i
                                  .slice(
                                    e.bookmarkIndex,
                                    null == (u = c[t + 1]) ? void 0 : u.bookmarkIndex,
                                  )
                                  .map((e, u) =>
                                    o().createElement(
                                      "div",
                                      {
                                        key: `${t}_${u}`,
                                        ref: (t) => {
                                          t ? F.current.set(e.intCD, t) : F.current.delete(e.intCD);
                                        },
                                      },
                                      o().createElement(
                                        $c,
                                        v_(
                                          {
                                            onSelectItem: X,
                                            onEditItem: Y,
                                            onHoverItem: s.hoverItem,
                                            classMix: h_.slot,
                                          },
                                          e,
                                        ),
                                      ),
                                    ),
                                  ),
                              ),
                            );
                          }),
                        ),
                        o().createElement(
                          "div",
                          { className: h_.scrollbarWrapper },
                          I &&
                            o().createElement(
                              "div",
                              { className: h_.bookmarksWrapper },
                              k.map(({ name: e, position: t, index: u }) =>
                                o().createElement(
                                  Le,
                                  { key: `${e}-${u}`, body: e },
                                  o().createElement("div", {
                                    onMouseEnter: q,
                                    onClick: () =>
                                      ((e) => {
                                        const t = A.getWrapperSize(),
                                          u = A.getContainerSize();
                                        if (!t || !u) return;
                                        const n = D.current.get(e);
                                        if (n) {
                                          De.playClick();
                                          const e = n.offsetTop + n.offsetHeight / 2,
                                            a = e - (e / u) * (t - 34) - 17;
                                          A.scrollPosition.start({ scrollPosition: a });
                                        }
                                      })(u),
                                    className: h_.bookmark,
                                    style: { top: 100 * t + "%" },
                                  }),
                                ),
                              ),
                            ),
                          o().createElement(vi.Vertical.Bar, {
                            classNames: { thumb: h_.thumb },
                            api: A,
                          }),
                        ),
                      )
                    : o().createElement(
                        f_,
                        {
                          warningHeader: F_.customization.message.header(),
                          warningDescription: F_.customization.message.description(),
                          buttonType: we.secondary,
                          onClick: s.clearFilter,
                          className: h_.emptyState,
                        },
                        o().createElement(Wt, { text: F_.customization.resetFiltersBtn.label() }),
                      ),
                ),
                o().createElement(Ce, {
                  id: R.views.lobby.customization.CustomizationMoneyBalance("resId"),
                  mixClass: h_.currency,
                }),
                o().createElement(
                  "div",
                  { className: h_.closeButton },
                  o().createElement($t, {
                    side: "right",
                    type: "close",
                    caption: F_.customization.closeButton(),
                    onClick: G,
                  }),
                ),
                o().createElement(
                  "div",
                  { className: h_.priceWrapper },
                  o().createElement("div", { className: se }),
                  o().createElement(
                    "div",
                    { className: h_.price },
                    v &&
                      o().createElement(Uu, {
                        price: v,
                        onResetHandler: s.onClearBasket,
                        onBackHandler: s.onCancelChanges,
                        cartParams: j,
                        onApplyHandler: K,
                        buttonSize: m,
                      }),
                  ),
                ),
              );
            },
          );
        let B_;
        !(function (e) {
          ((e[(e.UnselectedEmpty = 0)] = "UnselectedEmpty"),
            (e[(e.SelectedEmpty = 1)] = "SelectedEmpty"),
            (e[(e.UnselectedFilled = 2)] = "UnselectedFilled"),
            (e[(e.SelectedFilled = 3)] = "SelectedFilled"),
            (e[(e.Preview = 4)] = "Preview"),
            (e[(e.Locked = 5)] = "Locked"),
            (e[(e.Removed = 6)] = "Removed"),
            (e[(e.Edit = 7)] = "Edit"));
        })(B_ || (B_ = {}));
        const w_ = "ArrowMarker_base_a2",
          y_ = "ArrowMarker_base__scaled_c5",
          S_ = "ArrowMarker_content_b3",
          k_ = "ArrowMarker_arrow_93",
          T_ = "ArrowMarker_arrow__left_88",
          N_ = "ArrowMarker_arrow__right_6b",
          I_ = "ArrowMarker_arrow__leftPressed_e7",
          M_ = "ArrowMarker_arrow__rightPressed_7b",
          x_ = "ArrowMarker_arrow__leftDisabled_7d",
          O_ = "ArrowMarker_arrow__rightDisabled_11",
          R_ = "ArrowMarker_arrowHover_48",
          L_ = "ArrowMarker_arrowHover__left_36",
          P_ = "ArrowMarker_arrowHover__right_a5",
          H_ = "ArrowMarker_arrowHitArea_66",
          z_ = "ArrowMarker_arrowHitArea__left_a8",
          W_ = "ArrowMarker_arrowHitArea__right_e5";
        function U_() {
          return (
            (U_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            U_.apply(this, arguments)
          );
        }
        let V_;
        !(function (e) {
          ((e.left = "left"), (e.right = "right"));
        })(V_ || (V_ = {}));
        const j_ = (0, i.Pi)(() => {
            const e = ca(),
              t = e.model,
              u = e.controls,
              n = t.carouselModel.get(),
              a = n.isRightAvailable,
              s = n.isLeftAvailable,
              l = (0, r.useState)({ left: !1, right: !1 }),
              i = l[0],
              c = l[1],
              _ = (0, r.useState)({ left: !1, right: !1 }),
              d = _[0],
              m = _[1],
              E = Zn(),
              p = (e) => ({
                onMouseEnter: () =>
                  ((e) => {
                    c((t) => Object.assign({}, t, { [e]: !0 }));
                  })(e),
                onMouseLeave: () =>
                  ((e) => {
                    (c((t) => Object.assign({}, t, { [e]: !1 })),
                      m((t) => Object.assign({}, t, { [e]: !1 })));
                  })(e),
                onMouseDown: () =>
                  ((e) => {
                    m((t) => Object.assign({}, t, { [e]: !0 }));
                  })(e),
                onMouseUp: () =>
                  ((e) => {
                    m((t) => Object.assign({}, t, { [e]: !1 }));
                  })(e),
                onClick: () =>
                  ((e) => {
                    (Fe(R.sounds.cust_select()), u.onPressSelectNextItem(e === V_.left));
                  })(e),
              });
            return o().createElement(
              "div",
              { className: f()(w_, E > 1 && y_) },
              o().createElement(
                "div",
                { className: S_ },
                o().createElement("div", { className: f()(k_, T_, d.left && I_, !s && x_) }),
                o().createElement("div", { className: f()(k_, N_, d.right && M_, !a && O_) }),
                o().createElement("div", { className: f()(R_, i.left && !d.left && s && L_) }),
                o().createElement("div", { className: f()(R_, i.right && !d.right && a && P_) }),
                o().createElement("div", U_({ className: f()(H_, z_) }, p(V_.left))),
                o().createElement("div", U_({ className: f()(H_, W_) }, p(V_.right))),
              ),
            );
          }),
          $_ = {
            base: "EditMarker_base_77",
            underline: "EditMarker_underline_58",
            underline__1: "EditMarker_underline__1_bf",
            underline__2: "EditMarker_underline__2_a8",
            underline__3: "EditMarker_underline__3_7f",
            underline__errorAnimation: "EditMarker_underline__errorAnimation_ea",
            shake: "EditMarker_shake_85",
          },
          G_ = (0, i.Pi)(() => {
            const e = ca(),
              t = e.model,
              u = e.controls,
              n = t.computes.getEditData(),
              a = (0, r.useCallback)(
                (e) => {
                  const t = e.which;
                  if ((t === fe.n.ENTER && u.onEnterInput(), t >= fe.n.KEY_0 && t <= fe.n.KEY_9)) {
                    const e = t - fe.n.KEY_1 + 1;
                    u.onAddChar(String(e));
                  } else if (t >= fe.n.NUMPAD_0 && t <= fe.n.NUMPAD_9) {
                    const e = t - fe.n.NUMPAD_0;
                    u.onAddChar(String(e));
                  } else
                    (t === fe.n.DELETE && u.onDeleteAllChars(),
                      t === fe.n.BACKSPACE && u.onRemoveChar());
                },
                [u],
              );
            (0, r.useEffect)(
              () => (
                window.addEventListener("keydown", a),
                () => window.removeEventListener("keydown", a)
              ),
              [a],
            );
            const s = n.inscriptionState === us.NotAvailableEnter;
            return o().createElement(
              "div",
              { className: $_.base },
              o().createElement("div", {
                key: s ? n.startTimestamp : "",
                className: f()(
                  $_.underline,
                  $_[`underline__${n.editDigitsCount}`],
                  s && $_.underline__errorAnimation,
                ),
              }),
            );
          }),
          q_ = {
            base: "Marker_base_2a",
            markerItem: "Marker_markerItem_89",
            inscription: "Marker_inscription_c6",
            show: "Marker_show_37",
            hide: "Marker_hide_dc",
            inscriptionText: "Marker_inscriptionText_ae",
            editMarkerWrapper: "Marker_editMarkerWrapper_fd",
            arrowMarkerWrapper: "Marker_arrowMarkerWrapper_92",
            defaultMarker: "Marker_defaultMarker_06",
            defaultMarkerIcon: "Marker_defaultMarkerIcon_78",
            base__hovered: "Marker_base__hovered_2e",
            base__state2: "Marker_base__state2_d8",
            defaultMarkerIcon__Camouflage: "Marker_defaultMarkerIcon__Camouflage_ac",
            base__state3: "Marker_base__state3_5b",
            defaultMarkerIcon__Modification: "Marker_defaultMarkerIcon__Modification_77",
            defaultMarkerIcon__Paint: "Marker_defaultMarkerIcon__Paint_46",
            defaultMarkerIcon__Style: "Marker_defaultMarkerIcon__Style_3f",
            defaultMarkerIcon__Emblem: "Marker_defaultMarkerIcon__Emblem_36",
            base__state0: "Marker_base__state0_50",
            opacityFrom05to1: "Marker_opacityFrom05to1_1a",
            base__state1: "Marker_base__state1_95",
            scaleFrom02to1: "Marker_scaleFrom02to1_e9",
            base__state6: "Marker_base__state6_13",
            defaultMarkerIcon__Inscription: "Marker_defaultMarkerIcon__Inscription_58",
            base__state4: "Marker_base__state4_c9",
            defaultMarkerIcon__ProjectionDecal: "Marker_defaultMarkerIcon__ProjectionDecal_d3",
            defaultMarkerIcon__withAnimation: "Marker_defaultMarkerIcon__withAnimation_2f",
            scaleFrom05to1: "Marker_scaleFrom05to1_89",
            base__state5: "Marker_base__state5_5a",
            brightnessFrom1to17: "Marker_brightnessFrom1to17_3d",
            scaleFrom08to1: "Marker_scaleFrom08to1_d0",
            interactive: "Marker_interactive_87",
          };
        let X_;
        !(function (e) {
          ((e.EMBLEM = "Emblem"),
            (e.INSCRIPTION = "Inscription"),
            (e.PROJECTION_DECAL = "ProjectionDecal"));
        })(X_ || (X_ = {}));
        const Y_ = [X_.EMBLEM, X_.PROJECTION_DECAL, X_.INSCRIPTION],
          K_ = (0, r.memo)(
            ({
              isHovered: e,
              index: t,
              isActiveInscription: u,
              onMarkerClick: n,
              onMarkerHover: a,
              onMarkerDragOut: s,
              state: l,
              slotType: i,
              scale: c,
            }) => {
              const _ = (0, r.useState)(!1),
                d = _[0],
                m = _[1],
                E = (0, r.useRef)(l),
                p = (0, r.useState)(!1),
                b = p[0],
                g = p[1],
                A = Y_.includes(i);
              (0, r.useEffect)(() => {
                ((E.current === B_.Preview && l === B_.UnselectedFilled) ||
                (E.current === B_.Locked && l === B_.UnselectedEmpty)
                  ? g(!0)
                  : g(!1),
                  (E.current = l));
              }, [l]);
              return o().createElement(
                "div",
                { className: q_.markerItem },
                o().createElement(
                  "div",
                  {
                    className: f()(q_.base, q_[`base__state${l}`], e && q_.base__hovered),
                    onClick: () => {
                      (l === B_.UnselectedFilled && Fe(R.sounds.cust_select()),
                        l === B_.Removed && Fe(R.sounds.cust_select_remove()),
                        l === B_.Locked ? (Fe(R.sounds.cust_negative()), n(t)) : n(t));
                    },
                    onMouseEnter: () => {
                      (De.playHighlight(), a(t, !0));
                    },
                    onMouseLeave: () => {
                      (a(t, !1), d && s(t));
                    },
                    onMouseDown: () => {
                      m(!0);
                    },
                    onMouseUp: () => {
                      m(!1);
                    },
                    style: c
                      ? {
                          opacity: c.opacity,
                          transform: "translate(-50%, -50%) scale(" + c.scale + ")",
                        }
                      : {},
                  },
                  l !== B_.Edit &&
                    o().createElement(
                      "div",
                      { className: q_.defaultMarker },
                      o().createElement("div", {
                        className: f()(
                          q_.defaultMarkerIcon,
                          q_[`defaultMarkerIcon__${i}`],
                          b && q_.defaultMarkerIcon__withAnimation,
                        ),
                        onAnimationEndCapture: () => {
                          g(!1);
                        },
                      }),
                    ),
                  l === B_.Edit &&
                    o().createElement(
                      "div",
                      { className: q_.editMarkerWrapper },
                      o().createElement(G_, null),
                    ),
                  l === B_.SelectedFilled &&
                    A &&
                    o().createElement(
                      "div",
                      { className: q_.arrowMarkerWrapper },
                      o().createElement(j_, null),
                    ),
                  o().createElement("div", { className: q_.interactive }),
                ),
                u &&
                  l === B_.Locked &&
                  o().createElement(
                    "div",
                    { className: q_.inscription },
                    o().createElement(Wt, {
                      className: q_.inscriptionText,
                      text: R.strings.vehicle_customization.notification.slotIsFilled.title(),
                    }),
                  ),
              );
            },
          ),
          Z_ = "MarkersList_markerWrapper_90",
          J_ = (0, i.Pi)(({ isSceneDraggingChange: e }) => {
            const t = ca(),
              u = t.model,
              n = t.controls,
              a = u.customizationTypes.get(),
              s = (0, r.useState)(0),
              l = s[0],
              i = s[1],
              c = (0, r.useState)([]),
              _ = c[0],
              d = c[1],
              m = (0, r.useState)([]),
              E = m[0],
              p = m[1],
              b = (0, r.useState)([]),
              g = b[0],
              A = b[1],
              C = (0, r.useRef)(e),
              f = (0, r.useRef)(_);
            (0, r.useEffect)(() => {
              f.current = _;
            }, [_]);
            const h = (0, r.useRef)([]),
              v = (0, r.useRef)([]),
              F = (0, r.useRef)(0),
              D = (0, r.useState)(null),
              B = D[0],
              w = D[1],
              y = (0, r.useRef)([]),
              S = (0, r.useRef)([]),
              k = (0, r.useState)([]),
              T = k[0],
              N = k[1];
            ((0, r.useEffect)(() => {
              if (e)
                return fa(() => {
                  C.current = e;
                }, 300);
              C.current = e;
            }, [e]),
              ((e) => {
                const t = (0, r.useRef)(0),
                  u = (0, r.useRef)(0),
                  n = (0, r.useRef)(0),
                  a = (0, r.useRef)(0),
                  o = (r) => {
                    if (u.current) {
                      const t = r - u.current;
                      ((n.current += t), (a.current = a.current + t), (a.current = 0), e());
                    }
                    ((u.current = r), (t.current = requestAnimationFrame(o)));
                  };
                (0, r.useEffect)(
                  () => (
                    (t.current = requestAnimationFrame(o)),
                    () => cancelAnimationFrame(t.current)
                  ),
                  [],
                );
              })(() => {
                if (C.current) return;
                const e = u.computes.getMarkersList().filter((e) => 0 !== e.slotType);
                (e.length !== F.current &&
                  ((h.current = Array(e.length).fill("0")),
                  A(Array(e.length).fill(0)),
                  (v.current = Array(e.length).fill(!1)),
                  p(Array(e.length).fill(!1)),
                  (f.current = Array(e.length).fill(0)),
                  d(Array(e.length).fill(0)),
                  (F.current = e.length),
                  i(e.length)),
                  e.forEach((t, u) => {
                    const n = y.current[u];
                    if (!n) return;
                    const r = `${t.posx.toFixed(1)}rem`,
                      o = `${t.posy.toFixed(1)}rem`,
                      s = `${t.opacity.toFixed(2)}`,
                      l = `${t.scale.toFixed(2)}`,
                      i = `${t.areaId}`,
                      c = `${t.zIndex}`,
                      _ = Object.keys(a).find((e) => a[e] === t.slotType);
                    if (void 0 === _) throw Error(`invalid slotType ${t.slotType} of ${t.state}`);
                    const m = `${t.regionIdx}`,
                      E = t.state,
                      b = t.isHovered,
                      g = S.current[u] || { lastOpacityUpdate: 0 },
                      C = "flex" === n.style.display;
                    t.isVisible
                      ? ((n.style.display = "flex"),
                        (g.opacity === s && C) ||
                          ((n.style.opacity = "1"),
                          N((e) => {
                            var t;
                            return (
                              e[u] && null != (t = Object.keys(e[u])) && t.length
                                ? (e[u] = Object.assign({}, e[u], { opacity: s }))
                                : (e[u] = { opacity: s }),
                              e
                            );
                          })),
                        (g.x === r && C) || n.style.setProperty("--x", r),
                        (g.y === o && C) || n.style.setProperty("--y", o),
                        (g.zIndex === c && C) || n.style.setProperty("--zIndex", c),
                        (g.scale === l && C) ||
                          (n.style.setProperty("--scale", "1"),
                          N(
                            (e) => (
                              e[u] && Object.keys(e[u]).length
                                ? (e[u] = Object.assign({}, e[u], { scale: l }))
                                : (e[u] = { scale: l }),
                              e
                            ),
                          )),
                        (n.getAttribute("areaId") === i && e.length === F.current && C) ||
                          n.setAttribute("areaId", i),
                        (n.getAttribute("slotType") === _ && e.length === F.current && C) ||
                          n.setAttribute("slotType", _),
                        (n.getAttribute("regionIdx") === m && e.length === F.current && C) ||
                          n.setAttribute("regionIdx", m),
                        (S.current[u] = {
                          x: r,
                          y: o,
                          opacity: s,
                          scale: l,
                          lastOpacityUpdate: g.lastOpacityUpdate || 0,
                          lastScaleUpdate: g.lastScaleUpdate || 0,
                          areaId: i,
                          slotType: _,
                          regionIdx: m,
                          state: E,
                          zIndex: c,
                        }),
                        f.current[u] !== E &&
                          d((e) => {
                            const t = [...e];
                            return ((t[u] = E), t);
                          }),
                        h.current[u] !== _ &&
                          A((e) => {
                            const t = [...e];
                            return ((t[u] = _), t);
                          }),
                        v.current[u] !== b &&
                          p((e) => {
                            const t = [...e];
                            return ((t[u] = b), t);
                          }),
                        (f.current[u] = E),
                        (h.current[u] = _),
                        (v.current[u] = b))
                      : (n.style.display = "none");
                  }));
              }));
            const I = (0, r.useRef)(null),
              M = (0, r.useCallback)(
                (e) => {
                  I.current && clearTimeout(I.current);
                  const t = y.current[e];
                  if (!t) return;
                  if (f.current[e] === B_.Locked)
                    (w(null),
                      w(e),
                      (I.current = setTimeout(() => {
                        w((t) => (t === e ? null : t));
                      }, 2300)));
                  else {
                    const e = Number(t.getAttribute("areaId")),
                      u = t.getAttribute("slotType"),
                      r = Number(t.getAttribute("regionIdx"));
                    a[u] && n.selectAnchor(e, a[u], r);
                  }
                },
                [n, a],
              ),
              x = (0, r.useCallback)(
                (e, t) => {
                  if (y.current.length > e && e >= 0) {
                    const u = y.current[e],
                      r = Number(u.getAttribute("areaId")),
                      o = u.getAttribute("slotType"),
                      s = Number(u.getAttribute("regionIdx"));
                    a[o] && n.hoverAnchor(r, a[o], s, t);
                  }
                },
                [n, a],
              ),
              O = (0, r.useCallback)(
                (e) => {
                  if (y.current.length > e && e >= 0) {
                    const t = y.current[e],
                      u = Number(t.getAttribute("areaId")),
                      r = t.getAttribute("slotType"),
                      o = Number(t.getAttribute("regionIdx"));
                    a[r] && n.dragAnchor(u, a[r], o);
                  }
                },
                [n, a],
              );
            return o().createElement(
              o().Fragment,
              null,
              Array.from({ length: l }).map((e, t) =>
                o().createElement(
                  "div",
                  { key: t, className: Z_, ref: (e) => (y.current[t] = e) },
                  o().createElement(K_, {
                    index: t,
                    isActiveInscription: B === t,
                    onMarkerClick: () => M(t),
                    onMarkerHover: x,
                    onMarkerDragOut: O,
                    state: _[t],
                    isHovered: E[t],
                    slotType: g[t],
                    scale: T[t],
                  }),
                ),
              ),
            );
          });
        function Q_() {
          return (
            (Q_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Q_.apply(this, arguments)
          );
        }
        let ed;
        !(function (e) {
          ((e.CAMOUFLAGE = "camouflage"),
            (e.PROJECTION_DECAL = "projectionDecal"),
            (e.INSCRIPTION = "inscription"));
        })(ed || (ed = {}));
        const td = "mainview:close",
          ud = "close_dialog",
          nd = [ed.CAMOUFLAGE, ed.PROJECTION_DECAL],
          ad = R.strings.customization,
          rd = R.strings.customization.tooltips.filters;
        viewEnv.clearInternalCacheAfterFinalize();
        (0, i.Pi)(() => {
          var e, t;
          const u = ca(),
            n = u.controls,
            a = u.model,
            s = Et().mediaSize,
            l = a.root.get(),
            i = l.isBuyViewActive,
            c = l.isStyleInfoViewActive,
            _ = l.isEditable,
            m = l.isApplyToAllSeasonsAvailable,
            E = l.isApplyToAllSeasonsSelected,
            p = l.isShowProgressionInfoButton,
            b = l.isHoverVehicleSlot,
            g = l.isProgressiveItemsViewVisible,
            A = l.isFilterPopoverOpened,
            C = l.isOnboardingViewOpened,
            h = l.isCustomizationResourceEntryPointAvailable,
            v = (0, r.useRef)(null),
            F = a.computes.getStageSwitcher(),
            D = a.computes.getSelectedTabItemType(),
            B = F.isVisible,
            w = F.selectedLevel,
            y = F.numberOfBullets,
            S = F.isBulletsBeforeCurrentDisabled,
            k = F.currentLevel,
            T = a.toolbarModel.get(),
            N = T.isToolbarPanelEnabled,
            I = T.isInscriptionPanelEnabled,
            M = a.carouselModel.get(),
            x = M.scrollStartItemId,
            O = M.isCarouselArrowsHintVisible,
            L = a.computes.getSelectedItemId(),
            P = (0, r.useState)(-1),
            H = P[0],
            z = P[1],
            W = (0, r.useRef)({
              tabId: void 0,
              scrollStartItemId: void 0,
              selectedItemId: void 0,
              firstExpandedItemId: void 0,
            }),
            U = (0, r.useState)(!1),
            V = U[0],
            j = U[1],
            $ = (0, r.useState)(!1),
            G = $[0],
            q = $[1],
            X = (0, r.useState)(!1),
            Y = X[0],
            K = X[1],
            Z = (0, r.useState)(!1),
            J = Z[0],
            Q = Z[1],
            ee = a.computes.getBuyPrice(),
            te = a.computes.getItems(),
            ue = a.computes.getCategories(),
            ne = a.computes.getArrowsList(),
            ae = a.computes.getTabsItemsList(),
            re = a.computes.getBillModel(),
            oe = a.computes.getSeasonsTabsItemsList(),
            le = a.computes.getToolbarButtonsList(),
            ie = a.magneticToolModel.get(),
            ce = a.headerVehicleInfo.get(),
            _e = ce.description,
            de = ce.isStyleBonusPreviewText,
            me = ce.vehicle,
            Ee = s <= _t.Small ? ye.small : ye.medium,
            pe = Yt(),
            be = N && !I && !V && !i && !c,
            ge = se(be),
            Ae = se(ie.isEnabled),
            he = a.computes.getEditData(),
            ve = !V && !be && !he.inscriptionState;
          localStorage.removeItem(ud);
          const De = (0, r.useCallback)(
              (e) => {
                (z(e || -1), n.onExpandCarousel(!1), j(!1));
              },
              [n],
            ),
            Be = (0, r.useCallback)(
              (e, t) => {
                (n.onToolbarItemClick(e, t),
                  e === Gt.CUSTOMIZATION_SHEET_ACTION_CLOSE && n.onSceneOverChange(!0));
              },
              [n],
            ),
            Se = (0, r.useCallback)(() => {
              const e = localStorage.getItem(ud);
              engine.trigger(td);
              const t =
                a.computes
                  .getMarkersList()
                  .filter((e) => "1" === e.state.toString() || "3" === e.state.toString()).length >
                0;
              if (!V) {
                if (be)
                  return (
                    n.onToolbarItemClick(Gt.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1),
                    Be(Gt.CUSTOMIZATION_SHEET_ACTION_CLOSE, 0),
                    void n.onUnselectItem()
                  );
                if (
                  a.computes.getToolbarData().isInscriptionPanelEnabled &&
                  2 !== a.computes.getEditData().inscriptionState &&
                  1 !== a.computes.getEditData().inscriptionState
                )
                  n.onSceneClick();
                else if (
                  (!_ &&
                    0 === a.computes.getEditData().inscriptionState &&
                    !a.computes.getToolbarData().isToolbarPanelEnabled) ||
                  ((2 === a.computes.getEditData().inscriptionState ||
                    1 === a.computes.getEditData().inscriptionState) &&
                    n.onCancelChanges(),
                  n.closeEditItem(),
                  i)
                )
                  if (ie.isEnabled) n.onUnselectItem();
                  else {
                    if (!t)
                      return (
                        i
                          ? n.closeBinEsc()
                          : c
                            ? n.onCloseStyleInfoEsc()
                            : ((e && "0" !== e) || n.onClose(), localStorage.setItem(ud, "1")),
                        () => {
                          (engine.off(td), localStorage.setItem(ud, "0"));
                        }
                      );
                    n.onSceneClick();
                  }
              }
            }, [n, i, V, _, be, c, ie.isEnabled, a.computes, Be]);
          (0, r.useEffect)(() => {
            g && viewEnv.clearInternalCaches();
          }, [g]);
          const Te = nt(
            (e, t, u, n) => {
              if (t) {
                var a;
                let r = 0,
                  o = u,
                  s = !1,
                  l = 0;
                for (; l < u;) {
                  const u = n(l);
                  if (u) {
                    const n = u.position - e < 0,
                      a = u.position - e > t;
                    if ((n && l > r ? (r = l) : s || (s = !u.isFilled), a)) {
                      o = l;
                      break;
                    }
                  }
                  l++;
                }
                s || (s = !(null != (a = n(r)) && a.isFilled));
                let i = r,
                  c = 0;
                for (; c < 5 && i > 0;) (i--, c++);
                ((r = i), s && Ne(r, o));
              }
            },
            [(Ne = n.onRequestItems)],
            200,
          );
          var Ne;
          !(function ({
            key: e = fe.n.ESCAPE,
            callback: t = () => d.O.view.sendEvent.close(),
            preventPropagation: u = !0,
          } = {}) {
            cd(e, t, u);
          })({ callback: Se, preventPropagation: !1 });
          const Ie = lt(),
            Me = nt(
              () => {
                i ? n.buyItems() : n.onShowBuyWindow();
              },
              [i],
              300,
            ),
            xe = (0, r.useCallback)(
              (e) => {
                n.selectSeason(e);
              },
              [n],
            ),
            Oe = (0, r.useCallback)(
              (e) => {
                e && n.onSelectItem(e);
              },
              [n],
            ),
            Re = (0, r.useCallback)(
              (e) => {
                !C && n.onSceneOverChange(e);
              },
              [n, C],
            );
          ((0, r.useEffect)(() => {
            n.onSceneOverChange(!A);
          }, [A, n]),
            (0, r.useEffect)(() => {
              n.onSceneOverChange(!C);
            }, [C, n]),
            (0, r.useEffect)(() => {
              !Ae && ie.isEnabled && V && De();
            }, [De, V, ie.isEnabled, Ae]),
            (0, r.useEffect)(() => {
              be && !ge
                ? nd.includes(D)
                  ? Fe(R.sounds.radial_big())
                  : Fe(R.sounds.radial_small())
                : !be &&
                  ge &&
                  (nd.includes(D) ? Fe(R.sounds.radial_big_close()) : Fe(R.sounds.radial_small()));
            }, [be, ge, D]),
            (0, r.useEffect)(() => {
              if (pe.isRunning) return () => pe.clear();
            }, [pe]),
            (0, r.useEffect)(() => {
              (i && q(!0),
                i ||
                  pe.run(() => {
                    q(!1);
                  }, 400));
            }, [i, pe]),
            (0, r.useEffect)(() => {
              (c && (V && De(), Q(!0)),
                c ||
                  pe.run(() => {
                    Q(!1);
                  }));
            }, [c, pe, V, De]));
          const Pe = Object.fromEntries(Object.entries(re).filter(([e]) => "buyPrice" !== e)),
            He = (0, r.useCallback)(
              (e) => {
                n.onStageChange(e);
              },
              [n],
            ),
            ze = (0, r.useCallback)(() => {
              (n.onToolbarItemClick(Gt.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1),
                n.progressiveInfoButtonClick());
            }, [n]);
          (0, r.useEffect)(() => {
            0 === te.length &&
              Ie.scrollPosition.start({ scrollPosition: 0, reset: !0, immediate: !0 });
          }, [Ie, te]);
          const We = (0, r.useCallback)(() => {
              (n.onToolbarItemClick(Gt.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1), n.onClose());
            }, [n]),
            Ue = (0, r.useCallback)(() => {
              !C && n.onSceneOverChange(!1);
            }, [n, C]),
            Ve = (0, r.useCallback)(() => {
              !C && n.onSceneOverChange(!0);
            }, [n, C]);
          return o().createElement(
            "div",
            { className: f()($s, Y ? Js : Zs, V && Gs), onMouseEnter: Ve, onMouseLeave: Ue },
            o().createElement(
              "div",
              { className: qs },
              V
                ? o().createElement(D_, {
                    onCarouselCollapse: De,
                    startScrollItemId: H,
                    onUpdateItems: Te,
                    tabId: null == (e = a.computes.getSelectedTab()) ? void 0 : e.id,
                  })
                : o().createElement(
                    o().Fragment,
                    null,
                    !J &&
                      o().createElement(Ds, {
                        moveSpace: n.moveSpace,
                        onSceneOverChange: Re,
                        onSceneDraggingChange: n.onSceneDraggingChange,
                        onSceneClick: n.onSceneClick,
                        onHideElements: (e) => {
                          K(e);
                        },
                        onResetMagneticTool: n.onUnselectItem,
                        isHovered: b,
                        isOnboardingViewOpened: C,
                      }),
                    p &&
                      !i &&
                      o().createElement(
                        "div",
                        { className: Ks },
                        o().createElement($t, {
                          caption: ad.progression.info(),
                          type: "info",
                          onClick: ze,
                        }),
                      ),
                    !c &&
                      !i &&
                      o().createElement(
                        "div",
                        { className: Qs },
                        o().createElement($t, {
                          side: "right",
                          type: "close",
                          caption: ad.customization.closeButton(),
                          onClick: We,
                        }),
                      ),
                    c &&
                      o().createElement(
                        "div",
                        { className: Hl },
                        o().createElement($t, {
                          side: "left",
                          type: "back",
                          caption: ad.customization.backButton(),
                          onClick: n.onCloseStyleInfoEsc,
                        }),
                      ),
                    !i &&
                      !J &&
                      o().createElement(
                        "div",
                        { className: f()(ol, Y ? ll : sl), "data-magnetic-tool-support": !0 },
                        o().createElement(J_, { isSceneDraggingChange: Y }),
                      ),
                    Boolean(he.inscriptionState) &&
                      o().createElement("div", { className: Dl }, o().createElement(gs, he)),
                    o().createElement(
                      "div",
                      { className: f()(Xs, i && Ys) },
                      o().createElement(js, me),
                      !J && o().createElement(Wt, { text: _e, className: f()(el, de && tl) }),
                    ),
                    o().createElement(
                      "div",
                      { className: f()(Nl, (i || c) && Il) },
                      o().createElement(
                        "div",
                        { className: ul },
                        o().createElement(
                          "div",
                          { className: nl },
                          o().createElement(
                            "div",
                            { className: gl, onMouseEnter: Ue, onMouseLeave: Ve },
                            o().createElement(
                              Le,
                              { body: _ ? rd.openPanelDisabledButton() : rd.openPanelButton() },
                              o().createElement(
                                "div",
                                { className: zl },
                                o().createElement(
                                  ke,
                                  {
                                    type: we.ghost,
                                    size: Ee,
                                    mixClass: pl,
                                    onClick: () => {
                                      if (v.current) {
                                        const e = v.current.getFirstVisibleItemId();
                                        z(e || -1);
                                      }
                                      (n.onExpandCarousel(!0), j(!0));
                                    },
                                    disabled: _,
                                  },
                                  o().createElement(Wt, {
                                    className: bl,
                                    text: ad.filters.openPanelButton(),
                                  }),
                                ),
                              ),
                            ),
                            o().createElement("div", { className: Cl }),
                            o().createElement(Ca, { buttonSize: Ee }),
                          ),
                          o().createElement(
                            "div",
                            { className: Al, onMouseEnter: Ue, onMouseLeave: Ve },
                            ee &&
                              o().createElement(Uu, {
                                price: ee,
                                onResetHandler: n.onClearBasket,
                                onBackHandler: n.onCancelChanges,
                                onApplyHandler: Me,
                                cartParams: Pe,
                                buttonSize: Ee,
                              }),
                          ),
                        ),
                      ),
                      o().createElement(
                        "div",
                        { className: al, onMouseEnter: Ue, onMouseLeave: Ve },
                        o().createElement("div", { className: rl }),
                        o().createElement(zr, {
                          isEditable: _,
                          tabs: ae,
                          onClick: (e) => {
                            (Fe(R.sounds.cust_tab_switch()), n.selectTab(e));
                          },
                          onHoverTab: n.hoverTab,
                          onEditClose: n.closeEditItem,
                        }),
                        te.length > 0
                          ? o().createElement(l_, {
                              ref: v,
                              scrollApi: Ie,
                              items: te,
                              arrowsList: ne,
                              categories: ue,
                              onClick: Oe,
                              onHoverItem: n.hoverItem,
                              onEditClick: n.onEditItem,
                              onArrowClick: n.onPressSelectNextItem,
                              isCarouselArrowsHintVisible: O,
                              scrollStartItemId: x,
                              selectedItemId: L,
                              firstExpandedItemId: H,
                              tabId: null == (t = a.computes.getSelectedTab()) ? void 0 : t.id,
                              lastScrollState: W,
                              isEditable: _,
                              onUpdateItems: Te,
                            })
                          : o().createElement(
                              f_,
                              {
                                warningHeader: ad.customization.message.header(),
                                warningDescription: ad.customization.message.description(),
                                buttonType: we.secondary,
                                onClick: n.clearFilter,
                                className: il,
                              },
                              o().createElement(Wt, {
                                text: ad.customization.resetFiltersBtn.label(),
                              }),
                            ),
                      ),
                    ),
                  ),
              o().createElement(
                "div",
                {
                  className: f()(fl, !i && (Y ? vl : hl)),
                  "data-magnetic-tool-support": !0,
                  onMouseEnter: Ue,
                  onMouseLeave: Ve,
                },
                o().createElement(Ls, { tabs: oe, onClick: xe, isMinimised: V || i || J }),
              ),
              !V &&
                o().createElement(ks, {
                  onClick: n.clickDecalsBanner,
                  onMouseEnter: Ue,
                  onMouseLeave: Ve,
                  mixClass: f()(_l, (i || c) && dl, !(i || c) && (Y ? El : ml)),
                }),
              i &&
                o().createElement(
                  "div",
                  { className: f()(Ml, i && xl) },
                  o().createElement(
                    "div",
                    { className: Ol },
                    ee &&
                      o().createElement(Uu, {
                        price: ee,
                        onResetHandler: n.onClearBasket,
                        onBackHandler: n.onCancelChanges,
                        onApplyHandler: Me,
                        onAutoRentChange: n.onAutoRentChange,
                        onAutoRentHintClose: n.onAutoRentHintClose,
                        cartParams: Pe,
                        buttonSize: Ee,
                        className: Rl,
                      }),
                  ),
                ),
              m &&
                !V &&
                !i &&
                !c &&
                o().createElement(
                  "div",
                  { className: Sl, "data-magnetic-tool-support": !0 },
                  o().createElement(Mo, {
                    itemType: D,
                    isSelected: E,
                    onSelectApplyingAllSeasons: n.onApplyToAllSeasonsChange,
                  }),
                ),
              be &&
                o().createElement(
                  "div",
                  {
                    className: f()(Bl, B && yl),
                    "data-magnetic-tool-support": !0,
                    onMouseEnter: Ue,
                    onMouseLeave: Ve,
                  },
                  o().createElement(So, {
                    toolbarItems: le,
                    onItemClick: Be,
                    onCloseAction: n.onClose,
                  }),
                ),
              B &&
                !i &&
                !c &&
                o().createElement(
                  "div",
                  { className: f()(Bl, wl), onMouseEnter: Ue, onMouseLeave: Ve },
                  o().createElement(rr, {
                    numberOfBullets: y,
                    currentNumber: k,
                    selectedNumber: w,
                    isBulletsBeforeCurrentDisabled: S,
                    onChange: He,
                    switcherType: 2 === y ? qt.text : qt.digital,
                    size: ar.small,
                    styleID: 594,
                  }),
                ),
              G &&
                o().createElement(Ce, {
                  id: R.views.lobby.customization.CustomizationBinSubview("resId"),
                  mixClass: f()(kl, i && Tl),
                }),
              J &&
                o().createElement(Ce, {
                  id: R.views.lobby.customization.CustomizationStyleInfoView("resId"),
                  mixClass: f()(Ll, c && Pl),
                }),
              h && !G && !J && o().createElement(ts, { mixClass: cl }),
              ve &&
                o().createElement(
                  "div",
                  { className: Fl },
                  o().createElement(Cs, Q_({}, ie, { selectedTab: D })),
                ),
            ),
          );
        });
        const od = (e) => {
            console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
          },
          sd = "INPUT_KEY_STATE";
        var ld;
        !(function (e) {
          ((e.Idle = "IDLE"), (e.Pressed = "PRESSED"), (e.Released = "RELEASED"));
        })(ld || (ld = {}));
        function id(e) {
          localStorage.setItem(sd, JSON.stringify(e));
        }
        function cd(e = fe.n.NONE, t = od, u = !1, n, a = 300) {
          const o = (0, r.useRef)(0);
          (0, r.useEffect)(() => {
            if (e !== fe.n.NONE)
              return (
                window.addEventListener("keydown", r, { capture: u }),
                window.addEventListener("keyup", s, { capture: u }),
                () => {
                  (window.removeEventListener("keydown", r, { capture: u }),
                    window.removeEventListener("keyup", s, { capture: u }));
                }
              );
            function r(n) {
              if (n.keyCode !== e) return;
              if (n.repeat) return;
              if (d.O.view.isEventHandled()) return;
              d.O.view.setEventHandled();
              (
                (function () {
                  const e = localStorage.getItem(sd);
                  return e ? JSON.parse(e) : null;
                })() || { state: ld.Idle, pressTime: 0 }
              ).state === ld.Released
                ? (t(n), u && n.stopPropagation(), id({ state: ld.Idle, pressTime: 0 }))
                : (id({ state: ld.Pressed, pressTime: performance.now() }),
                  (o.current = performance.now()));
            }
            function s(t) {
              if ((localStorage.setItem(ud, "0"), t.keyCode !== e)) return;
              const u = performance.now(),
                r = u - (o.current || u);
              o.current = 0;
              (n && n(r, r >= a, t), id({ state: ld.Released, pressTime: 0 }));
            }
          }, [t, e, u, n, a]);
        }
        function _d() {
          return (
            (_d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            _d.apply(this, arguments)
          );
        }
        const dd = (0, r.memo)(({ Template: e }) => {
          const t = oe("model", re.None),
            u = t.onCloseClicked,
            n = t.placeHolders,
            a = t.background,
            s = t.dimmerAlpha,
            l = t.displayFlags;
          (0, r.useEffect)(() => {
            const e = document.getElementById("root");
            e && e.setAttribute("id", "stubDialogTemplate");
          }, []);
          const i = l.map(({ value: e }) => e),
            c = (0, r.useRef)(n.map(({ value: e }) => e.resourceID)),
            _ = (0, r.useState)(0 !== c.current.length),
            d = _[0],
            m = _[1],
            E = (0, r.useCallback)(
              (e = "default") => {
                u({ reason: e });
              },
              [u],
            ),
            p = (0, r.useCallback)(() => {
              E("escape");
            }, [E]);
          cd(fe.n.ESCAPE, p, !1, void 0, 300);
          const b = (0, r.useCallback)((e) => {
              const t = c.current,
                u = t.indexOf(e);
              u > -1 && (t.splice(u, 1), 0 === t.length && m(!1));
            }, []),
            g = (0, r.useMemo)(() => {
              const e = { backgroundColor: `rgba(19, 18, 16, ${s})` };
              return (a && (e.backgroundImage = `url(${a})`), e);
            }, [a, s]),
            A = (0, r.useMemo)(
              () =>
                n.reduce(
                  (e, { value: t }) => (
                    (e[t.placeHolder] = o().createElement(Ce, {
                      key: t.placeHolder,
                      id: t.resourceID,
                      mixClass: Ze,
                      onLoadCallback: b,
                    })),
                    e
                  ),
                  {},
                ),
              [b, n],
            ),
            C = f()(Ye, d && Ke);
          return o().createElement(
            M,
            null,
            o().createElement(
              "div",
              { className: C, style: g },
              o().createElement(
                e,
                _d(
                  {
                    onClose: E,
                    buttons: o().createElement(Xe, null),
                    displayFlags: i,
                    isShown: !d,
                  },
                  A,
                ),
              ),
            ),
          );
        });
        let md;
        !(function (e) {
          ((e.responsiveHeader = "responsiveHeader"),
            (e.responsiveClosePosition = "responsiveClosePosition"),
            (e.disableResponsiveContentPosition = "disableResponsiveContentPosition"));
        })(md || (md = {}));
        function Ed(e, t, u) {
          const n = (0, r.useContext)(k);
          let a = Object.entries(n).filter(([e, t]) => !0 === t && e in F);
          return (
            u && (a = a.filter((e) => u.includes(e[0]))),
            e.reduce((e, u) => {
              const n = a.map((e) =>
                f()(t[((e, t) => e + "__" + t)(u, e[0])], t[((e, t) => e + P(t))(u, e[0])]),
              );
              return ((e[u] = f()(t[u], ...n)), e);
            }, {})
          );
        }
        const pd = {
            base: "DefaultDialogTemplate_base_40",
            topRight: "DefaultDialogTemplate_topRight_13",
            center: "DefaultDialogTemplate_center_3b",
            center__shown: "DefaultDialogTemplate_center__shown_8f",
            windowIn: "DefaultDialogTemplate_windowIn_24",
            center__withIcon: "DefaultDialogTemplate_center__withIcon_13",
            base__extraSmallHeight: "DefaultDialogTemplate_base__extraSmallHeight_bb",
            center__responsive: "DefaultDialogTemplate_center__responsive_59",
            base__smallHeight: "DefaultDialogTemplate_base__smallHeight_1e",
            icon: "DefaultDialogTemplate_icon_28",
            icon__responsive: "DefaultDialogTemplate_icon__responsive_ab",
            title: "DefaultDialogTemplate_title_9b",
            title__responsive: "DefaultDialogTemplate_title__responsive_7b",
            content: "DefaultDialogTemplate_content_06",
            footer: "DefaultDialogTemplate_footer_65",
            buttons: "DefaultDialogTemplate_buttons_09",
            divider: "DefaultDialogTemplate_divider_43",
            divider__noContent: "DefaultDialogTemplate_divider__noContent_3a",
            divider__noFooter: "DefaultDialogTemplate_divider__noFooter_9c",
            closeBtn: "DefaultDialogTemplate_closeBtn_65",
            closeBtn__responsive: "DefaultDialogTemplate_closeBtn__responsive_b6",
          },
          bd = (0, r.memo)(
            ({
              isShown: e = !0,
              classMix: t,
              onClose: u,
              icon: n,
              topRight: a,
              title: s,
              content: l,
              buttons: i,
              footer: c,
              displayFlags: _,
              classNames: d,
            }) => {
              const m = ((e, t) =>
                  Object.keys(t).reduce((t, u) => ((t[u] = e.includes(u)), t), {}))(_, md),
                E = m.responsiveHeader,
                p = m.responsiveClosePosition,
                b = m.disableResponsiveContentPosition,
                g = Ed(["base"], pd),
                A = (0, r.useCallback)(() => {
                  u && u();
                }, [u]),
                C = f()(g.base, t),
                h = f()(
                  pd.center,
                  n && pd.center__withIcon,
                  e && pd.center__shown,
                  !b && pd.center__responsive,
                  null == d ? void 0 : d.center,
                ),
                v = f()(pd.icon, E && pd.icon__responsive),
                F = f()(pd.title, E && pd.title__responsive),
                D = f()(pd.closeBtn, p && pd.closeBtn__responsive),
                B = f()(
                  pd.divider,
                  !l && pd.divider__noContent,
                  !c && pd.divider__noFooter,
                  null == d ? void 0 : d.divider,
                );
              return o().createElement(
                "div",
                { className: C },
                o().createElement(
                  "div",
                  { className: pd.topRight },
                  a,
                  o().createElement(
                    "div",
                    { className: D },
                    o().createElement($t, {
                      caption: R.strings.menu.viewHeader.closeBtn.label(),
                      type: "close",
                      side: "right",
                      onClick: A,
                    }),
                  ),
                ),
                o().createElement(
                  "div",
                  { className: h },
                  n && o().createElement("div", { className: v }, n),
                  s && o().createElement("div", { className: F }, s),
                  l && o().createElement("div", { className: pd.content }, l),
                  o().createElement("div", { className: B }),
                  c && o().createElement("div", { className: pd.footer }, c),
                  i && o().createElement("div", { className: pd.buttons }, i),
                ),
              );
            },
          ),
          gd = (0, i.Pi)(() => {
            const e = A();
            (e.controls, e.model);
            return o().createElement(dd, { Template: bd });
          });
        engine.whenReady.then(() => {
          l().render(o().createElement(gd, null), document.getElementById("root"));
        });
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
    (__webpack_require__.O = (e, t, u, n) => {
      if (!t) {
        var a = 1 / 0;
        for (l = 0; l < deferred.length; l++) {
          for (var [t, u, n] = deferred[l], r = !0, o = 0; o < t.length; o++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((r = !1), n < a && (a = n));
          if (r) {
            deferred.splice(l--, 1);
            var s = u();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > n; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [t, u, n];
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
    (__webpack_require__.j = 736),
    (() => {
      var e = { 736: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var n,
            a,
            [r, o, s] = u,
            l = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (s) var i = s(__webpack_require__);
          }
          for (t && t(u); l < r.length; l++)
            ((a = r[l]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(i);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [858], () => __webpack_require__(2774));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
