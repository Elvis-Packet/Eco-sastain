from models import Collector, RecyclingCenter, WasteItem, CollectionLog, SessionLocal
from datetime import datetime
from faker import Faker
import random

fake = Faker()

def seed_database():
    db = SessionLocal()
    try:
        # Add collectors
        collectors = [
            Collector(name=fake.name(), contact_info=fake.phone_number()) for _ in range(100)
        ]
        db.add_all(collectors)
        db.commit()

        # Add recycling centers
        centers = [
            RecyclingCenter(name=fake.company(), location=fake.address()) for _ in range(50)
        ]
        db.add_all(centers)
        db.commit()

        # Add waste items
        waste_items = [
            WasteItem(name=fake.word(), category=random.choice(["Plastic", "Glass", "Metal", "Paper"]), weight=round(random.uniform(0.1, 5.0), 2)) for _ in range(20)
        ]
        db.add_all(waste_items)
        db.commit()

        # Add collection logs
        collection_logs = [
            CollectionLog(
                collector_id=random.choice(collectors).id,
                recycling_center_id=random.choice(centers).id,
                waste_item_id=random.choice(waste_items).id,
                collection_date=fake.date_time_this_year()
            ) for _ in range(50)
        ]
        db.add_all(collection_logs)
        db.commit()

        print("Database seeded successfully!")
    except Exception as e:
        db.rollback()
        print(f"Seeding error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
