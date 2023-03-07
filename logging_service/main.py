from flask import Flask
from flask import request
from flask import make_response
import sys


app = Flask(__name__)


@app.route("/logging_service", methods=['POST'])
def logging_post():
    message_json = request.get_json()
    got_message = message_json['message']
    got_uuid = message_json["uuid"]
    dict.update({got_uuid: got_message})
    print(str(dict), sys.stdout)
    print(request.get_json(), sys.stdout)
    response = make_response("Success")
    return response

@app.route("/logging_service", methods=['GET'])
def logging_get():
    return_messages = str(list(dict.values()))
    return return_messages


if __name__ == "__main__":
    dict = {}
    app.run(host="localhost",
            port=5001,
            debug=True)
