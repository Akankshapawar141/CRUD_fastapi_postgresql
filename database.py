from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#('postgresql+psycopg2://user:password@hostname/database_name')
SQLALCHEMY_DATABASE_URL ="postgresql://postgres:postgresql@localhost/partner_svc"

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
