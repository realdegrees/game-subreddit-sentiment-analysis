import praw
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

# Initialize PRAW with your credentials
reddit = praw.Reddit('bot')

# List of subreddits to scrape
subreddits = ['newworldgame', 'thefinals', 'Helldivers']

# Function to scrape subreddit posts from the last 24 hours
def scrape_subreddit(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.top(time_filter='day'):

        votes = submission.score
        upvote_ratio = submission.upvote_ratio
        upvotes = int(votes * upvote_ratio)
        downvotes = votes - upvotes
        num_comments = submission.num_comments

        # skip posts with low activity
        if upvotes + downvotes + num_comments < 10:
            continue
        
        comments = submission.comments.list()   

        # TODO
        # cleanup comments to be text only
        # filter out bots, non-english, etc.
        # calculate sentiment (top level comments at first, then recursively factor in sub-comments, their sentiment, and votes)
        # store sentiment and some stats like the timestamp, number of comments, submissions etc. which were used for the sentiment calculation in a database
        # provide API to query the sentiment of a subreddit, allow filtering like timeframe etc. to e.g. get the daily sentiment of a sub for the last 30 days
        # create a sveltekit frontend to display the sentiment of a subreddit over time (with nice graphs etc.)
        # optional: overlay graphs with steamcharts graphs (if API available) or timelines with dev tweets to see if there is a correlation between sentiment and player numbers or dev communication

        print(f"Comments: {num_comments}")
        print(f"Downvotes: {downvotes}")
        print(f"Upvotes: {upvotes}")
        # print(f"URL: {submission.url}")
        # print(f"Created: {submission_time}")
        print("-" * 40)

# Scrape each subreddit in the list
for subreddit in subreddits:
    print(f"Scraping subreddit: {subreddit}")
    scrape_subreddit(subreddit_name=subreddit)
    print("=" * 40)