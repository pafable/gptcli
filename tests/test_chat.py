import unittest
from src.gpt_cli.chat_cli import get_chat


class TestChat(unittest.TestCase):
    def test_get_chat(self):
        self.assertEqual(
            type(
                get_chat(
                    'gpt-3.5-turbo',
                    'say hello world'
                )
            ),
            type(
                'test'
            )
        )
