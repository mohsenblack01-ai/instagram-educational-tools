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
    <p>🚀 Deployment Successful!</p>
    <p><a href="/demo">View API Demo</a></p>
    <p><a href="/learn">Learn Programming Concepts</a></p>
    '''

@app.route('/demo')
def demo():
    concepts = [
        "API Rate Limiting: Wait between requests",
        "Error Handling: Manage API failures gracefully",
        "Authentication: Secure login patterns",
        "Data Parsing: Extract information from API responses"
    ]
    
    return jsonify({
        "educational_demo": True,
        "concept": random.choice(concepts),
        "timestamp": datetime.now().isoformat(),
        "message": "This demonstrates API integration concepts"
    })

@app.route('/learn')
def learn():
    return '''
    <h1>🎓 Programming Concepts</h1>
    <ul>
    <li>API Integration</li>
    <li>Error Handling</li>
    <li>Rate Limiting</li>
    <li>Web Automation</li>
    <li>Python Flask Framework</li>
    </ul>
    <p><a href="/">← Back to Home</a></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
