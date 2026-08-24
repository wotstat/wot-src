from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_publish_workflow_uses_the_caller_reserved_runner() -> None:
    workflow = (ROOT / ".github/workflows/publish-snapshot.yml").read_text()

    assert "workflow_call:" in workflow
    assert "permission-contents: write" in workflow
    assert "- ${{ inputs.runner_label }}" in workflow
    assert "ref: ${{ job.workflow_sha }}" in workflow
    assert "wot-src-publisher publish" in workflow
    assert "group: wot-src-${{ inputs.branch }}" in workflow
