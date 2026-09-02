(() => {
  var __webpack_modules__ = {
      4090: (e, t, a) => {
        "use strict";
        a.d(t, { A: () => l });
        var _ = a(6483),
          u = a.n(_),
          r = a(6179),
          n = a.n(r);
        const i = {
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
          o = ["size", "value", "isEmpty", "fadeInAnimation", "hide", "maximumNumber", "className"];
        function s() {
          return (
            (s =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            s.apply(this, arguments)
          );
        }
        const l = (e) => {
          let t = e.size,
            a = e.value,
            _ = e.isEmpty,
            r = e.fadeInAnimation,
            l = e.hide,
            c = e.maximumNumber,
            m = e.className,
            d = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, o);
          const b = _ ? null : a,
            g = "string" == typeof b;
          if ((b && !g && b < 0) || 0 === b) return null;
          const E = b && !g && b > c,
            p = u()(
              i.base,
              i[`base__${t}`],
              r && i.base__animated,
              l && i.base__hidden,
              !b && i.base__pattern,
              _ && i.base__empty,
              m,
            );
          return n().createElement(
            "div",
            s({ className: p }, d),
            n().createElement("div", { className: i.bg }),
            n().createElement("div", { className: i.pattern }),
            n().createElement(
              "div",
              { className: u()(i.value, g && i.value__text) },
              E ? c : b,
              E && n().createElement("span", { className: i.plus }, "+"),
            ),
          );
        };
        l.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
      },
      280: (e, t, a) => {
        "use strict";
        a.d(t, { z: () => s });
        var _ = a(6179),
          u = a.n(_),
          r = a(6483),
          n = a.n(r),
          i = a(3649),
          o = a(5287);
        const s = ({ binding: e, text: t = "", classMix: a, alignment: r = i.v2.left }) =>
          null === t
            ? (console.error("FormatText was supplied with 'null'"), null)
            : u().createElement(
                _.Fragment,
                null,
                t.split("\n").map((t, s) =>
                  u().createElement(
                    "div",
                    { className: n()(o.Z.base, a), key: `${t}-${s}` },
                    (0, i.Uw)(t, r, e).map((e, t) =>
                      u().createElement(_.Fragment, { key: `${t}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, t, a) => {
        "use strict";
        a.d(t, { Y: () => c });
        var _ = a(3138),
          u = a(6179),
          r = a(1043),
          n = a(5262);
        const i = _.O.client.getSize("rem"),
          o = i.width,
          s = i.height,
          l = Object.assign({ width: o, height: s }, (0, n.T)(o, s, r.j)),
          c = (0, u.createContext)(l);
      },
      1039: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => l });
        var _ = a(6179),
          u = a.n(_),
          r = a(6536),
          n = a(3495),
          i = a(1043),
          o = a(5262),
          s = a(3138);
        const l = (0, _.memo)(({ children: e }) => {
          const t = (0, _.useContext)(n.Y),
            a = (0, _.useState)(t),
            l = a[0],
            c = a[1],
            m = (0, _.useCallback)((e, t) => {
              const a = s.O.view.pxToRem(e),
                _ = s.O.view.pxToRem(t);
              c(Object.assign({ width: a, height: _ }, (0, o.T)(a, _, i.j)));
            }, []);
          ((0, r.Z)(() => {
            engine.on("clientResized", m);
          }),
            (0, _.useEffect)(() => () => engine.off("clientResized", m), [m]));
          const d = (0, _.useMemo)(() => Object.assign({}, l), [l]);
          return u().createElement(n.Y.Provider, { value: d }, e);
        });
      },
      6010: (e, t, a) => {
        "use strict";
        var _ = a(6179),
          u = a(7382),
          r = a(3495);
        const n = ["children"];
        const i = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, n);
          const i = (0, _.useContext)(r.Y),
            o = i.extraLarge,
            s = i.large,
            l = i.medium,
            c = i.small,
            m = i.extraSmall,
            d = i.extraLargeWidth,
            b = i.largeWidth,
            g = i.mediumWidth,
            E = i.smallWidth,
            p = i.extraSmallWidth,
            A = i.extraLargeHeight,
            C = i.largeHeight,
            F = i.mediumHeight,
            B = i.smallHeight,
            h = i.extraSmallHeight,
            D = { extraLarge: A, large: C, medium: F, small: B, extraSmall: h };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && o) return t;
            if (a.large && s) return t;
            if (a.medium && l) return t;
            if (a.small && c) return t;
            if (a.extraSmall && m) return t;
          } else {
            if (a.extraLargeWidth && d) return (0, u.H)(t, a, D);
            if (a.largeWidth && b) return (0, u.H)(t, a, D);
            if (a.mediumWidth && g) return (0, u.H)(t, a, D);
            if (a.smallWidth && E) return (0, u.H)(t, a, D);
            if (a.extraSmallWidth && p) return (0, u.H)(t, a, D);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && A) return t;
              if (a.largeHeight && C) return t;
              if (a.mediumHeight && F) return t;
              if (a.smallHeight && B) return t;
              if (a.extraSmallHeight && h) return t;
            }
          }
          return null;
        };
        i.defaultProps = {
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
        (0, _.memo)(i);
      },
      7382: (e, t, a) => {
        "use strict";
        a.d(t, { H: () => _ });
        const _ = (e, t, a) =>
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
      },
      7739: (e, t, a) => {
        "use strict";
        a.d(t, { YN: () => u.Y, ZN: () => _.Z });
        a(6010);
        var _ = a(1039),
          u = a(3495);
      },
      1043: (e, t, a) => {
        "use strict";
        a.d(t, { j: () => _ });
        const _ = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, a) => {
        "use strict";
        var _;
        function u(e, t, a) {
          const _ = (function (e, t) {
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
            r = Math.min(_, u);
          return {
            extraLarge: r === a.extraLarge.weight,
            large: r === a.large.weight,
            medium: r === a.medium.weight,
            small: r === a.small.weight,
            extraSmall: r === a.extraSmall.weight,
            extraLargeWidth: _ === a.extraLarge.weight,
            largeWidth: _ === a.large.weight,
            mediumWidth: _ === a.medium.weight,
            smallWidth: _ === a.small.weight,
            extraSmallWidth: _ === a.extraSmall.weight,
            extraLargeHeight: u === a.extraLarge.weight,
            largeHeight: u === a.large.weight,
            mediumHeight: u === a.medium.weight,
            smallHeight: u === a.small.weight,
            extraSmallHeight: u === a.extraSmall.weight,
          };
        }
        (a.d(t, { T: () => u, u: () => _ }),
          (function (e) {
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
          })(_ || (_ = {})));
      },
      7590: (e, t, a) => {
        "use strict";
        a.d(t, { ko: () => G, $u: () => o.$ });
        var _ = a(6483),
          u = a.n(_),
          r = a(6179),
          n = a.n(r);
        const i = {
          base: "ProgressBar_base_45",
          base__medium: "ProgressBar_base__medium_62",
          base__small: "ProgressBar_base__small_df",
          background: "ProgressBar_background_51",
          background__medium: "ProgressBar_background__medium_6e",
          background__small: "ProgressBar_background__small_46",
          lineWrapper: "ProgressBar_lineWrapper_6a",
        };
        var o = a(7736);
        const s = ({ size: e = o.$.Default, classMix: t }) =>
            n().createElement("div", { className: u()(i.background, i[`background__${e}`], t) }),
          l = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          c = ({ size: e }) => {
            const t = u()(l.base, l[`base__${e}`]);
            return n().createElement("div", { className: t });
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
          d = (0, r.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: a,
              baseStyles: _,
              isComplete: r,
              withoutBounce: i,
            }) => {
              const o = u()(
                  m.base,
                  m[`base__${e}`],
                  a && m.base__disabled,
                  r && m.base__finished,
                  i && m.base__withoutBounce,
                ),
                s = !a && !r;
              return n().createElement(
                "div",
                { className: o, style: _, ref: t },
                n().createElement("div", { className: m.pattern }),
                n().createElement("div", { className: m.gradient }),
                s && n().createElement(c, { size: e }),
              );
            },
          ),
          b = ({ size: e, value: t, lineRef: a, disabled: _, onComplete: u }) => {
            const i = (0, r.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              o = 100 === t;
            return (
              (0, r.useEffect)(() => {
                o && u && u();
              }, [o, u]),
              n().createElement(d, {
                size: e,
                disabled: _,
                baseStyles: i,
                isComplete: o,
                lineRef: a,
              })
            );
          },
          g = (e, t) => {
            let a;
            const _ = setTimeout(() => {
              a = e();
            }, t);
            return () => {
              ("function" == typeof a && a(), clearTimeout(_));
            };
          };
        let E, p;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(E || (E = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(p || (p = {})));
        const A = "ProgressBarDeltaSimple_base_6c",
          C = "ProgressBarDeltaSimple_delta_99",
          F = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: _,
              size: u,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: s,
            }) => {
              const l = i < _,
                m = (0, r.useState)(p.Idle),
                d = m[0],
                b = m[1],
                E = d === p.In,
                F = d === p.End,
                B = d === p.Idle,
                h = (0, r.useCallback)(
                  (e) => {
                    (b(e), s && s(e));
                  },
                  [s],
                );
              ((0, r.useEffect)(() => {
                if (B && !a) {
                  return g(() => {
                    h(p.In);
                  }, t);
                }
              }, [h, a, B, t]),
                (0, r.useEffect)(() => {
                  if (E) {
                    return g(() => {
                      (o && o(), h(p.End));
                    }, e + t);
                  }
                }, [h, E, o, t, e]));
              const D = (0, r.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [l ? "left" : "right"]: "0",
                  }),
                  [l, t, e],
                ),
                f = (0, r.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [l ? "left" : "right"]: "0",
                  }),
                  [l, t, e],
                ),
                v = (0, r.useMemo)(
                  () => ({ width: `${Math.abs(_ - i)}%`, left: `${l ? i : _}%` }),
                  [_, l, i],
                );
              return F
                ? null
                : n().createElement(
                    "div",
                    { className: A, style: v },
                    n().createElement(
                      "div",
                      { style: B ? D : f, className: C },
                      n().createElement(c, { size: u }),
                    ),
                  );
            },
          ),
          B = (0, r.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: _,
              disabled: u,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: s,
              onEndAnimation: l,
            }) => {
              const c = (0, r.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return n().createElement(
                n().Fragment,
                null,
                n().createElement(d, {
                  size: t,
                  lineRef: _,
                  disabled: u,
                  isComplete: i,
                  baseStyles: c,
                }),
                a >= 0 &&
                  n().createElement(F, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: a,
                    size: t,
                    to: e,
                    onChangeAnimationState: s,
                    onEndAnimation: l,
                  }),
              );
            },
          ),
          h = "ProgressBarDeltaGrow_base_7e",
          D = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          f = "ProgressBarDeltaGrow_glow_68",
          v = (e) => (e ? { left: 0 } : { right: 0 }),
          x = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          S = (e) => ({ transitionDuration: `${e}ms` }),
          w = (0, r.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: _,
              size: i,
              to: o,
              onEndAnimation: s,
              onChangeAnimationState: l,
              className: m,
            }) => {
              const d = o < _,
                b = (0, r.useState)(E.Idle),
                p = b[0],
                A = b[1],
                C = p === E.End,
                F = p === E.Idle,
                B = p === E.Grow,
                w = p === E.Shrink,
                k = (0, r.useCallback)(
                  (e) => {
                    (A(e), l && l(e));
                  },
                  [l],
                ),
                N = (0, r.useCallback)(
                  (e, t) =>
                    g(() => {
                      k(e);
                    }, t),
                  [k],
                );
              (0, r.useEffect)(() => {
                if (!a)
                  return F
                    ? N(E.Grow, t)
                    : B
                      ? N(E.Shrink, e)
                      : w
                        ? N(E.End, e)
                        : void (C && s && s());
              }, [N, a, C, B, F, w, s, t, e]);
              const T = (0, r.useMemo)(() => Object.assign({ width: "100%" }, S(e), v(d)), [d, e]),
                y = (0, r.useMemo)(() => Object.assign({ width: "0%" }, S(e), v(d)), [d, e]),
                L = (0, r.useMemo)(() => Object.assign({ width: "0%" }, x(d, _), S(e)), [_, d, e]),
                M = (0, r.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - _)}%` }, x(d, _), S(e)),
                  [_, d, o, e],
                );
              if (C) return null;
              const R = u()(h, m, d && 0 === o && D);
              return n().createElement(
                "div",
                { style: F ? L : M, className: R },
                n().createElement(
                  "div",
                  { style: w ? y : T, className: f },
                  n().createElement(c, { size: i }),
                ),
              );
            },
          ),
          k = (0, r.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: _,
              disabled: u,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: s,
              onChangeAnimationState: l,
            }) => {
              const c = e < a,
                m = (0, r.useState)(!1),
                b = m[0],
                g = m[1],
                p = (0, r.useCallback)(
                  (e) => {
                    (e === E.Shrink && g(!0), l && l(e));
                  },
                  [l],
                ),
                A = (0, r.useMemo)(() => ({ width: `${a}%`, transitionProperty: "none" }), [a]),
                C = (0, r.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return n().createElement(
                n().Fragment,
                null,
                n().createElement(d, {
                  size: t,
                  lineRef: _,
                  disabled: u,
                  isComplete: i,
                  withoutBounce: c && 0 === e,
                  baseStyles: b ? C : A,
                }),
                a >= 0 &&
                  n().createElement(w, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    onChangeAnimationState: p,
                    freezed: o.freezed,
                    onEndAnimation: s,
                    from: a,
                    size: t,
                    to: e,
                    className: o.delta.className,
                  }),
              );
            },
          ),
          N = ["onComplete", "onEndAnimation"];
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        const y = (0, r.memo)((e) => {
            let t = e.onComplete,
              a = e.onEndAnimation,
              _ = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, N);
            const u = (0, r.useState)(!1),
              i = u[0],
              s = u[1],
              l = (0, r.useCallback)(() => {
                const e = 100 === _.to;
                (e !== i && s(e), e && t && t(), a && a());
              }, [i, t, a, _.to]);
            switch (_.animationSettings.type) {
              case o.r.Simple:
                return n().createElement(B, T({}, _, { onEndAnimation: l, isComplete: i }));
              case o.r.Growing:
                return n().createElement(k, T({}, _, { onEndAnimation: l, isComplete: i }));
              default:
                return null;
            }
          }),
          L = ["onEndAnimation"];
        function M() {
          return (
            (M =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            M.apply(this, arguments)
          );
        }
        const R = (0, r.memo)((e) => {
          let t = e.onEndAnimation,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, L);
          const _ = (0, r.useRef)({}),
            u = (0, r.useCallback)(() => {
              ((_.current.from = void 0), t && t());
            }, [t]),
            i = "number" == typeof _.current.from ? _.current.from : a.from;
          return (
            (_.current.from = i),
            n().createElement(y, M({}, a, { onEndAnimation: u, key: `${i}-${a.to}`, from: i }))
          );
        });
        function W() {
          return (
            (W =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            W.apply(this, arguments)
          );
        }
        const I = (0, r.memo)(
          ({
            size: e,
            value: t,
            lineRef: a,
            disabled: _,
            deltaFrom: u,
            animationSettings: r,
            onEndAnimation: i,
            onChangeAnimationState: o,
            onComplete: s,
          }) => {
            if (u === t)
              return n().createElement(b, {
                key: `${u}-${t}`,
                size: e,
                value: t,
                lineRef: a,
                disabled: _,
                onComplete: s,
              });
            const l = {
              from: u,
              to: t,
              size: e,
              lineRef: a,
              disabled: _,
              animationSettings: r,
              onComplete: s,
              onEndAnimation: i,
              onChangeAnimationState: o,
            };
            return r.withStack
              ? n().createElement(R, l)
              : n().createElement(y, W({ key: `${u}-${t}` }, l));
          },
        );
        var P = a(156);
        const O = (e, t, a) => (a < e ? e : a > t ? t : a),
          H = (e, t, a) => {
            if ("number" == typeof a) {
              return (O(0, t, a) / t) * 100;
            }
            return e;
          },
          $ = P.Gh,
          z = {
            freezed: !1,
            withStack: !1,
            type: o.r.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          G = (0, r.memo)(
            ({
              maxValue: e = 100,
              theme: t = $,
              size: a = o.$.Default,
              animationSettings: _ = z,
              disabled: l = !1,
              withoutBackground: c = !1,
              progressBarBackgroundClassMix: m,
              value: d,
              deltaFrom: b,
              lineRef: g,
              onChangeAnimationState: E,
              onEndAnimation: p,
              onComplete: A,
            }) => {
              const C = ((e, t, a) =>
                (0, r.useMemo)(() => {
                  const _ = (O(0, t, e) / t) * 100;
                  return { value: _, deltaFrom: H(_, t, a) };
                }, [a, t, e]))(d, e, b);
              return n().createElement(
                "div",
                { className: u()(i.base, i[`base__${a}`]), style: (0, P.VQ)(t) },
                !c && n().createElement(s, { size: a, classMix: m }),
                n().createElement(I, {
                  size: a,
                  lineRef: g,
                  disabled: l,
                  value: C.value,
                  deltaFrom: C.deltaFrom,
                  animationSettings: _,
                  onEndAnimation: p,
                  onChangeAnimationState: E,
                  onComplete: A,
                }),
              );
            },
          );
      },
      156: (e, t, a) => {
        "use strict";
        a.d(t, { Gh: () => u, VQ: () => _, Yy: () => r });
        const _ = (e) => ({
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
          u = {
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
          r = {
            bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_grey",
            line: {
              bgColorBase: "#005aca",
              bgColorDisabled: "transparent",
              bgColorFinished: "#59a011",
            },
            pattern: {
              bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_blue",
              bgImageDisabled: "R.images.gui.maps.icons.components.progress_bar.pattern_disabled",
              bgImageFinished: "R.images.gui.maps.icons.components.progress_bar.pattern_green",
            },
            glow: "R.images.gui.maps.icons.components.progress_bar.glow_blue",
            glowSmall: "R.images.gui.maps.icons.components.progress_bar.glow_small_blue",
            delta: {
              color: "#c2ffff",
              shadow:
                "0 0 4px 1px #00e4ff66, 0 0 9px 1px #00c6ff66, 0 0 12px 2px #00a8ff66, 0 0 12px 4px #0b5aca66",
            },
          };
      },
      7736: (e, t, a) => {
        "use strict";
        let _, u;
        (a.d(t, { $: () => _, r: () => u }),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
          })(_ || (_ = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(u || (u = {})));
      },
      4322: (e, t, a) => {
        "use strict";
        a.d(t, { ZP: () => R });
        var _ = a(6483),
          u = a.n(_),
          r = a(9887),
          n = a.n(r),
          i = a(5415),
          o = a(6179),
          s = a.n(o);
        const l = ["xl", "lg", "md", "sm", "xs"],
          c = (e) => e.includes("_") && ((e) => l.includes(e))(e.split("_").at(-1)),
          m = [i.cJ.ExtraLarge, i.cJ.Large, i.cJ.Medium, i.cJ.Small, i.cJ.ExtraSmall],
          d = (e, t) =>
            Object.keys(e).reduce((a, _) => {
              if (_ in a) return a;
              if (c(_)) {
                const u = _.split("_").slice(0, -1).join("_");
                if (u in a) return a;
                const r = m.indexOf(t),
                  n = (-1 !== r ? l.slice(r) : [])
                    .map((e) => u + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  i = n ? e[n] : void 0;
                return ((a[u] = void 0 !== i ? i : e[u]), a);
              }
              const u = e[_];
              return (
                void 0 === u ||
                  ((e, t) => l.some((a) => void 0 !== t[`${e}_${a}`]))(_, e) ||
                  (a[_] = u),
                a
              );
            }, {}),
          b = (e, t = d) => {
            const a = (
              (e, t = d) =>
              (a) => {
                const _ = (0, i.GS)().mediaSize,
                  u = (0, o.useMemo)(() => t(a, _), [a, _]);
                return s().createElement(e, u);
              }
            )(e, t);
            return s().memo((t) =>
              Object.keys(t).some((e) => c(e) && void 0 !== t[e])
                ? s().createElement(a, t)
                : s().createElement(e, t),
            );
          },
          g = {
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
          E = [
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
        function p() {
          return (
            (p =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            p.apply(this, arguments)
          );
        }
        Object.keys(n());
        const A = {
            XL: { mt: g.mt__XL, mr: g.mr__XL, mb: g.mb__XL, ml: g.ml__XL },
            LG: { mt: g.mt__LG, mr: g.mr__LG, mb: g.mb__LG, ml: g.ml__LG },
            MDp: { mt: g.mt__MDp, mr: g.mr__MDp, mb: g.mb__MDp, ml: g.ml__MDp },
            MD: { mt: g.mt__MD, mr: g.mr__MD, mb: g.mb__MD, ml: g.ml__MD },
            SMp: { mt: g.mt__SMp, mr: g.mr__SMp, mb: g.mb__SMp, ml: g.ml__SMp },
            SM: { mt: g.mt__SM, mr: g.mr__SM, mb: g.mb__SM, ml: g.ml__SM },
            XS: { mt: g.mt__XS, mr: g.mr__XS, mb: g.mb__XS, ml: g.ml__XS },
          },
          C = (Object.keys(A), ["mt", "mr", "mb", "ml"]),
          F = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          B = b((e) => {
            let t = e.className,
              a = e.width,
              _ = e.height,
              r = e.m,
              n = e.mt,
              i = void 0 === n ? r : n,
              l = e.mr,
              c = void 0 === l ? r : l,
              m = e.mb,
              d = void 0 === m ? r : m,
              b = e.ml,
              B = void 0 === b ? r : b,
              h = e.column,
              D = e.row,
              f = e.flexDirection,
              v = void 0 === f ? (h ? "column" : D && "row") || void 0 : f,
              x = e.flexStart,
              S = e.center,
              w = e.flexEnd,
              k = e.spaceBetween,
              N = e.spaceAround,
              T = e.justifyContent,
              y =
                void 0 === T
                  ? (x ? "flex-start" : S && "center") ||
                    (w && "flex-end") ||
                    (k && "space-between") ||
                    (N && "space-around") ||
                    void 0
                  : T,
              L = e.alignItems,
              M =
                void 0 === L
                  ? (x ? "flex-start" : S && "center") || (w && "flex-end") || void 0
                  : L,
              R = e.alignSelf,
              W = e.wrap,
              I = e.flexWrap,
              P = void 0 === I ? (W ? "wrap" : void 0) : I,
              O = e.grow,
              H = e.shrink,
              $ = e.flex,
              z = void 0 === $ ? (O || H ? `${O ? 1 : 0} ${H ? 1 : 0} auto` : void 0) : $,
              G = e.style,
              U = e.children,
              j = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, E);
            const V = (0, o.useMemo)(() => {
                const e = { mt: i, mr: c, mb: d, ml: B },
                  t = ((e) =>
                    C.reduce((t, a) => {
                      const _ = e[a];
                      return _ && "number" != typeof _ ? t.concat(A[!0 === _ ? "MD" : _][a]) : t;
                    }, []))(e),
                  u = ((e) =>
                    C.reduce((t, a) => {
                      const _ = e[a];
                      return ("number" == typeof _ && (t[F[a]] = _ + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, G, u, {
                    width: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    height: void 0 !== _ && "number" == typeof _ ? _ + "rem" : _,
                    flex: z,
                    alignSelf: R,
                    display: v || M ? "flex" : void 0,
                    flexDirection: v,
                    flexWrap: P,
                    justifyContent: y,
                    alignItems: M,
                  }),
                  computedClassNames: t,
                };
              }, [a, _, i, c, d, B, G, z, R, v, P, y, M]),
              q = V.computedStyle,
              Z = V.computedClassNames;
            return s().createElement("div", p({ className: u()(g.base, ...Z, t), style: q }, j), U);
          });
        var h = a(280),
          D = a(3532),
          f = a.n(D);
        const v = {
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
          x = [
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
        function S() {
          return (
            (S =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            S.apply(this, arguments)
          );
        }
        Object.keys(n());
        const w = Object.keys(f()),
          k = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          N = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          T = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          y = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          L =
            (Object.keys(y),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": k,
              "heading-H36": k,
              "heading-H28": N,
              "heading-H24": N,
              "heading-H24R": N,
              "heading-H22": N,
              "heading-H20R": N,
              "heading-H18": N,
              "heading-H15": T,
              "heading-H14": T,
              "paragraph-P24": N,
              "paragraph-P18": N,
              "paragraph-P16": N,
              "paragraph-P14": T,
              "paragraph-P12": T,
              "paragraph-P10": T,
            }),
          M =
            (Object.keys(L),
            (e) =>
              e
                ? ((e) => w.includes(e))(e)
                  ? { colorClassName: v[e] }
                  : { colorStyle: { color: e } }
                : {}),
          R = b((e) => {
            let t = e.text,
              a = e.variant,
              _ = e.className,
              r = e.color,
              n = e.m,
              i = e.mt,
              l = void 0 === i ? n : i,
              c = e.mr,
              m = void 0 === c ? n : c,
              d = e.mb,
              b = void 0 === d ? n : d,
              g = e.ml,
              E = void 0 === g ? n : g,
              p = e.style,
              A = e.format,
              C = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, x);
            const F = (0, o.useMemo)(() => {
                const e = M(r),
                  t = e.colorClassName,
                  a = e.colorStyle,
                  _ = void 0 === a ? {} : a;
                return { computedStyle: Object.assign({}, p, _), colorClassName: t };
              }, [p, r]),
              D = F.computedStyle,
              f = F.colorClassName;
            return s().createElement(
              B,
              S(
                {
                  className: u()(v.base, a && v[a], f, _),
                  style: D,
                  mt: !0 === l ? L[a || "paragraph-P16"].mt : l,
                  mr: !0 === m ? L[a || "paragraph-P16"].mr : m,
                  mb: !0 === b ? L[a || "paragraph-P16"].mb : b,
                  ml: !0 === E ? L[a || "paragraph-P16"].ml : E,
                },
                C,
              ),
              void 0 !== A ? s().createElement(h.z, S({}, A, { text: t })) : t,
            );
          });
      },
      7078: (e, t, a) => {
        "use strict";
        a.d(t, { t: () => o });
        var _ = a(6179),
          u = a.n(_),
          r = a(2056);
        const n = ["children"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const o = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, n);
          return u().createElement(
            r.u,
            i(
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
        };
      },
      3415: (e, t, a) => {
        "use strict";
        a.d(t, { l: () => s });
        var _ = a(6179),
          u = a.n(_),
          r = a(7078),
          n = a(6373),
          i = a(2056);
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const s = ({ children: e, tooltipArgs: t, className: a }) => {
          if (!t) return e;
          const _ = u().createElement("div", { className: a }, e);
          if (t.header || t.body) return u().createElement(n.i, t, _);
          const s = t.contentId,
            l = t.args,
            c = null == l ? void 0 : l.contentId;
          return s || c
            ? u().createElement(i.u, o({}, t, { contentId: s || c }), _)
            : u().createElement(r.t, t, _);
        };
      },
      6373: (e, t, a) => {
        "use strict";
        a.d(t, { i: () => s });
        var _ = a(2056),
          u = a(6179),
          r = a.n(u);
        const n = ["children", "body", "header", "note", "alert", "args"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const o = R.views.common.tooltip_window.simple_tooltip_content,
          s = (e) => {
            let t = e.children,
              a = e.body,
              s = e.header,
              l = e.note,
              c = e.alert,
              m = e.args,
              d = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, n);
            const b = (0, u.useMemo)(() => {
              const e = Object.assign({}, m, { body: a, header: s, note: l, alert: c });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [c, a, s, l, m]);
            return r().createElement(
              _.u,
              i(
                {
                  contentId:
                    ((g = null == m ? void 0 : m.hasHtmlContent),
                    g ? o.SimpleTooltipHtmlContent("resId") : o.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: b,
                },
                d,
              ),
              t,
            );
            var g;
          };
      },
      2056: (e, t, a) => {
        "use strict";
        a.d(t, { u: () => s });
        var _ = a(7902),
          u = a(4179),
          r = a(6179);
        const n = [
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
        function i(e) {
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
        const o = (e, t, a = {}, _ = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: u.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: _,
                },
                a,
              ),
            );
          },
          s = (e) => {
            let t = e.children,
              a = e.contentId,
              u = e.args,
              s = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              m = e.onClick,
              d = e.ignoreShowDelay,
              b = void 0 !== d && d,
              g = e.ignoreMouseClick,
              E = void 0 !== g && g,
              p = e.decoratorId,
              A = void 0 === p ? 0 : p,
              C = e.isEnabled,
              F = void 0 === C || C,
              B = e.targetId,
              h = void 0 === B ? 0 : B,
              D = e.onShow,
              f = e.onHide,
              v = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, n);
            const x = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, r.useMemo)(() => h || (0, _.F)().resId, [h]),
              w = (0, r.useCallback)(() => {
                (x.current.isVisible && x.current.timeoutId) ||
                  (o(a, A, { isMouseEvent: !0, on: !0, arguments: i(u) }, S),
                  D && D(),
                  (x.current.isVisible = !0));
              }, [a, A, u, S, D]),
              k = (0, r.useCallback)(() => {
                if (x.current.isVisible || x.current.timeoutId) {
                  const e = x.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (x.current.timeoutId = 0)),
                    o(a, A, { on: !1 }, S),
                    x.current.isVisible && f && f(),
                    (x.current.isVisible = !1));
                }
              }, [a, A, S, f]),
              N = (0, r.useCallback)((e) => {
                x.current.isVisible &&
                  ((x.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (x.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(x.current.prevTarget) && k();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = x.current.hideTimerId;
              return (
                document.addEventListener("wheel", N, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", N, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === F && k();
              }, [F, k]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", k),
                  () => {
                    (window.removeEventListener("mouseleave", k), k());
                  }
                ),
                [k],
              ));
            return F
              ? (0, r.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((T = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((x.current.timeoutId = window.setTimeout(w, b ? 100 : 400)),
                            s && s(e),
                            T && T(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (k(), null == l || l(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === E && k(), null == m || m(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === E && k(), null == c || c(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    v,
                  ),
                )
              : t;
            var T;
          };
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
        (a.r(t), a.d(t, { mouse: () => i, onResize: () => r }));
        var _ = a(2472),
          u = a(1176);
        const r = (0, _.E)("clientResized"),
          n = { down: (0, _.E)("mousedown"), up: (0, _.E)("mouseup"), move: (0, _.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, u.R)(!1);
          }
          function a() {
            e.enabled && (0, u.R)(!0);
          }
          function _() {
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
                    i = n[t]((e) => a([e, "outside"]));
                  function o(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, o),
                    _(),
                    () => {
                      u &&
                        (i(), window.removeEventListener(r, o), (e.listeners -= 1), _(), (u = !1));
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
              ((e.enabled = !1), _());
            },
            enable() {
              ((e.enabled = !0), _());
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
            events: () => _,
            getMouseGlobalPosition: () => r,
            getSize: () => u,
            graphicsQuality: () => n,
          }));
        var _ = a(527);
        function u(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const n = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, a) => {
        "use strict";
        function _(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        a.d(t, { R: () => _ });
      },
      2472: (e, t, a) => {
        "use strict";
        function _(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        a.d(t, { E: () => _ });
      },
      3138: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => u });
        var _ = a(5959);
        const u = { view: a(7641), client: _ };
      },
      3722: (e, t, a) => {
        "use strict";
        function _(e, t, a = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, a);
        }
        function u(e, t, a) {
          return `url(${_(e, t, a)})`;
        }
        (a.r(t), a.d(t, { getBgUrl: () => u, getTextureUrl: () => _ }));
      },
      6112: (e, t, a) => {
        "use strict";
        a.d(t, { W: () => _ });
        const _ = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, a) => {
        "use strict";
        a.d(t, { U: () => u });
        var _ = a(2472);
        const u = {
          onTextureFrozen: (0, _.E)("self.onTextureFrozen"),
          onTextureReady: (0, _.E)("self.onTextureReady"),
          onDomBuilt: (0, _.E)("self.onDomBuilt"),
          onLoaded: (0, _.E)("self.onLoaded"),
          onDisplayChanged: (0, _.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, _.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, _.E)("children.onAdded"),
            onLoaded: (0, _.E)("children.onLoaded"),
            onRemoved: (0, _.E)("children.onRemoved"),
            onAttached: (0, _.E)("children.onAttached"),
            onTextureReady: (0, _.E)("children.onTextureReady"),
            onRequestPosition: (0, _.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            addModelObserver: () => l,
            addPreloadTexture: () => i,
            children: () => _,
            displayStatus: () => u.W,
            displayStatusIs: () => x,
            events: () => r.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => f,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => v,
            getScale: () => E,
            getSize: () => m,
            getViewGlobalPosition: () => b,
            isClientAccessible: () => B,
            isEventHandled: () => D,
            isFocused: () => F,
            pxToRem: () => p,
            remToPx: () => A,
            resize: () => d,
            sendEvent: () => n.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => h,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => c,
            whenTutorialReady: () => w,
          }));
        var _ = a(3722),
          u = a(6112),
          r = a(6538),
          n = a(8566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function s(e, t, a, _ = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, a, _);
        }
        function l(e, t, a) {
          return viewEnv.addDataChangedCallback(e, t, a);
        }
        function c(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function d(e, t, a = "px") {
          return "rem" === a ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function b(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: A(t.x), y: A(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function E() {
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
        function F() {
          return viewEnv.isFocused();
        }
        function B() {
          return viewEnv.isClientAccessible();
        }
        function h() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function f() {
          viewEnv.forceTriggerMouseMove();
        }
        function v() {
          return viewEnv.getShowingStatus();
        }
        const x = Object.keys(u.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === u.W[t]), e),
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
          w = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        "use strict";
        a.d(t, { qP: () => s });
        const _ = ["args"];
        const u = 2,
          r = 16,
          n = 32,
          i = 64,
          o = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                n = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    _,
                    u = {},
                    r = Object.keys(e);
                  for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                  return u;
                })(t, _);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, n, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, n));
            }
            return viewEnv.handleViewEvent({ __Type: a, type: e });
            var u;
          },
          s = {
            close(e) {
              o("popover" === e ? u : n);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      4598: (e, t, a) => {
        "use strict";
        function _() {}
        a.d(t, { ZT: () => _, jv: () => u });
        function u() {
          return !1;
        }
        console.log;
      },
      7902: (e, t, a) => {
        "use strict";
        a.d(t, { F: () => _ });
        const _ = (e = 1) => {
          const t = new Error().stack;
          let a,
            _ = R.invalid("resId");
          return (
            t &&
              ((a = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== a &&
                window.subViews[a] &&
                (_ = window.subViews[a].id)),
            { caller: a, stack: t, resId: _ }
          );
        };
      },
      6536: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => u });
        var _ = a(6179);
        const u = (e) => {
          const t = (0, _.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      5415: (e, t, a) => {
        "use strict";
        a.d(t, { Aq: () => o, GS: () => s, cJ: () => n, fd: () => i });
        var _ = a(6179),
          u = a(7739),
          r = a(1043);
        let n, i, o;
        (!(function (e) {
          ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = r.j.small.width)] = "Small"),
            (e[(e.Medium = r.j.medium.width)] = "Medium"),
            (e[(e.Large = r.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
        })(n || (n = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.width)] = "Small"),
              (e[(e.Medium = r.j.medium.width)] = "Medium"),
              (e[(e.Large = r.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
          })(i || (i = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.height)] = "Small"),
              (e[(e.Medium = r.j.medium.height)] = "Medium"),
              (e[(e.Large = r.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.height)] = "ExtraLarge"));
          })(o || (o = {})));
        const s = () => {
          const e = (0, _.useContext)(u.YN),
            t = e.width,
            a = e.height,
            r = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return n.ExtraLarge;
                case e.large:
                  return n.Large;
                case e.medium:
                  return n.Medium;
                case e.small:
                  return n.Small;
                case e.extraSmall:
                  return n.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), n.ExtraSmall);
              }
            })(e),
            s = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return i.ExtraLarge;
                case e.largeWidth:
                  return i.Large;
                case e.mediumWidth:
                  return i.Medium;
                case e.smallWidth:
                  return i.Small;
                case e.extraSmallWidth:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e),
            l = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return o.ExtraLarge;
                case e.largeHeight:
                  return o.Large;
                case e.mediumHeight:
                  return o.Medium;
                case e.smallHeight:
                  return o.Small;
                case e.extraSmallHeight:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: r,
            mediaWidth: s,
            mediaHeight: l,
            remScreenWidth: t,
            remScreenHeight: a,
          };
        };
      },
      9924: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => s });
        var _ = a(6483),
          u = a.n(_),
          r = a(7739),
          n = a(5262),
          i = a(6179),
          o = a(3649);
        function s(e, t, a) {
          const _ = (0, i.useContext)(r.YN);
          let s = Object.entries(_).filter(([e, t]) => !0 === t && e in n.u);
          return (
            a && (s = s.filter((e) => a.includes(e[0]))),
            e.reduce((e, a) => {
              const _ = s.map((e) =>
                u()(t[((e, t) => e + "__" + t)(a, e[0])], t[((e, t) => e + (0, o.e)(t))(a, e[0])]),
              );
              return ((e[a] = u()(t[a], ..._)), e);
            }, {})
          );
        }
      },
      5521: (e, t, a) => {
        "use strict";
        let _, u;
        (a.d(t, { n: () => _ }),
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
          })(_ || (_ = {})),
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
      3649: (e, t, a) => {
        "use strict";
        let _;
        function u(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        function r(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const a = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(a, -a)]);
          });
        }
        function n(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (a.d(t, {
          Eg: () => o,
          Uw: () => g,
          WU: () => u,
          e: () => n,
          uF: () => r,
          v2: () => _,
          z4: () => i,
        }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(_ || (_ = {})));
        const i = (e) => e.replace(/&nbsp;/g, " "),
          o = (e) => e.replace(/&zwnbsp;/g, "\ufeff"),
          s = (e, t, a) => {
            if (a % 2) {
              const a = e.pop();
              return [...e, a + t];
            }
            return [...e, t];
          },
          l = (e, t, a) => {
            if (0 === a) return [t];
            if (a % 2) return [...e, " " === t ? " " : t];
            {
              const a = e.pop();
              return [...e, a + t];
            }
          },
          c = (e, t, a = _.left) => e.split(t).reduce(a === _.left ? s : l, []),
          m = (() => {
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
          d = ["zh_cn", "zh_sg", "zh_tw"],
          b = (e, t = _.left) => {
            const a = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return d.includes(a)
              ? m(e)
              : ((e, t = _.left) => {
                  let a = [];
                  const u =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = i(e);
                  return (c(r, /( )/, t).forEach((e) => (a = a.concat(c(e, u, _.left)))), a);
                })(e, t);
          },
          g = (e, t, a) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (a && e in a ? a[e] : b(e, t)));
      },
      1358: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => r });
        var _ = a(3138);
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
            const r = _.O.view.addModelObserver(e, a, u);
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
              const _ = this._callbacks[a];
              void 0 !== _ && _(e, t);
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
          kH: () => m,
          B3: () => s,
          Gr: () => l,
          Z5: () => n,
          lf: () => c,
          cy: () => i,
          B0: () => o,
          wU: () => f,
          ry: () => A,
          Eu: () => C,
          Sy: () => B,
          SW: () => h,
          P3: () => D,
        });
        class _ {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: a }) => {
                  let _ = e.target;
                  do {
                    if (_ === t) return;
                    _ = _.parentNode;
                  } while (_);
                  a();
                });
              }));
          }
          static get instance() {
            return (_.__instance || (_.__instance = new _()), _.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const a = e,
              _ = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== a || t !== _,
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
        _.__instance = void 0;
        const u = _;
        var r = a(1358);
        const n = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          i = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, a) => userLocale.getTimeFormat(e, t, void 0 === a || a),
            getTimeString: (e, t, a) => userLocale.getTimeString(e, t, void 0 === a || a),
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
        const s = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          l = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          c = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var d = a(5521),
          b = a(3138);
        const g = ["args"];
        function E(e, t, a, _, u, r, n) {
          try {
            var i = e[r](n),
              o = i.value;
          } catch (e) {
            return void a(e);
          }
          i.done ? t(o) : Promise.resolve(o).then(_, u);
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
                    a = arguments;
                  return new Promise(function (_, u) {
                    var r = e.apply(t, a);
                    function n(e) {
                      E(r, _, u, n, i, "next", e);
                    }
                    function i(e) {
                      E(r, _, u, n, i, "throw", e);
                    }
                    n(void 0);
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
          F = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const u = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    _,
                    u = {},
                    r = Object.keys(e);
                  for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                  return u;
                })(t, g);
              void 0 !== u
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, r, {
                      arguments:
                        ((_ = u),
                        Object.entries(_).map(([e, t]) => {
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
            var _;
          },
          B = () => F(o.CLOSE),
          h = () => F(o.POP_OVER, { on: !1 }),
          D = (e, t, a, _, u = R.invalid("resId"), r) => {
            const n = b.O.view.getViewGlobalPosition(),
              i = a.getBoundingClientRect(),
              s = i.x,
              l = i.y,
              c = i.width,
              m = i.height,
              d = {
                x: b.O.view.pxToRem(s) + n.x,
                y: b.O.view.pxToRem(l) + n.y,
                width: b.O.view.pxToRem(c),
                height: b.O.view.pxToRem(m),
              };
            F(o.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: _ || R.invalid("resId"),
              targetID: u,
              direction: t,
              bbox: p(d),
              on: !0,
              args: r,
            });
          },
          f = () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
          v = (e, t) => {
            e.keyCode === d.n.ESCAPE && t();
          };
        var x = a(7572);
        const S = u.instance,
          w = {
            DataTracker: r.Z,
            ViewModel: x.Z,
            ViewEventType: o,
            NumberFormatType: s,
            RealFormatType: l,
            TimeFormatType: c,
            DateFormatType: m,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => F(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: B,
            sendClosePopOverEvent: h,
            sendShowContextMenuEvent: (e, t, a = 0) => {
              F(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: a,
                args: t,
              });
            },
            sendShowPopOverEvent: D,
            addEscapeListener: (e) => {
              const t = (t) => v(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              v(e, B);
            },
            handleViewEvent: F,
            onBindingsReady: A,
            onLayoutReady: C,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: f,
            dumpViewModel: function e(t) {
              const a = {};
              if ("object" != typeof t) return t;
              for (const _ in t)
                if (Object.prototype.hasOwnProperty.call(t, _)) {
                  const u = Object.prototype.toString.call(t[_]);
                  if (u.startsWith("[object CoherentArrayProxy]")) {
                    const u = t[_];
                    a[_] = [];
                    for (let t = 0; t < u.length; t++) a[_].push({ value: e(u[t].value) });
                  } else
                    u.startsWith("[object class BW::WULF::ViewModel")
                      ? (a[_] = e(t[_]))
                      : (a[_] = t[_]);
                }
              return a;
            },
            ClickOutsideManager: S,
            SystemLocale: n,
            UserLocale: i,
          };
        window.ViewEnvHelper = w;
      },
      3129: (e, t, a) => {
        "use strict";
        var _ = a(3138),
          u = a(7739),
          r = a(6179),
          n = a.n(r),
          i = a(6483),
          o = a.n(i),
          s = a(926),
          l = a.n(s),
          c = a(5415);
        const m = ["children", "className"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        const b = {
            [c.fd.ExtraSmall]: "",
            [c.fd.Small]: l().SMALL_WIDTH,
            [c.fd.Medium]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH}`,
            [c.fd.Large]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH}`,
            [c.fd.ExtraLarge]:
              `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH} ${l().EXTRA_LARGE_WIDTH}`,
          },
          g = {
            [c.Aq.ExtraSmall]: "",
            [c.Aq.Small]: l().SMALL_HEIGHT,
            [c.Aq.Medium]: `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT}`,
            [c.Aq.Large]: `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT} ${l().LARGE_HEIGHT}`,
            [c.Aq.ExtraLarge]:
              `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT} ${l().LARGE_HEIGHT} ${l().EXTRA_LARGE_HEIGHT}`,
          },
          E = {
            [c.cJ.ExtraSmall]: "",
            [c.cJ.Small]: l().SMALL,
            [c.cJ.Medium]: `${l().SMALL} ${l().MEDIUM}`,
            [c.cJ.Large]: `${l().SMALL} ${l().MEDIUM} ${l().LARGE}`,
            [c.cJ.ExtraLarge]: `${l().SMALL} ${l().MEDIUM} ${l().LARGE} ${l().EXTRA_LARGE}`,
          },
          p = (e) => {
            let t = e.children,
              a = e.className,
              _ = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, m);
            const u = (0, c.GS)(),
              r = u.mediaWidth,
              i = u.mediaHeight,
              s = u.mediaSize;
            return n().createElement("div", d({ className: o()(a, b[r], g[i], E[s]) }, _), t);
          },
          A = ["children"];
        const C = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, A);
          return n().createElement(u.ZN, null, n().createElement(p, a, t));
        };
        var F = a(493),
          B = a.n(F);
        function h(e) {
          engine.call("PlaySound", e);
        }
        const D = {
            playHighlight() {
              h("highlight");
            },
            playClick() {
              h("play");
            },
            playYes() {
              h("yes1");
            },
          },
          f = {
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
        let v, x;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(v || (v = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(x || (x = {})));
        const S = ({
          children: e,
          size: t,
          isFocused: a,
          type: _,
          disabled: u,
          mixClass: i,
          soundHover: s,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: m,
          onMouseDown: d,
          onMouseUp: b,
          onMouseLeave: g,
          onClick: E,
        }) => {
          const p = (0, r.useRef)(null),
            A = (0, r.useState)(a),
            C = A[0],
            F = A[1],
            B = (0, r.useState)(!1),
            D = B[0],
            x = B[1],
            S = (0, r.useState)(!1),
            w = S[0],
            k = S[1],
            N = (0, r.useCallback)(() => {
              u || (p.current && (p.current.focus(), F(!0)));
            }, [u]),
            T = (0, r.useCallback)(
              (e) => {
                C && null !== p.current && !p.current.contains(e.target) && F(!1);
              },
              [C],
            ),
            y = (0, r.useCallback)(
              (e) => {
                u || (E && E(e));
              },
              [u, E],
            ),
            L = (0, r.useCallback)(
              (e) => {
                u || (null !== s && h(s), c && c(e), k(!0));
              },
              [u, s, c],
            ),
            M = (0, r.useCallback)(
              (e) => {
                m && m(e);
              },
              [m],
            ),
            W = (0, r.useCallback)(
              (e) => {
                u || (b && b(e), x(!1));
              },
              [u, b],
            ),
            I = (0, r.useCallback)(
              (e) => {
                u || (null !== l && h(l), d && d(e), a && N(), x(!0));
              },
              [u, l, d, N, a],
            ),
            P = (0, r.useCallback)(
              (e) => {
                u || (g && g(e), x(!1));
              },
              [u, g],
            ),
            O = o()(
              f.base,
              f[`base__${_}`],
              {
                [f.base__disabled]: u,
                [f[`base__${t}`]]: t,
                [f.base__focus]: C,
                [f.base__highlightActive]: D,
                [f.base__firstHover]: w,
              },
              i,
            ),
            H = o()(f.state, f.state__default);
          return (
            (0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", T),
                () => {
                  document.removeEventListener("mousedown", T);
                }
              ),
              [T],
            ),
            (0, r.useEffect)(() => {
              F(a);
            }, [a]),
            n().createElement(
              "div",
              {
                ref: p,
                className: O,
                onMouseEnter: L,
                onMouseMove: M,
                onMouseUp: W,
                onMouseDown: I,
                onMouseLeave: P,
                onClick: y,
              },
              _ !== v.ghost &&
                n().createElement(
                  n().Fragment,
                  null,
                  n().createElement("div", { className: f.back }),
                  n().createElement("span", { className: f.texture }),
                ),
              n().createElement(
                "span",
                { className: H },
                n().createElement("span", { className: f.stateDisabled }),
                n().createElement("span", { className: f.stateHighlightHover }),
                n().createElement("span", { className: f.stateHighlightActive }),
              ),
              n().createElement(
                "span",
                { className: f.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        S.defaultProps = {
          type: v.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const w = (0, r.memo)(S),
          k = {
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
          N = [
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
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        class y extends n().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && h(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && h(this.props.soundClick));
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
              _ = e.goto,
              u = e.side,
              r = e.type,
              i = e.classNames,
              s = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              m = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var a,
                    _,
                    u = {},
                    r = Object.keys(e);
                  for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                  return u;
                })(e, N)),
              b = o()(k.base, k[`base__${r}`], k[`base__${u}`], null == i ? void 0 : i.base),
              g = o()(k.icon, k[`icon__${r}`], k[`icon__${u}`], null == i ? void 0 : i.icon),
              E = o()(k.glow, null == i ? void 0 : i.glow),
              p = o()(k.caption, k[`caption__${r}`], null == i ? void 0 : i.caption),
              A = o()(k.goto, null == i ? void 0 : i.goto);
            return n().createElement(
              "div",
              T(
                {
                  className: b,
                  onMouseEnter: this._onMouseEnter(s),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(m),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: a,
                },
                d,
              ),
              "info" !== r && n().createElement("div", { className: k.shine }),
              n().createElement(
                "div",
                { className: g },
                n().createElement("div", { className: E }),
              ),
              n().createElement("div", { className: p }, t),
              _ && n().createElement("div", { className: A }, _),
            );
          }
        }
        y.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var L = a(6373);
        var M = a(3649);
        let W;
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
        })(W || (W = {}));
        var I = a(4179);
        const P = 60,
          O = 3600,
          H = 86400;
        Date.now();
        const $ = () => {},
          z = (e = 0, t, a = 0, _ = $) => {
            const u = (0, r.useState)(e),
              n = u[0],
              i = u[1];
            return (
              (0, r.useEffect)(() => {
                if (e > 0) {
                  i(e);
                  const u = Date.now(),
                    r = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - u) / 1e3);
                        null !== a && t <= a ? (i(a), _ && _(), clearInterval(r)) : i(t);
                      },
                      1e3 * (t || (e > 120 ? P : 1)),
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                i(0);
              }, [e, t, a, _]),
              n
            );
          };
        var G = a(7902);
        const U = (e, t) => e.split(".").reduce((e, t) => e && e[t], t);
        var j = a(6536);
        const V = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          q = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          Z = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, a) => {
                const _ = U(`${e}.${a}`, window);
                return V(_) ? t(e, a, _) : `${e}.${a}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          Y = (e) => {
            const t = ((e) => {
                const t = (0, G.F)(),
                  a = t.caller,
                  _ = t.resId,
                  u = window.__feature && window.__feature !== a && a ? `subViews.${a}` : "";
                return { modelPrefix: u, modelPath: q(u, e || ""), resId: _ };
              })(),
              a = t.modelPrefix,
              _ = e.split(".");
            if (_.length > 0) {
              const e = [_[0]];
              return (
                _.reduce((t, _) => {
                  const u = U(q(a, `${t}.${_}`), window);
                  return V(u) ? (e.push(u.id), `${t}.${_}.value`) : (e.push(_), `${t}.${_}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          X = I.Sw.instance;
        let K;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(K || (K = {}));
        const J = (e = "model", t = K.Deep) => {
            const a = (0, r.useState)(0),
              _ = (a[0], a[1]),
              u = (0, r.useMemo)(() => (0, G.F)(), []),
              n = u.caller,
              i = u.resId,
              o = (0, r.useMemo)(
                () => (window.__feature && window.__feature !== n ? `subViews.${n}.${e}` : e),
                [n, e],
              ),
              s = (0, r.useState)(() =>
                ((e) => {
                  const t = U(e, window);
                  for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                  return V(t) ? t.value : t;
                })(Z(o)),
              ),
              l = s[0],
              c = s[1],
              m = (0, r.useRef)(-1);
            return (
              (0, j.Z)(() => {
                if (
                  ("boolean" == typeof t &&
                    ((t = t ? K.Deep : K.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  t !== K.None)
                ) {
                  const a = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      t === K.Deep
                        ? (e === l && _((e) => e + 1), c(e))
                        : c(Object.assign([], e));
                    },
                    u = Y(e);
                  m.current = X.addCallback(u, a, i, t === K.Deep);
                }
              }),
              (0, r.useEffect)(() => {
                if (t !== K.None)
                  return () => {
                    X.removeCallback(m.current, i);
                  };
              }, [i, t]),
              l
            );
          },
          Q = (I.Sw.instance, z);
        var ee = a(5521);
        const te = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function ae(e = ee.n.NONE, t = te, a = !1) {
          (0, r.useEffect)(() => {
            if (e !== ee.n.NONE)
              return (
                window.addEventListener("keydown", u, a),
                () => {
                  window.removeEventListener("keydown", u, a);
                }
              );
            function u(u) {
              if (u.keyCode === e) {
                if (_.O.view.isEventHandled()) return;
                (_.O.view.setEventHandled(), t(u), a && u.stopPropagation());
              }
            }
          }, [t, e, a]);
        }
        function _e() {
          !(function (e = ee.n.ESCAPE) {
            ae(e, I.Sy, !0);
          })(ee.n.ESCAPE);
        }
        var ue = a(9924),
          re = a(3486);
        let ne;
        !(function (e) {
          ((e.DISABLED = "disabled"), (e.ACTIVE = "active"));
        })(ne || (ne = {}));
        var ie = a(2646),
          oe = a(4194),
          se = a(7663),
          le = a(2100),
          ce = a(5060),
          me = a(8184),
          de = a(280),
          be = a(8188),
          ge = a(9930),
          Ee = a(4090),
          pe = a(7078),
          Ae = a(2056);
        const Ce = {
            base: "CardWrapper_base_b7",
            base__disabled: "CardWrapper_base__disabled_4f",
            base__locked: "CardWrapper_base__locked_95",
            base__isNotStarted: "CardWrapper_base__isNotStarted_29",
            mask: "CardWrapper_mask_f7",
            border: "CardWrapper_border_a3",
            border__locked: "CardWrapper_border__locked_c0",
            hover: "CardWrapper_hover_af",
            hover__anim: "CardWrapper_hover__anim_10",
            animBg: "CardWrapper_animBg_f3",
            animBg__wide: "CardWrapper_animBg__wide_16",
            selection: "CardWrapper_selection_35",
            check: "CardWrapper_check_c1",
            check__extraSmall: "CardWrapper_check__extraSmall_fa",
            check__small: "CardWrapper_check__small_33",
            checkBackground: "CardWrapper_checkBackground_bd",
            checkBackground__extraSmall: "CardWrapper_checkBackground__extraSmall_ff",
            checkBackground__small: "CardWrapper_checkBackground__small_d8",
            disabling: "CardWrapper_disabling_63",
            background: "CardWrapper_background_34",
            background__anim: "CardWrapper_background__anim_34",
            background__empty: "CardWrapper_background__empty_bb",
            lockBgTexture: "CardWrapper_lockBgTexture_c5",
            lockBlock: "CardWrapper_lockBlock_81",
            b0: "CardWrapper_b0_65",
            b1: "CardWrapper_b1_10",
            b2: "CardWrapper_b2_7a",
            b3: "CardWrapper_b3_5e",
            b4: "CardWrapper_b4_60",
            b5: "CardWrapper_b5_9a",
            lockBlock__medium: "CardWrapper_lockBlock__medium_12",
            lockBlock__big: "CardWrapper_lockBlock__big_51",
            lock: "CardWrapper_lock_31",
            lock__anim: "CardWrapper_lock__anim_fd",
            lock__medium: "CardWrapper_lock__medium_5f",
            lock__big: "CardWrapper_lock__big_8c",
            lockGlow: "CardWrapper_lockGlow_f2",
            lockGlow__medium: "CardWrapper_lockGlow__medium_36",
            lockGlow__big: "CardWrapper_lockGlow__big_b4",
            lockGlow__anim: "CardWrapper_lockGlow__anim_de",
            lockLine: "CardWrapper_lockLine_7e",
            lockLine__medium: "CardWrapper_lockLine__medium_47",
            lockLine__big: "CardWrapper_lockLine__big_91",
            lockLine__leftAnim: "CardWrapper_lockLine__leftAnim_5b",
            lockLine__rightAnim: "CardWrapper_lockLine__rightAnim_77",
            leftLineBg: "CardWrapper_leftLineBg_26",
            rightLineBg: "CardWrapper_rightLineBg_ee",
            novelty: "CardWrapper_novelty_ae",
            info: "CardWrapper_info_49",
            info__anim: "CardWrapper_info__anim_81",
            info__extraSmall: "CardWrapper_info__extraSmall_fc",
            info__small: "CardWrapper_info__small_9c",
            info__medium: "CardWrapper_info__medium_9f",
            infoCorner: "CardWrapper_infoCorner_49",
            infoCorner__anim: "CardWrapper_infoCorner__anim_ba",
            children: "CardWrapper_children_88",
          },
          Fe = ({
            index: e,
            size: t,
            isSelected: a,
            isDisabled: _,
            isNew: u = !1,
            isInfoIconVisible: i,
            resourcesFolderName: s,
            children: l,
            onHoverChanged: m,
            onItemClicked: d,
            onInfoClicked: b,
            resourceFolderGetter: g,
            id: E,
            modeName: p,
            isNotStarted: A,
            isLocked: C,
          }) => {
            const F = (0, ge.O)(),
              B = (0, c.GS)().mediaSize,
              f = (0, r.useCallback)(() => {
                (d({ index: e, size: t, cardMediaSize: F }), D.playClick());
              }, [d, e, t, F]),
              v = (0, r.useCallback)(
                (t) => {
                  (t.stopPropagation(), D.playYes(), b({ index: e }));
                },
                [b, e],
              ),
              x = (0, ge.B)(m),
              S = x[0],
              w = x[1],
              k = (0, r.useCallback)(() => {
                (h(
                  [re.Id.B4, re.Id.B5, re.Id.B6].includes(t)
                    ? "ev_mode_selector_hover_simple"
                    : "ev_mode_selector_hover",
                ),
                  w(!0));
              }, [w, t]),
              N = (0, r.useCallback)(() => {
                w(!1);
              }, [w]),
              T = (0, ue.Z)(["info", "check", "checkBackground"], Ce),
              y = F !== re.Cg.Big;
            let M;
            const W = g(s);
            if (null !== W) {
              const e = W.$dyn(`bg_${t}_${F}`);
              null !== e && (M = { backgroundImage: `url(${e})` });
              const a = W.$dyn(`bg_${t}`);
              null !== a && (M = { backgroundImage: `url(${a})`, backgroundSize: "cover" });
            }
            const I = {
                backgroundImage: `url(${R.images.gui.maps.icons.mode_selector.common.lui_locked.$dyn(`${t}`)})`,
                backgroundSize: "cover",
              },
              P = o()(Ce.lockBgTexture),
              O = i && (S || a),
              H =
                (B === c.cJ.Medium && (t === re.Id.B1 || t === re.Id.B2 || t === re.Id.B3)) ||
                (B === c.cJ.Large && (t === re.Id.B4 || t === re.Id.B5 || t === re.Id.B6)),
              $ = !(
                (B !== c.cJ.Large && B !== c.cJ.ExtraLarge) ||
                (t !== re.Id.B0 && t !== re.Id.B1 && t !== re.Id.B2 && t !== re.Id.B3)
              ),
              z = o()(
                Ce.base,
                _ && Ce.base__disabled,
                C && Ce.base__locked,
                A && Ce.base__isNotStarted,
              ),
              G = o()(
                Ce.background,
                void 0 === M && Ce.background__empty,
                S && !A && !C && Ce.background__anim,
              ),
              U = o()(Ce.lockBlock, { [Ce.lockBlock__medium]: H, [Ce.lockBlock__big]: $ }, Ce[t]),
              j = o()(
                Ce.lockLine,
                { [Ce.lockLine__medium]: H },
                { [Ce.lockLine__big]: $ },
                Ce.leftLineBg,
                { [Ce.lockLine__leftAnim]: S },
              ),
              V = o()(
                Ce.lockLine,
                { [Ce.lockLine__medium]: H },
                { [Ce.lockLine__big]: $ },
                Ce.rightLineBg,
                { [Ce.lockLine__rightAnim]: S },
              ),
              q = o()(Ce.lock, { [Ce.lock__medium]: H, [Ce.lock__big]: $, [Ce.lock__anim]: S }),
              Z = o()(Ce.lockGlow, {
                [Ce.lockGlow__medium]: H,
                [Ce.lockGlow__big]: $,
                [Ce.lockGlow__anim]: S,
              }),
              Y = n().createElement(
                "div",
                null,
                n().createElement(
                  "div",
                  {
                    id: E,
                    className: z,
                    onClick: C ? void 0 : f,
                    onMouseEnter: k,
                    onMouseLeave: N,
                  },
                  n().createElement(
                    "div",
                    { className: Ce.mask },
                    n().createElement("div", { className: G, style: M }),
                    C && n().createElement("div", { className: P, style: I }),
                  ),
                  n().createElement("div", {
                    className: o()(Ce.border, { [Ce.border__locked]: C }),
                  }),
                  a &&
                    n().createElement(
                      n().Fragment,
                      null,
                      n().createElement("div", { className: Ce.selection }),
                      n().createElement("div", {
                        className: o()(Ce.animBg, t === re.Id.B0 && Ce.animBg__wide),
                      }),
                      n().createElement("div", { className: T.checkBackground }),
                      n().createElement("div", { className: T.check }),
                    ),
                  n().createElement("div", {
                    className: o()(Ce.hover, S && !C && !A && Ce.hover__anim),
                  }),
                  n().createElement("div", { className: Ce.children }, l),
                  u &&
                    !_ &&
                    n().createElement(
                      "div",
                      { className: Ce.novelty },
                      n().createElement(Ee.A, {
                        value: R.strings.mode_selector.novelty(),
                        size: y ? "small" : "big",
                      }),
                    ),
                  !C &&
                    n().createElement(
                      n().Fragment,
                      null,
                      n().createElement("div", {
                        className: o()(Ce.infoCorner, O && Ce.infoCorner__anim),
                      }),
                      n().createElement(
                        L.i,
                        { body: R.strings.tooltips.mode_selector.info.body(), isEnabled: O },
                        n().createElement("div", {
                          className: o()(T.info, O && Ce.info__anim),
                          onClick: v,
                        }),
                      ),
                    ),
                  _ && n().createElement("div", { className: Ce.disabling }),
                  C &&
                    n().createElement(
                      "div",
                      { className: U },
                      n().createElement("div", { className: j }),
                      n().createElement("div", { className: q }),
                      n().createElement("div", { className: Z }),
                      n().createElement("div", { className: V }),
                    ),
                ),
              );
            return C
              ? n().createElement(
                  Ae.u,
                  {
                    contentId: R.views.lobby.tooltips.NewbieRestrictionsTooltip("resId"),
                    args: { index: e, modeName: p },
                    isEnabled: C,
                    ignoreShowDelay: !0,
                  },
                  Y,
                )
              : n().createElement(
                  pe.t,
                  { isEnabled: _, args: { index: e, modeName: p, tooltipId: ie.p5 } },
                  Y,
                );
          },
          Be = "TimeLeft_base_cf",
          he = "TimeLeft_base__small_7c",
          De = "TimeLeft_icon_5d",
          fe = ({
            index: e,
            text: t,
            isSmall: a = !1,
            classMix: _,
            tooltipId: u,
            modeName: r = "",
          }) =>
            n().createElement(
              pe.t,
              { args: u ? { tooltipId: u, modeName: r } : { tooltipId: ie.GN, index: e } },
              n().createElement(
                "div",
                { className: o()(Be, a && he, _) },
                n().createElement("div", { className: De }),
                t,
              ),
            );
        let ve;
        !(function (e) {
          ((e[(e.NONE = 0)] = "NONE"), (e[(e.STATIC = 1)] = "STATIC"), (e[(e.NEW = 2)] = "NEW"));
        })(ve || (ve = {}));
        const xe = {
            base: "BattlePassIcon_base_bf",
            bpIcon: "BattlePassIcon_bpIcon_18",
            bpIcon__extraLarge: "BattlePassIcon_bpIcon__extraLarge_b3",
            bpIcon__large: "BattlePassIcon_bpIcon__large_c2",
            bpIcon__locked: "BattlePassIcon_bpIcon__locked_86",
            bpAnim: "BattlePassIcon_bpAnim_01",
            bpAnim__extraLarge: "BattlePassIcon_bpAnim__extraLarge_38",
            bpAnim__large: "BattlePassIcon_bpAnim__large_1e",
          },
          Se = ({ modeName: e, isDisabled: t, battlePassState: a, isLocked: _ }) => {
            const u = (0, ue.Z)([...(0, re.Hp)("bpIcon", "bpAnim")], xe);
            return (
              (0, r.useEffect)(() => {
                a !== ve.NEW || t || h("ev_mode_selector_bp_points_icon_appear");
              }, [a, t]),
              a === ve.NONE || t
                ? null
                : n().createElement(
                    "div",
                    { className: xe.base },
                    n().createElement(
                      Ae.u,
                      {
                        contentId:
                          R.views.lobby.mode_selector.tooltips.SimplyFormatTooltip("resId"),
                        args: { modeName: e },
                        ignoreShowDelay: !0,
                        isEnabled: !_,
                      },
                      n().createElement("div", {
                        className: o()(u.bpIcon, { [xe.bpIcon__locked]: _ }),
                      }),
                    ),
                    a === ve.NEW && n().createElement("div", { className: u.bpAnim }),
                  )
            );
          };
        var we = a(3415);
        const ke = {
            base: "Reward_base_80",
            base__narrowMargins: "Reward_base__narrowMargins_42",
            header: "Reward_header_7c",
            vehicleType: "Reward_vehicleType_fa",
            icon: "Reward_icon_93",
            icon__locked: "Reward_icon__locked_6f",
            base__small: "Reward_base__small_cb",
            "base__small-b0": "Reward_base__small-b0_c5",
            "base__small-b1": "Reward_base__small-b1_16",
            base__medium: "Reward_base__medium_ce",
            "base__medium-b1": "Reward_base__medium-b1_3f",
            name: "Reward_name_17",
          },
          Ne = R.images.gui.maps.icons.mode_selector.rewards,
          Te = R.images.gui.maps.icons.vehicleTypes,
          ye = ["small", "small-b0", "small-b1", "medium"],
          Le = [re.Id.B0, re.Id.B1],
          Me = ({
            mediaSize: e,
            cardSize: t,
            iconName: a,
            name: _,
            description: u,
            tooltipID: i,
            vehicleLevel: s,
            vehicleType: l,
            narrowMargins: c = !1,
          }) => {
            const m = `${e}${Le.includes(t) ? `-${t}` : ""}`,
              d = (0, r.useMemo)(() => {
                const e = ye.includes(m) ? "c_48x48" : "c_64x64";
                return { backgroundImage: `url(${Ne.$dyn(e).$dyn(a)})` };
              }, [m, a]);
            return n().createElement(
              we.l,
              {
                tooltipArgs: {
                  args: { tooltipId: i },
                  body: i ? "" : u,
                  header: i ? "" : _,
                  ignoreShowDelay: !0,
                },
              },
              n().createElement(
                "div",
                { className: o()(c ? ke.base__narrowMargins : ke.base, ke[`base__${m}`]) },
                n().createElement(
                  "div",
                  { className: ke.header },
                  n().createElement("div", {
                    className: ke.vehicleType,
                    style: l ? { backgroundImage: `url(${Te.$dyn(l)})` } : void 0,
                  }),
                  n().createElement("div", null, s),
                ),
                n().createElement("div", { className: ke.icon, style: d }),
                _ && n().createElement(de.z, { text: _, classMix: ke.name }),
              ),
            );
          },
          Re = {
            base: "Rewards_base_c8",
            base__extraSmall: "Rewards_base__extraSmall_9b",
            base__small: "Rewards_base__small_78",
            base__medium: "Rewards_base__medium_75",
          };
        function We() {
          return (
            (We =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            We.apply(this, arguments)
          );
        }
        const Ie = ({ size: e, rewardsList: t }) => {
            const a = (0, ge.O)(),
              _ = (0, ue.Z)(["base"], Re);
            return n().createElement(
              "div",
              { className: _.base },
              t &&
                t.map(
                  (_) =>
                    _ &&
                    _.value &&
                    n().createElement(
                      Me,
                      We(
                        {
                          key: _.value.iconName,
                          mediaSize: a,
                          cardSize: e,
                          narrowMargins: t.length >= 3,
                        },
                        _.value,
                      ),
                    ),
                ),
            );
          },
          Pe = {
            base: "NormalCard_base_7a",
            base__medium: "NormalCard_base__medium_34",
            base__extraLarge: "NormalCard_base__extraLarge_87",
            base__large: "NormalCard_base__large_a8",
            base__b0: "NormalCard_base__b0_17",
            base__b0__medium: "NormalCard_base__b0__medium_8c",
            base__b0__extraLarge: "NormalCard_base__b0__extraLarge_bc",
            base__b0__large: "NormalCard_base__b0__large_ff",
            base__b1: "NormalCard_base__b1_ff",
            base__b1__medium: "NormalCard_base__b1__medium_63",
            base__b1__extraLarge: "NormalCard_base__b1__extraLarge_b0",
            base__b1__large: "NormalCard_base__b1__large_f9",
            base__b2: "NormalCard_base__b2_54",
            base__b2__medium: "NormalCard_base__b2__medium_57",
            base__b2__extraLarge: "NormalCard_base__b2__extraLarge_c0",
            base__b2__large: "NormalCard_base__b2__large_22",
            base__b3: "NormalCard_base__b3_50",
            base__b3__medium: "NormalCard_base__b3__medium_25",
            base__b3__extraLarge: "NormalCard_base__b3__extraLarge_8f",
            base__b3__large: "NormalCard_base__b3__large_18",
            base__b4: "NormalCard_base__b4_d9",
            base__b4__medium: "NormalCard_base__b4__medium_5c",
            base__b4__extraLarge: "NormalCard_base__b4__extraLarge_c3",
            base__b4__large: "NormalCard_base__b4__large_52",
            base__b5: "NormalCard_base__b5_f3",
            base__b5__medium: "NormalCard_base__b5__medium_30",
            base__b5__extraLarge: "NormalCard_base__b5__extraLarge_2b",
            base__b5__large: "NormalCard_base__b5__large_df",
            base__b6: "NormalCard_base__b6_8b",
            base__b6__medium: "NormalCard_base__b6__medium_10",
            base__b6__extraLarge: "NormalCard_base__b6__extraLarge_35",
            base__b6__large: "NormalCard_base__b6__large_5c",
            name: "NormalCard_name_ce",
            name__b0: "NormalCard_name__b0_98",
            name__b1: "NormalCard_name__b1_a6",
            name__b0__medium: "NormalCard_name__b0__medium_d2",
            name__b1__medium: "NormalCard_name__b1__medium_e3",
            name__b0__extraLarge: "NormalCard_name__b0__extraLarge_0e",
            name__b0__large: "NormalCard_name__b0__large_d2",
            name__b1__extraLarge: "NormalCard_name__b1__extraLarge_a3",
            name__b1__large: "NormalCard_name__b1__large_20",
            name__b2: "NormalCard_name__b2_73",
            name__b2__medium: "NormalCard_name__b2__medium_1c",
            name__b2__extraLarge: "NormalCard_name__b2__extraLarge_76",
            name__b2__large: "NormalCard_name__b2__large_53",
            name__b3: "NormalCard_name__b3_49",
            name__b3__medium: "NormalCard_name__b3__medium_78",
            name__b3__extraLarge: "NormalCard_name__b3__extraLarge_e9",
            name__b3__large: "NormalCard_name__b3__large_68",
            name__b4: "NormalCard_name__b4_ac",
            name__b4__medium: "NormalCard_name__b4__medium_e4",
            name__b4__extraLarge: "NormalCard_name__b4__extraLarge_2b",
            name__b4__large: "NormalCard_name__b4__large_a3",
            name__b5: "NormalCard_name__b5_2b",
            name__b5__medium: "NormalCard_name__b5__medium_c3",
            name__b5__extraLarge: "NormalCard_name__b5__extraLarge_78",
            name__b5__large: "NormalCard_name__b5__large_9b",
            name__b6: "NormalCard_name__b6_49",
            name__b6__medium: "NormalCard_name__b6__medium_dc",
            name__b6__extraLarge: "NormalCard_name__b6__extraLarge_83",
            name__b6__large: "NormalCard_name__b6__large_89",
            name__locked: "NormalCard_name__locked_71",
            formatText: "NormalCard_formatText_cb",
            formatText__b0__extraSmall: "NormalCard_formatText__b0__extraSmall_7b",
            formatText__b0__small: "NormalCard_formatText__b0__small_65",
            formatText__b1__extraSmall: "NormalCard_formatText__b1__extraSmall_e4",
            formatText__b1__small: "NormalCard_formatText__b1__small_1e",
            formatText__b2__extraSmall: "NormalCard_formatText__b2__extraSmall_e0",
            formatText__b2__small: "NormalCard_formatText__b2__small_e4",
            formatText__b3__extraSmall: "NormalCard_formatText__b3__extraSmall_13",
            formatText__b3__small: "NormalCard_formatText__b3__small_8c",
            formatText__b4__extraSmall: "NormalCard_formatText__b4__extraSmall_f5",
            formatText__b4__small: "NormalCard_formatText__b4__small_49",
            formatText__b5__extraSmall: "NormalCard_formatText__b5__extraSmall_04",
            formatText__b5__small: "NormalCard_formatText__b5__small_b6",
            formatText__b6__extraSmall: "NormalCard_formatText__b6__extraSmall_a3",
            formatText__b6__small: "NormalCard_formatText__b6__small_e0",
            subtitle: "NormalCard_subtitle_75",
            subtitle__b0: "NormalCard_subtitle__b0_bf",
            subtitle__b1: "NormalCard_subtitle__b1_2e",
            subtitle__b0__medium: "NormalCard_subtitle__b0__medium_42",
            subtitle__b1__medium: "NormalCard_subtitle__b1__medium_95",
            subtitle__b0__extraLarge: "NormalCard_subtitle__b0__extraLarge_f2",
            subtitle__b0__large: "NormalCard_subtitle__b0__large_76",
            subtitle__b1__extraLarge: "NormalCard_subtitle__b1__extraLarge_8f",
            subtitle__b1__large: "NormalCard_subtitle__b1__large_d1",
            subtitle__b2: "NormalCard_subtitle__b2_98",
            subtitle__b2__medium: "NormalCard_subtitle__b2__medium_86",
            subtitle__b2__extraLarge: "NormalCard_subtitle__b2__extraLarge_44",
            subtitle__b2__large: "NormalCard_subtitle__b2__large_77",
            subtitle__b3: "NormalCard_subtitle__b3_7e",
            subtitle__b3__medium: "NormalCard_subtitle__b3__medium_57",
            subtitle__b3__extraLarge: "NormalCard_subtitle__b3__extraLarge_f3",
            subtitle__b3__large: "NormalCard_subtitle__b3__large_00",
            subtitle__b4: "NormalCard_subtitle__b4_b1",
            subtitle__b4__medium: "NormalCard_subtitle__b4__medium_64",
            subtitle__b4__extraLarge: "NormalCard_subtitle__b4__extraLarge_44",
            subtitle__b4__large: "NormalCard_subtitle__b4__large_6d",
            subtitle__b5: "NormalCard_subtitle__b5_4a",
            subtitle__b5__medium: "NormalCard_subtitle__b5__medium_03",
            subtitle__b5__extraLarge: "NormalCard_subtitle__b5__extraLarge_04",
            subtitle__b5__large: "NormalCard_subtitle__b5__large_14",
            subtitle__b6: "NormalCard_subtitle__b6_51",
            subtitle__b6__medium: "NormalCard_subtitle__b6__medium_94",
            subtitle__b6__extraLarge: "NormalCard_subtitle__b6__extraLarge_34",
            subtitle__b6__large: "NormalCard_subtitle__b6__large_f3",
            subtitle__normal: "NormalCard_subtitle__normal_23",
            subtitle__noReward: "NormalCard_subtitle__noReward_9c",
            subtitle__statusActive: "NormalCard_subtitle__statusActive_8c",
            subtitle__staticPrepare: "NormalCard_subtitle__staticPrepare_7c",
            subtitle__anim: "NormalCard_subtitle__anim_07",
            subtitle__disable: "NormalCard_subtitle__disable_9d",
            statusDescription: "NormalCard_statusDescription_9b",
            statusDescription__position: "NormalCard_statusDescription__position_e1",
            statusDescription__color: "NormalCard_statusDescription__color_b5",
            belowStatus: "NormalCard_belowStatus_05",
            calendarIcon: "NormalCard_calendarIcon_c1",
            calendarIcon__hover: "NormalCard_calendarIcon__hover_7c",
            calendarIcon__extraSmall: "NormalCard_calendarIcon__extraSmall_9a",
            calendarIcon__small: "NormalCard_calendarIcon__small_3d",
            timeLeft: "NormalCard_timeLeft_28",
            timeLeft__small: "NormalCard_timeLeft__small_a5",
            footer: "NormalCard_footer_ba",
            footer__medium: "NormalCard_footer__medium_77",
            footer__extraLarge: "NormalCard_footer__extraLarge_5e",
            footer__large: "NormalCard_footer__large_69",
            footer__anim: "NormalCard_footer__anim_73",
            mask: "NormalCard_mask_ee",
            mask__b0: "NormalCard_mask__b0_e9",
            mask__b1: "NormalCard_mask__b1_02",
            mask__b0__medium: "NormalCard_mask__b0__medium_ac",
            mask__b1__medium: "NormalCard_mask__b1__medium_26",
            mask__b0__extraLarge: "NormalCard_mask__b0__extraLarge_28",
            mask__b0__large: "NormalCard_mask__b0__large_d1",
            mask__b1__extraLarge: "NormalCard_mask__b1__extraLarge_74",
            mask__b1__large: "NormalCard_mask__b1__large_74",
            mask__b2: "NormalCard_mask__b2_71",
            mask__b2__medium: "NormalCard_mask__b2__medium_b2",
            mask__b2__extraLarge: "NormalCard_mask__b2__extraLarge_6c",
            mask__b2__large: "NormalCard_mask__b2__large_b2",
            mask__b3: "NormalCard_mask__b3_f4",
            mask__b3__medium: "NormalCard_mask__b3__medium_d1",
            mask__b3__extraLarge: "NormalCard_mask__b3__extraLarge_3a",
            mask__b3__large: "NormalCard_mask__b3__large_17",
            mask__b4: "NormalCard_mask__b4_3c",
            mask__b4__medium: "NormalCard_mask__b4__medium_b1",
            mask__b4__extraLarge: "NormalCard_mask__b4__extraLarge_4c",
            mask__b4__large: "NormalCard_mask__b4__large_ed",
            mask__b5: "NormalCard_mask__b5_85",
            mask__b5__medium: "NormalCard_mask__b5__medium_99",
            mask__b5__extraLarge: "NormalCard_mask__b5__extraLarge_8a",
            mask__b5__large: "NormalCard_mask__b5__large_cc",
            mask__b6: "NormalCard_mask__b6_90",
            mask__b6__medium: "NormalCard_mask__b6__medium_fe",
            mask__b6__extraLarge: "NormalCard_mask__b6__extraLarge_97",
            mask__b6__large: "NormalCard_mask__b6__large_bc",
            mask__static: "NormalCard_mask__static_ae",
            mask__anim: "NormalCard_mask__anim_b6",
            icon: "NormalCard_icon_cb",
            icon__animPrepare: "NormalCard_icon__animPrepare_a2",
            icon__anim__b0: "NormalCard_icon__anim__b0_e3",
            icon__anim__b1: "NormalCard_icon__anim__b1_04",
            icon__anim__b2: "NormalCard_icon__anim__b2_19",
            icon__anim__b3: "NormalCard_icon__anim__b3_e8",
            icon__static__b0: "NormalCard_icon__static__b0_3c",
            icon__static__b1: "NormalCard_icon__static__b1_36",
            icon__static__b2: "NormalCard_icon__static__b2_13",
            icon__static__b3: "NormalCard_icon__static__b3_6d",
            icon__static__b0__medium: "NormalCard_icon__static__b0__medium_64",
            icon__static__b1__medium: "NormalCard_icon__static__b1__medium_b9",
            icon__anim__b0__medium: "NormalCard_icon__anim__b0__medium_a6",
            icon__anim__b1__medium: "NormalCard_icon__anim__b1__medium_6c",
            icon__static__b0__extraLarge: "NormalCard_icon__static__b0__extraLarge_0b",
            icon__static__b0__large: "NormalCard_icon__static__b0__large_7c",
            icon__static__b1__extraLarge: "NormalCard_icon__static__b1__extraLarge_8b",
            icon__static__b1__large: "NormalCard_icon__static__b1__large_f0",
            icon__anim__b0__extraLarge: "NormalCard_icon__anim__b0__extraLarge_2c",
            icon__anim__b0__large: "NormalCard_icon__anim__b0__large_07",
            icon__anim__b1__extraLarge: "NormalCard_icon__anim__b1__extraLarge_a7",
            icon__anim__b1__large: "NormalCard_icon__anim__b1__large_0a",
            icon__static__b2__medium: "NormalCard_icon__static__b2__medium_92",
            icon__anim__b2__medium: "NormalCard_icon__anim__b2__medium_da",
            icon__static__b2__extraLarge: "NormalCard_icon__static__b2__extraLarge_99",
            icon__static__b2__large: "NormalCard_icon__static__b2__large_e3",
            icon__anim__b2__extraLarge: "NormalCard_icon__anim__b2__extraLarge_8e",
            icon__anim__b2__large: "NormalCard_icon__anim__b2__large_94",
            icon__static__b3__medium: "NormalCard_icon__static__b3__medium_1a",
            icon__anim__b3__medium: "NormalCard_icon__anim__b3__medium_eb",
            icon__static__b3__extraLarge: "NormalCard_icon__static__b3__extraLarge_a0",
            icon__static__b3__large: "NormalCard_icon__static__b3__large_e3",
            icon__anim__b3__extraLarge: "NormalCard_icon__anim__b3__extraLarge_92",
            icon__anim__b3__large: "NormalCard_icon__anim__b3__large_7a",
            icon__huge: "NormalCard_icon__huge_56",
            icon__big: "NormalCard_icon__big_c9",
            icon__medium: "NormalCard_icon__medium_87",
            icon__small: "NormalCard_icon__small_a6",
            icon__b0: "NormalCard_icon__b0_f2",
            icon__b1: "NormalCard_icon__b1_50",
            icon__b0__medium: "NormalCard_icon__b0__medium_d8",
            icon__b1__medium: "NormalCard_icon__b1__medium_d4",
            icon__b0__extraLarge: "NormalCard_icon__b0__extraLarge_3b",
            icon__b0__large: "NormalCard_icon__b0__large_32",
            icon__b1__extraLarge: "NormalCard_icon__b1__extraLarge_db",
            icon__b1__large: "NormalCard_icon__b1__large_53",
            icon__b2: "NormalCard_icon__b2_ae",
            icon__b2__medium: "NormalCard_icon__b2__medium_17",
            icon__b2__extraLarge: "NormalCard_icon__b2__extraLarge_b9",
            icon__b2__large: "NormalCard_icon__b2__large_a7",
            icon__b3: "NormalCard_icon__b3_28",
            icon__b3__medium: "NormalCard_icon__b3__medium_74",
            icon__b3__extraLarge: "NormalCard_icon__b3__extraLarge_64",
            icon__b3__large: "NormalCard_icon__b3__large_89",
            icon__b4: "NormalCard_icon__b4_f8",
            icon__b4__medium: "NormalCard_icon__b4__medium_c6",
            icon__b4__extraLarge: "NormalCard_icon__b4__extraLarge_eb",
            icon__b4__large: "NormalCard_icon__b4__large_90",
            icon__b5: "NormalCard_icon__b5_e9",
            icon__b5__medium: "NormalCard_icon__b5__medium_df",
            icon__b5__extraLarge: "NormalCard_icon__b5__extraLarge_e3",
            icon__b5__large: "NormalCard_icon__b5__large_2d",
            icon__b6: "NormalCard_icon__b6_dc",
            icon__b6__medium: "NormalCard_icon__b6__medium_73",
            icon__b6__extraLarge: "NormalCard_icon__b6__extraLarge_63",
            icon__b6__large: "NormalCard_icon__b6__large_c3",
            statusNotActive: "NormalCard_statusNotActive_9c",
            statusNotActive__b0: "NormalCard_statusNotActive__b0_4f",
            statusNotActive__b1: "NormalCard_statusNotActive__b1_78",
            statusNotActive__b0__medium: "NormalCard_statusNotActive__b0__medium_8f",
            statusNotActive__b1__medium: "NormalCard_statusNotActive__b1__medium_f6",
            statusNotActive__b0__extraLarge: "NormalCard_statusNotActive__b0__extraLarge_33",
            statusNotActive__b0__large: "NormalCard_statusNotActive__b0__large_bf",
            statusNotActive__b1__extraLarge: "NormalCard_statusNotActive__b1__extraLarge_d8",
            statusNotActive__b1__large: "NormalCard_statusNotActive__b1__large_10",
            statusNotActive__b2: "NormalCard_statusNotActive__b2_35",
            statusNotActive__b2__medium: "NormalCard_statusNotActive__b2__medium_f9",
            statusNotActive__b2__extraLarge: "NormalCard_statusNotActive__b2__extraLarge_09",
            statusNotActive__b2__large: "NormalCard_statusNotActive__b2__large_a0",
            statusNotActive__b3: "NormalCard_statusNotActive__b3_fe",
            statusNotActive__b3__medium: "NormalCard_statusNotActive__b3__medium_88",
            statusNotActive__b3__extraLarge: "NormalCard_statusNotActive__b3__extraLarge_b2",
            statusNotActive__b3__large: "NormalCard_statusNotActive__b3__large_69",
            statusNotActive__b4: "NormalCard_statusNotActive__b4_dd",
            statusNotActive__b4__medium: "NormalCard_statusNotActive__b4__medium_ae",
            statusNotActive__b4__extraLarge: "NormalCard_statusNotActive__b4__extraLarge_78",
            statusNotActive__b4__large: "NormalCard_statusNotActive__b4__large_d5",
            statusNotActive__b5: "NormalCard_statusNotActive__b5_02",
            statusNotActive__b5__medium: "NormalCard_statusNotActive__b5__medium_24",
            statusNotActive__b5__extraLarge: "NormalCard_statusNotActive__b5__extraLarge_f4",
            statusNotActive__b5__large: "NormalCard_statusNotActive__b5__large_1f",
            statusNotActive__b6: "NormalCard_statusNotActive__b6_9d",
            statusNotActive__b6__medium: "NormalCard_statusNotActive__b6__medium_cd",
            statusNotActive__b6__extraLarge: "NormalCard_statusNotActive__b6__extraLarge_09",
            statusNotActive__b6__large: "NormalCard_statusNotActive__b6__large_09",
            widgetOverlay__hide: "NormalCard_widgetOverlay__hide_7e",
            darken__show: "NormalCard_darken__show_3f",
          };
        var Oe = a(8668);
        const He = [
          "name",
          "eventName",
          "statusNotActive",
          "description",
          "conditions",
          "children",
          "onHoverChanged",
          "calendarTooltip",
          "widgetComponent",
          "battlePassState",
          "isDisabled",
          "timeLeft",
          "rewardList",
          "statusActive",
          "divider",
          "belowStatusComponent",
          "nameSuffixComponent",
          "forceShowIcon",
          "hideStatus",
          "noWidgetSizes",
          "classNames",
          "resourceFolderGetter",
        ];
        function $e() {
          return (
            ($e =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            $e.apply(this, arguments)
          );
        }
        const ze = (e) => {
            let t = e.name,
              a = e.eventName,
              _ = e.statusNotActive,
              u = e.description,
              i = e.conditions,
              s = e.children,
              l = e.onHoverChanged,
              c = e.calendarTooltip,
              m = void 0 === c ? "" : c,
              d = e.widgetComponent,
              b = e.battlePassState,
              g = e.isDisabled,
              E = e.timeLeft,
              p = e.rewardList,
              A = e.statusActive,
              C = e.divider,
              F = void 0 === C ? " " : C,
              B = e.belowStatusComponent,
              h = e.nameSuffixComponent,
              D = e.forceShowIcon,
              f = void 0 !== D && D,
              v = e.hideStatus,
              x = void 0 !== v && v,
              S = e.noWidgetSizes,
              w = void 0 === S ? [re.Id.B5, re.Id.B6] : S,
              k = e.classNames,
              N = e.resourceFolderGetter,
              T = void 0 === N ? re.d6 : N,
              y = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, He);
            const L = (0, ge.O)(),
              W = (0, ue.Z)(
                [
                  ...(0, re.Hp)(
                    "base",
                    "icon",
                    "footer",
                    "name",
                    "subtitle",
                    "mask",
                    "formatText",
                    "icon__anim",
                    "icon__static",
                    "statusNotActive",
                  ),
                  "calendarIcon",
                ],
                Pe,
              ),
              I = J("model", K.None),
              P = I.onItemClicked,
              O = I.onInfoClicked,
              H = y.resourcesFolderName,
              $ = y.size,
              z = y.isSelected,
              G = y.showWidget,
              U = y.isNew,
              j = y.modeName,
              V = y.index,
              q = y.isLocked,
              Z = (0, ge.B)(l),
              Y = Z[0],
              X = Z[1],
              Q = (0, r.useMemo)(() => Oe.S4[$][L], [$, L]),
              ee = (0, r.useMemo)(() => {
                const e = T(H);
                if (null !== e) {
                  const t = q ? e.$dyn(`icon_${Q}_locked`) : e.$dyn(`icon_${Q}`);
                  if (void 0 !== t) return { backgroundImage: `url(${t})` };
                }
              }, [T, H, Q, q]),
              te = G || z,
              ae = Oe.Hi.includes($),
              _e = $ === re.Id.B1,
              ne = $ === re.Id.B2,
              ie = $ === re.Id.B3,
              oe = Oe.u_.includes($),
              se = !w.includes($) && G && d,
              le = te && !ae,
              ce = Y && !q && !ae && !te,
              me = Y || (z && A),
              de = L !== re.Cg.Big,
              Ee = p && p.length > 0 && !_ && oe,
              pe = (0, r.useMemo)(
                () =>
                  g
                    ? R.strings.ranked_battles.rankedBattlesUnreachableView.subtitleText()
                    : A || a || void 0,
                [g, A, a],
              ),
              Ae = (0, r.useMemo)(
                () => (oe || ie ? _ || "" : void 0 === _ ? "" : _.replace("\n", " ")),
                [oe, _, ie],
              );
            let Ce = "";
            _e && u === pe ? i && (Ce = (0, M.z4)(i)) : (Ce = (0, M.z4)(u + F + i));
            const Be = o()(
                Pe.icon,
                Pe[`icon__${Q}`],
                W[`icon__${$}`],
                !ae && Pe.icon__animPrepare,
                le && W[`icon__static__${$}`],
                ce && W[`icon__anim__${$}`],
              ),
              he = o()(Pe.mask, W[`mask__${$}`], le && Pe.mask__static, ce && Pe.mask__anim),
              De = o()(
                W.subtitle,
                W[`subtitle__${$}`],
                (a || !ae) && Pe.subtitle__normal,
                !oe && Pe.subtitle__noReward,
                A && ae && Pe.subtitle__statusActive,
                A && te && Pe.subtitle__staticPrepare,
                me && Pe.subtitle__anim,
                g && Pe.subtitle__disable,
                null == k ? void 0 : k.subtitle,
              ),
              ve = o()(
                Pe.statusDescription,
                ne && Pe.statusDescription__position,
                oe && Pe.statusDescription__color,
              ),
              xe = o()(
                W.footer,
                (Y || z) && !G && ie && Pe.footer__anim,
                null == k ? void 0 : k.footer,
              ),
              we = o()(W.formatText, W[`formatText__${$}`]),
              ke = o()(Pe.darken, G && Pe.darken__show),
              Ne = o()(
                Pe.widgetOverlay,
                !se && Pe.widgetOverlay__hide,
                null == k ? void 0 : k.widgetOverlay,
              ),
              Te = Ce && oe && !g && !q && (!se || oe);
            return n().createElement(
              "div",
              { className: o()(W.base, W[`base__${$}`]) },
              n().createElement(
                Fe,
                $e({ onHoverChanged: X, isDisabled: g }, y, {
                  onItemClicked: P,
                  onInfoClicked: O,
                  resourceFolderGetter: T,
                }),
                Ee && n().createElement(Ie, { size: $, rewardsList: p, isLocked: q }),
                _ &&
                  n().createElement(
                    "div",
                    { className: o()(W.statusNotActive, W[`statusNotActive__${$}`]) },
                    n().createElement(be.B, { text: Ae, classMix: we }),
                  ),
                n().createElement("div", { className: ke }),
                d && n().createElement("div", { className: Ne }, d),
                s,
                (!se || f) &&
                  n().createElement(
                    "div",
                    { className: he },
                    n().createElement("div", { className: Be, style: ee }),
                  ),
                n().createElement(
                  "div",
                  {
                    className: o()(Pe.name, W.name, W[`name__${$}`], null == k ? void 0 : k.name, {
                      [Pe.name__locked]: q,
                    }),
                  },
                  t,
                  h,
                ),
                n().createElement(
                  "div",
                  { className: De },
                  !x &&
                    !q &&
                    (!ne || g) &&
                    n().createElement(be.B, { classMix: we, text: pe || "" }),
                  Te &&
                    n().createElement(
                      "div",
                      { className: ve },
                      n().createElement(be.B, { classMix: we, text: Ce }),
                    ),
                  B &&
                    n().createElement(
                      "div",
                      { className: o()(Pe.belowStatus, null == k ? void 0 : k.belowStatus) },
                      B,
                    ),
                ),
                i &&
                  !q &&
                  n().createElement(
                    "div",
                    { className: xe },
                    n().createElement(be.B, { classMix: we, text: (0, M.z4)(i) }),
                  ),
                E &&
                  !U &&
                  n().createElement(fe, {
                    index: V,
                    text: E,
                    isSmall: de,
                    classMix: o()(Pe.timeLeft, de && Pe.timeLeft__small),
                    tooltipId: m,
                    modeName: j,
                  }),
                n().createElement(Se, {
                  modeName: j,
                  isDisabled: g,
                  battlePassState: b,
                  isLocked: q,
                }),
              ),
            );
          },
          Ge = {
            widgetOverlay: "Card_widgetOverlay_a5",
            belowStatus: "Card_belowStatus_b6",
            base__b1: "Card_base__b1_6f",
            subtitle: "Card_subtitle_4a",
            base__b2: "Card_base__b2_53",
            name: "Card_name_d9",
          };
        var Ue = a(7590),
          je = a(7736);
        const Ve = {
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
          qe =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          Ze = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          Ye = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          Xe = (0, r.memo)(({ text: e, binding: t, classMix: a }) => {
            const _ = (0, r.useCallback)((e) => ({ color: `#${e}` }), []),
              u = (0, r.useMemo)(() => t || {}, [t]);
            let i = qe.exec(e),
              o = e,
              s = 0;
            for (; i;) {
              const a = i[0],
                r = Ze.exec(a),
                l = Ye.exec(a),
                c = i[1];
              if (r && l) {
                const e = r[0],
                  i = e + s++ + e;
                ((o = o.replace(a, `%(${i})`)),
                  (u[i] = Ve[e]
                    ? n().createElement(
                        "span",
                        { className: Ve[e] },
                        n().createElement(de.z, { text: c, binding: t }),
                      )
                    : n().createElement(
                        "span",
                        { style: _(e) },
                        n().createElement(de.z, { text: c, binding: t }),
                      )));
              }
              i = qe.exec(e);
            }
            return n().createElement(de.z, { text: o, classMix: a, binding: u });
          }),
          Ke = {
            base: "Progression_base_94",
            title: "Progression_title_81",
            contentWrapper: "Progression_contentWrapper_3a",
            progress: "Progression_progress_7b",
            currentStage: "Progression_currentStage_67",
            progressValue: "Progression_progressValue_f7",
            progressValueIcon: "Progression_progressValueIcon_e9",
          },
          Je = R.strings.mode_selector.mode.battleRoyale.progression,
          Qe = {
            freezed: !1,
            withStack: !1,
            type: je.r.Growing,
            delta: { duration: 2e3, delay: 100 },
            line: { duration: 2e3, delay: 100 },
          },
          et = ({
            status: e = ne.ACTIVE,
            currentStage: t,
            stageCurrentPoints: a,
            stageMaximumPoints: _,
          }) =>
            n().createElement(
              "div",
              { className: o()(Ke.base, Ke[`base__${e}`]) },
              n().createElement(
                "div",
                { className: Ke.contentWrapper },
                a !== _ &&
                  e === ne.ACTIVE &&
                  n().createElement(
                    "div",
                    { className: Ke.progress },
                    n().createElement(
                      "div",
                      { className: Ke.currentStage },
                      Je.currentStage(),
                      n().createElement("span", null, t),
                    ),
                    n().createElement(Ue.ko, {
                      size: Ue.$u.Small,
                      value: a,
                      maxValue: _,
                      animationSettings: Qe,
                      deltaFrom: a,
                    }),
                    n().createElement(
                      "div",
                      { className: Ke.progressValue },
                      n().createElement(Xe, { text: Je.steps(), binding: { done: a, total: _ } }),
                      n().createElement("div", { className: Ke.progressValueIcon }),
                    ),
                  ),
              ),
            ),
          tt = ["size", "showWidget", "widget", "name"];
        function at() {
          return (
            (at =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            at.apply(this, arguments)
          );
        }
        const _t = (e) => {
          let t = e.size,
            a = e.showWidget,
            _ = e.widget,
            u = e.name,
            r = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, tt);
          const i = t === re.Id.B1 && a;
          return n().createElement(
            "div",
            { className: Ge[`base__${t}`] },
            n().createElement(
              ze,
              at(
                {
                  showWidget: a,
                  size: t,
                  belowStatusComponent: i && n().createElement(et, _),
                  classNames: { belowStatus: Ge.belowStatus, subtitle: Ge.subtitle, name: Ge.name },
                },
                r,
                { name: n().createElement(de.z, { text: u }) },
              ),
            ),
          );
        };
        let ut;
        !(function (e) {
          ((e[(e.First = 6)] = "First"),
            (e[(e.Second = 5)] = "Second"),
            (e[(e.Third = 4)] = "Third"),
            (e[(e.Fourth = 3)] = "Fourth"),
            (e[(e.Fifth = 2)] = "Fifth"),
            (e[(e.Sixth = 1)] = "Sixth"));
        })(ut || (ut = {}));
        class rt extends n().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = I.B3.GOLD;
            else e = I.B3.INTEGRAL;
            const t = I.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        rt.defaultProps = { format: "integral" };
        var nt = a(4322);
        const it = "FailedFetchPointsText_base_be",
          ot = "FailedFetchPointsText_icon_76",
          st = "FailedFetchPointsText_text_ea",
          lt = ({ containerStyles: e }) =>
            n().createElement(
              "div",
              { className: o()(it, e) },
              n().createElement("div", { className: ot }),
              n().createElement(nt.ZP, {
                text: R.strings.comp7.honorsPlace.failedFetchPointsText(),
                className: st,
              }),
            ),
          ct = "HonorsPlace_base_57",
          mt = "HonorsPlace_base__error_c4",
          dt = "HonorsPlace_base__tooltip_b9",
          bt = "HonorsPlace_base__tooltipError_3c",
          gt = "HonorsPlace_transferPlace_46",
          Et = "HonorsPlace_elitePlace_eb",
          pt = "HonorsPlace_elitePlace__bronze_5b",
          At = "HonorsPlace_elitePlace__silver_cd",
          Ct = "HonorsPlace_elitePlace__gold_87",
          Ft = "HonorsPlace_elitePlace__tooltip_0a",
          Bt = "HonorsPlace_elitePlace__modeSelector_dc",
          ht = "HonorsPlace_garland_ab",
          Dt = "HonorsPlace_garland__transferPlaceLeft_e7",
          ft = "HonorsPlace_garland__transferPlaceLeft__tooltip_23",
          vt = "HonorsPlace_garland__transferPlaceLeft__modeSelector_5a",
          xt = "HonorsPlace_garland__transferPlaceRight_d4",
          St = "HonorsPlace_garland__transferPlaceRight__tooltip_20",
          wt = "HonorsPlace_garland__transferPlaceRight__modeSelector_9f",
          kt = "HonorsPlace_garland__tooltip_3f",
          Nt = "HonorsPlace_garland__modeSelector_e0",
          Tt = "HonorsPlace_placeText_23",
          yt = "HonorsPlace_placeText__transfer_d3",
          Lt = "HonorsPlace_placeText__transfer__copied_0f",
          Mt = "HonorsPlace_placeText__tooltip_98",
          Rt = "HonorsPlace_placeText__notInLeaderboard_81",
          Wt = "HonorsPlace_placeText__modeSelector_57",
          It = "HonorsPlace_positionTitle_c9",
          Pt = "HonorsPlace_positionTitle__tooltip_8a",
          Ot = "HonorsPlace_positionTitle__modeSelector_c7",
          Ht = "HonorsPlace_titleDescriptionContainer_15",
          $t = "HonorsPlace_descriptionText_b8",
          zt = "HonorsPlace_descriptionText__tooltip_70",
          Gt = "HonorsPlace_descriptionText__withoutMargin_a9",
          Ut = "HonorsPlace_descriptionText__blackout_3a",
          jt = "HonorsPlace_rankInactivityCount_34",
          Vt = "HonorsPlace_failedFetchPointsText_e2",
          qt = (0, r.memo)(({ datetime: e, format: t = W.SHORT_DATE, localize: a = !0 }) =>
            ((e, t, a) => {
              switch (t) {
                case W.SHORT_DATE:
                  return a
                    ? I.Z5.getDateFormat(e, I.kH.SHORT_FORMAT)
                    : I.cy.getTimeFormat("%d.%m.%y", e, !0);
                case W.SHORT_TIME:
                  return a
                    ? I.Z5.getTimeFormat(e, I.lf.SHORT_FORMAT)
                    : I.cy.getTimeFormat("%I:%M %p", e, !0);
                case W.SHORT_DATE_TIME:
                  return a
                    ? `${I.Z5.getDateFormat(e, I.kH.SHORT_FORMAT)}, ${I.Z5.getTimeFormat(e, I.lf.SHORT_FORMAT)}`
                    : I.cy.getTimeFormat("%d.%m.%y, %I:%M %p", e, !0);
                case W.FULL_DATE:
                  return a
                    ? I.Z5.getDateFormat(e, I.kH.LONG_FORMAT)
                    : I.cy.getTimeFormat("%B %d, %Y", e, !0);
                case W.FULL_DATE_TIME:
                  return a
                    ? `${I.Z5.getDateFormat(e, I.kH.LONG_FORMAT)}, ${I.Z5.getTimeFormat(e, I.lf.SHORT_FORMAT)}`
                    : I.cy.getTimeFormat("%B %d, %Y, %I:%M %p", e, !0);
                case W.MONTH:
                  return I.cy.getTimeFormat("%B", e, !0);
                case W.MONTH_DATE:
                  return I.cy.getTimeFormat("%B %e", e, !0);
                case W.DATE_MONTH:
                  return I.cy.getTimeFormat("%e %B", e, !0);
                case W.MONTH_YEAR:
                  return I.cy.getTimeFormat("%B %Y", e, !0);
                case W.WEEK_DAY:
                  return I.cy.getTimeFormat("%A", e, !0);
                case W.WEEK_DAY_TIME:
                  return a
                    ? `${I.cy.getTimeFormat("%A", e, !0)} ${I.Z5.getTimeFormat(e, I.lf.SHORT_FORMAT)}`
                    : I.cy.getTimeFormat("%A, %I:%M %p", e, !0);
                case W.YEAR:
                  return I.cy.getTimeFormat("%Y", e, !0);
                case W.DATE_YEAR:
                  return I.cy.getTimeFormat("%d, %Y", e, !0);
              }
            })(e, t, a),
          ),
          Zt =
            ((0, M.uF)(R.strings.comp7.lastUpdateNote.lastBestUserPoints.description(), {
              count: 15,
            }),
            "LastUpdateNote_base_7f"),
          Yt = "LastUpdateNote_infoIcon_5c",
          Xt = "LastUpdateNote_lineDivider_2c";
        let Kt;
        !(function (e) {
          ((e[(e.ICON = 0)] = "ICON"), (e[(e.LINE = 1)] = "LINE"));
        })(Kt || (Kt = {}));
        const Jt = R.strings.comp7.lastUpdateNote,
          Qt = ({
            timestamp: e,
            className: t,
            classNames: a,
            dateTimeFormat: _ = W.SHORT_TIME,
            dividerType: u = Kt.ICON,
          }) =>
            n().createElement(
              "div",
              { className: o()(Zt, t) },
              n().createElement(nt.ZP, {
                text: Jt.info(),
                format: { binding: { date: n().createElement(qt, { datetime: e, format: _ }) } },
              }),
              u === Kt.ICON &&
                n().createElement(
                  L.i,
                  { body: Jt.tooltip.info() },
                  n().createElement("div", { className: o()(Yt, null == a ? void 0 : a.icon) }),
                ),
              u === Kt.LINE &&
                n().createElement("div", { className: o()(Xt, null == a ? void 0 : a.line) }),
            ),
          ea = "RankInactivityCount_base_c2",
          ta = "RankInactivityCount_count_28",
          aa = "RankInactivityCount_iconContainer_85",
          _a = "RankInactivityCount_icon_52",
          ua = ({ count: e, containerStyles: t }) => {
            const a = o()(ea, t);
            return n().createElement(
              Ae.u,
              {
                ignoreShowDelay: !0,
                contentId: R.views.lobby.comp7.tooltips.RankInactivityTooltip("resId"),
                args: { count: e },
              },
              n().createElement(
                "div",
                { className: a },
                n().createElement("div", { className: ta }, e),
                n().createElement(
                  "div",
                  { className: aa },
                  n().createElement("div", { className: _a }),
                ),
              ),
            );
          },
          ra = R.strings.comp7.honorsPlace.description;
        var na;
        let ia;
        (!(function (e) {
          ((e[(e.BRONZE = 3)] = "BRONZE"),
            (e[(e.SILVER = 2)] = "SILVER"),
            (e[(e.GOLD = 1)] = "GOLD"),
            (e[(e.NOT_IN_LEADERBOARD = 0)] = "NOT_IN_LEADERBOARD"),
            (e[(e.ERROR = -1)] = "ERROR"));
        })(na || (na = {})),
          (function (e) {
            ((e.PROGRESSION = "PROGRESSION"),
              (e.TOOLTIP = "TOOLTIP"),
              (e.MODE_SELECTOR = "MODE_SELECTOR"));
          })(ia || (ia = {})));
        const oa = ({ mode: e, model: t }) => {
          var a, _;
          const u = t.root.get(),
            r = u.myPosition,
            i = u.currentScore,
            s = u.rankInactivityCount,
            l = u.leaderboardUpdateTimestamp,
            c =
              null == t || null == (a = t.computes) || null == a.hasCurrentItemRankInactivity
                ? void 0
                : a.hasCurrentItemRankInactivity(),
            m = r === na.ERROR,
            d = r === na.BRONZE,
            b = r === na.SILVER,
            g = r === na.GOLD,
            E = !m && (d || b || g),
            p = r === na.NOT_IN_LEADERBOARD,
            A = e === ia.TOOLTIP,
            C = e === ia.MODE_SELECTOR,
            F = (({
              isErrorLoadingPointsValue: e,
              isElitePlace: t,
              isTooltip: a,
              isBronze: _,
              isSilver: u,
              isGold: r,
              isNotInLeaderboard: n,
              isModeSelector: i,
            }) => {
              const s = o()(ct, e && !a && mt, a && e && bt, a && dt),
                l = o()(It, a && Pt, i && Ot);
              return {
                baseStyles: s,
                leftGarlandStyle: o()(ht, !t && Dt, a && ft, a && kt, i && Nt, i && vt),
                rightGarlandStyle: o()(ht, !t && xt, a && St, a && kt, i && Nt, i && wt),
                placeTextStyle: o()(Tt, !t && yt, a && Mt, n && Rt, i && Wt),
                placeTextCopiedStyle: o()(Tt, yt, Lt, a && Mt, n && Rt, i && Wt),
                elitePlaceStyle: o()(Et, _ && pt, u && At, r && Ct, a && Ft, i && Bt),
                positionTitleStyle: l,
                lastUpdateNoteStyle: o()($t, a && zt, a && Ut),
              };
            })({
              isErrorLoadingPointsValue: m,
              isElitePlace: E,
              isTooltip: A,
              isBronze: d,
              isSilver: b,
              isGold: g,
              isNotInLeaderboard: p,
              isModeSelector: C,
            }),
            B = F.baseStyles,
            h = F.leftGarlandStyle,
            D = F.rightGarlandStyle,
            f = F.placeTextStyle,
            v = F.placeTextCopiedStyle,
            x = F.elitePlaceStyle,
            S = F.positionTitleStyle,
            w = F.lastUpdateNoteStyle,
            k =
              e === ia.PROGRESSION &&
              (null == (_ = t.computes) || null == _.hasCurrentItemRankInactivity
                ? void 0
                : _.hasCurrentItemRankInactivity()),
            N = p ? "--" : I.Z5.getNumberFormat(r, I.B3.INTEGRAL);
          return n().createElement(
            "div",
            { className: B },
            m && !C && n().createElement(lt, { containerStyles: Vt }),
            !m &&
              n().createElement(
                n().Fragment,
                null,
                E
                  ? n().createElement("div", { className: x })
                  : n().createElement(
                      "div",
                      { className: gt },
                      n().createElement("div", { className: h }),
                      n().createElement(nt.ZP, { text: String(N), className: f }),
                      n().createElement(nt.ZP, { text: String(N), className: v }),
                      n().createElement("div", { className: D }),
                    ),
                n().createElement(nt.ZP, { text: ra.title(), className: S }),
              ),
            n().createElement(
              "div",
              { className: Ht },
              !m &&
                "number" == typeof l &&
                n().createElement(Qt, {
                  timestamp: l,
                  className: w,
                  dividerType: A ? Kt.LINE : Kt.ICON,
                }),
              !C &&
                n().createElement(Xe, {
                  text: ra.ratingCount(),
                  binding: { count: n().createElement(rt, { value: i }) },
                  classMix: o()($t, A && zt, A && Gt),
                }),
              c &&
                "number" == typeof s &&
                k &&
                n().createElement(ua, { count: s, containerStyles: jt }),
            ),
          );
        };
        let sa, la;
        (!(function (e) {
          ((e[(e.A = 1)] = "A"),
            (e[(e.B = 2)] = "B"),
            (e[(e.C = 3)] = "C"),
            (e[(e.D = 4)] = "D"),
            (e[(e.E = 5)] = "E"));
        })(sa || (sa = {})),
          (function (e) {
            ((e[(e.Achieved = 0)] = "Achieved"),
              (e[(e.Current = 1)] = "Current"),
              (e[(e.Inactive = 2)] = "Inactive"));
          })(la || (la = {})));
        const ca = R.strings.comp7.division,
          ma = { [sa.A]: "A", [sa.B]: "B", [sa.C]: "C", [sa.D]: "D", [sa.E]: "E" },
          da = (e) => ca.$dyn(ma[e]);
        let ba;
        !(function (e) {
          ((e[(e.First = 6)] = "First"),
            (e[(e.Second = 5)] = "Second"),
            (e[(e.Third = 4)] = "Third"),
            (e[(e.Fourth = 3)] = "Fourth"),
            (e[(e.Fifth = 2)] = "Fifth"),
            (e[(e.Sixth = 1)] = "Sixth"));
        })(ba || (ba = {}));
        const ga = {
            [ba.First]: "first",
            [ba.Second]: "second",
            [ba.Third]: "third",
            [ba.Fourth]: "fourth",
            [ba.Fifth]: "fifth",
            [ba.Sixth]: "sixth",
          },
          Ea = (e) => ((e, t) => `${e.$dyn(ga[t])}`)(R.strings.comp7.rank, e),
          pa = [ba.First, ba.Second, ba.Third, ba.Fourth, ba.Fifth, ba.Sixth],
          Aa = (e) => pa.includes(e);
        let Ca, Fa, Ba;
        (!(function (e) {
          ((e.Previous = "previous"), (e.Current = "current"), (e.Future = "future"));
        })(Ca || (Ca = {})),
          (function (e) {
            ((e[(e.Page = 0)] = "Page"),
              (e[(e.Maps = 1)] = "Maps"),
              (e[(e.SeasonVehicles = 2)] = "SeasonVehicles"));
          })(Fa || (Fa = {})),
          (function (e) {
            ((e[(e.BASIC = 0)] = "BASIC"),
              (e[(e.TRANSFER = 1)] = "TRANSFER"),
              (e[(e.ELITE = 2)] = "ELITE"));
          })(Ba || (Ba = {})));
        const ha = {
            widget: "Comp7BattleCard_widget_3b",
            base__b0: "Comp7BattleCard_base__b0_91",
            base__b1: "Comp7BattleCard_base__b1_30",
            base__b2: "Comp7BattleCard_base__b2_da",
            base__b3: "Comp7BattleCard_base__b3_23",
            belowStatus: "Comp7BattleCard_belowStatus_48",
          },
          Da = "QualificationCounter_base_fb",
          fa = "QualificationCounter_dash_e2",
          va = "QualificationCounter_dash__right_3e",
          xa = "QualificationCounter_iconContainer_c3",
          Sa = "QualificationCounter_battleIcon_2e",
          wa = "QualificationCounter_score_3b",
          ka = ({ battlesCount: e, maxBattlesCount: t, className: a }) =>
            n().createElement(
              "div",
              { className: o()(Da, a) },
              n().createElement("div", { className: fa }),
              n().createElement(Xe, {
                text: R.strings.comp7.qualification.battlesCounter(),
                binding: {
                  battleIcon: n().createElement(
                    "div",
                    { className: xa },
                    n().createElement("div", { className: Sa }),
                  ),
                  battlesCount: e,
                  maxBattlesCount: t,
                },
                classMix: wa,
              }),
              n().createElement("div", { className: o()(fa, va) }),
            ),
          Na = (e) => {
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
        var Ta = a(3403),
          ya = a(7030);
        const La = {
            [ba.First]: "first",
            [ba.Second]: "second",
            [ba.Third]: "third",
            [ba.Fourth]: "fourth",
            [ba.Fifth]: "fifth",
            [ba.Sixth]: "sixth",
          },
          Ma = (e) => La[e],
          Ra = "RankEmblem_base_ec";
        let Wa;
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
        })(Wa || (Wa = {}));
        const Ia = ({ rank: e, size: t, division: a, className: _ }) => {
            const u = (0, r.useMemo)(() => {
              const _ = R.images.comp7.gui.maps.icons.comp7.ranks.$num(t),
                u = Aa(e) && void 0 !== a ? `_${da(a)}` : "";
              return {
                backgroundImage: `url(${_.$dyn(`${Ma(e)}${u}`)})`,
                "--imageSize": `${t}rem`,
              };
            }, [e, t, a]);
            return n().createElement("div", { className: o()(Ra, _), style: u });
          },
          Pa = { from: { opacity: 0 }, to: { opacity: 1 }, delay: 100, config: { duration: 300 } };
        var Oa = a(4598),
          Ha = a(9174);
        function $a(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return za(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return za(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var _ = 0;
            return function () {
              return _ >= e.length ? { done: !0 } : { done: !1, value: e[_++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function za(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, _ = new Array(t); a < t; a++) _[a] = e[a];
          return _;
        }
        const Ga = (e) => (0 === e ? window : window.subViews.get(e));
        const Ua = ((e, t) => {
            const a = (0, r.createContext)({});
            return [
              function ({ mode: u = "real", options: i, children: o, mocks: s }) {
                const l = (0, r.useRef)([]),
                  c = (a, u, r) => {
                    var n;
                    const i = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: a = Ga,
                        context: u = "model",
                      } = {}) {
                        const r = new Map();
                        function n(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, a) => {
                            a.forEach((t) => {
                              const a = r.get(t);
                              void 0 !== a && a(e);
                            });
                          });
                        });
                        const i = (e) => {
                          const _ = a(t),
                            r = u.split(".").reduce((e, t) => e[t], _);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, t) => {
                                const a = e[t];
                                return "function" == typeof a ? a.bind(e) : a;
                              }, r);
                        };
                        return {
                          subscribe: (a, n) => {
                            const o = "string" == typeof n ? `${u}.${n}` : u,
                              s = _.O.view.addModelObserver(o, t, !0);
                            return (r.set(s, a), e && a(i(n)), s);
                          },
                          readByPath: i,
                          createCallback: (e, t) => {
                            const a = i(t);
                            return (...t) => {
                              a(e(...t));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const t = i(e);
                            return () => {
                              t();
                            };
                          },
                          dispose: function () {
                            for (var e, a = $a(r.keys()); !(e = a()).done;) n(e.value, t);
                          },
                          unsubscribe: n,
                        };
                      })(u),
                      o =
                        "real" === a
                          ? i
                          : Object.assign({}, i, {
                              readByPath:
                                null != (n = null == r ? void 0 : r.getter) ? n : () => {},
                            }),
                      s = (e) =>
                        "mocks" === a ? (null == r ? void 0 : r.getter(e)) : o.readByPath(e),
                      c = (e) => l.current.push(e),
                      m = e({
                        mode: a,
                        readByPath: s,
                        externalModel: o,
                        observableModel: {
                          array: (e, t) => {
                            const _ = null != t ? t : s(e),
                              u = Ha.LO.box(_, { equals: Oa.jv });
                            return (
                              "real" === a &&
                                o.subscribe(
                                  (0, Ha.aD)((e) => u.set(e)),
                                  e,
                                ),
                              u
                            );
                          },
                          object: (e, t) => {
                            const _ = null != t ? t : s(e),
                              u = Ha.LO.box(_, { equals: Oa.jv });
                            return (
                              "real" === a &&
                                o.subscribe(
                                  (0, Ha.aD)((e) => u.set(e)),
                                  e,
                                ),
                              u
                            );
                          },
                          primitives: (e, t) => {
                            const _ = s(t);
                            if (Array.isArray(e)) {
                              const u = e.reduce((e, t) => ((e[t] = Ha.LO.box(_[t], {})), e), {});
                              return (
                                "real" === a &&
                                  o.subscribe(
                                    (0, Ha.aD)((t) => {
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
                                n = r.reduce((e, [t, a]) => ((e[a] = Ha.LO.box(_[t], {})), e), {});
                              return (
                                "real" === a &&
                                  o.subscribe(
                                    (0, Ha.aD)((e) => {
                                      r.forEach(([t, a]) => {
                                        n[a].set(e[t]);
                                      });
                                    }),
                                    t,
                                  ),
                                n
                              );
                            }
                          },
                        },
                        cleanup: c,
                      }),
                      d = { mode: a, model: m, externalModel: o, cleanup: c };
                    return {
                      model: m,
                      controls: "mocks" === a && r ? r.controls(d) : t(d),
                      externalModel: o,
                      mode: a,
                    };
                  },
                  m = (0, r.useRef)(!1),
                  d = (0, r.useState)(u),
                  b = d[0],
                  g = d[1],
                  E = (0, r.useState)(() => c(u, i, s)),
                  p = E[0],
                  A = E[1];
                return (
                  (0, r.useEffect)(() => {
                    m.current ? A(c(b, i, s)) : (m.current = !0);
                  }, [s, b, i]),
                  (0, r.useEffect)(() => {
                    g(u);
                  }, [u]),
                  (0, r.useEffect)(
                    () => () => {
                      (p.externalModel.dispose(), l.current.forEach((e) => e()));
                    },
                    [p],
                  ),
                  n().createElement(a.Provider, { value: p }, o)
                );
              },
              () => (0, r.useContext)(a),
            ];
          })(
            ({ observableModel: e }) => ({
              root: e.object(),
              divisionInfo: e.object("divisionInfo"),
              qualification: e.primitives(
                ["isActive", "maxBattlesCount", "battlesCount", "isRatingCalculation"],
                "qualificationModel",
              ),
            }),
            ({ externalModel: e }) => ({ onOpenMeta: e.createCallbackNoArgs("onOpenMeta") }),
          ),
          ja = (Ua[0], Ua[1]),
          Va = "Progress_base_2e",
          qa = "Progress_progress_32",
          Za = "Progress_status_95",
          Ya = "Progress_statusPoints_73",
          Xa = "Progress_points_a7",
          Ka = "Progress_dash_32",
          Ja = "Progress_dash__right_fb",
          Qa = "Progress_score_c0",
          e_ = ({
            currentScore: e,
            prevScore: t,
            divisionInfo: a,
            isHonorPlace: _,
            className: u,
          }) =>
            _
              ? n().createElement(
                  "div",
                  { className: Xa },
                  n().createElement("div", { className: Ka }),
                  n().createElement("div", { className: Qa }, e),
                  n().createElement("div", { className: o()(Ka, Ja) }),
                )
              : n().createElement(
                  "div",
                  { className: o()(Va, u) },
                  n().createElement(
                    "div",
                    { className: qa },
                    n().createElement(Ue.ko, {
                      size: Ue.$u.Small,
                      value: e - a.from,
                      maxValue: a.to - a.from,
                      deltaFrom: t - a.from,
                    }),
                  ),
                  n().createElement(
                    "div",
                    { className: Za },
                    n().createElement(nt.ZP, {
                      text: R.strings.comp7.mainWidget.status(),
                      format: {
                        binding: {
                          score: n().createElement("span", { className: Ya }, e),
                          scoreToNextDivision: a.to,
                        },
                      },
                    }),
                  ),
                ),
          t_ = R.strings.comp7.qualification,
          a_ = { hasHtmlContent: !0 },
          __ = ({ maxBattlesCount: e, children: t }) =>
            n().createElement(
              L.i,
              {
                header: t_.conditionTooltip.header(),
                body: (0, M.uF)(t_.conditionTooltip.body(e), { maxBattlesCount: e }),
                args: a_,
              },
              n().createElement("div", null, t),
            ),
          u_ = "Qualification_base_46",
          r_ = "Qualification_qualificationEmblem_01",
          n_ = "Qualification_ratingCalculation_8f",
          i_ = "Qualification_timer_78",
          o_ = R.strings.comp7.mainWidget,
          s_ = (0, Ta.Pi)(({ classNames: e }) => {
            const t = ja(),
              a = t.model,
              _ = t.controls,
              u = a.root.get().isEnabled,
              r = a.qualification.battlesCount.get(),
              i = a.qualification.maxBattlesCount.get(),
              s = a.qualification.isRatingCalculation.get();
            return n().createElement(
              "div",
              { className: u_ },
              n().createElement(
                "div",
                { className: null == e ? void 0 : e.content },
                n().createElement(
                  Ae.u,
                  {
                    contentId: R.views.lobby.comp7.tooltips.MainWidgetTooltip("resId"),
                    isEnabled: u,
                  },
                  n().createElement(
                    "div",
                    {
                      className: null == e ? void 0 : e.emblemContainer,
                      onClick: u ? _.onOpenMeta : void 0,
                      onMouseDown: u ? D.playClick : void 0,
                      onMouseEnter: D.playHighlight,
                    },
                    n().createElement("div", { className: o()(null == e ? void 0 : e.emblem, r_) }),
                  ),
                ),
                n().createElement(
                  __,
                  { maxBattlesCount: i },
                  n().createElement(ka, { battlesCount: r, maxBattlesCount: i }),
                ),
              ),
              s &&
                n().createElement(
                  L.i,
                  { body: R.strings.comp7.qualification.ratingCalculationTooltip() },
                  n().createElement(
                    "div",
                    null,
                    n().createElement(de.z, {
                      text: o_.ratingCalculation(),
                      classMix: n_,
                      binding: { timer: n().createElement("div", { className: i_ }) },
                    }),
                  ),
                ),
            );
          }),
          l_ = "Warning_base_a5",
          c_ = "Warning_lighting_e0",
          m_ = "Warning_value_1e",
          d_ = "Warning_base__text_08",
          b_ = "Warning_timer_fe",
          g_ = ({ rankInactivityCount: e, warningText: t, className: a }) => {
            const _ = 0 === e;
            return n().createElement(
              "div",
              { className: o()(l_, _ && d_, a) },
              !_ && n().createElement("div", { className: c_ }),
              n().createElement("div", { className: m_ }, _ ? t : e),
              n().createElement(
                "div",
                { className: b_ },
                _ && n().createElement("div", { className: c_ }),
              ),
            );
          },
          E_ = "App_base_de",
          p_ = "App_content_da",
          A_ = "App_emblemContainer_dc",
          C_ = "App_base__unavailable_e1",
          F_ = "App_emblem_90",
          B_ = "App_progression_e6",
          h_ = "App_warning_f8",
          D_ = R.strings.comp7,
          f_ = R.views.lobby.comp7.tooltips,
          v_ = { content: p_, emblemContainer: A_, emblem: F_ },
          x_ =
            ((0, Ta.Pi)(() => {
              const e = ja(),
                t = e.model,
                a = e.controls,
                _ = t.root.get(),
                u = _.hasRankInactivityWarning,
                i = _.rankInactivityCount,
                s = _.isEnabled,
                l = _.rank,
                m = _.currentScore,
                d = _.prevScore,
                b = _.divisionInfo,
                g = t.qualification.isActive.get(),
                E = (0, r.useRef)(null),
                p = (0, c.GS)().mediaSize,
                A = (0, ya.useSpring)(Pa);
              (0, r.useEffect)(
                () =>
                  Na(() => {
                    if (null != E && E.current) {
                      const e = E.current.getBoundingClientRect();
                      viewEnv.setInputArea(
                        viewEnv.pxToRem(e.x),
                        viewEnv.pxToRem(e.y),
                        viewEnv.pxToRem(e.width),
                        viewEnv.pxToRem(e.height),
                      );
                    }
                  }),
                [p, u],
              );
              const C = l === ut.Sixth || (l === ut.Fifth && b.name === sa.A),
                F = o()(E_, !s && C_);
              return n().createElement(
                ya.animated.div,
                { className: F, ref: E, style: A },
                g
                  ? n().createElement(s_, { classNames: v_ })
                  : n().createElement(
                      n().Fragment,
                      null,
                      n().createElement(
                        "div",
                        { className: p_ },
                        n().createElement(
                          Ae.u,
                          { contentId: f_.MainWidgetTooltip("resId"), isEnabled: s },
                          n().createElement(
                            "div",
                            {
                              className: A_,
                              onClick: s ? a.onOpenMeta : void 0,
                              onMouseDown: s ? D.playClick : void 0,
                              onMouseEnter: D.playHighlight,
                            },
                            n().createElement(Ia, {
                              rank: l,
                              size: Wa.x150,
                              className: F_,
                              division: s ? b.name : void 0,
                            }),
                          ),
                        ),
                        s &&
                          n().createElement(
                            L.i,
                            { header: D_.scoreTooltip.header(), body: D_.scoreTooltip.body() },
                            n().createElement(
                              "div",
                              null,
                              n().createElement(e_, {
                                currentScore: m,
                                prevScore: d,
                                divisionInfo: b,
                                className: B_,
                                isHonorPlace: C,
                              }),
                            ),
                          ),
                      ),
                      s &&
                        u &&
                        n().createElement(
                          Ae.u,
                          { contentId: f_.RankInactivityTooltip("resId"), ignoreShowDelay: !0 },
                          n().createElement(
                            "div",
                            null,
                            n().createElement(g_, {
                              rankInactivityCount: i,
                              warningText: D_.mainWidget.warning(),
                              className: h_,
                            }),
                          ),
                        ),
                    ),
              );
            }),
            {
              base: "Progression_base_bb",
              progress: "Progression_progress_2a",
              warning: "Progression_warning_1f",
              battlesCounter__b0: "Progression_battlesCounter__b0_31",
              battlesCounter__b1: "Progression_battlesCounter__b1_92",
              battlesCounter__b2: "Progression_battlesCounter__b2_0c",
              battlesCounter: "Progression_battlesCounter_df",
            }),
          S_ = R.strings.comp7.scoreTooltip,
          w_ = ({
            rankInactivityCount: e,
            hasRankInactivityWarning: t,
            rank: a,
            currentScore: _,
            prevScore: u,
            divisionInfo: r,
            size: i,
            qualificationModel: s,
          }) => {
            const l = a === ut.Sixth || (a === ut.Fifth && r.name === sa.A);
            return n().createElement(
              n().Fragment,
              null,
              n().createElement(
                "div",
                { className: x_.base },
                s.isActive
                  ? n().createElement(
                      "div",
                      { className: o()(x_.battlesCounter, x_[`battlesCounter__${i}`]) },
                      n().createElement(ka, {
                        battlesCount: s.battlesCount,
                        maxBattlesCount: s.maxBattlesCount,
                      }),
                    )
                  : n().createElement(
                      L.i,
                      { header: S_.header(), body: S_.body() },
                      n().createElement(e_, {
                        currentScore: _,
                        prevScore: u,
                        divisionInfo: r,
                        isHonorPlace: l,
                        className: x_.progress,
                      }),
                    ),
              ),
              t &&
                n().createElement(
                  Ae.u,
                  {
                    contentId: R.views.lobby.comp7.tooltips.RankInactivityTooltip("resId"),
                    ignoreShowDelay: !0,
                  },
                  n().createElement(
                    "div",
                    null,
                    n().createElement(g_, {
                      rankInactivityCount: e,
                      warningText: R.strings.mode_selector.mode.comp7.warning(),
                      className: x_.warning,
                    }),
                  ),
                ),
            );
          },
          k_ = {
            qualificationEmblem: "Widget_qualificationEmblem_d8",
            qualificationEmblem__x64: "Widget_qualificationEmblem__x64_5d",
            qualificationEmblem__x84: "Widget_qualificationEmblem__x84_7e",
            qualificationEmblem__x110: "Widget_qualificationEmblem__x110_54",
            qualificationEmblem__x150: "Widget_qualificationEmblem__x150_f1",
          },
          N_ = ({ widget: e, size: t, className: a }) => {
            const _ = (0, c.GS)().mediaSize,
              u = _ < c.cJ.Medium || (_ >= c.cJ.Medium && t === re.Id.B3),
              i = e.qualificationModel.isActive,
              s = (0, r.useMemo)(
                () =>
                  _ === c.cJ.Medium
                    ? t === re.Id.B3
                      ? Wa.x84
                      : Wa.x150
                    : _ > c.cJ.Medium
                      ? t === re.Id.B3
                        ? Wa.x110
                        : Wa.x150
                      : Wa.x64,
                [t, _],
              );
            return n().createElement(
              Ae.u,
              { contentId: R.views.lobby.comp7.tooltips.MainWidgetTooltip("resId") },
              n().createElement(
                "div",
                { onMouseEnter: D.playHighlight },
                i
                  ? n().createElement("div", {
                      className: o()(k_.qualificationEmblem, k_[`qualificationEmblem__x${s}`], a),
                    })
                  : n().createElement(Ia, {
                      rank: e.rank,
                      division: u ? void 0 : e.divisionInfo.name,
                      size: s,
                      className: a,
                    }),
              ),
            );
          },
          T_ = ["size", "description", "showWidget", "widget", "isLocked"];
        function y_() {
          return (
            (y_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            y_.apply(this, arguments)
          );
        }
        const L_ = R.strings.mode_selector.mode.comp7.widgetDescription,
          M_ = [re.Id.B0, re.Id.B1],
          R_ = [re.Id.B4, re.Id.B5, re.Id.B6],
          W_ = (e) => {
            if (e.qualificationModel.isActive) {
              const t = e.qualificationModel.maxBattlesCount;
              return (0, M.uF)(L_.qualification(t), { maxBattlesCount: t });
            }
            const t = Ea(e.rank);
            return Aa(e.rank)
              ? (0, M.uF)(L_.status(), {
                  rank: t,
                  division: ((a = e.divisionInfo.name), (0, M.uF)(ca.text(), { division: da(a) })),
                })
              : t;
            var a;
          },
          I_ = (e) => {
            let t = e.size,
              a = e.description,
              _ = e.showWidget,
              u = e.widget,
              r = e.isLocked,
              i = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, T_);
            const o = u && u.isEnabled && !r,
              s = _ && o && M_.includes(t),
              l = {
                root: { get: () => ({ myPosition: u.myPosition, currentScore: u.currentScore }) },
              },
              c =
                u.rank === ut.Sixth || (u.rank === ut.Fifth && u.divisionInfo.type === Ba.TRANSFER);
            return n().createElement(
              "div",
              { className: ha[`base__${t}`] },
              n().createElement(
                ze,
                y_(
                  {
                    widgetComponent:
                      o && n().createElement(N_, { widget: u, size: t, className: ha.widget }),
                    showWidget: _,
                    size: t,
                    belowStatusComponent:
                      s && c
                        ? n().createElement(oa, { mode: ia.MODE_SELECTOR, model: l })
                        : s
                          ? n().createElement(w_, y_({}, u, { size: t }))
                          : void 0,
                    description: _ && o ? W_(u) : a,
                    classNames: { belowStatus: ha.belowStatus },
                    noWidgetSizes: R_,
                    isLocked: r,
                  },
                  i,
                ),
              ),
            );
          };
        var P_ = a(156);
        const O_ = {
            base: "Progression_base_5f",
            base__extraSmall: "Progression_base__extraSmall_77",
            base__small: "Progression_base__small_a4",
            base__medium: "Progression_base__medium_8d",
            base__extraLarge: "Progression_base__extraLarge_28",
            base__large: "Progression_base__large_09",
            contentWrapper: "Progression_contentWrapper_ed",
            progress: "Progression_progress_85",
            progressValue: "Progression_progressValue_c5",
            currentAmount: "Progression_currentAmount_e9",
            textCollection: "Progression_textCollection_7c",
            textCollection__extraSmall: "Progression_textCollection__extraSmall_2e",
            textCollection__small: "Progression_textCollection__small_e4",
            textCollection__medium: "Progression_textCollection__medium_b8",
            textCollection__extraLarge: "Progression_textCollection__extraLarge_74",
            textCollection__large: "Progression_textCollection__large_00",
          },
          H_ = ({ totalCount: e, currentProgress: t, size: a }) => {
            const _ = a === re.Id.B1,
              u = (0, ue.Z)(["base", "textCollection", "progress"], O_),
              i = t && e ? (100 * t) / e : 0,
              o = (0, r.useMemo)(
                () => ({
                  current: n().createElement("span", { className: O_.currentAmount }, t),
                  total: e,
                }),
                [t, e],
              );
            return n().createElement(
              "div",
              { className: u.base },
              n().createElement(
                "div",
                { className: O_.contentWrapper },
                _ &&
                  n().createElement(
                    "div",
                    { className: u.progress },
                    n().createElement(
                      "div",
                      { className: O_.progressValue },
                      n().createElement(de.z, {
                        classMix: u.textCollection,
                        text: R.strings.mode_selector.mode.cosmic_event.progression(),
                        binding: o,
                      }),
                    ),
                    n().createElement(Ue.ko, { size: Ue.$u.Small, value: i, theme: P_.Gh }),
                  ),
              ),
            );
          },
          $_ = {
            base: "Suspended_base_26",
            base__b1: "Suspended_base__b1_f0",
            base__b1__extraSmall: "Suspended_base__b1__extraSmall_74",
            base__b1__small: "Suspended_base__b1__small_fe",
            base__b1__medium: "Suspended_base__b1__medium_ed",
            base__b1__extraLarge: "Suspended_base__b1__extraLarge_2f",
            base__b1__large: "Suspended_base__b1__large_73",
            base__b2: "Suspended_base__b2_40",
            base__b2__medium: "Suspended_base__b2__medium_18",
            base__b2__extraLarge: "Suspended_base__b2__extraLarge_d5",
            base__b2__large: "Suspended_base__b2__large_6f",
            base__b3: "Suspended_base__b3_a7",
            base__b3__medium: "Suspended_base__b3__medium_5a",
            base__b3__extraLarge: "Suspended_base__b3__extraLarge_ea",
            base__b3__large: "Suspended_base__b3__large_22",
            textContainer: "Suspended_textContainer_99",
            textContainer__extraSmall: "Suspended_textContainer__extraSmall_15",
            textContainer__small: "Suspended_textContainer__small_00",
            textContainer__medium: "Suspended_textContainer__medium_62",
            textContainer__extraLarge: "Suspended_textContainer__extraLarge_40",
            textContainer__large: "Suspended_textContainer__large_42",
            textContainer__b2: "Suspended_textContainer__b2_00",
            textContainer__b2__extraSmall: "Suspended_textContainer__b2__extraSmall_d6",
            textContainer__b2__small: "Suspended_textContainer__b2__small_d1",
            textContainer__b2__medium: "Suspended_textContainer__b2__medium_11",
            textContainer__b2__extraLarge: "Suspended_textContainer__b2__extraLarge_64",
            textContainer__b2__large: "Suspended_textContainer__b2__large_8f",
            locked: "Suspended_locked_de",
            locked__extraSmall: "Suspended_locked__extraSmall_8d",
            locked__small: "Suspended_locked__small_ad",
            locked__medium: "Suspended_locked__medium_0b",
            locked__extraLarge: "Suspended_locked__extraLarge_be",
            locked__large: "Suspended_locked__large_19",
            lockBase: "Suspended_lockBase_38",
            lockBase__b1__extraSmall: "Suspended_lockBase__b1__extraSmall_17",
            lockBase__b1__small: "Suspended_lockBase__b1__small_88",
            lockBase__b1__medium: "Suspended_lockBase__b1__medium_9c",
            lockBase__b1__extraLarge: "Suspended_lockBase__b1__extraLarge_39",
            lockBase__b1__large: "Suspended_lockBase__b1__large_34",
            lockBase__b2: "Suspended_lockBase__b2_78",
            lockBase__b2__extraSmall: "Suspended_lockBase__b2__extraSmall_fd",
            lockBase__b2__small: "Suspended_lockBase__b2__small_7a",
            lockBase__b2__medium: "Suspended_lockBase__b2__medium_04",
            lockBase__b2__extraLarge: "Suspended_lockBase__b2__extraLarge_32",
            lockBase__b2__large: "Suspended_lockBase__b2__large_2a",
            textContent: "Suspended_textContent_93",
            textContent__extraSmall: "Suspended_textContent__extraSmall_77",
            textContent__small: "Suspended_textContent__small_49",
            textContent__medium: "Suspended_textContent__medium_18",
            textContent__extraLarge: "Suspended_textContent__extraLarge_c2",
            textContent__large: "Suspended_textContent__large_0e",
            primeTimeValue: "Suspended_primeTimeValue_79",
            primeTimeValue__extraSmall: "Suspended_primeTimeValue__extraSmall_d5",
            primeTimeValue__small: "Suspended_primeTimeValue__small_93",
            primeTimeValue__medium: "Suspended_primeTimeValue__medium_a8",
            primeTimeValue__extraLarge: "Suspended_primeTimeValue__extraLarge_0f",
            primeTimeValue__large: "Suspended_primeTimeValue__large_81",
          },
          z_ = ({ size: e }) => {
            const t = (0, ue.Z)(
                [
                  ...(0, re.Hp)("base", "textContainer", "lockBase"),
                  "textContent",
                  "primeTimeValue",
                  "locked",
                ],
                $_,
              ),
              a = o()(t.base, t[`base__${e}`]),
              _ = o()(t.textContainer, t[`textContainer__${e}`]),
              u = o()(t.lockBase, t[`lockBase__${e}`]);
            return n().createElement(
              "div",
              { className: a },
              n().createElement(
                "div",
                { className: _ },
                n().createElement(
                  "div",
                  { className: t.textContent },
                  R.strings.mode_selector.mode.cosmic_event.notStarted(),
                ),
              ),
              n().createElement(
                "div",
                { className: u },
                n().createElement("div", { className: t.locked }),
                n().createElement(de.z, {
                  classMix: t.primeTimeValue,
                  text: R.strings.mode_selector.mode.cosmic_event.primeTime(),
                }),
              ),
            );
          },
          G_ = "CosmicCard_subTitle_51",
          U_ = "CosmicCard_name_ed",
          j_ = ["showWidget", "size", "widget", "isSuspended"];
        function V_() {
          return (
            (V_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            V_.apply(this, arguments)
          );
        }
        const q_ = R.strings.mode_selector.mode.cosmic_event.description(),
          Z_ = (0, r.memo)((e) => {
            let t = e.showWidget,
              a = e.size,
              _ = e.widget,
              u = e.isSuspended,
              r = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, j_);
            const i = a === re.Id.B1 && t,
              o = !!u || t,
              s = u ? "" : q_,
              l = { subtitle: G_, name: U_ };
            return n().createElement(
              ze,
              V_(
                {
                  showWidget: o,
                  size: a,
                  isNotStarted: u,
                  belowStatusComponent:
                    (!u && i && n().createElement(H_, V_({}, _, { size: a }))) ||
                    (u && n().createElement(z_, { size: a })),
                },
                r,
                { statusActive: s, classNames: l },
              ),
            );
          });
        var Y_ = a(9459);
        let X_, K_;
        (!(function (e) {
          ((e.Timer = "timer"),
            (e.Countdown = "countdown"),
            (e.Cooldown = "cooldown"),
            (e.None = "none"));
        })(X_ || (X_ = {})),
          (function (e) {
            ((e.Description = "description"),
              (e.Short = "short"),
              (e.Long = "long"),
              (e.Extended = "extended"));
          })(K_ || (K_ = {})));
        const J_ = "Countdown_base_fe",
          Q_ = "Countdown_icon_8b",
          eu = "Countdown_description_8d",
          tu = (e) => e.toString().padStart(2, "0"),
          au = (e, t) => {
            switch (t) {
              case K_.Description:
                return ((e, t = !0) =>
                  e.days > 7 && t
                    ? (0, M.WU)(R.strings.common.duration.days(), { days: e.days })
                    : e.days >= 1
                      ? 0 === e.hours
                        ? (0, M.WU)(R.strings.common.duration.days(), { days: e.days })
                        : `${(0, M.WU)(R.strings.common.duration.days(), { days: e.days })} ${(0, M.WU)(R.strings.common.duration.hours(), { hours: e.hours })}`
                      : e.hours >= 1
                        ? 0 === e.minutes
                          ? (0, M.WU)(R.strings.common.duration.hours(), { hours: e.hours })
                          : `${(0, M.WU)(R.strings.common.duration.hours(), { hours: e.hours })} ${(0, M.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes })}`
                        : (0, M.WU)(R.strings.common.duration.minutes(), {
                            minutes: e.minutes || 1,
                          }))(e);
              case K_.Short:
                return `${tu(e.minutes)}:${tu(e.seconds)}`;
              case K_.Long:
                return `${tu(e.hours)}:${tu(e.minutes)}:${tu(e.seconds)}`;
              case K_.Extended:
                return `${(0, M.WU)(R.strings.common.duration.days(), { days: e.days })} | ${tu(e.hours)}:${tu(e.minutes)}:${tu(e.seconds)}`;
            }
          },
          _u = R.images.gui.maps.icons.components.countdown,
          uu = (e, t) => {
            const a = 2 === t ? _u.big : _u;
            switch (e) {
              case X_.Timer:
                return a.clock();
              case X_.Countdown:
                return a.hourglass();
              case X_.Cooldown:
                return a.lock();
            }
          },
          ru = (0, r.memo)(
            ({
              duration: e,
              icon: t = X_.Timer,
              style: a = K_.Description,
              onTimeReached: u,
              className: i = "",
              classNames: s = {},
              labelFormat: l = "",
            }) => {
              const c = a !== K_.Description ? 1 : void 0,
                m = Q(e, c),
                d = (() => {
                  const e = (0, r.useState)(_.O.view.getScale()),
                    t = e[0],
                    a = e[1];
                  return (
                    (0, r.useEffect)(() => {
                      const e = () => {
                        a(_.O.view.getScale());
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
                })();
              u && u[m] && u[m]();
              const b = au(
                (function (e = 0) {
                  let t = e;
                  const a = Math.trunc(t / H);
                  t -= a * H;
                  const _ = Math.trunc(t / O);
                  t -= _ * O;
                  const u = Math.trunc(t / P);
                  return ((t -= u * P), { days: a, hours: _, minutes: u, seconds: t });
                })(m),
                a,
              );
              return n().createElement(
                "div",
                { className: o()(J_, i) },
                t !== X_.None &&
                  n().createElement("div", {
                    className: o()(Q_, s.icon),
                    style: { backgroundImage: `url('${uu(t, d)}')` },
                  }),
                l
                  ? n().createElement(
                      "div",
                      { className: o()(eu, s.text) },
                      n().createElement(de.z, { text: l, binding: { timerText: b } }),
                    )
                  : n().createElement("div", { className: o()(eu, s.text) }, b),
              );
            },
          );
        let nu;
        !(function (e) {
          ((e.DISABLED = "disabled"), (e.ACTIVE = "active"), (e.RESETTABLE = "resettable"));
        })(nu || (nu = {}));
        const iu = {
          base: "Progression_base_4f",
          title: "Progression_title_d7",
          base__resettable: "Progression_base__resettable_e1",
          base__disabled: "Progression_base__disabled_bf",
          contentWrapper: "Progression_contentWrapper_24",
          progress: "Progression_progress_4f",
          progressValue: "Progression_progressValue_1a",
          countdown: "Progression_countdown_5b",
        };
        var ou = a(9762),
          su = a(6457);
        let lu, cu;
        (!(function (e) {
          ((e.Init = "init"),
            (e.Active = "active"),
            (e.NonActive = "nonActive"),
            (e.UpdateState = "updateState"));
        })(lu || (lu = {})),
          (function (e) {
            ((e.CheckDataUpdate = "checkDataUpdate"),
              (e.UpdateStageData = "updateStageData"),
              (e.SwitchState = "switchState"));
          })(cu || (cu = {})));
        const mu = (e) => e === nu.ACTIVE,
          du = (e) => mu(e.status),
          bu = (e) => !mu(e.status),
          gu = (e, t) => e.status !== t.status && Eu(e, t),
          Eu = (e, t) =>
            t.stage === e.stage &&
            t.currentPoints === e.currentPoints &&
            t.maximumPoints === e.maximumPoints &&
            0 === e.earnedPoints,
          pu = (e, t) =>
            mu(t.status) &&
            ((1 === t.stage && 0 === t.currentPoints) ||
              (t.stage === e.stage && e.maximumPoints !== t.maximumPoints)),
          Au = (e, t) =>
            t.stage === e.stage &&
            t.currentPoints === e.currentPoints &&
            t.maximumPoints === e.maximumPoints &&
            0 !== e.earnedPoints,
          Cu = (e, t) =>
            t.stage === e.stage &&
            t.currentPoints !== e.currentPoints &&
            t.maximumPoints === e.maximumPoints,
          Fu = (e, t) => t.stage > e.stage && e.currentPoints < e.maximumPoints,
          Bu = (e, t) => t.stage > e.stage && e.currentPoints === e.maximumPoints,
          hu = (e, t) => t.stage < e.stage && e.currentPoints > 0,
          Du = (e, t) => t.stage < e.stage && 0 === e.currentPoints,
          fu = (e, t) => e.status !== t.status && mu(t.status),
          vu = (e) => {
            e.isSoundEnabled && 0 !== e.earnedPoints && h("ev_fep_progress_bar");
          },
          xu = R.strings.fun_random.modes,
          Su = R.strings.fun_random.modeSelector.progression,
          wu = {
            freezed: !1,
            withStack: !1,
            type: je.r.Growing,
            delta: { duration: 2e3, delay: 100 },
            line: { duration: 2e3, delay: 100 },
          },
          ku = ({
            status: e,
            currentStage: t,
            resetTimer: a,
            stageCurrentPoints: _,
            stageMaximumPoints: u,
            conditionText: i,
            isContentVisible: s,
            assetsPointer: l,
          }) => {
            const c = n().useMemo(() => {
                return (
                  (a = "fun-card-fsm"),
                  (r = {
                    status: e,
                    stage: t,
                    currentPoints: _,
                    maximumPoints: u,
                    earnedPoints: 0,
                    isSoundEnabled: s,
                  }),
                  (n = 300),
                  (0, ou.C)(
                    {
                      preserveActionOrder: !0,
                      id: a,
                      initial: lu.Init,
                      context: r,
                      states: {
                        [lu.Init]: { always: { target: lu.UpdateState } },
                        [lu.UpdateState]: {
                          always: [
                            { target: lu.Active, cond: du },
                            { target: lu.NonActive, cond: bu },
                          ],
                        },
                        [lu.Active]: {
                          on: {
                            [cu.CheckDataUpdate]: [
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e, t) => ({
                                    type: cu.SwitchState,
                                    status: t.status,
                                  })),
                                ],
                                cond: gu,
                              },
                              { target: lu.Active, cond: Eu },
                              {
                                target: lu.UpdateState,
                                actions: [
                                  (0, su.f0)({
                                    status: (e, t) => t.status,
                                    stage: (e, t) => t.stage,
                                    currentPoints: (e, t) => t.currentPoints,
                                    maximumPoints: (e, t) => t.maximumPoints,
                                    earnedPoints: 0,
                                  }),
                                ],
                                cond: pu,
                              },
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e) => ({
                                    type: cu.UpdateStageData,
                                    stage: e.stage,
                                    currentPoints: e.maximumPoints,
                                    maximumPoints: e.maximumPoints,
                                    earnedPoints: e.maximumPoints - e.currentPoints,
                                  })),
                                ],
                                cond: Fu,
                              },
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e, t) => ({
                                    type: cu.UpdateStageData,
                                    stage: t.stage,
                                    currentPoints: 0,
                                    maximumPoints: t.maximumPoints,
                                    earnedPoints: 0,
                                  })),
                                  (0, su.lW)(
                                    (e, t) => ({
                                      type: cu.UpdateStageData,
                                      stage: t.stage,
                                      currentPoints: t.currentPoints,
                                      maximumPoints: t.maximumPoints,
                                      earnedPoints: t.currentPoints,
                                    }),
                                    { delay: n },
                                  ),
                                ],
                                cond: Bu,
                              },
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e, t) => ({
                                    type: cu.UpdateStageData,
                                    stage: e.stage,
                                    currentPoints: t.currentPoints,
                                    maximumPoints: e.maximumPoints,
                                    earnedPoints: t.currentPoints - e.currentPoints,
                                  })),
                                ],
                                cond: Cu,
                              },
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e) => ({
                                    type: cu.UpdateStageData,
                                    stage: e.stage,
                                    currentPoints: e.currentPoints,
                                    maximumPoints: e.maximumPoints,
                                    earnedPoints: 0,
                                  })),
                                  (0, su.lW)((e, t) => ({
                                    type: cu.SwitchState,
                                    status: t.status,
                                  })),
                                ],
                                cond: Au,
                              },
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e) => ({
                                    type: cu.UpdateStageData,
                                    stage: e.stage,
                                    currentPoints: 0,
                                    maximumPoints: e.maximumPoints,
                                    earnedPoints: -e.currentPoints,
                                  })),
                                ],
                                cond: hu,
                              },
                              {
                                target: lu.Active,
                                actions: [
                                  (0, su.lW)((e, t) => ({
                                    type: cu.UpdateStageData,
                                    stage: t.stage,
                                    currentPoints: t.currentPoints,
                                    maximumPoints: t.maximumPoints,
                                    earnedPoints: t.currentPoints - t.maximumPoints,
                                  })),
                                ],
                                cond: Du,
                              },
                            ],
                            [cu.UpdateStageData]: {
                              target: lu.Active,
                              actions: [
                                (0, su.f0)({
                                  stage: (e, t) => t.stage,
                                  currentPoints: (e, t) => t.currentPoints,
                                  maximumPoints: (e, t) => t.maximumPoints,
                                  earnedPoints: (e, t) => t.earnedPoints,
                                }),
                                vu,
                              ],
                            },
                            [cu.SwitchState]: {
                              target: lu.UpdateState,
                              actions: (0, su.f0)({ status: (e, t) => t.status }),
                            },
                          },
                        },
                        [lu.NonActive]: {
                          on: {
                            [cu.CheckDataUpdate]: {
                              target: lu.UpdateState,
                              actions: [
                                (0, su.f0)({
                                  status: (e, t) => t.status,
                                  stage: (e, t) => t.stage,
                                  currentPoints: (e, t) => t.currentPoints,
                                  maximumPoints: (e, t) => t.maximumPoints,
                                  earnedPoints: 0,
                                }),
                              ],
                              cond: fu,
                            },
                            [cu.SwitchState]: {
                              target: lu.UpdateState,
                              actions: (0, su.f0)({ status: (e, t) => t.status }),
                            },
                          },
                        },
                      },
                    },
                    {
                      guards: {
                        hasActiveStatus: du,
                        hasNonActiveStatus: bu,
                        isStatusUpdate: gu,
                        isNoUpdate: Eu,
                        isTaskSwitchingUpdate: pu,
                        isUpdateCurrentStageWithZeroEarnPoints: Au,
                        isUpdateCurrentStageWithCurrentPoints: Cu,
                        isUpdateToNextStageWithoutFillMax: Bu,
                        isUpdateToNextStageWithFillMax: Fu,
                        isUpdateToPrevStageWithReset: hu,
                        isUpdateToPrevStageWithoutReset: Du,
                        isUpdateWithActiveSwitch: fu,
                      },
                    },
                  )
                );
                var a, r, n;
              }, []),
              m = (0, Y_.eO)(c),
              d = m[0],
              b = m[1],
              g = (0, r.useMemo)(() => {
                var e;
                return (null != (e = xu.$dyn(l)) ? e : xu.undefined).mode_selector.progression;
              }, [l]),
              E = d.context.status === nu.ACTIVE,
              p = d.context.status === nu.RESETTABLE,
              A = Su.$dyn(d.context.currentPoints > 0 ? "steps" : "stepsNoProgress"),
              C = g.resettable(),
              F = p ? C : i;
            (0, r.useEffect)(() => {
              b({
                type: cu.CheckDataUpdate,
                status: e,
                stage: t,
                currentPoints: _,
                maximumPoints: u,
              });
            }, [e, _, u, t, b]);
            const B = (0, r.useCallback)(() => {
              b({
                type: cu.CheckDataUpdate,
                status: e,
                stage: t,
                currentPoints: _,
                maximumPoints: u,
              });
            }, [_, u, t, e, b]);
            return n().createElement(
              Ae.u,
              {
                contentId:
                  R.views.fun_random.lobby.tooltips.FunRandomProgressionTooltipView("resId"),
                isEnabled: E,
              },
              n().createElement(
                "div",
                { className: o()(iu.base, iu[`base__${d.context.status}`]) },
                n().createElement("div", { className: iu.title }, F),
                n().createElement(
                  "div",
                  { className: iu.contentWrapper },
                  n().createElement(
                    "div",
                    { className: iu.progress },
                    n().createElement(
                      "div",
                      { className: iu.progressValue },
                      n().createElement(Xe, {
                        text: A,
                        binding: { done: d.context.currentPoints, total: d.context.maximumPoints },
                      }),
                    ),
                    n().createElement(Ue.ko, {
                      size: Ue.$u.Small,
                      value: d.context.currentPoints,
                      maxValue: d.context.maximumPoints,
                      animationSettings: wu,
                      deltaFrom: d.context.currentPoints - d.context.earnedPoints,
                      onEndAnimation: B,
                    }),
                  ),
                  n().createElement(
                    "div",
                    { className: iu.countdown },
                    n().createElement(ru, { duration: a, style: K_.Description }),
                  ),
                ),
              ),
            );
          },
          Nu = {
            widgetOverlay: "FunRandomCard_widgetOverlay_f2",
            subtitle: "FunRandomCard_subtitle_d0",
            belowStatus: "FunRandomCard_belowStatus_03",
          },
          Tu = ["size", "showWidget", "widget", "isContentVisible", "resourcesFolderName"];
        function yu() {
          return (
            (yu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            yu.apply(this, arguments)
          );
        }
        const Lu = R.images.fun_random.gui.maps.icons.feature.asset_packs.modes,
          Mu = (e) => {
            let t = e.size,
              a = e.showWidget,
              _ = e.widget,
              u = e.isContentVisible,
              r = e.resourcesFolderName,
              i = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Tu);
            const o = t === re.Id.B1 && a;
            return n().createElement(
              "div",
              { className: Nu[`base__${t}`] },
              n().createElement(
                ze,
                yu(
                  {
                    showWidget: a,
                    size: t,
                    belowStatusComponent:
                      o &&
                      n().createElement(ku, yu({}, _, { isContentVisible: u, assetsPointer: r })),
                    classNames: { belowStatus: Nu.belowStatus, subtitle: Nu.subtitle },
                    resourcesFolderName: r,
                  },
                  i,
                  {
                    resourceFolderGetter: (e) => {
                      var t;
                      return (null != (t = Lu.$dyn(e)) ? t : Lu.undefined.mode_selector)
                        .mode_selector;
                    },
                  },
                ),
              ),
            );
          },
          Ru = "display",
          Wu = (e) => {
            (0, r.useEffect)(e, []);
          },
          Iu = {
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
        var Pu;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(Pu || (Pu = {}));
        const Ou = ["__left", "__right", "__top", "__bottom"],
          Hu =
            ((0, r.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: t, onOutsideClick: a, customStyles: u = {} },
                i,
              ) => {
                const s = (0, r.useRef)(null),
                  l = (0, r.useRef)(null),
                  c = (0, r.useRef)(null),
                  m = (0, r.useState)(window.decorator && window.decorator.directionType),
                  d = m[0],
                  b = m[1],
                  g = (0, r.useCallback)(() => {
                    (D.playClick(), _.O.view.sendEvent.close());
                  }, []),
                  E = (0, r.useCallback)(() => {
                    D.playHighlight();
                  }, []),
                  p = o()(Iu.arrow, Iu[`arrow${Ou[d]}`]);
                Wu(
                  () => (
                    _.O.client.events.mouse.enableOutside(),
                    _.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (a ? a() : _.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const A = (0, r.useCallback)(
                    (e) => {
                      let t = e.target;
                      do {
                        if (t === s.current || t === c.current) return;
                        t = t.parentNode;
                      } while (t);
                      const u = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = _.O.client.getMouseGlobalPosition(),
                          t = ![u.boundX, u.boundY, u.boundWidth, u.boundHeight].includes(void 0),
                          a =
                            e.x < u.boundX ||
                            e.x > u.boundX + u.boundWidth ||
                            e.y > u.boundY + u.boundHeight ||
                            e.y < u.boundY;
                        if (t && !a) return;
                      }
                      a ? a() : _.O.view.sendEvent.close("popover");
                    },
                    [s, c, a],
                  ),
                  C = (0, r.useCallback)(
                    () => (
                      _.O.view.freezeTextureBeforeResize(),
                      Na(() => {
                        if (l.current) {
                          const e = l.current.scrollWidth,
                            t = l.current.scrollHeight;
                          (_.O.view.resize(e, t), b(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, r.useImperativeHandle)(i, () => ({ updateSize: C })),
                  Wu(() => {
                    _.O.view.setInputPaddingsRem(58);
                  }),
                  (0, r.useEffect)(() => {
                    document.addEventListener("mousedown", A, { capture: !0 });
                    const e = ((e) => {
                      let t = !1;
                      return {
                        promise: new Promise((a, _) => {
                          e.then((e) => !t && a(e)).catch((e) => !t && _(e));
                        }),
                        cancel() {
                          t = !0;
                        },
                      };
                    })((0, I.Eu)());
                    return (
                      !t && e.promise.then(() => C()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", A));
                      }
                    );
                  }, [C, A, t]),
                  n().createElement(
                    "div",
                    { className: Iu.base, ref: l },
                    n().createElement(
                      "div",
                      { className: Iu.decorator },
                      n().createElement(
                        "div",
                        { className: Iu.content, ref: s },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          n().createElement(
                            L.i,
                            { body: R.strings.dialogs.common.error.cancel() },
                            n().createElement("div", {
                              className: Iu.closeBtn,
                              onClick: g,
                              onMouseEnter: E,
                              ref: c,
                            }),
                          ),
                      ),
                      n().createElement("div", { className: p, style: u.arrow }),
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
        function $u() {
          return (
            ($u =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            $u.apply(this, arguments)
          );
        }
        const zu = (e) => {
            let t = e.contentId,
              a = e.decoratorId,
              _ = e.direction,
              u = void 0 === _ ? Pu.Top : _,
              i = e.targetId,
              o = e.args,
              s = e.onClick,
              l = e.children,
              c = e.isEnabled,
              m = void 0 === c || c,
              d = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Hu);
            const b = (0, r.useRef)(null),
              g = (0, r.useCallback)(() => {
                if ((0, I.wU)()) return (0, I.SW)();
                b.current && (0, I.P3)(t, u, b.current, a, i, o);
              }, [t, u, o, a, i]);
            return n().createElement(
              "div",
              $u(
                {
                  ref: b,
                  onClick:
                    ((E = l.props.onClick),
                    (e) => {
                      m && (g(), s && s(e), E && E(e));
                    }),
                },
                d,
              ),
              l,
            );
            var E;
          },
          Gu = "ToggleButton_base_d9",
          Uu = "ToggleButton_content_ee",
          ju = "ToggleButton_overlay_d9",
          Vu = "ToggleButton_base__active_6e",
          qu = "ToggleButton_indicator_c5",
          Zu = ["active", "className", "children", "size", "showIndicator"];
        function Yu() {
          return (
            (Yu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            Yu.apply(this, arguments)
          );
        }
        const Xu = (e) => {
            let t = e.active,
              a = e.className,
              _ = e.children,
              u = e.size,
              r = void 0 === u ? x.small : u,
              i = e.showIndicator,
              s = void 0 === i || i,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Zu);
            return n().createElement(
              "div",
              { className: o()(Gu, a, t && Vu) },
              n().createElement(
                w,
                Yu({ type: "secondary", size: r }, l),
                n().createElement("div", { className: Uu }, _),
              ),
              s && n().createElement("div", { className: qu }),
              n().createElement("div", { className: ju }),
            );
          },
          Ku =
            ((0, r.memo)(Xu),
            {
              base: "Settings_base_fe",
              base__extraSmall: "Settings_base__extraSmall_6e",
              base__small: "Settings_base__small_5a",
              base__medium: "Settings_base__medium_a8",
              base__bigButton: "Settings_base__bigButton_d2",
              base__bigButton__medium: "Settings_base__bigButton__medium_7f",
              base__bigButton__extraSmall: "Settings_base__bigButton__extraSmall_8f",
              base__bigButton__small: "Settings_base__bigButton__small_76",
              base__anim: "Settings_base__anim_b2",
              settingsLabel: "Settings_settingsLabel_0e",
              toggle: "Settings_toggle_92",
              toggle__extraSmall: "Settings_toggle__extraSmall_ff",
              toggle__small: "Settings_toggle__small_df",
              toggle__medium: "Settings_toggle__medium_a6",
              toggle__shortBtn: "Settings_toggle__shortBtn_b5",
              icon: "Settings_icon_90",
              icon__shortBtn: "Settings_icon__shortBtn_34",
              bubble: "Settings_bubble_6e",
            }),
          Ju = R.strings.mode_selector.mode.random,
          Qu = (0, r.memo)(
            ({
              contentId: e,
              handleSettingsClick: t,
              body: a,
              showBigSettingsButton: _,
              isShowButton: u,
              isSettingsActive: r,
              withBubble: i,
            }) => {
              const s = (0, ue.Z)(["base", "toggle", "base__bigButton"], Ku);
              return n().createElement(
                "div",
                { className: o()(s.base, _ && s.base__bigButton, u && Ku.base__anim), onClick: t },
                n().createElement(
                  zu,
                  { contentId: e, direction: _ ? Pu.Top : Pu.Right },
                  n().createElement(
                    L.i,
                    { body: a, isEnabled: u },
                    n().createElement(
                      Xu,
                      {
                        type: v.ghost,
                        size: x.medium,
                        active: r,
                        showIndicator: !1,
                        mixClass: o()(s.toggle, !_ && Ku.toggle__shortBtn),
                      },
                      n().createElement(
                        "div",
                        { className: Ku.settingsLabel },
                        n().createElement("div", {
                          className: o()(Ku.icon, !_ && Ku.icon__shortBtn),
                        }),
                        _ && Ju.setup(),
                      ),
                    ),
                  ),
                ),
                Boolean(i) && n().createElement("div", { className: Ku.bubble }),
              );
            },
          ),
          er = [
            "isSelected",
            "onHoverChanged",
            "isSettingsActive",
            "withSettingsNotification",
            "state",
          ];
        function tr() {
          return (
            (tr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            tr.apply(this, arguments)
          );
        }
        const ar = (e) => {
          let t = e.isSelected,
            a = e.onHoverChanged,
            _ = e.isSettingsActive,
            u = e.withSettingsNotification,
            i = e.state,
            o = (function (e, t) {
              if (null == e) return {};
              var a,
                _,
                u = {},
                r = Object.keys(e);
              for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
              return u;
            })(e, er);
          const s = (0, r.useCallback)((e) => {
              e.stopPropagation();
            }, []),
            l = (0, ge.B)(a),
            c = l[0],
            m = l[1],
            d = [re.Id.B0, re.Id.B1].includes(o.size),
            b = (c || t || _) && !(1 === i),
            g = ((e, t) => {
              const a = J("tutorialModel.effects.items").filter((a) => {
                if (!a) return !1;
                const _ = a.value,
                  u = window.__featureId.toString();
                return _.componentId === e && _.type === t && _.viewId === u;
              });
              if (0 === a.length) return null;
              const _ = Object.assign({}, a[0].value);
              return {
                effect: _,
                completeEffect: () => {
                  (tutorialModel.onEffectCompleted({
                    componentId: e,
                    viewId: window.__featureId.toFixed(0),
                    effectType: t,
                    effectBuilder: _.builder,
                  }),
                    t === Ru && window.tutorialApi && window.tutorialApi.updateComponents());
                },
              };
            })("RandomBattleModeGameface", Ru);
          return (
            (0, r.useEffect)(
              () =>
                Na(() => {
                  null !== g && g.completeEffect();
                }),
              [g],
            ),
            n().createElement(
              ze,
              tr(
                {
                  id: "mode-selector-random-battle",
                  isSelected: t,
                  onHoverChanged: m,
                  state: i,
                  belowStatusComponent: n().createElement(Qu, {
                    contentId: R.views.lobby.mode_selector.popovers.RandomBattlePopover("resId"),
                    handleSettingsClick: s,
                    body: R.strings.tooltips.mode_selector.popover.body(),
                    showBigSettingsButton: d,
                    isShowButton: b,
                    isSettingsActive: _,
                    withBubble: u,
                  }),
                },
                o,
              ),
            )
          );
        };
        function _r() {
          return (
            (_r =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            _r.apply(this, arguments)
          );
        }
        const ur = [re.Id.B5, re.Id.B6],
          rr = [re.Id.B4, re.Id.B5, re.Id.B6],
          nr = [re.Id.B4, re.Id.B5, re.Id.B6],
          ir = (e) => {
            let t = _r({}, e);
            return n().createElement(
              ze,
              _r(
                {
                  calendarTooltip: ie.D3,
                  forceShowIcon: t.showWidget && ur.includes(t.size),
                  hideStatus: t.showWidget && rr.includes(t.size),
                  noWidgetSizes: nr,
                },
                t,
              ),
            );
          },
          or = "StrongholdCard_widgetOverlay_66";
        function sr() {
          return (
            (sr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            sr.apply(this, arguments)
          );
        }
        const lr = [re.Id.B5, re.Id.B6],
          cr = [re.Id.B5, re.Id.B6],
          mr = (e) => {
            let t = sr({}, e);
            return n().createElement(
              ze,
              sr(
                {
                  forceShowIcon: t.showWidget && cr.includes(t.size),
                  noWidgetSizes: lr,
                  classNames: { widgetOverlay: or },
                },
                t,
              ),
            );
          };
        let dr;
        !(function (e) {
          ((e.High = "high"), (e.Medium = "medium"), (e.Low = "low"));
        })(dr || (dr = {}));
        const br = {
            base: "Performance_base_2a",
            text: "Performance_text_93",
            text__medium: "Performance_text__medium_94",
            text__high: "Performance_text__high_c4",
            icon: "Performance_icon_4e",
            icon__medium: "Performance_icon__medium_66",
            icon__high: "Performance_icon__high_59",
          },
          gr = (0, r.memo)(({ modeName: e, performanceRisk: t = dr.Low }) => {
            const a = R.strings.mode_selector.mode.$dyn(e),
              _ = o()(br.text, br[`text__${t}`]),
              u = (0, r.useMemo)(
                () => ({
                  icon: n().createElement("div", { className: o()(br.icon, br[`icon__${t}`]) }),
                }),
                [t],
              ),
              i = (0, r.useMemo)(() => {
                if (a)
                  return {
                    header: a.performanceRisk.$dyn(t).header(),
                    body: a.performanceRisk.$dyn(t).description(),
                  };
              }, [a, t]),
              s = a.performanceRisk.$dyn(t).headerIcon();
            return n().createElement(
              L.i,
              i,
              n().createElement(
                "div",
                { className: br.base },
                n().createElement(de.z, { classMix: _, text: s, binding: u }),
              ),
            );
          }),
          Er = {
            name: "WTCard_name_2f",
            name__b0: "WTCard_name__b0_fc",
            name__b1: "WTCard_name__b1_a7",
            name__b0__medium: "WTCard_name__b0__medium_c3",
            name__b1__medium: "WTCard_name__b1__medium_00",
            name__b0__extraLarge: "WTCard_name__b0__extraLarge_3a",
            name__b0__large: "WTCard_name__b0__large_32",
            name__b1__extraLarge: "WTCard_name__b1__extraLarge_b4",
            name__b1__large: "WTCard_name__b1__large_5a",
            subtitle__b0: "WTCard_subtitle__b0_55",
            subtitle__b1: "WTCard_subtitle__b1_d8",
            subtitle__b0__medium: "WTCard_subtitle__b0__medium_80",
            subtitle__b1__medium: "WTCard_subtitle__b1__medium_ad",
            subtitle__b0__extraLarge: "WTCard_subtitle__b0__extraLarge_b0",
            subtitle__b0__large: "WTCard_subtitle__b0__large_0e",
            subtitle__b1__extraLarge: "WTCard_subtitle__b1__extraLarge_8d",
            subtitle__b1__large: "WTCard_subtitle__b1__large_ad",
            performance: "WTCard_performance_cd",
          },
          pr = ["showWidget", "size", "rewardList", "performanceRisk"];
        function Ar() {
          return (
            (Ar =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            Ar.apply(this, arguments)
          );
        }
        const Cr = [re.Id.B5, re.Id.B6],
          Fr = (0, r.memo)((e) => {
            let t = e.showWidget,
              a = e.size,
              _ = e.rewardList,
              u = e.performanceRisk,
              r = void 0 === u ? dr.Low : u,
              i = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, pr);
            const s = a === re.Id.B1 || (a === re.Id.B2 && !t) ? _ : [],
              l = (0, ue.Z)((0, re.Hp)("name", "subtitle"), Er),
              c = r !== dr.Low && (a === re.Id.B0 || a === re.Id.B1),
              m = c
                ? {
                    name: o()(Er.name, l[`name__${a}`]),
                    subtitle: o()(Er.subtitle, l[`subtitle__${a}`]),
                  }
                : void 0;
            return n().createElement(
              ze,
              Ar(
                {
                  calendarTooltip: ie.U4,
                  noWidgetSizes: Cr,
                  divider: "\n",
                  showWidget: t,
                  size: a,
                  rewardList: s,
                  classNames: m,
                  nameSuffixComponent:
                    c &&
                    n().createElement(
                      "div",
                      { className: Er.performance },
                      n().createElement(gr, { modeName: "white_tiger", performanceRisk: r }),
                    ),
                },
                i,
                { statusActive: t ? "" : R.strings.mode_selector.mode.white_tiger.description() },
              ),
            );
          }),
          Br = ["type", "widget", "isContentVisible"];
        function hr() {
          return (
            (hr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            hr.apply(this, arguments)
          );
        }
        const Dr = [re.Id.B6],
          fr = (e) => {
            let t = e.type,
              a = e.widget,
              _ = e.isContentVisible,
              u = void 0 === _ || _,
              r = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, Br);
            const i = r.size;
            switch (t) {
              case 1:
                return n().createElement(ar, r);
              case 2: {
                const e =
                  a && a.isEnabled && !r.isLocked && n().createElement(le.n, hr({ size: i }, a));
                return n().createElement(ir, hr({ widgetComponent: e }, r));
              }
              case 3:
                return n().createElement(ze, hr({ calendarTooltip: ie.zD }, r));
              case 4: {
                const e =
                  a &&
                  a.isEnabled &&
                  !r.isLocked &&
                  n().createElement(se.Gg, hr({ size: i, conditions: r.conditions }, a));
                return n().createElement(
                  ze,
                  hr(
                    {
                      calendarTooltip: ie.TR,
                      widgetComponent: e,
                      noWidgetSizes: Dr,
                      divider: "\n",
                    },
                    r,
                  ),
                );
              }
              case 5: {
                const e = a,
                  t = e.status,
                  _ = e.stageCurrentPoints,
                  u = e.stageMaximumPoints,
                  o =
                    a &&
                    t === ne.ACTIVE &&
                    n().createElement(oe.$, { size: i, isCompletedProgression: _ === u });
                return n().createElement(
                  _t,
                  hr({ widgetComponent: o, widget: a, divider: "\n" }, r),
                );
              }
              case 6:
                return n().createElement(
                  Mu,
                  hr({ calendarTooltip: ie.$b, widget: a, isContentVisible: u, divider: "\n" }, r),
                );
              case 7:
                return n().createElement(I_, hr({ calendarTooltip: ie.hg, widget: a }, r));
              case 9:
                return n().createElement(Z_, hr({ widget: a }, r));
              case 10: {
                const e = a && !r.isLocked && n().createElement(ce.b, hr({ size: i }, a));
                return n().createElement(mr, hr({ widgetComponent: e }, r));
              }
              case 11: {
                const e = a && a.isEnabled && n().createElement(me.B, hr({ size: i }, a));
                return n().createElement(Fr, hr({ widgetComponent: e }, r));
              }
              default:
                return n().createElement(ze, r);
            }
          },
          vr = "Column_base_41";
        function xr() {
          return (
            (xr =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            xr.apply(this, arguments)
          );
        }
        const Sr = ({
            items: e,
            showWidgets: t,
            state: a,
            canBeWide: _ = !1,
            isContentVisible: u = !0,
          }) => {
            const r = (0, re.SH)(e.length, _);
            return n().createElement(
              "div",
              { className: vr },
              e
                .sort((e, t) => e.priority - t.priority)
                .map((e) =>
                  n().createElement(
                    fr,
                    xr({ key: `item_${e.index}` }, e, {
                      size: r,
                      showWidget: t,
                      state: a,
                      isContentVisible: u,
                    }),
                  ),
                ),
            );
          },
          wr = {
            base: "ModeSelectorViewApp_base_4a",
            placeholder: "ModeSelectorViewApp_placeholder_1e",
            base__show: "ModeSelectorViewApp_base__show_3c",
            closeButton: "ModeSelectorViewApp_closeButton_d2",
            closeButton__extraSmall: "ModeSelectorViewApp_closeButton__extraSmall_52",
            closeButton__small: "ModeSelectorViewApp_closeButton__small_e4",
            toggleButton: "ModeSelectorViewApp_toggleButton_a8",
            toggleButtonContainer: "ModeSelectorViewApp_toggleButtonContainer_23",
            title: "ModeSelectorViewApp_title_f5",
            title__medium: "ModeSelectorViewApp_title__medium_99",
            title__extraSmall: "ModeSelectorViewApp_title__extraSmall_e5",
            title__small: "ModeSelectorViewApp_title__small_32",
            selectMap: "ModeSelectorViewApp_selectMap_4a",
            selectMap__empty: "ModeSelectorViewApp_selectMap__empty_ce",
            selectMapTitle: "ModeSelectorViewApp_selectMapTitle_00",
            selectMapTitle__extraSmall: "ModeSelectorViewApp_selectMapTitle__extraSmall_3a",
            selectMapTitle__small: "ModeSelectorViewApp_selectMapTitle__small_01",
            selectMapTitle__medium: "ModeSelectorViewApp_selectMapTitle__medium_a1",
            selectMapButton: "ModeSelectorViewApp_selectMapButton_04",
            buttonText: "ModeSelectorViewApp_buttonText_44",
            centerBlock: "ModeSelectorViewApp_centerBlock_13",
            items: "ModeSelectorViewApp_items_8f",
            base__hide: "ModeSelectorViewApp_base__hide_20",
            hide: "ModeSelectorViewApp_hide_4a",
            show: "ModeSelectorViewApp_show_ef",
            items__medium: "ModeSelectorViewApp_items__medium_72",
            items__extraSmall: "ModeSelectorViewApp_items__extraSmall_fc",
            items__small: "ModeSelectorViewApp_items__small_36",
          },
          kr = () => {
            const e = J(),
              t = e.isMapSelectionVisible,
              a = e.isMapSelectionEnabled,
              _ = e.onShowMapSelectionClicked,
              u = e.onShowWidgetsClicked,
              i = e.areWidgetsVisible,
              s = e.state,
              l = e.isContentVisible,
              c = J("model.cardList"),
              m = (0, r.useState)(!1),
              d = m[0],
              b = m[1],
              g = (0, r.useRef)(!0),
              E = 1 !== s,
              p = E && i === !d,
              A = (0, ue.Z)(["closeButton", "title", "items", "selectMapTitle"], wr),
              C = {};
            c.forEach(({ value: e }) => {
              const t = e.column;
              (t in C || (C[t] = new Array()), C[t].push(e));
            });
            const F = Object.keys(C)
                .sort((e, t) => parseInt(e) - parseInt(t))
                .map((e) => C[e]),
              B = (0, r.useCallback)(() => {
                (0, I.Sy)();
              }, []),
              h = (0, r.useCallback)(() => {
                _();
              }, [_]),
              D = (0, r.useCallback)(() => {
                u();
              }, [u]),
              f = (0, r.useCallback)(() => {
                g.current = !0;
              }, []),
              S = (0, r.useCallback)(() => {
                ((g.current = !1), !i && d && b(!1));
              }, [i, d]);
            (_e(),
              (0, r.useEffect)(() => {
                function e(e) {
                  g.current && b(e.altKey);
                }
                return (
                  window.addEventListener("keydown", e),
                  window.addEventListener("keyup", e),
                  () => {
                    (window.removeEventListener("keydown", e),
                      window.removeEventListener("keyup", e));
                  }
                );
              }, []));
            const k = (0, r.useRef)(null);
            return (
              (0, r.useEffect)(() => {
                k.current &&
                  (l
                    ? (k.current.classList.remove(wr.base__hide),
                      k.current.classList.add(wr.base__show))
                    : (k.current.classList.remove(wr.base__show),
                      k.current.classList.add(wr.base__hide)));
              }, [l]),
              n().createElement(
                "div",
                { className: wr.base, ref: k },
                n().createElement(
                  "div",
                  { className: wr.placeholder, onMouseOver: f, onMouseLeave: S },
                  n().createElement(
                    "div",
                    { className: A.closeButton },
                    n().createElement(y, {
                      caption: R.strings.menu.viewHeader.closeBtn.label(),
                      type: "close",
                      side: "right",
                      onClick: B,
                    }),
                  ),
                  n().createElement(
                    "div",
                    { className: wr.centerBlock },
                    n().createElement(
                      "div",
                      { className: A.title },
                      R.strings.mode_selector.title(),
                    ),
                    n().createElement(
                      "div",
                      { className: o()(wr.selectMap, !t && wr.selectMap__empty) },
                      n().createElement(
                        "div",
                        { className: A.selectMapTitle },
                        R.strings.mode_selector.selectMap(),
                      ),
                      n().createElement(
                        w,
                        {
                          size: x.small,
                          type: v.primary,
                          mixClass: wr.selectMapButton,
                          onClick: h,
                          disabled: !a,
                        },
                        n().createElement(
                          "div",
                          { className: wr.buttonText },
                          R.strings.mode_selector.button.select(),
                        ),
                      ),
                    ),
                    n().createElement(
                      "div",
                      { className: wr.items },
                      F.map((e, t) =>
                        n().createElement(Sr, {
                          key: `column_${t}`,
                          items: e,
                          showWidgets: p,
                          state: s,
                          canBeWide: 0 === t && F.length <= 3,
                          isContentVisible: l,
                        }),
                      ),
                    ),
                    E &&
                      n().createElement(
                        "div",
                        { className: wr.toggleButtonContainer },
                        l &&
                          n().createElement(
                            L.i,
                            { body: R.strings.tooltips.mode_selector.progressionBtn.body() },
                            n().createElement(
                              "div",
                              { id: "mode-selector-widgets-btn" },
                              n().createElement(
                                Xu,
                                {
                                  size: x.small,
                                  type: v.secondary,
                                  onClick: D,
                                  active: p,
                                  mixClass: wr.toggleButton,
                                },
                                R.strings.mode_selector.button.progression(),
                              ),
                            ),
                          ),
                      ),
                  ),
                ),
              )
            );
          };
        (_.O.view.extraSize.set(0, 0),
          _.O.view.whenTutorialReady.then(() => {
            B().render(
              n().createElement(C, null, n().createElement(kr, null)),
              document.getElementById("root"),
            );
          }));
      },
      8668: (e, t, a) => {
        "use strict";
        a.d(t, { Hi: () => r, Jh: () => u, S4: () => i, u_: () => n });
        var _ = a(3486);
        let u;
        !(function (e) {
          ((e.Huge = "huge"), (e.Big = "big"), (e.Medium = "medium"), (e.Small = "small"));
        })(u || (u = {}));
        const r = [_.Id.B4, _.Id.B5, _.Id.B6],
          n = [_.Id.B0, _.Id.B1, _.Id.B2],
          i = {
            [_.Id.B0]: { [_.Cg.Big]: u.Huge, [_.Cg.Medium]: u.Huge, [_.Cg.Small]: u.Big },
            [_.Id.B1]: { [_.Cg.Big]: u.Huge, [_.Cg.Medium]: u.Huge, [_.Cg.Small]: u.Big },
            [_.Id.B2]: { [_.Cg.Big]: u.Huge, [_.Cg.Medium]: u.Huge, [_.Cg.Small]: u.Big },
            [_.Id.B3]: { [_.Cg.Big]: u.Huge, [_.Cg.Medium]: u.Big, [_.Cg.Small]: u.Big },
            [_.Id.B4]: { [_.Cg.Big]: u.Big, [_.Cg.Medium]: u.Big, [_.Cg.Small]: u.Medium },
            [_.Id.B5]: { [_.Cg.Big]: u.Medium, [_.Cg.Medium]: u.Medium, [_.Cg.Small]: u.Small },
            [_.Id.B6]: { [_.Cg.Big]: u.Medium, [_.Cg.Medium]: u.Small, [_.Cg.Small]: u.Small },
          };
      },
      8188: (e, t, a) => {
        "use strict";
        a.d(t, { B: () => l });
        var _ = a(280),
          u = a(6179),
          r = a.n(u),
          n = a(8487);
        const i =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          o = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          s = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          l = ({ text: e, binding: t, classMix: a }) => {
            const l = (0, u.useCallback)((e) => ({ color: `#${e}` }), []),
              c = t || {};
            let m = i.exec(e),
              d = e;
            for (; m;) {
              const a = m[0],
                u = o.exec(a),
                b = s.exec(a),
                g = m[1];
              if (u && b) {
                const e = u[0],
                  i = e + b[0].length + e;
                ((d = d.replace(a, `%(${i})`)),
                  (c[i] = n.Z[e]
                    ? r().createElement(
                        "span",
                        { className: n.Z[e] },
                        r().createElement(_.z, { text: g, binding: t }),
                      )
                    : r().createElement(
                        "span",
                        { style: l(e) },
                        r().createElement(_.z, { text: g, binding: t }),
                      )));
              }
              m = i.exec(e);
            }
            return r().createElement(_.z, { text: d, classMix: a, binding: c });
          };
      },
      9930: (e, t, a) => {
        "use strict";
        a.d(t, { B: () => n, O: () => i });
        var _ = a(7739),
          u = a(6179),
          r = a(3486);
        const n = (e) => {
            const t = (0, u.useState)(!1),
              a = t[0],
              _ = t[1],
              r = (0, u.useCallback)(
                (t) => {
                  (_(t), e && e(t));
                },
                [e],
              );
            return [a, r];
          },
          i = () => {
            const e = (0, u.useContext)(_.YN),
              t = e.extraSmall,
              a = e.small,
              n = e.medium;
            return (0, u.useMemo)(() => {
              switch (!0) {
                case a:
                case t:
                  return r.Cg.Small;
                case n:
                  return r.Cg.Medium;
                default:
                  return r.Cg.Big;
              }
            }, [t, n, a]);
          };
      },
      3486: (e, t, a) => {
        "use strict";
        a.d(t, { Cg: () => r, Hp: () => o, Id: () => u, SH: () => n, d6: () => _ });
        const _ = (e) => R.images.gui.maps.icons.mode_selector.mode.$dyn(e);
        let u, r;
        (!(function (e) {
          ((e.B0 = "b0"),
            (e.B1 = "b1"),
            (e.B2 = "b2"),
            (e.B3 = "b3"),
            (e.B4 = "b4"),
            (e.B5 = "b5"),
            (e.B6 = "b6"));
        })(u || (u = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"));
          })(r || (r = {})));
        const n = (e, t = !1) =>
            t && 1 === e ? u.B0 : `b${Math.min(Math.max(Math.floor(e), 0), 6)}`,
          i = {},
          o = (...e) => {
            let t = [];
            for (var a = 0, _ = e; a < _.length; a++) {
              const e = _[a];
              if (e in i) t = t.concat(i[e]);
              else {
                const a = [e];
                for (let t = 0; t <= 6; t++) a.push(`${e}__${n(t)}`);
                ((i[e] = a), (t = t.concat(i[e])));
              }
            }
            return t;
          };
      },
      4194: (e, t, a) => {
        "use strict";
        a.d(t, { $: () => b });
        var _ = a(6483),
          u = a.n(_),
          r = a(9924),
          n = a(6179),
          i = a.n(n),
          o = a(8668),
          s = a(9930),
          l = a(3486);
        const c = {
            base: "Widget_base_e7",
            icon: "Widget_icon_16",
            icon__huge: "Widget_icon__huge_6c",
            icon__big: "Widget_icon__big_ad",
            icon__medium: "Widget_icon__medium_db",
            icon__small: "Widget_icon__small_ea",
            icon__b0: "Widget_icon__b0_19",
            icon__b1: "Widget_icon__b1_0b",
            icon__b0__medium: "Widget_icon__b0__medium_43",
            icon__b1__medium: "Widget_icon__b1__medium_85",
            icon__b0__extraSmall: "Widget_icon__b0__extraSmall_a2",
            icon__b0__small: "Widget_icon__b0__small_c9",
            icon__b1__extraSmall: "Widget_icon__b1__extraSmall_6a",
            icon__b1__small: "Widget_icon__b1__small_67",
            icon__b2: "Widget_icon__b2_c7",
            icon__b2__medium: "Widget_icon__b2__medium_7f",
            icon__b2__extraSmall: "Widget_icon__b2__extraSmall_6b",
            icon__b2__small: "Widget_icon__b2__small_33",
            icon__b3: "Widget_icon__b3_21",
            icon__b3__medium: "Widget_icon__b3__medium_8c",
            icon__b3__extraSmall: "Widget_icon__b3__extraSmall_a9",
            icon__b3__small: "Widget_icon__b3__small_c7",
            icon__b4: "Widget_icon__b4_55",
            icon__b4__medium: "Widget_icon__b4__medium_f1",
            icon__b4__extraSmall: "Widget_icon__b4__extraSmall_26",
            icon__b4__small: "Widget_icon__b4__small_78",
            icon__b5: "Widget_icon__b5_af",
            icon__b5__medium: "Widget_icon__b5__medium_67",
            icon__b5__extraSmall: "Widget_icon__b5__extraSmall_7e",
            icon__b5__small: "Widget_icon__b5__small_32",
            icon__b6: "Widget_icon__b6_3a",
            icon__b6__medium: "Widget_icon__b6__medium_e3",
            icon__b6__extraSmall: "Widget_icon__b6__extraSmall_3e",
            icon__b6__small: "Widget_icon__b6__small_69",
          },
          m = {
            [o.Jh.Huge]: "130x130",
            [o.Jh.Big]: "64x64",
            [o.Jh.Medium]: "64x64",
            [o.Jh.Small]: "64x64",
          },
          d = R.images.gui.maps.icons.battleRoyale.widget,
          b = ({ size: e, isCompletedProgression: t }) => {
            const a = (0, s.O)(),
              _ = (0, r.Z)([...(0, l.Hp)("icon")], c),
              n = o.S4[e][a],
              b = d.$dyn(`c_${m[n]}`),
              g = b && b.$dyn(t ? "bg1" : "bg2"),
              E = u()(c.icon, c[`icon__${n}`], _[`icon__${e}`]);
            return i().createElement(
              "div",
              { className: c.base },
              i().createElement("div", {
                className: E,
                style: g ? { backgroundImage: `url(${g})` } : void 0,
              }),
            );
          };
      },
      7663: (e, t, a) => {
        "use strict";
        a.d(t, { Gg: () => B });
        var _ = a(6483),
          u = a.n(_),
          r = a(7078),
          n = a(2646),
          i = a(9924),
          o = a(3649),
          s = a(6179),
          l = a.n(s),
          c = a(4090),
          m = a(8188),
          d = a(8668),
          b = a(9930),
          g = a(3486);
        const E = {
          base: "EpicWidget_base_4d",
          icon: "EpicWidget_icon_c8",
          icon__huge: "EpicWidget_icon__huge_1b",
          icon__big: "EpicWidget_icon__big_e5",
          icon__medium: "EpicWidget_icon__medium_5c",
          icon__small: "EpicWidget_icon__small_bc",
          icon__b0: "EpicWidget_icon__b0_36",
          icon__b1: "EpicWidget_icon__b1_9a",
          icon__b0__medium: "EpicWidget_icon__b0__medium_e8",
          icon__b1__medium: "EpicWidget_icon__b1__medium_19",
          icon__b0__extraSmall: "EpicWidget_icon__b0__extraSmall_57",
          icon__b0__small: "EpicWidget_icon__b0__small_25",
          icon__b1__extraSmall: "EpicWidget_icon__b1__extraSmall_b1",
          icon__b1__small: "EpicWidget_icon__b1__small_6f",
          icon__b2: "EpicWidget_icon__b2_21",
          icon__b2__medium: "EpicWidget_icon__b2__medium_37",
          icon__b2__extraSmall: "EpicWidget_icon__b2__extraSmall_1a",
          icon__b2__small: "EpicWidget_icon__b2__small_84",
          icon__b3: "EpicWidget_icon__b3_9c",
          icon__b3__medium: "EpicWidget_icon__b3__medium_6d",
          icon__b3__extraSmall: "EpicWidget_icon__b3__extraSmall_4f",
          icon__b3__small: "EpicWidget_icon__b3__small_ca",
          icon__b4: "EpicWidget_icon__b4_04",
          icon__b4__medium: "EpicWidget_icon__b4__medium_ba",
          icon__b4__extraSmall: "EpicWidget_icon__b4__extraSmall_81",
          icon__b4__small: "EpicWidget_icon__b4__small_fe",
          icon__b5: "EpicWidget_icon__b5_09",
          icon__b5__medium: "EpicWidget_icon__b5__medium_4a",
          icon__b5__extraSmall: "EpicWidget_icon__b5__extraSmall_b1",
          icon__b5__small: "EpicWidget_icon__b5__small_00",
          icon__b6: "EpicWidget_icon__b6_04",
          icon__b6__medium: "EpicWidget_icon__b6__medium_d7",
          icon__b6__extraSmall: "EpicWidget_icon__b6__extraSmall_91",
          icon__b6__small: "EpicWidget_icon__b6__small_9a",
          counter: "EpicWidget_counter_ff",
          counter__huge: "EpicWidget_counter__huge_a5",
          level: "EpicWidget_level_ca",
          icon__bg0: "EpicWidget_icon__bg0_2e",
          icon__bg1: "EpicWidget_icon__bg1_d4",
          icon__bg2: "EpicWidget_icon__bg2_5a",
          icon__bg3: "EpicWidget_icon__bg3_c6",
          icon__bg4: "EpicWidget_icon__bg4_f9",
          icon__bg5: "EpicWidget_icon__bg5_a5",
          level__b0: "EpicWidget_level__b0_17",
          level__b1: "EpicWidget_level__b1_fd",
          level__b2: "EpicWidget_level__b2_cd",
          level__b3: "EpicWidget_level__b3_59",
          level__b0__extraSmall: "EpicWidget_level__b0__extraSmall_48",
          level__b0__small: "EpicWidget_level__b0__small_57",
          level__b1__extraSmall: "EpicWidget_level__b1__extraSmall_e4",
          level__b1__small: "EpicWidget_level__b1__small_10",
          level__b2__extraSmall: "EpicWidget_level__b2__extraSmall_fc",
          level__b2__small: "EpicWidget_level__b2__small_50",
          level__b3__extraSmall: "EpicWidget_level__b3__extraSmall_3d",
          level__b3__small: "EpicWidget_level__b3__small_76",
          subtitle: "EpicWidget_subtitle_e4",
          subtitle__b0: "EpicWidget_subtitle__b0_5d",
          subtitle__b1: "EpicWidget_subtitle__b1_f4",
          subtitle__b0__medium: "EpicWidget_subtitle__b0__medium_60",
          subtitle__b1__medium: "EpicWidget_subtitle__b1__medium_e0",
          subtitle__b0__extraSmall: "EpicWidget_subtitle__b0__extraSmall_7c",
          subtitle__b0__small: "EpicWidget_subtitle__b0__small_23",
          subtitle__b1__extraSmall: "EpicWidget_subtitle__b1__extraSmall_27",
          subtitle__b1__small: "EpicWidget_subtitle__b1__small_ac",
          subtitle__b2: "EpicWidget_subtitle__b2_44",
          subtitle__b2__medium: "EpicWidget_subtitle__b2__medium_b2",
          subtitle__b2__extraSmall: "EpicWidget_subtitle__b2__extraSmall_54",
          subtitle__b2__small: "EpicWidget_subtitle__b2__small_3d",
          subtitle__b3: "EpicWidget_subtitle__b3_c1",
          subtitle__b3__medium: "EpicWidget_subtitle__b3__medium_f2",
          subtitle__b3__extraSmall: "EpicWidget_subtitle__b3__extraSmall_27",
          subtitle__b3__small: "EpicWidget_subtitle__b3__small_2f",
          subtitle__b4: "EpicWidget_subtitle__b4_fa",
          subtitle__b4__medium: "EpicWidget_subtitle__b4__medium_a9",
          subtitle__b4__extraSmall: "EpicWidget_subtitle__b4__extraSmall_ba",
          subtitle__b4__small: "EpicWidget_subtitle__b4__small_9b",
          subtitle__b5: "EpicWidget_subtitle__b5_67",
          subtitle__b5__medium: "EpicWidget_subtitle__b5__medium_f2",
          subtitle__b5__extraSmall: "EpicWidget_subtitle__b5__extraSmall_25",
          subtitle__b5__small: "EpicWidget_subtitle__b5__small_95",
          subtitle__b6: "EpicWidget_subtitle__b6_e7",
          subtitle__b6__medium: "EpicWidget_subtitle__b6__medium_87",
          subtitle__b6__extraSmall: "EpicWidget_subtitle__b6__extraSmall_0f",
          subtitle__b6__small: "EpicWidget_subtitle__b6__small_04",
        };
        let p;
        !(function (e) {
          ((e.Icon1 = "bg0"),
            (e.Icon2 = "bg1"),
            (e.Icon3 = "bg2"),
            (e.Icon4 = "bg3"),
            (e.Icon5 = "bg4"),
            (e.Icon6 = "bg5"));
        })(p || (p = {}));
        const A = {
            [d.Jh.Huge]: "130x130",
            [d.Jh.Big]: "72x72",
            [d.Jh.Medium]: "64x64",
            [d.Jh.Small]: "40x40",
          },
          C = {
            [p.Icon1]: [0],
            [p.Icon2]: [1, 2, 3, 4],
            [p.Icon3]: [5, 6, 7, 8, 9],
            [p.Icon4]: [10, 11, 12, 13, 14],
            [p.Icon5]: [15, 16, 17, 18, 19],
            [p.Icon6]: [20],
          },
          F = [g.Id.B0, g.Id.B1, g.Id.B2],
          B = ({ size: e, level: t, conditions: a, restRewards: _ }) => {
            const B = (0, b.O)(),
              h = (0, i.Z)([...(0, g.Hp)("icon", "level", "subtitle")], E),
              D = (0, s.useMemo)(() => d.S4[e][B], [e, B]),
              f = (0, s.useMemo)(
                () => ((e) => Object.keys(C).find((t) => C[t].includes(e)) || p.Icon1)(t),
                [t],
              ),
              v = (0, s.useMemo)(() => ({ tooltipId: n.I3 }), []),
              x = (0, s.useMemo)(() => {
                const e = R.images.gui.maps.icons.epicBattles.metaLvls;
                if (null !== e) {
                  const t = e.$dyn(`c_${A[D]}`);
                  if (t && void 0 !== f) return { backgroundImage: `url(${t.$dyn(f)})` };
                }
              }, [f, D]),
              S = u()(E.icon, E[`icon__${f}`], E[`icon__${D}`], h[`icon__${e}`]);
            return l().createElement(
              "div",
              { className: E.base },
              l().createElement(
                r.t,
                { args: v },
                l().createElement(
                  "div",
                  { className: S, style: x },
                  _ > 0 &&
                    l().createElement(
                      "div",
                      { className: u()(E.counter, E[`counter__${D}`]) },
                      l().createElement(c.A, { size: "normal", value: _ }),
                    ),
                  t > 0 &&
                    l().createElement("div", { className: u()(E.level, h[`level__${e}`]) }, t),
                ),
              ),
              a &&
                !F.includes(e) &&
                l().createElement(m.B, {
                  classMix: u()(h.subtitle, h[`subtitle__${e}`]),
                  text: (0, o.z4)(a),
                }),
            );
          };
      },
      2100: (e, t, a) => {
        "use strict";
        a.d(t, { n: () => ce });
        var _ = a(6483),
          u = a.n(_),
          r = a(7739),
          n = a(9924),
          i = a(6179),
          o = a.n(i),
          s = a(3486),
          l = a(7078),
          c = a(2646),
          m = a(4179);
        const d = "BonusBattles_base_1b",
          b = "BonusBattles_light_51",
          g = "BonusBattles_divider_52",
          E = "BonusBattles_divider__right_08",
          p = "BonusBattles_icon_2c",
          A = "BonusBattles_amount_a2",
          C = { tooltipId: c.T3 },
          F = (0, i.memo)((e) => {
            const t = e.amount,
              a = m.Z5.getNumberFormat(t, m.B3.INTEGRAL),
              _ = u()(g, E);
            return o().createElement(
              l.t,
              { args: C },
              o().createElement(
                "div",
                { className: d },
                o().createElement("div", { className: b }),
                o().createElement("div", { className: g }),
                o().createElement("div", { className: p }),
                o().createElement("div", { className: A }, a),
                o().createElement("div", { className: _ }),
              ),
            );
          });
        let B, h;
        (!(function (e) {
          ((e.ExtraLarge = "extraLarge"),
            (e.Large = "large"),
            (e.Medium = "medium"),
            (e.SMedium = "smedium"),
            (e.Small = "small"),
            (e.ExtraSmall = "extraSmall"),
            (e.Tiny = "tiny"));
        })(B || (B = {})),
          (function (e) {
            ((e.Large = "large"),
              (e.Medium = "medium"),
              (e.SMedium = "smedium"),
              (e.Small = "small"),
              (e.ExtraSmall = "extraSmall"));
          })(h || (h = {})));
        const D = {
            base: "Blink_base_67",
            blink: "Blink_blink_75",
            blinker: "Blink_blinker_ef",
            widget: "Blink_widget_98",
            widgetBlinker: "Blink_widgetBlinker_14",
            widget__small: "Blink_widget__small_ea",
            widgetBlinkerSmall: "Blink_widgetBlinkerSmall_f2",
          },
          f = (0, i.memo)(({ isWidget: e = !1, size: t = h.Medium }) => {
            const a = u()(D.base, { [D.widget]: e, [D[`widget__${t}`]]: e });
            return o().createElement(
              "div",
              { className: a },
              o().createElement("div", { className: D.blink }),
            );
          }),
          v = {
            base: "Rank_base_80",
            icon: "Rank_icon_64",
            icon__extraSmall: "Rank_icon__extraSmall_ed",
            icon__medium: "Rank_icon__medium_c3",
            icon__large: "Rank_icon__large_65",
            icon__next: "Rank_icon__next_89",
            frame: "Rank_frame_88",
            frame__extraSmall: "Rank_frame__extraSmall_6a",
            frame__small: "Rank_frame__small_33",
            unburnable: "Rank_unburnable_65",
            unburnable__small: "Rank_unburnable__small_76",
            lock: "Rank_lock_01",
            lock__medium: "Rank_lock__medium_89",
            lock__extraSmall: "Rank_lock__extraSmall_c1",
            lock__small: "Rank_lock__small_6f",
          },
          x = {
            [h.Large]: "80x110",
            [h.Medium]: "58x80",
            [h.SMedium]: "58x80",
            [h.Small]: "42x56",
            [h.ExtraSmall]: "42x56",
          },
          S = (0, i.memo)((e) => {
            const t = e.isInactive,
              a = void 0 !== t && t,
              _ = e.divisionID,
              r = e.rankName,
              n = e.rankID,
              s = e.isUnburnable,
              m = e.size,
              d = void 0 === m ? h.Medium : m,
              b = e.isLocked,
              g = void 0 !== b && b,
              E = (0, i.useMemo)(() => {
                const e = R.images.gui.maps.icons.rankedBattles,
                  t = x[d],
                  a = e.ranks.$dyn(`c_${t}`),
                  u = a && a.$dyn(`rank${_}_${r}`);
                return u ? { backgroundImage: `url(${u})` } : void 0;
              }, [_, r, d]),
              p = (e) => [v[e], v[`${e}__${d}`]],
              A = u()(v.icon, a && v.icon__next, ...p("icon")),
              C = u()(...p("frame"), ...p("unburnable")),
              F = u()(...p("lock")),
              B = d !== h.ExtraSmall;
            return o().createElement(
              l.t,
              { args: { rankID: n, tooltipId: c.MS } },
              o().createElement(
                "div",
                { className: v.base },
                o().createElement("div", { className: A, style: E }),
                s && o().createElement("div", { className: C }),
                !a && B && o().createElement(f, { isWidget: !0, size: d }),
                g && o().createElement("div", { className: F, "data-emblem": "lock" }),
              ),
            );
          }),
          w = {
            base: "Division_base_30",
            base__extraSmall: "Division_base__extraSmall_1a",
            base__smedium: "Division_base__smedium_98",
            base__medium: "Division_base__medium_08",
            base__hasOneRank: "Division_base__hasOneRank_66",
            steps: "Division_steps_31",
            steps__small: "Division_steps__small_b4",
            step: "Division_step_54",
            step__notReceived: "Division_step__notReceived_d3",
            step__small: "Division_step__small_b3",
          };
        function k() {
          return (
            (k =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            k.apply(this, arguments)
          );
        }
        const N = { tooltipId: c.u6 },
          T = (e) => {
            const t = e.rankLeft,
              a = void 0 === t ? void 0 : t,
              _ = e.rankRight,
              r = e.steps,
              n = e.stepsTotal,
              c = e.size,
              m = e.maxRank,
              d = e.cardSize,
              b = n > 0 && !_.isQualification,
              g = void 0 !== a || b,
              E = ![B.ExtraLarge, B.Medium].includes(c),
              p = _.rankID > m,
              A = void 0 === a,
              C = (0, i.useMemo)(
                () =>
                  [B.Small, B.ExtraSmall].includes(c)
                    ? h.ExtraSmall
                    : B.SMedium === c
                      ? h.Small
                      : h.Medium,
                [c],
              ),
              F = u()(w.base, w[`base__${B.SMedium === c && d === s.Id.B2 ? B.Medium : c}`], {
                [w.base__hasOneRank]: A,
              }),
              D = u()(
                w.steps,
                E && w.steps__small,
                c === B.Medium && w.steps__wide,
                void 0 === a && w.steps__side,
              );
            return o().createElement(
              "div",
              { className: F },
              a && o().createElement(S, k({}, a, { size: C })),
              b &&
                o().createElement(
                  l.t,
                  { args: N },
                  o().createElement(
                    "div",
                    { className: D },
                    [...Array(n)].map((e, t) => {
                      return o().createElement("div", {
                        key: `step_${t}`,
                        className:
                          ((a = t < r), u()(w.step, E && w.step__small, !a && w.step__notReceived)),
                      });
                      var a;
                    }),
                  ),
                ),
              o().createElement(S, k({}, _, { size: C, isInactive: g, isLocked: p })),
            );
          },
          y = {
            base: "RankedStat_base_29",
            icon: "RankedStat_icon_83",
            icon__efficiency: "RankedStat_icon__efficiency_9e",
            icon__efficiency__medium: "RankedStat_icon__efficiency__medium_e6",
            icon__position: "RankedStat_icon__position_6f",
            icon__position__medium: "RankedStat_icon__position__medium_10",
            value: "RankedStat_value_cb",
            value__medium: "RankedStat_value__medium_dc",
            delta: "RankedStat_delta_ff",
            delta__medium: "RankedStat_delta__medium_89",
            delta__smedium: "RankedStat_delta__smedium_74",
            delta__minus: "RankedStat_delta__minus_71",
            arrow: "RankedStat_arrow_97",
            arrow__medium: "RankedStat_arrow__medium_f8",
            arrow__smedium: "RankedStat_arrow__smedium_52",
            arrow__minus: "RankedStat_arrow__minus_e1",
          };
        let L, M;
        (!(function (e) {
          ((e.Efficiency = "efficiency"), (e.Position = "position"));
        })(L || (L = {})),
          (function (e) {
            ((e.Medium = "medium"), (e.SMedium = "smedium"));
          })(M || (M = {})));
        const W = {
            [L.Efficiency]: "rankedBattlesEfficiency",
            [L.Position]: "RANKED_BATTLES_POSITION_TOOLTIP",
          },
          I = (0, i.memo)(
            ({
              type: e,
              value: t,
              valueDiff: a = 0,
              isUnavailable: _ = !1,
              isPercent: r = !1,
              size: n = M.Medium,
            }) => {
              const i = (e) =>
                  _
                    ? "---"
                    : r
                      ? m.Z5.getRealFormat(100 * e, m.Gr.WO_ZERO_DIGITS) + "%"
                      : m.Z5.getRealFormat(e, m.Gr.WO_ZERO_DIGITS),
                s = i(t),
                c = i(a);
              return o().createElement(
                l.t,
                { args: { tooltipId: W[e] } },
                o().createElement(
                  "div",
                  { className: u()(y.base, y[`base__${n}`]) },
                  o().createElement("div", {
                    className: u()(y.icon, y[`icon__${e}`], y[`icon__${e}__${n}`]),
                  }),
                  o().createElement("div", { className: u()(y.value, y[`value__${n}`]) }, s),
                  0 !== a &&
                    !_ &&
                    o().createElement(
                      "div",
                      { className: u()(y.delta, y[`delta__${n}`], a < 0 && y.delta__minus) },
                      o().createElement("div", {
                        className: u()(y.arrow, y[`arrow__${n}`], a < 0 && y.arrow__minus),
                      }),
                      c,
                    ),
                ),
              );
            },
          ),
          P = 33,
          O = 0,
          H = !0,
          $ = "play";
        const z = [
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
        function G() {
          return (
            (G =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var _ in a) Object.prototype.hasOwnProperty.call(a, _) && (e[_] = a[_]);
                }
                return e;
              }),
            G.apply(this, arguments)
          );
        }
        const U = (0, i.memo)(function (e) {
            let t = e.width,
              a = e.height,
              _ = e.getImageSource,
              u = e.frameCount,
              r = e.onAnimate,
              n = e.frameTime,
              s = void 0 === n ? P : n,
              l = e.initialFrameIndex,
              c = void 0 === l ? O : l,
              m = e.lastFrameIndex,
              d = void 0 === m ? u - 1 : m,
              b = e.loop,
              g = void 0 === b ? H : b,
              E = e.state,
              p = void 0 === E ? $ : E,
              A = e.onAnimationDone,
              C = e.onAnimationComplete,
              F = e.poster,
              B = (function (e, t) {
                if (null == e) return {};
                var a,
                  _,
                  u = {},
                  r = Object.keys(e);
                for (_ = 0; _ < r.length; _++) ((a = r[_]), t.indexOf(a) >= 0 || (u[a] = e[a]));
                return u;
              })(e, z);
            const h = (0, i.useRef)(null);
            return (
              (0, i.useEffect)(() => {
                const e = h.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  a = (a) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(a.img, -a.x, -a.y));
                  };
                switch (p) {
                  case "play":
                    return (function () {
                      const e = q(c, d, _),
                        t = j(c, d),
                        u = window.setInterval(() => {
                          const _ = t(),
                            n = e.get(_);
                          n
                            ? (null == r || r(_, n),
                              a(n),
                              _ === d &&
                                (null == C || C(),
                                g || (null == A || A(), window.clearInterval(u))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, s);
                      return () => window.clearInterval(u);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === c && F ? { path: F, x: 0, y: 0 } : _(c),
                        t = new Image();
                      t.src = e.path;
                      const u = () => a(V(e, t));
                      return (
                        t.addEventListener("load", u),
                        () => t.removeEventListener("load", u)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [s, _, c, d, g, r, C, A, F, p]),
              o().createElement("canvas", G({}, B, { width: t, height: a, ref: h }))
            );
          }),
          j = (e, t) => {
            let a = e;
            return () => {
              const _ = a;
              return ((a += 1), a > t && (a = e), _);
            };
          },
          V = (e, t) => Object.assign({}, e, { img: t }),
          q = (e, t, a) => {
            const _ = new Map(),
              u = {};
            for (let r = e; r <= t; r++) {
              const e = a(r),
                t = u[e.path];
              if (t) _.set(r, V(e, t));
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
                  _.set(r, V(e, t)));
              }
            }
            return _;
          };
        var Z = a(3138),
          Y = a(4598);
        const X = {
            base: "AnimatedBackground_base_12",
            widget: "AnimatedBackground_widget_3d",
            rays: "AnimatedBackground_rays_85",
            sunShineCanvas: "AnimatedBackground_sunShineCanvas_27",
            staticHighlight: "AnimatedBackground_staticHighlight_a8",
            widget__smedium: "AnimatedBackground_widget__smedium_a0",
            animation: "AnimatedBackground_animation_06",
            fadeIn: "AnimatedBackground_fadeIn_78",
            none: "AnimatedBackground_none_f0",
            raysAppearance: "AnimatedBackground_raysAppearance_7c",
            rotate: "AnimatedBackground_rotate_fa",
            "reverse-rotate": "AnimatedBackground_reverse-rotate_cc",
            slideUp: "AnimatedBackground_slideUp_64",
            fadeInWithScale: "AnimatedBackground_fadeInWithScale_ae",
            lockStartAnimation: "AnimatedBackground_lockStartAnimation_d6",
            lockEndAnimation: "AnimatedBackground_lockEndAnimation_17",
            fadeOut: "AnimatedBackground_fadeOut_50",
          },
          K = {
            width: 400,
            height: 400,
            frameCount: 50,
            chunk: { count: 2, rows: 5, columns: 5 },
            getChunkPath:
              ((J = "R.images.gui.maps.icons.sequence.sun_shine_big_sprite.sprite_"),
              (e) => `${J}${e}`),
          };
        var J;
        const Q = (function (e) {
          const t = e.chunk,
            a = t.rows * t.columns;
          return (_) => {
            const u = _ % a,
              r = (u % t.columns) * e.width,
              n = Math.trunc(u / t.columns) * e.height;
            return { path: e.getChunkPath(Math.trunc(_ / a)), x: r, y: n };
          };
        })(K);
        let ee;
        !(function (e) {
          ((e.Medium = "medium"), (e.SMedium = "smedium"), (e.ExtraSmall = "extraSmall"));
        })(ee || (ee = {}));
        const te = ({ className: e, isAnimated: t, isWidget: a, size: _ }) => {
          const r = u()(e, X.base, { [X.animation]: t, [X.widget]: a, [X[`widget__${_}`]]: a });
          return o().createElement(
            "div",
            { className: r },
            Z.O.client.graphicsQuality.isHigh()
              ? o().createElement(
                  o().Fragment,
                  null,
                  o().createElement(U, {
                    onAnimationDone: Y.ZT,
                    width: K.width,
                    height: K.height,
                    frameCount: K.frameCount,
                    getImageSource: Q,
                    frameTime: 50,
                    className: X.sunShineCanvas,
                  }),
                  o().createElement("div", { className: X.rays }),
                )
              : o().createElement("div", { className: X.staticHighlight }),
          );
        };
        var ae = a(6373);
        const _e = {
          base: "RankedStatBattles_base_f2",
          icon: "RankedStatBattles_icon_c5",
          icon__medium: "RankedStatBattles_icon__medium_f7",
          value: "RankedStatBattles_value_1d",
          value__medium: "RankedStatBattles_value__medium_34",
        };
        let ue;
        !(function (e) {
          ((e.Medium = "medium"), (e.SMedium = "smedium"));
        })(ue || (ue = {}));
        const re = (0, i.memo)(({ value: e, isUnavailable: t = !1, size: a = ue.Medium }) => {
            const _ = ((e) => (t ? "---" : m.Z5.getRealFormat(e, m.Gr.WO_ZERO_DIGITS)))(e),
              r = R.strings.tooltips.rankedBattleView.stats.totalBattles;
            return o().createElement(
              ae.i,
              { header: r.$dyn("header"), body: r.$dyn("body") },
              o().createElement(
                "div",
                { className: u()(_e.base, _e[`base__${a}`]) },
                o().createElement("div", { className: u()(_e.icon, _e[`icon__${a}`]) }),
                o().createElement("div", { className: u()(_e.value, _e[`value__${a}`]) }, _),
              ),
            );
          }),
          ne = {
            base: "League_base_18",
            base__extraSmall: "League_base__extraSmall_c7",
            base__smedium: "League_base__smedium_5e",
            base__medium: "League_base__medium_15",
            base__b2: "League_base__b2_c9",
            wrapper: "League_wrapper_91",
            icon: "League_icon_dd",
            base__small: "League_base__small_30",
          },
          ie = { [h.Medium]: "100x100", [h.SMedium]: "70x70", [h.ExtraSmall]: "70x70" },
          oe = { tooltipId: c._Y },
          se = (0, i.memo)((e) => {
            const t = e.leagueID,
              a = e.efficiency,
              _ = e.efficiencyDiff,
              r = e.isEfficiencyUnavailable,
              n = void 0 !== r && r,
              c = e.isBattlesUnavailable,
              m = void 0 !== c && c,
              d = e.size,
              b = e.battlesTotal,
              g = e.cardSize,
              E = ![B.Small, B.ExtraSmall].includes(d),
              p = ![B.Small, B.ExtraSmall].includes(d),
              A = (0, i.useMemo)(
                () =>
                  [B.Small, B.ExtraSmall].includes(d)
                    ? h.ExtraSmall
                    : B.SMedium === d
                      ? h.SMedium
                      : h.Medium,
                [d],
              ),
              C = (0, i.useMemo)(() => (d === B.SMedium ? M.SMedium : M.Medium), [d]),
              F = (0, i.useMemo)(
                () =>
                  [B.Small, B.ExtraSmall].includes(d)
                    ? ee.ExtraSmall
                    : d === B.SMedium
                      ? ee.SMedium
                      : ee.Medium,
                [d],
              ),
              D = (0, i.useMemo)(() => {
                const e = R.images.gui.maps.icons.rankedBattles.league,
                  a = ie[A],
                  _ = e.$dyn(`c_${a}`);
                if (_) {
                  return { backgroundImage: `url(${_.$num(t)})` };
                }
              }, [t, A]);
            return o().createElement(
              "div",
              {
                className: u()(
                  ne.base,
                  ne[`base__${B.SMedium === d && g === s.Id.B2 ? s.Id.B2 : d}`],
                ),
              },
              E &&
                o().createElement(I, {
                  type: L.Efficiency,
                  value: a,
                  valueDiff: _,
                  isUnavailable: n,
                  isPercent: !0,
                  size: C,
                }),
              o().createElement(
                l.t,
                { args: oe },
                o().createElement(
                  "div",
                  { className: ne.wrapper },
                  o().createElement("div", { className: ne.icon, style: D }),
                  p && o().createElement(te, { isAnimated: !0, isWidget: !0, size: F }),
                ),
              ),
              E && o().createElement(re, { value: b, isUnavailable: m, size: C }),
            );
          }),
          le = {
            base: "RankedWidget_base_9c",
            ranks: "RankedWidget_ranks_a7",
            ranks__b0: "RankedWidget_ranks__b0_7d",
            ranks__b1: "RankedWidget_ranks__b1_fc",
            ranks__b0__medium: "RankedWidget_ranks__b0__medium_db",
            ranks__b1__medium: "RankedWidget_ranks__b1__medium_57",
            ranks__b0__extraSmall: "RankedWidget_ranks__b0__extraSmall_a9",
            ranks__b0__small: "RankedWidget_ranks__b0__small_45",
            ranks__b1__extraSmall: "RankedWidget_ranks__b1__extraSmall_1e",
            ranks__b1__small: "RankedWidget_ranks__b1__small_6c",
            ranks__b2: "RankedWidget_ranks__b2_f5",
            ranks__b2__medium: "RankedWidget_ranks__b2__medium_7e",
            ranks__b2__extraSmall: "RankedWidget_ranks__b2__extraSmall_ff",
            ranks__b2__small: "RankedWidget_ranks__b2__small_8d",
            ranks__b3: "RankedWidget_ranks__b3_77",
            ranks__b3__medium: "RankedWidget_ranks__b3__medium_29",
            ranks__b3__extraSmall: "RankedWidget_ranks__b3__extraSmall_fb",
            ranks__b3__small: "RankedWidget_ranks__b3__small_cb",
            ranks__b4: "RankedWidget_ranks__b4_80",
            ranks__b4__medium: "RankedWidget_ranks__b4__medium_ff",
            ranks__b4__extraSmall: "RankedWidget_ranks__b4__extraSmall_f2",
            ranks__b4__small: "RankedWidget_ranks__b4__small_38",
            bonus: "RankedWidget_bonus_35",
            bonus__b0: "RankedWidget_bonus__b0_8d",
            bonus__b1: "RankedWidget_bonus__b1_3d",
            bonus__b0__medium: "RankedWidget_bonus__b0__medium_68",
            bonus__b1__medium: "RankedWidget_bonus__b1__medium_80",
            bonus__b0__extraSmall: "RankedWidget_bonus__b0__extraSmall_78",
            bonus__b0__small: "RankedWidget_bonus__b0__small_bc",
            bonus__b1__extraSmall: "RankedWidget_bonus__b1__extraSmall_f0",
            bonus__b1__small: "RankedWidget_bonus__b1__small_d2",
            bonus__b2: "RankedWidget_bonus__b2_42",
            bonus__b2__medium: "RankedWidget_bonus__b2__medium_ee",
            bonus__b2__extraSmall: "RankedWidget_bonus__b2__extraSmall_63",
            bonus__b2__small: "RankedWidget_bonus__b2__small_cb",
            bonus__b3: "RankedWidget_bonus__b3_83",
            bonus__b3__medium: "RankedWidget_bonus__b3__medium_13",
            bonus__b3__extraSmall: "RankedWidget_bonus__b3__extraSmall_03",
            bonus__b3__small: "RankedWidget_bonus__b3__small_76",
            bonus__b5__extraSmall: "RankedWidget_bonus__b5__extraSmall_c8",
            bonus__b5__small: "RankedWidget_bonus__b5__small_c0",
            bonus__b6__extraSmall: "RankedWidget_bonus__b6__extraSmall_b1",
            bonus__b6__small: "RankedWidget_bonus__b6__small_08",
          },
          ce = ({
            size: e,
            rankLeft: t,
            rankRight: a,
            hasLeftRank: _,
            steps: l,
            stepsTotal: c,
            leagueID: m,
            efficiency: d,
            efficiencyDiff: b,
            isEfficiencyUnavailable: g,
            battlesTotal: E,
            bonusBattles: p,
            maxRank: A,
          }) => {
            const C = (0, i.useContext)(r.YN),
              h = C.extraSmall,
              D = C.small,
              f = C.medium,
              v = C.large,
              x = C.extraLarge,
              S = ![s.Id.B5, s.Id.B6].includes(e),
              w = m > -1,
              k = p > 0,
              N = (0, n.Z)((0, s.Hp)("qualBattles", "ranks", "ranks__qual", "bonus"), le),
              y = (0, i.useMemo)(
                () =>
                  D || h
                    ? B.ExtraSmall
                    : f
                      ? e === s.Id.B1
                        ? B.Medium
                        : B.SMedium
                      : (v || x) && e === s.Id.B3
                        ? B.SMedium
                        : B.Medium,
                [e, h, D, f, v, x],
              ),
              L = u()(le.ranks, N[`ranks__${e}`]);
            return o().createElement(
              "div",
              { className: le.base },
              S &&
                o().createElement(
                  "div",
                  { className: L },
                  w
                    ? o().createElement(se, {
                        leagueID: m,
                        efficiency: d,
                        efficiencyDiff: b,
                        isEfficiencyUnavailable: g,
                        isBattlesUnavailable: !w,
                        battlesTotal: E,
                        size: y,
                        cardSize: e,
                      })
                    : o().createElement(T, {
                        rankLeft: _ ? t : void 0,
                        rankRight: a,
                        steps: l,
                        stepsTotal: c,
                        size: y,
                        cardSize: e,
                        maxRank: A,
                      }),
                ),
              k &&
                o().createElement(
                  "div",
                  { className: u()(le.bonus, N[`bonus__${e}`]) },
                  o().createElement(F, { amount: p }),
                ),
            );
          };
      },
      5060: (e, t, a) => {
        "use strict";
        a.d(t, { b: () => g });
        var _ = a(6483),
          u = a.n(_),
          r = a(2056),
          n = a(5415),
          i = a(6179),
          o = a.n(i),
          s = a(3486);
        const l = {
            [s.Id.B1]: "136x136",
            [s.Id.B2]: "136x136",
            [s.Id.B3]: "136x136",
            [s.Id.B4]: "72x72",
          },
          c = {
            [s.Id.B1]: "136x136",
            [s.Id.B2]: "136x136",
            [s.Id.B3]: "72x72",
            [s.Id.B4]: "72x72",
          },
          m = { [s.Id.B1]: "72x72", [s.Id.B2]: "72x72", [s.Id.B3]: "72x72", [s.Id.B4]: "64x64" },
          d = {
            base: "StrongholdWidget_base_6e",
            inactive: "StrongholdWidget_inactive_a4",
            base__b1: "StrongholdWidget_base__b1_0b",
            base__b2: "StrongholdWidget_base__b2_0b",
            base__b3: "StrongholdWidget_base__b3_49",
            base__b4: "StrongholdWidget_base__b4_f0",
            mediumScreen: "StrongholdWidget_mediumScreen_7b",
            smallScreen: "StrongholdWidget_smallScreen_4b",
          },
          b = R.images.gui.maps.icons.stronghold.ranks,
          g = ({ currentStage: e, isInClan: t, isActive: a, size: _ }) => {
            const g = (0, n.GS)().mediaSize,
              E = ![s.Id.B5, s.Id.B6].includes(_),
              p = g === n.cJ.Medium,
              A = g === n.cJ.Small || g === n.cJ.ExtraSmall,
              C = u()(d.base, d[`base__${_}`], {
                [d.mediumScreen]: p,
                [d.smallScreen]: A,
                [d.inactive]: !t || !a,
              }),
              F = (0, i.useMemo)(() => {
                if (!E) return {};
                let t = l;
                (A && (t = m), p && (t = c));
                const a = t[_] || t[s.Id.B1],
                  u = b.$dyn(`c_${a}`);
                if (!u) return {};
                const r = u.$dyn(`rank_${e}`);
                return r ? { backgroundImage: `url(${r})` } : {};
              }, [p, A, e, _, E]);
            return o().createElement(
              "div",
              null,
              E &&
                o().createElement(
                  r.u,
                  {
                    contentId:
                      R.views.lobby.stronghold.tooltips.StrongholdMainWidgetTooltip("resId"),
                  },
                  o().createElement(
                    "div",
                    { className: C },
                    o().createElement("div", { style: F }),
                  ),
                ),
            );
          };
      },
      8184: (e, t, a) => {
        "use strict";
        a.d(t, { B: () => Z });
        var _ = a(6179),
          u = a.n(_),
          r = a(6483),
          n = a.n(r),
          i = a(7590),
          o = a(156),
          s = a(2056),
          l = a(3415),
          c = a(8045);
        const m = "ExtendedText_base_71",
          d = "ExtendedText_base__zeroPadding_25",
          b = "ExtendedText_base__isTruncationAvailable_5b",
          g = "ExtendedText_truncated_97",
          E = "ExtendedText_truncated__hide_31",
          p = "ExtendedText_unTruncated_b8";
        var A = a(3649);
        let C, F, B;
        (!(function (e) {
          ((e[(e.Word = 0)] = "Word"),
            (e[(e.LineBreak = 1)] = "LineBreak"),
            (e[(e.NewLine = 2)] = "NewLine"),
            (e[(e.NoBreakSymbol = 3)] = "NoBreakSymbol"),
            (e[(e.NoBreakWrapper = 4)] = "NoBreakWrapper"),
            (e[(e.Binding = 5)] = "Binding"));
        })(C || (C = {})),
          (function (e) {
            ((e.FlexStart = "flex-start"), (e.Center = "center"), (e.FlexEnd = "flex-end"));
          })(F || (F = {})),
          (function (e) {
            ((e.NBSP = " "), (e.ZWNBSP = "\ufeff"), (e.NEW_LINE = "\n"));
          })(B || (B = {})));
        const h = {
            [B.NBSP]: C.NoBreakSymbol,
            [B.ZWNBSP]: C.NoBreakSymbol,
            [B.NEW_LINE]: C.LineBreak,
          },
          D = {
            blackReal: "colors_blackReal_fc",
            whiteReal: "colors_whiteReal_31",
            white: "colors_white_45",
            whiteOrange: "colors_whiteOrange_81",
            whiteSpanish: "colors_whiteSpanish_c3",
            par: "colors_par_5b",
            parSecondary: "colors_parSecondary_fd",
            parTertiary: "colors_parTertiary_97",
            red: "colors_red_79",
            redDark: "colors_redDark_73",
            yellow: "colors_yellow_76",
            orange: "colors_orange_cd",
            cream: "colors_cream_0f",
            brown: "colors_brown_82",
            greenBright: "colors_greenBright_68",
            green: "colors_green_fa",
            greenDark: "colors_greenDark_a9",
            blueBooster: "colors_blueBooster_26",
            blueTeamkiller: "colors_blueTeamkiller_86",
            cred: "colors_cred_35",
            gold: "colors_gold_c3",
            bond: "colors_bond_ce",
            prom: "colors_prom_83",
          },
          f = "renderers_noBreakWrapper_10",
          v = "renderers_lineBreak_b5",
          x = "renderers_newLine_bd",
          S = (e) => ({ color: `#${e}` }),
          w = ({ elementList: e, textBlock: t, key: a }) => {
            const _ = t.colorTag;
            return _
              ? D[_]
                ? u().createElement(
                    "span",
                    { key: a, "data-block-type": t.blockType, className: D[_] },
                    e,
                  )
                : u().createElement(
                    "span",
                    { key: a, "data-block-type": t.blockType, style: S(_) },
                    e,
                  )
              : u().createElement("span", { key: a, "data-block-type": t.blockType }, e);
          },
          k = {
            [C.Word]: w,
            [C.NoBreakSymbol]: w,
            [C.Binding]: ({ elementList: e, textBlock: t, key: a }) =>
              u().createElement(
                "span",
                { key: a, "data-block-type": t.blockType },
                e.map((e) => u().createElement(u().Fragment, { key: a }, e)),
              ),
            [C.LineBreak]: ({ key: e }) =>
              u().createElement("span", { key: e, "data-block-type": C.LineBreak, className: v }),
            [C.NewLine]: ({ elementList: e, key: t }) =>
              u().createElement("span", { key: t, "data-block-type": C.NewLine, className: x }, e),
            [C.NoBreakWrapper]: ({ elementList: e, key: t }) =>
              u().createElement(
                "span",
                { key: t, "data-block-type": C.NoBreakWrapper, className: f },
                e,
              ),
          },
          N = (e, t, a) => {
            const _ = [];
            return (
              e.childList.forEach((u, r) => {
                const n = `${a}_${r}`;
                if (((e) => void 0 !== e.childList)(u)) {
                  const e = u,
                    t = e.blockType,
                    a = N(e, k[t], n);
                  _.push(...a);
                } else _.push(t({ elementList: [u], textBlock: e, key: n }));
              }),
              _
            );
          },
          T = (e) => {
            const t = [];
            return (
              e.forEach((e, a) => {
                t.push(
                  ...((e, t) => {
                    const a = [],
                      _ = e.blockType,
                      u = k[_],
                      r = N(e, u, t);
                    return (
                      _ === C.NoBreakWrapper
                        ? a.push(u({ elementList: r, textBlock: e, key: `${t}` }))
                        : a.push(...r),
                      a
                    );
                  })(e, a),
                );
              }),
              t
            );
          },
          y = (e, t, a, _) => {
            let u = t.exec(e),
              r = 0;
            for (; u;)
              (r !== u.index && a(e.slice(r, u.index)), _(u), (r = t.lastIndex), (u = t.exec(e)));
            r !== e.length && a(e.slice(r));
          },
          L = (e) => {
            const t = /[\s\u002d]/g;
            let a = t.exec(e);
            if (!a) return [e];
            const _ = [];
            let u = 0;
            for (; a;) (_.push(e.slice(u, t.lastIndex)), (u = t.lastIndex), (a = t.exec(e)));
            return (u !== e.length && _.push(e.slice(u)), _);
          },
          M = (e, t = "") => {
            const a = [];
            return (
              y(
                e,
                /(\n+|[\xa0\ufeff]+)/g,
                (e) => {
                  a.push({ blockType: C.Word, colorTag: t, childList: L(e) });
                },
                (e) => {
                  const _ = e[0],
                    u = h[_.charAt(0)];
                  u === C.LineBreak
                    ? a.push(
                        ...((e) => {
                          const t = [
                            { blockType: C.LineBreak, colorTag: "", childList: [e.charAt(0)] },
                          ];
                          for (let a = 0; a < e.length - 1; a++)
                            t.push({
                              blockType: C.NewLine,
                              colorTag: "",
                              childList: [e.charAt(0)],
                            });
                          return t;
                        })(_),
                      )
                    : a.push({ blockType: u, colorTag: t, childList: [_] });
                },
              ),
              a
            );
          },
          W = (e, t, a = "") => {
            const _ = [];
            return (
              y(
                e,
                /(?:%\(|{)(.*?)[)}][sd]?/g,
                (e) => {
                  _.push(...M(e, a));
                },
                (e) => {
                  const u = e[1],
                    r = void 0 === t[u] ? e[0] : t[u];
                  "string" == typeof r || "number" == typeof r
                    ? _.push(...M(String(r), a))
                    : _.push({ blockType: C.Binding, colorTag: a, childList: [r] });
                },
              ),
              _
            );
          },
          I = (e, t) => {
            if (!e) return [t];
            const a = [],
              _ = Object.assign({}, t, { childList: t.childList.splice(0, 1) });
            if (e.blockType === C.NoBreakWrapper) (e.childList.push(_), a.push(e));
            else {
              const t = Object.assign({}, e, { childList: e.childList.splice(-1) });
              (e.childList.length > 0 && a.push(e),
                a.push({ blockType: C.NoBreakWrapper, colorTag: "", childList: [t, _] }));
            }
            return (t.childList.length > 0 && a.push(t), a);
          },
          P = (e, t = {}) => {
            if (!e) return [];
            const a = ((e) => {
              const t = [];
              let a = !1;
              return (
                e.forEach((e) => {
                  e.blockType === C.NoBreakSymbol
                    ? ((a = !0), t.push(...I(t.pop(), e)))
                    : (a ? t.push(...I(t.pop(), e)) : t.push(e), (a = !1));
                }),
                t
              );
            })(
              ((e, t) => {
                const a = [];
                return (
                  y(
                    e,
                    /(?:%\(|{)(\w*)(?:_[Oo]pen|_Start)(?:\)s|})([\s\S]*?)(?:%\(|{)\w*(?:_[Cc]lose|_End)(?:\)s|})/g,
                    (e) => {
                      a.push(...W(e, t));
                    },
                    (e) => {
                      a.push(...W(e[2], t, e[1]));
                    },
                  ),
                  a
                );
              })((0, A.Eg)((0, A.z4)(e)), t),
            );
            return T(a);
          },
          O = (e, t) => !e || e.offsetTop + e.offsetHeight > t,
          H = (e, t) => e.offsetLeft + e.offsetWidth - t,
          $ = (e, t, a) => {
            if (!e || !e.textContent) return [!1, 0];
            if (e.offsetLeft > t) return [!1, 0];
            const _ = H(e, t),
              u = e.textContent.length,
              r = e.offsetWidth / u,
              n = Math.ceil(_ / r);
            if (_ > 0) {
              const _ = Math.floor((t - e.offsetLeft) / r);
              return _ >= a ? [!0, a + n] : [!1, _];
            }
            const i = Math.max(a + n, 0);
            return u < i ? [!1, 0] : [!0, i];
          },
          z = (e, t, a, _, r, n) => {
            let i = -1,
              o = null;
            for (let s = a; s >= 0; s--) {
              const a = e[s],
                l = Number(e[s].getAttribute("data-block-type"));
              if (l === C.LineBreak || l === C.NewLine || l === C.Binding) continue;
              const c = a.textContent || "";
              if (!(a.childElementCount > 1)) {
                const e = $(a, _, r),
                  l = e[0],
                  m = e[1];
                if (!l) {
                  m > 0 && (r -= m);
                  continue;
                }
                const d = c.slice(0, c.length - m) + n,
                  b = t[s];
                ((o = u().cloneElement(b, b.props, d)), (i = s));
                break;
              }
              {
                const e = a.children,
                  l = t[s],
                  m = l.props.children,
                  d = z(e, m, e.length - 1, _, r, n),
                  b = d[0],
                  g = d[1];
                if (!(b < 0)) {
                  const e = m.slice(0, b);
                  ((o = u().cloneElement(l, l.props, e, g)), (i = s));
                  break;
                }
                r -= c.length;
              }
            }
            return [i, o];
          },
          G = (e, t, a, _ = "...") => {
            const u = [...t],
              r = e.current;
            if (!r) return [u, !1];
            const n = a.height,
              i = a.width,
              o = r.lastElementChild;
            if (!O(o, n) && H(o, i) <= 0) return [u, !1];
            const s = r.children,
              l = ((e, t) => {
                let a = 0,
                  _ = e.length - 1;
                for (; _ - a >= 0;) {
                  const u = a + Math.ceil(0.5 * (_ - a));
                  O(e[u], t) ? (_ = u - 1) : (a = u + 1);
                }
                return a - 1;
              })(s, n);
            if (l < 0) return [u, !1];
            const c = z(s, u, l, i, _.length, _),
              m = c[0],
              d = c[1];
            return (d && (u.splice(m, 1, d), u.splice(m + 1)), [u, !0]);
          },
          U = u().memo(
            ({
              text: e,
              classMix: t,
              onSizeChanged: a,
              binding: r,
              isTooltipEnable: i = !1,
              isTruncationAvailable: o = !1,
              targetId: s,
              justifyContent: A = F.FlexStart,
              alignContent: C = F.FlexStart,
              truncateIdentify: B = "...",
            }) => {
              const h = (0, _.useRef)(null),
                D = (0, _.useRef)({ height: 0, width: 0 }),
                f = (0, _.useState)({ elementList: [], isTruncated: !1, isTruncateFinished: !1 }),
                v = f[0],
                x = f[1],
                S = (0, _.useMemo)(() => P(e, r), [r, e]),
                w = (0, _.useMemo)(() => {
                  if (i && v.isTruncated)
                    return {
                      args: { text: e, stringifyKwargs: r ? JSON.stringify(r) : "" },
                      contentId: R.views.lobby.common.tooltips.ExtendedTextTooltip("resId"),
                      targetId: s,
                    };
                }, [r, i, s, e, v.isTruncated]),
                k = (0, _.useCallback)(
                  (e) => {
                    ((D.current.width = e.contentRect.width),
                      (D.current.height = e.contentRect.height));
                    const t = G(h, S, D.current, B),
                      _ = t[0],
                      u = t[1];
                    (x({ elementList: _, isTruncated: u, isTruncateFinished: !0 }), a && a(u));
                  },
                  [a, B, S],
                ),
                N = (0, _.useMemo)(() => ({ justifyContent: A, alignContent: C }), [C, A]);
              return (
                ((e, t, a = !0) => {
                  const u = (0, _.useCallback)(
                    (e) => {
                      const a = e[0];
                      t && t(a);
                    },
                    [t],
                  );
                  (0, _.useEffect)(() => {
                    if (!e.current || !a) return;
                    const t = new c.Z((e) => u(e));
                    return (
                      t.observe(e.current),
                      () => {
                        t.disconnect();
                      }
                    );
                  }, [u, a, e]);
                })(h, k, o),
                u().createElement(
                  "div",
                  { className: n()(m, t, d, o && b), style: N },
                  u().createElement("div", { className: p, ref: h }, S),
                  u().createElement(
                    l.l,
                    { tooltipArgs: w },
                    u().createElement(
                      "div",
                      { className: n()(g, !v.isTruncateFinished && o && E), style: N },
                      v.isTruncateFinished && o ? v.elementList : S,
                    ),
                  ),
                )
              );
            },
          );
        var j = a(4322),
          V = a(3486);
        const q = {
            base: "WTWidget_base_4b",
            base__b1: "WTWidget_base__b1_78",
            base__b2: "WTWidget_base__b2_9b",
            base__b3: "WTWidget_base__b3_48",
            emblem: "WTWidget_emblem_4b",
            base__b4: "WTWidget_base__b4_c9",
            emblem__full: "WTWidget_emblem__full_8a",
            checkmark: "WTWidget_checkmark_31",
            checkmark__visible: "WTWidget_checkmark__visible_3f",
            progress: "WTWidget_progress_f2",
            collection: "WTWidget_collection_9a",
            tickets: "WTWidget_tickets_8d",
            ticketCount: "WTWidget_ticketCount_9f",
            progressionWrapper: "WTWidget_progressionWrapper_2b",
          },
          Z = (0, _.memo)(({ totalCount: e, currentProgress: t, ticketCount: a, size: _ }) => {
            const r = _ === V.Id.B1 || _ === V.Id.B2 || _ === V.Id.B3,
              l = t && e ? (100 * t) / e : 0,
              c = n()(q.base, q[`base__${_}`]),
              m = n()(q.emblem, t === e && q.emblem__full),
              d = n()(q.checkmark, t === e && q.checkmark__visible);
            return u().createElement(
              "div",
              { className: c },
              u().createElement(
                s.u,
                {
                  contentId:
                    R.views.white_tiger.lobby.tooltips.ProgressionEntryPointTooltip("resId"),
                },
                u().createElement(
                  "div",
                  { className: m },
                  u().createElement("div", { className: d }),
                ),
              ),
              r &&
                u().createElement(
                  u().Fragment,
                  null,
                  u().createElement(
                    "div",
                    { className: q.tickets },
                    u().createElement(j.ZP, { text: R.strings.mode_selector.event.wt.tickets() }),
                    u().createElement(
                      s.u,
                      { contentId: R.views.white_tiger.lobby.tooltips.TicketTooltipView("resId") },
                      u().createElement(j.ZP, { className: q.ticketCount, text: String(a) }),
                    ),
                  ),
                  u().createElement(
                    "div",
                    { className: q.progress },
                    u().createElement(
                      "div",
                      { className: q.progressionWrapper },
                      u().createElement(U, {
                        classMix: q.collection,
                        text: R.strings.mode_selector.event.wt.collection(),
                        binding: { current: t, total: e },
                        justifyContent: F.Center,
                      }),
                    ),
                    u().createElement(i.ko, { size: i.$u.Small, value: l, theme: o.Yy }),
                  ),
                ),
            );
          });
      },
      2646: (e, t, a) => {
        "use strict";
        a.d(t, {
          $b: () => d,
          D3: () => u,
          GN: () => s,
          I3: () => m,
          MS: () => n,
          T3: () => i,
          TR: () => c,
          U4: () => g,
          _Y: () => o,
          hg: () => b,
          p5: () => _,
          u6: () => r,
          zD: () => l,
        });
        const _ = "disabledTooltip",
          u = "rankedCalendarDayInfoExtended",
          r = "rankedStep",
          n = "rankedBattlesRank",
          i = "rankedBattlesBonus",
          o = "rankedBattlesLeague",
          s = "calendarTooltip",
          l = "mapboxCalendar",
          c = "epicBattleCalendarTooltip",
          m = "epicBattleWidgetInfo",
          d = "funRandomModeSelectorCalendarDay",
          b = "comp7CalendarDayExtendedInfo",
          g = "eventBattlesCalendar";
      },
      5287: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => _ });
        const _ = { base: "FormatText_base_d0" };
      },
      8487: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => _ });
        const _ = {
          blackReal: "FormatTextWithColorTags_blackReal_d5",
          whiteReal: "FormatTextWithColorTags_whiteReal_d8",
          white: "FormatTextWithColorTags_white_b9",
          whiteOrange: "FormatTextWithColorTags_whiteOrange_ea",
          whiteSpanish: "FormatTextWithColorTags_whiteSpanish_54",
          par: "FormatTextWithColorTags_par_c1",
          parSecondary: "FormatTextWithColorTags_parSecondary_4e",
          parTertiary: "FormatTextWithColorTags_parTertiary_14",
          red: "FormatTextWithColorTags_red_d9",
          redDark: "FormatTextWithColorTags_redDark_ea",
          yellow: "FormatTextWithColorTags_yellow_48",
          orange: "FormatTextWithColorTags_orange_ad",
          cream: "FormatTextWithColorTags_cream_96",
          brown: "FormatTextWithColorTags_brown_27",
          greenBright: "FormatTextWithColorTags_greenBright_04",
          green: "FormatTextWithColorTags_green_58",
          greenDark: "FormatTextWithColorTags_greenDark_af",
          blueBooster: "FormatTextWithColorTags_blueBooster_b3",
          blueTeamkiller: "FormatTextWithColorTags_blueTeamkiller_ab",
          cred: "FormatTextWithColorTags_cred_d3",
          gold: "FormatTextWithColorTags_gold_28",
          bond: "FormatTextWithColorTags_bond_74",
          prom: "FormatTextWithColorTags_prom_58",
        };
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
    (__webpack_require__.O = (e, t, a, _) => {
      if (!t) {
        var u = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [t, a, _] = deferred[o], r = !0, n = 0; n < t.length; n++)
            (!1 & _ || u >= _) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[n]))
              ? t.splice(n--, 1)
              : ((r = !1), _ < u && (u = _));
          if (r) {
            deferred.splice(o--, 1);
            var i = a();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      _ = _ || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > _; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [t, a, _];
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
    (__webpack_require__.j = 261),
    (() => {
      var e = { 261: 0, 588: 0, 13: 0, 153: 0, 819: 0, 930: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var _,
            u,
            [r, n, i] = a,
            o = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (_ in n) __webpack_require__.o(n, _) && (__webpack_require__.m[_] = n[_]);
            if (i) var s = i(__webpack_require__);
          }
          for (t && t(a); o < r.length; o++)
            ((u = r[o]), __webpack_require__.o(e, u) && e[u] && e[u][0](), (e[u] = 0));
          return __webpack_require__.O(s);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [705], () => __webpack_require__(3129));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
