"""
Bot.py
Handles the Twitter bot stuff
"""

# Imports
import os
import twitter
from dotenv import load_dotenv


# Initialize
def init():
    load_dotenv()

# API
def sendTweet(text, image):
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