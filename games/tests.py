from django.test import TestCase
from games.models import Game

class GamesTest(TestCase):
    def test_models_exist(self):
        game = Game()
        self.assertIsNotNone(game)

    def test_attributes_from_mlb_json_exist(self):
        game = Game()
        attributes = game._meta.get_fields()
        self.assertNotEqual(0, len(attributes))
        self.assertNotEqual(1, len(attributes))

