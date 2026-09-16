from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

import wot_src_publisher.publication as publication


def _payload(
    root: Path, path: str, content: bytes, language: str | None = None
) -> publication.PayloadFile:
    source = root / (language or "base") / path
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_bytes(content)
    return publication.PayloadFile(
        source=source,
        path=path,
        sha256=hashlib.sha256(content).hexdigest(),
        size=len(content),
        language=language,
    )


def test_def_is_projected_with_default_locale_overlay(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "snapshot"
    version = _payload(root, "version.xml", b"<root><version>v.1.2.3.4 #5</version></root>")
    base_def = _payload(root, "res/config/vehicle.def", b"<base/>")
    locale_def = _payload(root, "res/config/vehicle.def", b"<locale/>", "EN")
    other_def = _payload(root, "res/config/other.def", b"<other/>", "FR")
    gameface = _payload(root, "res/gui/gameface/index.html", b"<html/>")
    snapshot = publication.VerifiedSnapshot(
        root=root,
        descriptor={
            "source": {
                "publisher": "wargaming",
                "release_name": "release",
                "client_type": "sd",
                "languages": ["EN", "FR"],
            },
            "contract_version": "1.1.0",
            "created_at": "2026-01-01T00:00:00Z",
        },
        descriptor_sha256="a" * 64,
        files=(version, base_def, locale_def, other_def, gameface),
        actionscript=(),
        stubs=(),
    )
    monkeypatch.setattr(publication, "_verify_snapshot", lambda *_args, **_kwargs: snapshot)
    output = tmp_path / "published"

    result = publication._project_snapshot(
        root,
        output,
        target="wot-eu",
        expected_snapshot_id="sha256:" + "b" * 64,
        expected_descriptor_sha256="a" * 64,
        config_path=Path(__file__).parents[1] / "config/targets.json",
    )

    assert (output / "sources/res/config/vehicle.def").read_bytes() == b"<locale/>"
    assert (output / "locales/EN/res/config/vehicle.def").read_bytes() == b"<locale/>"
    assert (output / "locales/FR/res/config/other.def").read_bytes() == b"<other/>"
    assert result["counts"]["sources"] == 2
