import json
from flask import Flask
from flask import request
from flask import make_response
import requests
import uuid

app = Flask(__name__)

@app.route("/facade_service", methods=['POST'])
def facade_post():
    message_json = request.get_json()
    send_message = str(message_json['message'])
    random_uuid = uuid.uuid4()
    uuid_str = str(random_uuid)
    send_to_log = {'message': send_message, 'uuid': uuid_str}
    requests.post(url="http://localhost:5001/logging_service", json=send_to_log)
    response = make_response("Success")
    return response

@app.route("/facade_service", methods=['GET'])
def facade_get():
    logging_service = requests.get(url="http://localhost:5001/logging_service")
    messages_service = requests.get(url="http://localhost:5005/messages_service")
    return_string = "logging_service:" + logging_service.text + "\n messages_service: " + messages_service.text
    return return_string


if __name__ == "__main__":
    app.run(host="localhost",
            port=5000,
            debug=True)
