from pydantic import BaseModel


class BookSchema(BaseModel):
    """
    Schema class for representing book data.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
        year (int): Year of publication of the book.
        latitude (float): Latitude coordinate of the book's location.
        longitude (float): Longitude coordinate of the book's location.
    """
    title: str
    author: str
    year: int
    latitude: float
    longitude: float
