from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/nudge_db"
mongo = PyMongo(app)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/nudges', methods=['GET'])
def get_nudges():
    nudges = mongo.db.nudges.find()
    return jsonify([{'message': nudge['message']} for nudge in nudges])

if __name__ == '__main__':
    app.run(debug=True)
