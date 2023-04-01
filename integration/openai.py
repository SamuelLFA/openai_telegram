import requests
from decouple import config

OPENAI_API_URL = config('OPENAI_API_URL')
OPENAI_API_KEY = config('OPENAI_API_KEY')

# Set the endpoint URL
chat_url = '/v1/chat/completions'

# Set the request headers, including the authorization bearer token
headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json'
}

# Set url to the endpoint URL
url = OPENAI_API_URL + chat_url

# Function to send a POST request to the OpenAI API
def send_request(prompt):
    # Set the request body
    request_body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    # Send the POST request to the OpenAI API
    response = requests.post(
        url=url,
        headers=headers,
        json=request_body
    )
    
    # Check if the status code is 429, which means we've exceeded our quota
    if response.status_code == 429:
        return "I'm out of quota. Please try again later."
    
    if response.status_code != 200:
        return "---- Error ----"

    # Return the response
    return response.json()['choices'][0]['message']['content']
