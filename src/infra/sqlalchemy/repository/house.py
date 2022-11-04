from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryHouse():
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, house: schemas.House):
        db_house = models.House(name=house.name,
                                    type=house.type,
                                    size=house.size,
                                    product_adress=house.product_adress,
                                    bedroom=house.bedroom,
                                    restroom=house.restroom,
                                    furniture=house.furniture,
                                    available=house.available)
        self.db.add(db_house)
        self.db.commit()
        self.db.refresh(db_house)
        return db_house
    
    def list(self):
        houses = self.db.query(models.House).all()
        return houses
    
    def get(self, house_id: int):
        stat = select(models.House).filter_by(id=house_id)
        house = self.db.execute(stat).one()
        return house
    
    def remove(self, house_id: int):
        state = delete(models.House).where(models.House.id==house_id)
        
        self.db.execute(state)
        self.db.commit()