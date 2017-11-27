"""This package helps with serialize mongo objects in flask."""
import datetime
from flask import json
from bson.objectid import ObjectId


class MongoJsonEncoder(json.JSONEncoder):
    """."""

    def default(self, obj):
        """."""
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class Serializer:
    """."""

    def __init__(self, app):
        """."""
        self.app = app

    def jsonify(self, *args, **kwargs):
        """Function jsonify with support for MongoDB ObjectId."""
        indent = None
        separators = (',', ':')

        if self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] or self.app.debug:
            indent = 2
            separators = (', ', ': ')

        if args and kwargs:
            raise TypeError(
                'jsonify() behavior undefined when passed both args and kwargs'
            )
        elif len(args) == 1:  # single args are passed directly to dumps()
            data = args[0]
        else:
            data = args or kwargs

        return self.app.response_class(
            (json.dumps(
                data, indent=indent,
                separators=separators, cls=MongoJsonEncoder),
             '\n'),
            mimetype=self.app.config['JSONIFY_MIMETYPE']
        )


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    ser = Serializer(app)

    @app.route('/')
    def serialize_test():
        """Testing the serializer."""
        test_json = {'id': ObjectId("58d8e4f9f2d63f0349523a7e"),
                     'Salute': 'Hey Whats up?',
                     'array': [1, 3, 4, 5]
                     }
        return ser.jsonify(test_json)

    app.run(host='0.0.0.0', port=5006)
