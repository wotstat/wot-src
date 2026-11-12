(() => {
  var __webpack_modules__ = {
      3779: (e, t, n) => {
        "use strict";
        n.d(t, { ZP: () => p });
        var u = n(6483),
          a = n.n(u),
          r = n(9887),
          s = n.n(r),
          o = n(3377),
          i = n(6179),
          l = n.n(i),
          c = n(5026);
        const m = [
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
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        Object.keys(s());
        const _ = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          E = (Object.keys(_), ["mt", "mr", "mb", "ml"]),
          g = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          p = (0, o.ZP)((e) => {
            let t = e.className,
              n = e.width,
              u = e.height,
              r = e.m,
              s = e.mt,
              o = void 0 === s ? r : s,
              p = e.mr,
              b = void 0 === p ? r : p,
              h = e.mb,
              A = void 0 === h ? r : h,
              v = e.ml,
              C = void 0 === v ? r : v,
              f = e.column,
              D = e.row,
              F = e.flexDirection,
              B = void 0 === F ? (f ? "column" : D && "row") || void 0 : F,
              w = e.flexStart,
              k = e.center,
              y = e.flexEnd,
              S = e.spaceBetween,
              L = e.spaceAround,
              T = e.justifyContent,
              N =
                void 0 === T
                  ? (w ? "flex-start" : k && "center") ||
                    (y && "flex-end") ||
                    (S && "space-between") ||
                    (L && "space-around") ||
                    void 0
                  : T,
              I = e.alignItems,
              x =
                void 0 === I
                  ? (w ? "flex-start" : k && "center") || (y && "flex-end") || void 0
                  : I,
              M = e.alignSelf,
              R = e.wrap,
              P = e.flexWrap,
              O = void 0 === P ? (R ? "wrap" : void 0) : P,
              H = e.grow,
              W = e.shrink,
              G = e.flex,
              j = void 0 === G ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : G,
              z = e.style,
              $ = e.children,
              U = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, m);
            const V = (0, i.useMemo)(() => {
                const e = { mt: o, mr: b, mb: A, ml: C },
                  t = ((e) =>
                    E.reduce((t, n) => {
                      const u = e[n];
                      return u && "number" != typeof u ? t.concat(_[!0 === u ? "MD" : u][n]) : t;
                    }, []))(e),
                  a = ((e) =>
                    E.reduce((t, n) => {
                      const u = e[n];
                      return ("number" == typeof u && (t[g[n]] = u + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, z, a, {
                    width: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    height: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    flex: j,
                    alignSelf: M,
                    display: B || x ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: O,
                    justifyContent: N,
                    alignItems: x,
                  }),
                  computedClassNames: t,
                };
              }, [n, u, o, b, A, C, z, j, M, B, O, N, x]),
              Z = V.computedStyle,
              X = V.computedClassNames;
            return l().createElement(
              "div",
              d({ className: a()(c.Z.base, ...X, t), style: Z }, U),
              $,
            );
          });
      },
      3457: (e, t, n) => {
        "use strict";
        n.d(t, { L$: () => l.L, qE: () => l.q, u5: () => m });
        var u = n(6483),
          a = n.n(u),
          r = n(7727),
          s = n(6179),
          o = n.n(s),
          i = n(6880),
          l = n(2106);
        const c = ({
          children: e,
          size: t,
          isFocused: n,
          type: u,
          disabled: c,
          mixClass: m,
          soundHover: d,
          soundClick: _,
          onMouseEnter: E,
          onMouseMove: g,
          onMouseDown: p,
          onMouseUp: b,
          onMouseLeave: h,
          onClick: A,
        }) => {
          const v = (0, s.useRef)(null),
            C = (0, s.useState)(n),
            f = C[0],
            D = C[1],
            F = (0, s.useState)(!1),
            B = F[0],
            w = F[1],
            k = (0, s.useState)(!1),
            y = k[0],
            S = k[1],
            L = (0, s.useCallback)(() => {
              c || (v.current && (v.current.focus(), D(!0)));
            }, [c]),
            T = (0, s.useCallback)(
              (e) => {
                f && null !== v.current && !v.current.contains(e.target) && D(!1);
              },
              [f],
            ),
            N = (0, s.useCallback)(
              (e) => {
                c || (A && A(e));
              },
              [c, A],
            ),
            I = (0, s.useCallback)(
              (e) => {
                c || (null !== d && (0, r.G)(d), E && E(e), S(!0));
              },
              [c, d, E],
            ),
            x = (0, s.useCallback)(
              (e) => {
                g && g(e);
              },
              [g],
            ),
            M = (0, s.useCallback)(
              (e) => {
                c || (b && b(e), w(!1));
              },
              [c, b],
            ),
            P = (0, s.useCallback)(
              (e) => {
                c || (null !== _ && (0, r.G)(_), p && p(e), n && L(), w(!0));
              },
              [c, _, p, L, n],
            ),
            O = (0, s.useCallback)(
              (e) => {
                c || (h && h(e), w(!1));
              },
              [c, h],
            ),
            H = a()(
              i.Z.base,
              i.Z[`base__${u}`],
              {
                [i.Z.base__disabled]: c,
                [i.Z[`base__${t}`]]: t,
                [i.Z.base__focus]: f,
                [i.Z.base__highlightActive]: B,
                [i.Z.base__firstHover]: y,
              },
              m,
            ),
            W = a()(i.Z.state, i.Z.state__default);
          return (
            (0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", T),
                () => {
                  document.removeEventListener("mousedown", T);
                }
              ),
              [T],
            ),
            (0, s.useEffect)(() => {
              D(n);
            }, [n]),
            o().createElement(
              "div",
              {
                ref: v,
                className: H,
                onMouseEnter: I,
                onMouseMove: x,
                onMouseUp: M,
                onMouseDown: P,
                onMouseLeave: O,
                onClick: N,
              },
              u !== l.L.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: i.Z.back }),
                  o().createElement("span", { className: i.Z.texture }),
                ),
              o().createElement(
                "span",
                { className: W },
                o().createElement("span", { className: i.Z.stateDisabled }),
                o().createElement("span", { className: i.Z.stateHighlightHover }),
                o().createElement("span", { className: i.Z.stateHighlightActive }),
              ),
              o().createElement(
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
        const m = (0, s.memo)(c);
      },
      2106: (e, t, n) => {
        "use strict";
        let u, a;
        (n.d(t, { L: () => u, q: () => a }),
          (function (e) {
            ((e.main = "main"),
              (e.primary = "primary"),
              (e.primaryGreen = "primaryGreen"),
              (e.primaryRed = "primaryRed"),
              (e.secondary = "secondary"),
              (e.ghost = "ghost"));
          })(u || (u = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(a || (a = {})));
      },
      9987: (e, t, n) => {
        "use strict";
        n.d(t, { A: () => c });
        var u = n(6483),
          a = n.n(u),
          r = n(6179),
          s = n.n(r),
          o = n(8055);
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
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            l.apply(this, arguments)
          );
        }
        const c = (e) => {
          let t = e.size,
            n = e.value,
            u = e.isEmpty,
            r = e.fadeInAnimation,
            c = e.hide,
            m = e.maximumNumber,
            d = e.className,
            _ = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, i);
          const E = u ? null : n,
            g = "string" == typeof E;
          if ((E && !g && E < 0) || 0 === E) return null;
          const p = E && !g && E > m,
            b = a()(
              o.Z.base,
              o.Z[`base__${t}`],
              r && o.Z.base__animated,
              c && o.Z.base__hidden,
              !E && o.Z.base__pattern,
              u && o.Z.base__empty,
              d,
            );
          return s().createElement(
            "div",
            l({ className: b }, _),
            s().createElement("div", { className: o.Z.bg }),
            s().createElement("div", { className: o.Z.pattern }),
            s().createElement(
              "div",
              { className: a()(o.Z.value, g && o.Z.value__text) },
              p ? m : E,
              p && s().createElement("span", { className: o.Z.plus }, "+"),
            ),
          );
        };
        c.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
      },
      280: (e, t, n) => {
        "use strict";
        n.d(t, { z: () => l });
        var u = n(6179),
          a = n.n(u),
          r = n(6483),
          s = n.n(r),
          o = n(3649),
          i = n(5287);
        const l = ({ binding: e, text: t = "", classMix: n, alignment: r = o.v2.left }) =>
          null === t
            ? (console.error("FormatText was supplied with 'null'"), null)
            : a().createElement(
                u.Fragment,
                null,
                t.split("\n").map((t, l) =>
                  a().createElement(
                    "div",
                    { className: s()(i.Z.base, n), key: `${t}-${l}` },
                    (0, o.Uw)(t, r, e).map((e, t) =>
                      a().createElement(u.Fragment, { key: `${t}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, t, n) => {
        "use strict";
        n.d(t, { Y: () => m });
        var u = n(3138),
          a = n(6179),
          r = n(1043),
          s = n(5262);
        const o = u.O.client.getSize("rem"),
          i = o.width,
          l = o.height,
          c = Object.assign({ width: i, height: l }, (0, s.T)(i, l, r.j)),
          m = (0, a.createContext)(c);
      },
      1039: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => c });
        var u = n(6179),
          a = n.n(u),
          r = n(6536),
          s = n(3495),
          o = n(1043),
          i = n(5262),
          l = n(3138);
        const c = (0, u.memo)(({ children: e }) => {
          const t = (0, u.useContext)(s.Y),
            n = (0, u.useState)(t),
            c = n[0],
            m = n[1],
            d = (0, u.useCallback)((e, t) => {
              const n = l.O.view.pxToRem(e),
                u = l.O.view.pxToRem(t);
              m(Object.assign({ width: n, height: u }, (0, i.T)(n, u, o.j)));
            }, []);
          ((0, r.Z)(() => {
            engine.on("clientResized", d);
          }),
            (0, u.useEffect)(() => () => engine.off("clientResized", d), [d]));
          const _ = (0, u.useMemo)(() => Object.assign({}, c), [c]);
          return a().createElement(s.Y.Provider, { value: _ }, e);
        });
      },
      6010: (e, t, n) => {
        "use strict";
        var u = n(6179),
          a = n(7382),
          r = n(3495);
        const s = ["children"];
        const o = (e) => {
          let t = e.children,
            n = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, s);
          const o = (0, u.useContext)(r.Y),
            i = o.extraLarge,
            l = o.large,
            c = o.medium,
            m = o.small,
            d = o.extraSmall,
            _ = o.extraLargeWidth,
            E = o.largeWidth,
            g = o.mediumWidth,
            p = o.smallWidth,
            b = o.extraSmallWidth,
            h = o.extraLargeHeight,
            A = o.largeHeight,
            v = o.mediumHeight,
            C = o.smallHeight,
            f = o.extraSmallHeight,
            D = { extraLarge: h, large: A, medium: v, small: C, extraSmall: f };
          if (n.extraLarge || n.large || n.medium || n.small || n.extraSmall) {
            if (n.extraLarge && i) return t;
            if (n.large && l) return t;
            if (n.medium && c) return t;
            if (n.small && m) return t;
            if (n.extraSmall && d) return t;
          } else {
            if (n.extraLargeWidth && _) return (0, a.H)(t, n, D);
            if (n.largeWidth && E) return (0, a.H)(t, n, D);
            if (n.mediumWidth && g) return (0, a.H)(t, n, D);
            if (n.smallWidth && p) return (0, a.H)(t, n, D);
            if (n.extraSmallWidth && b) return (0, a.H)(t, n, D);
            if (!(
              n.extraLargeWidth ||
              n.largeWidth ||
              n.mediumWidth ||
              n.smallWidth ||
              n.extraSmallWidth
            )) {
              if (n.extraLargeHeight && h) return t;
              if (n.largeHeight && A) return t;
              if (n.mediumHeight && v) return t;
              if (n.smallHeight && C) return t;
              if (n.extraSmallHeight && f) return t;
            }
          }
          return null;
        };
        o.defaultProps = {
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
        (0, u.memo)(o);
      },
      7382: (e, t, n) => {
        "use strict";
        n.d(t, { H: () => u });
        const u = (e, t, n) =>
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
      },
      7739: (e, t, n) => {
        "use strict";
        n.d(t, { YN: () => a.Y, ZN: () => u.Z });
        n(6010);
        var u = n(1039),
          a = n(3495);
      },
      1043: (e, t, n) => {
        "use strict";
        n.d(t, { j: () => u });
        const u = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, n) => {
        "use strict";
        var u;
        function a(e, t, n) {
          const u = (function (e, t) {
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
            r = Math.min(u, a);
          return {
            extraLarge: r === n.extraLarge.weight,
            large: r === n.large.weight,
            medium: r === n.medium.weight,
            small: r === n.small.weight,
            extraSmall: r === n.extraSmall.weight,
            extraLargeWidth: u === n.extraLarge.weight,
            largeWidth: u === n.large.weight,
            mediumWidth: u === n.medium.weight,
            smallWidth: u === n.small.weight,
            extraSmallWidth: u === n.extraSmall.weight,
            extraLargeHeight: a === n.extraLarge.weight,
            largeHeight: a === n.large.weight,
            mediumHeight: a === n.medium.weight,
            smallHeight: a === n.small.weight,
            extraSmallHeight: a === n.extraSmall.weight,
          };
        }
        (n.d(t, { T: () => a }),
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
          })(u || (u = {})));
      },
      1037: (e, t, n) => {
        "use strict";
        n.d(t, { IC: () => u });
        var u,
          a = n(6483),
          r = n.n(a),
          s = n(6373),
          o = n(1856),
          i = n(3138),
          l = n(2039),
          c = n(5099),
          m = n(7727),
          d = n(4179),
          _ = n(6179),
          E = n.n(_),
          g = n(4769);
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(u || (u = {}));
        const p = ["__left", "__right", "__top", "__bottom"];
        (0, _.forwardRef)(
          (
            { children: e, disableAutoSizeUpdate: t, onOutsideClick: n, customStyles: u = {} },
            a,
          ) => {
            const b = (0, _.useRef)(null),
              h = (0, _.useRef)(null),
              A = (0, _.useRef)(null),
              v = (0, _.useState)(window.decorator && window.decorator.directionType),
              C = v[0],
              f = v[1],
              D = (0, _.useCallback)(() => {
                (m.$.playClick(), i.O.view.sendEvent.close());
              }, []),
              F = (0, _.useCallback)(() => {
                m.$.playHighlight();
              }, []),
              B = r()(g.Z.arrow, g.Z[`arrow${p[C]}`]);
            (0, l.b)(
              () => (
                i.O.client.events.mouse.enableOutside(),
                i.O.client.events.mouse.down(([, e]) => {
                  "outside" === e && (n ? n() : i.O.view.sendEvent.close("popover"));
                })
              ),
            );
            const w = (0, _.useCallback)(
                (e) => {
                  let t = e.target;
                  do {
                    if (t === b.current || t === A.current) return;
                    t = t.parentNode;
                  } while (t);
                  const u = window.decorator;
                  if (void 0 !== window.decorator) {
                    const e = i.O.client.getMouseGlobalPosition(),
                      t = ![u.boundX, u.boundY, u.boundWidth, u.boundHeight].includes(void 0),
                      n =
                        e.x < u.boundX ||
                        e.x > u.boundX + u.boundWidth ||
                        e.y > u.boundY + u.boundHeight ||
                        e.y < u.boundY;
                    if (t && !n) return;
                  }
                  n ? n() : i.O.view.sendEvent.close("popover");
                },
                [b, A, n],
              ),
              k = (0, _.useCallback)(
                () => (
                  i.O.view.freezeTextureBeforeResize(),
                  (0, o.v)(() => {
                    if (h.current) {
                      const e = h.current.scrollWidth,
                        t = h.current.scrollHeight;
                      (i.O.view.resize(e, t), f(window.decorator.directionType));
                    }
                  })
                ),
                [],
              );
            return (
              (0, _.useImperativeHandle)(a, () => ({ updateSize: k })),
              (0, l.b)(() => {
                i.O.view.setInputPaddingsRem(58);
              }),
              (0, _.useEffect)(() => {
                document.addEventListener("mousedown", w, { capture: !0 });
                const e = (0, c.B)((0, d.Eu)());
                return (
                  !t && e.promise.then(() => k()),
                  () => {
                    (e.cancel(), document.removeEventListener("mousedown", w));
                  }
                );
              }, [k, w, t]),
              E().createElement(
                "div",
                { className: g.Z.base, ref: h },
                E().createElement(
                  "div",
                  { className: g.Z.decorator },
                  E().createElement(
                    "div",
                    { className: g.Z.content, ref: b },
                    e,
                    window.decorator &&
                      window.decorator.isCloseBtnVisible &&
                      E().createElement(
                        s.i,
                        { body: R.strings.dialogs.common.error.cancel() },
                        E().createElement("div", {
                          className: g.Z.closeBtn,
                          onClick: D,
                          onMouseEnter: F,
                          ref: A,
                        }),
                      ),
                  ),
                  E().createElement("div", { className: B, style: u.arrow }),
                ),
              )
            );
          },
        );
      },
      3616: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => l });
        var u = n(1037),
          a = n(4179),
          r = n(6179),
          s = n.n(r);
        const o = [
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
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = (e) => {
          let t = e.contentId,
            n = e.decoratorId,
            l = e.direction,
            c = void 0 === l ? u.IC.Top : l,
            m = e.targetId,
            d = e.args,
            _ = e.onClick,
            E = e.children,
            g = e.isEnabled,
            p = void 0 === g || g,
            b = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, o);
          const h = (0, r.useRef)(null),
            A = (0, r.useCallback)(() => {
              if ((0, a.wU)()) return (0, a.SW)();
              h.current && (0, a.P3)(t, c, h.current, n, m, d);
            }, [t, c, d, n, m]);
          return s().createElement(
            "div",
            i(
              {
                ref: h,
                onClick:
                  ((v = E.props.onClick),
                  (e) => {
                    p && (A(), _ && _(e), v && v(e));
                  }),
              },
              b,
            ),
            E,
          );
          var v;
        };
      },
      7613: (e, t, n) => {
        "use strict";
        n.d(t, { ZP: () => F });
        var u = n(6483),
          a = n.n(u),
          r = n(3779),
          s = n(280),
          o = n(3532),
          i = n.n(o),
          l = n(9887),
          c = n.n(l),
          m = n(3377),
          d = n(6179),
          _ = n.n(d),
          E = n(3393);
        const g = [
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
        function p() {
          return (
            (p =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            p.apply(this, arguments)
          );
        }
        Object.keys(c());
        const b = Object.keys(i()),
          h = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          A = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          v = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          C = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          f =
            (Object.keys(C),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": h,
              "heading-H36": h,
              "heading-H28": A,
              "heading-H24": A,
              "heading-H24R": A,
              "heading-H22": A,
              "heading-H20R": A,
              "heading-H18": A,
              "heading-H15": v,
              "heading-H14": v,
              "paragraph-P24": A,
              "paragraph-P18": A,
              "paragraph-P16": A,
              "paragraph-P14": v,
              "paragraph-P12": v,
              "paragraph-P10": v,
            }),
          D =
            (Object.keys(f),
            (e) =>
              e
                ? ((e) => b.includes(e))(e)
                  ? { colorClassName: E.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          F = (0, m.ZP)((e) => {
            let t = e.text,
              n = e.variant,
              u = e.className,
              o = e.color,
              i = e.m,
              l = e.mt,
              c = void 0 === l ? i : l,
              m = e.mr,
              b = void 0 === m ? i : m,
              h = e.mb,
              A = void 0 === h ? i : h,
              v = e.ml,
              C = void 0 === v ? i : v,
              F = e.style,
              B = e.format,
              w = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, g);
            const k = (0, d.useMemo)(() => {
                const e = D(o),
                  t = e.colorClassName,
                  n = e.colorStyle,
                  u = void 0 === n ? {} : n;
                return { computedStyle: Object.assign({}, F, u), colorClassName: t };
              }, [F, o]),
              y = k.computedStyle,
              S = k.colorClassName;
            return _().createElement(
              r.ZP,
              p(
                {
                  className: a()(E.Z.base, n && E.Z[n], S, u),
                  style: y,
                  mt: !0 === c ? f[n || "paragraph-P16"].mt : c,
                  mr: !0 === b ? f[n || "paragraph-P16"].mr : b,
                  mb: !0 === A ? f[n || "paragraph-P16"].mb : A,
                  ml: !0 === C ? f[n || "paragraph-P16"].ml : C,
                },
                w,
              ),
              void 0 !== B ? _().createElement(s.z, p({}, B, { text: t })) : t,
            );
          });
      },
      7078: (e, t, n) => {
        "use strict";
        n.d(t, { t: () => i });
        var u = n(6179),
          a = n.n(u),
          r = n(2056);
        const s = ["children"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const i = (e) => {
          let t = e.children,
            n = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, s);
          return a().createElement(
            r.u,
            o(
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
        };
      },
      3415: (e, t, n) => {
        "use strict";
        n.d(t, { l: () => l });
        var u = n(6179),
          a = n.n(u),
          r = n(7078),
          s = n(6373),
          o = n(2056);
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: t, className: n }) => {
          if (!t) return e;
          const u = a().createElement("div", { className: n }, e);
          if (t.header || t.body) return a().createElement(s.i, t, u);
          const l = t.contentId,
            c = t.args,
            m = null == c ? void 0 : c.contentId;
          return l || m
            ? a().createElement(o.u, i({}, t, { contentId: l || m }), u)
            : a().createElement(r.t, t, u);
        };
      },
      6373: (e, t, n) => {
        "use strict";
        n.d(t, { i: () => l });
        var u = n(2056),
          a = n(6179),
          r = n.n(a);
        const s = ["children", "body", "header", "note", "alert", "args"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const i = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let t = e.children,
              n = e.body,
              l = e.header,
              c = e.note,
              m = e.alert,
              d = e.args,
              _ = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, s);
            const E = (0, a.useMemo)(() => {
              const e = Object.assign({}, d, { body: n, header: l, note: c, alert: m });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [m, n, l, c, d]);
            return r().createElement(
              u.u,
              o(
                {
                  contentId:
                    ((g = null == d ? void 0 : d.hasHtmlContent),
                    g ? i.SimpleTooltipHtmlContent("resId") : i.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                _,
              ),
              t,
            );
            var g;
          };
      },
      2056: (e, t, n) => {
        "use strict";
        n.d(t, { u: () => l });
        var u = n(7902),
          a = n(4179),
          r = n(6179);
        const s = [
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
        function o(e) {
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
        const i = (e, t, n = {}, u = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: a.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: u,
                },
                n,
              ),
            );
          },
          l = (e) => {
            let t = e.children,
              n = e.contentId,
              a = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onClick,
              _ = e.ignoreShowDelay,
              E = void 0 !== _ && _,
              g = e.ignoreMouseClick,
              p = void 0 !== g && g,
              b = e.decoratorId,
              h = void 0 === b ? 0 : b,
              A = e.isEnabled,
              v = void 0 === A || A,
              C = e.targetId,
              f = void 0 === C ? 0 : C,
              D = e.onShow,
              F = e.onHide,
              B = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, s);
            const w = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              k = (0, r.useMemo)(() => f || (0, u.F)().resId, [f]),
              y = (0, r.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (i(n, h, { isMouseEvent: !0, on: !0, arguments: o(a) }, k),
                  D && D(),
                  (w.current.isVisible = !0));
              }, [n, h, a, k, D]),
              S = (0, r.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    i(n, h, { on: !1 }, k),
                    w.current.isVisible && F && F(),
                    (w.current.isVisible = !1));
                }
              }, [n, h, k, F]),
              L = (0, r.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(w.current.prevTarget) && S();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", L, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", L, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === v && S();
              }, [v, S]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", S),
                  () => {
                    (window.removeEventListener("mouseleave", S), S());
                  }
                ),
                [S],
              ));
            return v
              ? (0, r.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((T = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(y, E ? 100 : 400)),
                            l && l(e),
                            T && T(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (S(), null == c || c(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === p && S(), null == d || d(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === p && S(), null == m || m(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    B,
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
      1856: (e, t, n) => {
        "use strict";
        n.d(t, { v: () => u });
        const u = (e) => {
          let t,
            n = null;
          return (
            (n = requestAnimationFrame(() => {
              n = requestAnimationFrame(() => {
                ((n = null), (t = e()));
              });
            })),
            () => {
              ("function" == typeof t && t(), null !== n && cancelAnimationFrame(n));
            }
          );
        };
      },
      8246: (e, t, n) => {
        "use strict";
        n.d(t, { U: () => o });
        var u = n(3138);
        function a(e, t) {
          var n = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (n) return (n = n.call(e)).next.bind(n);
          if (
            Array.isArray(e) ||
            (n = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return r(e, t);
              var n = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === n && e.constructor && (n = e.constructor.name);
              if ("Map" === n || "Set" === n) return Array.from(e);
              if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                return r(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            n && (e = n);
            var u = 0;
            return function () {
              return u >= e.length ? { done: !0 } : { done: !1, value: e[u++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function r(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var n = 0, u = new Array(t); n < t; n++) u[n] = e[n];
          return u;
        }
        const s = (e) => (0 === e ? window : window.subViews.get(e));
        function o({
          initializer: e = !0,
          rootId: t = 0,
          getRoot: n = s,
          context: r = "model",
        } = {}) {
          const o = new Map();
          function i(e, t = 0) {
            viewEnv.removeDataChangedCallback(e, t)
              ? o.delete(e)
              : console.error("Can't remove callback by id:", e);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (e, t, n) => {
              n.forEach((t) => {
                const n = o.get(t);
                void 0 !== n && n(e);
              });
            });
          });
          const l = (e) => {
            const u = n(t),
              a = r.split(".").reduce((e, t) => e[t], u);
            return "string" != typeof e || 0 === e.length
              ? a
              : e.split(".").reduce((e, t) => {
                  const n = e[t];
                  return "function" == typeof n ? n.bind(e) : n;
                }, a);
          };
          return {
            subscribe: (n, a) => {
              const s = "string" == typeof a ? `${r}.${a}` : r,
                i = u.O.view.addModelObserver(s, t, !0);
              return (o.set(i, n), e && n(l(a)), i);
            },
            readByPath: l,
            createCallback: (e, t) => {
              const n = l(t);
              return (...t) => {
                n(e(...t));
              };
            },
            createCallbackNoArgs: (e) => {
              const t = l(e);
              return () => {
                t();
              };
            },
            dispose: function () {
              for (var e, n = a(o.keys()); !(e = n()).done;) {
                i(e.value, t);
              }
            },
            unsubscribe: i,
          };
        }
      },
      3215: (e, t, n) => {
        "use strict";
        n.d(t, { q: () => i });
        var u = n(4598),
          a = n(9174),
          r = n(6179),
          s = n.n(r),
          o = n(8246);
        const i = () => (e, t) => {
          const n = (0, r.createContext)({});
          return [
            function ({ mode: i = "real", options: l, children: c, mocks: m }) {
              const d = (0, r.useRef)([]),
                _ = (n, r, s) => {
                  var i;
                  const l = o.U(r),
                    c =
                      "real" === n
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (i = null == s ? void 0 : s.getter) ? i : () => {},
                          }),
                    m = (e) =>
                      "mocks" === n ? (null == s ? void 0 : s.getter(e)) : c.readByPath(e),
                    _ = (e) => d.current.push(e),
                    E = e({
                      mode: n,
                      readByPath: m,
                      externalModel: c,
                      observableModel: {
                        array: (e, t) => {
                          const r = null != t ? t : m(e),
                            s = a.LO.box(r, { equals: u.jv });
                          return (
                            "real" === n &&
                              c.subscribe(
                                (0, a.aD)((e) => s.set(e)),
                                e,
                              ),
                            s
                          );
                        },
                        object: (e, t) => {
                          const r = null != t ? t : m(e),
                            s = a.LO.box(r, { equals: u.jv });
                          return (
                            "real" === n &&
                              c.subscribe(
                                (0, a.aD)((e) => s.set(e)),
                                e,
                              ),
                            s
                          );
                        },
                        primitives: (e, t) => {
                          const u = m(t);
                          if (Array.isArray(e)) {
                            const r = e.reduce((e, t) => ((e[t] = a.LO.box(u[t], {})), e), {});
                            return (
                              "real" === n &&
                                c.subscribe(
                                  (0, a.aD)((t) => {
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
                              s = Object.entries(r),
                              o = s.reduce((e, [t, n]) => ((e[n] = a.LO.box(u[t], {})), e), {});
                            return (
                              "real" === n &&
                                c.subscribe(
                                  (0, a.aD)((e) => {
                                    s.forEach(([t, n]) => {
                                      o[n].set(e[t]);
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
                    g = { mode: n, model: E, externalModel: c, cleanup: _ };
                  return {
                    model: E,
                    controls: "mocks" === n && s ? s.controls(g) : t(g),
                    externalModel: c,
                    mode: n,
                  };
                },
                E = (0, r.useRef)(!1),
                g = (0, r.useState)(i),
                p = g[0],
                b = g[1],
                h = (0, r.useState)(() => _(i, l, m)),
                A = h[0],
                v = h[1];
              return (
                (0, r.useEffect)(() => {
                  E.current ? v(_(p, l, m)) : (E.current = !0);
                }, [m, p, l]),
                (0, r.useEffect)(() => {
                  b(i);
                }, [i]),
                (0, r.useEffect)(
                  () => () => {
                    (A.externalModel.dispose(), d.current.forEach((e) => e()));
                  },
                  [A],
                ),
                s().createElement(n.Provider, { value: A }, c)
              );
            },
            () => (0, r.useContext)(n),
          ];
        };
      },
      527: (e, t, n) => {
        "use strict";
        (n.r(t), n.d(t, { mouse: () => o, onResize: () => r }));
        var u = n(2472),
          a = n(1176);
        const r = (0, u.E)("clientResized"),
          s = { down: (0, u.E)("mousedown"), up: (0, u.E)("mouseup"), move: (0, u.E)("mousemove") };
        const o = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, a.R)(!1);
          }
          function n() {
            e.enabled && (0, a.R)(!0);
          }
          function u() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", n))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", n))
              : (0, a.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, n) => (
              (t[n] = (function (t) {
                return (n) => {
                  e.listeners += 1;
                  let a = !0;
                  const r = `mouse${t}`,
                    o = s[t]((e) => n([e, "outside"]));
                  function i(e) {
                    n([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    u(),
                    () => {
                      a &&
                        (o(), window.removeEventListener(r, i), (e.listeners -= 1), u(), (a = !1));
                    }
                  );
                };
              })(n)),
              t
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), u());
            },
            enable() {
              ((e.enabled = !0), u());
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
      5959: (e, t, n) => {
        "use strict";
        (n.r(t),
          n.d(t, {
            events: () => u,
            getMouseGlobalPosition: () => r,
            getSize: () => a,
            graphicsQuality: () => s,
          }));
        var u = n(527);
        function a(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const s = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, n) => {
        "use strict";
        function u(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        n.d(t, { R: () => u });
      },
      2472: (e, t, n) => {
        "use strict";
        function u(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        n.d(t, { E: () => u });
      },
      3138: (e, t, n) => {
        "use strict";
        n.d(t, { O: () => a });
        var u = n(5959);
        const a = { view: n(7641), client: u };
      },
      3722: (e, t, n) => {
        "use strict";
        function u(e, t, n = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, n);
        }
        function a(e, t, n) {
          return `url(${u(e, t, n)})`;
        }
        (n.r(t), n.d(t, { getBgUrl: () => a, getTextureUrl: () => u }));
      },
      6112: (e, t, n) => {
        "use strict";
        n.d(t, { W: () => u });
        const u = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, n) => {
        "use strict";
        n.d(t, { U: () => a });
        var u = n(2472);
        const a = {
          onTextureFrozen: (0, u.E)("self.onTextureFrozen"),
          onTextureReady: (0, u.E)("self.onTextureReady"),
          onDomBuilt: (0, u.E)("self.onDomBuilt"),
          onLoaded: (0, u.E)("self.onLoaded"),
          onDisplayChanged: (0, u.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, u.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, u.E)("children.onAdded"),
            onLoaded: (0, u.E)("children.onLoaded"),
            onRemoved: (0, u.E)("children.onRemoved"),
            onAttached: (0, u.E)("children.onAttached"),
            onTextureReady: (0, u.E)("children.onTextureReady"),
            onRequestPosition: (0, u.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, n) => {
        "use strict";
        (n.r(t),
          n.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => o,
            children: () => u,
            displayStatus: () => a.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => k,
            forceTriggerMouseMove: () => F,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => B,
            getScale: () => p,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => C,
            isEventHandled: () => D,
            isFocused: () => v,
            pxToRem: () => b,
            remToPx: () => h,
            resize: () => _,
            sendEvent: () => s.qP,
            setAnimateWindow: () => A,
            setEventHandled: () => f,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => y,
          }));
        var u = n(3722),
          a = n(6112),
          r = n(6538),
          s = n(8566);
        function o(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, n, u = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, n, u);
        }
        function c(e, t, n) {
          return viewEnv.addDataChangedCallback(e, t, n);
        }
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function _(e, t, n = "px") {
          return "rem" === n ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: h(t.x), y: h(t.y) };
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
        function h(e) {
          return viewEnv.remToPx(e);
        }
        function A(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function v() {
          return viewEnv.isFocused();
        }
        function C() {
          return viewEnv.isClientAccessible();
        }
        function f() {
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
        const w = Object.keys(a.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === a.W[t]), e),
            {},
          ),
          k = {
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
      8566: (e, t, n) => {
        "use strict";
        n.d(t, { qP: () => l });
        const u = ["args"];
        const a = 2,
          r = 16,
          s = 32,
          o = 64,
          i = (e, t) => {
            const n = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                s = (function (e, t) {
                  if (null == e) return {};
                  var n,
                    u,
                    a = {},
                    r = Object.keys(e);
                  for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(t, u);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: n, type: e }, s, {
                      arguments:
                        ((a = r),
                        Object.entries(a).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: n, type: e }, s));
            }
            return viewEnv.handleViewEvent({ __Type: n, type: e });
            var a;
          },
          l = {
            close(e) {
              i("popover" === e ? a : s);
            },
            minimize() {
              i(o);
            },
            move(e) {
              i(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      4598: (e, t, n) => {
        "use strict";
        n.d(t, { jv: () => u });
        function u() {
          return !1;
        }
        console.log;
      },
      7902: (e, t, n) => {
        "use strict";
        n.d(t, { F: () => u });
        const u = (e = 1) => {
          const t = new Error().stack;
          let n,
            u = R.invalid("resId");
          return (
            t &&
              ((n = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== n &&
                window.subViews[n] &&
                (u = window.subViews[n].id)),
            { caller: n, stack: t, resId: u }
          );
        };
      },
      3377: (e, t, n) => {
        "use strict";
        n.d(t, { ZP: () => c });
        var u = n(5415),
          a = n(6179),
          r = n.n(a);
        const s = ["xl", "lg", "md", "sm", "xs"],
          o = (e) => e.includes("_") && ((e) => s.includes(e))(e.split("_").at(-1)),
          i = [u.cJ.ExtraLarge, u.cJ.Large, u.cJ.Medium, u.cJ.Small, u.cJ.ExtraSmall],
          l = (e, t) =>
            Object.keys(e).reduce((n, u) => {
              if (u in n) return n;
              if (o(u)) {
                const a = u.split("_").slice(0, -1).join("_");
                if (a in n) return n;
                const r = i.indexOf(t),
                  o = (-1 !== r ? s.slice(r) : [])
                    .map((e) => a + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  l = o ? e[o] : void 0;
                return ((n[a] = void 0 !== l ? l : e[a]), n);
              }
              const a = e[u];
              return (
                void 0 === a ||
                  ((e, t) => s.some((n) => void 0 !== t[`${e}_${n}`]))(u, e) ||
                  (n[u] = a),
                n
              );
            }, {}),
          c = (e, t = l) => {
            const n = (
              (e, t = l) =>
              (n) => {
                const s = (0, u.GS)().mediaSize,
                  o = (0, a.useMemo)(() => t(n, s), [n, s]);
                return r().createElement(e, o);
              }
            )(e, t);
            return r().memo((t) =>
              Object.keys(t).some((e) => o(e) && void 0 !== t[e])
                ? r().createElement(n, t)
                : r().createElement(e, t),
            );
          };
      },
      6536: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => a });
        var u = n(6179);
        const a = (e) => {
          const t = (0, u.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      5415: (e, t, n) => {
        "use strict";
        n.d(t, { Aq: () => i, GS: () => l, cJ: () => s, fd: () => o });
        var u = n(6179),
          a = n(7739),
          r = n(1043);
        let s, o, i;
        (!(function (e) {
          ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = r.j.small.width)] = "Small"),
            (e[(e.Medium = r.j.medium.width)] = "Medium"),
            (e[(e.Large = r.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
        })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.width)] = "Small"),
              (e[(e.Medium = r.j.medium.width)] = "Medium"),
              (e[(e.Large = r.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
          })(o || (o = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.height)] = "Small"),
              (e[(e.Medium = r.j.medium.height)] = "Medium"),
              (e[(e.Large = r.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.height)] = "ExtraLarge"));
          })(i || (i = {})));
        const l = () => {
          const e = (0, u.useContext)(a.YN),
            t = e.width,
            n = e.height,
            r = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return s.ExtraLarge;
                case e.large:
                  return s.Large;
                case e.medium:
                  return s.Medium;
                case e.small:
                  return s.Small;
                case e.extraSmall:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(e),
            l = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return o.ExtraLarge;
                case e.largeWidth:
                  return o.Large;
                case e.mediumWidth:
                  return o.Medium;
                case e.smallWidth:
                  return o.Small;
                case e.extraSmallWidth:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
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
            mediaSize: r,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: t,
            remScreenHeight: n,
          };
        };
      },
      2039: (e, t, n) => {
        "use strict";
        n.d(t, { b: () => a });
        var u = n(6179);
        const a = (e) => {
          (0, u.useEffect)(e, []);
        };
      },
      3112: (e, t, n) => {
        "use strict";
        n.d(t, { V: () => r });
        var u = n(6179),
          a = n(3138);
        const r = () => {
          const e = (0, u.useState)(a.O.view.getScale()),
            t = e[0],
            n = e[1];
          return (
            (0, u.useEffect)(() => {
              const e = () => {
                n(a.O.view.getScale());
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
        };
      },
      4489: (e, t, n) => {
        "use strict";
        n.d(t, { f: () => r });
        var u = n(5139),
          a = n(6179);
        function r(e, t, n) {
          const r = (0, a.useMemo)(() => (0, u.Z)(n, e), t);
          return ((0, a.useEffect)(() => r.cancel, [r]), r);
        }
      },
      5521: (e, t, n) => {
        "use strict";
        let u, a;
        (n.d(t, { n: () => u }),
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
          })(u || (u = {})),
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
      5175: (e, t, n) => {
        "use strict";
        n.d(t, { c: () => r });
        var u = n(9480);
        const a = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? u.UI(e, (e) => ("object" == typeof e ? a(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? a(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? a(t) : t]),
                    )
              : e,
          r = (e) => a(e);
      },
      9480: (e, t, n) => {
        "use strict";
        function u(e, t) {
          var n;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (n = e[t]) ? void 0 : n.value;
        }
        n.d(t, { U2: () => u, UI: () => r, sE: () => s });
        function a(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function r(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, n, u) => t(null == e ? void 0 : e.value, n, u));
        }
        function s(e, t) {
          for (let n = 0; n < e.length; n++) {
            const u = a(e[n]);
            if (t(u, n, e)) return u;
          }
        }
      },
      5099: (e, t, n) => {
        "use strict";
        n.d(t, { B: () => u });
        const u = (e) => {
          let t = !1;
          return {
            promise: new Promise((n, u) => {
              e.then((e) => !t && n(e)).catch((e) => !t && u(e));
            }),
            cancel() {
              t = !0;
            },
          };
        };
      },
      4385: (e, t, n) => {
        "use strict";
        n.d(t, { K: () => u });
        const u = (e, t) => {
          const n = [];
          for (let u = 0; u < e; u++) n.push(t(u));
          return n;
        };
      },
      9690: (e, t, n) => {
        "use strict";
        n.d(t, { HG: () => s });
        const u = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          a = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const r = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          s = (e) =>
            r
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let n = a.length - 1; n >= 0; n--)
                    for (; e >= a[n];) ((t += u[n]), (e -= a[n]));
                  return t;
                })(e);
      },
      7727: (e, t, n) => {
        "use strict";
        function u(e) {
          engine.call("PlaySound", e);
        }
        n.d(t, { $: () => a, G: () => u });
        const a = {
          playHighlight() {
            u("highlight");
          },
          playClick() {
            u("play");
          },
          playYes() {
            u("yes1");
          },
        };
      },
      3649: (e, t, n) => {
        "use strict";
        let u;
        function a(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        function r(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const n = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(n, -n)]);
          });
        }
        function s(e) {
          return e.replace(/-/g, "_");
        }
        function o(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (n.d(t, {
          BN: () => s,
          Eg: () => l,
          Uw: () => p,
          WU: () => a,
          e: () => o,
          uF: () => r,
          v2: () => u,
          z4: () => i,
        }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(u || (u = {})));
        const i = (e) => e.replace(/&nbsp;/g, " "),
          l = (e) => e.replace(/&zwnbsp;/g, "\ufeff"),
          c = (e, t, n) => {
            if (n % 2) {
              const n = e.pop();
              return [...e, n + t];
            }
            return [...e, t];
          },
          m = (e, t, n) => {
            if (0 === n) return [t];
            if (n % 2) return [...e, " " === t ? " " : t];
            {
              const n = e.pop();
              return [...e, n + t];
            }
          },
          d = (e, t, n = u.left) => e.split(t).reduce(n === u.left ? c : m, []),
          _ = (() => {
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
          E = ["zh_cn", "zh_sg", "zh_tw"],
          g = (e, t = u.left) => {
            const n = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return E.includes(n)
              ? _(e)
              : ((e, t = u.left) => {
                  let n = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = i(e);
                  return (d(r, /( )/, t).forEach((e) => (n = n.concat(d(e, a, u.left)))), n);
                })(e, t);
          },
          p = (e, t, n) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (n && e in n ? n[e] : g(e, t)));
      },
      5139: (e, t, n) => {
        "use strict";
        function u(e, t, n, u) {
          let a,
            r = !1,
            s = 0;
          function o() {
            a && clearTimeout(a);
          }
          function i(...i) {
            const l = this,
              c = Date.now() - s;
            function m() {
              ((s = Date.now()), n.apply(l, i));
            }
            r ||
              (u && !a && m(),
              o(),
              void 0 === u && c > e
                ? m()
                : !0 !== t &&
                  (a = setTimeout(
                    u
                      ? function () {
                          a = void 0;
                        }
                      : m,
                    void 0 === u ? e - c : e,
                  )));
          }
          return (
            "boolean" != typeof t && ((u = n), (n = t), (t = void 0)),
            (i.cancel = function () {
              (o(), (r = !0));
            }),
            i
          );
        }
        n.d(t, { Z: () => u });
      },
      1358: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => r });
        var u = n(3138);
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
            const r = u.O.view.addModelObserver(e, n, a);
            return (
              r > 0
                ? ((this._callbacks[r] = t),
                  n > 0 && (this._views[n] ? this._views[n].push(r) : (this._views[n] = [r])))
                : console.error("Can't add callback for model:", e),
              r
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
              const u = this._callbacks[n];
              void 0 !== u && u(e, t);
            });
          }
        }
        a.__instance = void 0;
        const r = a;
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
      4179: (e, t, n) => {
        "use strict";
        n.d(t, {
          Sw: () => r.Z,
          B0: () => i,
          c9: () => v,
          wU: () => F,
          ry: () => h,
          Eu: () => A,
          SW: () => f,
          P3: () => D,
        });
        class u {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: n }) => {
                  let u = e.target;
                  do {
                    if (u === t) return;
                    u = u.parentNode;
                  } while (u);
                  n();
                });
              }));
          }
          static get instance() {
            return (u.__instance || (u.__instance = new u()), u.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const n = e,
              u = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== n || t !== u,
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
        u.__instance = void 0;
        const a = u;
        var r = n(1358);
        const s = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, n) => userLocale.getTimeFormat(e, t, void 0 === n || n),
            getTimeString: (e, t, n) => userLocale.getTimeString(e, t, void 0 === n || n),
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
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = n(5521),
          E = n(3138);
        const g = ["args"];
        function p(e, t, n, u, a, r, s) {
          try {
            var o = e[r](s),
              i = o.value;
          } catch (e) {
            return void n(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(u, a);
        }
        const b = (e) => ({
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
                    n = arguments;
                  return new Promise(function (u, a) {
                    var r = e.apply(t, n);
                    function s(e) {
                      p(r, u, a, s, o, "next", e);
                    }
                    function o(e) {
                      p(r, u, a, s, o, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          A = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          v = (e, t) => {
            const n = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var n,
                    u,
                    a = {},
                    r = Object.keys(e);
                  for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(t, g);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: n, type: e }, r, {
                      arguments:
                        ((u = a),
                        Object.entries(u).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: n, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: n, type: e });
            var u;
          },
          C = () => v(i.CLOSE),
          f = () => v(i.POP_OVER, { on: !1 }),
          D = (e, t, n, u, a = R.invalid("resId"), r) => {
            const s = E.O.view.getViewGlobalPosition(),
              o = n.getBoundingClientRect(),
              l = o.x,
              c = o.y,
              m = o.width,
              d = o.height,
              _ = {
                x: E.O.view.pxToRem(l) + s.x,
                y: E.O.view.pxToRem(c) + s.y,
                width: E.O.view.pxToRem(m),
                height: E.O.view.pxToRem(d),
              };
            v(i.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: u || R.invalid("resId"),
              targetID: a,
              direction: t,
              bbox: b(_),
              on: !0,
              args: r,
            });
          },
          F = () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
          B = (e, t) => {
            e.keyCode === _.n.ESCAPE && t();
          };
        var w = n(7572);
        const k = a.instance,
          y = {
            DataTracker: r.Z,
            ViewModel: w.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: d,
            makeGlobalBoundingBox: b,
            sendMoveEvent: (e) => v(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: f,
            sendShowContextMenuEvent: (e, t, n = 0) => {
              v(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: n,
                args: t,
              });
            },
            sendShowPopOverEvent: D,
            addEscapeListener: (e) => {
              const t = (t) => B(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              B(e, C);
            },
            handleViewEvent: v,
            onBindingsReady: h,
            onLayoutReady: A,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: F,
            dumpViewModel: function e(t) {
              const n = {};
              if ("object" != typeof t) return t;
              for (const u in t)
                if (Object.prototype.hasOwnProperty.call(t, u)) {
                  const a = Object.prototype.toString.call(t[u]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = t[u];
                    n[u] = [];
                    for (let t = 0; t < a.length; t++) n[u].push({ value: e(a[t].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (n[u] = e(t[u]))
                      : (n[u] = t[u]);
                }
              return n;
            },
            ClickOutsideManager: k,
            SystemLocale: s,
            UserLocale: o,
          };
        window.ViewEnvHelper = y;
      },
      3458: (e, t, n) => {
        "use strict";
        let u;
        (n.d(t, { Z0: () => a, in: () => u, sx: () => r }),
          (function (e) {
            ((e[(e.NonSet = 0)] = "NonSet"),
              (e[(e.Debug = 10)] = "Debug"),
              (e[(e.Info = 20)] = "Info"),
              (e[(e.Warning = 30)] = "Warning"));
          })(u || (u = {})));
        const a = "tooltip_watched",
          r = 2;
        let s;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(s || (s = {}));
      },
      4828: (e, t, n) => {
        "use strict";
        n.d(t, { AB: () => d, D9: () => u, eX: () => r, sC: () => s, tL: () => a, x3: () => l });
        const u = "crew",
          a = 2e3;
        let r, s, o, i, l, c, m;
        (!(function (e) {
          ((e.Viewed = "viewed"), (e.Click = "click"));
        })(r || (r = {})),
          (function (e) {
            ((e.Hangar = "hangar"),
              (e.PersonalFile = "personal_file_view"),
              (e.PersonalData = "personal_data_view"),
              (e.ServiceRecord = "service_record_view"),
              (e.Barracks = "barracks_view"),
              (e.MemberChange = "member_change_view"),
              (e.QuickTraining = "quick_training_view"),
              (e.TankChange = "tank_change_view"));
          })(s || (s = {})),
          (function (e) {
            e.DocumentChange = "document_change_dialog";
          })(o || (o = {})),
          (function (e) {
            ((e.PremiumTooltip = "personal_file_view_premium_tooltip"),
              (e.MstlTooltip = "personal_file_view_mstl_tooltip"));
          })(i || (i = {})),
          (function (e) {
            ((e.ChangeButtonTooltip = "crew_widget_change_button_tooltip"),
              (e.MstlTooltip = "crew_widget_mstl_tooltip"),
              (e.SlotContextMenu = "crew_widget_slot_context_menu"),
              (e.CrewOperationsButton = "crew_widget_crew_operations_button"));
          })(l || (l = {})),
          (function (e) {
            ((e.FirstnameSelect = "document_change_dialog_firstname_select"),
              (e.Firstname = "document_change_dialog_firstname"),
              (e.LastnameSelect = "document_change_dialog_lastname_select"),
              (e.Lastname = "document_change_dialog_lastname"));
          })(c || (c = {})),
          (function (e) {
            e.CardContextMenu = "barracks_view_card_context_menu";
          })(m || (m = {})));
        const d = {
          [R.views.lobby.crew.personal_case.PersonalFileView("resId")]: s.PersonalFile,
          [R.views.lobby.crew.personal_case.PersonalDataView("resId")]: s.PersonalData,
          [R.views.lobby.crew.personal_case.ServiceRecordView("resId")]: s.ServiceRecord,
          [R.views.lobby.crew.BarracksView("resId")]: s.Barracks,
          [R.views.lobby.crew.HangarCrewWidget("resId")]: s.Hangar,
          [R.views.lobby.crew.MemberChangeView("resId")]: s.MemberChange,
          [R.views.lobby.crew.TankChangeView("resId")]: s.TankChange,
          [R.views.lobby.crew.QuickTrainingView("resId")]: s.QuickTraining,
        };
      },
      1943: (e, t, n) => {
        "use strict";
        n.d(t, { Jp: () => m, Sr: () => _ });
        var u = n(6179),
          a = n(3458);
        const r = ["action", "timeLimit"];
        const s = "metrics",
          o = () => Date.now(),
          i = ({ partnerID: e, item: t, parentScreen: n, itemState: u, info: a }) => ({
            item: t,
            partnerID: e || null,
            parent_screen: n || null,
            item_state: u || null,
            additional_info: a || null,
          }),
          l = (e, t) => {
            const n = (0, u.useCallback)(
              (n, u = a.in.Info, r) => {
                (r || (r = {}),
                  Object.keys(r).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: t,
                      action: n,
                      logLevel: u,
                      params: JSON.stringify(r),
                    }));
              },
              [e, t],
            );
            return (e, t, u) => n(e, t, u);
          },
          c = (e, t) => {
            const n = l(e, t),
              a = (0, u.useRef)(new Map()),
              r = (0, u.useRef)(new Map()),
              s = (0, u.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  (void 0 !== t && t > 0) || a.current.set(e, o());
                },
                [a],
              ),
              i = (0, u.useCallback)(() => {
                (a.current.clear(), r.current.clear());
              }, [a, r]),
              c = (0, u.useCallback)(
                (e) => {
                  e &&
                    void 0 !== a.current.get(e) &&
                    void 0 === r.current.get(e) &&
                    r.current.set(e, o());
                },
                [a, r],
              ),
              m = (0, u.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  if (void 0 === t) return;
                  const n = r.current.get(e);
                  if (void 0 === n) return;
                  r.current.delete(e);
                  const u = o() - n;
                  a.current.set(e, t + u);
                },
                [a, r],
              ),
              d = (0, u.useCallback)(
                (e, t = 0, u, s) => {
                  const i = a.current.get(e);
                  if (void 0 === i) return;
                  (void 0 !== r.current.get(e) && m(e), a.current.delete(e));
                  const l = (o() - i) / 1e3;
                  l <= t ||
                    ((s = ((e, t) => (void 0 === e && (e = {}), (e.timeSpent = t), e))(s, l)),
                    n(e, u, s));
                },
                [a, r, n, m],
              );
            return [
              (e) => s(e),
              (e, t, n, u) => d(e, t, n, u),
              () => i(),
              (e) => c(e),
              (e) => m(e),
            ];
          },
          m = (e) => {
            const t = l(e, s),
              n = (0, u.useCallback)(
                (e) => {
                  t(e.action, e.logLevel, i(e));
                },
                [t],
              );
            return (e) => n(e);
          },
          d = (e) => {
            const t = c(e, s),
              n = t[0],
              a = t[1],
              r = t[2],
              o = t[3],
              l = t[4],
              m = (0, u.useCallback)(
                (e) => {
                  const t = e.action,
                    n = e.timeLimit,
                    u = e.logLevel;
                  a(t, n, u, i(e));
                },
                [a],
              );
            return [(e) => n(e), (e) => m(e), () => r(), (e) => o(e), (e) => l(e)];
          },
          _ = (e, t) => {
            const n = d(e),
              s = n[0],
              o = n[1],
              i = t.action,
              l = t.timeLimit,
              c = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(t, r);
            return (0, u.useMemo)(
              () => ({
                onShow: () => s(i || a.Z0),
                onHide: () => o(Object.assign({ action: i || a.Z0, timeLimit: l || a.sx }, c)),
              }),
              [i, l, c, s, o],
            );
          };
      },
      2258: (e, t, n) => {
        "use strict";
        var u = {};
        (n.r(u),
          n.d(u, {
            Area: () => pe,
            Bar: () => _e,
            DefaultScroll: () => ge,
            Direction: () => Y,
            defaultSettings: () => Q,
            useHorizontalScrollApi: () => ee,
          }));
        var a = {};
        (n.r(a),
          n.d(a, {
            Area: () => xe,
            Bar: () => Te,
            Default: () => Ie,
            useVerticalScrollApi: () => be,
          }));
        var r = n(7739),
          s = n(6179),
          o = n.n(s),
          i = n(6483),
          l = n.n(i),
          c = n(926),
          m = n.n(c),
          d = n(5415);
        const _ = ["children", "className"];
        function E() {
          return (
            (E =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            E.apply(this, arguments)
          );
        }
        const g = {
            [d.fd.ExtraSmall]: "",
            [d.fd.Small]: m().SMALL_WIDTH,
            [d.fd.Medium]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH}`,
            [d.fd.Large]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH}`,
            [d.fd.ExtraLarge]:
              `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH} ${m().EXTRA_LARGE_WIDTH}`,
          },
          p = {
            [d.Aq.ExtraSmall]: "",
            [d.Aq.Small]: m().SMALL_HEIGHT,
            [d.Aq.Medium]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT}`,
            [d.Aq.Large]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT}`,
            [d.Aq.ExtraLarge]:
              `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT} ${m().EXTRA_LARGE_HEIGHT}`,
          },
          b = {
            [d.cJ.ExtraSmall]: "",
            [d.cJ.Small]: m().SMALL,
            [d.cJ.Medium]: `${m().SMALL} ${m().MEDIUM}`,
            [d.cJ.Large]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE}`,
            [d.cJ.ExtraLarge]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE} ${m().EXTRA_LARGE}`,
          },
          h = (e) => {
            let t = e.children,
              n = e.className,
              u = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, _);
            const a = (0, d.GS)(),
              r = a.mediaWidth,
              s = a.mediaHeight,
              i = a.mediaSize;
            return o().createElement("div", E({ className: l()(n, g[r], p[s], b[i]) }, u), t);
          },
          A = ["children"];
        const v = (e) => {
          let t = e.children,
            n = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, A);
          return o().createElement(r.ZN, null, o().createElement(h, n, t));
        };
        var C = n(493),
          f = n.n(C),
          D = n(1037),
          F = n(3138),
          B = n(5521),
          w = n(4179);
        const k = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function y(e = B.n.NONE, t = k, n = !1) {
          (0, s.useEffect)(() => {
            if (e !== B.n.NONE)
              return (
                window.addEventListener("keydown", u, n),
                () => {
                  window.removeEventListener("keydown", u, n);
                }
              );
            function u(u) {
              if (u.keyCode === e) {
                if (F.O.view.isEventHandled()) return;
                (F.O.view.setEventHandled(), t(u), n && u.stopPropagation());
              }
            }
          }, [t, e, n]);
        }
        var S = n(3649),
          L = n(3403),
          T = n(3215);
        let N, I, x, M;
        (!(function (e) {
          ((e.Initialization = "initialization"),
            (e.Loading = "loading"),
            (e.ForceLoading = "forceLoading"),
            (e.Loaded = "loaded"));
        })(N || (N = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.Loading = "loading"),
              (e.Loaded = "loaded"),
              (e.Failed = "failed"));
          })(I || (I = {})),
          (function (e) {
            ((e.Initialization = "initialization"), (e.Loaded = "loaded"), (e.Failed = "failed"));
          })(x || (x = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.BrowserLoading = "browserLoading"),
              (e.PageLoading = "pageLoading"),
              (e.ForceLoading = "forceLoading"),
              (e.PageFailed = "pageFailed"),
              (e.TextureFailed = "textureFailed"),
              (e.Loaded = "loaded"));
          })(M || (M = {})));
        (N.Initialization, I.Initialization);
        const P = (0, T.q)()(
            ({ observableModel: e }) => {
              const t = { groups: e.array("groups", []) };
              return Object.assign({}, t);
            },
            ({ externalModel: e }) => ({
              onGroupClick: e.createCallback((e) => ({ groupName: e }), "onGroupClick"),
            }),
          ),
          O = P[0],
          H = P[1];
        var W = n(1856);
        const G = (e, t, n) => (n < e ? e : n > t ? t : n),
          j = [];
        function z(e) {
          const t = (0, s.useRef)(e);
          return (
            (0, s.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, s.useCallback)((...e) => (0, t.current)(...e), j)
          );
        }
        function $(e, t, n = []) {
          const u = (0, s.useRef)(0),
            a = (0, s.useCallback)(() => window.clearInterval(u.current), n || []);
          (0, s.useEffect)(() => a, [a]);
          const r = (null != n ? n : []).concat([t]);
          return [
            (0, s.useCallback)((n) => {
              ((u.current = window.setInterval(() => e(n, !0), t)), e(n, !1));
            }, r),
            a,
          ];
        }
        var U = n(7727);
        function V(e, t) {
          var n = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (n) return (n = n.call(e)).next.bind(n);
          if (
            Array.isArray(e) ||
            (n = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Z(e, t);
              var n = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === n && e.constructor && (n = e.constructor.name);
              if ("Map" === n || "Set" === n) return Array.from(e);
              if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                return Z(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            n && (e = n);
            var u = 0;
            return function () {
              return u >= e.length ? { done: !0 } : { done: !1, value: e[u++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Z(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var n = 0, u = new Array(t); n < t; n++) u[n] = e[n];
          return u;
        }
        const X = () => {
          const e = (0, s.useMemo)(() => ({}), []),
            t = (t) => (e[t] || (e[t] = new Map()), e[t]),
            n = (e, n) => {
              t(e).set(n, n);
            },
            u = (e, n) => {
              t(e).delete(n);
            },
            a = (e, ...n) => {
              for (var u, a = V(t(e).values()); !(u = a()).done;) {
                (0, u.value)(...n);
              }
            };
          return (0, s.useMemo)(() => ({ on: n, off: u, trigger: a }), []);
        };
        var q = n(4489),
          K = n(7030);
        let Y;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Y || (Y = {}));
        const Q = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          J = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: n,
            getDirection: u,
            getWrapperSize: a,
            triggerMouseMoveOnUpdate: r = !1,
          }) => {
            const o = (e, n) => {
              const u = t(e),
                a = u[0],
                r = u[1];
              return G(a, r, n);
            };
            return (i = {}) => {
              const l = i.settings,
                c = void 0 === l ? Q : l,
                m = (0, s.useRef)(null),
                d = (0, s.useRef)(null),
                _ = X(),
                E = (0, q.f)(
                  () => {
                    F.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                g = (0, K.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = m.current;
                    t && (n(t, e), _.trigger("change", e), r && E());
                  },
                  onRest: (e) => _.trigger("rest", e),
                  onStart: (e) => _.trigger("start", e),
                  onPause: (e) => _.trigger("pause", e),
                })),
                p = g[0],
                b = g[1],
                h = (0, s.useCallback)(
                  (e, t, n) => {
                    var u;
                    const a = p.scrollPosition.get(),
                      r = (null != (u = p.scrollPosition.goal) ? u : 0) - a;
                    return o(e, t * n + r + a);
                  },
                  [p.scrollPosition],
                ),
                A = (0, s.useCallback)(
                  (e, { immediate: t = !1, reset: n = !0 } = {}) => {
                    const u = m.current;
                    u &&
                      b.start({
                        scrollPosition: o(u, e),
                        immediate: t,
                        reset: n,
                        config: c.animationConfig,
                        from: { scrollPosition: o(u, p.scrollPosition.get()) },
                      });
                  },
                  [b, c.animationConfig, p.scrollPosition],
                ),
                v = (0, s.useCallback)(
                  (e) => {
                    const t = m.current,
                      n = d.current;
                    if (!t || !n) return;
                    const u = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return a(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(n, c.step),
                      r = h(t, e, u);
                    A(r);
                  },
                  [A, h, c.step],
                ),
                C = (0, s.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && v(u(e)),
                      m.current && _.trigger("mouseWheel", e, p.scrollPosition, t(m.current)));
                  },
                  [p.scrollPosition, v, _],
                ),
                f = ((e, t = []) => {
                  const n = (0, s.useRef)(),
                    u = (0, s.useCallback)((...t) => {
                      (n.current && n.current(), (n.current = e(...t)));
                    }, t);
                  return (
                    (0, s.useEffect)(
                      () => () => {
                        n.current && n.current();
                      },
                      [u],
                    ),
                    u
                  );
                })(
                  () =>
                    (0, W.v)(() => {
                      const e = m.current;
                      e &&
                        (A(o(e, p.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [A, p.scrollPosition.goal],
                ),
                D = z(() => {
                  const e = m.current;
                  if (!e) return;
                  const t = o(e, p.scrollPosition.goal);
                  (t !== p.scrollPosition.goal && A(t, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", f),
                  () => {
                    window.removeEventListener("resize", f);
                  }
                ),
                [f],
              );
              const B = (0, s.useCallback)((e) => _.trigger("isThumbDraggingChanged", e), [_]);
              return (0, s.useMemo)(
                () => ({
                  getWrapperSize: () => (d.current ? a(d.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? t(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: c.step.clampedArrowStepTimeout,
                  clampPosition: o,
                  handleMouseWheel: C,
                  applyScroll: A,
                  applyStepTo: v,
                  contentRef: m,
                  wrapperRef: d,
                  scrollPosition: b,
                  animationScroll: p,
                  recalculateContent: D,
                  handleIsThumbDragging: B,
                  events: { on: _.on, off: _.off },
                }),
                [p.scrollPosition, A, v, B, _.off, _.on, D, C, b, c.step.clampedArrowStepTimeout],
              );
            };
          },
          ee = J({
            getBounds: (e) => {
              var t, n;
              return [
                0,
                e.offsetWidth -
                  (null != (t = null == (n = e.parentElement) ? void 0 : n.offsetWidth) ? t : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, t) => {
              e.style.transform = `translateX(-${t.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? Y.Next : Y.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          te = "HorizontalBar_base_49",
          ne = "HorizontalBar_base__nonActive_82",
          ue = "HorizontalBar_leftButton_5f",
          ae = "HorizontalBar_rightButton_03",
          re = "HorizontalBar_track_0d",
          se = "HorizontalBar_thumb_fd",
          oe = "HorizontalBar_rail_32",
          ie = "disable",
          le = { pending: !1, offset: 0 },
          ce = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          me = () => {},
          de = (e, t) => Math.max(20, e.offsetWidth * t),
          _e = (0, s.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: n = ce, onDrag: u = me }) => {
              const a = (0, s.useRef)(null),
                r = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                d = e.stepTimeout || 100,
                _ = (0, s.useState)(le),
                E = _[0],
                g = _[1],
                p = (0, s.useCallback)(
                  (e) => {
                    (g(e),
                      m.current &&
                        u({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [u],
                ),
                b = () => {
                  const t = c.current,
                    n = m.current,
                    u = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(u && t && n && a)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, u / a),
                    l = G(0, 1, s / (a - u)),
                    d = (t.offsetWidth - de(t, o)) * l;
                  ((n.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (r.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (r.current.classList.add(ie), void i.current.classList.remove(ie));
                        if (
                          ((t = c.current),
                          (n = m.current),
                          e - (t.offsetWidth - n.offsetWidth) >= -0.5)
                        )
                          return (r.current.classList.remove(ie), void i.current.classList.add(ie));
                        var t, n;
                        (r.current.classList.remove(ie), i.current.classList.remove(ie));
                      }
                    })(d));
                },
                h = z(() => {
                  ((() => {
                    const t = m.current,
                      n = c.current,
                      u = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && u && n)) return;
                    const s = Math.min(1, u / r);
                    ((t.style.width = `${de(n, s)}px`),
                      (t.style.display = "flex"),
                      a.current &&
                        (1 === s ? a.current.classList.add(ne) : a.current.classList.remove(ne)));
                  })(),
                    b());
                });
              ((0, s.useEffect)(() => (0, W.v)(h)),
                (0, s.useEffect)(
                  () =>
                    (0, W.v)(() => {
                      const t = () => {
                        b();
                      };
                      let n = me;
                      const u = () => {
                        (n(), (n = (0, W.v)(h)));
                      };
                      return (
                        e.events.on("recalculateContent", h),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", u),
                        () => {
                          (n(),
                            e.events.off("recalculateContent", h),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", u));
                        }
                      );
                    }),
                  [e],
                ),
                (0, s.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      var n;
                      const a = e.contentRef.current;
                      if (!a) return;
                      const r = c.current,
                        s = m.current;
                      if (!a || !r || !s) return;
                      const o = t.screenX - E.offset - r.getBoundingClientRect().x,
                        i = (o / r.offsetWidth) * (null != (n = e.getContainerSize()) ? n : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(a, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        u({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                    },
                    n = () => {
                      (window.removeEventListener("mousemove", t), p(le));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", n),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", n));
                    }
                  );
                }, [e, E.offset, E.pending, u, p]));
              const A = $((t) => e.applyStepTo(t), d, [e]),
                v = A[0],
                C = A[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", C, !0),
                  () => document.removeEventListener("mouseup", C, !0)
                ),
                [C],
              );
              const f = (e) => {
                e.target.classList.contains(ie) || (0, U.G)("highlight");
              };
              return o().createElement(
                "div",
                { className: l()(te, t.base), ref: a, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: l()(ue, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(ie) ||
                      0 !== e.button ||
                      ((0, U.G)("play"), v(Y.Next));
                  },
                  onMouseUp: C,
                  ref: r,
                  onMouseEnter: f,
                }),
                o().createElement(
                  "div",
                  {
                    className: l()(re, t.track),
                    onMouseDown: (t) => {
                      const u = m.current;
                      if (u && 0 === t.button)
                        if (((0, U.G)("play"), t.target === u))
                          p({ pending: !0, offset: t.screenX - u.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const u = m.current,
                              a = e.contentRef.current;
                            if (!u || !a) return;
                            const r = n(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * t);
                          })(t.screenX > u.getBoundingClientRect().x ? Y.Prev : Y.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: f,
                  },
                  o().createElement("div", { ref: m, className: l()(se, t.thumb) }),
                  o().createElement("div", { className: l()(oe, t.rail) }),
                ),
                o().createElement("div", {
                  className: l()(ae, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(ie) ||
                      0 !== e.button ||
                      ((0, U.G)("play"), v(Y.Prev));
                  },
                  onMouseUp: C,
                  ref: i,
                  onMouseEnter: f,
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
            className: n,
            barClassNames: u,
            areaClassName: a,
            classNames: r,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = u || {};
                return Object.assign({}, e, { base: l()(Ee.base, e.base) });
              }, [u]),
              _ = (0, s.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: l()(Ee.defaultScroll, n), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Ee.defaultScrollArea, a) },
                o().createElement(pe, { className: i, api: _, classNames: r }, e),
              ),
              o().createElement(_e, { getStepByRailClick: c, api: t, onDrag: m, classNames: d }),
            );
          },
          pe = ({ api: e, className: t, classNames: n, children: u, style: a }) => (
            (0, s.useEffect)(() => (0, W.v)(e.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Ee.base, t), style: a },
              o().createElement(
                "div",
                {
                  className: l()(Ee.wrapper, null == n ? void 0 : n.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: l()(Ee.content, null == n ? void 0 : n.content), ref: e.contentRef },
                  u,
                ),
              ),
            )
          );
        ((pe.Bar = _e),
          (pe.Default = ge),
          (pe.SeniorityAwards = ({ api: e, className: t, classNames: n, children: u }) => (
            (0, s.useEffect)(() => (0, W.v)(e.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Ee.base, t) },
              o().createElement(
                "div",
                { className: l()(Ee.wrapper, null == n ? void 0 : n.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: l()(Ee.content, null == n ? void 0 : n.content), ref: e.contentRef },
                  u,
                ),
              ),
            )
          )));
        const be = J({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Y.Next : Y.Prev),
          }),
          he = "VerticalBar_base_f3",
          Ae = "VerticalBar_base__nonActive_42",
          ve = "VerticalBar_topButton_d7",
          Ce = "VerticalBar_bottomButton_06",
          fe = "VerticalBar_track_df",
          De = "VerticalBar_thumb_32",
          Fe = "VerticalBar_rail_43",
          Be = "disable",
          we = () => {},
          ke = { pending: !1, offset: 0 },
          ye = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Se = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          Le = (e, t) => Math.max(20, e.offsetHeight * t),
          Te = (0, s.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: n = ye, onDrag: u = we }) => {
              const a = (0, s.useRef)(null),
                r = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                d = e.stepTimeout || 100,
                _ = (0, s.useState)(ke),
                E = _[0],
                g = _[1],
                p = (0, s.useCallback)(
                  (e) => {
                    (g(e),
                      m.current &&
                        u({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [u],
                ),
                b = z(() => {
                  const t = m.current,
                    n = c.current,
                    u = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(u && r && t && n)) return;
                  const s = Math.min(1, u / r);
                  return (
                    (t.style.height = `${Le(n, s)}px`),
                    t.classList.add(De),
                    a.current &&
                      (1 === s ? a.current.classList.add(Ae) : a.current.classList.remove(Ae)),
                    s
                  );
                }),
                h = z(() => {
                  const t = c.current,
                    n = m.current,
                    u = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(u && t && n && a)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, u / a),
                    l = G(0, 1, s / (a - u)),
                    d = (t.offsetHeight - Le(t, o)) * l;
                  ((n.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (r.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (r.current.classList.add(Be), void i.current.classList.remove(Be));
                        if (
                          ((t = c.current),
                          (n = m.current),
                          e - (t.offsetHeight - n.offsetHeight) >= -0.5)
                        )
                          return (r.current.classList.remove(Be), void i.current.classList.add(Be));
                        var t, n;
                        (r.current.classList.remove(Be), i.current.classList.remove(Be));
                      }
                    })(d));
                }),
                A = z(() => {
                  Se(e, () => {
                    (b(), h());
                  });
                });
              ((0, s.useEffect)(() => (0, W.v)(A)),
                (0, s.useEffect)(() => {
                  const t = () => {
                    Se(e, () => {
                      h();
                    });
                  };
                  let n = we;
                  const u = () => {
                    (n(), (n = (0, W.v)(A)));
                  };
                  return (
                    e.events.on("recalculateContent", A),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", u),
                    () => {
                      (n(),
                        e.events.off("recalculateContent", A),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", u));
                    }
                  );
                }, [e]),
                (0, s.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      Se(e, (n) => {
                        const a = c.current,
                          r = m.current,
                          s = e.getContainerSize();
                        if (!a || !r || !s) return;
                        const o = t.screenY - E.offset - a.getBoundingClientRect().y,
                          i = (o / a.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(n, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: n.scrollTop },
                        }),
                          u({ type: "dragging", thumb: r, thumbOffset: o, contentOffset: i }));
                      });
                    },
                    n = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        p(ke));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", n),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", n));
                    }
                  );
                }, [e, E.offset, E.pending, u, p]));
              const v = $((t) => e.applyStepTo(t), d, [e]),
                C = v[0],
                f = v[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", f, !0),
                  () => document.removeEventListener("mouseup", f, !0)
                ),
                [f],
              );
              const D = (e) => {
                e.target.classList.contains(Be) || (0, U.G)("highlight");
              };
              return o().createElement(
                "div",
                { className: l()(he, t.base), ref: a, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: l()(ve, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Be) ||
                      0 !== e.button ||
                      ((0, U.G)("play"), C(Y.Next));
                  },
                  ref: r,
                  onMouseEnter: D,
                }),
                o().createElement(
                  "div",
                  {
                    className: l()(fe, t.track),
                    onMouseDown: (t) => {
                      const u = m.current;
                      if (u && 0 === t.button)
                        if (((0, U.G)("play"), t.target === u))
                          (e.handleIsThumbDragging(!0),
                            p({ pending: !0, offset: t.screenY - u.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            m.current &&
                              Se(e, (u) => {
                                if (!u) return;
                                const a = n(e),
                                  r = e.clampPosition(u, u.scrollTop + a * t);
                                e.applyScroll(r);
                              });
                          })(t.screenY > u.getBoundingClientRect().y ? Y.Prev : Y.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: D,
                  },
                  o().createElement("div", { ref: m, className: t.thumb }),
                  o().createElement("div", { className: l()(Fe, t.rail) }),
                ),
                o().createElement("div", {
                  className: l()(Ce, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Be) ||
                      0 !== e.button ||
                      ((0, U.G)("play"), C(Y.Prev));
                  },
                  onMouseUp: f,
                  ref: i,
                  onMouseEnter: D,
                }),
              );
            },
          ),
          Ne = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Ie = ({
            children: e,
            api: t,
            className: n,
            barClassNames: u,
            areaClassName: a,
            scrollClassName: r,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = u || {};
                return Object.assign({}, e, { base: l()(Ne.base, e.base) });
              }, [u]),
              _ = (0, s.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: l()(Ne.defaultScroll, n), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Ne.area, a) },
                o().createElement(xe, { className: r, classNames: i, api: _ }, e),
              ),
              o().createElement(Te, { getStepByRailClick: c, api: t, onDrag: m, classNames: d }),
            );
          },
          xe = ({ className: e, classNames: t, children: n, api: u }) => (
            (0, s.useEffect)(() => (0, W.v)(u.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Ne.base, e), ref: u.wrapperRef, onWheel: u.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Ne.content, null == t ? void 0 : t.content), ref: u.contentRef },
                n,
              ),
            )
          );
        xe.Default = Ie;
        const Me = { Vertical: a, Horizontal: u };
        var Re = n(9480),
          Pe = n(7078),
          Oe = n(3415),
          He = n(8045);
        const We = "ExtendedText_base_71",
          Ge = "ExtendedText_base__zeroPadding_25",
          je = "ExtendedText_base__isTruncationAvailable_5b",
          ze = "ExtendedText_truncated_97",
          $e = "ExtendedText_truncated__hide_31",
          Ue = "ExtendedText_unTruncated_b8";
        let Ve, Ze, Xe;
        (!(function (e) {
          ((e[(e.Word = 0)] = "Word"),
            (e[(e.LineBreak = 1)] = "LineBreak"),
            (e[(e.NewLine = 2)] = "NewLine"),
            (e[(e.NoBreakSymbol = 3)] = "NoBreakSymbol"),
            (e[(e.NoBreakWrapper = 4)] = "NoBreakWrapper"),
            (e[(e.Binding = 5)] = "Binding"));
        })(Ve || (Ve = {})),
          (function (e) {
            ((e.FlexStart = "flex-start"), (e.Center = "center"), (e.FlexEnd = "flex-end"));
          })(Ze || (Ze = {})),
          (function (e) {
            ((e.NBSP = " "), (e.ZWNBSP = "\ufeff"), (e.NEW_LINE = "\n"));
          })(Xe || (Xe = {})));
        const qe = {
            [Xe.NBSP]: Ve.NoBreakSymbol,
            [Xe.ZWNBSP]: Ve.NoBreakSymbol,
            [Xe.NEW_LINE]: Ve.LineBreak,
          },
          Ke = {
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
          Ye = "renderers_noBreakWrapper_10",
          Qe = "renderers_lineBreak_b5",
          Je = "renderers_newLine_bd",
          et = (e) => ({ color: `#${e}` }),
          tt = ({ elementList: e, textBlock: t, key: n }) => {
            const u = t.colorTag;
            return u
              ? Ke[u]
                ? o().createElement(
                    "span",
                    { key: n, "data-block-type": t.blockType, className: Ke[u] },
                    e,
                  )
                : o().createElement(
                    "span",
                    { key: n, "data-block-type": t.blockType, style: et(u) },
                    e,
                  )
              : o().createElement("span", { key: n, "data-block-type": t.blockType }, e);
          },
          nt = {
            [Ve.Word]: tt,
            [Ve.NoBreakSymbol]: tt,
            [Ve.Binding]: ({ elementList: e, textBlock: t, key: n }) =>
              o().createElement(
                "span",
                { key: n, "data-block-type": t.blockType },
                e.map((e) => o().createElement(o().Fragment, { key: n }, e)),
              ),
            [Ve.LineBreak]: ({ key: e }) =>
              o().createElement("span", { key: e, "data-block-type": Ve.LineBreak, className: Qe }),
            [Ve.NewLine]: ({ elementList: e, key: t }) =>
              o().createElement(
                "span",
                { key: t, "data-block-type": Ve.NewLine, className: Je },
                e,
              ),
            [Ve.NoBreakWrapper]: ({ elementList: e, key: t }) =>
              o().createElement(
                "span",
                { key: t, "data-block-type": Ve.NoBreakWrapper, className: Ye },
                e,
              ),
          },
          ut = (e, t, n) => {
            const u = [];
            return (
              e.childList.forEach((a, r) => {
                const s = `${n}_${r}`;
                if (((e) => void 0 !== e.childList)(a)) {
                  const e = a,
                    t = e.blockType,
                    n = ut(e, nt[t], s);
                  u.push(...n);
                } else u.push(t({ elementList: [a], textBlock: e, key: s }));
              }),
              u
            );
          },
          at = (e) => {
            const t = [];
            return (
              e.forEach((e, n) => {
                t.push(
                  ...((e, t) => {
                    const n = [],
                      u = e.blockType,
                      a = nt[u],
                      r = ut(e, a, t);
                    return (
                      u === Ve.NoBreakWrapper
                        ? n.push(a({ elementList: r, textBlock: e, key: `${t}` }))
                        : n.push(...r),
                      n
                    );
                  })(e, n),
                );
              }),
              t
            );
          },
          rt = (e, t, n, u) => {
            let a = t.exec(e),
              r = 0;
            for (; a;)
              (r !== a.index && n(e.slice(r, a.index)), u(a), (r = t.lastIndex), (a = t.exec(e)));
            r !== e.length && n(e.slice(r));
          },
          st = (e) => {
            const t = /[\s\u002d]/g;
            let n = t.exec(e);
            if (!n) return [e];
            const u = [];
            let a = 0;
            for (; n;) (u.push(e.slice(a, t.lastIndex)), (a = t.lastIndex), (n = t.exec(e)));
            return (a !== e.length && u.push(e.slice(a)), u);
          },
          ot = (e, t = "") => {
            const n = [];
            return (
              rt(
                e,
                /(\n+|[\xa0\ufeff]+)/g,
                (e) => {
                  n.push({ blockType: Ve.Word, colorTag: t, childList: st(e) });
                },
                (e) => {
                  const u = e[0],
                    a = qe[u.charAt(0)];
                  a === Ve.LineBreak
                    ? n.push(
                        ...((e) => {
                          const t = [
                            { blockType: Ve.LineBreak, colorTag: "", childList: [e.charAt(0)] },
                          ];
                          for (let n = 0; n < e.length - 1; n++)
                            t.push({
                              blockType: Ve.NewLine,
                              colorTag: "",
                              childList: [e.charAt(0)],
                            });
                          return t;
                        })(u),
                      )
                    : n.push({ blockType: a, colorTag: t, childList: [u] });
                },
              ),
              n
            );
          },
          it = (e, t, n = "") => {
            const u = [];
            return (
              rt(
                e,
                /(?:%\(|{)(.*?)[)}][sd]?/g,
                (e) => {
                  u.push(...ot(e, n));
                },
                (e) => {
                  const a = e[1],
                    r = void 0 === t[a] ? e[0] : t[a];
                  "string" == typeof r || "number" == typeof r
                    ? u.push(...ot(String(r), n))
                    : u.push({ blockType: Ve.Binding, colorTag: n, childList: [r] });
                },
              ),
              u
            );
          },
          lt = (e, t) => {
            if (!e) return [t];
            const n = [],
              u = Object.assign({}, t, { childList: t.childList.splice(0, 1) });
            if (e.blockType === Ve.NoBreakWrapper) (e.childList.push(u), n.push(e));
            else {
              const t = Object.assign({}, e, { childList: e.childList.splice(-1) });
              (e.childList.length > 0 && n.push(e),
                n.push({ blockType: Ve.NoBreakWrapper, colorTag: "", childList: [t, u] }));
            }
            return (t.childList.length > 0 && n.push(t), n);
          },
          ct = (e, t = {}) => {
            if (!e) return [];
            const n = ((e) => {
              const t = [];
              let n = !1;
              return (
                e.forEach((e) => {
                  e.blockType === Ve.NoBreakSymbol
                    ? ((n = !0), t.push(...lt(t.pop(), e)))
                    : (n ? t.push(...lt(t.pop(), e)) : t.push(e), (n = !1));
                }),
                t
              );
            })(
              ((e, t) => {
                const n = [];
                return (
                  rt(
                    e,
                    /(?:%\(|{)(\w*)(?:_[Oo]pen|_Start)(?:\)s|})([\s\S]*?)(?:%\(|{)\w*(?:_[Cc]lose|_End)(?:\)s|})/g,
                    (e) => {
                      n.push(...it(e, t));
                    },
                    (e) => {
                      n.push(...it(e[2], t, e[1]));
                    },
                  ),
                  n
                );
              })((0, S.Eg)((0, S.z4)(e)), t),
            );
            return at(n);
          },
          mt = (e, t) => !e || e.offsetTop + e.offsetHeight > t,
          dt = (e, t) => e.offsetLeft + e.offsetWidth - t,
          _t = (e, t, n) => {
            if (!e || !e.textContent) return [!1, 0];
            if (e.offsetLeft > t) return [!1, 0];
            const u = dt(e, t),
              a = e.textContent.length,
              r = e.offsetWidth / a,
              s = Math.ceil(u / r);
            if (u > 0) {
              const u = Math.floor((t - e.offsetLeft) / r);
              return u >= n ? [!0, n + s] : [!1, u];
            }
            const o = Math.max(n + s, 0);
            return a < o ? [!1, 0] : [!0, o];
          },
          Et = (e, t, n, u, a, r) => {
            let s = -1,
              i = null;
            for (let l = n; l >= 0; l--) {
              const n = e[l],
                c = Number(e[l].getAttribute("data-block-type"));
              if (c === Ve.LineBreak || c === Ve.NewLine || c === Ve.Binding) continue;
              const m = n.textContent || "";
              if (!(n.childElementCount > 1)) {
                const e = _t(n, u, a),
                  c = e[0],
                  d = e[1];
                if (!c) {
                  d > 0 && (a -= d);
                  continue;
                }
                const _ = m.slice(0, m.length - d) + r,
                  E = t[l];
                ((i = o().cloneElement(E, E.props, _)), (s = l));
                break;
              }
              {
                const e = n.children,
                  c = t[l],
                  d = c.props.children,
                  _ = Et(e, d, e.length - 1, u, a, r),
                  E = _[0],
                  g = _[1];
                if (!(E < 0)) {
                  const e = d.slice(0, E);
                  ((i = o().cloneElement(c, c.props, e, g)), (s = l));
                  break;
                }
                a -= m.length;
              }
            }
            return [s, i];
          },
          gt = (e, t, n, u = "...") => {
            const a = [...t],
              r = e.current;
            if (!r) return [a, !1];
            const s = n.height,
              o = n.width,
              i = r.lastElementChild;
            if (!mt(i, s) && dt(i, o) <= 0) return [a, !1];
            const l = r.children,
              c = ((e, t) => {
                let n = 0,
                  u = e.length - 1;
                for (; u - n >= 0;) {
                  const a = n + Math.ceil(0.5 * (u - n));
                  mt(e[a], t) ? (u = a - 1) : (n = a + 1);
                }
                return n - 1;
              })(l, s);
            if (c < 0) return [a, !1];
            const m = Et(l, a, c, o, u.length, u),
              d = m[0],
              _ = m[1];
            return (_ && (a.splice(d, 1, _), a.splice(d + 1)), [a, !0]);
          },
          pt = o().memo(
            ({
              text: e,
              classMix: t,
              onSizeChanged: n,
              binding: u,
              isTooltipEnable: a = !1,
              isTruncationAvailable: r = !1,
              targetId: i,
              justifyContent: c = Ze.FlexStart,
              alignContent: m = Ze.FlexStart,
              truncateIdentify: d = "...",
            }) => {
              const _ = (0, s.useRef)(null),
                E = (0, s.useRef)({ height: 0, width: 0 }),
                g = (0, s.useState)({ elementList: [], isTruncated: !1, isTruncateFinished: !1 }),
                p = g[0],
                b = g[1],
                h = (0, s.useMemo)(() => ct(e, u), [u, e]),
                A = (0, s.useMemo)(() => {
                  if (a && p.isTruncated)
                    return {
                      args: { text: e, stringifyKwargs: u ? JSON.stringify(u) : "" },
                      contentId: R.views.lobby.common.tooltips.ExtendedTextTooltip("resId"),
                      targetId: i,
                    };
                }, [u, a, i, e, p.isTruncated]),
                v = (0, s.useCallback)(
                  (e) => {
                    ((E.current.width = e.contentRect.width),
                      (E.current.height = e.contentRect.height));
                    const t = gt(_, h, E.current, d),
                      u = t[0],
                      a = t[1];
                    (b({ elementList: u, isTruncated: a, isTruncateFinished: !0 }), n && n(a));
                  },
                  [n, d, h],
                ),
                C = (0, s.useMemo)(() => ({ justifyContent: c, alignContent: m }), [m, c]);
              return (
                ((e, t, n = !0) => {
                  const u = (0, s.useCallback)(
                    (e) => {
                      const n = e[0];
                      t && t(n);
                    },
                    [t],
                  );
                  (0, s.useEffect)(() => {
                    if (!e.current || !n) return;
                    const t = new He.Z((e) => u(e));
                    return (
                      t.observe(e.current),
                      () => {
                        t.disconnect();
                      }
                    );
                  }, [u, n, e]);
                })(_, v, r),
                o().createElement(
                  "div",
                  { className: l()(We, t, Ge, r && je), style: C },
                  o().createElement("div", { className: Ue, ref: _ }, h),
                  o().createElement(
                    Oe.l,
                    { tooltipArgs: A },
                    o().createElement(
                      "div",
                      { className: l()(ze, !p.isTruncateFinished && r && $e), style: C },
                      p.isTruncateFinished && r ? p.elementList : h,
                    ),
                  ),
                )
              );
            },
          );
        let bt;
        !(function (e) {
          ((e[(e.none = 0)] = "none"),
            (e[(e.increase = 1)] = "increase"),
            (e[(e.decrease = 2)] = "decrease"),
            (e[(e.mixed = 3)] = "mixed"));
        })(bt || (bt = {}));
        const ht = {
            base: "BuffIcon_base_c8",
            base__increase: "BuffIcon_base__increase_60",
            base__decrease: "BuffIcon_base__decrease_31",
            base__mixed: "BuffIcon_base__mixed_23",
          },
          At = o().memo(function ({ buffIconType: e, className: t }) {
            return e === bt.none
              ? null
              : o().createElement("div", { className: l()(ht.base, ht[`base__${bt[e]}`], t) });
          }),
          vt = "Delta_base_3e",
          Ct = "Delta_base__positive_82",
          ft = "Delta_base__negative_86",
          Dt = o().memo(function ({ isPositive: e, width: t, isUseAnim: n }) {
            const u = (0, K.useSpring)({
                from: { left: 0, width: 0 },
                left: e ? 0 : t,
                width: e ? 0 : Math.abs(t),
                config: { duration: Nt },
                delay: e ? 0 : Nt,
                immediate: !n,
              }),
              a = (0, K.useSpring)({
                from: { left: 2, width: 0 },
                left: 2,
                width: e ? t : 0,
                config: { duration: Nt },
                delay: e || 0 === t ? Nt : 0,
                immediate: !n,
              });
            return o().createElement(
              o().Fragment,
              null,
              o().createElement(K.animated.div, { className: l()(vt, ft), style: u }),
              o().createElement(K.animated.div, { className: l()(vt, Ct), style: a }),
            );
          }),
          Ft = "Indicator_base_b9",
          Bt = "Indicator_progress_ce",
          wt = "Indicator_progressMarker_b4",
          kt = "Indicator_indicator_bc",
          yt = "Indicator_indicator__start_80",
          St = "Indicator_indicator__end_3b",
          Lt = "Indicator_marker_f7",
          Tt = "Indicator_valueLine_1d",
          Nt = 300,
          It = o().memo(function ({
            minValue: e,
            maxValue: t,
            value: n,
            markerValue: u,
            delta: a,
            isUseAnim: r,
          }) {
            const s = u === e ? 2 : (u / t) * 254,
              i = (n / t) * 254,
              c = (a / t) * 254,
              m = a > 0,
              d = { config: { duration: Nt }, immediate: !r },
              _ = (0, K.useSpring)(
                Object.assign({ from: { left: 2 }, to: { left: s }, delay: Nt }, d),
              ),
              E = (0, K.useSpring)(
                Object.assign({ from: { width: e }, to: { width: i }, delay: Nt }, d),
              );
            return o().createElement(
              "div",
              { className: Ft },
              o().createElement(
                "div",
                { className: Bt },
                o().createElement("div", { className: l()(kt, yt) }),
                o().createElement(K.animated.div, { className: Tt, style: E }),
                o().createElement(
                  "div",
                  { className: wt },
                  o().createElement(
                    K.animated.div,
                    { className: Lt, style: _ },
                    o().createElement(Dt, { isPositive: m, width: c, isUseAnim: r }),
                  ),
                ),
                o().createElement("div", { className: l()(kt, St) }),
              ),
            );
          });
        let xt;
        !(function (e) {
          ((e.None = "none"), (e.Increase = "increase"), (e.Decrease = "decrease"));
        })(xt || (xt = {}));
        const Mt = {
            base: "Param_base_51",
            value: "Param_value_51",
            icon: "Param_icon_37",
            name: "Param_name_82",
            highlight: "Param_highlight_81",
            highlight__increase: "Param_highlight__increase_35",
            highlight__decrease: "Param_highlight__decrease_ec",
          },
          Rt = o().memo(function ({
            id: e,
            value: t,
            tooltipID: n,
            isEnabled: u,
            highlightType: a,
            localizedName: r,
          }) {
            return o().createElement(
              Pe.t,
              {
                args: { tooltipId: n, paramId: e },
                targetId: R.views.lobby.hangar.subViews.VehicleParams("resId"),
                isEnabled: u,
              },
              o().createElement(
                "div",
                { className: Mt.base },
                o().createElement(pt, { justifyContent: Ze.FlexEnd, classMix: Mt.value, text: t }),
                o().createElement("div", {
                  className: Mt.icon,
                  style: { backgroundImage: `url('R.images.gui.maps.icons.vehParams.small.${e}')` },
                }),
                o().createElement(
                  "div",
                  { className: Mt.name },
                  r || R.strings.menu.tank_params.$dyn(e),
                ),
                a !== xt.None &&
                  o().createElement("div", { className: l()(Mt.highlight, Mt[`highlight__${a}`]) }),
              ),
            );
          }),
          Pt = "Group_base_66",
          Ot = "Group_group_07",
          Ht = "Group_hoverBg_97",
          Wt = "Group_hoverBg__scrollable_2a",
          Gt = "Group_groupHeader_f5",
          jt = "Group_name_21",
          zt = "Group_arrow_96",
          $t = "Group_arrow__opened_47",
          Ut = "Group_params_88",
          Vt = "Group_params__opened_9a",
          Zt = "Group_separator_b5",
          Xt = "Group_right_13",
          qt = "Group_buff_fa",
          Kt = "Group_value_00",
          Yt = "Group_value__additional_81";
        function Qt() {
          return (
            (Qt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Qt.apply(this, arguments)
          );
        }
        const Jt = (0, L.Pi)(
            ({
              id: e,
              isOpen: t,
              params: n,
              extraParams: u,
              tooltipID: a,
              indicator: r,
              value: s,
              additionalValue: i,
              buffIconType: c,
              isEnabled: m,
              isScrollable: d,
            }) => {
              const _ = H().controls,
                E = u && u.length > 0;
              return o().createElement(
                "div",
                { className: Pt },
                o().createElement(
                  Pe.t,
                  {
                    args: { tooltipId: a, paramId: e },
                    targetId: R.views.lobby.hangar.subViews.VehicleParams("resId"),
                    isEnabled: m,
                  },
                  o().createElement(
                    "div",
                    {
                      className: Ot,
                      onClick: () => _.onGroupClick(e),
                      onMouseEnter: U.$.playHighlight,
                    },
                    o().createElement("div", { className: l()(Ht, d && Wt) }),
                    o().createElement(
                      "div",
                      { className: Gt },
                      o().createElement("div", { className: l()(zt, t && $t) }),
                      o().createElement(
                        "div",
                        { className: jt },
                        R.strings.menu.tank_params.$dyn(e),
                      ),
                      o().createElement(
                        "div",
                        { className: Xt },
                        o().createElement(At, { buffIconType: c, className: qt }),
                        i && o().createElement(pt, { classMix: l()(Kt, Yt), text: i }),
                        o().createElement(pt, { classMix: Kt, text: s }),
                      ),
                    ),
                    o().createElement(It, r),
                  ),
                ),
                o().createElement(
                  "div",
                  { className: l()(Ut, t && Vt) },
                  Re.UI(n, (e) => o().createElement(Rt, Qt({ key: e.id }, e))),
                  E && o().createElement("div", { className: Zt }),
                  Re.UI(u, (e) => o().createElement(Rt, Qt({ key: e.id }, e))),
                ),
              );
            },
          ),
          en = {
            base: "VehicleParams_base_3b",
            base__bg: "VehicleParams_base__bg_c4",
            scroll: "VehicleParams_scroll_59",
            content: "VehicleParams_content_09",
            barBase: "VehicleParams_barBase_6f",
          };
        function tn() {
          return (
            (tn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            tn.apply(this, arguments)
          );
        }
        const nn = {
            settings: {
              step: { type: "fixed", value: 48, clampedArrowStepTimeout: 0 },
              animationConfig: { tension: 0, friction: 0 },
            },
          },
          un = (0, L.Pi)(({ showBackground: e = !0, className: t }) => {
            const n = H().model,
              u = (0, s.useState)(!1),
              a = u[0],
              r = u[1],
              i = n.groups.get(),
              c = be(nn);
            return (
              (0, s.useEffect)(() => {
                const e = () => {
                  const e = c.getContainerSize(),
                    t = c.getWrapperSize();
                  e && t && r(e > t);
                };
                return (
                  c.events.on("recalculateContent", e),
                  () => {
                    c.events.off("recalculateContent", e);
                  }
                );
              }, [c]),
              o().createElement(
                "div",
                { className: l()(en.base, e && en.base__bg, t) },
                o().createElement(
                  Me.Vertical.Area.Default,
                  {
                    api: c,
                    barClassNames: { base: en.barBase },
                    scrollClassName: en.scroll,
                    scrollClassNames: { content: en.content },
                  },
                  o().createElement(
                    "div",
                    { className: en.groups },
                    Re.UI(i, (e) =>
                      o().createElement(Jt, tn({ key: e.id }, e, { isScrollable: a })),
                    ),
                  ),
                ),
              )
            );
          }),
          an = (0, s.memo)(function (e) {
            const t = (0, s.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return o().createElement(O, { options: t }, o().createElement(un, e));
          }),
          rn = {
            base: "FlagIcon_base_25",
            base__c_1080x454: "FlagIcon_base__c_1080x454_6c",
            base__c_240x118: "FlagIcon_base__c_240x118_92",
          };
        let sn;
        !(function (e) {
          ((e.c1080x454 = "c_1080x454"), (e.c240x118 = "c_240x118"));
        })(sn || (sn = {}));
        const on = (e, t) => {
            switch (t) {
              case sn.c1080x454:
                return R.images.gui.maps.icons.crew.flags.$dyn(e);
              case sn.c240x118:
                return R.images.gui.maps.icons.tankmen.card.nations.$dyn(e);
            }
          },
          ln = o().memo(function ({ nation: e, size: t, className: n }) {
            return o().createElement("div", {
              className: l()(rn.base, rn[`base__${t}`], n),
              style: { backgroundImage: `url('${on(e, t)}')` },
            });
          }),
          cn = {
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
          mn = [
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
        function dn() {
          return (
            (dn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            dn.apply(this, arguments)
          );
        }
        class _n extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, U.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, U.G)(this.props.soundClick));
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
              u = e.goto,
              a = e.side,
              r = e.type,
              s = e.classNames,
              i = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onMouseUp,
              _ =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var n,
                    u,
                    a = {},
                    r = Object.keys(e);
                  for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(e, mn)),
              E = l()(cn.base, cn[`base__${r}`], cn[`base__${a}`], null == s ? void 0 : s.base),
              g = l()(cn.icon, cn[`icon__${r}`], cn[`icon__${a}`], null == s ? void 0 : s.icon),
              p = l()(cn.glow, null == s ? void 0 : s.glow),
              b = l()(cn.caption, cn[`caption__${r}`], null == s ? void 0 : s.caption),
              h = l()(cn.goto, null == s ? void 0 : s.goto);
            return o().createElement(
              "div",
              dn(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(m),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: n,
                },
                _,
              ),
              "info" !== r && o().createElement("div", { className: cn.shine }),
              o().createElement(
                "div",
                { className: g },
                o().createElement("div", { className: p }),
              ),
              o().createElement("div", { className: b }, t),
              u && o().createElement("div", { className: h }, u),
            );
          }
        }
        _n.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const En = ({ onClick: e }) =>
            o().createElement(_n, {
              onClick: e,
              caption: R.strings.crew.common.navigation.aboutCrew(),
              type: "info",
            }),
          gn = "common_close_0e",
          pn = ({ onClick: e, label: t = R.strings.menu.viewHeader.closeBtn.label() }) =>
            o().createElement(_n, {
              onClick: e,
              classNames: { base: gn },
              caption: t,
              type: "close",
              side: "right",
            }),
          bn = "TopButtons_base_ef",
          hn = "TopButtons_leftButtons_9e",
          An = "TopButtons_rightButtons_33",
          vn = o().memo(function ({
            backButtonLabel: e,
            closeButtonLabel: t = R.strings.menu.viewHeader.closeBtn.label(),
            onBackClick: n,
            onAboutClick: u,
            onCloseClick: a,
            className: r,
            classNames: s,
          }) {
            return o().createElement(
              "div",
              { className: l()(bn, r) },
              o().createElement(
                "div",
                { className: l()(hn, null == s ? void 0 : s.leftButtons) },
                e && n && o().createElement(_n, { onClick: n, caption: e, type: "back" }),
              ),
              o().createElement(
                "div",
                { className: l()(An, null == s ? void 0 : s.rightButtons) },
                u && o().createElement(En, { onClick: u }),
                a && o().createElement(pn, { onClick: a, label: t }),
              ),
            );
          });
        var Cn = n(9690);
        const fn = {
          base: "TankName_base_f1",
          base__sizeMedium: "TankName_base__sizeMedium_3a",
          base__sizBig: "TankName_base__sizBig_a9",
          base__typeWhite: "TankName_base__typeWhite_32",
          base__typeWhiteSpanish: "TankName_base__typeWhiteSpanish_e2",
          base__typeColored: "TankName_base__typeColored_bc",
          level: "TankName_level_bb",
          type: "TankName_type_3c",
          type__elite: "TankName_type__elite_cc",
          base__sizeBig: "TankName_base__sizeBig_2b",
          name: "TankName_name_56",
          base__tagPremiumIGR: "TankName_base__tagPremiumIGR_26",
          premiumIGR: "TankName_premiumIGR_25",
        };
        let Dn, Fn;
        (!(function (e) {
          ((e.extraSmall = "extraSmall"), (e.medium = "medium"), (e.big = "big"));
        })(Dn || (Dn = {})),
          (function (e) {
            ((e.colored = "colored"), (e.white = "white"), (e.whiteSpanish = "whiteSpanish"));
          })(Fn || (Fn = {})));
        const Bn = ({
            isElite: e,
            vehicleName: t,
            vehicleShortName: n,
            vehicleType: u,
            vehicleLvl: a,
            tags: r,
            isPremiumIGR: s,
            size: i = Dn.extraSmall,
            type: c = Fn.colored,
            className: m,
            classNames: d,
            isShortName: _ = !1,
          }) => {
            const E = `${(0, S.BN)(u)}${e ? "_elite" : ""}`,
              g = R.images.gui.maps.icons.vehicleTypes.big.$dyn(E);
            return o().createElement(
              "div",
              {
                className: l()(
                  fn.base,
                  fn[`base__size${(0, S.e)(i)}`],
                  fn[`base__type${(0, S.e)(c)}`],
                  r && Re.UI(r, (e) => fn[`base__tag${(0, S.e)(e)}`]),
                  m,
                ),
              },
              o().createElement(
                "div",
                { className: l()(fn.level, null == d ? void 0 : d.level) },
                (0, Cn.HG)(a),
              ),
              o().createElement("div", {
                className: l()(fn.type, e && fn.type__elite, null == d ? void 0 : d.typeIcon),
                style: { backgroundImage: `url(${g})` },
              }),
              s && o().createElement("div", { className: fn.premiumIGR }),
              o().createElement(
                "div",
                { className: l()(fn.name, null == d ? void 0 : d.name) },
                _ ? n : t,
              ),
            );
          },
          wn = "VehicleParamsDecorator_base_32",
          kn = "VehicleParamsDecorator_vehicleInfo_02",
          yn = "VehicleParamsDecorator_tankName_ac",
          Sn = "VehicleParamsDecorator_tankLvl_26",
          Ln = "VehicleParamsDecorator_type_e7",
          Tn = "VehicleParamsDecorator_tip_6c",
          Nn = ["children", "isPerkTipShown"];
        function In() {
          return (
            (In =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            In.apply(this, arguments)
          );
        }
        const xn = (e) => {
          let t = e.children,
            n = e.isPerkTipShown,
            u = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, Nn);
          return o().createElement(
            "div",
            { className: wn },
            o().createElement(
              Bn,
              In({ className: kn, classNames: { name: yn, level: Sn, typeIcon: Ln } }, u, {
                isShortName: !0,
              }),
            ),
            t,
            n &&
              o().createElement(
                "div",
                { className: Tn },
                R.strings.crew.vehicleParamsDecorator.perkTip(),
              ),
          );
        };
        var Mn = n(8727),
          Rn = n(4543),
          Pn = n(5175),
          On = n(3946),
          Hn = n(4598);
        const Wn = (e) => ({ tankmanID: e }),
          Gn = (e) => ({ recruitID: e }),
          jn = (0, T.q)()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  { tankmanList: e.array("tankmanList"), vehicleInfo: e.object("vehicleInfo") },
                  e.primitives([
                    "requiredRole",
                    "vehicle",
                    "nation",
                    "hasCrew",
                    "hasFilters",
                    "backButtonLabel",
                    "isButtonBarVisible",
                    "roleChangeDiscountPercent",
                    "itemsOffset",
                    "itemsAmount",
                  ]),
                ),
                n = e.array("headersIndexes"),
                u = (0, On.Om)(
                  (e) => {
                    const n = e - t.itemsOffset.get(),
                      u = (0, Pn.c)(t.tankmanList.get());
                    if (n >= 0 && n < u.length) return u[n];
                  },
                  { equals: Hn.jv },
                ),
                a = (0, On.Om)(() => (t.hasCrew.get() ? t.backButtonLabel.get() : R.invalid())),
                r = (0, On.Om)(() => (0, Pn.c)(n.get()), { equals: Hn.jv });
              return Object.assign({}, t, {
                computes: { backButtonLabel: a, getItem: u, getHeadersIndexes: r },
              });
            },
            ({ externalModel: e }) => ({
              close: e.createCallbackNoArgs("onClose"),
              closeWithEsc: e.createCallback(() => ({ isFromEscape: !0 }), "onClose"),
              hangar: e.createCallbackNoArgs("onHangar"),
              selectTankman: e.createCallback(Wn, "onTankmanSelected"),
              selectRecruit: e.createCallback((e) => ({ recruitID: e }), "onRecruitSelected"),
              restoreTankman: e.createCallback(Wn, "onTankmanRestore"),
              recruitNewTankman: e.createCallbackNoArgs("onRecruitNewTankman"),
              back: e.createCallbackNoArgs("onBack"),
              resetFilters: e.createCallbackNoArgs("onResetFilters"),
              playRecruitVoiceover: e.createCallback(Gn, "onPlayRecruitVoiceover"),
              loadCards: e.createCallback((e, t) => ({ limit: e, offset: t }), "onLoadCards"),
            }),
          ),
          zn = jn[0],
          $n = jn[1];
        var Un = n(3457),
          Vn = n(6373);
        const Zn = {
          base: "ListHeader_base_ad",
          title: "ListHeader_title_a8",
          base__memberChange: "ListHeader_base__memberChange_c2",
          base__tankChange: "ListHeader_base__tankChange_fb",
          base__personalData: "ListHeader_base__personalData_aa",
        };
        let Xn;
        !(function (e) {
          ((e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(Xn || (Xn = {}));
        const qn = ({ title: e, theme: t = Xn.Barracks, className: n, children: u }) =>
            o().createElement(
              "div",
              { className: l()(Zn.base, Zn[`base__${t}`]) },
              o().createElement("div", { className: l()(Zn.title, n) }, e),
              u,
            ),
          Kn = "Header_base_4c",
          Yn = "Header_button_fa",
          Qn = (0, L.Pi)(({ isSmall: e }) => {
            const t = $n(),
              n = t.model,
              u = t.controls,
              a = n.requiredRole.get(),
              r = e && "driver" === a;
            return o().createElement(
              qn,
              {
                theme: Xn.MemberChange,
                title: (0, S.uF)(R.strings.crew.memberChange.title(), {
                  role: r
                    ? R.strings.item_types.tankman.roles.smallResolution.upperCase.driver()
                    : R.strings.item_types.tankman.roles.objectiveCase.upperCase.$dyn(a),
                  vehicle: n.vehicle.get(),
                }),
              },
              o().createElement(
                "div",
                { className: Kn },
                o().createElement(
                  Vn.i,
                  { body: R.strings.crew.tankmanList.tooltip.recruit.body() },
                  o().createElement(
                    Un.u5,
                    {
                      onClick: u.recruitNewTankman,
                      type: Un.L$.secondary,
                      size: Un.qE.small,
                      mixClass: Yn,
                    },
                    (0, S.uF)(R.strings.crew.memberChange.action.recruit(), {
                      role: r
                        ? R.strings.item_types.tankman.roles.smallResolution.normalCase.driver()
                        : R.strings.item_types.tankman.roles.objectiveCase.$dyn(a),
                    }),
                  ),
                ),
              ),
            );
          });
        var Jn = n(2106),
          eu = n(8018);
        const tu = "WarningText_base_13",
          nu = "WarningText_icon_5d",
          uu = "WarningText_label_c6",
          au = o().memo(function ({ label: e }) {
            return o().createElement(
              "div",
              { className: tu },
              o().createElement("div", { className: nu }),
              o().createElement("div", { className: uu }, e),
            );
          }),
          ru = "ListEmptyState_base_ae",
          su = "ListEmptyState_content_1e",
          ou = "ListEmptyState_shadow_ae",
          iu = "ListEmptyState_buttonWrapper_78",
          lu = "ListEmptyState_button_f1",
          cu = o().memo(function ({
            warningText: e,
            buttonType: t = Un.L$.secondary,
            tooltipArgs: n = eu.Xd,
            className: u,
            onClick: a,
            children: r,
          }) {
            return o().createElement(
              "div",
              { className: l()(ru, u) },
              o().createElement(
                "div",
                { className: su },
                o().createElement("div", { className: ou }),
                o().createElement(au, { label: e }),
                r &&
                  o().createElement(
                    "div",
                    { className: iu },
                    o().createElement(
                      Vn.i,
                      n,
                      o().createElement(
                        Un.u5,
                        { size: Un.qE.small, type: t, onClick: a, mixClass: lu },
                        r,
                      ),
                    ),
                  ),
              ),
            );
          });
        var mu = n(2603);
        let du, _u, Eu, gu, pu;
        (!(function (e) {
          ((e.Any = "any"),
            (e.Commander = "commander"),
            (e.Radioman = "radioman"),
            (e.Driver = "driver"),
            (e.Gunner = "gunner"),
            (e.Loader = "loader"));
        })(du || (du = {})),
          (function (e) {
            ((e.InBarracks = "in_barracks"), (e.InTank = "in_tank"), (e.Dismissed = "dismissed"));
          })(_u || (_u = {})),
          (function (e) {
            ((e.Tankman = "tankman"),
              (e.Recruit = "recruit"),
              (e.Dismissed = "dismissed"),
              (e.Unique = "unique"));
          })(Eu || (Eu = {})),
          (function (e) {
            ((e.Default = "default"), (e.Selected = "selected"), (e.Disabled = "disabled"));
          })(gu || (gu = {})),
          (function (e) {
            ((e.IsLockCrew = "isLockCrew"), (e.TankmanHasRole = "tankmanHasRole"));
          })(pu || (pu = {})));
        var bu = n(5139);
        function hu(e, t, n) {
          const u = (0, s.useMemo)(
            () =>
              (function (e, t, n) {
                return void 0 === n ? (0, bu.Z)(e, t, !1) : (0, bu.Z)(e, n, !1 !== t);
              })(n, e),
            t,
          );
          return ((0, s.useEffect)(() => u.cancel, [u]), u);
        }
        var Au = n(7077);
        const vu = "Content_base_48",
          Cu = "Content_name_7b",
          fu = "Content_specializationInfo_ac",
          Du = "Content_recruitLabel_17",
          Fu = "Content_levelPercentage_f1",
          Bu = "Content_levelPercentage__red_c9";
        function wu() {
          return (
            (wu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            wu.apply(this, arguments)
          );
        }
        const ku = ({
          fullUserName: e,
          isRecruit: t,
          tankmanVehicleInfo: n,
          specializationLevel: u,
          hasSpecializationLevelPenalty: a,
          className: r,
        }) => {
          const i = (0, s.useMemo)(() => (0, eu.T3)(Math.floor(u)), [u]);
          return o().createElement(
            "div",
            { className: l()(vu, r) },
            o().createElement("div", { className: Cu }, e),
            o().createElement(
              "div",
              { className: fu },
              t
                ? o().createElement("div", { className: Du }, R.strings.crew.tankman.recruit())
                : o().createElement(
                    o().Fragment,
                    null,
                    o().createElement(Bn, wu({}, n, { type: Fn.whiteSpanish, isShortName: !0 })),
                    o().createElement("div", { className: l()(Fu, a && Bu) }, `(${i})`),
                  ),
            ),
          );
        };
        let yu;
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
        })(yu || (yu = {}));
        const Su = 60,
          Lu = 3600,
          Tu = 86400;
        Date.now();
        const Nu = (0, s.memo)(({ duration: e }) => {
            const t =
              e >= 0
                ? (n = (function (e = 0) {
                    let t = e;
                    const n = Math.trunc(t / Tu);
                    t -= n * Tu;
                    const u = Math.trunc(t / Lu);
                    t -= u * Lu;
                    const a = Math.trunc(t / Su);
                    return ((t -= a * Su), { days: n, hours: u, minutes: a, seconds: t });
                  })(e)).days > 0
                  ? (0, S.WU)(R.strings.common.duration.days(), { days: n.days })
                  : n.hours > 0
                    ? (0, S.WU)(R.strings.common.duration.hours(), { hours: n.hours })
                    : n.minutes > 0
                      ? (0, S.WU)(R.strings.common.duration.minutes(), { minutes: n.minutes })
                      : (0, S.WU)(R.strings.common.duration.seconds(), { seconds: n.seconds })
                : R.strings.common.duration.unlimited();
            var n;
            return o().createElement("span", null, t);
          }),
          Iu = () => {},
          xu = (e = 0, t, n = 0, u = Iu) => {
            const a = (0, s.useState)(e),
              r = a[0],
              o = a[1];
            return (
              (0, s.useEffect)(() => {
                if (e > 0) {
                  o(e);
                  const a = Date.now(),
                    r = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - a) / 1e3);
                        null !== n && t <= n ? (o(n), u && u(), clearInterval(r)) : o(t);
                      },
                      1e3 * (t || (e > 120 ? Su : 1)),
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                o(0);
              }, [e, t, n, u]),
              r
            );
          };
        n(6536);
        w.Sw.instance;
        let Mu;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Mu || (Mu = {}));
        w.Sw.instance;
        const Ru = xu,
          Pu = o().memo(function ({ duration: e, className: t }) {
            const n = Ru(e, 1);
            return o().createElement(
              "div",
              { className: t },
              o().createElement(Nu, { duration: n }),
            );
          }),
          Ou = "Location_base_4d",
          Hu = "Location_duration_5d",
          Wu = "Location_icon_eb",
          Gu = o().memo(function ({ location: e, className: t, timeToDismiss: n }) {
            return o().createElement(
              "div",
              { className: l()(Ou, t) },
              e === _u.Dismissed && o().createElement(Pu, { className: Hu, duration: n }),
              o().createElement("div", {
                className: Wu,
                style: {
                  backgroundImage: `url(R.images.gui.maps.icons.tankmen.card.location.${e})`,
                },
              }),
            );
          });
        let ju, zu;
        (!(function (e) {
          ((e.Default = "default"), (e.Selected = "selected"), (e.InBattle = "in_battle"));
        })(ju || (ju = {})),
          (function (e) {
            ((e.White = "white"), (e.Red = "red"));
          })(zu || (zu = {})));
        const $u = "Role_base_68",
          Uu = o().memo(function ({ role: e, className: t, roleIconColor: n = zu.White }) {
            return o().createElement("div", {
              className: l()($u, t),
              style: {
                backgroundImage: `url(R.images.gui.maps.icons.tankmen.roles.opaque.${n}.${e})`,
              },
            });
          });
        var Vu = n(8271);
        var Zu = n(8485);
        const Xu = {
          base: "Skill_base_a9",
          base__double: "Skill_base__double_7a",
          base__collapsed: "Skill_base__collapsed_6e",
          skillLevel: "Skill_skillLevel_85",
        };
        let qu;
        !(function (e) {
          ((e.Default = "default"), (e.Double = "double"), (e.Collapsed = "collapsed"));
        })(qu || (qu = {}));
        const Ku = ({ icon: e, type: t, isLevelVisible: n, skillLevel: u, theme: a }) =>
            o().createElement(
              "div",
              {
                className: l()(
                  Xu.base,
                  Xu[`base__${a}`],
                  n && Xu.base__hasSkillLevel,
                  "new_skill" === e && Xu.base__isNewSkill,
                ),
              },
              o().createElement(Zu.d, { icon: e, size: Zu.O.Big, type: t }),
              n && o().createElement("div", { className: Xu.skillLevel }, (0, eu.T3)(u)),
            ),
          Yu = "Skills_base_d8",
          Qu = "Skills_skillContainer_54",
          Ju = "Skills_divider_ee";
        function ea() {
          return (
            (ea =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            ea.apply(this, arguments)
          );
        }
        const ta = (0, s.memo)(({ skills: e, lastSkillLevel: t, className: n }) => {
            const u = e.length - 1,
              a = e.filter((e) => e.type === Vu.W.ZeroSkill).length,
              r = a > 0,
              s = a === e.length;
            return o().createElement(
              "div",
              { className: l()(Yu, n) },
              e.map((n, i) => {
                const l = i === u,
                  c = r ? 26 : 28,
                  m = l && e.length < c && t < 100 && -1 !== t,
                  d = ((e, t, n, u, a) => {
                    const r = a ? 16 : 18,
                      s = a ? 13 : 14,
                      o = a ? 8 : 9;
                    return t && n
                      ? qu.Double
                      : u > r
                        ? e === s - 1 || t
                          ? qu.Default
                          : qu.Collapsed
                        : u > o && e === o - 1
                          ? qu.Double
                          : qu.Default;
                  })(i, l, m, e.length, r);
                return o().createElement(
                  "div",
                  { key: n.name + i, className: Qu },
                  o().createElement(Ku, ea({ theme: d, isLevelVisible: m, skillLevel: t }, n)),
                  i === a - 1 && !s && o().createElement("div", { className: Ju }),
                );
              }),
            );
          }),
          na = "ThemeHelper_base_39",
          ua = "ThemeHelper_disabledContent_20",
          aa = "ThemeHelper_disabledIcon_95",
          ra = "ThemeHelper_disabledTitle_57",
          sa = o().memo(function ({
            isDisabled: e,
            className: t,
            disableReason: n,
            disableIcon: u,
          }) {
            return o().createElement(
              "div",
              { className: l()(na, t) },
              e &&
                o().createElement(
                  "div",
                  { className: ua },
                  u &&
                    o().createElement("div", {
                      className: aa,
                      style: { backgroundImage: `url(${u})` },
                    }),
                  o().createElement("div", { className: ra }, n),
                ),
            );
          }),
          oa = ({ cantBeSelected: e, args: t, children: n, isTooltipEnabled: u }) =>
            e
              ? o().createElement(
                  Vn.i,
                  { body: R.strings.crew.tankman.tooltip.cantBeSelected.body() },
                  n,
                )
              : o().createElement(Pe.t, { args: t, isEnabled: u }, n),
          ia = {
            base: "TankmanCard_base_dd",
            base__hovered: "TankmanCard_base__hovered_96",
            base__selected: "TankmanCard_base__selected_24",
            base__selectedFromMultiselect: "TankmanCard_base__selectedFromMultiselect_cb",
            base__selectDisabled: "TankmanCard_base__selectDisabled_b1",
            base__disabled: "TankmanCard_base__disabled_1f",
            themeHelper: "TankmanCard_themeHelper_78",
            locationIcon: "TankmanCard_locationIcon_26",
            crewRole: "TankmanCard_crewRole_2e",
            iconWrapper: "TankmanCard_iconWrapper_a3",
            base__isCollapsedOnHover: "TankmanCard_base__isCollapsedOnHover_5e",
            flag: "TankmanCard_flag_78",
            icon: "TankmanCard_icon_a5",
            separatorWrapper: "TankmanCard_separatorWrapper_fe",
            separator: "TankmanCard_separator_73",
            separator__top: "TankmanCard_separator__top_72",
            content: "TankmanCard_content_0c",
            fadeForSkills: "TankmanCard_fadeForSkills_3b",
            skills: "TankmanCard_skills_ef",
            helperLayer: "TankmanCard_helperLayer_09",
          },
          la = (0, s.memo)(
            ({
              tankmanID: e,
              recruitID: t,
              nation: n,
              skills: u,
              lastSkillLevel: a,
              specializationLevel: r,
              role: i,
              fullUserName: c,
              iconName: m,
              tankmanVehicleInfo: d,
              className: _,
              location: E,
              tankmanKind: g,
              onClick: p,
              onMouseDown: b,
              timeToDismiss: h,
              recruitGlowImage: A,
              isInSkin: v,
              isSelectedMode: C = !1,
              disableReason: f,
              disableIcon: D,
              cardState: F = gu.Default,
              isCollapsedOnHover: B = !1,
              isTooltipEnabled: w = !0,
              isSelectedTankmanFromMultySelect: k = !1,
              isSelectedLimitReached: y = !1,
              hasSpecializationLevelPenalty: S = !1,
              hasRolePenalty: L = !1,
              children: T,
            }) => {
              const N = g === Eu.Recruit,
                I = N && C ? gu.Disabled : F,
                x = F === gu.Selected,
                M = I === gu.Disabled,
                R = C && y && !k && !M,
                P = ((e, t, n = 150) => {
                  const u = (0, s.useState)(e),
                    a = u[0],
                    r = u[1],
                    o = hu((e) => r(e), t, n);
                  return {
                    isHovered: a,
                    handleMouseEnter: (0, s.useCallback)(() => o(!0), [o]),
                    handleMouseLeave: (0, s.useCallback)(() => o(!1), [o]),
                  };
                })(!1, []),
                O = P.isHovered,
                H = P.handleMouseEnter,
                W = P.handleMouseLeave,
                G = (0, s.useMemo)(() => {
                  if (A && N) return { backgroundImage: `url(${A})` };
                }, [A, N]);
              (0, s.useEffect)(() => {
                !O || x || M || (U.$.playHighlight(), B && (0, U.G)(eu.gO.SHOP_INFO));
              }, [O, x, M, B]);
              return o().createElement(
                "div",
                {
                  className: l()(
                    ia.base,
                    _,
                    !R && O && ia.base__hovered,
                    R && ia.base__selectDisabled,
                    B && !M && ia.base__isCollapsedOnHover,
                    ia[`base__${k ? "selectedFromMultiselect" : I}`],
                  ),
                  onMouseEnter: H,
                  onMouseLeave: W,
                  onMouseDown: b,
                },
                o().createElement(sa, {
                  isDisabled: M,
                  disableReason: null != f ? f : void 0,
                  disableIcon: null != D ? D : void 0,
                  className: ia.themeHelper,
                }),
                i !== du.Any &&
                  o().createElement(Uu, {
                    role: i,
                    roleIconColor: L ? zu.Red : zu.White,
                    className: ia.crewRole,
                  }),
                o().createElement(Gu, {
                  className: ia.locationIcon,
                  location: E,
                  timeToDismiss: h,
                }),
                o().createElement(
                  "div",
                  { className: ia.iconWrapper, style: G },
                  n &&
                    o().createElement("div", {
                      className: ia.flag,
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.tankmen.card.nations.${n})`,
                      },
                    }),
                  o().createElement(Au.G, {
                    name: m,
                    size: Au.U.c158x118,
                    className: ia.icon,
                    isSkin: v,
                  }),
                ),
                o().createElement(
                  "div",
                  { className: ia.separatorWrapper },
                  o().createElement("div", { className: l()(ia.separator, ia.separator__top) }),
                  o().createElement("div", { className: ia.separator }),
                ),
                o().createElement(
                  "div",
                  { className: ia.content },
                  o().createElement(ku, {
                    fullUserName: c,
                    isRecruit: N,
                    tankmanVehicleInfo: d,
                    specializationLevel: r,
                    hasSpecializationLevelPenalty: S,
                  }),
                  o().createElement(ta, {
                    skills: u,
                    lastSkillLevel: a,
                    className: l()(ia.skills, C && ia.fadeForSkills),
                  }),
                ),
                o().createElement(
                  oa,
                  {
                    args: { tooltipId: N ? mu.XG : mu.v$, targetId: N ? t : e },
                    cantBeSelected: y && !M && !k,
                    isTooltipEnabled: w,
                  },
                  o().createElement("div", {
                    className: ia.helperLayer,
                    onClick: () => {
                      M || x || !p || (p(), U.$.playClick());
                    },
                  }),
                ),
                !M && (null == T ? void 0 : T(O)),
              );
            },
          );
        var ca = n(4385);
        const ma = ({
            startRowIndex: e,
            cellHeight: t,
            paddingTop: n,
            paddingBottom: u,
            amount: a,
            itemsAmountPerRow: r,
            visibleRowsAmount: s,
            numOdfHeadingsBefore: o,
            numOfEmptySlotsInside: i,
          }) => {
            const l = Math.ceil(a / r) * t,
              c = s * t + 40 * i,
              m = e * t + 40 * o;
            return { paddingTop: `${m + n}rem`, paddingBottom: `${Math.max(l - m - c, 0) + u}rem` };
          },
          da = (0, s.memo)((e) => {
            const t = e.className,
              n = e.children,
              u = e.itemsAmountPerRow,
              a = e.visibleRowsAmount,
              r = e.realFirstInRowIndex,
              s = e.amount,
              i = e.numOdfHeadingsBefore,
              l = e.numOfEmptySlotsInside,
              c = Math.min(a * u + l, s - r);
            return o().createElement(
              "div",
              { className: t, style: ma(Object.assign({}, e, { numOdfHeadingsBefore: i })) },
              (0, ca.K)(c, (e) => n(r + e)),
            );
          }),
          _a = "VirtualGrid_base_52",
          Ea = ({
            amount: e,
            headingsIndexes: t,
            cellWidth: n,
            cellHeight: u,
            children: a,
            api: r,
            classNames: i,
            preloadedRows: c = 1,
            paddingTop: m = 0,
            paddingBottom: d = 0,
          }) => {
            const _ = r.scrollApi,
              E = (0, s.useRef)(0),
              g = (0, s.useState)(0),
              p = g[0],
              b = g[1],
              h = (0, s.useState)(null),
              A = h[0],
              v = h[1],
              C = (0, s.useState)(null),
              f = C[0],
              D = C[1];
            ((0, s.useEffect)(() => {
              const t = (t) => {
                if (!A) return;
                const n = Math.floor((F.O.view.pxToRem(t.value.scrollPosition) - m) / u),
                  a = Math.ceil(e / A),
                  s = Math.max(0, Math.min(n - c, a));
                (b(s), r.startRowIndexChanged(s));
              };
              return (_.events.on("change", t), () => _.events.off("change", t));
            }, [r, _, u, m, A, e, c]),
              (0, s.useEffect)(() => {
                const e = () => {
                    if (_.contentRef.current) {
                      const e = getComputedStyle(_.contentRef.current),
                        t = _.contentRef.current.getBoundingClientRect(),
                        a =
                          F.O.view.pxToRem(t.width) -
                          (parseFloat(e.paddingLeft) + parseFloat(e.paddingRight)),
                        s = Math.floor(a / n),
                        o = Math.ceil(F.O.view.pxToRem(t.height) / u) + 2 * c;
                      ((E.current = s), A !== s && v(s), D(o), r.layoutCalculated(s, o));
                    }
                  },
                  t = () => {
                    const t = E.current;
                    (e(), r.scrollToIndex(p * t));
                  };
                return (
                  _.events.on("recalculateContent", e),
                  _.events.on("resizeHandled", t),
                  () => {
                    (_.events.off("recalculateContent", e), _.events.off("resizeHandled", t));
                  }
                );
              }, [r, _, u, n, A, c, p]),
              (0, s.useEffect)(() => {
                const e = (e, t = !0) => {
                  A && _.applyScroll(Math.floor((e + 1) / A) * u + m, { immediate: t });
                };
                return (r.events.on("scrollToIndex", e), () => r.events.off("scrollToIndex", e));
              }, [r, u, A, m, _]));
            const B = (({ api: e, startRowIndex: t, itemsAmountPerRow: n, headingsIndexes: u }) => {
                const a = t * n;
                if (!u) return a;
                const r = u.reduce((e, t, u, r) => {
                  if (t < a) {
                    if (0 === u) return e + 1;
                    const a = (t - 1 - r[u - 1]) % n;
                    e += 1 - (a ? n - a : 0);
                  }
                  return e;
                }, a);
                return (e.firstCardIndexChanged(r), r);
              })({ api: r, headingsIndexes: t, startRowIndex: p, itemsAmountPerRow: A || 4 }),
              w = (({ offset: e, headingsIndexes: t }) => (t ? t.filter((t) => t < e).length : 0))({
                offset: B,
                headingsIndexes: t,
              }),
              k = (({ amount: e, offset: t, headingsIndexes: n }) =>
                n ? n.filter((n) => n >= t && n <= t + e).length : 0)({
                offset: B,
                amount: (f || 1) * (A || 4),
                headingsIndexes: t,
              }),
              y = (({ offset: e, amount: t, itemsAmountPerRow: n, headingsIndexes: u }) =>
                u
                  ? u.reduce((u, a, r, s) => {
                      if (a >= e && a <= e + t) {
                        if (0 === r) return u + 1;
                        const e = (a - 1 - s[r - 1]) % n;
                        u += 1 + (e ? n - e : 0);
                      }
                      return u;
                    }, 0)
                  : 0)({
                headingsIndexes: t,
                offset: B,
                amount: (f || 1) * (A || 4),
                itemsAmountPerRow: A || 4,
              });
            return o().createElement(
              Me.Vertical.Default,
              {
                api: _,
                className: null == i ? void 0 : i.scroll,
                areaClassName: null == i ? void 0 : i.areaClassName,
                scrollClassName: null == i ? void 0 : i.scrollClassName,
                scrollClassNames: {
                  content: null == i ? void 0 : i.content,
                  wrapper: null == i ? void 0 : i.wrapper,
                },
              },
              null !== A &&
                null !== f &&
                o().createElement(
                  da,
                  {
                    className: l()(_a, null == i ? void 0 : i.inner),
                    paddingBottom: d,
                    realFirstInRowIndex: B,
                    numOdfHeadingsBefore: w,
                    numOdfHeadingsInside: k,
                    paddingTop: m,
                    amount: e,
                    itemsAmountPerRow: A,
                    visibleRowsAmount: f,
                    numOfEmptySlotsInside: y,
                    startRowIndex: p,
                    cellHeight: u,
                  },
                  a,
                ),
            );
          },
          ga = "VirtualGridWithFade_scrollAreaFade_94",
          pa = ["api", "children", "classNames"];
        function ba() {
          return (
            (ba =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            ba.apply(this, arguments)
          );
        }
        const ha = (e) => {
            let t = e.api,
              n = e.children,
              u = e.classNames,
              a = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, pa);
            const r = (0, s.useState)(!0),
              i = r[0],
              c = r[1],
              m = t.scrollApi;
            return (
              (0, s.useEffect)(() => {
                const e = () => {
                  const e = m.getBounds()[1];
                  c(Math.abs(e - m.animationScroll.scrollPosition.goal) > 0.1);
                };
                return (
                  m.events.on("change", e),
                  m.events.on("recalculateContent", e),
                  () => {
                    (m.events.off("change", e), m.events.off("recalculateContent", e));
                  }
                );
              }, [m]),
              o().createElement(
                Ea,
                ba(
                  {
                    api: t,
                    classNames: Object.assign({}, u, {
                      scrollClassName: l()(null == u ? void 0 : u.scrollClassName, i && ga),
                    }),
                  },
                  a,
                ),
                n,
              )
            );
          },
          Aa = "TankmanVirtualList_grid_41",
          va = ({
            amount: e,
            headingsIndexes: t,
            paddingTop: n = 11,
            paddingBottom: u = 11,
            api: a,
            children: r,
          }) =>
            o().createElement(
              ha,
              {
                amount: e,
                headingsIndexes: t,
                classNames: { content: Aa },
                cellWidth: 318,
                cellHeight: 265,
                paddingTop: n,
                paddingBottom: u,
                api: a,
              },
              r,
            );
        var Ca = n(7613);
        const fa = "BarracksTankmanCard_headerWrapper_e3",
          Da = "BarracksTankmanCard_header_d6",
          Fa = "Actions_base_07",
          Ba = ({ className: e, children: t }) =>
            o().createElement("div", { className: l()(Fa, e) }, t),
          wa = { base: "VoiceOverButton_base_a3", soundIcon: "VoiceOverButton_soundIcon_8a" },
          ka = ({ onClick: e }) =>
            o().createElement(
              Vn.i,
              {
                header: R.strings.crew.tankman.action.voiceover.tooltip.title(),
                body: R.strings.crew.tankman.action.voiceover.tooltip.body(),
              },
              o().createElement(
                Un.u5,
                {
                  size: Un.qE.small,
                  mixClass: l()(wa.base, wa.base__visible),
                  type: Un.L$.secondary,
                  onClick: e,
                },
                o().createElement("div", { className: wa.soundIcon }),
              ),
            ),
          ya = ({ className: e }) => o().createElement("div", { className: l()(ia.base, e) });
        function Sa() {
          return (
            (Sa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Sa.apply(this, arguments)
          );
        }
        const La = (0, L.Pi)(({ index: e, className: t, onLazyLoad: n }) => {
            const u = $n(),
              a = u.model,
              r = u.controls,
              i = a.computes.getItem(e);
            if (
              ((0, s.useEffect)(() => {
                i || n();
              }, [n, i]),
              !i)
            )
              return o().createElement(ya, { className: t });
            if (-1 === i.tankmanID)
              return o().createElement(
                "div",
                { className: fa },
                o().createElement(Ca.ZP, { className: Da, text: i.fullUserName }),
              );
            const l = i.hasVoiceover && i.tankmanKind === Eu.Recruit;
            return o().createElement(
              la,
              Sa({ key: e }, i, {
                className: t,
                onClick: () => {
                  i.tankmanKind === Eu.Recruit
                    ? r.selectRecruit(i.recruitID)
                    : i.location === _u.Dismissed
                      ? r.restoreTankman(i.tankmanID)
                      : r.selectTankman(i.tankmanID);
                },
              }),
              () =>
                l &&
                o().createElement(
                  Ba,
                  null,
                  o().createElement(ka, { onClick: () => r.playRecruitVoiceover(i.recruitID) }),
                ),
            );
          }),
          Ta = "MemberChangeTankmanList_base_66",
          Na = "MemberChangeTankmanList_gridWrapper_99",
          Ia = "MemberChangeTankmanList_gridWrapper__qHDWidth_14",
          xa = "MemberChangeTankmanList_emptyState_4a",
          Ma = "MemberChangeTankmanList_item_35",
          Ra = "MemberChangeTankmanList_item__withoutTopMargin_c6",
          Pa = R.strings.crew.tankmanList.emptyState,
          Oa = (e) => (e ? eu.Xd : { body: R.strings.crew.tankmanList.tooltip.recruit.body() }),
          Ha = (0, L.Pi)(function ({ isQHD: e, hasTopPadding: t = !0 }) {
            const n = $n(),
              u = n.model,
              a = n.controls,
              r = (() => {
                const e = Me.Vertical.useVerticalScrollApi(),
                  t = X(),
                  n = (0, s.useCallback)((e, n = !0) => t.trigger("scrollToIndex", e, n), [t]),
                  u = (0, s.useCallback)((e, n) => t.trigger("layoutCalculated", e, n), [t]),
                  a = (0, s.useCallback)((e) => t.trigger("startRowIndexChanged", e), [t]),
                  r = (0, s.useCallback)((e) => t.trigger("firstCardIndexChanged", e), [t]);
                return (0, s.useMemo)(
                  () => ({
                    scrollToIndex: n,
                    layoutCalculated: u,
                    startRowIndexChanged: a,
                    firstCardIndexChanged: r,
                    scrollApi: e,
                    events: { off: t.off, on: t.on },
                  }),
                  [n, u, a, r, e, t.off, t.on],
                );
              })(),
              i = u.hasFilters.get(),
              c = u.itemsAmount.get(),
              m = u.computes.getHeadersIndexes(),
              d = ((e, t, n) => {
                const u = (0, s.useRef)([0, 0]),
                  a = (0, s.useRef)(0),
                  r = (0, s.useRef)(0),
                  o = (0, s.useRef)([0, !0]);
                return (
                  (0, s.useEffect)(() => {
                    const e = (e, t) => {
                        u.current = [e, t];
                      },
                      n = (e) => {
                        a.current = e;
                      },
                      s = (e) => {
                        r.current = e;
                      },
                      i = (e) => {
                        const t = o.current[0];
                        o.current = [e.value.scrollPosition, t < e.value.scrollPosition];
                      };
                    return (
                      t.scrollApi.events.on("change", i),
                      t.events.on("layoutCalculated", e),
                      t.events.on("startRowIndexChanged", n),
                      t.events.on("firstCardIndexChanged", s),
                      () => {
                        (t.scrollApi.events.off("change", i),
                          t.events.off("layoutCalculated", e),
                          t.events.off("startRowIndexChanged", n),
                          t.events.off("firstCardIndexChanged", s));
                      }
                    );
                  }, [t]),
                  hu(
                    () => {
                      const t = u.current,
                        n = t[0],
                        a = t[1],
                        s = r.current,
                        i = n * a;
                      e(2 * i, o.current[1] ? s : Math.max(s - 1 * i, 0));
                    },
                    [n],
                    n ? 200 : 10,
                  )
                );
              })(a.loadCards, r);
            return o().createElement(
              "div",
              { className: Ta },
              c > 0
                ? o().createElement(
                    "div",
                    { className: l()(Na, e && Ia) },
                    o().createElement(
                      va,
                      {
                        amount: c,
                        paddingTop: t ? 11 : 0,
                        paddingBottom: t ? 11 : 2,
                        headingsIndexes: m,
                        api: r,
                      },
                      (e) =>
                        o().createElement(La, {
                          className: l()(Ma, !t && Ra),
                          key: e,
                          index: e,
                          onLazyLoad: d,
                        }),
                    ),
                  )
                : o().createElement(
                    cu,
                    {
                      warningText: i ? Pa.noFilteredItems() : Pa.noItems(),
                      buttonType: Jn.L.primary,
                      tooltipArgs: Oa(i),
                      onClick: i ? a.resetFilters : a.recruitNewTankman,
                      className: xa,
                    },
                    i
                      ? Pa.button.resetFilers()
                      : (0, S.uF)(R.strings.crew.memberChange.action.recruit(), {
                          role: R.strings.item_types.tankman.roles.objectiveCase.$dyn(
                            u.requiredRole.get(),
                          ),
                        }),
                  ),
            );
          }),
          Wa = "MemberChangeApp_base_05",
          Ga = "MemberChangeApp_flagIcon_02",
          ja = "MemberChangeApp_widget_30",
          za = "MemberChangeApp_ttc_4a",
          $a = "MemberChangeApp_topButtons_88",
          Ua = "MemberChangeApp_base__qHDWidth_f9",
          Va = "MemberChangeApp_discount_83",
          Za = "MemberChangeApp_content_dc",
          Xa = (0, L.Pi)(() => {
            const e = $n(),
              t = e.model,
              n = e.controls,
              u = t.roleChangeDiscountPercent.get(),
              a = u > 0,
              r = (0, d.GS)(),
              s = r.mediaWidth,
              i = r.mediaHeight,
              c = (0, d.GS)().remScreenWidth >= 2560;
            var m;
            return (
              (m = n.closeWithEsc),
              y(B.n.ESCAPE, m),
              o().createElement(
                "div",
                { className: l()(Wa, c && Ua) },
                o().createElement(ln, {
                  className: Ga,
                  nation: t.nation.get(),
                  size: sn.c1080x454,
                }),
                o().createElement(
                  "div",
                  { className: Za },
                  o().createElement(Qn, { isSmall: s < d.fd.Small }),
                  o().createElement(Rn.p, {
                    popoverDirection: i < d.Aq.Medium ? D.IC.Left : D.IC.Bottom,
                  }),
                  a &&
                    o().createElement(
                      "div",
                      { className: Va },
                      (0, S.uF)(R.strings.crew.memberChange.discount(), { discountAmount: u }),
                    ),
                  o().createElement(Ha, { isQHD: c, hasTopPadding: !a }),
                ),
                o().createElement("div", { className: ja }, o().createElement(Mn.O, null)),
                s >= d.fd.Large &&
                  o().createElement(
                    "div",
                    { className: za },
                    o().createElement(
                      xn,
                      t.vehicleInfo.get(),
                      o().createElement(an, {
                        showBackground: !1,
                        resId: R.views.lobby.hangar.subViews.VehicleParams("resId"),
                      }),
                    ),
                  ),
                o().createElement(vn, {
                  backButtonLabel: t.computes.backButtonLabel(),
                  onBackClick: n.back,
                  closeButtonLabel: R.strings.crew.common.navigation.toGarage(),
                  onCloseClick: n.hangar,
                  className: t.isButtonBarVisible.get() && $a,
                }),
              )
            );
          });
        engine.whenReady.then(() => {
          f().render(
            o().createElement(zn, null, o().createElement(v, null, o().createElement(Xa, null))),
            document.getElementById("root"),
          );
        });
      },
      9367: (e, t, n) => {
        "use strict";
        n.d(t, { Q: () => m });
        var u = n(6483),
          a = n.n(u),
          r = n(9987),
          s = n(6179),
          o = n.n(s);
        const i = "AlertCounter_base_f3",
          l = "AlertCounter_counter_da",
          c = "AlertCounter_label_18",
          m = ({ value: e, className: t }) =>
            o().createElement(
              "div",
              { className: a()(i, t) },
              o().createElement(r.A, { value: e, className: l }),
              !e &&
                o().createElement("div", { className: c }, R.strings.crew.common.exclamationMark()),
            );
      },
      9197: (e, t, n) => {
        "use strict";
        n.d(t, { C: () => D });
        var u = n(6483),
          a = n.n(u),
          r = n(3112),
          s = n(6179),
          o = n.n(s),
          i = n(7613),
          l = n(6373);
        const c = "NumberRange_base_5e",
          m = "NumberRange_base__animation_79",
          d = "NumberRange_from_70",
          _ = "NumberRange_from__red_f8",
          E = "NumberRange_separator_c0",
          g = R.strings.crew.barracks.berthsAmountDivider(),
          p = R.strings.crew.filterPanel.counter.selectLimit,
          b = (0, s.memo)(function ({
            isFilterRange: e,
            from: t,
            to: n,
            className: u,
            isSelectMode: r = !1,
            isSelectedLimitReached: s = !1,
          }) {
            return r
              ? o().createElement(
                  l.i,
                  { header: p.header(), body: p.body(), ignoreShowDelay: !0 },
                  o().createElement(
                    "div",
                    { className: a()(c, u) },
                    o().createElement(i.ZP, { className: d, text: String(t) }),
                    (t !== n || s) &&
                      o().createElement(
                        o().Fragment,
                        null,
                        o().createElement(i.ZP, { className: E, text: g }),
                        o().createElement(i.ZP, { text: String(n) }),
                      ),
                  ),
                )
              : e
                ? o().createElement(
                    "div",
                    { className: a()(c, 0 === t && m, u) },
                    o().createElement(i.ZP, {
                      className: a()(d, 0 === t && n > 0 && _),
                      text: String(t),
                    }),
                    t !== n &&
                      o().createElement(
                        o().Fragment,
                        null,
                        o().createElement(i.ZP, { className: E, text: g }),
                        o().createElement(i.ZP, { text: String(n) }),
                      ),
                  )
                : o().createElement(
                    "div",
                    { className: a()(c, t > n && m, u) },
                    o().createElement(i.ZP, { className: a()(d, t > n && _), text: String(t) }),
                    o().createElement(i.ZP, { className: E, text: g }),
                    o().createElement(i.ZP, { text: String(n) }),
                  );
          }),
          h = "NumberRangeWithLabel_base_2b",
          A = "NumberRangeWithLabel_title_94",
          v = "NumberRangeWithLabel_counter_00",
          C = "NumberRangeWithLabel_counterGlow_1f",
          f = "NumberRangeWithLabel_blink_89",
          D = (0, s.memo)(
            ({
              title: e,
              isGlowVisible: t = !1,
              isSelectedLimitReached: n = !1,
              isFilterRange: u = !1,
              isSelectMode: s = !1,
              className: l,
              classNames: c,
              from: m,
              to: d,
            }) => {
              const _ = (0, r.V)(),
                E = {
                  left:
                    m !== d || n
                      ? 7 * String(m).length * _ + 4 * _
                      : Math.round((7 * String(m).length * _) / 2),
                };
              return o().createElement(
                "div",
                { className: a()(h, l) },
                o().createElement(i.ZP, { className: A, text: e }),
                o().createElement(
                  "div",
                  { className: v },
                  o().createElement(b, {
                    isFilterRange: u,
                    isSelectedLimitReached: n,
                    isSelectMode: s,
                    from: m,
                    to: d,
                  }),
                  t &&
                    u &&
                    o().createElement("div", {
                      style: E,
                      className: a()(C, n && f, null == c ? void 0 : c.counterGlow),
                    }),
                ),
              );
            },
          );
      },
      7077: (e, t, n) => {
        "use strict";
        n.d(t, { G: () => m, U: () => l });
        var u = n(6483),
          a = n.n(u),
          r = n(3649),
          s = n(6179),
          o = n.n(s),
          i = n(3938);
        let l;
        !(function (e) {
          ((e.c158x118 = "big"),
            (e.c100x60 = "small"),
            (e.c100x60Barracks = "barracks"),
            (e.c444x300 = "special"),
            (e.c204x256 = "c_204x256"));
        })(l || (l = {}));
        const c = R.images.gui.maps.icons.tankmen.icons,
          m = (0, s.memo)(({ name: e, size: t = l.c100x60, className: n, isSkin: u = !1 }) => {
            const s = (u ? c.$dyn(t).$dyn("crewSkins") : c.$dyn(t)).$dyn((0, r.BN)(e)),
              m = t === l.c204x256;
            return o().createElement(
              "div",
              {
                style: { backgroundImage: `url(${s})` },
                className: a()(i.Z.base, i.Z[`base__${t}`], n),
              },
              m && o().createElement("div", { className: i.Z.innerShadow }),
            );
          });
      },
      8485: (e, t, n) => {
        "use strict";
        n.d(t, { O: () => l, d: () => c });
        var u = n(6483),
          a = n.n(u),
          r = n(8271),
          s = n(6179),
          o = n.n(s),
          i = n(9426);
        let l;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(l || (l = {}));
        const c = o().memo(function ({ icon: e, type: t, size: n }) {
          const u = (0, s.useMemo)(() => {
              let e;
              return (
                (e =
                  t === r.W.Possible || t === r.W.New
                    ? R.images.gui.maps.icons.tankmen.skills.medium.new_skill()
                    : R.images.gui.maps.icons.crew.$dyn(`${t}SkillFrame_${n}`)),
                { backgroundImage: `url(${e})` }
              );
            }, [t, n]),
            c = (0, s.useMemo)(() => {
              if (!e) return null;
              return {
                backgroundImage: `url(${R.images.gui.maps.icons.tankmen.skills.$dyn(n === l.Big ? "c_22x22" : "small").$dyn(e)})`,
              };
            }, [e, n]);
          return o().createElement(
            "div",
            { className: a()(i.Z.base, i.Z[`base__${n}`]) },
            o().createElement("div", { className: i.Z.bg, style: u }),
            c &&
              o().createElement("div", { className: a()(i.Z.icon, i.Z[`icon__${t}`]), style: c }),
          );
        });
      },
      9631: (e, t, n) => {
        "use strict";
        n.d(t, { C: () => _ });
        var u = n(6483),
          a = n.n(u),
          r = n(3457),
          s = n(2106),
          o = n(9987),
          i = n(6179),
          l = n.n(i),
          c = n(4723);
        const m = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        const _ = l().memo(function (e) {
          let t = e.isActive,
            n = e.counter,
            u = e.className,
            i = e.children,
            _ = e.type,
            E = void 0 === _ ? s.L.secondary : _,
            g = e.size,
            p = void 0 === g ? s.q.small : g,
            b = e.hasIndicator,
            h = void 0 === b || b,
            A = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, m);
          return l().createElement(
            "div",
            { className: a()(c.Z.base, u, t && c.Z.base__active) },
            l().createElement(r.u5, d({ type: E, size: p, mixClass: c.Z.button }, A), i),
            l().createElement("div", { className: c.Z.overlay }),
            h && l().createElement("div", { className: c.Z.indicator }),
            Boolean(n) &&
              l().createElement(
                "div",
                { className: c.Z.counter },
                l().createElement(o.A, { value: n, size: "small" }),
              ),
          );
        });
      },
      7160: (e, t, n) => {
        "use strict";
        n.d(t, { BH: () => r, Fs: () => s, ei: () => u, qb: () => a });
        const u = (e) => Math.sqrt(1 - Math.pow(--e, 2)),
          a = (e) => (e < 0.5 ? 4 * e * e * e : 1 - Math.pow(-2 * e + 2, 3) / 2),
          r = (e) => {
            const t = 1.70158;
            return 1 + 2.70158 * Math.pow(e - 1, 3) + t * Math.pow(e - 1, 2);
          },
          s = (e) => -(Math.cos(Math.PI * e) - 1) / 2;
      },
      8018: (e, t, n) => {
        "use strict";
        n.d(t, { Er: () => i, Gc: () => c, T3: () => r, Xd: () => o, gO: () => l, wP: () => s });
        var u = n(3649);
        const a = R.strings.common.percentValue(),
          r = (e) => (0, u.uF)(a, { value: e });
        let s;
        !(function (e) {
          ((e.Objective = "objective"), (e.Possessive = "possessive"));
        })(s || (s = {}));
        const o = {
            header: R.strings.crew.filterPanel.counter.reset.header(),
            body: R.strings.crew.filterPanel.counter.reset.body(),
          },
          i = {
            header: R.strings.crew.filterPanel.counterMultySelect.reset.header(),
            body: R.strings.crew.filterPanel.counterMultySelect.reset.body(),
          };
        let l;
        !(function (e) {
          ((e.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (e.SHOP_INFO = "shop_info"),
            (e.RUDY = "rudy"));
        })(l || (l = {}));
        const c = (e, t = !1, n = null) => {
          const u = t
            ? R.strings.item_types.tankman.roles.female
            : R.strings.item_types.tankman.roles;
          return (n ? u.$dyn(`${n}Case`) : u).$dyn(e);
        };
      },
      8727: (e, t, n) => {
        "use strict";
        n.d(t, { O: () => uu });
        var u = n(6179),
          a = n.n(u),
          r = n(7727),
          s = n(3403),
          o = n(3215),
          i = n(4598),
          l = n(5175),
          c = n(9480),
          m = n(9174),
          d = n(3946),
          _ = n(4828);
        const E = [
            R.views.lobby.crew.TankmanContainerView("resId"),
            R.views.lobby.crew.personal_case.PersonalFileView("resId"),
            R.views.lobby.crew.personal_case.PersonalDataView("resId"),
            R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
          ],
          g = (0, o.q)()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {},
                  e.primitives([
                    "selectedSlotIdx",
                    "isDisabled",
                    "hasDog",
                    "vehicleName",
                    "vehicleType",
                    "currentLayoutID",
                    "previousLayoutID",
                    "isCrewLocked",
                    "nation",
                    "isAcceleratedTraining",
                    "isExtended",
                  ]),
                  {
                    slots: e.array("slots", []),
                    buttonsBar: e.object("buttonsBar"),
                    crewOperations: e.object("buttonsBar.crewOperations"),
                    crewBooks: e.object("buttonsBar.crewBooks"),
                    wotPlus: e.object("buttonsBar.wotPlus"),
                    isWidgetHover: m.LO.box(!1),
                  },
                ),
                n = (0, d.Om)(() => (0, l.c)(t.slots.get()), { equals: i.jv }),
                u = (0, d.Om)(() => Boolean(c.sE(n(), (e) => -1 === e.tankman.tankmanID))),
                a = (0, d.Om)(() => 1 === t.slots.get().length),
                r = (0, d.Om)((e) => t.selectedSlotIdx.get() === e),
                s = (0, d.Om)(() => -1 !== t.selectedSlotIdx.get()),
                o = (0, d.Om)((e) => {
                  var t;
                  return null == (t = c.U2(n(), e)) ? void 0 : t.tankman;
                }),
                g = (0, d.Om)((e) => {
                  var t;
                  const u = null == (t = c.U2(n(), e)) ? void 0 : t.tankman;
                  return u ? u.skills.length + u.newSkillsAmount + u.possibleSkillsAmount : 0;
                }),
                p = (0, d.Om)(() => {
                  return (
                    (e = t.currentLayoutID.get()),
                    (n = t.previousLayoutID.get()),
                    {
                      isCurrentLayoutHangar: e === R.views.lobby.crew.HangarCrewWidget("resId"),
                      isCurrentLayoutTankmanContainer: E.includes(e),
                      isCurrentLayoutQuickTraining:
                        e === R.views.lobby.crew.QuickTrainingView("resId"),
                      isCurrentLayoutMemberChange:
                        e === R.views.lobby.crew.MemberChangeView("resId"),
                      isPreviousLayoutHangar: n === R.views.lobby.crew.HangarCrewWidget("resId"),
                      isPreviousLayoutTankmanContainer: E.includes(n),
                      isPreviousLayoutQuickTraining:
                        n === R.views.lobby.crew.QuickTrainingView("resId"),
                      isPreviousLayoutMemberChange:
                        n === R.views.lobby.crew.MemberChangeView("resId"),
                      isPreviousLayoutBarrack: n === R.views.lobby.crew.BarracksView("resId"),
                    }
                  );
                  var e, n;
                }),
                b = (0, d.Om)(() => {
                  const e = p(),
                    t = e.isCurrentLayoutHangar,
                    n = e.isCurrentLayoutQuickTraining;
                  return !a() && !t && !n;
                }),
                h = (0, d.Om)(() => !a() && t.buttonsBar.get().isVisible),
                A = (0, d.Om)(() => {
                  return ((e = t.currentLayoutID.get()), _.AB[e] || _.sC.Hangar);
                  var e;
                });
              return Object.assign({}, t, {
                computes: {
                  getSlots: n,
                  isSlotSelected: r,
                  isAnySlotSelected: s,
                  getSlotTankman: o,
                  getAllSkillsAmount: g,
                  isAnyEmptySlots: u,
                  isTankmanMode: a,
                  isChangeCrewButtonVisible: b,
                  isButtonBarVisible: h,
                  getLayoutInfo: p,
                  getUiLoggingParentScreen: A,
                },
              });
            },
            ({ externalModel: e, model: t }) => ({
              onSlotClick: e.createCallback(
                (e, t) => ({ slotIdx: e, tankmanID: t }),
                "onSlotClick",
              ),
              onChangeCrewClick: e.createCallback(
                (e, t) => ({ slotIdx: e, tankmanID: t }),
                "onChangeCrewClick",
              ),
              onCrewBooksClick: e.createCallbackNoArgs("buttonsBar.onCrewBooksClick"),
              onWotPlusClick: e.createCallbackNoArgs("buttonsBar.onWotPlusClick"),
              onDogClick: e.createCallbackNoArgs("onDogClick"),
              onDogMoreInfoClick: e.createCallbackNoArgs("onDogMoreInfoClick"),
              setIsWidgetHover: (0, m.aD)((e) => t.isWidgetHover.set(e)),
            }),
          ),
          p = g[0],
          b = g[1];
        var h = n(6483),
          A = n.n(h),
          v = n(7613),
          C = n(6373),
          f = n(2056);
        let D;
        !(function (e) {
          ((e.On = "on"), (e.Off = "off"), (e.Disabled = "disabled"), (e.Hidden = "hidden"));
        })(D || (D = {}));
        const F = "ButtonsBar_base_9c",
          B = "ButtonsBar_button_d1",
          w = "ButtonsBar_button__crewOperaions_70",
          k = "ButtonsBar_button__crewBooks_b4",
          y = "ButtonsBar_button__toggle_64",
          S = "ButtonsBar_acceleratedTrainingContainer_ee",
          L = "ButtonsBar_acceleratedTrainingContainer__visible_79",
          T = "ButtonsBar_acceleratedTraining_94",
          N = "ButtonsBar_acceleratedTraining__icon_9b",
          I = "ButtonsBar_acceleratedTraining__label_ad";
        var x = n(3457),
          M = n(9987),
          P = n(3649);
        const O = "CrewBookButton_base_da",
          H = "CrewBookButton_button_ee",
          W = "CrewBookButton_icon_11",
          G = "CrewBookButton_discount_6b",
          j = "CrewBookButton_counter_5d",
          z = (0, s.Pi)(({ classMix: e, isWidgetDisabled: t }) => {
            const n = b(),
              u = n.model,
              r = n.controls,
              s = u.crewBooks.get(),
              o = r.onCrewBooksClick;
            return a().createElement(
              C.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.crewBooks.header(),
                body: (0, P.uF)(R.strings.crew_widget.tooltip.buttonsBar.crewBooks.body(), {
                  count: s.totalAmount,
                }),
              },
              a().createElement(
                "div",
                { id: "crew_book_button", className: A()(O, e) },
                a().createElement(
                  x.u5,
                  { type: x.L$.primary, mixClass: H, disabled: s.isDisabled || t, onClick: o },
                  a().createElement("div", { className: W }),
                ),
                s.newAmount > 0 &&
                  a().createElement(
                    "div",
                    { className: j },
                    a().createElement(M.A, { value: s.newAmount }),
                  ),
                s.hasDiscount && a().createElement("div", { className: G }),
              ),
            );
          });
        var $ = n(3616);
        const U = ["children"];
        function V() {
          return (
            (V =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            V.apply(this, arguments)
          );
        }
        const Z = (e) => {
          let t = e.children,
            n = (function (e, t) {
              if (null == e) return {};
              var n,
                u,
                a = {},
                r = Object.keys(e);
              for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
              return a;
            })(e, U);
          return a().createElement(
            $.Z,
            V(
              {
                decoratorId:
                  R.views.common.pop_over_window.backport_pop_over.BackportPopOverWindow("resId"),
                contentId:
                  R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent("resId"),
              },
              n,
            ),
            t,
          );
        };
        var X = n(4489);
        let q;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(q || (q = {}));
        var K = n(1943);
        const Y = "CrewOperationsButton_base_e3",
          Q = "CrewOperationsButton_button_8e",
          J = "CrewOperationsButton_icon_0c",
          ee = "CrewOperationsButton_autoReturnIcon_f0",
          te = (0, s.Pi)(({ classMix: e, isWidgetDisabled: t }) => {
            const n = b().model,
              u = ((e) => {
                const t = (0, K.Jp)(_.D9);
                return (n) => t({ action: _.eX.Click, parentScreen: e, item: n });
              })(n.computes.getUiLoggingParentScreen()),
              r = n.crewOperations.get();
            return a().createElement(
              "div",
              { id: "crew_operations_button", className: A()(Y, e) },
              a().createElement(
                Z,
                {
                  targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  isEnabled: !t,
                  onClick: () => u(_.x3.CrewOperationsButton),
                },
                a().createElement(
                  C.i,
                  {
                    header: R.strings.crew_widget.tooltip.buttonsBar.crewOperations.header(),
                    body: R.strings.crew_widget.tooltip.buttonsBar.crewOperations.body(),
                  },
                  a().createElement(
                    "div",
                    null,
                    a().createElement(
                      x.u5,
                      { type: x.L$.primary, mixClass: Q, disabled: t },
                      a().createElement("div", { className: J }),
                    ),
                    r.isAutoReturnOn && a().createElement("div", { className: ee }),
                  ),
                ),
              ),
            );
          });
        var ne = n(9631);
        const ue = "CrewToggleButton_base_03",
          ae = "CrewToggleButton_button_89",
          re = "CrewToggleButton_iconContainer_f9",
          se = "CrewToggleButton_icon_a7";
        let oe;
        !(function (e) {
          e.WotPlus = "wotPlus";
        })(oe || (oe = {}));
        const ie = (0, u.memo)(({ type: e, state: t, isDisabled: n, onClick: r, classMix: s }) => {
            const o = (0, u.useMemo)(() => {
              const n = t === D.Disabled ? D.Off : t;
              return {
                backgroundImage: `url(R.images.gui.maps.icons.crewWidget.buttonsBar.icons.${e}_${n})`,
              };
            }, [e, t]);
            return a().createElement(
              "div",
              { className: A()(ue, s) },
              a().createElement(
                ne.C,
                {
                  type: x.L$.primary,
                  isActive: t === D.On,
                  disabled: n || t === D.Disabled,
                  className: ae,
                  onClick: r,
                },
                a().createElement(
                  "div",
                  { className: re },
                  a().createElement("div", { className: se, style: o }),
                ),
              ),
            );
          }),
          le = R.strings.crew.acceleratedTraining,
          ce = (0, s.Pi)(({ isWidgetDisabled: e, isCurrentLayoutHangar: t }) => {
            const n = b(),
              u = n.model,
              r = n.controls,
              s = u.isWidgetHover.get(),
              o = u.isAcceleratedTraining.get(),
              i = u.wotPlus.get(),
              l = r.onWotPlusClick;
            return a().createElement(
              "div",
              { className: F },
              a().createElement(te, { classMix: A()(B, w), isWidgetDisabled: e }),
              a().createElement(z, { classMix: A()(B, k), isWidgetDisabled: e }),
              i.state !== D.Hidden &&
                a().createElement(
                  f.u,
                  {
                    contentId: R.views.lobby.crew.CrewHeaderTooltipView("resId"),
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  },
                  a().createElement(
                    "div",
                    null,
                    a().createElement(ie, {
                      type: oe.WotPlus,
                      state: i.state,
                      isDisabled: e || i.isDisabled,
                      onClick: l,
                      classMix: A()(B, y),
                    }),
                  ),
                ),
              a().createElement(
                "div",
                { className: A()(S, (!t || s) && L) },
                o &&
                  a().createElement(
                    C.i,
                    { header: le.tooltip.header(), body: le.tooltip.body() },
                    a().createElement(
                      "div",
                      { className: T },
                      a().createElement("div", { className: N }),
                      a().createElement(v.ZP, { className: I, text: le.label() }),
                    ),
                  ),
              ),
            );
          }),
          me = "CrewWidgetApp_base_cc",
          de = "CrewWidgetApp_buttonsBar_e5",
          _e = "CrewWidgetApp_slotsList_ee";
        var Ee = n(7030),
          ge = n(8018),
          pe = n(7160);
        const be = {
            base: "BaseSlot_base_97",
            base__inactive: "BaseSlot_base__inactive_7e",
            background: "BaseSlot_background_ef",
            background__hovered: "BaseSlot_background__hovered_ee",
            background__inactive: "BaseSlot_background__inactive_6b",
            base__widgetHovered: "BaseSlot_base__widgetHovered_48",
            hoverGlow: "BaseSlot_hoverGlow_de",
            hoverGlow__visible: "BaseSlot_hoverGlow__visible_f4",
            selectedGlow: "BaseSlot_selectedGlow_25",
            selectedGlow__visible: "BaseSlot_selectedGlow__visible_2f",
            hover: "BaseSlot_hover_e9",
            hover__visible: "BaseSlot_hover__visible_1f",
            disabled: "BaseSlot_disabled_67",
          },
          he = (0, u.memo)(
            ({
              onClick: e,
              children: t,
              isSelected: n = !1,
              isDisabled: s,
              isEnabledForMouse: o,
              isEmpty: i = !1,
              isWidgetHovered: l = !0,
              layoutInfo: c,
            }) => {
              const m = (0, u.useState)(!1),
                d = m[0],
                _ = m[1],
                E = d && (!n || (!i && c.isCurrentLayoutMemberChange)),
                g = E && !i && !c.isCurrentLayoutHangar;
              return a().createElement(
                "div",
                {
                  className: A()(
                    be.base,
                    (d || n) && !c.isCurrentLayoutHangar && be.base__hovered,
                    (n || !o) && be.base__inactive,
                    c.isCurrentLayoutHangar && l && be.base__widgetHovered,
                  ),
                  onClick: e,
                  onMouseEnter: () => {
                    o && !n && (r.$.playHighlight(), _(!0));
                  },
                  onMouseLeave: () => {
                    _(!1);
                  },
                },
                a().createElement("div", { className: be.background }),
                !c.isCurrentLayoutMemberChange &&
                  a().createElement("div", {
                    className: A()(be.selectedGlow, n && be.selectedGlow__visible),
                  }),
                a().createElement("div", {
                  className: A()(be.hoverGlow, g && be.hoverGlow__visible),
                }),
                a().createElement("div", { className: A()(be.hover, E && be.hover__visible) }),
                s && a().createElement("div", { className: be.disabled }),
                t,
              );
            },
          ),
          Ae = ({
            startState: e,
            endState: t,
            layoutInfo: n,
            isPaused: r,
            children: s,
            className: o,
            isTankmanMode: i,
          }) => {
            const l = (0, Ee.useSpring)(
                () => ({ from: e, to: t, config: { duration: 300, easing: pe.qb }, pause: r }),
                [r],
              )[0],
              c = (0, u.useMemo)(
                () =>
                  n.isCurrentLayoutHangar || n.isCurrentLayoutQuickTraining || i
                    ? e
                    : (!n.isPreviousLayoutHangar && !n.isPreviousLayoutBarrack) || r
                      ? t
                      : l,
                [n, r, l, e, t, i],
              );
            return a().createElement(Ee.animated.div, { className: o, style: c }, s);
          },
          ve = "DogSlot_base_8f",
          Ce = "DogSlot_icon_ba",
          fe = "DogSlot_container_63",
          De = "DogSlot_roleAndName_c9",
          Fe = "DogSlot_role_5c",
          Be = "DogSlot_name_9c",
          we = "DogSlot_name__hidden_56",
          ke = "DogSlot_btnDetails_b7",
          ye = "DogSlot_btnDetails__hidden_44",
          Se = "DogSlot_infoIcon_09",
          Le = "DogSlot_infoIcon__hidden_8e",
          Te = { transform: "translateX(0rem)" },
          Ne = (0, s.Pi)(({ isDisabled: e, layoutInfo: t }) => {
            const n = b(),
              s = n.model,
              o = n.controls,
              i = s.nation.get(),
              l = s.isWidgetHover.get(),
              c = o.onDogMoreInfoClick,
              m = (0, u.useCallback)(() => {
                !e && (0, r.G)(ge.gO.RUDY);
              }, [e]),
              d = (0, u.useCallback)(
                (t) => {
                  (t.stopPropagation(), !e && c());
                },
                [c, e],
              ),
              _ = (0, Ee.useSpring)(
                () => ({
                  from: Te,
                  to: { transform: "translateX(16rem)" },
                  config: { duration: 300, easing: pe.qb },
                  pause: !t.isCurrentLayoutQuickTraining,
                }),
                [t],
              )[0],
              E = R.strings.tooltips.hangar.crew.rudy.dog.$dyn(i);
            return a().createElement(
              C.i,
              { header: E.header(), body: E.body() },
              a().createElement(
                "div",
                null,
                a().createElement(
                  he,
                  {
                    onClick: m,
                    isDisabled: e,
                    isEnabledForMouse: !1,
                    layoutInfo: t,
                    isWidgetHovered: l,
                  },
                  a().createElement(
                    Ae,
                    {
                      startState: Te,
                      endState: { transform: "translateX(42rem)" },
                      layoutInfo: t,
                      isPaused: !1,
                      className: ve,
                      isTankmanMode: !1,
                    },
                    a().createElement(Ee.animated.div, { className: Ce, style: _ }),
                    a().createElement(
                      "div",
                      { className: fe },
                      a().createElement(
                        "div",
                        { className: De },
                        a().createElement("div", { className: Fe }),
                        a().createElement(v.ZP, {
                          className: A()(Be, t.isCurrentLayoutHangar && !l && we),
                          text: R.strings.menu.hangar.crew.rody.dog.$dyn(i).name(),
                        }),
                      ),
                      a().createElement(
                        "div",
                        { className: A()(ke, t.isCurrentLayoutHangar && !l && ye) },
                        a().createElement(
                          x.u5,
                          { onClick: d },
                          a().createElement(v.ZP, { text: R.strings.crew_widget.btnDetails() }),
                        ),
                      ),
                      a().createElement("div", {
                        className: A()(Se, (!t.isCurrentLayoutHangar || l) && Le),
                      }),
                    ),
                  ),
                ),
              ),
            );
          });
        var Ie = n(4179);
        const xe = ({
            children: e,
            contentID: t,
            decoratorID: n = 0,
            targetId: a = 0,
            args: s,
            isEnabled: o = !0,
            onMouseDown: i,
          }) => {
            const l = (0, u.useCallback)(() => {
                ((0, Ie.c9)(Ie.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: n,
                  targetID: a,
                  isMouseEvent: !0,
                  on: !0,
                  args: s,
                }),
                  r.$.playYes());
              }, [s, t, n, a]),
              c = (0, u.useCallback)(() => {
                (0, Ie.c9)(Ie.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: n,
                  targetID: a,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, n, a]),
              m = (0, u.useCallback)(
                (e) => {
                  (i && i(e), ((e) => e.button === q.RIGHT)(e) && l());
                },
                [i, l],
              );
            return (
              (0, u.useEffect)(() => {
                !1 === o && c();
              }, [o, c]),
              o ? (0, u.cloneElement)(e, { onMouseDown: m }) : e
            );
          },
          Me = ["children"];
        function Re() {
          return (
            (Re =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Re.apply(this, arguments)
          );
        }
        const Pe = (e) => {
            let t = e.children,
              n = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, Me);
            return a().createElement(
              xe,
              Re({}, n, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          Oe = "ChangeCrewButton_base_0f",
          He = "ChangeCrewButton_base__inactive_77",
          We = "ChangeCrewButton_normalState_07",
          Ge = "ChangeCrewButton_normalState__hide_db",
          je = "ChangeCrewButton_hoverState_68",
          ze = "ChangeCrewButton_hoverState__show_89",
          $e = (0, s.Pi)(({ isSelected: e, isLocked: t, mainRole: n, isFemale: s }) => {
            const o = b().model,
              i = (0, u.useState)(!1),
              l = i[0],
              c = i[1],
              m = (0, K.Sr)(_.D9, {
                item: _.x3.ChangeButtonTooltip,
                action: _.eX.Viewed,
                parentScreen: o.computes.getUiLoggingParentScreen(),
              }),
              d = (0, u.useMemo)(
                () =>
                  t
                    ? [
                        R.strings.crew_widget.tooltip.changeCrewButton.unavailable.header(),
                        R.strings.crew_widget.tooltip.changeCrewButton.unavailable.body(),
                      ]
                    : [
                        "",
                        (0, P.uF)(R.strings.crew_widget.changeTankman(), {
                          role: (0, ge.Gc)(n, s, ge.wP.Objective),
                        }),
                      ],
                [t, s, n],
              ),
              E = d[0],
              g = d[1];
            return a().createElement(
              C.i,
              {
                header: E,
                body: g,
                targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                ignoreMouseClick: !0,
              },
              a().createElement(
                "div",
                {
                  className: A()(Oe, (t || e) && He),
                  onMouseEnter: () => {
                    (m.onShow(), t || e || (r.$.playHighlight(), c(!0)));
                  },
                  onMouseLeave: () => {
                    (m.onHide(), c(!1));
                  },
                },
                a().createElement("div", { className: A()(We, l && Ge) }),
                a().createElement("div", { className: A()(je, (e || l) && ze) }),
              ),
            );
          }),
          Ue = "CrewSlot_base_ac",
          Ve = "CrewSlot_changeCrew_02",
          Ze = "CrewSlot_content_5b",
          Xe = "CrewSlot_content__withChangeCrewButton_4e",
          qe = "CrewSlot_warningHighlight_ff",
          Ke = "CrewSlot_selectHighlight_50",
          Ye = "CrewSlot_selectHighlightInTankmanMode_37";
        var Qe = n(7077);
        const Je = "AcceleratedTrainingIcon_base_4f",
          et = "AcceleratedTrainingIcon_icon_45",
          tt = (0, u.memo)(({ classMix: e }) =>
            a().createElement(
              C.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.header(),
                body: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.body(),
              },
              a().createElement(
                "div",
                { className: A()(Je, e) },
                a().createElement("div", { className: et }),
              ),
            ),
          ),
          nt = "SpecializationAndName_base_ef",
          ut = "SpecializationAndName_roleWrapper_87",
          at = "SpecializationAndName_secondaryRolesWrapper_d0",
          rt = "SpecializationAndName_secondaryRolesWrapper__hidden_ac",
          st = "SpecializationAndName_role_55",
          ot = "SpecializationAndName_role__withGap_35",
          it = "SpecializationAndName_percent_e6",
          lt = "SpecializationAndName_percent__untrained_1b",
          ct = "SpecializationAndName_percent__wrapped_9b",
          mt = "SpecializationAndName_acceleratedTrainingIcon_35",
          dt = "SpecializationAndName_name_aa",
          _t = "SpecializationAndName_name__hidden_20";
        function Et() {
          return (
            (Et =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Et.apply(this, arguments)
          );
        }
        const gt = (0, s.Pi)(
            ({
              roles: e,
              specializationLevel: t = 0,
              tankmanID: n,
              isUntrained: u,
              name: r,
              isCurrentLayoutHangar: s,
              isAcceleratedTrainingAvailable: o,
            }) => {
              const i = b().model,
                l = (0, K.Sr)(_.D9, {
                  item: _.x3.MstlTooltip,
                  action: _.eX.Viewed,
                  parentScreen: i.computes.getUiLoggingParentScreen(),
                }),
                c = e[0],
                m = e.slice(1),
                d = i.isWidgetHover.get();
              return a().createElement(
                "div",
                { className: nt },
                a().createElement(
                  f.u,
                  Et(
                    {
                      targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      args: { tankmanID: n },
                      isEnabled: Boolean(n),
                      ignoreMouseClick: !0,
                    },
                    l,
                  ),
                  a().createElement(
                    "div",
                    { className: ut },
                    a().createElement("div", {
                      key: `role__${c}`,
                      className: st,
                      style: {
                        backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(c)})`,
                      },
                    }),
                    a().createElement(
                      "div",
                      { className: A()(at, s && !d && rt) },
                      m.map((e) =>
                        a().createElement("div", {
                          key: `role__${e}`,
                          className: A()(st, ot),
                          style: {
                            backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(e)})`,
                          },
                        }),
                      ),
                    ),
                    t > 0 &&
                      a().createElement(v.ZP, {
                        className: A()(it, u && lt, s && !d && ct),
                        style: { "--marginLeft": -23 * (e.length - 1) + 4 + "rem" },
                        text: (0, P.uF)(R.strings.common.percentValue(), { value: t }),
                      }),
                  ),
                ),
                o && a().createElement(tt, { classMix: mt }),
                a().createElement(v.ZP, { className: A()(dt, s && !d && _t), text: r || "" }),
              );
            },
          ),
          pt = "EmptySlotContent_base_77",
          bt = "EmptySlotContent_tankmanIcon_07",
          ht = "EmptySlotContent_icon_a8",
          At = "EmptySlotContent_specialization_1f",
          vt = "EmptySlotContent_specialization__disabled_3d",
          Ct = "EmptySlotContent_vehicle_55",
          ft = { transform: "translateX(0rem)", opacity: 1 },
          Dt = { transform: "translateX(-70rem)", opacity: 0 },
          Ft = (0, u.memo)(
            ({
              roles: e,
              layoutInfo: t,
              vehicleName: n,
              vehicleType: u,
              isDisabled: r,
              isSelected: s,
              blinkStyle: o,
              qtTankmanIconStyle: i,
            }) => {
              const l = (0, Ee.useSpring)(
                  () => ({
                    from: ft,
                    to: Dt,
                    config: { duration: 200, easing: pe.ei },
                    immediate: !0,
                    pause: s,
                  }),
                  [s],
                ),
                m = l[0],
                d = l[1],
                _ = () => {
                  t.isCurrentLayoutQuickTraining || d.start({ reset: !0, reverse: !0 });
                },
                E = c.U2(e, 0) || "",
                g = R.strings.crew_widget.vehicleWithName.$dyn((0, P.BN)(u)),
                p = (0, P.uF)(R.strings.crew_widget.emptySlot.chooseTankman(), {
                  role: R.strings.item_types.tankman.roles.objectiveCase.$dyn(E),
                });
              return a().createElement(
                "div",
                { className: pt, onMouseEnter: _, onMouseLeave: _ },
                a().createElement(
                  "div",
                  { className: bt },
                  a().createElement(
                    Ee.animated.div,
                    { style: i },
                    a().createElement(Qe.G, {
                      name: "empty",
                      size: Qe.U.c100x60Barracks,
                      className: ht,
                    }),
                    a().createElement(
                      Ee.animated.div,
                      { style: r ? void 0 : o },
                      a().createElement(Qe.G, {
                        name: "emptyRed",
                        size: Qe.U.c100x60Barracks,
                        className: ht,
                      }),
                    ),
                  ),
                ),
                a().createElement(
                  "div",
                  { className: A()(At, r && vt) },
                  a().createElement(gt, {
                    tankmanID: 0,
                    roles: e,
                    name: p,
                    isUntrained: !0,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                  }),
                ),
                a().createElement(
                  Ee.animated.div,
                  { className: Ct, style: s ? void 0 : m },
                  (0, P.uF)(g, { name: n }),
                ),
              );
            },
          );
        var Bt = n(7078),
          wt = n(2603),
          kt = n(5415);
        const yt = (e) => e.skills.length + e.newSkillsAmount + e.possibleSkillsAmount;
        var St = n(8271),
          Lt = n(4385);
        const Tt = {
            base: "RoleLevelIcon_base_e1",
            realLevel: "RoleLevelIcon_realLevel_96",
            base__small: "RoleLevelIcon_base__small_ce",
            icon: "RoleLevelIcon_icon_fa",
          },
          Nt = (0, u.memo)(({ percentValue: e, skillSize: t, hasSkills: n }) => {
            const u = n ? R.strings.crew_widget.plusValue() : R.strings.crew_widget.plusSpecValue();
            return a().createElement(
              C.i,
              {
                header: R.strings.crew_widget.tooltip.roleLevelIcon.header(),
                body: R.strings.crew_widget.tooltip.roleLevelIcon.body(),
              },
              a().createElement(
                "div",
                { className: A()(Tt.base, Tt[`base__${t}`]) },
                a().createElement("div", { className: Tt.icon }),
                a().createElement(
                  "div",
                  { className: Tt.realLevel },
                  a().createElement(v.ZP, {
                    text: u,
                    format: { binding: { value: a().createElement(v.ZP, { text: e }) } },
                  }),
                ),
              ),
            );
          }),
          It = {
            base: "LastSkillInfo_base_38",
            realLevel: "LastSkillInfo_realLevel_78",
            base__small: "LastSkillInfo_base__small_c5",
            possibleLevel: "LastSkillInfo_possibleLevel_02",
            acceleratedTrainingIcon: "LastSkillInfo_acceleratedTrainingIcon_bf",
            base__big: "LastSkillInfo_base__big_10",
          },
          xt = 0.01,
          Mt = (0, u.memo)(
            ({
              lastSkillLevel: e,
              lastPossibleSkillLevel: t,
              showAcceleratedTrainingIcon: n,
              skillSize: r,
              blinkStyle: s,
            }) => {
              const o = (0, u.useRef)(e),
                i = (0, Ee.useSpring)(() => ({ from: { scale: 1 } })),
                l = i[0],
                c = i[1];
              (0, u.useEffect)(() => {
                t < 0 &&
                  o.current !== e &&
                  (c.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: pe.Fs },
                  }),
                  (o.current = e));
              }, [e, t, c]);
              const m = (0, u.useMemo)(
                  () =>
                    0 === t
                      ? [R.strings.common.percentValue(), t]
                      : t < xt
                        ? [R.strings.crew_widget.plusMinValue(), xt]
                        : [R.strings.crew_widget.plusValue(), t],
                  [t],
                ),
                d = m[0],
                _ = m[1];
              return a().createElement(
                "div",
                { className: A()(It.base, It[`base__${r}`]) },
                e >= 0 &&
                  e < 100 &&
                  a().createElement(
                    Ee.animated.div,
                    { style: l },
                    a().createElement(
                      "div",
                      { className: It.realLevel },
                      (0, P.uF)(R.strings.common.percentValue(), {
                        value: e > 0 && e < xt ? xt : e,
                      }),
                    ),
                  ),
                t >= 0 &&
                  t < 100 &&
                  a().createElement(
                    Ee.animated.div,
                    { className: It.possibleLevel, style: s },
                    (0, P.uF)(d, { value: _ }),
                  ),
                n && a().createElement(tt, { classMix: It.acceleratedTrainingIcon }),
              );
            },
          );
        var Rt = n(8485);
        const Pt = 33,
          Ot = 0,
          Ht = !0,
          Wt = "play";
        const Gt = [
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
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            jt.apply(this, arguments)
          );
        }
        const zt = (0, u.memo)(function (e) {
            let t = e.width,
              n = e.height,
              r = e.getImageSource,
              s = e.frameCount,
              o = e.onAnimate,
              i = e.frameTime,
              l = void 0 === i ? Pt : i,
              c = e.initialFrameIndex,
              m = void 0 === c ? Ot : c,
              d = e.lastFrameIndex,
              _ = void 0 === d ? s - 1 : d,
              E = e.loop,
              g = void 0 === E ? Ht : E,
              p = e.state,
              b = void 0 === p ? Wt : p,
              h = e.onAnimationDone,
              A = e.onAnimationComplete,
              v = e.poster,
              C = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, Gt);
            const f = (0, u.useRef)(null);
            return (
              (0, u.useEffect)(() => {
                const e = f.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  n = (n) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(n.img, -n.x, -n.y));
                  };
                switch (b) {
                  case "play":
                    return (function () {
                      const e = Vt(m, _, r),
                        t = $t(m, _),
                        u = window.setInterval(() => {
                          const a = t(),
                            r = e.get(a);
                          r
                            ? (null == o || o(a, r),
                              n(r),
                              a === _ &&
                                (null == A || A(),
                                g || (null == h || h(), window.clearInterval(u))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, l);
                      return () => window.clearInterval(u);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === m && v ? { path: v, x: 0, y: 0 } : r(m),
                        t = new Image();
                      t.src = e.path;
                      const u = () => n(Ut(e, t));
                      return (
                        t.addEventListener("load", u),
                        () => t.removeEventListener("load", u)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [l, r, m, _, g, o, A, h, v, b]),
              a().createElement("canvas", jt({}, C, { width: t, height: n, ref: f }))
            );
          }),
          $t = (e, t) => {
            let n = e;
            return () => {
              const u = n;
              return ((n += 1), n > t && (n = e), u);
            };
          },
          Ut = (e, t) => Object.assign({}, e, { img: t }),
          Vt = (e, t, n) => {
            const u = new Map(),
              a = {};
            for (let r = e; r <= t; r++) {
              const e = n(r),
                t = a[e.path];
              if (t) u.set(r, Ut(e, t));
              else {
                const t = new Image();
                ((a[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${r})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  u.set(r, Ut(e, t)));
              }
            }
            return u;
          };
        const Zt = [
          "width",
          "height",
          "getSrcByFrame",
          "frameCount",
          "onAnimate",
          "frameTime",
          "initialFrameIndex",
          "loop",
          "state",
          "onAnimationComplete",
          "revers",
        ];
        function Xt() {
          return (
            (Xt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Xt.apply(this, arguments)
          );
        }
        let qt;
        !(function (e) {
          ((e.Play = "play"), (e.Stop = "stop"));
        })(qt || (qt = {}));
        const Kt = (e, t, n) => {
            const u = new Image();
            ((u.src = n(t)), e.push(u));
          },
          Yt =
            ((0, u.memo)((e) => {
              let t = e.width,
                n = e.height,
                r = e.getSrcByFrame,
                s = e.frameCount,
                o = e.onAnimate,
                i = void 0 === o ? () => {} : o,
                l = e.frameTime,
                c = void 0 === l ? 33 : l,
                m = e.initialFrameIndex,
                d = void 0 === m ? 0 : m,
                _ = e.loop,
                E = void 0 === _ || _,
                g = e.state,
                p = void 0 === g ? qt.Play : g,
                b = e.onAnimationComplete,
                h = void 0 === b ? () => {} : b,
                A = e.revers,
                v = void 0 !== A && A,
                C = (function (e, t) {
                  if (null == e) return {};
                  var n,
                    u,
                    a = {},
                    r = Object.keys(e);
                  for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                  return a;
                })(e, Zt);
              const f = (0, u.useRef)(null);
              return (
                (0, u.useEffect)(() => {
                  const e = f.current;
                  if (!e) return;
                  const u = s - 1,
                    a = e.getContext("2d"),
                    o = (u) => {
                      (a.clearRect(0, 0, e.width, e.height), a.drawImage(u, 0, 0, t, n));
                    };
                  if ("stop" === p) {
                    const e = r(0),
                      t = new Image();
                    t.src = e;
                    const n = () => o(t);
                    return (t.addEventListener("load", n), () => t.removeEventListener("load", n));
                  }
                  const l = ((e, t, n) => {
                      const u = [];
                      if (n) for (let n = e; n >= 0; n--) Kt(u, n, t);
                      else for (let n = 0; n < e; n++) Kt(u, n, t);
                      return u;
                    })(s, r, v),
                    m = ((e, t = 0) => {
                      let n = t;
                      return () => {
                        const t = n;
                        return ((n += 1), n > e && (n = 0), t);
                      };
                    })(u, d),
                    _ = setInterval(() => {
                      const e = m(),
                        t = l[e];
                      (o(l[e]), i(e, t), e === u && (h(), E || clearInterval(_)));
                    }, c);
                  return () => clearInterval(_);
                }, [s, c, r, n, d, E, i, h, p, t, v]),
                a().createElement("canvas", Xt({}, C, { width: t, height: n, ref: f }))
              );
            }),
            "AnimatedNewSkill_base_6b"),
          Qt = "AnimatedNewSkill_base__big_31";
        function Jt(e, t) {
          var n = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (n) return (n = n.call(e)).next.bind(n);
          if (
            Array.isArray(e) ||
            (n = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return en(e, t);
              var n = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === n && e.constructor && (n = e.constructor.name);
              if ("Map" === n || "Set" === n) return Array.from(e);
              if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                return en(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            n && (e = n);
            var u = 0;
            return function () {
              return u >= e.length ? { done: !0 } : { done: !1, value: e[u++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function en(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var n = 0, u = new Array(t); n < t; n++) u[n] = e[n];
          return u;
        }
        class tn {
          constructor() {
            ((this._intervalID = void 0),
              (this._observers = void 0),
              (this._intervalID = null),
              (this._observers = new Map()));
          }
          static get instance() {
            return (tn._instance || (tn._instance = new tn()), tn._instance);
          }
          subscribe(e) {
            (this._observers.set(e, e),
              1 === this._observers.size &&
                (this._intervalID = window.setInterval(() => {
                  for (var e, t = Jt(this._observers.values()); !(e = t()).done;) {
                    (0, e.value)();
                  }
                }, 5e3)));
          }
          unsubscribe(e) {
            (this._observers.delete(e),
              0 === this._observers.size &&
                null !== this._intervalID &&
                (clearInterval(this._intervalID), (this._intervalID = null)));
          }
        }
        tn._instance = void 0;
        const nn = {
          width: 24,
          height: 24,
          frameCount: 42,
          chunk: { count: 1, columns: 42, rows: 1 },
          getChunkPath:
            ((un = "R.images.gui.maps.icons.sequence.new_skill.skill_"), (e) => `${un}${e}`),
        };
        var un;
        const an = ({ size: e }) => {
            const t = (function (e) {
                const t = e.chunk,
                  n = t.rows * t.columns;
                return (u) => {
                  const a = u % n,
                    r = (a % t.columns) * e.width,
                    s = Math.trunc(a / t.columns) * e.height;
                  return { path: e.getChunkPath(Math.trunc(u / n)), x: r, y: s };
                };
              })(nn),
              n = (0, u.useState)(qt.Stop),
              r = n[0],
              s = n[1],
              o = (0, u.useCallback)(() => {
                s(qt.Play);
              }, [s]),
              i = (0, u.useCallback)(() => {
                s(qt.Stop);
              }, [s]);
            return (
              (0, u.useEffect)(
                () => (tn.instance.subscribe(o), () => tn.instance.unsubscribe(o)),
                [o],
              ),
              a().createElement(zt, {
                width: nn.width,
                height: nn.height,
                frameCount: nn.frameCount,
                getImageSource: t,
                loop: !1,
                state: r,
                onAnimationDone: i,
                className: A()(Yt, e === Rt.O.Big && Qt),
              })
            );
          },
          rn = {
            base: "Skill_base_ba",
            base__big: "Skill_base__big_eb",
            container: "Skill_container_0f",
            divider: "Skill_divider_e8",
            divider__small: "Skill_divider__small_42",
          };
        function sn() {
          return (
            (sn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            sn.apply(this, arguments)
          );
        }
        let on;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(on || (on = {}));
        const ln = (0, u.memo)(
            ({
              name: e,
              icon: t,
              type: n,
              size: r,
              commonMarginValue: s,
              marginValue: o,
              clipWidth: i,
              tankmanID: l,
              blinkStyle: c,
              showNewSkillAnimation: m,
              isTooltipEnabled: d = !0,
              isLastZeroSkill: _ = !1,
            }) => {
              const E = (0, u.useRef)(""),
                g = (0, Ee.useSpring)(() => ({ from: { scale: 1 } })),
                p = g[0],
                b = g[1];
              (0, u.useEffect)(() => {
                (n === St.W.New &&
                  E.current === St.W.Possible &&
                  b.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: pe.Fs },
                  }),
                  (E.current = n));
              }, [n, b]);
              return a().createElement(
                f.u,
                sn(
                  {},
                  (() => {
                    switch (n) {
                      case St.W.Learned:
                      case St.W.ZeroSkill:
                      case St.W.Learning:
                      case St.W.Irrelevant:
                        return {
                          contentId:
                            R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                              "resId",
                            ),
                          args: { tooltipId: wt.HZ, tankmanID: l, skillName: e },
                        };
                      case St.W.New:
                      case St.W.Possible:
                        return {
                          contentId: R.views.lobby.crew.tooltips.PerkAvailableTooltip("resId"),
                          args: { tankmanID: l },
                        };
                    }
                  })(),
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    isEnabled: d,
                    ignoreShowDelay: !0,
                  },
                ),
                a().createElement(
                  Ee.animated.div,
                  { className: rn.container, style: p },
                  a().createElement(
                    Ee.animated.div,
                    { style: n === St.W.Possible ? c : void 0 },
                    a().createElement(
                      "div",
                      {
                        className: A()(rn.base, rn[`base__${r}`]),
                        style: {
                          marginLeft: n !== St.W.ZeroSkill ? `${o}rem` : `${o < 0 ? 2 : o}rem`,
                          clipPath: `inset(0 ${i}rem 0 0)`,
                        },
                      },
                      !m || (n !== St.W.Possible && n !== St.W.New)
                        ? a().createElement(Rt.d, { icon: t, size: r, type: n })
                        : a().createElement(an, { size: r }),
                    ),
                  ),
                  _ &&
                    a().createElement("div", {
                      className: A()(rn.divider, r === on.Small && rn.divider__small),
                      style: { marginRight: (r === on.Small ? 6 : 8) - (o || s || 0) + "rem" },
                    }),
                ),
              );
            },
          ),
          cn = "SkillsList_base_11",
          mn = "SkillsList_numOfSkills_64",
          dn = "SkillsList_numOfSkills__twoRows_8d",
          _n = "SkillsList_numOfSkills__hidden_c5",
          En = "SkillsList_numOfSkillsContent_a4",
          gn = "SkillsList_numOfSkillsContent__withNew_b6",
          pn = "SkillsList_row_03",
          bn = "SkillsList_skillsWithOutLast_02",
          hn = "SkillsList_skillsWithOutLast__hidden_8d",
          An = "SkillsList_lastSkill_96",
          vn = "SkillsList_lastSkill__wrapped_9d",
          Cn = "SkillsList_possibleLevel_97",
          fn = "SkillsList_possibleLevel__before_6f",
          Dn = (0, u.memo)(
            ({
              tankman: e,
              showAcceleratedTrainingIcon: t = !1,
              rowWidth: n = 220,
              maxBigSkillsInRow: r = 10,
              blinkStyle: s,
              isSkillTooltipEnabled: o = !0,
              isCurrentLayoutHangar: i = !1,
              isWidgetHovered: l = !1,
            }) => {
              const c = e.skills,
                m = c.filter((e) => e.type === St.W.ZeroSkill).length,
                d = m > 0 ? c[m - 1].name : null,
                _ = c.length,
                E = yt(e),
                g = ((e, t, n) => {
                  let u = e > t ? 10 : e;
                  const a = 0 === e ? e : Math.ceil(e / u),
                    r = a > 1 ? 16 : 24;
                  let s = 2,
                    o = r;
                  for (; (n - (r + s)) / (o + s) < Math.floor((e - 1) / a);) s > 0 ? s-- : o--;
                  return (
                    (u = Math.min(u, 1 + Math.floor((n - r) / (o + s)))),
                    o !== r && (s = o - r),
                    [a, u, s, r, o]
                  );
                })(E, r, n),
                p = g[0],
                b = g[1],
                h = g[2],
                C = g[3],
                f = g[4],
                D = p > 1 ? on.Small : on.Big,
                F = (0, u.useMemo)(
                  () =>
                    a().createElement(
                      Ee.animated.div,
                      { className: A()(Cn, 0 === _ && fn), style: s },
                      a().createElement(Nt, {
                        percentValue: e.lastPossibleRoleLevel,
                        skillSize: D,
                        hasSkills: e.possibleSkillsAmount > 0 || _ > 0,
                      }),
                    ),
                  [s, D, _, e.lastPossibleRoleLevel, e.possibleSkillsAmount],
                ),
                B = e.skills.filter((e) => e.type === St.W.New).length > 1,
                w = (0, u.useCallback)(
                  (t, n) => {
                    const u = b * t + n;
                    let a = "",
                      r = "",
                      s = St.W.Learned;
                    if (u < _) {
                      const e = c[u];
                      e && ((a = e.name), (r = e.icon), (s = e.type));
                    } else s = u < _ + e.newSkillsAmount ? St.W.New : St.W.Possible;
                    return { skillIndex: u, name: a, icon: r, type: s };
                  },
                  [b, c, _, e.newSkillsAmount],
                ),
                k = Array(p)
                  .fill(null)
                  .reduce((e, t, n) => e + Math.min(b, E - n * b) - 1, 0),
                y = (0, u.useCallback)(
                  (t, n, u) => {
                    const r = n - 1,
                      c = w(t, r),
                      d = c.skillIndex,
                      _ = c.name,
                      E = c.icon,
                      g = c.type,
                      b = 0 === r ? h : 0,
                      v = r * (C + h),
                      f = 2 * (D === on.Big ? 8 : 6) + 1 - h;
                    return a().createElement(
                      "div",
                      {
                        className: A()(An, i && !l && vn),
                        style: {
                          "--leftPosition": -(v + (!(m > 0) || (p > 1 && u) ? 0 : f)) + "rem",
                        },
                      },
                      a().createElement(ln, {
                        name: _,
                        icon: E,
                        type: g,
                        size: D,
                        marginValue: 0 === r ? 0 : h,
                        commonMarginValue: b,
                        key: d + "_" + _,
                        clipWidth: 0,
                        tankmanID: e.tankmanID,
                        blinkStyle: s,
                        isTooltipEnabled: o,
                        showNewSkillAnimation: i,
                      }),
                    );
                  },
                  [w, h, i, l, C, m, p, D, e.tankmanID, s, o],
                );
              return a().createElement(
                "div",
                { className: cn },
                a().createElement(
                  "div",
                  { className: A()(mn, p > 1 && dn, l && _n) },
                  i &&
                    k > 0 &&
                    a().createElement(v.ZP, {
                      className: A()(En, B && gn),
                      text: R.strings.crew_widget.hiddenSkills(),
                      format: { binding: { num: k } },
                    }),
                ),
                (0, Lt.K)(p, (n) => {
                  const u = Math.min(b, E - n * b),
                    r = n === p - 1;
                  return a().createElement(
                    "div",
                    { className: pn, key: `row_${n}` },
                    e.lastPossibleRoleLevel > 0 && 0 === _ && F,
                    a().createElement(
                      "div",
                      { className: A()(bn, i && !l && hn) },
                      (0, Lt.K)(u - 1, (t) => {
                        const r = w(n, t),
                          l = r.skillIndex,
                          c = r.name,
                          m = r.icon,
                          _ = r.type;
                        return a().createElement(ln, {
                          name: c,
                          icon: m,
                          type: _,
                          size: D,
                          marginValue: 0 === t ? 0 : h,
                          commonMarginValue: 0 === t ? h : 0,
                          key: l + "_" + c + "_" + _,
                          clipWidth: t === u - 1 || _ === St.W.ZeroSkill ? 0 : C - f,
                          tankmanID: e.tankmanID,
                          blinkStyle: s,
                          isTooltipEnabled: o,
                          showNewSkillAnimation: i,
                          isLastZeroSkill: c === d,
                        });
                      }),
                    ),
                    y(n, u, r),
                    r &&
                      a().createElement(
                        a().Fragment,
                        null,
                        a().createElement(Mt, {
                          lastSkillLevel: e.possibleSkillsAmount > 0 ? -1 : e.lastSkillLevel,
                          lastPossibleSkillLevel: e.lastPossibleSkillLevel,
                          showAcceleratedTrainingIcon: t,
                          skillSize: D,
                          blinkStyle: s,
                        }),
                        e.lastPossibleRoleLevel > 0 && _ > 0 && F,
                      ),
                  );
                }),
                !p &&
                  a().createElement(
                    "div",
                    { className: pn },
                    e.lastPossibleRoleLevel > 0 && 0 === _ && F,
                    a().createElement(Mt, {
                      lastSkillLevel: e.possibleSkillsAmount > 0 ? -1 : e.lastSkillLevel,
                      lastPossibleSkillLevel: e.lastPossibleSkillLevel,
                      showAcceleratedTrainingIcon: t,
                      skillSize: D,
                      blinkStyle: s,
                    }),
                    e.lastPossibleRoleLevel > 0 && _ > 0 && F,
                  ),
              );
            },
          ),
          Fn = "TankmanInfo_base_69",
          Bn = "TankmanInfo_base__disabled_36",
          wn = "TankmanInfo_tankmanTooltipHoverArea_9b",
          kn = "TankmanInfo_specialization_77",
          yn = "TankmanInfo_specialization__withManySkills_9a",
          Sn = "TankmanInfo_skillsContainer_17",
          Ln = "TankmanInfo_skillsContainer__withManySkills_00",
          Tn = (0, s.Pi)(
            ({ tankman: e, layoutInfo: t, isUntrained: n, blinkStyle: r, isDisabled: s }) => {
              const o = b().model,
                i = (0, kt.GS)().mediaSize,
                l = o.isWidgetHover.get(),
                c = t.isCurrentLayoutQuickTraining || o.computes.isChangeCrewButtonVisible(),
                m = (0, u.useMemo)(() => (c ? (i >= kt.cJ.Small ? 190 : 146) : 220), [c, i]),
                d = ((e, t) => yt(e) > t)(e, 10),
                _ = !t.isCurrentLayoutQuickTraining && -1 !== e.tankmanID && e.isLessMastered,
                E = e.baseSpecializationLevel >= 100;
              return a().createElement(
                "div",
                { className: A()(Fn, s && Bn) },
                a().createElement(
                  Bt.t,
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    args: { tooltipId: wt.v$, tankmanID: e.tankmanID },
                    ignoreShowDelay: !1,
                  },
                  a().createElement("div", { className: wn }),
                ),
                a().createElement(
                  "div",
                  { className: A()(kn, d && yn) },
                  a().createElement(gt, {
                    roles: e.roles,
                    tankmanID: e.tankmanID,
                    specializationLevel: e.specializationLevel,
                    isUntrained: n,
                    name: e.fullName,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                    isAcceleratedTrainingAvailable: _ && !E,
                  }),
                ),
                a().createElement(
                  "div",
                  { className: A()(Sn, d && Ln) },
                  a().createElement(Dn, {
                    tankman: e,
                    showAcceleratedTrainingIcon: _ && E,
                    rowWidth: m,
                    maxBigSkillsInRow: 10,
                    blinkStyle: r,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                    isWidgetHovered: l,
                  }),
                ),
              );
            },
          ),
          Nn = "QuickTrainingTankmanSlotContent_base_8d",
          In = "QuickTrainingTankmanSlotContent_arrow_5a",
          xn = "QuickTrainingTankmanSlotContent_highlight_72",
          Mn = "QuickTrainingTankmanSlotContent_icon_7c",
          Rn = { transform: "translateY(50rem)", opacity: 0, scale: 1 },
          Pn = { transform: "translateY(0rem)", opacity: 1, scale: 1 },
          On = [
            { transform: "translateY(-10rem)", scale: 1.3 },
            { opacity: 0, scale: 1 },
          ],
          Hn = { opacity: 0 },
          Wn = [{ opacity: 1 }, { opacity: 0 }],
          Gn = (0, u.memo)(
            ({
              tankman: e,
              isUntrained: t,
              blinkStyle: n,
              qtTankmanIconStyle: r,
              layoutInfo: s,
              isDisabled: o,
            }) => {
              const i = (0, u.useRef)(e.lastSkillLevelFull),
                l = (0, u.useRef)(e.skills.length),
                c = (0, Ee.useSpring)(() => ({ from: Rn })),
                m = c[0],
                d = c[1],
                _ = (0, Ee.useSpring)(() => ({ from: Hn })),
                E = _[0],
                g = _[1],
                p = (0, u.useRef)(!1);
              return (
                (0, u.useEffect)(() => {
                  e.hasPossibleProgress
                    ? p.current ||
                      (d.start({
                        from: Rn,
                        to: Pn,
                        reverse: false,
                        config: { duration: 300, easing: pe.BH },
                      }),
                      (p.current = !0))
                    : p.current
                      ? (i.current !== e.lastSkillLevelFull || l.current !== e.skills.length
                          ? (d.start({
                              from: Pn,
                              to: On,
                              delay: 200,
                              config: { duration: 500, easing: pe.BH },
                            }),
                            (i.current = e.lastSkillLevelFull),
                            (l.current = e.skills.length),
                            g.start({
                              from: Hn,
                              to: Wn,
                              delay: 200,
                              config: { duration: 500, easing: pe.BH },
                            }))
                          : d.start({ reset: !0, reverse: !0 }),
                        (p.current = !1))
                      : ((i.current = e.lastSkillLevelFull), (l.current = e.skills.length));
                }, [d, g, e.lastSkillLevelFull, e.hasPossibleProgress, e.skills.length]),
                a().createElement(
                  "div",
                  { className: Nn },
                  a().createElement(Ee.animated.div, { className: xn, style: E }),
                  a().createElement(
                    Ee.animated.div,
                    { style: r },
                    a().createElement(Qe.G, {
                      name: e.icon,
                      size: Qe.U.c100x60Barracks,
                      className: Mn,
                      isSkin: e.isInSkin,
                    }),
                  ),
                  a().createElement(Ee.animated.div, { className: In, style: m }),
                  a().createElement(Tn, {
                    tankman: e,
                    layoutInfo: s,
                    isUntrained: t,
                    blinkStyle: n,
                    isDisabled: o,
                  }),
                )
              );
            },
            (e, t) => {
              const n = e.tankman,
                u = t.tankman;
              return (
                n.hasPossibleProgress === u.hasPossibleProgress &&
                ((e, t) => {
                  if (e.length !== t.length) return !1;
                  const n = e.length;
                  for (let r = 0; r < n; r++) {
                    var u, a;
                    if (
                      (null == (u = c.U2(e, r)) ? void 0 : u.name) !==
                      (null == (a = c.U2(t, r)) ? void 0 : a.name)
                    )
                      return !1;
                  }
                  return !0;
                })(n.skills, u.skills) &&
                n.lastSkillLevelFull === u.lastSkillLevelFull &&
                n.possibleSkillsAmount === u.possibleSkillsAmount &&
                n.lastPossibleSkillLevel === u.lastPossibleSkillLevel &&
                n.specializationLevel === u.specializationLevel &&
                n.lastPossibleRoleLevel === u.lastPossibleRoleLevel
              );
            },
          ),
          jn = "TankmanSlotContent_base_00",
          zn = "TankmanSlotContent_icon_ef",
          $n = (0, u.memo)(({ tankman: e, layoutInfo: t, isUntrained: n, isDisabled: u }) =>
            a().createElement(
              "div",
              { className: jn },
              a().createElement(Qe.G, {
                name: e.icon,
                size: Qe.U.c100x60Barracks,
                className: zn,
                isSkin: e.isInSkin,
              }),
              a().createElement(Tn, { tankman: e, layoutInfo: t, isUntrained: n, isDisabled: u }),
            ),
          ),
          Un = (0, u.memo)(
            ({
              roles: e,
              tankman: t,
              layoutInfo: n,
              vehicleName: u,
              vehicleType: r,
              isUntrained: s,
              isDisabled: o,
              isSelected: i,
              blinkSlotStyle: l,
              blinkTankmanStyle: c,
              qtTankmanIconStyle: m,
            }) =>
              -1 === t.tankmanID
                ? a().createElement(Ft, {
                    roles: e,
                    layoutInfo: n,
                    vehicleName: u,
                    vehicleType: r,
                    isDisabled: o,
                    isSelected: i,
                    blinkStyle: c,
                    qtTankmanIconStyle: m,
                  })
                : n.isCurrentLayoutQuickTraining
                  ? a().createElement(Gn, {
                      tankman: t,
                      isUntrained: s,
                      blinkStyle: l,
                      qtTankmanIconStyle: m,
                      layoutInfo: n,
                      isDisabled: o,
                    })
                  : a().createElement($n, {
                      tankman: t,
                      layoutInfo: n,
                      isUntrained: s,
                      isDisabled: o,
                    }),
          ),
          Vn = { transform: "translateX(0rem)" },
          Zn = { transform: "translateX(41rem)" },
          Xn = { opacity: 0 },
          qn = { opacity: 1 },
          Kn = (0, s.Pi)(
            ({
              slotIdx: e,
              roles: t,
              tankman: n,
              layoutInfo: s,
              isSelected: o,
              isAnySlotSelected: i,
              isDisabled: l,
              blinkSlotStyle: c,
              blinkTankmanStyle: m,
              qtTankmanIconStyle: d,
            }) => {
              const E = b(),
                g = E.model,
                p = E.controls,
                h = ((e, t) => {
                  const n = (0, K.Jp)(_.D9),
                    u = (0, X.f)(
                      () => n({ action: _.eX.Click, parentScreen: e, item: t }),
                      [e, t],
                      _.tL,
                    );
                  return (e) => {
                    e.button === q.RIGHT && u();
                  };
                })(g.computes.getUiLoggingParentScreen(), _.x3.SlotContextMenu),
                v = p.onSlotClick,
                C = p.onChangeCrewClick,
                f = g.isWidgetHover.get(),
                D = g.computes.isChangeCrewButtonVisible(),
                F = g.computes.isTankmanMode(),
                B = g.isCrewLocked.get(),
                w = g.vehicleName.get(),
                k = g.vehicleType.get(),
                y = !l && n.isInteractive && (!s.isCurrentLayoutQuickTraining || i),
                S = (0, u.useCallback)(() => {
                  y && !F && ((0, r.G)(R.sounds.yes1()), v(e, n.tankmanID));
                }, [e, n, v, F, y]),
                L = (0, u.useCallback)(
                  (t) => {
                    (t.stopPropagation(), B || ((0, r.G)(R.sounds.yes1()), C(e, n.tankmanID)));
                  },
                  [e, n, C, B],
                ),
                T = (0, u.useMemo)(() => ({ tankmanID: n.tankmanID, slotIdx: e }), [n, e]);
              return a().createElement(
                Pe,
                {
                  args: T,
                  isEnabled: !l,
                  targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  onMouseDown: h,
                },
                a().createElement(
                  "div",
                  null,
                  a().createElement(
                    he,
                    {
                      onClick: S,
                      isSelected: o,
                      isDisabled: l,
                      isEmpty: -1 === n.tankmanID,
                      layoutInfo: s,
                      isEnabledForMouse: y,
                      isWidgetHovered: f,
                    },
                    a().createElement(
                      "div",
                      { className: Ue },
                      n.hasWarning && a().createElement("div", { className: qe }),
                      o && a().createElement("div", { className: F ? Ye : Ke }),
                      a().createElement(
                        Ae,
                        {
                          startState: Vn,
                          endState: Zn,
                          layoutInfo: s,
                          isPaused: !D,
                          className: A()(Ze, D && Xe),
                          isTankmanMode: F,
                        },
                        a().createElement(Un, {
                          roles: t,
                          tankman: n,
                          layoutInfo: s,
                          isUntrained: n.isUntrained,
                          isDisabled: l,
                          vehicleName: w,
                          vehicleType: k,
                          blinkSlotStyle: c,
                          blinkTankmanStyle: m,
                          qtTankmanIconStyle: d,
                          isSelected: o,
                        }),
                      ),
                      D &&
                        a().createElement(
                          "div",
                          { onClick: L },
                          a().createElement(
                            Ae,
                            {
                              startState: Xn,
                              endState: qn,
                              layoutInfo: s,
                              isPaused: !D,
                              className: Ve,
                              isTankmanMode: F,
                            },
                            a().createElement($e, {
                              isSelected: s.isCurrentLayoutMemberChange && o,
                              isLocked: B,
                              mainRole: t[0] || "",
                              isFemale: -1 !== n.tankmanID && n.isFemale,
                            }),
                          ),
                        ),
                    ),
                  ),
                ),
              );
            },
          ),
          Yn = "SlotsList_base_5f";
        function Qn() {
          return (
            (Qn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Qn.apply(this, arguments)
          );
        }
        const Jn = { transform: "translateX(0rem)" },
          eu = { transform: "translateX(15rem)" },
          tu = (0, s.Pi)(({ layoutInfo: e, isWidgetDisabled: t, className: n }) => {
            const r = b().model,
              s = r.computes.isAnyEmptySlots(),
              o = (0, Ee.useSpring)(
                () => ({
                  from: { opacity: 1 },
                  to: [{ opacity: 0 }, { opacity: 1 }],
                  config: { duration: 750, easing: pe.Fs },
                  loop: !0,
                }),
                [],
              ),
              i = o[0],
              l = o[1];
            (0, u.useEffect)(() => {
              s ? l.resume() : l.pause();
            }, [l, s]);
            const c = (0, Ee.useSpring)(
                () => ({
                  from: { opacity: 1 },
                  to: [{ opacity: 0.3 }, { opacity: 1 }],
                  config: { duration: 400, easing: pe.Fs },
                  loop: !0,
                }),
                [],
              ),
              m = c[0],
              d = c[1];
            (0, u.useEffect)(() => {
              e.isCurrentLayoutQuickTraining ? d.resume() : d.pause();
            }, [d, e.isCurrentLayoutQuickTraining]);
            const _ = (0, Ee.useSpring)(() => ({
                from: Jn,
                to: eu,
                delay: 200,
                config: { duration: 300, easing: pe.ei },
                pause: !e.isCurrentLayoutQuickTraining,
              }))[0],
              E = (0, u.useCallback)(
                (n) => t || (e.isCurrentLayoutQuickTraining && -1 === n),
                [t, e.isCurrentLayoutQuickTraining],
              );
            return a().createElement(
              "div",
              { id: "crew_widget_slots_list", className: A()(Yn, n) },
              r.computes
                .getSlots()
                .map((t, n) =>
                  a().createElement(
                    Kn,
                    Qn({}, t, {
                      layoutInfo: e,
                      key: `slot_${n}_${t.tankman.tankmanID}`,
                      isSelected:
                        !e.isCurrentLayoutHangar &&
                        (r.computes.isSlotSelected(t.slotIdx) || r.computes.isTankmanMode()),
                      isAnySlotSelected: r.computes.isAnySlotSelected(),
                      isDisabled: E(t.tankman.tankmanID),
                      blinkSlotStyle: m,
                      blinkTankmanStyle: i,
                      qtTankmanIconStyle: _,
                    }),
                  ),
                ),
            );
          }),
          nu = (0, s.Pi)(() => {
            const e = b(),
              t = e.model,
              n = e.controls,
              s = t.isDisabled.get(),
              o = t.hasDog.get(),
              i = t.computes.getLayoutInfo(),
              l = t.isExtended.get();
            return (
              (0, u.useEffect)(() => {
                n.setIsWidgetHover(l);
              }, [l, n]),
              a().createElement(
                "div",
                {
                  className: me,
                  onMouseEnter: () => {
                    l ||
                      (n.setIsWidgetHover(!0),
                      i.isCurrentLayoutHangar && !s && (0, r.G)(R.sounds.crew_hover()));
                  },
                  onMouseLeave: () => {
                    l ||
                      (n.setIsWidgetHover(!1),
                      i.isCurrentLayoutHangar && !s && (0, r.G)(R.sounds.crew_unhover()));
                  },
                },
                t.computes.isButtonBarVisible() &&
                  a().createElement(
                    "div",
                    { className: de },
                    a().createElement(ce, {
                      isWidgetDisabled: s,
                      isCurrentLayoutHangar: i.isCurrentLayoutHangar,
                    }),
                  ),
                a().createElement(tu, { layoutInfo: i, isWidgetDisabled: s, className: _e }),
                o && a().createElement(Ne, { layoutInfo: i, isDisabled: s }),
              )
            );
          }),
          uu = (0, u.memo)(() =>
            a().createElement(
              p,
              { options: { rootId: R.views.lobby.crew.widgets.CrewWidget("resId") } },
              a().createElement(nu, null),
            ),
          );
      },
      4543: (e, t, n) => {
        "use strict";
        n.d(t, { p: () => Ue });
        var u = n(6179),
          a = n.n(u),
          r = n(6483),
          s = n.n(r),
          o = n(3457),
          i = n(2106),
          l = n(7613),
          c = n(6373);
        let m;
        !(function (e) {
          ((e.Default = "default"),
            (e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(m || (m = {}));
        var d = n(3403),
          _ = n(3415),
          E = n(9480),
          g = n(9631);
        const p = "FilterTitle_base_a7",
          b = "FilterTitle_label_05",
          h = "FilterTitle_discount_42",
          A = "FilterTitle_discountIcon_30",
          v = ({ label: e, hasDiscount: t, className: n }) =>
            a().createElement(
              "div",
              { className: s()(p, n) },
              a().createElement("div", { className: b }, e),
              t &&
                a().createElement(
                  "div",
                  { className: h },
                  a().createElement("div", { className: A }),
                ),
            );
        let C;
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
        })(C || (C = {}));
        var f = n(3649);
        const D = "ToggleIcon_base_59",
          F = "ToggleIcon_base__small_3e",
          B = "ToggleIcon_icon_e7",
          w = a().memo(function ({ icon: e, isSmall: t = !1, classNames: n }) {
            return a().createElement(
              "div",
              { className: s()(D, t && F) },
              a().createElement("div", {
                className: s()(B, null == n ? void 0 : n.icon),
                style: { backgroundImage: `url(${e})` },
              }),
            );
          });
        var k = n(9690);
        const y = "VehicleTier_base_9c",
          S = "VehicleTier_base__small_fc",
          L = ({ level: e, isSmall: t = !1 }) =>
            a().createElement("div", { className: s()(y, t && S) }, (0, k.HG)(e)),
          T = {
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
          N = ({ id: e, icon: t, type: n, isSmall: u = !0, isSelected: r = !1 }) =>
            n === C.VehicleTier
              ? a().createElement(L, { isSmall: u, level: Number(e) })
              : a().createElement(w, {
                  icon: t,
                  isSmall: u,
                  classNames: {
                    icon: s()(
                      T[`icon__${n}`],
                      T[`icon__${n}${(0, f.e)(e)}`],
                      r && T.icon__selected,
                    ),
                  },
                }),
          I = {
            base: "FilterToggleGroup_base_69",
            title: "FilterToggleGroup_title_65",
            content: "FilterToggleGroup_content_80",
            toggle: "FilterToggleGroup_toggle_d4",
            base__inPopup: "FilterToggleGroup_base__inPopup_11",
          };
        function x() {
          return (
            (x =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            x.apply(this, arguments)
          );
        }
        let M;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(M || (M = {}));
        const P = ({ header: e, body: t, contentId: n, targetId: u }) =>
            n
              ? { contentId: n, targetId: u }
              : t || e
                ? { header: null != e ? e : void 0, body: null != t ? t : void 0 }
                : void 0,
          O = ({
            id: e,
            type: t,
            label: n,
            hasDiscount: u,
            filters: r,
            onClick: o,
            className: i,
            toggleProps: l,
            theme: c = M.Default,
          }) => {
            const m = c === M.InPopup;
            return a().createElement(
              "div",
              { className: s()(I.base, I[`base__${c}`], i) },
              m && a().createElement(v, { className: I.title, label: n, hasDiscount: u }),
              a().createElement(
                "div",
                { className: I.content },
                E.UI(r, ({ id: n, isSelected: u, tooltip: r, icon: i, counter: c }) =>
                  a().createElement(
                    _.l,
                    { key: n, tooltipArgs: P(r), className: I.toggle },
                    a().createElement(
                      g.C,
                      x({}, l, {
                        className: s()(I.toggle, null == l ? void 0 : l.className),
                        isActive: u,
                        onClick: () => (null == o ? void 0 : o(e, n)),
                        counter: c,
                      }),
                      a().createElement(N, { id: n, icon: i, type: t, isSmall: m, isSelected: u }),
                    ),
                  ),
                ),
              ),
            );
          };
        var H = n(9197),
          W = n(3215),
          G = n(4598),
          j = n(5175),
          z = n(3946);
        const $ = (0, W.q)()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  amountInfo: e.object("amountInfo"),
                  filter: e.array("filter"),
                  filters: e.array("filter.filters"),
                },
                n = (0, z.Om)(() => (0, j.c)(t.filter.get()), { equals: G.jv }),
                u = (0, z.Om)(() => (0, j.c)(t.filters.get()), { equals: G.jv }),
                a = (0, z.Om)(
                  () =>
                    (0, j.c)(t.filters.get()).filter((e) => "dismissed" === e.id && e.isSelected)
                      .length > 0,
                  { equals: G.jv },
                );
              return Object.assign({}, t, {
                computes: { getFilterGroup: n, getFilters: u, getIsRestoreFilter: a },
              });
            },
            ({ externalModel: e }) => ({
              search: e.createCallback((e) => ({ value: e }), "onSearch"),
              updateFilter: e.createCallback(
                (e, t) => ({ groupID: e, toggleID: t }),
                "onUpdateFilter",
              ),
              resetFilter: e.createCallbackNoArgs("onResetFilter"),
              updateSelectMode: e.createCallbackNoArgs("onSelectedModeChange"),
              onCancelSelection: e.createCallbackNoArgs("onCancelSelection"),
              onDismissOrRestore: e.createCallbackNoArgs("onDismissOrRestore"),
            }),
          ),
          U = $[0],
          V = $[1];
        var Z = n(3616),
          X = n(1037),
          q = n(9367);
        const K = "PopupButton_base_7c",
          Y = "PopupButton_popupButtonLabel_ed",
          Q = "PopupButton_buttonIconWrapper_d7",
          J = "PopupButton_buttonIcon_e0",
          ee = "PopupButton_buttonIcon__isHighlighted_84",
          te = "PopupButton_discountAlert_c8",
          ne = ({ isHighlighted: e, hasDiscountAlert: t, popoverDirection: n = X.IC.Bottom }) =>
            a().createElement(
              "div",
              { className: K },
              a().createElement(
                "div",
                { className: Y },
                R.strings.crew.filter.popup.button.title(),
              ),
              a().createElement(
                Z.Z,
                {
                  contentId: R.views.lobby.crew.popovers.FilterPopoverView("resId"),
                  targetId: R.views.lobby.crew.widgets.FilterPanelWidget("resId"),
                  direction: n,
                },
                a().createElement(
                  "div",
                  { id: "popup_btn", className: Q },
                  a().createElement(
                    g.C,
                    { type: o.L$.ghost, size: o.qE.small, isActive: e, hasIndicator: !1 },
                    a().createElement("div", { className: s()(J, e && ee) }),
                  ),
                  t && a().createElement(q.Q, { className: te }),
                ),
              ),
            );
        var ue = n(8018);
        const ae = "ResetButton_base_58",
          re = "ResetButton_button_a5",
          se = "ResetButton_icon_4a",
          oe = ({ isSelectMode: e, onClick: t }) =>
            a().createElement(
              "div",
              { className: ae },
              a().createElement(
                c.i,
                e ? ue.Er : ue.Xd,
                a().createElement(
                  o.u5,
                  { mixClass: re, onClick: t, type: o.L$.ghost, size: o.qE.small },
                  a().createElement("div", { className: se }),
                ),
              ),
            );
        var ie = n(7078),
          le = n(2056);
        const ce = ["children", "tooltipType", "wrap"],
          me = ["contentId"];
        function de() {
          return (
            (de =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            de.apply(this, arguments)
          );
        }
        function _e(e, t) {
          if (null == e) return {};
          var n,
            u,
            a = {},
            r = Object.keys(e);
          for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
          return a;
        }
        let Ee;
        !(function (e) {
          ((e.Base = "base"), (e.Backport = "backport"), (e.Simple = "simple"));
        })(Ee || (Ee = {}));
        const ge = (e) => {
            let t = e.children,
              n = e.tooltipType,
              u = e.wrap,
              r = void 0 !== u && u,
              s = _e(e, ce);
            if (!s) return t;
            const o =
                r && (s.isEnabled || void 0 === s.isEnabled)
                  ? a().createElement("div", null, t)
                  : t,
              i = s.contentId,
              l = _e(s, me);
            switch (n) {
              case Ee.Base:
                return (
                  !i && console.error("`contentId` field is required for a base Tooltip"),
                  i ? a().createElement(le.u, de({}, l, { contentId: i }), o) : o
                );
              case Ee.Simple:
                return a().createElement(c.i, l, o);
              case Ee.Backport:
                return a().createElement(ie.t, l, o);
              default:
                return a().createElement(_.l, { tooltipArgs: s }, o);
            }
          },
          pe = "default",
          be = "search",
          he = "email",
          Ae = "password",
          ve = "normal",
          Ce = "disabled",
          fe = "alert",
          De = "error",
          Fe = "medium",
          Be = {
            [pe]: "",
            [he]: R.strings.common.input.placeholder.email(),
            [be]: R.strings.common.input.placeholder.search(),
            [Ae]: R.strings.common.input.placeholder.password(),
          },
          we = { [pe]: "text", [he]: "text", [be]: "text", [Ae]: "password" },
          ke = { [pe]: "", [he]: "Invalid email", [be]: "", [Ae]: "" },
          ye = R.images.gui.maps.icons.components.input;
        function Se(e, t) {
          return (
            t !== he ||
            (function (e) {
              const t = e.match(
                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
              );
              return Boolean(t);
            })(e)
          );
        }
        var Le = n(7727);
        const Te = {
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
          Ne = a().memo(
            ({
              componentId: e,
              value: t = "",
              type: n = pe,
              size: r = Fe,
              variant: o = ve,
              placeholder: i = "",
              highlighted: l,
              withClear: c,
              selectOnFocus: m = !0,
              maxLength: d,
              iconSource: _,
              classMix: E,
              onMouseEnter: g,
              onMouseLeave: p,
              onMouseDown: b,
              onMouseUp: h,
              onClick: A,
              onChange: v,
              onClear: C,
              onFocus: f,
              onBlur: D,
            }) => {
              const F = (0, u.useState)(!1),
                B = F[0],
                w = F[1],
                k = (0, u.useRef)(null),
                y = (0, u.useRef)({ mouseOver: !1, mouseDown: !1 }),
                S = o !== Ce,
                L = (0, u.useCallback)(
                  (e) => {
                    S && (w(!0), f && f(e));
                  },
                  [S, f],
                ),
                T = (0, u.useCallback)(
                  (e) => {
                    S && !y.current.mouseOver && (w(!1), D && D(e));
                  },
                  [S, D],
                );
              (0, u.useEffect)(() => {
                S && B && m && k.current && k.current.select();
              }, [m, B, S]);
              const N = (0, u.useCallback)(
                  (e) => {
                    S && v && v(e.target.value);
                  },
                  [S, v],
                ),
                I = (0, u.useCallback)(
                  (e) => {
                    S && ((y.current.mouseOver = !0), g && g(e));
                  },
                  [S, g],
                ),
                x = (0, u.useCallback)(
                  (e) => {
                    S &&
                      k.current &&
                      (y.current.mouseDown && k.current.focus(),
                      (y.current.mouseOver = !1),
                      p && p(e));
                  },
                  [S, p],
                ),
                M = (0, u.useCallback)(
                  (e) => {
                    S && ((y.current.mouseDown = !0), b && b(e));
                  },
                  [S, b],
                ),
                R = (0, u.useCallback)(
                  (e) => {
                    S && ((y.current.mouseDown = !1), h && h(e));
                  },
                  [S, h],
                ),
                P = (0, u.useCallback)(
                  (e) => {
                    if (S && k.current) {
                      ((!B || (B && e.target !== k.current)) && k.current.focus(), A && A(e));
                    }
                  },
                  [B, S, A],
                ),
                O = i || Be[n],
                H = Boolean(_),
                W = s()(
                  Te.base,
                  Te[`base__${r}`],
                  l && Te[`base__${o}`],
                  B && Te.base__focused,
                  H && Te.base__withIcon,
                  E,
                ),
                G = (0, u.useMemo)(() => (_ ? { backgroundImage: `url(${_})` } : null), [_]),
                j = s()(Te.input, Te[`input__${n}`]),
                z = s()(Te.icon, Te[`icon__${n}`]),
                $ = s()(Te.placeholder, Te[`placeholder__${n}`]);
              return a().createElement(
                "div",
                {
                  id: e,
                  className: W,
                  onMouseEnter: I,
                  onMouseDown: M,
                  onMouseUp: R,
                  onMouseLeave: x,
                  onClick: P,
                },
                !S && a().createElement("div", { className: Te.disabled }),
                G && a().createElement("div", { style: G, className: z }),
                a().createElement("input", {
                  ref: k,
                  className: j,
                  type: we[n],
                  value: t,
                  onChange: N,
                  disabled: !S,
                  onFocus: L,
                  onBlur: T,
                  maxLength: d,
                }),
                O && !t && !B && a().createElement("div", { className: $ }, O),
                c &&
                  a().createElement("div", {
                    className: Te.clear,
                    onClick: (e) => {
                      (Le.$.playClick(), C && C(e));
                    },
                    onMouseEnter: Le.$.playHighlight,
                  }),
              );
            },
          ),
          Ie = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          xe = ({ variant: e, show: t = !0, helperText: n, helperIcon: r, classMix: o }) => {
            const i = (0, u.useMemo)(() => {
                const t =
                  r ||
                  (function (e) {
                    return e === fe ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(e);
                return t && { backgroundImage: `url(${t})` };
              }, [r, e]),
              l = s()(Ie.base, t && Ie.base__shown),
              c = s()(Ie.message, Ie[`message__${e}`], o);
            return a().createElement(
              "div",
              { className: l },
              i && a().createElement("div", { className: Ie.icon, style: i }),
              a().createElement("div", { className: c }, n),
            );
          },
          Me = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          Re = [
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
        function Pe() {
          return (
            (Pe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var n = arguments[t];
                  for (var u in n) Object.prototype.hasOwnProperty.call(n, u) && (e[u] = n[u]);
                }
                return e;
              }),
            Pe.apply(this, arguments)
          );
        }
        const Oe = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          He = (e) => {
            let t = e.componentId,
              n = e.type,
              r = void 0 === n ? pe : n,
              o = e.variant,
              i = void 0 === o ? ve : o,
              l = e.size,
              c = void 0 === l ? Fe : l,
              m = e.value,
              d = e.tooltipArgs,
              _ = e.helperText,
              E = void 0 === _ ? "" : _,
              g = e.isValidated,
              p = void 0 === g || g,
              b = e.showHelper,
              h = void 0 === b || b,
              A = e.error,
              v = e.options,
              C = e.onFocus,
              f = e.onMouseEnter,
              D = e.onMouseLeave,
              F = e.onMouseUp,
              B = e.onMouseDown,
              w = e.onChange,
              k = e.classMix,
              y = e.controlClassMix,
              S = e.helperClassMix,
              L = (function (e, t) {
                if (null == e) return {};
                var n,
                  u,
                  a = {},
                  r = Object.keys(e);
                for (u = 0; u < r.length; u++) ((n = r[u]), t.indexOf(n) >= 0 || (a[n] = e[n]));
                return a;
              })(e, Re);
            const T = (0, u.useState)(m),
              N = T[0],
              I = T[1],
              x = (0, u.useState)(p),
              M = x[0],
              R = x[1],
              P = (0, u.useMemo)(() => Object.assign({}, Oe, v), [v]),
              O = (0, u.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: m, type: r }),
              H = (0, u.useCallback)((e) => {
                e !== O.current.value &&
                  ((O.current.value = e), (O.current.isChangeHandled = !1), I(e));
              }, []),
              W = (0, u.useCallback)(
                (e) => {
                  let t = !0;
                  (P.performChangeValidation &&
                    (t = P.changesValidator ? P.changesValidator(e) : Se(e, O.current.type)),
                    w && w(e, t));
                },
                [w, P],
              ),
              G = (0, u.useCallback)(() => {
                O.current.debounceTimeout &&
                  (window.clearTimeout(O.current.debounceTimeout), (O.current.debounceTimeout = 0));
              }, []),
              j = (0, u.useCallback)(() => H(""), [H]);
            (0, u.useEffect)(() => () => G(), [G]);
            const z = (0, u.useCallback)(
              (e) => {
                (G(),
                  P.debounceTime
                    ? (O.current.debounceTimeout = window.setTimeout(() => {
                        W(e);
                      }, P.debounceTime))
                    : W(e));
              },
              [W, G, P.debounceTime],
            );
            ((0, u.useEffect)(() => {
              O.current.isChangeHandled ||
                O.current.value !== N ||
                (z(O.current.value), (O.current.isChangeHandled = !0));
            }, [N, z]),
              (0, u.useEffect)(() => {
                (O.current.isChangeHandled &&
                  m !== O.current.value &&
                  ((O.current.value = m), I(m)),
                  (O.current.type = r));
              }, [m, r]),
              (0, u.useEffect)(() => {
                R(p);
              }, [p, i]));
            const $ = (0, u.useCallback)((e) => f && f(e), [f]),
              U = (0, u.useCallback)(
                (e) => {
                  (P.disableHighlightOnFocus && M && R(!1), C && C(e));
                },
                [M, C, P.disableHighlightOnFocus],
              ),
              V = (0, u.useCallback)((e) => F && F(e), [F]),
              Z = (0, u.useCallback)((e) => B && B(e), [B]),
              X = (0, u.useCallback)((e) => D && D(e), [D]),
              q = (0, u.useMemo)(
                () =>
                  P.withTypeIcon
                    ? (function (e, t) {
                        return e === be ? ye.$dyn(`search_${t}`) : "";
                      })(r, c)
                    : "",
                [r, c, P.withTypeIcon],
              ),
              K = E || ke[r],
              Y = Boolean(N),
              Q = A ? De : i,
              J = Boolean(A) || M,
              ee = (0, u.useMemo)(
                () => ("boolean" == typeof P.withClear ? Y && P.withClear : Y && r === be),
                [r, Y, P],
              ),
              te = s()(Me.base, Me[`base__${c}`], Me[`base__${i}`], k);
            return a().createElement(
              "div",
              {
                id: t,
                className: te,
                onMouseEnter: $,
                onMouseDown: Z,
                onMouseUp: V,
                onMouseLeave: X,
              },
              a().createElement(
                ge,
                Pe({ wrap: !0 }, d),
                a().createElement(
                  Ne,
                  Pe(
                    {
                      componentId: t ? `${t}-inputControl` : void 0,
                      iconSource: q,
                      size: c,
                      type: r,
                      variant: Q,
                      value: N,
                      withClear: ee,
                      highlighted: J,
                      selectOnFocus: P.selectOnFocus,
                      maxLength: P.maxLength,
                      classMix: y,
                      onFocus: U,
                      onChange: H,
                      onClear: j,
                    },
                    L,
                  ),
                ),
              ),
              K &&
                a().createElement(
                  "div",
                  { className: Me.helper },
                  a().createElement(xe, {
                    variant: Q,
                    show: h && (P.isPermanentHelper || J),
                    helperText: A || K,
                    helperIcon: P.helperIconSource,
                    classMix: S,
                  }),
                ),
            );
          },
          We = ({
            value: e,
            placeholder: t,
            tooltipHeader: n,
            onChange: u,
            className: r,
            tooltipBody: s,
          }) =>
            a().createElement(
              c.i,
              { header: null != n ? n : void 0, body: s, isEnabled: Boolean(n || s) },
              a().createElement(He, {
                type: be,
                placeholder: null != t ? t : void 0,
                value: e,
                classMix: r,
                onChange: u,
              }),
            ),
          Ge = {
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
        var je = n(5415);
        const ze = R.strings.crew.filterPanel,
          $e = (0, d.Pi)(({ popoverDirection: e }) => {
            const t = V(),
              n = t.model,
              u = t.controls,
              r = n.root.get(),
              d = r.hasDiscountAlert,
              _ = r.isPopoverHighlighted,
              E = r.isPopoverEnabled,
              g = r.searchTooltipBody,
              p = r.searchTooltipHeader,
              b = r.searchPlaceholder,
              h = r.searchString,
              A = r.isSearchEnabled,
              v = r.title,
              C = r.panelType,
              f = r.hasAppliedFilters,
              D = r.popoverTooltipHeader,
              F = r.popoverTooltipBody,
              B = r.isSelectedMode,
              w = r.isSelectButtonVisible,
              k = r.isSelectButtonActive,
              y = r.isSelectedLimitReached,
              S = n.amountInfo.get(),
              L = S.from,
              T = S.to,
              N = n.computes.getFilterGroup(),
              I = n.computes.getFilters(),
              x = n.computes.getIsRestoreFilter(),
              M = f || (0 === L && 0 === T) || B,
              P =
                (0, je.GS)().mediaSize === je.cJ.ExtraSmall && B
                  ? R.strings.crew.tankmanList.selected.titleSmall()
                  : v;
            return a().createElement(
              "div",
              { className: s()(Ge.base, Ge[`base__${C}`]) },
              a().createElement(
                "div",
                { className: Ge.titleWrapper },
                a().createElement(H.C, {
                  title: P || "",
                  isGlowVisible: M,
                  isSelectedLimitReached: y,
                  isFilterRange: !0,
                  isSelectMode: B,
                  from: L,
                  to: T,
                  className: Ge.title,
                  classNames: { counterGlow: Ge.counterGlow },
                }),
                f && a().createElement(oe, { isSelectMode: B, onClick: u.resetFilter }),
              ),
              a().createElement(
                "div",
                { className: Ge.filters },
                A &&
                  a().createElement(
                    a().Fragment,
                    null,
                    a().createElement(We, {
                      value: h,
                      onChange: u.search,
                      className: Ge.search,
                      placeholder: b,
                      tooltipHeader: p,
                      tooltipBody: g,
                    }),
                    C === m.Barracks && w && a().createElement("div", { className: Ge.separator }),
                  ),
                N.label && a().createElement(l.ZP, { className: Ge.filterLabel, text: N.label }),
                w &&
                  (B
                    ? a().createElement(
                        a().Fragment,
                        null,
                        a().createElement(
                          o.u5,
                          { mixClass: Ge.button, type: i.L.primary, onClick: u.onCancelSelection },
                          a().createElement(l.ZP, { text: ze.demobilize.cancel() }),
                        ),
                        a().createElement(
                          o.u5,
                          {
                            mixClass: s()(Ge.button, Ge.button__demobilize),
                            type: i.L.main,
                            onClick: u.onDismissOrRestore,
                            disabled: !k,
                          },
                          a().createElement(l.ZP, {
                            text: x ? ze.restore.confirm() : ze.demobilize.confirm(),
                          }),
                        ),
                      )
                    : a().createElement(
                        o.u5,
                        { mixClass: Ge.button, type: i.L.secondary, onClick: u.updateSelectMode },
                        a().createElement(l.ZP, { text: ze.selectMode.title() }),
                      )),
                (w || A) && a().createElement("div", { className: Ge.separator }),
                a().createElement(O, {
                  id: N.id,
                  label: N.label,
                  type: N.type,
                  hasDiscount: N.hasDiscount,
                  filters: I,
                  toggleProps: { type: i.L.ghost },
                  onClick: u.updateFilter,
                }),
                E &&
                  a().createElement(
                    c.i,
                    { header: D || void 0, body: F || void 0, isEnabled: Boolean(D || F) },
                    a().createElement(
                      "div",
                      { className: Ge.popupButtonWrapper },
                      a().createElement(ne, {
                        isHighlighted: _,
                        hasDiscountAlert: d,
                        popoverDirection: e,
                      }),
                    ),
                  ),
              ),
            );
          }),
          Ue = ({ popoverDirection: e }) =>
            a().createElement(
              U,
              { options: { rootId: R.views.lobby.crew.widgets.FilterPanelWidget("resId") } },
              a().createElement($e, { popoverDirection: e }),
            );
      },
      8271: (e, t, n) => {
        "use strict";
        let u;
        (n.d(t, { W: () => u }),
          (function (e) {
            ((e.New = "new"),
              (e.Learned = "learned"),
              (e.Learning = "learning"),
              (e.Irrelevant = "irrelevant"),
              (e.Possible = "possible"),
              (e.ZeroSkill = "zeroSkill"));
          })(u || (u = {})));
      },
      2603: (e, t, n) => {
        "use strict";
        n.d(t, { HZ: () => u, XG: () => r, v$: () => a });
        const u = "crewPerkGf",
          a = "tankman",
          r = "tankmanNotRecruited";
      },
      5026: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
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
      6880: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
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
      8055: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
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
      5287: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = { base: "FormatText_base_d0" };
      },
      4769: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
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
      3393: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
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
      3938: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
          base: "TankmanIcon_base_f9",
          base__big: "TankmanIcon_base__big_98",
          base__small: "TankmanIcon_base__small_b2",
          base__barracks: "TankmanIcon_base__barracks_62",
          base__special: "TankmanIcon_base__special_3f",
          base__c_204x256: "TankmanIcon_base__c_204x256_97",
          innerShadow: "TankmanIcon_innerShadow_c6",
        };
      },
      9426: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
          base: "TankmanSkill_base_84",
          base__big: "TankmanSkill_base__big_a0",
          bg: "TankmanSkill_bg_f9",
          icon: "TankmanSkill_icon_1b",
          icon__irrelevant: "TankmanSkill_icon__irrelevant_50",
        };
      },
      4723: (e, t, n) => {
        "use strict";
        n.d(t, { Z: () => u });
        const u = {
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
    var t = __webpack_module_cache__[e];
    if (void 0 !== t) return t.exports;
    var n = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](n, n.exports, __webpack_require__), n.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, n, u) => {
      if (!t) {
        var a = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, n, u] = deferred[i], r = !0, s = 0; s < t.length; s++)
            (!1 & u || a >= u) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[s]))
              ? t.splice(s--, 1)
              : ((r = !1), u < a && (a = u));
          if (r) {
            deferred.splice(i--, 1);
            var o = n();
            void 0 !== o && (e = o);
          }
        }
        return e;
      }
      u = u || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > u; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, n, u];
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
    (__webpack_require__.j = 906),
    (() => {
      var e = { 906: 0, 3: 0, 595: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, n) => {
          var u,
            a,
            [r, s, o] = n,
            i = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (u in s) __webpack_require__.o(s, u) && (__webpack_require__.m[u] = s[u]);
            if (o) var l = o(__webpack_require__);
          }
          for (t && t(n); i < r.length; i++)
            ((a = r[i]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        n = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (n.forEach(t.bind(null, 0)), (n.push = t.bind(null, n.push.bind(n))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(2258));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
