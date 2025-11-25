from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🤖 Instagram API Educational Toolkit</h1>
    <p>📚 Learning: API Integration & Python Automation</p>
    <p>⚠️ For Educational Purposes Only</p>
    <p><a href="/demo">View Demo</a></p>
    '''

@app.route('/demo')
def demo():
    return jsonify({
        "educational_demo": True,
        "message": "Learning API Rate Limiting & Error Handling",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
