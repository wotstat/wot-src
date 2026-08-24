from __future__ import annotations

import json
from pathlib import Path

import pytest
from snapshot_fixture import create_snapshot

from wot_src_publisher.publication import PublicationError, project_snapshot

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
) -> dict[str, object]:
    return project_snapshot(
        snapshot,
        output,
        target=target,
        expected_snapshot_id=snapshot_id,
        expected_descriptor_sha256=descriptor_sha256,
        config_path=ROOT / "config/targets.json",
    )


def test_wargaming_projection_applies_default_locale_and_keeps_all_locales(
    tmp_path: Path,
) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
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

    assert result["branch"] == "wot-eu"
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
    assert "Ветка: `wot-eu`" in readme
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
    assert publication_text.startswith('{\n  "branch": "wot-eu",\n')
    assert publication_text.endswith("\n")
    publication = json.loads(publication_text)
    assert publication["snapshot_id"] == snapshot_id
    assert publication["descriptor_sha256"] == descriptor_sha256
    assert publication["default_locale"] == "EN"
    assert publication["branch"] == "wot-eu"
    assert publication["commit_subject"] == "2.3.1.0 #903"


def test_lesta_projection_uses_base_and_ignores_locale_layers(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="mt-ru",
        publisher="lesta",
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

    assert result["branch"] == "mt-ru"
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


def test_projection_rejects_snapshot_without_base_gameface(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot_id, descriptor_sha256 = create_snapshot(
        snapshot,
        target="wot-eu",
        publisher="wargaming",
        release_name="2.3.1.5400",
        base_files={"res/scripts/client/App.py": b"SOURCE = 'base'\n"},
        locale_files={"EN": {"res/scripts/client/App.py": b"SOURCE = 'english'\n"}},
        actionscript_files={},
        stub_files={},
    )
    output = tmp_path / "output"

    with pytest.raises(PublicationError, match="no base res/gui/gameface payload"):
        _project(
            snapshot,
            output,
            target="wot-eu",
            snapshot_id=snapshot_id,
            descriptor_sha256=descriptor_sha256,
        )
    assert not output.exists()
