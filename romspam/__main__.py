import sys
import os
import romspam

def main():
    # First thing, make sure that the expected folder structure is in tact. This
    # means having an "images" folder in the root of the repo.
    romspam.init()

    # Parse command line arguments. The following commands are possible:
    #       -h / help           display usage information
    #       reset               reset sent romantic quotes and images
    #       start               start sending romantic phrases
    #       auth[enticate]      enter credentials
    #       cred[entials]       print the currently stored credentials
    #       quote               print out a random quote
    if len(sys.argv) != 2:
        print "Incorrect number of arguments!"
        romspam.print_usage()
    elif sys.argv[1] == "reset":
        romspam.reset()
    elif sys.argv[1] == "start":
        romspam.start()
    elif sys.argv[1] == "auth" or sys.argv[1] == "authenticate":
        romspam.authenticate()
    elif sys.argv[1] == "cred" or sys.argv[1] == "credentials":
        romspam.print_credentials()
    elif sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        romspam.print_usage()
    elif sys.argv[1] == "quote":
        romspam.quote()
    else:
        print ("Invalid command entered!")
        romspam.print_usage()
