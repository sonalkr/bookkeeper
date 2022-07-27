import os

from services.utils.gui_template_util import view


root_locaiton = os.path.dirname(__file__)
file_name = "button_component.qml"


def button_component():
    view(root_location=root_locaiton, file_name=file_name)
