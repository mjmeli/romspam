import argparse

def main():
    print "Entered main"

    # Parse command line arguments. The following optional arguments can be
    # specified:
    #   -c  cache romantic phrases
    parser = argparse.ArgumentParser(description="run a tool of rom-spam")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c","--cache", help="cache romantic phrases",
                       action="store_true")
    parser.parse_args()

    # Determine what action to take based on command line input
    if args.cache:
        print "Cache command"
    else:
        print "No command specified"

def test():
    return "This is a test!"
