"""
Bot.py
Handles the Twitter bot stuff
"""

# Imports
import os
import twitter
from dotenv import load_dotenv

# Constructor
class Bot:
    # Fields
    load_dotenv()

    api = twitter.Api(
        consumer_key = os.getenv("consumer_key"),
        consumer_secret = os.getenv("consumer_secret"),
        access_token_key = os.getenv("access_token_key"),
        access_token_secret = os.getenv("access_token_secret")
    )

    print("[Bot]: Verifying credentials:")
    print(api.VerifyCredentials())

    # Constructor
    def __init__(self):
        print("init")

    # Post a tweet with an iamge attached
    def post_image(self, text, image):
        print("Bot: attempting to authenticate")

        api = twitter.Api(
            consumer_key=os.getenv("consumer_key"),
            consumer_secret=os.getenv("consumer_secret"),
            access_token_key=os.getenv("access_token_key"),
            access_token_secret=os.getenv("access_token_secret")
        )
        print(api.VerifyCredentials())

        print("Posting...")
        api.PostUpdate(str(text), media=image)
        print("Posted.")

    # Post a tweet (with an image attached) as a response to another tweet
    def post_image_as_response(self, text, image, originalTweetId):
        #

    # Post a tweet that is just text
    def post_text(self, text):
        #

    # Posts a tweet that is just text as a response to another tweet
    def post_text_as_response(self, text):
        #