"""Lyric: Base"""
import logging


class LyricBase:
    """Base class for Lyric."""

    logger = logging.getLogger("Lyric")

    def __init__(self, attributes) -> None:
        """Initialize."""
        self.attributes = attributes
