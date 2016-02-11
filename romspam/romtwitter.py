# Thanks to bear for his python-twitter API! Don't have time to write my own...
# https://github.com/bear/python-twitter

import twitter
import json

"""
    AuthenticationException
    Exception to be thrown in the event of a failed authentication.
"""
class AuthenticationException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

"""
    authenticate
    Retrieve login credentials and create an api instance. Requires the json
    representation of the credentials.
"""
def authenticate(creds):
    # Convert json string of credentials to object
    creds = json.loads(creds)

    # Grab each of the credentials
    try:
        consumerKey = creds['twitter']['consumerKey']
        consumerSecret = creds['twitter']['consumerSecret']
        accessToken = creds['twitter']['accessToken']
        accessSecret = creds['twitter']['accessSecret']
    except Exception as e:
        raise Exception("Twitter credentials were not in the correct format.")

    # Do the authenication
    api = twitter.Api(consumer_key=consumerKey,
                      consumer_secret=consumerSecret,
                      access_token_key=accessToken,
                      access_token_secret=accessSecret)

    # Verify authentication
    try:
        api.VerifyCredentials()
    except twitter.TwitterError as e:
        raise AuthenticationException("Could not authenticate. Invalid credentials/tokens?")

    # Return the authenticated api object
    return api

"""
    sendtweet
    Post a tweet to Twitter. Don't try to worry about character limits, this
    will handle it better.
"""
def sendtweet(api, user, tweet):
    # Verify authentication first
    try:
        api.VerifyCredentials()
    except twitter.TwitterError as e:
        raise AuthenticationException("Could not authenticate. Invalid credentials/tokens?")

    # Segment tweet into 140 characters or less
    tweets = formattweet(user, tweet)

    # Post each tweet
    for tweet in tweets:
        status = api.PostUpdate(tweet)

"""
    formattweet
    Formats a tweet being sent to a user into 140 characters.
    Returns an list of strings; each is a unique message to send.
"""
def formattweet(user, tweet):
    start = "@" + user + " "
    maxtweet = 140 - len(start)
    tweets = []

    # If we don't need to split up the message, then don't.
    if len(tweet) <= maxtweet:
        tweets.append(start + tweet)
        return tweets
    else:
        # If we do, do some nifty formatting involving splitting on newlines and stuff.
        lastSpace = -1
        lastNewline = -1
        lastSplit = -1
        splits = []

        # Identify where to split. Use some custom looping to reset iterator.
        i = 0
        while i < len(tweet):
            # Get the current character
            c = tweet[i]

            # Keep track of the last space and newline for splitting purposes
            if c == ' ':
                lastSpace = i
            elif c == '\n':
                lastNewline = i

            # Check if we've reached a tweet limit
            if (i - lastSplit) % maxtweet == 0:
                # Check if we should split at a newline (this is priority)
                if lastNewline != -1:
                    splits.append(lastNewline)
                    i = lastNewline
                # If there are no newlines, split at the last space
                elif lastSpace != -1:
                    splits.append(lastSpace)
                    i = lastSpace
                else:
                    splits.append(i)

                # Reset last newline and last space and update last split
                lastSplit = i
                lastNewline = -1
                lastSpace = -1

            # Increment our iterator
            i = i + 1

        # Make sure we have the end of the string as a 'split' point
        if splits[len(splits)-1] != len(tweet):
            splits.append(len(tweet))

        # Do the splitting
        lastSplit = 0
        for i in splits:
            tweets.append(start + tweet[lastSplit : i])
            lastSplit = i + 1
        return tweets
