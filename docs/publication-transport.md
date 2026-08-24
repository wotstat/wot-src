# Транспорт публикации больших Git trees

Статус: реализован симметрично с `wot-gui-assets` 2026-08-24. Этот документ фиксирует причины и
наблюдаемое поведение, которые не видны из одной только формы текущего Python-кода.

## Где проходит seam

Внешний интерфейс publisher — команда `wot-src-publisher publish`: она получает sealed
`GameSnapshot` и ожидаемую identity, строит полный локальный publication tree и атомарно публикует
его в одну data-ветку. Вызывающий workflow не должен знать, понадобился обычный push или large-tree
transport.

Внутренние helper-функции, context manager и dataclass'ы можно свободно менять. Обязательны
наблюдаемые свойства публикации и отказов, перечисленные ниже.

## Почему обычного push недостаточно

Мотивирующий full workload проявился в sibling publisher `wot-gui-assets`: десятки тысяч blobs и
около 5.9 ГБ несжатых изменённых файлов. В
[run 32698945531](https://github.com/wotstat/game-unpack-pipeline/actions/runs/32698945531)
шесть staging pushes прошли, но последующий push version commit снова собрал pack около 3.61 ГиБ и
трижды завершился GitHub HTTP 500/disconnect. Наличие объектов на GitHub само по себе не заставляет
`send-pack` считать временную ветку базой production-ref. `wot-src` использует тот же transport,
чтобы его корректность не зависела от текущего размера конкретной проекции или дельты обновления.

Последовательные некумулятивные commits также недостаточны: последний ref не гарантирует
достижимость полного итогового tree. Если сделать version commit потомком transport commits, Git
переиспользует объекты, но служебная история навсегда попадёт в production-ветку.

Попытка заново собрать большой tree через Git Database API убрала большой Git push, но
[run 32722293486](https://github.com/wotstat/game-unpack-pipeline/actions/runs/32722293486)
получил HTTP 502 на `POST git/trees` для 59 тысяч entries sibling-проекции. Поэтому текущая схема не
пересоздаёт большой tree через API: она сначала материализует и проверяет tree обычными bounded Git
pushes, а API использует только для создания одного commit и обновления ref.

[Run 32731613071](https://github.com/wotstat/game-unpack-pipeline/actions/runs/32731613071)
подтвердил рабочую схему на `wot-gui-assets`: шесть batches, равенство staging/local tree, один API
version commit, non-force update и удаление staging-ref. Large path в этом репозитории реализован и
тестируется теми же инвариантами; его изменение требует отдельного реального workload больше порога.

Это не документация «точного лимита GitHub в 2 ГБ». Зафиксирован наблюдаемый отказ большого pack;
он возможен при любом обновлении с большой передаваемой дельтой, не только при initial commit.
Порог и batch budget по 1 000 000 000 bytes — консервативный эксплуатационный предел, а не
утверждение об официальной границе GitHub.

## Обязательный протокол

Для существующей ветки publisher сначала делает commit/tree-only partial fetch. Старые payload blobs
не должны скачиваться: новый tree полностью строится из локального snapshot.

Если сумма размеров изменённых blobs не больше 1 ГБ, используется один обычный non-force push.

Если сумма больше 1 ГБ:

1. Каждый отдельный blob проверяется против GitHub file limit 100 МиБ, а blobs разбиваются на
   batches не больше 1 ГБ.
2. Создаётся уникальный `publication-staging/<branch>/<run-owner>-<commit>` ref. Параллельные runs не
   должны использовать общий staging-ref.
3. Staging tree начинается с текущего production parent. Для новой orphan-ветки он начинается с
   пустого tree. Удалённые пути применяются до добавления batches.
4. Каждый следующий staging commit кумулятивно добавляет следующую порцию blobs к предыдущему tree.
   Поэтому последний staging ref делает достижимыми все объекты полного publication tree.
5. После последнего push object ID staging tree сравнивается с object ID локального provisional
   version tree. Несовпадение — hard failure до изменения production-ref.
6. Git Database API создаёт один commit на уже существующем verified tree с локально вычисленными
   parent, message, author и committer. Большой tree через API повторно не строится.
7. Существующий production-ref обновляется с `force: false`; новая ветка создаётся на готовом commit.
   Workflow дополнительно сериализует пару publisher/data-branch с `cancel-in-progress: false`.
8. Staging-ref удаляется в `finally` и после успеха, и после ошибки. Staging commits не являются
   предками final commit и не попадают в production log.

Удаление cumulative tree, hash equality, API commit или non-force ref update не является
«упрощением»: оно возвращает один из уже наблюдавшихся режимов отказа либо снимает защиту данных.

## Неопределённые сетевые результаты

Git push и GitHub API могут вернуть transport error после фактического применения операции.
Publisher обязан проверить remote ref перед повтором или объявлением ошибки:

- после неуспешного push успех признаётся, если remote ref уже указывает на ожидаемый commit;
- после ошибки update-ref через API remote ref читается и сравнивается с созданным commit;
- повторы bounded и применяются только к transient transport/HTTP 429/5xx ошибкам.

Конкретное число попыток, задержки и форма helper'ов могут меняться. Семантика ambiguous success и
отсутствие force update должны сохраниться.

## Что защищают тесты

Тесты могут быть переписаны при cleanup, но должны продолжать доказывать через interface публикации:

- batch не превышает budget, а blob больше 100 МиБ отклоняется;
- large path работает для новой и существующей/bootstrap ветки;
- каждый staging push ограничен, прямого большого push в production нет;
- последний staging tree равен локальному publication tree;
- GitHub API получает точные tree и parent, ref обновляется с `force: false`;
- production log содержит один version commit и не содержит transport commits;
- staging-ref удаляется;
- повтор идентичных данных возвращает `unchanged`, а изменённые данные той же версии дают новый
  commit;
- partial fetch не требует payload предыдущих версий.

Локальный bare remote проверяет граф Git и историю, но не моделирует GitHub pack/API limits. Поэтому
изменение large path требует отдельного реального full-run до production pin.

## Inventory обратной совместимости

Проверено по remote heads 2026-08-24:

- `wot-eu`, `mt-ru`, `mt-public-test` уже содержат `.publication.json` и от bootstrap README hash не
  зависят;
- `wot-na`, `wot-asia`, `wot-cn`, `wot-common-test` указывают на один README-only commit
  `3980e29c07a07aa26ef1aaf3d3e5c6d4e582cf4d` с README SHA-256
  `c0b5be60db2a12702d8f8856079d6d4098624dd663253c95c76b4b50a89896b4`;
- legacy hash `fe9c7b92755ce20f3004f4ef66d3c0518b1a89253ebe9ac75c286f309155cdec` не используется текущими
  remote heads и является кандидатом на удаление после повторной проверки.

Когда все README-only ветки будут опубликованы или намеренно заменены, можно удалить весь legacy
hash set и ветку совместимости `_validate_bootstrap_branch`. До этого удаление hash `c0b5...`
сломает первую публикацию в четыре production-ветки.

## Checklist изменения транспорта

1. Повторно проверить remote heads и bootstrap inventory, не полагаясь только на этот датированный
   снимок.
2. Сохранить один CLI interface; не выносить детали staging в workflow caller.
3. Прогнать `uv run pytest -q`, `uv run ruff check .`, `uv run mypy src`.
4. Если тот же transport меняется в `wot-gui-assets`, обновить его симметрично либо явно
   документировать расхождение.
5. После проверки закрепить новый полный publisher SHA в `game-unpack-pipeline` и запустить там
   `./scripts/check.sh`.
6. Для изменения large path выполнить реальный full-run и проверить tree, production log и отсутствие
   оставшихся `publication-staging/*` refs.
