from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from snapshot_fixture import create_snapshot

import wot_src_publisher.publication as publication_module

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
            "--expected-snapshot-id",
            snapshot_id,
            "--expected-descriptor-sha256",
            descriptor_sha256,
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
    created_at: str = "2026-08-24T00:00:00Z",
    source_payload: bytes = b"SOURCE = 'english'\n",
    tool_version: str = "1",
) -> tuple[str, str]:
    return create_snapshot(
        root,
        target="wot-eu",
        publisher="wargaming",
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


@pytest.mark.parametrize("branch_exists", [False, True])
def test_large_publication_prestages_blobs_and_removes_temporary_ref(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    branch_exists: bool,
) -> None:
    repository, remote = _service_repository(tmp_path)
    branch = "wot-eu"
    if branch_exists:
        _git("switch", "--orphan", branch, cwd=repository)
        (repository / "README.md").write_text("owned data branch\n")
        (repository / ".publication.json").write_text(
            json.dumps({"version_name": "previous"})
        )
        _git("add", "README.md", ".publication.json", cwd=repository)
        _git("commit", "--message", "init", cwd=repository)
        _git("push", "origin", branch, cwd=repository)
        _git("switch", "main", cwd=repository)
    incoming_push_sizes = _record_incoming_push_sizes(remote)
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = _snapshot(
        snapshot,
        created_at="2026-08-24T01:00:00Z" if branch_exists else "2026-08-24T00:00:00Z",
        source_payload=(
            b"SOURCE = 'updated'\n" if branch_exists else b"SOURCE = 'english'\n"
        ),
        tool_version="2" if branch_exists else "1",
    )
    monkeypatch.setattr(publication_module, "OBJECT_STAGING_THRESHOLD_BYTES", 1)
    monkeypatch.setattr(publication_module, "OBJECT_STAGING_BATCH_BYTES", 3_500)
    streamed_git_calls: list[tuple[str, ...]] = []
    github_finalize_calls: list[tuple[str, bool, str, str]] = []
    original_run_git_streaming = publication_module._run_git_streaming

    def record_streamed_git(worktree: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        streamed_git_calls.append(arguments)
        return original_run_git_streaming(worktree, *arguments)

    monkeypatch.setattr(publication_module, "_run_git_streaming", record_streamed_git)

    def fake_github_finalize(
        worktree: Path,
        *,
        branch: str,
        branch_exists: bool,
        commit_sha: str,
        tree_sha: str,
    ) -> str:
        github_finalize_calls.append((branch, branch_exists, commit_sha, tree_sha))
        assert tree_sha == _git("rev-parse", f"{commit_sha}^{{tree}}", cwd=worktree)
        _git("--git-dir", str(remote), "fetch", str(worktree), commit_sha)
        ref = f"refs/heads/{branch}"
        if branch_exists:
            old_commit = _git("--git-dir", str(remote), "rev-parse", ref)
            _git("--git-dir", str(remote), "update-ref", ref, commit_sha, old_commit)
        else:
            _git("--git-dir", str(remote), "update-ref", ref, commit_sha)
        return commit_sha

    monkeypatch.setattr(
        publication_module,
        "_publish_large_commit_via_github_api",
        fake_github_finalize,
    )

    result = publication_module.publish_snapshot(
        repository,
        snapshot,
        target="wot-eu",
        expected_snapshot_id=snapshot_id,
        expected_descriptor_sha256=descriptor_sha256,
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
    assert len(github_finalize_calls) == 1
    assert github_finalize_calls[0][0:2] == (branch, branch_exists)
    production_pushes = [
        arguments
        for arguments in streamed_git_calls
        if arguments[-1] == f"HEAD:refs/heads/{branch}"
    ]
    assert production_pushes == []
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
    assert staging_sizes
    assert all(ref != f"refs/heads/{branch}" for ref, _size in recorded_sizes)
    subjects = _git(
        "--git-dir",
        str(remote),
        "log",
        "--format=%s",
        f"refs/heads/{branch}",
    ).splitlines()
    assert subjects[0] == "2.3.1.0 #903"
    assert not any(subject.startswith("stage publication objects ") for subject in subjects)
    assert subjects == (
        ["2.3.1.0 #903", "init"]
        if branch_exists
        else ["2.3.1.0 #903"]
    )


def test_github_api_finalization_creates_commit_and_fast_forward_ref(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    repository, _remote = _service_repository(tmp_path)
    parent = _git("rev-parse", "HEAD", cwd=repository)
    (repository / "README.md").unlink()
    (repository / "a.txt").write_text("a")
    (repository / "b.txt").write_text("b")
    _git("add", "--all", cwd=repository)
    _git("commit", "--message", "publication", cwd=repository)
    commit_sha = _git("rev-parse", "HEAD", cwd=repository)
    expected_tree = _git("rev-parse", "HEAD^{tree}", cwd=repository)
    monkeypatch.setenv("PUBLISHER_GITHUB_REPOSITORY", "wotstat/wot-src")
    monkeypatch.setenv("PUBLISHER_GITHUB_TOKEN", "test-token")
    calls: list[tuple[str, str, dict[str, object] | None]] = []

    def fake_api_request(
        api_repository: str,
        token: str,
        method: str,
        path: str,
        payload: dict[str, object] | None = None,
        **_kwargs: object,
    ) -> dict[str, object]:
        assert api_repository == "wotstat/wot-src"
        assert token == "test-token"
        calls.append((method, path, payload))
        if path == "git/commits":
            return {"sha": commit_sha}
        return {"object": {"sha": commit_sha}}

    monkeypatch.setattr(publication_module, "_github_api_request", fake_api_request)

    result = publication_module._publish_large_commit_via_github_api(
        repository,
        branch="wot-eu",
        branch_exists=True,
        commit_sha=commit_sha,
        tree_sha=expected_tree,
    )

    assert result == commit_sha
    commit_call = calls[0]
    assert commit_call[0:2] == ("POST", "git/commits")
    assert commit_call[2] is not None
    assert commit_call[2]["tree"] == expected_tree
    assert commit_call[2]["parents"] == [parent]
    assert calls[1] == (
        "PATCH",
        "git/refs/heads/wot-eu",
        {"sha": commit_sha, "force": False},
    )


def test_publish_creates_orphan_data_branch_and_is_idempotent(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
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
        "refs/heads/wot-eu",
    ) == "1"
    assert _git(
        "--git-dir",
        str(remote),
        "log",
        "-1",
        "--format=%s",
        "refs/heads/wot-eu",
    ) == "2.3.1.0 #903"
    assert _git(
        "--git-dir",
        str(remote),
        "rev-list",
        "--max-parents=0",
        "refs/heads/wot-eu",
    ) == first_result["commit_sha"]

    data_checkout = tmp_path / "data-checkout"
    _git("clone", "--branch", "wot-eu", str(remote), str(data_checkout))
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
        "refs/heads/wot-eu",
    ) == "1"


def test_rebuilt_same_version_with_identical_data_is_unchanged(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    first_snapshot = tmp_path / "first-snapshot"
    first_id, first_descriptor = _snapshot(
        first_snapshot,
        created_at="2026-08-24T00:00:00Z",
    )
    second_snapshot = tmp_path / "second-snapshot"
    second_id, second_descriptor = _snapshot(
        second_snapshot,
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
        "refs/heads/wot-eu",
    ) == "1"
    stored = json.loads(
        _git(
            "--git-dir",
            str(remote),
            "show",
            "refs/heads/wot-eu:.publication.json",
        )
    )
    assert stored["descriptor_sha256"] == first_descriptor


def test_same_version_with_changed_data_creates_another_commit(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    first_snapshot = tmp_path / "first-snapshot"
    first_id, first_descriptor = _snapshot(
        first_snapshot,
        source_payload=b"SOURCE = 'first'\n",
    )
    second_snapshot = tmp_path / "second-snapshot"
    second_id, second_descriptor = _snapshot(
        second_snapshot,
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
        "refs/heads/wot-eu",
    ) == "2"
    assert _git(
        "--git-dir",
        str(remote),
        "log",
        "--format=%s",
        "refs/heads/wot-eu",
    ).splitlines() == ["2.3.1.0 #903", "2.3.1.0 #903"]
    assert _git(
        "--git-dir",
        str(remote),
        "show",
        "refs/heads/wot-eu:sources/res/scripts/client/App.py",
    ) == "SOURCE = 'updated'"
    stored = json.loads(
        _git(
            "--git-dir",
            str(remote),
            "show",
            "refs/heads/wot-eu:.publication.json",
        )
    )
    assert stored["descriptor_sha256"] == second_descriptor


def test_publish_rejects_existing_branch_without_ownership_marker(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    _git("switch", "--orphan", "wot-eu", cwd=repository)
    (repository / "README.md").write_text("unowned data branch\n")
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
    )

    assert result.returncode == 1
    assert "no .publication.json ownership marker" in result.stderr
    assert _git(
        "--git-dir", str(remote), "rev-list", "--count", "refs/heads/wot-eu"
    ) == "1"
    assert _git(
        "--git-dir", str(remote), "log", "--format=%s", "refs/heads/wot-eu"
    ).splitlines() == ["init"]


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
