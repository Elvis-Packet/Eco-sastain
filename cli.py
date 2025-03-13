import datetime
from models import Collector, WasteItem, RecyclingCenter, CollectionLog, SessionLocal

def display_menu():
    """Display the main menu options."""
    print("\n--- Waste Collection Management System ---")
    print("1. Manage Collectors")
    print("2. Log Waste Collection")
    print("3. View Collection History")
    print("4. Generate Collector Report")
    print("5. Exit")

# --- Helper Functions for Database Operations ---
def add_collector():
    """Adds a new collector to the database."""
    name = input("Enter collector name: ")
    contact = input("Enter contact info: ")
    db = SessionLocal()
    try:
        collector = Collector(name=name, contact_info=contact)
        db.add(collector)
        db.commit()
        print(f"Collector '{name}' added successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error: {str(e)}")
    finally:
        db.close()

def update_collector():
    """Updates an existing collector."""
    try:
        collector_id = int(input("Enter collector ID to update: "))
    except ValueError:
        print("Error: Collector ID must be an integer!")
        return

    db = SessionLocal()
    try:
        collector = db.get(Collector, collector_id)
        if collector:
            name = input(f"Enter new name (current: {collector.name}): ") or collector.name
            contact = input(f"Enter new contact info (current: {collector.contact_info}): ") or collector.contact_info
            collector.name = name
            collector.contact_info = contact
            db.commit()
            print(f"Collector ID {collector_id} updated successfully!")
        else:
            print(f"Collector ID {collector_id} not found.")
    except Exception as e:
        db.rollback()
        print(f"Error: {str(e)}")
    finally:
        db.close()

def delete_collector():
    """Deletes a collector from the database."""
    try:
        collector_id = int(input("Enter collector ID to delete: "))
    except ValueError:
        print("Error: Collector ID must be an integer!")
        return

    db = SessionLocal()
    try:
        collector = db.get(Collector, collector_id)
        if collector:
            db.delete(collector)
            db.commit()
            print(f"Collector ID {collector_id} deleted successfully!")
        else:
            print(f"Collector ID {collector_id} not found.")
    except Exception as e:
        db.rollback()
        print(f"Error: {str(e)}")
    finally:
        db.close()

def manage_collectors():
    """Submenu for managing collectors."""
    while True:
        print("\n--- Manage Collectors ---")
        print("1. Add Collector")
        print("2. Update Collector")
        print("3. Delete Collector")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_collector()
        elif choice == "2":
            update_collector()
        elif choice == "3":
            delete_collector()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def view_collection_history():
    """Displays the waste collection history."""
    print("\n--- Collection History ---")
    db = SessionLocal()
    try:
        logs = db.query(CollectionLog).all()
        if not logs:
            print("No collection history found.")
            return

        for log in logs:
            print(f"Collector ID: {log.collector_id}, Waste Item ID: {log.waste_item_id}, "
                  f"Recycling Center ID: {log.recycling_center_id}, Date: {log.collection_date}")
    except Exception as e:
        print(f"Error retrieving collection history: {e}")
    finally:
        db.close()

def generate_collector_report():
    """Generates a report of all collectors."""
    print("\n--- Collector Report ---")
    db = SessionLocal()
    try:
        collectors = db.query(Collector).all()
        if not collectors:
            print("No collectors found.")
            return

        for collector in collectors:
            print(f"Collector ID: {collector.id}, Name: {collector.name}, Contact: {collector.contact_info}")
    except Exception as e:
        print(f"Error generating collector report: {e}")
    finally:
        db.close()

def log_waste_collection():
    """Logs a waste collection event."""
    print("\n--- Log Waste Collection ---")
    db = SessionLocal()
    try:
        collector_id = int(input("Enter collector ID: "))
        waste_item_id = int(input("Enter waste item ID: "))
        recycling_center_id = int(input("Enter recycling center ID: "))

        collector = db.get(Collector, collector_id)
        waste_item = db.get(WasteItem, waste_item_id)
        recycling_center = db.get(RecyclingCenter, recycling_center_id)

        if not collector or not waste_item or not recycling_center:
            print("Error: One or more IDs are invalid!")
            return

        collection_date = datetime.datetime.now()
        new_log = CollectionLog(
            collector_id=collector_id,
            waste_item_id=waste_item_id,
            recycling_center_id=recycling_center_id,
            collection_date=collection_date
        )
        db.add(new_log)
        db.commit()
        print("Collection logged successfully!")
    except ValueError:
        print("Error: IDs must be integers!")
    except Exception as e:
        db.rollback()
        print(f"Error logging waste collection: {e}")
    finally:
        db.close()

def main():
    """Main menu loop."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_collectors()
        elif choice == "2":
            log_waste_collection()
        elif choice == "3":
            view_collection_history()
        elif choice == "4":
            generate_collector_report()
        elif choice == "5":
            print("Exiting ADIOS .KEEP IT CLEAN !")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
