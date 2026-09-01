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
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => s, onResize: () => a }));
        var n = u(472),
          r = u(176);
        const a = (0, n.E)("clientResized"),
          o = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, r.R)(!1);
          }
          function u() {
            e.enabled && (0, r.R)(!0);
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
              : (0, r.R)(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let r = !0;
                  const a = `mouse${t}`,
                    s = o[t]((e) => u([e, "outside"]));
                  function i(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, i),
                    n(),
                    () => {
                      r &&
                        (s(), window.removeEventListener(a, i), (e.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(u)),
              t
            ),
            {},
          );
          return Object.assign({}, a, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
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
      959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => a,
            getSize: () => r,
            graphicsQuality: () => o,
          }));
        var n = u(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function a(e = "px") {
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
      176: (e, t, u) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => n });
      },
      472: (e, t, u) => {
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
      138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => r });
        var n = u(959);
        const r = { view: u(641), client: n };
      },
      722: (e, t, u) => {
        "use strict";
        function n(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function r(e, t, u) {
          return `url(${n(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => r, getTextureUrl: () => n }));
      },
      112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => r });
        var n = u(472);
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
      641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => y,
            events: () => a.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => b,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => g,
            getSize: () => _,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => D,
            isEventHandled: () => v,
            isFocused: () => F,
            pxToRem: () => p,
            remToPx: () => h,
            resize: () => m,
            sendEvent: () => o.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => B,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => P,
          }));
        var n = u(722),
          r = u(112),
          a = u(538),
          o = u(566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, u, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, n);
        }
        function c(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function _(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: h(t.x), y: h(t.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function g() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function h(e) {
          return viewEnv.remToPx(e);
        }
        function C(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function F() {
          return viewEnv.isFocused();
        }
        function D() {
          return viewEnv.isClientAccessible();
        }
        function B() {
          return viewEnv.setEventHandled();
        }
        function v() {
          return viewEnv.isEventHandled();
        }
        function b() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const y = Object.keys(r.W).reduce(
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
          P = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : a.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => l });
        const n = ["args"];
        const r = 2,
          a = 16,
          o = 32,
          s = 64,
          i = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, n);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, o, {
                      arguments:
                        ((r = a),
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
          l = {
            close(e) {
              i("popover" === e ? r : o);
            },
            minimize() {
              i(s);
            },
            move(e) {
              i(a, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, t, u) => {
        "use strict";
        let n, r;
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
          })(r || (r = {})));
      },
      358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => a });
        var n = u(138);
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
            const a = n.O.view.addModelObserver(e, u, r);
            return (
              a > 0
                ? ((this._callbacks[a] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(a) : (this._views[u] = [a])))
                : console.error("Can't add callback for model:", e),
              a
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
        r.__instance = void 0;
        const a = r;
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
      364: (e, t, u) => {
        "use strict";
        u.d(t, { Sw: () => a.Z, B3: () => l, Z5: () => o, B0: () => i, c9: () => C, ry: () => h });
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
        const r = n;
        var a = u(358);
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
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = u(521),
          E = u(138);
        const A = ["args"];
        function g(e, t, u, n, r, a, o) {
          try {
            var s = e[a](o),
              i = s.value;
          } catch (e) {
            return void u(e);
          }
          s.done ? t(i) : Promise.resolve(i).then(n, r);
        }
        const p = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          h = (function () {
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
                  return new Promise(function (n, r) {
                    var a = e.apply(t, u);
                    function o(e) {
                      g(a, n, r, o, s, "next", e);
                    }
                    function s(e) {
                      g(a, n, r, o, s, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          C = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                a = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                  return r;
                })(t, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, a, {
                      arguments:
                        ((n = r),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, a));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          F = () => C(i.CLOSE),
          D = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var B = u(572);
        const v = r.instance,
          b = {
            DataTracker: a.Z,
            ViewModel: B.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: _,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => C(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: F,
            sendClosePopOverEvent: () => C(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, u = 0) => {
              C(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, u, n, r = R.invalid("resId"), a) => {
              const o = E.O.view.getViewGlobalPosition(),
                s = u.getBoundingClientRect(),
                l = s.x,
                c = s.y,
                d = s.width,
                _ = s.height,
                m = {
                  x: E.O.view.pxToRem(l) + o.x,
                  y: E.O.view.pxToRem(c) + o.y,
                  width: E.O.view.pxToRem(d),
                  height: E.O.view.pxToRem(_),
                };
              C(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: t,
                bbox: p(m),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => D(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              D(e, F);
            },
            handleViewEvent: C,
            onBindingsReady: h,
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
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const r = Object.prototype.toString.call(t[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = t[n];
                    u[n] = [];
                    for (let t = 0; t < r.length; t++) u[n].push({ value: e(r[t].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[n] = e(t[n]))
                      : (u[n] = t[n]);
                }
              return u;
            },
            ClickOutsideManager: v,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = b;
      },
      686: (e, t, u) => {
        "use strict";
        var n = {};
        (u.r(n),
          u.d(n, {
            Area: () => qi,
            Bar: () => Ui,
            DefaultScroll: () => Xi,
            Direction: () => Ni,
            defaultSettings: () => Si,
            useHorizontalScrollApi: () => Li,
          }));
        var r = {};
        (u.r(r),
          u.d(r, {
            Area: () => _l,
            Bar: () => ll,
            Default: () => dl,
            useVerticalScrollApi: () => Yi,
          }));
        var a = u(179),
          o = u.n(a);
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
        var i = u(138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function d(e, t, u) {
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
            a = Math.min(n, r);
          return {
            extraLarge: a === u.extraLarge.weight,
            large: a === u.large.weight,
            medium: a === u.medium.weight,
            small: a === u.small.weight,
            extraSmall: a === u.extraSmall.weight,
            extraLargeWidth: n === u.extraLarge.weight,
            largeWidth: n === u.large.weight,
            mediumWidth: n === u.medium.weight,
            smallWidth: n === u.small.weight,
            extraSmallWidth: n === u.extraSmall.weight,
            extraLargeHeight: r === u.extraLarge.weight,
            largeHeight: r === u.large.weight,
            mediumHeight: r === u.medium.weight,
            smallHeight: r === u.small.weight,
            extraSmallHeight: r === u.extraSmall.weight,
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
        const _ = i.O.client.getSize("rem"),
          m = _.width,
          E = _.height,
          A = Object.assign({ width: m, height: E }, d(m, E, l)),
          g = (0, a.createContext)(A),
          p = ["children"];
        const h = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, p);
          const n = (0, a.useContext)(g),
            r = n.extraLarge,
            o = n.large,
            i = n.medium,
            l = n.small,
            c = n.extraSmall,
            d = n.extraLargeWidth,
            _ = n.largeWidth,
            m = n.mediumWidth,
            E = n.smallWidth,
            A = n.extraSmallWidth,
            h = n.extraLargeHeight,
            C = n.largeHeight,
            F = n.mediumHeight,
            D = n.smallHeight,
            B = n.extraSmallHeight,
            v = { extraLarge: h, large: C, medium: F, small: D, extraSmall: B };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && r) return t;
            if (u.large && o) return t;
            if (u.medium && i) return t;
            if (u.small && l) return t;
            if (u.extraSmall && c) return t;
          } else {
            if (u.extraLargeWidth && d) return s(t, u, v);
            if (u.largeWidth && _) return s(t, u, v);
            if (u.mediumWidth && m) return s(t, u, v);
            if (u.smallWidth && E) return s(t, u, v);
            if (u.extraSmallWidth && A) return s(t, u, v);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && h) return t;
              if (u.largeHeight && C) return t;
              if (u.mediumHeight && F) return t;
              if (u.smallHeight && D) return t;
              if (u.extraSmallHeight && B) return t;
            }
          }
          return null;
        };
        h.defaultProps = {
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
        (0, a.memo)(h);
        const C = (e) => {
            const t = (0, a.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          F = (0, a.memo)(({ children: e }) => {
            const t = (0, a.useContext)(g),
              u = (0, a.useState)(t),
              n = u[0],
              r = u[1],
              s = (0, a.useCallback)((e, t) => {
                const u = i.O.view.pxToRem(e),
                  n = i.O.view.pxToRem(t);
                r(Object.assign({ width: u, height: n }, d(u, n, l)));
              }, []);
            (C(() => {
              engine.on("clientResized", s);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", s), [s]));
            const c = (0, a.useMemo)(() => Object.assign({}, n), [n]);
            return o().createElement(g.Provider, { value: c }, e);
          });
        var D = u(483),
          B = u.n(D),
          v = u(926),
          b = u.n(v);
        let f, y, w;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(f || (f = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = l.small.width)] = "Small"),
              (e[(e.Medium = l.medium.width)] = "Medium"),
              (e[(e.Large = l.large.width)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
          })(y || (y = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.small.height)] = "Small"),
              (e[(e.Medium = l.medium.height)] = "Medium"),
              (e[(e.Large = l.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(w || (w = {})));
        const P = () => {
            const e = (0, a.useContext)(g),
              t = e.width,
              u = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return f.ExtraLarge;
                  case e.large:
                    return f.Large;
                  case e.medium:
                    return f.Medium;
                  case e.small:
                    return f.Small;
                  case e.extraSmall:
                    return f.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), f.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return y.ExtraLarge;
                  case e.largeWidth:
                    return y.Large;
                  case e.mediumWidth:
                    return y.Medium;
                  case e.smallWidth:
                    return y.Small;
                  case e.extraSmallWidth:
                    return y.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), y.ExtraSmall);
                }
              })(e),
              o = ((e) => {
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
              mediaHeight: o,
              remScreenWidth: t,
              remScreenHeight: u,
            };
          },
          N = ["children", "className"];
        function S() {
          return (
            (S =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            S.apply(this, arguments)
          );
        }
        const T = {
            [y.ExtraSmall]: "",
            [y.Small]: b().SMALL_WIDTH,
            [y.Medium]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH}`,
            [y.Large]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH}`,
            [y.ExtraLarge]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH} ${b().EXTRA_LARGE_WIDTH}`,
          },
          L = {
            [w.ExtraSmall]: "",
            [w.Small]: b().SMALL_HEIGHT,
            [w.Medium]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT}`,
            [w.Large]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT}`,
            [w.ExtraLarge]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT} ${b().EXTRA_LARGE_HEIGHT}`,
          },
          k = {
            [f.ExtraSmall]: "",
            [f.Small]: b().SMALL,
            [f.Medium]: `${b().SMALL} ${b().MEDIUM}`,
            [f.Large]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE}`,
            [f.ExtraLarge]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE} ${b().EXTRA_LARGE}`,
          },
          x = (e) => {
            let t = e.children,
              u = e.className,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, N);
            const r = P(),
              a = r.mediaWidth,
              s = r.mediaHeight,
              i = r.mediaSize;
            return o().createElement("div", S({ className: B()(u, T[a], L[s], k[i]) }, n), t);
          },
          I = ["children"];
        const M = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, I);
          return o().createElement(F, null, o().createElement(x, u, t));
        };
        var O = u(493),
          H = u.n(O);
        const z = (e = 1) => {
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
        };
        var W = u(364);
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
        function V(e) {
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
        const $ = (e, t, u = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: W.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                u,
              ),
            );
          },
          U = (e) => {
            let t = e.children,
              u = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              o = e.onMouseLeave,
              s = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              d = e.ignoreMouseClick,
              _ = void 0 !== d && d,
              m = e.decoratorId,
              E = void 0 === m ? 0 : m,
              A = e.isEnabled,
              g = void 0 === A || A,
              p = e.targetId,
              h = void 0 === p ? 0 : p,
              C = e.onShow,
              F = e.onHide,
              D = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, G);
            const B = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              v = (0, a.useMemo)(() => h || z().resId, [h]),
              b = (0, a.useCallback)(() => {
                (B.current.isVisible && B.current.timeoutId) ||
                  ($(u, E, { isMouseEvent: !0, on: !0, arguments: V(n) }, v),
                  C && C(),
                  (B.current.isVisible = !0));
              }, [u, E, n, v, C]),
              f = (0, a.useCallback)(() => {
                if (B.current.isVisible || B.current.timeoutId) {
                  const e = B.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (B.current.timeoutId = 0)),
                    $(u, E, { on: !1 }, v),
                    B.current.isVisible && F && F(),
                    (B.current.isVisible = !1));
                }
              }, [u, E, v, F]),
              y = (0, a.useCallback)((e) => {
                B.current.isVisible &&
                  ((B.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (B.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(B.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = B.current.hideTimerId;
              return (
                document.addEventListener("wheel", y, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", y, { capture: !0 }),
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
                            ((B.current.timeoutId = window.setTimeout(b, c ? 100 : 400)),
                            r && r(e),
                            w && w(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (f(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === _ && f(), null == i || i(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === _ && f(), null == s || s(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    D,
                  ),
                )
              : t;
            var w;
          },
          j = ["children"];
        function X() {
          return (
            (X =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            X.apply(this, arguments)
          );
        }
        const q = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, j);
            return o().createElement(
              U,
              X(
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
          },
          Y = ["children", "body", "header", "note", "alert", "args"];
        function K() {
          return (
            (K =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            K.apply(this, arguments)
          );
        }
        const Z = R.views.common.tooltip_window.simple_tooltip_content,
          Q = (e) => {
            let t = e.children,
              u = e.body,
              n = e.header,
              r = e.note,
              s = e.alert,
              i = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Y);
            const c = (0, a.useMemo)(() => {
              const e = Object.assign({}, i, { body: u, header: n, note: r, alert: s });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [s, u, n, r, i]);
            return o().createElement(
              U,
              K(
                {
                  contentId:
                    ((d = null == i ? void 0 : i.hasHtmlContent),
                    d ? Z.SimpleTooltipHtmlContent("resId") : Z.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var d;
          };
        function J() {
          return (
            (J =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            J.apply(this, arguments)
          );
        }
        const ee = ({ children: e, tooltipArgs: t, className: u }) => {
            if (!t) return e;
            const n = o().createElement("div", { className: u }, e);
            if (t.header || t.body) return o().createElement(Q, t, n);
            const r = t.contentId,
              a = t.args,
              s = null == a ? void 0 : a.contentId;
            return r || s
              ? o().createElement(U, J({}, t, { contentId: r || s }), n)
              : o().createElement(q, t, n);
          },
          te = (e) => {
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
        function ue() {}
        function ne(e) {
          return e;
        }
        function re() {
          return !1;
        }
        console.log;
        function ae(e, t, u, n) {
          let r,
            a = !1,
            o = 0;
          function s() {
            r && clearTimeout(r);
          }
          function i(...i) {
            const l = this,
              c = Date.now() - o;
            function d() {
              ((o = Date.now()), u.apply(l, i));
            }
            a ||
              (n && !r && d(),
              s(),
              void 0 === n && c > e
                ? d()
                : !0 !== t &&
                  (r = setTimeout(
                    n
                      ? function () {
                          r = void 0;
                        }
                      : d,
                    void 0 === n ? e - c : e,
                  )));
          }
          return (
            "boolean" != typeof t && ((n = u), (u = t), (t = void 0)),
            (i.cancel = function () {
              (s(), (a = !0));
            }),
            i
          );
        }
        function oe(e, t, u) {
          const n = (0, a.useMemo)(
            () =>
              (function (e, t, u) {
                return void 0 === u ? ae(e, t, !1) : ae(e, u, !1 !== t);
              })(u, e),
            t,
          );
          return ((0, a.useEffect)(() => n.cancel, [n]), n);
        }
        var se = u(521);
        const ie = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function le(e = se.n.NONE, t = ie, u = !1) {
          (0, a.useEffect)(() => {
            if (e !== se.n.NONE)
              return (
                window.addEventListener("keydown", n, u),
                () => {
                  window.removeEventListener("keydown", n, u);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), t(n), u && n.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        const ce = () => {
            const e = (0, a.useState)(i.O.view.getScale()),
              t = e[0],
              u = e[1];
            return (
              (0, a.useEffect)(() => {
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
          de = (e, t) => e.split(".").reduce((e, t) => e && e[t], t),
          _e = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          me = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          Ee = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, u) => {
                const n = de(`${e}.${u}`, window);
                return _e(n) ? t(e, u, n) : `${e}.${u}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          Ae = (e) => {
            const t = ((e) => {
                const t = z(),
                  u = t.caller,
                  n = t.resId,
                  r = window.__feature && window.__feature !== u && u ? `subViews.${u}` : "";
                return { modelPrefix: r, modelPath: me(r, e || ""), resId: n };
              })(),
              u = t.modelPrefix,
              n = e.split(".");
            if (n.length > 0) {
              const e = [n[0]];
              return (
                n.reduce((t, n) => {
                  const r = de(me(u, `${t}.${n}`), window);
                  return _e(r) ? (e.push(r.id), `${t}.${n}.value`) : (e.push(n), `${t}.${n}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          ge = W.Sw.instance;
        let pe;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(pe || (pe = {}));
        const he = (e = "model", t = pe.Deep) => {
            const u = (0, a.useState)(0),
              n = (u[0], u[1]),
              r = (0, a.useMemo)(() => z(), []),
              o = r.caller,
              s = r.resId,
              i = (0, a.useMemo)(
                () => (window.__feature && window.__feature !== o ? `subViews.${o}.${e}` : e),
                [o, e],
              ),
              l = (0, a.useState)(() =>
                ((e) => {
                  const t = de(e, window);
                  for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                  return _e(t) ? t.value : t;
                })(Ee(i)),
              ),
              c = l[0],
              d = l[1],
              _ = (0, a.useRef)(-1);
            return (
              C(() => {
                if (
                  ("boolean" == typeof t &&
                    ((t = t ? pe.Deep : pe.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  t !== pe.None)
                ) {
                  const u = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      t === pe.Deep
                        ? (e === c && n((e) => e + 1), d(e))
                        : d(Object.assign([], e));
                    },
                    r = Ae(e);
                  _.current = ge.addCallback(r, u, s, t === pe.Deep);
                }
              }),
              (0, a.useEffect)(() => {
                if (t !== pe.None)
                  return () => {
                    ge.removeCallback(_.current, s);
                  };
              }, [s, t]),
              c
            );
          },
          Ce = "display",
          Fe = "enabled",
          De = "visible_change",
          Be = "enabled_change",
          ve = De,
          be = (e, t) => {
            const u = he("tutorialModel.triggers.items").filter((u) => {
              if (!u) return !1;
              const n = u.value,
                r = n.triggers.filter((e) => e.value === t);
              return n.componentId === e && r.length > 0;
            });
            if (0 === u.length) return null;
            if (!window.tutorialModel.foundComponents.items.some((t) => t.value.componentId === e))
              return null;
            return {
              trigger: u[0].value,
              runTrigger: (u) => {
                window.tutorialModel.onTriggerActivated({
                  componentId: e,
                  triggerType: t,
                  state: u,
                });
              },
            };
          };
        function fe(e) {
          engine.call("PlaySound", e);
        }
        const ye = {
          playHighlight() {
            fe("highlight");
          },
          playClick() {
            fe("play");
          },
          playYes() {
            fe("yes1");
          },
        };
        var we = u(403),
          Pe = u(30);
        let Ne;
        !(function (e) {
          ((e.BlueprintsConvert = "BlueprintsTechtreeConvertButtonHint"),
            (e.TechTreeAction = "TechTreeActionStartNodeHint"));
        })(Ne || (Ne = {}));
        var Se = u(174);
        function Te(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Le(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return Le(e, t);
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
        function Le(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const Re = (e) => (0 === e ? window : window.subViews.get(e));
        function ke(e, t) {
          var u;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (u = e[t]) ? void 0 : u.value;
        }
        function xe(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function Ie(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, u, n) => t(null == e ? void 0 : e.value, u, n));
        }
        function Me(e, t) {
          if (Array.isArray(e)) return e.filter(t);
          const u = [];
          for (let r = 0; r < e.length; r++) {
            var n;
            const a = null == (n = e[r]) ? void 0 : n.value;
            t(a, r, e) && u.push(a);
          }
          return u;
        }
        function Oe(e, t) {
          for (let u = 0; u < e.length; u++) {
            const n = xe(e[u]);
            if (t(n, u, e)) return n;
          }
        }
        const He = (e) =>
          null !== e && "object" == typeof e
            ? "CoherentArrayProxy" === e.constructor.name
              ? Ie(e, (e) => ("object" == typeof e ? He(e) : e))
              : Array.isArray(e)
                ? e.map((e) => ("object" == typeof e ? He(e) : e))
                : Object.fromEntries(
                    Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? He(t) : t]),
                  )
            : e;
        var ze = u(946);
        const We = (e) => (2 & e) > 0,
          Ge = (e) => (4 & e) > 0,
          Ve = (e) => (256 & e) > 0,
          $e = (e) => 0 == (256 & e),
          Ue = (e) => (1073741824 & e) > 0,
          je = (e) => (536870912 & e) > 0,
          Xe = (e) => (4 & e) > 0;
        let qe, Ye, Ke;
        (!(function (e) {
          ((e.CONVERT = "convert-hint"), (e.IN_BATTLE = "in-battle-hint"));
        })(qe || (qe = {})),
          (function (e) {
            ((e.LEFT_TO_RIGHT = "leftToRight"), (e.RIGHT_TO_LEFT = "rightToLeft"));
          })(Ye || (Ye = {})),
          (function (e) {
            ((e.PLAYING = "playing"), (e.STOPPED = "stopped"), (e.DEFAULT = "default"));
          })(Ke || (Ke = {})));
        const Ze = ((e, t) => {
            const u = (0, a.createContext)({});
            return [
              function ({ mode: n = "real", options: r, children: s, mocks: l }) {
                const c = (0, a.useRef)([]),
                  d = (u, n, r) => {
                    var a;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: u = Re,
                        context: n = "model",
                      } = {}) {
                        const r = new Map();
                        function a(e, t = 0) {
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
                            a = n.split(".").reduce((e, t) => e[t], r);
                          return "string" != typeof e || 0 === e.length
                            ? a
                            : e.split(".").reduce((e, t) => {
                                const u = e[t];
                                return "function" == typeof u ? u.bind(e) : u;
                              }, a);
                        };
                        return {
                          subscribe: (u, a) => {
                            const s = "string" == typeof a ? `${n}.${a}` : n,
                              l = i.O.view.addModelObserver(s, t, !0);
                            return (r.set(l, u), e && u(o(a)), l);
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
                            for (var e, u = Te(r.keys()); !(e = u()).done;) a(e.value, t);
                          },
                          unsubscribe: a,
                        };
                      })(n),
                      s =
                        "real" === u
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (a = null == r ? void 0 : r.getter) ? a : () => {},
                            }),
                      l = (e) =>
                        "mocks" === u ? (null == r ? void 0 : r.getter(e)) : s.readByPath(e),
                      d = (e) => c.current.push(e),
                      _ = e({
                        mode: u,
                        readByPath: l,
                        externalModel: s,
                        observableModel: {
                          array: (e, t) => {
                            const n = null != t ? t : l(e),
                              r = Se.LO.box(n, { equals: re });
                            return (
                              "real" === u &&
                                s.subscribe(
                                  (0, Se.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, t) => {
                            const n = null != t ? t : l(e),
                              r = Se.LO.box(n, { equals: re });
                            return (
                              "real" === u &&
                                s.subscribe(
                                  (0, Se.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, t) => {
                            const n = l(t);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, t) => ((e[t] = Se.LO.box(n[t], {})), e), {});
                              return (
                                "real" === u &&
                                  s.subscribe(
                                    (0, Se.aD)((t) => {
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
                                a = Object.entries(r),
                                o = a.reduce((e, [t, u]) => ((e[u] = Se.LO.box(n[t], {})), e), {});
                              return (
                                "real" === u &&
                                  s.subscribe(
                                    (0, Se.aD)((e) => {
                                      a.forEach(([t, u]) => {
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
                        cleanup: d,
                      }),
                      m = { mode: u, model: _, externalModel: s, cleanup: d };
                    return {
                      model: _,
                      controls: "mocks" === u && r ? r.controls(m) : t(m),
                      externalModel: s,
                      mode: u,
                    };
                  },
                  _ = (0, a.useRef)(!1),
                  m = (0, a.useState)(n),
                  E = m[0],
                  A = m[1],
                  g = (0, a.useState)(() => d(n, r, l)),
                  p = g[0],
                  h = g[1];
                return (
                  (0, a.useEffect)(() => {
                    _.current ? h(d(E, r, l)) : (_.current = !0);
                  }, [l, E, r]),
                  (0, a.useEffect)(() => {
                    A(n);
                  }, [n]),
                  (0, a.useEffect)(
                    () => () => {
                      (p.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [p],
                  ),
                  o().createElement(u.Provider, { value: p }, s)
                );
              },
              () => (0, a.useContext)(u),
            ];
          })(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  paragonsEntryPoint: e.array("paragonsEntryPoint"),
                  settings: e.object("settings"),
                  nodes: e.array("nodes"),
                  hints: e.array("hints"),
                  nodesRelation: e.array("nodesRelation"),
                  techTreeButtons: e.array("techTreeButtons"),
                  vehiclesData: e.array("vehiclesData"),
                  selectedNation: e.primitives(["selectedNation"]),
                  availableNations: e.array("availableNations"),
                  paragonsUnlockedBranchesToShow: e.array("paragonsUnlockedBranchesToShow"),
                  isEarlyAccessButtonHovered: Se.LO.box(!1),
                  isOnView: Se.LO.box(!0),
                  isNeedParagonsBrightness: Se.LO.box(!1),
                  paragonsHoveredNodes: Se.LO.box([]),
                  paragonsResetNodes: Se.LO.box([]),
                  paragonsResetAnimationStatus: Se.LO.box(Ke.DEFAULT),
                  paragonsLockedAnimationStatus: Se.LO.box(Ke.DEFAULT),
                  hintProperties: Se.LO.box({
                    [qe.CONVERT]: { direction: Ye.LEFT_TO_RIGHT, isInView: !0 },
                    [qe.IN_BATTLE]: { direction: Ye.LEFT_TO_RIGHT, isInView: !0 },
                  }),
                },
                u = (0, ze.Om)(
                  () =>
                    Ie(t.techTreeButtons.get(), (e) =>
                      Object.assign({}, e, { vehiclesCDs: Ie(e.vehiclesCDs, ne) }),
                    ),
                  { equals: re },
                ),
                n = (0, ze.Om)(
                  () => {
                    return ((e = t.nodes.get()), He(e));
                    var e;
                  },
                  { equals: re },
                ),
                r = (0, ze.Om)(() => Ie(t.hints.get().activeHints, (e) => Object.assign({}, e)), {
                  equals: re,
                }),
                a = (0, ze.Om)(() => r().find((e) => e.hintID === Ne.BlueprintsConvert)),
                o = (0, ze.Om)(() => r().find((e) => e.hintID === Ne.TechTreeAction)),
                s = (0, ze.Om)(() => Me(n(), (e) => $e(e.state)), { equals: re }),
                i = (0, ze.Om)(() => Me(n(), (e) => (2 & e.extendedState) > 0), { equals: re }),
                l = (0, ze.Om)(
                  (e) =>
                    Boolean(
                      Me(t.paragonsUnlockedBranchesToShow.get(), (t) =>
                        Ie(t.unlockedVehicleCDs, ne).includes(e),
                      ).length,
                    ),
                  { equals: re },
                ),
                c = (0, ze.Om)(
                  () => {
                    const e = ke(t.paragonsUnlockedBranchesToShow.get(), 0);
                    return e
                      ? Object.assign({}, e, { unlockedVehicleCDs: Ie(e.unlockedVehicleCDs, ne) })
                      : null;
                  },
                  { equals: re },
                ),
                d = (0, ze.Om)(() => Me(n(), (e) => Ue(e.state)), { equals: re }),
                _ = (0, ze.Om)(() => Oe(n(), (e) => e.blueprintCanConvert), { equals: re }),
                m = (0, ze.Om)(() => Me(n(), (e) => Ve(e.state)), { equals: re }),
                E = (0, ze.Om)((e) => Me(n(), (t) => t.row === e && $e(t.state)), { equals: re }),
                A = (0, ze.Om)(() => Oe(n(), (e) => 1 === e.column), { equals: re }),
                g = (0, ze.Om)((e) => Me(t.nodesRelation.get(), (t) => t.nodeOutId === e), {
                  equals: re,
                }),
                p = (0, ze.Om)((e) => Oe(n(), (t) => t.id === e), { equals: re }),
                h = (0, ze.Om)(() => Ie(t.availableNations.get(), ne), { equals: re }),
                C = (0, ze.Om)(() => t.vehiclesData.get(), { equals: re }),
                F = (0, ze.Om)(
                  (e) => {
                    var t, u, n, r, a, o, s;
                    const i = Oe(C(), (t) => t.nodeId === e);
                    return i
                      ? {
                          buyPrice:
                            null == (t = i.price.price[0]) || null == (u = t.value)
                              ? void 0
                              : u.value,
                          buyDiscount:
                            null == (n = i.price.discount[0]) || null == (r = n.value)
                              ? void 0
                              : r.value,
                          unlockPrice:
                            null == (a = i.unlock.xpCost.price[0].value) ? void 0 : a.value,
                          unlockDiscount:
                            null == (o = i.unlock.xpCost.discount[0]) || null == (s = o.value)
                              ? void 0
                              : s.value,
                          vehicleType: i.vehicleType,
                          vehicleNation: i.vehicleNation,
                          vehicleTechName: i.vehicleTechName,
                          isElite: i.isElite,
                          vehicleLvl: i.vehicleLvl,
                          vehicleCD: i.vehicleCD,
                          vehicleName: i.vehicleName,
                        }
                      : null;
                  },
                  { equals: re },
                ),
                D = (0, ze.Om)(
                  () =>
                    Me(t.availableNations.get(), (e) => e.hasNewDiscountEvent).map((e) => e.nation),
                  { equals: re },
                ),
                B = (0, ze.Om)(() => s().filter((e) => je(e.state)), { equals: re }),
                v = (0, ze.Om)(
                  () => {
                    var e;
                    return (null == (e = B()[0]) ? void 0 : e.column) - 1;
                  },
                  { equals: re },
                ),
                b = (0, ze.Om)(() => B().map((e) => ({ id: e.id, index: e.column - v() }))),
                f = (0, ze.Om)(
                  () => {
                    const e = b();
                    return e && e.length ? e[0].id : void 0;
                  },
                  { equals: re },
                ),
                y = (0, ze.Om)(
                  () => {
                    const e = b();
                    return e && e.length ? e[e.length - 1].id : void 0;
                  },
                  { equals: re },
                ),
                w = (0, ze.Om)(
                  () => {
                    const e = d();
                    return e && e.length ? e[0].id : void 0;
                  },
                  { equals: re },
                ),
                P = (0, ze.Om)(
                  () => {
                    const e = d();
                    return e && e.length ? e[e.length - 1].id : void 0;
                  },
                  { equals: re },
                ),
                N = (0, ze.Om)(
                  () => {
                    const e = t.paragonsResetNodes.get();
                    return e && e.length ? e[0] : void 0;
                  },
                  { equals: re },
                ),
                S = (0, ze.Om)(
                  () => {
                    const e = t.paragonsResetNodes.get();
                    return e && e.length ? e[e.length - 1] : void 0;
                  },
                  { equals: re },
                ),
                T = (0, ze.Om)(
                  () => {
                    const e = c();
                    if (e && e.unlockedVehicleCDs && e.unlockedVehicleCDs.length)
                      return e.unlockedVehicleCDs[0];
                  },
                  { equals: re },
                ),
                L = (0, ze.Om)(
                  () => {
                    const e = c();
                    if (e && e.unlockedVehicleCDs && e.unlockedVehicleCDs.length)
                      return e.unlockedVehicleCDs[e.unlockedVehicleCDs.length - 1];
                  },
                  { equals: re },
                ),
                R = (0, ze.Om)(() => t.paragonsEntryPoint.get().currentChapter, { equals: re }),
                k = (0, ze.Om)(
                  () => Ie(R().levels, (e) => Object.assign({}, e, { rewards: Ie(e.rewards, ne) })),
                  { equals: re },
                ),
                x = (0, ze.Om)(() => k().length, { equals: re }),
                I = (0, ze.Om)(
                  () => {
                    var e;
                    return null == (e = k()[x() - 1]) ? void 0 : e.maxPoints;
                  },
                  { equals: re },
                ),
                M = (0, ze.Om)(() => t.paragonsEntryPoint.get().freePoints, { equals: re });
              return Object.assign({}, t, {
                computes: {
                  getNodes: n,
                  getAvailableNations: h,
                  getFirstNode: A,
                  getMainNodes: s,
                  getPremiumNodes: m,
                  getRowData: E,
                  getNodeById: p,
                  getNodeConnectors: g,
                  getVehicles: C,
                  getVehicleByNodeId: F,
                  getEarlyAccessNodes: d,
                  getParagonsResetNodes: i,
                  getInBattleNations: D,
                  getFirstNodeWithAddBlueprintButton: _,
                  getHints: r,
                  getBlueprintConvertHint: a,
                  getTreeActionHint: o,
                  getFormattedInBattleNodes: b,
                  getFirstEarlyAccessNodeId: w,
                  getLastEarlyAccessNodeId: P,
                  getFirstInBattleNodeId: f,
                  getLastInBattleNodeId: y,
                  getFirstParagonsResetNodeId: N,
                  getLastParagonsResetNodeId: S,
                  getIsUnlockedNode: l,
                  getParagonsUnlockedBranchToShow: c,
                  getFirstParagonsUnLockedNodeId: T,
                  getLastParagonsUnLockedNodeId: L,
                  getRowButtons: u,
                  paragonsEntryPointComputes: {
                    getLevelsCount: x,
                    getMaxPointsCount: I,
                    getLevels: k,
                    getCurrentChapter: R,
                    getFreePoints: M,
                  },
                },
              });
            },
            ({ externalModel: e, model: t }) => ({
              onNationChange: e.createCallback((e) => ({ nationName: e }), "onNationChange"),
              onAddVehicleToCompare: e.createCallback(
                (e) => ({ vehicleCD: e }),
                "addVehicleToCompare",
              ),
              onBuyVehicle: e.createCallback((e) => ({ vehicleCD: e }), "buyVehicle"),
              onUnlockVehicle: e.createCallback((e) => ({ vehicleCD: e }), "unlockVehicle"),
              onGoToCollectionVehicle: e.createCallback(
                (e) => ({ nationName: e }),
                "goToCollectionVehicle",
              ),
              onGoToModulesTechTree: e.createCallback(
                (e) => ({ vehicleCD: e }),
                "goToModulesTechTree",
              ),
              onGoToBlueprintView: e.createCallback((e) => ({ vehicleCD: e }), "goToBlueprintView"),
              onGoToEarlyAccess: e.createCallbackNoArgs("goToEarlyAccess"),
              setEarlyAccessButtonHovered: (0, Se.aD)((e) => {
                t.isEarlyAccessButtonHovered.set(e);
              }),
              setIsOnView: (0, Se.aD)((e) => {
                t.isOnView.set(e);
              }),
              setParagonsResetAnimationStatus: (0, Se.aD)((e) => {
                t.paragonsResetAnimationStatus.set(e);
              }),
              setParagonsLockedAnimationStatus: (0, Se.aD)((e) => {
                t.paragonsLockedAnimationStatus.set(e);
              }),
              setIsNeedParagonsBrightness: (0, Se.aD)((e) => {
                t.isNeedParagonsBrightness.set(e);
              }),
              setParagonsHoveredNodes: (0, Se.aD)((e) => {
                t.paragonsHoveredNodes.set(e);
              }),
              setParagonsResetNodes: (0, Se.aD)((e) => {
                t.paragonsResetNodes.set(e);
              }),
              setHintConvertProperties: (0, Se.aD)((e) => {
                t.hintProperties.set(
                  Object.assign({}, t.hintProperties.get(), {
                    [qe.CONVERT]: Object.assign({}, t.hintProperties.get()[qe.IN_BATTLE], e),
                  }),
                );
              }),
              setHintInBattleProperties: (0, Se.aD)((e) => {
                t.hintProperties.set(
                  Object.assign({}, t.hintProperties.get(), {
                    [qe.IN_BATTLE]: Object.assign({}, t.hintProperties.get()[qe.IN_BATTLE], e),
                  }),
                );
              }),
              onBlueprintModeChanged: e.createCallback(
                (e) => ({ isEnabled: e }),
                "onBlueprintModeChanged",
              ),
              onClose: e.createCallbackNoArgs("onClose"),
              onHintClick: e.createCallback((e) => ({ hintID: e }), "hints.onHintShown"),
              onTechTreeButtonPressed: e.createCallback(
                (e, t) => ({ buttonType: e, branchID: t }),
                "onTechTreeButtonPressed",
              ),
              onResetBranchShown: e.createCallbackNoArgs("onResetBranchShown"),
              onParagonsUnlockedBranchShown: e.createCallback(
                (e) => ({ paragonsUnlockID: e }),
                "onParagonsUnlockedBranchShown",
              ),
              onEntryPointClick: e.createCallbackNoArgs("paragonsEntryPoint.onEntryPointClick"),
            }),
          ),
          Qe = Ze[0],
          Je = Ze[1],
          et = "App_base_3e",
          tt = "App_premiumPanelWrapper_2b",
          ut = "App_premiumPanelWrapper__active_47",
          nt = "App_premiumPanelWrapper__effects_fa",
          rt = "App_premiumPanelWrapper__noScroll_92",
          at = "App_treeContainer_b0",
          ot = "App_treeHolder_23",
          st = "App_treeHolder__withRightPadding_f0",
          it = "App_blueprintIcon_41",
          lt = "App_tabs_93",
          ct = "App_tabs__dragging_e1",
          dt = "App_scrollHolderHorizontal_5c",
          _t = "App_scrollHolderVertical_a9",
          mt = "App_scrollHolderVertical__withoutBottom_45",
          Et = "App_scrollHolderVertical__hidden_af",
          At = "App_verticalContent_8e",
          gt = "App_verticalContent__withPremiumPanel_78",
          pt = "App_verticalContent__withVerticalScrollBar_40",
          ht = "App_mainLine_37",
          Ct = "App_rowButtons_18",
          Ft = "App_rowButtonsContainer_85",
          Dt = "App_blueprintBalance_4d",
          Bt = "App_nationTitle_f4",
          vt = "App_base__blueprints_fd",
          bt = "App_paragonsEntryPoint_ce",
          ft = "App_levels_01",
          yt = "App_levels__witButtons_78",
          wt = "App_background_9f",
          Pt = "Background_base_7e",
          Nt = "Background_blueprints_aa",
          St = "Background_blueprints__active_ac",
          Tt = "Background_blueprintsGrid_da",
          Lt = "Background_blueprintsGrid__scale_2f",
          Rt = (0, a.memo)(({ isBlueprintMode: e }) => {
            const t = ce();
            return o().createElement(
              "div",
              { className: Pt },
              o().createElement(
                "div",
                { className: B()(Nt, e && St) },
                o().createElement("div", { className: B()(Tt, 2 === t && Lt) }),
              ),
            );
          });
        var kt = u(887),
          xt = u.n(kt);
        const It = ["xl", "lg", "md", "sm", "xs"],
          Mt = (e) => e.includes("_") && ((e) => It.includes(e))(e.split("_").at(-1)),
          Ot = [f.ExtraLarge, f.Large, f.Medium, f.Small, f.ExtraSmall],
          Ht = (e, t) =>
            Object.keys(e).reduce((u, n) => {
              if (n in u) return u;
              if (Mt(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in u) return u;
                const a = Ot.indexOf(t),
                  o = (-1 !== a ? It.slice(a) : [])
                    .map((e) => r + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  s = o ? e[o] : void 0;
                return ((u[r] = void 0 !== s ? s : e[r]), u);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, t) => It.some((u) => void 0 !== t[`${e}_${u}`]))(n, e) ||
                  (u[n] = r),
                u
              );
            }, {}),
          zt = (e, t = Ht) => {
            const u = (
              (e, t = Ht) =>
              (u) => {
                const n = P().mediaSize,
                  r = (0, a.useMemo)(() => t(u, n), [u, n]);
                return o().createElement(e, r);
              }
            )(e, t);
            return o().memo((t) =>
              Object.keys(t).some((e) => Mt(e) && void 0 !== t[e])
                ? o().createElement(u, t)
                : o().createElement(e, t),
            );
          },
          Wt = {
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
          Gt = [
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
        function Vt() {
          return (
            (Vt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Vt.apply(this, arguments)
          );
        }
        Object.keys(xt());
        const $t = {
            XL: { mt: Wt.mt__XL, mr: Wt.mr__XL, mb: Wt.mb__XL, ml: Wt.ml__XL },
            LG: { mt: Wt.mt__LG, mr: Wt.mr__LG, mb: Wt.mb__LG, ml: Wt.ml__LG },
            MDp: { mt: Wt.mt__MDp, mr: Wt.mr__MDp, mb: Wt.mb__MDp, ml: Wt.ml__MDp },
            MD: { mt: Wt.mt__MD, mr: Wt.mr__MD, mb: Wt.mb__MD, ml: Wt.ml__MD },
            SMp: { mt: Wt.mt__SMp, mr: Wt.mr__SMp, mb: Wt.mb__SMp, ml: Wt.ml__SMp },
            SM: { mt: Wt.mt__SM, mr: Wt.mr__SM, mb: Wt.mb__SM, ml: Wt.ml__SM },
            XS: { mt: Wt.mt__XS, mr: Wt.mr__XS, mb: Wt.mb__XS, ml: Wt.ml__XS },
          },
          Ut = (Object.keys($t), ["mt", "mr", "mb", "ml"]),
          jt = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Xt = zt((e) => {
            let t = e.className,
              u = e.width,
              n = e.height,
              r = e.m,
              s = e.mt,
              i = void 0 === s ? r : s,
              l = e.mr,
              c = void 0 === l ? r : l,
              d = e.mb,
              _ = void 0 === d ? r : d,
              m = e.ml,
              E = void 0 === m ? r : m,
              A = e.column,
              g = e.row,
              p = e.flexDirection,
              h = void 0 === p ? (A ? "column" : g && "row") || void 0 : p,
              C = e.flexStart,
              F = e.center,
              D = e.flexEnd,
              v = e.spaceBetween,
              b = e.spaceAround,
              f = e.justifyContent,
              y =
                void 0 === f
                  ? (C ? "flex-start" : F && "center") ||
                    (D && "flex-end") ||
                    (v && "space-between") ||
                    (b && "space-around") ||
                    void 0
                  : f,
              w = e.alignItems,
              P =
                void 0 === w
                  ? (C ? "flex-start" : F && "center") || (D && "flex-end") || void 0
                  : w,
              N = e.alignSelf,
              S = e.wrap,
              T = e.flexWrap,
              L = void 0 === T ? (S ? "wrap" : void 0) : T,
              R = e.grow,
              k = e.shrink,
              x = e.flex,
              I = void 0 === x ? (R || k ? `${R ? 1 : 0} ${k ? 1 : 0} auto` : void 0) : x,
              M = e.style,
              O = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Gt);
            const z = (0, a.useMemo)(() => {
                const e = { mt: i, mr: c, mb: _, ml: E },
                  t = ((e) =>
                    Ut.reduce((t, u) => {
                      const n = e[u];
                      return n && "number" != typeof n ? t.concat($t[!0 === n ? "MD" : n][u]) : t;
                    }, []))(e),
                  r = ((e) =>
                    Ut.reduce((t, u) => {
                      const n = e[u];
                      return ("number" == typeof n && (t[jt[u]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, M, r, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: I,
                    alignSelf: N,
                    display: h || P ? "flex" : void 0,
                    flexDirection: h,
                    flexWrap: L,
                    justifyContent: y,
                    alignItems: P,
                  }),
                  computedClassNames: t,
                };
              }, [u, n, i, c, _, E, M, I, N, h, L, y, P]),
              W = z.computedStyle,
              G = z.computedClassNames;
            return o().createElement(
              "div",
              Vt({ className: B()(Wt.base, ...G, t), style: W }, H),
              O,
            );
          });
        let qt;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(qt || (qt = {}));
        const Yt = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          Kt = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          Zt = (e, t, u = qt.left) => e.split(t).reduce(u === qt.left ? Yt : Kt, []),
          Qt = (() => {
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
          Jt = ["zh_cn", "zh_sg", "zh_tw"],
          eu = (e, t = qt.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Jt.includes(u)
              ? Qt(e)
              : ((e, t = qt.left) => {
                  let u = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (Zt(r, /( )/, t).forEach((e) => (u = u.concat(Zt(e, n, qt.left)))), u);
                })(e, t);
          },
          tu = "FormatText_base_d0",
          uu = ({ binding: e, text: t = "", classMix: u, alignment: n = qt.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  a.Fragment,
                  null,
                  t.split("\n").map((t, r) =>
                    o().createElement(
                      "div",
                      { className: B()(tu, u), key: `${t}-${r}` },
                      ((e, t, u) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (u && e in u ? u[e] : eu(e, t))))(t, n, e).map((e, t) =>
                        o().createElement(a.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var nu = u(532),
          ru = u.n(nu);
        const au = {
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
          ou = [
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
        function su() {
          return (
            (su =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            su.apply(this, arguments)
          );
        }
        Object.keys(xt());
        const iu = Object.keys(ru()),
          lu = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          cu = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          du = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          _u = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          mu =
            (Object.keys(_u),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": lu,
              "heading-H36": lu,
              "heading-H28": cu,
              "heading-H24": cu,
              "heading-H24R": cu,
              "heading-H22": cu,
              "heading-H20R": cu,
              "heading-H18": cu,
              "heading-H15": du,
              "heading-H14": du,
              "paragraph-P24": cu,
              "paragraph-P18": cu,
              "paragraph-P16": cu,
              "paragraph-P14": du,
              "paragraph-P12": du,
              "paragraph-P10": du,
            }),
          Eu =
            (Object.keys(mu),
            (e) =>
              e
                ? ((e) => iu.includes(e))(e)
                  ? { colorClassName: au[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Au = zt((e) => {
            let t = e.text,
              u = e.variant,
              n = e.className,
              r = e.color,
              s = e.m,
              i = e.mt,
              l = void 0 === i ? s : i,
              c = e.mr,
              d = void 0 === c ? s : c,
              _ = e.mb,
              m = void 0 === _ ? s : _,
              E = e.ml,
              A = void 0 === E ? s : E,
              g = e.style,
              p = e.format,
              h = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, ou);
            const C = (0, a.useMemo)(() => {
                const e = Eu(r),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  n = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, g, n), colorClassName: t };
              }, [g, r]),
              F = C.computedStyle,
              D = C.colorClassName;
            return o().createElement(
              Xt,
              su(
                {
                  className: B()(au.base, u && au[u], D, n),
                  style: F,
                  mt: !0 === l ? mu[u || "paragraph-P16"].mt : l,
                  mr: !0 === d ? mu[u || "paragraph-P16"].mr : d,
                  mb: !0 === m ? mu[u || "paragraph-P16"].mb : m,
                  ml: !0 === A ? mu[u || "paragraph-P16"].ml : A,
                },
                h,
              ),
              void 0 !== p ? o().createElement(uu, su({}, p, { text: t })) : t,
            );
          }),
          gu = "blueprintFragmentInfo",
          pu = "BlueprintBalance_base_e5",
          hu = "BlueprintBalance_text_2e",
          Cu = "BlueprintBalance_amountWithFlag_70",
          Fu = "BlueprintBalance_amount_5b",
          Du = "BlueprintBalance_icon_2d",
          Bu = "BlueprintBalance_icon__national_48",
          vu = (0, a.memo)(
            ({ nationBlueprintsCount: e, universalBlueprintsCount: t, nation: u }) => {
              const n = `url(R.images.gui.maps.icons.blueprints.fragment.special.${u})`;
              return o().createElement(
                "div",
                { className: pu },
                o().createElement(Au, {
                  className: hu,
                  text: R.strings.techtree.vehicle_tree.header.blueprintBalance(),
                }),
                o().createElement(
                  ee,
                  { tooltipArgs: { args: { tooltipId: gu, isUniversal: !0 } } },
                  o().createElement(
                    "div",
                    { className: Cu },
                    o().createElement("div", { className: Du }),
                    o().createElement(Au, {
                      className: Fu,
                      text: String(W.Z5.getNumberFormat(t, W.B3.INTEGRAL)),
                    }),
                  ),
                ),
                o().createElement(
                  ee,
                  { tooltipArgs: { args: { tooltipId: gu } } },
                  o().createElement(
                    "div",
                    { className: Cu },
                    o().createElement("div", {
                      className: B()(Du, Bu),
                      style: { backgroundImage: n },
                    }),
                    o().createElement(Au, {
                      className: Fu,
                      text: String(W.Z5.getNumberFormat(e, W.B3.INTEGRAL)),
                    }),
                  ),
                ),
              );
            },
          ),
          bu = 33,
          fu = 0,
          yu = !0,
          wu = "play";
        const Pu = [
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
        function Nu() {
          return (
            (Nu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Nu.apply(this, arguments)
          );
        }
        const Su = (0, a.memo)(function (e) {
            let t = e.width,
              u = e.height,
              n = e.getImageSource,
              r = e.frameCount,
              s = e.onAnimate,
              i = e.frameTime,
              l = void 0 === i ? bu : i,
              c = e.initialFrameIndex,
              d = void 0 === c ? fu : c,
              _ = e.lastFrameIndex,
              m = void 0 === _ ? r - 1 : _,
              E = e.loop,
              A = void 0 === E ? yu : E,
              g = e.state,
              p = void 0 === g ? wu : g,
              h = e.onAnimationDone,
              C = e.onAnimationComplete,
              F = e.poster,
              D = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Pu);
            const B = (0, a.useRef)(null);
            return (
              (0, a.useEffect)(() => {
                const e = B.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  u = (u) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(u.img, -u.x, -u.y));
                  };
                switch (p) {
                  case "play":
                    return (function () {
                      const e = Ru(d, m, n),
                        t = Tu(d, m),
                        r = window.setInterval(() => {
                          const n = t(),
                            a = e.get(n);
                          a
                            ? (null == s || s(n, a),
                              u(a),
                              n === m &&
                                (null == C || C(),
                                A || (null == h || h(), window.clearInterval(r))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, l);
                      return () => window.clearInterval(r);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === d && F ? { path: F, x: 0, y: 0 } : n(d),
                        t = new Image();
                      t.src = e.path;
                      const r = () => u(Lu(e, t));
                      return (
                        t.addEventListener("load", r),
                        () => t.removeEventListener("load", r)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [l, n, d, m, A, s, C, h, F, p]),
              o().createElement("canvas", Nu({}, D, { width: t, height: u, ref: B }))
            );
          }),
          Tu = (e, t) => {
            let u = e;
            return () => {
              const n = u;
              return ((u += 1), u > t && (u = e), n);
            };
          },
          Lu = (e, t) => Object.assign({}, e, { img: t }),
          Ru = (e, t, u) => {
            const n = new Map(),
              r = {};
            for (let a = e; a <= t; a++) {
              const e = u(a),
                t = r[e.path];
              if (t) n.set(a, Lu(e, t));
              else {
                const t = new Image();
                ((r[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${a})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  n.set(a, Lu(e, t)));
              }
            }
            return n;
          };
        function ku(e) {
          return (t) => `${e}${t}`;
        }
        const xu = "BlueprintSwitcher_base_b6",
          Iu = "BlueprintSwitcher_base__disabled_bb",
          Mu = "BlueprintSwitcher_hintBody_9f",
          Ou = "BlueprintSwitcher_icon_5d",
          Hu = "BlueprintSwitcher_sequence_d4",
          zu = "BlueprintSwitcher_glow_f8",
          Wu = "BlueprintSwitcher_glow__toBlueprintMode_7c";
        var Gu;
        !(function (e) {
          ((e.PLAY = "play"), (e.STOP = "stop"));
        })(Gu || (Gu = {}));
        const Vu = R.strings.techtree.vehicle_tree.header,
          $u = "R.images.gui.maps.icons.techtree.researchTree.blueprintsHeader.switcher",
          Uu = (0, a.memo)(({ isBlueprintMode: e, isBlueprintModeEnabled: t, onClick: u }) => {
            const n = (0, a.useState)(!0),
              r = n[0],
              s = n[1],
              i = (0, a.useState)(!1),
              l = i[0],
              c = i[1],
              d = (0, a.useState)(!1),
              _ = d[0],
              m = d[1],
              E = (0, a.useState)(!e),
              A = E[0],
              g = E[1],
              p = ((e) => ({
                width: 80,
                height: 80,
                frameCount: 11,
                chunk: { count: 1, columns: 11, rows: 1 },
                getChunkPath: ku(
                  e ? `${$u}.bp_frames_to_blueprints_` : `${$u}.bp_frames_to_common_`,
                ),
              }))(A),
              h = (function (e) {
                const t = e.chunk,
                  u = t.rows * t.columns;
                return (n) => {
                  const r = n % u,
                    a = (r % t.columns) * e.width,
                    o = Math.trunc(r / t.columns) * e.height;
                  return { path: e.getChunkPath(Math.trunc(n / u)), x: a, y: o };
                };
              })(p),
              C = be("BlueprintsSwitchButton", Be);
            (0, a.useEffect)(() => {
              C && C.runTrigger(!0);
            }, [C]);
            const F = t ? Vu.blueprintsSwitchTooltip() : Vu.blueprintsSwitchTooltipDisabled();
            (0, a.useEffect)(() => {
              (m(e), r || c(!0));
            }, [e, r]);
            const D = (0, a.useCallback)(() => {
              (g(!e), c(!1));
            }, [e]);
            return o().createElement(
              "div",
              { className: B()(xu, !t && Iu) },
              o().createElement("div", { className: B()(zu, _ && Wu) }),
              o().createElement("div", { className: Mu, id: "blueprint-switcher" }),
              o().createElement(
                "div",
                {
                  className: Ou,
                  onClick: () => {
                    !l && t && (s(!1), u());
                  },
                },
                o().createElement(
                  Q,
                  { body: F },
                  o().createElement(Su, {
                    frameTime: 15,
                    state: l ? Gu.PLAY : Gu.STOP,
                    width: p.width,
                    height: p.height,
                    frameCount: p.frameCount,
                    className: Hu,
                    getImageSource: h,
                    onAnimationDone: D,
                    loop: !1,
                  }),
                ),
              ),
            );
          }),
          ju = "Levels_base_e6",
          Xu = "Levels_levelNumberWrapper_d0",
          qu = "Levels_levelNumberWrapper__lastColumn_30",
          Yu = "Levels_levelNumber_72",
          Ku = "Levels_levelNumber__active_32",
          Zu = "Levels_levelDividers_8a",
          Qu = "Levels_levelDivider_7d",
          Ju = (0, a.memo)(({ activeLevel: e, className: t = "", levels: u }) =>
            o().createElement(
              "div",
              { className: B()(ju, t) },
              u.map((t) =>
                o().createElement(
                  "div",
                  { className: B()(Xu, t === u.length && qu), key: `nodes-column-level-${t}` },
                  o().createElement("div", {
                    className: B()(Yu, e === t && Ku),
                    style: {
                      backgroundImage: `url('R.images.gui.maps.icons.techtree.researchTree.levels.l${t}')`,
                    },
                  }),
                  t !== u.length &&
                    o().createElement(
                      "div",
                      { className: Zu },
                      o().createElement("div", { className: Qu }),
                      o().createElement("div", { className: Qu }),
                      o().createElement("div", { className: Qu }),
                      o().createElement("div", { className: Qu }),
                    ),
                ),
              ),
            ),
          );
        let en;
        !(function (e) {
          ((e.UP = "up"), (e.DOWN = "down"), (e.STRAIGHT = "straight"));
        })(en || (en = {}));
        const tn = "TreeCell_base_e4",
          un = "TreeCell_base__premium_87",
          nn = "TreeCell_premiumBackground_50",
          rn = "TreeCell_base__premiumLastColumn_bf",
          an = "TreeCell_base__premiumLastRow_b2",
          on = (0, a.memo)(
            ({ children: e, isPremiumCell: t, isPremiumLastRow: u, isPremiumLastColumn: n }) =>
              o().createElement(
                "div",
                { className: B()(tn, t && un, u && an, n && rn) },
                t && o().createElement("div", { className: nn }),
                e,
              ),
          ),
          sn = "TreeColumn_base_c8",
          ln = "TreeColumn_base__withVerticalScrollBar_06",
          cn = "TreeColumn_base__lastColumn_75",
          dn = "TreeColumn_base__dragging_1e",
          _n = (0, a.memo)(
            ({ children: e, isVerticalScrollBarShown: t, isLastColumn: u, isDragging: n }) =>
              o().createElement("div", { className: B()(sn, t && ln, u && cn, n && dn) }, e),
          );
        let mn;
        !(function (e) {
          ((e[(e.horizontal = 0)] = "horizontal"),
            (e[(e.vertical = 1)] = "vertical"),
            (e[(e.H_V = 2)] = "H_V"));
        })(mn || (mn = {}));
        const En = "HorizontalConnector_base_8e",
          An = "HorizontalConnector_connector_b4",
          gn = "HorizontalConnector_connector__down_ba",
          pn = "HorizontalConnector_connector__withPadding_18",
          hn = "HorizontalConnector_part_93",
          Cn = "HorizontalConnector_part__line_2d",
          Fn = "HorizontalConnector_base__dashed_37",
          Dn = "HorizontalConnector_base__thick_38",
          Bn = "HorizontalConnector_base__inBattle_f0",
          vn = "HorizontalConnector_base__blueprint_ca",
          bn = "HorizontalConnector_base__earlyAccess_2f",
          fn = "HorizontalConnector_base__paragonsReadyToReset_48",
          yn = "HorizontalConnector_part__vertical_55",
          wn = "HorizontalConnector_part__start_ed",
          Pn = "HorizontalConnector_part__middle_07",
          Nn = "HorizontalConnector_part__end_c7",
          Sn = "HorizontalConnector_part__straight_4b",
          Tn = "HorizontalConnector_part__arrow_97",
          Ln = (0, a.memo)(
            ({
              direction: e,
              size: t,
              isThick: u,
              isDashed: n,
              isBlueprint: r,
              isEarlyAccess: a,
              isInBattle: s,
              isParagonsReadyToReset: i,
            }) => {
              const l = e === en.UP,
                c = e === en.DOWN,
                d = e === en.STRAIGHT;
              return o().createElement(
                "div",
                {
                  className: B()(En, u && Dn, n && Fn, r && vn, a && bn, s && Bn, i && fn),
                  style: { "--size": t },
                },
                (l || c) &&
                  o().createElement(
                    "div",
                    { className: B()(An, c && gn) },
                    o().createElement("div", { className: B()(hn, Cn, wn) }),
                    o().createElement("div", { className: B()(hn, Cn, yn, Pn) }),
                    o().createElement("div", { className: B()(hn, Cn, Nn) }),
                    o().createElement("div", { className: B()(hn, Tn) }),
                  ),
                d &&
                  o().createElement(
                    "div",
                    { className: B()(An, pn) },
                    o().createElement("div", { className: B()(hn, Cn, Sn) }),
                    o().createElement("div", { className: B()(hn, Tn) }),
                  ),
              );
            },
          ),
          Rn = "HorizontalVerticalConnector_base_01",
          kn = "HorizontalVerticalConnector_connector_29",
          xn = "HorizontalVerticalConnector_connector__down_10",
          In = "HorizontalVerticalConnector_part_b9",
          Mn = "HorizontalVerticalConnector_part__line_9e",
          On = "HorizontalVerticalConnector_base__dashed_02",
          Hn = "HorizontalVerticalConnector_base__thick_90",
          zn = "HorizontalVerticalConnector_base__inBattle_9e",
          Wn = "HorizontalVerticalConnector_base__blueprint_b8",
          Gn = "HorizontalVerticalConnector_base__earlyAccess_cd",
          Vn = "HorizontalVerticalConnector_base__paragonsReadyToReset_64",
          $n = "HorizontalVerticalConnector_part__vertical_fa",
          Un = "HorizontalVerticalConnector_part__start_94",
          jn = "HorizontalVerticalConnector_part__end_42",
          Xn = "HorizontalVerticalConnector_part__arrow_06",
          qn = (0, a.memo)(
            ({
              direction: e,
              size: t,
              isThick: u,
              isDashed: n,
              isBlueprint: r,
              isEarlyAccess: a,
              isInBattle: s,
              isParagonsReadyToReset: i,
            }) => {
              const l = e === en.DOWN;
              return o().createElement(
                "div",
                {
                  className: B()(Rn, u && Hn, n && On, r && Wn, a && Gn, s && zn, i && Vn),
                  style: { "--size": t },
                },
                o().createElement(
                  "div",
                  { className: B()(kn, l && xn) },
                  o().createElement("div", { className: B()(In, Mn, Un) }),
                  o().createElement("div", { className: B()(In, Mn, $n, jn) }),
                  o().createElement("div", { className: B()(In, Xn) }),
                ),
              );
            },
          ),
          Yn = "VerticalConnector_base_8d",
          Kn = "VerticalConnector_connector_4b",
          Zn = "VerticalConnector_connector__down_14",
          Qn = "VerticalConnector_part_bd",
          Jn = "VerticalConnector_part__line_2c",
          er = "VerticalConnector_base__dashed_12",
          tr = "VerticalConnector_base__thick_1a",
          ur = "VerticalConnector_base__inBattle_b8",
          nr = "VerticalConnector_base__blueprint_38",
          rr = "VerticalConnector_base__earlyAccess_79",
          ar = "VerticalConnector_base__paragonsReadyToReset_f2",
          or = "VerticalConnector_part__straight_59",
          sr = "VerticalConnector_part__arrow_e5",
          ir = (0, a.memo)(
            ({
              direction: e,
              size: t,
              isThick: u,
              isDashed: n,
              isBlueprint: r,
              isEarlyAccess: a,
              isInBattle: s,
              isParagonsReadyToReset: i,
            }) => {
              const l = e === en.DOWN;
              return o().createElement(
                "div",
                {
                  className: B()(Yn, u && tr, n && er, r && nr, a && rr, s && ur, i && ar),
                  style: { "--size": t },
                },
                o().createElement(
                  "div",
                  { className: B()(Kn, l && Zn) },
                  o().createElement("div", { className: B()(Qn, Jn, or) }),
                  o().createElement("div", { className: B()(Qn, sr) }),
                ),
              );
            },
          ),
          lr = "TreeConnectors_base_a6",
          cr = "TreeConnectors_connectorWrapper_5b",
          dr = "TreeConnectors_connectorWrapper__thick_47",
          _r = "TreeConnectors_connectorWrapper__custom_d8",
          mr = (0, a.memo)(({ connectors: e, isBlueprintMode: t }) => {
            const u = (0, a.useCallback)(
              (e) => {
                switch (e.lineType) {
                  case mn.horizontal:
                    return o().createElement(Ln, {
                      direction: e.direction,
                      size: e.length,
                      isThick: e.isThick,
                      isDashed: e.isDashed,
                      isBlueprint: t,
                      isEarlyAccess: e.isEarlyAccessConnector,
                      isInBattle: e.isInBattleConnector,
                      isParagonsReadyToReset: e.isParagonsReadyToResetConnector,
                    });
                  case mn.vertical:
                    return o().createElement(ir, {
                      direction: e.direction,
                      size: e.length,
                      isThick: e.isThick,
                      isDashed: e.isDashed,
                      isBlueprint: t,
                      isEarlyAccess: e.isEarlyAccessConnector,
                      isInBattle: e.isInBattleConnector,
                      isParagonsReadyToReset: e.isParagonsReadyToResetConnector,
                    });
                  case mn.H_V:
                    return o().createElement(qn, {
                      direction: e.direction,
                      size: e.length,
                      isThick: e.isThick,
                      isDashed: e.isDashed,
                      isBlueprint: t,
                      isEarlyAccess: e.isEarlyAccessConnector,
                      isInBattle: e.isInBattleConnector,
                      isParagonsReadyToReset: e.isParagonsReadyToResetConnector,
                    });
                }
              },
              [t],
            );
            return o().createElement(
              "div",
              { className: lr },
              e.map((e) =>
                o().createElement(
                  "div",
                  {
                    className: B()(
                      cr,
                      e.isThick && dr,
                      (e.isInBattleConnector ||
                        e.isEarlyAccessConnector ||
                        e.isParagonsReadyToResetConnector) &&
                        _r,
                    ),
                    key: `connector-${e.nodeInId}`,
                  },
                  u(e),
                ),
              ),
            );
          }),
          Er = {
            base: "Hint_base_b8",
            border: "Hint_border_80",
            base__hidden: "Hint_base__hidden_8b",
            hint: "Hint_hint_70",
            base__leftToRight: "Hint_base__leftToRight_9a",
            hintSubstrate: "Hint_hintSubstrate_e9",
            hintArrow: "Hint_hintArrow_0f",
            blink: "Hint_blink_7e",
            blinkLeftToRight: "Hint_blinkLeftToRight_93",
            hintText: "Hint_hintText_b9",
          },
          Ar = (0, a.memo)(
            ({
              id: e,
              className: t,
              isHidden: u = !1,
              text: n,
              isHideBorder: r = !1,
              properties: s,
            }) => {
              const i = s.isInView,
                l = s.direction,
                c = (0, a.useState)(!1),
                d = c[0],
                _ = c[1],
                m = B()(
                  Er.base,
                  (u || d) && Er.base__hidden,
                  t && t,
                  l === Ye.LEFT_TO_RIGHT && Er[`base__${Ye.LEFT_TO_RIGHT}`],
                );
              return o().createElement(
                "div",
                { className: m, id: e },
                !r && o().createElement("div", { className: Er.border }),
                o().createElement(
                  "div",
                  {
                    className: Er.hint,
                    onClick: () => {
                      d || _(!0);
                    },
                  },
                  o().createElement("div", { className: Er.hintSubstrate }),
                  o().createElement("div", {
                    className: B()(Er.hintArrow, !i && Er.hintArrow__notInView),
                  }),
                  o().createElement(Au, { text: n, className: Er.hintText }),
                ),
              );
            },
          ),
          gr = {
            base__blueprintConvert: "HintManager_base__blueprintConvert_4c",
            base__inBattle: "HintManager_base__inBattle_3c",
          },
          pr = (0, we.Pi)(({ nodeId: e }) => {
            var t;
            const u = Je().model,
              n = u.root.get(),
              r = n.selectedNation,
              a = n.isBlueprintMode,
              s = u.hintProperties.get(),
              i = u.computes,
              l = i.getInBattleNations,
              c = i.getFirstNodeWithAddBlueprintButton,
              d = i.getBlueprintConvertHint,
              _ = i.getTreeActionHint,
              m = l().includes(r),
              E = null == (t = c()) ? void 0 : t.id,
              A = d(),
              g = _(),
              p = s[qe.CONVERT],
              h = s[qe.IN_BATTLE];
            return a && E === e && A
              ? o().createElement(Ar, {
                  className: B()(gr.base, gr.base__blueprintConvert),
                  text: A.hintText,
                  id: qe.CONVERT,
                  properties: p,
                })
              : !a && m && g && g.nodeID === e
                ? o().createElement(
                    "div",
                    { id: qe.IN_BATTLE },
                    o().createElement(Ar, {
                      className: B()(gr.base, gr.base__inBattle),
                      text: g.hintText,
                      isHideBorder: !0,
                      id: qe.CONVERT,
                      properties: h,
                    }),
                  )
                : o().createElement(o().Fragment, null);
          });
        let hr;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(hr || (hr = {}));
        const Cr = ({
            children: e,
            contentID: t,
            decoratorID: u = 0,
            targetId: n = 0,
            args: r,
            isEnabled: o = !0,
            onMouseDown: s,
          }) => {
            const i = (0, a.useCallback)(() => {
                ((0, W.c9)(W.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: n,
                  isMouseEvent: !0,
                  on: !0,
                  args: r,
                }),
                  ye.playYes());
              }, [r, t, u, n]),
              l = (0, a.useCallback)(() => {
                (0, W.c9)(W.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: n,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, u, n]),
              c = (0, a.useCallback)(
                (e) => {
                  (s && s(e), ((e) => e.button === hr.RIGHT)(e) && i());
                },
                [s, i],
              );
            return (
              (0, a.useEffect)(() => {
                !1 === o && l();
              }, [o, l]),
              o ? (0, a.cloneElement)(e, { onMouseDown: c }) : e
            );
          },
          Fr = ["children"];
        function Dr() {
          return (
            (Dr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Dr.apply(this, arguments)
          );
        }
        const Br = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, Fr);
          return o().createElement(
            Cr,
            Dr({}, u, { contentID: R.views.common.BackportContextMenu("resId") }),
            t,
          );
        };
        let vr, br, fr;
        (!(function (e) {
          ((e.small = "small"),
            (e.big = "big"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(vr || (vr = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(br || (br = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(fr || (fr = {})));
        class yr extends o().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = W.B3.GOLD;
            else e = W.B3.INTEGRAL;
            const t = W.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        yr.defaultProps = { format: "integral" };
        const wr = {
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
          Pr = ({
            isDiscount: e,
            isInteractiveDiscount: t,
            size: u,
            type: n,
            isEnough: r,
            value: a,
            discountValue: s,
            showPlus: i,
            stockBackgroundName: l = fr.Red,
          }) => {
            const c = B()(wr.value, wr[`value__${n}`], !r && wr.value__notEnough),
              d = B()(wr.icon, wr[`icon__${n}-${u}`]),
              _ = B()(wr.stock, s && wr.stock__indent, t && wr.stock__interactive),
              m = i && a > 0 && "+",
              E = B()(wr.base, wr[`base__${u}`]);
            return o().createElement(
              "span",
              { className: E },
              o().createElement(
                "span",
                { className: c },
                m,
                o().createElement(yr, { value: a, format: n === br.gold ? "gold" : "integral" }),
              ),
              o().createElement("span", { className: d }),
              e &&
                o().createElement(
                  "span",
                  { className: _ },
                  o().createElement("span", {
                    className: wr.stockBackground,
                    style: { backgroundImage: `url(R.images.gui.maps.icons.library.${l})` },
                  }),
                  Boolean(s) && s,
                ),
            );
          };
        Pr.defaultProps = { isEnough: !0 };
        const Nr = o().memo(Pr);
        function Sr() {
          const e = (0, a.useRef)(0);
          var t;
          return (
            (t = () => {
              window.clearTimeout(e.current);
            }),
            (0, a.useEffect)(() => t, []),
            (0, a.useMemo)(
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
        const Tr = "ActionButton_base_8b",
          Lr = "ActionButton_base__scaled_c3",
          Rr = "ActionButton_base__buyGold_9b",
          kr = "ActionButton_base__buySilver_08",
          xr = "ActionButton_base__buyDisabled_83",
          Ir = "ActionButton_base__explore_ba",
          Mr = "ActionButton_base__exploreDisabled_41",
          Or = "ActionButton_actionButtonHover_ae",
          Hr = "ActionButton_actionButtonHover__visible_7d",
          zr = "ActionButton_recoveryText_c1",
          Wr = (0, we.Pi)(
            ({
              vehicleCD: e,
              buyPrice: t,
              explorePrice: u,
              isTop: n,
              isPremiumNode: r,
              isHovered: s,
              isBlueprintMode: i,
              isEnoughMoneyToBuy: l,
              isUnlockedNode: c,
              isAllNextUnlocked: d,
              isEnoughXpToUnlock: _,
              isAvailableToUnlockNode: m,
              isRecoveryEnableNode: E,
            }) => {
              const A = Je().controls,
                g = 2 === ce(),
                p = (0, Pe.useSpring)({
                  to: { opacity: n || !d || s ? 1 : 0 },
                  config: { duration: 150 },
                }),
                h = B()(
                  Tr,
                  g && Lr,
                  r && l && c && !i && Rr,
                  !r && l && c && !i && kr,
                  !l && c && !i && xr,
                  _ && m && Ir,
                  !_ && m && Mr,
                ),
                C = (0, a.useState)(!1),
                F = C[0],
                D = C[1];
              return o().createElement(
                Pe.animated.div,
                {
                  style: p,
                  className: h,
                  onMouseEnter: () => {
                    ((l && c) || (_ && m)) && (fe(R.sounds.highlight()), D(!0));
                  },
                  onMouseLeave: () => {
                    D(!1);
                  },
                  onClick: (t) => {
                    (t.stopPropagation(),
                      fe(R.sounds.play()),
                      l && c ? A.onBuyVehicle(e) : _ && m && A.onUnlockVehicle(e));
                  },
                },
                (!i || (_ && m)) && o().createElement("div", { className: B()(Or, F && Hr) }),
                c &&
                  !i &&
                  (E
                    ? o().createElement(Au, {
                        className: zr,
                        text: R.strings.techtree.vehicle_tree.actionButton.recovery(),
                      })
                    : o().createElement(Nr, {
                        size: vr.small,
                        type: r ? br.gold : br.credits,
                        value: t,
                      })),
                m && o().createElement(Nr, { size: vr.small, type: br.xp, value: u }),
              );
            },
          ),
          Gr = (0, a.memo)(Wr),
          Vr = "AddBluePrintButton_base_2b",
          $r = "AddBluePrintButton_hovered_5f",
          Ur = "AddBluePrintButton_hovered__visible_cb",
          jr = (0, a.memo)(({ onClick: e, nodeId: t }) => {
            const u = (0, a.useState)(!1),
              n = u[0],
              r = u[1];
            return o().createElement(
              ee,
              {
                tooltipArgs: { args: { tooltipId: "TOOLTIP_BLUEPRINT_CONVERT_COUNT", nodeId: t } },
              },
              o().createElement(
                "div",
                {
                  className: Vr,
                  onClick: e,
                  onMouseEnter: () => {
                    (fe(R.sounds.highlight()), r(!0));
                  },
                  onMouseLeave: () => {
                    r(!1);
                  },
                },
                o().createElement("div", { className: B()($r, n && Ur) }),
              ),
            );
          }),
          Xr = {
            base: "CompareButton_base_9e",
            base__hovered: "CompareButton_base__hovered_6a",
            compareButtonActiveZone: "CompareButton_compareButtonActiveZone_86",
          },
          qr = (0, we.Pi)(({ isHovered: e, vehicleCD: t }) => {
            const u = Je().controls,
              n = (0, a.useState)(!1),
              r = n[0],
              s = n[1],
              i = B()(Xr.base, !e && Xr.base__hidden, r && Xr.base__hovered);
            return o().createElement(
              Q,
              { body: R.strings.techtree.vehicle_tree.tank_node.compareButtonTooltip.body() },
              o().createElement("div", {
                className: i,
                onMouseEnter: () => {
                  (fe(R.sounds.highlight()), s(!0));
                },
                onMouseLeave: () => {
                  s(!1);
                },
                onClick: (e) => {
                  (e.stopPropagation(), fe(R.sounds.yes1()), u.onAddVehicleToCompare(t));
                },
              }),
            );
          }),
          Yr = (0, a.memo)(qr),
          Kr = "ParagonsLocked_base_4b",
          Zr = "ParagonsLocked_paragonsLocked_76",
          Qr = "ParagonsLocked_paragonsLocked__locked_95",
          Jr = "ParagonsLocked_paragonsLocked__animation_c8",
          ea = "ParagonsLocked_paragonsLockedIcon_3c",
          ta = "ParagonsLocked_paragonsLockedIcon__locked_62",
          ua = "ParagonsLocked_paragonsLockedIcon__animation_3d",
          na = (0, a.memo)(
            ({
              vehicleCD: e,
              isParagonsUnlockedBranchToShowNode: t,
              paragonsLockedAnimationStatus: u,
              setIsParagonsLockedIcons: n,
            }) =>
              o().createElement(
                "div",
                { className: Kr },
                o().createElement("div", {
                  className: B()(Zr, !t && Qr, t && u === Ke.STOPPED && Jr),
                  onAnimationEnd: () => n(!1),
                }),
                o().createElement(
                  U,
                  {
                    contentId: R.views.lobby.techtree.tooltips.ParagonsLockedTooltip("resId"),
                    args: { vehicleCD: e },
                  },
                  o().createElement("div", {
                    className: B()(ea, !t && ta, t && u === Ke.STOPPED && ua),
                    onAnimationEnd: () => n(!1),
                  }),
                ),
              ),
          ),
          ra = {
            base: "TreeNode_base_e4",
            base__brightness: "TreeNode_base__brightness_02",
            paragonsResetAnimation: "TreeNode_paragonsResetAnimation_35",
            background: "TreeNode_background_3a",
            background__locked: "TreeNode_background__locked_9a",
            background__unlocked: "TreeNode_background__unlocked_8f",
            background__inInventory: "TreeNode_background__inInventory_36",
            background__premium: "TreeNode_background__premium_04",
            background__paragonsReset: "TreeNode_background__paragonsReset_9d",
            background__paragonsResetLocked: "TreeNode_background__paragonsResetLocked_0e",
            blueprints: "TreeNode_blueprints_80",
            blueprints__availableToUnlock: "TreeNode_blueprints__availableToUnlock_3d",
            border: "TreeNode_border_72",
            border__blueprint: "TreeNode_border__blueprint_bc",
            border__blueprintScaled: "TreeNode_border__blueprintScaled_6b",
            border__earlyAccess: "TreeNode_border__earlyAccess_ec",
            border__earlyAccessLocked: "TreeNode_border__earlyAccessLocked_65",
            border__earlyAccessPaused: "TreeNode_border__earlyAccessPaused_cc",
            border__inBattle: "TreeNode_border__inBattle_ee",
            border__inBattleFirstEntry: "TreeNode_border__inBattleFirstEntry_2b",
            border__lockedParagonsReset: "TreeNode_border__lockedParagonsReset_c2",
            paragonsReadyToResetBorder: "TreeNode_paragonsReadyToResetBorder_1c",
            paragonsReadyToResetAnimation: "TreeNode_paragonsReadyToResetAnimation_69",
            paragonsVehicleCardShadow: "TreeNode_paragonsVehicleCardShadow_b3",
            hover: "TreeNode_hover_41",
            base__hovered: "TreeNode_base__hovered_f4",
            hover__earlyAccess: "TreeNode_hover__earlyAccess_94",
            hover__earlyAccessLocked: "TreeNode_hover__earlyAccessLocked_c4",
            hover__earlyAccessPaused: "TreeNode_hover__earlyAccessPaused_6b",
            earlyAccessMainButtonHover: "TreeNode_earlyAccessMainButtonHover_e2",
            earlyAccessMainButtonHover__visible: "TreeNode_earlyAccessMainButtonHover__visible_f7",
            actionButton: "TreeNode_actionButton_21",
            actionButton__hidden: "TreeNode_actionButton__hidden_c4",
            addBlueprintButtonContainer: "TreeNode_addBlueprintButtonContainer_db",
            content: "TreeNode_content_7c",
            title: "TreeNode_title_d9",
            base__gold: "TreeNode_base__gold_46",
            content__locked: "TreeNode_content__locked_46",
            vehicleLevel: "TreeNode_vehicleLevel_51",
            base__elite: "TreeNode_base__elite_2d",
            vehicleTypeWrapper: "TreeNode_vehicleTypeWrapper_23",
            vehicleType: "TreeNode_vehicleType_5f",
            vehicleType__lightTank: "TreeNode_vehicleType__lightTank_e4",
            vehicleType__mediumTank: "TreeNode_vehicleType__mediumTank_ba",
            vehicleType__heavyTank: "TreeNode_vehicleType__heavyTank_af",
            "vehicleType__AT-SPG": "TreeNode_vehicleType__AT-SPG_d7",
            vehicleType__SPG: "TreeNode_vehicleType__SPG_6a",
            vehicleIcon: "TreeNode_vehicleIcon_71",
            base__blueprint: "TreeNode_base__blueprint_8f",
            tradeIn: "TreeNode_tradeIn_84",
            inInventoryIcon: "TreeNode_inInventoryIcon_75",
            inInventoryIcon__rent: "TreeNode_inInventoryIcon__rent_37",
            inInventoryIcon__blueprint: "TreeNode_inInventoryIcon__blueprint_d2",
            earlyAccessLocked: "TreeNode_earlyAccessLocked_16",
            xpCost: "TreeNode_xpCost_e5",
            xpCost__discount: "TreeNode_xpCost__discount_f5",
            xpCost__earned: "TreeNode_xpCost__earned_ef",
            xpCost__earned__elite: "TreeNode_xpCost__earned__elite_0d",
            xpCost__hidden: "TreeNode_xpCost__hidden_c6",
            discount: "TreeNode_discount_61",
            discount__buy: "TreeNode_discount__buy_a4",
            discount__research: "TreeNode_discount__research_fe",
            discount__locked: "TreeNode_discount__locked_46",
            tokenBalance: "TreeNode_tokenBalance_cd",
            tokenBalance__earlyAccess: "TreeNode_tokenBalance__earlyAccess_a3",
            earlyAccessTokenIcon: "TreeNode_earlyAccessTokenIcon_58",
            compareButton: "TreeNode_compareButton_f1",
            earlyAccessGlowContainer: "TreeNode_earlyAccessGlowContainer_17",
            earlyAccessGlow: "TreeNode_earlyAccessGlow_a8",
          },
          aa = { lightTank: "lt", mediumTank: "st", heavyTank: "tt", SPG: "sau", "AT-SPG": "pt" },
          oa = R.images.gui.maps.icons.techtree.researchTree.node,
          sa = R.strings.techtree.vehicle_tree,
          ia = 300,
          la = "lastNode",
          ca = ({
            children: e,
            isParagonsLockedNode: t,
            vehicleCD: u,
            id: n,
            isBlueprintMode: r,
          }) =>
            t && r
              ? o().createElement(
                  U,
                  {
                    contentId: R.views.lobby.techtree.tooltips.ParagonsLockedTooltip("resId"),
                    args: { vehicleCD: u },
                  },
                  o().createElement("div", null, e),
                )
              : o().createElement(
                  ee,
                  {
                    tooltipArgs: {
                      args: {
                        tooltipId: r ? "TOOLTIP_BLUEPRINT" : "techtreeVehicleTooltip",
                        nodeId: n,
                      },
                    },
                  },
                  e,
                ),
          da = (0, we.Pi)(
            ({
              earnedXp: e,
              state: t,
              extendedState: u,
              id: n,
              vehicle: r,
              earlyAccessBalance: s,
              earlyAccessPrice: i,
              isAllNextUnlocked: l,
              blueprintConvertHint: c,
              isEarlyAccessBlocked: d,
              isBlueprintMode: _,
              blueprintMaxCount: m,
              blueprintBalance: E,
              canAddBlueprint: A,
              shouldInBattleShow: g,
              onMouseEnter: p,
              onMouseLeave: h,
            }) => {
              const C = Je(),
                F = C.model,
                D = C.controls,
                v = (0, a.useState)(!1),
                b = v[0],
                f = v[1],
                y = (0, a.useState)(!0),
                w = y[0],
                P = y[1],
                N = F.computes,
                S = N.getEarlyAccessNodes,
                T = N.getFormattedInBattleNodes,
                L = N.getFirstEarlyAccessNodeId,
                k = N.getLastEarlyAccessNodeId,
                x = N.getFirstInBattleNodeId,
                I = N.getLastInBattleNodeId,
                M = N.getParagonsResetNodes,
                O = N.getFirstParagonsResetNodeId,
                H = N.getLastParagonsResetNodeId,
                z = N.getParagonsUnlockedBranchToShow,
                W = N.getFirstParagonsUnLockedNodeId,
                G = N.getLastParagonsUnLockedNodeId,
                V = N.getIsUnlockedNode,
                $ = F.paragonsHoveredNodes.get(),
                U = F.paragonsResetAnimationStatus.get(),
                j = F.paragonsLockedAnimationStatus.get(),
                X = F.paragonsResetNodes.get(),
                q = F.isNeedParagonsBrightness.get(),
                Y = F.isEarlyAccessButtonHovered.get(),
                K = F.root.get(),
                Z = K.isEarlyAccessFirstTimeShown,
                Q = K.isEarlyAccessPaused,
                J = K.isParagonsResetBranchNeedToShow,
                ee = S(),
                te = T(),
                ue = M(),
                ne = z(),
                re = Ve(t),
                ae = ((e) => (128 & e) > 0)(t),
                oe = ((e) => (1 & e) > 0)(t),
                se = Ge(t),
                ie = ((e) => (32 & e) > 0)(t),
                le = We(t),
                de = ((e) => (16 & e) > 0)(t),
                _e = ((e) => (8 & e) > 0)(t),
                me = ((e) => (32768 & e) > 0)(t),
                Ee = ((e) => (2097152 & e) > 0)(t),
                Ae = Ue(t),
                ge = je(t),
                pe = ((e) => (262144 & e) > 0)(t),
                he = Xe(u),
                Ce = Boolean(null == ne ? void 0 : ne.unlockedVehicleCDs.includes(n)),
                Fe = V(n),
                De = Boolean(ue.find((e) => e.id === n)),
                Be = X.includes(n),
                ve = $.includes(n),
                be = Sr(),
                ye = Sr(),
                we = 2 === ce(),
                Pe = De && !_ && !le && !se && !Be,
                Ne = (De && (!_ || se)) || (Be && U === Ke.PLAYING),
                Se = (0, a.useMemo)(
                  () =>
                    B()(
                      ra.background,
                      oe && ra.background__locked,
                      se && ra.background__unlocked,
                      re && ra.background__premium,
                      ie && ra.background__inInventory,
                      !oe && _ && ra.background__blueprints,
                      Ne && ra.background__paragonsReset,
                      Pe && ra.background__paragonsResetLocked,
                    ),
                  [_, ie, oe, Ne, Pe, re, se],
                ),
                Te = aa[r.vehicleType],
                Le = Boolean(r.buyDiscount) && !ie,
                Re = Boolean(r.unlockDiscount) && !se,
                ke = Re || Le,
                xe = {
                  backgroundImage: r
                    ? `url(R.images.gui.maps.icons.vehicle.small.${((Ie = `${r.vehicleNation}-${r.vehicleTechName}`), Ie.replace(/-/g, "_"))})`
                    : void 0,
                };
              var Ie;
              const Me = {
                  backgroundImage: `url(${oa.vehicleTypeIcons.$dyn(`${Te}${r.isElite ? "_gold" : ""}${we ? "_x2" : ""}`)})`,
                },
                Oe = {
                  backgroundImage: `url(${oa.levels.$dyn(`c_${r.vehicleLvl}${we ? "_x2" : ""}`)})`,
                },
                He = B()(
                  ra.discount,
                  Le && ra.discount__buy,
                  Re && ra.discount__research,
                  oe && ra.discount__locked,
                ),
                ze = _ && De && !le && !se && !Be,
                $e = B()(
                  ra.border,
                  _ && le && ra.border__blueprint,
                  _ && le && we && ra.border__blueprintScaled,
                  Ae && ra.border__earlyAccess,
                  Ae && !se && ra.border__earlyAccessLocked,
                  Ae && Q && ra.border__earlyAccessPaused,
                  !_ && ge && ra.border__inBattle,
                  !_ && ge && g && ra.border__inBattleFirstEntry,
                  ze && ra.border__lockedParagonsReset,
                ),
                qe = B()(
                  ra.hover,
                  Ae && ra.hover__earlyAccess,
                  Ae && !se && ra.hover__earlyAccessLocked,
                  Ae && Q && ra.hover__earlyAccessPaused,
                ),
                Ye = ze || Pe || Ne,
                Ze = () => {
                  (p(), b || fe(R.sounds.highlight()), f(!0));
                },
                Qe = () => {
                  (h(), f(!1));
                },
                et = (E / m) * 100,
                tt = L(),
                ut = k(),
                nt = O(),
                rt = H(),
                at = W(),
                ot = G(),
                st = (0, a.useMemo)(
                  () => (Ae ? ee.findIndex((e) => e.id === n) * ia : 0),
                  [ee, Ae, n],
                ),
                it = (0, a.useMemo)(() => {
                  var e;
                  return ge
                    ? ((null == (e = te.find((e) => e.id === n)) ? void 0 : e.index) || 0) * ia
                    : 0;
                }, [te, ge, n]),
                lt = x(),
                ct = (0, a.useMemo)(
                  () => (De && Be ? X.findIndex((e) => e === n) * ia + 500 : 0),
                  [De, Be, X, n],
                ),
                dt = (0, a.useMemo)(
                  () => (Ce && ne ? ne.unlockedVehicleCDs.findIndex((e) => e === n) * ia + 1e3 : 0),
                  [Ce, ne, n],
                ),
                _t = I(),
                mt = !De || !Be || U !== Ke.DEFAULT;
              (0, a.useEffect)(
                () => () => {
                  (be.clear(), ye.clear());
                },
                [],
              );
              const Et = rt === n || ot === n ? la : String(n);
              return o().createElement(
                o().Fragment,
                null,
                !Ae &&
                  !he &&
                  A &&
                  _ &&
                  o().createElement(
                    "div",
                    { className: ra.addBlueprintButtonContainer },
                    o().createElement(jr, {
                      onClick: () => {
                        (fe(R.sounds.play()),
                          c && D.onHintClick(c.hintID),
                          D.onGoToBlueprintView(r.vehicleCD));
                      },
                      nodeId: n,
                    }),
                  ),
                !_ &&
                  o().createElement(
                    "div",
                    { className: ra.compareButton, onMouseEnter: Ze, onMouseLeave: Qe },
                    b && o().createElement(Yr, { isHovered: b, vehicleCD: r.vehicleCD }),
                  ),
                ((!ie && !oe && !Ae) || (Ae && se && !ie)) &&
                  mt &&
                  o().createElement(
                    "div",
                    {
                      className: B()(
                        ra.actionButton,
                        ((J && Be) || he || Ce) && ra.actionButton__hidden,
                      ),
                      onMouseEnter: Ze,
                      onMouseLeave: Qe,
                    },
                    o().createElement(Gr, {
                      vehicleCD: r.vehicleCD,
                      buyPrice: r.buyPrice,
                      explorePrice: r.unlockPrice,
                      isPremiumNode: re,
                      isTop: 10 === r.vehicleLvl,
                      isHovered: b,
                      isBlueprintMode: _,
                      isEnoughMoneyToBuy: de,
                      isUnlockedNode: se,
                      isAllNextUnlocked: l,
                      isEnoughXpToUnlock: _e,
                      isAvailableToUnlockNode: le,
                      isRecoveryEnableNode: pe,
                    }),
                  ),
                (he || Ce || Fe) &&
                  w &&
                  o().createElement(
                    "div",
                    { onMouseEnter: Ze, onMouseLeave: Qe },
                    o().createElement(na, {
                      vehicleCD: r.vehicleCD,
                      isParagonsUnlockedBranchToShowNode: Ce,
                      setIsParagonsLockedIcons: P,
                      paragonsLockedAnimationStatus: j,
                    }),
                  ),
                o().createElement(
                  ca,
                  { isParagonsLockedNode: he, isBlueprintMode: _, vehicleCD: r.vehicleCD, id: n },
                  o().createElement(
                    Br,
                    { args: { nodeId: n } },
                    o().createElement(
                      "div",
                      {
                        className: B()(
                          ra.base,
                          b && ra.base__hovered,
                          re && ra.base__gold,
                          _ && ra.base__blueprint,
                          ae && ra.base__elite,
                          Ae && ra.base__earlyAccess,
                          q && De && Be && ra.base__brightness,
                        ),
                        id: Et,
                        onMouseEnter: Ze,
                        onMouseLeave: Qe,
                        onClick: () => {
                          (fe(R.sounds.play()), D.onGoToModulesTechTree(r.vehicleCD));
                        },
                      },
                      o().createElement("div", { className: $e }),
                      o().createElement("div", { className: qe }),
                      Ae &&
                        o().createElement("div", {
                          className: B()(
                            ra.earlyAccessMainButtonHover,
                            Y && ra.earlyAccessMainButtonHover__visible,
                          ),
                        }),
                      ve && o().createElement("div", { className: ra.paragonsReadyToResetBorder }),
                      o().createElement("div", { className: Se }),
                      Ye && o().createElement("div", { className: ra.paragonsVehicleCardShadow }),
                      (oe || _e) &&
                        o().createElement("div", {
                          className: B()(ra.blueprints, _e && ra.blueprints__availableToUnlock),
                          style: _ ? { width: `${et}%` } : { width: "0%" },
                        }),
                      o().createElement(
                        "div",
                        { className: B()(ra.content, oe && (!Be || !J) && ra.content__locked) },
                        o().createElement("div", { className: ra.vehicleIcon, style: xe }),
                        o().createElement(Au, { className: ra.title, text: r.vehicleName }),
                        o().createElement(
                          "div",
                          { className: ra.vehicleTypeWrapper },
                          o().createElement("div", {
                            className: B()(ra.vehicleType, ra[`vehicleType__${r.vehicleType}`]),
                            style: Me,
                          }),
                          o().createElement("div", { className: ra.vehicleLevel, style: Oe }),
                        ),
                        o().createElement("div", { className: ra.discount }),
                        !_ && ke && o().createElement("div", { className: He }),
                        !Ae &&
                          oe &&
                          !_ &&
                          mt &&
                          o().createElement(
                            "div",
                            {
                              className: B()(
                                ra.xpCost,
                                ke && ra.xpCost__discount,
                                ((J && Be) || he || Ce) && ra.xpCost__hidden,
                              ),
                            },
                            o().createElement(Nr, {
                              size: vr.small,
                              type: br.xp,
                              value: Number(r.unlockPrice),
                            }),
                          ),
                        !pe &&
                          !oe &&
                          !_ &&
                          Boolean(e) &&
                          o().createElement(
                            "div",
                            {
                              className: B()(
                                ra.xpCost,
                                ra.xpCost__earned,
                                ke && ra.xpCost__discount,
                                ae && ra.xpCost__earned__elite,
                              ),
                            },
                            o().createElement(Nr, {
                              size: vr.small,
                              type: ae ? br.freeXP : br.xp,
                              value: e,
                            }),
                          ),
                        !Ae &&
                          !he &&
                          _ &&
                          o().createElement(Au, {
                            className: ra.tokenBalance,
                            text: sa.blueprints.node.tokenBalance(),
                            format: { binding: { earned: E, max: m } },
                          }),
                        Ae &&
                          !d &&
                          !se &&
                          o().createElement(
                            o().Fragment,
                            null,
                            o().createElement(Au, {
                              className: B()(ra.tokenBalance, Ae && ra.tokenBalance__earlyAccess),
                              text: oe ? String(i) : sa.blueprints.node.tokenBalance(),
                              format: { binding: { earned: s, max: i } },
                            }),
                            o().createElement("div", { className: ra.earlyAccessTokenIcon }),
                          ),
                      ),
                      (ie || (_ && se)) &&
                        o().createElement("div", {
                          className: B()(
                            ra.inInventoryIcon,
                            me && ra.inInventoryIcon__rent,
                            _ && ra.inInventoryIcon__blueprint,
                          ),
                        }),
                      Ee && o().createElement("div", { className: ra.tradeIn }),
                      d && o().createElement("div", { className: ra.earlyAccessLocked }),
                      ((!Q && Z && Ae) || (ge && g) || (Be && De && J) || Ce) &&
                        o().createElement(
                          "div",
                          { className: ra.earlyAccessGlowContainer },
                          o().createElement("div", {
                            className: ra.earlyAccessGlow,
                            style: { animationDelay: `${st || it || ct || dt}ms` },
                            onAnimationStart: () => {
                              ((Ae && n === tt) ||
                                (ge && n === lt) ||
                                (Be && De && n === nt) ||
                                (Ce && at === n)) &&
                                (Be &&
                                  De &&
                                  n === nt &&
                                  D.setParagonsResetAnimationStatus(Ke.PLAYING),
                                fe("researches_top_of_the_tree_start"));
                            },
                            onAnimationEnd: () => {
                              ((Ae && n === ut) ||
                                (ge && n === _t) ||
                                (Be && De && n === rt) ||
                                (Ce && ot === n)) &&
                                (fe("researches_top_of_the_tree_stop"),
                                fe("paragons_branch_successfully_reset"),
                                Be &&
                                  De &&
                                  n === rt &&
                                  (D.setIsNeedParagonsBrightness(!0),
                                  be.run(() => {
                                    (D.setParagonsResetAnimationStatus(Ke.STOPPED),
                                      D.onResetBranchShown(),
                                      D.setIsNeedParagonsBrightness(!1),
                                      D.setParagonsResetNodes([]));
                                  }, 700)),
                                Ce &&
                                  ot === n &&
                                  ne &&
                                  (D.setParagonsLockedAnimationStatus(Ke.STOPPED),
                                  ye.run(() => {
                                    (D.onParagonsUnlockedBranchShown(ne.paragonsUnlockID),
                                      D.setParagonsLockedAnimationStatus(Ke.DEFAULT));
                                  }, 700)));
                            },
                          }),
                        ),
                    ),
                  ),
                ),
              );
            },
          ),
          _a = {
            base: "TreeNodeHolder_base_5a",
            base__premiumEmpty: "TreeNodeHolder_base__premiumEmpty_07",
          },
          ma = (0, we.Pi)(
            ({
              columnIndex: e,
              isPremium: t,
              isAllNextUnlocked: u = !1,
              node: n,
              levels: r,
              onSetActiveLevel: a,
            }) => {
              const s = Je().model,
                i = s.root.get(),
                l = i.isBlueprintMode,
                c = i.earlyAccessCurrentTokens,
                d = i.selectedNation,
                _ = s.computes,
                m = _.getInBattleNations,
                E = _.getBlueprintConvertHint,
                A = _.getVehicleByNodeId;
              if (!n && t)
                return o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: B()(_a.base, _a.base__premiumEmpty) }),
                  e !== r.length && o().createElement("div", { className: _a.connectors }),
                );
              if (!n) return null;
              const g = A(n.id);
              if (!g) return null;
              const p = m().includes(d),
                h = E();
              return o().createElement(
                "div",
                {
                  id: "node-container",
                  "data-cd": g.vehicleCD,
                  "data-tech-name": g.vehicleTechName,
                  "data-is-premium": t,
                  "data-level": g.vehicleLvl,
                  "data-vehicle-type": g.vehicleType,
                },
                o().createElement(pr, { nodeId: n.id }),
                o().createElement(
                  "div",
                  { className: _a.base },
                  o().createElement(da, {
                    earnedXp: n.earnedXP,
                    state: n.state,
                    extendedState: n.extendedState,
                    id: n.id,
                    isAllNextUnlocked: u,
                    blueprintConvertHint: h,
                    isBlueprintMode: l,
                    vehicle: g,
                    isEarlyAccessBlocked: n.isEarlyAccessLocked,
                    canAddBlueprint: n.blueprintCanConvert,
                    blueprintBalance: n.blueprintBalance,
                    blueprintMaxCount: n.blueprintMaxCount,
                    earlyAccessBalance: c,
                    earlyAccessPrice: n.earlyAccessPrice,
                    shouldInBattleShow: p,
                    onMouseEnter: () => a(e),
                    onMouseLeave: () => a(0),
                  }),
                ),
              );
            },
          ),
          Ea = "MainNodesWithConnectors_connectors_06",
          Aa = (0, a.memo)(
            ({
              checkIsEmptyRow: e,
              columnIndex: t,
              isDragging: u,
              isVerticalScrollBarShown: n,
              levels: r,
              treeRows: a,
              mainNodes: s,
              shouldInBattleShow: i,
              setActiveLevel: l,
              getNodeById: c,
              getNodeConnectors: d,
              isEarlyAccessFirstTimeShown: _,
              isBlueprintMode: m,
              isEarlyAccessPaused: E,
              hoveredParagonsReadyToResetBranch: A,
              paragonsUnlockedBranchToShowNodes: g,
            }) =>
              o().createElement(
                _n,
                {
                  key: `nodes-column-${t}`,
                  isLastColumn: t === r.length,
                  isVerticalScrollBarShown: n,
                  isDragging: u,
                },
                o().createElement(
                  o().Fragment,
                  null,
                  a.map((u) => {
                    const n = s.find((e) => e.row === u && e.column === t),
                      a =
                        t !== r.length && n
                          ? ((e, t, u, n, r, a, o, s) =>
                              u(e.id).map((u) => {
                                const i = e,
                                  l = t(u.nodeInId);
                                let c = en.STRAIGHT,
                                  d = 0,
                                  _ = !1,
                                  m = !1,
                                  E = !1,
                                  A = !1,
                                  g = !1;
                                return (
                                  l &&
                                    ((_ =
                                      Ge(i.state) &&
                                      (Ge(l.state) || We(l.state)) &&
                                      (Ue(i.state) || !Ue(l.state))),
                                    (E = Ue(i.state) && Ue(l.state) && r),
                                    (m =
                                      (n ? Ue(i.state) && Ue(l.state) : l.isEarlyAccessLocked) ||
                                      Xe(l.extendedState) ||
                                      Boolean(null == s ? void 0 : s.includes(l.id))),
                                    (A = a && je(i.state) && je(l.state)),
                                    (g = o.includes(l.id) && o.includes(i.id)),
                                    i.row > l.row
                                      ? ((c = en.UP), (d = i.row - l.row))
                                      : i.row < l.row
                                        ? ((c = en.DOWN), (d = l.row - i.row))
                                        : ((c = en.STRAIGHT), (d = 0))),
                                  Object.assign({}, u, {
                                    direction: c,
                                    length: d,
                                    isThick: _,
                                    isDashed: m,
                                    isEarlyAccessConnector: E,
                                    isInBattleConnector: A,
                                    isParagonsReadyToResetConnector: g,
                                  })
                                );
                              }))(n, c, d, E, _, i, A, g)
                          : null,
                      p = !(null != a && a.some((e) => !e.isThick));
                    return (
                      e(u) &&
                      o().createElement(
                        on,
                        { key: `node-cell-${u}` },
                        o().createElement(
                          o().Fragment,
                          null,
                          o().createElement(ma, {
                            columnIndex: t,
                            isPremium: !1,
                            node: n,
                            levels: r,
                            isAllNextUnlocked: p,
                            onSetActiveLevel: l,
                          }),
                          a &&
                            o().createElement(
                              "div",
                              { className: Ea },
                              o().createElement(mr, { connectors: a, isBlueprintMode: m }),
                            ),
                        ),
                      )
                    );
                  }),
                ),
              ),
          );
        let ga;
        !(function (e) {
          ((e.Active = "active"),
            (e.ChapterNotChosen = "chapterNotChosen"),
            (e.NotAvailable = "notAvailable"),
            (e.AllChaptersCompleted = "allChaptersCompleted"),
            (e.Paused = "paused"));
        })(ga || (ga = {}));
        const pa = {
          base: "ProgressBar_base_45",
          base__medium: "ProgressBar_base__medium_62",
          base__small: "ProgressBar_base__small_df",
          background: "ProgressBar_background_51",
          background__medium: "ProgressBar_background__medium_6e",
          background__small: "ProgressBar_background__small_46",
          lineWrapper: "ProgressBar_lineWrapper_6a",
        };
        let ha, Ca;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(ha || (ha = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(Ca || (Ca = {})));
        const Fa = ({ size: e = ha.Default, classMix: t }) =>
            o().createElement("div", { className: B()(pa.background, pa[`background__${e}`], t) }),
          Da = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          Ba = ({ size: e }) => {
            const t = B()(Da.base, Da[`base__${e}`]);
            return o().createElement("div", { className: t });
          },
          va = {
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
          ba = (0, a.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: u,
              baseStyles: n,
              isComplete: r,
              withoutBounce: a,
            }) => {
              const s = B()(
                  va.base,
                  va[`base__${e}`],
                  u && va.base__disabled,
                  r && va.base__finished,
                  a && va.base__withoutBounce,
                ),
                i = !u && !r;
              return o().createElement(
                "div",
                { className: s, style: n, ref: t },
                o().createElement("div", { className: va.pattern }),
                o().createElement("div", { className: va.gradient }),
                i && o().createElement(Ba, { size: e }),
              );
            },
          ),
          fa = ({ size: e, value: t, lineRef: u, disabled: n, onComplete: r }) => {
            const s = (0, a.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              i = 100 === t;
            return (
              (0, a.useEffect)(() => {
                i && r && r();
              }, [i, r]),
              o().createElement(ba, {
                size: e,
                disabled: n,
                baseStyles: s,
                isComplete: i,
                lineRef: u,
              })
            );
          },
          ya = (e, t) => {
            let u;
            const n = setTimeout(() => {
              u = e();
            }, t);
            return () => {
              ("function" == typeof u && u(), clearTimeout(n));
            };
          };
        let wa, Pa;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(wa || (wa = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(Pa || (Pa = {})));
        const Na = "ProgressBarDeltaSimple_base_6c",
          Sa = "ProgressBarDeltaSimple_delta_99",
          Ta = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: n,
              size: r,
              to: s,
              onEndAnimation: i,
              onChangeAnimationState: l,
            }) => {
              const c = s < n,
                d = (0, a.useState)(Pa.Idle),
                _ = d[0],
                m = d[1],
                E = _ === Pa.In,
                A = _ === Pa.End,
                g = _ === Pa.Idle,
                p = (0, a.useCallback)(
                  (e) => {
                    (m(e), l && l(e));
                  },
                  [l],
                );
              ((0, a.useEffect)(() => {
                if (g && !u) {
                  return ya(() => {
                    p(Pa.In);
                  }, t);
                }
              }, [p, u, g, t]),
                (0, a.useEffect)(() => {
                  if (E) {
                    return ya(() => {
                      (i && i(), p(Pa.End));
                    }, e + t);
                  }
                }, [p, E, i, t, e]));
              const h = (0, a.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                C = (0, a.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                F = (0, a.useMemo)(
                  () => ({ width: `${Math.abs(n - s)}%`, left: `${c ? s : n}%` }),
                  [n, c, s],
                );
              return A
                ? null
                : o().createElement(
                    "div",
                    { className: Na, style: F },
                    o().createElement(
                      "div",
                      { style: g ? h : C, className: Sa },
                      o().createElement(Ba, { size: r }),
                    ),
                  );
            },
          ),
          La = (0, a.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: n,
              disabled: r,
              isComplete: s,
              animationSettings: i,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const d = (0, a.useMemo)(
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
                o().createElement(ba, {
                  size: t,
                  lineRef: n,
                  disabled: r,
                  isComplete: s,
                  baseStyles: d,
                }),
                u >= 0 &&
                  o().createElement(Ta, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    freezed: i.freezed,
                    from: u,
                    size: t,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          Ra = "ProgressBarDeltaGrow_base_7e",
          ka = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          xa = "ProgressBarDeltaGrow_glow_68",
          Ia = (e) => (e ? { left: 0 } : { right: 0 }),
          Ma = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          Oa = (e) => ({ transitionDuration: `${e}ms` }),
          Ha = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: n,
              size: r,
              to: s,
              onEndAnimation: i,
              onChangeAnimationState: l,
              className: c,
            }) => {
              const d = s < n,
                _ = (0, a.useState)(wa.Idle),
                m = _[0],
                E = _[1],
                A = m === wa.End,
                g = m === wa.Idle,
                p = m === wa.Grow,
                h = m === wa.Shrink,
                C = (0, a.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                ),
                F = (0, a.useCallback)(
                  (e, t) =>
                    ya(() => {
                      C(e);
                    }, t),
                  [C],
                );
              (0, a.useEffect)(() => {
                if (!u)
                  return g
                    ? F(wa.Grow, t)
                    : p
                      ? F(wa.Shrink, e)
                      : h
                        ? F(wa.End, e)
                        : void (A && i && i());
              }, [F, u, A, p, g, h, i, t, e]);
              const D = (0, a.useMemo)(
                  () => Object.assign({ width: "100%" }, Oa(e), Ia(d)),
                  [d, e],
                ),
                v = (0, a.useMemo)(() => Object.assign({ width: "0%" }, Oa(e), Ia(d)), [d, e]),
                b = (0, a.useMemo)(
                  () => Object.assign({ width: "0%" }, Ma(d, n), Oa(e)),
                  [n, d, e],
                ),
                f = (0, a.useMemo)(
                  () => Object.assign({ width: `${Math.abs(s - n)}%` }, Ma(d, n), Oa(e)),
                  [n, d, s, e],
                );
              if (A) return null;
              const y = B()(Ra, c, d && 0 === s && ka);
              return o().createElement(
                "div",
                { style: g ? b : f, className: y },
                o().createElement(
                  "div",
                  { style: h ? v : D, className: xa },
                  o().createElement(Ba, { size: r }),
                ),
              );
            },
          ),
          za = (0, a.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: n,
              disabled: r,
              isComplete: s,
              animationSettings: i,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const d = e < u,
                _ = (0, a.useState)(!1),
                m = _[0],
                E = _[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (e === wa.Shrink && E(!0), c && c(e));
                  },
                  [c],
                ),
                g = (0, a.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
                p = (0, a.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${i.line.duration}ms` }),
                  [i.line.duration, e],
                );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(ba, {
                  size: t,
                  lineRef: n,
                  disabled: r,
                  isComplete: s,
                  withoutBounce: d && 0 === e,
                  baseStyles: m ? p : g,
                }),
                u >= 0 &&
                  o().createElement(Ha, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    onChangeAnimationState: A,
                    freezed: i.freezed,
                    onEndAnimation: l,
                    from: u,
                    size: t,
                    to: e,
                    className: i.delta.className,
                  }),
              );
            },
          ),
          Wa = ["onComplete", "onEndAnimation"];
        function Ga() {
          return (
            (Ga =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ga.apply(this, arguments)
          );
        }
        const Va = (0, a.memo)((e) => {
            let t = e.onComplete,
              u = e.onEndAnimation,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Wa);
            const r = (0, a.useState)(!1),
              s = r[0],
              i = r[1],
              l = (0, a.useCallback)(() => {
                const e = 100 === n.to;
                (e !== s && i(e), e && t && t(), u && u());
              }, [s, t, u, n.to]);
            switch (n.animationSettings.type) {
              case Ca.Simple:
                return o().createElement(La, Ga({}, n, { onEndAnimation: l, isComplete: s }));
              case Ca.Growing:
                return o().createElement(za, Ga({}, n, { onEndAnimation: l, isComplete: s }));
              default:
                return null;
            }
          }),
          $a = ["onEndAnimation"];
        function Ua() {
          return (
            (Ua =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ua.apply(this, arguments)
          );
        }
        const ja = (0, a.memo)((e) => {
          let t = e.onEndAnimation,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
              return r;
            })(e, $a);
          const n = (0, a.useRef)({}),
            r = (0, a.useCallback)(() => {
              ((n.current.from = void 0), t && t());
            }, [t]),
            s = "number" == typeof n.current.from ? n.current.from : u.from;
          return (
            (n.current.from = s),
            o().createElement(Va, Ua({}, u, { onEndAnimation: r, key: `${s}-${u.to}`, from: s }))
          );
        });
        function Xa() {
          return (
            (Xa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Xa.apply(this, arguments)
          );
        }
        const qa = (0, a.memo)(
            ({
              size: e,
              value: t,
              lineRef: u,
              disabled: n,
              deltaFrom: r,
              animationSettings: a,
              onEndAnimation: s,
              onChangeAnimationState: i,
              onComplete: l,
            }) => {
              if (r === t)
                return o().createElement(fa, {
                  key: `${r}-${t}`,
                  size: e,
                  value: t,
                  lineRef: u,
                  disabled: n,
                  onComplete: l,
                });
              const c = {
                from: r,
                to: t,
                size: e,
                lineRef: u,
                disabled: n,
                animationSettings: a,
                onComplete: l,
                onEndAnimation: s,
                onChangeAnimationState: i,
              };
              return a.withStack
                ? o().createElement(ja, c)
                : o().createElement(Va, Xa({ key: `${r}-${t}` }, c));
            },
          ),
          Ya = (e) => ({
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
          Ka = (e, t, u) => (u < e ? e : u > t ? t : u),
          Za = (e, t, u) => {
            if ("number" == typeof u) {
              return (Ka(0, t, u) / t) * 100;
            }
            return e;
          },
          Qa = {
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
          Ja = {
            freezed: !1,
            withStack: !1,
            type: Ca.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          eo = (0, a.memo)(
            ({
              maxValue: e = 100,
              theme: t = Qa,
              size: u = ha.Default,
              animationSettings: n = Ja,
              disabled: r = !1,
              withoutBackground: s = !1,
              progressBarBackgroundClassMix: i,
              value: l,
              deltaFrom: c,
              lineRef: d,
              onChangeAnimationState: _,
              onEndAnimation: m,
              onComplete: E,
            }) => {
              const A = ((e, t, u) =>
                (0, a.useMemo)(() => {
                  const n = (Ka(0, t, e) / t) * 100;
                  return { value: n, deltaFrom: Za(n, t, u) };
                }, [u, t, e]))(l, e, c);
              return o().createElement(
                "div",
                { className: B()(pa.base, pa[`base__${u}`]), style: Ya(t) },
                !s && o().createElement(Fa, { size: u, classMix: i }),
                o().createElement(qa, {
                  size: u,
                  lineRef: d,
                  disabled: r,
                  value: A.value,
                  deltaFrom: A.deltaFrom,
                  animationSettings: n,
                  onEndAnimation: m,
                  onChangeAnimationState: _,
                  onComplete: E,
                }),
              );
            },
          ),
          to = Object.assign({}, Ja, {
            withStack: !0,
            type: Ca.Growing,
            delta: { duration: 400, delay: 300 },
            line: { duration: 400, delay: 300 },
          }),
          uo = "paragons_entry_point",
          no = 3e3,
          ro = 1500,
          ao = 5e3,
          oo = 6600,
          so = 18e3;
        let io, lo;
        (!(function (e) {
          ((e.FLIPPING = "flipping"), (e.FLIPPED = "flipped"));
        })(io || (io = {})),
          (function (e) {
            ((e.FLIPPED_TO_11 = "flippedTo11"), (e.FLIPPED_TO_PARAGONS = "flippedToParagons"));
          })(lo || (lo = {})));
        const co = "OptimizedProgressBar_base_1f",
          _o = "OptimizedProgressBar_wrapper_ab",
          mo = "OptimizedProgressBar_background_ce",
          Eo = ["api", "value", "maxValue", "theme"];
        function Ao() {
          return (
            (Ao =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ao.apply(this, arguments)
          );
        }
        const go = (e, t) => ("number" == typeof t ? t : e.offsetLeft),
          po = (e) => {
            let t = e.api,
              u = e.value,
              n = e.maxValue,
              r = void 0 === n ? 100 : n,
              s = e.theme,
              i = void 0 === s ? Qa : s,
              l = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((u = a[n]), t.indexOf(u) >= 0 || (r[u] = e[u]));
                return r;
              })(e, Eo);
            const c = (0, a.useRef)(null),
              d = (0, a.useRef)(null),
              _ = (0, a.useRef)(null),
              m = Ka(0, u, r) / r,
              E = (0, a.useCallback)(
                (e) => {
                  (_.current &&
                    c.current &&
                    (({ horizontalScrollPosition: e, leftOffset: t }, u, n) => {
                      const r = u.offsetWidth - n.offsetWidth,
                        a = e - go(u, t),
                        o = Ka(0, r, a);
                      n.style.left = `${o}px`;
                    })(e, c.current, _.current),
                    d.current &&
                      c.current &&
                      ((
                        { horizontalScrollPosition: e, leftOffset: t },
                        u,
                        { container: n, line: r },
                      ) => {
                        const a = Math.max(0, Math.floor(n.offsetWidth * u) - 8e3),
                          o = e - go(n, t),
                          s = Ka(0, a, o);
                        r.style.left = `${s}px`;
                      })(e, m, { line: d.current, container: c.current }));
                },
                [m],
              ),
              A = (0, a.useMemo)(() => Ya(i), [i]);
            return (
              (t.current.update = E),
              o().createElement(
                "div",
                { className: co, ref: c },
                o().createElement(
                  "div",
                  { className: _o },
                  o().createElement(
                    "div",
                    { style: A, className: B()(mo, l.progressBarBackgroundClassMix), ref: _ },
                    o().createElement(Fa, {
                      size: l.size,
                      classMix: l.progressBarBackgroundClassMix,
                    }),
                  ),
                  o().createElement(
                    eo,
                    Ao({}, l, {
                      lineRef: d,
                      value: u,
                      theme: i,
                      maxValue: r,
                      withoutBackground: !0,
                    }),
                  ),
                ),
              )
            );
          },
          ho = (e, t) => (t < 0 ? 0 : e[t].maxPoints),
          Co = (e, t, u) => {
            let n = 0;
            const r = ho(u, t - 2),
              a = ho(u, u.length - 1) / u.length;
            return (
              u.forEach((u, o) => {
                o < t &&
                  (n += ((e, t, u, n) => (e >= t ? n : (n / (t - u)) * (e - u)))(
                    e,
                    u.maxPoints,
                    r,
                    a,
                  ));
              }),
              n
            );
          },
          Fo = "Progression_base_85",
          Do = "Progression_progressLineContainer_e9",
          Bo = "Progression_point_f9",
          vo = "Progression_line_7f",
          bo = "Progression_line__top_60",
          fo = "Progression_line__bottom_45",
          yo = (0, a.memo)(
            ({ points: e, currentLevel: t, levels: u, maxPointsCount: n, maxLevel: r }) => {
              const s = (0, a.useRef)({ update: () => {} }),
                i = P().mediaSize >= f.Medium ? 68 : 47,
                l = (0, a.useMemo)(() => [0, ...u.map((e) => e.number)], [u]),
                c = -1 * (t - 1) * i + 10;
              return o().createElement(
                "div",
                { className: Fo },
                o().createElement(
                  "div",
                  {
                    className: Do,
                    style: { width: i * r + "rem", transform: `translateX(${c}rem)` },
                  },
                  l
                    .slice(0, l.length)
                    .map((e, t) =>
                      o().createElement(
                        "div",
                        {
                          key: e,
                          className: B()(Bo),
                          style: { transform: `translateX(${t * i}rem)` },
                        },
                        o().createElement("div", { className: B()(vo, bo) }),
                        o().createElement("div", { className: B()(vo, fo) }),
                      ),
                    ),
                  o().createElement(po, {
                    animationSettings: to,
                    value: Co(e, t, u),
                    maxValue: n,
                    api: s,
                    size: ha.Small,
                  }),
                ),
              );
            },
          ),
          wo = {
            base: "ActiveEntryPointState_base_a3",
            entryPoint: "ActiveEntryPointState_entryPoint_93",
            entryPoint__small: "ActiveEntryPointState_entryPoint__small_87",
            bubble: "ActiveEntryPointState_bubble_1a",
            progress: "ActiveEntryPointState_progress_ea",
            progressBg: "ActiveEntryPointState_progressBg_ee",
            progressHoverBg: "ActiveEntryPointState_progressHoverBg_fb",
            entryPoint__hovered: "ActiveEntryPointState_entryPoint__hovered_e2",
            levelText: "ActiveEntryPointState_levelText_4b",
            levelText__gradient: "ActiveEntryPointState_levelText__gradient_a4",
            level: "ActiveEntryPointState_level_dc",
            progressLine: "ActiveEntryPointState_progressLine_e4",
            icon: "ActiveEntryPointState_icon_2f",
            icon__alfa: "ActiveEntryPointState_icon__alfa_b6",
            icon__bravo: "ActiveEntryPointState_icon__bravo_14",
            icon__flipping: "ActiveEntryPointState_icon__flipping_84",
            scaleDown: "ActiveEntryPointState_scaleDown_2a",
            scaleUp: "ActiveEntryPointState_scaleUp_e7",
            icon__flippedTo11: "ActiveEntryPointState_icon__flippedTo11_39",
            glowContainer: "ActiveEntryPointState_glowContainer_c6",
            glow: "ActiveEntryPointState_glow_68",
          },
          Po = ["", "alfa", "bravo"],
          No = (0, a.memo)(
            ({
              isAnySelectableRewardInInventory: e,
              progressState: t,
              isAnySelectableReward: u,
              levelsCount: n,
              maxPointsCount: r,
              points: s,
              currentLevel: i,
              levels: l,
              isHovered: c,
              currentChapterId: d,
              onClick: _,
            }) => {
              const m = (0, a.useState)(io.FLIPPED),
                E = m[0],
                A = m[1],
                g = (0, a.useState)(lo.FLIPPED_TO_PARAGONS),
                p = g[0],
                h = g[1],
                C = (0, a.useState)(!1),
                F = C[0],
                D = C[1],
                v = Sr(),
                b = Sr(),
                f = Sr(),
                y = Sr(),
                w = (0, a.useCallback)(() => {
                  (A(io.FLIPPING),
                    h(lo.FLIPPED_TO_11),
                    D(!0),
                    fe(R.sounds.paragons_vidget_anim()),
                    v.run(() => {
                      (A(io.FLIPPED), D(!1));
                    }, ro),
                    b.run(() => {
                      (A(io.FLIPPING),
                        h(lo.FLIPPED_TO_PARAGONS),
                        fe(R.sounds.paragons_vidget_anim()),
                        D(!0));
                    }, ao),
                    f.run(() => {
                      (A(io.FLIPPED), D(!1));
                    }, oo));
                }, [v, b, f]);
              return (
                (0, a.useEffect)(() => {
                  if (!e && t !== ga.Paused) {
                    let e;
                    return (
                      y.run(() => {
                        (w(),
                          (e = setInterval(() => {
                            w();
                          }, so)));
                      }, no),
                      () => {
                        (clearInterval(e), v.clear(), b.clear(), f.clear());
                      }
                    );
                  }
                }, [e]),
                o().createElement(
                  "div",
                  { className: wo.base },
                  o().createElement(
                    "div",
                    { className: B()(wo.entryPoint, c && wo.entryPoint__hovered), onClick: _ },
                    u && o().createElement("div", { className: wo.bubble }),
                    o().createElement(
                      "div",
                      { className: wo.progress },
                      o().createElement("div", { className: wo.progressBg }),
                      o().createElement("div", { className: wo.progressHoverBg }),
                      o().createElement(Au, { className: wo.levelText, text: String(i) }),
                      o().createElement(Au, {
                        className: B()(wo.levelText, wo.levelText__gradient),
                        text: String(i),
                      }),
                      o().createElement(
                        "div",
                        { className: wo.progressLine },
                        o().createElement(yo, {
                          points: s,
                          currentLevel: i,
                          maxLevel: n,
                          maxPointsCount: r,
                          levels: l,
                        }),
                      ),
                    ),
                    o().createElement("div", {
                      className: B()(
                        wo.icon,
                        wo[`icon__${Po[d]}`],
                        E === io.FLIPPING && wo.icon__flipping,
                        p === lo.FLIPPED_TO_11 && wo.icon__flippedTo11,
                      ),
                    }),
                    F &&
                      o().createElement(
                        "div",
                        { className: wo.glowContainer },
                        o().createElement("div", { className: wo.glow }),
                      ),
                  ),
                )
              );
            },
          ),
          So = "FreePoints_base_7d",
          To = "FreePoints_freePointsBg_f7",
          Lo = "FreePoints_freePointsHoverBg_8a",
          Ro = "FreePoints_base__hovered_3f",
          ko = "FreePoints_freePointsText_8f",
          xo = "FreePoints_freePointsText__gradient_18",
          Io = ({ freePoints: e, isHovered: t }) =>
            o().createElement(
              "div",
              { className: B()(So, t && Ro) },
              o().createElement("div", { className: To }),
              o().createElement("div", { className: Lo }),
              o().createElement(
                "div",
                { className: ko },
                o().createElement(yr, { value: e, format: "integral" }),
              ),
              o().createElement(
                "div",
                { className: B()(ko, xo) },
                o().createElement(yr, { value: e, format: "integral" }),
              ),
            ),
          Mo = "AllChaptersCompletedEntryPointState_base_89",
          Oo = "AllChaptersCompletedEntryPointState_entryPoint_60",
          Ho = "AllChaptersCompletedEntryPointState_icon_40",
          zo = "AllChaptersCompletedEntryPointState_entryPoint__hovered_14",
          Wo = "AllChaptersCompletedEntryPointState_icon__flipping_54",
          Go = "AllChaptersCompletedEntryPointState_icon__flippedTo11_b3",
          Vo = "AllChaptersCompletedEntryPointState_glowContainer_35",
          $o = "AllChaptersCompletedEntryPointState_glow_04",
          Uo = "AllChaptersCompletedEntryPointState_completedIcon_ad",
          jo = (0, a.memo)(
            ({
              freePoints: e,
              isAnySelectableRewardInInventory: t,
              progressState: u,
              isHovered: n,
              onClick: r,
            }) => {
              const s = (0, a.useState)(io.FLIPPED),
                i = s[0],
                l = s[1],
                c = (0, a.useState)(lo.FLIPPED_TO_PARAGONS),
                d = c[0],
                _ = c[1],
                m = (0, a.useState)(!1),
                E = m[0],
                A = m[1],
                g = Sr(),
                p = Sr(),
                h = Sr(),
                C = Sr(),
                F = (0, a.useCallback)(() => {
                  (l(io.FLIPPING),
                    _(lo.FLIPPED_TO_11),
                    A(!0),
                    fe(R.sounds.paragons_vidget_anim()),
                    g.run(() => {
                      (l(io.FLIPPED), A(!1));
                    }, ro),
                    p.run(() => {
                      (l(io.FLIPPING),
                        _(lo.FLIPPED_TO_PARAGONS),
                        fe(R.sounds.paragons_vidget_anim()),
                        A(!0));
                    }, ao),
                    h.run(() => {
                      (l(io.FLIPPED), A(!1));
                    }, oo));
                }, [g, p, h]);
              return (
                (0, a.useEffect)(() => {
                  if (!t && u !== ga.Paused) {
                    let e;
                    return (
                      C.run(() => {
                        (F(),
                          (e = setInterval(() => {
                            F();
                          }, so)));
                      }, no),
                      () => {
                        (clearInterval(e), g.clear(), p.clear(), h.clear());
                      }
                    );
                  }
                }, [t]),
                o().createElement(
                  "div",
                  { className: Mo },
                  o().createElement(
                    "div",
                    { className: B()(Oo, n && zo), onClick: r },
                    Boolean(e) && o().createElement(Io, { freePoints: e, isHovered: n }),
                    o().createElement("div", {
                      className: B()(Ho, i === io.FLIPPING && Wo, d === lo.FLIPPED_TO_11 && Go),
                    }),
                    E &&
                      o().createElement(
                        "div",
                        { className: Vo },
                        o().createElement("div", { className: $o }),
                      ),
                    o().createElement("div", { className: Uo }),
                  ),
                )
              );
            },
          ),
          Xo = "ChapterNotChosenEntryPointState_base_47",
          qo = "ChapterNotChosenEntryPointState_entryPoint_8c",
          Yo = "ChapterNotChosenEntryPointState_entryPoint__show_64",
          Ko = "ChapterNotChosenEntryPointState_bubble_87",
          Zo = "ChapterNotChosenEntryPointState_icon_e7",
          Qo = "ChapterNotChosenEntryPointState_entryPoint__hovered_8b",
          Jo = "ChapterNotChosenEntryPointState_icon__flipping_a3",
          es = "ChapterNotChosenEntryPointState_icon__flippedTo11_90",
          ts = "ChapterNotChosenEntryPointState_glowContainer_59",
          us = "ChapterNotChosenEntryPointState_glow_56",
          ns = "ChapterNotChosenEntryPointState_plusIcon_3f",
          rs = (0, a.memo)(
            ({
              freePoints: e,
              isAnySelectableRewardInInventory: t,
              progressState: u,
              isAnySelectableReward: n,
              isHovered: r,
              onClick: s,
            }) => {
              const i = (0, a.useState)(io.FLIPPED),
                l = i[0],
                c = i[1],
                d = (0, a.useState)(lo.FLIPPED_TO_PARAGONS),
                _ = d[0],
                m = d[1],
                E = (0, a.useState)(!1),
                A = E[0],
                g = E[1],
                p = be("ParagonsEntryPoint", ve);
              (0, a.useEffect)(() => {
                p && p.runTrigger(!0);
              }, [p]);
              const h = Sr(),
                C = Sr(),
                F = Sr(),
                D = Sr(),
                v = (0, a.useCallback)(() => {
                  (c(io.FLIPPING),
                    m(lo.FLIPPED_TO_11),
                    g(!0),
                    fe(R.sounds.paragons_vidget_anim()),
                    h.run(() => {
                      (c(io.FLIPPED), g(!1));
                    }, ro),
                    C.run(() => {
                      (c(io.FLIPPING),
                        m(lo.FLIPPED_TO_PARAGONS),
                        fe(R.sounds.paragons_vidget_anim()),
                        g(!0));
                    }, ao),
                    F.run(() => {
                      (c(io.FLIPPED), g(!1));
                    }, oo));
                }, [h, C, F]);
              return (
                (0, a.useEffect)(() => {
                  if (!t && u !== ga.Paused) {
                    let e;
                    return (
                      D.run(() => {
                        (v(),
                          (e = setInterval(() => {
                            v();
                          }, so)));
                      }, no),
                      () => {
                        (clearInterval(e), h.clear(), C.clear(), F.clear());
                      }
                    );
                  }
                }, [t]),
                o().createElement(
                  "div",
                  { className: Xo },
                  o().createElement(
                    "div",
                    { id: e ? uo : "", className: B()(qo, Boolean(e) && Yo, r && Qo), onClick: s },
                    Boolean(e) && o().createElement(Io, { freePoints: e, isHovered: r }),
                    n && o().createElement("div", { className: Ko }),
                    o().createElement("div", {
                      id: e ? "" : uo,
                      className: B()(Zo, l === io.FLIPPING && Jo, _ === lo.FLIPPED_TO_11 && es),
                    }),
                    o().createElement("div", { className: ns }),
                    A &&
                      o().createElement(
                        "div",
                        { className: ts },
                        o().createElement("div", { className: us }),
                      ),
                  ),
                )
              );
            },
          ),
          as = "NotAvailableEntryPointState_base_31",
          os = "NotAvailableEntryPointState_entryPoint_cc",
          ss = "NotAvailableEntryPointState_icon_43",
          is = "NotAvailableEntryPointState_entryPoint__hovered_2f",
          ls = (0, a.memo)(({ isHovered: e, onClick: t }) =>
            o().createElement(
              "div",
              { className: as },
              o().createElement(
                "div",
                { className: B()(os, e && is), onClick: t },
                o().createElement("div", { className: B()(ss) }),
              ),
            ),
          ),
          cs = "PausedEntryPointState_base_38",
          ds = "PausedEntryPointState_entryPoint_73",
          _s = "PausedEntryPointState_entryPoint__small_d0",
          ms = "PausedEntryPointState_icon_ca",
          Es = "PausedEntryPointState_icon__disabled_79",
          As = "PausedEntryPointState_entryPoint__hovered_55",
          gs = (0, a.memo)(({ isHovered: e, onClick: t }) =>
            o().createElement(
              "div",
              { className: cs },
              o().createElement(
                "div",
                { className: B()(ds, _s, e && As), onClick: t },
                o().createElement("div", { className: B()(ms, Es) }),
              ),
            ),
          ),
          ps = "MainParagonsEntryPoint_base_90",
          hs = (0, a.memo)(
            ({
              points: e,
              levels: t,
              freePoints: u,
              levelsCount: n,
              progressState: r,
              currentChapter: s,
              maxPointsCount: i,
              isAnySelectableReward: l,
              isAnySelectableRewardInInventory: c,
              onEntryPointClick: d,
            }) => {
              const _ = (0, a.useState)(!1),
                m = _[0],
                E = _[1],
                A = s.chapterLevel || 0,
                g = s.id || 0,
                p = () => {
                  (ye.playClick(), d());
                };
              return o().createElement(
                "div",
                {
                  className: ps,
                  onMouseEnter: () => {
                    (ye.playHighlight(), E(!0));
                  },
                  onMouseLeave: () => {
                    (ye.playHighlight(), E(!1));
                  },
                },
                r === ga.Paused && o().createElement(gs, { isHovered: m, onClick: p }),
                r === ga.AllChaptersCompleted &&
                  o().createElement(jo, {
                    freePoints: u,
                    isAnySelectableRewardInInventory: c,
                    progressState: r,
                    onClick: p,
                    isHovered: m,
                  }),
                r === ga.NotAvailable && o().createElement(ls, { isHovered: m, onClick: p }),
                r === ga.ChapterNotChosen &&
                  o().createElement(rs, {
                    freePoints: u,
                    isAnySelectableRewardInInventory: c,
                    progressState: r,
                    isAnySelectableReward: l,
                    onClick: p,
                    isHovered: m,
                  }),
                r === ga.Active &&
                  o().createElement(No, {
                    isAnySelectableRewardInInventory: c,
                    progressState: r,
                    isAnySelectableReward: l,
                    levelsCount: n,
                    maxPointsCount: i,
                    points: e,
                    currentLevel: A,
                    levels: t,
                    onClick: p,
                    isHovered: m,
                    currentChapterId: g,
                  }),
              );
            },
          );
        const Cs = "Frame_base_dc",
          Fs = "Frame_base__scaled_74",
          Ds = "Frame_arrow_ec",
          Bs = o().forwardRef(function ({ arrowRef: e }, t) {
            const u = 2 === ce();
            return o().createElement(
              "div",
              { className: B()(Cs, u && Fs), ref: t },
              o().createElement("div", { className: Ds, ref: e }),
            );
          }),
          vs = {
            base: "Tab_base_d9",
            base__scaled: "Tab_base__scaled_bf",
            base__active: "Tab_base__active_da",
            earlyAccessIcon: "Tab_earlyAccessIcon_cc",
            discountIcon: "Tab_discountIcon_6e",
            discountIcon__scaled: "Tab_discountIcon__scaled_4c",
            highlight: "Tab_highlight_1d",
            icon: "Tab_icon_0f",
          },
          bs = { mouseEnter: R.sounds.highlight(), click: R.sounds.tabb() },
          fs = o().forwardRef(function (
            {
              id: e,
              isActive: t,
              sounds: u = bs,
              title: n,
              icon: r,
              hasNewDiscountEvent: a,
              isEarlyAccess: s,
              onClick: i,
              onMouseEnter: l,
              onMouseLeave: c,
            },
            d,
          ) {
            const _ = 2 === ce(),
              m = (e) => {
                !t && u[e] && fe(u[e]);
              };
            return o().createElement(
              q,
              { args: { tooltipId: "techtreeNationTooltip", nation: n } },
              o().createElement(
                "div",
                {
                  className: B()(vs.base, t && vs.base__active, _ && vs.base__scaled),
                  onClick:
                    ((E = n),
                    () => {
                      (m("click"), null == i || i(E));
                    }),
                  onMouseEnter: ((e) => () => {
                    (m("mouseEnter"), null == l || l(e));
                  })(e),
                  onMouseLeave: ((e) => () => {
                    (m("mouseLeave"), null == c || c(e));
                  })(e),
                  ref: t ? d : null,
                },
                s && !t && o().createElement("div", { className: vs.earlyAccessIcon }),
                a &&
                  o().createElement("div", {
                    className: B()(vs.discountIcon, _ && vs.discountIcon__scaled),
                  }),
                o().createElement("div", {
                  className: B()(vs.highlight, _ && vs.highlight__scaled),
                }),
                o().createElement("div", {
                  className: vs.icon,
                  style: { backgroundImage: `url(${r})` },
                }),
              ),
            );
            var E;
          }),
          ys = "VerticalTabs_base_a6",
          ws = "VerticalTabs_group_e1";
        function Ps() {
          return (
            (Ps =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ps.apply(this, arguments)
          );
        }
        const Ns = (0, a.memo)(
            ({ active: e, tabs: t, sounds: u, onClick: n, onMouseEnter: r, onMouseLeave: s }) => {
              const l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                d = (0, a.useRef)(null),
                _ = (0, a.useRef)(null),
                m = (0, Pe.useSpring)(() => ({
                  marginLeft: 0,
                  onChange: (e) => {
                    const t = l.current;
                    t && (t.style.marginLeft = `${e.value.marginLeft}rem`);
                  },
                }))[1],
                E = (0, Pe.useSpring)(() => ({
                  opacity: 0,
                  onChange: (e) => {
                    const t = l.current;
                    t && (t.style.opacity = `${e.value.opacity}`);
                  },
                }))[1],
                A = (0, Pe.useSpring)(() => ({
                  position: 0,
                  onChange: (e) => {
                    const t = c.current;
                    t &&
                      (t.style.transform = `translateY(${e.value.position / i.O.view.getScale()}rem)`);
                  },
                  onStart: () => {
                    (m.start({
                      from: { marginLeft: 12 },
                      to: { marginLeft: 0 },
                      config: { duration: 50 },
                    }),
                      E.start({
                        from: { opacity: 1 },
                        to: { opacity: 0 },
                        config: { duration: 50 },
                      }));
                  },
                  onRest: () => {
                    (m.start({
                      from: { marginLeft: 0 },
                      to: { marginLeft: 12 },
                      config: { duration: 150 },
                    }),
                      E.start({
                        from: { opacity: 0 },
                        to: { opacity: 1 },
                        config: { duration: 150 },
                      }));
                  },
                }))[1],
                g = (0, a.useCallback)((e) => {
                  if (null !== d.current && null !== _.current) {
                    e(
                      d.current.getBoundingClientRect().top - _.current.getBoundingClientRect().top,
                    );
                  }
                }, []);
              var p, h;
              return (
                (0, a.useEffect)(() => {
                  g((e) => {
                    A.start({ position: e, config: { duration: 200 } });
                  });
                }, [A, e, g]),
                (0, a.useEffect)(
                  () =>
                    te(() => {
                      g((e) => {
                        A.start({ position: e, immediate: !0 });
                      });
                    }),
                  [A, g],
                ),
                (p = () => {
                  g((e) => {
                    A.start({ position: e, config: { duration: 200 } });
                  });
                }),
                (h = [A, g]),
                (0, a.useEffect)(() => {
                  let e = () => {};
                  const t = () => {
                    (e(), (e = te(p)));
                  };
                  return (
                    window.addEventListener("resize", t),
                    () => {
                      (e(), window.removeEventListener("resize", t));
                    }
                  );
                }, h),
                o().createElement(
                  "div",
                  { className: ys, ref: _ },
                  t.map(({ id: t, items: a }) =>
                    o().createElement(
                      "div",
                      { key: t, className: ws },
                      a.map((t) =>
                        o().createElement(
                          fs,
                          Ps(
                            {
                              key: t.id,
                              ref: d,
                              sounds: u,
                              isActive: e === t.title,
                              onMouseEnter: r,
                              onMouseLeave: s,
                              onClick: n,
                            },
                            t,
                          ),
                        ),
                      ),
                    ),
                  ),
                  o().createElement(Bs, { arrowRef: l, ref: c }),
                )
              );
            },
          ),
          Ss = "NationsMenu_base_98",
          Ts = "NationsMenu_shadowContainer_2b",
          Ls = "NationsMenu_shadow_b5",
          Rs = "NationsMenu_shadow__scaled_68",
          ks = (0, we.Pi)(() => {
            const e = Je(),
              t = e.controls,
              u = e.model,
              n = u.root.get(),
              r = n.selectedNation,
              s = n.isEarlyAccessFirstTimeShown,
              i = n.earlyAccessNation,
              l = u.computes.getAvailableNations,
              c = ce(),
              d = (0, a.useCallback)(
                (e) => {
                  r !== e && t.onNationChange(e);
                },
                [t, r],
              ),
              _ = l(),
              m = (0, a.useMemo)(
                () => [
                  {
                    id: 0,
                    items: _.map((e) => ({
                      id: e.nationIndex,
                      isEarlyAccess: s && e.nation === i,
                      hasNewDiscountEvent: e.hasNewDiscountEvent,
                      title: e.nation,
                      icon: R.images.gui.maps.icons.flags.c_60x40.$dyn(e.nation),
                    })),
                  },
                ],
                [i, _, s],
              ),
              E = 2 === c;
            return o().createElement(
              "div",
              { className: Ss },
              o().createElement(
                "div",
                { className: Ts },
                o().createElement("div", { className: B()(Ls, E && Rs) }),
              ),
              o().createElement(Ns, { tabs: m, active: r, onClick: d }),
            );
          }),
          xs = (0, a.memo)(ks),
          Is = "NationTitle_base_60",
          Ms = "NationTitle_nationTitle_06",
          Os = "NationTitle_collectionVehicles_5a",
          Hs = R.strings.techtree,
          zs = (0, we.Pi)(() => {
            const e = Je(),
              t = e.model,
              u = e.controls,
              n = t.root.get(),
              r = n.selectedNation,
              a = n.isBlueprintMode,
              s = n.hasCollectibleVehicles;
            return o().createElement(
              "div",
              { className: Is },
              o().createElement(Au, {
                className: Ms,
                text: Hs.vehicle_tree.header.title.$dyn(a ? `${r}_blueprints` : r),
              }),
              s &&
                !a &&
                o().createElement(
                  ee,
                  { tooltipArgs: { args: { tooltipId: "vehicleCollectorTooltip", nation: r } } },
                  o().createElement("div", {
                    className: Os,
                    onClick: () => {
                      (fe(R.sounds.play()), u.onGoToCollectionVehicle(r));
                    },
                    onMouseEnter: () => {
                      fe(R.sounds.highlight());
                    },
                  }),
                ),
            );
          }),
          Ws = "PremiumPanel_base_90",
          Gs = "PremiumPanel_backgroundWrapper_a5",
          Vs = "PremiumPanel_background_50",
          $s = "PremiumPanel_topBorder_b3",
          Us = "PremiumPanel_base__active_05",
          js = "PremiumPanel_contentWrapper_a7",
          Xs = "PremiumPanel_content_63",
          qs = "PremiumPanel_content__withRowButtons_18",
          Ys = (0, a.memo)(
            ({
              isPremiumAreaActive: e,
              isDragging: t,
              levels: u,
              premiumRows: n,
              premiumNodes: r,
              isVerticalScrollBarShown: a,
              onSetActiveLevel: s,
              onShowPremiumPanel: i,
              isRowButtons: l,
            }) =>
              o().createElement(
                "div",
                { className: B()(Ws, e && Us) },
                o().createElement(
                  "div",
                  { className: Gs },
                  o().createElement(
                    "div",
                    { className: Vs },
                    o().createElement("div", { className: $s }),
                  ),
                ),
                o().createElement(
                  "div",
                  { className: js, onMouseEnter: i },
                  o().createElement(
                    "div",
                    { className: B()(Xs, l && qs) },
                    u.map((e) =>
                      o().createElement(
                        _n,
                        {
                          key: `nodes-column-${e}`,
                          isLastColumn: e === u.length,
                          isVerticalScrollBarShown: a,
                          isDragging: t,
                        },
                        o().createElement(
                          o().Fragment,
                          null,
                          n.map((t) => {
                            const a = r.find((u) => u.row === t + 1 && u.column === e);
                            return o().createElement(
                              on,
                              {
                                key: `node-cell-${null != a && a.id ? a.id : `${t}-${e}`}`,
                                isPremiumCell: !0,
                                isPremiumLastRow: t + 1 === n.length,
                                isPremiumLastColumn: e === u.length,
                              },
                              o().createElement(ma, {
                                columnIndex: e,
                                isPremium: !0,
                                node: a,
                                levels: u,
                                onSetActiveLevel: s,
                              }),
                            );
                          }),
                        ),
                      ),
                    ),
                  ),
                ),
              ),
          ),
          Ks = "PremiumPanelEffects_base_41",
          Zs = "PremiumPanelEffects_shadow_63",
          Qs = "PremiumPanelEffects_base__active_6a",
          Js = "PremiumPanelEffects_topGlow_b7",
          ei = "PremiumPanelEffects_wreathWrapper_96",
          ti = "PremiumPanelEffects_wreathContent_bb",
          ui = "PremiumPanelEffects_wreath_d8",
          ni = "PremiumPanelEffects_titleGlow_bd",
          ri = "PremiumPanelEffects_header_72",
          ai = R.strings.techtree,
          oi = (0, a.memo)(({ isPremiumAreaActive: e }) => {
            const t = viewEnv.getGraphicsQuality() < 1;
            return o().createElement(
              "div",
              { className: B()(Ks, e && Qs) },
              t &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: Zs }),
                  o().createElement("div", { className: Js }),
                ),
              o().createElement(
                "div",
                { className: ei },
                o().createElement(
                  "div",
                  { className: ti },
                  o().createElement("div", { className: ui }),
                  o().createElement("div", { className: ni }),
                  o().createElement(Au, { className: ri, text: ai.vehicle_tree.premium.title() }),
                ),
              ),
            );
          });
        let si, ii;
        (!(function (e) {
          ((e.EarlyAccess = "earlyAccess"), (e.Paragons = "paragons"));
        })(si || (si = {})),
          (function (e) {
            ((e.ENABLED = "enabled"),
              (e.DISABLED = "disabled"),
              (e.FIRST_BRANCH_RESET = "firstBranchReset"),
              (e.DROPPED_BRANCH = "droppedBranch"));
          })(ii || (ii = {})));
        const li = "EarlyAccessButton_base_f8",
          ci = "EarlyAccessButton_touchableZone_30",
          di = "EarlyAccessButton_base__disabled_b8",
          _i = "EarlyAccessButton_background_4a",
          mi = "EarlyAccessButton_base__scaled_47",
          Ei = "EarlyAccessButton_backgroundHovered_e1",
          Ai = "EarlyAccessButton_base__hovered_92",
          gi = "EarlyAccessButton_icon_c2",
          pi = ({ isDisabled: e, children: t }) =>
            e
              ? o().createElement(
                  U,
                  {
                    contentId:
                      R.views.lobby.early_access.tooltips.EarlyAccessEntryPointPausedTooltip(
                        "resId",
                      ),
                  },
                  t,
                )
              : o().createElement(
                  Q,
                  {
                    header: R.strings.tooltips.techTreePage.earlyAccessEntryPointTooltip.header(),
                    body: R.strings.tooltips.techTreePage.earlyAccessEntryPointTooltip.body(),
                  },
                  t,
                ),
          hi = (0, a.memo)(({ rowsButton: e, onHover: t, onClick: u }) => {
            const n = (0, a.useState)(!1),
              r = n[0],
              s = n[1],
              i = 2 === ce(),
              l = e.buttonState === ii.DISABLED;
            return o().createElement(
              "div",
              { className: B()(li, l && di, r && Ai, i && mi) },
              o().createElement(
                pi,
                { isDisabled: l },
                o().createElement("div", {
                  className: ci,
                  onMouseEnter: () => {
                    l || (s(!0), t(!0));
                  },
                  onMouseLeave: () => {
                    l || (s(!1), t(!1));
                  },
                  onClick: () => {
                    l || u(e.buttonType, e.branchID);
                  },
                }),
              ),
              o().createElement("div", { className: _i }),
              !l &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: Ei }),
                  o().createElement("div", { className: gi }),
                ),
            );
          }),
          Ci = {
            base: "ParagonsRowButton_base_b3",
            base__disabled: "ParagonsRowButton_base__disabled_c8",
            background: "ParagonsRowButton_background_1d",
            backgroundHovered: "ParagonsRowButton_backgroundHovered_4f",
            base__hovered: "ParagonsRowButton_base__hovered_e6",
            icon: "ParagonsRowButton_icon_a4",
            base__droppedBranch: "ParagonsRowButton_base__droppedBranch_11",
            iconHovered: "ParagonsRowButton_iconHovered_42",
            iconGlow: "ParagonsRowButton_iconGlow_d0",
            hintArrow: "ParagonsRowButton_hintArrow_1b",
            blink: "ParagonsRowButton_blink_b3",
            pulse: "ParagonsRowButton_pulse_0c",
          },
          Fi = "R.images.gui.maps.icons.techtree.researchTree.rowButtons.paragons",
          Di = (0, a.memo)(
            ({ rowsButton: e, setHoveredNodes: t, setResetNodes: u, onClick: n }) => {
              const r = ce(),
                s = (0, a.useState)(!1),
                i = s[0],
                l = s[1],
                c = e.buttonState,
                d = c === ii.ENABLED,
                _ = c === ii.DISABLED,
                m = r >= 1.5,
                E = m ? "_scaled" : "",
                A = `url('${Fi}.backgrounds.${c}${E}')`,
                g = `url('${Fi}.backgrounds.${c}_hover${E}')`,
                p = c === ii.DROPPED_BRANCH ? "info" : "default",
                h = `url('${Fi}.icons.${p}')`,
                C = `url('${Fi}.icons.${p}_hover')`;
              let F;
              return (
                (0, a.useEffect)(() => (i || clearInterval(F), () => clearInterval(F)), [i]),
                o().createElement(
                  U,
                  {
                    contentId: R.views.lobby.paragons.tooltips.ResetButtonTooltip("resId"),
                    args: { branchID: e.branchID },
                  },
                  o().createElement(
                    "div",
                    {
                      className: B()(
                        Ci.base,
                        !d && Ci.base__disabled,
                        i && Ci.base__hovered,
                        m && Ci.base__scaled,
                        Ci[`base__${c}`],
                      ),
                      "data-branch-id": e.branchID,
                      "data-vehicle-cds": String(e.vehiclesCDs),
                      onMouseEnter: () => {
                        d && (l(!0), ye.playHighlight(), t(e.vehiclesCDs));
                      },
                      onMouseLeave: () => {
                        d && (l(!1), t([]));
                      },
                      onClick: () => {
                        d && (ye.playClick(), n(e.buttonType, e.branchID), u(e.vehiclesCDs));
                      },
                    },
                    i &&
                      o().createElement("div", {
                        className: Ci.hintArrow,
                        onAnimationStart: () => {
                          (fe(R.sounds.paragons_reset_btn_anim()),
                            (F = setInterval(() => {
                              fe(R.sounds.paragons_reset_btn_anim());
                            }, 1200)));
                        },
                      }),
                    _ &&
                      o().createElement("div", {
                        className: Ci.icon,
                        style: { backgroundImage: h },
                      }),
                    o().createElement("div", {
                      className: Ci.background,
                      style: { backgroundImage: A },
                    }),
                    d &&
                      o().createElement("div", {
                        className: Ci.backgroundHovered,
                        style: { backgroundImage: g },
                      }),
                    !_ &&
                      o().createElement("div", {
                        className: Ci.icon,
                        style: { backgroundImage: h },
                      }),
                    d &&
                      o().createElement(
                        o().Fragment,
                        null,
                        o().createElement("div", { className: Ci.iconGlow }),
                        o().createElement("div", {
                          className: Ci.iconHovered,
                          style: { backgroundImage: C },
                        }),
                      ),
                  ),
                )
              );
            },
          ),
          Bi = "RowButtons_base_2d",
          vi = (0, we.Pi)(({ rowButton: e }) => {
            const t = Je().controls;
            return o().createElement(
              "div",
              { className: Bi },
              e.buttonType === si.Paragons &&
                o().createElement(Di, {
                  rowsButton: e,
                  setHoveredNodes: t.setParagonsHoveredNodes,
                  setResetNodes: t.setParagonsResetNodes,
                  onClick: t.onTechTreeButtonPressed,
                }),
              e.buttonType === si.EarlyAccess &&
                o().createElement(hi, {
                  rowsButton: e,
                  onHover: t.setEarlyAccessButtonHovered,
                  onClick: t.onTechTreeButtonPressed,
                }),
            );
          }),
          bi = [];
        function fi(e) {
          const t = (0, a.useRef)(e);
          return (
            (0, a.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, a.useCallback)((...e) => (0, t.current)(...e), bi)
          );
        }
        function yi(e, t, u = []) {
          const n = (0, a.useRef)(0),
            r = (0, a.useCallback)(() => window.clearInterval(n.current), u || []);
          (0, a.useEffect)(() => r, [r]);
          const o = (null != u ? u : []).concat([t]);
          return [
            (0, a.useCallback)((u) => {
              ((n.current = window.setInterval(() => e(u, !0), t)), e(u, !1));
            }, o),
            r,
          ];
        }
        function wi(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Pi(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return Pi(e, t);
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
        function Pi(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        let Ni;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Ni || (Ni = {}));
        const Si = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: {},
          },
          Ti = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: u,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const s = (e, u) => {
              const n = t(e),
                r = n[0],
                a = n[1];
              return Ka(r, a, u);
            };
            return (l = {}) => {
              const c = l.settings,
                d = void 0 === c ? Si : c,
                _ = (0, a.useRef)(null),
                m = (0, a.useRef)(null),
                E = (() => {
                  const e = (0, a.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    u = (e, u) => {
                      t(e).set(u, u);
                    },
                    n = (e, u) => {
                      t(e).delete(u);
                    },
                    r = (e, ...u) => {
                      for (var n, r = wi(t(e).values()); !(n = r()).done;) (0, n.value)(...u);
                    };
                  return (0, a.useMemo)(() => ({ on: u, off: n, trigger: r }), []);
                })(),
                A = (function (e, t, u) {
                  const n = (0, a.useMemo)(() => ae(u, e), t);
                  return ((0, a.useEffect)(() => n.cancel, [n]), n);
                })(
                  () => {
                    i.O.view.forceTriggerMouseMove();
                  },
                  [],
                  0,
                ),
                g = (0, Pe.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = _.current;
                    t && (u(t, e), E.trigger("change", e), o && A());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                p = g[0],
                h = g[1],
                C = (0, a.useCallback)(
                  (e, t, u) => {
                    var n;
                    const r = p.scrollPosition.get(),
                      a = (null != (n = p.scrollPosition.goal) ? n : 0) - r;
                    return s(e, t * u + a + r);
                  },
                  [p.scrollPosition],
                ),
                F = (0, a.useCallback)(
                  (e, { immediate: t = !1, reset: u = !0 } = {}) => {
                    const n = _.current;
                    n &&
                      h.start({
                        scrollPosition: s(n, e),
                        immediate: t,
                        reset: u,
                        config: d.animationConfig,
                        from: { scrollPosition: s(n, p.scrollPosition.get()) },
                      });
                  },
                  [h, d.animationConfig, p.scrollPosition],
                ),
                D = (0, a.useCallback)(
                  (e) => {
                    const t = _.current,
                      u = m.current;
                    if (!t || !u) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return r(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(u, d.step),
                      a = C(t, e, n);
                    F(a);
                  },
                  [F, C, d.step],
                ),
                B = (0, a.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && D(n(e)),
                      _.current && E.trigger("mouseWheel", e, p.scrollPosition, t(_.current)));
                  },
                  [p.scrollPosition, D, E],
                ),
                v = ((e, t = []) => {
                  const u = (0, a.useRef)(),
                    n = (0, a.useCallback)((...t) => {
                      (u.current && u.current(), (u.current = e(...t)));
                    }, t);
                  return (
                    (0, a.useEffect)(
                      () => () => {
                        u.current && u.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    te(() => {
                      const e = _.current;
                      e &&
                        (F(s(e, p.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [F, p.scrollPosition.goal],
                ),
                b = fi(() => {
                  const e = _.current;
                  if (!e) return;
                  const t = s(e, p.scrollPosition.goal);
                  (t !== p.scrollPosition.goal && F(t, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, a.useEffect)(
                () => (
                  window.addEventListener("resize", v),
                  () => {
                    window.removeEventListener("resize", v);
                  }
                ),
                [v],
              );
              return (0, a.useMemo)(
                () => ({
                  getWrapperSize: () => (m.current ? r(m.current) : void 0),
                  getContainerSize: () => (_.current ? e(_.current) : void 0),
                  getBounds: () =>
                    _.current
                      ? t(_.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: d.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: B,
                  applyScroll: F,
                  applyStepTo: D,
                  contentRef: _,
                  wrapperRef: m,
                  scrollPosition: h,
                  animationScroll: p,
                  recalculateContent: b,
                  events: { on: E.on, off: E.off },
                }),
                [p.scrollPosition, F, D, E.off, E.on, b, B, h, d.step.clampedArrowStepTimeout],
              );
            };
          },
          Li = Ti({
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
            getDirection: (e) => (e.deltaY > 1 ? Ni.Next : Ni.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          Ri = "HorizontalBar_base_72",
          ki = "HorizontalBar_base__nonActive_8b",
          xi = "HorizontalBar_leftButton_14",
          Ii = "HorizontalBar_rightButton_88",
          Mi = "HorizontalBar_track_bc",
          Oi = "HorizontalBar_thumb_63",
          Hi = "HorizontalBar_rail_3b",
          zi = "disable",
          Wi = { pending: !1, offset: 0 },
          Gi = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Vi = () => {},
          $i = (e, t) => Math.max(20, e.offsetWidth * t),
          Ui = (0, a.memo)(
            ({
              api: e,
              classNames: t = {},
              getStepByRailClick: u = Gi,
              onDrag: n = Vi,
              isOnView: r,
            }) => {
              const s = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                d = (0, a.useRef)(null),
                _ = e.stepTimeout || 100,
                m = (0, a.useState)(Wi),
                E = m[0],
                A = m[1],
                g = (0, a.useCallback)(
                  (e) => {
                    (A(e),
                      d.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: d.current }));
                  },
                  [n],
                ),
                p = () => {
                  const t = c.current,
                    u = d.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && u && r)) return;
                  const a = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / r),
                    s = Ka(0, 1, a / (r - n)),
                    _ = (t.offsetWidth - $i(t, o)) * s;
                  ((u.style.transform = `translateX(${0 | _}px)`),
                    ((e) => {
                      if (i.current && l.current && c.current && d.current) {
                        if (0 === e)
                          return (i.current.classList.add(zi), void l.current.classList.remove(zi));
                        if (
                          ((t = c.current),
                          (u = d.current),
                          e - (t.offsetWidth - u.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(zi), void l.current.classList.add(zi));
                        var t, u;
                        (i.current.classList.remove(zi), l.current.classList.remove(zi));
                      }
                    })(_));
                },
                h = fi(() => {
                  ((() => {
                    const t = d.current,
                      u = c.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && n && u)) return;
                    const a = Math.min(1, n / r);
                    ((t.style.width = `${$i(u, a)}px`),
                      s.current &&
                        (1 === a ? s.current.classList.add(ki) : s.current.classList.remove(ki)));
                  })(),
                    p());
                });
              ((0, a.useEffect)(() => te(h)),
                (0, a.useEffect)(
                  () =>
                    te(() => {
                      const t = () => {
                        p();
                      };
                      let u = Vi;
                      const n = () => {
                        (u(), (u = te(h)));
                      };
                      return (
                        e.events.on("recalculateContent", h),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (u(),
                            e.events.off("recalculateContent", h),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, a.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      var u;
                      if (!r) return;
                      const a = e.contentRef.current;
                      if (!a) return;
                      const o = c.current,
                        s = d.current;
                      if (!a || !o || !s) return;
                      const i = t.screenX - E.offset - o.getBoundingClientRect().x,
                        l = (i / o.offsetWidth) * (null != (u = e.getContainerSize()) ? u : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(a, l),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: l }));
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), g(Wi));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, E.offset, E.pending, r, n, g]));
              const C = yi((t) => e.applyStepTo(t), _, [e]),
                F = C[0],
                D = C[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", D, !0),
                  () => document.removeEventListener("mouseup", D, !0)
                ),
                [D],
              );
              const v = (e) => {
                e.target.classList.contains(zi) || fe(R.sounds.highlight());
              };
              return o().createElement(
                "div",
                { className: B()(Ri, t.base), ref: s, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: B()(xi, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(zi) ||
                      0 !== e.button ||
                      (fe(R.sounds.play()), F(Ni.Next));
                  },
                  onMouseUp: D,
                  ref: i,
                  onMouseEnter: v,
                }),
                o().createElement(
                  "div",
                  {
                    className: B()(Mi, t.track),
                    onMouseDown: (t) => {
                      const n = d.current;
                      if (n && 0 === t.button)
                        if ((fe(R.sounds.play()), t.target === n))
                          g({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = d.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const a = u(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * t);
                          })(t.screenX > n.getBoundingClientRect().x ? Ni.Prev : Ni.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: v,
                  },
                  o().createElement("div", { ref: d, className: B()(Oi, t.thumb) }),
                  o().createElement("div", { className: B()(Hi, t.rail) }),
                ),
                o().createElement("div", {
                  className: B()(Ii, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(zi) ||
                      0 !== e.button ||
                      (fe(R.sounds.play()), F(Ni.Prev));
                  },
                  onMouseUp: D,
                  ref: l,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          ji = {
            base: "HorizontalScroll_base_f2",
            wrapper: "HorizontalScroll_wrapper_89",
            content: "HorizontalScroll_content_0e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8f",
          },
          Xi = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: r,
            classNames: s,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, a.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: B()(ji.base, e.base) });
              }, [n]),
              _ = (0, a.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: B()(ji.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: B()(ji.defaultScrollArea, r) },
                o().createElement(qi, { className: i, api: _, classNames: s }, e),
              ),
              o().createElement(Ui, { getStepByRailClick: l, api: t, onDrag: c, classNames: d }),
            );
          },
          qi = ({ api: e, className: t, children: u }) => (
            (0, a.useEffect)(() => te(e.recalculateContent)),
            o().createElement(
              "div",
              { className: B()(ji.base, t) },
              o().createElement(
                "div",
                { className: ji.wrapper, onWheel: e.handleMouseWheel, ref: e.wrapperRef },
                o().createElement("div", { className: ji.content, ref: e.contentRef }, u),
              ),
            )
          );
        ((qi.Bar = Ui),
          (qi.Default = Xi),
          (qi.SeniorityAwards = ({ api: e, className: t, classNames: u, children: n }) => (
            (0, a.useEffect)(() => te(e.recalculateContent)),
            o().createElement(
              "div",
              { className: B()(ji.base, t) },
              o().createElement(
                "div",
                { className: B()(ji.wrapper, null == u ? void 0 : u.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: B()(ji.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Yi = Ti({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Ni.Next : Ni.Prev),
          }),
          Ki = "VerticalBar_base_d6",
          Zi = "VerticalBar_base__nonActive_3c",
          Qi = "VerticalBar_topButton_6f",
          Ji = "VerticalBar_bottomButton_db",
          el = "VerticalBar_track_ab",
          tl = "VerticalBar_thumb_f8",
          ul = "VerticalBar_rail_cd",
          nl = "disable",
          rl = () => {},
          al = { pending: !1, offset: 0 },
          ol = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          sl = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          il = (e, t) => Math.max(20, e.offsetHeight * t),
          ll = (0, a.memo)(
            ({
              api: e,
              classNames: t = {},
              getStepByRailClick: u = ol,
              onDrag: n = rl,
              isOnView: r,
            }) => {
              const s = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                d = (0, a.useRef)(null),
                _ = e.stepTimeout || 100,
                m = (0, a.useState)(al),
                E = m[0],
                A = m[1],
                g = (0, a.useCallback)(
                  (e) => {
                    (A(e),
                      d.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: d.current }));
                  },
                  [n],
                ),
                p = fi(() => {
                  const t = d.current,
                    u = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && t && u)) return;
                  const a = Math.min(1, n / r);
                  return (
                    (t.style.height = `${il(u, a)}px`),
                    t.classList.add(tl),
                    s.current &&
                      (1 === a ? s.current.classList.add(Zi) : s.current.classList.remove(Zi)),
                    a
                  );
                }),
                h = fi(() => {
                  const t = c.current,
                    u = d.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && u && r)) return;
                  const a = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / r),
                    s = Ka(0, 1, a / (r - n)),
                    _ = (t.offsetHeight - il(t, o)) * s;
                  ((u.style.transform = `translateY(${0 | _}px)`),
                    ((e) => {
                      if (i.current && l.current && c.current && d.current) {
                        if (0 === e)
                          return (i.current.classList.add(nl), void l.current.classList.remove(nl));
                        if (
                          ((t = c.current),
                          (u = d.current),
                          e - (t.offsetHeight - u.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(nl), void l.current.classList.add(nl));
                        var t, u;
                        (i.current.classList.remove(nl), l.current.classList.remove(nl));
                      }
                    })(_));
                }),
                C = fi(() => {
                  sl(e, () => {
                    (p(), h());
                  });
                });
              ((0, a.useEffect)(() => te(C)),
                (0, a.useEffect)(() => {
                  const t = () => {
                    sl(e, () => {
                      h();
                    });
                  };
                  let u = rl;
                  const n = () => {
                    (u(), (u = te(C)));
                  };
                  return (
                    e.events.on("recalculateContent", C),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (u(),
                        e.events.off("recalculateContent", C),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, a.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      r &&
                        sl(e, (u) => {
                          const r = c.current,
                            a = d.current,
                            o = e.getContainerSize();
                          if (!r || !a || !o) return;
                          const s = t.screenY - E.offset - r.getBoundingClientRect().y,
                            i = (s / r.offsetHeight) * o;
                          (e.scrollPosition.start({
                            scrollPosition: e.clampPosition(u, i),
                            reset: !0,
                            immediate: !0,
                            from: { scrollPosition: u.scrollTop },
                          }),
                            n({ type: "dragging", thumb: a, thumbOffset: s, contentOffset: i }));
                        });
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), g(al));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, E.offset, E.pending, r, n, g]));
              const F = yi((t) => e.applyStepTo(t), _, [e]),
                D = F[0],
                v = F[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const b = (e) => {
                e.target.classList.contains(nl) || fe(R.sounds.highlight());
              };
              return o().createElement(
                "div",
                { className: B()(Ki, t.base), ref: s, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: B()(Qi, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(nl) ||
                      0 !== e.button ||
                      (fe(R.sounds.play()), D(Ni.Next));
                  },
                  ref: i,
                  onMouseEnter: b,
                }),
                o().createElement(
                  "div",
                  {
                    className: B()(el, t.track),
                    onMouseDown: (t) => {
                      const n = d.current;
                      if (n && 0 === t.button)
                        if ((fe(R.sounds.play()), t.target === n))
                          g({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y });
                        else {
                          ((t) => {
                            d.current &&
                              sl(e, (n) => {
                                if (!n) return;
                                const r = u(e),
                                  a = e.clampPosition(n, n.scrollTop + r * t);
                                e.applyScroll(a);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? Ni.Prev : Ni.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: b,
                  },
                  o().createElement("div", { ref: d, className: t.thumb }),
                  o().createElement("div", { className: B()(ul, t.rail) }),
                ),
                o().createElement("div", {
                  className: B()(Ji, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(nl) ||
                      0 !== e.button ||
                      (fe(R.sounds.play()), D(Ni.Prev));
                  },
                  onMouseUp: v,
                  ref: l,
                  onMouseEnter: b,
                }),
              );
            },
          ),
          cl = {
            content: "VerticalScroll_content_dc",
            defaultScroll: "VerticalScroll_defaultScroll_3b",
            bar: "VerticalScroll_bar_bb",
            area: "VerticalScroll_area_d6",
          },
          dl = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: s,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, a.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: B()(cl.base, e.base) });
              }, [n]),
              _ = (0, a.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: B()(cl.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: B()(cl.area, r) },
                o().createElement(_l, { className: s, classNames: i, api: _ }, e),
              ),
              o().createElement(ll, { getStepByRailClick: l, api: t, onDrag: c, classNames: d }),
            );
          },
          _l = ({ className: e, classNames: t, children: u, api: n }) => (
            (0, a.useEffect)(() => te(n.recalculateContent)),
            o().createElement(
              "div",
              { className: B()(cl.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              o().createElement(
                "div",
                { className: B()(cl.content, null == t ? void 0 : t.content), ref: n.contentRef },
                u,
              ),
            )
          );
        _l.Default = dl;
        const ml = { Vertical: r, Horizontal: n },
          El = "ScrollDrag_base_55",
          Al = "ScrollDrag_base__grabbing_12",
          gl = "ScrollDrag_base__noDrag_02",
          pl = ({
            isPremiumAreaActive: e,
            isHorizontalScrollbarShown: t,
            isVerticalScrollBarShown: u,
            isDragging: n,
            horizontalApi: r,
            verticalApi: s,
            children: i,
            setIsDragging: l,
            onDrag: c,
          }) => {
            const d = (0, a.useState)(0),
              _ = d[0],
              m = d[1],
              E = (0, a.useState)(0),
              A = E[0],
              g = E[1],
              p = (0, a.useState)(0),
              h = p[0],
              C = p[1],
              F = (0, a.useState)(0),
              D = F[0],
              v = F[1],
              b = (0, a.useState)(!1),
              f = b[0],
              y = b[1];
            (0, a.useEffect)(
              () =>
                te(() => {
                  const e = (e) => {
                      const t = e.value.scrollPosition;
                      n || m(-t);
                    },
                    t = (e) => {
                      const t = e.value.scrollPosition;
                      n || C(-t);
                    };
                  return (
                    r.events.on("change", e),
                    s.events.on("change", t),
                    () => {
                      (r.events.off("change", e), s.events.off("change", t));
                    }
                  );
                }),
              [r, s, n],
            );
            return o().createElement(
              "div",
              {
                className: B()(El, n && Al, !u && !t && gl),
                onMouseDown: (e) => {
                  0 === e.nativeEvent.button && (y(!0), g(e.clientX), v(e.clientY));
                },
                onMouseUp: () => {
                  (l(!1), y(!1), g(0), v(0));
                },
                onMouseMove: (t) => {
                  if (f) {
                    l(!0);
                    const u = Ka(-(r.getBounds()[1] || 0), 0, _ + t.clientX - A);
                    if ((r.applyScroll(-u, !0), !e)) {
                      const e = Ka(-(s.getBounds()[1] || 0), 0, h + t.clientY - D);
                      (s.applyScroll(-e, !0), v(t.clientY), C(e));
                    }
                    (g(t.clientX), m(u), c());
                  }
                },
              },
              i,
            );
          },
          hl = (e) => (e < 0.5 ? 2 * e * e : 1 - Math.pow(-2 * e + 2, 2) / 2);
        viewEnv.clearInternalCacheAfterFinalize();
        const Cl = (0, we.Pi)(() => {
          const e = Je(),
            t = e.model,
            u = e.controls,
            n = t.root.get(),
            r = n.selectedNation,
            s = n.nationBlueprintsCount,
            l = n.universalBlueprintsCount,
            c = n.isBlueprintMode,
            d = n.isBlueprintModeEnabled,
            _ = n.isEarlyAccessPaused,
            m = n.isEarlyAccessFirstTimeShown,
            E = n.isParagonsEnabled,
            A = n.closePremiumPanelTrigger,
            g = t.paragonsEntryPoint.get(),
            p = g.isAnySelectableRewardInInventory,
            h = g.progressState,
            C = g.isAnySelectableReward,
            F = t.computes.paragonsEntryPointComputes,
            D = F.getCurrentChapter(),
            v = F.getLevelsCount(),
            b = F.getMaxPointsCount() || 0,
            y = F.getFreePoints(),
            w = F.getLevels(),
            N = t.isOnView.get(),
            S = t.hintProperties.get(),
            T = t.settings.get(),
            L = T.columnsNumber,
            k = T.rowsNumber,
            x = T.premiumRowsNumber,
            I = t.computes,
            M = I.getMainNodes,
            O = I.getPremiumNodes,
            H = I.getNodeById,
            z = I.getNodeConnectors,
            W = I.getRowData,
            G = I.getFirstNode,
            V = I.getInBattleNations,
            $ = I.getRowButtons,
            U = I.getLastParagonsUnLockedNodeId,
            j = (0, I.getParagonsUnlockedBranchToShow)(),
            X = U(),
            q = M(),
            Y = O(),
            K = $(),
            Z = t.paragonsHoveredNodes.get(),
            Q = (0, a.useMemo)(() => [...Array(L).keys()].map((e) => e + 1), [L]),
            J = (0, a.useMemo)(() => [...Array(k).keys()].map((e) => e + 1), [k]),
            ne = (0, a.useMemo)(() => [...Array(x).keys()], [x]),
            re = ce(),
            ae = P().mediaSize >= f.Medium;
          var ie;
          ((ie = u.onClose), le(se.n.ESCAPE, ie));
          const de = (0, a.useState)(!1),
            _e = de[0],
            me = de[1],
            Ee = (0, a.useState)(0),
            Ae = Ee[0],
            ge = Ee[1],
            pe = (0, a.useState)(!1),
            De = pe[0],
            ve = pe[1],
            ye = (0, a.useState)({ emptyRows: [], topEmptyRows: [] }),
            we = ye[0],
            Ne = ye[1],
            Se = (0, a.useState)(0),
            Te = Se[0],
            Le = Se[1],
            Re = (0, a.useState)(!1),
            ke = Re[0],
            xe = Re[1],
            Ie = (0, a.useState)(!1),
            Me = Ie[0],
            Oe = Ie[1];
          (0, a.useEffect)(() => {
            _e && (fe("researches_premium_panel_slide_out"), me(!1));
          }, [A]);
          const He = document.getElementById(qe.CONVERT),
            ze = ml.Horizontal.useHorizontalScrollApi(),
            We = ml.Vertical.useVerticalScrollApi(),
            Ge = (0, a.useCallback)(
              () =>
                (({ convertHint: e, setHintConvertProperties: t, convertHintProperties: u }) => {
                  e &&
                    (e.getBoundingClientRect().left > 160
                      ? (e.getBoundingClientRect().left > i.O.view.getSize().width &&
                          u.isInView &&
                          t({ isInView: !1 }),
                        e.getBoundingClientRect().left < i.O.view.getSize().width &&
                          !u.isInView &&
                          t({ isInView: !0 }),
                        u.direction !== Ye.LEFT_TO_RIGHT && t({ direction: Ye.LEFT_TO_RIGHT }))
                      : u.direction !== Ye.RIGHT_TO_LEFT && t({ direction: Ye.RIGHT_TO_LEFT }));
                })({
                  convertHint: He,
                  setHintConvertProperties: u.setHintConvertProperties,
                  convertHintProperties: S[qe.CONVERT],
                }),
              [u.setHintConvertProperties, He, S],
            ),
            Ve = oe(Ge, [Ge], 500);
          (0, a.useEffect)(() => {
            Ge();
          }, []);
          const $e = (0, a.useMemo)(
              () =>
                Object.assign({}, ze, {
                  handleMouseWheel: (e) => {
                    (ze.handleMouseWheel(e), Ve());
                  },
                }),
              [Ve, ze],
            ),
            Ue = ($e.contentRef.current ? $e.getBounds() : [0, 0])[1],
            je = Boolean(Ue),
            Xe = (0, a.useMemo)(
              () =>
                Object.assign({}, We, {
                  handleMouseWheel: je
                    ? (e) => {
                        e.preventDefault();
                      }
                    : We.handleMouseWheel,
                }),
              [We, je],
            );
          (({ id: e, horizontalApi: t, verticalApi: u, deps: n }) => {
            const r = () => {
                const u = document.getElementById(e);
                u &&
                  u.getBoundingClientRect().right + 120 > i.O.view.getSize().width &&
                  t.applyScroll(i.O.view.getSize().width);
              },
              o = () => {
                const t = document.getElementById(e);
                t &&
                  (t.getBoundingClientRect().top < 120 && u.applyScroll(0),
                  t.getBoundingClientRect().top > i.O.view.getSize().height - 250 &&
                    u.applyScroll(i.O.view.getSize().height));
              };
            ((0, a.useEffect)(() => {
              const n = setTimeout(() => {
                const n = document.getElementById(e);
                n &&
                  (n.getBoundingClientRect().right + 120 > i.O.view.getSize().width &&
                    t.applyScroll(i.O.view.getSize().width),
                  n.getBoundingClientRect().top < 120 && u.applyScroll(0),
                  n.getBoundingClientRect().top > i.O.view.getSize().height - 250 &&
                    u.applyScroll(i.O.view.getSize().height));
              }, 400);
              return () => {
                (clearTimeout(n),
                  t.events.off("resizeHandled", r),
                  u.events.off("resizeHandled", o));
              };
            }, n),
              t.events.on("resizeHandled", r),
              u.events.on("resizeHandled", o));
          })({ id: la, verticalApi: Xe, horizontalApi: $e, deps: [X || null] });
          const Ke = ((e, t) => {
            const u = he("tutorialModel.effects.items").filter((u) => {
              if (!u) return !1;
              const n = u.value,
                r = window.__featureId.toString();
              return n.componentId === e && n.type === t && n.viewId === r;
            });
            if (0 === u.length) return null;
            const n = Object.assign({}, u[0].value);
            return {
              effect: n,
              completeEffect: () => {
                (tutorialModel.onEffectCompleted({
                  componentId: e,
                  viewId: window.__featureId.toFixed(0),
                  effectType: t,
                  effectBuilder: n.builder,
                }),
                  t === Ce && window.tutorialApi && window.tutorialApi.updateComponents());
              },
            };
          })("BlueprintsTechtreeConvertButton", Fe);
          (0, a.useEffect)(
            () =>
              te(() => {
                null !== Ke && Ke.completeEffect();
              }),
            [Ke],
          );
          const Ze = be("BlueprintsTechtreeConvertButton", Be);
          ((0, a.useEffect)(() => {
            Ze && Ze.runTrigger(!0);
          }, [Ze]),
            (0, a.useEffect)(() => {
              let e = 0,
                t = -1;
              const u = G();
              J.forEach((u) => {
                const n = W(u),
                  r = W(J.length - u + 1);
                (0 === e && n.length && (e = u), -1 === t && r.length && (t = J.length - u + 1));
              });
              const n = Array.from({ length: e - 1 }, (e, t) => t + 1),
                r = Array.from({ length: J.length - t }, (e, t) => J.length - t);
              (Le(((null == u ? void 0 : u.row) || Math.floor(k / 2)) - n.length),
                Ne({ emptyRows: [...n, ...r], topEmptyRows: n }));
            }, [r]));
          const Qe = () => {
            (Oe(!0),
              !Y.length || c || ke || _e || (fe("researches_premium_panel_slide_in"), me(!0)));
          };
          (0, a.useEffect)(() => {
            ke || Me || me(!1);
          }, [ke]);
          const Pt = (0, a.useCallback)(() => {
              (u.onBlueprintModeChanged(!c), _e && me(!1));
            }, [u, c, _e]),
            Nt = V().includes(r),
            St = (0, a.useCallback)((e) => !we.emptyRows.some((t) => e === t), [we.emptyRows]),
            Tt = (0, Pe.useTransition)(r, {
              from: { opacity: 0 },
              enter: { opacity: 1 },
              config: { duration: 400, easing: hl },
              key: r,
            });
          (0, a.useEffect)(() => {
            const e = () => {
              const e = Xe.getWrapperSize() || 0,
                t = J.length - we.emptyRows.length;
              ve(53 * t > e / re - (Y.length ? 110 : 0) - (ae ? 123 : 107));
            };
            let t = ue;
            const u = () => {
              t = te(() => {
                const t = $e.getWrapperSize(),
                  u = $e.getContainerSize(),
                  n = Xe.getWrapperSize(),
                  r = Xe.getContainerSize();
                u && t && n && r && e();
              });
            };
            return (
              u(),
              $e.events.on("change", e),
              $e.events.on("resizeHandled", u),
              Xe.events.on("change", e),
              Xe.events.on("resizeHandled", u),
              () => {
                ($e.events.off("change", e),
                  $e.events.off("resizeHandled", u),
                  Xe.events.off("change", e),
                  Xe.events.off("resizeHandled", u),
                  t());
              }
            );
          }, [ae, c, re, we.emptyRows.length]);
          const Lt = (0, Pe.useSpring)({ to: { opacity: c ? 1 : 0 }, config: { duration: 150 } }),
            kt = (0, Pe.useSpring)({ to: { opacity: E && !c ? 1 : 0 }, config: { duration: 150 } });
          document.addEventListener("mouseout", (e) => {
            const t = e.relatedTarget;
            t && "HTML" !== (null == t ? void 0 : t.nodeName)
              ? N || u.setIsOnView(!0)
              : N && (u.setIsOnView(!1), _e && (Oe(!1), me(!1)));
          });
          const xt = (0, a.useMemo)(
            () =>
              J.slice(
                we.topEmptyRows.length ? we.topEmptyRows[we.topEmptyRows.length - 1] : 0,
                we.emptyRows.length ? we.emptyRows[we.emptyRows.length - 1] - 1 : J.length,
              ),
            [we.emptyRows, we.topEmptyRows, J],
          );
          return o().createElement(
            "div",
            { className: B()(et, c && vt) },
            o().createElement(
              "div",
              { className: wt },
              o().createElement(Rt, { isBlueprintMode: c }),
            ),
            o().createElement(
              pl,
              {
                isHorizontalScrollbarShown: je,
                isVerticalScrollBarShown: De,
                isDragging: ke,
                isPremiumAreaActive: _e,
                setIsDragging: xe,
                horizontalApi: $e,
                verticalApi: Xe,
                onDrag: Ge,
              },
              o().createElement(
                ml.Horizontal.Area,
                { api: $e },
                o().createElement(
                  "div",
                  { className: at },
                  o().createElement(
                    ml.Vertical.Area,
                    { api: Xe, classNames: { content: B()(At, De && pt, Y.length && gt) } },
                    Tt((e) =>
                      o().createElement(
                        Pe.animated.div,
                        { style: e },
                        o().createElement(
                          "div",
                          { className: B()(ot, 0 !== K.length && c && st) },
                          o().createElement("div", {
                            className: ht,
                            style: { "--rows-from-top": Te },
                          }),
                          Q.map((e) =>
                            o().createElement(Aa, {
                              key: e,
                              checkIsEmptyRow: St,
                              columnIndex: e,
                              isVerticalScrollBarShown: De,
                              levels: Q,
                              treeRows: J,
                              mainNodes: q,
                              setActiveLevel: ge,
                              isBlueprintMode: c,
                              isEarlyAccessPaused: _,
                              isEarlyAccessFirstTimeShown: m,
                              shouldInBattleShow: Nt,
                              getNodeById: H,
                              getNodeConnectors: z,
                              isDragging: ke,
                              hoveredParagonsReadyToResetBranch: Z,
                              paragonsUnlockedBranchToShowNodes:
                                null == j ? void 0 : j.unlockedVehicleCDs,
                            }),
                          ),
                          !c &&
                            0 !== K.length &&
                            o().createElement(
                              "div",
                              { className: Ct },
                              xt.map((e) => {
                                const t = K.find((t) => t.buttonRow === e);
                                return t
                                  ? o().createElement(
                                      "div",
                                      { className: Ft, key: e },
                                      o().createElement(vi, { rowButton: t }),
                                    )
                                  : o().createElement("div", { className: Ft, key: e });
                              }),
                            ),
                        ),
                      ),
                    ),
                  ),
                  !c &&
                    Boolean(Y.length) &&
                    o().createElement(
                      "div",
                      {
                        className: B()(tt, _e && ut, ke && !_e && nt, !je && rt),
                        onMouseLeave: () => {
                          (Oe(!1),
                            Y.length &&
                              !ke &&
                              _e &&
                              (fe("researches_premium_panel_slide_out"), me(!1)));
                        },
                      },
                      o().createElement(Ys, {
                        isPremiumAreaActive: _e,
                        isVerticalScrollBarShown: De,
                        levels: Q,
                        premiumRows: ne,
                        premiumNodes: Y,
                        onSetActiveLevel: ge,
                        onShowPremiumPanel: Qe,
                        isDragging: ke,
                        isRowButtons: Boolean(K.length),
                      }),
                    ),
                ),
                o().createElement(
                  "div",
                  { className: B()(ft, 0 !== K.length && yt) },
                  o().createElement(Ju, { activeLevel: Ae, levels: Q }),
                ),
              ),
            ),
            Boolean(Y.length) &&
              !c &&
              o().createElement(
                "div",
                { className: B()(tt, nt, _e && ut) },
                o().createElement(oi, { isPremiumAreaActive: _e }),
              ),
            o().createElement(
              "div",
              { className: dt, onMouseEnter: Qe },
              o().createElement(ml.Horizontal.Bar, { api: $e, onDrag: Ge, isOnView: N }),
            ),
            o().createElement(
              "div",
              { className: B()(_t, (c || !Y) && mt, (_e || !De) && Et) },
              o().createElement(ml.Vertical.Bar, { api: Xe, isOnView: N }),
            ),
            o().createElement(
              "div",
              { className: Bt },
              o().createElement(zs, null),
              E &&
                !c &&
                o().createElement(
                  Pe.animated.div,
                  { style: kt, className: bt },
                  o().createElement(
                    ee,
                    {
                      tooltipArgs: {
                        contentId: R.views.lobby.paragons.tooltips.EntryPointTooltip("resId"),
                      },
                    },
                    o().createElement(hs, {
                      isAnySelectableRewardInInventory: p,
                      progressState: h,
                      isAnySelectableReward: C,
                      levelsCount: v,
                      maxPointsCount: b,
                      currentChapter: D,
                      freePoints: y,
                      levels: w,
                      points: D.points,
                      onEntryPointClick: u.onEntryPointClick,
                    }),
                  ),
                ),
            ),
            o().createElement(
              "div",
              { className: it },
              o().createElement(Uu, { isBlueprintMode: c, isBlueprintModeEnabled: d, onClick: Pt }),
            ),
            o().createElement("div", { className: B()(lt, ke && ct) }, o().createElement(xs, null)),
            c &&
              o().createElement(
                Pe.animated.div,
                { style: Lt, className: Dt },
                o().createElement(vu, {
                  nationBlueprintsCount: s,
                  universalBlueprintsCount: l,
                  nation: r,
                }),
              ),
          );
        });
        engine.whenReady.then(() => {
          H().render(
            o().createElement(M, null, o().createElement(Qe, null, o().createElement(Cl, null))),
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
    (__webpack_require__.O = (e, t, u, n) => {
      if (!t) {
        var r = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, u, n] = deferred[i], a = !0, o = 0; o < t.length; o++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(i--, 1);
            var s = u();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > n; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, u, n];
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
    (__webpack_require__.j = 210),
    (() => {
      var e = { 210: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var n,
            r,
            [a, o, s] = u,
            i = 0;
          if (a.some((t) => 0 !== e[t])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (t && t(u); i < a.length; i++)
            ((r = a[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [904], () => __webpack_require__(686));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
