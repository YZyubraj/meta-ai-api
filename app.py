from flask import Flask, jsonify
from src.meta_ai_api.main import MetaAI

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/prompt/<message>')
def prompt(message):
    meta = MetaAI()
    response = meta.prompt(message, stream=False)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
