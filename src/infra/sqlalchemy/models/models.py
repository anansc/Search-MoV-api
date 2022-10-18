from sqlalchemy import Column, Boolean, Integer, String
from src.infra.sqlalchemy.config.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    user_adress = Column(String)
    phone = Column(String)
    cpf = Column(String)
    cnpj = Column(String)
    email = Column(String)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    size = Column(String)
    product_adress = Column(String)
    bedroom = Column(Integer)
    restroom = Column(Integer)
    furniture = Column(Boolean)
    available = Column(Boolean)