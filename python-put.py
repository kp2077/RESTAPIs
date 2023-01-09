import requests
api_url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(api_url)
print(response.json())

todo = {
    "user_id": 909,
    "id": 909,
    "title": "Sakda Sungkamanee" ,
    "completed": True
    }

response = requests.put(api_url, json=todo)

print(response.json())
print(response.status_code)