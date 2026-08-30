# wot-src • wot-cn • 2.3.1.3 #929

Публичная история читаемых исходников и текстовых данных клиентов World of Tanks и «Мира танков». Служебный publisher-код и reusable workflow находятся в ветке
[`main`](https://github.com/wotstat/wot-src/tree/main), а данные каждого клиента — в отдельной региональной ветке.

Скачать только текущую data-ветку без истории:

```bash
git clone --branch wot-cn --single-branch --depth 1 https://github.com/wotstat/wot-src.git
```

Скачать все data-ветки без истории:

```bash
git clone --depth 1 --no-single-branch https://github.com/wotstat/wot-src.git
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

Версия игры с которой снят снепшот записывается в commit сообщение и `.version_name`.

## Структура data-ветки

```text
README.md
.version_name
.publication.json
sources/             # base + default locale overlay; .py, .xml, .po, .txt
locales/<LANG>/      # все locale overlays WG, включая default locale
sources-as3/         # декомпилированные .as
sources-gameface/    # содержимое base/res/gui/gameface без исходного префикса
stubs/               # полный manifest payload IDE stubs
```

Для клиентов Wargaming default locale накладывается поверх `base` в `sources/`, а все локали, включая default locale, также сохраняются в `locales/`.
У клиентов Lesta отдельного дерева `locales/` нет, их локализованные файлы уже входят в `sources/`.


## Текущая публикация

- Target: `wot-cn`
- Ветка: `wot-cn`
- Версия: `2.3.1.5418`
- Publisher: `qihoo`
- GameSnapshot: `sha256:772a58218f72038545e713075a00122cdf1ee4c1b11ae639b91faf12be48144d`

Машиночитаемые метаданные и контрольные идентификаторы находятся в `.publication.json`.
