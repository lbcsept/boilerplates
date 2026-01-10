from flask import Flask, request, jsonify
from .switch import on as switch_on, off as switch_off

app = Flask(__name__)


@app.route('/on', methods=['POST'])
def on_test():
    # Your Python logic here
    print("Triggering on brain")
    switch_on()
    return jsonify({"status": "brain turned on"})

@app.route('/off', methods=['POST'])
def off():
    # Your Python logic here
    switch_off()
    return jsonify({"status": "switching off brain"})

@app.route('/trigger', methods=['POST'])
def trigger_code():
    # Your Python logic here
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)