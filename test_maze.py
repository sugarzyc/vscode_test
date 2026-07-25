import unittest
from unittest.mock import patch

with patch("builtins.input", return_value=""):
    from test import move


class MazeTests(unittest.TestCase):
    def test_moves_into_open_space(self):
        maze = ["#####", "#  E#", "#####"]
        self.assertEqual(move(maze, (1, 1), "d"), (1, 2))

    def test_stays_put_when_hitting_wall(self):
        maze = ["#####", "#  E#", "#####"]
        self.assertEqual(move(maze, (1, 1), "w"), (1, 1))


if __name__ == "__main__":
    unittest.main()
