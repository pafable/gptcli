"""
Interacts with OpenAI's image generation AI
"""
import argparse
import webbrowser
import os
import openai

# non-standard
from gpt_args import BaseArgs

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_image(prompt: str, count: int, res: str) -> dict:
    """
    Sends a request to generate images
    :param prompt: str
    :param count: int
    :param res: str
    :return:
    """
    retval = openai.Image.create(
        prompt=prompt,
        n=count,
        size=res
    )
    return retval.data


# pylint: disable=missing-function-docstring
def main():
    parser = BaseArgs()
    parser.add_argument(
        '-p',
        '--prompt',
        help='enter text to generate image',
        required=True,
        type=str
    )
    parser.add_argument(
        '-c',
        '--count',
        default=1,
        help='enter amount of images to generate [MAX = 10]',
        type=int
    )
    parser.add_argument(
        '-r',
        '--resolution',
        default='512x512',
        help='enter the resolution of the image. ex: 256x256, 512x512, 1024x1024 ',
        type=str
    )

    args = parser.parse_args()

    resp = get_image(
        args.prompt,
        args.count,
        args.resolution
    )

    for url in resp:
        webbrowser.open_new_tab(url.url)


if __name__ == '__main__':
    main()
