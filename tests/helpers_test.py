import unittest, helpers
import exceptions as e


class TestHelpers(unittest.TestCase):

    def test_buildText(self):
        self.assertEqual(helpers.buildText('@name went to @place', 'Mary', 'school'), 'Mary went to school',
                         'Testing buildText normal functionality')
        self.assertRaises(e.WrongNumberOfArguments, helpers.buildText, '@name went to @place', 'Mary', 'school', 'mom')
