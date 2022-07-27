
from sqlmodel import Session
from models.model_init import engine
from models.monitor_model import Logger_action


def loggerActionSeed():

    with Session(engine) as session:
        for i in ['create', 'update', 'cancel', 'delete']:
            action = Logger_action(action_name=i)
            session.add(action)
            session.commit()
            session.refresh(action)
