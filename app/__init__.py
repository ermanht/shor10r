from flask import Flask, jsonify


# buat app
app = Flask(__name__)


# definisi route
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'success',
        'message': 'hello from shor10r',
    })

