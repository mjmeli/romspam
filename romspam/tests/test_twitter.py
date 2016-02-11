from unittest import TestCase
import os
import mock
from romspam import romcreds
from romspam import romtwitter
from romspam import romquote

class TestTwitter(TestCase):
    # Test to make authentication is working
    def test_authentication(self):
        # Get credentials
        if os.path.isfile("creds"):
            with mock.patch('getpass.getpass', return_value=''):
                creds = romcreds.readcreds("creds")

            # Get an api instance
            try:
                api = romtwitter.authenticate(creds)
                self.assertTrue(api.VerifyCredentials() != None)
            except romtwitter.AuthenticationException as e:
                raise AssertionError("Credentials could not be authenticated.")
        else:
            raise AssertionError("Credential file does not exist, so can't test Twitter.")

    # Test tweet formatting
    def test_tweet_format(self):
        # Create a couple of test tweets
        user = "testuser"
        testtweets = [
            'Not even one moment passes without a thought of you.',
            'I had such a wonderful dream that you were mine, then I woke up smiling because I realized it was not just a dream.',
            'When I first saw you, you took my breath away.\n' + \
                'When you first talked to me, I couldn\'t think.\n' + \
                'When you asked me out, I couldn\'t respond.\n' + \
                'When you touched me, I got shivers all through my body.\n' + \
                'And when we first kissed, I floated away in my dreams.',
            'Love is like a friendship caught on fire. In the beginning a flame, very pretty, often hot and fierce, but still only light and flickering. As love grows older, our hearts mature and our love becomes as coals, deep-burning and unquenchable.\n' + \
                '- Bruce Lee'
        ]

        # Add in some random tweets for good coverage
        for i in range(25):
            testtweets.append(romquote.getquote())

        # Check each tweet in turn
        for i, testtweet in enumerate(testtweets):
            # Format the tweet
            tweets = romtwitter.formattweet(user, testtweet)

            # Verify certain aspects of each tweet
            for tweet in tweets:
                # Verify each tweet in the array is under the character limit
                self.assertTrue(len(tweet) <= 140)

                # Make sure the first character after the user isn't a newline or space
                tweetStart = len("@" + user + " ")
                self.assertTrue(tweet[tweetStart] != ' ')
                self.assertTrue(tweet[tweetStart] != '\n')

            # Now check specific tweets come out correctly
            if i == 0 or i == 1:
                self.assertTrue(len(tweets) == 1)
            if i == 2:
                self.assertTrue(len(tweets) == 3)
            if i == 3:
                self.assertTrue(len(tweets) == 2)
