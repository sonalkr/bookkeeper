from sqlmodel import SQLModel, create_engine

from models.core_model import Account, Voucher_type, Voucher, Transaction  # type: ignore
from models.monitor_model import Log, Logger_action  # type: ignore
from models.seed_migrate_model import Migrate, Seed  # type: ignore
from models.user_model import User  # type: ignore


SQLITE_FILE_NAME = "data/database.sqlite"
sqlite_url = f"sqlite:///{SQLITE_FILE_NAME}"

engine = create_engine(sqlite_url)
# engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
