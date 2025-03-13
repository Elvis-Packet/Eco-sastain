# Eco-sastain
# EcoSustain Manager

EcoSustain Manager is a waste collection management system that helps manage collectors, log waste collection events, and generate reports.

## Features

- Manage collectors (add, update, delete)
- Log waste collection events
- View collection history
- Generate collector reports

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Elvis-Packet/Eco-sastain.git
    cd ecosustain_manager
    ```

2. Install dependencies using `pipenv`:
    ```bash
    pipenv install
    ```

3. Initialize the database:
    ```bash
    pipenv run python ecosustain/models.py // or just write python models.py
    ```

4. Seed the database with initial data:
    ```bash
    pipenv run python ecosustain/seed.py
    ```

## Usage

1. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

2. Run the CLI:
    ```bash
    python ecosustain/cli.py
    ```

## Alembic Migrations

1. Initialize Alembic:
    ```bash
    alembic init ecosustain/migration
    ```

2. Create a new migration:
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    ```

3. Apply migrations:
    ```bash
    alembic upgrade head
    ```

## Project Structure

- `ecosustain/models.py`: Defines the database models and initializes the database.
- `ecosustain/seed.py`: Seeds the database with initial data.
- `ecosustain/cli.py`: Provides a command-line interface for managing collectors and logging waste collection.
- `ecosustain/__init__.py`: Initializes the package. links the files of models and cli 
- `ecosustain/migration/`: Contains Alembic migration scripts.
- `ecosustain/alembic.ini`: Configuration file for Alembic.

# All done by @ Elvis 
