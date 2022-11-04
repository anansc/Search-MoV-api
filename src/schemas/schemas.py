from pydantic import BaseModel
from typing import Optional

#Criando a classe usuário
class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    age: int
    user_adress: Optional[str] = None
    phone: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    email: str
    
    class Config:
        orm_mode = True

#Criando a classe produtos
class House(BaseModel):
    id: Optional[str] = None
    name: str
    type: str
    size: str
    product_adress: str    
    bedroom: Optional[int] = 0
    restroom: Optional[int] = 0
    furniture: bool = False
    available: bool = False
    
    class Config:
        orm_mode = True