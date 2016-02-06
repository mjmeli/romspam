from unittest import TestCase

#import testname    # change to the module under test

class TestTestname(TestCase):
    def test_is_string(self):
        s = "test"
        self.assertTrue(isinstance(s, basestring))
