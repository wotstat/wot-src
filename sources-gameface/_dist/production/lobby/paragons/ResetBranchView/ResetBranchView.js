(() => {
  var __webpack_modules__ = {
      3779: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => F });
        var n = t(6483),
          r = t.n(n),
          a = t(9887),
          s = t.n(a),
          o = t(3377),
          i = t(6179),
          l = t.n(i),
          c = t(5026);
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
        Object.keys(s());
        const E = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          d = (Object.keys(E), ["mt", "mr", "mb", "ml"]),
          A = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          F = (0, o.ZP)((e) => {
            let u = e.className,
              t = e.width,
              n = e.height,
              a = e.m,
              s = e.mt,
              o = void 0 === s ? a : s,
              F = e.mr,
              C = void 0 === F ? a : F,
              D = e.mb,
              g = void 0 === D ? a : D,
              p = e.ml,
              h = void 0 === p ? a : p,
              B = e.column,
              f = e.row,
              v = e.flexDirection,
              b = void 0 === v ? (B ? "column" : f && "row") || void 0 : v,
              S = e.flexStart,
              x = e.center,
              w = e.flexEnd,
              R = e.spaceBetween,
              T = e.spaceAround,
              y = e.justifyContent,
              N =
                void 0 === y
                  ? (S ? "flex-start" : x && "center") ||
                    (w && "flex-end") ||
                    (R && "space-between") ||
                    (T && "space-around") ||
                    void 0
                  : y,
              M = e.alignItems,
              P =
                void 0 === M
                  ? (S ? "flex-start" : x && "center") || (w && "flex-end") || void 0
                  : M,
              L = e.alignSelf,
              O = e.wrap,
              k = e.flexWrap,
              I = void 0 === k ? (O ? "wrap" : void 0) : k,
              H = e.grow,
              U = e.shrink,
              W = e.flex,
              G = void 0 === W ? (H || U ? `${H ? 1 : 0} ${U ? 1 : 0} auto` : void 0) : W,
              $ = e.style,
              z = e.children,
              V = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, m);
            const j = (0, i.useMemo)(() => {
                const e = { mt: o, mr: C, mb: g, ml: h },
                  u = ((e) =>
                    d.reduce((u, t) => {
                      const n = e[t];
                      return n && "number" != typeof n ? u.concat(E[!0 === n ? "MD" : n][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    d.reduce((u, t) => {
                      const n = e[t];
                      return ("number" == typeof n && (u[A[t]] = n + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, $, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: G,
                    alignSelf: L,
                    display: b || P ? "flex" : void 0,
                    flexDirection: b,
                    flexWrap: I,
                    justifyContent: N,
                    alignItems: P,
                  }),
                  computedClassNames: u,
                };
              }, [t, n, o, C, g, h, $, G, L, b, I, N, P]),
              X = j.computedStyle,
              q = j.computedClassNames;
            return l().createElement(
              "div",
              _({ className: r()(c.Z.base, ...q, u), style: X }, V),
              z,
            );
          });
      },
      280: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => l });
        var n = t(6179),
          r = t.n(n),
          a = t(6483),
          s = t.n(a),
          o = t(3649),
          i = t(5287);
        const l = ({ binding: e, text: u = "", classMix: t, alignment: a = o.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                n.Fragment,
                null,
                u.split("\n").map((u, l) =>
                  r().createElement(
                    "div",
                    { className: s()(i.Z.base, t), key: `${u}-${l}` },
                    (0, o.Uw)(u, a, e).map((e, u) =>
                      r().createElement(n.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => m });
        var n = t(3138),
          r = t(6179),
          a = t(1043),
          s = t(5262);
        const o = n.O.client.getSize("rem"),
          i = o.width,
          l = o.height,
          c = Object.assign({ width: i, height: l }, (0, s.T)(i, l, a.j)),
          m = (0, r.createContext)(c);
      },
      1039: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => c });
        var n = t(6179),
          r = t.n(n),
          a = t(6536),
          s = t(3495),
          o = t(1043),
          i = t(5262),
          l = t(3138);
        const c = (0, n.memo)(({ children: e }) => {
          const u = (0, n.useContext)(s.Y),
            t = (0, n.useState)(u),
            c = t[0],
            m = t[1],
            _ = (0, n.useCallback)((e, u) => {
              const t = l.O.view.pxToRem(e),
                n = l.O.view.pxToRem(u);
              m(Object.assign({ width: t, height: n }, (0, i.T)(t, n, o.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", _);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", _), [_]));
          const E = (0, n.useMemo)(() => Object.assign({}, c), [c]);
          return r().createElement(s.Y.Provider, { value: E }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var n = t(6179),
          r = t(7382),
          a = t(3495);
        const s = ["children"];
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
            })(e, s);
          const o = (0, n.useContext)(a.Y),
            i = o.extraLarge,
            l = o.large,
            c = o.medium,
            m = o.small,
            _ = o.extraSmall,
            E = o.extraLargeWidth,
            d = o.largeWidth,
            A = o.mediumWidth,
            F = o.smallWidth,
            C = o.extraSmallWidth,
            D = o.extraLargeHeight,
            g = o.largeHeight,
            p = o.mediumHeight,
            h = o.smallHeight,
            B = o.extraSmallHeight,
            f = { extraLarge: D, large: g, medium: p, small: h, extraSmall: B };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && i) return u;
            if (t.large && l) return u;
            if (t.medium && c) return u;
            if (t.small && m) return u;
            if (t.extraSmall && _) return u;
          } else {
            if (t.extraLargeWidth && E) return (0, r.H)(u, t, f);
            if (t.largeWidth && d) return (0, r.H)(u, t, f);
            if (t.mediumWidth && A) return (0, r.H)(u, t, f);
            if (t.smallWidth && F) return (0, r.H)(u, t, f);
            if (t.extraSmallWidth && C) return (0, r.H)(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && D) return u;
              if (t.largeHeight && g) return u;
              if (t.mediumHeight && p) return u;
              if (t.smallHeight && h) return u;
              if (t.extraSmallHeight && B) return u;
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
        (0, n.memo)(o);
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
      7613: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => v });
        var n = t(6483),
          r = t.n(n),
          a = t(3779),
          s = t(280),
          o = t(3532),
          i = t.n(o),
          l = t(9887),
          c = t.n(l),
          m = t(3377),
          _ = t(6179),
          E = t.n(_),
          d = t(3393);
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
        const C = Object.keys(i()),
          D = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          g = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          p = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          h = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          B =
            (Object.keys(h),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": D,
              "heading-H36": D,
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
            (Object.keys(B),
            (e) =>
              e
                ? ((e) => C.includes(e))(e)
                  ? { colorClassName: d.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          v = (0, m.ZP)((e) => {
            let u = e.text,
              t = e.variant,
              n = e.className,
              o = e.color,
              i = e.m,
              l = e.mt,
              c = void 0 === l ? i : l,
              m = e.mr,
              C = void 0 === m ? i : m,
              D = e.mb,
              g = void 0 === D ? i : D,
              p = e.ml,
              h = void 0 === p ? i : p,
              v = e.style,
              b = e.format,
              S = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, A);
            const x = (0, _.useMemo)(() => {
                const e = f(o),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, v, n), colorClassName: u };
              }, [v, o]),
              w = x.computedStyle,
              R = x.colorClassName;
            return E().createElement(
              a.ZP,
              F(
                {
                  className: r()(d.Z.base, t && d.Z[t], R, n),
                  style: w,
                  mt: !0 === c ? B[t || "paragraph-P16"].mt : c,
                  mr: !0 === C ? B[t || "paragraph-P16"].mr : C,
                  mb: !0 === g ? B[t || "paragraph-P16"].mb : g,
                  ml: !0 === h ? B[t || "paragraph-P16"].ml : h,
                },
                S,
              ),
              void 0 !== b ? E().createElement(s.z, F({}, b, { text: u })) : u,
            );
          });
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
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => o, onResize: () => a }));
        var n = t(2472),
          r = t(1176);
        const a = (0, n.E)("clientResized"),
          s = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const o = (function () {
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
                    o = s[u]((e) => t([e, "outside"]));
                  function i(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, i),
                    n(),
                    () => {
                      r &&
                        (o(), window.removeEventListener(a, i), (e.listeners -= 1), n(), (r = !1));
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
            graphicsQuality: () => s,
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
        const s = {
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
            addPreloadTexture: () => o,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => S,
            events: () => a.U,
            extraSize: () => x,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => b,
            getScale: () => F,
            getSize: () => _,
            getViewGlobalPosition: () => d,
            isClientAccessible: () => h,
            isEventHandled: () => f,
            isFocused: () => p,
            pxToRem: () => C,
            remToPx: () => D,
            resize: () => E,
            sendEvent: () => s.qP,
            setAnimateWindow: () => g,
            setEventHandled: () => B,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => w,
          }));
        var n = t(3722),
          r = t(6112),
          a = t(6538),
          s = t(8566);
        function o(e) {
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
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function _(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function E(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function d(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: D(u.x), y: D(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function C(e) {
          return viewEnv.pxToRem(e);
        }
        function D(e) {
          return viewEnv.remToPx(e);
        }
        function g(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function p() {
          return viewEnv.isFocused();
        }
        function h() {
          return viewEnv.isClientAccessible();
        }
        function B() {
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
        const S = Object.keys(r.W).reduce(
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
          w = Promise.all([
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
          s = 32,
          o = 64,
          i = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                s = (function (e, u) {
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
                    Object.assign({ __Type: t, type: e }, s, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, s));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          l = {
            close(e) {
              i("popover" === e ? r : s);
            },
            minimize() {
              i(o);
            },
            move(e) {
              i(a, { isMouseEvent: !0, on: e });
            },
          };
      },
      3377: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => c });
        var n = t(5415),
          r = t(6179),
          a = t.n(r);
        const s = ["xl", "lg", "md", "sm", "xs"],
          o = (e) => e.includes("_") && ((e) => s.includes(e))(e.split("_").at(-1)),
          i = [n.cJ.ExtraLarge, n.cJ.Large, n.cJ.Medium, n.cJ.Small, n.cJ.ExtraSmall],
          l = (e, u) =>
            Object.keys(e).reduce((t, n) => {
              if (n in t) return t;
              if (o(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const a = i.indexOf(u),
                  o = (-1 !== a ? s.slice(a) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  l = o ? e[o] : void 0;
                return ((t[r] = void 0 !== l ? l : e[r]), t);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, u) => s.some((t) => void 0 !== u[`${e}_${t}`]))(n, e) ||
                  (t[n] = r),
                t
              );
            }, {}),
          c = (e, u = l) => {
            const t = (
              (e, u = l) =>
              (t) => {
                const s = (0, n.GS)().mediaSize,
                  o = (0, r.useMemo)(() => u(t, s), [t, s]);
                return a().createElement(e, o);
              }
            )(e, u);
            return a().memo((u) =>
              Object.keys(u).some((e) => o(e) && void 0 !== u[e])
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
        t.d(u, { Aq: () => i, GS: () => l, cJ: () => s, fd: () => o });
        var n = t(6179),
          r = t(7739),
          a = t(1043);
        let s, o, i;
        (!(function (e) {
          ((e[(e.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = a.j.small.width)] = "Small"),
            (e[(e.Medium = a.j.medium.width)] = "Medium"),
            (e[(e.Large = a.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
        })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = a.j.small.width)] = "Small"),
              (e[(e.Medium = a.j.medium.width)] = "Medium"),
              (e[(e.Large = a.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
          })(o || (o = {})),
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
            mediaSize: a,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: u,
            remScreenHeight: t,
          };
        };
      },
      5521: (e, u, t) => {
        "use strict";
        let n, r;
        (t.d(u, { n: () => n, s: () => r }),
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
      3649: (e, u, t) => {
        "use strict";
        let n;
        function r(e, u) {
          return e.replace(/\{\w+\}/g, (e) => String(u[e.slice(1, -1)]));
        }
        function a(e) {
          return e.replace(/-/g, "_");
        }
        (t.d(u, { BN: () => a, Uw: () => _, WU: () => r, v2: () => n }),
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
          o = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          i = (e, u, t = n.left) => e.split(u).reduce(t === n.left ? s : o, []),
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
          m = (e, u = n.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return c.includes(t)
              ? l(e)
              : ((e, u = n.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = e.replace(/&nbsp;/g, " ");
                  return (i(a, /( )/, u).forEach((e) => (t = t.concat(i(e, r, n.left)))), t);
                })(e, u);
          },
          _ = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : m(e, u)));
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
        t.d(u, { B3: () => l, Z5: () => s, B0: () => i, ry: () => D });
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
        const s = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
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
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = t(5521),
          d = t(3138);
        const A = ["args"];
        function F(e, u, t, n, r, a, s) {
          try {
            var o = e[a](s),
              i = o.value;
          } catch (e) {
            return void t(e);
          }
          o.done ? u(i) : Promise.resolve(i).then(n, r);
        }
        const C = (e) => ({
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
                  return new Promise(function (n, r) {
                    var a = e.apply(u, t);
                    function s(e) {
                      F(a, n, r, s, o, "next", e);
                    }
                    function o(e) {
                      F(a, n, r, s, o, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          g = (e, u) => {
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
          p = () => g(i.CLOSE),
          h = (e, u) => {
            e.keyCode === E.n.ESCAPE && u();
          };
        var B = t(7572);
        const f = r.instance,
          v = {
            DataTracker: a.Z,
            ViewModel: B.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: _,
            makeGlobalBoundingBox: C,
            sendMoveEvent: (e) => g(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: p,
            sendClosePopOverEvent: () => g(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              g(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, r = R.invalid("resId"), a) => {
              const s = d.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                m = o.width,
                _ = o.height,
                E = {
                  x: d.O.view.pxToRem(l) + s.x,
                  y: d.O.view.pxToRem(c) + s.y,
                  width: d.O.view.pxToRem(m),
                  height: d.O.view.pxToRem(_),
                };
              g(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: C(E),
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
              h(e, p);
            },
            handleViewEvent: g,
            onBindingsReady: D,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
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
            SystemLocale: s,
            UserLocale: o,
          };
        window.ViewEnvHelper = v;
      },
      6394: (e, u, t) => {
        "use strict";
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => Et,
            Bar: () => ct,
            DefaultScroll: () => _t,
            Direction: () => Re,
            defaultSettings: () => Te,
            useHorizontalScrollApi: () => Ne,
          }));
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => yt,
            Bar: () => wt,
            Default: () => Tt,
            useVerticalScrollApi: () => dt,
          }));
        var a = t(7739),
          s = t(6179),
          o = t.n(s),
          i = t(6483),
          l = t.n(i),
          c = t(926),
          m = t.n(c),
          _ = t(5415);
        const E = ["children", "className"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        const A = {
            [_.fd.ExtraSmall]: "",
            [_.fd.Small]: m().SMALL_WIDTH,
            [_.fd.Medium]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH}`,
            [_.fd.Large]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH}`,
            [_.fd.ExtraLarge]:
              `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH} ${m().EXTRA_LARGE_WIDTH}`,
          },
          F = {
            [_.Aq.ExtraSmall]: "",
            [_.Aq.Small]: m().SMALL_HEIGHT,
            [_.Aq.Medium]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT}`,
            [_.Aq.Large]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT}`,
            [_.Aq.ExtraLarge]:
              `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT} ${m().EXTRA_LARGE_HEIGHT}`,
          },
          C = {
            [_.cJ.ExtraSmall]: "",
            [_.cJ.Small]: m().SMALL,
            [_.cJ.Medium]: `${m().SMALL} ${m().MEDIUM}`,
            [_.cJ.Large]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE}`,
            [_.cJ.ExtraLarge]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE} ${m().EXTRA_LARGE}`,
          },
          D = (e) => {
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
              })(e, E);
            const r = (0, _.GS)(),
              a = r.mediaWidth,
              s = r.mediaHeight,
              i = r.mediaSize;
            return o().createElement("div", d({ className: l()(t, A[a], F[s], C[i]) }, n), u);
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
          return o().createElement(a.ZN, null, o().createElement(D, t, u));
        };
        var h = t(493),
          B = t.n(h);
        function f(e) {
          engine.call("PlaySound", e);
        }
        const v = {
            playHighlight() {
              f("highlight");
            },
            playClick() {
              f("play");
            },
            playYes() {
              f("yes1");
            },
          },
          b = {
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
        let S, x;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(S || (S = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(x || (x = {})));
        const w = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: r,
          mixClass: a,
          soundHover: i,
          soundClick: c,
          onMouseEnter: m,
          onMouseMove: _,
          onMouseDown: E,
          onMouseUp: d,
          onMouseLeave: A,
          onClick: F,
        }) => {
          const C = (0, s.useRef)(null),
            D = (0, s.useState)(t),
            g = D[0],
            p = D[1],
            h = (0, s.useState)(!1),
            B = h[0],
            v = h[1],
            x = (0, s.useState)(!1),
            w = x[0],
            T = x[1],
            y = (0, s.useCallback)(() => {
              r || (C.current && (C.current.focus(), p(!0)));
            }, [r]),
            N = (0, s.useCallback)(
              (e) => {
                g && null !== C.current && !C.current.contains(e.target) && p(!1);
              },
              [g],
            ),
            M = (0, s.useCallback)(
              (e) => {
                r || (F && F(e));
              },
              [r, F],
            ),
            P = (0, s.useCallback)(
              (e) => {
                r || (null !== i && f(i), m && m(e), T(!0));
              },
              [r, i, m],
            ),
            L = (0, s.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            O = (0, s.useCallback)(
              (e) => {
                r || (d && d(e), v(!1));
              },
              [r, d],
            ),
            k = (0, s.useCallback)(
              (e) => {
                r || (null !== c && f(c), E && E(e), t && y(), v(!0));
              },
              [r, c, E, y, t],
            ),
            I = (0, s.useCallback)(
              (e) => {
                r || (A && A(e), v(!1));
              },
              [r, A],
            ),
            H = l()(
              b.base,
              b[`base__${n}`],
              {
                [b.base__disabled]: r,
                [b[`base__${u}`]]: u,
                [b.base__focus]: g,
                [b.base__highlightActive]: B,
                [b.base__firstHover]: w,
              },
              a,
            ),
            U = l()(b.state, b.state__default);
          return (
            (0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", N),
                () => {
                  document.removeEventListener("mousedown", N);
                }
              ),
              [N],
            ),
            (0, s.useEffect)(() => {
              p(t);
            }, [t]),
            o().createElement(
              "div",
              {
                ref: C,
                className: H,
                onMouseEnter: P,
                onMouseMove: L,
                onMouseUp: O,
                onMouseDown: k,
                onMouseLeave: I,
                onClick: M,
              },
              n !== S.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: b.back }),
                  o().createElement("span", { className: b.texture }),
                ),
              o().createElement(
                "span",
                { className: U },
                o().createElement("span", { className: b.stateDisabled }),
                o().createElement("span", { className: b.stateHighlightHover }),
                o().createElement("span", { className: b.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: b.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        w.defaultProps = {
          type: S.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const T = (0, s.memo)(w);
        var y = t(7613);
        const N = {
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
          M = [
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
        function P() {
          return (
            (P =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            P.apply(this, arguments)
          );
        }
        class L extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && f(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && f(this.props.soundClick));
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
              s = e.classNames,
              i = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              _ = e.onMouseUp,
              E =
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
                })(e, M)),
              d = l()(N.base, N[`base__${a}`], N[`base__${r}`], null == s ? void 0 : s.base),
              A = l()(N.icon, N[`icon__${a}`], N[`icon__${r}`], null == s ? void 0 : s.icon),
              F = l()(N.glow, null == s ? void 0 : s.glow),
              C = l()(N.caption, N[`caption__${a}`], null == s ? void 0 : s.caption),
              D = l()(N.goto, null == s ? void 0 : s.goto);
            return o().createElement(
              "div",
              P(
                {
                  className: d,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(m),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                E,
              ),
              "info" !== a && o().createElement("div", { className: N.shine }),
              o().createElement(
                "div",
                { className: A },
                o().createElement("div", { className: F }),
              ),
              o().createElement("div", { className: C }, u),
              n && o().createElement("div", { className: D }, n),
            );
          }
        }
        L.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        let O;
        !(function (e) {
          ((e[(e.Initial = 0)] = "Initial"),
            (e[(e.Success = 1)] = "Success"),
            (e[(e.Failed = 2)] = "Failed"));
        })(O || (O = {}));
        const k = (e, u) => {
          let t;
          const n = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(n));
          };
        };
        var I = t(3138),
          H = t(5521),
          U = t(4179);
        const W = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function G(e = H.n.NONE, u = W, t = !1) {
          (0, s.useEffect)(() => {
            if (e !== H.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (I.O.view.isEventHandled()) return;
                (I.O.view.setEventHandled(), u(n), t && n.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        function $() {
          const e = (0, s.useRef)(!0);
          var u;
          return (
            (u = () => {
              e.current = !1;
            }),
            (0, s.useEffect)(u, []),
            e.current
          );
        }
        var z = t(3403);
        let V;
        !(function (e) {
          ((e.NORMAL = "normal"), (e.ERROR = "error"), (e.CONFORMITY = "conformity"));
        })(V || (V = {}));
        function j(e) {
          return e;
        }
        function X() {
          return !1;
        }
        console.log;
        var q = t(9174);
        function Y(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return Z(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Z(e, u);
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
        function Z(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const K = (e) => (0 === e ? window : window.subViews.get(e));
        function Q(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        const J = Q;
        function ee(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, n) => u(null == e ? void 0 : e.value, t, n));
        }
        var ue = t(3946);
        const te = ((e, u) => {
            const t = (0, s.createContext)({});
            return [
              function ({ mode: n = "real", options: r, children: a, mocks: i }) {
                const l = (0, s.useRef)([]),
                  c = (t, n, r) => {
                    var a;
                    const s = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = K,
                        context: n = "model",
                      } = {}) {
                        const r = new Map();
                        function a(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = r.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const s = (e) => {
                          const r = t(u),
                            a = n.split(".").reduce((e, u) => e[u], r);
                          return "string" != typeof e || 0 === e.length
                            ? a
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, a);
                        };
                        return {
                          subscribe: (t, a) => {
                            const o = "string" == typeof a ? `${n}.${a}` : n,
                              i = I.O.view.addModelObserver(o, u, !0);
                            return (r.set(i, t), e && t(s(a)), i);
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
                            for (var e, t = Y(r.keys()); !(e = t()).done;) a(e.value, u);
                          },
                          unsubscribe: a,
                        };
                      })(n),
                      o =
                        "real" === t
                          ? s
                          : Object.assign({}, s, {
                              readByPath:
                                null != (a = null == r ? void 0 : r.getter) ? a : () => {},
                            }),
                      i = (e) =>
                        "mocks" === t ? (null == r ? void 0 : r.getter(e)) : o.readByPath(e),
                      c = (e) => l.current.push(e),
                      m = e({
                        mode: t,
                        readByPath: i,
                        externalModel: o,
                        observableModel: {
                          array: (e, u) => {
                            const n = null != u ? u : i(e),
                              r = q.LO.box(n, { equals: X });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, q.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, u) => {
                            const n = null != u ? u : i(e),
                              r = q.LO.box(n, { equals: X });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, q.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, u) => {
                            const n = i(u);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, u) => ((e[u] = q.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, q.aD)((u) => {
                                      e.forEach((e) => {
                                        r[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                r
                              );
                            }
                            {
                              const r = e,
                                a = Object.entries(r),
                                s = a.reduce((e, [u, t]) => ((e[t] = q.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, q.aD)((e) => {
                                      a.forEach(([u, t]) => {
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
                        cleanup: c,
                      }),
                      _ = { mode: t, model: m, externalModel: o, cleanup: c };
                    return {
                      model: m,
                      controls: "mocks" === t && r ? r.controls(_) : u(_),
                      externalModel: o,
                      mode: t,
                    };
                  },
                  m = (0, s.useRef)(!1),
                  _ = (0, s.useState)(n),
                  E = _[0],
                  d = _[1],
                  A = (0, s.useState)(() => c(n, r, i)),
                  F = A[0],
                  C = A[1];
                return (
                  (0, s.useEffect)(() => {
                    m.current ? C(c(E, r, i)) : (m.current = !0);
                  }, [i, E, r]),
                  (0, s.useEffect)(() => {
                    d(n);
                  }, [n]),
                  (0, s.useEffect)(
                    () => () => {
                      (F.externalModel.dispose(), l.current.forEach((e) => e()));
                    },
                    [F],
                  ),
                  o().createElement(t.Provider, { value: F }, a)
                );
              },
              () => (0, s.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  resetVehicles: e.array("resetVehicles"),
                  pageState: q.LO.box("default"),
                  checkboxState: q.LO.box(!1),
                  captchaState: q.LO.box(V.NORMAL),
                },
                t = (0, ue.Om)(
                  () =>
                    ee(u.resetVehicles.get(), (e) =>
                      Object.assign({}, e, {
                        vehicleInfo: Object.assign({}, e.vehicleInfo, {
                          tags: ee(e.vehicleInfo.tags, j),
                        }),
                        returnedItems: ee(e.returnedItems, (e) =>
                          Object.assign({}, e, { groupInfo: ee(e.groupInfo, j) }),
                        ),
                      }),
                    ),
                  { equals: X },
                ),
                n = (0, ue.Om)(
                  () =>
                    (function (e, u, t) {
                      if (Array.isArray(e)) return e.reduce(u, t);
                      let n = t;
                      for (let t = 0; t < e.length; t++) n = u(n, J(e, t), t, e);
                      return n;
                    })(t(), (e, u) => e + u.progressPoints, 0),
                  { equals: X },
                );
              return Object.assign({}, u, {
                computes: { getResetVehicles: t, getTotalVehiclesProgressPoints: n },
              });
            },
            ({ externalModel: e, model: u }) => ({
              onCaptchaStateChange: (0, q.aD)((e) => {
                u.captchaState.set(e);
              }),
              onCheckboxStateChange: (0, q.aD)((e) => {
                u.checkboxState.set(e);
              }),
              onClose: e.createCallbackNoArgs("onClose"),
              onConfirm: e.createCallbackNoArgs("onConfirm"),
              onInstallVehicleConfiguration: e.createCallback(
                (e) => ({ configuration: e }),
                "onInstallVehicleConfiguration",
              ),
            }),
          ),
          ne = te[0],
          re = te[1];
        let ae, se, oe, ie, le, ce;
        (!(function (e) {
          ((e[(e.Initial = 0)] = "Initial"),
            (e[(e.Success = 1)] = "Success"),
            (e[(e.Failed = 2)] = "Failed"));
        })(ae || (ae = {})),
          (function (e) {
            ((e[(e.INFO = 0)] = "INFO"),
              (e[(e.DETAILS = 1)] = "DETAILS"),
              (e[(e.CAPTCHA = 2)] = "CAPTCHA"));
          })(se || (se = {})),
          (function (e) {
            ((e[(e.OptionalDevices = 0)] = "OptionalDevices"),
              (e[(e.BattleBoosters = 1)] = "BattleBoosters"),
              (e[(e.Shells = 2)] = "Shells"),
              (e[(e.Customization = 3)] = "Customization"),
              (e[(e.Equipments = 4)] = "Equipments"),
              (e[(e.Crew = 5)] = "Crew"));
          })(oe || (oe = {})),
          (function (e) {
            ((e.CREDITS = "credits"),
              (e.EQUIPMENTS = "equipment"),
              (e.BLUEPRINTS = "finalBlueprints"));
          })(ie || (ie = {})),
          (function (e) {
            ((e.INFO = "info-page"),
              (e.DETAILS = "details-page"),
              (e.RETURN_ITEMS = "return-items"));
          })(le || (le = {})),
          (function (e) {
            ((e.COINS_FOR_BRANCH_RESET = "coinsForBranchReset"),
              (e.TOTAL_VEHICLE_POINTS = "totalVehiclesPoints"),
              (e.COMPLETE_BONUS_COINS = "completeBonusCoins"));
          })(ce || (ce = {})));
        const me = {
            base: "App_base_87",
            content: "App_content_2c",
            content__captcha: "App_content__captcha_f5",
            content__result: "App_content__result_5d",
            close: "App_close_a3",
            header: "App_header_9a",
            captchaWrapper: "App_captchaWrapper_30",
            footer: "App_footer_df",
            footer__captcha: "App_footer__captcha_8e",
            resultScreenButton: "App_resultScreenButton_5c",
          },
          _e = (e) => {
            if (!e) return !1;
            const u = e.getBoundingClientRect(),
              t = u.width,
              n = u.height;
            return 0 !== t && 0 !== n;
          },
          Ee = (e) => {
            const u = (0, s.useState)(_e(e ? e.current : null)),
              t = u[0],
              n = u[1];
            return (
              (0, s.useEffect)(() => {
                let u = 0;
                const t = () => {
                  u = requestAnimationFrame(() => {
                    _e(e ? e.current : null) ? n(!0) : t();
                  });
                };
                return (
                  t(),
                  () => {
                    cancelAnimationFrame(u);
                  }
                );
              }, [e]),
              (0, s.useEffect)(() => () => n(!1), [e]),
              t
            );
          },
          de = {
            base: "Captcha_base_24",
            base__error: "Captcha_base__error_32",
            base__conformity: "Captcha_base__conformity_9b",
            glow: "Captcha_glow_1b",
            border: "Captcha_border_66",
            header: "Captcha_header_1d",
            captchaValue: "Captcha_captchaValue_3f",
            input: "Captcha_input_cd",
            input__notEmpty: "Captcha_input__notEmpty_a2",
            warning: "Captcha_warning_99",
            warningIcon: "Captcha_warningIcon_85",
            warningText: "Captcha_warningText_5b",
            conformityIcon: "Captcha_conformityIcon_0a",
          },
          Ae = (e) => e.replace(/\B(?=(\d{3})+(?!\d))/g, " "),
          Fe = (e, u, t) =>
            e
              .split("")
              .filter((e, n) => (n < u || n >= t) && " " !== e)
              .join(""),
          Ce = /^\d+$/,
          De = /\s/g,
          ge = R.strings.paragons.resetBranch.captcha,
          pe = (0, z.Pi)(() => {
            const e = re(),
              u = e.model,
              t = e.controls,
              n = (0, s.useRef)(null),
              r = u.root.get().totalCredits,
              a = ((e, u, t) => {
                const n = (0, s.useState)(""),
                  r = n[0],
                  a = n[1],
                  o = (0, s.useState)(""),
                  i = o[0],
                  l = o[1],
                  c = (0, s.useCallback)(
                    (e) => {
                      const n = r.replace(De, ""),
                        a = u.toString().slice(0, n.toString().length);
                      String(n) !== a
                        ? (t(V.ERROR), e && f(R.sounds.paragons_captcha_incorrect()))
                        : n.toString().length === String(u).length
                          ? (t(V.CONFORMITY), e && f(R.sounds.paragons_captcha_enter()))
                          : (t(V.NORMAL), e && f(R.sounds.paragons_captcha_correct()));
                    },
                    [r, t, u],
                  );
                return (
                  (0, s.useEffect)(() => {
                    c(r.length > i.length);
                  }, [r, c]),
                  {
                    inputValue: r,
                    handleChange: (t) => {
                      const n = t.currentTarget.value.replace(De, ""),
                        s = Ce.test(n);
                      if (n.length > u.toString().length) return;
                      const o = e.current;
                      if (s || "" === n) {
                        const e = Ae(n);
                        if (
                          (a(e), l(r), e.length === r.length - 2 && o && null !== o.selectionStart)
                        ) {
                          const e = o.selectionStart - 1 >= 0 ? o.selectionStart - 1 : 0;
                          o.setSelectionRange(e, e);
                        }
                        e.length - 2 === r.length &&
                          o &&
                          null !== o.selectionStart &&
                          setTimeout(
                            () => o.setSelectionRange(o.selectionStart + 1, o.selectionStart + 1),
                            0,
                          );
                      } else
                        o &&
                          null !== o.selectionStart &&
                          o.setSelectionRange(o.selectionStart - 1, o.selectionStart - 1);
                    },
                    handleChangeKey: (e) => {
                      ((e.which !== H.n.DELETE && e.which !== H.n.BACKSPACE) ||
                        f(R.sounds.paragons_captcha_delete()),
                        (e.which === H.n.SPACE ||
                          e.getModifierState(H.s.CONTROL) ||
                          e.getModifierState(H.s.SHIFT)) &&
                          e.preventDefault());
                      const u = e.currentTarget,
                        t = u.selectionStart,
                        n = u.selectionEnd,
                        s = t !== n;
                      if (
                        (s &&
                          null !== t &&
                          null !== n &&
                          setTimeout(() => {
                            const e = r.split("").filter((e) => " " === e).length,
                              a = r.split("").splice(t, n - t),
                              s = e - u.value.split("").filter((e) => " " === e).length,
                              o =
                                u.value.replace(De, "").length ===
                                r.replace(De, "").length - a.join("").replace(De, "").length;
                            if (s && o) {
                              const e = t - s >= 0 ? t - s : 0;
                              a.includes(" ")
                                ? u.setSelectionRange(t, t)
                                : u.setSelectionRange(e, e);
                            } else if (!o && a.length > 1) {
                              const e =
                                r.split("").filter((e, u) => " " === e && u < t).length -
                                u.value.split("").filter((e, u) => " " === e && u < t).length;
                              if (e) u.setSelectionRange(t + 1 - e, t + 1 - e);
                              else {
                                const e = 2 === a.length && a.includes(" ") ? 2 : 1;
                                u.setSelectionRange(t + e, t + e);
                              }
                            }
                          }, 0),
                        e.which !== H.n.BACKSPACE ||
                          s ||
                          (t &&
                            " " === r[t - 1] &&
                            (e.preventDefault(),
                            a((e) => {
                              const u = Fe(e, t - 2, t);
                              return Ae(u);
                            }),
                            u.setSelectionRange(t - 2, t - 2))),
                        e.which === H.n.DELETE && !s && t && " " === r[t])
                      ) {
                        e.preventDefault();
                        const n = Fe(r, t, t + 2),
                          s = Ae(n);
                        (a(s),
                          r.length - 2 === s.length
                            ? u.setSelectionRange(t, t)
                            : u.setSelectionRange(t + 1, t + 1));
                      }
                    },
                  }
                );
              })(n, r, t.onCaptchaStateChange),
              i = a.inputValue,
              c = a.handleChange,
              m = a.handleChangeKey,
              _ = Ee(n),
              E = U.Z5.getNumberFormat(r, U.B3.INTEGRAL),
              d = u.captchaState.get(),
              A = d === V.ERROR,
              F = d === V.CONFORMITY,
              C = l()(de.base, A && de.base__error, F && de.base__conformity);
            (0, s.useEffect)(() => {
              _ && n.current && n.current.focus();
            }, [_]);
            return o().createElement(
              "div",
              { className: C },
              A && o().createElement("div", { className: de.glow }),
              o().createElement("div", { className: de.border }),
              o().createElement(y.ZP, { text: ge.header(), className: de.header }),
              o().createElement(y.ZP, { text: String(E), className: de.captchaValue }),
              o().createElement("input", {
                ref: n,
                className: l()(
                  de.input,
                  i && de.input__notEmpty,
                  A && de.input__error,
                  F && de.input__comnformity,
                ),
                type: "number",
                value: i,
                onChange: c,
                onClick: () => {
                  f(R.sounds.yes1());
                },
                onMouseEnter: () => {
                  v.playHighlight();
                },
                onKeyDown: () => m,
                maxLength: Ae(r.toString()).length,
              }),
              A &&
                o().createElement(
                  "div",
                  { className: de.warning },
                  o().createElement("div", { className: de.warningIcon }),
                  o().createElement(y.ZP, { text: ge.error(), className: de.warningText }),
                ),
              F && o().createElement("div", { className: de.conformityIcon }),
            );
          }),
          he = (e, u, t) => (t < e ? e : t > u ? u : t),
          Be = (e) => {
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
        function fe(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return ve(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return ve(e, u);
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
        function ve(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const be = [];
        function Se(e) {
          const u = (0, s.useRef)(e);
          return (
            (0, s.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, s.useCallback)((...e) => (0, u.current)(...e), be)
          );
        }
        function xe(e, u, t) {
          const n = (0, s.useMemo)(
            () =>
              (function (e, u, t, n) {
                let r,
                  a = !1,
                  s = 0;
                function o() {
                  r && clearTimeout(r);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - s;
                  function m() {
                    ((s = Date.now()), t.apply(l, i));
                  }
                  a ||
                    (n && !r && m(),
                    o(),
                    void 0 === n && c > e
                      ? m()
                      : !0 !== u &&
                        (r = setTimeout(
                          n
                            ? function () {
                                r = void 0;
                              }
                            : m,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
                  (i.cancel = function () {
                    (o(), (a = !0));
                  }),
                  i
                );
              })(t, e),
            u,
          );
          return ((0, s.useEffect)(() => n.cancel, [n]), n);
        }
        var we = t(7030);
        let Re;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Re || (Re = {}));
        const Te = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          ye = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: a = !1,
          }) => {
            const o = (e, t) => {
              const n = u(e),
                r = n[0],
                a = n[1];
              return he(r, a, t);
            };
            return (i = {}) => {
              const l = i.settings,
                c = void 0 === l ? Te : l,
                m = (0, s.useRef)(null),
                _ = (0, s.useRef)(null),
                E = (() => {
                  const e = (0, s.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    n = (e, t) => {
                      u(e).delete(t);
                    },
                    r = (e, ...t) => {
                      for (var n, r = fe(u(e).values()); !(n = r()).done;) (0, n.value)(...t);
                    };
                  return (0, s.useMemo)(() => ({ on: t, off: n, trigger: r }), []);
                })(),
                d = xe(
                  () => {
                    I.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                A = (0, we.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = m.current;
                    u && (t(u, e), E.trigger("change", e), a && d());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                F = A[0],
                C = A[1],
                D = (0, s.useCallback)(
                  (e, u, t) => {
                    var n;
                    const r = F.scrollPosition.get(),
                      a = (null != (n = F.scrollPosition.goal) ? n : 0) - r;
                    return o(e, u * t + a + r);
                  },
                  [F.scrollPosition],
                ),
                g = (0, s.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = m.current;
                    n &&
                      C.start({
                        scrollPosition: o(n, e),
                        immediate: u,
                        reset: t,
                        config: c.animationConfig,
                        from: { scrollPosition: o(n, F.scrollPosition.get()) },
                      });
                  },
                  [C, c.animationConfig, F.scrollPosition],
                ),
                p = (0, s.useCallback)(
                  (e) => {
                    const u = m.current,
                      t = _.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return r(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, c.step),
                      a = D(u, e, n);
                    g(a);
                  },
                  [g, D, c.step],
                ),
                h = (0, s.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && p(n(e)),
                      m.current && E.trigger("mouseWheel", e, F.scrollPosition, u(m.current)));
                  },
                  [F.scrollPosition, p, E],
                ),
                B = ((e, u = []) => {
                  const t = (0, s.useRef)(),
                    n = (0, s.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, s.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    Be(() => {
                      const e = m.current;
                      e &&
                        (g(o(e, F.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [g, F.scrollPosition.goal],
                ),
                f = Se(() => {
                  const e = m.current;
                  if (!e) return;
                  const u = o(e, F.scrollPosition.goal);
                  (u !== F.scrollPosition.goal && g(u, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", B),
                  () => {
                    window.removeEventListener("resize", B);
                  }
                ),
                [B],
              );
              const v = (0, s.useCallback)((e) => E.trigger("isThumbDraggingChanged", e), [E]);
              return (0, s.useMemo)(
                () => ({
                  getWrapperSize: () => (_.current ? r(_.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? u(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: c.step.clampedArrowStepTimeout,
                  clampPosition: o,
                  handleMouseWheel: h,
                  applyScroll: g,
                  applyStepTo: p,
                  contentRef: m,
                  wrapperRef: _,
                  scrollPosition: C,
                  animationScroll: F,
                  recalculateContent: f,
                  handleIsThumbDragging: v,
                  events: { on: E.on, off: E.off },
                }),
                [F.scrollPosition, g, p, v, E.off, E.on, f, h, C, c.step.clampedArrowStepTimeout],
              );
            };
          },
          Ne = ye({
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
            getDirection: (e) => (e.deltaY > 1 ? Re.Next : Re.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          Me = [
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
        function Pe(e) {
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
        const Le = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: U.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          Oe = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              a = e.onMouseLeave,
              o = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              m = e.ignoreMouseClick,
              _ = void 0 !== m && m,
              E = e.decoratorId,
              d = void 0 === E ? 0 : E,
              A = e.isEnabled,
              F = void 0 === A || A,
              C = e.targetId,
              D = void 0 === C ? 0 : C,
              g = e.onShow,
              p = e.onHide,
              h = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Me);
            const B = (0, s.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              f = (0, s.useMemo)(
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
              v = (0, s.useCallback)(() => {
                (B.current.isVisible && B.current.timeoutId) ||
                  (Le(t, d, { isMouseEvent: !0, on: !0, arguments: Pe(n) }, f),
                  g && g(),
                  (B.current.isVisible = !0));
              }, [t, d, n, f, g]),
              b = (0, s.useCallback)(() => {
                if (B.current.isVisible || B.current.timeoutId) {
                  const e = B.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (B.current.timeoutId = 0)),
                    Le(t, d, { on: !1 }, f),
                    B.current.isVisible && p && p(),
                    (B.current.isVisible = !1));
                }
              }, [t, d, f, p]),
              S = (0, s.useCallback)((e) => {
                B.current.isVisible &&
                  ((B.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (B.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(B.current.prevTarget) && b();
                  }, 200)));
              }, []);
            ((0, s.useEffect)(() => {
              const e = B.current.hideTimerId;
              return (
                document.addEventListener("wheel", S, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", S, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, s.useEffect)(() => {
                !1 === F && b();
              }, [F, b]),
              (0, s.useEffect)(
                () => (
                  window.addEventListener("mouseleave", b),
                  () => {
                    (window.removeEventListener("mouseleave", b), b());
                  }
                ),
                [b],
              ));
            return F
              ? (0, s.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((B.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            r && r(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (b(), null == a || a(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === _ && b(), null == i || i(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === _ && b(), null == o || o(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    h,
                  ),
                )
              : u;
            var x;
          },
          ke = ["children"];
        function Ie() {
          return (
            (Ie =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Ie.apply(this, arguments)
          );
        }
        const He = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, ke);
          return o().createElement(
            Oe,
            Ie(
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
        var Ue = t(5190);
        let We, Ge, $e, ze, Ve, je, Xe, qe, Ye;
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
        })(We || (We = {})),
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
          })(Ge || (Ge = {})),
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
          })($e || ($e = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(ze || (ze = {})),
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
          })(Ve || (Ve = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(je || (je = {})),
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
          })(Xe || (Xe = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(qe || (qe = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Ye || (Ye = {})));
        const Ze = {
            [oe.OptionalDevices]: "optionalDevices",
            [oe.Shells]: "shells",
            [oe.Customization]: "customization",
            [oe.Equipments]: "equipments",
            [oe.BattleBoosters]: "battleBoosters",
            [oe.Crew]: "crew",
          },
          Ke = {
            [oe.OptionalDevices]: "hangarCardModule",
            [oe.Shells]: "defaultShell",
            [oe.Customization]: "techCustomizationItem",
            [oe.Equipments]: "hangarCardModule",
            [oe.BattleBoosters]: "battleBoosterBlock",
            [oe.Crew]: "",
            VEHICLE: "awardVehicle",
          },
          Qe = (e, u) => {
            const t = R.strings.paragons.resetBranch.tooltip;
            switch (e) {
              case ie.CREDITS:
                return {
                  header: t.credits.header(),
                  description: t.credits.description(),
                  contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                };
              case ie.EQUIPMENTS:
                return {
                  header: t.returnBack.header(),
                  description: t.returnBack.description(),
                  additionalDescription: t.returnBack.additionalDescription(),
                  contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                };
              case ie.BLUEPRINTS:
                return {
                  contentId: R.views.lobby.paragons.tooltips.BlueprintUniversalTooltip("resId"),
                  vehicleCD: u,
                };
            }
          },
          Je = (e, u, t) =>
            e === oe.Crew
              ? { invID: t, contentId: R.views.lobby.crew.tooltips.TankmanTooltip("resId") }
              : { intCD: t, alias: Ke[e], vehicleCD: u },
          eu = "Frame_base_b1",
          uu = "Frame_corners_57",
          tu = "Frame_stroke_34",
          nu = "Frame_corner_08",
          ru = [
            "Frame_corner__topLeft_a0",
            "Frame_corner__topRight_12",
            "Frame_corner__bottomLeft_6e",
            "Frame_corner__bottomRight_17",
          ],
          au = (0, s.memo)(() =>
            o().createElement(
              "div",
              { className: eu },
              o().createElement(
                "div",
                { className: uu },
                ru.map((e) => o().createElement("div", { key: e, className: l()(nu, e) })),
              ),
              o().createElement("div", { className: tu }),
            ),
          ),
          su = {
            base: "Card_base_c4",
            container: "Card_container_a5",
            container__scale: "Card_container__scale_c1",
            scaleDown: "Card_scaleDown_9c",
            scaleUp: "Card_scaleUp_47",
            frame: "Card_frame_fb",
            card: "Card_card_a5",
            glow: "Card_glow_93",
            vehicle: "Card_vehicle_22",
            vehicleName: "Card_vehicleName_14",
            vehicleIcon: "Card_vehicleIcon_25",
            shadow: "Card_shadow_04",
            typeWrapper: "Card_typeWrapper_e8",
            level: "Card_level_bf",
            name: "Card_name_02",
            inner: "Card_inner_69",
            cardContent: "Card_cardContent_36",
            notInHangar: "Card_notInHangar_7e",
            vehicleNameText: "Card_vehicleNameText_f9",
          },
          ou = "DefaultCardContent_base_12",
          iu = "DefaultCardContent_pointsWrapper_2b";
        class lu extends o().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = U.B3.GOLD;
            else e = U.B3.INTEGRAL;
            const u = U.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        lu.defaultProps = { format: "integral" };
        const cu = "InfoCardContent_base_9e",
          mu = "InfoCardContent_points_a6",
          _u = "InfoCardContent_pointsBg_45",
          Eu = "InfoCardContent_count_32",
          du = "InfoCardContent_paragonIcon_79",
          Au = "InfoCardContent_pointsDescription_6e",
          Fu = R.strings.paragons.resetBranch,
          Cu = (0, s.memo)(({ progressPoints: e }) =>
            o().createElement(
              "div",
              { className: cu },
              o().createElement(
                Oe,
                {
                  contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                  args: {
                    header: Fu.tooltip.progressionPoints.header(),
                    description: Fu.tooltip.progressionPoints.description(),
                  },
                },
                o().createElement(
                  "div",
                  { className: mu },
                  o().createElement("div", { className: _u }),
                  o().createElement("div", { className: Eu }, o().createElement(lu, { value: e })),
                  o().createElement("div", { className: du }),
                ),
              ),
              o().createElement(y.ZP, { text: Fu.step1.pointsDescription(), className: Au }),
            ),
          ),
          Du = [
            We.Items,
            We.Equipment,
            We.Xp,
            We.XpFactor,
            We.Blueprints,
            We.BlueprintsAny,
            We.Goodies,
            We.Berths,
            We.Slots,
            We.Tokens,
            We.CrewSkins,
            We.CrewBooks,
            We.Customizations,
            We.CreditsFactor,
            We.TankmenXp,
            We.TankmenXpFactor,
            We.FreeXpFactor,
            We.BattleToken,
            We.PremiumUniversal,
            We.NaturalCover,
            We.BpCoin,
            We.BattlePassSelectToken,
            We.BattlaPassFinalAchievement,
            We.BattleBadge,
            We.BonusX5,
            We.CrewBonusX3,
            We.NewYearFillers,
            We.NewYearInvoice,
            We.EpicSelectToken,
            We.Comp7TokenWeeklyReward,
            We.Comp7TokenCouponReward,
            We.BattleBoosterGift,
            We.CosmicLootboxCommon,
            We.CosmicLootboxSilver,
            We.SelectableBonus,
            We.PostStamp,
            We.PremiumPlusUniversal,
            We.GoldenTicket,
            We.RewardsSlots,
            We.WtStamp,
            We.WtTicket,
            We.WtMainPrizeDiscount,
            We.WtHunter,
            We.WtHunterCollection,
          ],
          gu = [We.Gold, We.Credits, We.Crystal, We.FreeXp],
          pu = [We.BattlePassPoints],
          hu = [We.PremiumPlus, We.Premium];
        let Bu;
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
        })(Bu || (Bu = {}));
        const fu = ["engravings", "backgrounds"],
          vu = ["engraving", "background"],
          bu = (e, u = $e.Small) => {
            const t = e.name,
              n = e.type,
              r = e.value,
              a = e.icon,
              s = e.item,
              o = e.dogTagType,
              i = ((e) => {
                switch (e) {
                  case $e.S600x450:
                    return "c_600x450";
                  case $e.S400x300:
                    return "c_400x300";
                  case $e.S296x222:
                    return "c_296x222";
                  case $e.S232x174:
                    return "c_232x174";
                  case $e.Big:
                    return "c_80x80";
                  case $e.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_${r}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${r}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${r}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${s}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${a}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case $e.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case $e.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${a}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const n = fu[e];
                  if (n) {
                    const r = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(n),
                      a = r.$dyn(t);
                    return a ? `${a}` : `${r.$dyn(vu[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, u, a);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${i}.${a}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case $e.S600x450:
                      return "c_600x450";
                    case $e.S400x300:
                      return "c_400x300";
                    case $e.S296x222:
                      return "c_296x222";
                    case $e.S232x174:
                      return "c_232x174";
                    case $e.S180x135:
                      return "big";
                    case $e.Big:
                    case $e.S80x80:
                      return "c_80x80";
                    case $e.Small:
                    case $e.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${a}`;
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
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${i}.${a}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case $e.Mini:
                      return Bu.s32;
                    case $e.Small:
                    case $e.S48x48:
                      return Bu.s48;
                    case $e.S80x80:
                    case $e.Big:
                      return Bu.s80;
                    case $e.S128x100:
                      return Bu.s116;
                    case $e.S180x135:
                    case $e.S232x174:
                    case $e.S296x222:
                      return Bu.s296;
                    case $e.S400x300:
                      return Bu.s400;
                    case $e.S600x450:
                      return Bu.s600;
                  }
                })(u)}`;
              case We.StyleProgress:
              case We.LbStyleProgress:
                return Su(a, u, Ye.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          Su = (e, u, t) => {
            const n = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              r = n.$dyn(e);
            return String(null != r ? r : n.$dyn(t));
          },
          xu = ["children", "body", "header", "note", "alert", "args"];
        function wu() {
          return (
            (wu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            wu.apply(this, arguments)
          );
        }
        const Ru = R.views.common.tooltip_window.simple_tooltip_content,
          Tu = (e) => {
            let u = e.children,
              t = e.body,
              n = e.header,
              r = e.note,
              a = e.alert,
              i = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, xu);
            const c = (0, s.useMemo)(() => {
              const e = Object.assign({}, i, { body: t, header: n, note: r, alert: a });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [a, t, n, r, i]);
            return o().createElement(
              Oe,
              wu(
                {
                  contentId:
                    ((m = null == i ? void 0 : i.hasHtmlContent),
                    m ? Ru.SimpleTooltipHtmlContent("resId") : Ru.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              u,
            );
            var m;
          };
        function yu() {
          return (
            (yu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            yu.apply(this, arguments)
          );
        }
        const Nu = ({ children: e, tooltipArgs: u, className: t }) => {
            if (!u) return e;
            const n = o().createElement("div", { className: t }, e);
            if (u.header || u.body) return o().createElement(Tu, u, n);
            const r = u.contentId,
              a = u.args,
              s = null == a ? void 0 : a.contentId;
            return r || s
              ? o().createElement(Oe, yu({}, u, { contentId: r || s }), n)
              : o().createElement(He, u, n);
          },
          Mu = {
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
          Pu = ({
            name: e,
            image: u,
            isPeriodic: t = !1,
            size: n = $e.Big,
            special: r,
            value: a,
            valueType: s,
            style: i,
            className: c,
            classNames: m,
            tooltipArgs: _,
            periodicIconTooltipArgs: E,
          }) => {
            const d = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Ve.BATTLE_BOOSTER:
                  case Ve.BATTLE_BOOSTER_REPLACE:
                    return je.BATTLE_BOOSTER;
                }
              })(r),
              A = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Ve.BATTLE_BOOSTER:
                    return Xe.BATTLE_BOOSTER;
                  case Ve.BATTLE_BOOSTER_REPLACE:
                    return Xe.BATTLE_BOOSTER_REPLACE;
                  case Ve.BUILT_IN_EQUIPMENT:
                    return Xe.BUILT_IN_EQUIPMENT;
                  case Ve.EQUIPMENT_PLUS:
                    return Xe.EQUIPMENT_PLUS;
                  case Ve.EQUIPMENT_TROPHY_BASIC:
                    return Xe.EQUIPMENT_TROPHY_BASIC;
                  case Ve.EQUIPMENT_TROPHY_UPGRADED:
                    return Xe.EQUIPMENT_TROPHY_UPGRADED;
                  case Ve.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return Xe.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case Ve.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return Xe.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case Ve.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return Xe.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case Ve.PROGRESSION_STYLE_UPGRADED_1:
                    return Xe.PROGRESSION_STYLE_UPGRADED_1;
                  case Ve.PROGRESSION_STYLE_UPGRADED_2:
                    return Xe.PROGRESSION_STYLE_UPGRADED_2;
                  case Ve.PROGRESSION_STYLE_UPGRADED_3:
                    return Xe.PROGRESSION_STYLE_UPGRADED_3;
                  case Ve.PROGRESSION_STYLE_UPGRADED_4:
                    return Xe.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(r),
              F = ((e, u) => {
                if (void 0 === e) return null;
                switch (u) {
                  case ze.MULTI: {
                    const u = Number(e);
                    return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
                  }
                  case ze.CURRENCY:
                  case ze.NUMBER:
                    return o().createElement(lu, { format: "integral", value: Number(e) });
                  case ze.PREMIUM_PLUS: {
                    const u = Number(e);
                    return isNaN(u) ? e : null;
                  }
                  default:
                    return e;
                }
              })(a, s);
            return o().createElement(
              "div",
              { className: l()(Mu.base, Mu[`base__${n}`], c), style: i },
              o().createElement(
                Nu,
                { tooltipArgs: _, className: Mu.tooltipWrapper },
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement(
                    "div",
                    { className: l()(Mu.image, null == m ? void 0 : m.image) },
                    d &&
                      o().createElement("div", {
                        className: l()(Mu.highlight, null == m ? void 0 : m.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${d}_highlight)`,
                        },
                      }),
                    u &&
                      o().createElement("div", {
                        className: l()(Mu.icon, null == m ? void 0 : m.rewardIcon),
                        style: { backgroundImage: `url(${u})` },
                      }),
                    A &&
                      o().createElement("div", {
                        className: l()(Mu.overlay, null == m ? void 0 : m.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${A}_overlay)`,
                        },
                      }),
                  ),
                  F &&
                    o().createElement(
                      "div",
                      {
                        className: l()(
                          Mu.info,
                          Mu[`info__${e}`],
                          s === ze.MULTI && Mu.info__multi,
                          null == m ? void 0 : m.info,
                        ),
                      },
                      F,
                    ),
                ),
              ),
              t &&
                o().createElement(
                  Nu,
                  { tooltipArgs: E },
                  o().createElement("div", {
                    className: l()(Mu.timer, null == m ? void 0 : m.periodicIcon),
                  }),
                ),
            );
          };
        var Lu = t(3649);
        let Ou;
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
        })(Ou || (Ou = {}));
        Date.now();
        const ku = [We.Branch, We.VehicleSelect, We.ParagonsUnlocks, We.StyleProgress],
          Iu =
            (R.strings.paragons.seasonsProgression.timeLeft,
            (e, u = $e.Small) => {
              const t = (0, Lu.BN)(e.vehicleName || "");
              if (e.name === We.Vehicles)
                switch (u) {
                  case $e.Mini:
                  case $e.Small:
                  case $e.S48x48:
                    return e.isRent
                      ? "R.images.gui.maps.icons.quests.bonuses.small.vehicles_rent"
                      : `R.images.gui.maps.icons.quests.bonuses.small.${t}`;
                  case $e.Big:
                  case $e.S80x80:
                    return e.isRent
                      ? "R.images.gui.maps.icons.quests.bonuses.big.vehicles_rent"
                      : `R.images.gui.maps.icons.quests.bonuses.big.${t}`;
                  case $e.S128x100:
                  case $e.S180x135:
                    return `R.images.gui.maps.shop.vehicles.c_180x135.${t}`;
                  case $e.S232x174:
                  case $e.S296x222:
                    return `R.images.gui.maps.shop.vehicles.c_360x270.${t}`;
                  case $e.S400x300:
                  case $e.S600x450:
                    return `R.images.gui.maps.shop.vehicles.c_600x450.${t}`;
                  default:
                    return (
                      console.error("Unknown vehicle image size", u, e.vehicleName),
                      "R.images.gui.maps.icons.quests.bonuses.big.vehicles"
                    );
                }
              if (e.name === We.TmanToken)
                switch (u) {
                  case $e.Mini:
                  case $e.Small:
                  case $e.S48x48:
                  case $e.Big:
                  case $e.S80x80:
                    return `R.images.gui.maps.icons.tankmen.icons.s80x80.${e.icon}`;
                  case $e.S128x100:
                  case $e.S180x135:
                  case $e.S232x174:
                    return `R.images.gui.maps.icons.tankmen.icons.s232x174.${e.icon}`;
                  case $e.S296x222:
                    return `R.images.gui.maps.icons.tankmen.icons.s296x222.${e.icon}`;
                  case $e.S400x300:
                    return `R.images.gui.maps.icons.tankmen.icons.s400x300.${e.icon}`;
                  case $e.S600x450:
                    return `R.images.gui.maps.icons.tankmen.icons.s600x450.${e.icon}`;
                  default:
                    return (
                      console.error("Unknown image size", u),
                      "R.images.gui.maps.icons.tankmen.icons.s600x450.tankman"
                    );
                }
              if (e.name === We.CollectionItem)
                switch (u) {
                  case $e.Mini:
                  case $e.Small:
                  case $e.S48x48:
                    return `R.images.gui.maps.icons.collectionItems.c_48x48.${e.icon}`;
                  case $e.Big:
                  case $e.S80x80:
                    return `R.images.gui.maps.icons.collectionItems.c_80x80.${e.icon}`;
                  case $e.S128x100:
                  case $e.S180x135:
                  case $e.S232x174:
                    return `R.images.gui.maps.icons.collectionItems.c_232x174.${e.icon}`;
                  case $e.S296x222:
                    return `R.images.gui.maps.icons.collectionItems.c_296x222.${e.icon}`;
                  case $e.S400x300:
                    return `R.images.gui.maps.icons.collectionItems.c_400x300.${e.icon}`;
                  case $e.S600x450:
                    return `R.images.gui.maps.icons.collectionItems.c_600x450.${e.icon}`;
                  default:
                    console.error("Unknown image size", u);
                }
              if (e.name === We.StyleProgress)
                switch (u) {
                  case $e.Small:
                  case $e.Big:
                    return `R.images.gui.maps.icons.quests.bonuses.${u}.progressionStyle`;
                  default:
                    return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                }
              if (ku.includes(e.name))
                switch (e.name) {
                  case "branch":
                  case "vehicleSelect":
                  case "paragonsUnlocks":
                    return `R.images.gui.maps.icons.paragons.allRewards.${u}.${e.icon}`;
                  default:
                    return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                }
              return bu(e, u);
            }),
          Hu = "ReturnValueContent_base_be",
          Uu = "ReturnValueContent_return_05",
          Wu = "ReturnValueContent_line_e7",
          Gu = "ReturnValueContent_line__right_b6",
          $u = "ReturnValueContent_returnBack_40",
          zu = "ReturnValueContent_arrowDown_16",
          Vu = "ReturnValueContent_list_4a",
          ju = "ReturnValueContent_btnContainer_42",
          Xu = "ReturnValueContent_btn_43",
          qu = R.strings.paragons.resetBranch,
          Yu = (0, s.memo)(({ returnedItemsShort: e, vehicleCD: u, onOpenDetails: t }) => {
            const n = (0, _.GS)().mediaSize <= _.cJ.Medium ? $e.Small : $e.Big;
            return o().createElement(
              "div",
              { className: Hu },
              o().createElement(
                "div",
                { className: Uu },
                o().createElement("div", { className: Wu }),
                o().createElement(y.ZP, { text: qu.step2.returnBack(), className: $u }),
                o().createElement("div", { className: l()(Wu, Gu) }),
                o().createElement("div", { className: zu }),
              ),
              o().createElement(
                "div",
                { className: Vu },
                e.map((e, t) => {
                  return o().createElement(Pu, {
                    name: e.name,
                    image: Iu(e, n),
                    value: String(e.value),
                    size: n,
                    valueType:
                      ((r = e.type),
                      Du.includes(r)
                        ? ze.MULTI
                        : gu.includes(r)
                          ? ze.CURRENCY
                          : pu.includes(r)
                            ? ze.NUMBER
                            : hu.includes(r)
                              ? ze.PREMIUM_PLUS
                              : ze.STRING),
                    key: `${e.name}_${t}`,
                    tooltipArgs: { args: Qe(e.name, u) },
                  });
                  var r;
                }),
              ),
              e.length > 1 &&
                o().createElement(
                  "div",
                  { className: ju },
                  o().createElement(
                    T,
                    {
                      type: S.ghost,
                      size: x.medium,
                      mixClass: Xu,
                      onClick: t,
                      onMouseDown: (e) => {
                        e.stopPropagation();
                      },
                    },
                    o().createElement(y.ZP, { text: qu.step2.details() }),
                  ),
                ),
            );
          }),
          Zu = (0, s.memo)(
            ({
              currentStep: e,
              progressPoints: u,
              returnedItemsShort: t,
              vehicleCD: n,
              onOpenDetails: r,
            }) =>
              o().createElement(
                "div",
                { className: ou },
                e === se.INFO
                  ? o().createElement(
                      "div",
                      { className: iu },
                      o().createElement(Cu, { progressPoints: u }),
                    )
                  : o().createElement(Yu, {
                      returnedItemsShort: t,
                      vehicleCD: n,
                      onOpenDetails: r,
                    }),
              ),
          );
        function Ku(e, u, t = []) {
          const n = (0, s.useRef)(0),
            r = (0, s.useCallback)(() => window.clearInterval(n.current), t || []);
          (0, s.useEffect)(() => r, [r]);
          const a = (null != t ? t : []).concat([u]);
          return [
            (0, s.useCallback)((t) => {
              ((n.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, a),
            r,
          ];
        }
        const Qu = "HorizontalBar_base_49",
          Ju = "HorizontalBar_base__nonActive_82",
          et = "HorizontalBar_leftButton_5f",
          ut = "HorizontalBar_rightButton_03",
          tt = "HorizontalBar_track_0d",
          nt = "HorizontalBar_thumb_fd",
          rt = "HorizontalBar_rail_32",
          at = "disable",
          st = { pending: !1, offset: 0 },
          ot = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          it = () => {},
          lt = (e, u) => Math.max(20, e.offsetWidth * u),
          ct = (0, s.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = ot, onDrag: n = it }) => {
              const r = (0, s.useRef)(null),
                a = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                _ = e.stepTimeout || 100,
                E = (0, s.useState)(st),
                d = E[0],
                A = E[1],
                F = (0, s.useCallback)(
                  (e) => {
                    (A(e),
                      m.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [n],
                ),
                C = () => {
                  const u = c.current,
                    t = m.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / r),
                    l = he(0, 1, s / (r - n)),
                    _ = (u.offsetWidth - lt(u, o)) * l;
                  ((t.style.transform = `translateX(${0 | _}px)`),
                    ((e) => {
                      if (a.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (a.current.classList.add(at), void i.current.classList.remove(at));
                        if (
                          ((u = c.current),
                          (t = m.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (a.current.classList.remove(at), void i.current.classList.add(at));
                        var u, t;
                        (a.current.classList.remove(at), i.current.classList.remove(at));
                      }
                    })(_));
                },
                D = Se(() => {
                  ((() => {
                    const u = m.current,
                      t = c.current,
                      n = e.getWrapperSize(),
                      a = e.getContainerSize();
                    if (!(a && u && n && t)) return;
                    const s = Math.min(1, n / a);
                    ((u.style.width = `${lt(t, s)}px`),
                      (u.style.display = "flex"),
                      r.current &&
                        (1 === s ? r.current.classList.add(Ju) : r.current.classList.remove(Ju)));
                  })(),
                    C());
                });
              ((0, s.useEffect)(() => Be(D)),
                (0, s.useEffect)(
                  () =>
                    Be(() => {
                      const u = () => {
                        C();
                      };
                      let t = it;
                      const n = () => {
                        (t(), (t = Be(D)));
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
                    }),
                  [e],
                ),
                (0, s.useEffect)(() => {
                  if (!d.pending) return;
                  const u = (u) => {
                      var t;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const a = c.current,
                        s = m.current;
                      if (!r || !a || !s) return;
                      const o = u.screenX - d.offset - a.getBoundingClientRect().x,
                        i = (o / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), F(st));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, d.offset, d.pending, n, F]));
              const g = Ku((u) => e.applyStepTo(u), _, [e]),
                p = g[0],
                h = g[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const B = (e) => {
                e.target.classList.contains(at) || f("highlight");
              };
              return o().createElement(
                "div",
                { className: l()(Qu, u.base), ref: r, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: l()(et, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(at) || 0 !== e.button || (f("play"), p(Re.Next));
                  },
                  onMouseUp: h,
                  ref: a,
                  onMouseEnter: B,
                }),
                o().createElement(
                  "div",
                  {
                    className: l()(tt, u.track),
                    onMouseDown: (u) => {
                      const n = m.current;
                      if (n && 0 === u.button)
                        if ((f("play"), u.target === n))
                          F({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = m.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const a = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * u);
                          })(u.screenX > n.getBoundingClientRect().x ? Re.Prev : Re.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: B,
                  },
                  o().createElement("div", { ref: m, className: l()(nt, u.thumb) }),
                  o().createElement("div", { className: l()(rt, u.rail) }),
                ),
                o().createElement("div", {
                  className: l()(ut, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(at) || 0 !== e.button || (f("play"), p(Re.Prev));
                  },
                  onMouseUp: h,
                  ref: i,
                  onMouseEnter: B,
                }),
              );
            },
          ),
          mt = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          _t = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            classNames: a,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const _ = (0, s.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: l()(mt.base, e.base) });
              }, [n]),
              E = (0, s.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return o().createElement(
              "div",
              { className: l()(mt.defaultScroll, t), onWheel: u.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(mt.defaultScrollArea, r) },
                o().createElement(Et, { className: i, api: E, classNames: a }, e),
              ),
              o().createElement(ct, { getStepByRailClick: c, api: u, onDrag: m, classNames: _ }),
            );
          },
          Et = ({ api: e, className: u, classNames: t, children: n, style: r }) => (
            (0, s.useEffect)(() => Be(e.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(mt.base, u), style: r },
              o().createElement(
                "div",
                {
                  className: l()(mt.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: l()(mt.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((Et.Bar = ct),
          (Et.Default = _t),
          (Et.SeniorityAwards = ({ api: e, className: u, classNames: t, children: n }) => (
            (0, s.useEffect)(() => Be(e.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(mt.base, u) },
              o().createElement(
                "div",
                { className: l()(mt.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: l()(mt.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const dt = ye({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Re.Next : Re.Prev),
          }),
          At = "VerticalBar_base_f3",
          Ft = "VerticalBar_base__nonActive_42",
          Ct = "VerticalBar_topButton_d7",
          Dt = "VerticalBar_bottomButton_06",
          gt = "VerticalBar_track_df",
          pt = "VerticalBar_thumb_32",
          ht = "VerticalBar_rail_43",
          Bt = "disable",
          ft = () => {},
          vt = { pending: !1, offset: 0 },
          bt = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          St = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          xt = (e, u) => Math.max(20, e.offsetHeight * u),
          wt = (0, s.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = bt, onDrag: n = ft }) => {
              const r = (0, s.useRef)(null),
                a = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                _ = e.stepTimeout || 100,
                E = (0, s.useState)(vt),
                d = E[0],
                A = E[1],
                F = (0, s.useCallback)(
                  (e) => {
                    (A(e),
                      m.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [n],
                ),
                C = Se(() => {
                  const u = m.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && a && u && t)) return;
                  const s = Math.min(1, n / a);
                  return (
                    (u.style.height = `${xt(t, s)}px`),
                    u.classList.add(pt),
                    r.current &&
                      (1 === s ? r.current.classList.add(Ft) : r.current.classList.remove(Ft)),
                    s
                  );
                }),
                D = Se(() => {
                  const u = c.current,
                    t = m.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / r),
                    l = he(0, 1, s / (r - n)),
                    _ = (u.offsetHeight - xt(u, o)) * l;
                  ((t.style.transform = `translateY(${0 | _}px)`),
                    ((e) => {
                      if (a.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (a.current.classList.add(Bt), void i.current.classList.remove(Bt));
                        if (
                          ((u = c.current),
                          (t = m.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (a.current.classList.remove(Bt), void i.current.classList.add(Bt));
                        var u, t;
                        (a.current.classList.remove(Bt), i.current.classList.remove(Bt));
                      }
                    })(_));
                }),
                g = Se(() => {
                  St(e, () => {
                    (C(), D());
                  });
                });
              ((0, s.useEffect)(() => Be(g)),
                (0, s.useEffect)(() => {
                  const u = () => {
                    St(e, () => {
                      D();
                    });
                  };
                  let t = ft;
                  const n = () => {
                    (t(), (t = Be(g)));
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
                (0, s.useEffect)(() => {
                  if (!d.pending) return;
                  const u = (u) => {
                      St(e, (t) => {
                        const r = c.current,
                          a = m.current,
                          s = e.getContainerSize();
                        if (!r || !a || !s) return;
                        const o = u.screenY - d.offset - r.getBoundingClientRect().y,
                          i = (o / r.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: a, thumbOffset: o, contentOffset: i }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        F(vt));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, d.offset, d.pending, n, F]));
              const p = Ku((u) => e.applyStepTo(u), _, [e]),
                h = p[0],
                B = p[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", B, !0),
                  () => document.removeEventListener("mouseup", B, !0)
                ),
                [B],
              );
              const v = (e) => {
                e.target.classList.contains(Bt) || f("highlight");
              };
              return o().createElement(
                "div",
                { className: l()(At, u.base), ref: r, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: l()(Ct, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Bt) || 0 !== e.button || (f("play"), h(Re.Next));
                  },
                  ref: a,
                  onMouseEnter: v,
                }),
                o().createElement(
                  "div",
                  {
                    className: l()(gt, u.track),
                    onMouseDown: (u) => {
                      const n = m.current;
                      if (n && 0 === u.button)
                        if ((f("play"), u.target === n))
                          (e.handleIsThumbDragging(!0),
                            F({ pending: !0, offset: u.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            m.current &&
                              St(e, (n) => {
                                if (!n) return;
                                const r = t(e),
                                  a = e.clampPosition(n, n.scrollTop + r * u);
                                e.applyScroll(a);
                              });
                          })(u.screenY > n.getBoundingClientRect().y ? Re.Prev : Re.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: v,
                  },
                  o().createElement("div", { ref: m, className: u.thumb }),
                  o().createElement("div", { className: l()(ht, u.rail) }),
                ),
                o().createElement("div", {
                  className: l()(Dt, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Bt) || 0 !== e.button || (f("play"), h(Re.Prev));
                  },
                  onMouseUp: B,
                  ref: i,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          Rt = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Tt = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: a,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const _ = (0, s.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: l()(Rt.base, e.base) });
              }, [n]),
              E = (0, s.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return o().createElement(
              "div",
              { className: l()(Rt.defaultScroll, t), onWheel: u.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Rt.area, r) },
                o().createElement(yt, { className: a, classNames: i, api: E }, e),
              ),
              o().createElement(wt, { getStepByRailClick: c, api: u, onDrag: m, classNames: _ }),
            );
          },
          yt = ({ className: e, classNames: u, children: t, api: n }) => (
            (0, s.useEffect)(() => Be(n.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Rt.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Rt.content, null == u ? void 0 : u.content), ref: n.contentRef },
                t,
              ),
            )
          );
        yt.Default = Tt;
        const Nt = { Vertical: r, Horizontal: n },
          Mt = "ReversedCardContent_base_7c",
          Pt = "ReversedCardContent_header_5e",
          Lt = "ReversedCardContent_close_54",
          Ot = "ReversedCardContent_closeHover_f8",
          kt = "ReversedCardContent_closeContainer_3e",
          It = "ReversedCardContent_scrollWrapper_1a",
          Ht = "ReversedCardContent_scrollArea_f4",
          Ut = "ReversedCardContent_scrollBase_89",
          Wt = "ReversedCardContent_divider_b0",
          Gt = "ReversedCardContent_divider__top_f7",
          $t = "ReversedCardContent_divider__bottom_f4",
          zt = "ReversedCardContent_group_79",
          Vt = {
            title: "RewardType_title_7d",
            list: "RewardType_list_9d",
            rewardOverlay: "RewardType_rewardOverlay_2f",
            rewardOverlay__equipmentPlus: "RewardType_rewardOverlay__equipmentPlus_38",
            reward: "RewardType_reward_2e",
          },
          jt = R.strings.paragons.resetBranch,
          Xt = (0, s.memo)(({ type: e, isSmall: u, groupInfo: t, imageSize: n, vehicleCD: r }) => {
            const a = ((e, u) => {
              const t = R.images.gui.maps.icons;
              switch (e) {
                case oe.Customization:
                case oe.Equipments:
                case oe.BattleBoosters:
                case oe.OptionalDevices:
                case oe.Crew:
                  return u ? t.quests.bonuses.small : t.quests.bonuses.big;
                case oe.Shells:
                  return u ? t.shell.small : t.shell.medium;
                default:
                  return "";
              }
            })(e, u);
            return o().createElement(
              o().Fragment,
              null,
              o().createElement(y.ZP, {
                text: String(jt.returnBack.$dyn(Ze[e])),
                className: Vt.title,
              }),
              o().createElement(
                "div",
                { className: Vt.list },
                t.map((u, t) => {
                  const s = a.$dyn(u.icon);
                  return o().createElement(Pu, {
                    image: String(s),
                    name: u.name,
                    value: String(u.count),
                    valueType: ze.MULTI,
                    key: `${u.name}_${t}`,
                    size: n,
                    classNames: {
                      overlay: l()(Vt.rewardOverlay, Vt[`rewardOverlay__${u.overlayIcon}`]),
                    },
                    special: u.overlayIcon,
                    className: Vt.reward,
                    tooltipArgs: { args: Je(e, r, u.intCD) },
                  });
                }),
              ),
            );
          }),
          qt = { type: "idle" };
        const Yt = R.strings.paragons.resetBranch,
          Zt = (0, s.memo)(({ returnedItems: e, onClose: u, vehicleCD: t }) => {
            const n = (0, s.useState)(!1),
              r = n[0],
              a = n[1],
              i = (0, _.GS)().mediaSize <= _.cJ.Medium,
              c = i ? $e.Small : $e.Big,
              m = Nt.Vertical.useVerticalScrollApi(),
              E = m.getContainerSize,
              d = m.getWrapperSize,
              A = (0, s.useRef)(null),
              F = Ee(A),
              C = d(),
              D = E(),
              g = (e) => e.stopPropagation();
            return (
              (function (e, u) {
                const t = e.contentRef,
                  n = e.wrapperRef,
                  r = e.scrollPosition,
                  a = e.clampPosition,
                  o = e.animationScroll,
                  i = e.events,
                  l = (0, s.useState)(qt),
                  c = l[0],
                  m = l[1];
                ((0, s.useEffect)(() => {
                  const e = t.current;
                  e && (e.style.cursor = "dragging" === c.type ? "grabbing" : "grab");
                }, [t, c.type]),
                  (0, s.useEffect)(() => {
                    if ("dragging" !== c.type) return;
                    const e = (e) => {
                        const s = t.current,
                          i = n.current;
                        if (!s || !i) return;
                        const l = c.positionFrom - e.screenY,
                          m = c.previousScrollPosition + l;
                        r.start(
                          Object.assign(
                            {
                              scrollPosition: a(s, m),
                              from: { scrollPosition: o.scrollPosition.get() },
                            },
                            u && { config: u },
                          ),
                        );
                      },
                      s = () => {
                        (window.removeEventListener("mousemove", e), m({ type: "scrollingToEnd" }));
                      };
                    return (
                      window.addEventListener("mousemove", e),
                      window.addEventListener("mouseup", s),
                      () => {
                        (window.removeEventListener("mousemove", e),
                          window.removeEventListener("mouseup", s));
                      }
                    );
                  }, [o.scrollPosition, a, t, c, r, n, u]),
                  (0, s.useEffect)(() => {
                    if ("scrollingToEnd" !== c.type) return;
                    const e = () => {
                      m(qt);
                    };
                    return (o.scrollPosition.idle && e(), i.on("rest", e), () => i.off("rest", e));
                  }, [o.scrollPosition, c.type, i]),
                  (0, s.useEffect)(() => {
                    const e = t.current;
                    if (!e) return;
                    const u = (e) => {
                      (e.stopPropagation(),
                        0 === e.button &&
                          m({
                            type: "dragging",
                            positionFrom: e.screenY,
                            previousScrollPosition: o.scrollPosition.get(),
                          }));
                    };
                    return (
                      e.addEventListener("mousedown", u),
                      () => e.removeEventListener("mousedown", u)
                    );
                  }, [o.scrollPosition, t]));
              })(m),
              (0, s.useEffect)(() => {
                C && D && C < D && a(!0);
              }, [F, D, C]),
              (0, s.useEffect)(() => {
                if (r) return (m.events.on("mouseWheel", g), () => m.events.off("mouseWheel", g));
              }, [r, m]),
              m.events.on("resizeHandled", () => {
                const e = d(),
                  u = E();
                if (e && u) {
                  a(u > e);
                } else a(!1);
              }),
              o().createElement(
                "div",
                { className: Mt },
                o().createElement(y.ZP, { text: Yt.returnBack.header(), className: Pt }),
                o().createElement(
                  "div",
                  {
                    className: kt,
                    onClick: u,
                    onMouseDown: g,
                    onMouseEnter: () => {
                      v.playHighlight();
                    },
                  },
                  o().createElement("div", { className: Lt }),
                  o().createElement("div", { className: Ot }),
                ),
                o().createElement(
                  "div",
                  { className: It },
                  o().createElement("div", { className: l()(Wt, Gt) }),
                  o().createElement(
                    Nt.Vertical.Area.Default,
                    {
                      api: m,
                      scrollClassNames: { content: r ? "" : Ht },
                      barClassNames: { base: r ? "" : Ut },
                    },
                    o().createElement(
                      "div",
                      { className: zt, ref: A },
                      e
                        .filter(({ groupInfo: e }) => e.length)
                        .map(({ type: e, groupInfo: u }, n) =>
                          o().createElement(Xt, {
                            key: `rewardType_${e}_${n}`,
                            type: e,
                            isSmall: i,
                            groupInfo: u,
                            imageSize: c,
                            vehicleCD: t,
                          }),
                        ),
                    ),
                  ),
                  o().createElement("div", { className: l()(Wt, $t) }),
                ),
              )
            );
          }),
          Kt = R.images.gui.maps.shop.vehicles.c_360x270,
          Qt = R.strings.paragons.resetBranch,
          Jt = (0, s.memo)(({ currentStep: e, resetVehicleInfo: u, index: t, realStep: n }) => {
            const r = (0, s.useState)(!1),
              a = r[0],
              i = r[1],
              c = (0, s.useState)(!1),
              m = c[0],
              _ = c[1],
              E = (0, s.useState)(!1),
              d = E[0],
              A = E[1],
              F = u.vehicleInfo,
              C = u.blueprintFragments,
              D = u.credits,
              g = u.returnedItems,
              p = u.progressPoints,
              h = F.name,
              B = F.techName,
              b = F.tier,
              S = F.type,
              x = F.isPremium,
              w = F.vehicleCD,
              T = e === se.CAPTCHA,
              N = n === se.CAPTCHA,
              M = (0, s.useMemo)(
                () => ((e) => e.reduce((e, u) => e + u.groupInfo.length, 0))(g),
                [g],
              ),
              P = (0, s.useMemo)(
                () =>
                  ((e, u, t) => {
                    const n = [{ name: "credits", value: e, icon: "credits", type: We.Credits }];
                    return (
                      0 !== u &&
                        n.push({
                          name: "equipment",
                          value: u,
                          icon: "equipment",
                          type: We.Equipment,
                        }),
                      0 !== t &&
                        n.push({
                          name: "finalBlueprints",
                          value: t,
                          icon: "vehicle",
                          type: We.Blueprints,
                        }),
                      n
                    );
                  })(D, M, C),
                [D, M, C],
              ),
              L = $();
            ((0, s.useEffect)(() => {
              ((e === se.INFO && a) || T) && i(!1);
            }, [e, a, T]),
              (0, s.useEffect)(() => {
                if ((e !== n || a !== m) && !N)
                  return (
                    A(!0),
                    k(() => {
                      A(!1);
                    }, 2 * jr)
                  );
              }, [e]),
              (0, s.useEffect)(() => {
                if (e !== se.INFO && !L)
                  return (
                    A(!0),
                    k(() => {
                      A(!1);
                    }, 2 * jr)
                  );
              }, [a]),
              (0, s.useEffect)(
                () =>
                  k(() => {
                    _(a);
                  }, jr),
                [a],
              ));
            const O = (0, s.useCallback)(() => {
                (i(!0), f(R.sounds.paragons_card_turn()));
              }, []),
              I = (0, s.useCallback)(() => {
                (i(!1), v.playClick(), f(R.sounds.paragons_card_turn()));
              }, []);
            return o().createElement(
              "div",
              { className: su.base },
              o().createElement(
                "div",
                { className: l()(su.container, d && !N && su.container__scale) },
                o().createElement(
                  "div",
                  { className: l()(su.card, !N && su[`card__extend__${t}`]) },
                  o().createElement("div", { className: su.frame }, o().createElement(au, null)),
                  !m &&
                    o().createElement(
                      "div",
                      { className: su.cardContent },
                      o().createElement("div", { className: su.shadow }),
                      o().createElement(
                        "div",
                        { className: su.vehicle },
                        o().createElement(
                          He,
                          { args: { alias: Ke.VEHICLE, vehicleCD: w } },
                          o().createElement("div", {
                            className: su.vehicleIcon,
                            style: { backgroundImage: `url(${Kt.$dyn(B)})` },
                          }),
                        ),
                      ),
                      o().createElement(Ue.M2, {
                        vehicleName: h,
                        vehicleLvl: b,
                        vehicleType: S,
                        isElite: x,
                        size: Ue.uA.Medium,
                        className: su.vehicleNameText,
                      }),
                      0 === D && n !== se.INFO
                        ? o().createElement(y.ZP, {
                            className: su.notInHangar,
                            text: Qt.step2.notInHangar(),
                          })
                        : o().createElement(Zu, {
                            currentStep: n,
                            progressPoints: p,
                            onOpenDetails: O,
                            returnedItemsShort: P,
                            vehicleCD: w,
                          }),
                    ),
                  m &&
                    o().createElement(
                      "div",
                      { className: su.cardContent },
                      o().createElement(Zt, { returnedItems: g, onClose: I, vehicleCD: w }),
                    ),
                ),
              ),
            );
          }),
          en = { type: "idle" };
        const un = "HorizontalDrag_base_fa",
          tn = "HorizontalDrag_base__withoutScroll_56",
          nn = "HorizontalDrag_base__shadowBoth_9e",
          rn = "HorizontalDrag_content_ab",
          an = (0, s.memo)(
            ({ children: e, scroll: u, cardListApi: t }) => (
              (function (e, u, t) {
                const n = e.contentRef,
                  r = e.wrapperRef,
                  a = e.scrollPosition,
                  o = e.clampPosition,
                  i = e.animationScroll,
                  l = e.events,
                  c = (0, s.useState)(en),
                  m = c[0],
                  _ = c[1];
                ((0, s.useEffect)(() => {
                  const e = n.current;
                  e && (e.style.cursor = "dragging" === m.type ? "move" : "grab");
                }, [n, m.type]),
                  (0, s.useEffect)(() => {
                    if ("dragging" !== m.type) return;
                    const e = I.O.client.events.mouse.move(([e, t]) => {
                        const s = n.current,
                          l = r.current;
                        if (!s || !l) return;
                        if ("inside" === t && e.clientX < 0) return;
                        const c = "inside" === t ? e.clientX : e.clientX - l.offsetLeft,
                          _ = m.positionFrom - c,
                          E = m.previousScrollPosition + _;
                        a.start(
                          Object.assign(
                            {
                              scrollPosition: o(s, E),
                              from: { scrollPosition: i.scrollPosition.get() },
                            },
                            u && { config: u },
                          ),
                        );
                      }),
                      t = I.O.client.events.mouse.up(function () {
                        _({ type: "scrollingToEnd" });
                      });
                    return () => {
                      (e(), t());
                    };
                  }, [i.scrollPosition, o, n, m, a, r, u]),
                  (0, s.useEffect)(() => {
                    if ("scrollingToEnd" !== m.type) return;
                    const e = () => {
                      _(en);
                    };
                    return (i.scrollPosition.idle && e(), l.on("rest", e), () => l.off("rest", e));
                  }, [i.scrollPosition, m.type, l]),
                  (0, s.useEffect)(() => {
                    const e = n.current;
                    if (!e) return;
                    const u = (e) => {
                      (t &&
                        t.allowedButtons &&
                        -1 === t.allowedButtons.findIndex((u) => e.button === u)) ||
                        _({
                          type: "dragging",
                          positionFrom: e.screenX,
                          previousScrollPosition: i.scrollPosition.get(),
                        });
                    };
                    return (
                      e.addEventListener("mousedown", u),
                      () => e.removeEventListener("mousedown", u)
                    );
                  }, [i.scrollPosition, n, t]));
              })(t),
              o().createElement(
                Nt.Horizontal.Area,
                { api: t, classNames: { wrapper: l()(un, !u && tn, u && nn), content: rn } },
                e,
              )
            ),
          ),
          sn = {
            base: "MiniCard_base_96",
            container: "MiniCard_container_b1",
            card: "MiniCard_card_26",
            glow: "MiniCard_glow_16",
            corner: "MiniCard_corner_4b",
            vehicle: "MiniCard_vehicle_b2",
            vehicleIcon: "MiniCard_vehicleIcon_11",
            shadow: "MiniCard_shadow_60",
            typeWrapper: "MiniCard_typeWrapper_14",
            level: "MiniCard_level_c6",
            name: "MiniCard_name_01",
            inner: "MiniCard_inner_26",
            cardContent: "MiniCard_cardContent_d3",
            vehicleNameContainer: "MiniCard_vehicleNameContainer_d1",
            vehicleNameText: "MiniCard_vehicleNameText_08",
            vehicleNameText__medium: "MiniCard_vehicleNameText__medium_91",
          },
          on = R.images.gui.maps.shop.vehicles.c_360x270,
          ln = (0, s.memo)(({ resetVehicleInfo: e }) => {
            const u = (0, _.GS)().mediaSize,
              t = e.vehicleInfo,
              n = t.techName,
              r = t.vehicleCD,
              a = u <= _.cJ.Medium ? Ue.uA.Small : Ue.uA.Medium;
            return o().createElement(
              "div",
              { className: sn.base },
              o().createElement(
                "div",
                { className: sn.container },
                o().createElement(
                  "div",
                  { className: sn.card },
                  o().createElement(au, null),
                  o().createElement(
                    "div",
                    { className: sn.cardContent },
                    o().createElement("div", { className: sn.glow }),
                    o().createElement("div", { className: sn.shadow }),
                    o().createElement(
                      "div",
                      { className: sn.vehicle },
                      o().createElement(
                        He,
                        { args: { alias: Ke.VEHICLE, vehicleCD: r } },
                        o().createElement("div", {
                          className: sn.vehicleIcon,
                          style: { backgroundImage: `url(${on.$dyn(n)})` },
                        }),
                      ),
                    ),
                    o().createElement(
                      "div",
                      { className: sn.vehicleNameContainer },
                      o().createElement(Ue.M2, {
                        vehicleLvl: t.tier,
                        size: a,
                        vehicleName: t.name,
                        vehicleType: t.type,
                        isElite: t.isPremium,
                        className: l()(sn.vehicleNameText, sn[`vehicleNameText__${a}`]),
                      }),
                    ),
                  ),
                ),
              ),
            );
          }),
          cn = {
            base: "CardList_base_ba",
            animation: "CardList_animation_33",
            cardList: "CardList_cardList_15",
            cardList__captchaStep: "CardList_cardList__captchaStep_14",
            cardList__hidden: "CardList_cardList__hidden_43",
            cardWrapper: "CardList_cardWrapper_f4",
            module: "CardList_module_c0",
          };
        let mn;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(mn || (mn = {}));
        const _n = {
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
        let En, dn, An;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(En || (En = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(dn || (dn = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(An || (An = {})));
        const Fn = [
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
        function Cn() {
          return (
            (Cn =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Cn.apply(this, arguments)
          );
        }
        const Dn = (e) => {
            let u = e.id,
              t = e.isChecked,
              n = void 0 !== t && t,
              r = e.isDisabled,
              a = void 0 !== r && r,
              i = e.isAlert,
              c = void 0 !== i && i,
              m = e.size,
              _ = void 0 === m ? En.medium : m,
              E = e.type,
              d = void 0 === E ? dn.primary : E,
              A = e.soundHover,
              F = void 0 === A ? "highlight" : A,
              C = e.soundClick,
              D = void 0 === C ? "play" : C,
              g = e.onMouseEnter,
              p = e.onMouseLeave,
              h = e.onMouseUp,
              B = e.onMouseDown,
              v = e.onClick,
              b = e.onChange,
              S = e.onFocus,
              x = e.onBlur,
              w = e.text,
              R = e.contentStyles,
              T = e.children,
              y = e.alignment,
              N = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Fn);
            const M = (0, s.useState)(!1),
              P = M[0],
              L = M[1],
              O = (0, s.useState)(!1),
              k = (O[0], O[1]),
              I = (0, s.useCallback)(
                (e) => {
                  a || (b && b(), v && v(e));
                },
                [a, b, v],
              ),
              H = (0, s.useCallback)(
                (e) => {
                  const u = e.button === mn.LEFT;
                  a || (u && L(!0), u && B && B(e), D && f(D));
                },
                [a, B, D],
              ),
              U = (0, s.useCallback)(
                (e) => {
                  a || (L(!1), h && h(e));
                },
                [a, h],
              ),
              W = (0, s.useCallback)(
                (e) => {
                  a || (g && g(e), F && f(F));
                },
                [a, g, F],
              ),
              G = (0, s.useCallback)(
                (e) => {
                  a || (L(!1), p && p(e));
                },
                [a, p],
              ),
              $ = (0, s.useCallback)(
                (e) => {
                  a || (k(!0), S && S(e));
                },
                [a, S],
              ),
              z = (0, s.useCallback)(
                (e) => {
                  a || (k(!1), x && x(e));
                },
                [a, x],
              ),
              V = o().createElement(
                "div",
                { className: _n.label },
                o().createElement(
                  "div",
                  { className: l()(_n.labelContent, "s-labelContent"), style: R },
                  w || T,
                ),
              );
            return o().createElement(
              "div",
              Cn(
                {
                  id: u,
                  className: l()(_n.base, _n[`base__${_}`], _n[`base__${d}`], {
                    [_n.base__checked]: n,
                    [_n.base__disabled]: a,
                    [_n.base__mouseDown]: P,
                    [_n.base__alert]: c,
                    [_n.base__center]: y === An.Center,
                    [_n.base__bottom]: y === An.Bottom,
                  }),
                  onClick: I,
                  onMouseEnter: W,
                  onMouseLeave: G,
                  onMouseDown: H,
                  onMouseUp: U,
                  onFocus: $,
                  onBlur: z,
                },
                N,
              ),
              o().createElement(
                "div",
                { className: _n.input },
                o().createElement("div", { className: _n.alertOverlay }),
                o().createElement("div", { className: _n.inputHoverOverlay }),
                o().createElement("div", { className: _n.highlight }),
              ),
              o().createElement("div", { className: _n.checkmark }),
              ((w || T) && V) || null,
            );
          },
          gn = "CheckboxModule_base_c8",
          pn = "CheckboxModule_content_78",
          hn = "CheckboxModule_moduleDescription_3e",
          Bn = "CheckboxModule_info_b3",
          fn = "CheckboxModule_checkbox_8d",
          vn = "CheckboxModule_content__notPressed_0c",
          bn = R.strings.paragons.resetBranch,
          Sn = (0, s.memo)(({ checkboxState: e, onCheckboxChange: u }) => {
            const t = (0, s.useState)(!1),
              n = t[0],
              r = t[1];
            return o().createElement(
              "div",
              { className: gn },
              o().createElement(
                "div",
                {
                  className: l()(pn, !n && vn),
                  onMouseDown: () => {
                    r(!0);
                  },
                  onMouseEnter: () => {
                    v.playHighlight();
                  },
                  onMouseUp: () => {
                    r(!1);
                  },
                  onClick: () => {
                    (v.playClick(), u());
                  },
                },
                o().createElement(
                  "div",
                  { className: fn },
                  o().createElement(Dn, {
                    soundHover: "",
                    soundClick: "",
                    isChecked: e,
                    type: dn.main,
                  }),
                ),
                o().createElement(y.ZP, { text: bn.step2.module(), className: hn }),
                o().createElement("div", { className: Bn }),
              ),
            );
          }),
          xn = R.strings.paragons.resetBranch,
          wn = (e) => 1 - Math.pow(1 - e, 3),
          Rn = (0, s.memo)(
            ({
              isCardListAnimation: e,
              currentStep: u,
              cardList: t,
              realStep: n,
              canEquipStock: r,
              onChangeCardListAnimation: a,
              onInstallVehicleConfiguration: i,
              onChangeCheckboxState: c,
              checkboxState: m,
            }) => {
              const _ = (0, s.useState)(null),
                E = _[0],
                d = _[1],
                A = Ne(),
                F = A.getWrapperSize,
                C = A.getContainerSize,
                D = (0, s.useRef)(null),
                g = Ee(D),
                p = u === se.CAPTCHA,
                h = n === se.CAPTCHA,
                B = p && !h,
                b = u === se.DETAILS && h,
                S = l()(
                  cn.cardList,
                  (null === E || B || b) && cn.cardList__hidden,
                  null !== E && cn.blinkList,
                  h && cn.cardList__captchaStep,
                ),
                x = (0, s.useCallback)(() => {
                  (i(m ? "current" : "stock"), c(!m));
                }, [m, i, c]),
                w = (0, s.useCallback)(() => {
                  const e = F(),
                    u = C();
                  if (g)
                    if (e && u) {
                      d(u > e);
                    } else d(!1);
                }, [C, F, g]);
              ((0, s.useEffect)(() => {
                a(!(!B && !b));
              }, [B, b, a]),
                (0, s.useLayoutEffect)(() => {
                  const e = F(),
                    u = C();
                  if (g)
                    if (e && u) {
                      d(u > e);
                    } else d(!1);
                }, [g, u, n, F, C, A]),
                A.events.on("resizeHandled", w),
                (0, s.useEffect)(() => () => A.events.off("resizeHandled", w), []));
              const T = (0, we.useSpring)({
                from: { transform: `translateX(${F()}rem)`, opacity: 0 },
                to: { transform: "translateX(0rem)", opacity: 1 },
                delay: jr,
                config: { duration: 900, easing: wn },
                reset: !1,
                onStart: () => {
                  e || f(R.sounds.paragons_cards_slide());
                },
              });
              return o().createElement(
                "div",
                { className: cn.base },
                o().createElement(
                  an,
                  { scroll: E, cardListApi: A },
                  o().createElement(
                    we.animated.div,
                    {
                      className: S,
                      ref: D,
                      style: T,
                      onMouseEnter: () => {
                        E && v.playHighlight();
                      },
                      onMouseDown: () => {
                        E && v.playClick();
                      },
                    },
                    t.map((e, r) =>
                      o().createElement(
                        "div",
                        { className: cn.cardWrapper, key: e.vehicleInfo.name },
                        h
                          ? o().createElement(ln, {
                              key: `${e.vehicleInfo.name}_mini_${r}`,
                              resetVehicleInfo: e,
                            })
                          : o().createElement(Jt, {
                              resetVehicleInfo: e,
                              currentStep: u,
                              key: `${e.vehicleInfo.name}_${r}`,
                              index: t.length - r,
                              realStep: n,
                            }),
                      ),
                    ),
                  ),
                ),
                n === se.DETAILS &&
                  r &&
                  o().createElement(
                    Oe,
                    {
                      contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                      args: {
                        header: xn.tooltip.modules.header(),
                        description: xn.tooltip.modules.description(),
                      },
                    },
                    o().createElement(
                      "div",
                      { className: cn.module },
                      o().createElement(Sn, { checkboxState: m, onCheckboxChange: x }),
                    ),
                  ),
              );
            },
          ),
          Tn = "FadeAnimation_base_f3",
          yn = "FadeAnimation_base__fadeOut_59",
          Nn = "FadeAnimation_base__fadeIn_6d",
          Mn = "FadeAnimation_base__firstRender_24",
          Pn = (0, s.memo)(({ children: e, fadeOutAnimation: u, disabled: t = !1 }) => {
            const n = $();
            return t
              ? e
              : o().createElement("div", { className: l()(Tn, u ? yn : Nn, n && Mn) }, e);
          }),
          Ln = "DetailsFooter_base_8a",
          On = "DetailsFooter_pointsText_1b",
          kn = "DetailsFooter_count_bf",
          In = "DetailsFooter_creditIcon_24",
          Hn = R.strings.paragons.resetBranch,
          Un = (0, s.memo)(({ totalCredits: e }) =>
            o().createElement(
              "div",
              { className: Ln },
              o().createElement(y.ZP, { text: Hn.step2.creditsBack(), className: On }),
              o().createElement("div", { className: kn }, o().createElement(lu, { value: e })),
              o().createElement(
                Oe,
                {
                  contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                  args: {
                    header: Hn.tooltip.credits.header(),
                    description: Hn.tooltip.credits.description(),
                  },
                },
                o().createElement("div", { className: In }),
              ),
            ),
          ),
          Wn = "Footer_base_ad",
          Gn = "Footer_buttons_8b",
          $n = "Footer_buttons__step2_3b",
          zn = "Footer_button_d2",
          Vn = "Footer_smallButton_c5",
          jn = "Footer_smallButtonText_da",
          Xn = "Footer_detailsFooterContainer_55",
          qn = "Footer_confirmText_20",
          Yn = "InfoFooter_base_2b",
          Zn = "InfoFooter_branchCountCurrent_65",
          Kn = "InfoFooter_description_90",
          Qn = "InfoFooter_pointsWrapper_9b",
          Jn = "InfoFooter_points_df",
          er = "InfoFooter_pointsTitle_5b",
          ur = "InfoFooter_pointsDescription_3d",
          tr = "InfoFooter_count_0a",
          nr = "InfoFooter_paragonIcon_67",
          rr = "InfoFooter_plus_4f",
          ar = "InfoFooter_pointsBack_34",
          sr = R.strings.paragons.resetBranch,
          or = (0, s.memo)(
            ({
              maxResetBranchesCount: e,
              resetBranchesCount: u,
              totalVehiclesPoints: t,
              completeBonusCoins: n,
              coinsForBranchReset: r,
            }) => {
              const a = (0, s.useMemo)(
                () =>
                  ((e, u, t) =>
                    [
                      { key: ce.COINS_FOR_BRANCH_RESET, value: e },
                      { key: ce.TOTAL_VEHICLE_POINTS, value: u },
                      { key: ce.COMPLETE_BONUS_COINS, value: t },
                    ].filter((e) => e.value))(r, t, n),
                [r, n, t],
              );
              return o().createElement(
                "div",
                { className: Yn },
                o().createElement(
                  Oe,
                  {
                    contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                    args: {
                      header: sr.tooltip.resetBranch.header(),
                      description: (0, Lu.WU)(sr.tooltip.resetBranch.description(), {
                        maxResetBranchesCount: e,
                      }),
                    },
                  },
                  o().createElement(y.ZP, {
                    text: sr.step1.branchCount(),
                    format: {
                      binding: {
                        current: o().createElement(y.ZP, { text: String(u), className: Zn }),
                        maxResetBranchesCount: e,
                      },
                    },
                    className: Kn,
                  }),
                ),
                o().createElement(
                  Oe,
                  {
                    contentId: R.views.lobby.paragons.tooltips.ResetBranchTooltip("resId"),
                    args: {
                      header: sr.tooltip.totalProgressionPoints.header(),
                      description: sr.tooltip.totalProgressionPoints.description(),
                    },
                  },
                  o().createElement(
                    "div",
                    { className: Qn },
                    o().createElement(y.ZP, { text: sr.step1.willGet(), className: er }),
                    a.map(({ key: e, value: u }, t) => {
                      const n = a.length > t + 1,
                        r = e === ce.COMPLETE_BONUS_COINS;
                      return o().createElement(
                        "div",
                        { key: e, className: Jn },
                        o().createElement(y.ZP, { text: sr.step1.$dyn(e), className: ur }),
                        o().createElement(
                          "div",
                          { className: tr },
                          o().createElement(lu, { value: u }),
                        ),
                        o().createElement("div", { className: nr }),
                        n && o().createElement("div", { className: rr }),
                        r && o().createElement("div", { className: ar }),
                      );
                    }),
                  ),
                ),
              );
            },
          ),
          ir = R.strings.paragons.resetBranch,
          lr = (0, s.memo)(
            ({
              realStep: e,
              resetBranchesCount: u,
              maxResetBranchesCount: t,
              totalVehiclesPoints: n,
              completeBonusCoins: r,
              coinsForBranchReset: a,
              totalCredits: s,
              captchaState: i,
              onBack: c,
              onNext: m,
              isFadeOutAnimation: E,
            }) => {
              const d = (0, _.GS)().mediaSize >= _.cJ.Medium,
                A = e === se.CAPTCHA,
                F = A && i !== V.CONFORMITY,
                C = A ? ir.buttons.reset() : ir.buttons.next();
              return o().createElement(
                Pn,
                { fadeOutAnimation: E },
                o().createElement(
                  "div",
                  { className: Wn },
                  e === se.INFO &&
                    o().createElement(or, {
                      maxResetBranchesCount: t,
                      resetBranchesCount: u,
                      totalVehiclesPoints: n,
                      completeBonusCoins: r,
                      coinsForBranchReset: a,
                    }),
                  e === se.DETAILS &&
                    o().createElement(
                      "div",
                      { className: Xn },
                      o().createElement(Un, { totalCredits: s }),
                    ),
                  e === se.CAPTCHA &&
                    o().createElement(y.ZP, { text: ir.step3.confirmText(), className: qn }),
                  o().createElement(
                    "div",
                    { className: l()(Gn, e === se.DETAILS && $n) },
                    o().createElement(
                      "div",
                      { className: zn },
                      o().createElement(
                        T,
                        {
                          size: d ? x.medium : x.small,
                          type: S.secondary,
                          onClick: c,
                          mixClass: d ? void 0 : Vn,
                        },
                        o().createElement(y.ZP, {
                          text: ir.buttons.back(),
                          className: d ? void 0 : jn,
                        }),
                      ),
                    ),
                    o().createElement(
                      "div",
                      { className: zn },
                      o().createElement(
                        T,
                        {
                          size: d ? x.medium : x.small,
                          type: S.primary,
                          onClick: m,
                          disabled: F,
                          mixClass: d ? void 0 : Vn,
                        },
                        o().createElement(y.ZP, { text: C, className: d ? void 0 : jn }),
                      ),
                    ),
                  ),
                ),
              );
            },
          );
        var cr = t(280);
        const mr = {
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
          _r =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          Er = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          dr = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          Ar = (0, s.memo)(({ text: e, binding: u, classMix: t }) => {
            const n = (0, s.useCallback)((e) => ({ color: `#${e}` }), []),
              r = (0, s.useMemo)(() => u || {}, [u]);
            let a = _r.exec(e),
              i = e,
              l = 0;
            for (; a;) {
              const t = a[0],
                s = Er.exec(t),
                c = dr.exec(t),
                m = a[1];
              if (s && c) {
                const e = s[0],
                  a = e + l++ + e;
                ((i = i.replace(t, `%(${a})`)),
                  (r[a] = mr[e]
                    ? o().createElement(
                        "span",
                        { className: mr[e] },
                        o().createElement(cr.z, { text: m, binding: u }),
                      )
                    : o().createElement(
                        "span",
                        { style: n(e) },
                        o().createElement(cr.z, { text: m, binding: u }),
                      )));
              }
              a = _r.exec(e);
            }
            return o().createElement(cr.z, { text: i, classMix: t, binding: r });
          }),
          Fr = "Header_base_a0",
          Cr = "Header_subtitle_47",
          Dr = "Header_title_6b",
          gr = "Header_stepperWrapper_90",
          pr = "Header_description_ce",
          hr = "ResetBranchStepper_base_3a",
          Br = "ResetBranchStepper_line_1a",
          fr = "ResetBranchStepperTab_base_78",
          vr = "ResetBranchStepperTab_base__completed_61",
          br = "ResetBranchStepperTab_base__active_d7",
          Sr = "ResetBranchStepperTab_base__border_14",
          xr = "ResetBranchStepperTab_base__next_59",
          wr = "ResetBranchStepperTab_base__bg_44",
          Rr = "ResetBranchStepperTab_step_c5",
          Tr = "ResetBranchStepperTab_completeIcon_1a",
          yr = R.strings.paragons.resetBranch.tooltip,
          Nr = (0, s.memo)(({ step: e, isSelected: u, isCompleted: t, onStepChange: n }) => {
            const r = e + 1,
              a = yr.$dyn(`step${r}`),
              s = l()(fr, t && vr, u && br, !u && !t && xr);
            return o().createElement(
              Tu,
              { header: String(a.$dyn("header")), body: String(a.$dyn("descr")) },
              o().createElement(
                "div",
                {
                  className: s,
                  onClick: n,
                  onMouseEnter: () => {
                    t && v.playHighlight();
                  },
                },
                o().createElement("div", { className: wr }),
                o().createElement("div", { className: Sr }),
                t && o().createElement("div", { className: Tr }),
                o().createElement(y.ZP, { text: String(r), className: Rr }),
              ),
            );
          }),
          Mr = (0, s.memo)(({ currentStep: e, onTabChange: u }) => {
            const t = (n = se) ? Object.values(n).filter((e) => !isNaN(Number(e))) : [];
            var n;
            const r = (0, s.useCallback)(
              (e) => () => {
                (v.playClick(), u(e));
              },
              [u],
            );
            return o().createElement(
              "div",
              { className: hr },
              t.map((u, n) => {
                const a = e === n,
                  s = e > n;
                return o().createElement(
                  o().Fragment,
                  { key: u },
                  o().createElement(Nr, {
                    step: u,
                    isSelected: a,
                    isCompleted: s,
                    onStepChange: s ? r(u) : void 0,
                  }),
                  n !== t.length - 1 && o().createElement("div", { className: Br }),
                );
              }),
            );
          }),
          Pr = R.strings.paragons.resetBranch,
          Lr = (0, s.memo)(({ realStep: e, isFadeOutAnimation: u, onTabChange: t }) => {
            const n = e === se.CAPTCHA,
              r = Pr.$dyn(`step${e + 1}`);
            return o().createElement(
              "div",
              { className: Fr },
              o().createElement(y.ZP, { text: Pr.subtitle(), className: Cr }),
              o().createElement(y.ZP, { text: Pr.title(), className: Dr }),
              o().createElement(
                "div",
                { className: gr },
                o().createElement(Mr, { currentStep: e, onTabChange: t }),
              ),
              !n &&
                o().createElement(
                  Pn,
                  { fadeOutAnimation: u },
                  o().createElement(Ar, { text: String(r.$dyn("description")), classMix: pr }),
                ),
            );
          }),
          Or = "ResultScreen_base_6a",
          kr = "ResultScreen_fire_a1",
          Ir = "ResultScreen_smoke_47",
          Hr = "ResultScreen_icon_78",
          Ur = "ResultScreen_icon__failed_bd",
          Wr = "ResultScreen_text_d7",
          Gr = "ResultScreen_title_dd",
          $r = "ResultScreen_subTitle_fd";
        var zr;
        !(function (e) {
          ((e.Success = "success"), (e.Failed = "failed"));
        })(zr || (zr = {}));
        const Vr = (0, s.memo)(({ state: e }) => {
            const u = e === O.Success,
              t = u ? zr.Success : zr.Failed;
            return (
              (0, s.useEffect)(() => {
                f(u ? R.sounds.bp_reward_screen() : R.sounds.gui_error_screen());
              }, [u]),
              o().createElement(
                "div",
                { className: Or },
                o().createElement("div", { className: kr }),
                o().createElement("div", { className: Ir }),
                o().createElement("div", { className: l()(Hr, e === O.Failed && Ur) }),
                o().createElement(
                  "div",
                  { className: Wr },
                  o().createElement(y.ZP, {
                    className: Gr,
                    text: String(R.strings.paragons.resetBranch.resultScreen.title.$dyn(t)),
                  }),
                  o().createElement(y.ZP, {
                    className: $r,
                    text: String(R.strings.paragons.resetBranch.resultScreen.subTitle.$dyn(t)),
                  }),
                ),
              )
            );
          }),
          jr = 250,
          Xr = R.strings.paragons.resetBranch,
          qr = (0, z.Pi)(() => {
            const e = re(),
              u = e.model,
              t = e.controls,
              n = (0, _.GS)().mediaSize,
              r = $(),
              a = (0, s.useState)(0),
              i = a[0],
              c = a[1],
              m = (0, s.useState)(0),
              E = m[0],
              d = m[1],
              A = (0, s.useState)(!1),
              F = A[0],
              C = A[1],
              D = (0, s.useState)(!1),
              g = D[0],
              p = D[1],
              h = u.root.get(),
              B = h.totalCredits,
              v = h.resetBranchesCount,
              b = h.maxResetBranchesCount,
              w = h.isFill,
              N = h.canEquipStock,
              M = h.resetState,
              P = h.completeBonusCoins,
              U = h.coinsForBranchReset,
              W = u.checkboxState.get(),
              z = u.computes.getResetVehicles(),
              j = u.captchaState.get(),
              X = u.computes.getTotalVehiclesProgressPoints(),
              q = E === se.DETAILS,
              Y = E === se.CAPTCHA,
              Z = i === se.CAPTCHA,
              K = n >= _.cJ.Medium,
              Q = (0, s.useCallback)(() => {
                (0 === i && t.onClose(), c((e) => e - 1));
              }, [i, t]),
              J = (0, s.useCallback)(() => {
                i >= se.CAPTCHA ? t.onConfirm() : c((e) => e + 1);
              }, [i, t]);
            return (
              (0, s.useEffect)(
                () => (
                  r || C(!0),
                  k(() => {
                    (C(!1), d(i));
                  }, jr)
                ),
                [i],
              ),
              (0, s.useEffect)(() => {
                E === i || Y || Z || f(R.sounds.paragons_card_turn());
              }, [i, Z, Y, E]),
              (0, s.useEffect)(() => {
                j !== V.NORMAL && t.onCaptchaStateChange(V.NORMAL);
              }, [t, E]),
              (function ({
                key: e = H.n.ESCAPE,
                callback: u = () => I.O.view.sendEvent.close(),
                preventPropagation: t = !0,
              } = {}) {
                G(e, u, t);
              })({ callback: t.onClose, preventPropagation: !1 }),
              o().createElement(
                "div",
                { className: me.base },
                o().createElement(
                  "div",
                  { className: me.close },
                  o().createElement(L, {
                    caption: Xr.close(),
                    type: "close",
                    side: "right",
                    onClick: t.onClose,
                  }),
                ),
                (M === O.Failed || M === O.Success) &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement(
                      "div",
                      { className: l()(me.content, me.content__result) },
                      o().createElement(Vr, { state: M }),
                    ),
                    o().createElement(
                      T,
                      {
                        mixClass: me.resultScreenButton,
                        onClick: t.onClose,
                        type: S.primary,
                        size: K ? x.medium : x.small,
                      },
                      o().createElement(y.ZP, { text: Xr.resultScreen.button() }),
                    ),
                  ),
                M === O.Initial &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement(
                      "div",
                      { className: l()(me.content, Y && me.content__captcha) },
                      o().createElement(
                        "div",
                        { className: me.header },
                        o().createElement(Lr, {
                          realStep: E,
                          isFadeOutAnimation: F,
                          onTabChange: (e) => {
                            c(e);
                          },
                        }),
                      ),
                      Y &&
                        o().createElement(
                          Pn,
                          { fadeOutAnimation: F },
                          o().createElement(
                            "div",
                            { className: me.captchaWrapper },
                            o().createElement(pe, null),
                          ),
                        ),
                      w &&
                        o().createElement(
                          Pn,
                          { fadeOutAnimation: F, disabled: !g },
                          o().createElement(Rn, {
                            checkboxState: W,
                            onChangeCheckboxState: t.onCheckboxStateChange,
                            isCardListAnimation: g,
                            currentStep: i,
                            cardList: z,
                            realStep: E,
                            canEquipStock: N,
                            onChangeCardListAnimation: p,
                            onInstallVehicleConfiguration: t.onInstallVehicleConfiguration,
                          }),
                        ),
                    ),
                    o().createElement(
                      "div",
                      {
                        className: l()(me.footer, q && me.footer__details, Y && me.footer__captcha),
                      },
                      o().createElement(lr, {
                        realStep: E,
                        totalVehiclesPoints: X,
                        completeBonusCoins: P,
                        coinsForBranchReset: U,
                        maxResetBranchesCount: b,
                        resetBranchesCount: v,
                        totalCredits: B,
                        captchaState: j,
                        onBack: Q,
                        onNext: J,
                        isFadeOutAnimation: F,
                      }),
                    ),
                  ),
              )
            );
          });
        engine.whenReady.then(() => {
          B().render(
            o().createElement(ne, null, o().createElement(p, null, o().createElement(qr, null))),
            document.getElementById("root"),
          );
        });
      },
      5190: (e, u, t) => {
        "use strict";
        t.d(u, { M2: () => C, uA: () => A });
        var n = t(6483),
          r = t.n(n),
          a = t(7613);
        const s = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          o = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const i = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          l = (e) =>
            i
              ? `${e}`
              : (function (e) {
                  let u = "";
                  for (let t = o.length - 1; t >= 0; t--)
                    for (; e >= o[t];) ((u += s[t]), (e -= o[t]));
                  return u;
                })(e);
        var c = t(3649),
          m = t(6179),
          _ = t.n(m);
        const E = {
            base: "VehicleName_base_f4",
            base__white: "VehicleName_base__white_3d",
            base__whiteSpanish: "VehicleName_base__whiteSpanish_90",
            base__whiteOrange: "VehicleName_base__whiteOrange_52",
            base__cream: "VehicleName_base__cream_b3",
            nation: "VehicleName_nation_8b",
            base__colored: "VehicleName_base__colored_f2",
            level: "VehicleName_level_7d",
            type: "VehicleName_type_12",
            type__elite: "VehicleName_type__elite_0d",
            base__extraSmall: "VehicleName_base__extraSmall_74",
            base__medium: "VehicleName_base__medium_16",
            name: "VehicleName_name_5c",
          },
          d = "R.images.gui.maps.icons",
          A = { ExtraSmall: "extraSmall", Small: "small", Medium: "medium" },
          F = "whiteOrange",
          C = (0, m.memo)(
            ({
              isElite: e = !0,
              vehicleName: u,
              vehicleNation: t,
              vehicleType: n,
              vehicleLvl: s,
              isShortVehicleName: o = !1,
              size: i = A.Small,
              type: m = F,
              className: C,
            }) => {
              const D = r()(E.base, E[`base__${i}`], E[`base__${m}`], C),
                g = r()(E.type, e && E.type__elite),
                p = A.Medium ? "big" : "c_64x64";
              return _().createElement(
                "div",
                { className: D },
                !o &&
                  _().createElement(
                    _().Fragment,
                    null,
                    t &&
                      _().createElement("div", {
                        className: E.nation,
                        style: { backgroundImage: `url(${d}.flags.c_25x17.${t})` },
                      }),
                    _().createElement(a.ZP, { text: l(s), className: E.level }),
                    _().createElement("div", {
                      className: g,
                      style: {
                        backgroundImage: `url(${d}.vehicleTypes.${p}.${(0, c.BN)(n)}${e ? "_elite" : ""})`,
                      },
                    }),
                  ),
                _().createElement(a.ZP, { text: u, className: E.name }),
              );
            },
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
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        const n = { base: "FormatText_base_d0" };
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
          for (var [u, t, n] = deferred[i], a = !0, s = 0; s < u.length; s++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(i--, 1);
            var o = t();
            void 0 !== o && (e = o);
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
    (__webpack_require__.j = 844),
    (() => {
      var e = { 844: 0, 731: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            r,
            [a, s, o] = t,
            i = 0;
          if (a.some((u) => 0 !== e[u])) {
            for (n in s) __webpack_require__.o(s, n) && (__webpack_require__.m[n] = s[n]);
            if (o) var l = o(__webpack_require__);
          }
          for (u && u(t); i < a.length; i++)
            ((r = a[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [454], () => __webpack_require__(6394));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
