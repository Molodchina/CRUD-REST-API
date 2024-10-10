from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLAlchemy models
class Book(Base):
    # Table name
    __tablename__ = 'books'

    # Book id
    id = Column(Integer, primary_key=True, index=True)

    # Book title
    title = Column(String, index=True)

    # Book author
    author = Column(String, index=True)

    # Book publication year
    published_year = Column(Integer, index=True)
