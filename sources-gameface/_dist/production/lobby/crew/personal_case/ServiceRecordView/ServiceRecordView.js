(() => {
  var __webpack_modules__ = {
      3779: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => F });
        var n = t(6483),
          r = t.n(n),
          a = t(9887),
          i = t.n(a),
          s = t(3377),
          o = t(6179),
          l = t.n(o),
          c = t(5026);
        const E = [
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
        function m() {
          return (
            (m =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            m.apply(this, arguments)
          );
        }
        Object.keys(i());
        const d = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          A = (Object.keys(d), ["mt", "mr", "mb", "ml"]),
          _ = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          F = (0, s.ZP)((e) => {
            let u = e.className,
              t = e.width,
              n = e.height,
              a = e.m,
              i = e.mt,
              s = void 0 === i ? a : i,
              F = e.mr,
              D = void 0 === F ? a : F,
              B = e.mb,
              C = void 0 === B ? a : B,
              g = e.ml,
              h = void 0 === g ? a : g,
              p = e.column,
              v = e.row,
              f = e.flexDirection,
              b = void 0 === f ? (p ? "column" : v && "row") || void 0 : f,
              w = e.flexStart,
              S = e.center,
              x = e.flexEnd,
              y = e.spaceBetween,
              k = e.spaceAround,
              T = e.justifyContent,
              L =
                void 0 === T
                  ? (w ? "flex-start" : S && "center") ||
                    (x && "flex-end") ||
                    (y && "space-between") ||
                    (k && "space-around") ||
                    void 0
                  : T,
              N = e.alignItems,
              R =
                void 0 === N
                  ? (w ? "flex-start" : S && "center") || (x && "flex-end") || void 0
                  : N,
              M = e.alignSelf,
              O = e.wrap,
              P = e.flexWrap,
              I = void 0 === P ? (O ? "wrap" : void 0) : P,
              H = e.grow,
              W = e.shrink,
              V = e.flex,
              Z = void 0 === V ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : V,
              j = e.style,
              z = e.children,
              G = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, E);
            const U = (0, o.useMemo)(() => {
                const e = { mt: s, mr: D, mb: C, ml: h },
                  u = ((e) =>
                    A.reduce((u, t) => {
                      const n = e[t];
                      return n && "number" != typeof n ? u.concat(d[!0 === n ? "MD" : n][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    A.reduce((u, t) => {
                      const n = e[t];
                      return ("number" == typeof n && (u[_[t]] = n + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, j, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: Z,
                    alignSelf: M,
                    display: b || R ? "flex" : void 0,
                    flexDirection: b,
                    flexWrap: I,
                    justifyContent: L,
                    alignItems: R,
                  }),
                  computedClassNames: u,
                };
              }, [t, n, s, D, C, h, j, Z, M, b, I, L, R]),
              X = U.computedStyle,
              $ = U.computedClassNames;
            return l().createElement(
              "div",
              m({ className: r()(c.Z.base, ...$, u), style: X }, G),
              z,
            );
          });
      },
      3457: (e, u, t) => {
        "use strict";
        t.d(u, { L$: () => l.L, qE: () => l.q, u5: () => E });
        var n = t(6483),
          r = t.n(n),
          a = t(7727),
          i = t(6179),
          s = t.n(i),
          o = t(6880),
          l = t(2106);
        const c = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: c,
          mixClass: E,
          soundHover: m,
          soundClick: d,
          onMouseEnter: A,
          onMouseMove: _,
          onMouseDown: F,
          onMouseUp: D,
          onMouseLeave: B,
          onClick: C,
        }) => {
          const g = (0, i.useRef)(null),
            h = (0, i.useState)(t),
            p = h[0],
            v = h[1],
            f = (0, i.useState)(!1),
            b = f[0],
            w = f[1],
            S = (0, i.useState)(!1),
            x = S[0],
            y = S[1],
            k = (0, i.useCallback)(() => {
              c || (g.current && (g.current.focus(), v(!0)));
            }, [c]),
            T = (0, i.useCallback)(
              (e) => {
                p && null !== g.current && !g.current.contains(e.target) && v(!1);
              },
              [p],
            ),
            L = (0, i.useCallback)(
              (e) => {
                c || (C && C(e));
              },
              [c, C],
            ),
            N = (0, i.useCallback)(
              (e) => {
                c || (null !== m && (0, a.G)(m), A && A(e), y(!0));
              },
              [c, m, A],
            ),
            M = (0, i.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            O = (0, i.useCallback)(
              (e) => {
                c || (D && D(e), w(!1));
              },
              [c, D],
            ),
            P = (0, i.useCallback)(
              (e) => {
                c || (null !== d && (0, a.G)(d), F && F(e), t && k(), w(!0));
              },
              [c, d, F, k, t],
            ),
            I = (0, i.useCallback)(
              (e) => {
                c || (B && B(e), w(!1));
              },
              [c, B],
            ),
            H = r()(
              o.Z.base,
              o.Z[`base__${n}`],
              {
                [o.Z.base__disabled]: c,
                [o.Z[`base__${u}`]]: u,
                [o.Z.base__focus]: p,
                [o.Z.base__highlightActive]: b,
                [o.Z.base__firstHover]: x,
              },
              E,
            ),
            W = r()(o.Z.state, o.Z.state__default);
          return (
            (0, i.useEffect)(
              () => (
                document.addEventListener("mousedown", T),
                () => {
                  document.removeEventListener("mousedown", T);
                }
              ),
              [T],
            ),
            (0, i.useEffect)(() => {
              v(t);
            }, [t]),
            s().createElement(
              "div",
              {
                ref: g,
                className: H,
                onMouseEnter: N,
                onMouseMove: M,
                onMouseUp: O,
                onMouseDown: P,
                onMouseLeave: I,
                onClick: L,
              },
              n !== l.L.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: o.Z.back }),
                  s().createElement("span", { className: o.Z.texture }),
                ),
              s().createElement(
                "span",
                { className: W },
                s().createElement("span", { className: o.Z.stateDisabled }),
                s().createElement("span", { className: o.Z.stateHighlightHover }),
                s().createElement("span", { className: o.Z.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: o.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
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
        const E = (0, i.memo)(c);
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
      280: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => l });
        var n = t(6179),
          r = t.n(n),
          a = t(6483),
          i = t.n(a),
          s = t(3649),
          o = t(5287);
        const l = ({ binding: e, text: u = "", classMix: t, alignment: a = s.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                n.Fragment,
                null,
                u.split("\n").map((u, l) =>
                  r().createElement(
                    "div",
                    { className: i()(o.Z.base, t), key: `${u}-${l}` },
                    (0, s.Uw)(u, a, e).map((e, u) =>
                      r().createElement(n.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => E });
        var n = t(3138),
          r = t(6179),
          a = t(1043),
          i = t(5262);
        const s = n.O.client.getSize("rem"),
          o = s.width,
          l = s.height,
          c = Object.assign({ width: o, height: l }, (0, i.T)(o, l, a.j)),
          E = (0, r.createContext)(c);
      },
      1039: (e, u, t) => {
        "use strict";
        var n = t(6179),
          r = t.n(n),
          a = t(6536),
          i = t(3495),
          s = t(1043),
          o = t(5262),
          l = t(3138);
        (0, n.memo)(({ children: e }) => {
          const u = (0, n.useContext)(i.Y),
            t = (0, n.useState)(u),
            c = t[0],
            E = t[1],
            m = (0, n.useCallback)((e, u) => {
              const t = l.O.view.pxToRem(e),
                n = l.O.view.pxToRem(u);
              E(Object.assign({ width: t, height: n }, (0, o.T)(t, n, s.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", m);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", m), [m]));
          const d = (0, n.useMemo)(() => Object.assign({}, c), [c]);
          return r().createElement(i.Y.Provider, { value: d }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var n = t(6179),
          r = t(7382),
          a = t(3495);
        const i = ["children"];
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
            })(e, i);
          const s = (0, n.useContext)(a.Y),
            o = s.extraLarge,
            l = s.large,
            c = s.medium,
            E = s.small,
            m = s.extraSmall,
            d = s.extraLargeWidth,
            A = s.largeWidth,
            _ = s.mediumWidth,
            F = s.smallWidth,
            D = s.extraSmallWidth,
            B = s.extraLargeHeight,
            C = s.largeHeight,
            g = s.mediumHeight,
            h = s.smallHeight,
            p = s.extraSmallHeight,
            v = { extraLarge: B, large: C, medium: g, small: h, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && o) return u;
            if (t.large && l) return u;
            if (t.medium && c) return u;
            if (t.small && E) return u;
            if (t.extraSmall && m) return u;
          } else {
            if (t.extraLargeWidth && d) return (0, r.H)(u, t, v);
            if (t.largeWidth && A) return (0, r.H)(u, t, v);
            if (t.mediumWidth && _) return (0, r.H)(u, t, v);
            if (t.smallWidth && F) return (0, r.H)(u, t, v);
            if (t.extraSmallWidth && D) return (0, r.H)(u, t, v);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return u;
              if (t.largeHeight && C) return u;
              if (t.mediumHeight && g) return u;
              if (t.smallHeight && h) return u;
              if (t.extraSmallHeight && p) return u;
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
        t.d(u, { YN: () => n.Y });
        (t(6010), t(1039));
        var n = t(3495);
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
      2773: (e, u, t) => {
        "use strict";
        t.d(u, { $Q: () => C });
        var n = t(6483),
          r = t.n(n),
          a = t(7515),
          i = t(1856),
          s = t(3815),
          o = t(560),
          l = t(7727),
          c = t(6179),
          E = t.n(c),
          m = t(6358),
          d = t(372);
        const A = "disable",
          _ = { pending: !1, offset: 0 },
          F = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          D = () => {},
          B = (e, u) => Math.max(20, e.offsetWidth * u),
          C = (0, c.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = F, onDrag: n = D }) => {
              const C = (0, c.useRef)(null),
                g = (0, c.useRef)(null),
                h = (0, c.useRef)(null),
                p = (0, c.useRef)(null),
                v = (0, c.useRef)(null),
                f = e.stepTimeout || 100,
                b = (0, c.useState)(_),
                w = b[0],
                S = b[1],
                x = (0, c.useCallback)(
                  (e) => {
                    (S(e),
                      v.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: v.current }));
                  },
                  [n],
                ),
                y = () => {
                  const u = p.current,
                    t = v.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const i = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    o = (0, a.u)(0, 1, i / (r - n)),
                    l = (u.offsetWidth - B(u, s)) * o;
                  ((t.style.transform = `translateX(${0 | l}px)`),
                    ((e) => {
                      if (g.current && h.current && p.current && v.current) {
                        if (0 === e)
                          return (g.current.classList.add(A), void h.current.classList.remove(A));
                        if (
                          ((u = p.current),
                          (t = v.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (g.current.classList.remove(A), void h.current.classList.add(A));
                        var u, t;
                        (g.current.classList.remove(A), h.current.classList.remove(A));
                      }
                    })(l));
                },
                k = (0, s.z)(() => {
                  ((() => {
                    const u = v.current,
                      t = p.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && u && n && t)) return;
                    const a = Math.min(1, n / r);
                    ((u.style.width = `${B(t, a)}px`),
                      (u.style.display = "flex"),
                      C.current &&
                        (1 === a
                          ? C.current.classList.add(d.Z.base__nonActive)
                          : C.current.classList.remove(d.Z.base__nonActive)));
                  })(),
                    y());
                });
              ((0, c.useEffect)(() => (0, i.v)(k)),
                (0, c.useEffect)(
                  () =>
                    (0, i.v)(() => {
                      const u = () => {
                        y();
                      };
                      let t = D;
                      const n = () => {
                        (t(), (t = (0, i.v)(k)));
                      };
                      return (
                        e.events.on("recalculateContent", k),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", n),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", k),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, c.useEffect)(() => {
                  if (!w.pending) return;
                  const u = (u) => {
                      var t;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const a = p.current,
                        i = v.current;
                      if (!r || !a || !i) return;
                      const s = u.screenX - w.offset - a.getBoundingClientRect().x,
                        o = (s / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, o),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: i, thumbOffset: s, contentOffset: o }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), x(_));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, w.offset, w.pending, n, x]));
              const T = (0, o.B)((u) => e.applyStepTo(u), f, [e]),
                L = T[0],
                N = T[1];
              (0, c.useEffect)(
                () => (
                  document.addEventListener("mouseup", N, !0),
                  () => document.removeEventListener("mouseup", N, !0)
                ),
                [N],
              );
              const R = (e) => {
                e.target.classList.contains(A) || (0, l.G)("highlight");
              };
              return E().createElement(
                "div",
                { className: r()(d.Z.base, u.base), ref: C, onWheel: e.handleMouseWheel },
                E().createElement("div", {
                  className: r()(d.Z.leftButton, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(A) ||
                      0 !== e.button ||
                      ((0, l.G)("play"), L(m.Nm.Next));
                  },
                  onMouseUp: N,
                  ref: g,
                  onMouseEnter: R,
                }),
                E().createElement(
                  "div",
                  {
                    className: r()(d.Z.track, u.track),
                    onMouseDown: (u) => {
                      const n = v.current;
                      if (n && 0 === u.button)
                        if (((0, l.G)("play"), u.target === n))
                          x({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = v.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const a = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * u);
                          })(u.screenX > n.getBoundingClientRect().x ? m.Nm.Prev : m.Nm.Next);
                        }
                    },
                    ref: p,
                    onMouseEnter: R,
                  },
                  E().createElement("div", { ref: v, className: r()(d.Z.thumb, u.thumb) }),
                  E().createElement("div", { className: r()(d.Z.rail, u.rail) }),
                ),
                E().createElement("div", {
                  className: r()(d.Z.rightButton, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(A) ||
                      0 !== e.button ||
                      ((0, l.G)("play"), L(m.Nm.Prev));
                  },
                  onMouseUp: N,
                  ref: h,
                  onMouseEnter: R,
                }),
              );
            },
          );
      },
      2840: (e, u, t) => {
        "use strict";
        t.d(u, { K: () => c });
        var n = t(6483),
          r = t.n(n),
          a = t(6179),
          i = t.n(a),
          s = t(2773),
          o = t(7950),
          l = t(4682);
        const c = ({
          children: e,
          api: u,
          className: t,
          barClassNames: n,
          areaClassName: c,
          classNames: E,
          scrollClassName: m,
          getStepByRailClick: d,
          onDrag: A,
        }) => {
          const _ = (0, a.useMemo)(() => {
              const e = n || {};
              return Object.assign({}, e, { base: r()(l.Z.base, e.base) });
            }, [n]),
            F = (0, a.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
          return i().createElement(
            "div",
            { className: r()(l.Z.defaultScroll, t), onWheel: u.handleMouseWheel },
            i().createElement(
              "div",
              { className: r()(l.Z.defaultScrollArea, c) },
              i().createElement(o.Area, { className: m, api: F, classNames: E }, e),
            ),
            i().createElement(s.$Q, { getStepByRailClick: d, api: u, onDrag: A, classNames: _ }),
          );
        };
      },
      7950: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            Area: () => d,
            Bar: () => o.$Q,
            DefaultScroll: () => l.K,
            Direction: () => m.Nm,
            defaultSettings: () => m.he,
            useHorizontalScrollApi: () => m.T5,
          }));
        var n = t(6483),
          r = t.n(n),
          a = t(1856),
          i = t(6179),
          s = t.n(i),
          o = t(2773),
          l = t(2840),
          c = t(4682),
          E = t(8579),
          m = t(6358);
        const d = ({ api: e, className: u, classNames: t, children: n, style: o }) => (
          (0, i.useEffect)(() => (0, a.v)(e.recalculateContent)),
          s().createElement(
            "div",
            { className: r()(c.Z.base, u), style: o },
            s().createElement(
              "div",
              {
                className: r()(c.Z.wrapper, null == t ? void 0 : t.wrapper),
                onWheel: e.handleMouseWheel,
                ref: e.wrapperRef,
              },
              s().createElement(
                "div",
                { className: r()(c.Z.content, null == t ? void 0 : t.content), ref: e.contentRef },
                n,
              ),
            ),
          )
        );
        ((d.Bar = o.$Q), (d.Default = l.K), (d.SeniorityAwards = E.Tm));
      },
      8579: (e, u, t) => {
        "use strict";
        t.d(u, { Tm: () => l });
        var n = t(6483),
          r = t.n(n),
          a = t(1856),
          i = t(6179),
          s = t.n(i),
          o = (t(2773), t(2840), t(4682));
        t(6358);
        const l = ({ api: e, className: u, classNames: t, children: n }) => (
          (0, i.useEffect)(() => (0, a.v)(e.recalculateContent)),
          s().createElement(
            "div",
            { className: r()(o.Z.base, u) },
            s().createElement(
              "div",
              { className: r()(o.Z.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
              s().createElement(
                "div",
                { className: r()(o.Z.content, null == t ? void 0 : t.content), ref: e.contentRef },
                n,
              ),
            ),
          )
        );
      },
      6358: (e, u, t) => {
        "use strict";
        t.d(u, { Nm: () => n.Nm, T5: () => r, he: () => n.he });
        var n = t(7308);
        const r = (0, n.EO)({
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
          getDirection: (e) => (e.deltaY > 1 ? n.Nm.Next : n.Nm.Prev),
          triggerMouseMoveOnUpdate: !0,
        });
      },
      6225: (e, u, t) => {
        "use strict";
        t.d(u, { $Q: () => g });
        var n = t(6483),
          r = t.n(n),
          a = t(7515),
          i = t(1856),
          s = t(3815),
          o = t(560),
          l = t(7727),
          c = t(6179),
          E = t.n(c),
          m = t(7701),
          d = t(9168);
        const A = "disable",
          _ = () => {},
          F = { pending: !1, offset: 0 },
          D = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          B = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          C = (e, u) => Math.max(20, e.offsetHeight * u),
          g = (0, c.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = D, onDrag: n = _ }) => {
              const g = (0, c.useRef)(null),
                h = (0, c.useRef)(null),
                p = (0, c.useRef)(null),
                v = (0, c.useRef)(null),
                f = (0, c.useRef)(null),
                b = e.stepTimeout || 100,
                w = (0, c.useState)(F),
                S = w[0],
                x = w[1],
                y = (0, c.useCallback)(
                  (e) => {
                    (x(e),
                      f.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: f.current }));
                  },
                  [n],
                ),
                k = (0, s.z)(() => {
                  const u = f.current,
                    t = v.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && u && t)) return;
                  const a = Math.min(1, n / r);
                  return (
                    (u.style.height = `${C(t, a)}px`),
                    u.classList.add(d.Z.thumb),
                    g.current &&
                      (1 === a
                        ? g.current.classList.add(d.Z.base__nonActive)
                        : g.current.classList.remove(d.Z.base__nonActive)),
                    a
                  );
                }),
                T = (0, s.z)(() => {
                  const u = v.current,
                    t = f.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const i = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    o = (0, a.u)(0, 1, i / (r - n)),
                    l = (u.offsetHeight - C(u, s)) * o;
                  ((t.style.transform = `translateY(${0 | l}px)`),
                    ((e) => {
                      if (h.current && p.current && v.current && f.current) {
                        if (0 === e)
                          return (h.current.classList.add(A), void p.current.classList.remove(A));
                        if (
                          ((u = v.current),
                          (t = f.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (h.current.classList.remove(A), void p.current.classList.add(A));
                        var u, t;
                        (h.current.classList.remove(A), p.current.classList.remove(A));
                      }
                    })(l));
                }),
                L = (0, s.z)(() => {
                  B(e, () => {
                    (k(), T());
                  });
                });
              ((0, c.useEffect)(() => (0, i.v)(L)),
                (0, c.useEffect)(() => {
                  const u = () => {
                    B(e, () => {
                      T();
                    });
                  };
                  let t = _;
                  const n = () => {
                    (t(), (t = (0, i.v)(L)));
                  };
                  return (
                    e.events.on("recalculateContent", L),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", n),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", L),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, c.useEffect)(() => {
                  if (!S.pending) return;
                  const u = (u) => {
                      B(e, (t) => {
                        const r = v.current,
                          a = f.current,
                          i = e.getContainerSize();
                        if (!r || !a || !i) return;
                        const s = u.screenY - S.offset - r.getBoundingClientRect().y,
                          o = (s / r.offsetHeight) * i;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, o),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: a, thumbOffset: s, contentOffset: o }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        y(F));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, S.offset, S.pending, n, y]));
              const N = (0, o.B)((u) => e.applyStepTo(u), b, [e]),
                R = N[0],
                M = N[1];
              (0, c.useEffect)(
                () => (
                  document.addEventListener("mouseup", M, !0),
                  () => document.removeEventListener("mouseup", M, !0)
                ),
                [M],
              );
              const O = (e) => {
                e.target.classList.contains(A) || (0, l.G)("highlight");
              };
              return E().createElement(
                "div",
                { className: r()(d.Z.base, u.base), ref: g, onWheel: e.handleMouseWheel },
                E().createElement("div", {
                  className: r()(d.Z.topButton, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(A) ||
                      0 !== e.button ||
                      ((0, l.G)("play"), R(m.Nm.Next));
                  },
                  ref: h,
                  onMouseEnter: O,
                }),
                E().createElement(
                  "div",
                  {
                    className: r()(d.Z.track, u.track),
                    onMouseDown: (u) => {
                      const n = f.current;
                      if (n && 0 === u.button)
                        if (((0, l.G)("play"), u.target === n))
                          (e.handleIsThumbDragging(!0),
                            y({ pending: !0, offset: u.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            f.current &&
                              B(e, (n) => {
                                if (!n) return;
                                const r = t(e),
                                  a = e.clampPosition(n, n.scrollTop + r * u);
                                e.applyScroll(a);
                              });
                          })(u.screenY > n.getBoundingClientRect().y ? m.Nm.Prev : m.Nm.Next);
                        }
                    },
                    ref: v,
                    onMouseEnter: O,
                  },
                  E().createElement("div", { ref: f, className: u.thumb }),
                  E().createElement("div", { className: r()(d.Z.rail, u.rail) }),
                ),
                E().createElement("div", {
                  className: r()(d.Z.bottomButton, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(A) ||
                      0 !== e.button ||
                      ((0, l.G)("play"), R(m.Nm.Prev));
                  },
                  onMouseUp: M,
                  ref: p,
                  onMouseEnter: O,
                }),
              );
            },
          );
      },
      1158: (e, u, t) => {
        "use strict";
        t.d(u, { K: () => c });
        var n = t(6483),
          r = t.n(n),
          a = t(6179),
          i = t.n(a),
          s = t(6225),
          o = t(9605),
          l = t(5636);
        const c = ({
          children: e,
          api: u,
          className: t,
          barClassNames: n,
          areaClassName: c,
          scrollClassName: E,
          scrollClassNames: m,
          getStepByRailClick: d,
          onDrag: A,
        }) => {
          const _ = (0, a.useMemo)(() => {
              const e = n || {};
              return Object.assign({}, e, { base: r()(l.Z.base, e.base) });
            }, [n]),
            F = (0, a.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
          return i().createElement(
            "div",
            { className: r()(l.Z.defaultScroll, t), onWheel: u.handleMouseWheel },
            i().createElement(
              "div",
              { className: r()(l.Z.area, c) },
              i().createElement(o.Area, { className: E, classNames: m, api: F }, e),
            ),
            i().createElement(s.$Q, { getStepByRailClick: d, api: u, onDrag: A, classNames: _ }),
          );
        };
      },
      9605: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            Area: () => m,
            Bar: () => o.$Q,
            Default: () => l.K,
            useVerticalScrollApi: () => c.c4,
          }));
        var n = t(6483),
          r = t.n(n),
          a = t(1856),
          i = t(6179),
          s = t.n(i),
          o = t(6225),
          l = t(1158),
          c = t(7701),
          E = t(5636);
        const m = ({ className: e, classNames: u, children: t, api: n }) => (
          (0, i.useEffect)(() => (0, a.v)(n.recalculateContent)),
          s().createElement(
            "div",
            { className: r()(E.Z.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
            s().createElement(
              "div",
              { className: r()(E.Z.content, null == u ? void 0 : u.content), ref: n.contentRef },
              t,
            ),
          )
        );
        m.Default = l.K;
      },
      7701: (e, u, t) => {
        "use strict";
        t.d(u, { Nm: () => n.Nm, c4: () => r });
        var n = t(7308);
        const r = (0, n.EO)({
          getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
          getContainerSize: (e) => e.scrollHeight,
          getWrapperSize: (e) => e.offsetHeight,
          setScrollPosition: (e, u) => {
            e.scrollTop = u.value.scrollPosition;
          },
          getDirection: (e) => (e.deltaY > 1 ? n.Nm.Next : n.Nm.Prev),
        });
      },
      7308: (e, u, t) => {
        "use strict";
        t.d(u, { EO: () => A, Nm: () => m, he: () => d });
        var n = t(7515),
          r = t(1856),
          a = t(3138),
          i = t(4532),
          s = t(9653),
          o = t(3815),
          l = t(4489),
          c = t(6179),
          E = t(7030);
        let m;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(m || (m = {}));
        const d = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          A = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: m,
            getWrapperSize: A,
            triggerMouseMoveOnUpdate: _ = !1,
          }) => {
            const F = (e, t) => {
              const r = u(e),
                a = r[0],
                i = r[1];
              return (0, n.u)(a, i, t);
            };
            return (n = {}) => {
              const D = n.settings,
                B = void 0 === D ? d : D,
                C = (0, c.useRef)(null),
                g = (0, c.useRef)(null),
                h = (0, s.q)(),
                p = (0, l.f)(
                  () => {
                    a.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                v = (0, E.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = C.current;
                    u && (t(u, e), h.trigger("change", e), _ && p());
                  },
                  onRest: (e) => h.trigger("rest", e),
                  onStart: (e) => h.trigger("start", e),
                  onPause: (e) => h.trigger("pause", e),
                })),
                f = v[0],
                b = v[1],
                w = (0, c.useCallback)(
                  (e, u, t) => {
                    var n;
                    const r = f.scrollPosition.get(),
                      a = (null != (n = f.scrollPosition.goal) ? n : 0) - r;
                    return F(e, u * t + a + r);
                  },
                  [f.scrollPosition],
                ),
                S = (0, c.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = C.current;
                    n &&
                      b.start({
                        scrollPosition: F(n, e),
                        immediate: u,
                        reset: t,
                        config: B.animationConfig,
                        from: { scrollPosition: F(n, f.scrollPosition.get()) },
                      });
                  },
                  [b, B.animationConfig, f.scrollPosition],
                ),
                x = (0, c.useCallback)(
                  (e) => {
                    const u = C.current,
                      t = g.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return A(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, B.step),
                      r = w(u, e, n);
                    S(r);
                  },
                  [S, w, B.step],
                ),
                y = (0, c.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && x(m(e)),
                      C.current && h.trigger("mouseWheel", e, f.scrollPosition, u(C.current)));
                  },
                  [f.scrollPosition, x, h],
                ),
                k = (0, i.M)(
                  () =>
                    (0, r.v)(() => {
                      const e = C.current;
                      e &&
                        (S(F(e, f.scrollPosition.goal), { immediate: !0 }),
                        h.trigger("resizeHandled"));
                    }),
                  [S, f.scrollPosition.goal],
                ),
                T = (0, o.z)(() => {
                  const e = C.current;
                  if (!e) return;
                  const u = F(e, f.scrollPosition.goal);
                  (u !== f.scrollPosition.goal && S(u, { immediate: !0 }),
                    h.trigger("recalculateContent"));
                });
              (0, c.useEffect)(
                () => (
                  window.addEventListener("resize", k),
                  () => {
                    window.removeEventListener("resize", k);
                  }
                ),
                [k],
              );
              const L = (0, c.useCallback)((e) => h.trigger("isThumbDraggingChanged", e), [h]);
              return (0, c.useMemo)(
                () => ({
                  getWrapperSize: () => (g.current ? A(g.current) : void 0),
                  getContainerSize: () => (C.current ? e(C.current) : void 0),
                  getBounds: () =>
                    C.current
                      ? u(C.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: B.step.clampedArrowStepTimeout,
                  clampPosition: F,
                  handleMouseWheel: y,
                  applyScroll: S,
                  applyStepTo: x,
                  contentRef: C,
                  wrapperRef: g,
                  scrollPosition: b,
                  animationScroll: f,
                  recalculateContent: T,
                  handleIsThumbDragging: L,
                  events: { on: h.on, off: h.off },
                }),
                [f.scrollPosition, S, x, L, h.off, h.on, T, y, b, B.step.clampedArrowStepTimeout],
              );
            };
          };
      },
      794: (e, u, t) => {
        "use strict";
        t.d(u, { X: () => r });
        var n = t(7950);
        const r = { Vertical: t(9605), Horizontal: n };
      },
      7613: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => f });
        var n = t(6483),
          r = t.n(n),
          a = t(3779),
          i = t(280),
          s = t(3532),
          o = t.n(s),
          l = t(9887),
          c = t.n(l),
          E = t(3377),
          m = t(6179),
          d = t.n(m),
          A = t(3393);
        const _ = [
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
        const D = Object.keys(o()),
          B = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          C = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          g = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          h = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          p =
            (Object.keys(h),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": B,
              "heading-H36": B,
              "heading-H28": C,
              "heading-H24": C,
              "heading-H24R": C,
              "heading-H22": C,
              "heading-H20R": C,
              "heading-H18": C,
              "heading-H15": g,
              "heading-H14": g,
              "paragraph-P24": C,
              "paragraph-P18": C,
              "paragraph-P16": C,
              "paragraph-P14": g,
              "paragraph-P12": g,
              "paragraph-P10": g,
            }),
          v =
            (Object.keys(p),
            (e) =>
              e
                ? ((e) => D.includes(e))(e)
                  ? { colorClassName: A.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          f = (0, E.ZP)((e) => {
            let u = e.text,
              t = e.variant,
              n = e.className,
              s = e.color,
              o = e.m,
              l = e.mt,
              c = void 0 === l ? o : l,
              E = e.mr,
              D = void 0 === E ? o : E,
              B = e.mb,
              C = void 0 === B ? o : B,
              g = e.ml,
              h = void 0 === g ? o : g,
              f = e.style,
              b = e.format,
              w = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, _);
            const S = (0, m.useMemo)(() => {
                const e = v(s),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, f, n), colorClassName: u };
              }, [f, s]),
              x = S.computedStyle,
              y = S.colorClassName;
            return d().createElement(
              a.ZP,
              F(
                {
                  className: r()(A.Z.base, t && A.Z[t], y, n),
                  style: x,
                  mt: !0 === c ? p[t || "paragraph-P16"].mt : c,
                  mr: !0 === D ? p[t || "paragraph-P16"].mr : D,
                  mb: !0 === C ? p[t || "paragraph-P16"].mb : C,
                  ml: !0 === h ? p[t || "paragraph-P16"].ml : h,
                },
                w,
              ),
              void 0 !== b ? d().createElement(i.z, F({}, b, { text: u })) : u,
            );
          });
      },
      7078: (e, u, t) => {
        "use strict";
        t.d(u, { t: () => o });
        var n = t(6179),
          r = t.n(n),
          a = t(2056);
        const i = ["children"];
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
        const o = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, i);
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
          i = t(6373),
          s = t(2056);
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const n = r().createElement("div", { className: t }, e);
          if (u.header || u.body) return r().createElement(i.i, u, n);
          const l = u.contentId,
            c = u.args,
            E = null == c ? void 0 : c.contentId;
          return l || E
            ? r().createElement(s.u, o({}, u, { contentId: l || E }), n)
            : r().createElement(a.t, u, n);
        };
      },
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => l });
        var n = t(2056),
          r = t(6179),
          a = t.n(r);
        const i = ["children", "body", "header", "note", "alert", "args"];
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
        const o = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let u = e.children,
              t = e.body,
              l = e.header,
              c = e.note,
              E = e.alert,
              m = e.args,
              d = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, i);
            const A = (0, r.useMemo)(() => {
              const e = Object.assign({}, m, { body: t, header: l, note: c, alert: E });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [E, t, l, c, m]);
            return a().createElement(
              n.u,
              s(
                {
                  contentId:
                    ((_ = null == m ? void 0 : m.hasHtmlContent),
                    _ ? o.SimpleTooltipHtmlContent("resId") : o.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: A,
                },
                d,
              ),
              u,
            );
            var _;
          };
      },
      2056: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => l });
        var n = t(7902),
          r = t(4179),
          a = t(6179);
        const i = [
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
        const o = (e, u, t = {}, n = 0) => {
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
              E = e.onMouseDown,
              m = e.onClick,
              d = e.ignoreShowDelay,
              A = void 0 !== d && d,
              _ = e.ignoreMouseClick,
              F = void 0 !== _ && _,
              D = e.decoratorId,
              B = void 0 === D ? 0 : D,
              C = e.isEnabled,
              g = void 0 === C || C,
              h = e.targetId,
              p = void 0 === h ? 0 : h,
              v = e.onShow,
              f = e.onHide,
              b = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, i);
            const w = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, a.useMemo)(() => p || (0, n.F)().resId, [p]),
              x = (0, a.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (o(t, B, { isMouseEvent: !0, on: !0, arguments: s(r) }, S),
                  v && v(),
                  (w.current.isVisible = !0));
              }, [t, B, r, S, v]),
              y = (0, a.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    o(t, B, { on: !1 }, S),
                    w.current.isVisible && f && f(),
                    (w.current.isVisible = !1));
                }
              }, [t, B, S, f]),
              k = (0, a.useCallback)((e) => {
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
                document.addEventListener("wheel", k, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", k, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === g && y();
              }, [g, y]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", y),
                  () => {
                    (window.removeEventListener("mouseleave", y), y());
                  }
                ),
                [y],
              ));
            return g
              ? (0, a.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((T = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(x, A ? 100 : 400)),
                            l && l(e),
                            T && T(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (y(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === F && y(), null == m || m(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === F && y(), null == E || E(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    b,
                  ),
                )
              : u;
            var T;
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
      7515: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => n });
        const n = (e, u, t) => (t < e ? e : t > u ? u : t);
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
        const i = (e) => (0 === e ? window : window.subViews.get(e));
        function s({
          initializer: e = !0,
          rootId: u = 0,
          getRoot: t = i,
          context: a = "model",
        } = {}) {
          const s = new Map();
          function o(e, u = 0) {
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
              const i = "string" == typeof r ? `${a}.${r}` : a,
                o = n.O.view.addModelObserver(i, u, !0);
              return (s.set(o, t), e && t(l(r)), o);
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
                o(e.value, u);
              }
            },
            unsubscribe: o,
          };
        }
      },
      3215: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => o });
        var n = t(4598),
          r = t(9174),
          a = t(6179),
          i = t.n(a),
          s = t(8246);
        const o = () => (e, u) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: o = "real", options: l, children: c, mocks: E }) {
              const m = (0, a.useRef)([]),
                d = (t, a, i) => {
                  var o;
                  const l = s.U(a),
                    c =
                      "real" === t
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (o = null == i ? void 0 : i.getter) ? o : () => {},
                          }),
                    E = (e) =>
                      "mocks" === t ? (null == i ? void 0 : i.getter(e)) : c.readByPath(e),
                    d = (e) => m.current.push(e),
                    A = e({
                      mode: t,
                      readByPath: E,
                      externalModel: c,
                      observableModel: {
                        array: (e, u) => {
                          const a = null != u ? u : E(e),
                            i = r.LO.box(a, { equals: n.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, r.aD)((e) => i.set(e)),
                                e,
                              ),
                            i
                          );
                        },
                        object: (e, u) => {
                          const a = null != u ? u : E(e),
                            i = r.LO.box(a, { equals: n.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, r.aD)((e) => i.set(e)),
                                e,
                              ),
                            i
                          );
                        },
                        primitives: (e, u) => {
                          const n = E(u);
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
                              i = Object.entries(a),
                              s = i.reduce((e, [u, t]) => ((e[t] = r.LO.box(n[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, r.aD)((e) => {
                                    i.forEach(([u, t]) => {
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
                    _ = { mode: t, model: A, externalModel: c, cleanup: d };
                  return {
                    model: A,
                    controls: "mocks" === t && i ? i.controls(_) : u(_),
                    externalModel: c,
                    mode: t,
                  };
                },
                A = (0, a.useRef)(!1),
                _ = (0, a.useState)(o),
                F = _[0],
                D = _[1],
                B = (0, a.useState)(() => d(o, l, E)),
                C = B[0],
                g = B[1];
              return (
                (0, a.useEffect)(() => {
                  A.current ? g(d(F, l, E)) : (A.current = !0);
                }, [E, F, l]),
                (0, a.useEffect)(() => {
                  D(o);
                }, [o]),
                (0, a.useEffect)(
                  () => () => {
                    (C.externalModel.dispose(), m.current.forEach((e) => e()));
                  },
                  [C],
                ),
                i().createElement(t.Provider, { value: C }, c)
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
          i = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
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
                    s = i[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, o),
                    n(),
                    () => {
                      r &&
                        (s(), window.removeEventListener(a, o), (e.listeners -= 1), n(), (r = !1));
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
            graphicsQuality: () => i,
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
        const i = {
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
            extraSize: () => S,
            forceTriggerMouseMove: () => f,
            freezeTextureBeforeResize: () => _,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => b,
            getScale: () => F,
            getSize: () => m,
            getViewGlobalPosition: () => A,
            isClientAccessible: () => h,
            isEventHandled: () => v,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => d,
            sendEvent: () => i.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => p,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => x,
          }));
        var n = t(3722),
          r = t(6112),
          a = t(6538),
          i = t(8566);
        function s(e) {
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
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function d(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function A(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: B(u.x), y: B(u.y) };
        }
        function _() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function B(e) {
          return viewEnv.remToPx(e);
        }
        function C(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function g() {
          return viewEnv.isFocused();
        }
        function h() {
          return viewEnv.isClientAccessible();
        }
        function p() {
          return viewEnv.setEventHandled();
        }
        function v() {
          return viewEnv.isEventHandled();
        }
        function f() {
          viewEnv.forceTriggerMouseMove();
        }
        function b() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(r.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === r.W[u]), e),
            {},
          ),
          S = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          x = Promise.all([
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
          i = 32,
          s = 64,
          o = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                i = (function (e, u) {
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
                    Object.assign({ __Type: t, type: e }, i, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, i));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          l = {
            close(e) {
              o("popover" === e ? r : i);
            },
            minimize() {
              o(s);
            },
            move(e) {
              o(a, { isMouseEvent: !0, on: e });
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
        const i = ["xl", "lg", "md", "sm", "xs"],
          s = (e) => e.includes("_") && ((e) => i.includes(e))(e.split("_").at(-1)),
          o = [n.cJ.ExtraLarge, n.cJ.Large, n.cJ.Medium, n.cJ.Small, n.cJ.ExtraSmall],
          l = (e, u) =>
            Object.keys(e).reduce((t, n) => {
              if (n in t) return t;
              if (s(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const a = o.indexOf(u),
                  s = (-1 !== a ? i.slice(a) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  l = s ? e[s] : void 0;
                return ((t[r] = void 0 !== l ? l : e[r]), t);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, u) => i.some((t) => void 0 !== u[`${e}_${t}`]))(n, e) ||
                  (t[n] = r),
                t
              );
            }, {}),
          c = (e, u = l) => {
            const t = (
              (e, u = l) =>
              (t) => {
                const i = (0, n.GS)().mediaSize,
                  s = (0, r.useMemo)(() => u(t, i), [t, i]);
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
      4532: (e, u, t) => {
        "use strict";
        t.d(u, { M: () => r });
        var n = t(6179);
        const r = (e, u = []) => {
          const t = (0, n.useRef)(),
            r = (0, n.useCallback)((...u) => {
              (t.current && t.current(), (t.current = e(...u)));
            }, u);
          return (
            (0, n.useEffect)(
              () => () => {
                t.current && t.current();
              },
              [r],
            ),
            r
          );
        };
      },
      9653: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => i });
        var n = t(6179);
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
        const i = () => {
          const e = (0, n.useMemo)(() => ({}), []),
            u = (u) => (e[u] || (e[u] = new Map()), e[u]),
            t = (e, t) => {
              u(e).set(t, t);
            },
            a = (e, t) => {
              u(e).delete(t);
            },
            i = (e, ...t) => {
              for (var n, a = r(u(e).values()); !(n = a()).done;) {
                (0, n.value)(...t);
              }
            };
          return (0, n.useMemo)(() => ({ on: t, off: a, trigger: i }), []);
        };
      },
      3815: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => a });
        var n = t(6179);
        const r = [];
        function a(e) {
          const u = (0, n.useRef)(e);
          return (
            (0, n.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, n.useCallback)((...e) => (0, u.current)(...e), r)
          );
        }
      },
      5415: (e, u, t) => {
        "use strict";
        t.d(u, { GS: () => l, cJ: () => i });
        var n = t(6179),
          r = t(7739),
          a = t(1043);
        let i, s, o;
        (!(function (e) {
          ((e[(e.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = a.j.small.width)] = "Small"),
            (e[(e.Medium = a.j.medium.width)] = "Medium"),
            (e[(e.Large = a.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
        })(i || (i = {})),
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
          })(o || (o = {})));
        const l = () => {
          const e = (0, n.useContext)(r.YN),
            u = e.width,
            t = e.height,
            a = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return i.ExtraLarge;
                case e.large:
                  return i.Large;
                case e.medium:
                  return i.Medium;
                case e.small:
                  return i.Small;
                case e.extraSmall:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
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
            mediaSize: a,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: u,
            remScreenHeight: t,
          };
        };
      },
      560: (e, u, t) => {
        "use strict";
        t.d(u, { B: () => r });
        var n = t(6179);
        function r(e, u, t = []) {
          const r = (0, n.useRef)(0),
            a = (0, n.useCallback)(() => window.clearInterval(r.current), t || []);
          (0, n.useEffect)(() => a, [a]);
          const i = (null != t ? t : []).concat([u]);
          return [
            (0, n.useCallback)((t) => {
              ((r.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, i),
            a,
          ];
        }
      },
      4419: (e, u, t) => {
        "use strict";
        t.d(u, { y: () => a });
        var n = t(8045),
          r = t(6179);
        const a = (e, u, t = !0) => {
          const a = (0, r.useCallback)(
            (e) => {
              const t = e[0];
              u && u(t);
            },
            [u],
          );
          (0, r.useEffect)(() => {
            if (!e.current || !t) return;
            const u = new n.Z((e) => a(e));
            return (
              u.observe(e.current),
              () => {
                u.disconnect();
              }
            );
          }, [a, t, e]);
        };
      },
      4489: (e, u, t) => {
        "use strict";
        t.d(u, { f: () => a });
        var n = t(5139),
          r = t(6179);
        function a(e, u, t) {
          const a = (0, r.useMemo)(() => (0, n.Z)(t, e), u);
          return ((0, r.useEffect)(() => a.cancel, [a]), a);
        }
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
      9480: (e, u, t) => {
        "use strict";
        t.d(u, { UI: () => n });
        function n(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, n) => u(null == e ? void 0 : e.value, t, n));
        }
      },
      1612: (e, u, t) => {
        "use strict";
        t.d(u, { h: () => r });
        var n = t(9174);
        function r(e) {
          const u = {};
          for (const t in e)
            if (Object.prototype.hasOwnProperty.call(e, t)) {
              const r = e[t];
              u[t] = (0, n.aD)(r);
            }
          return u;
        }
      },
      9690: (e, u, t) => {
        "use strict";
        t.d(u, { HG: () => i });
        const n = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          r = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const a = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          i = (e) =>
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
        t.d(u, { G: () => n });
      },
      3649: (e, u, t) => {
        "use strict";
        let n;
        function r(e, u) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const t = 0 === e.indexOf("%") ? 2 : 1;
            return String(u[e.slice(t, -t)]);
          });
        }
        function a(e) {
          return e.replace(/-/g, "_");
        }
        (t.d(u, { BN: () => a, Eg: () => s, Uw: () => A, uF: () => r, v2: () => n, z4: () => i }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(n || (n = {})));
        const i = (e) => e.replace(/&nbsp;/g, " "),
          s = (e) => e.replace(/&zwnbsp;/g, "\ufeff"),
          o = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          l = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          c = (e, u, t = n.left) => e.split(u).reduce(t === n.left ? o : l, []),
          E = (() => {
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
          m = ["zh_cn", "zh_sg", "zh_tw"],
          d = (e, u = n.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return m.includes(t)
              ? E(e)
              : ((e, u = n.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = i(e);
                  return (c(a, /( )/, u).forEach((e) => (t = t.concat(c(e, r, n.left)))), t);
                })(e, u);
          },
          A = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : d(e, u)));
      },
      5139: (e, u, t) => {
        "use strict";
        function n(e, u, t, n) {
          let r,
            a = !1,
            i = 0;
          function s() {
            r && clearTimeout(r);
          }
          function o(...o) {
            const l = this,
              c = Date.now() - i;
            function E() {
              ((i = Date.now()), t.apply(l, o));
            }
            a ||
              (n && !r && E(),
              s(),
              void 0 === n && c > e
                ? E()
                : !0 !== u &&
                  (r = setTimeout(
                    n
                      ? function () {
                          r = void 0;
                        }
                      : E,
                    void 0 === n ? e - c : e,
                  )));
          }
          return (
            "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
            (o.cancel = function () {
              (s(), (a = !0));
            }),
            o
          );
        }
        t.d(u, { Z: () => n });
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
        t.d(u, { B0: () => o, ry: () => B });
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
        const i = {
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
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var d = t(5521),
          A = t(3138);
        const _ = ["args"];
        function F(e, u, t, n, r, a, i) {
          try {
            var s = e[a](i),
              o = s.value;
          } catch (e) {
            return void t(e);
          }
          s.done ? u(o) : Promise.resolve(o).then(n, r);
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
                  return new Promise(function (n, r) {
                    var a = e.apply(u, t);
                    function i(e) {
                      F(a, n, r, i, s, "next", e);
                    }
                    function s(e) {
                      F(a, n, r, i, s, "throw", e);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          C = (e, u) => {
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
                })(u, _);
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
          g = () => C(o.CLOSE),
          h = (e, u) => {
            e.keyCode === d.n.ESCAPE && u();
          };
        var p = t(7572);
        const v = r.instance,
          f = {
            DataTracker: a.Z,
            ViewModel: p.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: m,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => C(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: g,
            sendClosePopOverEvent: () => C(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              C(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, r = R.invalid("resId"), a) => {
              const i = A.O.view.getViewGlobalPosition(),
                s = t.getBoundingClientRect(),
                l = s.x,
                c = s.y,
                E = s.width,
                m = s.height,
                d = {
                  x: A.O.view.pxToRem(l) + i.x,
                  y: A.O.view.pxToRem(c) + i.y,
                  width: A.O.view.pxToRem(E),
                  height: A.O.view.pxToRem(m),
                };
              C(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: D(d),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => h(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              h(e, g);
            },
            handleViewEvent: C,
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
            ClickOutsideManager: v,
            SystemLocale: i,
            UserLocale: s,
          };
        window.ViewEnvHelper = f;
      },
      3618: (e, u, t) => {
        "use strict";
        t.d(u, { w: () => d });
        var n = t(6483),
          r = t.n(n),
          a = t(3415),
          i = t(4419),
          s = t(6179),
          o = t.n(s),
          l = t(6143),
          c = t(3310),
          E = t(131),
          m = t(9053);
        const d = o().memo(
          ({
            text: e,
            classMix: u,
            onSizeChanged: t,
            binding: n,
            isTooltipEnable: d = !1,
            isTruncationAvailable: A = !1,
            targetId: _,
            justifyContent: F = m.v2.FlexStart,
            alignContent: D = m.v2.FlexStart,
            truncateIdentify: B = m.YA,
          }) => {
            const C = (0, s.useRef)(null),
              g = (0, s.useRef)({ height: 0, width: 0 }),
              h = (0, s.useState)({ elementList: [], isTruncated: !1, isTruncateFinished: !1 }),
              p = h[0],
              v = h[1],
              f = (0, s.useMemo)(() => (0, c.s)(e, n), [n, e]),
              b = (0, s.useMemo)(() => {
                if (d && p.isTruncated)
                  return {
                    args: { text: e, stringifyKwargs: n ? JSON.stringify(n) : "" },
                    contentId: R.views.lobby.common.tooltips.ExtendedTextTooltip("resId"),
                    targetId: _,
                  };
              }, [n, d, _, e, p.isTruncated]),
              w = (0, s.useCallback)(
                (e) => {
                  ((g.current.width = e.contentRect.width),
                    (g.current.height = e.contentRect.height));
                  const u = (0, E.T)(C, f, g.current, B),
                    n = u[0],
                    r = u[1];
                  (v({ elementList: n, isTruncated: r, isTruncateFinished: !0 }), t && t(r));
                },
                [t, B, f],
              ),
              S = (0, s.useMemo)(() => ({ justifyContent: F, alignContent: D }), [D, F]);
            return (
              (0, i.y)(C, w, A),
              o().createElement(
                "div",
                {
                  className: r()(
                    l.Z.base,
                    u,
                    l.Z.base__zeroPadding,
                    A && l.Z.base__isTruncationAvailable,
                  ),
                  style: S,
                },
                o().createElement("div", { className: l.Z.unTruncated, ref: C }, f),
                o().createElement(
                  a.l,
                  { tooltipArgs: b },
                  o().createElement(
                    "div",
                    {
                      className: r()(
                        l.Z.truncated,
                        !p.isTruncateFinished && A && l.Z.truncated__hide,
                      ),
                      style: S,
                    },
                    p.isTruncateFinished && A ? p.elementList : f,
                  ),
                ),
              )
            );
          },
        );
      },
      3310: (e, u, t) => {
        "use strict";
        t.d(u, { s: () => E });
        var n = t(3649),
          r = t(6799),
          a = t(6960),
          i = t(9053);
        const s = (e) => {
            const u = /[\s\u002d]/g;
            let t = u.exec(e);
            if (!t) return [e];
            const n = [];
            let r = 0;
            for (; t;) (n.push(e.slice(r, u.lastIndex)), (r = u.lastIndex), (t = u.exec(e)));
            return (r !== e.length && n.push(e.slice(r)), n);
          },
          o = (e, u = "") => {
            const t = [];
            return (
              (0, a.Z)(
                e,
                /(\n+|[\xa0\ufeff]+)/g,
                (e) => {
                  t.push({ blockType: i.kH.Word, colorTag: u, childList: s(e) });
                },
                (e) => {
                  const n = e[0],
                    r = i.aF[n.charAt(0)];
                  r === i.kH.LineBreak
                    ? t.push(
                        ...((e) => {
                          const u = [
                            { blockType: i.kH.LineBreak, colorTag: "", childList: [e.charAt(0)] },
                          ];
                          for (let t = 0; t < e.length - 1; t++)
                            u.push({
                              blockType: i.kH.NewLine,
                              colorTag: "",
                              childList: [e.charAt(0)],
                            });
                          return u;
                        })(n),
                      )
                    : t.push({ blockType: r, colorTag: u, childList: [n] });
                },
              ),
              t
            );
          },
          l = (e, u, t = "") => {
            const n = [];
            return (
              (0, a.Z)(
                e,
                /(?:%\(|{)(.*?)[)}][sd]?/g,
                (e) => {
                  n.push(...o(e, t));
                },
                (e) => {
                  const r = e[1],
                    a = void 0 === u[r] ? e[0] : u[r];
                  "string" == typeof a || "number" == typeof a
                    ? n.push(...o(String(a), t))
                    : n.push({ blockType: i.kH.Binding, colorTag: t, childList: [a] });
                },
              ),
              n
            );
          },
          c = (e, u) => {
            if (!e) return [u];
            const t = [],
              n = Object.assign({}, u, { childList: u.childList.splice(0, 1) });
            if (e.blockType === i.kH.NoBreakWrapper) (e.childList.push(n), t.push(e));
            else {
              const u = Object.assign({}, e, { childList: e.childList.splice(-1) });
              (e.childList.length > 0 && t.push(e),
                t.push({ blockType: i.kH.NoBreakWrapper, colorTag: "", childList: [u, n] }));
            }
            return (u.childList.length > 0 && t.push(u), t);
          },
          E = (e, u = {}) => {
            if (!e) return [];
            const t = ((e) => {
              const u = [];
              let t = !1;
              return (
                e.forEach((e) => {
                  e.blockType === i.kH.NoBreakSymbol
                    ? ((t = !0), u.push(...c(u.pop(), e)))
                    : (t ? u.push(...c(u.pop(), e)) : u.push(e), (t = !1));
                }),
                u
              );
            })(
              ((e, u) => {
                const t = [];
                return (
                  (0, a.Z)(
                    e,
                    /(?:%\(|{)(\w*)(?:_[Oo]pen|_Start)(?:\)s|})([\s\S]*?)(?:%\(|{)\w*(?:_[Cc]lose|_End)(?:\)s|})/g,
                    (e) => {
                      t.push(...l(e, u));
                    },
                    (e) => {
                      t.push(...l(e[2], u, e[1]));
                    },
                  ),
                  t
                );
              })((0, n.Eg)((0, n.z4)(e)), u),
            );
            return (0, r.w)(t);
          };
      },
      6799: (e, u, t) => {
        "use strict";
        t.d(u, { w: () => i });
        var n = t(597),
          r = t(9053);
        const a = (e, u, t) => {
            const i = [];
            return (
              e.childList.forEach((s, o) => {
                const l = `${t}_${o}`;
                if ((0, r.dz)(s)) {
                  const e = s,
                    u = e.blockType,
                    t = n.IY[u],
                    r = a(e, t, l);
                  i.push(...r);
                } else i.push(u({ elementList: [s], textBlock: e, key: l }));
              }),
              i
            );
          },
          i = (e) => {
            const u = [];
            return (
              e.forEach((e, t) => {
                u.push(
                  ...((e, u) => {
                    const t = [],
                      i = e.blockType,
                      s = n.IY[i],
                      o = a(e, s, u);
                    return (
                      i === r.kH.NoBreakWrapper
                        ? t.push(s({ elementList: o, textBlock: e, key: `${u}` }))
                        : t.push(...o),
                      t
                    );
                  })(e, t),
                );
              }),
              u
            );
          };
      },
      6960: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = (e, u, t, n) => {
          let r = u.exec(e),
            a = 0;
          for (; r;)
            (a !== r.index && t(e.slice(a, r.index)), n(r), (a = u.lastIndex), (r = u.exec(e)));
          a !== e.length && t(e.slice(a));
        };
      },
      131: (e, u, t) => {
        "use strict";
        t.d(u, { T: () => c });
        var n = t(6179),
          r = t.n(n),
          a = t(9053);
        const i = (e, u) => !e || e.offsetTop + e.offsetHeight > u,
          s = (e, u) => e.offsetLeft + e.offsetWidth - u,
          o = (e, u, t) => {
            if (!e || !e.textContent) return [!1, 0];
            if (e.offsetLeft > u) return [!1, 0];
            const n = s(e, u),
              r = e.textContent.length,
              a = e.offsetWidth / r,
              i = Math.ceil(n / a);
            if (n > 0) {
              const n = Math.floor((u - e.offsetLeft) / a);
              return n >= t ? [!0, t + i] : [!1, n];
            }
            const o = Math.max(t + i, 0);
            return r < o ? [!1, 0] : [!0, o];
          },
          l = (e, u, t, n, i, s) => {
            let c = -1,
              E = null;
            for (let m = t; m >= 0; m--) {
              const t = e[m],
                d = Number(e[m].getAttribute(a.bF));
              if (d === a.kH.LineBreak || d === a.kH.NewLine || d === a.kH.Binding) continue;
              const A = t.textContent || "";
              if (!(t.childElementCount > 1)) {
                const e = o(t, n, i),
                  a = e[0],
                  l = e[1];
                if (!a) {
                  l > 0 && (i -= l);
                  continue;
                }
                const d = A.slice(0, A.length - l) + s,
                  _ = u[m];
                ((E = r().cloneElement(_, _.props, d)), (c = m));
                break;
              }
              {
                const e = t.children,
                  a = u[m],
                  o = a.props.children,
                  d = l(e, o, e.length - 1, n, i, s),
                  _ = d[0],
                  F = d[1];
                if (!(_ < 0)) {
                  const e = o.slice(0, _);
                  ((E = r().cloneElement(a, a.props, e, F)), (c = m));
                  break;
                }
                i -= A.length;
              }
            }
            return [c, E];
          },
          c = (e, u, t, n = a.YA) => {
            const r = [...u],
              o = e.current;
            if (!o) return [r, !1];
            const c = t.height,
              E = t.width,
              m = o.lastElementChild;
            if (!i(m, c) && s(m, E) <= 0) return [r, !1];
            const d = o.children,
              A = ((e, u) => {
                let t = 0,
                  n = e.length - 1;
                for (; n - t >= 0;) {
                  const r = t + Math.ceil(0.5 * (n - t));
                  i(e[r], u) ? (n = r - 1) : (t = r + 1);
                }
                return t - 1;
              })(d, c);
            if (A < 0) return [r, !1];
            const _ = l(d, r, A, E, n.length, n),
              F = _[0],
              D = _[1];
            return (D && (r.splice(F, 1, D), r.splice(F + 1)), [r, !0]);
          };
      },
      9053: (e, u, t) => {
        "use strict";
        let n, r, a;
        (t.d(u, { YA: () => s, aF: () => l, bF: () => o, dz: () => i, kH: () => n, v2: () => r }),
          (function (e) {
            ((e[(e.Word = 0)] = "Word"),
              (e[(e.LineBreak = 1)] = "LineBreak"),
              (e[(e.NewLine = 2)] = "NewLine"),
              (e[(e.NoBreakSymbol = 3)] = "NoBreakSymbol"),
              (e[(e.NoBreakWrapper = 4)] = "NoBreakWrapper"),
              (e[(e.Binding = 5)] = "Binding"));
          })(n || (n = {})),
          (function (e) {
            ((e.FlexStart = "flex-start"), (e.Center = "center"), (e.FlexEnd = "flex-end"));
          })(r || (r = {})),
          (function (e) {
            ((e.NBSP = " "), (e.ZWNBSP = "\ufeff"), (e.NEW_LINE = "\n"));
          })(a || (a = {})));
        const i = (e) => void 0 !== e.childList,
          s = "...",
          o = "data-block-type",
          l = { [a.NBSP]: n.NoBreakSymbol, [a.ZWNBSP]: n.NoBreakSymbol, [a.NEW_LINE]: n.LineBreak };
      },
      597: (e, u, t) => {
        "use strict";
        t.d(u, { IY: () => c });
        var n = t(6179),
          r = t.n(n),
          a = t(9053),
          i = t(9627),
          s = t(7629);
        const o = (e) => ({ color: `#${e}` }),
          l = ({ elementList: e, textBlock: u, key: t }) => {
            const n = u.colorTag;
            return n
              ? i.Z[n]
                ? r().createElement(
                    "span",
                    { key: t, "data-block-type": u.blockType, className: i.Z[n] },
                    e,
                  )
                : r().createElement(
                    "span",
                    { key: t, "data-block-type": u.blockType, style: o(n) },
                    e,
                  )
              : r().createElement("span", { key: t, "data-block-type": u.blockType }, e);
          },
          c = {
            [a.kH.Word]: l,
            [a.kH.NoBreakSymbol]: l,
            [a.kH.Binding]: ({ elementList: e, textBlock: u, key: t }) =>
              r().createElement(
                "span",
                { key: t, "data-block-type": u.blockType },
                e.map((e) => r().createElement(r().Fragment, { key: t }, e)),
              ),
            [a.kH.LineBreak]: ({ key: e }) =>
              r().createElement("span", {
                key: e,
                "data-block-type": a.kH.LineBreak,
                className: s.Z.lineBreak,
              }),
            [a.kH.NewLine]: ({ elementList: e, key: u }) =>
              r().createElement(
                "span",
                { key: u, "data-block-type": a.kH.NewLine, className: s.Z.newLine },
                e,
              ),
            [a.kH.NoBreakWrapper]: ({ elementList: e, key: u }) =>
              r().createElement(
                "span",
                { key: u, "data-block-type": a.kH.NoBreakWrapper, className: s.Z.noBreakWrapper },
                e,
              ),
          };
      },
      3458: (e, u, t) => {
        "use strict";
        let n;
        (t.d(u, { Z0: () => r, in: () => n, sx: () => a }),
          (function (e) {
            ((e[(e.NonSet = 0)] = "NonSet"),
              (e[(e.Debug = 10)] = "Debug"),
              (e[(e.Info = 20)] = "Info"),
              (e[(e.Warning = 30)] = "Warning"));
          })(n || (n = {})));
        const r = "tooltip_watched",
          a = 2;
        let i;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(i || (i = {}));
      },
      4828: (e, u, t) => {
        "use strict";
        t.d(u, { D9: () => n, eX: () => r, sC: () => a, sk: () => s });
        const n = "crew";
        let r, a, i, s, o, l, c;
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
          })(a || (a = {})),
          (function (e) {
            e.DocumentChange = "document_change_dialog";
          })(i || (i = {})),
          (function (e) {
            ((e.PremiumTooltip = "personal_file_view_premium_tooltip"),
              (e.MstlTooltip = "personal_file_view_mstl_tooltip"));
          })(s || (s = {})),
          (function (e) {
            ((e.ChangeButtonTooltip = "crew_widget_change_button_tooltip"),
              (e.MstlTooltip = "crew_widget_mstl_tooltip"),
              (e.SlotContextMenu = "crew_widget_slot_context_menu"),
              (e.CrewOperationsButton = "crew_widget_crew_operations_button"));
          })(o || (o = {})),
          (function (e) {
            ((e.FirstnameSelect = "document_change_dialog_firstname_select"),
              (e.Firstname = "document_change_dialog_firstname"),
              (e.LastnameSelect = "document_change_dialog_lastname_select"),
              (e.Lastname = "document_change_dialog_lastname"));
          })(l || (l = {})),
          (function (e) {
            e.CardContextMenu = "barracks_view_card_context_menu";
          })(c || (c = {})));
        (R.views.lobby.crew.personal_case.PersonalFileView("resId"),
          a.PersonalFile,
          R.views.lobby.crew.personal_case.PersonalDataView("resId"),
          a.PersonalData,
          R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
          a.ServiceRecord,
          R.views.lobby.crew.BarracksView("resId"),
          a.Barracks,
          R.views.lobby.crew.HangarCrewWidget("resId"),
          a.Hangar,
          R.views.lobby.crew.MemberChangeView("resId"),
          a.MemberChange,
          R.views.lobby.crew.TankChangeView("resId"),
          a.TankChange,
          R.views.lobby.crew.QuickTrainingView("resId"),
          a.QuickTraining);
      },
      1943: (e, u, t) => {
        "use strict";
        t.d(u, { Sr: () => m });
        var n = t(6179),
          r = t(3458);
        const a = ["action", "timeLimit"];
        const i = "metrics",
          s = () => Date.now(),
          o = ({ partnerID: e, item: u, parentScreen: t, itemState: n, info: r }) => ({
            item: u,
            partnerID: e || null,
            parent_screen: t || null,
            item_state: n || null,
            additional_info: r || null,
          }),
          l = (e, u) => {
            const t = (0, n.useCallback)(
              (t, n = r.in.Info, a) => {
                (a || (a = {}),
                  Object.keys(a).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: u,
                      action: t,
                      logLevel: n,
                      params: JSON.stringify(a),
                    }));
              },
              [e, u],
            );
            return (e, u, n) => t(e, u, n);
          },
          c = (e, u) => {
            const t = l(e, u),
              r = (0, n.useRef)(new Map()),
              a = (0, n.useRef)(new Map()),
              i = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const u = r.current.get(e);
                  (void 0 !== u && u > 0) || r.current.set(e, s());
                },
                [r],
              ),
              o = (0, n.useCallback)(() => {
                (r.current.clear(), a.current.clear());
              }, [r, a]),
              c = (0, n.useCallback)(
                (e) => {
                  e &&
                    void 0 !== r.current.get(e) &&
                    void 0 === a.current.get(e) &&
                    a.current.set(e, s());
                },
                [r, a],
              ),
              E = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const u = r.current.get(e);
                  if (void 0 === u) return;
                  const t = a.current.get(e);
                  if (void 0 === t) return;
                  a.current.delete(e);
                  const n = s() - t;
                  r.current.set(e, u + n);
                },
                [r, a],
              ),
              m = (0, n.useCallback)(
                (e, u = 0, n, i) => {
                  const o = r.current.get(e);
                  if (void 0 === o) return;
                  (void 0 !== a.current.get(e) && E(e), r.current.delete(e));
                  const l = (s() - o) / 1e3;
                  l <= u ||
                    ((i = ((e, u) => (void 0 === e && (e = {}), (e.timeSpent = u), e))(i, l)),
                    t(e, n, i));
                },
                [r, a, t, E],
              );
            return [
              (e) => i(e),
              (e, u, t, n) => m(e, u, t, n),
              () => o(),
              (e) => c(e),
              (e) => E(e),
            ];
          },
          E = (e) => {
            const u = c(e, i),
              t = u[0],
              r = u[1],
              a = u[2],
              s = u[3],
              l = u[4],
              E = (0, n.useCallback)(
                (e) => {
                  const u = e.action,
                    t = e.timeLimit,
                    n = e.logLevel;
                  r(u, t, n, o(e));
                },
                [r],
              );
            return [(e) => t(e), (e) => E(e), () => a(), (e) => s(e), (e) => l(e)];
          },
          m = (e, u) => {
            const t = E(e),
              i = t[0],
              s = t[1],
              o = u.action,
              l = u.timeLimit,
              c = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(u, a);
            return (0, n.useMemo)(
              () => ({
                onShow: () => i(o || r.Z0),
                onHide: () => s(Object.assign({ action: o || r.Z0, timeLimit: l || r.sx }, c)),
              }),
              [o, l, c, i, s],
            );
          };
      },
      7077: (e, u, t) => {
        "use strict";
        t.d(u, { G: () => E, U: () => l });
        var n = t(6483),
          r = t.n(n),
          a = t(3649),
          i = t(6179),
          s = t.n(i),
          o = t(3938);
        let l;
        !(function (e) {
          ((e.c158x118 = "big"),
            (e.c100x60 = "small"),
            (e.c100x60Barracks = "barracks"),
            (e.c444x300 = "special"),
            (e.c204x256 = "c_204x256"));
        })(l || (l = {}));
        const c = R.images.gui.maps.icons.tankmen.icons,
          E = (0, i.memo)(({ name: e, size: u = l.c100x60, className: t, isSkin: n = !1 }) => {
            const i = (n ? c.$dyn(u).$dyn("crewSkins") : c.$dyn(u)).$dyn((0, a.BN)(e)),
              E = u === l.c204x256;
            return s().createElement(
              "div",
              {
                style: { backgroundImage: `url(${i})` },
                className: r()(o.Z.base, o.Z[`base__${u}`], t),
              },
              E && s().createElement("div", { className: o.Z.innerShadow }),
            );
          });
      },
      8018: (e, u, t) => {
        "use strict";
        t.d(u, { Gc: () => o, T3: () => a });
        var n = t(3649);
        const r = R.strings.common.percentValue(),
          a = (e) => (0, n.uF)(r, { value: e });
        let i;
        !(function (e) {
          ((e.Objective = "objective"), (e.Possessive = "possessive"));
        })(i || (i = {}));
        (R.strings.crew.filterPanel.counter.reset.header(),
          R.strings.crew.filterPanel.counter.reset.body(),
          R.strings.crew.filterPanel.counterMultySelect.reset.header(),
          R.strings.crew.filterPanel.counterMultySelect.reset.body());
        let s;
        !(function (e) {
          ((e.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (e.SHOP_INFO = "shop_info"),
            (e.RUDY = "rudy"));
        })(s || (s = {}));
        const o = (e, u = !1, t = null) => {
          const n = u
            ? R.strings.item_types.tankman.roles.female
            : R.strings.item_types.tankman.roles;
          return (t ? n.$dyn(`${t}Case`) : n).$dyn(e);
        };
      },
      894: (e, u, t) => {
        "use strict";
        var n = t(6179),
          r = t.n(n),
          a = t(3403),
          i = t(4022),
          s = t(3215),
          o = t(4598),
          l = t(9480),
          c = t(1612),
          E = t(9174),
          m = t(3946);
        const d = (0, s.q)()(
            ({ observableModel: e }) => {
              const u = Object.assign(
                  {},
                  e.primitives([
                    "rankName",
                    "rankIcon",
                    "battlesCount",
                    "averageXP",
                    "isTankmanInVehicle",
                  ]),
                  { achievementsList: e.array("achievementsList"), isTTCVisible: E.LO.box(!1) },
                ),
                t = (0, m.Om)(() => l.UI(u.achievementsList.get(), o.yR)),
                n = (0, m.Om)(() => u.isTankmanInVehicle.get() && u.isTTCVisible.get(), !0),
                r = (0, m.Om)(() => u.achievementsList.get().length > 0);
              return Object.assign({}, u, {
                computes: { getAchievementsList: t, isTTCVisible: n, hasAchievements: r },
              });
            },
            ({ model: e }) =>
              Object.assign({}, (0, c.h)({ setTTCVisible: (u) => e.isTTCVisible.set(u) })),
          ),
          A = d[0],
          _ = d[1];
        var F = t(6483),
          D = t.n(F),
          B = t(5415),
          C = t(3961);
        const g = "AchievementsList_base_90",
          h = "AchievementsList_title_f4",
          p = "AchievementsList_container_a7",
          v = "AchievementsList_item_10",
          f = "AchievementsList_bar_4a";
        var b = t(7078),
          w = t(2603);
        const S = {
          base: "AchievementItem_base_45",
          base__small: "AchievementItem_base__small_b4",
          icon: "AchievementItem_icon_91",
          amountBG: "AchievementItem_amountBG_46",
          amount: "AchievementItem_amount_65",
        };
        let x;
        !(function (e) {
          ((e.Small = "small"), (e.Big = "big"));
        })(x || (x = {}));
        const y = ({ name: e, amount: u, block: t, isRare: n, size: a, className: i }) => {
          const s =
            a === x.Small
              ? R.images.gui.maps.icons.achievement
              : R.images.gui.maps.icons.achievement.big;
          return r().createElement(
            b.t,
            {
              args: { tooltipId: w.Th, name: e, block: t, isRare: n },
              targetId: R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
            },
            r().createElement(
              "div",
              { className: D()(S.base, S[`base__${a}`], i) },
              r().createElement("div", {
                className: S.icon,
                style: { backgroundImage: `url(${s.$dyn(e)})` },
              }),
              u > 1 &&
                r().createElement(
                  "div",
                  { className: S.amountBG },
                  r().createElement("div", { className: S.amount }, u),
                ),
            ),
          );
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
        const T = (0, a.Pi)(({ className: e }) => {
          const u = _().model,
            t = (0, B.GS)().mediaSize,
            n = t === B.cJ.Small || t === B.cJ.ExtraSmall ? x.Small : x.Big;
          return r().createElement(
            "div",
            { className: D()(g, e) },
            r().createElement(
              C.z,
              { classNames: { bar: f } },
              r().createElement(
                "div",
                { className: h },
                R.strings.crew.serviceRecord.achievementsList.title(),
              ),
              r().createElement(
                "div",
                { className: p },
                (0, l.UI)(u.computes.getAchievementsList(), (e, u) =>
                  r().createElement(
                    y,
                    k({}, e, { size: n, key: `achievement_${u}`, className: v }),
                  ),
                ),
              ),
            ),
          );
        });
        var L = t(6373);
        const N = "BattlesInfo_base_25",
          M = "BattlesInfo_container_da",
          O = "Item_base_e0",
          P = "Item_icon_81",
          I = "Item_value_28",
          H = "Item_name_35",
          W = ({ name: e, icon: u, value: t }) =>
            r().createElement(
              "div",
              { className: O },
              r().createElement("div", { className: P, style: { backgroundImage: `url(${u})` } }),
              r().createElement("div", { className: I }, t),
              r().createElement("div", { className: H }, e),
            );
        var V = t(3649);
        const Z = "RankItem_base_19",
          j = "RankItem_icon_10",
          z = "RankItem_name_9d",
          G = ({ name: e, icon: u }) =>
            r().createElement(
              L.i,
              {
                header: R.strings.crew.serviceRecord.tooltip.rank.header(),
                body: R.strings.crew.serviceRecord.tooltip.rank.body(),
              },
              r().createElement(
                "div",
                { className: Z },
                r().createElement("div", {
                  className: j,
                  style: {
                    backgroundImage: `url(${R.images.gui.maps.icons.tankmen.ranks.big.$dyn((0, V.BN)(u))})`,
                  },
                }),
                r().createElement("div", { className: z }, e),
              ),
            ),
          U = (0, a.Pi)(() => {
            const e = _().model;
            return r().createElement(
              "div",
              { className: N },
              r().createElement(
                "div",
                { className: M },
                r().createElement(G, { name: e.rankName.get(), icon: e.rankIcon.get() }),
                r().createElement(
                  L.i,
                  {
                    header: R.strings.tooltips.battlesDetails.header(),
                    body: R.strings.tooltips.battlesDetails.body(),
                  },
                  r().createElement(
                    "div",
                    null,
                    r().createElement(W, {
                      name: R.strings.crew.serviceRecord.battlesCounter(),
                      icon: R.images.gui.maps.icons.crew.serviceRecord.battlesCountIcon(),
                      value: e.battlesCount.get(),
                    }),
                  ),
                ),
                r().createElement(
                  L.i,
                  {
                    header: R.strings.crew.serviceRecord.tooltip.averageXP.header(),
                    body: R.strings.crew.serviceRecord.tooltip.averageXP.body(),
                  },
                  r().createElement(
                    "div",
                    null,
                    r().createElement(W, {
                      name: R.strings.crew.serviceRecord.averageXP(),
                      icon: R.images.gui.maps.icons.crew.serviceRecord.averageXPIcon(),
                      value: e.averageXP.get(),
                    }),
                  ),
                ),
              ),
            );
          }),
          X = "NoAchievements_base_a5",
          $ = "NoAchievements_icon_c7",
          Y = "NoAchievements_text_34",
          K = ({ className: e }) =>
            r().createElement(
              "div",
              { className: D()(X, e) },
              r().createElement("div", { className: $ }),
              r().createElement(
                "div",
                { className: Y },
                R.strings.crew.serviceRecord.noAchievements(),
              ),
            ),
          q = "ServiceRecordApp_achievementsList_fd",
          J = "ServiceRecordApp_noAchievements_07",
          Q = (0, a.Pi)(({ setTTCVisibility: e }) => {
            e(!1);
            const u = _().model.computes.hasAchievements();
            return r().createElement(
              i.d,
              null,
              r().createElement(U, null),
              u ? r().createElement(T, { className: q }) : r().createElement(K, { className: J }),
            );
          }),
          ee = R.views.lobby.crew.personal_case.ServiceRecordView("resId");
        r().memo(({ setTTCVisibility: e }) =>
          r().createElement(
            A,
            { options: { rootId: ee } },
            r().createElement(Q, { setTTCVisibility: e }),
          ),
        );
      },
      3961: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => _ });
        var n = t(6483),
          r = t.n(n),
          a = t(794),
          i = t(7701),
          s = t(6179),
          o = t.n(s);
        const l = "ScrollWithLips_base_81",
          c = "ScrollWithLips_fadeTop_3d",
          E = "ScrollWithLips_fadeBottom_44",
          m = "ScrollWithLips_bar_52",
          d = "ScrollWithLips_content_fb";
        let A;
        !(function (e) {
          ((e.None = "none"), (e.Top = "top"), (e.Both = "both"), (e.Bottom = "bottom"));
        })(A || (A = {}));
        const _ = ({ children: e, className: u, classNames: t }) => {
          const n = (0, s.useState)(A.None),
            _ = n[0],
            F = n[1],
            D = _ === A.Both,
            B = (0, i.c4)();
          return (
            (0, s.useEffect)(() => {
              const e = () => {
                const e = B.getBounds()[1],
                  u = B.animationScroll.scrollPosition.get();
                0 === e
                  ? F(A.None)
                  : u > 1 && u < e - 21
                    ? F(A.Both)
                    : u <= 1
                      ? F(A.Bottom)
                      : u >= e - 21 && F(A.Top);
              };
              return (
                B.events.on("change", e),
                B.events.on("resizeHandled", e),
                B.events.on("recalculateContent", e),
                () => {
                  (B.events.off("change", e),
                    B.events.off("resizeHandled", e),
                    B.events.off("recalculateContent", e));
                }
              );
            }, [B]),
            o().createElement(
              "div",
              { className: r()(l, u) },
              o().createElement(
                a.X.Vertical.Default,
                {
                  api: B,
                  barClassNames: { base: r()(m, null == t ? void 0 : t.bar) },
                  scrollClassNames: { content: d },
                },
                e,
              ),
              (_ === A.Top || D) && o().createElement("div", { className: c }),
              (_ === A.Bottom || D) && o().createElement("div", { className: E }),
            )
          );
        };
      },
      4022: (e, u, t) => {
        "use strict";
        t.d(u, { d: () => c });
        var n = t(6179),
          r = t.n(n),
          a = t(3055);
        const i = "TankmanInfoWrapper_base_5a",
          s = "TankmanInfoWrapper_content_b4",
          o = "TankmanInfoWrapper_tankmanInfo_80",
          l = "TankmanInfoWrapper_children_66",
          c = ({ children: e, isLoggingEnabled: u = !1 }) =>
            r().createElement(
              "div",
              { className: i },
              r().createElement(
                "div",
                { className: s },
                r().createElement(a.JW, { className: o, isLoggingEnabled: u }),
                r().createElement("div", { className: l }, e),
              ),
            );
      },
      3055: (e, u, t) => {
        "use strict";
        t.d(u, { Zk: () => Ve, zn: () => We, JW: () => Ze });
        var n = t(6179),
          r = t.n(n),
          a = t(6483),
          i = t.n(a),
          s = t(7613),
          o = t(7727),
          l = t(3403),
          c = t(3618),
          E = t(3649),
          m = t(7077);
        const d = "TankmanFolder_base_00",
          A = "TankmanFolder_activeZone_c3",
          _ = "TankmanFolder_folderLight_eb",
          F = "TankmanFolder_base__withLight_93",
          D = "TankmanFolder_base__hovered_f8",
          B = "TankmanFolder_folder_f5",
          C = "TankmanFolder_photoFrame_ae",
          g = "TankmanFolder_base__big_60",
          h = "TankmanFolder_icon_74",
          p = "TankmanFolder_editTextWrapper_07",
          v = "TankmanFolder_editText_4c",
          f = R.images.gui.maps.icons.tankmen.icons.c_204x256,
          b = r().memo(function ({
            name: e,
            className: u,
            isSkin: t = !1,
            isFolderLight: a,
            onClick: l,
          }) {
            const c = (0, n.useState)(!1),
              b = c[0],
              w = c[1],
              S = (0, n.useMemo)(() => {
                const u = (0, E.BN)(String(e));
                return null !== (t ? f.$dyn("crewSkins") : f).$dyn(u) ? m.U.c204x256 : m.U.c158x118;
              }, [e, t]),
              x = i()(d, S === m.U.c204x256 && g, a && F, b && D, u);
            return r().createElement(
              "div",
              { className: x },
              r().createElement("div", {
                className: A,
                onMouseEnter: () => {
                  ((0, o.G)(R.sounds.gui_hangar_hover()), w(!0));
                },
                onMouseLeave: () => {
                  w(!1);
                },
                onClick: l,
              }),
              r().createElement("div", { className: _ }),
              r().createElement("div", { className: B }),
              r().createElement(
                "div",
                { className: C },
                r().createElement(m.G, { name: e, size: S, isSkin: t, className: h }),
              ),
              r().createElement(
                "div",
                { className: p },
                r().createElement(s.ZP, {
                  className: v,
                  text: R.strings.crew.personalFile.profileEdit(),
                }),
              ),
            );
          });
        var w = t(3215),
          S = t(3946);
        const x = (0, w.q)()(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  currentVehicle: e.object("currentVehicle"),
                  nativeVehicle: e.object("nativeVehicle"),
                  currentVehicleTags: e.array("currentVehicle.tags"),
                },
                t = (0, S.Om)(() => {
                  const e = u.currentVehicle.get(),
                    t = u.nativeVehicle.get(),
                    n = Boolean(e.name);
                  return {
                    isWrongVehicleType: n && !(e.type === t.type && e.isPremium),
                    isWrongVehicle: n && e.name !== t.name,
                  };
                }),
                n = (0, S.Om)(() => {
                  const e = t(),
                    u = e.isWrongVehicle,
                    n = e.isWrongVehicleType;
                  return u && n;
                }),
                r = (0, S.Om)(() =>
                  u.root.get().hasRetrainDiscount
                    ? { args: { tooltipId: "actionPrice" }, targetId: We }
                    : {
                        contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                        targetId: We,
                      },
                );
              return Object.assign({}, u, {
                computes: {
                  vehicleValidator: t,
                  isRoleLevelPenaltyActive: n,
                  discountTooltipArgs: r,
                },
              });
            },
            ({ externalModel: e }) => ({
              playUniqueVoice: e.createCallbackNoArgs("onPlayUniqueVoice"),
              changeVehicle: e.createCallbackNoArgs("onChangeVehicle"),
              onEditProfileClick: e.createCallbackNoArgs("onEditProfileClick"),
              retrain: e.createCallbackNoArgs("onRetrain"),
            }),
          ),
          y = x[0],
          k = x[1];
        var T = t(3457),
          L = t(3415),
          N = t(2056),
          M = t(5415),
          O = t(4828),
          P = t(1943),
          I = t(8018);
        const H = "CurrentVehicleTrain_base_22",
          W = "CurrentVehicleTrain_container_ae",
          V = "CurrentVehicleTrain_currentVehicle_9d",
          Z = "CurrentVehicleTrain_currentVehicleName_19",
          j = "CurrentVehicleTrain_currentVehicleName__isPremium_86",
          z = "CurrentVehicleTrain_retrainContainer_6a",
          G = "CurrentVehicleTrain_leftContainer_f4",
          U = "CurrentVehicleTrain_rightContainer_60",
          X = "CurrentVehicleTrain_roleLevelContainer_95",
          $ = "CurrentVehicleTrain_roleLevelLabel_31",
          Y = "CurrentVehicleTrain_roleLevelLabel__red_0e",
          K = "CurrentVehicleTrain_retrainBtnContainer_00",
          q = "CurrentVehicleTrain_discountIcon_04",
          J = "CurrentVehicleTrain_discountIcon__forText_d9",
          Q = "CurrentVehicleTrain_retrainBtn_3e",
          ee = "CurrentVehicleTrain_frameGlow_80",
          ue = "CurrentVehicleTrain_trainLevelRateContainer_5c",
          te = "CurrentVehicleTrain_trainLevelNumber_b0",
          ne = "CurrentVehicleTrain_trainLevelNumber__red_07",
          re = "CurrentVehicleTrain_trainLevelInfoIcon_27",
          ae = "CurrentVehicleTrain_discountContainer_24",
          ie = "CurrentVehicleTrain_discountText_45";
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
        const oe = (0, l.Pi)(function ({ className: e }) {
          const u = k(),
            t = u.model,
            a = u.controls,
            s = (0, M.GS)().mediaSize,
            o = t.currentVehicle.get(),
            l = o.name,
            E = Boolean(l),
            m = t.computes.vehicleValidator().isWrongVehicle,
            d = t.computes.discountTooltipArgs(),
            A = t.root.get(),
            _ = A.hasRetrainDiscount,
            F = A.realRoleLevel,
            D = t.computes.isRoleLevelPenaltyActive(),
            B = (0, n.useContext)(Ve),
            C = (0, P.Sr)(O.D9, {
              item: O.sk.MstlTooltip,
              action: O.eX.Viewed,
              parentScreen: O.sC.PersonalFile,
            });
          return r().createElement(
            "div",
            { className: i()(H, e) },
            r().createElement(
              "div",
              { className: W },
              r().createElement(
                "div",
                { className: G },
                r().createElement(
                  N.u,
                  se(
                    {
                      targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      ignoreShowDelay: !0,
                      ignoreMouseClick: !0,
                    },
                    B ? C : void 0,
                  ),
                  r().createElement(
                    "div",
                    null,
                    r().createElement(c.w, {
                      classMix: V,
                      text: E
                        ? R.strings.crew.personalFile.inVehicle()
                        : R.strings.crew.common.inBarracks(),
                      binding: {
                        vehicle: r().createElement(
                          "div",
                          { className: i()(Z, o.isPremium && j) },
                          l,
                        ),
                      },
                    }),
                  ),
                ),
              ),
              r().createElement(
                "div",
                { className: U },
                r().createElement(
                  N.u,
                  se(
                    {
                      targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      ignoreShowDelay: !0,
                      ignoreMouseClick: !0,
                    },
                    B ? C : void 0,
                  ),
                  r().createElement(
                    "div",
                    { className: X },
                    r().createElement(
                      "div",
                      { className: i()($, D && Y) },
                      R.strings.crew.personalFile.retrainLevel(),
                    ),
                    r().createElement(
                      "div",
                      { className: ue },
                      r().createElement("div", { className: i()(te, D && ne) }, (0, I.T3)(F)),
                      !D && r().createElement("div", { className: re }),
                    ),
                  ),
                ),
                D &&
                  r().createElement(
                    L.l,
                    { tooltipArgs: d },
                    r().createElement(
                      "div",
                      { className: z },
                      r().createElement(
                        "div",
                        { className: K },
                        _ && r().createElement("div", { className: q }),
                        r().createElement(
                          T.u5,
                          { onClick: a.retrain, type: T.L$.secondary, mixClass: Q },
                          m && r().createElement("div", { className: ee }),
                          R.strings.crew.personalFile.retrain(),
                        ),
                      ),
                    ),
                  ),
                _ &&
                  !D &&
                  r().createElement(
                    L.l,
                    { tooltipArgs: d },
                    r().createElement(
                      "div",
                      { className: ae },
                      r().createElement("div", { className: i()(q, J) }),
                      r().createElement(
                        "div",
                        { className: ie },
                        s === M.cJ.ExtraSmall || s === M.cJ.Small
                          ? R.strings.crew.personalFile.discount.short()
                          : R.strings.crew.personalFile.discount.full(),
                      ),
                    ),
                  ),
              ),
            ),
          );
        });
        var le = t(6373);
        const ce = "Name_base_2d",
          Ee = "Name_label_31",
          me = "Name_voiceButton_00",
          de = "Name_soundIcon_2a",
          Ae = (0, l.Pi)(function ({ className: e }) {
            const u = k(),
              t = u.model,
              a = u.controls,
              o = t.root.get(),
              l = o.fullName,
              c = o.hasUniqueSound,
              E = (0, n.useCallback)(() => {
                a.playUniqueVoice();
              }, [a]);
            return r().createElement(
              "div",
              { className: i()(ce, e) },
              r().createElement(
                "div",
                null,
                r().createElement("div", { className: Ee }, r().createElement(s.ZP, { text: l })),
                c &&
                  r().createElement(
                    le.i,
                    {
                      header: R.strings.crew.personalFile.voiceTooltip.header(),
                      body: R.strings.crew.personalFile.voiceTooltip.body(),
                    },
                    r().createElement(
                      T.u5,
                      { size: T.qE.extraSmall, type: T.L$.ghost, mixClass: me, onClick: E },
                      r().createElement("div", { className: de }),
                    ),
                  ),
              ),
            );
          });
        var _e = t(7078),
          Fe = t(2603);
        const De = "Role_base_e0",
          Be = "Role_role_2a",
          Ce = "Role_roleIcon_e6",
          ge = "Role_roleName_79",
          he = "Role_commanderFeature_e2",
          pe = "Role_sense_21",
          ve = "Role_commanderBonus_99",
          fe = (0, n.memo)(({ role: e, isFemale: u, className: t, setIsFolderLight: n }) =>
            r().createElement(
              "div",
              { className: i()(De, t) },
              r().createElement(
                _e.t,
                { args: { tooltipId: Fe.v$ }, targetId: We, ignoreShowDelay: !1 },
                r().createElement(
                  "div",
                  {
                    className: Be,
                    onMouseEnter: () => {
                      n && n(!0);
                    },
                    onMouseLeave: () => {
                      n && n(!1);
                    },
                  },
                  r().createElement("div", {
                    style: {
                      backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(e)})`,
                    },
                    className: Ce,
                  }),
                  r().createElement(
                    "div",
                    { className: ge },
                    r().createElement(s.ZP, { text: (0, I.Gc)(e, u) }),
                  ),
                ),
              ),
              "commander" === e &&
                r().createElement(
                  "div",
                  { className: he },
                  r().createElement(
                    _e.t,
                    {
                      args: { skillName: "commander_sixthSense", tooltipId: Fe.HZ, level: 100 },
                      targetId: We,
                    },
                    r().createElement("div", { className: pe }),
                  ),
                  r().createElement(
                    _e.t,
                    { args: { tooltipId: Fe.uN }, targetId: We },
                    r().createElement("div", { className: ve }),
                  ),
                ),
            ),
          );
        var be = t(9690);
        const we = {
          base: "SpecializationSlots_base_1a",
          frame: "SpecializationSlots_frame_85",
          frame__first: "SpecializationSlots_frame__first_23",
          arrowsIcon: "SpecializationSlots_arrowsIcon_fc",
          changeVehicle: "SpecializationSlots_changeVehicle_58",
          tier: "SpecializationSlots_tier_68",
          vehicle: "SpecializationSlots_vehicle_b6",
          vehicleTypeIcon: "SpecializationSlots_vehicleTypeIcon_77",
          info: "SpecializationSlots_info_7c",
          flag: "SpecializationSlots_flag_84",
          vehicleIcon: "SpecializationSlots_vehicleIcon_ec",
          premVehicle: "SpecializationSlots_premVehicle_c3",
        };
        function Se() {
          return (
            (Se =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Se.apply(this, arguments)
          );
        }
        const xe = ({ isCrewLocked: e, nativeVehicle: u, className: t, setIsFolderLight: a }) => {
            const s = (0, n.useContext)(Ve),
              o = (0, P.Sr)(O.D9, {
                item: O.sk.PremiumTooltip,
                action: O.eX.Viewed,
                parentScreen: O.sC.PersonalFile,
              }),
              l = (0, n.useCallback)(() => {
                a(!0);
              }, [a]),
              c = (0, n.useCallback)(() => a(!1), [a]),
              m = (0, n.useCallback)(
                (e) => ({
                  backgroundImage: `url(${R.images.gui.maps.icons.vehicleTypes.$dyn(e ? "c_48x48_elite" : "c_48x48_specSlot").$dyn((0, E.BN)(u.type))})`,
                }),
                [u.type],
              ),
              d = {
                backgroundImage: `url(${R.images.gui.maps.icons.nations.c_155x31.$dyn(u.nation)})`,
              };
            return r().createElement(
              "div",
              { className: i()(we.base, t) },
              r().createElement(
                le.i,
                {
                  header: e
                    ? R.strings.crew.personalFile.crewLockedTooltip.header()
                    : R.strings.crew.personalFile.vehicleTooltip.header(),
                  body: e ? R.strings.crew.personalFile.crewLockedTooltip.body() : u.name,
                  ignoreMouseClick: e,
                },
                r().createElement(
                  "div",
                  {
                    id: "retraining_btn",
                    onMouseEnter: e ? void 0 : l,
                    onMouseLeave: e ? void 0 : c,
                    className: i()(we.frame, we.frame__first, e && we.frame__crewLocked),
                  },
                  r().createElement("div", { style: d, className: we.flag }),
                  r().createElement("div", {
                    style: {
                      backgroundImage: `url(${R.images.gui.maps.icons.vehicle.small.$dyn((0, E.BN)(`${u.nation}-${u.techName}`))})`,
                    },
                    className: we.vehicleIcon,
                  }),
                  r().createElement(
                    "div",
                    { className: we.info },
                    r().createElement("div", { className: we.tier }, (0, be.HG)(u.tier)),
                    r().createElement("div", {
                      style: m(u.isPremium),
                      className: we.vehicleTypeIcon,
                    }),
                    r().createElement("div", { className: we.vehicle }, u.name),
                  ),
                ),
              ),
              r().createElement(
                N.u,
                Se(
                  {
                    targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                    contentId: R.views.lobby.crew.tooltips.PremiumVehicleTooltip("resId"),
                  },
                  s ? o : void 0,
                ),
                r().createElement(
                  "div",
                  { className: we.frame },
                  r().createElement("div", { style: d, className: we.flag }),
                  r().createElement(
                    "div",
                    { className: we.info },
                    r().createElement("div", { style: m(!0), className: we.vehicleTypeIcon }),
                    r().createElement(
                      "div",
                      { className: we.premVehicle },
                      R.strings.crew.personalFile.premiumVehicle(),
                    ),
                  ),
                ),
              ),
            );
          },
          ye = "TankmanInfoApp_base_8a",
          ke = "TankmanInfoApp_tankmanFolder_2d",
          Te = "TankmanInfoApp_descriptionBlock_f2",
          Le = "TankmanInfoApp_role_71",
          Ne = "TankmanInfoApp_name_68",
          Re = "TankmanInfoApp_description_a6",
          Me = "TankmanInfoApp_currentVehicle_06",
          Oe = "TankmanInfoApp_nativeVehicle_5c",
          Pe = "TankmanInfoApp_nativeVehicle__withDescription_03",
          Ie = "TankmanInfoApp_slots_a1",
          He = (0, l.Pi)(({ className: e }) => {
            const u = k(),
              t = u.model,
              a = u.controls,
              l = t.root.get(),
              E = l.description,
              m = l.iconName,
              d = l.isFemale,
              A = l.isCrewLocked,
              _ = l.role,
              F = l.isInSkin,
              D = t.nativeVehicle.get(),
              B = Boolean(E),
              C = (0, n.useState)(!1),
              g = C[0],
              h = C[1],
              p = (0, n.useCallback)(() => {
                ((0, o.G)(R.sounds.yes1()), a.onEditProfileClick());
              }, [a]);
            return r().createElement(
              "div",
              { className: i()(ye, e) },
              r().createElement(b, {
                isFolderLight: g,
                name: m,
                isSkin: F,
                className: ke,
                onClick: p,
              }),
              r().createElement(
                "div",
                { className: Te },
                r().createElement(fe, { className: Le, isFemale: d, role: _, setIsFolderLight: h }),
                r().createElement(Ae, { className: Ne }),
                B &&
                  r().createElement(c.w, {
                    classMix: Re,
                    isTruncationAvailable: !0,
                    isTooltipEnable: !0,
                    targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                    text: E,
                  }),
                r().createElement(
                  "div",
                  { className: i()(Oe, B && Pe) },
                  r().createElement(s.ZP, { text: R.strings.crew.personalFile.specialization() }),
                ),
                r().createElement(xe, {
                  nativeVehicle: D,
                  isCrewLocked: A,
                  className: Ie,
                  setIsFolderLight: h,
                }),
                r().createElement(oe, { className: Me }),
              ),
            );
          }),
          We = R.views.lobby.crew.widgets.TankmanInfo("resId"),
          Ve = (0, n.createContext)(!1),
          Ze = r().memo(function ({ rootId: e = We, className: u, isLoggingEnabled: t = !1 }) {
            return r().createElement(
              y,
              { options: { rootId: e } },
              r().createElement(Ve.Provider, { value: t }, r().createElement(He, { className: u })),
            );
          });
      },
      2603: (e, u, t) => {
        "use strict";
        t.d(u, { HZ: () => n, Th: () => a, uN: () => r, v$: () => i });
        const n = "crewPerkGf",
          r = "commanderBonus",
          a = "achievement",
          i = "tankman";
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
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = { base: "FormatText_base_d0" };
      },
      372: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          base: "HorizontalBar_base_49",
          base__nonActive: "HorizontalBar_base__nonActive_82",
          leftButton: "HorizontalBar_leftButton_5f",
          rightButton: "HorizontalBar_rightButton_03",
          track: "HorizontalBar_track_0d",
          thumb: "HorizontalBar_thumb_fd",
          rail: "HorizontalBar_rail_32",
        };
      },
      4682: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          base: "HorizontalScroll_base_29",
          wrapper: "HorizontalScroll_wrapper_1e",
          defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
        };
      },
      9168: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          base: "VerticalBar_base_f3",
          base__nonActive: "VerticalBar_base__nonActive_42",
          topButton: "VerticalBar_topButton_d7",
          bottomButton: "VerticalBar_bottomButton_06",
          track: "VerticalBar_track_df",
          thumb: "VerticalBar_thumb_32",
          rail: "VerticalBar_rail_43",
        };
      },
      5636: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          content: "VerticalScroll_content_cb",
          defaultScroll: "VerticalScroll_defaultScroll_f8",
          bar: "VerticalScroll_bar_1e",
          area: "VerticalScroll_area_af",
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
      6143: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          base: "ExtendedText_base_71",
          base__zeroPadding: "ExtendedText_base__zeroPadding_25",
          base__isTruncationAvailable: "ExtendedText_base__isTruncationAvailable_5b",
          truncated: "ExtendedText_truncated_97",
          truncated__hide: "ExtendedText_truncated__hide_31",
          unTruncated: "ExtendedText_unTruncated_b8",
        };
      },
      9627: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
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
        };
      },
      7629: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          noBreakWrapper: "renderers_noBreakWrapper_10",
          lineBreak: "renderers_lineBreak_b5",
          newLine: "renderers_newLine_bd",
        };
      },
      3938: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = {
          base: "TankmanIcon_base_f9",
          base__big: "TankmanIcon_base__big_98",
          base__small: "TankmanIcon_base__small_b2",
          base__barracks: "TankmanIcon_base__barracks_62",
          base__special: "TankmanIcon_base__special_3f",
          base__c_204x256: "TankmanIcon_base__c_204x256_97",
          innerShadow: "TankmanIcon_innerShadow_c6",
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
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, n] = deferred[o], a = !0, i = 0; i < u.length; i++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[i]))
              ? u.splice(i--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(o--, 1);
            var s = t();
            void 0 !== s && (e = s);
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
    (__webpack_require__.j = 2),
    (() => {
      var e = { 2: 0, 987: 0, 42: 0, 695: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            r,
            [a, i, s] = t,
            o = 0;
          if (a.some((u) => 0 !== e[u])) {
            for (n in i) __webpack_require__.o(i, n) && (__webpack_require__.m[n] = i[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (u && u(t); o < a.length; o++)
            ((r = a[o]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(894));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
