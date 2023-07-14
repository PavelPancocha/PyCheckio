import unittest

from ice_base.find_quotes import find_quotes


class TestFindQuotes(unittest.TestCase):
    def test_find_quotes_greetings(self):
        self.assertEqual(find_quotes('"Greetings"'), ['Greetings'])

    def test_find_quotes_hi(self):
        self.assertEqual(find_quotes('Hi'), [])

    def test_find_quotes_superman(self):
        self.assertEqual(find_quotes('good morning mister "superman"'), ['superman'])

    def test_find_quotes_no_sense(self):
        self.assertEqual(find_quotes('"this" doesn\'t make any "sense"'), ['this', 'sense'])

    def test_find_quotes_lorem_ipsum(self):
        self.assertEqual(
            find_quotes(
                '"Lorem Ipsum" is simply dummy text '
                'of the printing and typesetting '
                'industry. Lorem Ipsum has been the '
                '"industry\'s standard dummy text '
                'ever since the 1500s", when an '
                'unknown printer took a galley of '
                'type and scrambled it to make a type '
                'specimen book. It has survived not '
                'only five centuries, but also the '
                'leap into electronic typesetting, '
                'remaining essentially unchanged. "It '
                'was popularised in the 1960s" with '
                'the release of Letraset sheets '
                'containing Lorem Ipsum passages, and '
                'more recently with desktop '
                'publishing software like Aldus '
                'PageMaker including versions of '
                'Lorem Ipsum.'
                ), ['Lorem Ipsum',
                    "industry's standard dummy text ever "
                    'since the 1500s',
                    'It was popularised in the 1960s']
            )

    def test_find_quotes_empty(self):
        self.assertEqual(find_quotes('count empty quotes ""'), [''])


if __name__ == "__main__":
    unittest.main()
