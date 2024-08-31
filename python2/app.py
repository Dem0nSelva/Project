from flask import Flask, request, jsonify, render_template
import praw
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

# Reddit API credentials
REDDIT_CLIENT_ID = 'G_g8iVFhdo18N_LoJ55h4g'
REDDIT_CLIENT_SECRET = 'dvic1ZE6m9rSzcD4SoMmkh4DZjvumg'
REDDIT_USER_AGENT = 'my_api/0'

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_post_and_comments', methods=['POST'])
def get_post_and_comments():
    data = request.json
    post_id = data['post_id']

    try:
        submission = reddit.submission(id=post_id)
        post_text = submission.title + " " + submission.selftext
        comments = submission.comments.list()
        comments_text = [comment.body for comment in comments if hasattr(comment, 'body')]
        return jsonify({'post': post_text, 'comments': comments_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    post_text = data['post']
    comments = data['comments']

    try:
        post_sentiment = analyze_sentiment([post_text])
        comments_sentiment = analyze_sentiment(comments)
        return jsonify({'post_sentiment': post_sentiment, 'comments_sentiment': comments_sentiment})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
