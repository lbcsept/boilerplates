from flask import Flask, request, jsonify
from .switch import on as switch_on, off as switch_off
import os
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/on', methods=['POST'])
def on():
    # Your Python logic here
    logging.info("Triggering on brain")
    logging.debug(f"BRAIN_MAC:  {os.environ.get('BRAIN_MAC')}")
    logging.debug(f"BRAIN_HOST: {os.environ.get('BRAIN_HOST')}")
    return jsonify(switch_on())
    # return jsonify({"status": "turning brain on"})

@app.route('/off', methods=['POST'])
def off():
    logging.info("Triggering off brain")
    return jsonify(switch_off())

@app.route('/trigger', methods=['POST'])
def trigger_code():
    # Your Python logic here
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)