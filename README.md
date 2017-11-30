# mongo-flask-serializer

A serializer for MongoDB objects using flask and python.

When creating APIs with Flask and MongoDB, it can be very stressful to return a
JSON response with a MongoDB objectID or datetime format. This python class
handles that problem.

## Requirements
* flask

## Usage

```python
from flask import Flask
from serialize import Serializer

app = Flask(__name__)
ser = Serializer(app)

@app.route('/')
def serialize_test():
    """Testing the serializer."""
    test_json = {'id': ObjectId("58d8e4f9f2d63f0909523a7e"),
                 'Salute': 'Hey Whats up?',
                 'array': [1, 3, 4, 5]
                 }
    return ser.jsonify(test_json)

app.run(host='0.0.0.0', port=5006)
```
