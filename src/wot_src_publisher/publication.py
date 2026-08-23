from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
SNAPSHOT_ID_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
LANGUAGE_RE = re.compile(r"^[A-Z]{2}(?:_[A-Z]{2})?$")
SOURCE_SUFFIXES = frozenset({".po", ".py", ".xml"})
GAMEFACE_PREFIX = "res/gui/gameface/"
MANIFEST_NAMES = ("files", "actionscript", "stubs", "packages", "conflicts")
REPOSITORY_URL = "https://github.com/wotstat/wot-src"
REGION_BRANCHES = (
    ("World of Tanks — Europe", "wot-eu"),
    ("World of Tanks — North America", "wot-na"),
    ("World of Tanks — Asia", "wot-asia"),
    ("World of Tanks — China", "wot-cn"),
    ("World of Tanks — Common Test", "wot-common-test"),
    ("Мир танков — Россия", "mt-ru"),
    ("Мир танков — Public Test", "mt-public-test"),
)


class PublicationError(ValueError):
    """A snapshot cannot be safely projected into a data branch."""


@dataclass(frozen=True, slots=True)
class TargetConfig:
    name: str
    data_branch: str
    publisher: str
    default_locale: str | None


@dataclass(frozen=True, slots=True)
class PayloadFile:
    source: Path
    path: str
    sha256: str
    size: int
    language: str | None = None


@dataclass(frozen=True, slots=True)
class VerifiedSnapshot:
    root: Path
    descriptor: dict[str, Any]
    descriptor_sha256: str
    files: tuple[PayloadFile, ...]
    actionscript: tuple[PayloadFile, ...]
    stubs: tuple[PayloadFile, ...]


