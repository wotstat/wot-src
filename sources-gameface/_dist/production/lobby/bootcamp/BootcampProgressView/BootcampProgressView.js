(() => {
  "use strict";
  var __webpack_modules__ = {
      67: (e, t, n) => {
        n.d(t, { O: () => q });
        var r = {};
        (n.r(r), n.d(r, { mouse: () => _, onResize: () => c }));
        var a = {};
        (n.r(a),
          n.d(a, {
            events: () => r,
            getMouseGlobalPosition: () => m,
            getSize: () => d,
            graphicsQuality: () => g,
          }));
        var o = {};
        (n.r(o), n.d(o, { getBgUrl: () => p, getTextureUrl: () => h }));
        var i = {};
        function s(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        function l(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        (n.r(i),
          n.d(i, {
            addModelObserver: () => M,
            addPreloadTexture: () => O,
            children: () => o,
            displayStatus: () => b,
            displayStatusIs: () => j,
            events: () => w,
            extraSize: () => G,
            forceTriggerMouseMove: () => V,
            freezeTextureBeforeResize: () => N,
            getBrowserTexturePath: () => x,
            getDisplayStatus: () => $,
            getScale: () => A,
            getSize: () => T,
            getViewGlobalPosition: () => B,
            isClientAccessible: () => W,
            isEventHandled: () => z,
            isFocused: () => H,
            pxToRem: () => D,
            remToPx: () => I,
            resize: () => R,
            sendEvent: () => C,
            setAnimateWindow: () => F,
            setEventHandled: () => U,
            setInputPaddingsRem: () => P,
            setSidePaddingsRem: () => L,
            whenTutorialReady: () => K,
          }));
        const c = s("clientResized"),
          u = { down: s("mousedown"), up: s("mouseup"), move: s("mousemove") };
        const _ = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && l(!1);
          }
          function n() {
            e.enabled && l(!0);
          }
          function r() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", n))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", n))
              : l(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (t, n) => (
              (t[n] = (function (t) {
                return (n) => {
                  e.listeners += 1;
                  let a = !0;
                  const o = `mouse${t}`,
                    i = u[t]((e) => n([e, "outside"]));
                  function s(e) {
                    n([e, "inside"]);
                  }
                  return (
                    window.addEventListener(o, s),
                    r(),
                    () => {
                      a &&
                        (i(), window.removeEventListener(o, s), (e.listeners -= 1), r(), (a = !1));
                    }
                  );
                };
              })(n)),
              t
            ),
            {},
          );
          return Object.assign({}, a, {
            disable() {
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
            },
            enableOutside() {
              e.enabled && l(!0);
            },
            disableOutside() {
              e.enabled && l(!1);
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
        const g = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function h(e, t, n = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, n);
        }
        function p(e, t, n) {
          return `url(${h(e, t, n)})`;
        }
        const b = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          w = {
            onTextureFrozen: s("self.onTextureFrozen"),
            onTextureReady: s("self.onTextureReady"),
            onDomBuilt: s("self.onDomBuilt"),
            onLoaded: s("self.onLoaded"),
            onDisplayChanged: s("self.onShowingStatusChanged"),
            onFocusUpdated: s("self.onFocusChanged"),
            children: {
              onAdded: s("children.onAdded"),
              onLoaded: s("children.onLoaded"),
              onRemoved: s("children.onRemoved"),
              onAttached: s("children.onAttached"),
              onTextureReady: s("children.onTextureReady"),
              onRequestPosition: s("children.requestPosition"),
            },
          },
          v = ["args"];
        const f = 2,
          E = 16,
          y = 32,
          S = 64,
          k = (e, t) => {
            const n = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var n,
                    r,
                    a = {},
                    o = Object.keys(e);
                  for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(t, v);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: n, type: e }, o, {
                      arguments:
                        ((r = a),
                        Object.entries(r).map(([e, t]) => {
                          const n = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: n, name: e, number: t };
                            case "boolean":
                              return { __Type: n, name: e, bool: t };
                            default:
                              return { __Type: n, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: n, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: n, type: e });
            var r;
          },
          C = {
            close(e) {
              k("popover" === e ? f : y);
            },
            minimize() {
              k(S);
            },
            move(e) {
              k(E, { isMouseEvent: !0, on: e });
            },
          };
        function O(e) {
          viewEnv.addPreloadTexture(e);
        }
        function P(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function x(e, t, n, r = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, n, r);
        }
        function M(e, t, n) {
          return viewEnv.addDataChangedCallback(e, t, n);
        }
        function L(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function T(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function R(e, t, n = "px") {
          return "rem" === n ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function B(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: I(t.x), y: I(t.y) };
        }
        function N() {
          viewEnv.freezeTextureBeforeResize();
        }
        function A() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function I(e) {
          return viewEnv.remToPx(e);
        }
        function F(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function H() {
          return viewEnv.isFocused();
        }
        function W() {
          return viewEnv.isClientAccessible();
        }
        function U() {
          return viewEnv.setEventHandled();
        }
        function z() {
          return viewEnv.isEventHandled();
        }
        function V() {
          viewEnv.forceTriggerMouseMove();
        }
        function $() {
          return viewEnv.getShowingStatus();
        }
        const j = Object.keys(b).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === b[t]), e),
            {},
          ),
          G = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          K = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : w.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          q = { view: i, client: a };
      },
      521: (e, t, n) => {
        let r, a;
        (n.d(t, { n: () => r }),
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
          })(a || (a = {})));
      },
      358: (e, t, n) => {
        n.d(t, { Z: () => o });
        var r = n(67);
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
          addCallback(e, t, n = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const o = r.O.view.addModelObserver(e, n, a);
            return (
              o > 0
                ? ((this._callbacks[o] = t),
                  n > 0 && (this._views[n] ? this._views[n].push(o) : (this._views[n] = [o])))
                : console.error("Can't add callback for model:", e),
              o
            );
          }
          removeCallback(e, t = 0) {
            let n = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((n = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              n || console.error("Can't remove callback by id:", e),
              n
            );
          }
          _emmitDataChanged(e, t, n) {
            n.forEach((n) => {
              const r = this._callbacks[n];
              void 0 !== r && r(e, t);
            });
          }
        }
        a.__instance = void 0;
        const o = a;
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
      364: (e, t, n) => {
        n.d(t, { Sw: () => o.Z, B0: () => l, ry: () => w, Sy: () => f });
        class r {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: n }) => {
                  let r = e.target;
                  do {
                    if (r === t) return;
                    r = r.parentNode;
                  } while (r);
                  n();
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
            const n = e,
              r = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== n || t !== r,
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
        const a = r;
        var o = n(358);
        const i = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          s = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, n) => userLocale.getTimeFormat(e, t, void 0 === n || n),
            getTimeString: (e, t, n) => userLocale.getTimeString(e, t, void 0 === n || n),
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
        const c = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          u = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = n(521),
          g = n(67);
        const h = ["args"];
        function p(e, t, n, r, a, o, i) {
          try {
            var s = e[o](i),
              l = s.value;
          } catch (e) {
            return void n(e);
          }
          s.done ? t(l) : Promise.resolve(l).then(r, a);
        }
        const b = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          w = (function () {
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
                    n = arguments;
                  return new Promise(function (r, a) {
                    var o = e.apply(t, n);
                    function i(e) {
                      p(o, r, a, i, s, "next", e);
                    }
                    function s(e) {
                      p(o, r, a, i, s, "throw", e);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          v = (e, t) => {
            const n = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var n,
                    r,
                    a = {},
                    o = Object.keys(e);
                  for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(t, h);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: n, type: e }, o, {
                      arguments:
                        ((r = a),
                        Object.entries(r).map(([e, t]) => {
                          const n = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              n.number = t;
                              break;
                            case "boolean":
                              n.bool = t;
                              break;
                            default:
                              n.string = t.toString();
                          }
                          return n;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: n, type: e }, o));
            } else viewEnv.handleViewEvent({ __Type: n, type: e });
            var r;
          },
          f = () => v(l.CLOSE),
          E = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var y = n(572);
        const S = a.instance,
          k = {
            DataTracker: o.Z,
            ViewModel: y.Z,
            ViewEventType: l,
            NumberFormatType: c,
            RealFormatType: u,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: b,
            sendMoveEvent: (e) => v(l.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: f,
            sendClosePopOverEvent: () => v(l.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, n = 0) => {
              v(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: n,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, n, r, a = R.invalid("resId"), o) => {
              const i = g.O.view.getViewGlobalPosition(),
                s = n.getBoundingClientRect(),
                c = s.x,
                u = s.y,
                _ = s.width,
                d = s.height,
                m = {
                  x: g.O.view.pxToRem(c) + i.x,
                  y: g.O.view.pxToRem(u) + i.y,
                  width: g.O.view.pxToRem(_),
                  height: g.O.view.pxToRem(d),
                };
              v(l.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: r || R.invalid("resId"),
                targetID: a,
                direction: t,
                bbox: b(m),
                on: !0,
                args: o,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => E(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              E(e, f);
            },
            handleViewEvent: v,
            onBindingsReady: w,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
            dumpViewModel: function e(t) {
              const n = {};
              if ("object" != typeof t) return t;
              for (const r in t)
                if (Object.prototype.hasOwnProperty.call(t, r)) {
                  const a = Object.prototype.toString.call(t[r]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = t[r];
                    n[r] = [];
                    for (let t = 0; t < a.length; t++) n[r].push({ value: e(a[t].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (n[r] = e(t[r]))
                      : (n[r] = t[r]);
                }
              return n;
            },
            ClickOutsideManager: S,
            SystemLocale: i,
            UserLocale: s,
          };
        window.ViewEnvHelper = k;
      },
      352: (e, t, n) => {
        var r = n(179),
          a = n.n(r),
          o = n(493),
          i = n.n(o);
        const s = (e, t, n) =>
          t.extraLargeHeight ||
          t.largeHeight ||
          t.mediumHeight ||
          t.smallHeight ||
          t.extraSmallHeight
            ? (t.extraLargeHeight && n.extraLarge) ||
              (t.largeHeight && n.large) ||
              (t.mediumHeight && n.medium) ||
              (t.smallHeight && n.small) ||
              (t.extraSmallHeight && n.extraSmall)
              ? e
              : null
            : e;
        var l = n(67);
        const c = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var u;
        function _(e, t, n) {
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
            })(e, n),
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
            })(t, n),
            o = Math.min(r, a);
          return {
            extraLarge: o === n.extraLarge.weight,
            large: o === n.large.weight,
            medium: o === n.medium.weight,
            small: o === n.small.weight,
            extraSmall: o === n.extraSmall.weight,
            extraLargeWidth: r === n.extraLarge.weight,
            largeWidth: r === n.large.weight,
            mediumWidth: r === n.medium.weight,
            smallWidth: r === n.small.weight,
            extraSmallWidth: r === n.extraSmall.weight,
            extraLargeHeight: a === n.extraLarge.weight,
            largeHeight: a === n.large.weight,
            mediumHeight: a === n.medium.weight,
            smallHeight: a === n.small.weight,
            extraSmallHeight: a === n.extraSmall.weight,
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
        })(u || (u = {}));
        const d = l.O.client.getSize("rem"),
          m = d.width,
          g = d.height,
          h = Object.assign({ width: m, height: g }, _(m, g, c)),
          p = (0, r.createContext)(h),
          b = ["children"];
        const w = (e) => {
          let t = e.children,
            n = (function (e, t) {
              if (null == e) return {};
              var n,
                r,
                a = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, b);
          const a = (0, r.useContext)(p),
            o = a.extraLarge,
            i = a.large,
            l = a.medium,
            c = a.small,
            u = a.extraSmall,
            _ = a.extraLargeWidth,
            d = a.largeWidth,
            m = a.mediumWidth,
            g = a.smallWidth,
            h = a.extraSmallWidth,
            w = a.extraLargeHeight,
            v = a.largeHeight,
            f = a.mediumHeight,
            E = a.smallHeight,
            y = a.extraSmallHeight,
            S = { extraLarge: w, large: v, medium: f, small: E, extraSmall: y };
          if (n.extraLarge || n.large || n.medium || n.small || n.extraSmall) {
            if (n.extraLarge && o) return t;
            if (n.large && i) return t;
            if (n.medium && l) return t;
            if (n.small && c) return t;
            if (n.extraSmall && u) return t;
          } else {
            if (n.extraLargeWidth && _) return s(t, n, S);
            if (n.largeWidth && d) return s(t, n, S);
            if (n.mediumWidth && m) return s(t, n, S);
            if (n.smallWidth && g) return s(t, n, S);
            if (n.extraSmallWidth && h) return s(t, n, S);
            if (!(
              n.extraLargeWidth ||
              n.largeWidth ||
              n.mediumWidth ||
              n.smallWidth ||
              n.extraSmallWidth
            )) {
              if (n.extraLargeHeight && w) return t;
              if (n.largeHeight && v) return t;
              if (n.mediumHeight && f) return t;
              if (n.smallHeight && E) return t;
              if (n.extraSmallHeight && y) return t;
            }
          }
          return null;
        };
        w.defaultProps = {
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
        (0, r.memo)(w);
        const v = (e) => {
            const t = (0, r.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          f = (0, r.memo)(({ children: e }) => {
            const t = (0, r.useContext)(p),
              n = (0, r.useState)(t),
              o = n[0],
              i = n[1],
              s = (0, r.useCallback)((e, t) => {
                const n = l.O.view.pxToRem(e),
                  r = l.O.view.pxToRem(t);
                i(Object.assign({ width: n, height: r }, _(n, r, c)));
              }, []);
            (v(() => {
              engine.on("clientResized", s);
            }),
              (0, r.useEffect)(() => () => engine.off("clientResized", s), [s]));
            const u = (0, r.useMemo)(() => Object.assign({}, o), [o]);
            return a().createElement(p.Provider, { value: u }, e);
          });
        var E = n(483),
          y = n.n(E),
          S = n(364),
          k = n(521);
        const C = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function O(e = k.n.NONE, t = C, n = !1) {
          (0, r.useEffect)(() => {
            if (e !== k.n.NONE)
              return (
                window.addEventListener("keydown", r, n),
                () => {
                  window.removeEventListener("keydown", r, n);
                }
              );
            function r(r) {
              if (r.keyCode === e) {
                if (l.O.view.isEventHandled()) return;
                (l.O.view.setEventHandled(), t(r), n && r.stopPropagation());
              }
            }
          }, [t, e, n]);
        }
        function P() {
          !(function (e = k.n.ESCAPE) {
            O(e, S.Sy, !0);
          })(k.n.ESCAPE);
        }
        function x(e) {
          engine.call("PlaySound", e);
        }
        const M = {
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
          L = [
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
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        class B extends a().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && x(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && x(this.props.soundClick));
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
              n = e.onClick,
              r = e.goto,
              o = e.side,
              i = e.type,
              s = e.classNames,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              u = e.onMouseDown,
              _ = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var n,
                    r,
                    a = {},
                    o = Object.keys(e);
                  for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(e, L)),
              m = y()(M.base, M[`base__${i}`], M[`base__${o}`], null == s ? void 0 : s.base),
              g = y()(M.icon, M[`icon__${i}`], M[`icon__${o}`], null == s ? void 0 : s.icon),
              h = y()(M.glow, null == s ? void 0 : s.glow),
              p = y()(M.caption, M[`caption__${i}`], null == s ? void 0 : s.caption),
              b = y()(M.goto, null == s ? void 0 : s.goto);
            return a().createElement(
              "div",
              T(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(l),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(u),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: n,
                },
                d,
              ),
              "info" !== i && a().createElement("div", { className: M.shine }),
              a().createElement(
                "div",
                { className: g },
                a().createElement("div", { className: h }),
              ),
              a().createElement("div", { className: p }, t),
              r && a().createElement("div", { className: b }, r),
            );
          }
        }
        B.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const N = {
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
        let A, D;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(A || (A = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(D || (D = {})));
        const I = ({
          children: e,
          size: t,
          isFocused: n,
          type: o,
          disabled: i,
          mixClass: s,
          soundHover: l,
          soundClick: c,
          onMouseEnter: u,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: g,
          onClick: h,
        }) => {
          const p = (0, r.useRef)(null),
            b = (0, r.useState)(n),
            w = b[0],
            v = b[1],
            f = (0, r.useState)(!1),
            E = f[0],
            S = f[1],
            k = (0, r.useState)(!1),
            C = k[0],
            O = k[1],
            P = (0, r.useCallback)(() => {
              i || (p.current && (p.current.focus(), v(!0)));
            }, [i]),
            M = (0, r.useCallback)(
              (e) => {
                w && null !== p.current && !p.current.contains(e.target) && v(!1);
              },
              [w],
            ),
            L = (0, r.useCallback)(
              (e) => {
                i || (h && h(e));
              },
              [i, h],
            ),
            T = (0, r.useCallback)(
              (e) => {
                i || (null !== l && x(l), u && u(e), O(!0));
              },
              [i, l, u],
            ),
            B = (0, r.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            D = (0, r.useCallback)(
              (e) => {
                i || (m && m(e), S(!1));
              },
              [i, m],
            ),
            I = (0, r.useCallback)(
              (e) => {
                i || (null !== c && x(c), d && d(e), n && P(), S(!0));
              },
              [i, c, d, P, n],
            ),
            F = (0, r.useCallback)(
              (e) => {
                i || (g && g(e), S(!1));
              },
              [i, g],
            ),
            H = y()(
              N.base,
              N[`base__${o}`],
              {
                [N.base__disabled]: i,
                [N[`base__${t}`]]: t,
                [N.base__focus]: w,
                [N.base__highlightActive]: E,
                [N.base__firstHover]: C,
              },
              s,
            ),
            W = y()(N.state, N.state__default);
          return (
            (0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", M),
                () => {
                  document.removeEventListener("mousedown", M);
                }
              ),
              [M],
            ),
            (0, r.useEffect)(() => {
              v(n);
            }, [n]),
            a().createElement(
              "div",
              {
                ref: p,
                className: H,
                onMouseEnter: T,
                onMouseMove: B,
                onMouseUp: D,
                onMouseDown: I,
                onMouseLeave: F,
                onClick: L,
              },
              o !== A.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: N.back }),
                  a().createElement("span", { className: N.texture }),
                ),
              a().createElement(
                "span",
                { className: W },
                a().createElement("span", { className: N.stateDisabled }),
                a().createElement("span", { className: N.stateHighlightHover }),
                a().createElement("span", { className: N.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: N.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        I.defaultProps = {
          type: A.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const F = (0, r.memo)(I);
        let H, W, U;
        (!(function (e) {
          e.Bootcamp = "bootcamp";
        })(H || (H = {})),
          (function (e) {
            ((e.BC_DEVICE_SETUP_SUB_VIEW = "bc_device_setup_sub_view"),
              (e.BC_CONSUMABLE_SETUP_SUB_VIEW = "bc_consumable_setup_sub_view"),
              (e.BC_EXIT_VIEW = "bc_exit_view"),
              (e.BC_CURRENT_PROGRESS_WIDGET = "bc_current_progress_widget"),
              (e.BC_RESULT_SCREEN = "bc_result_screen"));
          })(W || (W = {})),
          (function (e) {
            e.TooltipOpened = "tooltip_opened";
          })(U || (U = {})));
        const z = (e = 1) => {
            const t = new Error().stack;
            let n,
              r = R.invalid("resId");
            return (
              t &&
                ((n = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                window.__feature &&
                  window.__feature !== n &&
                  window.subViews[n] &&
                  (r = window.subViews[n].id)),
              { caller: n, stack: t, resId: r }
            );
          },
          V = (e, t) => e.split(".").reduce((e, t) => e && e[t], t),
          $ = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          j = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          G = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, n) => {
                const r = V(`${e}.${n}`, window);
                return $(r) ? t(e, n, r) : `${e}.${n}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          K = (e) => {
            const t = ((e) => {
                const t = z(),
                  n = t.caller,
                  r = t.resId,
                  a = window.__feature && window.__feature !== n && n ? `subViews.${n}` : "";
                return { modelPrefix: a, modelPath: j(a, e || ""), resId: r };
              })(),
              n = t.modelPrefix,
              r = e.split(".");
            if (r.length > 0) {
              const e = [r[0]];
              return (
                r.reduce((t, r) => {
                  const a = V(j(n, `${t}.${r}`), window);
                  return $(a) ? (e.push(a.id), `${t}.${r}.value`) : (e.push(r), `${t}.${r}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          q = S.Sw.instance;
        let Y;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Y || (Y = {}));
        const X = (e = "model", t = Y.Deep) => {
            const n = (0, r.useState)(0),
              a = (n[0], n[1]),
              o = (0, r.useMemo)(() => z(), []),
              i = o.caller,
              s = o.resId,
              l = (0, r.useMemo)(
                () => (window.__feature && window.__feature !== i ? `subViews.${i}.${e}` : e),
                [i, e],
              ),
              c = (0, r.useState)(() =>
                ((e) => {
                  const t = V(e, window);
                  for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                  return $(t) ? t.value : t;
                })(G(l)),
              ),
              u = c[0],
              _ = c[1],
              d = (0, r.useRef)(-1);
            return (
              v(() => {
                if (
                  ("boolean" == typeof t &&
                    ((t = t ? Y.Deep : Y.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  t !== Y.None)
                ) {
                  const n = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      t === Y.Deep
                        ? (e === u && a((e) => e + 1), _(e))
                        : _(Object.assign([], e));
                    },
                    r = K(e);
                  d.current = q.addCallback(r, n, s, t === Y.Deep);
                }
              }),
              (0, r.useEffect)(() => {
                if (t !== Y.None)
                  return () => {
                    q.removeCallback(d.current, s);
                  };
              }, [s, t]),
              u
            );
          },
          Z = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let Q, J;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(Q || (Q = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(J || (J = {})));
        const ee = ({ size: e = Q.Default, classMix: t }) =>
            a().createElement("div", { className: y()(Z.background, Z[`background__${e}`], t) }),
          te = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          ne = ({ size: e }) => {
            const t = y()(te.base, te[`base__${e}`]);
            return a().createElement("div", { className: t });
          },
          re = {
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
          ae = (0, r.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: n,
              baseStyles: r,
              isComplete: o,
              withoutBounce: i,
            }) => {
              const s = y()(
                  re.base,
                  re[`base__${e}`],
                  n && re.base__disabled,
                  o && re.base__finished,
                  i && re.base__withoutBounce,
                ),
                l = !n && !o;
              return a().createElement(
                "div",
                { className: s, style: r, ref: t },
                a().createElement("div", { className: re.pattern }),
                a().createElement("div", { className: re.gradient }),
                l && a().createElement(ne, { size: e }),
              );
            },
          ),
          oe = ({ size: e, value: t, lineRef: n, disabled: o, onComplete: i }) => {
            const s = (0, r.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              l = 100 === t;
            return (
              (0, r.useEffect)(() => {
                l && i && i();
              }, [l, i]),
              a().createElement(ae, {
                size: e,
                disabled: o,
                baseStyles: s,
                isComplete: l,
                lineRef: n,
              })
            );
          },
          ie = (e, t) => {
            let n;
            const r = setTimeout(() => {
              n = e();
            }, t);
            return () => {
              ("function" == typeof n && n(), clearTimeout(r));
            };
          };
        let se, le;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(se || (se = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(le || (le = {})));
        const ce = "ProgressBarDeltaSimple_base_6c",
          ue = "ProgressBarDeltaSimple_delta_99",
          _e = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: n,
              from: o,
              size: i,
              to: s,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const u = s < o,
                _ = (0, r.useState)(le.Idle),
                d = _[0],
                m = _[1],
                g = d === le.In,
                h = d === le.End,
                p = d === le.Idle,
                b = (0, r.useCallback)(
                  (e) => {
                    (m(e), c && c(e));
                  },
                  [c],
                );
              ((0, r.useEffect)(() => {
                if (p && !n) {
                  return ie(() => {
                    b(le.In);
                  }, t);
                }
              }, [b, n, p, t]),
                (0, r.useEffect)(() => {
                  if (g) {
                    return ie(() => {
                      (l && l(), b(le.End));
                    }, e + t);
                  }
                }, [b, g, l, t, e]));
              const w = (0, r.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [u ? "left" : "right"]: "0",
                  }),
                  [u, t, e],
                ),
                v = (0, r.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [u ? "left" : "right"]: "0",
                  }),
                  [u, t, e],
                ),
                f = (0, r.useMemo)(
                  () => ({ width: `${Math.abs(o - s)}%`, left: `${u ? s : o}%` }),
                  [o, u, s],
                );
              return h
                ? null
                : a().createElement(
                    "div",
                    { className: ce, style: f },
                    a().createElement(
                      "div",
                      { style: p ? w : v, className: ue },
                      a().createElement(ne, { size: i }),
                    ),
                  );
            },
          ),
          de = (0, r.memo)(
            ({
              to: e,
              size: t,
              from: n,
              lineRef: o,
              disabled: i,
              isComplete: s,
              animationSettings: l,
              onChangeAnimationState: c,
              onEndAnimation: u,
            }) => {
              const _ = (0, r.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${l.line.duration}ms`,
                  transitionDelay: `${l.line.delay}ms`,
                }),
                [l.line.delay, l.line.duration, e],
              );
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(ae, {
                  size: t,
                  lineRef: o,
                  disabled: i,
                  isComplete: s,
                  baseStyles: _,
                }),
                n >= 0 &&
                  a().createElement(_e, {
                    transitionDuration: l.delta.duration,
                    transitionDelay: l.delta.delay,
                    freezed: l.freezed,
                    from: n,
                    size: t,
                    to: e,
                    onChangeAnimationState: c,
                    onEndAnimation: u,
                  }),
              );
            },
          ),
          me = "ProgressBarDeltaGrow_base_7e",
          ge = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          he = "ProgressBarDeltaGrow_glow_68",
          pe = (e) => (e ? { left: 0 } : { right: 0 }),
          be = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          we = (e) => ({ transitionDuration: `${e}ms` }),
          ve = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: n,
              from: o,
              size: i,
              to: s,
              onEndAnimation: l,
              onChangeAnimationState: c,
              className: u,
            }) => {
              const _ = s < o,
                d = (0, r.useState)(se.Idle),
                m = d[0],
                g = d[1],
                h = m === se.End,
                p = m === se.Idle,
                b = m === se.Grow,
                w = m === se.Shrink,
                v = (0, r.useCallback)(
                  (e) => {
                    (g(e), c && c(e));
                  },
                  [c],
                ),
                f = (0, r.useCallback)(
                  (e, t) =>
                    ie(() => {
                      v(e);
                    }, t),
                  [v],
                );
              (0, r.useEffect)(() => {
                if (!n)
                  return p
                    ? f(se.Grow, t)
                    : b
                      ? f(se.Shrink, e)
                      : w
                        ? f(se.End, e)
                        : void (h && l && l());
              }, [f, n, h, b, p, w, l, t, e]);
              const E = (0, r.useMemo)(
                  () => Object.assign({ width: "100%" }, we(e), pe(_)),
                  [_, e],
                ),
                S = (0, r.useMemo)(() => Object.assign({ width: "0%" }, we(e), pe(_)), [_, e]),
                k = (0, r.useMemo)(
                  () => Object.assign({ width: "0%" }, be(_, o), we(e)),
                  [o, _, e],
                ),
                C = (0, r.useMemo)(
                  () => Object.assign({ width: `${Math.abs(s - o)}%` }, be(_, o), we(e)),
                  [o, _, s, e],
                );
              if (h) return null;
              const O = y()(me, u, _ && 0 === s && ge);
              return a().createElement(
                "div",
                { style: p ? k : C, className: O },
                a().createElement(
                  "div",
                  { style: w ? S : E, className: he },
                  a().createElement(ne, { size: i }),
                ),
              );
            },
          ),
          fe = (0, r.memo)(
            ({
              to: e,
              size: t,
              from: n,
              lineRef: o,
              disabled: i,
              isComplete: s,
              animationSettings: l,
              onEndAnimation: c,
              onChangeAnimationState: u,
            }) => {
              const _ = e < n,
                d = (0, r.useState)(!1),
                m = d[0],
                g = d[1],
                h = (0, r.useCallback)(
                  (e) => {
                    (e === se.Shrink && g(!0), u && u(e));
                  },
                  [u],
                ),
                p = (0, r.useMemo)(() => ({ width: `${n}%`, transitionProperty: "none" }), [n]),
                b = (0, r.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${l.line.duration}ms` }),
                  [l.line.duration, e],
                );
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(ae, {
                  size: t,
                  lineRef: o,
                  disabled: i,
                  isComplete: s,
                  withoutBounce: _ && 0 === e,
                  baseStyles: m ? b : p,
                }),
                n >= 0 &&
                  a().createElement(ve, {
                    transitionDuration: l.delta.duration,
                    transitionDelay: l.delta.delay,
                    onChangeAnimationState: h,
                    freezed: l.freezed,
                    onEndAnimation: c,
                    from: n,
                    size: t,
                    to: e,
                    className: l.delta.className,
                  }),
              );
            },
          ),
          Ee = ["onComplete", "onEndAnimation"];
        function ye() {
          return (
            (ye =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r]);
                }
                return e;
              }),
            ye.apply(this, arguments)
          );
        }
        const Se = (0, r.memo)((e) => {
            let t = e.onComplete,
              n = e.onEndAnimation,
              o = (function (e, t) {
                if (null == e) return {};
                var n,
                  r,
                  a = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, Ee);
            const i = (0, r.useState)(!1),
              s = i[0],
              l = i[1],
              c = (0, r.useCallback)(() => {
                const e = 100 === o.to;
                (e !== s && l(e), e && t && t(), n && n());
              }, [s, t, n, o.to]);
            switch (o.animationSettings.type) {
              case J.Simple:
                return a().createElement(de, ye({}, o, { onEndAnimation: c, isComplete: s }));
              case J.Growing:
                return a().createElement(fe, ye({}, o, { onEndAnimation: c, isComplete: s }));
              default:
                return null;
            }
          }),
          ke = ["onEndAnimation"];
        function Ce() {
          return (
            (Ce =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r]);
                }
                return e;
              }),
            Ce.apply(this, arguments)
          );
        }
        const Oe = (0, r.memo)((e) => {
          let t = e.onEndAnimation,
            n = (function (e, t) {
              if (null == e) return {};
              var n,
                r,
                a = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, ke);
          const o = (0, r.useRef)({}),
            i = (0, r.useCallback)(() => {
              ((o.current.from = void 0), t && t());
            }, [t]),
            s = "number" == typeof o.current.from ? o.current.from : n.from;
          return (
            (o.current.from = s),
            a().createElement(Se, Ce({}, n, { onEndAnimation: i, key: `${s}-${n.to}`, from: s }))
          );
        });
        function Pe() {
          return (
            (Pe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r]);
                }
                return e;
              }),
            Pe.apply(this, arguments)
          );
        }
        const xe = (0, r.memo)(
            ({
              size: e,
              value: t,
              lineRef: n,
              disabled: r,
              deltaFrom: o,
              animationSettings: i,
              onEndAnimation: s,
              onChangeAnimationState: l,
              onComplete: c,
            }) => {
              if (o === t)
                return a().createElement(oe, {
                  key: `${o}-${t}`,
                  size: e,
                  value: t,
                  lineRef: n,
                  disabled: r,
                  onComplete: c,
                });
              const u = {
                from: o,
                to: t,
                size: e,
                lineRef: n,
                disabled: r,
                animationSettings: i,
                onComplete: c,
                onEndAnimation: s,
                onChangeAnimationState: l,
              };
              return i.withStack
                ? a().createElement(Oe, u)
                : a().createElement(Se, Pe({ key: `${o}-${t}` }, u));
            },
          ),
          Me = (e) => ({
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
          Le = (e, t, n) => (n < e ? e : n > t ? t : n),
          Te = (e, t, n) => {
            if ("number" == typeof n) {
              return (Le(0, t, n) / t) * 100;
            }
            return e;
          },
          Re = {
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
          Be = {
            freezed: !1,
            withStack: !1,
            type: J.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          Ne = (0, r.memo)(
            ({
              maxValue: e = 100,
              theme: t = Re,
              size: n = Q.Default,
              animationSettings: o = Be,
              disabled: i = !1,
              withoutBackground: s = !1,
              progressBarBackgroundClassMix: l,
              value: c,
              deltaFrom: u,
              lineRef: _,
              onChangeAnimationState: d,
              onEndAnimation: m,
              onComplete: g,
            }) => {
              const h = ((e, t, n) =>
                (0, r.useMemo)(() => {
                  const r = (Le(0, t, e) / t) * 100;
                  return { value: r, deltaFrom: Te(r, t, n) };
                }, [n, t, e]))(c, e, u);
              return a().createElement(
                "div",
                { className: y()(Z.base, Z[`base__${n}`]), style: Me(t) },
                !s && a().createElement(ee, { size: n, classMix: l }),
                a().createElement(xe, {
                  size: n,
                  lineRef: _,
                  disabled: i,
                  value: h.value,
                  deltaFrom: h.deltaFrom,
                  animationSettings: o,
                  onEndAnimation: m,
                  onChangeAnimationState: d,
                  onComplete: g,
                }),
              );
            },
          );
        let Ae;
        !(function (e) {
          ((e[(e.NonSet = 0)] = "NonSet"),
            (e[(e.Debug = 10)] = "Debug"),
            (e[(e.Info = 20)] = "Info"),
            (e[(e.Warning = 30)] = "Warning"));
        })(Ae || (Ae = {}));
        let De;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(De || (De = {}));
        const Ie = () => Date.now(),
          Fe = (e, t) => {
            const n = (0, r.useCallback)(
              (n, r = Ae.Info, a) => {
                (a || (a = {}),
                  Object.keys(a).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: t,
                      action: n,
                      logLevel: r,
                      params: JSON.stringify(a),
                    }));
              },
              [e, t],
            );
            return (e, t, r) => n(e, t, r);
          },
          He = (e, t) => {
            const n = Fe(e, t),
              a = (0, r.useRef)(new Map()),
              o = (0, r.useRef)(new Map()),
              i = (0, r.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  (void 0 !== t && t > 0) || a.current.set(e, Ie());
                },
                [a],
              ),
              s = (0, r.useCallback)(() => {
                (a.current.clear(), o.current.clear());
              }, [a, o]),
              l = (0, r.useCallback)(
                (e) => {
                  e &&
                    void 0 !== a.current.get(e) &&
                    void 0 === o.current.get(e) &&
                    o.current.set(e, Ie());
                },
                [a, o],
              ),
              c = (0, r.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  if (void 0 === t) return;
                  const n = o.current.get(e);
                  if (void 0 === n) return;
                  o.current.delete(e);
                  const r = Ie() - n;
                  a.current.set(e, t + r);
                },
                [a, o],
              ),
              u = (0, r.useCallback)(
                (e, t = 0, r, i) => {
                  const s = a.current.get(e);
                  if (void 0 === s) return;
                  (void 0 !== o.current.get(e) && c(e), a.current.delete(e));
                  const l = (Ie() - s) / 1e3;
                  l <= t ||
                    ((i = ((e, t) => (void 0 === e && (e = {}), (e.timeSpent = t), e))(i, l)),
                    n(e, r, i));
                },
                [a, o, n, c],
              );
            return [
              (e) => i(e),
              (e, t, n, r) => u(e, t, n, r),
              () => s(),
              (e) => l(e),
              (e) => c(e),
            ];
          },
          We = (e, t) => {
            const n = He(e, t),
              r = n[0],
              a = n[1],
              o = n[2],
              i = n[3],
              s = n[4];
            return [
              (e) => r(e),
              (e, t, n, r) => a(e, t, n, r),
              () => o(),
              (e) => i(e),
              (e) => s(e),
            ];
          },
          Ue = [
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
            "onShow",
            "onHide",
          ];
        function ze(e) {
          return Object.entries(e || {}).map(([e, t]) => {
            const n = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                n.number = t;
                break;
              case "boolean":
                n.bool = t;
                break;
              case "undefined":
                break;
              default:
                n.string = t.toString();
            }
            return n;
          });
        }
        const Ve = (e, t, n = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: S.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: r,
                },
                n,
              ),
            );
          },
          $e = (e) => {
            let t = e.children,
              n = e.contentId,
              a = e.args,
              o = e.onMouseEnter,
              i = e.onMouseLeave,
              s = e.onMouseDown,
              l = e.onClick,
              c = e.ignoreShowDelay,
              u = void 0 !== c && c,
              _ = e.ignoreMouseClick,
              d = void 0 !== _ && _,
              m = e.decoratorId,
              g = void 0 === m ? 0 : m,
              h = e.isEnabled,
              p = void 0 === h || h,
              b = e.onShow,
              w = e.onHide,
              v = (function (e, t) {
                if (null == e) return {};
                var n,
                  r,
                  a = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, Ue);
            const f = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              E = (0, r.useMemo)(() => z(), []).resId,
              y = (0, r.useCallback)(() => {
                (f.current.isVisible && f.current.timeoutId) ||
                  (Ve(n, g, { isMouseEvent: !0, on: !0, arguments: ze(a) }, E),
                  b && b(),
                  (f.current.isVisible = !0));
              }, [n, g, a, E, b]),
              S = (0, r.useCallback)(() => {
                if (f.current.isVisible || f.current.timeoutId) {
                  const e = f.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (f.current.timeoutId = 0)),
                    Ve(n, g, { on: !1 }, E),
                    f.current.isVisible && w && w(),
                    (f.current.isVisible = !1));
                }
              }, [n, g, E, w]),
              k = (0, r.useCallback)((e) => {
                f.current.isVisible &&
                  ((f.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (f.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(f.current.prevTarget) && S();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = f.current.hideTimerId;
              return (
                document.addEventListener("wheel", k, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", k, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", S),
                  () => {
                    (window.removeEventListener("mouseleave", S), S());
                  }
                ),
                [S],
              ));
            return p
              ? (0, r.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((C = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((f.current.timeoutId = window.setTimeout(y, u ? 100 : 400)),
                            o && o(e),
                            C && C(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (S(), i && i(t), e && e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!d && S(), l && l(t), e && e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!d && S(), s && s(t), e && e(t));
                      })(t.props.onMouseDown),
                    },
                    v,
                  ),
                )
              : t;
            var C;
          },
          je = ["children"];
        function Ge() {
          return (
            (Ge =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r]);
                }
                return e;
              }),
            Ge.apply(this, arguments)
          );
        }
        const Ke = (e) => {
            let t = e.children,
              n = (function (e, t) {
                if (null == e) return {};
                var n,
                  r,
                  a = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((n = o[r]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, je);
            return a().createElement(
              $e,
              Ge(
                {
                  contentId:
                    R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                      "resId",
                    ),
                  ignoreShowDelay: !0,
                },
                n,
              ),
              t,
            );
          },
          qe = {
            base: "Level_base_9f",
            base__medium: "Level_base__medium_6a",
            base__large: "Level_base__large_ec",
            progressBarOverlay: "Level_progressBarOverlay_39",
            lesson: "Level_lesson_74",
            lesson__current: "Level_lesson__current_dd",
            separator: "Level_separator_34",
            separator__first: "Level_separator__first_8c",
            done: "Level_done_93",
            glow: "Level_glow_aa",
            flare: "Level_flare_b5",
          },
          Ye = (0, r.memo)(
            ({
              size: e,
              isFirst: t,
              lessonNumber: n,
              completed: o,
              current: i,
              tooltipId: s,
              loggerGroup: l,
            }) => {
              const c = We(H.Bootcamp, l),
                u = c[0],
                _ = c[1],
                d = (0, r.useRef)(!1),
                m = (0, r.useCallback)(() => {
                  ((d.current = !1), u(U.TooltipOpened));
                }, [u]),
                g = (0, r.useCallback)(() => {
                  d.current || _(U.TooltipOpened, 2, Ae.Info, { tooltip: `level_${n}` });
                }, [_, n, d]),
                h = (0, r.useMemo)(() => ({ tooltipId: s }), [s]),
                p = y()(qe.lesson, i && qe.lesson__current),
                b = y()(qe.separator, qe.separator__first),
                w = y()(qe.base, qe[`base__${e}`]);
              return a().createElement(
                "div",
                { className: w },
                a().createElement(
                  Ke,
                  { args: h, onShow: m, onHide: g },
                  a().createElement(
                    "div",
                    { className: qe.progressBarOverlay },
                    a().createElement("div", { className: qe.separator }),
                    i && a().createElement("div", { className: qe.flare }),
                    t && a().createElement("div", { className: b }),
                    !o && a().createElement("div", { className: p }, n),
                    o &&
                      a().createElement(
                        a().Fragment,
                        null,
                        e !== lt.Small && a().createElement("div", { className: qe.glow }),
                        a().createElement("div", { className: qe.done }),
                      ),
                  ),
                ),
              );
            },
          ),
          Xe = "BootcampProgress_base_67",
          Ze = "BootcampProgress_icon_77",
          Qe = "BootcampProgress_icon__small_7a",
          Je = "BootcampProgress_icon__medium_1a",
          et = "BootcampProgress_icon__large_1b",
          tt = "BootcampProgress_status_2a",
          nt = "BootcampProgress_container_57",
          rt = "BootcampProgress_container__medium_26",
          at = "BootcampProgress_container__large_84",
          ot = "BootcampProgress_progressionBar_d5",
          it = "BootcampProgress_progressionBar__large_84";
        function st() {
          return (
            (st =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var r in n) Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r]);
                }
                return e;
              }),
            st.apply(this, arguments)
          );
        }
        let lt;
        !(function (e) {
          ((e.Large = "large"), (e.Medium = "medium"), (e.Small = "small"));
        })(lt || (lt = {}));
        const ct = (0, r.memo)(({ iconSize: e, progressSize: t, loggerGroup: n }) => {
            const o = X("model"),
              i = o.currentLesson,
              s = o.totalLessons,
              l = o.isNeedAwarding,
              c = X("model.levels"),
              u = We(H.Bootcamp, n),
              _ = u[0],
              d = u[1],
              m = (0, r.useRef)(!1),
              g = (0, r.useCallback)(() => {
                ((m.current = !0), _(U.TooltipOpened));
              }, [_]),
              h = (0, r.useCallback)(() => {
                m.current && d(U.TooltipOpened, 2, Ae.Info);
              }, [d, m]),
              p = (0, r.useCallback)(
                () => () => {
                  h();
                },
                [h],
              ),
              b = e === lt.Medium,
              w = e === lt.Large,
              v = y()(Ze, !l && Qe, b && Je, w && et),
              f = y()(nt, b && rt, w && at),
              E = t !== lt.Small,
              S = y()(ot, E && it);
            return a().createElement(
              "div",
              { className: Xe },
              a().createElement(
                $e,
                { onShow: g, onHide: p, contentId: R.views.lobby.bootcamp.RewardsTooltip("resId") },
                a().createElement("div", { className: v }),
              ),
              !l &&
                a().createElement(
                  "div",
                  { className: tt },
                  R.strings.bootcamp.tooltip.progression.status.got(),
                ),
              a().createElement(
                "div",
                { className: f },
                a().createElement(
                  "div",
                  { className: S },
                  a().createElement(Ne, { value: i, maxValue: s }),
                ),
                c.map(({ value: e }, r) =>
                  a().createElement(
                    Ye,
                    st({ key: `level${r}`, size: t, isFirst: 0 === r, loggerGroup: n }, e),
                  ),
                ),
              ),
            );
          }),
          ut = "BootcampProgressViewApp_base_78",
          _t = "BootcampProgressViewApp_close_29",
          dt = "BootcampProgressViewApp_content_32",
          mt = "BootcampProgressViewApp_header_8a",
          gt = "BootcampProgressViewApp_description_65",
          ht = "BootcampProgressViewApp_description__small_35",
          pt = "BootcampProgressViewApp_shine_fa",
          bt = "BootcampProgressViewApp_shine__small_61",
          wt = "BootcampProgressViewApp_progress_b1",
          vt = () => {
            P();
            const e = (0, r.useContext)(p),
              t = (0, r.useMemo)(() => (e.extraSmall ? lt.Medium : lt.Large), [e]),
              n = y()(gt, e.extraSmall && ht),
              o = y()(pt, e.extraSmall && bt);
            return a().createElement(
              "div",
              { className: ut },
              a().createElement("div", { className: o }),
              a().createElement(
                "div",
                { className: _t },
                a().createElement(B, {
                  caption: R.strings.menu.viewHeader.closeBtn.label(),
                  type: "close",
                  side: "right",
                  onClick: S.Sy,
                }),
              ),
              a().createElement(
                "div",
                { className: dt },
                a().createElement(
                  "div",
                  { className: mt },
                  R.strings.bootcamp.progress.window.title(),
                ),
                a().createElement(
                  "div",
                  { className: n },
                  R.strings.bootcamp.progress.window.description(),
                ),
                a().createElement(
                  "div",
                  { className: wt },
                  a().createElement(ct, {
                    iconSize: lt.Large,
                    progressSize: t,
                    loggerGroup: W.BC_CURRENT_PROGRESS_WIDGET,
                  }),
                ),
                a().createElement(
                  F,
                  { type: A.primary, size: D.medium, onClick: S.Sy },
                  R.strings.bootcamp.progress.window.exit(),
                ),
              ),
            );
          };
        engine.whenReady.then(() => {
          i().render(
            a().createElement(f, null, a().createElement(vt, null)),
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
    var n = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](n, n.exports, __webpack_require__), n.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, n, r) => {
      if (!t) {
        var a = 1 / 0;
        for (l = 0; l < deferred.length; l++) {
          for (var [t, n, r] = deferred[l], o = !0, i = 0; i < t.length; i++)
            (!1 & r || a >= r) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[i]))
              ? t.splice(i--, 1)
              : ((o = !1), r < a && (a = r));
          if (o) {
            deferred.splice(l--, 1);
            var s = n();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      r = r || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > r; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [t, n, r];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var n in t)
        __webpack_require__.o(t, n) &&
          !__webpack_require__.o(e, n) &&
          Object.defineProperty(e, n, { enumerable: !0, get: t[n] });
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
    (__webpack_require__.j = 520),
    (() => {
      var e = { 520: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, n) => {
          var r,
            a,
            [o, i, s] = n,
            l = 0;
          if (o.some((t) => 0 !== e[t])) {
            for (r in i) __webpack_require__.o(i, r) && (__webpack_require__.m[r] = i[r]);
            if (s) var c = s(__webpack_require__);
          }
          for (t && t(n); l < o.length; l++)
            ((a = o[l]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(c);
        },
        n = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (n.forEach(t.bind(null, 0)), (n.push = t.bind(null, n.push.bind(n))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [172], () => __webpack_require__(352));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
