from flask import Flask, request, jsonify
import os
import sys

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify(message='Server shutting down...')

@app.route('/')
def streamlit():
    os.system(f'streamlit run --server.port {request.host.split(":")[-1]} web.py')
    sys.exit(0)

if __name__ == '__main__':
    app.run(debug=True)
