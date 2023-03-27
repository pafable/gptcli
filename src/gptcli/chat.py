"""
Interacts with OpenAI's ChatGPT
"""

import argparse
import os
import sys
import openai

# non-standard
from gpt_args import BaseArgs

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_models_list() -> list:
    """
    Retrieves model list
    :return: None
    """
    retval = []
    models = openai.Model.list()

    for i in models.data:
        retval.append(i['id'])

    retval.sort()
    return retval


def get_chat(model: str, prompt: str) -> str:
    """
    Sends prompt to ChatGPT and retrieves a response
    :param model: str
    :param prompt: str
    :return: str
    """
    retval = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    return retval.choices[0].message.content


# pylint: disable=missing-function-docstring
def main():
    parser = BaseArgs()
    parser.add_argument(
        dest='prompt',
        help='enter text to ask ChatGPT',
        nargs='*',
        type=str
    )

    args = parser.parse_args()

    resp = get_chat(
        'gpt-3.5-turbo',
        ' '.join(args.prompt)
    )

    print(resp)


if __name__ == '__main__':
    sys.exit(main())
