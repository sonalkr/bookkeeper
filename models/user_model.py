
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String

from sqlmodel import Field, SQLModel  # type: ignore


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str = Field(sa_column=Column('user_name', String, unique=True))
    first_name: str
    middle_name: str
    last_name: str
    password: str
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
