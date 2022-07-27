from sqlmodel import Session, select  # type: ignore
from models.seed_migrate_model import Seed
from models.seeds.logger_action_seed_1 import loggerActionSeed

from models.model_init import engine


def seed():
    with Session(engine) as session:
        statement = select(Seed.version)
        result = session.exec(statement)
        r = result.first()
        print(r)
        if(not r):
            print("seeding")
            loggerActionSeed()

            with Session(engine) as s:
                v = Seed(version=1)
                s.add(v)
                s.commit()
                s.refresh(v)

    with Session(engine) as session:
        statement = select(Seed.version)
        result = session.exec(statement)
        v = result.first()

        if v == 1:
            print("seeding v 1")
            v = v + 1
            update_seed_version(v)

        if v == 2:
            print("seeding v 2")
            v = v + 1
            update_seed_version(v)

        if v == 3:
            print("seeding v 3")
            v = v + 1
            update_seed_version(v)


def update_seed_version(version: int):
    try:
        with Session(engine) as session:
            statement = select(Seed)
            result = session.exec(statement)
            seed = result.first()
            if seed is not None:
                seed.version = version
                session.add(seed)
                session.commit()
                session.refresh(seed)
    except:
        print("error on ", version)


if __name__ == "__main__":
    seed()
