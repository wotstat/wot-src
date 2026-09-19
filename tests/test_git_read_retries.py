from __future__ import annotations

import subprocess
import time
from pathlib import Path
from typing import Any

import pytest

import wot_src_publisher.publication as publication


@pytest.mark.parametrize("failed_command", ["ls-tree", "show"])
def test_existing_publication_recovers_from_promisor_network_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failed_command: str
) -> None:
    def git(*args: str) -> None:
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)

    git("init")
    git("config", "user.name", "Test")
    git("config", "user.email", "test@example.test")
    (tmp_path / ".publication.json").write_text('{"schema_version": 1}')
    git("add", ".publication.json")
    git("commit", "-m", "Publication")
    monkeypatch.setattr(publication, "_probe_github_transport", lambda: None)
    real_run = subprocess.run
    failures = 0
    sleeps: list[float] = []

    def run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        nonlocal failures
        if command[3] == failed_command and failures == 0:
            failures += 1
            return subprocess.CompletedProcess(
                command,
                128,
                "",
                "fatal: Failed to connect to github.com port 443: "
                "Couldn't connect to server\nfatal: could not fetch object from promisor remote",
            )
        return real_run(command, **kwargs)

    monkeypatch.setattr(subprocess, "run", run)
    monkeypatch.setattr(time, "sleep", sleeps.append)
    assert publication._existing_publication(tmp_path) == {"schema_version": 1}
    assert failures == 1
    assert sleeps == [5.0]


@pytest.mark.parametrize(
    ("command", "error", "attempts"),
    [
        ("ls-tree", "Failed to connect to github.com", 3),
        ("ls-tree", "fatal: bad object HEAD", 1),
        ("ls-tree", "fatal: Authentication failed", 1),
        ("commit", "Failed to connect to github.com", 1),
        ("fetch", "Failed to connect to github.com", 3),
        ("ls-remote", "Failed to connect to github.com", 3),
    ],
)
def test_git_retries_are_bounded_and_only_for_safe_transient_failures(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, command: str, error: str, attempts: int
) -> None:
    monkeypatch.setattr(publication, "_probe_github_transport", lambda: None)
    calls = 0
    sleeps: list[float] = []

    def run(args: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        calls += 1
        return subprocess.CompletedProcess(args, 128, "", error)

    monkeypatch.setattr(subprocess, "run", run)
    monkeypatch.setattr(time, "sleep", sleeps.append)
    with pytest.raises(publication.PublicationError, match=error):
        publication._run_git(tmp_path, command)
    assert calls == attempts
    assert len(sleeps) == attempts - 1
