(() => {
  "use strict";
  var e,
    n = {
      875: (e, n, t) => {
        t.d(n, { ko: () => q, uu: () => T });
        var a = t(483),
          r = t.n(a),
          s = t(179),
          o = t.n(s);
        const i = {
          base: "ProgressBar_base_45",
          base__medium: "ProgressBar_base__medium_62",
          base__small: "ProgressBar_base__small_df",
          background: "ProgressBar_background_51",
          background__medium: "ProgressBar_background__medium_6e",
          background__small: "ProgressBar_background__small_46",
          lineWrapper: "ProgressBar_lineWrapper_6a",
        };
        var l = t(736);
        const m = ({ size: e = l.$.Default, classMix: n }) =>
            o().createElement("div", { className: r()(i.background, i[`background__${e}`], n) }),
          d = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          u = ({ size: e }) => {
            const n = r()(d.base, d[`base__${e}`]);
            return o().createElement("div", { className: n });
          },
          c = {
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
          g = (0, s.memo)(
            ({
              size: e,
              lineRef: n,
              disabled: t,
              baseStyles: a,
              isComplete: s,
              withoutBounce: i,
            }) => {
              const l = r()(
                  c.base,
                  c[`base__${e}`],
                  t && c.base__disabled,
                  s && c.base__finished,
                  i && c.base__withoutBounce,
                ),
                m = !t && !s;
              return o().createElement(
                "div",
                { className: l, style: a, ref: n },
                o().createElement("div", { className: c.pattern }),
                o().createElement("div", { className: c.gradient }),
                m && o().createElement(u, { size: e }),
              );
            },
          ),
          f = ({ size: e, value: n, lineRef: t, disabled: a, onComplete: r }) => {
            const i = (0, s.useMemo)(() => ({ width: `${n}%`, transitionProperty: "none" }), [n]),
              l = 100 === n;
            return (
              (0, s.useEffect)(() => {
                l && r && r();
              }, [l, r]),
              o().createElement(g, {
                size: e,
                disabled: a,
                baseStyles: i,
                isComplete: l,
                lineRef: t,
              })
            );
          };
        var b = t(122);
        let p, _;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(p || (p = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(_ || (_ = {})));
        const h = "ProgressBarDeltaSimple_base_6c",
          E = "ProgressBarDeltaSimple_delta_99",
          w = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: n,
              freezed: t,
              from: a,
              size: r,
              to: i,
              onEndAnimation: l,
              onChangeAnimationState: m,
            }) => {
              const d = i < a,
                c = (0, s.useState)(_.Idle),
                g = c[0],
                f = c[1],
                p = g === _.In,
                w = g === _.End,
                y = g === _.Idle,
                v = (0, s.useCallback)(
                  (e) => {
                    (f(e), m && m(e));
                  },
                  [m],
                );
              ((0, s.useEffect)(() => {
                if (y && !t) {
                  const e = n;
                  return (0, b.F)(() => {
                    v(_.In);
                  }, e);
                }
              }, [v, t, y, n]),
                (0, s.useEffect)(() => {
                  if (p) {
                    const t = e + n;
                    return (0, b.F)(() => {
                      (l && l(), v(_.End));
                    }, t);
                  }
                }, [v, p, l, n, e]));
              const C = (0, s.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${n}ms`,
                    [d ? "left" : "right"]: "0",
                  }),
                  [d, n, e],
                ),
                S = (0, s.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${n}ms`,
                    [d ? "left" : "right"]: "0",
                  }),
                  [d, n, e],
                ),
                k = (0, s.useMemo)(
                  () => ({ width: `${Math.abs(a - i)}%`, left: `${d ? i : a}%` }),
                  [a, d, i],
                );
              return w
                ? null
                : o().createElement(
                    "div",
                    { className: h, style: k },
                    o().createElement(
                      "div",
                      { style: y ? C : S, className: E },
                      o().createElement(u, { size: r }),
                    ),
                  );
            },
          ),
          y = (0, s.memo)(
            ({
              to: e,
              size: n,
              from: t,
              lineRef: a,
              disabled: r,
              isComplete: i,
              animationSettings: l,
              onChangeAnimationState: m,
              onEndAnimation: d,
            }) => {
              const u = (0, s.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${l.line.duration}ms`,
                  transitionDelay: `${l.line.delay}ms`,
                }),
                [l.line.delay, l.line.duration, e],
              );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(g, {
                  size: n,
                  lineRef: a,
                  disabled: r,
                  isComplete: i,
                  baseStyles: u,
                }),
                t >= 0 &&
                  o().createElement(w, {
                    transitionDuration: l.delta.duration,
                    transitionDelay: l.delta.delay,
                    freezed: l.freezed,
                    from: t,
                    size: n,
                    to: e,
                    onChangeAnimationState: m,
                    onEndAnimation: d,
                  }),
              );
            },
          ),
          v = "ProgressBarDeltaGrow_base_7e",
          C = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          S = "ProgressBarDeltaGrow_glow_68",
          k = (e) => (e ? { left: 0 } : { right: 0 }),
          B = (e, n) => (e ? { right: 100 - n + "%" } : { left: `${n}%` }),
          $ = (e) => ({ transitionDuration: `${e}ms` }),
          I = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: n,
              freezed: t,
              from: a,
              size: i,
              to: l,
              onEndAnimation: m,
              onChangeAnimationState: d,
              className: c,
            }) => {
              const g = l < a,
                f = (0, s.useState)(p.Idle),
                _ = f[0],
                h = f[1],
                E = _ === p.End,
                w = _ === p.Idle,
                y = _ === p.Grow,
                I = _ === p.Shrink,
                P = (0, s.useCallback)(
                  (e) => {
                    (h(e), d && d(e));
                  },
                  [d],
                ),
                z = (0, s.useCallback)(
                  (e, n) =>
                    (0, b.F)(() => {
                      P(e);
                    }, n),
                  [P],
                );
              (0, s.useEffect)(() => {
                if (!t)
                  return w
                    ? z(p.Grow, n)
                    : y
                      ? z(p.Shrink, e)
                      : I
                        ? z(p.End, e)
                        : void (E && m && m());
              }, [z, t, E, y, w, I, m, n, e]);
              const A = (0, s.useMemo)(() => Object.assign({ width: "100%" }, $(e), k(g)), [g, e]),
                D = (0, s.useMemo)(() => Object.assign({ width: "0%" }, $(e), k(g)), [g, e]),
                O = (0, s.useMemo)(() => Object.assign({ width: "0%" }, B(g, a), $(e)), [a, g, e]),
                R = (0, s.useMemo)(
                  () => Object.assign({ width: `${Math.abs(l - a)}%` }, B(g, a), $(e)),
                  [a, g, l, e],
                );
              if (E) return null;
              const j = r()(v, c, g && 0 === l && C);
              return o().createElement(
                "div",
                { style: w ? O : R, className: j },
                o().createElement(
                  "div",
                  { style: I ? D : A, className: S },
                  o().createElement(u, { size: i }),
                ),
              );
            },
          ),
          P = (0, s.memo)(
            ({
              to: e,
              size: n,
              from: t,
              lineRef: a,
              disabled: r,
              isComplete: i,
              animationSettings: l,
              onEndAnimation: m,
              onChangeAnimationState: d,
            }) => {
              const u = e < t,
                c = (0, s.useState)(!1),
                f = c[0],
                b = c[1],
                _ = (0, s.useCallback)(
                  (e) => {
                    (e === p.Shrink && b(!0), d && d(e));
                  },
                  [d],
                ),
                h = (0, s.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                E = (0, s.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${l.line.duration}ms` }),
                  [l.line.duration, e],
                );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(g, {
                  size: n,
                  lineRef: a,
                  disabled: r,
                  isComplete: i,
                  withoutBounce: u && 0 === e,
                  baseStyles: f ? E : h,
                }),
                t >= 0 &&
                  o().createElement(I, {
                    transitionDuration: l.delta.duration,
                    transitionDelay: l.delta.delay,
                    onChangeAnimationState: _,
                    freezed: l.freezed,
                    onEndAnimation: m,
                    from: t,
                    size: n,
                    to: e,
                    className: l.delta.className,
                  }),
              );
            },
          ),
          z = ["onComplete", "onEndAnimation"];
        function A() {
          return (
            (A =
              Object.assign ||
              function (e) {
                for (var n = 1; n < arguments.length; n++) {
                  var t = arguments[n];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            A.apply(this, arguments)
          );
        }
        const D = (0, s.memo)((e) => {
            let n = e.onComplete,
              t = e.onEndAnimation,
              a = (function (e, n) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  s = Object.keys(e);
                for (a = 0; a < s.length; a++) ((t = s[a]), n.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, z);
            const r = (0, s.useState)(!1),
              i = r[0],
              m = r[1],
              d = (0, s.useCallback)(() => {
                const e = 100 === a.to;
                (e !== i && m(e), e && n && n(), t && t());
              }, [i, n, t, a.to]);
            switch (a.animationSettings.type) {
              case l.r.Simple:
                return o().createElement(y, A({}, a, { onEndAnimation: d, isComplete: i }));
              case l.r.Growing:
                return o().createElement(P, A({}, a, { onEndAnimation: d, isComplete: i }));
              default:
                return null;
            }
          }),
          O = ["onEndAnimation"];
        function R() {
          return (
            (R =
              Object.assign ||
              function (e) {
                for (var n = 1; n < arguments.length; n++) {
                  var t = arguments[n];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            R.apply(this, arguments)
          );
        }
        const j = (0, s.memo)((e) => {
          let n = e.onEndAnimation,
            t = (function (e, n) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                s = Object.keys(e);
              for (a = 0; a < s.length; a++) ((t = s[a]), n.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, O);
          const a = (0, s.useRef)({}),
            r = (0, s.useCallback)(() => {
              ((a.current.from = void 0), n && n());
            }, [n]),
            i = "number" == typeof a.current.from ? a.current.from : t.from;
          return (
            (a.current.from = i),
            o().createElement(D, R({}, t, { onEndAnimation: r, key: `${i}-${t.to}`, from: i }))
          );
        });
        function M() {
          return (
            (M =
              Object.assign ||
              function (e) {
                for (var n = 1; n < arguments.length; n++) {
                  var t = arguments[n];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            M.apply(this, arguments)
          );
        }
        const x = (0, s.memo)(
            ({
              size: e,
              value: n,
              lineRef: t,
              disabled: a,
              deltaFrom: r,
              animationSettings: s,
              onEndAnimation: i,
              onChangeAnimationState: l,
              onComplete: m,
            }) => {
              if (r === n)
                return o().createElement(f, {
                  key: `${r}-${n}`,
                  size: e,
                  value: n,
                  lineRef: t,
                  disabled: a,
                  onComplete: m,
                });
              const d = {
                from: r,
                to: n,
                size: e,
                lineRef: t,
                disabled: a,
                animationSettings: s,
                onComplete: m,
                onEndAnimation: i,
                onChangeAnimationState: l,
              };
              return s.withStack
                ? o().createElement(j, d)
                : o().createElement(D, M({ key: `${r}-${n}` }, d));
            },
          ),
          F = (e) => ({
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
        var N = t(515);
        const G = (e, n, t) => {
            if ("number" == typeof t) {
              return ((0, N.u)(0, n, t) / n) * 100;
            }
            return e;
          },
          L = {
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
          T = {
            freezed: !1,
            withStack: !1,
            type: l.r.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          q = (0, s.memo)(
            ({
              maxValue: e = 100,
              theme: n = L,
              size: t = l.$.Default,
              animationSettings: a = T,
              disabled: d = !1,
              withoutBackground: u = !1,
              progressBarBackgroundClassMix: c,
              value: g,
              deltaFrom: f,
              lineRef: b,
              onChangeAnimationState: p,
              onEndAnimation: _,
              onComplete: h,
            }) => {
              const E = ((e, n, t) =>
                (0, s.useMemo)(() => {
                  const a = ((0, N.u)(0, n, e) / n) * 100;
                  return { value: a, deltaFrom: G(a, n, t) };
                }, [t, n, e]))(g, e, f);
              return o().createElement(
                "div",
                { className: r()(i.base, i[`base__${t}`]), style: F(n) },
                !u && o().createElement(m, { size: t, classMix: c }),
                o().createElement(x, {
                  size: t,
                  lineRef: b,
                  disabled: d,
                  value: E.value,
                  deltaFrom: E.deltaFrom,
                  animationSettings: a,
                  onEndAnimation: _,
                  onChangeAnimationState: p,
                  onComplete: h,
                }),
              );
            },
          );
      },
      736: (e, n, t) => {
        let a, r;
        (t.d(n, { $: () => a, r: () => r }),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
          })(a || (a = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(r || (r = {})));
      },
      515: (e, n, t) => {
        t.d(n, { u: () => a });
        const a = (e, n, t) => (t < e ? e : t > n ? n : t);
      },
      122: (e, n, t) => {
        t.d(n, { F: () => a });
        const a = (e, n) => {
          let t;
          const a = setTimeout(() => {
            t = e();
          }, n);
          return () => {
            ("function" == typeof t && t(), clearTimeout(a));
          };
        };
      },
      438: (e, n, t) => {
        (t(483), t(179));
        (t(875), t(736));
        (R.strings.quests.dailyQuests.postBattle.genericAmpersand(),
          R.strings.quests.dailyQuests.postBattle.and());
        var a = t(229);
        a.I.CENTER;
      },
      229: (e, n, t) => {
        let a, r;
        (t.d(n, { $: () => r, I: () => a }),
          (function (e) {
            ((e.LEFT = "left"), (e.RIGHT = "right"), (e.CENTER = "center"));
          })(a || (a = {})),
          (function (e) {
            ((e.BIG = "big"), (e.HUGE = "huge"));
          })(r || (r = {})));
      },
    },
    t = {};
  function a(e) {
    var r = t[e];
    if (void 0 !== r) return r.exports;
    var s = (t[e] = { exports: {} });
    return (n[e](s, s.exports, a), s.exports);
  }
  ((a.m = n),
    (e = []),
    (a.O = (n, t, r, s) => {
      if (!t) {
        var o = 1 / 0;
        for (d = 0; d < e.length; d++) {
          for (var [t, r, s] = e[d], i = !0, l = 0; l < t.length; l++)
            (!1 & s || o >= s) && Object.keys(a.O).every((e) => a.O[e](t[l]))
              ? t.splice(l--, 1)
              : ((i = !1), s < o && (o = s));
          if (i) {
            e.splice(d--, 1);
            var m = r();
            void 0 !== m && (n = m);
          }
        }
        return n;
      }
      s = s || 0;
      for (var d = e.length; d > 0 && e[d - 1][2] > s; d--) e[d] = e[d - 1];
      e[d] = [t, r, s];
    }),
    (a.n = (e) => {
      var n = e && e.__esModule ? () => e.default : () => e;
      return (a.d(n, { a: n }), n);
    }),
    (a.d = (e, n) => {
      for (var t in n)
        a.o(n, t) && !a.o(e, t) && Object.defineProperty(e, t, { enumerable: !0, get: n[t] });
    }),
    (a.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (a.o = (e, n) => Object.prototype.hasOwnProperty.call(e, n)),
    (a.j = 320),
    (() => {
      var e = { 320: 0 };
      a.O.j = (n) => 0 === e[n];
      var n = (n, t) => {
          var r,
            s,
            [o, i, l] = t,
            m = 0;
          if (o.some((n) => 0 !== e[n])) {
            for (r in i) a.o(i, r) && (a.m[r] = i[r]);
            if (l) var d = l(a);
          }
          for (n && n(t); m < o.length; m++)
            ((s = o[m]), a.o(e, s) && e[s] && e[s][0](), (e[s] = 0));
          return a.O(d);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(n.bind(null, 0)), (t.push = n.bind(null, t.push.bind(t))));
    })());
  var r = a.O(void 0, [45], () => a(438));
  r = a.O(r);
})();
