from flask import Flask, request, jsonify
from .switch import on as switch_on, off as switch_off
from .switch import state as brain_state
import os
import logging

log_file = 'brain_app.log'

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file,  # Specify the log file name
    filemode='a'  # Append mode
)

@app.route('/on', methods=['POST'])
def on():
    client_ip = request.remote_addr
    logging.debug(f"BRAIN_MAC:  {os.environ.get('BRAIN_MAC')}")
    logging.debug(f"BRAIN_HOST: {os.environ.get('BRAIN_HOST')}")
    logging.debug(f"Client IP: {client_ip}")
    res = switch_on()
    logging.info(f"{client_ip} is switching brain ON: {res}")
    return jsonify(res)

@app.route('/off', methods=['POST'])
def off():
    client_ip = request.remote_addr
    logging.debug(f"Client IP: {client_ip}")
    res = switch_off()
    logging.info(f"{client_ip} is switching brain OFF: {res}")
    return jsonify(res)

@app.route('/state', methods=['GET'])
@app.route('/status', methods=['GET'])
@app.route('/health', methods=['GET'])
def status():
    client_ip = request.remote_addr
    logging.debug(f"Client IP: {client_ip}")
    res = brain_state()
    logging.info(f"{client_ip} ask for brain state: {res}")
    return jsonify(res)

@app.route('/logs', methods=['GET'])
def get_logs():
    n = request.args.get('n', default=10, type=int)  # Default to 10 lines if 'n' is not provided
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:] if len(lines) >= n else lines
            return jsonify({'logs': last_n_lines})
    except FileNotFoundError:
        return jsonify({'error': 'Log file not found'}), 404



# @app.route('/alexa-endpoint', methods=['POST'])
# def handle_alexa_request():
#     """ curl -X POST https://brain.h2d2cloud.org/alexa-endpoint 
#     -d '{"request": {"intent": {"name": "coco", "slots": {"onoff" : {"value": "on"}}}  } }' 
#     -H "Content-Type: application/json"""
#     data = request.get_json()
#     client_ip = request.remote_addr
#     logging.info(f"Received from Alexa ({client_ip}):'{data}'")

#     # Extract intent and slots
#     intent = data.get('request', {}).get('intent', {}).get('name')
#     onoff = data.get('request', {}).get('intent', {}).get('slots', {}).get('onoff', {}).get('value')
#     action = "allumer"
#     if onoff == 'on':
#         res = switch_on()
#     else:
#         action = "eteindre"
#         res = switch_off()

#     mess = f"brain va s'{action}"   
#     if res.get("status") != "success":
#         mess = f"une erreur s'est produite lors de la commande pour {action} brain"

#     logging.info(res)

#     # Your logic here (e.g., toggle a switch)
#     response = {
#         "version": "1.0",
#         "response": {
#             "outputSpeech": {
#                 "type": "PlainText",
#                 "text": mess
#             }
#         }
#     }

#     return jsonify(response)

# @app.route('/authorize', methods=['POST'])
# def authorize():
#     client_ip = request.remote_addr
#     payload = request.get_json()
#     return jsonify({"status": "success", 
#           "message": f"authorize payload was: {payload}"})

# @app.route('/token', methods=['GET'])
# def token():
#     client_ip = request.remote_addr
#     return jsonify({"status": "success", 
#           "message": f"I am fine (status not yet implemented)"})



# @app.route('/alexaworld', methods=['POST'])
# def alexa_webhook():
#     data = request.get_json()
#     logging.info(f"in alexaworld: '{data}'")
#     if not data:
#         return jsonify({'error': 'No data provided'}), 400

#     # Handle Alexa request
#     if data.get('request', {}).get('type') == 'LaunchRequest':
#         response = {
#             'version': '1.0',
#             'response': {
#                 'outputSpeech': {
#                     'type': 'PlainText',
#                     'text': 'Hello, World!'
#                 }
#             }
#         }
#     else:
#         response = {
#             'version': '1.0',
#             'response': {
#                 'outputSpeech': {
#                     'type': 'PlainText',
#                     'text': 'Sorry, I didn\'t understand that.'
#                 }
#             }
#         }

#     return jsonify(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)