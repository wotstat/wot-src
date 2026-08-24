from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_publisher_is_a_caller_owned_reusable_workflow() -> None:
    workflow = (ROOT / ".github/workflows/publish-snapshot.yml").read_text()

    assert "workflow_call:" in workflow
    assert "workflow_dispatch:" not in workflow
    assert "environment: selectel" in workflow
    assert "repository: ${{ job.workflow_repository }}" in workflow
    assert "ref: ${{ job.workflow_sha }}" in workflow
    assert "repositories: wot-src" in workflow
    assert "permission-contents: write" in workflow
    assert "${{ steps.app-token.outputs.token }}" in workflow
    assert "commit_sha:" in workflow
    assert "publication_state:" in workflow
    assert "version_name:" in workflow
