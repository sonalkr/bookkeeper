
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel  # type: ignore


class Seed(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: int
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)


class Migrate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: int
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
