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
      527: (e, t, a) => {
        "use strict";
        (a.r(t), a.d(t, { mouse: () => s, onResize: () => r }));
        var n = a(2472),
          u = a(1176);
        const r = (0, n.E)("clientResized"),
          o = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, u.R)(!1);
          }
          function a() {
            e.enabled && (0, u.R)(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", a))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", a))
              : (0, u.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, a) => (
              (t[a] = (function (t) {
                return (a) => {
                  e.listeners += 1;
                  let u = !0;
                  const r = `mouse${t}`,
                    s = o[t]((e) => a([e, "outside"]));
                  function i(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    n(),
                    () => {
                      u &&
                        (s(), window.removeEventListener(r, i), (e.listeners -= 1), n(), (u = !1));
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
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
            },
            enableOutside() {
              e.enabled && (0, u.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, u.R)(!1);
            },
          });
        })();
      },
      5959: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => r,
            getSize: () => u,
            graphicsQuality: () => o,
          }));
        var n = a(527);
        function u(e = "px") {
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
      1176: (e, t, a) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        a.d(t, { R: () => n });
      },
      2472: (e, t, a) => {
        "use strict";
        function n(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        a.d(t, { E: () => n });
      },
      3138: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => u });
        var n = a(5959);
        const u = { view: a(7641), client: n };
      },
      3722: (e, t, a) => {
        "use strict";
        function n(e, t, a = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, a);
        }
        function u(e, t, a) {
          return `url(${n(e, t, a)})`;
        }
        (a.r(t), a.d(t, { getBgUrl: () => u, getTextureUrl: () => n }));
      },
      6112: (e, t, a) => {
        "use strict";
        a.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, a) => {
        "use strict";
        a.d(t, { U: () => u });
        var n = a(2472);
        const u = {
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
      7641: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => n,
            displayStatus: () => u.W,
            displayStatusIs: () => S,
            events: () => r.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => D,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => B,
            getScale: () => p,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => h,
            isEventHandled: () => F,
            isFocused: () => f,
            pxToRem: () => b,
            remToPx: () => A,
            resize: () => m,
            sendEvent: () => o.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => v,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => _,
            whenTutorialReady: () => y,
          }));
        var n = a(3722),
          u = a(6112),
          r = a(6538),
          o = a(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, a, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, a, n);
        }
        function c(e, t, a) {
          return viewEnv.addDataChangedCallback(e, t, a);
        }
        function _(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, t, a = "px") {
          return "rem" === a ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: A(t.x), y: A(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function p() {
          return viewEnv.getScale();
        }
        function b(e) {
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
        const S = Object.keys(u.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === u.W[t]), e),
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
          y = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        "use strict";
        a.d(t, { qP: () => l });
        const n = ["args"];
        const u = 2,
          r = 16,
          o = 32,
          s = 64,
          i = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    n,
                    u = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                  return u;
                })(t, n);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, o, {
                      arguments:
                        ((u = r),
                        Object.entries(u).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: a, type: e });
            var u;
          },
          l = {
            close(e) {
              i("popover" === e ? u : o);
            },
            minimize() {
              i(s);
            },
            move(e) {
              i(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      5521: (e, t, a) => {
        "use strict";
        let n, u;
        (a.d(t, { n: () => n }),
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
          })(u || (u = {})));
      },
      1358: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => r });
        var n = a(3138);
        class u {
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
            return (window.__dataTracker || (window.__dataTracker = new u()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, t, a = 0, u = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = n.O.view.addModelObserver(e, a, u);
            return (
              r > 0
                ? ((this._callbacks[r] = t),
                  a > 0 && (this._views[a] ? this._views[a].push(r) : (this._views[a] = [r])))
                : console.error("Can't add callback for model:", e),
              r
            );
          }
          removeCallback(e, t = 0) {
            let a = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((a = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              a || console.error("Can't remove callback by id:", e),
              a
            );
          }
          _emmitDataChanged(e, t, a) {
            a.forEach((a) => {
              const n = this._callbacks[a];
              void 0 !== n && n(e, t);
            });
          }
        }
        u.__instance = void 0;
        const r = u;
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
      4179: (e, t, a) => {
        "use strict";
        a.d(t, {
          Sw: () => r.Z,
          B3: () => l,
          Z5: () => o,
          B0: () => i,
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
                this.entries.forEach(({ container: t, callback: a }) => {
                  let n = e.target;
                  do {
                    if (n === t) return;
                    n = n.parentNode;
                  } while (n);
                  a();
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
            const a = e,
              n = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== a || t !== n,
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
        const u = n;
        var r = a(1358);
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
            getTimeFormat: (e, t, a) => userLocale.getTimeFormat(e, t, void 0 === a || a),
            getTimeString: (e, t, a) => userLocale.getTimeString(e, t, void 0 === a || a),
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
        var m = a(5521),
          E = a(3138);
        const g = ["args"];
        function p(e, t, a, n, u, r, o) {
          try {
            var s = e[r](o),
              i = s.value;
          } catch (e) {
            return void a(e);
          }
          s.done ? t(i) : Promise.resolve(i).then(n, u);
        }
        const b = (e) => ({
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
                    a = arguments;
                  return new Promise(function (n, u) {
                    var r = e.apply(t, a);
                    function o(e) {
                      p(r, n, u, o, s, "next", e);
                    }
                    function s(e) {
                      p(r, n, u, o, s, "throw", e);
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
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const u = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    n,
                    u = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                  return u;
                })(t, g);
              void 0 !== u
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, r, {
                      arguments:
                        ((n = u),
                        Object.entries(n).map(([e, t]) => {
                          const a = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              a.number = t;
                              break;
                            case "boolean":
                              a.bool = t;
                              break;
                            default:
                              a.string = t.toString();
                          }
                          return a;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: a, type: e });
            var n;
          },
          h = () => f(i.CLOSE),
          v = () => f(i.POP_OVER, { on: !1 }),
          F = (e, t, a, n, u = R.invalid("resId"), r) => {
            const o = E.O.view.getViewGlobalPosition(),
              s = a.getBoundingClientRect(),
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
            f(i.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: u,
              direction: t,
              bbox: b(m),
              on: !0,
              args: r,
            });
          },
          D = () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
          B = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var S = a(7572);
        const w = u.instance,
          y = {
            DataTracker: r.Z,
            ViewModel: S.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: b,
            sendMoveEvent: (e) => f(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: h,
            sendClosePopOverEvent: v,
            sendShowContextMenuEvent: (e, t, a = 0) => {
              f(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: a,
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
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: D,
            dumpViewModel: function e(t) {
              const a = {};
              if ("object" != typeof t) return t;
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const u = Object.prototype.toString.call(t[n]);
                  if (u.startsWith("[object CoherentArrayProxy]")) {
                    const u = t[n];
                    a[n] = [];
                    for (let t = 0; t < u.length; t++) a[n].push({ value: e(u[t].value) });
                  } else
                    u.startsWith("[object class BW::WULF::ViewModel")
                      ? (a[n] = e(t[n]))
                      : (a[n] = t[n]);
                }
              return a;
            },
            ClickOutsideManager: w,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = y;
      },
      9884: (e, t, a) => {
        "use strict";
        var n = {};
        (a.r(n),
          a.d(n, {
            Area: () => pe,
            Bar: () => me,
            DefaultScroll: () => ge,
            Direction: () => Z,
            defaultSettings: () => J,
            useHorizontalScrollApi: () => ee,
          }));
        var u = {};
        (a.r(u),
          a.d(u, {
            Area: () => xe,
            Bar: () => Ne,
            Default: () => Me,
            useVerticalScrollApi: () => be,
          }));
        var r = a(6179),
          o = a.n(r);
        const s = (e, t, a) =>
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
        var i = a(3138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function _(e, t, a) {
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
            })(e, a),
            u = (function (e, t) {
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
            r = Math.min(n, u);
          return {
            extraLarge: r === a.extraLarge.weight,
            large: r === a.large.weight,
            medium: r === a.medium.weight,
            small: r === a.small.weight,
            extraSmall: r === a.extraSmall.weight,
            extraLargeWidth: n === a.extraLarge.weight,
            largeWidth: n === a.large.weight,
            mediumWidth: n === a.medium.weight,
            smallWidth: n === a.small.weight,
            extraSmallWidth: n === a.extraSmall.weight,
            extraLargeHeight: u === a.extraLarge.weight,
            largeHeight: u === a.large.weight,
            mediumHeight: u === a.medium.weight,
            smallHeight: u === a.small.weight,
            extraSmallHeight: u === a.extraSmall.weight,
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
          p = (0, r.createContext)(g),
          b = ["children"];
        const A = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                u = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, b);
          const n = (0, r.useContext)(p),
            u = n.extraLarge,
            o = n.large,
            i = n.medium,
            l = n.small,
            c = n.extraSmall,
            _ = n.extraLargeWidth,
            d = n.largeWidth,
            m = n.mediumWidth,
            E = n.smallWidth,
            g = n.extraSmallWidth,
            A = n.extraLargeHeight,
            C = n.largeHeight,
            f = n.mediumHeight,
            h = n.smallHeight,
            v = n.extraSmallHeight,
            F = { extraLarge: A, large: C, medium: f, small: h, extraSmall: v };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && u) return t;
            if (a.large && o) return t;
            if (a.medium && i) return t;
            if (a.small && l) return t;
            if (a.extraSmall && c) return t;
          } else {
            if (a.extraLargeWidth && _) return s(t, a, F);
            if (a.largeWidth && d) return s(t, a, F);
            if (a.mediumWidth && m) return s(t, a, F);
            if (a.smallWidth && E) return s(t, a, F);
            if (a.extraSmallWidth && g) return s(t, a, F);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && A) return t;
              if (a.largeHeight && C) return t;
              if (a.mediumHeight && f) return t;
              if (a.smallHeight && h) return t;
              if (a.extraSmallHeight && v) return t;
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
          f = (0, r.memo)(({ children: e }) => {
            const t = (0, r.useContext)(p),
              a = (0, r.useState)(t),
              n = a[0],
              u = a[1],
              s = (0, r.useCallback)((e, t) => {
                const a = i.O.view.pxToRem(e),
                  n = i.O.view.pxToRem(t);
                u(Object.assign({ width: a, height: n }, _(a, n, l)));
              }, []);
            (C(() => {
              engine.on("clientResized", s);
            }),
              (0, r.useEffect)(() => () => engine.off("clientResized", s), [s]));
            const c = (0, r.useMemo)(() => Object.assign({}, n), [n]);
            return o().createElement(p.Provider, { value: c }, e);
          });
        var h = a(6483),
          v = a.n(h),
          F = a(926),
          D = a.n(F);
        let B, S, w;
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
          })(w || (w = {})));
        const y = () => {
            const e = (0, r.useContext)(p),
              t = e.width,
              a = e.height,
              n = ((e) => {
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
              u = ((e) => {
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
              mediaWidth: u,
              mediaHeight: o,
              remScreenWidth: t,
              remScreenHeight: a,
            };
          },
          k = ["children", "className"];
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
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
            [w.ExtraSmall]: "",
            [w.Small]: D().SMALL_HEIGHT,
            [w.Medium]: `${D().SMALL_HEIGHT} ${D().MEDIUM_HEIGHT}`,
            [w.Large]: `${D().SMALL_HEIGHT} ${D().MEDIUM_HEIGHT} ${D().LARGE_HEIGHT}`,
            [w.ExtraLarge]: `${D().SMALL_HEIGHT} ${D().MEDIUM_HEIGHT} ${D().LARGE_HEIGHT} ${D().EXTRA_LARGE_HEIGHT}`,
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
              a = e.className,
              n = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, k);
            const u = y(),
              r = u.mediaWidth,
              s = u.mediaHeight,
              i = u.mediaSize;
            return o().createElement("div", T({ className: v()(a, N[r], I[s], M[i]) }, n), t);
          },
          O = ["children"];
        const L = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                u = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, O);
          return o().createElement(f, null, o().createElement(x, a, t));
        };
        var P = a(493),
          H = a.n(P);
        const W = (e) => {
            let t,
              a = null;
            return (
              (a = requestAnimationFrame(() => {
                a = requestAnimationFrame(() => {
                  ((a = null), (t = e()));
                });
              })),
              () => {
                ("function" == typeof t && t(), null !== a && cancelAnimationFrame(a));
              }
            );
          },
          z = (e, t, a) => (a < e ? e : a > t ? t : a),
          V = [];
        function U(e) {
          const t = (0, r.useRef)(e);
          return (
            (0, r.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, r.useCallback)((...e) => (0, t.current)(...e), V)
          );
        }
        function G(e, t, a = []) {
          const n = (0, r.useRef)(0),
            u = (0, r.useCallback)(() => window.clearInterval(n.current), a || []);
          (0, r.useEffect)(() => u, [u]);
          const o = (null != a ? a : []).concat([t]);
          return [
            (0, r.useCallback)((a) => {
              ((n.current = window.setInterval(() => e(a, !0), t)), e(a, !1));
            }, o),
            u,
          ];
        }
        function j(e) {
          engine.call("PlaySound", e);
        }
        const $ = {
          playHighlight() {
            j("highlight");
          },
          playClick() {
            j("play");
          },
          playYes() {
            j("yes1");
          },
        };
        function X(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return q(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return q(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function q(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        function Y(e, t, a) {
          const n = (0, r.useMemo)(
            () =>
              (function (e, t, a, n) {
                let u,
                  r = !1,
                  o = 0;
                function s() {
                  u && clearTimeout(u);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - o;
                  function _() {
                    ((o = Date.now()), a.apply(l, i));
                  }
                  r ||
                    (n && !u && _(),
                    s(),
                    void 0 === n && c > e
                      ? _()
                      : !0 !== t &&
                        (u = setTimeout(
                          n
                            ? function () {
                                u = void 0;
                              }
                            : _,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((n = a), (a = t), (t = void 0)),
                  (i.cancel = function () {
                    (s(), (r = !0));
                  }),
                  i
                );
              })(a, e),
            t,
          );
          return ((0, r.useEffect)(() => n.cancel, [n]), n);
        }
        var K = a(7030);
        let Z;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Z || (Z = {}));
        const J = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          Q = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: a,
            getDirection: n,
            getWrapperSize: u,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const s = (e, a) => {
              const n = t(e),
                u = n[0],
                r = n[1];
              return z(u, r, a);
            };
            return (l = {}) => {
              const c = l.settings,
                _ = void 0 === c ? J : c,
                d = (0, r.useRef)(null),
                m = (0, r.useRef)(null),
                E = (() => {
                  const e = (0, r.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    a = (e, a) => {
                      t(e).set(a, a);
                    },
                    n = (e, a) => {
                      t(e).delete(a);
                    },
                    u = (e, ...a) => {
                      for (var n, u = X(t(e).values()); !(n = u()).done;) (0, n.value)(...a);
                    };
                  return (0, r.useMemo)(() => ({ on: a, off: n, trigger: u }), []);
                })(),
                g = Y(
                  () => {
                    i.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                p = (0, K.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = d.current;
                    t && (a(t, e), E.trigger("change", e), o && g());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                b = p[0],
                A = p[1],
                C = (0, r.useCallback)(
                  (e, t, a) => {
                    var n;
                    const u = b.scrollPosition.get(),
                      r = (null != (n = b.scrollPosition.goal) ? n : 0) - u;
                    return s(e, t * a + r + u);
                  },
                  [b.scrollPosition],
                ),
                f = (0, r.useCallback)(
                  (e, { immediate: t = !1, reset: a = !0 } = {}) => {
                    const n = d.current;
                    n &&
                      A.start({
                        scrollPosition: s(n, e),
                        immediate: t,
                        reset: a,
                        config: _.animationConfig,
                        from: { scrollPosition: s(n, b.scrollPosition.get()) },
                      });
                  },
                  [A, _.animationConfig, b.scrollPosition],
                ),
                h = (0, r.useCallback)(
                  (e) => {
                    const t = d.current,
                      a = m.current;
                    if (!t || !a) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return u(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(a, _.step),
                      r = C(t, e, n);
                    f(r);
                  },
                  [f, C, _.step],
                ),
                v = (0, r.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && h(n(e)),
                      d.current && E.trigger("mouseWheel", e, b.scrollPosition, t(d.current)));
                  },
                  [b.scrollPosition, h, E],
                ),
                F = ((e, t = []) => {
                  const a = (0, r.useRef)(),
                    n = (0, r.useCallback)((...t) => {
                      (a.current && a.current(), (a.current = e(...t)));
                    }, t);
                  return (
                    (0, r.useEffect)(
                      () => () => {
                        a.current && a.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    W(() => {
                      const e = d.current;
                      e &&
                        (f(s(e, b.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [f, b.scrollPosition.goal],
                ),
                D = U(() => {
                  const e = d.current;
                  if (!e) return;
                  const t = s(e, b.scrollPosition.goal);
                  (t !== b.scrollPosition.goal && f(t, { immediate: !0 }),
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
                  getWrapperSize: () => (m.current ? u(m.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? t(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: _.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: v,
                  applyScroll: f,
                  applyStepTo: h,
                  contentRef: d,
                  wrapperRef: m,
                  scrollPosition: A,
                  animationScroll: b,
                  recalculateContent: D,
                  handleIsThumbDragging: B,
                  events: { on: E.on, off: E.off },
                }),
                [b.scrollPosition, f, h, B, E.off, E.on, D, v, A, _.step.clampedArrowStepTimeout],
              );
            };
          },
          ee = Q({
            getBounds: (e) => {
              var t, a;
              return [
                0,
                e.offsetWidth -
                  (null != (t = null == (a = e.parentElement) ? void 0 : a.offsetWidth) ? t : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, t) => {
              e.style.transform = `translateX(-${t.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? Z.Next : Z.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          te = "HorizontalBar_base_49",
          ae = "HorizontalBar_base__nonActive_82",
          ne = "HorizontalBar_leftButton_5f",
          ue = "HorizontalBar_rightButton_03",
          re = "HorizontalBar_track_0d",
          oe = "HorizontalBar_thumb_fd",
          se = "HorizontalBar_rail_32",
          ie = "disable",
          le = { pending: !1, offset: 0 },
          ce = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          _e = () => {},
          de = (e, t) => Math.max(20, e.offsetWidth * t),
          me = (0, r.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = ce, onDrag: n = _e }) => {
              const u = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, r.useState)(le),
                m = d[0],
                E = d[1],
                g = (0, r.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                p = () => {
                  const t = l.current,
                    a = c.current,
                    n = e.getWrapperSize(),
                    u = e.getContainerSize();
                  if (!(n && t && a && u)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / u),
                    _ = z(0, 1, r / (u - n)),
                    d = (t.offsetWidth - de(t, o)) * _;
                  ((a.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (s.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (s.current.classList.add(ie), void i.current.classList.remove(ie));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetWidth - a.offsetWidth) >= -0.5)
                        )
                          return (s.current.classList.remove(ie), void i.current.classList.add(ie));
                        var t, a;
                        (s.current.classList.remove(ie), i.current.classList.remove(ie));
                      }
                    })(d));
                },
                b = U(() => {
                  ((() => {
                    const t = c.current,
                      a = l.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && n && a)) return;
                    const o = Math.min(1, n / r);
                    ((t.style.width = `${de(a, o)}px`),
                      (t.style.display = "flex"),
                      u.current &&
                        (1 === o ? u.current.classList.add(ae) : u.current.classList.remove(ae)));
                  })(),
                    p());
                });
              ((0, r.useEffect)(() => W(b)),
                (0, r.useEffect)(
                  () =>
                    W(() => {
                      const t = () => {
                        p();
                      };
                      let a = _e;
                      const n = () => {
                        (a(), (a = W(b)));
                      };
                      return (
                        e.events.on("recalculateContent", b),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (a(),
                            e.events.off("recalculateContent", b),
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
                      var a;
                      const u = e.contentRef.current;
                      if (!u) return;
                      const r = l.current,
                        o = c.current;
                      if (!u || !r || !o) return;
                      const s = t.screenX - m.offset - r.getBoundingClientRect().x,
                        i = (s / r.offsetWidth) * (null != (a = e.getContainerSize()) ? a : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(u, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: o, thumbOffset: s, contentOffset: i }));
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t), g(le));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, m.offset, m.pending, n, g]));
              const A = G((t) => e.applyStepTo(t), _, [e]),
                C = A[0],
                f = A[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", f, !0),
                  () => document.removeEventListener("mouseup", f, !0)
                ),
                [f],
              );
              const h = (e) => {
                e.target.classList.contains(ie) || j("highlight");
              };
              return o().createElement(
                "div",
                { className: v()(te, t.base), ref: u, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: v()(ne, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(ie) || 0 !== e.button || (j("play"), C(Z.Next));
                  },
                  onMouseUp: f,
                  ref: s,
                  onMouseEnter: h,
                }),
                o().createElement(
                  "div",
                  {
                    className: v()(re, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if ((j("play"), t.target === n))
                          g({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = c.current,
                              u = e.contentRef.current;
                            if (!n || !u) return;
                            const r = a(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * t);
                          })(t.screenX > n.getBoundingClientRect().x ? Z.Prev : Z.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: h,
                  },
                  o().createElement("div", { ref: c, className: v()(oe, t.thumb) }),
                  o().createElement("div", { className: v()(se, t.rail) }),
                ),
                o().createElement("div", {
                  className: v()(ue, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(ie) || 0 !== e.button || (j("play"), C(Z.Prev));
                  },
                  onMouseUp: f,
                  ref: i,
                  onMouseEnter: h,
                }),
              );
            },
          ),
          Ee = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          ge = ({
            children: e,
            api: t,
            className: a,
            barClassNames: n,
            areaClassName: u,
            classNames: s,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, r.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: v()(Ee.base, e.base) });
              }, [n]),
              d = (0, r.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: v()(Ee.defaultScroll, a), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: v()(Ee.defaultScrollArea, u) },
                o().createElement(pe, { className: i, api: d, classNames: s }, e),
              ),
              o().createElement(me, { getStepByRailClick: l, api: t, onDrag: c, classNames: _ }),
            );
          },
          pe = ({ api: e, className: t, classNames: a, children: n, style: u }) => (
            (0, r.useEffect)(() => W(e.recalculateContent)),
            o().createElement(
              "div",
              { className: v()(Ee.base, t), style: u },
              o().createElement(
                "div",
                {
                  className: v()(Ee.wrapper, null == a ? void 0 : a.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: v()(Ee.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((pe.Bar = me),
          (pe.Default = ge),
          (pe.SeniorityAwards = ({ api: e, className: t, classNames: a, children: n }) => (
            (0, r.useEffect)(() => W(e.recalculateContent)),
            o().createElement(
              "div",
              { className: v()(Ee.base, t) },
              o().createElement(
                "div",
                { className: v()(Ee.wrapper, null == a ? void 0 : a.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: v()(Ee.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const be = Q({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Z.Next : Z.Prev),
          }),
          Ae = "VerticalBar_base_f3",
          Ce = "VerticalBar_base__nonActive_42",
          fe = "VerticalBar_topButton_d7",
          he = "VerticalBar_bottomButton_06",
          ve = "VerticalBar_track_df",
          Fe = "VerticalBar_thumb_32",
          De = "VerticalBar_rail_43",
          Be = "disable",
          Se = () => {},
          we = { pending: !1, offset: 0 },
          ye = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          ke = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          Te = (e, t) => Math.max(20, e.offsetHeight * t),
          Ne = (0, r.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = ye, onDrag: n = Se }) => {
              const u = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, r.useState)(we),
                m = d[0],
                E = d[1],
                g = (0, r.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                p = U(() => {
                  const t = c.current,
                    a = l.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && t && a)) return;
                  const o = Math.min(1, n / r);
                  return (
                    (t.style.height = `${Te(a, o)}px`),
                    t.classList.add(Fe),
                    u.current &&
                      (1 === o ? u.current.classList.add(Ce) : u.current.classList.remove(Ce)),
                    o
                  );
                }),
                b = U(() => {
                  const t = l.current,
                    a = c.current,
                    n = e.getWrapperSize(),
                    u = e.getContainerSize();
                  if (!(n && t && a && u)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / u),
                    _ = z(0, 1, r / (u - n)),
                    d = (t.offsetHeight - Te(t, o)) * _;
                  ((a.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (s.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (s.current.classList.add(Be), void i.current.classList.remove(Be));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetHeight - a.offsetHeight) >= -0.5)
                        )
                          return (s.current.classList.remove(Be), void i.current.classList.add(Be));
                        var t, a;
                        (s.current.classList.remove(Be), i.current.classList.remove(Be));
                      }
                    })(d));
                }),
                A = U(() => {
                  ke(e, () => {
                    (p(), b());
                  });
                });
              ((0, r.useEffect)(() => W(A)),
                (0, r.useEffect)(() => {
                  const t = () => {
                    ke(e, () => {
                      b();
                    });
                  };
                  let a = Se;
                  const n = () => {
                    (a(), (a = W(A)));
                  };
                  return (
                    e.events.on("recalculateContent", A),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (a(),
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
                      ke(e, (a) => {
                        const u = l.current,
                          r = c.current,
                          o = e.getContainerSize();
                        if (!u || !r || !o) return;
                        const s = t.screenY - m.offset - u.getBoundingClientRect().y,
                          i = (s / u.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(a, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: a.scrollTop },
                        }),
                          n({ type: "dragging", thumb: r, thumbOffset: s, contentOffset: i }));
                      });
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        g(we));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, m.offset, m.pending, n, g]));
              const C = G((t) => e.applyStepTo(t), _, [e]),
                f = C[0],
                h = C[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const F = (e) => {
                e.target.classList.contains(Be) || j("highlight");
              };
              return o().createElement(
                "div",
                { className: v()(Ae, t.base), ref: u, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: v()(fe, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Be) || 0 !== e.button || (j("play"), f(Z.Next));
                  },
                  ref: s,
                  onMouseEnter: F,
                }),
                o().createElement(
                  "div",
                  {
                    className: v()(ve, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if ((j("play"), t.target === n))
                          (e.handleIsThumbDragging(!0),
                            g({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              ke(e, (n) => {
                                if (!n) return;
                                const u = a(e),
                                  r = e.clampPosition(n, n.scrollTop + u * t);
                                e.applyScroll(r);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? Z.Prev : Z.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: F,
                  },
                  o().createElement("div", { ref: c, className: t.thumb }),
                  o().createElement("div", { className: v()(De, t.rail) }),
                ),
                o().createElement("div", {
                  className: v()(he, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Be) || 0 !== e.button || (j("play"), f(Z.Prev));
                  },
                  onMouseUp: h,
                  ref: i,
                  onMouseEnter: F,
                }),
              );
            },
          ),
          Ie = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Me = ({
            children: e,
            api: t,
            className: a,
            barClassNames: n,
            areaClassName: u,
            scrollClassName: s,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, r.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: v()(Ie.base, e.base) });
              }, [n]),
              d = (0, r.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: v()(Ie.defaultScroll, a), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: v()(Ie.area, u) },
                o().createElement(xe, { className: s, classNames: i, api: d }, e),
              ),
              o().createElement(Ne, { getStepByRailClick: l, api: t, onDrag: c, classNames: _ }),
            );
          },
          xe = ({ className: e, classNames: t, children: a, api: n }) => (
            (0, r.useEffect)(() => W(n.recalculateContent)),
            o().createElement(
              "div",
              { className: v()(Ie.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              o().createElement(
                "div",
                { className: v()(Ie.content, null == t ? void 0 : t.content), ref: n.contentRef },
                a,
              ),
            )
          );
        xe.Default = Me;
        const Oe = { Vertical: u, Horizontal: n };
        var Le = a(3403);
        const Re = { type: "idle" };
        const Pe = {
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
          He = [
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
        function We() {
          return (
            (We =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            We.apply(this, arguments)
          );
        }
        class ze extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && j(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && j(this.props.soundClick));
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
              a = e.onClick,
              n = e.goto,
              u = e.side,
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
                  var a,
                    n,
                    u = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                  return u;
                })(e, He)),
              m = v()(Pe.base, Pe[`base__${r}`], Pe[`base__${u}`], null == s ? void 0 : s.base),
              E = v()(Pe.icon, Pe[`icon__${r}`], Pe[`icon__${u}`], null == s ? void 0 : s.icon),
              g = v()(Pe.glow, null == s ? void 0 : s.glow),
              p = v()(Pe.caption, Pe[`caption__${r}`], null == s ? void 0 : s.caption),
              b = v()(Pe.goto, null == s ? void 0 : s.goto);
            return o().createElement(
              "div",
              We(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: a,
                },
                d,
              ),
              "info" !== r && o().createElement("div", { className: Pe.shine }),
              o().createElement(
                "div",
                { className: E },
                o().createElement("div", { className: g }),
              ),
              o().createElement("div", { className: p }, t),
              n && o().createElement("div", { className: b }, n),
            );
          }
        }
        ze.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const Ve = "EscBtn_base_d0",
          Ue = "EscBtn_esc_97",
          Ge = "EscBtn_close_90",
          je = (0, r.memo)(({ mixClass: e, soundClick: t = "play", onCloseCallback: a }) => {
            const n = v()(Ve, e);
            return o().createElement(
              "div",
              { className: n },
              o().createElement(ze, {
                caption: "",
                type: "close",
                soundClick: t,
                onClick: a,
                classNames: { base: Ge },
              }),
              o().createElement("div", { className: Ue }),
            );
          });
        function $e() {
          return !1;
        }
        console.log;
        var Xe = a(9174);
        function qe(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Ye(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return Ye(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Ye(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        const Ke = (e) => (0 === e ? window : window.subViews.get(e));
        const Ze = () => (e, t) => {
          const a = (0, r.createContext)({});
          return [
            function ({ mode: n = "real", options: u, children: s, mocks: l }) {
              const c = (0, r.useRef)([]),
                _ = (a, n, u) => {
                  var r;
                  const o = (function ({
                      initializer: e = !0,
                      rootId: t = 0,
                      getRoot: a = Ke,
                      context: n = "model",
                    } = {}) {
                      const u = new Map();
                      function r(e, t = 0) {
                        viewEnv.removeDataChangedCallback(e, t)
                          ? u.delete(e)
                          : console.error("Can't remove callback by id:", e);
                      }
                      engine.whenReady.then(() => {
                        engine.on("viewEnv.onDataChanged", (e, t, a) => {
                          a.forEach((t) => {
                            const a = u.get(t);
                            void 0 !== a && a(e);
                          });
                        });
                      });
                      const o = (e) => {
                        const u = a(t),
                          r = n.split(".").reduce((e, t) => e[t], u);
                        return "string" != typeof e || 0 === e.length
                          ? r
                          : e.split(".").reduce((e, t) => {
                              const a = e[t];
                              return "function" == typeof a ? a.bind(e) : a;
                            }, r);
                      };
                      return {
                        subscribe: (a, r) => {
                          const s = "string" == typeof r ? `${n}.${r}` : n,
                            l = i.O.view.addModelObserver(s, t, !0);
                          return (u.set(l, a), e && a(o(r)), l);
                        },
                        readByPath: o,
                        createCallback: (e, t) => {
                          const a = o(t);
                          return (...t) => {
                            a(e(...t));
                          };
                        },
                        createCallbackNoArgs: (e) => {
                          const t = o(e);
                          return () => {
                            t();
                          };
                        },
                        dispose: function () {
                          for (var e, a = qe(u.keys()); !(e = a()).done;) r(e.value, t);
                        },
                        unsubscribe: r,
                      };
                    })(n),
                    s =
                      "real" === a
                        ? o
                        : Object.assign({}, o, {
                            readByPath: null != (r = null == u ? void 0 : u.getter) ? r : () => {},
                          }),
                    l = (e) =>
                      "mocks" === a ? (null == u ? void 0 : u.getter(e)) : s.readByPath(e),
                    _ = (e) => c.current.push(e),
                    d = e({
                      mode: a,
                      readByPath: l,
                      externalModel: s,
                      observableModel: {
                        array: (e, t) => {
                          const n = null != t ? t : l(e),
                            u = Xe.LO.box(n, { equals: $e });
                          return (
                            "real" === a &&
                              s.subscribe(
                                (0, Xe.aD)((e) => u.set(e)),
                                e,
                              ),
                            u
                          );
                        },
                        object: (e, t) => {
                          const n = null != t ? t : l(e),
                            u = Xe.LO.box(n, { equals: $e });
                          return (
                            "real" === a &&
                              s.subscribe(
                                (0, Xe.aD)((e) => u.set(e)),
                                e,
                              ),
                            u
                          );
                        },
                        primitives: (e, t) => {
                          const n = l(t);
                          if (Array.isArray(e)) {
                            const u = e.reduce((e, t) => ((e[t] = Xe.LO.box(n[t], {})), e), {});
                            return (
                              "real" === a &&
                                s.subscribe(
                                  (0, Xe.aD)((t) => {
                                    e.forEach((e) => {
                                      u[e].set(t[e]);
                                    });
                                  }),
                                  t,
                                ),
                              u
                            );
                          }
                          {
                            const u = e,
                              r = Object.entries(u),
                              o = r.reduce((e, [t, a]) => ((e[a] = Xe.LO.box(n[t], {})), e), {});
                            return (
                              "real" === a &&
                                s.subscribe(
                                  (0, Xe.aD)((e) => {
                                    r.forEach(([t, a]) => {
                                      o[a].set(e[t]);
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
                    m = { mode: a, model: d, externalModel: s, cleanup: _ };
                  return {
                    model: d,
                    controls: "mocks" === a && u ? u.controls(m) : t(m),
                    externalModel: s,
                    mode: a,
                  };
                },
                d = (0, r.useRef)(!1),
                m = (0, r.useState)(n),
                E = m[0],
                g = m[1],
                p = (0, r.useState)(() => _(n, u, l)),
                b = p[0],
                A = p[1];
              return (
                (0, r.useEffect)(() => {
                  d.current ? A(_(E, u, l)) : (d.current = !0);
                }, [l, E, u]),
                (0, r.useEffect)(() => {
                  g(n);
                }, [n]),
                (0, r.useEffect)(
                  () => () => {
                    (b.externalModel.dispose(), c.current.forEach((e) => e()));
                  },
                  [b],
                ),
                o().createElement(a.Provider, { value: b }, s)
              );
            },
            () => (0, r.useContext)(a),
          ];
        };
        function Je(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function Qe(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, a, n) => t(null == e ? void 0 : e.value, a, n));
        }
        function et(e, t) {
          for (let a = 0; a < e.length; a++) {
            const n = Je(e[a]);
            if (t(n, a, e)) return n;
          }
        }
        const tt = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? Qe(e, (e) => ("object" == typeof e ? tt(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? tt(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? tt(t) : t]),
                    )
              : e,
          at = (e) => tt(e);
        var nt = a(3946);
        const ut = Ze()(
            ({ observableModel: e }) => {
              const t = { root: e.object(), seasons: e.array("seasons") },
                a = (0, nt.Om)(() => at(t.seasons.get()), { equals: $e });
              return Object.assign({}, t, { computes: { getSeasonsItemsList: a } });
            },
            ({ externalModel: e }) => ({
              close: e.createCallbackNoArgs("onCloseAction"),
              selectItem: e.createCallback(
                (e, t, a) => ({ itemID: e, selected: t, season: a }),
                "onSelectItem",
              ),
            }),
          ),
          rt = ut[0],
          ot = ut[1],
          st = "App_base_38",
          it = "App_scratches_bc",
          lt = "App_close_44",
          ct = "App_contentWrapper_cf",
          _t = "App_contentWrapper__maskTop_ac",
          dt = "App_contentWrapper__maskBottom_c5",
          mt = "App_contentWrapper__fullMask_90",
          Et = "App_content_e9",
          gt = "App_content__defaultCursor_a8",
          pt = "App_categories_26",
          bt = "App_divider_6e",
          At = "App_cards_ef",
          Ct = "App_bar_6c",
          ft = "App_lip_f7",
          ht = "App_slot_08";
        var vt = a(9887),
          Ft = a.n(vt);
        const Dt = ["xl", "lg", "md", "sm", "xs"],
          Bt = (e) => e.includes("_") && ((e) => Dt.includes(e))(e.split("_").at(-1)),
          St = [B.ExtraLarge, B.Large, B.Medium, B.Small, B.ExtraSmall],
          wt = (e, t) =>
            Object.keys(e).reduce((a, n) => {
              if (n in a) return a;
              if (Bt(n)) {
                const u = n.split("_").slice(0, -1).join("_");
                if (u in a) return a;
                const r = St.indexOf(t),
                  o = (-1 !== r ? Dt.slice(r) : [])
                    .map((e) => u + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  s = o ? e[o] : void 0;
                return ((a[u] = void 0 !== s ? s : e[u]), a);
              }
              const u = e[n];
              return (
                void 0 === u ||
                  ((e, t) => Dt.some((a) => void 0 !== t[`${e}_${a}`]))(n, e) ||
                  (a[n] = u),
                a
              );
            }, {}),
          yt = (e, t = wt) => {
            const a = (
              (e, t = wt) =>
              (a) => {
                const n = y().mediaSize,
                  u = (0, r.useMemo)(() => t(a, n), [a, n]);
                return o().createElement(e, u);
              }
            )(e, t);
            return o().memo((t) =>
              Object.keys(t).some((e) => Bt(e) && void 0 !== t[e])
                ? o().createElement(a, t)
                : o().createElement(e, t),
            );
          },
          kt = {
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
          Tt = [
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
        function Nt() {
          return (
            (Nt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Nt.apply(this, arguments)
          );
        }
        Object.keys(Ft());
        const It = {
            XL: { mt: kt.mt__XL, mr: kt.mr__XL, mb: kt.mb__XL, ml: kt.ml__XL },
            LG: { mt: kt.mt__LG, mr: kt.mr__LG, mb: kt.mb__LG, ml: kt.ml__LG },
            MDp: { mt: kt.mt__MDp, mr: kt.mr__MDp, mb: kt.mb__MDp, ml: kt.ml__MDp },
            MD: { mt: kt.mt__MD, mr: kt.mr__MD, mb: kt.mb__MD, ml: kt.ml__MD },
            SMp: { mt: kt.mt__SMp, mr: kt.mr__SMp, mb: kt.mb__SMp, ml: kt.ml__SMp },
            SM: { mt: kt.mt__SM, mr: kt.mr__SM, mb: kt.mb__SM, ml: kt.ml__SM },
            XS: { mt: kt.mt__XS, mr: kt.mr__XS, mb: kt.mb__XS, ml: kt.ml__XS },
          },
          Mt = (Object.keys(It), ["mt", "mr", "mb", "ml"]),
          xt = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Ot = yt((e) => {
            let t = e.className,
              a = e.width,
              n = e.height,
              u = e.m,
              s = e.mt,
              i = void 0 === s ? u : s,
              l = e.mr,
              c = void 0 === l ? u : l,
              _ = e.mb,
              d = void 0 === _ ? u : _,
              m = e.ml,
              E = void 0 === m ? u : m,
              g = e.column,
              p = e.row,
              b = e.flexDirection,
              A = void 0 === b ? (g ? "column" : p && "row") || void 0 : b,
              C = e.flexStart,
              f = e.center,
              h = e.flexEnd,
              F = e.spaceBetween,
              D = e.spaceAround,
              B = e.justifyContent,
              S =
                void 0 === B
                  ? (C ? "flex-start" : f && "center") ||
                    (h && "flex-end") ||
                    (F && "space-between") ||
                    (D && "space-around") ||
                    void 0
                  : B,
              w = e.alignItems,
              y =
                void 0 === w
                  ? (C ? "flex-start" : f && "center") || (h && "flex-end") || void 0
                  : w,
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
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Tt);
            const W = (0, r.useMemo)(() => {
                const e = { mt: i, mr: c, mb: d, ml: E },
                  t = ((e) =>
                    Mt.reduce((t, a) => {
                      const n = e[a];
                      return n && "number" != typeof n ? t.concat(It[!0 === n ? "MD" : n][a]) : t;
                    }, []))(e),
                  u = ((e) =>
                    Mt.reduce((t, a) => {
                      const n = e[a];
                      return ("number" == typeof n && (t[xt[a]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, R, u, {
                    width: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: L,
                    alignSelf: k,
                    display: A || y ? "flex" : void 0,
                    flexDirection: A,
                    flexWrap: I,
                    justifyContent: S,
                    alignItems: y,
                  }),
                  computedClassNames: t,
                };
              }, [a, n, i, c, d, E, R, L, k, A, I, S, y]),
              z = W.computedStyle,
              V = W.computedClassNames;
            return o().createElement(
              "div",
              Nt({ className: v()(kt.base, ...V, t), style: z }, H),
              P,
            );
          });
        let Lt;
        function Rt(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(Lt || (Lt = {}));
        const Pt = (e, t, a) => {
            if (a % 2) {
              const a = e.pop();
              return [...e, a + t];
            }
            return [...e, t];
          },
          Ht = (e, t, a) => {
            if (0 === a) return [t];
            if (a % 2) return [...e, " " === t ? " " : t];
            {
              const a = e.pop();
              return [...e, a + t];
            }
          },
          Wt = (e, t, a = Lt.left) => e.split(t).reduce(a === Lt.left ? Pt : Ht, []),
          zt = (() => {
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
          Vt = ["zh_cn", "zh_sg", "zh_tw"],
          Ut = (e, t = Lt.left) => {
            const a = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Vt.includes(a)
              ? zt(e)
              : ((e, t = Lt.left) => {
                  let a = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    u = e.replace(/&nbsp;/g, " ");
                  return (Wt(u, /( )/, t).forEach((e) => (a = a.concat(Wt(e, n, Lt.left)))), a);
                })(e, t);
          },
          Gt = "FormatText_base_d0",
          jt = ({ binding: e, text: t = "", classMix: a, alignment: n = Lt.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  r.Fragment,
                  null,
                  t.split("\n").map((t, u) =>
                    o().createElement(
                      "div",
                      { className: v()(Gt, a), key: `${t}-${u}` },
                      ((e, t, a) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (a && e in a ? a[e] : Ut(e, t))))(t, n, e).map((e, t) =>
                        o().createElement(r.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var $t = a(3532),
          Xt = a.n($t);
        const qt = {
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
          Yt = [
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
        function Kt() {
          return (
            (Kt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Kt.apply(this, arguments)
          );
        }
        Object.keys(Ft());
        const Zt = Object.keys(Xt()),
          Jt = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Qt = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          ea = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          ta = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          aa =
            (Object.keys(ta),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Jt,
              "heading-H36": Jt,
              "heading-H28": Qt,
              "heading-H24": Qt,
              "heading-H24R": Qt,
              "heading-H22": Qt,
              "heading-H20R": Qt,
              "heading-H18": Qt,
              "heading-H15": ea,
              "heading-H14": ea,
              "paragraph-P24": Qt,
              "paragraph-P18": Qt,
              "paragraph-P16": Qt,
              "paragraph-P14": ea,
              "paragraph-P12": ea,
              "paragraph-P10": ea,
            }),
          na =
            (Object.keys(aa),
            (e) =>
              e
                ? ((e) => Zt.includes(e))(e)
                  ? { colorClassName: qt[e] }
                  : { colorStyle: { color: e } }
                : {}),
          ua = yt((e) => {
            let t = e.text,
              a = e.variant,
              n = e.className,
              u = e.color,
              s = e.m,
              i = e.mt,
              l = void 0 === i ? s : i,
              c = e.mr,
              _ = void 0 === c ? s : c,
              d = e.mb,
              m = void 0 === d ? s : d,
              E = e.ml,
              g = void 0 === E ? s : E,
              p = e.style,
              b = e.format,
              A = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Yt);
            const C = (0, r.useMemo)(() => {
                const e = na(u),
                  t = e.colorClassName,
                  a = e.colorStyle,
                  n = void 0 === a ? {} : a;
                return { computedStyle: Object.assign({}, p, n), colorClassName: t };
              }, [p, u]),
              f = C.computedStyle,
              h = C.colorClassName;
            return o().createElement(
              Ot,
              Kt(
                {
                  className: v()(qt.base, a && qt[a], h, n),
                  style: f,
                  mt: !0 === l ? aa[a || "paragraph-P16"].mt : l,
                  mr: !0 === _ ? aa[a || "paragraph-P16"].mr : _,
                  mb: !0 === m ? aa[a || "paragraph-P16"].mb : m,
                  ml: !0 === g ? aa[a || "paragraph-P16"].ml : g,
                },
                A,
              ),
              void 0 !== b ? o().createElement(jt, Kt({}, b, { text: t })) : t,
            );
          }),
          ra = "NoData_base_af",
          oa = "NoData_titleWrapper_3a",
          sa = "NoData_icon_7f",
          ia = "NoData_title_12",
          la = "NoData_description_ed",
          ca = R.strings.customization.cart,
          _a = () =>
            o().createElement(
              "div",
              { className: ra },
              o().createElement(
                "div",
                { className: oa },
                o().createElement("div", { className: sa }),
                o().createElement(ua, { text: ca.emptyTitle(), className: ia }),
              ),
              o().createElement(ua, { text: ca.emptyDescription(), className: la }),
            );
        var da = a(4179);
        const ma = [
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
        function Ea(e) {
          return Object.entries(e || {}).map(([e, t]) => {
            const a = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                a.number = t;
                break;
              case "boolean":
                a.bool = t;
                break;
              case "undefined":
                break;
              default:
                a.string = t.toString();
            }
            return a;
          });
        }
        const ga = (e, t, a = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: da.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                a,
              ),
            );
          },
          pa = (e) => {
            let t = e.children,
              a = e.contentId,
              n = e.args,
              u = e.onMouseEnter,
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
              p = void 0 === g || g,
              b = e.targetId,
              A = void 0 === b ? 0 : b,
              C = e.onShow,
              f = e.onHide,
              h = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, ma);
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
                    let a,
                      n = R.invalid("resId");
                    return (
                      t &&
                        ((a = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== a &&
                          window.subViews[a] &&
                          (n = window.subViews[a].id)),
                      { caller: a, stack: t, resId: n }
                    );
                  })().resId,
                [A],
              ),
              D = (0, r.useCallback)(() => {
                (v.current.isVisible && v.current.timeoutId) ||
                  (ga(a, E, { isMouseEvent: !0, on: !0, arguments: Ea(n) }, F),
                  C && C(),
                  (v.current.isVisible = !0));
              }, [a, E, n, F, C]),
              B = (0, r.useCallback)(() => {
                if (v.current.isVisible || v.current.timeoutId) {
                  const e = v.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (v.current.timeoutId = 0)),
                    ga(a, E, { on: !1 }, F),
                    v.current.isVisible && f && f(),
                    (v.current.isVisible = !1));
                }
              }, [a, E, F, f]),
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
                !1 === p && B();
              }, [p, B]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", B),
                  () => {
                    (window.removeEventListener("mouseleave", B), B());
                  }
                ),
                [B],
              ));
            return p
              ? (0, r.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((w = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((v.current.timeoutId = window.setTimeout(D, c ? 100 : 400)),
                            u && u(e),
                            w && w(e));
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
                    h,
                  ),
                )
              : t;
            var w;
          },
          ba = ["children"];
        function Aa() {
          return (
            (Aa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Aa.apply(this, arguments)
          );
        }
        const Ca = (e) => {
            let t = e.children,
              a = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, ba);
            return o().createElement(
              pa,
              Aa(
                {
                  contentId:
                    R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                      "resId",
                    ),
                  ignoreShowDelay: !0,
                },
                a,
              ),
              t,
            );
          },
          fa = /<link.*?>/g,
          ha = /\.\.\//g,
          va = /<script.*?>/g,
          Fa = "default.css",
          Da = (e) => {
            const t = e.match(ha);
            return t && t.join("");
          },
          Ba = () => {
            for (
              var e = 0, t = Array.from(document.head.querySelectorAll('link[rel="stylesheet"]'));
              e < t.length;
              e++
            ) {
              const a = t[e];
              if (!a.href.includes(Fa)) return a.href;
            }
            return "";
          },
          Sa = (e, t) => {
            const a = Ba(),
              n = Da(a);
            let u,
              r = e;
            for (; null !== (u = va.exec(e));) {
              const e = u[0].match(/<script (defer|defer="defer") src="(.*?)">/);
              if (e) {
                const a = n + e[2].replace(ha, "");
                ((r = r.replace(e[2], a)),
                  (r = r.replace('<div id="root"', `<div data-root-id=${t} id="root"`)));
              }
            }
            return r;
          },
          wa = () => {
            const e = [];
            let t = !1;
            const a = () => {
              if (!e.length) return void (t = !1);
              const n = e.shift();
              n && ((t = !0), n().then(() => a()));
            };
            return {
              add: (n) => {
                (e.push(n), t || a());
              },
            };
          },
          ya = "SubView_base_0d",
          ka = "subViews.onChanged",
          Ta = "subView:destroy",
          Na = ".html",
          Ia = /^coui:\/\/gui\/.*/,
          Ma = wa(),
          xa = (e) => {
            const t = document.createElement("script");
            ((t.src = e), (t.defer = !0), document.head.appendChild(t));
          },
          Oa =
            ((0, r.memo)(({ id: e, mixClass: t, children: a }) => {
              const n = (0, r.useRef)(null),
                u = (0, r.useMemo)(() => window.subViews.addChildChangedCallback(e), [e]),
                s = (0, r.useState)(!1),
                i = s[0],
                l = s[1],
                c = (0, r.useState)(!0),
                _ = c[0],
                d = c[1],
                m = (0, r.useCallback)(
                  (e) => {
                    e.includes(u) &&
                      (l(!0), engine.off(ka, m), window.subViews.removeChildChangedCallback(u));
                  },
                  [u],
                ),
                E = (0, r.useCallback)((e) => {
                  Ma.add(
                    () =>
                      new Promise((t) => {
                        const a = new MutationObserver(() => {
                          (d(!1), a.disconnect(), t());
                        });
                        if (n.current) {
                          const t = document.getElementById("root");
                          (t && t.setAttribute("id", "bugSubView"),
                            n.current.setAttribute("id", "root"));
                          const u = document.createElement("link");
                          ((u.href = e.replace(Na, ".css")),
                            (u.rel = "stylesheet"),
                            document.head.appendChild(u),
                            Ia.test(e) &&
                              xa(
                                e
                                  .split("/")
                                  .slice(0, -3)
                                  .concat(["vendors.js"])
                                  .join("/")
                                  .replace("/production/", "/production/lib/"),
                              ),
                            xa(e.replace(Na, ".js")),
                            a.observe(n.current, { childList: !0 }));
                        }
                      }),
                  );
                }, []);
              return (
                (0, r.useEffect)(() => {
                  if (window.subViews.ids().includes(e)) {
                    const t = window.subViews.get(e),
                      a = t.path;
                    let n = a.split("/").pop();
                    if (n)
                      return (
                        (n = n.split(".")[0]),
                        (window.subViews[n] = Object.assign({ id: e }, t)),
                        E(a),
                        () => {
                          (n && window.subViews[n] && delete window.subViews[n],
                            engine.trigger("subView:destroy", { viewName: n, viewId: e }),
                            window.__dataTracker &&
                              window.__dataTracker.clearViewCallbacks &&
                              window.__dataTracker.clearViewCallbacks(e),
                            console.info(`Sub view ${n} is destroyed: ${a}`));
                        }
                      );
                    console.error("subView: can't get View component name");
                  } else engine.on(ka, m);
                }, [m, E, e, i]),
                o().createElement(
                  "div",
                  { className: v()(ya, t) },
                  _ && a,
                  o().createElement("div", { ref: n, "data-root-id": e }),
                )
              );
            }),
            {
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
            });
        let La, Ra;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(La || (La = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(Ra || (Ra = {})));
        const Pa = ({
          children: e,
          size: t,
          isFocused: a,
          type: n,
          disabled: u,
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
          const p = (0, r.useRef)(null),
            b = (0, r.useState)(a),
            A = b[0],
            C = b[1],
            f = (0, r.useState)(!1),
            h = f[0],
            F = f[1],
            D = (0, r.useState)(!1),
            B = D[0],
            S = D[1],
            w = (0, r.useCallback)(() => {
              u || (p.current && (p.current.focus(), C(!0)));
            }, [u]),
            y = (0, r.useCallback)(
              (e) => {
                A && null !== p.current && !p.current.contains(e.target) && C(!1);
              },
              [A],
            ),
            k = (0, r.useCallback)(
              (e) => {
                u || (g && g(e));
              },
              [u, g],
            ),
            T = (0, r.useCallback)(
              (e) => {
                u || (null !== i && j(i), c && c(e), S(!0));
              },
              [u, i, c],
            ),
            N = (0, r.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            I = (0, r.useCallback)(
              (e) => {
                u || (m && m(e), F(!1));
              },
              [u, m],
            ),
            M = (0, r.useCallback)(
              (e) => {
                u || (null !== l && j(l), d && d(e), a && w(), F(!0));
              },
              [u, l, d, w, a],
            ),
            x = (0, r.useCallback)(
              (e) => {
                u || (E && E(e), F(!1));
              },
              [u, E],
            ),
            O = v()(
              Oa.base,
              Oa[`base__${n}`],
              {
                [Oa.base__disabled]: u,
                [Oa[`base__${t}`]]: t,
                [Oa.base__focus]: A,
                [Oa.base__highlightActive]: h,
                [Oa.base__firstHover]: B,
              },
              s,
            ),
            L = v()(Oa.state, Oa.state__default);
          return (
            (0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", y),
                () => {
                  document.removeEventListener("mousedown", y);
                }
              ),
              [y],
            ),
            (0, r.useEffect)(() => {
              C(a);
            }, [a]),
            o().createElement(
              "div",
              {
                ref: p,
                className: O,
                onMouseEnter: T,
                onMouseMove: N,
                onMouseUp: I,
                onMouseDown: M,
                onMouseLeave: x,
                onClick: k,
              },
              n !== La.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: Oa.back }),
                  o().createElement("span", { className: Oa.texture }),
                ),
              o().createElement(
                "span",
                { className: L },
                o().createElement("span", { className: Oa.stateDisabled }),
                o().createElement("span", { className: Oa.stateHighlightHover }),
                o().createElement("span", { className: Oa.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: Oa.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Pa.defaultProps = {
          type: La.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Ha = (0, r.memo)(Pa),
          Wa = ["children", "body", "header", "note", "alert", "args"];
        function za() {
          return (
            (za =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            za.apply(this, arguments)
          );
        }
        const Va = R.views.common.tooltip_window.simple_tooltip_content,
          Ua = (e) => {
            let t = e.children,
              a = e.body,
              n = e.header,
              u = e.note,
              s = e.alert,
              i = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Wa);
            const c = (0, r.useMemo)(() => {
              const e = Object.assign({}, i, { body: a, header: n, note: u, alert: s });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [s, a, n, u, i]);
            return o().createElement(
              pa,
              za(
                {
                  contentId:
                    ((_ = null == i ? void 0 : i.hasHtmlContent),
                    _ ? Va.SimpleTooltipHtmlContent("resId") : Va.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var _;
          };
        let Ga, ja;
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
        })(Ga || (Ga = {})),
          (function (e) {
            ((e[(e.digital = 0)] = "digital"), (e[(e.text = 1)] = "text"));
          })(ja || (ja = {})));
        const $a = (e) => {
          const t = (0, r.useRef)();
          return (
            (0, r.useEffect)(() => {
              t.current = e;
            }, [e]),
            t.current
          );
        };
        let Xa;
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
        })(Xa || (Xa = {}));
        const qa = 60,
          Ya = 3600,
          Ka = 86400;
        Date.now();
        const Za = () => {},
          Ja = (e = 0, t, a = 0, n = Za) => {
            const u = (0, r.useState)(e),
              o = u[0],
              s = u[1];
            return (
              (0, r.useEffect)(() => {
                if (e > 0) {
                  s(e);
                  const u = Date.now(),
                    r = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - u) / 1e3);
                        null !== a && t <= a ? (s(a), n && n(), clearInterval(r)) : s(t);
                      },
                      1e3 * (t || (e > 120 ? qa : 1)),
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                s(0);
              }, [e, t, a, n]),
              o
            );
          };
        da.Sw.instance;
        let Qa;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Qa || (Qa = {}));
        da.Sw.instance;
        const en = $a,
          tn = Ja,
          an = (e) => {
            (0, r.useEffect)(e, []);
          };
        function nn() {
          const e = (0, r.useRef)(0);
          var t;
          return (
            (t = () => {
              window.clearTimeout(e.current);
            }),
            (0, r.useEffect)(() => t, []),
            (0, r.useMemo)(
              () => ({
                run: (t, a) => {
                  (window.clearTimeout(e.current),
                    (e.current = window.setTimeout(() => {
                      (t(), (e.current = 0));
                    }, a)));
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
        const un = "SubView_base_df",
          rn = "subViews.onChanged",
          on = wa(),
          sn = (0, r.memo)(({ id: e, fallback: t, onLoadCallback: a, mixClass: n }) => {
            const u = (0, r.useState)(""),
              s = u[0],
              i = u[1],
              l = (0, r.useMemo)(() => ({ __html: Sa(s, e) }), [s, e]),
              c = (0, r.useMemo)(() => window.subViews.addChildChangedCallback(e), [e]),
              _ = (0, r.useState)(!1),
              d = _[0],
              m = _[1],
              E = (0, r.useCallback)(
                (e) => {
                  e.includes(c) &&
                    (m(!0), engine.off(rn, E), window.subViews.removeChildChangedCallback(c));
                },
                [c],
              ),
              g = (0, r.useCallback)((e) => {
                on.add(
                  () =>
                    new Promise((t) => {
                      i(e);
                      const a = new MutationObserver(() => {
                          (a.disconnect(), t());
                        }),
                        n = document.getElementById("root");
                      n && a.observe(n, { childList: !0 });
                    }),
                );
              }, []);
            ((0, r.useEffect)(() => {
              if (window.subViews.ids().includes(e)) {
                const t = window.subViews.get(e),
                  a = t.path;
                let n;
                if ((n = a.split("/").pop()))
                  return (
                    (n = n.split(".")[0]),
                    (window.subViews[n] = Object.assign({ id: e }, t)),
                    engine.on(`subView:inject->${n}`, g),
                    (({ path: e, name: t }) => {
                      const a = new XMLHttpRequest();
                      ((a.onreadystatechange = () => {
                        4 === a.readyState &&
                          (200 === a.status
                            ? (0, da.Eu)().then(() => {
                                (console.info(`Sub view ${t} loaded: ${e}`),
                                  engine.TriggerEvent(`subView:inject->${t}`, a.responseText));
                              })
                            : console.error(`subView: status: ${a.status} - can't get bundle`));
                      }),
                        a.open("GET", e),
                        a.send());
                    })({ name: n, path: a }),
                    () => {
                      (n && window.subViews[n] && delete window.subViews[n],
                        engine.trigger("subView:destroy", { viewName: n, viewId: e }),
                        window.__dataTracker &&
                          window.__dataTracker.clearViewCallbacks &&
                          window.__dataTracker.clearViewCallbacks(e),
                        engine.off(`subView:inject->${n}`, g),
                        console.info(`Sub view ${n} is destroyed: ${a}`));
                    }
                  );
                console.error("subView: can't get View component name");
              } else engine.on(rn, E);
            }, [E, g, e, d]),
              (0, r.useEffect)(
                () => () => {
                  s &&
                    ((e) => {
                      const t = Da(Ba());
                      let a;
                      for (; null !== (a = fa.exec(e));) {
                        const e = a[0].match(/href="(.*?)"/);
                        if (e) {
                          const a = t + e[1].replace(ha, ""),
                            n = document.head.querySelector(`[href="${a}"]`);
                          n && document.head.removeChild(n);
                        }
                      }
                    })(s);
                },
                [s],
              ));
            const p = v()(un, n);
            if (s) {
              let t;
              return (
                (t = document.getElementById("root")) && t.setAttribute("id", "bugSubView"),
                ((e) => {
                  let t;
                  const a = Ba(),
                    n = Da(a);
                  for (; null !== (t = fa.exec(e));) {
                    const e = t[0].match(/href="(.*?)"/);
                    if (e && !e[1].includes(Fa) && n) {
                      const t = n + e[1].replace(ha, ""),
                        a = document.createElement("link");
                      ((a.href = t), (a.rel = "stylesheet"), document.head.appendChild(a));
                    }
                  }
                })(s),
                a && a(e),
                o().createElement("div", { className: p, dangerouslySetInnerHTML: l })
              );
            }
            return t
              ? o().createElement("div", { className: p }, o().createElement(t, null))
              : null;
          });
        let ln;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(ln || (ln = {}));
        const cn = {
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
        let _n, dn, mn;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(_n || (_n = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(dn || (dn = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(mn || (mn = {})));
        const En = [
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
        function gn() {
          return (
            (gn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            gn.apply(this, arguments)
          );
        }
        const pn = (e) => {
          let t = e.id,
            a = e.isChecked,
            n = void 0 !== a && a,
            u = e.isDisabled,
            s = void 0 !== u && u,
            i = e.isAlert,
            l = void 0 !== i && i,
            c = e.size,
            _ = void 0 === c ? _n.medium : c,
            d = e.type,
            m = void 0 === d ? dn.primary : d,
            E = e.soundHover,
            g = void 0 === E ? "highlight" : E,
            p = e.soundClick,
            b = void 0 === p ? "play" : p,
            A = e.onMouseEnter,
            C = e.onMouseLeave,
            f = e.onMouseUp,
            h = e.onMouseDown,
            F = e.onClick,
            D = e.onChange,
            B = e.onFocus,
            S = e.onBlur,
            w = e.text,
            y = e.contentStyles,
            k = e.children,
            T = e.alignment,
            N = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                u = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, En);
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
                const t = e.button === ln.LEFT;
                s || (t && x(!0), t && h && h(e), b && j(b));
              },
              [s, h, b],
            ),
            H = (0, r.useCallback)(
              (e) => {
                s || (x(!1), f && f(e));
              },
              [s, f],
            ),
            W = (0, r.useCallback)(
              (e) => {
                s || (A && A(e), g && j(g));
              },
              [s, A, g],
            ),
            z = (0, r.useCallback)(
              (e) => {
                s || (x(!1), C && C(e));
              },
              [s, C],
            ),
            V = (0, r.useCallback)(
              (e) => {
                s || (L(!0), B && B(e));
              },
              [s, B],
            ),
            U = (0, r.useCallback)(
              (e) => {
                s || (L(!1), S && S(e));
              },
              [s, S],
            ),
            G = o().createElement(
              "div",
              { className: cn.label },
              o().createElement(
                "div",
                { className: v()(cn.labelContent, "s-labelContent"), style: y },
                w || k,
              ),
            );
          return o().createElement(
            "div",
            gn(
              {
                id: t,
                className: v()(cn.base, cn[`base__${_}`], cn[`base__${m}`], {
                  [cn.base__checked]: n,
                  [cn.base__disabled]: s,
                  [cn.base__mouseDown]: M,
                  [cn.base__alert]: l,
                  [cn.base__center]: T === mn.Center,
                  [cn.base__bottom]: T === mn.Bottom,
                }),
                onClick: R,
                onMouseEnter: W,
                onMouseLeave: z,
                onMouseDown: P,
                onMouseUp: H,
                onFocus: V,
                onBlur: U,
              },
              N,
            ),
            o().createElement(
              "div",
              { className: cn.input },
              o().createElement("div", { className: cn.alertOverlay }),
              o().createElement("div", { className: cn.inputHoverOverlay }),
              o().createElement("div", { className: cn.highlight }),
            ),
            o().createElement("div", { className: cn.checkmark }),
            ((w || k) && G) || null,
          );
        };
        let bn, An, Cn;
        (!(function (e) {
          ((e.small = "small"),
            (e.big = "big"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(bn || (bn = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(An || (An = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(Cn || (Cn = {})));
        class fn extends o().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = da.B3.GOLD;
            else e = da.B3.INTEGRAL;
            const t = da.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        fn.defaultProps = { format: "integral" };
        const hn = {
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
          vn = ({
            isDiscount: e,
            isInteractiveDiscount: t,
            size: a,
            type: n,
            isEnough: u,
            value: r,
            discountValue: s,
            showPlus: i,
            stockBackgroundName: l = Cn.Red,
          }) => {
            const c = v()(hn.value, hn[`value__${n}`], !u && hn.value__notEnough),
              _ = v()(hn.icon, hn[`icon__${n}-${a}`]),
              d = v()(hn.stock, s && hn.stock__indent, t && hn.stock__interactive),
              m = i && r > 0 && "+",
              E = v()(hn.base, hn[`base__${a}`]);
            return o().createElement(
              "span",
              { className: E },
              o().createElement(
                "span",
                { className: c },
                m,
                o().createElement(fn, { value: r, format: n === An.gold ? "gold" : "integral" }),
              ),
              o().createElement("span", { className: _ }),
              e &&
                o().createElement(
                  "span",
                  { className: d },
                  o().createElement("span", {
                    className: hn.stockBackground,
                    style: { backgroundImage: `url(R.images.gui.maps.icons.library.${l})` },
                  }),
                  Boolean(s) && s,
                ),
            );
          };
        vn.defaultProps = { isEnough: !0 };
        const Fn = o().memo(vn),
          Dn = "Tutorial_tutorial_ce",
          Bn = "Tutorial_tutorial_border_ab",
          Sn = "Tutorial_tutorial__hidden_8a",
          wn = "Tutorial_tutorial_hint_bc",
          yn = "Tutorial_tutorial_hintSubstrate_c7",
          kn = "Tutorial_tutorial_hintArrow_75",
          Tn = "Tutorial_tutorial_hintText_b5";
        class Nn extends o().PureComponent {
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
            const e = v()(Dn, { [Sn]: this.props.isHidden });
            return o().createElement(
              "div",
              { className: e, onClick: this.onClick },
              o().createElement("div", { className: Bn }),
              o().createElement(
                "div",
                { className: wn },
                o().createElement("div", { className: yn }),
                o().createElement("div", { className: kn }),
                o().createElement("div", { className: Tn }, this.props.text),
              ),
            );
          }
        }
        const In = "HangarCounter_base_43",
          Mn = "HangarCounter_currencyWrapper_cb",
          xn = "HangarCounter_hangarIcon_46",
          On = (0, r.memo)(({ count: e }) => {
            const t = y().mediaSize <= B.Small ? bn.small : bn.big;
            return o().createElement(
              "div",
              { className: In },
              o().createElement(
                "div",
                { className: Mn },
                o().createElement(Fn, { value: e, size: t, type: "equipCoin" }),
              ),
              o().createElement("div", { className: xn }),
            );
          }),
          Ln = "CartPanel_base_e7",
          Rn = "CartPanel_base__onlyRightSide_f7",
          Pn = "CartPanel_leftSide_d1",
          Hn = "CartPanel_checkboxContainer_32",
          Wn = "CartPanel_rightSide_12",
          zn = "CartPanel_setupButton_b9",
          Vn = "CartPanel_deleteButton_b0",
          Un = "CartPanel_deleteButtonIcon_77",
          Gn = "CartPanel_backButton_ee",
          jn = "CartPanel_backButtonIcon_f2",
          $n = "CartPanel_amountWrapper_f1",
          Xn = "CartPanel_amountGold_c6",
          qn = "CartPanel_amountRent_c7",
          Yn = "CartPanel_amountCredits_7b",
          Kn = "CartPanel_amountEquipment_5b",
          Zn = "CartPanel_rentCount_11",
          Jn = R.strings.customization,
          Qn = R.strings.vehicle_customization.customization,
          eu = R.strings.customization.tooltips.cart,
          tu = (0, r.memo)(
            ({
              price: e,
              onResetHandler: t,
              onBackHandler: a,
              onApplyHandler: n,
              onAutoRentChange: u,
              onAutoRentHintClose: s,
              cartParams: i,
              buttonSize: l,
              className: c,
            }) => {
              const _ = (0, r.useState)(!1),
                d = _[0],
                m = _[1],
                E = y().mediaSize <= B.Small ? bn.small : bn.big,
                g = ((e) =>
                  Array.from(e.values()).reduce((e, t) => {
                    if ("object" == typeof t && null !== t) {
                      const a = t.name,
                        n = t.value;
                      e[a] = (e[a] || 0) + n;
                    }
                    return e;
                  }, {}))(e),
                p = [
                  i.isEnoughMoney ? "" : eu.BuyButtonDisabledNotEnoughMoney(),
                  i.isVehicleCustomized || i.buyButtonEnabled ? "" : eu.buyButtonDisabledDefault(),
                  i.isLockedItem ? Qn.lockedItemsApply() : "",
                ].filter((e) => e.length > 0)[0],
                b = i.isRentable && u,
                A = (0, r.useCallback)(() => {
                  (i.showAutoRentHint && (m(!0), s && s()), u && u());
                }, [i.showAutoRentHint, u, s]);
              return o().createElement(
                "div",
                { className: v()(Ln, c, !b && Rn) },
                b &&
                  o().createElement(
                    "div",
                    { className: Pn },
                    i.showAutoRentHint &&
                      o().createElement(Nn, {
                        text: R.strings.tutorial.customization.autoprolongation(),
                        isHidden: d,
                      }),
                    o().createElement(
                      "div",
                      { className: Hn },
                      o().createElement(pn, {
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
                  { className: Wn },
                  o().createElement(
                    "div",
                    { className: $n },
                    i.inStorageCount > 0 &&
                      o().createElement(
                        "div",
                        { className: Kn },
                        o().createElement(On, { count: i.inStorageCount }),
                      ),
                    i.isRentable &&
                      ((null == g ? void 0 : g.gold) || (null == g ? void 0 : g.credits)) &&
                      !i.inStorageCount &&
                      o().createElement(
                        "div",
                        { className: qn },
                        o().createElement(
                          "div",
                          { className: Zn },
                          o().createElement(ua, {
                            text: `${i.rentCount} ${Jn.cartPanel.rentAmountLabel()}`,
                          }),
                        ),
                      ),
                    i.isGoldPrice
                      ? (null == g ? void 0 : g.gold) &&
                          o().createElement(
                            "div",
                            { className: Xn },
                            o().createElement(Fn, {
                              value: null == g ? void 0 : g.gold,
                              size: E,
                              type: An.gold,
                              isEnough: i.isEnoughMoney,
                            }),
                          )
                      : (null == g ? void 0 : g.credits) &&
                          o().createElement(
                            "div",
                            { className: Yn },
                            o().createElement(Fn, {
                              value: null == g ? void 0 : g.credits,
                              size: E,
                              type: An.credits,
                              isEnough: i.isEnoughMoney,
                            }),
                          ),
                  ),
                  (i.clearButtonEnabled || i.cancelButtonEnabled) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      o().createElement(
                        Ua,
                        {
                          body: i.cancelButtonEnabled
                            ? eu.cancelButtonEnabled()
                            : eu.cancelButtonDisabled(),
                        },
                        o().createElement(
                          "div",
                          null,
                          o().createElement(
                            Ha,
                            {
                              type: La.ghost,
                              size: l,
                              mixClass: Gn,
                              onClick: a,
                              disabled: !i.cancelButtonEnabled,
                            },
                            o().createElement("div", { className: jn }),
                          ),
                        ),
                      ),
                      o().createElement(
                        Ua,
                        {
                          body: i.clearButtonEnabled
                            ? eu.clearButtonEnabled()
                            : eu.clearButtonDisabled(),
                        },
                        o().createElement(
                          "div",
                          null,
                          o().createElement(
                            Ha,
                            {
                              type: La.ghost,
                              size: l,
                              mixClass: Vn,
                              onClick: t,
                              soundClick: "cust_select_remove",
                              disabled: !i.clearButtonEnabled,
                            },
                            o().createElement("div", { className: Un }),
                          ),
                        ),
                      ),
                    ),
                  o().createElement(
                    Ua,
                    {
                      body: p || "",
                      isEnabled: i.isEnoughMoney
                        ? !i.isApplyButton && (null == p ? void 0 : p.length) > 0
                        : !i.buyButtonEnabled && (null == p ? void 0 : p.length) > 0,
                    },
                    o().createElement(
                      "div",
                      null,
                      o().createElement(
                        Ha,
                        {
                          type: La.main,
                          size: l,
                          mixClass: zn,
                          disabled: !i.buyButtonEnabled,
                          onClick: n,
                        },
                        o().createElement(ua, {
                          text: i.isApplyButton
                            ? Jn.cartPanel.applyButton()
                            : Jn.cartPanel.setupButton(),
                        }),
                      ),
                    ),
                  ),
                ),
              );
            },
          ),
          au = {
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
          nu = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function uu() {
          return (
            (uu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            uu.apply(this, arguments)
          );
        }
        const ru = (e) => {
          let t = e.size,
            a = e.value,
            n = e.isEmpty,
            u = e.fadeInAnimation,
            r = e.hide,
            s = e.maximumNumber,
            i = e.className,
            l = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                u = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, nu);
          const c = n ? null : a,
            _ = "string" == typeof c;
          if ((c && !_ && c < 0) || 0 === c) return null;
          const d = c && !_ && c > s,
            m = v()(
              au.base,
              au[`base__${t}`],
              u && au.base__animated,
              r && au.base__hidden,
              !c && au.base__pattern,
              n && au.base__empty,
              i,
            );
          return o().createElement(
            "div",
            uu({ className: m }, l),
            o().createElement("div", { className: au.bg }),
            o().createElement("div", { className: au.pattern }),
            o().createElement(
              "div",
              { className: v()(au.value, _ && au.value__text) },
              d ? s : c,
              d && o().createElement("span", { className: au.plus }, "+"),
            ),
          );
        };
        ru.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const ou = {
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
        var su;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(su || (su = {}));
        const iu = ["__left", "__right", "__top", "__bottom"],
          lu =
            ((0, r.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: t, onOutsideClick: a, customStyles: n = {} },
                u,
              ) => {
                const s = (0, r.useRef)(null),
                  l = (0, r.useRef)(null),
                  c = (0, r.useRef)(null),
                  _ = (0, r.useState)(window.decorator && window.decorator.directionType),
                  d = _[0],
                  m = _[1],
                  E = (0, r.useCallback)(() => {
                    ($.playClick(), i.O.view.sendEvent.close());
                  }, []),
                  g = (0, r.useCallback)(() => {
                    $.playHighlight();
                  }, []),
                  p = v()(ou.arrow, ou[`arrow${iu[d]}`]);
                an(
                  () => (
                    i.O.client.events.mouse.enableOutside(),
                    i.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (a ? a() : i.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const b = (0, r.useCallback)(
                    (e) => {
                      let t = e.target;
                      do {
                        if (t === s.current || t === c.current) return;
                        t = t.parentNode;
                      } while (t);
                      const n = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = i.O.client.getMouseGlobalPosition(),
                          t = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                          a =
                            e.x < n.boundX ||
                            e.x > n.boundX + n.boundWidth ||
                            e.y > n.boundY + n.boundHeight ||
                            e.y < n.boundY;
                        if (t && !a) return;
                      }
                      a ? a() : i.O.view.sendEvent.close("popover");
                    },
                    [s, c, a],
                  ),
                  A = (0, r.useCallback)(
                    () => (
                      i.O.view.freezeTextureBeforeResize(),
                      W(() => {
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
                  (0, r.useImperativeHandle)(u, () => ({ updateSize: A })),
                  an(() => {
                    i.O.view.setInputPaddingsRem(58);
                  }),
                  (0, r.useEffect)(() => {
                    document.addEventListener("mousedown", b, { capture: !0 });
                    const e = ((e) => {
                      let t = !1;
                      return {
                        promise: new Promise((a, n) => {
                          e.then((e) => !t && a(e)).catch((e) => !t && n(e));
                        }),
                        cancel() {
                          t = !0;
                        },
                      };
                    })((0, da.Eu)());
                    return (
                      !t && e.promise.then(() => A()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", b));
                      }
                    );
                  }, [A, b, t]),
                  o().createElement(
                    "div",
                    { className: ou.base, ref: l },
                    o().createElement(
                      "div",
                      { className: ou.decorator },
                      o().createElement(
                        "div",
                        { className: ou.content, ref: s },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          o().createElement(
                            Ua,
                            { body: R.strings.dialogs.common.error.cancel() },
                            o().createElement("div", {
                              className: ou.closeBtn,
                              onClick: E,
                              onMouseEnter: g,
                              ref: c,
                            }),
                          ),
                      ),
                      o().createElement("div", { className: p, style: n.arrow }),
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
        function cu() {
          return (
            (cu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            cu.apply(this, arguments)
          );
        }
        const _u = (e) => {
          let t = e.contentId,
            a = e.decoratorId,
            n = e.direction,
            u = void 0 === n ? su.Top : n,
            s = e.targetId,
            i = e.args,
            l = e.onClick,
            c = e.children,
            _ = e.isEnabled,
            d = void 0 === _ || _,
            m = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                u = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, lu);
          const E = (0, r.useRef)(null),
            g = (0, r.useCallback)(() => {
              if ((0, da.wU)()) return (0, da.SW)();
              E.current && (0, da.P3)(t, u, E.current, a, s, i);
            }, [t, u, i, a, s]);
          return o().createElement(
            "div",
            cu(
              {
                ref: E,
                onClick:
                  ((p = c.props.onClick),
                  (e) => {
                    d && (g(), l && l(e), p && p(e));
                  }),
              },
              m,
            ),
            c,
          );
          var p;
        };
        let du, mu;
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
        })(du || (du = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"));
          })(mu || (mu = {})));
        const Eu = {
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
          gu = [
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
        function pu() {
          return (
            (pu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            pu.apply(this, arguments)
          );
        }
        const bu = (0, r.memo)((e) => {
            let t = e.children,
              a = e.labelRenderer,
              n = e.value,
              u = e.currentValue,
              s = e.autofocus,
              i = void 0 !== s && s,
              l = e.disabled,
              c = void 0 !== l && l,
              _ = e.size,
              d = void 0 === _ ? mu.Medium : _,
              m = e.label,
              E = e.soundHover,
              g = void 0 === E ? "highlight" : E,
              p = e.soundClick,
              b = void 0 === p ? "play" : p,
              A = e.onMouseEnter,
              C = e.onMouseLeave,
              f = e.onMouseUp,
              h = e.onMouseDown,
              F = e.onClick,
              D = e.onChange,
              B = e.onFocus,
              S = e.onBlur,
              w = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, gu);
            const y = n === u,
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
            const V = (0, r.useCallback)(
                (e) => {
                  c || (D && D(n), F && F(n, e));
                },
                [c, D, F, n],
              ),
              U = (0, r.useCallback)(
                (e) => {
                  if (!c) {
                    const t = e.button === ln.LEFT;
                    (t && N(!0), t && h && h(n, e), b && j(b), i && H());
                  }
                },
                [i, c, h, H, b, n],
              ),
              G = (0, r.useCallback)(
                (e) => {
                  c || (N(!1), f && f(n, e));
                },
                [c, f, n],
              ),
              $ = (0, r.useCallback)(
                (e) => {
                  c || (A && A(n, e), g && j(g), x(!0));
                },
                [c, A, g, n],
              ),
              X = (0, r.useCallback)(
                (e) => {
                  c || (N(!1), x(!1), C && C(n, e));
                },
                [c, C, n],
              ),
              q = (0, r.useCallback)(
                (e) => {
                  c || (R(!0), B && B(n, e));
                },
                [c, B, n],
              ),
              Y = (0, r.useCallback)(
                (e) => {
                  c || (R(!1), S && S(n, e));
                },
                [c, S, n],
              ),
              K = v()(Eu.base, Eu[`base__${d}`], {
                [Eu.base__blank]: !y && !M,
                [Eu.base__blankHover]: !y && M && !T,
                [Eu.base__blankMousedown]: !y && M && T,
                [Eu.base__check]: y && !M,
                [Eu.base__checkHover]: y && M && !T,
                [Eu.base__checkMousedown]: y && M && T,
                [Eu.base__focused]: L,
                [Eu.base__disabled]: c,
              }),
              Z = (0, r.useMemo)(
                () => ({ isHovered: M, isMouseDown: T, isFocused: L, isChecked: y }),
                [M, T, L, y],
              ),
              J = (0, r.useRef)(Eu.blank),
              Q = (0, r.useRef)(Eu.blankHover),
              ee = (0, r.useRef)(Eu.blankMousedown),
              te = (0, r.useRef)(Eu.check),
              ae = (0, r.useRef)(Eu.checkHover),
              ne = (0, r.useRef)(Eu.checkMousedown);
            return (
              (0, r.useEffect)(
                W(() => {
                  ((J.current = v()(Eu.blank, Eu.transition)),
                    (Q.current = v()(Eu.blankHover, Eu.transition)),
                    (ee.current = v()(Eu.blankMousedown, Eu.transition)),
                    (te.current = v()(Eu.check, Eu.transition)),
                    (ae.current = v()(Eu.checkHover, Eu.transition)),
                    (ne.current = v()(Eu.checkMousedown, Eu.transition)));
                }),
                [],
              ),
              o().createElement(
                "div",
                pu(
                  {
                    ref: P,
                    className: K,
                    onClick: V,
                    onMouseEnter: $,
                    onMouseLeave: X,
                    onMouseDown: U,
                    onMouseUp: G,
                    onFocus: q,
                    onBlur: Y,
                  },
                  w,
                ),
                o().createElement(
                  "div",
                  { className: Eu.input },
                  o().createElement("div", { className: J.current }),
                  o().createElement("div", { className: Q.current }),
                  o().createElement("div", { className: ee.current }),
                  o().createElement("div", { className: te.current }),
                  o().createElement("div", { className: ae.current }),
                  o().createElement("div", { className: ne.current }),
                ),
                o().createElement("div", { className: Eu.label }, m || t || (a && a(Z))),
              )
            );
          }),
          Au = "RadioGroup_base_6e",
          Cu = "RadioGroup_radio_3b",
          fu = "RadioGroup_label_86",
          hu = (0, r.memo)(({ data: e, selectedValue: t, onClickHandler: a }) => {
            const n = (0, r.useState)(t),
              u = n[0],
              s = n[1],
              i = (0, r.useCallback)(
                (t) => {
                  t && (s(t), void 0 !== a && a(e[0].name, t));
                },
                [e, a],
              );
            return (
              (0, r.useEffect)(() => {
                s(t);
              }, [t]),
              o().createElement(
                "div",
                { className: Au },
                null == e
                  ? void 0
                  : e.map((e) =>
                      o().createElement(
                        "div",
                        { className: Cu, key: e.id },
                        o().createElement(
                          Ua,
                          { header: e.tooltipHeader, body: e.tooltipBody },
                          o().createElement(
                            bu,
                            { value: e.value, currentValue: u, onClick: () => i(e.value) },
                            o().createElement(ua, { className: fu, text: e.label }),
                          ),
                        ),
                      ),
                    ),
              )
            );
          });
        function vu() {
          return (
            (vu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            vu.apply(this, arguments)
          );
        }
        const Fu = ({ children: e, tooltipArgs: t, className: a }) => {
            if (!t) return e;
            const n = o().createElement("div", { className: a }, e);
            if (t.header || t.body) return o().createElement(Ua, t, n);
            const u = t.contentId,
              r = t.args,
              s = null == r ? void 0 : r.contentId;
            return u || s
              ? o().createElement(pa, vu({}, t, { contentId: u || s }), n)
              : o().createElement(Ca, t, n);
          },
          Du = "ToggleButton_base_19",
          Bu = "ToggleButton_overlay_6b",
          Su = "ToggleButton_base__active_6c",
          wu = "ToggleButton_button_1c",
          yu = "ToggleButton_indicator_9b",
          ku = "ToggleButton_counter_63",
          Tu = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function Nu() {
          return (
            (Nu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Nu.apply(this, arguments)
          );
        }
        const Iu = o().memo(function (e) {
            let t = e.isActive,
              a = e.counter,
              n = e.className,
              u = e.children,
              r = e.type,
              s = void 0 === r ? La.secondary : r,
              i = e.size,
              l = void 0 === i ? Ra.small : i,
              c = e.hasIndicator,
              _ = void 0 === c || c,
              d = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Tu);
            return o().createElement(
              "div",
              { className: v()(Du, n, t && Su) },
              o().createElement(Ha, Nu({ type: s, size: l, mixClass: wu }, d), u),
              o().createElement("div", { className: Bu }),
              _ && o().createElement("div", { className: yu }),
              Boolean(a) &&
                o().createElement(
                  "div",
                  { className: ku },
                  o().createElement(ru, { value: a, size: "small" }),
                ),
            );
          }),
          Mu = "FilterTitle_base_53",
          xu = "FilterTitle_label_14",
          Ou = "FilterTitle_discount_49",
          Lu = "FilterTitle_discountIcon_d4",
          Ru = ({ label: e, hasDiscount: t, className: a }) =>
            o().createElement(
              "div",
              { className: v()(Mu, a) },
              o().createElement("div", { className: xu }, e),
              t &&
                o().createElement(
                  "div",
                  { className: Ou },
                  o().createElement("div", { className: Lu }),
                ),
            ),
          Pu = "ToggleIcon_base_31",
          Hu = "ToggleIcon_base__small_0e",
          Wu = "ToggleIcon_icon_9e",
          zu = o().memo(function ({ icon: e, iconParams: t, isSmall: a = !1, classNames: n }) {
            return o().createElement(
              "div",
              { className: v()(Pu, null == n ? void 0 : n.base, a && Hu) },
              o().createElement("div", {
                className: v()(Wu, null == n ? void 0 : n.icon),
                style: {
                  backgroundImage: `url(${e})`,
                  width: (null == t ? void 0 : t.iconWidth) || "inherit",
                  height: (null == t ? void 0 : t.iconHeight) || "inherit",
                },
              }),
            );
          }),
          Vu = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          Uu = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Gu = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          ju = (e) =>
            Gu
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let a = Uu.length - 1; a >= 0; a--)
                    for (; e >= Uu[a];) ((t += Vu[a]), (e -= Uu[a]));
                  return t;
                })(e),
          $u = "VehicleTier_base_99",
          Xu = "VehicleTier_base__small_67",
          qu = ({ level: e, isSmall: t = !1 }) =>
            o().createElement("div", { className: v()($u, t && Xu) }, ju(e)),
          Yu = {
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
          Ku = ({
            id: e,
            icon: t,
            iconParams: a,
            type: n,
            isSmall: u = !0,
            isSelected: r = !1,
            baseClassName: s = "",
            iconClassName: i = "",
          }) => {
            return n === du.VehicleTier
              ? o().createElement(qu, { isSmall: u, level: Number(e) })
              : o().createElement(zu, {
                  icon: t,
                  isSmall: u,
                  iconParams: a,
                  classNames: {
                    icon: v()(
                      Yu[`icon__${n}`],
                      Yu[`icon__${n}${((l = e), l[0].toUpperCase() + l.slice(1))}`],
                      r && Yu.icon__selected,
                      i,
                    ),
                    base: s,
                  },
                });
            var l;
          },
          Zu = {
            base: "FilterToggleGroup_base_bd",
            title: "FilterToggleGroup_title_5c",
            content: "FilterToggleGroup_content_1b",
            toggle: "FilterToggleGroup_toggle_c2",
            base__inPopup: "FilterToggleGroup_base__inPopup_51",
          },
          Ju = ["id", "isSelected", "tooltip", "icon", "counter"];
        function Qu() {
          return (
            (Qu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Qu.apply(this, arguments)
          );
        }
        let er;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(er || (er = {}));
        const tr = ({ header: e, body: t, contentId: a, targetId: n }) =>
            a
              ? { contentId: a, targetId: n }
              : t || e
                ? { header: null != e ? e : void 0, body: null != t ? t : void 0 }
                : void 0,
          ar = ({
            id: e,
            type: t,
            label: a,
            hasDiscount: n,
            filters: u,
            onClick: r,
            className: s,
            toggleProps: i,
            theme: l = er.Default,
          }) => {
            const c = l === er.InPopup;
            return o().createElement(
              "div",
              { className: v()(Zu.base, Zu[`base__${l}`], s) },
              c && o().createElement(Ru, { className: Zu.title, label: a, hasDiscount: n }),
              o().createElement(
                "div",
                { className: Zu.content },
                Qe(u, (a) => {
                  let n = a.id,
                    u = a.isSelected,
                    s = a.tooltip,
                    l = a.icon,
                    _ = a.counter;
                  const d = (function (e, t) {
                      if (null == e) return {};
                      var a,
                        n,
                        u = {},
                        r = Object.keys(e);
                      for (n = 0; n < r.length; n++)
                        ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                      return u;
                    })(a, Ju),
                    m = d.iconWidth,
                    E = d.iconHeight;
                  return o().createElement(
                    Fu,
                    { key: n, tooltipArgs: tr(s), className: Zu.toggle },
                    o().createElement(
                      Iu,
                      Qu({}, i, {
                        className: v()(Zu.toggle, null == i ? void 0 : i.className),
                        isActive: u,
                        onClick: () => (null == r ? void 0 : r(e, n)),
                        counter: _,
                      }),
                      o().createElement(Ku, {
                        id: n,
                        icon: l,
                        iconParams: { iconWidth: m, iconHeight: E },
                        type: t,
                        isSmall: c,
                        isSelected: u,
                        baseClassName: null == i ? void 0 : i.baseClassName,
                        iconClassName: v()(
                          null == i ? void 0 : i.iconClassName,
                          (null == i ? void 0 : i.parentStyles) &&
                            (null == i ? void 0 : i.parentStyles[`icon_${n}`]),
                        ),
                      }),
                    ),
                  );
                }),
              ),
            );
          },
          nr = () => {
            const e = (0, r.useState)(i.O.view.getScale()),
              t = e[0],
              a = e[1];
            return (
              (0, r.useEffect)(() => {
                const e = () => {
                  a(i.O.view.getScale());
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
          ur = {
            base: "NumberRange_base_65",
            base__animation: "NumberRange_base__animation_70",
            blinkAnim: "NumberRange_blinkAnim_5f",
            from: "NumberRange_from_45",
            from__red: "NumberRange_from__red_53",
            separatorWrapper: "NumberRange_separatorWrapper_5a",
            separator: "NumberRange_separator_61",
            counterGlow: "NumberRange_counterGlow_f6",
          },
          rr = R.strings.crew.barracks.berthsAmountDivider(),
          or = R.strings.crew.filterPanel.counter.selectLimit,
          sr = (0, r.memo)(function ({
            isFilterRange: e,
            from: t,
            to: a,
            className: n,
            isSelectMode: u = !1,
            isSelectedLimitReached: r = !1,
            isHideTotalCounter: s = !1,
            counterGlowShift: i,
            classNames: l,
            isAnimationEnabled: c = !1,
          }) {
            const _ = i
              ? o().createElement(
                  "div",
                  { className: ur.separatorWrapper },
                  o().createElement(ua, { className: ur.separator, text: rr }),
                  o().createElement("div", {
                    style: i,
                    className: v()(
                      ur.counterGlow,
                      r && ur.blink,
                      null == l ? void 0 : l.counterGlow,
                    ),
                  }),
                )
              : o().createElement(ua, { className: ur.separator, text: rr });
            return u
              ? o().createElement(
                  Ua,
                  { header: or.header(), body: or.body(), ignoreShowDelay: !0 },
                  o().createElement(
                    "div",
                    { className: v()(ur.base, n) },
                    o().createElement(ua, { className: ur.from, text: String(t) }),
                    (t !== a || r) &&
                      o().createElement(
                        o().Fragment,
                        null,
                        _,
                        o().createElement(ua, { text: String(a) }),
                      ),
                  ),
                )
              : o().createElement(
                  "div",
                  {
                    className: v()(
                      ur.base,
                      e ? 0 === t && ur.base__animation : t > a && ur.base__animation,
                      c && ur.base__animation,
                      n,
                    ),
                  },
                  o().createElement(ua, {
                    className: v()(
                      ur.from,
                      e ? 0 === t && a > 0 && ur.from__red : t > a && ur.from__red,
                    ),
                    text: String(t),
                  }),
                  (!s || t !== a) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      _,
                      o().createElement(ua, { text: String(a) }),
                    ),
                );
          }),
          ir = "NumberRangeWithLabel_base_fd",
          lr = "NumberRangeWithLabel_counterGlow_fa",
          cr = "NumberRangeWithLabel_blink_15",
          _r = (0, r.memo)(
            ({
              title: e,
              label: t = "",
              isGlowVisible: a = !1,
              isSelectedLimitReached: n = !1,
              isFilterRange: u = !1,
              isSelectMode: r = !1,
              className: s,
              classNames: i,
              from: l,
              to: c,
              staticCounterGlowShift: _,
              isHideTotalCounter: d = !1,
              isAnimationEnabled: m = !1,
            }) => {
              const E = nr(),
                g =
                  l !== c || n
                    ? 7 * String(l).length * E + 4 * E
                    : Math.round((7 * String(l).length * E) / 2),
                p = { left: _ || g };
              return o().createElement(
                "div",
                { className: v()(ir, s) },
                t,
                o().createElement(sr, {
                  isFilterRange: u,
                  isSelectedLimitReached: n,
                  isSelectMode: r,
                  from: l,
                  to: c,
                  isHideTotalCounter: d,
                  classNames: i,
                  isAnimationEnabled: m,
                }),
                a &&
                  u &&
                  o().createElement("div", {
                    style: p,
                    className: v()(lr, n && cr, null == i ? void 0 : i.counterGlow),
                  }),
                e,
              );
            },
          ),
          dr = Ze()(
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
                a = (0, nt.Om)(
                  () =>
                    at(t.carouselItemsList.get()).slice(0, t.carouselModel.get().totalItemsCount),
                  { equals: $e },
                ),
                n = (0, nt.Om)(() => et(a(), (e) => e.isSelected), { equals: $e }),
                u = (0, nt.Om)(
                  () => {
                    var e;
                    return null == (e = n()) ? void 0 : e.intCD;
                  },
                  { equals: $e },
                ),
                r = (0, nt.Om)(() => at(t.arrowsList.get()), { equals: $e }),
                o = (0, nt.Om)(() => at(t.bookmarksList.get()), { equals: $e }),
                s = (0, nt.Om)(() => at(t.tabsItemsList.get()), { equals: $e }),
                i = (0, nt.Om)(() => et(s(), (e) => e.isSelected), { equals: $e }),
                l = (0, nt.Om)(
                  () => {
                    var e;
                    return null == (e = i()) ? void 0 : e.itemType;
                  },
                  { equals: $e },
                ),
                c = (0, nt.Om)(() => at(t.seasonsTabsItems.get()), { equals: $e }),
                _ = (0, nt.Om)(() => at(t.markers.get()), { equals: $e }),
                d = (0, nt.Om)(() => at(t.editModeData.get()), { equals: $e }),
                m = (0, nt.Om)(() => at(t.toolbarModel.get()), { equals: $e }),
                E = (0, nt.Om)(() => at(t.billModel.get()), { equals: $e }),
                g = (0, nt.Om)(() => at(t.buyPrice.get()), { equals: $e }),
                p = (0, nt.Om)(() => at(t.stageSwitcherWidgetModel.get()), { equals: $e }),
                b = (0, nt.Om)(() => at(t.toolbarButtonList.get()), { equals: $e }),
                A = (0, nt.Om)(() => at(t.filterModelStructure.get()), { equals: $e });
              return Object.assign({}, t, {
                computes: {
                  getItems: a,
                  getSelectedItem: n,
                  getSelectedItemId: u,
                  getCategories: o,
                  getTabsItemsList: s,
                  getSelectedTab: i,
                  getSelectedTabItemType: l,
                  getSeasonsTabsItemsList: c,
                  getMarkersList: _,
                  getEditData: d,
                  getBillModel: E,
                  getBuyPrice: g,
                  getToolbarButtonsList: b,
                  getArrowsList: r,
                  getStageSwitcher: p,
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
                (e) => ({ isOver: !(0, da.wU)() && e }),
                "onSceneOverChange",
              ),
              onSceneDraggingChange: e.createCallback(
                (e) => ({ isDragging: e }),
                "onSceneDraggingChange",
              ),
              onSceneClick: e.createCallbackNoArgs("onSceneClick"),
              selectSeason: e.createCallback((e) => ({ seasonName: e }), "onSelectSeason"),
              selectAnchor: e.createCallback(
                (e, t, a) => ({ areaId: e, slotType: t, regionIdx: a }),
                "markersModel.onSelectAnchor",
              ),
              hoverAnchor: e.createCallback(
                (e, t, a, n) => ({ areaId: e, slotType: t, regionIdx: a, hover: n }),
                "markersModel.onHoverAnchor",
              ),
              dragAnchor: e.createCallback(
                (e, t, a) => ({ areaId: e, slotType: t, regionIdx: a }),
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
          mr = (dr[0], dr[1]),
          Er = {
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
          gr = R.strings.customization.tooltips.filters,
          pr = R.strings.customization.filters,
          br = R.strings.customization,
          Ar = "all",
          Cr = "sale",
          fr = "inventory",
          hr = [
            {
              label: pr.labelAll(),
              id: Ar,
              value: Ar,
              name: "availability",
              tooltipHeader: gr.allRadioHeader(),
              tooltipBody: gr.allRadioBody(),
            },
            {
              label: pr.labelStock(),
              id: fr,
              value: fr,
              tooltipHeader: gr.stockRadioHeader(),
              tooltipBody: gr.stockRadioBody(),
            },
            {
              label: pr.labelSale(),
              id: Cr,
              value: Cr,
              tooltipHeader: gr.saleRadioHeader(),
              tooltipBody: gr.saleRadioBody(),
            },
          ],
          vr = (0, Le.Pi)(({ isReverse: e = !1, buttonSize: t }) => {
            const a = mr(),
              n = a.controls,
              u = a.model,
              s = y().mediaSize,
              i = u.filterModel.get(),
              l = i.availability,
              c = i.filteredItemsCounter,
              _ = i.allItemsCounter,
              d = i.newHiddenItemsCounter,
              m = i.isFilteringActive,
              E = i.favorite,
              g = u.computes.getStructureList,
              p = (0, r.useMemo)(
                () => [
                  {
                    id: "fav1",
                    icon: "R.images.gui.maps.icons.customization.icon_favorites",
                    isSelected: E,
                    counter: 0,
                    tooltip: {
                      header: gr.favoritesToggleHeader(),
                      body: gr.favoritesToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
                [E],
              ),
              b = (0, r.useCallback)(() => {
                n.changeFilter("favorite", !E);
              }, [n, E]),
              A = e ? su.Top : su.Bottom;
            return o().createElement(
              "div",
              { className: v()(Er.base, e && Er.reverse) },
              o().createElement(
                "div",
                { className: Er.counterWrapper },
                o().createElement(
                  _u,
                  {
                    contentId:
                      R.views.lobby.customization.popovers.CustomizationFilterPopoverView("resId"),
                    direction: g().length > 5 && s <= B.Small ? su.Left : A,
                  },
                  o().createElement(
                    "div",
                    null,
                    o().createElement(
                      Ua,
                      { header: gr.popoverButtonTitle(), body: gr.popoverButtonBody() },
                      o().createElement(
                        Ha,
                        {
                          type: La.ghost,
                          size: t,
                          mixClass: v()(Er.filtersPopover, e && Er.filtersPopoverUpdate),
                        },
                        o().createElement("div", { className: Er.filtersPopoverIcon }),
                      ),
                    ),
                    d > 0 &&
                      o().createElement(ru, {
                        size: "normal",
                        value: d,
                        className: Er.hiddenItemCounter,
                      }),
                  ),
                ),
                m &&
                  !e &&
                  o().createElement(_r, {
                    title:
                      m &&
                      o().createElement(
                        Ua,
                        { body: br.customization.resetFilter.tooltip.text() },
                        o().createElement(
                          Ha,
                          {
                            type: La.ghost,
                            onClick: n.clearFilter,
                            mixClass: v()(Er.filtersClearButton),
                          },
                          o().createElement("div", { className: Er.filtersClearIcon }),
                        ),
                      ),
                    from: c,
                    to: _,
                    isFilterRange: !0,
                    isGlowVisible: !0,
                    isSelectMode: !1,
                    isSelectedLimitReached: d > 0,
                    className: Er.filterNumbers,
                    staticCounterGlowShift: -1,
                    isAnimationEnabled: d > 0,
                  }),
              ),
              o().createElement(ar, {
                id: "favorites",
                label: "",
                type: du.Default,
                hasDiscount: !1,
                filters: p,
                toggleProps: { type: La.ghost },
                onClick: b,
                className: v()(Er.buttonFavorites, e && Er.buttonFavoritesBorder),
              }),
              o().createElement(hu, { onClickHandler: n.changeFilter, data: hr, selectedValue: l }),
            );
          }),
          Fr = (e, t) => {
            let a;
            const n = setTimeout(() => {
              a = e();
            }, t);
            return () => {
              ("function" == typeof a && a(), clearTimeout(n));
            };
          },
          Dr = (e, t, a) => Math.min(Math.max(e, t), a),
          Br = {
            base: "Switcher_base_9c",
            base__hasCurrentText: "Switcher_base__hasCurrentText_57",
            base__small: "Switcher_base__small_96",
            base__isVisible: "Switcher_base__isVisible_02",
          },
          Sr = (e) => ({ transitionDelay: e / 20 + "s" }),
          wr = "SwitcherBullet_base_94",
          yr = "SwitcherBullet_container_28",
          kr = "SwitcherBullet_base__selected_6e",
          Tr = "SwitcherBullet_container__text_ff",
          Nr = "SwitcherBullet_finishedHover_42",
          Ir = "SwitcherBullet_base__finished_e2",
          Mr = "SwitcherBullet_base__hover_87",
          xr = "SwitcherBullet_iconSmall_d4",
          Or = "SwitcherBullet_base__afterCurrent_f6",
          Lr = "SwitcherBullet_iconBig_65",
          Rr = "SwitcherBullet_base__currentSelected_eb",
          Pr = "SwitcherBullet_iconText_ca",
          Hr = "SwitcherBullet_iconTextGlow_a0",
          Wr = "SwitcherBullet_clickArea_84",
          zr = "SwitcherBullet_base__disabled_2a",
          Vr = "SwitcherBullet_disabled_56",
          Ur = "SwitcherBullet_number_08",
          Gr = "SwitcherBullet_currentText_b6",
          jr = "SwitcherBullet_text_e9",
          $r = "SwitcherBullet_texture_b3";
        var Xr, qr;
        (!(function (e) {
          ((e.BIG = "big"), (e.SMALL = "small"));
        })(Xr || (Xr = {})),
          (function (e) {
            ((e.LIGHT = "light"), (e.DARK = "dark"));
          })(qr || (qr = {})));
        const Yr = R.images.gui.maps.icons.components.switcher.numbers,
          Kr = (0, r.memo)(
            ({
              numberToDisplay: e,
              index: t,
              selectedIndex: a,
              previousSelectedIndex: n,
              onChange: u,
              currentIndex: s,
              currentText: i,
              isDisabled: l = !1,
              mouseEnterSound: c,
              clickSound: _,
            }) => {
              const d = t !== a,
                m = (0, r.useState)(!1),
                E = m[0],
                g = m[1],
                p = (0, r.useCallback)(() => {
                  (g(!0), d && j(c));
                }, [d, c]),
                b = (0, r.useCallback)(() => {
                  d && (j(_), u(e));
                }, [d, _, e, u]),
                A = (0, r.useCallback)(() => {
                  g(!1);
                }, []),
                C = s || 0,
                f = v()(
                  wr,
                  t === a && kr,
                  t === a && t === C && Rr,
                  t > C && t !== a && Or,
                  t <= C && Ir,
                  E && Mr,
                  l && zr,
                ),
                h = (0, r.useMemo)(
                  () =>
                    ((e, t, a) =>
                      e === t
                        ? Sr(0)
                        : e === a
                          ? Sr(Math.abs(e - t) - 2)
                          : (a > t && e > t && e < a) || (a < t && e < t && e > a)
                            ? Sr(Math.abs(e - t) - 1)
                            : void 0)(t, n, a),
                  [t, n, a],
                ),
                F = (0, r.useCallback)(
                  () => ((t === a && t === C) || t === a ? Xr.BIG : Xr.SMALL),
                  [t, a, C],
                ),
                D = (0, r.useMemo)(() => {
                  const e = t > C ? qr.LIGHT : qr.DARK;
                  return Object.assign({}, h, {
                    backgroundImage: `url(${Yr.$dyn(`number_${t}_${F()}_${e}`)})`,
                  });
                }, [t, C, h, F]);
              return o().createElement(
                "div",
                { className: f },
                o().createElement(
                  "div",
                  { className: yr, style: h },
                  o().createElement("div", { className: Nr, style: h }),
                  o().createElement("div", { className: xr, style: h }),
                  o().createElement("div", { className: Lr, style: h }),
                  o().createElement("div", { className: Vr }),
                  o().createElement("div", { className: Ur, style: D }),
                  o().createElement("div", {
                    className: Wr,
                    style: h,
                    onClick: b,
                    onMouseEnter: p,
                    onMouseLeave: A,
                  }),
                ),
                i && t === s && o().createElement("div", { className: Gr }, i),
              );
            },
          ),
          Zr = ({
            numberToDisplay: e,
            index: t,
            selectedIndex: a,
            previousSelectedIndex: n,
            onChange: u,
            currentIndex: s = 0,
            isDisabled: i = !1,
            mouseEnterSound: l,
            clickSound: c,
            styleID: _,
          }) => {
            const d = t === a,
              m = (0, r.useState)(!1),
              E = m[0],
              g = m[1],
              p = (0, r.useCallback)(() => {
                (g(!0), d || j(l));
              }, [d, l]),
              b = (0, r.useCallback)(() => {
                d || (j(c), u(e));
              }, [d, c, e, u]),
              A = (0, r.useCallback)(() => {
                g(!1);
              }, []),
              C = R.strings.vehicle_customization.style_switcher
                .$dyn(`style_${_}`)
                .$dyn(`level${e}`),
              f = v()(
                wr,
                d && kr,
                d && t === s && Rr,
                t > s && t !== a && Or,
                t <= s && Ir,
                E && Mr,
                i && zr,
              ),
              h = (0, r.useMemo)(
                () =>
                  ((e, t, a) =>
                    e === t
                      ? Sr(0)
                      : e === a
                        ? Sr(Math.abs(e - t) - 2)
                        : (a > t && e > t && e < a) || (a < t && e < t && e > a)
                          ? Sr(Math.abs(e - t) - 1)
                          : void 0)(t, n, a),
                [t, n, a],
              ),
              F = v()(yr, Tr);
            return o().createElement(
              "div",
              { className: f },
              o().createElement(
                "div",
                { className: F, style: h },
                d && o().createElement("div", { className: $r }),
                !d && o().createElement("div", { className: Hr }),
                o().createElement("div", { className: Pr, style: h }),
                o().createElement("div", { className: jr }, C),
                o().createElement("div", {
                  className: Wr,
                  style: h,
                  onClick: b,
                  onMouseEnter: p,
                  onMouseLeave: A,
                }),
              ),
            );
          },
          Jr = "SwitcherSeparator_base_06",
          Qr = "SwitcherSeparator_base__isBeforeSelectedBullet_a8",
          eo = "SwitcherSeparator_base__notAnimated_73",
          to = "SwitcherSeparator_base__scaled_76",
          ao = "SwitcherSeparator_base__rightTransformOrigin_b8",
          no = "SwitcherSeparator_base__leftTransformOrigin_49",
          uo = "SwitcherSeparator_base__transitionTransformOrigin_9f",
          ro = (0, r.memo)(
            ({ index: e, selectedIndex: t, previousSelectedIndex: a, isAnimated: n = !0 }) => {
              const u = ((e, t, a) =>
                  e === t + 1 || e === t - 1
                    ? Sr(0)
                    : e === a + 1 || e === a - 1
                      ? Sr(Math.abs(a - t) - 2)
                      : (a > t && e > t && e < a + 1) || (a < t && e < t && e > a - 1)
                        ? Sr(Math.abs(e - t) - 1)
                        : void 0)(e, a, t),
                r = 1 === Math.abs(e - t),
                s = 1 === Math.abs(e - a),
                i = ((e, t, a, n) =>
                  e === a + 1 || (e === t + 1 && !n)
                    ? ao
                    : e === a - 1 || (e === t - 1 && !n)
                      ? no
                      : void 0)(e, a, t, r),
                l = v()(
                  Jr,
                  n && e < t && Qr,
                  n && s && r && uo,
                  n && (e === t + 1 || e === t - 1) && to,
                  n && i,
                  !n && eo,
                );
              return o().createElement("div", { className: l, style: u });
            },
          ),
          oo = (e, t) => ("number" == typeof e ? 2 * (e - t) : void 0);
        let so;
        !(function (e) {
          e.small = "small";
        })(so || (so = {}));
        const io = ({
            numberOfBullets: e,
            selectedNumber: t,
            onChange: a,
            currentText: n,
            currentNumber: u,
            startNumber: s = 1,
            isBulletsBeforeCurrentDisabled: i = !1,
            size: l,
            mouseEnterSound: c = "highlight",
            clickSound: _ = "play",
            isArabic: d = !1,
            hasLightShadows: m = !1,
            styleID: E = 0,
            switcherType: g = ja.digital,
          }) => {
            const p = (0, r.useState)(!1),
              b = p[0],
              A = p[1];
            (0, r.useEffect)(() => Fr(() => A(!0), 0), []);
            const C = s + e - 1,
              f = Dr(t, i && u ? u : s, C),
              h = "number" == typeof u ? Dr(u, s, C) : void 0,
              F = oo(f, s),
              D = oo(h, s),
              B = (0, r.useRef)(F);
            (0, r.useEffect)(() => {
              B.current = F;
            });
            const S = B.current,
              w = v()(
                Br.base,
                n && void 0 !== D && Br.base__hasCurrentText,
                l && Br[`base__${l}`],
                b && Br.base__isVisible,
              ),
              y = (0, r.useMemo)(
                () =>
                  ((e, t) => {
                    const a = [];
                    for (let n = e; n <= t; n++) a.push(n);
                    return a;
                  })(s, C),
                [C, s],
              ),
              k = g === ja.digital;
            return o().createElement(
              "div",
              { className: w },
              y.map((e, t) => {
                const u = 2 * t,
                  r = !(!i || !D) && u < D;
                return o().createElement(
                  o().Fragment,
                  { key: t },
                  t > 0 &&
                    o().createElement(ro, {
                      index: u - 1,
                      selectedIndex: F,
                      previousSelectedIndex: S,
                      isAnimated: k,
                    }),
                  k
                    ? o().createElement(Kr, {
                        index: u,
                        selectedIndex: F,
                        previousSelectedIndex: S,
                        numberToDisplay: e,
                        currentIndex: D,
                        currentText: n,
                        onChange: a,
                        isDisabled: r,
                        mouseEnterSound: c,
                        clickSound: _,
                        isArabic: d,
                        hasLightShadows: m,
                      })
                    : o().createElement(Zr, {
                        index: u,
                        selectedIndex: F,
                        previousSelectedIndex: S,
                        numberToDisplay: e,
                        currentIndex: D,
                        onChange: a,
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
          lo = "Tab_base_05",
          co = "Tab_content_99",
          _o = "Tab_base__selected_4b",
          mo = "Tab_base__accent_b2",
          Eo = "Tab_selectedDivider_25",
          go = "Tab_selectedDivider__left_57",
          po = "Tab_selectedDivider__right_78",
          bo = "Tab_divider_0e",
          Ao = "Tab_divider__left_ac",
          Co = "Tab_divider__right_44",
          fo = "Tab_icon_fb",
          ho = "Tab_base__hover_54",
          vo = "Tab_plus_2d",
          Fo = "Tab_iconWrapper_c5",
          Do = "Tab_label_e8",
          Bo = "Tab_highlight_1c",
          So = "Tab_highlight__left_87",
          wo = "Tab_highlight__right_d6",
          yo = "Tab_tick_a3",
          ko = "Tab_tabsDivider_17",
          To = "Tab_bubble_4f";
        let No;
        !(function (e) {
          ((e.Active = "active"), (e.Accent = "accent"), (e.Default = "default"));
        })(No || (No = {}));
        const Io = R.images.gui.maps.icons.customization.tabs,
          Mo = R.strings.customization.itemTypes,
          xo = R.strings.customization.tooltips.tabs,
          Oo = (0, r.memo)(
            ({
              id: e,
              itemType: t,
              isFirst: a,
              isPlus: n,
              isLast: u,
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
                p = g[0],
                b = g[1],
                A = (0, r.useCallback)(() => {
                  _ || ($.playHighlight(), b(!0), E && E(e));
                }, [e, _, E]),
                C = (0, r.useMemo)(() => {
                  let e;
                  return (
                    (e = _ ? No.Active : c ? No.Accent : No.Default),
                    { backgroundImage: `url(${Io.$dyn(`${t}_${e}`)})` }
                  );
                }, [c, _, t]),
                f = v()(lo, p && ho, _ && _o, c && !_ && mo);
              return o().createElement(
                "div",
                {
                  onClick: () => {
                    m(e);
                  },
                  onMouseEnter: A,
                  onMouseLeave: () => {
                    b(!1);
                  },
                  className: f,
                },
                a && !_ && o().createElement("div", { className: v()(bo, Ao) }),
                o().createElement(
                  Ua,
                  {
                    header: String(xo.$dyn(`${t}_title`)),
                    body: String(xo.$dyn(`${t}_description`)),
                  },
                  o().createElement(
                    "div",
                    { className: co },
                    o().createElement(
                      "div",
                      { className: Fo },
                      o().createElement("div", { className: fo, style: C }),
                      n && o().createElement("div", { className: vo }),
                    ),
                    o().createElement("div", { className: Do }, Mo.$dyn(`${t}`)),
                    _
                      ? o().createElement(
                          o().Fragment,
                          null,
                          o().createElement("div", { className: v()(Bo, So) }),
                          o().createElement("div", { className: v()(Bo, wo) }),
                          o().createElement("div", { className: yo }),
                          o().createElement("div", { className: v()(Eo, go) }),
                          o().createElement("div", { className: v()(Eo, po) }),
                        )
                      : o().createElement(
                          o().Fragment,
                          null,
                          s && o().createElement("div", { className: v()(bo, Ao) }),
                          i && o().createElement("div", { className: v()(bo, Co) }),
                        ),
                  ),
                ),
                !i && !_ && !l && o().createElement("div", { className: u ? v()(bo, Co) : ko }),
                Boolean(d) && o().createElement(ua, { className: To, text: d.toString() }),
              );
            },
          ),
          Lo = "Tabs_base_51",
          Ro = "Tabs_tabs_ab",
          Po = "Tabs_groupDivider_b2";
        function Ho() {
          return (
            (Ho =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ho.apply(this, arguments)
          );
        }
        const Wo = (0, r.memo)(
            ({
              isEditable: e,
              tabs: t,
              onClick: a,
              onHoverTab: n,
              onEditClose: u,
              mixClass: r,
            }) => {
              var s;
              const i = null == (s = t.find((e) => e.isSelected)) ? void 0 : s.groupId;
              return o().createElement(
                "div",
                { className: v()(Lo, r) },
                t &&
                  t.map((e, u) => {
                    const r = t[u + 1],
                      s = t[u - 1],
                      l = r && r.isSelected,
                      c = s && e.groupId !== s.groupId,
                      _ = r && e.groupId !== r.groupId,
                      d = e.groupId === i;
                    return o().createElement(
                      "div",
                      { key: `${u}-${e.id}`, className: Ro },
                      o().createElement(
                        Oo,
                        Ho(
                          {
                            isFirst: 0 === u,
                            isLast: u === t.length - 1,
                            isNextSelected: l,
                            isPrevAnotherGroup: c,
                            isNextAnotherGroup: _,
                            isAccent: d,
                            onClick: a,
                            onHoverTab: n,
                          },
                          e,
                        ),
                      ),
                      _ && o().createElement("div", { className: Po }),
                    );
                  }),
                e && o().createElement(je, { onCloseCallback: u }),
              );
            },
          ),
          zo = "ExtendedItem_base_8b",
          Vo = "ExtendedItem_hoverBg_5c",
          Uo = "ExtendedItem_hoverBg__visible_6a",
          Go = "ExtendedItem_toggleBorder_9c",
          jo = "ExtendedItem_toggleBorder__select_01",
          $o = "ExtendedItem_toggle_24",
          Xo = "ExtendedItem_size_1c",
          qo = "ExtendedItem_paletteIcon_87",
          Yo = R.images.gui.maps.icons.customization.toolbar.extended,
          Ko = (0, r.memo)(({ item: e, onActionClick: t, actionType: a }) => {
            const n = e.actionData,
              u = e.isSelected,
              s = e.icon,
              i = e.paletteIcon,
              l = (0, r.useState)(!1),
              c = l[0],
              _ = l[1],
              d = u ? Yo.toggle_on() : Yo.toggle_default();
            return o().createElement(
              "div",
              {
                className: zo,
                onClick: () => {
                  (t(a, n), $.playClick());
                },
                onMouseEnter: () => {
                  (_(!0), $.playHighlight());
                },
                onMouseLeave: () => {
                  _(!1);
                },
              },
              o().createElement("div", { className: v()(Vo, c && Uo) }),
              o().createElement("div", { className: v()(Go, u && jo) }),
              o().createElement("div", { className: $o, style: { backgroundImage: `url(${d})` } }),
              Boolean(s.length) && o().createElement(ua, { className: Xo, text: s }),
              Boolean(i.length) &&
                o().createElement("div", {
                  className: qo,
                  style: { backgroundImage: `url(${i})` },
                }),
            );
          }),
          Zo = "ExtendedSubButtons_base_b5",
          Jo = "ExtendedSubButtons_bg_4f",
          Qo = "ExtendedSubButtons_content_17",
          es = (0, r.memo)(({ subButtons: e, onMouseLeave: t, onActionClick: a, actionType: n }) =>
            o().createElement(
              "div",
              { className: Zo, onMouseLeave: t },
              o().createElement(
                "div",
                { className: Qo },
                o().createElement("div", { className: Jo }),
                e.map((e) =>
                  o().createElement(Ko, {
                    key: e.actionData,
                    item: e,
                    onActionClick: a,
                    actionType: n,
                  }),
                ),
              ),
            ),
          ),
          ts = "ToolbarItem_base_c1",
          as = "ToolbarItem_base__disable_40",
          ns = "ToolbarItem_hoverBg_89",
          us = "ToolbarItem_hoverBg__visible_c9",
          rs = "ToolbarItem_icon_65",
          os = "ToolbarItem_icon__disable_ef",
          ss = "ToolbarItem_disable_43",
          is = "ToolbarItem_hoveredIcon_a8",
          ls = "ToolbarItem_base__hover_02",
          cs = "ToolbarItem_actionName_38",
          _s = "ToolbarItem_arrow_f4",
          ds = "ToolbarItem_arrow__left_00",
          ms = "ToolbarItem_arrow__leftHover_72",
          Es = "ToolbarItem_arrow__right_a9",
          gs = "ToolbarItem_arrow__rightHover_a9",
          ps = "ToolbarItem_arrow__leftDisable_8c",
          bs = "ToolbarItem_arrow__rightDisable_bd";
        let As, Cs;
        (!(function (e) {
          ((e[(e.RIGHT = 0)] = "RIGHT"), (e[(e.LEFT = 1)] = "LEFT"));
        })(As || (As = {})),
          (function (e) {
            ((e.COLOR_CHANGE = "color_change"), (e.SCALE_CHANGE = "scale_change"));
          })(Cs || (Cs = {})));
        const fs = R.images.gui.maps.icons.customization.toolbar,
          hs = [Cs.COLOR_CHANGE, Cs.SCALE_CHANGE],
          vs = [
            Ga.CUSTOMIZATION_SHEET_ACTION_REMOVE_ONE,
            Ga.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_SEASONS,
            Ga.CUSTOMIZATION_SHEET_ACTION_REMOVE_FROM_ALL_PARTS,
          ],
          Fs = (0, r.memo)(({ toolbarItem: e, onItemClick: t, onItemOver: a, isSelected: n }) => {
            const u = e.actionType,
              s = e.isEnabled,
              i = e.actionBtnLabel,
              l = e.subButtons,
              c = e.progressionLevel,
              _ = `${u}${c}`,
              d = c > 0,
              m = s ? fs.default.$dyn(d ? _ : u) : fs.disable.$dyn(u),
              E = fs.idle.$dyn(d ? _ : u),
              g = (0, r.useState)(!1),
              p = g[0],
              b = g[1],
              A = (0, r.useState)(!1),
              C = A[0],
              f = A[1],
              h = (0, r.useState)(!1),
              F = h[0],
              D = h[1],
              B = (0, r.useState)({ left: !1, right: !1 }),
              S = B[0],
              w = B[1],
              y = hs.includes(u);
            (0, r.useEffect)(() => {
              (n && s && b(!0), n && y && D(!0));
            }, [n, y, s]);
            const k = (0, r.useCallback)(() => {
                (f(!1), n && y && f(!0));
              }, [n, y]),
              T = (e, a) => {
                (e.stopPropagation(), t(u, a));
              },
              N = (e) => {
                s &&
                  (e === As.LEFT
                    ? w((e) => Object.assign({}, e, { left: !0 }))
                    : w((e) => Object.assign({}, e, { right: !0 })));
              },
              I = (e) => {
                s &&
                  (e === As.LEFT
                    ? w((e) => Object.assign({}, e, { left: !1 }))
                    : w((e) => Object.assign({}, e, { right: !1 })));
              },
              M = y && C && n,
              x = v()(ts, p && ls, !s && as),
              O = v()(_s, ds, S.left && s && ms, !s && ps),
              L = v()(_s, Es, S.right && s && gs, !s && bs);
            return o().createElement(
              "div",
              {
                onMouseEnter: () => {
                  s && (b(!0), y && !C && f(!0), a(u), $.playHighlight());
                },
                onMouseLeave: () => {
                  (b(!1), C && f(!1), F && D(!1));
                },
                onClick: () => {
                  s &&
                    !y &&
                    (u === Ga.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_SEASONS
                      ? j(R.sounds.cust_select_double())
                      : u === Ga.CUSTOMIZATION_SHEET_ACTION_APPLY_TO_ALL_PARTS
                        ? j(R.sounds.cust_color_apply())
                        : vs.includes(u)
                          ? j(R.sounds.cust_select_remove())
                          : j(R.sounds.cust_select()),
                    t(u, d ? As.RIGHT : -1));
                },
                className: x,
              },
              (M || F) &&
                s &&
                o().createElement(es, {
                  subButtons: l,
                  actionType: u,
                  onActionClick: t,
                  onMouseLeave: k,
                }),
              o().createElement("div", { className: v()(ns, p && us) }),
              !s && o().createElement("div", { className: ss }),
              o().createElement(ua, { text: i, className: cs }),
              d &&
                o().createElement("div", {
                  className: O,
                  onMouseEnter: () => N(As.LEFT),
                  onMouseLeave: () => I(As.LEFT),
                  onClick: (e) => T(e, As.LEFT),
                }),
              o().createElement("div", {
                className: v()(rs, !s && os),
                style: { backgroundImage: `url(${m})` },
              }),
              o().createElement("div", { className: is, style: { backgroundImage: `url(${E})` } }),
              d &&
                o().createElement("div", {
                  className: L,
                  onMouseEnter: () => N(As.RIGHT),
                  onMouseLeave: () => I(As.RIGHT),
                  onClick: (e) => T(e, As.RIGHT),
                }),
            );
          }),
          Ds = "Toolbar_base_56",
          Bs = "Toolbar_content_31",
          Ss = { type: "", index: -1 },
          ws = (0, r.memo)(({ toolbarItems: e, onItemClick: t }) => {
            const a = (0, r.useState)(Ss),
              n = a[0],
              u = a[1];
            (0, r.useEffect)(() => () => u(Ss), [e]);
            const s = (0, r.useCallback)((e) => {
                u((t) => Object.assign({}, t, { type: e }));
              }, []),
              i = (0, r.useCallback)(
                (e, a, n) => {
                  (t(e, a), u({ type: e, index: n }));
                },
                [t],
              );
            return o().createElement(
              "div",
              { className: Ds },
              o().createElement(
                "div",
                { className: Bs },
                e.map((e, t) =>
                  o().createElement(
                    Fu,
                    {
                      key: e.actionType,
                      tooltipArgs: {
                        body: e.disableTooltip,
                        isEnabled: Boolean(e.disableTooltip.length),
                      },
                    },
                    o().createElement(Fs, {
                      key: e.actionType,
                      toolbarItem: e,
                      onItemClick: (e, a) => i(e, a, t),
                      onItemOver: s,
                      isSelected: n.type === e.actionType || t === n.index,
                    }),
                  ),
                ),
              ),
            );
          }),
          ys = "AllSeasonsHint_base_d7",
          ks = "AllSeasonsHint_text_7b",
          Ts = R.strings.customization.customization.allSeasonsHint,
          Ns = R.strings.customization.itemTypes,
          Is = (0, r.memo)(({ itemType: e, isSelected: t, onSelectApplyingAllSeasons: a }) => {
            const n = y().mediaSize <= B.Small,
              u = n ? _n.medium : _n.large;
            return o().createElement(
              Ua,
              { header: Ts.tooltip.header(), body: Ts.tooltip.body() },
              o().createElement(
                "div",
                { className: ys },
                o().createElement(
                  pn,
                  {
                    isChecked: t,
                    size: u,
                    type: dn.main,
                    soundHover: R.sounds.highlight(),
                    soundClick: R.sounds.play(),
                    onChange: () => {
                      a();
                    },
                  },
                  o().createElement(ua, {
                    text: n ? Ts.shortText() : Ts.text(),
                    className: ks,
                    format: {
                      binding: !n && e ? { item: String(Ns.$dyn(`${e}`)).toLowerCase() } : void 0,
                    },
                  }),
                ),
              ),
            );
          }),
          Ms = 33,
          xs = 0,
          Os = !0,
          Ls = "play";
        const Rs = [
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
        function Ps() {
          return (
            (Ps =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ps.apply(this, arguments)
          );
        }
        const Hs = (0, r.memo)(function (e) {
            let t = e.width,
              a = e.height,
              n = e.getImageSource,
              u = e.frameCount,
              s = e.onAnimate,
              i = e.frameTime,
              l = void 0 === i ? Ms : i,
              c = e.initialFrameIndex,
              _ = void 0 === c ? xs : c,
              d = e.lastFrameIndex,
              m = void 0 === d ? u - 1 : d,
              E = e.loop,
              g = void 0 === E ? Os : E,
              p = e.state,
              b = void 0 === p ? Ls : p,
              A = e.onAnimationDone,
              C = e.onAnimationComplete,
              f = e.poster,
              h = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Rs);
            const v = (0, r.useRef)(null);
            return (
              (0, r.useEffect)(() => {
                const e = v.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  a = (a) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(a.img, -a.x, -a.y));
                  };
                switch (b) {
                  case "play":
                    return (function () {
                      const e = Vs(_, m, n),
                        t = Ws(_, m),
                        u = window.setInterval(() => {
                          const n = t(),
                            r = e.get(n);
                          r
                            ? (null == s || s(n, r),
                              a(r),
                              n === m &&
                                (null == C || C(),
                                g || (null == A || A(), window.clearInterval(u))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, l);
                      return () => window.clearInterval(u);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === _ && f ? { path: f, x: 0, y: 0 } : n(_),
                        t = new Image();
                      t.src = e.path;
                      const u = () => a(zs(e, t));
                      return (
                        t.addEventListener("load", u),
                        () => t.removeEventListener("load", u)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [l, n, _, m, g, s, C, A, f, b]),
              o().createElement("canvas", Ps({}, h, { width: t, height: a, ref: v }))
            );
          }),
          Ws = (e, t) => {
            let a = e;
            return () => {
              const n = a;
              return ((a += 1), a > t && (a = e), n);
            };
          },
          zs = (e, t) => Object.assign({}, e, { img: t }),
          Vs = (e, t, a) => {
            const n = new Map(),
              u = {};
            for (let r = e; r <= t; r++) {
              const e = a(r),
                t = u[e.path];
              if (t) n.set(r, zs(e, t));
              else {
                const t = new Image();
                ((u[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${r})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  n.set(r, zs(e, t)));
              }
            }
            return n;
          };
        let Us;
        !(function (e) {
          ((e.Active = "active"), (e.Ending = "ending"), (e.Disabled = "disabled"));
        })(Us || (Us = {}));
        const Gs = (e) => (e < 0.5 ? 4 * e * e * e : (e - 1) * (2 * e - 2) * (2 * e - 2) + 1),
          js = (e) => {
            const t = ((e) => {
                const t = new Date(1e3 * e);
                return { day: t.getDate(), month: t.getMonth() };
              })(e),
              a = t.day,
              n = t.month;
            return { day: a, month: R.strings.menu.dateTime.months.$num(n + 1) };
          },
          $s = (0, r.memo)(
            ({
              children: e,
              isVisible: t = !0,
              delay: a = 0,
              duration: n = 800,
              opacityFrom: u = 0,
              opacityEnter: r = 1,
              opacityLeave: s = 0,
              classMix: i,
            }) =>
              (0, K.useTransition)(t, {
                key: t,
                from: { opacity: u },
                enter: { opacity: r },
                leave: { opacity: s },
                delay: a,
                config: { duration: n, easing: Gs },
              })((t, a) => a && o().createElement(K.animated.div, { className: i, style: t }, e)),
          ),
          Xs = {
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
        function qs() {
          return (
            (qs =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            qs.apply(this, arguments)
          );
        }
        var Ys;
        !(function (e) {
          ((e.Large = "large"), (e.Big = "big"), (e.Medium = "medium"), (e.Small = "small"));
        })(Ys || (Ys = {}));
        const Ks = R.strings.event.customizationResource,
          Zs = {
            width: 280,
            height: 170,
            frameCount: 136,
            chunk: { count: 1, rows: 20, columns: 7 },
            getChunkPath: () =>
              "R.images.gui.maps.icons.event.customizationResource.entryPoint.particles_sequence",
          },
          Js = (function (e) {
            const t = e.chunk,
              a = t.rows * t.columns;
            return (n) => {
              const u = n % a,
                r = (u % t.columns) * e.width,
                o = Math.trunc(u / t.columns) * e.height;
              return { path: e.getChunkPath(Math.trunc(n / a)), x: r, y: o };
            };
          })(Zs),
          Qs = (e) => {
            const t = (function (e = 0) {
                let t = e;
                const a = Math.trunc(t / Ka);
                t -= a * Ka;
                const n = Math.trunc(t / Ya);
                t -= n * Ya;
                const u = Math.trunc(t / qa);
                return ((t -= u * qa), { days: a, hours: n, minutes: u, seconds: t });
              })(e),
              a = t.days,
              n = t.hours,
              u = t.minutes,
              r = R.strings.common.duration;
            if (a) {
              let e = Ks.eventFinishFormat() + Rt(r.days(), { days: a });
              return (n && (e += " " + Rt(r.hours(), { hours: n })), e);
            }
            if (n) {
              let e = Ks.eventFinishFormat() + Rt(r.hours(), { hours: n });
              return (u && (e += " " + Rt(r.minutes(), { minutes: u })), e);
            }
            return u
              ? Ks.eventFinishFormat() + Rt(r.minutes(), { minutes: u })
              : Ks.lessThanMinute();
          },
          ei = (0, Le.Pi)(({ mixClass: e }) => {
            const t = mr(),
              a = t.controls,
              n = t.model,
              u = y().mediaSize,
              s = (function (e = {}, t = []) {
                var a, n, u, o;
                const s = (0, r.useState)(null != (a = e.state) ? a : Ls),
                  i = s[0],
                  l = s[1],
                  c = (0, r.useState)(null != (n = e.initialFrameIndex) ? n : xs),
                  _ = c[0],
                  d = c[1],
                  m = (0, r.useState)(null != (u = e.frameTime) ? u : Ms),
                  E = m[0],
                  g = m[1],
                  p = (0, r.useState)(null != (o = e.loop) ? o : Os),
                  b = p[0],
                  A = p[1],
                  C = (0, r.useRef)(_),
                  f = (0, r.useCallback)((e) => {
                    (d(e), l("play"));
                  }, []),
                  h = (0, r.useCallback)((e) => {
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
                    loop: b,
                    onAnimate: (0, r.useCallback)((t, a) => {
                      ((C.current = t), null == e.onAnimate || e.onAnimate(t, a));
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
                  goAndPlay: f,
                  goAndStop: h,
                  stop: v,
                  play: F,
                  pause: D,
                };
              })(),
              i = n.root.get(),
              l = i.timer,
              c = i.status,
              _ = i.isLimitsUpdated,
              d = i.isAloneBanner,
              m = c === Us.Active,
              E = c === Us.Disabled,
              g = c === Us.Ending,
              p = tn(l - Math.floor(Date.now() / 1e3), qa);
            const b = (0, r.useMemo)(() => Qs(p), [p]),
              A = (0, r.useState)(!1),
              C = A[0],
              f = A[1],
              h = (0, r.useMemo)(() => js(l), [l]),
              F = h.day,
              D = h.month,
              S = (0, r.useMemo)(
                () =>
                  u >= B.Large ? Ys.Large : d ? Ys.Big : u === B.Medium ? Ys.Medium : Ys.Small,
                [u, d],
              ),
              w = (0, K.useSpring)({
                from: { x: 0, opacity: 0 },
                to: { x: 0, opacity: 1 },
                delay: 0,
                config: { duration: 800, easing: Gs },
              });
            return o().createElement(
              K.animated.div,
              {
                className: v()(
                  Xs.base,
                  E && Xs.base__disabled,
                  Xs[`base__${S}`],
                  C && Xs.base__hover,
                  d && Xs.base__isAloneBanner,
                  e,
                ),
                onMouseEnter: () => {
                  E || ($.playHighlight(), f(!0));
                },
                onMouseLeave: () => {
                  f(!1);
                },
                onClick: () => {
                  E || ($.playClick(), a.toCustomizationResourceEvent());
                },
                style: w,
              },
              o().createElement("div", { className: Xs.bg }),
              o().createElement("div", { className: Xs.shadow }),
              o().createElement($s, { classMix: Xs.highlight, isVisible: C }),
              o().createElement(
                "div",
                { className: Xs.content },
                o().createElement(ua, { className: Xs.title, text: Ks.title() }),
                _ &&
                  o().createElement(ua, {
                    className: Xs.subTitle,
                    text: u >= B.Large ? Ks.subTitle() : Ks.shortSubTitle(),
                  }),
              ),
              o().createElement(
                "div",
                { className: v()(Xs.timeContent, E && Xs.timeContent__disabled) },
                m &&
                  o().createElement(ua, {
                    className: Xs.timeActive,
                    text: Ks.endDateText(),
                    format: { binding: { day: F, month: D } },
                  }),
                g && o().createElement(ua, { className: Xs.timeEnding, text: b }),
                E &&
                  o().createElement(ua, { className: Xs.timeEnding, text: Ks.unavailable.text() }),
              ),
              _ &&
                o().createElement(
                  Hs,
                  qs({}, s.props, {
                    width: Zs.width,
                    height: Zs.height,
                    frameCount: Zs.frameCount,
                    getImageSource: Js,
                    frameTime: 50,
                    loop: !0,
                    className: Xs.particles,
                  }),
                ),
            );
          });
        let ti;
        !(function (e) {
          ((e[(e.Empty = 0)] = "Empty"),
            (e[(e.SubmitEnter = 1)] = "SubmitEnter"),
            (e[(e.FirstEnter = 2)] = "FirstEnter"),
            (e[(e.EditEnter = 3)] = "EditEnter"),
            (e[(e.NotAvailableEnter = 4)] = "NotAvailableEnter"));
        })(ti || (ti = {}));
        const ai = "Inscription_base_27",
          ni = "Inscription_base__invalidInput_3d",
          ui = "Inscription_base__show_19",
          ri = "Inscription_base__hide_4c",
          oi = "Inscription_base__withIcons_ea",
          si = "Inscription_invalidEnterIcon_5f",
          ii = "Inscription_icons_1d",
          li = "Inscription_icon_44",
          ci = "Inscription_icon__withDelete_9a",
          _i = "Inscription_text_7e",
          di = "Inscription_invalidNumber_78",
          mi = R.strings.vehicle_customization.propertySheet.inscriptionController,
          Ei = {
            [ti.Empty]: "",
            [ti.EditEnter]: mi.editEnter(),
            [ti.FirstEnter]: mi.firstEnter(),
            [ti.SubmitEnter]: mi.submitEnter(),
            [ti.NotAvailableEnter]: mi.notAvailableEnter(),
          },
          gi = {
            [ti.Empty]: [],
            [ti.EditEnter]: [
              R.images.gui.maps.icons.customization.inscription_controller.bspace_btn(),
              R.images.gui.maps.icons.customization.inscription_controller.delete_btn(),
            ],
            [ti.FirstEnter]: [],
            [ti.SubmitEnter]: [
              R.images.gui.maps.icons.customization.inscription_controller.enter_btn(),
            ],
            [ti.NotAvailableEnter]: [],
          },
          pi = (0, r.memo)(
            ({
              inscriptionState: e,
              inscriptionDuration: t,
              inscriptionDelay: a,
              invalidInscriptionNumber: n,
              inscriptionFirstEnterRange: u,
              startTimestamp: s,
            }) => {
              const i = (0, r.useState)(!1),
                l = i[0],
                c = i[1],
                _ = (0, r.useState)(e),
                d = _[0],
                m = _[1],
                E = nn(),
                g = nn();
              (0, r.useEffect)(
                () => (
                  c(!1),
                  g.run(() => {
                    (c(!0), m(e));
                  }, a),
                  E.run(() => {
                    c(!1);
                  }, t + a),
                  () => {
                    (g.clear(), E.clear());
                  }
                ),
                [s],
              );
              const p = d === ti.NotAvailableEnter;
              return o().createElement(
                "div",
                { className: v()(ai, p && ni, l && ui, !l && ri, Boolean(gi[d].length) && oi) },
                p && o().createElement("div", { className: si }),
                o().createElement(ua, {
                  className: _i,
                  text: Ei[d],
                  format: {
                    binding: {
                      value: o().createElement(ua, { className: di, text: n }),
                      start: Boolean(u.length) && u[0],
                      end: Boolean(u.length > 1) && u[1],
                    },
                  },
                }),
                !p &&
                  Boolean(gi[d].length) &&
                  o().createElement(
                    "div",
                    { className: ii },
                    gi[d].map((e, t) =>
                      o().createElement("div", {
                        className: v()(li, d === ti.EditEnter && ci),
                        key: t,
                        style: { backgroundImage: `url(${e})` },
                      }),
                    ),
                  ),
              );
            },
          ),
          bi = {
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
          Ai = ({ isEnabled: e, icon: t, isWide: a, isDim: n, formFactor: u, selectedTab: s }) => {
            const l = (0, r.useRef)(null),
              c = en(e);
            ((0, r.useEffect)(() => {
              !e && c && s !== Bd.INSCRIPTION && j(R.sounds.cancelcloseno());
            }, [e, c, s]),
              (0, r.useEffect)(() => {
                if (!e) return;
                const t = i.O.client.events.mouse.move(([{ clientX: e, clientY: t }, a]) => {
                  const n = l.current;
                  n &&
                    ("outside" !== a
                      ? (n.style.setProperty("--visibility", "visible"),
                        n.style.setProperty("--x", `${viewEnv.pxToRem(e + 7)}rem`),
                        n.style.setProperty("--y", `${viewEnv.pxToRem(t + -40)}rem`))
                      : n.style.setProperty("--visibility", "hidden"));
                });
                return () => {
                  t();
                };
              }, [e]));
            const _ = u > 0,
              d = v()(bi.base, !_ && a && bi.base__wide, _ && bi[`base__factor${u}`]);
            return o().createElement(
              "div",
              { className: d },
              e &&
                o().createElement(
                  "div",
                  { ref: l, className: bi.wrapper },
                  n && o().createElement("div", { className: bi.shine }),
                  o().createElement("div", {
                    className: bi.icon,
                    style: { backgroundImage: `url(${t})` },
                  }),
                  o().createElement("div", { className: bi.border }),
                ),
            );
          },
          Ci = "SceneHitArea_base_ec",
          fi = "SceneHitArea_base__down_e8",
          hi = "SceneHitArea_base__cursorActive_6e";
        let vi;
        !(function (e) {
          ((e.None = "none"), (e.Ready = "ready"), (e.Dragging = "dragging"));
        })(vi || (vi = {}));
        const Fi = ({
            moveSpace: e,
            onSceneOverChange: t,
            onSceneDraggingChange: a,
            onSceneClick: n,
            onHideElements: u,
            onResetMagneticTool: s,
            isHovered: l,
            isOnboardingViewOpened: c = !1,
          }) => {
            const _ = (0, r.useState)(!1),
              d = _[0],
              m = _[1],
              E = (0, r.useRef)({ x: 0, y: 0, state: vi.None }),
              g = (0, r.useRef)(null),
              p = (0, r.useRef)(null);
            ((0, r.useEffect)(() => {
              const e = i.O.client.events.mouse.up(([e]) => {
                (m(!1),
                  E.current.state === vi.Ready && n(),
                  p.current && (clearTimeout(p.current), (p.current = null)),
                  u(!1),
                  a(!1));
                const t = e;
                if (t && t.button === ln.RIGHT) s();
                else {
                  const e = t && t.target;
                  e && e !== g.current && !e.closest("[data-magnetic-tool-support]") && s();
                }
                E.current.state = vi.None;
              });
              return () => e();
            }, [E, u, n, a, s]),
              (0, r.useEffect)(
                () => () => {
                  p.current && clearTimeout(p.current);
                },
                [],
              ));
            const b = (e) => {
              if (!g.current) return;
              const t = g.current.getBoundingClientRect(),
                a = t.width,
                n = t.height;
              return !(
                0 === e.clientX ||
                0 === e.clientY ||
                e.clientX >= a - 1 ||
                e.clientY >= n - 1
              );
            };
            return o().createElement("div", {
              className: v()(Ci, d && fi, l && hi),
              ref: g,
              onMouseDown: (e) => {
                (e.preventDefault(),
                  e.button === ln.LEFT &&
                    b(e) &&
                    (m(!0),
                    (E.current.x = e.clientX),
                    (E.current.y = e.clientY),
                    (E.current.state = vi.Ready),
                    a(!0),
                    (p.current = setTimeout(() => {
                      ((p.current = null), u(!0));
                    }, 200))));
              },
              onMouseMove: (t) => {
                if ((t.preventDefault(), d)) {
                  if (!b(t)) return;
                  const a = E.current,
                    n = t.clientX !== a.x ? t.clientX - a.x : 0,
                    r = t.clientY !== a.y ? t.clientY - a.y : 0;
                  (0 !== n && 0 !== r && (a.state = vi.Dragging),
                    (a.x = t.clientX),
                    (a.y = t.clientY),
                    e({ dx: n, dy: r, dz: 0 }),
                    p.current && (clearTimeout(p.current), (p.current = null), u(!0)));
                }
              },
              onWheel: (t) => {
                if ((t.preventDefault(), !b(t))) return;
                const a = t.deltaY < 0;
                e({ dx: 0, dy: 0, dz: a ? -600 : 600 });
              },
              onMouseEnter: () => {
                !c && t(!0);
              },
              onMouseLeave: () => {
                !c && t(!0);
              },
            });
          },
          Di = "BannerDecals_base_b8",
          Bi = "BannerDecals_base__hover_b3",
          Si = "BannerDecals_title_f7",
          wi = R.strings.customization,
          yi = (0, r.memo)(({ onClick: e, onMouseLeave: t, onMouseEnter: a, mixClass: n }) => {
            const u = (0, r.useState)(!1),
              s = u[0],
              i = u[1],
              l = (0, r.useState)(!1),
              c = l[0],
              _ = l[1];
            return o().createElement(
              "div",
              {
                className: v()(Di, s && Bi, n),
                onMouseEnter: () => {
                  (a && a(), i(!0), $.playHighlight());
                },
                onMouseLeave: () => {
                  (!c && t && t(), i(!1));
                },
                onClick: () => {
                  (a && a(), _(!0), $.playClick(), e());
                },
              },
              o().createElement(ua, { className: Si, text: wi.customization.decalsBanner() }),
            );
          }),
          ki = {
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
          Ti = R.strings.customization.customization.seasonsTabs,
          Ni = R.images.gui.maps.icons.customization.seasons,
          Ii = (0, r.memo)(
            ({
              onClick: e,
              isSelected: t,
              season: a,
              isShowFullTabContent: n,
              isAllTabsFull: u,
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
                p = nn(),
                b = null != (l = en(s)) ? l : s;
              ((0, r.useEffect)(() => {
                if (p.isRunning) return () => p.clear();
              }, [p]),
                (0, r.useEffect)(() => {
                  (!b && s && (g(!0), !u && j(R.sounds.cust_tick_on())),
                    b && !s && j(R.sounds.cust_tick_off()));
                }, [b, s, p, u]),
                (0, r.useEffect)(() => {
                  if (E)
                    return p.run(() => {
                      g(!1);
                    }, 1200);
                }, [p, E]));
              const A = (0, r.useCallback)(() => {
                  p.isRunning || e(a);
                }, [p, e, a]),
                C = v()(
                  ki.base,
                  ki[`base__${a}`],
                  s && !E && ki.base__full,
                  E && ki.base__animatingAppear,
                  !E && null !== E && ki.base__animatingDisappear,
                  _ && ki.base__hover,
                  t && ki.base__active,
                  n && ki.base__fullContent,
                  i,
                );
              return o().createElement(
                "div",
                {
                  onMouseEnter: () => {
                    t || (0, da.wU)() || (d(!0), $.playHighlight());
                  },
                  onMouseLeave: () => {
                    d(!1);
                  },
                  onClick: A,
                  className: C,
                },
                o().createElement("div", { className: ki.background }),
                t &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", { className: ki.blink }),
                    o().createElement(
                      "div",
                      {
                        className: ki.activeTab,
                        style: { backgroundImage: `url(${Ni.$dyn(`${a}_bg`)})` },
                      },
                      o().createElement("div", {
                        className: ki.shine,
                        style: { backgroundImage: `url(${Ni.$dyn(`${a}_shine`)})` },
                      }),
                    ),
                  ),
                o().createElement(
                  "div",
                  { className: ki.iconsWrapper },
                  o().createElement(
                    "div",
                    { className: ki.seasonIconWrapper },
                    o().createElement("div", {
                      className: v()(
                        ki.seasonIcon,
                        _ || t ? ki.seasonIcon__hide : ki.seasonIcon__show,
                      ),
                      style: { backgroundImage: `url(${Ni.$dyn(`${a}_default`)})` },
                    }),
                    o().createElement("div", {
                      className: v()(
                        ki.seasonIcon,
                        _ || t ? ki.seasonIcon__show : ki.seasonIcon__hide,
                      ),
                      style: { backgroundImage: `url(${Ni.$dyn(`${a}_active`)})` },
                    }),
                  ),
                  o().createElement("div", { className: ki.plus }),
                  o().createElement("div", { className: ki.check }),
                ),
                o().createElement(
                  "div",
                  { className: ki.titleWrapper },
                  o().createElement(ua, { text: Ti.$dyn(`${a}`), className: ki.title }),
                  t && o().createElement(ua, { text: Ti.map(), className: ki.title }),
                ),
                o().createElement(
                  "div",
                  { className: ki.flareWrapper },
                  o().createElement("div", { className: ki.flare }),
                ),
                t && o().createElement("div", { className: ki.blik }),
              );
            },
          ),
          Mi = "SeasonsTabs_base_24",
          xi = "SeasonsTabs_base__show_61";
        function Oi() {
          return (
            (Oi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Oi.apply(this, arguments)
          );
        }
        const Li = ({ tabs: e, isMinimised: t, onClick: a, className: n }) => {
            const u = y().mediaSize,
              s = !t && u >= B.Medium,
              i = e.every((e) => e.isFull);
            return (
              (0, r.useEffect)(() => {
                i && j(R.sounds.cust_tick_on_all());
              }, [i]),
              o().createElement(
                "div",
                { className: v()(Mi, s && xi, n) },
                Boolean(null == e ? void 0 : e.length) &&
                  e.map((e) =>
                    o().createElement(
                      Ii,
                      Oi(
                        { key: e.season, isShowFullTabContent: s, isAllTabsFull: i, onClick: a },
                        e,
                      ),
                    ),
                  ),
              )
            );
          },
          Ri = "VehicleName_base_4d",
          Pi = "VehicleName_vehicleTypeContainer_1e",
          Hi = "VehicleName_base__prem_ec",
          Wi = "VehicleName_vehicleType_68",
          zi = "VehicleName_shortName_23",
          Vi = R.images.gui.maps.icons.vehicleTypes.big,
          Ui = (0, r.memo)(({ name: e, tier: t, type: a, isPremium: n = !1, classMix: u }) => {
            const r = `${((s = a), s.replace(/-/g, "_"))}${n ? "_elite" : ""}`;
            var s;
            return o().createElement(
              o().Fragment,
              null,
              o().createElement(
                "div",
                { className: v()(Ri, n && Hi, u) },
                o().createElement(ua, { text: ju(t) }),
                o().createElement(
                  "div",
                  { className: Pi },
                  o().createElement("div", {
                    className: Wi,
                    style: { backgroundImage: `url(${Vi.$dyn(r)})` },
                  }),
                ),
                o().createElement(ua, { text: e, className: zi }),
              ),
              o().createElement("div", null),
            );
          });
        var Gi = a(5521);
        const ji = (e) => {
            console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
          },
          $i = "INPUT_KEY_STATE";
        var Xi;
        !(function (e) {
          ((e.Idle = "IDLE"), (e.Pressed = "PRESSED"), (e.Released = "RELEASED"));
        })(Xi || (Xi = {}));
        function qi(e) {
          localStorage.setItem($i, JSON.stringify(e));
        }
        function Yi(e = Gi.n.NONE, t = ji, a = !1, n, u = 300) {
          const o = (0, r.useRef)(0);
          (0, r.useEffect)(() => {
            if (e !== Gi.n.NONE)
              return (
                window.addEventListener("keydown", r, { capture: a }),
                window.addEventListener("keyup", s, { capture: a }),
                () => {
                  (window.removeEventListener("keydown", r, { capture: a }),
                    window.removeEventListener("keyup", s, { capture: a }));
                }
              );
            function r(n) {
              if (n.keyCode !== e) return;
              if (n.repeat) return;
              if (i.O.view.isEventHandled()) return;
              i.O.view.setEventHandled();
              (
                (function () {
                  const e = localStorage.getItem($i);
                  return e ? JSON.parse(e) : null;
                })() || { state: Xi.Idle, pressTime: 0 }
              ).state === Xi.Released
                ? (t(n), a && n.stopPropagation(), qi({ state: Xi.Idle, pressTime: 0 }))
                : (qi({ state: Xi.Pressed, pressTime: performance.now() }),
                  (o.current = performance.now()));
            }
            function s(t) {
              if ((localStorage.setItem(wd, "0"), t.keyCode !== e)) return;
              const a = performance.now(),
                r = a - (o.current || a);
              o.current = 0;
              (n && n(r, r >= u, t), qi({ state: Xi.Released, pressTime: 0 }));
            }
          }, [t, e, a, n, u]);
        }
        const Ki = "App_base_f6",
          Zi = "App_base__expanded_2a",
          Ji = "App_wrapper_5c",
          Qi = "App_header_17",
          el = "App_header__hide_c5",
          tl = "App_infoButton_db",
          al = "App_base__fadeIn_54",
          nl = "App_base__fadeOut_33",
          ul = "App_closeButton_7c",
          rl = "App_description_d6",
          ol = "App_description__bonus_a0",
          sl = "App_topPanelWrapper_50",
          il = "App_topPanel_29",
          ll = "App_carouselBlock_24",
          cl = "App_carouselBlockBack_d6",
          _l = "App_markers_2a",
          dl = "App_markers__fadeIn_94",
          ml = "App_markers__fadeOut_e3",
          El = "App_emptyState_2f",
          gl = "App_entryPoint_ac",
          pl = "App_decalsBanner_75",
          bl = "App_decalsBanner__hide_98",
          Al = "App_decalsBanner__fadeIn_92",
          Cl = "App_decalsBanner__fadeOut_38",
          fl = "App_openPanelButton_55",
          hl = "App_openPanelButtonText_6f",
          vl = "App_leftPanel_85",
          Fl = "App_rightPanel_fb",
          Dl = "App_divider_8c",
          Bl = "App_seasontTabs_50",
          Sl = "App_seasontTabs__fadeIn_3a",
          wl = "App_seasontTabs__fadeOut_a6",
          yl = "App_magneticTool_4d",
          kl = "App_inscription_3e",
          Tl = "App_toolbarWrapper_55",
          Nl = "App_progressionWrapper_19",
          Il = "App_withProgressionWrapper_cb",
          Ml = "App_seasonsHint_6d",
          xl = "App_sub_7b",
          Ol = "App_sub__open_1c",
          Ll = "App_footer_b1",
          Rl = "App_footer__hide_ce",
          Pl = "App_binCartPannelWrapper_8c",
          Hl = "App_binCartPannelWrapper__open_3f",
          Wl = "App_binCartPannel_b1",
          zl = "App_cart_25",
          Vl = "App_subInfo_18",
          Ul = "App_subInfo__open_b7",
          Gl = "App_back_ff",
          jl = "App_buttonHolder_58",
          $l = { type: "idle" };
        const Xl = (e, t) => {
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
          ql = "ArrowsHint_base_3c",
          Yl = "ArrowsHint_content_ac",
          Kl = "ArrowsHint_notificationBg_ef",
          Zl = "ArrowsHint_arrows_7c",
          Jl = "ArrowsHint_bg_e0",
          Ql = "ArrowsHint_arrow_41",
          ec = "ArrowsHint_arrow__left_9c",
          tc = "ArrowsHint_arrow__right_50",
          ac = "ArrowsHint_text_a2",
          nc = () =>
            o().createElement(
              "div",
              { className: ql },
              o().createElement("div", { className: Jl }),
              o().createElement(
                "div",
                { className: Yl },
                o().createElement("div", { className: Kl }),
                o().createElement(ua, {
                  className: ac,
                  text: R.strings.customization.arrowHint.text(),
                }),
                o().createElement(
                  "div",
                  { className: Zl },
                  o().createElement("div", { className: v()(Ql, ec) }),
                  o().createElement("div", { className: v()(Ql, tc) }),
                ),
              ),
            ),
          uc = ({
            children: e,
            contentID: t,
            decoratorID: a = 0,
            targetId: n = 0,
            args: u,
            isEnabled: o = !0,
            onMouseDown: s,
          }) => {
            const i = (0, r.useCallback)(() => {
                ((0, da.c9)(da.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: a,
                  targetID: n,
                  isMouseEvent: !0,
                  on: !0,
                  args: u,
                }),
                  $.playYes());
              }, [u, t, a, n]),
              l = (0, r.useCallback)(() => {
                (0, da.c9)(da.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: a,
                  targetID: n,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, a, n]),
              c = (0, r.useCallback)(
                (e) => {
                  (s && s(e), ((e) => e.button === ln.RIGHT)(e) && i());
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
          rc = ["children"];
        function oc() {
          return (
            (oc =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            oc.apply(this, arguments)
          );
        }
        const sc = (e) => {
            let t = e.children,
              a = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  u = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((a = r[n]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, rc);
            return o().createElement(
              uc,
              oc({}, a, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          ic = "Image_base_5c",
          lc = "Image_shine_08",
          cc = "Image_content_03",
          _c = (0, r.memo)(({ isDim: e, icon: t }) => {
            const a = (0, r.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]);
            return t
              ? o().createElement(
                  "span",
                  { className: ic },
                  e && o().createElement("span", { className: lc }),
                  o().createElement("span", { className: cc, style: a }),
                )
              : o().createElement("span", { className: cc });
          }),
          dc = "Price_base_9e",
          mc = "Price_base__stock_cc",
          Ec = "Price_storage_04",
          gc = "Price_storage__empty_2d",
          pc = "Price_icon_df",
          bc = "Price_iconRent_ec",
          Ac = "Price_iconRent__autoRent_df",
          Cc = "Price_rental_5a",
          fc = "Price_iconLocked_07",
          hc = R.strings.customization,
          vc = (0, r.memo)(
            ({
              locked: e,
              hasDiscount: t,
              isRental: a,
              autoRentEnabled: n,
              rentalInfoText: u,
              isStub: r,
              price: s,
              quantity: i,
              isFromStorage: l = !0,
              classMix: c,
            }) => {
              var _, d;
              if (r) return null;
              const m = v()(bc, n && Ac);
              if (e)
                return o().createElement(
                  "span",
                  { className: v()(dc, c) },
                  o().createElement(
                    "span",
                    { className: pc },
                    o().createElement("span", { className: fc }),
                  ),
                );
              if (a && i > 0)
                return o().createElement(
                  "span",
                  { className: v()(dc, c) },
                  o().createElement(
                    "span",
                    { className: pc },
                    o().createElement("span", { className: m }),
                  ),
                  i,
                );
              if (l && (0 === s.length || i > 0))
                return o().createElement(
                  "span",
                  { className: v()(dc, c) },
                  o().createElement("span", { className: v()(Ec, !i && gc) }, i),
                );
              const E = v()(dc, t && mc, c);
              return o().createElement(
                "div",
                { className: E },
                "" !== u && o().createElement(ua, { className: Cc, text: u }),
                Boolean(i && i > 1) &&
                  o().createElement(ua, {
                    text: hc.cart.quantity(),
                    format: { binding: { quantity: i } },
                  }),
                o().createElement(Fn, {
                  isDiscount: t,
                  size: bn.small,
                  type: null == (_ = s[0]) ? void 0 : _.name,
                  value: Number(null == (d = s[0]) ? void 0 : d.value),
                }),
              );
            },
          ),
          Fc = "ProgressionLevelIcon_base_8a",
          Dc = "ProgressionLevelIcon_icon_49",
          Bc = "ProgressionLevelIcon_icon__big_74",
          Sc = "ProgressionLevelIcon_icon__small_46",
          wc = ({ typeId: e, progressionLevel: t, classMix: a }) => {
            const n = `level_${t}`,
              u =
                36 === e
                  ? R.images.gui.maps.icons.customization.progression_icons
                  : R.images.gui.maps.icons.customization.progression_styles.icons,
              s = u.$dyn(n),
              i = u.$dyn(n.concat("_small")),
              l = (0, r.useMemo)(() => ({ backgroundImage: `url(${i})` }), [i]),
              c = (0, r.useMemo)(() => ({ backgroundImage: `url(${s})` }), [s]);
            return s && i
              ? o().createElement(
                  "div",
                  { className: Fc },
                  o().createElement("div", { className: v()(Dc, Sc, a), style: l }),
                  o().createElement("div", { className: v()(Dc, Bc, a), style: c }),
                )
              : null;
          },
          yc = "Slot_base_25",
          kc = "Slot_base__big_e2",
          Tc = "Slot_base__isProgression_0b",
          Nc = "Slot_base__locked_4d",
          Ic = "Slot_base__isAlreadyUsed_dd",
          Mc = "Slot_base__selected_03",
          xc = "Slot_equippedIcon_0d",
          Oc = "Slot_pulse_3a",
          Lc = "Slot_image_c9",
          Rc = "Slot_inProgressIcon_8a",
          Pc = "Slot_progressionArrow_74",
          Hc = "Slot_progressionArrow__enabled_25",
          Wc = "Slot_shadowBottom_96",
          zc = "Slot_base__hasExtraName_55",
          Vc = "Slot_shadowTop_11",
          Uc = "Slot_base__topLeftCornerVisible_f9",
          Gc = "Slot_border_74",
          jc = "Slot_base__equipped_be",
          $c = "Slot_topLeftCorner_b3",
          Xc = "Slot_ribbon_f5",
          qc = "Slot_isLocked_bb",
          Yc = "Slot_isAlreadyUsed_1a",
          Kc = "Slot_isAlreadyUsedText_50",
          Zc = "Slot_isAlreadyUsedIcon_6a",
          Jc = "Slot_icon_fc",
          Qc = "Slot_icon__editable_69",
          e_ = "Slot_icon__rewindable_fd",
          t_ = "Slot_icon__special_50",
          a_ = "Slot_icon__alert_6d",
          n_ = "Slot_icon__unHistorical_64",
          u_ = "Slot_icon__fantastical_3a",
          r_ = "Slot_icon__serialNumber_26",
          o_ = "Slot_hover_7b",
          s_ = "Slot_price_d1",
          i_ = "Slot_styleName_c6",
          l_ = "Slot_button_a6",
          c_ = "Slot_buttonWrapper_ac",
          __ = "Slot_bubble_cc",
          d_ = "Slot_bubble__placeButton_28",
          m_ = R.strings.customization,
          E_ = (0, r.memo)(
            ({
              intCD: e,
              typeId: t,
              locked: a,
              soundHover: n = R.sounds.highlight(),
              soundClick: u = R.sounds.cust_select(),
              isSelected: s,
              customizationDisplayType: i,
              tooltip: l,
              isSpecial: c,
              showAlert: _,
              isDim: d,
              icon: m,
              isWide: E,
              quantity: g,
              buyPrice: p,
              extraName: b,
              classMix: A,
              progressionLevel: C,
              isProgressionRewindEnabled: f,
              editableIcon: h,
              onSelectItem: F,
              isEquipped: D,
              editBtnEnabled: S,
              onEditItem: w,
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
              arrowEnabled: W,
              isNew: z,
              isFilled: V,
            }) => {
              var U;
              const G = (0, r.useMemo)(() => -1 === e, [e]),
                $ = (0, r.useMemo)(() => !a, [a]),
                X = y().mediaSize,
                q = h.includes("disable") ? null : h,
                Y = 1 === i,
                K = 2 === i,
                Z = _ || c || I || i || q,
                J = (0, r.useCallback)(() => {
                  (e && P(e), $ && n && !s && j(n));
                }, [P, e, $, n, s]),
                Q = (0, r.useCallback)(() => {
                  (C <= 0 && (a || x)) || (F && (e && F(e), j(u)));
                }, [e, x, a, F, C, u]),
                ee = (0, r.useCallback)(
                  (t) => {
                    (t.stopPropagation(), w && !a && e && w(e));
                  },
                  [e, a, w],
                ),
                te = v()(
                  yc,
                  A,
                  E && kc,
                  s && Mc,
                  D && jc,
                  C > 0 && Tc,
                  Z && Uc,
                  b && zc,
                  a && Nc,
                  x && Ic,
                ),
                ae = (0, r.useMemo)(
                  () => ({ intCD: e, tooltip: l, showInventoryBlock: !a, progressionLevel: C }),
                  [e, a, C, l],
                ),
                ne = (0, r.useMemo)(
                  () => ({
                    tooltip: Y
                      ? "techCustomizationNonhistoricItem"
                      : "techCustomizationFantasticalItem",
                  }),
                  [Y],
                ),
                ue = Boolean(null == (U = p.discount[0]) ? void 0 : U.value);
              return V
                ? o().createElement(
                    sc,
                    { key: e, isEnabled: !G, args: { type: "customizationItem", intCD: e } },
                    o().createElement(
                      Ca,
                      { args: ae },
                      o().createElement(
                        "div",
                        { className: te, onMouseEnter: J, onClick: Q },
                        z && o().createElement("div", { className: Oc }),
                        D && o().createElement("div", { className: xc }),
                        o().createElement(
                          "div",
                          { className: Gc },
                          void 0 !== W && o().createElement("div", { className: v()(Pc, W && Hc) }),
                          H && o().createElement("div", { className: Rc }),
                          o().createElement(
                            "div",
                            { className: Lc },
                            o().createElement(_c, { isDim: d, icon: m }),
                          ),
                          o().createElement("div", { className: Vc }),
                          o().createElement("div", { className: Wc }),
                          a && o().createElement("div", { className: qc }),
                          x &&
                            o().createElement(
                              "div",
                              { className: Yc },
                              o().createElement(
                                "div",
                                { className: Kc },
                                o().createElement("div", { className: Zc }),
                                E &&
                                  o().createElement(ua, {
                                    text: m_.customization.carousel.is_already_used(),
                                  }),
                              ),
                            ),
                          Boolean(O) &&
                            o().createElement(ua, { className: __, text: O.toString() }),
                          M && o().createElement("div", { className: Xc }),
                          o().createElement(
                            "div",
                            { className: $c },
                            _ && o().createElement("div", { className: v()(Jc, a_) }),
                            c && o().createElement("div", { className: v()(Jc, t_) }),
                            I && o().createElement("div", { className: v()(Jc, r_) }),
                            (Y || K) &&
                              !G &&
                              o().createElement(
                                Ca,
                                { args: ne },
                                o().createElement("div", { className: v()(Jc, Y ? n_ : u_) }),
                              ),
                            q &&
                              o().createElement("div", {
                                className: v()(Jc, Qc),
                                style: {
                                  backgroundImage: `url(${(() => {
                                    if (q) return X <= B.Small ? q : q.replace("small", "big");
                                  })()})`,
                                },
                              }),
                            f
                              ? o().createElement("div", { className: v()(Jc, e_) })
                              : o().createElement(wc, {
                                  typeId: t,
                                  progressionLevel: C,
                                  classMix: Jc,
                                }),
                          ),
                          o().createElement(ua, { className: i_, text: b }),
                          o().createElement(vc, {
                            classMix: s_,
                            isStub: G,
                            price: p.price,
                            quantity: g,
                            isRental: k,
                            rentalInfoText: T,
                            autoRentEnabled: N,
                            locked: a,
                            hasDiscount: ue,
                          }),
                          o().createElement("div", { className: o_ }),
                          Boolean(h) &&
                            D &&
                            o().createElement(
                              Ua,
                              {
                                body: S
                                  ? m_.customization.changeButton.tooltip()
                                  : m_.customization.changeButtonDisabled.tooltip(),
                              },
                              o().createElement(
                                "div",
                                { id: `${e}-tooltip`, className: c_ },
                                o().createElement(
                                  Ha,
                                  {
                                    size: Ra.small,
                                    type: S ? La.primary : La.secondary,
                                    disabled: !S,
                                    mixClass: l_,
                                    onClick: ee,
                                  },
                                  Boolean(L) &&
                                    o().createElement(ua, {
                                      className: v()(__, d_),
                                      text: L.toString(),
                                    }),
                                  X >= B.Small
                                    ? o().createElement(ua, {
                                        text: m_.customization.carousel.change_button(),
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
                    { className: v()(yc, E && kc), onMouseEnter: J, onClick: Q },
                    o().createElement("div", { className: Gc }),
                  );
            },
          ),
          g_ = "Slots_base_ef",
          p_ = "Slots_categories_6b",
          b_ = "Slots_categorieBox_d3",
          A_ = "Slots_categorieText_12",
          C_ = "Slots_categorieBoxPattern_8d",
          f_ = "Slots_slot_17";
        function h_() {
          return (
            (h_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            h_.apply(this, arguments)
          );
        }
        const v_ = (0, r.memo)(
          ({
            items: e,
            arrowsList: t,
            categories: a,
            onClick: n,
            onHoverItem: u,
            onEditClick: r,
            isEditable: s,
            categoriesRef: i,
            itemsRef: l,
          }) =>
            o().createElement(
              "div",
              { className: g_ },
              a.map((c, _) => {
                var d;
                return o().createElement(
                  "div",
                  { className: p_, key: `${_}` },
                  "" !== c.bookmarkName &&
                    o().createElement(
                      "div",
                      {
                        className: b_,
                        ref: (e) => {
                          e ? i.current.set(c.bookmarkIndex, e) : i.current.delete(c.bookmarkIndex);
                        },
                      },
                      o().createElement("div", { className: C_ }),
                      o().createElement("div", { className: A_ }, c.bookmarkName),
                    ),
                  e
                    .slice(c.bookmarkIndex, null == (d = a[_ + 1]) ? void 0 : d.bookmarkIndex)
                    .map((e, a) => {
                      const i = t.find((e) => e.arrowIndex === a);
                      return o().createElement(
                        "div",
                        {
                          key: `${_}_${a}`,
                          ref: (t) => {
                            t ? l.current.set(e.intCD, t) : l.current.delete(e.intCD);
                          },
                          "data-magnetic-tool-support": !0,
                        },
                        o().createElement(
                          E_,
                          h_(
                            {
                              onSelectItem: n,
                              onHoverItem: u,
                              onEditItem: r,
                              classMix: f_,
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
        let F_;
        !(function (e) {
          ((e.auto = "auto"), (e.left = "left"), (e.right = "right"));
        })(F_ || (F_ = {}));
        const D_ = {
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
          B_ = "right",
          S_ = "left",
          w_ = (e) => e.offsetLeft - 0.5 * e.offsetWidth,
          y_ = (e, t) => e.offsetLeft - t + 1.5 * e.offsetWidth,
          k_ = R.strings.customization,
          T_ = { allowedButtons: [ln.LEFT] },
          N_ = (0, r.memo)(
            (0, r.forwardRef)(
              (
                {
                  items: e,
                  arrowsList: t,
                  categories: a,
                  onClick: n,
                  onHoverItem: u,
                  onEditClick: s,
                  scrollApi: l,
                  onArrowClick: c,
                  isCarouselArrowsHintVisible: _,
                  scrollStartItemId: d,
                  selectedItemId: m,
                  firstExpandedItemId: E,
                  tabId: g,
                  lastScrollState: p,
                  isEditable: b,
                  onUpdateItems: A,
                },
                C,
              ) => {
                const f = y().mediaSize,
                  h = (0, r.useRef)(new Map()),
                  F = (0, r.useRef)(new Map()),
                  D = (0, r.useMemo)(() => e.filter((e) => e.isEquipped), [e]),
                  S = (0, r.useState)(0),
                  w = S[0],
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
                  z = H[1],
                  V = (0, r.useState)([]),
                  U = V[0],
                  G = V[1],
                  j = (0, r.useState)(!1),
                  X = j[0],
                  q = j[1],
                  Y = (0, r.useState)([0, 0]),
                  K = Y[0],
                  Z = Y[1];
                (0, r.useImperativeHandle)(C, () => ({
                  getFirstVisibleItemId: () => {
                    const t = e.find((e) => {
                      const t = h.current.get(e.intCD);
                      return t && t.getBoundingClientRect().left > 0;
                    });
                    return t ? t.intCD : -1;
                  },
                }));
                const J = { left: K[0], right: K[1] },
                  Q = J.right <= 0 && J.left <= 0,
                  ee = (function (e, t, a) {
                    const n = e.contentRef,
                      u = e.wrapperRef,
                      o = e.scrollPosition,
                      s = e.clampPosition,
                      l = e.animationScroll,
                      c = e.events,
                      _ = (0, r.useState)($l),
                      d = _[0],
                      m = _[1];
                    return (
                      (0, r.useEffect)(() => {
                        const e = n.current;
                        e && (e.style.cursor = "dragging" === d.type ? "move" : "grab");
                      }, [n, d.type]),
                      (0, r.useEffect)(() => {
                        if ("dragging" !== d.type) return;
                        const e = i.O.client.events.mouse.move(([e, a]) => {
                            const r = n.current,
                              i = u.current;
                            if (!r || !i) return;
                            if ("inside" === a && e.clientX < 0) return;
                            const c = "inside" === a ? e.clientX : e.clientX - i.offsetLeft,
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
                          a = i.O.client.events.mouse.up(function () {
                            m({ type: "scrollingToEnd" });
                          });
                        return () => {
                          (e(), a());
                        };
                      }, [l.scrollPosition, s, n, d, o, u, t]),
                      (0, r.useEffect)(() => {
                        if ("scrollingToEnd" !== d.type) return;
                        const e = () => {
                          m($l);
                        };
                        return (
                          l.scrollPosition.idle && e(),
                          c.on("rest", e),
                          () => c.off("rest", e)
                        );
                      }, [l.scrollPosition, d.type, c]),
                      (0, r.useEffect)(() => {
                        const e = n.current;
                        if (!e) return;
                        const t = (e) => {
                          (a &&
                            a.allowedButtons &&
                            -1 === a.allowedButtons.findIndex((t) => e.button === t)) ||
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
                      }, [l.scrollPosition, n, a]),
                      d
                    );
                  })(l, void 0, T_),
                  te = "dragging" === ee.type,
                  ae = (0, r.useCallback)(() => {
                    const e = l.getWrapperSize();
                    if (!e) return null;
                    let t = !1,
                      a = !1;
                    (D.forEach((n) => {
                      const u = h.current.get(n.intCD);
                      if (!u) return null;
                      const r = u.getBoundingClientRect();
                      (r.right <= 0 && (t = !0), r.left >= e && (a = !0));
                    }),
                      I(t),
                      O(a));
                  }, [D, l]),
                  ne = (e) => {
                    const t = l.getWrapperSize();
                    if (!t) return null;
                    let a = null,
                      n = 1 / 0;
                    if (
                      (D.forEach((u) => {
                        const r = h.current.get(u.intCD);
                        if (!r) return null;
                        const o = r.getBoundingClientRect(),
                          s = o.width / 2;
                        if (e === S_) {
                          if (o.right - s <= 0) {
                            const e = t - o.right;
                            e < n && ((n = e), (a = r));
                          }
                        } else if (o.left + s >= t) {
                          const e = o.left - t;
                          e < n && ((n = e), (a = r));
                        }
                      }),
                      a)
                    ) {
                      const n = a.getBoundingClientRect(),
                        u = e === S_ ? a.offsetLeft - 36 : a.offsetLeft - t + n.width + 29;
                      l.scrollPosition.start({ scrollPosition: J.right < u ? J.right : u });
                    }
                  },
                  ue = (0, r.useCallback)(() => {
                    const e = l.getContainerSize();
                    if (!e) return;
                    const t = a.length > 1 && !Q;
                    if ((t !== X && q(t), !t)) return void (U.length > 0 && G([]));
                    const n = [];
                    (a.forEach((t) => {
                      const a = F.current.get(t.bookmarkIndex);
                      if (a) {
                        let u = (a.offsetLeft + a.offsetWidth / 2) / e;
                        ((u = Math.max(0, Math.min(1, u))),
                          n.push({ name: t.bookmarkName, position: u, index: t.bookmarkIndex }));
                      }
                    }),
                      JSON.stringify(n) !== JSON.stringify(U) && G(n));
                  }, [U, a, Q, l, X]),
                  re = (0, r.useCallback)(
                    (e) => {
                      const t = e.which;
                      (t === Gi.n.ARROW_LEFT && c(!0), t === Gi.n.ARROW_RIGHT && c(!1));
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
                      a = t[0],
                      n = t[1];
                    (a === J.left && n === J.right) || Z([a, n]);
                  }, [l, J.left, J.right]),
                  se = (0, r.useCallback)(
                    (t) => {
                      const a = e[t],
                        n = h.current.get(a.intCD);
                      if (n) return { position: n.offsetLeft, isFilled: a.isFilled };
                    },
                    [e],
                  ),
                  ie = (0, r.useCallback)(() => {
                    const t = l.getWrapperSize();
                    if (t) {
                      const a = l.animationScroll.scrollPosition.goal;
                      A(a, t, e.length, se);
                    }
                  }, [l, e, A, se]),
                  le = (0, r.useCallback)(() => {
                    (oe(), ue(), ae(), ie());
                  }, [ae, oe, ue, ie]);
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
                    (e, t = !0, a = F_.auto) => {
                      const n = l.getBounds(),
                        u = n[0],
                        r = n[1];
                      if (!((u <= 0 && r <= 0) || void 0 === e))
                        if (e > 0) {
                          const n = l.getWrapperSize(),
                            u = h.current.get(e);
                          if (u && n) {
                            const e = l.animationScroll.scrollPosition.goal;
                            let r = 0,
                              o = !0;
                            if (a === F_.left) r = w_(u);
                            else if (a === F_.right) r = y_(u, n);
                            else {
                              const t = u.offsetLeft - e < 0,
                                a = u.offsetLeft + u.offsetWidth - e > n;
                              t || a ? (t ? (r = w_(u)) : a && (r = y_(u, n))) : (o = !1);
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
                Xl(() => {
                  if (de && _e && p.current)
                    return p.current.firstExpandedItemId !== E
                      ? ((p.current.firstExpandedItemId = E), void (E && ce(E, !0, F_.left)))
                      : p.current.selectedItemId !== m
                        ? ((p.current.selectedItemId = m), void (m && ce(m, !1, F_.auto)))
                        : p.current.tabId !== g
                          ? ((p.current.tabId = g), void ce(d, !0, F_.left))
                          : void 0;
                }, [ce, m, E, d, g, _e, de, p]);
                const me = v()(
                    D_.shadow,
                    D_.shadow__left,
                    (w === J.left || Q) && D_.shadow__hidden,
                  ),
                  Ee = v()(D_.shadow, D_.shadow__right, (w === J.right || Q) && D_.shadow__hidden),
                  ge = v()(
                    D_.arrow,
                    D_.arrow__left,
                    R && D_.arrow__hover,
                    (!N || Q) && D_.arrow__hidden,
                  ),
                  pe = v()(
                    D_.arrow,
                    D_.arrow__right,
                    W && D_.arrow__hover,
                    (!x || Q) && D_.arrow__hidden,
                  ),
                  be = () => {
                    $.playHighlight();
                  };
                return o().createElement(
                  "div",
                  { className: v()(D_.base, te && D_.base__dragging) },
                  _ &&
                    o().createElement(
                      "div",
                      { className: D_.arrowsHint },
                      o().createElement(nc, null),
                    ),
                  o().createElement(
                    Oe.Horizontal.Area,
                    {
                      api: l,
                      classNames: {
                        wrapper: v()(
                          D_.horizontalWrapper,
                          Q && D_.horizontalWrapper__withoutScroll,
                        ),
                        content: D_.horizontalContent,
                      },
                    },
                    o().createElement(
                      "div",
                      { className: D_.slots },
                      o().createElement(v_, {
                        items: e,
                        categories: a,
                        arrowsList: t,
                        onClick: n,
                        onHoverItem: u,
                        onEditClick: s,
                        isEditable: b,
                        itemsRef: h,
                        categoriesRef: F,
                      }),
                    ),
                  ),
                  o().createElement(Oe.Horizontal.Bar, {
                    classNames: { base: D_.horizontalBar, thumb: D_.thumb },
                    api: l,
                  }),
                  X &&
                    o().createElement(
                      "div",
                      { className: D_.bookmarksWrapper },
                      U.map(({ name: e, position: t, index: a }) =>
                        o().createElement(
                          Ua,
                          { key: `${e}-${a}`, body: e },
                          o().createElement("div", {
                            onMouseEnter: be,
                            onClick: () =>
                              ((e) => {
                                const t = l.getWrapperSize(),
                                  a = l.getContainerSize();
                                if (!t || !a) return;
                                const n = F.current.get(e);
                                if (n) {
                                  $.playClick();
                                  const e = n.offsetLeft + 0.5 * n.offsetWidth,
                                    u = e / a,
                                    r = f >= B.Medium ? 36 : 29,
                                    o = e - u * (t - 2 * r) - r;
                                  l.scrollPosition.start({ scrollPosition: o });
                                }
                              })(a),
                            className: D_.bookmark,
                            style: { left: 100 * t + "%" },
                          }),
                        ),
                      ),
                    ),
                  o().createElement("div", { className: me }),
                  o().createElement("div", { className: Ee }),
                  o().createElement(
                    Ua,
                    { body: k_.tooltips.carousel.arrow() },
                    o().createElement("div", {
                      className: ge,
                      onMouseEnter: () => {
                        (P(!0), $.playHighlight());
                      },
                      onMouseLeave: () => {
                        P(!1);
                      },
                      onClick: () => {
                        ne(S_);
                      },
                    }),
                  ),
                  o().createElement(
                    Ua,
                    { body: k_.tooltips.carousel.arrow() },
                    o().createElement("div", {
                      className: pe,
                      onMouseEnter: () => {
                        (z(!0), $.playHighlight());
                      },
                      onClick: () => {
                        ne(B_);
                      },
                      onMouseLeave: () => {
                        z(!1);
                      },
                    }),
                  ),
                );
              },
            ),
          ),
          I_ = { type: "idle" };
        const M_ = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function x_(e = Gi.n.NONE, t = M_, a = !1) {
          (0, r.useEffect)(() => {
            if (e !== Gi.n.NONE)
              return (
                window.addEventListener("keydown", n, a),
                () => {
                  window.removeEventListener("keydown", n, a);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), t(n), a && n.stopPropagation());
              }
            }
          }, [t, e, a]);
        }
        const O_ = "WarningText_base_5d",
          L_ = "WarningText_header_57",
          R_ = "WarningText_headerIcon_2f",
          P_ = "WarningText_description_78",
          H_ = o().memo(({ header: e, description: t }) =>
            o().createElement(
              "div",
              { className: O_ },
              o().createElement(
                "div",
                { className: L_ },
                o().createElement("div", { className: R_ }),
                e,
              ),
              o().createElement("div", { className: P_ }, t),
            ),
          ),
          W_ = "ListEmptyState_base_5f",
          z_ = "ListEmptyState_content_22",
          V_ = "ListEmptyState_buttonWrapper_fa",
          U_ = "ListEmptyState_button_cd",
          G_ = R.strings.customization,
          j_ = (0, r.memo)(
            ({
              warningHeader: e,
              warningDescription: t,
              buttonType: a = La.secondary,
              tooltipArgs: n = { body: G_.customization.resetFilter.tooltip.text() },
              className: u,
              onClick: r,
              children: s,
            }) =>
              o().createElement(
                "div",
                { className: v()(W_, u) },
                o().createElement(
                  "div",
                  { className: z_ },
                  o().createElement(H_, { header: e, description: t }),
                  s &&
                    o().createElement(
                      "div",
                      { className: V_ },
                      o().createElement(
                        Ua,
                        n,
                        o().createElement(
                          Ha,
                          { size: Ra.small, type: a, onClick: r, mixClass: U_ },
                          s,
                        ),
                      ),
                    ),
                ),
              ),
          ),
          $_ = {
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
        function X_() {
          return (
            (X_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            X_.apply(this, arguments)
          );
        }
        const q_ = R.strings.customization,
          Y_ = (0, Le.Pi)(
            ({ onCarouselCollapse: e, startScrollItemId: t, tabId: a, onUpdateItems: n }) => {
              const u = mr(),
                s = u.controls,
                l = u.model,
                c = l.computes.getItems(),
                _ = l.computes.getCategories(),
                d = l.computes.getBillModel(),
                m = y().mediaSize <= B.Small ? Ra.small : Ra.medium,
                E = l.computes.getTabsItemsList(),
                g = l.root.get(),
                p = g.filterModel,
                b = g.carouselModel,
                A = Oe.Vertical.useVerticalScrollApi(),
                C = A.getWrapperSize(),
                f = A.getContainerSize(),
                h = l.computes.getBuyPrice(),
                F = (0, r.useRef)(new Map()),
                D = (0, r.useRef)(new Map()),
                S = (0, r.useState)(0),
                w = S[0],
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
                W = p.filteredItemsCounter,
                z = p.allItemsCounter,
                V = p.isFilteringActive,
                U = p.newHiddenItemsCounter,
                G = { top: P[0], bottom: P[1] },
                X = G.top <= 0 && G.bottom <= 0,
                q = Object.fromEntries(Object.entries(d).filter(([e]) => "buyPrice" !== e)),
                Y = (0, r.useCallback)(
                  () =>
                    c.find((e) => {
                      const t = F.current.get(e.intCD);
                      return t && t.offsetTop - w > 0;
                    }),
                  [c, w],
                ),
                K = (0, r.useCallback)(() => {
                  var t;
                  e(null == (t = Y()) ? void 0 : t.intCD);
                }, [Y, e]);
              !(function ({
                key: e = Gi.n.ESCAPE,
                callback: t = () => i.O.view.sendEvent.close(),
                preventPropagation: a = !0,
              } = {}) {
                x_(e, t, a);
              })({ callback: K });
              const Z = () => {
                  $.playHighlight();
                },
                J = (0, r.useCallback)(
                  (t) => {
                    (t && s.onSelectItem(t), e());
                  },
                  [e, s],
                ),
                Q = (0, r.useCallback)(
                  (t) => {
                    (t && s.onEditItem(t), e());
                  },
                  [s, e],
                ),
                ee = (0, r.useCallback)(() => {
                  (s.onShowBuyWindow(), e());
                }, [s, e]),
                te = (function (e, t) {
                  const a = e.contentRef,
                    n = e.wrapperRef,
                    u = e.scrollPosition,
                    o = e.clampPosition,
                    s = e.animationScroll,
                    l = e.events,
                    c = (0, r.useState)(I_),
                    _ = c[0],
                    d = c[1];
                  return (
                    (0, r.useEffect)(() => {
                      const e = a.current;
                      e && (e.style.cursor = "dragging" === _.type ? "grabbing" : "grab");
                    }, [a, _.type]),
                    (0, r.useEffect)(() => {
                      if ("dragging" !== _.type) return;
                      const e = i.O.client.events.mouse.move(([e, r]) => {
                          const i = a.current,
                            l = n.current;
                          if (!i || !l) return;
                          if ("inside" === r && e.clientY < 0) return;
                          const c = "inside" === r ? e.clientY : e.clientY - l.offsetTop,
                            d = _.positionFrom - c,
                            m = _.previousScrollPosition + d;
                          u.start(
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
                    }, [s.scrollPosition, o, a, _, u, n, t]),
                    (0, r.useEffect)(() => {
                      if ("scrollingToEnd" !== _.type) return;
                      const e = () => {
                        d(I_);
                      };
                      return (
                        s.scrollPosition.idle && e(),
                        l.on("rest", e),
                        () => l.off("rest", e)
                      );
                    }, [s.scrollPosition, _.type, l]),
                    (0, r.useEffect)(() => {
                      const e = a.current;
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
                    }, [s.scrollPosition, a]),
                    _
                  );
                })(A),
                ae = "dragging" === te.type,
                ne = (0, r.useCallback)(() => {
                  const e = A.getContainerSize();
                  if (!e) return;
                  const t = _.length > 1 && !X;
                  if ((t !== x && O(t), !t)) return void (N.length > 0 && I([]));
                  const a = [];
                  (_.forEach((t) => {
                    const n = D.current.get(t.bookmarkIndex);
                    if (n) {
                      let u = (n.offsetTop + n.offsetHeight / 2) / e;
                      ((u = Math.max(0, Math.min(1, u))),
                        a.push({ name: t.bookmarkName, position: u, index: t.bookmarkIndex }));
                    }
                  }),
                    JSON.stringify(a) !== JSON.stringify(N) && I(a));
                }, [N, _, X, A, x]),
                ue = (0, r.useCallback)(() => {
                  const e = A.animationScroll.scrollPosition.goal;
                  k(e);
                  const t = A.getBounds(),
                    a = t[0],
                    n = t[1];
                  (a === G.top && n === G.bottom) || H([a, n]);
                }, [A, G.top, G.bottom]),
                re = (0, r.useCallback)(
                  (e) => {
                    const t = c[e],
                      a = F.current.get(t.intCD);
                    if (a) return { position: a.offsetTop, isFilled: t.isFilled };
                  },
                  [c],
                ),
                oe = (0, r.useCallback)(() => {
                  const e = A.getWrapperSize();
                  if (e) {
                    const t = A.animationScroll.scrollPosition.goal;
                    n(t, e, c.length, re);
                  }
                }, [A, c, n, re]),
                se = (0, r.useCallback)(() => {
                  (ue(), ne(), oe());
                }, [ue, ne, oe]);
              (0, r.useEffect)(
                () => (
                  A.events.on("change", se),
                  A.events.on("recalculateContent", se),
                  A.events.on("resizeHandled", se),
                  () => {
                    (A.events.off("change", se),
                      A.events.off("recalculateContent", se),
                      A.events.off("resizeHandled", se));
                  }
                ),
                [se, ue, A.events],
              );
              const ie = (0, r.useState)(t),
                le = ie[0],
                ce = ie[1];
              (Xl(() => {
                if (le > -1 && C && f && !X) {
                  const e = F.current.get(le);
                  if (e) {
                    const t = e.offsetTop - 0.5 * e.offsetHeight;
                    (A.applyScroll(t, { immediate: !0, reset: !0 }), ce(-1));
                  }
                }
              }, [t, C, f, X, A]),
                Xl(() => {
                  A.applyScroll(0, { immediate: !0, reset: !0 });
                }, [a, A]));
              const _e = v()($_.lip, (w === G.bottom || X) && $_.lip__hidden);
              return o().createElement(
                "div",
                { className: v()($_.base, ae && $_.base__dragging) },
                o().createElement("div", { className: $_.baseBack }),
                o().createElement(Wo, {
                  tabs: E,
                  onClick: (e) => {
                    (j(R.sounds.cust_tab_switch()), s.selectTab(e));
                  },
                  onHoverTab: s.hoverTab,
                  mixClass: $_.tabs,
                }),
                o().createElement(
                  "div",
                  { className: $_.filterHeader },
                  o().createElement(
                    "div",
                    { className: $_.filterCounter },
                    o().createElement(_r, {
                      title:
                        V &&
                        o().createElement(
                          Ua,
                          { body: q_.customization.resetFilter.tooltip.text() },
                          o().createElement(
                            Ha,
                            {
                              type: La.ghost,
                              onClick: s.clearFilter,
                              mixClass: v()($_.filtersClearButton),
                            },
                            o().createElement("div", { className: $_.filtersClearIcon }),
                          ),
                        ),
                      label: o().createElement(ua, {
                        text: q_.filters.selectedTitle(),
                        className: $_.filterNumbersLabel,
                      }),
                      from: W,
                      to: z,
                      isFilterRange: !0,
                      isGlowVisible: V,
                      isSelectMode: !1,
                      className: $_.filterNumbers,
                      classNames: { counterGlow: $_.counterGlow },
                      isHideTotalCounter: !V,
                      isSelectedLimitReached: U > 0,
                      isAnimationEnabled: U > 0,
                    }),
                  ),
                  o().createElement(
                    "div",
                    { className: $_.filter },
                    o().createElement(vr, { isReverse: !0, buttonSize: m }),
                  ),
                ),
                o().createElement(
                  "div",
                  { className: $_.carouselWrapper },
                  c.length > 0
                    ? o().createElement(
                        o().Fragment,
                        null,
                        o().createElement(
                          Oe.Vertical.Area,
                          {
                            api: A,
                            className: v()($_.scrollArea, X && $_.scrollArea__withoutScroll),
                            classNames: {
                              content: v()($_.scrollContent, X && $_.scrollContent__withoutScroll),
                            },
                          },
                          _.map((e, t) => {
                            var a;
                            const n = b.isProgressionDecalsBannerVisible && e.isProgressive;
                            return o().createElement(
                              "div",
                              { className: $_.categories, key: `${t}` },
                              "" !== e.bookmarkName &&
                                o().createElement(
                                  "div",
                                  {
                                    className: $_.category,
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
                                { className: $_.slots },
                                n &&
                                  o().createElement(yi, {
                                    mixClass: $_.slot,
                                    onClick: s.clickDecalsBanner,
                                  }),
                                c
                                  .slice(
                                    e.bookmarkIndex,
                                    null == (a = _[t + 1]) ? void 0 : a.bookmarkIndex,
                                  )
                                  .map((e, a) =>
                                    o().createElement(
                                      "div",
                                      {
                                        key: `${t}_${a}`,
                                        ref: (t) => {
                                          t ? F.current.set(e.intCD, t) : F.current.delete(e.intCD);
                                        },
                                      },
                                      o().createElement(
                                        E_,
                                        X_(
                                          {
                                            onSelectItem: J,
                                            onEditItem: Q,
                                            onHoverItem: s.hoverItem,
                                            classMix: $_.slot,
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
                          { className: $_.scrollbarWrapper },
                          x &&
                            o().createElement(
                              "div",
                              { className: $_.bookmarksWrapper },
                              N.map(({ name: e, position: t, index: a }) =>
                                o().createElement(
                                  Ua,
                                  { key: `${e}-${a}`, body: e },
                                  o().createElement("div", {
                                    onMouseEnter: Z,
                                    onClick: () =>
                                      ((e) => {
                                        const t = A.getWrapperSize(),
                                          a = A.getContainerSize();
                                        if (!t || !a) return;
                                        const n = D.current.get(e);
                                        if (n) {
                                          $.playClick();
                                          const e = n.offsetTop + n.offsetHeight / 2,
                                            u = e - (e / a) * (t - 34) - 17;
                                          A.scrollPosition.start({ scrollPosition: u });
                                        }
                                      })(a),
                                    className: $_.bookmark,
                                    style: { top: 100 * t + "%" },
                                  }),
                                ),
                              ),
                            ),
                          o().createElement(Oe.Vertical.Bar, {
                            classNames: { thumb: $_.thumb },
                            api: A,
                          }),
                        ),
                      )
                    : o().createElement(
                        j_,
                        {
                          warningHeader: q_.customization.message.header(),
                          warningDescription: q_.customization.message.description(),
                          buttonType: La.secondary,
                          onClick: s.clearFilter,
                          className: $_.emptyState,
                        },
                        o().createElement(ua, { text: q_.customization.resetFiltersBtn.label() }),
                      ),
                ),
                o().createElement(sn, {
                  id: R.views.lobby.customization.CustomizationMoneyBalance("resId"),
                  mixClass: $_.currency,
                }),
                o().createElement(
                  "div",
                  { className: $_.closeButton },
                  o().createElement(ze, {
                    side: "right",
                    type: "close",
                    caption: q_.customization.closeButton(),
                    onClick: K,
                  }),
                ),
                o().createElement(
                  "div",
                  { className: $_.priceWrapper },
                  o().createElement("div", { className: _e }),
                  o().createElement(
                    "div",
                    { className: $_.price },
                    h &&
                      o().createElement(tu, {
                        price: h,
                        onResetHandler: s.onClearBasket,
                        onBackHandler: s.onCancelChanges,
                        cartParams: q,
                        onApplyHandler: ee,
                        buttonSize: m,
                      }),
                  ),
                ),
              );
            },
          );
        let K_;
        !(function (e) {
          ((e[(e.UnselectedEmpty = 0)] = "UnselectedEmpty"),
            (e[(e.SelectedEmpty = 1)] = "SelectedEmpty"),
            (e[(e.UnselectedFilled = 2)] = "UnselectedFilled"),
            (e[(e.SelectedFilled = 3)] = "SelectedFilled"),
            (e[(e.Preview = 4)] = "Preview"),
            (e[(e.Locked = 5)] = "Locked"),
            (e[(e.Removed = 6)] = "Removed"),
            (e[(e.Edit = 7)] = "Edit"));
        })(K_ || (K_ = {}));
        const Z_ = "ArrowMarker_base_a2",
          J_ = "ArrowMarker_base__scaled_c5",
          Q_ = "ArrowMarker_content_b3",
          ed = "ArrowMarker_arrow_93",
          td = "ArrowMarker_arrow__left_88",
          ad = "ArrowMarker_arrow__right_6b",
          nd = "ArrowMarker_arrow__leftPressed_e7",
          ud = "ArrowMarker_arrow__rightPressed_7b",
          rd = "ArrowMarker_arrow__leftDisabled_7d",
          od = "ArrowMarker_arrow__rightDisabled_11",
          sd = "ArrowMarker_arrowHover_48",
          id = "ArrowMarker_arrowHover__left_36",
          ld = "ArrowMarker_arrowHover__right_a5",
          cd = "ArrowMarker_arrowHitArea_66",
          _d = "ArrowMarker_arrowHitArea__left_a8",
          dd = "ArrowMarker_arrowHitArea__right_e5";
        function md() {
          return (
            (md =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            md.apply(this, arguments)
          );
        }
        let Ed;
        !(function (e) {
          ((e.left = "left"), (e.right = "right"));
        })(Ed || (Ed = {}));
        const gd = (0, Le.Pi)(() => {
            const e = mr(),
              t = e.model,
              a = e.controls,
              n = t.carouselModel.get(),
              u = n.isRightAvailable,
              s = n.isLeftAvailable,
              i = (0, r.useState)({ left: !1, right: !1 }),
              l = i[0],
              c = i[1],
              _ = (0, r.useState)({ left: !1, right: !1 }),
              d = _[0],
              m = _[1],
              E = nr(),
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
                    (j(R.sounds.cust_select()), a.onPressSelectNextItem(e === Ed.left));
                  })(e),
              });
            return o().createElement(
              "div",
              { className: v()(Z_, E > 1 && J_) },
              o().createElement(
                "div",
                { className: Q_ },
                o().createElement("div", { className: v()(ed, td, d.left && nd, !s && rd) }),
                o().createElement("div", { className: v()(ed, ad, d.right && ud, !u && od) }),
                o().createElement("div", { className: v()(sd, l.left && !d.left && s && id) }),
                o().createElement("div", { className: v()(sd, l.right && !d.right && u && ld) }),
                o().createElement("div", md({ className: v()(cd, _d) }, g(Ed.left))),
                o().createElement("div", md({ className: v()(cd, dd) }, g(Ed.right))),
              ),
            );
          }),
          pd = {
            base: "EditMarker_base_77",
            underline: "EditMarker_underline_58",
            underline__1: "EditMarker_underline__1_bf",
            underline__2: "EditMarker_underline__2_a8",
            underline__3: "EditMarker_underline__3_7f",
            underline__errorAnimation: "EditMarker_underline__errorAnimation_ea",
            shake: "EditMarker_shake_85",
          },
          bd = (0, Le.Pi)(() => {
            const e = mr(),
              t = e.model,
              a = e.controls,
              n = t.computes.getEditData(),
              u = (0, r.useCallback)(
                (e) => {
                  const t = e.which;
                  if ((t === Gi.n.ENTER && a.onEnterInput(), t >= Gi.n.KEY_0 && t <= Gi.n.KEY_9)) {
                    const e = t - Gi.n.KEY_1 + 1;
                    a.onAddChar(String(e));
                  } else if (t >= Gi.n.NUMPAD_0 && t <= Gi.n.NUMPAD_9) {
                    const e = t - Gi.n.NUMPAD_0;
                    a.onAddChar(String(e));
                  } else
                    (t === Gi.n.DELETE && a.onDeleteAllChars(),
                      t === Gi.n.BACKSPACE && a.onRemoveChar());
                },
                [a],
              );
            (0, r.useEffect)(
              () => (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              ),
              [u],
            );
            const s = n.inscriptionState === ti.NotAvailableEnter;
            return o().createElement(
              "div",
              { className: pd.base },
              o().createElement("div", {
                key: s ? n.startTimestamp : "",
                className: v()(
                  pd.underline,
                  pd[`underline__${n.editDigitsCount}`],
                  s && pd.underline__errorAnimation,
                ),
              }),
            );
          }),
          Ad = {
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
        let Cd;
        !(function (e) {
          ((e.EMBLEM = "Emblem"),
            (e.INSCRIPTION = "Inscription"),
            (e.PROJECTION_DECAL = "ProjectionDecal"));
        })(Cd || (Cd = {}));
        const fd = [Cd.EMBLEM, Cd.PROJECTION_DECAL, Cd.INSCRIPTION],
          hd = (0, r.memo)(
            ({
              isHovered: e,
              index: t,
              isActiveInscription: a,
              onMarkerClick: n,
              onMarkerHover: u,
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
                p = g[0],
                b = g[1],
                A = fd.includes(l);
              (0, r.useEffect)(() => {
                ((E.current === K_.Preview && i === K_.UnselectedFilled) ||
                (E.current === K_.Locked && i === K_.UnselectedEmpty)
                  ? b(!0)
                  : b(!1),
                  (E.current = i));
              }, [i]);
              return o().createElement(
                "div",
                { className: Ad.markerItem },
                o().createElement(
                  "div",
                  {
                    className: v()(Ad.base, Ad[`base__state${i}`], e && Ad.base__hovered),
                    onClick: () => {
                      (i === K_.UnselectedFilled && j(R.sounds.cust_select()),
                        i === K_.Removed && j(R.sounds.cust_select_remove()),
                        i === K_.Locked ? (j(R.sounds.cust_negative()), n(t)) : n(t));
                    },
                    onMouseEnter: () => {
                      ($.playHighlight(), u(t, !0));
                    },
                    onMouseLeave: () => {
                      (u(t, !1), d && s(t));
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
                  i !== K_.Edit &&
                    o().createElement(
                      "div",
                      { className: Ad.defaultMarker },
                      o().createElement("div", {
                        className: v()(
                          Ad.defaultMarkerIcon,
                          Ad[`defaultMarkerIcon__${l}`],
                          p && Ad.defaultMarkerIcon__withAnimation,
                        ),
                        onAnimationEndCapture: () => {
                          b(!1);
                        },
                      }),
                    ),
                  i === K_.Edit &&
                    o().createElement(
                      "div",
                      { className: Ad.editMarkerWrapper },
                      o().createElement(bd, null),
                    ),
                  i === K_.SelectedFilled &&
                    A &&
                    o().createElement(
                      "div",
                      { className: Ad.arrowMarkerWrapper },
                      o().createElement(gd, null),
                    ),
                  o().createElement("div", { className: Ad.interactive }),
                ),
                a &&
                  i === K_.Locked &&
                  o().createElement(
                    "div",
                    { className: Ad.inscription },
                    o().createElement(ua, {
                      className: Ad.inscriptionText,
                      text: R.strings.vehicle_customization.notification.slotIsFilled.title(),
                    }),
                  ),
              );
            },
          ),
          vd = "MarkersList_markerWrapper_90",
          Fd = (0, Le.Pi)(({ isSceneDraggingChange: e }) => {
            const t = mr(),
              a = t.model,
              n = t.controls,
              u = a.customizationTypes.get(),
              s = (0, r.useState)(0),
              i = s[0],
              l = s[1],
              c = (0, r.useState)([]),
              _ = c[0],
              d = c[1],
              m = (0, r.useState)([]),
              E = m[0],
              g = m[1],
              p = (0, r.useState)([]),
              b = p[0],
              A = p[1],
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
              S = D[1],
              w = (0, r.useRef)([]),
              y = (0, r.useRef)([]),
              k = (0, r.useState)([]),
              T = k[0],
              N = k[1];
            ((0, r.useEffect)(() => {
              if (e)
                return Fr(() => {
                  C.current = e;
                }, 300);
              C.current = e;
            }, [e]),
              ((e) => {
                const t = (0, r.useRef)(0),
                  a = (0, r.useRef)(0),
                  n = (0, r.useRef)(0),
                  u = (0, r.useRef)(0),
                  o = (r) => {
                    if (a.current) {
                      const t = r - a.current;
                      ((n.current += t), (u.current = u.current + t), (u.current = 0), e());
                    }
                    ((a.current = r), (t.current = requestAnimationFrame(o)));
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
                const e = a.computes.getMarkersList().filter((e) => 0 !== e.slotType);
                (e.length !== F.current &&
                  ((h.current = Array(e.length).fill("0")),
                  A(Array(e.length).fill(0)),
                  (v.current = Array(e.length).fill(!1)),
                  g(Array(e.length).fill(!1)),
                  (f.current = Array(e.length).fill(0)),
                  d(Array(e.length).fill(0)),
                  (F.current = e.length),
                  l(e.length)),
                  e.forEach((t, a) => {
                    const n = w.current[a];
                    if (!n) return;
                    const r = `${t.posx.toFixed(1)}rem`,
                      o = `${t.posy.toFixed(1)}rem`,
                      s = `${t.opacity.toFixed(2)}`,
                      i = `${t.scale.toFixed(2)}`,
                      l = `${t.areaId}`,
                      c = `${t.zIndex}`,
                      _ = Object.keys(u).find((e) => u[e] === t.slotType);
                    if (void 0 === _) throw Error(`invalid slotType ${t.slotType} of ${t.state}`);
                    const m = `${t.regionIdx}`,
                      E = t.state,
                      p = t.isHovered,
                      b = y.current[a] || { lastOpacityUpdate: 0 },
                      C = "flex" === n.style.display;
                    t.isVisible
                      ? ((n.style.display = "flex"),
                        (b.opacity === s && C) ||
                          ((n.style.opacity = "1"),
                          N((e) => {
                            var t;
                            return (
                              e[a] && null != (t = Object.keys(e[a])) && t.length
                                ? (e[a] = Object.assign({}, e[a], { opacity: s }))
                                : (e[a] = { opacity: s }),
                              e
                            );
                          })),
                        (b.x === r && C) || n.style.setProperty("--x", r),
                        (b.y === o && C) || n.style.setProperty("--y", o),
                        (b.zIndex === c && C) || n.style.setProperty("--zIndex", c),
                        (b.scale === i && C) ||
                          (n.style.setProperty("--scale", "1"),
                          N(
                            (e) => (
                              e[a] && Object.keys(e[a]).length
                                ? (e[a] = Object.assign({}, e[a], { scale: i }))
                                : (e[a] = { scale: i }),
                              e
                            ),
                          )),
                        (n.getAttribute("areaId") === l && e.length === F.current && C) ||
                          n.setAttribute("areaId", l),
                        (n.getAttribute("slotType") === _ && e.length === F.current && C) ||
                          n.setAttribute("slotType", _),
                        (n.getAttribute("regionIdx") === m && e.length === F.current && C) ||
                          n.setAttribute("regionIdx", m),
                        (y.current[a] = {
                          x: r,
                          y: o,
                          opacity: s,
                          scale: i,
                          lastOpacityUpdate: b.lastOpacityUpdate || 0,
                          lastScaleUpdate: b.lastScaleUpdate || 0,
                          areaId: l,
                          slotType: _,
                          regionIdx: m,
                          state: E,
                          zIndex: c,
                        }),
                        f.current[a] !== E &&
                          d((e) => {
                            const t = [...e];
                            return ((t[a] = E), t);
                          }),
                        h.current[a] !== _ &&
                          A((e) => {
                            const t = [...e];
                            return ((t[a] = _), t);
                          }),
                        v.current[a] !== p &&
                          g((e) => {
                            const t = [...e];
                            return ((t[a] = p), t);
                          }),
                        (f.current[a] = E),
                        (h.current[a] = _),
                        (v.current[a] = p))
                      : (n.style.display = "none");
                  }));
              }));
            const I = (0, r.useRef)(null),
              M = (0, r.useCallback)(
                (e) => {
                  I.current && clearTimeout(I.current);
                  const t = w.current[e];
                  if (!t) return;
                  if (f.current[e] === K_.Locked)
                    (S(null),
                      S(e),
                      (I.current = setTimeout(() => {
                        S((t) => (t === e ? null : t));
                      }, 2300)));
                  else {
                    const e = Number(t.getAttribute("areaId")),
                      a = t.getAttribute("slotType"),
                      r = Number(t.getAttribute("regionIdx"));
                    u[a] && n.selectAnchor(e, u[a], r);
                  }
                },
                [n, u],
              ),
              x = (0, r.useCallback)(
                (e, t) => {
                  if (w.current.length > e && e >= 0) {
                    const a = w.current[e],
                      r = Number(a.getAttribute("areaId")),
                      o = a.getAttribute("slotType"),
                      s = Number(a.getAttribute("regionIdx"));
                    u[o] && n.hoverAnchor(r, u[o], s, t);
                  }
                },
                [n, u],
              ),
              O = (0, r.useCallback)(
                (e) => {
                  if (w.current.length > e && e >= 0) {
                    const t = w.current[e],
                      a = Number(t.getAttribute("areaId")),
                      r = t.getAttribute("slotType"),
                      o = Number(t.getAttribute("regionIdx"));
                    u[r] && n.dragAnchor(a, u[r], o);
                  }
                },
                [n, u],
              );
            return o().createElement(
              o().Fragment,
              null,
              Array.from({ length: i }).map((e, t) =>
                o().createElement(
                  "div",
                  { key: t, className: vd, ref: (e) => (w.current[t] = e) },
                  o().createElement(hd, {
                    index: t,
                    isActiveInscription: B === t,
                    onMarkerClick: () => M(t),
                    onMarkerHover: x,
                    onMarkerDragOut: O,
                    state: _[t],
                    isHovered: E[t],
                    slotType: b[t],
                    scale: T[t],
                  }),
                ),
              ),
            );
          });
        function Dd() {
          return (
            (Dd =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Dd.apply(this, arguments)
          );
        }
        let Bd;
        !(function (e) {
          ((e.CAMOUFLAGE = "camouflage"),
            (e.PROJECTION_DECAL = "projectionDecal"),
            (e.INSCRIPTION = "inscription"));
        })(Bd || (Bd = {}));
        const Sd = "mainview:close",
          wd = "close_dialog",
          yd = [Bd.CAMOUFLAGE, Bd.PROJECTION_DECAL],
          kd = R.strings.customization,
          Td = R.strings.customization.tooltips.filters;
        viewEnv.clearInternalCacheAfterFinalize();
        (0, Le.Pi)(() => {
          var e, t;
          const a = mr(),
            n = a.controls,
            u = a.model,
            s = y().mediaSize,
            l = u.root.get(),
            c = l.isBuyViewActive,
            _ = l.isStyleInfoViewActive,
            d = l.isEditable,
            m = l.isApplyToAllSeasonsAvailable,
            E = l.isApplyToAllSeasonsSelected,
            g = l.isShowProgressionInfoButton,
            p = l.isHoverVehicleSlot,
            b = l.isProgressiveItemsViewVisible,
            A = l.isFilterPopoverOpened,
            C = l.isOnboardingViewOpened,
            f = l.isCustomizationResourceEntryPointAvailable,
            h = (0, r.useRef)(null),
            F = u.computes.getStageSwitcher(),
            D = u.computes.getSelectedTabItemType(),
            S = F.isVisible,
            w = F.selectedLevel,
            k = F.numberOfBullets,
            T = F.isBulletsBeforeCurrentDisabled,
            N = F.currentLevel,
            I = u.toolbarModel.get(),
            M = I.isToolbarPanelEnabled,
            x = I.isInscriptionPanelEnabled,
            O = u.carouselModel.get(),
            L = O.scrollStartItemId,
            P = O.isCarouselArrowsHintVisible,
            H = u.computes.getSelectedItemId(),
            W = (0, r.useState)(-1),
            z = W[0],
            V = W[1],
            U = (0, r.useRef)({
              tabId: void 0,
              scrollStartItemId: void 0,
              selectedItemId: void 0,
              firstExpandedItemId: void 0,
            }),
            G = (0, r.useState)(!1),
            $ = G[0],
            X = G[1],
            q = (0, r.useState)(!1),
            K = q[0],
            Z = q[1],
            J = (0, r.useState)(!1),
            Q = J[0],
            te = J[1],
            ae = (0, r.useState)(!1),
            ne = ae[0],
            ue = ae[1],
            re = u.computes.getBuyPrice(),
            oe = u.computes.getItems(),
            se = u.computes.getCategories(),
            ie = u.computes.getArrowsList(),
            le = u.computes.getTabsItemsList(),
            ce = u.computes.getBillModel(),
            _e = u.computes.getSeasonsTabsItemsList(),
            de = u.computes.getToolbarButtonsList(),
            me = u.magneticToolModel.get(),
            Ee = u.headerVehicleInfo.get(),
            ge = Ee.description,
            pe = Ee.isStyleBonusPreviewText,
            be = Ee.vehicle,
            Ae = s <= B.Small ? Ra.small : Ra.medium,
            Ce = nn(),
            fe = M && !x && !$ && !c && !_,
            he = en(fe),
            ve = en(me.isEnabled),
            Fe = u.computes.getEditData(),
            De = !$ && !fe && !Fe.inscriptionState;
          localStorage.removeItem(wd);
          const Be = (0, r.useCallback)(
              (e) => {
                (V(e || -1), n.onExpandCarousel(!1), X(!1));
              },
              [n],
            ),
            Se = (0, r.useCallback)(
              (e, t) => {
                (n.onToolbarItemClick(e, t),
                  e === Ga.CUSTOMIZATION_SHEET_ACTION_CLOSE && n.onSceneOverChange(!0));
              },
              [n],
            ),
            we = (0, r.useCallback)(() => {
              const e = localStorage.getItem(wd);
              engine.trigger(Sd);
              const t =
                u.computes
                  .getMarkersList()
                  .filter((e) => "1" === e.state.toString() || "3" === e.state.toString()).length >
                0;
              if (!$) {
                if (fe)
                  return (
                    n.onToolbarItemClick(Ga.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1),
                    Se(Ga.CUSTOMIZATION_SHEET_ACTION_CLOSE, 0),
                    void n.onUnselectItem()
                  );
                if (
                  u.computes.getToolbarData().isInscriptionPanelEnabled &&
                  2 !== u.computes.getEditData().inscriptionState &&
                  1 !== u.computes.getEditData().inscriptionState
                )
                  n.onSceneClick();
                else if (
                  (!d &&
                    0 === u.computes.getEditData().inscriptionState &&
                    !u.computes.getToolbarData().isToolbarPanelEnabled) ||
                  ((2 === u.computes.getEditData().inscriptionState ||
                    1 === u.computes.getEditData().inscriptionState) &&
                    n.onCancelChanges(),
                  n.closeEditItem(),
                  c)
                )
                  if (me.isEnabled) n.onUnselectItem();
                  else {
                    if (!t)
                      return (
                        c
                          ? n.closeBinEsc()
                          : _
                            ? n.onCloseStyleInfoEsc()
                            : ((e && "0" !== e) || n.onClose(), localStorage.setItem(wd, "1")),
                        () => {
                          (engine.off(Sd), localStorage.setItem(wd, "0"));
                        }
                      );
                    n.onSceneClick();
                  }
              }
            }, [n, c, $, d, fe, _, me.isEnabled, u.computes, Se]);
          (0, r.useEffect)(() => {
            b && viewEnv.clearInternalCaches();
          }, [b]);
          const ye = Y(
            (e, t, a, n) => {
              if (t) {
                var u;
                let r = 0,
                  o = a,
                  s = !1,
                  i = 0;
                for (; i < a;) {
                  const a = n(i);
                  if (a) {
                    const n = a.position - e < 0,
                      u = a.position - e > t;
                    if ((n && i > r ? (r = i) : s || (s = !a.isFilled), u)) {
                      o = i;
                      break;
                    }
                  }
                  i++;
                }
                s || (s = !(null != (u = n(r)) && u.isFilled));
                let l = r,
                  c = 0;
                for (; c < 5 && l > 0;) (l--, c++);
                ((r = l), s && ke(r, o));
              }
            },
            [(ke = n.onRequestItems)],
            200,
          );
          var ke;
          !(function ({
            key: e = Gi.n.ESCAPE,
            callback: t = () => i.O.view.sendEvent.close(),
            preventPropagation: a = !0,
          } = {}) {
            Yi(e, t, a);
          })({ callback: we, preventPropagation: !1 });
          const Te = ee(),
            Ne = Y(
              () => {
                c ? n.buyItems() : n.onShowBuyWindow();
              },
              [c],
              300,
            ),
            Ie = (0, r.useCallback)(
              (e) => {
                n.selectSeason(e);
              },
              [n],
            ),
            Me = (0, r.useCallback)(
              (e) => {
                e && n.onSelectItem(e);
              },
              [n],
            ),
            xe = (0, r.useCallback)(
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
              !ve && me.isEnabled && $ && Be();
            }, [Be, $, me.isEnabled, ve]),
            (0, r.useEffect)(() => {
              fe && !he
                ? yd.includes(D)
                  ? j(R.sounds.radial_big())
                  : j(R.sounds.radial_small())
                : !fe &&
                  he &&
                  (yd.includes(D) ? j(R.sounds.radial_big_close()) : j(R.sounds.radial_small()));
            }, [fe, he, D]),
            (0, r.useEffect)(() => {
              if (Ce.isRunning) return () => Ce.clear();
            }, [Ce]),
            (0, r.useEffect)(() => {
              (c && Z(!0),
                c ||
                  Ce.run(() => {
                    Z(!1);
                  }, 400));
            }, [c, Ce]),
            (0, r.useEffect)(() => {
              (_ && ($ && Be(), ue(!0)),
                _ ||
                  Ce.run(() => {
                    ue(!1);
                  }));
            }, [_, Ce, $, Be]));
          const Oe = Object.fromEntries(Object.entries(ce).filter(([e]) => "buyPrice" !== e)),
            Le = (0, r.useCallback)(
              (e) => {
                n.onStageChange(e);
              },
              [n],
            ),
            Re = (0, r.useCallback)(() => {
              (n.onToolbarItemClick(Ga.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1),
                n.progressiveInfoButtonClick());
            }, [n]);
          (0, r.useEffect)(() => {
            0 === oe.length &&
              Te.scrollPosition.start({ scrollPosition: 0, reset: !0, immediate: !0 });
          }, [Te, oe]);
          const Pe = (0, r.useCallback)(() => {
              (n.onToolbarItemClick(Ga.CUSTOMIZATION_SHEET_ACTION_CLOSE, -1), n.onClose());
            }, [n]),
            He = (0, r.useCallback)(() => {
              !C && n.onSceneOverChange(!1);
            }, [n, C]),
            We = (0, r.useCallback)(() => {
              !C && n.onSceneOverChange(!0);
            }, [n, C]);
          return o().createElement(
            "div",
            { className: v()(Ki, Q ? nl : al, $ && Zi), onMouseEnter: We, onMouseLeave: He },
            o().createElement(
              "div",
              { className: Ji },
              $
                ? o().createElement(Y_, {
                    onCarouselCollapse: Be,
                    startScrollItemId: z,
                    onUpdateItems: ye,
                    tabId: null == (e = u.computes.getSelectedTab()) ? void 0 : e.id,
                  })
                : o().createElement(
                    o().Fragment,
                    null,
                    !ne &&
                      o().createElement(Fi, {
                        moveSpace: n.moveSpace,
                        onSceneOverChange: xe,
                        onSceneDraggingChange: n.onSceneDraggingChange,
                        onSceneClick: n.onSceneClick,
                        onHideElements: (e) => {
                          te(e);
                        },
                        onResetMagneticTool: n.onUnselectItem,
                        isHovered: p,
                        isOnboardingViewOpened: C,
                      }),
                    g &&
                      !c &&
                      o().createElement(
                        "div",
                        { className: tl },
                        o().createElement(ze, {
                          caption: kd.progression.info(),
                          type: "info",
                          onClick: Re,
                        }),
                      ),
                    !_ &&
                      !c &&
                      o().createElement(
                        "div",
                        { className: ul },
                        o().createElement(ze, {
                          side: "right",
                          type: "close",
                          caption: kd.customization.closeButton(),
                          onClick: Pe,
                        }),
                      ),
                    _ &&
                      o().createElement(
                        "div",
                        { className: Gl },
                        o().createElement(ze, {
                          side: "left",
                          type: "back",
                          caption: kd.customization.backButton(),
                          onClick: n.onCloseStyleInfoEsc,
                        }),
                      ),
                    !c &&
                      !ne &&
                      o().createElement(
                        "div",
                        { className: v()(_l, Q ? ml : dl), "data-magnetic-tool-support": !0 },
                        o().createElement(Fd, { isSceneDraggingChange: Q }),
                      ),
                    Boolean(Fe.inscriptionState) &&
                      o().createElement("div", { className: kl }, o().createElement(pi, Fe)),
                    o().createElement(
                      "div",
                      { className: v()(Qi, c && el) },
                      o().createElement(Ui, be),
                      !ne && o().createElement(ua, { text: ge, className: v()(rl, pe && ol) }),
                    ),
                    o().createElement(
                      "div",
                      { className: v()(Ll, (c || _) && Rl) },
                      o().createElement(
                        "div",
                        { className: sl },
                        o().createElement(
                          "div",
                          { className: il },
                          o().createElement(
                            "div",
                            { className: vl, onMouseEnter: He, onMouseLeave: We },
                            o().createElement(
                              Ua,
                              { body: d ? Td.openPanelDisabledButton() : Td.openPanelButton() },
                              o().createElement(
                                "div",
                                { className: jl },
                                o().createElement(
                                  Ha,
                                  {
                                    type: La.ghost,
                                    size: Ae,
                                    mixClass: fl,
                                    onClick: () => {
                                      if (h.current) {
                                        const e = h.current.getFirstVisibleItemId();
                                        V(e || -1);
                                      }
                                      (n.onExpandCarousel(!0), X(!0));
                                    },
                                    disabled: d,
                                  },
                                  o().createElement(ua, {
                                    className: hl,
                                    text: kd.filters.openPanelButton(),
                                  }),
                                ),
                              ),
                            ),
                            o().createElement("div", { className: Dl }),
                            o().createElement(vr, { buttonSize: Ae }),
                          ),
                          o().createElement(
                            "div",
                            { className: Fl, onMouseEnter: He, onMouseLeave: We },
                            re &&
                              o().createElement(tu, {
                                price: re,
                                onResetHandler: n.onClearBasket,
                                onBackHandler: n.onCancelChanges,
                                onApplyHandler: Ne,
                                cartParams: Oe,
                                buttonSize: Ae,
                              }),
                          ),
                        ),
                      ),
                      o().createElement(
                        "div",
                        { className: ll, onMouseEnter: He, onMouseLeave: We },
                        o().createElement("div", { className: cl }),
                        o().createElement(Wo, {
                          isEditable: d,
                          tabs: le,
                          onClick: (e) => {
                            (j(R.sounds.cust_tab_switch()), n.selectTab(e));
                          },
                          onHoverTab: n.hoverTab,
                          onEditClose: n.closeEditItem,
                        }),
                        oe.length > 0
                          ? o().createElement(N_, {
                              ref: h,
                              scrollApi: Te,
                              items: oe,
                              arrowsList: ie,
                              categories: se,
                              onClick: Me,
                              onHoverItem: n.hoverItem,
                              onEditClick: n.onEditItem,
                              onArrowClick: n.onPressSelectNextItem,
                              isCarouselArrowsHintVisible: P,
                              scrollStartItemId: L,
                              selectedItemId: H,
                              firstExpandedItemId: z,
                              tabId: null == (t = u.computes.getSelectedTab()) ? void 0 : t.id,
                              lastScrollState: U,
                              isEditable: d,
                              onUpdateItems: ye,
                            })
                          : o().createElement(
                              j_,
                              {
                                warningHeader: kd.customization.message.header(),
                                warningDescription: kd.customization.message.description(),
                                buttonType: La.secondary,
                                onClick: n.clearFilter,
                                className: El,
                              },
                              o().createElement(ua, {
                                text: kd.customization.resetFiltersBtn.label(),
                              }),
                            ),
                      ),
                    ),
                  ),
              o().createElement(
                "div",
                {
                  className: v()(Bl, !c && (Q ? wl : Sl)),
                  "data-magnetic-tool-support": !0,
                  onMouseEnter: He,
                  onMouseLeave: We,
                },
                o().createElement(Li, { tabs: _e, onClick: Ie, isMinimised: $ || c || ne }),
              ),
              !$ &&
                o().createElement(yi, {
                  onClick: n.clickDecalsBanner,
                  onMouseEnter: He,
                  onMouseLeave: We,
                  mixClass: v()(pl, (c || _) && bl, !(c || _) && (Q ? Cl : Al)),
                }),
              c &&
                o().createElement(
                  "div",
                  { className: v()(Pl, c && Hl) },
                  o().createElement(
                    "div",
                    { className: Wl },
                    re &&
                      o().createElement(tu, {
                        price: re,
                        onResetHandler: n.onClearBasket,
                        onBackHandler: n.onCancelChanges,
                        onApplyHandler: Ne,
                        onAutoRentChange: n.onAutoRentChange,
                        onAutoRentHintClose: n.onAutoRentHintClose,
                        cartParams: Oe,
                        buttonSize: Ae,
                        className: zl,
                      }),
                  ),
                ),
              m &&
                !$ &&
                !c &&
                !_ &&
                o().createElement(
                  "div",
                  { className: Ml, "data-magnetic-tool-support": !0 },
                  o().createElement(Is, {
                    itemType: D,
                    isSelected: E,
                    onSelectApplyingAllSeasons: n.onApplyToAllSeasonsChange,
                  }),
                ),
              fe &&
                o().createElement(
                  "div",
                  {
                    className: v()(Tl, S && Il),
                    "data-magnetic-tool-support": !0,
                    onMouseEnter: He,
                    onMouseLeave: We,
                  },
                  o().createElement(ws, {
                    toolbarItems: de,
                    onItemClick: Se,
                    onCloseAction: n.onClose,
                  }),
                ),
              S &&
                !c &&
                !_ &&
                o().createElement(
                  "div",
                  { className: v()(Tl, Nl), onMouseEnter: He, onMouseLeave: We },
                  o().createElement(io, {
                    numberOfBullets: k,
                    currentNumber: N,
                    selectedNumber: w,
                    isBulletsBeforeCurrentDisabled: T,
                    onChange: Le,
                    switcherType: 2 === k ? ja.text : ja.digital,
                    size: so.small,
                    styleID: 594,
                  }),
                ),
              K &&
                o().createElement(sn, {
                  id: R.views.lobby.customization.CustomizationBinSubview("resId"),
                  mixClass: v()(xl, c && Ol),
                }),
              ne &&
                o().createElement(sn, {
                  id: R.views.lobby.customization.CustomizationStyleInfoView("resId"),
                  mixClass: v()(Vl, _ && Ul),
                }),
              f && !K && !ne && o().createElement(ei, { mixClass: gl }),
              De &&
                o().createElement(
                  "div",
                  { className: yl },
                  o().createElement(Ai, Dd({}, me, { selectedTab: D })),
                ),
            ),
          );
        });
        const Nd = "Slot_base_de",
          Id = "Slot_base__big_d6",
          Md = "Slot_base__locked_8d",
          xd = "Slot_inActive_24",
          Od = "Slot_border_6c",
          Ld = "Slot_base__selected_75",
          Rd = "Slot_topLeftCorner_3f",
          Pd = "Slot_shadowBottom_a1",
          Hd = "Slot_base__hasExtraName_c3",
          Wd = "Slot_shadowTop_14",
          zd = "Slot_base__topLeftCornerVisible_2c",
          Vd = "Slot_base__unSelected_2d",
          Ud = "Slot_image_c8",
          Gd = "Slot_ribbon_9e",
          jd = "Slot_icon_2d",
          $d = "Slot_icon__rewindable_44",
          Xd = "Slot_icon__special_ee",
          qd = "Slot_icon__alert_51",
          Yd = "Slot_icon__unHistorical_ce",
          Kd = "Slot_icon__fantastical_0f",
          Zd = "Slot_icon__serialNumber_19",
          Jd = "Slot_icon__progression_db",
          Qd = "Slot_hover_22",
          em = "Slot_base__hovered_eb",
          tm = "Slot_price_7e",
          am = "Slot_styleName_5b",
          nm = (0, r.memo)(
            ({
              itemID: e,
              intCD: t,
              typeId: a,
              isDisabled: n,
              soundHover: u = R.sounds.highlight(),
              isSelected: s,
              customizationDisplayType: i,
              tooltip: l,
              isSpecial: c,
              showAlert: _,
              isDim: d,
              isFromStorage: m,
              icon: E,
              isWide: g,
              quantity: p,
              buyPrice: b,
              extraName: A,
              classMix: C,
              progressionLevel: f,
              isProgressionRewindEnabled: h,
              onSelectItem: F,
              isRental: D,
              rentalInfoText: B,
              autoRentEnabled: S,
              isWithSerialNumber: w,
              isMainType: y,
              season: k,
            }) => {
              var T;
              const N = (0, r.useState)(!1),
                I = N[0],
                M = N[1],
                x = (0, r.useMemo)(() => -1 === t, [t]),
                O = (0, r.useState)(!x && !n),
                L = O[0],
                P = O[1],
                H = _ || c || (i && !x) || f > -1,
                W = (0, r.useCallback)(() => {
                  !u || x || n || (M(!0), j(u));
                }, [x, n, u]),
                z = (0, r.useCallback)(() => {
                  x ||
                    n ||
                    (j(s ? R.sounds.cust_select_remove() : R.sounds.cust_color_apply()),
                    e && F(e, !s, k));
                }, [F, x, n, s, e, k]),
                V = v()(
                  Nd,
                  C,
                  I && em,
                  g && Id,
                  s && !x && Ld,
                  !s && Vd,
                  H && zd,
                  A && Hd,
                  (x || n) && Md,
                ),
                U = (0, r.useMemo)(
                  () => ({ itemID: e, tooltip: l, showInventoryBlock: !x, progressionLevel: f }),
                  [x, e, f, l],
                ),
                G = (0, r.useCallback)(() => {
                  P(!1);
                }, [P]);
              return (
                (0, r.useEffect)(
                  () => (
                    engine.on(Sd, G),
                    engine.on(Ta, () => {
                      engine.off(Sd, G);
                    }),
                    () => {
                      engine.off(Sd, G);
                    }
                  ),
                  [G],
                ),
                o().createElement(
                  Ca,
                  { args: U, isEnabled: L },
                  o().createElement(
                    "div",
                    {
                      className: V,
                      onMouseEnter: W,
                      onMouseLeave: () => {
                        M(!1);
                      },
                      onClick: z,
                    },
                    o().createElement(
                      "div",
                      { className: Od },
                      o().createElement(
                        "div",
                        { className: Ud },
                        o().createElement(_c, { isDim: d, icon: E }),
                      ),
                      o().createElement("div", { className: Wd }),
                      (A || b.price[0]) && o().createElement("div", { className: Pd }),
                      y && o().createElement("div", { className: Gd }),
                      o().createElement(
                        "div",
                        { className: Rd },
                        _ && o().createElement("div", { className: v()(jd, qd) }),
                        c && o().createElement("div", { className: v()(jd, Xd) }),
                        w && o().createElement("div", { className: v()(jd, Zd) }),
                        1 === i && !x && o().createElement("div", { className: v()(jd, Yd) }),
                        2 === i && !x && o().createElement("div", { className: v()(jd, Kd) }),
                        !h &&
                          o().createElement(wc, {
                            typeId: a,
                            progressionLevel: f,
                            classMix: v()(jd, Jd),
                          }),
                        h && o().createElement("div", { className: v()(jd, $d) }),
                      ),
                      o().createElement(ua, { className: am, text: A }),
                      o().createElement(vc, {
                        classMix: tm,
                        isStub: x,
                        price: b.price,
                        quantity: p,
                        isRental: D,
                        rentalInfoText: B,
                        autoRentEnabled: S,
                        isFromStorage: m,
                        hasDiscount: Boolean(null == (T = b.discount[0]) ? void 0 : T.value),
                        locked: !1,
                      }),
                      o().createElement("span", { className: Qd }),
                      (!s || n) && o().createElement("div", { className: xd }),
                    ),
                  ),
                )
              );
            },
          ),
          um = "Title_base_16",
          rm = "Title_title_65",
          om = "Title_count_ac",
          sm = "Title_count__empty_39",
          im = "Title_icon_39",
          lm = "Title_bonus_37",
          cm = "Title_blink_da",
          _m = "Title_blink__first_74",
          dm = R.strings.customization.cart,
          mm = R.images.gui.maps.icons.customization.cart,
          Em = ["summer", "winter", "desert"],
          gm = ({ count: e, name: t, selectedSeason: a, bonusValue: n }) => {
            const u = en(a);
            return o().createElement(
              "div",
              { className: um },
              "all_seasons" === t
                ? Em.map((e) =>
                    o().createElement("div", {
                      key: e,
                      className: im,
                      style: { backgroundImage: `url(${mm.$dyn(e)})` },
                    }),
                  )
                : o().createElement("div", {
                    className: im,
                    style: { backgroundImage: `url(${mm.$dyn(t)})` },
                  }),
              o().createElement(ua, { text: dm.seasonsName.$dyn(`${t}`), className: rm }),
              e >= 0 &&
                o().createElement(ua, { text: `(${e})`, className: v()(om, 0 === e && sm) }),
              n &&
                o().createElement(ua, {
                  text: dm.bonus(),
                  format: { binding: { bonus: n } },
                  className: lm,
                }),
              a === t && o().createElement("div", { className: v()(cm, !u && _m) }),
            );
          };
        function pm() {
          return (
            (pm =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            pm.apply(this, arguments)
          );
        }
        viewEnv.clearInternalCacheAfterFinalize();
        const bm = (0, Le.Pi)(() => {
          const e = ot(),
            t = e.controls,
            a = e.model,
            n = a.root.get().selectedSeason,
            u = a.computes.getSeasonsItemsList(),
            s = Oe.Vertical.useVerticalScrollApi(),
            i = (0, r.useState)(!1),
            l = i[0],
            c = i[1],
            _ = (0, r.useState)(!1),
            d = _[0],
            m = _[1],
            E = (0, r.useState)(!1),
            g = E[0],
            p = E[1],
            b = (0, r.useRef)(null);
          !(function (e, t) {
            const a = e.contentRef,
              n = e.wrapperRef,
              u = e.scrollPosition,
              o = e.clampPosition,
              s = e.animationScroll,
              i = e.events,
              l = (0, r.useState)(Re),
              c = l[0],
              _ = l[1];
            ((0, r.useEffect)(() => {
              const e = a.current;
              e && (e.style.cursor = "dragging" === c.type ? "grabbing" : "grab");
            }, [a, c.type]),
              (0, r.useEffect)(() => {
                if ("dragging" !== c.type) return;
                const e = (e) => {
                    const r = a.current,
                      i = n.current;
                    if (!r || !i) return;
                    const l = c.positionFrom - e.screenY,
                      _ = c.previousScrollPosition + l;
                    u.start(
                      Object.assign(
                        {
                          scrollPosition: o(r, _),
                          from: { scrollPosition: s.scrollPosition.get() },
                        },
                        t && { config: t },
                      ),
                    );
                  },
                  r = () => {
                    (window.removeEventListener("mousemove", e), _({ type: "scrollingToEnd" }));
                  };
                return (
                  window.addEventListener("mousemove", e),
                  window.addEventListener("mouseup", r),
                  () => {
                    (window.removeEventListener("mousemove", e),
                      window.removeEventListener("mouseup", r));
                  }
                );
              }, [s.scrollPosition, o, a, c, u, n, t]),
              (0, r.useEffect)(() => {
                if ("scrollingToEnd" !== c.type) return;
                const e = () => {
                  _(Re);
                };
                return (s.scrollPosition.idle && e(), i.on("rest", e), () => i.off("rest", e));
              }, [s.scrollPosition, c.type, i]),
              (0, r.useEffect)(() => {
                const e = a.current;
                if (!e) return;
                const t = (e) => {
                  (e.stopPropagation(),
                    0 === e.button &&
                      _({
                        type: "dragging",
                        positionFrom: e.screenY,
                        previousScrollPosition: s.scrollPosition.get(),
                      }));
                };
                return (
                  e.addEventListener("mousedown", t),
                  () => e.removeEventListener("mousedown", t)
                );
              }, [s.scrollPosition, a]));
          })(s);
          const A = (0, r.useMemo)(() => u.some((e) => Boolean(e.items.items.length)), [u]);
          (0, r.useEffect)(() => {
            const e = () => {
              const e = s.animationScroll.scrollPosition.goal;
              c(0 !== e);
              const t = s.getBounds()[1];
              var a, n, u;
              (m(t !== e),
                b.current &&
                  p(
                    ((a = b.current),
                    (null != (n = null == (u = a.parentElement) ? void 0 : u.offsetHeight)
                      ? n
                      : 0) < a.offsetHeight),
                  ));
            };
            return (
              e(),
              s.events.on("change", e),
              s.events.on("resizeHandled", e),
              () => {
                (s.events.off("change", e), s.events.off("resizeHandled", e));
              }
            );
          }, [s]);
          const C = v()(ct, l && _t, d && dt, l && d && mt);
          return o().createElement(
            "div",
            { className: st },
            o().createElement("div", { className: it }),
            A
              ? o().createElement(
                  o().Fragment,
                  null,
                  l && o().createElement("div", { className: ft }),
                  o().createElement(
                    "div",
                    { className: C },
                    o().createElement(
                      Oe.Vertical.Area,
                      { api: s },
                      o().createElement(
                        "div",
                        { className: v()(Et, !g && gt), ref: b },
                        u.map((e) =>
                          e.items.items.length > 0
                            ? o().createElement(
                                "div",
                                { key: e.name, className: pt },
                                o().createElement(gm, {
                                  count: e.count,
                                  name: e.name,
                                  bonusValue: e.bonusValue,
                                  selectedSeason: n,
                                }),
                                o().createElement("div", { className: bt }),
                                o().createElement(
                                  "div",
                                  { className: At },
                                  e.items.items.map((a, n) =>
                                    o().createElement(
                                      nm,
                                      pm(
                                        {
                                          key: `${a.intCD}_${n}`,
                                          onSelectItem: t.selectItem,
                                          season: e.name,
                                          classMix: ht,
                                        },
                                        a,
                                      ),
                                    ),
                                  ),
                                ),
                              )
                            : null,
                        ),
                      ),
                    ),
                    o().createElement(Oe.Vertical.Bar, { api: s, classNames: { base: Ct } }),
                  ),
                )
              : o().createElement(_a, null),
            o().createElement(
              "div",
              { className: lt },
              o().createElement(je, {
                onCloseCallback: () => {
                  t.close();
                },
              }),
            ),
          );
        });
        engine.whenReady.then(() => {
          const e = document.getElementById("root").getAttribute("data-root-id");
          H().render(
            o().createElement(
              rt,
              { options: { rootId: Number(e) } },
              o().createElement(L, null, o().createElement(bm, null)),
            ),
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
    var a = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](a, a.exports, __webpack_require__), a.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, a, n) => {
      if (!t) {
        var u = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, a, n] = deferred[i], r = !0, o = 0; o < t.length; o++)
            (!1 & n || u >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((r = !1), n < u && (u = n));
          if (r) {
            deferred.splice(i--, 1);
            var s = a();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > n; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, a, n];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var a in t)
        __webpack_require__.o(t, a) &&
          !__webpack_require__.o(e, a) &&
          Object.defineProperty(e, a, { enumerable: !0, get: t[a] });
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
    (__webpack_require__.j = 690),
    (() => {
      var e = { 690: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var n,
            u,
            [r, o, s] = a,
            i = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (t && t(a); i < r.length; i++)
            ((u = r[i]), __webpack_require__.o(e, u) && e[u] && e[u][0](), (e[u] = 0));
          return __webpack_require__.O(l);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [858], () => __webpack_require__(9884));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
