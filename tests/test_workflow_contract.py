from pathlib import Path

WORKFLOW = Path(__file__).parents[1] / ".github/workflows/publish-snapshot.yml"


def test_private_key_is_an_explicit_reusable_workflow_secret() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")

    assert (
        "    secrets:\n"
        "      GH_APP_PRIVATE_KEY:\n"
        "        description: GitHub App private key supplied by the caller\n"
        "        required: true"
    ) in workflow
    assert "environment: selectel" not in workflow
    assert "private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}" in workflow
