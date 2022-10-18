from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import User, Product
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repository.user import RepositoryUser
from src.infra.sqlalchemy.repository.product import RepositoryProduct

create_db()

app = FastAPI()

#Usuário

@app.post('/users')
def create_user(user: User, db: Session = Depends(get_db)):
    user_created = RepositoryUser(db).create(user)
    return user_created

@app.get('/users')
def list_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).list()
    return users

#Produto
@app.post('/products')
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created

@app.get('/products')
def list_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).list()
    return products