import os, sys
import romquote, romcreds

import mock

def main():
    # Parse command line arguments. The following commands are possible:
    #       -h / help           display usage information
    #       reset               reset sent romantic phrases
    #       send                start sending romantic phrases
    #       auth/authenticate   enter credentials
    if len(sys.argv) != 2:
        print "Incorrect number of arguments!"
        print_usage()
    elif sys.argv[1] == "reset":
        reset()
    elif sys.argv[1] == "send":
        send()
    elif sys.argv[1] == "auth" or sys.argv[1] == "authenticate":
        authenticate()
    elif sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print_usage()
    else:
        print ("Invalid command entered!")
        print_usage()

# Print usage information to command line
def print_usage():
    print "Usage:"
    print "  python romspam <command>"
    print ""
    print "Commands:"
    print "  [--]help/-h       display this usage information"
    print "  reset             reset sent romantic phrases"
    print "  send              start sending romantic phrases"
    print "  auth[enticate]    enter social media credentials"

# When reset, clear sent romantic phrases.
def reset():
    if os.path.isfile("sent.json"):
        os.remove("sent.json")
    print "Sent phrases reset!"

# When send, start sending romantic phrases
def send():
    print romquote.getquote()

# When authenticate, request the user's credentials
def authenticate():
    if os.path.isfile("creds"):
        answer = raw_input("You already have credentials. Continue anyway? [y/n] ")
        if answer == "y":
            romcreds.storecreds("creds")
        elif answer != "n":
            print "I asked for y/n..."
    else:
        romcreds.storecreds("creds")
