import requests

url = 'http://127.0.0.1:5000/'

book:dict[str, str|int] = {
    'title':'En liten restaurant i Thailand',
    'isbn': 9788234725180,
    'description':'Book about cooking and recipes about Thailand.',
    'release_year':2000,
    'author':'Warunne Bolstad',
    'author_id': 1,
    'themes':'Cooking',
    'status':'Available',
}

headers={
    'Content-type':'application/json',
    'Accept':'application/json'
}

response = requests.patch(url + 'book/1', json=book, headers=headers)
print(response.json())
