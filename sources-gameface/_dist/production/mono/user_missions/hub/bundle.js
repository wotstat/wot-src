const __vite__mapDeps = (
  i,
  m = __vite__mapDeps,
  d = m.f ||
    (m.f = [
      "../chunks/lib.css",
      "../chunks/basic_missions.css",
      "../chunks/challenge_missions.css",
    ]),
) => i.map((i) => d[i]);
import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Dn as s,
  Gt as t,
  St as u,
  Tt as a,
  Xt as n,
  _t as _,
  an as r,
  bt as l,
  gt as o,
  ht as i,
  ln as h,
  mt as m,
  qt as b,
  vt as c,
  yt as g,
} from "../chunks/lib.js";
import "../chunks/_wg-global-styles.js";
/* empty css              */ var d = {
    umg_hub_quest_progress: "umg_hub_quest_progress",
    umg_hub_quest_complete: "umg_hub_quest_complete",
    umg_hub_highlight: "umg_hub_highlight",
    umg_hub_unlock_bonus: "umg_hub_unlock_bonus",
    umg_hub_unlock_premium: "umg_hub_unlock_premium",
    umg_hub_quest_reroll: "umg_hub_quest_reroll",
  },
  p = {
    [d.umg_hub_quest_progress]: a(d.umg_hub_quest_progress),
    [d.umg_hub_quest_complete]: a(d.umg_hub_quest_complete),
    [d.umg_hub_highlight]: a(d.umg_hub_highlight),
    [d.umg_hub_unlock_bonus]: a(d.umg_hub_unlock_bonus),
    [d.umg_hub_unlock_premium]: a(d.umg_hub_unlock_premium),
    [d.umg_hub_quest_reroll]: a(d.umg_hub_quest_reroll),
  },
  k = "basic",
  C = "challenges",
  f = e(s(), 1),
  [v, j] = u()(
    ({ observableModel: e }) => ({
      ...e.primitives(["currentTabId"]),
      tabsList: e.arrayClone("tabsList"),
    }),
    ({ externalModel: e }) => ({
      onTabChange: e.createCallback((e) => ({ tabId: e }), "onTabChange"),
      onContentLayoutChanged: e.createCallback(
        (e, s) => ({ y: e, height: s }),
        "onContentLayoutChanged",
      ),
    }),
  ),
  q = "Hub_a7d012e0",
  y = "Hub_tabsContainer_e39aa10a",
  x = "Hub_tab_5c9743bd",
  z = "Hub_content_f95705c3",
  E = e(b(), 1),
  L = {
    [k]: f.lazy(() =>
      m(() => import("../chunks/basic_missions.js"), __vite__mapDeps([0, 1]), import.meta.url),
    ),
    [C]: f.lazy(() =>
      m(() => import("../chunks/challenge_missions.js"), __vite__mapDeps([0, 2]), import.meta.url),
    ),
  },
  w = _(() => {
    const { controls: e, model: s } = j(),
      u = s.currentTabId.get(),
      a = (0, f.useRef)(null),
      _ = (0, f.useCallback)(() => {
        n(() =>
          n(() => {
            if (a.current) {
              const s = a.current.getBoundingClientRect(),
                t = viewEnv.getScale();
              e.onContentLayoutChanged(Math.floor(s.y / t), Math.floor(s.height / t));
            }
          }),
        );
      }, [e]);
    ((0, f.useEffect)(
      () => (
        window.addEventListener("resize", _),
        engine.on("clientResized", _),
        () => {
          (window.removeEventListener("resize", _), engine.off("clientResized", _));
        }
      ),
      [_],
    ),
      (0, f.useEffect)(() => {
        _();
      }, [a, _]));
    const l = t({ tabSize: o.small }, { large: { tabSize: o.medium } });
    return (0, E.jsxs)("div", {
      className: q,
      children: [
        (0, E.jsx)(i, {
          active: u,
          theme: "primary",
          size: l.tabSize,
          onActiveChange: e.onTabChange,
          children: (0, E.jsx)(i.Switcher, {
            classNames: { base: y },
            children: r(s.tabsList.get(), (e) =>
              (0, E.jsx)(i.Tab, { tabId: e.id, className: x, children: e.title }, `tab_${e.id}`),
            ),
          }),
        }),
        (0, E.jsx)("div", {
          className: z,
          ref: a,
          children:
            L[u] &&
            (0, E.jsx)(f.Suspense, {
              fallback: (0, E.jsx)("div", {}),
              children: f.createElement(L[u]),
            }),
        }),
      ],
    });
  });
g(
  new l()
    .addWithProps(c, { soundsOverrides: p })
    .add(v)
    .render((0, E.jsx)(w, {})),
).then(h);
export { d as t };
