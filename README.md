# wot-src

Публичная история читаемых исходников и текстовых данных клиентов World of Tanks и «Мира
танков». Служебный publisher-код находится в ветке
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
следующий commit соответствует одной версии клиента: сообщение строится из `sources/version.xml`
без префикса `v.` в формате `2.3.1.0 #903`, а точный release name записывается в `.version_name`.

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
  → три изолированных ephemeral JIT runner на одной VM
  → game-snapshot-builder собирает и запечатывает GameSnapshot
  → orchestrator-owned publisher job получает локальный путь и identity snapshot
  → wot-src проверяет snapshot, строит data tree и создаёт commit с точной версией
  → data-ветка отправляется в GitHub
  → runner registrations и ресурсы Selectel удаляются
```

Runner для builder и оба publisher runner подготавливаются одновременно, но публикация начинается
только после успешной сборки snapshot. Snapshot не передаётся через Actions artifacts: все runner
читают один локальный путь на VM, работая под разными Unix-пользователями и в разных рабочих
каталогах.

Оркестратор владеет lifecycle publication job и checkout’ит этот репозиторий по закреплённому
commit SHA. Data-ветка, конфигурация и publisher-код остаются здесь, а workflow, Environment и JIT
runner принадлежат `game-unpack-pipeline`. Publisher независимо проверяет canonical descriptor, маркер
`READY`, snapshot identity, manifest hashes, payload hashes и полное manifest coverage. Затем он
проецирует только публичные данные, создаёт commit с версией из `sources/version.xml` и отправляет
его в ветку целевого региона. История data-ветки загружается как commit-only partial fetch; payload
предыдущих версий не скачивается, а новый Git tree строится напрямую из локального GameSnapshot.

Production-ветки принимают только `full` snapshot. Light-прогоны публикуются во временные ветки
`test/light-<target>`, чтобы интеграционные проверки не попадали в постоянную историю. Повторная
публикация той же версии сравнивает только публикуемые данные, не считая служебные метаданные
изменением данных. При неизменных данных publisher возвращает `unchanged` без commit и push; при
изменениях создаёт новый commit с тем же сообщением версии и обновлёнными метаданными.

Если суммарный размер изменённых Git blobs превышает 1 ГБ, publisher заранее загружает их
порциями не более 1 ГБ через уникальную временную ветку `publication-staging/...`. Пока эта ветка
существует, финальный push version commit переиспользует уже известные GitHub объекты и не создаёт
единый pack больше 2 ГБ. Временная ветка удаляется после финального push, включая ошибочный путь;
отдельный файл по-прежнему не может превышать лимит GitHub 100 МиБ.

## Служебная ветка `main`

В `main` находятся конфигурация targets, publisher и тесты. Эти файлы не копируются в
data-ветки; там остаются только README, метаданные публикации и данные конкретной версии клиента.

Локальные проверки:

```bash
uv sync --frozen
uv run pytest
uv run ruff check .
uv run mypy
```
