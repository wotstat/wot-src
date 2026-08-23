# wot-src

Публичная история читаемых исходников и текстовых данных клиентов World of Tanks и «Мира
танков». Ветка `main` содержит только publisher и GitHub Actions workflow. Данные публикуются в
отдельные orphan-ветки:

- `wot-eu`
- `wot-na`
- `wot-asia`
- `wot-cn`
- `wot-common-test`
- `mt-ru`
- `mt-public-test`

Каждый commit data-ветки соответствует одной версии клиента. Сообщение commit и файл
`.version_name` содержат точный `release_name` из проверенного GameSnapshot.

## Дерево data-ветки

```text
.version_name
.publication.json
sources/             # base + default locale overlay; .py, .xml, .po, Licenses.txt
locales/<LANG>/      # все locale overlays WG, включая default locale
sources-as3/         # декомпилированные .as
sources-gameface/    # всё из base/res/gui/gameface без исходного префикса
stubs/               # полный manifest payload IDE stubs
```

Для Lesta locale overlays намеренно не публикуются: языковые файлы уже находятся в base.
Publisher независимо проверяет canonical descriptor, `READY`, snapshot identity, manifest hashes,
payload hashes и полное manifest coverage до создания commit.

Временные интеграционные прогоны используют ветки вида `test/light-wot-eu`; они не являются
частью постоянной истории и удаляются после завершения тестов.

## Локальная проверка

```bash
uv sync --frozen
uv run pytest
uv run ruff check .
uv run mypy
```
