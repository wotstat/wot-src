from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from snapshot_fixture import create_snapshot

ROOT = Path(__file__).parents[1]
VERSION_XML = b"""<version.xml>
  <version> v.2.3.1.0 #903 </version>
</version.xml>
"""


def _project(
    snapshot: Path,
    output: Path,
    *,
    target: str,
    snapshot_id: str,
    descriptor_sha256: str,
    profile: str = "light",
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "wot_src_publisher",
            "project",
            "--snapshot",
            str(snapshot),
            "--output",
            str(output),
            "--target",
            target,
            "--branch",
            f"test/light-{target}",
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


def test_wargaming_projection_applies_default_locale_and_keeps_all_locales(
    tmp_path: Path,
) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        build_profile="light",
        release_name="2.3.1.5400",
        base_files={
            "Licenses.txt": b"licenses\n",
            "version.xml": VERSION_XML,
            "res/config/base.xml": b"<base/>\n",
            "res/gui/gameface/app.js": b"console.log('base')\n",
            "res/gui/gameface/assets/raw.bin": b"\x00\x01",
            "res/scripts/client/App.py": b"SOURCE = 'base'\n",
            "res/scripts/client/ignored.txt": b"not source\n",
        },
        locale_files={
            "EN": {
                "res/config/base.xml": b"<english/>\n",
                "res/scripts/client/App.py": b"SOURCE = 'english'\n",
                "res/text/messages.po": b"msgid \"hello\"\n",
            },
            "RU": {
                "res/config/base.xml": b"<russian/>\n",
                "res/scripts/client/App.py": b"SOURCE = 'russian'\n",
            },
        },
        actionscript_files={"base_app/scripts/App.as": b"package {}\n"},
        stub_files={
            "BigWorld.pyi": b"def time() -> float: ...\n",
            "manifest.json": b"{}\n",
            "py.typed": b"",
        },
    )
    output = tmp_path / "output"

    result = _project(
        snapshot,
        output,
        target="wot-eu",
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
    )

    assert result.returncode == 0, result.stderr
    assert (output / ".version_name").read_text() == "2.3.1.5400\n"
    readme = (output / "README.md").read_text()
    assert readme.startswith("# wot-src\n")
    for branch in (
        "wot-eu",
        "wot-na",
        "wot-asia",
        "wot-cn",
        "wot-common-test",
        "mt-ru",
        "mt-public-test",
    ):
        assert f"https://github.com/wotstat/wot-src/tree/{branch}" in readme
    assert "## Структура data-ветки" in readme
    assert "Target: `wot-eu`" in readme
    assert "Ветка: `test/light-wot-eu`" in readme
    assert "Версия: `2.3.1.5400`" in readme
    assert "GameSnapshot: `sha256:" in readme
    assert (output / "sources/res/scripts/client/App.py").read_bytes() == (
        b"SOURCE = 'english'\n"
    )
    assert (output / "sources/res/config/base.xml").read_bytes() == b"<english/>\n"
    assert (output / "sources/Licenses.txt").read_bytes() == b"licenses\n"
    assert not (output / "sources/res/scripts/client/ignored.txt").exists()
    assert not (output / "sources/res/gui/gameface").exists()
    assert (output / "locales/EN/res/scripts/client/App.py").is_file()
    assert (output / "locales/EN/res/text/messages.po").is_file()
    assert (output / "locales/RU/res/scripts/client/App.py").is_file()
    assert (output / "sources-gameface/app.js").is_file()
    assert (output / "sources-gameface/assets/raw.bin").read_bytes() == b"\x00\x01"
    assert (output / "sources-as3/base_app/scripts/App.as").is_file()
    assert (output / "stubs/BigWorld.pyi").is_file()
    assert (output / "stubs/manifest.json").is_file()
    assert (output / "stubs/py.typed").is_file()

    publication_text = (output / ".publication.json").read_text()
    assert publication_text.startswith('{\n  "branch": "test/light-wot-eu",\n')
    assert publication_text.endswith("\n")
    publication = json.loads(publication_text)
    assert publication["snapshot_id"] == snapshot_id
    assert publication["descriptor_sha256"] == descriptor_sha256
    assert publication["build_profile"] == "light"
    assert publication["default_locale"] == "EN"
    assert publication["branch"] == "test/light-wot-eu"
    assert publication["commit_subject"] == "v.2.3.1.0 #903"


def test_lesta_projection_uses_base_and_ignores_locale_layers(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="mt-ru",
        publisher="lesta",
        build_profile="light",
        release_name="1.37.0.4001",
        base_files={
            "version.xml": b"""<version.xml>
  <version> v.1.37.0.0 #4001 </version>
</version.xml>
""",
            "res/gui/gameface/index.html": b"<html></html>\n",
            "res/scripts/client/App.py": b"SOURCE = 'lesta-base'\n",
            "res/text/lesta.po": b"msgid \"base\"\n",
        },
        locale_files={
            "RU": {"res/scripts/client/App.py": b"SOURCE = 'must-not-overlay'\n"}
        },
        actionscript_files={"base_app/scripts/App.as": b"package {}\n"},
        stub_files={"BigWorld.pyi": b"class Player: ...\n"},
    )
    output = tmp_path / "output"

    result = _project(
        snapshot,
        output,
        target="mt-ru",
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
    )

    assert result.returncode == 0, result.stderr
    assert (output / "sources/res/scripts/client/App.py").read_bytes() == (
        b"SOURCE = 'lesta-base'\n"
    )
    assert (output / "sources/res/text/lesta.po").is_file()
    assert not (output / "locales").exists()
    readme = (output / "README.md").read_text()
    assert "Target: `mt-ru`" in readme
    assert "У клиентов Lesta отдельного дерева\n`locales/` нет" in readme  # noqa: RUF001
    publication = json.loads((output / ".publication.json").read_text())
    assert publication["publisher"] == "lesta"
    assert "default_locale" not in publication


def test_projection_rejects_profile_mismatch_before_creating_output(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        build_profile="full",
        release_name="2.3.1.5400",
        base_files={"res/gui/gameface/index.html": b"<html></html>\n"},
        locale_files={"EN": {"res/scripts/client/App.py": b"SOURCE = 'english'\n"}},
        actionscript_files={},
        stub_files={},
    )
    output = tmp_path / "output"

    result = _project(
        snapshot,
        output,
        target="wot-eu",
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
        profile="light",
    )

    assert result.returncode == 1
    assert "build profile differs" in result.stderr
    assert not output.exists()


def test_projection_rejects_snapshot_without_base_gameface(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        build_profile="light",
        release_name="2.3.1.5400",
        base_files={"res/scripts/client/App.py": b"SOURCE = 'base'\n"},
        locale_files={"EN": {"res/scripts/client/App.py": b"SOURCE = 'english'\n"}},
        actionscript_files={},
        stub_files={},
    )
    output = tmp_path / "output"

    result = _project(
        snapshot,
        output,
        target="wot-eu",
        snapshot_id=snapshot_id,
        descriptor_sha256=descriptor_sha256,
    )

    assert result.returncode == 1
    assert "no base res/gui/gameface payload" in result.stderr
    assert not output.exists()
