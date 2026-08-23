# wot-src

Публичная история читаемых исходников и текстовых данных клиентов World of Tanks и «Мира
танков». Служебный код и GitHub Actions workflows находятся в ветке
[`main`](https://github.com/wotstat/wot-src/tree/main), а данные каждого клиента — в отдельной
региональной ветке.

## Регионы

| Клиент | Data-ветка |
| --- | --- |
| World of Tanks — Europe | [`wot-eu`](https://github.com/wotstat/wot-src/tree/wot-eu) |
| World of Tanks — North America | [`wot-na`](https://github.com/wotstat/wot-src/tree/wot-na) |
| World of Tanks — Asia | [`wot-asia`](https://github.com/wotstat/wot-src/tree/wot-asia) |
| World of Tanks — China | [`wot-cn`](https://github.com/wotstat/wot-src/tree/wot-cn) |
| World of Tanks — Common Test | [`wot-common-test`](https://github.com/wotstat/wot-src/tree/wot-common-test) |
| Мир танков — Россия | [`mt-ru`](https://github.com/wotstat/wot-src/tree/mt-ru) |
| Мир танков — Public Test | [`mt-public-test`](https://github.com/wotstat/wot-src/tree/mt-public-test) |

Каждая production data-ветка начинается с bootstrap commit `init`, содержащего этот README. Каждый
следующий commit соответствует одной версии клиента; точный номер версии записан в сообщении commit
и в `.version_name`.

## Структура data-ветки

```text
README.md
.version_name
.publication.json
sources/             # base + default locale overlay; .py, .xml, .po, Licenses.txt
locales/<LANG>/      # все locale overlays WG, включая default locale
sources-as3/         # декомпилированные .as
sources-gameface/    # содержимое base/res/gui/gameface без исходного префикса
stubs/               # полный manifest payload IDE stubs
```

Для клиентов Wargaming default locale накладывается поверх `base` в `sources/`, а все локали,
включая default locale, также сохраняются в `locales/`. У клиентов Lesta отдельного дерева
`locales/` нет: локализованные файлы уже входят в `sources/`.

## Общая логика pipeline

```text
game-unpack-pipeline workflow_dispatch
  → временная VM в Selectel
  → два изолированных ephemeral JIT runner на одной VM
  → game-snapshot-builder собирает и запечатывает GameSnapshot
  → оркестратор передаёт wot-src workflow локальный путь и identity snapshot
  → wot-src проверяет snapshot, строит data tree и создаёт commit с точной версией
  → data-ветка отправляется в GitHub
  → runner registrations и ресурсы Selectel удаляются
```

Runner для builder и runner для `wot-src` подготавливаются одновременно, но публикация начинается
только после успешной сборки snapshot. Snapshot не передаётся через Actions artifacts: оба runner
читают один локальный путь на VM, работая под разными Unix-пользователями и в разных рабочих
каталогах.

Оркестратор вызывает workflow [`publish-snapshot.yml`](.github/workflows/publish-snapshot.yml)
только из служебной ветки `main`. Publisher независимо проверяет canonical descriptor, маркер
`READY`, snapshot identity, manifest hashes, payload hashes и полное manifest coverage. Затем он
проецирует только публичные данные, создаёт commit с сообщением из `.version_name` и отправляет его
в ветку целевого региона. История data-ветки загружается как commit-only partial fetch; payload
предыдущих версий не скачивается, а новый Git tree строится напрямую из локального GameSnapshot.

Production-ветки принимают только `full` snapshot. Light-прогоны публикуются во временные ветки
`test/light-<target>`, чтобы интеграционные проверки не попадали в постоянную историю. Повторная
публикация того же snapshot идемпотентна, а разные snapshot с одинаковой версией отклоняются.

## Служебная ветка `main`

В `main` находятся workflow, конфигурация targets, publisher и тесты. Эти файлы не копируются в
data-ветки; там остаются только README, метаданные публикации и данные конкретной версии клиента.

Локальные проверки:

```bash
uv sync --frozen
uv run pytest
uv run ruff check .
uv run mypy
```
