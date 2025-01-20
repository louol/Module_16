from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
def read_main():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
def read_admin():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
def read_user(user_id: Annotated[int, Path(gt=1, le=100, description='Enter User ID', example=1)]):
    return {'message': f'Вы вошли как пользователь №  {user_id}'}

@app.get('/user')
def read_user_info(username: str = '123', age: int = 56):
    return {'message': f'Информация о пользователе. Имя:  {username}, Возраст: {age}'}

@app.get('/user/{username}/{age}')
def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                  example='UrbanUser')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]
):
    return {'message': f'Информация о пользователе. Имя:  {username}, Возраст: {age}'}

