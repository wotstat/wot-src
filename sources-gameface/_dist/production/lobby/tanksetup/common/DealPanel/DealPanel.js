(() => {
  "use strict";
  var __webpack_modules__ = {
      3457: (e, u, t) => {
        t.d(u, { L$: () => s.L, qE: () => s.q, u5: () => d });
        var n = t(6483),
          r = t.n(n),
          o = t(7727),
          i = t(6179),
          l = t.n(i),
          a = t(6880),
          s = t(2106);
        const c = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: c,
          mixClass: d,
          soundHover: _,
          soundClick: E,
          onMouseEnter: h,
          onMouseMove: m,
          onMouseDown: A,
          onMouseUp: b,
          onMouseLeave: F,
          onClick: v,
        }) => {
          const C = (0, i.useRef)(null),
            g = (0, i.useState)(t),
            D = g[0],
            f = g[1],
            p = (0, i.useState)(!1),
            B = p[0],
            w = p[1],
            y = (0, i.useState)(!1),
            L = y[0],
            k = y[1],
            S = (0, i.useCallback)(() => {
              c || (C.current && (C.current.focus(), f(!0)));
            }, [c]),
            x = (0, i.useCallback)(
              (e) => {
                D && null !== C.current && !C.current.contains(e.target) && f(!1);
              },
              [D],
            ),
            M = (0, i.useCallback)(
              (e) => {
                c || (v && v(e));
              },
              [c, v],
            ),
            T = (0, i.useCallback)(
              (e) => {
                c || (null !== _ && (0, o.G)(_), h && h(e), k(!0));
              },
              [c, _, h],
            ),
            O = (0, i.useCallback)(
              (e) => {
                m && m(e);
              },
              [m],
            ),
            P = (0, i.useCallback)(
              (e) => {
                c || (b && b(e), w(!1));
              },
              [c, b],
            ),
            H = (0, i.useCallback)(
              (e) => {
                c || (null !== E && (0, o.G)(E), A && A(e), t && S(), w(!0));
              },
              [c, E, A, S, t],
            ),
            W = (0, i.useCallback)(
              (e) => {
                c || (F && F(e), w(!1));
              },
              [c, F],
            ),
            Y = r()(
              a.Z.base,
              a.Z[`base__${n}`],
              {
                [a.Z.base__disabled]: c,
                [a.Z[`base__${u}`]]: u,
                [a.Z.base__focus]: D,
                [a.Z.base__highlightActive]: B,
                [a.Z.base__firstHover]: L,
              },
              d,
            ),
            N = r()(a.Z.state, a.Z.state__default);
          return (
            (0, i.useEffect)(
              () => (
                document.addEventListener("mousedown", x),
                () => {
                  document.removeEventListener("mousedown", x);
                }
              ),
              [x],
            ),
            (0, i.useEffect)(() => {
              f(t);
            }, [t]),
            l().createElement(
              "div",
              {
                ref: C,
                className: Y,
                onMouseEnter: T,
                onMouseMove: O,
                onMouseUp: P,
                onMouseDown: H,
                onMouseLeave: W,
                onClick: M,
              },
              n !== s.L.ghost &&
                l().createElement(
                  l().Fragment,
                  null,
                  l().createElement("div", { className: a.Z.back }),
                  l().createElement("span", { className: a.Z.texture }),
                ),
              l().createElement(
                "span",
                { className: N },
                l().createElement("span", { className: a.Z.stateDisabled }),
                l().createElement("span", { className: a.Z.stateHighlightHover }),
                l().createElement("span", { className: a.Z.stateHighlightActive }),
              ),
              l().createElement(
                "span",
                { className: a.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        c.defaultProps = {
          type: s.L.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const d = (0, i.memo)(c);
      },
      2106: (e, u, t) => {
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
      2262: (e, u, t) => {
        t.d(u, { XZ: () => E });
        var n = t(6483),
          r = t.n(n),
          o = t(1641),
          i = t(7727),
          l = t(6179),
          a = t.n(l),
          s = t(4382),
          c = t(8844);
        const d = [
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
        const E = (e) => {
          let u = e.id,
            t = e.isChecked,
            n = void 0 !== t && t,
            E = e.isDisabled,
            h = void 0 !== E && E,
            m = e.isAlert,
            A = void 0 !== m && m,
            b = e.size,
            F = void 0 === b ? c.yB.medium : b,
            v = e.type,
            C = void 0 === v ? c.Rh.primary : v,
            g = e.soundHover,
            D = void 0 === g ? "highlight" : g,
            f = e.soundClick,
            p = void 0 === f ? "play" : f,
            B = e.onMouseEnter,
            w = e.onMouseLeave,
            y = e.onMouseUp,
            L = e.onMouseDown,
            k = e.onClick,
            S = e.onChange,
            x = e.onFocus,
            M = e.onBlur,
            R = e.text,
            T = e.contentStyles,
            O = e.children,
            P = e.alignment,
            H = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, d);
          const W = (0, l.useState)(!1),
            Y = W[0],
            N = W[1],
            X = (0, l.useState)(!1),
            I = (X[0], X[1]),
            U = (0, l.useCallback)(
              (e) => {
                h || (S && S(), k && k(e));
              },
              [h, S, k],
            ),
            j = (0, l.useCallback)(
              (e) => {
                const u = e.button === o.t.LEFT;
                h || (u && N(!0), u && L && L(e), p && (0, i.G)(p));
              },
              [h, L, p],
            ),
            Z = (0, l.useCallback)(
              (e) => {
                h || (N(!1), y && y(e));
              },
              [h, y],
            ),
            z = (0, l.useCallback)(
              (e) => {
                h || (B && B(e), D && (0, i.G)(D));
              },
              [h, B, D],
            ),
            q = (0, l.useCallback)(
              (e) => {
                h || (N(!1), w && w(e));
              },
              [h, w],
            ),
            K = (0, l.useCallback)(
              (e) => {
                h || (I(!0), x && x(e));
              },
              [h, x],
            ),
            G = (0, l.useCallback)(
              (e) => {
                h || (I(!1), M && M(e));
              },
              [h, M],
            ),
            V = a().createElement(
              "div",
              { className: s.Z.label },
              a().createElement(
                "div",
                { className: r()(s.Z.labelContent, "s-labelContent"), style: T },
                R || O,
              ),
            );
          return a().createElement(
            "div",
            _(
              {
                id: u,
                className: r()(s.Z.base, s.Z[`base__${F}`], s.Z[`base__${C}`], {
                  [s.Z.base__checked]: n,
                  [s.Z.base__disabled]: h,
                  [s.Z.base__mouseDown]: Y,
                  [s.Z.base__alert]: A,
                  [s.Z.base__center]: P === c.N3.Center,
                  [s.Z.base__bottom]: P === c.N3.Bottom,
                }),
                onClick: U,
                onMouseEnter: z,
                onMouseLeave: q,
                onMouseDown: j,
                onMouseUp: Z,
                onFocus: K,
                onBlur: G,
              },
              H,
            ),
            a().createElement(
              "div",
              { className: s.Z.input },
              a().createElement("div", { className: s.Z.alertOverlay }),
              a().createElement("div", { className: s.Z.inputHoverOverlay }),
              a().createElement("div", { className: s.Z.highlight }),
            ),
            a().createElement("div", { className: s.Z.checkmark }),
            ((R || O) && V) || null,
          );
        };
      },
      8844: (e, u, t) => {
        let n, r, o;
        (t.d(u, { N3: () => o, Rh: () => r, yB: () => n }),
          (function (e) {
            ((e.small = "small"),
              (e.medium = "medium"),
              (e.large = "large"),
              (e.extraLarge = "extraLarge"));
          })(n || (n = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(r || (r = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(o || (o = {})));
      },
      7405: (e, u, t) => {
        var n = t(6483),
          r = t.n(n),
          o = t(6179),
          i = t.n(o),
          l = t(329),
          a = t(2372),
          s = t(8460);
        const c = ({
          isDiscount: e,
          isInteractiveDiscount: u,
          size: t,
          type: n,
          isEnough: o,
          value: c,
          discountValue: d,
          showPlus: _,
          stockBackgroundName: E = l.we.Red,
        }) => {
          const h = r()(s.Z.value, s.Z[`value__${n}`], !o && s.Z.value__notEnough),
            m = r()(s.Z.icon, s.Z[`icon__${n}-${t}`]),
            A = r()(s.Z.stock, d && s.Z.stock__indent, u && s.Z.stock__interactive),
            b = _ && c > 0 && "+",
            F = r()(s.Z.base, s.Z[`base__${t}`]);
          return i().createElement(
            "span",
            { className: F },
            i().createElement(
              "span",
              { className: h },
              b,
              i().createElement(a.A, { value: c, format: n === l.V2.gold ? "gold" : "integral" }),
            ),
            i().createElement("span", { className: m }),
            e &&
              i().createElement(
                "span",
                { className: A },
                i().createElement("span", {
                  className: s.Z.stockBackground,
                  style: { backgroundImage: `url(R.images.gui.maps.icons.library.${E})` },
                }),
                Boolean(d) && d,
              ),
          );
        };
        c.defaultProps = { isEnough: !0 };
        i().memo(c);
      },
      329: (e, u, t) => {
        let n, r, o;
        (t.d(u, { V2: () => r, we: () => o }),
          (function (e) {
            ((e.small = "small"),
              (e.big = "big"),
              (e.large = "large"),
              (e.extraLarge = "extraLarge"));
          })(n || (n = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(r || (r = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(o || (o = {})));
      },
      2372: (e, u, t) => {
        t.d(u, { A: () => i });
        var n = t(6179),
          r = t.n(n),
          o = t(4179);
        class i extends r().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = o.B3.GOLD;
            else e = o.B3.INTEGRAL;
            const u = o.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        i.defaultProps = { format: "integral" };
      },
      3495: (e, u, t) => {
        t.d(u, { Y: () => d });
        var n = t(3138),
          r = t(6179),
          o = t(1043),
          i = t(5262);
        const l = n.O.client.getSize("rem"),
          a = l.width,
          s = l.height,
          c = Object.assign({ width: a, height: s }, (0, i.T)(a, s, o.j)),
          d = (0, r.createContext)(c);
      },
      1039: (e, u, t) => {
        var n = t(6179),
          r = t.n(n),
          o = t(6536),
          i = t(3495),
          l = t(1043),
          a = t(5262),
          s = t(3138);
        (0, n.memo)(({ children: e }) => {
          const u = (0, n.useContext)(i.Y),
            t = (0, n.useState)(u),
            c = t[0],
            d = t[1],
            _ = (0, n.useCallback)((e, u) => {
              const t = s.O.view.pxToRem(e),
                n = s.O.view.pxToRem(u);
              d(Object.assign({ width: t, height: n }, (0, a.T)(t, n, l.j)));
            }, []);
          ((0, o.Z)(() => {
            engine.on("clientResized", _);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", _), [_]));
          const E = (0, n.useMemo)(() => Object.assign({}, c), [c]);
          return r().createElement(i.Y.Provider, { value: E }, e);
        });
      },
      6010: (e, u, t) => {
        var n = t(6179),
          r = t(7382),
          o = t(3495);
        const i = ["children"];
        const l = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, i);
          const l = (0, n.useContext)(o.Y),
            a = l.extraLarge,
            s = l.large,
            c = l.medium,
            d = l.small,
            _ = l.extraSmall,
            E = l.extraLargeWidth,
            h = l.largeWidth,
            m = l.mediumWidth,
            A = l.smallWidth,
            b = l.extraSmallWidth,
            F = l.extraLargeHeight,
            v = l.largeHeight,
            C = l.mediumHeight,
            g = l.smallHeight,
            D = l.extraSmallHeight,
            f = { extraLarge: F, large: v, medium: C, small: g, extraSmall: D };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && a) return u;
            if (t.large && s) return u;
            if (t.medium && c) return u;
            if (t.small && d) return u;
            if (t.extraSmall && _) return u;
          } else {
            if (t.extraLargeWidth && E) return (0, r.H)(u, t, f);
            if (t.largeWidth && h) return (0, r.H)(u, t, f);
            if (t.mediumWidth && m) return (0, r.H)(u, t, f);
            if (t.smallWidth && A) return (0, r.H)(u, t, f);
            if (t.extraSmallWidth && b) return (0, r.H)(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && F) return u;
              if (t.largeHeight && v) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && g) return u;
              if (t.extraSmallHeight && D) return u;
            }
          }
          return null;
        };
        l.defaultProps = {
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
        (0, n.memo)(l);
      },
      7382: (e, u, t) => {
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
        (t(6010), t(1039), t(3495));
      },
      1043: (e, u, t) => {
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
            o = Math.min(n, r);
          return {
            extraLarge: o === t.extraLarge.weight,
            large: o === t.large.weight,
            medium: o === t.medium.weight,
            small: o === t.small.weight,
            extraSmall: o === t.extraSmall.weight,
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
      570: (e, u, t) => {
        t.d(u, { x: () => A });
        var n = t(6483),
          r = t.n(n),
          o = t(1856),
          i = t(1091),
          l = t(6179),
          a = t.n(l),
          s = t(8380),
          c = t.n(s);
        const d = "ScrollArea_base_47",
          _ = "ScrollArea_base__scrollIndent_1d",
          E = "ScrollArea_base__verticalScrollbarMargin_50",
          h = "ScrollArea_base__multiple_44",
          m = "ScrollArea_base__hidden_ec",
          A = a().forwardRef((e, u) => {
            const t = e.offsetLeft,
              n = void 0 === t ? 0 : t,
              s = e.offsetTop,
              A = void 0 === s ? 0 : s,
              b = e.scrollSettings,
              F = e.onUpdateActiveAxis,
              v = e.onHorizontalScroll,
              C = e.onVerticalScroll,
              g = e.onOverScrollAtBeginning,
              D = e.onOverScrollAtEnd,
              f = e.wrapperIndent,
              p = e.verticalScrollbarMargin,
              B = e.isMultipleScroll,
              w = e.scrollAreaContainer,
              y = e.children,
              L = e.classMix,
              k = e.onScrollLeftHandled,
              S = (0, l.useState)(!1),
              x = S[0],
              M = S[1],
              R = (0, l.useState)(),
              T = R[0],
              O = R[1],
              P = (0, l.useState)(),
              H = P[0],
              W = P[1],
              Y = (0, l.useRef)(null),
              N = (0, l.useCallback)(() => {
                T &&
                  F &&
                  F(
                    { x: T.scrollbarXActive, y: T.scrollbarYActive },
                    { x: T.reach.x, y: T.reach.y },
                  );
              }, [F, T]),
              X = (0, l.useCallback)(() => T, [T]),
              I = (0, l.useCallback)(() => {
                T && T.update();
              }, [T]),
              U = (0, l.useCallback)(
                (e, u, t) => {
                  T && (T.setScrollLeft(e, u, t), k && k(e, T.contentWidth - T.containerWidth));
                },
                [T, k],
              ),
              j = (0, l.useCallback)(
                (e) => {
                  T &&
                    (T.setScrollLeftImmediately(e), k && k(e, T.contentWidth - T.containerWidth));
                },
                [T, k],
              ),
              Z = (0, l.useCallback)(
                (e, u, t) => {
                  T && T.setScrollTop(e, u, t);
                },
                [T],
              ),
              z = (0, l.useCallback)(
                (e) => {
                  T && T.setScrollTopImmediately(e);
                },
                [T],
              ),
              q = (0, l.useCallback)(() => {
                if (H && v && T) {
                  const e = {
                    scrollPosition: H.scrollLeft < 0 ? 0 : H.scrollLeft,
                    reach: T.reach.x,
                  };
                  v(e);
                }
              }, [v, H, T]),
              K = (0, l.useCallback)(() => {
                if (H && C && T) {
                  const e = { scrollPosition: H.scrollTop, reach: T.reach.y };
                  C(e);
                }
              }, [C, H, T]),
              G = (0, l.useCallback)(() => {
                g && g();
              }, [g]),
              V = (0, l.useCallback)(() => {
                D && D();
              }, [D]),
              $ = (0, l.useCallback)(
                (e) => {
                  ("function" == typeof u ? u(e) : null !== u && (u.current = e), W(e));
                },
                [u],
              ),
              Q = (0, l.useCallback)(() => {
                T &&
                  (T.update(),
                  (Y.current = (0, o.v)(() => {
                    N();
                  })));
              }, [T, N]),
              J = (0, l.useCallback)((e) => {
                0 === e.screenX &&
                  0 === e.screenY &&
                  (e.stopImmediatePropagation(), e.preventDefault());
              }, []);
            (0, l.useEffect)(() => {
              if (T && H)
                return (
                  document.addEventListener("mousemove", J),
                  window.addEventListener("resize", Q),
                  H.addEventListener("ps-scroll-x", q),
                  H.addEventListener("ps-scroll-y", K),
                  H.addEventListener("over-scroll-beginning", G),
                  H.addEventListener("over-scroll-ending", V),
                  M(!0),
                  () => {
                    (window.removeEventListener("resize", Q),
                      document.removeEventListener("mousemove", J),
                      H &&
                        (H.removeEventListener("ps-scroll-x", q),
                        H.removeEventListener("ps-scroll-y", K),
                        H.removeEventListener("over-scroll-beginning", G),
                        H.removeEventListener("over-scroll-ending", V)));
                  }
                );
            }, [J, q, G, V, Q, H, T, K]);
            const ee = (0, l.useRef)(H || null);
            ee.current = H || null;
            const ue = (0, i.Z)(ee);
            ((0, l.useEffect)(
              () => (
                !T && H && ue && O(new (c())(H, Object.assign({}, b))),
                () => {
                  T && (T.destroy(), O(void 0));
                }
              ),
              [H, ue, b, T],
            ),
              (0, l.useEffect)(
                () => () => {
                  null == Y.current || Y.current();
                },
                [],
              ),
              (0, l.useEffect)(
                () =>
                  (0, o.v)(() => {
                    T && N();
                  }),
                [N, T],
              ),
              (0, l.useEffect)(() => {
                n > 0 && j(n);
              }, [n, j]),
              (0, l.useEffect)(() => {
                A > 0 && z(A);
              }, [A, z]),
              (0, l.useEffect)(() => {
                w &&
                  ((w.setScrollLeft = U),
                  (w.setScrollTop = Z),
                  (w.setScrollLeftImmediately = j),
                  (w.setScrollTopImmediately = z),
                  (w.updateScrollArea = I),
                  (w.getScrollbar = X));
              }, [w, U, j, Z, z, I, X]));
            const te = r()(d, { [_]: f, [m]: !x, [E]: p, [h]: B }, L);
            return a().createElement("div", { className: te, ref: $ }, y);
          });
      },
      8380: (e) => {
        function u(e) {
          return getComputedStyle(e);
        }
        function t(e, u) {
          for (var t in u) {
            var n = u[t];
            ("number" == typeof n && (n += "px"), (e.style[t] = n));
          }
          return e;
        }
        function n(e) {
          var u = document.createElement("div");
          return ((u.className = e), u);
        }
        var r =
          "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        function o(e, u) {
          if (!r) throw new Error("No element matching method supported");
          return r.call(e, u);
        }
        function i(e) {
          e.remove ? e.remove() : e.parentNode && e.parentNode.removeChild(e);
        }
        function l(e, u) {
          return Array.prototype.filter.call(e.children, function (e) {
            return o(e, u);
          });
        }
        var a = "ps",
          s = {
            thumb: function (e) {
              return "ps__thumb-" + e;
            },
            rail: function (e) {
              return "ps__rail-" + e;
            },
            buttonStart: function (e) {
              return "ps__button-start-" + e;
            },
            track: function (e) {
              return "ps__track_" + e;
            },
            buttonEnd: function (e) {
              return "ps__button-end-" + e;
            },
            consuming: "ps__child--consume",
          },
          c = {
            focus: "ps--focus",
            clicking: "ps--clicking",
            active: function (e) {
              return "ps--active-" + e;
            },
            scrolling: function (e) {
              return "ps--scrolling-" + e;
            },
          },
          d = { x: null, y: null },
          _ = { immediately: !1 };
        function E(e, u, t) {
          void 0 === t && (t = {});
          var n = e.element.classList,
            r = c.scrolling(u);
          n.contains(r) ? clearTimeout(d[u]) : n.add(r);
        }
        function h(e, u, t) {
          void 0 === t && (t = {});
          Object.assign(_, t).immediately
            ? e.isAlive && e.element.classList.remove(c.scrolling(u))
            : (d[u] = setTimeout(function () {
                return e.isAlive && e.element.classList.remove(c.scrolling(u));
              }, e.settings.scrollingThreshold));
        }
        var m = function (e) {
            ((this.element = e), (this.handlers = {}));
          },
          A = { isEmpty: { configurable: !0 } };
        ((m.prototype.bind = function (e, u) {
          (void 0 === this.handlers[e] && (this.handlers[e] = []),
            this.handlers[e].push(u),
            this.element.addEventListener(e, u, !1));
        }),
          (m.prototype.unbind = function (e, u) {
            var t = this;
            this.handlers[e] = this.handlers[e].filter(function (n) {
              return !(!u || n === u) || (t.element.removeEventListener(e, n, !1), !1);
            });
          }),
          (m.prototype.unbindAll = function () {
            for (var e in this.handlers) this.unbind(e);
          }),
          (A.isEmpty.get = function () {
            var e = this;
            return Object.keys(this.handlers).every(function (u) {
              return 0 === e.handlers[u].length;
            });
          }),
          Object.defineProperties(m.prototype, A));
        var b = function () {
          this.eventElements = [];
        };
        function F(e) {
          return parseInt(e, 10) || 0;
        }
        ((b.prototype.eventElement = function (e) {
          var u = this.eventElements.filter(function (u) {
            return u.element === e;
          })[0];
          return (u || ((u = new m(e)), this.eventElements.push(u)), u);
        }),
          (b.prototype.bind = function (e, u, t) {
            this.eventElement(e).bind(u, t);
          }),
          (b.prototype.unbind = function (e, u, t) {
            var n = this.eventElement(e);
            (n.unbind(u, t),
              n.isEmpty && this.eventElements.splice(this.eventElements.indexOf(n), 1));
          }),
          (b.prototype.unbindAll = function () {
            (this.eventElements.forEach(function (e) {
              return e.unbindAll();
            }),
              (this.eventElements = []));
          }),
          (b.prototype.once = function (e, u, t) {
            var n = this.eventElement(e);
            n.bind(u, function e(r) {
              (n.unbind(u, e), t(r));
            });
          }));
        var v = {
          isWebKit:
            "undefined" != typeof document && "WebkitAppearance" in document.documentElement.style,
          supportsTouch:
            "undefined" != typeof window &&
            ("ontouchstart" in window ||
              (window.DocumentTouch && document instanceof window.DocumentTouch)),
          supportsIePointer: "undefined" != typeof navigator && navigator.msMaxTouchPoints,
          isChrome:
            "undefined" != typeof navigator && /Chrome/i.test(navigator && navigator.userAgent),
        };
        function C() {
          return new Promise(function (e) {
            requestAnimationFrame(function () {
              requestAnimationFrame(function () {
                e();
              });
            });
          });
        }
        function g(e) {
          if ("function" == typeof window.CustomEvent) return new CustomEvent(e);
          var u = document.createEvent("CustomEvent");
          return (u.initCustomEvent(e, !1, !1, void 0), u);
        }
        var D = function (e, u, t, n, r, o) {
          var i;
          if (
            (void 0 === n && (n = !0),
            void 0 === r && (r = !1),
            void 0 === o && (o = !1),
            "top" === u)
          )
            i = ["contentHeight", "containerHeight", "scrollTop", "y", "up", "down"];
          else {
            if ("left" !== u) throw new Error("A proper axis should be provided");
            i = ["contentWidth", "containerWidth", "scrollLeft", "x", "left", "right"];
          }
          !(function (e, u, t, n, r, o) {
            var i = t[0],
              l = t[1],
              a = t[2],
              s = t[3],
              c = t[4],
              d = t[5];
            void 0 === n && (n = !0);
            void 0 === r && (r = !1);
            void 0 === o && (o = !1);
            var _ = e.element;
            if (!e.reach) return;
            ((e.reach[s] = null), _[a] < 1 && (e.reach[s] = "start"));
            _[a] > e[i] - e[l] - 1 && (e.reach[s] = "end");
            u &&
              !r &&
              (_.dispatchEvent(g("ps-scroll-" + s)),
              u < 0
                ? _.dispatchEvent(g("ps-scroll-" + c))
                : u > 0 && _.dispatchEvent(g("ps-scroll-" + d)),
              n &&
                (function (e, u) {
                  (E(e, u), h(e, u));
                })(e, s));
            e.reach[s] && (u || o) && _.dispatchEvent(g("ps-" + s + "-reach-" + e.reach[s]));
          })(e, t, i, n, r, o);
        };
        var f = function (e, u, n, r) {
          (void 0 === u && (u = !1), void 0 === n && (n = 0), void 0 === r && (r = !1));
          var o = e.element;
          if (o) {
            if (
              ((e.containerWidth = Math.round(o.getBoundingClientRect().width)),
              (e.containerHeight = Math.round(o.getBoundingClientRect().height)),
              (e.contentWidth = Math.round(o.scrollWidth) - 2 * n),
              (e.contentHeight = Math.round(o.scrollHeight)),
              !r)
            ) {
              e.contentWidth = Math.round(o.scrollWidth) - 2 * n;
              var a = e.contentWidth - e.containerWidth + n;
              o.scrollLeft < n ? (o.scrollLeft = n) : o.scrollLeft > a && (o.scrollLeft = a);
            }
            var d = Math.floor(o.scrollTop),
              _ = Math.floor(o.scrollLeft) - n,
              E = parseFloat(getComputedStyle(document.documentElement).fontSize);
            (o.contains(e.scrollbarXRail) ||
              (l(o, s.rail("x")).forEach(function (e) {
                return i(e);
              }),
              o.appendChild(e.scrollbarXRail)),
              o.contains(e.scrollbarYRail) ||
                (l(o, s.rail("y")).forEach(function (e) {
                  return i(e);
                }),
                o.appendChild(e.scrollbarYRail)),
              !e.settings.suppressScrollX &&
              e.containerWidth + e.settings.scrollXMarginOffset < e.contentWidth
                ? ((e.scrollbarXActive = !0),
                  (e.railXWidth = e.containerWidth - e.railXMarginWidth * E - 15 * E),
                  (e.railXRatio = e.containerWidth / e.railXWidth),
                  (e.scrollbarXWidth = p(e, F((e.railXWidth * e.containerWidth) / e.contentWidth))),
                  (e.scrollbarXLeft = F(
                    ((e.negativeScrollAdjustment + _) * (e.railXWidth - e.scrollbarXWidth)) /
                      (e.contentWidth - e.containerWidth),
                  )),
                  e.scrollbarXLeft < 0 && (e.scrollbarXLeft = 0))
                : (e.scrollbarXActive = !1),
              !e.settings.suppressScrollY &&
              e.containerHeight + e.settings.scrollYMarginOffset < e.contentHeight
                ? ((e.scrollbarYActive = !0),
                  (e.railYHeight = e.containerHeight - e.railYMarginHeight * E - 15 * E),
                  (e.railYRatio = e.containerHeight / e.railYHeight),
                  (e.scrollbarYHeight = p(
                    e,
                    F((e.railYHeight * e.containerHeight) / e.contentHeight),
                  )),
                  (e.scrollbarYTop = F(
                    (d * (e.railYHeight - e.scrollbarYHeight)) /
                      (e.contentHeight - e.containerHeight),
                  )))
                : (e.scrollbarYActive = !1),
              e.scrollbarXLeft >= e.railXWidth - e.scrollbarXWidth &&
                (e.scrollbarXLeft = e.railXWidth - e.scrollbarXWidth),
              e.scrollbarYTop >= e.railYHeight - e.scrollbarYHeight &&
                (e.scrollbarYTop = e.railYHeight - e.scrollbarYHeight),
              (function (e, u, n) {
                var r = { width: u.railXWidth },
                  o = Math.floor(e.scrollTop);
                u.isRtl
                  ? (r.left =
                      u.negativeScrollAdjustment + e.scrollLeft + u.containerWidth - u.contentWidth)
                  : (r.left = e.scrollLeft);
                u.isScrollbarXUsingBottom
                  ? (r.bottom = u.scrollbarXBottom - o)
                  : (r.top = u.scrollbarXTop + o);
                t(u.scrollbarXRail, r);
                var i = { top: o, height: u.railYHeight };
                u.isScrollbarYUsingRight
                  ? u.isRtl
                    ? (i.right =
                        u.contentWidth -
                        (u.negativeScrollAdjustment + e.scrollLeft) -
                        u.scrollbarYRight -
                        u.scrollbarYOuterWidth)
                    : (i.right = u.scrollbarYRight - e.scrollLeft)
                  : u.isRtl
                    ? (i.left =
                        u.negativeScrollAdjustment +
                        e.scrollLeft +
                        2 * u.containerWidth -
                        u.contentWidth -
                        u.scrollbarYLeft -
                        u.scrollbarYOuterWidth)
                    : (i.left = u.scrollbarYLeft + e.scrollLeft);
                (t(u.scrollbarYRail, i),
                  t(u.scrollbarX, {
                    left: u.scrollbarXLeft,
                    width: u.scrollbarXWidth - u.railBorderXWidth * n,
                  }),
                  t(u.scrollbarY, {
                    top: u.scrollbarYTop,
                    height: u.scrollbarYHeight - u.railBorderYWidth * n,
                  }));
              })(o, e, E),
              e.scrollbarXButtonStart.classList.toggle("disabled", _ < 1),
              e.scrollbarXButtonEnd.classList.toggle(
                "disabled",
                _ + e.containerWidth >= e.contentWidth,
              ),
              e.scrollbarYButtonStart.classList.toggle("disabled", o.scrollTop < 1),
              e.scrollbarYButtonEnd.classList.toggle(
                "disabled",
                o.scrollTop + e.containerHeight >= e.contentHeight,
              ),
              e.scrollbarXActive
                ? (o.classList.add(c.active("x")), D(e, "left", _ - e.lastScrollLeft, !0, u))
                : (o.classList.remove(c.active("x")),
                  (e.scrollbarXWidth = 0),
                  (e.scrollbarXLeft = 0),
                  (o.scrollLeft = 0)),
              e.scrollbarYActive
                ? (o.classList.add(c.active("y")),
                  D(e, "top", o.scrollTop - e.lastScrollTop, !0, u))
                : (o.classList.remove(c.active("y")),
                  (e.scrollbarYHeight = 0),
                  (e.scrollbarYTop = 0),
                  (o.scrollTop = 0)),
              (e.lastScrollTop = d),
              (e.lastScrollLeft = _),
              (e.scrollTopPercent = o.scrollTop / o.scrollHeight),
              (e.scrollLeftPercent = o.scrollLeft / o.scrollWidth));
          }
        };
        function p(e, u) {
          return (
            e.settings.minScrollbarLength && (u = Math.max(u, e.settings.minScrollbarLength)),
            e.settings.maxScrollbarLength && (u = Math.min(u, e.settings.maxScrollbarLength)),
            u
          );
        }
        var B = {
            linear: function (e) {
              return e;
            },
            easeInQuad: function (e) {
              return e * e;
            },
            easeOutQuad: function (e) {
              return e * (2 - e);
            },
            easeInOutQuad: function (e) {
              return e < 0.5 ? 2 * e * e : (4 - 2 * e) * e - 1;
            },
            easeInCubic: function (e) {
              return e * e * e;
            },
            easeOutCubic: function (e) {
              return --e * e * e + 1;
            },
            easeInOutCubic: function (e) {
              return e < 0.5 ? 4 * e * e * e : (e - 1) * (2 * e - 2) * (2 * e - 2) + 1;
            },
            easeInQuart: function (e) {
              return e * e * e * e;
            },
            easeOutQuart: function (e) {
              return 1 - --e * e * e * e;
            },
            easeInOutQuart: function (e) {
              return e < 0.5 ? 8 * e * e * e * e : 1 - 8 * --e * e * e * e;
            },
            easeInQuint: function (e) {
              return e * e * e * e * e;
            },
            easeOutQuint: function (e) {
              return 1 + --e * e * e * e * e;
            },
            easeInOutQuint: function (e) {
              return e < 0.5 ? 16 * e * e * e * e * e : 1 + 16 * --e * e * e * e * e;
            },
          },
          w = function (e) {
            var u,
              t = e.percentTimeElapsed,
              n = e.x1,
              r = e.y1,
              o = e.x2,
              i = e.y2;
            return (
              1 -
              (n * ((u = t), Math.pow(u, 3)) +
                r *
                  (function (e) {
                    return 3 * e * e * (1 - e);
                  })(t) +
                o *
                  (function (e) {
                    return 3 * e * Math.pow(1 - e, 2);
                  })(t) +
                i *
                  (function (e) {
                    return Math.pow(1 - e, 3);
                  })(t))
            );
          },
          y = { breakBounds: !1, startBound: 0, endBound: 0 },
          L = function (e) {
            var u = e.scrollableDomEle,
              t = e.onAnimationCompleteCallback,
              n = e.direction,
              r = e.onRefUpdateCallback,
              o = e.duration,
              i = e.cubicBezierPoints,
              l = e.easingPreset,
              a = e.scrollAmount,
              s = e.onCheckForBreakCallback,
              c = e.boundsInfo;
            void 0 === c && (c = y);
            var d = null,
              _ = null,
              E = null,
              h = null,
              m = u === window,
              A = ["left", "right"].indexOf(n) > -1,
              b = ["right", "bottom"].indexOf(n) > -1;
            A
              ? ((_ = m ? "scrollX" : "scrollLeft"),
                (h = m ? "innerWidth" : "width"),
                (E = "scrollWidth"))
              : ((_ = m ? "scrollY" : "scrollTop"),
                (h = m ? "innerHeight" : "height"),
                (E = "scrollHeight"));
            var F = u[_],
              v = (function (e) {
                var u,
                  t = e.isWindow,
                  n = e.scrollableDomEle,
                  r = e.elementLengthProp,
                  o = e.initialScrollPosition,
                  i = e.isHorizontalDirection,
                  l = e.scrollLengthProp,
                  a = e.direction;
                if (t) {
                  var s = document.documentElement;
                  u = i ? s.offsetWidth : s.offsetHeight;
                } else u = (n[l] - n.getBoundingClientRect()[r]) | 0;
                return ["left", "top"].includes(a) ? o : u - o;
              })({
                isWindow: m,
                scrollableDomEle: u,
                elementLengthProp: h,
                initialScrollPosition: F,
                isHorizontalDirection: A,
                scrollLengthProp: E,
                direction: n,
              });
            !isNaN(a) && a < v && (v = a);
            var C = function e(n) {
              if (!s || !s()) {
                var a = n - d,
                  E = (function (e) {
                    var u = e.easingPreset,
                      t = e.cubicBezierPoints,
                      n = e.duration,
                      r = e.runTime / n;
                    if (B.hasOwnProperty(u)) return B[u](r);
                    if (
                      t &&
                      !isNaN(t.x1) &&
                      !isNaN(t.y1) &&
                      !isNaN(t.x2) &&
                      !isNaN(t.y2) &&
                      t.x1 >= 0 &&
                      t.x2 >= 0
                    )
                      return w({ percentTimeElapsed: r, x1: t.x1, x2: t.x2, y1: t.y1, y2: t.y2 });
                    throw new Error("Please enter a valid easing value");
                  })({ easingPreset: l, cubicBezierPoints: i, runTime: a, duration: o });
                if (!isNaN(E)) {
                  var h = Math.round(E * v),
                    C = b ? h + F : v - h;
                  if (
                    (c.breakBounds &&
                      (C < c.startBound ? (C = c.startBound) : C > c.endBound && (C = c.endBound)),
                    a < o)
                  ) {
                    if (m) {
                      var g = A ? C : 0,
                        D = A ? 0 : C;
                      window.scrollTo(g, D);
                    } else u[_] = C;
                    (r && r(C), requestAnimationFrame(e));
                  } else t && t();
                }
              }
            };
            requestAnimationFrame(function (e) {
              ((d = e), C(e));
            });
          },
          k = function (e) {
            var u = e.axis,
              t = e.cursorPositionOnRail,
              n = e.direction,
              r = e.i,
              o = (function (e) {
                var u = e.axis,
                  t = e.i,
                  n = e.cursorPositionOnRail;
                if ("y" === u) {
                  var r = t.scrollbarY.offsetTop,
                    o = r + t.scrollbarYHeight;
                  return n >= r && n <= o;
                }
                var i = t.scrollbarX.offsetLeft,
                  l = i + t.scrollbarXWidth;
                return n >= i && n <= l;
              })({ axis: u, i: r, cursorPositionOnRail: t });
            return o
              ? ((function (e) {
                  var u = e.axis,
                    t = e.i,
                    n = e.cursorPositionOnRail,
                    r = (function (e, u) {
                      if ("y" === e) {
                        var t = u.contentHeight - u.containerHeight;
                        return {
                          rail: u.railYHeight,
                          content: u.contentHeight,
                          scrollbar: u.scrollbarYHeight,
                          maxScroll: t,
                        };
                      }
                      var n = u.contentWidth - u.containerWidth;
                      return {
                        rail: u.railXWidth,
                        content: u.contentWidth,
                        scrollbar: u.scrollbarXWidth,
                        maxScroll: n,
                      };
                    })(u, t),
                    o = (n - r.scrollbar / 2) / r.rail,
                    i = Math.round(Math.min(r.maxScroll, Math.max(0, r.content * o)));
                  "y" === u ? (t.element.scrollTop = i) : (t.element.scrollLeft = i);
                })({ axis: u, i: r, cursorPositionOnRail: t }),
                !0)
              : ("y" === u
                  ? (r.element.scrollTop += n * r.containerHeight)
                  : (r.element.scrollLeft += n * r.containerWidth),
                !1);
          },
          S = function (e, u, t) {
            return function (n) {
              u = u.toLowerCase();
              var r = null,
                o = function () {
                  if (1 === n.buttons) {
                    if (
                      !n.target.closest(".ps__rail-" + u) ||
                      !n.target.closest(".ps__track_" + u)
                    ) {
                      var o = (function (e) {
                          var u = e.axis,
                            t = e.e,
                            n = e.i;
                          return "y" === u
                            ? {
                                cursorPosition: t.screenY,
                                windowScrolled: window.pageYOffset,
                                elementPosition: n.scrollbarYRail.getBoundingClientRect().top,
                              }
                            : {
                                cursorPosition: t.screenX,
                                windowScrolled: window.pageXOffset,
                                elementPosition: n.scrollbarXRail.getBoundingClientRect().left,
                              };
                        })({ axis: u, e: n, i: e }),
                        i = o.cursorPosition - o.windowScrolled - o.elementPosition,
                        l = (function (e) {
                          var u = e.axis,
                            t = e.cursorPositionOnRail,
                            n = e.i;
                          return t > ("y" === u ? n.scrollbarYTop : n.scrollbarXLeft) ? 1 : -1;
                        })({ axis: u, cursorPositionOnRail: i, i: e });
                      (k({ axis: u, cursorPositionOnRail: i, direction: l, i: e }) &&
                        clearTimeout(r),
                        f(e, !1, t));
                    }
                    n.stopPropagation();
                  }
                };
              (o(),
                (r = setInterval(o, 100)),
                e.event.once(e.ownerDocument, "mouseup", function () {
                  clearTimeout(r);
                }));
            };
          };
        function x(e, u, t) {
          var n = t[0],
            r = t[1],
            o = t[2],
            i = t[3],
            l = t[4],
            a = t[5],
            s = t[6],
            d = t[7],
            _ = t[8],
            m = e.element,
            A = null,
            b = null,
            v = null;
          function C(t) {
            ((m[s] = F(A + v * (t[o] - b))),
              E(e, d),
              f(e, !1, u),
              t.stopPropagation(),
              t.preventDefault());
          }
          function g() {
            (h(e, d),
              e[_].classList.remove(c.clicking),
              e.event.unbind(e.ownerDocument, "mousemove", C));
          }
          e.event.bind(e[l], "mousedown", function (u) {
            1 === u.buttons &&
              ((A = m[s]),
              (b = u[o]),
              (v = (e[r] - e[n]) / (e[i] - e[a])),
              e.event.bind(e.ownerDocument, "mousemove", C),
              e.event.once(e.ownerDocument, "mouseup", g),
              e[_].classList.add(c.clicking),
              u.stopPropagation(),
              u.preventDefault());
          });
        }
        var M = 1e3,
          R = {
            "click-rail": function (e, u) {
              (e.event.bind(e.scrollbarY, "mousedown", function (e) {
                return e.stopPropagation();
              }),
                e.event.bind(e.scrollbarYRail, "mousedown", S(e, "y", 0)),
                e.event.bind(e.scrollbarX, "mousedown", function (e) {
                  return e.stopPropagation();
                }),
                e.event.bind(e.scrollbarXRail, "mousedown", S(e, "x", u)));
            },
            "drag-thumb": function (e, u) {
              (x(e, u, [
                "containerWidth",
                "contentWidth",
                "screenX",
                "railXWidth",
                "scrollbarX",
                "scrollbarXWidth",
                "scrollLeft",
                "x",
                "scrollbarXRail",
              ]),
                x(e, u, [
                  "containerHeight",
                  "contentHeight",
                  "screenY",
                  "railYHeight",
                  "scrollbarY",
                  "scrollbarYHeight",
                  "scrollTop",
                  "y",
                  "scrollbarYRail",
                ]));
            },
            keyboard: function (e, u) {
              var t = e.element;
              e.event.bind(e.ownerDocument, "keydown", function (n) {
                if (
                  !((n.isDefaultPrevented && n.isDefaultPrevented()) || n.defaultPrevented) &&
                  o(t, ":hover")
                ) {
                  var r,
                    i = document.activeElement
                      ? document.activeElement
                      : e.ownerDocument.activeElement;
                  if (i) {
                    if ("IFRAME" === i.tagName) i = i.contentDocument.activeElement;
                    else for (; i.shadowRoot;) i = i.shadowRoot.activeElement;
                    if (
                      o((r = i), "input,[contenteditable]") ||
                      o(r, "select,[contenteditable]") ||
                      o(r, "textarea,[contenteditable]") ||
                      o(r, "button,[contenteditable]")
                    )
                      return;
                  }
                  var l = 0,
                    a = 0;
                  switch (n.which) {
                    case 37:
                      l = n.metaKey ? -e.contentWidth : n.altKey ? -e.containerWidth : -30;
                      break;
                    case 38:
                      a = n.metaKey ? e.contentHeight : n.altKey ? e.containerHeight : 30;
                      break;
                    case 39:
                      l = n.metaKey ? e.contentWidth : n.altKey ? e.containerWidth : 30;
                      break;
                    case 40:
                      a = n.metaKey ? -e.contentHeight : n.altKey ? -e.containerHeight : -30;
                      break;
                    case 32:
                      a = n.shiftKey ? e.containerHeight : -e.containerHeight;
                      break;
                    case 33:
                      a = e.containerHeight;
                      break;
                    case 34:
                      a = -e.containerHeight;
                      break;
                    case 36:
                      a = e.contentHeight;
                      break;
                    case 35:
                      a = -e.contentHeight;
                      break;
                    default:
                      return;
                  }
                  (e.settings.suppressScrollX && 0 !== l) ||
                    (e.settings.suppressScrollY && 0 !== a) ||
                    ((t.scrollTop -= a),
                    (t.scrollLeft += l),
                    f(e, !1, u),
                    (function (u, n) {
                      var r = Math.floor(t.scrollTop);
                      if (0 === u) {
                        if (!e.scrollbarYActive) return !1;
                        if (
                          (0 === r && n > 0) ||
                          (r >= e.contentHeight - e.containerHeight && n < 0)
                        )
                          return !e.settings.wheelPropagation;
                      }
                      var o = t.scrollLeft;
                      if (0 === n) {
                        if (!e.scrollbarXActive) return !1;
                        if ((0 === o && u < 0) || (o >= e.contentWidth - e.containerWidth && u > 0))
                          return !e.settings.wheelPropagation;
                      }
                      return !0;
                    })(l, a) && n.preventDefault());
                }
              });
            },
            wheel: function (e, t) {
              var n = e.element;
              function r(r) {
                var o = (function (e) {
                    var u = -1 * e.deltaX,
                      t = e.deltaY;
                    return (
                      (void 0 !== u && void 0 !== t) ||
                        ((u = (-1 * e.wheelDeltaX) / 6), (t = e.wheelDeltaY / 6)),
                      e.deltaMode && 1 === e.deltaMode && ((u *= 10), (t *= 10)),
                      u != u && t != t && ((u = 0), (t = e.wheelDelta)),
                      e.shiftKey ? [-t, -u] : [u, t]
                    );
                  })(r),
                  i = o[0],
                  l = o[1];
                if (
                  !(function (e, t, r) {
                    if (!v.isWebKit && n.querySelector("select")) return !0;
                    if (!n.contains(e)) return !1;
                    for (var o = e; o && o !== n;) {
                      if (o.classList.contains(s.consuming)) return !0;
                      var i = u(o);
                      if ([i.overflow, i.overflowX, i.overflowY].join("").match(/(scroll|auto)/)) {
                        var l = o.scrollHeight - o.clientHeight;
                        if (
                          l > 0 &&
                          !((0 === o.scrollTop && r > 0) || (o.scrollTop === l && r < 0))
                        )
                          return !0;
                        var a = o.scrollWidth - o.clientWidth;
                        if (
                          a > 0 &&
                          !((0 === o.scrollLeft && t < 0) || (o.scrollLeft === a && t > 0))
                        )
                          return !0;
                      }
                      o = o.parentNode;
                    }
                    return !1;
                  })(r.target, i, l)
                ) {
                  var a = !1,
                    c = (i * e.settings.wheelSpeed) | 0,
                    d = (l * e.settings.wheelSpeed) | 0;
                  (e.settings.useBothWheelAxes
                    ? e.scrollbarYActive && !e.scrollbarXActive
                      ? (l ? (n.scrollTop -= d) : (n.scrollTop += c), (a = !0))
                      : e.scrollbarXActive &&
                        !e.scrollbarYActive &&
                        (i ? (n.scrollLeft += c) : (n.scrollLeft -= d), (a = !0))
                    : ((n.scrollTop -= d), (n.scrollLeft += c)),
                    f(e, !1, t),
                    (a =
                      a ||
                      (function (u, t) {
                        var r = Math.floor(n.scrollTop),
                          o = 0 === n.scrollTop,
                          i = r + n.offsetHeight === n.scrollHeight,
                          l = 0 === n.scrollLeft,
                          a = n.scrollLeft + n.offsetWidth === n.scrollWidth;
                        return (
                          !(Math.abs(t) > Math.abs(u) ? o || i : l || a) ||
                          !e.settings.wheelPropagation
                        );
                      })(i, l)),
                    a && !r.ctrlKey && (r.stopPropagation(), r.preventDefault()));
                }
              }
              (e.event.bind(n, "wheel", r),
                void 0 !== window.onmousewheel && e.event.bind(n, "mousewheel", r));
            },
            touch: function (e, t) {
              if (v.supportsTouch || v.supportsIePointer) {
                var n = e.element,
                  r = {},
                  o = 0,
                  i = {},
                  l = null;
                v.supportsTouch
                  ? (e.event.bind(n, "touchstart", _),
                    e.event.bind(n, "touchmove", E),
                    e.event.bind(n, "touchend", h))
                  : v.supportsIePointer &&
                    (window.PointerEvent
                      ? (e.event.bind(n, "pointerdown", _),
                        e.event.bind(n, "pointermove", E),
                        e.event.bind(n, "pointerup", h))
                      : window.MSPointerEvent &&
                        (e.event.bind(n, "MSPointerDown", _),
                        e.event.bind(n, "MSPointerMove", E),
                        e.event.bind(n, "MSPointerUp", h)));
              }
              function a(u, r) {
                ((n.scrollTop -= r), (n.scrollLeft -= u), f(e, !1, t));
              }
              function c(e) {
                return e.targetTouches ? e.targetTouches[0] : e;
              }
              function d(e) {
                return (
                  (!e.pointerType || "pen" !== e.pointerType || 0 !== e.buttons) &&
                  (!(!e.targetTouches || 1 !== e.targetTouches.length) ||
                    !(
                      !e.pointerType ||
                      "mouse" === e.pointerType ||
                      e.pointerType === e.MSPOINTER_TYPE_MOUSE
                    ))
                );
              }
              function _(e) {
                if (d(e)) {
                  var u = c(e);
                  ((r.pageX = u.pageX),
                    (r.pageY = u.pageY),
                    (o = new Date().getTime()),
                    null !== l && clearInterval(l));
                }
              }
              function E(t) {
                if (d(t)) {
                  var l = c(t),
                    _ = { pageX: l.pageX, pageY: l.pageY },
                    E = _.pageX - r.pageX,
                    h = _.pageY - r.pageY;
                  if (
                    (function (e, t, r) {
                      if (!n.contains(e)) return !1;
                      for (var o = e; o && o !== n;) {
                        if (o.classList.contains(s.consuming)) return !0;
                        var i = u(o);
                        if (
                          [i.overflow, i.overflowX, i.overflowY].join("").match(/(scroll|auto)/)
                        ) {
                          var l = o.scrollHeight - o.clientHeight;
                          if (
                            l > 0 &&
                            !((0 === o.scrollTop && r > 0) || (o.scrollTop === l && r < 0))
                          )
                            return !0;
                          var a = o.scrollLeft - o.clientWidth;
                          if (
                            a > 0 &&
                            !((0 === o.scrollLeft && t < 0) || (o.scrollLeft === a && t > 0))
                          )
                            return !0;
                        }
                        o = o.parentNode;
                      }
                      return !1;
                    })(t.target, E, h)
                  )
                    return;
                  (a(E, h), (r = _));
                  var m = new Date().getTime(),
                    A = m - o;
                  (A > 0 && ((i.x = E / A), (i.y = h / A), (o = m)),
                    (function (u, t) {
                      var r = Math.floor(n.scrollTop),
                        o = n.scrollLeft,
                        i = Math.abs(u),
                        l = Math.abs(t);
                      if (l > i) {
                        if (
                          (t < 0 && r === e.contentHeight - e.containerHeight) ||
                          (t > 0 && 0 === r)
                        )
                          return 0 === window.scrollY && t > 0 && v.isChrome;
                      } else if (
                        i > l &&
                        ((u < 0 && o === e.contentWidth - e.containerWidth) || (u > 0 && 0 === o))
                      )
                        return !0;
                      return !0;
                    })(E, h) && t.preventDefault());
                }
              }
              function h() {
                e.settings.swipeEasing &&
                  (clearInterval(l),
                  (l = setInterval(function () {
                    e.isInitialized
                      ? clearInterval(l)
                      : i.x || i.y
                        ? Math.abs(i.x) < 0.01 && Math.abs(i.y) < 0.01
                          ? clearInterval(l)
                          : (a(30 * i.x, 30 * i.y), (i.x *= 0.8), (i.y *= 0.8))
                        : clearInterval(l);
                  }, 10)));
              }
            },
            "drag-move": function (e, u) {
              void 0 === u && (u = 0);
              var t = e.element,
                n = null,
                r = !1,
                o = 0,
                i = 0,
                l = 0;
              function a() {
                e.onScroll();
              }
              function s(n, r, o, i) {
                (void 0 === o && (o = null),
                  void 0 === i && (i = !1),
                  L({
                    scrollableDomEle: t,
                    direction: "right",
                    onRefUpdateCallback: a,
                    duration: r,
                    easingPreset: "easeOutCubic",
                    scrollAmount: n,
                    onCheckForBreakCallback: o,
                    boundsInfo: {
                      breakBounds: i,
                      startBound: u,
                      endBound: e.contentWidth - e.containerWidth + u,
                    },
                  }));
              }
              function d() {
                if (r) return r;
              }
              function _() {
                l = 0;
              }
              function m(r) {
                if (e.scrollbarXActive) {
                  var a = n - r.screenX;
                  ((t.scrollLeft += a), (n = r.screenX));
                  var s = new Date().getTime();
                  if (((o = (a / (s - i)) * 1e3), (i = s), e.onScroll(), u > 0)) {
                    var c = e.contentWidth - e.containerWidth + 2 * u;
                    0 === t.scrollLeft || t.scrollLeft === c
                      ? 0 === l && (l = window.setTimeout(_, 250))
                      : 0 !== l && (window.clearTimeout(l), (l = 0));
                  }
                  (E(e, "x"),
                    E(e, "dragging", { immediately: !0 }),
                    r.stopPropagation(),
                    r.preventDefault());
                }
              }
              function A(e) {
                ((n = e.screenX),
                  (r = !0),
                  requestAnimationFrame(function () {
                    r = !1;
                  }),
                  (i = new Date().getTime()));
              }
              function b(n) {
                var r = e.contentWidth - e.containerWidth + u;
                if (t.scrollLeft < u) s(u - t.scrollLeft, M, d);
                else if (t.scrollLeft > r) s(r - t.scrollLeft, M, d);
                else {
                  new Date().getTime() - i < 100 && s(o / 4, M, d, !0);
                }
                (h(e, "x"),
                  h(e, "dragging", { immediately: !0 }),
                  e.scrollbarXRail.classList.remove(c.clicking),
                  e.event.unbind(e.ownerDocument, "mousemove", m));
              }
              function F() {
                r = !0;
              }
              t.addEventListener(
                "mousedown",
                function (u) {
                  1 === u.buttons &&
                    ((n = u.screenX),
                    e.event.bind(e.ownerDocument, "mousemove", m),
                    e.event.once(e.ownerDocument, "mouseup", b),
                    e.event.once(e.ownerDocument, "mousedown", A),
                    e.event.once(t, "wheel", F),
                    e.scrollbarXRail.classList.add(c.clicking),
                    u.preventDefault());
                },
                !1,
              );
            },
          },
          T = function (e, r) {
            var o = this;
            if (
              (void 0 === r && (r = {}),
              "string" == typeof e && (e = document.querySelector(e)),
              !e || !e.nodeName)
            )
              throw new Error("no element is specified to initialize PerfectScrollbar");
            for (var i in ((this.element = e),
            e.classList.add(a),
            (this.settings = {
              handlers: ["click-rail", "drag-thumb", "keyboard", "wheel", "touch", "drag-move"],
              maxScrollbarLength: null,
              minScrollbarLength: null,
              scrollingThreshold: 1e3,
              scrollXMarginOffset: 0,
              scrollYMarginOffset: 0,
              suppressScrollX: !1,
              suppressScrollY: !1,
              swipeEasing: !0,
              useBothWheelAxes: !1,
              wheelPropagation: !0,
              wheelSpeed: 10,
              enableHorizontalScroll: !1,
              animationDuration: 1e3,
              animationEasingPreset: "easeInOutQuint",
              isDisableScrollToLastPositionOnResize: !1,
              overScrollWidth: 0,
            }),
            r))
              o.settings[i] = r[i];
            ((this.containerWidth = null),
              (this.containerHeight = null),
              (this.contentWidth = null),
              (this.contentHeight = null));
            var l,
              d,
              _ = function () {
                return e.classList.add(c.focus);
              },
              E = function () {
                return e.classList.remove(c.focus);
              };
            ((this.isRtl = "rtl" === u(e).direction),
              (this.isNegativeScroll =
                ((d = e.scrollLeft),
                (e.scrollLeft = -1),
                (l = e.scrollLeft < 0),
                (e.scrollLeft = d),
                l)),
              (this.negativeScrollAdjustment = this.isNegativeScroll
                ? e.scrollWidth - e.clientWidth
                : 0),
              (this.event = new b()),
              (this.ownerDocument = e.ownerDocument || document),
              (this.scrollbarXRail = n(s.rail("x"))),
              (this.scrollbarXButtonStart = n(s.buttonStart("x"))),
              (this.scrollbarXButtonEnd = n(s.buttonEnd("x"))),
              (this.scrollbarXTrack = n(s.track("x"))),
              e.appendChild(this.scrollbarXRail),
              this.scrollbarXRail.appendChild(this.scrollbarXTrack),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonStart),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonEnd),
              (this.scrollbarX = n(s.thumb("x"))),
              this.scrollbarXRail.appendChild(this.scrollbarX),
              this.scrollbarX.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarX, "focus", _),
              this.event.bind(this.scrollbarX, "blur", E),
              (this.scrollbarXActive = null),
              (this.scrollbarXWidth = null),
              (this.scrollbarXLeft = null),
              (this.scrollbarYRail = n(s.rail("y"))),
              (this.scrollbarYButtonStart = n(s.buttonStart("y"))),
              (this.scrollbarYButtonEnd = n(s.buttonEnd("y"))),
              (this.scrollbarYTrack = n(s.track("y"))),
              e.appendChild(this.scrollbarYRail),
              this.scrollbarYRail.appendChild(this.scrollbarYTrack),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonStart),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonEnd),
              (this.scrollbarY = n(s.thumb("y"))),
              this.scrollbarYRail.appendChild(this.scrollbarY),
              this.scrollbarY.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarY, "focus", _),
              this.event.bind(this.scrollbarY, "blur", E),
              (this.scrollbarYActive = null),
              (this.scrollbarYHeight = null),
              (this.scrollbarYTop = null),
              C().then(function () {
                var n = u(o.scrollbarXRail);
                ((o.scrollbarXBottom = parseInt(n.bottom, 10)),
                  isNaN(o.scrollbarXBottom)
                    ? ((o.isScrollbarXUsingBottom = !1), (o.scrollbarXTop = F(n.top)))
                    : (o.isScrollbarXUsingBottom = !0),
                  (o.railBorderXWidth = F(n.borderLeftWidth) + F(n.borderRightWidth)),
                  t(o.scrollbarXRail, { display: "block" }),
                  (o.railXMarginWidth = F(n.marginLeft) + F(n.marginRight)),
                  t(o.scrollbarXRail, { display: "" }),
                  (o.railXWidth = null),
                  (o.railXRatio = null));
                var r = u(o.scrollbarYRail);
                ((o.scrollbarYRight = parseInt(r.right, 10)),
                  isNaN(o.scrollbarYRight)
                    ? ((o.isScrollbarYUsingRight = !1), (o.scrollbarYLeft = F(r.left)))
                    : (o.isScrollbarYUsingRight = !0),
                  (o.scrollbarYOuterWidth = o.isRtl
                    ? (function (e) {
                        var t = u(e);
                        return (
                          F(t.width) +
                          F(t.paddingLeft) +
                          F(t.paddingRight) +
                          F(t.borderLeftWidth) +
                          F(t.borderRightWidth)
                        );
                      })(o.scrollbarY)
                    : null),
                  (o.railBorderYWidth = F(r.borderTopWidth) + F(r.borderBottomWidth)),
                  t(o.scrollbarYRail, { display: "block" }),
                  (o.railYMarginHeight = F(r.marginTop) + F(r.marginBottom)),
                  t(o.scrollbarXRail, { display: "" }),
                  t(o.scrollbarYRail, { display: "" }),
                  (o.railYHeight = null),
                  (o.railYRatio = null),
                  (o.reach = {
                    x:
                      e.scrollLeft <= 0
                        ? "start"
                        : e.scrollLeft >= o.contentWidth - o.containerWidth
                          ? "end"
                          : null,
                    y:
                      e.scrollTop <= 0
                        ? "start"
                        : e.scrollTop >= o.contentHeight - o.containerHeight
                          ? "end"
                          : null,
                  }),
                  (o.isAlive = !0),
                  o.settings.handlers.forEach(function (e) {
                    return R[e](o, o.settings.overScrollWidth);
                  }),
                  (o.boundHandleButtonEnter = o.handleMouseEnter.bind(o)),
                  (o.boundHandleMouseLeave = o.handleMouseLeave.bind(o)),
                  (o.boundHandleMouseEnter = o.handleMouseEnter.bind(o)),
                  (o.boundPlayClickSound = o.playClickSound.bind(o)),
                  o.scrollbarYButtonStart.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarYButtonEnd.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarXButtonStart.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarXButtonEnd.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarXButtonStart.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarXButtonEnd.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarYButtonStart.addEventListener("mouseenter", o.boundHandleButtonEnter),
                  o.scrollbarYButtonEnd.addEventListener("mouseenter", o.boundHandleButtonEnter),
                  o.scrollbarYButtonStart.addEventListener("mouseleave", o.boundHandleMouseLeave),
                  o.scrollbarYButtonEnd.addEventListener("mouseleave", o.boundHandleMouseLeave),
                  o.scrollbarY.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarX.addEventListener("mouseenter", o.boundHandleMouseEnter),
                  o.scrollbarY.addEventListener("mouseleave", o.boundHandleMouseLeave),
                  o.scrollbarY.addEventListener("mousedown", o.boundPlayClickSound),
                  o.scrollbarX.addEventListener("mousedown", o.boundPlayClickSound),
                  (o.lastScrollTop = Math.floor(e.scrollTop)),
                  (o.lastScrollLeft = e.scrollLeft),
                  (o.scrollTopPercent = e.scrollTop / e.scrollHeight),
                  (o.scrollLeftPercent = e.scrollLeft / e.scrollWidth),
                  o.event.bind(o.element, "scroll", function (e) {
                    return o.onScroll(e);
                  }),
                  o.settings.enableHorizontalScroll &&
                    o.event.bind(o.element, "wheel", function (e) {
                      return o.onWheel(e);
                    }),
                  f(o, !1, o.settings.overScrollWidth, !1));
              }));
          };
        ((T.prototype._getAnimationSettings = function (e, u, t, n) {
          var r = this,
            o = 0;
          return (
            null !== this.element &&
              (o = ["bottom", "top"].includes(u)
                ? this.element.scrollTop
                : this.element.scrollLeft),
            {
              scrollableDomEle: this.element,
              duration: this.settings.animationDuration,
              easingPreset: this.settings.animationEasingPreset,
              scrollAmount: e - o,
              direction: u,
              onRefUpdateCallback: function (e) {
                (f(r, !0, r.settings.overScrollWidth, !1), t && t(e));
              },
              onAnimationCompleteCallback: function () {
                n && n();
              },
            }
          );
        }),
          (T.prototype.playHoverSound = function () {
            window.engine && engine.call("PlaySound", "highlight");
          }),
          (T.prototype.playClickSound = function () {
            window.engine && engine.call("PlaySound", "play");
          }),
          (T.prototype.handleMouseEnter = function () {
            this.playHoverSound();
          }),
          (T.prototype.handleMouseLeave = function () {}),
          (T.prototype.update = function () {
            var e = this;
            this.isAlive &&
              ((this.negativeScrollAdjustment = this.isNegativeScroll
                ? this.element.scrollWidth - this.element.clientWidth
                : 0),
              t(this.scrollbarXRail, { display: "block" }),
              t(this.scrollbarYRail, { display: "block" }),
              (this.railXMarginWidth =
                F(u(this.scrollbarXRail).marginLeft) + F(u(this.scrollbarXRail).marginRight)),
              (this.railYMarginHeight =
                F(u(this.scrollbarYRail).marginTop) + F(u(this.scrollbarYRail).marginBottom)),
              t(this.scrollbarXRail, { display: "none" }),
              t(this.scrollbarYRail, { display: "none" }),
              C().then(function () {
                (e.settings.isDisableScrollToLastPositionOnResize ||
                  ((e.element.scrollTop = e.element.scrollHeight * e.scrollTopPercent),
                  (e.element.scrollLeft = e.element.scrollWidth * e.scrollLeftPercent)),
                  f(e, !1, e.settings.overScrollWidth, !1),
                  D(e, "top", 0, !1, !1, !0),
                  D(e, "left", 0, !1, !1, !0),
                  t(e.scrollbarXRail, { display: "" }),
                  t(e.scrollbarYRail, { display: "" }));
              }));
          }),
          (T.prototype.setScrollLeft = function (e, u, t) {
            L(this._getAnimationSettings(e, "right", u, t));
          }),
          (T.prototype.setScrollLeftImmediately = function (e) {
            ((this.element.scrollLeft = 0 | e), this.update());
          }),
          (T.prototype.setScrollTop = function (e, u, t) {
            L(this._getAnimationSettings(e, "bottom", u, t));
          }),
          (T.prototype.setScrollTopImmediately = function (e) {
            ((this.element.scrollTop = 0 | e), this.update());
          }),
          (T.prototype.onScroll = function (e) {
            this.isAlive && f(this, !1, this.settings.overScrollWidth, !0);
          }),
          (T.prototype.onWheel = function (e) {
            this.isAlive &&
              (f(this, !1, this.settings.overScrollWidth, !1),
              D(this, "left", this.element.scrollLeft - this.lastScrollLeft),
              (this.lastScrollLeft = this.element.scrollLeft));
          }),
          (T.prototype.destroy = function () {
            this.isAlive &&
              (this.scrollbarYButtonStart.removeEventListener(
                "mousedown",
                this.boundPlayClickSound,
              ),
              this.scrollbarYButtonEnd.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarXButtonStart.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarXButtonEnd.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarXButtonStart.removeEventListener(
                "mouseenter",
                this.boundHandleMouseEnter,
              ),
              this.scrollbarXButtonEnd.removeEventListener(
                "mouseenter",
                this.boundHandleMouseEnter,
              ),
              this.scrollbarYButtonStart.removeEventListener(
                "mouseenter",
                this.boundHandleButtonEnter,
              ),
              this.scrollbarYButtonEnd.removeEventListener(
                "mouseenter",
                this.boundHandleButtonEnter,
              ),
              this.scrollbarYButtonStart.removeEventListener(
                "mouseleave",
                this.boundHandleMouseLeave,
              ),
              this.scrollbarYButtonEnd.removeEventListener(
                "mouseleave",
                this.boundHandleMouseLeave,
              ),
              this.scrollbarY.removeEventListener("mouseenter", this.boundHandleMouseEnter),
              this.scrollbarX.removeEventListener("mouseenter", this.boundHandleMouseEnter),
              this.scrollbarY.removeEventListener("mouseleave", this.boundHandleMouseLeave),
              this.scrollbarY.removeEventListener("mousedown", this.boundPlayClickSound),
              this.scrollbarX.removeEventListener("mousedown", this.boundPlayClickSound),
              this.event.unbindAll(),
              i(this.scrollbarX),
              i(this.scrollbarY),
              i(this.scrollbarXRail),
              i(this.scrollbarYRail),
              this.removePsClasses(),
              (this.element = null),
              (this.scrollbarX = null),
              (this.scrollbarY = null),
              (this.scrollbarXRail = null),
              (this.scrollbarYRail = null),
              (this.isAlive = !1));
          }),
          (T.prototype.removePsClasses = function () {
            this.element.className = this.element.className
              .split(" ")
              .filter(function (e) {
                return !e.match(/^ps([-_].+|)$/);
              })
              .join(" ");
          }),
          (e.exports = T));
      },
      7078: (e, u, t) => {
        t.d(u, { t: () => a });
        var n = t(6179),
          r = t.n(n),
          o = t(2056);
        const i = ["children"];
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
        const a = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                o = Object.keys(e);
              for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, i);
          return r().createElement(
            o.u,
            l(
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
        t.d(u, { l: () => s });
        var n = t(6179),
          r = t.n(n),
          o = t(7078),
          i = t(6373),
          l = t(2056);
        function a() {
          return (
            (a =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            a.apply(this, arguments)
          );
        }
        const s = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const n = r().createElement("div", { className: t }, e);
          if (u.header || u.body) return r().createElement(i.i, u, n);
          const s = u.contentId,
            c = u.args,
            d = null == c ? void 0 : c.contentId;
          return s || d
            ? r().createElement(l.u, a({}, u, { contentId: s || d }), n)
            : r().createElement(o.t, u, n);
        };
      },
      6373: (e, u, t) => {
        t.d(u, { i: () => s });
        var n = t(2056),
          r = t(6179),
          o = t.n(r);
        const i = ["children", "body", "header", "note", "alert", "args"];
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
        const a = R.views.common.tooltip_window.simple_tooltip_content,
          s = (e) => {
            let u = e.children,
              t = e.body,
              s = e.header,
              c = e.note,
              d = e.alert,
              _ = e.args,
              E = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, i);
            const h = (0, r.useMemo)(() => {
              const e = Object.assign({}, _, { body: t, header: s, note: c, alert: d });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [d, t, s, c, _]);
            return o().createElement(
              n.u,
              l(
                {
                  contentId:
                    ((m = null == _ ? void 0 : _.hasHtmlContent),
                    m ? a.SimpleTooltipHtmlContent("resId") : a.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: h,
                },
                E,
              ),
              u,
            );
            var m;
          };
      },
      2056: (e, u, t) => {
        t.d(u, { u: () => s });
        var n = t(7902),
          r = t(4179),
          o = t(6179);
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
        function l(e) {
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
        const a = (e, u, t = {}, n = 0) => {
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
          s = (e) => {
            let u = e.children,
              t = e.contentId,
              r = e.args,
              s = e.onMouseEnter,
              c = e.onMouseLeave,
              d = e.onMouseDown,
              _ = e.onClick,
              E = e.ignoreShowDelay,
              h = void 0 !== E && E,
              m = e.ignoreMouseClick,
              A = void 0 !== m && m,
              b = e.decoratorId,
              F = void 0 === b ? 0 : b,
              v = e.isEnabled,
              C = void 0 === v || v,
              g = e.targetId,
              D = void 0 === g ? 0 : g,
              f = e.onShow,
              p = e.onHide,
              B = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, i);
            const w = (0, o.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              y = (0, o.useMemo)(() => D || (0, n.F)().resId, [D]),
              L = (0, o.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (a(t, F, { isMouseEvent: !0, on: !0, arguments: l(r) }, y),
                  f && f(),
                  (w.current.isVisible = !0));
              }, [t, F, r, y, f]),
              k = (0, o.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    a(t, F, { on: !1 }, y),
                    w.current.isVisible && p && p(),
                    (w.current.isVisible = !1));
                }
              }, [t, F, y, p]),
              S = (0, o.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(w.current.prevTarget) && k();
                  }, 200)));
              }, []);
            ((0, o.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", S, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", S, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, o.useEffect)(() => {
                !1 === C && k();
              }, [C, k]),
              (0, o.useEffect)(
                () => (
                  window.addEventListener("mouseleave", k),
                  () => {
                    (window.removeEventListener("mouseleave", k), k());
                  }
                ),
                [k],
              ));
            return C
              ? (0, o.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(L, h ? 100 : 400)),
                            s && s(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (k(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === A && k(), null == _ || _(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === A && k(), null == d || d(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    B,
                  ),
                )
              : u;
            var x;
          };
      },
      1856: (e, u, t) => {
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
      7044: (e, u, t) => {
        (t(3649), t(728), t(4179));
        Date.now();
      },
      527: (e, u, t) => {
        (t.r(u), t.d(u, { mouse: () => l, onResize: () => o }));
        var n = t(2472),
          r = t(1176);
        const o = (0, n.E)("clientResized"),
          i = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const l = (function () {
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
          const o = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const o = `mouse${u}`,
                    l = i[u]((e) => t([e, "outside"]));
                  function a(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(o, a),
                    n(),
                    () => {
                      r &&
                        (l(), window.removeEventListener(o, a), (e.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, o, {
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
        (t.r(u),
          t.d(u, {
            events: () => n,
            getMouseGlobalPosition: () => o,
            getSize: () => r,
            graphicsQuality: () => i,
          }));
        var n = t(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function o(e = "px") {
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
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => n });
      },
      2472: (e, u, t) => {
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
        t.d(u, { O: () => r });
        var n = t(5959);
        const r = { view: t(7641), client: n };
      },
      3722: (e, u, t) => {
        function n(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function r(e, u, t) {
          return `url(${n(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => r, getTextureUrl: () => n }));
      },
      6112: (e, u, t) => {
        t.d(u, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
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
        (t.r(u),
          t.d(u, {
            addModelObserver: () => c,
            addPreloadTexture: () => l,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => o.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => p,
            freezeTextureBeforeResize: () => m,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => B,
            getScale: () => A,
            getSize: () => _,
            getViewGlobalPosition: () => h,
            isClientAccessible: () => g,
            isEventHandled: () => f,
            isFocused: () => C,
            pxToRem: () => b,
            remToPx: () => F,
            resize: () => E,
            sendEvent: () => i.qP,
            setAnimateWindow: () => v,
            setEventHandled: () => D,
            setInputPaddingsRem: () => a,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => L,
          }));
        var n = t(3722),
          r = t(6112),
          o = t(6538),
          i = t(8566);
        function l(e) {
          viewEnv.addPreloadTexture(e);
        }
        function a(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function s(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function c(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function _(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function E(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function h(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: F(u.x), y: F(u.y) };
        }
        function m() {
          viewEnv.freezeTextureBeforeResize();
        }
        function A() {
          return viewEnv.getScale();
        }
        function b(e) {
          return viewEnv.pxToRem(e);
        }
        function F(e) {
          return viewEnv.remToPx(e);
        }
        function v(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function g() {
          return viewEnv.isClientAccessible();
        }
        function D() {
          return viewEnv.setEventHandled();
        }
        function f() {
          return viewEnv.isEventHandled();
        }
        function p() {
          viewEnv.forceTriggerMouseMove();
        }
        function B() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(r.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === r.W[u]), e),
            {},
          ),
          y = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          L = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : o.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, u, t) => {
        t.d(u, { qP: () => s });
        const n = ["args"];
        const r = 2,
          o = 16,
          i = 32,
          l = 64,
          a = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const o = u.args,
                i = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    o = Object.keys(e);
                  for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, n);
              return void 0 !== o
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, i, {
                      arguments:
                        ((r = o),
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
          s = {
            close(e) {
              a("popover" === e ? r : i);
            },
            minimize() {
              a(l);
            },
            move(e) {
              a(o, { isMouseEvent: !0, on: e });
            },
          };
      },
      7902: (e, u, t) => {
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
      8071: (e, u, t) => {
        t.d(u, { M: () => n });
        const n = (e, u) => e.split(".").reduce((e, u) => e && e[u], u);
      },
      2344: (e, u, t) => {
        t.d(u, { D9: () => r });
        var n = t(2790);
        (t(3469), t(2133), t(579), t(5360), t(9056));
        const r = n.Z;
      },
      6536: (e, u, t) => {
        t.d(u, { Z: () => r });
        var n = t(6179);
        const r = (e) => {
          const u = (0, n.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      3469: (e, u, t) => {
        (t(7044), t(6179));
      },
      2133: (e, u, t) => {
        t(6179);
      },
      8526: (e, u, t) => {
        t.d(u, { gd: () => l });
        var n = t(3138),
          r = t(5521),
          o = (t(4179), t(6179));
        const i = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function l(e = r.n.NONE, u = i, t = !1) {
          (0, o.useEffect)(() => {
            if (e !== r.n.NONE)
              return (
                window.addEventListener("keydown", o, t),
                () => {
                  window.removeEventListener("keydown", o, t);
                }
              );
            function o(r) {
              if (r.keyCode === e) {
                if (n.O.view.isEventHandled()) return;
                (n.O.view.setEventHandled(), u(r), t && r.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
      },
      5360: (e, u, t) => {
        t(6536);
        var n = t(4179);
        t(6179);
        n.Sw.instance;
        let r;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(r || (r = {}));
      },
      9056: (e, u, t) => {
        t.d(u, { m: () => a });
        var n = t(7902),
          r = t(8071),
          o = t(4179),
          i = t(6179);
        const l = o.Sw.instance,
          a = (e = "model", u = !0) => {
            const t = (0, i.useState)(0),
              o = (t[0], t[1]),
              a = (0, i.useMemo)(() => (0, n.F)(), []),
              s = a.caller,
              c = a.resId,
              d = (0, i.useMemo)(
                () => (window.__feature && window.__feature !== s ? `children.${s}.${e}` : e),
                [s, e],
              ),
              _ = (0, i.useMemo)(
                () =>
                  ((e) => {
                    const u = (0, r.M)(e, window);
                    for (const e in u) "function" == typeof u[e] && (u[e] = u[e].bind(u));
                    return u;
                  })(d),
                [d],
              );
            return (
              (0, i.useEffect)(() => {
                if (u) {
                  const u = () => {
                      o((e) => e + 1);
                    },
                    t = l.addCallback(e, u, c);
                  return () => l.removeCallback(t, c);
                }
              }, [e, u, c]),
              _
            );
          };
      },
      2790: (e, u, t) => {
        t.d(u, { Z: () => r });
        var n = t(6179);
        const r = (e) => {
          const u = (0, n.useRef)();
          return (
            (0, n.useEffect)(() => {
              u.current = e;
            }, [e]),
            u.current
          );
        };
      },
      579: (e, u, t) => {
        (t(3138), t(6179));
      },
      1091: (e, u, t) => {
        t.d(u, { Z: () => o });
        var n = t(6179);
        const r = (e) => {
            if (!e) return !1;
            const u = e.getBoundingClientRect(),
              t = u.width,
              n = u.height;
            return 0 !== t && 0 !== n;
          },
          o = (e) => {
            const u = (0, n.useState)(r(e ? e.current : null)),
              t = u[0],
              o = u[1];
            return (
              (0, n.useEffect)(() => {
                let u = 0;
                const t = () => {
                  u = requestAnimationFrame(() => {
                    r(e ? e.current : null) ? o(!0) : t();
                  });
                };
                return (
                  t(),
                  () => {
                    cancelAnimationFrame(u);
                  }
                );
              }, [e]),
              (0, n.useEffect)(() => () => o(!1), [e]),
              t
            );
          };
      },
      5521: (e, u, t) => {
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
      1641: (e, u, t) => {
        let n;
        (t.d(u, { t: () => n }),
          (function (e) {
            ((e[(e.LEFT = 0)] = "LEFT"),
              (e[(e.WHEEL = 1)] = "WHEEL"),
              (e[(e.RIGHT = 2)] = "RIGHT"),
              (e[(e.FOURTH = 3)] = "FOURTH"),
              (e[(e.FIFTH = 4)] = "FIFTH"));
          })(n || (n = {})));
      },
      7727: (e, u, t) => {
        function n(e) {
          engine.call("PlaySound", e);
        }
        t.d(u, { G: () => n });
      },
      3649: (e, u, t) => {
        let n;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(n || (n = {}));
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
      },
      728: (e, u, t) => {
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
      },
      1358: (e, u, t) => {
        t.d(u, { Z: () => o });
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
            const o = n.O.view.addModelObserver(e, t, r);
            return (
              o > 0
                ? ((this._callbacks[o] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(o) : (this._views[t] = [o])))
                : console.error("Can't add callback for model:", e),
              o
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
        const o = r;
      },
      7572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
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
        t.d(u, { c1: () => f, Sw: () => o.Z, B3: () => s, Z5: () => i, B0: () => a, ry: () => F });
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
        var o = t(1358);
        const i = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          l = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
          };
        let a;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(a || (a = {}));
        const s = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = t(5521),
          h = t(3138);
        const m = ["args"];
        function A(e, u, t, n, r, o, i) {
          try {
            var l = e[o](i),
              a = l.value;
          } catch (e) {
            return void t(e);
          }
          l.done ? u(a) : Promise.resolve(a).then(n, r);
        }
        const b = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          F = (function () {
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
                    var o = e.apply(u, t);
                    function i(e) {
                      A(o, n, r, i, l, "next", e);
                    }
                    function l(e) {
                      A(o, n, r, i, l, "throw", e);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          v = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                o = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    o = Object.keys(e);
                  for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, m);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, o, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, o));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          C = () => v(a.CLOSE),
          g = (e, u) => {
            e.keyCode === E.n.ESCAPE && u();
          };
        var D = t(7572);
        const f = r.instance,
          p = {
            DataTracker: o.Z,
            ViewModel: D.Z,
            ViewEventType: a,
            NumberFormatType: s,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: _,
            makeGlobalBoundingBox: b,
            sendMoveEvent: (e) => v(a.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => v(a.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              v(a.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, r = R.invalid("resId"), o) => {
              const i = h.O.view.getViewGlobalPosition(),
                l = t.getBoundingClientRect(),
                s = l.x,
                c = l.y,
                d = l.width,
                _ = l.height,
                E = {
                  x: h.O.view.pxToRem(s) + i.x,
                  y: h.O.view.pxToRem(c) + i.y,
                  width: h.O.view.pxToRem(d),
                  height: h.O.view.pxToRem(_),
                };
              v(a.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: b(E),
                on: !0,
                args: o,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => g(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              g(e, C);
            },
            handleViewEvent: v,
            onBindingsReady: F,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(a.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(a.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(a.POP_OVER),
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
            ClickOutsideManager: f,
            SystemLocale: i,
            UserLocale: l,
          };
        window.ViewEnvHelper = p;
      },
      1922: (e, u, t) => {
        (t(6483), t(7739), t(6179), t(1960));
        let n;
        !(function (e) {
          ((e.None = ""),
            (e.Tiny = "tiny"),
            (e.Small = "small"),
            (e.Medium = "medium"),
            (e.Large = "large"),
            (e.Huge = "huge"));
        })(n || (n = {}));
      },
      9220: (e, u, t) => {
        t.d(u, { v: () => N });
        var n = t(6483),
          r = t.n(n),
          o = t(3415),
          i = t(1856),
          l = t(8526),
          a = t(6179),
          s = t.n(a);
        var c = t(5521),
          d = t(4179);
        let _, E;
        (!(function (e) {
          ((e.Basic = "basic"),
            (e.Disabled = "disabled"),
            (e.Focused = "focused"),
            (e.Alert = "alert"),
            (e.Selected = "selected"));
        })(_ || (_ = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"));
          })(E || (E = {})));
        var h = t(6373);
        const m = "TextOverflow_base_3b",
          A = ({ content: e, classMix: u }) => {
            const t = (0, a.useRef)(null),
              n = (0, a.useState)(!0),
              o = n[0],
              l = n[1];
            return (
              (0, a.useEffect)(() =>
                (0, i.v)(() => {
                  const e = t.current;
                  e && e.offsetWidth >= e.scrollWidth && l(!1);
                }),
              ),
              s().createElement(
                h.i,
                { isEnabled: o, body: e },
                s().createElement("div", { ref: t, className: r()(m, u) }, e),
              )
            );
          };
        var b = t(7727);
        const F = {
          base: "DropDownControl_base_46",
          base__small: "DropDownControl_base__small_22",
          base__medium: "DropDownControl_base__medium_09",
          base__over: "DropDownControl_base__over_e7",
          base__down: "DropDownControl_base__down_1c",
          base__open: "DropDownControl_base__open_e3",
          base__focused: "DropDownControl_base__focused_63",
          base__selected: "DropDownControl_base__selected_46",
          base__disabled: "DropDownControl_base__disabled_37",
          label: "DropDownControl_label_12",
          label__small: "DropDownControl_label__small_e7",
          label__medium: "DropDownControl_label__medium_0b",
          label__placeholder: "DropDownControl_label__placeholder_98",
          button: "DropDownControl_button_cb",
          button__small: "DropDownControl_button__small_b5",
          button__medium: "DropDownControl_button__medium_14",
          gradient: "DropDownControl_gradient_b5",
          disabled: "DropDownControl_disabled_4e",
          arrow: "DropDownControl_arrow_de",
          arrow__small: "DropDownControl_arrow__small_77",
          arrow__medium: "DropDownControl_arrow__medium_3d",
          alert: "DropDownControl_alert_75",
          blink: "DropDownControl_blink_68",
        };
        let v;
        !(function (e) {
          ((e.Out = "out"), (e.Over = "over"), (e.Down = "down"));
        })(v || (v = {}));
        const C = (0, a.memo)(
          ({
            parentId: e,
            variant: u = _.Basic,
            size: t = E.Medium,
            isOpen: n,
            placeholder: o = R.strings.common.dropdown.placeholder.select(),
            label: i = "",
            classMix: l,
            onClick: c,
            soundHover: d,
            soundClick: h,
            customControl: m,
          }) => {
            const C = (0, a.useState)(v.Out),
              g = C[0],
              D = C[1],
              f = (0, a.useState)(!1),
              p = f[0],
              B = f[1],
              w = u === _.Disabled,
              y = w || u === _.Basic,
              L = (0, a.useCallback)(() => {
                w || (D(v.Over), d && (0, b.G)(d));
              }, [w, d]),
              k = (0, a.useCallback)(() => {
                w || (D(v.Down), h && (0, b.G)(h));
              }, [w, h]),
              S = (0, a.useCallback)(() => {
                (!w && D(v.Over), !y && B(!0));
              }, [w, y]),
              x = (0, a.useCallback)((e) => c && c(e), [c]),
              M = (0, a.useCallback)(() => D(v.Out), []);
            ((0, a.useEffect)(() => {
              y || B(!1);
            }, [u, y]),
              (0, a.useEffect)(() => {
                w && M();
              }, [w, M]));
            const T = r()(
              F.base,
              n && F.base__open,
              F[`base__${g}`],
              (y || !p) && F[`base__${u}`],
              l,
            );
            return s().createElement(
              "div",
              {
                id: e ? `${e}_control` : void 0,
                className: T,
                onMouseEnter: L,
                onMouseUp: S,
                onMouseDown: k,
                onMouseLeave: M,
                onClick: x,
              },
              !p && u === _.Alert && s().createElement("div", { className: F.alert }),
              s().createElement(
                "div",
                { className: r()(F.label, F[`label__${t}`], !i && F.label__placeholder) },
                m || s().createElement(A, { content: i || o }),
              ),
              s().createElement(
                "div",
                { className: r()(F.button, F[`button__${t}`]) },
                s().createElement("div", { className: r()(F.arrow, F[`arrow__${t}`]) }),
                g === v.Over && s().createElement("div", { className: F.gradient }),
                w && s().createElement("div", { className: F.disabled }),
              ),
            );
          },
        );
        var g = t(2344);
        var D = t(570);
        const f = [
          "children",
          "isEnabled",
          "selectedItemId",
          "scrollAreaKey",
          "withCompleteTrigger",
          "containerClasses",
        ];
        function p() {
          return (
            (p =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            p.apply(this, arguments)
          );
        }
        const B = (e) => {
            let u = e.children,
              t = e.isEnabled,
              n = void 0 === t || t,
              r = e.selectedItemId,
              o = e.scrollAreaKey,
              l = void 0 === o ? "scrollArea" : o,
              c = e.withCompleteTrigger,
              d = void 0 !== c && c,
              _ = e.containerClasses,
              E = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, f);
            const h = (0, a.useState)(!1),
              m = h[0],
              A = h[1],
              b = (0, a.useRef)({}),
              F = (0, a.useRef)(null),
              v = (0, a.useRef)(null),
              C = (0, a.useRef)(null),
              g = (0, a.useCallback)(() => {
                A(!0);
              }, []),
              B = (0, a.useCallback)(() => {
                A(!1);
              }, []),
              w = (0, a.useCallback)(() => {
                const e = C.current,
                  u = F.current,
                  t = b.current;
                if (e && t && u) {
                  const n = e.offsetTop + 0.5 * (e.offsetHeight - u.offsetHeight);
                  t.setScrollTop(n, void 0, d ? g : void 0);
                }
              }, [g, d]);
            (0, a.useEffect)(() => {
              if (n && null !== r) return (0, i.v)(w);
            }, [l, w, r, n]);
            const y = !(!v.current || !v.current.scrollbar) && v.current.scrollbar.scrollbarYActive,
              L = {
                scrollContainerRef: F,
                selectedItemRef: C,
                selectedItemId: r,
                isScrollComplete: m,
                scrollbarActive: y,
                onScrollAnimationComplete: B,
              },
              k = (0, a.cloneElement)(u, L);
            return s().createElement(
              "div",
              { className: _, ref: F },
              s().createElement(D.x, p({ ref: v, key: l, scrollAreaContainer: b.current }, E), k),
            );
          },
          w = {
            base: "DropDownItem_base_5e",
            base__small: "DropDownItem_base__small_d6",
            base__medium: "DropDownItem_base__medium_e4",
            base__selected: "DropDownItem_base__selected_8e",
            base__disabled: "DropDownItem_base__disabled_21",
          },
          y = ["size", "classMix", "onClick", "itemRenderer"];
        const L = (0, a.memo)((e) => {
            let u = e.size,
              t = e.classMix,
              n = e.onClick,
              o = e.itemRenderer,
              i = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  o = Object.keys(e);
                for (n = 0; n < o.length; n++) ((t = o[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, y);
            const l = i.id,
              c = i.isSelected,
              d = i.isDisabled,
              _ = i.label,
              E = i.soundHover,
              h = i.soundClick,
              m = (0, a.useCallback)(
                (e) => {
                  d || (n && n(e, l));
                },
                [l, d, n],
              ),
              A = (0, a.useCallback)(() => {
                d || (E && (0, b.G)(E));
              }, [d, E]),
              F = (0, a.useCallback)(() => {
                d || (h && (0, b.G)(h));
              }, [d, h]),
              v = r()(
                w.base,
                u && w[`base__${u}`],
                c && w.base__selected,
                d && w.base__disabled,
                t,
              );
            return s().createElement(
              "div",
              { className: v, onMouseEnter: A, onMouseDown: F, onClick: m },
              o ? o(i) : _,
            );
          }),
          k = { base__withScroll: "DropDownItems_base__withScroll_19" };
        function S() {
          return (
            (S =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            S.apply(this, arguments)
          );
        }
        const x = ({
            size: e,
            items: u,
            selectedIds: t,
            selectedItemId: n,
            selectedItemRef: o,
            onClick: i,
            parentId: l,
            soundHover: a,
            soundClick: c,
            itemClassMix: d,
            itemRenderer: _,
            scrollbarActive: E,
          }) =>
            s().createElement(
              "div",
              { className: r()(k.base, E && k.base__withScroll) },
              u.map((u) => {
                const r = `${l}_${u.id}`;
                return s().createElement(
                  "div",
                  { id: l ? r : void 0, key: r, ref: u.id === n ? o : null },
                  s().createElement(
                    L,
                    S({ size: e, soundHover: a, soundClick: c, classMix: d, itemRenderer: _ }, u, {
                      onClick: i,
                      isSelected: t.includes(u.id),
                    }),
                  ),
                );
              }),
            ),
          M = {
            base: "DropDownList_base_62",
            base__small: "DropDownList_base__small_0c",
            base__medium: "DropDownList_base__medium_99",
            scrollMix: "DropDownList_scrollMix_45",
          },
          T = {
            handlers: ["click-rail", "keyboard", "wheel", "drag-thumb"],
            wheelSpeed: 6,
            suppressScrollX: !0,
            animationDuration: 300,
            minScrollbarLength: 20,
          },
          O = ({
            parentId: e,
            size: u = E.Medium,
            items: t,
            selectedIds: n,
            isOpen: o,
            autoScroll: i,
            classMix: l,
            itemClassMix: c,
            itemRenderer: d,
            onClick: _,
            soundHover: h,
            soundClick: m,
          }) => {
            const A = (0, a.useState)(null),
              b = A[0],
              F = A[1],
              v = (0, g.D9)(o);
            (0, a.useEffect)(() => {
              if (o && !v) {
                const e = ((e, u) => {
                  if (!u.length) return null;
                  const t = e.find((e) => u.includes(e.id));
                  return t ? t.id : null;
                })(t, n);
                null !== e && F(e);
              }
              o || F(null);
            }, [o, t, n, v]);
            const C = e ? `${e}_list` : void 0;
            return s().createElement(
              "div",
              { id: C, className: r()(M.base, M[`base__${u}`], l) },
              s().createElement(
                B,
                { selectedItemId: b, isEnabled: i, scrollSettings: T, classMix: M.scrollMix },
                s().createElement(x, {
                  parentId: e,
                  items: t,
                  size: u,
                  selectedIds: n,
                  onClick: _,
                  soundHover: h,
                  soundClick: m,
                  itemClassMix: c,
                  itemRenderer: d,
                }),
              ),
            );
          },
          P = {
            base: "PureDropDown_base_fc",
            base__small: "PureDropDown_base__small_a6",
            base__medium: "PureDropDown_base__medium_05",
            control__down: "PureDropDown_control__down_18",
            list: "PureDropDown_list_28",
            list__up: "PureDropDown_list__up_a1",
            list__down: "PureDropDown_list__down_c4",
            list__under: "PureDropDown_list__under_64",
            list__above: "PureDropDown_list__above_c8",
          },
          H = (0, a.memo)(
            ({
              componentId: e,
              containerRef: u,
              items: t,
              selected: n = [],
              variant: h = _.Basic,
              size: m = E.Medium,
              multiple: A = !1,
              autoScroll: b = !0,
              placeholder: F,
              classMix: v,
              controlRenderer: g,
              itemRenderer: D,
              open: f,
              tooltipArgs: p,
              onChanges: B,
              onOpen: w,
              onClose: y,
              onClick: L,
              onClickOutside: k,
              onMouseEnter: S,
              onMouseDown: x,
              onMouseUp: M,
              onMouseLeave: R,
              soundHover: T = "highlight",
              soundClick: H = "play",
              soundItemHover: W,
              soundItemClick: Y,
            }) => {
              const N = (0, a.useRef)(null),
                X = (0, a.useRef)(null),
                I = (0, a.useRef)({ open: !1, listAbove: !1 }),
                U = (0, a.useState)(!1),
                j = U[0],
                Z = U[1],
                z = (0, a.useState)(!1),
                q = z[0],
                K = z[1],
                G = (0, a.useState)(window.innerHeight),
                V = G[0],
                $ = G[1],
                Q = ((e, u) => {
                  const t = Array.isArray(e) ? e : [e];
                  return !u && t.length > 1 ? t.slice(0, 1) : t;
                })(n, A),
                J = h !== _.Disabled,
                ee = void 0 === f,
                ue = Boolean(ee ? j : f);
              var te, ne;
              ((te = () => {
                $(window.innerHeight);
              }),
                (ne = []),
                (0, a.useEffect)(
                  () => (
                    window.addEventListener("resize", te),
                    () => window.removeEventListener("resize", te)
                  ),
                  ne,
                ));
              const re = (0, a.useCallback)(() => {
                I.current.open && ((I.current.open = !1), Z(!1), y && y());
              }, [y]);
              (0, l.gd)(ue ? c.n.ESCAPE : c.n.NONE, re, ue);
              const oe = (0, a.useCallback)(() => {
                (k && k(), ee && (Z(!1), (I.current.open = !1), y && y()));
              }, [k, y, ee]);
              ((0, a.useEffect)(() => {
                const e = N.current;
                if (e && ue)
                  return (
                    d.c1.register(e, oe),
                    () => {
                      d.c1.unregister(e, oe);
                    }
                  );
              }, [ue, oe]),
                (0, a.useEffect)(() => {
                  void 0 !== f && (I.current.open = f);
                }, [f]));
              const ie = (0, a.useCallback)(() => {
                if (!N.current || !X.current) return;
                const e = u && u.current,
                  t = e ? e.getBoundingClientRect().bottom : V,
                  n =
                    N.current.getBoundingClientRect().bottom +
                      X.current.getBoundingClientRect().height >
                    t;
                n !== I.current.listAbove && ((I.current.listAbove = n), K(n));
              }, [u, V]);
              (0, a.useEffect)(() => (0, i.v)(ie), [ie, m, t.length]);
              const le = (0, a.useCallback)(
                  (e) => {
                    const u = Q.findIndex((u) => u === e) > -1;
                    let t = [];
                    ((t = A ? (u ? Q.filter((u) => u !== e) : [e, ...Q]) : u ? [] : [e]),
                      B && B(t));
                  },
                  [A, B, Q],
                ),
                ae = (0, a.useCallback)(() => {
                  ee &&
                    ((I.current.open = !I.current.open),
                    Z(I.current.open),
                    I.current.open ? w && w() : y && y());
                }, [ee, w, y]),
                se = (0, a.useCallback)(
                  (e) => {
                    (J && ae(), L && L(e));
                  },
                  [J, L, ae],
                ),
                ce = (0, a.useCallback)(
                  (e, u) => {
                    (L && L(e, u), le(u), !A && ae());
                  },
                  [L, A, ae, le],
                ),
                de = (0, a.useCallback)((e) => S && S(e), [S]),
                _e = (0, a.useCallback)((e) => M && M(e), [M]),
                Ee = (0, a.useCallback)((e) => x && x(e), [x]),
                he = (0, a.useCallback)((e) => R && R(e), [R]),
                me = (0, a.useMemo)(
                  () =>
                    t
                      .filter((e) => Q.includes(e.id))
                      .map((e) => e.label)
                      .join(", "),
                  [t, Q],
                ),
                Ae = (0, a.useMemo)(() => t.filter((e) => Q.includes(e.id)), [t, Q]),
                be = g ? g(Ae) : void 0;
              return s().createElement(
                "div",
                {
                  id: e,
                  ref: N,
                  className: r()(P.base, P[`base__${m}`], v && v.base),
                  onMouseEnter: de,
                  onMouseUp: _e,
                  onMouseDown: Ee,
                  onMouseLeave: he,
                },
                s().createElement(
                  "div",
                  { className: r()(P.control, ue && P.control__down) },
                  s().createElement(
                    o.l,
                    { tooltipArgs: p },
                    s().createElement(C, {
                      parentId: e,
                      size: m,
                      variant: h,
                      isOpen: ue,
                      placeholder: F,
                      label: me,
                      classMix: v && v.control,
                      onClick: se,
                      soundHover: T,
                      soundClick: H,
                      customControl: be,
                    }),
                  ),
                ),
                s().createElement(
                  "div",
                  {
                    ref: X,
                    className: r()(
                      P.list,
                      ue ? P.list__down : P.list__up,
                      q ? P.list__above : P.list__under,
                    ),
                  },
                  s().createElement(O, {
                    parentId: e,
                    size: m,
                    items: t,
                    selectedIds: Q,
                    isOpen: ue,
                    autoScroll: b,
                    classMix: v && v.list,
                    itemClassMix: v && v.item,
                    itemRenderer: D,
                    onClick: ce,
                    soundHover: W || T,
                    soundClick: Y || H,
                  }),
                ),
              );
            },
          ),
          W = "AutoRenewalDropdown_base_3d",
          Y = "AutoRenewalDropdown_dropdownList_c6",
          N = ({
            nameList: e,
            selectedAutoRenewalType: u,
            onChange: t,
            onOpen: n,
            isAutoRenewalEnabled: r,
            tooltipArgs: o,
          }) => {
            const i = (0, a.useState)(u),
              l = i[0],
              c = i[1];
            return s().createElement(H, {
              items: e,
              selected: l,
              onChanges: (e) => {
                null != e && e.length && (c(e[0]), t(e[0]));
              },
              tooltipArgs: o,
              onOpen: n,
              size: E.Small,
              variant: r ? _.Basic : _.Disabled,
              classMix: { list: Y, base: W },
            });
          };
      },
      7208: (e, u, t) => {
        (t(6179), t(6483), t(4179));
      },
      5851: (e, u, t) => {
        var n = t(2262),
          r = t(8844),
          o = t(6373),
          i = t(483),
          l = t(9056),
          a = t(6179),
          s = t.n(a),
          c = t(9220),
          d = t(8935);
        const _ = R.strings.tank_setup;
        let E;
        !(function (e) {
          ((e.General = "general"),
            (e.Consumables = "consumables"),
            (e.Shells = "shells"),
            (e.Boosters = "boosters"),
            (e.Repair = "repair"));
        })(E || (E = {}));
        (0, a.memo)(
          ({
            modelPath: e,
            label: u = _.dealPanel.autoRenew(),
            onValueChanged: t,
            renewType: h = E.General,
          }) => {
            const m = (0, l.m)(e),
              A = m.isAutoRenewalEnabled,
              b = m.onAutoRenewalChanged,
              F = m.selectedAutoRenewalType,
              v = (0, a.useCallback)(() => {
                const e = { type: F, value: !A };
                (b && b(e), t && t(e));
              }, [t, b, A, F]),
              C = (0, a.useMemo)(() => {
                const e = _.tooltip.autoRenewal;
                return {
                  header: e.header.$dyn(h) || e.header.general(),
                  body: h === E.General ? "" : e.body.$dyn(h),
                };
              }, [h]),
              g = (0, a.useMemo)(() => {
                const e = _.tooltip.autoRenewal;
                return { header: e.dropdown.header.$dyn(F), body: e.dropdown.body.$dyn(F) };
              }, [F]),
              D = (0, a.useCallback)(
                (e) => {
                  if (!A) return;
                  const u = { type: e, value: A };
                  (b && b(u), t && t(u));
                },
                [t, b, A],
              ),
              f = (0, a.useMemo)(() => {
                const e = [i.t8.Soft, i.t8.Hard],
                  u = [];
                for (let t = 0; t < e.length; t++) {
                  const n = e[t],
                    r = _.dealPanel.autoRenewType.$dyn(n);
                  u.push({ id: n, label: r });
                }
                return u;
              }, []);
            return s().createElement(
              s().Fragment,
              null,
              s().createElement(
                o.i,
                C,
                s().createElement(n.XZ, {
                  id: "renewal-setup-checkbox",
                  isChecked: A,
                  text: u,
                  onChange: v,
                  alignment: r.N3.Center,
                }),
              ),
              h === E.Boosters &&
                s().createElement(
                  "div",
                  { className: d.Z.dropdown },
                  s().createElement(c.v, {
                    nameList: f,
                    selectedAutoRenewalType: F,
                    onChange: D,
                    isAutoRenewalEnabled: A,
                    tooltipArgs: g,
                  }),
                ),
            );
          },
        );
      },
      8982: (e, u, t) => {
        var n = t(6179),
          r = t.n(n),
          o = t(3457),
          i = t(6373),
          l = t(7383);
        const a = "ConfirmButton_base_75",
          s = r().memo(
            ({ applyBtnString: e, isDisabled: u, onConfirm: t, confirmButtonRef: i }) => {
              const l = R.strings.tank_setup.dealPanel.button.$dyn(e),
                s = (0, n.useCallback)(() => t && t(), [t]);
              return r().createElement(
                "div",
                { ref: i, className: a, id: "deal-panel-confirm" },
                r().createElement(o.u5, { size: o.qE.medium, disabled: u, onClick: s }, l),
              );
            },
          ),
          c = "Controls_base_d3",
          d = "Controls_button_f8";
        r().memo(
          ({
            applyBtnString: e = l.YR,
            isDisabled: u,
            canCancel: t,
            onCancel: n,
            onConfirm: a,
            confirmButtonRef: _,
          }) => {
            const E = R.strings.tank_setup.dealPanel,
              h = r().createElement(s, {
                applyBtnString: e,
                isDisabled: u,
                onConfirm: a,
                confirmButtonRef: _,
              });
            return r().createElement(
              "div",
              { id: "deal-panel-controls", className: c },
              u
                ? r().createElement(
                    i.i,
                    { body: E.tooltip.notEnough() },
                    r().createElement("div", null, h),
                  )
                : h,
              r().createElement(
                "div",
                { id: "deal-panel-cancel" },
                r().createElement(
                  o.u5,
                  {
                    size: o.qE.medium,
                    type: o.L$.secondary,
                    mixClass: d,
                    disabled: !t,
                    onClick: n,
                  },
                  E.button.cancel(),
                ),
              ),
            );
          },
        );
      },
      8772: (e, u, t) => {
        (t(6483), t(9056), t(6179), t(1922), t(3934), t(7208), t(5851), t(8982));
        t(8401);
        let n;
        !(function (e) {
          ((e.Column = "column"), (e.Row = "row"));
        })(n || (n = {}));
        R.strings.tank_setup.dealPanel;
      },
      8401: (e, u, t) => {
        (t(6179), t(6483), t(7405), t(329));
      },
      3934: (e, u, t) => {
        (t(6179), t(6483));
      },
      483: (e, u, t) => {
        t.d(u, { t8: () => n });
        let n;
        !(function (e) {
          ((e.Undefined = "Undefined"), (e.Soft = "soft"), (e.Hard = "hard"));
        })(n || (n = {}));
      },
      7383: (e, u, t) => {
        t.d(u, { YR: () => n });
        const n = "apply";
      },
      6880: (e, u, t) => {
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
      4382: (e, u, t) => {
        t.d(u, { Z: () => n });
        const n = {
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
      },
      8460: (e, u, t) => {
        t.d(u, { Z: () => n });
        const n = {
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
        };
      },
      1960: () => {},
      8935: (e, u, t) => {
        t.d(u, { Z: () => n });
        const n = { dropdown: "AutoRenewal_dropdown_35" };
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
        for (a = 0; a < deferred.length; a++) {
          for (var [u, t, n] = deferred[a], o = !0, i = 0; i < u.length; i++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[i]))
              ? u.splice(i--, 1)
              : ((o = !1), n < r && (r = n));
          if (o) {
            deferred.splice(a--, 1);
            var l = t();
            void 0 !== l && (e = l);
          }
        }
        return e;
      }
      n = n || 0;
      for (var a = deferred.length; a > 0 && deferred[a - 1][2] > n; a--)
        deferred[a] = deferred[a - 1];
      deferred[a] = [u, t, n];
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
    (__webpack_require__.j = 826),
    (() => {
      var e = { 826: 0, 543: 0, 745: 0, 653: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            r,
            [o, i, l] = t,
            a = 0;
          if (o.some((u) => 0 !== e[u])) {
            for (n in i) __webpack_require__.o(i, n) && (__webpack_require__.m[n] = i[n]);
            if (l) var s = l(__webpack_require__);
          }
          for (u && u(t); a < o.length; a++)
            ((r = o[a]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(s);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [727], () => __webpack_require__(8772));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