def _run_git(
    repository: Path,
    *arguments: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip()
        raise PublicationError(
            f"git {arguments[0] if arguments else 'command'} failed: {details}"
        )
    return result


def _canonical_json(value: object) -> bytes:
    try:
        return (
            json.dumps(
                value,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            ).encode("utf-8")
            + b"\n"
        )
    except (TypeError, ValueError) as error:
        raise PublicationError(f"document is not canonical JSON: {error}") from error


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _safe_path(value: object, *, label: str) -> str:
    if not isinstance(value, str):
        raise PublicationError(f"{label} must be a string")
    path = PurePosixPath(value)
    if (
        not value
        or value.startswith("/")
        or "\\" in value
        or "\x00" in value
        or any(part in {"", ".", ".."} for part in value.split("/"))
        or path.as_posix() != value
    ):
        raise PublicationError(f"{label} is unsafe or non-canonical: {value!r}")
    return value


def _object(value: object, *, label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise PublicationError(f"{label} must be a JSON object")
    return value


def _string(value: object, *, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise PublicationError(f"{label} must be a non-empty string")
    return value


def _regular_file(root: Path, relative_path: str, *, label: str) -> Path:
    path = root.joinpath(*PurePosixPath(relative_path).parts)
    try:
        path_stat = path.lstat()
    except OSError as error:
        raise PublicationError(f"{label} is unavailable: {relative_path}: {error}") from error
    if path.is_symlink() or not stat.S_ISREG(path_stat.st_mode):
        raise PublicationError(f"{label} is not a regular file: {relative_path}")
    return path


def _read_json(path: Path, *, label: str) -> tuple[dict[str, Any], bytes]:
    try:
        encoded = path.read_bytes()
        value = json.loads(encoded)
    except (OSError, json.JSONDecodeError) as error:
        raise PublicationError(f"cannot read {label}: {error}") from error
    return _object(value, label=label), encoded


def _load_target(config_path: Path, target: str) -> TargetConfig:
    config, _encoded = _read_json(config_path, label="target configuration")
    if config.get("schema_version") != 1:
        raise PublicationError("target configuration has an unsupported schema_version")
    targets = _object(config.get("targets"), label="target configuration targets")
    raw = _object(targets.get(target), label=f"target configuration for {target}")
    publisher = _string(raw.get("publisher"), label=f"{target}.publisher")
    branch = _string(raw.get("data_branch"), label=f"{target}.data_branch")
    default_locale_value = raw.get("default_locale")
    default_locale: str | None
    if default_locale_value is None:
        default_locale = None
    elif isinstance(default_locale_value, str) and LANGUAGE_RE.fullmatch(default_locale_value):
        default_locale = default_locale_value
    else:
        raise PublicationError(f"{target}.default_locale is invalid")
    return TargetConfig(target, branch, publisher, default_locale)


def _load_manifest(
    root: Path,
    descriptor: dict[str, Any],
    name: str,
) -> tuple[dict[str, Any], ...]:
    manifests = _object(descriptor.get("manifests"), label="snapshot manifests")
    reference = _object(manifests.get(name), label=f"{name} manifest reference")
    relative_path = _safe_path(reference.get("path"), label=f"{name} manifest path")
    expected_sha256 = _string(
        reference.get("sha256"), label=f"{name} manifest sha256"
    )
    if not SHA256_RE.fullmatch(expected_sha256):
        raise PublicationError(f"{name} manifest sha256 is invalid")
    expected_records = reference.get("records")
    if (
        not isinstance(expected_records, int)
        or isinstance(expected_records, bool)
        or expected_records < 0
    ):
        raise PublicationError(f"{name} manifest records is invalid")
    encoded = _regular_file(root, relative_path, label=f"{name} manifest").read_bytes()
    if _sha256_bytes(encoded) != expected_sha256:
        raise PublicationError(f"{name} manifest digest does not match")
    lines = encoded.splitlines()
    if len(lines) != expected_records:
        raise PublicationError(f"{name} manifest record count does not match")
    values: list[dict[str, Any]] = []
    for index, line in enumerate(lines, start=1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise PublicationError(f"{name} manifest line {index} is invalid JSON") from error
        values.append(_object(value, label=f"{name} manifest line {index}"))
    return tuple(values)


def _payload_file(
    root: Path,
    payload_root: str,
    entry: dict[str, Any],
    *,
    label: str,
    language: str | None = None,
) -> PayloadFile:
    relative_path = _safe_path(entry.get("path"), label=f"{label} path")
    digest = _string(entry.get("sha256"), label=f"{label} sha256")
    size = entry.get("size")
    if not SHA256_RE.fullmatch(digest):
        raise PublicationError(f"{label} sha256 is invalid")
    if not isinstance(size, int) or isinstance(size, bool) or size < 0:
        raise PublicationError(f"{label} size is invalid")
    source = _regular_file(root, f"{payload_root}/{relative_path}", label=label)
    encoded = source.read_bytes()
    if len(encoded) != size or _sha256_bytes(encoded) != digest:
        raise PublicationError(f"{label} payload does not match its manifest")
    return PayloadFile(source, relative_path, digest, size, language)


def _verify_payload_coverage(root: Path, payload_root: str, expected: set[str]) -> None:
    directory = root.joinpath(*PurePosixPath(payload_root).parts)
    if directory.is_symlink() or not directory.is_dir():
        raise PublicationError(f"payload root is not a real directory: {payload_root}")
    observed: set[str] = set()
    for current, directories, filenames in os.walk(directory):
        current_path = Path(current)
        for name in (*directories, *filenames):
            candidate = current_path / name
            if candidate.is_symlink():
                raise PublicationError(f"payload contains a symlink: {candidate}")
        for name in filenames:
            candidate = current_path / name
            if not candidate.is_file():
                raise PublicationError(f"payload contains a non-regular file: {candidate}")
            observed.add(candidate.relative_to(directory).as_posix())
    if observed != expected:
        missing = sorted(expected - observed)[:3]
        extra = sorted(observed - expected)[:3]
        raise PublicationError(
            f"payload coverage mismatch for {payload_root}: missing={missing}, extra={extra}"
        )


def _verify_snapshot(
    root: Path,
    *,
    expected_snapshot_id: str,
    expected_descriptor_sha256: str,
    expected_target: str,
    expected_profile: str,
) -> VerifiedSnapshot:
    root = root.absolute()
    if root.is_symlink() or not root.is_dir():
        raise PublicationError(f"snapshot root is not a real directory: {root}")
    descriptor_path = _regular_file(root, "snapshot.json", label="snapshot descriptor")
    descriptor, descriptor_bytes = _read_json(descriptor_path, label="snapshot descriptor")
    if descriptor_bytes != _canonical_json(descriptor):
        raise PublicationError("snapshot descriptor is not canonical JSON")
    descriptor_sha256 = _sha256_bytes(descriptor_bytes)
    if descriptor_sha256 != expected_descriptor_sha256:
        raise PublicationError("snapshot descriptor digest differs from the pipeline output")
    ready = _regular_file(root, "READY", label="snapshot READY marker").read_bytes()
    if ready != f"sha256:{descriptor_sha256}\n".encode():
        raise PublicationError("snapshot READY marker does not match the descriptor")
    if descriptor.get("contract") != "game-snapshot" or descriptor.get(
        "contract_version"
    ) != "1.1.0":
        raise PublicationError("only GameSnapshot v1.1.0 is supported")
    source = _object(descriptor.get("source"), label="snapshot source")
    if source.get("target") != expected_target:
        raise PublicationError("snapshot target differs from the requested target")
    if source.get("build_profile") != expected_profile:
        raise PublicationError("snapshot build profile differs from the requested profile")
    identity = {
        key: descriptor.get(key)
        for key in ("contract", "contract_version", "policies", "source", "tools")
    }
    computed_snapshot_id = f"sha256:{_sha256_bytes(_canonical_json(identity))}"
    if descriptor.get("snapshot_id") != computed_snapshot_id:
        raise PublicationError("snapshot_id does not match the identity document")
    if computed_snapshot_id != expected_snapshot_id:
        raise PublicationError("snapshot_id differs from the pipeline output")
    quality = _object(descriptor.get("quality"), label="snapshot quality")
    if quality != {
        "required_transform_failures": 0,
        "unmanifested_payload_files": 0,
        "unresolved_conflicts": 0,
    }:
        raise PublicationError("snapshot quality gates are not all zero")

    payload = _object(descriptor.get("payload"), label="snapshot payload")
    base_root = _safe_path(payload.get("base_root"), label="base payload root")
    actionscript_root = _safe_path(
        payload.get("actionscript_root"), label="ActionScript payload root"
    )
    stubs_root = _safe_path(payload.get("stubs_root"), label="stubs payload root")
    locale_roots_raw = _object(payload.get("locale_roots"), label="locale payload roots")
    locale_roots = {
        language: _safe_path(path, label=f"{language} locale payload root")
        for language, path in locale_roots_raw.items()
        if LANGUAGE_RE.fullmatch(language)
    }
    if len(locale_roots) != len(locale_roots_raw):
        raise PublicationError("snapshot contains an invalid locale language")

    manifest_values = {name: _load_manifest(root, descriptor, name) for name in MANIFEST_NAMES}
    files: list[PayloadFile] = []
    expected_by_root: dict[str, set[str]] = {base_root: set()}
    expected_by_root.update({path: set() for path in locale_roots.values()})
    seen_files: set[tuple[str | None, str]] = set()
    for index, entry in enumerate(manifest_values["files"], start=1):
        layer = _object(entry.get("layer"), label=f"files manifest layer {index}")
        kind = layer.get("kind")
        if kind == "base":
            language = None
            selected_root = base_root
        elif kind == "locale":
            language = _string(layer.get("language"), label=f"files locale {index}")
            if language not in locale_roots:
                raise PublicationError(f"files manifest references unknown locale {language}")
            selected_root = locale_roots[language]
        else:
            raise PublicationError(f"files manifest layer {index} is invalid")
        item = _payload_file(
            root,
            selected_root,
            entry,
            label=f"files manifest entry {index}",
            language=language,
        )
        key = language, item.path.casefold()
        if key in seen_files:
            raise PublicationError(f"duplicate case-insensitive source path: {item.path}")
        seen_files.add(key)
        expected_by_root[selected_root].add(item.path)
        files.append(item)

    actionscript = tuple(
        _payload_file(
            root,
            actionscript_root,
            entry,
            label=f"ActionScript manifest entry {index}",
        )
        for index, entry in enumerate(manifest_values["actionscript"], start=1)
    )
    stubs = tuple(
        _payload_file(root, stubs_root, entry, label=f"stubs manifest entry {index}")
        for index, entry in enumerate(manifest_values["stubs"], start=1)
    )
    for payload_root, expected in expected_by_root.items():
        _verify_payload_coverage(root, payload_root, expected)
    _verify_payload_coverage(root, actionscript_root, {item.path for item in actionscript})
    _verify_payload_coverage(root, stubs_root, {item.path for item in stubs})
    return VerifiedSnapshot(
        root,
        descriptor,
        descriptor_sha256,
        tuple(files),
        actionscript,
        stubs,
    )


def _is_source(path: str) -> bool:
    pure = PurePosixPath(path)
    return pure.name.casefold() == "licenses.txt" or pure.suffix.casefold() in SOURCE_SUFFIXES


def _copy(item: PayloadFile, root: Path, relative_path: str) -> None:
    destination = root.joinpath(*PurePosixPath(relative_path).parts)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(item.source, destination)
    encoded = destination.read_bytes()
    if len(encoded) != item.size or _sha256_bytes(encoded) != item.sha256:
        raise PublicationError(f"copied payload changed during projection: {item.path}")
    destination.chmod(0o644)


def _assert_no_collisions(paths: list[str]) -> None:
    seen: dict[str, str] = {}
    for path in paths:
        folded = path.casefold()
        previous = seen.get(folded)
        if previous is not None:
            raise PublicationError(f"case-insensitive output collision: {previous!r} and {path!r}")
        seen[folded] = path


def _data_readme_intro() -> str:
    region_rows = "\n".join(
        f"| {client} | [`{data_branch}`]({REPOSITORY_URL}/tree/{data_branch}) |"
        for client, data_branch in REGION_BRANCHES
    )
    readme = f"""# wot-src

Публичная история читаемых исходников и текстовых данных клиентов World of Tanks и «Мира
танков». Служебный код и GitHub Actions workflows находятся в ветке
[`main`]({REPOSITORY_URL}/tree/main), а данные каждого клиента — в отдельной региональной ветке.

## Регионы

| Клиент | Data-ветка |
| --- | --- |
{region_rows}

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
"""  # noqa: RUF001 - the generated README intentionally contains Russian prose
    return readme


def render_bootstrap_readme() -> str:
    return f"""{_data_readme_intro()}

## Статус ветки

Первая версия клиента ещё не опубликована. После публикации здесь появятся данные версии и
машиночитаемые метаданные `.publication.json`.
"""


def _data_readme(
    *,
    target: str,
    branch: str,
    release_name: str,
    build_profile: str,
    publisher: str,
    snapshot_id: str,
) -> str:
    return f"""{_data_readme_intro()}

## Текущая публикация

- Target: `{target}`
- Ветка: `{branch}`
- Версия: `{release_name}`
- Профиль snapshot: `{build_profile}`
- Publisher: `{publisher}`
- GameSnapshot: `{snapshot_id}`

Машиночитаемые метаданные и контрольные идентификаторы находятся в `.publication.json`.
"""


def project_snapshot(
    snapshot_path: Path,
    output_path: Path,
    *,
    target: str,
    branch: str,
    expected_snapshot_id: str,
    expected_descriptor_sha256: str,
    expected_profile: str,
    config_path: Path,
) -> dict[str, Any]:
    if not SNAPSHOT_ID_RE.fullmatch(expected_snapshot_id):
        raise PublicationError("expected snapshot ID is invalid")
    if not SHA256_RE.fullmatch(expected_descriptor_sha256):
        raise PublicationError("expected descriptor SHA-256 is invalid")
    if expected_profile not in {"full", "light"}:
        raise PublicationError("expected profile must be full or light")
    if not branch or branch.startswith("-") or any(character.isspace() for character in branch):
        raise PublicationError("data branch name is invalid")
    target_config = _load_target(config_path, target)
    allowed_branches = {
        target_config.data_branch,
        f"test/{expected_profile}-{target}",
    }
    if branch not in allowed_branches:
        raise PublicationError(
            f"branch {branch!r} is not the configured data or test branch for {target}"
        )
    if branch == target_config.data_branch and expected_profile != "full":
        raise PublicationError("a light snapshot cannot be published to a production data branch")
    snapshot = _verify_snapshot(
        snapshot_path,
        expected_snapshot_id=expected_snapshot_id,
        expected_descriptor_sha256=expected_descriptor_sha256,
        expected_target=target,
        expected_profile=expected_profile,
    )
    source = _object(snapshot.descriptor["source"], label="snapshot source")
    publisher = _string(source.get("publisher"), label="snapshot publisher")
    if publisher != target_config.publisher:
        raise PublicationError(
            f"snapshot publisher {publisher!r} differs from target configuration"
        )
    layered_publisher = publisher != "lesta"
    if layered_publisher and target_config.default_locale is None:
        raise PublicationError(f"default locale is not configured for {target}")
    default_locale = target_config.default_locale
    if default_locale is not None and default_locale not in {
        item.language for item in snapshot.files if item.language is not None
    }:
        raise PublicationError(f"default locale {default_locale} is absent from the snapshot")

    base_files = [item for item in snapshot.files if item.language is None]
    source_map = {
        item.path: item
        for item in base_files
        if _is_source(item.path) and not item.path.casefold().startswith(GAMEFACE_PREFIX)
    }
    if layered_publisher:
        source_map.update(
            {
                item.path: item
                for item in snapshot.files
                if item.language == default_locale
                and _is_source(item.path)
                and not item.path.casefold().startswith(GAMEFACE_PREFIX)
            }
        )
    locale_files = (
        {
            language: tuple(
                item
                for item in snapshot.files
                if item.language == language
                and _is_source(item.path)
                and not item.path.casefold().startswith(GAMEFACE_PREFIX)
            )
            for language in sorted(
                {item.language for item in snapshot.files if item.language is not None}
            )
        }
        if layered_publisher
        else {}
    )
    gameface_files = tuple(
        item
        for item in base_files
        if item.path.casefold().startswith(GAMEFACE_PREFIX)
        and len(item.path) > len(GAMEFACE_PREFIX)
    )
    if not gameface_files:
        raise PublicationError(
            "snapshot has no base res/gui/gameface payload; refusing an incomplete publication"
        )
    actionscript_files = tuple(
        item
        for item in snapshot.actionscript
        if PurePosixPath(item.path).suffix.casefold() == ".as"
    )

    output = output_path.absolute()
    if output.exists():
        raise PublicationError(f"output path already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}-", dir=output.parent))
    try:
        output_paths = [f"sources/{path}" for path in source_map]
        output_paths.extend(
            f"locales/{language}/{item.path}"
            for language, items in locale_files.items()
            for item in items
        )
        output_paths.extend(
            f"sources-gameface/{item.path[len(GAMEFACE_PREFIX):]}"
            for item in gameface_files
        )
        output_paths.extend(f"sources-as3/{item.path}" for item in actionscript_files)
        output_paths.extend(f"stubs/{item.path}" for item in snapshot.stubs)
        _assert_no_collisions(output_paths)

        for path, item in sorted(source_map.items()):
            relative = f"sources/{path}"
            _copy(item, temporary, relative)
        for language, items in locale_files.items():
            for item in items:
                relative = f"locales/{language}/{item.path}"
                _copy(item, temporary, relative)
        for item in gameface_files:
            relative = f"sources-gameface/{item.path[len(GAMEFACE_PREFIX):]}"
            _copy(item, temporary, relative)
        for item in actionscript_files:
            relative = f"sources-as3/{item.path}"
            _copy(item, temporary, relative)
        for item in snapshot.stubs:
            relative = f"stubs/{item.path}"
            _copy(item, temporary, relative)

        release_name = _string(source.get("release_name"), label="snapshot release name")
        (temporary / "README.md").write_text(
            _data_readme(
                target=target,
                branch=branch,
                release_name=release_name,
                build_profile=expected_profile,
                publisher=publisher,
                snapshot_id=expected_snapshot_id,
            ),
            encoding="utf-8",
        )
        (temporary / ".version_name").write_text(f"{release_name}\n", encoding="utf-8")
        publication: dict[str, Any] = {
            "branch": branch,
            "build_profile": expected_profile,
            "client_type": source.get("client_type"),
            "counts": {
                "locales": {language: len(items) for language, items in locale_files.items()},
                "sources": len(source_map),
                "sources_as3": len(actionscript_files),
                "sources_gameface": len(gameface_files),
                "stubs": len(snapshot.stubs),
            },
            "descriptor_sha256": snapshot.descriptor_sha256,
            "languages": source.get("languages"),
            "publisher": publisher,
            "schema_version": 1,
            "snapshot_contract_version": snapshot.descriptor.get("contract_version"),
            "snapshot_created_at": snapshot.descriptor.get("created_at"),
            "snapshot_id": expected_snapshot_id,
            "target": target,
            "version_name": release_name,
        }
        if layered_publisher:
            publication["default_locale"] = default_locale
        (temporary / ".publication.json").write_bytes(_canonical_json(publication))
        os.replace(temporary, output)
        return publication
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise


def _clear_worktree(path: Path) -> None:
    for child in path.iterdir():
        if child.name == ".git":
            continue
        if child.is_symlink() or child.is_file():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)
        else:
            raise PublicationError(f"unsupported worktree entry: {child}")


def _copy_tree(source: Path, destination: Path) -> None:
    for child in source.iterdir():
        target = destination / child.name
        if child.is_dir():
            shutil.copytree(child, target)
        elif child.is_file() and not child.is_symlink():
            shutil.copy2(child, target)
        else:
            raise PublicationError(f"projected tree contains an unsupported entry: {child}")


def _existing_publication(worktree: Path) -> dict[str, Any] | None:
    path = worktree / ".publication.json"
    if not path.exists():
        return None
    value, _encoded = _read_json(path, label="existing publication metadata")
    return value


def _validate_bootstrap_branch(worktree: Path) -> None:
    commit_count = _run_git(worktree, "rev-list", "--count", "HEAD").stdout.strip()
    subject = _run_git(worktree, "log", "-1", "--format=%s").stdout.strip()
    tracked_files = _run_git(
        worktree, "ls-tree", "-r", "--name-only", "HEAD"
    ).stdout.splitlines()
    if commit_count != "1" or subject != "init" or tracked_files != ["README.md"]:
        raise PublicationError(
            "existing data branch is not a valid README-only init branch"
        )
    readme = _regular_file(worktree, "README.md", label="bootstrap README").read_text(
        encoding="utf-8"
    )
    if readme != render_bootstrap_readme():
        raise PublicationError("existing data branch bootstrap README does not match")


def publish_snapshot(
    repository_path: Path,
    snapshot_path: Path,
    *,
    target: str,
    branch: str,
    expected_snapshot_id: str,
    expected_descriptor_sha256: str,
    expected_profile: str,
    config_path: Path,
) -> dict[str, Any]:
    repository = repository_path.absolute()
    if not repository.is_dir():
        raise PublicationError(f"repository is not a directory: {repository}")
    if _run_git(repository, "rev-parse", "--is-inside-work-tree").stdout.strip() != "true":
        raise PublicationError(f"path is not a Git worktree: {repository}")
    branch_check = subprocess.run(
        ["git", "check-ref-format", "--branch", branch],
        text=True,
        capture_output=True,
        check=False,
    )
    if branch_check.returncode != 0:
        raise PublicationError(f"invalid data branch name: {branch}")

    temporary = Path(tempfile.mkdtemp(prefix="wot-src-publication-"))
    projected_tree = temporary / "projected"
    worktree = temporary / "worktree"
    worktree_registered = False
    try:
        publication = project_snapshot(
            snapshot_path,
            projected_tree,
            target=target,
            branch=branch,
            expected_snapshot_id=expected_snapshot_id,
            expected_descriptor_sha256=expected_descriptor_sha256,
            expected_profile=expected_profile,
            config_path=config_path,
        )
        remote_ref = f"refs/heads/{branch}"
        remote_check = _run_git(
            repository,
            "ls-remote",
            "--exit-code",
            "--heads",
            "origin",
            remote_ref,
            check=False,
        )
        if remote_check.returncode not in {0, 2}:
            details = remote_check.stderr.strip() or remote_check.stdout.strip()
            raise PublicationError(f"could not inspect remote data branch: {details}")
        branch_exists = remote_check.returncode == 0
        if branch_exists:
            tracking_ref = f"refs/remotes/origin/{branch}"
            _run_git(repository, "fetch", "--no-tags", "origin", f"+{remote_ref}:{tracking_ref}")
            _run_git(repository, "worktree", "add", "--detach", str(worktree), tracking_ref)
        else:
            _run_git(repository, "worktree", "add", "--detach", str(worktree), "HEAD")
            _run_git(worktree, "switch", "--orphan", branch)
            _run_git(worktree, "read-tree", "--empty")
        worktree_registered = True

        existing = _existing_publication(worktree) if branch_exists else None
        if branch_exists and existing is None:
            target_config = _load_target(config_path, target)
            if branch != target_config.data_branch:
                raise PublicationError(
                    "existing test branch has no .publication.json ownership marker"
                )
            _validate_bootstrap_branch(worktree)
        release_name = _string(publication.get("version_name"), label="publication version")
        if existing is not None:
            existing_snapshot_id = existing.get("snapshot_id")
            existing_version = existing.get("version_name")
            if existing_snapshot_id == expected_snapshot_id and existing_version != release_name:
                raise PublicationError("existing snapshot ID has a different version name")
            if existing_version == release_name and existing_snapshot_id != expected_snapshot_id:
                raise PublicationError(
                    f"version {release_name} is already bound to another snapshot"
                )

        _clear_worktree(worktree)
        _copy_tree(projected_tree, worktree)
        _run_git(worktree, "add", "--all")
        difference = _run_git(worktree, "diff", "--cached", "--quiet", check=False)
        if difference.returncode not in {0, 1}:
            raise PublicationError(f"could not compare projected data tree: {difference.stderr}")
        if existing is not None and existing.get("snapshot_id") == expected_snapshot_id:
            if difference.returncode != 0:
                raise PublicationError(
                    "the same snapshot now projects to a different data tree"
                )
            commit_sha = _run_git(worktree, "rev-parse", "HEAD").stdout.strip()
            return {
                **publication,
                "commit_sha": commit_sha,
                "publication_state": "unchanged",
            }
        if difference.returncode == 0:
            raise PublicationError("new snapshot produced no data-tree changes")
        if branch_exists:
            subjects = _run_git(worktree, "log", "--format=%s").stdout.splitlines()
            if release_name in subjects:
                raise PublicationError(f"version {release_name} already exists in branch history")
        _run_git(worktree, "commit", "--message", release_name)
        commit_sha = _run_git(worktree, "rev-parse", "HEAD").stdout.strip()
        _run_git(worktree, "push", "origin", f"HEAD:{remote_ref}")
        return {
            **publication,
            "commit_sha": commit_sha,
            "publication_state": "published",
        }
    finally:
        if worktree_registered:
            _run_git(repository, "worktree", "remove", "--force", str(worktree), check=False)
            _run_git(repository, "worktree", "prune", check=False)
        shutil.rmtree(temporary, ignore_errors=True)


__all__ = [
    "PublicationError",
    "project_snapshot",
    "publish_snapshot",
    "render_bootstrap_readme",
]
