from pydantic import BaseModel, Field
import datetime

class BookBase(BaseModel):
    title: str = Field(
        title="The title of the book",
        min_length=1, max_length=26000
    )
    author: str = Field(
        title="The author of the book",
        min_length=1, max_length=1000,
        pattern=r'^[\w\.\,\s]*$'
    )
    published_year: int = Field(
        title="The publication year of the book",
        lt=datetime.date.today().year
    )

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: str | None = None

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
