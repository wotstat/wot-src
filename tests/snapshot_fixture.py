from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def _canonical_json(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()
        + b"\n"
    )


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def create_snapshot(
    root: Path,
    *,
    target: str,
    publisher: str,
    build_profile: str,
    release_name: str,
    base_files: dict[str, bytes],
    locale_files: dict[str, dict[str, bytes]],
    actionscript_files: dict[str, bytes],
    stub_files: dict[str, bytes],
) -> tuple[str, str]:
    (root / "sources-as3").mkdir(parents=True, exist_ok=True)
    (root / "stubs").mkdir(parents=True, exist_ok=True)
    file_entries: list[dict[str, Any]] = []
    for path, payload in sorted(base_files.items()):
        destination = root / "sources/base" / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        file_entries.append(
            {
                "layer": {"kind": "base"},
                "path": path,
                "sha256": _sha256(payload),
                "size": len(payload),
            }
        )
    for language, files in sorted(locale_files.items()):
        for path, payload in sorted(files.items()):
            destination = root / "sources/locales" / language / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
            file_entries.append(
                {
                    "layer": {"kind": "locale", "language": language},
                    "path": path,
                    "sha256": _sha256(payload),
                    "size": len(payload),
                }
            )

    manifests: dict[str, dict[str, object]] = {}
    manifest_values: dict[str, list[dict[str, Any]]] = {
        "files": file_entries,
        "actionscript": [],
        "stubs": [],
        "packages": [],
        "conflicts": [],
    }
    for path, payload in sorted(actionscript_files.items()):
        destination = root / "sources-as3" / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        manifest_values["actionscript"].append(
            {"path": path, "sha256": _sha256(payload), "size": len(payload)}
        )
    for path, payload in sorted(stub_files.items()):
        destination = root / "stubs" / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        manifest_values["stubs"].append(
            {"path": path, "sha256": _sha256(payload), "size": len(payload)}
        )
    for name, values in manifest_values.items():
        encoded = b"".join(_canonical_json(value) for value in values)
        manifest_path = root / "manifests" / f"{name}.jsonl"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_bytes(encoded)
        manifests[name] = {
            "path": f"manifests/{name}.jsonl",
            "records": len(values),
            "sha256": _sha256(encoded),
        }

    source = {
        "api_host": "https://example.invalid/",
        "build_profile": build_profile,
        "chain_id": "fixture-chain",
        "client_type": "sd",
        "languages": sorted(locale_files) or ["RU"],
        "metadata_version": "fixture-metadata",
        "publisher": publisher,
        "release_name": release_name,
        "resolved_app_id": "FIXTURE",
        "target": target,
        "version_vector": [
            {"acquisition_mode": "reference", "name": "client", "version": "1"},
            {"acquisition_mode": "reference", "name": "sdcontent", "version": "1"},
            {
                "acquisition_mode": "install-bundle",
                "language": (sorted(locale_files) or ["RU"])[0],
                "name": "locale",
                "version": "1",
            },
        ],
    }
    policies = {
        name: {"name": f"fixture-{name}", "sha256": digit * 64, "version": "1"}
        for name, digit in (("readable", "1"), ("source_tree", "2"), ("vfs", "3"))
    }
    tools = [{"name": "fixture-tool", "version": "1"}]
    identity = {
        "contract": "game-snapshot",
        "contract_version": "1.1.0",
        "policies": policies,
        "source": source,
        "tools": tools,
    }
    snapshot_id = f"sha256:{_sha256(_canonical_json(identity))}"
    descriptor = {
        "contract": "game-snapshot",
        "contract_version": "1.1.0",
        "created_at": "2026-08-24T00:00:00Z",
        "manifests": manifests,
        "payload": {
            "actionscript_root": "sources-as3",
            "base_root": "sources/base",
            "locale_roots": {
                language: f"sources/locales/{language}" for language in sorted(locale_files)
            },
            "overlay_order": ["base", "locale:{language}"],
            "stubs_root": "stubs",
        },
        "policies": policies,
        "quality": {
            "required_transform_failures": 0,
            "unmanifested_payload_files": 0,
            "unresolved_conflicts": 0,
        },
        "snapshot_id": snapshot_id,
        "source": source,
        "tools": tools,
    }
    descriptor_bytes = _canonical_json(descriptor)
    descriptor_sha256 = _sha256(descriptor_bytes)
    (root / "snapshot.json").write_bytes(descriptor_bytes)
    (root / "READY").write_text(f"sha256:{descriptor_sha256}\n")
    return snapshot_id, descriptor_sha256
