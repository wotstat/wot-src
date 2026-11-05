import {
  Di as t,
  Ei as e,
  Ni as n,
  Oi as s,
  Qt as a,
  Yt as i,
  an as l,
  bi as r,
  dn as o,
  fn as c,
  in as u,
  nn as d,
  on as g,
  pn as h,
  rn as f,
  sn as v,
  tn as p,
  un as y,
  uo as m,
} from "./lib.js";
var b = m.resolve("strings");
function _(t, e, s = "...") {
  return (
    n(
      e - s.length >= 0,
      `Incorrect tranticate config max(${e}) - rest.length(${s.length}) must be greater than 0`,
    ),
    t.length <= e ? [t, !1] : [`${t.slice(0, e - s.length)}${s}`, !0]
  );
}
var I = s(e + t),
  N = () => `${Date.now().toString(16)}_${I(3)}`;
function w(t, e, n = 1) {
  const s = i(e, { count: n });
  return t.has(s) ? w(t, e, n + 1) : s;
}
function A(t = "", e = []) {
  return {
    title: "" !== t ? t : b.readOrEmpty("playlists.defaultName"),
    createdAt: Date.now(),
    modifiedAt: Date.now(),
    list: e,
  };
}
function B(t, e) {
  return t.title === e.title && r.shallow(t.list, e.list);
}
var E = (t) => ({ type: "ok", value: t }),
  $ = (t, e) => ({ type: "error", error: { tag: t, msg: e } });
function O(t) {
  if ("ok" === t.type) return t.value;
}
var k = { delete: "delete", save: "save", import: "import" },
  x = {
    delete: "delete",
    save: "save",
    import: "import",
    cancel: "cancel",
    discard: "discard",
    submit: "submit",
  },
  D = g({
    title: o(),
    createdAt: y(l(), p(), u(0)),
    modifiedAt: y(l(), p(), u(0)),
    list: a(y(l(), p())),
  }),
  T = y(
    o(),
    c((t) => (t.length > 0 ? t : void 0)),
  ),
  R = { New: "new", Existing: "existing" },
  U = g({ id: y(o(), f(1)), playlistState: v(h([d(R.Existing), d(R.New)])) }),
  C = g({ title: o() }),
  L = g({
    titles: y(
      a(o()),
      c((t) => new Set(t)),
    ),
  }),
  P = {
    "mouse-enter": { "vehicle-card": "carousel", "vehicle:playlists:card": "carousel" },
    click: {
      "vehicle:action-cards": "yes1",
      "vehicle-card": "tank_selection",
      "vehicle:playlists:dropdown_trigger": "tabs",
      "vehicle:playlists:copy_button": "tabb",
      "vehicle:playlists:edit_button": "tabb",
      "vehicle:playlists:card": "carouselButton",
      "vehicle:playlists:edit:footer:save_button": "yes1",
      "vehicle:playlists:edit:footer:cancel_button": "cancelcloseno",
      "vehicle:playlists:edit:preview_card:close_button": "cancelcloseno",
      "vehicle:playlists:overlay:submit_button": "yes1",
      "vehicle:playlists:overlay:cancel_button": "cancelcloseno",
    },
    animation: { "vehicle-ttc-section:accordion-summary": "gui_ttc_start" },
    drag: { "vehicle:playlists:edit:draggable_item": "play" },
    drop: { "vehicle:playlists:edit:draggable_item": "tank_selection" },
  },
  S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_";
function V(t) {
  let e = t[0] ?? 0;
  for (let n = 0; n < t.length; n++) e = (e + t[n]) & 65535;
  return e;
}
function Y(t) {
  if (0 === t.length) return $("EMPTY_INPUT");
  const e = V(t),
    n = new Uint8Array(5 + 5 * t.length);
  ((n[0] = e >>> 8), (n[1] = 255 & e), (n[2] = 1));
  let s = 5;
  for (let o = 0; o < t.length; o++) {
    let e = t[o];
    for (;;) {
      const t = 127 & e;
      if (((e >>>= 7), 0 === e)) {
        ((n[s] = t), s++);
        break;
      }
      ((n[s] = 128 | t), s++);
    }
  }
  ((n[3] = (s - 5) >>> 8), (n[4] = (s - 5) & 255));
  let a = "",
    i = 0n,
    l = 0;
  const r = n.slice(0, s);
  for (const o of r)
    for (i = (i << 8n) | BigInt(o), l += 8; l >= 6;) {
      l -= 6;
      const t = Number((i >> BigInt(l)) & 63n);
      ((a += S[t]), (i &= (1n << BigInt(l)) - 1n));
    }
  if (l > 0) {
    const t = 63 & Number(i << BigInt(6 - l));
    a += S[t];
  }
  return E(a);
}
function j(t) {
  if (0 === t.length) return $("INVALID_INPUT");
  let e = 0n,
    n = 0;
  const s = [];
  for (const o of t) {
    const t = S.indexOf(o);
    if (-1 === t) return $("INVALID_CHAR");
    for (e = (e << 6n) | BigInt(t), n += 6; n >= 8;)
      ((n -= 8), s.push(Number((e >> BigInt(n)) & 255n)), (e &= (1n << BigInt(n)) - 1n));
  }
  if (s.length < 6) return $("INCORRECT_LEN");
  const a = (s[0] << 8) | s[1],
    i = s[2] << 8,
    l = 5 + ((s[3] << 8) | s[4]),
    r = [];
  for (let o = 5; o < l;) {
    let t,
      e = 0,
      n = 0;
    do {
      if (((t = s[o++]), void 0 === t))
        return $("OUT_OF_RANGE", `Out of range ${o} in ${s.length}\n\n${s}`);
      ((e |= (127 & t) << n), (n += 7));
    } while (!(128 & ~t));
    r.push(e);
  }
  return E({ numbers: r, hash: a, version: i });
}
export {
  E as _,
  U as a,
  O as b,
  C as c,
  x as d,
  k as f,
  N as g,
  w as h,
  P as i,
  D as l,
  $ as m,
  Y as n,
  R as o,
  A as p,
  V as r,
  L as s,
  j as t,
  T as u,
  B as v,
  _ as y,
};
