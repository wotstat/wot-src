from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from snapshot_fixture import create_snapshot

import wot_src_publisher.publication as publication_module
from wot_src_publisher.publication import render_bootstrap_readme

ROOT = Path(__file__).parents[1]
VERSION_XML = b"""<version.xml>
  <version> v.2.3.1.0 #903 </version>
</version.xml>
"""


def _git(*arguments: str, cwd: Path | None = None) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def _service_repository(tmp_path: Path) -> tuple[Path, Path]:
    remote = tmp_path / "remote.git"
    repository = tmp_path / "service"
    _git("init", "--bare", "--initial-branch=main", str(remote))
    _git("--git-dir", str(remote), "config", "uploadpack.allowFilter", "true")
    _git("--git-dir", str(remote), "config", "uploadpack.allowAnySHA1InWant", "true")
    _git("init", "--initial-branch=main", str(repository))
    _git("config", "user.name", "fixture", cwd=repository)
    _git("config", "user.email", "fixture@example.invalid", cwd=repository)
    (repository / "README.md").write_text("service branch\n")
    _git("add", "README.md", cwd=repository)
    _git("commit", "-m", "service", cwd=repository)
    _git("remote", "add", "origin", str(remote), cwd=repository)
    _git("push", "-u", "origin", "main", cwd=repository)
    return repository, remote


def _record_incoming_push_sizes(remote: Path) -> Path:
    log_path = remote / "incoming-push-sizes"
    hook = remote / "hooks/pre-receive"
    hook.write_text(
        """#!/usr/bin/env python3
import os
import sys
from pathlib import Path

object_directory_value = os.environ.get("GIT_OBJECT_DIRECTORY")
object_directory = Path(object_directory_value) if object_directory_value else None
incoming_bytes = (
    sum(path.stat().st_size for path in object_directory.rglob("*") if path.is_file())
    if object_directory is not None
    else 0
)
git_directory = Path(os.environ.get("GIT_DIR", "."))
with (git_directory / "incoming-push-sizes").open("a", encoding="utf-8") as log:
    for line in sys.stdin:
        _old, _new, ref = line.split()
        log.write(f"{ref} {incoming_bytes}\\n")
""",
        encoding="utf-8",
    )
    hook.chmod(0o755)
    return log_path


def _publish(
    repository: Path,
    snapshot: Path,
    *,
    snapshot_id: str,
    descriptor_sha256: str,
    branch: str = "test/light-wot-eu",
    profile: str = "light",
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "wot_src_publisher",
            "publish",
            "--repository",
            str(repository),
            "--snapshot",
            str(snapshot),
            "--target",
            "wot-eu",
            "--branch",
            branch,
            "--expected-snapshot-id",
            snapshot_id,
            "--expected-descriptor-sha256",
            descriptor_sha256,
            "--expected-profile",
            profile,
        ],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )


def _snapshot(
    root: Path,
    *,
    profile: str,
    created_at: str = "2026-08-24T00:00:00Z",
    source_payload: bytes = b"SOURCE = 'english'\n",
    tool_version: str = "1",
) -> tuple[str, str]:
    return create_snapshot(
        root,
        target="wot-eu",
        publisher="wargaming",
        build_profile=profile,
        release_name="2.3.1.5400",
        base_files={
            "version.xml": VERSION_XML,
            "res/gui/gameface/index.html": b"<html></html>\n",
            "res/scripts/client/App.py": b"SOURCE = 'base'\n",
        },
        locale_files={"EN": {"res/scripts/client/App.py": source_payload}},
        actionscript_files={"base_app/scripts/App.as": b"package {}\n"},
        stub_files={"BigWorld.pyi": b"class Player: ...\n"},
        created_at=created_at,
        tool_version=tool_version,
    )


