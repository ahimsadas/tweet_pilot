number_of_news_articles = 10
query_topic = "crypto"

# Surround phrases with quotes (") for exact match.
# Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
# Prepend words that must not appear with a - symbol. Eg: -bitcoin
# Alternatively you can use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.
# The complete value for q must be URL-encoded. Max length: 500 chars.

# SECRETS
openai_api_key              = "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"
openai_organization_key     = "org-FyPhgskwwxBLTTt9nIPjy4gD"
newsapi_api_key             = "cc5426462a664c0399c218ae0bdfd1b9"
TWITTER_API_KEY             = 'S9DlzxrQVnhkC7umCq4HCcZgS'
TWITTER_API_SECRET_KEY      = "TV9BrSpAEXB3GcNC5VxFTuS5wQuT4rVdyN50R3tLDpzL9QRxEC"
# TWITTER_CLIENT_ID           = "Umt2NjhGWnZ4TnF2UFhkZEZ3Q2o6MTpjaQ"
# TWITTER_CLIENT_SECRET       = "kJxtp-0cCZk8ZDjFGEOmzRo5-Qbgr4DrpQ9YdKsv6QaPNOWCqF"
TWITTER_ACCESS_TOKEN        = "3180326750-Ka9zltqvg6bZAwdWrPyjIE9qbloyGqd8hTsAHrL"
TWITTER_ACCESS_TOKEN_SECRET = "UI1kfi7xWnVJmcFCQOwJddZi8pKz5NYGIPfbgcQbxCENt"
# TWITTER_BEARER_TOKEN        = "AAAAAAAAAAAAAAAAAAAAANa2nAEAAAAAlGEO4ySucJ3pZjn3e%2BzFzIYrcnc%3DHmkvHIXw1hg8jQJELntbzKUrJCjMIQfM59tMm9cQJS7B8ECXLa"

chatGPT_prompt = "Form an opinion and compose a tweet based on the news article URL provided below - in a sarcastic, satirical, and funny tone.\n\nReturn the output in the given JSON format\n{\"generated_tweet\":\"<tweet>\"}\n\nAppend relevant hashtags at the end of the <tweet>.\nThe <tweet> should be in this format '<tweet_text> <relevant_hashtags>'.\nThrow in some emojis in the <tweet_text>.\n"