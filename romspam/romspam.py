"""
    romspam.py
    Contains all the functions for each command.
"""

import os
import sys
import json
import time
import romquote, romcreds, romtwitter, setencoder

# Print usage information to command line
def print_usage():
    print "Usage:"
    print "  romspam <command>"
    print ""
    print "Commands:"
    print "  [--]help/-h       display this usage information"
    print "  reset             reset sent romantic phrases"
    print "  start              start sending romantic phrases"
    print "  auth[enticate]    enter social media credentials"
    print "  cred[entials]     print the currently stored credentials"

# When reset, clear sent romantic phrases.
def reset():
    if os.path.isfile("sent"):
        os.remove("sent")
        print "Sent phrases reset!"
    else:
        print "You don't even have any sent phrases..."

# When start, start sending romantic phrases
def start():
    # Verify credentials exist. If not, give some suggestions.
    if not os.path.isfile("creds"):
        print "Could not locate credentials file."
        print "Did you try running romspam with the auth option?"
        print "See help for more info (\'romspam help\')."
        sys.exit()

    # Get credentials
    print "Getting credentials. Please help me decrypt!"
    creds = romcreds.readcreds("creds")

    # Authenticate with twitter
    api = romtwitter.authenticate(creds)

    # Request name of user to send tweet to
    user = raw_input("Thanks!\nEnter bae's name: ").strip()
    if len(user) == 0 or len(user) > 15:
        print "Invalid name entered."
        sys.exit()
    if user[0] == "@":
        user = user[1:]

    # Everything is set up to run. Now we just send a quote every 15 minutes.
    try:
        while True:
            # Get a quote to send. We want it to be unique, so we must check against
            # the sent quotes file. If this file doesn't exist it's obviously unique.
            if os.path.isfile("sent"):
                with open("sent", "r") as f:
                    sent = set(json.loads(f.read()))
            else:
                sent = set({})
            quote = romquote.getquote()
            while quote in sent or not isinstance(quote, str):
                quote = romquote.getquote()

            # Send tweet
            print "Sending..."
            #romtwitter.sendtweet(api, user, quote)
            print quote
            print "Done!"

            # Add quote to the set and write out
            sent.add(quote)
            with open("sent", "w+") as f:
                f.write(json.dumps(sent, cls=setencoder.SetEncoder))

            # Wait 15 minutes
            time.sleep(60*15)
    except KeyboardInterrupt:
        print "\nHappy Valentine's Day!"
        pass

# When authenticate, request the user's credentials
def authenticate():
    if os.path.isfile("creds"):
        answer = raw_input("You already have credentials. Continue anyway? [y/n] ")
        if answer == "y":
            print ""
            romcreds.storecreds("creds")
        elif answer != "n":
            print "I asked for y/n..."
    else:
        romcreds.storecreds("creds")

# When credentials, print the currently stored credentials.
def print_credentials():
    if os.path.isfile("creds"):
        creds = romcreds.readcreds("creds")
        print romcreds.stringify(creds)
    else:
        print "No credentials are currently stored. Try using \'romspam auth\'."

# When quote, just print out a random quote
def quote():
    print romquote.getquote()
