# wot-src

Публичная история читаемых исходников и текстовых данных клиентов World of Tanks и «Мира
танков». Служебный код и GitHub Actions workflows находятся в ветке
[`main`](https://github.com/wotstat/wot-src/tree/main), а данные каждого клиента — в отдельной региональной ветке.

Скачать только текущую data-ветку без истории:

```bash
git clone --branch wot-eu --single-branch --depth 1 https://github.com/wotstat/wot-src.git
```

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

Первая публикация создаёт data-ветку сразу на version commit. Его сообщение строится из
`sources/version.xml` без префикса `v.` в формате `2.3.1.0 #903`, а точный release name
записывается в `.version_name`.
Транспортные staging commits в историю data-ветки не входят.

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


## Текущая публикация

- Target: `wot-eu`
- Ветка: `wot-eu`
- Версия: `2.3.1.5412`
- Publisher: `wargaming`
- GameSnapshot: `sha256:0737e69564b5943debbdff06ff4683771c915f8a4bb1630cc730cac11ab59cc2`

Машиночитаемые метаданные и контрольные идентификаторы находятся в `.publication.json`.
