from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {'1': 'Имя: Пример, возраст: 18'}
user_id_counter = 1

class User(BaseModel):
    username: str
    age: int

@app.get("/users")
def get_users():
    return users

@app.post('/user/{username}/{age}')
def create_user(username: str, age: int):
    global user_id_counter
    user_id_counter += 1
    users[str(user_id_counter)] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id_counter} зарегистрирован'

@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id} обновлен'

@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    del users[user_id]
    return f'Пользователь {user_id} удален'

#    uvicorn module_16_3:app --reload

