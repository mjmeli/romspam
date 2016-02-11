from unittest import TestCase
from lxml import html
import requests

from romspam import romquote

class TestGetQuote(TestCase):
    # Tests ability to get a random romantic quote
    def test_get_quote(self):
        page = requests.get('http://www.romanticlovemessages.com/random/')
        tree = html.fromstring(page.content)
        # Get quote and new quote button
        quote = tree.xpath('normalize-space(//div[@id="hl1"]/text())')
        button = tree.xpath('//center/form/button[@class="button"]/text()')
        # Verify this information
        print "*****QUOTE****** = " + quote
        self.assertTrue(len(quote) >= 1)
        self.assertTrue(isinstance(quote, str))
        self.assertEqual(len(button), 1)
        self.assertEqual(button[0], "Next Random Romantic Love Message")

    def test_get_quote_module(self):
        for x in range(10):
            quote = romquote.getquote()
            self.assertTrue(len(quote) >= 1)
            self.assertTrue(isinstance(quote, str))
            self.assertFalse("`" in quote)
