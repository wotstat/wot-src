from __future__ import annotations

import subprocess
from typing import Any

import pytest

import wot_src_publisher.publication as publication


@pytest.mark.parametrize(
    ("output", "exit_code", "expected"),
    [
        ("200 192.0.2.1 0.01 0.02 0.03 0.04", 0, 'remote_ip="192.0.2.1"'),
        ("000  0.01 0.00 0.00 5.00", 28, "exit_code=28"),
        ("000  0.00 0.00 0.00 0.01", 6, "exit_code=6"),
        ("secret invalid output", 1, "exit_code=1"),
    ],
)
def test_probe_logs_only_safe_metrics(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    output: str,
    exit_code: int,
    expected: str,
) -> None:
    def run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        assert command[:2] == ["curl", "--disable"]
        assert command[-1] == "https://github.com/"
        assert "--header" not in command
        assert "--verbose" not in command
        assert kwargs["timeout"] == 12
        return subprocess.CompletedProcess(command, exit_code, output, "Authorization: secret")

    monkeypatch.setattr(subprocess, "run", run)
    publication._probe_github_transport()
    logs = capsys.readouterr().err
    assert expected in logs
    assert "secret" not in logs
    assert "Authorization" not in logs


@pytest.mark.parametrize("error", [OSError("secret"), subprocess.TimeoutExpired("curl", 12)])
def test_diagnostics_failure_does_not_interrupt_recovery(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], error: Exception
) -> None:
    def run(*args: Any, **kwargs: Any) -> None:
        raise error

    monkeypatch.setattr(subprocess, "run", run)
    publication._probe_github_transport()
    assert (
        capsys.readouterr().err.strip() == "publisher stage=github-connectivity status=unavailable"
    )


def test_git_diagnostics_do_not_expose_error_text() -> None:
    fields = publication._git_failure_fields(
        "fatal: unable to access https://secret@github.com/private: Failed to connect "
        "to github.com port 443 after 135401 ms: Couldn't connect to server\n"
        "fatal: could not fetch " + "a" * 40 + " from promisor remote"
    )
    assert fields == {"reason": "connect", "promisor_fetch": True, "missing_object": "a" * 40}
    assert "secret" not in str(fields)
