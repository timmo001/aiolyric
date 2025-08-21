"""Test __version__ module."""

from aiolyric._version import __version__


def test__version():
    """Test the __version__ string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0
