from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from login_post_reddit import login_and_post_reddit
from datetime import datetime
from reddit_post_data import get_analytics
from twitter_post import login_and_post_twitter

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
        
        post = {}

        now = datetime.now() 
        post['datetime'] = now.strftime("%m-%d-%Y, %H:%M:%S")
        reddit_configured = userData["reddit"]["configured"]
        if(reddit_configured and some_json['reddit']):
            reddit_username = userData["reddit"]["username"]
            reddit_password = userData["reddit"]["password"]
            reddit_sub = some_json['subreddit']
            reddit_subject = some_json['subject']
            reddit_message = message;
            reddit_urls = login_and_post_reddit(reddit_username, reddit_password, reddit_subject, reddit_message, reddit_sub)
            # print(reddit_urls)
            reddit_url = reddit_urls
            # print(reddit_url)
            posts = userData["posts"]
            # print(posts)
            post["reddit_url"] = reddit_url
            # print("POST", post)
            posts.append(post)
            userRef.document(email).update({"posts":posts})
            # print(reddit_username)

        
        twitter_configured = userData["reddit"]["configured"]
        if(twitter_configured and some_json['twitter']):
            twitter_username = userData["twitter"]["username"]
            twitter_password = userData["twitter"]["password"]
            twitter_message = message;
            twitter_url = login_and_post_twitter(twitter_username, twitter_password, twitter_message)
            post["twitter_url"] = twitter_url

        return jsonify(userData)


@app.route("/data", methods=['POST'])
def data():
    if(request.method == 'POST'):
        some_json = request.get_json()
        email = some_json['email']
        datetime = some_json['datetime']

        userData = userRef.document(email).get().to_dict()
        posts = userData["posts"]

        output = []
        for post in posts:
            if post["datetime"] == datetime:
                output.append(get_analytics(post["reddit_url"]))
        
        return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
    