from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def index():
    json_response = [
        {
            "electric": [
                62,
                45,
                15,
                44,
                20
            ],
            "magnetic": [
                47,
                10,
                43,
                61
            ],
            "gravitational": [
                5,
                41,
                63,
                -9,
                9,
                12
            ]
        },
        {
            "electric": [
                1,
                82,
                56,
                48
            ],
            "magnetic": [
                -2,
                58,
                96,
                14,
                94
            ],
            "gravitational": [
                -8,
                98,
                -5
            ]
        },
        {
            "electric": [
                68,
                81,
                40,
                -2,
                -8
            ],
            "magnetic": [
                74,
                -12,
                67,
                54
            ],
            "gravitational": [
                85,
                -6
            ]
        }
    ]
    return json.dumps(json_response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
