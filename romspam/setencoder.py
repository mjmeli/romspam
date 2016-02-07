# Serializes a set into json by first converting it to a list.
# http://stackoverflow.com/questions/8230315/python-sets-are-not-json-serializable

import json

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
