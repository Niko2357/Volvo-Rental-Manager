import oracledb
import json
import os
import sys
from tkinter import messagebox


def resource_path():
    """
    Gets path to files for PyInstaller .exe to function correctly.
    :return: new path to file
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        return project_root


def get_connection():
    """
    Connects to database.
    :return: connection or None
    """
    try:
        base_path = resource_path()
        file_path = os.path.join(base_path, "config.json")
        with open(file_path, "r") as file:
            db_config = json.load(file)
            return oracledb.connect(user=db_config["user"], password=db_config["password"], dsn=db_config["dsn"])
    except FileNotFoundError:
        messagebox.showerror("Error", f"File config.json not found!")
        return None
    except Exception as e:
        messagebox.showerror("Connection Error", f"Detail:\n{str(e)}")
        return None
