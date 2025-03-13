from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

DATABASE_URL = "sqlite:///waste_management.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Collector(Base):
    __tablename__ = 'collectors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, )
    contact_info = Column(String)
    gender = Column(String)
    collection_logs = relationship('CollectionLog', back_populates='collector', lazy='joined')

class RecyclingCenter(Base):
    __tablename__ = 'recycling_centers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    collection_logs = relationship('CollectionLog', back_populates='recycling_center', lazy='joined')

class WasteItem(Base):
    __tablename__ = 'waste_items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    weight = Column(Float)
    collection_logs = relationship('CollectionLog', back_populates='waste_item', lazy='joined')

class CollectionLog(Base):
    __tablename__ = 'collection_logs'
    
    id = Column(Integer, primary_key=True)
    collector_id = Column(Integer, ForeignKey('collectors.id'))
    recycling_center_id = Column(Integer, ForeignKey('recycling_centers.id'))
    waste_item_id = Column(Integer, ForeignKey('waste_items.id'))
    collection_date = Column(DateTime, default=datetime.utcnow)

    collector = relationship('Collector', back_populates='collection_logs', lazy='joined')
    recycling_center = relationship('RecyclingCenter', back_populates='collection_logs', lazy='joined')
    waste_item = relationship('WasteItem', back_populates='collection_logs', lazy='joined')

def create_tables():
    Base.metadata.create_all(bind=engine)

def initialize_database():
    with SessionLocal() as db:
        if not db.query(Collector).first():
            db.add_all()
            db.commit()

if __name__ == "__main__":
    create_tables()
    initialize_database()
