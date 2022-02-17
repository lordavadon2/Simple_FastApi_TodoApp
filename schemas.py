from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    password: str


class ResponseUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool


class ResponseTodo(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: int
    complete: bool

    class Config:
        orm_mode = True


class ResponseTodos(ResponseTodo):
    owner: ResponseUser

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
