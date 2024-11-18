import unittest

from utils import display_ranking, decision, sorting, read_text, read_file


class TestUtilities(unittest.TestCase):
    def setUp(self):
        self.final = {}
        self.teams = ["Team_1 1", " Team_2 3"]
        return super().setUp()
    def test_sorting(self):
        self.assertEqual(sorting(self.teams, self.final), {'Team_2': 3, 'Team_1': 0})



if __name__ == "__main__":
    unittest.main(verbosity=2)