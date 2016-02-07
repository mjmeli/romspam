from unittest import TestCase
import json
from romspam.setencoder import SetEncoder

class TestSetEncoder(TestCase):
    # Tests ability to serialize a set into json
    def test_set_encoder(self):
        # Create set
        testset = {"test1", "test2", "test3", "test4", "test4", "test2", "test2"}
        self.assertEquals(len(list(testset)), 4)
        # Encode to json string and verify it's valid
        enc = json.dumps(testset, cls=SetEncoder)
        self.assertTrue(self.is_json(enc))
        # Go back to json object and check length
        jsonobj = json.loads(enc)
        self.assertEquals(len(jsonobj), 4)

    # Verifies a string is valid json
    def is_json(self, str):
        try:
            jsonobj = json.loads(str)
        except ValueError, e:
            return False
        return True
