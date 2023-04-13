from requests import get, post, delete, put


print(put('http://localhost:5000/api/jobs/1',
          json={'id': 1, 'job': 'test', 'work_size': 16, 'collaborators': '1, 5, 7', 'is_finished': False, 'team_leader': 1}).json())

print(put('http://localhost:5000/api/jobs/999',
          json={'id': 8, 'job': 'test', 'work_size': 16, 'collaborators': '1, 5, 7', 'is_finished': False, 'team_leader': 1}).json())
# Некорректное значение для id

print(put('http://localhost:5000/api/jobs/test',
          json={'id': 8, 'job': 'test', 'work_size': 16, 'collaborators': '1, 5, 7', 'is_finished': False, 'team_leader': 1}).json())
# Некорректное значение для id

print(get('http://localhost:5000/api/jobs').json())
