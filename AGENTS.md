# Контекст проекта для агентов

## Назначение репозитория

`wot-src` хранит publisher-код в `main` и чистые исходники/текстовые данные клиентов в отдельных
региональных ветках. Репозиторий владеет reusable workflow `.github/workflows/publish-snapshot.yml`;
`game-unpack-pipeline` вызывает его по полному commit SHA на выделенном JIT runner.

Перед изменением Git-транспорта полностью прочитать
[`docs/publication-transport.md`](docs/publication-transport.md). В нём отделены обязательные
инварианты от legacy-совместимости и случайной формы текущей реализации.

## Интерфейс publisher

Внешний интерфейс — reusable workflow, CLI `publish`, формат `GameSnapshot`, `config/targets.json`,
результат в stdout/GitHub outputs и наблюдаемый результат в data-ветке. Приватные функции,
dataclass'ы и внутренняя функция проекции интерфейсом не являются: их можно объединять, удалять или
переписывать.

Reusable workflow требует `GH_APP_PRIVATE_KEY` как явный `workflow_call` secret от оркестратора.
Репозиторий не хранит собственную копию ключа и не использует Environment для авторизации.

## Обязательные инварианты

- Snapshot проверяется независимо до проекции: identity, canonical descriptor, `READY`, manifest и
  payload hashes, полное manifest coverage.
- Правила проекции `sources`, locale layers, AS3, Gameface и stubs описаны в README и защищены
  projection tests; не смешивать их с Git transport.
- Ветка выводится только из target config. Отсутствующая ветка создаётся первой публикацией;
  существующая без `.publication.json` не принимается.
- История существующей data-ветки читается partial fetch без загрузки payload прошлых версий.
- Малое изменение публикуется одним обычным push. Изменённые Git blobs суммарно больше 1 ГБ
  проходят bounded cumulative staging и GitHub API finalization, описанные в transport-документе.
- В production-истории остаётся один version commit на публикацию. Staging commits туда не входят.
- Итоговый Git tree обязан быть равен локально проверенному tree по object ID. Production-ref
  обновляется без force; временный ref уникален и удаляется также при ошибке.
- Неопределённый результат сетевой операции разрешается чтением remote state. Нельзя слепо
  повторять потенциально уже применённое обновление.

## Жизненный цикл веток и упрощение

Все старые data-ветки были намеренно удалены перед первым release. Bootstrap commits и проверка
старых README hashes не поддерживаются. Не возвращать ручной выбор branch, light/test-ветки или
совместимость с markerless refs.

Текущая структура helper-функций, context manager и внутренних типов не священна. При cleanup
сохранять поведение через интерфейс, а не старые абстракции. Тесты приватных helper'ов разрешено
заменять тестами внешнего интерфейса, если все transport-инварианты остаются покрыты.

## Проверки

После изменений запускать:

```bash
uv run pytest -q
uv run ruff check .
uv run mypy src
```

Если изменился workflow, CLI или Git transport, обновить pinned полный SHA в
`game-unpack-pipeline`, проверить
оба publisher call path и запустить там `./scripts/check.sh`. Изменение большого transport path до
production pin требует реального full-run на workload больше порога: локальный bare Git remote не
воспроизводит лимиты и поведение GitHub receive-pack/API.
