from sqlalchemy import create_engine,text
import os
from sqlalchemy.orm import sessionmaker,declarative_base
from api.core.config import DATABASE_URL


engine = create_engine (DATABASE_URL,pool_pre_ping=True,pool_recycle=300)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




