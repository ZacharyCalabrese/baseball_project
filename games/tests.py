from django.test import TestCase
from games.models import Game

class GamesTest(TestCase):
    def test_models_exist(self):
        game = Game()
        self.assertIsNotNone(game)
