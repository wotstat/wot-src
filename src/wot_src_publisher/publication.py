from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ElementTree
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
GIT_OBJECT_ID_RE = re.compile(r"^(?:[a-f0-9]{40}|[a-f0-9]{64})$")
SNAPSHOT_ID_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
LANGUAGE_RE = re.compile(r"^[A-Z]{2}(?:_[A-Z]{2})?$")
VERSION_XML_COMMIT_RE = re.compile(r"^v\.[0-9]+(?:\.[0-9]+){3} #[0-9]+$")
SOURCE_SUFFIXES = frozenset({".po", ".py", ".xml"})
GAMEFACE_PREFIX = "res/gui/gameface/"
MANIFEST_NAMES = ("files", "actionscript", "stubs", "packages", "conflicts")
REPOSITORY_URL = "https://github.com/wotstat/wot-src"
OBJECT_STAGING_THRESHOLD_BYTES = 1_000_000_000
OBJECT_STAGING_BATCH_BYTES = 1_000_000_000
GITHUB_MAX_BLOB_BYTES = 100 * 1024 * 1024
GITHUB_API_VERSION = "2022-11-28"
GITHUB_REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
LEGACY_BOOTSTRAP_README_SHA256S = frozenset(
    {
        "c0b5be60db2a12702d8f8856079d6d4098624dd663253c95c76b4b50a89896b4",
        "fe9c7b92755ce20f3004f4ef66d3c0518b1a89253ebe9ac75c286f309155cdec",
    }
)
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


def _progress(stage: str, status: str, **fields: object) -> None:
    details = " ".join(
        f"{name}={json.dumps(value, ensure_ascii=False, separators=(',', ':'))}"
        for name, value in fields.items()
    )
    suffix = f" {details}" if details else ""
    print(f"publisher stage={stage} status={status}{suffix}", file=sys.stderr, flush=True)


@contextmanager
def _progress_stage(stage: str, **fields: object) -> Iterator[dict[str, object]]:
    started_at = time.monotonic()
    completion_fields: dict[str, object] = {}
    _progress(stage, "started", **fields)
    try:
        yield completion_fields
    except Exception:
        _progress(
            stage,
            "failed",
            elapsed_seconds=round(time.monotonic() - started_at, 3),
        )
        raise
    _progress(
        stage,
        "completed",
        elapsed_seconds=round(time.monotonic() - started_at, 3),
        **completion_fields,
    )


