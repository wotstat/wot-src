from __future__ import annotations

import subprocess
import time
from pathlib import Path
from typing import Any

import pytest

import wot_src_publisher.publication as publication


def git(repository: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repository), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


@pytest.mark.parametrize("failure_point", ["before_commit", "after_commit"])
def test_publication_survives_transient_commit_failure_without_duplicate_commit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure_point: str
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()
    git(repository, "init")
    git(repository, "config", "user.name", "Test")
    git(repository, "config", "user.email", "test@example.test")
    (repository / "old.txt").write_text("before")
    git(repository, "add", ".")
    git(repository, "commit", "-m", "base")
    parent = git(repository, "rev-parse", "HEAD")

    # Use the real publication entry point, replacing only snapshot projection.
    def project(_snapshot: Path, output: Path, **_kwargs: Any) -> dict[str, Any]:
        output.mkdir()
        (output / "new.txt").write_text("after")
        return {"branch": "test", "version_name": "release", "commit_subject": "publication"}

    monkeypatch.setattr(publication, "_project_snapshot", project)
    monkeypatch.setattr(publication, "_existing_publication", lambda *_: {"version_name": "old"})
    # Model an existing remote branch using a real local bare repository.
    remote = tmp_path / "remote.git"
    git(tmp_path, "init", "--bare", str(remote))
    git(repository, "remote", "add", "origin", str(remote))
    git(repository, "push", "origin", "HEAD:refs/heads/test")
    monkeypatch.setattr(publication, "_probe_github_transport", lambda: None)
    real_run = subprocess.run
    calls = 0
    sleeps: list[float] = []

    def run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        if command[0] == "git" and command[3] == "commit":
            calls += 1
            if calls == 1:
                if failure_point == "after_commit":
                    result = real_run(command, **kwargs)
                    assert result.returncode == 0, result.stderr
                return subprocess.CompletedProcess(
                    command,
                    128,
                    "",
                    "fatal: Failed to connect "
                    "to github.com port 443: Couldn't connect to server\nfatal: could not fetch "
                    + "a" * 40
                    + " from promisor remote",
                )
        return real_run(command, **kwargs)

    monkeypatch.setattr(subprocess, "run", run)
    monkeypatch.setattr(time, "sleep", sleeps.append)
    result = publication.publish_snapshot(
        repository,
        tmp_path / "snapshot",
        target="test",
        expected_snapshot_id="snapshot",
        expected_descriptor_sha256="digest",
        config_path=tmp_path / "config",
    )
    commit = git(remote, "rev-parse", "refs/heads/test")
    assert result["commit_sha"] == commit
    assert git(remote, "rev-parse", f"{commit}^") == parent
    assert git(remote, "show", f"{commit}:new.txt") == "after"
    assert git(remote, "ls-tree", "--name-only", commit) == "new.txt"
    assert calls == (2 if failure_point == "before_commit" else 1)
    assert sleeps == ([5.0] if failure_point == "before_commit" else [])


def prepare_repository(tmp_path: Path, *, unborn: bool = False) -> Path:
    repository = tmp_path / "repository"
    repository.mkdir()
    git(repository, "init")
    git(repository, "config", "user.name", "Test")
    git(repository, "config", "user.email", "test@example.test")
    if not unborn:
        (repository / "data.txt").write_text("before")
        git(repository, "add", ".")
        git(repository, "commit", "-m", "base")
    (repository / "data.txt").write_text("after")
    git(repository, "add", ".")
    return repository


@pytest.mark.parametrize("unborn", [False, True])
def test_commit_recovery_preserves_first_publication_and_parent(
    tmp_path: Path, unborn: bool
) -> None:
    repository = prepare_repository(tmp_path, unborn=unborn)
    expected_tree = git(repository, "write-tree")
    commit = publication._commit_with_recovery(repository, "publication")
    assert git(repository, "rev-parse", f"{commit}^{{tree}}") == expected_tree
    assert git(repository, "rev-list", "--count", "HEAD") == ("1" if unborn else "2")


