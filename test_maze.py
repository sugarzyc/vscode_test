import unittest
from test import move, render


class MazeTests(unittest.TestCase):
    def test_moves_into_open_space(self):
        maze = ["#####", "#  E#", "#####"]
        self.assertEqual(move(maze, (1, 1), "d"), (1, 2))

    def test_stays_put_when_hitting_wall(self):
        maze = ["#####", "#  E#", "#####"]
        self.assertEqual(move(maze, (1, 1), "w"), (1, 1))

    def test_render_places_player(self):
        maze = ["#####", "#  E#", "#####"]
        self.assertIn("@", render(maze, (1, 1)))


if __name__ == "__main__":
    unittest.main()
