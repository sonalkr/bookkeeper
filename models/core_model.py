from datetime import datetime
from typing import Optional
from pydantic import condecimal
from sqlalchemy import Column, String

from sqlmodel import Date, Field, SQLModel  # type: ignore


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account_name: str = Field(sa_column=Column(
        'account_name', String, unique=True, nullable=False))
    opening_dr: condecimal(max_digits=20, decimal_places=4)  # type: ignore
    opening_cr: condecimal(max_digits=20, decimal_places=4)  # type: ignore
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)


class Voucher_type(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    voucher_type_name: str = Field(sa_column=Column(
        'voucher_type_name', String, unique=True, nullable=False))
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)


class Voucher(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    voucher_name: str = Field(sa_column=Column(
        'voucher_name', String, unique=True, nullable=False))
    voucher_number: str
    voucher_type_id: int = Field(foreign_key="voucher_type.id")
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    _date: Date
    voucher_id: int = Field(foreign_key="voucher.id")
    account_id: int = Field(foreign_key="account.id")
    amount_dr: condecimal(max_digits=20, decimal_places=4)  # type: ignore
    amount_cr: condecimal(max_digits=20, decimal_places=4)  # type: ignore
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
