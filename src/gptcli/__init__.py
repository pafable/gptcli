# pylint: disable=missing-module-docstring
try:
    from .chat import (
        get_chat,
        get_models_list
    )
    from .image import get_image
    from .__version__ import __version__
except ImportError:
    from chat import (
        get_chat,
        get_models_list
    )
    from image import get_image
    from __version__ import __version__