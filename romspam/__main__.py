import os, sys
import romquote, romcreds, romtwitter

def main():
    # Parse command line arguments. The following commands are possible:
    #       -h / help           display usage information
    #       reset               reset sent romantic phrases
    #       send                start sending romantic phrases
    #       auth[enticate]      enter credentials
    #       cred[entials]       print the currently stored credentials
    if len(sys.argv) != 2:
        print "Incorrect number of arguments!"
        print_usage()
    elif sys.argv[1] == "reset":
        reset()
    elif sys.argv[1] == "send":
        send()
    elif sys.argv[1] == "auth" or sys.argv[1] == "authenticate":
        authenticate()
    elif sys.argv[1] == "cred" or sys.argv[1] == "credentials":
        print_credentials()
    elif sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print_usage()
    else:
        print ("Invalid command entered!")
        print_usage()

# Print usage information to command line
def print_usage():
    print "Usage:"
    print "  romspam <command>"
    print ""
    print "Commands:"
    print "  [--]help/-h       display this usage information"
    print "  reset             reset sent romantic phrases"
    print "  send              start sending romantic phrases"
    print "  auth[enticate]    enter social media credentials"
    print "  cred[entials]     print the currently stored credentials"

# When reset, clear sent romantic phrases.
def reset():
    if os.path.isfile("sent"):
        os.remove("sent")
    print "Sent phrases reset!"

# When send, start sending romantic phrases
def send():
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

    # Get a quote to send
    quote = romquote.getquote()

    # Request name of user to send tweet to
    user = raw_input("Thanks!\nEnter bae's name: ").strip()
    if user[0] == "@":
        user = user[1:]

    # Send tweet
    print "Sending..."
    romtwitter.sendtweet(api, user, quote)
    print "Done!"

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
