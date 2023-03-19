import argparse
import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_models_list() -> list:
    retval = []
    models = openai.Model.list()

    for i in models.data:
        retval.append(i['id'])

    retval.sort()
    return retval


def get_chat(model: str, prompt: str) -> str:
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


def main():
    parser = argparse.ArgumentParser()
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
    exit(main())
