from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

import wot_src_publisher.publication as publication_module


def _git(repository: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def test_large_object_staging_preserves_unchanged_parent_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()
    _git(repository, "init")
    _git(repository, "config", "user.name", "Publisher Test")
    _git(repository, "config", "user.email", "publisher@example.test")
    (repository / "unchanged.txt").write_text("keep me\n")
    (repository / "changed.bin").write_bytes(b"before")
    _git(repository, "add", "--all")
    _git(repository, "commit", "--message", "existing publication")

    (repository / "changed.bin").write_bytes(b"after")
    _git(repository, "add", "--all")
    _git(repository, "commit", "--message", "new publication")
    commit_sha = _git(repository, "rev-parse", "HEAD")
    expected_tree = _git(repository, "rev-parse", "HEAD^{tree}")

    monkeypatch.setattr(publication_module, "OBJECT_STAGING_THRESHOLD_BYTES", 0)
    monkeypatch.setattr(publication_module, "_push_commit", lambda *_args: None)
    monkeypatch.setattr(publication_module, "_delete_remote_ref", lambda *_args: None)

    with publication_module._prestage_large_git_objects(
        repository,
        repository,
        tmp_path / "staging-worktree",
        branch="wot-eu",
        commit_sha=commit_sha,
        changed_files=("changed.bin",),
    ) as staged:
        assert staged is not None
        assert staged.tree_sha == expected_tree


def test_large_object_staging_removes_the_source_of_a_detected_rename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()
    _git(repository, "init")
    _git(repository, "config", "user.name", "Publisher Test")
    _git(repository, "config", "user.email", "publisher@example.test")
    _git(repository, "config", "diff.renames", "true")
    (repository / "old.bin").write_bytes(b"same payload")
    _git(repository, "add", "--all")
    _git(repository, "commit", "--message", "existing publication")

    _git(repository, "mv", "old.bin", "new.bin")
    changed_files = publication_module._staged_changed_files(repository)
    assert set(changed_files) == {"old.bin", "new.bin"}
    _git(repository, "commit", "--message", "new publication")
    commit_sha = _git(repository, "rev-parse", "HEAD")
    expected_tree = _git(repository, "rev-parse", "HEAD^{tree}")

    monkeypatch.setattr(publication_module, "OBJECT_STAGING_THRESHOLD_BYTES", 0)
    monkeypatch.setattr(publication_module, "_push_commit", lambda *_args: None)
    monkeypatch.setattr(publication_module, "_delete_remote_ref", lambda *_args: None)

    with publication_module._prestage_large_git_objects(
        repository,
        repository,
        tmp_path / "staging-worktree",
        branch="wot-na",
        commit_sha=commit_sha,
        changed_files=changed_files,
    ) as staged:
        assert staged is not None
        assert staged.tree_sha == expected_tree
