from gui.main_gui import gui
from models.model_init import create_db_and_tables
from models.seeds.seed import seed
from services.core.logger_service import createLoger


def main():
    create_db_and_tables()
    seed()
    createLoger("test")
    gui()


if __name__ == "__main__":
    main()