@pytest.mark.parametrize(
    ("failure", "expected_calls"),
    [
        ("network", 3),
        ("authentication", 1),
        ("index_changed", 1),
        ("wrong_tree", 1),
        ("wrong_parent", 1),
        ("wrong_message", 1),
    ],
)
def test_commit_failure_never_accepts_unexpected_state(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure: str, expected_calls: int
) -> None:
    repository = prepare_repository(tmp_path)
    real_run = subprocess.run
    calls = 0
    monkeypatch.setattr(publication, "_probe_github_transport", lambda: None)
    monkeypatch.setattr(time, "sleep", lambda _: None)

    def run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        if command[0] == "git" and command[3] == "commit":
            calls += 1
            if failure in {"wrong_tree", "index_changed"}:
                (repository / "data.txt").write_text("unexpected")
                git(repository, "add", ".")
            if failure.startswith("wrong_"):
                changed = command.copy()
                if failure == "wrong_message":
                    changed[-1] = "unexpected"
                if failure == "wrong_parent":
                    changed.insert(4, "--amend")
                result = real_run(changed, **kwargs)
                assert result.returncode == 0
            details = "Failed to connect to github.com"
            if failure == "authentication":
                details = "Authentication failed"
            return subprocess.CompletedProcess(command, 128, "", details)
        return real_run(command, **kwargs)

    monkeypatch.setattr(subprocess, "run", run)
    with pytest.raises(publication.PublicationError):
        publication._commit_with_recovery(repository, "publication")
    assert calls == expected_calls


def test_real_partial_clone_recovers_when_commit_summary_cannot_fetch_old_blob(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    import threading
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    origin = prepare_repository(tmp_path)
    git(origin, "config", "uploadpack.allowFilter", "true")
    repository = tmp_path / "partial"
    git(tmp_path, "clone", "--filter=tree:0", "--no-checkout", origin.as_uri(), str(repository))
    git(repository, "config", "user.name", "Test")
    git(repository, "config", "user.email", "test@example.test")
    (repository / "new.txt").write_text("new payload\n" * 100)
    git(repository, "add", "--all")
    git(repository, "diff", "--cached", "--name-only", "--no-renames")
    parent = git(repository, "rev-parse", "HEAD")
    expected_tree = git(repository, "write-tree")
    requests = 0

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            nonlocal requests
            requests += 1
            self.send_response(503)
            self.end_headers()

        def log_message(self, format: str, *args: object) -> None:
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    git(repository, "remote", "set-url", "origin", f"http://127.0.0.1:{server.server_port}/repo")
    monkeypatch.setattr(publication, "_probe_github_transport", lambda: None)
    monkeypatch.setattr(time, "sleep", lambda _: None)
    try:
        commit = publication._commit_with_recovery(repository, "publication")
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    assert requests > 0  # Real Git tried and failed to fetch; no fake commit result.
    assert git(repository, "rev-parse", f"{commit}^") == parent
    assert git(repository, "rev-parse", f"{commit}^{{tree}}") == expected_tree
    assert git(repository, "show", "HEAD:new.txt") == ("new payload\n" * 100).strip()
    assert git(repository, "rev-list", "--count", "HEAD") == "2"
    logs = capsys.readouterr().err
    assert 'reason="http_5xx"' in logs
    assert "promisor_fetch=true" in logs
    assert 'result="recovered_after_transport_error"' in logs
    assert "tree_verified=true" in logs


def test_staging_commit_recovers_after_transport_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository = prepare_repository(tmp_path)
    git(repository, "commit", "-m", "publication")
    commit = git(repository, "rev-parse", "HEAD")
    expected_tree = git(repository, "rev-parse", "HEAD^{tree}")
    monkeypatch.setattr(publication, "OBJECT_STAGING_THRESHOLD_BYTES", 0)
    monkeypatch.setattr(publication, "_push_commit", lambda *_: None)
    monkeypatch.setattr(publication, "_delete_remote_ref", lambda *_: None)
    monkeypatch.setattr(publication, "_probe_github_transport", lambda: None)
    real_run = subprocess.run
    calls = 0

    def run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        result = real_run(command, **kwargs)
        if command[0] == "git" and command[3] == "commit":
            calls += 1
            assert result.returncode == 0
            return subprocess.CompletedProcess(command, 128, "", "Failed to connect to github.com")
        return result

    monkeypatch.setattr(subprocess, "run", run)
    with publication._prestage_large_git_objects(
        repository,
        repository,
        tmp_path / "staging",
        branch="test",
        commit_sha=commit,
        changed_files=("data.txt",),
    ) as staged:
        assert staged is not None
        assert staged.tree_sha == expected_tree
    assert calls == 1
