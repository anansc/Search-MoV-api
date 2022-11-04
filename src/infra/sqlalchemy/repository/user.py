from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryUser():
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: schemas.User):
        db_user = models.User(
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
            user_adress=user.user_adress,
            phone=user.phone,
            cpf=user.cpf,
            cnpj=user.cnpj,
            email=user.email,           
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def list(self):
        users = self.db.query(models.User).all()
        return users
    
    def get(self, user_id: int):
        stat = select(models.User).filter_by(id=user_id)
        user = self.db.execute(stat).one()
        return user
    
    def remove(self, user_id: int):
        state = delete(models.User).where(models.User.id==user_id)
        
        self.db.execute(state)
        self.db.commit()