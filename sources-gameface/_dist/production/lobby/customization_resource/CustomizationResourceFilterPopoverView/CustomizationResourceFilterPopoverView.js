(() => {
  var __webpack_modules__ = {
      380: (e) => {
        "use strict";
        function u(e) {
          return getComputedStyle(e);
        }
        function t(e, u) {
          for (var t in u) {
            var r = u[t];
            ("number" == typeof r && (r += "px"), (e.style[t] = r));
          }
          return e;
        }
        function r(e) {
          var u = document.createElement("div");
          return ((u.className = e), u);
        }
        var n =
          "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        function o(e, u) {
          if (!n) throw new Error("No element matching method supported");
          return n.call(e, u);
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
          E = { immediately: !1 };
        function m(e, u, t) {
          void 0 === t && (t = {});
          var r = e.element.classList,
            n = c.scrolling(u);
          r.contains(n) ? clearTimeout(d[u]) : r.add(n);
        }
        function _(e, u, t) {
          void 0 === t && (t = {});
          Object.assign(E, t).immediately
            ? e.isAlive && e.element.classList.remove(c.scrolling(u))
            : (d[u] = setTimeout(function () {
                return e.isAlive && e.element.classList.remove(c.scrolling(u));
              }, e.settings.scrollingThreshold));
        }
        var A = function (e) {
            ((this.element = e), (this.handlers = {}));
          },
          F = { isEmpty: { configurable: !0 } };
        ((A.prototype.bind = function (e, u) {
          (void 0 === this.handlers[e] && (this.handlers[e] = []),
            this.handlers[e].push(u),
            this.element.addEventListener(e, u, !1));
        }),
          (A.prototype.unbind = function (e, u) {
            var t = this;
            this.handlers[e] = this.handlers[e].filter(function (r) {
              return !(!u || r === u) || (t.element.removeEventListener(e, r, !1), !1);
            });
          }),
          (A.prototype.unbindAll = function () {
            for (var e in this.handlers) this.unbind(e);
          }),
          (F.isEmpty.get = function () {
            var e = this;
            return Object.keys(this.handlers).every(function (u) {
              return 0 === e.handlers[u].length;
            });
          }),
          Object.defineProperties(A.prototype, F));
        var D = function () {
          this.eventElements = [];
        };
        function h(e) {
          return parseInt(e, 10) || 0;
        }
        ((D.prototype.eventElement = function (e) {
          var u = this.eventElements.filter(function (u) {
            return u.element === e;
          })[0];
          return (u || ((u = new A(e)), this.eventElements.push(u)), u);
        }),
          (D.prototype.bind = function (e, u, t) {
            this.eventElement(e).bind(u, t);
          }),
          (D.prototype.unbind = function (e, u, t) {
            var r = this.eventElement(e);
            (r.unbind(u, t),
              r.isEmpty && this.eventElements.splice(this.eventElements.indexOf(r), 1));
          }),
          (D.prototype.unbindAll = function () {
            (this.eventElements.forEach(function (e) {
              return e.unbindAll();
            }),
              (this.eventElements = []));
          }),
          (D.prototype.once = function (e, u, t) {
            var r = this.eventElement(e);
            r.bind(u, function e(n) {
              (r.unbind(u, e), t(n));
            });
          }));
        var g = {
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
        function f(e) {
          if ("function" == typeof window.CustomEvent) return new CustomEvent(e);
          var u = document.createEvent("CustomEvent");
          return (u.initCustomEvent(e, !1, !1, void 0), u);
        }
        var b = function (e, u, t, r, n, o) {
          var i;
          if (
            (void 0 === r && (r = !0),
            void 0 === n && (n = !1),
            void 0 === o && (o = !1),
            "top" === u)
          )
            i = ["contentHeight", "containerHeight", "scrollTop", "y", "up", "down"];
          else {
            if ("left" !== u) throw new Error("A proper axis should be provided");
            i = ["contentWidth", "containerWidth", "scrollLeft", "x", "left", "right"];
          }
          !(function (e, u, t, r, n, o) {
            var i = t[0],
              l = t[1],
              a = t[2],
              s = t[3],
              c = t[4],
              d = t[5];
            void 0 === r && (r = !0);
            void 0 === n && (n = !1);
            void 0 === o && (o = !1);
            var E = e.element;
            if (!e.reach) return;
            ((e.reach[s] = null), E[a] < 1 && (e.reach[s] = "start"));
            E[a] > e[i] - e[l] - 1 && (e.reach[s] = "end");
            u &&
              !n &&
              (E.dispatchEvent(f("ps-scroll-" + s)),
              u < 0
                ? E.dispatchEvent(f("ps-scroll-" + c))
                : u > 0 && E.dispatchEvent(f("ps-scroll-" + d)),
              r &&
                (function (e, u) {
                  (m(e, u), _(e, u));
                })(e, s));
            e.reach[s] && (u || o) && E.dispatchEvent(f("ps-" + s + "-reach-" + e.reach[s]));
          })(e, t, i, r, n, o);
        };
        var p = function (e, u, r, n) {
          (void 0 === u && (u = !1), void 0 === r && (r = 0), void 0 === n && (n = !1));
          var o = e.element;
          if (o) {
            if (
              ((e.containerWidth = Math.round(o.getBoundingClientRect().width)),
              (e.containerHeight = Math.round(o.getBoundingClientRect().height)),
              (e.contentWidth = Math.round(o.scrollWidth) - 2 * r),
              (e.contentHeight = Math.round(o.scrollHeight)),
              !n)
            ) {
              e.contentWidth = Math.round(o.scrollWidth) - 2 * r;
              var a = e.contentWidth - e.containerWidth + r;
              o.scrollLeft < r ? (o.scrollLeft = r) : o.scrollLeft > a && (o.scrollLeft = a);
            }
            var d = Math.floor(o.scrollTop),
              E = Math.floor(o.scrollLeft) - r,
              m = parseFloat(getComputedStyle(document.documentElement).fontSize);
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
                  (e.railXWidth = e.containerWidth - e.railXMarginWidth * m - 15 * m),
                  (e.railXRatio = e.containerWidth / e.railXWidth),
                  (e.scrollbarXWidth = B(e, h((e.railXWidth * e.containerWidth) / e.contentWidth))),
                  (e.scrollbarXLeft = h(
                    ((e.negativeScrollAdjustment + E) * (e.railXWidth - e.scrollbarXWidth)) /
                      (e.contentWidth - e.containerWidth),
                  )),
                  e.scrollbarXLeft < 0 && (e.scrollbarXLeft = 0))
                : (e.scrollbarXActive = !1),
              !e.settings.suppressScrollY &&
              e.containerHeight + e.settings.scrollYMarginOffset < e.contentHeight
                ? ((e.scrollbarYActive = !0),
                  (e.railYHeight = e.containerHeight - e.railYMarginHeight * m - 15 * m),
                  (e.railYRatio = e.containerHeight / e.railYHeight),
                  (e.scrollbarYHeight = B(
                    e,
                    h((e.railYHeight * e.containerHeight) / e.contentHeight),
                  )),
                  (e.scrollbarYTop = h(
                    (d * (e.railYHeight - e.scrollbarYHeight)) /
                      (e.contentHeight - e.containerHeight),
                  )))
                : (e.scrollbarYActive = !1),
              e.scrollbarXLeft >= e.railXWidth - e.scrollbarXWidth &&
                (e.scrollbarXLeft = e.railXWidth - e.scrollbarXWidth),
              e.scrollbarYTop >= e.railYHeight - e.scrollbarYHeight &&
                (e.scrollbarYTop = e.railYHeight - e.scrollbarYHeight),
              (function (e, u, r) {
                var n = { width: u.railXWidth },
                  o = Math.floor(e.scrollTop);
                u.isRtl
                  ? (n.left =
                      u.negativeScrollAdjustment + e.scrollLeft + u.containerWidth - u.contentWidth)
                  : (n.left = e.scrollLeft);
                u.isScrollbarXUsingBottom
                  ? (n.bottom = u.scrollbarXBottom - o)
                  : (n.top = u.scrollbarXTop + o);
                t(u.scrollbarXRail, n);
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
                    width: u.scrollbarXWidth - u.railBorderXWidth * r,
                  }),
                  t(u.scrollbarY, {
                    top: u.scrollbarYTop,
                    height: u.scrollbarYHeight - u.railBorderYWidth * r,
                  }));
              })(o, e, m),
              e.scrollbarXButtonStart.classList.toggle("disabled", E < 1),
              e.scrollbarXButtonEnd.classList.toggle(
                "disabled",
                E + e.containerWidth >= e.contentWidth,
              ),
              e.scrollbarYButtonStart.classList.toggle("disabled", o.scrollTop < 1),
              e.scrollbarYButtonEnd.classList.toggle(
                "disabled",
                o.scrollTop + e.containerHeight >= e.contentHeight,
              ),
              e.scrollbarXActive
                ? (o.classList.add(c.active("x")), b(e, "left", E - e.lastScrollLeft, !0, u))
                : (o.classList.remove(c.active("x")),
                  (e.scrollbarXWidth = 0),
                  (e.scrollbarXLeft = 0),
                  (o.scrollLeft = 0)),
              e.scrollbarYActive
                ? (o.classList.add(c.active("y")),
                  b(e, "top", o.scrollTop - e.lastScrollTop, !0, u))
                : (o.classList.remove(c.active("y")),
                  (e.scrollbarYHeight = 0),
                  (e.scrollbarYTop = 0),
                  (o.scrollTop = 0)),
              (e.lastScrollTop = d),
              (e.lastScrollLeft = E),
              (e.scrollTopPercent = o.scrollTop / o.scrollHeight),
              (e.scrollLeftPercent = o.scrollLeft / o.scrollWidth));
          }
        };
        function B(e, u) {
          return (
            e.settings.minScrollbarLength && (u = Math.max(u, e.settings.minScrollbarLength)),
            e.settings.maxScrollbarLength && (u = Math.min(u, e.settings.maxScrollbarLength)),
            u
          );
        }
        var v = {
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
              r = e.x1,
              n = e.y1,
              o = e.x2,
              i = e.y2;
            return (
              1 -
              (r * ((u = t), Math.pow(u, 3)) +
                n *
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
          S = { breakBounds: !1, startBound: 0, endBound: 0 },
          T = function (e) {
            var u = e.scrollableDomEle,
              t = e.onAnimationCompleteCallback,
              r = e.direction,
              n = e.onRefUpdateCallback,
              o = e.duration,
              i = e.cubicBezierPoints,
              l = e.easingPreset,
              a = e.scrollAmount,
              s = e.onCheckForBreakCallback,
              c = e.boundsInfo;
            void 0 === c && (c = S);
            var d = null,
              E = null,
              m = null,
              _ = null,
              A = u === window,
              F = ["left", "right"].indexOf(r) > -1,
              D = ["right", "bottom"].indexOf(r) > -1;
            F
              ? ((E = A ? "scrollX" : "scrollLeft"),
                (_ = A ? "innerWidth" : "width"),
                (m = "scrollWidth"))
              : ((E = A ? "scrollY" : "scrollTop"),
                (_ = A ? "innerHeight" : "height"),
                (m = "scrollHeight"));
            var h = u[E],
              g = (function (e) {
                var u,
                  t = e.isWindow,
                  r = e.scrollableDomEle,
                  n = e.elementLengthProp,
                  o = e.initialScrollPosition,
                  i = e.isHorizontalDirection,
                  l = e.scrollLengthProp,
                  a = e.direction;
                if (t) {
                  var s = document.documentElement;
                  u = i ? s.offsetWidth : s.offsetHeight;
                } else u = (r[l] - r.getBoundingClientRect()[n]) | 0;
                return ["left", "top"].includes(a) ? o : u - o;
              })({
                isWindow: A,
                scrollableDomEle: u,
                elementLengthProp: _,
                initialScrollPosition: h,
                isHorizontalDirection: F,
                scrollLengthProp: m,
                direction: r,
              });
            !isNaN(a) && a < g && (g = a);
            var C = function e(r) {
              if (!s || !s()) {
                var a = r - d,
                  m = (function (e) {
                    var u = e.easingPreset,
                      t = e.cubicBezierPoints,
                      r = e.duration,
                      n = e.runTime / r;
                    if (v.hasOwnProperty(u)) return v[u](n);
                    if (
                      t &&
                      !isNaN(t.x1) &&
                      !isNaN(t.y1) &&
                      !isNaN(t.x2) &&
                      !isNaN(t.y2) &&
                      t.x1 >= 0 &&
                      t.x2 >= 0
                    )
                      return w({ percentTimeElapsed: n, x1: t.x1, x2: t.x2, y1: t.y1, y2: t.y2 });
                    throw new Error("Please enter a valid easing value");
                  })({ easingPreset: l, cubicBezierPoints: i, runTime: a, duration: o });
                if (!isNaN(m)) {
                  var _ = Math.round(m * g),
                    C = D ? _ + h : g - _;
                  if (
                    (c.breakBounds &&
                      (C < c.startBound ? (C = c.startBound) : C > c.endBound && (C = c.endBound)),
                    a < o)
                  ) {
                    if (A) {
                      var f = F ? C : 0,
                        b = F ? 0 : C;
                      window.scrollTo(f, b);
                    } else u[E] = C;
                    (n && n(C), requestAnimationFrame(e));
                  } else t && t();
                }
              }
            };
            requestAnimationFrame(function (e) {
              ((d = e), C(e));
            });
          },
          y = function (e) {
            var u = e.axis,
              t = e.cursorPositionOnRail,
              r = e.direction,
              n = e.i,
              o = (function (e) {
                var u = e.axis,
                  t = e.i,
                  r = e.cursorPositionOnRail;
                if ("y" === u) {
                  var n = t.scrollbarY.offsetTop,
                    o = n + t.scrollbarYHeight;
                  return r >= n && r <= o;
                }
                var i = t.scrollbarX.offsetLeft,
                  l = i + t.scrollbarXWidth;
                return r >= i && r <= l;
              })({ axis: u, i: n, cursorPositionOnRail: t });
            return o
              ? ((function (e) {
                  var u = e.axis,
                    t = e.i,
                    r = e.cursorPositionOnRail,
                    n = (function (e, u) {
                      if ("y" === e) {
                        var t = u.contentHeight - u.containerHeight;
                        return {
                          rail: u.railYHeight,
                          content: u.contentHeight,
                          scrollbar: u.scrollbarYHeight,
                          maxScroll: t,
                        };
                      }
                      var r = u.contentWidth - u.containerWidth;
                      return {
                        rail: u.railXWidth,
                        content: u.contentWidth,
                        scrollbar: u.scrollbarXWidth,
                        maxScroll: r,
                      };
                    })(u, t),
                    o = (r - n.scrollbar / 2) / n.rail,
                    i = Math.round(Math.min(n.maxScroll, Math.max(0, n.content * o)));
                  "y" === u ? (t.element.scrollTop = i) : (t.element.scrollLeft = i);
                })({ axis: u, i: n, cursorPositionOnRail: t }),
                !0)
              : ("y" === u
                  ? (n.element.scrollTop += r * n.containerHeight)
                  : (n.element.scrollLeft += r * n.containerWidth),
                !1);
          },
          L = function (e, u, t) {
            return function (r) {
              u = u.toLowerCase();
              var n = null,
                o = function () {
                  if (1 === r.buttons) {
                    if (
                      !r.target.closest(".ps__rail-" + u) ||
                      !r.target.closest(".ps__track_" + u)
                    ) {
                      var o = (function (e) {
                          var u = e.axis,
                            t = e.e,
                            r = e.i;
                          return "y" === u
                            ? {
                                cursorPosition: t.screenY,
                                windowScrolled: window.pageYOffset,
                                elementPosition: r.scrollbarYRail.getBoundingClientRect().top,
                              }
                            : {
                                cursorPosition: t.screenX,
                                windowScrolled: window.pageXOffset,
                                elementPosition: r.scrollbarXRail.getBoundingClientRect().left,
                              };
                        })({ axis: u, e: r, i: e }),
                        i = o.cursorPosition - o.windowScrolled - o.elementPosition,
                        l = (function (e) {
                          var u = e.axis,
                            t = e.cursorPositionOnRail,
                            r = e.i;
                          return t > ("y" === u ? r.scrollbarYTop : r.scrollbarXLeft) ? 1 : -1;
                        })({ axis: u, cursorPositionOnRail: i, i: e });
                      (y({ axis: u, cursorPositionOnRail: i, direction: l, i: e }) &&
                        clearTimeout(n),
                        p(e, !1, t));
                    }
                    r.stopPropagation();
                  }
                };
              (o(),
                (n = setInterval(o, 100)),
                e.event.once(e.ownerDocument, "mouseup", function () {
                  clearTimeout(n);
                }));
            };
          };
        function R(e, u, t) {
          var r = t[0],
            n = t[1],
            o = t[2],
            i = t[3],
            l = t[4],
            a = t[5],
            s = t[6],
            d = t[7],
            E = t[8],
            A = e.element,
            F = null,
            D = null,
            g = null;
          function C(t) {
            ((A[s] = h(F + g * (t[o] - D))),
              m(e, d),
              p(e, !1, u),
              t.stopPropagation(),
              t.preventDefault());
          }
          function f() {
            (_(e, d),
              e[E].classList.remove(c.clicking),
              e.event.unbind(e.ownerDocument, "mousemove", C));
          }
          e.event.bind(e[l], "mousedown", function (u) {
            1 === u.buttons &&
              ((F = A[s]),
              (D = u[o]),
              (g = (e[n] - e[r]) / (e[i] - e[a])),
              e.event.bind(e.ownerDocument, "mousemove", C),
              e.event.once(e.ownerDocument, "mouseup", f),
              e[E].classList.add(c.clicking),
              u.stopPropagation(),
              u.preventDefault());
          });
        }
        var O = 1e3,
          x = {
            "click-rail": function (e, u) {
              (e.event.bind(e.scrollbarY, "mousedown", function (e) {
                return e.stopPropagation();
              }),
                e.event.bind(e.scrollbarYRail, "mousedown", L(e, "y", 0)),
                e.event.bind(e.scrollbarX, "mousedown", function (e) {
                  return e.stopPropagation();
                }),
                e.event.bind(e.scrollbarXRail, "mousedown", L(e, "x", u)));
            },
            "drag-thumb": function (e, u) {
              (R(e, u, [
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
                R(e, u, [
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
              e.event.bind(e.ownerDocument, "keydown", function (r) {
                if (
                  !((r.isDefaultPrevented && r.isDefaultPrevented()) || r.defaultPrevented) &&
                  o(t, ":hover")
                ) {
                  var n,
                    i = document.activeElement
                      ? document.activeElement
                      : e.ownerDocument.activeElement;
                  if (i) {
                    if ("IFRAME" === i.tagName) i = i.contentDocument.activeElement;
                    else for (; i.shadowRoot;) i = i.shadowRoot.activeElement;
                    if (
                      o((n = i), "input,[contenteditable]") ||
                      o(n, "select,[contenteditable]") ||
                      o(n, "textarea,[contenteditable]") ||
                      o(n, "button,[contenteditable]")
                    )
                      return;
                  }
                  var l = 0,
                    a = 0;
                  switch (r.which) {
                    case 37:
                      l = r.metaKey ? -e.contentWidth : r.altKey ? -e.containerWidth : -30;
                      break;
                    case 38:
                      a = r.metaKey ? e.contentHeight : r.altKey ? e.containerHeight : 30;
                      break;
                    case 39:
                      l = r.metaKey ? e.contentWidth : r.altKey ? e.containerWidth : 30;
                      break;
                    case 40:
                      a = r.metaKey ? -e.contentHeight : r.altKey ? -e.containerHeight : -30;
                      break;
                    case 32:
                      a = r.shiftKey ? e.containerHeight : -e.containerHeight;
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
                    p(e, !1, u),
                    (function (u, r) {
                      var n = Math.floor(t.scrollTop);
                      if (0 === u) {
                        if (!e.scrollbarYActive) return !1;
                        if (
                          (0 === n && r > 0) ||
                          (n >= e.contentHeight - e.containerHeight && r < 0)
                        )
                          return !e.settings.wheelPropagation;
                      }
                      var o = t.scrollLeft;
                      if (0 === r) {
                        if (!e.scrollbarXActive) return !1;
                        if ((0 === o && u < 0) || (o >= e.contentWidth - e.containerWidth && u > 0))
                          return !e.settings.wheelPropagation;
                      }
                      return !0;
                    })(l, a) && r.preventDefault());
                }
              });
            },
            wheel: function (e, t) {
              var r = e.element;
              function n(n) {
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
                  })(n),
                  i = o[0],
                  l = o[1];
                if (
                  !(function (e, t, n) {
                    if (!g.isWebKit && r.querySelector("select")) return !0;
                    if (!r.contains(e)) return !1;
                    for (var o = e; o && o !== r;) {
                      if (o.classList.contains(s.consuming)) return !0;
                      var i = u(o);
                      if ([i.overflow, i.overflowX, i.overflowY].join("").match(/(scroll|auto)/)) {
                        var l = o.scrollHeight - o.clientHeight;
                        if (
                          l > 0 &&
                          !((0 === o.scrollTop && n > 0) || (o.scrollTop === l && n < 0))
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
                  })(n.target, i, l)
                ) {
                  var a = !1,
                    c = (i * e.settings.wheelSpeed) | 0,
                    d = (l * e.settings.wheelSpeed) | 0;
                  (e.settings.useBothWheelAxes
                    ? e.scrollbarYActive && !e.scrollbarXActive
                      ? (l ? (r.scrollTop -= d) : (r.scrollTop += c), (a = !0))
                      : e.scrollbarXActive &&
                        !e.scrollbarYActive &&
                        (i ? (r.scrollLeft += c) : (r.scrollLeft -= d), (a = !0))
                    : ((r.scrollTop -= d), (r.scrollLeft += c)),
                    p(e, !1, t),
                    (a =
                      a ||
                      (function (u, t) {
                        var n = Math.floor(r.scrollTop),
                          o = 0 === r.scrollTop,
                          i = n + r.offsetHeight === r.scrollHeight,
                          l = 0 === r.scrollLeft,
                          a = r.scrollLeft + r.offsetWidth === r.scrollWidth;
                        return (
                          !(Math.abs(t) > Math.abs(u) ? o || i : l || a) ||
                          !e.settings.wheelPropagation
                        );
                      })(i, l)),
                    a && !n.ctrlKey && (n.stopPropagation(), n.preventDefault()));
                }
              }
              (e.event.bind(r, "wheel", n),
                void 0 !== window.onmousewheel && e.event.bind(r, "mousewheel", n));
            },
            touch: function (e, t) {
              if (g.supportsTouch || g.supportsIePointer) {
                var r = e.element,
                  n = {},
                  o = 0,
                  i = {},
                  l = null;
                g.supportsTouch
                  ? (e.event.bind(r, "touchstart", E),
                    e.event.bind(r, "touchmove", m),
                    e.event.bind(r, "touchend", _))
                  : g.supportsIePointer &&
                    (window.PointerEvent
                      ? (e.event.bind(r, "pointerdown", E),
                        e.event.bind(r, "pointermove", m),
                        e.event.bind(r, "pointerup", _))
                      : window.MSPointerEvent &&
                        (e.event.bind(r, "MSPointerDown", E),
                        e.event.bind(r, "MSPointerMove", m),
                        e.event.bind(r, "MSPointerUp", _)));
              }
              function a(u, n) {
                ((r.scrollTop -= n), (r.scrollLeft -= u), p(e, !1, t));
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
                  ((n.pageX = u.pageX),
                    (n.pageY = u.pageY),
                    (o = new Date().getTime()),
                    null !== l && clearInterval(l));
                }
              }
              function m(t) {
                if (d(t)) {
                  var l = c(t),
                    E = { pageX: l.pageX, pageY: l.pageY },
                    m = E.pageX - n.pageX,
                    _ = E.pageY - n.pageY;
                  if (
                    (function (e, t, n) {
                      if (!r.contains(e)) return !1;
                      for (var o = e; o && o !== r;) {
                        if (o.classList.contains(s.consuming)) return !0;
                        var i = u(o);
                        if (
                          [i.overflow, i.overflowX, i.overflowY].join("").match(/(scroll|auto)/)
                        ) {
                          var l = o.scrollHeight - o.clientHeight;
                          if (
                            l > 0 &&
                            !((0 === o.scrollTop && n > 0) || (o.scrollTop === l && n < 0))
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
                    })(t.target, m, _)
                  )
                    return;
                  (a(m, _), (n = E));
                  var A = new Date().getTime(),
                    F = A - o;
                  (F > 0 && ((i.x = m / F), (i.y = _ / F), (o = A)),
                    (function (u, t) {
                      var n = Math.floor(r.scrollTop),
                        o = r.scrollLeft,
                        i = Math.abs(u),
                        l = Math.abs(t);
                      if (l > i) {
                        if (
                          (t < 0 && n === e.contentHeight - e.containerHeight) ||
                          (t > 0 && 0 === n)
                        )
                          return 0 === window.scrollY && t > 0 && g.isChrome;
                      } else if (
                        i > l &&
                        ((u < 0 && o === e.contentWidth - e.containerWidth) || (u > 0 && 0 === o))
                      )
                        return !0;
                      return !0;
                    })(m, _) && t.preventDefault());
                }
              }
              function _() {
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
                r = null,
                n = !1,
                o = 0,
                i = 0,
                l = 0;
              function a() {
                e.onScroll();
              }
              function s(r, n, o, i) {
                (void 0 === o && (o = null),
                  void 0 === i && (i = !1),
                  T({
                    scrollableDomEle: t,
                    direction: "right",
                    onRefUpdateCallback: a,
                    duration: n,
                    easingPreset: "easeOutCubic",
                    scrollAmount: r,
                    onCheckForBreakCallback: o,
                    boundsInfo: {
                      breakBounds: i,
                      startBound: u,
                      endBound: e.contentWidth - e.containerWidth + u,
                    },
                  }));
              }
              function d() {
                if (n) return n;
              }
              function E() {
                l = 0;
              }
              function A(n) {
                if (e.scrollbarXActive) {
                  var a = r - n.screenX;
                  ((t.scrollLeft += a), (r = n.screenX));
                  var s = new Date().getTime();
                  if (((o = (a / (s - i)) * 1e3), (i = s), e.onScroll(), u > 0)) {
                    var c = e.contentWidth - e.containerWidth + 2 * u;
                    0 === t.scrollLeft || t.scrollLeft === c
                      ? 0 === l && (l = window.setTimeout(E, 250))
                      : 0 !== l && (window.clearTimeout(l), (l = 0));
                  }
                  (m(e, "x"),
                    m(e, "dragging", { immediately: !0 }),
                    n.stopPropagation(),
                    n.preventDefault());
                }
              }
              function F(e) {
                ((r = e.screenX),
                  (n = !0),
                  requestAnimationFrame(function () {
                    n = !1;
                  }),
                  (i = new Date().getTime()));
              }
              function D(r) {
                var n = e.contentWidth - e.containerWidth + u;
                if (t.scrollLeft < u) s(u - t.scrollLeft, O, d);
                else if (t.scrollLeft > n) s(n - t.scrollLeft, O, d);
                else {
                  new Date().getTime() - i < 100 && s(o / 4, O, d, !0);
                }
                (_(e, "x"),
                  _(e, "dragging", { immediately: !0 }),
                  e.scrollbarXRail.classList.remove(c.clicking),
                  e.event.unbind(e.ownerDocument, "mousemove", A));
              }
              function h() {
                n = !0;
              }
              t.addEventListener(
                "mousedown",
                function (u) {
                  1 === u.buttons &&
                    ((r = u.screenX),
                    e.event.bind(e.ownerDocument, "mousemove", A),
                    e.event.once(e.ownerDocument, "mouseup", D),
                    e.event.once(e.ownerDocument, "mousedown", F),
                    e.event.once(t, "wheel", h),
                    e.scrollbarXRail.classList.add(c.clicking),
                    u.preventDefault());
                },
                !1,
              );
            },
          },
          M = function (e, n) {
            var o = this;
            if (
              (void 0 === n && (n = {}),
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
            n))
              o.settings[i] = n[i];
            ((this.containerWidth = null),
              (this.containerHeight = null),
              (this.contentWidth = null),
              (this.contentHeight = null));
            var l,
              d,
              E = function () {
                return e.classList.add(c.focus);
              },
              m = function () {
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
              (this.event = new D()),
              (this.ownerDocument = e.ownerDocument || document),
              (this.scrollbarXRail = r(s.rail("x"))),
              (this.scrollbarXButtonStart = r(s.buttonStart("x"))),
              (this.scrollbarXButtonEnd = r(s.buttonEnd("x"))),
              (this.scrollbarXTrack = r(s.track("x"))),
              e.appendChild(this.scrollbarXRail),
              this.scrollbarXRail.appendChild(this.scrollbarXTrack),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonStart),
              this.scrollbarXRail.appendChild(this.scrollbarXButtonEnd),
              (this.scrollbarX = r(s.thumb("x"))),
              this.scrollbarXRail.appendChild(this.scrollbarX),
              this.scrollbarX.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarX, "focus", E),
              this.event.bind(this.scrollbarX, "blur", m),
              (this.scrollbarXActive = null),
              (this.scrollbarXWidth = null),
              (this.scrollbarXLeft = null),
              (this.scrollbarYRail = r(s.rail("y"))),
              (this.scrollbarYButtonStart = r(s.buttonStart("y"))),
              (this.scrollbarYButtonEnd = r(s.buttonEnd("y"))),
              (this.scrollbarYTrack = r(s.track("y"))),
              e.appendChild(this.scrollbarYRail),
              this.scrollbarYRail.appendChild(this.scrollbarYTrack),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonStart),
              this.scrollbarYRail.appendChild(this.scrollbarYButtonEnd),
              (this.scrollbarY = r(s.thumb("y"))),
              this.scrollbarYRail.appendChild(this.scrollbarY),
              this.scrollbarY.setAttribute("tabindex", 0),
              this.event.bind(this.scrollbarY, "focus", E),
              this.event.bind(this.scrollbarY, "blur", m),
              (this.scrollbarYActive = null),
              (this.scrollbarYHeight = null),
              (this.scrollbarYTop = null),
              C().then(function () {
                var r = u(o.scrollbarXRail);
                ((o.scrollbarXBottom = parseInt(r.bottom, 10)),
                  isNaN(o.scrollbarXBottom)
                    ? ((o.isScrollbarXUsingBottom = !1), (o.scrollbarXTop = h(r.top)))
                    : (o.isScrollbarXUsingBottom = !0),
                  (o.railBorderXWidth = h(r.borderLeftWidth) + h(r.borderRightWidth)),
                  t(o.scrollbarXRail, { display: "block" }),
                  (o.railXMarginWidth = h(r.marginLeft) + h(r.marginRight)),
                  t(o.scrollbarXRail, { display: "" }),
                  (o.railXWidth = null),
                  (o.railXRatio = null));
                var n = u(o.scrollbarYRail);
                ((o.scrollbarYRight = parseInt(n.right, 10)),
                  isNaN(o.scrollbarYRight)
                    ? ((o.isScrollbarYUsingRight = !1), (o.scrollbarYLeft = h(n.left)))
                    : (o.isScrollbarYUsingRight = !0),
                  (o.scrollbarYOuterWidth = o.isRtl
                    ? (function (e) {
                        var t = u(e);
                        return (
                          h(t.width) +
                          h(t.paddingLeft) +
                          h(t.paddingRight) +
                          h(t.borderLeftWidth) +
                          h(t.borderRightWidth)
                        );
                      })(o.scrollbarY)
                    : null),
                  (o.railBorderYWidth = h(n.borderTopWidth) + h(n.borderBottomWidth)),
                  t(o.scrollbarYRail, { display: "block" }),
                  (o.railYMarginHeight = h(n.marginTop) + h(n.marginBottom)),
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
                    return x[e](o, o.settings.overScrollWidth);
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
                  p(o, !1, o.settings.overScrollWidth, !1));
              }));
          };
        ((M.prototype._getAnimationSettings = function (e, u, t, r) {
          var n = this,
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
                (p(n, !0, n.settings.overScrollWidth, !1), t && t(e));
              },
              onAnimationCompleteCallback: function () {
                r && r();
              },
            }
          );
        }),
          (M.prototype.playHoverSound = function () {
            window.engine && engine.call("PlaySound", "highlight");
          }),
          (M.prototype.playClickSound = function () {
            window.engine && engine.call("PlaySound", "play");
          }),
          (M.prototype.handleMouseEnter = function () {
            this.playHoverSound();
          }),
          (M.prototype.handleMouseLeave = function () {}),
          (M.prototype.update = function () {
            var e = this;
            this.isAlive &&
              ((this.negativeScrollAdjustment = this.isNegativeScroll
                ? this.element.scrollWidth - this.element.clientWidth
                : 0),
              t(this.scrollbarXRail, { display: "block" }),
              t(this.scrollbarYRail, { display: "block" }),
              (this.railXMarginWidth =
                h(u(this.scrollbarXRail).marginLeft) + h(u(this.scrollbarXRail).marginRight)),
              (this.railYMarginHeight =
                h(u(this.scrollbarYRail).marginTop) + h(u(this.scrollbarYRail).marginBottom)),
              t(this.scrollbarXRail, { display: "none" }),
              t(this.scrollbarYRail, { display: "none" }),
              C().then(function () {
                (e.settings.isDisableScrollToLastPositionOnResize ||
                  ((e.element.scrollTop = e.element.scrollHeight * e.scrollTopPercent),
                  (e.element.scrollLeft = e.element.scrollWidth * e.scrollLeftPercent)),
                  p(e, !1, e.settings.overScrollWidth, !1),
                  b(e, "top", 0, !1, !1, !0),
                  b(e, "left", 0, !1, !1, !0),
                  t(e.scrollbarXRail, { display: "" }),
                  t(e.scrollbarYRail, { display: "" }));
              }));
          }),
          (M.prototype.setScrollLeft = function (e, u, t) {
            T(this._getAnimationSettings(e, "right", u, t));
          }),
          (M.prototype.setScrollLeftImmediately = function (e) {
            ((this.element.scrollLeft = 0 | e), this.update());
          }),
          (M.prototype.setScrollTop = function (e, u, t) {
            T(this._getAnimationSettings(e, "bottom", u, t));
          }),
          (M.prototype.setScrollTopImmediately = function (e) {
            ((this.element.scrollTop = 0 | e), this.update());
          }),
          (M.prototype.onScroll = function (e) {
            this.isAlive && p(this, !1, this.settings.overScrollWidth, !0);
          }),
          (M.prototype.onWheel = function (e) {
            this.isAlive &&
              (p(this, !1, this.settings.overScrollWidth, !1),
              b(this, "left", this.element.scrollLeft - this.lastScrollLeft),
              (this.lastScrollLeft = this.element.scrollLeft));
          }),
          (M.prototype.destroy = function () {
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
          (M.prototype.removePsClasses = function () {
            this.element.className = this.element.className
              .split(" ")
              .filter(function (e) {
                return !e.match(/^ps([-_].+|)$/);
              })
              .join(" ");
          }),
          (e.exports = M));
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
      532: (e) => {
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
      887: (e) => {
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
        (t.r(u), t.d(u, { mouse: () => l, onResize: () => o }));
        var r = t(472),
          n = t(176);
        const o = (0, r.E)("clientResized"),
          i = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const l = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, n.R)(!1);
          }
          function t() {
            e.enabled && (0, n.R)(!0);
          }
          function r() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : (0, n.R)(!1);
          }
          const o = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let n = !0;
                  const o = `mouse${u}`,
                    l = i[u]((e) => t([e, "outside"]));
                  function a(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(o, a),
                    r(),
                    () => {
                      n &&
                        (l(), window.removeEventListener(o, a), (e.listeners -= 1), r(), (n = !1));
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
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
            },
            enableOutside() {
              e.enabled && (0, n.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, n.R)(!1);
            },
          });
        })();
      },
      959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => r,
            getMouseGlobalPosition: () => o,
            getSize: () => n,
            graphicsQuality: () => i,
          }));
        var r = t(527);
        function n(e = "px") {
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
      176: (e, u, t) => {
        "use strict";
        function r(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => r });
      },
      472: (e, u, t) => {
        "use strict";
        function r(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        t.d(u, { E: () => r });
      },
      138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => n });
        var r = t(959);
        const n = { view: t(641), client: r };
      },
      722: (e, u, t) => {
        "use strict";
        function r(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function n(e, u, t) {
          return `url(${r(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => n, getTextureUrl: () => r }));
      },
      112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => r });
        const r = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => n });
        var r = t(472);
        const n = {
          onTextureFrozen: (0, r.E)("self.onTextureFrozen"),
          onTextureReady: (0, r.E)("self.onTextureReady"),
          onDomBuilt: (0, r.E)("self.onDomBuilt"),
          onLoaded: (0, r.E)("self.onLoaded"),
          onDisplayChanged: (0, r.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, r.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, r.E)("children.onAdded"),
            onLoaded: (0, r.E)("children.onLoaded"),
            onRemoved: (0, r.E)("children.onRemoved"),
            onAttached: (0, r.E)("children.onAttached"),
            onTextureReady: (0, r.E)("children.onTextureReady"),
            onRequestPosition: (0, r.E)("children.requestPosition"),
          },
        };
      },
      641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => c,
            addPreloadTexture: () => l,
            children: () => r,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => o.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => B,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => v,
            getScale: () => F,
            getSize: () => E,
            getViewGlobalPosition: () => _,
            isClientAccessible: () => f,
            isEventHandled: () => p,
            isFocused: () => C,
            pxToRem: () => D,
            remToPx: () => h,
            resize: () => m,
            sendEvent: () => i.qP,
            setAnimateWindow: () => g,
            setEventHandled: () => b,
            setInputPaddingsRem: () => a,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => T,
          }));
        var r = t(722),
          n = t(112),
          o = t(538),
          i = t(566);
        function l(e) {
          viewEnv.addPreloadTexture(e);
        }
        function a(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function s(e, u, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, r);
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
          return "rem" === e ? u : { x: h(u.x), y: h(u.y) };
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
        function h(e) {
          return viewEnv.remToPx(e);
        }
        function g(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function f() {
          return viewEnv.isClientAccessible();
        }
        function b() {
          return viewEnv.setEventHandled();
        }
        function p() {
          return viewEnv.isEventHandled();
        }
        function B() {
          viewEnv.forceTriggerMouseMove();
        }
        function v() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === n.W[u]), e),
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
          T = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : o.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => s });
        const r = ["args"];
        const n = 2,
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
                    r,
                    n = {},
                    o = Object.keys(e);
                  for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, r);
              return void 0 !== o
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, i, {
                      arguments:
                        ((n = o),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, i));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          s = {
            close(e) {
              a("popover" === e ? n : i);
            },
            minimize() {
              a(l);
            },
            move(e) {
              a(o, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, u, t) => {
        "use strict";
        let r, n;
        (t.d(u, { n: () => r }),
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
          })(n || (n = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => o });
        var r = t(138);
        class n {
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
            return (window.__dataTracker || (window.__dataTracker = new n()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const o = r.O.view.addModelObserver(e, t, n);
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
              const r = this._callbacks[t];
              void 0 !== r && r(e, u);
            });
          }
        }
        n.__instance = void 0;
        const o = n;
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
        t.d(u, { c1: () => v, Sw: () => o.Z, B0: () => a, ry: () => h, Eu: () => g, SW: () => b });
        class r {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let r = e.target;
                  do {
                    if (r === u) return;
                    r = r.parentNode;
                  } while (r);
                  t();
                });
              }));
          }
          static get instance() {
            return (r.__instance || (r.__instance = new r()), r.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              r = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== r,
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
        const n = r;
        var o = t(358);
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
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(521),
          _ = t(138);
        const A = ["args"];
        function F(e, u, t, r, n, o, i) {
          try {
            var l = e[o](i),
              a = l.value;
          } catch (e) {
            return void t(e);
          }
          l.done ? u(a) : Promise.resolve(a).then(r, n);
        }
        const D = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          h = (function () {
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
                  return new Promise(function (r, n) {
                    var o = e.apply(u, t);
                    function i(e) {
                      F(o, r, n, i, l, "next", e);
                    }
                    function l(e) {
                      F(o, r, n, i, l, "throw", e);
                    }
                    i(void 0);
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
          C = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                o = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    n = {},
                    o = Object.keys(e);
                  for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, A);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, o, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, u]) => {
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
            var r;
          },
          f = () => C(a.CLOSE),
          b = () => C(a.POP_OVER, { on: !1 }),
          p = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var B = t(572);
        const v = n.instance,
          w = {
            DataTracker: o.Z,
            ViewModel: B.Z,
            ViewEventType: a,
            NumberFormatType: s,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: E,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => C(a.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: f,
            sendClosePopOverEvent: b,
            sendShowContextMenuEvent: (e, u, t = 0) => {
              C(a.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, r, n = R.invalid("resId"), o) => {
              const i = _.O.view.getViewGlobalPosition(),
                l = t.getBoundingClientRect(),
                s = l.x,
                c = l.y,
                d = l.width,
                E = l.height,
                m = {
                  x: _.O.view.pxToRem(s) + i.x,
                  y: _.O.view.pxToRem(c) + i.y,
                  width: _.O.view.pxToRem(d),
                  height: _.O.view.pxToRem(E),
                };
              C(a.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: r || R.invalid("resId"),
                targetID: n,
                direction: u,
                bbox: D(m),
                on: !0,
                args: o,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => p(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              p(e, f);
            },
            handleViewEvent: C,
            onBindingsReady: h,
            onLayoutReady: g,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(a.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(a.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(a.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const r in u)
                if (Object.prototype.hasOwnProperty.call(u, r)) {
                  const n = Object.prototype.toString.call(u[r]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = u[r];
                    t[r] = [];
                    for (let u = 0; u < n.length; u++) t[r].push({ value: e(n[u].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[r] = e(u[r]))
                      : (t[r] = u[r]);
                }
              return t;
            },
            ClickOutsideManager: v,
            SystemLocale: i,
            UserLocale: l,
          };
        window.ViewEnvHelper = w;
      },
      85: (e, u, t) => {
        "use strict";
        var r = t(179),
          n = t.n(r);
        const o = (e, u, t) =>
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
        var i = t(138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var a;
        function s(e, u, t) {
          const r = (function (e, u) {
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
            n = (function (e, u) {
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
            o = Math.min(r, n);
          return {
            extraLarge: o === t.extraLarge.weight,
            large: o === t.large.weight,
            medium: o === t.medium.weight,
            small: o === t.small.weight,
            extraSmall: o === t.extraSmall.weight,
            extraLargeWidth: r === t.extraLarge.weight,
            largeWidth: r === t.large.weight,
            mediumWidth: r === t.medium.weight,
            smallWidth: r === t.small.weight,
            extraSmallWidth: r === t.extraSmall.weight,
            extraLargeHeight: n === t.extraLarge.weight,
            largeHeight: n === t.large.weight,
            mediumHeight: n === t.medium.weight,
            smallHeight: n === t.small.weight,
            extraSmallHeight: n === t.extraSmall.weight,
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
        })(a || (a = {}));
        const c = i.O.client.getSize("rem"),
          d = c.width,
          E = c.height,
          m = Object.assign({ width: d, height: E }, s(d, E, l)),
          _ = (0, r.createContext)(m),
          A = ["children"];
        const F = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, A);
          const n = (0, r.useContext)(_),
            i = n.extraLarge,
            l = n.large,
            a = n.medium,
            s = n.small,
            c = n.extraSmall,
            d = n.extraLargeWidth,
            E = n.largeWidth,
            m = n.mediumWidth,
            F = n.smallWidth,
            D = n.extraSmallWidth,
            h = n.extraLargeHeight,
            g = n.largeHeight,
            C = n.mediumHeight,
            f = n.smallHeight,
            b = n.extraSmallHeight,
            p = { extraLarge: h, large: g, medium: C, small: f, extraSmall: b };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && i) return u;
            if (t.large && l) return u;
            if (t.medium && a) return u;
            if (t.small && s) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && d) return o(u, t, p);
            if (t.largeWidth && E) return o(u, t, p);
            if (t.mediumWidth && m) return o(u, t, p);
            if (t.smallWidth && F) return o(u, t, p);
            if (t.extraSmallWidth && D) return o(u, t, p);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && h) return u;
              if (t.largeHeight && g) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && f) return u;
              if (t.extraSmallHeight && b) return u;
            }
          }
          return null;
        };
        F.defaultProps = {
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
        (0, r.memo)(F);
        const D = (e) => {
            const u = (0, r.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          h = (0, r.memo)(({ children: e }) => {
            const u = (0, r.useContext)(_),
              t = (0, r.useState)(u),
              o = t[0],
              a = t[1],
              c = (0, r.useCallback)((e, u) => {
                const t = i.O.view.pxToRem(e),
                  r = i.O.view.pxToRem(u);
                a(Object.assign({ width: t, height: r }, s(t, r, l)));
              }, []);
            (D(() => {
              engine.on("clientResized", c);
            }),
              (0, r.useEffect)(() => () => engine.off("clientResized", c), [c]));
            const d = (0, r.useMemo)(() => Object.assign({}, o), [o]);
            return n().createElement(_.Provider, { value: d }, e);
          });
        var g = t(483),
          C = t.n(g),
          f = t(926),
          b = t.n(f);
        let p, B, v;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(p || (p = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = l.small.width)] = "Small"),
              (e[(e.Medium = l.medium.width)] = "Medium"),
              (e[(e.Large = l.large.width)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
          })(B || (B = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.small.height)] = "Small"),
              (e[(e.Medium = l.medium.height)] = "Medium"),
              (e[(e.Large = l.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(v || (v = {})));
        const w = () => {
            const e = (0, r.useContext)(_),
              u = e.width,
              t = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return p.ExtraLarge;
                  case e.large:
                    return p.Large;
                  case e.medium:
                    return p.Medium;
                  case e.small:
                    return p.Small;
                  case e.extraSmall:
                    return p.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), p.ExtraSmall);
                }
              })(e),
              o = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return B.ExtraLarge;
                  case e.largeWidth:
                    return B.Large;
                  case e.mediumWidth:
                    return B.Medium;
                  case e.smallWidth:
                    return B.Small;
                  case e.extraSmallWidth:
                    return B.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), B.ExtraSmall);
                }
              })(e),
              i = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return v.ExtraLarge;
                  case e.largeHeight:
                    return v.Large;
                  case e.mediumHeight:
                    return v.Medium;
                  case e.smallHeight:
                    return v.Small;
                  case e.extraSmallHeight:
                    return v.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), v.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: n,
              mediaWidth: o,
              mediaHeight: i,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          S = ["children", "className"];
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        const y = {
            [B.ExtraSmall]: "",
            [B.Small]: b().SMALL_WIDTH,
            [B.Medium]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH}`,
            [B.Large]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH}`,
            [B.ExtraLarge]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH} ${b().EXTRA_LARGE_WIDTH}`,
          },
          L = {
            [v.ExtraSmall]: "",
            [v.Small]: b().SMALL_HEIGHT,
            [v.Medium]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT}`,
            [v.Large]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT}`,
            [v.ExtraLarge]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT} ${b().EXTRA_LARGE_HEIGHT}`,
          },
          O = {
            [p.ExtraSmall]: "",
            [p.Small]: b().SMALL,
            [p.Medium]: `${b().SMALL} ${b().MEDIUM}`,
            [p.Large]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE}`,
            [p.ExtraLarge]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE} ${b().EXTRA_LARGE}`,
          },
          x = (e) => {
            let u = e.children,
              t = e.className,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, S);
            const o = w(),
              i = o.mediaWidth,
              l = o.mediaHeight,
              a = o.mediaSize;
            return n().createElement("div", T({ className: C()(t, y[i], L[l], O[a]) }, r), u);
          },
          M = ["children"];
        const P = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, M);
          return n().createElement(h, null, n().createElement(x, t, u));
        };
        var I = t(493),
          H = t.n(I);
        var k = t(364);
        const N = [
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
        function W(e) {
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
        const Y = (e, u, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: k.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: r,
                },
                t,
              ),
            );
          },
          X = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              o = e.onMouseEnter,
              i = e.onMouseLeave,
              l = e.onMouseDown,
              a = e.onClick,
              s = e.ignoreShowDelay,
              c = void 0 !== s && s,
              d = e.ignoreMouseClick,
              E = void 0 !== d && d,
              m = e.decoratorId,
              _ = void 0 === m ? 0 : m,
              A = e.isEnabled,
              F = void 0 === A || A,
              D = e.targetId,
              h = void 0 === D ? 0 : D,
              g = e.onShow,
              C = e.onHide,
              f = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, N);
            const b = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              p = (0, r.useMemo)(
                () =>
                  h ||
                  ((e = 1) => {
                    const u = new Error().stack;
                    let t,
                      r = R.invalid("resId");
                    return (
                      u &&
                        ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (r = window.subViews[t].id)),
                      { caller: t, stack: u, resId: r }
                    );
                  })().resId,
                [h],
              ),
              B = (0, r.useCallback)(() => {
                (b.current.isVisible && b.current.timeoutId) ||
                  (Y(t, _, { isMouseEvent: !0, on: !0, arguments: W(n) }, p),
                  g && g(),
                  (b.current.isVisible = !0));
              }, [t, _, n, p, g]),
              v = (0, r.useCallback)(() => {
                if (b.current.isVisible || b.current.timeoutId) {
                  const e = b.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (b.current.timeoutId = 0)),
                    Y(t, _, { on: !1 }, p),
                    b.current.isVisible && C && C(),
                    (b.current.isVisible = !1));
                }
              }, [t, _, p, C]),
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
                !1 === F && v();
              }, [F, v]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", v),
                  () => {
                    (window.removeEventListener("mouseleave", v), v());
                  }
                ),
                [v],
              ));
            return F
              ? (0, r.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((b.current.timeoutId = window.setTimeout(B, c ? 100 : 400)),
                            o && o(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (v(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === E && v(), null == a || a(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === E && v(), null == l || l(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    f,
                  ),
                )
              : u;
            var S;
          },
          G = ["children", "body", "header", "note", "alert", "args"];
        function j() {
          return (
            (j =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            j.apply(this, arguments)
          );
        }
        const U = R.views.common.tooltip_window.simple_tooltip_content,
          z = (e) => {
            let u = e.children,
              t = e.body,
              o = e.header,
              i = e.note,
              l = e.alert,
              a = e.args,
              s = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, G);
            const c = (0, r.useMemo)(() => {
              const e = Object.assign({}, a, { body: t, header: o, note: i, alert: l });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [l, t, o, i, a]);
            return n().createElement(
              X,
              j(
                {
                  contentId:
                    ((d = null == a ? void 0 : a.hasHtmlContent),
                    d ? U.SimpleTooltipHtmlContent("resId") : U.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                s,
              ),
              u,
            );
            var d;
          },
          K = (e) => {
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
          },
          V = (e) => {
            (0, r.useEffect)(e, []);
          };
        function $(e) {
          engine.call("PlaySound", e);
        }
        const q = {
            playHighlight() {
              $("highlight");
            },
            playClick() {
              $("play");
            },
            playYes() {
              $("yes1");
            },
          },
          Q = {
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
        var Z;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(Z || (Z = {}));
        const J = ["__left", "__right", "__top", "__bottom"],
          ee = (0, r.forwardRef)(
            (
              { children: e, disableAutoSizeUpdate: u, onOutsideClick: t, customStyles: o = {} },
              l,
            ) => {
              const a = (0, r.useRef)(null),
                s = (0, r.useRef)(null),
                c = (0, r.useRef)(null),
                d = (0, r.useState)(window.decorator && window.decorator.directionType),
                E = d[0],
                m = d[1],
                _ = (0, r.useCallback)(() => {
                  (q.playClick(), i.O.view.sendEvent.close());
                }, []),
                A = (0, r.useCallback)(() => {
                  q.playHighlight();
                }, []),
                F = C()(Q.arrow, Q[`arrow${J[E]}`]);
              V(
                () => (
                  i.O.client.events.mouse.enableOutside(),
                  i.O.client.events.mouse.down(([, e]) => {
                    "outside" === e && (t ? t() : i.O.view.sendEvent.close("popover"));
                  })
                ),
              );
              const D = (0, r.useCallback)(
                  (e) => {
                    let u = e.target;
                    do {
                      if (u === a.current || u === c.current) return;
                      u = u.parentNode;
                    } while (u);
                    const r = window.decorator;
                    if (void 0 !== window.decorator) {
                      const e = i.O.client.getMouseGlobalPosition(),
                        u = ![r.boundX, r.boundY, r.boundWidth, r.boundHeight].includes(void 0),
                        t =
                          e.x < r.boundX ||
                          e.x > r.boundX + r.boundWidth ||
                          e.y > r.boundY + r.boundHeight ||
                          e.y < r.boundY;
                      if (u && !t) return;
                    }
                    t ? t() : i.O.view.sendEvent.close("popover");
                  },
                  [a, c, t],
                ),
                h = (0, r.useCallback)(
                  () => (
                    i.O.view.freezeTextureBeforeResize(),
                    K(() => {
                      if (s.current) {
                        const e = s.current.scrollWidth,
                          u = s.current.scrollHeight;
                        (i.O.view.resize(e, u), m(window.decorator.directionType));
                      }
                    })
                  ),
                  [],
                );
              return (
                (0, r.useImperativeHandle)(l, () => ({ updateSize: h })),
                V(() => {
                  i.O.view.setInputPaddingsRem(58);
                }),
                (0, r.useEffect)(() => {
                  document.addEventListener("mousedown", D, { capture: !0 });
                  const e = ((e) => {
                    let u = !1;
                    return {
                      promise: new Promise((t, r) => {
                        e.then((e) => !u && t(e)).catch((e) => !u && r(e));
                      }),
                      cancel() {
                        u = !0;
                      },
                    };
                  })((0, k.Eu)());
                  return (
                    !u && e.promise.then(() => h()),
                    () => {
                      (e.cancel(), document.removeEventListener("mousedown", D));
                    }
                  );
                }, [h, D, u]),
                n().createElement(
                  "div",
                  { className: Q.base, ref: s },
                  n().createElement(
                    "div",
                    { className: Q.decorator },
                    n().createElement(
                      "div",
                      { className: Q.content, ref: a },
                      e,
                      window.decorator &&
                        window.decorator.isCloseBtnVisible &&
                        n().createElement(
                          z,
                          { body: R.strings.dialogs.common.error.cancel() },
                          n().createElement("div", {
                            className: Q.closeBtn,
                            onClick: _,
                            onMouseEnter: A,
                            ref: c,
                          }),
                        ),
                    ),
                    n().createElement("div", { className: F, style: o.arrow }),
                  ),
                )
              );
            },
          );
        var ue = t(521);
        const te = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function re(e = ue.n.NONE, u = te, t = !1) {
          (0, r.useEffect)(() => {
            if (e !== ue.n.NONE)
              return (
                window.addEventListener("keydown", r, t),
                () => {
                  window.removeEventListener("keydown", r, t);
                }
              );
            function r(r) {
              if (r.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), u(r), t && r.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        var ne = t(515);
        const oe = {
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
        let ie, le;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(ie || (ie = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(le || (le = {})));
        const ae = ({
          children: e,
          size: u,
          isFocused: t,
          type: o,
          disabled: i,
          mixClass: l,
          soundHover: a,
          soundClick: s,
          onMouseEnter: c,
          onMouseMove: d,
          onMouseDown: E,
          onMouseUp: m,
          onMouseLeave: _,
          onClick: A,
        }) => {
          const F = (0, r.useRef)(null),
            D = (0, r.useState)(t),
            h = D[0],
            g = D[1],
            f = (0, r.useState)(!1),
            b = f[0],
            p = f[1],
            B = (0, r.useState)(!1),
            v = B[0],
            w = B[1],
            S = (0, r.useCallback)(() => {
              i || (F.current && (F.current.focus(), g(!0)));
            }, [i]),
            T = (0, r.useCallback)(
              (e) => {
                h && null !== F.current && !F.current.contains(e.target) && g(!1);
              },
              [h],
            ),
            y = (0, r.useCallback)(
              (e) => {
                i || (A && A(e));
              },
              [i, A],
            ),
            L = (0, r.useCallback)(
              (e) => {
                i || (null !== a && $(a), c && c(e), w(!0));
              },
              [i, a, c],
            ),
            O = (0, r.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            x = (0, r.useCallback)(
              (e) => {
                i || (m && m(e), p(!1));
              },
              [i, m],
            ),
            M = (0, r.useCallback)(
              (e) => {
                i || (null !== s && $(s), E && E(e), t && S(), p(!0));
              },
              [i, s, E, S, t],
            ),
            P = (0, r.useCallback)(
              (e) => {
                i || (_ && _(e), p(!1));
              },
              [i, _],
            ),
            I = C()(
              oe.base,
              oe[`base__${o}`],
              {
                [oe.base__disabled]: i,
                [oe[`base__${u}`]]: u,
                [oe.base__focus]: h,
                [oe.base__highlightActive]: b,
                [oe.base__firstHover]: v,
              },
              l,
            ),
            H = C()(oe.state, oe.state__default);
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
              g(t);
            }, [t]),
            n().createElement(
              "div",
              {
                ref: F,
                className: I,
                onMouseEnter: L,
                onMouseMove: O,
                onMouseUp: x,
                onMouseDown: M,
                onMouseLeave: P,
                onClick: y,
              },
              o !== ie.ghost &&
                n().createElement(
                  n().Fragment,
                  null,
                  n().createElement("div", { className: oe.back }),
                  n().createElement("span", { className: oe.texture }),
                ),
              n().createElement(
                "span",
                { className: H },
                n().createElement("span", { className: oe.stateDisabled }),
                n().createElement("span", { className: oe.stateHighlightHover }),
                n().createElement("span", { className: oe.stateHighlightActive }),
              ),
              n().createElement(
                "span",
                { className: oe.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        ae.defaultProps = {
          type: ie.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const se = (0, r.memo)(ae);
        var ce = t(887),
          de = t.n(ce);
        const Ee = ["xl", "lg", "md", "sm", "xs"],
          me = (e) => e.includes("_") && ((e) => Ee.includes(e))(e.split("_").at(-1)),
          _e = [p.ExtraLarge, p.Large, p.Medium, p.Small, p.ExtraSmall],
          Ae = (e, u) =>
            Object.keys(e).reduce((t, r) => {
              if (r in t) return t;
              if (me(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const o = _e.indexOf(u),
                  i = (-1 !== o ? Ee.slice(o) : [])
                    .map((e) => n + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  l = i ? e[i] : void 0;
                return ((t[n] = void 0 !== l ? l : e[n]), t);
              }
              const n = e[r];
              return (
                void 0 === n ||
                  ((e, u) => Ee.some((t) => void 0 !== u[`${e}_${t}`]))(r, e) ||
                  (t[r] = n),
                t
              );
            }, {}),
          Fe = (e, u = Ae) => {
            const t = (
              (e, u = Ae) =>
              (t) => {
                const o = w().mediaSize,
                  i = (0, r.useMemo)(() => u(t, o), [t, o]);
                return n().createElement(e, i);
              }
            )(e, u);
            return n().memo((u) =>
              Object.keys(u).some((e) => me(e) && void 0 !== u[e])
                ? n().createElement(t, u)
                : n().createElement(e, u),
            );
          },
          De = {
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
          he = [
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
        function ge() {
          return (
            (ge =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            ge.apply(this, arguments)
          );
        }
        Object.keys(de());
        const Ce = {
            XL: { mt: De.mt__XL, mr: De.mr__XL, mb: De.mb__XL, ml: De.ml__XL },
            LG: { mt: De.mt__LG, mr: De.mr__LG, mb: De.mb__LG, ml: De.ml__LG },
            MDp: { mt: De.mt__MDp, mr: De.mr__MDp, mb: De.mb__MDp, ml: De.ml__MDp },
            MD: { mt: De.mt__MD, mr: De.mr__MD, mb: De.mb__MD, ml: De.ml__MD },
            SMp: { mt: De.mt__SMp, mr: De.mr__SMp, mb: De.mb__SMp, ml: De.ml__SMp },
            SM: { mt: De.mt__SM, mr: De.mr__SM, mb: De.mb__SM, ml: De.ml__SM },
            XS: { mt: De.mt__XS, mr: De.mr__XS, mb: De.mb__XS, ml: De.ml__XS },
          },
          fe = (Object.keys(Ce), ["mt", "mr", "mb", "ml"]),
          be = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          pe = Fe((e) => {
            let u = e.className,
              t = e.width,
              o = e.height,
              i = e.m,
              l = e.mt,
              a = void 0 === l ? i : l,
              s = e.mr,
              c = void 0 === s ? i : s,
              d = e.mb,
              E = void 0 === d ? i : d,
              m = e.ml,
              _ = void 0 === m ? i : m,
              A = e.column,
              F = e.row,
              D = e.flexDirection,
              h = void 0 === D ? (A ? "column" : F && "row") || void 0 : D,
              g = e.flexStart,
              f = e.center,
              b = e.flexEnd,
              p = e.spaceBetween,
              B = e.spaceAround,
              v = e.justifyContent,
              w =
                void 0 === v
                  ? (g ? "flex-start" : f && "center") ||
                    (b && "flex-end") ||
                    (p && "space-between") ||
                    (B && "space-around") ||
                    void 0
                  : v,
              S = e.alignItems,
              T =
                void 0 === S
                  ? (g ? "flex-start" : f && "center") || (b && "flex-end") || void 0
                  : S,
              y = e.alignSelf,
              L = e.wrap,
              R = e.flexWrap,
              O = void 0 === R ? (L ? "wrap" : void 0) : R,
              x = e.grow,
              M = e.shrink,
              P = e.flex,
              I = void 0 === P ? (x || M ? `${x ? 1 : 0} ${M ? 1 : 0} auto` : void 0) : P,
              H = e.style,
              k = e.children,
              N = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, he);
            const W = (0, r.useMemo)(() => {
                const e = { mt: a, mr: c, mb: E, ml: _ },
                  u = ((e) =>
                    fe.reduce((u, t) => {
                      const r = e[t];
                      return r && "number" != typeof r ? u.concat(Ce[!0 === r ? "MD" : r][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    fe.reduce((u, t) => {
                      const r = e[t];
                      return ("number" == typeof r && (u[be[t]] = r + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, H, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== o && "number" == typeof o ? o + "rem" : o,
                    flex: I,
                    alignSelf: y,
                    display: h || T ? "flex" : void 0,
                    flexDirection: h,
                    flexWrap: O,
                    justifyContent: w,
                    alignItems: T,
                  }),
                  computedClassNames: u,
                };
              }, [t, o, a, c, E, _, H, I, y, h, O, w, T]),
              Y = W.computedStyle,
              X = W.computedClassNames;
            return n().createElement(
              "div",
              ge({ className: C()(De.base, ...X, u), style: Y }, N),
              k,
            );
          });
        let Be;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(Be || (Be = {}));
        const ve = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          we = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          Se = (e, u, t = Be.left) => e.split(u).reduce(t === Be.left ? ve : we, []),
          Te = (() => {
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
          ye = ["zh_cn", "zh_sg", "zh_tw"],
          Le = (e, u = Be.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return ye.includes(t)
              ? Te(e)
              : ((e, u = Be.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (Se(n, /( )/, u).forEach((e) => (t = t.concat(Se(e, r, Be.left)))), t);
                })(e, u);
          },
          Re = "FormatText_base_d0",
          Oe = ({ binding: e, text: u = "", classMix: t, alignment: o = Be.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : n().createElement(
                  r.Fragment,
                  null,
                  u.split("\n").map((u, i) =>
                    n().createElement(
                      "div",
                      { className: C()(Re, t), key: `${u}-${i}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : Le(e, u))))(u, o, e).map((e, u) =>
                        n().createElement(r.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var xe = t(532),
          Me = t.n(xe);
        const Pe = {
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
          Ie = [
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
        function He() {
          return (
            (He =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            He.apply(this, arguments)
          );
        }
        Object.keys(de());
        const ke = Object.keys(Me()),
          Ne = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          We = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Ye = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Xe = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Ge =
            (Object.keys(Xe),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ne,
              "heading-H36": Ne,
              "heading-H28": We,
              "heading-H24": We,
              "heading-H24R": We,
              "heading-H22": We,
              "heading-H20R": We,
              "heading-H18": We,
              "heading-H15": Ye,
              "heading-H14": Ye,
              "paragraph-P24": We,
              "paragraph-P18": We,
              "paragraph-P16": We,
              "paragraph-P14": Ye,
              "paragraph-P12": Ye,
              "paragraph-P10": Ye,
            }),
          je =
            (Object.keys(Ge),
            (e) =>
              e
                ? ((e) => ke.includes(e))(e)
                  ? { colorClassName: Pe[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Ue = Fe((e) => {
            let u = e.text,
              t = e.variant,
              o = e.className,
              i = e.color,
              l = e.m,
              a = e.mt,
              s = void 0 === a ? l : a,
              c = e.mr,
              d = void 0 === c ? l : c,
              E = e.mb,
              m = void 0 === E ? l : E,
              _ = e.ml,
              A = void 0 === _ ? l : _,
              F = e.style,
              D = e.format,
              h = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Ie);
            const g = (0, r.useMemo)(() => {
                const e = je(i),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, r), colorClassName: u };
              }, [F, i]),
              f = g.computedStyle,
              b = g.colorClassName;
            return n().createElement(
              pe,
              He(
                {
                  className: C()(Pe.base, t && Pe[t], b, o),
                  style: f,
                  mt: !0 === s ? Ge[t || "paragraph-P16"].mt : s,
                  mr: !0 === d ? Ge[t || "paragraph-P16"].mr : d,
                  mb: !0 === m ? Ge[t || "paragraph-P16"].mb : m,
                  ml: !0 === A ? Ge[t || "paragraph-P16"].ml : A,
                },
                h,
              ),
              void 0 !== D ? n().createElement(Oe, He({}, D, { text: u })) : u,
            );
          });
        let ze, Ke;
        (!(function (e) {
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
        })(ze || (ze = {})),
          (function (e) {
            ((e.Groups = "groups"),
              (e.Availability = "availability"),
              (e.OnAnotherVeh = "onAnotherVeh"),
              (e.Special = "special"),
              (e.Historic = "historic"),
              (e.Editable = "editable"),
              (e.Formfactor = "formfactor"),
              (e.Sorting = "sorting"),
              (e.ProgressionDecals = "progressionDecals"));
          })(Ke || (Ke = {})));
        const Ve = (e, u) => {
            const t = Array.isArray(e) ? e : [e];
            return !u && t.length > 1 ? t.slice(0, 1) : t;
          },
          $e = ["children"];
        function qe() {
          return (
            (qe =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            qe.apply(this, arguments)
          );
        }
        const Qe = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, $e);
          return n().createElement(
            X,
            qe(
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
        function Ze() {
          return (
            (Ze =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Ze.apply(this, arguments)
          );
        }
        const Je = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const r = n().createElement("div", { className: t }, e);
          if (u.header || u.body) return n().createElement(z, u, r);
          const o = u.contentId,
            i = u.args,
            l = null == i ? void 0 : i.contentId;
          return o || l
            ? n().createElement(X, Ze({}, u, { contentId: o || l }), r)
            : n().createElement(Qe, u, r);
        };
        let eu, uu;
        (!(function (e) {
          ((e.Basic = "basic"),
            (e.Disabled = "disabled"),
            (e.Focused = "focused"),
            (e.Alert = "alert"),
            (e.Selected = "selected"));
        })(eu || (eu = {})),
          (function (e) {
            ((e.Small = "small"), (e.Medium = "medium"));
          })(uu || (uu = {})));
        const tu = "TextOverflow_base_3b",
          ru = ({ content: e, classMix: u }) => {
            const t = (0, r.useRef)(null),
              o = (0, r.useState)(!0),
              i = o[0],
              l = o[1];
            return (
              (0, r.useEffect)(() =>
                K(() => {
                  const e = t.current;
                  e && e.offsetWidth >= e.scrollWidth && l(!1);
                }),
              ),
              n().createElement(
                z,
                { isEnabled: i, body: e },
                n().createElement("div", { ref: t, className: C()(tu, u) }, e),
              )
            );
          },
          nu = {
            base: "DropDownControl_base_c3",
            base__small: "DropDownControl_base__small_28",
            base__medium: "DropDownControl_base__medium_d0",
            base__over: "DropDownControl_base__over_cc",
            base__down: "DropDownControl_base__down_b3",
            base__open: "DropDownControl_base__open_ed",
            base__focused: "DropDownControl_base__focused_d1",
            base__selected: "DropDownControl_base__selected_0f",
            base__disabled: "DropDownControl_base__disabled_80",
            label: "DropDownControl_label_3a",
            label__small: "DropDownControl_label__small_08",
            label__medium: "DropDownControl_label__medium_61",
            label__placeholder: "DropDownControl_label__placeholder_c0",
            button: "DropDownControl_button_12",
            button__small: "DropDownControl_button__small_13",
            button__medium: "DropDownControl_button__medium_ba",
            gradient: "DropDownControl_gradient_ea",
            disabled: "DropDownControl_disabled_a5",
            arrow: "DropDownControl_arrow_a2",
            arrow__small: "DropDownControl_arrow__small_ed",
            arrow__medium: "DropDownControl_arrow__medium_9e",
            alert: "DropDownControl_alert_d7",
            blink: "DropDownControl_blink_1e",
          };
        let ou;
        !(function (e) {
          ((e.Out = "out"), (e.Over = "over"), (e.Down = "down"));
        })(ou || (ou = {}));
        const iu = (0, r.memo)(
            ({
              parentId: e,
              variant: u = eu.Basic,
              size: t = uu.Medium,
              isOpen: o,
              placeholder: i = R.strings.common.dropdown.placeholder.select(),
              label: l = "",
              classMix: a,
              onClick: s,
              soundHover: c,
              soundClick: d,
              customControl: E,
            }) => {
              const m = (0, r.useState)(ou.Out),
                _ = m[0],
                A = m[1],
                F = (0, r.useState)(!1),
                D = F[0],
                h = F[1],
                g = u === eu.Disabled,
                f = g || u === eu.Basic,
                b = (0, r.useCallback)(() => {
                  g || (A(ou.Over), c && $(c));
                }, [g, c]),
                p = (0, r.useCallback)(() => {
                  g || (A(ou.Down), d && $(d));
                }, [g, d]),
                B = (0, r.useCallback)(() => {
                  (!g && A(ou.Over), !f && h(!0));
                }, [g, f]),
                v = (0, r.useCallback)((e) => s && s(e), [s]),
                w = (0, r.useCallback)(() => A(ou.Out), []);
              ((0, r.useEffect)(() => {
                f || h(!1);
              }, [u, f]),
                (0, r.useEffect)(() => {
                  g && w();
                }, [g, w]));
              const S = C()(
                nu.base,
                o && nu.base__open,
                nu[`base__${_}`],
                (f || !D) && nu[`base__${u}`],
                a,
              );
              return n().createElement(
                "div",
                {
                  id: e ? `${e}_control` : void 0,
                  className: S,
                  onMouseEnter: b,
                  onMouseUp: B,
                  onMouseDown: p,
                  onMouseLeave: w,
                  onClick: v,
                },
                !D && u === eu.Alert && n().createElement("div", { className: nu.alert }),
                n().createElement(
                  "div",
                  { className: C()(nu.label, nu[`label__${t}`], !l && nu.label__placeholder) },
                  E || n().createElement(ru, { content: l || i }),
                ),
                n().createElement(
                  "div",
                  { className: C()(nu.button, nu[`button__${t}`]) },
                  n().createElement("div", { className: C()(nu.arrow, nu[`arrow__${t}`]) }),
                  _ === ou.Over && n().createElement("div", { className: nu.gradient }),
                  g && n().createElement("div", { className: nu.disabled }),
                ),
              );
            },
          ),
          lu = (e) => {
            const u = (0, r.useRef)();
            return (
              (0, r.useEffect)(() => {
                u.current = e;
              }, [e]),
              u.current
            );
          };
        let au;
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
        })(au || (au = {}));
        Date.now();
        k.Sw.instance;
        let su;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(su || (su = {}));
        k.Sw.instance;
        const cu = lu,
          du = (e) => {
            if (!e) return !1;
            const u = e.getBoundingClientRect(),
              t = u.width,
              r = u.height;
            return 0 !== t && 0 !== r;
          },
          Eu = (e) => {
            const u = (0, r.useState)(du(e ? e.current : null)),
              t = u[0],
              n = u[1];
            return (
              (0, r.useEffect)(() => {
                let u = 0;
                const t = () => {
                  u = requestAnimationFrame(() => {
                    du(e ? e.current : null) ? n(!0) : t();
                  });
                };
                return (
                  t(),
                  () => {
                    cancelAnimationFrame(u);
                  }
                );
              }, [e]),
              (0, r.useEffect)(() => () => n(!1), [e]),
              t
            );
          };
        var mu = t(380),
          _u = t.n(mu);
        const Au = "ScrollArea_base_47",
          Fu = "ScrollArea_base__scrollIndent_1d",
          Du = "ScrollArea_base__verticalScrollbarMargin_50",
          hu = "ScrollArea_base__multiple_44",
          gu = "ScrollArea_base__hidden_ec",
          Cu = n().forwardRef((e, u) => {
            const t = e.offsetLeft,
              o = void 0 === t ? 0 : t,
              i = e.offsetTop,
              l = void 0 === i ? 0 : i,
              a = e.scrollSettings,
              s = e.onUpdateActiveAxis,
              c = e.onHorizontalScroll,
              d = e.onVerticalScroll,
              E = e.onOverScrollAtBeginning,
              m = e.onOverScrollAtEnd,
              _ = e.wrapperIndent,
              A = e.verticalScrollbarMargin,
              F = e.isMultipleScroll,
              D = e.scrollAreaContainer,
              h = e.children,
              g = e.classMix,
              f = e.onScrollLeftHandled,
              b = (0, r.useState)(!1),
              p = b[0],
              B = b[1],
              v = (0, r.useState)(),
              w = v[0],
              S = v[1],
              T = (0, r.useState)(),
              y = T[0],
              L = T[1],
              R = (0, r.useRef)(null),
              O = (0, r.useCallback)(() => {
                w &&
                  s &&
                  s(
                    { x: w.scrollbarXActive, y: w.scrollbarYActive },
                    { x: w.reach.x, y: w.reach.y },
                  );
              }, [s, w]),
              x = (0, r.useCallback)(() => w, [w]),
              M = (0, r.useCallback)(() => {
                w && w.update();
              }, [w]),
              P = (0, r.useCallback)(
                (e, u, t) => {
                  w && (w.setScrollLeft(e, u, t), f && f(e, w.contentWidth - w.containerWidth));
                },
                [w, f],
              ),
              I = (0, r.useCallback)(
                (e) => {
                  w &&
                    (w.setScrollLeftImmediately(e), f && f(e, w.contentWidth - w.containerWidth));
                },
                [w, f],
              ),
              H = (0, r.useCallback)(
                (e, u, t) => {
                  w && w.setScrollTop(e, u, t);
                },
                [w],
              ),
              k = (0, r.useCallback)(
                (e) => {
                  w && w.setScrollTopImmediately(e);
                },
                [w],
              ),
              N = (0, r.useCallback)(() => {
                if (y && c && w) {
                  const e = {
                    scrollPosition: y.scrollLeft < 0 ? 0 : y.scrollLeft,
                    reach: w.reach.x,
                  };
                  c(e);
                }
              }, [c, y, w]),
              W = (0, r.useCallback)(() => {
                if (y && d && w) {
                  const e = { scrollPosition: y.scrollTop, reach: w.reach.y };
                  d(e);
                }
              }, [d, y, w]),
              Y = (0, r.useCallback)(() => {
                E && E();
              }, [E]),
              X = (0, r.useCallback)(() => {
                m && m();
              }, [m]),
              G = (0, r.useCallback)(
                (e) => {
                  ("function" == typeof u ? u(e) : null !== u && (u.current = e), L(e));
                },
                [u],
              ),
              j = (0, r.useCallback)(() => {
                w &&
                  (w.update(),
                  (R.current = K(() => {
                    O();
                  })));
              }, [w, O]),
              U = (0, r.useCallback)((e) => {
                0 === e.screenX &&
                  0 === e.screenY &&
                  (e.stopImmediatePropagation(), e.preventDefault());
              }, []);
            (0, r.useEffect)(() => {
              if (w && y)
                return (
                  document.addEventListener("mousemove", U),
                  window.addEventListener("resize", j),
                  y.addEventListener("ps-scroll-x", N),
                  y.addEventListener("ps-scroll-y", W),
                  y.addEventListener("over-scroll-beginning", Y),
                  y.addEventListener("over-scroll-ending", X),
                  B(!0),
                  () => {
                    (window.removeEventListener("resize", j),
                      document.removeEventListener("mousemove", U),
                      y &&
                        (y.removeEventListener("ps-scroll-x", N),
                        y.removeEventListener("ps-scroll-y", W),
                        y.removeEventListener("over-scroll-beginning", Y),
                        y.removeEventListener("over-scroll-ending", X)));
                  }
                );
            }, [U, N, Y, X, j, y, w, W]);
            const z = (0, r.useRef)(y || null);
            z.current = y || null;
            const V = Eu(z);
            ((0, r.useEffect)(
              () => (
                !w && y && V && S(new (_u())(y, Object.assign({}, a))),
                () => {
                  w && (w.destroy(), S(void 0));
                }
              ),
              [y, V, a, w],
            ),
              (0, r.useEffect)(
                () => () => {
                  null == R.current || R.current();
                },
                [],
              ),
              (0, r.useEffect)(
                () =>
                  K(() => {
                    w && O();
                  }),
                [O, w],
              ),
              (0, r.useEffect)(() => {
                o > 0 && I(o);
              }, [o, I]),
              (0, r.useEffect)(() => {
                l > 0 && k(l);
              }, [l, k]),
              (0, r.useEffect)(() => {
                D &&
                  ((D.setScrollLeft = P),
                  (D.setScrollTop = H),
                  (D.setScrollLeftImmediately = I),
                  (D.setScrollTopImmediately = k),
                  (D.updateScrollArea = M),
                  (D.getScrollbar = x));
              }, [D, P, I, H, k, M, x]));
            const $ = C()(Au, { [Fu]: _, [gu]: !p, [Du]: A, [hu]: F }, g);
            return n().createElement("div", { className: $, ref: G }, h);
          }),
          fu = [
            "children",
            "isEnabled",
            "selectedItemId",
            "scrollAreaKey",
            "withCompleteTrigger",
            "containerClasses",
          ];
        function bu() {
          return (
            (bu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            bu.apply(this, arguments)
          );
        }
        const pu = (e) => {
            let u = e.children,
              t = e.isEnabled,
              o = void 0 === t || t,
              i = e.selectedItemId,
              l = e.scrollAreaKey,
              a = void 0 === l ? "scrollArea" : l,
              s = e.withCompleteTrigger,
              c = void 0 !== s && s,
              d = e.containerClasses,
              E = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, fu);
            const m = (0, r.useState)(!1),
              _ = m[0],
              A = m[1],
              F = (0, r.useRef)({}),
              D = (0, r.useRef)(null),
              h = (0, r.useRef)(null),
              g = (0, r.useRef)(null),
              C = (0, r.useCallback)(() => {
                A(!0);
              }, []),
              f = (0, r.useCallback)(() => {
                A(!1);
              }, []),
              b = (0, r.useCallback)(() => {
                const e = g.current,
                  u = D.current,
                  t = F.current;
                if (e && t && u) {
                  const r = e.offsetTop + 0.5 * (e.offsetHeight - u.offsetHeight);
                  t.setScrollTop(r, void 0, c ? C : void 0);
                }
              }, [C, c]);
            (0, r.useEffect)(() => {
              if (o && null !== i) return K(b);
            }, [a, b, i, o]);
            const p = !(!h.current || !h.current.scrollbar) && h.current.scrollbar.scrollbarYActive,
              B = {
                scrollContainerRef: D,
                selectedItemRef: g,
                selectedItemId: i,
                isScrollComplete: _,
                scrollbarActive: p,
                onScrollAnimationComplete: f,
              },
              v = (0, r.cloneElement)(u, B);
            return n().createElement(
              "div",
              { className: d, ref: D },
              n().createElement(Cu, bu({ ref: h, key: a, scrollAreaContainer: F.current }, E), v),
            );
          },
          Bu = {
            base: "DropDownItem_base_aa",
            base__small: "DropDownItem_base__small_4c",
            base__medium: "DropDownItem_base__medium_1f",
            base__selected: "DropDownItem_base__selected_80",
            base__disabled: "DropDownItem_base__disabled_75",
          },
          vu = ["size", "classMix", "onClick", "itemRenderer"];
        const wu = (0, r.memo)((e) => {
            let u = e.size,
              t = e.classMix,
              o = e.onClick,
              i = e.itemRenderer,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, vu);
            const a = l.id,
              s = l.isSelected,
              c = l.isDisabled,
              d = l.label,
              E = l.soundHover,
              m = l.soundClick,
              _ = (0, r.useCallback)(
                (e) => {
                  c || (o && o(e, a));
                },
                [a, c, o],
              ),
              A = (0, r.useCallback)(() => {
                c || (E && $(E));
              }, [c, E]),
              F = (0, r.useCallback)(() => {
                c || (m && $(m));
              }, [c, m]),
              D = C()(
                Bu.base,
                u && Bu[`base__${u}`],
                s && Bu.base__selected,
                c && Bu.base__disabled,
                t,
              );
            return n().createElement(
              "div",
              { className: D, onMouseEnter: A, onMouseDown: F, onClick: _ },
              i ? i(l) : d,
            );
          }),
          Su = { base__withScroll: "DropDownItems_base__withScroll_63" };
        function Tu() {
          return (
            (Tu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Tu.apply(this, arguments)
          );
        }
        const yu = ({
            size: e,
            items: u,
            selectedIds: t,
            selectedItemId: r,
            selectedItemRef: o,
            onClick: i,
            parentId: l,
            soundHover: a,
            soundClick: s,
            itemClassMix: c,
            itemRenderer: d,
            scrollbarActive: E,
          }) =>
            n().createElement(
              "div",
              { className: C()(Su.base, E && Su.base__withScroll) },
              u.map((u) => {
                const E = `${l}_${u.id}`;
                return n().createElement(
                  "div",
                  { id: l ? E : void 0, key: E, ref: u.id === r ? o : null },
                  n().createElement(
                    wu,
                    Tu({ size: e, soundHover: a, soundClick: s, classMix: c, itemRenderer: d }, u, {
                      onClick: i,
                      isSelected: t.includes(u.id),
                    }),
                  ),
                );
              }),
            ),
          Lu = {
            base: "DropDownList_base_fd",
            base__small: "DropDownList_base__small_3b",
            base__medium: "DropDownList_base__medium_3b",
            scrollMix: "DropDownList_scrollMix_67",
          },
          Ru = {
            handlers: ["click-rail", "keyboard", "wheel", "drag-thumb"],
            wheelSpeed: 6,
            suppressScrollX: !0,
            animationDuration: 300,
            minScrollbarLength: 20,
          },
          Ou = ({
            parentId: e,
            size: u = uu.Medium,
            items: t,
            selectedIds: o,
            isOpen: i,
            autoScroll: l,
            classMix: a,
            itemClassMix: s,
            itemRenderer: c,
            onClick: d,
            soundHover: E,
            soundClick: m,
          }) => {
            const _ = (0, r.useState)(null),
              A = _[0],
              F = _[1],
              D = cu(i);
            (0, r.useEffect)(() => {
              if (i && !D) {
                const e = ((e, u) => {
                  if (!u.length) return null;
                  const t = e.find((e) => u.includes(e.id));
                  return t ? t.id : null;
                })(t, o);
                null !== e && F(e);
              }
              i || F(null);
            }, [i, t, o, D]);
            const h = e ? `${e}_list` : void 0;
            return n().createElement(
              "div",
              { id: h, className: C()(Lu.base, Lu[`base__${u}`], a) },
              n().createElement(
                pu,
                { selectedItemId: A, isEnabled: l, scrollSettings: Ru, classMix: Lu.scrollMix },
                n().createElement(yu, {
                  parentId: e,
                  items: t,
                  size: u,
                  selectedIds: o,
                  onClick: d,
                  soundHover: E,
                  soundClick: m,
                  itemClassMix: s,
                  itemRenderer: c,
                }),
              ),
            );
          },
          xu = {
            base: "PureDropDown_base_d0",
            base__small: "PureDropDown_base__small_72",
            base__medium: "PureDropDown_base__medium_e8",
            control__down: "PureDropDown_control__down_d5",
            list: "PureDropDown_list_64",
            list__up: "PureDropDown_list__up_54",
            list__down: "PureDropDown_list__down_83",
            list__under: "PureDropDown_list__under_d6",
            list__above: "PureDropDown_list__above_87",
          },
          Mu = (0, r.memo)(
            ({
              componentId: e,
              containerRef: u,
              items: t,
              selected: o = [],
              variant: i = eu.Basic,
              size: l = uu.Medium,
              multiple: a = !1,
              autoScroll: s = !0,
              placeholder: c,
              classMix: d,
              controlRenderer: E,
              itemRenderer: m,
              open: _,
              tooltipArgs: A,
              onChanges: F,
              onOpen: D,
              onClose: h,
              onClick: g,
              onClickOutside: f,
              onMouseEnter: b,
              onMouseDown: p,
              onMouseUp: B,
              onMouseLeave: v,
              soundHover: w = "highlight",
              soundClick: S = "yes1",
              soundItemHover: T,
              soundItemClick: y,
            }) => {
              const L = (0, r.useRef)(null),
                R = (0, r.useRef)(null),
                O = (0, r.useRef)({ open: !1, listAbove: !1 }),
                x = (0, r.useState)(!1),
                M = x[0],
                P = x[1],
                I = (0, r.useState)(!1),
                H = I[0],
                N = I[1],
                W = (0, r.useState)(window.innerHeight),
                Y = W[0],
                X = W[1],
                G = Ve(o, a),
                j = i !== eu.Disabled,
                U = void 0 === _,
                z = Boolean(U ? M : _);
              var V, $;
              ((V = () => {
                X(window.innerHeight);
              }),
                ($ = []),
                (0, r.useEffect)(
                  () => (
                    window.addEventListener("resize", V),
                    () => window.removeEventListener("resize", V)
                  ),
                  $,
                ));
              const q = (0, r.useCallback)(() => {
                O.current.open && ((O.current.open = !1), P(!1), h && h());
              }, [h]);
              re(z ? ue.n.ESCAPE : ue.n.NONE, q, z);
              const Q = (0, r.useCallback)(() => {
                (f && f(), U && (P(!1), (O.current.open = !1), h && h()));
              }, [f, h, U]);
              ((0, r.useEffect)(() => {
                const e = L.current;
                if (e && z)
                  return (
                    k.c1.register(e, Q),
                    () => {
                      k.c1.unregister(e, Q);
                    }
                  );
              }, [z, Q]),
                (0, r.useEffect)(() => {
                  void 0 !== _ && (O.current.open = _);
                }, [_]));
              const Z = (0, r.useCallback)(() => {
                if (!L.current || !R.current) return;
                const e = u && u.current,
                  t = e ? e.getBoundingClientRect().bottom : Y,
                  r =
                    L.current.getBoundingClientRect().bottom +
                      R.current.getBoundingClientRect().height >
                    t;
                r !== O.current.listAbove && ((O.current.listAbove = r), N(r));
              }, [u, Y]);
              (0, r.useEffect)(() => K(Z), [Z, l, t.length]);
              const J = (0, r.useCallback)(
                  (e) => {
                    const u = G.findIndex((u) => u === e) > -1;
                    let t = [];
                    ((t = a ? (u ? G.filter((u) => u !== e) : [e, ...G]) : u ? [] : [e]),
                      F && F(t));
                  },
                  [a, F, G],
                ),
                ee = (0, r.useCallback)(() => {
                  U &&
                    ((O.current.open = !O.current.open),
                    P(O.current.open),
                    O.current.open ? D && D() : h && h());
                }, [U, D, h]),
                te = (0, r.useCallback)(
                  (e) => {
                    (j && ee(), g && g(e));
                  },
                  [j, g, ee],
                ),
                ne = (0, r.useCallback)(
                  (e, u) => {
                    (g && g(e, u), J(u), !a && ee());
                  },
                  [g, a, ee, J],
                ),
                oe = (0, r.useCallback)((e) => b && b(e), [b]),
                ie = (0, r.useCallback)((e) => B && B(e), [B]),
                le = (0, r.useCallback)((e) => p && p(e), [p]),
                ae = (0, r.useCallback)((e) => v && v(e), [v]),
                se = (0, r.useMemo)(
                  () =>
                    t
                      .filter((e) => G.includes(e.id))
                      .map((e) => e.label)
                      .join(", "),
                  [t, G],
                ),
                ce = (0, r.useMemo)(() => t.filter((e) => G.includes(e.id)), [t, G]),
                de = E ? E(ce) : void 0;
              return n().createElement(
                "div",
                {
                  id: e,
                  ref: L,
                  className: C()(xu.base, xu[`base__${l}`], d && d.base),
                  onMouseEnter: oe,
                  onMouseUp: ie,
                  onMouseDown: le,
                  onMouseLeave: ae,
                },
                n().createElement(
                  "div",
                  { className: C()(xu.control, z && xu.control__down) },
                  n().createElement(
                    Je,
                    { tooltipArgs: A },
                    n().createElement(iu, {
                      parentId: e,
                      size: l,
                      variant: i,
                      isOpen: z,
                      placeholder: c,
                      label: se,
                      classMix: d && d.control,
                      onClick: te,
                      soundHover: w,
                      soundClick: S,
                      customControl: de,
                    }),
                  ),
                ),
                n().createElement(
                  "div",
                  {
                    ref: R,
                    className: C()(
                      xu.list,
                      z ? xu.list__down : xu.list__up,
                      H ? xu.list__above : xu.list__under,
                    ),
                  },
                  n().createElement(Ou, {
                    parentId: e,
                    size: l,
                    items: t,
                    selectedIds: G,
                    isOpen: z,
                    autoScroll: s,
                    classMix: d && d.list,
                    itemClassMix: d && d.item,
                    itemRenderer: m,
                    onClick: ne,
                    soundHover: T || w,
                    soundClick: y || S,
                  }),
                ),
              );
            },
          ),
          Pu = ["items", "selected", "multiple", "onChanges"];
        function Iu() {
          return (
            (Iu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Iu.apply(this, arguments)
          );
        }
        const Hu = (e) => {
          let u = e.items,
            t = e.selected,
            o = void 0 === t ? [] : t,
            i = e.multiple,
            l = void 0 !== i && i,
            a = e.onChanges,
            s = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, Pu);
          const c = (0, r.useState)(Ve(o, l)),
            d = c[0],
            E = c[1],
            m = (0, r.useCallback)(
              (e) => {
                (E(Array.isArray(e) && e.length > 0 ? e : d),
                  a &&
                    a(
                      u.filter((u) =>
                        Array.isArray(e) && e.length > 0 ? e.includes(u.id) : d.includes(u.id),
                      ),
                    ));
              },
              [u, a, d],
            );
          return n().createElement(Mu, Iu({ onChanges: m, items: u, selected: d, multiple: l }, s));
        };
        function ku(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, r) => u(null == e ? void 0 : e.value, t, r));
        }
        const Nu = {
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
          Wu = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function Yu() {
          return (
            (Yu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Yu.apply(this, arguments)
          );
        }
        const Xu = (e) => {
          let u = e.size,
            t = e.value,
            r = e.isEmpty,
            o = e.fadeInAnimation,
            i = e.hide,
            l = e.maximumNumber,
            a = e.className,
            s = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                o = Object.keys(e);
              for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, Wu);
          const c = r ? null : t,
            d = "string" == typeof c;
          if ((c && !d && c < 0) || 0 === c) return null;
          const E = c && !d && c > l,
            m = C()(
              Nu.base,
              Nu[`base__${u}`],
              o && Nu.base__animated,
              i && Nu.base__hidden,
              !c && Nu.base__pattern,
              r && Nu.base__empty,
              a,
            );
          return n().createElement(
            "div",
            Yu({ className: m }, s),
            n().createElement("div", { className: Nu.bg }),
            n().createElement("div", { className: Nu.pattern }),
            n().createElement(
              "div",
              { className: C()(Nu.value, d && Nu.value__text) },
              E ? l : c,
              E && n().createElement("span", { className: Nu.plus }, "+"),
            ),
          );
        };
        Xu.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const Gu = "ToggleButton_base_c0",
          ju = "ToggleButton_overlay_5d",
          Uu = "ToggleButton_base__active_49",
          zu = "ToggleButton_button_3c",
          Ku = "ToggleButton_indicator_1b",
          Vu = "ToggleButton_counter_4f",
          $u = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function qu() {
          return (
            (qu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            qu.apply(this, arguments)
          );
        }
        const Qu = n().memo(function (e) {
            let u = e.isActive,
              t = e.counter,
              r = e.className,
              o = e.children,
              i = e.type,
              l = void 0 === i ? ie.secondary : i,
              a = e.size,
              s = void 0 === a ? le.small : a,
              c = e.hasIndicator,
              d = void 0 === c || c,
              E = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, $u);
            return n().createElement(
              "div",
              { className: C()(Gu, r, u && Uu) },
              n().createElement(se, qu({ type: l, size: s, mixClass: zu }, E), o),
              n().createElement("div", { className: ju }),
              d && n().createElement("div", { className: Ku }),
              Boolean(t) &&
                n().createElement(
                  "div",
                  { className: Vu },
                  n().createElement(Xu, { value: t, size: "small" }),
                ),
            );
          }),
          Zu = "FilterTitle_base_58",
          Ju = "FilterTitle_label_85",
          et = "FilterTitle_discount_75",
          ut = "FilterTitle_discountIcon_d9",
          tt = n().memo(({ label: e, hasDiscount: u, className: t }) =>
            n().createElement(
              "div",
              { className: C()(Zu, t) },
              n().createElement("div", { className: Ju }, e),
              u &&
                n().createElement(
                  "div",
                  { className: et },
                  n().createElement("div", { className: ut }),
                ),
            ),
          ),
          rt = "ToggleIcon_base_b6",
          nt = "ToggleIcon_base__small_d0",
          ot = "ToggleIcon_icon_0b",
          it = n().memo(function ({ icon: e, iconParams: u, isSmall: t = !1, classNames: r }) {
            return n().createElement(
              "div",
              { className: C()(rt, null == r ? void 0 : r.base, t && nt) },
              n().createElement("div", {
                className: C()(ot, null == r ? void 0 : r.icon),
                style: {
                  backgroundImage: `url(${e})`,
                  width: (null == u ? void 0 : u.iconWidth) || "inherit",
                  height: (null == u ? void 0 : u.iconHeight) || "inherit",
                },
              }),
            );
          }),
          lt = {
            icon__vehicleType: "ToggleButtonIcon_icon__vehicleType_8b",
            icon__nation: "ToggleButtonIcon_icon__nation_3d",
            icon__vehicleGradePrimary: "ToggleButtonIcon_icon__vehicleGradePrimary_36",
            icon__tankmanRole: "ToggleButtonIcon_icon__tankmanRole_6c",
            icon__selected: "ToggleButtonIcon_icon__selected_d7",
            icon__tankmanKind: "ToggleButtonIcon_icon__tankmanKind_b0",
            icon__vehicleGradeElite: "ToggleButtonIcon_icon__vehicleGradeElite_72",
            icon__locationRecruit: "ToggleButtonIcon_icon__locationRecruit_ae",
            icon__locationTankman: "ToggleButtonIcon_icon__locationTankman_1c",
            icon__locationUnique: "ToggleButtonIcon_icon__locationUnique_66",
            icon__personalDataType: "ToggleButtonIcon_icon__personalDataType_82",
            icon__tankmanKindDismissed: "ToggleButtonIcon_icon__tankmanKindDismissed_59",
            icon__vehicleGradePremium: "ToggleButtonIcon_icon__vehicleGradePremium_00",
          },
          at = n().memo(
            ({
              id: e,
              icon: u,
              iconParams: t,
              type: r,
              isSmall: o = !0,
              isSelected: i = !1,
              baseClassName: l = "",
              iconClassName: a = "",
            }) => {
              return n().createElement(it, {
                icon: u,
                isSmall: o,
                iconParams: t,
                classNames: {
                  icon: C()(
                    lt[`icon__${r}`],
                    lt[`icon__${r}${((s = e), s[0].toUpperCase() + s.slice(1))}`],
                    i && lt.icon__selected,
                    a,
                  ),
                  base: l,
                },
              });
              var s;
            },
          ),
          st = {
            base: "FilterToggleGroup_base_30",
            title: "FilterToggleGroup_title_88",
            content: "FilterToggleGroup_content_71",
            toggle: "FilterToggleGroup_toggle_c0",
            base__inPopup: "FilterToggleGroup_base__inPopup_4f",
          },
          ct = ["id", "isSelected", "tooltip", "icon", "counter"];
        function dt() {
          return (
            (dt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            dt.apply(this, arguments)
          );
        }
        let Et;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(Et || (Et = {}));
        const mt = ({ header: e, body: u, contentId: t, targetId: r }) =>
            t
              ? { contentId: t, targetId: r }
              : u || e
                ? { header: null != e ? e : void 0, body: null != u ? u : void 0 }
                : void 0,
          _t = ({
            id: e,
            type: u,
            label: t,
            hasDiscount: r,
            filters: o,
            onClick: i,
            className: l,
            toggleProps: a,
            theme: s = Et.Default,
          }) => {
            const c = s === Et.InPopup;
            return n().createElement(
              "div",
              { className: C()(st.base, st[`base__${s}`], l) },
              c && n().createElement(tt, { className: st.title, label: t, hasDiscount: r }),
              n().createElement(
                "div",
                { className: st.content },
                ku(o, (t) => {
                  let r = t.id,
                    o = t.isSelected,
                    l = t.tooltip,
                    s = t.icon,
                    d = t.counter;
                  const E = (function (e, u) {
                      if (null == e) return {};
                      var t,
                        r,
                        n = {},
                        o = Object.keys(e);
                      for (r = 0; r < o.length; r++)
                        ((t = o[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                      return n;
                    })(t, ct),
                    m = E.iconWidth,
                    _ = E.iconHeight;
                  return n().createElement(
                    Je,
                    { key: r, tooltipArgs: mt(l), className: st.toggle },
                    n().createElement(
                      Qu,
                      dt({}, a, {
                        className: C()(st.toggle, null == a ? void 0 : a.className),
                        isActive: o,
                        onClick: () => (null == i ? void 0 : i(e, r)),
                        counter: d,
                      }),
                      n().createElement(at, {
                        id: r,
                        icon: s,
                        iconParams: { iconWidth: m, iconHeight: _ },
                        type: u,
                        isSmall: c,
                        isSelected: o,
                        baseClassName: null == a ? void 0 : a.baseClassName,
                        iconClassName: C()(
                          null == a ? void 0 : a.iconClassName,
                          (null == a ? void 0 : a.parentStyles) &&
                            (null == a ? void 0 : a.parentStyles[`icon_${r}`]),
                        ),
                      }),
                    ),
                  );
                }),
              ),
            );
          };
        function At() {
          return !1;
        }
        console.log;
        var Ft = t(174);
        function Dt(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return ht(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return ht(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function ht(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        const gt = (e) => (0 === e ? window : window.subViews.get(e));
        const Ct = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? ku(e, (e) => ("object" == typeof e ? Ct(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? Ct(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? Ct(u) : u]),
                    )
              : e,
          ft = (e) => Ct(e);
        var bt = t(946);
        const pt = ((e, u) => {
            const t = (0, r.createContext)({});
            return [
              function ({ mode: o = "real", options: l, children: a, mocks: s }) {
                const c = (0, r.useRef)([]),
                  d = (t, r, n) => {
                    var o;
                    const l = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = gt,
                        context: r = "model",
                      } = {}) {
                        const n = new Map();
                        function o(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? n.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = n.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const l = (e) => {
                          const n = t(u),
                            o = r.split(".").reduce((e, u) => e[u], n);
                          return "string" != typeof e || 0 === e.length
                            ? o
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, o);
                        };
                        return {
                          subscribe: (t, o) => {
                            const a = "string" == typeof o ? `${r}.${o}` : r,
                              s = i.O.view.addModelObserver(a, u, !0);
                            return (n.set(s, t), e && t(l(o)), s);
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
                            for (var e, t = Dt(n.keys()); !(e = t()).done;) o(e.value, u);
                          },
                          unsubscribe: o,
                        };
                      })(r),
                      a =
                        "real" === t
                          ? l
                          : Object.assign({}, l, {
                              readByPath:
                                null != (o = null == n ? void 0 : n.getter) ? o : () => {},
                            }),
                      s = (e) =>
                        "mocks" === t ? (null == n ? void 0 : n.getter(e)) : a.readByPath(e),
                      d = (e) => c.current.push(e),
                      E = e({
                        mode: t,
                        readByPath: s,
                        externalModel: a,
                        observableModel: {
                          array: (e, u) => {
                            const r = null != u ? u : s(e),
                              n = Ft.LO.box(r, { equals: At });
                            return (
                              "real" === t &&
                                a.subscribe(
                                  (0, Ft.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          object: (e, u) => {
                            const r = null != u ? u : s(e),
                              n = Ft.LO.box(r, { equals: At });
                            return (
                              "real" === t &&
                                a.subscribe(
                                  (0, Ft.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          primitives: (e, u) => {
                            const r = s(u);
                            if (Array.isArray(e)) {
                              const n = e.reduce((e, u) => ((e[u] = Ft.LO.box(r[u], {})), e), {});
                              return (
                                "real" === t &&
                                  a.subscribe(
                                    (0, Ft.aD)((u) => {
                                      e.forEach((e) => {
                                        n[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                n
                              );
                            }
                            {
                              const n = e,
                                o = Object.entries(n),
                                i = o.reduce((e, [u, t]) => ((e[t] = Ft.LO.box(r[u], {})), e), {});
                              return (
                                "real" === t &&
                                  a.subscribe(
                                    (0, Ft.aD)((e) => {
                                      o.forEach(([u, t]) => {
                                        i[t].set(e[u]);
                                      });
                                    }),
                                    u,
                                  ),
                                i
                              );
                            }
                          },
                        },
                        cleanup: d,
                      }),
                      m = { mode: t, model: E, externalModel: a, cleanup: d };
                    return {
                      model: E,
                      controls: "mocks" === t && n ? n.controls(m) : u(m),
                      externalModel: a,
                      mode: t,
                    };
                  },
                  E = (0, r.useRef)(!1),
                  m = (0, r.useState)(o),
                  _ = m[0],
                  A = m[1],
                  F = (0, r.useState)(() => d(o, l, s)),
                  D = F[0],
                  h = F[1];
                return (
                  (0, r.useEffect)(() => {
                    E.current ? h(d(_, l, s)) : (E.current = !0);
                  }, [s, _, l]),
                  (0, r.useEffect)(() => {
                    A(o);
                  }, [o]),
                  (0, r.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [D],
                  ),
                  n().createElement(t.Provider, { value: D }, a)
                );
              },
              () => (0, r.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  filterModel: e.object("filterModel"),
                  filterGroups: e.array("filterModel.groups"),
                  filterStructure: e.array("filterModel.structure"),
                  displayGroups: e.array("displayGroups"),
                },
                t = (0, bt.Om)(() => ft(u.filterGroups.get()), { equals: At }),
                r = (0, bt.Om)(() => ft(u.filterStructure.get()), { equals: At }),
                n = (0, bt.Om)(() => ft(u.displayGroups.get()), { equals: At });
              return Object.assign({}, u, {
                computes: { getFilterGroups: t, getFilterStructure: r, getDisplayGroupsItems: n },
              });
            },
            ({ externalModel: e }) => ({
              changeFilter: e.createCallback((e, u) => ({ key: e, value: u }), "changeFilter"),
              clearFilter: e.createCallbackNoArgs("clearFilter"),
            }),
          ),
          Bt = pt[0],
          vt = pt[1],
          wt = R.strings.customization.tooltips.filters;
        let St;
        !(function (e) {
          ((e.INVENTORY = "inventory"),
            (e.APPLIED = "applied"),
            (e.FAVORITES = "favorite"),
            (e.HISTORIC = "historic"),
            (e.NONHISTORIC = "nonHistoric"),
            (e.FANTASTICAL = "fantastical"),
            (e.GROUP = "group"),
            (e.DISPLAY_GROUP = "displayGroup"),
            (e.ON_ANOTHER_VEHICLE = "onAnotherVeh"),
            (e.ONLY_EDITABLE_STYLES = "onlyEditableStyles"),
            (e.ONLY_NON_EDITABLE_STYLES = "onlyNonEditableStyles"),
            (e.ONLY_PROGRESSION_STYLES = "onlyProgressionStyles"),
            (e.ONLY_PROGRESSION_DECALS = "onlyProgressionDecals"),
            (e.FORMFACTOR_SQUARE = "formfactor_square"),
            (e.FORMFACTOR_RECT1X2 = "formfactor_rect1x2"),
            (e.FORMFACTOR_RECT1X3 = "formfactor_rect1x3"),
            (e.FORMFACTOR_RECT1X4 = "formfactor_rect1x4"),
            (e.FORMFACTOR_RECT1X6 = "formfactor_rect1x6"));
        })(St || (St = {}));
        const Tt = {
            [St.INVENTORY]: !1,
            [St.APPLIED]: !1,
            [St.FAVORITES]: !1,
            [St.HISTORIC]: !1,
            [St.NONHISTORIC]: !1,
            [St.FANTASTICAL]: !1,
            [St.ONLY_EDITABLE_STYLES]: !1,
            [St.ONLY_NON_EDITABLE_STYLES]: !1,
            [St.ONLY_PROGRESSION_STYLES]: !1,
            [St.ONLY_PROGRESSION_DECALS]: !1,
            [St.FORMFACTOR_SQUARE]: !1,
            [St.FORMFACTOR_RECT1X2]: !1,
            [St.FORMFACTOR_RECT1X3]: !1,
            [St.FORMFACTOR_RECT1X4]: !1,
            [St.FORMFACTOR_RECT1X6]: !1,
          },
          yt = "FiltersDropdown_customItem_d0",
          Lt = "FiltersDropdown_customList_89",
          Rt = {
            base: "FiltersPopover_base_8c",
            filtersTitle: "FiltersPopover_filtersTitle_49",
            filtersCounterText: "FiltersPopover_filtersCounterText_8e",
            filtersCounterValue: "FiltersPopover_filtersCounterValue_71",
            allFiltersCounterValue: "FiltersPopover_allFiltersCounterValue_32",
            filtersContent: "FiltersPopover_filtersContent_fd",
            filterItem: "FiltersPopover_filterItem_33",
            filterButton: "FiltersPopover_filterButton_8e",
            filterButtonBase: "FiltersPopover_filterButtonBase_83",
            filterButtonIcon: "FiltersPopover_filterButtonIcon_5a",
            filterFormButtonIcon: "FiltersPopover_filterFormButtonIcon_33",
            filterLabel: "FiltersPopover_filterLabel_77",
            filterBody: "FiltersPopover_filterBody_b1",
            anotherVehCheck: "FiltersPopover_anotherVehCheck_dc",
            filterBodyMarginTop: "FiltersPopover_filterBodyMarginTop_81",
            filterBodyMarginBottom: "FiltersPopover_filterBodyMarginBottom_2b",
            filterColumns: "FiltersPopover_filterColumns_17",
            filtersFooter: "FiltersPopover_filtersFooter_9c",
            resetButtonWrapper: "FiltersPopover_resetButtonWrapper_18",
            filtersResetButton: "FiltersPopover_filtersResetButton_1c",
            hiddenItemCounter: "FiltersPopover_hiddenItemCounter_66",
            buttonAppliedIcon: "FiltersPopover_buttonAppliedIcon_10",
            buttonPremiumIcon: "FiltersPopover_buttonPremiumIcon_dd",
            buttonHistoricIcon: "FiltersPopover_buttonHistoricIcon_8e",
            buttonNonhistoricIcon: "FiltersPopover_buttonNonhistoricIcon_a6",
            buttonFantasticalIcon: "FiltersPopover_buttonFantasticalIcon_ff",
            alertCaption: "FiltersPopover_alertCaption_51",
            alertIcon: "FiltersPopover_alertIcon_f4",
            alertGlow: "FiltersPopover_alertGlow_3a",
          },
          Ot = R.strings.customization,
          xt = (0, ne.Pi)(() => {
            const e = vt(),
              u = e.controls,
              t = e.model,
              o = t.filterModel.get(),
              i = t.filterModel.get(),
              l = i.allItemsCounter,
              a = i.filteredItemsCounter,
              s = i.selectedGroup,
              c = i.isFilteringActive,
              d = t.computes.getFilterStructure(),
              E = t.computes.getFilterGroups(),
              m = (0, r.useCallback)(() => {
                const e = JSON.parse(JSON.stringify(Tt));
                return (
                  (e[St.INVENTORY] = o.inventory),
                  (e[St.APPLIED] = o.applied),
                  (e[St.FAVORITES] = o.favorite),
                  (e[St.HISTORIC] = o.historic),
                  (e[St.NONHISTORIC] = o.nonHistoric),
                  (e[St.FANTASTICAL] = o.fantastical),
                  (e[St.ONLY_EDITABLE_STYLES] = o.onlyEditableStyles),
                  (e[St.ONLY_NON_EDITABLE_STYLES] = o.onlyNonEditableStyles),
                  (e[St.ONLY_PROGRESSION_STYLES] = o.onlyProgressionStyles),
                  (e[St.ONLY_PROGRESSION_DECALS] = o.onlyProgressionDecals),
                  (e[St.FORMFACTOR_SQUARE] = o.formfactor_square),
                  (e[St.FORMFACTOR_RECT1X2] = o.formfactor_rect1x2),
                  (e[St.FORMFACTOR_RECT1X3] = o.formfactor_rect1x3),
                  (e[St.FORMFACTOR_RECT1X4] = o.formfactor_rect1x4),
                  (e[St.FORMFACTOR_RECT1X6] = o.formfactor_rect1x6),
                  e
                );
              }, [o]),
              _ = (0, r.useState)(m()),
              A = _[0],
              F = _[1];
            (0, r.useEffect)(() => {
              F(m());
            }, [m]);
            const D = ((e) => ({
                FILTERS_SPECIAL: [
                  {
                    id: St.INVENTORY,
                    icon: "R.images.gui.maps.icons.event.customizationResource.storage",
                    iconWidth: "30rem",
                    iconHeight: "24rem",
                    isSelected: e[St.INVENTORY],
                    counter: 0,
                    tooltip: {
                      header: R.strings.event.customizationResource.filters.inventoryToggleHeader(),
                      body: R.strings.event.customizationResource.filters.inventoryToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.APPLIED,
                    icon: "R.images.gui.maps.icons.event.customizationResource.tank",
                    iconWidth: "30rem",
                    iconHeight: "24rem",
                    isSelected: e[St.APPLIED],
                    counter: 0,
                    tooltip: {
                      header: R.strings.event.customizationResource.filters.appliedToggleHeader(),
                      body: R.strings.event.customizationResource.filters.appliedToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.FAVORITES,
                    icon: "R.images.gui.maps.icons.customization.favorite_filter",
                    iconWidth: "54rem",
                    iconHeight: "18rem",
                    isSelected: e[St.FAVORITES],
                    counter: 0,
                    tooltip: {
                      header: wt.favoritesToggleHeader(),
                      body: wt.favoritesToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.ONLY_PROGRESSION_DECALS,
                    icon: "R.images.gui.maps.icons.customization.progression_icons.level_0",
                    iconWidth: "24rem",
                    iconHeight: "18rem",
                    isSelected: e[St.ONLY_PROGRESSION_DECALS],
                    counter: 0,
                    tooltip: {
                      header: wt.progressionDecalsToggleHeader(),
                      body: wt.progressionDecalsToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
                FILTERS_HISTORIC: [
                  {
                    id: St.HISTORIC,
                    icon: "R.images.gui.maps.icons.customization.historical_small",
                    iconWidth: "24rem",
                    iconHeight: "24rem",
                    isSelected: e[St.HISTORIC],
                    counter: 0,
                    tooltip: {
                      header: wt.historicToggleHeader(),
                      body: wt.historicToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.NONHISTORIC,
                    icon: "R.images.gui.maps.icons.customization.non_historical_small",
                    iconWidth: "24rem",
                    iconHeight: "24rem",
                    isSelected: e[St.NONHISTORIC],
                    counter: 0,
                    tooltip: {
                      header: wt.nonhistoricToggleHeader(),
                      body: wt.nonhistoricToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.FANTASTICAL,
                    icon: "R.images.gui.maps.icons.customization.fantastical_small",
                    iconWidth: "24rem",
                    iconHeight: "24rem",
                    isSelected: e[St.FANTASTICAL],
                    counter: 0,
                    tooltip: {
                      header: wt.fantasticalToggleHeader(),
                      body: wt.fantasticalToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
                FILTERS_FORMFACTOR: [
                  {
                    id: St.FORMFACTOR_SQUARE,
                    icon: "R.images.gui.maps.icons.customization.icon_form_1",
                    iconWidth: "9rem",
                    iconHeight: "9rem",
                    isSelected: e[St.FORMFACTOR_SQUARE],
                    counter: 0,
                    tooltip: {
                      header: wt.formfactor11ToggleHeader(),
                      body: wt.formfactor11ToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.FORMFACTOR_RECT1X2,
                    icon: "R.images.gui.maps.icons.customization.icon_form_2",
                    iconWidth: "15rem",
                    iconHeight: "9rem",
                    isSelected: e[St.FORMFACTOR_RECT1X2],
                    counter: 0,
                    tooltip: {
                      header: wt.formfactor12ToggleHeader(),
                      body: wt.formfactor12ToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.FORMFACTOR_RECT1X3,
                    icon: "R.images.gui.maps.icons.customization.icon_form_3",
                    iconWidth: "21rem",
                    iconHeight: "9rem",
                    isSelected: e[St.FORMFACTOR_RECT1X3],
                    counter: 0,
                    tooltip: {
                      header: wt.formfactor13ToggleHeader(),
                      body: wt.formfactor13ToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.FORMFACTOR_RECT1X4,
                    icon: "R.images.gui.maps.icons.customization.icon_form_4",
                    iconWidth: "27rem",
                    iconHeight: "9rem",
                    isSelected: e[St.FORMFACTOR_RECT1X4],
                    counter: 0,
                    tooltip: {
                      header: wt.formfactor14ToggleHeader(),
                      body: wt.formfactor14ToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.FORMFACTOR_RECT1X6,
                    icon: "R.images.gui.maps.icons.customization.icon_form_6",
                    iconWidth: "39rem",
                    iconHeight: "9rem",
                    isSelected: e[St.FORMFACTOR_RECT1X6],
                    counter: 0,
                    tooltip: {
                      header: wt.formfactor16ToggleHeader(),
                      body: wt.formfactor16ToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
                FILTERS_EDITABLE: [
                  {
                    id: St.ONLY_EDITABLE_STYLES,
                    icon: "R.images.gui.maps.icons.customization.editable_small",
                    iconWidth: "16rem",
                    iconHeight: "16rem",
                    isSelected: e[St.ONLY_EDITABLE_STYLES],
                    counter: 0,
                    tooltip: {
                      header: R.strings.event.customizationResource.filters.editableToggleHeader(),
                      body: R.strings.event.customizationResource.filters.editableToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.ONLY_NON_EDITABLE_STYLES,
                    icon: "R.images.gui.maps.icons.customization.icon_non_editable",
                    iconWidth: "24rem",
                    iconHeight: "16rem",
                    isSelected: e[St.ONLY_NON_EDITABLE_STYLES],
                    counter: 0,
                    tooltip: {
                      header: wt.noneditableToggleHeader(),
                      body: wt.noneditableToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                  {
                    id: St.ONLY_PROGRESSION_STYLES,
                    icon: "R.images.gui.maps.icons.customization.icon_rarity",
                    iconWidth: "24rem",
                    iconHeight: "22rem",
                    isSelected: e[St.ONLY_PROGRESSION_STYLES],
                    counter: 0,
                    tooltip: {
                      header: wt.progressionstylesToggleHeader(),
                      body: wt.progressionstylesToggleBody(),
                      contentId: 0,
                      targetId: 0,
                    },
                  },
                ],
              }))(A),
              h = D.FILTERS_SPECIAL,
              g = D.FILTERS_HISTORIC,
              f = D.FILTERS_FORMFACTOR,
              b = D.FILTERS_EDITABLE,
              p = (e) => d.filter((u) => u === e).length > 0,
              B =
                ((v = E),
                (w = Ot.filtersPopover.filters.groupsDefaultTitle()),
                v.includes(w) || v.unshift(w),
                v);
            var v, w;
            const S = ({ id: e, labelKey: u, bodyContent: t, addClass: r = "" }) => {
                return p(e)
                  ? n().createElement(
                      "div",
                      { className: C()(Rt.filterItem, r) },
                      u &&
                        n().createElement(
                          "div",
                          { className: Rt.filterLabel },
                          n().createElement(Ue, {
                            text: ((o = u), Ot.filtersPopover.filters[o]()),
                          }),
                        ),
                      n().createElement("div", { className: Rt.filterBody }, t),
                    )
                  : null;
                var o;
              },
              T = (0, r.useCallback)(
                (e, t) => {
                  if ("boolean" == typeof t && "string" == typeof e)
                    (F(Object.assign({}, A, { [e]: t })), u.changeFilter(e, t));
                  else {
                    const e = t.toString(),
                      r = A[e];
                    (F(Object.assign({}, A, { [e]: !r })), u.changeFilter(t, !r));
                  }
                },
                [u, A],
              ),
              y = (0, r.useCallback)(() => {
                (F(Tt), u.clearFilter());
              }, [u]),
              L = (0, r.useCallback)(
                (e, t) => {
                  if (0 === e.length) {
                    const e = A[t];
                    (F(Object.assign({}, A, { [t]: e })), u.changeFilter(t, e));
                  }
                  e.length > 0 &&
                    (F(Object.assign({}, A, { [t]: e[0].id })), u.changeFilter(t, e[0].id));
                },
                [u, A],
              );
            return n().createElement(
              "div",
              { className: Rt.base },
              n().createElement(Ue, {
                text: Ot.filtersPopover.title(),
                className: Rt.filtersTitle,
              }),
              n().createElement(
                "div",
                { className: Rt.filtersCounterText },
                n().createElement(Ue, { text: Ot.filtersPopover.counterText() }),
                n().createElement(
                  "div",
                  { className: Rt.filtersCounterValue },
                  n().createElement(Ue, { text: a.toString() }),
                ),
                n().createElement(Ue, { text: "/" }),
                n().createElement(Ue, { text: l.toString(), className: Rt.allFiltersCounterValue }),
              ),
              n().createElement(
                "div",
                { className: Rt.filtersContent },
                S({
                  id: Ke.Groups,
                  labelKey: "groupsTitle",
                  bodyContent: n().createElement(Hu, {
                    size: uu.Small,
                    variant: eu.Basic,
                    placeholder: Ot.filtersPopover.filters.groupsDefaultTitle(),
                    items: ((e, u = !0) =>
                      e.map((e, t) =>
                        u
                          ? { id: 0 === t ? -1 : t - 1, label: e, value: t }
                          : { id: t, label: e, value: t },
                      ))(B),
                    onChanges: (e) => L(e, St.GROUP),
                    classMix: { item: yt, base: Lt },
                    selected: s,
                  }),
                }),
                S({
                  id: Ke.Special,
                  labelKey: "commonTitle",
                  bodyContent: n().createElement(_t, {
                    id: Ke.Special,
                    label: Ot.filtersPopover.filters.commonTitle(),
                    type: ze.Default,
                    hasDiscount: !1,
                    filters: ((e, u) =>
                      u ? e : e.filter((e) => e.id !== St.ONLY_PROGRESSION_DECALS))(
                      h,
                      p(Ke.ProgressionDecals),
                    ),
                    toggleProps: {
                      type: ie.secondary,
                      size: le.extraSmall,
                      className: Rt.filterButton,
                      baseClassName: Rt.filterButtonBase,
                      iconClassName: Rt.filterButtonIcon,
                    },
                    onClick: T,
                    className: Rt.filtersBlock,
                  }),
                  addClass: Rt.filterBodyMarginTop,
                }),
                S({
                  id: Ke.Historic,
                  labelKey: "historicTitle",
                  bodyContent: n().createElement(_t, {
                    id: Ke.Historic,
                    label: Ot.filtersPopover.filters.historicTitle(),
                    type: ze.Default,
                    hasDiscount: !1,
                    filters: g,
                    toggleProps: {
                      type: ie.secondary,
                      size: le.extraSmall,
                      className: Rt.filterButton,
                      baseClassName: Rt.filterButtonBase,
                      iconClassName: Rt.filterButtonIcon,
                    },
                    onClick: T,
                    className: Rt.filtersBlock,
                  }),
                }),
                S({
                  id: Ke.Formfactor,
                  labelKey: "formfactorTitle",
                  bodyContent: n().createElement(_t, {
                    id: Ke.Formfactor,
                    label: Ot.filtersPopover.filters.formfactorTitle(),
                    type: ze.Default,
                    hasDiscount: !1,
                    filters: f,
                    toggleProps: {
                      type: ie.secondary,
                      size: le.extraSmall,
                      className: Rt.filterButton,
                      baseClassName: Rt.filterButtonBase,
                      iconClassName: Rt.filterFormButtonIcon,
                      parentStyles: Rt,
                    },
                    onClick: T,
                    className: Rt.filtersBlock,
                  }),
                }),
                S({
                  id: Ke.Editable,
                  labelKey: "editableTitle",
                  bodyContent: n().createElement(_t, {
                    id: Ke.Editable,
                    label: Ot.filtersPopover.filters.editableTitle(),
                    type: ze.Default,
                    hasDiscount: !1,
                    filters: b,
                    toggleProps: {
                      type: ie.secondary,
                      size: le.extraSmall,
                      className: Rt.filterButton,
                      baseClassName: Rt.filterButtonBase,
                      iconClassName: Rt.filterButtonIcon,
                    },
                    onClick: T,
                    className: Rt.filtersBlock,
                  }),
                }),
              ),
              n().createElement(
                "div",
                { className: C()(Rt.filtersContent, Rt.filtersFooter) },
                n().createElement(
                  "div",
                  { className: Rt.resetButtonWrapper },
                  n().createElement(
                    se,
                    {
                      type: ie.secondary,
                      size: le.small,
                      mixClass: Rt.filtersResetButton,
                      onClick: y,
                      disabled: !c,
                    },
                    n().createElement(Ue, { text: Ot.customization.resetFiltersBtn.label() }),
                  ),
                ),
              ),
            );
          }),
          Mt = (e, u, t, r) => (100 * (u + t / 2 - (r + 58))) / i.O.view.pxToRem(e),
          Pt = (0, ne.Pi)(() => {
            const e = (0, r.useState)(void 0),
              u = e[0],
              t = e[1],
              o = (0, r.useRef)(null);
            return (
              (function ({
                key: e = ue.n.ESCAPE,
                callback: u = () => i.O.view.sendEvent.close(),
                preventPropagation: t = !0,
              } = {}) {
                re(e, u, t);
              })({ callback: k.SW }),
              (0, r.useEffect)(
                () =>
                  K(() =>
                    K(() => {
                      o.current &&
                        t(
                          ((e) => {
                            const u = window.decorator,
                              t = u.directionType,
                              r = u.boundY,
                              n = u.boundHeight,
                              o = u.boundX,
                              l = u.boundWidth,
                              a = e.getBoundingClientRect(),
                              s = a.width,
                              c = a.height,
                              d = i.O.view.getViewGlobalPosition(),
                              E = d.x,
                              m = d.y;
                            switch (t) {
                              case Z.Left:
                              case Z.Right:
                                return { top: `${Mt(c, r, n, m)}%` };
                              case Z.Bottom:
                              case Z.Top:
                                return { left: `${Mt(s, o, l, E)}%` };
                            }
                          })(o.current),
                        );
                    }),
                  ),
                [],
              ),
              n().createElement(
                ee,
                { customStyles: { arrow: u } },
                n().createElement("div", { ref: o }, n().createElement(xt, null)),
              )
            );
          });
        engine.whenReady.then(() => {
          H().render(
            n().createElement(Bt, null, n().createElement(P, null, n().createElement(Pt, null))),
            document.getElementById("root"),
          );
        });
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
    (__webpack_require__.O = (e, u, t, r) => {
      if (!u) {
        var n = 1 / 0;
        for (a = 0; a < deferred.length; a++) {
          for (var [u, t, r] = deferred[a], o = !0, i = 0; i < u.length; i++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[i]))
              ? u.splice(i--, 1)
              : ((o = !1), r < n && (n = r));
          if (o) {
            deferred.splice(a--, 1);
            var l = t();
            void 0 !== l && (e = l);
          }
        }
        return e;
      }
      r = r || 0;
      for (var a = deferred.length; a > 0 && deferred[a - 1][2] > r; a--)
        deferred[a] = deferred[a - 1];
      deferred[a] = [u, t, r];
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
    (__webpack_require__.j = 18),
    (() => {
      var e = { 18: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var r,
            n,
            [o, i, l] = t,
            a = 0;
          if (o.some((u) => 0 !== e[u])) {
            for (r in i) __webpack_require__.o(i, r) && (__webpack_require__.m[r] = i[r]);
            if (l) var s = l(__webpack_require__);
          }
          for (u && u(t); a < o.length; a++)
            ((n = o[a]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(s);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [841], () => __webpack_require__(85));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
