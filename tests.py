import unittest

from utils import sorting


class TestUtilities(unittest.TestCase):
    def setUp(self):
        self.final = {}
        self.teams = ["Team_1 1", " Team_2 3"]
        self.final_outcome = {'Foxes': 3, 'Tar': 1, 'Arks': 1, 'Hawks': 0}
        return super().setUp()
    def test_sorting(self):
        self.assertEqual(sorting(self.teams, self.final), {'Team_2': 3, 'Team_1': 0})



if __name__ == "__main__":
    unittest.main(verbosity=2)