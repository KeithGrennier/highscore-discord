import unittest
from highscores import read_data

class TestHighScore(unittest.TestCase):
    def test_read_data(self):
        data=read_data()
        self.assertIsNotNone(data)