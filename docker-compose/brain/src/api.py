from flask import Flask, request, jsonify
from .switch import on as switch_on, off as switch_off
import os
import logging

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
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

@app.route('/authorize', methods=['POST'])
def authorize():
    client_ip = request.remote_addr
    payload = request.get_json()
    return jsonify({"status": "success", 
          "message": f"authorize payload was: {payload}"})


@app.route('/status', methods=['GET'])
@app.route('/health', methods=['GET'])
def status():
    client_ip = request.remote_addr
    return jsonify({"status": "success", 
          "message": f"I am fine (status not yet implemented)"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)