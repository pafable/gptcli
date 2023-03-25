import unittest
from src.gptcli.image import get_image


class TestImage(unittest.TestCase):
    def test_get_image(self):
        self.assertEqual(
            type(
                get_image(
                    'A dog swimming at the beach',
                    1,
                    '256x256'
                )
            ),
            type([])
        )
