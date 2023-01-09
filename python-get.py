import requests
api_url = 'https://api.github.com/users/kp2077'


response = requests.get(api_url)

print(response.json())
print(response.status_code)