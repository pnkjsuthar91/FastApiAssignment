from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.books.schemas import BookSchema
from app.books import crud
from app.database import SessionLocal


# Dependency to get a database session
def get_db():
    """
    Dependency to get a database session.
    Yields:
        Session: SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/books",
    tags=["items"],  # Tags help organize API documentation
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=BookSchema)
def create_book(book: BookSchema, db: Session = Depends(get_db)):
    """
    Create a new book in the database.

    Args:
        book (BookSchema): Book data to be created.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        BookSchema: Created book data.

    Raises:
        HTTPException: If a book with the same title already exists.
    """
    db_user = crud.get_book_by_title(db, title=book.title)
    if db_user:
        raise HTTPException(status_code=400, detail="Title already given.")
    return crud.create_book(db=db, book=book)


@router.get("/", response_model=list[BookSchema])
def fetch_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Fetch a list of books from the database.

    Args:
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        list[BookSchema]: List of book data.
    """
    return crud.get_books(db, skip=skip, limit=limit)
    # return users


@router.put("/{title}", response_model=BookSchema)
def update_book(title: str, book: BookSchema, db: Session = Depends(get_db)):
    """
    Update an existing book in the database.

    Args:
        title (str): Title of the book to update.
        book (BookSchema): Updated book data.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        BookSchema: Updated book data.

    Raises:
        HTTPException: If the book with the given title does not exist.
    """
    db_book = crud.get_book_by_title(db, title=title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db=db, title=title, book_data=book)


# Endpoint to delete a book
@router.delete("/{title}")
def delete_book(title: str, db: Session = Depends(get_db)):
    """
    Delete a book from the database.

    Args:
        title (str): Title of the book to delete.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        dict: Message confirming deletion.

    Raises:
        HTTPException: If the book with the given title does not exist.
    """
    db_book = crud.get_book_by_title(db, title=title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db=db, title=title)
    return {"message": "Book deleted successfully"}
