from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

DATABASE_PATH = os.path.join(PROJECT_ROOT, "nba.db")

engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)