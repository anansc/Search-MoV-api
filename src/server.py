from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas.schemas import User, House
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repository.user import RepositoryUser
from src.infra.sqlalchemy.repository.house import RepositoryHouse

create_db()

app = FastAPI()

#Usuário
@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_db)):
    user_created = RepositoryUser(db).create(user)
    return user_created

@app.get('/users', status_code=status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).list()
    return users

@app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = RepositoryUser(db).get(user_id)
    return user

@app.delete('/users/{user_id}', status_code=status.HTTP_200_OK)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    RepositoryUser(db).remove(user_id)
    return {"MSG": "Usuário removido com sucesso"}

#Imóveis
@app.post('/houses', status_code=status.HTTP_201_CREATED)
def create_house(house: House, db: Session = Depends(get_db)):
    house_created = RepositoryHouse(db).create(house)
    return house_created

@app.get('/houses', status_code=status.HTTP_200_OK)
def list_house(db: Session = Depends(get_db)):
    houses = RepositoryHouse(db).list()
    return houses

@app.get('/houses/{house_id}', status_code=status.HTTP_200_OK)
def get_house(house_id: int, db: Session = Depends(get_db)):
    house = RepositoryHouse(db).get(house_id)
    return house

@app.delete('/houses/{house_id}', status_code=status.HTTP_200_OK)
def remove_house(house_id: int, db: Session = Depends(get_db)):
    RepositoryHouse(db).remove(house_id)
    return {"MSG": "Imóvel removido com sucesso"}