import os
from flask import Flask, jsonify


# buat app
app = Flask(__name__)


# app configuration
app_settings = os.environ.get('APP_SETTINGS')
app.config.from_object(app_settings)


# definisi route
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'success',
        'message': 'hello from shor10r',
    })

