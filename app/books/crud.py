from sqlalchemy.orm import Session
from app.books.models import BookModel
from app.books.schemas import BookSchema


def get_book_by_title(db: Session, title: str):
    """
        Retrieve a book by its title from the database.

        Args:
            db (Session): Database session.
            title (str): Title of the book to retrieve.

        Returns:
            BookModel: Book model object if found, else None.
        """
    return db.query(BookModel).filter(BookModel.title == title).first()


def create_book(db: Session, book: BookSchema):
    """
        Create a new book in the database.

        Args:
            db (Session): Database session.
            book (BookSchema): Book data to be created.

        Returns:
            BookModel: Created book model object.
        """

    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 100):
    """
        Retrieve a list of books from the database with optional pagination.

        Args:
            db (Session): Database session.
            skip (int): Number of records to skip.
            limit (int): Maximum number of records to return.

        Returns:
            List[BookModel]: List of book model objects.
        """

    return db.query(BookModel).offset(skip).limit(limit).all()


def delete_book(db: Session, title: str):
    """
    Delete a book from the database by its title.

    Args:
        db (Session): Database session.
        title (str): Title of the book to delete.

    Returns:
        None
    """
    db.query(BookModel).filter(BookModel.title == title).delete()
    db.commit()


def update_book(db: Session, title: str, book_data: BookSchema):
    """
    Update a book in the database by its title.

    Args:
        db (Session): Database session.
        title (str): Title of the book to update.
        book_data (BookSchema): New data for the book.

    Returns:
        BookModel: Updated book model object.
    """
    db_book = db.query(BookModel).filter(BookModel.title == title).first()
    if db_book:
        for key, value in book_data.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    return None