def test_partitions_changed_blobs_below_the_push_budget() -> None:
    blobs = (
        publication_module._GitBlob("a", "100644", "a" * 40, 60),
        publication_module._GitBlob("b", "100644", "b" * 40, 40),
        publication_module._GitBlob("c", "100644", "c" * 40, 70),
    )

    batches = publication_module._partition_git_blobs(blobs, max_batch_bytes=100)

    assert [[blob.path for blob in batch] for batch in batches] == [["a", "b"], ["c"]]
    assert all(sum(blob.size for blob in batch) <= 100 for batch in batches)


@pytest.mark.parametrize(
    ("branch", "profile", "bootstrap"),
    [
        ("test/light-wot-eu", "light", False),
        ("wot-eu", "full", True),
    ],
)
def test_large_publication_prestages_blobs_and_removes_temporary_ref(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    branch: str,
    profile: str,
    bootstrap: bool,
) -> None:
    repository, remote = _service_repository(tmp_path)
    if bootstrap:
        _git("switch", "--orphan", branch, cwd=repository)
        (repository / "README.md").write_text(render_bootstrap_readme())
        _git("add", "README.md", cwd=repository)
        _git("commit", "--message", "init", cwd=repository)
        _git("push", "origin", branch, cwd=repository)
        _git("switch", "main", cwd=repository)
    incoming_push_sizes = _record_incoming_push_sizes(remote)
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = _snapshot(snapshot, profile=profile)
    monkeypatch.setattr(publication_module, "OBJECT_STAGING_THRESHOLD_BYTES", 1)
    monkeypatch.setattr(publication_module, "OBJECT_STAGING_BATCH_BYTES", 3_500)
    streamed_git_calls: list[tuple[str, ...]] = []
    original_run_git_streaming = publication_module._run_git_streaming

    def record_streamed_git(worktree: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        streamed_git_calls.append(arguments)
        return original_run_git_streaming(worktree, *arguments)

    monkeypatch.setattr(publication_module, "_run_git_streaming", record_streamed_git)

    result = publication_module.publish_snapshot(
        repository,
        snapshot,
        target="wot-eu",
        branch=branch,
        expected_snapshot_id=snapshot_id,
        expected_descriptor_sha256=descriptor_sha256,
        expected_profile=profile,
        config_path=ROOT / "config/targets.json",
    )

    assert result["publication_state"] == "published"
    assert _git(
        "--git-dir", str(remote), "rev-parse", f"refs/heads/{branch}"
    ) == result["commit_sha"]
    assert (
        _git(
            "--git-dir",
            str(remote),
            "for-each-ref",
            "--format=%(refname)",
            "refs/heads/publication-staging",
        )
        == ""
    )
    captured = capsys.readouterr()
    assert "publisher stage=stage-objects status=started" in captured.err
    assert "publisher stage=stage-objects status=batch_completed" in captured.err
    assert "publisher stage=stage-objects status=cleanup_completed" in captured.err
    production_pushes = [
        arguments
        for arguments in streamed_git_calls
        if arguments[-1] == f"HEAD:refs/heads/{branch}"
    ]
    assert len(production_pushes) == 1
    assert production_pushes[0] == (
        "push",
        "--progress",
        "origin",
        f"HEAD:refs/heads/{branch}",
    )
    recorded_sizes = [
        (ref, int(size))
        for ref, size in (
            line.split() for line in incoming_push_sizes.read_text().splitlines()
        )
    ]
    staging_sizes = [
        size
        for ref, size in recorded_sizes
        if ref.startswith("refs/heads/publication-staging/") and size > 0
    ]
    production_sizes = [
        size for ref, size in recorded_sizes if ref == f"refs/heads/{branch}"
    ]
    assert staging_sizes
    assert len(production_sizes) == 1
    assert production_sizes[0] == 0
    subjects = _git(
        "--git-dir",
        str(remote),
        "log",
        "--format=%s",
        f"refs/heads/{branch}",
    ).splitlines()
    assert subjects[0] == "2.3.1.0 #903"
    assert any(subject.startswith("stage publication objects ") for subject in subjects[1:])


def test_publish_creates_orphan_data_branch_and_is_idempotent(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        build_profile="light",
        release_name="2.3.1.5400",
        base_files={
            "version.xml": VERSION_XML,
            "res/gui/gameface/index.html": b"<html></html>\n",
            "res/scripts/client/App.py": b"SOURCE = 'base'\n",
        },
        locale_files={"EN": {"res/scripts/client/App.py": b"SOURCE = 'english'\n"}},
        actionscript_files={"base_app/scripts/App.as": b"package {}\n"},
        stub_files={"BigWorld.pyi": b"class Player: ...\n"},
    )

    first = _publish(
        repository,
        snapshot,
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
    )

    assert first.returncode == 0, first.stderr
    assert "publisher stage=verify status=started" in first.stderr
    assert "publisher stage=push status=completed" in first.stderr
    first_result = json.loads(first.stdout)
    assert first_result["publication_state"] == "published"
    assert _git(
        "--git-dir",
        str(remote),
        "rev-list",
        "--count",
        "refs/heads/test/light-wot-eu",
    ) == "1"
    assert _git(
        "--git-dir",
        str(remote),
        "log",
        "-1",
        "--format=%s",
        "refs/heads/test/light-wot-eu",
    ) == "2.3.1.0 #903"
    assert _git(
        "--git-dir",
        str(remote),
        "rev-list",
        "--max-parents=0",
        "refs/heads/test/light-wot-eu",
    ) == first_result["commit_sha"]

    data_checkout = tmp_path / "data-checkout"
    _git("clone", "--branch", "test/light-wot-eu", str(remote), str(data_checkout))
    assert (data_checkout / "README.md").is_file()
    assert "https://github.com/wotstat/wot-src/tree/wot-na" in (
        data_checkout / "README.md"
    ).read_text()
    assert not (data_checkout / "pyproject.toml").exists()
    assert (data_checkout / "sources/res/scripts/client/App.py").read_bytes() == (
        b"SOURCE = 'english'\n"
    )

    second = _publish(
        repository,
        snapshot,
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
    )

    assert second.returncode == 0, second.stderr
    assert json.loads(second.stdout)["publication_state"] == "unchanged"
    assert _git(
        "--git-dir",
        str(remote),
        "rev-list",
        "--count",
        "refs/heads/test/light-wot-eu",
    ) == "1"


def test_rebuilt_same_version_with_identical_data_is_unchanged(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    first_snapshot = tmp_path / "first-snapshot"
    first_id, first_descriptor = _snapshot(
        first_snapshot,
        profile="light",
        created_at="2026-08-24T00:00:00Z",
    )
    second_snapshot = tmp_path / "second-snapshot"
    second_id, second_descriptor = _snapshot(
        second_snapshot,
        profile="light",
        created_at="2026-08-24T01:00:00Z",
        tool_version="2",
    )
    assert second_id != first_id
    assert second_descriptor != first_descriptor

    first = _publish(
        repository,
        first_snapshot,
        snapshot_id=first_id,
        descriptor_sha256=first_descriptor,
    )
    second = _publish(
        repository,
        second_snapshot,
        snapshot_id=second_id,
        descriptor_sha256=second_descriptor,
    )

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert json.loads(second.stdout)["publication_state"] == "unchanged"
    assert _git(
        "--git-dir",
        str(remote),
        "rev-list",
        "--count",
        "refs/heads/test/light-wot-eu",
    ) == "1"
    stored = json.loads(
        _git(
            "--git-dir",
            str(remote),
            "show",
            "refs/heads/test/light-wot-eu:.publication.json",
        )
    )
    assert stored["descriptor_sha256"] == first_descriptor


def test_same_version_with_changed_data_creates_another_commit(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    first_snapshot = tmp_path / "first-snapshot"
    first_id, first_descriptor = _snapshot(
        first_snapshot,
        profile="light",
        source_payload=b"SOURCE = 'first'\n",
    )
    second_snapshot = tmp_path / "second-snapshot"
    second_id, second_descriptor = _snapshot(
        second_snapshot,
        profile="light",
        created_at="2026-08-24T01:00:00Z",
        source_payload=b"SOURCE = 'updated'\n",
        tool_version="2",
    )
    assert second_id != first_id

    first = _publish(
        repository,
        first_snapshot,
        snapshot_id=first_id,
        descriptor_sha256=first_descriptor,
    )
    second = _publish(
        repository,
        second_snapshot,
        snapshot_id=second_id,
        descriptor_sha256=second_descriptor,
    )

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert json.loads(second.stdout)["publication_state"] == "published"
    assert _git(
        "--git-dir",
        str(remote),
        "rev-list",
        "--count",
        "refs/heads/test/light-wot-eu",
    ) == "2"
    assert _git(
        "--git-dir",
        str(remote),
        "log",
        "--format=%s",
        "refs/heads/test/light-wot-eu",
    ).splitlines() == ["2.3.1.0 #903", "2.3.1.0 #903"]
    assert _git(
        "--git-dir",
        str(remote),
        "show",
        "refs/heads/test/light-wot-eu:sources/res/scripts/client/App.py",
    ) == "SOURCE = 'updated'"
    stored = json.loads(
        _git(
            "--git-dir",
            str(remote),
            "show",
            "refs/heads/test/light-wot-eu:.publication.json",
        )
    )
    assert stored["descriptor_sha256"] == second_descriptor


def _legacy_bootstrap_readme() -> str:
    current = render_bootstrap_readme()
    previous = current.replace(
        "Каждая\nпубликация завершается version commit: его сообщение строится из "  # noqa: RUF001
        "`sources/version.xml` без префикса\n`v.` в формате `2.3.1.0 #903`, а точный release "  # noqa: RUF001
        "name записывается в `.version_name`. Перед version\ncommit большой публикации в истории "
        "могут находиться служебные staging commits.",
        "Каждый\nследующий commit соответствует одной версии клиента: сообщение строится из "  # noqa: RUF001
        "`sources/version.xml`\nбез префикса `v.` в формате `2.3.1.0 #903`, а точный release name "  # noqa: RUF001
        "записывается в `.version_name`.",
    )
    legacy = previous.replace("строится", "берётся").replace(
        "без префикса `v.` в формате `2.3.1.0 #903`",
        "в формате `v.2.3.1.0 #903`",
    )
    assert legacy != previous != current
    return legacy


@pytest.mark.parametrize(
    "bootstrap_readme",
    [render_bootstrap_readme(), _legacy_bootstrap_readme()],
    ids=["current", "legacy"],
)
def test_publish_continues_a_valid_production_init_branch(
    tmp_path: Path,
    bootstrap_readme: str,
) -> None:
    repository, remote = _service_repository(tmp_path)
    _git("switch", "--orphan", "wot-eu", cwd=repository)
    (repository / "README.md").write_text(bootstrap_readme)
    _git("add", "README.md", cwd=repository)
    _git("commit", "--message", "init", cwd=repository)
    _git("push", "origin", "wot-eu", cwd=repository)
    _git("switch", "main", cwd=repository)

    publisher_repository = tmp_path / "fresh-publisher"
    _git(
        "clone",
        "--no-local",
        "--depth",
        "1",
        "--branch",
        "main",
        "--single-branch",
        str(remote),
        str(publisher_repository),
    )
    _git("config", "user.name", "publisher", cwd=publisher_repository)
    _git("config", "user.email", "publisher@example.invalid", cwd=publisher_repository)

    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        build_profile="full",
        release_name="2.3.1.5400",
        base_files={
            "version.xml": VERSION_XML,
            "res/gui/gameface/index.html": b"<html></html>\n",
            "res/scripts/client/App.py": b"SOURCE = 'base'\n",
        },
        locale_files={"EN": {"res/scripts/client/App.py": b"SOURCE = 'english'\n"}},
        actionscript_files={"base_app/scripts/App.as": b"package {}\n"},
        stub_files={"BigWorld.pyi": b"class Player: ...\n"},
    )

    result = _publish(
        publisher_repository,
        snapshot,
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
        branch="wot-eu",
        profile="full",
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["publication_state"] == "published"
    assert _git(
        "--git-dir", str(remote), "rev-list", "--count", "refs/heads/wot-eu"
    ) == "2"
    assert _git(
        "--git-dir", str(remote), "log", "--format=%s", "refs/heads/wot-eu"
    ).splitlines() == ["2.3.1.0 #903", "init"]

    data_checkout = tmp_path / "production-checkout"
    _git("clone", "--branch", "wot-eu", str(remote), str(data_checkout))
    assert (data_checkout / ".publication.json").is_file()
    assert "Версия: `2.3.1.5400`" in (data_checkout / "README.md").read_text()


def test_publisher_uses_a_commit_only_fetch_without_checking_out_old_data() -> None:
    source = (ROOT / "src/wot_src_publisher/publication.py").read_text()

    assert '"--filter=tree:0"' in source
    assert '"--no-checkout"' in source
    assert '"show", "HEAD:.publication.json"' in source


def test_push_retries_a_transient_github_http_500(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    commit_sha = "a" * 40
    push_results = iter(
        (
            subprocess.CompletedProcess(
                ["git", "push"],
                1,
                "",
                "error: RPC failed; HTTP 500\nfatal: the remote end hung up unexpectedly\n",
            ),
            subprocess.CompletedProcess(["git", "push"], 0, "", ""),
        )
    )
    push_attempts = 0

    def fake_streaming_git(
        repository: Path,
        *arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        nonlocal push_attempts
        assert repository == tmp_path
        assert arguments[0] == "push"
        push_attempts += 1
        return next(push_results)

    def fake_run_git(
        repository: Path,
        *arguments: str,
        check: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        assert repository == tmp_path
        assert arguments[:3] == ("ls-remote", "--heads", "origin")
        assert not check
        return subprocess.CompletedProcess(["git", *arguments], 2, "", "")

    monkeypatch.setattr(publication_module, "_run_git_streaming", fake_streaming_git, raising=False)
    monkeypatch.setattr(publication_module, "_run_git", fake_run_git)
    publication_module._push_commit(
        tmp_path,
        "refs/heads/wot-eu",
        commit_sha,
        retry_delays=(0,),
    )

    assert push_attempts == 2
    captured = capsys.readouterr()
    assert "publisher stage=push status=retrying" in captured.err
    assert "publisher stage=push status=completed" in captured.err


def test_push_accepts_a_remote_update_after_the_response_disconnects(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    commit_sha = "b" * 40
    remote_ref = "refs/heads/wot-eu"
    push_attempts = 0

    def fake_streaming_git(
        repository: Path,
        *arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        nonlocal push_attempts
        assert repository == tmp_path
        assert arguments[0] == "push"
        push_attempts += 1
        return subprocess.CompletedProcess(
            ["git", *arguments],
            1,
            "",
            "fatal: the remote end hung up unexpectedly\n",
        )

    def fake_run_git(
        repository: Path,
        *arguments: str,
        check: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        assert repository == tmp_path
        assert not check
        return subprocess.CompletedProcess(
            ["git", *arguments],
            0,
            f"{commit_sha}\t{remote_ref}\n",
            "",
        )

    monkeypatch.setattr(publication_module, "_run_git_streaming", fake_streaming_git)
    monkeypatch.setattr(publication_module, "_run_git", fake_run_git)

    publication_module._push_commit(tmp_path, remote_ref, commit_sha, retry_delays=(0,))

    assert push_attempts == 1
    captured = capsys.readouterr()
    assert 'result="remote_updated_after_transport_error"' in captured.err


def test_push_does_not_retry_githubs_explicit_pack_size_rejection() -> None:
    assert not publication_module._is_retryable_push_failure(
        "remote: fatal: pack exceeds maximum allowed size"
    )
