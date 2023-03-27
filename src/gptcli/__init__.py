# pylint: disable=missing-module-docstring
import os

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

import openai
openai.api_key = os.environ.get('OPENAI_API_KEY')
