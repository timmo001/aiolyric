"""Lyric base."""

import logging

from ..client import LyricClient


class LyricBaseObject:
    """Base class for Lyric."""

    logger = logging.getLogger(__name__)

    def __init__(
        self,
        attributes: dict,
    ) -> None:
        """Initialize."""
        self.attributes = attributes


class LyricBaseClient(LyricBaseObject):
    """Base class for Lyric."""

    def __init__(
        self,
        client: LyricClient,
        attributes: dict,
    ) -> None:
        """Initialise."""
        super().__init__(attributes)
        self.client = client
