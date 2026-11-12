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
        var a = u(2472),
          n = u(1176);
        const r = (0, a.E)("clientResized"),
          o = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, n.R)(!1);
          }
          function u() {
            e.enabled && (0, n.R)(!0);
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
              : (0, n.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let n = !0;
                  const r = `mouse${t}`,
                    s = o[t]((e) => u([e, "outside"]));
                  function i(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    a(),
                    () => {
                      n &&
                        (s(), window.removeEventListener(r, i), (e.listeners -= 1), a(), (n = !1));
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
      5959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => a,
            getMouseGlobalPosition: () => r,
            getSize: () => n,
            graphicsQuality: () => o,
          }));
        var a = u(527);
        function n(e = "px") {
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
        u.d(t, { O: () => n });
        var a = u(5959);
        const n = { view: u(7641), client: a };
      },
      3722: (e, t, u) => {
        "use strict";
        function a(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function n(e, t, u) {
          return `url(${a(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => n, getTextureUrl: () => a }));
      },
      6112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => n });
        var a = u(2472);
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
      7641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => a,
            displayStatus: () => n.W,
            displayStatusIs: () => S,
            events: () => r.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => D,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => B,
            getScale: () => b,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => f,
            isEventHandled: () => F,
            isFocused: () => h,
            pxToRem: () => p,
            remToPx: () => A,
            resize: () => m,
            sendEvent: () => o.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => v,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => _,
            whenTutorialReady: () => w,
          }));
        var a = u(3722),
          n = u(6112),
          r = u(6538),
          o = u(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, u, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, a);
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
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function b() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function A(e) {
          return viewEnv.remToPx(e);
        }
        function C(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function h() {
          return viewEnv.isFocused();
        }
        function f() {
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
        const S = Object.keys(n.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === n.W[t]), e),
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
          w = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => l });
        const a = ["args"];
        const n = 2,
          r = 16,
          o = 32,
          s = 64,
          i = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                  return n;
                })(t, a);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, o, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, t]) => {
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
            var n;
          },
          l = {
            close(e) {
              i("popover" === e ? n : o);
            },
            minimize() {
              i(s);
            },
            move(e) {
              i(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      5521: (e, t, u) => {
        "use strict";
        let a, n;
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
          })(n || (n = {})));
      },
      1358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => r });
        var a = u(3138);
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
          addCallback(e, t, u = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = a.O.view.addModelObserver(e, u, n);
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
              const a = this._callbacks[u];
              void 0 !== a && a(e, t);
            });
          }
        }
        n.__instance = void 0;
        const r = n;
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
          B3: () => l,
          Z5: () => o,
          B0: () => i,
          c9: () => h,
          wU: () => D,
          ry: () => A,
          Eu: () => C,
          SW: () => v,
          P3: () => F,
        });
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
        const n = a;
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
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = u(5521),
          E = u(3138);
        const g = ["args"];
        function b(e, t, u, a, n, r, o) {
          try {
            var s = e[r](o),
              i = s.value;
          } catch (e) {
            return void u(e);
          }
          s.done ? t(i) : Promise.resolve(i).then(a, n);
        }
        const p = (e) => ({
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
                  return new Promise(function (a, n) {
                    var r = e.apply(t, u);
                    function o(e) {
                      b(r, a, n, o, s, "next", e);
                    }
                    function s(e) {
                      b(r, a, n, o, s, "throw", e);
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
          h = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const n = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                  return n;
                })(t, g);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, r, {
                      arguments:
                        ((a = n),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var a;
          },
          f = () => h(i.CLOSE),
          v = () => h(i.POP_OVER, { on: !1 }),
          F = (e, t, u, a, n = R.invalid("resId"), r) => {
            const o = E.O.view.getViewGlobalPosition(),
              s = u.getBoundingClientRect(),
              l = s.x,
              c = s.y,
              _ = s.width,
              d = s.height,
              m = {
                x: E.O.view.pxToRem(l) + o.x,
                y: E.O.view.pxToRem(c) + o.y,
                width: E.O.view.pxToRem(_),
                height: E.O.view.pxToRem(d),
              };
            h(i.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: a || R.invalid("resId"),
              targetID: n,
              direction: t,
              bbox: p(m),
              on: !0,
              args: r,
            });
          },
          D = () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
          B = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var S = u(7572);
        const y = n.instance,
          w = {
            DataTracker: r.Z,
            ViewModel: S.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => h(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: f,
            sendClosePopOverEvent: v,
            sendShowContextMenuEvent: (e, t, u = 0) => {
              h(i.CONTEXT_MENU, {
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
              B(e, f);
            },
            handleViewEvent: h,
            onBindingsReady: A,
            onLayoutReady: C,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: D,
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const a in t)
                if (Object.prototype.hasOwnProperty.call(t, a)) {
                  const n = Object.prototype.toString.call(t[a]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = t[a];
                    u[a] = [];
                    for (let t = 0; t < n.length; t++) u[a].push({ value: e(n[t].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[a] = e(t[a]))
                      : (u[a] = t[a]);
                }
              return u;
            },
            ClickOutsideManager: y,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = w;
      },
      4429: (e, t, u) => {
        "use strict";
        var a = {};
        (u.r(a),
          u.d(a, {
            Area: () => $i,
            Bar: () => Gi,
            DefaultScroll: () => ji,
            Direction: () => te,
            defaultSettings: () => ue,
            useHorizontalScrollApi: () => ne,
          }));
        var n = {};
        (u.r(n),
          u.d(n, {
            Area: () => cl,
            Bar: () => sl,
            Default: () => ll,
            useVerticalScrollApi: () => Xi,
          }));
        var r = u(6179),
          o = u.n(r);
        const s = (e, t, u) =>
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
        var i = u(3138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function _(e, t, u) {
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
            n = (function (e, t) {
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
            r = Math.min(a, n);
          return {
            extraLarge: r === u.extraLarge.weight,
            large: r === u.large.weight,
            medium: r === u.medium.weight,
            small: r === u.small.weight,
            extraSmall: r === u.extraSmall.weight,
            extraLargeWidth: a === u.extraLarge.weight,
            largeWidth: a === u.large.weight,
            mediumWidth: a === u.medium.weight,
            smallWidth: a === u.small.weight,
            extraSmallWidth: a === u.extraSmall.weight,
            extraLargeHeight: n === u.extraLarge.weight,
            largeHeight: n === u.large.weight,
            mediumHeight: n === u.medium.weight,
            smallHeight: n === u.small.weight,
            extraSmallHeight: n === u.extraSmall.weight,
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
          E = d.height,
          g = Object.assign({ width: m, height: E }, _(m, E, l)),
          b = (0, r.createContext)(g),
          p = ["children"];
        const A = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, p);
          const a = (0, r.useContext)(b),
            n = a.extraLarge,
            o = a.large,
            i = a.medium,
            l = a.small,
            c = a.extraSmall,
            _ = a.extraLargeWidth,
            d = a.largeWidth,
            m = a.mediumWidth,
            E = a.smallWidth,
            g = a.extraSmallWidth,
            A = a.extraLargeHeight,
            C = a.largeHeight,
            h = a.mediumHeight,
            f = a.smallHeight,
            v = a.extraSmallHeight,
            F = { extraLarge: A, large: C, medium: h, small: f, extraSmall: v };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && n) return t;
            if (u.large && o) return t;
            if (u.medium && i) return t;
            if (u.small && l) return t;
            if (u.extraSmall && c) return t;
          } else {
            if (u.extraLargeWidth && _) return s(t, u, F);
            if (u.largeWidth && d) return s(t, u, F);
            if (u.mediumWidth && m) return s(t, u, F);
            if (u.smallWidth && E) return s(t, u, F);
            if (u.extraSmallWidth && g) return s(t, u, F);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && A) return t;
              if (u.largeHeight && C) return t;
              if (u.mediumHeight && h) return t;
              if (u.smallHeight && f) return t;
              if (u.extraSmallHeight && v) return t;
            }
          }
          return null;
        };
        A.defaultProps = {
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
        (0, r.memo)(A);
        const C = (e) => {
            const t = (0, r.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          h = (0, r.memo)(({ children: e }) => {
            const t = (0, r.useContext)(b),
              u = (0, r.useState)(t),
              a = u[0],
              n = u[1],
              s = (0, r.useCallback)((e, t) => {
                const u = i.O.view.pxToRem(e),
                  a = i.O.view.pxToRem(t);
                n(Object.assign({ width: u, height: a }, _(u, a, l)));
              }, []);
            (C(() => {
              engine.on("clientResized", s);
            }),
              (0, r.useEffect)(() => () => engine.off("clientResized", s), [s]));
            const c = (0, r.useMemo)(() => Object.assign({}, a), [a]);
            return o().createElement(b.Provider, { value: c }, e);
          });
        var f = u(6483),
          v = u.n(f),
          F = u(926),
          D = u.n(F);
        let B, S, y;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(B || (B = {})),
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
          })(y || (y = {})));
        const w = () => {
            const e = (0, r.useContext)(b),
              t = e.width,
              u = e.height,
              a = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return B.ExtraLarge;
                  case e.large:
                    return B.Large;
                  case e.medium:
                    return B.Medium;
                  case e.small:
                    return B.Small;
                  case e.extraSmall:
                    return B.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), B.ExtraSmall);
                }
              })(e),
              n = ((e) => {
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
              o = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return y.ExtraLarge;
                  case e.largeHeight:
                    return y.Large;
                  case e.mediumHeight:
                    return y.Medium;
                  case e.smallHeight:
                    return y.Small;
                  case e.extraSmallHeight:
                    return y.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), y.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: a,
              mediaWidth: n,
              mediaHeight: o,
              remScreenWidth: t,
              remScreenHeight: u,
            };
          },
          k = ["children", "className"];
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        const N = {
            [S.ExtraSmall]: "",
            [S.Small]: D().SMALL_WIDTH,
            [S.Medium]: `${D().SMALL_WIDTH} ${D().MEDIUM_WIDTH}`,
            [S.Large]: `${D().SMALL_WIDTH} ${D().MEDIUM_WIDTH} ${D().LARGE_WIDTH}`,
            [S.ExtraLarge]: `${D().SMALL_WIDTH} ${D().MEDIUM_WIDTH} ${D().LARGE_WIDTH} ${D().EXTRA_LARGE_WIDTH}`,
          },
          I = {
            [y.ExtraSmall]: "",
            [y.Small]: D().SMALL_HEIGHT,
            [y.Medium]: `${D().SMALL_HEIGHT} ${D().MEDIUM_HEIGHT}`,
            [y.Large]: `${D().SMALL_HEIGHT} ${D().MEDIUM_HEIGHT} ${D().LARGE_HEIGHT}`,
            [y.ExtraLarge]: `${D().SMALL_HEIGHT} ${D().MEDIUM_HEIGHT} ${D().LARGE_HEIGHT} ${D().EXTRA_LARGE_HEIGHT}`,
          },
          M = {
            [B.ExtraSmall]: "",
            [B.Small]: D().SMALL,
            [B.Medium]: `${D().SMALL} ${D().MEDIUM}`,
            [B.Large]: `${D().SMALL} ${D().MEDIUM} ${D().LARGE}`,
            [B.ExtraLarge]: `${D().SMALL} ${D().MEDIUM} ${D().LARGE} ${D().EXTRA_LARGE}`,
          },
          x = (e) => {
            let t = e.children,
              u = e.className,
              a = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, k);
            const n = w(),
              r = n.mediaWidth,
              s = n.mediaHeight,
              i = n.mediaSize;
            return o().createElement("div", T({ className: v()(u, N[r], I[s], M[i]) }, a), t);
          },
          O = ["children"];
        const L = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, O);
          return o().createElement(h, null, o().createElement(x, u, t));
        };
        var P = u(493),
          H = u.n(P);
        function W(e) {
          engine.call("PlaySound", e);
        }
        const z = {
            playHighlight() {
              W("highlight");
            },
            playClick() {
              W("play");
            },
            playYes() {
              W("yes1");
            },
          },
          U = {
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
        let G, V;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(G || (G = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(V || (V = {})));
        const j = ({
          children: e,
          size: t,
          isFocused: u,
          type: a,
          disabled: n,
          mixClass: s,
          soundHover: i,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: E,
          onClick: g,
        }) => {
          const b = (0, r.useRef)(null),
            p = (0, r.useState)(u),
            A = p[0],
            C = p[1],
            h = (0, r.useState)(!1),
            f = h[0],
            F = h[1],
            D = (0, r.useState)(!1),
            B = D[0],
            S = D[1],
            y = (0, r.useCallback)(() => {
              n || (b.current && (b.current.focus(), C(!0)));
            }, [n]),
            w = (0, r.useCallback)(
              (e) => {
                A && null !== b.current && !b.current.contains(e.target) && C(!1);
              },
              [A],
            ),
            k = (0, r.useCallback)(
              (e) => {
                n || (g && g(e));
              },
              [n, g],
            ),
            T = (0, r.useCallback)(
              (e) => {
                n || (null !== i && W(i), c && c(e), S(!0));
              },
              [n, i, c],
            ),
            N = (0, r.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            I = (0, r.useCallback)(
              (e) => {
                n || (m && m(e), F(!1));
              },
              [n, m],
            ),
            M = (0, r.useCallback)(
              (e) => {
                n || (null !== l && W(l), d && d(e), u && y(), F(!0));
              },
              [n, l, d, y, u],
            ),
            x = (0, r.useCallback)(
              (e) => {
                n || (E && E(e), F(!1));
              },
              [n, E],
            ),
            O = v()(
              U.base,
              U[`base__${a}`],
              {
                [U.base__disabled]: n,
                [U[`base__${t}`]]: t,
                [U.base__focus]: A,
                [U.base__highlightActive]: f,
                [U.base__firstHover]: B,
              },
              s,
            ),
            L = v()(U.state, U.state__default);
          return (
            (0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", w),
                () => {
                  document.removeEventListener("mousedown", w);
                }
              ),
              [w],
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
              a !== G.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: U.back }),
                  o().createElement("span", { className: U.texture }),
                ),
              o().createElement(
                "span",
                { className: L },
                o().createElement("span", { className: U.stateDisabled }),
                o().createElement("span", { className: U.stateHighlightHover }),
                o().createElement("span", { className: U.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: U.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        j.defaultProps = {
          type: G.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const $ = (0, r.memo)(j),
          X = (e, t, u) => (u < e ? e : u > t ? t : u),
          q = (e) => {
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
        function Y(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return K(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return K(e, t);
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
        function K(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, a = new Array(t); u < t; u++) a[u] = e[u];
          return a;
        }
        const Z = [];
        function J(e) {
          const t = (0, r.useRef)(e);
          return (
            (0, r.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, r.useCallback)((...e) => (0, t.current)(...e), Z)
          );
        }
        function Q(e, t, u) {
          const a = (0, r.useMemo)(
            () =>
              (function (e, t, u, a) {
                let n,
                  r = !1,
                  o = 0;
                function s() {
                  n && clearTimeout(n);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - o;
                  function _() {
                    ((o = Date.now()), u.apply(l, i));
                  }
                  r ||
                    (a && !n && _(),
                    s(),
                    void 0 === a && c > e
                      ? _()
                      : !0 !== t &&
                        (n = setTimeout(
                          a
                            ? function () {
                                n = void 0;
                              }
                            : _,
                          void 0 === a ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((a = u), (u = t), (t = void 0)),
                  (i.cancel = function () {
                    (s(), (r = !0));
                  }),
                  i
                );
              })(u, e),
            t,
          );
          return ((0, r.useEffect)(() => a.cancel, [a]), a);
        }
        var ee = u(7030);
        let te;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(te || (te = {}));
        const ue = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          ae = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: u,
            getDirection: a,
            getWrapperSize: n,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const s = (e, u) => {
              const a = t(e),
                n = a[0],
                r = a[1];
              return X(n, r, u);
            };
            return (l = {}) => {
              const c = l.settings,
                _ = void 0 === c ? ue : c,
                d = (0, r.useRef)(null),
                m = (0, r.useRef)(null),
                E = (() => {
                  const e = (0, r.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    u = (e, u) => {
                      t(e).set(u, u);
                    },
                    a = (e, u) => {
                      t(e).delete(u);
                    },
                    n = (e, ...u) => {
                      for (var a, n = Y(t(e).values()); !(a = n()).done;) (0, a.value)(...u);
                    };
                  return (0, r.useMemo)(() => ({ on: u, off: a, trigger: n }), []);
                })(),
                g = Q(
                  () => {
                    i.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                b = (0, ee.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = d.current;
                    t && (u(t, e), E.trigger("change", e), o && g());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                p = b[0],
                A = b[1],
                C = (0, r.useCallback)(
                  (e, t, u) => {
                    var a;
                    const n = p.scrollPosition.get(),
                      r = (null != (a = p.scrollPosition.goal) ? a : 0) - n;
                    return s(e, t * u + r + n);
                  },
                  [p.scrollPosition],
                ),
                h = (0, r.useCallback)(
                  (e, { immediate: t = !1, reset: u = !0 } = {}) => {
                    const a = d.current;
                    a &&
                      A.start({
                        scrollPosition: s(a, e),
                        immediate: t,
                        reset: u,
                        config: _.animationConfig,
                        from: { scrollPosition: s(a, p.scrollPosition.get()) },
                      });
                  },
                  [A, _.animationConfig, p.scrollPosition],
                ),
                f = (0, r.useCallback)(
                  (e) => {
                    const t = d.current,
                      u = m.current;
                    if (!t || !u) return;
                    const a = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return n(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(u, _.step),
                      r = C(t, e, a);
                    h(r);
                  },
                  [h, C, _.step],
                ),
                v = (0, r.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && f(a(e)),
                      d.current && E.trigger("mouseWheel", e, p.scrollPosition, t(d.current)));
                  },
                  [p.scrollPosition, f, E],
                ),
                F = ((e, t = []) => {
                  const u = (0, r.useRef)(),
                    a = (0, r.useCallback)((...t) => {
                      (u.current && u.current(), (u.current = e(...t)));
                    }, t);
                  return (
                    (0, r.useEffect)(
                      () => () => {
                        u.current && u.current();
                      },
                      [a],
                    ),
                    a
                  );
                })(
                  () =>
                    q(() => {
                      const e = d.current;
                      e &&
                        (h(s(e, p.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [h, p.scrollPosition.goal],
                ),
                D = J(() => {
                  const e = d.current;
                  if (!e) return;
                  const t = s(e, p.scrollPosition.goal);
                  (t !== p.scrollPosition.goal && h(t, { immediate: !0 }),
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
                  getWrapperSize: () => (m.current ? n(m.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? t(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: _.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: v,
                  applyScroll: h,
                  applyStepTo: f,
                  contentRef: d,
                  wrapperRef: m,
                  scrollPosition: A,
                  animationScroll: p,
                  recalculateContent: D,
                  handleIsThumbDragging: B,
                  events: { on: E.on, off: E.off },
                }),
                [p.scrollPosition, h, f, B, E.off, E.on, D, v, A, _.step.clampedArrowStepTimeout],
              );
            };
          },
          ne = ae({
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
            getDirection: (e) => (e.deltaY > 1 ? te.Next : te.Prev),
            triggerMouseMoveOnUpdate: !0,
          });
        var re = u(9887),
          oe = u.n(re);
        const se = ["xl", "lg", "md", "sm", "xs"],
          ie = (e) => e.includes("_") && ((e) => se.includes(e))(e.split("_").at(-1)),
          le = [B.ExtraLarge, B.Large, B.Medium, B.Small, B.ExtraSmall],
          ce = (e, t) =>
            Object.keys(e).reduce((u, a) => {
              if (a in u) return u;
              if (ie(a)) {
                const n = a.split("_").slice(0, -1).join("_");
                if (n in u) return u;
                const r = le.indexOf(t),
                  o = (-1 !== r ? se.slice(r) : [])
                    .map((e) => n + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  s = o ? e[o] : void 0;
                return ((u[n] = void 0 !== s ? s : e[n]), u);
              }
              const n = e[a];
              return (
                void 0 === n ||
                  ((e, t) => se.some((u) => void 0 !== t[`${e}_${u}`]))(a, e) ||
                  (u[a] = n),
                u
              );
            }, {}),
          _e = (e, t = ce) => {
            const u = (
              (e, t = ce) =>
              (u) => {
                const a = w().mediaSize,
                  n = (0, r.useMemo)(() => t(u, a), [u, a]);
                return o().createElement(e, n);
              }
            )(e, t);
            return o().memo((t) =>
              Object.keys(t).some((e) => ie(e) && void 0 !== t[e])
                ? o().createElement(u, t)
                : o().createElement(e, t),
            );
          },
          de = {
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
          me = [
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
        function Ee() {
          return (
            (Ee =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Ee.apply(this, arguments)
          );
        }
        Object.keys(oe());
        const ge = {
            XL: { mt: de.mt__XL, mr: de.mr__XL, mb: de.mb__XL, ml: de.ml__XL },
            LG: { mt: de.mt__LG, mr: de.mr__LG, mb: de.mb__LG, ml: de.ml__LG },
            MDp: { mt: de.mt__MDp, mr: de.mr__MDp, mb: de.mb__MDp, ml: de.ml__MDp },
            MD: { mt: de.mt__MD, mr: de.mr__MD, mb: de.mb__MD, ml: de.ml__MD },
            SMp: { mt: de.mt__SMp, mr: de.mr__SMp, mb: de.mb__SMp, ml: de.ml__SMp },
            SM: { mt: de.mt__SM, mr: de.mr__SM, mb: de.mb__SM, ml: de.ml__SM },
            XS: { mt: de.mt__XS, mr: de.mr__XS, mb: de.mb__XS, ml: de.ml__XS },
          },
          be = (Object.keys(ge), ["mt", "mr", "mb", "ml"]),
          pe = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Ae = _e((e) => {
            let t = e.className,
              u = e.width,
              a = e.height,
              n = e.m,
              s = e.mt,
              i = void 0 === s ? n : s,
              l = e.mr,
              c = void 0 === l ? n : l,
              _ = e.mb,
              d = void 0 === _ ? n : _,
              m = e.ml,
              E = void 0 === m ? n : m,
              g = e.column,
              b = e.row,
              p = e.flexDirection,
              A = void 0 === p ? (g ? "column" : b && "row") || void 0 : p,
              C = e.flexStart,
              h = e.center,
              f = e.flexEnd,
              F = e.spaceBetween,
              D = e.spaceAround,
              B = e.justifyContent,
              S =
                void 0 === B
                  ? (C ? "flex-start" : h && "center") ||
                    (f && "flex-end") ||
                    (F && "space-between") ||
                    (D && "space-around") ||
                    void 0
                  : B,
              y = e.alignItems,
              w =
                void 0 === y
                  ? (C ? "flex-start" : h && "center") || (f && "flex-end") || void 0
                  : y,
              k = e.alignSelf,
              T = e.wrap,
              N = e.flexWrap,
              I = void 0 === N ? (T ? "wrap" : void 0) : N,
              M = e.grow,
              x = e.shrink,
              O = e.flex,
              L = void 0 === O ? (M || x ? `${M ? 1 : 0} ${x ? 1 : 0} auto` : void 0) : O,
              R = e.style,
              P = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, me);
            const W = (0, r.useMemo)(() => {
                const e = { mt: i, mr: c, mb: d, ml: E },
                  t = ((e) =>
                    be.reduce((t, u) => {
                      const a = e[u];
                      return a && "number" != typeof a ? t.concat(ge[!0 === a ? "MD" : a][u]) : t;
                    }, []))(e),
                  n = ((e) =>
                    be.reduce((t, u) => {
                      const a = e[u];
                      return ("number" == typeof a && (t[pe[u]] = a + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, R, n, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    flex: L,
                    alignSelf: k,
                    display: A || w ? "flex" : void 0,
                    flexDirection: A,
                    flexWrap: I,
                    justifyContent: S,
                    alignItems: w,
                  }),
                  computedClassNames: t,
                };
              }, [u, a, i, c, d, E, R, L, k, A, I, S, w]),
              z = W.computedStyle,
              U = W.computedClassNames;
            return o().createElement(
              "div",
              Ee({ className: v()(de.base, ...U, t), style: z }, H),
              P,
            );
          });
        let Ce;
        function he(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(Ce || (Ce = {}));
        const fe = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          ve = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          Fe = (e, t, u = Ce.left) => e.split(t).reduce(u === Ce.left ? fe : ve, []),
          De = (() => {
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
          Be = ["zh_cn", "zh_sg", "zh_tw"],
          Se = (e, t = Ce.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Be.includes(u)
              ? De(e)
              : ((e, t = Ce.left) => {
                  let u = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (Fe(n, /( )/, t).forEach((e) => (u = u.concat(Fe(e, a, Ce.left)))), u);
                })(e, t);
          },
          ye = "FormatText_base_d0",
          we = ({ binding: e, text: t = "", classMix: u, alignment: a = Ce.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  r.Fragment,
                  null,
                  t.split("\n").map((t, n) =>
                    o().createElement(
                      "div",
                      { className: v()(ye, u), key: `${t}-${n}` },
                      ((e, t, u) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (u && e in u ? u[e] : Se(e, t))))(t, a, e).map((e, t) =>
                        o().createElement(r.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var ke = u(3532),
          Te = u.n(ke);
        const Ne = {
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
          Ie = [
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
        function Me() {
          return (
            (Me =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Me.apply(this, arguments)
          );
        }
        Object.keys(oe());
        const xe = Object.keys(Te()),
          Oe = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Le = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Re = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Pe = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          He =
            (Object.keys(Pe),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Oe,
              "heading-H36": Oe,
              "heading-H28": Le,
              "heading-H24": Le,
              "heading-H24R": Le,
              "heading-H22": Le,
              "heading-H20R": Le,
              "heading-H18": Le,
              "heading-H15": Re,
              "heading-H14": Re,
              "paragraph-P24": Le,
              "paragraph-P18": Le,
              "paragraph-P16": Le,
              "paragraph-P14": Re,
              "paragraph-P12": Re,
              "paragraph-P10": Re,
            }),
          We =
            (Object.keys(He),
            (e) =>
              e
                ? ((e) => xe.includes(e))(e)
                  ? { colorClassName: Ne[e] }
                  : { colorStyle: { color: e } }
                : {}),
          ze = _e((e) => {
            let t = e.text,
              u = e.variant,
              a = e.className,
              n = e.color,
              s = e.m,
              i = e.mt,
              l = void 0 === i ? s : i,
              c = e.mr,
              _ = void 0 === c ? s : c,
              d = e.mb,
              m = void 0 === d ? s : d,
              E = e.ml,
              g = void 0 === E ? s : E,
              b = e.style,
              p = e.format,
              A = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Ie);
            const C = (0, r.useMemo)(() => {
                const e = We(n),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  a = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, b, a), colorClassName: t };
              }, [b, n]),
              h = C.computedStyle,
              f = C.colorClassName;
            return o().createElement(
              Ae,
              Me(
                {
                  className: v()(Ne.base, u && Ne[u], f, a),
                  style: h,
                  mt: !0 === l ? He[u || "paragraph-P16"].mt : l,
                  mr: !0 === _ ? He[u || "paragraph-P16"].mr : _,
                  mb: !0 === m ? He[u || "paragraph-P16"].mb : m,
                  ml: !0 === g ? He[u || "paragraph-P16"].ml : g,
                },
                A,
              ),
              void 0 !== p ? o().createElement(we, Me({}, p, { text: t })) : t,
            );
          }),
          Ue = {
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
          Ge = [
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
        function Ve() {
          return (
            (Ve =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Ve.apply(this, arguments)
          );
        }
        class je extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && W(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && W(this.props.soundClick));
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
              a = e.goto,
              n = e.side,
              r = e.type,
              s = e.classNames,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              _ = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                  return n;
                })(e, Ge)),
              m = v()(Ue.base, Ue[`base__${r}`], Ue[`base__${n}`], null == s ? void 0 : s.base),
              E = v()(Ue.icon, Ue[`icon__${r}`], Ue[`icon__${n}`], null == s ? void 0 : s.icon),
              g = v()(Ue.glow, null == s ? void 0 : s.glow),
              b = v()(Ue.caption, Ue[`caption__${r}`], null == s ? void 0 : s.caption),
              p = v()(Ue.goto, null == s ? void 0 : s.goto);
            return o().createElement(
              "div",
              Ve(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                d,
              ),
              "info" !== r && o().createElement("div", { className: Ue.shine }),
              o().createElement(
                "div",
                { className: E },
                o().createElement("div", { className: g }),
              ),
              o().createElement("div", { className: b }, t),
              a && o().createElement("div", { className: p }, a),
            );
          }
        }
        je.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var $e = u(4179);
        const Xe = [
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
        function qe(e) {
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
        const Ye = (e, t, u = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: $e.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: a,
                },
                u,
              ),
            );
          },
          Ke = (e) => {
            let t = e.children,
              u = e.contentId,
              a = e.args,
              n = e.onMouseEnter,
              o = e.onMouseLeave,
              s = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              _ = e.ignoreMouseClick,
              d = void 0 !== _ && _,
              m = e.decoratorId,
              E = void 0 === m ? 0 : m,
              g = e.isEnabled,
              b = void 0 === g || g,
              p = e.targetId,
              A = void 0 === p ? 0 : p,
              C = e.onShow,
              h = e.onHide,
              f = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Xe);
            const v = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              F = (0, r.useMemo)(
                () =>
                  A ||
                  ((e = 1) => {
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
                  })().resId,
                [A],
              ),
              D = (0, r.useCallback)(() => {
                (v.current.isVisible && v.current.timeoutId) ||
                  (Ye(u, E, { isMouseEvent: !0, on: !0, arguments: qe(a) }, F),
                  C && C(),
                  (v.current.isVisible = !0));
              }, [u, E, a, F, C]),
              B = (0, r.useCallback)(() => {
                if (v.current.isVisible || v.current.timeoutId) {
                  const e = v.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (v.current.timeoutId = 0)),
                    Ye(u, E, { on: !1 }, F),
                    v.current.isVisible && h && h(),
                    (v.current.isVisible = !1));
                }
              }, [u, E, F, h]),
              S = (0, r.useCallback)((e) => {
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
                document.addEventListener("wheel", S, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", S, { capture: !0 }),
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
                            n && n(e),
                            y && y(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (B(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === d && B(), null == i || i(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === d && B(), null == s || s(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    f,
                  ),
                )
              : t;
            var y;
          },
          Ze = ["children", "body", "header", "note", "alert", "args"];
        function Je() {
          return (
            (Je =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Je.apply(this, arguments)
          );
        }
        const Qe = R.views.common.tooltip_window.simple_tooltip_content,
          et = (e) => {
            let t = e.children,
              u = e.body,
              a = e.header,
              n = e.note,
              s = e.alert,
              i = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Ze);
            const c = (0, r.useMemo)(() => {
              const e = Object.assign({}, i, { body: u, header: a, note: n, alert: s });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [s, u, a, n, i]);
            return o().createElement(
              Ke,
              Je(
                {
                  contentId:
                    ((_ = null == i ? void 0 : i.hasHtmlContent),
                    _ ? Qe.SimpleTooltipHtmlContent("resId") : Qe.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var _;
          };
        let tt, ut;
        (!(function (e) {
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
        })(tt || (tt = {})),
          (function (e) {
            ((e[(e.digital = 0)] = "digital"), (e[(e.text = 1)] = "text"));
          })(ut || (ut = {})));
        const at = (e) => {
          const t = (0, r.useRef)();
          return (
            (0, r.useEffect)(() => {
              t.current = e;
            }, [e]),
            t.current
          );
        };
        let nt;
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
        })(nt || (nt = {}));
        const rt = 60,
          ot = 3600,
          st = 86400;
        Date.now();
        const it = () => {},
          lt = (e = 0, t, u = 0, a = it) => {
            const n = (0, r.useState)(e),
              o = n[0],
              s = n[1];
            return (
              (0, r.useEffect)(() => {
                if (e > 0) {
                  s(e);
                  const n = Date.now(),
                    r = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - n) / 1e3);
                        null !== u && t <= u ? (s(u), a && a(), clearInterval(r)) : s(t);
                      },
                      1e3 * (t || (e > 120 ? rt : 1)),
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                s(0);
              }, [e, t, u, a]),
              o
            );
          };
        $e.Sw.instance;
        let ct;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(ct || (ct = {}));
        $e.Sw.instance;
        const _t = at,
          dt = lt,
          mt = (e) => {
            (0, r.useEffect)(e, []);
          };
        function Et() {
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
        const gt = /<link.*?>/g,
          bt = /\.\.\//g,
          pt = /<script.*?>/g,
          At = "default.css",
          Ct = (e) => {
            const t = e.match(bt);
            return t && t.join("");
          },
          ht = () => {
            for (
              var e = 0, t = Array.from(document.head.querySelectorAll('link[rel="stylesheet"]'));
              e < t.length;
              e++
            ) {
              const u = t[e];
              if (!u.href.includes(At)) return u.href;
            }
            return "";
          },
          ft = (e, t) => {
            const u = ht(),
              a = Ct(u);
            let n,
              r = e;
            for (; null !== (n = pt.exec(e));) {
              const e = n[0].match(/<script (defer|defer="defer") src="(.*?)">/);
              if (e) {
                const u = a + e[2].replace(bt, "");
                ((r = r.replace(e[2], u)),
                  (r = r.replace('<div id="root"', `<div data-root-id=${t} id="root"`)));
              }
            }
            return r;
          },
          vt = "SubView_base_df",
          Ft = "subViews.onChanged",
          Dt = (() => {
            const e = [];
            let t = !1;
            const u = () => {
              if (!e.length) return void (t = !1);
              const a = e.shift();
              a && ((t = !0), a().then(() => u()));
            };
            return {
              add: (a) => {
                (e.push(a), t || u());
              },
            };
          })(),
          Bt = (0, r.memo)(({ id: e, fallback: t, onLoadCallback: u, mixClass: a }) => {
            const n = (0, r.useState)(""),
              s = n[0],
              i = n[1],
              l = (0, r.useMemo)(() => ({ __html: ft(s, e) }), [s, e]),
              c = (0, r.useMemo)(() => window.subViews.addChildChangedCallback(e), [e]),
              _ = (0, r.useState)(!1),
              d = _[0],
              m = _[1],
              E = (0, r.useCallback)(
                (e) => {
                  e.includes(c) &&
                    (m(!0), engine.off(Ft, E), window.subViews.removeChildChangedCallback(c));
                },
                [c],
              ),
              g = (0, r.useCallback)((e) => {
                Dt.add(
                  () =>
                    new Promise((t) => {
                      i(e);
                      const u = new MutationObserver(() => {
                          (u.disconnect(), t());
                        }),
                        a = document.getElementById("root");
                      a && u.observe(a, { childList: !0 });
                    }),
                );
              }, []);
            ((0, r.useEffect)(() => {
              if (window.subViews.ids().includes(e)) {
                const t = window.subViews.get(e),
                  u = t.path;
                let a;
                if ((a = u.split("/").pop()))
                  return (
                    (a = a.split(".")[0]),
                    (window.subViews[a] = Object.assign({ id: e }, t)),
                    engine.on(`subView:inject->${a}`, g),
                    (({ path: e, name: t }) => {
                      const u = new XMLHttpRequest();
                      ((u.onreadystatechange = () => {
                        4 === u.readyState &&
                          (200 === u.status
                            ? (0, $e.Eu)().then(() => {
                                (console.info(`Sub view ${t} loaded: ${e}`),
                                  engine.TriggerEvent(`subView:inject->${t}`, u.responseText));
                              })
                            : console.error(`subView: status: ${u.status} - can't get bundle`));
                      }),
                        u.open("GET", e),
                        u.send());
                    })({ name: a, path: u }),
                    () => {
                      (a && window.subViews[a] && delete window.subViews[a],
                        engine.trigger("subView:destroy", { viewName: a, viewId: e }),
                        window.__dataTracker &&
                          window.__dataTracker.clearViewCallbacks &&
                          window.__dataTracker.clearViewCallbacks(e),
                        engine.off(`subView:inject->${a}`, g),
                        console.info(`Sub view ${a} is destroyed: ${u}`));
                    }
                  );
                console.error("subView: can't get View component name");
              } else engine.on(Ft, E);
            }, [E, g, e, d]),
              (0, r.useEffect)(
                () => () => {
                  s &&
                    ((e) => {
                      const t = Ct(ht());
                      let u;
                      for (; null !== (u = gt.exec(e));) {
                        const e = u[0].match(/href="(.*?)"/);
                        if (e) {
                          const u = t + e[1].replace(bt, ""),
                            a = document.head.querySelector(`[href="${u}"]`);
                          a && document.head.removeChild(a);
                        }
                      }
                    })(s);
                },
                [s],
              ));
            const b = v()(vt, a);
            if (s) {
              let t;
              return (
                (t = document.getElementById("root")) && t.setAttribute("id", "bugSubView"),
                ((e) => {
                  let t;
                  const u = ht(),
                    a = Ct(u);
                  for (; null !== (t = gt.exec(e));) {
                    const e = t[0].match(/href="(.*?)"/);
                    if (e && !e[1].includes(At) && a) {
                      const t = a + e[1].replace(bt, ""),
                        u = document.createElement("link");
                      ((u.href = t), (u.rel = "stylesheet"), document.head.appendChild(u));
                    }
                  }
                })(s),
                u && u(e),
                o().createElement("div", { className: b, dangerouslySetInnerHTML: l })
              );
            }
            return t
              ? o().createElement("div", { className: b }, o().createElement(t, null))
              : null;
          });
        var St = u(3403);
        let yt;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(yt || (yt = {}));
        const wt = {
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
        let kt, Tt, Nt;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(kt || (kt = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(Tt || (Tt = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(Nt || (Nt = {})));
        const It = [
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
        function Mt() {
          return (
            (Mt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Mt.apply(this, arguments)
          );
        }
        const xt = (e) => {
          let t = e.id,
            u = e.isChecked,
            a = void 0 !== u && u,
            n = e.isDisabled,
            s = void 0 !== n && n,
            i = e.isAlert,
            l = void 0 !== i && i,
            c = e.size,
            _ = void 0 === c ? kt.medium : c,
            d = e.type,
            m = void 0 === d ? Tt.primary : d,
            E = e.soundHover,
            g = void 0 === E ? "highlight" : E,
            b = e.soundClick,
            p = void 0 === b ? "play" : b,
            A = e.onMouseEnter,
            C = e.onMouseLeave,
            h = e.onMouseUp,
            f = e.onMouseDown,
            F = e.onClick,
            D = e.onChange,
            B = e.onFocus,
            S = e.onBlur,
            y = e.text,
            w = e.contentStyles,
            k = e.children,
            T = e.alignment,
            N = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, It);
          const I = (0, r.useState)(!1),
            M = I[0],
            x = I[1],
            O = (0, r.useState)(!1),
            L = (O[0], O[1]),
            R = (0, r.useCallback)(
              (e) => {
                s || (D && D(), F && F(e));
              },
              [s, D, F],
            ),
            P = (0, r.useCallback)(
              (e) => {
                const t = e.button === yt.LEFT;
                s || (t && x(!0), t && f && f(e), p && W(p));
              },
              [s, f, p],
            ),
            H = (0, r.useCallback)(
              (e) => {
                s || (x(!1), h && h(e));
              },
              [s, h],
            ),
            z = (0, r.useCallback)(
              (e) => {
                s || (A && A(e), g && W(g));
              },
              [s, A, g],
            ),
            U = (0, r.useCallback)(
              (e) => {
                s || (x(!1), C && C(e));
              },
              [s, C],
            ),
            G = (0, r.useCallback)(
              (e) => {
                s || (L(!0), B && B(e));
              },
              [s, B],
            ),
            V = (0, r.useCallback)(
              (e) => {
                s || (L(!1), S && S(e));
              },
              [s, S],
            ),
            j = o().createElement(
              "div",
              { className: wt.label },
              o().createElement(
                "div",
                { className: v()(wt.labelContent, "s-labelContent"), style: w },
                y || k,
              ),
            );
          return o().createElement(
            "div",
            Mt(
              {
                id: t,
                className: v()(wt.base, wt[`base__${_}`], wt[`base__${m}`], {
                  [wt.base__checked]: a,
                  [wt.base__disabled]: s,
                  [wt.base__mouseDown]: M,
                  [wt.base__alert]: l,
                  [wt.base__center]: T === Nt.Center,
                  [wt.base__bottom]: T === Nt.Bottom,
                }),
                onClick: R,
                onMouseEnter: z,
                onMouseLeave: U,
                onMouseDown: P,
                onMouseUp: H,
                onFocus: G,
                onBlur: V,
              },
              N,
            ),
            o().createElement(
              "div",
              { className: wt.input },
              o().createElement("div", { className: wt.alertOverlay }),
              o().createElement("div", { className: wt.inputHoverOverlay }),
              o().createElement("div", { className: wt.highlight }),
            ),
            o().createElement("div", { className: wt.checkmark }),
            ((y || k) && j) || null,
          );
        };
        let Ot, Lt, Rt;
        (!(function (e) {
          ((e.small = "small"),
            (e.big = "big"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(Ot || (Ot = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(Lt || (Lt = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(Rt || (Rt = {})));
        class Pt extends o().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = $e.B3.GOLD;
            else e = $e.B3.INTEGRAL;
            const t = $e.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        Pt.defaultProps = { format: "integral" };
        const Ht = {
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
          Wt = ({
            isDiscount: e,
            isInteractiveDiscount: t,
            size: u,
            type: a,
            isEnough: n,
            value: r,
            discountValue: s,
            showPlus: i,
            stockBackgroundName: l = Rt.Red,
          }) => {
            const c = v()(Ht.value, Ht[`value__${a}`], !n && Ht.value__notEnough),
              _ = v()(Ht.icon, Ht[`icon__${a}-${u}`]),
              d = v()(Ht.stock, s && Ht.stock__indent, t && Ht.stock__interactive),
              m = i && r > 0 && "+",
              E = v()(Ht.base, Ht[`base__${u}`]);
            return o().createElement(
              "span",
              { className: E },
              o().createElement(
                "span",
                { className: c },
                m,
                o().createElement(Pt, { value: r, format: a === Lt.gold ? "gold" : "integral" }),
              ),
              o().createElement("span", { className: _ }),
              e &&
                o().createElement(
                  "span",
                  { className: d },
                  o().createElement("span", {
                    className: Ht.stockBackground,
                    style: { backgroundImage: `url(R.images.gui.maps.icons.library.${l})` },
                  }),
                  Boolean(s) && s,
                ),
            );
          };
        Wt.defaultProps = { isEnough: !0 };
        const zt = o().memo(Wt),
          Ut = "Tutorial_tutorial_ce",
          Gt = "Tutorial_tutorial_border_ab",
          Vt = "Tutorial_tutorial__hidden_8a",
          jt = "Tutorial_tutorial_hint_bc",
          $t = "Tutorial_tutorial_hintSubstrate_c7",
          Xt = "Tutorial_tutorial_hintArrow_75",
          qt = "Tutorial_tutorial_hintText_b5";
        class Yt extends o().PureComponent {
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
            const e = v()(Ut, { [Vt]: this.props.isHidden });
            return o().createElement(
              "div",
              { className: e, onClick: this.onClick },
              o().createElement("div", { className: Gt }),
              o().createElement(
                "div",
                { className: jt },
                o().createElement("div", { className: $t }),
                o().createElement("div", { className: Xt }),
                o().createElement("div", { className: qt }, this.props.text),
              ),
            );
          }
        }
        const Kt = "HangarCounter_base_43",
          Zt = "HangarCounter_currencyWrapper_cb",
          Jt = "HangarCounter_hangarIcon_46",
          Qt = (0, r.memo)(({ count: e }) => {
            const t = w().mediaSize <= B.Small ? Ot.small : Ot.big;
            return o().createElement(
              "div",
              { className: Kt },
              o().createElement(
                "div",
                { className: Zt },
                o().createElement(zt, { value: e, size: t, type: "equipCoin" }),
              ),
              o().createElement("div", { className: Jt }),
            );
          }),
          eu = "CartPanel_base_e7",
          tu = "CartPanel_base__onlyRightSide_f7",
          uu = "CartPanel_leftSide_d1",
          au = "CartPanel_checkboxContainer_32",
          nu = "CartPanel_rightSide_12",
          ru = "CartPanel_setupButton_b9",
          ou = "CartPanel_deleteButton_b0",
          su = "CartPanel_deleteButtonIcon_77",
          iu = "CartPanel_backButton_ee",
          lu = "CartPanel_backButtonIcon_f2",
          cu = "CartPanel_amountWrapper_f1",
          _u = "CartPanel_amountGold_c6",
          du = "CartPanel_amountRent_c7",
          mu = "CartPanel_amountCredits_7b",
          Eu = "CartPanel_amountEquipment_5b",
          gu = "CartPanel_rentCount_11",
          bu = R.strings.customization,
          pu = R.strings.vehicle_customization.customization,
          Au = R.strings.customization.tooltips.cart,
          Cu = (0, r.memo)(
            ({
              price: e,
              onResetHandler: t,
              onBackHandler: u,
              onApplyHandler: a,
              onAutoRentChange: n,
              onAutoRentHintClose: s,
              cartParams: i,
              buttonSize: l,
              className: c,
            }) => {
              const _ = (0, r.useState)(!1),
                d = _[0],
                m = _[1],
                E = w().mediaSize <= B.Small ? Ot.small : Ot.big,
                g = ((e) =>
                  Array.from(e.values()).reduce((e, t) => {
                    if ("object" == typeof t && null !== t) {
                      const u = t.name,
                        a = t.value;
                      e[u] = (e[u] || 0) + a;
                    }
                    return e;
                  }, {}))(e),
                b = [
                  i.isEnoughMoney ? "" : Au.BuyButtonDisabledNotEnoughMoney(),
                  i.isVehicleCustomized || i.buyButtonEnabled ? "" : Au.buyButtonDisabledDefault(),
                  i.isLockedItem ? pu.lockedItemsApply() : "",
                ].filter((e) => e.length > 0)[0],
                p = i.isRentable && n,
                A = (0, r.useCallback)(() => {
                  (i.showAutoRentHint && (m(!0), s && s()), n && n());
                }, [i.showAutoRentHint, n, s]);
              return o().createElement(
                "div",
                { className: v()(eu, c, !p && tu) },
                p &&
                  o().createElement(
                    "div",
                    { className: uu },
                    i.showAutoRentHint &&
                      o().createElement(Yt, {
                        text: R.strings.tutorial.customization.autoprolongation(),
                        isHidden: d,
                      }),
                    o().createElement(
                      "div",
                      { className: au },
                      o().createElement(xt, {
                        isChecked: i.isAutoRentSelected,
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
                  { className: nu },
                  o().createElement(
                    "div",
                    { className: cu },
                    i.inStorageCount > 0 &&
                      o().createElement(
                        "div",
                        { className: Eu },
                        o().createElement(Qt, { count: i.inStorageCount }),
                      ),
                    i.isRentable &&
                      ((null == g ? void 0 : g.gold) || (null == g ? void 0 : g.credits)) &&
                      !i.inStorageCount &&
                      o().createElement(
                        "div",
                        { className: du },
                        o().createElement(
                          "div",
                          { className: gu },
                          o().createElement(ze, {
                            text: `${i.rentCount} ${bu.cartPanel.rentAmountLabel()}`,
                          }),
                        ),
                      ),
                    i.isGoldPrice
                      ? (null == g ? void 0 : g.gold) &&
                          o().createElement(
                            "div",
                            { className: _u },
                            o().createElement(zt, {
                              value: null == g ? void 0 : g.gold,
                              size: E,
                              type: Lt.gold,
                              isEnough: i.isEnoughMoney,
                            }),
                          )
                      : (null == g ? void 0 : g.credits) &&
                          o().createElement(
                            "div",
                            { className: mu },
                            o().createElement(zt, {
                              value: null == g ? void 0 : g.credits,
                              size: E,
                              type: Lt.credits,
                              isEnough: i.isEnoughMoney,
                            }),
                          ),
                  ),
                  (i.clearButtonEnabled || i.cancelButtonEnabled) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      o().createElement(
                        et,
                        {
                          body: i.cancelButtonEnabled
                            ? Au.cancelButtonEnabled()
                            : Au.cancelButtonDisabled(),
                        },
                        o().createElement(
                          "div",
                          null,
                          o().createElement(
                            $,
                            {
                              type: G.ghost,
                              size: l,
                              mixClass: iu,
                              onClick: u,
                              disabled: !i.cancelButtonEnabled,
                            },
                            o().createElement("div", { className: lu }),
                          ),
                        ),
                      ),
                      o().createElement(
                        et,
                        {
                          body: i.clearButtonEnabled
                            ? Au.clearButtonEnabled()
                            : Au.clearButtonDisabled(),
                        },
                        o().createElement(
                          "div",
                          null,
                          o().createElement(
                            $,
                            {
                              type: G.ghost,
                              size: l,
                              mixClass: ou,
                              onClick: t,
                              soundClick: "cust_select_remove",
                              disabled: !i.clearButtonEnabled,
                            },
                            o().createElement("div", { className: su }),
                          ),
                        ),
                      ),
                    ),
                  o().createElement(
                    et,
                    {
                      body: b || "",
                      isEnabled: i.isEnoughMoney
                        ? !i.isApplyButton && (null == b ? void 0 : b.length) > 0
                        : !i.buyButtonEnabled && (null == b ? void 0 : b.length) > 0,
                    },
                    o().createElement(
                      "div",
                      null,
                      o().createElement(
                        $,
                        {
                          type: G.main,
                          size: l,
                          mixClass: ru,
                          disabled: !i.buyButtonEnabled,
                          onClick: a,
                        },
                        o().createElement(ze, {
                          text: i.isApplyButton
                            ? bu.cartPanel.applyButton()
                            : bu.cartPanel.setupButton(),
                        }),
                      ),
                    ),
                  ),
                ),
              );
            },
          ),
          hu = {
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
          fu = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function vu() {
          return (
            (vu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            vu.apply(this, arguments)
          );
        }
        const Fu = (e) => {
          let t = e.size,
            u = e.value,
            a = e.isEmpty,
            n = e.fadeInAnimation,
            r = e.hide,
            s = e.maximumNumber,
            i = e.className,
            l = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, fu);
          const c = a ? null : u,
            _ = "string" == typeof c;
          if ((c && !_ && c < 0) || 0 === c) return null;
          const d = c && !_ && c > s,
            m = v()(
              hu.base,
              hu[`base__${t}`],
              n && hu.base__animated,
              r && hu.base__hidden,
              !c && hu.base__pattern,
              a && hu.base__empty,
              i,
            );
          return o().createElement(
            "div",
            vu({ className: m }, l),
            o().createElement("div", { className: hu.bg }),
            o().createElement("div", { className: hu.pattern }),
            o().createElement(
              "div",
              { className: v()(hu.value, _ && hu.value__text) },
              d ? s : c,
              d && o().createElement("span", { className: hu.plus }, "+"),
            ),
          );
        };
        Fu.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const Du = {
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
        var Bu;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(Bu || (Bu = {}));
        const Su = ["__left", "__right", "__top", "__bottom"],
          yu =
            ((0, r.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: t, onOutsideClick: u, customStyles: a = {} },
                n,
              ) => {
                const s = (0, r.useRef)(null),
                  l = (0, r.useRef)(null),
                  c = (0, r.useRef)(null),
                  _ = (0, r.useState)(window.decorator && window.decorator.directionType),
                  d = _[0],
                  m = _[1],
                  E = (0, r.useCallback)(() => {
                    (z.playClick(), i.O.view.sendEvent.close());
                  }, []),
                  g = (0, r.useCallback)(() => {
                    z.playHighlight();
                  }, []),
                  b = v()(Du.arrow, Du[`arrow${Su[d]}`]);
                mt(
                  () => (
                    i.O.client.events.mouse.enableOutside(),
                    i.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (u ? u() : i.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const p = (0, r.useCallback)(
                    (e) => {
                      let t = e.target;
                      do {
                        if (t === s.current || t === c.current) return;
                        t = t.parentNode;
                      } while (t);
                      const a = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = i.O.client.getMouseGlobalPosition(),
                          t = ![a.boundX, a.boundY, a.boundWidth, a.boundHeight].includes(void 0),
                          u =
                            e.x < a.boundX ||
                            e.x > a.boundX + a.boundWidth ||
                            e.y > a.boundY + a.boundHeight ||
                            e.y < a.boundY;
                        if (t && !u) return;
                      }
                      u ? u() : i.O.view.sendEvent.close("popover");
                    },
                    [s, c, u],
                  ),
                  A = (0, r.useCallback)(
                    () => (
                      i.O.view.freezeTextureBeforeResize(),
                      q(() => {
                        if (l.current) {
                          const e = l.current.scrollWidth,
                            t = l.current.scrollHeight;
                          (i.O.view.resize(e, t), m(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, r.useImperativeHandle)(n, () => ({ updateSize: A })),
                  mt(() => {
                    i.O.view.setInputPaddingsRem(58);
                  }),
                  (0, r.useEffect)(() => {
                    document.addEventListener("mousedown", p, { capture: !0 });
                    const e = ((e) => {
                      let t = !1;
                      return {
                        promise: new Promise((u, a) => {
                          e.then((e) => !t && u(e)).catch((e) => !t && a(e));
                        }),
                        cancel() {
                          t = !0;
                        },
                      };
                    })((0, $e.Eu)());
                    return (
                      !t && e.promise.then(() => A()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", p));
                      }
                    );
                  }, [A, p, t]),
                  o().createElement(
                    "div",
                    { className: Du.base, ref: l },
                    o().createElement(
                      "div",
                      { className: Du.decorator },
                      o().createElement(
                        "div",
                        { className: Du.content, ref: s },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          o().createElement(
                            et,
                            { body: R.strings.dialogs.common.error.cancel() },
                            o().createElement("div", {
                              className: Du.closeBtn,
                              onClick: E,
                              onMouseEnter: g,
                              ref: c,
                            }),
                          ),
                      ),
                      o().createElement("div", { className: b, style: a.arrow }),
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
        function wu() {
          return (
            (wu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            wu.apply(this, arguments)
          );
        }
        const ku = (e) => {
          let t = e.contentId,
            u = e.decoratorId,
            a = e.direction,
            n = void 0 === a ? Bu.Top : a,
            s = e.targetId,
            i = e.args,
            l = e.onClick,
            c = e.children,
            _ = e.isEnabled,
            d = void 0 === _ || _,
            m = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, yu);
          const E = (0, r.useRef)(null),
            g = (0, r.useCallback)(() => {
              if ((0, $e.wU)()) return (0, $e.SW)();
              E.current && (0, $e.P3)(t, n, E.current, u, s, i);
            }, [t, n, i, u, s]);
          return o().createElement(
            "div",
            wu(
              {
                ref: E,
                onClick:
                  ((b = c.props.onClick),
                  (e) => {
                    d && (g(), l && l(e), b && b(e));
                  }),
              },
              m,
            ),
            c,
          );
          var b;
        };
        let Tu, Nu;
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
        })(Tu || (Tu = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"));
          })(Nu || (Nu = {})));
        const Iu = {
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
          Mu = [
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
        function xu() {
          return (
            (xu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            xu.apply(this, arguments)
          );
        }
        const Ou = (0, r.memo)((e) => {
            let t = e.children,
              u = e.labelRenderer,
              a = e.value,
              n = e.currentValue,
              s = e.autofocus,
              i = void 0 !== s && s,
              l = e.disabled,
              c = void 0 !== l && l,
              _ = e.size,
              d = void 0 === _ ? Nu.Medium : _,
              m = e.label,
              E = e.soundHover,
              g = void 0 === E ? "highlight" : E,
              b = e.soundClick,
              p = void 0 === b ? "play" : b,
              A = e.onMouseEnter,
              C = e.onMouseLeave,
              h = e.onMouseUp,
              f = e.onMouseDown,
              F = e.onClick,
              D = e.onChange,
              B = e.onFocus,
              S = e.onBlur,
              y = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Mu);
            const w = a === n,
              k = (0, r.useState)(!1),
              T = k[0],
              N = k[1],
              I = (0, r.useState)(!1),
              M = I[0],
              x = I[1],
              O = (0, r.useState)(i),
              L = O[0],
              R = O[1],
              P = (0, r.useRef)(null),
              H = (0, r.useCallback)(() => {
                !c && P.current && (P.current.focus(), R(!0));
              }, [c]),
              z = (0, r.useCallback)(
                (e) => {
                  L && null !== P.current && !P.current.contains(e.target) && R(!1);
                },
                [L],
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
                R(i);
              }, [i]));
            const U = (0, r.useCallback)(
                (e) => {
                  c || (D && D(a), F && F(a, e));
                },
                [c, D, F, a],
              ),
              G = (0, r.useCallback)(
                (e) => {
                  if (!c) {
                    const t = e.button === yt.LEFT;
                    (t && N(!0), t && f && f(a, e), p && W(p), i && H());
                  }
                },
                [i, c, f, H, p, a],
              ),
              V = (0, r.useCallback)(
                (e) => {
                  c || (N(!1), h && h(a, e));
                },
                [c, h, a],
              ),
              j = (0, r.useCallback)(
                (e) => {
                  c || (A && A(a, e), g && W(g), x(!0));
                },
                [c, A, g, a],
              ),
              $ = (0, r.useCallback)(
                (e) => {
                  c || (N(!1), x(!1), C && C(a, e));
                },
                [c, C, a],
              ),
              X = (0, r.useCallback)(
                (e) => {
                  c || (R(!0), B && B(a, e));
                },
                [c, B, a],
              ),
              Y = (0, r.useCallback)(
                (e) => {
                  c || (R(!1), S && S(a, e));
                },
                [c, S, a],
              ),
              K = v()(Iu.base, Iu[`base__${d}`], {
                [Iu.base__blank]: !w && !M,
                [Iu.base__blankHover]: !w && M && !T,
                [Iu.base__blankMousedown]: !w && M && T,
                [Iu.base__check]: w && !M,
                [Iu.base__checkHover]: w && M && !T,
                [Iu.base__checkMousedown]: w && M && T,
                [Iu.base__focused]: L,
                [Iu.base__disabled]: c,
              }),
              Z = (0, r.useMemo)(
                () => ({ isHovered: M, isMouseDown: T, isFocused: L, isChecked: w }),
                [M, T, L, w],
              ),
              J = (0, r.useRef)(Iu.blank),
              Q = (0, r.useRef)(Iu.blankHover),
              ee = (0, r.useRef)(Iu.blankMousedown),
              te = (0, r.useRef)(Iu.check),
              ue = (0, r.useRef)(Iu.checkHover),
              ae = (0, r.useRef)(Iu.checkMousedown);
            return (
              (0, r.useEffect)(
                q(() => {
                  ((J.current = v()(Iu.blank, Iu.transition)),
                    (Q.current = v()(Iu.blankHover, Iu.transition)),
                    (ee.current = v()(Iu.blankMousedown, Iu.transition)),
                    (te.current = v()(Iu.check, Iu.transition)),
                    (ue.current = v()(Iu.checkHover, Iu.transition)),
                    (ae.current = v()(Iu.checkMousedown, Iu.transition)));
                }),
                [],
              ),
              o().createElement(
                "div",
                xu(
                  {
                    ref: P,
                    className: K,
                    onClick: U,
                    onMouseEnter: j,
                    onMouseLeave: $,
                    onMouseDown: G,
                    onMouseUp: V,
                    onFocus: X,
                    onBlur: Y,
                  },
                  y,
                ),
                o().createElement(
                  "div",
                  { className: Iu.input },
                  o().createElement("div", { className: J.current }),
                  o().createElement("div", { className: Q.current }),
                  o().createElement("div", { className: ee.current }),
                  o().createElement("div", { className: te.current }),
                  o().createElement("div", { className: ue.current }),
                  o().createElement("div", { className: ae.current }),
                ),
                o().createElement("div", { className: Iu.label }, m || t || (u && u(Z))),
              )
            );
          }),
          Lu = "RadioGroup_base_6e",
          Ru = "RadioGroup_radio_3b",
          Pu = "RadioGroup_label_86",
          Hu = (0, r.memo)(({ data: e, selectedValue: t, onClickHandler: u }) => {
            const a = (0, r.useState)(t),
              n = a[0],
              s = a[1],
              i = (0, r.useCallback)(
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
                { className: Lu },
                null == e
                  ? void 0
                  : e.map((e) =>
                      o().createElement(
                        "div",
                        { className: Ru, key: e.id },
                        o().createElement(
                          et,
                          { header: e.tooltipHeader, body: e.tooltipBody },
                          o().createElement(
                            Ou,
                            { value: e.value, currentValue: n, onClick: () => i(e.value) },
                            o().createElement(ze, { className: Pu, text: e.label }),
                          ),
                        ),
                      ),
                    ),
              )
            );
          }),
          Wu = ["children"];
        function zu() {
          return (
            (zu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            zu.apply(this, arguments)
          );
        }
        const Uu = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, Wu);
          return o().createElement(
            Ke,
            zu(
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
        function Gu() {
          return (
            (Gu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Gu.apply(this, arguments)
          );
        }
        const Vu = ({ children: e, tooltipArgs: t, className: u }) => {
          if (!t) return e;
          const a = o().createElement("div", { className: u }, e);
          if (t.header || t.body) return o().createElement(et, t, a);
          const n = t.contentId,
            r = t.args,
            s = null == r ? void 0 : r.contentId;
          return n || s
            ? o().createElement(Ke, Gu({}, t, { contentId: n || s }), a)
            : o().createElement(Uu, t, a);
        };
        function ju(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function $u(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, u, a) => t(null == e ? void 0 : e.value, u, a));
        }
        function Xu(e, t) {
          for (let u = 0; u < e.length; u++) {
            const a = ju(e[u]);
            if (t(a, u, e)) return a;
          }
        }
        const qu = "ToggleButton_base_19",
          Yu = "ToggleButton_overlay_6b",
          Ku = "ToggleButton_base__active_6c",
          Zu = "ToggleButton_button_1c",
          Ju = "ToggleButton_indicator_9b",
          Qu = "ToggleButton_counter_63",
          ea = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function ta() {
          return (
            (ta =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            ta.apply(this, arguments)
          );
        }
        const ua = o().memo(function (e) {
            let t = e.isActive,
              u = e.counter,
              a = e.className,
              n = e.children,
              r = e.type,
              s = void 0 === r ? G.secondary : r,
              i = e.size,
              l = void 0 === i ? V.small : i,
              c = e.hasIndicator,
              _ = void 0 === c || c,
              d = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, ea);
            return o().createElement(
              "div",
              { className: v()(qu, a, t && Ku) },
              o().createElement($, ta({ type: s, size: l, mixClass: Zu }, d), n),
              o().createElement("div", { className: Yu }),
              _ && o().createElement("div", { className: Ju }),
              Boolean(u) &&
                o().createElement(
                  "div",
                  { className: Qu },
                  o().createElement(Fu, { value: u, size: "small" }),
                ),
            );
          }),
          aa = "FilterTitle_base_53",
          na = "FilterTitle_label_14",
          ra = "FilterTitle_discount_49",
          oa = "FilterTitle_discountIcon_d4",
          sa = ({ label: e, hasDiscount: t, className: u }) =>
            o().createElement(
              "div",
              { className: v()(aa, u) },
              o().createElement("div", { className: na }, e),
              t &&
                o().createElement(
                  "div",
                  { className: ra },
                  o().createElement("div", { className: oa }),
                ),
            ),
          ia = "ToggleIcon_base_31",
          la = "ToggleIcon_base__small_0e",
          ca = "ToggleIcon_icon_9e",
          _a = o().memo(function ({ icon: e, iconParams: t, isSmall: u = !1, classNames: a }) {
            return o().createElement(
              "div",
              { className: v()(ia, null == a ? void 0 : a.base, u && la) },
              o().createElement("div", {
                className: v()(ca, null == a ? void 0 : a.icon),
                style: {
                  backgroundImage: `url(${e})`,
                  width: (null == t ? void 0 : t.iconWidth) || "inherit",
                  height: (null == t ? void 0 : t.iconHeight) || "inherit",
                },
              }),
            );
          }),
          da = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          ma = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Ea = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          ga = (e) =>
            Ea
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let u = ma.length - 1; u >= 0; u--)
                    for (; e >= ma[u];) ((t += da[u]), (e -= ma[u]));
                  return t;
                })(e),
          ba = "VehicleTier_base_99",
          pa = "VehicleTier_base__small_67",
          Aa = ({ level: e, isSmall: t = !1 }) =>
            o().createElement("div", { className: v()(ba, t && pa) }, ga(e)),
          Ca = {
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
          ha = ({
            id: e,
            icon: t,
            iconParams: u,
            type: a,
            isSmall: n = !0,
            isSelected: r = !1,
            baseClassName: s = "",
            iconClassName: i = "",
          }) => {
            return a === Tu.VehicleTier
              ? o().createElement(Aa, { isSmall: n, level: Number(e) })
              : o().createElement(_a, {
                  icon: t,
                  isSmall: n,
                  iconParams: u,
                  classNames: {
                    icon: v()(
                      Ca[`icon__${a}`],
                      Ca[`icon__${a}${((l = e), l[0].toUpperCase() + l.slice(1))}`],
                      r && Ca.icon__selected,
                      i,
                    ),
                    base: s,
                  },
                });
            var l;
          },
          fa = {
            base: "FilterToggleGroup_base_bd",
            title: "FilterToggleGroup_title_5c",
            content: "FilterToggleGroup_content_1b",
            toggle: "FilterToggleGroup_toggle_c2",
            base__inPopup: "FilterToggleGroup_base__inPopup_51",
          },
          va = ["id", "isSelected", "tooltip", "icon", "counter"];
        function Fa() {
          return (
            (Fa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Fa.apply(this, arguments)
          );
        }
        let Da;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(Da || (Da = {}));
        const Ba = ({ header: e, body: t, contentId: u, targetId: a }) =>
            u
              ? { contentId: u, targetId: a }
              : t || e
                ? { header: null != e ? e : void 0, body: null != t ? t : void 0 }
                : void 0,
          Sa = ({
            id: e,
            type: t,
            label: u,
            hasDiscount: a,
            filters: n,
            onClick: r,
            className: s,
            toggleProps: i,
            theme: l = Da.Default,
          }) => {
            const c = l === Da.InPopup;
            return o().createElement(
              "div",
              { className: v()(fa.base, fa[`base__${l}`], s) },
              c && o().createElement(sa, { className: fa.title, label: u, hasDiscount: a }),
              o().createElement(
                "div",
                { className: fa.content },
                $u(n, (u) => {
                  let a = u.id,
                    n = u.isSelected,
                    s = u.tooltip,
                    l = u.icon,
                    _ = u.counter;
                  const d = (function (e, t) {
                      if (null == e) return {};
                      var u,
                        a,
                        n = {},
                        r = Object.keys(e);
                      for (a = 0; a < r.length; a++)
                        ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                      return n;
                    })(u, va),
                    m = d.iconWidth,
                    E = d.iconHeight;
                  return o().createElement(
                    Vu,
                    { key: a, tooltipArgs: Ba(s), className: fa.toggle },
                    o().createElement(
                      ua,
                      Fa({}, i, {
                        className: v()(fa.toggle, null == i ? void 0 : i.className),
                        isActive: n,
                        onClick: () => (null == r ? void 0 : r(e, a)),
                        counter: _,
                      }),
                      o().createElement(ha, {
                        id: a,
                        icon: l,
                        iconParams: { iconWidth: m, iconHeight: E },
                        type: t,
                        isSmall: c,
                        isSelected: n,
                        baseClassName: null == i ? void 0 : i.baseClassName,
                        iconClassName: v()(
                          null == i ? void 0 : i.iconClassName,
                          (null == i ? void 0 : i.parentStyles) &&
                            (null == i ? void 0 : i.parentStyles[`icon_${a}`]),
                        ),
                      }),
                    ),
                  );
                }),
              ),
            );
          },
          ya = () => {
            const e = (0, r.useState)(i.O.view.getScale()),
              t = e[0],
              u = e[1];
            return (
              (0, r.useEffect)(() => {
                const e = () => {
                  u(i.O.view.getScale());
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
          wa = {
            base: "NumberRange_base_65",
            base__animation: "NumberRange_base__animation_70",
            blinkAnim: "NumberRange_blinkAnim_5f",
            from: "NumberRange_from_45",
            from__red: "NumberRange_from__red_53",
            separatorWrapper: "NumberRange_separatorWrapper_5a",
            separator: "NumberRange_separator_61",
            counterGlow: "NumberRange_counterGlow_f6",
          },
          ka = R.strings.crew.barracks.berthsAmountDivider(),
          Ta = R.strings.crew.filterPanel.counter.selectLimit,
          Na = (0, r.memo)(function ({
            isFilterRange: e,
            from: t,
            to: u,
            className: a,
            isSelectMode: n = !1,
            isSelectedLimitReached: r = !1,
            isHideTotalCounter: s = !1,
            counterGlowShift: i,
            classNames: l,
            isAnimationEnabled: c = !1,
          }) {
            const _ = i
              ? o().createElement(
                  "div",
                  { className: wa.separatorWrapper },
                  o().createElement(ze, { className: wa.separator, text: ka }),
                  o().createElement("div", {
                    style: i,
                    className: v()(
                      wa.counterGlow,
                      r && wa.blink,
                      null == l ? void 0 : l.counterGlow,
                    ),
                  }),
                )
              : o().createElement(ze, { className: wa.separator, text: ka });
            return n
              ? o().createElement(
                  et,
                  { header: Ta.header(), body: Ta.body(), ignoreShowDelay: !0 },
                  o().createElement(
                    "div",
                    { className: v()(wa.base, a) },
                    o().createElement(ze, { className: wa.from, text: String(t) }),
                    (t !== u || r) &&
                      o().createElement(
                        o().Fragment,
                        null,
                        _,
                        o().createElement(ze, { text: String(u) }),
                      ),
                  ),
                )
              : o().createElement(
                  "div",
                  {
                    className: v()(
                      wa.base,
                      e ? 0 === t && wa.base__animation : t > u && wa.base__animation,
                      c && wa.base__animation,
                      a,
                    ),
                  },
                  o().createElement(ze, {
                    className: v()(
                      wa.from,
                      e ? 0 === t && u > 0 && wa.from__red : t > u && wa.from__red,
                    ),
                    text: String(t),
                  }),
                  (!s || t !== u) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      _,
                      o().createElement(ze, { text: String(u) }),
                    ),
                );
          }),
          Ia = "NumberRangeWithLabel_base_fd",
          Ma = "NumberRangeWithLabel_counterGlow_fa",
          xa = "NumberRangeWithLabel_blink_15",
          Oa = (0, r.memo)(
            ({
              title: e,
              label: t = "",
              isGlowVisible: u = !1,
              isSelectedLimitReached: a = !1,
              isFilterRange: n = !1,
              isSelectMode: r = !1,
              className: s,
              classNames: i,
              from: l,
              to: c,
              staticCounterGlowShift: _,
              isHideTotalCounter: d = !1,
              isAnimationEnabled: m = !1,
            }) => {
              const E = ya(),
                g =
                  l !== c || a
                    ? 7 * String(l).length * E + 4 * E
                    : Math.round((7 * String(l).length * E) / 2),
                b = { left: _ || g };
              return o().createElement(
                "div",
                { className: v()(Ia, s) },
                t,
                o().createElement(Na, {
                  isFilterRange: n,
                  isSelectedLimitReached: a,
                  isSelectMode: r,
                  from: l,
                  to: c,
                  isHideTotalCounter: d,
                  classNames: i,
                  isAnimationEnabled: m,
                }),
                u &&
                  n &&
                  o().createElement("div", {
                    style: b,
                    className: v()(Ma, a && xa, null == i ? void 0 : i.counterGlow),
                  }),
                e,
              );
            },
          );
        function La() {
          return !1;
        }
        console.log;
        var Ra = u(9174);
        function Pa(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Ha(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return Ha(e, t);
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
        function Ha(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, a = new Array(t); u < t; u++) a[u] = e[u];
          return a;
        }
        const Wa = (e) => (0 === e ? window : window.subViews.get(e));
        const za = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? $u(e, (e) => ("object" == typeof e ? za(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? za(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? za(t) : t]),
                    )
              : e,
          Ua = (e) => za(e);
        var Ga = u(3946);
        const Va = ((e, t) => {
            const u = (0, r.createContext)({});
            return [
              function ({ mode: a = "real", options: n, children: s, mocks: l }) {
                const c = (0, r.useRef)([]),
                  _ = (u, a, n) => {
                    var r;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: u = Wa,
                        context: a = "model",
                      } = {}) {
                        const n = new Map();
                        function r(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? n.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, u) => {
                            u.forEach((t) => {
                              const u = n.get(t);
                              void 0 !== u && u(e);
                            });
                          });
                        });
                        const o = (e) => {
                          const n = u(t),
                            r = a.split(".").reduce((e, t) => e[t], n);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, t) => {
                                const u = e[t];
                                return "function" == typeof u ? u.bind(e) : u;
                              }, r);
                        };
                        return {
                          subscribe: (u, r) => {
                            const s = "string" == typeof r ? `${a}.${r}` : a,
                              l = i.O.view.addModelObserver(s, t, !0);
                            return (n.set(l, u), e && u(o(r)), l);
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
                            for (var e, u = Pa(n.keys()); !(e = u()).done;) r(e.value, t);
                          },
                          unsubscribe: r,
                        };
                      })(a),
                      s =
                        "real" === u
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (r = null == n ? void 0 : n.getter) ? r : () => {},
                            }),
                      l = (e) =>
                        "mocks" === u ? (null == n ? void 0 : n.getter(e)) : s.readByPath(e),
                      _ = (e) => c.current.push(e),
                      d = e({
                        mode: u,
                        readByPath: l,
                        externalModel: s,
                        observableModel: {
                          array: (e, t) => {
                            const a = null != t ? t : l(e),
                              n = Ra.LO.box(a, { equals: La });
                            return (
                              "real" === u &&
                                s.subscribe(
                                  (0, Ra.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          object: (e, t) => {
                            const a = null != t ? t : l(e),
                              n = Ra.LO.box(a, { equals: La });
                            return (
                              "real" === u &&
                                s.subscribe(
                                  (0, Ra.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          primitives: (e, t) => {
                            const a = l(t);
                            if (Array.isArray(e)) {
                              const n = e.reduce((e, t) => ((e[t] = Ra.LO.box(a[t], {})), e), {});
                              return (
                                "real" === u &&
                                  s.subscribe(
                                    (0, Ra.aD)((t) => {
                                      e.forEach((e) => {
                                        n[e].set(t[e]);
                                      });
                                    }),
                                    t,
                                  ),
                                n
                              );
                            }
                            {
                              const n = e,
                                r = Object.entries(n),
                                o = r.reduce((e, [t, u]) => ((e[u] = Ra.LO.box(a[t], {})), e), {});
                              return (
                                "real" === u &&
                                  s.subscribe(
                                    (0, Ra.aD)((e) => {
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
                        cleanup: _,
                      }),
                      m = { mode: u, model: d, externalModel: s, cleanup: _ };
                    return {
                      model: d,
                      controls: "mocks" === u && n ? n.controls(m) : t(m),
                      externalModel: s,
                      mode: u,
                    };
                  },
                  d = (0, r.useRef)(!1),
                  m = (0, r.useState)(a),
                  E = m[0],
                  g = m[1],
                  b = (0, r.useState)(() => _(a, n, l)),
                  p = b[0],
                  A = b[1];
                return (
                  (0, r.useEffect)(() => {
                    d.current ? A(_(E, n, l)) : (d.current = !0);
                  }, [l, E, n]),
                  (0, r.useEffect)(() => {
                    g(a);
                  }, [a]),
                  (0, r.useEffect)(
                    () => () => {
                      (p.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [p],
                  ),
                  o().createElement(u.Provider, { value: p }, s)
                );
              },
              () => (0, r.useContext)(u),
            ];
          })(
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
                u = (0, Ga.Om)(
                  () =>
                    Ua(t.carouselItemsList.get()).slice(0, t.carouselModel.get().totalItemsCount),
                  { equals: La },
                ),
                a = (0, Ga.Om)(() => Xu(u(), (e) => e.isSelected), { equals: La }),
                n = (0, Ga.Om)(
                  () => {
                    var e;
                    return null == (e = a()) ? void 0 : e.intCD;
                  },
                  { equals: La },
                ),
                r = (0, Ga.Om)(() => Ua(t.arrowsList.get()), { equals: La }),
                o = (0, Ga.Om)(() => Ua(t.bookmarksList.get()), { equals: La }),
                s = (0, Ga.Om)(() => Ua(t.tabsItemsList.get()), { equals: La }),
                i = (0, Ga.Om)(() => Xu(s(), (e) => e.isSelected), { equals: La }),
                l = (0, Ga.Om)(
                  () => {
                    var e;
                    return null == (e = i()) ? void 0 : e.itemType;
                  },
                  { equals: La },
                ),
                c = (0, Ga.Om)(() => Ua(t.seasonsTabsItems.get()), { equals: La }),
                _ = (0, Ga.Om)(() => Ua(t.markers.get()), { equals: La }),
                d = (0, Ga.Om)(() => Ua(t.editModeData.get()), { equals: La }),
                m = (0, Ga.Om)(() => Ua(t.toolbarModel.get()), { equals: La }),
                E = (0, Ga.Om)(() => Ua(t.billModel.get()), { equals: La }),
                g = (0, Ga.Om)(() => Ua(t.buyPrice.get()), { equals: La }),
                b = (0, Ga.Om)(() => Ua(t.stageSwitcherWidgetModel.get()), { equals: La }),
                p = (0, Ga.Om)(() => Ua(t.toolbarButtonList.get()), { equals: La }),
                A = (0, Ga.Om)(() => Ua(t.filterModelStructure.get()), { equals: La });
              return Object.assign({}, t, {
                computes: {
                  getItems: u,
                  getSelectedItem: a,
                  getSelectedItemId: n,
                  getCategories: o,
                  getTabsItemsList: s,
                  getSelectedTab: i,
                  getSelectedTabItemType: l,
                  getSeasonsTabsItemsList: c,
                  getMarkersList: _,
                  getEditData: d,
                  getBillModel: E,
                  getBuyPrice: g,
                  getToolbarButtonsList: p,
                  getArrowsList: r,
                  getStageSwitcher: b,
                  getStructureList: A,
                  getToolbarData: m,
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
                (e) => ({ isOver: !(0, $e.wU)() && e }),
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
                (e, t, u, a) => ({ areaId: e, slotType: t, regionIdx: u, hover: a }),
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
          ja = Va[0],
          $a = Va[1],
          Xa = {
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
          qa = R.strings.customization.tooltips.filters,
          Ya = R.strings.customization.filters,
          Ka = R.strings.customization,
          Za = "all",
          Ja = "sale",
          Qa = "inventory",
          en = [
            {
              label: Ya.labelAll(),
              id: Za,
              value: Za,
              name: "availability",
              tooltipHeader: qa.allRadioHeader(),
              tooltipBody: qa.allRadioBody(),
            },
            {
              label: Ya.labelStock(),
              id: Qa,
              value: Qa,
              tooltipHeader: qa.stockRadioHeader(),
              tooltipBody: qa.stockRadioBody(),
            },
            {
              label: Ya.labelSale(),
              id: Ja,
              value: Ja,
              tooltipHeader: qa.saleRadioHeader(),
              tooltipBody: qa.saleRadioBody(),
            },
          ],
          tn = (0, St.Pi)(({ isReverse: e = !1, buttonSize: t }) => {
            const u = $a(),
              a = u.controls,
              n = u.model,
              s = w().mediaSize,
              i = n.filterModel.get(),
              l = i.availability,
              c = i.filteredItemsCounter,
              _ = i.allItemsCounter,
              d = i.newHiddenItemsCounter,
              m = i.isFilteringActive,
              E = i.favorite,
              g = n.computes.getStructureList,
              b = (0, r.useMemo)(
                () => [
                  {
                    id: "fav1",
                    icon: "R.images.gui.maps.icons.customization.icon_favorites",
                    isSelected: E,
                    counter: 0,
                    tooltip: {
                      header: qa.favoritesToggleHeader(),
                      body: qa.favoritesToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
                [E],
              ),
              p = (0, r.useCallback)(() => {
                a.changeFilter("favorite", !E);
              }, [a, E]),
              A = e ? Bu.Top : Bu.Bottom;
            return o().createElement(
              "div",
              { className: v()(Xa.base, e && Xa.reverse) },
              o().createElement(
                "div",
                { className: Xa.counterWrapper },
                o().createElement(
                  ku,
                  {
                    contentId:
                      R.views.lobby.customization.popovers.CustomizationFilterPopoverView("resId"),
                    direction: g().length > 5 && s <= B.Small ? Bu.Left : A,
                  },
                  o().createElement(
                    "div",
                    null,
                    o().createElement(
                      et,
                      { header: qa.popoverButtonTitle(), body: qa.popoverButtonBody() },
                      o().createElement(
                        $,
                        {
                          type: G.ghost,
                          size: t,
                          mixClass: v()(Xa.filtersPopover, e && Xa.filtersPopoverUpdate),
                        },
                        o().createElement("div", { className: Xa.filtersPopoverIcon }),
                      ),
                    ),
                    d > 0 &&
                      o().createElement(Fu, {
                        size: "normal",
                        value: d,
                        className: Xa.hiddenItemCounter,
                      }),
                  ),
                ),
                m &&
                  !e &&
                  o().createElement(Oa, {
                    title:
                      m &&
                      o().createElement(
                        et,
                        { body: Ka.customization.resetFilter.tooltip.text() },
                        o().createElement(
                          $,
                          {
                            type: G.ghost,
                            onClick: a.clearFilter,
                            mixClass: v()(Xa.filtersClearButton),
                          },
                          o().createElement("div", { className: Xa.filtersClearIcon }),
                        ),
                      ),
                    from: c,
                    to: _,
                    isFilterRange: !0,
                    isGlowVisible: !0,
                    isSelectMode: !1,
                    isSelectedLimitReached: d > 0,
                    className: Xa.filterNumbers,
                    staticCounterGlowShift: -1,
                    isAnimationEnabled: d > 0,
                  }),
              ),
              o().createElement(Sa, {
                id: "favorites",
                label: "",
                type: Tu.Default,
                hasDiscount: !1,
                filters: b,
                toggleProps: { type: G.ghost },
                onClick: p,
                className: v()(Xa.buttonFavorites, e && Xa.buttonFavoritesBorder),
              }),
              o().createElement(Hu, { onClickHandler: a.changeFilter, data: en, selectedValue: l }),
            );
          }),
          un = (e, t) => {
            let u;
            const a = setTimeout(() => {
              u = e();
            }, t);
            return () => {
              ("function" == typeof u && u(), clearTimeout(a));
            };
          },
          an = (e, t, u) => Math.min(Math.max(e, t), u),
          nn = {
            base: "Switcher_base_9c",
            base__hasCurrentText: "Switcher_base__hasCurrentText_57",
            base__small: "Switcher_base__small_96",
            base__isVisible: "Switcher_base__isVisible_02",
          },
          rn = (e) => ({ transitionDelay: e / 20 + "s" }),
          on = "SwitcherBullet_base_94",
          sn = "SwitcherBullet_container_28",
          ln = "SwitcherBullet_base__selected_6e",
          cn = "SwitcherBullet_container__text_ff",
          _n = "SwitcherBullet_finishedHover_42",
          dn = "SwitcherBullet_base__finished_e2",
          mn = "SwitcherBullet_base__hover_87",
          En = "SwitcherBullet_iconSmall_d4",
          gn = "SwitcherBullet_base__afterCurrent_f6",
          bn = "SwitcherBullet_iconBig_65",
          pn = "SwitcherBullet_base__currentSelected_eb",
          An = "SwitcherBullet_iconText_ca",
          Cn = "SwitcherBullet_iconTextGlow_a0",
          hn = "SwitcherBullet_clickArea_84",
          fn = "SwitcherBullet_base__disabled_2a",
          vn = "SwitcherBullet_disabled_56",
          Fn = "SwitcherBullet_number_08",
          Dn = "SwitcherBullet_currentText_b6",
          Bn = "SwitcherBullet_text_e9",
          Sn = "SwitcherBullet_texture_b3";
        var yn, wn;
        (!(function (e) {
          ((e.BIG = "big"), (e.SMALL = "small"));
        })(yn || (yn = {})),
          (function (e) {
            ((e.LIGHT = "light"), (e.DARK = "dark"));
          })(wn || (wn = {})));
        const kn = R.images.gui.maps.icons.components.switcher.numbers,
          Tn = (0, r.memo)(
            ({
              numberToDisplay: e,
              index: t,
              selectedIndex: u,
              previousSelectedIndex: a,
              onChange: n,
              currentIndex: s,
              currentText: i,
              isDisabled: l = !1,
              mouseEnterSound: c,
              clickSound: _,
            }) => {
              const d = t !== u,
                m = (0, r.useState)(!1),
                E = m[0],
                g = m[1],
                b = (0, r.useCallback)(() => {
                  (g(!0), d && W(c));
                }, [d, c]),
                p = (0, r.useCallback)(() => {
                  d && (W(_), n(e));
                }, [d, _, e, n]),
                A = (0, r.useCallback)(() => {
                  g(!1);
                }, []),
                C = s || 0,
                h = v()(
                  on,
                  t === u && ln,
                  t === u && t === C && pn,
                  t > C && t !== u && gn,
                  t <= C && dn,
                  E && mn,
                  l && fn,
                ),
                f = (0, r.useMemo)(
                  () =>
                    ((e, t, u) =>
                      e === t
                        ? rn(0)
                        : e === u
                          ? rn(Math.abs(e - t) - 2)
                          : (u > t && e > t && e < u) || (u < t && e < t && e > u)
                            ? rn(Math.abs(e - t) - 1)
                            : void 0)(t, a, u),
                  [t, a, u],
                ),
                F = (0, r.useCallback)(
                  () => ((t === u && t === C) || t === u ? yn.BIG : yn.SMALL),
                  [t, u, C],
                ),
                D = (0, r.useMemo)(() => {
                  const e = t > C ? wn.LIGHT : wn.DARK;
                  return Object.assign({}, f, {
                    backgroundImage: `url(${kn.$dyn(`number_${t}_${F()}_${e}`)})`,
                  });
                }, [t, C, f, F]);
              return o().createElement(
                "div",
                { className: h },
                o().createElement(
                  "div",
                  { className: sn, style: f },
                  o().createElement("div", { className: _n, style: f }),
                  o().createElement("div", { className: En, style: f }),
                  o().createElement("div", { className: bn, style: f }),
                  o().createElement("div", { className: vn }),
                  o().createElement("div", { className: Fn, style: D }),
                  o().createElement("div", {
                    className: hn,
                    style: f,
                    onClick: p,
                    onMouseEnter: b,
                    onMouseLeave: A,
                  }),
                ),
                i && t === s && o().createElement("div", { className: Dn }, i),
              );
            },
          ),
          Nn = ({
            numberToDisplay: e,
            index: t,
            selectedIndex: u,
            previousSelectedIndex: a,
            onChange: n,
            currentIndex: s = 0,
            isDisabled: i = !1,
            mouseEnterSound: l,
            clickSound: c,
            styleID: _,
          }) => {
            const d = t === u,
              m = (0, r.useState)(!1),
              E = m[0],
              g = m[1],
              b = (0, r.useCallback)(() => {
                (g(!0), d || W(l));
              }, [d, l]),
              p = (0, r.useCallback)(() => {
                d || (W(c), n(e));
              }, [d, c, e, n]),
              A = (0, r.useCallback)(() => {
                g(!1);
              }, []),
              C = R.strings.vehicle_customization.style_switcher
                .$dyn(`style_${_}`)
                .$dyn(`level${e}`),
              h = v()(
                on,
                d && ln,
                d && t === s && pn,
                t > s && t !== u && gn,
                t <= s && dn,
                E && mn,
                i && fn,
              ),
              f = (0, r.useMemo)(
                () =>
                  ((e, t, u) =>
                    e === t
                      ? rn(0)
                      : e === u
                        ? rn(Math.abs(e - t) - 2)
                        : (u > t && e > t && e < u) || (u < t && e < t && e > u)
                          ? rn(Math.abs(e - t) - 1)
                          : void 0)(t, a, u),
                [t, a, u],
              ),
              F = v()(sn, cn);
            return o().createElement(
              "div",
              { className: h },
              o().createElement(
                "div",
                { className: F, style: f },
                d && o().createElement("div", { className: Sn }),
                !d && o().createElement("div", { className: Cn }),
                o().createElement("div", { className: An, style: f }),
                o().createElement("div", { className: Bn }, C),
                o().createElement("div", {
                  className: hn,
                  style: f,
                  onClick: p,
                  onMouseEnter: b,
                  onMouseLeave: A,
                }),
              ),
            );
          },
          In = "SwitcherSeparator_base_06",
          Mn = "SwitcherSeparator_base__isBeforeSelectedBullet_a8",
          xn = "SwitcherSeparator_base__notAnimated_73",
          On = "SwitcherSeparator_base__scaled_76",
          Ln = "SwitcherSeparator_base__rightTransformOrigin_b8",
          Rn = "SwitcherSeparator_base__leftTransformOrigin_49",
          Pn = "SwitcherSeparator_base__transitionTransformOrigin_9f",
          Hn = (0, r.memo)(
            ({ index: e, selectedIndex: t, previousSelectedIndex: u, isAnimated: a = !0 }) => {
              const n = ((e, t, u) =>
                  e === t + 1 || e === t - 1
                    ? rn(0)
                    : e === u + 1 || e === u - 1
                      ? rn(Math.abs(u - t) - 2)
                      : (u > t && e > t && e < u + 1) || (u < t && e < t && e > u - 1)
                        ? rn(Math.abs(e - t) - 1)
                        : void 0)(e, u, t),
                r = 1 === Math.abs(e - t),
                s = 1 === Math.abs(e - u),
                i = ((e, t, u, a) =>
                  e === u + 1 || (e === t + 1 && !a)
                    ? Ln
                    : e === u - 1 || (e === t - 1 && !a)
                      ? Rn
                      : void 0)(e, u, t, r),
                l = v()(
                  In,
                  a && e < t && Mn,
                  a && s && r && Pn,
                  a && (e === t + 1 || e === t - 1) && On,
                  a && i,
                  !a && xn,
                );
              return o().createElement("div", { className: l, style: n });
            },
          ),
          Wn = (e, t) => ("number" == typeof e ? 2 * (e - t) : void 0);
        let zn;
        !(function (e) {
          e.small = "small";
        })(zn || (zn = {}));
        const Un = ({
            numberOfBullets: e,
            selectedNumber: t,
            onChange: u,
            currentText: a,
            currentNumber: n,
            startNumber: s = 1,
            isBulletsBeforeCurrentDisabled: i = !1,
            size: l,
            mouseEnterSound: c = "highlight",
            clickSound: _ = "play",
            isArabic: d = !1,
            hasLightShadows: m = !1,
            styleID: E = 0,
            switcherType: g = ut.digital,
          }) => {
            const b = (0, r.useState)(!1),
              p = b[0],
              A = b[1];
            (0, r.useEffect)(() => un(() => A(!0), 0), []);
            const C = s + e - 1,
              h = an(t, i && n ? n : s, C),
              f = "number" == typeof n ? an(n, s, C) : void 0,
              F = Wn(h, s),
              D = Wn(f, s),
              B = (0, r.useRef)(F);
            (0, r.useEffect)(() => {
              B.current = F;
            });
            const S = B.current,
              y = v()(
                nn.base,
                a && void 0 !== D && nn.base__hasCurrentText,
                l && nn[`base__${l}`],
                p && nn.base__isVisible,
              ),
              w = (0, r.useMemo)(
                () =>
                  ((e, t) => {
                    const u = [];
                    for (let a = e; a <= t; a++) u.push(a);
                    return u;
                  })(s, C),
                [C, s],
              ),
              k = g === ut.digital;
            return o().createElement(
              "div",
              { className: y },
              w.map((e, t) => {
                const n = 2 * t,
                  r = !(!i || !D) && n < D;
                return o().createElement(
                  o().Fragment,
                  { key: t },
                  t > 0 &&
                    o().createElement(Hn, {
                      index: n - 1,
                      selectedIndex: F,
                      previousSelectedIndex: S,
                      isAnimated: k,
                    }),
                  k
                    ? o().createElement(Tn, {
                        index: n,
                        selectedIndex: F,
                        previousSelectedIndex: S,
                        numberToDisplay: e,
                        currentIndex: D,
                        currentText: a,
                        onChange: u,
                        isDisabled: r,
                        mouseEnterSound: c,
                        clickSound: _,
                        isArabic: d,
                        hasLightShadows: m,
                      })
                    : o().createElement(Nn, {
                        index: n,
                        selectedIndex: F,
                        previousSelectedIndex: S,
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
          Gn = "EscBtn_base_d0",
          Vn = "EscBtn_esc_97",
          jn = "EscBtn_close_90",
          $n = (0, r.memo)(({ mixClass: e, soundClick: t = "play", onCloseCallback: u }) => {
            const a = v()(Gn, e);
            return o().createElement(
              "div",
              { className: a },
              o().createElement(je, {
                caption: "",
                type: "close",
                soundClick: t,
                onClick: u,
                classNames: { base: jn },
              }),
              o().createElement("div", { className: Vn }),
            );
          }),
          Xn = "Tab_base_05",
          qn = "Tab_content_99",
          Yn = "Tab_base__selected_4b",
          Kn = "Tab_base__accent_b2",
          Zn = "Tab_selectedDivider_25",
          Jn = "Tab_selectedDivider__left_57",
          Qn = "Tab_selectedDivider__right_78",
          er = "Tab_divider_0e",
          tr = "Tab_divider__left_ac",
          ur = "Tab_divider__right_44",
          ar = "Tab_icon_fb",
          nr = "Tab_base__hover_54",
          rr = "Tab_plus_2d",
          or = "Tab_iconWrapper_c5",
          sr = "Tab_label_e8",
          ir = "Tab_highlight_1c",
          lr = "Tab_highlight__left_87",
          cr = "Tab_highlight__right_d6",
          _r = "Tab_tick_a3",
          dr = "Tab_tabsDivider_17",
          mr = "Tab_bubble_4f";
        let Er;
        !(function (e) {
          ((e.Active = "active"), (e.Accent = "accent"), (e.Default = "default"));
        })(Er || (Er = {}));
        const gr = R.images.gui.maps.icons.customization.tabs,
          br = R.strings.customization.itemTypes,
          pr = R.strings.customization.tooltips.tabs,
          Ar = (0, r.memo)(
            ({
              id: e,
              itemType: t,
              isFirst: u,
              isPlus: a,
              isLast: n,
              isPrevAnotherGroup: s,
              isNextAnotherGroup: i,
              isNextSelected: l,
              isAccent: c,
              isSelected: _,
              noveltyCounter: d,
              onClick: m,
              onHoverTab: E,
            }) => {
              const g = (0, r.useState)(!1),
                b = g[0],
                p = g[1],
                A = (0, r.useCallback)(() => {
                  _ || (z.playHighlight(), p(!0), E && E(e));
                }, [e, _, E]),
                C = (0, r.useMemo)(() => {
                  let e;
                  return (
                    (e = _ ? Er.Active : c ? Er.Accent : Er.Default),
                    { backgroundImage: `url(${gr.$dyn(`${t}_${e}`)})` }
                  );
                }, [c, _, t]),
                h = v()(Xn, b && nr, _ && Yn, c && !_ && Kn);
              return o().createElement(
                "div",
                {
                  onClick: () => {
                    m(e);
                  },
                  onMouseEnter: A,
                  onMouseLeave: () => {
                    p(!1);
                  },
                  className: h,
                },
                u && !_ && o().createElement("div", { className: v()(er, tr) }),
                o().createElement(
                  et,
                  {
                    header: String(pr.$dyn(`${t}_title`)),
                    body: String(pr.$dyn(`${t}_description`)),
                  },
                  o().createElement(
                    "div",
                    { className: qn },
                    o().createElement(
                      "div",
                      { className: or },
                      o().createElement("div", { className: ar, style: C }),
                      a && o().createElement("div", { className: rr }),
                    ),
                    o().createElement("div", { className: sr }, br.$dyn(`${t}`)),
                    _
                      ? o().createElement(
                          o().Fragment,
                          null,
                          o().createElement("div", { className: v()(ir, lr) }),
                          o().createElement("div", { className: v()(ir, cr) }),
                          o().createElement("div", { className: _r }),
                          o().createElement("div", { className: v()(Zn, Jn) }),
                          o().createElement("div", { className: v()(Zn, Qn) }),
                        )
                      : o().createElement(
                          o().Fragment,
                          null,
                          s && o().createElement("div", { className: v()(er, tr) }),
                          i && o().createElement("div", { className: v()(er, ur) }),
                        ),
                  ),
                ),
                !i && !_ && !l && o().createElement("div", { className: n ? v()(er, ur) : dr }),
                Boolean(d) && o().createElement(ze, { className: mr, text: d.toString() }),
              );
            },
          ),
          Cr = "Tabs_base_51",
          hr = "Tabs_tabs_ab",
          fr = "Tabs_groupDivider_b2";
        function vr() {
          return (
            (vr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            vr.apply(this, arguments)
          );
        }
        const Fr = (0, r.memo)(
            ({
              isEditable: e,
              tabs: t,
              onClick: u,
              onHoverTab: a,
              onEditClose: n,
              mixClass: r,
            }) => {
              var s;
              const i = null == (s = t.find((e) => e.isSelected)) ? void 0 : s.groupId;
              return o().createElement(
                "div",
                { className: v()(Cr, r) },
                t &&
                  t.map((e, n) => {
                    const r = t[n + 1],
                      s = t[n - 1],
                      l = r && r.isSelected,
                      c = s && e.groupId !== s.groupId,
                      _ = r && e.groupId !== r.groupId,
                      d = e.groupId === i;
                    return o().createElement(
                      "div",
                      { key: `${n}-${e.id}`, className: hr },
                      o().createElement(
                        Ar,
                        vr(
                          {
                            isFirst: 0 === n,
                            isLast: n === t.length - 1,
                            isNextSelected: l,
                            isPrevAnotherGroup: c,
                            isNextAnotherGroup: _,
                            isAccent: d,
                            onClick: u,
                            onHoverTab: a,
                          },
                          e,
                        ),
                      ),
                      _ && o().createElement("div", { className: fr }),
                    );
                  }),
                e && o().createElement($n, { onCloseCallback: n }),
              );
            },
          ),
          Dr = "ExtendedItem_base_8b",
          Br = "ExtendedItem_hoverBg_5c",
          Sr = "ExtendedItem_hoverBg__visible_6a",
          yr = "ExtendedItem_toggleBorder_9c",
          wr = "ExtendedItem_toggleBorder__select_01",
          kr = "ExtendedItem_toggle_24",
          Tr = "ExtendedItem_size_1c",
          Nr = "ExtendedItem_paletteIcon_87",
          Ir = R.images.gui.maps.icons.customization.toolbar.extended,
          Mr = (0, r.memo)(({ item: e, onActionClick: t, actionType: u }) => {
            const a = e.actionData,
              n = e.isSelected,
              s = e.icon,
              i = e.paletteIcon,
              l = (0, r.useState)(!1),
              c = l[0],
              _ = l[1],
              d = n ? Ir.toggle_on() : Ir.toggle_default();
            return o().createElement(
              "div",
              {
                className: Dr,
                onClick: () => {
                  (t(u, a), z.playClick());
                },
                onMouseEnter: () => {
                  (_(!0), z.playHighlight());
                },
                onMouseLeave: () => {
                  _(!1);
                },
              },
              o().createElement("div", { className: v()(Br, c && Sr) }),
              o().createElement("div", { className: v()(yr, n && wr) }),
              o().createElement("div", { className: kr, style: { backgroundImage: `url(${d})` } }),
              Boolean(s.length) && o().createElement(ze, { className: Tr, text: s }),
              Boolean(i.length) &&
                o().createElement("div", {
                  className: Nr,
                  style: { backgroundImage: `url(${i})` },
                }),
            );
          }),
          xr = "ExtendedSubButtons_base_b5",
          Or = "ExtendedSubButtons_bg_4f",
          Lr = "ExtendedSubButtons_content_17",
          Rr = (0, r.memo)(({ subButtons: e, onMouseLeave: t, onActionClick: u, actionType: a }) =>
            o().createElement(
              "div",
              { className: xr, onMouseLeave: t },
              o().createElement(
                "div",
                { className: Lr },
                o().createElement("div", { className: Or }),
                e.map((e) =>
                  o().createElement(Mr, {
                    key: e.actionData,
                    item: e,
                    onActionClick: u,
                    actionType: a,
                  }),
                ),
              ),
            ),
          ),
          Pr = "ToolbarItem_base_c1",
          Hr = "ToolbarItem_base__disable_40",
          Wr = "ToolbarItem_hoverBg_89",
          zr = "ToolbarItem_hoverBg__visible_c9",
          Ur = "ToolbarItem_icon_65",
          Gr = "ToolbarItem_icon__disable_ef",
          Vr = "ToolbarItem_disable_43",
          jr = "ToolbarItem_hoveredIcon_a8",
          $r = "ToolbarItem_base__hover_02",
          Xr = "ToolbarItem_actionName_38",
          qr = "ToolbarItem_arrow_f4",
          Yr = "ToolbarItem_arrow__left_00",
          Kr = "ToolbarItem_arrow__leftHover_72",
          Zr = "ToolbarItem_arrow__right_a9",
          Jr = "ToolbarItem_arrow__rightHover_a9",
          Qr = "ToolbarItem_arrow__leftDisable_8c",
          eo = "ToolbarItem_arrow__rightDisable_bd";
        let to, uo;
        (!(function (e) {
          ((e[(e.RIGHT = 0)] = "RIGHT"), (e[(e.LEFT = 1)] = "LEFT"));
        })(to || (to = {})),
          (function (e) {
            ((e.COLOR_CHANGE = "color_change"), (e.SCALE_CHANGE = "scale_change"));
          })(uo || (uo = {})));
        const ao = R.images.gui.maps.icons.customization.toolbar,
          no = [uo.COLOR_CHANGE, uo.SCALE_CHANGE],
          ro = [
            tt.CUSTOMIZATION_SHEET_ACTION_REMOVE_ONE,
            tt.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_SEASONS,
            tt.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_PARTS,
          ],
          oo = (0, r.memo)(({ toolbarItem: e, onItemClick: t, onItemOver: u, isSelected: a }) => {
            const n = e.actionType,
              s = e.isEnabled,
              i = e.actionBtnLabel,
              l = e.subButtons,
              c = e.progressionLevel,
              _ = `${n}${c}`,
              d = c > 0,
              m = s ? ao.default.$dyn(d ? _ : n) : ao.disable.$dyn(n),
              E = ao.idle.$dyn(d ? _ : n),
              g = (0, r.useState)(!1),
              b = g[0],
              p = g[1],
              A = (0, r.useState)(!1),
              C = A[0],
              h = A[1],
              f = (0, r.useState)(!1),
              F = f[0],
              D = f[1],
              B = (0, r.useState)({ left: !1, right: !1 }),
              S = B[0],
              y = B[1],
              w = no.includes(n);
            (0, r.useEffect)(() => {
              (a && s && p(!0), a && w && D(!0));
            }, [a, w, s]);
            const k = (0, r.useCallback)(() => {
                (h(!1), a && w && h(!0));
              }, [a, w]),
              T = (e, u) => {
                (e.stopPropagation(), t(n, u));
              },
              N = (e) => {
                s &&
                  (e === to.LEFT
                    ? y((e) => Object.assign({}, e, { left: !0 }))
                    : y((e) => Object.assign({}, e, { right: !0 })));
              },
              I = (e) => {
                s &&
                  (e === to.LEFT
                    ? y((e) => Object.assign({}, e, { left: !1 }))
                    : y((e) => Object.assign({}, e, { right: !1 })));
              },
              M = w && C && a,
              x = v()(Pr, b && $r, !s && Hr),
              O = v()(qr, Yr, S.left && s && Kr, !s && Qr),
              L = v()(qr, Zr, S.right && s && Jr, !s && eo);
            return o().createElement(
              "div",
              {
                onMouseEnter: () => {
                  s && (p(!0), w && !C && h(!0), u(n), z.playHighlight());
                },
                onMouseLeave: () => {
                  (p(!1), C && h(!1), F && D(!1));
                },
                onClick: () => {
                  s &&
                    !w &&
                    (n === tt.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS
                      ? W(R.sounds.cust_select_double())
                      : n === tt.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_PARTS
                        ? W(R.sounds.cust_color_apply())
                        : ro.includes(n)
                          ? W(R.sounds.cust_select_remove())
                          : W(R.sounds.cust_select()),
                    t(n, d ? to.RIGHT : -1));
                },
                className: x,
              },
              (M || F) &&
                s &&
                o().createElement(Rr, {
                  subButtons: l,
                  actionType: n,
                  onActionClick: t,
                  onMouseLeave: k,
                }),
              o().createElement("div", { className: v()(Wr, b && zr) }),
              !s && o().createElement("div", { className: Vr }),
              o().createElement(ze, { text: i, className: Xr }),
              d &&
                o().createElement("div", {
                  className: O,
                  onMouseEnter: () => N(to.LEFT),
                  onMouseLeave: () => I(to.LEFT),
                  onClick: (e) => T(e, to.LEFT),
                }),
              o().createElement("div", {
                className: v()(Ur, !s && Gr),
                style: { backgroundImage: `url(${m})` },
              }),
              o().createElement("div", { className: jr, style: { backgroundImage: `url(${E})` } }),
              d &&
                o().createElement("div", {
                  className: L,
                  onMouseEnter: () => N(to.RIGHT),
                  onMouseLeave: () => I(to.RIGHT),
                  onClick: (e) => T(e, to.RIGHT),
                }),
            );
          }),
          so = "Toolbar_base_56",
          io = "Toolbar_content_31",
          lo = { type: "", index: -1 },
          co = (0, r.memo)(({ toolbarItems: e, onItemClick: t }) => {
            const u = (0, r.useState)(lo),
              a = u[0],
              n = u[1];
            (0, r.useEffect)(() => () => n(lo), [e]);
            const s = (0, r.useCallback)((e) => {
                n((t) => Object.assign({}, t, { type: e }));
              }, []),
              i = (0, r.useCallback)(
                (e, u, a) => {
                  (t(e, u), n({ type: e, index: a }));
                },
                [t],
              );
            return o().createElement(
              "div",
              { className: so },
              o().createElement(
                "div",
                { className: io },
                e.map((e, t) =>
                  o().createElement(
                    Vu,
                    {
                      key: e.actionType,
                      tooltipArgs: {
                        body: e.disableTooltip,
                        isEnabled: Boolean(e.disableTooltip.length),
                      },
                    },
                    o().createElement(oo, {
                      key: e.actionType,
                      toolbarItem: e,
                      onItemClick: (e, u) => i(e, u, t),
                      onItemOver: s,
                      isSelected: a.type === e.actionType || t === a.index,
                    }),
                  ),
                ),
              ),
            );
          }),
          _o = "AllSeasonsHint_base_d7",
          mo = "AllSeasonsHint_text_7b",
          Eo = R.strings.customization.customization.allSeasonsHint,
          go = R.strings.customization.itemTypes,
          bo = (0, r.memo)(({ itemType: e, isSelected: t, onSelectApplyingAllSeasons: u }) => {
            const a = w().mediaSize <= B.Small,
              n = a ? kt.medium : kt.large;
            return o().createElement(
              et,
              { header: Eo.tooltip.header(), body: Eo.tooltip.body() },
              o().createElement(
                "div",
                { className: _o },
                o().createElement(
                  xt,
                  {
                    isChecked: t,
                    size: n,
                    type: Tt.main,
                    soundHover: R.sounds.highlight(),
                    soundClick: R.sounds.play(),
                    onChange: () => {
                      u();
                    },
                  },
                  o().createElement(ze, {
                    text: a ? Eo.shortText() : Eo.text(),
                    className: mo,
                    format: {
                      binding: !a && e ? { item: String(go.$dyn(`${e}`)).toLowerCase() } : void 0,
                    },
                  }),
                ),
              ),
            );
          }),
          po = 33,
          Ao = 0,
          Co = !0,
          ho = "play";
        const fo = [
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
        function vo() {
          return (
            (vo =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            vo.apply(this, arguments)
          );
        }
        const Fo = (0, r.memo)(function (e) {
            let t = e.width,
              u = e.height,
              a = e.getImageSource,
              n = e.frameCount,
              s = e.onAnimate,
              i = e.frameTime,
              l = void 0 === i ? po : i,
              c = e.initialFrameIndex,
              _ = void 0 === c ? Ao : c,
              d = e.lastFrameIndex,
              m = void 0 === d ? n - 1 : d,
              E = e.loop,
              g = void 0 === E ? Co : E,
              b = e.state,
              p = void 0 === b ? ho : b,
              A = e.onAnimationDone,
              C = e.onAnimationComplete,
              h = e.poster,
              f = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, fo);
            const v = (0, r.useRef)(null);
            return (
              (0, r.useEffect)(() => {
                const e = v.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  u = (u) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(u.img, -u.x, -u.y));
                  };
                switch (p) {
                  case "play":
                    return (function () {
                      const e = So(_, m, a),
                        t = Do(_, m),
                        n = window.setInterval(() => {
                          const a = t(),
                            r = e.get(a);
                          r
                            ? (null == s || s(a, r),
                              u(r),
                              a === m &&
                                (null == C || C(),
                                g || (null == A || A(), window.clearInterval(n))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, l);
                      return () => window.clearInterval(n);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === _ && h ? { path: h, x: 0, y: 0 } : a(_),
                        t = new Image();
                      t.src = e.path;
                      const n = () => u(Bo(e, t));
                      return (
                        t.addEventListener("load", n),
                        () => t.removeEventListener("load", n)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [l, a, _, m, g, s, C, A, h, p]),
              o().createElement("canvas", vo({}, f, { width: t, height: u, ref: v }))
            );
          }),
          Do = (e, t) => {
            let u = e;
            return () => {
              const a = u;
              return ((u += 1), u > t && (u = e), a);
            };
          },
          Bo = (e, t) => Object.assign({}, e, { img: t }),
          So = (e, t, u) => {
            const a = new Map(),
              n = {};
            for (let r = e; r <= t; r++) {
              const e = u(r),
                t = n[e.path];
              if (t) a.set(r, Bo(e, t));
              else {
                const t = new Image();
                ((n[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${r})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  a.set(r, Bo(e, t)));
              }
            }
            return a;
          };
        let yo;
        !(function (e) {
          ((e.Active = "active"), (e.Ending = "ending"), (e.Disabled = "disabled"));
        })(yo || (yo = {}));
        const wo = (e) => (e < 0.5 ? 4 * e * e * e : (e - 1) * (2 * e - 2) * (2 * e - 2) + 1),
          ko = (e) => {
            const t = ((e) => {
                const t = new Date(1e3 * e);
                return { day: t.getDate(), month: t.getMonth() };
              })(e),
              u = t.day,
              a = t.month;
            return { day: u, month: R.strings.menu.dateTime.months.$num(a + 1) };
          },
          To = (0, r.memo)(
            ({
              children: e,
              isVisible: t = !0,
              delay: u = 0,
              duration: a = 800,
              opacityFrom: n = 0,
              opacityEnter: r = 1,
              opacityLeave: s = 0,
              classMix: i,
            }) =>
              (0, ee.useTransition)(t, {
                key: t,
                from: { opacity: n },
                enter: { opacity: r },
                leave: { opacity: s },
                delay: u,
                config: { duration: a, easing: wo },
              })((t, u) => u && o().createElement(ee.animated.div, { className: i, style: t }, e)),
          ),
          No = {
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
        function Io() {
          return (
            (Io =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Io.apply(this, arguments)
          );
        }
        var Mo;
        !(function (e) {
          ((e.Large = "large"), (e.Big = "big"), (e.Medium = "medium"), (e.Small = "small"));
        })(Mo || (Mo = {}));
        const xo = R.strings.event.customizationResource,
          Oo = {
            width: 280,
            height: 170,
            frameCount: 136,
            chunk: { count: 1, rows: 20, columns: 7 },
            getChunkPath: () =>
              "R.images.gui.maps.icons.event.customizationResource.entryPoint.particles_sequence",
          },
          Lo = (function (e) {
            const t = e.chunk,
              u = t.rows * t.columns;
            return (a) => {
              const n = a % u,
                r = (n % t.columns) * e.width,
                o = Math.trunc(n / t.columns) * e.height;
              return { path: e.getChunkPath(Math.trunc(a / u)), x: r, y: o };
            };
          })(Oo),
          Ro = (e) => {
            const t = (function (e = 0) {
                let t = e;
                const u = Math.trunc(t / st);
                t -= u * st;
                const a = Math.trunc(t / ot);
                t -= a * ot;
                const n = Math.trunc(t / rt);
                return ((t -= n * rt), { days: u, hours: a, minutes: n, seconds: t });
              })(e),
              u = t.days,
              a = t.hours,
              n = t.minutes,
              r = R.strings.common.duration;
            if (u) {
              let e = xo.eventFinishFormat() + he(r.days(), { days: u });
              return (a && (e += " " + he(r.hours(), { hours: a })), e);
            }
            if (a) {
              let e = xo.eventFinishFormat() + he(r.hours(), { hours: a });
              return (n && (e += " " + he(r.minutes(), { minutes: n })), e);
            }
            return n
              ? xo.eventFinishFormat() + he(r.minutes(), { minutes: n })
              : xo.lessThanMinute();
          },
          Po = (0, St.Pi)(({ mixClass: e }) => {
            const t = $a(),
              u = t.controls,
              a = t.model,
              n = w().mediaSize,
              s = (function (e = {}, t = []) {
                var u, a, n, o;
                const s = (0, r.useState)(null != (u = e.state) ? u : ho),
                  i = s[0],
                  l = s[1],
                  c = (0, r.useState)(null != (a = e.initialFrameIndex) ? a : Ao),
                  _ = c[0],
                  d = c[1],
                  m = (0, r.useState)(null != (n = e.frameTime) ? n : po),
                  E = m[0],
                  g = m[1],
                  b = (0, r.useState)(null != (o = e.loop) ? o : Co),
                  p = b[0],
                  A = b[1],
                  C = (0, r.useRef)(_),
                  h = (0, r.useCallback)((e) => {
                    (d(e), l("play"));
                  }, []),
                  f = (0, r.useCallback)((e) => {
                    (d(e), l("stop"));
                  }, []),
                  v = (0, r.useCallback)(() => {
                    (d(0), l("stop"));
                  }, []),
                  F = (0, r.useCallback)(() => l("play"), []),
                  D = (0, r.useCallback)(() => {
                    (d(C.current + 1), l("stop"));
                  }, []);
                return {
                  props: {
                    state: i,
                    initialFrameIndex: _,
                    frameTime: E,
                    loop: p,
                    onAnimate: (0, r.useCallback)((t, u) => {
                      ((C.current = t), null == e.onAnimate || e.onAnimate(t, u));
                    }, t),
                    onAnimationDone: (0, r.useCallback)(() => {
                      v();
                    }, t),
                  },
                  enableLoop: (0, r.useCallback)(() => A(!0), []),
                  disableLoop: (0, r.useCallback)(() => A(!1), []),
                  setState: l,
                  setInitialFrameIndex: d,
                  setFrameTime: g,
                  goAndPlay: h,
                  goAndStop: f,
                  stop: v,
                  play: F,
                  pause: D,
                };
              })(),
              i = a.root.get(),
              l = i.timer,
              c = i.status,
              _ = i.isLimitsUpdated,
              d = i.isAloneBanner,
              m = c === yo.Active,
              E = c === yo.Disabled,
              g = c === yo.Ending,
              b = dt(l - Math.floor(Date.now() / 1e3), rt);
            const p = (0, r.useMemo)(() => Ro(b), [b]),
              A = (0, r.useState)(!1),
              C = A[0],
              h = A[1],
              f = (0, r.useMemo)(() => ko(l), [l]),
              F = f.day,
              D = f.month,
              S = (0, r.useMemo)(
                () =>
                  n >= B.Large ? Mo.Large : d ? Mo.Big : n === B.Medium ? Mo.Medium : Mo.Small,
                [n, d],
              ),
              y = (0, ee.useSpring)({
                from: { x: 0, opacity: 0 },
                to: { x: 0, opacity: 1 },
                delay: 0,
                config: { duration: 800, easing: wo },
              });
            return o().createElement(
              ee.animated.div,
              {
                className: v()(
                  No.base,
                  E && No.base__disabled,
                  No[`base__${S}`],
                  C && No.base__hover,
                  d && No.base__isAloneBanner,
                  e,
                ),
                onMouseEnter: () => {
                  E || (z.playHighlight(), h(!0));
                },
                onMouseLeave: () => {
                  h(!1);
                },
                onClick: () => {
                  E || (z.playClick(), u.toCustomizationResourceEvent());
                },
                style: y,
              },
              o().createElement("div", { className: No.bg }),
              o().createElement("div", { className: No.shadow }),
              o().createElement(To, { classMix: No.highlight, isVisible: C }),
              o().createElement(
                "div",
                { className: No.content },
                o().createElement(ze, { className: No.title, text: xo.title() }),
                _ &&
                  o().createElement(ze, {
                    className: No.subTitle,
                    text: n >= B.Large ? xo.subTitle() : xo.shortSubTitle(),
                  }),
              ),
              o().createElement(
                "div",
                { className: v()(No.timeContent, E && No.timeContent__disabled) },
                m &&
                  o().createElement(ze, {
                    className: No.timeActive,
                    text: xo.endDateText(),
                    format: { binding: { day: F, month: D } },
                  }),
                g && o().createElement(ze, { className: No.timeEnding, text: p }),
                E &&
                  o().createElement(ze, { className: No.timeEnding, text: xo.unavailable.text() }),
              ),
              _ &&
                o().createElement(
                  Fo,
                  Io({}, s.props, {
                    width: Oo.width,
                    height: Oo.height,
                    frameCount: Oo.frameCount,
                    getImageSource: Lo,
                    frameTime: 50,
                    loop: !0,
                    className: No.particles,
                  }),
                ),
            );
          });
        let Ho;
        !(function (e) {
          ((e[(e.Empty = 0)] = "Empty"),
            (e[(e.SubmitEnter = 1)] = "SubmitEnter"),
            (e[(e.FirstEnter = 2)] = "FirstEnter"),
            (e[(e.EditEnter = 3)] = "EditEnter"),
            (e[(e.NotAvailableEnter = 4)] = "NotAvailableEnter"));
        })(Ho || (Ho = {}));
        const Wo = "Inscription_base_27",
          zo = "Inscription_base__invalidInput_3d",
          Uo = "Inscription_base__show_19",
          Go = "Inscription_base__hide_4c",
          Vo = "Inscription_base__withIcons_ea",
          jo = "Inscription_invalidEnterIcon_5f",
          $o = "Inscription_icons_1d",
          Xo = "Inscription_icon_44",
          qo = "Inscription_icon__withDelete_9a",
          Yo = "Inscription_text_7e",
          Ko = "Inscription_invalidNumber_78",
          Zo = R.strings.vehicle_customization.propertySheet.inscriptionController,
          Jo = {
            [Ho.Empty]: "",
            [Ho.EditEnter]: Zo.editEnter(),
            [Ho.FirstEnter]: Zo.firstEnter(),
            [Ho.SubmitEnter]: Zo.submitEnter(),
            [Ho.NotAvailableEnter]: Zo.notAvailableEnter(),
          },
          Qo = {
            [Ho.Empty]: [],
            [Ho.EditEnter]: [
              R.images.gui.maps.icons.customization.inscription_controller.bspace_btn(),
              R.images.gui.maps.icons.customization.inscription_controller.delete_btn(),
            ],
            [Ho.FirstEnter]: [],
            [Ho.SubmitEnter]: [
              R.images.gui.maps.icons.customization.inscription_controller.enter_btn(),
            ],
            [Ho.NotAvailableEnter]: [],
          },
          es = (0, r.memo)(
            ({
              inscriptionState: e,
              inscriptionDuration: t,
              inscriptionDelay: u,
              invalidInscriptionNumber: a,
              inscriptionFirstEnterRange: n,
              startTimestamp: s,
            }) => {
              const i = (0, r.useState)(!1),
                l = i[0],
                c = i[1],
                _ = (0, r.useState)(e),
                d = _[0],
                m = _[1],
                E = Et(),
                g = Et();
              (0, r.useEffect)(
                () => (
                  c(!1),
                  g.run(() => {
                    (c(!0), m(e));
                  }, u),
                  E.run(() => {
                    c(!1);
                  }, t + u),
                  () => {
                    (g.clear(), E.clear());
                  }
                ),
                [s],
              );
              const b = d === Ho.NotAvailableEnter;
              return o().createElement(
                "div",
                { className: v()(Wo, b && zo, l && Uo, !l && Go, Boolean(Qo[d].length) && Vo) },
                b && o().createElement("div", { className: jo }),
                o().createElement(ze, {
                  className: Yo,
                  text: Jo[d],
                  format: {
                    binding: {
                      value: o().createElement(ze, { className: Ko, text: a }),
                      start: Boolean(n.length) && n[0],
                      end: Boolean(n.length > 1) && n[1],
                    },
                  },
                }),
                !b &&
                  Boolean(Qo[d].length) &&
                  o().createElement(
                    "div",
                    { className: $o },
                    Qo[d].map((e, t) =>
                      o().createElement("div", {
                        className: v()(Xo, d === Ho.EditEnter && qo),
                        key: t,
                        style: { backgroundImage: `url(${e})` },
                      }),
                    ),
                  ),
              );
            },
          ),
          ts = {
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
          us = ({ isEnabled: e, icon: t, isWide: u, isDim: a, formFactor: n, selectedTab: s }) => {
            const l = (0, r.useRef)(null),
              c = _t(e);
            ((0, r.useEffect)(() => {
              !e && c && s !== j_.INSCRIPTION && W(R.sounds.cancelcloseno());
            }, [e, c, s]),
              (0, r.useEffect)(() => {
                if (!e) return;
                const t = i.O.client.events.mouse.move(([{ clientX: e, clientY: t }, u]) => {
                  const a = l.current;
                  a &&
                    ("outside" !== u
                      ? (a.style.setProperty("--visibility", "visible"),
                        a.style.setProperty("--x", `${viewEnv.pxToRem(e + 7)}rem`),
                        a.style.setProperty("--y", `${viewEnv.pxToRem(t + -40)}rem`))
                      : a.style.setProperty("--visibility", "hidden"));
                });
                return () => {
                  t();
                };
              }, [e]));
            const _ = n > 0,
              d = v()(ts.base, !_ && u && ts.base__wide, _ && ts[`base__factor${n}`]);
            return o().createElement(
              "div",
              { className: d },
              e &&
                o().createElement(
                  "div",
                  { ref: l, className: ts.wrapper },
                  a && o().createElement("div", { className: ts.shine }),
                  o().createElement("div", {
                    className: ts.icon,
                    style: { backgroundImage: `url(${t})` },
                  }),
                  o().createElement("div", { className: ts.border }),
                ),
            );
          },
          as = "SceneHitArea_base_ec",
          ns = "SceneHitArea_base__down_e8",
          rs = "SceneHitArea_base__cursorActive_6e";
        let os;
        !(function (e) {
          ((e.None = "none"), (e.Ready = "ready"), (e.Dragging = "dragging"));
        })(os || (os = {}));
        const ss = ({
            moveSpace: e,
            onSceneOverChange: t,
            onSceneDraggingChange: u,
            onSceneClick: a,
            onHideElements: n,
            onResetMagneticTool: s,
            isHovered: l,
            isOnboardingViewOpened: c = !1,
          }) => {
            const _ = (0, r.useState)(!1),
              d = _[0],
              m = _[1],
              E = (0, r.useRef)({ x: 0, y: 0, state: os.None }),
              g = (0, r.useRef)(null),
              b = (0, r.useRef)(null);
            ((0, r.useEffect)(() => {
              const e = i.O.client.events.mouse.up(([e]) => {
                (m(!1),
                  E.current.state === os.Ready && a(),
                  b.current && (clearTimeout(b.current), (b.current = null)),
                  n(!1),
                  u(!1));
                const t = e;
                if (t && t.button === yt.RIGHT) s();
                else {
                  const e = t && t.target;
                  e && e !== g.current && !e.closest("[data-magnetic-tool-support]") && s();
                }
                E.current.state = os.None;
              });
              return () => e();
            }, [E, n, a, u, s]),
              (0, r.useEffect)(
                () => () => {
                  b.current && clearTimeout(b.current);
                },
                [],
              ));
            const p = (e) => {
              if (!g.current) return;
              const t = g.current.getBoundingClientRect(),
                u = t.width,
                a = t.height;
              return !(
                0 === e.clientX ||
                0 === e.clientY ||
                e.clientX >= u - 1 ||
                e.clientY >= a - 1
              );
            };
            return o().createElement("div", {
              className: v()(as, d && ns, l && rs),
              ref: g,
              onMouseDown: (e) => {
                (e.preventDefault(),
                  e.button === yt.LEFT &&
                    p(e) &&
                    (m(!0),
                    (E.current.x = e.clientX),
                    (E.current.y = e.clientY),
                    (E.current.state = os.Ready),
                    u(!0),
                    (b.current = setTimeout(() => {
                      ((b.current = null), n(!0));
                    }, 200))));
              },
              onMouseMove: (t) => {
                if ((t.preventDefault(), d)) {
                  if (!p(t)) return;
                  const u = E.current,
                    a = t.clientX !== u.x ? t.clientX - u.x : 0,
                    r = t.clientY !== u.y ? t.clientY - u.y : 0;
                  (0 !== a && 0 !== r && (u.state = os.Dragging),
                    (u.x = t.clientX),
                    (u.y = t.clientY),
                    e({ dx: a, dy: r, dz: 0 }),
                    b.current && (clearTimeout(b.current), (b.current = null), n(!0)));
                }
              },
              onWheel: (t) => {
                if ((t.preventDefault(), !p(t))) return;
                const u = t.deltaY < 0;
                e({ dx: 0, dy: 0, dz: u ? -600 : 600 });
              },
              onMouseEnter: () => {
                !c && t(!0);
              },
              onMouseLeave: () => {
                !c && t(!0);
              },
            });
          },
          is = "BannerDecals_base_b8",
          ls = "BannerDecals_base__hover_b3",
          cs = "BannerDecals_title_f7",
          _s = R.strings.customization,
          ds = (0, r.memo)(({ onClick: e, onMouseLeave: t, onMouseEnter: u, mixClass: a }) => {
            const n = (0, r.useState)(!1),
              s = n[0],
              i = n[1],
              l = (0, r.useState)(!1),
              c = l[0],
              _ = l[1];
            return o().createElement(
              "div",
              {
                className: v()(is, s && ls, a),
                onMouseEnter: () => {
                  (u && u(), i(!0), z.playHighlight());
                },
                onMouseLeave: () => {
                  (!c && t && t(), i(!1));
                },
                onClick: () => {
                  (u && u(), _(!0), z.playClick(), e());
                },
              },
              o().createElement(ze, { className: cs, text: _s.customization.decalsBanner() }),
            );
          }),
          ms = {
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
          Es = R.strings.customization.customization.seasonsTabs,
          gs = R.images.gui.maps.icons.customization.seasons,
          bs = (0, r.memo)(
            ({
              onClick: e,
              isSelected: t,
              season: u,
              isShowFullTabContent: a,
              isAllTabsFull: n,
              isFull: s,
              className: i,
            }) => {
              var l;
              const c = (0, r.useState)(!1),
                _ = c[0],
                d = c[1],
                m = (0, r.useState)(null),
                E = m[0],
                g = m[1],
                b = Et(),
                p = null != (l = _t(s)) ? l : s;
              ((0, r.useEffect)(() => {
                if (b.isRunning) return () => b.clear();
              }, [b]),
                (0, r.useEffect)(() => {
                  (!p && s && (g(!0), !n && W(R.sounds.cust_tick_on())),
                    p && !s && W(R.sounds.cust_tick_off()));
                }, [p, s, b, n]),
                (0, r.useEffect)(() => {
                  if (E)
                    return b.run(() => {
                      g(!1);
                    }, 1200);
                }, [b, E]));
              const A = (0, r.useCallback)(() => {
                  b.isRunning || e(u);
                }, [b, e, u]),
                C = v()(
                  ms.base,
                  ms[`base__${u}`],
                  s && !E && ms.base__full,
                  E && ms.base__animatingAppear,
                  !E && null !== E && ms.base__animatingDisappear,
                  _ && ms.base__hover,
                  t && ms.base__active,
                  a && ms.base__fullContent,
                  i,
                );
              return o().createElement(
                "div",
                {
                  onMouseEnter: () => {
                    t || (0, $e.wU)() || (d(!0), z.playHighlight());
                  },
                  onMouseLeave: () => {
                    d(!1);
                  },
                  onClick: A,
                  className: C,
                },
                o().createElement("div", { className: ms.background }),
                t &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", { className: ms.blink }),
                    o().createElement(
                      "div",
                      {
                        className: ms.activeTab,
                        style: { backgroundImage: `url(${gs.$dyn(`${u}_bg`)})` },
                      },
                      o().createElement("div", {
                        className: ms.shine,
                        style: { backgroundImage: `url(${gs.$dyn(`${u}_shine`)})` },
                      }),
                    ),
                  ),
                o().createElement(
                  "div",
                  { className: ms.iconsWrapper },
                  o().createElement(
                    "div",
                    { className: ms.seasonIconWrapper },
                    o().createElement("div", {
                      className: v()(
                        ms.seasonIcon,
                        _ || t ? ms.seasonIcon__hide : ms.seasonIcon__show,
                      ),
                      style: { backgroundImage: `url(${gs.$dyn(`${u}_default`)})` },
                    }),
                    o().createElement("div", {
                      className: v()(
                        ms.seasonIcon,
                        _ || t ? ms.seasonIcon__show : ms.seasonIcon__hide,
                      ),
                      style: { backgroundImage: `url(${gs.$dyn(`${u}_active`)})` },
                    }),
                  ),
                  o().createElement("div", { className: ms.plus }),
                  o().createElement("div", { className: ms.check }),
                ),
                o().createElement(
                  "div",
                  { className: ms.titleWrapper },
                  o().createElement(ze, { text: Es.$dyn(`${u}`), className: ms.title }),
                  t && o().createElement(ze, { text: Es.map(), className: ms.title }),
                ),
                o().createElement(
                  "div",
                  { className: ms.flareWrapper },
                  o().createElement("div", { className: ms.flare }),
                ),
                t && o().createElement("div", { className: ms.blik }),
              );
            },
          ),
          ps = "SeasonsTabs_base_24",
          As = "SeasonsTabs_base__show_61";
        function Cs() {
          return (
            (Cs =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Cs.apply(this, arguments)
          );
        }
        const hs = ({ tabs: e, isMinimised: t, onClick: u, className: a }) => {
            const n = w().mediaSize,
              s = !t && n >= B.Medium,
              i = e.every((e) => e.isFull);
            return (
              (0, r.useEffect)(() => {
                i && W(R.sounds.cust_tick_on_all());
              }, [i]),
              o().createElement(
                "div",
                { className: v()(ps, s && As, a) },
                Boolean(null == e ? void 0 : e.length) &&
                  e.map((e) =>
                    o().createElement(
                      bs,
                      Cs(
                        { key: e.season, isShowFullTabContent: s, isAllTabsFull: i, onClick: u },
                        e,
                      ),
                    ),
                  ),
              )
            );
          },
          fs = "VehicleName_base_4d",
          vs = "VehicleName_vehicleTypeContainer_1e",
          Fs = "VehicleName_base__prem_ec",
          Ds = "VehicleName_vehicleType_68",
          Bs = "VehicleName_shortName_23",
          Ss = R.images.gui.maps.icons.vehicleTypes.big,
          ys = (0, r.memo)(({ name: e, tier: t, type: u, isPremium: a = !1, classMix: n }) => {
            const r = `${((s = u), s.replace(/-/g, "_"))}${a ? "_elite" : ""}`;
            var s;
            return o().createElement(
              o().Fragment,
              null,
              o().createElement(
                "div",
                { className: v()(fs, a && Fs, n) },
                o().createElement(ze, { text: ga(t) }),
                o().createElement(
                  "div",
                  { className: vs },
                  o().createElement("div", {
                    className: Ds,
                    style: { backgroundImage: `url(${Ss.$dyn(r)})` },
                  }),
                ),
                o().createElement(ze, { text: e, className: Bs }),
              ),
              o().createElement("div", null),
            );
          });
        var ws = u(5521);
        const ks = (e) => {
            console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
          },
          Ts = "INPUT_KEY_STATE";
        var Ns;
        !(function (e) {
          ((e.Idle = "IDLE"), (e.Pressed = "PRESSED"), (e.Released = "RELEASED"));
        })(Ns || (Ns = {}));
        function Is(e) {
          localStorage.setItem(Ts, JSON.stringify(e));
        }
        function Ms(e = ws.n.NONE, t = ks, u = !1, a, n = 300) {
          const o = (0, r.useRef)(0);
          (0, r.useEffect)(() => {
            if (e !== ws.n.NONE)
              return (
                window.addEventListener("keydown", r, { capture: u }),
                window.addEventListener("keyup", s, { capture: u }),
                () => {
                  (window.removeEventListener("keydown", r, { capture: u }),
                    window.removeEventListener("keyup", s, { capture: u }));
                }
              );
            function r(a) {
              if (a.keyCode !== e) return;
              if (a.repeat) return;
              if (i.O.view.isEventHandled()) return;
              i.O.view.setEventHandled();
              (
                (function () {
                  const e = localStorage.getItem(Ts);
                  return e ? JSON.parse(e) : null;
                })() || { state: Ns.Idle, pressTime: 0 }
              ).state === Ns.Released
                ? (t(a), u && a.stopPropagation(), Is({ state: Ns.Idle, pressTime: 0 }))
                : (Is({ state: Ns.Pressed, pressTime: performance.now() }),
                  (o.current = performance.now()));
            }
            function s(t) {
              if ((localStorage.setItem(X_, "0"), t.keyCode !== e)) return;
              const u = performance.now(),
                r = u - (o.current || u);
              o.current = 0;
              (a && a(r, r >= n, t), Is({ state: Ns.Released, pressTime: 0 }));
            }
          }, [t, e, u, a, n]);
        }
        const xs = "App_base_f6",
          Os = "App_base__expanded_2a",
          Ls = "App_wrapper_5c",
          Rs = "App_header_17",
          Ps = "App_header__hide_c5",
          Hs = "App_infoButton_db",
          Ws = "App_base__fadeIn_54",
          zs = "App_base__fadeOut_33",
          Us = "App_closeButton_7c",
          Gs = "App_description_d6",
          Vs = "App_description__bonus_a0",
          js = "App_topPanelWrapper_50",
          $s = "App_topPanel_29",
          Xs = "App_carouselBlock_24",
          qs = "App_carouselBlockBack_d6",
          Ys = "App_markers_2a",
          Ks = "App_markers__fadeIn_94",
          Zs = "App_markers__fadeOut_e3",
          Js = "App_emptyState_2f",
          Qs = "App_entryPoint_ac",
          ei = "App_decalsBanner_75",
          ti = "App_decalsBanner__hide_98",
          ui = "App_decalsBanner__fadeIn_92",
          ai = "App_decalsBanner__fadeOut_38",
          ni = "App_openPanelButton_55",
          ri = "App_openPanelButtonText_6f",
          oi = "App_leftPanel_85",
          si = "App_rightPanel_fb",
          ii = "App_divider_8c",
          li = "App_seasontTabs_50",
          ci = "App_seasontTabs__fadeIn_3a",
          _i = "App_seasontTabs__fadeOut_a6",
          di = "App_magneticTool_4d",
          mi = "App_inscription_3e",
          Ei = "App_toolbarWrapper_55",
          gi = "App_progressionWrapper_19",
          bi = "App_withProgressionWrapper_cb",
          pi = "App_seasonsHint_6d",
          Ai = "App_sub_7b",
          Ci = "App_sub__open_1c",
          hi = "App_footer_b1",
          fi = "App_footer__hide_ce",
          vi = "App_binCartPannelWrapper_8c",
          Fi = "App_binCartPannelWrapper__open_3f",
          Di = "App_binCartPannel_b1",
          Bi = "App_cart_25",
          Si = "App_subInfo_18",
          yi = "App_subInfo__open_b7",
          wi = "App_back_ff",
          ki = "App_buttonHolder_58";
        function Ti(e, t, u = []) {
          const a = (0, r.useRef)(0),
            n = (0, r.useCallback)(() => window.clearInterval(a.current), u || []);
          (0, r.useEffect)(() => n, [n]);
          const o = (null != u ? u : []).concat([t]);
          return [
            (0, r.useCallback)((u) => {
              ((a.current = window.setInterval(() => e(u, !0), t)), e(u, !1));
            }, o),
            n,
          ];
        }
        const Ni = "HorizontalBar_base_49",
          Ii = "HorizontalBar_base__nonActive_82",
          Mi = "HorizontalBar_leftButton_5f",
          xi = "HorizontalBar_rightButton_03",
          Oi = "HorizontalBar_track_0d",
          Li = "HorizontalBar_thumb_fd",
          Ri = "HorizontalBar_rail_32",
          Pi = "disable",
          Hi = { pending: !1, offset: 0 },
          Wi = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          zi = () => {},
          Ui = (e, t) => Math.max(20, e.offsetWidth * t),
          Gi = (0, r.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = Wi, onDrag: a = zi }) => {
              const n = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, r.useState)(Hi),
                m = d[0],
                E = d[1],
                g = (0, r.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        a({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [a],
                ),
                b = () => {
                  const t = l.current,
                    u = c.current,
                    a = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(a && t && u && n)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, a / n),
                    _ = X(0, 1, r / (n - a)),
                    d = (t.offsetWidth - Ui(t, o)) * _;
                  ((u.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (s.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (s.current.classList.add(Pi), void i.current.classList.remove(Pi));
                        if (
                          ((t = l.current),
                          (u = c.current),
                          e - (t.offsetWidth - u.offsetWidth) >= -0.5)
                        )
                          return (s.current.classList.remove(Pi), void i.current.classList.add(Pi));
                        var t, u;
                        (s.current.classList.remove(Pi), i.current.classList.remove(Pi));
                      }
                    })(d));
                },
                p = J(() => {
                  ((() => {
                    const t = c.current,
                      u = l.current,
                      a = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && a && u)) return;
                    const o = Math.min(1, a / r);
                    ((t.style.width = `${Ui(u, o)}px`),
                      (t.style.display = "flex"),
                      n.current &&
                        (1 === o ? n.current.classList.add(Ii) : n.current.classList.remove(Ii)));
                  })(),
                    b());
                });
              ((0, r.useEffect)(() => q(p)),
                (0, r.useEffect)(
                  () =>
                    q(() => {
                      const t = () => {
                        b();
                      };
                      let u = zi;
                      const a = () => {
                        (u(), (u = q(p)));
                      };
                      return (
                        e.events.on("recalculateContent", p),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", a),
                        () => {
                          (u(),
                            e.events.off("recalculateContent", p),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", a));
                        }
                      );
                    }),
                  [e],
                ),
                (0, r.useEffect)(() => {
                  if (!m.pending) return;
                  const t = (t) => {
                      var u;
                      const n = e.contentRef.current;
                      if (!n) return;
                      const r = l.current,
                        o = c.current;
                      if (!n || !r || !o) return;
                      const s = t.screenX - m.offset - r.getBoundingClientRect().x,
                        i = (s / r.offsetWidth) * (null != (u = e.getContainerSize()) ? u : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(n, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        a({ type: "dragging", thumb: o, thumbOffset: s, contentOffset: i }));
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), g(Hi));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, m.offset, m.pending, a, g]));
              const A = Ti((t) => e.applyStepTo(t), _, [e]),
                C = A[0],
                h = A[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const f = (e) => {
                e.target.classList.contains(Pi) || W("highlight");
              };
              return o().createElement(
                "div",
                { className: v()(Ni, t.base), ref: n, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: v()(Mi, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Pi) || 0 !== e.button || (W("play"), C(te.Next));
                  },
                  onMouseUp: h,
                  ref: s,
                  onMouseEnter: f,
                }),
                o().createElement(
                  "div",
                  {
                    className: v()(Oi, t.track),
                    onMouseDown: (t) => {
                      const a = c.current;
                      if (a && 0 === t.button)
                        if ((W("play"), t.target === a))
                          g({ pending: !0, offset: t.screenX - a.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const a = c.current,
                              n = e.contentRef.current;
                            if (!a || !n) return;
                            const r = u(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * t);
                          })(t.screenX > a.getBoundingClientRect().x ? te.Prev : te.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: f,
                  },
                  o().createElement("div", { ref: c, className: v()(Li, t.thumb) }),
                  o().createElement("div", { className: v()(Ri, t.rail) }),
                ),
                o().createElement("div", {
                  className: v()(xi, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Pi) || 0 !== e.button || (W("play"), C(te.Prev));
                  },
                  onMouseUp: h,
                  ref: i,
                  onMouseEnter: f,
                }),
              );
            },
          ),
          Vi = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          ji = ({
            children: e,
            api: t,
            className: u,
            barClassNames: a,
            areaClassName: n,
            classNames: s,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, r.useMemo)(() => {
                const e = a || {};
                return Object.assign({}, e, { base: v()(Vi.base, e.base) });
              }, [a]),
              d = (0, r.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: v()(Vi.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: v()(Vi.defaultScrollArea, n) },
                o().createElement($i, { className: i, api: d, classNames: s }, e),
              ),
              o().createElement(Gi, { getStepByRailClick: l, api: t, onDrag: c, classNames: _ }),
            );
          },
          $i = ({ api: e, className: t, classNames: u, children: a, style: n }) => (
            (0, r.useEffect)(() => q(e.recalculateContent)),
            o().createElement(
              "div",
              { className: v()(Vi.base, t), style: n },
              o().createElement(
                "div",
                {
                  className: v()(Vi.wrapper, null == u ? void 0 : u.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: v()(Vi.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  a,
                ),
              ),
            )
          );
        (($i.Bar = Gi),
          ($i.Default = ji),
          ($i.SeniorityAwards = ({ api: e, className: t, classNames: u, children: a }) => (
            (0, r.useEffect)(() => q(e.recalculateContent)),
            o().createElement(
              "div",
              { className: v()(Vi.base, t) },
              o().createElement(
                "div",
                { className: v()(Vi.wrapper, null == u ? void 0 : u.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: v()(Vi.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  a,
                ),
              ),
            )
          )));
        const Xi = ae({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? te.Next : te.Prev),
          }),
          qi = "VerticalBar_base_f3",
          Yi = "VerticalBar_base__nonActive_42",
          Ki = "VerticalBar_topButton_d7",
          Zi = "VerticalBar_bottomButton_06",
          Ji = "VerticalBar_track_df",
          Qi = "VerticalBar_thumb_32",
          el = "VerticalBar_rail_43",
          tl = "disable",
          ul = () => {},
          al = { pending: !1, offset: 0 },
          nl = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          rl = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          ol = (e, t) => Math.max(20, e.offsetHeight * t),
          sl = (0, r.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = nl, onDrag: a = ul }) => {
              const n = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, r.useState)(al),
                m = d[0],
                E = d[1],
                g = (0, r.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        a({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [a],
                ),
                b = J(() => {
                  const t = c.current,
                    u = l.current,
                    a = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(a && r && t && u)) return;
                  const o = Math.min(1, a / r);
                  return (
                    (t.style.height = `${ol(u, o)}px`),
                    t.classList.add(Qi),
                    n.current &&
                      (1 === o ? n.current.classList.add(Yi) : n.current.classList.remove(Yi)),
                    o
                  );
                }),
                p = J(() => {
                  const t = l.current,
                    u = c.current,
                    a = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(a && t && u && n)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, a / n),
                    _ = X(0, 1, r / (n - a)),
                    d = (t.offsetHeight - ol(t, o)) * _;
                  ((u.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (s.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (s.current.classList.add(tl), void i.current.classList.remove(tl));
                        if (
                          ((t = l.current),
                          (u = c.current),
                          e - (t.offsetHeight - u.offsetHeight) >= -0.5)
                        )
                          return (s.current.classList.remove(tl), void i.current.classList.add(tl));
                        var t, u;
                        (s.current.classList.remove(tl), i.current.classList.remove(tl));
                      }
                    })(d));
                }),
                A = J(() => {
                  rl(e, () => {
                    (b(), p());
                  });
                });
              ((0, r.useEffect)(() => q(A)),
                (0, r.useEffect)(() => {
                  const t = () => {
                    rl(e, () => {
                      p();
                    });
                  };
                  let u = ul;
                  const a = () => {
                    (u(), (u = q(A)));
                  };
                  return (
                    e.events.on("recalculateContent", A),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", a),
                    () => {
                      (u(),
                        e.events.off("recalculateContent", A),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", a));
                    }
                  );
                }, [e]),
                (0, r.useEffect)(() => {
                  if (!m.pending) return;
                  const t = (t) => {
                      rl(e, (u) => {
                        const n = l.current,
                          r = c.current,
                          o = e.getContainerSize();
                        if (!n || !r || !o) return;
                        const s = t.screenY - m.offset - n.getBoundingClientRect().y,
                          i = (s / n.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(u, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: u.scrollTop },
                        }),
                          a({ type: "dragging", thumb: r, thumbOffset: s, contentOffset: i }));
                      });
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        g(al));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, m.offset, m.pending, a, g]));
              const C = Ti((t) => e.applyStepTo(t), _, [e]),
                h = C[0],
                f = C[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", f, !0),
                  () => document.removeEventListener("mouseup", f, !0)
                ),
                [f],
              );
              const F = (e) => {
                e.target.classList.contains(tl) || W("highlight");
              };
              return o().createElement(
                "div",
                { className: v()(qi, t.base), ref: n, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: v()(Ki, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(tl) || 0 !== e.button || (W("play"), h(te.Next));
                  },
                  ref: s,
                  onMouseEnter: F,
                }),
                o().createElement(
                  "div",
                  {
                    className: v()(Ji, t.track),
                    onMouseDown: (t) => {
                      const a = c.current;
                      if (a && 0 === t.button)
                        if ((W("play"), t.target === a))
                          (e.handleIsThumbDragging(!0),
                            g({ pending: !0, offset: t.screenY - a.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              rl(e, (a) => {
                                if (!a) return;
                                const n = u(e),
                                  r = e.clampPosition(a, a.scrollTop + n * t);
                                e.applyScroll(r);
                              });
                          })(t.screenY > a.getBoundingClientRect().y ? te.Prev : te.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: F,
                  },
                  o().createElement("div", { ref: c, className: t.thumb }),
                  o().createElement("div", { className: v()(el, t.rail) }),
                ),
                o().createElement("div", {
                  className: v()(Zi, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(tl) || 0 !== e.button || (W("play"), h(te.Prev));
                  },
                  onMouseUp: f,
                  ref: i,
                  onMouseEnter: F,
                }),
              );
            },
          ),
          il = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          ll = ({
            children: e,
            api: t,
            className: u,
            barClassNames: a,
            areaClassName: n,
            scrollClassName: s,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, r.useMemo)(() => {
                const e = a || {};
                return Object.assign({}, e, { base: v()(il.base, e.base) });
              }, [a]),
              d = (0, r.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: v()(il.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: v()(il.area, n) },
                o().createElement(cl, { className: s, classNames: i, api: d }, e),
              ),
              o().createElement(sl, { getStepByRailClick: l, api: t, onDrag: c, classNames: _ }),
            );
          },
          cl = ({ className: e, classNames: t, children: u, api: a }) => (
            (0, r.useEffect)(() => q(a.recalculateContent)),
            o().createElement(
              "div",
              { className: v()(il.base, e), ref: a.wrapperRef, onWheel: a.handleMouseWheel },
              o().createElement(
                "div",
                { className: v()(il.content, null == t ? void 0 : t.content), ref: a.contentRef },
                u,
              ),
            )
          );
        cl.Default = ll;
        const _l = { Vertical: n, Horizontal: a },
          dl = { type: "idle" };
        const ml = (e, t) => {
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
          El = "ArrowsHint_base_3c",
          gl = "ArrowsHint_content_ac",
          bl = "ArrowsHint_notificationBg_ef",
          pl = "ArrowsHint_arrows_7c",
          Al = "ArrowsHint_bg_e0",
          Cl = "ArrowsHint_arrow_41",
          hl = "ArrowsHint_arrow__left_9c",
          fl = "ArrowsHint_arrow__right_50",
          vl = "ArrowsHint_text_a2",
          Fl = () =>
            o().createElement(
              "div",
              { className: El },
              o().createElement("div", { className: Al }),
              o().createElement(
                "div",
                { className: gl },
                o().createElement("div", { className: bl }),
                o().createElement(ze, {
                  className: vl,
                  text: R.strings.customization.arrowHint.text(),
                }),
                o().createElement(
                  "div",
                  { className: pl },
                  o().createElement("div", { className: v()(Cl, hl) }),
                  o().createElement("div", { className: v()(Cl, fl) }),
                ),
              ),
            ),
          Dl = ({
            children: e,
            contentID: t,
            decoratorID: u = 0,
            targetId: a = 0,
            args: n,
            isEnabled: o = !0,
            onMouseDown: s,
          }) => {
            const i = (0, r.useCallback)(() => {
                ((0, $e.c9)($e.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: a,
                  isMouseEvent: !0,
                  on: !0,
                  args: n,
                }),
                  z.playYes());
              }, [n, t, u, a]),
              l = (0, r.useCallback)(() => {
                (0, $e.c9)($e.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: a,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, u, a]),
              c = (0, r.useCallback)(
                (e) => {
                  (s && s(e), ((e) => e.button === yt.RIGHT)(e) && i());
                },
                [s, i],
              );
            return (
              (0, r.useEffect)(() => {
                !1 === o && l();
              }, [o, l]),
              o ? (0, r.cloneElement)(e, { onMouseDown: c }) : e
            );
          },
          Bl = ["children"];
        function Sl() {
          return (
            (Sl =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Sl.apply(this, arguments)
          );
        }
        const yl = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Bl);
            return o().createElement(
              Dl,
              Sl({}, u, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          wl = "Image_base_5c",
          kl = "Image_shine_08",
          Tl = "Image_content_03",
          Nl = (0, r.memo)(({ isDim: e, icon: t }) => {
            const u = (0, r.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]);
            return t
              ? o().createElement(
                  "span",
                  { className: wl },
                  e && o().createElement("span", { className: kl }),
                  o().createElement("span", { className: Tl, style: u }),
                )
              : o().createElement("span", { className: Tl });
          }),
          Il = "Price_base_9e",
          Ml = "Price_base__stock_cc",
          xl = "Price_storage_04",
          Ol = "Price_storage__empty_2d",
          Ll = "Price_icon_df",
          Rl = "Price_iconRent_ec",
          Pl = "Price_iconRent__autoRent_df",
          Hl = "Price_rental_5a",
          Wl = "Price_iconLocked_07",
          zl = R.strings.customization,
          Ul = (0, r.memo)(
            ({
              locked: e,
              hasDiscount: t,
              isRental: u,
              autoRentEnabled: a,
              rentalInfoText: n,
              isStub: r,
              price: s,
              quantity: i,
              isFromStorage: l = !0,
              classMix: c,
            }) => {
              var _, d;
              if (r) return null;
              const m = v()(Rl, a && Pl);
              if (e)
                return o().createElement(
                  "span",
                  { className: v()(Il, c) },
                  o().createElement(
                    "span",
                    { className: Ll },
                    o().createElement("span", { className: Wl }),
                  ),
                );
              if (u && i > 0)
                return o().createElement(
                  "span",
                  { className: v()(Il, c) },
                  o().createElement(
                    "span",
                    { className: Ll },
                    o().createElement("span", { className: m }),
                  ),
                  i,
                );
              if (l && (0 === s.length || i > 0))
                return o().createElement(
                  "span",
                  { className: v()(Il, c) },
                  o().createElement("span", { className: v()(xl, !i && Ol) }, i),
                );
              const E = v()(Il, t && Ml, c);
              return o().createElement(
                "div",
                { className: E },
                "" !== n && o().createElement(ze, { className: Hl, text: n }),
                Boolean(i && i > 1) &&
                  o().createElement(ze, {
                    text: zl.cart.quantity(),
                    format: { binding: { quantity: i } },
                  }),
                o().createElement(zt, {
                  isDiscount: t,
                  size: Ot.small,
                  type: null == (_ = s[0]) ? void 0 : _.name,
                  value: Number(null == (d = s[0]) ? void 0 : d.value),
                }),
              );
            },
          ),
          Gl = "ProgressionLevelIcon_base_8a",
          Vl = "ProgressionLevelIcon_icon_49",
          jl = "ProgressionLevelIcon_icon__big_74",
          $l = "ProgressionLevelIcon_icon__small_46",
          Xl = ({ typeId: e, progressionLevel: t, classMix: u }) => {
            const a = `level_${t}`,
              n =
                36 === e
                  ? R.images.gui.maps.icons.customization.progression_icons
                  : R.images.gui.maps.icons.customization.progression_styles.icons,
              s = n.$dyn(a),
              i = n.$dyn(a.concat("_small")),
              l = (0, r.useMemo)(() => ({ backgroundImage: `url(${i})` }), [i]),
              c = (0, r.useMemo)(() => ({ backgroundImage: `url(${s})` }), [s]);
            return s && i
              ? o().createElement(
                  "div",
                  { className: Gl },
                  o().createElement("div", { className: v()(Vl, $l, u), style: l }),
                  o().createElement("div", { className: v()(Vl, jl, u), style: c }),
                )
              : null;
          },
          ql = "Slot_base_25",
          Yl = "Slot_base__big_e2",
          Kl = "Slot_base__isProgression_0b",
          Zl = "Slot_base__locked_4d",
          Jl = "Slot_base__isAlreadyUsed_dd",
          Ql = "Slot_base__selected_03",
          ec = "Slot_equippedIcon_0d",
          tc = "Slot_pulse_3a",
          uc = "Slot_image_c9",
          ac = "Slot_inProgressIcon_8a",
          nc = "Slot_progressionArrow_74",
          rc = "Slot_progressionArrow__enabled_25",
          oc = "Slot_shadowBottom_96",
          sc = "Slot_base__hasExtraName_55",
          ic = "Slot_shadowTop_11",
          lc = "Slot_base__topLeftCornerVisible_f9",
          cc = "Slot_border_74",
          _c = "Slot_base__equipped_be",
          dc = "Slot_topLeftCorner_b3",
          mc = "Slot_ribbon_f5",
          Ec = "Slot_isLocked_bb",
          gc = "Slot_isAlreadyUsed_1a",
          bc = "Slot_isAlreadyUsedText_50",
          pc = "Slot_isAlreadyUsedIcon_6a",
          Ac = "Slot_icon_fc",
          Cc = "Slot_icon__editable_69",
          hc = "Slot_icon__rewindable_fd",
          fc = "Slot_icon__special_50",
          vc = "Slot_icon__alert_6d",
          Fc = "Slot_icon__unHistorical_64",
          Dc = "Slot_icon__fantastical_3a",
          Bc = "Slot_icon__serialNumber_26",
          Sc = "Slot_hover_7b",
          yc = "Slot_price_d1",
          wc = "Slot_styleName_c6",
          kc = "Slot_button_a6",
          Tc = "Slot_buttonWrapper_ac",
          Nc = "Slot_bubble_cc",
          Ic = "Slot_bubble__placeButton_28",
          Mc = R.strings.customization,
          xc = (0, r.memo)(
            ({
              intCD: e,
              typeId: t,
              locked: u,
              soundHover: a = R.sounds.highlight(),
              soundClick: n = R.sounds.cust_select(),
              isSelected: s,
              customizationDisplayType: i,
              tooltip: l,
              isSpecial: c,
              showAlert: _,
              isDim: d,
              icon: m,
              isWide: E,
              quantity: g,
              buyPrice: b,
              extraName: p,
              classMix: A,
              progressionLevel: C,
              isProgressionRewindEnabled: h,
              editableIcon: f,
              onSelectItem: F,
              isEquipped: D,
              editBtnEnabled: S,
              onEditItem: y,
              isRental: k,
              rentalInfoText: T,
              autoRentEnabled: N,
              isWithSerialNumber: I,
              isMainType: M,
              isAlreadyUsed: x,
              noveltyCounter: O,
              editNoveltyCounter: L,
              onHoverItem: P,
              isInProgress: H,
              arrowEnabled: z,
              isNew: U,
              isFilled: j,
            }) => {
              var X;
              const q = (0, r.useMemo)(() => -1 === e, [e]),
                Y = (0, r.useMemo)(() => !u, [u]),
                K = w().mediaSize,
                Z = f.includes("disable") ? null : f,
                J = 1 === i,
                Q = 2 === i,
                ee = _ || c || I || i || Z,
                te = (0, r.useCallback)(() => {
                  (e && P(e), Y && a && !s && W(a));
                }, [P, e, Y, a, s]),
                ue = (0, r.useCallback)(() => {
                  (C <= 0 && (u || x)) || (F && (e && F(e), W(n)));
                }, [e, x, u, F, C, n]),
                ae = (0, r.useCallback)(
                  (t) => {
                    (t.stopPropagation(), y && !u && e && y(e));
                  },
                  [e, u, y],
                ),
                ne = v()(
                  ql,
                  A,
                  E && Yl,
                  s && Ql,
                  D && _c,
                  C > 0 && Kl,
                  ee && lc,
                  p && sc,
                  u && Zl,
                  x && Jl,
                ),
                re = (0, r.useMemo)(
                  () => ({ intCD: e, tooltip: l, showInventoryBlock: !u, progressionLevel: C }),
                  [e, u, C, l],
                ),
                oe = (0, r.useMemo)(
                  () => ({
                    tooltip: J
                      ? "techCustomizationNonhistoricItem"
                      : "techCustomizationFantasticalItem",
                  }),
                  [J],
                ),
                se = Boolean(null == (X = b.discount[0]) ? void 0 : X.value);
              return j
                ? o().createElement(
                    yl,
                    { key: e, isEnabled: !q, args: { type: "customizationItem", intCD: e } },
                    o().createElement(
                      Uu,
                      { args: re },
                      o().createElement(
                        "div",
                        { className: ne, onMouseEnter: te, onClick: ue },
                        U && o().createElement("div", { className: tc }),
                        D && o().createElement("div", { className: ec }),
                        o().createElement(
                          "div",
                          { className: cc },
                          void 0 !== z && o().createElement("div", { className: v()(nc, z && rc) }),
                          H && o().createElement("div", { className: ac }),
                          o().createElement(
                            "div",
                            { className: uc },
                            o().createElement(Nl, { isDim: d, icon: m }),
                          ),
                          o().createElement("div", { className: ic }),
                          o().createElement("div", { className: oc }),
                          u && o().createElement("div", { className: Ec }),
                          x &&
                            o().createElement(
                              "div",
                              { className: gc },
                              o().createElement(
                                "div",
                                { className: bc },
                                o().createElement("div", { className: pc }),
                                E &&
                                  o().createElement(ze, {
                                    text: Mc.customization.carousel.is_already_used(),
                                  }),
                              ),
                            ),
                          Boolean(O) &&
                            o().createElement(ze, { className: Nc, text: O.toString() }),
                          M && o().createElement("div", { className: mc }),
                          o().createElement(
                            "div",
                            { className: dc },
                            _ && o().createElement("div", { className: v()(Ac, vc) }),
                            c && o().createElement("div", { className: v()(Ac, fc) }),
                            I && o().createElement("div", { className: v()(Ac, Bc) }),
                            (J || Q) &&
                              !q &&
                              o().createElement(
                                Uu,
                                { args: oe },
                                o().createElement("div", { className: v()(Ac, J ? Fc : Dc) }),
                              ),
                            Z &&
                              o().createElement("div", {
                                className: v()(Ac, Cc),
                                style: {
                                  backgroundImage: `url(${(() => {
                                    if (Z) return K <= B.Small ? Z : Z.replace("small", "big");
                                  })()})`,
                                },
                              }),
                            h
                              ? o().createElement("div", { className: v()(Ac, hc) })
                              : o().createElement(Xl, {
                                  typeId: t,
                                  progressionLevel: C,
                                  classMix: Ac,
                                }),
                          ),
                          o().createElement(ze, { className: wc, text: p }),
                          o().createElement(Ul, {
                            classMix: yc,
                            isStub: q,
                            price: b.price,
                            quantity: g,
                            isRental: k,
                            rentalInfoText: T,
                            autoRentEnabled: N,
                            locked: u,
                            hasDiscount: se,
                          }),
                          o().createElement("div", { className: Sc }),
                          Boolean(f) &&
                            D &&
                            o().createElement(
                              et,
                              {
                                body: S
                                  ? Mc.customization.changeButton.tooltip()
                                  : Mc.customization.changeButtonDisabled.tooltip(),
                              },
                              o().createElement(
                                "div",
                                { id: `${e}-tooltip`, className: Tc },
                                o().createElement(
                                  $,
                                  {
                                    size: V.small,
                                    type: S ? G.primary : G.secondary,
                                    disabled: !S,
                                    mixClass: kc,
                                    onClick: ae,
                                  },
                                  Boolean(L) &&
                                    o().createElement(ze, {
                                      className: v()(Nc, Ic),
                                      text: L.toString(),
                                    }),
                                  K >= B.Small
                                    ? o().createElement(ze, {
                                        text: Mc.customization.carousel.change_button(),
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
                    { className: v()(ql, E && Yl), onMouseEnter: te, onClick: ue },
                    o().createElement("div", { className: cc }),
                  );
            },
          ),
          Oc = "Slots_base_ef",
          Lc = "Slots_categories_6b",
          Rc = "Slots_categorieBox_d3",
          Pc = "Slots_categorieText_12",
          Hc = "Slots_categorieBoxPattern_8d",
          Wc = "Slots_slot_17";
        function zc() {
          return (
            (zc =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            zc.apply(this, arguments)
          );
        }
        const Uc = (0, r.memo)(
          ({
            items: e,
            arrowsList: t,
            categories: u,
            onClick: a,
            onHoverItem: n,
            onEditClick: r,
            isEditable: s,
            categoriesRef: i,
            itemsRef: l,
          }) =>
            o().createElement(
              "div",
              { className: Oc },
              u.map((c, _) => {
                var d;
                return o().createElement(
                  "div",
                  { className: Lc, key: `${_}` },
                  "" !== c.bookmarkName &&
                    o().createElement(
                      "div",
                      {
                        className: Rc,
                        ref: (e) => {
                          e ? i.current.set(c.bookmarkIndex, e) : i.current.delete(c.bookmarkIndex);
                        },
                      },
                      o().createElement("div", { className: Hc }),
                      o().createElement("div", { className: Pc }, c.bookmarkName),
                    ),
                  e
                    .slice(c.bookmarkIndex, null == (d = u[_ + 1]) ? void 0 : d.bookmarkIndex)
                    .map((e, u) => {
                      const i = t.find((e) => e.arrowIndex === u);
                      return o().createElement(
                        "div",
                        {
                          key: `${_}_${u}`,
                          ref: (t) => {
                            t ? l.current.set(e.intCD, t) : l.current.delete(e.intCD);
                          },
                          "data-magnetic-tool-support": !0,
                        },
                        o().createElement(
                          xc,
                          zc(
                            {
                              onSelectItem: a,
                              onHoverItem: n,
                              onEditItem: r,
                              classMix: Wc,
                              arrowEnabled: null == i ? void 0 : i.isEnabled,
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
        let Gc;
        !(function (e) {
          ((e.auto = "auto"), (e.left = "left"), (e.right = "right"));
        })(Gc || (Gc = {}));
        const Vc = {
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
          jc = "right",
          $c = "left",
          Xc = (e) => e.offsetLeft - 0.5 * e.offsetWidth,
          qc = (e, t) => e.offsetLeft - t + 1.5 * e.offsetWidth,
          Yc = R.strings.customization,
          Kc = { allowedButtons: [yt.LEFT] },
          Zc = (0, r.memo)(
            (0, r.forwardRef)(
              (
                {
                  items: e,
                  arrowsList: t,
                  categories: u,
                  onClick: a,
                  onHoverItem: n,
                  onEditClick: s,
                  scrollApi: l,
                  onArrowClick: c,
                  isCarouselArrowsHintVisible: _,
                  scrollStartItemId: d,
                  selectedItemId: m,
                  firstExpandedItemId: E,
                  tabId: g,
                  lastScrollState: b,
                  isEditable: p,
                  onUpdateItems: A,
                },
                C,
              ) => {
                const h = w().mediaSize,
                  f = (0, r.useRef)(new Map()),
                  F = (0, r.useRef)(new Map()),
                  D = (0, r.useMemo)(() => e.filter((e) => e.isEquipped), [e]),
                  S = (0, r.useState)(0),
                  y = S[0],
                  k = S[1],
                  T = (0, r.useState)(!1),
                  N = T[0],
                  I = T[1],
                  M = (0, r.useState)(!1),
                  x = M[0],
                  O = M[1],
                  L = (0, r.useState)(!1),
                  R = L[0],
                  P = L[1],
                  H = (0, r.useState)(!1),
                  W = H[0],
                  U = H[1],
                  G = (0, r.useState)([]),
                  V = G[0],
                  j = G[1],
                  $ = (0, r.useState)(!1),
                  X = $[0],
                  q = $[1],
                  Y = (0, r.useState)([0, 0]),
                  K = Y[0],
                  Z = Y[1];
                (0, r.useImperativeHandle)(C, () => ({
                  getFirstVisibleItemId: () => {
                    const t = e.find((e) => {
                      const t = f.current.get(e.intCD);
                      return t && t.getBoundingClientRect().left > 0;
                    });
                    return t ? t.intCD : -1;
                  },
                }));
                const J = { left: K[0], right: K[1] },
                  Q = J.right <= 0 && J.left <= 0,
                  ee = (function (e, t, u) {
                    const a = e.contentRef,
                      n = e.wrapperRef,
                      o = e.scrollPosition,
                      s = e.clampPosition,
                      l = e.animationScroll,
                      c = e.events,
                      _ = (0, r.useState)(dl),
                      d = _[0],
                      m = _[1];
                    return (
                      (0, r.useEffect)(() => {
                        const e = a.current;
                        e && (e.style.cursor = "dragging" === d.type ? "move" : "grab");
                      }, [a, d.type]),
                      (0, r.useEffect)(() => {
                        if ("dragging" !== d.type) return;
                        const e = i.O.client.events.mouse.move(([e, u]) => {
                            const r = a.current,
                              i = n.current;
                            if (!r || !i) return;
                            if ("inside" === u && e.clientX < 0) return;
                            const c = "inside" === u ? e.clientX : e.clientX - i.offsetLeft,
                              _ = d.positionFrom - c,
                              m = d.previousScrollPosition + _;
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
                          u = i.O.client.events.mouse.up(function () {
                            m({ type: "scrollingToEnd" });
                          });
                        return () => {
                          (e(), u());
                        };
                      }, [l.scrollPosition, s, a, d, o, n, t]),
                      (0, r.useEffect)(() => {
                        if ("scrollingToEnd" !== d.type) return;
                        const e = () => {
                          m(dl);
                        };
                        return (
                          l.scrollPosition.idle && e(),
                          c.on("rest", e),
                          () => c.off("rest", e)
                        );
                      }, [l.scrollPosition, d.type, c]),
                      (0, r.useEffect)(() => {
                        const e = a.current;
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
                      }, [l.scrollPosition, a, u]),
                      d
                    );
                  })(l, void 0, Kc),
                  te = "dragging" === ee.type,
                  ue = (0, r.useCallback)(() => {
                    const e = l.getWrapperSize();
                    if (!e) return null;
                    let t = !1,
                      u = !1;
                    (D.forEach((a) => {
                      const n = f.current.get(a.intCD);
                      if (!n) return null;
                      const r = n.getBoundingClientRect();
                      (r.right <= 0 && (t = !0), r.left >= e && (u = !0));
                    }),
                      I(t),
                      O(u));
                  }, [D, l]),
                  ae = (e) => {
                    const t = l.getWrapperSize();
                    if (!t) return null;
                    let u = null,
                      a = 1 / 0;
                    if (
                      (D.forEach((n) => {
                        const r = f.current.get(n.intCD);
                        if (!r) return null;
                        const o = r.getBoundingClientRect(),
                          s = o.width / 2;
                        if (e === $c) {
                          if (o.right - s <= 0) {
                            const e = t - o.right;
                            e < a && ((a = e), (u = r));
                          }
                        } else if (o.left + s >= t) {
                          const e = o.left - t;
                          e < a && ((a = e), (u = r));
                        }
                      }),
                      u)
                    ) {
                      const a = u.getBoundingClientRect(),
                        n = e === $c ? u.offsetLeft - 36 : u.offsetLeft - t + a.width + 29;
                      l.scrollPosition.start({ scrollPosition: J.right < n ? J.right : n });
                    }
                  },
                  ne = (0, r.useCallback)(() => {
                    const e = l.getContainerSize();
                    if (!e) return;
                    const t = u.length > 1 && !Q;
                    if ((t !== X && q(t), !t)) return void (V.length > 0 && j([]));
                    const a = [];
                    (u.forEach((t) => {
                      const u = F.current.get(t.bookmarkIndex);
                      if (u) {
                        let n = (u.offsetLeft + u.offsetWidth / 2) / e;
                        ((n = Math.max(0, Math.min(1, n))),
                          a.push({ name: t.bookmarkName, position: n, index: t.bookmarkIndex }));
                      }
                    }),
                      JSON.stringify(a) !== JSON.stringify(V) && j(a));
                  }, [V, u, Q, l, X]),
                  re = (0, r.useCallback)(
                    (e) => {
                      const t = e.which;
                      (t === ws.n.ARROW_LEFT && c(!0), t === ws.n.ARROW_RIGHT && c(!1));
                    },
                    [c],
                  );
                (0, r.useEffect)(
                  () => (
                    window.addEventListener("keydown", re),
                    () => window.removeEventListener("keydown", re)
                  ),
                  [re],
                );
                const oe = (0, r.useCallback)(() => {
                    const e = l.animationScroll.scrollPosition.goal;
                    k(e);
                    const t = l.getBounds(),
                      u = t[0],
                      a = t[1];
                    (u === J.left && a === J.right) || Z([u, a]);
                  }, [l, J.left, J.right]),
                  se = (0, r.useCallback)(
                    (t) => {
                      const u = e[t],
                        a = f.current.get(u.intCD);
                      if (a) return { position: a.offsetLeft, isFilled: u.isFilled };
                    },
                    [e],
                  ),
                  ie = (0, r.useCallback)(() => {
                    const t = l.getWrapperSize();
                    if (t) {
                      const u = l.animationScroll.scrollPosition.goal;
                      A(u, t, e.length, se);
                    }
                  }, [l, e, A, se]),
                  le = (0, r.useCallback)(() => {
                    (oe(), ne(), ue(), ie());
                  }, [ue, oe, ne, ie]);
                (0, r.useEffect)(
                  () => (
                    l.events.on("change", le),
                    l.events.on("recalculateContent", le),
                    l.events.on("resizeHandled", le),
                    () => {
                      (l.events.off("change", le),
                        l.events.off("recalculateContent", le),
                        l.events.off("resizeHandled", le));
                    }
                  ),
                  [le, l.events],
                );
                const ce = (0, r.useCallback)(
                    (e, t = !0, u = Gc.auto) => {
                      const a = l.getBounds(),
                        n = a[0],
                        r = a[1];
                      if (!((n <= 0 && r <= 0) || void 0 === e))
                        if (e > 0) {
                          const a = l.getWrapperSize(),
                            n = f.current.get(e);
                          if (n && a) {
                            const e = l.animationScroll.scrollPosition.goal;
                            let r = 0,
                              o = !0;
                            if (u === Gc.left) r = Xc(n);
                            else if (u === Gc.right) r = qc(n, a);
                            else {
                              const t = n.offsetLeft - e < 0,
                                u = n.offsetLeft + n.offsetWidth - e > a;
                              t || u ? (t ? (r = Xc(n)) : u && (r = qc(n, a))) : (o = !1);
                            }
                            o &&
                              l.scrollPosition.start({ scrollPosition: r, immediate: t, reset: t });
                          }
                        } else l.applyScroll(0, { immediate: !0, reset: !0 });
                    },
                    [l],
                  ),
                  _e = l.getContainerSize(),
                  de = l.getWrapperSize();
                ml(() => {
                  if (de && _e && b.current)
                    return b.current.firstExpandedItemId !== E
                      ? ((b.current.firstExpandedItemId = E), void (E && ce(E, !0, Gc.left)))
                      : b.current.selectedItemId !== m
                        ? ((b.current.selectedItemId = m), void (m && ce(m, !1, Gc.auto)))
                        : b.current.tabId !== g
                          ? ((b.current.tabId = g), void ce(d, !0, Gc.left))
                          : void 0;
                }, [ce, m, E, d, g, _e, de, b]);
                const me = v()(
                    Vc.shadow,
                    Vc.shadow__left,
                    (y === J.left || Q) && Vc.shadow__hidden,
                  ),
                  Ee = v()(Vc.shadow, Vc.shadow__right, (y === J.right || Q) && Vc.shadow__hidden),
                  ge = v()(
                    Vc.arrow,
                    Vc.arrow__left,
                    R && Vc.arrow__hover,
                    (!N || Q) && Vc.arrow__hidden,
                  ),
                  be = v()(
                    Vc.arrow,
                    Vc.arrow__right,
                    W && Vc.arrow__hover,
                    (!x || Q) && Vc.arrow__hidden,
                  ),
                  pe = () => {
                    z.playHighlight();
                  };
                return o().createElement(
                  "div",
                  { className: v()(Vc.base, te && Vc.base__dragging) },
                  _ &&
                    o().createElement(
                      "div",
                      { className: Vc.arrowsHint },
                      o().createElement(Fl, null),
                    ),
                  o().createElement(
                    _l.Horizontal.Area,
                    {
                      api: l,
                      classNames: {
                        wrapper: v()(
                          Vc.horizontalWrapper,
                          Q && Vc.horizontalWrapper__withoutScroll,
                        ),
                        content: Vc.horizontalContent,
                      },
                    },
                    o().createElement(
                      "div",
                      { className: Vc.slots },
                      o().createElement(Uc, {
                        items: e,
                        categories: u,
                        arrowsList: t,
                        onClick: a,
                        onHoverItem: n,
                        onEditClick: s,
                        isEditable: p,
                        itemsRef: f,
                        categoriesRef: F,
                      }),
                    ),
                  ),
                  o().createElement(_l.Horizontal.Bar, {
                    classNames: { base: Vc.horizontalBar, thumb: Vc.thumb },
                    api: l,
                  }),
                  X &&
                    o().createElement(
                      "div",
                      { className: Vc.bookmarksWrapper },
                      V.map(({ name: e, position: t, index: u }) =>
                        o().createElement(
                          et,
                          { key: `${e}-${u}`, body: e },
                          o().createElement("div", {
                            onMouseEnter: pe,
                            onClick: () =>
                              ((e) => {
                                const t = l.getWrapperSize(),
                                  u = l.getContainerSize();
                                if (!t || !u) return;
                                const a = F.current.get(e);
                                if (a) {
                                  z.playClick();
                                  const e = a.offsetLeft + 0.5 * a.offsetWidth,
                                    n = e / u,
                                    r = h >= B.Medium ? 36 : 29,
                                    o = e - n * (t - 2 * r) - r;
                                  l.scrollPosition.start({ scrollPosition: o });
                                }
                              })(u),
                            className: Vc.bookmark,
                            style: { left: 100 * t + "%" },
                          }),
                        ),
                      ),
                    ),
                  o().createElement("div", { className: me }),
                  o().createElement("div", { className: Ee }),
                  o().createElement(
                    et,
                    { body: Yc.tooltips.carousel.arrow() },
                    o().createElement("div", {
                      className: ge,
                      onMouseEnter: () => {
                        (P(!0), z.playHighlight());
                      },
                      onMouseLeave: () => {
                        P(!1);
                      },
                      onClick: () => {
                        ae($c);
                      },
                    }),
                  ),
                  o().createElement(
                    et,
                    { body: Yc.tooltips.carousel.arrow() },
                    o().createElement("div", {
                      className: be,
                      onMouseEnter: () => {
                        (U(!0), z.playHighlight());
                      },
                      onClick: () => {
                        ae(jc);
                      },
                      onMouseLeave: () => {
                        U(!1);
                      },
                    }),
                  ),
                );
              },
            ),
          ),
          Jc = { type: "idle" };
        const Qc = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function e_(e = ws.n.NONE, t = Qc, u = !1) {
          (0, r.useEffect)(() => {
            if (e !== ws.n.NONE)
              return (
                window.addEventListener("keydown", a, u),
                () => {
                  window.removeEventListener("keydown", a, u);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), t(a), u && a.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        const t_ = "WarningText_base_5d",
          u_ = "WarningText_header_57",
          a_ = "WarningText_headerIcon_2f",
          n_ = "WarningText_description_78",
          r_ = o().memo(({ header: e, description: t }) =>
            o().createElement(
              "div",
              { className: t_ },
              o().createElement(
                "div",
                { className: u_ },
                o().createElement("div", { className: a_ }),
                e,
              ),
              o().createElement("div", { className: n_ }, t),
            ),
          ),
          o_ = "ListEmptyState_base_5f",
          s_ = "ListEmptyState_content_22",
          i_ = "ListEmptyState_buttonWrapper_fa",
          l_ = "ListEmptyState_button_cd",
          c_ = R.strings.customization,
          __ = (0, r.memo)(
            ({
              warningHeader: e,
              warningDescription: t,
              buttonType: u = G.secondary,
              tooltipArgs: a = { body: c_.customization.resetFilter.tooltip.text() },
              className: n,
              onClick: r,
              children: s,
            }) =>
              o().createElement(
                "div",
                { className: v()(o_, n) },
                o().createElement(
                  "div",
                  { className: s_ },
                  o().createElement(r_, { header: e, description: t }),
                  s &&
                    o().createElement(
                      "div",
                      { className: i_ },
                      o().createElement(
                        et,
                        a,
                        o().createElement(
                          $,
                          { size: V.small, type: u, onClick: r, mixClass: l_ },
                          s,
                        ),
                      ),
                    ),
                ),
              ),
          ),
          d_ = {
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
        function m_() {
          return (
            (m_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            m_.apply(this, arguments)
          );
        }
        const E_ = R.strings.customization,
          g_ = (0, St.Pi)(
            ({ onCarouselCollapse: e, startScrollItemId: t, tabId: u, onUpdateItems: a }) => {
              const n = $a(),
                s = n.controls,
                l = n.model,
                c = l.computes.getItems(),
                _ = l.computes.getCategories(),
                d = l.computes.getBillModel(),
                m = w().mediaSize <= B.Small ? V.small : V.medium,
                E = l.computes.getTabsItemsList(),
                g = l.root.get(),
                b = g.filterModel,
                p = g.carouselModel,
                A = _l.Vertical.useVerticalScrollApi(),
                C = A.getWrapperSize(),
                h = A.getContainerSize(),
                f = l.computes.getBuyPrice(),
                F = (0, r.useRef)(new Map()),
                D = (0, r.useRef)(new Map()),
                S = (0, r.useState)(0),
                y = S[0],
                k = S[1],
                T = (0, r.useState)([]),
                N = T[0],
                I = T[1],
                M = (0, r.useState)(!1),
                x = M[0],
                O = M[1],
                L = (0, r.useState)([0, 0]),
                P = L[0],
                H = L[1],
                U = b.filteredItemsCounter,
                j = b.allItemsCounter,
                X = b.isFilteringActive,
                q = b.newHiddenItemsCounter,
                Y = { top: P[0], bottom: P[1] },
                K = Y.top <= 0 && Y.bottom <= 0,
                Z = Object.fromEntries(Object.entries(d).filter(([e]) => "buyPrice" !== e)),
                J = (0, r.useCallback)(
                  () =>
                    c.find((e) => {
                      const t = F.current.get(e.intCD);
                      return t && t.offsetTop - y > 0;
                    }),
                  [c, y],
                ),
                Q = (0, r.useCallback)(() => {
                  var t;
                  e(null == (t = J()) ? void 0 : t.intCD);
                }, [J, e]);
              !(function ({
                key: e = ws.n.ESCAPE,
                callback: t = () => i.O.view.sendEvent.close(),
                preventPropagation: u = !0,
              } = {}) {
                e_(e, t, u);
              })({ callback: Q });
              const ee = () => {
                  z.playHighlight();
                },
                te = (0, r.useCallback)(
                  (t) => {
                    (t && s.onSelectItem(t), e());
                  },
                  [e, s],
                ),
                ue = (0, r.useCallback)(
                  (t) => {
                    (t && s.onEditItem(t), e());
                  },
                  [s, e],
                ),
                ae = (0, r.useCallback)(() => {
                  (s.onShowBuyWindow(), e());
                }, [s, e]),
                ne = (function (e, t) {
                  const u = e.contentRef,
                    a = e.wrapperRef,
                    n = e.scrollPosition,
                    o = e.clampPosition,
                    s = e.animationScroll,
                    l = e.events,
                    c = (0, r.useState)(Jc),
                    _ = c[0],
                    d = c[1];
                  return (
                    (0, r.useEffect)(() => {
                      const e = u.current;
                      e && (e.style.cursor = "dragging" === _.type ? "grabbing" : "grab");
                    }, [u, _.type]),
                    (0, r.useEffect)(() => {
                      if ("dragging" !== _.type) return;
                      const e = i.O.client.events.mouse.move(([e, r]) => {
                          const i = u.current,
                            l = a.current;
                          if (!i || !l) return;
                          if ("inside" === r && e.clientY < 0) return;
                          const c = "inside" === r ? e.clientY : e.clientY - l.offsetTop,
                            d = _.positionFrom - c,
                            m = _.previousScrollPosition + d;
                          n.start(
                            Object.assign(
                              {
                                scrollPosition: o(i, m),
                                from: { scrollPosition: s.scrollPosition.get() },
                              },
                              t && { config: t },
                            ),
                          );
                        }),
                        r = i.O.client.events.mouse.up(function () {
                          d({ type: "scrollingToEnd" });
                        });
                      return () => {
                        (e(), r());
                      };
                    }, [s.scrollPosition, o, u, _, n, a, t]),
                    (0, r.useEffect)(() => {
                      if ("scrollingToEnd" !== _.type) return;
                      const e = () => {
                        d(Jc);
                      };
                      return (
                        s.scrollPosition.idle && e(),
                        l.on("rest", e),
                        () => l.off("rest", e)
                      );
                    }, [s.scrollPosition, _.type, l]),
                    (0, r.useEffect)(() => {
                      const e = u.current;
                      if (!e) return;
                      const t = (e) => {
                        d({
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
                    _
                  );
                })(A),
                re = "dragging" === ne.type,
                oe = (0, r.useCallback)(() => {
                  const e = A.getContainerSize();
                  if (!e) return;
                  const t = _.length > 1 && !K;
                  if ((t !== x && O(t), !t)) return void (N.length > 0 && I([]));
                  const u = [];
                  (_.forEach((t) => {
                    const a = D.current.get(t.bookmarkIndex);
                    if (a) {
                      let n = (a.offsetTop + a.offsetHeight / 2) / e;
                      ((n = Math.max(0, Math.min(1, n))),
                        u.push({ name: t.bookmarkName, position: n, index: t.bookmarkIndex }));
                    }
                  }),
                    JSON.stringify(u) !== JSON.stringify(N) && I(u));
                }, [N, _, K, A, x]),
                se = (0, r.useCallback)(() => {
                  const e = A.animationScroll.scrollPosition.goal;
                  k(e);
                  const t = A.getBounds(),
                    u = t[0],
                    a = t[1];
                  (u === Y.top && a === Y.bottom) || H([u, a]);
                }, [A, Y.top, Y.bottom]),
                ie = (0, r.useCallback)(
                  (e) => {
                    const t = c[e],
                      u = F.current.get(t.intCD);
                    if (u) return { position: u.offsetTop, isFilled: t.isFilled };
                  },
                  [c],
                ),
                le = (0, r.useCallback)(() => {
                  const e = A.getWrapperSize();
                  if (e) {
                    const t = A.animationScroll.scrollPosition.goal;
                    a(t, e, c.length, ie);
                  }
                }, [A, c, a, ie]),
                ce = (0, r.useCallback)(() => {
                  (se(), oe(), le());
                }, [se, oe, le]);
              (0, r.useEffect)(
                () => (
                  A.events.on("change", ce),
                  A.events.on("recalculateContent", ce),
                  A.events.on("resizeHandled", ce),
                  () => {
                    (A.events.off("change", ce),
                      A.events.off("recalculateContent", ce),
                      A.events.off("resizeHandled", ce));
                  }
                ),
                [ce, se, A.events],
              );
              const _e = (0, r.useState)(t),
                de = _e[0],
                me = _e[1];
              (ml(() => {
                if (de > -1 && C && h && !K) {
                  const e = F.current.get(de);
                  if (e) {
                    const t = e.offsetTop - 0.5 * e.offsetHeight;
                    (A.applyScroll(t, { immediate: !0, reset: !0 }), me(-1));
                  }
                }
              }, [t, C, h, K, A]),
                ml(() => {
                  A.applyScroll(0, { immediate: !0, reset: !0 });
                }, [u, A]));
              const Ee = v()(d_.lip, (y === Y.bottom || K) && d_.lip__hidden);
              return o().createElement(
                "div",
                { className: v()(d_.base, re && d_.base__dragging) },
                o().createElement("div", { className: d_.baseBack }),
                o().createElement(Fr, {
                  tabs: E,
                  onClick: (e) => {
                    (W(R.sounds.cust_tab_switch()), s.selectTab(e));
                  },
                  onHoverTab: s.hoverTab,
                  mixClass: d_.tabs,
                }),
                o().createElement(
                  "div",
                  { className: d_.filterHeader },
                  o().createElement(
                    "div",
                    { className: d_.filterCounter },
                    o().createElement(Oa, {
                      title:
                        X &&
                        o().createElement(
                          et,
                          { body: E_.customization.resetFilter.tooltip.text() },
                          o().createElement(
                            $,
                            {
                              type: G.ghost,
                              onClick: s.clearFilter,
                              mixClass: v()(d_.filtersClearButton),
                            },
                            o().createElement("div", { className: d_.filtersClearIcon }),
                          ),
                        ),
                      label: o().createElement(ze, {
                        text: E_.filters.selectedTitle(),
                        className: d_.filterNumbersLabel,
                      }),
                      from: U,
                      to: j,
                      isFilterRange: !0,
                      isGlowVisible: X,
                      isSelectMode: !1,
                      className: d_.filterNumbers,
                      classNames: { counterGlow: d_.counterGlow },
                      isHideTotalCounter: !X,
                      isSelectedLimitReached: q > 0,
                      isAnimationEnabled: q > 0,
                    }),
                  ),
                  o().createElement(
                    "div",
                    { className: d_.filter },
                    o().createElement(tn, { isReverse: !0, buttonSize: m }),
                  ),
                ),
                o().createElement(
                  "div",
                  { className: d_.carouselWrapper },
                  c.length > 0
                    ? o().createElement(
                        o().Fragment,
                        null,
                        o().createElement(
                          _l.Vertical.Area,
                          {
                            api: A,
                            className: v()(d_.scrollArea, K && d_.scrollArea__withoutScroll),
                            classNames: {
                              content: v()(d_.scrollContent, K && d_.scrollContent__withoutScroll),
                            },
                          },
                          _.map((e, t) => {
                            var u;
                            const a = p.isProgressionDecalsBannerVisible && e.isProgressive;
                            return o().createElement(
                              "div",
                              { className: d_.categories, key: `${t}` },
                              "" !== e.bookmarkName &&
                                o().createElement(
                                  "div",
                                  {
                                    className: d_.category,
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
                                { className: d_.slots },
                                a &&
                                  o().createElement(ds, {
                                    mixClass: d_.slot,
                                    onClick: s.clickDecalsBanner,
                                  }),
                                c
                                  .slice(
                                    e.bookmarkIndex,
                                    null == (u = _[t + 1]) ? void 0 : u.bookmarkIndex,
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
                                        xc,
                                        m_(
                                          {
                                            onSelectItem: te,
                                            onEditItem: ue,
                                            onHoverItem: s.hoverItem,
                                            classMix: d_.slot,
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
                          { className: d_.scrollbarWrapper },
                          x &&
                            o().createElement(
                              "div",
                              { className: d_.bookmarksWrapper },
                              N.map(({ name: e, position: t, index: u }) =>
                                o().createElement(
                                  et,
                                  { key: `${e}-${u}`, body: e },
                                  o().createElement("div", {
                                    onMouseEnter: ee,
                                    onClick: () =>
                                      ((e) => {
                                        const t = A.getWrapperSize(),
                                          u = A.getContainerSize();
                                        if (!t || !u) return;
                                        const a = D.current.get(e);
                                        if (a) {
                                          z.playClick();
                                          const e = a.offsetTop + a.offsetHeight / 2,
                                            n = e - (e / u) * (t - 34) - 17;
                                          A.scrollPosition.start({ scrollPosition: n });
                                        }
                                      })(u),
                                    className: d_.bookmark,
                                    style: { top: 100 * t + "%" },
                                  }),
                                ),
                              ),
                            ),
                          o().createElement(_l.Vertical.Bar, {
                            classNames: { thumb: d_.thumb },
                            api: A,
                          }),
                        ),
                      )
                    : o().createElement(
                        __,
                        {
                          warningHeader: E_.customization.message.header(),
                          warningDescription: E_.customization.message.description(),
                          buttonType: G.secondary,
                          onClick: s.clearFilter,
                          className: d_.emptyState,
                        },
                        o().createElement(ze, { text: E_.customization.resetFiltersBtn.label() }),
                      ),
                ),
                o().createElement(Bt, {
                  id: R.views.lobby.customization.CustomizationMoneyBalance("resId"),
                  mixClass: d_.currency,
                }),
                o().createElement(
                  "div",
                  { className: d_.closeButton },
                  o().createElement(je, {
                    side: "right",
                    type: "close",
                    caption: E_.customization.closeButton(),
                    onClick: Q,
                  }),
                ),
                o().createElement(
                  "div",
                  { className: d_.priceWrapper },
                  o().createElement("div", { className: Ee }),
                  o().createElement(
                    "div",
                    { className: d_.price },
                    f &&
                      o().createElement(Cu, {
                        price: f,
                        onResetHandler: s.onClearBasket,
                        onBackHandler: s.onCancelChanges,
                        cartParams: Z,
                        onApplyHandler: ae,
                        buttonSize: m,
                      }),
                  ),
                ),
              );
            },
          );
        let b_;
        !(function (e) {
          ((e[(e.UnselectedEmpty = 0)] = "UnselectedEmpty"),
            (e[(e.SelectedEmpty = 1)] = "SelectedEmpty"),
            (e[(e.UnselectedFilled = 2)] = "UnselectedFilled"),
            (e[(e.SelectedFilled = 3)] = "SelectedFilled"),
            (e[(e.Preview = 4)] = "Preview"),
            (e[(e.Locked = 5)] = "Locked"),
            (e[(e.Removed = 6)] = "Removed"),
            (e[(e.Edit = 7)] = "Edit"));
        })(b_ || (b_ = {}));
        const p_ = "ArrowMarker_base_a2",
          A_ = "ArrowMarker_base__scaled_c5",
          C_ = "ArrowMarker_content_b3",
          h_ = "ArrowMarker_arrow_93",
          f_ = "ArrowMarker_arrow__left_88",
          v_ = "ArrowMarker_arrow__right_6b",
          F_ = "ArrowMarker_arrow__leftPressed_e7",
          D_ = "ArrowMarker_arrow__rightPressed_7b",
          B_ = "ArrowMarker_arrow__leftDisabled_7d",
          S_ = "ArrowMarker_arrow__rightDisabled_11",
          y_ = "ArrowMarker_arrowHover_48",
          w_ = "ArrowMarker_arrowHover__left_36",
          k_ = "ArrowMarker_arrowHover__right_a5",
          T_ = "ArrowMarker_arrowHitArea_66",
          N_ = "ArrowMarker_arrowHitArea__left_a8",
          I_ = "ArrowMarker_arrowHitArea__right_e5";
        function M_() {
          return (
            (M_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            M_.apply(this, arguments)
          );
        }
        let x_;
        !(function (e) {
          ((e.left = "left"), (e.right = "right"));
        })(x_ || (x_ = {}));
        const O_ = (0, St.Pi)(() => {
            const e = $a(),
              t = e.model,
              u = e.controls,
              a = t.carouselModel.get(),
              n = a.isRightAvailable,
              s = a.isLeftAvailable,
              i = (0, r.useState)({ left: !1, right: !1 }),
              l = i[0],
              c = i[1],
              _ = (0, r.useState)({ left: !1, right: !1 }),
              d = _[0],
              m = _[1],
              E = ya(),
              g = (e) => ({
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
                    (W(R.sounds.cust_select()), u.onPressSelectNextItem(e === x_.left));
                  })(e),
              });
            return o().createElement(
              "div",
              { className: v()(p_, E > 1 && A_) },
              o().createElement(
                "div",
                { className: C_ },
                o().createElement("div", { className: v()(h_, f_, d.left && F_, !s && B_) }),
                o().createElement("div", { className: v()(h_, v_, d.right && D_, !n && S_) }),
                o().createElement("div", { className: v()(y_, l.left && !d.left && s && w_) }),
                o().createElement("div", { className: v()(y_, l.right && !d.right && n && k_) }),
                o().createElement("div", M_({ className: v()(T_, N_) }, g(x_.left))),
                o().createElement("div", M_({ className: v()(T_, I_) }, g(x_.right))),
              ),
            );
          }),
          L_ = {
            base: "EditMarker_base_77",
            underline: "EditMarker_underline_58",
            underline__1: "EditMarker_underline__1_bf",
            underline__2: "EditMarker_underline__2_a8",
            underline__3: "EditMarker_underline__3_7f",
            underline__errorAnimation: "EditMarker_underline__errorAnimation_ea",
            shake: "EditMarker_shake_85",
          },
          R_ = (0, St.Pi)(() => {
            const e = $a(),
              t = e.model,
              u = e.controls,
              a = t.computes.getEditData(),
              n = (0, r.useCallback)(
                (e) => {
                  const t = e.which;
                  if ((t === ws.n.ENTER && u.onEnterInput(), t >= ws.n.KEY_0 && t <= ws.n.KEY_9)) {
                    const e = t - ws.n.KEY_1 + 1;
                    u.onAddChar(String(e));
                  } else if (t >= ws.n.NUMPAD_0 && t <= ws.n.NUMPAD_9) {
                    const e = t - ws.n.NUMPAD_0;
                    u.onAddChar(String(e));
                  } else
                    (t === ws.n.DELETE && u.onDeleteAllChars(),
                      t === ws.n.BACKSPACE && u.onRemoveChar());
                },
                [u],
              );
            (0, r.useEffect)(
              () => (
                window.addEventListener("keydown", n),
                () => window.removeEventListener("keydown", n)
              ),
              [n],
            );
            const s = a.inscriptionState === Ho.NotAvailableEnter;
            return o().createElement(
              "div",
              { className: L_.base },
              o().createElement("div", {
                key: s ? a.startTimestamp : "",
                className: v()(
                  L_.underline,
                  L_[`underline__${a.editDigitsCount}`],
                  s && L_.underline__errorAnimation,
                ),
              }),
            );
          }),
          P_ = {
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
        let H_;
        !(function (e) {
          ((e.EMBLEM = "Emblem"),
            (e.INSCRIPTION = "Inscription"),
            (e.PROJECTION_DECAL = "ProjectionDecal"));
        })(H_ || (H_ = {}));
        const W_ = [H_.EMBLEM, H_.PROJECTION_DECAL, H_.INSCRIPTION],
          z_ = (0, r.memo)(
            ({
              isHovered: e,
              index: t,
              isActiveInscription: u,
              onMarkerClick: a,
              onMarkerHover: n,
              onMarkerDragOut: s,
              state: i,
              slotType: l,
              scale: c,
            }) => {
              const _ = (0, r.useState)(!1),
                d = _[0],
                m = _[1],
                E = (0, r.useRef)(i),
                g = (0, r.useState)(!1),
                b = g[0],
                p = g[1],
                A = W_.includes(l);
              (0, r.useEffect)(() => {
                ((E.current === b_.Preview && i === b_.UnselectedFilled) ||
                (E.current === b_.Locked && i === b_.UnselectedEmpty)
                  ? p(!0)
                  : p(!1),
                  (E.current = i));
              }, [i]);
              return o().createElement(
                "div",
                { className: P_.markerItem },
                o().createElement(
                  "div",
                  {
                    className: v()(P_.base, P_[`base__state${i}`], e && P_.base__hovered),
                    onClick: () => {
                      (i === b_.UnselectedFilled && W(R.sounds.cust_select()),
                        i === b_.Removed && W(R.sounds.cust_select_remove()),
                        i === b_.Locked ? (W(R.sounds.cust_negative()), a(t)) : a(t));
                    },
                    onMouseEnter: () => {
                      (z.playHighlight(), n(t, !0));
                    },
                    onMouseLeave: () => {
                      (n(t, !1), d && s(t));
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
                  i !== b_.Edit &&
                    o().createElement(
                      "div",
                      { className: P_.defaultMarker },
                      o().createElement("div", {
                        className: v()(
                          P_.defaultMarkerIcon,
                          P_[`defaultMarkerIcon__${l}`],
                          b && P_.defaultMarkerIcon__withAnimation,
                        ),
                        onAnimationEndCapture: () => {
                          p(!1);
                        },
                      }),
                    ),
                  i === b_.Edit &&
                    o().createElement(
                      "div",
                      { className: P_.editMarkerWrapper },
                      o().createElement(R_, null),
                    ),
                  i === b_.SelectedFilled &&
                    A &&
                    o().createElement(
                      "div",
                      { className: P_.arrowMarkerWrapper },
                      o().createElement(O_, null),
                    ),
                  o().createElement("div", { className: P_.interactive }),
                ),
                u &&
                  i === b_.Locked &&
                  o().createElement(
                    "div",
                    { className: P_.inscription },
                    o().createElement(ze, {
                      className: P_.inscriptionText,
                      text: R.strings.vehicle_customization.notification.slotIsFilled.title(),
                    }),
                  ),
              );
            },
          ),
          U_ = "MarkersList_markerWrapper_90",
          G_ = (0, St.Pi)(({ isSceneDraggingChange: e }) => {
            const t = $a(),
              u = t.model,
              a = t.controls,
              n = u.customizationTypes.get(),
              s = (0, r.useState)(0),
              i = s[0],
              l = s[1],
              c = (0, r.useState)([]),
              _ = c[0],
              d = c[1],
              m = (0, r.useState)([]),
              E = m[0],
              g = m[1],
              b = (0, r.useState)([]),
              p = b[0],
              A = b[1],
              C = (0, r.useRef)(e),
              h = (0, r.useRef)(_);
            (0, r.useEffect)(() => {
              h.current = _;
            }, [_]);
            const f = (0, r.useRef)([]),
              v = (0, r.useRef)([]),
              F = (0, r.useRef)(0),
              D = (0, r.useState)(null),
              B = D[0],
              S = D[1],
              y = (0, r.useRef)([]),
              w = (0, r.useRef)([]),
              k = (0, r.useState)([]),
              T = k[0],
              N = k[1];
            ((0, r.useEffect)(() => {
              if (e)
                return un(() => {
                  C.current = e;
                }, 300);
              C.current = e;
            }, [e]),
              ((e) => {
                const t = (0, r.useRef)(0),
                  u = (0, r.useRef)(0),
                  a = (0, r.useRef)(0),
                  n = (0, r.useRef)(0),
                  o = (r) => {
                    if (u.current) {
                      const t = r - u.current;
                      ((a.current += t), (n.current = n.current + t), (n.current = 0), e());
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
                  ((f.current = Array(e.length).fill("0")),
                  A(Array(e.length).fill(0)),
                  (v.current = Array(e.length).fill(!1)),
                  g(Array(e.length).fill(!1)),
                  (h.current = Array(e.length).fill(0)),
                  d(Array(e.length).fill(0)),
                  (F.current = e.length),
                  l(e.length)),
                  e.forEach((t, u) => {
                    const a = y.current[u];
                    if (!a) return;
                    const r = `${t.posx.toFixed(1)}rem`,
                      o = `${t.posy.toFixed(1)}rem`,
                      s = `${t.opacity.toFixed(2)}`,
                      i = `${t.scale.toFixed(2)}`,
                      l = `${t.areaId}`,
                      c = `${t.zIndex}`,
                      _ = Object.keys(n).find((e) => n[e] === t.slotType);
                    if (void 0 === _) throw Error(`invalid slotType ${t.slotType} of ${t.state}`);
                    const m = `${t.regionIdx}`,
                      E = t.state,
                      b = t.isHovered,
                      p = w.current[u] || { lastOpacityUpdate: 0 },
                      C = "flex" === a.style.display;
                    t.isVisible
                      ? ((a.style.display = "flex"),
                        (p.opacity === s && C) ||
                          ((a.style.opacity = "1"),
                          N((e) => {
                            var t;
                            return (
                              e[u] && null != (t = Object.keys(e[u])) && t.length
                                ? (e[u] = Object.assign({}, e[u], { opacity: s }))
                                : (e[u] = { opacity: s }),
                              e
                            );
                          })),
                        (p.x === r && C) || a.style.setProperty("--x", r),
                        (p.y === o && C) || a.style.setProperty("--y", o),
                        (p.zIndex === c && C) || a.style.setProperty("--zIndex", c),
                        (p.scale === i && C) ||
                          (a.style.setProperty("--scale", "1"),
                          N(
                            (e) => (
                              e[u] && Object.keys(e[u]).length
                                ? (e[u] = Object.assign({}, e[u], { scale: i }))
                                : (e[u] = { scale: i }),
                              e
                            ),
                          )),
                        (a.getAttribute("areaId") === l && e.length === F.current && C) ||
                          a.setAttribute("areaId", l),
                        (a.getAttribute("slotType") === _ && e.length === F.current && C) ||
                          a.setAttribute("slotType", _),
                        (a.getAttribute("regionIdx") === m && e.length === F.current && C) ||
                          a.setAttribute("regionIdx", m),
                        (w.current[u] = {
                          x: r,
                          y: o,
                          opacity: s,
                          scale: i,
                          lastOpacityUpdate: p.lastOpacityUpdate || 0,
                          lastScaleUpdate: p.lastScaleUpdate || 0,
                          areaId: l,
                          slotType: _,
                          regionIdx: m,
                          state: E,
                          zIndex: c,
                        }),
                        h.current[u] !== E &&
                          d((e) => {
                            const t = [...e];
                            return ((t[u] = E), t);
                          }),
                        f.current[u] !== _ &&
                          A((e) => {
                            const t = [...e];
                            return ((t[u] = _), t);
                          }),
                        v.current[u] !== b &&
                          g((e) => {
                            const t = [...e];
                            return ((t[u] = b), t);
                          }),
                        (h.current[u] = E),
                        (f.current[u] = _),
                        (v.current[u] = b))
                      : (a.style.display = "none");
                  }));
              }));
            const I = (0, r.useRef)(null),
              M = (0, r.useCallback)(
                (e) => {
                  I.current && clearTimeout(I.current);
                  const t = y.current[e];
                  if (!t) return;
                  if (h.current[e] === b_.Locked)
                    (S(null),
                      S(e),
                      (I.current = setTimeout(() => {
                        S((t) => (t === e ? null : t));
                      }, 2300)));
                  else {
                    const e = Number(t.getAttribute("areaId")),
                      u = t.getAttribute("slotType"),
                      r = Number(t.getAttribute("regionIdx"));
                    n[u] && a.selectAnchor(e, n[u], r);
                  }
                },
                [a, n],
              ),
              x = (0, r.useCallback)(
                (e, t) => {
                  if (y.current.length > e && e >= 0) {
                    const u = y.current[e],
                      r = Number(u.getAttribute("areaId")),
                      o = u.getAttribute("slotType"),
                      s = Number(u.getAttribute("regionIdx"));
                    n[o] && a.hoverAnchor(r, n[o], s, t);
                  }
                },
                [a, n],
              ),
              O = (0, r.useCallback)(
                (e) => {
                  if (y.current.length > e && e >= 0) {
                    const t = y.current[e],
                      u = Number(t.getAttribute("areaId")),
                      r = t.getAttribute("slotType"),
                      o = Number(t.getAttribute("regionIdx"));
                    n[r] && a.dragAnchor(u, n[r], o);
                  }
                },
                [a, n],
              );
            return o().createElement(
              o().Fragment,
              null,
              Array.from({ length: i }).map((e, t) =>
                o().createElement(
                  "div",
                  { key: t, className: U_, ref: (e) => (y.current[t] = e) },
                  o().createElement(z_, {
                    index: t,
                    isActiveInscription: B === t,
                    onMarkerClick: () => M(t),
                    onMarkerHover: x,
                    onMarkerDragOut: O,
                    state: _[t],
                    isHovered: E[t],
                    slotType: p[t],
                    scale: T[t],
                  }),
                ),
              ),
            );
          });
        function V_() {
          return (
            (V_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            V_.apply(this, arguments)
          );
        }
        let j_;
        !(function (e) {
          ((e.CAMOUFLAGE = "camouflage"),
            (e.PROJECTION_DECAL = "projectionDecal"),
            (e.INSCRIPTION = "inscription"));
        })(j_ || (j_ = {}));
        const $_ = "mainview:close",
          X_ = "close_dialog",
          q_ = [j_.CAMOUFLAGE, j_.PROJECTION_DECAL],
          Y_ = R.strings.customization,
          K_ = R.strings.customization.tooltips.filters;
        viewEnv.clearInternalCacheAfterFinalize();
        const Z_ = (0, St.Pi)(() => {
          var e, t;
          const u = $a(),
            a = u.controls,
            n = u.model,
            s = w().mediaSize,
            l = n.root.get(),
            c = l.isBuyViewActive,
            _ = l.isStyleInfoViewActive,
            d = l.isEditable,
            m = l.isApplyToAllSeasonsAvailable,
            E = l.isApplyToAllSeasonsSelected,
            g = l.isShowProgressionInfoButton,
            b = l.isHoverVehicleSlot,
            p = l.isProgressiveItemsViewVisible,
            A = l.isFilterPopoverOpened,
            C = l.isOnboardingViewOpened,
            h = l.isCustomizationResourceEntryPointAvailable,
            f = (0, r.useRef)(null),
            F = n.computes.getStageSwitcher(),
            D = n.computes.getSelectedTabItemType(),
            S = F.isVisible,
            y = F.selectedLevel,
            k = F.numberOfBullets,
            T = F.isBulletsBeforeCurrentDisabled,
            N = F.currentLevel,
            I = n.toolbarModel.get(),
            M = I.isToolbarPanelEnabled,
            x = I.isInscriptionPanelEnabled,
            O = n.carouselModel.get(),
            L = O.scrollStartItemId,
            P = O.isCarouselArrowsHintVisible,
            H = n.computes.getSelectedItemId(),
            z = (0, r.useState)(-1),
            U = z[0],
            j = z[1],
            X = (0, r.useRef)({
              tabId: void 0,
              scrollStartItemId: void 0,
              selectedItemId: void 0,
              firstExpandedItemId: void 0,
            }),
            q = (0, r.useState)(!1),
            Y = q[0],
            K = q[1],
            Z = (0, r.useState)(!1),
            J = Z[0],
            ee = Z[1],
            te = (0, r.useState)(!1),
            ue = te[0],
            ae = te[1],
            re = (0, r.useState)(!1),
            oe = re[0],
            se = re[1],
            ie = n.computes.getBuyPrice(),
            le = n.computes.getItems(),
            ce = n.computes.getCategories(),
            _e = n.computes.getArrowsList(),
            de = n.computes.getTabsItemsList(),
            me = n.computes.getBillModel(),
            Ee = n.computes.getSeasonsTabsItemsList(),
            ge = n.computes.getToolbarButtonsList(),
            be = n.magneticToolModel.get(),
            pe = n.headerVehicleInfo.get(),
            Ae = pe.description,
            Ce = pe.isStyleBonusPreviewText,
            he = pe.vehicle,
            fe = s <= B.Small ? V.small : V.medium,
            ve = Et(),
            Fe = M && !x && !Y && !c && !_,
            De = _t(Fe),
            Be = _t(be.isEnabled),
            Se = n.computes.getEditData(),
            ye = !Y && !Fe && !Se.inscriptionState;
          localStorage.removeItem(X_);
          const we = (0, r.useCallback)(
              (e) => {
                (j(e || -1), a.onExpandCarousel(!1), K(!1));
              },
              [a],
            ),
            ke = (0, r.useCallback)(
              (e, t) => {
                (a.onToolbarItemClick(e, t),
                  e === tt.CUSTOMIZATION_SHEET_ACTION_CLOSE && a.onSceneOverChange(!0));
              },
              [a],
            ),
            Te = (0, r.useCallback)(() => {
              const e = localStorage.getItem(X_);
              engine.trigger($_);
              const t =
                n.computes
                  .getMarkersList()
                  .filter((e) => "1" === e.state.toString() || "3" === e.state.toString()).length >
                0;
              if (!Y) {
                if (Fe)
                  return (
                    a.onToolbarItemClick(tt.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1),
                    ke(tt.CUSTOMIZATION_SHEET_ACTION_CLOSE, 0),
                    void a.onUnselectItem()
                  );
                if (
                  n.computes.getToolbarData().isInscriptionPanelEnabled &&
                  2 !== n.computes.getEditData().inscriptionState &&
                  1 !== n.computes.getEditData().inscriptionState
                )
                  a.onSceneClick();
                else if (
                  (!d &&
                    0 === n.computes.getEditData().inscriptionState &&
                    !n.computes.getToolbarData().isToolbarPanelEnabled) ||
                  ((2 === n.computes.getEditData().inscriptionState ||
                    1 === n.computes.getEditData().inscriptionState) &&
                    a.onCancelChanges(),
                  a.closeEditItem(),
                  c)
                )
                  if (be.isEnabled) a.onUnselectItem();
                  else {
                    if (!t)
                      return (
                        c
                          ? a.closeBinEsc()
                          : _
                            ? a.onCloseStyleInfoEsc()
                            : ((e && "0" !== e) || a.onClose(), localStorage.setItem(X_, "1")),
                        () => {
                          (engine.off($_), localStorage.setItem(X_, "0"));
                        }
                      );
                    a.onSceneClick();
                  }
              }
            }, [a, c, Y, d, Fe, _, be.isEnabled, n.computes, ke]);
          (0, r.useEffect)(() => {
            p && viewEnv.clearInternalCaches();
          }, [p]);
          const Ne = Q(
            (e, t, u, a) => {
              if (t) {
                var n;
                let r = 0,
                  o = u,
                  s = !1,
                  i = 0;
                for (; i < u;) {
                  const u = a(i);
                  if (u) {
                    const a = u.position - e < 0,
                      n = u.position - e > t;
                    if ((a && i > r ? (r = i) : s || (s = !u.isFilled), n)) {
                      o = i;
                      break;
                    }
                  }
                  i++;
                }
                s || (s = !(null != (n = a(r)) && n.isFilled));
                let l = r,
                  c = 0;
                for (; c < 5 && l > 0;) (l--, c++);
                ((r = l), s && Ie(r, o));
              }
            },
            [(Ie = a.onRequestItems)],
            200,
          );
          var Ie;
          !(function ({
            key: e = ws.n.ESCAPE,
            callback: t = () => i.O.view.sendEvent.close(),
            preventPropagation: u = !0,
          } = {}) {
            Ms(e, t, u);
          })({ callback: Te, preventPropagation: !1 });
          const Me = ne(),
            xe = Q(
              () => {
                c ? a.buyItems() : a.onShowBuyWindow();
              },
              [c],
              300,
            ),
            Oe = (0, r.useCallback)(
              (e) => {
                a.selectSeason(e);
              },
              [a],
            ),
            Le = (0, r.useCallback)(
              (e) => {
                e && a.onSelectItem(e);
              },
              [a],
            ),
            Re = (0, r.useCallback)(
              (e) => {
                !C && a.onSceneOverChange(e);
              },
              [a, C],
            );
          ((0, r.useEffect)(() => {
            a.onSceneOverChange(!A);
          }, [A, a]),
            (0, r.useEffect)(() => {
              a.onSceneOverChange(!C);
            }, [C, a]),
            (0, r.useEffect)(() => {
              !Be && be.isEnabled && Y && we();
            }, [we, Y, be.isEnabled, Be]),
            (0, r.useEffect)(() => {
              Fe && !De
                ? q_.includes(D)
                  ? W(R.sounds.radial_big())
                  : W(R.sounds.radial_small())
                : !Fe &&
                  De &&
                  (q_.includes(D) ? W(R.sounds.radial_big_close()) : W(R.sounds.radial_small()));
            }, [Fe, De, D]),
            (0, r.useEffect)(() => {
              if (ve.isRunning) return () => ve.clear();
            }, [ve]),
            (0, r.useEffect)(() => {
              (c && ee(!0),
                c ||
                  ve.run(() => {
                    ee(!1);
                  }, 400));
            }, [c, ve]),
            (0, r.useEffect)(() => {
              (_ && (Y && we(), se(!0)),
                _ ||
                  ve.run(() => {
                    se(!1);
                  }));
            }, [_, ve, Y, we]));
          const Pe = Object.fromEntries(Object.entries(me).filter(([e]) => "buyPrice" !== e)),
            He = (0, r.useCallback)(
              (e) => {
                a.onStageChange(e);
              },
              [a],
            ),
            We = (0, r.useCallback)(() => {
              (a.onToolbarItemClick(tt.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1),
                a.progressiveInfoButtonClick());
            }, [a]);
          (0, r.useEffect)(() => {
            0 === le.length &&
              Me.scrollPosition.start({ scrollPosition: 0, reset: !0, immediate: !0 });
          }, [Me, le]);
          const Ue = (0, r.useCallback)(() => {
              (a.onToolbarItemClick(tt.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1), a.onClose());
            }, [a]),
            Ge = (0, r.useCallback)(() => {
              !C && a.onSceneOverChange(!1);
            }, [a, C]),
            Ve = (0, r.useCallback)(() => {
              !C && a.onSceneOverChange(!0);
            }, [a, C]);
          return o().createElement(
            "div",
            { className: v()(xs, ue ? zs : Ws, Y && Os), onMouseEnter: Ve, onMouseLeave: Ge },
            o().createElement(
              "div",
              { className: Ls },
              Y
                ? o().createElement(g_, {
                    onCarouselCollapse: we,
                    startScrollItemId: U,
                    onUpdateItems: Ne,
                    tabId: null == (e = n.computes.getSelectedTab()) ? void 0 : e.id,
                  })
                : o().createElement(
                    o().Fragment,
                    null,
                    !oe &&
                      o().createElement(ss, {
                        moveSpace: a.moveSpace,
                        onSceneOverChange: Re,
                        onSceneDraggingChange: a.onSceneDraggingChange,
                        onSceneClick: a.onSceneClick,
                        onHideElements: (e) => {
                          ae(e);
                        },
                        onResetMagneticTool: a.onUnselectItem,
                        isHovered: b,
                        isOnboardingViewOpened: C,
                      }),
                    g &&
                      !c &&
                      o().createElement(
                        "div",
                        { className: Hs },
                        o().createElement(je, {
                          caption: Y_.progression.info(),
                          type: "info",
                          onClick: We,
                        }),
                      ),
                    !_ &&
                      !c &&
                      o().createElement(
                        "div",
                        { className: Us },
                        o().createElement(je, {
                          side: "right",
                          type: "close",
                          caption: Y_.customization.closeButton(),
                          onClick: Ue,
                        }),
                      ),
                    _ &&
                      o().createElement(
                        "div",
                        { className: wi },
                        o().createElement(je, {
                          side: "left",
                          type: "back",
                          caption: Y_.customization.backButton(),
                          onClick: a.onCloseStyleInfoEsc,
                        }),
                      ),
                    !c &&
                      !oe &&
                      o().createElement(
                        "div",
                        { className: v()(Ys, ue ? Zs : Ks), "data-magnetic-tool-support": !0 },
                        o().createElement(G_, { isSceneDraggingChange: ue }),
                      ),
                    Boolean(Se.inscriptionState) &&
                      o().createElement("div", { className: mi }, o().createElement(es, Se)),
                    o().createElement(
                      "div",
                      { className: v()(Rs, c && Ps) },
                      o().createElement(ys, he),
                      !oe && o().createElement(ze, { text: Ae, className: v()(Gs, Ce && Vs) }),
                    ),
                    o().createElement(
                      "div",
                      { className: v()(hi, (c || _) && fi) },
                      o().createElement(
                        "div",
                        { className: js },
                        o().createElement(
                          "div",
                          { className: $s },
                          o().createElement(
                            "div",
                            { className: oi, onMouseEnter: Ge, onMouseLeave: Ve },
                            o().createElement(
                              et,
                              { body: d ? K_.openPanelDisabledButton() : K_.openPanelButton() },
                              o().createElement(
                                "div",
                                { className: ki },
                                o().createElement(
                                  $,
                                  {
                                    type: G.ghost,
                                    size: fe,
                                    mixClass: ni,
                                    onClick: () => {
                                      if (f.current) {
                                        const e = f.current.getFirstVisibleItemId();
                                        j(e || -1);
                                      }
                                      (a.onExpandCarousel(!0), K(!0));
                                    },
                                    disabled: d,
                                  },
                                  o().createElement(ze, {
                                    className: ri,
                                    text: Y_.filters.openPanelButton(),
                                  }),
                                ),
                              ),
                            ),
                            o().createElement("div", { className: ii }),
                            o().createElement(tn, { buttonSize: fe }),
                          ),
                          o().createElement(
                            "div",
                            { className: si, onMouseEnter: Ge, onMouseLeave: Ve },
                            ie &&
                              o().createElement(Cu, {
                                price: ie,
                                onResetHandler: a.onClearBasket,
                                onBackHandler: a.onCancelChanges,
                                onApplyHandler: xe,
                                cartParams: Pe,
                                buttonSize: fe,
                              }),
                          ),
                        ),
                      ),
                      o().createElement(
                        "div",
                        { className: Xs, onMouseEnter: Ge, onMouseLeave: Ve },
                        o().createElement("div", { className: qs }),
                        o().createElement(Fr, {
                          isEditable: d,
                          tabs: de,
                          onClick: (e) => {
                            (W(R.sounds.cust_tab_switch()), a.selectTab(e));
                          },
                          onHoverTab: a.hoverTab,
                          onEditClose: a.closeEditItem,
                        }),
                        le.length > 0
                          ? o().createElement(Zc, {
                              ref: f,
                              scrollApi: Me,
                              items: le,
                              arrowsList: _e,
                              categories: ce,
                              onClick: Le,
                              onHoverItem: a.hoverItem,
                              onEditClick: a.onEditItem,
                              onArrowClick: a.onPressSelectNextItem,
                              isCarouselArrowsHintVisible: P,
                              scrollStartItemId: L,
                              selectedItemId: H,
                              firstExpandedItemId: U,
                              tabId: null == (t = n.computes.getSelectedTab()) ? void 0 : t.id,
                              lastScrollState: X,
                              isEditable: d,
                              onUpdateItems: Ne,
                            })
                          : o().createElement(
                              __,
                              {
                                warningHeader: Y_.customization.message.header(),
                                warningDescription: Y_.customization.message.description(),
                                buttonType: G.secondary,
                                onClick: a.clearFilter,
                                className: Js,
                              },
                              o().createElement(ze, {
                                text: Y_.customization.resetFiltersBtn.label(),
                              }),
                            ),
                      ),
                    ),
                  ),
              o().createElement(
                "div",
                {
                  className: v()(li, !c && (ue ? _i : ci)),
                  "data-magnetic-tool-support": !0,
                  onMouseEnter: Ge,
                  onMouseLeave: Ve,
                },
                o().createElement(hs, { tabs: Ee, onClick: Oe, isMinimised: Y || c || oe }),
              ),
              !Y &&
                o().createElement(ds, {
                  onClick: a.clickDecalsBanner,
                  onMouseEnter: Ge,
                  onMouseLeave: Ve,
                  mixClass: v()(ei, (c || _) && ti, !(c || _) && (ue ? ai : ui)),
                }),
              c &&
                o().createElement(
                  "div",
                  { className: v()(vi, c && Fi) },
                  o().createElement(
                    "div",
                    { className: Di },
                    ie &&
                      o().createElement(Cu, {
                        price: ie,
                        onResetHandler: a.onClearBasket,
                        onBackHandler: a.onCancelChanges,
                        onApplyHandler: xe,
                        onAutoRentChange: a.onAutoRentChange,
                        onAutoRentHintClose: a.onAutoRentHintClose,
                        cartParams: Pe,
                        buttonSize: fe,
                        className: Bi,
                      }),
                  ),
                ),
              m &&
                !Y &&
                !c &&
                !_ &&
                o().createElement(
                  "div",
                  { className: pi, "data-magnetic-tool-support": !0 },
                  o().createElement(bo, {
                    itemType: D,
                    isSelected: E,
                    onSelectApplyingAllSeasons: a.onApplyToAllSeasonsChange,
                  }),
                ),
              Fe &&
                o().createElement(
                  "div",
                  {
                    className: v()(Ei, S && bi),
                    "data-magnetic-tool-support": !0,
                    onMouseEnter: Ge,
                    onMouseLeave: Ve,
                  },
                  o().createElement(co, {
                    toolbarItems: ge,
                    onItemClick: ke,
                    onCloseAction: a.onClose,
                  }),
                ),
              S &&
                !c &&
                !_ &&
                o().createElement(
                  "div",
                  { className: v()(Ei, gi), onMouseEnter: Ge, onMouseLeave: Ve },
                  o().createElement(Un, {
                    numberOfBullets: k,
                    currentNumber: N,
                    selectedNumber: y,
                    isBulletsBeforeCurrentDisabled: T,
                    onChange: He,
                    switcherType: 2 === k ? ut.text : ut.digital,
                    size: zn.small,
                    styleID: 594,
                  }),
                ),
              J &&
                o().createElement(Bt, {
                  id: R.views.lobby.customization.CustomizationBinSubview("resId"),
                  mixClass: v()(Ai, c && Ci),
                }),
              oe &&
                o().createElement(Bt, {
                  id: R.views.lobby.customization.CustomizationStyleInfoView("resId"),
                  mixClass: v()(Si, _ && yi),
                }),
              h && !J && !oe && o().createElement(Po, { mixClass: Qs }),
              ye &&
                o().createElement(
                  "div",
                  { className: di },
                  o().createElement(us, V_({}, be, { selectedTab: D })),
                ),
            ),
          );
        });
        engine.whenReady.then(() => {
          H().render(
            o().createElement(ja, null, o().createElement(L, null, o().createElement(Z_, null))),
            document.getElementById("root"),
          );
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
    (__webpack_require__.O = (e, t, u, a) => {
      if (!t) {
        var n = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, u, a] = deferred[i], r = !0, o = 0; o < t.length; o++)
            (!1 & a || n >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((r = !1), a < n && (n = a));
          if (r) {
            deferred.splice(i--, 1);
            var s = u();
            void 0 !== s && (e = s);
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
    (__webpack_require__.j = 376),
    (() => {
      var e = { 376: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var a,
            n,
            [r, o, s] = u,
            i = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (a in o) __webpack_require__.o(o, a) && (__webpack_require__.m[a] = o[a]);
            if (s) var l = s(__webpack_require__);
          }
          for (t && t(u); i < r.length; i++)
            ((n = r[i]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(l);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [858], () => __webpack_require__(4429));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
