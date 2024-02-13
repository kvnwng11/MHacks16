import os
import openai
import json

openai.api_type = "azure"
openai.api_key = '9fd2d1a84636415685bcf7dc451040fb'

openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
openai.api_version = '2023-03-15-preview'

try:
    response = openai.ChatCompletion.create(
        engine='gpt-4',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    )

    # print the response
    print(response['choices'][0]['message']['content'])

except openai.error.APIError as e:
    # Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")

except openai.error.AuthenticationError as e:
    # Handle Authentication error here, e.g. invalid API key
    print(f"OpenAI API returned an Authentication Error: {e}")

except openai.error.APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")

except openai.error.InvalidRequestError as e:
    # Handle connection error here
    print(f"Invalid Request Error: {e}")

except openai.error.RateLimitError as e:
    # Handle rate limit error
    print(f"OpenAI API request exceeded rate limit: {e}")

except openai.error.ServiceUnavailableError as e:
    # Handle Service Unavailable error
    print(f"Service Unavailable: {e}")

except openai.error.Timeout as e:
    # Handle request timeout
    print(f"Request timed out: {e}")

except:
    # Handles all other exceptions
    print("An exception has occured.")