import json
import sys
import os
from SimpleAES import SimpleAES
import getpass

"""
    storecreds
    Store credentials locally and encrypt them with a master key.
"""
def storecreds(filename):
    # Give overview
    print "We are now going to store your social media credentials."
    print "You will encrypt this using a master key at the end of this process."
    raw_input("Press Enter to continue...")
    print ""

    # Get credentials
    creds = getcreds()

    # Encrypt credentials
    enc = encryptcreds(creds)

    # Store credentials
    with open(filename, 'w+') as f:
        f.write(enc)

"""
    readcreds
    Read stored credentials locally and decrypt them.
    Returns json string containing credentials.
"""
def readcreds(filename):
    # Verify crendentials exists first
    if not os.path.isfile("creds"):
        raise Exception("Credentials file does not exist!")

    # Read credentials
    with open(filename, 'r') as f:
        enc = f.read()

    # Decrypt
    dec = decryptcreds(enc)

    # If good json string, return it. If not, exit.
    if is_json(dec):
        return dec
    else:
        raise Exception("Could not decrypt successfully!")

"""
    getcreds
    Get credentials from the user.
    Returns a json string of credentials (plain text).
"""
def getcreds():
    # Credentials will be stored in a json object
    creds = {}

    # Twitter
    print "Twitter credentials:"
    creds['twitter'] = {}
    creds['twitter']['consumerKey'] = raw_input("Consumer/API key: ")
    creds['twitter']['consumerSecret'] = raw_input("Consumer/API secret: ")
    creds['twitter']['accessToken'] = raw_input("Access token: ")
    creds['twitter']['accessSecret'] = raw_input("Access token secret: ")

    # For formatting
    print ""

    # Return as json string
    return json.dumps(creds)

"""
    encryptcreds
    Encrypts credentials.
    Returns an encrypted string.
"""
def encryptcreds(creds):
    # Request a master key
    print "We will now encrypt your credentials. Enter a master secret key."
    print "You will have to enter this key when you run romspam."
    masterKey = getpass.getpass("Master secret key: ")

    # Encrypt using AES-256
    aes = SimpleAES(masterKey)
    enc = aes.encrypt(creds)

    # Just to be safe, verify decryption
    dec = aes.decrypt(enc)
    if dec != creds:
        raise Exception("ERROR: Could not encrypt credentials!")

    # Return as encrypted string
    return enc

"""
    decryptcreds
    Decrypts credentials.
    Returns an decrypted string.
"""
def decryptcreds(creds):
    # Request the master key
    masterKey = getpass.getpass("Enter the master key you used to encrypt: ")

    # Decrypt using AES-256
    aes = SimpleAES(masterKey)
    dec = aes.decrypt(creds)

    # Return as decrypted string
    return dec

# Verifies a string is valid json
def is_json(str):
    try:
        jsonobj = json.loads(str)
    except ValueError, e:
        return False
    return True
