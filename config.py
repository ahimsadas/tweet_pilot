number_of_tweets = 5
query_topic = "crypto"

# Surround phrases with quotes (") for exact match.
# Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
# Prepend words that must not appear with a - symbol. Eg: -bitcoin
# Alternatively you can use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.
# The complete value for q must be URL-encoded. Max length: 500 chars.

# SECRETS
openai_api_key          = "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"
openai_organization_key = "org-FyPhgskwwxBLTTt9nIPjy4gD"
newsapi_api_key         = "cc5426462a664c0399c218ae0bdfd1b9"

chatGPT_prompt = "Compose tweets based on the news articles provided below in a sarcastic, satirical, and funny tone. Return the output in the given JSON format.{\"generated_tweets\": [{\"content\": \"<tweet>\"},{\"content\": \"<tweet>\"},...]}Append relevant hashtags and the respective URL of the article at the end of each <tweet>. Do not shorten the URLs and also throw in some emojis in the <tweet>"