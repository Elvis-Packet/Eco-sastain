
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, sessionmaker, joinedload
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///waste_management.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Collector(Base):
    __tablename__ = 'collectors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    collection_logs = relationship('CollectionLog', back_populates='collector')

class RecyclingCenter(Base):
    __tablename__ = 'recycling_centers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    collection_logs = relationship('CollectionLog', back_populates='recycling_center')

class WasteItem(Base):
    __tablename__ = 'waste_items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    collection_logs = relationship('CollectionLog', back_populates='waste_item')

class CollectionLog(Base):
    __tablename__ = 'collection_logs'
    
    id = Column(Integer, primary_key=True)
    collector_id = Column(Integer, ForeignKey('collectors.id'), nullable=False)
    recycling_center_id = Column(Integer, ForeignKey('recycling_centers.id'), nullable=False)
    waste_item_id = Column(Integer, ForeignKey('waste_items.id'), nullable=False)
    collection_date = Column(DateTime, default=datetime.utcnow)
    
    # Relationships with explicit loading strategy
    collector = relationship('Collector', back_populates='collection_logs', lazy='joined')
    recycling_center = relationship('RecyclingCenter', back_populates='collection_logs', lazy='joined')
    waste_item = relationship('WasteItem', back_populates='collection_logs', lazy='joined')

def create_tables():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")

def get_db():
    """Database session generator for dependency injection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_database():
    """Initialize database with sample data"""
    db = SessionLocal()
    try:
        # Only add sample data if tables are empty
        if not db.query(Collector).first():
            default_collector = Collector(
                name="John Doe",
                contact_info="123-456-7890"
            )
            default_center = RecyclingCenter(
                name="Green Recycling",
                location="123 Green St"
            )
            default_waste = WasteItem(
                name="Plastic Bottle",
                category="Plastic",
                weight=0.5
            )
            
            db.add_all([default_collector, default_center, default_waste])
            db.commit()
            print("Initial sample data added")
    except Exception as e:
        db.rollback()
        print(f"Initialization error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    create_tables()
    initialize_database()