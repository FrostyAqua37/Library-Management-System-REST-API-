import requests

url = 'http://127.0.0.1:5000/'

Information = {
    'title': 'Project Hail Mary',
    'isbn': 9781529157468,
    'description': 'A lone astronaut.',
    'release_year': 2022,
    'author': 'Andy Weir',
    'author_id': 1,
    'themes': 'Space',
    'status': 'Available',
}

response = requests.put(url + 'book/1', Information)
print(response.headers)
