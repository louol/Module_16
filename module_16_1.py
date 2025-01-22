from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_main() -> str:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
def read_admin() -> str:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
def read_user(user_id: int) -> str:
    return {'message': f'Вы вошли как пользователь №  {user_id}'}

@app.get('/user')
def read_user_info(username: str = '123', age: int = 56) -> str:
    return {'message': f'Информация о пользователе. Имя:  {username}, Возраст: {age}'}


