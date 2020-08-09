from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from login_post_reddit import login_and_post_reddit

cred = credentials.Certificate('./python/firebase-sdk.json');
firebase_admin.initialize_app(cred)
db = firestore.client()
userRef = db.collection('users')

app = Flask(__name__)
CORS(app)

@app.route("/post", methods=['POST'])
def post():
    if(request.method == 'POST'):
        some_json = request.get_json()
        email = some_json['email']
        message = some_json['message']

        userData = userRef.document(email).get().to_dict()
        
        reddit_configured = userData["reddit"]["configured"]
        if(reddit_configured and some_json['reddit']):
            reddit_username = userData["reddit"]["username"]
            reddit_password = userData["reddit"]["password"]
            reddit_sub = some_json['subreddit']
            reddit_subject = some_json['subject']
            reddit_message = message;
            login_and_post_reddit(reddit_username, reddit_password, reddit_subject, reddit_message, reddit_sub)
            # print(reddit_username)

        return jsonify(userData)


@app.route("/data", methods=['POST'])
def data():
    if(request.method == 'POST'):
        some_json = request.get_json()
        email = some_json['email']

        userData = userRef.document(email).get()
        # print(userData.to_dict())

        return jsonify(userData.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
    