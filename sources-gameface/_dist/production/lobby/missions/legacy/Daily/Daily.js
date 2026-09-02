(() => {
  var __webpack_modules__ = {
      875: (e, u, t) => {
        "use strict";
        t.d(u, { ko: () => z, uu: () => W });
        var n = t(483),
          a = t.n(n),
          r = t(179),
          s = t.n(r);
        const i = {
          base: "ProgressBar_base_45",
          base__medium: "ProgressBar_base__medium_62",
          base__small: "ProgressBar_base__small_df",
          background: "ProgressBar_background_51",
          background__medium: "ProgressBar_background__medium_6e",
          background__small: "ProgressBar_background__small_46",
          lineWrapper: "ProgressBar_lineWrapper_6a",
        };
        var o = t(736);
        const l = ({ size: e = o.$.Default, classMix: u }) =>
            s().createElement("div", { className: a()(i.background, i[`background__${e}`], u) }),
          c = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          d = ({ size: e }) => {
            const u = a()(c.base, c[`base__${e}`]);
            return s().createElement("div", { className: u });
          },
          m = {
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
          E = (0, r.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: n,
              isComplete: r,
              withoutBounce: i,
            }) => {
              const o = a()(
                  m.base,
                  m[`base__${e}`],
                  t && m.base__disabled,
                  r && m.base__finished,
                  i && m.base__withoutBounce,
                ),
                l = !t && !r;
              return s().createElement(
                "div",
                { className: o, style: n, ref: u },
                s().createElement("div", { className: m.pattern }),
                s().createElement("div", { className: m.gradient }),
                l && s().createElement(d, { size: e }),
              );
            },
          ),
          _ = ({ size: e, value: u, lineRef: t, disabled: n, onComplete: a }) => {
            const i = (0, r.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              o = 100 === u;
            return (
              (0, r.useEffect)(() => {
                o && a && a();
              }, [o, a]),
              s().createElement(E, {
                size: e,
                disabled: n,
                baseStyles: i,
                isComplete: o,
                lineRef: t,
              })
            );
          };
        var A = t(122);
        let g, F;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(g || (g = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(F || (F = {})));
        const D = "ProgressBarDeltaSimple_base_6c",
          p = "ProgressBarDeltaSimple_delta_99",
          C = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: n,
              size: a,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
            }) => {
              const c = i < n,
                m = (0, r.useState)(F.Idle),
                E = m[0],
                _ = m[1],
                g = E === F.In,
                C = E === F.End,
                B = E === F.Idle,
                b = (0, r.useCallback)(
                  (e) => {
                    (_(e), l && l(e));
                  },
                  [l],
                );
              ((0, r.useEffect)(() => {
                if (B && !t) {
                  const e = u;
                  return (0, A.F)(() => {
                    b(F.In);
                  }, e);
                }
              }, [b, t, B, u]),
                (0, r.useEffect)(() => {
                  if (g) {
                    const t = e + u;
                    return (0, A.F)(() => {
                      (o && o(), b(F.End));
                    }, t);
                  }
                }, [b, g, o, u, e]));
              const f = (0, r.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, u, e],
                ),
                h = (0, r.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, u, e],
                ),
                v = (0, r.useMemo)(
                  () => ({ width: `${Math.abs(n - i)}%`, left: `${c ? i : n}%` }),
                  [n, c, i],
                );
              return C
                ? null
                : s().createElement(
                    "div",
                    { className: D, style: v },
                    s().createElement(
                      "div",
                      { style: B ? f : h, className: p },
                      s().createElement(d, { size: a }),
                    ),
                  );
            },
          ),
          B = (0, r.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: n,
              disabled: a,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const d = (0, r.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(E, {
                  size: u,
                  lineRef: n,
                  disabled: a,
                  isComplete: i,
                  baseStyles: d,
                }),
                t >= 0 &&
                  s().createElement(C, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          b = "ProgressBarDeltaGrow_base_7e",
          f = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          h = "ProgressBarDeltaGrow_glow_68",
          v = (e) => (e ? { left: 0 } : { right: 0 }),
          w = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          y = (e) => ({ transitionDuration: `${e}ms` }),
          S = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: n,
              size: i,
              to: o,
              onEndAnimation: l,
              onChangeAnimationState: c,
              className: m,
            }) => {
              const E = o < n,
                _ = (0, r.useState)(g.Idle),
                F = _[0],
                D = _[1],
                p = F === g.End,
                C = F === g.Idle,
                B = F === g.Grow,
                S = F === g.Shrink,
                T = (0, r.useCallback)(
                  (e) => {
                    (D(e), c && c(e));
                  },
                  [c],
                ),
                R = (0, r.useCallback)(
                  (e, u) =>
                    (0, A.F)(() => {
                      T(e);
                    }, u),
                  [T],
                );
              (0, r.useEffect)(() => {
                if (!t)
                  return C
                    ? R(g.Grow, u)
                    : B
                      ? R(g.Shrink, e)
                      : S
                        ? R(g.End, e)
                        : void (p && l && l());
              }, [R, t, p, B, C, S, l, u, e]);
              const x = (0, r.useMemo)(() => Object.assign({ width: "100%" }, y(e), v(E)), [E, e]),
                N = (0, r.useMemo)(() => Object.assign({ width: "0%" }, y(e), v(E)), [E, e]),
                P = (0, r.useMemo)(() => Object.assign({ width: "0%" }, w(E, n), y(e)), [n, E, e]),
                k = (0, r.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - n)}%` }, w(E, n), y(e)),
                  [n, E, o, e],
                );
              if (p) return null;
              const M = a()(b, m, E && 0 === o && f);
              return s().createElement(
                "div",
                { style: C ? P : k, className: M },
                s().createElement(
                  "div",
                  { style: S ? N : x, className: h },
                  s().createElement(d, { size: i }),
                ),
              );
            },
          ),
          T = (0, r.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: n,
              disabled: a,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const d = e < t,
                m = (0, r.useState)(!1),
                _ = m[0],
                A = m[1],
                F = (0, r.useCallback)(
                  (e) => {
                    (e === g.Shrink && A(!0), c && c(e));
                  },
                  [c],
                ),
                D = (0, r.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                p = (0, r.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(E, {
                  size: u,
                  lineRef: n,
                  disabled: a,
                  isComplete: i,
                  withoutBounce: d && 0 === e,
                  baseStyles: _ ? p : D,
                }),
                t >= 0 &&
                  s().createElement(S, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    onChangeAnimationState: F,
                    freezed: o.freezed,
                    onEndAnimation: l,
                    from: t,
                    size: u,
                    to: e,
                    className: o.delta.className,
                  }),
              );
            },
          ),
          R = ["onComplete", "onEndAnimation"];
        function x() {
          return (
            (x =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            x.apply(this, arguments)
          );
        }
        const N = (0, r.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, R);
            const a = (0, r.useState)(!1),
              i = a[0],
              l = a[1],
              c = (0, r.useCallback)(() => {
                const e = 100 === n.to;
                (e !== i && l(e), e && u && u(), t && t());
              }, [i, u, t, n.to]);
            switch (n.animationSettings.type) {
              case o.r.Simple:
                return s().createElement(B, x({}, n, { onEndAnimation: c, isComplete: i }));
              case o.r.Growing:
                return s().createElement(T, x({}, n, { onEndAnimation: c, isComplete: i }));
              default:
                return null;
            }
          }),
          P = ["onEndAnimation"];
        function k() {
          return (
            (k =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            k.apply(this, arguments)
          );
        }
        const M = (0, r.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, P);
          const n = (0, r.useRef)({}),
            a = (0, r.useCallback)(() => {
              ((n.current.from = void 0), u && u());
            }, [u]),
            i = "number" == typeof n.current.from ? n.current.from : t.from;
          return (
            (n.current.from = i),
            s().createElement(N, k({}, t, { onEndAnimation: a, key: `${i}-${t.to}`, from: i }))
          );
        });
        function I() {
          return (
            (I =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            I.apply(this, arguments)
          );
        }
        const L = (0, r.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: n,
              deltaFrom: a,
              animationSettings: r,
              onEndAnimation: i,
              onChangeAnimationState: o,
              onComplete: l,
            }) => {
              if (a === u)
                return s().createElement(_, {
                  key: `${a}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: n,
                  onComplete: l,
                });
              const c = {
                from: a,
                to: u,
                size: e,
                lineRef: t,
                disabled: n,
                animationSettings: r,
                onComplete: l,
                onEndAnimation: i,
                onChangeAnimationState: o,
              };
              return r.withStack
                ? s().createElement(M, c)
                : s().createElement(N, I({ key: `${a}-${u}` }, c));
            },
          ),
          O = (e) => ({
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
          });
        var H = t(515);
        const U = (e, u, t) => {
            if ("number" == typeof t) {
              return ((0, H.u)(0, u, t) / u) * 100;
            }
            return e;
          },
          $ = {
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
          W = {
            freezed: !1,
            withStack: !1,
            type: o.r.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          z = (0, r.memo)(
            ({
              maxValue: e = 100,
              theme: u = $,
              size: t = o.$.Default,
              animationSettings: n = W,
              disabled: c = !1,
              withoutBackground: d = !1,
              progressBarBackgroundClassMix: m,
              value: E,
              deltaFrom: _,
              lineRef: A,
              onChangeAnimationState: g,
              onEndAnimation: F,
              onComplete: D,
            }) => {
              const p = ((e, u, t) =>
                (0, r.useMemo)(() => {
                  const n = ((0, H.u)(0, u, e) / u) * 100;
                  return { value: n, deltaFrom: U(n, u, t) };
                }, [t, u, e]))(E, e, _);
              return s().createElement(
                "div",
                { className: a()(i.base, i[`base__${t}`]), style: O(u) },
                !d && s().createElement(l, { size: t, classMix: m }),
                s().createElement(L, {
                  size: t,
                  lineRef: A,
                  disabled: c,
                  value: p.value,
                  deltaFrom: p.deltaFrom,
                  animationSettings: n,
                  onEndAnimation: F,
                  onChangeAnimationState: g,
                  onComplete: D,
                }),
              );
            },
          );
      },
      736: (e, u, t) => {
        "use strict";
        let n, a;
        (t.d(u, { $: () => n, r: () => a }),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
          })(n || (n = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(a || (a = {})));
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
      515: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => n });
        const n = (e, u, t) => (t < e ? e : t > u ? u : t);
      },
      122: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => n });
        const n = (e, u) => {
          let t;
          const n = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(n));
          };
        };
      },
      374: (e, u, t) => {
        "use strict";
        t.d(u, { s_: () => a, dV: () => s, yR: () => r, f8: () => o });
        t(649);
        let n;
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
        })(n || (n = {}));
        t(364);
        const a = 1e3,
          r = 60,
          s = 60 * r,
          i = 24 * s;
        Date.now();
        function o(e = 0) {
          let u = e;
          const t = Math.trunc(u / i);
          u -= t * i;
          const n = Math.trunc(u / s);
          u -= n * s;
          const a = Math.trunc(u / r);
          return ((u -= a * r), { days: t, hours: n, minutes: a, seconds: u });
        }
      },
      67: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => j });
        var n = {};
        (t.r(n), t.d(n, { mouse: () => d, onResize: () => l }));
        var a = {};
        (t.r(a),
          t.d(a, {
            events: () => n,
            getMouseGlobalPosition: () => E,
            getSize: () => m,
            graphicsQuality: () => _,
          }));
        var r = {};
        (t.r(r), t.d(r, { getBgUrl: () => g, getTextureUrl: () => A }));
        var s = {};
        function i(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        function o(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        (t.r(s),
          t.d(s, {
            addModelObserver: () => T,
            addPreloadTexture: () => w,
            children: () => r,
            displayStatus: () => F,
            displayStatusIs: () => q,
            events: () => D,
            extraSize: () => Q,
            forceTriggerMouseMove: () => z,
            freezeTextureBeforeResize: () => k,
            getBrowserTexturePath: () => S,
            getDisplayStatus: () => G,
            getScale: () => M,
            getSize: () => x,
            getViewGlobalPosition: () => P,
            isClientAccessible: () => U,
            isEventHandled: () => W,
            isFocused: () => H,
            pxToRem: () => I,
            remToPx: () => L,
            resize: () => N,
            sendEvent: () => v,
            setAnimateWindow: () => O,
            setEventHandled: () => $,
            setInputPaddingsRem: () => y,
            setSidePaddingsRem: () => R,
            whenTutorialReady: () => V,
          }));
        const l = i("clientResized"),
          c = { down: i("mousedown"), up: i("mouseup"), move: i("mousemove") };
        const d = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && o(!1);
          }
          function t() {
            e.enabled && o(!0);
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
              : o(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let a = !0;
                  const r = `mouse${u}`,
                    s = c[u]((e) => t([e, "outside"]));
                  function i(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    n(),
                    () => {
                      a &&
                        (s(), window.removeEventListener(r, i), (e.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(t)),
              u
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
              e.enabled && o(!0);
            },
            disableOutside() {
              e.enabled && o(!1);
            },
          });
        })();
        function m(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function E(e = "px") {
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
        function g(e, u, t) {
          return `url(${A(e, u, t)})`;
        }
        const F = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          D = {
            onTextureFrozen: i("self.onTextureFrozen"),
            onTextureReady: i("self.onTextureReady"),
            onDomBuilt: i("self.onDomBuilt"),
            onLoaded: i("self.onLoaded"),
            onDisplayChanged: i("self.onShowingStatusChanged"),
            onFocusUpdated: i("self.onFocusChanged"),
            children: {
              onAdded: i("children.onAdded"),
              onLoaded: i("children.onLoaded"),
              onRemoved: i("children.onRemoved"),
              onAttached: i("children.onAttached"),
              onTextureReady: i("children.onTextureReady"),
              onRequestPosition: i("children.requestPosition"),
            },
          },
          p = ["args"];
        const C = 2,
          B = 16,
          b = 32,
          f = 64,
          h = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, p);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((n = a),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          v = {
            close(e) {
              h("popover" === e ? C : b);
            },
            minimize() {
              h(f);
            },
            move(e) {
              h(B, { isMouseEvent: !0, on: e });
            },
          };
        function w(e) {
          viewEnv.addPreloadTexture(e);
        }
        function y(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function S(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function T(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function R(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function x(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function N(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function P(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: L(u.x), y: L(u.y) };
        }
        function k() {
          viewEnv.freezeTextureBeforeResize();
        }
        function M() {
          return viewEnv.getScale();
        }
        function I(e) {
          return viewEnv.pxToRem(e);
        }
        function L(e) {
          return viewEnv.remToPx(e);
        }
        function O(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function H() {
          return viewEnv.isFocused();
        }
        function U() {
          return viewEnv.isClientAccessible();
        }
        function $() {
          return viewEnv.setEventHandled();
        }
        function W() {
          return viewEnv.isEventHandled();
        }
        function z() {
          viewEnv.forceTriggerMouseMove();
        }
        function G() {
          return viewEnv.getShowingStatus();
        }
        const q = Object.keys(F).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === F[u]), e),
            {},
          ),
          Q = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          V = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : D.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          j = { view: s, client: a };
      },
      255: (e, u, t) => {
        "use strict";
        t.d(u, { au: () => E, tp: () => _, D9: () => m });
        var n = t(179);
        const a = (e) => {
          const u = (0, n.useRef)();
          return (
            (0, n.useEffect)(() => {
              u.current = e;
            }, [e]),
            u.current
          );
        };
        var r = t(374);
        const s = () => {},
          i = (e = 0, u, t = 0, a = s) => {
            const i = (0, n.useState)(e),
              o = i[0],
              l = i[1];
            return (
              (0, n.useEffect)(() => {
                if (e > 0) {
                  l(e);
                  const n = Date.now(),
                    s = u || (e > 2 * r.yR ? r.yR : 1),
                    i = setInterval(() => {
                      const u = e - Math.floor((Date.now() - n) / r.s_);
                      null !== t && u <= t ? (l(t), a && a(), clearInterval(i)) : l(u);
                    }, s * r.s_);
                  return () => {
                    clearInterval(i);
                  };
                }
                l(0);
              }, [e, u, t, a]),
              o
            );
          };
        var o = t(122);
        const l = (e, u) => {
          const t = (0, n.useState)(e),
            a = t[0],
            r = t[1];
          return ((0, n.useEffect)(() => (0, o.F)(() => r(e), u), [e, u]), a);
        };
        t(67);
        t(536);
        var c = t(364);
        c.Sw.instance;
        let d;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(d || (d = {}));
        c.Sw.instance;
        const m = a,
          E = i,
          _ = l;
      },
      536: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var n = t(179);
        const a = (e) => {
          const u = (0, n.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      521: (e, u, t) => {
        "use strict";
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
      649: (e, u, t) => {
        "use strict";
        let n;
        function a(e, u) {
          return e.replace(/\{\w+\}/g, (e) => String(u[e.slice(1, -1)]));
        }
        function r(e, u) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const t = 0 === e.indexOf("%") ? 2 : 1;
            return String(u[e.slice(t, -t)]);
          });
        }
        (t.d(u, { Uw: () => m, WU: () => a, uF: () => r, v2: () => n }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(n || (n = {})));
        const s = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          i = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          o = (e, u, t = n.left) => e.split(u).reduce(t === n.left ? s : i, []),
          l = (() => {
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
          c = ["zh_cn", "zh_sg", "zh_tw"],
          d = (e, u = n.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return c.includes(t)
              ? l(e)
              : ((e, u = n.left) => {
                  let t = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (o(r, /( )/, u).forEach((e) => (t = t.concat(o(e, a, n.left)))), t);
                })(e, u);
          },
          m = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : d(e, u)));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var n = t(67);
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
            const r = n.O.view.addModelObserver(e, t, a);
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
              const n = this._callbacks[t];
              void 0 !== n && n(e, u);
            });
          }
        }
        a.__instance = void 0;
        const r = a;
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
        t.d(u, { Sw: () => r.Z, B3: () => l, Z5: () => s, B0: () => o, ry: () => D });
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
        var r = t(358);
        const s = {
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
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = t(521),
          _ = t(67);
        const A = ["args"];
        function g(e, u, t, n, a, r, s) {
          try {
            var i = e[r](s),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(n, a);
        }
        const F = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          D = (function () {
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
                    var r = e.apply(u, t);
                    function s(e) {
                      g(r, n, a, s, i, "next", e);
                    }
                    function i(e) {
                      g(r, n, a, s, i, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          p = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, A);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          C = () => p(o.CLOSE),
          B = (e, u) => {
            e.keyCode === E.n.ESCAPE && u();
          };
        var b = t(572);
        const f = a.instance,
          h = {
            DataTracker: r.Z,
            ViewModel: b.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: m,
            makeGlobalBoundingBox: F,
            sendMoveEvent: (e) => p(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => p(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              p(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, a = R.invalid("resId"), r) => {
              const s = _.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                d = i.width,
                m = i.height,
                E = {
                  x: _.O.view.pxToRem(l) + s.x,
                  y: _.O.view.pxToRem(c) + s.y,
                  width: _.O.view.pxToRem(d),
                  height: _.O.view.pxToRem(m),
                };
              p(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: a,
                direction: u,
                bbox: F(E),
                on: !0,
                args: r,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => B(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              B(e, C);
            },
            handleViewEvent: p,
            onBindingsReady: D,
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
            ClickOutsideManager: f,
            SystemLocale: s,
            UserLocale: i,
          };
        window.ViewEnvHelper = h;
      },
      181: (e, u, t) => {
        "use strict";
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => Ou,
            Bar: () => Mu,
            DefaultScroll: () => Lu,
            Direction: () => pu,
            defaultSettings: () => Cu,
            useHorizontalScrollApi: () => bu,
          }));
        var a = {};
        (t.r(a),
          t.d(a, {
            Area: () => tt,
            Bar: () => Ju,
            Default: () => ut,
            useVerticalScrollApi: () => Hu,
          }));
        var r = t(179),
          s = t.n(r);
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
        var o = t(67);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function d(e, u, t) {
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
            r = Math.min(n, a);
          return {
            extraLarge: r === t.extraLarge.weight,
            large: r === t.large.weight,
            medium: r === t.medium.weight,
            small: r === t.small.weight,
            extraSmall: r === t.extraSmall.weight,
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
        const m = o.O.client.getSize("rem"),
          E = m.width,
          _ = m.height,
          A = Object.assign({ width: E, height: _ }, d(E, _, l)),
          g = (0, r.createContext)(A),
          F = ["children"];
        const D = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, F);
          const n = (0, r.useContext)(g),
            a = n.extraLarge,
            s = n.large,
            o = n.medium,
            l = n.small,
            c = n.extraSmall,
            d = n.extraLargeWidth,
            m = n.largeWidth,
            E = n.mediumWidth,
            _ = n.smallWidth,
            A = n.extraSmallWidth,
            D = n.extraLargeHeight,
            p = n.largeHeight,
            C = n.mediumHeight,
            B = n.smallHeight,
            b = n.extraSmallHeight,
            f = { extraLarge: D, large: p, medium: C, small: B, extraSmall: b };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && a) return u;
            if (t.large && s) return u;
            if (t.medium && o) return u;
            if (t.small && l) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && d) return i(u, t, f);
            if (t.largeWidth && m) return i(u, t, f);
            if (t.mediumWidth && E) return i(u, t, f);
            if (t.smallWidth && _) return i(u, t, f);
            if (t.extraSmallWidth && A) return i(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && D) return u;
              if (t.largeHeight && p) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && B) return u;
              if (t.extraSmallHeight && b) return u;
            }
          }
          return null;
        };
        D.defaultProps = {
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
        (0, r.memo)(D);
        var p = t(536);
        const C = (0, r.memo)(({ children: e }) => {
          const u = (0, r.useContext)(g),
            t = (0, r.useState)(u),
            n = t[0],
            a = t[1],
            i = (0, r.useCallback)((e, u) => {
              const t = o.O.view.pxToRem(e),
                n = o.O.view.pxToRem(u);
              a(Object.assign({ width: t, height: n }, d(t, n, l)));
            }, []);
          ((0, p.Z)(() => {
            engine.on("clientResized", i);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", i), [i]));
          const c = (0, r.useMemo)(() => Object.assign({}, n), [n]);
          return s().createElement(g.Provider, { value: c }, e);
        });
        var B = t(483),
          b = t.n(B),
          f = t(926),
          h = t.n(f);
        let v, w, y;
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
          })(w || (w = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.small.height)] = "Small"),
              (e[(e.Medium = l.medium.height)] = "Medium"),
              (e[(e.Large = l.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(y || (y = {})));
        const S = () => {
            const e = (0, r.useContext)(g),
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
              a = ((e) => {
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
              s = ((e) => {
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
              mediaSize: n,
              mediaWidth: a,
              mediaHeight: s,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          T = ["children", "className"];
        function x() {
          return (
            (x =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            x.apply(this, arguments)
          );
        }
        const N = {
            [w.ExtraSmall]: "",
            [w.Small]: h().SMALL_WIDTH,
            [w.Medium]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH}`,
            [w.Large]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH} ${h().EXTRA_LARGE_WIDTH}`,
          },
          P = {
            [y.ExtraSmall]: "",
            [y.Small]: h().SMALL_HEIGHT,
            [y.Medium]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT}`,
            [y.Large]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT}`,
            [y.ExtraLarge]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT} ${h().EXTRA_LARGE_HEIGHT}`,
          },
          k = {
            [v.ExtraSmall]: "",
            [v.Small]: h().SMALL,
            [v.Medium]: `${h().SMALL} ${h().MEDIUM}`,
            [v.Large]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE}`,
            [v.ExtraLarge]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE} ${h().EXTRA_LARGE}`,
          },
          M = (e) => {
            let u = e.children,
              t = e.className,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, T);
            const a = S(),
              r = a.mediaWidth,
              i = a.mediaHeight,
              o = a.mediaSize;
            return s().createElement("div", x({ className: b()(t, N[r], P[i], k[o]) }, n), u);
          },
          I = ["children"];
        const L = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, I);
          return s().createElement(C, null, s().createElement(M, t, u));
        };
        var O = t(493),
          H = t.n(O);
        let U, $;
        (!(function (e) {
          e.Default = "default";
        })(U || (U = {})),
          (function (e) {
            ((e.AVAILABLE = "available"), (e.DISABLED = "disabled"), (e.NO_OFFERS = "no_offers"));
          })($ || ($ = {})));
        var W = t(521),
          z = t(364);
        const G = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function q(e = W.n.NONE, u = G, t = !1) {
          (0, r.useEffect)(() => {
            if (e !== W.n.NONE)
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
        var Q = t(403),
          V = t(30);
        let j, Y, X, K, Z, J, ee, ue, te;
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
        })(j || (j = {})),
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
          })(Y || (Y = {})),
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
          })(X || (X = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(K || (K = {})),
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
          })(Z || (Z = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(J || (J = {})),
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
          })(ee || (ee = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(ue || (ue = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(te || (te = {})));
        class ne extends s().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = z.B3.GOLD;
            else e = z.B3.INTEGRAL;
            const u = z.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        ne.defaultProps = { format: "integral" };
        const ae = [
            j.Items,
            j.Equipment,
            j.Xp,
            j.XpFactor,
            j.Blueprints,
            j.BlueprintsAny,
            j.Goodies,
            j.Berths,
            j.Slots,
            j.Tokens,
            j.CrewSkins,
            j.CrewBooks,
            j.Customizations,
            j.CreditsFactor,
            j.TankmenXp,
            j.TankmenXpFactor,
            j.FreeXpFactor,
            j.BattleToken,
            j.PremiumUniversal,
            j.NaturalCover,
            j.BpCoin,
            j.BattlePassSelectToken,
            j.BattlaPassFinalAchievement,
            j.BattleBadge,
            j.BonusX5,
            j.CrewBonusX3,
            j.NewYearFillers,
            j.NewYearInvoice,
            j.EpicSelectToken,
            j.Comp7TokenWeeklyReward,
            j.Comp7TokenCouponReward,
            j.BattleBoosterGift,
            j.CosmicLootboxCommon,
            j.CosmicLootboxSilver,
            j.SelectableBonus,
            j.PostStamp,
            j.PremiumPlusUniversal,
            j.GoldenTicket,
            j.RewardsSlots,
            j.WtStamp,
            j.WtTicket,
            j.WtMainPrizeDiscount,
            j.WtHunter,
            j.WtHunterCollection,
          ],
          re = [j.Gold, j.Credits, j.Crystal, j.FreeXp],
          se = [j.BattlePassPoints],
          ie = [j.PremiumPlus, j.Premium];
        let oe;
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
        })(oe || (oe = {}));
        const le = (e) =>
            ae.includes(e)
              ? K.MULTI
              : re.includes(e)
                ? K.CURRENCY
                : se.includes(e)
                  ? K.NUMBER
                  : ie.includes(e)
                    ? K.PREMIUM_PLUS
                    : K.STRING,
          ce = ["engravings", "backgrounds"],
          de = ["engraving", "background"],
          me = (e, u = X.Small) => {
            const t = e.name,
              n = e.type,
              a = e.value,
              r = e.icon,
              s = e.item,
              i = e.dogTagType,
              o = ((e) => {
                switch (e) {
                  case X.S600x450:
                    return "c_600x450";
                  case X.S400x300:
                    return "c_400x300";
                  case X.S296x222:
                    return "c_296x222";
                  case X.S232x174:
                    return "c_232x174";
                  case X.Big:
                    return "c_80x80";
                  case X.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_${a}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${a}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${a}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${s}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${r}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case X.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case X.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${r}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const n = ce[e];
                  if (n) {
                    const a = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(n),
                      r = a.$dyn(t);
                    return r ? `${r}` : `${a.$dyn(de[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(i, u, r);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${o}.${r}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case X.S600x450:
                      return "c_600x450";
                    case X.S400x300:
                      return "c_400x300";
                    case X.S296x222:
                      return "c_296x222";
                    case X.S232x174:
                      return "c_232x174";
                    case X.S180x135:
                      return "big";
                    case X.Big:
                    case X.S80x80:
                      return "c_80x80";
                    case X.Small:
                    case X.S48x48:
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
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${o}.${r}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case X.Mini:
                      return oe.s32;
                    case X.Small:
                    case X.S48x48:
                      return oe.s48;
                    case X.S80x80:
                    case X.Big:
                      return oe.s80;
                    case X.S128x100:
                      return oe.s116;
                    case X.S180x135:
                    case X.S232x174:
                    case X.S296x222:
                      return oe.s296;
                    case X.S400x300:
                      return oe.s400;
                    case X.S600x450:
                      return oe.s600;
                  }
                })(u)}`;
              case j.StyleProgress:
              case j.LbStyleProgress:
                return _e(r, u, te.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          Ee = (e, u, t) => {
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
          _e = (e, u, t) => {
            const n = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              a = n.$dyn(e);
            return String(null != a ? a : n.$dyn(t));
          };
        let Ae;
        function ge(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        !(function (e) {
          ((e.Done = "done"),
            (e.UndoneSubscription = "undoneSubscription"),
            (e.Locked = "notAvailable"),
            (e.Active = ""));
        })(Ae || (Ae = {}));
        const Fe = ge;
        function De(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, n) => u(null == e ? void 0 : e.value, t, n));
        }
        function pe(e, u, t) {
          const n = [];
          for (let a = 0; a < e.length; a++) {
            const r = Fe(e, a);
            u(r, a, e) && n.push(t(r, a, e));
          }
          return n;
        }
        const Ce = ["from", "enter", "leave"],
          Be = ["from", "enter", "leave"],
          be = ["from", "enter", "leave"];
        function fe(e, u) {
          if (null == e) return {};
          var t,
            n,
            a = {},
            r = Object.keys(e);
          for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
          return a;
        }
        const he = "tooltipId";
        let ve, we, ye;
        (!(function (e) {
          ((e.VEHICLE_FOR_GIFT = "vehicleForGift"),
            (e.VEHICLE_DISCOUNT = "vehicleDiscount"),
            (e.VEHICLE_FOR_RENT = "vehicleForRent"),
            (e.SELECTABLE_VEHICLE_FOR_GIFT = "selectableVehicleForGift"),
            (e.SELECTABLE_VEHICLE_DISCOUNT = "selectableVehicleDiscount"));
        })(ve || (ve = {})),
          (function (e) {
            ((e[(e.ExtraSmall = 32)] = "ExtraSmall"),
              (e[(e.Small = 48)] = "Small"),
              (e[(e.Medium = 64)] = "Medium"),
              (e[(e.Large = 80)] = "Large"),
              (e[(e.ExtraLarge = 100)] = "ExtraLarge"));
          })(we || (we = {})),
          (function (e) {
            ((e[(e.DailyQuests = 0)] = "DailyQuests"),
              (e[(e.PremiumQuests = 1)] = "PremiumQuests"));
          })(ye || (ye = {})));
        const Se = { [ye.DailyQuests]: "dailyQuests", [ye.PremiumQuests]: "premiumQuests" },
          Te = (e) => {
            if (void 0 !== e)
              return (
                void 0 === Se[e] &&
                  console.error(`Content resource name was not found for tab index ${e}`),
                Se[e]
              );
          },
          Re = (e, u, t) => {
            const n = R.images.gui.maps.icons.missions.missionIcons.$num(
                ((e) => {
                  switch (!0) {
                    case e >= v.ExtraLarge:
                      return we.ExtraLarge;
                    case e >= v.Large:
                      return we.Large;
                    case e >= v.Medium:
                      return we.Medium;
                    default:
                      return we.ExtraSmall;
                  }
                })(e),
              ),
              a = t ? "_gold" : "_silver";
            return { backgroundImage: `url(${n.$dyn(`${u}${a}`)})` };
          },
          xe = (e, u, t) =>
            De(e, (e) => ({
              name: e.name,
              image: me(e, t),
              special: e.overlayType,
              value: e.value,
              valueType: le(e.name),
              tooltipArgs: Ee({ [he]: `${u}:${e.index}` }, Number(e.tooltipContentId), {
                ignoreShowDelay: !0,
              }),
            })),
          Ne = (e, u) => (e.items.length >= 1 ? e : u.items.length >= 1 ? u : void 0),
          Pe = (e) =>
            (function (e, u) {
              if (Array.isArray(e)) return e.filter(u);
              const t = [];
              for (let a = 0; a < e.length; a++) {
                var n;
                const r = null == (n = e[a]) ? void 0 : n.value;
                u(r, a, e) && t.push(r);
              }
              return t;
            })(e, (e) => e.status === Ae.Done || e.status === Ae.UndoneSubscription).length,
          ke = (e) => e.filter((e) => e.value).length,
          Me =
            (Object.values(Z),
            ve.VEHICLE_FOR_GIFT,
            ve.VEHICLE_DISCOUNT,
            ve.VEHICLE_FOR_RENT,
            ve.SELECTABLE_VEHICLE_FOR_GIFT,
            ve.SELECTABLE_VEHICLE_DISCOUNT,
            ve.VEHICLE_DISCOUNT,
            ve.SELECTABLE_VEHICLE_DISCOUNT,
            {
              easeOutCubic: (e) => 1 - Math.pow(1 - e, 3),
              easeInCubic: (e) => e * e * e,
              easeOutQuint: (e) => 1 - Math.pow(1 - e, 5),
              easeOutSine: (e) => Math.sin((e * Math.PI) / 2),
              easeInSine: (e) => 1 - Math.cos((e * Math.PI) / 2),
              easeOutCirc: (e) => Math.sqrt(1 - Math.pow(e - 1, 2)),
              easeInCirc: (e) => 1 - Math.sqrt(1 - Math.pow(e, 2)),
            }),
          Ie = (e, u = {}) => {
            let t = u.from,
              n = void 0 === t ? {} : t,
              a = u.enter,
              r = void 0 === a ? {} : a,
              s = u.leave,
              i = void 0 === s ? {} : s,
              o = fe(u, Ce);
            return (0, V.useTransition)(
              e,
              Object.assign(
                {
                  from: Object.assign({ opacity: 0, pointerEvents: "none" }, n),
                  enter: Object.assign(
                    {
                      opacity: 1,
                      pointerEvents: "auto",
                      config: { duration: 400, easing: Me.easeInSine },
                    },
                    r,
                  ),
                  leave: Object.assign(
                    {
                      opacity: 0,
                      pointerEvents: "none",
                      config: { duration: 400, easing: Me.easeOutSine },
                    },
                    i,
                  ),
                  expires: !1,
                },
                o,
              ),
            );
          },
          Le = (e, u, t = {}) => {
            let n = t.from,
              a = void 0 === n ? {} : n,
              r = t.enter,
              s = void 0 === r ? {} : r,
              i = t.leave,
              o = void 0 === i ? {} : i,
              l = fe(t, Be);
            return (0, V.useTransition)(
              e,
              Object.assign(
                {
                  from: Object.assign(
                    { opacity: 0, transform: `translateY(${u}rem)`, pointerEvents: "none" },
                    a,
                  ),
                  enter: Object.assign(
                    {
                      opacity: 1,
                      transform: "translateY(0rem)",
                      pointerEvents: "auto",
                      config: { duration: 200, easing: Me.easeOutCirc },
                    },
                    s,
                  ),
                  leave: Object.assign(
                    {
                      opacity: 0,
                      transform: `translateY(${u}rem)`,
                      pointerEvents: "none",
                      config: { duration: 300, easing: Me.easeInCirc },
                    },
                    o,
                  ),
                  expires: !1,
                },
                l,
              ),
            );
          },
          Oe = (e, u, t = {}) => {
            let n = t.from,
              a = void 0 === n ? {} : n,
              r = t.enter,
              s = void 0 === r ? {} : r,
              i = t.leave,
              o = void 0 === i ? {} : i,
              l = fe(t, be);
            return (0, V.useTransition)(
              e,
              Object.assign(
                {
                  from: Object.assign(
                    { opacity: 0, transform: `translateX(${u}rem)`, pointerEvents: "none" },
                    a,
                  ),
                  enter: Object.assign(
                    {
                      opacity: 1,
                      transform: "translateX(0rem)",
                      pointerEvents: "auto",
                      config: { duration: 300, easing: Me.easeOutQuint },
                    },
                    s,
                  ),
                  leave: Object.assign(
                    {
                      opacity: 0,
                      transform: `translateX(${u}rem)`,
                      pointerEvents: "none",
                      config: { duration: 300, easing: Me.easeInCubic },
                    },
                    o,
                  ),
                  expires: !1,
                },
                l,
              ),
            );
          };
        function He() {
          return !1;
        }
        console.log;
        var Ue = t(174);
        function $e(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return We(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return We(e, u);
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
        function We(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const ze = (e) => (0 === e ? window : window.subViews.get(e));
        var Ge = t(946);
        const qe = ((e, u) => {
            const t = (0, r.createContext)({});
            return [
              function ({ mode: n = "real", options: a, children: i, mocks: l }) {
                const c = (0, r.useRef)([]),
                  d = (t, n, a) => {
                    var r;
                    const s = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = ze,
                        context: n = "model",
                      } = {}) {
                        const a = new Map();
                        function r(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? a.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = a.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const s = (e) => {
                          const a = t(u),
                            r = n.split(".").reduce((e, u) => e[u], a);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, r);
                        };
                        return {
                          subscribe: (t, r) => {
                            const i = "string" == typeof r ? `${n}.${r}` : n,
                              l = o.O.view.addModelObserver(i, u, !0);
                            return (a.set(l, t), e && t(s(r)), l);
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
                            for (var e, t = $e(a.keys()); !(e = t()).done;) r(e.value, u);
                          },
                          unsubscribe: r,
                        };
                      })(n),
                      i =
                        "real" === t
                          ? s
                          : Object.assign({}, s, {
                              readByPath:
                                null != (r = null == a ? void 0 : a.getter) ? r : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == a ? void 0 : a.getter(e)) : i.readByPath(e),
                      d = (e) => c.current.push(e),
                      m = e({
                        mode: t,
                        readByPath: l,
                        externalModel: i,
                        observableModel: {
                          array: (e, u) => {
                            const n = null != u ? u : l(e),
                              a = Ue.LO.box(n, { equals: He });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, Ue.aD)((e) => a.set(e)),
                                  e,
                                ),
                              a
                            );
                          },
                          object: (e, u) => {
                            const n = null != u ? u : l(e),
                              a = Ue.LO.box(n, { equals: He });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, Ue.aD)((e) => a.set(e)),
                                  e,
                                ),
                              a
                            );
                          },
                          primitives: (e, u) => {
                            const n = l(u);
                            if (Array.isArray(e)) {
                              const a = e.reduce((e, u) => ((e[u] = Ue.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, Ue.aD)((u) => {
                                      e.forEach((e) => {
                                        a[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                a
                              );
                            }
                            {
                              const a = e,
                                r = Object.entries(a),
                                s = r.reduce((e, [u, t]) => ((e[t] = Ue.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, Ue.aD)((e) => {
                                      r.forEach(([u, t]) => {
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
                        cleanup: d,
                      }),
                      E = { mode: t, model: m, externalModel: i, cleanup: d };
                    return {
                      model: m,
                      controls: "mocks" === t && a ? a.controls(E) : u(E),
                      externalModel: i,
                      mode: t,
                    };
                  },
                  m = (0, r.useRef)(!1),
                  E = (0, r.useState)(n),
                  _ = E[0],
                  A = E[1],
                  g = (0, r.useState)(() => d(n, a, l)),
                  F = g[0],
                  D = g[1];
                return (
                  (0, r.useEffect)(() => {
                    m.current ? D(d(_, a, l)) : (m.current = !0);
                  }, [l, _, a]),
                  (0, r.useEffect)(() => {
                    A(n);
                  }, [n]),
                  (0, r.useEffect)(
                    () => () => {
                      (F.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [F],
                  ),
                  s().createElement(t.Provider, { value: F }, i)
                );
              },
              () => (0, r.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  primitives: e.primitives(["currentTabIdx"]),
                  daily: e.object("dailyQuests"),
                  dailyQuests: e.array("dailyQuests.quests", []),
                  dailyQuestsCompletedVisited: e.array("dailyQuests.missionsCompletedVisited", []),
                  premium: e.object("premiumMissions"),
                  premiumQuests: e.array("premiumMissions.missions", []),
                  premiumQuestsCompletedVisited: e.array(
                    "premiumMissions.missionsCompletedVisited",
                    [],
                  ),
                  epicQuest: e.object("epicQuest"),
                  epicQuestBonuses: e.array("epicQuest.bonuses"),
                },
                t = (0, Ge.Om)(() => {
                  const e = u.root.get().premMissionsTabDiscovered;
                  return [
                    { id: ye.DailyQuests, title: R.strings.quests.dailyQuests.tab.label() },
                    {
                      id: ye.PremiumQuests,
                      title: R.strings.quests.premiumQuests.tab.label(),
                      notification: e ? void 0 : { type: "dot" },
                    },
                  ];
                }),
                n = (0, Ge.Om)(() =>
                  [
                    { tabIndex: ye.DailyQuests, isEnabled: u.daily.get().isEnabled },
                    { tabIndex: ye.PremiumQuests, isEnabled: u.premium.get().isEnabled },
                  ].filter((e) => e.isEnabled),
                ),
                a = (0, Ge.Om)(() => {
                  var e;
                  const t = u.primitives.currentTabIdx.get(),
                    a = n(),
                    r = a.find((e) => e.tabIndex === t);
                  return r ? r.tabIndex : null == (e = a[0]) ? void 0 : e.tabIndex;
                }),
                r = (0, Ge.Om)((e, t) => {
                  const n = t >= v.Large ? X.Big : X.Small,
                    a = (e) =>
                      De(e, (e) =>
                        Object.assign({}, e, {
                          rewardSize: n,
                          bonuses: xe(e.bonuses, e.id, n),
                          subscriptionBonuses: xe(e.subscriptionBonuses, e.id, n),
                        }),
                      );
                  switch (e) {
                    case ye.DailyQuests:
                      return a(u.dailyQuests.get()).slice(0, 3);
                    case ye.PremiumQuests:
                      return a(u.premiumQuests.get());
                    default:
                      return [];
                  }
                }),
                s = (0, Ge.Om)(() =>
                  u.dailyQuests.get().some((e) => e.value.isEnabledSubscription),
                ),
                i = (0, Ge.Om)(() => u.dailyQuestsCompletedVisited.get(), { equals: He }),
                o = (0, Ge.Om)(() => u.premiumQuestsCompletedVisited.get(), { equals: He }),
                l = (0, Ge.Om)((e, u) => {
                  switch (e) {
                    case ye.DailyQuests:
                      return ge(i(), u);
                    case ye.PremiumQuests:
                      return ge(o(), u);
                    default:
                      return void console.error(`Unreachable branch in tabIndex ${e}`);
                  }
                });
              return Object.assign({}, u, {
                computes: {
                  getEnabledFeatures: n,
                  getCurrentTabIndex: a,
                  getTabs: t,
                  getQuests: r,
                  isCardVisited: l,
                  isEnabledSubscription: s,
                  getDailyQuestsCompletedVisited: i,
                  getPremiumQuestsCompletedVisited: o,
                  getRerolledCardsIds: (e, u) =>
                    pe(
                      e,
                      (e, t) => {
                        const n = u[t];
                        return (
                          void 0 !== n &&
                          (e.id !== n.id ||
                            ((e.status === Ae.Done || e.status === Ae.UndoneSubscription) &&
                              n.status !== Ae.Done &&
                              n.status !== Ae.UndoneSubscription))
                        );
                      },
                      (e) => e.id,
                    ),
                },
              });
            },
            ({ externalModel: e }) => ({
              close: e.createCallbackNoArgs("onClose"),
              reroll: e.createCallback((e) => ({ questId: e }), "onReroll"),
              tabClick: e.createCallback((e) => ({ tabIdx: e }), "onTabClick"),
              infoToggle: e.createCallbackNoArgs("onInfoToggle"),
              buyPremiumBtnClick: e.createCallbackNoArgs("onBuyPremiumBtnClick"),
              rerollEnabled: e.createCallbackNoArgs("onRerollEnabled"),
              claimRewards: e.createCallbackNoArgs("onClaimRewards"),
            }),
          ),
          Qe = qe[0],
          Ve = qe[1],
          je = {
            base: "App_base_9b",
            background: "App_background_5f",
            background__dailyQuests: "App_background__dailyQuests_0c",
            background__premiumQuests: "App_background__premiumQuests_5b",
            infoButton: "App_infoButton_9b",
            infoButton__info: "App_infoButton__info_67",
            fadeIn: "App_fadeIn_77",
            rewardsButton: "App_rewardsButton_f4",
          };
        function Ye(e) {
          engine.call("PlaySound", e);
        }
        const Xe = {
            playHighlight() {
              Ye("highlight");
            },
            playClick() {
              Ye("play");
            },
            playYes() {
              Ye("yes1");
            },
          },
          Ke = {
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
          Ze = [
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
        function Je() {
          return (
            (Je =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Je.apply(this, arguments)
          );
        }
        class eu extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && Ye(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && Ye(this.props.soundClick));
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
              a = e.side,
              r = e.type,
              i = e.classNames,
              o = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              d = e.onMouseUp,
              m =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(e, Ze)),
              E = b()(Ke.base, Ke[`base__${r}`], Ke[`base__${a}`], null == i ? void 0 : i.base),
              _ = b()(Ke.icon, Ke[`icon__${r}`], Ke[`icon__${a}`], null == i ? void 0 : i.icon),
              A = b()(Ke.glow, null == i ? void 0 : i.glow),
              g = b()(Ke.caption, Ke[`caption__${r}`], null == i ? void 0 : i.caption),
              F = b()(Ke.goto, null == i ? void 0 : i.goto);
            return s().createElement(
              "div",
              Je(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                m,
              ),
              "info" !== r && s().createElement("div", { className: Ke.shine }),
              s().createElement(
                "div",
                { className: _ },
                s().createElement("div", { className: A }),
              ),
              s().createElement("div", { className: g }, u),
              n && s().createElement("div", { className: F }, n),
            );
          }
        }
        eu.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const uu = [
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
        function tu(e) {
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
        const nu = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: z.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          au = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              a = e.onMouseEnter,
              s = e.onMouseLeave,
              i = e.onMouseDown,
              o = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              d = e.ignoreMouseClick,
              m = void 0 !== d && d,
              E = e.decoratorId,
              _ = void 0 === E ? 0 : E,
              A = e.isEnabled,
              g = void 0 === A || A,
              F = e.targetId,
              D = void 0 === F ? 0 : F,
              p = e.onShow,
              C = e.onHide,
              B = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, uu);
            const b = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              f = (0, r.useMemo)(
                () =>
                  D ||
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
                [D],
              ),
              h = (0, r.useCallback)(() => {
                (b.current.isVisible && b.current.timeoutId) ||
                  (nu(t, _, { isMouseEvent: !0, on: !0, arguments: tu(n) }, f),
                  p && p(),
                  (b.current.isVisible = !0));
              }, [t, _, n, f, p]),
              v = (0, r.useCallback)(() => {
                if (b.current.isVisible || b.current.timeoutId) {
                  const e = b.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (b.current.timeoutId = 0)),
                    nu(t, _, { on: !1 }, f),
                    b.current.isVisible && C && C(),
                    (b.current.isVisible = !1));
                }
              }, [t, _, f, C]),
              w = (0, r.useCallback)((e) => {
                b.current.isVisible &&
                  ((b.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (b.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(b.current.prevTarget) && v();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = b.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === g && v();
              }, [g, v]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", v),
                  () => {
                    (window.removeEventListener("mouseleave", v), v());
                  }
                ),
                [v],
              ));
            return g
              ? (0, r.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((y = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((b.current.timeoutId = window.setTimeout(h, c ? 100 : 400)),
                            a && a(e),
                            y && y(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (v(), null == s || s(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === m && v(), null == o || o(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === m && v(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    B,
                  ),
                )
              : u;
            var y;
          },
          ru = ["children", "body", "header", "note", "alert", "args"];
        function su() {
          return (
            (su =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            su.apply(this, arguments)
          );
        }
        const iu = R.views.common.tooltip_window.simple_tooltip_content,
          ou = (e) => {
            let u = e.children,
              t = e.body,
              n = e.header,
              a = e.note,
              i = e.alert,
              o = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, ru);
            const c = (0, r.useMemo)(() => {
              const e = Object.assign({}, o, { body: t, header: n, note: a, alert: i });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [i, t, n, a, o]);
            return s().createElement(
              au,
              su(
                {
                  contentId:
                    ((d = null == o ? void 0 : o.hasHtmlContent),
                    d ? iu.SimpleTooltipHtmlContent("resId") : iu.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              u,
            );
            var d;
          },
          lu = R.strings.quests.infoPage,
          cu = (0, Q.Pi)(({ className: e }) => {
            const u = Ve(),
              t = u.model,
              n = u.controls,
              a = t.root.get(),
              r = a.infoVisible,
              i = a.dailyType,
              o = S().mediaSize;
            return s().createElement(
              "div",
              { className: e },
              r
                ? s().createElement(eu, {
                    type: "back",
                    caption: lu.infoButton.back.title(),
                    goto: o >= v.Small ? lu.infoButton.back.goto() : void 0,
                    onClick: n.infoToggle,
                  })
                : s().createElement(
                    ou,
                    {
                      body: lu.infoButtonTooltip.body(),
                      header: lu.infoButtonTooltip.header.$dyn(i),
                    },
                    s().createElement(eu, {
                      type: "info",
                      caption: lu.infoButton.$dyn(i),
                      onClick: n.infoToggle,
                    }),
                  ),
            );
          }),
          du = (e) => {
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
          };
        var mu = t(515);
        const Eu = [];
        function _u(e) {
          const u = (0, r.useRef)(e);
          return (
            (0, r.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, r.useCallback)((...e) => (0, u.current)(...e), Eu)
          );
        }
        function Au(e, u, t = []) {
          const n = (0, r.useRef)(0),
            a = (0, r.useCallback)(() => window.clearInterval(n.current), t || []);
          (0, r.useEffect)(() => a, [a]);
          const s = (null != t ? t : []).concat([u]);
          return [
            (0, r.useCallback)((t) => {
              ((n.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, s),
            a,
          ];
        }
        function gu(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return Fu(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Fu(e, u);
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
        function Fu(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        function Du(e, u, t) {
          const n = (0, r.useMemo)(
            () =>
              (function (e, u, t, n) {
                let a,
                  r = !1,
                  s = 0;
                function i() {
                  a && clearTimeout(a);
                }
                function o(...o) {
                  const l = this,
                    c = Date.now() - s;
                  function d() {
                    ((s = Date.now()), t.apply(l, o));
                  }
                  r ||
                    (n && !a && d(),
                    i(),
                    void 0 === n && c > e
                      ? d()
                      : !0 !== u &&
                        (a = setTimeout(
                          n
                            ? function () {
                                a = void 0;
                              }
                            : d,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
                  (o.cancel = function () {
                    (i(), (r = !0));
                  }),
                  o
                );
              })(t, e),
            u,
          );
          return ((0, r.useEffect)(() => n.cancel, [n]), n);
        }
        let pu;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(pu || (pu = {}));
        const Cu = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          Bu = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: n,
            getWrapperSize: a,
            triggerMouseMoveOnUpdate: s = !1,
          }) => {
            const i = (e, t) => {
              const n = u(e),
                a = n[0],
                r = n[1];
              return (0, mu.u)(a, r, t);
            };
            return (l = {}) => {
              const c = l.settings,
                d = void 0 === c ? Cu : c,
                m = (0, r.useRef)(null),
                E = (0, r.useRef)(null),
                _ = (() => {
                  const e = (0, r.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    n = (e, t) => {
                      u(e).delete(t);
                    },
                    a = (e, ...t) => {
                      for (var n, a = gu(u(e).values()); !(n = a()).done;) (0, n.value)(...t);
                    };
                  return (0, r.useMemo)(() => ({ on: t, off: n, trigger: a }), []);
                })(),
                A = Du(
                  () => {
                    o.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                g = (0, V.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = m.current;
                    u && (t(u, e), _.trigger("change", e), s && A());
                  },
                  onRest: (e) => _.trigger("rest", e),
                  onStart: (e) => _.trigger("start", e),
                  onPause: (e) => _.trigger("pause", e),
                })),
                F = g[0],
                D = g[1],
                p = (0, r.useCallback)(
                  (e, u, t) => {
                    var n;
                    const a = F.scrollPosition.get(),
                      r = (null != (n = F.scrollPosition.goal) ? n : 0) - a;
                    return i(e, u * t + r + a);
                  },
                  [F.scrollPosition],
                ),
                C = (0, r.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = m.current;
                    n &&
                      D.start({
                        scrollPosition: i(n, e),
                        immediate: u,
                        reset: t,
                        config: d.animationConfig,
                        from: { scrollPosition: i(n, F.scrollPosition.get()) },
                      });
                  },
                  [D, d.animationConfig, F.scrollPosition],
                ),
                B = (0, r.useCallback)(
                  (e) => {
                    const u = m.current,
                      t = E.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return a(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, d.step),
                      r = p(u, e, n);
                    C(r);
                  },
                  [C, p, d.step],
                ),
                b = (0, r.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && B(n(e)),
                      m.current && _.trigger("mouseWheel", e, F.scrollPosition, u(m.current)));
                  },
                  [F.scrollPosition, B, _],
                ),
                f = ((e, u = []) => {
                  const t = (0, r.useRef)(),
                    n = (0, r.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, r.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    du(() => {
                      const e = m.current;
                      e &&
                        (C(i(e, F.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [C, F.scrollPosition.goal],
                ),
                h = _u(() => {
                  const e = m.current;
                  if (!e) return;
                  const u = i(e, F.scrollPosition.goal);
                  (u !== F.scrollPosition.goal && C(u, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, r.useEffect)(
                () => (
                  window.addEventListener("resize", f),
                  () => {
                    window.removeEventListener("resize", f);
                  }
                ),
                [f],
              );
              const v = (0, r.useCallback)((e) => _.trigger("isThumbDraggingChanged", e), [_]);
              return (0, r.useMemo)(
                () => ({
                  getWrapperSize: () => (E.current ? a(E.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? u(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: d.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: b,
                  applyScroll: C,
                  applyStepTo: B,
                  contentRef: m,
                  wrapperRef: E,
                  scrollPosition: D,
                  animationScroll: F,
                  recalculateContent: h,
                  handleIsThumbDragging: v,
                  events: { on: _.on, off: _.off },
                }),
                [F.scrollPosition, C, B, v, _.off, _.on, h, b, D, d.step.clampedArrowStepTimeout],
              );
            };
          },
          bu = Bu({
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
            getDirection: (e) => (e.deltaY > 1 ? pu.Next : pu.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          fu = "HorizontalBar_base_49",
          hu = "HorizontalBar_base__nonActive_82",
          vu = "HorizontalBar_leftButton_5f",
          wu = "HorizontalBar_rightButton_03",
          yu = "HorizontalBar_track_0d",
          Su = "HorizontalBar_thumb_fd",
          Tu = "HorizontalBar_rail_32",
          Ru = "disable",
          xu = { pending: !1, offset: 0 },
          Nu = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Pu = () => {},
          ku = (e, u) => Math.max(20, e.offsetWidth * u),
          Mu = (0, r.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Nu, onDrag: n = Pu }) => {
              const a = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                o = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                d = e.stepTimeout || 100,
                m = (0, r.useState)(xu),
                E = m[0],
                _ = m[1],
                A = (0, r.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                g = () => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && u && t && a)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / a),
                    d = (0, mu.u)(0, 1, r / (a - n)),
                    m = (u.offsetWidth - ku(u, s)) * d;
                  ((t.style.transform = `translateX(${0 | m}px)`),
                    ((e) => {
                      if (i.current && o.current && l.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Ru), void o.current.classList.remove(Ru));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(Ru), void o.current.classList.add(Ru));
                        var u, t;
                        (i.current.classList.remove(Ru), o.current.classList.remove(Ru));
                      }
                    })(m));
                },
                F = _u(() => {
                  ((() => {
                    const u = c.current,
                      t = l.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && u && n && t)) return;
                    const s = Math.min(1, n / r);
                    ((u.style.width = `${ku(t, s)}px`),
                      (u.style.display = "flex"),
                      a.current &&
                        (1 === s ? a.current.classList.add(hu) : a.current.classList.remove(hu)));
                  })(),
                    g());
                });
              ((0, r.useEffect)(() => du(F)),
                (0, r.useEffect)(
                  () =>
                    du(() => {
                      const u = () => {
                        g();
                      };
                      let t = Pu;
                      const n = () => {
                        (t(), (t = du(F)));
                      };
                      return (
                        e.events.on("recalculateContent", F),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", n),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", F),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, r.useEffect)(() => {
                  if (!E.pending) return;
                  const u = (u) => {
                      var t;
                      const a = e.contentRef.current;
                      if (!a) return;
                      const r = l.current,
                        s = c.current;
                      if (!a || !r || !s) return;
                      const i = u.screenX - E.offset - r.getBoundingClientRect().x,
                        o = (i / r.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(a, o),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: o }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), A(xu));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, E.offset, E.pending, n, A]));
              const D = Au((u) => e.applyStepTo(u), d, [e]),
                p = D[0],
                C = D[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", C, !0),
                  () => document.removeEventListener("mouseup", C, !0)
                ),
                [C],
              );
              const B = (e) => {
                e.target.classList.contains(Ru) || Ye("highlight");
              };
              return s().createElement(
                "div",
                { className: b()(fu, u.base), ref: a, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: b()(vu, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ru) || 0 !== e.button || (Ye("play"), p(pu.Next));
                  },
                  onMouseUp: C,
                  ref: i,
                  onMouseEnter: B,
                }),
                s().createElement(
                  "div",
                  {
                    className: b()(yu, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((Ye("play"), u.target === n))
                          A({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = c.current,
                              a = e.contentRef.current;
                            if (!n || !a) return;
                            const r = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * u);
                          })(u.screenX > n.getBoundingClientRect().x ? pu.Prev : pu.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: B,
                  },
                  s().createElement("div", { ref: c, className: b()(Su, u.thumb) }),
                  s().createElement("div", { className: b()(Tu, u.rail) }),
                ),
                s().createElement("div", {
                  className: b()(wu, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ru) || 0 !== e.button || (Ye("play"), p(pu.Prev));
                  },
                  onMouseUp: C,
                  ref: o,
                  onMouseEnter: B,
                }),
              );
            },
          ),
          Iu = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Lu = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: a,
            classNames: i,
            scrollClassName: o,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, r.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: b()(Iu.base, e.base) });
              }, [n]),
              m = (0, r.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: b()(Iu.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: b()(Iu.defaultScrollArea, a) },
                s().createElement(Ou, { className: o, api: m, classNames: i }, e),
              ),
              s().createElement(Mu, { getStepByRailClick: l, api: u, onDrag: c, classNames: d }),
            );
          },
          Ou = ({ api: e, className: u, classNames: t, children: n, style: a }) => (
            (0, r.useEffect)(() => du(e.recalculateContent)),
            s().createElement(
              "div",
              { className: b()(Iu.base, u), style: a },
              s().createElement(
                "div",
                {
                  className: b()(Iu.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: b()(Iu.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((Ou.Bar = Mu),
          (Ou.Default = Lu),
          (Ou.SeniorityAwards = ({ api: e, className: u, classNames: t, children: n }) => (
            (0, r.useEffect)(() => du(e.recalculateContent)),
            s().createElement(
              "div",
              { className: b()(Iu.base, u) },
              s().createElement(
                "div",
                { className: b()(Iu.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: b()(Iu.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Hu = Bu({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? pu.Next : pu.Prev),
          }),
          Uu = "VerticalBar_base_f3",
          $u = "VerticalBar_base__nonActive_42",
          Wu = "VerticalBar_topButton_d7",
          zu = "VerticalBar_bottomButton_06",
          Gu = "VerticalBar_track_df",
          qu = "VerticalBar_thumb_32",
          Qu = "VerticalBar_rail_43",
          Vu = "disable",
          ju = () => {},
          Yu = { pending: !1, offset: 0 },
          Xu = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Ku = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          Zu = (e, u) => Math.max(20, e.offsetHeight * u),
          Ju = (0, r.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Xu, onDrag: n = ju }) => {
              const a = (0, r.useRef)(null),
                i = (0, r.useRef)(null),
                o = (0, r.useRef)(null),
                l = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                d = e.stepTimeout || 100,
                m = (0, r.useState)(Yu),
                E = m[0],
                _ = m[1],
                A = (0, r.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                g = _u(() => {
                  const u = c.current,
                    t = l.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && u && t)) return;
                  const s = Math.min(1, n / r);
                  return (
                    (u.style.height = `${Zu(t, s)}px`),
                    u.classList.add(qu),
                    a.current &&
                      (1 === s ? a.current.classList.add($u) : a.current.classList.remove($u)),
                    s
                  );
                }),
                F = _u(() => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && u && t && a)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / a),
                    d = (0, mu.u)(0, 1, r / (a - n)),
                    m = (u.offsetHeight - Zu(u, s)) * d;
                  ((t.style.transform = `translateY(${0 | m}px)`),
                    ((e) => {
                      if (i.current && o.current && l.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Vu), void o.current.classList.remove(Vu));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(Vu), void o.current.classList.add(Vu));
                        var u, t;
                        (i.current.classList.remove(Vu), o.current.classList.remove(Vu));
                      }
                    })(m));
                }),
                D = _u(() => {
                  Ku(e, () => {
                    (g(), F());
                  });
                });
              ((0, r.useEffect)(() => du(D)),
                (0, r.useEffect)(() => {
                  const u = () => {
                    Ku(e, () => {
                      F();
                    });
                  };
                  let t = ju;
                  const n = () => {
                    (t(), (t = du(D)));
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
                }, [e]),
                (0, r.useEffect)(() => {
                  if (!E.pending) return;
                  const u = (u) => {
                      Ku(e, (t) => {
                        const a = l.current,
                          r = c.current,
                          s = e.getContainerSize();
                        if (!a || !r || !s) return;
                        const i = u.screenY - E.offset - a.getBoundingClientRect().y,
                          o = (i / a.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, o),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: r, thumbOffset: i, contentOffset: o }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        A(Yu));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, E.offset, E.pending, n, A]));
              const p = Au((u) => e.applyStepTo(u), d, [e]),
                C = p[0],
                B = p[1];
              (0, r.useEffect)(
                () => (
                  document.addEventListener("mouseup", B, !0),
                  () => document.removeEventListener("mouseup", B, !0)
                ),
                [B],
              );
              const f = (e) => {
                e.target.classList.contains(Vu) || Ye("highlight");
              };
              return s().createElement(
                "div",
                { className: b()(Uu, u.base), ref: a, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: b()(Wu, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Vu) || 0 !== e.button || (Ye("play"), C(pu.Next));
                  },
                  ref: i,
                  onMouseEnter: f,
                }),
                s().createElement(
                  "div",
                  {
                    className: b()(Gu, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((Ye("play"), u.target === n))
                          (e.handleIsThumbDragging(!0),
                            A({ pending: !0, offset: u.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            c.current &&
                              Ku(e, (n) => {
                                if (!n) return;
                                const a = t(e),
                                  r = e.clampPosition(n, n.scrollTop + a * u);
                                e.applyScroll(r);
                              });
                          })(u.screenY > n.getBoundingClientRect().y ? pu.Prev : pu.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: f,
                  },
                  s().createElement("div", { ref: c, className: u.thumb }),
                  s().createElement("div", { className: b()(Qu, u.rail) }),
                ),
                s().createElement("div", {
                  className: b()(zu, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Vu) || 0 !== e.button || (Ye("play"), C(pu.Prev));
                  },
                  onMouseUp: B,
                  ref: o,
                  onMouseEnter: f,
                }),
              );
            },
          ),
          et = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          ut = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: a,
            scrollClassName: i,
            scrollClassNames: o,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, r.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: b()(et.base, e.base) });
              }, [n]),
              m = (0, r.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: b()(et.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: b()(et.area, a) },
                s().createElement(tt, { className: i, classNames: o, api: m }, e),
              ),
              s().createElement(Ju, { getStepByRailClick: l, api: u, onDrag: c, classNames: d }),
            );
          },
          tt = ({ className: e, classNames: u, children: t, api: n }) => (
            (0, r.useEffect)(() => du(n.recalculateContent)),
            s().createElement(
              "div",
              { className: b()(et.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              s().createElement(
                "div",
                { className: b()(et.content, null == u ? void 0 : u.content), ref: n.contentRef },
                t,
              ),
            )
          );
        tt.Default = ut;
        const nt = { Vertical: a, Horizontal: n };
        var at = t(411),
          rt = t(982),
          st = t(649);
        const it = "FormatText_base_d0",
          ot = ({ binding: e, text: u = "", classMix: t, alignment: n = st.v2.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : s().createElement(
                  r.Fragment,
                  null,
                  u.split("\n").map((u, a) =>
                    s().createElement(
                      "div",
                      { className: b()(it, t), key: `${u}-${a}` },
                      (0, st.Uw)(u, n, e).map((e, u) =>
                        s().createElement(r.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                ),
          lt = {
            base: "InfoCard_base_0b",
            base__general: "InfoCard_base__general_fd",
            base__horizontal: "InfoCard_base__horizontal_d3",
            base__horizontalReversed: "InfoCard_base__horizontalReversed_e5",
            image: "InfoCard_image_91",
            container: "InfoCard_container_2d",
            title: "InfoCard_title_96",
            content: "InfoCard_content_b5",
          };
        let ct;
        !(function (e) {
          ((e.Horizontal = "horizontal"),
            (e.HorizontalReversed = "horizontalReversed"),
            (e.General = "general"));
        })(ct || (ct = {}));
        const dt = ({ icon: e, title: u, paragraph: t, cardType: n = ct.General }) =>
            s().createElement(
              "div",
              { className: b()(lt.base, lt[`base__${n}`]) },
              s().createElement("div", {
                className: lt.image,
                style: { backgroundImage: `url(${e})` },
              }),
              s().createElement(
                "div",
                { className: lt.container },
                s().createElement(ot, { text: u, classMix: lt.title }),
                s().createElement(ot, { text: t, classMix: lt.content }),
              ),
            ),
          mt = R.strings.quests.infoPage,
          Et = R.images.gui.maps.icons.missions.icons,
          _t = (...e) => e.filter((e) => e.length).join("\n"),
          At = "InfoPage_base_dd",
          gt = "InfoPage_scrollContent_4d",
          Ft = "InfoPage_scrollBar_f7",
          Dt = "InfoPage_content_24",
          pt = "InfoPage_missionsDescription_ba",
          Ct = "InfoPage_generalDescription_9b",
          Bt = "InfoPage_separator_44",
          bt = "InfoPage_title_bd";
        function ft() {
          return (
            (ft =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            ft.apply(this, arguments)
          );
        }
        const ht = R.strings.quests.infoPage,
          vt = (0, Q.Pi)(() => {
            const e = Ve().model,
              u = e.root.get(),
              t = u.dailyType,
              n = u.isBattlePassActive,
              a = u.isComp7Active,
              r = e.computes.isEnabledSubscription(),
              i = e.daily.get().rerollTimeout,
              o = Hu(),
              l = S().mediaSize,
              c =
                t === U.Default
                  ? ((e, u, t, n) => {
                      const a = n >= v.Medium ? Et.big : Et,
                        r = u ? mt.dailyMissions.subscription.default() : "";
                      return {
                        missionsDescription: [
                          {
                            cardType: ct.HorizontalReversed,
                            icon: e ? a.daily_bp_active() : a.daily(),
                            title: mt.dailyMissionTitle(),
                            paragraph: _t(
                              e
                                ? mt.dailyMissions.battlePassDailyMissions.default()
                                : mt.dailyMissions.default(),
                              r,
                            ),
                          },
                          {
                            cardType: ct.Horizontal,
                            icon: a.premium(),
                            title: mt.premiumMissionsTitle(),
                            paragraph: mt.premiumMissions.default(),
                          },
                        ],
                        generalDescription: [
                          {
                            icon: Et.pm_info_2(),
                            title: mt.conditionsTitle(),
                            paragraph: mt.conditions.default(),
                          },
                          {
                            icon: Et.dq_info_3(),
                            title: mt.bonusMissionTitle(),
                            paragraph: mt.bonusMission.default(),
                          },
                          {
                            icon: Et.pm_info_3(),
                            title: mt.epicRewardsTitle(),
                            paragraph: mt.epicRewards.default(),
                          },
                          {
                            icon: Et.dq_info_2(),
                            title: mt.missionSwitchTitle(),
                            paragraph: (0, rt.G)(
                              ((s = t),
                              s % 3600 > 0 ? mt.missionSwitch_min() : mt.missionSwitch_hrs()),
                              t,
                            ),
                          },
                        ],
                      };
                      var s;
                    })(n, r, i, l)
                  : ((e, u, t, n, a) => {
                      const r = a >= v.Medium ? Et.big : Et,
                        s = n ? mt.dailyMissions.subscription.default() : "";
                      return {
                        missionsDescription: [
                          {
                            cardType: ct.HorizontalReversed,
                            icon: t ? r.daily_bp_active() : r.daily(),
                            title: mt.dailyMissionTitle(),
                            paragraph: _t(
                              t
                                ? mt.dailyMissions.battlePassDailyMissions.winback()
                                : mt.dailyMissions.winback(),
                              s,
                            ),
                          },
                          {
                            cardType: ct.Horizontal,
                            icon: r.premium(),
                            title: mt.premiumMissionsTitle(),
                            paragraph: u
                              ? mt.premiumMissions.winback_comp7Active()
                              : mt.premiumMissions.winback(),
                          },
                        ],
                        generalDescription: [
                          {
                            icon: Et.pm_info_2(),
                            title: mt.conditionsTitle(),
                            paragraph: u
                              ? mt.conditions.winback_comp7Active()
                              : mt.conditions.winback(),
                          },
                          {
                            icon: Et.dq_info_3(),
                            title: mt.bonusMissionTitle(),
                            paragraph: mt.bonusMission.winback(),
                          },
                          {
                            icon: Et.pm_info_3(),
                            title: mt.epicRewardsTitle(),
                            paragraph: mt.epicRewards.winback(),
                          },
                          {
                            icon: Et.dq_info_2(),
                            title: mt.missionSwitchTitle(),
                            paragraph: mt.missionSwitch.winback(),
                          },
                        ],
                      };
                    })(0, a, n, r, l);
            return s().createElement(
              "div",
              { className: At },
              s().createElement(
                nt.Vertical.Area.Default,
                { api: o, scrollClassNames: { content: gt }, barClassNames: { base: Ft } },
                s().createElement(
                  "div",
                  null,
                  s().createElement("div", { className: bt }, ht.header.$dyn(t)),
                  s().createElement(
                    "div",
                    { className: Dt },
                    s().createElement(
                      "div",
                      { className: pt },
                      c.missionsDescription.map((e, u) => s().createElement(dt, ft({ key: u }, e))),
                    ),
                    s().createElement("div", { className: Bt }),
                    s().createElement(
                      "div",
                      { className: Ct },
                      c.generalDescription.map((e, u) => s().createElement(dt, ft({ key: u }, e))),
                    ),
                  ),
                ),
              ),
            );
          }),
          wt = "Disabled_base_13",
          yt = "Disabled_alert_f6",
          St = "Disabled_icon_43",
          Tt = "Disabled_info_e1",
          Rt = R.strings.menu.browser.dataUnavailable,
          xt = () =>
            s().createElement(
              "div",
              { className: wt },
              s().createElement(
                "div",
                { className: yt },
                s().createElement("div", { className: St }),
                Rt.header(),
              ),
              s().createElement("div", { className: Tt }, Rt.description()),
            ),
          Nt = s().memo;
        const Pt = {
            base: "HorizontalTabs_base_92",
            tab: "HorizontalTabs_tab_ca",
            tab__medium: "HorizontalTabs_tab__medium_88",
            tab__active: "HorizontalTabs_tab__active_3e",
            tab__nonInteractive: "HorizontalTabs_tab__nonInteractive_ce",
            state: "HorizontalTabs_state_3d",
            highlight: "HorizontalTabs_highlight_9e",
            border: "HorizontalTabs_border_08",
            border__left: "HorizontalTabs_border__left_64",
            border__right: "HorizontalTabs_border__right_45",
            divider: "HorizontalTabs_divider_6f",
            title: "HorizontalTabs_title_10",
            notification: "HorizontalTabs_notification_89",
            notification__symbol: "HorizontalTabs_notification__symbol_8b",
            notification__small: "HorizontalTabs_notification__small_7c",
            notification__large: "HorizontalTabs_notification__large_a2",
            notification__dot: "HorizontalTabs_notification__dot_d7",
            notification__medium: "HorizontalTabs_notification__medium_19",
          },
          kt = { mouseEnter: "highlight", click: "play" },
          Mt = (e, { active: u, enableInteractiveActiveTab: t = !1 }) => !!t || e !== u,
          It = Nt(function (e) {
            const u = e.active,
              t = e.tabs,
              n = e.onClick,
              a = e.onMouseEnter,
              r = e.onMouseLeave,
              i = e.className,
              o = e.classNames,
              l = e.sounds,
              c = void 0 === l ? kt : l,
              d = (u) => () => {
                Mt(u, e) && (c.click && Ye(c.click), null == n || n(u));
              },
              m = (u) => () => {
                Mt(u, e) && (c.mouseEnter && Ye(c.mouseEnter), null == a || a(u));
              },
              E = (u) => () => {
                Mt(u, e) && (c.mouseLeave && Ye(c.mouseLeave), null == r || r(u));
              };
            return s().createElement(
              "div",
              { className: b()(Pt.base, i) },
              t.map(({ id: n, title: a, notification: r }, i) => {
                var l;
                return s().createElement(
                  "div",
                  {
                    className: b()(
                      Pt.tab,
                      n === u && b()(Pt.tab__active, null == o ? void 0 : o.activeTab),
                      !Mt(n, e) && Pt.tab__nonInteractive,
                      null == o ? void 0 : o.tab,
                    ),
                    key: n,
                    onClick: d(n),
                    onMouseEnter: m(n),
                    onMouseLeave: E(n),
                  },
                  ((e, u) => !((e, u) => e.length - 1 === u)(e, u))(t, i) &&
                    s().createElement("div", {
                      className: b()(Pt.divider, null == o ? void 0 : o.divider),
                    }),
                  s().createElement(
                    "div",
                    { className: b()(Pt.state, null == o ? void 0 : o.state) },
                    s().createElement("div", {
                      className: b()(Pt.highlight, null == o ? void 0 : o.highlight),
                    }),
                    s().createElement("div", {
                      className: b()(
                        Pt.border,
                        Pt.border__left,
                        null == o ? void 0 : o.border,
                        null == o ? void 0 : o.borderLeft,
                      ),
                    }),
                    s().createElement("div", {
                      className: b()(
                        Pt.border,
                        Pt.border__right,
                        null == o ? void 0 : o.border,
                        null == o ? void 0 : o.borderRight,
                      ),
                    }),
                  ),
                  s().createElement(
                    "div",
                    { className: b()(Pt.title, null == o ? void 0 : o.title) },
                    a,
                  ),
                  void 0 !== r &&
                    s().createElement(
                      "div",
                      {
                        className: b()(
                          Pt.notification,
                          Pt[`notification__${r.type}`],
                          Pt[`notification__${null != (l = r.size) ? l : "medium"}`],
                          null == o ? void 0 : o.notification,
                        ),
                      },
                      "dot" !== r.type && r.value,
                    ),
                );
              }),
            );
          });
        var Lt = t(255),
          Ot = t(122);
        const Ht = {
            questsContainer: "styles_questsContainer_79",
            questsContainer__winback: "styles_questsContainer__winback_4d",
          },
          Ut = "BonusCard_base_95",
          $t = "BonusCard_glow_f0",
          Wt = "BonusCard_wrapper_c4",
          zt = "BonusCard_flag_6d",
          Gt = "BonusCard_content_6f",
          qt = ["children"];
        function Qt() {
          return (
            (Qt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Qt.apply(this, arguments)
          );
        }
        const Vt = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, qt);
          return s().createElement(
            au,
            Qt(
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
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            jt.apply(this, arguments)
          );
        }
        const Yt = ({ children: e, tooltipArgs: u, className: t }) => {
            if (!u) return e;
            const n = s().createElement("div", { className: t }, e);
            if (u.header || u.body) return s().createElement(ou, u, n);
            const a = u.contentId,
              r = u.args,
              i = null == r ? void 0 : r.contentId;
            return a || i
              ? s().createElement(au, jt({}, u, { contentId: a || i }), n)
              : s().createElement(Vt, u, n);
          },
          Xt = {
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
          Kt = ({
            name: e,
            image: u,
            isPeriodic: t = !1,
            size: n = X.Big,
            special: a,
            value: r,
            valueType: i,
            style: o,
            className: l,
            classNames: c,
            tooltipArgs: d,
            periodicIconTooltipArgs: m,
          }) => {
            const E = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Z.BATTLE_BOOSTER:
                  case Z.BATTLE_BOOSTER_REPLACE:
                    return J.BATTLE_BOOSTER;
                }
              })(a),
              _ = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Z.BATTLE_BOOSTER:
                    return ee.BATTLE_BOOSTER;
                  case Z.BATTLE_BOOSTER_REPLACE:
                    return ee.BATTLE_BOOSTER_REPLACE;
                  case Z.BUILT_IN_EQUIPMENT:
                    return ee.BUILT_IN_EQUIPMENT;
                  case Z.EQUIPMENT_PLUS:
                    return ee.EQUIPMENT_PLUS;
                  case Z.EQUIPMENT_TROPHY_BASIC:
                    return ee.EQUIPMENT_TROPHY_BASIC;
                  case Z.EQUIPMENT_TROPHY_UPGRADED:
                    return ee.EQUIPMENT_TROPHY_UPGRADED;
                  case Z.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return ee.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case Z.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return ee.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case Z.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return ee.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case Z.PROGRESSION_STYLE_UPGRADED_1:
                    return ee.PROGRESSION_STYLE_UPGRADED_1;
                  case Z.PROGRESSION_STYLE_UPGRADED_2:
                    return ee.PROGRESSION_STYLE_UPGRADED_2;
                  case Z.PROGRESSION_STYLE_UPGRADED_3:
                    return ee.PROGRESSION_STYLE_UPGRADED_3;
                  case Z.PROGRESSION_STYLE_UPGRADED_4:
                    return ee.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(a),
              A = ((e, u) => {
                if (void 0 === e) return null;
                switch (u) {
                  case K.MULTI: {
                    const u = Number(e);
                    return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
                  }
                  case K.CURRENCY:
                  case K.NUMBER:
                    return s().createElement(ne, { format: "integral", value: Number(e) });
                  case K.PREMIUM_PLUS: {
                    const u = Number(e);
                    return isNaN(u) ? e : null;
                  }
                  default:
                    return e;
                }
              })(r, i);
            return s().createElement(
              "div",
              { className: b()(Xt.base, Xt[`base__${n}`], l), style: o },
              s().createElement(
                Yt,
                { tooltipArgs: d, className: Xt.tooltipWrapper },
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement(
                    "div",
                    { className: b()(Xt.image, null == c ? void 0 : c.image) },
                    E &&
                      s().createElement("div", {
                        className: b()(Xt.highlight, null == c ? void 0 : c.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${E}_highlight)`,
                        },
                      }),
                    u &&
                      s().createElement("div", {
                        className: b()(Xt.icon, null == c ? void 0 : c.rewardIcon),
                        style: { backgroundImage: `url(${u})` },
                      }),
                    _ &&
                      s().createElement("div", {
                        className: b()(Xt.overlay, null == c ? void 0 : c.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${_}_overlay)`,
                        },
                      }),
                  ),
                  A &&
                    s().createElement(
                      "div",
                      {
                        className: b()(
                          Xt.info,
                          Xt[`info__${e}`],
                          i === K.MULTI && Xt.info__multi,
                          null == c ? void 0 : c.info,
                        ),
                      },
                      A,
                    ),
                ),
              ),
              t &&
                s().createElement(
                  Yt,
                  { tooltipArgs: m },
                  s().createElement("div", {
                    className: b()(Xt.timer, null == c ? void 0 : c.periodicIcon),
                  }),
                ),
            );
          },
          Zt = "Rewards_base_26",
          Jt = "Rewards_base__vertical_9f",
          en = "Rewards_reward_7b",
          un = "Rewards_reward__vertical_c6";
        function tn() {
          return (
            (tn =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            tn.apply(this, arguments)
          );
        }
        const nn = s().memo(
          ({
            data: e,
            size: u = X.Big,
            isVertical: t = !1,
            count: n,
            classMix: a,
            rewardItemClassMix: i,
            boxRewardTooltip: o,
            boxRewardValue: l,
          }) => {
            const c = (0, r.useMemo)(
                () =>
                  n && n < e.length ? `R.images.gui.maps.icons.quests.bonuses.${u}.default` : "",
                [n, e.length, u],
              ),
              d =
                l ||
                (0, st.uF)(R.strings.tooltips.quests.awards.additional.bottom(), {
                  count: e.length - (n || 0),
                }),
              m = b()(Zt, t && Jt, a),
              E = b()(en, t && un, i);
            return s().createElement(
              "div",
              { className: m },
              c
                ? s().createElement(
                    s().Fragment,
                    null,
                    e
                      .slice(0, n)
                      .map((e, t) =>
                        s().createElement(
                          "div",
                          { key: t, className: E },
                          s().createElement(Kt, tn({ size: u }, e)),
                        ),
                      ),
                    s().createElement(
                      "div",
                      { className: E },
                      s().createElement(Kt, {
                        name: "more",
                        image: c,
                        size: u,
                        value: d,
                        tooltipArgs: o,
                      }),
                    ),
                  )
                : e.map((e, t) =>
                    s().createElement(
                      "div",
                      { key: t, className: E },
                      s().createElement(Kt, tn({ size: u }, e)),
                    ),
                  ),
            );
          },
        );
        var an = t(438);
        const rn = {
            base: "Transition_base_f1",
            component: "Transition_component_9a",
            fadeIn: "Transition_fadeIn_c5",
            lock: "Transition_lock_58",
            zoomOut: "Transition_zoomOut_f4",
            lock__big: "Transition_lock__big_c0",
            background: "Transition_background_e2",
            fadeInBg: "Transition_fadeInBg_ed",
            background__big: "Transition_background__big_a0",
          },
          sn = (0, r.memo)(({ delay: e, isEnabled: u = !0, size: t = X.Small, children: n }) =>
            u
              ? s().createElement(
                  "div",
                  { className: rn.base },
                  s().createElement("div", {
                    className: b()(rn.lock, rn[`lock__${t}`]),
                    style: { animationDelay: `${e + 300}ms, ${e + 400}ms` },
                  }),
                  s().createElement("div", {
                    className: b()(rn.background, rn[`background__${t}`]),
                    style: { animationDelay: `${e + 400}ms` },
                  }),
                  s().createElement(
                    "div",
                    { className: rn.component, style: { animationDelay: `${e + 400}ms` } },
                    n,
                  ),
                )
              : n,
          ),
          on = {
            base: "BonusReward_base_3a",
            base__locked: "BonusReward_base__locked_52",
            subscriptionRewardBackground: "BonusReward_subscriptionRewardBackground_45",
            subscriptionRewardBackground__big: "BonusReward_subscriptionRewardBackground__big_fb",
            subscriptionRewardBackground__animated:
              "BonusReward_subscriptionRewardBackground__animated_0d",
            lockedIcon: "BonusReward_lockedIcon_39",
            lockedIcon__big: "BonusReward_lockedIcon__big_1f",
            reward: "BonusReward_reward_eb",
          };
        function ln() {
          return (
            (ln =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            ln.apply(this, arguments)
          );
        }
        const cn = R.strings.subscription,
          dn = ({
            data: e,
            isUnlockedQuestReward: u = !1,
            size: t = X.Small,
            isClosedRewardOnCompletedQuest: n = !1,
            animationDelay: a = 0,
            isAnimatedUnlock: i = !1,
          }) => {
            (0, r.useEffect)(() => {
              i &&
                setTimeout(() => {
                  Ye("dq_subscription_reward_unlock");
                }, a);
            }, []);
            const o = u
              ? b()(
                  on.subscriptionRewardBackground,
                  on[`subscriptionRewardBackground__${t}`],
                  i && on.subscriptionRewardBackground__animated,
                )
              : b()(on.lockedIcon, on[`lockedIcon__${t}`]);
            return s().createElement(
              "div",
              { className: on.base },
              e.map((e, r) =>
                s().createElement(
                  ou,
                  {
                    isEnabled: n,
                    header: cn.dailyQuestsLockedReward.header(),
                    body: cn.dailyQuestsLockedReward.body(),
                    key: r,
                  },
                  ((e, n) =>
                    e
                      ? s().createElement(
                          "div",
                          { className: on.reward },
                          s().createElement("div", { className: o }),
                          s().createElement(
                            "div",
                            { className: u ? "" : on.base__locked },
                            s().createElement(Kt, ln({ size: t }, n)),
                          ),
                        )
                      : s().createElement(
                          sn,
                          { delay: a, isEnabled: i, size: t },
                          s().createElement(
                            Yt,
                            {
                              tooltipArgs: u
                                ? n.tooltipArgs
                                : {
                                    contentId:
                                      R.views.lobby.daily.tooltips.LockedSubscriptionBonusTooltip(
                                        "resId",
                                      ),
                                  },
                            },
                            s().createElement(
                              "div",
                              { className: on.reward },
                              s().createElement("div", { className: o }),
                              s().createElement(
                                "div",
                                { className: u ? "" : on.base__locked },
                                s().createElement(Kt, ln({ size: t }, n)),
                              ),
                            ),
                          ),
                        ))(n, e),
                ),
              ),
            );
          },
          mn = "Content_base_b4",
          En = "Content_header_92",
          _n = "Content_title_39",
          An = "Content_countDownContainer_ec",
          gn = "Content_timer_78",
          Fn = "Content_countDown_ae",
          Dn = "Content_missionIcon_65",
          pn = "Content_battleConditions_e0",
          Cn = "Content_text_b9",
          Bn = "Content_progressInfo_85",
          bn = "Content_progressBar_e8",
          fn = "Content_rewards_4a";
        let hn;
        !(function (e) {
          ((e[(e.BIG = 80)] = "BIG"),
            (e[(e.MEDIUM = 48)] = "MEDIUM"),
            (e[(e.SMALL = 32)] = "SMALL"));
        })(hn || (hn = {}));
        const vn = R.images.gui.maps.icons.missions.icons,
          wn = R.strings.quests.dailyQuests.bonusQuest,
          yn = (e) => (e >= v.Large ? hn.BIG : e >= v.Medium ? hn.MEDIUM : hn.SMALL),
          Sn = (0, Q.Pi)(() => {
            const e = Ve().model,
              u = e.root.get().countDown,
              t = (0, r.useContext)(lr).isExiting,
              n = S().mediaSize,
              a = ge(e.dailyQuests.get(), 3);
            if (void 0 === a) throw new Error("There is no bonus quest in daily quests");
            const i = a.bonusCondition,
              o = a.id,
              l = a.postBattleCondition,
              c = a.bonuses,
              d = a.subscriptionBonuses,
              m = a.isActiveSubscription,
              E = a.isEnabledSubscription,
              _ = a.icon,
              A = a.status,
              g = a.isFirstView,
              F = Ne(i, l),
              D = n >= v.Large ? X.Big : X.Small,
              p = xe(c, o, D),
              C = xe(d, o, D),
              B = Le(t, -10, {
                leave: { opacity: 1, config: { duration: 400, easing: Me.easeInCubic } },
                delay: t ? 100 : 300,
              });
            return s().createElement(
              "div",
              { className: mn },
              B(
                (e, t) =>
                  !t &&
                  s().createElement(
                    V.animated.div,
                    { style: e, className: En },
                    s().createElement("div", { className: _n }, wn.bonusMissionTitle()),
                    s().createElement(
                      "div",
                      { className: An },
                      s().createElement("div", { className: gn }),
                      s().createElement(at.Z, {
                        startValue: u,
                        hourFormat: wn.countDown_hrs(),
                        minuteFormat: wn.countDown_minSec(),
                        pendingDotCount: 8,
                        className: Fn,
                      }),
                    ),
                  ),
              ),
              s().createElement(
                "div",
                { className: pn },
                s().createElement("div", {
                  className: Dn,
                  style: { backgroundImage: `url(${vn.$dyn(`c_${yn(n)}_${_}_silver`)})` },
                }),
                void 0 !== F &&
                  s().createElement(an.L, {
                    conditions: F,
                    missionId: o,
                    columns: !0,
                    reverse: !0,
                    swapProgress: !0,
                    classNames: { text: Cn, progressInfo: Bn, progressBar: bn },
                  }),
              ),
              s().createElement(
                "div",
                { className: fn },
                s().createElement(nn, {
                  size: D,
                  data: p,
                  count: ((b = p.length), (f = 3), b > f ? f - 1 : void 0),
                }),
                E &&
                  s().createElement(dn, {
                    data: C,
                    size: D,
                    isUnlockedQuestReward:
                      (m && A !== Ae.UndoneSubscription) || (!m && A === Ae.Done),
                    isClosedRewardOnCompletedQuest: A === Ae.UndoneSubscription,
                    isAnimatedUnlock: g && A === Ae.Active && m,
                  }),
              ),
            );
            var b, f;
          }),
          Tn = {
            from: { opacity: 0, transform: "translateY(-200rem) scaleX(0.15) scaleY(0.15)" },
            enter: {
              opacity: 1,
              transform: "translateY(0rem) scaleX(1) scaleY(1)",
              config: { duration: 800, easing: Me.easeOutQuint },
            },
            leave: {
              opacity: 0,
              transform: "translateY(0rem) scaleX(1) scaleY(1)",
              config: { duration: 100, easing: Me.easeInCubic },
              delay: 300,
            },
          },
          Rn = ({ bonusQuestCompleted: e, isFirstAppearing: u }) => {
            const t = (0, r.useContext)(lr).isExiting,
              n = t || e,
              a = Ie(n, {
                enter: { pointerEvents: "none", config: { duration: 400, easing: Me.easeOutCirc } },
                leave: { config: { duration: 300, easing: Me.easeInCubic } },
                delay: n ? (e ? 2300 : 0) : 600,
              }),
              i = Le(e, 20, {
                from: { opacity: 1, transform: "translateY(0rem)", pointerEvents: "auto" },
                delay: e ? 2300 : 0,
              }),
              o = Le(
                t,
                20,
                Object.assign(
                  {},
                  u ? Tn : { from: { transform: "translateY(0rem)" }, delay: t ? 100 : 200 },
                ),
              ),
              l = Le(
                t,
                -30,
                Object.assign(
                  {},
                  u
                    ? {
                        enter: { config: { duration: 800, easing: Me.easeOutQuint } },
                        leave: {
                          transform: "translateY(-20rem)",
                          opacity: 0,
                          config: { duration: 300, easing: Me.easeInCubic },
                        },
                      }
                    : {
                        from: { transform: "translateY(-20rem)" },
                        enter: {
                          transform: "translateY(0rem)",
                          config: { duration: 600, easing: Me.easeOutCirc },
                        },
                        leave: { transform: "translateY(20rem)" },
                      },
                  { delay: t ? 100 : 400 },
                ),
              );
            return s().createElement(
              "div",
              { className: Ut },
              a((e, u) => !u && s().createElement(V.animated.div, { style: e, className: $t })),
              i(
                (e, u) =>
                  !u &&
                  s().createElement(
                    V.animated.div,
                    { style: e, className: Wt },
                    o(
                      (e, u) =>
                        !u && s().createElement(V.animated.div, { style: e, className: zt }),
                    ),
                    l(
                      (e, u) =>
                        !u &&
                        s().createElement(
                          V.animated.div,
                          { style: e, className: Gt },
                          s().createElement(Sn, null),
                        ),
                    ),
                  ),
              ),
            );
          },
          xn = "AllCompleteCountdown_base_ab",
          Nn = "AllCompleteCountdown_title_90",
          Pn = "AllCompleteCountdown_subTitle_2b",
          kn = "AllCompleteCountdown_timer_47",
          Mn = "AllCompleteCountdown_timerDecoration_7b",
          In = "AllCompleteCountdown_timerDecoration__left_4e",
          Ln = "AllCompleteCountdown_timerCountdown_2d",
          On = (0, Q.Pi)(() => {
            const e = Ve().model,
              u = (0, r.useContext)(lr),
              t = u.previousTabIndex,
              n = u.isExiting,
              a = e.root.get().countDown,
              i = Te(t);
            if (void 0 === i)
              throw new Error("Can not show content for undefined content resource name.");
            const o = R.strings.quests.$dyn(i).$dyn("countDown"),
              l = Le(n, 50, { delay: n ? 300 : 200 }),
              c = Oe(n, -50),
              d = Oe(n, 50);
            return l(
              (e, u) =>
                !u &&
                s().createElement(
                  V.animated.div,
                  { style: e, className: xn },
                  s().createElement("div", { className: Nn }, o.$dyn("title")),
                  s().createElement(
                    "div",
                    { className: kn },
                    c(
                      (e, u) =>
                        !u &&
                        s().createElement(
                          V.animated.div,
                          { style: e },
                          s().createElement("div", { className: b()(Mn, In) }),
                        ),
                    ),
                    s().createElement(at.Z, { startValue: a, className: Ln }),
                    d(
                      (e, u) =>
                        !u &&
                        s().createElement(
                          V.animated.div,
                          { style: e },
                          s().createElement("div", { className: Mn }),
                        ),
                    ),
                  ),
                  s().createElement("div", { className: Pn }, o.$dyn("remainingText")),
                ),
            );
          }),
          Hn = {
            bonusCard: "DailyQuests_bonusCard_c0",
            bonusCard__winback: "DailyQuests_bonusCard__winback_44",
          };
        var Un = t(374),
          $n = t(229);
        const Wn = "BattleCondition_base_b4",
          zn = "BattleCondition_text_a6",
          Gn = "BattleCondition_base__prem_e6",
          qn = "BattleCondition_progressInfo_1a",
          Qn = "BattleCondition_progressBar_b9",
          Vn = (0, Q.Pi)(({ quest: e, className: u, isPremium: t }) => {
            const n = Ne(e.bonusCondition, e.postBattleCondition);
            return n
              ? s().createElement(
                  "div",
                  { className: b()(Wn, t && Gn, u) },
                  s().createElement(an.L, {
                    conditions: n,
                    inlineOperator: !0,
                    columns: !0,
                    size: $n.$.BIG,
                    missionId: e.id,
                    swapProgress: !0,
                    reverse: !0,
                    classNames: { text: zn, progressInfo: qn, progressBar: Qn },
                  }),
                )
              : null;
          }),
          jn = {
            base: "Card_base_09",
            base__done: "Card_base__done_dc",
            base__undoneSubscription: "Card_base__undoneSubscription_a3",
            base__notAvailable: "Card_base__notAvailable_b8",
            base__prem: "Card_base__prem_cb",
            borderTop: "Card_borderTop_ee",
            borderAnimationWrapper: "Card_borderAnimationWrapper_7a",
            borderAnimation: "Card_borderAnimation_1f",
            "border-anim": "Card_border-anim_3d",
            completedAnimationBg: "Card_completedAnimationBg_fc",
            "bg-blink": "Card_bg-blink_8e",
            cardIcon: "Card_cardIcon_29",
            condition: "Card_condition_f1",
            rewardsWrapper: "Card_rewardsWrapper_40",
            premiumLock: "Card_premiumLock_3b",
            rerollButton: "Card_rerollButton_06",
            statusIcon: "Card_statusIcon_2b",
            statusIcon__animated: "Card_statusIcon__animated_9d",
            "completed-icon": "Card_completed-icon_0d",
            arrow: "Card_arrow_64",
            arrow__done: "Card_arrow__done_44",
            arrow__undoneSubscription: "Card_arrow__undoneSubscription_3f",
          },
          Yn = "RerollButton_base_22",
          Xn = "RerollButton_base__disabled_2c",
          Kn = "RerollButton_text_a3",
          Zn = "RerollButton_icons_98",
          Jn = "RerollButton_icon_2b",
          ea = "RerollButton_iconHover_5c",
          ua = "RerollButton_iconDisabled_64",
          ta = (0, Q.Pi)(({ canReroll: e, questId: u, className: t }) => {
            const n = Ve().controls,
              a = (0, r.useContext)(lr).isExiting;
            return s().createElement(
              au,
              {
                ignoreMouseClick: !e,
                contentId: R.views.lobby.missions.legacy.RerollTooltipWithCountdown("resId"),
                isEnabled: !a && !e,
              },
              s().createElement(
                "div",
                {
                  className: b()(Yn, t, !e && Xn),
                  onClick: e ? () => n.reroll(u) : void 0,
                  onMouseEnter: e ? () => Ye(R.sounds.highlight()) : void 0,
                },
                e &&
                  s().createElement(
                    "div",
                    { className: Kn },
                    R.strings.quests.dailyQuests.body.reroll(),
                  ),
                s().createElement(
                  "div",
                  { className: Zn },
                  e
                    ? s().createElement(
                        s().Fragment,
                        null,
                        s().createElement("div", { className: Jn }),
                        s().createElement("div", { className: ea }),
                      )
                    : s().createElement("div", { className: ua }),
                ),
              ),
            );
          }),
          na = (e, u) => (e === Ae.Active && u ? "prem" : e),
          aa = R.strings.quests.premiumQuests.tooltips.locked,
          ra = ({
            quest: e,
            isRerolling: u,
            isRerollEnabled: t,
            isRerollAvailable: n,
            isVisited: a,
            isPremium: i,
            className: o,
            index: l,
          }) => {
            const c = S().mediaSize,
              d = (0, r.useContext)(lr).isExiting,
              m = !i && t && e.status === Ae.Active,
              E = 400 + 300 * (3 + l - 1),
              _ = d || u;
            return Le(_, 20, {
              enter: { config: { duration: 300, easing: Me.easeOutCirc } },
              delay: _ ? (u ? 1e3 : 200 * l) : u ? 0 : 400 + 200 * l,
            })(
              (u, t) =>
                !t &&
                s().createElement(
                  V.animated.div,
                  { style: u, className: b()(jn.base, o, jn[`base__${na(e.status, i)}`]) },
                  s().createElement("div", { className: jn.borderTop }),
                  (e.status === Ae.Done || e.status === Ae.UndoneSubscription) &&
                    !a &&
                    s().createElement(
                      s().Fragment,
                      null,
                      s().createElement(
                        "div",
                        { className: jn.borderAnimationWrapper },
                        s().createElement("div", { className: jn.borderAnimation }),
                      ),
                      s().createElement("div", { className: b()(jn.completedAnimationBg) }),
                    ),
                  s().createElement("div", { className: jn.cardIcon, style: Re(c, e.icon, i) }),
                  s().createElement(Vn, { className: jn.condition, quest: e, isPremium: i }),
                  s().createElement(
                    "div",
                    { className: jn.rewardsWrapper },
                    s().createElement(nn, { size: e.rewardSize, data: e.bonuses }),
                    e.isEnabledSubscription &&
                      !i &&
                      s().createElement(dn, {
                        data: e.subscriptionBonuses,
                        size: e.rewardSize,
                        isUnlockedQuestReward:
                          (e.isActiveSubscription && e.status !== Ae.UndoneSubscription) ||
                          (!e.isActiveSubscription && e.status === Ae.Done),
                        isClosedRewardOnCompletedQuest: e.status === Ae.UndoneSubscription,
                        animationDelay: E,
                        isAnimatedUnlock:
                          e.isFirstView && e.status === Ae.Active && e.isActiveSubscription,
                      }),
                  ),
                  i &&
                    e.status === Ae.Locked &&
                    s().createElement(
                      ou,
                      { ignoreMouseClick: !0, isEnabled: !d, body: aa.body(), header: aa.header() },
                      s().createElement("div", { className: jn.premiumLock }),
                    ),
                  m &&
                    s().createElement(ta, {
                      className: jn.rerollButton,
                      canReroll: n,
                      questId: e.id,
                    }),
                  (e.status === Ae.Done || e.status === Ae.UndoneSubscription) &&
                    s().createElement("div", {
                      className: b()(jn.statusIcon, !a && jn.statusIcon__animated),
                    }),
                  i &&
                    2 !== l &&
                    s().createElement("div", {
                      className: b()(jn.arrow, jn[`arrow__${e.status}`]),
                    }),
                ),
            );
          },
          sa = "Cards_base_ee",
          ia = "Cards_card_c2",
          oa = { opacity: 1, transform: "translateY(0rem)", pointerEvents: "auto" },
          la = (0, Q.Pi)(({ isOutAnimation: e, delayOut: u }) => {
            const t = S().mediaSize,
              n = Ve().model,
              a = n.computes.getRerolledCardsIds,
              i = (0, r.useContext)(lr).previousTabIndex,
              o = n.computes.getQuests(i, t),
              l = (0, r.useState)(o),
              c = l[0],
              d = l[1],
              m = (0, r.useState)([]),
              E = m[0],
              _ = m[1];
            (0, r.useEffect)(() => {
              const e = a(c, o);
              if (e.length > 0)
                return (
                  Ye(R.sounds.dq_screen_quest_reroll()),
                  _(e),
                  (0, Ot.F)(() => {
                    (d(o), _([]));
                  }, 1500)
                );
              d(o);
            }, [a, c, o]);
            const A = (0, V.useSpring)(() => oa),
              g = A[0],
              F = A[1];
            return (
              (0, r.useEffect)(() => {
                if (e)
                  return (0, Ot.F)(() => {
                    F.start({
                      opacity: 0,
                      transform: "translateY(20rem)",
                      pointerEvents: "none",
                      config: { duration: 300, easing: Me.easeInCirc },
                    });
                  }, u);
                F.start(
                  Object.assign({}, oa, { config: { duration: 200, easing: Me.easeOutCirc } }),
                );
              }, [F, e, u]),
              s().createElement(
                V.animated.div,
                { style: g, className: sa },
                c.map((e, u) => {
                  var t;
                  return s().createElement(ra, {
                    key: e.id,
                    className: ia,
                    isPremium: i === ye.PremiumQuests,
                    index: u,
                    quest: e,
                    isRerolling: E.includes(e.id),
                    isRerollEnabled: n.daily.get().rerollEnabled,
                    isRerollAvailable: n.daily.get().rerollCountDown <= 0,
                    isVisited: null == (t = n.computes.isCardVisited(i, u)) || t,
                  });
                }),
              )
            );
          }),
          ca = "AnimatedFlag_base_e5",
          da = s().memo(({ baseQuestsCompleted: e }) => {
            const u = S().mediaSize >= v.Medium,
              t = (0, V.useSpring)({
                x: e ? 1 : 0,
                transform: e
                  ? `translateY(${u ? "-450rem" : "-240rem"}) scale(1.3, 1.3)`
                  : `translateY(0rem) scale(${u ? "0.8, 0.8" : "0.6, 0.6"})`,
                config: { duration: 1e3, easing: Me.easeOutCubic },
                delay: 2e3,
              }),
              n = t.x,
              a = t.transform;
            return s().createElement(V.animated.div, {
              style: {
                opacity: n.to({ range: [0, 0.4, 0.7, 1], output: [0, 0, 0.8, 0] }),
                transform: a,
              },
              className: ca,
            });
          }),
          ma = "LockedBonusQuest_base_51",
          Ea = "LockedBonusQuest_flag_27",
          _a = "LockedBonusQuest_bonusMissionDescription_d0",
          Aa = "LockedBonusQuest_lockIcon_5e",
          ga = "LockedBonusQuest_text_aa",
          Fa = "LockedBonusQuest_styleLine_b1",
          Da = "LockedBonusQuest_styleLine__left_4b",
          pa = "LockedBonusQuest_styleLine__right_22",
          Ca = R.strings.quests.dailyQuests,
          Ba = s().memo(({ baseQuestsCompleted: e }) => {
            const u = (0, r.useContext)(lr).isExiting,
              t = Le(u, 20, { delay: u ? 0 : 150 }),
              n = (0, V.useSpring)({
                from: { opacity: 1 },
                to: { opacity: 0 },
                cancel: !e,
                reset: !e,
                config: { duration: 300, easing: Me.easeInCirc },
                delay: 1700,
              });
            return s().createElement(
              V.animated.div,
              { style: n },
              t(
                (e, u) =>
                  !u &&
                  s().createElement(
                    V.animated.div,
                    { style: e, className: ma },
                    s().createElement("div", { className: Ea }),
                    s().createElement(
                      ou,
                      {
                        ignoreMouseClick: !0,
                        isEnabled: !u,
                        header: Ca.bonus.tooltipTitle(),
                        body: Ca.bonus.tooltipDescription(),
                      },
                      s().createElement(
                        "div",
                        { className: _a },
                        s().createElement("div", { className: Aa }),
                        s().createElement(
                          "div",
                          { className: ga },
                          Ca.bonusQuest.bonusMissionTitle(),
                        ),
                      ),
                    ),
                    s().createElement("div", { className: b()(Fa, Da) }),
                    s().createElement("div", { className: b()(Fa, pa) }),
                  ),
              ),
            );
          }),
          ba = "MainContent_base_67",
          fa = "MainContent_lockedBonusQuest_89",
          ha = "MainContent_animatedFlag_d1",
          va = "MainContent_countDownContainer_32",
          wa = "MainContent_timer_72",
          ya = "MainContent_countDown_3b",
          Sa = (0, Q.Pi)(({ baseQuestsCompleted: e }) => {
            const u = Ve().model.daily.get().rerollCountDown,
              t =
                (n = u) < Un.yR
                  ? R.strings.quests.general.countdown.text.timer_sec()
                  : n < Un.dV
                    ? R.strings.quests.general.countdown.text.timer_min()
                    : R.strings.quests.general.countdown.text.timer_hrs();
            var n;
            const a = (0, r.useContext)(lr).isExiting,
              i = Ie(e);
            return s().createElement(
              "div",
              { className: ba },
              u > 0 &&
                s().createElement(
                  au,
                  {
                    ignoreMouseClick: !0,
                    isEnabled: !a && u > 0,
                    contentId: R.views.lobby.missions.legacy.RerollTooltip("resId"),
                  },
                  i(
                    (e, n) =>
                      !n &&
                      s().createElement(
                        V.animated.div,
                        { style: e, className: va },
                        s().createElement("div", { className: wa }),
                        s().createElement("div", { className: ya }, (0, rt.G)(t, u)),
                      ),
                  ),
                ),
              s().createElement(la, { isOutAnimation: e, delayOut: 1500 }),
              s().createElement(
                "div",
                { className: fa },
                s().createElement(
                  "div",
                  { className: ha },
                  s().createElement(da, { baseQuestsCompleted: e }),
                ),
                s().createElement(Ba, { baseQuestsCompleted: e }),
              ),
            );
          }),
          Ta = (0, Q.Pi)(() => {
            var e, u;
            const t = Ve().model,
              n = (0, r.useContext)(lr).isExiting,
              a = t.root.get().dailyType,
              i = t.daily.get().bonusMissionVisited,
              o = t.computes.getDailyQuestsCompletedVisited(),
              l = t.dailyQuests.get(),
              c = Pe(l),
              d = null != (e = (0, Lt.D9)(c)) ? e : c,
              m = 4 === c,
              E = 3 === c,
              _ = ke(o) >= 3,
              A = (0, r.useState)(!1),
              g = A[0],
              F = A[1],
              D = (0, r.useState)(!!(c >= 3 && o[3]) && i),
              p = D[0],
              C = D[1],
              B = (0, r.useState)(
                m && null != (u = t.computes.isCardVisited(ye.DailyQuests, 3)) && u,
              ),
              f = B[0],
              h = B[1];
            return (
              (0, r.useEffect)(() => {
                if (E && l.length > 3) {
                  if ((F(!0), !i)) {
                    const e = (0, Ot.F)(() => Ye(R.sounds.dq_screen_bonus_quest_unlock()), 1600),
                      u = (0, Ot.F)(() => C(!0), 3e3);
                    return () => {
                      (e(), u());
                    };
                  }
                  C(!0);
                }
              }, [i, E, l.length]),
              (0, r.useEffect)(() => {
                void 0 !== d &&
                  d >= 3 &&
                  c < 3 &&
                  (Ye(R.sounds.dq_screen_switch()), F(!1), C(!1), h(!1));
              }, [c, d]),
              (0, r.useEffect)(() => {
                if (m && !o[3].value)
                  return (
                    Ye(R.sounds.dq_screen_bonus_quest_complete()),
                    (0, Ot.F)(() => {
                      h(!0);
                    }, 2600)
                  );
              }, [m, o]),
              (0, r.useEffect)(() => {
                n || m || (_ && !(c > d)) || Ye(R.sounds.dq_screen_quest_complete());
              }, [n, m, _, c, d]),
              f
                ? s().createElement(On, null)
                : p && l.length > 3
                  ? s().createElement(
                      "div",
                      { className: b()(Hn.bonusCard, Hn[`bonusCard__${a}`]) },
                      s().createElement(Rn, { bonusQuestCompleted: m, isFirstAppearing: !i }),
                    )
                  : s().createElement(
                      "div",
                      { className: b()(Ht.questsContainer, Ht[`questsContainer__${a}`]) },
                      s().createElement(Sa, { baseQuestsCompleted: g }),
                    )
            );
          }),
          Ra = {
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
        let xa, Na;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(xa || (xa = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(Na || (Na = {})));
        const Pa = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: a,
          mixClass: i,
          soundHover: o,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: d,
          onMouseDown: m,
          onMouseUp: E,
          onMouseLeave: _,
          onClick: A,
        }) => {
          const g = (0, r.useRef)(null),
            F = (0, r.useState)(t),
            D = F[0],
            p = F[1],
            C = (0, r.useState)(!1),
            B = C[0],
            f = C[1],
            h = (0, r.useState)(!1),
            v = h[0],
            w = h[1],
            y = (0, r.useCallback)(() => {
              a || (g.current && (g.current.focus(), p(!0)));
            }, [a]),
            S = (0, r.useCallback)(
              (e) => {
                D && null !== g.current && !g.current.contains(e.target) && p(!1);
              },
              [D],
            ),
            T = (0, r.useCallback)(
              (e) => {
                a || (A && A(e));
              },
              [a, A],
            ),
            x = (0, r.useCallback)(
              (e) => {
                a || (null !== o && Ye(o), c && c(e), w(!0));
              },
              [a, o, c],
            ),
            N = (0, r.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            P = (0, r.useCallback)(
              (e) => {
                a || (E && E(e), f(!1));
              },
              [a, E],
            ),
            k = (0, r.useCallback)(
              (e) => {
                a || (null !== l && Ye(l), m && m(e), t && y(), f(!0));
              },
              [a, l, m, y, t],
            ),
            M = (0, r.useCallback)(
              (e) => {
                a || (_ && _(e), f(!1));
              },
              [a, _],
            ),
            I = b()(
              Ra.base,
              Ra[`base__${n}`],
              {
                [Ra.base__disabled]: a,
                [Ra[`base__${u}`]]: u,
                [Ra.base__focus]: D,
                [Ra.base__highlightActive]: B,
                [Ra.base__firstHover]: v,
              },
              i,
            ),
            L = b()(Ra.state, Ra.state__default);
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
              p(t);
            }, [t]),
            s().createElement(
              "div",
              {
                ref: g,
                className: I,
                onMouseEnter: x,
                onMouseMove: N,
                onMouseUp: P,
                onMouseDown: k,
                onMouseLeave: M,
                onClick: T,
              },
              n !== xa.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: Ra.back }),
                  s().createElement("span", { className: Ra.texture }),
                ),
              s().createElement(
                "span",
                { className: L },
                s().createElement("span", { className: Ra.stateDisabled }),
                s().createElement("span", { className: Ra.stateHighlightHover }),
                s().createElement("span", { className: Ra.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: Ra.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Pa.defaultProps = {
          type: xa.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const ka = (0, r.memo)(Pa),
          Ma = "NotPremiumAccount_base_31",
          Ia = "NotPremiumAccount_image_4a",
          La = "NotPremiumAccount_title_4f",
          Oa = "NotPremiumAccount_text_06",
          Ha = "NotPremiumAccount_button_75",
          Ua = R.strings.quests.premiumQuests.notPremiumAccount,
          $a = (0, Q.Pi)(({ isPremiumChanging: e }) => {
            const u = Ve().controls,
              t = (0, r.useContext)(lr).isExiting;
            return Le(t || e, 20, {
              delay: 100,
              enter: { config: { duration: 300, easing: Me.easeOutCirc } },
            })(
              (e, t) =>
                !t &&
                s().createElement(
                  V.animated.div,
                  { style: e, className: Ma },
                  s().createElement("div", { className: Ia }),
                  s().createElement(ot, { text: Ua.title(), classMix: La }),
                  s().createElement(ot, { text: Ua.paragraph(), classMix: Oa }),
                  s().createElement(
                    ka,
                    { type: xa.main, size: Na.medium, mixClass: Ha, onClick: u.buyPremiumBtnClick },
                    Ua.button(),
                  ),
                ),
            );
          }),
          Wa = (0, Q.Pi)(() => {
            const e = Ve().model,
              u = e.root.get().dailyType,
              t = e.premium.get().isPremiumAccount,
              n = e.computes.getPremiumQuestsCompletedVisited(),
              a = e.premiumQuests.get(),
              i = Pe(a),
              o = (0, Lt.D9)(i),
              l = 3 === i,
              c = ke(n),
              d = e.computes.isCardVisited(ye.PremiumQuests, 2),
              m = void 0 !== d && !d,
              E = (0, r.useState)(l && !m),
              _ = E[0],
              A = E[1];
            ((0, r.useEffect)(() => {
              if (l && m)
                return (
                  Ye(R.sounds.dq_screen_premium_missions_all_complete()),
                  (0, Ot.F)(() => {
                    A(!0);
                  }, 3500)
                );
            }, [l, m]),
              (0, r.useEffect)(() => {
                3 === o && i < 3 && (Ye(R.sounds.dq_screen_switch()), A(!1));
              }, [o, i]),
              (0, r.useEffect)(() => {
                const e = i - c;
                e > 0 && e < 3 && Ye(R.sounds.dq_screen_premium_missions_complete());
              }, [i, c]));
            const g = (0, Lt.tp)(t, 500),
              F = g !== t;
            return g
              ? _
                ? s().createElement(On, null)
                : s().createElement(
                    "div",
                    { className: b()(Ht.questsContainer, Ht[`questsContainer__${u}`]) },
                    s().createElement(la, { isOutAnimation: l || F, delayOut: F ? 0 : 2400 }),
                  )
              : s().createElement($a, { isPremiumChanging: F });
          });
        var za = t(875);
        const Ga = "Progress_base_55",
          qa = "Progress_infoContainer_ca",
          Qa = "Progress_missionsCompleted_73",
          Va = "Progress_title_a4",
          ja = "Progress_description_aa",
          Ya = "Progress_current_af",
          Xa = "Progress_separator_7e",
          Ka = "Progress_checkIcon_9d",
          Za = "Progress_rewardsWrapper_c7",
          Ja = "Progress_progressWrapper_7c",
          er = "Progress_footerSeparator_08",
          ur = "Progress_disabled_af",
          tr = "Progress_alertIcon_f5",
          nr = "Progress_alertText_63",
          ar = Object.assign({}, za.uu, {
            delta: { delay: 100, duration: 2e3 },
            line: { delay: 100, duration: 2e3 },
          }),
          rr = R.strings.quests.dailyQuests.footer,
          sr = (0, Q.Pi)(() => {
            const e = Ve().model,
              u = S().mediaSize,
              t = e.epicQuest.get(),
              n = t.id,
              a = t.earned,
              i = t.total,
              o = t.isEnabled,
              l = t.current,
              c = e.epicQuestBonuses.get(),
              d = u >= v.Large ? X.Big : X.Small;
            (0, r.useEffect)(() => {
              a > 0 && o && Ye(R.sounds.dq_screen_progress_bar());
            }, [a, o]);
            const m = (0, V.useSpring)({
              from: { opacity: 0, transform: "translateY(20rem)" },
              to: { opacity: 1, transform: "translateY(0rem)" },
              config: { duration: 600, easing: Me.easeOutQuint },
            });
            return s().createElement(
              V.animated.div,
              { style: m, className: Ga },
              s().createElement("div", { className: er }),
              o
                ? s().createElement(
                    s().Fragment,
                    null,
                    s().createElement(
                      "div",
                      { className: qa },
                      s().createElement(
                        "div",
                        { className: Qa },
                        s().createElement(
                          "div",
                          { className: Va },
                          rr.title(),
                          s().createElement("div", { className: Ya }, l),
                          s().createElement("div", { className: Xa }, "/"),
                          i,
                          s().createElement("div", { className: Ka }),
                        ),
                        s().createElement("div", { className: ja }, rr.paragraph()),
                      ),
                      s().createElement(nn, {
                        data: xe(c, n, d),
                        size: u >= v.Large ? X.Big : X.Small,
                        classMix: Za,
                      }),
                    ),
                    s().createElement(
                      "div",
                      { className: Ja },
                      s().createElement(za.ko, {
                        animationSettings: ar,
                        value: l,
                        deltaFrom: l - a,
                        maxValue: i,
                      }),
                    ),
                  )
                : s().createElement(
                    "div",
                    { className: ur },
                    s().createElement("div", { className: tr }),
                    s().createElement(
                      "div",
                      { className: nr },
                      R.strings.menu.browser.dataUnavailable.description(),
                    ),
                  ),
            );
          }),
          ir = {
            base: "QuestsContent_base_39",
            header: "QuestsContent_header_71",
            fadeIn: "QuestsContent_fadeIn_31",
            title: "QuestsContent_title_ec",
            tab: "QuestsContent_tab_18",
            content: "QuestsContent_content_bb",
          },
          or = R.strings.quests,
          lr = (0, r.createContext)({}),
          cr = (0, Q.Pi)(() => {
            const e = Ve(),
              u = e.model,
              t = e.controls,
              n = u.root.get().dailyType,
              a = u.computes.getCurrentTabIndex(),
              i = u.computes.getTabs();
            if (void 0 === a) throw new Error("Can not show quests for undefined tab index.");
            const o = (0, Lt.tp)(a, 500),
              l = (0, r.useMemo)(() => ({ isExiting: o !== a, previousTabIndex: o }), [o, a]);
            return s().createElement(
              lr.Provider,
              { value: l },
              s().createElement(
                "div",
                { className: ir.base },
                s().createElement(
                  "div",
                  { className: ir.header },
                  s().createElement("div", { className: ir.title }, or.dailyQuests.header.$dyn(n)),
                  s().createElement(It, {
                    tabs: i,
                    active: a,
                    onClick: (e) => {
                      (Ye(R.sounds.dq_screen_switch()), t.tabClick(e));
                    },
                    classNames: { tab: ir.tab },
                  }),
                ),
                s().createElement(
                  "div",
                  { className: ir.content },
                  (() => {
                    switch (o) {
                      case ye.DailyQuests:
                        return s().createElement(Ta, null);
                      case ye.PremiumQuests:
                        return s().createElement(Wa, null);
                      default:
                        return (console.error(`Unreachable branch in tabs index: ${o}`), null);
                    }
                  })(),
                ),
                s().createElement(
                  "div",
                  { className: ir.progress },
                  n === U.Default
                    ? s().createElement(sr, null)
                    : (console.error(`Unreachable branch in progress type: ${n}`), null),
                ),
              ),
            );
          }),
          dr = {
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
          mr =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          Er = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          _r = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          Ar = (0, r.memo)(({ text: e, binding: u, classMix: t }) => {
            const n = (0, r.useCallback)((e) => ({ color: `#${e}` }), []),
              a = (0, r.useMemo)(() => u || {}, [u]);
            let i = mr.exec(e),
              o = e,
              l = 0;
            for (; i;) {
              const t = i[0],
                r = Er.exec(t),
                c = _r.exec(t),
                d = i[1];
              if (r && c) {
                const e = r[0],
                  i = e + l++ + e;
                ((o = o.replace(t, `%(${i})`)),
                  (a[i] = dr[e]
                    ? s().createElement(
                        "span",
                        { className: dr[e] },
                        s().createElement(ot, { text: d, binding: u }),
                      )
                    : s().createElement(
                        "span",
                        { style: n(e) },
                        s().createElement(ot, { text: d, binding: u }),
                      )));
              }
              i = mr.exec(e);
            }
            return s().createElement(ot, { text: o, classMix: t, binding: a });
          }),
          gr = R.strings.common.duration,
          Fr = {
            base: "TakeRewards_base_ac",
            base__disabled: "TakeRewards_base__disabled_ae",
            button: "TakeRewards_button_d4",
            border: "TakeRewards_border_d7",
            glow: "TakeRewards_glow_16",
            content: "TakeRewards_content_49",
            buttonIcon: "TakeRewards_buttonIcon_a9",
            hightlightWrapper: "TakeRewards_hightlightWrapper_0f",
            hightlight: "TakeRewards_hightlight_21",
            slide: "TakeRewards_slide_10",
            countdown: "TakeRewards_countdown_6c",
            countdownIcon: "TakeRewards_countdownIcon_77",
          },
          Dr = { [$.AVAILABLE]: "active", [$.NO_OFFERS]: "hidden", [$.DISABLED]: "disabled" },
          pr = R.strings.quests.dailyQuests.takeRewardsButton,
          Cr = (0, Q.Pi)(({ className: e }) => {
            const u = Ve(),
              t = u.model,
              n = u.controls,
              a = t.root.get(),
              r = a.getRewardsTimeLeft,
              i = a.offersState,
              o = i === $.DISABLED,
              l = ((e, u = !0) =>
                e.days > 7 && u
                  ? (0, st.WU)(gr.days(), { days: e.days })
                  : e.days >= 1
                    ? (0, st.WU)(gr.days(), { days: 0 === e.hours ? e.days : e.days + 1 })
                    : e.hours >= 1
                      ? (0, st.WU)(gr.hours(), { hours: 0 === e.minutes ? e.hours : e.hours + 1 })
                      : (0, st.WU)(gr.minutes(), { minutes: e.minutes || 1 }))((0, Un.f8)(r), !1);
            return s().createElement(
              "div",
              { className: b()(Fr.base, e, Fr[`base__${Dr[i]}`]) },
              s().createElement(
                ou,
                { body: o ? pr.tooltipDisable() : pr.tooltip() },
                s().createElement(
                  "div",
                  {
                    className: Fr.button,
                    onClick: o
                      ? void 0
                      : () => {
                          (Xe.playClick(), n.claimRewards());
                        },
                    onMouseEnter: o ? void 0 : Xe.playHighlight,
                  },
                  !o &&
                    s().createElement(
                      s().Fragment,
                      null,
                      s().createElement("div", { className: Fr.border }),
                      s().createElement("div", { className: Fr.glow }),
                    ),
                  s().createElement(
                    "div",
                    { className: Fr.content },
                    s().createElement("div", { className: Fr.buttonIcon }),
                    pr.text(),
                  ),
                  !o &&
                    s().createElement(
                      "div",
                      { className: Fr.hightlightWrapper },
                      s().createElement("div", { className: Fr.hightlight }),
                    ),
                ),
              ),
              !o &&
                r > 0 &&
                s().createElement(
                  "div",
                  { className: Fr.countdown },
                  s().createElement("div", { className: Fr.countdownIcon }),
                  s().createElement(Ar, { text: pr.countdown(), binding: { leftTime: l } }),
                ),
            );
          }),
          Br = (0, Q.Pi)(() => {
            var e;
            const u = Ve(),
              t = u.model,
              n = u.controls,
              a = t.root.get(),
              r = a.infoVisible,
              i = a.offersState;
            var o;
            ((o = r ? n.infoToggle : n.close), q(W.n.ESCAPE, o));
            const l = null != (e = Te(t.computes.getCurrentTabIndex())) ? e : "",
              c = (0, V.useTransition)(l, {
                from: { opacity: 0 },
                enter: { opacity: 1 },
                leave: { opacity: 0 },
                delay: 200,
              });
            return 0 === t.computes.getEnabledFeatures().length
              ? s().createElement(xt, null)
              : s().createElement(
                  "div",
                  { className: b()(je.base, je[`base__${l}`]) },
                  c((e, u) =>
                    s().createElement(V.animated.div, {
                      style: e,
                      className: b()(je.background, je[`background__${u}`]),
                    }),
                  ),
                  r
                    ? s().createElement(vt, null)
                    : s().createElement(
                        s().Fragment,
                        null,
                        s().createElement(cr, null),
                        i &&
                          i !== $.NO_OFFERS &&
                          s().createElement(Cr, { className: je.rewardsButton }),
                      ),
                  s().createElement(cu, {
                    className: b()(je.infoButton, !r && je.infoButton__info),
                  }),
                );
          });
        engine.whenReady.then(() => {
          H().render(
            s().createElement(L, null, s().createElement(Qe, null, s().createElement(Br, null))),
            document.getElementById("root"),
          );
        });
      },
      438: (e, u, t) => {
        "use strict";
        t.d(u, { L: () => k });
        var n = t(483),
          a = t.n(n),
          r = t(179),
          s = t.n(r);
        const i = "BattleConditions_base_3c",
          o = "BattleConditions_base__big_fd",
          l = "BattleConditions_description_97",
          c = "BattleConditions_operator_43",
          d = "BattleConditions_base__huge_92",
          m = "BattleConditions_base__reverse_1a",
          E = "BattleConditions_condition_e2",
          _ = "BattleConditions_base__bolded_92",
          A = "BattleConditions_conditionBlockColumn_c7",
          g = "BattleConditions_conditionBlockRow_a8",
          F = "BattleConditions_description_inlineOperator_34",
          D = "BattleConditions_progress_c0",
          p = "BattleConditions_progress__completed_1b",
          C = "BattleConditions_progress_current_fa",
          B = "BattleConditions_progress_separator_d0",
          b = "BattleConditions_progress_total_62",
          f = "BattleConditions_progressBarWrapper_85",
          h = "BattleConditions_timingFunction_8f";
        var v = t(875),
          w = t(736);
        const y = ({
            conditionData: e,
            children: u,
            swapProgress: t,
            progressBarStyles: n,
            progressInfoStyles: i,
            progressBarTheme: o,
            classNames: l,
          }) => {
            const c = e.current,
              d = e.earned,
              m = e.total,
              _ = a()(D, { [p]: c === m }),
              A = (0, r.useMemo)(
                () =>
                  Object.assign({}, v.uu, {
                    line: { delay: 1e3, duration: 1e3 },
                    delta: { className: h, delay: 200, duration: 1e3 },
                  }),
                [],
              ),
              g = t
                ? s().createElement(
                    s().Fragment,
                    null,
                    s().createElement(
                      "div",
                      { className: a()(f, null == l ? void 0 : l.progressBar), style: n },
                      s().createElement(v.ko, {
                        size: w.$.Small,
                        value: c,
                        deltaFrom: c - d,
                        maxValue: m,
                        animationSettings: A,
                        theme: o,
                      }),
                    ),
                    s().createElement(
                      "div",
                      { className: a()(_, null == l ? void 0 : l.progressInfo), style: i },
                      s().createElement("div", { className: C }, c),
                      s().createElement("div", { className: B }, "/"),
                      s().createElement("div", { className: b }, m),
                    ),
                  )
                : s().createElement(
                    s().Fragment,
                    null,
                    s().createElement(
                      "div",
                      { className: a()(_, null == l ? void 0 : l.progressInfo), style: i },
                      s().createElement("div", { className: C }, c),
                      s().createElement("div", { className: B }, "/"),
                      s().createElement("div", { className: b }, m),
                    ),
                    s().createElement(
                      "div",
                      { className: a()(f, null == l ? void 0 : l.progressBar), style: n },
                      s().createElement(v.ko, {
                        size: w.$.Small,
                        value: c,
                        deltaFrom: c - d,
                        maxValue: m,
                        animationSettings: A,
                        theme: o,
                      }),
                    ),
                  );
            return s().createElement("div", { className: E }, m > 0 && g, u);
          },
          S = R.strings.quests.dailyQuests.postBattle.genericAmpersand(),
          T = R.strings.quests.dailyQuests.postBattle.and(),
          x = ({
            conditions: e,
            missionId: u,
            columns: t,
            depth: n,
            inlineOperator: r,
            align: i,
            swapProgress: o,
            progressBarStyles: d,
            textStyles: m,
            progressInfoStyles: E,
            progressBarTheme: _,
            inlineOperatorStyles: D,
            useAmpersand: p,
            classNames: C,
          }) => {
            if (e.items.length <= 0 || (void 0 !== n && 0 === n)) return null;
            const B = Object.assign({}, m, { textAlign: `${i}` });
            return s().createElement(
              "div",
              { className: t ? A : g },
              e.items.map(({ value: A }, g) => {
                const b = ((e, u, t, n) => {
                  const a = { processMore: !0, showOperator: !1, isFirstCondition: !1 };
                  if (u.items) t < e.items.length - 1 && (a.showOperator = !0);
                  else {
                    if (void 0 !== n) {
                      for (let u = t + 1; u < e.items.length; u++)
                        if (!e.items[u].value.items || (e.items[u].value.items && n - 1 != 0)) {
                          a.showOperator = !0;
                          break;
                        }
                    } else t < e.items.length - 1 && (a.showOperator = !0);
                    ((a.processMore = !1), t || (a.isFirstCondition = !0));
                  }
                  return a;
                })(e, A, g, n);
                let f = A.descrData;
                if (f && b.isFirstCondition) {
                  f = `${systemLocale.toUpperCase(f[0])}${f.slice(1)}`;
                }
                return s().createElement(
                  s().Fragment,
                  { key: `${u}_${g}` },
                  b.processMore
                    ? s().createElement(x, {
                        conditions: A,
                        missionId: u,
                        columns: !t,
                        depth: n ? n - 1 : void 0,
                        inlineOperator: r,
                        align: i,
                        swapProgress: o,
                        progressBarStyles: d,
                        progressBarTheme: _,
                        textStyles: m,
                        progressInfoStyles: E,
                        inlineOperatorStyles: D,
                        useAmpersand: p,
                        classNames: C,
                      })
                    : s().createElement(
                        y,
                        {
                          conditionData: A,
                          swapProgress: o,
                          progressBarStyles: d,
                          progressInfoStyles: E,
                          progressBarTheme: _,
                          classNames: {
                            progressBar: null == C ? void 0 : C.progressBar,
                            progressInfo: null == C ? void 0 : C.progressInfo,
                          },
                        },
                        b.showOperator && r
                          ? s().createElement(
                              "div",
                              { className: a()(l, null == C ? void 0 : C.text), style: m },
                              f,
                              s().createElement(
                                "span",
                                { className: F, style: D },
                                "and" === e.conditionType && p ? S : T,
                              ),
                            )
                          : s().createElement(
                              "div",
                              { className: a()(l, null == C ? void 0 : C.text), style: B },
                              f,
                            ),
                      ),
                  b.showOperator &&
                    !r &&
                    s().createElement(
                      "div",
                      { className: c },
                      "and" === e.conditionType && p ? S : T,
                    ),
                );
              }),
            );
          },
          N = x;
        var P = t(229);
        const k = ({
          conditions: e,
          columns: u,
          depth: t,
          size: n,
          reverse: r,
          isBold: l,
          inlineOperator: c,
          align: E,
          swapProgress: A,
          missionId: g,
          progressBarStyles: F,
          progressBarTheme: D,
          textStyles: p,
          progressInfoStyles: C,
          inlineOperatorStyles: B,
          useAmpersand: b,
          className: f,
          classNames: h,
        }) => {
          if (0 === e.items.length) return null;
          const v = a()(i, f, { [o]: n === P.$.BIG, [d]: n === P.$.HUGE, [m]: r, [_]: l });
          return s().createElement(
            "div",
            { className: v },
            s().createElement(N, {
              conditions: e,
              missionId: g,
              columns: u,
              depth: t,
              inlineOperator: c,
              align: E,
              swapProgress: A,
              progressBarStyles: F,
              progressBarTheme: D,
              inlineOperatorStyles: B,
              textStyles: p,
              progressInfoStyles: C,
              useAmpersand: b,
              classNames: h,
            }),
          );
        };
        k.defaultProps = { align: P.I.CENTER, swapProgress: !1, isBold: !1, columns: !1 };
      },
      229: (e, u, t) => {
        "use strict";
        let n, a;
        (t.d(u, { $: () => a, I: () => n }),
          (function (e) {
            ((e.LEFT = "left"), (e.RIGHT = "right"), (e.CENTER = "center"));
          })(n || (n = {})),
          (function (e) {
            ((e.BIG = "big"), (e.HUGE = "huge"));
          })(a || (a = {})));
      },
      411: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => l });
        var n = t(374),
          a = t(255),
          r = t(179),
          s = t.n(r),
          i = t(982),
          o = t(963);
        const l = ({
          startValue: e,
          hourFormat: u = R.strings.quests.general.countdown.timer_hrs(),
          minuteFormat: t = R.strings.quests.general.countdown.timer_min(),
          roundUpHours: r = !1,
          pendingDotCount: l = 5,
          className: c,
        }) => {
          const d = e > n.dV + n.yR ? n.yR : 1,
            m = (0, a.au)(e, d);
          return s().createElement(
            "div",
            { className: c },
            m > 0
              ? ((e, u, t, a) => {
                  const r = e < n.dV ? t : u;
                  return (0, i.G)(r, e, a);
                })(m, u, t, r)
              : s().createElement(o.Z, { count: l, delay: 500 }),
          );
        };
      },
      963: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var n = t(179),
          a = t.n(n);
        const r = ({ className: e, count: u, delay: t }) => {
          const r = (0, n.useState)(1),
            s = r[0],
            i = r[1];
          return (
            (0, n.useEffect)(() => {
              const e = setInterval(() => {
                i((e) => (e <= u ? e + 1 : 1));
              }, t);
              return () => {
                clearInterval(e);
              };
            }),
            a().createElement("span", { className: e }, ". ".repeat(s))
          );
        };
      },
      982: (e, u, t) => {
        "use strict";
        t.d(u, { G: () => n });
        const n = (e, u, t) => {
          const n = Math.floor(u / 3600).toString(),
            a = Math.floor((u % 3600) / 60).toString(),
            r = Math.floor(u % 60).toString();
          return e
            .replace("%HH", n.padStart(2, "0"))
            .replace("%H", t && Number(a) >= 30 ? (Number(n) + 1).toString() : n)
            .replace("%MM", a.padStart(2, "0"))
            .replace("%M", a.toString())
            .replace("%SS", r.padStart(2, "0"))
            .replace("%S", r);
        };
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
          for (var [u, t, n] = deferred[o], r = !0, s = 0; s < u.length; s++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((r = !1), n < a && (a = n));
          if (r) {
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
    (__webpack_require__.j = 476),
    (() => {
      var e = { 476: 0, 320: 0, 428: 0, 993: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            a,
            [r, s, i] = t,
            o = 0;
          if (r.some((u) => 0 !== e[u])) {
            for (n in s) __webpack_require__.o(s, n) && (__webpack_require__.m[n] = s[n]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < r.length; o++)
            ((a = r[o]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [45], () => __webpack_require__(181));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
