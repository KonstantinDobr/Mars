from requests import get, post, delete


print(delete('http://localhost:5000/api/jobs/1').json())

print(delete('http://localhost:5000/api/jobs/999').json())
# Некорректное значение для id

print(delete('http://localhost:5000/api/jobs/test').json())
# Некорректное значение для id

print(get('http://localhost:5000/api/jobs').json())
