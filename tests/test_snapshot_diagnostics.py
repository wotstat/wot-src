from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from wot_src_publisher import publication


@pytest.mark.parametrize("language", [None, "EN"])
@pytest.mark.parametrize("actual", [b"altered", b""])
def test_payload_mismatch_identifies_the_file_without_logging_payload_or_runner_paths(
    tmp_path: Path,
    language: str | None,
    actual: bytes,
) -> None:
    root = tmp_path / "private-runner-home" / "snapshot"
    payload_root = "sources/base" if language is None else f"sources/locales/{language}"
    relative_path = 'res/gui/icon "quoted"\n.png'
    path = root / payload_root / relative_path
    path.parent.mkdir(parents=True)
    path.write_bytes(actual)
    expected = b"correct"
    expected_sha256 = hashlib.sha256(expected).hexdigest()
    entry = {"path": relative_path, "size": len(expected), "sha256": expected_sha256}

    with pytest.raises(publication.PublicationError, match="payload does not match") as failure:
        publication._payload_file(
            root, payload_root, entry, label="files manifest entry 84337", language=language
        )

    message = str(failure.value)
    assert '"payload_path":' in message
    details = json.loads(message.split(" details=", 1)[1])
    assert details["payload_path"] == f"{payload_root}/{relative_path}"
    assert details["language"] == language
    assert details["expected_size"] == len(expected)
    assert details["actual_size"] == len(actual)
    assert details["filesystem_size"] == len(actual)
    assert details["expected_sha256"] == expected_sha256
    assert details["actual_sha256"] == hashlib.sha256(actual).hexdigest()
    assert details["mtime_ns"] > 0
    assert details["ctime_ns"] > 0
    assert "private-runner-home" not in message
    assert "altered" not in message
    assert "\n" not in message
    assert "\\n" in message

