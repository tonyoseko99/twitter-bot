# Twitter Bot

This is a Python-based Twitter bot that retweets tweets with over a million likes.

## Prerequisites

- Python 3.x
- Tweepy library
- Twitter API credentials

## Installation

1. Clone the repository: 
- `git clone https://github.com/your-username/twitter-bot.git`

2. Change to the project directory: 
- `cd twitter-bot`

3. Set up a virtual environment (optional but recommended):
- `python3 -m venv venv`
- `source venv/bin/activate`

4. Install the required dependencies:
- `pip install -r requirements.txt`


## Configuration

1. Obtain Twitter API credentials by creating a Twitter Developer account and a new app.
2. Copy the credentials (consumer key, consumer secret, access token, access token secret) to the `config.py` file.
3. Alternatively, you can set the credentials as environment variables.

## Usage

1. Run the bot script:
- `python3 bot.py`

2. The bot will start retweeting tweets with over a million likes in real-time.

## Customization

- You can modify the search query in the `bot.py` file to change the criteria for retweeting tweets.
- Adjust the frequency of retweeting by modifying the sleep duration between retweets.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).