class _FileProgress:
    def __init__(self, stage: str, total: int) -> None:
        self.stage = stage
        self.total = total
        self.files = 0
        self.bytes = 0
        self.interval = max(100, (total + 19) // 20)
        self.next_report = min(self.interval, total)

    def advance(self, size: int) -> None:
        self.files += 1
        self.bytes += size
        if self.files < self.next_report:
            return
        percent = round(self.files * 100 / self.total, 1) if self.total else 100.0
        _progress(
            self.stage,
            "in_progress",
            files=self.files,
            total_files=self.total,
            bytes=self.bytes,
            percent=percent,
        )
        self.next_report = min(self.total, self.next_report + self.interval)


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


@dataclass(frozen=True, slots=True)
class _GitBlob:
    path: str
    mode: str
    object_id: str
    size: int


@dataclass(frozen=True, slots=True)
class _StagedObjects:
    remote_ref: str
    tree_sha: str


def _run_git(
    repository: Path,
    *arguments: str,
    check: bool = True,
    input_text: str | None = None,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        text=True,
        capture_output=True,
        check=False,
        input=input_text,
    )
    if check and result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip()
        raise PublicationError(
            f"git {arguments[0] if arguments else 'command'} failed: {details}"
        )
    return result


def _run_git_streaming(
    repository: Path,
    *arguments: str,
) -> subprocess.CompletedProcess[str]:
    command = ["git", "-C", str(repository), *arguments]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if process.stdout is None:  # pragma: no cover - PIPE always creates stdout
        raise PublicationError("could not capture git output")
    chunks: list[str] = []
    while chunk := os.read(process.stdout.fileno(), 65536):
        text = chunk.decode("utf-8", errors="replace")
        chunks.append(text)
        sys.stderr.write(text)
        sys.stderr.flush()
    return subprocess.CompletedProcess(
        command,
        process.wait(),
        "",
        "".join(chunks),
    )


def _remote_head(repository: Path, remote_ref: str) -> str | None:
    result = _run_git(
        repository,
        "ls-remote",
        "--heads",
        "origin",
        remote_ref,
        check=False,
    )
    if result.returncode != 0:
        return None
    fields = result.stdout.split()
    if len(fields) != 2 or fields[1] != remote_ref or not GIT_OBJECT_ID_RE.fullmatch(fields[0]):
        return None
    return fields[0]


def _is_retryable_push_failure(details: str) -> bool:
    lowered = details.casefold()
    if "pack exceeds maximum allowed size" in lowered or "file exceeds github's" in lowered:
        return False
    return bool(re.search(r"\bhttp 5[0-9]{2}\b", lowered)) or any(
        marker in lowered
        for marker in (
            "connection reset",
            "connection timed out",
            "could not resolve host",
            "failed to connect",
            "operation timed out",
            "remote end hung up unexpectedly",
            "the requested url returned error: 5",
            "unexpected disconnect",
        )
    )


def _git_error_excerpt(details: str) -> str:
    lines = [line.strip() for line in re.split(r"[\r\n]+", details) if line.strip()]
    excerpt = " | ".join(lines[-20:])
    excerpt = re.sub(r"https://[^@\s]+@", "https://***@", excerpt)
    return excerpt[-4000:]


def _github_api_credentials() -> tuple[str, str]:
    repository = os.environ.get("PUBLISHER_GITHUB_REPOSITORY", "")
    token = os.environ.get("PUBLISHER_GITHUB_TOKEN", "")
    if not GITHUB_REPOSITORY_RE.fullmatch(repository):
        raise PublicationError(
            "PUBLISHER_GITHUB_REPOSITORY must be an owner/repository slug"
        )
    if not token:
        raise PublicationError("PUBLISHER_GITHUB_TOKEN is required for a large publication")
    return repository, token


def _github_api_error_excerpt(body: bytes) -> str:
    details = body.decode("utf-8", errors="replace")
    try:
        document = json.loads(details)
    except json.JSONDecodeError:
        pass
    else:
        if isinstance(document, dict):
            message = document.get("message")
            details = str(message) if message else "GitHub API request failed"
    return re.sub(r"https://[^@\s]+@", "https://***@", details.strip())[-2000:]


def _github_api_request(
    repository: str,
    token: str,
    method: str,
    path: str,
    payload: dict[str, object] | None = None,
    *,
    retry_delays: Sequence[float] = (5.0, 15.0),
) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, separators=(",", ":")).encode()
    attempts = len(retry_delays) + 1
    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(
            f"https://api.github.com/repos/{repository}/{path}",
            data=data,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "User-Agent": "wotstat-snapshot-publisher",
                "X-GitHub-Api-Version": GITHUB_API_VERSION,
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
        except urllib.error.HTTPError as error:
            body = error.read()
            retryable = error.code == 429 or 500 <= error.code < 600
            if retryable and attempt < attempts:
                delay = retry_delays[attempt - 1]
                _progress(
                    "github-api",
                    "retrying",
                    method=method,
                    path=path,
                    status_code=error.code,
                    attempt=attempt,
                    next_attempt=attempt + 1,
                    retry_delay_seconds=delay,
                )
                time.sleep(delay)
                continue
            raise PublicationError(
                f"GitHub API {method} {path} failed with HTTP {error.code}: "
                f"{_github_api_error_excerpt(body)}"
            ) from error
        except urllib.error.URLError as error:
            if attempt < attempts:
                delay = retry_delays[attempt - 1]
                _progress(
                    "github-api",
                    "retrying",
                    method=method,
                    path=path,
                    attempt=attempt,
                    next_attempt=attempt + 1,
                    retry_delay_seconds=delay,
                    reason=type(error.reason).__name__,
                )
                time.sleep(delay)
                continue
            raise PublicationError(
                f"GitHub API {method} {path} transport failed: {type(error.reason).__name__}"
            ) from error
        try:
            document = json.loads(body)
        except json.JSONDecodeError as error:
            raise PublicationError(
                f"GitHub API {method} {path} returned invalid JSON"
            ) from error
        if not isinstance(document, dict):
            raise PublicationError(
                f"GitHub API {method} {path} returned a non-object response"
            )
        return document
    raise AssertionError("unreachable GitHub API retry state")


def _required_git_object_id(document: dict[str, Any], *, label: str) -> str:
    object_id = document.get("sha")
    if not isinstance(object_id, str) or not GIT_OBJECT_ID_RE.fullmatch(object_id):
        raise PublicationError(f"GitHub API returned an invalid {label} object ID")
    return object_id


def _publish_large_commit_via_github_api(
    worktree: Path,
    *,
    branch: str,
    branch_exists: bool,
    commit_sha: str,
    tree_sha: str,
) -> str:
    repository, token = _github_api_credentials()
    parent_result = _run_git(
        worktree,
        "rev-parse",
        "--verify",
        f"{commit_sha}^",
        check=False,
    )
    parent = parent_result.stdout.strip() if parent_result.returncode == 0 else None
    if branch_exists != (parent is not None):
        raise PublicationError("local publication parent does not match remote branch state")
    expected_tree = _run_git(
        worktree, "rev-parse", f"{commit_sha}^{{tree}}"
    ).stdout.strip()
    if tree_sha != expected_tree:
        raise PublicationError(
            "staged Git tree does not match the locally verified publication tree"
        )
    _progress(
        "github-finalize",
        "started",
        repository=repository,
        branch=branch,
        tree=tree_sha[:12],
        provisional_commit=commit_sha[:12],
    )
    _progress("github-finalize", "tree_verified", tree=tree_sha[:12])

    identity = _run_git(
        worktree,
        "show",
        "--no-patch",
        "--format=%an%x00%ae%x00%aI%x00%cn%x00%ce%x00%cI",
        commit_sha,
    ).stdout.rstrip("\n").split("\0")
    if len(identity) != 6:
        raise PublicationError("could not inspect publication commit identity")
    (
        author_name,
        author_email,
        author_date,
        committer_name,
        committer_email,
        committer_date,
    ) = identity
    message = _run_git(
        worktree,
        "show",
        "--no-patch",
        "--format=%B",
        commit_sha,
    ).stdout.rstrip("\n")
    commit_payload: dict[str, object] = {
        "message": message,
        "tree": tree_sha,
        "parents": [parent] if parent is not None else [],
        "author": {"name": author_name, "email": author_email, "date": author_date},
        "committer": {
            "name": committer_name,
            "email": committer_email,
            "date": committer_date,
        },
    }
    commit_response = _github_api_request(
        repository,
        token,
        "POST",
        "git/commits",
        commit_payload,
    )
    published_commit = _required_git_object_id(commit_response, label="commit")
    _progress("github-finalize", "commit_created", commit=published_commit[:12])

    ref_path = f"git/refs/heads/{branch}"
    get_ref_path = f"git/ref/heads/{branch}"
    try:
        if branch_exists:
            ref_response = _github_api_request(
                repository,
                token,
                "PATCH",
                ref_path,
                {"sha": published_commit, "force": False},
            )
        else:
            ref_response = _github_api_request(
                repository,
                token,
                "POST",
                "git/refs",
                {"ref": f"refs/heads/{branch}", "sha": published_commit},
            )
    except PublicationError as update_error:
        try:
            ref_response = _github_api_request(
                repository,
                token,
                "GET",
                get_ref_path,
            )
            remote_object = ref_response.get("object")
            remote_sha = (
                remote_object.get("sha") if isinstance(remote_object, dict) else None
            )
        except PublicationError as inspect_error:
            raise update_error from inspect_error
        if remote_sha != published_commit:
            raise update_error
    else:
        remote_object = ref_response.get("object")
        remote_sha = remote_object.get("sha") if isinstance(remote_object, dict) else None
        if remote_sha != published_commit:
            raise PublicationError("GitHub API returned an unexpected updated ref target")
    _progress(
        "github-finalize",
        "ref_updated",
        branch=branch,
        commit=published_commit[:12],
    )
    _progress(
        "github-finalize",
        "completed",
        branch=branch,
        commit=published_commit[:12],
    )
    return published_commit


def _git_object_stats(repository: Path) -> dict[str, int]:
    values: dict[str, int] = {}
    for line in _run_git(repository, "count-objects", "-v").stdout.splitlines():
        name, separator, raw_value = line.partition(": ")
        if separator and raw_value.isdigit():
            values[name] = int(raw_value)
    return {
        "loose_objects": values.get("count", 0),
        "loose_object_bytes": values.get("size", 0) * 1024,
        "packs": values.get("packs", 0),
        "packed_object_bytes": values.get("size-pack", 0) * 1024,
    }


def _changed_git_blobs(worktree: Path, changed_files: Sequence[str]) -> tuple[_GitBlob, ...]:
    changed = set(changed_files)
    if not changed:
        return ()
    entries: list[_GitBlob] = []
    for record in _run_git(worktree, "ls-files", "--stage", "-z").stdout.split("\0"):
        if not record:
            continue
        metadata, separator, path = record.partition("\t")
        if not separator or path not in changed:
            continue
        fields = metadata.split()
        if len(fields) != 3 or fields[2] != "0":
            raise PublicationError(f"could not inspect staged Git blob: {path}")
        mode, object_id, _stage = fields
        if mode not in {"100644", "100755"} or not GIT_OBJECT_ID_RE.fullmatch(object_id):
            raise PublicationError(f"unsupported staged Git entry: {path}")
        file_path = worktree / path
        file_stat = file_path.stat()
        if not stat.S_ISREG(file_stat.st_mode):
            raise PublicationError(f"staged publication entry is not a regular file: {path}")
        entries.append(_GitBlob(path, mode, object_id, file_stat.st_size))
    expected = {
        path
        for path in changed
        if (worktree / path).exists() and not (worktree / path).is_dir()
    }
    actual = {entry.path for entry in entries}
    if actual != expected:
        missing = sorted(expected - actual)
        raise PublicationError(
            f"could not resolve {len(missing)} changed Git blobs"
            + (f": {missing[0]}" if missing else "")
        )
    return tuple(entries)


def _partition_git_blobs(
    blobs: Sequence[_GitBlob],
    *,
    max_batch_bytes: int,
) -> tuple[tuple[_GitBlob, ...], ...]:
    if max_batch_bytes <= 0:
        raise PublicationError("Git object staging batch budget must be positive")
    batches: list[tuple[_GitBlob, ...]] = []
    current: list[_GitBlob] = []
    current_bytes = 0
    for blob in blobs:
        if blob.size > GITHUB_MAX_BLOB_BYTES:
            raise PublicationError(
                f"Git blob exceeds GitHub's 100 MiB file limit: {blob.path} ({blob.size} bytes)"
            )
        if blob.size > max_batch_bytes:
            raise PublicationError(
                f"Git blob exceeds the staging batch budget: {blob.path} ({blob.size} bytes)"
            )
        if current and current_bytes + blob.size > max_batch_bytes:
            batches.append(tuple(current))
            current = []
            current_bytes = 0
        current.append(blob)
        current_bytes += blob.size
    if current:
        batches.append(tuple(current))
    return tuple(batches)


def _staging_ref(branch: str, commit_sha: str) -> str:
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    if run_id.isdigit() and run_attempt.isdigit():
        owner = f"{run_id}-{run_attempt}"
    else:
        owner = f"local-{os.getpid()}"
    return f"refs/heads/publication-staging/{branch}/{owner}-{commit_sha[:12]}"


def _delete_remote_ref(repository: Path, remote_ref: str) -> None:
    result = _run_git_streaming(
        repository,
        "push",
        "--progress",
        "origin",
        f":{remote_ref}",
    )
    if result.returncode == 0 or _remote_head(repository, remote_ref) is None:
        _progress("stage-objects", "cleanup_completed", remote_ref=remote_ref)
        return
    details = result.stderr.strip() or result.stdout.strip()
    _progress(
        "stage-objects",
        "cleanup_failed",
        remote_ref=remote_ref,
        error=_git_error_excerpt(details),
    )


@contextmanager
def _prestage_large_git_objects(
    repository: Path,
    publication_worktree: Path,
    staging_worktree: Path,
    *,
    branch: str,
    commit_sha: str,
    changed_files: Sequence[str],
) -> Iterator[_StagedObjects | None]:
    blobs = _changed_git_blobs(publication_worktree, changed_files)
    total_bytes = sum(blob.size for blob in blobs)
    batches = _partition_git_blobs(
        blobs,
        max_batch_bytes=OBJECT_STAGING_BATCH_BYTES,
    )
    if total_bytes <= OBJECT_STAGING_THRESHOLD_BYTES:
        _progress(
            "stage-objects",
            "skipped",
            reason="below_threshold",
            files=len(blobs),
            bytes=total_bytes,
            threshold_bytes=OBJECT_STAGING_THRESHOLD_BYTES,
        )
        yield None
        return

    remote_ref = _staging_ref(branch, commit_sha)
    registered = False
    pushed_ref = False
    _progress(
        "stage-objects",
        "started",
        files=len(blobs),
        bytes=total_bytes,
        batches=len(batches),
        batch_budget_bytes=OBJECT_STAGING_BATCH_BYTES,
        remote_ref=remote_ref,
    )
    try:
        parent = _run_git(
            publication_worktree,
            "rev-parse",
            "--verify",
            f"{commit_sha}^",
            check=False,
        )
        staging_base = parent.stdout.strip() if parent.returncode == 0 else commit_sha
        _run_git(
            repository,
            "worktree",
            "add",
            "--detach",
            "--no-checkout",
            str(staging_worktree),
            staging_base,
        )
        registered = True
        if parent.returncode != 0:
            _run_git(
                staging_worktree,
                "switch",
                "--orphan",
                f"publication-staging-{commit_sha[:12]}",
            )
            _run_git(staging_worktree, "read-tree", "--empty")
        deleted_paths = sorted(set(changed_files) - {blob.path for blob in blobs})
        if deleted_paths:
            _run_git(
                staging_worktree,
                "update-index",
                "--force-remove",
                "-z",
                "--stdin",
                input_text="".join(f"{path}\0" for path in deleted_paths),
            )
        for batch_number, batch in enumerate(batches, start=1):
            batch_bytes = sum(blob.size for blob in batch)
            index_info = "".join(
                f"{blob.mode} {blob.object_id}\t{blob.path}\0" for blob in batch
            )
            _run_git(
                staging_worktree,
                "update-index",
                "-z",
                "--index-info",
                input_text=index_info,
            )
            _run_git(
                staging_worktree,
                "commit",
                "--message",
                f"stage publication objects {batch_number}/{len(batches)}",
            )
            staging_commit = _run_git(
                staging_worktree, "rev-parse", "HEAD"
            ).stdout.strip()
            pushed_ref = True
            _push_commit(staging_worktree, remote_ref, staging_commit)
            _progress(
                "stage-objects",
                "batch_completed",
                batch=batch_number,
                batches=len(batches),
                files=len(batch),
                bytes=batch_bytes,
                commit=staging_commit[:12],
            )
        staging_tree = _run_git(
            staging_worktree, "rev-parse", "HEAD^{tree}"
        ).stdout.strip()
        expected_tree = _run_git(
            publication_worktree, "rev-parse", f"{commit_sha}^{{tree}}"
        ).stdout.strip()
        if staging_tree != expected_tree:
            raise PublicationError(
                "cumulative staging tree does not match the publication tree"
            )
        _progress(
            "stage-objects",
            "completed",
            remote_ref=remote_ref,
            tree=staging_tree[:12],
        )
        yield _StagedObjects(remote_ref=remote_ref, tree_sha=staging_tree)
    finally:
        if pushed_ref:
            _delete_remote_ref(repository, remote_ref)
        if registered:
            _run_git(
                repository,
                "worktree",
                "remove",
                "--force",
                str(staging_worktree),
                check=False,
            )
            _run_git(repository, "worktree", "prune", check=False)


def _push_commit(
    worktree: Path,
    remote_ref: str,
    commit_sha: str,
    *,
    retry_delays: Sequence[float] = (5.0, 15.0),
) -> None:
    attempts = len(retry_delays) + 1
    for attempt in range(1, attempts + 1):
        started_at = time.monotonic()
        _progress(
            "push",
            "started",
            attempt=attempt,
            attempts=attempts,
            commit=commit_sha[:12],
            remote_ref=remote_ref,
        )
        result = _run_git_streaming(
            worktree,
            "push",
            "--progress",
            "origin",
            f"HEAD:{remote_ref}",
        )
        elapsed_seconds = round(time.monotonic() - started_at, 3)
        if result.returncode == 0:
            _progress(
                "push",
                "completed",
                attempt=attempt,
                elapsed_seconds=elapsed_seconds,
                commit=commit_sha[:12],
                remote_ref=remote_ref,
            )
            return

        if _remote_head(worktree, remote_ref) == commit_sha:
            _progress(
                "push",
                "completed",
                attempt=attempt,
                elapsed_seconds=elapsed_seconds,
                commit=commit_sha[:12],
                result="remote_updated_after_transport_error",
                remote_ref=remote_ref,
            )
            return

        details = result.stderr.strip() or result.stdout.strip()
        retryable = _is_retryable_push_failure(details)
        if retryable and attempt < attempts:
            delay = retry_delays[attempt - 1]
            _progress(
                "push",
                "retrying",
                attempt=attempt,
                elapsed_seconds=elapsed_seconds,
                next_attempt=attempt + 1,
                retry_delay_seconds=delay,
                reason="transient_git_transport_error",
            )
            time.sleep(delay)
            continue

        _progress(
            "push",
            "failed",
            attempt=attempt,
            elapsed_seconds=elapsed_seconds,
            retryable=retryable,
        )
        raise PublicationError(f"git push failed: {_git_error_excerpt(details)}")


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


def _pretty_json(value: object) -> bytes:
    try:
        return (
            json.dumps(
                value,
                allow_nan=False,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ).encode("utf-8")
            + b"\n"
        )
    except (TypeError, ValueError) as error:
        raise PublicationError(f"document cannot be encoded as JSON: {error}") from error


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
    payload_progress = _FileProgress(
        "verify",
        sum(
            len(manifest_values[name])
            for name in ("files", "actionscript", "stubs")
        ),
    )
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
        payload_progress.advance(item.size)

    actionscript: list[PayloadFile] = []
    for index, entry in enumerate(manifest_values["actionscript"], start=1):
        item = _payload_file(
            root,
            actionscript_root,
            entry,
            label=f"ActionScript manifest entry {index}",
        )
        actionscript.append(item)
        payload_progress.advance(item.size)
    stubs: list[PayloadFile] = []
    for index, entry in enumerate(manifest_values["stubs"], start=1):
        item = _payload_file(root, stubs_root, entry, label=f"stubs manifest entry {index}")
        stubs.append(item)
        payload_progress.advance(item.size)
    _progress("verify", "in_progress", phase="payload_coverage")
    for payload_root, expected in expected_by_root.items():
        _verify_payload_coverage(root, payload_root, expected)
    _verify_payload_coverage(root, actionscript_root, {item.path for item in actionscript})
    _verify_payload_coverage(root, stubs_root, {item.path for item in stubs})
    return VerifiedSnapshot(
        root,
        descriptor,
        descriptor_sha256,
        tuple(files),
        tuple(actionscript),
        tuple(stubs),
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


def _commit_subject(source_map: dict[str, PayloadFile]) -> str:
    candidates = [
        item for path, item in source_map.items() if path.casefold() == "version.xml"
    ]
    if len(candidates) != 1:
        raise PublicationError("projected sources must contain exactly one root version.xml")
    try:
        root = ElementTree.fromstring(candidates[0].source.read_bytes())
    except (OSError, ElementTree.ParseError) as error:
        raise PublicationError(f"cannot parse root version.xml: {error}") from error
    version = root.find("version")
    subject = " ".join(version.text.split()) if version is not None and version.text else ""
    if not VERSION_XML_COMMIT_RE.fullmatch(subject):
        raise PublicationError(f"root version.xml has an invalid commit version: {subject!r}")
    return subject.removeprefix("v.")


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

Каждая production data-ветка начинается с bootstrap commit `init`, содержащего этот README. Каждая
публикация завершается version commit: его сообщение строится из `sources/version.xml` без префикса
`v.` в формате `2.3.1.0 #903`, а точный release name записывается в `.version_name`.
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
    with _progress_stage("verify", target=target, profile=expected_profile) as progress:
        snapshot = _verify_snapshot(
            snapshot_path,
            expected_snapshot_id=expected_snapshot_id,
            expected_descriptor_sha256=expected_descriptor_sha256,
            expected_target=target,
            expected_profile=expected_profile,
        )
        payload_files = (*snapshot.files, *snapshot.actionscript, *snapshot.stubs)
        progress.update(
            files=len(payload_files),
            bytes=sum(item.size for item in payload_files),
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
        projected_file_count = (
            len(source_map)
            + sum(len(items) for items in locale_files.values())
            + len(gameface_files)
            + len(actionscript_files)
            + len(snapshot.stubs)
        )
        projection_progress = _FileProgress("project", projected_file_count)
        _progress(
            "project",
            "started",
            files=projected_file_count,
            target=target,
            branch=branch,
        )
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
            projection_progress.advance(item.size)
        for language, items in locale_files.items():
            for item in items:
                relative = f"locales/{language}/{item.path}"
                _copy(item, temporary, relative)
                projection_progress.advance(item.size)
        for item in gameface_files:
            relative = f"sources-gameface/{item.path[len(GAMEFACE_PREFIX):]}"
            _copy(item, temporary, relative)
            projection_progress.advance(item.size)
        for item in actionscript_files:
            relative = f"sources-as3/{item.path}"
            _copy(item, temporary, relative)
            projection_progress.advance(item.size)
        for item in snapshot.stubs:
            relative = f"stubs/{item.path}"
            _copy(item, temporary, relative)
            projection_progress.advance(item.size)

        release_name = _string(source.get("release_name"), label="snapshot release name")
        commit_subject = _commit_subject(source_map)
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
            "commit_subject": commit_subject,
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
        (temporary / ".publication.json").write_bytes(_pretty_json(publication))
        os.replace(temporary, output)
        _progress(
            "project",
            "completed",
            files=projection_progress.files,
            bytes=projection_progress.bytes,
            counts=publication["counts"],
        )
        return publication
    except Exception:
        _progress("project", "failed", files=projection_progress.files)
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
    tracked = _run_git(
        worktree,
        "ls-tree",
        "--name-only",
        "HEAD",
        "--",
        ".publication.json",
    ).stdout.strip()
    if not tracked:
        return None
    encoded = _run_git(worktree, "show", "HEAD:.publication.json").stdout
    try:
        value = json.loads(encoded)
    except json.JSONDecodeError as error:
        raise PublicationError(
            f"cannot read existing publication metadata: {error}"
        ) from error
    return _object(value, label="existing publication metadata")


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
    readme = _run_git(worktree, "show", "HEAD:README.md").stdout
    accepted_readme_sha256s = LEGACY_BOOTSTRAP_README_SHA256S | {
        _sha256_bytes(render_bootstrap_readme().encode())
    }
    if _sha256_bytes(readme.encode()) not in accepted_readme_sha256s:
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
    staging_worktree = temporary / "staging-worktree"
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
        with _progress_stage("inspect-remote", branch=branch) as progress:
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
            progress["branch_exists"] = branch_exists

        with _progress_stage("prepare-worktree", branch=branch) as progress:
            if branch_exists:
                tracking_ref = f"refs/remotes/origin/{branch}"
                _run_git(repository, "config", "remote.origin.promisor", "true")
                _run_git(repository, "config", "remote.origin.partialclonefilter", "tree:0")
                _run_git(
                    repository,
                    "fetch",
                    "--no-tags",
                    "--filter=tree:0",
                    "origin",
                    f"+{remote_ref}:{tracking_ref}",
                )
                _run_git(
                    repository,
                    "worktree",
                    "add",
                    "--detach",
                    "--no-checkout",
                    str(worktree),
                    tracking_ref,
                )
                worktree_registered = True
            else:
                _run_git(
                    repository,
                    "worktree",
                    "add",
                    "--detach",
                    "--no-checkout",
                    str(worktree),
                    "HEAD",
                )
                worktree_registered = True
                _run_git(worktree, "switch", "--orphan", branch)
                _run_git(worktree, "read-tree", "--empty")

            existing = _existing_publication(worktree) if branch_exists else None
            if branch_exists and existing is None:
                target_config = _load_target(config_path, target)
                if branch != target_config.data_branch:
                    raise PublicationError(
                        "existing test branch has no .publication.json ownership marker"
                    )
                _validate_bootstrap_branch(worktree)
            progress["existing_publication"] = existing is not None
        release_name = _string(publication.get("version_name"), label="publication version")
        commit_subject = _string(
            publication.get("commit_subject"), label="publication commit subject"
        )
        with _progress_stage("stage-changes", branch=branch) as progress:
            _clear_worktree(worktree)
            _copy_tree(projected_tree, worktree)
            _run_git(worktree, "add", "--all")
            difference = _run_git(worktree, "diff", "--cached", "--quiet", check=False)
            if difference.returncode not in {0, 1}:
                raise PublicationError(
                    f"could not compare projected data tree: {difference.stderr}"
                )
            changed_files = (
                _run_git(
                    worktree,
                    "diff",
                    "--cached",
                    "--name-only",
                    "-z",
                ).stdout.rstrip("\0").split("\0")
                if difference.returncode == 1
                else []
            )
            progress.update(changed=difference.returncode == 1, files=len(changed_files))
        same_version = existing is not None and existing.get("version_name") == release_name
        if same_version:
            data_difference = _run_git(
                worktree,
                "diff",
                "--cached",
                "--quiet",
                "--",
                ".",
                ":(exclude)README.md",
                ":(exclude).version_name",
                ":(exclude).publication.json",
                check=False,
            )
            if data_difference.returncode not in {0, 1}:
                raise PublicationError(
                    f"could not compare projected publication data: {data_difference.stderr}"
                )
            if data_difference.returncode == 0:
                commit_sha = _run_git(worktree, "rev-parse", "HEAD").stdout.strip()
                _progress(
                    "publication",
                    "completed",
                    result="unchanged",
                    commit=commit_sha[:12],
                )
                return {
                    **publication,
                    "commit_sha": commit_sha,
                    "publication_state": "unchanged",
                }
        if difference.returncode == 0:
            commit_sha = _run_git(worktree, "rev-parse", "HEAD").stdout.strip()
            _progress(
                "publication",
                "completed",
                result="unchanged",
                commit=commit_sha[:12],
            )
            return {
                **publication,
                "commit_sha": commit_sha,
                "publication_state": "unchanged",
            }
        with _progress_stage("commit", files=len(changed_files)) as progress:
            _run_git(worktree, "commit", "--message", commit_subject)
            commit_sha = _run_git(worktree, "rev-parse", "HEAD").stdout.strip()
            progress["commit"] = commit_sha[:12]
            progress.update(_git_object_stats(worktree))
        with _prestage_large_git_objects(
            repository,
            worktree,
            staging_worktree,
            branch=branch,
            commit_sha=commit_sha,
            changed_files=changed_files,
        ) as staged_objects:
            if staged_objects is not None:
                try:
                    commit_sha = _publish_large_commit_via_github_api(
                        worktree,
                        branch=branch,
                        branch_exists=branch_exists,
                        commit_sha=commit_sha,
                        tree_sha=staged_objects.tree_sha,
                    )
                except Exception:
                    _progress("github-finalize", "failed", branch=branch)
                    raise
            else:
                _push_commit(
                    worktree,
                    remote_ref,
                    commit_sha,
                )
        _progress(
            "publication",
            "completed",
            result="published",
            commit=commit_sha[:12],
        )
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
