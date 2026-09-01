from __future__ import annotations

from pathlib import Path

from wot_src_publisher.publication import (
    REGION_BRANCHES,
    PayloadFile,
    _commit_subject,
    _data_readme,
)

ROOT = Path(__file__).parents[1]


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


def test_data_readme_contains_all_status_badges_in_main_order() -> None:
    readme = _data_readme(
        target="wot-eu",
        branch="wot-eu",
        release_name="1.44.0.8017",
        commit_subject="1.44.0.0 #8017",
        publisher="wargaming",
        snapshot_id="sha256:" + "a" * 64,
    )

    expected = [
        f"[![{branch} status](https://img.shields.io/endpoint?"
        "url=https%3A%2F%2Fwotstat.github.io%2F"
        f"game-unpack-pipeline%2Fbadges%2F{branch}.json)]"
        f"(https://github.com/wotstat/wot-src/tree/{branch})"
        for _, branch in REGION_BRANCHES
    ]
    data_badges = [line for line in readme.splitlines() if line.startswith("[![")]
    main_badges = [
        line
        for line in (ROOT / "README.md").read_text().splitlines()
        if line.startswith("[![")
    ]

    assert data_badges == expected
    assert main_badges == expected
