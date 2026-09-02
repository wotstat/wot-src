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
        (a.r(t), a.d(t, { mouse: () => o, onResize: () => s }));
        var r = a(2472),
          n = a(1176);
        const s = (0, r.E)("clientResized"),
          u = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const o = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, n.R)(!1);
          }
          function a() {
            e.enabled && (0, n.R)(!0);
          }
          function r() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", a))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", a))
              : (0, n.R)(!1);
          }
          const s = ["down", "up", "move"].reduce(
            (t, a) => (
              (t[a] = (function (t) {
                return (a) => {
                  e.listeners += 1;
                  let n = !0;
                  const s = `mouse${t}`,
                    o = u[t]((e) => a([e, "outside"]));
                  function i(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(s, i),
                    r(),
                    () => {
                      n &&
                        (o(), window.removeEventListener(s, i), (e.listeners -= 1), r(), (n = !1));
                    }
                  );
                };
              })(a)),
              t
            ),
            {},
          );
          return Object.assign({}, s, {
            disable() {
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
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
      5959: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            events: () => r,
            getMouseGlobalPosition: () => s,
            getSize: () => n,
            graphicsQuality: () => u,
          }));
        var r = a(527);
        function n(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function s(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const u = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, a) => {
        "use strict";
        function r(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        a.d(t, { R: () => r });
      },
      2472: (e, t, a) => {
        "use strict";
        function r(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        a.d(t, { E: () => r });
      },
      3138: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => n });
        var r = a(5959);
        const n = { view: a(7641), client: r };
      },
      3722: (e, t, a) => {
        "use strict";
        function r(e, t, a = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, a);
        }
        function n(e, t, a) {
          return `url(${r(e, t, a)})`;
        }
        (a.r(t), a.d(t, { getBgUrl: () => n, getTextureUrl: () => r }));
      },
      6112: (e, t, a) => {
        "use strict";
        a.d(t, { W: () => r });
        const r = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, a) => {
        "use strict";
        a.d(t, { U: () => n });
        var r = a(2472);
        const n = {
          onTextureFrozen: (0, r.E)("self.onTextureFrozen"),
          onTextureReady: (0, r.E)("self.onTextureReady"),
          onDomBuilt: (0, r.E)("self.onDomBuilt"),
          onLoaded: (0, r.E)("self.onLoaded"),
          onDisplayChanged: (0, r.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, r.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, r.E)("children.onAdded"),
            onLoaded: (0, r.E)("children.onLoaded"),
            onRemoved: (0, r.E)("children.onRemoved"),
            onAttached: (0, r.E)("children.onAttached"),
            onTextureReady: (0, r.E)("children.onTextureReady"),
            onRequestPosition: (0, r.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => o,
            children: () => r,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => s.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => F,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => B,
            getScale: () => p,
            getSize: () => m,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => v,
            isEventHandled: () => D,
            isFocused: () => A,
            pxToRem: () => b,
            remToPx: () => f,
            resize: () => _,
            sendEvent: () => u.qP,
            setAnimateWindow: () => h,
            setEventHandled: () => C,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => P,
          }));
        var r = a(3722),
          n = a(6112),
          s = a(6538),
          u = a(8566);
        function o(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, a, r = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, a, r);
        }
        function c(e, t, a) {
          return viewEnv.addDataChangedCallback(e, t, a);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function _(e, t, a = "px") {
          return "rem" === a ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: f(t.x), y: f(t.y) };
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
        function f(e) {
          return viewEnv.remToPx(e);
        }
        function h(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function A() {
          return viewEnv.isFocused();
        }
        function v() {
          return viewEnv.isClientAccessible();
        }
        function C() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function F() {
          viewEnv.forceTriggerMouseMove();
        }
        function B() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === n.W[t]), e),
            {},
          ),
          S = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          P = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : s.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        "use strict";
        a.d(t, { qP: () => l });
        const r = ["args"];
        const n = 2,
          s = 16,
          u = 32,
          o = 64,
          i = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const s = t.args,
                u = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    r,
                    n = {},
                    s = Object.keys(e);
                  for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                  return n;
                })(t, r);
              return void 0 !== s
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, u, {
                      arguments:
                        ((n = s),
                        Object.entries(n).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, u));
            }
            return viewEnv.handleViewEvent({ __Type: a, type: e });
            var n;
          },
          l = {
            close(e) {
              i("popover" === e ? n : u);
            },
            minimize() {
              i(o);
            },
            move(e) {
              i(s, { isMouseEvent: !0, on: e });
            },
          };
      },
      5521: (e, t, a) => {
        "use strict";
        let r, n;
        (a.d(t, { n: () => r }),
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
          })(r || (r = {})),
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
      1358: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => s });
        var r = a(3138);
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
          addCallback(e, t, a = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const s = r.O.view.addModelObserver(e, a, n);
            return (
              s > 0
                ? ((this._callbacks[s] = t),
                  a > 0 && (this._views[a] ? this._views[a].push(s) : (this._views[a] = [s])))
                : console.error("Can't add callback for model:", e),
              s
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
              const r = this._callbacks[a];
              void 0 !== r && r(e, t);
            });
          }
        }
        n.__instance = void 0;
        const s = n;
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
          Sw: () => s.Z,
          kH: () => m,
          B3: () => l,
          Z5: () => u,
          lf: () => d,
          cy: () => o,
          B0: () => i,
          c9: () => A,
          ry: () => f,
          Eu: () => h,
        });
        class r {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: a }) => {
                  let r = e.target;
                  do {
                    if (r === t) return;
                    r = r.parentNode;
                  } while (r);
                  a();
                });
              }));
          }
          static get instance() {
            return (r.__instance || (r.__instance = new r()), r.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const a = e,
              r = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== a || t !== r,
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
        r.__instance = void 0;
        const n = r;
        var s = a(1358);
        const u = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
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
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = a(5521),
          E = a(3138);
        const g = ["args"];
        function p(e, t, a, r, n, s, u) {
          try {
            var o = e[s](u),
              i = o.value;
          } catch (e) {
            return void a(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(r, n);
        }
        const b = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          f = (function () {
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
                  return new Promise(function (r, n) {
                    var s = e.apply(t, a);
                    function u(e) {
                      p(s, r, n, u, o, "next", e);
                    }
                    function o(e) {
                      p(s, r, n, u, o, "throw", e);
                    }
                    u(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          h = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          A = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const n = t.args,
                s = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    r,
                    n = {},
                    s = Object.keys(e);
                  for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                  return n;
                })(t, g);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, s, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, s));
            } else viewEnv.handleViewEvent({ __Type: a, type: e });
            var r;
          },
          v = () => A(i.CLOSE),
          C = (e, t) => {
            e.keyCode === _.n.ESCAPE && t();
          };
        var D = a(7572);
        const F = n.instance,
          B = {
            DataTracker: s.Z,
            ViewModel: D.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: m,
            makeGlobalBoundingBox: b,
            sendMoveEvent: (e) => A(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: v,
            sendClosePopOverEvent: () => A(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, a = 0) => {
              A(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: a,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, a, r, n = R.invalid("resId"), s) => {
              const u = E.O.view.getViewGlobalPosition(),
                o = a.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                d = o.width,
                m = o.height,
                _ = {
                  x: E.O.view.pxToRem(l) + u.x,
                  y: E.O.view.pxToRem(c) + u.y,
                  width: E.O.view.pxToRem(d),
                  height: E.O.view.pxToRem(m),
                };
              A(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: r || R.invalid("resId"),
                targetID: n,
                direction: t,
                bbox: b(_),
                on: !0,
                args: s,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => C(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              C(e, v);
            },
            handleViewEvent: A,
            onBindingsReady: f,
            onLayoutReady: h,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
            dumpViewModel: function e(t) {
              const a = {};
              if ("object" != typeof t) return t;
              for (const r in t)
                if (Object.prototype.hasOwnProperty.call(t, r)) {
                  const n = Object.prototype.toString.call(t[r]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = t[r];
                    a[r] = [];
                    for (let t = 0; t < n.length; t++) a[r].push({ value: e(n[t].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (a[r] = e(t[r]))
                      : (a[r] = t[r]);
                }
              return a;
            },
            ClickOutsideManager: F,
            SystemLocale: u,
            UserLocale: o,
          };
        window.ViewEnvHelper = B;
      },
      4304: (e, t, a) => {
        "use strict";
        var r = {};
        (a.r(r),
          a.d(r, {
            Area: () => yr,
            Bar: () => wr,
            Default: () => Pr,
            useVerticalScrollApi: () => nr,
          }));
        var n = {};
        (a.r(n),
          a.d(n, {
            Area: () => Co,
            Bar: () => ho,
            DefaultScroll: () => vo,
            Direction: () => tr,
            defaultSettings: () => ar,
            useHorizontalScrollApi: () => so,
          }));
        var s = a(6179),
          u = a.n(s);
        const o = (e, t, a) =>
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
        function d(e, t, a) {
          const r = (function (e, t) {
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
            })(t, a),
            s = Math.min(r, n);
          return {
            extraLarge: s === a.extraLarge.weight,
            large: s === a.large.weight,
            medium: s === a.medium.weight,
            small: s === a.small.weight,
            extraSmall: s === a.extraSmall.weight,
            extraLargeWidth: r === a.extraLarge.weight,
            largeWidth: r === a.large.weight,
            mediumWidth: r === a.medium.weight,
            smallWidth: r === a.small.weight,
            extraSmallWidth: r === a.extraSmall.weight,
            extraLargeHeight: n === a.extraLarge.weight,
            largeHeight: n === a.large.weight,
            mediumHeight: n === a.medium.weight,
            smallHeight: n === a.small.weight,
            extraSmallHeight: n === a.extraSmall.weight,
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
        const m = i.O.client.getSize("rem"),
          _ = m.width,
          E = m.height,
          g = Object.assign({ width: _, height: E }, d(_, E, l)),
          p = (0, s.createContext)(g),
          b = ["children"];
        const f = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                r,
                n = {},
                s = Object.keys(e);
              for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
              return n;
            })(e, b);
          const r = (0, s.useContext)(p),
            n = r.extraLarge,
            u = r.large,
            i = r.medium,
            l = r.small,
            c = r.extraSmall,
            d = r.extraLargeWidth,
            m = r.largeWidth,
            _ = r.mediumWidth,
            E = r.smallWidth,
            g = r.extraSmallWidth,
            f = r.extraLargeHeight,
            h = r.largeHeight,
            A = r.mediumHeight,
            v = r.smallHeight,
            C = r.extraSmallHeight,
            D = { extraLarge: f, large: h, medium: A, small: v, extraSmall: C };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && n) return t;
            if (a.large && u) return t;
            if (a.medium && i) return t;
            if (a.small && l) return t;
            if (a.extraSmall && c) return t;
          } else {
            if (a.extraLargeWidth && d) return o(t, a, D);
            if (a.largeWidth && m) return o(t, a, D);
            if (a.mediumWidth && _) return o(t, a, D);
            if (a.smallWidth && E) return o(t, a, D);
            if (a.extraSmallWidth && g) return o(t, a, D);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && f) return t;
              if (a.largeHeight && h) return t;
              if (a.mediumHeight && A) return t;
              if (a.smallHeight && v) return t;
              if (a.extraSmallHeight && C) return t;
            }
          }
          return null;
        };
        f.defaultProps = {
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
        (0, s.memo)(f);
        const h = (e) => {
            const t = (0, s.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          A = (0, s.memo)(({ children: e }) => {
            const t = (0, s.useContext)(p),
              a = (0, s.useState)(t),
              r = a[0],
              n = a[1],
              o = (0, s.useCallback)((e, t) => {
                const a = i.O.view.pxToRem(e),
                  r = i.O.view.pxToRem(t);
                n(Object.assign({ width: a, height: r }, d(a, r, l)));
              }, []);
            (h(() => {
              engine.on("clientResized", o);
            }),
              (0, s.useEffect)(() => () => engine.off("clientResized", o), [o]));
            const c = (0, s.useMemo)(() => Object.assign({}, r), [r]);
            return u().createElement(p.Provider, { value: c }, e);
          });
        var v = a(6483),
          C = a.n(v),
          D = a(926),
          F = a.n(D);
        let B, w, S;
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
          })(w || (w = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.small.height)] = "Small"),
              (e[(e.Medium = l.medium.height)] = "Medium"),
              (e[(e.Large = l.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(S || (S = {})));
        const P = () => {
            const e = (0, s.useContext)(p),
              t = e.width,
              a = e.height,
              r = ((e) => {
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
                    return w.ExtraLarge;
                  case e.largeWidth:
                    return w.Large;
                  case e.mediumWidth:
                    return w.Medium;
                  case e.smallWidth:
                    return w.Small;
                  case e.extraSmallWidth:
                    return w.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), w.ExtraSmall);
                }
              })(e),
              u = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return S.ExtraLarge;
                  case e.largeHeight:
                    return S.Large;
                  case e.mediumHeight:
                    return S.Medium;
                  case e.smallHeight:
                    return S.Small;
                  case e.extraSmallHeight:
                    return S.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), S.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: r,
              mediaWidth: n,
              mediaHeight: u,
              remScreenWidth: t,
              remScreenHeight: a,
            };
          },
          y = ["children", "className"];
        function k() {
          return (
            (k =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            k.apply(this, arguments)
          );
        }
        const T = {
            [w.ExtraSmall]: "",
            [w.Small]: F().SMALL_WIDTH,
            [w.Medium]: `${F().SMALL_WIDTH} ${F().MEDIUM_WIDTH}`,
            [w.Large]: `${F().SMALL_WIDTH} ${F().MEDIUM_WIDTH} ${F().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${F().SMALL_WIDTH} ${F().MEDIUM_WIDTH} ${F().LARGE_WIDTH} ${F().EXTRA_LARGE_WIDTH}`,
          },
          x = {
            [S.ExtraSmall]: "",
            [S.Small]: F().SMALL_HEIGHT,
            [S.Medium]: `${F().SMALL_HEIGHT} ${F().MEDIUM_HEIGHT}`,
            [S.Large]: `${F().SMALL_HEIGHT} ${F().MEDIUM_HEIGHT} ${F().LARGE_HEIGHT}`,
            [S.ExtraLarge]: `${F().SMALL_HEIGHT} ${F().MEDIUM_HEIGHT} ${F().LARGE_HEIGHT} ${F().EXTRA_LARGE_HEIGHT}`,
          },
          N = {
            [B.ExtraSmall]: "",
            [B.Small]: F().SMALL,
            [B.Medium]: `${F().SMALL} ${F().MEDIUM}`,
            [B.Large]: `${F().SMALL} ${F().MEDIUM} ${F().LARGE}`,
            [B.ExtraLarge]: `${F().SMALL} ${F().MEDIUM} ${F().LARGE} ${F().EXTRA_LARGE}`,
          },
          I = (e) => {
            let t = e.children,
              a = e.className,
              r = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, y);
            const n = P(),
              s = n.mediaWidth,
              o = n.mediaHeight,
              i = n.mediaSize;
            return u().createElement("div", k({ className: C()(a, T[s], x[o], N[i]) }, r), t);
          },
          L = ["children"];
        const M = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                r,
                n = {},
                s = Object.keys(e);
              for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
              return n;
            })(e, L);
          return u().createElement(A, null, u().createElement(I, a, t));
        };
        var O = a(493),
          H = a.n(O);
        function W(e) {
          engine.call("PlaySound", e);
        }
        const $ = {
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
          z = [
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
        function G() {
          return (
            (G =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            G.apply(this, arguments)
          );
        }
        class j extends u().PureComponent {
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
              a = e.onClick,
              r = e.goto,
              n = e.side,
              s = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              d = e.onMouseUp,
              m =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var a,
                    r,
                    n = {},
                    s = Object.keys(e);
                  for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                  return n;
                })(e, z)),
              _ = C()(U.base, U[`base__${s}`], U[`base__${n}`], null == o ? void 0 : o.base),
              E = C()(U.icon, U[`icon__${s}`], U[`icon__${n}`], null == o ? void 0 : o.icon),
              g = C()(U.glow, null == o ? void 0 : o.glow),
              p = C()(U.caption, U[`caption__${s}`], null == o ? void 0 : o.caption),
              b = C()(U.goto, null == o ? void 0 : o.goto);
            return u().createElement(
              "div",
              G(
                {
                  className: _,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: a,
                },
                m,
              ),
              "info" !== s && u().createElement("div", { className: U.shine }),
              u().createElement(
                "div",
                { className: E },
                u().createElement("div", { className: g }),
              ),
              u().createElement("div", { className: p }, t),
              r && u().createElement("div", { className: b }, r),
            );
          }
        }
        j.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var q = a(3403),
          V = a(5521),
          X = a(4179);
        const Q = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function Y(e = V.n.NONE, t = Q, a = !1) {
          (0, s.useEffect)(() => {
            if (e !== V.n.NONE)
              return (
                window.addEventListener("keydown", r, a),
                () => {
                  window.removeEventListener("keydown", r, a);
                }
              );
            function r(r) {
              if (r.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), t(r), a && r.stopPropagation());
              }
            }
          }, [t, e, a]);
        }
        const K = "page_heading_05",
          Z = "page_close_a4",
          J = ({ onClose: e, className: t }) => {
            var a;
            return (
              (a = e),
              Y(V.n.ESCAPE, a),
              u().createElement(
                "div",
                { className: C()(Z, t) },
                u().createElement(j, {
                  caption: R.strings.comp7.closeButtonLabel(),
                  type: "close",
                  side: "right",
                  onClick: e,
                }),
              )
            );
          },
          ee = () => i.O.client.graphicsQuality.isHigh();
        function te() {}
        function ae() {
          return !1;
        }
        console.log;
        var re = a(9174);
        function ne(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return se(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return se(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function se(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, r = new Array(t); a < t; a++) r[a] = e[a];
          return r;
        }
        const ue = (e) => (0 === e ? window : window.subViews.get(e));
        const oe = () => (e, t) => {
            const a = (0, s.createContext)({});
            return [
              function ({ mode: r = "real", options: n, children: o, mocks: l }) {
                const c = (0, s.useRef)([]),
                  d = (a, r, n) => {
                    var s;
                    const u = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: a = ue,
                        context: r = "model",
                      } = {}) {
                        const n = new Map();
                        function s(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? n.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, a) => {
                            a.forEach((t) => {
                              const a = n.get(t);
                              void 0 !== a && a(e);
                            });
                          });
                        });
                        const u = (e) => {
                          const n = a(t),
                            s = r.split(".").reduce((e, t) => e[t], n);
                          return "string" != typeof e || 0 === e.length
                            ? s
                            : e.split(".").reduce((e, t) => {
                                const a = e[t];
                                return "function" == typeof a ? a.bind(e) : a;
                              }, s);
                        };
                        return {
                          subscribe: (a, s) => {
                            const o = "string" == typeof s ? `${r}.${s}` : r,
                              l = i.O.view.addModelObserver(o, t, !0);
                            return (n.set(l, a), e && a(u(s)), l);
                          },
                          readByPath: u,
                          createCallback: (e, t) => {
                            const a = u(t);
                            return (...t) => {
                              a(e(...t));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const t = u(e);
                            return () => {
                              t();
                            };
                          },
                          dispose: function () {
                            for (var e, a = ne(n.keys()); !(e = a()).done;) s(e.value, t);
                          },
                          unsubscribe: s,
                        };
                      })(r),
                      o =
                        "real" === a
                          ? u
                          : Object.assign({}, u, {
                              readByPath:
                                null != (s = null == n ? void 0 : n.getter) ? s : () => {},
                            }),
                      l = (e) =>
                        "mocks" === a ? (null == n ? void 0 : n.getter(e)) : o.readByPath(e),
                      d = (e) => c.current.push(e),
                      m = e({
                        mode: a,
                        readByPath: l,
                        externalModel: o,
                        observableModel: {
                          array: (e, t) => {
                            const r = null != t ? t : l(e),
                              n = re.LO.box(r, { equals: ae });
                            return (
                              "real" === a &&
                                o.subscribe(
                                  (0, re.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          object: (e, t) => {
                            const r = null != t ? t : l(e),
                              n = re.LO.box(r, { equals: ae });
                            return (
                              "real" === a &&
                                o.subscribe(
                                  (0, re.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          primitives: (e, t) => {
                            const r = l(t);
                            if (Array.isArray(e)) {
                              const n = e.reduce((e, t) => ((e[t] = re.LO.box(r[t], {})), e), {});
                              return (
                                "real" === a &&
                                  o.subscribe(
                                    (0, re.aD)((t) => {
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
                                s = Object.entries(n),
                                u = s.reduce((e, [t, a]) => ((e[a] = re.LO.box(r[t], {})), e), {});
                              return (
                                "real" === a &&
                                  o.subscribe(
                                    (0, re.aD)((e) => {
                                      s.forEach(([t, a]) => {
                                        u[a].set(e[t]);
                                      });
                                    }),
                                    t,
                                  ),
                                u
                              );
                            }
                          },
                        },
                        cleanup: d,
                      }),
                      _ = { mode: a, model: m, externalModel: o, cleanup: d };
                    return {
                      model: m,
                      controls: "mocks" === a && n ? n.controls(_) : t(_),
                      externalModel: o,
                      mode: a,
                    };
                  },
                  m = (0, s.useRef)(!1),
                  _ = (0, s.useState)(r),
                  E = _[0],
                  g = _[1],
                  p = (0, s.useState)(() => d(r, n, l)),
                  b = p[0],
                  f = p[1];
                return (
                  (0, s.useEffect)(() => {
                    m.current ? f(d(E, n, l)) : (m.current = !0);
                  }, [l, E, n]),
                  (0, s.useEffect)(() => {
                    g(r);
                  }, [r]),
                  (0, s.useEffect)(
                    () => () => {
                      (b.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [b],
                  ),
                  u().createElement(a.Provider, { value: b }, o)
                );
              },
              () => (0, s.useContext)(a),
            ];
          },
          ie = oe()(
            ({ observableModel: e }) => ({
              root: e.object(),
              season: e.primitives(
                ["startTimestamp", "endTimestamp", "serverTimestamp", "state"],
                "season",
              ),
              year: e.primitives(["state"], "year"),
            }),
            ({ externalModel: e }) => ({
              pollServerTime: e.createCallbackNoArgs("season.pollServerTime"),
            }),
          ),
          le = ie[0],
          ce = ie[1];
        let de;
        !(function (e) {
          ((e[(e.Progression = 0)] = "Progression"),
            (e[(e.RankRewards = 1)] = "RankRewards"),
            (e[(e.WeeklyQuests = 2)] = "WeeklyQuests"),
            (e[(e.Leaderboard = 3)] = "Leaderboard"));
        })(de || (de = {}));
        const me = {
            [de.Progression]: "progression",
            [de.RankRewards]: "rankRewards",
            [de.WeeklyQuests]: "weeklyQuests",
            [de.Leaderboard]: "leaderboard",
          },
          _e = { from: { opacity: 0 }, to: { opacity: 1 }, delay: 300, config: { duration: 300 } };
        var Ee = a(3946);
        const ge = oe()(
            ({ observableModel: e }) => {
              const t = { root: e.object() },
                a = e.object("progressionModel.qualificationModel"),
                r = (0, Ee.Om)(
                  () => t.root.get().pageViewId === de.Progression && a.get().isActive,
                );
              return Object.assign({}, t, { computes: { isProgressionInQualification: r } });
            },
            ({ externalModel: e }) => ({
              close: e.createCallbackNoArgs("onClose"),
              openInfoPage: e.createCallbackNoArgs("onInfoPageOpen"),
            }),
          ),
          pe = ge[0],
          be = ge[1];
        function fe(e, t) {
          var a;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (a = e[t]) ? void 0 : a.value;
        }
        const he = fe;
        function Ae(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function ve(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, a, r) => t(null == e ? void 0 : e.value, a, r));
        }
        function Ce(e, t = 0, a = e.length - 1) {
          return {
            [Symbol.iterator]() {
              let r = Math.max(t, 0);
              const n = Math.min(
                a,
                (function (e) {
                  return Math.max(0, e.length - 1);
                })(e),
              );
              return {
                next: function () {
                  if (r > n) return { done: !0, value: null };
                  const t = e[r++];
                  return t ? { value: Ae(t), done: !1 } : { done: !0, value: null };
                },
              };
            },
          };
        }
        function De(e, t) {
          for (let a = 0; a < e.length; a++) {
            const r = Ae(e[a]);
            if (t(r, a, e)) return r;
          }
        }
        function Fe(e, t) {
          for (let a = 0; a < e.length; a++) {
            if (t(he(e, a), a, e)) return a;
          }
        }
        const Be = R.images.comp7.gui.maps.icons.comp7.metaTabs,
          we = (e, t) => {
            const a = me[e];
            return t ? `${Be.$dyn(a)}` : `${Be.small.$dyn(a)}`;
          },
          Se = oe()(
            ({ observableModel: e }) => {
              const t = { root: e.object() },
                a = e.array("items"),
                r = (0, Ee.Om)(
                  (e) => [
                    {
                      id: 0,
                      items: ve(a.get(), ({ id: t, hasNotification: a }) =>
                        Object.assign(
                          { id: t, icon: we(t, e) },
                          a && { notification: { type: "dot" } },
                        ),
                      ),
                    },
                  ],
                  { equals: ae },
                );
              return Object.assign({}, t, { computes: { tabs: r } });
            },
            ({ externalModel: e }) => ({
              changeSidebarTab: e.createCallback((e) => ({ tabId: e }), "onSideBarTabChange"),
            }),
          ),
          Pe = Se[0],
          ye = Se[1],
          Re = (e) => {
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
          };
        var ke = a(7030);
        const Te = {
            base: "Frame_base_af",
            base__small: "Frame_base__small_f0",
            base__medium: "Frame_base__medium_05",
            border: "Frame_border_17",
            border__top: "Frame_border__top_f7",
            border__bottom: "Frame_border__bottom_52",
            arrow: "Frame_arrow_c3",
          },
          xe = u().forwardRef(function (
            { classNames: e, arrowRef: t, size: a = "medium", className: r },
            n,
          ) {
            return u().createElement(
              "div",
              { className: C()(Te.base, Te[`base__${a}`], r), ref: n },
              u().createElement("div", {
                className: C()(
                  Te.border,
                  Te.border__top,
                  null == e ? void 0 : e.border,
                  null == e ? void 0 : e.borderTop,
                ),
              }),
              u().createElement("div", {
                className: C()(
                  Te.border,
                  Te.border__bottom,
                  null == e ? void 0 : e.border,
                  null == e ? void 0 : e.borderBottom,
                ),
              }),
              u().createElement("div", {
                className: C()(Te.arrow, null == e ? void 0 : e.arrow),
                ref: t,
              }),
            );
          }),
          Ne = {
            base: "Tab_base_cd",
            base__small: "Tab_base__small_bf",
            base__medium: "Tab_base__medium_96",
            base__active: "Tab_base__active_7e",
            highlight: "Tab_highlight_b6",
            icon: "Tab_icon_28",
            icon__small: "Tab_icon__small_48",
            icon__medium: "Tab_icon__medium_73",
            notification: "Tab_notification_86",
            notification__symbol: "Tab_notification__symbol_9b",
            notification__small: "Tab_notification__small_92",
            notification__dot: "Tab_notification__dot_51",
            notification__medium: "Tab_notification__medium_e6",
            notification__large: "Tab_notification__large_6b",
          },
          Ie = { mouseEnter: "highlight", click: "play" },
          Le = u().forwardRef(function (
            {
              id: e,
              isActive: t,
              className: a,
              classNames: r,
              sounds: n = Ie,
              notification: s,
              icon: o,
              size: i,
              additionContent: l,
              onClick: c,
              onMouseEnter: d,
              onMouseLeave: m,
              WrapperElement: _,
            },
            E,
          ) {
            const g = (e, a) => {
                !t && n[a] && W(n[a]);
              },
              p = u().createElement(
                "div",
                {
                  className: C()(
                    Ne.base,
                    Ne[`base__${i}`],
                    t && C()(Ne.base__active, null == r ? void 0 : r.activeTab),
                    a,
                  ),
                  onClick: ((e) => () => {
                    (g(0, "click"), null == c || c(e));
                  })(e),
                  onMouseEnter: ((e) => () => {
                    (g(0, "mouseEnter"), null == d || d(e));
                  })(e),
                  onMouseLeave: ((e) => () => {
                    (g(0, "mouseLeave"), null == m || m(e));
                  })(e),
                  ref: t ? E : null,
                },
                u().createElement("div", {
                  className: C()(Ne.highlight, null == r ? void 0 : r.highlight),
                }),
                "function" == typeof o && i
                  ? o(i)
                  : u().createElement("div", {
                      className: C()(Ne.icon, Ne[`icon__${i}`], null == r ? void 0 : r.icon),
                      style: { backgroundImage: `url(${o})` },
                    }),
                l && l({ id: e, isActive: t, size: i }),
                s &&
                  u().createElement(
                    "div",
                    {
                      className: C()(
                        Ne.notification,
                        Ne[`notification__${s.type}`],
                        s.size ? Ne[`notification__${s.size}`] : Ne.notification__medium,
                        null == r ? void 0 : r.notification,
                      ),
                    },
                    "dot" !== s.type && s.value,
                  ),
              );
            return _ ? u().createElement(_, { key: e, id: e }, p) : p;
          }),
          Me = {
            base: "VerticalTabs_base_41",
            title: "VerticalTabs_title_8c",
            group: "VerticalTabs_group_08",
            group__small: "VerticalTabs_group__small_69",
            group__medium: "VerticalTabs_group__medium_68",
          },
          Oe = u().memo(function ({
            active: e,
            tabs: t,
            sounds: a,
            className: r,
            classNames: n,
            size: o = "medium",
            additionContent: l,
            onClick: c,
            onMouseEnter: d,
            onMouseLeave: m,
            WrapperElement: _,
          }) {
            const E = (0, s.useRef)(null),
              g = (0, s.useRef)(null),
              p = (0, s.useRef)(null),
              b = (0, s.useRef)(null),
              f = (0, ke.useSpring)(() => ({
                marginLeft: 0,
                onChange: (e) => {
                  const t = E.current;
                  t && (t.style.marginLeft = `${e.value.marginLeft}rem`);
                },
              }))[1],
              h = (0, ke.useSpring)(() => ({
                opacity: 0,
                onChange: (e) => {
                  const t = E.current;
                  t && (t.style.opacity = `${e.value.opacity}`);
                },
              }))[1],
              A = (0, ke.useSpring)(() => ({
                position: 0,
                onChange: (e) => {
                  const t = g.current;
                  t &&
                    (t.style.transform = `translateY(${e.value.position / i.O.view.getScale()}rem)`);
                },
                onStart: () => {
                  (f.start({
                    from: { marginLeft: 12 },
                    to: { marginLeft: 0 },
                    config: { duration: 50 },
                  }),
                    h.start({
                      from: { opacity: 1 },
                      to: { opacity: 0 },
                      config: { duration: 50 },
                    }));
                },
                onRest: () => {
                  (f.start({
                    from: { marginLeft: 0 },
                    to: { marginLeft: 12 },
                    config: { duration: 150 },
                  }),
                    h.start({
                      from: { opacity: 0 },
                      to: { opacity: 1 },
                      config: { duration: 150 },
                    }));
                },
              }))[1],
              v = (0, s.useCallback)((e) => {
                if (null !== p.current && null !== b.current) {
                  e(p.current.getBoundingClientRect().top - b.current.getBoundingClientRect().top);
                }
              }, []);
            var D, F;
            return (
              (0, s.useEffect)(() => {
                v((e) => {
                  A.start({ position: e, config: { duration: 200 } });
                });
              }, [A, e, v]),
              (0, s.useEffect)(
                () =>
                  Re(() => {
                    v((e) => {
                      A.start({ position: e, immediate: !0 });
                    });
                  }),
                [A, v, o],
              ),
              (D = () => {
                v((e) => {
                  A.start({ position: e, config: { duration: 200 } });
                });
              }),
              (F = [A, v]),
              (0, s.useEffect)(() => {
                let e = () => {};
                const t = () => {
                  (e(), (e = Re(D)));
                };
                return (
                  window.addEventListener("resize", t),
                  () => {
                    (e(), window.removeEventListener("resize", t));
                  }
                );
              }, F),
              u().createElement(
                "div",
                { className: C()(Me.base, r), ref: b },
                t.map(({ id: t, items: r, title: s, groupClassNames: i }) =>
                  u().createElement(
                    "div",
                    {
                      key: t,
                      className: C()(Me.group, Me[`group__${o}`], null == i ? void 0 : i.group),
                    },
                    s &&
                      u().createElement(
                        "div",
                        { className: C()(Me.title, null == i ? void 0 : i.title) },
                        s,
                      ),
                    r.map(({ id: t, icon: r, notification: s }) =>
                      u().createElement(Le, {
                        key: t,
                        id: t,
                        icon: r,
                        notification: s,
                        ref: p,
                        sounds: a,
                        isActive: e === t,
                        size: o,
                        className: null == n ? void 0 : n.tab,
                        classNames: n,
                        additionContent: l,
                        onMouseEnter: d,
                        onMouseLeave: m,
                        onClick: c,
                        WrapperElement: _,
                      }),
                    ),
                  ),
                ),
                u().createElement(xe, {
                  arrowRef: E,
                  ref: g,
                  size: o,
                  className: null == n ? void 0 : n.frame,
                  classNames: n,
                }),
              )
            );
          }),
          He = [
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
        function We(e) {
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
        const $e = (e, t, a = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: X.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: r,
                },
                a,
              ),
            );
          },
          Ue = (e) => {
            let t = e.children,
              a = e.contentId,
              r = e.args,
              n = e.onMouseEnter,
              u = e.onMouseLeave,
              o = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              d = e.ignoreMouseClick,
              m = void 0 !== d && d,
              _ = e.decoratorId,
              E = void 0 === _ ? 0 : _,
              g = e.isEnabled,
              p = void 0 === g || g,
              b = e.targetId,
              f = void 0 === b ? 0 : b,
              h = e.onShow,
              A = e.onHide,
              v = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, He);
            const C = (0, s.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              D = (0, s.useMemo)(
                () =>
                  f ||
                  ((e = 1) => {
                    const t = new Error().stack;
                    let a,
                      r = R.invalid("resId");
                    return (
                      t &&
                        ((a = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== a &&
                          window.subViews[a] &&
                          (r = window.subViews[a].id)),
                      { caller: a, stack: t, resId: r }
                    );
                  })().resId,
                [f],
              ),
              F = (0, s.useCallback)(() => {
                (C.current.isVisible && C.current.timeoutId) ||
                  ($e(a, E, { isMouseEvent: !0, on: !0, arguments: We(r) }, D),
                  h && h(),
                  (C.current.isVisible = !0));
              }, [a, E, r, D, h]),
              B = (0, s.useCallback)(() => {
                if (C.current.isVisible || C.current.timeoutId) {
                  const e = C.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (C.current.timeoutId = 0)),
                    $e(a, E, { on: !1 }, D),
                    C.current.isVisible && A && A(),
                    (C.current.isVisible = !1));
                }
              }, [a, E, D, A]),
              w = (0, s.useCallback)((e) => {
                C.current.isVisible &&
                  ((C.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (C.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(C.current.prevTarget) && B();
                  }, 200)));
              }, []);
            ((0, s.useEffect)(() => {
              const e = C.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, s.useEffect)(() => {
                !1 === p && B();
              }, [p, B]),
              (0, s.useEffect)(
                () => (
                  window.addEventListener("mouseleave", B),
                  () => {
                    (window.removeEventListener("mouseleave", B), B());
                  }
                ),
                [B],
              ));
            return p
              ? (0, s.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((C.current.timeoutId = window.setTimeout(F, c ? 100 : 400)),
                            n && n(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (B(), null == u || u(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === m && B(), null == i || i(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === m && B(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    v,
                  ),
                )
              : t;
            var S;
          },
          ze = ["children", "body", "header", "note", "alert", "args"];
        function Ge() {
          return (
            (Ge =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Ge.apply(this, arguments)
          );
        }
        const je = R.views.common.tooltip_window.simple_tooltip_content,
          qe = (e) => {
            let t = e.children,
              a = e.body,
              r = e.header,
              n = e.note,
              o = e.alert,
              i = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, ze);
            const c = (0, s.useMemo)(() => {
              const e = Object.assign({}, i, { body: a, header: r, note: n, alert: o });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [o, a, r, n, i]);
            return u().createElement(
              Ue,
              Ge(
                {
                  contentId:
                    ((d = null == i ? void 0 : i.hasHtmlContent),
                    d ? je.SimpleTooltipHtmlContent("resId") : je.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var d;
          },
          Ve = R.strings.comp7.sidebar.tabs.tooltip,
          Xe = ({ children: e, id: t }) => {
            const a = me[t];
            return u().createElement(
              qe,
              { header: `${Ve.header.$dyn(a)}`, body: `${Ve.body.$dyn(a)}` },
              e,
            );
          },
          Qe = { icon: "Tabs_icon_78" },
          Ye = (0, q.Pi)(({ pageView: e, className: t }) => {
            const a = ye(),
              r = a.model,
              n = a.controls,
              o = P().mediaSize >= B.Medium,
              i = (0, s.useCallback)((e) => n.changeSidebarTab(e), [n]),
              l = r.computes.tabs(o);
            return u().createElement(Oe, {
              tabs: l,
              onClick: i,
              active: e,
              size: o ? "medium" : "small",
              className: t,
              classNames: Qe,
              WrapperElement: Xe,
            });
          }),
          Ke = "Spinner_base_87",
          Ze = "Spinner_caption_cf",
          Je = "Spinner_gear_c4",
          et = "Spinner_logo_bf",
          tt = ({ message: e, className: t, classNames: a }) =>
            u().createElement(
              "div",
              { className: C()(Ke, t) },
              e &&
                u().createElement("div", { className: C()(Ze, null == a ? void 0 : a.caption) }, e),
              u().createElement("div", { className: C()(Je, null == a ? void 0 : a.gear) }),
              u().createElement("div", { className: C()(et, null == a ? void 0 : a.logo) }),
            ),
          at = 50;
        let rt;
        !(function (e) {
          ((e[(e.Initial = 0)] = "Initial"),
            (e[(e.Success = 1)] = "Success"),
            (e[(e.Error = 2)] = "Error"));
        })(rt || (rt = {}));
        const nt = "Heading_base_74",
          st = ({ children: e, className: t }) =>
            u().createElement("div", { className: C()(nt, t) }, e),
          ut = (e, t) => {
            let a;
            const r = setTimeout(() => {
              a = e();
            }, t);
            return () => {
              ("function" == typeof a && a(), clearTimeout(r));
            };
          };
        let ot;
        function it(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        function lt(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const a = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(a, -a)]);
          });
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(ot || (ot = {}));
        const ct = (e, t, a) => {
            if (a % 2) {
              const a = e.pop();
              return [...e, a + t];
            }
            return [...e, t];
          },
          dt = (e, t, a) => {
            if (0 === a) return [t];
            if (a % 2) return [...e, " " === t ? " " : t];
            {
              const a = e.pop();
              return [...e, a + t];
            }
          },
          mt = (e, t, a = ot.left) => e.split(t).reduce(a === ot.left ? ct : dt, []),
          _t = (() => {
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
          Et = ["zh_cn", "zh_sg", "zh_tw"],
          gt = (e, t = ot.left) => {
            const a = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Et.includes(a)
              ? _t(e)
              : ((e, t = ot.left) => {
                  let a = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (mt(n, /( )/, t).forEach((e) => (a = a.concat(mt(e, r, ot.left)))), a);
                })(e, t);
          };
        let pt;
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
        })(pt || (pt = {}));
        const bt = 60,
          ft = 3600,
          ht = 86400;
        Date.now();
        const At = (0, s.memo)(({ datetime: e, format: t = pt.SHORT_DATE, localize: a = !0 }) =>
            ((e, t, a) => {
              switch (t) {
                case pt.SHORT_DATE:
                  return a
                    ? X.Z5.getDateFormat(e, X.kH.SHORT_FORMAT)
                    : X.cy.getTimeFormat("%d.%m.%y", e, !0);
                case pt.SHORT_TIME:
                  return a
                    ? X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)
                    : X.cy.getTimeFormat("%I:%M %p", e, !0);
                case pt.SHORT_DATE_TIME:
                  return a
                    ? `${X.Z5.getDateFormat(e, X.kH.SHORT_FORMAT)}, ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                    : X.cy.getTimeFormat("%d.%m.%y, %I:%M %p", e, !0);
                case pt.FULL_DATE:
                  return a
                    ? X.Z5.getDateFormat(e, X.kH.LONG_FORMAT)
                    : X.cy.getTimeFormat("%B %d, %Y", e, !0);
                case pt.FULL_DATE_TIME:
                  return a
                    ? `${X.Z5.getDateFormat(e, X.kH.LONG_FORMAT)}, ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                    : X.cy.getTimeFormat("%B %d, %Y, %I:%M %p", e, !0);
                case pt.MONTH:
                  return X.cy.getTimeFormat("%B", e, !0);
                case pt.MONTH_DATE:
                  return X.cy.getTimeFormat("%B %e", e, !0);
                case pt.DATE_MONTH:
                  return X.cy.getTimeFormat("%e %B", e, !0);
                case pt.MONTH_YEAR:
                  return X.cy.getTimeFormat("%B %Y", e, !0);
                case pt.WEEK_DAY:
                  return X.cy.getTimeFormat("%A", e, !0);
                case pt.WEEK_DAY_TIME:
                  return a
                    ? `${X.cy.getTimeFormat("%A", e, !0)} ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                    : X.cy.getTimeFormat("%A, %I:%M %p", e, !0);
                case pt.YEAR:
                  return X.cy.getTimeFormat("%Y", e, !0);
                case pt.DATE_YEAR:
                  return X.cy.getTimeFormat("%d, %Y", e, !0);
              }
            })(e, t, a),
          ),
          vt = "FormatText_base_d0",
          Ct = ({ binding: e, text: t = "", classMix: a, alignment: r = ot.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : u().createElement(
                  s.Fragment,
                  null,
                  t.split("\n").map((t, n) =>
                    u().createElement(
                      "div",
                      { className: C()(vt, a), key: `${t}-${n}` },
                      ((e, t, a) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (a && e in a ? a[e] : gt(e, t))))(t, r, e).map((e, t) =>
                        u().createElement(s.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                ),
          Dt = ["children"];
        function Ft() {
          return (
            (Ft =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Ft.apply(this, arguments)
          );
        }
        const Bt = (e) => {
            let t = e.children,
              a = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, Dt);
            return u().createElement(
              Ue,
              Ft(
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
          wt = (e) => {
            const t = Math.floor(e);
            return {
              totalSecondsLeft: t,
              seconds: Math.floor(t % 60),
              minutes: Math.floor(t / 60) % 60,
              hours: Math.floor((t / 3600) % 24),
              totalDays: Math.floor(t / 86400),
            };
          },
          St = "ActiveSeasonState_base_55",
          Pt = "ActiveSeasonState_calendarIcon_df",
          yt = "ActiveSeasonState_divider_5b",
          Rt = R.strings.comp7.season,
          kt = (e, t) => ({
            startDate: u().createElement(At, { datetime: e, format: pt.SHORT_DATE }),
            endDate: u().createElement(At, { datetime: t, format: pt.SHORT_DATE }),
          }),
          Tt = (e, t, a) => {
            const r = t - a,
              n = ((e, t) => wt(e - t))(t, a);
            return r >= 604800
              ? u().createElement(Ct, { text: Rt.range(), binding: kt(e, t) })
              : r >= ht
                ? u().createElement(Ct, { text: Rt.daysLeft(), binding: n })
                : r >= ft
                  ? u().createElement(Ct, { text: Rt.hoursLeft(), binding: n })
                  : r >= bt
                    ? u().createElement(Ct, { text: Rt.minutesLeft(), binding: n })
                    : r >= 1
                      ? u().createElement(Ct, { text: Rt.secondsLeft(), binding: n })
                      : void 0;
          },
          xt = ({
            startTimestamp: e,
            endTimestamp: t,
            currentTimestamp: a,
            tooltipId: r = "",
            hasSeasonName: n = !0,
          }) =>
            u().createElement(
              Bt,
              { args: { tooltipId: r }, isEnabled: Boolean(r) },
              u().createElement(
                "div",
                { className: St },
                u().createElement("div", { className: Pt }),
                n &&
                  u().createElement(
                    u().Fragment,
                    null,
                    Rt.name(),
                    u().createElement("div", { className: yt }),
                  ),
                Tt(e, t, a),
              ),
            ),
          Nt = "ScheduleSubheading_base_f7",
          It = (0, q.Pi)(({ className: e, hasSeasonName: t = !0 }) => {
            const a = ce(),
              r = a.model,
              n = a.controls,
              o = r.season.startTimestamp.get(),
              i = r.season.endTimestamp.get(),
              l = r.season.serverTimestamp.get();
            return (
              (function (e, t, a) {
                (0, s.useEffect)(() => {
                  if (!(e >= t))
                    return ut(() => {
                      a();
                    }, 950);
                }, [t, a, e]);
              })(l, i, n.pollServerTime),
              u().createElement(
                "div",
                { className: C()(Nt, e) },
                l < i
                  ? u().createElement(xt, {
                      startTimestamp: o,
                      endTimestamp: i,
                      currentTimestamp: l,
                      tooltipId: r.root.get().tooltipId,
                      hasSeasonName: t,
                    })
                  : R.strings.comp7.season.over(),
              )
            );
          }),
          Lt = {
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
        let Mt, Ot;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(Mt || (Mt = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(Ot || (Ot = {})));
        const Ht = ({
          children: e,
          size: t,
          isFocused: a,
          type: r,
          disabled: n,
          mixClass: o,
          soundHover: i,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: d,
          onMouseDown: m,
          onMouseUp: _,
          onMouseLeave: E,
          onClick: g,
        }) => {
          const p = (0, s.useRef)(null),
            b = (0, s.useState)(a),
            f = b[0],
            h = b[1],
            A = (0, s.useState)(!1),
            v = A[0],
            D = A[1],
            F = (0, s.useState)(!1),
            B = F[0],
            w = F[1],
            S = (0, s.useCallback)(() => {
              n || (p.current && (p.current.focus(), h(!0)));
            }, [n]),
            P = (0, s.useCallback)(
              (e) => {
                f && null !== p.current && !p.current.contains(e.target) && h(!1);
              },
              [f],
            ),
            y = (0, s.useCallback)(
              (e) => {
                n || (g && g(e));
              },
              [n, g],
            ),
            k = (0, s.useCallback)(
              (e) => {
                n || (null !== i && W(i), c && c(e), w(!0));
              },
              [n, i, c],
            ),
            T = (0, s.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            x = (0, s.useCallback)(
              (e) => {
                n || (_ && _(e), D(!1));
              },
              [n, _],
            ),
            N = (0, s.useCallback)(
              (e) => {
                n || (null !== l && W(l), m && m(e), a && S(), D(!0));
              },
              [n, l, m, S, a],
            ),
            I = (0, s.useCallback)(
              (e) => {
                n || (E && E(e), D(!1));
              },
              [n, E],
            ),
            L = C()(
              Lt.base,
              Lt[`base__${r}`],
              {
                [Lt.base__disabled]: n,
                [Lt[`base__${t}`]]: t,
                [Lt.base__focus]: f,
                [Lt.base__highlightActive]: v,
                [Lt.base__firstHover]: B,
              },
              o,
            ),
            M = C()(Lt.state, Lt.state__default);
          return (
            (0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", P),
                () => {
                  document.removeEventListener("mousedown", P);
                }
              ),
              [P],
            ),
            (0, s.useEffect)(() => {
              h(a);
            }, [a]),
            u().createElement(
              "div",
              {
                ref: p,
                className: L,
                onMouseEnter: k,
                onMouseMove: T,
                onMouseUp: x,
                onMouseDown: N,
                onMouseLeave: I,
                onClick: y,
              },
              r !== Mt.ghost &&
                u().createElement(
                  u().Fragment,
                  null,
                  u().createElement("div", { className: Lt.back }),
                  u().createElement("span", { className: Lt.texture }),
                ),
              u().createElement(
                "span",
                { className: M },
                u().createElement("span", { className: Lt.stateDisabled }),
                u().createElement("span", { className: Lt.stateHighlightHover }),
                u().createElement("span", { className: Lt.stateHighlightActive }),
              ),
              u().createElement(
                "span",
                { className: Lt.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Ht.defaultProps = {
          type: Mt.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Wt = (0, s.memo)(Ht),
          $t = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? ve(e, (e) => ("object" == typeof e ? $t(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? $t(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? $t(t) : t]),
                    )
              : e,
          Ut = (e) => $t(e),
          zt = (e, t) =>
            Object.keys(e).length === Object.keys(t).length &&
            Object.keys(e).every(
              (a) => Object.prototype.hasOwnProperty.call(t, a) && e[a] === t[a],
            ),
          Gt = oe()(
            ({ observableModel: e, mode: t }) => {
              const a = { root: e.object() },
                r = e.array("items"),
                n = e.array("divisions"),
                s = (0, Ee.Om)(
                  () =>
                    Ut(n.get())
                      .sort((e, t) => e.name - t.name)
                      .reduce((e, t) => {
                        const a = null == t ? void 0 : t.rankId;
                        return ((a && e[a]) || (e[a] = []), e[a].push(t), e);
                      }, {}),
                  { equals: ae },
                ),
                u = (0, Ee.Om)(
                  () =>
                    Ut(n.get()).reduce((e, t) => {
                      const a = null == t ? void 0 : t.firstMemberPosition;
                      return (a >= 0 && (e[a] = t), e);
                    }, {}),
                  { equals: ae },
                ),
                o = (0, Ee.Om)(() => r.get().length),
                i = (0, Ee.Om)(
                  (e) => {
                    const t = fe(r.get(), e);
                    if (!t) throw new Error(`leaderboard item with index ${e} was not found`);
                    return Object.assign({}, t);
                  },
                  { equals: ae },
                ),
                l = (0, Ee.Om)(() => {
                  const e = a.root.get(),
                    t = e.state,
                    r = e.leaderboardUpdateTimestamp;
                  return t !== rt.Initial && r > 0;
                }),
                c = (0, Ee.Om)(() => o() > 0),
                d = (0, Ee.Om)((e) => a.root.get().ownSpaID === i(e).spaID),
                m = (0, Ee.Om)(
                  () => ({ first: c() ? i(0).position : 0, last: c() ? i(0).position + o() : 0 }),
                  { equals: zt },
                ),
                _ = (0, Ee.Om)(
                  (e) => {
                    const t = Math.ceil(a.root.get().recordsCount / e);
                    return {
                      amount: t,
                      hasPagination: t > 1,
                      active: Math.floor(m().first / e) + 1,
                    };
                  },
                  { equals: zt },
                ),
                E = (0, Ee.Om)((e) => i(e).position < 3),
                g = (0, Ee.Om)(() => -1 === a.root.get().personalPosition);
              return Object.assign(
                {},
                a,
                {
                  computes: {
                    leaderboardItemsLength: o,
                    leaderboardItem: i,
                    hasUpdateInfo: l,
                    hasRecords: c,
                    isPersonalRow: d,
                    hasPositionIcon: E,
                    isDefaultPersonalPosition: g,
                    pages: _,
                    pagePositions: m,
                    getRankTabs: s,
                    getDivisionsDividers: u,
                  },
                },
                "mocks" === t && { internal: { items: r } },
              );
            },
            ({ externalModel: e }) => ({
              refresh: e.createCallbackNoArgs("onRefresh"),
              getTableRecords: e.createCallback(
                (e, t) => ({ limit: e, offset: t }),
                "getTableRecords",
              ),
            }),
          ),
          jt = Gt[0],
          qt = Gt[1],
          Vt = "ErrorState_base_eb",
          Xt = "ErrorState_titleContainer_ca",
          Qt = "ErrorState_alertIcon_76",
          Yt = "ErrorState_title_c1",
          Kt = "ErrorState_description_d9",
          Zt = "ErrorState_buttonWrapper_5e",
          Jt = "ErrorState_button_23",
          ea = R.strings.comp7.leaderboard.error,
          ta = (0, q.Pi)(({ className: e }) => {
            const t = qt(),
              a = t.model,
              r = t.controls,
              n = a.root.get().isLoading,
              s = P().mediaSize;
            return u().createElement(
              "div",
              { className: C()(Vt, e) },
              u().createElement(
                "div",
                { className: Xt },
                u().createElement("div", { className: Qt }),
                u().createElement("div", { className: Yt }, ea.title()),
              ),
              u().createElement("div", { className: Kt }, ea.description()),
              u().createElement(
                "div",
                { className: Zt },
                u().createElement(
                  Wt,
                  {
                    type: Mt.secondary,
                    disabled: n,
                    size: ((o = s), o >= B.Medium ? Ot.medium : Ot.small),
                    mixClass: Jt,
                    onClick: r.refresh,
                  },
                  ea.buttonText(),
                ),
              ),
            );
            var o;
          });
        var aa = a(9887),
          ra = a.n(aa);
        const na = ["xl", "lg", "md", "sm", "xs"],
          sa = (e) => e.includes("_") && ((e) => na.includes(e))(e.split("_").at(-1)),
          ua = [B.ExtraLarge, B.Large, B.Medium, B.Small, B.ExtraSmall],
          oa = (e, t) =>
            Object.keys(e).reduce((a, r) => {
              if (r in a) return a;
              if (sa(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in a) return a;
                const s = ua.indexOf(t),
                  u = (-1 !== s ? na.slice(s) : [])
                    .map((e) => n + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  o = u ? e[u] : void 0;
                return ((a[n] = void 0 !== o ? o : e[n]), a);
              }
              const n = e[r];
              return (
                void 0 === n ||
                  ((e, t) => na.some((a) => void 0 !== t[`${e}_${a}`]))(r, e) ||
                  (a[r] = n),
                a
              );
            }, {}),
          ia = (e, t = oa) => {
            const a = (
              (e, t = oa) =>
              (a) => {
                const r = P().mediaSize,
                  n = (0, s.useMemo)(() => t(a, r), [a, r]);
                return u().createElement(e, n);
              }
            )(e, t);
            return u().memo((t) =>
              Object.keys(t).some((e) => sa(e) && void 0 !== t[e])
                ? u().createElement(a, t)
                : u().createElement(e, t),
            );
          },
          la = {
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
          ca = [
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
        function da() {
          return (
            (da =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            da.apply(this, arguments)
          );
        }
        Object.keys(ra());
        const ma = {
            XL: { mt: la.mt__XL, mr: la.mr__XL, mb: la.mb__XL, ml: la.ml__XL },
            LG: { mt: la.mt__LG, mr: la.mr__LG, mb: la.mb__LG, ml: la.ml__LG },
            MDp: { mt: la.mt__MDp, mr: la.mr__MDp, mb: la.mb__MDp, ml: la.ml__MDp },
            MD: { mt: la.mt__MD, mr: la.mr__MD, mb: la.mb__MD, ml: la.ml__MD },
            SMp: { mt: la.mt__SMp, mr: la.mr__SMp, mb: la.mb__SMp, ml: la.ml__SMp },
            SM: { mt: la.mt__SM, mr: la.mr__SM, mb: la.mb__SM, ml: la.ml__SM },
            XS: { mt: la.mt__XS, mr: la.mr__XS, mb: la.mb__XS, ml: la.ml__XS },
          },
          _a = (Object.keys(ma), ["mt", "mr", "mb", "ml"]),
          Ea = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          ga = ia((e) => {
            let t = e.className,
              a = e.width,
              r = e.height,
              n = e.m,
              o = e.mt,
              i = void 0 === o ? n : o,
              l = e.mr,
              c = void 0 === l ? n : l,
              d = e.mb,
              m = void 0 === d ? n : d,
              _ = e.ml,
              E = void 0 === _ ? n : _,
              g = e.column,
              p = e.row,
              b = e.flexDirection,
              f = void 0 === b ? (g ? "column" : p && "row") || void 0 : b,
              h = e.flexStart,
              A = e.center,
              v = e.flexEnd,
              D = e.spaceBetween,
              F = e.spaceAround,
              B = e.justifyContent,
              w =
                void 0 === B
                  ? (h ? "flex-start" : A && "center") ||
                    (v && "flex-end") ||
                    (D && "space-between") ||
                    (F && "space-around") ||
                    void 0
                  : B,
              S = e.alignItems,
              P =
                void 0 === S
                  ? (h ? "flex-start" : A && "center") || (v && "flex-end") || void 0
                  : S,
              y = e.alignSelf,
              R = e.wrap,
              k = e.flexWrap,
              T = void 0 === k ? (R ? "wrap" : void 0) : k,
              x = e.grow,
              N = e.shrink,
              I = e.flex,
              L = void 0 === I ? (x || N ? `${x ? 1 : 0} ${N ? 1 : 0} auto` : void 0) : I,
              M = e.style,
              O = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, ca);
            const W = (0, s.useMemo)(() => {
                const e = { mt: i, mr: c, mb: m, ml: E },
                  t = ((e) =>
                    _a.reduce((t, a) => {
                      const r = e[a];
                      return r && "number" != typeof r ? t.concat(ma[!0 === r ? "MD" : r][a]) : t;
                    }, []))(e),
                  n = ((e) =>
                    _a.reduce((t, a) => {
                      const r = e[a];
                      return ("number" == typeof r && (t[Ea[a]] = r + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, M, n, {
                    width: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: L,
                    alignSelf: y,
                    display: f || P ? "flex" : void 0,
                    flexDirection: f,
                    flexWrap: T,
                    justifyContent: w,
                    alignItems: P,
                  }),
                  computedClassNames: t,
                };
              }, [a, r, i, c, m, E, M, L, y, f, T, w, P]),
              $ = W.computedStyle,
              U = W.computedClassNames;
            return u().createElement(
              "div",
              da({ className: C()(la.base, ...U, t), style: $ }, H),
              O,
            );
          });
        var pa = a(3532),
          ba = a.n(pa);
        const fa = {
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
          ha = [
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
        function Aa() {
          return (
            (Aa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Aa.apply(this, arguments)
          );
        }
        Object.keys(ra());
        const va = Object.keys(ba()),
          Ca = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Da = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Fa = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Ba = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          wa =
            (Object.keys(Ba),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ca,
              "heading-H36": Ca,
              "heading-H28": Da,
              "heading-H24": Da,
              "heading-H24R": Da,
              "heading-H22": Da,
              "heading-H20R": Da,
              "heading-H18": Da,
              "heading-H15": Fa,
              "heading-H14": Fa,
              "paragraph-P24": Da,
              "paragraph-P18": Da,
              "paragraph-P16": Da,
              "paragraph-P14": Fa,
              "paragraph-P12": Fa,
              "paragraph-P10": Fa,
            }),
          Sa =
            (Object.keys(wa),
            (e) =>
              e
                ? ((e) => va.includes(e))(e)
                  ? { colorClassName: fa[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Pa = ia((e) => {
            let t = e.text,
              a = e.variant,
              r = e.className,
              n = e.color,
              o = e.m,
              i = e.mt,
              l = void 0 === i ? o : i,
              c = e.mr,
              d = void 0 === c ? o : c,
              m = e.mb,
              _ = void 0 === m ? o : m,
              E = e.ml,
              g = void 0 === E ? o : E,
              p = e.style,
              b = e.format,
              f = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, ha);
            const h = (0, s.useMemo)(() => {
                const e = Sa(n),
                  t = e.colorClassName,
                  a = e.colorStyle,
                  r = void 0 === a ? {} : a;
                return { computedStyle: Object.assign({}, p, r), colorClassName: t };
              }, [p, n]),
              A = h.computedStyle,
              v = h.colorClassName;
            return u().createElement(
              ga,
              Aa(
                {
                  className: C()(fa.base, a && fa[a], v, r),
                  style: A,
                  mt: !0 === l ? wa[a || "paragraph-P16"].mt : l,
                  mr: !0 === d ? wa[a || "paragraph-P16"].mr : d,
                  mb: !0 === _ ? wa[a || "paragraph-P16"].mb : _,
                  ml: !0 === g ? wa[a || "paragraph-P16"].ml : g,
                },
                f,
              ),
              void 0 !== b ? u().createElement(Ct, Aa({}, b, { text: t })) : t,
            );
          }),
          ya =
            (lt(R.strings.comp7.lastUpdateNote.lastBestUserPoints.description(), { count: 15 }),
            "LastUpdateNote_base_7f"),
          Ra = "LastUpdateNote_infoIcon_5c",
          ka = "LastUpdateNote_lineDivider_2c";
        let Ta;
        !(function (e) {
          ((e[(e.ICON = 0)] = "ICON"), (e[(e.LINE = 1)] = "LINE"));
        })(Ta || (Ta = {}));
        const xa = R.strings.comp7.lastUpdateNote,
          Na = ({
            timestamp: e,
            className: t,
            classNames: a,
            dateTimeFormat: r = pt.SHORT_TIME,
            dividerType: n = Ta.ICON,
          }) =>
            u().createElement(
              "div",
              { className: C()(ya, t) },
              u().createElement(Pa, {
                text: xa.info(),
                format: { binding: { date: u().createElement(At, { datetime: e, format: r }) } },
              }),
              n === Ta.ICON &&
                u().createElement(
                  qe,
                  { body: xa.tooltip.info() },
                  u().createElement("div", { className: C()(Ra, null == a ? void 0 : a.icon) }),
                ),
              n === Ta.LINE &&
                u().createElement("div", { className: C()(ka, null == a ? void 0 : a.line) }),
            );
        class Ia extends u().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = X.B3.GOLD;
            else e = X.B3.INTEGRAL;
            const t = X.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        Ia.defaultProps = { format: "integral" };
        const La = {
            blackReal: "FormatTextWithColorTags_blackReal_3c",
            whiteReal: "FormatTextWithColorTags_whiteReal_8a",
            white: "FormatTextWithColorTags_white_16",
            whiteOrange: "FormatTextWithColorTags_whiteOrange_18",
            whiteSpanish: "FormatTextWithColorTags_whiteSpanish_10",
            par: "FormatTextWithColorTags_par_ca",
            parSecondary: "FormatTextWithColorTags_parSecondary_8d",
            parTertiary: "FormatTextWithColorTags_parTertiary_a3",
            red: "FormatTextWithColorTags_red_60",
            redDark: "FormatTextWithColorTags_redDark_03",
            yellow: "FormatTextWithColorTags_yellow_ad",
            orange: "FormatTextWithColorTags_orange_e4",
            cream: "FormatTextWithColorTags_cream_cd",
            brown: "FormatTextWithColorTags_brown_c8",
            greenBright: "FormatTextWithColorTags_greenBright_f0",
            green: "FormatTextWithColorTags_green_c5",
            greenDark: "FormatTextWithColorTags_greenDark_af",
            blueBooster: "FormatTextWithColorTags_blueBooster_ac",
            blueTeamkiller: "FormatTextWithColorTags_blueTeamkiller_6f",
            cred: "FormatTextWithColorTags_cred_4e",
            gold: "FormatTextWithColorTags_gold_90",
            bond: "FormatTextWithColorTags_bond_71",
            prom: "FormatTextWithColorTags_prom_dd",
          },
          Ma =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          Oa = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          Ha = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          Wa = (0, s.memo)(({ text: e, binding: t, classMix: a }) => {
            const r = (0, s.useCallback)((e) => ({ color: `#${e}` }), []),
              n = (0, s.useMemo)(() => t || {}, [t]);
            let o = Ma.exec(e),
              i = e,
              l = 0;
            for (; o;) {
              const a = o[0],
                s = Oa.exec(a),
                c = Ha.exec(a),
                d = o[1];
              if (s && c) {
                const e = s[0],
                  o = e + l++ + e;
                ((i = i.replace(a, `%(${o})`)),
                  (n[o] = La[e]
                    ? u().createElement(
                        "span",
                        { className: La[e] },
                        u().createElement(Ct, { text: d, binding: t }),
                      )
                    : u().createElement(
                        "span",
                        { style: r(e) },
                        u().createElement(Ct, { text: d, binding: t }),
                      )));
              }
              o = Ma.exec(e);
            }
            return u().createElement(Ct, { text: i, classMix: a, binding: n });
          }),
          $a = "NoRecordsState_base_9b",
          Ua = "NoRecordsState_imageContainer_13",
          za = "NoRecordsState_image_fe",
          Ga = "NoRecordsState_title_f4",
          ja = "NoRecordsState_subtitle_5b",
          qa = R.strings.comp7.leaderboard.noRecords,
          Va = (0, q.Pi)(() => {
            const e = qt().model.root.get().from;
            return u().createElement(
              "div",
              { className: $a },
              u().createElement(
                "div",
                { className: Ua },
                u().createElement("div", { className: za }),
              ),
              u().createElement("div", { className: Ga }, qa.title()),
              u().createElement(Wa, {
                text: qa.subtitle(),
                binding: { pointsCount: u().createElement(Ia, { value: e }) },
                classMix: ja,
              }),
            );
          }),
          Xa = (e, t) => e - (e % t),
          Qa = (e, t, a) => (a < e ? e : a > t ? t : a);
        function Ya(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Ka(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return Ka(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Ka(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, r = new Array(t); a < t; a++) r[a] = e[a];
          return r;
        }
        const Za = [];
        function Ja(e) {
          const t = (0, s.useRef)(e);
          return (
            (0, s.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, s.useCallback)((...e) => (0, t.current)(...e), Za)
          );
        }
        function er(e, t, a) {
          const r = (0, s.useMemo)(
            () =>
              (function (e, t, a, r) {
                let n,
                  s = !1,
                  u = 0;
                function o() {
                  n && clearTimeout(n);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - u;
                  function d() {
                    ((u = Date.now()), a.apply(l, i));
                  }
                  s ||
                    (r && !n && d(),
                    o(),
                    void 0 === r && c > e
                      ? d()
                      : !0 !== t &&
                        (n = setTimeout(
                          r
                            ? function () {
                                n = void 0;
                              }
                            : d,
                          void 0 === r ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((r = a), (a = t), (t = void 0)),
                  (i.cancel = function () {
                    (o(), (s = !0));
                  }),
                  i
                );
              })(a, e),
            t,
          );
          return ((0, s.useEffect)(() => r.cancel, [r]), r);
        }
        let tr;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(tr || (tr = {}));
        const ar = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          rr = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: a,
            getDirection: r,
            getWrapperSize: n,
            triggerMouseMoveOnUpdate: u = !1,
          }) => {
            const o = (e, a) => {
              const r = t(e),
                n = r[0],
                s = r[1];
              return Qa(n, s, a);
            };
            return (l = {}) => {
              const c = l.settings,
                d = void 0 === c ? ar : c,
                m = (0, s.useRef)(null),
                _ = (0, s.useRef)(null),
                E = (() => {
                  const e = (0, s.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    a = (e, a) => {
                      t(e).set(a, a);
                    },
                    r = (e, a) => {
                      t(e).delete(a);
                    },
                    n = (e, ...a) => {
                      for (var r, n = Ya(t(e).values()); !(r = n()).done;) (0, r.value)(...a);
                    };
                  return (0, s.useMemo)(() => ({ on: a, off: r, trigger: n }), []);
                })(),
                g = er(
                  () => {
                    i.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                p = (0, ke.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = m.current;
                    t && (a(t, e), E.trigger("change", e), u && g());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                b = p[0],
                f = p[1],
                h = (0, s.useCallback)(
                  (e, t, a) => {
                    var r;
                    const n = b.scrollPosition.get(),
                      s = (null != (r = b.scrollPosition.goal) ? r : 0) - n;
                    return o(e, t * a + s + n);
                  },
                  [b.scrollPosition],
                ),
                A = (0, s.useCallback)(
                  (e, { immediate: t = !1, reset: a = !0 } = {}) => {
                    const r = m.current;
                    r &&
                      f.start({
                        scrollPosition: o(r, e),
                        immediate: t,
                        reset: a,
                        config: d.animationConfig,
                        from: { scrollPosition: o(r, b.scrollPosition.get()) },
                      });
                  },
                  [f, d.animationConfig, b.scrollPosition],
                ),
                v = (0, s.useCallback)(
                  (e) => {
                    const t = m.current,
                      a = _.current;
                    if (!t || !a) return;
                    const r = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return n(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(a, d.step),
                      s = h(t, e, r);
                    A(s);
                  },
                  [A, h, d.step],
                ),
                C = (0, s.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && v(r(e)),
                      m.current && E.trigger("mouseWheel", e, b.scrollPosition, t(m.current)));
                  },
                  [b.scrollPosition, v, E],
                ),
                D = ((e, t = []) => {
                  const a = (0, s.useRef)(),
                    r = (0, s.useCallback)((...t) => {
                      (a.current && a.current(), (a.current = e(...t)));
                    }, t);
                  return (
                    (0, s.useEffect)(
                      () => () => {
                        a.current && a.current();
                      },
                      [r],
                    ),
                    r
                  );
                })(
                  () =>
                    Re(() => {
                      const e = m.current;
                      e &&
                        (A(o(e, b.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [A, b.scrollPosition.goal],
                ),
                F = Ja(() => {
                  const e = m.current;
                  if (!e) return;
                  const t = o(e, b.scrollPosition.goal);
                  (t !== b.scrollPosition.goal && A(t, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", D),
                  () => {
                    window.removeEventListener("resize", D);
                  }
                ),
                [D],
              );
              const B = (0, s.useCallback)((e) => E.trigger("isThumbDraggingChanged", e), [E]);
              return (0, s.useMemo)(
                () => ({
                  getWrapperSize: () => (_.current ? n(_.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? t(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: d.step.clampedArrowStepTimeout,
                  clampPosition: o,
                  handleMouseWheel: C,
                  applyScroll: A,
                  applyStepTo: v,
                  contentRef: m,
                  wrapperRef: _,
                  scrollPosition: f,
                  animationScroll: b,
                  recalculateContent: F,
                  handleIsThumbDragging: B,
                  events: { on: E.on, off: E.off },
                }),
                [b.scrollPosition, A, v, B, E.off, E.on, F, C, f, d.step.clampedArrowStepTimeout],
              );
            };
          },
          nr = rr({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? tr.Next : tr.Prev),
          }),
          sr = {
            "--pageContentWidth": "78vw",
            base: "CurrentPositionPanel_base_92",
            base__active: "CurrentPositionPanel_base__active_8c",
            base__highlight: "CurrentPositionPanel_base__highlight_f1",
            marker: "CurrentPositionPanel_marker_0b",
            cell: "CurrentPositionPanel_cell_be",
            cell__highlightMarker: "CurrentPositionPanel_cell__highlightMarker_9f",
            cell__order: "CurrentPositionPanel_cell__order_be",
            cell__currentPosition: "CurrentPositionPanel_cell__currentPosition_c5",
            cell__battles: "CurrentPositionPanel_cell__battles_8f",
            cell__score: "CurrentPositionPanel_cell__score_d2",
            screwIcon: "CurrentPositionPanel_screwIcon_8f",
            screwIcon__left: "CurrentPositionPanel_screwIcon__left_cb",
            screwIcon__right: "CurrentPositionPanel_screwIcon__right_6e",
          };
        let ur;
        !(function (e) {
          ((e.None = "None"), (e.Active = "Active"));
        })(ur || (ur = {}));
        const or = R.strings.comp7.leaderboard.currentPosition,
          ir = R.strings.comp7.leaderboard.table.tooltip,
          lr = R.views.lobby.comp7.tooltips.LeaderboardRewardTooltip("resId"),
          cr = { [ur.None]: "none", [ur.Active]: "active" },
          dr = (0, q.Pi)(({ state: e, height: t, onClick: a, className: r }) => {
            const n = qt().model.root.get(),
              s = n.personalPosition,
              o = n.personalBattlesCount,
              i = n.personalScore,
              l = s < 10,
              c = s + 1,
              d = C()(sr.base, sr[`base__${cr[e]}`], l && sr.base__highlight, r);
            return u().createElement(
              "div",
              { className: d, onClick: a, style: { "--height": t ? `${t}rem` : "auto" } },
              u().createElement("div", { className: C()(sr.screwIcon, sr.screwIcon__left) }),
              {
                [ur.None]: u().createElement("div", { className: C()(sr.cell) }, or.none()),
                [ur.Active]: u().createElement(
                  u().Fragment,
                  null,
                  u().createElement(
                    Ue,
                    { contentId: lr, args: { place: c }, isEnabled: l },
                    u().createElement(
                      "div",
                      { className: C()(sr.cell, sr.cell__highlightMarker) },
                      l && u().createElement("div", { className: sr.marker }),
                    ),
                  ),
                  u().createElement(
                    qe,
                    { header: ir.order.header(), body: ir.order.body() },
                    u().createElement("div", { className: C()(sr.cell, sr.cell__order) }, c),
                  ),
                  u().createElement(
                    "div",
                    { className: C()(sr.cell, sr.cell__currentPosition) },
                    or.body(),
                  ),
                  u().createElement(
                    qe,
                    { header: ir.battlesCount.header(), body: ir.battlesCount.body() },
                    u().createElement(
                      "div",
                      { className: C()(sr.cell, sr.cell__battles) },
                      u().createElement(Ia, { value: o }),
                    ),
                  ),
                  u().createElement(
                    qe,
                    { header: ir.score.header(), body: ir.score.body() },
                    u().createElement(
                      "div",
                      { className: C()(sr.cell, sr.cell__score) },
                      u().createElement(Ia, { value: i }),
                    ),
                  ),
                ),
              }[e],
              u().createElement("div", { className: C()(sr.screwIcon, sr.screwIcon__right) }),
            );
          });
        function mr(e, t, a = []) {
          const r = (0, s.useRef)(0),
            n = (0, s.useCallback)(() => window.clearInterval(r.current), a || []);
          (0, s.useEffect)(() => n, [n]);
          const u = (null != a ? a : []).concat([t]);
          return [
            (0, s.useCallback)((a) => {
              ((r.current = window.setInterval(() => e(a, !0), t)), e(a, !1));
            }, u),
            n,
          ];
        }
        const _r = "VerticalBar_base_f3",
          Er = "VerticalBar_base__nonActive_42",
          gr = "VerticalBar_topButton_d7",
          pr = "VerticalBar_bottomButton_06",
          br = "VerticalBar_track_df",
          fr = "VerticalBar_thumb_32",
          hr = "VerticalBar_rail_43",
          Ar = "disable",
          vr = () => {},
          Cr = { pending: !1, offset: 0 },
          Dr = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Fr = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          Br = (e, t) => Math.max(20, e.offsetHeight * t),
          wr = (0, s.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = Dr, onDrag: r = vr }) => {
              const n = (0, s.useRef)(null),
                o = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                l = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                d = e.stepTimeout || 100,
                m = (0, s.useState)(Cr),
                _ = m[0],
                E = m[1],
                g = (0, s.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                p = Ja(() => {
                  const t = c.current,
                    a = l.current,
                    r = e.getWrapperSize(),
                    s = e.getContainerSize();
                  if (!(r && s && t && a)) return;
                  const u = Math.min(1, r / s);
                  return (
                    (t.style.height = `${Br(a, u)}px`),
                    t.classList.add(fr),
                    n.current &&
                      (1 === u ? n.current.classList.add(Er) : n.current.classList.remove(Er)),
                    u
                  );
                }),
                b = Ja(() => {
                  const t = l.current,
                    a = c.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && t && a && n)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    u = Math.min(1, r / n),
                    d = Qa(0, 1, s / (n - r)),
                    m = (t.offsetHeight - Br(t, u)) * d;
                  ((a.style.transform = `translateY(${0 | m}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(Ar), void i.current.classList.remove(Ar));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetHeight - a.offsetHeight) >= -0.5)
                        )
                          return (o.current.classList.remove(Ar), void i.current.classList.add(Ar));
                        var t, a;
                        (o.current.classList.remove(Ar), i.current.classList.remove(Ar));
                      }
                    })(m));
                }),
                f = Ja(() => {
                  Fr(e, () => {
                    (p(), b());
                  });
                });
              ((0, s.useEffect)(() => Re(f)),
                (0, s.useEffect)(() => {
                  const t = () => {
                    Fr(e, () => {
                      b();
                    });
                  };
                  let a = vr;
                  const r = () => {
                    (a(), (a = Re(f)));
                  };
                  return (
                    e.events.on("recalculateContent", f),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", r),
                    () => {
                      (a(),
                        e.events.off("recalculateContent", f),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", r));
                    }
                  );
                }, [e]),
                (0, s.useEffect)(() => {
                  if (!_.pending) return;
                  const t = (t) => {
                      Fr(e, (a) => {
                        const n = l.current,
                          s = c.current,
                          u = e.getContainerSize();
                        if (!n || !s || !u) return;
                        const o = t.screenY - _.offset - n.getBoundingClientRect().y,
                          i = (o / n.offsetHeight) * u;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(a, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: a.scrollTop },
                        }),
                          r({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                      });
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        g(Cr));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, _.offset, _.pending, r, g]));
              const h = mr((t) => e.applyStepTo(t), d, [e]),
                A = h[0],
                v = h[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const D = (e) => {
                e.target.classList.contains(Ar) || W("highlight");
              };
              return u().createElement(
                "div",
                { className: C()(_r, t.base), ref: n, onWheel: e.handleMouseWheel },
                u().createElement("div", {
                  className: C()(gr, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ar) || 0 !== e.button || (W("play"), A(tr.Next));
                  },
                  ref: o,
                  onMouseEnter: D,
                }),
                u().createElement(
                  "div",
                  {
                    className: C()(br, t.track),
                    onMouseDown: (t) => {
                      const r = c.current;
                      if (r && 0 === t.button)
                        if ((W("play"), t.target === r))
                          (e.handleIsThumbDragging(!0),
                            g({ pending: !0, offset: t.screenY - r.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              Fr(e, (r) => {
                                if (!r) return;
                                const n = a(e),
                                  s = e.clampPosition(r, r.scrollTop + n * t);
                                e.applyScroll(s);
                              });
                          })(t.screenY > r.getBoundingClientRect().y ? tr.Prev : tr.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: D,
                  },
                  u().createElement("div", { ref: c, className: t.thumb }),
                  u().createElement("div", { className: C()(hr, t.rail) }),
                ),
                u().createElement("div", {
                  className: C()(pr, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ar) || 0 !== e.button || (W("play"), A(tr.Prev));
                  },
                  onMouseUp: v,
                  ref: i,
                  onMouseEnter: D,
                }),
              );
            },
          ),
          Sr = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Pr = ({
            children: e,
            api: t,
            className: a,
            barClassNames: r,
            areaClassName: n,
            scrollClassName: o,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: C()(Sr.base, e.base) });
              }, [r]),
              m = (0, s.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return u().createElement(
              "div",
              { className: C()(Sr.defaultScroll, a), onWheel: t.handleMouseWheel },
              u().createElement(
                "div",
                { className: C()(Sr.area, n) },
                u().createElement(yr, { className: o, classNames: i, api: m }, e),
              ),
              u().createElement(wr, { getStepByRailClick: l, api: t, onDrag: c, classNames: d }),
            );
          },
          yr = ({ className: e, classNames: t, children: a, api: r }) => (
            (0, s.useEffect)(() => Re(r.recalculateContent)),
            u().createElement(
              "div",
              { className: C()(Sr.base, e), ref: r.wrapperRef, onWheel: r.handleMouseWheel },
              u().createElement(
                "div",
                { className: C()(Sr.content, null == t ? void 0 : t.content), ref: r.contentRef },
                a,
              ),
            )
          );
        yr.Default = Pr;
        const Rr = (e, t) => {
          const a = [];
          for (let r = 0; r < e; r++) a.push(t(r));
          return a;
        };
        let kr, Tr;
        (!(function (e) {
          ((e[(e.A = 1)] = "A"),
            (e[(e.B = 2)] = "B"),
            (e[(e.C = 3)] = "C"),
            (e[(e.D = 4)] = "D"),
            (e[(e.E = 5)] = "E"));
        })(kr || (kr = {})),
          (function (e) {
            ((e[(e.Achieved = 0)] = "Achieved"),
              (e[(e.Current = 1)] = "Current"),
              (e[(e.Inactive = 2)] = "Inactive"));
          })(Tr || (Tr = {})));
        const xr = R.strings.comp7.division,
          Nr = { [kr.A]: "A", [kr.B]: "B", [kr.C]: "C", [kr.D]: "D", [kr.E]: "E" },
          Ir = (e) => xr.$dyn(Nr[e]);
        let Lr;
        !(function (e) {
          ((e[(e.First = 6)] = "First"),
            (e[(e.Second = 5)] = "Second"),
            (e[(e.Third = 4)] = "Third"),
            (e[(e.Fourth = 3)] = "Fourth"),
            (e[(e.Fifth = 2)] = "Fifth"),
            (e[(e.Sixth = 1)] = "Sixth"));
        })(Lr || (Lr = {}));
        const Mr = {
            [Lr.First]: "first",
            [Lr.Second]: "second",
            [Lr.Third]: "third",
            [Lr.Fourth]: "fourth",
            [Lr.Fifth]: "fifth",
            [Lr.Sixth]: "sixth",
          },
          Or = (e) => Mr[e],
          Hr = [Lr.First, Lr.Second, Lr.Third, Lr.Fourth, Lr.Fifth, Lr.Sixth],
          Wr = (e) => Hr.includes(e),
          $r = "RankEmblem_base_ec";
        let Ur;
        !(function (e) {
          ((e[(e.x22 = 22)] = "x22"),
            (e[(e.x40 = 40)] = "x40"),
            (e[(e.x48 = 48)] = "x48"),
            (e[(e.x64 = 64)] = "x64"),
            (e[(e.x84 = 84)] = "x84"),
            (e[(e.x110 = 110)] = "x110"),
            (e[(e.x150 = 150)] = "x150"),
            (e[(e.x200 = 200)] = "x200"),
            (e[(e.x260 = 260)] = "x260"),
            (e[(e.x320 = 320)] = "x320"),
            (e[(e.x420 = 420)] = "x420"),
            (e[(e.x600 = 600)] = "x600"));
        })(Ur || (Ur = {}));
        const zr = ({ rank: e, size: t, division: a, className: r }) => {
            const n = (0, s.useMemo)(() => {
              const r = R.images.comp7.gui.maps.icons.comp7.ranks.$num(t),
                n = Wr(e) && void 0 !== a ? `_${Ir(a)}` : "";
              return {
                backgroundImage: `url(${r.$dyn(`${Or(e)}${n}`)})`,
                "--imageSize": `${t}rem`,
              };
            }, [e, t, a]);
            return u().createElement("div", { className: C()($r, r), style: n });
          },
          Gr = {
            [Lr.First]: "first",
            [Lr.Second]: "second",
            [Lr.Third]: "third",
            [Lr.Fourth]: "fourth",
            [Lr.Fifth]: "fifth",
            [Lr.Sixth]: "sixth",
          },
          jr = (e, t) => `${e.$dyn(Gr[t])}`,
          qr = (e) => jr(R.strings.comp7.rank, e),
          Vr = (e) => lt(R.strings.comp7.rank.text(), { rank: qr(e) }),
          Xr = "RowsDivider_base_0a",
          Qr = "RowsDivider_rankText_96",
          Yr = "RowsDivider_divisionText_7d",
          Kr = ({ data: e, className: t, onClick: a }) => {
            const r = e.rankId,
              n = e.name;
            return u().createElement(
              "div",
              { className: C()(Xr, t), onClick: a, id: String(e.firstMemberPosition) },
              u().createElement(Pa, { className: Qr, text: Vr(r) }),
              u().createElement(zr, { rank: r, size: Ur.x40 }),
              u().createElement(Pa, {
                className: Yr,
                text: ((s = n), lt(xr.text(), { division: Ir(s) })),
              }),
            );
            var s;
          },
          Zr = "Header_base_83",
          Jr = "Header_separator_14",
          en = "Header_cell_0e",
          tn = "Header_cell__order_7d",
          an = "Header_cell__player_c5",
          rn = "Header_cell__score_3e",
          nn = R.strings.comp7.leaderboard.table.header,
          sn = R.strings.comp7.leaderboard.table.tooltip,
          un = () =>
            u().createElement(
              "div",
              { className: Zr },
              u().createElement(
                qe,
                { header: sn.order.header(), body: sn.order.body() },
                u().createElement("div", { className: C()(en, tn) }, nn.order()),
              ),
              u().createElement("div", { className: Jr }),
              u().createElement(
                qe,
                { header: sn.player.header(), body: sn.player.body() },
                u().createElement("div", { className: C()(en, an) }, nn.player()),
              ),
              u().createElement("div", { className: Jr }),
              u().createElement(
                qe,
                { header: sn.battlesCount.header(), body: sn.battlesCount.body() },
                u().createElement("div", { className: C()(en, rn) }, nn.battlesCount()),
              ),
              u().createElement("div", { className: Jr }),
              u().createElement(
                qe,
                { header: sn.score.header(), body: sn.score.body() },
                u().createElement("div", { className: C()(en, rn) }, nn.score()),
              ),
            );
        let on;
        !(function (e) {
          ((e.default = "default"), (e.x48 = "x48"), (e.x80 = "x80"), (e.x220 = "x220"));
        })(on || (on = {}));
        const ln = "TextOverflow_base_3b",
          cn = ({ content: e, classMix: t }) => {
            const a = (0, s.useRef)(null),
              r = (0, s.useState)(!0),
              n = r[0],
              o = r[1];
            return (
              (0, s.useEffect)(() =>
                Re(() => {
                  const e = a.current;
                  e && e.offsetWidth >= e.scrollWidth && o(!1);
                }),
              ),
              u().createElement(
                qe,
                { isEnabled: n, body: e },
                u().createElement("div", { ref: a, className: C()(ln, t) }, e),
              )
            );
          },
          dn = {
            base: "Badge_base_ac",
            base__default: "Badge_base__default_c9",
            base__x48: "Badge_base__x48_e4",
          },
          mn = {
            [on.default]: "c_24x24",
            [on.x48]: "c_48x48",
            [on.x80]: "c_80x80",
            [on.x220]: "c_220x220",
          },
          _n = ({ badgeID: e, size: t = on.default, className: a }) => {
            const r = R.images.gui.maps.icons.library.badges.$dyn(mn[t]);
            return u().createElement("div", {
              className: C()(dn.base, dn[`base__${t}`], a),
              style: { backgroundImage: `url(${r.$dyn(`badge_${e}`)})` },
            });
          },
          En = {
            base: "PlayerNickname_base_32",
            userName: "PlayerNickname_userName_cc",
            igrIcon: "PlayerNickname_igrIcon_34",
            base__default: "PlayerNickname_base__default_8d",
            base__x48: "PlayerNickname_base__x48_84",
            suffixBadgeWrapper: "PlayerNickname_suffixBadgeWrapper_cc",
            suffixBadgeStripe: "PlayerNickname_suffixBadgeStripe_8a",
            base__inverted: "PlayerNickname_base__inverted_34",
            suffixBadge: "PlayerNickname_suffixBadge_bd",
            anonymizedIcon: "PlayerNickname_anonymizedIcon_80",
          },
          gn = (0, s.memo)(({ tooltipHeaderName: e }) => {
            const t = (0, s.useMemo)(
                () => lt(R.strings.tooltips.anonymizer.teamStats.header(), { name: e }),
                [e],
              ),
              a = R.strings.tooltips.anonymizer.teamStats.body();
            return u().createElement(
              qe,
              { header: t, body: a },
              u().createElement("div", { className: En.anonymizedIcon }),
            );
          });
        function pn() {
          return (
            (pn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            pn.apply(this, arguments)
          );
        }
        const bn = { [on.default]: "c_64x24", [on.x48]: "c_68x28" },
          fn = { [on.default]: "c_48x48", [on.x48]: "c_48x48" },
          hn = ({
            userName: e,
            clanAbbrev: t = "",
            igrType: a = 0,
            badge: r = { badgeID: "" },
            suffixBadge: n = { badgeID: "" },
            isInverted: o = !1,
            isFakeNameVisible: i = !1,
            isAnonymizerShown: l = !1,
            hiddenUserName: c = "",
            size: d = on.default,
            userNameClassName: m = "",
            clanTagClassName: _ = "",
          }) => {
            const E = R.images.gui.maps.icons.library.badges.strips.$dyn(bn[d]),
              g = (0, s.useMemo)(
                () => ({ backgroundImage: `url(${E.$dyn(`strip_${n.badgeID}`)})` }),
                [n, E],
              ),
              p = R.images.gui.maps.icons.library.badges.$dyn(fn[d]),
              b = (0, s.useMemo)(
                () => ({ backgroundImage: `url(${p.$dyn(`badge_${n.badgeID}`)})` }),
                [n, p],
              ),
              f = t ? `[${t}]` : "",
              h = C()(En.base, En[`base__${d}`], o && En.base__inverted),
              A = C()(En.userName, m),
              v = C()(En.clanTag, _),
              D = e !== c,
              F = i ? `${c}${f}` : c,
              B = Boolean(r.badgeID) && u().createElement(_n, pn({ size: d }, r, { key: "badge" })),
              w = Date.now(),
              S = [
                B,
                [
                  u().createElement(
                    "div",
                    { className: A, key: "userName" },
                    u().createElement(cn, { content: e, key: w }),
                  ),
                  !i && Boolean(f) && u().createElement("div", { className: v, key: "clanTag" }, f),
                ],
                0 !== a && u().createElement("div", { className: En.igrIcon, key: "igrType" }),
                Boolean(n.badgeID) &&
                  u().createElement(
                    "div",
                    { className: En.suffixBadgeWrapper, key: "suffixBadge" },
                    u().createElement("div", { className: En.suffixBadgeStripe, style: g }),
                    u().createElement("div", { className: En.suffixBadge, style: b }),
                  ),
                l && D && u().createElement(gn, { tooltipHeaderName: F, key: "anonymizer" }),
              ];
            return u().createElement("div", { className: h }, o ? S.reverse() : S);
          };
        let An;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(An || (An = {}));
        const vn = ({
            children: e,
            contentID: t,
            decoratorID: a = 0,
            targetId: r = 0,
            args: n,
            isEnabled: u = !0,
            onMouseDown: o,
          }) => {
            const i = (0, s.useCallback)(() => {
                ((0, X.c9)(X.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: a,
                  targetID: r,
                  isMouseEvent: !0,
                  on: !0,
                  args: n,
                }),
                  $.playYes());
              }, [n, t, a, r]),
              l = (0, s.useCallback)(() => {
                (0, X.c9)(X.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: a,
                  targetID: r,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, a, r]),
              c = (0, s.useCallback)(
                (e) => {
                  (o && o(e), ((e) => e.button === An.RIGHT)(e) && i());
                },
                [o, i],
              );
            return (
              (0, s.useEffect)(() => {
                !1 === u && l();
              }, [u, l]),
              u ? (0, s.cloneElement)(e, { onMouseDown: c }) : e
            );
          },
          Cn = ["children"];
        function Dn() {
          return (
            (Dn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Dn.apply(this, arguments)
          );
        }
        const Fn = (e) => {
            let t = e.children,
              a = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, Cn);
            return u().createElement(
              vn,
              Dn({}, a, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          Bn = ({ children: e, isEnabled: t, contextMenuArgs: a }) =>
            t ? u().createElement(Fn, { args: a }, e) : e,
          wn = {
            base: "Row_base_fc",
            base__highlight: "Row_base__highlight_35",
            base__personal: "Row_base__personal_1c",
            marker: "Row_marker_b0",
            highlightMarker: "Row_highlightMarker_eb",
            order: "Row_order_30",
            order__first: "Row_order__first_53",
            order__second: "Row_order__second_cb",
            order__third: "Row_order__third_c6",
            playerContainer: "Row_playerContainer_9e",
            player: "Row_player_f9",
            clanTag: "Row_clanTag_73",
            battles: "Row_battles_61",
            score: "Row_score_55",
          },
          Sn = R.strings.comp7.leaderboard.table.tooltip,
          Pn = { 0: "first", 1: "second", 2: "third" },
          yn = R.views.lobby.comp7.tooltips.LeaderboardRewardTooltip("resId"),
          Rn = (0, q.Pi)(({ index: e, className: t }) => {
            const a = qt().model,
              r = a.computes.leaderboardItem(e),
              n = r.position,
              s = r.battlesCount,
              o = r.userName,
              i = r.clanTag,
              l = r.clanTagColor,
              c = r.score,
              d = r.spaID,
              m = n + 1,
              _ = a.computes.isPersonalRow(e),
              E = a.computes.hasPositionIcon(e),
              g = n < 10,
              p = C()(wn.base, g && wn.base__highlight, _ && wn.base__personal, t),
              b = C()(wn.order, E && wn[`order__${Pn[n]}`]);
            return u().createElement(
              "div",
              { className: p, style: { "--clanTagColor": l } },
              u().createElement(
                Ue,
                { contentId: yn, args: { place: m }, isEnabled: g },
                u().createElement(
                  "div",
                  { className: wn.highlightMarker },
                  g && u().createElement("div", { className: wn.marker }),
                ),
              ),
              u().createElement(
                qe,
                { header: Sn.order.header(), body: Sn.order.body() },
                u().createElement("div", { className: b }, !E && n + 1),
              ),
              u().createElement(
                Bn,
                { contextMenuArgs: { spaID: d, userName: o }, isEnabled: !_ },
                u().createElement(
                  "div",
                  { className: wn.playerContainer },
                  u().createElement(
                    qe,
                    { header: Sn.player.header(), body: Sn.player.body() },
                    u().createElement(
                      "div",
                      { className: wn.player },
                      u().createElement(hn, {
                        userName: o,
                        clanAbbrev: i,
                        clanTagClassName: l && wn.clanTag,
                      }),
                    ),
                  ),
                ),
              ),
              u().createElement(
                qe,
                { header: Sn.battlesCount.header(), body: Sn.battlesCount.body() },
                u().createElement(
                  "div",
                  { className: wn.battles },
                  u().createElement(Ia, { value: s }),
                ),
              ),
              u().createElement(
                qe,
                { header: Sn.score.header(), body: Sn.score.body() },
                u().createElement(
                  "div",
                  { className: wn.score },
                  u().createElement(Ia, { value: c }),
                ),
              ),
            );
          }),
          kn = "Leaderboard_base_ec",
          Tn = "Leaderboard_content_a5",
          xn = "Leaderboard_shadowsContainer_bc",
          Nn = "Leaderboard_shadowsContainer__bottom_b4",
          In = "Leaderboard_shadow_3f",
          Ln = "Leaderboard_shadow__left_ee",
          Mn = "Leaderboard_shadow__center_37",
          On = "Leaderboard_shadow__right_ee",
          Hn = "Leaderboard_area_c7",
          Wn = "Leaderboard_row_06",
          $n = "Leaderboard_rowsDivider_2c",
          Un = { base: "Leaderboard_bar_69" },
          zn = (0, q.Pi)(
            ({
              api: e,
              rowHeight: t = 0,
              rowsDividerHeight: a = 0,
              rowsDividerMargin: r = 0,
              markUserScrollStart: n,
            }) => {
              const o = qt().model,
                i = o.computes.getDivisionsDividers(),
                l = o.computes.pages(at),
                c = (0, s.useMemo)(() => Object.assign({}, e, { handleMouseWheel: () => {} }), [e]),
                d = (0, s.useCallback)(
                  (t) => {
                    (null == n || n(), e.handleMouseWheel(t));
                  },
                  [e, n],
                );
              return u().createElement(
                "div",
                {
                  className: kn,
                  style: {
                    "--rowHeight": t ? `${t}rem` : "auto",
                    "--rowsDividerHeight": `${a}rem`,
                    "--rowsDividerMargin": `${r}rem`,
                  },
                },
                u().createElement(un, null),
                u().createElement(
                  "div",
                  { className: Tn, onWheel: d },
                  u().createElement(
                    "div",
                    { className: xn },
                    u().createElement("div", { className: C()(In, Ln) }),
                    u().createElement("div", { className: C()(In, Mn) }),
                    u().createElement("div", { className: C()(In, On) }),
                  ),
                  u().createElement(
                    yr,
                    { api: c, className: Hn },
                    Rr(o.computes.leaderboardItemsLength(), (e) => {
                      const t = (l.active - 1) * at + e + 1;
                      return u().createElement(
                        u().Fragment,
                        { key: e },
                        i[t] && u().createElement(Kr, { data: i[t], className: $n }),
                        u().createElement(Rn, { className: Wn, index: e }),
                      );
                    }),
                  ),
                  u().createElement(
                    "div",
                    { className: C()(xn, Nn) },
                    u().createElement("div", { className: C()(In, Ln) }),
                    u().createElement("div", { className: C()(In, Mn) }),
                    u().createElement("div", { className: C()(In, On) }),
                  ),
                  u().createElement(wr, { api: c, classNames: Un }),
                ),
              );
            },
          ),
          Gn = {
            base: "Pagination_base_49",
            pageButton: "Pagination_pageButton_27",
            pageButton__active: "Pagination_pageButton__active_0b",
            pageButton__inactive: "Pagination_pageButton__inactive_4c",
            pageButton__disabled: "Pagination_pageButton__disabled_e4",
            pageValue: "Pagination_pageValue_b2",
            control: "Pagination_control_4f",
            control__active: "Pagination_control__active_25",
            control__prev: "Pagination_control__prev_8e",
            control__next: "Pagination_control__next_86",
          };
        let jn;
        !(function (e) {
          ((e.Active = "active"), (e.Inactive = "inactive"), (e.Disabled = "disabled"));
        })(jn || (jn = {}));
        const qn = R.strings.comp7.pagination,
          Vn = Math.trunc(4),
          Xn = ({
            pagesAmount: e,
            activePage: t,
            className: a,
            onPageClick: r,
            onControlEvent: n,
          }) => {
            const s = t > 1,
              o = t < e,
              i = e < 9 ? e : 9,
              l = (e) => () => {
                null == r || r(e);
              },
              c = (e) => () => {
                null == n || n(e);
              };
            return u().createElement(
              "div",
              { className: C()(Gn.base, a) },
              u().createElement(
                "div",
                {
                  className: C()(Gn.control, Gn.control__prev, s && Gn.control__active),
                  onClick: s ? c("prevClick") : void 0,
                },
                qn.prev(),
              ),
              Rr(i, (a) => {
                const r = ((e, t, a) => {
                    const r = t > Vn + 1,
                      n = a > 9 && t + Vn < a;
                    return a <= 9
                      ? e + 1
                      : 0 === e
                        ? 1
                        : (1 === e && r) || (7 === e && n)
                          ? qn.dots()
                          : 8 === e
                            ? a
                            : r && !n
                              ? a - 8 + e
                              : !r && n
                                ? e + 1
                                : e - Vn + t;
                  })(a, t, e),
                  n = ((e, t) =>
                    Number.isInteger(e) ? (t === e ? jn.Active : jn.Inactive) : jn.Disabled)(r, t);
                return u().createElement(
                  "div",
                  {
                    key: a,
                    className: C()(Gn.pageButton, Gn[`pageButton__${n}`]),
                    onClick: n !== jn.Disabled && "number" == typeof r ? l(r) : void 0,
                  },
                  u().createElement("div", { className: Gn.pageValue }, r),
                );
              }),
              u().createElement(
                "div",
                {
                  className: C()(Gn.control, Gn.control__next, o && Gn.control__active),
                  onClick: o ? c("nextClick") : void 0,
                },
                qn.next(),
              ),
            );
          },
          Qn = {
            settings: Object.assign({}, ar, {
              animationConfig: Object.assign({}, ar.animationConfig, { round: 1 }),
            }),
          },
          Yn = "HasRecordsState_base_bb",
          Kn = "HasRecordsState_base__withoutPagination_ad",
          Zn = "HasRecordsState_tableContainer_02",
          Jn = "HasRecordsState_pagination_cb",
          es = (e) => Object.keys(e).sort((e, t) => Number(e) - Number(t)),
          ts = (e, t) => {
            const a = document.getElementById(e);
            return a ? a.offsetTop - t : null;
          },
          as = (e, t) => t.reduce((t, a) => (Number(a) <= e + 1 ? Number(a) : t), Number(t[0])),
          rs = (e, t, a) => {
            const r = ((e) => e.filter((e) => null !== document.getElementById(e)))(t);
            return 0 === r.length
              ? null
              : r.reduce((r, n, s) => {
                  const u = ts(n, a);
                  if (null === u) return r;
                  if (u <= e) return Number(n);
                  if (0 === s) {
                    const e = t.indexOf(n) - 1;
                    return Number(t[e]);
                  }
                  return r;
                }, Number(r[0]));
          },
          ns = ({
            dividers: e,
            positionToScroll: t,
            onPositionToScrollChange: a,
            setSelectedTab: r,
            startPosition: n,
            activePage: u,
            personalPosition: o,
            limit: i,
            applyScroll: l,
            events: c,
            getScrollPosition: d,
          }) => {
            const m = (0, s.useRef)(!1),
              _ = (0, s.useRef)(!1),
              E = (0, s.useRef)(null),
              g = (0, s.useCallback)(() => {
                ((m.current = !1), (_.current = !0));
              }, []),
              p = (0, s.useCallback)(
                (t) => {
                  const a = es(e),
                    r = viewEnv.remToPx(12);
                  E.current = rs(t, a, r);
                },
                [e],
              );
            return (
              (0, s.useEffect)(
                () =>
                  Re(() => {
                    if (void 0 === t) return;
                    const n = es(e),
                      s = viewEnv.remToPx(12);
                    let u = !1;
                    const c = (e) => {
                      ((_.current = !1), (m.current = !0), l(e), (u = !0));
                    };
                    switch (t.type) {
                      case "division": {
                        r(t.position);
                        const e = ((e, t) => ts(String(e), t))(t.position, s);
                        null !== e && c(e);
                        break;
                      }
                      case "personalPosition":
                        (n.length > 0 && r(as(o, n)),
                          c(((e, t, a) => viewEnv.remToPx(a) * (e % t))(o, i, 44)));
                        break;
                      case "page":
                        (n.length > 0 && r(as(t.offset, n)), c(0));
                    }
                    (u || (m.current = !1), a(void 0));
                  }),
                [e, r, n, l, i, o, t, a],
              ),
              (0, s.useEffect)(() => {
                if (void 0 !== t) return;
                const a = es(e);
                if (0 === a.length) return;
                if (m.current) return;
                const s = as(n, a);
                (r(s), (E.current = s));
              }, [e, n, u, t, r]),
              (0, s.useEffect)(
                () =>
                  Re(() => {
                    p(d());
                  }),
                [u, e, d, p],
              ),
              (0, s.useEffect)(() => {
                const t = viewEnv.remToPx(12),
                  a = (a) => {
                    const n = es(e),
                      s = rs(a, n, t);
                    null !== s && s !== E.current && ((E.current = s), r(s));
                  },
                  n = (e) => {
                    e && g();
                  },
                  s = (e) => {
                    const t = e.value.scrollPosition;
                    if (m.current) return ((m.current = !1), void p(t));
                    ((_.current = !1), a(t));
                  },
                  u = (e) => {
                    !m.current && _.current && a(e.value.scrollPosition);
                  };
                return (
                  c.on("change", u),
                  c.on("rest", s),
                  c.on("isThumbDraggingChanged", n),
                  () => {
                    (c.off("change", u), c.off("rest", s), c.off("isThumbDraggingChanged", n));
                  }
                );
              }, [e, c, g, r, p]),
              { markUserScrollStart: g }
            );
          },
          ss = (0, q.Pi)(
            ({
              limit: e,
              positionToScroll: t,
              onPositionToScrollChange: a,
              setSelectedTab: r,
              className: n,
            }) => {
              const o = qt(),
                i = o.model,
                l = o.controls,
                c = i.root.get().personalPosition,
                d = i.computes.getDivisionsDividers(),
                m = nr(Qn),
                _ = m.applyScroll,
                E = m.events,
                g = m.animationScroll,
                p = (0, s.useCallback)(() => g.scrollPosition.get(), [g.scrollPosition]),
                b = i.computes.isDefaultPersonalPosition() ? ur.None : ur.Active,
                f = i.computes.pages(e),
                h = i.computes.pagePositions().first,
                A = ns({
                  dividers: d,
                  positionToScroll: t,
                  onPositionToScrollChange: a,
                  setSelectedTab: r,
                  startPosition: h,
                  activePage: f.active,
                  personalPosition: c,
                  limit: e,
                  applyScroll: _,
                  events: E,
                  getScrollPosition: p,
                }).markUserScrollStart,
                v = (0, s.useCallback)(() => {
                  b !== ur.None &&
                    ($.playYes(),
                    l.getTableRecords(e, c - (c % e)),
                    a({ type: "personalPosition" }));
                }, [l, e, b, c, a]),
                D = (0, s.useCallback)(
                  (t) => {
                    ($.playYes(),
                      l.getTableRecords(e, (t - 1) * e),
                      a({ type: "page", offset: (t - 1) * e }));
                  },
                  [l, e, a],
                ),
                F = (0, s.useCallback)(
                  (t) => {
                    $.playYes();
                    const r = (("prevClick" === t ? f.active - 1 : f.active + 1) - 1) * e;
                    (l.getTableRecords(e, r), a({ type: "page", offset: r }));
                  },
                  [f.active, l, e, a],
                );
              return u().createElement(
                "div",
                { className: C()(Yn, !f.hasPagination && Kn, n) },
                u().createElement(
                  "div",
                  { className: Zn },
                  u().createElement(zn, {
                    api: m,
                    rowHeight: 44,
                    rowsDividerHeight: 52,
                    rowsDividerMargin: 12,
                    markUserScrollStart: A,
                  }),
                ),
                u().createElement(dr, { state: b, onClick: v, height: 44 }),
                f.hasPagination &&
                  u().createElement(Xn, {
                    pagesAmount: f.amount,
                    activePage: f.active,
                    className: Jn,
                    onPageClick: D,
                    onControlEvent: F,
                  }),
              );
            },
          ),
          us = "DivisionTab_base_52",
          os = "DivisionTab_border_1c",
          is = "DivisionTab_disabled_57",
          ls = "DivisionTab_text_9b",
          cs = "DivisionTab_glow_8c",
          ds = "DivisionTab_selected_0e",
          ms = ({ division: e, isSelected: t, onClick: a, className: r }) => {
            const n = e.rankId,
              o = e.name,
              i = e.from,
              l = e.to,
              c = e.type,
              d = e.elitePercent,
              m = e.firstMemberPosition,
              _ = kr[o],
              E = -1 === m,
              g = C()(us, r, { [ds]: t, [is]: E }),
              p = (0, s.useCallback)(() => {
                E || a(m);
              }, [a, m, E]);
            return u().createElement(
              Ue,
              {
                contentId: R.views.lobby.comp7.tooltips.DivisionTooltip("resId"),
                args: { rank: n, division: o, from: i, to: l + 1, type: c, elitePercent: d },
              },
              u().createElement(
                "div",
                { className: g },
                u().createElement("div", { className: os }),
                u().createElement("div", { className: cs }),
                u().createElement(Pa, { text: _, className: ls, onClick: p }),
              ),
            );
          },
          _s = "RankTabs_base_c4",
          Es = "RankTabs_divisions_a2",
          gs = "RankTabs_rankEmblem_d6",
          ps = ({ tabs: e, selectedTab: t, onTabClick: a, setSelectedTab: r }) => {
            const n = (e) => {
              (r(e), a(e));
            };
            return u().createElement(
              "div",
              { className: _s },
              Object.keys(e).map((a) => {
                const r = a,
                  s = e[a];
                return u().createElement(
                  "div",
                  { key: r },
                  u().createElement(zr, { rank: r, size: Ur.x64, className: gs }),
                  u().createElement(
                    "div",
                    { className: Es },
                    s.map((e) => {
                      const a = String(r + e.name);
                      return u().createElement(ms, {
                        key: a,
                        division: e,
                        isSelected: t === e.firstMemberPosition,
                        onClick: n,
                      });
                    }),
                  ),
                );
              }),
            );
          },
          bs = {
            base: "StateContainer_base_4e",
            content: "StateContainer_content_62",
            line: "StateContainer_line_30",
            noRecords: "StateContainer_noRecords_49",
            controls: "StateContainer_controls_11",
            updateInfo: "StateContainer_updateInfo_12",
            noRecordsLine: "StateContainer_noRecordsLine_71",
          },
          fs = (0, q.Pi)(() => {
            const e = (0, s.useState)(1),
              t = e[0],
              a = e[1],
              r = qt(),
              n = r.model,
              o = r.controls,
              i = n.computes.hasRecords(),
              l = n.root.get().leaderboardUpdateTimestamp,
              c = n.computes.pages(at),
              d = n.computes.hasUpdateInfo(),
              m = (0, s.useState)(),
              _ = m[0],
              E = m[1],
              g = C()(bs.base, { [bs.hasRecords]: i, [bs.noRecords]: !i }),
              p = C()(bs.line, { [bs.noRecordsLine]: !i }),
              b = n.computes.getRankTabs(),
              f = (0, s.useCallback)(
                (e) => {
                  var t, a, r;
                  ($.playClick(),
                    (t = c.active),
                    (a = e),
                    ((e, t) => (e - 1) * t)(t, (r = at)) !== Xa(a, r) &&
                      o.getTableRecords(at, Xa(e, at)),
                    E({ type: "division", position: e }));
                },
                [c.active, o],
              );
            return u().createElement(
              "div",
              { className: g },
              u().createElement(
                "div",
                { className: bs.controls },
                d &&
                  u().createElement(
                    "div",
                    { className: bs.updateInfo },
                    u().createElement(Na, { timestamp: l }),
                    u().createElement("div", { className: p }),
                  ),
                i &&
                  u().createElement(
                    u().Fragment,
                    null,
                    u().createElement(ps, {
                      tabs: b,
                      onTabClick: f,
                      selectedTab: t,
                      setSelectedTab: a,
                    }),
                    u().createElement("div", { className: bs.line }),
                  ),
              ),
              i
                ? u().createElement(ss, {
                    limit: at,
                    positionToScroll: _,
                    onPositionToScrollChange: E,
                    className: bs.content,
                    setSelectedTab: a,
                  })
                : u().createElement(Va, null),
            );
          }),
          hs = {
            "--pageContentWidth": "78vw",
            base: "LeaderboardPage_base_4a",
            animationContainer: "LeaderboardPage_animationContainer_94",
            subHeading: "LeaderboardPage_subHeading_ae",
            content: "LeaderboardPage_content_46",
            base__loading: "LeaderboardPage_base__loading_12",
            error: "LeaderboardPage_error_7d",
            spinner: "LeaderboardPage_spinner_67",
            fadeIn: "LeaderboardPage_fadeIn_46",
            fadeInThreeQuarters: "LeaderboardPage_fadeInThreeQuarters_98",
            fadeInHalf: "LeaderboardPage_fadeInHalf_30",
            fadeOut: "LeaderboardPage_fadeOut_e8",
            fadeInWithScale: "LeaderboardPage_fadeInWithScale_07",
            slideUp: "LeaderboardPage_slideUp_9c",
            scale: "LeaderboardPage_scale_5d",
            raysAppearance: "LeaderboardPage_raysAppearance_c3",
            rotate: "LeaderboardPage_rotate_db",
            "reverse-rotate": "LeaderboardPage_reverse-rotate_1d",
            glowAppearance: "LeaderboardPage_glowAppearance_4f",
            highlightAppearance: "LeaderboardPage_highlightAppearance_23",
            blink: "LeaderboardPage_blink_7e",
            slideUpIn: "LeaderboardPage_slideUpIn_37",
          },
          As = { [rt.Initial]: "initial", [rt.Success]: "success", [rt.Error]: "error" },
          vs = (0, q.Pi)(() => {
            const e = qt().model.root.get(),
              t = e.state,
              a = e.isLoading,
              r = (0, ke.useSpring)(_e);
            return u().createElement(
              "div",
              { className: C()(hs.base, hs[`base__${As[t]}`], a && hs.base__loading) },
              u().createElement(st, { className: K }, R.strings.comp7.page.heading.leaderboard()),
              u().createElement(It, null),
              u().createElement(
                ke.animated.div,
                { className: hs.animationContainer, style: r },
                u().createElement(
                  "div",
                  { className: hs.content },
                  (() => {
                    switch (t) {
                      case rt.Initial:
                        return null;
                      case rt.Success:
                        return u().createElement(fs, null);
                      case rt.Error:
                        return u().createElement(ta, { className: hs.error });
                      default:
                        console.error(
                          "Unreachable branch: add component for proper leaderboard state",
                        );
                    }
                  })(),
                ),
                a &&
                  u().createElement(tt, {
                    message: R.strings.comp7.waitingSpinner.message(),
                    className: hs.spinner,
                  }),
              ),
            );
          }),
          Cs = { context: "model.leaderboardModel" },
          Ds = (e) => ve(e, (e) => Ir(e.name)).join(R.strings.comp7.listSeparator()),
          Fs = (e) => ve(e, (e) => e.elitePercent).sort((e, t) => t - e)[0];
        let Bs, ws, Ss;
        (!(function (e) {
          ((e.Previous = "previous"), (e.Current = "current"), (e.Future = "future"));
        })(Bs || (Bs = {})),
          (function (e) {
            ((e[(e.Page = 0)] = "Page"),
              (e[(e.Maps = 1)] = "Maps"),
              (e[(e.SeasonVehicles = 2)] = "SeasonVehicles"));
          })(ws || (ws = {})),
          (function (e) {
            ((e[(e.BASIC = 0)] = "BASIC"),
              (e[(e.TRANSFER = 1)] = "TRANSFER"),
              (e[(e.ELITE = 2)] = "ELITE"));
          })(Ss || (Ss = {})));
        const Ps = (e, t, a) => (e > t || a ? Bs.Future : e < t ? Bs.Previous : Bs.Current),
          ys = (e) => ({ from: e[0].from, to: e[e.length - 1].to }),
          Rs = oe()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  qualificationModel: e.primitives(
                    ["isActive", "battlesCount", "maxBattlesCount", "isRatingCalculation"],
                    "qualificationModel",
                  ),
                  isRewardLayerVisible: re.LO.box(!1),
                  isParallaxPreloaded: re.LO.box(!1),
                },
                a = e.array("items"),
                r = e.array("qualificationModel.battles"),
                n = (0, Ee.Om)(
                  (e) => {
                    const t = fe(a.get(), e);
                    if (!t) throw new Error(`item with index ${e} was not found`);
                    return { hasRankInactivity: t.hasRankInactivity, rank: t.rank };
                  },
                  { equals: zt },
                ),
                s = (0, Ee.Om)(
                  (e) => {
                    const t = fe(a.get(), e);
                    if (!t) throw new Error(`rank with index ${e} was not found`);
                    const r = ve(t.divisions, (e) => Object.assign({}, e));
                    if (r.length > 0) return ys(r);
                    throw new Error(`no basic divisions for rank with ${e}`);
                  },
                  { equals: ae },
                ),
                u = (0, Ee.Om)(
                  (e) => {
                    const t = fe(a.get(), e);
                    if (!t) throw new Error(`item with index ${e} was not found`);
                    return ve(t.divisions, (e) => Object.assign({}, e));
                  },
                  { equals: ae },
                ),
                o = (0, Ee.Om)(
                  (e, t) => {
                    const a = u(e);
                    if (!a) throw new Error(`divisions from rank index ${e} was not found`);
                    return a.filter((e) => e.type === t);
                  },
                  { equals: ae },
                ),
                i = (0, Ee.Om)(
                  (e) => {
                    const t = u(e);
                    return {
                      list: Ds(t),
                      count: t.length,
                      currentDivisionIndex: Fe(t, (e) => e.state === Tr.Current),
                      elitePercent: Fs(t),
                    };
                  },
                  { equals: zt },
                ),
                l = (0, Ee.Om)(() => {
                  const e = t.root.get().currentItemIndex,
                    r = fe(a.get(), e);
                  if (!r) throw new Error(`current item with currentItemIndex ${e} was not found`);
                  return r.hasRankInactivity;
                }),
                c = (0, Ee.Om)(
                  (e, a) => {
                    var r;
                    return {
                      state: Ps(e, t.root.get().currentItemIndex, a),
                      division:
                        null == (r = De(u(e), (e) => e.state === Tr.Current)) ? void 0 : r.name,
                    };
                  },
                  { equals: zt },
                ),
                d = (0, Ee.Om)(
                  (e) => {
                    const t = fe(r.get(), e);
                    if (!t) throw new Error(`qualification battle with index ${e} was not found`);
                    return t;
                  },
                  { equals: ae },
                );
              return Object.assign({}, t, {
                computes: {
                  modelItems: (0, Ee.Om)(() =>
                    ve(a.get(), (e) =>
                      Object.assign({}, e, {
                        divisions: ve(e.divisions, (e) => Object.assign({}, e)),
                      }),
                    ),
                  ),
                  itemsLength: (0, Ee.Om)(() => a.get().length),
                  qualificationBattlesLength: (0, Ee.Om)(() => r.get().length),
                  item: n,
                  rankPointsDiapason: s,
                  qualificationBattle: d,
                  rankSettings: c,
                  hasCurrentItemRankInactivity: l,
                  divisions: u,
                  divisionsConfig: i,
                  divisionsByType: o,
                },
              });
            },
            ({ externalModel: e, model: t }) => {
              const a = (0, re.aD)((e) => t.isRewardLayerVisible.set(e));
              return {
                setIsParallaxPreloaded: (0, re.aD)((e) => t.isParallaxPreloaded.set(e)),
                setRewardLayerVisible: a,
                goToRankRewardsPage: e.createCallbackNoArgs(
                  "qualificationModel.onRankRewardsPageOpen",
                ),
                goToLeaderboardPage: e.createCallbackNoArgs("onLeaderboardLinkClick"),
              };
            },
          ),
          ks = Rs[0],
          Ts = Rs[1];
        var xs = a(7006);
        const Ns = ["iron", "bronze", "silver", "gold", "champion", "legend"],
          Is = (e, t, a) => {
            const r = (0, s.useMemo)(() => {
                return (t = e) >= 0 && t < Ns.length
                  ? Ns[t]
                  : (console.warn(`Invalid rank index: ${t}, fallback to 'iron'`), "iron");
                var t;
              }, [e]),
              n = (0, s.useState)(r),
              u = n[0],
              o = n[1];
            (0, s.useEffect)(() => {
              const e = setTimeout(() => o(r), t);
              return () => clearTimeout(e);
            }, [r, t]);
            const i = (0, s.useState)(u),
              l = i[0],
              c = i[1],
              d = (0, s.useState)(null),
              m = d[0],
              _ = d[1],
              E = (0, s.useRef)(l);
            E.current = l;
            const g = (0, xs.useSpring)(() => ({ opacity: 0, config: { duration: a } })),
              p = g[0],
              b = g[1];
            return (
              (0, s.useEffect)(() => {
                if (u === E.current) return;
                const e = E.current;
                (c(u), _(e), b.set({ opacity: 1 }), b.start({ opacity: 0, onRest: () => _(null) }));
              }, [u, b]),
              { currentBg: l, prevBg: m, spring: p }
            );
          },
          Ls = "FailedFetchPointsText_base_be",
          Ms = "FailedFetchPointsText_icon_76",
          Os = "FailedFetchPointsText_text_ea",
          Hs = ({ containerStyles: e }) =>
            u().createElement(
              "div",
              { className: C()(Ls, e) },
              u().createElement("div", { className: Ms }),
              u().createElement(Pa, {
                text: R.strings.comp7.honorsPlace.failedFetchPointsText(),
                className: Os,
              }),
            ),
          Ws = "HonorsPlace_base_57",
          $s = "HonorsPlace_base__error_c4",
          Us = "HonorsPlace_base__tooltip_b9",
          zs = "HonorsPlace_base__tooltipError_3c",
          Gs = "HonorsPlace_transferPlace_46",
          js = "HonorsPlace_elitePlace_eb",
          qs = "HonorsPlace_elitePlace__bronze_5b",
          Vs = "HonorsPlace_elitePlace__silver_cd",
          Xs = "HonorsPlace_elitePlace__gold_87",
          Qs = "HonorsPlace_elitePlace__tooltip_0a",
          Ys = "HonorsPlace_elitePlace__modeSelector_dc",
          Ks = "HonorsPlace_garland_ab",
          Zs = "HonorsPlace_garland__transferPlaceLeft_e7",
          Js = "HonorsPlace_garland__transferPlaceLeft__tooltip_23",
          eu = "HonorsPlace_garland__transferPlaceLeft__modeSelector_5a",
          tu = "HonorsPlace_garland__transferPlaceRight_d4",
          au = "HonorsPlace_garland__transferPlaceRight__tooltip_20",
          ru = "HonorsPlace_garland__transferPlaceRight__modeSelector_9f",
          nu = "HonorsPlace_garland__tooltip_3f",
          su = "HonorsPlace_garland__modeSelector_e0",
          uu = "HonorsPlace_placeText_23",
          ou = "HonorsPlace_placeText__transfer_d3",
          iu = "HonorsPlace_placeText__transfer__copied_0f",
          lu = "HonorsPlace_placeText__tooltip_98",
          cu = "HonorsPlace_placeText__notInLeaderboard_81",
          du = "HonorsPlace_placeText__modeSelector_57",
          mu = "HonorsPlace_positionTitle_c9",
          _u = "HonorsPlace_positionTitle__tooltip_8a",
          Eu = "HonorsPlace_positionTitle__modeSelector_c7",
          gu = "HonorsPlace_titleDescriptionContainer_15",
          pu = "HonorsPlace_descriptionText_b8",
          bu = "HonorsPlace_descriptionText__tooltip_70",
          fu = "HonorsPlace_descriptionText__withoutMargin_a9",
          hu = "HonorsPlace_descriptionText__blackout_3a",
          Au = "HonorsPlace_rankInactivityCount_34",
          vu = "HonorsPlace_failedFetchPointsText_e2",
          Cu = "RankInactivityCount_base_c2",
          Du = "RankInactivityCount_count_28",
          Fu = "RankInactivityCount_iconContainer_85",
          Bu = "RankInactivityCount_icon_52",
          wu = ({ count: e, containerStyles: t }) => {
            const a = C()(Cu, t);
            return u().createElement(
              Ue,
              {
                ignoreShowDelay: !0,
                contentId: R.views.lobby.comp7.tooltips.RankInactivityTooltip("resId"),
                args: { count: e },
              },
              u().createElement(
                "div",
                { className: a },
                u().createElement("div", { className: Du }, e),
                u().createElement(
                  "div",
                  { className: Fu },
                  u().createElement("div", { className: Bu }),
                ),
              ),
            );
          },
          Su = R.strings.comp7.honorsPlace.description;
        var Pu;
        let yu;
        (!(function (e) {
          ((e[(e.BRONZE = 3)] = "BRONZE"),
            (e[(e.SILVER = 2)] = "SILVER"),
            (e[(e.GOLD = 1)] = "GOLD"),
            (e[(e.NOT_IN_LEADERBOARD = 0)] = "NOT_IN_LEADERBOARD"),
            (e[(e.ERROR = -1)] = "ERROR"));
        })(Pu || (Pu = {})),
          (function (e) {
            ((e.PROGRESSION = "PROGRESSION"),
              (e.TOOLTIP = "TOOLTIP"),
              (e.MODE_SELECTOR = "MODE_SELECTOR"));
          })(yu || (yu = {})));
        const Ru = ({ mode: e, model: t }) => {
            var a, r;
            const n = t.root.get(),
              s = n.myPosition,
              o = n.currentScore,
              i = n.rankInactivityCount,
              l = n.leaderboardUpdateTimestamp,
              c =
                null == t || null == (a = t.computes) || null == a.hasCurrentItemRankInactivity
                  ? void 0
                  : a.hasCurrentItemRankInactivity(),
              d = s === Pu.ERROR,
              m = s === Pu.BRONZE,
              _ = s === Pu.SILVER,
              E = s === Pu.GOLD,
              g = !d && (m || _ || E),
              p = s === Pu.NOT_IN_LEADERBOARD,
              b = e === yu.TOOLTIP,
              f = e === yu.MODE_SELECTOR,
              h = (({
                isErrorLoadingPointsValue: e,
                isElitePlace: t,
                isTooltip: a,
                isBronze: r,
                isSilver: n,
                isGold: s,
                isNotInLeaderboard: u,
                isModeSelector: o,
              }) => {
                const i = C()(Ws, e && !a && $s, a && e && zs, a && Us),
                  l = C()(mu, a && _u, o && Eu);
                return {
                  baseStyles: i,
                  leftGarlandStyle: C()(Ks, !t && Zs, a && Js, a && nu, o && su, o && eu),
                  rightGarlandStyle: C()(Ks, !t && tu, a && au, a && nu, o && su, o && ru),
                  placeTextStyle: C()(uu, !t && ou, a && lu, u && cu, o && du),
                  placeTextCopiedStyle: C()(uu, ou, iu, a && lu, u && cu, o && du),
                  elitePlaceStyle: C()(js, r && qs, n && Vs, s && Xs, a && Qs, o && Ys),
                  positionTitleStyle: l,
                  lastUpdateNoteStyle: C()(pu, a && bu, a && hu),
                };
              })({
                isErrorLoadingPointsValue: d,
                isElitePlace: g,
                isTooltip: b,
                isBronze: m,
                isSilver: _,
                isGold: E,
                isNotInLeaderboard: p,
                isModeSelector: f,
              }),
              A = h.baseStyles,
              v = h.leftGarlandStyle,
              D = h.rightGarlandStyle,
              F = h.placeTextStyle,
              B = h.placeTextCopiedStyle,
              w = h.elitePlaceStyle,
              S = h.positionTitleStyle,
              P = h.lastUpdateNoteStyle,
              y =
                e === yu.PROGRESSION &&
                (null == (r = t.computes) || null == r.hasCurrentItemRankInactivity
                  ? void 0
                  : r.hasCurrentItemRankInactivity()),
              R = p ? "--" : X.Z5.getNumberFormat(s, X.B3.INTEGRAL);
            return u().createElement(
              "div",
              { className: A },
              d && !f && u().createElement(Hs, { containerStyles: vu }),
              !d &&
                u().createElement(
                  u().Fragment,
                  null,
                  g
                    ? u().createElement("div", { className: w })
                    : u().createElement(
                        "div",
                        { className: Gs },
                        u().createElement("div", { className: v }),
                        u().createElement(Pa, { text: String(R), className: F }),
                        u().createElement(Pa, { text: String(R), className: B }),
                        u().createElement("div", { className: D }),
                      ),
                  u().createElement(Pa, { text: Su.title(), className: S }),
                ),
              u().createElement(
                "div",
                { className: gu },
                !d &&
                  "number" == typeof l &&
                  u().createElement(Na, {
                    timestamp: l,
                    className: P,
                    dividerType: b ? Ta.LINE : Ta.ICON,
                  }),
                !f &&
                  u().createElement(Wa, {
                    text: Su.ratingCount(),
                    binding: { count: u().createElement(Ia, { value: o }) },
                    classMix: C()(pu, b && bu, b && fu),
                  }),
                c &&
                  "number" == typeof i &&
                  y &&
                  u().createElement(wu, { count: i, containerStyles: Au }),
              ),
            );
          },
          ku = "RatingScore_base_bd",
          Tu = "RatingScore_rating_c9",
          xu = "RatingScore_content_62",
          Nu = "RatingScore_score_33",
          Iu = "RatingScore_counter_1a",
          Lu = "RatingScore_title_e4",
          Mu = ({ currentScore: e, hasRankInactivity: t, rankInactivityCount: a, className: r }) =>
            u().createElement(
              "div",
              { className: C()(ku, r) },
              u().createElement(
                "div",
                { className: Tu },
                u().createElement(
                  "div",
                  { className: xu },
                  u().createElement("div", { className: Nu }, e),
                  u().createElement("div", { className: Lu }, R.strings.comp7.ratingScore.title()),
                ),
                t && u().createElement(wu, { containerStyles: Iu, count: a }),
              ),
            ),
          Ou = "ItemFooter_base_0f",
          Hu = "ItemFooter_background_bf",
          Wu = "ItemFooter_divider_bb",
          $u = "ItemFooter_light_79",
          Uu = "ItemFooter_footer_e7",
          zu = "ItemFooter_rankItemFooter_e6",
          Gu = (0, q.Pi)(({ className: e }) => {
            var t;
            const a = Ts().model,
              r = a.root.get(),
              n = r.currentScore,
              s = r.myPosition,
              o = r.rankInactivityCount,
              i = r.currentItemIndex,
              l = a.computes.modelItems(),
              c = a.computes.divisionsConfig(i).currentDivisionIndex,
              d = a.computes.divisions(i),
              m =
                (null == d || null == (t = d[null != c ? c : -1]) ? void 0 : t.type) ===
                Ss.TRANSFER,
              _ = l.findIndex((e) => e.divisions.findIndex((e) => e.type === Ss.TRANSFER) > -1),
              E = l.findIndex((e) => e.divisions.findIndex((e) => e.type === Ss.ELITE) > -1),
              g = isFinite(s) && ((i >= _ && m) || i === E),
              p = C()(Ou, e),
              b = a.computes.hasCurrentItemRankInactivity();
            return u().createElement(
              "div",
              { className: p },
              u().createElement("div", { className: Hu }),
              u().createElement("div", { className: Wu }),
              u().createElement("div", { className: $u }),
              u().createElement(
                "div",
                { className: Uu },
                g
                  ? u().createElement(Ru, { model: a, mode: yu.PROGRESSION })
                  : u().createElement(Mu, {
                      currentScore: n,
                      hasRankInactivity: b,
                      rankInactivityCount: o,
                      className: zu,
                    }),
              ),
            );
          }),
          ju = [
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_6(),
              speedX: 0,
              speedY: 0,
            },
          ],
          qu = () => {
            const e = i.O.view.getSize("rem"),
              t = (0, s.useState)({ height: e.height, width: e.width }),
              a = t[0],
              r = t[1];
            return (
              (0, s.useEffect)(() => {
                const e = (e) => {
                  r(e);
                };
                return (
                  engine.on("screenResized", e),
                  () => {
                    engine.off("screenResized", e);
                  }
                );
              }, []),
              a
            );
          },
          Vu = "Parallax_base_c9",
          Xu = "Parallax_layer_15",
          Qu = "Parallax_shadow_45",
          Yu = [
            R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_1_1(),
            R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_0_1(),
          ],
          Ku = ju.reduce((e, t) => {
            const a = Math.abs(t.speedX);
            return a > e ? a : e;
          }, 0),
          Zu = (0, q.Pi)(({ className: e }) => {
            const t = Ts().model,
              a = qu().width,
              r = (0, s.createRef)(),
              n = Ku * a,
              o = (0, ke.useSpring)({
                to: { opacity: t.isRewardLayerVisible.get() ? 1 : 0 },
                config: { duration: 300 },
              }),
              l = ((e) => {
                const t = (0, s.useCallback)(
                    (t) => {
                      if (!e.current) return;
                      const a = e.current.getBoundingClientRect(),
                        r = a.width,
                        n = a.height;
                      return (
                        0 !== t.clientX &&
                        0 !== t.clientY &&
                        t.clientX <= r - 2 &&
                        t.clientY <= n - 2
                      );
                    },
                    [e],
                  ),
                  a = (0, ke.useSpring)(
                    () => Object.assign({}, i.O.client.getMouseGlobalPosition("px")),
                    [],
                  );
                return (
                  (0, s.useEffect)(() => {
                    const e = (e) => {
                      t(e) && a[1].start({ x: e.clientX, y: e.clientY });
                    };
                    return (
                      document.addEventListener("mousemove", e),
                      () => {
                        document.removeEventListener("mousemove", e);
                      }
                    );
                  }, [t, a]),
                  a
                );
              })(r),
              c = l[0];
            return u().createElement(
              "div",
              { ref: r, className: C()(Vu, e) },
              ju.map((e, t) =>
                u().createElement(
                  ke.animated.div,
                  {
                    key: t,
                    className: Xu,
                    style: Object.assign(
                      {
                        width: `${a + 2 * n}rem`,
                        left: -n + "rem",
                        x: c.x.to((t) => t * e.speedX),
                        y: c.y.to((t) => t * e.speedY),
                        backgroundImage: `url(${e.path})`,
                      },
                      Yu.includes(e.path) && o,
                    ),
                  },
                  3 === t && u().createElement(ke.animated.div, { className: Qu, style: o }),
                ),
              ),
            );
          }),
          Ju = "ParallaxContainer_base_17",
          eo = ju.map((e) => e.path),
          to = (0, q.Pi)(({ className: e }) => {
            const t = Ts(),
              a = t.model,
              r = t.controls,
              n = a.isParallaxPreloaded.get(),
              o = (0, ke.useSpring)({ to: { opacity: n ? 1 : 0 }, config: { duration: 300 } });
            return (
              "success" ===
                ((e) => {
                  const t = (0, s.useState)("pending"),
                    a = t[0],
                    r = t[1];
                  return (
                    (0, s.useLayoutEffect)(() => {
                      let t = 0,
                        a = 0;
                      const n = () => {
                        t + a === e.length && r(0 === t ? "success" : "error");
                      };
                      e.forEach((e) => {
                        const r = new Image();
                        ((r.src = e),
                          r.addEventListener("load", () => {
                            (a++, n());
                          }),
                          r.addEventListener("error", () => {
                            (t++, n());
                          }));
                      });
                    }, [e]),
                    a
                  );
                })(eo) && r.setIsParallaxPreloaded(!0),
              u().createElement(
                ke.animated.div,
                { className: C()(Ju, e), style: o },
                u().createElement(Zu, null),
              )
            );
          }),
          ao = () => {
            const e = (0, s.useState)(i.O.view.getScale()),
              t = e[0],
              a = e[1];
            return (
              (0, s.useEffect)(() => {
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
          ro = { type: "idle" };
        const no = (e, t = 100) =>
            ((viewEnv.pxToRem(i.O.client.getSize("px").width) * t) / 100 - e) / 2,
          so = rr({
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
            getDirection: (e) => (e.deltaY > 1 ? tr.Next : tr.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          uo = "HorizontalBar_base_49",
          oo = "HorizontalBar_base__nonActive_82",
          io = "HorizontalBar_leftButton_5f",
          lo = "HorizontalBar_rightButton_03",
          co = "HorizontalBar_track_0d",
          mo = "HorizontalBar_thumb_fd",
          _o = "HorizontalBar_rail_32",
          Eo = "disable",
          go = { pending: !1, offset: 0 },
          po = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          bo = () => {},
          fo = (e, t) => Math.max(20, e.offsetWidth * t),
          ho = (0, s.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = po, onDrag: r = bo }) => {
              const n = (0, s.useRef)(null),
                o = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                l = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                d = e.stepTimeout || 100,
                m = (0, s.useState)(go),
                _ = m[0],
                E = m[1],
                g = (0, s.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                p = () => {
                  const t = l.current,
                    a = c.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && t && a && n)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    u = Math.min(1, r / n),
                    d = Qa(0, 1, s / (n - r)),
                    m = (t.offsetWidth - fo(t, u)) * d;
                  ((a.style.transform = `translateX(${0 | m}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(Eo), void i.current.classList.remove(Eo));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetWidth - a.offsetWidth) >= -0.5)
                        )
                          return (o.current.classList.remove(Eo), void i.current.classList.add(Eo));
                        var t, a;
                        (o.current.classList.remove(Eo), i.current.classList.remove(Eo));
                      }
                    })(m));
                },
                b = Ja(() => {
                  ((() => {
                    const t = c.current,
                      a = l.current,
                      r = e.getWrapperSize(),
                      s = e.getContainerSize();
                    if (!(s && t && r && a)) return;
                    const u = Math.min(1, r / s);
                    ((t.style.width = `${fo(a, u)}px`),
                      (t.style.display = "flex"),
                      n.current &&
                        (1 === u ? n.current.classList.add(oo) : n.current.classList.remove(oo)));
                  })(),
                    p());
                });
              ((0, s.useEffect)(() => Re(b)),
                (0, s.useEffect)(
                  () =>
                    Re(() => {
                      const t = () => {
                        p();
                      };
                      let a = bo;
                      const r = () => {
                        (a(), (a = Re(b)));
                      };
                      return (
                        e.events.on("recalculateContent", b),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", r),
                        () => {
                          (a(),
                            e.events.off("recalculateContent", b),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", r));
                        }
                      );
                    }),
                  [e],
                ),
                (0, s.useEffect)(() => {
                  if (!_.pending) return;
                  const t = (t) => {
                      var a;
                      const n = e.contentRef.current;
                      if (!n) return;
                      const s = l.current,
                        u = c.current;
                      if (!n || !s || !u) return;
                      const o = t.screenX - _.offset - s.getBoundingClientRect().x,
                        i = (o / s.offsetWidth) * (null != (a = e.getContainerSize()) ? a : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(n, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        r({ type: "dragging", thumb: u, thumbOffset: o, contentOffset: i }));
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t), g(go));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, _.offset, _.pending, r, g]));
              const f = mr((t) => e.applyStepTo(t), d, [e]),
                h = f[0],
                A = f[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", A, !0),
                  () => document.removeEventListener("mouseup", A, !0)
                ),
                [A],
              );
              const v = (e) => {
                e.target.classList.contains(Eo) || W("highlight");
              };
              return u().createElement(
                "div",
                { className: C()(uo, t.base), ref: n, onWheel: e.handleMouseWheel },
                u().createElement("div", {
                  className: C()(io, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Eo) || 0 !== e.button || (W("play"), h(tr.Next));
                  },
                  onMouseUp: A,
                  ref: o,
                  onMouseEnter: v,
                }),
                u().createElement(
                  "div",
                  {
                    className: C()(co, t.track),
                    onMouseDown: (t) => {
                      const r = c.current;
                      if (r && 0 === t.button)
                        if ((W("play"), t.target === r))
                          g({ pending: !0, offset: t.screenX - r.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const r = c.current,
                              n = e.contentRef.current;
                            if (!r || !n) return;
                            const s = a(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + s * t);
                          })(t.screenX > r.getBoundingClientRect().x ? tr.Prev : tr.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: v,
                  },
                  u().createElement("div", { ref: c, className: C()(mo, t.thumb) }),
                  u().createElement("div", { className: C()(_o, t.rail) }),
                ),
                u().createElement("div", {
                  className: C()(lo, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Eo) || 0 !== e.button || (W("play"), h(tr.Prev));
                  },
                  onMouseUp: A,
                  ref: i,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          Ao = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          vo = ({
            children: e,
            api: t,
            className: a,
            barClassNames: r,
            areaClassName: n,
            classNames: o,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: C()(Ao.base, e.base) });
              }, [r]),
              m = (0, s.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return u().createElement(
              "div",
              { className: C()(Ao.defaultScroll, a), onWheel: t.handleMouseWheel },
              u().createElement(
                "div",
                { className: C()(Ao.defaultScrollArea, n) },
                u().createElement(Co, { className: i, api: m, classNames: o }, e),
              ),
              u().createElement(ho, { getStepByRailClick: l, api: t, onDrag: c, classNames: d }),
            );
          },
          Co = ({ api: e, className: t, classNames: a, children: r, style: n }) => (
            (0, s.useEffect)(() => Re(e.recalculateContent)),
            u().createElement(
              "div",
              { className: C()(Ao.base, t), style: n },
              u().createElement(
                "div",
                {
                  className: C()(Ao.wrapper, null == a ? void 0 : a.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                u().createElement(
                  "div",
                  { className: C()(Ao.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          );
        ((Co.Bar = ho),
          (Co.Default = vo),
          (Co.SeniorityAwards = ({ api: e, className: t, classNames: a, children: r }) => (
            (0, s.useEffect)(() => Re(e.recalculateContent)),
            u().createElement(
              "div",
              { className: C()(Ao.base, t) },
              u().createElement(
                "div",
                { className: C()(Ao.wrapper, null == a ? void 0 : a.wrapper), ref: e.wrapperRef },
                u().createElement(
                  "div",
                  { className: C()(Ao.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          )));
        const Do = "ProgressionScroll_base_0f",
          Fo = "ProgressionScroll_areaWrapper_dc",
          Bo = "ProgressionScroll_areaContent_2f",
          wo = ({
            api: e,
            stuckIndex: t,
            itemWidth: a,
            itemsOffset: r = 0,
            children: n,
            onStick: o,
            className: l,
            areaClassNames: c,
            barClassNames: d,
            staticContent: m,
            containerMaxWidth: _,
          }) => {
            const E = viewEnv.remToPx(a),
              g = e.animationScroll,
              p = e.events,
              b = e.applyScroll,
              f = (function (e, t, a) {
                const r = e.contentRef,
                  n = e.wrapperRef,
                  u = e.scrollPosition,
                  o = e.clampPosition,
                  l = e.animationScroll,
                  c = e.events,
                  d = (0, s.useState)(ro),
                  m = d[0],
                  _ = d[1];
                return (
                  (0, s.useEffect)(() => {
                    const e = r.current;
                    e && (e.style.cursor = "dragging" === m.type ? "move" : "grab");
                  }, [r, m.type]),
                  (0, s.useEffect)(() => {
                    if ("dragging" !== m.type) return;
                    const e = i.O.client.events.mouse.move(([e, a]) => {
                        const s = r.current,
                          i = n.current;
                        if (!s || !i) return;
                        if ("inside" === a && e.clientX < 0) return;
                        const c = "inside" === a ? e.clientX : e.clientX - i.offsetLeft,
                          d = m.positionFrom - c,
                          _ = m.previousScrollPosition + d;
                        u.start(
                          Object.assign(
                            {
                              scrollPosition: o(s, _),
                              from: { scrollPosition: l.scrollPosition.get() },
                            },
                            t && { config: t },
                          ),
                        );
                      }),
                      a = i.O.client.events.mouse.up(function () {
                        _({ type: "scrollingToEnd" });
                      });
                    return () => {
                      (e(), a());
                    };
                  }, [l.scrollPosition, o, r, m, u, n, t]),
                  (0, s.useEffect)(() => {
                    if ("scrollingToEnd" !== m.type) return;
                    const e = () => {
                      _(ro);
                    };
                    return (l.scrollPosition.idle && e(), c.on("rest", e), () => c.off("rest", e));
                  }, [l.scrollPosition, m.type, c]),
                  (0, s.useEffect)(() => {
                    const e = r.current;
                    if (!e) return;
                    const t = (e) => {
                      (a &&
                        a.allowedButtons &&
                        -1 === a.allowedButtons.findIndex((t) => e.button === t)) ||
                        _({
                          type: "dragging",
                          positionFrom: e.screenX,
                          previousScrollPosition: l.scrollPosition.get(),
                        });
                    };
                    return (
                      e.addEventListener("mousedown", t),
                      () => e.removeEventListener("mousedown", t)
                    );
                  }, [l.scrollPosition, r, a]),
                  m
                );
              })(e),
              h = (0, s.useCallback)(
                (e) => {
                  b(t * E, e);
                },
                [b, E, t],
              ),
              A = (0, s.useCallback)(() => {
                null == o || o(Math.round(g.scrollPosition.goal / E));
              }, [o, g.scrollPosition, E]);
            ((0, s.useEffect)(() => (p.on("rest", A), () => p.off("rest", A)), [p, A]),
              (0, s.useEffect)(() => {
                const e = () => {
                  h({ immediate: !0, reset: !0 });
                };
                return (
                  p.on("resizeHandled", e),
                  () => {
                    p.off("resizeHandled", e);
                  }
                );
              }, [h, p]),
              (0, s.useEffect)(
                () =>
                  Re(() => {
                    "idle" === f.type && g.scrollPosition.idle && h();
                  }),
                [g.scrollPosition, f, h],
              ));
            const v = (0, s.useCallback)(
              (e) => {
                "dragEnd" === e.type && b(t * E);
              },
              [b, E, t],
            );
            return u().createElement(
              "div",
              {
                className: C()(Do, l),
                style: { "--offset": `${r}rem`, maxWidth: _ ? `${_}rem` : "100%" },
              },
              u().createElement(
                Co,
                {
                  api: e,
                  className: null == c ? void 0 : c.base,
                  classNames: {
                    wrapper: C()(Fo, null == c ? void 0 : c.wrapper),
                    content: C()(Bo, null == c ? void 0 : c.content),
                  },
                },
                n,
              ),
              m,
              u().createElement(ho, { api: e, onDrag: v, classNames: d }),
            );
          },
          So = (e, t = 150, a) => {
            const r = viewEnv.remToPx(e),
              n = (0, s.useMemo)(
                () => ({
                  settings: {
                    step: { type: "fixed", value: r, clampedArrowStepTimeout: t },
                    animationConfig: Object.assign({ frequency: 0.5 }, a),
                  },
                }),
                [a, r, t],
              );
            return so(n);
          },
          Po = {
            "--pageContentWidth": "78vw",
            base: "HighlightedRankEmblem_base_e2",
            highlights: "HighlightedRankEmblem_highlights_cc",
            highlights__gold: "HighlightedRankEmblem_highlights__gold_9f",
            highlights__silver: "HighlightedRankEmblem_highlights__silver_f4",
            highlights__hidden: "HighlightedRankEmblem_highlights__hidden_10",
            highlight: "HighlightedRankEmblem_highlight_72",
            highlightAppearance: "HighlightedRankEmblem_highlightAppearance_60",
            rotate: "HighlightedRankEmblem_rotate_0f",
            highlight__second: "HighlightedRankEmblem_highlight__second_91",
            base__static: "HighlightedRankEmblem_base__static_87",
            rankEmblem: "HighlightedRankEmblem_rankEmblem_29",
            fadeIn: "HighlightedRankEmblem_fadeIn_3a",
            fadeInThreeQuarters: "HighlightedRankEmblem_fadeInThreeQuarters_a4",
            fadeInHalf: "HighlightedRankEmblem_fadeInHalf_6e",
            fadeOut: "HighlightedRankEmblem_fadeOut_48",
            fadeInWithScale: "HighlightedRankEmblem_fadeInWithScale_a8",
            slideUp: "HighlightedRankEmblem_slideUp_82",
            scale: "HighlightedRankEmblem_scale_ec",
            raysAppearance: "HighlightedRankEmblem_raysAppearance_a6",
            "reverse-rotate": "HighlightedRankEmblem_reverse-rotate_e8",
            glowAppearance: "HighlightedRankEmblem_glowAppearance_2a",
            blink: "HighlightedRankEmblem_blink_ce",
            slideUpIn: "HighlightedRankEmblem_slideUpIn_80",
          };
        let yo, Ro;
        (!(function (e) {
          ((e.Silver = "silver"), (e.Gold = "gold"), (e.Hidden = "hidden"));
        })(yo || (yo = {})),
          (function (e) {
            ((e.Dynamic = "dynamic"), (e.Static = "static"));
          })(Ro || (Ro = {})));
        const ko = {
            [Ur.x48]: 64,
            [Ur.x64]: 80,
            [Ur.x110]: 140,
            [Ur.x200]: 260,
            [Ur.x260]: 340,
            [Ur.x320]: 400,
            [Ur.x420]: 550,
          },
          To = ({
            size: e,
            rank: t,
            division: a,
            type: r = Ro.Dynamic,
            state: n,
            classNames: s,
          }) => {
            const o = ((e) => ({
              backgroundImage: `url(${R.images.comp7.gui.maps.icons.comp7.ranks.$num(e).$dyn("highlight")})`,
            }))(e);
            return u().createElement(
              "div",
              { className: C()(Po.base, Po[`base__${r}`]) },
              u().createElement(
                "div",
                {
                  className: C()(
                    Po.highlights,
                    Po[`highlights__${n}`],
                    null == s ? void 0 : s.highlights,
                  ),
                  style: { "--highlightsSize": `${ko[e]}rem` },
                },
                u().createElement("div", {
                  className: C()(
                    Po.highlight,
                    Po.highlight__first,
                    null == s ? void 0 : s.highlight,
                  ),
                  style: o,
                }),
                r === Ro.Dynamic &&
                  u().createElement("div", {
                    className: C()(
                      Po.highlight,
                      Po.highlight__second,
                      null == s ? void 0 : s.highlight,
                    ),
                    style: o,
                  }),
              ),
              u().createElement(zr, {
                size: e,
                rank: t,
                division: a,
                className: C()(Po.rankEmblem, null == s ? void 0 : s.rankEmblem),
              }),
            );
          },
          xo = [Lr.Fifth, Lr.Sixth],
          No = (e, t, a) =>
            e !== Bs.Current || a ? yo.Hidden : xo.includes(t) ? yo.Gold : yo.Silver,
          Io = "RankItemDivider_base_c4",
          Lo = () => u().createElement("div", { className: Io }),
          Mo = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let Oo, Ho;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(Oo || (Oo = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(Ho || (Ho = {})));
        const Wo = ({ size: e = Oo.Default, classMix: t }) =>
            u().createElement("div", { className: C()(Mo.background, Mo[`background__${e}`], t) }),
          $o = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          Uo = ({ size: e }) => {
            const t = C()($o.base, $o[`base__${e}`]);
            return u().createElement("div", { className: t });
          },
          zo = {
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
          Go = (0, s.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: a,
              baseStyles: r,
              isComplete: n,
              withoutBounce: s,
            }) => {
              const o = C()(
                  zo.base,
                  zo[`base__${e}`],
                  a && zo.base__disabled,
                  n && zo.base__finished,
                  s && zo.base__withoutBounce,
                ),
                i = !a && !n;
              return u().createElement(
                "div",
                { className: o, style: r, ref: t },
                u().createElement("div", { className: zo.pattern }),
                u().createElement("div", { className: zo.gradient }),
                i && u().createElement(Uo, { size: e }),
              );
            },
          ),
          jo = ({ size: e, value: t, lineRef: a, disabled: r, onComplete: n }) => {
            const o = (0, s.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              i = 100 === t;
            return (
              (0, s.useEffect)(() => {
                i && n && n();
              }, [i, n]),
              u().createElement(Go, {
                size: e,
                disabled: r,
                baseStyles: o,
                isComplete: i,
                lineRef: a,
              })
            );
          };
        let qo, Vo;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(qo || (qo = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(Vo || (Vo = {})));
        const Xo = "ProgressBarDeltaSimple_base_6c",
          Qo = "ProgressBarDeltaSimple_delta_99",
          Yo = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: r,
              size: n,
              to: o,
              onEndAnimation: i,
              onChangeAnimationState: l,
            }) => {
              const c = o < r,
                d = (0, s.useState)(Vo.Idle),
                m = d[0],
                _ = d[1],
                E = m === Vo.In,
                g = m === Vo.End,
                p = m === Vo.Idle,
                b = (0, s.useCallback)(
                  (e) => {
                    (_(e), l && l(e));
                  },
                  [l],
                );
              ((0, s.useEffect)(() => {
                if (p && !a) {
                  return ut(() => {
                    b(Vo.In);
                  }, t);
                }
              }, [b, a, p, t]),
                (0, s.useEffect)(() => {
                  if (E) {
                    return ut(() => {
                      (i && i(), b(Vo.End));
                    }, e + t);
                  }
                }, [b, E, i, t, e]));
              const f = (0, s.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                h = (0, s.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                A = (0, s.useMemo)(
                  () => ({ width: `${Math.abs(r - o)}%`, left: `${c ? o : r}%` }),
                  [r, c, o],
                );
              return g
                ? null
                : u().createElement(
                    "div",
                    { className: Xo, style: A },
                    u().createElement(
                      "div",
                      { style: p ? f : h, className: Qo },
                      u().createElement(Uo, { size: n }),
                    ),
                  );
            },
          ),
          Ko = (0, s.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: r,
              disabled: n,
              isComplete: o,
              animationSettings: i,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const d = (0, s.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${i.line.duration}ms`,
                  transitionDelay: `${i.line.delay}ms`,
                }),
                [i.line.delay, i.line.duration, e],
              );
              return u().createElement(
                u().Fragment,
                null,
                u().createElement(Go, {
                  size: t,
                  lineRef: r,
                  disabled: n,
                  isComplete: o,
                  baseStyles: d,
                }),
                a >= 0 &&
                  u().createElement(Yo, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    freezed: i.freezed,
                    from: a,
                    size: t,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          Zo = "ProgressBarDeltaGrow_base_7e",
          Jo = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          ei = "ProgressBarDeltaGrow_glow_68",
          ti = (e) => (e ? { left: 0 } : { right: 0 }),
          ai = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          ri = (e) => ({ transitionDuration: `${e}ms` }),
          ni = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: r,
              size: n,
              to: o,
              onEndAnimation: i,
              onChangeAnimationState: l,
              className: c,
            }) => {
              const d = o < r,
                m = (0, s.useState)(qo.Idle),
                _ = m[0],
                E = m[1],
                g = _ === qo.End,
                p = _ === qo.Idle,
                b = _ === qo.Grow,
                f = _ === qo.Shrink,
                h = (0, s.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                ),
                A = (0, s.useCallback)(
                  (e, t) =>
                    ut(() => {
                      h(e);
                    }, t),
                  [h],
                );
              (0, s.useEffect)(() => {
                if (!a)
                  return p
                    ? A(qo.Grow, t)
                    : b
                      ? A(qo.Shrink, e)
                      : f
                        ? A(qo.End, e)
                        : void (g && i && i());
              }, [A, a, g, b, p, f, i, t, e]);
              const v = (0, s.useMemo)(
                  () => Object.assign({ width: "100%" }, ri(e), ti(d)),
                  [d, e],
                ),
                D = (0, s.useMemo)(() => Object.assign({ width: "0%" }, ri(e), ti(d)), [d, e]),
                F = (0, s.useMemo)(
                  () => Object.assign({ width: "0%" }, ai(d, r), ri(e)),
                  [r, d, e],
                ),
                B = (0, s.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - r)}%` }, ai(d, r), ri(e)),
                  [r, d, o, e],
                );
              if (g) return null;
              const w = C()(Zo, c, d && 0 === o && Jo);
              return u().createElement(
                "div",
                { style: p ? F : B, className: w },
                u().createElement(
                  "div",
                  { style: f ? D : v, className: ei },
                  u().createElement(Uo, { size: n }),
                ),
              );
            },
          ),
          si = (0, s.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: r,
              disabled: n,
              isComplete: o,
              animationSettings: i,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const d = e < a,
                m = (0, s.useState)(!1),
                _ = m[0],
                E = m[1],
                g = (0, s.useCallback)(
                  (e) => {
                    (e === qo.Shrink && E(!0), c && c(e));
                  },
                  [c],
                ),
                p = (0, s.useMemo)(() => ({ width: `${a}%`, transitionProperty: "none" }), [a]),
                b = (0, s.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${i.line.duration}ms` }),
                  [i.line.duration, e],
                );
              return u().createElement(
                u().Fragment,
                null,
                u().createElement(Go, {
                  size: t,
                  lineRef: r,
                  disabled: n,
                  isComplete: o,
                  withoutBounce: d && 0 === e,
                  baseStyles: _ ? b : p,
                }),
                a >= 0 &&
                  u().createElement(ni, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    onChangeAnimationState: g,
                    freezed: i.freezed,
                    onEndAnimation: l,
                    from: a,
                    size: t,
                    to: e,
                    className: i.delta.className,
                  }),
              );
            },
          ),
          ui = ["onComplete", "onEndAnimation"];
        function oi() {
          return (
            (oi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            oi.apply(this, arguments)
          );
        }
        const ii = (0, s.memo)((e) => {
            let t = e.onComplete,
              a = e.onEndAnimation,
              r = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, ui);
            const n = (0, s.useState)(!1),
              o = n[0],
              i = n[1],
              l = (0, s.useCallback)(() => {
                const e = 100 === r.to;
                (e !== o && i(e), e && t && t(), a && a());
              }, [o, t, a, r.to]);
            switch (r.animationSettings.type) {
              case Ho.Simple:
                return u().createElement(Ko, oi({}, r, { onEndAnimation: l, isComplete: o }));
              case Ho.Growing:
                return u().createElement(si, oi({}, r, { onEndAnimation: l, isComplete: o }));
              default:
                return null;
            }
          }),
          li = ["onEndAnimation"];
        function ci() {
          return (
            (ci =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            ci.apply(this, arguments)
          );
        }
        const di = (0, s.memo)((e) => {
          let t = e.onEndAnimation,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                r,
                n = {},
                s = Object.keys(e);
              for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
              return n;
            })(e, li);
          const r = (0, s.useRef)({}),
            n = (0, s.useCallback)(() => {
              ((r.current.from = void 0), t && t());
            }, [t]),
            o = "number" == typeof r.current.from ? r.current.from : a.from;
          return (
            (r.current.from = o),
            u().createElement(ii, ci({}, a, { onEndAnimation: n, key: `${o}-${a.to}`, from: o }))
          );
        });
        function mi() {
          return (
            (mi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            mi.apply(this, arguments)
          );
        }
        const _i = (0, s.memo)(
            ({
              size: e,
              value: t,
              lineRef: a,
              disabled: r,
              deltaFrom: n,
              animationSettings: s,
              onEndAnimation: o,
              onChangeAnimationState: i,
              onComplete: l,
            }) => {
              if (n === t)
                return u().createElement(jo, {
                  key: `${n}-${t}`,
                  size: e,
                  value: t,
                  lineRef: a,
                  disabled: r,
                  onComplete: l,
                });
              const c = {
                from: n,
                to: t,
                size: e,
                lineRef: a,
                disabled: r,
                animationSettings: s,
                onComplete: l,
                onEndAnimation: o,
                onChangeAnimationState: i,
              };
              return s.withStack
                ? u().createElement(di, c)
                : u().createElement(ii, mi({ key: `${n}-${t}` }, c));
            },
          ),
          Ei = (e) => ({
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
          gi = (e, t, a) => {
            if ("number" == typeof a) {
              return (Qa(0, t, a) / t) * 100;
            }
            return e;
          },
          pi = {
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
          bi = {
            freezed: !1,
            withStack: !1,
            type: Ho.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          fi = (0, s.memo)(
            ({
              maxValue: e = 100,
              theme: t = pi,
              size: a = Oo.Default,
              animationSettings: r = bi,
              disabled: n = !1,
              withoutBackground: o = !1,
              progressBarBackgroundClassMix: i,
              value: l,
              deltaFrom: c,
              lineRef: d,
              onChangeAnimationState: m,
              onEndAnimation: _,
              onComplete: E,
            }) => {
              const g = ((e, t, a) =>
                (0, s.useMemo)(() => {
                  const r = (Qa(0, t, e) / t) * 100;
                  return { value: r, deltaFrom: gi(r, t, a) };
                }, [a, t, e]))(l, e, c);
              return u().createElement(
                "div",
                { className: C()(Mo.base, Mo[`base__${a}`]), style: Ei(t) },
                !o && u().createElement(Wo, { size: a, classMix: i }),
                u().createElement(_i, {
                  size: a,
                  lineRef: d,
                  disabled: n,
                  value: g.value,
                  deltaFrom: g.deltaFrom,
                  animationSettings: r,
                  onEndAnimation: _,
                  onChangeAnimationState: m,
                  onComplete: E,
                }),
              );
            },
          ),
          hi = "ProgressionDivision_base_6e",
          Ai = "ProgressionDivision_highlightContainer_3d",
          vi = "ProgressionDivision_radialBack_d2",
          Ci = "ProgressionDivision_mainBack_d2",
          Di = "ProgressionDivision_bottomLine_f5",
          Fi = "ProgressionDivision_bottomLine__first_d9",
          Bi = "ProgressionDivision_bottomLine__second_8d",
          wi = "ProgressionDivision_bottomLine__third_91",
          Si = "ProgressionDivision_divisionText_c7",
          Pi = "ProgressionDivision_divisionText__current_74",
          yi = "ProgressionDivision_note_53",
          Ri = ({ rank: e, division: t, isCurrentDivision: a }) => {
            const r = C()(Si, a && Pi);
            return u().createElement(
              Ue,
              {
                contentId: R.views.lobby.comp7.tooltips.DivisionTooltip("resId"),
                args: {
                  rank: e,
                  division: t.name,
                  from: t.from,
                  to: t.to + 1,
                  type: t.type,
                  elitePercent: t.elitePercent,
                },
              },
              u().createElement(
                "div",
                { className: hi },
                a &&
                  u().createElement(
                    "div",
                    { className: Ai },
                    u().createElement("div", { className: vi }),
                    u().createElement("div", { className: Ci }),
                    u().createElement("div", { className: C()(Di, Fi) }),
                    u().createElement("div", { className: C()(Di, Bi) }),
                    u().createElement("div", { className: C()(Di, wi) }),
                  ),
                u().createElement(
                  "div",
                  { className: r },
                  a && u().createElement("div", { className: yi }, R.strings.comp7.division.note()),
                  Ir(t.name),
                ),
              ),
            );
          },
          ki = "RankProgressDivisions_base_54",
          Ti = (0, q.Pi)(({ itemIndex: e, rank: t, customDivisions: a }) => {
            const r = Ts().model,
              n = null != a ? a : r.computes.divisions(e);
            return u().createElement(
              "div",
              { className: ki },
              ve(n, (e) => {
                const a = e.state === Tr.Current;
                return u().createElement(Ri, {
                  key: e.name,
                  rank: t,
                  division: e,
                  isCurrentDivision: a,
                });
              }),
            );
          }),
          xi = {
            point: "RankProgressPoint_point_b1",
            point__top: "RankProgressPoint_point__top_d2",
            point__bottom: "RankProgressPoint_point__bottom_d9",
            pointLine: "RankProgressPoint_pointLine_56",
            pointLine__extended: "RankProgressPoint_pointLine__extended_05",
            pointLine__top: "RankProgressPoint_pointLine__top_0e",
            pointLine__bottom: "RankProgressPoint_pointLine__bottom_ee",
            pointValue: "RankProgressPoint_pointValue_22",
            pointValue__highlight: "RankProgressPoint_pointValue__highlight_65",
            pointValue__top: "RankProgressPoint_pointValue__top_a7",
            pointValue__bottom: "RankProgressPoint_pointValue__bottom_7a",
          },
          Ni = ({
            value: e,
            isHighlightPointValue: t,
            isHaveExtendedPointLine: a,
            style: r,
            direction: n,
          }) => {
            const s = "number" == typeof e ? u().createElement(Ia, { value: e }) : e,
              o = C()(xi.point, xi[`point__${n}`]),
              i = C()(xi.pointLine, xi[`pointLine__${n}`], a && xi.pointLine__extended),
              l = C()(xi.pointValue, xi[`pointValue__${n}`], t && xi.pointValue__highlight);
            return u().createElement(
              "div",
              { className: o, style: r },
              u().createElement("div", { className: i }),
              void 0 !== e && u().createElement("div", { className: l }, s),
            );
          },
          Ii = { "--pointLineWidth": "1rem", base: "RankProgressPoints_base_86" };
        let Li, Mi;
        (!(function (e) {
          ((e.Top = "top"), (e.Bottom = "bottom"));
        })(Li || (Li = {})),
          (function (e) {
            ((e[(e.Start = 0)] = "Start"), (e[(e.End = 1)] = "End"), (e[(e.All = 2)] = "All"));
          })(Mi || (Mi = {})));
        const Oi = (e, t) => {
            const a = t > 0 ? (100 / t) * e + "%" : "0%";
            return e === t
              ? { left: a, transform: `translateX(-${Ii["--pointLineWidth"]})` }
              : { left: a };
          },
          Hi = { [Mi.Start]: (e) => e % 2 == 0, [Mi.End]: (e) => e % 2 == 1, [Mi.All]: () => !0 },
          Wi = ({
            divisionsCount: e,
            from: t,
            currentDivisionIndex: a,
            direction: r = Li.Bottom,
            viewPosition: n = Mi.All,
            divisions: s,
          }) => {
            const o = r === Li.Bottom ? Hi[n] : () => !1,
              i = Math.max(0, e),
              l = (e, a) => {
                var r;
                return (
                  t ||
                  (e === i
                    ? (null != (r = null == a ? void 0 : a.to) ? r : 0) + 1
                    : null == a
                      ? void 0
                      : a.from)
                );
              };
            return u().createElement(
              "div",
              { className: C()(Ii.base, Ii[`base__${r}`]) },
              s
                ? Rr(i + 1, (e) => {
                    const n = s[e === i ? e - 1 : e],
                      c = !t && void 0 !== a && e === a + 1,
                      d = void 0 !== a && e === a,
                      m = void 0 === (null == n ? void 0 : n.from) && (d || c),
                      _ = Boolean(t) && void 0 !== a && e === a - 1;
                    return u().createElement(Ni, {
                      key: `${null == n ? void 0 : n.name}-${e}`,
                      value: o(e) ? l(e, n) : void 0,
                      isHighlightPointValue: c || _,
                      isHaveExtendedPointLine: m,
                      style: Oi(e, i),
                      direction: r,
                    });
                  })
                : u().createElement(Ni, {
                    value: t,
                    isHighlightPointValue: !0,
                    isHaveExtendedPointLine: !0,
                    style: Oi(0, 1),
                    direction: r,
                  }),
            );
          },
          $i = {
            "--pageContentWidth": "78vw",
            base: "RankProgress_base_97",
            base__hidden: "RankProgress_base__hidden_b9",
            base__inactive: "RankProgress_base__inactive_49",
            base__active: "RankProgress_base__active_a2",
            progressWrapper: "RankProgress_progressWrapper_4e",
          },
          Ui = {
            freezed: !0,
            withStack: !1,
            type: Ho.Simple,
            delta: { duration: 0, delay: 0 },
            line: { duration: 0, delay: 0 },
          },
          zi = (0, q.Pi)(({ itemIndex: e, progressState: t }) => {
            const a = Ts().model,
              r = a.root.get().currentScore,
              n = a.qualificationModel.isActive.get(),
              s = a.computes.item(e).rank,
              o = a.computes.rankSettings(e, n).state,
              i = a.computes.divisionsConfig(e),
              l = a.computes.divisions(e).filter((e) => e.type === Ss.BASIC),
              c = l.length,
              d = ys(l),
              m = d.from,
              _ = d.to - m,
              E = 105 * c;
            return u().createElement(
              "div",
              { style: { width: `${E}rem` }, className: C()($i.base, $i[`base__${t}`]) },
              u().createElement(Ti, { itemIndex: e, rank: s, customDivisions: l }),
              u().createElement(Wi, {
                divisionsCount: c,
                direction: Li.Top,
                currentDivisionIndex: i.currentDivisionIndex,
                divisions: l,
              }),
              u().createElement(
                "div",
                { className: $i.progressWrapper },
                o === Bs.Current
                  ? u().createElement(fi, { maxValue: _, value: r - m, animationSettings: Ui })
                  : u().createElement(fi, { maxValue: _, value: r < m ? 0 : _, disabled: r < m }),
              ),
              u().createElement(Wi, {
                divisionsCount: c,
                currentDivisionIndex: i.currentDivisionIndex,
                divisions: l,
              }),
            );
          }),
          Gi = "HighlightedRectangles_base_4c",
          ji = "HighlightedRectangles_triangle_ae",
          qi = "HighlightedRectangles_running_cc",
          Vi = ({ isVisible: e }) => {
            const t = C()(Gi, e && qi);
            return u().createElement(
              "div",
              { className: t },
              u().createElement("div", { className: ji }),
              u().createElement("div", { className: ji }),
              u().createElement("div", { className: ji }),
            );
          },
          Xi = {
            "--pageContentWidth": "78vw",
            base: "RankTransferProgression_base_28",
            transferProgression: "RankTransferProgression_transferProgression_8c",
            transferProgression__inactive:
              "RankTransferProgression_transferProgression__inactive_87",
            progressWrapper: "RankTransferProgression_progressWrapper_f9",
            default: "RankTransferProgression_default_35",
            complete: "RankTransferProgression_complete_e7",
            visible: "RankTransferProgression_visible_c9",
            fadeIn: "RankTransferProgression_fadeIn_17",
            fadeInThreeQuarters: "RankTransferProgression_fadeInThreeQuarters_31",
            fadeInHalf: "RankTransferProgression_fadeInHalf_ee",
            fadeOut: "RankTransferProgression_fadeOut_9d",
            fadeInWithScale: "RankTransferProgression_fadeInWithScale_f9",
            slideUp: "RankTransferProgression_slideUp_2b",
            scale: "RankTransferProgression_scale_28",
            raysAppearance: "RankTransferProgression_raysAppearance_59",
            rotate: "RankTransferProgression_rotate_3d",
            "reverse-rotate": "RankTransferProgression_reverse-rotate_19",
            glowAppearance: "RankTransferProgression_glowAppearance_5c",
            highlightAppearance: "RankTransferProgression_highlightAppearance_12",
            blink: "RankTransferProgression_blink_12",
            slideUpIn: "RankTransferProgression_slideUpIn_f3",
          },
          Qi = (0, q.Pi)(({ itemIndex: e, progressState: t }) => {
            var a, r;
            const n = Ts().model,
              s = n.computes.modelItems(),
              o = n.computes.divisionsConfig(e),
              i = n.computes.divisionsByType(e, Ss.TRANSFER),
              l = s.findIndex((e) => e.divisions.findIndex((e) => e.type === Ss.TRANSFER) > -1),
              c = null == s ? void 0 : s[l],
              d =
                null !=
                (a =
                  null == c || null == (r = c.divisions)
                    ? void 0
                    : r.findIndex((e) => e.type === Ss.TRANSFER && e.state === Tr.Current))
                  ? a
                  : -1,
              m = e === l && d === o.currentDivisionIndex,
              _ = n.computes.rankSettings(e, !1).state === Bs.Previous;
            return u().createElement(
              "div",
              { className: Xi.base },
              u().createElement(zi, { itemIndex: e, progressState: t }),
              u().createElement(
                "div",
                { className: C()(Xi.transferProgression, Xi[`transferProgression__${t}`]) },
                u().createElement(Ti, { itemIndex: e, rank: c.rank, customDivisions: i }),
                u().createElement(Wi, {
                  divisionsCount: 1,
                  direction: Li.Top,
                  currentDivisionIndex: o.currentDivisionIndex,
                  divisions: i,
                }),
                u().createElement(
                  "div",
                  { className: Xi.progressWrapper },
                  u().createElement("div", { className: Xi.default }),
                  u().createElement("div", { className: C()(Xi.complete, _ && Xi.visible) }),
                  u().createElement(Vi, { isVisible: m }),
                ),
                u().createElement(Wi, {
                  divisionsCount: 1,
                  direction: Li.Bottom,
                  currentDivisionIndex: o.currentDivisionIndex,
                  from: R.strings.comp7.rankTransferProgression.transferPoint(),
                  viewPosition: Mi.End,
                  divisions: i,
                }),
              ),
            );
          }),
          Yi = "AchievedRankStatus_base_70",
          Ki = (0, q.Pi)(({ itemIndex: e, progressState: t }) => {
            const a = Ts().model.computes.item(e).rank;
            switch (a) {
              case Lr.First:
              case Lr.Second:
              case Lr.Third:
              case Lr.Fourth:
                return u().createElement(zi, { itemIndex: e, progressState: t });
              case Lr.Fifth:
                return u().createElement(
                  "div",
                  { className: Yi },
                  u().createElement(Qi, { itemIndex: e, progressState: t }),
                );
              default:
                return (
                  console.warn(`Status for rank '${a}' was not mapped to any react component.`),
                  null
                );
            }
          }),
          Zi = "LinkButton_base_fa",
          Ji = { mouseEnter: "highlight", click: "play" },
          el = ({ onClick: e, children: t, className: a }) => {
            const r = (e) => {
              const t = Ji[e];
              t && W(t);
            };
            return u().createElement(
              "div",
              {
                className: C()(Zi, a),
                onClick: (t) => {
                  (r("click"), e(t));
                },
                onMouseEnter: () => {
                  r("mouseEnter");
                },
                onMouseLeave: () => {
                  r("mouseLeave");
                },
              },
              t,
            );
          },
          tl = "HonorRankDescription_base_fd",
          al = "HonorRankDescription_text_38",
          rl = "HonorRankDescription_button_88",
          nl = R.strings.comp7.honorRankDescription,
          sl = (0, q.Pi)(() => {
            var e, t, a;
            const r = Ts(),
              n = r.model,
              s = r.controls,
              o = n.computes.modelItems(),
              i = o.flatMap((e) => e.divisions).find((e) => e.type === Ss.TRANSFER),
              l = o.find((e) => e.divisions.filter((e) => e.type === Ss.ELITE).length > 0),
              c = null != (e = null == i ? void 0 : i.from) ? e : 0,
              d = null != (t = Fs(null != (a = null == l ? void 0 : l.divisions) ? a : [])) ? t : 0;
            return u().createElement(
              "div",
              { className: tl },
              u().createElement(Wa, {
                text: nl.text(),
                binding: {
                  pointCount: u().createElement(
                    u().Fragment,
                    null,
                    X.Z5.getNumberFormat(c, X.B3.INTEGRAL),
                  ),
                  button: u().createElement(
                    u().Fragment,
                    null,
                    u().createElement(
                      el,
                      { className: rl, onClick: () => s.goToLeaderboardPage() },
                      nl.button(),
                    ),
                    u().createElement(Pa, { text: nl.dot(), className: al }),
                  ),
                  percent: d,
                },
                classMix: al,
              }),
            );
          }),
          ul = "RankEliteProgression_base_4d",
          ol = "RankEliteProgression_elite_00",
          il = "RankEliteProgression_elitePercent_61",
          ll = "RankEliteProgression_elitePercent__current_d1",
          cl = (0, q.Pi)(({ itemIndex: e }) => {
            const t = Ts().model,
              a = t.computes.item(e).rank,
              r = t.computes.divisions(e);
            return u().createElement(
              u().Fragment,
              null,
              u().createElement(
                "div",
                { className: ul },
                ve(r, (e) => {
                  const t = e.state === Tr.Current;
                  return u().createElement(Ri, {
                    key: e.name,
                    rank: a,
                    division: e,
                    isCurrentDivision: t,
                  });
                }),
              ),
              u().createElement(
                "div",
                { className: ol },
                ve(r, (e, t) => {
                  const a = e.state === Tr.Current;
                  return u().createElement(Pa, {
                    key: t,
                    text: R.strings.comp7.division.elite(),
                    format: { binding: { elitePercent: e.elitePercent } },
                    className: C()(il, a && ll),
                  });
                }),
              ),
            );
          });
        let dl;
        !(function (e) {
          ((e.Active = "active"), (e.Inactive = "inactive"), (e.Hidden = "hidden"));
        })(dl || (dl = {}));
        const ml = "CurrentRankStatus_base_d4",
          _l = (0, q.Pi)(({ itemIndex: e, progressState: t }) => {
            const a = Ts().model,
              r = a.computes.item(e).rank,
              n = a.qualificationModel.isActive.get(),
              o = a.computes.rankSettings(e, n).division;
            return (
              (0, s.useEffect)(() => {
                t === dl.Active && W("comp_7_progression_rank_active");
              }, [t]),
              u().createElement(
                "div",
                { className: ml },
                (() => {
                  switch (r) {
                    case Lr.First:
                    case Lr.Second:
                    case Lr.Third:
                    case Lr.Fourth:
                      return u().createElement(zi, { itemIndex: e, progressState: t });
                    case Lr.Fifth:
                      return u().createElement(
                        "div",
                        { className: ml },
                        u().createElement(Qi, { itemIndex: e, progressState: t }),
                        o === kr.A && u().createElement(sl, null),
                      );
                    case Lr.Sixth:
                      return u().createElement(
                        "div",
                        { className: ml },
                        u().createElement(cl, { itemIndex: e }),
                        u().createElement(sl, null),
                      );
                    default:
                      return (
                        console.warn(
                          `Status for rank '${r}' was not mapped to any react component.`,
                        ),
                        null
                      );
                  }
                })(),
              )
            );
          }),
          El = "RankStatusDescription_base_07",
          gl = ({ text: e, binding: t, className: a }) => {
            const r = ((e) =>
              "number" == typeof (null == e ? void 0 : e.pointsCount)
                ? Object.assign({}, e, {
                    pointsCount: u().createElement(Ia, { value: e.pointsCount }),
                  })
                : e)(t);
            return u().createElement(Wa, { text: e, binding: r, classMix: C()(El, a) });
          },
          pl = "FutureRankStatus_base_c2",
          bl = "FutureRankStatus_lock_d0",
          fl = (0, q.Pi)(({ itemIndex: e }) => {
            const t = Ts().model,
              a = t.computes.item(e).rank,
              r = t.computes.rankPointsDiapason(e),
              n = r.from,
              o = r.to,
              i = (0, s.useMemo)(() => {
                const e = u().createElement(Ia, { value: n }),
                  t = u().createElement(Ia, { value: o + 1 });
                return a === Lr.Fifth ? { fromScore: e } : { fromScore: e, toScore: t };
              }, [n, o, a]);
            return u().createElement(
              "div",
              { className: pl },
              u().createElement("div", { className: bl }),
              a === Lr.Sixth
                ? u().createElement(sl, null)
                : u().createElement(gl, {
                    text: jr(R.strings.comp7.rankItemStatus.future.description, a),
                    binding: i,
                  }),
            );
          }),
          hl = ({ rankState: e, itemIndex: t, progressState: a }) => {
            switch (e) {
              case Bs.Previous:
                return u().createElement(Ki, { itemIndex: t, progressState: a });
              case Bs.Current:
                return u().createElement(_l, { itemIndex: t, progressState: a });
              case Bs.Future:
                return u().createElement(fl, { itemIndex: t });
              default:
                return (
                  console.error(`Unreachable code for state '${e}' in RankStatusResolver.`),
                  null
                );
            }
          };
        let Al;
        !(function (e) {
          ((e.Progress = "progress"), (e.Text = "text"));
        })(Al || (Al = {}));
        const vl = {
            "--pageContentWidth": "78vw",
            base: "RankItem_base_60",
            rankEmblem__future: "RankItem_rankEmblem__future_08",
            rankDescription: "RankItem_rankDescription_32",
            rankDescription__text: "RankItem_rankDescription__text_90",
            rankDescription__progress: "RankItem_rankDescription__progress_e2",
            rankDescription__viewed: "RankItem_rankDescription__viewed_6b",
            rankInfo: "RankItem_rankInfo_6f",
            dividerContainer: "RankItem_dividerContainer_0f",
            fadeIn: "RankItem_fadeIn_95",
            fadeInThreeQuarters: "RankItem_fadeInThreeQuarters_f1",
            fadeInHalf: "RankItem_fadeInHalf_8a",
            fadeOut: "RankItem_fadeOut_56",
            fadeInWithScale: "RankItem_fadeInWithScale_68",
            slideUp: "RankItem_slideUp_74",
            scale: "RankItem_scale_6b",
            raysAppearance: "RankItem_raysAppearance_a8",
            rotate: "RankItem_rotate_da",
            "reverse-rotate": "RankItem_reverse-rotate_3e",
            glowAppearance: "RankItem_glowAppearance_90",
            highlightAppearance: "RankItem_highlightAppearance_5c",
            blink: "RankItem_blink_7e",
            slideUpIn: "RankItem_slideUpIn_ee",
          },
          Cl = (0, q.Pi)(({ itemIndex: e, isViewed: t, hasDivider: a = !0 }) => {
            const r = Ts().model,
              n = r.qualificationModel.isActive.get(),
              s = P().mediaSize,
              o = r.computes.item(e).rank,
              i = r.computes.rankPointsDiapason(e),
              l = i.from,
              c = i.to,
              d = r.computes.divisionsConfig(e),
              m = r.computes.rankSettings(e, n),
              _ = m.state,
              E = m.division,
              g = ((e) => {
                switch (!0) {
                  case e >= B.ExtraLarge:
                    return Ur.x420;
                  case e >= B.Large:
                    return Ur.x320;
                  case e >= B.Medium:
                    return Ur.x260;
                  default:
                    return Ur.x200;
                }
              })(s),
              p = No(_, o, n),
              b = ((e, t) => (t ? (e === Bs.Current ? dl.Active : dl.Inactive) : dl.Hidden))(_, t),
              f = ((e, t) => {
                const a = Wr(t);
                switch (e) {
                  case Bs.Previous:
                  case Bs.Current:
                    return a ? Al.Progress : Al.Text;
                  default:
                    return Al.Text;
                }
              })(_, o);
            return u().createElement(
              "div",
              { className: vl.base },
              u().createElement(
                Ue,
                {
                  contentId: R.views.lobby.comp7.tooltips.GeneralRankTooltip("resId"),
                  args: {
                    rank: o,
                    divisions: d.list,
                    from: l,
                    to: c + 1,
                    elitePercent: d.elitePercent,
                  },
                },
                u().createElement(
                  "div",
                  null,
                  u().createElement(To, {
                    size: g,
                    rank: o,
                    division: E,
                    state: p,
                    classNames: { rankEmblem: vl[`rankEmblem__${_}`] },
                  }),
                ),
              ),
              u().createElement(
                "div",
                {
                  className: C()(
                    vl.rankDescription,
                    vl[`rankDescription__${f}`],
                    t && vl.rankDescription__viewed,
                  ),
                },
                u().createElement(hl, { rankState: _, itemIndex: e, progressState: b }),
              ),
              a &&
                u().createElement(
                  "div",
                  { className: vl.dividerContainer, style: { "--emblemSize": `${g}rem` } },
                  u().createElement(Lo, null),
                ),
            );
          }),
          Dl = "RankItemContainer_base_b3",
          Fl = "RankItemContainer_title_d5",
          Bl = "RankItemContainer_title__active_f0",
          wl = (0, q.Pi)(
            ({ itemIndex: e, itemWidth: t, isViewed: a, onMouseDown: r, hasDivider: n }) => {
              const s = Ts().model.computes.item(e);
              return u().createElement(
                "div",
                { className: Dl, style: { "--itemWidth": `${t}rem` }, onMouseDown: r },
                u().createElement("div", { className: C()(Fl, a && Bl) }, Vr(s.rank)),
                u().createElement(Cl, { itemIndex: e, isViewed: a, hasDivider: n }),
              );
            },
          ),
          Sl = "Progression_base_97",
          Pl = { base: "Progression_areaContainer_09", wrapper: "Progression_areaWrapper_5f" },
          yl = { base: "Progression_bar_4d" },
          Rl = (0, q.Pi)(
            ({
              staticContent: e,
              className: t,
              currentViewedItemIndex: a,
              setCurrentViewedItemIndex: r,
            }) => {
              const n = Ts().model,
                o = n.root.get().currentItemIndex,
                i = n.computes.itemsLength(),
                l = P().mediaSize,
                c = ao(),
                d = ((e) =>
                  e >= B.ExtraLarge ? 640 : e >= B.Large ? 500 : e >= B.Medium ? 440 : 400)(l),
                m = no(d),
                _ = So(d),
                E = (0, s.useCallback)(
                  (e) => () => {
                    ($.playClick(), r(e));
                  },
                  [r],
                );
              return (
                (0, s.useLayoutEffect)(() => {
                  _.scrollPosition.start({ scrollPosition: viewEnv.remToPx(o * d), immediate: !0 });
                }, [c]),
                u().createElement(
                  wo,
                  {
                    api: _,
                    stuckIndex: a,
                    itemWidth: d,
                    itemsOffset: m,
                    staticContent: e,
                    onStick: r,
                    className: C()(Sl, t),
                    areaClassNames: Pl,
                    barClassNames: yl,
                  },
                  Rr(i, (e) =>
                    u().createElement(wl, {
                      key: e,
                      itemIndex: e,
                      isViewed: a === e,
                      hasDivider: e < i - 1,
                      itemWidth: d,
                      onMouseDown: E(e),
                    }),
                  ),
                )
              );
            },
          ),
          kl = R.strings.comp7.qualification,
          Tl = { hasHtmlContent: !0 },
          xl = ({ maxBattlesCount: e, children: t }) =>
            u().createElement(
              qe,
              {
                header: kl.conditionTooltip.header(),
                body: lt(kl.conditionTooltip.body(e), { maxBattlesCount: e }),
                args: Tl,
              },
              u().createElement("div", null, t),
            ),
          Nl = "BattlesCounter_base_f1",
          Il = "BattlesCounter_battlesCount_ef",
          Ll = ({ battlesCount: e, maxBattlesCount: t, className: a }) =>
            u().createElement(Ct, {
              text: R.strings.comp7.qualification.counter(),
              binding: {
                battlesCount: u().createElement("div", { className: Il }, e),
                maxBattlesCount: t,
              },
              classMix: C()(Nl, a),
            }),
          Ml = {
            "--pageContentWidth": "78vw",
            base: "QualificationBattleItem_base_0d",
            base__size_234: "QualificationBattleItem_base__size_234_ab",
            battleBackground: "QualificationBattleItem_battleBackground_67",
            base__inProgress: "QualificationBattleItem_base__inProgress_2a",
            blink: "QualificationBattleItem_blink_3b",
            fadeIn: "QualificationBattleItem_fadeIn_c9",
            fadeInThreeQuarters: "QualificationBattleItem_fadeInThreeQuarters_20",
            fadeInHalf: "QualificationBattleItem_fadeInHalf_89",
            fadeOut: "QualificationBattleItem_fadeOut_c3",
            fadeInWithScale: "QualificationBattleItem_fadeInWithScale_4f",
            slideUp: "QualificationBattleItem_slideUp_1f",
            scale: "QualificationBattleItem_scale_37",
            raysAppearance: "QualificationBattleItem_raysAppearance_8f",
            rotate: "QualificationBattleItem_rotate_2d",
            "reverse-rotate": "QualificationBattleItem_reverse-rotate_9d",
            glowAppearance: "QualificationBattleItem_glowAppearance_56",
            highlightAppearance: "QualificationBattleItem_highlightAppearance_a0",
            slideUpIn: "QualificationBattleItem_slideUpIn_be",
          },
          Ol = {
            notPlayed: "notFinished",
            inProgress: "notFinished",
            victory: "victory",
            defeat: "defeat",
          },
          Hl = { x173: 173, x234: 234 },
          Wl = ({ className: e, state: t, size: a = "x173" }) => {
            const r = Hl[a],
              n = R.images.comp7.gui.maps.icons.comp7.icons.$dyn(`battle_${Ol[t]}`);
            return u().createElement(
              "div",
              { className: C()(Ml.base, e, Ml[`base__${t}`], Ml[`base__size_${r}`]) },
              u().createElement("div", {
                className: Ml.battleBackground,
                style: { backgroundImage: `url(${n})`, "--imageSize": `${r}rem` },
              }),
            );
          },
          $l = (0, q.Pi)(({ index: e, className: t }) => {
            const a = Ts().model,
              r = P().mediaSize,
              n = a.computes.qualificationBattle(e);
            return u().createElement(Wl, {
              state: n.state,
              className: t,
              key: e,
              size: r >= B.ExtraLarge ? "x234" : "x173",
            });
          }),
          Ul = "BattlesProgression_base_a1",
          zl = "BattlesProgression_item_73",
          Gl = (0, q.Pi)(({ className: e }) => {
            const t = Ts().model;
            return u().createElement(
              "div",
              { className: C()(Ul, e) },
              Rr(t.computes.qualificationBattlesLength(), (e) =>
                u().createElement($l, { index: e, className: zl, key: e }),
              ),
            );
          }),
          jl = "Qualification_base_0f",
          ql = "Qualification_content_64",
          Vl = "Qualification_footer_8f",
          Xl = "Qualification_qualificationEmblem_e2",
          Ql = "Qualification_battlesProgression_51",
          Yl = "Qualification_counterDescription_20",
          Kl = "Qualification_ratingCalculationDescription_7a",
          Zl = "Qualification_timerIcon_35",
          Jl = "Qualification_conditionContainer_c4",
          ec = "Qualification_condition_23",
          tc = "Qualification_rewardsDescription_c2",
          ac = "Qualification_infoIcon_fe",
          rc = "Qualification_rewardsButton_db",
          nc = "Qualification_buttonIcon_39",
          sc = "Qualification_waiting_de",
          uc = R.strings.comp7.qualification,
          oc = { base: rc, icon: nc },
          ic = (0, q.Pi)(({ className: e }) => {
            const t = Ts(),
              a = t.model,
              r = t.controls,
              n = a.qualificationModel.battlesCount.get(),
              s = a.qualificationModel.maxBattlesCount.get(),
              o = a.qualificationModel.isRatingCalculation.get(),
              i = a.isParallaxPreloaded.get(),
              l = (0, ke.useSpring)({
                from: { opacity: 0 },
                to: ee() ? { opacity: i ? 1 : 0 } : { opacity: 1 },
                delay: 300,
                config: { duration: 300 },
              });
            return ee() && !i
              ? u().createElement("div", { className: sc }, u().createElement(tt, null))
              : u().createElement(
                  ke.animated.div,
                  { style: l, className: C()(jl, e) },
                  u().createElement(
                    "div",
                    { className: ql },
                    u().createElement("div", { className: Xl }),
                    o
                      ? u().createElement(
                          u().Fragment,
                          null,
                          u().createElement(Ll, { battlesCount: n, maxBattlesCount: s }),
                          u().createElement(
                            qe,
                            { body: R.strings.comp7.qualification.ratingCalculationTooltip() },
                            u().createElement(
                              "div",
                              null,
                              u().createElement(Ct, {
                                text: uc.ratingCalculationDescription(),
                                binding: { timerIcon: u().createElement("div", { className: Zl }) },
                                classMix: Kl,
                              }),
                            ),
                          ),
                        )
                      : u().createElement(Wa, {
                          text: uc.counterWithDescription(),
                          classMix: Yl,
                          binding: {
                            counter: u().createElement(Ll, { battlesCount: n, maxBattlesCount: s }),
                          },
                        }),
                    u().createElement(Gl, { className: Ql }),
                  ),
                  u().createElement(
                    "div",
                    { className: Vl },
                    u().createElement(
                      "div",
                      { className: Jl },
                      u().createElement(Wa, {
                        text: uc.condition(s),
                        classMix: ec,
                        binding: { maxBattlesCount: s },
                      }),
                      u().createElement(
                        xl,
                        { maxBattlesCount: s },
                        u().createElement("div", { className: ac }),
                      ),
                    ),
                    u().createElement(Ct, { text: uc.rewardsDescription(), classMix: tc }),
                    u().createElement(j, {
                      caption: uc.rewardsButton(),
                      classNames: oc,
                      onMouseEnter: () => r.setRewardLayerVisible(!0),
                      onMouseLeave: () => r.setRewardLayerVisible(!1),
                      onClick: () => r.goToRankRewardsPage(),
                      soundHover: "comp_7_rank_rewards_hover",
                    }),
                  ),
                );
          }),
          lc = {
            "--pageContentWidth": "78vw",
            base: "ProgressionPage_base_fa",
            bgLayer: "ProgressionPage_bgLayer_41",
            bgLayer__iron: "ProgressionPage_bgLayer__iron_79",
            bgLayer__bronze: "ProgressionPage_bgLayer__bronze_46",
            bgLayer__silver: "ProgressionPage_bgLayer__silver_53",
            bgLayer__gold: "ProgressionPage_bgLayer__gold_ef",
            bgLayer__champion: "ProgressionPage_bgLayer__champion_73",
            bgLayer__legend: "ProgressionPage_bgLayer__legend_8f",
            parallaxContainer: "ProgressionPage_parallaxContainer_c4",
            contentWrapper: "ProgressionPage_contentWrapper_cf",
            content: "ProgressionPage_content_4a",
            content__progression: "ProgressionPage_content__progression_c5",
            footer: "ProgressionPage_footer_d1",
            fadeIn: "ProgressionPage_fadeIn_16",
            fadeInThreeQuarters: "ProgressionPage_fadeInThreeQuarters_a8",
            fadeInHalf: "ProgressionPage_fadeInHalf_9d",
            fadeOut: "ProgressionPage_fadeOut_0e",
            fadeInWithScale: "ProgressionPage_fadeInWithScale_ee",
            slideUp: "ProgressionPage_slideUp_e2",
            scale: "ProgressionPage_scale_2c",
            raysAppearance: "ProgressionPage_raysAppearance_a2",
            rotate: "ProgressionPage_rotate_75",
            "reverse-rotate": "ProgressionPage_reverse-rotate_bc",
            glowAppearance: "ProgressionPage_glowAppearance_12",
            highlightAppearance: "ProgressionPage_highlightAppearance_da",
            blink: "ProgressionPage_blink_57",
            slideUpIn: "ProgressionPage_slideUpIn_0f",
          },
          cc = R.strings.comp7.page.heading,
          dc = (0, q.Pi)(() => {
            const e = Ts().model,
              t = e.root.get().currentItemIndex,
              a = (0, s.useState)(t),
              r = a[0],
              n = a[1];
            (0, s.useLayoutEffect)(() => {
              n(t);
            }, [t]);
            const o = Is(r, 200, 500),
              i = o.currentBg,
              l = o.prevBg,
              c = o.spring,
              d = e.qualificationModel.isActive.get(),
              m = (0, ke.useSpring)(_e);
            return u().createElement(
              "div",
              { className: lc.base },
              u().createElement("div", { className: C()(lc.bgLayer, lc[`bgLayer__${i}`]) }),
              l &&
                u().createElement(ke.animated.div, {
                  style: c,
                  className: C()(lc.bgLayer, lc[`bgLayer__${l}`]),
                }),
              ee() && d && u().createElement(to, { className: lc.parallaxContainer }),
              u().createElement(st, { className: K }, d ? cc.qualification() : cc.progression()),
              u().createElement(It, null),
              d
                ? u().createElement(
                    "div",
                    { className: lc.contentWrapper },
                    u().createElement(ic, { className: lc.content }),
                  )
                : u().createElement(
                    ke.animated.div,
                    { style: m, className: lc.contentWrapper },
                    u().createElement(Rl, {
                      className: C()(lc.content, lc.content__progression),
                      staticContent: u().createElement(Gu, { className: lc.footer }),
                      currentViewedItemIndex: r,
                      setCurrentViewedItemIndex: n,
                    }),
                  ),
            );
          }),
          mc = { context: "model.progressionModel" },
          _c = oe()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  qualification: e.primitives(["isActive"], "qualificationModel"),
                },
                a = e.array("items"),
                r = (0, Ee.Om)(() => a.get().length),
                n = (0, Ee.Om)(
                  (e) => {
                    const t = fe(a.get(), e);
                    if (!t) throw new Error(`rank rewards item with index ${e} was not found`);
                    return {
                      hasRewardsReceived: t.hasRewardsReceived,
                      rank: t.rank,
                      from: t.from,
                      to: t.to,
                    };
                  },
                  { equals: ae },
                ),
                s = (0, Ee.Om)(
                  (e) => {
                    const t = fe(a.get(), e);
                    if (!t) throw new Error(`rank rewards item with index ${e} was not found`);
                    return ve(t.rewards, (e) => Object.assign({}, e));
                  },
                  { equals: ae },
                ),
                u = (0, Ee.Om)(
                  (e) => {
                    const t = fe(s(e), 0);
                    if (!t)
                      throw new Error(
                        `rank rewards item with index ${e} has no any main reward at index: 0`,
                      );
                    return t;
                  },
                  { equals: ae },
                ),
                o = (0, Ee.Om)((e) => [...Ce(s(e), 1)], { equals: ae }),
                i = (0, Ee.Om)((e) => {
                  const t = fe(a.get(), e);
                  if (!t) throw new Error(`item with index ${e} was not found`);
                  const r = ve(t.divisions, (e) => Object.assign({}, e));
                  return Ds(r);
                }),
                l = (0, Ee.Om)((e) => {
                  const t = fe(a.get(), e);
                  if (!t) throw new Error(`item with index ${e} was not found`);
                  const r = ve(t.divisions, (e) => Object.assign({}, e));
                  return Fs(r);
                }),
                c = (0, Ee.Om)(
                  () => {
                    const e = Fe(a.get(), (e) => !e.hasRewardsReceived);
                    return {
                      nextNotAchievedItemIndex: null != e ? e : r(),
                      hasForceScroll: -1 !== t.root.get().initialItemIndex,
                    };
                  },
                  { equals: zt },
                );
              return Object.assign({}, t, {
                computes: {
                  rankRewardsItemsLength: r,
                  rankRewardsItem: n,
                  mainReward: u,
                  additionalRewards: o,
                  additionalRewardsCount: (0, Ee.Om)((e) => o(e).length),
                  divisionsString: i,
                  elitePercent: l,
                  scrollingSettings: c,
                },
              });
            },
            ({ externalModel: e, model: t }) => {
              const a = e.createCallback((e, t) => ({ rank: e, index: t }), "onPreviewOpen");
              return {
                openComp7Shop: e.createCallbackNoArgs("onComp7ShopOpen"),
                goToPreview: (0, re.aD)((e, r) => {
                  const n = t.computes.rankRewardsItem(e).rank;
                  a(n, r);
                }),
              };
            },
          ),
          Ec = _c[0],
          gc = _c[1];
        let pc, bc, fc, hc, Ac, vc, Cc, Dc, Fc;
        function Bc() {
          return (
            (Bc =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Bc.apply(this, arguments)
          );
        }
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
            (e.RewardsSlots = "rewardsSlots"),
            (e.WtStamp = "stamp"),
            (e.WtHunter = "wt_hunter"),
            (e.WtBoss = "wt_boss"),
            (e.WtHunterCollection = "hunter_collection"),
            (e.WtTicket = "wtevent_ticket"),
            (e.WtMainPrizeDiscount = "main_prize_discount"),
            (e.WtTicket25 = "wtevent_ticket25"));
        })(pc || (pc = {})),
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
          })(bc || (bc = {})),
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
          })(fc || (fc = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(hc || (hc = {})),
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
          })(Ac || (Ac = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(vc || (vc = {})),
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
          })(Cc || (Cc = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(Dc || (Dc = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Fc || (Fc = {})));
        const wc = ({ children: e, tooltipArgs: t, className: a }) => {
            if (!t) return e;
            const r = u().createElement("div", { className: a }, e);
            if (t.header || t.body) return u().createElement(qe, t, r);
            const n = t.contentId,
              s = t.args,
              o = null == s ? void 0 : s.contentId;
            return n || o
              ? u().createElement(Ue, Bc({}, t, { contentId: n || o }), r)
              : u().createElement(Bt, t, r);
          },
          Sc = [
            pc.Items,
            pc.Equipment,
            pc.Xp,
            pc.XpFactor,
            pc.Blueprints,
            pc.BlueprintsAny,
            pc.Goodies,
            pc.Berths,
            pc.Slots,
            pc.Tokens,
            pc.CrewSkins,
            pc.CrewBooks,
            pc.Customizations,
            pc.CreditsFactor,
            pc.TankmenXp,
            pc.TankmenXpFactor,
            pc.FreeXpFactor,
            pc.BattleToken,
            pc.PremiumUniversal,
            pc.NaturalCover,
            pc.BpCoin,
            pc.BattlePassSelectToken,
            pc.BattlaPassFinalAchievement,
            pc.BattleBadge,
            pc.BonusX5,
            pc.CrewBonusX3,
            pc.NewYearFillers,
            pc.NewYearInvoice,
            pc.EpicSelectToken,
            pc.Comp7TokenWeeklyReward,
            pc.Comp7TokenCouponReward,
            pc.BattleBoosterGift,
            pc.CosmicLootboxCommon,
            pc.CosmicLootboxSilver,
            pc.SelectableBonus,
            pc.PostStamp,
            pc.PremiumPlusUniversal,
            pc.GoldenTicket,
            pc.RewardsSlots,
            pc.WtStamp,
            pc.WtTicket,
            pc.WtMainPrizeDiscount,
            pc.WtHunter,
            pc.WtHunterCollection,
          ],
          Pc = [pc.Gold, pc.Credits, pc.Crystal, pc.FreeXp],
          yc = [pc.BattlePassPoints],
          Rc = [pc.PremiumPlus, pc.Premium];
        let kc;
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
        })(kc || (kc = {}));
        const Tc = ["engravings", "backgrounds"],
          xc = ["engraving", "background"],
          Nc = (e, t = fc.Small) => {
            const a = e.name,
              r = e.type,
              n = e.value,
              s = e.icon,
              u = e.item,
              o = e.dogTagType,
              i = ((e) => {
                switch (e) {
                  case fc.S600x450:
                    return "c_600x450";
                  case fc.S400x300:
                    return "c_400x300";
                  case fc.S296x222:
                    return "c_296x222";
                  case fc.S232x174:
                    return "c_232x174";
                  case fc.Big:
                    return "c_80x80";
                  case fc.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(t);
            switch (a) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${r}_${n}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}_plus_${n}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}_${n}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${u}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${t}.${s}`;
              case "tokens":
              case "battleToken":
                return ((e, t) => {
                  switch (t) {
                    case fc.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case fc.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.${e.icon}`;
                  }
                })(e, t);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${t}.${s}`;
              case "dogTagComponents":
                return ((e, t, a) => {
                  const r = Tc[e];
                  if (r) {
                    const n = R.images.gui.maps.icons.dogtags.$dyn(t).$dyn(r),
                      s = n.$dyn(a);
                    return s ? `${s}` : `${n.$dyn(xc[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, t, s);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${i}.${s}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case fc.S600x450:
                      return "c_600x450";
                    case fc.S400x300:
                      return "c_400x300";
                    case fc.S296x222:
                      return "c_296x222";
                    case fc.S232x174:
                      return "c_232x174";
                    case fc.S180x135:
                      return "big";
                    case fc.Big:
                    case fc.S80x80:
                      return "c_80x80";
                    case fc.Small:
                    case fc.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(t)}.${s}`;
              case "xp":
              case "xpFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.exp`;
              case "creditsFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.credits`;
              case "tankmenXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.tankmenXP`;
              case "dailyXPFactor":
              case "freeXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.freeXP`;
              case "tmanToken":
              case "battlePassSelectToken":
              case "selectableBonus":
              case "groups":
              case "lootBoxToken":
              case "customizations":
              case "crewSkins":
              case "goodies":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${s}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${i}.${s}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case fc.Mini:
                      return kc.s32;
                    case fc.Small:
                    case fc.S48x48:
                      return kc.s48;
                    case fc.S80x80:
                    case fc.Big:
                      return kc.s80;
                    case fc.S128x100:
                      return kc.s116;
                    case fc.S180x135:
                    case fc.S232x174:
                    case fc.S296x222:
                      return kc.s296;
                    case fc.S400x300:
                      return kc.s400;
                    case fc.S600x450:
                      return kc.s600;
                  }
                })(t)}`;
              case pc.StyleProgress:
              case pc.LbStyleProgress:
                return Ic(s, t, Fc.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}`;
            }
          },
          Ic = (e, t, a) => {
            const r = R.images.gui.maps.icons.quests.bonuses.$dyn(t),
              n = r.$dyn(e);
            return String(null != n ? n : r.$dyn(a));
          },
          Lc = {
            base: "Reward_base_ea",
            base__s48x48: "Reward_base__s48x48_46",
            base__small: "Reward_base__small_c0",
            base__s80x80: "Reward_base__s80x80_ce",
            base__big: "Reward_base__big_e5",
            base__s128x100: "Reward_base__s128x100_c3",
            base__s180x135: "Reward_base__s180x135_7c",
            base__s232x174: "Reward_base__s232x174_67",
            base__s296x222: "Reward_base__s296x222_78",
            base__s400x300: "Reward_base__s400x300_07",
            base__s600x450: "Reward_base__s600x450_f8",
            tooltipWrapper: "Reward_tooltipWrapper_b5",
            icon: "Reward_icon_df",
            overlay: "Reward_overlay_68",
            highlight: "Reward_highlight_36",
            image: "Reward_image_89",
            info: "Reward_info_72",
            info__multi: "Reward_info__multi_63",
            info__credits: "Reward_info__credits_ef",
            info__gold: "Reward_info__gold_36",
            info__crystal: "Reward_info__crystal_36",
            info__premiumTank: "Reward_info__premiumTank_d3",
            timer: "Reward_timer_d3",
          },
          Mc = ({
            name: e,
            image: t,
            isPeriodic: a = !1,
            size: r = fc.Big,
            special: n,
            value: s,
            valueType: o,
            style: i,
            className: l,
            classNames: c,
            tooltipArgs: d,
            periodicIconTooltipArgs: m,
          }) => {
            const _ = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Ac.BATTLE_BOOSTER:
                  case Ac.BATTLE_BOOSTER_REPLACE:
                    return vc.BATTLE_BOOSTER;
                }
              })(n),
              E = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Ac.BATTLE_BOOSTER:
                    return Cc.BATTLE_BOOSTER;
                  case Ac.BATTLE_BOOSTER_REPLACE:
                    return Cc.BATTLE_BOOSTER_REPLACE;
                  case Ac.BUILT_IN_EQUIPMENT:
                    return Cc.BUILT_IN_EQUIPMENT;
                  case Ac.EQUIPMENT_PLUS:
                    return Cc.EQUIPMENT_PLUS;
                  case Ac.EQUIPMENT_TROPHY_BASIC:
                    return Cc.EQUIPMENT_TROPHY_BASIC;
                  case Ac.EQUIPMENT_TROPHY_UPGRADED:
                    return Cc.EQUIPMENT_TROPHY_UPGRADED;
                  case Ac.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return Cc.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case Ac.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return Cc.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case Ac.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return Cc.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case Ac.PROGRESSION_STYLE_UPGRADED_1:
                    return Cc.PROGRESSION_STYLE_UPGRADED_1;
                  case Ac.PROGRESSION_STYLE_UPGRADED_2:
                    return Cc.PROGRESSION_STYLE_UPGRADED_2;
                  case Ac.PROGRESSION_STYLE_UPGRADED_3:
                    return Cc.PROGRESSION_STYLE_UPGRADED_3;
                  case Ac.PROGRESSION_STYLE_UPGRADED_4:
                    return Cc.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(n),
              g = ((e, t) => {
                if (void 0 === e) return null;
                switch (t) {
                  case hc.MULTI: {
                    const t = Number(e);
                    return isFinite(t) && t > 1 ? `x${Math.floor(t)}` : null;
                  }
                  case hc.CURRENCY:
                  case hc.NUMBER:
                    return u().createElement(Ia, { format: "integral", value: Number(e) });
                  case hc.PREMIUM_PLUS: {
                    const t = Number(e);
                    return isNaN(t) ? e : null;
                  }
                  default:
                    return e;
                }
              })(s, o);
            return u().createElement(
              "div",
              { className: C()(Lc.base, Lc[`base__${r}`], l), style: i },
              u().createElement(
                wc,
                { tooltipArgs: d, className: Lc.tooltipWrapper },
                u().createElement(
                  u().Fragment,
                  null,
                  u().createElement(
                    "div",
                    { className: C()(Lc.image, null == c ? void 0 : c.image) },
                    _ &&
                      u().createElement("div", {
                        className: C()(Lc.highlight, null == c ? void 0 : c.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${r}.${_}_highlight)`,
                        },
                      }),
                    t &&
                      u().createElement("div", {
                        className: C()(Lc.icon, null == c ? void 0 : c.rewardIcon),
                        style: { backgroundImage: `url(${t})` },
                      }),
                    E &&
                      u().createElement("div", {
                        className: C()(Lc.overlay, null == c ? void 0 : c.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${r}.${E}_overlay)`,
                        },
                      }),
                  ),
                  g &&
                    u().createElement(
                      "div",
                      {
                        className: C()(
                          Lc.info,
                          Lc[`info__${e}`],
                          o === hc.MULTI && Lc.info__multi,
                          null == c ? void 0 : c.info,
                        ),
                      },
                      g,
                    ),
                ),
              ),
              a &&
                u().createElement(
                  wc,
                  { tooltipArgs: m },
                  u().createElement("div", {
                    className: C()(Lc.timer, null == c ? void 0 : c.periodicIcon),
                  }),
                ),
            );
          },
          Oc = "Rewards_base_26",
          Hc = "Rewards_base__vertical_9f",
          Wc = "Rewards_reward_7b",
          $c = "Rewards_reward__vertical_c6";
        function Uc() {
          return (
            (Uc =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Uc.apply(this, arguments)
          );
        }
        const zc = u().memo(
            ({
              data: e,
              size: t = fc.Big,
              isVertical: a = !1,
              count: r,
              classMix: n,
              rewardItemClassMix: o,
              boxRewardTooltip: i,
              boxRewardValue: l,
            }) => {
              const c = (0, s.useMemo)(
                  () =>
                    r && r < e.length ? `R.images.gui.maps.icons.quests.bonuses.${t}.default` : "",
                  [r, e.length, t],
                ),
                d =
                  l ||
                  lt(R.strings.tooltips.quests.awards.additional.bottom(), {
                    count: e.length - (r || 0),
                  }),
                m = C()(Oc, a && Hc, n),
                _ = C()(Wc, a && $c, o);
              return u().createElement(
                "div",
                { className: m },
                c
                  ? u().createElement(
                      u().Fragment,
                      null,
                      e
                        .slice(0, r)
                        .map((e, a) =>
                          u().createElement(
                            "div",
                            { key: a, className: _ },
                            u().createElement(Mc, Uc({ size: t }, e)),
                          ),
                        ),
                      u().createElement(
                        "div",
                        { className: _ },
                        u().createElement(Mc, {
                          name: "more",
                          image: c,
                          size: t,
                          value: d,
                          tooltipArgs: i,
                        }),
                      ),
                    )
                  : e.map((e, a) =>
                      u().createElement(
                        "div",
                        { key: a, className: _ },
                        u().createElement(Mc, Uc({ size: t }, e)),
                      ),
                    ),
              );
            },
          ),
          Gc = ["overlayType"];
        const jc = (e, t) => {
            if ("dogTagComponents" === e.name) {
              if (t === fc.Big) return fc.S80x80;
              if (t === fc.Small) return fc.S48x48;
            }
            return t;
          },
          qc = (e) => ("vehicles_rent" === e.name ? e.label : e.value),
          Vc = ({ reward: e, rank: t, index: a }) => {
            const r = e.tooltipId,
              n = e.tooltipContentId;
            return ((e, t, a) => {
              const r = t && { contentId: t };
              return Object.assign(
                {
                  args: e,
                  isEnabled: Boolean((e && e.tooltipId) || t),
                  ignoreMouseClick: !0,
                  ignoreShowDelay: !t,
                },
                r,
                a,
              );
            })(
              Object.assign(
                { tooltipId: r },
                void 0 !== t && { rank: t },
                void 0 !== a && { index: a },
              ),
              Number(n),
              { ignoreShowDelay: !0 },
            );
          },
          Xc = ({ reward: e, size: t, rank: a, index: r }) => {
            const n = e.overlayType,
              s = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, Gc),
              u = jc(e, t);
            return Object.assign({}, s, {
              size: u,
              image: Nc(e, u),
              value: qc(e),
              valueType:
                ((o = e.name),
                Sc.includes(o)
                  ? hc.MULTI
                  : Pc.includes(o)
                    ? hc.CURRENCY
                    : yc.includes(o)
                      ? hc.NUMBER
                      : Rc.includes(o)
                        ? hc.PREMIUM_PLUS
                        : hc.STRING),
              special: n,
              tooltipArgs: Vc({ reward: e, rank: a, index: r }),
              periodicIconTooltipArgs: {
                header: R.strings.tooltips.periodicReward.header(),
                body: R.strings.tooltips.periodicReward.comp7.body(),
              },
            });
            var o;
          },
          Qc = ({ rewards: e, size: t, rank: a, index: r }) =>
            ve(e, (e) => Xc({ reward: e, size: t, rank: a, index: r })),
          Yc = (e, t) => (e > t ? t - 1 : void 0),
          Kc = "AdditionalRewards_reward_16",
          Zc = "AdditionalRewards_vehiclesRentBase_d4",
          Jc = "AdditionalRewards_vehiclesRentLabel_3e",
          ed = fc.Small,
          td = (0, q.Pi)(({ rank: e, itemIndex: t, visibleRewardsCount: a, className: r }) => {
            const n = gc().model,
              s = n.computes.additionalRewards(t),
              o = n.computes.additionalRewardsCount(t),
              i = ve(s, (t) => {
                const a = "vehicles_rent" === t.name;
                return Object.assign({}, Xc({ reward: t, size: ed, rank: e }), {
                  className: C()(a && Zc),
                  classNames: { info: C()(a && Jc) },
                });
              });
            return u().createElement(zc, {
              data: i,
              size: ed,
              count: Yc(o, a),
              rewardItemClassMix: Kc,
              boxRewardTooltip: {
                contentId: R.views.lobby.tooltips.AdditionalRewardsTooltip("resId"),
                args: { fromIndex: a, rank: e },
              },
              classMix: r,
            });
          });
        let ad;
        !(function (e) {
          ((e[(e.NotStarted = 0)] = "NotStarted"),
            (e[(e.Active = 1)] = "Active"),
            (e[(e.OffSeason = 3)] = "OffSeason"),
            (e[(e.Finished = 4)] = "Finished"));
        })(ad || (ad = {}));
        const rd = {
            base: "Heading_base_99",
            tooltipArea: "Heading_tooltipArea_c9",
            rankEmblem__future: "Heading_rankEmblem__future_6d",
            lock: "Heading_lock_a8",
            description: "Heading_description_6f",
            rankName: "Heading_rankName_05",
            rankStatus: "Heading_rankStatus_63",
          },
          nd = (0, q.Pi)(
            ({
              rank: e,
              from: t,
              to: a,
              elitePercent: r,
              divisions: n,
              rankEmblemSize: s,
              rankState: o,
            }) => {
              const i = gc().model,
                l = ce().model,
                c = i.qualification.isActive.get(),
                d = No(o, e, c),
                m = o === Bs.Current && !c;
              return u().createElement(
                "div",
                { className: rd.base },
                u().createElement(
                  Ue,
                  {
                    contentId: R.views.lobby.comp7.tooltips.GeneralRankTooltip("resId"),
                    ignoreShowDelay: !0,
                    args: { rank: e, divisions: n, from: t, to: a, elitePercent: r },
                  },
                  u().createElement(
                    "div",
                    { className: rd.tooltipArea },
                    u().createElement(To, {
                      rank: e,
                      size: s,
                      type: Ro.Static,
                      state: d,
                      classNames: { rankEmblem: rd[`rankEmblem__${o}`] },
                    }),
                    o === Bs.Future && u().createElement("div", { className: rd.lock }),
                  ),
                ),
                u().createElement(
                  "div",
                  { className: rd.description },
                  u().createElement("div", { className: rd.rankName }, Vr(e)),
                  m &&
                    u().createElement(
                      "div",
                      { className: rd.rankStatus },
                      ((e) => {
                        switch (e) {
                          case ad.OffSeason:
                          case ad.Finished:
                            return R.strings.comp7.rank.achieved();
                          case ad.Active:
                            return R.strings.comp7.rank.current();
                          default:
                            return "";
                        }
                      })(l.year.state.get()),
                    ),
                ),
              );
            },
          ),
          sd = {
            base: "Preview_base_1f",
            base__hovered: "Preview_base__hovered_ee",
            icon: "Preview_icon_f3",
            icon__small: "Preview_icon__small_a1",
            icon__normal: "Preview_icon__normal_5c",
            base__mouseDown: "Preview_base__mouseDown_d0",
            label: "Preview_label_2e",
            base__visibleLabel: "Preview_base__visibleLabel_92",
          },
          ud = [
            "label",
            "isVisibleLabel",
            "autofocus",
            "soundHover",
            "soundClick",
            "size",
            "classNames",
            "onClick",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onMouseUp",
            "onFocus",
            "onBlur",
          ];
        function od() {
          return (
            (od =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            od.apply(this, arguments)
          );
        }
        let id;
        !(function (e) {
          ((e.SMALL = "small"), (e.NORMAL = "normal"));
        })(id || (id = {}));
        const ld = (0, s.memo)((e) => {
            let t = e.label,
              a = e.isVisibleLabel,
              r = void 0 !== a && a,
              n = e.autofocus,
              o = void 0 !== n && n,
              i = e.soundHover,
              l = void 0 === i ? "highlight" : i,
              c = e.soundClick,
              d = void 0 === c ? "play" : c,
              m = e.size,
              _ = void 0 === m ? id.NORMAL : m,
              E = e.classNames,
              g = e.onClick,
              p = e.onMouseEnter,
              b = e.onMouseLeave,
              f = e.onMouseDown,
              h = e.onMouseUp,
              A = e.onFocus,
              v = e.onBlur,
              D = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, ud);
            const F = (0, s.useState)(!1),
              B = F[0],
              w = F[1],
              S = (0, s.useState)(!1),
              P = S[0],
              y = S[1],
              R = (0, s.useState)(o),
              k = R[0],
              T = R[1],
              x = (0, s.useRef)(null),
              N = (0, s.useCallback)(() => {
                x.current && (x.current.focus(), T(!0));
              }, []),
              I = (0, s.useCallback)(
                (e) => {
                  k && null !== x.current && !x.current.contains(e.target) && T(!1);
                },
                [k],
              );
            ((0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", I),
                () => {
                  document.removeEventListener("mousedown", I);
                }
              ),
              [I],
            ),
              (0, s.useEffect)(() => {
                T(o);
              }, [o]));
            const L = (0, s.useCallback)(
                (e) => {
                  g && g(e);
                },
                [g],
              ),
              M = (0, s.useCallback)(
                (e) => {
                  (w(!0), f && f(e), d && W(d), o && N());
                },
                [o, f, N, d],
              ),
              O = (0, s.useCallback)(
                (e) => {
                  (w(!1), h && h(e));
                },
                [h],
              ),
              H = (0, s.useCallback)(
                (e) => {
                  (p && p(e), l && W(l), y(!0));
                },
                [p, l],
              ),
              $ = (0, s.useCallback)(
                (e) => {
                  (w(!1), y(!1), b && b(e));
                },
                [b],
              ),
              U = (0, s.useCallback)(
                (e) => {
                  (T(!0), A && A(e));
                },
                [A],
              ),
              z = (0, s.useCallback)(
                (e) => {
                  (T(!1), v && v(e));
                },
                [v],
              ),
              G = C()(
                sd.base,
                r && sd.base__visibleLabel,
                B && sd.base__mouseDown,
                P && sd.base__hovered,
                k && sd.base__focused,
                null == E ? void 0 : E.base,
              ),
              j = C()(sd.icon, sd[`icon__${_}`], null == E ? void 0 : E.icon),
              q = C()(sd.label, null == E ? void 0 : E.label);
            return u().createElement(
              "div",
              od(
                {
                  ref: x,
                  className: G,
                  onClick: L,
                  onMouseEnter: H,
                  onMouseLeave: $,
                  onMouseDown: M,
                  onMouseUp: O,
                  onFocus: U,
                  onBlur: z,
                },
                D,
              ),
              u().createElement("div", { className: j }),
              u().createElement("div", { className: q }, t),
            );
          }),
          cd = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          dd = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const md = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          _d = (e) =>
            md
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let a = dd.length - 1; a >= 0; a--)
                    for (; e >= dd[a];) ((t += cd[a]), (e -= dd[a]));
                  return t;
                })(e),
          Ed = "MainReward_base_32",
          gd = "MainReward_imageContainer_37",
          pd = "MainReward_highlightContainer_cf",
          bd = "MainReward_highlight_06",
          fd = "MainReward_preview_7a",
          hd = "MainReward_info_58",
          Ad = "MainReward_title_6d",
          vd = "MainReward_subTitle_e2",
          Cd = (0, q.Pi)(
            ({ index: e, rank: t, size: a, hasHighlight: r, onPreviewClick: n, className: s }) => {
              const o = gc().model.computes.mainReward(e);
              return u().createElement(
                "div",
                { className: C()(Ed, s) },
                u().createElement(
                  "div",
                  { className: gd },
                  r &&
                    u().createElement(
                      "div",
                      { className: pd },
                      u().createElement("div", { className: bd }),
                    ),
                  u().createElement(Mc, Xc({ reward: o, size: a, rank: t })),
                  ((e) => "styleProgress" === e.name)(o) &&
                    u().createElement(
                      "div",
                      { className: fd },
                      u().createElement(ld, {
                        label: R.strings.comp7.rewards.preview(),
                        onClick: n,
                      }),
                    ),
                ),
                u().createElement(
                  "div",
                  { className: hd },
                  u().createElement("div", { className: Ad }, o.label),
                  u().createElement(Wa, {
                    text: String(R.strings.comp7.rewards.subtitle.$dyn(o.name)),
                    binding: { vehicleLevel: _d(10) },
                    classMix: vd,
                  }),
                ),
              );
            },
          ),
          Dd = "RankRewardsItem_base_a7",
          Fd = "RankRewardsItem_mainRewardContainer_e0",
          Bd = "RankRewardsItem_rewardsContainer_69",
          wd = "RankRewardsItem_rewardsContainer__qualification_b0",
          Sd = "RankRewardsItem_statusContainer_bf",
          Pd = "RankRewardsItem_statusContainer__hidden_c8",
          yd = "RankRewardsItem_icon_7d",
          Rd = (0, q.Pi)(
            ({
              itemIndex: e,
              itemWidth: t,
              rankState: a,
              mainRewardSize: r,
              hasHighlight: n,
              visibleRewardsCount: s,
              rankEmblemSize: o,
              isQualification: i,
              onPreviewClick: l,
            }) => {
              const c = gc().model,
                d = c.computes.rankRewardsItem(e),
                m = d.rank,
                _ = d.from,
                E = d.to,
                g = d.hasRewardsReceived,
                p = c.computes.divisionsString(e),
                b = c.computes.elitePercent(e);
              return u().createElement(
                "div",
                { className: Dd, style: { "--itemWidth": `${t}rem` } },
                u().createElement(nd, {
                  rank: m,
                  from: _,
                  to: E,
                  divisions: p,
                  elitePercent: b,
                  rankEmblemSize: o,
                  rankState: a,
                }),
                u().createElement(Cd, {
                  index: e,
                  rank: m,
                  size: r,
                  hasHighlight: n,
                  onPreviewClick: l,
                  className: Fd,
                }),
                u().createElement(
                  "div",
                  { className: C()(Bd, i && wd) },
                  u().createElement(td, { itemIndex: e, visibleRewardsCount: s, rank: m }),
                ),
                u().createElement(
                  "div",
                  { className: C()(Sd, !g && Pd) },
                  u().createElement("div", { className: yd }),
                  R.strings.comp7.rewards.status.achieved(),
                ),
              );
            },
          ),
          kd = (e) => (e >= B.Large ? Ur.x110 : e >= B.Medium ? Ur.x64 : Ur.x48),
          Td = (e) =>
            e >= B.ExtraLarge
              ? fc.S600x450
              : e >= B.Large
                ? fc.S400x300
                : e >= B.Medium
                  ? fc.S296x222
                  : fc.S232x174,
          xd = (e) => (e >= w.Medium ? 5 : 4),
          Nd = "RankRewardsPage_base_fd",
          Id = "RankRewardsPage_content_3f",
          Ld = "RankRewardsPage_scrollContainer_f2",
          Md = "RankRewardsPage_areaContainer_9e",
          Od = "RankRewardsPage_areaWrapper_fb",
          Hd = "RankRewardsPage_bar_59",
          Wd = "RankRewardsPage_qualificationFooter_71",
          $d = "RankRewardsPage_shopButtonContainer_90",
          Ud = "RankRewardsPage_shopButton_4e",
          zd = "RankRewardsPage_comp7ShopButtonBackground_cc",
          Gd = "RankRewardsPage_shopButtonIcon_51",
          jd = { duration: 700, easing: (e) => Math.pow(e, 4) },
          qd = R.strings.comp7.rewards,
          Vd = (0, q.Pi)(() => {
            const e = P(),
              t = e.mediaSize,
              a = e.mediaWidth,
              r = gc(),
              n = r.model,
              o = r.controls,
              i = n.root.get(),
              l = i.currentItemIndex,
              c = i.initialItemIndex,
              d = n.qualification.isActive.get(),
              m = n.computes.rankRewardsItemsLength(),
              _ = n.computes.scrollingSettings(),
              E = _.nextNotAchievedItemIndex,
              g = _.hasForceScroll,
              p = (0, s.useState)(g ? "idle" : "initial"),
              b = p[0],
              f = p[1],
              h = (0, s.useState)(g ? c : E),
              A = h[0],
              v = h[1],
              C = ((e) =>
                e >= B.ExtraLarge
                  ? 600
                  : e >= B.Large
                    ? 460
                    : e >= B.Medium
                      ? 400
                      : e >= B.Small
                        ? 340
                        : 300)(t),
              D = m * C,
              F = So(C),
              w = F.scrollPosition,
              S = F.clampPosition,
              y = F.contentRef,
              k = (function () {
                const e = (0, s.useRef)(!1);
                return (
                  (0, s.useEffect)(
                    () => () => {
                      e.current = !0;
                    },
                    [],
                  ),
                  e
                );
              })();
            ((0, s.useLayoutEffect)(() => {
              "idle" === b
                ? w.start({ scrollPosition: viewEnv.remToPx(c * C), immediate: !0 })
                : "initial" === b && w.start({ scrollPosition: viewEnv.remToPx(D), immediate: !0 });
            }, []),
              (0, s.useEffect)(
                () =>
                  Re(() => {
                    const e = y.current;
                    if (e && "initial" === b) {
                      const t = S(e, viewEnv.remToPx(E * C - C)),
                        a = S(e, viewEnv.remToPx(D));
                      if (t === a) return void f("idle");
                      w.start({
                        scrollPosition: t,
                        from: { scrollPosition: a },
                        config: jd,
                        onStart: () => {
                          f("scrolling");
                        },
                        onRest: () => {
                          k.current || f("idle");
                        },
                      });
                    }
                  }),
                [S, y, k, C, E, b, D, w],
              ));
            const T = (e) => "idle" === b && e === E && !d,
              x = (0, ke.useSpring)(_e),
              N = { lineHeight: 1.5 },
              I = no(C) - C;
            return u().createElement(
              "div",
              { className: Nd },
              u().createElement(st, { className: K }, R.strings.comp7.page.heading.rankRewards()),
              u().createElement(It, null),
              u().createElement(
                ke.animated.div,
                { className: Id, style: x },
                u().createElement(
                  wo,
                  {
                    api: F,
                    stuckIndex: A,
                    itemWidth: C,
                    itemsOffset: I,
                    onStick: v,
                    className: Ld,
                    areaClassNames: { base: Md, wrapper: Od },
                    barClassNames: { base: Hd },
                  },
                  Rr(m, (e) =>
                    u().createElement(Rd, {
                      key: e,
                      itemIndex: e,
                      visibleRewardsCount: xd(a),
                      rankState: Ps(e, l, d),
                      rankEmblemSize: kd(t),
                      mainRewardSize: Td(t),
                      itemWidth: C,
                      hasHighlight: T(e),
                      isQualification: d,
                      onPreviewClick: () => o.goToPreview(e, A),
                    }),
                  ),
                ),
              ),
              !d &&
                u().createElement(
                  "div",
                  { className: $d },
                  u().createElement(
                    Wt,
                    { type: Mt.ghost, size: Ot.medium, mixClass: Ud, onClick: o.openComp7Shop },
                    u().createElement("div", { className: zd }),
                    u().createElement("div", { className: Gd }),
                    u().createElement(Pa, {
                      text: qd.shopButton(),
                      color: "WHITE",
                      variant: "paragraph-P14",
                      variant_md: "paragraph-P18",
                      style: { fontWeight: 700 },
                    }),
                  ),
                ),
              d &&
                u().createElement(
                  "div",
                  { className: Wd },
                  u().createElement(Pa, {
                    text: qd.qualification.condition.first(),
                    color: "WHITE_REAL",
                    variant: "paragraph-P14",
                    variant_md: "paragraph-P16",
                    style: N,
                  }),
                  u().createElement(Pa, {
                    text: qd.qualification.condition.second(),
                    color: "WHITE_REAL",
                    variant: "paragraph-P14",
                    variant_md: "paragraph-P16",
                    style: N,
                  }),
                ),
            );
          }),
          Xd = { context: "model.rankRewardsModel" };
        let Qd;
        !(function (e) {
          ((e.LockedByNoXVehicles = "lockedByNoXVehicles"),
            (e.LockedByInactiveSeason = "lockedByInactiveSeason"),
            (e.LockedByPreviousQuest = "lockedByPreviousQuest"),
            (e.Active = "active"),
            (e.Completed = "completed"));
        })(Qd || (Qd = {}));
        const Yd = [Qd.LockedByNoXVehicles, Qd.LockedByInactiveSeason, Qd.LockedByPreviousQuest];
        let Kd;
        !(function (e) {
          ((e[(e.Scrolling = 0)] = "Scrolling"),
            (e[(e.ProgressChange = 1)] = "ProgressChange"),
            (e[(e.HighlightCard = 2)] = "HighlightCard"),
            (e[(e.ChangeCompleted = 3)] = "ChangeCompleted"),
            (e[(e.ProgressFinished = 4)] = "ProgressFinished"),
            (e[(e.ProgressAlreadyFinished = 5)] = "ProgressAlreadyFinished"));
        })(Kd || (Kd = {}));
        const Zd = 2140,
          Jd = 1500,
          em = 1264,
          tm = 1104,
          am = 804,
          rm = 187,
          nm = 158,
          sm = oe()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {
                    root: e.object(),
                    questCards: e.array("questCards"),
                    progressPoints: e.array("progressPoints"),
                  },
                  e.primitives(["currentTokenValue", "previousTokenValue"]),
                  { progressAnimationState: re.LO.box(Kd.HighlightCard) },
                ),
                a = (0, Ee.Om)(
                  (e) => {
                    const a = fe(t.questCards.get(), e);
                    if (!a) throw new Error(`Unexpected card index: ${e}`);
                    return Object.assign({}, a);
                  },
                  { equals: ae },
                ),
                r = (0, Ee.Om)(
                  (e, t) => {
                    const r = a(e).rewards;
                    return Qc({ rewards: r, size: t });
                  },
                  { equals: ae },
                ),
                n = (0, Ee.Om)(() =>
                  (function (e, t) {
                    if (Array.isArray(e)) return e.every(t);
                    for (let a = 0; a < e.length; a++) if (!t(he(e, a), a, e)) return !1;
                    return !0;
                  })(t.questCards.get(), (e) => e.state === Qd.Completed),
                ),
                s = (0, Ee.Om)((e) => Yd.includes(a(e).state)),
                u = (0, Ee.Om)(() => t.questCards.get().length),
                o = (0, Ee.Om)(() => 5 >= u(), { equals: ae }),
                i = (0, Ee.Om)(() => (n() ? Qd.Completed : Qd.Active), { equals: ae }),
                l = (0, Ee.Om)(() => t.currentTokenValue.get(), { equals: ae }),
                c = (0, Ee.Om)(() => t.previousTokenValue.get(), { equals: ae }),
                d = (0, Ee.Om)(
                  (e) => ({
                    wasProgressionVisited: c() === l(),
                    isRecentlyCompletedLevel: c() <= e && e <= l(),
                    isPrevLevel: e <= c(),
                  }),
                  { equals: ae },
                ),
                m = (0, Ee.Om)(
                  () => {
                    const e = t.currentTokenValue.get(),
                      a = t.progressPoints.get();
                    return ve(a, ({ rewards: t }, r) => ({
                      level: r + 1,
                      isCompleted: r < e,
                      isActive: r === e,
                      isLast: r === a.length - 1,
                      rewards: t,
                    }));
                  },
                  { equals: ae },
                ),
                _ = (0, Ee.Om)(
                  () => {
                    const e = 1 * t.progressPoints.get().length;
                    return t.currentTokenValue.get() >= e;
                  },
                  { equals: ae },
                ),
                E = (0, Ee.Om)(
                  () => _() && t.currentTokenValue.get() === t.previousTokenValue.get(),
                  { equals: ae },
                ),
                g = (0, Ee.Om)(
                  () => {
                    var e;
                    const a = t.progressPoints.get(),
                      r = fe(a, a.length - 1),
                      n = null != (e = null == r ? void 0 : r.count) ? e : 0;
                    return t.currentTokenValue.get() >= n;
                  },
                  { equals: ae },
                ),
                p = (0, Ee.Om)(
                  () => {
                    var e;
                    return null != (e = Fe(t.questCards.get(), (e) => e.state === Qd.Active))
                      ? e
                      : 0;
                  },
                  { equals: ae },
                ),
                b = (0, Ee.Om)(
                  (e, t, a, r) => {
                    if (t && t.length) {
                      const n = t.length * a + (t.length - 1) * r,
                        s = (e, t) => (e >= t ? t : e);
                      switch (!0) {
                        case e >= B.ExtraLarge:
                          return s(n, Zd);
                        case e >= B.Large:
                          return s(n, Jd);
                        case e >= B.Medium:
                          return s(n, em);
                        case e >= B.Small:
                          return s(n, tm);
                        default:
                          return s(n, am);
                      }
                    }
                    return 0;
                  },
                  { equals: ae },
                );
              return Object.assign({}, t, {
                computes: {
                  questCardsLength: u,
                  questCard: a,
                  questCards: t.questCards,
                  questRewards: r,
                  isQuestLocked: s,
                  areDefaultNumberQuests: o,
                  battleTasksStatus: i,
                  isAllQuestsCompleted: n,
                  levels: m,
                  currentLevel: l,
                  levelStatus: d,
                  isProgressionCompleted: _,
                  wasProgressionCompletedBeforeStart: E,
                  initialItemScrollIndex: p,
                  getScrollContainerMaxWidth: b,
                  isDoneProgression: g,
                },
              });
            },
            ({ externalModel: e, model: t }) => {
              const a = (function (e) {
                const t = {};
                for (const a in e)
                  if (Object.prototype.hasOwnProperty.call(e, a)) {
                    const r = e[a];
                    t[a] = (0, re.aD)(r);
                  }
                return t;
              })({
                finishScrolling: () => t.progressAnimationState.set(Kd.ProgressChange),
                finishProgressionChange: () => t.progressAnimationState.set(Kd.HighlightCard),
                finishHighlightCard: () => t.progressAnimationState.set(Kd.ChangeCompleted),
                completeProgression: () => t.progressAnimationState.set(Kd.ProgressFinished),
              });
              return Object.assign({}, a, {
                animationStart: e.createCallbackNoArgs("onAnimationStart"),
                animationEnd: e.createCallbackNoArgs("onAnimationEnd"),
              });
            },
          ),
          um = sm[0],
          om = sm[1],
          im = {
            base: "Prompt_base_74",
            defaultText: "Prompt_defaultText_05",
            defaultText__done: "Prompt_defaultText__done_b0",
          },
          lm = R.strings.comp7.weeklyQuests.tokenProgress.description,
          cm = (0, q.Pi)(({ className: e }) => {
            const t = om().model.computes.isDoneProgression();
            return u().createElement(
              "div",
              { className: C()(im.base, t && im.base__done, e) },
              t
                ? u().createElement(Pa, {
                    text: lm.done(),
                    variant: "paragraph-P14",
                    className: im.defaultText__done,
                  })
                : u().createElement(Pa, {
                    text: lm.normal(),
                    variant: "paragraph-P14",
                    className: im.defaultText,
                  }),
            );
          }),
          dm = { Vertical: r, Horizontal: n };
        "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        ("undefined" != typeof document && document.documentElement.style,
          "undefined" != typeof window &&
            ("ontouchstart" in window ||
              (window.DocumentTouch && (document, window.DocumentTouch))),
          "undefined" != typeof navigator && navigator.msMaxTouchPoints,
          "undefined" != typeof navigator && /Chrome/i.test(navigator && navigator.userAgent));
        const mm = {
            base: "LevelCard_base_cd",
            bgCompleted: "LevelCard_bgCompleted_e8",
            bgCompleted__completed: "LevelCard_bgCompleted__completed_53",
            bgCompleted__fast: "LevelCard_bgCompleted__fast_2a",
            completedIconContainer: "LevelCard_completedIconContainer_28",
            completedIconContainer__completed: "LevelCard_completedIconContainer__completed_47",
            completedIconContainer__prevLevel: "LevelCard_completedIconContainer__prevLevel_05",
            completedIcon: "LevelCard_completedIcon_40",
            completedIconGlow: "LevelCard_completedIconGlow_27",
            border: "LevelCard_border_b4",
            border__right: "LevelCard_border__right_c1",
          },
          _m = "LevelLabel_base_10",
          Em = "LevelLabel_activeGlow_6d",
          gm = "LevelLabel_activeGlow__completed_b9",
          pm = "LevelLabel_level_4c",
          bm = "LevelLabel_level__completed_c4",
          fm = "LevelLabel_level__active_85",
          hm = "LevelLabel_tokenIcon_67",
          Am = "LevelLabel_tokenIcon__active_7a",
          vm = "LevelLabel_levelCurrent_ce",
          Cm = "LevelLabel_levelCurrent__completed_97",
          Dm = R.strings.tooltips.awardItem.comp7TokenWeeklyReward,
          Fm = ({ level: e, isActive: t, isCompleted: a }) => {
            const r = C()(pm, a && bm, t && fm);
            return u().createElement(
              qe,
              { header: Dm.header(), body: Dm.body() },
              u().createElement(
                "div",
                { className: _m },
                u().createElement("div", { className: C()(Em, t && gm) }),
                t && u().createElement("div", { className: C()(vm, t && Cm) }, e),
                !t && u().createElement("div", { className: r }, e),
                u().createElement("div", { className: C()(hm, { [Am]: t }) }),
              ),
            );
          },
          Bm = "prevLevel",
          wm = "completed",
          Sm = "inProgress",
          Pm = (e, t, a) => (e ? wm : t ? Sm : a),
          ym = (0, q.Pi)(({ level: e, isActive: t, isCompleted: a, isLast: r }) => {
            const n = (0, s.useState)(),
              o = n[0],
              i = n[1],
              l = om().model,
              c = (0, s.useRef)(null),
              d = l.computes.levelStatus(e),
              m = d.wasProgressionVisited,
              _ = d.isRecentlyCompletedLevel,
              E = d.isPrevLevel;
            (0, s.useEffect)(() => {
              a && !m && _ && i(Bm);
            }, [a, m, _]);
            const g = (0, s.useCallback)(() => {
              W("pr_progress_tick");
            }, []);
            return (
              (0, s.useEffect)(() => {
                const e = c.current;
                return Re(() => {
                  if (e)
                    return (
                      e.addEventListener("transitionstart", g),
                      () => {
                        e.removeEventListener("transitionstart", g);
                      }
                    );
                });
              }, [c, g]),
              u().createElement(
                "div",
                { className: mm.base },
                u().createElement("div", {
                  className: C()(mm.bgCompleted, (t || a) && mm.bgCompleted__completed),
                  ref: c,
                }),
                u().createElement(
                  "div",
                  {
                    className: C()(
                      mm.completedIconContainer,
                      mm[`completedIconContainer__${Pm(E, !a, o)}`],
                    ),
                  },
                  u().createElement("div", { className: mm.completedIconGlow }),
                  u().createElement("div", { className: mm.completedIcon }),
                ),
                u().createElement(Fm, { level: e, isCompleted: a, isActive: t }),
                u().createElement("div", { className: mm.border }),
                r && u().createElement("div", { className: C()(mm.border, mm.border__right) }),
              )
            );
          }),
          Rm = "LevelCards_base_b9";
        function km() {
          return (
            (km =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            km.apply(this, arguments)
          );
        }
        const Tm = (0, q.Pi)(
            ({ levelRef: e }) => {
              const t = om().model.computes.levels();
              return u().createElement(
                "div",
                { className: Rm, ref: e },
                t.map((e) => u().createElement(ym, km({ key: e.level }, e))),
              );
            },
            { forwardRef: !0 },
          ),
          xm = {
            base: "RewardCard_base_1f",
            base__mediaLarge: "RewardCard_base__mediaLarge_1a",
            base__mediaExtraExtraLarge: "RewardCard_base__mediaExtraExtraLarge_c5",
            activeBlock: "RewardCard_activeBlock_0f",
            activeBlock__completed: "RewardCard_activeBlock__completed_7c",
            activeBlock__fast: "RewardCard_activeBlock__fast_1a",
            bgCompleted: "RewardCard_bgCompleted_3c",
            bgCompleted__completed: "RewardCard_bgCompleted__completed_c9",
            bgCompleted__fast: "RewardCard_bgCompleted__fast_93",
            border: "RewardCard_border_ab",
            border__right: "RewardCard_border__right_55",
          },
          Nm = "Rewards_base_76",
          Im = "Rewards_base__completed_f5",
          Lm = "Rewards_base__wide_f7",
          Mm = "Rewards_reward_24";
        function Om() {
          return (
            (Om =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Om.apply(this, arguments)
          );
        }
        const Hm = ({ isCompleted: e, isActive: t, rewards: a, fixedSize: r }) => {
            const n = P(),
              s = null != r ? r : n.mediaSize <= B.Medium ? fc.Small : fc.Big,
              o = (e) => Qc({ rewards: e, size: s }),
              i = C()(Nm, s === fc.Small && o(a).length > 2 && Lm, e && !t && Im);
            return u().createElement(
              "div",
              { className: i },
              ve(o(a), (e) => u().createElement(Mc, Om({ className: Mm, key: e.name }, e))),
            );
          },
          Wm = ({ isCompleted: e, isActive: t, isLast: a, rewards: r }) => {
            const n = P(),
              s = C()(
                xm.base,
                n.mediaSize === B.Medium && xm.base__mediaMedium,
                n.mediaSize === B.Large && xm.base__mediaLarge,
                n.remScreenHeight >= 1200 && xm.base__mediaExtraExtraLarge,
              ),
              o = C()(xm.activeBlock, t && xm.activeBlock__completed),
              i = C()(xm.bgCompleted, (t || e) && xm.bgCompleted__completed);
            return u().createElement(
              "div",
              { className: s },
              u().createElement("div", { className: o }),
              u().createElement("div", { className: i }),
              u().createElement(Hm, { rewards: r, isActive: t, isCompleted: e }),
              u().createElement("div", { className: xm.border }),
              a && u().createElement("div", { className: C()(xm.border, xm.border__right) }),
            );
          },
          $m = "RewardCards_base_07",
          Um = (0, q.Pi)(() => {
            const e = om().model.computes.levels();
            return u().createElement(
              "div",
              { className: $m },
              e.map(({ isCompleted: e, isActive: t, isLast: a, rewards: r }, n) =>
                u().createElement(Wm, {
                  key: n,
                  isCompleted: e,
                  isActive: t,
                  isLast: a,
                  rewards: r,
                }),
              ),
            );
          }),
          zm = "OptimizedProgressBar_base_1f",
          Gm = "OptimizedProgressBar_wrapper_ab",
          jm = "OptimizedProgressBar_background_ce",
          qm = ["api", "value", "maxValue", "theme"];
        function Vm() {
          return (
            (Vm =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            Vm.apply(this, arguments)
          );
        }
        const Xm = (e, t) => ("number" == typeof t ? t : e.offsetLeft),
          Qm = (e) => {
            let t = e.api,
              a = e.value,
              r = e.maxValue,
              n = void 0 === r ? 100 : r,
              o = e.theme,
              i = void 0 === o ? pi : o,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((a = s[r]), t.indexOf(a) >= 0 || (n[a] = e[a]));
                return n;
              })(e, qm);
            const c = (0, s.useRef)(null),
              d = (0, s.useRef)(null),
              m = (0, s.useRef)(null),
              _ = Qa(0, a, n) / n,
              E = (0, s.useCallback)(
                (e) => {
                  (m.current &&
                    c.current &&
                    (({ horizontalScrollPosition: e, leftOffset: t }, a, r) => {
                      const n = a.offsetWidth - r.offsetWidth,
                        s = e - Xm(a, t),
                        u = Qa(0, n, s);
                      r.style.left = `${u}px`;
                    })(e, c.current, m.current),
                    d.current &&
                      c.current &&
                      ((
                        { horizontalScrollPosition: e, leftOffset: t },
                        a,
                        { container: r, line: n },
                      ) => {
                        const s = Math.max(0, Math.floor(r.offsetWidth * a) - 8e3),
                          u = e - Xm(r, t),
                          o = Qa(0, s, u);
                        n.style.left = `${o}px`;
                      })(e, _, { line: d.current, container: c.current }));
                },
                [_],
              ),
              g = (0, s.useMemo)(() => Ei(i), [i]);
            return (
              (t.current.update = E),
              u().createElement(
                "div",
                { className: zm, ref: c },
                u().createElement(
                  "div",
                  { className: Gm },
                  u().createElement(
                    "div",
                    { style: g, className: C()(jm, l.progressBarBackgroundClassMix), ref: m },
                    u().createElement(Wo, {
                      size: l.size,
                      classMix: l.progressBarBackgroundClassMix,
                    }),
                  ),
                  u().createElement(
                    fi,
                    Vm({}, l, {
                      lineRef: d,
                      value: a,
                      theme: i,
                      maxValue: n,
                      withoutBackground: !0,
                    }),
                  ),
                ),
              )
            );
          },
          Ym = (e, t, a) =>
            C()(
              e[a],
              t === Kd.ProgressAlreadyFinished
                ? e[`${a}__fast`]
                : t >= Kd.ProgressFinished
                  ? e[`${a}__completed`]
                  : void 0,
            ),
          Km = {
            base: "Container_base_31",
            progressWrapper: "Container_progressWrapper_e1",
            progressWrapper__completed: "Container_progressWrapper__completed_9e",
            progressWrapper__fast: "Container_progressWrapper__fast_af",
            bg: "Container_bg_d7",
          },
          Zm = (0, q.Pi)(({ api: e, theme: t }) => {
            const a = om(),
              r = a.model,
              n = a.controls,
              o = r.progressAnimationState.get(),
              i = r.computes,
              l = r.previousTokenValue.get(),
              c = r.currentTokenValue.get(),
              d = (0, s.useRef)({ update: () => {} });
            e.current.moveProgressBars = (0, s.useCallback)((e) => {
              d.current.update(e);
            }, []);
            const m = (0, s.useState)({
                maxPoints: 1 * i.levels().length,
                previousEarnedPoints: l,
                progressionSize: l,
              }),
              _ = m[0],
              E = _.previousEarnedPoints,
              g = _.maxPoints,
              p = _.progressionSize,
              b = m[1];
            (0, s.useEffect)(() => {
              (b((e) => {
                const t = 0 === e.progressionSize ? l : e.progressionSize;
                return {
                  maxPoints: 1 * i.levels().length,
                  previousEarnedPoints: t,
                  progressionSize: c,
                };
              }),
                l !== c && W("pr_progress_bar"));
            }, [l, c, i]);
            const f = (0, s.useMemo)(
              () =>
                Object.assign({}, bi, {
                  withStack: !0,
                  type: Ho.Growing,
                  delta: { duration: 400, delay: 300 },
                  line: { duration: 400, delay: 300 },
                }),
              [],
            );
            return (
              (0, s.useEffect)(() => {
                if (o === Kd.ProgressChange)
                  return ut(() => {
                    n.finishProgressionChange();
                  }, 700);
              }, [n, o]),
              u().createElement(
                "div",
                { className: Km.base },
                u().createElement("div", { className: Km.bg }),
                u().createElement(
                  "div",
                  { className: Ym(Km, o, "progressWrapper") },
                  u().createElement(Qm, {
                    animationSettings: f,
                    deltaFrom: E,
                    value: p,
                    maxValue: g,
                    api: d,
                    theme: t,
                  }),
                ),
              )
            );
          }),
          Jm = {
            base: "Content_base_d5",
            base__centered: "Content_base__centered_e6",
            base__layoutReady: "Content_base__layoutReady_84",
            horizontalContent: "Content_horizontalContent_91",
            wrapper: "Content_wrapper_d8",
            progress: "Content_progress_35",
            progressArea: "Content_progressArea_68",
          },
          e_ = "ScrollDrag_base_bd",
          t_ = "ScrollDrag_base__grabbing_1f",
          a_ = ({ api: e, children: t, updateProgressBarPosition: a }) => {
            const r = (0, s.useState)(0),
              n = r[0],
              o = r[1],
              i = (0, s.useState)(0),
              l = i[0],
              c = i[1],
              d = (0, s.useState)(!1),
              m = d[0],
              _ = d[1];
            (0, s.useEffect)(
              () =>
                Re(() => {
                  const t = (e) => {
                    const t = e.value.scrollPosition;
                    m || o(-t);
                  };
                  return (
                    e.events.on("change", t),
                    () => {
                      e.events.off("change", t);
                    }
                  );
                }),
              [e, m],
            );
            const E = (0, s.useCallback)(
                (e) => {
                  (_(!0), c(e.clientX), a());
                },
                [a],
              ),
              g = (0, s.useCallback)(() => {
                (_(!1), c(0), a());
              }, [a]),
              p = (0, s.useCallback)(
                (t) => {
                  if (m) {
                    const r = Qa(-(e.getBounds()[1] || 0), 0, n + t.clientX - l);
                    (e.applyScroll(-r, !0), c(t.clientX), o(r), a());
                  }
                },
                [m, e, n, l, a],
              );
            return u().createElement(
              "div",
              {
                className: C()(e_, m && t_),
                onMouseDown: E,
                onMouseUp: g,
                onMouseMove: p,
                onMouseLeave: g,
              },
              t,
            );
          };
        function r_(e, t, a, r, n, s, u) {
          try {
            var o = e[s](u),
              i = o.value;
          } catch (e) {
            return void a(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(r, n);
        }
        const n_ = (0, q.Pi)(() => {
            const e = om().model,
              t = so(),
              a = e.computes,
              r = a.levels,
              n = a.getScrollContainerMaxWidth,
              o = a.currentLevel,
              i = P(),
              l = (0, s.useState)(!1),
              c = l[0],
              d = l[1],
              m = (0, s.useState)(!1),
              _ = m[0],
              E = m[1],
              g = r().length,
              p = e.currentTokenValue.get(),
              b = n(i.mediaSize, e.computes.levels(), i.mediaSize >= B.Large ? rm : nm, 0),
              f = (0, s.useRef)({ moveProgressBars: te }),
              h = (0, s.useRef)(null),
              A = (0, s.useRef)(null),
              v = t.animationScroll.scrollPosition,
              D = t.getWrapperSize,
              F = t.contentRef,
              w = t.wrapperRef,
              S = t.getContainerSize,
              y = t.applyScroll;
            (0, s.useLayoutEffect)(
              () =>
                Re(() => {
                  const e = w.current,
                    t = A.current;
                  if (!e || !t) return;
                  const a = parseFloat(getComputedStyle(t.children[0]).width),
                    r = parseFloat(getComputedStyle(t).paddingRight),
                    n = parseFloat(getComputedStyle(e).paddingLeft);
                  (d(i.remScreenWidth >= g * a + r + n), E(!0));
                }),
              [i.remScreenWidth, w, g],
            );
            const R = (0, s.useCallback)(
                (e) => {
                  if (h.current) {
                    const t = D();
                    f.current.moveProgressBars({
                      viewPort: h.current,
                      horizontalScrollPosition: t ? e - t : e,
                    });
                  }
                },
                [D],
              ),
              k = () => {
                R(v.goal);
              },
              T = (0, s.useCallback)(() => {
                const e = F.current,
                  t = r().length;
                if (e && t > 0) {
                  const a = S() || 0,
                    r = D() || 0,
                    n = a / t,
                    s = o() * n,
                    u = (r - e.offsetLeft - n) / 2;
                  y(Qa(0, a - r, s - u));
                }
                0 === v.goal && R(v.goal);
              }, [y, o, r, F, S, D, v.goal, R]);
            return (
              (0, s.useEffect)(() => {
                T();
              }, [p, T]),
              (0, s.useEffect)(() => {
                const e = (function () {
                  var e,
                    t =
                      ((e = function* () {
                        const e = S(),
                          t = v.goal;
                        (yield (0, X.Eu)(),
                          yield new Promise((e) => {
                            requestAnimationFrame(() => {
                              requestAnimationFrame(() => {
                                e();
                              });
                            });
                          }));
                        const a = S();
                        (R(a && e && a !== e ? (t * a) / e : t), T());
                      }),
                      function () {
                        var t = this,
                          a = arguments;
                        return new Promise(function (r, n) {
                          var s = e.apply(t, a);
                          function u(e) {
                            r_(s, r, n, u, o, "next", e);
                          }
                          function o(e) {
                            r_(s, r, n, u, o, "throw", e);
                          }
                          u(void 0);
                        });
                      });
                  return function () {
                    return t.apply(this, arguments);
                  };
                })();
                return (
                  engine.on("clientResized", e),
                  () => {
                    engine.off("clientResized", e);
                  }
                );
              }, []),
              (0, s.useEffect)(() => ut(() => R(v.goal), 0), [p, v.goal, R]),
              u().createElement(
                "div",
                {
                  className: C()(Jm.base, c && Jm.base__centered, _ && Jm.base__layoutReady),
                  ref: h,
                  onWheel: () => R(v.goal),
                  style: { maxWidth: `${b}rem` },
                },
                u().createElement(
                  dm.Horizontal.Area.Default,
                  {
                    api: t,
                    className: Jm.horizontalContent,
                    classNames: { wrapper: Jm.wrapper },
                    barClassNames: { base: Jm.bar },
                    onDrag: k,
                  },
                  u().createElement(
                    a_,
                    { api: t, updateProgressBarPosition: k },
                    u().createElement(Tm, { levelRef: A }),
                    u().createElement(
                      "div",
                      { className: Jm.progress },
                      u().createElement(
                        "div",
                        { className: Jm.progressArea },
                        u().createElement(Zm, { api: f }),
                      ),
                    ),
                    u().createElement(Um, null),
                  ),
                ),
              )
            );
          }),
          s_ = {
            base: "Progression_base_d2",
            contentWrapper: "Progression_contentWrapper_6f",
            progressionContentWrapper: "Progression_progressionContentWrapper_59",
            progressionContentWrapper__completed:
              "Progression_progressionContentWrapper__completed_a7",
            progressionContentWrapper__fast: "Progression_progressionContentWrapper__fast_58",
            prompt: "Progression_prompt_7b",
            "add-blur": "Progression_add-blur_31",
            hide: "Progression_hide_32",
            show: "Progression_show_89",
          },
          u_ = (0, q.Pi)(({ className: e }) => {
            const t = om(),
              a = t.model,
              r = t.controls,
              n = a.progressAnimationState.get(),
              o = a.computes.isProgressionCompleted(),
              i = a.computes.wasProgressionCompletedBeforeStart();
            return (
              (0, s.useEffect)(
                () =>
                  i || (n === Kd.ChangeCompleted && o)
                    ? ut(() => {
                        r.completeProgression();
                      }, 500)
                    : n === Kd.HighlightCard
                      ? ut(() => {
                          r.finishHighlightCard();
                        }, 500)
                      : void 0,
                [n, i, o, r],
              ),
              u().createElement(
                "div",
                { className: C()(s_.base, e) },
                u().createElement(
                  "div",
                  { className: s_.contentWrapper },
                  u().createElement(
                    "div",
                    { className: Ym(s_, n, "progressionContentWrapper") },
                    u().createElement(n_, null),
                  ),
                  u().createElement(cm, { className: s_.prompt }),
                ),
              )
            );
          });
        let o_, i_, l_;
        (!(function (e) {
          ((e.NotStarted = "notStarted"),
            (e.Active = "active"),
            (e.LastWeek = "lastWeek"),
            (e.Finished = "finished"));
        })(o_ || (o_ = {})),
          (function (e) {
            ((e.Timer = "timer"),
              (e.Countdown = "countdown"),
              (e.Cooldown = "cooldown"),
              (e.None = "none"));
          })(i_ || (i_ = {})),
          (function (e) {
            ((e.Description = "description"),
              (e.Short = "short"),
              (e.Long = "long"),
              (e.Extended = "extended"));
          })(l_ || (l_ = {})));
        const c_ = () => {},
          d_ = (e = 0, t, a = 0, r = c_) => {
            const n = (0, s.useState)(e),
              u = n[0],
              o = n[1];
            return (
              (0, s.useEffect)(() => {
                if (e > 0) {
                  o(e);
                  const n = Date.now(),
                    s = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - n) / 1e3);
                        null !== a && t <= a ? (o(a), r && r(), clearInterval(s)) : o(t);
                      },
                      1e3 * (t || (e > 120 ? bt : 1)),
                    );
                  return () => {
                    clearInterval(s);
                  };
                }
                o(0);
              }, [e, t, a, r]),
              u
            );
          };
        X.Sw.instance;
        let m_;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(m_ || (m_ = {}));
        X.Sw.instance;
        const __ = d_,
          E_ = "Countdown_base_fe",
          g_ = "Countdown_icon_8b",
          p_ = "Countdown_description_8d",
          b_ = (e) => e.toString().padStart(2, "0"),
          f_ = (e, t) => {
            switch (t) {
              case l_.Description:
                return ((e, t = !0) =>
                  e.days > 7 && t
                    ? it(R.strings.common.duration.days(), { days: e.days })
                    : e.days >= 1
                      ? 0 === e.hours
                        ? it(R.strings.common.duration.days(), { days: e.days })
                        : `${it(R.strings.common.duration.days(), { days: e.days })} ${it(R.strings.common.duration.hours(), { hours: e.hours })}`
                      : e.hours >= 1
                        ? 0 === e.minutes
                          ? it(R.strings.common.duration.hours(), { hours: e.hours })
                          : `${it(R.strings.common.duration.hours(), { hours: e.hours })} ${it(R.strings.common.duration.minutes(), { minutes: e.minutes })}`
                        : it(R.strings.common.duration.minutes(), { minutes: e.minutes || 1 }))(e);
              case l_.Short:
                return `${b_(e.minutes)}:${b_(e.seconds)}`;
              case l_.Long:
                return `${b_(e.hours)}:${b_(e.minutes)}:${b_(e.seconds)}`;
              case l_.Extended:
                return `${it(R.strings.common.duration.days(), { days: e.days })} | ${b_(e.hours)}:${b_(e.minutes)}:${b_(e.seconds)}`;
            }
          },
          h_ = R.images.gui.maps.icons.components.countdown,
          A_ = (e, t) => {
            const a = 2 === t ? h_.big : h_;
            switch (e) {
              case i_.Timer:
                return a.clock();
              case i_.Countdown:
                return a.hourglass();
              case i_.Cooldown:
                return a.lock();
            }
          },
          v_ = (0, s.memo)(
            ({
              duration: e,
              icon: t = i_.Timer,
              style: a = l_.Description,
              onTimeReached: r,
              className: n = "",
              classNames: s = {},
              labelFormat: o = "",
            }) => {
              const i = a !== l_.Description ? 1 : void 0,
                l = __(e, i),
                c = ao();
              r && r[l] && r[l]();
              const d = f_(
                (function (e = 0) {
                  let t = e;
                  const a = Math.trunc(t / ht);
                  t -= a * ht;
                  const r = Math.trunc(t / ft);
                  t -= r * ft;
                  const n = Math.trunc(t / bt);
                  return ((t -= n * bt), { days: a, hours: r, minutes: n, seconds: t });
                })(l),
                a,
              );
              return u().createElement(
                "div",
                { className: C()(E_, n) },
                t !== i_.None &&
                  u().createElement("div", {
                    className: C()(g_, s.icon),
                    style: { backgroundImage: `url('${A_(t, c)}')` },
                  }),
                o
                  ? u().createElement(
                      "div",
                      { className: C()(p_, s.text) },
                      u().createElement(Ct, { text: o, binding: { timerText: d } }),
                    )
                  : u().createElement("div", { className: C()(p_, s.text) }, d),
              );
            },
          ),
          C_ = {
            base: "Separator_base_81",
            separator: "Separator_separator_9e",
            base__completedBattleQuests: "Separator_base__completedBattleQuests_ef",
            separator__left: "Separator_separator__left_74",
            base__inProgressBattleQuests: "Separator_base__inProgressBattleQuests_4d",
            base__condition: "Separator_base__condition_d9",
            base__awards: "Separator_base__awards_d6",
            base__lockedByNoXVehicles: "Separator_base__lockedByNoXVehicles_00",
            base__lockedByInactiveSeason: "Separator_base__lockedByInactiveSeason_66",
            base__lockedByPreviousQuest: "Separator_base__lockedByPreviousQuest_75",
            base__completed: "Separator_base__completed_5f",
            show: "Separator_show_ca",
            separator__right: "Separator_separator__right_3d",
            ellipse: "Separator_ellipse_c0",
            firstLayer: "Separator_firstLayer_34",
            secondLayer: "Separator_secondLayer_54",
            "add-blur": "Separator_add-blur_ba",
            hide: "Separator_hide_0e",
          };
        let D_;
        !(function (e) {
          ((e.Awards = "awards"),
            (e.Condition = "condition"),
            (e.CompletedBattleQuests = "completedBattleQuests"),
            (e.InProgressBattleQuests = "inProgressBattleQuests"));
        })(D_ || (D_ = {}));
        const F_ = ({ children: e, statusAnimation: t, type: a }) =>
            u().createElement(
              "div",
              { className: C()(C_.base, C_[`base__${a}`], C_[`base__${t}`]) },
              u().createElement(
                "div",
                { className: C()(C_.separator, C_.separator__left) },
                u().createElement(
                  "div",
                  { className: C_.ellipse },
                  u().createElement(
                    "div",
                    { className: C_.firstLayer },
                    u().createElement("div", { className: C_.secondLayer }),
                  ),
                ),
              ),
              e,
              u().createElement(
                "div",
                { className: C()(C_.separator, C_.separator__right) },
                u().createElement(
                  "div",
                  { className: C_.ellipse },
                  u().createElement(
                    "div",
                    { className: C_.firstLayer },
                    u().createElement("div", { className: C_.secondLayer }),
                  ),
                ),
              ),
            ),
          B_ = {
            base: "Timer_base_ad",
            timer: "Timer_timer_4c",
            block: "Timer_block_de",
            base__small: "Timer_base__small_5a",
            base__big: "Timer_base__big_03",
            text: "Timer_text_35",
            bgCountdown: "Timer_bgCountdown_86",
            description: "Timer_description_bc",
            countdown: "Timer_countdown_e1",
            "add-blur": "Timer_add-blur_c0",
            hide: "Timer_hide_7d",
            show: "Timer_show_1b",
          };
        let w_;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(w_ || (w_ = {}));
        const S_ = ({ size: e, currentTimerDate: t, text: a, onlyText: r = !1 }) => {
            const n = e === w_.Big;
            return u().createElement(
              "div",
              { className: C()(B_.base, B_[`base__${e}`]) },
              u().createElement(
                "div",
                { className: B_.timer },
                u().createElement(
                  F_,
                  { type: n ? D_.CompletedBattleQuests : D_.InProgressBattleQuests },
                  u().createElement(
                    "div",
                    { className: B_.block },
                    a && u().createElement("div", { className: B_.text }, a),
                    !r &&
                      t &&
                      u().createElement(
                        "div",
                        { className: B_.countdown },
                        u().createElement("div", { className: B_.bgCountdown }),
                        u().createElement(v_, {
                          duration: t,
                          style: l_.Description,
                          classNames: { text: B_.description },
                          className: B_.countdown,
                        }),
                      ),
                  ),
                ),
              ),
            );
          },
          P_ = "ResetStatus_base_25",
          y_ = "ResetStatus_base__ended_5e",
          R_ = "ResetStatus_endedTextTitle_20",
          k_ = "ResetStatus_endedTextSubtitle_6e",
          T_ = R.strings.comp7.weeklyQuests.resetStatus,
          x_ = (0, q.Pi)(({ className: e }) => {
            const t = om().model,
              a = t.root.get(),
              r = a.seasonState,
              n = a.resetTimeLeft,
              s = t.computes.isAllQuestsCompleted;
            return s() && r === o_.LastWeek
              ? u().createElement(
                  "div",
                  { className: C()(P_, y_, e) },
                  u().createElement(Ct, { text: T_.ended.lastWeek.title(), classMix: R_ }),
                )
              : s()
                ? u().createElement(
                    "div",
                    { className: C()(P_, y_, e) },
                    u().createElement(Ct, { text: T_.ended.title(), classMix: R_ }),
                    u().createElement(Ct, { text: T_.ended.subtitle(), classMix: k_ }),
                    u().createElement(S_, {
                      size: w_.Big,
                      currentTimerDate: n,
                      text: T_.ended.title(),
                    }),
                  )
                : r === o_.LastWeek
                  ? u().createElement(
                      "div",
                      { className: C()(P_, e) },
                      u().createElement(S_, {
                        size: w_.Small,
                        currentTimerDate: n,
                        text: T_.lastWeek(),
                      }),
                    )
                  : u().createElement(
                      "div",
                      { className: C()(P_, e) },
                      u().createElement(S_, {
                        size: w_.Small,
                        currentTimerDate: n,
                        text: T_.timer(),
                      }),
                    );
          }),
          N_ = "Progress_base_d5",
          I_ = "Progress_counter_3b",
          L_ = "Progress_current_fd",
          M_ = "Progress_progressBar_d2",
          O_ = R.strings.comp7.weeklyQuests.card.progress,
          H_ = ({ current: e, total: t, isDisabled: a, className: r }) =>
            u().createElement(
              "div",
              { className: C()(N_, r) },
              u().createElement(Ct, {
                classMix: I_,
                text: O_.counter(),
                binding: {
                  current: u().createElement(
                    "div",
                    { className: L_ },
                    u().createElement(Ia, { value: e }),
                  ),
                  total: u().createElement(Ia, { value: t }),
                },
              }),
              u().createElement(
                "div",
                { className: M_ },
                u().createElement(fi, { size: Oo.Small, value: e, maxValue: t, disabled: a }),
              ),
            ),
          W_ = {
            nextArrowWrapper: "TaskBattle_nextArrowWrapper_bb",
            nextArrow: "TaskBattle_nextArrow_32",
            nextArrow__completed: "TaskBattle_nextArrow__completed_0d",
            nextArrow__active: "TaskBattle_nextArrow__active_0a",
            base: "TaskBattle_base_44",
            base__completed: "TaskBattle_base__completed_96",
            "add-shadow": "TaskBattle_add-shadow_a9",
            base__lockedByNoXVehicles: "TaskBattle_base__lockedByNoXVehicles_65",
            base__lockedByInactiveSeason: "TaskBattle_base__lockedByInactiveSeason_b0",
            base__lockedByPreviousQuest: "TaskBattle_base__lockedByPreviousQuest_34",
            base__mediaMediumHeight: "TaskBattle_base__mediaMediumHeight_96",
            taskType: "TaskBattle_taskType_94",
            conditions: "TaskBattle_conditions_2d",
            description: "TaskBattle_description_f6",
            description__completed: "TaskBattle_description__completed_a2",
            "update-condition": "TaskBattle_update-condition_a0",
            description__completedWasVisited: "TaskBattle_description__completedWasVisited_42",
            awards: "TaskBattle_awards_0a",
            "add-blur": "TaskBattle_add-blur_68",
            base__completedWasVisited: "TaskBattle_base__completedWasVisited_8a",
            awardsList: "TaskBattle_awardsList_bf",
            award: "TaskBattle_award_8b",
            hide: "TaskBattle_hide_e0",
            show: "TaskBattle_show_4d",
          },
          $_ = {
            base: "TaskType_base_d9",
            ellipse: "TaskType_ellipse_95",
            base__completed: "TaskType_base__completed_00",
            hide: "TaskType_hide_4e",
            base__completedWasVisited: "TaskType_base__completedWasVisited_28",
            base__lockedByNoXVehicles: "TaskType_base__lockedByNoXVehicles_99",
            base__lockedByInactiveSeason: "TaskType_base__lockedByInactiveSeason_c5",
            base__lockedByPreviousQuest: "TaskType_base__lockedByPreviousQuest_42",
            typeIcon: "TaskType_typeIcon_0c",
            completedIcon: "TaskType_completedIcon_cf",
            lockIcon: "TaskType_lockIcon_20",
            "slide-down": "TaskType_slide-down_53",
            "add-blur": "TaskType_add-blur_1d",
            show: "TaskType_show_a3",
          },
          U_ = ({ taskBattleIcon: e, statusAnimation: t }) =>
            u().createElement(
              "div",
              { className: C()($_.base, $_[`base__${t}`]) },
              u().createElement("div", { className: $_.ellipse }),
              u().createElement("div", {
                className: $_.typeIcon,
                style: {
                  backgroundImage: `url('${R.images.comp7.gui.maps.icons.comp7.weekly_quests.$dyn(e)}')`,
                },
              }),
              u().createElement("div", { className: $_.completedIcon }),
              u().createElement("div", { className: $_.lockIcon }),
            );
        function z_() {
          return (
            (z_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var r in a) Object.prototype.hasOwnProperty.call(a, r) && (e[r] = a[r]);
                }
                return e;
              }),
            z_.apply(this, arguments)
          );
        }
        const G_ = (0, q.Pi)(({ index: e }) => {
            const t = (0, s.useState)(Qd.Active),
              a = t[0],
              r = t[1],
              n = om().model,
              o = n.computes.questRewards,
              i = n.computes.questCard(e),
              l = i.state,
              c = i.currentProgress,
              d = i.totalProgress,
              m = i.description,
              _ = i.iconKey,
              E = P();
            return (
              (0, s.useEffect)(() => {
                r(l);
              }, [l]),
              u().createElement(
                u().Fragment,
                null,
                Boolean(e) &&
                  u().createElement(
                    "div",
                    { className: W_.nextArrowWrapper },
                    u().createElement("div", {
                      className: C()(W_.nextArrow, W_[`nextArrow__${a}`]),
                    }),
                  ),
                u().createElement(
                  "div",
                  {
                    className: C()(
                      W_.base,
                      W_[`base__${a}`],
                      E.mediaSize === B.Medium &&
                        E.remScreenHeight >= 1024 &&
                        W_.base__mediaMediumHeight,
                    ),
                  },
                  u().createElement(
                    "div",
                    { className: W_.taskType },
                    u().createElement(U_, { taskBattleIcon: _, statusAnimation: a }),
                  ),
                  u().createElement(
                    "div",
                    { className: W_.conditions },
                    u().createElement(
                      "div",
                      { className: C()(W_.description, W_[`description__${a}`]) },
                      m,
                    ),
                    l === Qd.Active &&
                      u().createElement(H_, { current: c, total: d, isDisabled: l !== Qd.Active }),
                  ),
                  u().createElement(
                    "div",
                    { className: W_.awards },
                    u().createElement(
                      F_,
                      { statusAnimation: a, type: D_.Awards },
                      u().createElement(
                        "div",
                        { className: W_.awardsList },
                        ve(o(e, fc.Small), (e) =>
                          u().createElement(Mc, z_({ className: W_.award, key: e.name }, e)),
                        ),
                      ),
                    ),
                  ),
                ),
              )
            );
          }),
          j_ = {
            "--pageContentWidth": "78vw",
            base__completed: "TaskBattleList_base__completed_e6",
            "hidden-tasks-list": "TaskBattleList_hidden-tasks-list_39",
            base: "TaskBattleList_base_c6",
            scroll: "TaskBattleList_scroll_73",
            timerWithQuestsTotal: "TaskBattleList_timerWithQuestsTotal_39",
            timer: "TaskBattleList_timer_fe",
            taskList: "TaskBattleList_taskList_d4",
            scrollContainer: "TaskBattleList_scrollContainer_e0",
            areaContainer: "TaskBattleList_areaContainer_fb",
            areaWrapper: "TaskBattleList_areaWrapper_04",
            bar: "TaskBattleList_bar_d9",
            "add-blur": "TaskBattleList_add-blur_67",
            hide: "TaskBattleList_hide_56",
            show: "TaskBattleList_show_f9",
            fadeIn: "TaskBattleList_fadeIn_38",
            fadeInThreeQuarters: "TaskBattleList_fadeInThreeQuarters_b4",
            fadeInHalf: "TaskBattleList_fadeInHalf_5a",
            fadeOut: "TaskBattleList_fadeOut_f6",
            fadeInWithScale: "TaskBattleList_fadeInWithScale_0a",
            slideUp: "TaskBattleList_slideUp_dd",
            scale: "TaskBattleList_scale_d4",
            raysAppearance: "TaskBattleList_raysAppearance_32",
            rotate: "TaskBattleList_rotate_3f",
            "reverse-rotate": "TaskBattleList_reverse-rotate_56",
            glowAppearance: "TaskBattleList_glowAppearance_55",
            highlightAppearance: "TaskBattleList_highlightAppearance_7c",
            blink: "TaskBattleList_blink_1d",
            slideUpIn: "TaskBattleList_slideUpIn_33",
          },
          q_ = (0, q.Pi)(() => {
            const e = om().model.computes,
              t = e.questCards,
              a = e.battleTasksStatus,
              r = e.initialItemScrollIndex,
              n = e.getScrollContainerMaxWidth,
              o = P(),
              i = (0, s.useState)(r()),
              l = i[0],
              c = i[1],
              d = So(268),
              m = t.get();
            return u().createElement(
              "div",
              { className: C()(j_.base, j_[`base__${a()}`]) },
              u().createElement(
                "div",
                { className: j_.taskList },
                u().createElement(
                  wo,
                  {
                    api: d,
                    stuckIndex: l,
                    itemWidth: 268,
                    onStick: c,
                    className: j_.scrollContainer,
                    areaClassNames: { base: j_.areaContainer, wrapper: j_.areaWrapper },
                    barClassNames: { base: j_.bar },
                    containerMaxWidth: n(o.mediaSize, m, 268, 38),
                  },
                  ve(m, (e, t) => u().createElement(G_, { key: t, index: t })),
                ),
              ),
            );
          }),
          V_ = "WeeklyQuestsPage_base_6c",
          X_ = "WeeklyQuestsPage_content_cc",
          Q_ = "WeeklyQuestsPage_resetStatus_8a",
          Y_ = "WeeklyQuestsPage_progression_25",
          K_ = () => {
            const e = (0, ke.useSpring)(_e);
            return u().createElement(
              "div",
              { className: V_ },
              u().createElement(st, { className: K }, R.strings.comp7.page.heading.weeklyQuests()),
              u().createElement(It, null),
              u().createElement(
                ke.animated.div,
                { className: X_, style: e },
                u().createElement(x_, { className: Q_ }),
                u().createElement(q_, null),
                u().createElement(u_, { className: Y_ }),
              ),
            );
          },
          Z_ = { context: "model.weeklyQuestsModel" },
          J_ = {
            [de.Progression]: () =>
              u().createElement(ks, { options: mc }, u().createElement(dc, null)),
            [de.RankRewards]: () =>
              u().createElement(Ec, { options: Xd }, u().createElement(Vd, null)),
            [de.WeeklyQuests]: () =>
              u().createElement(um, { options: Z_ }, u().createElement(K_, null)),
            [de.Leaderboard]: () =>
              u().createElement(jt, { options: Cs }, u().createElement(vs, null)),
          },
          eE = ({ pageView: e }) => {
            const t = J_[e];
            return t
              ? u().createElement(t, null)
              : (console.error("Unreachable code: ViewResolver"), null);
          },
          tE = {
            "--pageContentWidth": "78vw",
            base: "App_base_ef",
            base__qualification: "App_base__qualification_73",
            base__leaderboard: "App_base__leaderboard_da",
            base__rankRewards: "App_base__rankRewards_55",
            base__weeklyQuests: "App_base__weeklyQuests_58",
            viewContainer: "App_viewContainer_81",
            sidebar: "App_sidebar_95",
            info: "App_info_e9",
          },
          aE = { context: "model.sidebar" },
          rE = { context: "model.scheduleInfo" },
          nE = (0, q.Pi)(() => {
            const e = be(),
              t = e.model,
              a = e.controls,
              r = t.root.get().pageViewId,
              n = t.computes.isProgressionInQualification(),
              s = me[r];
            return u().createElement(
              "div",
              {
                className: C()(
                  tE.base,
                  n && !ee() && tE.base__qualification,
                  !n && s && tE[`base__${s}`],
                ),
              },
              u().createElement(
                "div",
                { className: tE.viewContainer },
                u().createElement(le, { options: rE }, u().createElement(eE, { pageView: r })),
              ),
              u().createElement(
                Pe,
                { options: aE },
                u().createElement(Ye, { pageView: r, className: tE.sidebar }),
              ),
              u().createElement(
                "div",
                { className: tE.info },
                u().createElement(j, {
                  caption: R.strings.comp7.infoPageButtonLabel(),
                  type: "info",
                  side: "left",
                  onClick: a.openInfoPage,
                }),
              ),
              u().createElement(J, { onClose: a.close }),
            );
          });
        engine.whenReady.then(() => {
          H().render(
            u().createElement(M, null, u().createElement(pe, null, u().createElement(nE, null))),
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
    (__webpack_require__.O = (e, t, a, r) => {
      if (!t) {
        var n = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, a, r] = deferred[i], s = !0, u = 0; u < t.length; u++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[u]))
              ? t.splice(u--, 1)
              : ((s = !1), r < n && (n = r));
          if (s) {
            deferred.splice(i--, 1);
            var o = a();
            void 0 !== o && (e = o);
          }
        }
        return e;
      }
      r = r || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > r; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, a, r];
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
    (__webpack_require__.j = 992),
    (() => {
      var e = { 992: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var r,
            n,
            [s, u, o] = a,
            i = 0;
          if (s.some((t) => 0 !== e[t])) {
            for (r in u) __webpack_require__.o(u, r) && (__webpack_require__.m[r] = u[r]);
            if (o) var l = o(__webpack_require__);
          }
          for (t && t(a); i < s.length; i++)
            ((n = s[i]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(l);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [926], () => __webpack_require__(4304));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
