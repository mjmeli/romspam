import sys
import romspam

def main():
    # Parse command line arguments. The following commands are possible:
    #       -h / help           display usage information
    #       reset               reset sent romantic phrases
    #       send                start sending romantic phrases
    #       auth[enticate]      enter credentials
    #       cred[entials]       print the currently stored credentials
    if len(sys.argv) != 2:
        print "Incorrect number of arguments!"
        romspam.print_usage()
    elif sys.argv[1] == "reset":
        romspam.reset()
    elif sys.argv[1] == "send":
        romspam.send()
    elif sys.argv[1] == "auth" or sys.argv[1] == "authenticate":
        romspam.authenticate()
    elif sys.argv[1] == "cred" or sys.argv[1] == "credentials":
        romspam.print_credentials()
    elif sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        romspam.print_usage()
    else:
        print ("Invalid command entered!")
        romspam.print_usage()
