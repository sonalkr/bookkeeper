
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String

from sqlmodel import Field, SQLModel  # type: ignore


class Logger_action(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    action_name: str = Field(sa_column=Column(
        "action_name", String, unique=True, nullable=False))


class Log(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str
    action_id: int = Field(foreign_key="logger_action.id")
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
