# waste_management/__init__.py

# Expose key functionality from modules
from .models import Collector, CollectionLog, RecyclingCenter, WasteItem
from .cli import main

# Optional: Add a version for the package
__version__ = "1.0.0"

# Optional: Initialize the package (e.g., set up logging or database)
def initialize():
    print("Initializing waste_management package...")
    # Add any initialization code here