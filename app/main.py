from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse

from app.database import engine
from app.books.routes import router as book_router
from app.books.models import Base

app = FastAPI()

app.include_router(book_router)

Base.metadata.create_all(bind=engine)


# Open defaul home page for base URL
@app.get("/")
def home_page(request: Request):
    """
    This is a default page and will redirect to Swagger documentation Page
    :param request:
    :return:
    """
    return RedirectResponse(url="/docs")
    # return f"Paste this URL in browser for api details {str(request.url)+'docs'}"
