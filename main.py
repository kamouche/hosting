import praw
reddit = praw.Reddit(
    client_id="BkKWoie6bDWNlkHti7Lptw",
    client_secret="eZGedgMdbicHBn6u5s2xbrct-P4rlQ",
    user_agent="my user agent",
    username="uxdesigning",
    password="kamouche@123",
    check_for_async = False
)
import time
import random
def karma():
  try:
    message = ["Upvoted, Upvote in return?", "Great post, care to share the upvotes!"]
    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
      submission.upvote()
      rand = random.randint(0,(len(message)-1))
      print(submission.title)
      submission.reply(message[rand])
      time.sleep(30)
  except:
    time.sleep(300)
    karma()
karma()
