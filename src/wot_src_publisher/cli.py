from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Sequence
from pathlib import Path

from wot_src_publisher.publication import (
    PublicationError,
    publish_snapshot,
)


def _add_snapshot_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--expected-snapshot-id", required=True)
    parser.add_argument("--expected-descriptor-sha256", required=True)
    parser.add_argument("--config", type=Path, default=Path("config/targets.json"))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Project a verified GameSnapshot into a wot-src data tree."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    publish = subparsers.add_parser("publish")
    _add_snapshot_arguments(publish)
    publish.add_argument("--repository", type=Path, default=Path.cwd())
    return parser


def _write_github_result(result: dict[str, object]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        counts = result.get("counts", {})
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("## wot-src publication\n\n")
            summary.write(f"- State: `{result.get('publication_state', 'projected')}`\n")
            summary.write(f"- Branch: `{result.get('branch')}`\n")
            summary.write(f"- Version: `{result.get('version_name')}`\n")
            summary.write(f"- Snapshot: `{result.get('snapshot_id')}`\n")
            summary.write(f"- Files: `{json.dumps(counts, sort_keys=True)}`\n")
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as output:
            for name in ("commit_sha", "publication_state", "version_name"):
                value = result.get(name)
                if isinstance(value, str) and "\n" not in value and "\r" not in value:
                    output.write(f"{name}={value}\n")


def _write_failure(error: PublicationError) -> None:
    message = " ".join(str(error).split())
    if len(message) > 4000:
        message = f"…{message[-3999:]}"
    print(
        "publisher stage=publication status=failed "
        f"error={json.dumps(message, ensure_ascii=False)}",
        file=sys.stderr,
        flush=True,
    )
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        safe_message = message.replace("`", "'")
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("## wot-src publication\n\n")
            summary.write("- State: `failed`\n")
            summary.write(f"- Error: {safe_message}\n")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        escaped = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(
            f"::error title=wot-src publication failed::{escaped}",
            file=sys.stderr,
            flush=True,
        )


def main(argv: Sequence[str] | None = None) -> int:
    try:
        arguments = _parser().parse_args(argv)
        common = {
            "target": arguments.target,
            "expected_snapshot_id": arguments.expected_snapshot_id,
            "expected_descriptor_sha256": arguments.expected_descriptor_sha256,
            "config_path": arguments.config,
        }
        if arguments.command == "publish":
            result = publish_snapshot(
                arguments.repository,
                arguments.snapshot,
                **common,
            )
        else:  # pragma: no cover - argparse enforces this
            raise AssertionError(arguments.command)
        _write_github_result(result)
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":"), sort_keys=True))
        return 0
    except PublicationError as error:
        _write_failure(error)
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
