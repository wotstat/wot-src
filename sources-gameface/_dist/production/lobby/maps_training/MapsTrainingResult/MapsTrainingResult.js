(() => {
  "use strict";
  var __webpack_modules__ = {
      527: (e, u, t) => {
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => s }));
        var n = t(472),
          a = t(176);
        const s = (0, n.E)("clientResized"),
          r = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, a.R)(!1);
          }
          function t() {
            e.enabled && (0, a.R)(!0);
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
              : (0, a.R)(!1);
          }
          const s = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let a = !0;
                  const s = `mouse${u}`,
                    i = r[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(s, o),
                    n(),
                    () => {
                      a &&
                        (i(), window.removeEventListener(s, o), (e.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, s, {
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
      959: (e, u, t) => {
        (t.r(u),
          t.d(u, {
            events: () => n,
            getMouseGlobalPosition: () => s,
            getSize: () => a,
            graphicsQuality: () => r,
          }));
        var n = t(527);
        function a(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function s(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const r = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      176: (e, u, t) => {
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => n });
      },
      472: (e, u, t) => {
        function n(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        t.d(u, { E: () => n });
      },
      138: (e, u, t) => {
        t.d(u, { O: () => a });
        var n = t(959);
        const a = { view: t(641), client: n };
      },
      722: (e, u, t) => {
        function n(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function a(e, u, t) {
          return `url(${n(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => a, getTextureUrl: () => n }));
      },
      112: (e, u, t) => {
        t.d(u, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, u, t) => {
        t.d(u, { U: () => a });
        var n = t(472);
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
      641: (e, u, t) => {
        (t.r(u),
          t.d(u, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => n,
            displayStatus: () => a.W,
            displayStatusIs: () => f,
            events: () => s.U,
            extraSize: () => T,
            forceTriggerMouseMove: () => b,
            freezeTextureBeforeResize: () => d,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => v,
            getScale: () => m,
            getSize: () => _,
            getViewGlobalPosition: () => F,
            isClientAccessible: () => p,
            isEventHandled: () => w,
            isFocused: () => C,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => A,
            sendEvent: () => r.qP,
            setAnimateWindow: () => g,
            setEventHandled: () => h,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => S,
          }));
        var n = t(722),
          a = t(112),
          s = t(538),
          r = t(566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function c(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function E(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function _(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function A(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function F(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: B(u.x), y: B(u.y) };
        }
        function d() {
          viewEnv.freezeTextureBeforeResize();
        }
        function m() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function B(e) {
          return viewEnv.remToPx(e);
        }
        function g(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function p() {
          return viewEnv.isClientAccessible();
        }
        function h() {
          return viewEnv.setEventHandled();
        }
        function w() {
          return viewEnv.isEventHandled();
        }
        function b() {
          viewEnv.forceTriggerMouseMove();
        }
        function v() {
          return viewEnv.getShowingStatus();
        }
        const f = Object.keys(a.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === a.W[u]), e),
            {},
          ),
          T = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          S = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : s.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, u, t) => {
        t.d(u, { qP: () => l });
        const n = ["args"];
        const a = 2,
          s = 16,
          r = 32,
          i = 64,
          o = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const s = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    s = Object.keys(e);
                  for (n = 0; n < s.length; n++) ((t = s[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, n);
              return void 0 !== s
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((a = s),
                        Object.entries(a).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var a;
          },
          l = {
            close(e) {
              o("popover" === e ? a : r);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(s, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, u, t) => {
        let n, a;
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
          })(a || (a = {})));
      },
      358: (e, u, t) => {
        t.d(u, { Z: () => s });
        var n = t(138);
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
          addCallback(e, u, t = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const s = n.O.view.addModelObserver(e, t, a);
            return (
              s > 0
                ? ((this._callbacks[s] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(s) : (this._views[t] = [s])))
                : console.error("Can't add callback for model:", e),
              s
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
        a.__instance = void 0;
        const s = a;
      },
      572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
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
        t.d(u, { Sw: () => s.Z, B3: () => l, Z5: () => r, B0: () => o, ry: () => B });
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
        const a = n;
        var s = t(358);
        const r = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          i = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
          };
        let o;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(o || (o = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var A = t(521),
          F = t(138);
        const d = ["args"];
        function m(e, u, t, n, a, s, r) {
          try {
            var i = e[s](r),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(n, a);
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
                  return new Promise(function (n, a) {
                    var s = e.apply(u, t);
                    function r(e) {
                      m(s, n, a, r, i, "next", e);
                    }
                    function i(e) {
                      m(s, n, a, r, i, "throw", e);
                    }
                    r(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          g = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                s = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    s = Object.keys(e);
                  for (n = 0; n < s.length; n++) ((t = s[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, d);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, s, {
                      arguments:
                        ((n = a),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, s));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          C = () => g(o.CLOSE),
          p = (e, u) => {
            e.keyCode === A.n.ESCAPE && u();
          };
        var h = t(572);
        const w = a.instance,
          b = {
            DataTracker: s.Z,
            ViewModel: h.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: _,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => g(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => g(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              g(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, a = R.invalid("resId"), s) => {
              const r = F.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                E = i.width,
                _ = i.height,
                A = {
                  x: F.O.view.pxToRem(l) + r.x,
                  y: F.O.view.pxToRem(c) + r.y,
                  width: F.O.view.pxToRem(E),
                  height: F.O.view.pxToRem(_),
                };
              g(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: a,
                direction: u,
                bbox: D(A),
                on: !0,
                args: s,
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
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const n in u)
                if (Object.prototype.hasOwnProperty.call(u, n)) {
                  const a = Object.prototype.toString.call(u[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = u[n];
                    t[n] = [];
                    for (let u = 0; u < a.length; u++) t[n].push({ value: e(a[u].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = e(u[n]))
                      : (t[n] = u[n]);
                }
              return t;
            },
            ClickOutsideManager: w,
            SystemLocale: r,
            UserLocale: i,
          };
        window.ViewEnvHelper = b;
      },
      637: (e, u, t) => {
        var n = t(179),
          a = t.n(n),
          s = t(493),
          r = t.n(s);
        const i = (e, u, t) =>
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
        var o = t(138);
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
            a = (function (e, u) {
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
            s = Math.min(n, a);
          return {
            extraLarge: s === t.extraLarge.weight,
            large: s === t.large.weight,
            medium: s === t.medium.weight,
            small: s === t.small.weight,
            extraSmall: s === t.extraSmall.weight,
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
        const _ = o.O.client.getSize("rem"),
          A = _.width,
          F = _.height,
          d = Object.assign({ width: A, height: F }, E(A, F, l)),
          m = (0, n.createContext)(d),
          D = ["children"];
        const B = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                s = Object.keys(e);
              for (n = 0; n < s.length; n++) ((t = s[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, D);
          const a = (0, n.useContext)(m),
            s = a.extraLarge,
            r = a.large,
            o = a.medium,
            l = a.small,
            c = a.extraSmall,
            E = a.extraLargeWidth,
            _ = a.largeWidth,
            A = a.mediumWidth,
            F = a.smallWidth,
            d = a.extraSmallWidth,
            B = a.extraLargeHeight,
            g = a.largeHeight,
            C = a.mediumHeight,
            p = a.smallHeight,
            h = a.extraSmallHeight,
            w = { extraLarge: B, large: g, medium: C, small: p, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return u;
            if (t.large && r) return u;
            if (t.medium && o) return u;
            if (t.small && l) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && E) return i(u, t, w);
            if (t.largeWidth && _) return i(u, t, w);
            if (t.mediumWidth && A) return i(u, t, w);
            if (t.smallWidth && F) return i(u, t, w);
            if (t.extraSmallWidth && d) return i(u, t, w);
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
        (0, n.memo)(B);
        const g = (e) => {
            const u = (0, n.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          C = (0, n.memo)(({ children: e }) => {
            const u = (0, n.useContext)(m),
              t = (0, n.useState)(u),
              s = t[0],
              r = t[1],
              i = (0, n.useCallback)((e, u) => {
                const t = o.O.view.pxToRem(e),
                  n = o.O.view.pxToRem(u);
                r(Object.assign({ width: t, height: n }, E(t, n, l)));
              }, []);
            (g(() => {
              engine.on("clientResized", i);
            }),
              (0, n.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, n.useMemo)(() => Object.assign({}, s), [s]);
            return a().createElement(m.Provider, { value: c }, e);
          }),
          p = (e = 1) => {
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
          },
          h = (e, u) => e.split(".").reduce((e, u) => e && e[u], u);
        var w = t(364);
        const b = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          v = (e, u) => (e.length > 0 ? `${e}.${u}` : u),
          f = (e) =>
            ((e, u) =>
              e.split(".").reduce((e, t) => {
                const n = h(`${e}.${t}`, window);
                return b(n) ? u(e, t, n) : `${e}.${t}`;
              }))(e, (e, u) => `${e}.${u}.value`),
          T = (e) => {
            const u = ((e) => {
                const u = p(),
                  t = u.caller,
                  n = u.resId,
                  a = window.__feature && window.__feature !== t && t ? `subViews.${t}` : "";
                return { modelPrefix: a, modelPath: v(a, e || ""), resId: n };
              })(),
              t = u.modelPrefix,
              n = e.split(".");
            if (n.length > 0) {
              const e = [n[0]];
              return (
                n.reduce((u, n) => {
                  const a = h(v(t, `${u}.${n}`), window);
                  return b(a) ? (e.push(a.id), `${u}.${n}.value`) : (e.push(n), `${u}.${n}`);
                }),
                e.reduce((e, u) => e + "." + u)
              );
            }
            return "";
          },
          S = w.Sw.instance;
        let y;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(y || (y = {}));
        const x = (e = "model", u = y.Deep) => {
          const t = (0, n.useState)(0),
            a = (t[0], t[1]),
            s = (0, n.useMemo)(() => p(), []),
            r = s.caller,
            i = s.resId,
            o = (0, n.useMemo)(
              () => (window.__feature && window.__feature !== r ? `subViews.${r}.${e}` : e),
              [r, e],
            ),
            l = (0, n.useState)(() =>
              ((e) => {
                const u = h(e, window);
                for (const e in u) "function" == typeof u[e] && (u[e] = u[e].bind(u));
                return b(u) ? u.value : u;
              })(f(o)),
            ),
            c = l[0],
            E = l[1],
            _ = (0, n.useRef)(-1);
          return (
            g(() => {
              if (
                ("boolean" == typeof u &&
                  ((u = u ? y.Deep : y.None),
                  console.warn(
                    'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                  )),
                u !== y.None)
              ) {
                const t = (e) => {
                    ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                    u === y.Deep
                      ? (e === c && a((e) => e + 1), E(e))
                      : E(Object.assign([], e));
                  },
                  n = T(e);
                _.current = S.addCallback(n, t, i, u === y.Deep);
              }
            }),
            (0, n.useEffect)(() => {
              if (u !== y.None)
                return () => {
                  S.removeCallback(_.current, i);
                };
            }, [i, u]),
            c
          );
        };
        var k = t(483),
          P = t.n(k);
        let M;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(M || (M = {}));
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
        function O(e, u, t) {
          const a = (0, n.useContext)(m);
          let s = Object.entries(a).filter(([e, u]) => !0 === u && e in c);
          return (
            t && (s = s.filter((e) => t.includes(e[0]))),
            e.reduce((e, t) => {
              const n = s.map((e) =>
                P()(
                  u[((e, u) => e + "__" + u)(t, e[0])],
                  u[
                    ((e, u) => {
                      return e + ((t = u)[0].toUpperCase() + t.slice(1));
                      var t;
                    })(t, e[0])
                  ],
                ),
              );
              return ((e[t] = P()(u[t], ...n)), e);
            }, {})
          );
        }
        var N = t(521);
        const L = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function I(e = N.n.NONE, u = L, t = !1) {
          (0, n.useEffect)(() => {
            if (e !== N.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (o.O.view.isEventHandled()) return;
                (o.O.view.setEventHandled(), u(n), t && n.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        function U(e) {
          engine.call("PlaySound", e);
        }
        const H = {
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
        let G, $;
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
          })($ || ($ = {})));
        const W = ({
          children: e,
          size: u,
          isFocused: t,
          type: s,
          disabled: r,
          mixClass: i,
          soundHover: o,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: E,
          onMouseDown: _,
          onMouseUp: A,
          onMouseLeave: F,
          onClick: d,
        }) => {
          const m = (0, n.useRef)(null),
            D = (0, n.useState)(t),
            B = D[0],
            g = D[1],
            C = (0, n.useState)(!1),
            p = C[0],
            h = C[1],
            w = (0, n.useState)(!1),
            b = w[0],
            v = w[1],
            f = (0, n.useCallback)(() => {
              r || (m.current && (m.current.focus(), g(!0)));
            }, [r]),
            T = (0, n.useCallback)(
              (e) => {
                B && null !== m.current && !m.current.contains(e.target) && g(!1);
              },
              [B],
            ),
            S = (0, n.useCallback)(
              (e) => {
                r || (d && d(e));
              },
              [r, d],
            ),
            y = (0, n.useCallback)(
              (e) => {
                r || (null !== o && U(o), c && c(e), v(!0));
              },
              [r, o, c],
            ),
            x = (0, n.useCallback)(
              (e) => {
                E && E(e);
              },
              [E],
            ),
            k = (0, n.useCallback)(
              (e) => {
                r || (A && A(e), h(!1));
              },
              [r, A],
            ),
            M = (0, n.useCallback)(
              (e) => {
                r || (null !== l && U(l), _ && _(e), t && f(), h(!0));
              },
              [r, l, _, f, t],
            ),
            O = (0, n.useCallback)(
              (e) => {
                r || (F && F(e), h(!1));
              },
              [r, F],
            ),
            N = P()(
              H.base,
              H[`base__${s}`],
              {
                [H.base__disabled]: r,
                [H[`base__${u}`]]: u,
                [H.base__focus]: B,
                [H.base__highlightActive]: p,
                [H.base__firstHover]: b,
              },
              i,
            ),
            L = P()(H.state, H.state__default);
          return (
            (0, n.useEffect)(
              () => (
                document.addEventListener("mousedown", T),
                () => {
                  document.removeEventListener("mousedown", T);
                }
              ),
              [T],
            ),
            (0, n.useEffect)(() => {
              g(t);
            }, [t]),
            a().createElement(
              "div",
              {
                ref: m,
                className: N,
                onMouseEnter: y,
                onMouseMove: x,
                onMouseUp: k,
                onMouseDown: M,
                onMouseLeave: O,
                onClick: S,
              },
              s !== G.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: H.back }),
                  a().createElement("span", { className: H.texture }),
                ),
              a().createElement(
                "span",
                { className: L },
                a().createElement("span", { className: H.stateDisabled }),
                a().createElement("span", { className: H.stateHighlightHover }),
                a().createElement("span", { className: H.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: H.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        W.defaultProps = {
          type: G.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Y = (0, n.memo)(W),
          q = {
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
          V = [
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
        function z() {
          return (
            (z =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            z.apply(this, arguments)
          );
        }
        class X extends a().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && U(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && U(this.props.soundClick));
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
              s = e.side,
              r = e.type,
              i = e.classNames,
              o = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              E = e.onMouseUp,
              _ =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    s = Object.keys(e);
                  for (n = 0; n < s.length; n++) ((t = s[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(e, V)),
              A = P()(q.base, q[`base__${r}`], q[`base__${s}`], null == i ? void 0 : i.base),
              F = P()(q.icon, q[`icon__${r}`], q[`icon__${s}`], null == i ? void 0 : i.icon),
              d = P()(q.glow, null == i ? void 0 : i.glow),
              m = P()(q.caption, q[`caption__${r}`], null == i ? void 0 : i.caption),
              D = P()(q.goto, null == i ? void 0 : i.goto);
            return a().createElement(
              "div",
              z(
                {
                  className: A,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(E),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                _,
              ),
              "info" !== r && a().createElement("div", { className: q.shine }),
              a().createElement(
                "div",
                { className: F },
                a().createElement("div", { className: d }),
              ),
              a().createElement("div", { className: m }, u),
              n && a().createElement("div", { className: D }, n),
            );
          }
        }
        let j;
        ((X.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (e) {
            ((e[(e.Undone = 0)] = "Undone"),
              (e[(e.PartialDone = 1)] = "PartialDone"),
              (e[(e.Done = 2)] = "Done"));
          })(j || (j = {})));
        let K;
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
        })(K || (K = {}));
        Date.now();
        w.Sw.instance;
        let Z;
        !(function (e) {
          ((e[(e.Init = 0)] = "Init"),
            (e[(e.TitleAndRewards = 1)] = "TitleAndRewards"),
            (e[(e.Done = 2)] = "Done"));
        })(Z || (Z = {}));
        const Q = (e, u, t) =>
            P()(
              e,
              t >= Z.TitleAndRewards && u.base__animTitleAndRewards,
              t >= Z.Done && u.base__done,
            ),
          J = {
            base: "StatItem_base_70",
            base__animTitleAndRewards: "StatItem_base__animTitleAndRewards_af",
            icon: "StatItem_icon_59",
            icon__destroy: "StatItem_icon__destroy_df",
            icon__timer: "StatItem_icon__timer_4b",
            value: "StatItem_value_22",
            valueAll: "StatItem_valueAll_01",
            description: "StatItem_description_5e",
          };
        let ee;
        !(function (e) {
          ((e.Destroy = "destroy"), (e.Timer = "timer"));
        })(ee || (ee = {}));
        const ue = (0, n.memo)(
            ({ value: e, label: u, icon: t, index: s, animState: r, all: i }) => {
              const o = (0, n.useMemo)(() => ({ transitionDelay: 0.9 + 0.1 * s + "s" }), [s]),
                l = Q(J.base, J, r),
                c = P()(J.icon, J[`icon__${t}`]);
              return a().createElement(
                "div",
                { className: l, style: o },
                a().createElement("div", { className: c }),
                a().createElement(
                  "div",
                  { className: J.value },
                  e,
                  void 0 !== i &&
                    i > 0 &&
                    a().createElement("div", { className: J.valueAll }, ` / ${i}`),
                ),
                a().createElement("div", { className: J.description }, u),
              );
            },
          ),
          te = {
            base: "Tank_base_c1",
            wrap: "Tank_wrap_4b",
            image: "Tank_image_12",
            bg: "Tank_bg_68",
            bg__back: "Tank_bg__back_e8",
            base__defeat: "Tank_base__defeat_8c",
            bg__foreground: "Tank_bg__foreground_7e",
            back: "Tank_back_79",
          },
          ne = (0, n.memo)(({ vehicleImage: e, isAnyNotDone: u }) => {
            const t = (0, n.useMemo)(() => ({ backgroundImage: `url(${e})` }), [e]),
              s = O(["base"], te),
              r = P()(s.base, u && te.base__defeat),
              i = P()(te.bg, te.bg__back),
              o = P()(te.bg, te.bg__foreground);
            return a().createElement(
              "div",
              { className: r },
              a().createElement("div", { className: i }),
              a().createElement(
                "div",
                { className: te.wrap },
                a().createElement("div", { className: te.image, style: t }),
              ),
              a().createElement("div", { className: o }),
              a().createElement("div", { className: te.back }),
            );
          }),
          ae = {
            base: "ResultStats_base_ce",
            base__small: "ResultStats_base__small_de",
            base__extraSmall: "ResultStats_base__extraSmall_11",
            base__animTitleAndRewards: "ResultStats_base__animTitleAndRewards_bd",
            stats: "ResultStats_stats_55",
            separator: "ResultStats_separator_46",
            separator__failed: "ResultStats_separator__failed_b8",
          };
        function se() {
          return (
            (se =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            se.apply(this, arguments)
          );
        }
        const re = R.strings.maps_training.result,
          ie = (0, n.memo)(({ animState: e, hasReward: u }) => {
            const t = x("model"),
              s = t.vehicleImage,
              r = t.kills,
              i = t.time,
              o = t.doneValue,
              l = t.allTargets,
              c = (0, n.useMemo)(
                () => [
                  { label: re.kills(), value: r, all: l, icon: ee.Destroy },
                  { label: re.time(), value: i, icon: ee.Timer },
                ],
                [r, i, l],
              ),
              E = o !== j.Done,
              _ = O(["base"], ae),
              A = P()(Q(_.base, ae, e), E && ae.base__defeat),
              F = P()(ae.separator, E && ae.separator__failed);
            return a().createElement(
              "div",
              { className: A },
              a().createElement(ne, { vehicleImage: s, isAnyNotDone: E }),
              a().createElement(
                "div",
                { className: ae.stats },
                c.map((u, t) =>
                  a().createElement(ue, se({ key: `item_${t}`, index: t, animState: e }, u)),
                ),
              ),
              !u && a().createElement("div", { className: F }),
            );
          });
        class oe extends a().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = w.B3.GOLD;
            else e = w.B3.INTEGRAL;
            const u = w.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        let le, ce, Ee, _e, Ae, Fe, de, me, De;
        ((oe.defaultProps = { format: "integral" }),
          (function (e) {
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
              (e.Entitlements = "entitlements"),
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
              (e.NyPetGoodies = "nyPetGoodies"),
              (e.HiddenVehicle = "hidden_vehicle"),
              (e.NyStaticDogTag = "nyStaticDogTag"),
              (e.NyToys = "nyToys"),
              (e.NyLootboxFragment = "nyLootboxFragment"));
          })(le || (le = {})),
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
          })(ce || (ce = {})),
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
          })(Ee || (Ee = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(_e || (_e = {})),
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
          })(Ae || (Ae = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(Fe || (Fe = {})),
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
          })(de || (de = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(me || (me = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(De || (De = {})));
        (le.Items,
          le.Equipment,
          le.Xp,
          le.XpFactor,
          le.Blueprints,
          le.BlueprintsAny,
          le.Goodies,
          le.Berths,
          le.Slots,
          le.Tokens,
          le.CrewSkins,
          le.CrewBooks,
          le.Customizations,
          le.CreditsFactor,
          le.TankmenXp,
          le.TankmenXpFactor,
          le.FreeXpFactor,
          le.BattleToken,
          le.Entitlements,
          le.PremiumUniversal,
          le.NaturalCover,
          le.BpCoin,
          le.BattlePassSelectToken,
          le.BattlaPassFinalAchievement,
          le.BattleBadge,
          le.BonusX5,
          le.CrewBonusX3,
          le.NewYearFillers,
          le.NewYearInvoice,
          le.EpicSelectToken,
          le.Comp7TokenWeeklyReward,
          le.Comp7TokenCouponReward,
          le.BattleBoosterGift,
          le.NewYearFillers,
          le.NewYearInvoice,
          le.LootBoxToken,
          le.CosmicLootboxCommon,
          le.CosmicLootboxSilver,
          le.SelectableBonus,
          le.PostStamp,
          le.PremiumPlusUniversal,
          le.GoldenTicket,
          le.RewardsSlots,
          le.NyPetGoodies,
          le.HiddenVehicle,
          le.NyLootboxFragment,
          le.Gold,
          le.Credits,
          le.Crystal,
          le.FreeXp,
          le.NewYearToyFragments,
          le.BattlePassPoints,
          le.PremiumPlus,
          le.Premium);
        let Be;
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
        })(Be || (Be = {}));
        const ge = ["engravings", "backgrounds"],
          Ce = ["engraving", "background"],
          pe = (e, u = Ee.Small, t) => {
            const n = e.name,
              a = e.type,
              s = e.value,
              r = e.icon,
              i = e.item,
              o = e.dogTagType,
              l = ((e) => {
                switch (e) {
                  case Ee.S600x450:
                    return "c_600x450";
                  case Ee.S400x300:
                    return "c_400x300";
                  case Ee.S296x222:
                    return "c_296x222";
                  case Ee.S232x174:
                    return "c_232x174";
                  case Ee.Big:
                    return "c_80x80";
                  case Ee.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (n) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}_${s}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_plus_${s}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_${s}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${i}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${r}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case Ee.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case Ee.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "entitlements":
                return "big" === u
                  ? e.iconBig.replace("..", "img://gui")
                  : e.iconSmall.replace("..", "img://gui");
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${r}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const n = ge[e];
                  if (n) {
                    const a = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(n),
                      s = a.$dyn(t);
                    return s ? `${s}` : `${a.$dyn(Ce[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, u, r);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${l}.${r}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case Ee.S600x450:
                      return "c_600x450";
                    case Ee.S400x300:
                      return "c_400x300";
                    case Ee.S296x222:
                      return "c_296x222";
                    case Ee.S232x174:
                      return "c_232x174";
                    case Ee.S180x135:
                      return "big";
                    case Ee.Big:
                    case Ee.S80x80:
                      return "c_80x80";
                    case Ee.Small:
                    case Ee.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${r}`;
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
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${r}`;
              case "nyPetGoodies":
                return `R.images.new_year.gui.maps.icons.newYear.common.categoriesIcons.${u}.${r}`;
              case "nyLootboxFragment":
                return `R.images.new_year.gui.maps.icons.newYear.common.rewards.fragments.${u}.lootbox_fragment`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${l}.${r}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case Ee.Mini:
                      return Be.s32;
                    case Ee.Small:
                    case Ee.S48x48:
                      return Be.s48;
                    case Ee.S80x80:
                    case Ee.Big:
                      return Be.s80;
                    case Ee.S128x100:
                      return Be.s116;
                    case Ee.S180x135:
                    case Ee.S232x174:
                    case Ee.S296x222:
                      return Be.s296;
                    case Ee.S400x300:
                      return Be.s400;
                    case Ee.S600x450:
                      return Be.s600;
                  }
                })(u)}`;
              case le.StyleProgress:
              case le.LbStyleProgress:
                return he(r, u, De.ProgressionStyle);
              case "newYearAlbumsAccess":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.albumsAccess`;
              case "nyFillers":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.fillers`;
              case "nyToyFragments":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.shards`;
              case "newYearSlot":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.slot`;
              case "hidden_vehicle":
                return "R.images.new_year.gui.maps.icons.newYear.common.rewards.vehicles.hidden_vehicle";
              case "nyStaticDogTag":
                return `R.images.new_year.gui.maps.icons.newYear.common.rewards.dogtags.${u}.dogtag_${t}`;
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}`;
            }
          },
          he = (e, u, t) => {
            const n = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              a = n.$dyn(e);
            return String(null != a ? a : n.$dyn(t));
          },
          we = [
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
        function be(e) {
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
        const ve = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: w.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          fe = (e) => {
            let u = e.children,
              t = e.contentId,
              a = e.args,
              s = e.onMouseEnter,
              r = e.onMouseLeave,
              i = e.onMouseDown,
              o = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              E = e.ignoreMouseClick,
              _ = void 0 !== E && E,
              A = e.decoratorId,
              F = void 0 === A ? 0 : A,
              d = e.isEnabled,
              m = void 0 === d || d,
              D = e.targetId,
              B = void 0 === D ? 0 : D,
              g = e.onShow,
              C = e.onHide,
              h = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  s = Object.keys(e);
                for (n = 0; n < s.length; n++) ((t = s[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, we);
            const w = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              b = (0, n.useMemo)(() => B || p().resId, [B]),
              v = (0, n.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (ve(t, F, { isMouseEvent: !0, on: !0, arguments: be(a) }, b),
                  g && g(),
                  (w.current.isVisible = !0));
              }, [t, F, a, b, g]),
              f = (0, n.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    ve(t, F, { on: !1 }, b),
                    w.current.isVisible && C && C(),
                    (w.current.isVisible = !1));
                }
              }, [t, F, b, C]),
              T = (0, n.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(w.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", T, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", T, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === m && f();
              }, [m, f]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", f),
                  () => {
                    (window.removeEventListener("mouseleave", f), f());
                  }
                ),
                [f],
              ));
            return m
              ? (0, n.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            s && s(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (f(), null == r || r(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === _ && f(), null == o || o(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === _ && f(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    h,
                  ),
                )
              : u;
            var S;
          },
          Te = {
            base: "Reward_base_63",
            base__animTitleAndRewards: "Reward_base__animTitleAndRewards_bc",
            base__small: "Reward_base__small_da",
            base__extraSmall: "Reward_base__extraSmall_16",
            icon: "Reward_icon_a7",
            info: "Reward_info_f4",
          },
          Se = (0, n.memo)(
            ({
              image: e,
              value: u,
              tooltipId: t,
              animState: s,
              index: r,
              onAnimationCompete: i,
            }) => {
              const o = ((e) => {
                  const u = (0, n.useRef)(null),
                    t = (0, n.useCallback)(() => {
                      e && e();
                    }, [e]);
                  return (
                    (0, n.useEffect)(() => {
                      const e = u.current;
                      if (e)
                        return (
                          e.addEventListener("transitionend", t),
                          () => {
                            e.removeEventListener("transitionend", t);
                          }
                        );
                    }, [u, t]),
                    u
                  );
                })(i),
                l = (0, n.useMemo)(() => ({ tooltipId: t }), [t]),
                c = 1.2 + 0.3 * r,
                E = s > Z.Init;
              (0, n.useEffect)(() => {
                if (E) {
                  const e = setTimeout(() => U(R.sounds.gui_random_reward_appear()), 1e3 * c);
                  return () => clearTimeout(e);
                }
              }, [c, E]);
              const _ = (0, n.useMemo)(() => ({ transitionDelay: `${c}s` }), [c]),
                A = (0, n.useMemo)(() => ({ backgroundImage: `url(${e})` }), [e]),
                F = O(["base"], Te),
                d = Q(F.base, Te, s);
              return a().createElement(
                fe,
                {
                  ignoreShowDelay: !0,
                  ignoreMouseClick: !0,
                  contentId:
                    R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                      "resId",
                    ),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: l,
                },
                a().createElement(
                  "div",
                  { className: d, style: _, ref: o },
                  a().createElement("div", { className: Te.icon, style: A }),
                  Number(u) > 1 && a().createElement("div", { className: Te.info }, u),
                ),
              );
            },
          ),
          Re = {
            base: "NoReward_base_18",
            base__animTitleAndRewards: "NoReward_base__animTitleAndRewards_6d",
            item: "NoReward_item_62",
            item__got: "NoReward_item__got_c8",
          },
          ye = R.strings.maps_training.result,
          xe = {
            [j.Undone]: ye.rewardNotGot(),
            [j.PartialDone]: ye.rewardGot(),
            [j.Done]: ye.allRewardGot(),
          },
          ke = (0, n.memo)(({ rewardGot: e, doneValue: u, wasDone: t, animState: n }) => {
            const s = O(["base"], Re),
              r = Q(s.base, Re, n),
              i = P()(Re.item, (e || t) && Re.item__got);
            return a().createElement(
              "div",
              { className: r },
              a().createElement("div", { className: i }, t ? ye.allRewardGot() : xe[u]),
            );
          }),
          Pe = {
            base: "ResultRewards_base_75",
            base__small: "ResultRewards_base__small_78",
            base__extraSmall: "ResultRewards_base__extraSmall_1c",
            base__animTitleAndRewards: "ResultRewards_base__animTitleAndRewards_02",
            ribbon: "ResultRewards_ribbon_67",
            rewards: "ResultRewards_rewards_b8",
          },
          Me = (0, n.memo)(({ doneValue: e, wasDone: u, animState: t, onAnimationCompete: s }) => {
            const r = x("model.rewards"),
              i = r.length > 0,
              o = e !== j.Undone,
              l = t > Z.Init,
              c = ((e, u) => {
                const t = (0, n.useState)(0),
                  a = t[0],
                  s = t[1];
                return (0, n.useCallback)(() => {
                  const t = a + 1;
                  (s(t), t === e && u && u());
                }, [a, s, e, u]);
              })(r.length, s),
              E = O(["base"], Pe),
              _ = Q(E.base, Pe, t);
            return (
              (0, n.useEffect)(() => {
                if (!i && s && l) {
                  const e = setTimeout(s, 1200);
                  return () => clearTimeout(e);
                }
              }, [l, i, s]),
              a().createElement(
                "div",
                { className: _ },
                i
                  ? a().createElement(
                      a().Fragment,
                      null,
                      a().createElement("div", { className: Pe.ribbon }),
                      a().createElement(
                        "div",
                        { className: Pe.rewards },
                        r.map(({ value: e }, u) =>
                          a().createElement(Se, {
                            key: `${u}_${e.name}_${e.value}`,
                            index: u,
                            image: pe(e, Ee.Big),
                            value: e.value,
                            tooltipId: e.tooltipId,
                            animState: t,
                            onAnimationCompete: c,
                          }),
                        ),
                      ),
                    )
                  : a().createElement(ke, { animState: t, doneValue: e, rewardGot: o, wasDone: u }),
              )
            );
          }),
          Oe = {
            base: "MapsTrainingResultApp_base_db",
            bg: "MapsTrainingResultApp_bg_20",
            bgFogging: "MapsTrainingResultApp_bgFogging_b9",
            bgShape: "MapsTrainingResultApp_bgShape_95",
            base__animTitleAndRewards: "MapsTrainingResultApp_base__animTitleAndRewards_d3",
            box: "MapsTrainingResultApp_box_f1",
            base__small: "MapsTrainingResultApp_base__small_ab",
            base__extraSmall: "MapsTrainingResultApp_base__extraSmall_52",
            mapTitle: "MapsTrainingResultApp_mapTitle_b8",
            titleWrapper: "MapsTrainingResultApp_titleWrapper_2c",
            titleBG: "MapsTrainingResultApp_titleBG_b7",
            title: "MapsTrainingResultApp_title_fd",
            close: "MapsTrainingResultApp_close_75",
            button: "MapsTrainingResultApp_button_b1",
          },
          Ne = R.strings.maps_training.result,
          Le = {
            [j.Undone]: Ne.title.lose(),
            [j.PartialDone]: Ne.title.partial(),
            [j.Done]: Ne.title.win(),
          },
          Ie = () => {
            const e = x("model"),
              u = e.mapID,
              t = e.mapName,
              s = e.selectedScenario,
              r = e.selectedVehicleType,
              i = e.doneValue,
              o = e.wasDone,
              l = e.hangarReady,
              c = e.rewards,
              E = e.onClose,
              _ = (0, n.useState)(Z.Init),
              A = _[0],
              F = _[1],
              d = i === j.Done,
              m = c.length > 0;
            (0, n.useEffect)(() => {
              A === Z.Init &&
                l &&
                (F(Z.TitleAndRewards),
                U(
                  d
                    ? R.sounds.gui_random_reward_red_ribbon_appear()
                    : R.sounds.gui_hangar_simple_execution_screen(),
                ));
            }, [A, l, d]);
            const D = (0, n.useCallback)(() => E(), [E]),
              B = (0, n.useCallback)(() => {
                (m || d
                  ? U(R.sounds.gui_random_reward_end())
                  : o && U(R.sounds.gui_random_reward_appear()),
                  F(Z.Done));
              }, [m, d, o]);
            I(N.n.ESCAPE, D);
            const g = (0, n.useMemo)(
                () =>
                  u ? { backgroundImage: `url(img://gui/maps/icons/map/screen/${u}.dds)` } : {},
                [u],
              ),
              C =
                ((p = Ne.mapName()),
                (h = { map: t, scenario: s, type: r }),
                p.replace(/\{\w+\}/g, (e) => String(h[e.slice(1, -1)])));
            var p, h;
            const w = O(["base"], Oe),
              b = Q(w.base, Oe, A);
            return a().createElement(
              "div",
              { className: b },
              a().createElement(
                "div",
                { className: Oe.close },
                a().createElement(X, {
                  caption: R.strings.menu.viewHeader.closeBtn.label(),
                  type: "close",
                  side: "right",
                  onClick: D,
                }),
              ),
              a().createElement(
                "div",
                { className: Oe.bg, style: g },
                a().createElement("div", { className: Oe.bgFogging }),
                d && a().createElement("div", { className: Oe.bgShape }),
              ),
              a().createElement(
                "div",
                { className: Oe.box },
                a().createElement("div", { className: Oe.mapTitle }, C),
                a().createElement(
                  "div",
                  { className: Oe.titleWrapper },
                  d && a().createElement("div", { className: Oe.titleBG }),
                  a().createElement("div", { className: Oe.title }, Le[i]),
                ),
                a().createElement(ie, { hasReward: m, animState: A }),
                a().createElement(Me, {
                  animState: A,
                  doneValue: i,
                  wasDone: o,
                  onAnimationCompete: B,
                }),
              ),
              a().createElement(
                Y,
                { type: G.primary, size: $.small, mixClass: Oe.button, onClick: D },
                R.strings.maps_training.result.submit(),
              ),
            );
          };
        engine.whenReady.then(() => {
          r().render(
            a().createElement(C, null, a().createElement(Ie, null)),
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
    (__webpack_require__.O = (e, u, t, n) => {
      if (!u) {
        var a = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, n] = deferred[o], s = !0, r = 0; r < u.length; r++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[r]))
              ? u.splice(r--, 1)
              : ((s = !1), n < a && (a = n));
          if (s) {
            deferred.splice(o--, 1);
            var i = t();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      n = n || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > n; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [u, t, n];
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
    (__webpack_require__.j = 349),
    (() => {
      var e = { 349: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            a,
            [s, r, i] = t,
            o = 0;
          if (s.some((u) => 0 !== e[u])) {
            for (n in r) __webpack_require__.o(r, n) && (__webpack_require__.m[n] = r[n]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < s.length; o++)
            ((a = s[o]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [453], () => __webpack_require__(637));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
