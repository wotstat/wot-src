from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from snapshot_fixture import create_snapshot

from wot_src_publisher.publication import render_bootstrap_readme

ROOT = Path(__file__).parents[1]


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
    _git("init", "--initial-branch=main", str(repository))
    _git("config", "user.name", "fixture", cwd=repository)
    _git("config", "user.email", "fixture@example.invalid", cwd=repository)
    (repository / "README.md").write_text("service branch\n")
    _git("add", "README.md", cwd=repository)
    _git("commit", "-m", "service", cwd=repository)
    _git("remote", "add", "origin", str(remote), cwd=repository)
    _git("push", "-u", "origin", "main", cwd=repository)
    return repository, remote


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
    ) == "2.3.1.5400"
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


def test_publish_continues_a_valid_production_init_branch(tmp_path: Path) -> None:
    repository, remote = _service_repository(tmp_path)
    _git("switch", "--orphan", "wot-eu", cwd=repository)
    (repository / "README.md").write_text(render_bootstrap_readme())
    _git("add", "README.md", cwd=repository)
    _git("commit", "--message", "init", cwd=repository)
    _git("push", "origin", "wot-eu", cwd=repository)
    _git("switch", "main", cwd=repository)

    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        build_profile="full",
        release_name="2.3.1.5400",
        base_files={
            "res/gui/gameface/index.html": b"<html></html>\n",
            "res/scripts/client/App.py": b"SOURCE = 'base'\n",
        },
        locale_files={"EN": {"res/scripts/client/App.py": b"SOURCE = 'english'\n"}},
        actionscript_files={"base_app/scripts/App.as": b"package {}\n"},
        stub_files={"BigWorld.pyi": b"class Player: ...\n"},
    )

    result = _publish(
        repository,
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
    ).splitlines() == ["2.3.1.5400", "init"]

    data_checkout = tmp_path / "production-checkout"
    _git("clone", "--branch", "wot-eu", str(remote), str(data_checkout))
    assert (data_checkout / ".publication.json").is_file()
    assert "Версия: `2.3.1.5400`" in (data_checkout / "README.md").read_text()
