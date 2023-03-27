"""
Base arguments
"""
import argparse

# non-standard import
try:
    from .__version__ import __version__
except ImportError:
    from __version__ import __version__


class BaseArgs(argparse.ArgumentParser):
    """
    Base arguments class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_argument(
            '-v',
            '--version',
            action='version',
            help='gpt-chat cli version',
            version=__version__
        )
