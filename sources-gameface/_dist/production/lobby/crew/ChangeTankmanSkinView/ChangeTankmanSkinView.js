(() => {
  var __webpack_modules__ = {
      3779: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => F });
        var n = t(6483),
          r = t.n(n),
          a = t(9887),
          o = t.n(a),
          s = t(3377),
          i = t(6179),
          l = t.n(i),
          c = t(5026);
        const d = [
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
        function E() {
          return (
            (E =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            E.apply(this, arguments)
          );
        }
        Object.keys(o());
        const m = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          _ = (Object.keys(m), ["mt", "mr", "mb", "ml"]),
          A = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          F = (0, s.ZP)((e) => {
            let u = e.className,
              t = e.width,
              n = e.height,
              a = e.m,
              o = e.mt,
              s = void 0 === o ? a : o,
              F = e.mr,
              D = void 0 === F ? a : F,
              C = e.mb,
              g = void 0 === C ? a : C,
              p = e.ml,
              B = void 0 === p ? a : p,
              h = e.column,
              f = e.row,
              v = e.flexDirection,
              b = void 0 === v ? (h ? "column" : f && "row") || void 0 : v,
              w = e.flexStart,
              x = e.center,
              S = e.flexEnd,
              y = e.spaceBetween,
              M = e.spaceAround,
              L = e.justifyContent,
              N =
                void 0 === L
                  ? (w ? "flex-start" : x && "center") ||
                    (S && "flex-end") ||
                    (y && "space-between") ||
                    (M && "space-around") ||
                    void 0
                  : L,
              T = e.alignItems,
              R =
                void 0 === T
                  ? (w ? "flex-start" : x && "center") || (S && "flex-end") || void 0
                  : T,
              k = e.alignSelf,
              O = e.wrap,
              P = e.flexWrap,
              I = void 0 === P ? (O ? "wrap" : void 0) : P,
              H = e.grow,
              W = e.shrink,
              G = e.flex,
              j = void 0 === G ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : G,
              Z = e.style,
              U = e.children,
              z = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, d);
            const V = (0, i.useMemo)(() => {
                const e = { mt: s, mr: D, mb: g, ml: B },
                  u = ((e) =>
                    _.reduce((u, t) => {
                      const n = e[t];
                      return n && "number" != typeof n ? u.concat(m[!0 === n ? "MD" : n][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    _.reduce((u, t) => {
                      const n = e[t];
                      return ("number" == typeof n && (u[A[t]] = n + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, Z, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: j,
                    alignSelf: k,
                    display: b || R ? "flex" : void 0,
                    flexDirection: b,
                    flexWrap: I,
                    justifyContent: N,
                    alignItems: R,
                  }),
                  computedClassNames: u,
                };
              }, [t, n, s, D, g, B, Z, j, k, b, I, N, R]),
              $ = V.computedStyle,
              X = V.computedClassNames;
            return l().createElement(
              "div",
              E({ className: r()(c.Z.base, ...X, u), style: $ }, z),
              U,
            );
          });
      },
      3457: (e, u, t) => {
        "use strict";
        t.d(u, { L$: () => l.L, qE: () => l.q, u5: () => d });
        var n = t(6483),
          r = t.n(n),
          a = t(7727),
          o = t(6179),
          s = t.n(o),
          i = t(6880),
          l = t(2106);
        const c = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: c,
          mixClass: d,
          soundHover: E,
          soundClick: m,
          onMouseEnter: _,
          onMouseMove: A,
          onMouseDown: F,
          onMouseUp: D,
          onMouseLeave: C,
          onClick: g,
        }) => {
          const p = (0, o.useRef)(null),
            B = (0, o.useState)(t),
            h = B[0],
            f = B[1],
            v = (0, o.useState)(!1),
            b = v[0],
            w = v[1],
            x = (0, o.useState)(!1),
            S = x[0],
            y = x[1],
            M = (0, o.useCallback)(() => {
              c || (p.current && (p.current.focus(), f(!0)));
            }, [c]),
            L = (0, o.useCallback)(
              (e) => {
                h && null !== p.current && !p.current.contains(e.target) && f(!1);
              },
              [h],
            ),
            N = (0, o.useCallback)(
              (e) => {
                c || (g && g(e));
              },
              [c, g],
            ),
            T = (0, o.useCallback)(
              (e) => {
                c || (null !== E && (0, a.G)(E), _ && _(e), y(!0));
              },
              [c, E, _],
            ),
            k = (0, o.useCallback)(
              (e) => {
                A && A(e);
              },
              [A],
            ),
            O = (0, o.useCallback)(
              (e) => {
                c || (D && D(e), w(!1));
              },
              [c, D],
            ),
            P = (0, o.useCallback)(
              (e) => {
                c || (null !== m && (0, a.G)(m), F && F(e), t && M(), w(!0));
              },
              [c, m, F, M, t],
            ),
            I = (0, o.useCallback)(
              (e) => {
                c || (C && C(e), w(!1));
              },
              [c, C],
            ),
            H = r()(
              i.Z.base,
              i.Z[`base__${n}`],
              {
                [i.Z.base__disabled]: c,
                [i.Z[`base__${u}`]]: u,
                [i.Z.base__focus]: h,
                [i.Z.base__highlightActive]: b,
                [i.Z.base__firstHover]: S,
              },
              d,
            ),
            W = r()(i.Z.state, i.Z.state__default);
          return (
            (0, o.useEffect)(
              () => (
                document.addEventListener("mousedown", L),
                () => {
                  document.removeEventListener("mousedown", L);
                }
              ),
              [L],
            ),
            (0, o.useEffect)(() => {
              f(t);
            }, [t]),
            s().createElement(
              "div",
              {
                ref: p,
                className: H,
                onMouseEnter: T,
                onMouseMove: k,
                onMouseUp: O,
                onMouseDown: P,
                onMouseLeave: I,
                onClick: N,
              },
              n !== l.L.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: i.Z.back }),
                  s().createElement("span", { className: i.Z.texture }),
                ),
              s().createElement(
                "span",
                { className: W },
                s().createElement("span", { className: i.Z.stateDisabled }),
                s().createElement("span", { className: i.Z.stateHighlightHover }),
                s().createElement("span", { className: i.Z.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: i.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        c.defaultProps = {
          type: l.L.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const d = (0, o.memo)(c);
      },
      2106: (e, u, t) => {
        "use strict";
        let n, r;
        (t.d(u, { L: () => n, q: () => r }),
          (function (e) {
            ((e.main = "main"),
              (e.primary = "primary"),
              (e.primaryGreen = "primaryGreen"),
              (e.primaryRed = "primaryRed"),
              (e.secondary = "secondary"),
              (e.ghost = "ghost"));
          })(n || (n = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(r || (r = {})));
      },
      9987: (e, u, t) => {
        "use strict";
        t.d(u, { A: () => c });
        var n = t(6483),
          r = t.n(n),
          a = t(6179),
          o = t.n(a),
          s = t(8055);
        const i = [
          "size",
          "value",
          "isEmpty",
          "fadeInAnimation",
          "hide",
          "maximumNumber",
          "className",
        ];
        function l() {
          return (
            (l =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            l.apply(this, arguments)
          );
        }
        const c = (e) => {
          let u = e.size,
            t = e.value,
            n = e.isEmpty,
            a = e.fadeInAnimation,
            c = e.hide,
            d = e.maximumNumber,
            E = e.className,
            m = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, i);
          const _ = n ? null : t,
            A = "string" == typeof _;
          if ((_ && !A && _ < 0) || 0 === _) return null;
          const F = _ && !A && _ > d,
            D = r()(
              s.Z.base,
              s.Z[`base__${u}`],
              a && s.Z.base__animated,
              c && s.Z.base__hidden,
              !_ && s.Z.base__pattern,
              n && s.Z.base__empty,
              E,
            );
          return o().createElement(
            "div",
            l({ className: D }, m),
            o().createElement("div", { className: s.Z.bg }),
            o().createElement("div", { className: s.Z.pattern }),
            o().createElement(
              "div",
              { className: r()(s.Z.value, A && s.Z.value__text) },
              F ? d : _,
              F && o().createElement("span", { className: s.Z.plus }, "+"),
            ),
          );
        };
        c.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
      },
      280: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => l });
        var n = t(6179),
          r = t.n(n),
          a = t(6483),
          o = t.n(a),
          s = t(3649),
          i = t(5287);
        const l = ({ binding: e, text: u = "", classMix: t, alignment: a = s.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                n.Fragment,
                null,
                u.split("\n").map((u, l) =>
                  r().createElement(
                    "div",
                    { className: o()(i.Z.base, t), key: `${u}-${l}` },
                    (0, s.Uw)(u, a, e).map((e, u) =>
                      r().createElement(n.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => d });
        var n = t(3138),
          r = t(6179),
          a = t(1043),
          o = t(5262);
        const s = n.O.client.getSize("rem"),
          i = s.width,
          l = s.height,
          c = Object.assign({ width: i, height: l }, (0, o.T)(i, l, a.j)),
          d = (0, r.createContext)(c);
      },
      1039: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => c });
        var n = t(6179),
          r = t.n(n),
          a = t(6536),
          o = t(3495),
          s = t(1043),
          i = t(5262),
          l = t(3138);
        const c = (0, n.memo)(({ children: e }) => {
          const u = (0, n.useContext)(o.Y),
            t = (0, n.useState)(u),
            c = t[0],
            d = t[1],
            E = (0, n.useCallback)((e, u) => {
              const t = l.O.view.pxToRem(e),
                n = l.O.view.pxToRem(u);
              d(Object.assign({ width: t, height: n }, (0, i.T)(t, n, s.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", E);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", E), [E]));
          const m = (0, n.useMemo)(() => Object.assign({}, c), [c]);
          return r().createElement(o.Y.Provider, { value: m }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var n = t(6179),
          r = t(7382),
          a = t(3495);
        const o = ["children"];
        const s = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, o);
          const s = (0, n.useContext)(a.Y),
            i = s.extraLarge,
            l = s.large,
            c = s.medium,
            d = s.small,
            E = s.extraSmall,
            m = s.extraLargeWidth,
            _ = s.largeWidth,
            A = s.mediumWidth,
            F = s.smallWidth,
            D = s.extraSmallWidth,
            C = s.extraLargeHeight,
            g = s.largeHeight,
            p = s.mediumHeight,
            B = s.smallHeight,
            h = s.extraSmallHeight,
            f = { extraLarge: C, large: g, medium: p, small: B, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && i) return u;
            if (t.large && l) return u;
            if (t.medium && c) return u;
            if (t.small && d) return u;
            if (t.extraSmall && E) return u;
          } else {
            if (t.extraLargeWidth && m) return (0, r.H)(u, t, f);
            if (t.largeWidth && _) return (0, r.H)(u, t, f);
            if (t.mediumWidth && A) return (0, r.H)(u, t, f);
            if (t.smallWidth && F) return (0, r.H)(u, t, f);
            if (t.extraSmallWidth && D) return (0, r.H)(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && C) return u;
              if (t.largeHeight && g) return u;
              if (t.mediumHeight && p) return u;
              if (t.smallHeight && B) return u;
              if (t.extraSmallHeight && h) return u;
            }
          }
          return null;
        };
        s.defaultProps = {
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
        (0, n.memo)(s);
      },
      7382: (e, u, t) => {
        "use strict";
        t.d(u, { H: () => n });
        const n = (e, u, t) =>
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
      },
      7739: (e, u, t) => {
        "use strict";
        t.d(u, { YN: () => r.Y, ZN: () => n.Z });
        t(6010);
        var n = t(1039),
          r = t(3495);
      },
      1043: (e, u, t) => {
        "use strict";
        t.d(u, { j: () => n });
        const n = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, u, t) => {
        "use strict";
        var n;
        function r(e, u, t) {
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
            r = (function (e, u) {
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
            a = Math.min(n, r);
          return {
            extraLarge: a === t.extraLarge.weight,
            large: a === t.large.weight,
            medium: a === t.medium.weight,
            small: a === t.small.weight,
            extraSmall: a === t.extraSmall.weight,
            extraLargeWidth: n === t.extraLarge.weight,
            largeWidth: n === t.large.weight,
            mediumWidth: n === t.medium.weight,
            smallWidth: n === t.small.weight,
            extraSmallWidth: n === t.extraSmall.weight,
            extraLargeHeight: r === t.extraLarge.weight,
            largeHeight: r === t.large.weight,
            mediumHeight: r === t.medium.weight,
            smallHeight: r === t.small.weight,
            extraSmallHeight: r === t.extraSmall.weight,
          };
        }
        (t.d(u, { T: () => r }),
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
          })(n || (n = {})));
      },
      1037: (e, u, t) => {
        "use strict";
        t.d(u, { IC: () => n });
        var n,
          r = t(6483),
          a = t.n(r),
          o = t(6373),
          s = t(1856),
          i = t(3138),
          l = t(2039),
          c = t(5099),
          d = t(7727),
          E = t(4179),
          m = t(6179),
          _ = t.n(m),
          A = t(4769);
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(n || (n = {}));
        const F = ["__left", "__right", "__top", "__bottom"];
        (0, m.forwardRef)(
          (
            { children: e, disableAutoSizeUpdate: u, onOutsideClick: t, customStyles: n = {} },
            r,
          ) => {
            const D = (0, m.useRef)(null),
              C = (0, m.useRef)(null),
              g = (0, m.useRef)(null),
              p = (0, m.useState)(window.decorator && window.decorator.directionType),
              B = p[0],
              h = p[1],
              f = (0, m.useCallback)(() => {
                (d.$.playClick(), i.O.view.sendEvent.close());
              }, []),
              v = (0, m.useCallback)(() => {
                d.$.playHighlight();
              }, []),
              b = a()(A.Z.arrow, A.Z[`arrow${F[B]}`]);
            (0, l.b)(
              () => (
                i.O.client.events.mouse.enableOutside(),
                i.O.client.events.mouse.down(([, e]) => {
                  "outside" === e && (t ? t() : i.O.view.sendEvent.close("popover"));
                })
              ),
            );
            const w = (0, m.useCallback)(
                (e) => {
                  let u = e.target;
                  do {
                    if (u === D.current || u === g.current) return;
                    u = u.parentNode;
                  } while (u);
                  const n = window.decorator;
                  if (void 0 !== window.decorator) {
                    const e = i.O.client.getMouseGlobalPosition(),
                      u = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                      t =
                        e.x < n.boundX ||
                        e.x > n.boundX + n.boundWidth ||
                        e.y > n.boundY + n.boundHeight ||
                        e.y < n.boundY;
                    if (u && !t) return;
                  }
                  t ? t() : i.O.view.sendEvent.close("popover");
                },
                [D, g, t],
              ),
              x = (0, m.useCallback)(
                () => (
                  i.O.view.freezeTextureBeforeResize(),
                  (0, s.v)(() => {
                    if (C.current) {
                      const e = C.current.scrollWidth,
                        u = C.current.scrollHeight;
                      (i.O.view.resize(e, u), h(window.decorator.directionType));
                    }
                  })
                ),
                [],
              );
            return (
              (0, m.useImperativeHandle)(r, () => ({ updateSize: x })),
              (0, l.b)(() => {
                i.O.view.setInputPaddingsRem(58);
              }),
              (0, m.useEffect)(() => {
                document.addEventListener("mousedown", w, { capture: !0 });
                const e = (0, c.B)((0, E.Eu)());
                return (
                  !u && e.promise.then(() => x()),
                  () => {
                    (e.cancel(), document.removeEventListener("mousedown", w));
                  }
                );
              }, [x, w, u]),
              _().createElement(
                "div",
                { className: A.Z.base, ref: C },
                _().createElement(
                  "div",
                  { className: A.Z.decorator },
                  _().createElement(
                    "div",
                    { className: A.Z.content, ref: D },
                    e,
                    window.decorator &&
                      window.decorator.isCloseBtnVisible &&
                      _().createElement(
                        o.i,
                        { body: R.strings.dialogs.common.error.cancel() },
                        _().createElement("div", {
                          className: A.Z.closeBtn,
                          onClick: f,
                          onMouseEnter: v,
                          ref: g,
                        }),
                      ),
                  ),
                  _().createElement("div", { className: b, style: n.arrow }),
                ),
              )
            );
          },
        );
      },
      3616: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => l });
        var n = t(1037),
          r = t(4179),
          a = t(6179),
          o = t.n(a);
        const s = [
          "contentId",
          "decoratorId",
          "direction",
          "targetId",
          "args",
          "onClick",
          "children",
          "isEnabled",
        ];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = (e) => {
          let u = e.contentId,
            t = e.decoratorId,
            l = e.direction,
            c = void 0 === l ? n.IC.Top : l,
            d = e.targetId,
            E = e.args,
            m = e.onClick,
            _ = e.children,
            A = e.isEnabled,
            F = void 0 === A || A,
            D = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, s);
          const C = (0, a.useRef)(null),
            g = (0, a.useCallback)(() => {
              if ((0, r.wU)()) return (0, r.SW)();
              C.current && (0, r.P3)(u, c, C.current, t, d, E);
            }, [u, c, E, t, d]);
          return o().createElement(
            "div",
            i(
              {
                ref: C,
                onClick:
                  ((p = _.props.onClick),
                  (e) => {
                    F && (g(), m && m(e), p && p(e));
                  }),
              },
              D,
            ),
            _,
          );
          var p;
        };
      },
      7613: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => v });
        var n = t(6483),
          r = t.n(n),
          a = t(3779),
          o = t(280),
          s = t(3532),
          i = t.n(s),
          l = t(9887),
          c = t.n(l),
          d = t(3377),
          E = t(6179),
          m = t.n(E),
          _ = t(3393);
        const A = [
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
        function F() {
          return (
            (F =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            F.apply(this, arguments)
          );
        }
        Object.keys(c());
        const D = Object.keys(i()),
          C = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          g = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          p = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          B = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          h =
            (Object.keys(B),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": C,
              "heading-H36": C,
              "heading-H28": g,
              "heading-H24": g,
              "heading-H24R": g,
              "heading-H22": g,
              "heading-H20R": g,
              "heading-H18": g,
              "heading-H15": p,
              "heading-H14": p,
              "paragraph-P24": g,
              "paragraph-P18": g,
              "paragraph-P16": g,
              "paragraph-P14": p,
              "paragraph-P12": p,
              "paragraph-P10": p,
            }),
          f =
            (Object.keys(h),
            (e) =>
              e
                ? ((e) => D.includes(e))(e)
                  ? { colorClassName: _.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          v = (0, d.ZP)((e) => {
            let u = e.text,
              t = e.variant,
              n = e.className,
              s = e.color,
              i = e.m,
              l = e.mt,
              c = void 0 === l ? i : l,
              d = e.mr,
              D = void 0 === d ? i : d,
              C = e.mb,
              g = void 0 === C ? i : C,
              p = e.ml,
              B = void 0 === p ? i : p,
              v = e.style,
              b = e.format,
              w = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, A);
            const x = (0, E.useMemo)(() => {
                const e = f(s),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, v, n), colorClassName: u };
              }, [v, s]),
              S = x.computedStyle,
              y = x.colorClassName;
            return m().createElement(
              a.ZP,
              F(
                {
                  className: r()(_.Z.base, t && _.Z[t], y, n),
                  style: S,
                  mt: !0 === c ? h[t || "paragraph-P16"].mt : c,
                  mr: !0 === D ? h[t || "paragraph-P16"].mr : D,
                  mb: !0 === g ? h[t || "paragraph-P16"].mb : g,
                  ml: !0 === B ? h[t || "paragraph-P16"].ml : B,
                },
                w,
              ),
              void 0 !== b ? m().createElement(o.z, F({}, b, { text: u })) : u,
            );
          });
      },
      7078: (e, u, t) => {
        "use strict";
        t.d(u, { t: () => i });
        var n = t(6179),
          r = t.n(n),
          a = t(2056);
        const o = ["children"];
        function s() {
          return (
            (s =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            s.apply(this, arguments)
          );
        }
        const i = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, o);
          return r().createElement(
            a.u,
            s(
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
      },
      3415: (e, u, t) => {
        "use strict";
        t.d(u, { l: () => l });
        var n = t(6179),
          r = t.n(n),
          a = t(7078),
          o = t(6373),
          s = t(2056);
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const n = r().createElement("div", { className: t }, e);
          if (u.header || u.body) return r().createElement(o.i, u, n);
          const l = u.contentId,
            c = u.args,
            d = null == c ? void 0 : c.contentId;
          return l || d
            ? r().createElement(s.u, i({}, u, { contentId: l || d }), n)
            : r().createElement(a.t, u, n);
        };
      },
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => l });
        var n = t(2056),
          r = t(6179),
          a = t.n(r);
        const o = ["children", "body", "header", "note", "alert", "args"];
        function s() {
          return (
            (s =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            s.apply(this, arguments)
          );
        }
        const i = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let u = e.children,
              t = e.body,
              l = e.header,
              c = e.note,
              d = e.alert,
              E = e.args,
              m = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, o);
            const _ = (0, r.useMemo)(() => {
              const e = Object.assign({}, E, { body: t, header: l, note: c, alert: d });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [d, t, l, c, E]);
            return a().createElement(
              n.u,
              s(
                {
                  contentId:
                    ((A = null == E ? void 0 : E.hasHtmlContent),
                    A ? i.SimpleTooltipHtmlContent("resId") : i.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: _,
                },
                m,
              ),
              u,
            );
            var A;
          };
      },
      2056: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => l });
        var n = t(7902),
          r = t(4179),
          a = t(6179);
        const o = [
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
        function s(e) {
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
        const i = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: r.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          l = (e) => {
            let u = e.children,
              t = e.contentId,
              r = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              d = e.onMouseDown,
              E = e.onClick,
              m = e.ignoreShowDelay,
              _ = void 0 !== m && m,
              A = e.ignoreMouseClick,
              F = void 0 !== A && A,
              D = e.decoratorId,
              C = void 0 === D ? 0 : D,
              g = e.isEnabled,
              p = void 0 === g || g,
              B = e.targetId,
              h = void 0 === B ? 0 : B,
              f = e.onShow,
              v = e.onHide,
              b = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, o);
            const w = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              x = (0, a.useMemo)(() => h || (0, n.F)().resId, [h]),
              S = (0, a.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (i(t, C, { isMouseEvent: !0, on: !0, arguments: s(r) }, x),
                  f && f(),
                  (w.current.isVisible = !0));
              }, [t, C, r, x, f]),
              y = (0, a.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    i(t, C, { on: !1 }, x),
                    w.current.isVisible && v && v(),
                    (w.current.isVisible = !1));
                }
              }, [t, C, x, v]),
              M = (0, a.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(w.current.prevTarget) && y();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", M, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", M, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === p && y();
              }, [p, y]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", y),
                  () => {
                    (window.removeEventListener("mouseleave", y), y());
                  }
                ),
                [y],
              ));
            return p
              ? (0, a.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((L = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(S, _ ? 100 : 400)),
                            l && l(e),
                            L && L(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (y(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === F && y(), null == E || E(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === F && y(), null == d || d(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    b,
                  ),
                )
              : u;
            var L;
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
      1856: (e, u, t) => {
        "use strict";
        t.d(u, { v: () => n });
        const n = (e) => {
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
      },
      8246: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => s });
        var n = t(3138);
        function r(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return a(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return a(e, u);
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
        function a(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const o = (e) => (0 === e ? window : window.subViews.get(e));
        function s({
          initializer: e = !0,
          rootId: u = 0,
          getRoot: t = o,
          context: a = "model",
        } = {}) {
          const s = new Map();
          function i(e, u = 0) {
            viewEnv.removeDataChangedCallback(e, u)
              ? s.delete(e)
              : console.error("Can't remove callback by id:", e);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (e, u, t) => {
              t.forEach((u) => {
                const t = s.get(u);
                void 0 !== t && t(e);
              });
            });
          });
          const l = (e) => {
            const n = t(u),
              r = a.split(".").reduce((e, u) => e[u], n);
            return "string" != typeof e || 0 === e.length
              ? r
              : e.split(".").reduce((e, u) => {
                  const t = e[u];
                  return "function" == typeof t ? t.bind(e) : t;
                }, r);
          };
          return {
            subscribe: (t, r) => {
              const o = "string" == typeof r ? `${a}.${r}` : a,
                i = n.O.view.addModelObserver(o, u, !0);
              return (s.set(i, t), e && t(l(r)), i);
            },
            readByPath: l,
            createCallback: (e, u) => {
              const t = l(u);
              return (...u) => {
                t(e(...u));
              };
            },
            createCallbackNoArgs: (e) => {
              const u = l(e);
              return () => {
                u();
              };
            },
            dispose: function () {
              for (var e, t = r(s.keys()); !(e = t()).done;) {
                i(e.value, u);
              }
            },
            unsubscribe: i,
          };
        }
      },
      3215: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => i });
        var n = t(4598),
          r = t(9174),
          a = t(6179),
          o = t.n(a),
          s = t(8246);
        const i = () => (e, u) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: i = "real", options: l, children: c, mocks: d }) {
              const E = (0, a.useRef)([]),
                m = (t, a, o) => {
                  var i;
                  const l = s.U(a),
                    c =
                      "real" === t
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (i = null == o ? void 0 : o.getter) ? i : () => {},
                          }),
                    d = (e) =>
                      "mocks" === t ? (null == o ? void 0 : o.getter(e)) : c.readByPath(e),
                    m = (e) => E.current.push(e),
                    _ = e({
                      mode: t,
                      readByPath: d,
                      externalModel: c,
                      observableModel: {
                        array: (e, u) => {
                          const a = null != u ? u : d(e),
                            o = r.LO.box(a, { equals: n.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, r.aD)((e) => o.set(e)),
                                e,
                              ),
                            o
                          );
                        },
                        object: (e, u) => {
                          const a = null != u ? u : d(e),
                            o = r.LO.box(a, { equals: n.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, r.aD)((e) => o.set(e)),
                                e,
                              ),
                            o
                          );
                        },
                        primitives: (e, u) => {
                          const n = d(u);
                          if (Array.isArray(e)) {
                            const a = e.reduce((e, u) => ((e[u] = r.LO.box(n[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, r.aD)((u) => {
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
                              o = Object.entries(a),
                              s = o.reduce((e, [u, t]) => ((e[t] = r.LO.box(n[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, r.aD)((e) => {
                                    o.forEach(([u, t]) => {
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
                      cleanup: m,
                    }),
                    A = { mode: t, model: _, externalModel: c, cleanup: m };
                  return {
                    model: _,
                    controls: "mocks" === t && o ? o.controls(A) : u(A),
                    externalModel: c,
                    mode: t,
                  };
                },
                _ = (0, a.useRef)(!1),
                A = (0, a.useState)(i),
                F = A[0],
                D = A[1],
                C = (0, a.useState)(() => m(i, l, d)),
                g = C[0],
                p = C[1];
              return (
                (0, a.useEffect)(() => {
                  _.current ? p(m(F, l, d)) : (_.current = !0);
                }, [d, F, l]),
                (0, a.useEffect)(() => {
                  D(i);
                }, [i]),
                (0, a.useEffect)(
                  () => () => {
                    (g.externalModel.dispose(), E.current.forEach((e) => e()));
                  },
                  [g],
                ),
                o().createElement(t.Provider, { value: g }, c)
              );
            },
            () => (0, a.useContext)(t),
          ];
        };
      },
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => s, onResize: () => a }));
        var n = t(2472),
          r = t(1176);
        const a = (0, n.E)("clientResized"),
          o = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, r.R)(!1);
          }
          function t() {
            e.enabled && (0, r.R)(!0);
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
              : (0, r.R)(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const a = `mouse${u}`,
                    s = o[u]((e) => t([e, "outside"]));
                  function i(e) {
                    t([e, "inside"]);
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
              e.enabled && (0, r.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, r.R)(!1);
            },
          });
        })();
      },
      5959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => n,
            getMouseGlobalPosition: () => a,
            getSize: () => r,
            graphicsQuality: () => o,
          }));
        var n = t(527);
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
      1176: (e, u, t) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => n });
      },
      2472: (e, u, t) => {
        "use strict";
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
      3138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => r });
        var n = t(5959);
        const r = { view: t(7641), client: n };
      },
      3722: (e, u, t) => {
        "use strict";
        function n(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function r(e, u, t) {
          return `url(${n(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => r, getTextureUrl: () => n }));
      },
      6112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => r });
        var n = t(2472);
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
      7641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => a.U,
            extraSize: () => x,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => b,
            getScale: () => F,
            getSize: () => E,
            getViewGlobalPosition: () => _,
            isClientAccessible: () => B,
            isEventHandled: () => f,
            isFocused: () => p,
            pxToRem: () => D,
            remToPx: () => C,
            resize: () => m,
            sendEvent: () => o.qP,
            setAnimateWindow: () => g,
            setEventHandled: () => h,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => S,
          }));
        var n = t(3722),
          r = t(6112),
          a = t(6538),
          o = t(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function c(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function E(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function _(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: C(u.x), y: C(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function C(e) {
          return viewEnv.remToPx(e);
        }
        function g(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function p() {
          return viewEnv.isFocused();
        }
        function B() {
          return viewEnv.isClientAccessible();
        }
        function h() {
          return viewEnv.setEventHandled();
        }
        function f() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function b() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(r.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === r.W[u]), e),
            {},
          ),
          x = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          S = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : a.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => l });
        const n = ["args"];
        const r = 2,
          a = 16,
          o = 32,
          s = 64,
          i = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                o = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, n);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, o, {
                      arguments:
                        ((r = a),
                        Object.entries(r).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
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
      4598: (e, u, t) => {
        "use strict";
        t.d(u, { jv: () => r, yR: () => n });
        function n(e) {
          return e;
        }
        function r() {
          return !1;
        }
        console.log;
      },
      7902: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => n });
        const n = (e = 1) => {
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
        };
      },
      3377: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => c });
        var n = t(5415),
          r = t(6179),
          a = t.n(r);
        const o = ["xl", "lg", "md", "sm", "xs"],
          s = (e) => e.includes("_") && ((e) => o.includes(e))(e.split("_").at(-1)),
          i = [n.cJ.ExtraLarge, n.cJ.Large, n.cJ.Medium, n.cJ.Small, n.cJ.ExtraSmall],
          l = (e, u) =>
            Object.keys(e).reduce((t, n) => {
              if (n in t) return t;
              if (s(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const a = i.indexOf(u),
                  s = (-1 !== a ? o.slice(a) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  l = s ? e[s] : void 0;
                return ((t[r] = void 0 !== l ? l : e[r]), t);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, u) => o.some((t) => void 0 !== u[`${e}_${t}`]))(n, e) ||
                  (t[n] = r),
                t
              );
            }, {}),
          c = (e, u = l) => {
            const t = (
              (e, u = l) =>
              (t) => {
                const o = (0, n.GS)().mediaSize,
                  s = (0, r.useMemo)(() => u(t, o), [t, o]);
                return a().createElement(e, s);
              }
            )(e, u);
            return a().memo((u) =>
              Object.keys(u).some((e) => s(e) && void 0 !== u[e])
                ? a().createElement(t, u)
                : a().createElement(e, u),
            );
          };
      },
      6536: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var n = t(6179);
        const r = (e) => {
          const u = (0, n.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      5415: (e, u, t) => {
        "use strict";
        t.d(u, { Aq: () => i, GS: () => l, cJ: () => o, fd: () => s });
        var n = t(6179),
          r = t(7739),
          a = t(1043);
        let o, s, i;
        (!(function (e) {
          ((e[(e.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = a.j.small.width)] = "Small"),
            (e[(e.Medium = a.j.medium.width)] = "Medium"),
            (e[(e.Large = a.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
        })(o || (o = {})),
          (function (e) {
            ((e[(e.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = a.j.small.width)] = "Small"),
              (e[(e.Medium = a.j.medium.width)] = "Medium"),
              (e[(e.Large = a.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
          })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = a.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = a.j.small.height)] = "Small"),
              (e[(e.Medium = a.j.medium.height)] = "Medium"),
              (e[(e.Large = a.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = a.j.extraLarge.height)] = "ExtraLarge"));
          })(i || (i = {})));
        const l = () => {
          const e = (0, n.useContext)(r.YN),
            u = e.width,
            t = e.height,
            a = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return o.ExtraLarge;
                case e.large:
                  return o.Large;
                case e.medium:
                  return o.Medium;
                case e.small:
                  return o.Small;
                case e.extraSmall:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(e),
            l = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return s.ExtraLarge;
                case e.largeWidth:
                  return s.Large;
                case e.mediumWidth:
                  return s.Medium;
                case e.smallWidth:
                  return s.Small;
                case e.extraSmallWidth:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(e),
            c = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return i.ExtraLarge;
                case e.largeHeight:
                  return i.Large;
                case e.mediumHeight:
                  return i.Medium;
                case e.smallHeight:
                  return i.Small;
                case e.extraSmallHeight:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: a,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: u,
            remScreenHeight: t,
          };
        };
      },
      2039: (e, u, t) => {
        "use strict";
        t.d(u, { b: () => r });
        var n = t(6179);
        const r = (e) => {
          (0, n.useEffect)(e, []);
        };
      },
      3112: (e, u, t) => {
        "use strict";
        t.d(u, { V: () => a });
        var n = t(6179),
          r = t(3138);
        const a = () => {
          const e = (0, n.useState)(r.O.view.getScale()),
            u = e[0],
            t = e[1];
          return (
            (0, n.useEffect)(() => {
              const e = () => {
                t(r.O.view.getScale());
              };
              return (
                window.addEventListener("resize", e),
                () => {
                  window.removeEventListener("resize", e);
                }
              );
            }, []),
            u
          );
        };
      },
      5521: (e, u, t) => {
        "use strict";
        let n, r;
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
          })(r || (r = {})));
      },
      5175: (e, u, t) => {
        "use strict";
        t.d(u, { c: () => a });
        var n = t(9480);
        const r = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? n.UI(e, (e) => ("object" == typeof e ? r(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? r(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? r(u) : u]),
                    )
              : e,
          a = (e) => r(e);
      },
      9480: (e, u, t) => {
        "use strict";
        function n(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        t.d(u, { U2: () => n, UI: () => r });
        function r(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, n) => u(null == e ? void 0 : e.value, t, n));
        }
      },
      5099: (e, u, t) => {
        "use strict";
        t.d(u, { B: () => n });
        const n = (e) => {
          let u = !1;
          return {
            promise: new Promise((t, n) => {
              e.then((e) => !u && t(e)).catch((e) => !u && n(e));
            }),
            cancel() {
              u = !0;
            },
          };
        };
      },
      9690: (e, u, t) => {
        "use strict";
        t.d(u, { HG: () => o });
        const n = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          r = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const a = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          o = (e) =>
            a
              ? `${e}`
              : (function (e) {
                  let u = "";
                  for (let t = r.length - 1; t >= 0; t--)
                    for (; e >= r[t];) ((u += n[t]), (e -= r[t]));
                  return u;
                })(e);
      },
      7727: (e, u, t) => {
        "use strict";
        function n(e) {
          engine.call("PlaySound", e);
        }
        t.d(u, { $: () => r, G: () => n });
        const r = {
          playHighlight() {
            n("highlight");
          },
          playClick() {
            n("play");
          },
          playYes() {
            n("yes1");
          },
        };
      },
      3649: (e, u, t) => {
        "use strict";
        let n;
        function r(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (t.d(u, { Uw: () => d, e: () => r, v2: () => n }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(n || (n = {})));
        const a = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          o = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          s = (e, u, t = n.left) => e.split(u).reduce(t === n.left ? a : o, []),
          i = (() => {
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
          l = ["zh_cn", "zh_sg", "zh_tw"],
          c = (e, u = n.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return l.includes(t)
              ? i(e)
              : ((e, u = n.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = e.replace(/&nbsp;/g, " ");
                  return (s(a, /( )/, u).forEach((e) => (t = t.concat(s(e, r, n.left)))), t);
                })(e, u);
          },
          d = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : c(e, u)));
      },
      1358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var n = t(3138);
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
          addCallback(e, u, t = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = n.O.view.addModelObserver(e, t, r);
            return (
              a > 0
                ? ((this._callbacks[a] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(a) : (this._views[t] = [a])))
                : console.error("Can't add callback for model:", e),
              a
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
        r.__instance = void 0;
        const a = r;
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
      4179: (e, u, t) => {
        "use strict";
        t.d(u, { B0: () => i, wU: () => v, ry: () => C, Eu: () => g, SW: () => h, P3: () => f });
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
        const r = n;
        var a = t(1358);
        const o = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          s = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
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
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(5521),
          _ = t(3138);
        const A = ["args"];
        function F(e, u, t, n, r, a, o) {
          try {
            var s = e[a](o),
              i = s.value;
          } catch (e) {
            return void t(e);
          }
          s.done ? u(i) : Promise.resolve(i).then(n, r);
        }
        const D = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          C = (function () {
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
                  return new Promise(function (n, r) {
                    var a = e.apply(u, t);
                    function o(e) {
                      F(a, n, r, o, s, "next", e);
                    }
                    function s(e) {
                      F(a, n, r, o, s, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          g = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          p = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((n = r),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, a));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          B = () => p(i.CLOSE),
          h = () => p(i.POP_OVER, { on: !1 }),
          f = (e, u, t, n, r = R.invalid("resId"), a) => {
            const o = _.O.view.getViewGlobalPosition(),
              s = t.getBoundingClientRect(),
              l = s.x,
              c = s.y,
              d = s.width,
              E = s.height,
              m = {
                x: _.O.view.pxToRem(l) + o.x,
                y: _.O.view.pxToRem(c) + o.y,
                width: _.O.view.pxToRem(d),
                height: _.O.view.pxToRem(E),
              };
            p(i.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: r,
              direction: u,
              bbox: D(m),
              on: !0,
              args: a,
            });
          },
          v = () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
          b = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var w = t(7572);
        const x = r.instance,
          S = {
            DataTracker: a.Z,
            ViewModel: w.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: E,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => p(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: B,
            sendClosePopOverEvent: h,
            sendShowContextMenuEvent: (e, u, t = 0) => {
              p(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: f,
            addEscapeListener: (e) => {
              const u = (u) => b(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              b(e, B);
            },
            handleViewEvent: p,
            onBindingsReady: C,
            onLayoutReady: g,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: v,
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const n in u)
                if (Object.prototype.hasOwnProperty.call(u, n)) {
                  const r = Object.prototype.toString.call(u[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = u[n];
                    t[n] = [];
                    for (let u = 0; u < r.length; u++) t[n].push({ value: e(r[u].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = e(u[n]))
                      : (t[n] = u[n]);
                }
              return t;
            },
            ClickOutsideManager: x,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = S;
      },
      2515: (e, u, t) => {
        "use strict";
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => Pe,
            Bar: () => Re,
            DefaultScroll: () => Oe,
            Direction: () => Ce,
            defaultSettings: () => ge,
            useHorizontalScrollApi: () => Be,
          }));
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => uu,
            Bar: () => Je,
            Default: () => eu,
            useVerticalScrollApi: () => Ie,
          }));
        var a = t(7739),
          o = t(6179),
          s = t.n(o),
          i = t(6483),
          l = t.n(i),
          c = t(926),
          d = t.n(c),
          E = t(5415);
        const m = ["children", "className"];
        function _() {
          return (
            (_ =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            _.apply(this, arguments)
          );
        }
        const A = {
            [E.fd.ExtraSmall]: "",
            [E.fd.Small]: d().SMALL_WIDTH,
            [E.fd.Medium]: `${d().SMALL_WIDTH} ${d().MEDIUM_WIDTH}`,
            [E.fd.Large]: `${d().SMALL_WIDTH} ${d().MEDIUM_WIDTH} ${d().LARGE_WIDTH}`,
            [E.fd.ExtraLarge]:
              `${d().SMALL_WIDTH} ${d().MEDIUM_WIDTH} ${d().LARGE_WIDTH} ${d().EXTRA_LARGE_WIDTH}`,
          },
          F = {
            [E.Aq.ExtraSmall]: "",
            [E.Aq.Small]: d().SMALL_HEIGHT,
            [E.Aq.Medium]: `${d().SMALL_HEIGHT} ${d().MEDIUM_HEIGHT}`,
            [E.Aq.Large]: `${d().SMALL_HEIGHT} ${d().MEDIUM_HEIGHT} ${d().LARGE_HEIGHT}`,
            [E.Aq.ExtraLarge]:
              `${d().SMALL_HEIGHT} ${d().MEDIUM_HEIGHT} ${d().LARGE_HEIGHT} ${d().EXTRA_LARGE_HEIGHT}`,
          },
          D = {
            [E.cJ.ExtraSmall]: "",
            [E.cJ.Small]: d().SMALL,
            [E.cJ.Medium]: `${d().SMALL} ${d().MEDIUM}`,
            [E.cJ.Large]: `${d().SMALL} ${d().MEDIUM} ${d().LARGE}`,
            [E.cJ.ExtraLarge]: `${d().SMALL} ${d().MEDIUM} ${d().LARGE} ${d().EXTRA_LARGE}`,
          },
          C = (e) => {
            let u = e.children,
              t = e.className,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, m);
            const r = (0, E.GS)(),
              a = r.mediaWidth,
              o = r.mediaHeight,
              i = r.mediaSize;
            return s().createElement("div", _({ className: l()(t, A[a], F[o], D[i]) }, n), u);
          },
          g = ["children"];
        const p = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, g);
          return s().createElement(a.ZN, null, s().createElement(C, t, u));
        };
        var B = t(493),
          h = t.n(B),
          f = t(1037),
          v = t(7727);
        const b = {
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
          w = [
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
        class S extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, v.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, v.G)(this.props.soundClick));
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
              r = e.side,
              a = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              c = e.onMouseLeave,
              d = e.onMouseDown,
              E = e.onMouseUp,
              m =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(e, w)),
              _ = l()(b.base, b[`base__${a}`], b[`base__${r}`], null == o ? void 0 : o.base),
              A = l()(b.icon, b[`icon__${a}`], b[`icon__${r}`], null == o ? void 0 : o.icon),
              F = l()(b.glow, null == o ? void 0 : o.glow),
              D = l()(b.caption, b[`caption__${a}`], null == o ? void 0 : o.caption),
              C = l()(b.goto, null == o ? void 0 : o.goto);
            return s().createElement(
              "div",
              x(
                {
                  className: _,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(d),
                  onMouseUp: this._onMouseUp(E),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                m,
              ),
              "info" !== a && s().createElement("div", { className: b.shine }),
              s().createElement(
                "div",
                { className: A },
                s().createElement("div", { className: F }),
              ),
              s().createElement("div", { className: D }, u),
              n && s().createElement("div", { className: C }, n),
            );
          }
        }
        S.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var y = t(3138),
          M = t(5521);
        t(4179);
        const L = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function N(e = M.n.NONE, u = L, t = !1) {
          (0, o.useEffect)(() => {
            if (e !== M.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (y.O.view.isEventHandled()) return;
                (y.O.view.setEventHandled(), u(n), t && n.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        var T = t(3112),
          k = t(3403);
        const O = {
          base: "ListHeader_base_ad",
          title: "ListHeader_title_a8",
          base__memberChange: "ListHeader_base__memberChange_c2",
          base__tankChange: "ListHeader_base__tankChange_fb",
          base__personalData: "ListHeader_base__personalData_aa",
        };
        let P;
        !(function (e) {
          ((e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(P || (P = {}));
        const I = ({ title: e, theme: u = P.Barracks, className: t, children: n }) =>
          s().createElement(
            "div",
            { className: l()(O.base, O[`base__${u}`]) },
            s().createElement("div", { className: l()(O.title, t) }, e),
            n,
          );
        var H = t(5801),
          W = t(3215),
          G = t(4598),
          j = t(9480),
          Z = t(3946);
        const U = (0, W.q)()(
            ({ observableModel: e }) => {
              const u = { root: e.object(), cardList: e.array("cardList", []) },
                t = (0, Z.Om)(() => j.UI(u.cardList.get(), G.yR), { equals: G.jv }),
                n = (0, Z.Om)(
                  (e) => {
                    const t = j.U2(u.cardList.get(), e);
                    return Object.assign({}, t, { restrictions: [...j.UI(t.restrictions, G.yR)] });
                  },
                  { equals: G.jv },
                );
              return Object.assign({}, u, { computes: { getCardList: t, getCard: n } });
            },
            ({ externalModel: e }) => ({
              onViewClose: e.createCallbackNoArgs("onViewClose"),
              resetFilters: e.createCallbackNoArgs("onResetFilters"),
              selectCard: e.createCallback((e, u) => ({ cardID: e, isSkin: u }), "onCardSelected"),
              markAsViewed: e.createCallback((e) => ({ cardID: e }), "onNewCardViewed"),
            }),
          ),
          z = U[0],
          V = U[1];
        var $ = t(2106),
          X = t(7613),
          q = t(3457),
          K = t(6373),
          Y = t(8018);
        const J = "WarningText_base_13",
          Q = "WarningText_icon_5d",
          ee = "WarningText_label_c6",
          ue = s().memo(function ({ label: e }) {
            return s().createElement(
              "div",
              { className: J },
              s().createElement("div", { className: Q }),
              s().createElement("div", { className: ee }, e),
            );
          }),
          te = "ListEmptyState_base_ae",
          ne = "ListEmptyState_content_1e",
          re = "ListEmptyState_shadow_ae",
          ae = "ListEmptyState_buttonWrapper_78",
          oe = "ListEmptyState_button_f1",
          se = s().memo(function ({
            warningText: e,
            buttonType: u = q.L$.secondary,
            tooltipArgs: t = Y.Xd,
            className: n,
            onClick: r,
            children: a,
          }) {
            return s().createElement(
              "div",
              { className: l()(te, n) },
              s().createElement(
                "div",
                { className: ne },
                s().createElement("div", { className: re }),
                s().createElement(ue, { label: e }),
                a &&
                  s().createElement(
                    "div",
                    { className: ae },
                    s().createElement(
                      K.i,
                      t,
                      s().createElement(
                        q.u5,
                        { size: q.qE.small, type: u, onClick: r, mixClass: oe },
                        a,
                      ),
                    ),
                  ),
              ),
            );
          });
        var ie = t(1856);
        const le = (e, u, t) => (t < e ? e : t > u ? u : t),
          ce = [];
        function de(e) {
          const u = (0, o.useRef)(e);
          return (
            (0, o.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, o.useCallback)((...e) => (0, u.current)(...e), ce)
          );
        }
        function Ee(e, u, t = []) {
          const n = (0, o.useRef)(0),
            r = (0, o.useCallback)(() => window.clearInterval(n.current), t || []);
          (0, o.useEffect)(() => r, [r]);
          const a = (null != t ? t : []).concat([u]);
          return [
            (0, o.useCallback)((t) => {
              ((n.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, a),
            r,
          ];
        }
        function me(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return _e(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return _e(e, u);
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
        function _e(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const Ae = () => {
          const e = (0, o.useMemo)(() => ({}), []),
            u = (u) => (e[u] || (e[u] = new Map()), e[u]),
            t = (e, t) => {
              u(e).set(t, t);
            },
            n = (e, t) => {
              u(e).delete(t);
            },
            r = (e, ...t) => {
              for (var n, r = me(u(e).values()); !(n = r()).done;) {
                (0, n.value)(...t);
              }
            };
          return (0, o.useMemo)(() => ({ on: t, off: n, trigger: r }), []);
        };
        function Fe(e, u, t) {
          const n = (0, o.useMemo)(
            () =>
              (function (e, u, t, n) {
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
                    ((o = Date.now()), t.apply(l, i));
                  }
                  a ||
                    (n && !r && d(),
                    s(),
                    void 0 === n && c > e
                      ? d()
                      : !0 !== u &&
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
                  "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
                  (i.cancel = function () {
                    (s(), (a = !0));
                  }),
                  i
                );
              })(t, e),
            u,
          );
          return ((0, o.useEffect)(() => n.cancel, [n]), n);
        }
        var De = t(7030);
        let Ce;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Ce || (Ce = {}));
        const ge = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          pe = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: a = !1,
          }) => {
            const s = (e, t) => {
              const n = u(e),
                r = n[0],
                a = n[1];
              return le(r, a, t);
            };
            return (i = {}) => {
              const l = i.settings,
                c = void 0 === l ? ge : l,
                d = (0, o.useRef)(null),
                E = (0, o.useRef)(null),
                m = Ae(),
                _ = Fe(
                  () => {
                    y.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                A = (0, De.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = d.current;
                    u && (t(u, e), m.trigger("change", e), a && _());
                  },
                  onRest: (e) => m.trigger("rest", e),
                  onStart: (e) => m.trigger("start", e),
                  onPause: (e) => m.trigger("pause", e),
                })),
                F = A[0],
                D = A[1],
                C = (0, o.useCallback)(
                  (e, u, t) => {
                    var n;
                    const r = F.scrollPosition.get(),
                      a = (null != (n = F.scrollPosition.goal) ? n : 0) - r;
                    return s(e, u * t + a + r);
                  },
                  [F.scrollPosition],
                ),
                g = (0, o.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = d.current;
                    n &&
                      D.start({
                        scrollPosition: s(n, e),
                        immediate: u,
                        reset: t,
                        config: c.animationConfig,
                        from: { scrollPosition: s(n, F.scrollPosition.get()) },
                      });
                  },
                  [D, c.animationConfig, F.scrollPosition],
                ),
                p = (0, o.useCallback)(
                  (e) => {
                    const u = d.current,
                      t = E.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return r(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, c.step),
                      a = C(u, e, n);
                    g(a);
                  },
                  [g, C, c.step],
                ),
                B = (0, o.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && p(n(e)),
                      d.current && m.trigger("mouseWheel", e, F.scrollPosition, u(d.current)));
                  },
                  [F.scrollPosition, p, m],
                ),
                h = ((e, u = []) => {
                  const t = (0, o.useRef)(),
                    n = (0, o.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, o.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    (0, ie.v)(() => {
                      const e = d.current;
                      e &&
                        (g(s(e, F.scrollPosition.goal), { immediate: !0 }),
                        m.trigger("resizeHandled"));
                    }),
                  [g, F.scrollPosition.goal],
                ),
                f = de(() => {
                  const e = d.current;
                  if (!e) return;
                  const u = s(e, F.scrollPosition.goal);
                  (u !== F.scrollPosition.goal && g(u, { immediate: !0 }),
                    m.trigger("recalculateContent"));
                });
              (0, o.useEffect)(
                () => (
                  window.addEventListener("resize", h),
                  () => {
                    window.removeEventListener("resize", h);
                  }
                ),
                [h],
              );
              const v = (0, o.useCallback)((e) => m.trigger("isThumbDraggingChanged", e), [m]);
              return (0, o.useMemo)(
                () => ({
                  getWrapperSize: () => (E.current ? r(E.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? u(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: c.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: B,
                  applyScroll: g,
                  applyStepTo: p,
                  contentRef: d,
                  wrapperRef: E,
                  scrollPosition: D,
                  animationScroll: F,
                  recalculateContent: f,
                  handleIsThumbDragging: v,
                  events: { on: m.on, off: m.off },
                }),
                [F.scrollPosition, g, p, v, m.off, m.on, f, B, D, c.step.clampedArrowStepTimeout],
              );
            };
          },
          Be = pe({
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
            getDirection: (e) => (e.deltaY > 1 ? Ce.Next : Ce.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          he = "HorizontalBar_base_49",
          fe = "HorizontalBar_base__nonActive_82",
          ve = "HorizontalBar_leftButton_5f",
          be = "HorizontalBar_rightButton_03",
          we = "HorizontalBar_track_0d",
          xe = "HorizontalBar_thumb_fd",
          Se = "HorizontalBar_rail_32",
          ye = "disable",
          Me = { pending: !1, offset: 0 },
          Le = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Ne = () => {},
          Te = (e, u) => Math.max(20, e.offsetWidth * u),
          Re = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Le, onDrag: n = Ne }) => {
              const r = (0, o.useRef)(null),
                a = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                d = (0, o.useRef)(null),
                E = e.stepTimeout || 100,
                m = (0, o.useState)(Me),
                _ = m[0],
                A = m[1],
                F = (0, o.useCallback)(
                  (e) => {
                    (A(e),
                      d.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: d.current }));
                  },
                  [n],
                ),
                D = () => {
                  const u = c.current,
                    t = d.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    l = le(0, 1, o / (r - n)),
                    E = (u.offsetWidth - Te(u, s)) * l;
                  ((t.style.transform = `translateX(${0 | E}px)`),
                    ((e) => {
                      if (a.current && i.current && c.current && d.current) {
                        if (0 === e)
                          return (a.current.classList.add(ye), void i.current.classList.remove(ye));
                        if (
                          ((u = c.current),
                          (t = d.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (a.current.classList.remove(ye), void i.current.classList.add(ye));
                        var u, t;
                        (a.current.classList.remove(ye), i.current.classList.remove(ye));
                      }
                    })(E));
                },
                C = de(() => {
                  ((() => {
                    const u = d.current,
                      t = c.current,
                      n = e.getWrapperSize(),
                      a = e.getContainerSize();
                    if (!(a && u && n && t)) return;
                    const o = Math.min(1, n / a);
                    ((u.style.width = `${Te(t, o)}px`),
                      (u.style.display = "flex"),
                      r.current &&
                        (1 === o ? r.current.classList.add(fe) : r.current.classList.remove(fe)));
                  })(),
                    D());
                });
              ((0, o.useEffect)(() => (0, ie.v)(C)),
                (0, o.useEffect)(
                  () =>
                    (0, ie.v)(() => {
                      const u = () => {
                        D();
                      };
                      let t = Ne;
                      const n = () => {
                        (t(), (t = (0, ie.v)(C)));
                      };
                      return (
                        e.events.on("recalculateContent", C),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", n),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", C),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, o.useEffect)(() => {
                  if (!_.pending) return;
                  const u = (u) => {
                      var t;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const a = c.current,
                        o = d.current;
                      if (!r || !a || !o) return;
                      const s = u.screenX - _.offset - a.getBoundingClientRect().x,
                        i = (s / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: o, thumbOffset: s, contentOffset: i }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), F(Me));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, _.offset, _.pending, n, F]));
              const g = Ee((u) => e.applyStepTo(u), E, [e]),
                p = g[0],
                B = g[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", B, !0),
                  () => document.removeEventListener("mouseup", B, !0)
                ),
                [B],
              );
              const h = (e) => {
                e.target.classList.contains(ye) || (0, v.G)("highlight");
              };
              return s().createElement(
                "div",
                { className: l()(he, u.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: l()(ve, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(ye) ||
                      0 !== e.button ||
                      ((0, v.G)("play"), p(Ce.Next));
                  },
                  onMouseUp: B,
                  ref: a,
                  onMouseEnter: h,
                }),
                s().createElement(
                  "div",
                  {
                    className: l()(we, u.track),
                    onMouseDown: (u) => {
                      const n = d.current;
                      if (n && 0 === u.button)
                        if (((0, v.G)("play"), u.target === n))
                          F({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = d.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const a = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * u);
                          })(u.screenX > n.getBoundingClientRect().x ? Ce.Prev : Ce.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: h,
                  },
                  s().createElement("div", { ref: d, className: l()(xe, u.thumb) }),
                  s().createElement("div", { className: l()(Se, u.rail) }),
                ),
                s().createElement("div", {
                  className: l()(be, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(ye) ||
                      0 !== e.button ||
                      ((0, v.G)("play"), p(Ce.Prev));
                  },
                  onMouseUp: B,
                  ref: i,
                  onMouseEnter: h,
                }),
              );
            },
          ),
          ke = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Oe = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            classNames: a,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: d,
          }) => {
            const E = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: l()(ke.base, e.base) });
              }, [n]),
              m = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: l()(ke.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: l()(ke.defaultScrollArea, r) },
                s().createElement(Pe, { className: i, api: m, classNames: a }, e),
              ),
              s().createElement(Re, { getStepByRailClick: c, api: u, onDrag: d, classNames: E }),
            );
          },
          Pe = ({ api: e, className: u, classNames: t, children: n, style: r }) => (
            (0, o.useEffect)(() => (0, ie.v)(e.recalculateContent)),
            s().createElement(
              "div",
              { className: l()(ke.base, u), style: r },
              s().createElement(
                "div",
                {
                  className: l()(ke.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: l()(ke.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((Pe.Bar = Re),
          (Pe.Default = Oe),
          (Pe.SeniorityAwards = ({ api: e, className: u, classNames: t, children: n }) => (
            (0, o.useEffect)(() => (0, ie.v)(e.recalculateContent)),
            s().createElement(
              "div",
              { className: l()(ke.base, u) },
              s().createElement(
                "div",
                { className: l()(ke.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: l()(ke.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Ie = pe({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Ce.Next : Ce.Prev),
          }),
          He = "VerticalBar_base_f3",
          We = "VerticalBar_base__nonActive_42",
          Ge = "VerticalBar_topButton_d7",
          je = "VerticalBar_bottomButton_06",
          Ze = "VerticalBar_track_df",
          Ue = "VerticalBar_thumb_32",
          ze = "VerticalBar_rail_43",
          Ve = "disable",
          $e = () => {},
          Xe = { pending: !1, offset: 0 },
          qe = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Ke = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          Ye = (e, u) => Math.max(20, e.offsetHeight * u),
          Je = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = qe, onDrag: n = $e }) => {
              const r = (0, o.useRef)(null),
                a = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                d = (0, o.useRef)(null),
                E = e.stepTimeout || 100,
                m = (0, o.useState)(Xe),
                _ = m[0],
                A = m[1],
                F = (0, o.useCallback)(
                  (e) => {
                    (A(e),
                      d.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: d.current }));
                  },
                  [n],
                ),
                D = de(() => {
                  const u = d.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && a && u && t)) return;
                  const o = Math.min(1, n / a);
                  return (
                    (u.style.height = `${Ye(t, o)}px`),
                    u.classList.add(Ue),
                    r.current &&
                      (1 === o ? r.current.classList.add(We) : r.current.classList.remove(We)),
                    o
                  );
                }),
                C = de(() => {
                  const u = c.current,
                    t = d.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    l = le(0, 1, o / (r - n)),
                    E = (u.offsetHeight - Ye(u, s)) * l;
                  ((t.style.transform = `translateY(${0 | E}px)`),
                    ((e) => {
                      if (a.current && i.current && c.current && d.current) {
                        if (0 === e)
                          return (a.current.classList.add(Ve), void i.current.classList.remove(Ve));
                        if (
                          ((u = c.current),
                          (t = d.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (a.current.classList.remove(Ve), void i.current.classList.add(Ve));
                        var u, t;
                        (a.current.classList.remove(Ve), i.current.classList.remove(Ve));
                      }
                    })(E));
                }),
                g = de(() => {
                  Ke(e, () => {
                    (D(), C());
                  });
                });
              ((0, o.useEffect)(() => (0, ie.v)(g)),
                (0, o.useEffect)(() => {
                  const u = () => {
                    Ke(e, () => {
                      C();
                    });
                  };
                  let t = $e;
                  const n = () => {
                    (t(), (t = (0, ie.v)(g)));
                  };
                  return (
                    e.events.on("recalculateContent", g),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", n),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", g),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, o.useEffect)(() => {
                  if (!_.pending) return;
                  const u = (u) => {
                      Ke(e, (t) => {
                        const r = c.current,
                          a = d.current,
                          o = e.getContainerSize();
                        if (!r || !a || !o) return;
                        const s = u.screenY - _.offset - r.getBoundingClientRect().y,
                          i = (s / r.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: a, thumbOffset: s, contentOffset: i }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        F(Xe));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, _.offset, _.pending, n, F]));
              const p = Ee((u) => e.applyStepTo(u), E, [e]),
                B = p[0],
                h = p[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const f = (e) => {
                e.target.classList.contains(Ve) || (0, v.G)("highlight");
              };
              return s().createElement(
                "div",
                { className: l()(He, u.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: l()(Ge, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ve) ||
                      0 !== e.button ||
                      ((0, v.G)("play"), B(Ce.Next));
                  },
                  ref: a,
                  onMouseEnter: f,
                }),
                s().createElement(
                  "div",
                  {
                    className: l()(Ze, u.track),
                    onMouseDown: (u) => {
                      const n = d.current;
                      if (n && 0 === u.button)
                        if (((0, v.G)("play"), u.target === n))
                          (e.handleIsThumbDragging(!0),
                            F({ pending: !0, offset: u.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            d.current &&
                              Ke(e, (n) => {
                                if (!n) return;
                                const r = t(e),
                                  a = e.clampPosition(n, n.scrollTop + r * u);
                                e.applyScroll(a);
                              });
                          })(u.screenY > n.getBoundingClientRect().y ? Ce.Prev : Ce.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: f,
                  },
                  s().createElement("div", { ref: d, className: u.thumb }),
                  s().createElement("div", { className: l()(ze, u.rail) }),
                ),
                s().createElement("div", {
                  className: l()(je, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ve) ||
                      0 !== e.button ||
                      ((0, v.G)("play"), B(Ce.Prev));
                  },
                  onMouseUp: h,
                  ref: i,
                  onMouseEnter: f,
                }),
              );
            },
          ),
          Qe = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          eu = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: a,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: d,
          }) => {
            const E = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: l()(Qe.base, e.base) });
              }, [n]),
              m = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: l()(Qe.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: l()(Qe.area, r) },
                s().createElement(uu, { className: a, classNames: i, api: m }, e),
              ),
              s().createElement(Je, { getStepByRailClick: c, api: u, onDrag: d, classNames: E }),
            );
          },
          uu = ({ className: e, classNames: u, children: t, api: n }) => (
            (0, o.useEffect)(() => (0, ie.v)(n.recalculateContent)),
            s().createElement(
              "div",
              { className: l()(Qe.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              s().createElement(
                "div",
                { className: l()(Qe.content, null == u ? void 0 : u.content), ref: n.contentRef },
                t,
              ),
            )
          );
        uu.Default = eu;
        const tu = { Vertical: r, Horizontal: n },
          nu = ({
            startRowIndex: e,
            cellHeight: u,
            paddingTop: t,
            paddingBottom: n,
            amount: r,
            itemsAmountPerRow: a,
            visibleRowsAmount: o,
            numOdfHeadingsBefore: s,
            numOfEmptySlotsInside: i,
          }) => {
            const l = Math.ceil(r / a) * u,
              c = o * u + 40 * i,
              d = e * u + 40 * s;
            return { paddingTop: `${d + t}rem`, paddingBottom: `${Math.max(l - d - c, 0) + n}rem` };
          },
          ru = (0, o.memo)((e) => {
            const u = e.className,
              t = e.children,
              n = e.itemsAmountPerRow,
              r = e.visibleRowsAmount,
              a = e.realFirstInRowIndex,
              o = e.amount,
              i = e.numOdfHeadingsBefore,
              l = e.numOfEmptySlotsInside,
              c = Math.min(r * n + l, o - a);
            return s().createElement(
              "div",
              { className: u, style: nu(Object.assign({}, e, { numOdfHeadingsBefore: i })) },
              ((e, u) => {
                const t = [];
                for (let n = 0; n < e; n++) t.push(u(n));
                return t;
              })(c, (e) => t(a + e)),
            );
          }),
          au = "VirtualGrid_base_52",
          ou = ({
            amount: e,
            headingsIndexes: u,
            cellWidth: t,
            cellHeight: n,
            children: r,
            api: a,
            classNames: i,
            preloadedRows: c = 1,
            paddingTop: d = 0,
            paddingBottom: E = 0,
          }) => {
            const m = a.scrollApi,
              _ = (0, o.useRef)(0),
              A = (0, o.useState)(0),
              F = A[0],
              D = A[1],
              C = (0, o.useState)(null),
              g = C[0],
              p = C[1],
              B = (0, o.useState)(null),
              h = B[0],
              f = B[1];
            ((0, o.useEffect)(() => {
              const u = (u) => {
                if (!g) return;
                const t = Math.floor((y.O.view.pxToRem(u.value.scrollPosition) - d) / n),
                  r = Math.ceil(e / g),
                  o = Math.max(0, Math.min(t - c, r));
                (D(o), a.startRowIndexChanged(o));
              };
              return (m.events.on("change", u), () => m.events.off("change", u));
            }, [a, m, n, d, g, e, c]),
              (0, o.useEffect)(() => {
                const e = () => {
                    if (m.contentRef.current) {
                      const e = getComputedStyle(m.contentRef.current),
                        u = m.contentRef.current.getBoundingClientRect(),
                        r =
                          y.O.view.pxToRem(u.width) -
                          (parseFloat(e.paddingLeft) + parseFloat(e.paddingRight)),
                        o = Math.floor(r / t),
                        s = Math.ceil(y.O.view.pxToRem(u.height) / n) + 2 * c;
                      ((_.current = o), g !== o && p(o), f(s), a.layoutCalculated(o, s));
                    }
                  },
                  u = () => {
                    const u = _.current;
                    (e(), a.scrollToIndex(F * u));
                  };
                return (
                  m.events.on("recalculateContent", e),
                  m.events.on("resizeHandled", u),
                  () => {
                    (m.events.off("recalculateContent", e), m.events.off("resizeHandled", u));
                  }
                );
              }, [a, m, n, t, g, c, F]),
              (0, o.useEffect)(() => {
                const e = (e, u = !0) => {
                  g && m.applyScroll(Math.floor((e + 1) / g) * n + d, { immediate: u });
                };
                return (a.events.on("scrollToIndex", e), () => a.events.off("scrollToIndex", e));
              }, [a, n, g, d, m]));
            const v = (({ api: e, startRowIndex: u, itemsAmountPerRow: t, headingsIndexes: n }) => {
                const r = u * t;
                if (!n) return r;
                const a = n.reduce((e, u, n, a) => {
                  if (u < r) {
                    if (0 === n) return e + 1;
                    const r = (u - 1 - a[n - 1]) % t;
                    e += 1 - (r ? t - r : 0);
                  }
                  return e;
                }, r);
                return (e.firstCardIndexChanged(a), a);
              })({ api: a, headingsIndexes: u, startRowIndex: F, itemsAmountPerRow: g || 4 }),
              b = (({ offset: e, headingsIndexes: u }) => (u ? u.filter((u) => u < e).length : 0))({
                offset: v,
                headingsIndexes: u,
              }),
              w = (({ amount: e, offset: u, headingsIndexes: t }) =>
                t ? t.filter((t) => t >= u && t <= u + e).length : 0)({
                offset: v,
                amount: (h || 1) * (g || 4),
                headingsIndexes: u,
              }),
              x = (({ offset: e, amount: u, itemsAmountPerRow: t, headingsIndexes: n }) =>
                n
                  ? n.reduce((n, r, a, o) => {
                      if (r >= e && r <= e + u) {
                        if (0 === a) return n + 1;
                        const e = (r - 1 - o[a - 1]) % t;
                        n += 1 + (e ? t - e : 0);
                      }
                      return n;
                    }, 0)
                  : 0)({
                headingsIndexes: u,
                offset: v,
                amount: (h || 1) * (g || 4),
                itemsAmountPerRow: g || 4,
              });
            return s().createElement(
              tu.Vertical.Default,
              {
                api: m,
                className: null == i ? void 0 : i.scroll,
                areaClassName: null == i ? void 0 : i.areaClassName,
                scrollClassName: null == i ? void 0 : i.scrollClassName,
                scrollClassNames: {
                  content: null == i ? void 0 : i.content,
                  wrapper: null == i ? void 0 : i.wrapper,
                },
              },
              null !== g &&
                null !== h &&
                s().createElement(
                  ru,
                  {
                    className: l()(au, null == i ? void 0 : i.inner),
                    paddingBottom: E,
                    realFirstInRowIndex: v,
                    numOdfHeadingsBefore: b,
                    numOdfHeadingsInside: w,
                    paddingTop: d,
                    amount: e,
                    itemsAmountPerRow: g,
                    visibleRowsAmount: h,
                    numOfEmptySlotsInside: x,
                    startRowIndex: F,
                    cellHeight: n,
                  },
                  r,
                ),
            );
          },
          su = "VirtualGridWithFade_scrollAreaFade_94",
          iu = ["api", "children", "classNames"];
        function lu() {
          return (
            (lu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            lu.apply(this, arguments)
          );
        }
        const cu = (e) => {
          let u = e.api,
            t = e.children,
            n = e.classNames,
            r = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, iu);
          const a = (0, o.useState)(!0),
            i = a[0],
            c = a[1],
            d = u.scrollApi;
          return (
            (0, o.useEffect)(() => {
              const e = () => {
                const e = d.getBounds()[1];
                c(Math.abs(e - d.animationScroll.scrollPosition.goal) > 0.1);
              };
              return (
                d.events.on("change", e),
                d.events.on("recalculateContent", e),
                () => {
                  (d.events.off("change", e), d.events.off("recalculateContent", e));
                }
              );
            }, [d]),
            s().createElement(
              ou,
              lu(
                {
                  api: u,
                  classNames: Object.assign({}, n, {
                    scrollClassName: l()(null == n ? void 0 : n.scrollClassName, i && su),
                  }),
                },
                r,
              ),
              t,
            )
          );
        };
        let du, Eu, mu, _u;
        (!(function (e) {
          ((e.Default = "default"), (e.Selected = "selected"), (e.Disabled = "disabled"));
        })(du || (du = {})),
          (function (e) {
            ((e.Document = "document"), (e.Skin = "skin"));
          })(Eu || (Eu = {})),
          (function (e) {
            ((e.Document = "document"), (e.SuitableSkin = "suitableSkin"));
          })(mu || (mu = {})),
          (function (e) {
            ((e.None = "none"), (e.Default = "default"), (e.CardLocked = "cardLocked"));
          })(_u || (_u = {})));
        var Au = t(3649);
        const Fu = {
          base: "FlagIcon_base_25",
          base__c_1080x454: "FlagIcon_base__c_1080x454_6c",
          base__c_240x118: "FlagIcon_base__c_240x118_92",
        };
        let Du;
        !(function (e) {
          ((e.c1080x454 = "c_1080x454"), (e.c240x118 = "c_240x118"));
        })(Du || (Du = {}));
        const Cu = (e, u) => {
            switch (u) {
              case Du.c1080x454:
                return R.images.gui.maps.icons.crew.flags.$dyn(e);
              case Du.c240x118:
                return R.images.gui.maps.icons.tankmen.card.nations.$dyn(e);
            }
          },
          gu = s().memo(function ({ nation: e, size: u, className: t }) {
            return s().createElement("div", {
              className: l()(Fu.base, Fu[`base__${u}`], t),
              style: { backgroundImage: `url('${Cu(e, u)}')` },
            });
          }),
          pu = "ListCardAlert_base_52",
          Bu = "ListCardAlert_glow_1c",
          hu = "ListCardAlert_icon_d2",
          fu = ({ className: e, tooltipArgs: u }) =>
            s().createElement(
              "div",
              { className: l()(pu, e) },
              s().createElement("div", { className: Bu }),
              s().createElement(K.i, u, s().createElement("div", { className: hu })),
            ),
          vu = {
            base: "BaseCard_base_b7",
            base__default: "BaseCard_base__default_32",
            base__selected: "BaseCard_base__selected_cd",
            base__disabled: "BaseCard_base__disabled_5c",
            base__alertCardLocked: "BaseCard_base__alertCardLocked_89",
            selectedFrame: "BaseCard_selectedFrame_f3",
            flag: "BaseCard_flag_40",
            icon: "BaseCard_icon_ab",
            separator: "BaseCard_separator_ac",
            cardInfo: "BaseCard_cardInfo_d9",
            cardInfo__withAdditionalInfo: "BaseCard_cardInfo__withAdditionalInfo_2c",
            name: "BaseCard_name_75",
            typeIcon: "BaseCard_typeIcon_a2",
            alertIcon: "BaseCard_alertIcon_18",
          },
          bu = (0, o.memo)(
            ({
              icon: e,
              typeIcon: u,
              name: t,
              nation: n,
              cardState: r,
              children: a,
              alertType: o,
            }) =>
              s().createElement(
                "div",
                {
                  onMouseEnter: v.$.playHighlight,
                  className: l()(vu.base, vu[`base__${r}`], vu[`base__alert${(0, Au.e)(o)}`]),
                },
                r === du.Selected && s().createElement("div", { className: vu.selectedFrame }),
                n && s().createElement(gu, { nation: n, size: Du.c240x118, className: vu.flag }),
                s().createElement("div", {
                  className: vu.icon,
                  style: { backgroundImage: `url(${e})` },
                }),
                s().createElement("div", { className: vu.separator }),
                t &&
                  s().createElement(
                    "div",
                    { className: l()(vu.cardInfo, Boolean(a) && vu.cardInfo__withAdditionalInfo) },
                    s().createElement(
                      "div",
                      { className: vu.name },
                      s().createElement(X.ZP, { text: t }),
                    ),
                    a,
                  ),
                s().createElement("div", {
                  className: vu.typeIcon,
                  style: { backgroundImage: `url(${u})` },
                }),
                o !== _u.None &&
                  s().createElement(fu, {
                    className: vu.alertIcon,
                    tooltipArgs: {
                      header: R.strings.crew.personalData.card.tooltip.locked.title(),
                      body: R.strings.crew.personalData.card.tooltip.locked.body(),
                      isEnabled: o === _u.CardLocked,
                    },
                  }),
              ),
          ),
          wu = R.strings.crew.personalData.card.tooltip.document,
          xu = (0, o.memo)(
            ({ icon: e, name: u, cardState: t, className: n, isCardsLocked: r, onClick: a }) =>
              s().createElement(
                K.i,
                { header: wu.title(), body: wu.body(), isEnabled: !r },
                s().createElement(
                  "div",
                  { className: n, onClick: a },
                  s().createElement(bu, {
                    icon: e,
                    typeIcon: R.images.gui.maps.icons.crew.personalData.c_24x24.document(),
                    name: u,
                    cardState: t,
                    alertType: r ? _u.CardLocked : _u.None,
                  }),
                ),
              ),
          );
        var Su = t(7078);
        var yu = t(9367);
        const Mu = "InventoryInfo_base_08",
          Lu = "InventoryInfo_icon_a6",
          Nu = "InventoryInfo_amount_ec",
          Tu = (0, o.memo)(({ amount: e, className: u }) =>
            s().createElement(
              "div",
              { className: l()(Mu, u) },
              s().createElement("div", { className: Lu }),
              s().createElement(
                "div",
                { className: Nu },
                s().createElement(X.ZP, { text: `${e}` }),
              ),
            ),
          ),
          Ru = (0, o.memo)(({ restrictions: e, className: u }) =>
            s().createElement(
              "div",
              { className: u },
              s().createElement(X.ZP, {
                text: R.strings.crew.personalData.card.restrictions(),
                format: { binding: { restrictions: e.join(", ") } },
              }),
            ),
          ),
          ku = "SkinCard_base_dd",
          Ou = "SkinCard_restrictions_42",
          Pu = "SkinCard_inventoryInfo_3d",
          Iu = "SkinCard_newSkinMark_37",
          Hu = (e, u) => (e ? _u.CardLocked : u ? _u.Default : _u.None),
          Wu = (0, o.memo)(
            ({
              id: e,
              nation: u,
              icon: t,
              name: n,
              restrictions: r,
              inventoryCount: a,
              cardState: o,
              newAmount: i,
              isCardsLocked: c,
              className: d,
              onClick: E,
              handleMarkAsViewed: m,
            }) => {
              const _ = r.length > 0,
                A = i > 0;
              return s().createElement(
                Su.t,
                { args: { tooltipId: "crewSkin", skinId: e } },
                s().createElement(
                  "div",
                  { className: l()(ku, d), onClick: E, onMouseEnter: () => A && m(e) },
                  s().createElement(
                    bu,
                    {
                      icon: t,
                      typeIcon: R.images.gui.maps.icons.crew.personalData.c_24x24.skin(),
                      name: n,
                      nation: u,
                      cardState: o,
                      alertType: Hu(c, _),
                    },
                    _ && s().createElement(Ru, { restrictions: r, className: Ou }),
                  ),
                  s().createElement(Tu, { amount: a, className: Pu }),
                  A && s().createElement(yu.Q, { value: i > 1 ? i : void 0, className: Iu }),
                ),
              );
            },
          );
        function Gu() {
          return (
            (Gu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Gu.apply(this, arguments)
          );
        }
        const ju = { [Eu.Skin]: Wu, [Eu.Document]: xu },
          Zu = (0, o.memo)(
            ({
              isCardsLocked: e,
              index: u,
              getCard: t,
              handleMarkAsViewed: n,
              handleCardSelected: r,
              className: a,
            }) => {
              const i = t(u),
                l = i.cardState !== du.Disabled && !e,
                c = (0, o.useCallback)(
                  () => l && r(i.id, i.cardType === Eu.Skin),
                  [i.cardType, i.id, l, r],
                ),
                d = ju[i.cardType];
              return s().createElement(
                d,
                Gu({}, i, { className: a, isCardsLocked: e, onClick: c, handleMarkAsViewed: n }),
              );
            },
          ),
          Uu = "DataCardList_base_2c",
          zu = "DataCardList_grid_f8",
          Vu = "DataCardList_gridWrapper_27",
          $u = "DataCardList_gridWrapper__scaled_f3",
          Xu = "DataCardList_emptyState_0e",
          qu = "DataCardList_item_6c",
          Ku = [],
          Yu = (0, k.Pi)(() => {
            const e = (() => {
                const e = tu.Vertical.useVerticalScrollApi(),
                  u = Ae(),
                  t = (0, o.useCallback)((e, t = !0) => u.trigger("scrollToIndex", e, t), [u]),
                  n = (0, o.useCallback)((e, t) => u.trigger("layoutCalculated", e, t), [u]),
                  r = (0, o.useCallback)((e) => u.trigger("startRowIndexChanged", e), [u]),
                  a = (0, o.useCallback)((e) => u.trigger("firstCardIndexChanged", e), [u]);
                return (0, o.useMemo)(
                  () => ({
                    scrollToIndex: t,
                    layoutCalculated: n,
                    startRowIndexChanged: r,
                    firstCardIndexChanged: a,
                    scrollApi: e,
                    events: { off: u.off, on: u.on },
                  }),
                  [t, n, r, a, e, u.off, u.on],
                );
              })(),
              u = V(),
              t = u.model,
              n = u.controls,
              r = t.root.get().isCardsLocked,
              a = t.computes.getCardList().length,
              i = 2 === (0, T.V)(),
              c = (e) => t.computes.getCard(e),
              d = (e) => n.markAsViewed(e),
              E = (e, u) => {
                (v.$.playClick(), n.selectCard(e, u));
              };
            return s().createElement(
              "div",
              { className: Uu },
              s().createElement(
                "div",
                { className: l()(Vu, i && $u) },
                a > 0
                  ? s().createElement(
                      cu,
                      {
                        amount: a,
                        cellWidth: 318,
                        cellHeight: 208,
                        paddingTop: 11,
                        paddingBottom: 11,
                        classNames: { content: zu },
                        api: e,
                        headingsIndexes: Ku,
                      },
                      (e) =>
                        s().createElement(Zu, {
                          key: e,
                          index: e,
                          isCardsLocked: r,
                          className: qu,
                          getCard: c,
                          handleMarkAsViewed: d,
                          handleCardSelected: E,
                        }),
                    )
                  : s().createElement(
                      se,
                      {
                        warningText: R.strings.crew.personalData.emptyState.noFilteredItems(),
                        buttonType: $.L.primary,
                        onClick: n.resetFilters,
                        className: Xu,
                      },
                      s().createElement(X.ZP, { text: R.strings.crew.filter.reset() }),
                    ),
              ),
            );
          }),
          Ju = {
            base: "App_base_48",
            flag: "App_flag_52",
            content: "App_content_b1",
            filterWrapper: "App_filterWrapper_e5",
            closeButton: "App_closeButton_c4",
            title: "App_title_a2",
          },
          Qu = R.strings.crew,
          et = (0, k.Pi)(() => {
            const e = V(),
              u = e.model,
              t = e.controls,
              n = u.root.get().nation,
              r = (0, E.GS)().mediaHeight,
              a = (0, E.GS)().remScreenWidth >= 2560,
              o = 2 === (0, T.V)();
            return (
              (function ({
                key: e = M.n.ESCAPE,
                callback: u = () => y.O.view.sendEvent.close(),
                preventPropagation: t = !0,
              } = {}) {
                N(e, u, t);
              })({ callback: t.onViewClose }),
              s().createElement(
                "div",
                { className: l()(Ju.base, a && !o && Ju.base__centered) },
                s().createElement("div", {
                  style: { backgroundImage: `url(${R.images.gui.maps.icons.crew.flags.$dyn(n)})` },
                  className: Ju.flag,
                }),
                s().createElement(
                  "div",
                  { className: l()(Ju.content, o && Ju.content__scaled) },
                  s().createElement(I, {
                    title: Qu.changeTankmanSkinView.header(),
                    theme: P.PersonalData,
                    className: Ju.title,
                  }),
                  s().createElement(
                    "div",
                    { className: Ju.filterWrapper },
                    s().createElement(H.p, {
                      popoverDirection: r < E.Aq.Medium ? f.IC.Left : f.IC.Bottom,
                    }),
                  ),
                  s().createElement(Yu, null),
                ),
                s().createElement(
                  "div",
                  { className: Ju.closeButton },
                  s().createElement(S, {
                    side: "right",
                    type: "close",
                    caption: Qu.tankmanChangeAndRecruitView.closeButton(),
                    onClick: t.onViewClose,
                  }),
                ),
              )
            );
          });
        engine.whenReady.then(() => {
          h().render(
            s().createElement(z, null, s().createElement(p, null, s().createElement(et, null))),
            document.getElementById("root"),
          );
        });
      },
      9367: (e, u, t) => {
        "use strict";
        t.d(u, { Q: () => d });
        var n = t(6483),
          r = t.n(n),
          a = t(9987),
          o = t(6179),
          s = t.n(o);
        const i = "AlertCounter_base_f3",
          l = "AlertCounter_counter_da",
          c = "AlertCounter_label_18",
          d = ({ value: e, className: u }) =>
            s().createElement(
              "div",
              { className: r()(i, u) },
              s().createElement(a.A, { value: e, className: l }),
              !e &&
                s().createElement("div", { className: c }, R.strings.crew.common.exclamationMark()),
            );
      },
      9197: (e, u, t) => {
        "use strict";
        t.d(u, { C: () => f });
        var n = t(6483),
          r = t.n(n),
          a = t(3112),
          o = t(6179),
          s = t.n(o),
          i = t(7613),
          l = t(6373);
        const c = "NumberRange_base_5e",
          d = "NumberRange_base__animation_79",
          E = "NumberRange_from_70",
          m = "NumberRange_from__red_f8",
          _ = "NumberRange_separator_c0",
          A = R.strings.crew.barracks.berthsAmountDivider(),
          F = R.strings.crew.filterPanel.counter.selectLimit,
          D = (0, o.memo)(function ({
            isFilterRange: e,
            from: u,
            to: t,
            className: n,
            isSelectMode: a = !1,
            isSelectedLimitReached: o = !1,
          }) {
            return a
              ? s().createElement(
                  l.i,
                  { header: F.header(), body: F.body(), ignoreShowDelay: !0 },
                  s().createElement(
                    "div",
                    { className: r()(c, n) },
                    s().createElement(i.ZP, { className: E, text: String(u) }),
                    (u !== t || o) &&
                      s().createElement(
                        s().Fragment,
                        null,
                        s().createElement(i.ZP, { className: _, text: A }),
                        s().createElement(i.ZP, { text: String(t) }),
                      ),
                  ),
                )
              : e
                ? s().createElement(
                    "div",
                    { className: r()(c, 0 === u && d, n) },
                    s().createElement(i.ZP, {
                      className: r()(E, 0 === u && t > 0 && m),
                      text: String(u),
                    }),
                    u !== t &&
                      s().createElement(
                        s().Fragment,
                        null,
                        s().createElement(i.ZP, { className: _, text: A }),
                        s().createElement(i.ZP, { text: String(t) }),
                      ),
                  )
                : s().createElement(
                    "div",
                    { className: r()(c, u > t && d, n) },
                    s().createElement(i.ZP, { className: r()(E, u > t && m), text: String(u) }),
                    s().createElement(i.ZP, { className: _, text: A }),
                    s().createElement(i.ZP, { text: String(t) }),
                  );
          }),
          C = "NumberRangeWithLabel_base_2b",
          g = "NumberRangeWithLabel_title_94",
          p = "NumberRangeWithLabel_counter_00",
          B = "NumberRangeWithLabel_counterGlow_1f",
          h = "NumberRangeWithLabel_blink_89",
          f = (0, o.memo)(
            ({
              title: e,
              isGlowVisible: u = !1,
              isSelectedLimitReached: t = !1,
              isFilterRange: n = !1,
              isSelectMode: o = !1,
              className: l,
              classNames: c,
              from: d,
              to: E,
            }) => {
              const m = (0, a.V)(),
                _ = {
                  left:
                    d !== E || t
                      ? 7 * String(d).length * m + 4 * m
                      : Math.round((7 * String(d).length * m) / 2),
                };
              return s().createElement(
                "div",
                { className: r()(C, l) },
                s().createElement(i.ZP, { className: g, text: e }),
                s().createElement(
                  "div",
                  { className: p },
                  s().createElement(D, {
                    isFilterRange: n,
                    isSelectedLimitReached: t,
                    isSelectMode: o,
                    from: d,
                    to: E,
                  }),
                  u &&
                    n &&
                    s().createElement("div", {
                      style: _,
                      className: r()(B, t && h, null == c ? void 0 : c.counterGlow),
                    }),
                ),
              );
            },
          );
      },
      9631: (e, u, t) => {
        "use strict";
        t.d(u, { C: () => m });
        var n = t(6483),
          r = t.n(n),
          a = t(3457),
          o = t(2106),
          s = t(9987),
          i = t(6179),
          l = t.n(i),
          c = t(4723);
        const d = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function E() {
          return (
            (E =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            E.apply(this, arguments)
          );
        }
        const m = l().memo(function (e) {
          let u = e.isActive,
            t = e.counter,
            n = e.className,
            i = e.children,
            m = e.type,
            _ = void 0 === m ? o.L.secondary : m,
            A = e.size,
            F = void 0 === A ? o.q.small : A,
            D = e.hasIndicator,
            C = void 0 === D || D,
            g = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, d);
          return l().createElement(
            "div",
            { className: r()(c.Z.base, n, u && c.Z.base__active) },
            l().createElement(a.u5, E({ type: _, size: F, mixClass: c.Z.button }, g), i),
            l().createElement("div", { className: c.Z.overlay }),
            C && l().createElement("div", { className: c.Z.indicator }),
            Boolean(t) &&
              l().createElement(
                "div",
                { className: c.Z.counter },
                l().createElement(s.A, { value: t, size: "small" }),
              ),
          );
        });
      },
      8018: (e, u, t) => {
        "use strict";
        t.d(u, { Er: () => a, Xd: () => r });
        t(3649);
        R.strings.common.percentValue();
        let n;
        !(function (e) {
          ((e.Objective = "objective"), (e.Possessive = "possessive"));
        })(n || (n = {}));
        const r = {
            header: R.strings.crew.filterPanel.counter.reset.header(),
            body: R.strings.crew.filterPanel.counter.reset.body(),
          },
          a = {
            header: R.strings.crew.filterPanel.counterMultySelect.reset.header(),
            body: R.strings.crew.filterPanel.counterMultySelect.reset.body(),
          };
        let o;
        !(function (e) {
          ((e.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (e.SHOP_INFO = "shop_info"),
            (e.RUDY = "rudy"));
        })(o || (o = {}));
      },
      5801: (e, u, t) => {
        "use strict";
        t.d(u, { p: () => Pe });
        var n = t(6179),
          r = t.n(n),
          a = t(6483),
          o = t.n(a),
          s = t(3457),
          i = t(2106),
          l = t(7613),
          c = t(6373);
        let d;
        !(function (e) {
          ((e.Default = "default"),
            (e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(d || (d = {}));
        var E = t(3403),
          m = t(3415),
          _ = t(9480),
          A = t(9631);
        const F = "FilterTitle_base_a7",
          D = "FilterTitle_label_05",
          C = "FilterTitle_discount_42",
          g = "FilterTitle_discountIcon_30",
          p = ({ label: e, hasDiscount: u, className: t }) =>
            r().createElement(
              "div",
              { className: o()(F, t) },
              r().createElement("div", { className: D }, e),
              u &&
                r().createElement(
                  "div",
                  { className: C },
                  r().createElement("div", { className: g }),
                ),
            );
        let B;
        !(function (e) {
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
        })(B || (B = {}));
        var h = t(3649);
        const f = "ToggleIcon_base_59",
          v = "ToggleIcon_base__small_3e",
          b = "ToggleIcon_icon_e7",
          w = r().memo(function ({ icon: e, isSmall: u = !1, classNames: t }) {
            return r().createElement(
              "div",
              { className: o()(f, u && v) },
              r().createElement("div", {
                className: o()(b, null == t ? void 0 : t.icon),
                style: { backgroundImage: `url(${e})` },
              }),
            );
          });
        var x = t(9690);
        const S = "VehicleTier_base_9c",
          y = "VehicleTier_base__small_fc",
          M = ({ level: e, isSmall: u = !1 }) =>
            r().createElement("div", { className: o()(S, u && y) }, (0, x.HG)(e)),
          L = {
            icon__vehicleType: "ToggleButtonIcon_icon__vehicleType_83",
            icon__nation: "ToggleButtonIcon_icon__nation_c1",
            icon__vehicleGradePrimary: "ToggleButtonIcon_icon__vehicleGradePrimary_d6",
            icon__tankmanRole: "ToggleButtonIcon_icon__tankmanRole_4b",
            icon__selected: "ToggleButtonIcon_icon__selected_ca",
            icon__tankmanKind: "ToggleButtonIcon_icon__tankmanKind_5e",
            icon__vehicleGradeElite: "ToggleButtonIcon_icon__vehicleGradeElite_26",
            icon__locationRecruit: "ToggleButtonIcon_icon__locationRecruit_3b",
            icon__locationTankman: "ToggleButtonIcon_icon__locationTankman_f6",
            icon__locationUnique: "ToggleButtonIcon_icon__locationUnique_cb",
            icon__personalDataType: "ToggleButtonIcon_icon__personalDataType_a8",
            icon__tankmanKindDismissed: "ToggleButtonIcon_icon__tankmanKindDismissed_86",
            icon__vehicleGradePremium: "ToggleButtonIcon_icon__vehicleGradePremium_11",
          },
          N = ({ id: e, icon: u, type: t, isSmall: n = !0, isSelected: a = !1 }) =>
            t === B.VehicleTier
              ? r().createElement(M, { isSmall: n, level: Number(e) })
              : r().createElement(w, {
                  icon: u,
                  isSmall: n,
                  classNames: {
                    icon: o()(
                      L[`icon__${t}`],
                      L[`icon__${t}${(0, h.e)(e)}`],
                      a && L.icon__selected,
                    ),
                  },
                }),
          T = {
            base: "FilterToggleGroup_base_69",
            title: "FilterToggleGroup_title_65",
            content: "FilterToggleGroup_content_80",
            toggle: "FilterToggleGroup_toggle_d4",
            base__inPopup: "FilterToggleGroup_base__inPopup_11",
          };
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
        let O;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(O || (O = {}));
        const P = ({ header: e, body: u, contentId: t, targetId: n }) =>
            t
              ? { contentId: t, targetId: n }
              : u || e
                ? { header: null != e ? e : void 0, body: null != u ? u : void 0 }
                : void 0,
          I = ({
            id: e,
            type: u,
            label: t,
            hasDiscount: n,
            filters: a,
            onClick: s,
            className: i,
            toggleProps: l,
            theme: c = O.Default,
          }) => {
            const d = c === O.InPopup;
            return r().createElement(
              "div",
              { className: o()(T.base, T[`base__${c}`], i) },
              d && r().createElement(p, { className: T.title, label: t, hasDiscount: n }),
              r().createElement(
                "div",
                { className: T.content },
                _.UI(a, ({ id: t, isSelected: n, tooltip: a, icon: i, counter: c }) =>
                  r().createElement(
                    m.l,
                    { key: t, tooltipArgs: P(a), className: T.toggle },
                    r().createElement(
                      A.C,
                      k({}, l, {
                        className: o()(T.toggle, null == l ? void 0 : l.className),
                        isActive: n,
                        onClick: () => (null == s ? void 0 : s(e, t)),
                        counter: c,
                      }),
                      r().createElement(N, { id: t, icon: i, type: u, isSmall: d, isSelected: n }),
                    ),
                  ),
                ),
              ),
            );
          };
        var H = t(9197),
          W = t(3215),
          G = t(4598),
          j = t(5175),
          Z = t(3946);
        const U = (0, W.q)()(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  amountInfo: e.object("amountInfo"),
                  filter: e.array("filter"),
                  filters: e.array("filter.filters"),
                },
                t = (0, Z.Om)(() => (0, j.c)(u.filter.get()), { equals: G.jv }),
                n = (0, Z.Om)(() => (0, j.c)(u.filters.get()), { equals: G.jv }),
                r = (0, Z.Om)(
                  () =>
                    (0, j.c)(u.filters.get()).filter((e) => "dismissed" === e.id && e.isSelected)
                      .length > 0,
                  { equals: G.jv },
                );
              return Object.assign({}, u, {
                computes: { getFilterGroup: t, getFilters: n, getIsRestoreFilter: r },
              });
            },
            ({ externalModel: e }) => ({
              search: e.createCallback((e) => ({ value: e }), "onSearch"),
              updateFilter: e.createCallback(
                (e, u) => ({ groupID: e, toggleID: u }),
                "onUpdateFilter",
              ),
              resetFilter: e.createCallbackNoArgs("onResetFilter"),
              updateSelectMode: e.createCallbackNoArgs("onSelectedModeChange"),
              onCancelSelection: e.createCallbackNoArgs("onCancelSelection"),
              onDismissOrRestore: e.createCallbackNoArgs("onDismissOrRestore"),
            }),
          ),
          z = U[0],
          V = U[1];
        var $ = t(3616),
          X = t(1037),
          q = t(9367);
        const K = "PopupButton_base_7c",
          Y = "PopupButton_popupButtonLabel_ed",
          J = "PopupButton_buttonIconWrapper_d7",
          Q = "PopupButton_buttonIcon_e0",
          ee = "PopupButton_buttonIcon__isHighlighted_84",
          ue = "PopupButton_discountAlert_c8",
          te = ({ isHighlighted: e, hasDiscountAlert: u, popoverDirection: t = X.IC.Bottom }) =>
            r().createElement(
              "div",
              { className: K },
              r().createElement(
                "div",
                { className: Y },
                R.strings.crew.filter.popup.button.title(),
              ),
              r().createElement(
                $.Z,
                {
                  contentId: R.views.lobby.crew.popovers.FilterPopoverView("resId"),
                  targetId: R.views.lobby.crew.widgets.FilterPanelWidget("resId"),
                  direction: t,
                },
                r().createElement(
                  "div",
                  { id: "popup_btn", className: J },
                  r().createElement(
                    A.C,
                    { type: s.L$.ghost, size: s.qE.small, isActive: e, hasIndicator: !1 },
                    r().createElement("div", { className: o()(Q, e && ee) }),
                  ),
                  u && r().createElement(q.Q, { className: ue }),
                ),
              ),
            );
        var ne = t(8018);
        const re = "ResetButton_base_58",
          ae = "ResetButton_button_a5",
          oe = "ResetButton_icon_4a",
          se = ({ isSelectMode: e, onClick: u }) =>
            r().createElement(
              "div",
              { className: re },
              r().createElement(
                c.i,
                e ? ne.Er : ne.Xd,
                r().createElement(
                  s.u5,
                  { mixClass: ae, onClick: u, type: s.L$.ghost, size: s.qE.small },
                  r().createElement("div", { className: oe }),
                ),
              ),
            ),
          ie = "default",
          le = "search",
          ce = "email",
          de = "password",
          Ee = "normal",
          me = "disabled",
          _e = "alert",
          Ae = "error",
          Fe = "medium",
          De = {
            [ie]: "",
            [ce]: R.strings.common.input.placeholder.email(),
            [le]: R.strings.common.input.placeholder.search(),
            [de]: R.strings.common.input.placeholder.password(),
          },
          Ce = { [ie]: "text", [ce]: "text", [le]: "text", [de]: "password" },
          ge = { [ie]: "", [ce]: "Invalid email", [le]: "", [de]: "" },
          pe = R.images.gui.maps.icons.components.input;
        function Be(e, u) {
          return (
            u !== ce ||
            (function (e) {
              const u = e.match(
                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
              );
              return Boolean(u);
            })(e)
          );
        }
        var he = t(7727);
        const fe = {
            base: "InputControl_base_68",
            base__focused: "InputControl_base__focused_aa",
            base__alert: "InputControl_base__alert_22",
            base__error: "InputControl_base__error_ff",
            base__done: "InputControl_base__done_a7",
            base__disabled: "InputControl_base__disabled_f8",
            input: "InputControl_input_93",
            base__small: "InputControl_base__small_85",
            base__medium: "InputControl_base__medium_a2",
            base__large: "InputControl_base__large_32",
            base__withIcon: "InputControl_base__withIcon_9e",
            input__search: "InputControl_input__search_85",
            disabled: "InputControl_disabled_78",
            placeholder: "InputControl_placeholder_e3",
            placeholder__search: "InputControl_placeholder__search_d5",
            icon: "InputControl_icon_13",
            icon__search: "InputControl_icon__search_57",
            clear: "InputControl_clear_bb",
          },
          ve = r().memo(
            ({
              componentId: e,
              value: u = "",
              type: t = ie,
              size: a = Fe,
              variant: s = Ee,
              placeholder: i = "",
              highlighted: l,
              withClear: c,
              selectOnFocus: d = !0,
              maxLength: E,
              iconSource: m,
              classMix: _,
              onMouseEnter: A,
              onMouseLeave: F,
              onMouseDown: D,
              onMouseUp: C,
              onClick: g,
              onChange: p,
              onClear: B,
              onFocus: h,
              onBlur: f,
            }) => {
              const v = (0, n.useState)(!1),
                b = v[0],
                w = v[1],
                x = (0, n.useRef)(null),
                S = (0, n.useRef)({ mouseOver: !1, mouseDown: !1 }),
                y = s !== me,
                M = (0, n.useCallback)(
                  (e) => {
                    y && (w(!0), h && h(e));
                  },
                  [y, h],
                ),
                L = (0, n.useCallback)(
                  (e) => {
                    y && !S.current.mouseOver && (w(!1), f && f(e));
                  },
                  [y, f],
                );
              (0, n.useEffect)(() => {
                y && b && d && x.current && x.current.select();
              }, [d, b, y]);
              const N = (0, n.useCallback)(
                  (e) => {
                    y && p && p(e.target.value);
                  },
                  [y, p],
                ),
                T = (0, n.useCallback)(
                  (e) => {
                    y && ((S.current.mouseOver = !0), A && A(e));
                  },
                  [y, A],
                ),
                R = (0, n.useCallback)(
                  (e) => {
                    y &&
                      x.current &&
                      (S.current.mouseDown && x.current.focus(),
                      (S.current.mouseOver = !1),
                      F && F(e));
                  },
                  [y, F],
                ),
                k = (0, n.useCallback)(
                  (e) => {
                    y && ((S.current.mouseDown = !0), D && D(e));
                  },
                  [y, D],
                ),
                O = (0, n.useCallback)(
                  (e) => {
                    y && ((S.current.mouseDown = !1), C && C(e));
                  },
                  [y, C],
                ),
                P = (0, n.useCallback)(
                  (e) => {
                    if (y && x.current) {
                      ((!b || (b && e.target !== x.current)) && x.current.focus(), g && g(e));
                    }
                  },
                  [b, y, g],
                ),
                I = i || De[t],
                H = Boolean(m),
                W = o()(
                  fe.base,
                  fe[`base__${a}`],
                  l && fe[`base__${s}`],
                  b && fe.base__focused,
                  H && fe.base__withIcon,
                  _,
                ),
                G = (0, n.useMemo)(() => (m ? { backgroundImage: `url(${m})` } : null), [m]),
                j = o()(fe.input, fe[`input__${t}`]),
                Z = o()(fe.icon, fe[`icon__${t}`]),
                U = o()(fe.placeholder, fe[`placeholder__${t}`]);
              return r().createElement(
                "div",
                {
                  id: e,
                  className: W,
                  onMouseEnter: T,
                  onMouseDown: k,
                  onMouseUp: O,
                  onMouseLeave: R,
                  onClick: P,
                },
                !y && r().createElement("div", { className: fe.disabled }),
                G && r().createElement("div", { style: G, className: Z }),
                r().createElement("input", {
                  ref: x,
                  className: j,
                  type: Ce[t],
                  value: u,
                  onChange: N,
                  disabled: !y,
                  onFocus: M,
                  onBlur: L,
                  maxLength: E,
                }),
                I && !u && !b && r().createElement("div", { className: U }, I),
                c &&
                  r().createElement("div", {
                    className: fe.clear,
                    onClick: (e) => {
                      (he.$.playClick(), B && B(e));
                    },
                    onMouseEnter: he.$.playHighlight,
                  }),
              );
            },
          ),
          be = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          we = ({ variant: e, show: u = !0, helperText: t, helperIcon: a, classMix: s }) => {
            const i = (0, n.useMemo)(() => {
                const u =
                  a ||
                  (function (e) {
                    return e === _e ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(e);
                return u && { backgroundImage: `url(${u})` };
              }, [a, e]),
              l = o()(be.base, u && be.base__shown),
              c = o()(be.message, be[`message__${e}`], s);
            return r().createElement(
              "div",
              { className: l },
              i && r().createElement("div", { className: be.icon, style: i }),
              r().createElement("div", { className: c }, t),
            );
          },
          xe = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          Se = [
            "componentId",
            "type",
            "variant",
            "size",
            "value",
            "tooltipArgs",
            "helperText",
            "isValidated",
            "showHelper",
            "error",
            "options",
            "onFocus",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseUp",
            "onMouseDown",
            "onChange",
            "classMix",
            "controlClassMix",
            "helperClassMix",
          ];
        function ye() {
          return (
            (ye =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            ye.apply(this, arguments)
          );
        }
        const Me = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          Le = (e) => {
            let u = e.componentId,
              t = e.type,
              a = void 0 === t ? ie : t,
              s = e.variant,
              i = void 0 === s ? Ee : s,
              l = e.size,
              c = void 0 === l ? Fe : l,
              d = e.value,
              E = e.tooltipArgs,
              _ = e.helperText,
              A = void 0 === _ ? "" : _,
              F = e.isValidated,
              D = void 0 === F || F,
              C = e.showHelper,
              g = void 0 === C || C,
              p = e.error,
              B = e.options,
              h = e.onFocus,
              f = e.onMouseEnter,
              v = e.onMouseLeave,
              b = e.onMouseUp,
              w = e.onMouseDown,
              x = e.onChange,
              S = e.classMix,
              y = e.controlClassMix,
              M = e.helperClassMix,
              L = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Se);
            const N = (0, n.useState)(d),
              T = N[0],
              R = N[1],
              k = (0, n.useState)(D),
              O = k[0],
              P = k[1],
              I = (0, n.useMemo)(() => Object.assign({}, Me, B), [B]),
              H = (0, n.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: d, type: a }),
              W = (0, n.useCallback)((e) => {
                e !== H.current.value &&
                  ((H.current.value = e), (H.current.isChangeHandled = !1), R(e));
              }, []),
              G = (0, n.useCallback)(
                (e) => {
                  let u = !0;
                  (I.performChangeValidation &&
                    (u = I.changesValidator ? I.changesValidator(e) : Be(e, H.current.type)),
                    x && x(e, u));
                },
                [x, I],
              ),
              j = (0, n.useCallback)(() => {
                H.current.debounceTimeout &&
                  (window.clearTimeout(H.current.debounceTimeout), (H.current.debounceTimeout = 0));
              }, []),
              Z = (0, n.useCallback)(() => W(""), [W]);
            (0, n.useEffect)(() => () => j(), [j]);
            const U = (0, n.useCallback)(
              (e) => {
                (j(),
                  I.debounceTime
                    ? (H.current.debounceTimeout = window.setTimeout(() => {
                        G(e);
                      }, I.debounceTime))
                    : G(e));
              },
              [G, j, I.debounceTime],
            );
            ((0, n.useEffect)(() => {
              H.current.isChangeHandled ||
                H.current.value !== T ||
                (U(H.current.value), (H.current.isChangeHandled = !0));
            }, [T, U]),
              (0, n.useEffect)(() => {
                (H.current.isChangeHandled &&
                  d !== H.current.value &&
                  ((H.current.value = d), R(d)),
                  (H.current.type = a));
              }, [d, a]),
              (0, n.useEffect)(() => {
                P(D);
              }, [D, i]));
            const z = (0, n.useCallback)((e) => f && f(e), [f]),
              V = (0, n.useCallback)(
                (e) => {
                  (I.disableHighlightOnFocus && O && P(!1), h && h(e));
                },
                [O, h, I.disableHighlightOnFocus],
              ),
              $ = (0, n.useCallback)((e) => b && b(e), [b]),
              X = (0, n.useCallback)((e) => w && w(e), [w]),
              q = (0, n.useCallback)((e) => v && v(e), [v]),
              K = (0, n.useMemo)(
                () =>
                  I.withTypeIcon
                    ? (function (e, u) {
                        return e === le ? pe.$dyn(`search_${u}`) : "";
                      })(a, c)
                    : "",
                [a, c, I.withTypeIcon],
              ),
              Y = A || ge[a],
              J = Boolean(T),
              Q = p ? Ae : i,
              ee = Boolean(p) || O,
              ue = (0, n.useMemo)(
                () => ("boolean" == typeof I.withClear ? J && I.withClear : J && a === le),
                [a, J, I],
              ),
              te = o()(xe.base, xe[`base__${c}`], xe[`base__${i}`], S);
            return r().createElement(
              "div",
              {
                id: u,
                className: te,
                onMouseEnter: z,
                onMouseDown: X,
                onMouseUp: $,
                onMouseLeave: q,
              },
              r().createElement(
                m.l,
                { tooltipArgs: E },
                r().createElement(
                  ve,
                  ye(
                    {
                      componentId: u ? `${u}-inputControl` : void 0,
                      iconSource: K,
                      size: c,
                      type: a,
                      variant: Q,
                      value: T,
                      withClear: ue,
                      highlighted: ee,
                      selectOnFocus: I.selectOnFocus,
                      maxLength: I.maxLength,
                      classMix: y,
                      onFocus: V,
                      onChange: W,
                      onClear: Z,
                    },
                    L,
                  ),
                ),
              ),
              Y &&
                r().createElement(
                  "div",
                  { className: xe.helper },
                  r().createElement(we, {
                    variant: Q,
                    show: g && (I.isPermanentHelper || ee),
                    helperText: p || Y,
                    helperIcon: I.helperIconSource,
                    classMix: M,
                  }),
                ),
            );
          },
          Ne = ({
            value: e,
            placeholder: u,
            tooltipHeader: t,
            onChange: n,
            className: a,
            tooltipBody: o,
          }) =>
            r().createElement(
              c.i,
              { header: null != t ? t : void 0, body: o, isEnabled: Boolean(t || o) },
              r().createElement(Le, {
                type: le,
                placeholder: null != u ? u : void 0,
                value: e,
                classMix: a,
                onChange: n,
              }),
            ),
          Te = {
            base: "FilterPanelWidgetApp_base_1c",
            titleWrapper: "FilterPanelWidgetApp_titleWrapper_1b",
            title: "FilterPanelWidgetApp_title_ad",
            filters: "FilterPanelWidgetApp_filters_0d",
            counterGlow: "FilterPanelWidgetApp_counterGlow_df",
            separator: "FilterPanelWidgetApp_separator_9e",
            filterLabel: "FilterPanelWidgetApp_filterLabel_5b",
            base__tankChange: "FilterPanelWidgetApp_base__tankChange_ff",
            base__memberChange: "FilterPanelWidgetApp_base__memberChange_18",
            popupButtonWrapper: "FilterPanelWidgetApp_popupButtonWrapper_4c",
            base__personalData: "FilterPanelWidgetApp_base__personalData_1d",
            search: "FilterPanelWidgetApp_search_0e",
            chooseButton: "FilterPanelWidgetApp_chooseButton_2b",
            button: "FilterPanelWidgetApp_button_8e",
            button__demobilize: "FilterPanelWidgetApp_button__demobilize_d8",
          };
        var Re = t(5415);
        const ke = R.strings.crew.filterPanel,
          Oe = (0, E.Pi)(({ popoverDirection: e }) => {
            const u = V(),
              t = u.model,
              n = u.controls,
              a = t.root.get(),
              E = a.hasDiscountAlert,
              m = a.isPopoverHighlighted,
              _ = a.isPopoverEnabled,
              A = a.searchTooltipBody,
              F = a.searchTooltipHeader,
              D = a.searchPlaceholder,
              C = a.searchString,
              g = a.isSearchEnabled,
              p = a.title,
              B = a.panelType,
              h = a.hasAppliedFilters,
              f = a.popoverTooltipHeader,
              v = a.popoverTooltipBody,
              b = a.isSelectedMode,
              w = a.isSelectButtonVisible,
              x = a.isSelectButtonActive,
              S = a.isSelectedLimitReached,
              y = t.amountInfo.get(),
              M = y.from,
              L = y.to,
              N = t.computes.getFilterGroup(),
              T = t.computes.getFilters(),
              k = t.computes.getIsRestoreFilter(),
              O = h || (0 === M && 0 === L) || b,
              P =
                (0, Re.GS)().mediaSize === Re.cJ.ExtraSmall && b
                  ? R.strings.crew.tankmanList.selected.titleSmall()
                  : p;
            return r().createElement(
              "div",
              { className: o()(Te.base, Te[`base__${B}`]) },
              r().createElement(
                "div",
                { className: Te.titleWrapper },
                r().createElement(H.C, {
                  title: P || "",
                  isGlowVisible: O,
                  isSelectedLimitReached: S,
                  isFilterRange: !0,
                  isSelectMode: b,
                  from: M,
                  to: L,
                  className: Te.title,
                  classNames: { counterGlow: Te.counterGlow },
                }),
                h && r().createElement(se, { isSelectMode: b, onClick: n.resetFilter }),
              ),
              r().createElement(
                "div",
                { className: Te.filters },
                g &&
                  r().createElement(
                    r().Fragment,
                    null,
                    r().createElement(Ne, {
                      value: C,
                      onChange: n.search,
                      className: Te.search,
                      placeholder: D,
                      tooltipHeader: F,
                      tooltipBody: A,
                    }),
                    B === d.Barracks && w && r().createElement("div", { className: Te.separator }),
                  ),
                N.label && r().createElement(l.ZP, { className: Te.filterLabel, text: N.label }),
                w &&
                  (b
                    ? r().createElement(
                        r().Fragment,
                        null,
                        r().createElement(
                          s.u5,
                          { mixClass: Te.button, type: i.L.primary, onClick: n.onCancelSelection },
                          r().createElement(l.ZP, { text: ke.demobilize.cancel() }),
                        ),
                        r().createElement(
                          s.u5,
                          {
                            mixClass: o()(Te.button, Te.button__demobilize),
                            type: i.L.main,
                            onClick: n.onDismissOrRestore,
                            disabled: !x,
                          },
                          r().createElement(l.ZP, {
                            text: k ? ke.restore.confirm() : ke.demobilize.confirm(),
                          }),
                        ),
                      )
                    : r().createElement(
                        s.u5,
                        { mixClass: Te.button, type: i.L.secondary, onClick: n.updateSelectMode },
                        r().createElement(l.ZP, { text: ke.selectMode.title() }),
                      )),
                (w || g) && r().createElement("div", { className: Te.separator }),
                r().createElement(I, {
                  id: N.id,
                  label: N.label,
                  type: N.type,
                  hasDiscount: N.hasDiscount,
                  filters: T,
                  toggleProps: { type: i.L.ghost },
                  onClick: n.updateFilter,
                }),
                _ &&
                  r().createElement(
                    c.i,
                    { header: f || void 0, body: v || void 0, isEnabled: Boolean(f || v) },
                    r().createElement(
                      "div",
                      { className: Te.popupButtonWrapper },
                      r().createElement(te, {
                        isHighlighted: m,
                        hasDiscountAlert: E,
                        popoverDirection: e,
                      }),
                    ),
                  ),
              ),
            );
          }),
          Pe = ({ popoverDirection: e }) =>
            r().createElement(
              z,
              { options: { rootId: R.views.lobby.crew.widgets.FilterPanelWidget("resId") } },
              r().createElement(Oe, { popoverDirection: e }),
            );
      },
      5026: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
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
        };
      },
      6880: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
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
      },
      8055: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
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
        };
      },
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = { base: "FormatText_base_d0" };
      },
      4769: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
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
      },
      3393: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
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
        };
      },
      4723: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          base: "ToggleButton_base_09",
          overlay: "ToggleButton_overlay_76",
          base__active: "ToggleButton_base__active_05",
          button: "ToggleButton_button_14",
          indicator: "ToggleButton_indicator_c2",
          counter: "ToggleButton_counter_86",
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
        var r = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [u, t, n] = deferred[i], a = !0, o = 0; o < u.length; o++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[o]))
              ? u.splice(o--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(i--, 1);
            var s = t();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > n; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [u, t, n];
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
    (__webpack_require__.j = 646),
    (() => {
      var e = { 646: 0, 595: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            r,
            [a, o, s] = t,
            i = 0;
          if (a.some((u) => 0 !== e[u])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (u && u(t); i < a.length; i++)
            ((r = a[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(2515));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
