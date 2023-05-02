import requests
import json
import config
import tweepy
import openai
openai.organization = config.openai_organization_key
openai.api_key = config.openai_api_key
openai.Model.list()

url = f"https://newsapi.org/v2/everything?pageSize={config.number_of_tweets}&q={config.query_topic}&apiKey={config.newsapi_api_key}"

client = tweepy.Client(
    consumer_key        = config.TWITTER_API_KEY,
    consumer_secret     = config.TWITTER_API_SECRET_KEY,
    access_token        = config.TWITTER_ACCESS_TOKEN,
    access_token_secret = config.TWITTER_ACCESS_TOKEN_SECRET
)

# Fetch the JSON data from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    chatGPT_prompt = config.chatGPT_prompt
    
    # Decode the JSON data
    data = json.loads(response.text)

    urls = []
    for article in data['articles']:
        urls.append(article['url'])

    print("DEBUG : Total Number of articles received = ",len(urls),"\n")

    # Append URLs in chatGPT prompt
    for url in urls:
        # TODO: Add check if URL has already been processed (implement DB)
        chatGPT_prompt+=f"\n{url}"

    # Set the parameters for the request
    model         = "text-davinci-003"
    prompt        = chatGPT_prompt
    temperature   = 0.9
    max_tokens    = 1024

    def ask_gpt(prompt):
        completions = openai.Completion.create(
            model       = model,
            prompt      = prompt,
            max_tokens  = max_tokens,
            temperature = temperature
        )
        message = completions.choices[0].text
        return message.strip()

    print("DEBUG : chatGPT_prompt = ",chatGPT_prompt,"\n")

    # Processing the response
    chatGPT_response = ask_gpt(prompt)

    print("DEBUG : chatGPT_response = ",chatGPT_response,"\n")

    # Converting response string to JSON
    chatGPT_json_response = json.loads(chatGPT_response)

    print("DEBUG : chatGPT_json_response = ",chatGPT_json_response,"\n")

    # Extracting the tweets array
    tweets = []
    for tweet in chatGPT_json_response['generated_tweets']:
        tweets.append(tweet['content'])

    # Processing each tweet
    for item in tweets:
        print(item,"\n")
        client.create_tweet(text=item)
else:
    print("Error fetching data: ", response.status_code)
