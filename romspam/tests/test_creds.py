from unittest import TestCase
import mock, six
import json
import getpass

from romspam import romcreds

class TestCreds(TestCase):
    # Test to make sure a json string containing credentials is valid
    def check_creds(self, creds):
        # Convert credentials to json and verify them
        credsJson = json.loads(creds)
        if 'twitter' in credsJson:
            for cred in credsJson['twitter']:
                if credsJson['twitter'][cred] == "testCred":
                    assert True
                else:
                    assert False

    # Test to make sure that credentials can be received
    def test_get_creds(self):
        # Get unencrypted credentials
        with mock.patch('__builtin__.raw_input', return_value='testCred'):
            creds = romcreds.getcreds()

        # Test the credentials
        self.check_creds(creds)

    # Test encryption
    def test_enc_creds(self):
        # Get unencrypted credentials
        with mock.patch('__builtin__.raw_input', return_value='testCred'):
            creds = romcreds.getcreds()

        # Test the credentials
        self.check_creds(creds)

        # Encrypt and then immediately decrypt credentials
        with mock.patch('getpass.getpass', return_value=''):
            enc = romcreds.encryptcreds(creds)
            dec = romcreds.decryptcreds(enc)

        # Test the credentials again
        self.check_creds(dec)
