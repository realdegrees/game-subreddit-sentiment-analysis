# Game Subreddit Sentiment Analysis

This project aims to analyze the sentiment of posts and comments in specific game-related subreddits. 
The goal is to provide insights into the community's sentiment over time and correlate it with external factors such as player numbers and developer communication.

## Planned Functionality

1. **Scrape Subreddit Posts and Comments**
    - Scrape posts from specified subreddits within the last 24 hours.
    - Extract and clean comments to be text-only.
    - Filter out bot comments and non-English comments.

2. **Sentiment Analysis**
    - Calculate sentiment for top-level comments initially.
    - Recursively factor in sub-comments, their sentiment, and votes.
    - Store sentiment data along with relevant statistics (timestamp, number of comments, submissions, etc.) in a database.

3. **API Development**
    - Provide an API to query the sentiment of a subreddit.
    - Allow filtering by timeframe to get daily sentiment for the last 30 days or other specified periods.

4. **Frontend Development**
    - Create a SvelteKit frontend to display the sentiment of a subreddit over time. (Likely in a separate repo)
    - Include visualizations such as graphs to represent sentiment trends.

5. **Optional Features**
    - Overlay sentiment graphs with [Steam player number charts](https://steamcommunity.com/dev) or timelines with developer tweets.
    - Analyze correlations between sentiment, player numbers, and developer communication.

## Subreddits to Scrape

- `tbd`

## License

This project is licensed under the MIT License.
