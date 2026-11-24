from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL="mysql+pymysql://root:root@localhost:3306/soriat"
enginee=create_engine(DB_URL)
session_lock=sessionmaker(autoflush=False,autocommit=False,bind=enginee)
base=declarative_base()
