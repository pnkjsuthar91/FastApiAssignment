from sqlalchemy import Boolean, Column, ForeignKey, Float, String, Integer

from app.database import Base


class BookModel(Base):
    """Model class representing a book in the database."""

    __tablename__ = "books"

    # Primary key for the BookModel table
    id = Column(Integer, primary_key=True, index=True)

    # Title of the book
    title = Column(String, index=True)

    # Author of the book
    author = Column(String, index=True)

    # Year of publication of the book
    year = Column(Integer)

    # Latitude coordinate of the book's location
    latitude = Column(Float)

    # Longitude coordinate of the book's location
    longitude = Column(Float)
