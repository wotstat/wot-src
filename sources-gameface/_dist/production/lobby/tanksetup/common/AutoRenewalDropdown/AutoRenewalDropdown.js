(() => {
  "use strict";
  var __webpack_modules__ = {
      570: (e, u, t) => {
        t.d(u, { x: () => D });
        var n = t(6483),
          o = t.n(n),
          r = t(1856),
          i = t(1091),
          l = t(6179),
          s = t.n(l),
          a = t(8380),
          c = t.n(a);
        const d = "ScrollArea_base_47",
          E = "ScrollArea_base__scrollIndent_1d",
          A = "ScrollArea_base__verticalScrollbarMargin_50",
          F = "ScrollArea_base__multiple_44",
          h = "ScrollArea_base__hidden_ec",
          D = s().forwardRef((e, u) => {
            const t = e.offsetLeft,
              n = void 0 === t ? 0 : t,
              a = e.offsetTop,
              D = void 0 === a ? 0 : a,
              v = e.scrollSettings,
              b = e.onUpdateActiveAxis,
              _ = e.onHorizontalScroll,
              m = e.onVerticalScroll,
              f = e.onOverScrollAtBeginning,
              C = e.onOverScrollAtEnd,
              p = e.wrapperIndent,
              B = e.verticalScrollbarMargin,
              g = e.isMultipleScroll,
              w = e.scrollAreaContainer,
              y = e.children,
              L = e.classMix,
              S = e.onScrollLeftHandled,
              T = (0, l.useState)(!1),
              k = T[0],
              M = T[1],
              O = (0, l.useState)(),
              R = O[0],
              P = O[1],
              x = (0, l.useState)(),
              Y = x[0],
              W = x[1],
              H = (0, l.useRef)(null),
              I = (0, l.useCallback)(() => {
                R &&
                  b &&
                  b(
                    { x: R.scrollbarXActive, y: R.scrollbarYActive },
                    { x: R.reach.x, y: R.reach.y },
                  );
              }, [b, R]),
              X = (0, l.useCallback)(() => R, [R]),
              N = (0, l.useCallback)(() => {
                R && R.update();
              }, [R]),
              U = (0, l.useCallback)(
                (e, u, t) => {
                  R && (R.setScrollLeft(e, u, t), S && S(e, R.contentWidth - R.containerWidth));
                },
                [R, S],
              ),
              j = (0, l.useCallback)(
                (e) => {
                  R &&
                    (R.setScrollLeftImmediately(e), S && S(e, R.contentWidth - R.containerWidth));
                },
                [R, S],
              ),
              z = (0, l.useCallback)(
                (e, u, t) => {
                  R && R.setScrollTop(e, u, t);
                },
                [R],
              ),
              K = (0, l.useCallback)(
                (e) => {
                  R && R.setScrollTopImmediately(e);
                },
                [R],
              ),
              V = (0, l.useCallback)(() => {
                if (Y && _ && R) {
                  const e = {
                    scrollPosition: Y.scrollLeft < 0 ? 0 : Y.scrollLeft,
                    reach: R.reach.x,
                  };
                  _(e);
                }
              }, [_, Y, R]),
              q = (0, l.useCallback)(() => {
                if (Y && m && R) {
                  const e = { scrollPosition: Y.scrollTop, reach: R.reach.y };
                  m(e);
                }
              }, [m, Y, R]),
              G = (0, l.useCallback)(() => {
                f && f();
              }, [f]),
              Z = (0, l.useCallback)(() => {
                C && C();
              }, [C]),
              $ = (0, l.useCallback)(
                (e) => {
                  ("function" == typeof u ? u(e) : null !== u && (u.current = e), W(e));
                },
                [u],
              ),
              Q = (0, l.useCallback)(() => {
                R &&
                  (R.update(),
                  (H.current = (0, r.v)(() => {
                    I();
                  })));
              }, [R, I]),
              J = (0, l.useCallback)((e) => {
                0 === e.screenX &&
                  0 === e.screenY &&
                  (e.stopImmediatePropagation(), e.preventDefault());
              }, []);
            (0, l.useEffect)(() => {
              if (R && Y)
                return (
                  document.addEventListener("mousemove", J),
                  window.addEventListener("resize", Q),
                  Y.addEventListener("ps-scroll-x", V),
                  Y.addEventListener("ps-scroll-y", q),
                  Y.addEventListener("over-scroll-beginning", G),
                  Y.addEventListener("over-scroll-ending", Z),
                  M(!0),
                  () => {
                    (window.removeEventListener("resize", Q),
                      document.removeEventListener("mousemove", J),
                      Y &&
                        (Y.removeEventListener("ps-scroll-x", V),
                        Y.removeEventListener("ps-scroll-y", q),
                        Y.removeEventListener("over-scroll-beginning", G),
                        Y.removeEventListener("over-scroll-ending", Z)));
                  }
                );
            }, [J, V, G, Z, Q, Y, R, q]);
            const ee = (0, l.useRef)(Y || null);
            ee.current = Y || null;
            const ue = (0, i.Z)(ee);
            ((0, l.useEffect)(
              () => (
                !R && Y && ue && P(new (c())(Y, Object.assign({}, v))),
                () => {
                  R && (R.destroy(), P(void 0));
                }
              ),
              [Y, ue, v, R],
            ),
              (0, l.useEffect)(
                () => () => {
                  null == H.current || H.current();
                },
                [],
              ),
              (0, l.useEffect)(
                () =>
                  (0, r.v)(() => {
                    R && I();
                  }),
                [I, R],
              ),
              (0, l.useEffect)(() => {
                n > 0 && j(n);
              }, [n, j]),
              (0, l.useEffect)(() => {
                D > 0 && K(D);
              }, [D, K]),
              (0, l.useEffect)(() => {
                w &&
                  ((w.setScrollLeft = U),
                  (w.setScrollTop = z),
                  (w.setScrollLeftImmediately = j),
                  (w.setScrollTopImmediately = K),
                  (w.updateScrollArea = N),
                  (w.getScrollbar = X));
              }, [w, U, j, z, K, N, X]));
            const te = o()(d, { [E]: p, [h]: !k, [A]: B, [F]: g }, L);
            return s().createElement("div", { className: te, ref: $ }, y);
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
        var o =
          "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        function r(e, u) {
          if (!o) throw new Error("No element matching method supported");
          return o.call(e, u);
        }
        function i(e) {
          e.remove ? e.remove() : e.parentNode && e.parentNode.removeChild(e);
        }
        function l(e, u) {
          return Array.prototype.filter.call(e.children, function (e) {
            return r(e, u);
          });
        }
        var s = "ps",
          a = {
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
          E = { immediately: !1 };
        function A(e, u, t) {
          void 0 === t && (t = {});
          var n = e.element.classList,
            o = c.scrolling(u);
          n.contains(o) ? clearTimeout(d[u]) : n.add(o);
        }
        function F(e, u, t) {
          void 0 === t && (t = {});
          Object.assign(E, t).immediately
            ? e.isAlive && e.element.classList.remove(c.scrolling(u))
            : (d[u] = setTimeout(function () {
                return e.isAlive && e.element.classList.remove(c.scrolling(u));
              }, e.settings.scrollingThreshold));
        }
        var h = function (e) {
            ((this.element = e), (this.handlers = {}));
          },
          D = { isEmpty: { configurable: !0 } };
        ((h.prototype.bind = function (e, u) {
          (void 0 === this.handlers[e] && (this.handlers[e] = []),
            this.handlers[e].push(u),
            this.element.addEventListener(e, u, !1));
        }),
          (h.prototype.unbind = function (e, u) {
            var t = this;
            this.handlers[e] = this.handlers[e].filter(function (n) {
              return !(!u || n === u) || (t.element.removeEventListener(e, n, !1), !1);
            });
          }),
          (h.prototype.unbindAll = function () {
            for (var e in this.handlers) this.unbind(e);
          }),
          (D.isEmpty.get = function () {
            var e = this;
            return Object.keys(this.handlers).every(function (u) {
              return 0 === e.handlers[u].length;
            });
          }),
          Object.defineProperties(h.prototype, D));
        var v = function () {
          this.eventElements = [];
        };
        function b(e) {
          return parseInt(e, 10) || 0;
        }
        ((v.prototype.eventElement = function (e) {
          var u = this.eventElements.filter(function (u) {
            return u.element === e;
          })[0];
          return (u || ((u = new h(e)), this.eventElements.push(u)), u);
        }),
          (v.prototype.bind = function (e, u, t) {
            this.eventElement(e).bind(u, t);
          }),
          (v.prototype.unbind = function (e, u, t) {
            var n = this.eventElement(e);
            (n.unbind(u, t),
              n.isEmpty && this.eventElements.splice(this.eventElements.indexOf(n), 1));
          }),
          (v.prototype.unbindAll = function () {
            (this.eventElements.forEach(function (e) {
              return e.unbindAll();
            }),
              (this.eventElements = []));
          }),
          (v.prototype.once = function (e, u, t) {
            var n = this.eventElement(e);
            n.bind(u, function e(o) {
              (n.unbind(u, e), t(o));
            });
          }));
        var _ = {
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
        function m() {
          return new Promise(function (e) {
            requestAnimationFrame(function () {
              requestAnimationFrame(function () {
                e();
              });
            });
          });
        }
        function f(e) {
          if ("function" == typeof window.CustomEvent) return new CustomEvent(e);
          var u = document.createEvent("CustomEvent");
          return (u.initCustomEvent(e, !1, !1, void 0), u);
        }
        var C = function (e, u, t, n, o, r) {
          var i;
          if (
            (void 0 === n && (n = !0),
            void 0 === o && (o = !1),
            void 0 === r && (r = !1),
            "top" === u)
          )
            i = ["contentHeight", "containerHeight", "scrollTop", "y", "up", "down"];
          else {
            if ("left" !== u) throw new Error("A proper axis should be provided");
            i = ["contentWidth", "containerWidth", "scrollLeft", "x", "left", "right"];
          }
          !(function (e, u, t, n, o, r) {
            var i = t[0],
              l = t[1],
              s = t[2],
              a = t[3],
              c = t[4],
              d = t[5];
            void 0 === n && (n = !0);
            void 0 === o && (o = !1);
            void 0 === r && (r = !1);
            var E = e.element;
            if (!e.reach) return;
            ((e.reach[a] = null), E[s] < 1 && (e.reach[a] = "start"));
            E[s] > e[i] - e[l] - 1 && (e.reach[a] = "end");
            u &&
              !o &&
              (E.dispatchEvent(f("ps-scroll-" + a)),
              u < 0
                ? E.dispatchEvent(f("ps-scroll-" + c))
                : u > 0 && E.dispatchEvent(f("ps-scroll-" + d)),
              n &&
                (function (e, u) {
                  (A(e, u), F(e, u));
                })(e, a));
            e.reach[a] && (u || r) && E.dispatchEvent(f("ps-" + a + "-reach-" + e.reach[a]));
          })(e, t, i, n, o, r);
        };
        var p = function (e, u, n, o) {
          (void 0 === u && (u = !1), void 0 === n && (n = 0), void 0 === o && (o = !1));
          var r = e.element;
          if (r) {
            if (
              ((e.containerWidth = Math.round(r.getBoundingClientRect().width)),
              (e.containerHeight = Math.round(r.getBoundingClientRect().height)),
              (e.contentWidth = Math.round(r.scrollWidth) - 2 * n),
              (e.contentHeight = Math.round(r.scrollHeight)),
              !o)
            ) {
              e.contentWidth = Math.round(r.scrollWidth) - 2 * n;
              var s = e.contentWidth - e.containerWidth + n;
              r.scrollLeft < n ? (r.scrollLeft = n) : r.scrollLeft > s && (r.scrollLeft = s);
            }
            var d = Math.floor(r.scrollTop),
              E = Math.floor(r.scrollLeft) - n,
              A = parseFloat(getComputedStyle(document.documentElement).fontSize);
            (r.contains(e.scrollbarXRail) ||
              (l(r, a.rail("x")).forEach(function (e) {
                return i(e);
              }),
              r.appendChild(e.scrollbarXRail)),
              r.contains(e.scrollbarYRail) ||
                (l(r, a.rail("y")).forEach(function (e) {
                  return i(e);
                }),
                r.appendChild(e.scrollbarYRail)),
              !e.settings.suppressScrollX &&
              e.containerWidth + e.settings.scrollXMarginOffset < e.contentWidth
                ? ((e.scrollbarXActive = !0),
                  (e.railXWidth = e.containerWidth - e.railXMarginWidth * A - 15 * A),
                  (e.railXRatio = e.containerWidth / e.railXWidth),
                  (e.scrollbarXWidth = B(e, b((e.railXWidth * e.containerWidth) / e.contentWidth))),
                  (e.scrollbarXLeft = b(
                    ((e.negativeScrollAdjustment + E) * (e.railXWidth - e.scrollbarXWidth)) /
                      (e.contentWidth - e.containerWidth),
                  )),
                  e.scrollbarXLeft < 0 && (e.scrollbarXLeft = 0))
                : (e.scrollbarXActive = !1),
              !e.settings.suppressScrollY &&
              e.containerHeight + e.settings.scrollYMarginOffset < e.contentHeight
                ? ((e.scrollbarYActive = !0),
                  (e.railYHeight = e.containerHeight - e.railYMarginHeight * A - 15 * A),
                  (e.railYRatio = e.containerHeight / e.railYHeight),
                  (e.scrollbarYHeight = B(
                    e,
                    b((e.railYHeight * e.containerHeight) / e.contentHeight),
                  )),
                  (e.scrollbarYTop = b(
                    (d * (e.railYHeight - e.scrollbarYHeight)) /
                      (e.contentHeight - e.containerHeight),
                  )))
                : (e.scrollbarYActive = !1),
              e.scrollbarXLeft >= e.railXWidth - e.scrollbarXWidth &&
                (e.scrollbarXLeft = e.railXWidth - e.scrollbarXWidth),
              e.scrollbarYTop >= e.railYHeight - e.scrollbarYHeight &&
                (e.scrollbarYTop = e.railYHeight - e.scrollbarYHeight),
              (function (e, u, n) {
                var o = { width: u.railXWidth },
                  r = Math.floor(e.scrollTop);
                u.isRtl
                  ? (o.left =
                      u.negativeScrollAdjustment + e.scrollLeft + u.containerWidth - u.contentWidth)
                  : (o.left = e.scrollLeft);
                u.isScrollbarXUsingBottom
                  ? (o.bottom = u.scrollbarXBottom - r)
                  : (o.top = u.scrollbarXTop + r);
                t(u.scrollbarXRail, o);
                var i = { top: r, height: u.railYHeight };
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
              })(r, e, A),
              e.scrollbarXButtonStart.classList.toggle("disabled", E < 1),
              e.scrollbarXButtonEnd.classList.toggle(
                "disabled",
                E + e.containerWidth >= e.contentWidth,
              ),
              e.scrollbarYButtonStart.classList.toggle("disabled", r.scrollTop < 1),
              e.scrollbarYButtonEnd.classList.toggle(
                "disabled",
                r.scrollTop + e.containerHeight >= e.contentHeight,
              ),
              e.scrollbarXActive
                ? (r.classList.add(c.active("x")), C(e, "left", E - e.lastScrollLeft, !0, u))
                : (r.classList.remove(c.active("x")),
                  (e.scrollbarXWidth = 0),
                  (e.scrollbarXLeft = 0),
                  (r.scrollLeft = 0)),
              e.scrollbarYActive
                ? (r.classList.add(c.active("y")),
                  C(e, "top", r.scrollTop - e.lastScrollTop, !0, u))
                : (r.classList.remove(c.active("y")),
                  (e.scrollbarYHeight = 0),
                  (e.scrollbarYTop = 0),
                  (r.scrollTop = 0)),
              (e.lastScrollTop = d),
              (e.lastScrollLeft = E),
              (e.scrollTopPercent = r.scrollTop / r.scrollHeight),
              (e.scrollLeftPercent = r.scrollLeft / r.scrollWidth));
          }
        };
        function B(e, u) {
          return (
            e.settings.minScrollbarLength && (u = Math.max(u, e.settings.minScrollbarLength)),
            e.settings.maxScrollbarLength && (u = Math.min(u, e.settings.maxScrollbarLength)),
            u
          );
        }
        var g = {
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
              o = e.y1,
              r = e.x2,
              i = e.y2;
            return (
              1 -
              (n * ((u = t), Math.pow(u, 3)) +
                o *
                  (function (e) {
                    return 3 * e * e * (1 - e);
                  })(t) +
                r *
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
              o = e.onRefUpdateCallback,
              r = e.duration,
              i = e.cubicBezierPoints,
              l = e.easingPreset,
              s = e.scrollAmount,
              a = e.onCheckForBreakCallback,
              c = e.boundsInfo;
            void 0 === c && (c = y);
            var d = null,
              E = null,
              A = null,
              F = null,
              h = u === window,
              D = ["left", "right"].indexOf(n) > -1,
              v = ["right", "bottom"].indexOf(n) > -1;
            D
              ? ((E = h ? "scrollX" : "scrollLeft"),
                (F = h ? "innerWidth" : "width"),
                (A = "scrollWidth"))
              : ((E = h ? "scrollY" : "scrollTop"),
                (F = h ? "innerHeight" : "height"),
                (A = "scrollHeight"));
            var b = u[E],
              _ = (function (e) {
                var u,
                  t = e.isWindow,
                  n = e.scrollableDomEle,
                  o = e.elementLengthProp,
                  r = e.initialScrollPosition,
                  i = e.isHorizontalDirection,
                  l = e.scrollLengthProp,
                  s = e.direction;
                if (t) {
                  var a = document.documentElement;
                  u = i ? a.offsetWidth : a.offsetHeight;
                } else u = (n[l] - n.getBoundingClientRect()[o]) | 0;
                return ["left", "top"].includes(s) ? r : u - r;
              })({
                isWindow: h,
                scrollableDomEle: u,
                elementLengthProp: F,
                initialScrollPosition: b,
                isHorizontalDirection: D,
                scrollLengthProp: A,
                direction: n,
              });
            !isNaN(s) && s < _ && (_ = s);
            var m = function e(n) {
              if (!a || !a()) {
                var s = n - d,
                  A = (function (e) {
                    var u = e.easingPreset,
                      t = e.cubicBezierPoints,
                      n = e.duration,
                      o = e.runTime / n;
                    if (g.hasOwnProperty(u)) return g[u](o);
                    if (
                      t &&
                      !isNaN(t.x1) &&
                      !isNaN(t.y1) &&
                      !isNaN(t.x2) &&
                      !isNaN(t.y2) &&
                      t.x1 >= 0 &&
                      t.x2 >= 0
                    )
                      return w({ percentTimeElapsed: o, x1: t.x1, x2: t.x2, y1: t.y1, y2: t.y2 });
                    throw new Error("Please enter a valid easing value");
                  })({ easingPreset: l, cubicBezierPoints: i, runTime: s, duration: r });
                if (!isNaN(A)) {
                  var F = Math.round(A * _),
                    m = v ? F + b : _ - F;
                  if (
                    (c.breakBounds &&
                      (m < c.startBound ? (m = c.startBound) : m > c.endBound && (m = c.endBound)),
                    s < r)
                  ) {
                    if (h) {
                      var f = D ? m : 0,
                        C = D ? 0 : m;
                      window.scrollTo(f, C);
                    } else u[E] = m;
                    (o && o(m), requestAnimationFrame(e));
                  } else t && t();
                }
              }
            };
            requestAnimationFrame(function (e) {
              ((d = e), m(e));
            });
          },
          S = function (e) {
            var u = e.axis,
              t = e.cursorPositionOnRail,
              n = e.direction,
              o = e.i,
              r = (function (e) {
                var u = e.axis,
                  t = e.i,
                  n = e.cursorPositionOnRail;
                if ("y" === u) {
                  var o = t.scrollbarY.offsetTop,
                    r = o + t.scrollbarYHeight;
                  return n >= o && n <= r;
                }
                var i = t.scrollbarX.offsetLeft,
                  l = i + t.scrollbarXWidth;
                return n >= i && n <= l;
              })({ axis: u, i: o, cursorPositionOnRail: t });
            return r
              ? ((function (e) {
                  var u = e.axis,
                    t = e.i,
                    n = e.cursorPositionOnRail,
                    o = (function (e, u) {
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
                    r = (n - o.scrollbar / 2) / o.rail,
                    i = Math.round(Math.min(o.maxScroll, Math.max(0, o.content * r)));
                  "y" === u ? (t.element.scrollTop = i) : (t.element.scrollLeft = i);
                })({ axis: u, i: o, cursorPositionOnRail: t }),
                !0)
              : ("y" === u
                  ? (o.element.scrollTop += n * o.containerHeight)
                  : (o.element.scrollLeft += n * o.containerWidth),
                !1);
          },
          T = function (e, u, t) {
            return function (n) {
              u = u.toLowerCase();
              var o = null,
                r = function () {
                  if (1 === n.buttons) {
                    if (
                      !n.target.closest(".ps__rail-" + u) ||
                      !n.target.closest(".ps__track_" + u)
                    ) {
                      var r = (function (e) {
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
                        i = r.cursorPosition - r.windowScrolled - r.elementPosition,
                        l = (function (e) {
                          var u = e.axis,
                            t = e.cursorPositionOnRail,
                            n = e.i;
                          return t > ("y" === u ? n.scrollbarYTop : n.scrollbarXLeft) ? 1 : -1;
                        })({ axis: u, cursorPositionOnRail: i, i: e });
                      (S({ axis: u, cursorPositionOnRail: i, direction: l, i: e }) &&
                        clearTimeout(o),
                        p(e, !1, t));
                    }
                    n.stopPropagation();
                  }
                };
              (r(),
                (o = setInterval(r, 100)),
                e.event.once(e.ownerDocument, "mouseup", function () {
                  clearTimeout(o);
                }));
            };
          };
        function k(e, u, t) {
          var n = t[0],
            o = t[1],
            r = t[2],
            i = t[3],
            l = t[4],
            s = t[5],
            a = t[6],
            d = t[7],
            E = t[8],
            h = e.element,
            D = null,
            v = null,
            _ = null;
          function m(t) {
            ((h[a] = b(D + _ * (t[r] - v))),
              A(e, d),
              p(e, !1, u),
              t.stopPropagation(),
              t.preventDefault());
          }
          function f() {
            (F(e, d),
              e[E].classList.remove(c.clicking),
              e.event.unbind(e.ownerDocument, "mousemove", m));
          }
          e.event.bind(e[l], "mousedown", function (u) {
            1 === u.buttons &&
              ((D = h[a]),
              (v = u[r]),
              (_ = (e[o] - e[n]) / (e[i] - e[s])),
              e.event.bind(e.ownerDocument, "mousemove", m),
              e.event.once(e.ownerDocument, "mouseup", f),
              e[E].classList.add(c.clicking),
              u.stopPropagation(),
              u.preventDefault());
          });
        }
        var M = 1e3,
          O = {
            "click-rail": function (e, u) {
              (e.event.bind(e.scrollbarY, "mousedown", function (e) {
                return e.stopPropagation();
              }),
                e.event.bind(e.scrollbarYRail, "mousedown", T(e, "y", 0)),
                e.event.bind(e.scrollbarX, "mousedown", function (e) {
                  return e.stopPropagation();
                }),
                e.event.bind(e.scrollbarXRail, "mousedown", T(e, "x", u)));
            },
            "drag-thumb": function (e, u) {
              (k(e, u, [
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
                k(e, u, [
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
                  r(t, ":hover")
                ) {
                  var o,
                    i = document.activeElement
                      ? document.activeElement
                      : e.ownerDocument.activeElement;
                  if (i) {
                    if ("IFRAME" === i.tagName) i = i.contentDocument.activeElement;
                    else for (; i.shadowRoot;) i = i.shadowRoot.activeElement;
                    if (
                      r((o = i), "input,[contenteditable]") ||
                      r(o, "select,[contenteditable]") ||
                      r(o, "textarea,[contenteditable]") ||
                      r(o, "button,[contenteditable]")
                    )
                      return;
                  }
                  var l = 0,
                    s = 0;
                  switch (n.which) {
                    case 37:
                      l = n.metaKey ? -e.contentWidth : n.altKey ? -e.containerWidth : -30;
                      break;
                    case 38:
                      s = n.metaKey ? e.contentHeight : n.altKey ? e.containerHeight : 30;
                      break;
                    case 39:
                      l = n.metaKey ? e.contentWidth : n.altKey ? e.containerWidth : 30;
                      break;
                    case 40:
                      s = n.metaKey ? -e.contentHeight : n.altKey ? -e.containerHeight : -30;
                      break;
                    case 32:
                      s = n.shiftKey ? e.containerHeight : -e.containerHeight;
                      break;
                    case 33:
                      s = e.containerHeight;
                      break;
                    case 34:
                      s = -e.containerHeight;
                      break;
                    case 36:
                      s = e.contentHeight;
                      break;
                    case 35:
                      s = -e.contentHeight;
                      break;
                    default:
                      return;
                  }
                  (e.settings.suppressScrollX && 0 !== l) ||
                    (e.settings.suppressScrollY && 0 !== s) ||
                    ((t.scrollTop -= s),
                    (t.scrollLeft += l),
                    p(e, !1, u),
                    (function (u, n) {
                      var o = Math.floor(t.scrollTop);
                      if (0 === u) {
                        if (!e.scrollbarYActive) return !1;
                        if (
                          (0 === o && n > 0) ||
                          (o >= e.contentHeight - e.containerHeight && n < 0)
                        )
                          return !e.settings.wheelPropagation;
                      }
                      var r = t.scrollLeft;
                      if (0 === n) {
                        if (!e.scrollbarXActive) return !1;
                        if ((0 === r && u < 0) || (r >= e.contentWidth - e.containerWidth && u > 0))
                          return !e.settings.wheelPropagation;
                      }
                      return !0;
                    })(l, s) && n.preventDefault());
                }
              });
            },
            wheel: function (e, t) {
              var n = e.element;
              function o(o) {
                var r = (function (e) {
                    var u = -1 * e.deltaX,
                      t = e.deltaY;
                    return (
                      (void 0 !== u && void 0 !== t) ||
                        ((u = (-1 * e.wheelDeltaX) / 6), (t = e.wheelDeltaY / 6)),
                      e.deltaMode && 1 === e.deltaMode && ((u *= 10), (t *= 10)),
                      u != u && t != t && ((u = 0), (t = e.wheelDelta)),
                      e.shiftKey ? [-t, -u] : [u, t]
                    );
                  })(o),
                  i = r[0],
                  l = r[1];
                if (
                  !(function (e, t, o) {
                    if (!_.isWebKit && n.querySelector("select")) return !0;
                    if (!n.contains(e)) return !1;
                    for (var r = e; r && r !== n;) {
                      if (r.classList.contains(a.consuming)) return !0;
                      var i = u(r);
                      if ([i.overflow, i.overflowX, i.overflowY].join("").match(/(scroll|auto)/)) {
                        var l = r.scrollHeight - r.clientHeight;
                        if (
                          l > 0 &&
                          !((0 === r.scrollTop && o > 0) || (r.scrollTop === l && o < 0))
                        )
                          return !0;
                        var s = r.scrollWidth - r.clientWidth;
                        if (
                          s > 0 &&
                          !((0 === r.scrollLeft && t < 0) || (r.scrollLeft === s && t > 0))
                        )
                          return !0;
                      }
                      r = r.parentNode;
                    }
                    return !1;
                  })(o.target, i, l)
                ) {
                  var s = !1,
                    c = (i * e.settings.wheelSpeed) | 0,
                    d = (l * e.settings.wheelSpeed) | 0;
                  (e.settings.useBothWheelAxes
                    ? e.scrollbarYActive && !e.scrollbarXActive
                      ? (l ? (n.scrollTop -= d) : (n.scrollTop += c), (s = !0))
                      : e.scrollbarXActive &&
                        !e.scrollbarYActive &&
                        (i ? (n.scrollLeft += c) : (n.scrollLeft -= d), (s = !0))
                    : ((n.scrollTop -= d), (n.scrollLeft += c)),
                    p(e, !1, t),
                    (s =
                      s ||
                      (function (u, t) {
                        var o = Math.floor(n.scrollTop),
                          r = 0 === n.scrollTop,
                          i = o + n.offsetHeight === n.scrollHeight,
                          l = 0 === n.scrollLeft,
                          s = n.scrollLeft + n.offsetWidth === n.scrollWidth;
                        return (
                          !(Math.abs(t) > Math.abs(u) ? r || i : l || s) ||
                          !e.settings.wheelPropagation
                        );
                      })(i, l)),
                    s && !o.ctrlKey && (o.stopPropagation(), o.preventDefault()));
                }
              }
              (e.event.bind(n, "wheel", o),
                void 0 !== window.onmousewheel && e.event.bind(n, "mousewheel", o));
            },
            touch: function (e, t) {
              if (_.supportsTouch || _.supportsIePointer) {
                var n = e.element,
                  o = {},
                  r = 0,
                  i = {},
                  l = null;
                _.supportsTouch
                  ? (e.event.bind(n, "touchstart", E),
                    e.event.bind(n, "touchmove", A),
                    e.event.bind(n, "touchend", F))
                  : _.supportsIePointer &&
                    (window.PointerEvent
                      ? (e.event.bind(n, "pointerdown", E),
                        e.event.bind(n, "pointermove", A),
                        e.event.bind(n, "pointerup", F))
                      : window.MSPointerEvent &&
                        (e.event.bind(n, "MSPointerDown", E),
                        e.event.bind(n, "MSPointerMove", A),
                        e.event.bind(n, "MSPointerUp", F)));
              }
              function s(u, o) {
                ((n.scrollTop -= o), (n.scrollLeft -= u), p(e, !1, t));
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
              function E(e) {
                if (d(e)) {
                  var u = c(e);
                  ((o.pageX = u.pageX),
                    (o.pageY = u.pageY),
                    (r = new Date().getTime()),
                    null !== l && clearInterval(l));
                }
              }
              function A(t) {
                if (d(t)) {
                  var l = c(t),
                    E = { pageX: l.pageX, pageY: l.pageY },
                    A = E.pageX - o.pageX,
                    F = E.pageY - o.pageY;
                  if (
                    (function (e, t, o) {
                      if (!n.contains(e)) return !1;
                      for (var r = e; r && r !== n;) {
                        if (r.classList.contains(a.consuming)) return !0;
                        var i = u(r);
                        if (
                          [i.overflow, i.overflowX, i.overflowY].join("").match(/(scroll|auto)/)
                        ) {
                          var l = r.scrollHeight - r.clientHeight;
                          if (
                            l > 0 &&
                            !((0 === r.scrollTop && o > 0) || (r.scrollTop === l && o < 0))
                          )
                            return !0;
                          var s = r.scrollLeft - r.clientWidth;
                          if (
                            s > 0 &&
                            !((0 === r.scrollLeft && t < 0) || (r.scrollLeft === s && t > 0))
                          )
                            return !0;
                        }
                        r = r.parentNode;
                      }
                      return !1;
                    })(t.target, A, F)
                  )
                    return;
                  (s(A, F), (o = E));
                  var h = new Date().getTime(),
                    D = h - r;
                  (D > 0 && ((i.x = A / D), (i.y = F / D), (r = h)),
                    (function (u, t) {
                      var o = Math.floor(n.scrollTop),
                        r = n.scrollLeft,
                        i = Math.abs(u),
                        l = Math.abs(t);
                      if (l > i) {
                        if (
                          (t < 0 && o === e.contentHeight - e.containerHeight) ||
                          (t > 0 && 0 === o)
                        )
                          return 0 === window.scrollY && t > 0 && _.isChrome;
                      } else if (
                        i > l &&
                        ((u < 0 && r === e.contentWidth - e.containerWidth) || (u > 0 && 0 === r))
                      )
                        return !0;
                      return !0;
                    })(A, F) && t.preventDefault());
                }
              }
              function F() {
                e.settings.swipeEasing &&
                  (clearInterval(l),
                  (l = setInterval(function () {
                    e.isInitialized
                      ? clearInterval(l)
                      : i.x || i.y
                        ? Math.abs(i.x) < 0.01 && Math.abs(i.y) < 0.01
                          ? clearInterval(l)
                          : (s(30 * i.x, 30 * i.y), (i.x *= 0.8), (i.y *= 0.8))
                        : clearInterval(l);
                  }, 10)));
              }
            },
            "drag-move": function (e, u) {
              void 0 === u && (u = 0);
              var t = e.element,
                n = null,
                o = !1,
                r = 0,
                i = 0,
                l = 0;
              function s() {
                e.onScroll();
              }
              function a(n, o, r, i) {
                (void 0 === r && (r = null),
                  void 0 === i && (i = !1),
                  L({
                    scrollableDomEle: t,
                    direction: "right",
                    onRefUpdateCallback: s,
                    duration: o,
                    easingPreset: "easeOutCubic",
                    scrollAmount: n,
                    onCheckForBreakCallback: r,
                    boundsInfo: {
                      breakBounds: i,
                      startBound: u,
                      endBound: e.contentWidth - e.containerWidth + u,
                    },
                  }));
              }
              function d() {
                if (o) return o;
              }
              function E() {
                l = 0;
              }
              function h(o) {
                if (e.scrollbarXActive) {
                  var s = n - o.screenX;
                  ((t.scrollLeft += s), (n = o.screenX));
                  var a = new Date().getTime();
                  if (((r = (s / (a - i)) * 1e3), (i = a), e.onScroll(), u > 0)) {
                    var c = e.contentWidth - e.containerWidth + 2 * u;
                    0 === t.scrollLeft || t.scrollLeft === c
                      ? 0 === l && (l = window.setTimeout(E, 250))
                      : 0 !== l && (window.clearTimeout(l), (l = 0));
                  }
                  (A(e, "x"),
                    A(e, "dragging", { immediately: !0 }),
                    o.stopPropagation(),
                    o.preventDefault());
                }
              }
              function D(e) {
                ((n = e.screenX),
                  (o = !0),
                  requestAnimationFrame(function () {
                    o = !1;
                  }),
                  (i = new Date().getTime()));
              }
              function v(n) {
                var o = e.contentWidth - e.containerWidth + u;
                if (t.scrollLeft < u) a(u - t.scrollLeft, M, d);
                else if (t.scrollLeft > o) a(o - t.scrollLeft, M, d);
                else {
                  new Date().getTime() - i < 100 && a(r / 4, M, d, !0);
                }
                (F(e, "x"),
                  F(e, "dragging", { immediately: !0 }),
                  e.scrollbarXRail.classList.remove(c.clicking),
                  e.event.unbind(e.ownerDocument, "mousemove", h));
              }
              function b() {
                o = !0;
              }
              t.addEventListener(
                "mousedown",
                function (u) {
                  1 === u.buttons &&
                    ((n = u.screenX),
                    e.event.bind(e.ownerDocument, "mousemove", h),
                    e.event.once(e.ownerDocument, "mouseup", v),
                    e.event.once(e.ownerDocument, "mousedown", D),
                    e.event.once(t, "wheel", b),
                    e.scrollbarXRail.classList.add(c.clicking),
                    u.preventDefault());
                },
                !1,
              );
            },
          },
          R = function (e, o) {
            var r = this;
            if (
              (void 0 === o && (o = {}),
              "string" == typeof e && (e = document.querySelector(e)),
              !e || !e.nodeName)
            )
              throw new Error("no element is specified to initialize PerfectScrollbar");
            for (var i in ((this.element = e),
            e.classList.add(s),
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
            o))
              r.settings[i] = o[i];
            ((this.containerWidth = null),
              (this.containerHeight = null),
              (this.contentWidth = null),
              (this.contentHeight = null));
            var l,
              d,
              E = function () {
                return e.classList.add(c.focus);
              },
              A = function () {
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
              (this.event = new v()),
              (this.ownerDocument = e.ownerDocument || document),
              (this.scrollbarXRail = n(a.rail("x"))),
              (this.scrollbarXButtonStart = n(a.buttonStart("x"))),
              (this.scrollbarXButtonEnd = n(a.buttonEnd("x"))),
              (this.scrollbarXTrack = n(a.track("x"))),
              e.appendChild(this.scrollbarXRail),
              this.scrollbarXRail.appendChild(this.scrollbarXTrack),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonStart),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonEnd),
              (this.scrollbarX = n(a.thumb("x"))),
              this.scrollbarXRail.appendChild(this.scrollbarX),
              this.scrollbarX.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarX, "focus", E),
              this.event.bind(this.scrollbarX, "blur", A),
              (this.scrollbarXActive = null),
              (this.scrollbarXWidth = null),
              (this.scrollbarXLeft = null),
              (this.scrollbarYRail = n(a.rail("y"))),
              (this.scrollbarYButtonStart = n(a.buttonStart("y"))),
              (this.scrollbarYButtonEnd = n(a.buttonEnd("y"))),
              (this.scrollbarYTrack = n(a.track("y"))),
              e.appendChild(this.scrollbarYRail),
              this.scrollbarYRail.appendChild(this.scrollbarYTrack),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonStart),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonEnd),
              (this.scrollbarY = n(a.thumb("y"))),
              this.scrollbarYRail.appendChild(this.scrollbarY),
              this.scrollbarY.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarY, "focus", E),
              this.event.bind(this.scrollbarY, "blur", A),
              (this.scrollbarYActive = null),
              (this.scrollbarYHeight = null),
              (this.scrollbarYTop = null),
              m().then(function () {
                var n = u(r.scrollbarXRail);
                ((r.scrollbarXBottom = parseInt(n.bottom, 10)),
                  isNaN(r.scrollbarXBottom)
                    ? ((r.isScrollbarXUsingBottom = !1), (r.scrollbarXTop = b(n.top)))
                    : (r.isScrollbarXUsingBottom = !0),
                  (r.railBorderXWidth = b(n.borderLeftWidth) + b(n.borderRightWidth)),
                  t(r.scrollbarXRail, { display: "block" }),
                  (r.railXMarginWidth = b(n.marginLeft) + b(n.marginRight)),
                  t(r.scrollbarXRail, { display: "" }),
                  (r.railXWidth = null),
                  (r.railXRatio = null));
                var o = u(r.scrollbarYRail);
                ((r.scrollbarYRight = parseInt(o.right, 10)),
                  isNaN(r.scrollbarYRight)
                    ? ((r.isScrollbarYUsingRight = !1), (r.scrollbarYLeft = b(o.left)))
                    : (r.isScrollbarYUsingRight = !0),
                  (r.scrollbarYOuterWidth = r.isRtl
                    ? (function (e) {
                        var t = u(e);
                        return (
                          b(t.width) +
                          b(t.paddingLeft) +
                          b(t.paddingRight) +
                          b(t.borderLeftWidth) +
                          b(t.borderRightWidth)
                        );
                      })(r.scrollbarY)
                    : null),
                  (r.railBorderYWidth = b(o.borderTopWidth) + b(o.borderBottomWidth)),
                  t(r.scrollbarYRail, { display: "block" }),
                  (r.railYMarginHeight = b(o.marginTop) + b(o.marginBottom)),
                  t(r.scrollbarXRail, { display: "" }),
                  t(r.scrollbarYRail, { display: "" }),
                  (r.railYHeight = null),
                  (r.railYRatio = null),
                  (r.reach = {
                    x:
                      e.scrollLeft <= 0
                        ? "start"
                        : e.scrollLeft >= r.contentWidth - r.containerWidth
                          ? "end"
                          : null,
                    y:
                      e.scrollTop <= 0
                        ? "start"
                        : e.scrollTop >= r.contentHeight - r.containerHeight
                          ? "end"
                          : null,
                  }),
                  (r.isAlive = !0),
                  r.settings.handlers.forEach(function (e) {
                    return O[e](r, r.settings.overScrollWidth);
                  }),
                  (r.boundHandleButtonEnter = r.handleMouseEnter.bind(r)),
                  (r.boundHandleMouseLeave = r.handleMouseLeave.bind(r)),
                  (r.boundHandleMouseEnter = r.handleMouseEnter.bind(r)),
                  (r.boundPlayClickSound = r.playClickSound.bind(r)),
                  r.scrollbarYButtonStart.addEventListener("mousedown", r.boundPlayClickSound),
                  r.scrollbarYButtonEnd.addEventListener("mousedown", r.boundPlayClickSound),
                  r.scrollbarXButtonStart.addEventListener("mousedown", r.boundPlayClickSound),
                  r.scrollbarXButtonEnd.addEventListener("mousedown", r.boundPlayClickSound),
                  r.scrollbarXButtonStart.addEventListener("mouseenter", r.boundHandleMouseEnter),
                  r.scrollbarXButtonEnd.addEventListener("mouseenter", r.boundHandleMouseEnter),
                  r.scrollbarYButtonStart.addEventListener("mouseenter", r.boundHandleButtonEnter),
                  r.scrollbarYButtonEnd.addEventListener("mouseenter", r.boundHandleButtonEnter),
                  r.scrollbarYButtonStart.addEventListener("mouseleave", r.boundHandleMouseLeave),
                  r.scrollbarYButtonEnd.addEventListener("mouseleave", r.boundHandleMouseLeave),
                  r.scrollbarY.addEventListener("mouseenter", r.boundHandleMouseEnter),
                  r.scrollbarX.addEventListener("mouseenter", r.boundHandleMouseEnter),
                  r.scrollbarY.addEventListener("mouseleave", r.boundHandleMouseLeave),
                  r.scrollbarY.addEventListener("mousedown", r.boundPlayClickSound),
                  r.scrollbarX.addEventListener("mousedown", r.boundPlayClickSound),
                  (r.lastScrollTop = Math.floor(e.scrollTop)),
                  (r.lastScrollLeft = e.scrollLeft),
                  (r.scrollTopPercent = e.scrollTop / e.scrollHeight),
                  (r.scrollLeftPercent = e.scrollLeft / e.scrollWidth),
                  r.event.bind(r.element, "scroll", function (e) {
                    return r.onScroll(e);
                  }),
                  r.settings.enableHorizontalScroll &&
                    r.event.bind(r.element, "wheel", function (e) {
                      return r.onWheel(e);
                    }),
                  p(r, !1, r.settings.overScrollWidth, !1));
              }));
          };
        ((R.prototype._getAnimationSettings = function (e, u, t, n) {
          var o = this,
            r = 0;
          return (
            null !== this.element &&
              (r = ["bottom", "top"].includes(u)
                ? this.element.scrollTop
                : this.element.scrollLeft),
            {
              scrollableDomEle: this.element,
              duration: this.settings.animationDuration,
              easingPreset: this.settings.animationEasingPreset,
              scrollAmount: e - r,
              direction: u,
              onRefUpdateCallback: function (e) {
                (p(o, !0, o.settings.overScrollWidth, !1), t && t(e));
              },
              onAnimationCompleteCallback: function () {
                n && n();
              },
            }
          );
        }),
          (R.prototype.playHoverSound = function () {
            window.engine && engine.call("PlaySound", "highlight");
          }),
          (R.prototype.playClickSound = function () {
            window.engine && engine.call("PlaySound", "play");
          }),
          (R.prototype.handleMouseEnter = function () {
            this.playHoverSound();
          }),
          (R.prototype.handleMouseLeave = function () {}),
          (R.prototype.update = function () {
            var e = this;
            this.isAlive &&
              ((this.negativeScrollAdjustment = this.isNegativeScroll
                ? this.element.scrollWidth - this.element.clientWidth
                : 0),
              t(this.scrollbarXRail, { display: "block" }),
              t(this.scrollbarYRail, { display: "block" }),
              (this.railXMarginWidth =
                b(u(this.scrollbarXRail).marginLeft) + b(u(this.scrollbarXRail).marginRight)),
              (this.railYMarginHeight =
                b(u(this.scrollbarYRail).marginTop) + b(u(this.scrollbarYRail).marginBottom)),
              t(this.scrollbarXRail, { display: "none" }),
              t(this.scrollbarYRail, { display: "none" }),
              m().then(function () {
                (e.settings.isDisableScrollToLastPositionOnResize ||
                  ((e.element.scrollTop = e.element.scrollHeight * e.scrollTopPercent),
                  (e.element.scrollLeft = e.element.scrollWidth * e.scrollLeftPercent)),
                  p(e, !1, e.settings.overScrollWidth, !1),
                  C(e, "top", 0, !1, !1, !0),
                  C(e, "left", 0, !1, !1, !0),
                  t(e.scrollbarXRail, { display: "" }),
                  t(e.scrollbarYRail, { display: "" }));
              }));
          }),
          (R.prototype.setScrollLeft = function (e, u, t) {
            L(this._getAnimationSettings(e, "right", u, t));
          }),
          (R.prototype.setScrollLeftImmediately = function (e) {
            ((this.element.scrollLeft = 0 | e), this.update());
          }),
          (R.prototype.setScrollTop = function (e, u, t) {
            L(this._getAnimationSettings(e, "bottom", u, t));
          }),
          (R.prototype.setScrollTopImmediately = function (e) {
            ((this.element.scrollTop = 0 | e), this.update());
          }),
          (R.prototype.onScroll = function (e) {
            this.isAlive && p(this, !1, this.settings.overScrollWidth, !0);
          }),
          (R.prototype.onWheel = function (e) {
            this.isAlive &&
              (p(this, !1, this.settings.overScrollWidth, !1),
              C(this, "left", this.element.scrollLeft - this.lastScrollLeft),
              (this.lastScrollLeft = this.element.scrollLeft));
          }),
          (R.prototype.destroy = function () {
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
          (R.prototype.removePsClasses = function () {
            this.element.className = this.element.className
              .split(" ")
              .filter(function (e) {
                return !e.match(/^ps([-_].+|)$/);
              })
              .join(" ");
          }),
          (e.exports = R));
      },
      7078: (e, u, t) => {
        t.d(u, { t: () => s });
        var n = t(6179),
          o = t.n(n),
          r = t(2056);
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
        const s = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                o = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
              return o;
            })(e, i);
          return o().createElement(
            r.u,
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
        t.d(u, { l: () => a });
        var n = t(6179),
          o = t.n(n),
          r = t(7078),
          i = t(6373),
          l = t(2056);
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
        const a = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const n = o().createElement("div", { className: t }, e);
          if (u.header || u.body) return o().createElement(i.i, u, n);
          const a = u.contentId,
            c = u.args,
            d = null == c ? void 0 : c.contentId;
          return a || d
            ? o().createElement(l.u, s({}, u, { contentId: a || d }), n)
            : o().createElement(r.t, u, n);
        };
      },
      6373: (e, u, t) => {
        t.d(u, { i: () => a });
        var n = t(2056),
          o = t(6179),
          r = t.n(o);
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
        const s = R.views.common.tooltip_window.simple_tooltip_content,
          a = (e) => {
            let u = e.children,
              t = e.body,
              a = e.header,
              c = e.note,
              d = e.alert,
              E = e.args,
              A = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  o = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
                return o;
              })(e, i);
            const F = (0, o.useMemo)(() => {
              const e = Object.assign({}, E, { body: t, header: a, note: c, alert: d });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [d, t, a, c, E]);
            return r().createElement(
              n.u,
              l(
                {
                  contentId:
                    ((h = null == E ? void 0 : E.hasHtmlContent),
                    h ? s.SimpleTooltipHtmlContent("resId") : s.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: F,
                },
                A,
              ),
              u,
            );
            var h;
          };
      },
      2056: (e, u, t) => {
        t.d(u, { u: () => a });
        var n = t(7902),
          o = t(4179),
          r = t(6179);
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
        const s = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: o.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          a = (e) => {
            let u = e.children,
              t = e.contentId,
              o = e.args,
              a = e.onMouseEnter,
              c = e.onMouseLeave,
              d = e.onMouseDown,
              E = e.onClick,
              A = e.ignoreShowDelay,
              F = void 0 !== A && A,
              h = e.ignoreMouseClick,
              D = void 0 !== h && h,
              v = e.decoratorId,
              b = void 0 === v ? 0 : v,
              _ = e.isEnabled,
              m = void 0 === _ || _,
              f = e.targetId,
              C = void 0 === f ? 0 : f,
              p = e.onShow,
              B = e.onHide,
              g = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  o = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
                return o;
              })(e, i);
            const w = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              y = (0, r.useMemo)(() => C || (0, n.F)().resId, [C]),
              L = (0, r.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (s(t, b, { isMouseEvent: !0, on: !0, arguments: l(o) }, y),
                  p && p(),
                  (w.current.isVisible = !0));
              }, [t, b, o, y, p]),
              S = (0, r.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    s(t, b, { on: !1 }, y),
                    w.current.isVisible && B && B(),
                    (w.current.isVisible = !1));
                }
              }, [t, b, y, B]),
              T = (0, r.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(w.current.prevTarget) && S();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", T, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", T, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === m && S();
              }, [m, S]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", S),
                  () => {
                    (window.removeEventListener("mouseleave", S), S());
                  }
                ),
                [S],
              ));
            return m
              ? (0, r.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((k = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(L, F ? 100 : 400)),
                            a && a(e),
                            k && k(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (S(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === D && S(), null == E || E(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === D && S(), null == d || d(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    g,
                  ),
                )
              : u;
            var k;
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
        (t.r(u), t.d(u, { mouse: () => l, onResize: () => r }));
        var n = t(2472),
          o = t(1176);
        const r = (0, n.E)("clientResized"),
          i = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const l = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, o.R)(!1);
          }
          function t() {
            e.enabled && (0, o.R)(!0);
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
              : (0, o.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let o = !0;
                  const r = `mouse${u}`,
                    l = i[u]((e) => t([e, "outside"]));
                  function s(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, s),
                    n(),
                    () => {
                      o &&
                        (l(), window.removeEventListener(r, s), (e.listeners -= 1), n(), (o = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
            },
            enableOutside() {
              e.enabled && (0, o.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, o.R)(!1);
            },
          });
        })();
      },
      5959: (e, u, t) => {
        (t.r(u),
          t.d(u, {
            events: () => n,
            getMouseGlobalPosition: () => r,
            getSize: () => o,
            graphicsQuality: () => i,
          }));
        var n = t(527);
        function o(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
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
        t.d(u, { O: () => o });
        var n = t(5959);
        const o = { view: t(7641), client: n };
      },
      3722: (e, u, t) => {
        function n(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function o(e, u, t) {
          return `url(${n(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => o, getTextureUrl: () => n }));
      },
      6112: (e, u, t) => {
        t.d(u, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
        t.d(u, { U: () => o });
        var n = t(2472);
        const o = {
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
            displayStatus: () => o.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => B,
            freezeTextureBeforeResize: () => h,
            getBrowserTexturePath: () => a,
            getDisplayStatus: () => g,
            getScale: () => D,
            getSize: () => E,
            getViewGlobalPosition: () => F,
            isClientAccessible: () => f,
            isEventHandled: () => p,
            isFocused: () => m,
            pxToRem: () => v,
            remToPx: () => b,
            resize: () => A,
            sendEvent: () => i.qP,
            setAnimateWindow: () => _,
            setEventHandled: () => C,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => L,
          }));
        var n = t(3722),
          o = t(6112),
          r = t(6538),
          i = t(8566);
        function l(e) {
          viewEnv.addPreloadTexture(e);
        }
        function s(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function a(e, u, t, n = 1) {
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
        function A(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function F(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: b(u.x), y: b(u.y) };
        }
        function h() {
          viewEnv.freezeTextureBeforeResize();
        }
        function D() {
          return viewEnv.getScale();
        }
        function v(e) {
          return viewEnv.pxToRem(e);
        }
        function b(e) {
          return viewEnv.remToPx(e);
        }
        function _(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function m() {
          return viewEnv.isFocused();
        }
        function f() {
          return viewEnv.isClientAccessible();
        }
        function C() {
          return viewEnv.setEventHandled();
        }
        function p() {
          return viewEnv.isEventHandled();
        }
        function B() {
          viewEnv.forceTriggerMouseMove();
        }
        function g() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(o.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === o.W[u]), e),
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
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, u, t) => {
        t.d(u, { qP: () => a });
        const n = ["args"];
        const o = 2,
          r = 16,
          i = 32,
          l = 64,
          s = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                i = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    o = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
                  return o;
                })(u, n);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, i, {
                      arguments:
                        ((o = r),
                        Object.entries(o).map(([e, u]) => {
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
            var o;
          },
          a = {
            close(e) {
              s("popover" === e ? o : i);
            },
            minimize() {
              s(l);
            },
            move(e) {
              s(r, { isMouseEvent: !0, on: e });
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
      2344: (e, u, t) => {
        t.d(u, { D9: () => o });
        var n = t(2790);
        (t(3469), t(2133), t(579), t(5360), t(9056));
        const o = n.Z;
      },
      6536: (e, u, t) => {
        t(6179);
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
          o = t(5521),
          r = (t(4179), t(6179));
        const i = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function l(e = o.n.NONE, u = i, t = !1) {
          (0, r.useEffect)(() => {
            if (e !== o.n.NONE)
              return (
                window.addEventListener("keydown", r, t),
                () => {
                  window.removeEventListener("keydown", r, t);
                }
              );
            function r(o) {
              if (o.keyCode === e) {
                if (n.O.view.isEventHandled()) return;
                (n.O.view.setEventHandled(), u(o), t && o.stopPropagation());
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
        let o;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(o || (o = {}));
      },
      9056: (e, u, t) => {
        var n = t(4179);
        t(6179);
        n.Sw.instance;
      },
      2790: (e, u, t) => {
        t.d(u, { Z: () => o });
        var n = t(6179);
        const o = (e) => {
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
        t.d(u, { Z: () => r });
        var n = t(6179);
        const o = (e) => {
            if (!e) return !1;
            const u = e.getBoundingClientRect(),
              t = u.width,
              n = u.height;
            return 0 !== t && 0 !== n;
          },
          r = (e) => {
            const u = (0, n.useState)(o(e ? e.current : null)),
              t = u[0],
              r = u[1];
            return (
              (0, n.useEffect)(() => {
                let u = 0;
                const t = () => {
                  u = requestAnimationFrame(() => {
                    o(e ? e.current : null) ? r(!0) : t();
                  });
                };
                return (
                  t(),
                  () => {
                    cancelAnimationFrame(u);
                  }
                );
              }, [e]),
              (0, n.useEffect)(() => () => r(!1), [e]),
              t
            );
          };
      },
      5521: (e, u, t) => {
        let n, o;
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
          })(o || (o = {})));
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
        t.d(u, { Z: () => r });
        var n = t(3138);
        class o {
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
            return (window.__dataTracker || (window.__dataTracker = new o()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, o = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = n.O.view.addModelObserver(e, t, o);
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
        o.__instance = void 0;
        const r = o;
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
        t.d(u, { c1: () => p, Sw: () => r.Z, B0: () => s, ry: () => b });
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
        const o = n;
        var r = t(1358);
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
        let s;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(s || (s = {}));
        const a = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var A = t(5521),
          F = t(3138);
        const h = ["args"];
        function D(e, u, t, n, o, r, i) {
          try {
            var l = e[r](i),
              s = l.value;
          } catch (e) {
            return void t(e);
          }
          l.done ? u(s) : Promise.resolve(s).then(n, o);
        }
        const v = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          b = (function () {
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
                  return new Promise(function (n, o) {
                    var r = e.apply(u, t);
                    function i(e) {
                      D(r, n, o, i, l, "next", e);
                    }
                    function l(e) {
                      D(r, n, o, i, l, "throw", e);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          _ = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const o = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    o = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
                  return o;
                })(u, h);
              void 0 !== o
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((n = o),
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
          m = () => _(s.CLOSE),
          f = (e, u) => {
            e.keyCode === A.n.ESCAPE && u();
          };
        var C = t(7572);
        const p = o.instance,
          B = {
            DataTracker: r.Z,
            ViewModel: C.Z,
            ViewEventType: s,
            NumberFormatType: a,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: E,
            makeGlobalBoundingBox: v,
            sendMoveEvent: (e) => _(s.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: m,
            sendClosePopOverEvent: () => _(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              _(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, o = R.invalid("resId"), r) => {
              const i = F.O.view.getViewGlobalPosition(),
                l = t.getBoundingClientRect(),
                a = l.x,
                c = l.y,
                d = l.width,
                E = l.height,
                A = {
                  x: F.O.view.pxToRem(a) + i.x,
                  y: F.O.view.pxToRem(c) + i.y,
                  width: F.O.view.pxToRem(d),
                  height: F.O.view.pxToRem(E),
                };
              _(s.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: o,
                direction: u,
                bbox: v(A),
                on: !0,
                args: r,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => f(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              f(e, m);
            },
            handleViewEvent: _,
            onBindingsReady: b,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const n in u)
                if (Object.prototype.hasOwnProperty.call(u, n)) {
                  const o = Object.prototype.toString.call(u[n]);
                  if (o.startsWith("[object CoherentArrayProxy]")) {
                    const o = u[n];
                    t[n] = [];
                    for (let u = 0; u < o.length; u++) t[n].push({ value: e(o[u].value) });
                  } else
                    o.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = e(u[n]))
                      : (t[n] = u[n]);
                }
              return t;
            },
            ClickOutsideManager: p,
            SystemLocale: i,
            UserLocale: l,
          };
        window.ViewEnvHelper = B;
      },
      9220: (e, u, t) => {
        var n = t(6483),
          o = t.n(n),
          r = t(3415),
          i = t(1856),
          l = t(8526),
          s = t(6179),
          a = t.n(s);
        var c = t(5521),
          d = t(4179);
        let E, A;
        (!(function (e) {
          ((e.Basic = "basic"),
            (e.Disabled = "disabled"),
            (e.Focused = "focused"),
            (e.Alert = "alert"),
            (e.Selected = "selected"));
        })(E || (E = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"));
          })(A || (A = {})));
        var F = t(6373);
        const h = "TextOverflow_base_3b",
          D = ({ content: e, classMix: u }) => {
            const t = (0, s.useRef)(null),
              n = (0, s.useState)(!0),
              r = n[0],
              l = n[1];
            return (
              (0, s.useEffect)(() =>
                (0, i.v)(() => {
                  const e = t.current;
                  e && e.offsetWidth >= e.scrollWidth && l(!1);
                }),
              ),
              a().createElement(
                F.i,
                { isEnabled: r, body: e },
                a().createElement("div", { ref: t, className: o()(h, u) }, e),
              )
            );
          };
        var v = t(7727);
        const b = {
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
        let _;
        !(function (e) {
          ((e.Out = "out"), (e.Over = "over"), (e.Down = "down"));
        })(_ || (_ = {}));
        const m = (0, s.memo)(
          ({
            parentId: e,
            variant: u = E.Basic,
            size: t = A.Medium,
            isOpen: n,
            placeholder: r = R.strings.common.dropdown.placeholder.select(),
            label: i = "",
            classMix: l,
            onClick: c,
            soundHover: d,
            soundClick: F,
            customControl: h,
          }) => {
            const m = (0, s.useState)(_.Out),
              f = m[0],
              C = m[1],
              p = (0, s.useState)(!1),
              B = p[0],
              g = p[1],
              w = u === E.Disabled,
              y = w || u === E.Basic,
              L = (0, s.useCallback)(() => {
                w || (C(_.Over), d && (0, v.G)(d));
              }, [w, d]),
              S = (0, s.useCallback)(() => {
                w || (C(_.Down), F && (0, v.G)(F));
              }, [w, F]),
              T = (0, s.useCallback)(() => {
                (!w && C(_.Over), !y && g(!0));
              }, [w, y]),
              k = (0, s.useCallback)((e) => c && c(e), [c]),
              M = (0, s.useCallback)(() => C(_.Out), []);
            ((0, s.useEffect)(() => {
              y || g(!1);
            }, [u, y]),
              (0, s.useEffect)(() => {
                w && M();
              }, [w, M]));
            const O = o()(
              b.base,
              n && b.base__open,
              b[`base__${f}`],
              (y || !B) && b[`base__${u}`],
              l,
            );
            return a().createElement(
              "div",
              {
                id: e ? `${e}_control` : void 0,
                className: O,
                onMouseEnter: L,
                onMouseUp: T,
                onMouseDown: S,
                onMouseLeave: M,
                onClick: k,
              },
              !B && u === E.Alert && a().createElement("div", { className: b.alert }),
              a().createElement(
                "div",
                { className: o()(b.label, b[`label__${t}`], !i && b.label__placeholder) },
                h || a().createElement(D, { content: i || r }),
              ),
              a().createElement(
                "div",
                { className: o()(b.button, b[`button__${t}`]) },
                a().createElement("div", { className: o()(b.arrow, b[`arrow__${t}`]) }),
                f === _.Over && a().createElement("div", { className: b.gradient }),
                w && a().createElement("div", { className: b.disabled }),
              ),
            );
          },
        );
        var f = t(2344);
        var C = t(570);
        const p = [
          "children",
          "isEnabled",
          "selectedItemId",
          "scrollAreaKey",
          "withCompleteTrigger",
          "containerClasses",
        ];
        function B() {
          return (
            (B =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            B.apply(this, arguments)
          );
        }
        const g = (e) => {
            let u = e.children,
              t = e.isEnabled,
              n = void 0 === t || t,
              o = e.selectedItemId,
              r = e.scrollAreaKey,
              l = void 0 === r ? "scrollArea" : r,
              c = e.withCompleteTrigger,
              d = void 0 !== c && c,
              E = e.containerClasses,
              A = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  o = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
                return o;
              })(e, p);
            const F = (0, s.useState)(!1),
              h = F[0],
              D = F[1],
              v = (0, s.useRef)({}),
              b = (0, s.useRef)(null),
              _ = (0, s.useRef)(null),
              m = (0, s.useRef)(null),
              f = (0, s.useCallback)(() => {
                D(!0);
              }, []),
              g = (0, s.useCallback)(() => {
                D(!1);
              }, []),
              w = (0, s.useCallback)(() => {
                const e = m.current,
                  u = b.current,
                  t = v.current;
                if (e && t && u) {
                  const n = e.offsetTop + 0.5 * (e.offsetHeight - u.offsetHeight);
                  t.setScrollTop(n, void 0, d ? f : void 0);
                }
              }, [f, d]);
            (0, s.useEffect)(() => {
              if (n && null !== o) return (0, i.v)(w);
            }, [l, w, o, n]);
            const y = !(!_.current || !_.current.scrollbar) && _.current.scrollbar.scrollbarYActive,
              L = {
                scrollContainerRef: b,
                selectedItemRef: m,
                selectedItemId: o,
                isScrollComplete: h,
                scrollbarActive: y,
                onScrollAnimationComplete: g,
              },
              S = (0, s.cloneElement)(u, L);
            return a().createElement(
              "div",
              { className: E, ref: b },
              a().createElement(C.x, B({ ref: _, key: l, scrollAreaContainer: v.current }, A), S),
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
        const L = (0, s.memo)((e) => {
            let u = e.size,
              t = e.classMix,
              n = e.onClick,
              r = e.itemRenderer,
              i = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  o = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (o[t] = e[t]));
                return o;
              })(e, y);
            const l = i.id,
              c = i.isSelected,
              d = i.isDisabled,
              E = i.label,
              A = i.soundHover,
              F = i.soundClick,
              h = (0, s.useCallback)(
                (e) => {
                  d || (n && n(e, l));
                },
                [l, d, n],
              ),
              D = (0, s.useCallback)(() => {
                d || (A && (0, v.G)(A));
              }, [d, A]),
              b = (0, s.useCallback)(() => {
                d || (F && (0, v.G)(F));
              }, [d, F]),
              _ = o()(
                w.base,
                u && w[`base__${u}`],
                c && w.base__selected,
                d && w.base__disabled,
                t,
              );
            return a().createElement(
              "div",
              { className: _, onMouseEnter: D, onMouseDown: b, onClick: h },
              r ? r(i) : E,
            );
          }),
          S = { base__withScroll: "DropDownItems_base__withScroll_19" };
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        const k = ({
            size: e,
            items: u,
            selectedIds: t,
            selectedItemId: n,
            selectedItemRef: r,
            onClick: i,
            parentId: l,
            soundHover: s,
            soundClick: c,
            itemClassMix: d,
            itemRenderer: E,
            scrollbarActive: A,
          }) =>
            a().createElement(
              "div",
              { className: o()(S.base, A && S.base__withScroll) },
              u.map((u) => {
                const o = `${l}_${u.id}`;
                return a().createElement(
                  "div",
                  { id: l ? o : void 0, key: o, ref: u.id === n ? r : null },
                  a().createElement(
                    L,
                    T({ size: e, soundHover: s, soundClick: c, classMix: d, itemRenderer: E }, u, {
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
          O = {
            handlers: ["click-rail", "keyboard", "wheel", "drag-thumb"],
            wheelSpeed: 6,
            suppressScrollX: !0,
            animationDuration: 300,
            minScrollbarLength: 20,
          },
          P = ({
            parentId: e,
            size: u = A.Medium,
            items: t,
            selectedIds: n,
            isOpen: r,
            autoScroll: i,
            classMix: l,
            itemClassMix: c,
            itemRenderer: d,
            onClick: E,
            soundHover: F,
            soundClick: h,
          }) => {
            const D = (0, s.useState)(null),
              v = D[0],
              b = D[1],
              _ = (0, f.D9)(r);
            (0, s.useEffect)(() => {
              if (r && !_) {
                const e = ((e, u) => {
                  if (!u.length) return null;
                  const t = e.find((e) => u.includes(e.id));
                  return t ? t.id : null;
                })(t, n);
                null !== e && b(e);
              }
              r || b(null);
            }, [r, t, n, _]);
            const m = e ? `${e}_list` : void 0;
            return a().createElement(
              "div",
              { id: m, className: o()(M.base, M[`base__${u}`], l) },
              a().createElement(
                g,
                { selectedItemId: v, isEnabled: i, scrollSettings: O, classMix: M.scrollMix },
                a().createElement(k, {
                  parentId: e,
                  items: t,
                  size: u,
                  selectedIds: n,
                  onClick: E,
                  soundHover: F,
                  soundClick: h,
                  itemClassMix: c,
                  itemRenderer: d,
                }),
              ),
            );
          },
          x = {
            base: "PureDropDown_base_fc",
            base__small: "PureDropDown_base__small_a6",
            base__medium: "PureDropDown_base__medium_05",
            control__down: "PureDropDown_control__down_18",
            list: "PureDropDown_list_28",
            list__up: "PureDropDown_list__up_a1",
            list__down: "PureDropDown_list__down_c4",
            list__under: "PureDropDown_list__under_64",
            list__above: "PureDropDown_list__above_c8",
          };
        (0, s.memo)(
          ({
            componentId: e,
            containerRef: u,
            items: t,
            selected: n = [],
            variant: F = E.Basic,
            size: h = A.Medium,
            multiple: D = !1,
            autoScroll: v = !0,
            placeholder: b,
            classMix: _,
            controlRenderer: f,
            itemRenderer: C,
            open: p,
            tooltipArgs: B,
            onChanges: g,
            onOpen: w,
            onClose: y,
            onClick: L,
            onClickOutside: S,
            onMouseEnter: T,
            onMouseDown: k,
            onMouseUp: M,
            onMouseLeave: O,
            soundHover: R = "highlight",
            soundClick: Y = "play",
            soundItemHover: W,
            soundItemClick: H,
          }) => {
            const I = (0, s.useRef)(null),
              X = (0, s.useRef)(null),
              N = (0, s.useRef)({ open: !1, listAbove: !1 }),
              U = (0, s.useState)(!1),
              j = U[0],
              z = U[1],
              K = (0, s.useState)(!1),
              V = K[0],
              q = K[1],
              G = (0, s.useState)(window.innerHeight),
              Z = G[0],
              $ = G[1],
              Q = ((e, u) => {
                const t = Array.isArray(e) ? e : [e];
                return !u && t.length > 1 ? t.slice(0, 1) : t;
              })(n, D),
              J = F !== E.Disabled,
              ee = void 0 === p,
              ue = Boolean(ee ? j : p);
            var te, ne;
            ((te = () => {
              $(window.innerHeight);
            }),
              (ne = []),
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", te),
                  () => window.removeEventListener("resize", te)
                ),
                ne,
              ));
            const oe = (0, s.useCallback)(() => {
              N.current.open && ((N.current.open = !1), z(!1), y && y());
            }, [y]);
            (0, l.gd)(ue ? c.n.ESCAPE : c.n.NONE, oe, ue);
            const re = (0, s.useCallback)(() => {
              (S && S(), ee && (z(!1), (N.current.open = !1), y && y()));
            }, [S, y, ee]);
            ((0, s.useEffect)(() => {
              const e = I.current;
              if (e && ue)
                return (
                  d.c1.register(e, re),
                  () => {
                    d.c1.unregister(e, re);
                  }
                );
            }, [ue, re]),
              (0, s.useEffect)(() => {
                void 0 !== p && (N.current.open = p);
              }, [p]));
            const ie = (0, s.useCallback)(() => {
              if (!I.current || !X.current) return;
              const e = u && u.current,
                t = e ? e.getBoundingClientRect().bottom : Z,
                n =
                  I.current.getBoundingClientRect().bottom +
                    X.current.getBoundingClientRect().height >
                  t;
              n !== N.current.listAbove && ((N.current.listAbove = n), q(n));
            }, [u, Z]);
            (0, s.useEffect)(() => (0, i.v)(ie), [ie, h, t.length]);
            const le = (0, s.useCallback)(
                (e) => {
                  const u = Q.findIndex((u) => u === e) > -1;
                  let t = [];
                  ((t = D ? (u ? Q.filter((u) => u !== e) : [e, ...Q]) : u ? [] : [e]), g && g(t));
                },
                [D, g, Q],
              ),
              se = (0, s.useCallback)(() => {
                ee &&
                  ((N.current.open = !N.current.open),
                  z(N.current.open),
                  N.current.open ? w && w() : y && y());
              }, [ee, w, y]),
              ae = (0, s.useCallback)(
                (e) => {
                  (J && se(), L && L(e));
                },
                [J, L, se],
              ),
              ce = (0, s.useCallback)(
                (e, u) => {
                  (L && L(e, u), le(u), !D && se());
                },
                [L, D, se, le],
              ),
              de = (0, s.useCallback)((e) => T && T(e), [T]),
              Ee = (0, s.useCallback)((e) => M && M(e), [M]),
              Ae = (0, s.useCallback)((e) => k && k(e), [k]),
              Fe = (0, s.useCallback)((e) => O && O(e), [O]),
              he = (0, s.useMemo)(
                () =>
                  t
                    .filter((e) => Q.includes(e.id))
                    .map((e) => e.label)
                    .join(", "),
                [t, Q],
              ),
              De = (0, s.useMemo)(() => t.filter((e) => Q.includes(e.id)), [t, Q]),
              ve = f ? f(De) : void 0;
            return a().createElement(
              "div",
              {
                id: e,
                ref: I,
                className: o()(x.base, x[`base__${h}`], _ && _.base),
                onMouseEnter: de,
                onMouseUp: Ee,
                onMouseDown: Ae,
                onMouseLeave: Fe,
              },
              a().createElement(
                "div",
                { className: o()(x.control, ue && x.control__down) },
                a().createElement(
                  r.l,
                  { tooltipArgs: B },
                  a().createElement(m, {
                    parentId: e,
                    size: h,
                    variant: F,
                    isOpen: ue,
                    placeholder: b,
                    label: he,
                    classMix: _ && _.control,
                    onClick: ae,
                    soundHover: R,
                    soundClick: Y,
                    customControl: ve,
                  }),
                ),
              ),
              a().createElement(
                "div",
                {
                  ref: X,
                  className: o()(
                    x.list,
                    ue ? x.list__down : x.list__up,
                    V ? x.list__above : x.list__under,
                  ),
                },
                a().createElement(P, {
                  parentId: e,
                  size: h,
                  items: t,
                  selectedIds: Q,
                  isOpen: ue,
                  autoScroll: v,
                  classMix: _ && _.list,
                  itemClassMix: _ && _.item,
                  itemRenderer: C,
                  onClick: ce,
                  soundHover: W || R,
                  soundClick: H || Y,
                }),
              ),
            );
          },
        );
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
        var o = 1 / 0;
        for (s = 0; s < deferred.length; s++) {
          for (var [u, t, n] = deferred[s], r = !0, i = 0; i < u.length; i++)
            (!1 & n || o >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[i]))
              ? u.splice(i--, 1)
              : ((r = !1), n < o && (o = n));
          if (r) {
            deferred.splice(s--, 1);
            var l = t();
            void 0 !== l && (e = l);
          }
        }
        return e;
      }
      n = n || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > n; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [u, t, n];
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
    (__webpack_require__.j = 543),
    (() => {
      var e = { 543: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            o,
            [r, i, l] = t,
            s = 0;
          if (r.some((u) => 0 !== e[u])) {
            for (n in i) __webpack_require__.o(i, n) && (__webpack_require__.m[n] = i[n]);
            if (l) var a = l(__webpack_require__);
          }
          for (u && u(t); s < r.length; s++)
            ((o = r[s]), __webpack_require__.o(e, o) && e[o] && e[o][0](), (e[o] = 0));
          return __webpack_require__.O(a);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [727], () => __webpack_require__(9220));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
