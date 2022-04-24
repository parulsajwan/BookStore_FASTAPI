import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from databases import Database
from database_config import SQLALCHEMY_DATABASE_URL

db = Database(SQLALCHEMY_DATABASE_URL)