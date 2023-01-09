import requests
api_url = 'https://api.github.com/users/kp2077'

todo = {
    "user_id": 909,
    "id": 909,
    "title": "Sakda Sungkamanee" ,
    "completed": True
    }


response = requests.get(api_url)

print(response.json())
print(response.status_code)