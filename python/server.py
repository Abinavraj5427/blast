from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from login_post_reddit import login_and_post_reddit
from datetime import datetime
from reddit_post_data import get_analytics
from twitter_post import login_and_post_twitter
from linkedin_post import post_linkedin
from twitter_post_data import get_twitter_analytics

cred = credentials.Certificate('firebase-sdk.json');
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
        urls = []
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
            urls.append(reddit_url)
            # print("POST", post)


            # print(reddit_username)
        else:
            post["reddit_url"] =""
        
        twitter_configured = userData["twitter"]["configured"]
        if(twitter_configured and some_json['twitter']):
            twitter_username = userData["twitter"]["username"]
            twitter_password = userData["twitter"]["password"]
            twitter_message = message;
            twitter_url = login_and_post_twitter(twitter_username, twitter_password, twitter_message)
            urls.append(twitter_url)
            post["twitter_url"] = twitter_url
        else:
            post["twitter_url"] = ""

        linkedin_configured = userData["linkedin"]["configured"]
        if(linkedin_configured and some_json["linkedin"]):
            linkedin_username = userData["linkedin"]["username"]
            linkedin_password = userData["linkedin"]["password"]
            linkedin_message = message;
            linkedin_url = post_linkedin(linkedin_username, linkedin_password, linkedin_message)
            urls.append(linkedin_url)
            post["linkedin_url"] = linkedin_url
        else:
            post["linkedin_url"] =""
        posts.append(post)
        userRef.document(email).update({"posts":posts})
        return jsonify(urls)


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
                if post["reddit_url"] != "":
                    output.append(get_analytics(post["reddit_url"]))
                else:
                    output.append({"output": False})

                if post["twitter_url"] != "":
                    output.append(get_twitter_analytics(post["twitter_url"]))
                else:
                    output.append({"output": False})
        
        return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
    