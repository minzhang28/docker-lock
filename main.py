#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/Plugin.Activate', methods=['POST'])
def active_plugin():
    return jsonify({'tasks': tasks})

@app.route('/AuthzPlugin.AuthZReq', methods=['POST'])
def auth_req():
    return jsonify(
            {
                "Allow": False,
                "Msg":   "The authorization is failed",
                "Err":   "The error message if things go wrong"
            }
        )

@app.route('/AuthzPlugin.AuthZRes', methods=['GET'])
def auth_res():
    return jsonify(
        {
            "Allow":  False,
            "Msg":  "The authorization message",
            "Err":  "Response is wrong"
       }
    )

if __name__ == '__main__':
    app.run(debug=True)
