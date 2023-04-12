from requests import get
from requests import get, post


print(post('http://localhost:5000/api/jobs',
           json={'id': 8, 'job': 'test', 'work_size': 16, 'collaborators': '1, 5, 7', 'is_finished': False, 'team_leader': 1}).json())

print(post('http://localhost:5000/api/jobs',
           json={'id': 8, 'job': 'test', 'work_size': 16, 'collaborators': 1, 'is_finished': False, 'team_leader': 1}).json())
# Некорректное значение для collaborators
print(post('http://localhost:5000/api/jobs',
           json={'id': 'test', 'job': 'test', 'work_size': 16, 'collaborators': '1, 5, 7', 'is_finished': False, 'team_leader': 1}).json())
# Некорректное значение для id
print(post('http://localhost:5000/api/jobs',
           json={'id': 1, 'job': 'test', 'work_size': 16, 'collaborators': '1, 5, 7', 'is_finished': False, 'team_leader': 1}).json())
# Использован существующий ключ id

print(get('http://localhost:5000/api/jobs').json())
