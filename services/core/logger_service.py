

from sqlmodel import Session, select  # type: ignore
from models.model_init import engine
from models.monitor_model import Log, Logger_action


CREATE = "create"
UPDATE = "update"
DELETE = "delete"
CANCEL = "cancel"


def createLoger(message: str):
    log(action_id=get_action_id(CREATE), message=message)


def updateLoger(message: str):
    log(action_id=get_action_id(UPDATE), message=message)


def deleteLoger(message: str):
    log(action_id=get_action_id(DELETE), message=message)


def cancelLoger(message: str):
    log(action_id=get_action_id(CANCEL), message=message)


def log(action_id: int, message: str):
    if action_id is 0:
        print("database error : unable to find the id of action for logger")
        return
    with Session(engine) as session:
        log_entity = Log(action_id=action_id, message=message)
        session.add(log_entity)
        session.commit()
        session.refresh(log_entity)


def get_action_id(action_name: str) -> int:
    with Session(engine) as session:
        statement = select(Logger_action.id).where(
            Logger_action.action_name == action_name)
        result = session.exec(statement)
        action_id = result.first()

    if action_id is None:
        return 0

    return action_id
