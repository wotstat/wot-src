from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_publish_workflow_is_native_to_main_and_uses_the_reserved_runner() -> None:
    workflow = (ROOT / ".github/workflows/publish-snapshot.yml").read_text()

    assert "workflow_dispatch:" in workflow
    assert "contents: write" in workflow
    assert "- ${{ inputs.runner_label }}" in workflow
    assert "ref: main" in workflow
    assert "wot-src-publisher publish" in workflow
    assert "group: wot-src-${{ inputs.branch }}" in workflow
