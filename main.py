import requests
import json
import config
import openai
openai.organization = config.openai_organization_key
openai.api_key = config.openai_api_key
openai.Model.list()

url = f"https://newsapi.org/v2/everything?pageSize={config.number_of_tweets}&q={config.query_topic}&apiKey={config.newsapi_api_key}"

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

    # Processing the response
    chatGPT_response = ask_gpt(prompt)

    # Converting response string to JSON
    chatGPT_json_response = json.loads(chatGPT_response)

    # Processing each tweet
    tweets = []
    for tweet in chatGPT_json_response['generated_tweets']:
        tweets.append(tweet['content'])

    for item in tweets:
        print(item,"\n")
else:
    print("Error fetching data: ", response.status_code)
