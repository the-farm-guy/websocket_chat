from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.model import Base

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()