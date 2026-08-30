from __future__ import annotations

from pathlib import Path

from wot_src_publisher.publication import PayloadFile, _commit_subject, _data_readme


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


def test_data_readme_contains_target_status_badge_linked_to_branch() -> None:
    readme = _data_readme(
        target="wot-eu",
        branch="wot-eu",
        release_name="1.44.0.8017",
        commit_subject="1.44.0.0 #8017",
        publisher="wargaming",
        snapshot_id="sha256:" + "a" * 64,
    )

    assert (
        "[![wot-eu status](https://img.shields.io/endpoint?"
        "url=https%3A%2F%2Fwotstat.github.io%2F"
        "game-unpack-pipeline%2Fbadges%2Fwot-eu.json)]"
        "(https://github.com/wotstat/wot-src/tree/wot-eu)"
    ) in readme
