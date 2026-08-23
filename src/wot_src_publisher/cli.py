from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Sequence
from pathlib import Path

from wot_src_publisher.publication import (
    PublicationError,
    project_snapshot,
    publish_snapshot,
)


def _add_snapshot_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--expected-snapshot-id", required=True)
    parser.add_argument("--expected-descriptor-sha256", required=True)
    parser.add_argument("--expected-profile", choices=("full", "light"), required=True)
    parser.add_argument("--config", type=Path, default=Path("config/targets.json"))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Project a verified GameSnapshot into a wot-src data tree."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    project = subparsers.add_parser("project")
    _add_snapshot_arguments(project)
    project.add_argument("--output", type=Path, required=True)
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


def main(argv: Sequence[str] | None = None) -> int:
    try:
        arguments = _parser().parse_args(argv)
        common = {
            "target": arguments.target,
            "branch": arguments.branch,
            "expected_snapshot_id": arguments.expected_snapshot_id,
            "expected_descriptor_sha256": arguments.expected_descriptor_sha256,
            "expected_profile": arguments.expected_profile,
            "config_path": arguments.config,
        }
        if arguments.command == "project":
            result = project_snapshot(
                arguments.snapshot,
                arguments.output,
                **common,
            )
        elif arguments.command == "publish":
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
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
