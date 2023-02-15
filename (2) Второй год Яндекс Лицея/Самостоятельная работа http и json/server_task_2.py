from flask import Flask, url_for, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    json_response = {
        "2220-10-17": {
            "source": [
                4.7,
                3.2,
                5.9,
                4.4,
                4.7,
                7.2,
                4.6,
                8.8
            ],
            "modified": [
                4.6,
                7.1,
                9.4,
                2.9,
                9.3,
                3.8,
                7.3,
                7.7
            ]
        },
        "2220-10-18": {
            "source": [
                6.9,
                7.2,
                4.6,
                1.8,
                7.2
            ],
            "modified": [
                6.5,
                2.6,
                7.1,
                5.1,
                7.1
            ]
        }
    }
    return json.dumps(json_response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)