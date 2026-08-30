from __future__ import annotations

from pathlib import Path

from wot_src_publisher.publication import PayloadFile, _commit_subject


def test_common_test_version_is_normalized_for_commit_subject(tmp_path: Path) -> None:
    payload = b"<version.xml><version>v.2.4.0.0 Common Test #927</version></version.xml>"
    version_path = tmp_path / "version.xml"
    version_path.write_bytes(payload)
    version_file = PayloadFile(
        source=version_path,
        path="version.xml",
        sha256="0" * 64,
        size=len(payload),
    )

    assert _commit_subject({"version.xml": version_file}) == "2.4.0.0 #927"
