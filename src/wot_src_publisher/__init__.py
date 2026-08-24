"""Publish source-oriented projections of sealed GameSnapshots."""

from wot_src_publisher.publication import (
    PublicationError,
    publish_snapshot,
)

__all__ = ["PublicationError", "publish_snapshot"]
