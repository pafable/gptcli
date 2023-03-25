import unittest
from src.gptcli.chat_cli import (
    get_models_list,
    get_chat
)


class TestGpt(unittest.TestCase):
    test_list = ['test']

    def test_get_models_list(self):
        self.assertEqual(
            type(
                get_models_list()
            ),
            type(
                TestGpt.test_list
            )
        )

    def test_get_chat(self):
        self.assertEqual(
            type(
                get_chat(
                    'gpt-3.5-turbo',
                    'say hello'
                )
            ),
            type(TestGpt.test_list[0])
        )
