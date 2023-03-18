import openai
import os
import argparse

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
    p = 'tell me a story of a lion cub'
    resp = get_chat('gpt-3.5-turbo', p)
    print(resp)


if __name__ == '__main__':
    exit(main())
