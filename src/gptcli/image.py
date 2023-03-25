import argparse
import webbrowser
import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_image(prompt: str, count: int, size: str) -> str:
    retval = openai.Image.create(
        prompt=prompt,
        itr=count,
        size=size
    )
    return retval


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--prompt',
        help='enter text to generate image',
        type=str
    )
    parser.add_argument(
        '-c',
        '--count',
        help='enter amount of images to generate [MAX = 10]',
        type=int
    )
    parser.add_argument(
        '-s',
        '--size',
        help='enter resolution size. ex: 256x256, 512x512, 1024x1024 ',
        type=str
    )

    args = parser.parse_args()

    resp = get_image(
        args.prompt,
        args.count,
        args.size
    )

    print(resp)


if __name__ == '__main__':
    main()
